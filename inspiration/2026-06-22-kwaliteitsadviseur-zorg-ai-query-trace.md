---
type: query-trace
question: "De kwaliteitsbewaking in de zorg staat onder druk. AI kan oplossingen bieden. Wat betekent dit voor onze rol als kwaliteitsadviseur? Hoe bewegen zij mee? Hoe passen ze de dagelijkse werkzaamheden aan?"
date: 2026-06-22
language: nl
trace: "2026-06-22-kwaliteitsadviseur-zorg-ai-query-trace.json"
pages_used: 8
pages_ignored: 33
---

# Query trace — Kwaliteitsadviseur in de zorg & AI

## 1. Question
- **Original:** De kwaliteitsbewaking in de zorg staat onder druk. AI kan oplossingen bieden. Wat betekent dit voor onze rol als kwaliteitsadviseur? Hoe bewegen zij mee? Hoe passen ze de dagelijkse werkzaamheden aan door slim gebruik te maken van de nieuwe mogelijkheden en kansen die zich in een razend tempo verder ontwikkelen?
- **Restated:** Wat betekent de opkomst van AI voor de rol van de kwaliteitsadviseur in de zorg, en hoe past die zijn dagelijkse werk aan om bij te blijven bij snel ontwikkelende AI-mogelijkheden?
- **Facets:** 1) hoe AI de *rol* van kennis-/kwaliteitsprofessionals hervormt; 2) hoe professionals hun *dagelijkse werk aanpassen* (augmentatie, taak-herontwerp, human-in-the-loop); 3) AI toegepast op *kwaliteitsbewaking/toezicht zelf* (zorg-specifiek, accountability, governance van de AI); 4) hoe je het *tempo bijhoudt* (dynamische capaciteit, duurzame vaardigheden, continu leren).

## 2. Paths explored
41 kandidaten uit `wiki-retrieve.mjs` (qmd ∪ graph, RRF-gefuseerd, decay-herrangschikt). `graph_available: true`, geen `graph_warning`.

**qmd hits** (relevantie-stream)

| # | Page | type | qmd score | fused | verdict |
|---|------|------|-----------|-------|---------|
| 1 | `wiki/sources/2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero.md` | source | 0.53 | 0.94 | IGNORE |
| 2 | `wiki/sources/2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care.md` | source | 0.42 | 0.93 | **USE (W2)** |
| 3 | `wiki/sources/2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont.md` | source | 0.39 | 0.91 | IGNORE |
| 4 | `wiki/sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees.md` | source | 0.36 | 0.90 | **USE (W4)** |
| 5 | `wiki/concepts/ai-employment-effects.md` | concept | 0.36 | 0.91 | IGNORE |
| 6 | `wiki/concepts/responsible-ai.md` | concept | 0.35 | 0.88 | **USE (W8)** |
| 7 | `wiki/sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era.md` | source | 0.33 | 0.86 | IGNORE |
| 8 | `wiki/sources/2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work.md` | source | 0.30 | 0.84 | **USE (W5)** |

**graph neighbours** (`--hops 1`, typed-edge stream — selectie; volledige ledger in JSON)

| Page | reached via | fused | verdict |
|------|-------------|-------|---------|
| `wiki/sources/2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals.md` | peron --supports--> this | 0.41 | **USE (W3)** |
| `wiki/sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation.md` | scheffer/kropp --supports--> this | 0.46 | **USE (W6)** |
| `wiki/concepts/automation-vs-augmentation.md` | ai-employment-effects --supports--> this | 0.36 | **USE (W1)** |
| `wiki/concepts/durable-skills.md` | ai-employment-effects <--instance-of-- this | 0.35 | **USE (W7)** |
| `wiki/sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships.md` | peron/scheffer --supports--> this | 0.47 | IGNORE |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | peron --contradicts--> this | 0.40 | IGNORE |
| `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` | peron --supports--> this | 0.40 | IGNORE |
| `wiki/sources/2025-06-09-krakowski-human-centered-ai-field-experiment.md` | kropp/brynjolfsson --supports--> this | 0.39 | IGNORE |
| `wiki/concepts/ai-deskilling.md` | ai-employment-effects <--instance-of-- this | 0.35 | IGNORE |
| `wiki/concepts/enterprise-ai-adoption.md` | responsible-ai --part-of--> this | 0.35 | IGNORE |
| _(+ 22 verdere graph-only kandidaten — alle IGNORE; zie JSON)_ | | | |

