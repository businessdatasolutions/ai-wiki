---
type: query-trace
question: "Zoek in de AI-wiki materiaal dat past bij het hoorcollege Informatiemanagement (8481) gezien de doelen en leeruitkomsten, en laat zien welk 'oude' denken nog waarde heeft met AI en van welk denken we volgens experts afscheid moeten nemen."
date: 2026-09-02
language: nl
trace: "im-hoorcollege-oud-denken-ai-query-trace.json"
pages_used: 26
pages_ignored: 133
related_output: "/Users/witoldtenhove/Documents/HAN/C-CLUSTER/NIEUW-2026-27/IM/houdbaarheidsonderzoek-informatiemanagement.html"
---

# Query trace — IM-hoorcollege: welk oud denken houdt stand met AI

## 1. Question
- **Original:** Zoek in de AI-wiki materiaal dat past bij het hoorcollege Informatiemanagement (8481) gezien de doelen en leeruitkomsten, en laat zien welk 'oude' denken nog waarde heeft met AI en van welk denken we volgens experts afscheid moeten nemen.
- **Restated:** Welke klassieke IM-modellen uit de syllabus (ITIL, TOGAF, Zachman, Henderson & Venkatraman, Maes, Porter, Laudon, Davenport, Kaplan & Norton, Markus, Davis, Venkatesh) houden volgens de 2025-2026-bronnen in de wiki stand nu AI mee-beslist, welke verschuiven, welke moeten weg — en welk wiki-materiaal kan het college dragen?
- **Facets:** 1) F1 alignment en negenvlak (criterium 5/6) 2) F2 architectuur, governance, centraal/decentraal, run/change (criterium 5/7) 3) F3 data, analytics en besluitvorming (criterium 8) 4) F4 implementatie en adoptie (criterium 9) 5) F5 ethiek en recht (criterium 9, gap-check)

Vijf facetten in plaats van 2–4, omdat de vraag een heel curriculum bestrijkt (de vijf IM-criteria van toetsmatrijs 6). Daarom vijf retrievals in plaats van één, en een USE-set van 26 pagina's — ruim boven de gebruikelijke 4–8, bewust: circa vijf per facet.

## 2. Paths explored

**Retrievals** (`node scripts/wiki-retrieve.mjs --json -n 12`)

| facet | qmd hits | kandidaten |
|---|---|---|
| F1 alignment en negenvlak | 10 | 75 |
| F2 architectuur en governance | 12 | 78 |
| F3 data, analytics en besluitvorming | 11 | 68 |
| F4 implementatie en adoptie | 12 | 80 |
| F5 ethiek en recht (gap-check) | 10 | 60 |

Samen 361 kandidaatregels, 159 unieke pagina's.

