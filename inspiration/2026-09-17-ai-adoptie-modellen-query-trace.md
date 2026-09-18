---
type: query-trace
question: "geef me een overzicht van AI adoptie modellen"
date: 2026-09-17
language: nl
trace: "2026-09-17-ai-adoptie-modellen-query-trace.json"
pages_used: 8
pages_ignored: 48
---

# Query trace — AI-adoptiemodellen

## 1. Question

- **Original:** geef me een overzicht van AI adoptie modellen
- **Restated:** Welke modellen en raamwerken voor AI-adoptie bevat de wiki, wat meten ze, en hoe sterk is de onderbouwing?
- **Facets:** 1) Welke benoemde adoptiemodellen/raamwerken draagt de wiki? 2) Wat meten ze — individuele acceptatie, organisatorische readiness, volwassenheid of implementatiediepte? 3) Welk empirisch bewijs ligt eronder, en waar lopen de cijfers uiteen? 4) Hoe verhouden ze zich tot de dynamic-capabilities ruggengraat (Teece / Warner & Wäger)?

## 2. Paths explored

Retrieval: `node scripts/wiki-retrieve.mjs --json -n 12` — RRF-fusie van qmd (relevantie) en `wiki/.graph.json` (structuur), daarna herordend op `effective_confidence`. Graph beschikbaar; geen `graph_warning`. **10 qmd-hits, 56 kandidaten totaal.**

**qmd hits** (relevantiestroom)

