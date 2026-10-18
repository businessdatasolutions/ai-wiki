---
type: query-trace
question: "Welke prognoses voor AI-investeringen, humanoids en de impact op arbeid en platformwerk staan in de wiki?"
date: 2026-10-15
language: nl
trace: "2026-10-15-prognoses-ai-investeringen-humanoids-arbeid-query-trace.json"
pages_used: 9
pages_ignored: 52
---

# Query trace — Prognoses voor AI-investeringen, robots/humanoids en arbeid

## 1. Question
- **Original:** Welke prognoses voor AI-investeringen, humanoids en de impact op arbeid en platformwerk staan in de wiki?
- **Restated:** Welke cijfers en prognoses geeft de wiki voor AI-investeringen en marktgroei, voor robots/humanoids, en voor de gevolgen voor arbeid en platformwerk?
- **Facets:** 1) AI-investeringen en marktprognoses 2) robots/humanoids: adoptie en verwachtingen 3) arbeid en platformwerk (incl. data-arbeid)

## 2. Paths explored
Retrieval: `node scripts/wiki-retrieve.mjs --no-bump --json -n 12 "<question>"` (graph available: true; 10 qmd hits, 58 candidates). `--no-bump` because the caller forbade modifying wiki pages.

**qmd hits** (relevance stream)
| # | Page | type | qmd score | fused | verdict |
|---|------|------|-----------|-------|---------|
| 1 | `wiki/concepts/ai-employment-effects.md` | concept | 1.00 | 0.95 | USE |
| 2 | `wiki/sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening.md` | source | 0.50 | 0.93 | IGNORE |
| 3 | `wiki/entities/Anthropic%20Economic%20Index.md` | entity | 0.20 | 0.85 | IGNORE |
| 4 | `wiki/sources/2026-03-07-vitucci-onshore-next-industry-ai-will-disrupt.md` | source | 0.17 | 0.90 | IGNORE |
| 5 | `wiki/sources/2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report.md` | source | 0.14 | 0.88 | IGNORE |
| 6 | `wiki/concepts/automation-vs-augmentation.md` | concept | 0.13 | 0.89 | USE |
| 7 | `wiki/concepts/strategic-foresight.md` | concept | 0.11 | 0.79 | IGNORE |
| 8 | `wiki/sources/2026-04-28-anthropic-economic-index-q4-2025.md` | source | 0.10 | 0.84 | IGNORE |
| 9 | `wiki/sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going.md` | source | 0.09 | 0.83 | IGNORE |
| 10 | `wiki/sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai.md` | source | 0.08 | 0.82 | IGNORE |

