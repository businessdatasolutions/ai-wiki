---
type: query-trace
question: "Welke concurrenten en bedrijven verzamelen of verkopen data voor embodied AI, en hoe werken datamarktplaatsen en datalicenties?"
date: 2026-10-15
language: nl
trace: "2026-10-15-bedrijven-data-embodied-ai-datamarkten-query-trace.json"
pages_used: 8
pages_ignored: 40
---

# Query trace — Bedrijven, datamarkten en licenties voor embodied-AI-data

## 1. Question
- **Original:** Welke concurrenten en bedrijven verzamelen of verkopen data voor embodied AI, en hoe werken datamarktplaatsen en datalicenties?
- **Restated:** Welke bedrijven verzamelen of verkopen data voor embodied AI, en wat zegt de wiki over datamarktplaatsen, licentiemodellen en herkomst/consent?
- **Facets:** 1) bedrijven die data voor embodied AI verzamelen of verkopen 2) datamarktplaatsen en licentiemodellen 3) herkomst, consent en juridische risico's

## 2. Paths explored
Retrieval: `node scripts/wiki-retrieve.mjs --no-bump --json -n 12 "<question>"` (graph available: true; 10 qmd hits, 42 candidates). `--no-bump` because the caller forbade modifying wiki pages.

**qmd hits** (relevance stream)
| # | Page | type | qmd score | fused | verdict |
|---|------|------|-----------|-------|---------|
| 1 | `wiki/sources/2026-07-06-sevilla-emarketer-custom-ai-coded-apps-trim-saas-expenses.md` | source | 1.00 | 0.94 | IGNORE |
| 2 | `wiki/sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness.md` | source | 0.50 | 0.93 | IGNORE |
| 3 | `wiki/concepts/generative-ai.md` | concept | 0.33 | 0.86 | IGNORE |
| 4 | `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | synthesis | 0.25 | 0.83 | IGNORE |
| 5 | `wiki/entities/HubSpot.md` | entity | 0.20 | 0.86 | IGNORE |
| 6 | `wiki/sources/2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free.md` | source | 0.14 | 0.87 | USE |
| 7 | `wiki/sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening.md` | source | 0.13 | 0.86 | IGNORE |
| 8 | `wiki/entities/AI%20Index.md` | entity | 0.11 | 0.79 | IGNORE |
| 9 | `wiki/sources/2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs.md` | source | 0.09 | 0.83 | IGNORE |
| 10 | `wiki/sources/2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about.md` | source | 0.08 | 0.82 | IGNORE |

**graph neighbours** (`--hops 1`, typed-edge stream)
| Page | reached via | hops | fused | verdict |
|------|-------------|------|-------|---------|
| `wiki/sources/2026-07-07-sinofsky-amble-a16z-software-in-the-age-of-agents.md` | sources/2026-07-06-sevilla-emarketer-custom-ai-coded-apps-trim-saas-expenses --supports--> this | 1 | 0.47 | IGNORE |
| `wiki/sources/2026-09-08-gauch-bcg-so-what-will-ai-agents-replace-your-crm.md` | sources/2026-07-06-sevilla-emarketer-custom-ai-coded-apps-trim-saas-expenses --contradicts--> this | 1 | 0.46 | IGNORE |
| `wiki/sources/2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai.md` | sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness --supports--> this | 1 | 0.46 | IGNORE |
| `wiki/sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai.md` | sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness --supports--> this | 1 | 0.45 | USE |
| `wiki/sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity.md` | sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness --supports--> this | 1 | 0.44 | IGNORE |
| `wiki/sources/2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity.md` | sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness --supports--> this | 1 | 0.43 | IGNORE |
| `wiki/sources/2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai.md` | sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness --supports--> this | 1 | 0.43 | IGNORE |
| `wiki/sources/2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models.md` | sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness --supports--> this | 1 | 0.42 | IGNORE |
| `wiki/sources/2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over.md` | sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness --supports--> this | 1 | 0.42 | IGNORE |
| `wiki/sources/2026-09-18-bloomberg-originals-how-china-plans-to-win-global-ai-race.md` | sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness --supports--> this | 1 | 0.41 | IGNORE |
| `wiki/sources/2026-09-18-reuters-on-assignment-inside-chinas-ai-race.md` | sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness --supports--> this | 1 | 0.40 | IGNORE |
| `wiki/concepts/ai-agents.md` | concepts/generative-ai --instance-of--> this | 1 | 0.40 | IGNORE |
| `wiki/concepts/enterprise-ai-adoption.md` | concepts/generative-ai --caused--> this | 1 | 0.40 | IGNORE |
| `wiki/sources/2026-09-30-michael-miller-department-of-war-ai-adoption.md` | sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness --supports--> this | 1 | 0.40 | IGNORE |
| `wiki/sources/2026-10-04-chu-liu-dw-the-dip-how-china-is-viewing-the-ai-race.md` | sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness --supports--> this | 1 | 0.39 | IGNORE |
| `wiki/concepts/foundation-models.md` | concepts/generative-ai --uses--> this | 1 | 0.38 | IGNORE |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | concepts/generative-ai --supports--> this | 1 | 0.37 | IGNORE |
| `wiki/concepts/micro-productivity-trap.md` | syntheses/organizational-frameworks-for-ai-adoption --supports--> this | 1 | 0.37 | IGNORE |
| `wiki/concepts/jagged-frontier.md` | concepts/generative-ai --instance-of--> this | 1 | 0.36 | IGNORE |
| `wiki/sources/2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook.md` | entities/HubSpot --published-by--> this | 1 | 0.35 | IGNORE |
| `wiki/sources/2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook.md` | entities/HubSpot --published-by--> this | 1 | 0.34 | IGNORE |
| `wiki/sources/2026-08-12-tan-a16z-new-rules-for-founders.md` | sources/2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free --supports--> this | 1 | 0.34 | IGNORE |
| `wiki/sources/2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet.md` | sources/2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free --supports--> this | 1 | 0.34 | IGNORE |
| `wiki/concepts/software-3.0.md` | concepts/generative-ai --instance-of--> this | 1 | 0.33 | IGNORE |
| `wiki/sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai.md` | sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.33 | IGNORE |
| `wiki/sources/2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces.md` | sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.33 | IGNORE |
| `wiki/sources/2026-04-28-brynjolfsson-canaries-coal-mine.md` | sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.33 | IGNORE |
| `wiki/sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company.md` | sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-08-18-covello-gs-new-models-ai-investment-landscape.md` | sources/2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-05-21-jones-stanford-gsb-ai-and-our-economic-future.md` | sources/2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-10-07-richardson-reuters-econ-world-ai-at-work.md` | sources/2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs --supports--> this | 1 | 0.31 | IGNORE |
| `wiki/syntheses/harness-thinning-what-persists.md` | syntheses/organizational-frameworks-for-ai-adoption --supports--> this | 1 | 0.31 | IGNORE |