| # | Page | type | qmd | fused | verdict |
|---|------|------|-----|-------|---------|
| 1 | `wiki/sources/2026-04-28-ai-index-report-2025.md` | source | 0.62 | 0.94 | USE (W4) |
| 2 | `wiki/concepts/enterprise-ai-adoption.md` | concept | 0.61 | 0.964 | USE (W2) |
| 3 | `wiki/entities/AI Index.md` | entity | 0.57 | 0.823 | IGNORE |
| 4 | `wiki/sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage.md` | source | 0.57 | 0.896 | IGNORE |
| 5 | `wiki/sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company.md` | source | 0.56 | 0.882 | IGNORE |
| 6 | `wiki/sources/2025-06-15-cimino-ai-adoption-sustainable-growth-smes.md` | source | 0.48 | 0.869 | USE (W6) |
| 7 | `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | synthesis | 0.46 | 0.833 | USE (W1) |
| 8 | `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` | source | 0.44 | 0.843 | IGNORE |
| 9 | `wiki/threads/ai-maturity-measurement-comparison.md` | thread | 0.42 | 0.743 | USE (W3) |
| 10 | `wiki/sources/2026-04-28-mittri-cisco-ai-enabled-enterprise.md` | source | 0.41 | 0.819 | USE (W5) |

**graph neighbours** (`--hops 1`, typed-edge stroom — 46 pagina's)

| Page | reached via | fused | effConf | verdict |
|------|-------------|-------|---------|---------|
| `wiki/concepts/automation-vs-augmentation.md` | concepts/enterprise-ai-adoption --supports--> | 0.473 | 0.94 | IGNORE |
| `wiki/concepts/dynamic-capabilities.md` | concepts/enterprise-ai-adoption --supports--> | 0.46 | 0.95 | USE (W8) |
| `wiki/concepts/ai-sovereignty.md` | concepts/enterprise-ai-adoption --supports--> | 0.459 | 0.83 | IGNORE |
| `wiki/concepts/ai-employment-effects.md` | concepts/enterprise-ai-adoption --caused--> | 0.451 | 0.94 | IGNORE |
| `wiki/concepts/ai-knowledge-hiding.md` | concepts/enterprise-ai-adoption --instance-of--> | 0.447 | 0.73 | IGNORE |
| `wiki/concepts/jagged-frontier.md` | concepts/enterprise-ai-adoption --uses--> | 0.442 | 0.93 | IGNORE |
| `wiki/concepts/micro-productivity-trap.md` | concepts/enterprise-ai-adoption --caused--> | 0.438 | 0.94 | IGNORE |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | concepts/enterprise-ai-adoption --supports--> | 0.416 | — | IGNORE |
| `wiki/concepts/generative-ai.md` | concepts/enterprise-ai-adoption --caused--> | 0.416 | 0.92 | IGNORE |
| `wiki/concepts/founder-led-sales.md` | concepts/enterprise-ai-adoption --supports--> | 0.406 | 0.83 | IGNORE |
| `wiki/concepts/responsible-ai.md` | concepts/enterprise-ai-adoption --part-of--> | 0.406 | 0.93 | IGNORE |
| `wiki/concepts/open-source-ai.md` | concepts/enterprise-ai-adoption --supports--> | 0.405 | 0.89 | IGNORE |
| `wiki/concepts/strategic-foresight.md` | concepts/enterprise-ai-adoption --supports--> | 0.379 | 0.80 | IGNORE |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | concepts/enterprise-ai-adoption --supports--> | 0.377 | — | IGNORE |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | concepts/enterprise-ai-adoption --supports--> | 0.372 | — | IGNORE |
| `wiki/sources/2026-05-06-mit-ocw-future-of-mit-open-education.md` | concepts/enterprise-ai-adoption --supports--> | 0.368 | — | IGNORE |
| `wiki/concepts/systems-thinking.md` | concepts/enterprise-ai-adoption --supports--> | 0.366 | 0.75 | IGNORE |
| `wiki/sources/2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china.md` | concepts/enterprise-ai-adoption --supports--> | 0.363 | — | IGNORE |
| `wiki/sources/2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas.md` | concepts/enterprise-ai-adoption --supports--> | 0.358 | — | IGNORE |
| `wiki/sources/2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells.md` | concepts/enterprise-ai-adoption --supports--> | 0.35 | — | IGNORE |
| `wiki/concepts/document-intelligence.md` | concepts/enterprise-ai-adoption --part-of--> | 0.344 | 0.30 | IGNORE |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --supports--> | 0.337 | — | IGNORE |
| `wiki/sources/2026-05-03-rewired-second-edition-sample.md` | sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --supports--> | 0.333 | — | IGNORE |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | concepts/enterprise-ai-adoption --supports--> | 0.331 | 0.70 | IGNORE |
| `wiki/sources/2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services.md` | sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --supports--> | 0.326 | — | IGNORE |
| `wiki/sources/2026-08-10-banholzer-laberge-mckinsey-how-to-maximize-competitive-advantage.md` | sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --supports--> | 0.322 | — | IGNORE |
| `wiki/entities/McKinsey-&-Company.md` | sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --authored-by--> | 0.32 | — | IGNORE |
| `wiki/syntheses/ai-worker-maturity-levels.md` | concepts/enterprise-ai-adoption --supports--> | 0.318 | 0.66 | USE (W7) |
| `wiki/sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening.md` | sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company --supports--> | 0.312 | — | IGNORE |
| `wiki/sources/2026-07-10-when-ai-becomes-common-organizational-capability-becomes-the-advantage-ep-16.md` | sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --supports--> | 0.309 | 0.70 | IGNORE |
| `wiki/entities/BBC.md` | sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company --published-by--> | 0.308 | 0.77 | IGNORE |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company --supports--> | 0.308 | 0.80 | IGNORE |
| `wiki/sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai.md` | sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company --supports--> | 0.308 | — | IGNORE |
| `wiki/sources/2026-07-20-bbc-researchers-studied-ai-layoffs-heres-their-warning.md` | sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company --supports--> | 0.305 | — | IGNORE |
| `wiki/sources/2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity.md` | sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company --supports--> | 0.302 | — | IGNORE |
| `wiki/sources/2026-08-10-miller-worklab-the-ai-shift-most-companies-didnt-see-coming.md` | sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company --supports--> | 0.299 | — | IGNORE |
| `wiki/sources/2026-08-18-covello-gs-new-models-ai-investment-landscape.md` | sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company --supports--> | 0.296 | — | IGNORE |
| `wiki/sources/2026-04-28-anand-wu-genai-playbook.md` | sources/2025-06-15-cimino-ai-adoption-sustainable-growth-smes --supports--> | 0.293 | — | IGNORE |
| `wiki/sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation.md` | sources/2025-06-15-cimino-ai-adoption-sustainable-growth-smes --supports--> | 0.29 | — | IGNORE |
| `wiki/sources/2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset.md` | sources/2025-06-15-cimino-ai-adoption-sustainable-growth-smes --contradicts--> | 0.287 | — | IGNORE |
| `wiki/sources/2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care.md` | sources/2026-05-07-ransbotham-augmented-learners --supports--> | 0.27 | — | IGNORE |
| `wiki/syntheses/harness-thinning-what-persists.md` | syntheses/organizational-frameworks-for-ai-adoption --supports--> | 0.268 | 0.72 | IGNORE |
| `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | sources/2026-05-07-ransbotham-augmented-learners --supports--> | 0.267 | 0.80 | IGNORE |
| `wiki/entities/David-Kiron.md` | sources/2026-05-07-ransbotham-augmented-learners --authored-by--> | 0.263 | — | IGNORE |
| `wiki/entities/MIT-Sloan-Management-Review.md` | sources/2026-05-07-ransbotham-augmented-learners --published-by--> | 0.261 | — | IGNORE |
| `wiki/entities/Sam-Ransbotham.md` | sources/2026-05-07-ransbotham-augmented-learners --authored-by--> | 0.258 | — | IGNORE |

