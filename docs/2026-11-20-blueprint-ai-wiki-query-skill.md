# Blueprint: skill `ai-wiki-query`

Een skill waarmee een AI-agent vragen beantwoordt op basis van de gepubliceerde ai-wiki op
<https://businessdatasolutions.github.io/ai-wiki/>, met een bronvermelding bij elke bewering.

**Zo gebruik je dit document.** Geef het in zijn geheel aan je agent (Claude Code of een vergelijkbare
agent met shell- en internettoegang) met de opdracht:

> Bouw de skill die deze blueprint beschrijft. Neem het script uit bijlage A ongewijzigd over, schrijf
> `SKILL.md` volgens §4 en §5, en draai daarna de zes acceptatietests uit §7. Rapporteer per test of hij
> slaagt.

Het document beschrijft de eindtoestand: wat de skill doet en waaraan je ziet dat hij werkt. De volgorde
van bouwen kiest de agent zelf.

---

## 1. Doel

De skill beantwoordt een vraag uitsluitend met inhoud van de ai-wiki op
`https://businessdatasolutions.github.io/ai-wiki/`. Elke inhoudelijke bewering in het antwoord verwijst
naar minstens één URL van die site, en de skill slaagt voor 6 van de 6 acceptatietests in §7.

Elke eis in §5 dient dit doel. Een eis die je er niet aan kunt koppelen, hoort er niet in.

---

## 2. De wiki in het kort

Gecontroleerd op 2026-11-20 tegen de live site.