**index.md / gap-expansion** (Step 5: one round, rg keyword sweep over `wiki/` for robot/humanoid/embodied/physical AI/world model/synthetic data/licensing/etc.)
| Page | why added |
|------|-----------|
| `wiki/sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai.md` | graph-only candidate promoted: ~3M modellen, 1M datasets, helft Fortune 500; platform vangt 1-2% van de waarde; Evox-copyrightzaak; Reachy Mini |
| `wiki/sources/2026-06-25-the-ai-factory-the-rewiring-of-indias-tech-industry.md` | not in ledger; found by keyword sweep: Object Ways (annotatie naar robotica), NextWealth; egocentrische data; extractieve keten |
| `wiki/sources/2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet.md` | not in ledger; found by keyword sweep: 52% crawlerverzoeken voor training; >50 publisher-AI-deals sinds 2023; licenties bespoke, waardering onopgelost; marktplaats |
| `wiki/sources/2026-04-28-ai-index-report-2025.md` | not in ledger; found by keyword sweep: Figure AI $675M bij $2,6B; C4-restricties 5-7% naar 20-33% |
| `wiki/sources/2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2.md` | not in ledger; found by keyword sweep: Large Action Model (xLAM) getraind op synthetische multi-turn-trajecten; gewichten en trainingsdata open |
| `wiki/concepts/responsible-ai.md` | not in ledger; found by keyword sweep: consent/surveillance van data-werkers; data commons krimpt |
| `wiki/sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing.md` | not in ledger; found by keyword sweep: synthetische-dataleverancier; geen teststandaard dus vertrouwde leverancier wint; contracten via insiders |