**index.md / gap-expansion** (Stap 5): geen — de USE-set dekte alle vier facetten; geen uitbreidingsronde nodig.

## 3. Ignore policy applied
De reason-classes die deze run gevuurd hebben:
- `off-facet` — semantisch nabij (founder-/startup-/PM-/consulting-vantage) maar raakt geen van de vier facetten over de kwaliteitsadviseur-in-de-zorg.
- `redundant` — dekt dezelfde claim als een al-gekozen, hoger gerangschikte/zekerere pagina (meestal `automation-vs-augmentation`, `kropp`, `durable-skills` of `responsible-ai`).
- `wrong-granularity` — entiteit-catalogus-kaart waar het facet om een claim/cijfer vraagt (twee `missing:true` entity-kaarten).

## 4. Information ignored
| Page | reason-class | one-line reason |
|------|--------------|-----------------|
| `sources/2026-05-27-scheffer-helloprint-ai-rebuild-from-day-zero` | off-facet | SME-bedrijf-herbouw / kantoorbanen-eliminatie, niet de kwaliteitsadviseur-rol in de zorg |
| `concepts/ai-employment-effects` | redundant | macro "hervormt-meer-dan-vervangt" wordt gedragen door `automation-vs-augmentation` (W1) |
| `sources/2025-12-01-marily-nika-pms-who-use-ai` | off-facet | PM-specifiek "gebruik AI of word vervangen" |
| `sources/2026-05-07-singhal-stanford-cs153` | off-facet | productmanagement in het AI-tijdperk |
| `sources/2025-11-25-yee-mgi-agents-robots-and-us` | redundant | beroeps-archetypen gedragen door W1 + `durable-skills` (W7) |
| `sources/2026-04-24-hu-yc-build-company` | off-facet | startup-vanaf-de-grond-opbouwen |
| `sources/2026-05-24-erginbilgic-rolls-royce-turnaround` | off-facet | corporate turnaround-playbook |
| `sources/2026-05-27-koomen-yc-ai-playbook` | off-facet | YC-infrastructuur-playbook |
| `sources/2026-05-28-giles-wp-human-machine-workforce` | redundant | herinzet-als-augmentatie gedragen door W4 + W1 |
| `sources/2026-06-03-warren-yc-ai-native-services` | off-facet | services-bedrijf product-ontwerp |
| `sources/2026-04-25-masad-replit-only-two-jobs` | off-facet | maximalistische verdringingsclaim; spreekt Peron tegen maar niet op het kern-facet |
| `sources/2026-05-07-ransbotham-augmented-learners` | redundant | leren-onder-AI gedragen door Peron radiologen-gap (W2) + `durable-skills` (W7) |
| `entities/MIT-Sloan-Management-Review` | wrong-granularity | entiteitskaart (missing); facet vraagt om claim, niet om identiteit |
| `sources/2026-05-02-schoening-cultivating-agency` | off-facet | agency-boven-functietitels, Notion/PM-vantage |
| `entities/Sam-Ransbotham` | wrong-granularity | entiteitskaart (missing) |
| `sources/2025-06-09-krakowski-human-centered-ai-field-experiment` | redundant | interactie-ontwerp-contingentie gedragen door W1 §14 + W4 |
| `sources/2026-04-03-bcg-emerson-kropp-reshape-more-than-replaces` | redundant | hervorm-niet-vervang + vraag-expandeerbaarheid gedragen door W1/W4 |
| `sources/2026-02-09-sternfels-mckinsey-survive-ai` | off-facet | consulting-herontwerp; durable-skills-hiring gedragen door W7 |
| `sources/2026-05-02-dutt-chatterji-experimentation-to-transformation` | off-facet | enterprise-transformatie / micro-productivity-trap |
| `sources/2026-05-08-running-an-ai-native-engineering-org` | off-facet | engineering-organisatie |
| `sources/2026-06-11-mit-smr-agentic-ai-leaders-wish` | redundant | manage-agents-als-medewerkers-debat gedragen door W4 |
| `sources/2026-05-21-allen-aws-agentic-team-structures` | redundant | "mensen op oordeel, agents op uitvoering" gedragen door W1 |
| `concepts/enterprise-ai-adoption` | off-facet | organisatie-adoptiebesluit, niet de kwaliteitsadviseur-rol |
| `sources/2026-05-19-garg-internal-ai-agent-evolves` | off-facet | startup intern back-office-agent |
| `concepts/ai-deskilling` | redundant | deskilling/trainings-gap gedragen door W2 (radiologen-gap) + W8 |
| `sources/2026-03-25-russell-bradley-mgi-arenas` | off-facet | competitie-arena's |
| `sources/2026-04-14-thompson-workers-letting-ai` | redundant | durable-skills developer-vantage gedragen door W7 |
| `concepts/micro-productivity-trap` | off-facet | firm-niveau waarde-vertaal-val |
| `sources/2025-07-31-wang-agentspec-runtime-enforcement` | redundant | runtime-governance gedragen door W8 |
| `concepts/vibe-coding` | off-facet | code-bouwen |
| `sources/2026-04-21-forsgren-macvean-core-skills-developer` | redundant | durable-skills engineering-vantage gedragen door W7 |
| `concepts/document-intelligence` | off-facet | document-AI (effConf 0.666, read-aged maar primair off-facet) |
| `sources/2026-02-18-lyft-customer-support-with-claude` | redundant | klantenservice-augmentatie gedragen door W5 |

