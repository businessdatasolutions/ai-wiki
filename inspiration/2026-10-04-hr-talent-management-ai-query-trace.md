---
type: query-trace
question: "Wat wordt er gezegd over human resources en talent management in relatie tot AI?"
date: 2026-10-04
language: nl
trace: "2026-10-04-hr-talent-management-ai-query-trace.json"
pages_used: 9
pages_ignored: 64
---

# Query trace — HR en talentmanagement in relatie tot AI

## 1. Question
- **Original:** Wat wordt er gezegd over human resources en talent management in relatie tot AI?
- **Restated:** Wat zegt de wiki over hoe AI talent, vaardigheden en HR-praktijk verandert, en over AI binnen HR-processen zelf?
- **Facets:** 1) F1 — hoe AI de vraag naar talent en vaardigheden verandert (banen, instroom, duurzame vaardigheden) · 2) F2 — hoe HR en management reageren (werving, bijscholing, functie- en werkontwerp) · 3) F3 — AI toegepast binnen HR-processen zelf (werving, beoordeling, agents in de organisatie)

## 2. Paths explored
Retrieval: `node scripts/wiki-retrieve.mjs --json -n 12 "…"` (qmd ∪ graph, RRF k=60, hops 1, decay-ranked). 12 qmd hits, 73 candidates; graph available.

**qmd hits** (relevance stream)
| # | Page | type | qmd score | fused | verdict |
|---|------|------|-----------|-------|---------|
| 1 | `wiki/sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening.md` | source | 0.81 | 0.94 | IGNORE |
| 2 | `wiki/sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity.md` | source | 0.57 | 0.93 | USE |
| 3 | `wiki/sources/2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services.md` | source | 0.56 | 0.91 | IGNORE |
| 4 | `wiki/sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs.md` | source | 0.54 | 0.90 | IGNORE |
| 5 | `wiki/sources/2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai.md` | source | 0.45 | 0.88 | IGNORE |
| 6 | `wiki/sources/2026-07-22-brown-wef-meet-the-leader-entry-level-jobs-in-an-ai-era.md` | source | 0.45 | 0.87 | USE |
| 7 | `wiki/sources/2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai.md` | source | 0.44 | 0.86 | IGNORE |
| 8 | `wiki/sources/2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero.md` | source | 0.42 | 0.84 | USE |
| 9 | `wiki/sources/2025-06-09-krakowski-human-centered-ai-field-experiment.md` | source | 0.4 | 0.83 | USE |
| 10 | `wiki/sources/2026-06-25-carroll-stanford-gsb-making-organizational-culture-great.md` | source | 0.39 | 0.82 | IGNORE |
| 12 | `wiki/concepts/automation-vs-augmentation.md` | concept | 0.36 | 0.81 | IGNORE |
| 11 | `wiki/concepts/durable-skills.md` | concept | 0.39 | 0.79 | USE |