- **Wat het is.** Een persoonlijke kenniswiki over AI: agents en agent-engineering, adoptie van AI in
  organisaties, effecten op werk en arbeidsmarkt, digitale transformatie en strategie. Een LLM bouwt en
  onderhoudt de wiki uit bronnen die de eigenaar verzamelt (papers, rapporten, video's, artikelen).
  Ze is in het **Engels** geschreven en wordt gepubliceerd met [Quartz](https://quartz.jzhao.xyz/) op
  GitHub Pages. Na elke wijziging wordt de site opnieuw gebouwd.
- **Omvang.** 723 pagina's: 432 sources, 219 entities, 55 concepts, 9 threads, 6 syntheses, plus de
  catalogus (`index`) en het logboek (`log`).
- **Paginatypes en hun gewicht bij het beantwoorden:**

  | Type | Map | Wat erin staat | Gebruik |
  | --- | --- | --- | --- |
  | synthesis | `syntheses/` | Eindconclusie op een onderzoeksvraag, met secties Question, Findings, Sources consulted, Lessons, Open questions | Eerste keus als de vraag al eens beantwoord is |
  | concept | `concepts/` | Een begrip, opgebouwd uit veel bronnen, met een sectie *Debates and supersession* waarin tegenstrijdigheden staan | Eerste keus voor "wat is X" en "wat weten we over X" |
  | source | `sources/` | Samenvatting van één bron (paper, video, rapport), met cijfers en citaten | Voor concrete cijfers, quotes en casussen |
  | entity | `entities/` | Kaartje van een persoon, organisatie of product | Alleen voor "wie/wat is X" |
  | thread | `threads/` | Open of gesloten onderzoeksvraag | Gesloten threads zijn vervangen door hun synthesis |

- **Betrouwbaarheidssignalen.** Concept-, entity- en synthesis-pagina's tonen onder de titel een regel als
  `Confidence 0.95 · 156 sources · last confirmed 2026-11-16`. Een verouderde pagina krijgt bovenaan een
  waarschuwing met een link naar de opvolger. Op 2026-11-20 had geen enkele pagina die markering.
- **Pagina's zijn lang.** De mediaan is 8.260 tekens. 85 pagina's zijn langer dan 20.000 tekens, de
  grootste concept-pagina (`concepts/agent-harness`) telt 196.371 tekens.

---

## 3. Wat de site levert

De site heeft geen API, maar Quartz publiceert een volledige zoekindex. Die is de kern van de skill.

| Endpoint (achter `https://businessdatasolutions.github.io/ai-wiki`) | Inhoud | Grootte (2026-11-20) | Rol in de skill |
| --- | --- | --- | --- |
| `/static/contentIndex.json` | JSON-object `slug → {slug, filePath, title, tags, links, content}` voor alle 723 pagina's | 11,1 MB | Zoekcorpus én linkgraaf |
| `/<slug>` | De gerenderde HTML-pagina | 30–450 kB | Confidence-regel, verouderd-markering, sectie-ankers |
| `/sitemap.xml` | Alle pagina-URL's met `lastmod` | 127 kB | Vindplaats van pagina's als het script niet kan draaien |
| `/concepts/`, `/syntheses/` | Mapoverzicht met alle pagina's van dat type | 85 kB / 30 kB | Startpunt als het script niet kan draaien |
| `/` | De catalogus | 1,4 MB HTML | Te groot om in één keer op te halen |

Eigenschappen waar een implementatie op moet rekenen:

- **Titel.** Het veld `title` bevat vaak alleen de bestandsnaam (`agent-harness`). De echte titel is de
  eerste regel van `content` (`Agent Harness`).
- **Tekst.** `content` is platte tekst van de hele pagina. Koppen staan als losse regels, zonder `#`.
  HTML-entiteiten blijven staan (`&amp;`), dus decodeer ze voor weergave.
- **Links.** `links` bevat de uitgaande interne links als slugs. Backlinks vind je door de lijst om te
  keren.
- **URL's.** URL = basis + `/` + slug. Hoofdletters blijven staan, spaties worden koppeltekens:
  `entities/Erik-Brynjolfsson`. Een slug met `.md` erachter geeft een 404.
- **Sectie-ankers.** Koppen in de HTML hebben een id, bijvoorbeeld `<h2 id="findings">`. Je kunt dus
  linken naar `<url>#findings`.
- **Confidence-regel.** In de HTML staat
  `<p class="confidence-badge"><em>Confidence 0.90 · 8 sources · last confirmed 2026-05-29</em></p>`.
  Deze regel staat **niet** in `contentIndex.json`.
- **Verouderd.** Een verouderde pagina bevat de tekst `This page is preserved for history`.
- **Caching.** De index heeft een `ETag` en `Last-Modified`, en `cache-control: max-age=600`. Met
  `If-None-Match` krijg je een `304` als er niets veranderd is.

---

## 4. Architectuur

```
ai-wiki-query/
├── SKILL.md               triggerbeschrijving en werkwijze (§4.2)
└── scripts/
    └── wiki_search.py     zoeken, lezen, links, meta (bijlage A)

cache (buiten de skill):   ~/.cache/ai-wiki/contentIndex.json + meta.json
```

Voor Claude Code staat de map in `~/.claude/skills/ai-wiki-query/`. Het script gebruikt alleen de
standaardbibliotheek van Python 3.8 of hoger.

### 4.1 Twee toegangsroutes

- **Route A (standaard).** De agent heeft een shell en internet. Het script downloadt de index één keer,
  bewaart hem in de cache en doet zoeken, lezen en links lokaal. Zo kost één zoekvraag geen 11 MB aan
  context.
- **Route B (terugval).** De agent kan alleen losse webpagina's ophalen, bijvoorbeeld omdat de omgeving
  geen netwerk voor scripts heeft. De agent start dan bij `/concepts/` of `/syntheses/`, of zoekt slugs in
  `/sitemap.xml`, haalt losse pagina's op en volgt hun links. Lange pagina's worden daarbij mogelijk
  afgekapt.

### 4.2 Werkwijze bij een vraag

`SKILL.md` beschrijft deze stappen. De verwijzingen tussen haken wijzen naar de eisen in §5.

1. **Inkaderen.** Herformuleer de vraag in één zin en splits hem in 2 tot 4 deelvragen (facetten).
   Noteer de taal van de vraag.
2. **Zoektermen maken.** Maak 2 tot 4 **Engelse** zoekopdrachten: per facet één, of synoniemen van de
   kernterm ([ZK-1](#zk-1), [ZK-2](#zk-2)).
3. **Zoeken.** Draai één keer
   `python3 scripts/wiki_search.py search "<q1>" "<q2>" ... -n 10`.
   Het resultaat bestaat uit twee blokken: zoektreffers en linkburen ([ZK-3](#zk-3)).
4. **Schiften.** Geef elke kandidaat USE of IGNORE, met een reden bij elke IGNORE ([TR-1](#tr-1)).
   Houd 3 tot 8 pagina's over ([TR-2](#tr-2)).
5. **Lezen.** Lees de USE-pagina's met `read <slug>`, of bij lange pagina's met
   `read <slug> --around "<term>"` ([LZ-1](#lz-1)). Haal voor concepts en syntheses de confidence-regel en
   de sectie-ankers op met `meta <slug>` ([LZ-2](#lz-2)).
6. **Gaten dichten (hoogstens één ronde).** Blijft een facet onbeantwoord, zoek dan één keer opnieuw met
   andere termen, of volg met `links <slug>` de links van een sterke USE-pagina.
7. **Antwoorden.** Schrijf het antwoord in de taal van de vraag, met een anker `[W1]`, `[W2]`, ... bij
   elke bewering en daaronder de bronnenlijst met URL's ([AN-1](#an-1) t/m [AN-6](#an-6)).
8. **Spoor tonen.** Sluit af met een kort zoekspoor ([SP-1](#sp-1)).

### 4.3 Commando's van het script

```sh
python3 scripts/wiki_search.py search "agent harness" "harness engineering runtime" -n 10
python3 scripts/wiki_search.py search "dynamic capabilities" -n 8 --hops 0      # zonder linkburen
python3 scripts/wiki_search.py search "is RAG dead" --json                       # machineleesbaar
python3 scripts/wiki_search.py read syntheses/is-rag-dead                        # max 20.000 tekens
python3 scripts/wiki_search.py read concepts/agent-harness --around "working definition" --window 1500
python3 scripts/wiki_search.py links syntheses/is-rag-dead                       # uitgaand + backlinks
python3 scripts/wiki_search.py meta syntheses/is-rag-dead                        # confidence, ankers
python3 scripts/wiki_search.py --refresh search "..."                            # cache negeren
```

Hoe het zoeken werkt: per zoekopdracht BM25 over titel (gewicht 3), tags (2) en tekst (1), met een
bonus voor de exacte woordgroep. Daarna een lichte voorkeur per paginatype (synthesis 1,3; concept 1,2;
source en thread 1,0; entity 0,8). Vervolgens worden de rangen van alle zoekopdrachten samengevoegd met
Reciprocal Rank Fusion (k = 60). `index` en `log` worden overgeslagen, omdat ze alles noemen en daardoor op
elke zoekterm scoren.

---

## 5. Eisen

**Prioriteit** volgt MoSCoW: **M** = Must, **S** = Should, **C** = Could. **Verificatie**: T = test,
D = demonstratie, I = inspectie, A = analyse.

### 5.1 Toegang en bron (TG)

| ID | Eis | Prio | Criterium | Verificatie |
| --- | --- | --- | --- | --- |
| <a id="tg-1"></a>TG-1 | De skill gebruikt als inhoudelijke bron alleen pagina's onder `https://businessdatasolutions.github.io/ai-wiki/`. | M | 100 % van de geciteerde URL's begint met die basis, in alle 6 testantwoorden. | I |
| <a id="tg-2"></a>TG-2 | Als de gecachete index langer dan 6 uur niet is gecontroleerd, controleert het script hem opnieuw met een `If-None-Match`-verzoek. | M | Een run binnen 6 uur doet 0 HTTP-verzoeken. Een run na 6 uur met ongewijzigde ETag downloadt 0 bytes index (HTTP 304, bestandsdatum van de cache blijft gelijk). | T |
| <a id="tg-3"></a>TG-3 | Als de site onbereikbaar is en er een cache bestaat, gebruikt het script de cache en meldt het dat. | S | Exitcode 0 en 1 waarschuwingsregel op stderr, met het netwerk uit. | T |
| <a id="tg-4"></a>TG-4 | De skill schrijft niets naar de wiki of naar de repository erachter. | M | 0 andere HTTP-methoden dan GET in de code. | I |
| <a id="tg-5"></a>TG-5 | Als het script niet kan draaien, beantwoordt de skill de vraag via route B (§4.1). | S | Test 1 levert zonder het script een antwoord met minstens 1 geciteerde wiki-URL. | D |
| <a id="sk-1"></a>SK-1 | De frontmatter van `SKILL.md` heeft `name: ai-wiki-query` en een `description` die de triggers noemt: vragen aan "de ai-wiki", "de wiki van businessdatasolutions", of een vraag over AI-adoptie, agents of AI en werk waarbij de gebruiker om de wiki vraagt. | M | De skill start bij 3 van 3 voorbeeldprompts: "Wat zegt de ai-wiki over agent harnesses?", "Zoek in de wiki wat er bekend is over AI en jonge werknemers", "/ai-wiki-query jagged frontier". | D |

### 5.2 Zoeken (ZK)

| ID | Eis | Prio | Criterium | Verificatie |
| --- | --- | --- | --- | --- |
| <a id="zk-1"></a>ZK-1 | Als de vraag niet in het Engels is, vertaalt de agent hem naar Engelse zoekopdrachten voordat hij zoekt. | M | Test 3 (Nederlandse vraag) citeert `concepts/dynamic-capabilities`. Ter controle: de zoekopdracht `"dynamische capaciteiten"` gaf op 2026-11-20 0 treffers. | T |
| <a id="zk-2"></a>ZK-2 | De agent geeft per zoekronde 2 tot 4 zoekopdrachten mee aan één `search`-aanroep. | M | Het veld `queries` van de ledger telt 2–4 items, in elk van de 6 tests. | I |
| <a id="zk-3"></a>ZK-3 | `search` geeft naast de zoektreffers apart de linkburen (één stap in de linkgraaf), gerangschikt op het aantal treffers waarmee ze verbonden zijn. | S | `search "agent harness" -n 8` geeft minstens 1 linkbuur met `seed_count` ≥ 2. | T |
| <a id="zk-4"></a>ZK-4 | `search` laat de pagina's `index` en `log` weg. | M | 0 keer `index` of `log` in de ledgers van de 6 tests. | T |

### 5.3 Schiften (TR)

| ID | Eis | Prio | Criterium | Verificatie |
| --- | --- | --- | --- | --- |
| <a id="tr-1"></a>TR-1 | De agent geeft elke kandidaat het oordeel USE of IGNORE. Elke IGNORE krijgt één reden uit deze lijst: `off-facet` (beantwoordt geen facet), `redundant` (zegt hetzelfde als een sterkere pagina), `superseded` (verouderd, opvolger aanwezig), `wrong-granularity` (entity-kaartje waar een cijfer of claim nodig is), `below-threshold` (zwakke treffer, geen facet heeft hem nodig). | M | 100 % van de kandidaten in het spoor heeft een oordeel, 100 % van de IGNORE's een reden uit de lijst. | I |
| <a id="tr-2"></a>TR-2 | De USE-set telt 3 tot 8 pagina's. | S | 3 ≤ aantal USE ≤ 8 in test 1 t/m 5. | I |
| <a id="tr-3"></a>TR-3 | Bij gelijke relevantie kiest de agent eerst een synthesis, dan een concept, dan een source, dan een entity. Een gesloten thread geldt als `redundant` naast zijn synthesis. | S | In test 2 is `syntheses/is-rag-dead` USE en `threads/is-rag-dead` IGNORE (`redundant`) of afwezig. | T |
| <a id="tr-4"></a>TR-4 | Als een pagina als verouderd gemarkeerd is, gebruikt de agent haar niet als enige steun voor een bewering. | M | 0 beweringen die alleen op een verouderde pagina rusten. `meta` meldt `stale: true` op een pagina met de tekst uit §3. | A |

### 5.4 Lezen (LZ)

| ID | Eis | Prio | Criterium | Verificatie |
| --- | --- | --- | --- | --- |
| <a id="lz-1"></a>LZ-1 | Als een pagina langer is dan 20.000 tekens, leest de agent alleen vensters rond zoektermen (`read --around`). | M | Geen enkele `read`-uitvoer is langer dan 20.000 tekens in test 4 (`concepts/agent-harness`, 196.371 tekens). | T |
| <a id="lz-2"></a>LZ-2 | Voor elke concept- en synthesis-pagina in de USE-set haalt de agent de confidence-regel op met `meta`. | S | Het spoor toont de confidence-regel bij 100 % van de USE-concepts en -syntheses. | I |
| <a id="lz-3"></a>LZ-3 | Als een USE-concept een sectie *Debates and supersession* heeft, leest de agent die sectie en noemt hij tegenstrijdigheden die de vraag raken. | S | De sectie is gelezen bij 100 % van de USE-concepts die haar hebben (zichtbaar in het spoor als `read --around "Debates and supersession"`). | I |

### 5.5 Antwoord (AN)

| ID | Eis | Prio | Criterium | Verificatie |
| --- | --- | --- | --- | --- |
| <a id="an-1"></a>AN-1 | De skill antwoordt in de taal van de vraag. Citaten uit de wiki blijven Engels. | M | Het antwoord op test 3 is Nederlands. | I |
| <a id="an-2"></a>AN-2 | Elke inhoudelijke bewering draagt een anker `[W#]` dat verwijst naar een URL in de bronnenlijst onder het antwoord. | M | 100 % van de zinnen met een feitelijke bewering heeft minstens 1 anker. 100 % van de ankers staat in de bronnenlijst. | I |
| <a id="an-3"></a>AN-3 | Een anker linkt naar de sectie waar de bewering staat (`<url>#<anker>` uit `meta`). | S | Minstens 50 % van de ankers bevat een sectie-anker, in test 1 t/m 5. | I |
| <a id="an-4"></a>AN-4 | Als de wiki de vraag niet dekt, zegt de skill dat en citeert hij geen pagina's als steun. | M | Test 6 geeft 0 wiki-citaten als steun en een zin die zegt dat de wiki dit onderwerp niet behandelt. | T |
| <a id="an-5"></a>AN-5 | Kennis van buiten de wiki staat apart en is gemarkeerd als "buiten de wiki". | M | 0 ongemarkeerde beweringen van buiten de wiki in de 6 testantwoorden. | I |
| <a id="an-6"></a>AN-6 | Facetten zonder USE-pagina noemt de skill onder een kopje "Wat de wiki niet zegt". | S | Elk onbeantwoord facet uit stap 1 staat onder dat kopje. | I |

### 5.6 Spoor (SP)

| ID | Eis | Prio | Criterium | Verificatie |
| --- | --- | --- | --- | --- |
| <a id="sp-1"></a>SP-1 | Onder het antwoord staat een zoekspoor met: de herformuleerde vraag, de facetten, de zoekopdrachten, de USE-pagina's met URL, de IGNORE-pagina's met reden. | S | Alle 5 onderdelen aanwezig, in test 1 t/m 5. | I |
| <a id="sp-2"></a>SP-2 | Op verzoek bewaart de skill antwoord en spoor als `<JJJJ-MM-DD>-<slug>-trace.md` in de werkmap. | C | Het bestand bestaat en bevat het antwoord plus de 5 onderdelen van SP-1. | D |

### 5.7 Prestatie (PR)

| ID | Eis | Prio | Criterium | Verificatie |
| --- | --- | --- | --- | --- |
| <a id="pr-1"></a>PR-1 | Met een gevulde cache is een `search`-aanroep binnen 5 seconden klaar. | S | ≤ 5 s wandkloktijd. Gemeten op 2026-11-20 op een laptop: 1,9 s. | T |
| <a id="pr-2"></a>PR-2 | Een volledig antwoord kost hoogstens 25 tool-aanroepen. | S | ≤ 25 aanroepen in test 1 t/m 5. | D |

---

## 6. Wat de skill bewust niet doet

- **Niets terugschrijven.** De wiki houdt lokaal bij welke pagina's gelezen worden (`accessed_at`). Dat
  mechanisme draait bij de eigenaar en bestaat niet op de site. De skill leest alleen.
- **Geen embeddings of vectorzoeken.** De eigenaar gebruikt lokaal `qmd` (BM25 plus vectoren). Online is
  er alleen de tekstindex. De agent vervangt het semantische deel door zelf Engelse zoektermen en
  synoniemen te kiezen.
- **Geen algemeen webzoeken** om gaten te vullen. Wat de wiki niet zegt, benoemt de skill als gat.
- **Geen andere sites of wiki's** als bron.
- **De catalogus (`/`) niet in zijn geheel ophalen.** Met 1,4 MB is hij te groot. De zoekindex dekt
  dezelfde pagina's.

### Ontwerpkeuzes die bij het testen ontstonden

- **Typevoorkeur vóór het samenvoegen.** In een eerdere versie werd de voorkeur per paginatype ná de
  Reciprocal Rank Fusion toegepast. Omdat RRF alleen naar rangen kijkt (1/61 tegen 1/65 scheelt 6 %),
  won de typevoorkeur (20 %) het dan van de relevantie. Een zwak concept versloeg zo de bron die precies
  over het onderwerp ging. De voorkeur zit daarom in de BM25-score, vóór de rangschikking.
- **BM25 vindt altijd iets.** De zoekopdracht `"pea soup recipe"` gaf op 2026-11-20 drie bronnen over
  robotdata en AI-agents. Het script kan dus niet beslissen dat een onderwerp ontbreekt. Dat oordeel ligt
  bij de agent ([AN-4](#an-4), test 6).
- **Linkburen apart tonen.** Hun score is een telling (met hoeveel treffers verbonden), geen relevantie.
  Ze in één lijst met de treffers zetten maakte de volgorde misleidend.

---

## 7. Acceptatietests

Gecontroleerd op 2026-11-20: de verwachte pagina's bestaan en komen bij de gegeven zoektermen in de top 5.
De wiki groeit, dus er kunnen sterkere pagina's bij komen. Een test slaagt zolang de verwachte pagina's in
de USE-set zitten.

| # | Vraag | Verwacht | Toetst |
| --- | --- | --- | --- |
| 1 | Wat zegt de wiki over het effect van AI op de werkgelegenheid van jonge werknemers? | USE bevat `sources/2026-04-28-brynjolfsson-canaries-coal-mine` en `concepts/ai-employment-effects` | ZK-2, TR-2, AN-2, AN-3 |
| 2 | Is RAG dood? | USE bevat `syntheses/is-rag-dead`. `threads/is-rag-dead` is IGNORE of afwezig | TR-3 |
| 3 | Wat zijn dynamische capaciteiten en hoe hangen ze samen met digitale transformatie? | USE bevat `concepts/dynamic-capabilities` en `sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation`. Antwoord in het Nederlands | ZK-1, AN-1 |
| 4 | Hoe definieert de wiki een agent harness, en uit welke onderdelen bestaat die? | USE bevat `concepts/agent-harness`, gelezen via `--around` (sectie *Working definition*) | LZ-1, LZ-2 |
| 5 | Wat is de jagged frontier en waar komt het begrip vandaan? | USE bevat `concepts/jagged-frontier` en `sources/2026-04-28-dellacqua-jagged-technological-frontier`. De sectie *Debates and supersession* van het concept is gelezen | LZ-2, LZ-3 |
| 6 | Wat is een goed recept voor erwtensoep? | Geen wiki-citaten als steun. Het antwoord zegt dat de wiki dit niet behandelt | AN-4, AN-5 |

Daarnaast, voor het script:

- [TG-2](#tg-2): draai twee keer `search` kort na elkaar en controleer dat de tweede run niets downloadt.
  Zet daarna `checked` in `~/.cache/ai-wiki/meta.json` op `0`, draai opnieuw en controleer dat de
  bestandsdatum van `contentIndex.json` gelijk blijft.
- [ZK-3](#zk-3): `search "agent harness" -n 8` toont onder "link neighbours" minstens één regel met
  `2 seeds` of meer.
- [PR-1](#pr-1): `time python3 scripts/wiki_search.py search "agent harness"` blijft onder 5 s.

---

## Bijlage A: `scripts/wiki_search.py`

Referentie-implementatie, op 2026-11-20 getest tegen de live site (alle commando's in §4.3, de
cacheherbevestiging met HTTP 304, het terugvallen op de cache zonder netwerk en het geval zonder
treffers). Alleen de standaardbibliotheek. Zet de
cachemap desgewenst ergens anders met de omgevingsvariabele `AI_WIKI_CACHE`.

```python
#!/usr/bin/env python3
"""Search the published ai-wiki (Quartz site) without a local copy.

Downloads the site's full-text index once (static/contentIndex.json), caches it,
and offers three commands:

  search  "<query>" ["<query>" ...]   ranked candidate ledger (BM25 per query, RRF across queries,
                                      plus one hop of link neighbours)
  read    <slug> [--around TERM]     page text, or only the windows around TERM
  links   <slug>                     outgoing links and backlinks of a page
  meta    <slug>                     from the rendered page: confidence badge, stale flag, section anchors

Standard library only. Python 3.8+.
"""
import argparse, html, json, math, os, re, sys, time, urllib.request, urllib.error
from collections import Counter, defaultdict

BASE = "https://businessdatasolutions.github.io/ai-wiki"
INDEX_URL = BASE + "/static/contentIndex.json"
CACHE_DIR = os.path.expanduser(os.environ.get("AI_WIKI_CACHE", "~/.cache/ai-wiki"))
CACHE = os.path.join(CACHE_DIR, "contentIndex.json")
META = os.path.join(CACHE_DIR, "meta.json")
MAX_AGE_S = 6 * 3600          # re-validate the cache after 6 hours
EXCLUDE = {"index", "log"}    # catalogue pages: they mention everything, so they rank on everything
TYPE_PRIOR = {"syntheses": 1.3, "concepts": 1.2, "threads": 1.0, "sources": 1.0, "entities": 0.8}
STOP = set("""a an the and or of to in on for with by from at as is are was were be been it its this that
these those what which who how why when where does do did can could should would about into than then
de het een en of van in op voor met door uit aan als is zijn was waren wat welke wie hoe waarom wanneer
waar wordt worden over naar dan bij ook niet die dat deze dit""".split())
K1, B_, K_RRF = 1.2, 0.75, 60


def tokens(text):
    return [t for t in re.findall(r"[a-z0-9][a-z0-9.\-]*[a-z0-9]|[a-z0-9]", text.lower()) if t not in STOP]


def url_of(slug):
    return f"{BASE}/{slug}"


def load_index(refresh=False):
    """Return the parsed index; download or re-validate with the stored ETag when stale."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    meta = json.load(open(META)) if os.path.exists(META) else {}
    fresh = os.path.exists(CACHE) and time.time() - meta.get("checked", 0) < MAX_AGE_S
    if refresh or not fresh:
        req = urllib.request.Request(INDEX_URL, headers={"User-Agent": "ai-wiki-query-skill"})
        if os.path.exists(CACHE) and meta.get("etag") and not refresh:
            req.add_header("If-None-Match", meta["etag"])
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                open(CACHE, "wb").write(data)
                meta = {"etag": r.headers.get("ETag"), "last_modified": r.headers.get("Last-Modified")}
        except urllib.error.HTTPError as e:
            if e.code != 304:
                if not os.path.exists(CACHE):
                    sys.exit(f"{INDEX_URL}: HTTP {e.code} and no cache exists")
                print(f"warning: HTTP {e.code}, using cached index", file=sys.stderr)
        except urllib.error.URLError as e:
            if not os.path.exists(CACHE):
                sys.exit(f"cannot reach {INDEX_URL} and no cache exists: {e}")
            print(f"warning: offline, using cached index ({e})", file=sys.stderr)
        meta["checked"] = time.time()
        json.dump(meta, open(META, "w"))
    return json.load(open(CACHE, encoding="utf-8")), meta


def page_title(page):
    """The H1 is the first line of `content`; the `title` field is often just the filename."""
    first = (page.get("content") or "").split("\n", 1)[0].strip()
    return html.unescape(first or page.get("title") or page["slug"])


def build(index):
    docs = {}
    for slug, p in index.items():
        if slug in EXCLUDE:
            continue
        title = page_title(p)
        tags = " ".join(t for t in p.get("tags", []) if not t.startswith(("type/", "kind/")))
        toks = tokens(title) * 3 + tokens(tags.replace("-", " ")) * 2 + tokens(p.get("content", ""))
        docs[slug] = {"tf": Counter(toks), "len": len(toks), "title": title, "p": p}
    df = Counter()
    for d in docs.values():
        df.update(d["tf"].keys())
    avg = sum(d["len"] for d in docs.values()) / max(len(docs), 1)
    back = defaultdict(set)
    for slug, p in index.items():
        for t in p.get("links", []):
            back[t].add(slug)
    return docs, df, avg, back


def bm25(query, docs, df, avg):
    q = tokens(query)
    n = len(docs)
    scores = {}
    for slug, d in docs.items():
        s = 0.0
        for t in q:
            f = d["tf"].get(t)
            if not f:
                continue
            idf = math.log(1 + (n - df[t] + 0.5) / (df[t] + 0.5))
            s += idf * f * (K1 + 1) / (f + K1 * (1 - B_ + B_ * d["len"] / avg))
        if s > 0:
            phrase = query.lower().strip()
            if phrase in d["title"].lower():
                s *= 1.5                      # exact phrase in the H1
            elif len(q) > 1 and phrase in d["p"].get("content", "").lower():
                s *= 1.25                     # exact multi-word phrase in the body
            # a light prior per page type, applied before ranking so that RRF (which only
            # sees ranks) cannot let a weak concept overtake a strong source
            scores[slug] = s * TYPE_PRIOR.get(slug.split("/")[0], 1.0)
    return sorted(scores.items(), key=lambda kv: -kv[1])


def snippet(text, query, width=220):
    text = html.unescape(text)
    terms = sorted(set(tokens(query)), key=len, reverse=True)
    low = text.lower()
    for t in terms:
        i = low.find(t)
        if i >= 0:
            a = max(0, i - width // 2)
            return re.sub(r"\s+", " ", text[a:a + width]).strip()
    return re.sub(r"\s+", " ", text[:width]).strip()


def cmd_search(args):
    index, meta = load_index(args.refresh)
    docs, df, avg, back = build(index)
    fused, hits = defaultdict(float), defaultdict(list)
    for q in args.queries:
        for rank, (slug, s) in enumerate(bm25(q, docs, df, avg)[:50], 1):
            fused[slug] += 1 / (K_RRF + rank)
            hits[slug].append({"query": q, "rank": rank})
    seeds = sorted(fused, key=lambda s: -fused[s])[: args.n]
    # one hop over the link graph: pages that seeds link to, or that link to seeds.
    # Ranked by how many seeds they touch (a page reached from several hits is central),
    # then by the rank of the best seed. Not comparable with search scores; reported apart.
    neighbours = {}
    if args.hops:
        for rank, s in enumerate(seeds, 1):
            linked = [(t, "links-to") for t in index[s].get("links", [])] + [(t, "linked-from") for t in back[s]]
            for t, rel in linked:
                if t in EXCLUDE or t not in docs or t in seeds:
                    continue
                nb = neighbours.setdefault(t, {"seeds": set(), "via": f"{s} {rel} this", "best": rank})
                nb["seeds"].add(s)
    nb_ranked = sorted(neighbours.items(), key=lambda kv: (-len(kv[1]["seeds"]), kv[1]["best"]))[: args.n]
    ranked = [(s, round(fused[s] * 1000, 2), None) for s in seeds]
    ranked += [(t, len(v["seeds"]), v) for t, v in nb_ranked]
    out = []
    for slug, score, nb in ranked:
        d = docs[slug]
        out.append({
            "slug": slug, "url": url_of(slug), "type": slug.split("/")[0], "title": d["title"],
            "score": score if nb is None else None, "stream": "search" if nb is None else "links",
            "matched": hits.get(slug, []), "via": nb["via"] if nb else None,
            "seed_count": len(nb["seeds"]) if nb else None,
            "chars": len(d["p"].get("content", "")),
            "snippet": snippet(d["p"].get("content", ""), " ".join(args.queries)),
        })
    ledger = {"queries": args.queries, "index_last_modified": meta.get("last_modified"),
              "pages_in_index": len(index), "candidates": out}
    if args.json:
        print(json.dumps(ledger, ensure_ascii=False, indent=1))
        return
    print(f"index: {len(index)} pages, last modified {meta.get('last_modified')}")
    if not out:
        print("no hits. The wiki is written in English: retry with English keywords or synonyms.")
    for i, c in enumerate(out, 1):
        if c["stream"] == "links" and (i == 1 or out[i - 2]["stream"] == "search"):
            print("\n-- link neighbours (one hop from the hits above) --")
        tag = f"score {c['score']}" if c["stream"] == "search" else f"{c['seed_count']} seeds; {c['via']}"
        print(f"{i:>2}. [{c['type']}] {c['title']}  —  {tag}\n    {c['url']}\n    … {c['snippet']} …")


def cmd_read(args):
    index, _ = load_index(args.refresh)
    p = index.get(args.slug) or sys.exit(f"unknown slug: {args.slug}")
    text = html.unescape(p.get("content", ""))
    print(f"# {page_title(p)}\nURL: {url_of(args.slug)}\nchars: {len(text)}\n")
    if not args.around:
        print(text[: args.max_chars])
        if len(text) > args.max_chars:
            print(f"\n[truncated at {args.max_chars} of {len(text)} chars; use --around TERM or --max-chars]")
        return
    low, term, w = text.lower(), args.around.lower(), args.window
    starts, i = [], low.find(term)
    while i >= 0 and len(starts) < args.max_hits:
        if not starts or i - starts[-1] > w:
            starts.append(i)
        i = low.find(term, i + 1)
    if not starts:
        print(f"[term not found: {args.around}]")
    for s in starts:
        a = max(0, s - w // 2)
        print(f"--- around char {s} ---\n{text[a:a + w]}\n")


def cmd_links(args):
    index, _ = load_index(args.refresh)
    if args.slug not in index:
        sys.exit(f"unknown slug: {args.slug}")
    back = sorted(s for s, p in index.items() if args.slug in p.get("links", []) and s not in EXCLUDE)
    out = sorted(set(index[args.slug].get("links", [])) - EXCLUDE)
    for name, group in (("links-to", out), ("linked-from", back)):
        print(f"## {name} ({len(group)})")
        for s in group:
            if s in index:
                print(f"- [{s.split('/')[0]}] {page_title(index[s])}  {url_of(s)}")


def cmd_meta(args):
    """Read lifecycle signals that exist only on the rendered HTML page, not in the index."""
    req = urllib.request.Request(url_of(args.slug), headers={"User-Agent": "ai-wiki-query-skill"})
    try:
        page = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        sys.exit(f"{url_of(args.slug)}: HTTP {e.code}")
    badge = re.search(r'class="confidence-badge"><em>(.*?)</em>', page)
    heads = re.findall(r'<h([23]) id="([^"]+)"[^>]*>(.*?)</h\1>', page, re.S)
    out = {
        "url": url_of(args.slug),
        "confidence_badge": html.unescape(badge.group(1)) if badge else None,
        "stale": "This page is preserved for history" in page,
        "sections": [{"level": int(l), "anchor": f"{url_of(args.slug)}#{a}",
                      "heading": html.unescape(re.sub(r"<[^>]+>", "", t)).strip()} for l, a, t in heads],
    }
    print(json.dumps(out, ensure_ascii=False, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--refresh", action="store_true", help="download the index again, ignoring the cache")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("queries", nargs="+")
    s.add_argument("-n", type=int, default=10, help="search hits to keep (and max link neighbours)")
    s.add_argument("--hops", type=int, default=1, choices=[0, 1], help="0 = search only")
    s.add_argument("--json", action="store_true")
    r = sub.add_parser("read"); r.add_argument("slug")
    r.add_argument("--around", help="print only windows around this term")
    r.add_argument("--window", type=int, default=1500)
    r.add_argument("--max-hits", type=int, default=6)
    r.add_argument("--max-chars", type=int, default=20000)
    l = sub.add_parser("links"); l.add_argument("slug")
    m = sub.add_parser("meta"); m.add_argument("slug")
    args = ap.parse_args()
    {"search": cmd_search, "read": cmd_read, "links": cmd_links, "meta": cmd_meta}[args.cmd](args)


if __name__ == "__main__":
    main()
```

## Bijlage B: voorbeeld van de antwoordvorm

```markdown
De wiki ziet een agent harness als de software rond een taalmodel die er een betrouwbaar werkend
systeem van maakt [W1]. Volgens de werkdefinitie regelt een harness minimaal context, beperkingen
(controles voor en na elke tool-aanroep) ... [W1]. Meerdere bronnen stellen dat de harness meer
verschil in prestaties verklaart dan de keuze van het model [W2][W3].

**Wat de wiki niet zegt:** kosten van harnesses voor kleine bedrijven komen in de gevonden pagina's
niet voor.

**Bronnen**
- [W1] Agent Harness (concept, Confidence 0.95 · 156 sources):
  https://businessdatasolutions.github.io/ai-wiki/concepts/agent-harness#working-definition
- [W2] ...
- [W3] ...

<details><summary>Zoekspoor</summary>

- Vraag: hoe definieert de wiki een agent harness, en uit welke onderdelen bestaat die?
- Facetten: 1) definitie 2) onderdelen 3) waarom het ertoe doet
- Zoekopdrachten: "agent harness", "harness engineering runtime", "harness components context constraints"
- USE: concepts/agent-harness, sources/..., ...
- IGNORE: entities/... (wrong-granularity), threads/... (redundant), ...
</details>
```