**gap-expansion** (Step 5)

| Method | Why | Result |
|---|---|---|
| corpus-grep over `wiki/**` | Facet 1 vroeg naar benoemde adoptiemodellen; de klassieke IS-canon ontbrak opvallend in de ledger. | `Technology Acceptance Model` 0, `UTAUT` 0, `diffusion of innovation` 0, `TOE` 0 echte treffers. Geen pagina toegevoegd — het hiaat zelf is in het antwoord vastgelegd. |

## 3. Ignore policy applied

Vijf reason-classes vuurden deze run:

- `off-facet` (13) — semantisch naburig, maar beantwoordt geen van de vier facetten.
- `redundant` (8) — het raamwerk staat al als laag in de synthese (W1) of integraal samengevat op het conceptpagina (W2).
- `wrong-granularity` (6) — entiteitkaarten bereikt via `authored-by`/`published-by`; de facetten vragen claims en cijfers, geen identiteit.
- `below-threshold` (20) — de lange staart van graph-only bronnen zonder facet die ze nodig heeft.
- `decayed` (1) — `effective_confidence` onder 0,5 én niet uniek voor enig facet.

Twee oordelen verdienen toelichting, omdat ze tegen het ruwe `fused_score`-signaal ingaan:

- **Twee graph-only pagina's zijn gepromoveerd tot USE** ondanks lage fusie-score: `concepts/dynamic-capabilities` (0,46) draagt facet 4 volledig, en `syntheses/ai-worker-maturity-levels` (0,318) is het enige model op medewerkersniveau in het corpus — zonder die pagina mist het antwoord een hele analyse-eenheid.
- **Een `contradicts`-edge is toch genegeerd.** `2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset` contradiceert W6 over de vraag of mindset de werkzame hefboom is. Het ignore-beleid merkt `contradicts` aan als sterk USE-signaal; hier is het toch `redundant`, omdat de Cimino-bronpagina de tegenstelling woordelijk draagt, inclusief de nuance dat de constructen aangrenzend zijn in plaats van identiek. De tegenstelling haalt het antwoord dus wél, via W6.

## 4. Information ignored