**graph neighbours** (`--hops 1`, typed-edge stream)
| Page | reached via | hops | fused | verdict |
|------|-------------|------|-------|---------|
| `wiki/sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai.md` | 2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.47 | IGNORE |
| `wiki/sources/2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces.md` | 2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.46 | IGNORE |
| `wiki/sources/2026-04-28-brynjolfsson-canaries-coal-mine.md` | 2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.46 | IGNORE |
| `wiki/sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company.md` | 2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.45 | IGNORE |
| `wiki/sources/2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity.md` | 2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening --supports--> this | 1 | 0.44 | IGNORE |
| `wiki/sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness.md` | 2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --supports--> this | 1 | 0.43 | IGNORE |
| `wiki/sources/2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable.md` | 2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --supports--> this | 1 | 0.43 | IGNORE |
| `wiki/sources/2026-08-10-miller-worklab-the-ai-shift-most-companies-didnt-see-coming.md` | 2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --supports--> this | 1 | 0.42 | IGNORE |
| `wiki/sources/2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs.md` | 2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --contradicts--> this | 1 | 0.42 | IGNORE |
| `wiki/sources/2026-06-24-mckinsey-ai-supercharging-software-development.md` | 2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services --supports--> this | 1 | 0.41 | IGNORE |
| `wiki/sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage.md` | 2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services --supports--> this | 1 | 0.40 | IGNORE |
| `wiki/sources/2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over.md` | 2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services --supports--> this | 1 | 0.40 | IGNORE |
| `wiki/sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships.md` | 2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.39 | IGNORE |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | 2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.38 | IGNORE |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | 2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.38 | IGNORE |
| `wiki/sources/2026-05-01-lf-state-of-tech-talent-global-2026.md` | 2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.38 | USE |
| `wiki/sources/2026-04-30-ai-index-report-2026.md` | 2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.37 | IGNORE |
| `wiki/sources/2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era.md` | 2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.36 | IGNORE |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | 2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.36 | IGNORE |
| `wiki/sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going.md` | 2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --contradicts--> this | 1 | 0.36 | IGNORE |
| `wiki/sources/2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care.md` | 2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.35 | IGNORE |
| `wiki/sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company.md` | 2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.34 | IGNORE |
| `wiki/sources/2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset.md` | 2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.34 | IGNORE |
| `wiki/sources/2026-06-22-bbc-what-if-were-wrong-about-ai-layoffs.md` | 2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.34 | IGNORE |
| `wiki/sources/2026-06-01-lf-state-of-tech-talent-europe-2026.md` | 2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.34 | IGNORE |
| `wiki/sources/2026-04-28-reitz-higgins-spacious-thinking.md` | 2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai --supports--> this | 1 | 0.33 | IGNORE |
| `wiki/sources/2026-05-02-dutt-chatterji-ai-experimentation-to-transformation.md` | 2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai --supports--> this | 1 | 0.33 | IGNORE |
| `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | 2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-05-02-schoening-lennys-podcast-cultivating-agency-ai-era.md` | 2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026.md` | 2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai --supports--> this | 1 | 0.32 | USE |
| `wiki/sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai.md` | 2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai.md` | 2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai --supports--> this | 1 | 0.31 | IGNORE |
| `wiki/sources/2026-09-18-reuters-on-assignment-inside-chinas-ai-race.md` | 2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai --supports--> this | 1 | 0.31 | IGNORE |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | 2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero --supports--> this | 1 | 0.30 | IGNORE |
| `wiki/sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation.md` | 2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero --supports--> this | 1 | 0.30 | IGNORE |
| `wiki/sources/2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook.md` | 2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero --supports--> this | 1 | 0.30 | IGNORE |
| `wiki/sources/2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook.md` | 2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero --supports--> this | 1 | 0.30 | IGNORE |
| `wiki/sources/2025-01-08-khanfar-factors-influencing-ai-adoption-slr.md` | 2025-06-09-krakowski-human-centered-ai-field-experiment --supports--> this | 1 | 0.29 | IGNORE |
| `wiki/sources/2026-04-28-anand-wu-genai-playbook.md` | 2025-06-09-krakowski-human-centered-ai-field-experiment --supports--> this | 1 | 0.29 | IGNORE |
| `wiki/sources/2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work.md` | 2025-06-09-krakowski-human-centered-ai-field-experiment --supports--> this | 1 | 0.29 | IGNORE |
| `wiki/sources/2026-04-28-dellacqua-jagged-technological-frontier.md` | 2025-06-09-krakowski-human-centered-ai-field-experiment --supports--> this | 1 | 0.28 | IGNORE |
| `wiki/sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees.md` | 2025-06-09-krakowski-human-centered-ai-field-experiment --supports--> this | 1 | 0.28 | USE |
| `wiki/sources/2026-07-01-bello-mckinsey-podcast-serial-builder-advantage.md` | 2026-06-25-carroll-stanford-gsb-making-organizational-culture-great --supports--> this | 1 | 0.28 | IGNORE |
| `wiki/sources/2026-07-07-sinofsky-amble-a16z-software-in-the-age-of-agents.md` | 2026-06-25-carroll-stanford-gsb-making-organizational-culture-great --supports--> this | 1 | 0.28 | IGNORE |
| `wiki/concepts/ai-benchmarks.md` | durable-skills --depends-on--> this | 1 | 0.28 | IGNORE |
| `wiki/sources/2026-08-16-hill-bloomberg-leaders-ceo-skills-age-of-ai.md` | 2026-06-25-carroll-stanford-gsb-making-organizational-culture-great --supports--> this | 1 | 0.27 | IGNORE |
| `wiki/concepts/ai-employment-effects.md` | durable-skills --instance-of--> this | 1 | 0.27 | USE |
| `wiki/sources/2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs.md` | durable-skills --supports--> this | 1 | 0.26 | IGNORE |
| `wiki/concepts/enterprise-ai-adoption.md` | automation-vs-augmentation --supports--> this | 1 | 0.26 | IGNORE |
| `wiki/sources/2026-05-06-mit-ocw-future-of-mit-open-education.md` | durable-skills --supports--> this | 1 | 0.26 | IGNORE |
| `wiki/concepts/jagged-frontier.md` | automation-vs-augmentation --supports--> this | 1 | 0.26 | IGNORE |
| `wiki/sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era.md` | durable-skills --supports--> this | 1 | 0.26 | IGNORE |
| `wiki/concepts/ai-deskilling.md` | durable-skills --contradicts--> this | 1 | 0.25 | IGNORE |
| `wiki/concepts/ai-coding-productivity-evidence.md` | automation-vs-augmentation --part-of--> this | 1 | 0.25 | IGNORE |
| `wiki/concepts/expert-generalist.md` | durable-skills --supports--> this | 1 | 0.25 | IGNORE |
| `wiki/concepts/micro-productivity-trap.md` | automation-vs-augmentation --contradicts--> this | 1 | 0.25 | IGNORE |
| `wiki/sources/2026-03-20-huggingface-agentic-evaluations-workshop.md` | automation-vs-augmentation --supports--> this | 1 | 0.24 | IGNORE |
| `wiki/syntheses/ai-worker-maturity-levels.md` | durable-skills --supports--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | automation-vs-augmentation --supports--> this | 1 | 0.22 | IGNORE |
| `wiki/sources/2026-02-09-hubspot-customer-success-with-claude.md` | automation-vs-augmentation --supports--> this | 1 | 0.22 | IGNORE |
| `wiki/sources/2026-02-18-lyft-customer-support-with-claude.md` | automation-vs-augmentation --supports--> this | 1 | 0.21 | IGNORE |

