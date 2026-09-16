# Featurebrainstorm: wat vier papers over de architectuur van deze wiki zeggen

**Datum:** 2026-09-16
**Aanleiding:** zoekopdracht via OpenAlex (`paper-search`) naar literatuur die deze wiki zelf kan verbeteren
**Status:** **verwerkt op 2026-09-16** — drie items geland, vijf in het plan, één premisse weerlegd. Zie [§Uitkomst](#uitkomst-2026-09-16) onderaan.
**Bronnen geacquireerd:** vier open-access papers, zie [§Geacquireerde bronnen](#geacquireerde-bronnen)

---

## Waarom deze zoekactie

De wiki bevat 275 bronnen, 50 concepten en 183 entiteiten — en **geen enkele bron over zijn
eigen architectuur**. Alle papers in `raw/papers/` gaan over coding agents of arbeidsmarkt.
Dat betekent dat §Retention (de decay-curve), §Search (hybride retrieval) en §Quality (de
rubriek) claims doen die nergens naar literatuur verwijzen. Ze zijn van de hand van de
ontwerper, niet van het veld.

Deze sessie zocht naar literatuur die (a) die claims kan onderbouwen of weerleggen, en
(b) concrete features suggereert voor de openstaande roadmapslots v0.6, v0.8 en v0.10.

---

## Vier bevindingen die deze wiki direct raken

### 1. De fusie-keuze in `wiki-retrieve.mjs` is empirisch aanvechtbaar

`scripts/wiki-retrieve.mjs` regel 45-46 hardcodeert `K_RRF = 60` en `GRAPH_W = 0.5`.
Bruch, Gai & Ingber (2023, ACM TOIS) vinden precies het tegendeel van wat het v0.10-plan
aanneemt:

> *"Contrary to existing studies, we find RRF to be sensitive to its parameters; that the
> learning of a convex combination fusion is generally agnostic to the choice of score
> normalization; that convex combination outperforms RRF in in-domain and out-of-domain
> settings; and finally, that convex combination is sample efficient, requiring only a small
> set of training examples to tune its only parameter to a target domain."*

Twee ongemeten constanten zitten dus in het hart van `/wqa`, en het paper zegt dat juist die
knoppen gevoelig zijn. Het v0.10-plan wil een conceptpagina `[[reciprocal-rank-fusion]]`
schrijven die `k=60` als de Cormack-default vastlegt — die pagina moet Bruch als voorbehoud
meenemen, anders codificeert de wiki een keuze die het veld inmiddels betwist.

### 2. Drie handmatige datumvelden benaderen slecht wat één temporeel model goed doet

De wiki onderhoudt `last_confirmed`, `accessed_at` en `supersedes`/`superseded_by` met de
hand. Zep/Graphiti (Rasmussen et al., 2025) gebruikt **bi-temporele kanten**: elk feit draagt
*wanneer het waar was* én *wanneer wij het leerden*. Supersessie wordt daarmee een query in
plaats van een protocol. Gerapporteerd resultaat: +18,5% op LongMemEval bij 90% lagere latency.

### 3. Citatiedichtheid meet het verkeerde

§Quality scoort wikilinks-per-1000-woorden (doel: ≥3,0). ALCE (Gao et al., 2023) laat zien
waarom dat zwak is: zelfs de beste systemen hebben *"incomplete citation support 50% of the
time"*. Een link náást een claim bewijst niet dat de bron de claim draagt. ALCE definieert
citation **precision** en **recall** als meetbare grootheden; dichtheid is een proxy die je
kunt spelen door meer links te strooien.

### 4. De v0.6 judge is naïef ontworpen

Het plan beschrijft `scripts/judge-quality.mjs` als "een tweede Claude-call met een
reviewer-prompt". Gu et al. (2024/2025) en Chen et al. (2024) documenteren positie-,
zelfvoorkeurs- en breedsprakigheidsbias. Die laatste is hier gevaarlijk: een judge die lange
pagina's hoger scoort, zet een prikkel om conceptpagina's op te blazen — precies tegengesteld
aan wat ACE (Zhang et al., 2025) *context collapse* noemt, waarbij iteratief herschrijven
detail juist erodeert. De wiki herschrijft conceptpagina's bij elke ingest en meet geen van
beide effecten.

---

## Negen features

### F1 — Meetbare fusie: `α`-tuning vervangt de hardcoded constanten

**Wat.** Voeg naast RRF een convexe-combinatie-fusor toe
(`score = α·qmd_norm + (1−α)·graph_norm`) en maak `α`, `k` en `graph_w` configureerbaar in
plaats van hardcoded. Gebruik de v0.10-evalset (≥50 synthetische query/doc-paren) om alle drie
te tunen op dit corpus; leg de gekozen waarden vast in `wiki/evals/`.

**Business case.**

- *Kosten:* laag — circa één sessie voor de fusor. Hangt af van `scripts/eval-qmd.mjs` en de
  evalset, maar die staan al op de v0.10-roadmap, dus geen extra scope.
- *Baten:* `/wq` en `/wqa` zijn het primaire ontsluitingskanaal voor 275 bronnen. Elke
  procentpunt retrieval-kwaliteit vermenigvuldigt zich over elke toekomstige query. Bruch
  levert bovendien een gratis argument: convexe combinatie is sample-efficiënt, dus 50
  evalparen volstaan om te tunen — een grote evalset is niet nodig.
- *Breekpunt:* rendeert direct; het kost nu al kwaliteit zonder dat iemand weet hoeveel.
- *Risico:* overfitten op 50 synthetische queries. Mitigatie: rapporteer NDCG@10 voor zowel de
  RRF-baseline als de getunede α, en bewaar beide.

### F2 — Bi-temporele claims: `valid_from` / `valid_until` naast `last_confirmed`

**Wat.** Een tweede tijdsas op concept- en bronpagina's. `last_confirmed`/`accessed_at` blijven
de *wiki-tijd* (wanneer wisten wij dit). Nieuw: `valid_from`/`valid_until` als *wereldtijd*
(wanneer gold de claim). Supersessie wordt dan afleidbaar in plaats van handmatig.

**Business case.**

- *Kosten:* middel — schemawijziging plus gesuperviseerde migratie over 50 concepten. Ongeveer
  de omvang van de v0.2-migratie.
- *Baten:* de wiki bevat veel claims met houdbaarheidsdatum (modelprestaties, adoptiecijfers,
  arbeidsmarkteffecten). Nu is "AI Index 2026 zegt X" niet te onderscheiden van "X geldt nog".
  Met een tweede as wordt *"wat wisten we in mei en klopt dat nog?"* een query in plaats van
  handwerk — precies de vraag die een wiki over een snel bewegend veld voortdurend stelt.
- *Breekpunt:* nu al. Bij 275 bronnen over een veld dat per kwartaal verschuift, is een groot
  deel van de empirische claims tijdgebonden.
- *Risico:* veldinflatie; vier datumvelden per pagina is veel administratie. Mitigatie:
  optioneel maken, alleen verplicht op claims die een expliciet jaartal noemen.

### F3 — Personalized PageRank als graafstroom (HippoRAG)

**Wat.** Vervang de hop-telling in `scripts/wiki-retrieve.mjs` (`ordered by hops asc,
seedScore desc`) door Personalized PageRank over `wiki/.graph.json`, met de qmd-hits als
seed-vector. Een pagina die vanuit drie seeds op twee hops bereikbaar is, scoort dan hoger dan
een pagina die vanuit één seed op één hop hangt — wat de huidige sortering niet kan uitdrukken.

**Business case.**

- *Kosten:* laag — PPR op een graaf van ~520 knopen is tientallen regels code en milliseconden
  rekentijd. Geen nieuwe dependency.
- *Baten:* HippoRAG rapporteert tot 20% winst op multi-hop QA, en presteert met één
  retrieval-stap zo goed als iteratieve retrieval tegen 10-30× lagere kosten. Juist de
  `/wqa`-vragen die provenance vereisen zijn multi-hop.
- *Breekpunt:* nu. Beste kosten/baten-verhouding in deze lijst — algoritmische vervanging,
  geen schemawijziging, geen migratie.
- *Risico:* verwaarloosbaar. Beide implementaties kunnen naast elkaar draaien; de evalset uit
  F1 wijst de winnaar aan.

### F4 — Citatie-entailmentcheck: van dichtheid naar dekking

**Wat.** Een `scripts/check-citations.mjs` die per claim-zin op een conceptpagina de aangehaalde
bronpagina ophaalt en met een goedkoop model toetst of de bron de claim draagt. Levert twee
getallen per pagina: *citation precision* (aandeel links dat de claim ondersteunt) en *citation
recall* (aandeel claims met ondersteunende link). Vervangt de dichtheidsdimensie in §Quality.

**Business case.**

- *Kosten:* de hoogste van de negen — de enige feature die per claim een API-call doet. Ruwe
  schatting: 50 concepten × ~15 claims ≈ 750 calls per volledige sweep. Op Haiku verwaarloosbaar
  in euro's, maar niet iets dat je per edit draait.
- *Baten:* raakt de kernbelofte van het repo. "Citations beat assertions" staat als werkprincipe
  in CLAUDE.md, maar wordt gemeten met een proxy die niets over waarheid zegt. ALCE laat zien
  dat de faalmodus reëel én groot is (50% incomplete support). Zodra de wiki bronmateriaal
  levert voor publicatie naar buiten, is dit het getal dat het verschil maakt tussen
  "onderbouwd" en "ziet er onderbouwd uit".
- *Breekpunt:* zodra de wiki naar buiten publiceert. Gezien de `taalrapport-*` bestanden in
  `inspiration/` is dat nu al zo.
- *Risico:* de checker heeft dezelfde biases als elke LLM-judge (zie F7). Mitigatie: uitsluitend
  als *flagger* draaien, nooit als auto-editor — consistent met het hookcontract.

### F5 — Conflictdetector met typologie

**Wat.** Adopteer de driedeling uit Xu et al. (2024) — *inter-context* (twee bronnen spreken
elkaar tegen), *context-memory* (bron spreekt de wiki tegen), *intra-memory* (de wiki spreekt
zichzelf tegen). Breid `contradicts` uit met een `conflict_class:`-veld en bouw een lint die
intra-memory conflicten detecteert: twee conceptpagina's die dezelfde bron citeren voor
onverenigbare claims.

**Business case.**

- *Kosten:* laag-middel. De vocabulaire-uitbreiding is triviaal; de detector is een graafquery
  plus een LLM-oordeel over kandidaatparen.
- *Baten:* `## Debates and supersession` is nu één ongedifferentieerde bak, en — belangrijker —
  wordt alleen gevuld als de ingestor de tegenspraak toevallig opmerkt. Intra-memory conflicten
  zijn per definitie onzichtbaar tijdens een ingest, omdat ze pas ontstaan als twee pagina's
  onafhankelijk van elkaar zijn geschreven. Bij 50 concepten en 275 bronnen is de kans dat ze
  bestaan hoog en de kans dat iemand ze handmatig vindt laag.
- *Breekpunt:* nu. Dit is de klassieke wiki-vervalmodus waartegen het hele repo ontworpen is.
- *Risico:* valse positieven (nuanceverschil ≠ tegenspraak). Mitigatie: rapporteer als
  kandidatenlijst met `via:`-suggestie; de mens beslist. Het v0.6-plan noemt dit al
  "contradiction-resolver-as-proposer".

### F6 — Collapse-detectie op conceptpagina's

**Wat.** Een lint die per conceptpagina de git-historie leest en waarschuwt bij *context
collapse*: woordenaantal daalt terwijl `source_count` stijgt, of een eerder genoemde
entiteit/nuance verdwijnt uit de body zonder bijbehorende supersessie-entry. ACE's antwoord —
incrementele delta-updates in plaats van herschrijven — wordt dan een expliciete werkregel in
§Process stap 6.

**Business case.**

- *Kosten:* laag. `git log -p` per pagina plus een diff-heuristiek. Geen LLM nodig voor de
  detectie, alleen voor het oordeel over gevonden gevallen.
- *Baten:* dit is een faalmodus die nu al kan lopen zonder dat iemand het merkt. Een
  conceptpagina met tien ingests is tien keer herschreven; ACE noemt brevity bias en collapse
  als de twee dominante faalmodi van precies dat patroon. De wiki heeft git, dus het bewijs ligt
  er al — er kijkt alleen niemand naar.
- *Breekpunt:* pagina's met ≥5 ingests. Kandidaten: `agent-harness`, `ai-employment-effects`.
- *Risico:* geen. Read-only lint, past binnen het hookcontract.

### F7 — Bias-geharde judge (herontwerp van v0.6)

**Wat.** Vóórdat `scripts/judge-quality.mjs` gebouwd wordt: neem de mitigaties uit Gu et al. en
Chen et al. over. Concreet — score per dimensie apart in plaats van één globaal cijfer,
randomiseer presentatievolgorde bij paarsgewijze vergelijking, normaliseer expliciet op lengte,
en kalibreer eenmalig tegen een handmatig gescoorde referentieset van ~10 pagina's om te toetsen
of de judge met de mens correleert.

**Business case.**

- *Kosten:* verwaarloosbaar *als het vóór de bouw gebeurt*; een gedeeltelijke herbouw erna.
- *Baten:* `quality_score` is het enige veld dat tooling in frontmatter mag schrijven — de
  smalle uitzondering op het auto-write-verbod. Een biased judge vervuilt dus precies het veld
  met de minste menselijke controle. Verbositeitsbias zou bovendien een perverse prikkel richting
  langere pagina's zetten, wat F6 direct tegenwerkt.
- *Breekpunt:* vóór v0.6. Dit is geen feature maar een ontwerpvoorwaarde.
- *Risico:* de kalibratieset is subjectief. Acceptabel — 10 pagina's is een uur werk; het
  alternatief is een ongekalibreerd getal.

### F8 — Procedurele-geheugendistillatie: CLAUDE.md schrijft zichzelf bij

**Wat.** ReMe's driedeling toegepast op het schema zelf: *multi-faceted distillation* (herken
succespatronen én faaltriggers uit `wiki/log.md`), *context-adaptive reuse*, en *utility-based
refinement* (voeg gevalideerde regels toe, snoei achterhaalde). Concreet: een
`/distill`-operatie die de laatste N logentries leest en kandidaat-schemaregels voorstelt voor
CLAUDE.md, met expliciete verwijzing naar de sessies die het patroon aantoonden.

**Business case.**

- *Kosten:* middel. De operatie zelf is een prompt over `log.md`; het is vooral een
  governance-vraag (wie keurt schemawijzigingen goed).
- *Baten:* CLAUDE.md is expliciet ontworpen als procedureel geheugen dat meebeweegt met de
  werkelijke workflow — maar dat meebewegen gebeurt nu alleen als de gebruiker eraan denkt. De
  index-completeness-bug is het bewijsstuk: **28 entiteitspagina's zonder indexbullet, maanden
  onopgemerkt**, en de reden die CLAUDE.md zelf geeft is *"because nothing checked for it"*.
  ReMe's punt is exact dit: passieve accumulatie is de faalmodus, en de oplossing is een
  expliciete refinement-stap. De wiki heeft die voor kennis (lint) maar niet voor zijn eigen
  procedures.
- *Breekpunt:* nu, en het rendement stijgt met elke sessie omdat `log.md` groeit.
- *Risico:* schema-drift richting complexiteit; elke sessie stelt regels voor en CLAUDE.md dijt
  uit. Mitigatie: de *snoei*-helft is niet optioneel — elke voorgestelde regel moet een
  kandidaat-regel noemen die eruit kan.

### F9 — Meervoudige graafviews (MAGMA) — *nu nog niet*

**Wat.** MAGMA splitst geheugen in orthogonale semantische, temporele, causale en
entiteitsgrafen, en maakt retrieval een policy-gestuurde traversal per query-intentie. De
12-typen-vocabulaire van deze wiki mengt alle vier: `caused` is causaal, `part-of` structureel,
`supports` evidentieel, `authored-by` provenance. Een traversal die alle vier gelijk behandelt,
haalt bij een causale vraag auteurs op.

**Business case.**

- *Kosten:* hoog. Dit is architectuur, geen feature.
- *Baten:* reëel maar pas op schaal. MAGMA's winst komt uit long-horizon reasoning; bij ~520
  knopen is de graaf klein genoeg dat ruis beheersbaar blijft.
- *Breekpunt:* v0.11+. **Wel nu doen:** de goedkope helft — annoteer de bestaande 12 typen met
  een `class:` (causaal / structureel / evidentieel / provenance) in de documentatie, zodat de
  graafstroom uit F3 per queryvorm kan filteren. Een middag werk, circa 80% van het voordeel.
- *Risico:* premature optimalisatie. Deze staat hier vooral om te markeren dat hij *niet* nu moet.

---

## Prioritering

| # | Feature | Kosten | Baten | Doen |
|---|---------|--------|-------|------|
| F3 | PPR-graafstroom | Laag | Hoog | **Nu** — beste kosten/baten in de lijst |
| F7 | Bias-geharde judge | Nihil (vooraf) | Hoog | **Nu** — ontwerpvoorwaarde voor v0.6 |
| F6 | Collapse-detectie | Laag | Hoog | **Nu** — read-only, bewijs ligt al in git |
| F1 | Fusie-tuning | Laag | Hoog | Met v0.10 (hangt aan de evalset) |
| F5 | Conflictdetector | Laag-middel | Hoog | Met v0.6 (past bij de resolver) |
| F8 | Schemadistillatie | Middel | Hoog | Met v0.8 (zelfde governance-vraag) |
| F2 | Bi-temporele claims | Middel | Middel-hoog | v0.11 — schemawijziging + migratie |
| F4 | Citatie-entailment | Hoog | Zeer hoog | v0.11 — belangrijkste op termijn |
| F9 | Multi-graaf | Hoog | Laag *nu* | Alleen de `class:`-annotatie |

De drie bovenaan zijn samen ongeveer één sessie werk en raken geen enkel schema — ze kunnen los
van de roadmap. F4 is de duurste en tegelijk de enige die de kernbelofte van het repo hard maakt;
die verdient een eigen versieslot.

---

## Geacquireerde bronnen

Vier open-access papers zijn op 2026-09-16 geland in `raw/papers/` (Acquire-fase; nog niet
geprocessed naar `wiki/sources/`). Alle vier `fulltext_source: pdf-converted`, converter
`pdftotext -layout` — tabellen zijn afgevlakt, verifieer cijfers tegen de PDF.

| Bestand | Paper | Relevantie |
|---|---|---|
| `2023-05-04-bruch-analysis-of-fusion-functions-for-hybrid-retrieval.md` | Bruch, Gai & Ingber (2023), ACM TOIS, [10.1145/3596512](https://doi.org/10.1145/3596512) | F1 — §Search, weerlegt de RRF-aanname |
| `2024-04-21-zhang-survey-memory-mechanism-llm-agents.md` | Zhang et al. (2025), ACM TOIS, [10.1145/3748302](https://doi.org/10.1145/3748302) | F2, F8 — §Retention, §Tier vocabulary |
| `2023-12-06-gao-enabling-llms-to-generate-text-with-citations.md` | Gao, Yen, Yu & Chen (2023), EMNLP, [10.18653/v1/2023.emnlp-main.398](https://doi.org/10.18653/v1/2023.emnlp-main.398) | F4 — §Quality, citatiemeting |
| `2025-10-19-gu-survey-on-llm-as-a-judge.md` | Gu et al. (2024), [arXiv:2411.15594](https://arxiv.org/abs/2411.15594) | F7 — v0.6 judge-ontwerp |

Twee identiteitsnotities (pre-flight Check 2), vastgelegd in de raw-bestanden zelf:

- **Zhang** — de citeerbare vindplaats is het ACM TOIS-artikel uit **2025**; de volledige tekst
  die we hier hebben is de **arXiv v1 uit april 2024**. De TOIS-versie zit achter een paywall.
- **Gu** — OpenAlex dateert het record op **2024**; de opgehaalde PDF is **v6 (19 okt 2025)**.
  Citeren als de survey uit 2024, paginaverwijzingen scopen op v6.

### Niet geacquireerd, wel de moeite waard

- **Zep** (Rasmussen et al., 2025), [arXiv:2501.13956](https://arxiv.org/abs/2501.13956) — bron voor F2
- **HippoRAG** (Jiménez Gutiérrez et al., 2024), [arXiv:2405.14831](https://arxiv.org/abs/2405.14831) — bron voor F3
- **ACE** (Zhang et al., 2025), [arXiv:2510.04618](https://arxiv.org/abs/2510.04618) — bron voor F6
- **ReMe** (Cao et al., 2026), [ACL Findings 2026.findings-acl.829](https://aclanthology.org/2026.findings-acl.829.pdf) — bron voor F8
- **Knowledge Conflicts for LLMs: A Survey** (Xu et al., 2024), [10.18653/v1/2024.emnlp-main.486](https://doi.org/10.18653/v1/2024.emnlp-main.486) — bron voor F5
- **MAGMA** (Jiang et al., 2026), [ACL 2026.acl-long.1709](https://aclanthology.org/2026.acl-long.1709.pdf) — bron voor F9
- **Graph RAG: A Survey** (Peng et al., 2025), ACM CSUR, [arXiv:2408.08921](https://arxiv.org/abs/2408.08921) — overzichtskaart
- **Humans or LLMs as the Judge? A Study on Judgement Bias** (Chen et al., 2024), EMNLP — aanvulling op F7

### Zoekopdracht die niets opleverde

Het v0.8-slot (gap-driven research direction) bleef leeg. Queries rond "structural holes" en
"knowledge gap detection" dreven af naar sociale-netwerkanalyse en ongerelateerde techniek.
InfraNodus' Phase 10-matrix lijkt praktijkwerk zonder academisch anker. Een tweede poging zou
anders geframed moeten worden: bibliometrisch ("research gap identification") of via
community-detection-for-missing-links.

---

## Mogelijke vervolgstap buiten deze lijst

Bij het processen van deze vier bronnen ontstaat er een conceptpagina die er nog niet is:
`agent-memory-architecture`. Die zou de vier §-secties van CLAUDE.md (Retention, Search,
Quality, Graph) voor het eerst aan externe literatuur koppelen in plaats van aan zichzelf.


---

## Uitkomst (2026-09-16)

Alle negen items zijn afgehandeld in dezelfde sessie als waarin dit document geschreven werd. Geen enkele wiki-inhoudspagina is aangeraakt.

| # | Uitkomst |
|---|---|
| **F1** | **Half geland.** De knoppen bestaan (`--fusion cc`, `--k-rrf`, `--graph-w`, `--alpha`, `--conf-floor`); het tunen wacht op de evalset → v0.10 item 5. |
| **F2** | **Nieuw versieslot v0.11** — bi-temporele claims. |
| **F3** | **Geland.** `--graph-rank ppr` in `scripts/wiki-retrieve.mjs`. |
| **F4** | **Nieuw versieslot v0.12** — citatie-entailment. |
| **F5** | **In v0.6** — `conflict_class:` + `scripts/lint-conflicts.mjs`. |
| **F6** | **Geland** als `scripts/lint-collapse.mjs` — en de premisse is weerlegd, zie hieronder. |
| **F7** | **In v0.6** als vier ontwerpvoorwaarden, vastgelegd vóór de judge bestaat. |
| **F8** | **In v0.8** — `/distill`, met verplichte snoei-helft. |
| **F9** | **Goedkope helft geland** (edge classes in CLAUDE.md + `.graph.json`); traversal-filter → v0.13+. |

### De premisse onder F6 hield geen stand

`lint-collapse.mjs` vond **nul signalen** over alle 53 concept- en synthesepagina's met historie, ook bij een drempel van 2%. De detector is geverifieerd tegen handmatig berekende historie voordat dat nulresultaat is geaccepteerd — de data wordt goed gelezen en het antwoord is echt niets.

Wat de data wél laat zien is het spiegelbeeld. `agent-harness`: **2.522 → 24.547 woorden over 60 revisies**, `source_count` 4 → 93. `ai-employment-effects` staat op 13,4× zijn eerste revisie, `micro-productivity-trap` op 18,2×. ACE's *brevity bias* is hier niet het probleem; **ongeremde aangroei** is het, en niets begrenst dat. Het script rapporteert daarom voortaan ook de zwaarste pagina's, zodat een schone run nog steeds informatie oplevert.

Er is bewust **geen drempel** voorgesteld: het is oprecht onduidelijk of een conceptpagina van 24.000 woorden een defect is of een goed bediend onderwerp, en de waarschijnlijke oplossing is *splitsen*, niet *inkorten*. Staat als open vraag in v0.13+.

### Consequentie voor de volgorde

v0.10 was een opruimversie. Het is nu de **meetafhankelijkheid van drie andere dingen** (de fuser-2×2, het traversal-filter, en elke toekomstige retrieval-wijziging), en er draaien inmiddels drie retrieval-configuraties waarvan er nul gemeten is. Dat pleit ervoor v0.10 vóór v0.6 te doen: een judge zonder kalibratieverhaal is dezelfde categorie fout als een retrieval-default zonder evalset. Bouw eerst de meetinstrumenten.