| Page | reason-class | reden |
|------|--------------|-------|
| `wiki/sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage.md` | `off-facet` | betoogt herontwerp boven productiviteit; levert geen adoptiemodel of meetinstrument |
| `wiki/sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company.md` | `redundant` | het zes-vector-instrument van Grant staat integraal samengevat op concepts/enterprise-ai-adoption (W2) |
| `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` | `redundant` | de Augmented Learners 2x2 is als laag "organizational learning" opgenomen in de synthese (W1) |
| `wiki/entities/AI Index.md` | `wrong-granularity` | catalogus-kaart van de uitgever; de facet vraagt om cijfers, die staan op de bron (W4) |
| `wiki/concepts/automation-vs-augmentation.md` | `off-facet` | inzetkeuze per taak, geen adoptie- of volwassenheidsmodel |
| `wiki/concepts/ai-sovereignty.md` | `off-facet` | geopolitiek/infrastructuur, buiten alle vier de facetten |
| `wiki/concepts/ai-employment-effects.md` | `off-facet` | arbeidsmarkteffecten, niet de adoptie van AI binnen de organisatie |
| `wiki/concepts/ai-knowledge-hiding.md` | `off-facet` | gedragsfenomeen rond AI-gebruik, geen adoptiemodel |
| `wiki/concepts/jagged-frontier.md` | `off-facet` | capaciteitsgrens van modellen, geen organisatiemodel |
| `wiki/concepts/micro-productivity-trap.md` | `redundant` | de trap wordt in W1 benoemd als de vraag die het Bain/OpenAI-model beantwoordt |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | `below-threshold` | alleen via graph bereikt (fused 0.416); geen facet die deze pagina nodig heeft |
| `wiki/concepts/generative-ai.md` | `off-facet` | technologiecategorie, geen adoptiemodel |
| `wiki/concepts/founder-led-sales.md` | `off-facet` | go-to-market-praktijk, buiten de vraag |
| `wiki/concepts/responsible-ai.md` | `off-facet` | governance-domein; raakt hooguit een pijler binnen W5 |
| `wiki/concepts/open-source-ai.md` | `off-facet` | leveringsmodel van modellen, geen organisatorisch adoptiemodel |
| `wiki/concepts/strategic-foresight.md` | `off-facet` | scenariodenken; raakt sensing maar levert geen adoptiemodel |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | `below-threshold` | alleen via graph bereikt (fused 0.377); geen facet die deze pagina nodig heeft |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | `below-threshold` | alleen via graph bereikt (fused 0.372); geen facet die deze pagina nodig heeft |
| `wiki/sources/2026-05-06-mit-ocw-future-of-mit-open-education.md` | `below-threshold` | alleen via graph bereikt (fused 0.368); geen facet die deze pagina nodig heeft |
| `wiki/concepts/systems-thinking.md` | `off-facet` | denkdiscipline, geen adoptie-instrument |
| `wiki/sources/2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china.md` | `below-threshold` | alleen via graph bereikt (fused 0.363); geen facet die deze pagina nodig heeft |
| `wiki/sources/2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas.md` | `below-threshold` | alleen via graph bereikt (fused 0.358); geen facet die deze pagina nodig heeft |
| `wiki/sources/2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells.md` | `below-threshold` | alleen via graph bereikt (fused 0.35); geen facet die deze pagina nodig heeft |
| `wiki/concepts/document-intelligence.md` | `decayed` | effective_confidence 0.303 en geen facet die deze pagina uniek dekt |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | `below-threshold` | alleen via graph bereikt (fused 0.337); geen facet die deze pagina nodig heeft |
| `wiki/sources/2026-05-03-rewired-second-edition-sample.md` | `redundant` | McKinsey Rewired 6 capabilities is een laag in de synthese (W1) |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | `below-threshold` | alleen via graph bereikt (fused 0.331); geen facet die deze pagina nodig heeft |
| `wiki/sources/2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services.md` | `below-threshold` | alleen via graph bereikt (fused 0.326); geen facet die deze pagina nodig heeft |
| `wiki/sources/2026-08-10-banholzer-laberge-mckinsey-how-to-maximize-competitive-advantage.md` | `below-threshold` | alleen via graph bereikt (fused 0.322); geen facet die deze pagina nodig heeft |
| `wiki/entities/McKinsey-&-Company.md` | `wrong-granularity` | entiteitkaart bereikt via authored-by/published-by; facet vraagt claims, niet identiteit |
| `wiki/sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening.md` | `below-threshold` | alleen via graph bereikt (fused 0.312); geen facet die deze pagina nodig heeft |
| `wiki/sources/2026-07-10-when-ai-becomes-common-organizational-capability-becomes-the-advantage-ep-16.md` | `redundant` | stelling staat met coefficienten op W6 |
| `wiki/entities/BBC.md` | `wrong-granularity` | entiteitkaart bereikt via authored-by/published-by; facet vraagt claims, niet identiteit |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | `below-threshold` | alleen via graph bereikt (fused 0.308); geen facet die deze pagina nodig heeft |
| `wiki/sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai.md` | `below-threshold` | alleen via graph bereikt (fused 0.308); geen facet die deze pagina nodig heeft |
| `wiki/sources/2026-07-20-bbc-researchers-studied-ai-layoffs-heres-their-warning.md` | `below-threshold` | alleen via graph bereikt (fused 0.305); geen facet die deze pagina nodig heeft |
| `wiki/sources/2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity.md` | `below-threshold` | alleen via graph bereikt (fused 0.302); geen facet die deze pagina nodig heeft |
| `wiki/sources/2026-08-10-miller-worklab-the-ai-shift-most-companies-didnt-see-coming.md` | `below-threshold` | alleen via graph bereikt (fused 0.299); geen facet die deze pagina nodig heeft |
| `wiki/sources/2026-08-18-covello-gs-new-models-ai-investment-landscape.md` | `below-threshold` | alleen via graph bereikt (fused 0.296); geen facet die deze pagina nodig heeft |
| `wiki/sources/2026-04-28-anand-wu-genai-playbook.md` | `redundant` | de 2x2 en de zes leakage points zijn twee lagen in de synthese (W1) |
| `wiki/sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation.md` | `redundant` | de negen microfundamenten staan volledig op concepts/dynamic-capabilities (W8) |
| `wiki/sources/2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset.md` | `redundant` | contradicts-edge op W6; die tegenstelling wordt woordelijk gedragen door de Cimino-bronpagina zelf |
| `wiki/sources/2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care.md` | `below-threshold` | alleen via graph bereikt (fused 0.27); geen facet die deze pagina nodig heeft |
| `wiki/syntheses/harness-thinning-what-persists.md` | `off-facet` | runtime-engineering lens; de harness-laag zelf is al vertegenwoordigd in W1 |
| `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | `below-threshold` | alleen via graph bereikt (fused 0.267); geen facet die deze pagina nodig heeft |
| `wiki/entities/David-Kiron.md` | `wrong-granularity` | entiteitkaart bereikt via authored-by/published-by; facet vraagt claims, niet identiteit |
| `wiki/entities/MIT-Sloan-Management-Review.md` | `wrong-granularity` | entiteitkaart bereikt via authored-by/published-by; facet vraagt claims, niet identiteit |
| `wiki/entities/Sam-Ransbotham.md` | `wrong-granularity` | entiteitkaart bereikt via authored-by/published-by; facet vraagt claims, niet identiteit |

## 5. Information used

| Anchor | Page | type | effConf | bijdrage |
|--------|------|------|---------|----------|
| W1 | `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | synthesis | 0.79 | de 10-framework gelaagde stack, de beslisboom, de echte meningsverschillen en de empirische-validatietabel |
| W2 | `wiki/concepts/enterprise-ai-adoption.md` | concept | 0.95 | spine-concept; BBC zes-vector-instrument, en de sectie "Readiness is not adoption" |
| W3 | `wiki/threads/ai-maturity-measurement-comparison.md` | thread | — | de instrument-cross-walk: welk model meet wat, met sample en definitie naast elkaar |
| W4 | `wiki/sources/2026-04-28-ai-index-report-2025.md` | source | — | adoptiebreedte-basislijn 78% / 71% / 1% mature, McKinsey-instrument n=2854 |
| W5 | `wiki/sources/2026-04-28-mittri-cisco-ai-enabled-enterprise.md` | source | — | Cisco 5 Foundations readiness-model + 13%/98%/85%-triade |
| W6 | `wiki/sources/2025-06-15-cimino-ai-adoption-sustainable-growth-smes.md` | source | — | het enige structurele model met padcoefficienten: AIAR/AIAI-split, PLS-SEM, n=210 |
| W7 | `wiki/syntheses/ai-worker-maturity-levels.md` | synthesis | 0.66 | het werknemer-niveau model L0-L5 over zes dimensies; graph-promoted |
| W8 | `wiki/concepts/dynamic-capabilities.md` | concept | 0.95 | Teece sense/seize/transform + de negen W&W digitale microfundamenten |