**index.md / gap-expansion** (Step 5)
| Page | why added |
|------|-----------|
| — | F3 (AI inside HR processes) checked by grep on `wiki/index.md` for recruit / HR / CHRO / people analytics / onboarding: only incidental mentions, no page added. Reported as a gap in §7. |

## 3. Ignore policy applied
- `below-threshold` — graph-only neighbour with a low fused score that no facet needs
- `off-facet` — semantically adjacent but answers none of the three facets
- `redundant` — covers a claim already carried by a stronger USE page, which is named in the row
- Graph-only candidates needed a higher bar: three were admitted on content (W4, W6, W7) and W1 as the central concept; the rest stayed out.
- `ai-deskilling` came in through a `contradicts` edge, which the policy treats as a strong USE signal; it was ignored because the edge marks two measurement frames of one question, not conflicting claims.

## 4. Information ignored
| Page | reason-class | one-line reason |
|------|--------------|-----------------|
| `wiki/sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening.md` | redundant | NL occupational-exposure scoring; its finding is summarised in W1 §The Netherlands sectoral vantage, and it scores exposure rather than talent practice |
| `wiki/sources/2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services.md` | redundant | the diamond talent model and the entry-level rung are carried by W3 and W5, which both cite it |
| `wiki/sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs.md` | redundant | its layoff anchor and critical-thinking demand are distilled in W1 and W2 |
| `wiki/sources/2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai.md` | off-facet | efficiency as quality per unit time: work measurement, not talent or HR |
| `wiki/sources/2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai.md` | redundant | career advice to students; its skills points are covered by W2 and W5 |
| `wiki/sources/2026-06-25-carroll-stanford-gsb-making-organizational-culture-great.md` | redundant | its hiring finding is used through W1 §AI reshapes hiring at the job-definition layer |
| `wiki/concepts/automation-vs-augmentation.md` | redundant | substitute-vs-complement framing is carried by W1 and W3 |
| `wiki/sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai.md` | redundant | observed-exposure measure summarised in W1 |
| `wiki/sources/2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces.md` | redundant | six-segment model and CEO warning used through W1 §Reshape ≫ replace |
| `wiki/sources/2026-04-28-brynjolfsson-canaries-coal-mine.md` | redundant | ADP entry-level finding used through W1 and updated by W3 |
| `wiki/sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company.md` | below-threshold | graph-only neighbour (2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening -supports->), fused 0.45; no facet needs it |
| `wiki/sources/2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity.md` | below-threshold | graph-only neighbour (2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening -supports->), fused 0.44; no facet needs it |
| `wiki/sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness.md` | below-threshold | graph-only neighbour (2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity -supports->), fused 0.43; no facet needs it |
| `wiki/sources/2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable.md` | below-threshold | graph-only neighbour (2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity -supports->), fused 0.43; no facet needs it |
| `wiki/sources/2026-08-10-miller-worklab-the-ai-shift-most-companies-didnt-see-coming.md` | redundant | its hiring criteria and agent org chart are referenced in W2 |
| `wiki/sources/2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs.md` | below-threshold | graph-only neighbour (2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity -contradicts->), fused 0.42; no facet needs it |
| `wiki/sources/2026-06-24-mckinsey-ai-supercharging-software-development.md` | below-threshold | graph-only neighbour (2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services -supports->), fused 0.41; no facet needs it |
| `wiki/sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage.md` | below-threshold | graph-only neighbour (2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services -supports->), fused 0.40; no facet needs it |
| `wiki/sources/2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over.md` | below-threshold | graph-only neighbour (2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services -supports->), fused 0.40; no facet needs it |
| `wiki/sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships.md` | below-threshold | graph-only neighbour (2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs -supports->), fused 0.39; no facet needs it |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | below-threshold | graph-only neighbour (2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs -supports->), fused 0.38; no facet needs it |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | below-threshold | graph-only neighbour (2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs -supports->), fused 0.38; no facet needs it |
| `wiki/sources/2026-04-30-ai-index-report-2026.md` | below-threshold | graph-only neighbour (2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs -supports->), fused 0.37; no facet needs it |
| `wiki/sources/2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era.md` | below-threshold | graph-only neighbour (2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs -supports->), fused 0.36; no facet needs it |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | below-threshold | graph-only neighbour (2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs -supports->), fused 0.36; no facet needs it |
| `wiki/sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going.md` | below-threshold | graph-only neighbour (2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs -contradicts->), fused 0.36; no facet needs it |
| `wiki/sources/2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care.md` | below-threshold | graph-only neighbour (2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs -supports->), fused 0.35; no facet needs it |
| `wiki/sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company.md` | below-threshold | graph-only neighbour (2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs -supports->), fused 0.34; no facet needs it |
| `wiki/sources/2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset.md` | redundant | mindset-not-skillset used through W2 |
| `wiki/sources/2026-06-22-bbc-what-if-were-wrong-about-ai-layoffs.md` | redundant | AI-washing attribution confound is noted in W1 |
| `wiki/sources/2026-06-01-lf-state-of-tech-talent-europe-2026.md` | redundant | its −3% entry-level finding is used through W1 and W2; W4 is the parent report |
| `wiki/sources/2026-04-28-reitz-higgins-spacious-thinking.md` | below-threshold | graph-only neighbour (2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai -supports->), fused 0.33; no facet needs it |
| `wiki/sources/2026-05-02-dutt-chatterji-ai-experimentation-to-transformation.md` | below-threshold | graph-only neighbour (2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai -supports->), fused 0.33; no facet needs it |
| `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | redundant | developer core skills; the upskilling point is carried by W2 and W4 |
| `wiki/sources/2026-05-02-schoening-lennys-podcast-cultivating-agency-ai-era.md` | below-threshold | graph-only neighbour (2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai -supports->), fused 0.32; no facet needs it |
| `wiki/sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai.md` | below-threshold | graph-only neighbour (2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai -supports->), fused 0.32; no facet needs it |
| `wiki/sources/2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai.md` | below-threshold | graph-only neighbour (2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai -supports->), fused 0.31; no facet needs it |
| `wiki/sources/2026-09-18-reuters-on-assignment-inside-chinas-ai-race.md` | below-threshold | graph-only neighbour (2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai -supports->), fused 0.31; no facet needs it |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | below-threshold | graph-only neighbour (2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero -supports->), fused 0.30; no facet needs it |
| `wiki/sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation.md` | below-threshold | graph-only neighbour (2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero -supports->), fused 0.30; no facet needs it |
| `wiki/sources/2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook.md` | below-threshold | graph-only neighbour (2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero -supports->), fused 0.30; no facet needs it |
| `wiki/sources/2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook.md` | below-threshold | graph-only neighbour (2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero -supports->), fused 0.30; no facet needs it |
| `wiki/sources/2025-01-08-khanfar-factors-influencing-ai-adoption-slr.md` | below-threshold | graph-only neighbour (2025-06-09-krakowski-human-centered-ai-field-experiment -supports->), fused 0.29; no facet needs it |
| `wiki/sources/2026-04-28-anand-wu-genai-playbook.md` | below-threshold | graph-only neighbour (2025-06-09-krakowski-human-centered-ai-field-experiment -supports->), fused 0.29; no facet needs it |
| `wiki/sources/2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work.md` | below-threshold | graph-only neighbour (2025-06-09-krakowski-human-centered-ai-field-experiment -supports->), fused 0.29; no facet needs it |
| `wiki/sources/2026-04-28-dellacqua-jagged-technological-frontier.md` | below-threshold | graph-only neighbour (2025-06-09-krakowski-human-centered-ai-field-experiment -supports->), fused 0.28; no facet needs it |
| `wiki/sources/2026-07-01-bello-mckinsey-podcast-serial-builder-advantage.md` | below-threshold | graph-only neighbour (2026-06-25-carroll-stanford-gsb-making-organizational-culture-great -supports->), fused 0.28; no facet needs it |
| `wiki/sources/2026-07-07-sinofsky-amble-a16z-software-in-the-age-of-agents.md` | below-threshold | graph-only neighbour (2026-06-25-carroll-stanford-gsb-making-organizational-culture-great -supports->), fused 0.28; no facet needs it |
| `wiki/concepts/ai-benchmarks.md` | below-threshold | graph-only neighbour (durable-skills -depends-on->), fused 0.28; no facet needs it |
| `wiki/sources/2026-08-16-hill-bloomberg-leaders-ceo-skills-age-of-ai.md` | off-facet | CEO leadership skills, not workforce talent management |
| `wiki/sources/2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs.md` | below-threshold | graph-only neighbour (durable-skills -supports->), fused 0.26; no facet needs it |
| `wiki/concepts/enterprise-ai-adoption.md` | below-threshold | graph-only neighbour (automation-vs-augmentation -supports->), fused 0.26; no facet needs it |
| `wiki/sources/2026-05-06-mit-ocw-future-of-mit-open-education.md` | below-threshold | graph-only neighbour (durable-skills -supports->), fused 0.26; no facet needs it |
| `wiki/concepts/jagged-frontier.md` | below-threshold | graph-only neighbour (automation-vs-augmentation -supports->), fused 0.26; no facet needs it |
| `wiki/sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era.md` | below-threshold | graph-only neighbour (durable-skills -supports->), fused 0.26; no facet needs it |
| `wiki/concepts/ai-deskilling.md` | redundant | contradicts-edge to durable-skills is two measurement frames of one question, not conflicting claims; the apprenticeship mechanism is carried by W5 and W3 |
| `wiki/concepts/ai-coding-productivity-evidence.md` | below-threshold | graph-only neighbour (automation-vs-augmentation -part-of->), fused 0.25; no facet needs it |
| `wiki/concepts/expert-generalist.md` | below-threshold | graph-only neighbour (durable-skills -supports->), fused 0.25; no facet needs it |
| `wiki/concepts/micro-productivity-trap.md` | below-threshold | graph-only neighbour (automation-vs-augmentation -contradicts->), fused 0.25; no facet needs it |
| `wiki/sources/2026-03-20-huggingface-agentic-evaluations-workshop.md` | below-threshold | graph-only neighbour (automation-vs-augmentation -supports->), fused 0.24; no facet needs it |
| `wiki/syntheses/ai-worker-maturity-levels.md` | off-facet | classifies an individual's AI-use maturity, not organisational talent practice |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | below-threshold | graph-only neighbour (automation-vs-augmentation -supports->), fused 0.22; no facet needs it |
| `wiki/sources/2026-02-09-hubspot-customer-success-with-claude.md` | below-threshold | graph-only neighbour (automation-vs-augmentation -supports->), fused 0.22; no facet needs it |
| `wiki/sources/2026-02-18-lyft-customer-support-with-claude.md` | below-threshold | graph-only neighbour (automation-vs-augmentation -supports->), fused 0.21; no facet needs it |

## 5. Information used
| Page | type | effConf | contribution |
|------|------|---------|--------------|
| [W1] `wiki/concepts/ai-employment-effects.md` | concept | 0.889 | reshape ≫ replace (BCG), entry-level pressure (LF Europe), CEO warning, hiring at the job-definition layer (Carroll) |
| [W2] `wiki/concepts/durable-skills.md` | concept | 0.804 | definition of durable skills; 2× human-skills demand; evaluation as terminal skill; upskilling over hiring; mindset not skillset |
| [W3] `wiki/sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity.md` | source | — | ADP 13%→16–17% entry-level decline; pyramid→diamond; don't fire top experts; design problem; mavericks; fleet of agents |
| [W4] `wiki/sources/2026-05-01-lf-state-of-tech-talent-global-2026.md` | source | 0.75 | net hiring +26%/+31%; upskilling 57%/94%, 3.5× vs hiring; training 93% vs pay 91%; certifications 76%; interest caveat |
| [W5] `wiki/sources/2026-07-22-brown-wef-meet-the-leader-entry-level-jobs-in-an-ai-era.md` | source | — | 2× human-skills demand; 7× seniorized skills; 25% more juniors; 81% vs 34% applied experience vs degrees; PwC entry routes 17–18→5 |
| [W6] `wiki/sources/2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026.md` | source | — | three organisational shifts (design not command, capability not category, develop people); 5 C's; onlyness |
| [W7] `wiki/sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees.md` | source | 0.85 | AI-as-employee framing: −9pp accountability, +44% escalation, −18% errors caught, +13% role uncertainty, no adoption gain |
| [W8] `wiki/sources/2025-06-09-krakowski-human-centered-ai-field-experiment.md` | source | 0.85 | untailored AI underperforms legacy IT; tailored interaction raises use and performance; work procedure the main lever |
| [W9] `wiki/sources/2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero.md` | source | — | customer service ~100→18 mostly via natural attrition; 'every office job behind a screen disappears' |

## 6. Answer-element map
| Anchor | Answer element (claim) | Wiki page(s) | Section / span used |
|--------|------------------------|--------------|---------------------|
| [W1] | reshape ≫ replace (50–55% reshaped, 10–15% vulnerable); LF Europe −3% entry-level; BCG warning on cutting beyond AI's reach; hiring changes at job definition and applicant pool, AI-written applications homogenise | [[concepts/ai-employment-effects|ai-employment-effects]] | ## Working definition; ## The Linux Foundation not-a-jobs-crisis…; ## Reshape ≫ replace…; ## AI reshapes hiring at the job-definition layer… |
| [W2] | definition of durable skills; 2× demand growth for human skills; evaluation of agent fleets; new hires 53% slower to productivity, 23% leave within six months; mindset not skillset (Argenti) | [[concepts/durable-skills|durable-skills]] | ## Working definition; ## Human skills growing twice as fast…; ## Upskilling over hiring…; ## The mindset-not-skillset inversion |
| [W3] | ADP: young workers in most-exposed jobs −13% then −16/17%; pyramid→diamond; firing top experts is short-sighted; 'a design problem', 'a little lazy'; mavericks; fleet of agents | [[sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity|2026-08-01-brynjolfsson-mckinsey-talks-talent-bi]] | ## TL;DR items 5, 9, 10, 12, 13, 14 |
| [W4] | net tech hiring +26%/+31%; upskilling 57%, 94%, 3.5× vs hiring; certifications 76%; training 93% vs pay 91%; publisher sells training | [[sources/2026-05-01-lf-state-of-tech-talent-global-2026|2026-05-01-lf-state-of-tech-talent-global-2026]] | ## TL;DR; ## Source-quality flag |
| [W5] | 'not yet backed up by data'; employer hiring 25% more juniors; 2× human-skills demand; 7× seniorized skills, 'not by osmosis'; 81% vs 34%; PwC routes 17–18→5; report not ingested | [[sources/2026-07-22-brown-wef-meet-the-leader-entry-level-jobs-in-an-ai-era|2026-07-22-brown-wef-meet-the-leader-entry-level]] | ## TL;DR items 3–6, 8; relationships: contradicts W3 |
| [W6] | three organisational shifts; 5 C's; identity not tied to job title | [[sources/2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026|2026-06-29-raman-wood-worklab-job-titles-dont-ma]] | ## TL;DR items 3–5 |
| [W7] | RCT N=1,261 HR/finance managers: −9pp accountability, +44% escalation, −18% errors caught, +13% role uncertainty, no adoption gain | [[sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees|2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-li]] | headline finding paragraph |
| [W8] | untailored AI underperformed legacy IT; tailored procedure/authority/training/incentives raised use and performance; procedure the main lever | [[sources/2025-06-09-krakowski-human-centered-ai-field-experiment|2025-06-09-krakowski-human-centered-ai-field-exp]] | ## TL;DR items 1, 2, 4, 6 |
| [W9] | HelloPrint customer service ~100→18, mostly natural attrition; every office job behind a screen disappears | [[sources/2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero|2026-05-27-scheffer-de-ondernemer-helloprint-ai-]] | ## TL;DR items 1, 5; title |

## 7. Final answer

**Kort:** de wiki behandelt HR en talentmanagement vooral via twee vragen. Wat doet AI met werk en vaardigheden? En hoe moeten organisaties daarop inspelen bij werving, ontwikkeling en functieontwerp? Over AI *binnen* HR-processen zelf (wervingssoftware, people analytics, beoordeling) staat er weinig.

**1. Werk verandert vaker dan het verdwijnt, en de druk zit bij instromers.**
- Over meerdere methoden heen is de rode draad dat banen eerder veranderen dan verdwijnen. BCG schat dat 50–55% van de Amerikaanse banen binnen 2–3 jaar ingrijpend verandert, en dat 10–15% over 4–5 jaar kan verdwijnen [W1].
- Starters merken het eerst. Brynjolfsson ziet in loongegevens van ADP dat de werkgelegenheid van jonge werknemers in de meest blootgestelde beroepen eerst met ~13% daalde en nu met *"up to 16 or 17%"* [W3]. De Linux Foundation meldt een netto groei van tech-banen (wereldwijd +26% in 2025 en +31% in 2026). In Europa krimpen de instroomfuncties in tech echter met 3% [W4][W1].
- Hierover is de wiki niet eensgezind. Peter Brown (PwC, WEF) zegt dat *"the most dire headlines about entry-level jobs are not yet backed up by data"*. Hij noemt een werkgever die juist 25% meer junioren aanneemt, om later genoeg leidinggevenden te hebben [W5]. De wiki legt dit vast als expliciete tegenspraak met Brynjolfsson. Het verschil zit in het soort bewijs: wat werkgevers zeggen van plan te zijn, tegenover wat de loonadministratie laat zien. Het zit ook in de reikwijdte: alle startersbanen, of alleen de meest blootgestelde beroepen [W3][W5].
- Een Nederlands voorbeeld: bij HelloPrint ging de klantenservice van ongeveer 100 naar 18 mensen, grotendeels via natuurlijk verloop. Oprichter Scheffer verwacht dat elke kantoorbaan achter een scherm verdwijnt [W9]. Het gaat om één bedrijf en om zijn eigen woorden.

**2. Het talentprobleem: de piramide wordt een diamant.**
- Als de instroom krimpt, droogt de aanvoer van middenkader en senioren op. Brynjolfsson: *"where are those middle managers, middle-skill people going to come from"* [W3].
- Werkgevers vragen van starters zeven keer zoveel *seniorized* vaardigheden: vaardigheden die vroeger in de eerste drie à vier jaar groeiden. Brown: *"It's not going to happen by osmosis."* Het leren in de praktijk moet dus bewust opnieuw worden ingericht [W5].
- BCG waarschuwt dat wie verder in personeel snijdt dan AI kan opvangen, kennis en sleuteltalent kwijtraakt [W1]. Brynjolfsson voegt toe dat de beste vakmensen juist meer waard worden, omdat hun kennis het systeem voedt. Hen ontslaan omdat minder ervaren mensen met AI bijna even goed presteren, noemt hij *"a very short-sighted approach"* [W3].

**3. Welke vaardigheden tellen.**
- De wiki noemt vaardigheden *duurzaam* als ze niet in vaste regels te vangen zijn, afhangen van context en mensen, en langzaam verouderen [W2]. In sectoren waar AI veel werk raakt, groeit de vraag naar menselijke vaardigheden twee keer zo snel: oordeelsvermogen, problemen oplossen, kritisch denken en relaties opbouwen. De aanbevolen combinatie is vakkennis, handigheid met AI en menselijke vaardigheden [W5][W2].
- Brynjolfsson verwacht dat bijna iedereen een *"fleet of agents"* gaat aansturen. Wie goed richting geeft en het werk vooral goed beoordeelt, gaat het best doen [W3][W2].
- Raman (LinkedIn) noemt vijf vaardigheden die je kunt trainen: creativiteit, nieuwsgierigheid, moed, compassie en communicatie. Iemands beroepsidentiteit hangt volgens hem niet meer aan een functietitel [W6]. Argenti (CIO van Goldman Sachs) gaat verder: verdedig geen lijst vaardigheden, maar verander je mindset en je gewoonten [W2].

**4. Wat HR concreet kan doen.**
- **Opleiden in plaats van aannemen.** In de enquête van de Linux Foundation (400 deelnemers) is bijscholing de eerste reactie op tekorten (57%), en 94% vindt bijscholing belangrijk. Organisaties kiezen 3,5 keer vaker voor opleiden dan voor aannemen [W4]. Nieuwe medewerkers doen 53% langer over volledige productiviteit, en 23% vertrekt binnen zes maanden [W2]. Kanttekening: de uitgever verkoopt zelf trainingen en certificaten [W4].
- **Vaardigheden tellen zwaarder dan diploma's.** 81% van de werkgevers geeft voorrang aan praktijkervaring, 34% aan diploma's. PwC bracht het aantal instroomroutes terug van zo'n 17 à 18 naar ongeveer vijf en werft op potentieel en vaardigheden [W5]. Voor 76% van de wervende managers zijn certificaten belangrijk. Als manier om mensen te behouden scoort training (93%) hoger dan salaris (91%) [W4].
- **Werk en functies opnieuw ontwerpen, niet AI eroverheen leggen.** Raman noemt drie verschuivingen: leiden door ontwerp in plaats van bevel, mensen beoordelen op wat ze kunnen in plaats van op hun functiecategorie, en mensen ontwikkelen in plaats van taken bewaken [W6]. Brynjolfsson noemt het *"a design problem"*. Alleen meten hoeveel minder mensen nodig zijn, noemt hij *"a little lazy"*. Organisaties moeten weten wie hun *mavericks* zijn en hen bewust inzetten [W3].
- **AI afstemmen op de medewerker.** In een veldexperiment met 72 verkopers (gepubliceerd in Management Science) presteerde AI die niet was afgestemd op de werkstijl slechter dan het oude systeem. De afgestemde versie, met aangepaste werkwijze, beslisruimte, training en beloning, werd steeds meer gebruikt en presteerde beter. De werkwijze bleek de belangrijkste knop [W8].

**5. AI in het HR-proces zelf: hier is de wiki dun.**
- **Werving.** De echte verandering zit volgens Carroll (die onderzoek van Fernández-Mateo aanhaalt) niet in de selectie. Ze zit in hoe functies worden omschreven en hoe de groep sollicitanten ontstaat. Sollicitaties die met AI zijn geschreven gaan steeds meer op elkaar lijken, en dat maakt selecteren moeilijker. Dit is tweedehands en niet gemeten [W1].
- **Agents als collega's.** In een experiment met 1.261 HR- en financemanagers leidde het presenteren van AI als collega tot 9 procentpunt minder eigen verantwoordelijkheid, 44% meer escalaties, 18% minder gevonden fouten en 13% meer onzekerheid over de eigen rol. Het leverde geen extra gebruik op [W7].
- **Wat ontbreekt.** De wiki heeft geen bron over wervingssoftware, people analytics of AI in beoordelingsgesprekken. Dat is een gat in de wiki, geen bevinding over de praktijk.

**Hoe stevig is dit?** Het sterkst zijn de loongegevens van Brynjolfsson en het experiment in Management Science [W3][W8]. Veel ander bewijs komt uit interviews en enquêtes van partijen met een eigen belang. Het onderliggende PwC-rapport zit niet zelf in de wiki, en de Linux Foundation verkoopt trainingen [W5][W4].

## 8. Trace artifact
Machine-readable provenance: [`2026-10-04-hr-talent-management-ai-query-trace.json`](2026-10-04-hr-talent-management-ai-query-trace.json)
