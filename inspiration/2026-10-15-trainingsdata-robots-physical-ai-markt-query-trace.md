---
type: query-trace
question: "Welke markt en groei is er voor trainingsdata voor robots en physical AI?"
date: 2026-10-15
language: nl
trace: "2026-10-15-trainingsdata-robots-physical-ai-markt-query-trace.json"
pages_used: 8
pages_ignored: 48
---

# Query trace — Markt en groei voor robot- en physical-AI-trainingsdata

## 1. Question
- **Original:** Welke markt en groei is er voor trainingsdata voor robots en physical AI?
- **Restated:** Hoe groot is en hoe snel groeit de markt voor robotica/physical AI, en wat zegt de wiki over vraag naar en aanbod van trainingsdata voor robots?
- **Facets:** 1) omvang en groei van de robotica/physical-AI-markt 2) vraag naar en aanbod van robot-trainingsdata (wie levert, tegen welke prijs) 3) rol van synthetische versus echte data

## 2. Paths explored
Retrieval: `node scripts/wiki-retrieve.mjs --no-bump --json -n 12 "<question>"` (graph available: true; 11 qmd hits, 55 candidates). `--no-bump` because the caller forbade modifying wiki pages.

**qmd hits** (relevance stream)
| # | Page | type | qmd score | fused | verdict |
|---|------|------|-----------|-------|---------|
| 1 | `wiki/sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening.md` | source | 1.00 | 0.94 | IGNORE |
| 2 | `wiki/concepts/responsible-ai.md` | concept | 0.50 | 0.95 | USE |
| 3 | `wiki/sources/2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable.md` | source | 0.33 | 0.91 | USE |
| 4 | `wiki/sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing.md` | source | 0.25 | 0.90 | USE |
| 5 | `wiki/sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai.md` | source | 0.20 | 0.88 | USE |
| 6 | `wiki/concepts/agentic-web.md` | concept | 0.14 | 0.83 | IGNORE |
| 7 | `wiki/concepts/generative-ai.md` | concept | 0.13 | 0.81 | IGNORE |
| 8 | `wiki/sources/2026-09-30-singh-botha-bloomberg-flow-engineering-ai-hardware-design.md` | source | 0.11 | 0.84 | IGNORE |
| 9 | `wiki/sources/2026-04-28-ai-index-report-2025.md` | source | 0.10 | 0.83 | USE |
| 10 | `wiki/entities/HubSpot.md` | entity | 0.09 | 0.80 | IGNORE |
| 11 | `wiki/concepts/industrial-ai-agents.md` | concept | 0.08 | 0.74 | USE |