**graph neighbours** (`--hops 1`, typed-edge stream)
| Page | reached via | hops | fused | verdict |
|------|-------------|------|-------|---------|
| `wiki/concepts/durable-skills.md` | concepts/ai-employment-effects --instance-of--> this | 1 | 0.47 | IGNORE |
| `wiki/concepts/enterprise-ai-adoption.md` | concepts/ai-employment-effects --caused--> this | 1 | 0.47 | USE |
| `wiki/concepts/ai-deskilling.md` | concepts/ai-employment-effects --instance-of--> this | 1 | 0.46 | IGNORE |
| `wiki/concepts/responsible-ai.md` | concepts/ai-employment-effects --supports--> this | 1 | 0.45 | IGNORE |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | concepts/ai-employment-effects --supports--> this | 1 | 0.43 | USE |
| `wiki/sources/2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs.md` | concepts/ai-employment-effects --supports--> this | 1 | 0.43 | IGNORE |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | concepts/ai-employment-effects --supports--> this | 1 | 0.42 | IGNORE |
| `wiki/sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era.md` | concepts/ai-employment-effects --supports--> this | 1 | 0.42 | IGNORE |
| `wiki/sources/2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces.md` | sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.41 | IGNORE |
| `wiki/sources/2026-04-28-brynjolfsson-canaries-coal-mine.md` | sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.40 | IGNORE |
| `wiki/sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company.md` | sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.40 | IGNORE |
| `wiki/sources/2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity.md` | sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.39 | IGNORE |
| `wiki/concepts/ai-washing.md` | concepts/ai-employment-effects --part-of--> this | 1 | 0.39 | IGNORE |
| `wiki/sources/2026-05-11-hill-vori-grocery-os-paper-and-fax.md` | sources/2026-03-07-vitucci-onshore-next-industry-ai-will-disrupt --supports--> this | 1 | 0.39 | IGNORE |
| `wiki/sources/2026-05-20-glasgow-campfire-erp-for-ai-revolution.md` | sources/2026-03-07-vitucci-onshore-next-industry-ai-will-disrupt --supports--> this | 1 | 0.38 | IGNORE |
| `wiki/sources/2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer.md` | sources/2026-03-07-vitucci-onshore-next-industry-ai-will-disrupt --supports--> this | 1 | 0.38 | IGNORE |
| `wiki/sources/2026-04-28-ftsg-convergence-outlook-2026.md` | sources/2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report --supports--> this | 1 | 0.37 | IGNORE |
| `wiki/sources/2026-04-30-ai-index-report-2026.md` | sources/2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report --supports--> this | 1 | 0.37 | USE |
| `wiki/sources/2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas.md` | sources/2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report --supports--> this | 1 | 0.36 | IGNORE |
| `wiki/sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing.md` | sources/2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report --supports--> this | 1 | 0.36 | IGNORE |
| `wiki/concepts/micro-productivity-trap.md` | concepts/automation-vs-augmentation --contradicts--> this | 1 | 0.36 | IGNORE |
| `wiki/concepts/ai-coding-productivity-evidence.md` | concepts/automation-vs-augmentation --part-of--> this | 1 | 0.34 | IGNORE |
| `wiki/concepts/ai-benchmarks.md` | concepts/automation-vs-augmentation --supports--> this | 1 | 0.34 | IGNORE |
| `wiki/concepts/jagged-frontier.md` | concepts/automation-vs-augmentation --supports--> this | 1 | 0.34 | IGNORE |
| `wiki/concepts/dynamic-capabilities.md` | concepts/strategic-foresight --part-of--> this | 1 | 0.33 | IGNORE |
| `wiki/sources/2026-03-20-huggingface-agentic-evaluations-workshop.md` | concepts/automation-vs-augmentation --supports--> this | 1 | 0.33 | IGNORE |
| `wiki/concepts/strategy.md` | concepts/strategic-foresight --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-06-16-anthropic-economic-index-agentic-coding-returns-to-expertise.md` | sources/2026-04-28-anthropic-economic-index-q4-2025 --contradicts--> this | 1 | 0.31 | IGNORE |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | concepts/automation-vs-augmentation --supports--> this | 1 | 0.30 | IGNORE |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | sources/2026-04-28-anthropic-economic-index-q4-2025 --supports--> this | 1 | 0.30 | IGNORE |
| `wiki/sources/2026-06-16-mollick-simon-sinek-ai-skills-experience-edge.md` | sources/2026-04-28-anthropic-economic-index-q4-2025 --supports--> this | 1 | 0.30 | IGNORE |
| `wiki/sources/2026-02-09-hubspot-customer-success-with-claude.md` | concepts/automation-vs-augmentation --supports--> this | 1 | 0.30 | IGNORE |
| `wiki/sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs.md` | sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going --contradicts--> this | 1 | 0.30 | USE |
| `wiki/sources/2026-02-18-lyft-customer-support-with-claude.md` | concepts/automation-vs-augmentation --supports--> this | 1 | 0.30 | IGNORE |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going --supports--> this | 1 | 0.30 | IGNORE |
| `wiki/sources/2026-04-26-how-to-win-when-software-is-not-a-moat-evan-spiegel-snapchat-ceo.md` | sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going --supports--> this | 1 | 0.29 | IGNORE |
| `wiki/sources/2026-04-28-dellacqua-jagged-technological-frontier.md` | sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going --contradicts--> this | 1 | 0.29 | IGNORE |
| `wiki/sources/2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering.md` | sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going --supports--> this | 1 | 0.28 | IGNORE |
| `wiki/entities/Lenny's-Podcast.md` | sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going --published-by--> this | 1 | 0.28 | IGNORE |
| `wiki/sources/2026-05-08-running-an-ai-native-engineering-org.md` | sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going --supports--> this | 1 | 0.28 | IGNORE |
| `wiki/sources/2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook.md` | sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going --supports--> this | 1 | 0.28 | IGNORE |
| `wiki/entities/Anthropic.md` | sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai --published-by--> this | 1 | 0.28 | IGNORE |
| `wiki/concepts/analogical-reasoning.md` | concepts/strategic-foresight --supports--> this | 1 | 0.28 | IGNORE |
| `wiki/sources/2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era.md` | sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going --supports--> this | 1 | 0.28 | IGNORE |
| `wiki/sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company.md` | sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going --supports--> this | 1 | 0.28 | IGNORE |
| `wiki/sources/2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world.md` | sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai --supports--> this | 1 | 0.27 | IGNORE |
| `wiki/sources/2026-06-22-bbc-what-if-were-wrong-about-ai-layoffs.md` | sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai --supports--> this | 1 | 0.27 | IGNORE |
| `wiki/entities/Anthropic-Economic-Index.md` | sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai --part-of--> this | 1 | 0.25 | IGNORE |