**qmd hits** (relevance stream)
| Page | type | qmd score | fused | verdict |
|---|---|---|---|---|
| `wiki/concepts/responsible-ai.md` | concept | 0.98 | 0.98 | USE |
| `wiki/concepts/enterprise-ai-adoption.md` | concept | 0.38 | 0.964 | USE |
| `wiki/concepts/ai-agents.md` | concept | 0.62 | 0.964 | USE |
| `wiki/sources/2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero.md` | source | 0.75 | 0.94 | USE |
| `wiki/concepts/durable-skills.md` | concept | 0.17 | 0.934 | IGNORE |
| `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | synthesis | 0.55 | 0.93 | USE |
| `wiki/sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company.md` | source | 0.62 | 0.925 | USE |
| `wiki/sources/2026-04-28-anand-wu-genai-playbook.md` | source | 0.62 | 0.925 | USE |
| `wiki/sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity.md` | source | 0.32 | 0.91 | USE |
| `wiki/sources/2026-04-30-ai-index-report-2026.md` | source | 0.25 | 0.91 | IGNORE |
| `wiki/concepts/ai-employment-effects.md` | concept | 0.12 | 0.906 | IGNORE |
| `wiki/sources/2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler.md` | source | 0.75 | 0.9 | USE |
| `wiki/sources/2026-08-19-rohrer-goto-modern-enterprise-architecture-architecting-for-outcomes.md` | source | 0.61 | 0.896 | USE |
| `wiki/sources/2026-01-22-imda-model-ai-governance-framework-for-agentic-ai.md` | source | 0.16 | 0.896 | USE |
| `wiki/sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening.md` | source | 0.17 | 0.882 | USE |
| `wiki/sources/2026-06-17-priest-atlantic-pwc-ai-agents-changing-business.md` | source | 0.61 | 0.882 | USE |
| `wiki/sources/2026-04-28-ai-index-report-2025.md` | source | 0.15 | 0.882 | IGNORE |
| `wiki/concepts/strategy.md` | concept | 0.39 | 0.874 | IGNORE |
| `wiki/sources/2026-06-12-aws-leaders-guide-data-strategy-agentic-ai.md` | source | 0.36 | 0.869 | USE |
| `wiki/sources/2026-04-28-mit-sloan-ai-maturity.md` | source | 0.39 | 0.869 | USE |
| `wiki/sources/2026-06-11-mit-smr-agentic-ai-what-leaders-wish-they-knew-sooner.md` | source | 0.34 | 0.856 | USE |
| `wiki/sources/2026-04-28-mittri-cisco-ai-enabled-enterprise.md` | source | 0.53 | 0.856 | IGNORE |
| `wiki/sources/2026-05-11-blank-mit-6s191-three-laws-of-ai.md` | source | 0.09 | 0.856 | IGNORE |
| `wiki/sources/2026-08-10-miller-worklab-the-ai-shift-most-companies-didnt-see-coming.md` | source | 0.38 | 0.843 | IGNORE |
| `wiki/sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage.md` | source | 0.34 | 0.843 | IGNORE |
| `wiki/sources/2026-07-10-when-ai-becomes-common-organizational-capability-becomes-the-advantage-ep-16.md` | source | 0.44 | 0.839 | USE |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | source | 0.1 | 0.838 | IGNORE |
| `wiki/sources/2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world.md` | source | 0.43 | 0.831 | IGNORE |
| `wiki/sources/2026-04-28-werner-lebrun-octopus-organization.md` | source | 0.32 | 0.831 | USE |
| `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` | source | 0.32 | 0.819 | IGNORE |
| `wiki/sources/2026-08-16-hill-bloomberg-leaders-ceo-skills-age-of-ai.md` | source | 0.04 | 0.819 | IGNORE |
| `wiki/threads/organizational-frameworks-for-ai-adoption.md` | thread | 0.47 | 0.813 | IGNORE |
| `wiki/sources/2026-05-02-dutt-chatterji-ai-experimentation-to-transformation.md` | source | 0.19 | 0.808 | USE |
| `wiki/sources/2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai.md` | source | 0.3 | 0.808 | IGNORE |
| `wiki/sources/2026-05-07-kiron-schrage-compound-benefits.md` | source | 0.2 | 0.802 | IGNORE |
| `wiki/sources/2026-06-01-lf-state-of-tech-talent-europe-2026.md` | source | 0.06 | 0.796 | IGNORE |
| `wiki/concepts/industrial-ai-agents.md` | concept | 0.42 | 0.784 | IGNORE |

**graph neighbours** (typed-edge stream, hops 1)
| Page | type | qmd | fused | verdict |
|---|---|---|---|---|
| `wiki/sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships.md` | source | — | 0.47 | IGNORE |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | source | — | 0.462 | IGNORE |
| `wiki/sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation.md` | source | — | 0.455 | IGNORE |
| `wiki/concepts/agent-oversight-and-delegation.md` | concept | — | 0.455 | USE |
| `wiki/sources/2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm.md` | source | — | 0.448 | IGNORE |
| `wiki/sources/2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook.md` | source | — | 0.448 | IGNORE |
| `wiki/sources/2025-07-31-wang-agentspec-runtime-enforcement-llm-agents.md` | source | — | 0.448 | IGNORE |
| `wiki/concepts/automation-vs-augmentation.md` | concept | — | 0.447 | USE |
| `wiki/sources/2026-05-08-running-an-ai-native-engineering-org.md` | source | — | 0.445 | IGNORE |
| `wiki/sources/2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook.md` | source | — | 0.441 | IGNORE |
| `wiki/concepts/agent-harness.md` | concept | — | 0.435 | IGNORE |
| `wiki/sources/2026-06-17-ng-langchain-interrupt-future-of-ai-agents.md` | source | — | 0.434 | IGNORE |
| `wiki/sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs.md` | source | — | 0.434 | IGNORE |
| `wiki/concepts/jagged-frontier.md` | concept | — | 0.434 | USE |
| `wiki/concepts/micro-productivity-trap.md` | concept | — | 0.429 | USE |
| `wiki/sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company.md` | source | — | 0.428 | IGNORE |
| `wiki/concepts/dynamic-capabilities.md` | concept | — | 0.423 | IGNORE |
| `wiki/sources/2026-06-18-dumra-mit-smr-dbs-everyone-an-innovator.md` | source | — | 0.422 | IGNORE |
| `wiki/concepts/agent-development-lifecycle.md` | concept | — | 0.422 | IGNORE |
| `wiki/sources/2025-06-09-krakowski-human-centered-ai-field-experiment.md` | source | — | 0.422 | IGNORE |
| `wiki/entities/BBC.md` | entity | — | 0.413 | IGNORE |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | source | — | 0.41 | IGNORE |
| `wiki/sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai.md` | source | — | 0.41 | IGNORE |
| `wiki/concepts/foundation-models.md` | concept | — | 0.408 | IGNORE |
| `wiki/sources/2026-07-20-bbc-researchers-studied-ai-layoffs-heres-their-warning.md` | source | — | 0.404 | IGNORE |
| `wiki/sources/2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services.md` | source | — | 0.398 | IGNORE |
| `wiki/sources/2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity.md` | source | — | 0.393 | IGNORE |
| `wiki/sources/2026-05-01-lf-state-of-tech-talent-global-2026.md` | source | — | 0.392 | IGNORE |
| `wiki/concepts/open-source-ai.md` | concept | — | 0.391 | IGNORE |
| `wiki/entities/MIT-Sloan-CIO-Symposium.md` | entity | — | 0.389 | IGNORE |
| `wiki/sources/2026-07-22-brown-wef-meet-the-leader-entry-level-jobs-in-an-ai-era.md` | source | — | 0.382 | IGNORE |
| `wiki/sources/2026-05-12-techlatest-hacker-search-engines-osint-tools-2026.md` | source | — | 0.382 | IGNORE |
| `wiki/sources/2026-05-28-from-event-to-ecosystem-rethinking-how-technology-leaders-build-knowledge-in-the-ai-era.md` | source | — | 0.378 | IGNORE |
| `wiki/sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness.md` | source | — | 0.377 | IGNORE |
| `wiki/concepts/multi-agent-failure-modes.md` | concept | — | 0.375 | IGNORE |
| `wiki/entities/Allan-Tate.md` | entity | — | 0.373 | IGNORE |
| `wiki/sources/2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable.md` | source | — | 0.372 | IGNORE |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | source | — | 0.372 | IGNORE |
| `wiki/concepts/systems-thinking.md` | concept | — | 0.371 | IGNORE |
| `wiki/concepts/strategic-foresight.md` | concept | — | 0.371 | IGNORE |
| `wiki/sources/2026-05-06-mit-ocw-future-of-mit-open-education.md` | source | — | 0.368 | IGNORE |
| `wiki/entities/Irving-Wladawsky-Berger.md` | entity | — | 0.368 | IGNORE |
| `wiki/concepts/document-intelligence.md` | concept | — | 0.366 | IGNORE |
| `wiki/sources/2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china.md` | source | — | 0.363 | IGNORE |
| `wiki/sources/2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas.md` | source | — | 0.358 | IGNORE |
| `wiki/concepts/ai-benchmarks.md` | concept | — | 0.353 | IGNORE |
| `wiki/sources/2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells.md` | source | — | 0.35 | IGNORE |
| `wiki/sources/2025-07-02-joshi-venkatraman-fowler-expert-generalists.md` | source | — | 0.345 | IGNORE |
| `wiki/sources/2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs.md` | source | — | 0.341 | IGNORE |
| `wiki/sources/2026-08-14-blomfield-yc-building-structuring-ai-native-company.md` | source | — | 0.341 | IGNORE |
| `wiki/sources/2025-10-05-patwardhan-et-al-openai-gdpval.md` | source | — | 0.341 | IGNORE |
| `wiki/concepts/ai-knowledge-hiding.md` | concept | — | 0.337 | IGNORE |
| `wiki/sources/2026-04-28-dellacqua-jagged-technological-frontier.md` | source | — | 0.337 | IGNORE |
| `wiki/sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees.md` | source | — | 0.333 | IGNORE |
| `wiki/sources/2026-01-09-baron-signals-for-2026.md` | source | — | 0.333 | IGNORE |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | source | — | 0.331 | IGNORE |
| `wiki/sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era.md` | source | — | 0.33 | IGNORE |
| `wiki/concepts/industry-4-0.md` | concept | — | 0.33 | IGNORE |
| `wiki/sources/2026-07-10-building-the-future-of-agentic-infrastructure.md` | source | — | 0.33 | IGNORE |
| `wiki/sources/2026-04-07-loukides-radar-trends-april-2026.md` | source | — | 0.33 | IGNORE |
| `wiki/concepts/ai-deskilling.md` | concept | — | 0.327 | USE |
| `wiki/sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai.md` | source | — | 0.326 | IGNORE |
| `wiki/concepts/founder-led-sales.md` | concept | — | 0.326 | IGNORE |
| `wiki/syntheses/harness-thinning-what-persists.md` | synthesis | — | 0.326 | IGNORE |
| `wiki/sources/2026-07-14-khan-academy-ceo-the-real-ai-opportunity-is-in-boring-industries-sal-khan.md` | source | — | 0.326 | IGNORE |
| `wiki/sources/2026-05-05-loukides-radar-trends-may-2026.md` | source | — | 0.326 | IGNORE |
| `wiki/concepts/expert-generalist.md` | concept | — | 0.325 | IGNORE |
| `wiki/sources/2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces.md` | source | — | 0.322 | IGNORE |
| `wiki/sources/2026-05-20-agrawal-stanford-mse435-economics-of-generative-ai.md` | source | — | 0.322 | IGNORE |
| `wiki/sources/2026-04-28-brynjolfsson-canaries-coal-mine.md` | source | — | 0.319 | IGNORE |
| `wiki/sources/2026-05-21-jones-stanford-gsb-ai-and-our-economic-future.md` | source | — | 0.319 | IGNORE |
| `wiki/sources/2026-05-21-neven-manyika-google-io-quantum-ai-future.md` | source | — | 0.315 | IGNORE |
| `wiki/concepts/generative-ai.md` | concept | — | 0.313 | IGNORE |
| `wiki/concepts/react-reasoning-acting.md` | concept | — | 0.312 | IGNORE |
| `wiki/sources/2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report.md` | source | — | 0.312 | IGNORE |
| `wiki/sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going.md` | source | — | 0.305 | IGNORE |
| `wiki/sources/2026-05-14-pochampally-assistant-or-actor-delegation-regret.md` | source | — | 0.302 | IGNORE |
| `wiki/concepts/agentic-engineering.md` | concept | — | 0.302 | IGNORE |
| `wiki/sources/2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot.md` | source | — | 0.299 | IGNORE |
| `wiki/sources/2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers.md` | source | — | 0.293 | IGNORE |
| `wiki/sources/2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset.md` | source | — | 0.29 | IGNORE |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | source | — | 0.287 | IGNORE |
| `wiki/sources/2025-12-02-allen-brozovich-davis-aws-reinvent-advanced-team-structures.md` | source | — | 0.286 | IGNORE |
| `wiki/concepts/ai-washing.md` | concept | — | 0.284 | IGNORE |
| `wiki/sources/2026-04-28-anthropic-economic-index-q4-2025.md` | source | — | 0.284 | IGNORE |
| `wiki/sources/2026-06-03-chopra-headroom-context-optimization-layer-for-llm-applications.md` | source | — | 0.28 | IGNORE |
| `wiki/sources/2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering.md` | source | — | 0.278 | IGNORE |
| `wiki/sources/2026-06-10-anicich-brouwers-why-employees-arent-transparent-ai-usage.md` | source | — | 0.278 | IGNORE |
| `wiki/sources/2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering.md` | source | — | 0.276 | IGNORE |
| `wiki/sources/2026-07-09-nyc-executive-forum-2026-a-leaders-guide-to-agentic-ai.md` | source | — | 0.273 | IGNORE |
| `wiki/sources/2026-05-03-rewired-second-edition-sample.md` | source | — | 0.273 | IGNORE |
| `wiki/sources/2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era.md` | source | — | 0.27 | IGNORE |
| `wiki/entities/MIT-Sloan-Management-Review.md` | entity | — | 0.268 | IGNORE |
| `wiki/sources/2026-08-10-banholzer-laberge-mckinsey-how-to-maximize-competitive-advantage.md` | source | — | 0.268 | IGNORE |
| `wiki/sources/2022-02-23-oberholzer-gee-hbr-what-is-strategy-value-stick.md` | source | — | 0.268 | IGNORE |
| `wiki/sources/2022-06-29-martin-hbr-a-plan-is-not-a-strategy.md` | source | — | 0.265 | IGNORE |
| `wiki/sources/2026-02-09-ross-schneider-adaptability.md` | source | — | 0.265 | IGNORE |
| `wiki/sources/2026-07-01-mcgrath-power-of-strategic-centering.md` | source | — | 0.263 | IGNORE |
| `wiki/sources/2026-06-25-carroll-stanford-gsb-making-organizational-culture-great.md` | source | — | 0.263 | IGNORE |
| `wiki/entities/McKinsey-&-Company.md` | entity | — | 0.261 | IGNORE |
| `wiki/sources/2026-07-24-turnbaugh-motherduck-context-layers-explained.md` | source | — | 0.256 | IGNORE |
| `wiki/entities/Microsoft.md` | entity | — | 0.253 | IGNORE |
| `wiki/entities/Bloomberg-Podcasts.md` | entity | — | 0.253 | IGNORE |
| `wiki/entities/Linda-Hill.md` | entity | — | 0.251 | IGNORE |
| `wiki/sources/2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026.md` | source | — | 0.249 | IGNORE |
| `wiki/sources/2026-07-19-why-netflix-is-betting-on-systems-thinkers-not-specialists-in-the-ai-era.md` | source | — | 0.247 | IGNORE |
| `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | source | — | 0.246 | IGNORE |
| `wiki/sources/2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success.md` | source | — | 0.245 | IGNORE |
| `wiki/sources/2026-06-24-mckinsey-ai-supercharging-software-development.md` | source | — | 0.245 | IGNORE |
| `wiki/sources/2026-02-11-shyamsundar-jain-organizational-strategies-collective-wisdom-nature.md` | source | — | 0.245 | IGNORE |
| `wiki/sources/2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide.md` | source | — | 0.243 | IGNORE |
| `wiki/entities/David-Kiron.md` | entity | — | 0.238 | IGNORE |
| `wiki/sources/2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care.md` | source | — | 0.237 | IGNORE |
| `wiki/sources/2026-04-28-reitz-higgins-spacious-thinking.md` | source | — | 0.235 | IGNORE |
| `wiki/sources/2026-05-02-schoening-lennys-podcast-cultivating-agency-ai-era.md` | source | — | 0.228 | IGNORE |
| `wiki/entities/Sam-Ransbotham.md` | entity | — | 0.226 | IGNORE |
| `wiki/concepts/strategic-centering.md` | concept | — | 0.208 | IGNORE |
| `wiki/concepts/theory-based-view.md` | concept | — | 0.205 | IGNORE |
| `wiki/concepts/infinite-game.md` | concept | — | 0.199 | IGNORE |
| `wiki/syntheses/strategy-finite-vs-infinite-game.md` | synthesis | — | 0.192 | IGNORE |