## 6. Answer-element map

| Anchor | Answer element (claim) | Wiki page | Section / span |
|--------|------------------------|-----------|----------------|
| [W1] | Tien raamwerken zijn complementair, niet concurrerend; elk benoemt een beslislaag. Plus de beslisboom, de echte meningsverschillen en de empirische-validatietabel. | [[syntheses/organizational-frameworks-for-ai-adoption]] | ## Findings → De frameworks operate on different layers / A decision tree / Where they genuinely disagree / Where empirical validation sits |
| [W2] | De readiness-implementatiekloof als concept-niveau claim; het zes-vector instrument; waarom AIAR/AIAI niet is gepromoveerd tot eigen pagina. | [[concepts/enterprise-ai-adoption]] | ## Readiness is not adoption (added 2026-09-17); ## Return on intelligence: a six-vector maturity instrument |
| [W3] | De instrumenten meten verschillende dingen onder dezelfde woorden; 1/7/12/13% cross-walk; de waarschuwing om altijd het instrument te noemen. | [[threads/ai-maturity-measurement-comparison]] | ## What we know so far → Apparent divergence; Updated cross-walk; A different unit of analysis |
| [W4] | Adoptiebreedte-basislijn: 78% gebruikt AI, 71% GenAI, 1% noemt de uitrol mature; McKinsey-instrument n=2.854. | [[sources/2026-04-28-ai-index-report-2025]] | ## Key claims → Enterprise adoption (the headline story) |
| [W5] | Cisco 5 Foundations als readiness-model; 13% ready / 98% urgentie / 85% <18 maanden; sponsored research-voorbehoud. | [[sources/2026-04-28-mittri-cisco-ai-enabled-enterprise]] | ## Key claims → Urgency and readiness gap; ## The "Foundations" framework; ## My take |
| [W6] | De AIAR/AIAI-splitsing met padcoëfficiënten; readiness bereikt economische prestatie niet; HTMT 0,878 en steekproefvoorbehoud; steun geldt de drie-clusterruggengraat niet de negen microfundamenten. | [[sources/2025-06-15-cimino-ai-adoption-sustainable-growth-smes]] | ## TL;DR; ## Key claims → Results (Table 7); ## Scope and reliability |
| [W7] | Medewerkersladder L0–L5 over zes dimensies; evaluatie is de bindende beperking; METR-perceptiekloof van ~39 punten; oordeelsbegrensde top. | [[syntheses/ai-worker-maturity-levels]] | ## Findings → The synthesized model: six levels; The six assessable dimensions; cross-cutting findings 1–3 |
| [W8] | Teece sense/seize/transform en de negen digitale microfundamenten van Warner & Wäger. | [[concepts/dynamic-capabilities]] | ## Working definition; ## Key claims → The three-cluster framework; Microfoundations for digital transformation |