**index.md / gap-expansion** (Step 5: one round, rg keyword sweep over `wiki/` for robot/humanoid/embodied/physical AI/world model/synthetic data/licensing/etc.)
| Page | why added |
|------|-----------|
| `wiki/concepts/enterprise-ai-adoption.md` | graph-only candidate promoted: MGI: $2,9T US / $28,7T wereldwijd per jaar in 2030; 77% agents / 23% robots ($0,67T) |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | graph-only candidate promoted: AI software & services $1,5-4,6T in 2040 (17-25% CAGR vanaf $85B); 18 arena's +$18T; videogames als arena; robotica 13-23% |
| `wiki/sources/2026-04-30-ai-index-report-2026.md` | graph-only candidate promoted: US private AI-investering $285,9B (2025) vs $109,1B (2024); 1.953 nieuw gefinancierde AI-bedrijven; robots 12% huishoudtaken |
| `wiki/sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs.md` | graph-only candidate promoted: Gartner: uitgaven aan agents $86,4B (2025) naar $206,5B (2026) |
| `wiki/sources/2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs.md` | not in ledger; found by keyword sweep: $5-7T tot 2030; piek 2,5-3% bbp in 2027-28; bijdrage ~0,1 procentpunt aan US-groei |
| `wiki/sources/2026-08-18-covello-gs-new-models-ai-investment-landscape.md` | not in ledger; found by keyword sweep: 95% consumenten gebruikt gratis AI; monetisatie moet uit bedrijven komen; markt stelt capex ter discussie |
| `wiki/sources/2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai.md` | not in ledger; found by keyword sweep: ~40M naar >70M Amerikanen in non-employment work (ongesourcet); embodied AI een zegen voor vergrijzend Azië |

## 3. Ignore policy applied
- `off-facet` — semantically adjacent but answers none of the facets.
- `redundant` — repeats a claim carried by a stronger USE page.
- `wrong-granularity` — entity card where the facet needs figures; the underlying sources were used.
- `below-threshold` — low fused score and no facet needs the page (graph-only long tail).