**index.md / gap-expansion**
| Page | why added |
|---|---|
| `wiki/concepts/ai-deskilling.md` | index.md/ls: deskilling is de studentzijde van criterium 9 |
| `wiki/entities/Thomas H. Davenport.md` | index.md/ls: syllabusauteur |
| `wiki/entities/Erik Brynjolfsson.md` | index.md/ls: bron van het equalizing effect en de Canaries |
| `wiki/concepts/responsible-ai.md`, `wiki/sources/2026-01-22-imda-…md`, `wiki/concepts/agent-oversight-and-delegation.md` | vijfde retrieval voor criterium 9 (ethiek/recht), dat in de vier facetqueries niets opleverde |
| `wiki/concepts/automation-vs-augmentation.md`, `micro-productivity-trap.md`, `jagged-frontier.md` | graaf-buren van sterke hits, gepromoveerd omdat ze het facetantwoord dragen (ladder ↔ analyticsvormen; taak- vs firmaniveau; grillige grens) |

## 3. Ignore policy applied
- `below-threshold` — graaf-buur zonder zoekhit en zonder facetbijdrage (de lange staart).
- `redundant` — dekt dezelfde claim als een al gekozen, sterkere pagina; de gekozen pagina staat in de reden.
- `off-facet` — semantisch nabij (arbeidsmarkt, strategie, macro-economie, techniek) maar beantwoordt geen van de vijf facetten.
- `superseded` — gesloten thread waarvan de synthese de opvolger is.
- `wrong-granularity` — technisch runtime-mechanisme waar het facet de bedrijfskundige laag vraagt.
- `decayed` — niet gebruikt: de enige verouderde kandidaat (synthese, effConf 0,52 bij de eerste query) is uniek en daarom USE, met de verouderingsvlag in het verslag.