## 5. Information used
| Page | type | effConf | contribution |
|------|------|---------|--------------|
| `concepts/automation-vs-augmentation` | concept | 0.93 | de centrale snede augment-vs-automate; "mensen op oordeel, agents op uitvoering"; Ask→Assist→Automate-ladder; betrouwbaarheid als drempel voor autonomie |
| `sources/2026-05-31-peron-mit-smr-philips-interoperability-health-care` | source | n.v.t. (bron) | zorg augment-niet-vervang; radioloog-verdringing-die-niet-kwam; SmartArt 15min→30s; "meer met dezelfde" bij structureel tekort; AI-als-klinische-bias-auditor; radioloog-trainings-gap |
| `sources/2026-04-09-dinakaran-yc-luminai-hospitals` | source | n.v.t. (bron) | AI op administratief/operationeel zorgwerk: fax-triage, data-transformatielaag, geverticaliseerde agents, ~$1bn administratieve verspilling |
| `sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees` | source | 0.85 | accountability/foutvangst (18% minder fouten gevangen onder AI-medewerker-framing); 5-punts-herontwerp; beslisrechten/escalatie/gevolgen; augmenteerbaar-vs-substitueerbaar |
| `sources/2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work` | source | n.v.t. (bron) | empirie: +15% productiviteit, +30% voor minst ervaren, 3× sneller leren, human-in-the-loop-ontwerp; kwaliteitsdaling bij topkrachten |
| `sources/2026-04-28-warner-wager-dynamic-capabilities` | source | n.v.t. (bron) | digitale transformatie = doorlopend proces van strategische vernieuwing; sensing/seizing/transforming; agility als kernmechanisme |
| `concepts/durable-skills` | concept | 0.93 | waarin te investeren: kritisch denken/samenwerken/creativiteit/oordeel, expert-als-evaluator, AI-geletterdheid, upskillen-boven-aannemen, frequent bijscholen, mindset-niet-skillset |
| `concepts/responsible-ai` | concept | 0.95 | de AI zélf governen: mens-accountability-ketens, Singapore agentic-governance, policy-enforcement-buiten-de-LLM-loop, AI-als-bias-auditor, "learn responsibly", stijgende incidenten, deskilling-val |