## 4. Information ignored
| Page | reason-class | one-line reason |
|------|--------------|-----------------|
| `wiki/sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening.md` | off-facet | sectorblootstelling van NL IT/zakelijke dienstverlening; geen investerings-, robot- of platformwerkcijfers |
| `wiki/sources/2026-03-07-vitucci-onshore-next-industry-ai-will-disrupt.md` | off-facet | disruptie van accountancy |
| `wiki/sources/2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report.md` | redundant | herhaalt de cijfers van het AI Index 2026-rapport (W1) |
| `wiki/entities/Anthropic%20Economic%20Index.md` | wrong-granularity | entiteitskaart |
| `wiki/sources/2026-04-28-anthropic-economic-index-q4-2025.md` | off-facet | Claude-gebruik per taak; geen robots/investering |
| `wiki/sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going.md` | off-facet | algemene duiding, geen kwantitatieve prognose die hier nodig is |
| `wiki/sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai.md` | redundant | arbeidsmarkteffecten al samengevat in ai-employment-effects (W7) |
| `wiki/concepts/strategic-foresight.md` | redundant | verwijst naar dezelfde MGI-projecties als W2 |
| `wiki/concepts/durable-skills.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/ai-deskilling.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/responsible-ai.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-28-brynjolfsson-canaries-coal-mine.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/ai-washing.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-11-hill-vori-grocery-os-paper-and-fax.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-20-glasgow-campfire-erp-for-ai-revolution.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-28-ftsg-convergence-outlook-2026.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/micro-productivity-trap.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/ai-coding-productivity-evidence.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/ai-benchmarks.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/jagged-frontier.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/dynamic-capabilities.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-03-20-huggingface-agentic-evaluations-workshop.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/strategy.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-06-16-anthropic-economic-index-agentic-coding-returns-to-expertise.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-06-16-mollick-simon-sinek-ai-skills-experience-edge.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-02-09-hubspot-customer-success-with-claude.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-02-18-lyft-customer-support-with-claude.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-26-how-to-win-when-software-is-not-a-moat-evan-spiegel-snapchat-ceo.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-28-dellacqua-jagged-technological-frontier.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/entities/Lenny's-Podcast.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-08-running-an-ai-native-engineering-org.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/entities/Anthropic.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/analogical-reasoning.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-06-22-bbc-what-if-were-wrong-about-ai-layoffs.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/entities/Anthropic-Economic-Index.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |

## 5. Information used
| Page | type | effConf | contribution |
|------|------|---------|--------------|
| `wiki/concepts/ai-employment-effects.md` | concept | 0.88 | data-annotatie en egocentrische robotdata als nieuwe arbeidslaag; robotaxi-impact over 5-10 jaar |
| `wiki/concepts/automation-vs-augmentation.md` | concept | 0.91 | MGI: agents 44% / robots 13% van US-werkuren; 65/35 niet-fysiek/fysiek; robot-centrisch archetype 8% |
| `wiki/concepts/enterprise-ai-adoption.md` | concept | 0.95 | MGI: $2,9T US / $28,7T wereldwijd per jaar in 2030; 77% agents / 23% robots ($0,67T) *(promoted: gap-expansion)* |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | source | — | AI software & services $1,5-4,6T in 2040 (17-25% CAGR vanaf $85B); 18 arena's +$18T; videogames als arena; robotica 13-23% *(promoted: gap-expansion)* |
| `wiki/sources/2026-04-30-ai-index-report-2026.md` | source | — | US private AI-investering $285,9B (2025) vs $109,1B (2024); 1.953 nieuw gefinancierde AI-bedrijven; robots 12% huishoudtaken *(promoted: gap-expansion)* |
| `wiki/sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs.md` | source | — | Gartner: uitgaven aan agents $86,4B (2025) naar $206,5B (2026) *(promoted: gap-expansion)* |
| `wiki/sources/2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs.md` | source | — | $5-7T tot 2030; piek 2,5-3% bbp in 2027-28; bijdrage ~0,1 procentpunt aan US-groei *(promoted: gap-expansion)* |
| `wiki/sources/2026-08-18-covello-gs-new-models-ai-investment-landscape.md` | source | — | 95% consumenten gebruikt gratis AI; monetisatie moet uit bedrijven komen; markt stelt capex ter discussie *(promoted: gap-expansion)* |
| `wiki/sources/2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai.md` | source | — | ~40M naar >70M Amerikanen in non-employment work (ongesourcet); embodied AI een zegen voor vergrijzend Azië *(promoted: gap-expansion)* |

## 6. Answer-element map
| Anchor | Answer element (claim) | Wiki page(s) | Section / span used |
|--------|------------------------|--------------|---------------------|
| [W1] | US private AI-investering $285,9B (2025) vs $109,1B (2024); 1.953 nieuw gefinancierde AI-bedrijven; robots 12% huishoudtaken | [[sources/2026-04-30-ai-index-report-2026]] | Top Takeaways #5, #7 |
| [W2] | AI software & services $1,5-4,6T in 2040 (17-25% CAGR vanaf $85B); 18 arena's +$18T; videogames als arena; robotica 13-23% | [[sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas]] | punten 1-2; tabel |
| [W3] | $5-7T tot 2030; piek 2,5-3% bbp in 2027-28; bijdrage ~0,1 procentpunt aan US-groei | [[sources/2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs]] | punten 1, 4 |
| [W4] | Gartner: uitgaven aan agents $86,4B (2025) naar $206,5B (2026) | [[sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs]] | punt 2 |
| [W5] | MGI: agents 44% / robots 13% van US-werkuren; 65/35 niet-fysiek/fysiek; robot-centrisch archetype 8% | [[concepts/automation-vs-augmentation]] | ### 17. The MGI structural framework |
| [W6] | MGI: $2,9T US / $28,7T wereldwijd per jaar in 2030; 77% agents / 23% robots ($0,67T) | [[concepts/enterprise-ai-adoption]] | ## The MGI workflow-as-unit... scaffold |
| [W7] | data-annotatie en egocentrische robotdata als nieuwe arbeidslaag; robotaxi-impact over 5-10 jaar | [[concepts/ai-employment-effects]] | FT-film-sectie; Khan |
| [W8] | 95% consumenten gebruikt gratis AI; monetisatie moet uit bedrijven komen; markt stelt capex ter discussie | [[sources/2026-08-18-covello-gs-new-models-ai-investment-landscape]] | punten 2, 9 |
| [W9] | ~40M naar >70M Amerikanen in non-employment work (ongesourcet); embodied AI een zegen voor vergrijzend Azië | [[sources/2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai]] | punt 7; source-quality |

## 7. Final answer
**Investeringen en markt.** De private AI-investering in de VS bedroeg $285,9 mld in 2025, tegen $109,1 mld in 2024. Dat is ~23x China ($12,4 mld). In de VS kregen 1.953 nieuwe AI-bedrijven financiering [W1]. MGI verwacht voor AI-software en -diensten $1,5-4,6 bln omzet in 2040, ofwel 17-25% groei per jaar vanaf $85 mld. MGI's 18 "arena's" wonnen sinds 2022 $18 bln aan beurswaarde, en videogames vormen een van die arena's [W2]. Goldman Sachs (Hatzius) noemt $5-7 bln cumulatief tot 2030, met een piek van 2,5-3% van het bbp in 2027-28. De bijdrage aan de Amerikaanse groei is nu ~0,1 procentpunt [W3]. Gartner verwacht dat de uitgaven aan agents stijgen van $86,4 mld in 2025 naar $206,5 mld in 2026 [W4]. Covello (ook Goldman) waarschuwt: 95% van de consumenten gebruikt gratis AI, dus het geld moet uit bedrijven komen [W8].

**Robots en humanoids.** Volgens MGI kunnen agents nu 44% van de Amerikaanse werkuren uitvoeren en robots 13%. Van alle werkuren is 35% fysiek. In het robot-centrische archetype (8% van de werkenden) vallen onder meer vakkenvullers en orderpickers [W5]. Agents en robots samen kunnen in 2030 $2,9 bln per jaar opleveren in de VS en $28,7 bln wereldwijd. Daarvan komt 23% van robots, ofwel $0,67 bln [W6]. Robots slagen nog maar in 12% van de huishoudtaken [W1]. Over humanoids specifiek staan er geen prognoses in de wiki.

**Arbeid en platformwerk.** AI schept een nieuwe laag data-arbeid: annotatie, RLHF en egocentrische data voor humanoids [W7]. Sundararajan ziet werk verschuiven naar "non-employment"-vormen, van ~40M naar meer dan 70M Amerikanen. Dat cijfer is ongesourcet. Embodied AI noemt hij "a boon" voor vergrijzend Azië [W9].

**Gaten.** De wiki heeft geen prognose voor de humanoid-markt, geen omvang van de AI-datamarkt en geen cijfers voor VR-training.

## 8. Trace artifact
Machine-readable provenance: [`2026-10-15-prognoses-ai-investeringen-humanoids-arbeid-query-trace.json`](2026-10-15-prognoses-ai-investeringen-humanoids-arbeid-query-trace.json)