## 4. Information ignored
| Page | reason-class | one-line reason |
|---|---|---|
| `wiki/concepts/durable-skills.md` | off-facet | arbeidsmarktvaardigheden, niet informatiemanagement; raakpunt loopt via W6 |
| `wiki/sources/2026-04-30-ai-index-report-2026.md` | redundant | RAI- en adoptiecijfers zijn al geaggregeerd in W16 en W18 |
| `wiki/concepts/ai-employment-effects.md` | off-facet | werkgelegenheidseffecten; de facetten gaan over organisatie-inrichting |
| `wiki/sources/2026-04-28-ai-index-report-2025.md` | redundant | idem, oudere jaargang |
| `wiki/concepts/strategy.md` | off-facet | strategie-concept in het algemeen; ander vak |
| `wiki/sources/2026-04-28-mittri-cisco-ai-enabled-enterprise.md` | redundant | vijf fundamenten zitten in W24; zelf vendor-rapport |
| `wiki/sources/2026-05-11-blank-mit-6s191-three-laws-of-ai.md` | off-facet | technische AI-wetten, geen governance voor bedrijfskundigen |
| `wiki/sources/2026-08-10-miller-worklab-the-ai-shift-most-companies-didnt-see-coming.md` | redundant | graaf: uitgewerkt geval van de adoption gap uit W12 |
| `wiki/sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage.md` | redundant | graaf noemt het wederzijdse bevestiging van W11; W11 heeft Davenport |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | redundant | teamstructuur en hourglass al gedekt door W2 en W3; W1 levert de pre-AI-controle |
| `wiki/sources/2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world.md` | redundant | zelfde AWS-reeks en inhoud als Allen; W8 is de gekozen AWS-bron |
| `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` | redundant | Augmented Learners-cijfers staan in W16 en W24 |
| `wiki/sources/2026-08-16-hill-bloomberg-leaders-ceo-skills-age-of-ai.md` | off-facet | CEO-vaardigheden; niet ethiek/recht |
| `wiki/threads/organizational-frameworks-for-ai-adoption.md` | superseded | gesloten thread; de synthese W24 is de opvolger |
| `wiki/sources/2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai.md` | off-facet | persoonlijke efficiëntie, geen organisatievraag |
| `wiki/sources/2026-05-07-kiron-schrage-compound-benefits.md` | redundant | flywheel is overgenomen in W21; Schrage spreekt in W9 |
| `wiki/sources/2026-06-01-lf-state-of-tech-talent-europe-2026.md` | off-facet | talentrapport; niet ethiek/recht |
| `wiki/concepts/industrial-ai-agents.md` | off-facet | OT/industriële agents; niet de bedrijfskundige facetten |
| `wiki/sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships.md` | below-threshold | alleen via graaf; het 44%-cijfer wordt in W4 al aangehaald |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | redundant | day-zero-these al via W4, in het Nederlands en op mkb-schaal |
| `wiki/sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation.md` | off-facet | dynamic-capabilities-lens hoort bij strategisch management, niet bij IM |
| `wiki/sources/2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm.md` | below-threshold | alleen via graaf; platform-CEO-perspectief voegt geen facetantwoord toe |
| `wiki/sources/2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook.md` | off-facet | turnaround-playbook, geen IM-facet |
| `wiki/sources/2025-07-31-wang-agentspec-runtime-enforcement-llm-agents.md` | wrong-granularity | technisch runtime-mechanisme; W19 geeft de bedrijfskundige laag |
| `wiki/sources/2026-05-08-running-an-ai-native-engineering-org.md` | redundant | engineering-intern; W2 is de cross-customer variant |
| `wiki/sources/2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/agent-harness.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-06-17-ng-langchain-interrupt-future-of-ai-agents.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/dynamic-capabilities.md` | off-facet | zie Warner & Wäger |
| `wiki/sources/2026-06-18-dumra-mit-smr-dbs-everyone-an-innovator.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/agent-development-lifecycle.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2025-06-09-krakowski-human-centered-ai-field-experiment.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/entities/BBC.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | off-facet | macro-economische arena's |
| `wiki/sources/2026-07-10-hugging-face-ceo-companies-done-renting-their-ai.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/foundation-models.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-07-20-bbc-researchers-studied-ai-layoffs-heres-their-warning.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-01-lf-state-of-tech-talent-global-2026.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/open-source-ai.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/entities/MIT-Sloan-CIO-Symposium.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-07-22-brown-wef-meet-the-leader-entry-level-jobs-in-an-ai-era.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-12-techlatest-hacker-search-engines-osint-tools-2026.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-28-from-event-to-ecosystem-rethinking-how-technology-leaders-build-knowledge-in-the-ai-era.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/multi-agent-failure-modes.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/entities/Allan-Tate.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/systems-thinking.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/strategic-foresight.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-06-mit-ocw-future-of-mit-open-education.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/entities/Irving-Wladawsky-Berger.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/document-intelligence.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/ai-benchmarks.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2025-07-02-joshi-venkatraman-fowler-expert-generalists.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-08-14-blomfield-yc-building-structuring-ai-native-company.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2025-10-05-patwardhan-et-al-openai-gdpval.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/ai-knowledge-hiding.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-04-28-dellacqua-jagged-technological-frontier.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-01-09-baron-signals-for-2026.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/industry-4-0.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-07-10-building-the-future-of-agentic-infrastructure.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-04-07-loukides-radar-trends-april-2026.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/founder-led-sales.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/syntheses/harness-thinning-what-persists.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-07-14-khan-academy-ceo-the-real-ai-opportunity-is-in-boring-industries-sal-khan.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-05-loukides-radar-trends-may-2026.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/expert-generalist.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-20-agrawal-stanford-mse435-economics-of-generative-ai.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-04-28-brynjolfsson-canaries-coal-mine.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-21-jones-stanford-gsb-ai-and-our-economic-future.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-21-neven-manyika-google-io-quantum-ai-future.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/generative-ai.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/react-reasoning-acting.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-14-pochampally-assistant-or-actor-delegation-regret.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/agentic-engineering.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2025-12-02-allen-brozovich-davis-aws-reinvent-advanced-team-structures.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/ai-washing.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-04-28-anthropic-economic-index-q4-2025.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-06-03-chopra-headroom-context-optimization-layer-for-llm-applications.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-06-10-anicich-brouwers-why-employees-arent-transparent-ai-usage.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-07-09-nyc-executive-forum-2026-a-leaders-guide-to-agentic-ai.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-03-rewired-second-edition-sample.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/entities/MIT-Sloan-Management-Review.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-08-10-banholzer-laberge-mckinsey-how-to-maximize-competitive-advantage.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2022-02-23-oberholzer-gee-hbr-what-is-strategy-value-stick.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2022-06-29-martin-hbr-a-plan-is-not-a-strategy.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-02-09-ross-schneider-adaptability.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-07-01-mcgrath-power-of-strategic-centering.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-06-25-carroll-stanford-gsb-making-organizational-culture-great.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/entities/McKinsey-&-Company.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-07-24-turnbaugh-motherduck-context-layers-explained.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/entities/Microsoft.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/entities/Bloomberg-Podcasts.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/entities/Linda-Hill.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-07-19-why-netflix-is-betting-on-systems-thinkers-not-specialists-in-the-ai-era.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-06-24-mckinsey-ai-supercharging-software-development.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-02-11-shyamsundar-jain-organizational-strategies-collective-wisdom-nature.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/entities/David-Kiron.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-04-28-reitz-higgins-spacious-thinking.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/sources/2026-05-02-schoening-lennys-podcast-cultivating-agency-ai-era.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/entities/Sam-Ransbotham.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/strategic-centering.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/theory-based-view.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/concepts/infinite-game.md` | below-threshold | graaf-buur zonder facetbijdrage |
| `wiki/syntheses/strategy-finite-vs-infinite-game.md` | below-threshold | graaf-buur zonder facetbijdrage |

## 5. Information used
| Page | type | effConf | contribution |
|---|---|---|---|
| `wiki/sources/2026-08-19-rohrer-goto-modern-enterprise-architecture-architecting-for-outcomes.md` | source | — (bron) | [W1] EA-praktijk 2025 als pre-AI-baseline: ARB-antipatroon, governance-by-PR, paved paths, AI-als-output |
| `wiki/sources/2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler.md` | source | 0.75 | [W2] Ask-Assist-Automate; governance ≠ transformatie; middle-layer gap; embedded engineering |
| `wiki/sources/2026-06-17-priest-atlantic-pwc-ai-agents-changing-business.md` | source | — (bron) | [W3] snelheid van vertrouwen; taaklengte-plafond; hourglass; agentic applications |
| `wiki/sources/2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero.md` | source | — (bron) | [W4] Nederlandse mkb-casus: technologie leidt, afdelingen vervallen, CAIO ontbreekt, 100→18 |
| `wiki/sources/2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening.md` | source | — (bron) | [W5] Nederlandse sectorcijfers; 18-studies-spreiding taak- vs firmaniveau; drie condities |
| `wiki/sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity.md` | source | — (bron) | [W6] J-curve; koppen tellen is lui; task as atomic unit; 13→16-17%; pyramid→diamond; amplifying intention |
| `wiki/sources/2026-04-28-anand-wu-genai-playbook.md` | source | — (bron) | [W7] 2×2 foutkosten × kennistype; paradox of access; zes lekpunten; HBR-register |
| `wiki/sources/2026-06-12-aws-leaders-guide-data-strategy-agentic-ai.md` | source | — (bron) | [W8] vier data-tijdperken; machine als dataconsument; minimum viable governance; ownership |
| `wiki/sources/2026-06-11-mit-smr-agentic-ai-what-leaders-wish-they-knew-sooner.md` | source | — (bron) | [W9] Davenport: performatief toezicht; in-loop vs on-loop; agents als werknemers beheren |
| `wiki/sources/2026-05-02-dutt-chatterji-ai-experimentation-to-transformation.md` | source | — (bron) | [W10] micro-productivity trap; procesherontwerp is de waarde; evals; 10–25% EBITDA |
| `wiki/sources/2026-07-10-when-ai-becomes-common-organizational-capability-becomes-the-advantage-ep-16.md` | source | 0.7 | [W11] Davenport 2026: organisatie > technologie; agentic loopt achter; wie is verantwoordelijk |
| `wiki/sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company.md` | source | — (bron) | [W12] keten-argument; 56%/1-op-8; adoption/training/imagination gap; 30% in productie |
| `wiki/sources/2026-04-28-werner-lebrun-octopus-organization.md` | source | — (bron) | [W13] Tin Man vs Octopus; 12% transformaties; gedistribueerde intelligentie |
| `wiki/sources/2026-04-28-mit-sloan-ai-maturity.md` | source | — (bron) | [W14] vier stadia; Four S; stewardship by design (Guardian Life) |
| `wiki/sources/2026-01-22-imda-model-ai-governance-framework-for-agentic-ai.md` | source | — (bron) | [W15] vier pijlers agentic governance; ex ante risicobegrenzing |
| `wiki/concepts/enterprise-ai-adoption.md` | concept | 0.95 | [W16] hub: 88% adoptie, agents single digits, 7–15% volwassen, Rewired, DBS action gap |
| `wiki/concepts/ai-agents.md` | concept | 0.95 | [W17] definitie agent; harness-fouten ≠ modelfouten; RE-Bench horizon |
| `wiki/concepts/responsible-ai.md` | concept | 0.95 | [W18] RAI erkend > gemitigeerd; incidenten; RAI als stewardship; runtime-taxonomie |
| `wiki/concepts/agent-oversight-and-delegation.md` | concept | 0.774 | [W19] delegation regret; onomkeerbaarheid × zichtbaarheid; waar toezicht niet op mag rusten |
| `wiki/concepts/automation-vs-augmentation.md` | concept | 0.919 | [W20] definities; Canaries fact 3; ladder ↔ analyticsvormen |
| `wiki/concepts/micro-productivity-trap.md` | concept | 0.929 | [W21] vijf bronnen: luisterfout, geen technologiefout; verify/evaluate/capture |
| `wiki/concepts/jagged-frontier.md` | concept | 0.919 | [W22] BCG-experiment; automate what you can verify; grens onzichtbaar en beweegt |
| `wiki/concepts/ai-deskilling.md` | concept | 0.673 | [W23] deskilling; productive struggle; intergenerationele zorg |
| `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | synthesis | 0.9 | [W24] 11 raamwerken op lagen; beslisboom; waar ze echt verschillen |
| `wiki/entities/Thomas H. Davenport.md` | entity | — (bron) | [W25] index.md/ls: syllabusauteur |
| `wiki/entities/Erik Brynjolfsson.md` | entity | — (bron) | [W26] index.md/ls: bron van het equalizing effect en de Canaries |

