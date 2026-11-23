---
type: research-log
topic: "Hoe verhoudt de Frontier Firm (Microsoft/HBS) zich tot het dynamic-capabilities-procesmodel van Warner & Wäger (2019)?"
date: 2026-11-22
output_target: "wiki-synthese (thread + synthese, zelfde sessie)"
related_output: "wiki/syntheses/dynamic-capabilities-and-the-frontier-firm.md"
---

# Research log — Dynamic capabilities (Warner & Wäger) en de Frontier Firm

## Afwijkingen van de skill

- **Niveau 1 is niet uit `wiki/index.md` geselecteerd.** De index is 882 KB en past niet in één keer in context. In plaats daarvan: gerichte grep op W&W-termen in de index, plus één qmd-query (`wiki-query.mjs --no-bump`, 10 hits), conform CLAUDE.md §Search bij vragen die meer dan vijf pagina's raken.
- **De Frontier Firm-bronnen waren al gelezen.** Ze zijn in dezelfde sessie geïngest (Ignite 2026, de Frontier Playbook) of eerder gelezen voor de `/wq frontier firm`-vraag (HBS-pagina, Sadun, George, Bornet, Diasio, Lakhani). Ze zijn daarom niet opnieuw geopend; de query richtte zich op de W&W- en dynamic-capabilities-kant.
- **Niveau 3 is verkort**: drie gerichte passages, geen nieuwe volledige pagina's.

## Niveau 0 — startvragen

1. Welke microfundamenten en uitkomsten uit het W&W-procesmodel (sensing, seizing, transforming; strategische vernieuwing; context) zijn terug te zien in wat de Frontier Firm-bronnen beschrijven?
2. Waar gaat het Frontier Firm-concept verder dan W&W of wijkt het ervan af (agents als werkkracht, token capital, hill-climbing), en waar schiet W&W daar tekort?
3. Hoe sterk is het bewijs aan beide kanten (academisch kader tegenover vendor-playbook), en wat zeggen de bronnen over het meten van zo'n koppeling?

## Niveau 1 — pagina's

Geselecteerd:
- `wiki/concepts/warner-wager-process-model.md` (concept) — voor Q1
- `wiki/sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation.md` (source) — voor Q1, Q2
- `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` (synthese) — voor Q3
- `wiki/concepts/dynamic-capabilities.md` (concept, alleen sectiestructuur op niveau 1) — voor Q2, Q3

### Antwoorden
- **Q1**: W&W kent 15 cellen. Microfundamenten: scouting, scenario planning, mindset crafting; rapid prototyping, portfolio balancing, strategic agility; ecosystems, internal structures, digital maturity. Uitkomsten: verdienmodel, samenwerking, cultuur. Context: triggers, enablers, barriers. Bron: Warner & Wäger, *Long Range Planning* 2019; zeven Duitse incumbents en 18 consultantinterviews, veldwerk 2016–17.
- **Q2**: W&W definiëren digitale transformatie als *"an ongoing process … agility as the core mechanism for the strategic renewal of an organization's (1) business model, (2) collaborative approach, and eventually the (3) culture."* Teece: ordinary capabilities zijn *"outsourceable to the cloud"* en daarom niet duurzaam.
- **Q3**: De negen W&W-cellen zijn nooit kwantitatief getest; alleen de generieke ruggengraat sense/seize/transform wel (Cimino, n=210). De bestaande synthese noemt als open vraag een *"cross-walk with academic strategy theory … integrate the cluster with [[dynamic-capabilities]] (Teece)"*. Deze query beantwoordt die vraag dus voor één kader.

### Niveau-1 vragen
Van W&W-concept: 1.1 Welke cellen raken de Frontier Firm-bronnen niet? 1.2 Heeft het AI-tijdperk cellen nodig die W&W niet heeft? 1.3 Komt de eigenaarschapsverdeling (role defaults) overeen met de Frontier Firm (CEO, AITO, named executive owner)?
Van W&W-bron: 2.1 Wat doet AI met het onderscheid tussen ordinary en dynamic capabilities? 2.2 Is "agility als kernmechanisme" terug te zien als continu experimenteren? 2.3 W&W zetten cultuur als laatste ("eventually"); de Frontier Firm noemt mensen "the most important section". Volgorde of tegenspraak?
Van synthese: 3.1 Is de cross-walk met academische strategietheorie sindsdien ergens gedaan? 3.2 Past "models commoditize; what's owned compounds" op de hill-climbing machine? 3.3 Is de "compounding cycle" dezelfde als het innovation flywheel van de playbook?

## Niveau 2 — links gevolgd

Geselecteerd:
- `wiki/concepts/dynamic-capabilities.md`, secties Debates, *The spine, measured*, *TOE*, *Concentration…*, *Mobilization…*, *Sensing, rewiring, lock-in*, *Business-model renewal…* — voor 1.2, 2.1, 3.1
- `wiki/sources/2025-08-05-hbs-ai-institute-mastering-change-resilience-key-to-ai-driven-success.md` — voor 1.2, 3.1, 3.3
- Telling van `dynamic_capabilities:`-tags over negen Frontier Firm-bronnen — voor 1.1