**graph neighbours** (`--hops 1`, typed-edge stream)
| Page | reached via | hops | fused | verdict |
|------|-------------|------|-------|---------|
| `wiki/sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai.md` | sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.47 | IGNORE |
| `wiki/sources/2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces.md` | sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.46 | IGNORE |
| `wiki/sources/2026-04-28-brynjolfsson-canaries-coal-mine.md` | sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.46 | IGNORE |
| `wiki/sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company.md` | sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.45 | IGNORE |
| `wiki/sources/2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity.md` | sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.44 | IGNORE |
| `wiki/concepts/agent-oversight-and-delegation.md` | concepts/responsible-ai --part-of--> this | 1 | 0.43 | IGNORE |
| `wiki/concepts/ai-sovereignty.md` | concepts/responsible-ai --supports--> this | 1 | 0.43 | IGNORE |
| `wiki/concepts/enterprise-ai-adoption.md` | concepts/responsible-ai --part-of--> this | 1 | 0.43 | IGNORE |
| `wiki/concepts/ai-employment-effects.md` | concepts/responsible-ai --supports--> this | 1 | 0.42 | IGNORE |
| `wiki/sources/2025-07-31-wang-agentspec-runtime-enforcement-llm-agents.md` | concepts/responsible-ai --supports--> this | 1 | 0.40 | IGNORE |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | sources/2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable --supports--> this | 1 | 0.40 | IGNORE |
| `wiki/sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity.md` | sources/2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable --supports--> this | 1 | 0.39 | IGNORE |
| `wiki/sources/2026-08-11-ellmer-dhar-bcg-so-what-is-your-ai-rollout-built-to-fail.md` | sources/2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable --supports--> this | 1 | 0.39 | IGNORE |
| `wiki/sources/2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2.md` | sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing --supports--> this | 1 | 0.38 | IGNORE |
| `wiki/sources/2026-03-20-huggingface-agentic-evaluations-workshop.md` | sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing --supports--> this | 1 | 0.38 | IGNORE |
| `wiki/sources/2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success.md` | sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing --supports--> this | 1 | 0.37 | IGNORE |
| `wiki/sources/2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report.md` | sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing --supports--> this | 1 | 0.37 | IGNORE |
| `wiki/sources/2026-09-30-yc-root-access-startup-industrial-base-dc.md` | sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing --part-of--> this | 1 | 0.36 | IGNORE |
| `wiki/sources/2026-10-02-hiza-bloomberg-lockheed-ai-openai-f35.md` | sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing --supports--> this | 1 | 0.36 | IGNORE |
| `wiki/sources/2026-07-08-jensen-huang-why-companies-need-open-agent-systems.md` | sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai --supports--> this | 1 | 0.35 | IGNORE |
| `wiki/sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness.md` | sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai --supports--> this | 1 | 0.35 | IGNORE |
| `wiki/sources/2026-08-06-garry-tan-own-your-intelligence.md` | sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai --supports--> this | 1 | 0.34 | IGNORE |
| `wiki/sources/2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai.md` | sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai --supports--> this | 1 | 0.34 | IGNORE |
| `wiki/sources/2026-08-18-covello-gs-new-models-ai-investment-landscape.md` | sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai --supports--> this | 1 | 0.34 | IGNORE |
| `wiki/sources/2026-09-01-cfa-institute-agentic-ai-finance-workflows-governance.md` | sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai --supports--> this | 1 | 0.33 | IGNORE |
| `wiki/sources/2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai.md` | sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai --supports--> this | 1 | 0.33 | IGNORE |
| `wiki/sources/2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over.md` | sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai --supports--> this | 1 | 0.33 | IGNORE |
| `wiki/sources/2026-09-18-bloomberg-originals-how-china-plans-to-win-global-ai-race.md` | sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/concepts/ai-agents.md` | concepts/agentic-web --depends-on--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-09-30-michael-miller-department-of-war-ai-adoption.md` | sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-09-30-murphy-koomen-diu-defense-ai-adoption.md` | sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/concepts/document-intelligence.md` | concepts/responsible-ai --supports--> this | 1 | 0.31 | IGNORE |
| `wiki/concepts/foundation-models.md` | concepts/generative-ai --uses--> this | 1 | 0.30 | IGNORE |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | concepts/generative-ai --supports--> this | 1 | 0.30 | USE |
| `wiki/concepts/jagged-frontier.md` | concepts/generative-ai --instance-of--> this | 1 | 0.30 | IGNORE |
| `wiki/concepts/answer-engine-optimization.md` | concepts/agentic-web --uses--> this | 1 | 0.29 | IGNORE |
| `wiki/sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees.md` | sources/2026-09-30-singh-botha-bloomberg-flow-engineering-ai-hardware-design --contradicts--> this | 1 | 0.29 | IGNORE |
| `wiki/sources/2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering.md` | sources/2026-09-30-singh-botha-bloomberg-flow-engineering-ai-hardware-design --supports--> this | 1 | 0.29 | IGNORE |
| `wiki/sources/2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet.md` | sources/2026-04-28-ai-index-report-2025 --supports--> this | 1 | 0.29 | IGNORE |
| `wiki/concepts/agent-harness.md` | concepts/industrial-ai-agents --depends-on--> this | 1 | 0.29 | IGNORE |
| `wiki/sources/2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook.md` | entities/HubSpot --published-by--> this | 1 | 0.28 | IGNORE |
| `wiki/sources/2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook.md` | entities/HubSpot --published-by--> this | 1 | 0.28 | IGNORE |
| `wiki/sources/2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide.md` | concepts/industrial-ai-agents --supports--> this | 1 | 0.28 | IGNORE |
| `wiki/concepts/software-3.0.md` | concepts/generative-ai --instance-of--> this | 1 | 0.27 | IGNORE |