## 7. Final answer

De wiki bevat **geen klassieke academische adoptietheorie** — geen Technology Acceptance Model, geen UTAUT, geen Rogers' diffusie-van-innovaties, geen TOE-raamwerk. Een gerichte controle over het hele corpus geeft nul treffers op alle vier. Wat de wiki wél heeft is een dicht bestand aan **praktijk- en consultancyraamwerken voor AI-adoptie in organisaties**, plus één peer-reviewed structureel model. Dat is een ander soort antwoord dan een literatuuroverzicht van adoptietheorie, en het is goed om dat onderscheid vooraf scherp te hebben.

## 1. De kern: tien raamwerken die op verschillende lagen werken

Het centrale document is de synthese [[syntheses/organizational-frameworks-for-ai-adoption|organizational-frameworks-for-ai-adoption]] [W1]. De hoofdstelling daarvan is dat de tien raamwerken **grotendeels complementair zijn, niet concurrerend** — elk benoemt een andere beslislaag, van organisatieontwerp tot runtime-engineering [W1]:

| Laag | Model | Vraag die het beantwoordt |
|---|---|---|
| Org-ontwerp | Tin Man / Octopus (Werner-Le Brun) | Is de organisatie structureel in staat te veranderen? |
| Readiness | Cisco 5 Foundations — Strategy / Infrastructure / Data / Governance / Culture | Zijn de randvoorwaarden er? |
| Capaciteitsprogressie | MIT CISR Four Stages + "Four S" | In welke fase zit je, en wat blokkeert de volgende? |
| Organisatieleren | Ransbotham/Kiron Augmented Learners 2×2 | Zet de organisatie AI-interacties om in samengestelde kennis? |
| Transformatie-playbook | McKinsey *Rewired* 6 capabilities | Hoe voer je het traject uit? |
| Firmagrens | Nishar-Nohria — Build / Compose / Collaborate / Buy Outcomes | Welke workflows houd je in huis? |
| Val-ontsnapping | Bain/OpenAI 4-staps | Hoe vermijd je de productiviteitsval? |
| Taakinzet | Anand-Wu 2×2 (foutkosten × kennistype) | Op welke taak richt je AI eerst? |
| Inzetvolwassenheid | Beutler Ask → Assist → Automate | Hoeveel autonomie geef je de agent? |
| Runtime | Agent harness — Context / Constraints / Contracts / Compounding | Welke infrastructuur moet tussen model en gebruiker staan? |
| ⊥ Dwarsdoorsnijdend | Carucci *resistance-as-data* | Wat zegt de weerstand over de verandering zelf? |

Die laatste is expliciet géén laag maar een **diagnostische houding** die je inzet zodra een van de andere negen lagen weerstand oproept [W1]. De synthese levert er ook een beslisboom bij: welk raamwerk je pakt, hangt af van de vraag die de bestuurder stelt, niet van het merk van het raamwerk [W1].

## 2. Waar ze het echt oneens zijn

Dit is het waardevolste deel, omdat de meeste schijnbare tegenstellingen alleen vocabulaireverschillen zijn [W1]. De echte breuklijnen:

- **Pilots als fase of als val.** MIT CISR maakt van piloteren Stage 2, een noodzakelijke doorgangsfase. Bain/OpenAI stelt dat bedrijven juist *vastlopen* in pilots. Dezelfde observatie, tegengestelde waardering [W1].
- **Incrementeel of herontwerp.** McKinsey *Rewired* en Bain/OpenAI drukken op procesherontwerp eerst, technologie tweede. MIT CISR staat geleidelijke progressie toe [W1].
- **Organisatieontwerp als voorwaarde of als uitkomst.** Werner-Le Brun stelt dat een "Tin Man"-organisatie de lagere raamwerken niet vasthoudt; de andere modellen veronderstellen simpelweg dat de organisatie kan handelen [W1].
- **Procesherontwerp of de harness als bron van waarde.** Bain/OpenAI zegt het eerste, Chatterjee het tweede. De synthese lost dit op als laagverschil: beide zijn waar op hun eigen niveau, en beide compounding-cycli moeten draaien [W1].

## 3. Wat de modellen meten — en waarom de cijfers uiteenlopen

De thread [[threads/ai-maturity-measurement-comparison|ai-maturity-measurement-comparison]] [W3] legt de meetinstrumenten naast elkaar, en dat is nodig, want ze meten **verschillende dingen onder dezelfde woorden**:

| Bron | Wat het meet | "Succes" | Instrument |
|---|---|---|---|
| AI Index 2025 (McKinsey) | GenAI-volwassenheid, zelfrapportage C-suite | **1%** mature | n=2.854, 2024 [W4] |
| MIT CISR | Stage 4, getrianguleerde effectiviteitsscore | **7%** Stage 4 | n=721, **2022** — pre-GenAI [W3] |
| Cisco | "Klaar om AI volledig te benutten" | **13%** ready | eigen instrument, methodologie dun [W5] |
| Werner-Le Brun | Transformaties met duurzame prestatiewinst | **12%** | geaggregeerd, niet AI-specifiek [W3] |
| Ransbotham/Kiron | Augmented Learners-kwadrant | **15%** | n=3.467, 136 landen [W1] |

Vijf onafhankelijke instrumenten, vijf getallen tussen 1% en 15% [W1][W3]. De wiki leest dat niet als meetruis maar als signaal: **wat je succes ook noemt, het is zeldzaam** [W3]. Tegelijk is de waarschuwing expliciet — noem altijd het instrument erbij, want "78% van de organisaties gebruikt AI" zonder "volgens McKinsey's ten-minste-één-functie-definitie" verliest betekenis [W3][W4].

Let op de aparte categorie die Cisco toevoegt: **readiness en urgentie** zijn een derde meettype, naast adoptiebreedte en volwassenheidsfase [W5][W3]. Cisco's triade is 13% klaar / 98% voelt urgentie / 85% geeft zichzelf minder dan 18 maanden [W5]. Dat is sponsored research van een infrastructuurleverancier — de wiki markeert dat expliciet als reden om de infrastructuur- en securitysecties te disconteren [W5].

## 4. Het enige model met coëfficiënten

Eén bron in het corpus is een echt **structureel model**, niet een raamwerk: [[2025-06-15-cimino-ai-adoption-sustainable-growth-smes|Cimino et al. (2025)]] [W6], PLS-SEM op 210 Italiaanse innovatieve startups. De bijdrage is een splitsing van adoptie in twee mediatoren [W6]:

- **AIAR — AI Acceptance Rate**: de bereidheid en openheid van de firma om te adopteren.
- **AIAI — AI Adoption Intensity**: hoe diep AI daadwerkelijk in processen is ingebed.

Het resultaat is een gekwantificeerde readiness-implementatiekloof [W6][W2]:

| | → technologisch | → economisch | → collaboratief | → duurzaam |
|---|---|---|---|---|
| **AIAI** (implementatie) | **0,390** | **0,498** | **0,268** | −0,079 *n.s.* |
| **AIAR** (bereidheid) | **0,192** | 0,094 *n.s.* | −0,108 *n.s.* | **0,213** |

Bereidheid raakt economische prestatie helemaal niet; het collaboratieve pad is zelfs negatief getekend [W6]. En dynamische capaciteiten produceren bereidheid bijna twee keer zo makkelijk als implementatie (β = 0,523 tegen 0,279) — dus de capaciteit die iedereen probeert op te bouwen levert eerst en vooral *willen* op, precies de toestand die niet betaalt [W6][W2]. De conclusie van de auteurs zelf: *"Simply fostering enthusiasm for AI is insufficient if not supported by resource allocation and strategic alignment."* [W6]