## 3. Ignore policy applied
- `off-facet` — semantically adjacent but answers none of the facets.
- `wrong-granularity` — entity card where the facet needs figures; the underlying sources were used.
- `below-threshold` — low fused score and no facet needs the page (graph-only long tail).

## 4. Information ignored
| Page | reason-class | one-line reason |
|------|--------------|-----------------|
| `wiki/sources/2026-07-06-sevilla-emarketer-custom-ai-coded-apps-trim-saas-expenses.md` | off-facet | MKB vervangt SaaS door zelfgebouwde apps |
| `wiki/sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness.md` | off-facet | Chinese open-source-modellen; geen datamarkt |
| `wiki/entities/HubSpot.md` | off-facet | marketing-SaaS |
| `wiki/concepts/generative-ai.md` | off-facet | algemeen GenAI-begrip |
| `wiki/sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening.md` | off-facet | sectorblootstelling NL |
| `wiki/sources/2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs.md` | off-facet | macro-investering; gebruikt in de prognose-vraag |
| `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | off-facet | adoptiekaders in organisaties |
| `wiki/sources/2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about.md` | off-facet | HBS-onderzoeksinitiatief |
| `wiki/entities/AI%20Index.md` | wrong-granularity | entiteitskaart; de rapportbronnen zelf zijn gebruikt |
| `wiki/sources/2026-07-07-sinofsky-amble-a16z-software-in-the-age-of-agents.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-08-gauch-bcg-so-what-will-ai-agents-replace-your-crm.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-18-bloomberg-originals-how-china-plans-to-win-global-ai-race.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-18-reuters-on-assignment-inside-chinas-ai-race.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/ai-agents.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/enterprise-ai-adoption.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-30-michael-miller-department-of-war-ai-adoption.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-10-04-chu-liu-dw-the-dip-how-china-is-viewing-the-ai-race.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/foundation-models.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/micro-productivity-trap.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/jagged-frontier.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-12-tan-a16z-new-rules-for-founders.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/software-3.0.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-28-brynjolfsson-canaries-coal-mine.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-18-covello-gs-new-models-ai-investment-landscape.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-21-jones-stanford-gsb-ai-and-our-economic-future.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-10-07-richardson-reuters-econ-world-ai-at-work.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/syntheses/harness-thinning-what-persists.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |

## 5. Information used
| Page | type | effConf | contribution |
|------|------|---------|--------------|
| `wiki/sources/2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free.md` | source | — | opnames gratis weggeven, betalen voor agentisch werk; "infrastructure or a data source/connector that doesn't accrue a lot of value" |
| `wiki/sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai.md` | source | — | ~3M modellen, 1M datasets, helft Fortune 500; platform vangt 1-2% van de waarde; Evox-copyrightzaak; Reachy Mini *(promoted: gap-expansion)* |
| `wiki/sources/2026-06-25-the-ai-factory-the-rewiring-of-indias-tech-industry.md` | source | — | Object Ways (annotatie naar robotica), NextWealth; egocentrische data; extractieve keten *(promoted: gap-expansion)* |
| `wiki/sources/2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet.md` | source | — | 52% crawlerverzoeken voor training; >50 publisher-AI-deals sinds 2023; licenties bespoke, waardering onopgelost; marktplaats *(promoted: gap-expansion)* |
| `wiki/sources/2026-04-28-ai-index-report-2025.md` | source | — | Figure AI $675M bij $2,6B; C4-restricties 5-7% naar 20-33% *(promoted: gap-expansion)* |
| `wiki/sources/2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2.md` | source | — | Large Action Model (xLAM) getraind op synthetische multi-turn-trajecten; gewichten en trainingsdata open *(promoted: gap-expansion)* |
| `wiki/concepts/responsible-ai.md` | concept | — | consent/surveillance van data-werkers; data commons krimpt *(promoted: gap-expansion)* |
| `wiki/sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing.md` | source | — | synthetische-dataleverancier; geen teststandaard dus vertrouwde leverancier wint; contracten via insiders *(promoted: gap-expansion)* |