**index.md / gap-expansion** (Step 5: one round, rg keyword sweep over `wiki/` for robot/humanoid/embodied/physical AI/world model/synthetic data/licensing/etc.)
| Page | why added |
|------|-----------|
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | graph-only candidate promoted: hard tech +$560B beurswaarde/+$30B omzet 2022-25; robotica 13-23%; definitie physical AI |
| `wiki/sources/2026-06-25-the-ai-factory-the-rewiring-of-indias-tech-industry.md` | not in ledger; found by keyword sweep: egocentrische data voor humanoids: GoPro/Meta-brillen, ~10.000 roepie/maand extra, Object Ways gripper/teleop-data |

## 3. Ignore policy applied
- `off-facet` — semantically adjacent but answers none of the facets.
- `below-threshold` — low fused score and no facet needs the page (graph-only long tail).

## 4. Information ignored
| Page | reason-class | one-line reason |
|------|--------------|-----------------|
| `wiki/sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening.md` | off-facet | Nederlandse AI-blootstelling van IT/zakelijke dienstverlening; geen robotica- of datamarktcijfers |
| `wiki/sources/2026-09-30-singh-botha-bloomberg-flow-engineering-ai-hardware-design.md` | off-facet | AI voor hardware-ontwerp (chip/PCB), niet over robotdata |
| `wiki/concepts/agentic-web.md` | off-facet | web-crawling en contentlicenties; voor deze vraag naar robotdata niet nodig (wel gebruikt in de bedrijven/licentie-vraag via de Cloudflare-bron) |
| `wiki/concepts/generative-ai.md` | off-facet | groeiprojectie gaat over AI-software, niet robotica; MGI-bron dekt dit beter |
| `wiki/entities/HubSpot.md` | off-facet | marketing-SaaS-bedrijf; geen relatie met robotdata |
| `wiki/sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-28-brynjolfsson-canaries-coal-mine.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/agent-oversight-and-delegation.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/ai-sovereignty.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/enterprise-ai-adoption.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/ai-employment-effects.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2025-07-31-wang-agentspec-runtime-enforcement-llm-agents.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-11-ellmer-dhar-bcg-so-what-is-your-ai-rollout-built-to-fail.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-03-20-huggingface-agentic-evaluations-workshop.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-30-yc-root-access-startup-industrial-base-dc.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-10-02-hiza-bloomberg-lockheed-ai-openai-f35.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-07-08-jensen-huang-why-companies-need-open-agent-systems.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-06-garry-tan-own-your-intelligence.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-18-covello-gs-new-models-ai-investment-landscape.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-01-cfa-institute-agentic-ai-finance-workflows-governance.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-18-bloomberg-originals-how-china-plans-to-win-global-ai-race.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/ai-agents.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-30-michael-miller-department-of-war-ai-adoption.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-30-murphy-koomen-diu-defense-ai-adoption.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/document-intelligence.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/foundation-models.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/jagged-frontier.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/answer-engine-optimization.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/agent-harness.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/software-3.0.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |

## 5. Information used
| Page | type | effConf | contribution |
|------|------|---------|--------------|
| `wiki/concepts/responsible-ai.md` | concept | 0.91 | data commons krimpt (C4-restricties) + extractieve keten/consent bij robot-trainingswerk |
| `wiki/sources/2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable.md` | source | — | CES-thema "physical AI, which you may call just robotics"; waarde verschuift naar fysieke uitvoering |
| `wiki/sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing.md` | source | — | synthetische dataset 10.000 beelden <45 min vs 2-4 weken verzamelen; risico synthetische artefacten |
| `wiki/sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai.md` | source | — | robotica onderbelegd; robotdata "huge... petabytes"; vertrouwen bij thuisrobots |
| `wiki/sources/2026-04-28-ai-index-report-2025.md` | source | — | industriële robots (China 51,1%, 4,28M stock, cobots 10,5%); Figure AI $675M bij $2,6B |
| `wiki/concepts/industrial-ai-agents.md` | concept | 0.66 | synthetische data voor zeldzame defecten; Brooks: eenvoudige taakspecifieke robots hebben impact |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | source | — | hard tech +$560B beurswaarde/+$30B omzet 2022-25; robotica 13-23%; definitie physical AI *(promoted: gap-expansion)* |
| `wiki/sources/2026-06-25-the-ai-factory-the-rewiring-of-indias-tech-industry.md` | source | — | egocentrische data voor humanoids: GoPro/Meta-brillen, ~10.000 roepie/maand extra, Object Ways gripper/teleop-data *(promoted: gap-expansion)* |

## 6. Answer-element map
| Anchor | Answer element (claim) | Wiki page(s) | Section / span used |
|--------|------------------------|--------------|---------------------|
| [W1] | data commons krimpt (C4-restricties) + extractieve keten/consent bij robot-trainingswerk | [[concepts/responsible-ai]] | ## The data commons is shrinking; sectie FT-film (extractive supply chain) |
| [W2] | CES-thema "physical AI, which you may call just robotics"; waarde verschuift naar fysieke uitvoering | [[sources/2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable]] | ## TL;DR punt 5 |
| [W3] | synthetische dataset 10.000 beelden <45 min vs 2-4 weken verzamelen; risico synthetische artefacten | [[sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing]] | ## TL;DR |
| [W4] | robotica onderbelegd; robotdata "huge... petabytes"; vertrouwen bij thuisrobots | [[sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai]] | ## TL;DR punt 11 |
| [W5] | industriële robots (China 51,1%, 4,28M stock, cobots 10,5%); Figure AI $675M bij $2,6B | [[sources/2026-04-28-ai-index-report-2025]] | ### Robotics; corporate-activity-lijst |
| [W6] | synthetische data voor zeldzame defecten; Brooks: eenvoudige taakspecifieke robots hebben impact | [[concepts/industrial-ai-agents]] | ### Synthetic data for rare-event training; Carrier/Brooks |
| [W7] | egocentrische data voor humanoids: GoPro/Meta-brillen, ~10.000 roepie/maand extra, Object Ways gripper/teleop-data | [[sources/2026-06-25-the-ai-factory-the-rewiring-of-indias-tech-industry]] | ## TL;DR bullet 2 |
| [W8] | hard tech +$560B beurswaarde/+$30B omzet 2022-25; robotica 13-23%; definitie physical AI | [[sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas]] | punt 2 (themes) + tabel 2040-scenario |

## 7. Final answer
De wiki bevat **geen marktomvang of groeicijfer voor robot-trainingsdata als zodanig**. Wel geeft hij indirecte signalen over groei, vraag en aanbod.

**Groei.** MGI rekent robotica tot het thema "hard tech". Dat thema won tussen 2022 en 2025 $560 mld aan beurswaarde en $30 mld aan omzet. Robotica groeit in het 2040-scenario met 13-23% per jaar. MGI definieert *physical AI* als systemen die "sense, think, and act in the real world" [W8] (zie [[2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas|MGI Race Takes Off]]). Op CES heette het hele thema "physical AI, which you may call just robotics" [W2]. Figure AI (humanoïde robots) haalde $675M op bij een waardering van $2,6 mld. China plaatste 51,1% van alle industriële robots, en cobots stegen van 2,8% naar 10,5% van de nieuwe installaties [W5]. Volgens de CEO van Hugging Face is robotica ondergeïnvesteerd. Robotdata noemt hij "huge... petabytes" [W4].

**Aanbod van data.** In India dragen ~60 van de 200 textielarbeiders 6-8 uur per dag GoPro's en Meta-brillen, voor ~10.000 roepie per maand extra. Zo leggen ze egocentrische data vast van vouwen, vegen en afwassen. Object Ways verzamelt "gripper data, teleoperations data" [W7]. De wiki noemt die keten "extractive by design", met een consentrisico voor de werkers [W1].

**Synthetische data.** Die werkt goed voor zeldzame gebeurtenissen [W6]. Ze maakt ook snel labelen mogelijk: 10.000 beelden in minder dan 45 minuten, tegen 2-4 weken verzamelen. Het risico is dat een model synthetische artefacten leert [W3]. Tegelijk krimpt de *data commons*: de restricties op C4-domeinen stegen van 5-7% naar 20-33% [W1].

**Gaten.** De wiki heeft geen prijs per uur robotdata, geen omvang van de labeling-markt en niets over Scale AI, Physical Intelligence, General Intuition of Medal.

## 8. Trace artifact
Machine-readable provenance: [`2026-10-15-trainingsdata-robots-physical-ai-markt-query-trace.json`](2026-10-15-trainingsdata-robots-physical-ai-markt-query-trace.json)