**Reserves die de wiki er expliciet bij houdt:** de twee constructen correleren op HTMT 0,878 (marginale discriminante validiteit, en de hele bijdrage rust erop), 81% van de steekproef heeft minder dan elf medewerkers, en de auteurs waarschuwen zelf dat innovatieve startups een aparte deelverzameling van het MKB zijn [W6]. De wiki heeft dit daarom bewust *niet* tot eigen conceptpagina gepromoveerd — pas bij een tweede bevestigende bron [W2].

## 5. Een tweede analyse-eenheid: de individuele medewerker

Alle bovenstaande instrumenten meten de **firma**. De synthese [[syntheses/ai-worker-maturity-levels|ai-worker-maturity-levels]] [W7] voegt een medewerkersladder toe, gefuseerd uit zeven gepubliceerde deelladders plus één volledig gedocumenteerd traject: **L0 Bystander → L1 Conversationalist → L2 Operator → L3 Delegator → L4 Orchestrator → L5 Multiplier**, gescoord over zes dimensies (tooling, delegatie, verificatie, contextontwerp, reikwijdte, leren) [W7].

Drie bevindingen daaruit disciplineren elk adoptiemodel [W7]:

1. **Evaluatie, niet generatie, is de bindende beperking** boven novice-niveau. Een model dat op gebruiksintensiteit alleen scoort, zet de zelfverzekerde niet-verifieerder boven de zorgvuldige beoordelaar — precies verkeerd om [W7].
2. **Zelfrapportage is een vertekend instrument.** METR's RCT vond ontwikkelaars die meetbaar 19% *trager* waren met AI en geloofden dat ze 20% *sneller* waren — een kloof van ~39 punten [W7]. Dat raakt direct de zelfgerapporteerde volwassenheidscijfers uit §3.
3. **De top is oordeelsbegrensd, niet doorvoerbegrensd** [W7].

Waarom dit ertoe doet voor de firma-instrumenten: als volwassenheid eerst bij *individuen* aanslaat en pas later bij firma's, dan onderschatten firma-instrumenten systematisch vroege volwassenheid en overschatten ze inkoop [W3].

## 6. De verbinding met dynamische capaciteiten

Onder de praktijkraamwerken ligt de theoretische ruggengraat van deze wiki: [[concepts/dynamic-capabilities|dynamic-capabilities]] [W8] — Teece's **sensing / seizing / transforming**, met Warner & Wäger's negen digitale microfundamenten erop gelegd (digital scouting, scenario planning, mindset crafting; rapid prototyping, balancing digital portfolios, strategic agility; navigating innovation ecosystems, redesigning internal structures, improving digital maturity) [W8].

Cimino is de eerste kwantitatieve toets van die ruggengraat in het corpus [W6]. Belangrijke nuance die de wiki zelf markeert: het gebruikte instrument (Kump & Kessler 2019) meet sensing/seizing/transforming in hun **generieke** vorm, niets erin is digitaal-specifiek. De steun geldt dus de **drie-clusterruggengraat**, niet de negen digitale microfundamenten erbovenop [W6].

## Wat de wiki niet dekt

Eerlijk over de randen:

- **Geen individuele-acceptatietheorie.** TAM, UTAUT, Rogers, TOE komen nergens voor. Alle modellen hier zijn organisatie- of medewerkersniveau, geen psychologische acceptatiemodellen.
- **De empirische basis helt naar prescriptief.** Van de tien raamwerken hebben er twee een representatieve steekproef van betekenis; de rest rust op casuïstiek, vendor-instrumenten of praktijkessays — Carucci heeft helemaal geen empirisch anker [W1].
- **Vendorbias is structureel.** McKinsey *Rewired* en Bain/OpenAI zijn vendor-of-deployment data met selectie-effect; Cisco en Werner-Le Brun zijn respectievelijk sponsored en AWS-geaffilieerd [W1][W5].
- **MIT CISR's verdeling is pre-GenAI** (2022) en daarmee het meest geciteerde volwassenheidsmodel op de oudste data [W3].

## 8. Trace artifact

Machine-readable provenance: [`2026-09-17-ai-adoptie-modellen-query-trace.json`](2026-09-17-ai-adoptie-modellen-query-trace.json)