## 6. Answer-element map
| Anchor | Answer element (claim) | Wiki page(s) | Section / span used |
|--------|------------------------|--------------|---------------------|
| [W1] | Object Ways (annotatie naar robotica), NextWealth; egocentrische data; extractieve keten | [[sources/2026-06-25-the-ai-factory-the-rewiring-of-indias-tech-industry]] | ## TL;DR |
| [W2] | ~3M modellen, 1M datasets, helft Fortune 500; platform vangt 1-2% van de waarde; Evox-copyrightzaak; Reachy Mini | [[sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai]] | ## TL;DR punten 1, 9, 10, 11 |
| [W3] | 52% crawlerverzoeken voor training; >50 publisher-AI-deals sinds 2023; licenties bespoke, waardering onopgelost; marktplaats | [[sources/2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet]] | Key findings |
| [W4] | Figure AI $675M bij $2,6B; C4-restricties 5-7% naar 20-33% | [[sources/2026-04-28-ai-index-report-2025]] | corporate activity; RAI-highlight |
| [W5] | Large Action Model (xLAM) getraind op synthetische multi-turn-trajecten; gewichten en trainingsdata open | [[sources/2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2]] | method |
| [W6] | consent/surveillance van data-werkers; data commons krimpt | [[concepts/responsible-ai]] | FT-film-sectie; data commons |
| [W7] | synthetische-dataleverancier; geen teststandaard dus vertrouwde leverancier wint; contracten via insiders | [[sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing]] | ## TL;DR |
| [W8] | opnames gratis weggeven, betalen voor agentisch werk; "infrastructure or a data source/connector that doesn't accrue a lot of value" | [[sources/2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free]] | ## TL;DR punten 1, 3, 4 |

## 7. Final answer
De wiki noemt **weinig bedrijven die data voor embodied AI verzamelen**. De meest directe zijn Indiase leveranciers. Object Ways begon in 2019 als annotatiebedrijf en verzamelt nu "gripper data, teleoperations data". Het bedrijf verwacht naar eigen zeggen "500 million hours [of data] in a single day". NextWealth doet annotatiewerk op het platteland [W1]. Figure AI haalde $675M op bij een waardering van $2,6 mld [W4]. Hugging Face host ~3M modellen en 1M datasets en wordt gebruikt door de helft van de Fortune 500. Het bedrijf wil als platform 1-2% van de gecreëerde waarde vangen en bouwt Reachy Mini-robots [W2].

**Licentiemarkt.** De beste analogie in de wiki is de markt voor webcontent. In juni 2026 diende 52% van de crawlerverzoeken voor AI-training. Sinds 2023 zijn er meer dan 50 deals tussen publishers en AI-bedrijven gesloten. Cloudflare beschrijft de keten als "transparency created scarcity. Scarcity created leverage. Leverage accelerated licensing". Wel zijn de deals "largely bespoke", en is de waardering van content nog onopgelost [W3]. Een waarschuwing over het verdienmodel komt van Fireflies: geef opnames gratis weg en vraag geld voor het agentische werk. Wie alleen "a data source or connector" is, "doesn't accrue a lot of value" [W8].

**Synthetische concurrentie.** Salesforce traint zijn Large Action Model (xLAM) op synthetische multi-turn-trajecten en publiceert die data open [W5]. Null Labs verkoopt synthetische beelddata. Zonder teststandaard wint "the trusted vendor" [W7].

**Herkomst en consent.** Werkers moeten soms camera's dragen "with no extra money", en "this data can be used against the workers" [W6]. Hugging Face ligt onder vuur in de copyrightzaak van Evox [W2]. De C4-restricties stegen van 5-7% naar 20-33% [W4].

**Gaten.** De wiki heeft niets over Scale AI, Surge, Sama, Mechanical Turk, Physical Intelligence, General Intuition, Medal of een betaalde datamarktplaats voor particulieren.

## 8. Trace artifact
Machine-readable provenance: [`2026-10-15-bedrijven-data-embodied-ai-datamarkten-query-trace.json`](2026-10-15-bedrijven-data-embodied-ai-datamarkten-query-trace.json)