### Antwoorden
- **1.1**: Tagtelling over negen bronnen: improving-digital-maturity 8; redesigning-internal-structures 6; rapid-prototyping 6; digital-mindset-crafting 4; internal-barriers 4; organizational-culture 3; internal-enablers 3; business-model 2; external-triggers 2; strategic-agility 1. Nul keer: scouting, scenario planning, balancing portfolios, ecosystems, collaborative approach. Kanttekening: dit is de eigen codering van de wiki; de financefunnel van Hrncirik is in feite portfoliokeuze.
- **1.2 / 3.1 / 3.3**: Lakhani, Stave, Ng & Martines (HBR 2025, via de HBS AI Institute-samenvatting) splitsen change resilience in sensing, rewiring (*"days or weeks, not fiscal quarters"*) en lock-in (*"codify what a team learns … higher baseline"*). Dat valt één op één samen met Teece; de samenvatting citeert hem niet. Ze voegen een tijdschaal en "Care" toe. Het HBS AI Institute voert het Frontier Firm-initiatief mee uit.
- **2.1 / 3.2**: Cimino 2025: dynamische capaciteiten voorspellen acceptatie (β 0,523) sterker dan implementatie-intensiteit (β 0,279), en economische prestaties niet (β 0,138, niet significant). Nguyen 2026: capaciteiten volgen op adoptie; AI versterkt bestaand voordeel.
- **Bevilacqua 2025** (in dezelfde sectie): de meest impactvolle AI-initiatieven kwamen van middenmanagers en de werkvloer; het topteam legitimeert.

### Niveau-2 vragen
A1 Waar zit strategic agility (rewiring in dagen of weken) in de Frontier Firm? A2 Is "CI alone gives a leaner version of your old company" het ordinary/dynamic-onderscheid? A3 Botst het codificeren van impliciete kennis met Teece's onnavolgbaarheid?
B1 Is lock-in hetzelfde als het innovation flywheel en de hill-climbing machine? B2 Vult het people-hoofdstuk van de playbook W&W's gat rond "Care"? B3 Wat is het bewijs voor waarde (26% volgens BCG)?
C1 Waarom ontbreekt sensing? C2 Is het initiatief zelf een ecosysteem? C3 Waar komt verdienmodelvernieuwing voor?

## Niveau 3 — laatste passages (verkort)

- **A3 (Nadella/Hoffman)**: impliciete kennis is *"the unique ways that you are able to operate, pass judgment, have taste"*; modellen halen die eruit *"through human trajectories"*; lekken is *"a one-way door"*. Token capital.
- **2.3 (Sadun)**: *"this is the time to learn"*; elk bedrijf heeft zijn eigen J-curve; reskilling is *"bloody hard"*, met middenmanagers als scharnier.
- **C3 (Diasio)**: het lastigste voor EY is het billable hour: *"a business model that has been built on the billable hour, where people monetize their efforts."*
- A1 en C2 zijn beantwoord uit eerder gelezen materiaal: de Krishna/Bain-sectie in dynamic-capabilities, en de HBS-pagina (lidbedrijven, Harvard, Microsoft).

## Synthese

Kernelementen in de output:
- De Frontier Firm is een operationalisering voor het AI-tijdperk van W&W's transforming-cluster: een vergelijkingstabel element voor element.
- Sensing, portfolio's, ecosystemen en verdienmodel ontbreken grotendeels. Sensing bestaat alleen als mindset en als operationele ontdekking van onderop.
- Andere uitkomsten van vernieuwing: het operating model wordt vernieuwd, het verdienmodel nauwelijks. Over cultuur zijn ze het inhoudelijk eens, maar de volgorde verschilt.
- AI verschuift de grens tussen ordinary en dynamic. De playbook verplaatst onnavolgbaarheid van impliciete kennis naar gecodificeerde kennis die door architectuur wordt beschermd (ongetest, en de auteur verkoopt die bescherming).
- Lock-in als gedeeld mechanisme, met een tijdschaal en transforming als continue routine.
- Gedeeld bewijsgat. Hypothese: de Frontier Firm specificeert het implementatiebeen dat Cimino zwak vond.

## Bronnenmatrix

| Wiki-pagina | Gebruikte claim |
| ----------- | --------------- |
| [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation]] | definitie digitale transformatie; ordinary vs dynamic; steekproef |
| [[warner-wager-process-model]] | celvocabulaire; ongetest; dual-use-hypothese |
| [[dynamic-capabilities]] | Cimino, Nguyen, Bevilacqua, de mapping van sensing/rewiring/lock-in |
| [[syntheses/organizational-frameworks-for-ai-adoption]] | de open vraag naar een cross-walk met strategietheorie |
| [[2025-08-05-hbs-ai-institute-mastering-change-resilience-key-to-ai-driven-success]] | sensing, rewiring, lock-in; tijdschaal; 26% |
| [[2026-09-16-microsoft-becoming-a-frontier-firm-second-edition]] | Success Framework, AITO, recepten, CI + AI = CA, law of hill-climbing, "most important section" |
| [[2026-11-19-george-hrncirik-ignite-becoming-a-frontier-firm]] | financefunnel; "best ideas … closest to the work"; starfish (publiek); cijfers en scope |
| [[2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about]] | het initiatief als ecosysteem; ongepubliceerde case |
| [[2025-11-24-sadun-wood-worklab-hard-to-become-ai-first-organization]] | lerend bedrijf; reskilling "bloody hard" |
| [[2025-12-16-diasio-wood-worklab-agentic-ai-corporate-ladder]] | billable hour als verdienmodelprobleem |
| [[2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm]] | impliciete kennis, token capital, "one-way door", wereldbeeld |
| [[2025-06-15-cimino-ai-adoption-sustainable-growth-smes]] | β-waarden acceptatie, implementatie, economische prestaties |
| [[2026-03-28-nguyen-ai-adoption-toe-dynamic-capabilities]] | capaciteiten na adoptie; AI als versterker |
| [[2025-12-02-bevilacqua-ai-strategic-leadership-skills-top-managers]] | sensing van onderop |