## 6. Answer-element map
| Anchor | Answer element (claim) | Wiki page(s) | Section / span |
|--------|------------------------|--------------|----------------|
| [W1] | augment-vs-automate als centrale snede; mensen op oordeel/agents op uitvoering; Ask→Assist→Automate; betrouwbaarheid is de autonomie-drempel | [[concepts/automation-vs-augmentation\|automation-vs-augmentation]] | §Working definition, §2 Task design, §10, §12 |
| [W2] | zorg = augment niet vervang; structureel tekort → "meer met dezelfde"; SmartArt 15min→30s; AI-als-klinische-bias-auditor; radioloog-trainings-gap | [[sources/2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care\|Peron / MIT SMR]] | TL;DR 1–2 & 5, §Recurring frame |
| [W3] | AI op administratief/operationeel zorgwerk: fax-triage → gestructureerde data → routering; administratieve verspilling | [[sources/2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals\|Dinakaran / Luminai]] | §1 Cleveland Clinic worked example |
| [W4] | accountability persoonlijk houden; AI-medewerker-framing daalt accountability/verhoogt escalatie/vangt minder fouten; 5-punts-herontwerp | [[sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees\|Kropp et al. / BCG-HBR]] | §Headline finding, §Four failure modes, §Five-point prescription |
| [W5] | human-in-the-loop-ontwerp levert +15% (+30% novicen, 3× sneller leren); kwaliteitsdaling bij topkrachten als waarschuwing | [[sources/2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work\|Brynjolfsson, Li & Raymond]] | §Headline result, §Equalizing effect, §AI tool design |
| [W6] | transformatie = doorlopend proces van strategische vernieuwing; sensing/seizing/transforming; agility | [[sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation\|Warner & Wäger]] | §Process model, §Definition |
| [W7] | duurzame vaardigheden; expert-als-evaluator; AI-geletterdheid; upskillen-boven-aannemen + frequent; mindset-niet-skillset | [[concepts/durable-skills\|durable-skills]] | §Working definition, §Kiron-Schrage, §Argenti, §BCG |
| [W8] | de AI zelf governen: mens-accountability-ketens, agentic-governance, enforcement-buiten-LLM-loop, AI-als-bias-auditor, "learn responsibly", deskilling-val | [[concepts/responsible-ai\|responsible-ai]] | §Singapore agentic-governance, §nine-German-women, §Learn responsibly, §Incidents rising |

## 7. Final answer

**Korte kadering eerst.** De wiki bevat geen bron die specifiek over de *kwaliteitsadviseur in de zorg* gaat. Dit antwoord is samengesteld uit aangrenzend materiaal — twee zorg-AI-bronnen (Philips, Luminai), het algemene automatisering-vs-augmentatie-raamwerk, accountability-onderzoek (BCG/HBR), en de concepten duurzame vaardigheden, verantwoorde AI en dynamische capaciteiten. De redenering is overdraagbaar, niet één-op-één gedocumenteerd voor jouw functie.

**1. Wat AI in de zorg verandert — en waarom dat goed nieuws is voor kwaliteit.**
In de zorg is de bindende beperking geen arbeidskosten maar een structureel tekort aan capaciteit; daardoor doet AI hier "meer met dezelfde mensen" in plaats van mensen te vervangen [W2]. Concreet: Philips' SmartArt comprimeert de setup van een cardiale MRI van ~15 minuten naar 30 seconden (FDA-clearance 2026), verviervoudigt de doorvoer en elimineert de terugbel-lus bij gemiste beelden [W2]; Luminai zet de papier-en-faxstroom van ziekenhuizen om in gestructureerde data en routeert die via "geverticaliseerde agents" — het deel van de circa $1 biljoen administratieve verspilling in de zorg [W3]. En AI kan zélf een kwaliteits- en bias-auditor worden: het voorbeeld van de norm voor "normaal" postpartum-bloedverlies, ooit vastgesteld op negen Duitse vrouwen en wereldwijd uitgerold, plus de op-mannen-gebaseerde cardiale protocollen, laten zien hoe een agent klinische richtlijnen op populatieschaal kan toetsen [W2][W8].

**2. Wat dit betekent voor je rol.**
De kern: AI *voegt toe, neemt niet over* — de tien jaar oude voorspelling dat radiologen zouden verdwijnen is niet uitgekomen; AI neemt het laagwaardige werk, de mens houdt het oordeelswerk [W2]. Het scharnierprincipe is "mensen op oordeelswerk, agents op uitvoeringswerk" [W1]. Voor de kwaliteitsadviseur betekent dat een verschuiving van zélf kwaliteit controleren naar het *ontwerpen en bewaken van het systeem* waarin mens en AI samen kwaliteit leveren — accountability expliciet en persoonlijk houden, en beslisrechten, escalatietriggers en gevolgen vastleggen [W4]. Dit is precies de valkuil die jij moet bewaken: zodra AI als "collega/medewerker" wordt neergezet, daalt de persoonlijke accountability (9 procentpunt), stijgt escalatie (44%) en worden 18% mínder fouten gevangen — positioneer AI daarom als *software-met-menselijke-verantwoordelijkheid*, niet als teamlid [W4]. En je remit verbreedt: niet alleen zorgkwaliteit bewaken, maar ook *de AI zelf* governen — AI-incidenten stijgen (362 gedocumenteerd in 2025), en kaders zoals Singapore's agentic-governance vereisen herleidbare mens-accountability-ketens, agent-identiteit en handhaving van regels *buiten* de LLM-loop ("je stopt het bij de gateway, je vraagt het de agent niet vriendelijk") [W8].