## 6. Answer-element map
| Anchor | Answer element (claim) | Wiki page(s) | Section / span used |
|---|---|---|---|
| [W1] | EA-praktijk 2025 als pre-AI-baseline: ARB-antipatroon, governance-by-PR, paved paths, AI-als-output | [[2026-08-19-rohrer-goto-modern-enterprise-architecture-architecting-for-outcomes]] | TL;DR / Key claims |
| [W2] | Ask-Assist-Automate; governance ≠ transformatie; middle-layer gap; embedded engineering | [[2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler]] | TL;DR / Key claims |
| [W3] | snelheid van vertrouwen; taaklengte-plafond; hourglass; agentic applications | [[2026-06-17-priest-atlantic-pwc-ai-agents-changing-business]] | TL;DR / Key claims |
| [W4] | Nederlandse mkb-casus: technologie leidt, afdelingen vervallen, CAIO ontbreekt, 100→18 | [[2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero]] | TL;DR / Key claims |
| [W5] | Nederlandse sectorcijfers; 18-studies-spreiding taak- vs firmaniveau; drie condities | [[2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening]] | TL;DR / Key claims |
| [W6] | J-curve; koppen tellen is lui; task as atomic unit; 13→16-17%; pyramid→diamond; amplifying intention | [[2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity]] | TL;DR / Key claims |
| [W7] | 2×2 foutkosten × kennistype; paradox of access; zes lekpunten; HBR-register | [[2026-04-28-anand-wu-genai-playbook]] | TL;DR / Key claims |
| [W8] | vier data-tijdperken; machine als dataconsument; minimum viable governance; ownership | [[2026-06-12-aws-leaders-guide-data-strategy-agentic-ai]] | TL;DR / Key claims |
| [W9] | Davenport: performatief toezicht; in-loop vs on-loop; agents als werknemers beheren | [[2026-06-11-mit-smr-agentic-ai-what-leaders-wish-they-knew-sooner]] | TL;DR / Key claims |
| [W10] | micro-productivity trap; procesherontwerp is de waarde; evals; 10–25% EBITDA | [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation]] | TL;DR / Key claims |
| [W11] | Davenport 2026: organisatie > technologie; agentic loopt achter; wie is verantwoordelijk | [[2026-07-10-when-ai-becomes-common-organizational-capability-becomes-the-advantage-ep-16]] | TL;DR / Key claims |
| [W12] | keten-argument; 56%/1-op-8; adoption/training/imagination gap; 30% in productie | [[2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company]] | TL;DR / Key claims |
| [W13] | Tin Man vs Octopus; 12% transformaties; gedistribueerde intelligentie | [[2026-04-28-werner-lebrun-octopus-organization]] | TL;DR / Key claims |
| [W14] | vier stadia; Four S; stewardship by design (Guardian Life) | [[2026-04-28-mit-sloan-ai-maturity]] | TL;DR / Key claims |
| [W15] | vier pijlers agentic governance; ex ante risicobegrenzing | [[2026-01-22-imda-model-ai-governance-framework-for-agentic-ai]] | TL;DR / Key claims |
| [W16] | hub: 88% adoptie, agents single digits, 7–15% volwassen, Rewired, DBS action gap | [[enterprise-ai-adoption]] | TL;DR / Key claims |
| [W17] | definitie agent; harness-fouten ≠ modelfouten; RE-Bench horizon | [[ai-agents]] | TL;DR / Key claims |
| [W18] | RAI erkend > gemitigeerd; incidenten; RAI als stewardship; runtime-taxonomie | [[responsible-ai]] | TL;DR / Key claims |
| [W19] | delegation regret; onomkeerbaarheid × zichtbaarheid; waar toezicht niet op mag rusten | [[agent-oversight-and-delegation]] | TL;DR / Key claims |
| [W20] | definities; Canaries fact 3; ladder ↔ analyticsvormen | [[automation-vs-augmentation]] | TL;DR / Key claims |
| [W21] | vijf bronnen: luisterfout, geen technologiefout; verify/evaluate/capture | [[micro-productivity-trap]] | TL;DR / Key claims |
| [W22] | BCG-experiment; automate what you can verify; grens onzichtbaar en beweegt | [[jagged-frontier]] | TL;DR / Key claims |
| [W23] | deskilling; productive struggle; intergenerationele zorg | [[ai-deskilling]] | TL;DR / Key claims |
| [W24] | 11 raamwerken op lagen; beslisboom; waar ze echt verschillen | [[organizational-frameworks-for-ai-adoption]] | TL;DR / Key claims |
| [W25] | syllabusauteur 3.1, in de wiki met 2026-standpunten | [[Thomas H. Davenport]] | TL;DR / Key claims |
| [W26] | equalizing effect; Canaries; J-curve | [[Erik Brynjolfsson]] | TL;DR / Key claims |

