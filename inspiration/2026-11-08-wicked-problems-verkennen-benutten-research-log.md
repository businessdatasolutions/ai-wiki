---
type: research-log
topic: "Welke bronnen dragen het idee dat strategische AI-vragen wicked problems zijn, en dat verkennen en benutten (exploration/exploitation, meerarmige bandiet, Bayesiaans optimaliseren, reële opties, one-way/two-way doors) het patroon is om ermee te werken?"
date: 2026-11-08
output_target: "Geverifieerde bronnenlijst (APA 7, Nederlandse claim per bron, betrouwbaarheid) voor de herstructurering van de LRD AISO26009 rond vier leiderschapsvragen"
related_output: "/Users/witoldtenhove/Projects/aiso/LRD-AISO26009-lesdagen.html (herstructurering in uitvoering; de bronnenlijst gaat via het rapport aan de hoofdsessie)"
---

# Research log — wicked problems en verkennen/benutten als patroon

Aanleiding: de LRD van AISO26009 wordt opgebouwd rond vier leiderschapsvragen die als wicked problems worden neergezet, met verkennen en benutten als antwoordpatroon. Dat patroon krijgt drie vormen: de portfoliokaart van Strategyzer (strategie), de meerarmige bandiet en Bayesiaans optimaliseren (wiskunde), en reële opties met de one-way/two-way doors van Bezos (investeren). Gevraagd: welke bronnen dit dragen, en een controle van negen opgegeven citaten.

