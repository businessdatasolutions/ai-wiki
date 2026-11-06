---
type: research-log
topic: "In hoeverre sluit de LRD AISO26009 (driedaagse training AI Strategie en Organisatietransformatie, S&N) aan bij wat de ai-wiki zegt over opschaling, de menskant en bouwen met AI?"
date: 2026-11-04
output_target: "Toets van een onderwijsontwerp (LRD) tegen de wiki: bevindingen per LRD-onderdeel met oordeel (sluit aan / spanning / ontbreekt / wiki zwijgt)"
related_output: "/Users/witoldtenhove/Projects/aiso/onderzoek/2026-11-04-lrd-wiki-toets.md"
---

# Research log — LRD AISO26009 getoetst aan de ai-wiki

Getoetst document: `/Users/witoldtenhove/Projects/aiso/LRD-AISO26009-lesdagen.html` (versie 0.1, 4 november 2026). Gelezen: de proza (deel 1–13, bijlage bronnen) en het `DATA`-object (`lu`, `sn`, `fr`, `nfr`, `ac`, `deck`, `workshops`, `kiss`, `days`, `experimentTypes`, `pipeline`, `examples`, `boardMoments`, `risks`, `phases`).

Zoekmethode: `wiki/index.md` is 844 KB. De secties Concepts, Syntheses en Threads zijn volledig gelezen. Voor de bronnen is volgens CLAUDE.md §Search (vraag raakt >5 pagina's) eerst `scripts/wiki-query.mjs --no-bump -n 12` gedraaid, één keer per startvraag. Daarna is per LRD-term met `grep` vastgesteld of de wiki er iets over zegt (om "wiki zwijgt" hard te maken). `accessed_at` is na afloop handmatig gebumpt op alleen de concept- en synthesepagina's die echt gelezen zijn.

## Niveau 0 — startvragen

1. Wat zegt de wiki over hoe organisaties AI van losse experimenten naar structurele, opgeschaalde inzet brengen (strategie, businesscase/ROI, roadmap, governance), en welke valkuilen en cijfers noemt ze?
2. Wat zegt de wiki over de menskant van AI-transformatie (adoptie, cultuur, vaardigheden, teams, weerstand, leiderschap), en welke aanpakken werken volgens de bronnen?
3. Wat zegt de wiki over werken en bouwen met AI (experimenteren, specificeren met PRD/spec, agents en multi-agent/persona-opzetten, evaluatie), en hoe worden managers en professionals AI-vaardig?

## Niveau 1 — pagina's uit index.md (+ qmd)

Geselecteerd (4 pagina's, 3 types: synthese, bron, concept):
- `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` — Q1 + Q2
- `wiki/sources/2026-05-02-dutt-chatterji-ai-experimentation-to-transformation.md` — Q1
- `wiki/syntheses/ai-worker-maturity-levels.md` — Q2 + Q3
- `wiki/concepts/spec-driven-development.md` — Q3

### Antwoorden

- **Q1 (organizational-frameworks)**: elf kaders op verschillende beslislagen; kies het kader naar de vraag van de bestuurder. Sterkste overeenstemming: "process redesign is the main cost, not technology" (7 bronnen). Senior-leader ownership: McKinsey *Rewired*: "We don't have a single success story where senior business leaders weren't in the driver's seat." Echte spanning: pilots als fase (MIT CISR Stage 2) tegenover pilots als val (Bain/OpenAI); de synthese verzoent dat zo: "treating MIT CISR's Stage 2 as a phase to pass through quickly, not dwell in". Cijfers: *Rewired* ~20% EBITDA, $3:$1 ROI, 1–2 jaar terugverdientijd (ongeveer 20 AI-leiders, selectie-effect); Bain 10–25% EBITDA (klantdata). Rijpe bovenkant 7–15% (AI Index 1%, MIT CISR Stage 4 7%, Cisco 13%, Augmented Learners 15%, Werner-Le-Brun 12%). Open vraag op de pagina zelf: geen brug naar de verandermanagementliteratuur ("Kotter, Lewin; none of the wiki's existing concept pages directly bridge to it").
- **Q1 (Dutt et al., HBR 30-04-2026, Bain + OpenAI)**: de micro-productivity trap, met offering lock-in en process lock-in. Vier stappen: (1) kies 4–5 kritieke domeinen, (2) herontwerp workflows over de hele organisatie ("It's the process redesign — not the technology — that is the most challenging part … and also creates most of the value"), (3) betrek de mensen die het dichtst bij het huidige proces staan, met een prototypecultuur in alle afdelingen, (4) meet wat ertoe doet: bedrijfsuitkomsten "with metrics that allow for comparisons with non-AI methods", plus doorlopende evals. FabricationCo: workshop van een week met frontlijn en managers, 14 use cases, ~$30M; offertes ~15× sneller, +10 pp winrate in 3 maanden. Lowe's: pilot in 1–2 afdelingen per winkel, nu 1.700+ winkels. "Boardroom imperative": achterblijvers delegeren AI aan IT zonder doelen of metrics.
- **Q2/Q3 (ai-worker-maturity-levels)**: zes niveaus L0–L5, gemeten aan wie maakt, wie controleert en wie beslist. "Evaluation, not generation, is the binding constraint at every level above novice." Stap L1→L2: betaald frontiermodel, actief het denkmodel kiezen, itereren, om kritiek vragen. Stap L2→L3: "shift from prompting to specifying — write the acceptance criteria before the request". Zelfrapportage is vertekend: in METR waren ontwikkelaars 19% langzamer en dachten ze 20% sneller te zijn, een gat van ~39 punten. Eigen voorbehoud van de pagina: de ladder is gebouwd op programmeerwerk, en "generalisation beyond code is untested at scale".
- **Q3 (spec-driven-development)**: een geschreven, door een mens gereviewde spec legt vast wat er gebouwd wordt. "AI makes vague specs more costly, not less" (Ivers, SEI/CMU: onderspecificatie is de slechte gewoonte die AI het sterkst versterkt). De review verschuift naar vóór de bouw. Kosten (Kmiecik): wildgroei aan markdown, geen standaard, spec drift, voorkeur voor greenfield, "partial waterfall". Debat: het Claude Code-team van Anthropic verving design docs door prototypes (vastgelegd als `contradicts`). Confidence 0.75: geen enkele bron meet een uitkomst.

### Niveau-1 vragen

Van organizational-frameworks: 1.1 Wat zegt Carucci precies over weerstand, en welke leiderschapsvalkuilen noemt hij? 1.2 Hoe ziet de micro-productivity trap eruit in cijfers (pilot purgatory)? 1.3 Wat meet MIT CISR over de overgang van pilots naar opschaling?
Van Dutt et al.: 2.1 Hoe meet je uitkomsten en evals zonder in de val te lopen? 2.2 Hoe kies je de eerste use case (Anand-Wu: kosten van fouten × soort kennis)? 2.3 Wat betekent de boardroom imperative voor wie de transformatie trekt?
Van ai-worker-maturity-levels: 3.1 Wat zegt Mollick over hoe mensen AI-vaardig worden? 3.2 Wat is de jagged frontier, en wat betekent die voor een les over "wat AI kan en niet kan"? 3.3 Hoe betrouwbaar is zelfrapportage over AI-gebruik?
Van spec-driven-development: 4.1 Prototype of document: welke bron zegt wat? 4.2 Waar komt de review terecht als agents bouwen? 4.3 Wat zegt de wiki over meerdere AI-perspectieven of agents tegelijk (relevant voor de boards)?

## Niveau 2 — links gevolgd

Geselecteerd (4 pagina's):
- `wiki/concepts/micro-productivity-trap.md` — voor 1.2 + 2.1 (gelezen: r. 1–175, plus 213–232, 288–345 en 360–367; de pagina is 109 KB)
- `wiki/sources/2026-05-07-carucci-resistance-as-data.md` — voor 1.1
- `wiki/sources/2026-06-16-mollick-simon-sinek-ai-skills-experience-edge.md` — voor 3.1 + 3.3
- `wiki/concepts/jagged-frontier.md` — voor 3.2

### Antwoorden

- **1.2 / 2.1 (micro-productivity-trap, confidence 0.95, 80 bronnen)**: MIT NANDA via Allen/AWS: "95% of organizations are getting zero return" ("pilot purgatory"; de BBC-panelleden plaatsen er kanttekeningen bij: de steekproef was 153 bedrijven). PwC Davos (~4.500 CEO's): 56% ziet nog geen rendement, slechts één op de acht een echte besparing of omzet. Grant: ~30% van de pilots haalt productie (eigen, niet-geaudite data). MGI: ~90% heeft geïnvesteerd, <40% ziet meetbare winst. BBC: verhouding toegang tot AI-tools en AI-training 3:1; Kuht noemt het "imagination gap". Hines-Pierce: "70% people … technology is like 10% … The other 20% is processes", plus een bewust ingericht governanceteam in het midden dat een opgeloste workflow verspreidt. Brynjolfsson: J-curve; kostenbesparing als maatstaf is "a little lazy"; "you're going to get more resistance … if you tell them this is a tool for cutting heads". BCG: "Refocus automation on redesign, not just cost reduction"; nieuwe KPI's die productiviteit aan uitkomsten koppelen. Argenti: "ask them to be 3x more productive, not 20%". Kiron & Schrage: verificatie → evaluatie → vastleggen van wat je leert; vastleggen in "decision journals, prompt repositories, evaluation logs"; de derde evaluatievraag is "What was *interestingly* wrong?". Ransbotham: organisaties met systematische feedbackloops tussen mens en AI hebben 6× zo vaak substantiële financiële baten. Kropp: de framing van AI als werknemer is een derde vorm van lock-in. Krakowski (RCT, N=72): AI die niet op de gebruiker is afgestemd, laat het marktaandeel langzaam dalen. Eigen voorbehoud van de pagina: "The page's diagnosis is corroborated far more strongly than any of its numbers."
- **1.1 (Carucci, HBR 20-04-2026)**: de vraag "legitieme zorg of reflexmatige weerstand?" is de verkeerde vraag; alle weerstand is data. Drie valkuilen: personaliseren, moraliseren, haast maken met een oplossing ("persuading harder or escalating authority"). Vier signalen: verlies, onzekerheid, gebrek aan controle (inclusief "faux-inclusion": input vragen nadat het besluit al is genomen) en fouten in de verandering ("the very people resisting the change are the ones closest to the risks"). Reactie: "Be willing to adapt the plan." Kwaliteitsvlag op de pagina: praktijkopinie, geen data.
- **3.1 / 3.3 (Mollick bij Sinek, 2026-06-16)**: ervaring is het voordeel; in de BCG-studie waren junioren slechter in AI-gebruik omdat ze de output niet konden beoordelen. De "$20 decision": betaal voor een groot model en kies actief het denkmodel. "Prompt engineering … none of that matters anymore." Geef AI zwaardere taken. "The AI is a sycophant — tell it to act like a critic"; gebruik persona-prompts voor een spreiding aan lezers. Inspanning tegenover resultaat: AI-shortcuts geven mensen het idee dat ze leren terwijl dat niet zo is. GDPval: het aandeel taken waarin het beste model gelijk speelt met of wint van experts steeg van ~48% naar ~84% (zijn herinnering aan de cijfers).
- **3.2 (jagged-frontier, confidence 0.95)**: Dell'Acqua et al., 758 BCG-consultants. Binnen de frontier: +12,2% voltooiing, +25,1% sneller, +33,9% kwaliteit. Buiten de frontier: 19 procentpunt minder vaak correct (84,5% → 60,0%/70,6%). AI verbetert de presentatie los van de inhoud ("subjective coherence"). "Familiarity training can backfire": de groep met GPT + overzicht scoorde buiten de frontier slechter dan de groep met alleen GPT. Allen & McDonald (*Strategy Science* 2026): 34 modellen in een strategiesimulatie over acht jaar; frontiermodellen uit midden/eind 2025 scoren onder modellen uit begin 2025 én onder MBA-studenten, door een "systematic exploitation bias". De kartel zit bij "forward-looking commitment under delayed feedback — exactly the region where a manager is most tempted to delegate a judgment". Boussioux: AI-oplossingen blijven dicht bij bestaande ideeën en schuiven naar het statistische gemiddelde. Böckeler: kans × impact × detecteerbaarheid bepaalt hoeveel toezicht nodig is.

### Niveau-2 vragen

A (micro-productivity-trap): A1 Hoe zou een businesscase de J-curve en uitkomstmaatstaven (geen kostenmaatstaven) moeten bevatten? A2 Wat maakt dat een pilot doorschaalt (integratie, een governanceteam in het midden)? A3 Wat zegt de wiki over het framen van AI als werknemer (Kropp)?
B (Carucci): B1 Moet je weerstand oefenen als overtuigingsgesprek of als diagnose? B2 Hoe voorkom je faux-inclusion in een transformatieplan? B3 Is er een tweede bron (concept-promotie uitgesteld)?
C (Mollick): C1 Is een persona-panel (Mollick: persona-prompts) onderbouwd als beoordelaar? C2 Hoe bouwen ervaren niet-technici AI-vaardigheid op? C3 Zelfrapportage, in welke richting vertekend?
D (jagged-frontier): D1 Hoe goed beoordelen LLM's strategieën en businessplannen (Csaszar)? D2 Waar ligt de kartel bij strategische oordelen (Allen & McDonald)? D3 Wat doet AI met teams en duo's (Dell'Acqua 2026)?

## Niveau 3 — laatste links

Gelezen (3 volledig of grotendeels, 3 gericht):
- `wiki/sources/2024-12-01-csaszar-ketkar-kim-ai-strategic-decision-making.md` (link vanuit jagged-frontier) — voor D1 + C1
- `wiki/sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees.md` (link vanuit micro-productivity-trap; frontmatter + TL;DR + opzet + eerste twee faalwijzen) — voor A3
- `wiki/sources/2026-06-12-dellacqua-cybernetic-teammate-field-experiment-genai-teamwork.md` (link vanuit jagged-frontier; TL;DR + resultaten) — voor D3 + C3
- Gericht: `wiki/concepts/responsible-ai.md` (secties: Hill r. 250–262, Agentic AI governance r. 298–308, plus grep op "AI Act"); `wiki/sources/2025-11-24-sadun-wood-worklab-hard-to-become-ai-first-organization.md` (r. 80–95; uit de qmd-resultaten voor Q1, niet via een link: afwijking van de linkregel, hier vastgelegd).
- Gericht, voor 4.1 (link vanuit spec-driven-development, sectie Debates): `wiki/sources/2026-05-08-running-an-ai-native-engineering-org.md` (TL;DR + slide 3). Daarnaast is gecontroleerd welke bronnen uit de LRD-tabel "Zo werken AI-bedrijven" in de wiki staan. Kohavi, model cards, de Responsible Scaling Policy en OpenAI Evals: geen treffer. Schluntz & Zhang wel: `wiki/sources/2024-12-19-anthropic-building-effective-agents.md` (r. 39–44 gelezen).

### Antwoorden

- **D1 / C1 (Csaszar, Ketkar & Kim 2024, *Strategy Science* 9(4), peer-reviewed)**: LLM's maken én beoordelen businessplannen "at a level comparable to humans" (accelerator en VC/angel-investeerders). Vignetten met AI-versies van klassieke strategie-instrumenten, waaronder Devil's Advocate. Voorbehoud: modellen uit 2023–24; uitspraak over prestatieniveau, niet over bedrijfsprestatie; risico dat AI "conventional strategies" reproduceert.
- **A3 (Kropp et al., BCG/HBR 2026-05-06, RCT N=1.261)**: AI framen als werknemer in plaats van als tool leidt tot −9 pp persoonlijke verantwoordelijkheid (8 pp verschuift naar de AI), 44% meer escalaties, 18% minder fouten gevonden, 13% meer onzekerheid over de eigen beroepsidentiteit, zonder dat de adoptie stijgt. Vijf aanbevelingen, waaronder "make accountability explicit and personal" en een capaciteitsplan voor mensen die agents aansturen. Let op: getest op documenten die een "AI-werknemer" schreef (subgroep: organisaties met AI op het organogram), niet op adviespersona's.
- **D3 / C3 (Dell'Acqua et al. 2026, *Organization Science*, preregistered, N=791, P&G)**: individu + AI ≈ team zonder AI (+0,37 SD tegen +0,24 SD); AI werkt "as an effective boundary-spanning mechanism" door functionele silo's heen. Team + AI heeft 9,2 pp meer kans op een top-10%-oplossing, ongeveer 3× de basis van 5,8%. Ook de vertekening in zelfbeoordeling liep hier de andere kant op: "self-assessment is decoupled from performance under AI".
- **Governance (responsible-ai)**: Singapore IMDA, kader voor agentic AI (januari 2026), vier pijlers: risico's vooraf begrenzen; mensen betekenisvol verantwoordelijk maken via controlepunten waar goedkeuring nodig is; technische controles over de hele levenscyclus; verantwoordelijkheid van de eindgebruiker via transparantie en training. Hill (Bloomberg, 2026): besturen spreken hun risicobereidheid zelden uit; "what is our risk appetite as we begin to … roll out AI solutions". De EU-AI-verordening komt in de wiki alleen in bijzinnen voor (Blank-college; een open vraag op de Allen-pagina). Risicoklassen en bijlage III staan er niet in.
- **4.1 (Fung / Anthropic, Code with Claude 2026-05-08)**: herschreven normen in het Claude Code-team: "JIT planning (no more 6-month roadmaps); design docs out, prototypes in". Slide 3 over het ritueel "design doc before any code": "For most work it was theater. Replaced with prototype-first. The doc, if it needs to exist, comes after." De verificatie wordt juist zwaarder: "shift left". Dit weerspreekt de LRD-tabel die design docs (Google, Ubl 2020) als werkwijze van AI-bedrijven presenteert, en het buildplan als roadmap voor een heel jaar.
- **Schluntz & Zhang (Anthropic, 2024-12-19)**: "Find the simplest solution possible, and only increase complexity when needed. This might mean not building agentic systems at all." Dit bevestigt de LRD-claim (`examples`, Anthropic).
- **Sadun & Wood (WorkLab 2025-11-24)**: "programmes that combine hard and soft skills, run in cohorts, and are part of a journey rather than an episode work better than self-paced platforms". "It's not just enough to do a pilot. You want to have hypothesis. You want to have measurement and you want to learn."

### Waar Niveau 3 verkort is

- Kropp is gelezen tot en met de eerste twee van de vier faalwijzen; de cijfers van alle vier staan in de TL;DR, de vijf aanbevelingen ook.
- responsible-ai (61 KB) is alleen op secties gelezen.
- Geen nieuwe pagina's voor de didactische kaders. Grep geeft 0 treffers op Kolb, COM-B, ADKAR, Mendelow, "Pink"/Drive-als-motivatietheorie en "AI-verordening". "7S" alleen als woord: 0. Kotter: 4 vermeldingen, nergens uitgewerkt. "Bloom" verwijst naar het woord, niet naar de taxonomie. De bronnen zijn hier op; dat is geen leesbeperking.
- Over AI die bronnen of citaten verzint (risico in de LRD) heeft de wiki geen bron die het meet; grep op fabricat/hallucinated citation levert niets relevants op.

## Synthese

Kernelementen voor de output (de toets zelf staat in het `related_output`-bestand):
- Diagnose en richting van de LRD (van experiment naar structurele inzet; eigen casus; experiment met norm vooraf; test gates) sluiten aan bij de sterkst onderbouwde wiki-uitspraken (micro-productivity trap, Dutt et al., Sadun).
- Grootste spanning: de bouwstraat werkt van één use case naar één product. De wiki zegt met 7+ bronnen dat procesherontwerp (workflow end-to-end) de waarde maakt en dat taakwinst zonder herontwerp verdampt (BBC/Hare, radiologie). De LRD heeft geen expliciete stap voor workflowherontwerp.
- Normen in het experiment: de wiki vraagt om vergelijking met de werkwijze zonder AI (Dutt) en om uitkomstmaatstaven in plaats van kostenmaatstaven (BCG, Brynjolfsson). De LRD vraagt alleen een norm vooraf.
- Pilots blijven hangen als ze niet in de beslisstromen van het bedrijf zitten (Allen/AWS, ~30% pilot → productie). De test gates in het buildplan gaan nu over het artefact, niet over integratie en adoptie.
- Menskant: Hines-Pierce 70/20/10. Carucci: weerstand is data, niet iets om om te zetten. Werkplaats 3 oefent een overtuigingsgesprek, wat dicht tegen Carucci's valkuil "rushing to resolution" aan zit.
- Boards: Csaszar onderbouwt dat een LLM als beoordelaar werkt (op businessplanniveau). Mollick: AI is een sycophant, vraag om kritiek. Kropp: personificatie verlaagt verantwoordelijkheid en foutdetectie. Allen & McDonald: modellen zijn zwak juist bij vooruitkijkende strategische commitment. Boussioux en Haghighi: diversiteit van perspectieven is niet gegarandeerd.
- LU1-blok "Wat AI kan en niet kan": de jagged frontier en "familiarity training can backfire" pleiten voor eerst doen en de grens laten ontdekken, met de grens expliciet in beeld.
- Interactief verslag: AI verbetert de presentatie los van de inhoud (Dell'Acqua). Beoordeel dus de opbouw, wat de LRD met AC-15 al doet.
- "Zo bouwen AI-bedrijven" (6.4): de wiki laat zien dat AI-bedrijven het onderling oneens zijn. Anthropic (Fung) schafte design docs vóór de code af ("theater") en ook roadmaps van zes maanden. De LRD presenteert design docs en een roadmap voor jaar 1 als de werkwijze.
- Wiki zwijgt: EU-AI-verordening (risicoklassen), McKinsey 7S, ADKAR, Kotter (alleen genoemd), Mendelow, COM-B, Kolb, Bloom, Pink.

## Bronnenmatrix

| Wiki-pagina | Gebruikte claim |
| ----------- | --------------- |
| `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | Elf lagen; procesherontwerp als belangrijkste kostenpost (7 bronnen); senior-leader ownership (McKinsey-citaat); pilots als fase of als val, met de verzoening "pass through quickly"; *Rewired* ~20% EBITDA, $3:$1, 1–2 jaar; rijpe bovenkant 7–15%; geen brug naar Kotter/Lewin |
| `wiki/sources/2026-05-02-dutt-chatterji-ai-experimentation-to-transformation.md` | Micro-productivity trap; vier stappen; metrics "comparisons with non-AI methods" + evals; FabricationCo (workshop, 14 use cases, 15×, +10 pp); Lowe's-pilots → 1.700+ winkels; boardroom imperative |
| `wiki/syntheses/ai-worker-maturity-levels.md` | L0–L5; evaluatie als bindende beperking; L1→L2 betaald denkmodel, kritiek vragen; L2→L3 acceptatiecriteria vóór het verzoek; zelfrapportagegat van 39 punten; ladder op codewerk gebouwd |
| `wiki/concepts/spec-driven-development.md` | Vage specs kosten meer met AI (Ivers); review verschuift naar vóór de bouw; kosten (markdown-wildgroei, partial waterfall); debat prototype tegenover document; confidence 0.75, geen gemeten uitkomst |
| `wiki/concepts/micro-productivity-trap.md` | MIT NANDA 95% (Allen; steekproef 153); PwC 56% / één op de acht; ~30% pilot → productie; MGI <40% van 90%; toegang tot training 3:1 + imagination gap; 70/20/10 (Hines-Pierce) + governanceteam in het midden; J-curve + "a little lazy"; BCG over herontwerp in plaats van kosten; Argenti 3× in plaats van 20%; Kiron-Schrage-cyclus + capture logs + "interestingly wrong"; Ransbotham 6×; "diagnosis corroborated far more strongly than any of its numbers" |
| `wiki/sources/2026-05-07-carucci-resistance-as-data.md` | Weerstand is data; drie valkuilen (o.a. "rushing to resolution"); vier signalen; faux-inclusion; "Be willing to adapt the plan"; geen data |
| `wiki/sources/2026-06-16-mollick-simon-sinek-ai-skills-experience-edge.md` | Ervaring is het voordeel (BCG: junioren slechter); $20-beslissing + denkmodel kiezen; prompt engineering doet er niet meer toe; zwaardere taken; "AI is a sycophant — tell it to act like a critic"; persona-prompts; inspanning tegenover resultaat |
| `wiki/concepts/jagged-frontier.md` | Dell'Acqua +12,2/+25,1/+33,9% binnen, −19 pp buiten; subjective coherence; familiarity training backfires; Allen & McDonald exploitation bias, kartel bij vooruitkijkende commitment; Boussioux convergentie naar het gemiddelde; Böckeler kans × impact × detecteerbaarheid |
| `wiki/sources/2024-12-01-csaszar-ketkar-kim-ai-strategic-decision-making.md` | LLM's maken en beoordelen businessplannen op menselijk niveau; Devil's Advocate-vignet; risico op conventionele strategieën; modellen uit 2023–24 |
| `wiki/sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees.md` | Framing van AI als werknemer: −9 pp verantwoordelijkheid, +44% escalaties, −18% fouten gevonden, +13% onzekerheid over identiteit; "make accountability explicit and personal" |
| `wiki/sources/2026-06-12-dellacqua-cybernetic-teammate-field-experiment-genai-teamwork.md` | Individu + AI ≈ team (+0,37 SD tegen +0,24 SD); AI als grensoverschrijder tussen silo's; team + AI ~3× zo vaak top-10%; zelfbeoordeling losgekoppeld van prestatie |
| `wiki/concepts/responsible-ai.md` | IMDA, vier pijlers (risico vooraf begrenzen, controlepunten voor menselijke goedkeuring); Hill: risicobereidheid uitspreken + beslisrechten; AI-verordening niet uitgewerkt |
| `wiki/sources/2025-11-24-sadun-wood-worklab-hard-to-become-ai-first-organization.md` | Cohortprogramma's met harde en zachte vaardigheden, als traject en niet als losse gebeurtenis; "hypothesis … measurement … learn" |
| `wiki/sources/2026-05-08-running-an-ai-native-engineering-org.md` | Anthropic: design docs eruit, prototypes erin ("For most work it was theater"); geen roadmaps van 6 maanden meer (JIT planning); verificatie naar voren halen |
| `wiki/sources/2024-12-19-anthropic-building-effective-agents.md` | "Find the simplest solution possible … This might mean not building agentic systems at all" |