## 7. Final answer
**Kernoordeel.** Het denken in syllabus 8481 is niet fout; het rust op drie aannames die de 2025–2026-bronnen in de wiki verwerpen: IT ondersteunt de business (HelloPrint: „technologie wordt leidend, en daaromheen zit een veel kleinere groep mensen die die technologie aanstuurt" [W4]), de mens is de enige beslisser (agents handelen zelf; de vraag is waar de mens nog goedkeurt [W17][W19]), en adoptie is de horde (88% adoptie, agents in de enkele procenten; de horde is herontwerp van werk [W16][W12]).

**Wat blijft, en scherper dan ooit.** Henderson & Venkatraman: „als het hoofd van de businessunit niet aansprakelijk is, heb je geen agent maar een demo" [W2]; McKinsey kent geen succesverhaal zonder business aan het stuur [W16]; „iedereen AI laten gebruiken is een output, geen uitkomst" [W1]. Markus (1983): de interactietheorie is de consensus — vijf bronnen noemen het falen van AI-projecten een luisterfout, geen technologiefout [W21]; „governance en transformatie in één hand: een van de twee wint" [W2]. Porter & Millar: de keten verklaart de productiviteitsparadox — taakniveau tot +73%, firmaniveau ~0% [W5]; „de meeste bedrijven zijn een keten" [W12]; de paradox of access is Porter [W7]. Zachman: wat/hoe/waar/waarom is wat een agent nodig heeft — „traditionele data geeft het wat; agentic AI eist het waarom" [W8]. Kaplan & Norton: meet output, niet input [W6]; DBS zet 20% van elke scorecard op transformatie [W16]. Davenport zelf (3.1) in 2026: organisatievermogen overtreft technologie [W11][W25].

**Wat verschuift.** Maes' negenvlak: de middenkolom is waar het misgaat (datastrategie voor machines [W8]; het ontbrekende middenniveau van team-agents [W2]) — maar de kolommen zijn geen afdelingen meer: „aparte afdelingen voor marketing, IT, operatie en finance verliezen hun functie" [W4]. TOGAF: de lagen blijven, de fasegewijze methode met architectuurboard is een antipatroon; governance-by-pull-request en paved paths [W1]. ITIL: agents vragen levenscyclusbeheer als een medewerker [W9], per model gemeten op drift en hallucinatie [W3]; run en change vallen samen [W1]. Davenport 2006: vier data-tijdperken, de machine is de primaire consument [W8]; de vier analyticsvormen worden een autonomieladder Ask→Assist→Automate [W2][W20]. Laudon besluitvorming: foutkosten × kennistype [W7] en een grillige grens (−19 pp bij BCG-consultants, en zelfverzekerder) [W22]. TAM/UTAUT: gebruiksgemak is geen barrière meer [W7]; de horde is de imagination gap, 3× zoveel toegang als training [W12]; vertrouwen per taak, onomkeerbaarheid × zichtbaarheid [W19]; adoptie op de snelheid van vertrouwen [W3].

**Waarvan afscheid, volgens experts.** Koppen tellen als rendement („een beetje lui" [W6]); governance in fasen [W1]; adoptie = gebruik („het informatiegat is weg, alleen het actiegat blijft" [W16]; „verificatie aangezien voor de hele klus" [W21]); de mens in de lus als vanzelfsprekende waarborg (Davenport: toezicht wordt performatief [W9]); data verzamelen als doel („$50M, vijf jaar, één ontslagen CIO, geen waarde" [W8]); pilots als vooruitgang (~30% haalt productie [W12]; stadium versus val [W24]).

**Materiaal.** Nederlands: Scheffer/De Ondernemer [W4], RaboResearch [W5] (vervangt KPMG 2024). HBR-register: Anand & Wu [W7], Dutt/Chatterji [W10], Werner & Le-Brun [W13]. Video voor de zaal: MIT SMR 11 min met Davenport [W9], BBC AI Decoded [W12], Brynjolfsson [W6]. Governance/ethiek: IMDA [W15], agent oversight [W19], responsible AI [W18], MIT CISR stewardship [W14]. Docentachtergrond: Rohrer [W1], Beutler [W2], AWS data [W8], synthese van 11 raamwerken [W24].

**Gaten.** De wiki heeft geen pagina over de EU AI-verordening en niets over TAM/UTAUT als theorie; de aanbevelingen uit de analyse van 24 augustus (Laudon 17e ed. H4/H11, AI-verordening-samenvatting, Shrestha 2019) blijven staan. Leveranciers (OpenAI W2/W10, AWS W8/W13, PwC W3) zijn gemarkeerd; hun cijfers zijn niet onafhankelijk geverifieerd.

Het volledige verslag, met per syllabusbron het oordeel blijft/verschuift/weg, het materiaal per collegeblok en de kwaliteitseisen, staat in `/Users/witoldtenhove/Documents/HAN/C-CLUSTER/NIEUW-2026-27/IM/houdbaarheidsonderzoek-informatiemanagement.html`.

## 8. Trace artifact
Machine-readable provenance: [`im-hoorcollege-oud-denken-ai-query-trace.json`](im-hoorcollege-oud-denken-ai-query-trace.json)