Werkwijze: `wiki/index.md` (secties Concepts, Syntheses, Threads volledig; Sources via grep) en daarna gerichte grep op de kerntermen in `wiki/` en `raw/`. Wat de wiki niet heeft, is op het web gecontroleerd (Crossref, OpenAlex, SEC EDGAR, Strategyzer, uitgeverspagina's, de auteurssite van Sutton & Barto en gescande originelen). Op verzoek van de opdrachtgever zijn geen wikipagina's aangepast: geen `accessed_at`-bump en geen regel in `wiki/log.md`. Er is niets gecommit.

## Niveau 0 — startvragen

1. Welke bronnen in de wiki beschrijven strategische vraagstukken, en AI-vragen in het bijzonder, als wicked problems, en welke eigenschappen noemen ze?
2. Welke bronnen dragen de spanning tussen verkennen en benutten (March), en wat meten ze over de neiging tot benutten, bij organisaties en bij AI-modellen?
3. Welke bronnen dragen de concrete vormen van het patroon: portfoliokaart, meerarmige bandiet en Bayesiaans optimaliseren, reële opties en one-way/two-way doors?

## Niveau 1 — pagina's uit index.md

Geselecteerd (4 pagina's, 2 types: concept en bron):
- `wiki/concepts/systems-thinking.md` — voor Q1
- `wiki/sources/2026-03-11-allen-mcdonald-how-well-can-ai-do-strategy-simulation-benchmark.md` — voor Q2
- `wiki/concepts/jagged-frontier.md` (r. 182–202) — voor Q2
- `wiki/concepts/strategy.md` (r. 249–269, plus grep op Bezos/McGrath) — voor Q1 + Q2

### Antwoorden

- **Q1 (systems-thinking, confidence 0.9)**: de sectie "Wicked problems (Rittel & Webber, 1973 — implicit reference)" noemt drie kenmerken: steeds veranderend en moeilijk te definiëren, veel belanghebbenden die de disfunctie verschillend ervaren, en oplossingen met lastige afwegingen. Systeemdenken past hier, doorbraakdenken en design thinking niet. Principe 2 van Bansal & Birkinshaw: "wicked problems lack a single definition"; herformuleer het probleem steeds opnieuw. Belangrijk: de wiki verwijst naar Rittel & Webber zonder de bron zelf of de tien kenmerken te hebben.
- **Q1 + Q2 (strategy)**: Allen & McDonald definiëren strategische beslissingen met vijf kenmerken: "complexity/interdependence, high stakes, multiperiod partially-irreversible commitments, delayed and noisy feedback, and deep uncertainty". Die lijst overlapt sterk met Rittel & Webber (onomkeerbaarheid, geen directe toets, diepe onzekerheid) en is de brug van wicked problems naar strategie. Over de neiging tot benutten: "That is the innovator's dilemma restated as a property of a reasoner rather than of an organisation".
- **Q2 (Allen & McDonald, *Strategy Science* 11(1), 93–117, peer-reviewed, open access)**: 21 gesloten en 13 open modellen in de Back Bay Battery-simulatie (acht jaar R&D-budget verdelen tussen een krimpende kerntechnologie en een opkomende), vergeleken met 249 MBA-studenten. Modellen van eind 2024/begin 2025 (o3-mini het hoogst) scoren boven het MBA-gemiddelde. De frontiermodellen van midden/eind 2025 (GPT-5, o3, Gemini 2.5 Pro) zakken onder de lichtere modellen van begin 2025 én onder de studenten. Het mechanisme heet "systematic exploitation bias": hoge cumulatieve winst, zeer lage omzet uit de nieuwe technologie. Citaat Gemini 2.5 Pro: *"We will not invest any R&D into QSC this year, preserving our limited capital for the core business"*. Het patroon blijft bestaan zonder ontslagregel. Kanttekening van de bronpagina: de figuurwaarden waren niet machineleesbaar, dus er staan geen scores in de wiki, alleen richtingen en rangordes.
- **Q2 (jagged-frontier)**: de kartel zit bij "forward-looking commitment under delayed feedback — which is exactly the region where a manager is most tempted to delegate a judgment". De kartel sluit niet met nieuwere modellen; de correlatie met GPQA Diamond draait na o4-mini om van positief naar negatief. Wang et al. (CHI '25): bij conceptontwerpers loopt de grens tussen de verkenfase (AI sterk) en de verfijnfase (AI zwak).

### Niveau-1 vragen

Van systems-thinking: 1.1 Wat zegt de oorspronkelijke bron (Bansal & Birkinshaw) over welke aanpak bij wicked problems past? 1.2 Heeft de wiki de lijst van Rittel & Webber zelf? 1.3 Wat betekent "nudge your way forward" als werkpatroon?
Van Allen & McDonald: 2.1 Op welke theorie over verkennen en benutten bouwen ze? 2.2 Welke cel van Warner & Wäger meet dit? 2.3 Zien we dezelfde neiging tot benutten bij organisaties?
Van jagged-frontier: 3.1 Waar bijt de kartel voor managers? (beantwoord op de pagina) 3.2 Zijn er bronnen over het delegeren van omkeerbare en onomkeerbare besluiten? 3.3 Verkenfase tegenover verfijnfase (beantwoord op de pagina, Wang et al.)
Van strategy: 4.1 Welke van de vijf kenmerken overlappen met wicked problems? (beantwoord hierboven) 4.2 Heeft de wiki het deurenvocabulaire van Bezos? 4.3 Heeft de wiki reële opties of McGrath (1999)?

## Niveau 2 — links gevolgd

Geselecteerd (4 pagina's, plus gericht in `raw/`):
- `wiki/sources/2026-04-28-bansal-birkinshaw-systems-thinking.md` — voor 1.1 + 1.3
- `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` — voor 2.3
- `wiki/sources/2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers.md` — voor 3.2 + 4.2
- `wiki/concepts/dynamic-capabilities.md` (r. 324–332) — voor 2.2
- Gericht: `raw/papers/how-well-can-ai-do-strategy-empirical-benchmarking-using-strategy-simulations.md` (r. 466–482 en de literatuurlijst) — voor 2.1 en 1.2

### Antwoorden

- **1.1 + 1.3 (Bansal & Birkinshaw, HBR sept–okt 2025, pp. 124–133)**: doorbraakdenken past bij afgebakende problemen ("rocketry"), niet bij "wicked, ill-defined problems (US healthcare/education)"; systeemdenken "best for wicked problems that affect arrays of stakeholders very differently". Principe 4 "Nudge your way forward": een "ecology of actions", kleine experimenten die inzicht in het systeem geven (de bron zet dit af tegen moonshots en silver bullets). Dat is het verkenpatroon in praktijktaal. Kwaliteitsvlag op de pagina: praktijkkader, geen empirisch onderzoek (Innovation North, 30+ bedrijven).
- **1.2**: nee. `grep -ri rittel` geeft één treffer (de "implicit reference" op systems-thinking). De tien kenmerken staan niet in de wiki.
- **2.1 (raw paper, r. 472–474)**: *"The simulation is designed to capture the classic strategic dilemma of balancing exploration and exploitation over time (March 1991, Benner and Tushman 2003, Gupta et al. 2006)."* Literatuurlijst: "March J (1991) Exploration and exploitation in organizational learning. Organ. Sci. 2:71–87." De tweede bron met March in `raw/` is de Cybernetic Teammate-paper (Dell'Acqua et al. 2026), alleen in de literatuurlijst.
- **2.2 (dynamic-capabilities)**: Allen & McDonald is "the most direct empirical measurement of a single Warner & Wäger cell — `digital-seizing/balancing-digital-portfolios`". Het faalpatroon: *"spreading investments too thin leads to mediocrity, ignoring disruption leads to decline, and over-committing too early leads to collapse."* Gevolg voor de pagina: een mens is nodig "not in the analysis … but in the commitment to an option whose payoff is not yet visible in the data". Dat is letterlijk de taal van reële opties.
- **2.3 (Ransbotham et al., MIT SMR × BCG, nov. 2024, 3.467 respondenten)**: stap 2 van vijf heet "Learn to explore with AI (not just exploit)". Augmented Learners (15% van de organisaties) gebruiken traditionele AI 2× zo vaak om nieuwe manieren van waardecreatie te verkennen, en generatieve AI 1,6× zo vaak; Limited Learners gebruiken AI 2× zo vaak om bestaande processen te verbeteren. Augmented Learners investeren 1,9× zo vaak in AI-projecten van meer dan vijf jaar en 2,4× zo vaak in projecten met hoog risico.
- **3.2 + 4.2 (Jassy, HBR IdeaCast 6 mei 2025)**: *"A two-way door decision is one where if you walk through it and you're wrong, you can walk back through it and no harm. A one-way door decision is when you walk through that door and you're wrong, it's really hard to walk it back."* Two-way-door-besluiten ("the overwhelming majority") horen bij de mensen die het werk doen. De bronpagina noemt het "Bezos-era Amazon vocabulary" en promoveert het niet tot concept (één bron). Er staat geen primaire Bezos-bron in de wiki.

### Niveau-2 vragen

A (Bansal): A1 Is "nudge your way forward" onderbouwd met data? (nee, praktijkkader) A2 Hoe verhoudt de kleine stap zich tot Rittel & Webbers waarschuwing tegen incrementalisme (kenmerk 8)? A3 Welke andere wikibronnen noemen wicked problems? (Webb, Boussioux: alleen als link)
B (raw paper): B1 Wat beweert March zelf? (wiki zwijgt → web) B2 Benner & Tushman en Gupta et al.: in de wiki? (nee) B3 Zijn er nog meer bronnen die het patroon als simulatie oefenen?
C (Ransbotham): C1 Is "2× vaker verkennen" causaal? (nee, enquête, samenhang) C2 Noemt de wiki een instrument om een verkenportefeuille te sturen? (nee: geen Strategyzer, geen portfoliokaart → web)
D (Jassy): D1 Is er een tweede bron voor het deurenvocabulaire? D2 Waar staat de primaire Bezos-tekst? (wiki zwijgt → web)

## Niveau 3 — laatste links

Verkort, omdat de wiki op de wiskundige en financiële vormen leeg is.

- **D1 (`wiki/sources/2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm.md`, r. 63)**: Nadella gebruikt de one-way door voor het weglekken van stille kennis naar modellenbouwers: *"if you leak it, it's a one-way door, you're done"*. Tweede bron voor het vocabulaire, in een AI-context. Bruikbaar als voorbeeld van een one-way door bij AI-besluiten.
- **B3 (`wiki/sources/2026-09-30-demaree-onebrief-ai-military-planning.md`, r. 245)**: Onebrief gebruikt een simulatie als terugkoppeling in een lus voor betere plannen; Allen & McDonald gebruiken een simulatie als meetlat. Beide zien simulatie als manier om besluiten met late terugkoppeling te beoordelen.
- **4.3 (grep)**: "real option" geeft 0 treffers in `wiki/` en `raw/`. De McGrath in de wiki is *strategic centering* (HBR 2026), een ander werk dan *Falling forward* (1999).
- **Lege plekken, vastgesteld met grep in `wiki/` en `raw/`**: "bandit" 0, "Bayesian optim" 0, "Osterwalder|Strategyzer|Invincible" 0, "Myers" alleen in een ongerelateerd transcript, "Sutton" alleen in ongerelateerde bronnen, "Rittel" alleen de impliciete verwijzing. Hier is de bronnenruimte op, niet de leesdiepte.

## Externe verificatie (web)

Per citaat: wat is gecontroleerd en waar.

1. **Rittel & Webber (1973)**. Crossref (DOI 10.1007/BF01405730): Horst W. J. Rittel, Melvin M. Webber; *Policy Sciences* 4(2), 155–169, juni 1973. De tien kenmerken zijn letterlijk gelezen in een scan van het origineel (ProQuest/Kluwer-herdruk, pp. 161–166). Kopjes, verbatim:
   1. "There is no definitive formulation of a wicked problem"
   2. "Wicked problems have no stopping rule"
   3. "Solutions to wicked problems are not true-or-false, but good-or-bad"
   4. "There is no immediate and no ultimate test of a solution to a wicked problem"
   5. "Every solution to a wicked problem is a 'one-shot operation'; because there is no opportunity to learn by trial-and-error, every attempt counts significantly"
   6. "Wicked problems do not have an enumerable (or an exhaustively describable) set of potential solutions, nor is there a well-described set of permissible operations that may be incorporated into the plan"
   7. "Every wicked problem is essentially unique"
   8. "Every wicked problem can be considered to be a symptom of another problem"
   9. "The existence of a discrepancy representing a wicked problem can be explained in numerous ways. The choice of explanation determines the nature of the problem's resolution"
   10. "The planner has no right to be wrong"
   Let op: het artikel gaat over maatschappelijke planning (armoede, criminaliteit, snelwegen), niet over bedrijfsstrategie. De brug naar strategie slaat Camillus (2008), "Strategy as a wicked problem", *HBR* 86(5), 98–106; die gegevens komen uit een catalogus, de tekst is niet gelezen. En kenmerk 5 ("geen leren met vallen en opstaan") staat op gespannen voet met naïef experimenteren; zie de synthese.
2. **March (1991)**. Crossref en OpenAlex (DOI 10.1287/orsc.2.1.71): James G. March, *Organization Science* 2(1), 71–87, februari 1991. Abstract, verbatim: *"The paper develops an argument that adaptive processes, by refining exploitation more rapidly than exploration, are likely to become effective in the short run but self-destructive in the long run."* Allen & McDonald citeren het (raw-paper).
3. **Osterwalder et al. (2020)**. Wiley-productpagina: titel en ondertitel *The Invincible Company: How to Constantly Reinvent Your Organization with Inspiration From the World's Best Business Models*, april 2020, 400 pp., The Strategyzer Series, ISBN 978-1-119-52396-3 (paperback), 978-1-119-52398-7 (e-book). **Auteursvolgorde**: de Wiley-pagina noemt Osterwalder, Pigneur, Smith, Etiemble. Strategyzers eigen boeksamenvatting ("Alexander Osterwalder, Yves Pigneur, Fred Etiemble, and Alan Smith") en een bibliotheekrecord met de verantwoordelijkheidsvermelding van de titelpagina ("written by Alexander Osterwalder, Yves Pigneur, Frederic Etiemble, Alan Smith") noemen Etiemble vóór Smith. Het persbericht van Wiley ("joined by Fred Etiemble and Alan Smith") ook. APA volgt de titelpagina: Osterwalder, Pigneur, Etiemble, Smith. **Assen**: Strategyzers boeksamenvatting noemt de dimensies "Innovation risk", "Expected return" en "Death & disruption risk". Pigneur (Strategyzer, 28-08-2017) beschrijft de verkenkaart: verwacht rendement (laag onder, hoog boven) tegen innovatierisico (geen bewijs links, getoetst op wenselijkheid, levensvatbaarheid en haalbaarheid rechts). De benutkaart zet rendement af tegen het risico op neergang en verstoring ("death & disruption risk"). In Pigneurs prototype uit 2017 heet de rendementsas nog "profitability". **Actiewerkwoorden**: NIET bevestigd uit een betrouwbare bron. Ze staan alleen in boeksamenvattingen van derden en in ongeautoriseerde PDF-kopieën van het boek (niet gebruikt). Strategyzers eigen pagina's noemen andere termen: "Ideation, Discovery, Validation" voor verkennen, "Transfer" voor de overgang, en bij Pigneur 2017 "improve", "divest", "spun off", "acquire". Controleer de zeven plus zeven werkwoorden in het boek zelf voordat ze in de LRD komen.
4. **Shahriari et al. (2016)**. Crossref (DOI 10.1109/JPROC.2015.2494218): Shahriari, Swersky, Wang, Adams, de Freitas; *Proceedings of the IEEE* 104(1), 148–175, januari 2016 (OpenAlex: online 2015; APA gebruikt het jaargangjaar 2016). Tekst van de auteursversie gelezen: *"These acquisition functions trade off exploration and exploitation; their optima are located where the uncertainty in the surrogate model is large (exploration) and/or where the model prediction is high (exploitation)."* Het artikel behandelt ook A/B-testen als een Beta-Bernoulli-bandiet met Thompson sampling. Daarmee verbindt één bron de bandiet en Bayesiaans optimaliseren.
5. **Allen & McDonald (2026)**. Uit de wikibronpagina (zie Niveau 1). De bronpagina noemt geen scores: de figuren waren afbeeldingen. Getallen die wel vaststaan: 34 modellen (21 gesloten, 13 open), 249 MBA-studenten in vijf cohorten, acht simulatiejaren.
6. **Myers (1977)**. Crossref en RePEc: Stewart C. Myers, *Journal of Financial Economics* 5(2), 147–175, november 1977. Werkpaperversie gelezen (MIT Sloan WP 875-76, september 1976, p. 3): *"Thus part of the value of a firm is accounted for by the present value of options to make further investments on possibly favorable terms."* Dat Myers de term "real options" bedacht, staat in secundaire bronnen: Wikipedia ("Real options valuation", met verwijzing naar Myers 1977) en de FAQ over reële opties van PUC-Rio. Het gepubliceerde abstract met de woorden "real options" kon niet worden opgehaald (ScienceDirect 403; Crossref, OpenAlex en RePEc hebben geen abstract). De zin "The value of such 'real options' depends on discretionary future investment by the firm" komt alleen uit een zoekresultaat en is dus niet eigenhandig gelezen.
7. **McGrath (1999)**. Crossref: Rita Gunther McGrath, *Academy of Management Review* 24(1), beginpagina 13, januari 1999; DOI 10.5465/amr.1999.1580438 is een alias van 10.2307/259034 (JSTOR). De eindpagina 30 komt uit catalogi van Columbia en bibliotheken, niet uit Crossref. Abstract via OpenAlex: *"Although failure in entrepreneurship is pervasive, theory often reflects an equally pervasive antifailure bias."* De aanpak: "pursuing high-variance outcomes, but investing only when conditions are favorable".
8. **Bezos**. Primaire bron: SEC EDGAR, Form 8-K van Amazon.com, Inc., gedateerd 5 april 2016. Exhibit 99.1 heet "2015 Letter to Shareholders". De deuren en Type 1/Type 2 staan in de brief over 2015, gepubliceerd in april 2016. Verbatim: *"Some decisions are consequential and irreversible or nearly irreversible – one-way doors – and these decisions must be made methodically, carefully, slowly, with great deliberation and consultation."* en *"But most decisions aren't like that – they are changeable, reversible – they're two-way doors."* Op aboutamazon.com staat de brief over 2015 niet als pagina (404). Daar staat wel de brief over 2016 (`aboutamazon.com/news/company-news/2016-letter-to-shareholders`), die het idee herhaalt en de 70%-informatieregel toevoegt.
9. **Sutton & Barto (2018)**. Auteurssite (incompleteideas.net): *Reinforcement Learning: An Introduction*, Second Edition, MIT Press, Cambridge, MA, 2018. Gratis PDF op dezelfde site. "Chapter 2: Multi-armed Bandits" (codepagina: 10-armed testbed, optimistic initial values, UCB, gradient bandits). ISBN 978-0-262-03924-6 en de reeks Adaptive Computation and Machine Learning komen uit catalogi.

## Synthese

Kernelementen voor de output (de bronnenlijst in het rapport aan de hoofdsessie):

- **Wicked problem → strategie → AI.** Rittel & Webber leveren de tien kenmerken. Bansal & Birkinshaw (wiki) passen het begrip toe op bedrijfsinnovatie. Allen & McDonald (wiki) definiëren strategische beslissingen met vijf kenmerken, waaronder "multiperiod partially-irreversible commitments" en "delayed and noisy feedback"; dat zijn kenmerken 4 en 5 van Rittel & Webber in bedrijfstaal. Camillus (2008) is de klassieke brug, maar nog niet gelezen.
- **Verkennen en benutten is de kern.** March: lerende organisaties verbeteren benutten sneller dan verkennen, wat op lange termijn zelfvernietigend kan zijn. Allen & McDonald meten precies dat bij de nieuwste taalmodellen ("systematic exploitation bias"). Ransbotham laat het bij organisaties zien: de 15% Augmented Learners verkennen 2× zo vaak met AI. De wiki legt de verbinding zelf: "the innovator's dilemma restated as a property of a reasoner".
- **Spanning om in de LRD te benoemen.** Rittel & Webber kenmerk 5 zegt dat leren met vallen en opstaan bij wicked problems niet kan, want elke poging laat sporen na. Dat lijkt het experimenteren te ondergraven. De verzoening zit in de andere drie bronnen: knip de one-way-door-vraag op in two-way-door-stappen (Bezos), koop met kleine investeringen het recht maar niet de plicht om door te zetten (Myers, McGrath), en verdeel proeven zo dat je tegelijk leert en verdient (bandiet, Bayesiaans optimaliseren). Bansal & Birkinshaw noemen dit in praktijktaal "nudge your way forward". De wiki bevestigt waar de mens nodig blijft: "in the commitment to an option whose payoff is not yet visible in the data" (dynamic-capabilities).
- **One-way doors bij AI.** Jassy (wiki) gebruikt het vocabulaire om besluiten te delegeren; Nadella (wiki) noemt het weglekken van stille kennis naar modellenbouwers een one-way door. Dat zijn bruikbare voorbeelden voor de lesdagen.
- **Wat de wiki niet heeft.** Geen pagina over reële opties, de meerarmige bandiet, Bayesiaans optimaliseren, de portfoliokaart van Strategyzer, of Rittel & Webber zelf. Kandidaten om in te nemen: March 1991, Rittel & Webber 1973, de 2015-brief van Bezos, McGrath 1999. "Exploration/exploitation" heeft ook nog geen conceptpagina, terwijl drie bronnen het begrip dragen (Allen & McDonald, Ransbotham, Wang et al. via jagged-frontier).

## Bronnenmatrix

| Bron | Gebruikte claim |
| ---- | --------------- |
| `wiki/concepts/systems-thinking.md` | Wicked problems: steeds veranderend, moeilijk te definiëren, veel belanghebbenden; systeemdenken past, doorbraak- en design thinking niet; Rittel & Webber alleen als impliciete verwijzing |
| `wiki/sources/2026-04-28-bansal-birkinshaw-systems-thinking.md` | Wicked problems hebben geen enkelvoudige definitie; herformuleer steeds; "nudge your way forward", een "ecology of actions"; praktijkkader, geen data |
| `wiki/concepts/strategy.md` | Vijf kenmerken van strategische beslissingen (Allen & McDonald); exploitation bias als "innovator's dilemma restated as a property of a reasoner" |
| `wiki/sources/2026-03-11-allen-mcdonald-how-well-can-ai-do-strategy-simulation-benchmark.md` | 34 modellen, 249 MBA-studenten, 8 jaar; frontiermodellen van midden/eind 2025 onder modellen van begin 2025 en onder studenten; systematic exploitation bias; citaat Gemini 2.5 Pro; geen figuurwaarden |
| `raw/papers/how-well-can-ai-do-strategy-empirical-benchmarking-using-strategy-simulations.md` | Simulatie bedoeld voor "balancing exploration and exploitation over time (March 1991 …)"; literatuurlijst: March, Organ. Sci. 2:71–87 |
| `wiki/concepts/jagged-frontier.md` | De kartel bijt bij "forward-looking commitment under delayed feedback"; sluit niet met nieuwere modellen; verkenfase tegenover verfijnfase (Wang et al.) |
| `wiki/concepts/dynamic-capabilities.md` | Allen & McDonald meet de cel *balancing-digital-portfolios*; mens nodig bij het vastleggen op een optie waarvan de opbrengst nog niet zichtbaar is |
| `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` | "Learn to explore with AI (not just exploit)"; 2× en 1,6× vaker verkennen; 1,9× langlopende en 2,4× risicovolle projecten |
| `wiki/sources/2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers.md` | Definitie two-way/one-way door (Jassy); two-way-door-besluiten bij de mensen die het werk doen |
| `wiki/sources/2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm.md` | Weglekken van stille kennis als one-way door |
| `wiki/sources/2026-09-30-demaree-onebrief-ai-military-planning.md` | Simulatie als terugkoppeling voor besluiten met late feedback |
| Extern: Rittel & Webber 1973 (scan origineel, Crossref) | Tien kenmerken, verbatim kopjes |
| Extern: March 1991 (Crossref, OpenAlex) | Abstract: adaptieve processen verbeteren benutten sneller dan verkennen; korte termijn effectief, lange termijn zelfvernietigend |
| Extern: Osterwalder et al. 2020 (Wiley, Strategyzer) | Titel, ISBN, auteursvolgorde volgens titelpagina, assen; actiewerkwoorden niet bevestigd |
| Extern: Shahriari et al. 2016 (Crossref, auteursversie) | Acquisitiefuncties wegen verkennen en benutten af; A/B-test als bandiet |
| Extern: Myers 1977 (Crossref, werkpaper 1976, Wikipedia) | Waarde van de onderneming bevat opties op toekomstige investeringen; term "real options" volgens secundaire bronnen |
| Extern: McGrath 1999 (Crossref, OpenAlex) | Reële opties als kader voor mislukking; investeer pas als de omstandigheden gunstig zijn |
| Extern: Bezos, brief over 2015 (SEC EDGAR) | One-way/two-way doors, Type 1/Type 2, verbatim |
| Extern: Sutton & Barto 2018 (auteurssite) | Hoofdstuk 2 "Multi-armed Bandits" |