**3. Hoe je meebeweegt met het tempo.**
Behandel dit niet als een eenmalig project maar als een *doorlopend proces van strategische vernieuwing*: signalen scannen (sensing), snel prototypen en je portfolio balanceren (seizing), en structuren en volwassenheid herontwerpen (transforming) — met wendbaarheid als kernmechanisme [W6]. Investeer in de vaardigheden die waardevol blijven naarmate AI codificeerbaar werk overneemt: kritisch denken, samenwerken, creativiteit en oordeelsvermogen — en specifiek de rol van *expert-als-evaluator* (beoordelen wat de AI produceert), met AI-geletterdheid als complement; upskillen verslaat aannemen, en doe het *frequent*, niet eenmalig [W7]. De onderliggende houding is mindset-niet-skillset: het vermogen om vertrouwde gewoonten los te laten en een nieuwe beroepsidentiteit aan te nemen [W7].

**4. Hoe je je dagelijkse werk concreet aanpast.**
- **Fase je AI-inzet via de Ask→Assist→Automate-ladder.** Begin read-only (Ask: ophalen/beantwoorden, bronnen valideren), dan aanbeveling-met-menselijke-validatie (Assist), en automatiseer pas wat betrouwbaar goed gaat. Je kunt niet nul-naar-Automate, zeker niet in een gereguleerde omgeving — en *betrouwbaarheid* (niet alleen capaciteit) is de drempel die bepaalt of iets autonoom mag draaien [W1].
- **Houd human-in-the-loop als default.** De empirisch sterkste augmentatiewinst (+15% productiviteit, +30% voor de minst ervaren werkers, ~3× sneller de leercurve af) kwam juist uit een ontwerp waarin de mens volledige discretie hield om suggesties te accepteren, aan te passen of te negeren [W5]. Let op de keerzijde die jij moet bewaken: topkrachten kunnen een lichte kwaliteitsdaling vertonen door té veel met de AI mee te gaan [W5].
- **Zet AI in om het kwaliteitswerk zelf te versterken.** Audit protocollen/richtlijnen tegen de brondata, spoor populatie-bias op, flag afwijkingen [W2][W8]; automatiseer de administratieve kwaliteitslast (intake, routering, dossiers) zodat menselijke aandacht naar oordeels- en empathiewerk gaat [W3][W2].
- **Herontwerp de rol expliciet (de 5 punten van BCG):** benoem werkprocessen én nieuwe (menselijke) rolverwachtingen; maak accountability persoonlijk; bouw een capability-plan voor wie agents superviseert; dwing agents niet in 1-op-1-rollen; en maak bewuste keuzes over hoe het menselijke werk evolueert richting oordeel, creativiteit en eigenaarschap [W4].
- **Bewaak "verantwoord leren" en de deskilling-val.** Als AI alle "normale" gevallen afhandelt, hoe blijven mensen dan kalibreren tegen normaal? (de open radioloog-trainingsvraag) — borg dat opleiding en kalibratie blijven doorlopen, en eis dat governance-kaders dit afdwingen [W2][W8].

In één zin: je beweegt van *controleur van kwaliteit* naar *ontwerper en bewaker van het mens-AI-kwaliteitssysteem* — je houdt mensen op het oordeelswerk en accountability, je laat AI het routinematige toezicht- en administratiewerk versnellen, je governt de AI zelf als nieuw kwaliteitsobject, en je houdt je vaardigheden en die van je team continu bij [W1][W4][W7][W8].

## 8. Trace artifact
Machine-readable provenance: [`2026-06-22-kwaliteitsadviseur-zorg-ai-query-trace.json`](2026-06-22-kwaliteitsadviseur-zorg-ai-query-trace.json)
