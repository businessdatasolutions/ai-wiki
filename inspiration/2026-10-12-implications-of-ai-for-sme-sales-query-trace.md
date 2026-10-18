---
type: query-trace
question: "Write a blog of 1000 words with title \"The implications of AI for SME sales.\""
date: 2026-10-12
language: en
trace: "2026-10-12-implications-of-ai-for-sme-sales-query-trace.json"
pages_used: 9
pages_ignored: 112
---

# Query trace — The implications of AI for SME sales

## 1. Question
- **Original:** Write a blog of 1000 words with title "The implications of AI for SME sales."
- **Restated:** What does the wiki say AI means for how small and medium-sized enterprises sell, written up as a ~1000-word blog?
- **Facets:** 1) How AI changes buyer discovery and the path to purchase (answer engines, agents) 2) How AI changes the selling conversation itself (intent, trust, go-to-market choice) 3) SME-specific constraints and capabilities for adopting AI in sales 4) Practical implications an SME can act on
- **Retrieval query used:** "AI implications for small and medium enterprise sales, buyer discovery, sales agents, SME adoption". Retrieval query rephrased from the writing instruction into its topical content so qmd matches on substance, not on "write a blog of 1000 words".

## 2. Paths explored
Ledger: 10 qmd hits, 120 candidates, graph available (hops 1), no graph warning.

**qmd hits** (relevance stream)
| # | Page | type | qmd score | fused | verdict |
|---|------|------|-----------|-------|---------|
| 1 | `wiki/concepts/enterprise-ai-adoption.md` | concept | 1.00 | 0.98 | IGNORE |
| 2 | `wiki/concepts/micro-productivity-trap.md` | concept | 0.33 | 0.95 | USE |
| 3 | `wiki/sources/2024-08-13-schwaeke-new-normal-ai-adoption-smes.md` | source | 0.25 | 0.91 | USE |
| 4 | `wiki/concepts/agent-harness.md` | concept | 0.17 | 0.93 | IGNORE |
| 5 | `wiki/sources/2025-06-15-cimino-ai-adoption-sustainable-growth-smes.md` | source | 0.14 | 0.88 | USE |
| 6 | `wiki/sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity.md` | source | 0.13 | 0.87 | IGNORE |
| 7 | `wiki/sources/2026-08-13-a16z-lighthouse-or-landgrab-ai-sales-strategy.md` | source | 0.11 | 0.86 | USE |
| 8 | `wiki/sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era.md` | source | 0.10 | 0.84 | IGNORE |
| 9 | `wiki/sources/2026-04-28-ai-index-report-2025.md` | source | 0.09 | 0.83 | IGNORE |
| 10 | `wiki/sources/2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet.md` | source | 0.08 | 0.82 | USE |

**graph neighbours** (typed-edge stream, 110 pages)
| Page | reached via | hops | fused | verdict |
|------|-------------|------|-------|---------|
| `wiki/concepts/ai-knowledge-hiding.md` | concepts/enterprise-ai-adoption --instance-of--> this | 1 | 0.46 | IGNORE |
| `wiki/concepts/automation-vs-augmentation.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.46 | IGNORE |
| `wiki/concepts/agentic-web.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.45 | USE |
| `wiki/concepts/ai-sovereignty.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.45 | IGNORE |
| `wiki/concepts/dynamic-capabilities.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.45 | IGNORE |
| `wiki/concepts/ai-employment-effects.md` | concepts/enterprise-ai-adoption --caused--> this | 1 | 0.43 | IGNORE |
| `wiki/concepts/answer-engine-optimization.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.43 | USE |
| `wiki/concepts/jagged-frontier.md` | concepts/enterprise-ai-adoption --uses--> this | 1 | 0.42 | IGNORE |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.41 | IGNORE |
| `wiki/concepts/responsible-ai.md` | concepts/enterprise-ai-adoption --part-of--> this | 1 | 0.40 | IGNORE |
| `wiki/concepts/open-source-ai.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.40 | IGNORE |
| `wiki/concepts/founder-led-sales.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.38 | IGNORE |
| `wiki/concepts/generative-ai.md` | concepts/enterprise-ai-adoption --caused--> this | 1 | 0.38 | IGNORE |
| `wiki/concepts/systems-thinking.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.38 | IGNORE |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.37 | IGNORE |
| `wiki/concepts/technology-adoption-theories.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.37 | IGNORE |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.36 | IGNORE |
| `wiki/sources/2026-05-06-mit-ocw-future-of-mit-open-education.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.36 | IGNORE |
| `wiki/concepts/strategic-foresight.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.36 | IGNORE |
| `wiki/sources/2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.35 | IGNORE |
| `wiki/sources/2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.35 | IGNORE |
| `wiki/sources/2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.34 | IGNORE |
| `wiki/sources/2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers.md` | concepts/micro-productivity-trap --supports--> this | 1 | 0.33 | IGNORE |
| `wiki/concepts/ai-coding-productivity-evidence.md` | concepts/micro-productivity-trap --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs.md` | concepts/micro-productivity-trap --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/concepts/document-intelligence.md` | concepts/enterprise-ai-adoption --part-of--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy.md` | concepts/micro-productivity-trap --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success.md` | sources/2024-08-13-schwaeke-new-normal-ai-adoption-smes --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2025-01-08-khanfar-factors-influencing-ai-adoption-slr.md` | sources/2024-08-13-schwaeke-new-normal-ai-adoption-smes --supports--> this | 1 | 0.31 | IGNORE |
| `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | concepts/enterprise-ai-adoption --instance-of--> this | 1 | 0.31 | IGNORE |
| `wiki/sources/2025-07-25-albishri-breaking-barriers-genai-adoption.md` | sources/2024-08-13-schwaeke-new-normal-ai-adoption-smes --supports--> this | 1 | 0.31 | IGNORE |
| `wiki/concepts/ai-agents.md` | concepts/agent-harness --part-of--> this | 1 | 0.31 | IGNORE |
| `wiki/sources/2026-03-28-nguyen-ai-adoption-toe-dynamic-capabilities.md` | sources/2024-08-13-schwaeke-new-normal-ai-adoption-smes --supports--> this | 1 | 0.30 | IGNORE |
| `wiki/concepts/agent-development-lifecycle.md` | concepts/agent-harness --uses--> this | 1 | 0.30 | IGNORE |
| `wiki/syntheses/ai-worker-maturity-levels.md` | concepts/enterprise-ai-adoption --supports--> this | 1 | 0.30 | IGNORE |
| `wiki/concepts/foundation-models.md` | concepts/agent-harness --uses--> this | 1 | 0.30 | IGNORE |
| `wiki/concepts/agentic-engineering.md` | concepts/agent-harness --depends-on--> this | 1 | 0.28 | IGNORE |
| `wiki/concepts/llm-wiki.md` | concepts/agent-harness --part-of--> this | 1 | 0.28 | IGNORE |
| `wiki/concepts/agent-fleet-management.md` | concepts/agent-harness --depends-on--> this | 1 | 0.27 | IGNORE |
| `wiki/concepts/small-language-models.md` | concepts/agent-harness --uses--> this | 1 | 0.27 | IGNORE |
| `wiki/concepts/react-reasoning-acting.md` | concepts/agent-harness --uses--> this | 1 | 0.27 | IGNORE |
| `wiki/concepts/industrial-ai-agents.md` | concepts/agent-harness --depends-on--> this | 1 | 0.26 | IGNORE |
| `wiki/concepts/graph-engineering.md` | concepts/agent-harness --part-of--> this | 1 | 0.26 | IGNORE |
| `wiki/concepts/software-3.0.md` | concepts/agent-harness --depends-on--> this | 1 | 0.25 | IGNORE |
| `wiki/concepts/multi-agent-failure-modes.md` | concepts/agent-harness --depends-on--> this | 1 | 0.25 | IGNORE |
| `wiki/entities/Antigravity.md` | concepts/agent-harness --instance-of--> this | 1 | 0.25 | IGNORE |
| `wiki/concepts/knowledge-graphs.md` | concepts/agent-harness --part-of--> this | 1 | 0.25 | IGNORE |
| `wiki/entities/Agent-Development-Kit.md` | concepts/agent-harness --instance-of--> this | 1 | 0.25 | IGNORE |
| `wiki/sources/2024-12-19-anthropic-building-effective-agents.md` | concepts/agent-harness --uses--> this | 1 | 0.24 | IGNORE |
| `wiki/sources/2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair.md` | concepts/agent-harness --supports--> this | 1 | 0.24 | IGNORE |
| `wiki/entities/Claude-Code.md` | concepts/agent-harness --instance-of--> this | 1 | 0.24 | IGNORE |
| `wiki/entities/Cursor.md` | concepts/agent-harness --instance-of--> this | 1 | 0.24 | IGNORE |
| `wiki/sources/2025-07-31-wang-agentspec-runtime-enforcement-llm-agents.md` | concepts/agent-harness --uses--> this | 1 | 0.24 | IGNORE |
| `wiki/sources/2025-09-28-husain-ai-evaluations-clearly-explained-50-min.md` | concepts/agent-harness --supports--> this | 1 | 0.24 | IGNORE |
| `wiki/sources/2025-11-26-anthropic-effective-harnesses-long-running-agents.md` | concepts/agent-harness --uses--> this | 1 | 0.24 | IGNORE |
| `wiki/concepts/spec-driven-development.md` | concepts/agent-harness --uses--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-02-17-langchain-improving-deep-agents-harness-engineering.md` | concepts/agent-harness --uses--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-03-05-lou-deepmind-autoharness-code-harness-synthesis.md` | concepts/agent-harness --uses--> this | 1 | 0.23 | IGNORE |
| `wiki/entities/Devin.md` | concepts/agent-harness --instance-of--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness.md` | concepts/agent-harness --uses--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-03-20-huggingface-agentic-evaluations-workshop.md` | concepts/agent-harness --supports--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-03-26-pan-natural-language-agent-harnesses.md` | concepts/agent-harness --uses--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-03-30-lee-meta-harness-end-to-end-optimization.md` | concepts/agent-harness --uses--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks.md` | concepts/agent-harness --supports--> this | 1 | 0.22 | IGNORE |
| `wiki/sources/2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained.md` | concepts/agent-harness --supports--> this | 1 | 0.22 | IGNORE |
| `wiki/entities/Cline.md` | concepts/agent-harness --instance-of--> this | 1 | 0.22 | IGNORE |
| `wiki/sources/2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack.md` | concepts/agent-harness --supports--> this | 1 | 0.22 | IGNORE |
| `wiki/sources/2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers.md` | concepts/agent-harness --supports--> this | 1 | 0.22 | IGNORE |
| `wiki/sources/2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide.md` | concepts/agent-harness --supports--> this | 1 | 0.22 | IGNORE |
| `wiki/entities/LiteLLM.md` | concepts/agent-harness --part-of--> this | 1 | 0.22 | IGNORE |
| `wiki/sources/2026-05-11-blank-mit-6s191-three-laws-of-ai.md` | concepts/agent-harness --supports--> this | 1 | 0.22 | IGNORE |
| `wiki/entities/Langfuse.md` | concepts/agent-harness --part-of--> this | 1 | 0.21 | IGNORE |
| `wiki/sources/2026-05-11-huber-chroma-rag-is-dead-agentic-search.md` | concepts/agent-harness --supports--> this | 1 | 0.21 | IGNORE |
| `wiki/sources/2026-05-11-karten-zhang-continual-harness-online-adaptation.md` | concepts/agent-harness --uses--> this | 1 | 0.21 | IGNORE |
| `wiki/sources/2026-05-18-wolfe-agent-evaluation-detailed-guide.md` | concepts/agent-harness --supports--> this | 1 | 0.21 | IGNORE |
| `wiki/sources/2026-07-14-wang-shi-harness-handbook-behavior-localization.md` | concepts/agent-harness --uses--> this | 1 | 0.21 | IGNORE |
| `wiki/sources/2026-04-28-anand-wu-genai-playbook.md` | sources/2025-06-15-cimino-ai-adoption-sustainable-growth-smes --supports--> this | 1 | 0.20 | IGNORE |
| `wiki/sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation.md` | sources/2025-06-15-cimino-ai-adoption-sustainable-growth-smes --supports--> this | 1 | 0.20 | IGNORE |
| `wiki/sources/2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset.md` | sources/2025-06-15-cimino-ai-adoption-sustainable-growth-smes --contradicts--> this | 1 | 0.20 | IGNORE |
| `wiki/sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company.md` | sources/2025-06-15-cimino-ai-adoption-sustainable-growth-smes --supports--> this | 1 | 0.20 | IGNORE |
| `wiki/sources/2026-07-22-brown-wef-meet-the-leader-entry-level-jobs-in-an-ai-era.md` | sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --contradicts--> this | 1 | 0.20 | IGNORE |
| `wiki/sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness.md` | sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --supports--> this | 1 | 0.20 | IGNORE |
| `wiki/sources/2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable.md` | sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --supports--> this | 1 | 0.19 | IGNORE |
| `wiki/sources/2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services.md` | sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --supports--> this | 1 | 0.19 | IGNORE |
| `wiki/sources/2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity.md` | sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --supports--> this | 1 | 0.19 | IGNORE |
| `wiki/sources/2026-08-10-miller-worklab-the-ai-shift-most-companies-didnt-see-coming.md` | sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --supports--> this | 1 | 0.19 | IGNORE |
| `wiki/sources/2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs.md` | sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --contradicts--> this | 1 | 0.19 | IGNORE |
| `wiki/sources/2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai.md` | sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --supports--> this | 1 | 0.19 | IGNORE |
| `wiki/sources/2026-07-10-when-ai-becomes-common-organizational-capability-becomes-the-advantage-ep-16.md` | sources/2025-06-15-cimino-ai-adoption-sustainable-growth-smes --supports--> this | 1 | 0.19 | IGNORE |
| `wiki/sources/2026-09-29-lavoie-mckinsey-talks-talent-leading-when-change-feels-threatening.md` | sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --supports--> this | 1 | 0.19 | IGNORE |
| `wiki/sources/2026-10-01-dw-news-estonia-young-people-entry-level-jobs.md` | sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --supports--> this | 1 | 0.18 | IGNORE |
| `wiki/syntheses/is-rag-dead.md` | concepts/agent-harness --supports--> this | 1 | 0.18 | IGNORE |
| `wiki/sources/2026-10-09-mollick-hbr-how-ai-is-changing-strategy-four-skills.md` | sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity --supports--> this | 1 | 0.18 | IGNORE |
| `wiki/syntheses/knowledge-architectures-for-llm-agents.md` | concepts/agent-harness --supports--> this | 1 | 0.18 | IGNORE |
| `wiki/sources/2026-06-22-yc-kolysh-how-to-get-your-first-10-customers.md` | sources/2026-08-13-a16z-lighthouse-or-landgrab-ai-sales-strategy --supports--> this | 1 | 0.18 | IGNORE |
| `wiki/concepts/durable-skills.md` | sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era --supports--> this | 1 | 0.18 | IGNORE |
| `wiki/concepts/vibe-coding.md` | sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era --supports--> this | 1 | 0.18 | IGNORE |
| `wiki/syntheses/harness-thinning-what-persists.md` | concepts/agent-harness --instance-of--> this | 1 | 0.18 | IGNORE |
| `wiki/sources/2026-06-24-rubinstein-onyemah-startup-founders-new-sales-playbook.md` | sources/2026-08-13-a16z-lighthouse-or-landgrab-ai-sales-strategy --supports--> this | 1 | 0.18 | USE |
| `wiki/sources/2026-07-31-collison-yc-startup-school-is-ai-breaking-the-lean-startup-playbook.md` | sources/2026-08-13-a16z-lighthouse-or-landgrab-ai-sales-strategy --supports--> this | 1 | 0.18 | IGNORE |
| `wiki/sources/2026-08-12-tan-a16z-new-rules-for-founders.md` | sources/2026-08-13-a16z-lighthouse-or-landgrab-ai-sales-strategy --supports--> this | 1 | 0.18 | IGNORE |
| `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era --supports--> this | 1 | 0.17 | IGNORE |
| `wiki/concepts/ai-deskilling.md` | sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era --supports--> this | 1 | 0.17 | IGNORE |
| `wiki/sources/2026-09-25-charles-lennys-podcast-what-product-looks-like-when-coding-is-solved.md` | sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era --supports--> this | 1 | 0.17 | IGNORE |
| `wiki/sources/2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet.md` | sources/2026-04-28-ai-index-report-2025 --supports--> this | 1 | 0.17 | IGNORE |
| `wiki/sources/2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet.md` | sources/2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet --supports--> this | 1 | 0.17 | IGNORE |
| `wiki/sources/2026-10-01-chesky-silicon-valley-girl-people-who-know-what-to-build-with-ai.md` | sources/2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet --supports--> this | 1 | 0.17 | IGNORE |
| `wiki/sources/2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook.md` | sources/2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet --supports--> this | 1 | 0.17 | IGNORE |
| `wiki/sources/2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free.md` | sources/2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet --supports--> this | 1 | 0.17 | IGNORE |

**index.md / gap-expansion** (Step 5)
| Page | why added |
|------|-----------|
| `wiki/sources/2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook.md` | Facet 1 needed the primary HubSpot traffic/leads figures; found via `wiki/index.md` grep for sales/buyer terms. Not in ledger. |

## 3. Ignore policy applied
- `off-facet` — adjacent via vector proximity or graph edges (mostly the agent-harness neighbourhood and labour-economics sources) but answers none of the four facets.
- `below-threshold` — graph-only neighbours with low fused scores (≤0.46) that no facet required.
- `redundant` — a stronger, already-selected page carries the same claim (e.g. the AEO concept page condenses the Amiel & Sanders source).
- `wrong-granularity` — entity catalogue cards; the facets need claims and figures.
- Graph-only candidates were held to a higher bar: three were promoted (W3, W5, W7) because each is the strongest page for a facet.

## 4. Information ignored
| Page | reason-class | one-line reason |
|------|--------------|-----------------|
| `wiki/concepts/enterprise-ai-adoption.md` | redundant | top qmd hit but a corpus-wide adoption hub; the SME-specific adoption facet is covered more precisely by W1/W2 and W9 |
| `wiki/concepts/agent-harness.md` | off-facet | agent runtime engineering; no bearing on SME selling |
| `wiki/sources/2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity.md` | off-facet | labour/talent economics, not sales or buyer behaviour |
| `wiki/sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era.md` | off-facet | product management role in AI era, not sales |
| `wiki/sources/2026-04-28-ai-index-report-2025.md` | off-facet | macro AI indicators; no SME-sales evidence used |
| `wiki/concepts/ai-knowledge-hiding.md` | below-threshold | graph-only neighbour (fused 0.46); no facet needs it |
| `wiki/concepts/automation-vs-augmentation.md` | below-threshold | graph-only neighbour (fused 0.46); no facet needs it |
| `wiki/concepts/ai-sovereignty.md` | below-threshold | graph-only neighbour (fused 0.45); no facet needs it |
| `wiki/concepts/dynamic-capabilities.md` | below-threshold | graph-only neighbour (fused 0.45); no facet needs it |
| `wiki/concepts/ai-employment-effects.md` | below-threshold | graph-only neighbour (fused 0.43); no facet needs it |
| `wiki/concepts/jagged-frontier.md` | below-threshold | graph-only neighbour (fused 0.42); no facet needs it |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | below-threshold | graph-only neighbour (fused 0.41); no facet needs it |
| `wiki/concepts/responsible-ai.md` | below-threshold | graph-only neighbour (fused 0.40); no facet needs it |
| `wiki/concepts/open-source-ai.md` | below-threshold | graph-only neighbour (fused 0.40); no facet needs it |
| `wiki/concepts/founder-led-sales.md` | redundant | its sales claims are carried by its anchors W7 and W8, read directly |
| `wiki/concepts/generative-ai.md` | below-threshold | graph-only neighbour (fused 0.38); no facet needs it |
| `wiki/concepts/systems-thinking.md` | below-threshold | graph-only neighbour (fused 0.38); no facet needs it |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | below-threshold | graph-only neighbour (fused 0.37); no facet needs it |
| `wiki/concepts/technology-adoption-theories.md` | below-threshold | graph-only neighbour (fused 0.37); no facet needs it |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | below-threshold | graph-only neighbour (fused 0.36); no facet needs it |
| `wiki/sources/2026-05-06-mit-ocw-future-of-mit-open-education.md` | below-threshold | graph-only neighbour (fused 0.36); no facet needs it |
| `wiki/concepts/strategic-foresight.md` | below-threshold | graph-only neighbour (fused 0.36); no facet needs it |
| `wiki/sources/2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china.md` | below-threshold | graph-only neighbour (fused 0.35); no facet needs it |
| `wiki/sources/2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas.md` | below-threshold | graph-only neighbour (fused 0.35); no facet needs it |
| `wiki/sources/2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells.md` | below-threshold | graph-only neighbour (fused 0.34); no facet needs it |
| `wiki/sources/2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers.md` | below-threshold | graph-only neighbour (fused 0.33); no facet needs it |
| `wiki/concepts/ai-coding-productivity-evidence.md` | below-threshold | graph-only neighbour (fused 0.32); no facet needs it |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | below-threshold | graph-only neighbour (fused 0.32); no facet needs it |
| `wiki/sources/2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs.md` | below-threshold | graph-only neighbour (fused 0.32); no facet needs it |
| `wiki/concepts/document-intelligence.md` | below-threshold | graph-only neighbour (fused 0.32); no facet needs it |
| `wiki/sources/2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy.md` | below-threshold | graph-only neighbour (fused 0.32); no facet needs it |
| `wiki/sources/2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success.md` | below-threshold | graph-only neighbour (fused 0.32); no facet needs it |
| `wiki/sources/2025-01-08-khanfar-factors-influencing-ai-adoption-slr.md` | below-threshold | graph-only neighbour (fused 0.31); no facet needs it |
| `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | below-threshold | graph-only neighbour (fused 0.31); no facet needs it |
| `wiki/sources/2025-07-25-albishri-breaking-barriers-genai-adoption.md` | below-threshold | graph-only neighbour (fused 0.31); no facet needs it |
| `wiki/concepts/ai-agents.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-03-28-nguyen-ai-adoption-toe-dynamic-capabilities.md` | below-threshold | graph-only neighbour (fused 0.30); no facet needs it |
| `wiki/concepts/agent-development-lifecycle.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/syntheses/ai-worker-maturity-levels.md` | below-threshold | graph-only neighbour (fused 0.30); no facet needs it |
| `wiki/concepts/foundation-models.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/concepts/agentic-engineering.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/concepts/llm-wiki.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/concepts/agent-fleet-management.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/concepts/small-language-models.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/concepts/react-reasoning-acting.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/concepts/industrial-ai-agents.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/concepts/graph-engineering.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/concepts/software-3.0.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/concepts/multi-agent-failure-modes.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/entities/Antigravity.md` | wrong-granularity | entity catalogue card; facets need claims, not identities |
| `wiki/concepts/knowledge-graphs.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/entities/Agent-Development-Kit.md` | wrong-granularity | entity catalogue card; facets need claims, not identities |
| `wiki/sources/2024-12-19-anthropic-building-effective-agents.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/entities/Claude-Code.md` | wrong-granularity | entity catalogue card; facets need claims, not identities |
| `wiki/entities/Cursor.md` | wrong-granularity | entity catalogue card; facets need claims, not identities |
| `wiki/sources/2025-07-31-wang-agentspec-runtime-enforcement-llm-agents.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2025-09-28-husain-ai-evaluations-clearly-explained-50-min.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2025-11-26-anthropic-effective-harnesses-long-running-agents.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/concepts/spec-driven-development.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-02-17-langchain-improving-deep-agents-harness-engineering.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-03-05-lou-deepmind-autoharness-code-harness-synthesis.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/entities/Devin.md` | wrong-granularity | entity catalogue card; facets need claims, not identities |
| `wiki/sources/2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-03-20-huggingface-agentic-evaluations-workshop.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-03-26-pan-natural-language-agent-harnesses.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-03-30-lee-meta-harness-end-to-end-optimization.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/entities/Cline.md` | wrong-granularity | entity catalogue card; facets need claims, not identities |
| `wiki/sources/2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/entities/LiteLLM.md` | wrong-granularity | entity catalogue card; facets need claims, not identities |
| `wiki/sources/2026-05-11-blank-mit-6s191-three-laws-of-ai.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/entities/Langfuse.md` | wrong-granularity | entity catalogue card; facets need claims, not identities |
| `wiki/sources/2026-05-11-huber-chroma-rag-is-dead-agentic-search.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-05-11-karten-zhang-continual-harness-online-adaptation.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-05-18-wolfe-agent-evaluation-detailed-guide.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-07-14-wang-shi-harness-handbook-behavior-localization.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-04-28-anand-wu-genai-playbook.md` | below-threshold | graph-only neighbour (fused 0.20); no facet needs it |
| `wiki/sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation.md` | below-threshold | graph-only neighbour (fused 0.20); no facet needs it |
| `wiki/sources/2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset.md` | off-facet | contradicts edge concerns labour/productivity claims of its seed, not sales; does not change the answer |
| `wiki/sources/2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company.md` | below-threshold | graph-only neighbour (fused 0.20); no facet needs it |
| `wiki/sources/2026-07-22-brown-wef-meet-the-leader-entry-level-jobs-in-an-ai-era.md` | off-facet | contradicts edge concerns labour/productivity claims of its seed, not sales; does not change the answer |
| `wiki/sources/2026-07-29-ng-washington-post-china-open-source-ai-competitiveness.md` | below-threshold | graph-only neighbour (fused 0.20); no facet needs it |
| `wiki/sources/2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable.md` | below-threshold | graph-only neighbour (fused 0.19); no facet needs it |
| `wiki/sources/2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services.md` | below-threshold | graph-only neighbour (fused 0.19); no facet needs it |
| `wiki/sources/2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity.md` | below-threshold | graph-only neighbour (fused 0.19); no facet needs it |
| `wiki/sources/2026-08-10-miller-worklab-the-ai-shift-most-companies-didnt-see-coming.md` | below-threshold | graph-only neighbour (fused 0.19); no facet needs it |
| `wiki/sources/2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs.md` | off-facet | contradicts edge concerns labour/productivity claims of its seed, not sales; does not change the answer |
| `wiki/sources/2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai.md` | below-threshold | graph-only neighbour (fused 0.19); no facet needs it |
| `wiki/sources/2026-07-10-when-ai-becomes-common-organizational-capability-becomes-the-advantage-ep-16.md` | below-threshold | graph-only neighbour (fused 0.19); no facet needs it |
| `wiki/sources/2026-09-29-lavoie-mckinsey-talks-talent-leading-when-change-feels-threatening.md` | below-threshold | graph-only neighbour (fused 0.19); no facet needs it |
| `wiki/sources/2026-10-01-dw-news-estonia-young-people-entry-level-jobs.md` | below-threshold | graph-only neighbour (fused 0.18); no facet needs it |
| `wiki/syntheses/is-rag-dead.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-10-09-mollick-hbr-how-ai-is-changing-strategy-four-skills.md` | below-threshold | graph-only neighbour (fused 0.18); no facet needs it |
| `wiki/syntheses/knowledge-architectures-for-llm-agents.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-06-22-yc-kolysh-how-to-get-your-first-10-customers.md` | redundant | first-customer tactics overlap W7 niche/wedge advice |
| `wiki/concepts/durable-skills.md` | below-threshold | graph-only neighbour (fused 0.18); no facet needs it |
| `wiki/concepts/vibe-coding.md` | below-threshold | graph-only neighbour (fused 0.18); no facet needs it |
| `wiki/syntheses/harness-thinning-what-persists.md` | off-facet | graph neighbour of agent-harness (agent engineering), unrelated to SME sales |
| `wiki/sources/2026-07-31-collison-yc-startup-school-is-ai-breaking-the-lean-startup-playbook.md` | below-threshold | graph-only neighbour (fused 0.18); no facet needs it |
| `wiki/sources/2026-08-12-tan-a16z-new-rules-for-founders.md` | below-threshold | graph-only neighbour (fused 0.18); no facet needs it |
| `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | below-threshold | graph-only neighbour (fused 0.17); no facet needs it |
| `wiki/concepts/ai-deskilling.md` | below-threshold | graph-only neighbour (fused 0.17); no facet needs it |
| `wiki/sources/2026-09-25-charles-lennys-podcast-what-product-looks-like-when-coding-is-solved.md` | below-threshold | graph-only neighbour (fused 0.17); no facet needs it |
| `wiki/sources/2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet.md` | redundant | figures used via W3, which condenses it |
| `wiki/sources/2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet.md` | redundant | agent-commerce thesis already carried by W6 |
| `wiki/sources/2026-10-01-chesky-silicon-valley-girl-people-who-know-what-to-build-with-ai.md` | below-threshold | graph-only neighbour (fused 0.17); no facet needs it |
| `wiki/sources/2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook.md` | redundant | primary source of W5; the concept page already condenses it |
| `wiki/sources/2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free.md` | off-facet | pricing model of one AI note-taker, not SME selling |

## 5. Information used
| Anchor | Page | type | effConf | contribution |
|--------|------|------|---------|--------------|
| W1 | `wiki/sources/2024-08-13-schwaeke-new-normal-ai-adoption-smes.md` | source | — | SME adoption barriers (resources, compatibility, ROI) — the SME constraint on AI in sales |
| W2 | `wiki/sources/2025-06-15-cimino-ai-adoption-sustainable-growth-smes.md` | source | — | readiness vs implementation gap in 210 small firms |
| W3 | `wiki/concepts/agentic-web.md` | concept | 0.75 | network-level evidence that discovery moved from search to answers; agents between shop and shopper *(graph-only)* |
| W4 | `wiki/sources/2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook.md` | source | — | HubSpot -80% traffic / +20% leads; buyers research in chat assistants *(promoted: gap-expansion)* |
| W5 | `wiki/concepts/answer-engine-optimization.md` | concept | 0.74 | AEO mechanics: prompts vs keywords, consensus signal, low-tech measurement, late-stage buyer arrival *(graph-only)* |
| W6 | `wiki/sources/2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet.md` | source | — | agentic commerce; AI discovery surfaces niche/long-tail sellers |
| W7 | `wiki/sources/2026-06-24-rubinstein-onyemah-startup-founders-new-sales-playbook.md` | source | — | 250+ founder study: attention ≠ traction, buyer fear, SPRINT, niche wedge *(graph-only)* |
| W8 | `wiki/sources/2026-08-13-a16z-lighthouse-or-landgrab-ai-sales-strategy.md` | source | — | whom to sell to: proof vs math; Meraki mid-market case |
| W9 | `wiki/concepts/micro-productivity-trap.md` | concept | 0.91 | task gains ≠ firm value; quote-generation case (15× faster, +10pp win rate) |

**Coverage gap:** No wiki source studies SME sales directly; sales evidence is from startups/vendors, SME evidence is about AI adoption generally.

## 6. Answer-element map
| Anchor | Answer element (claim) | Wiki page(s) | Section / span used |
|--------|------------------------|--------------|---------------------|
| [W1] | SME adoption barriers: money, specialists, expertise; positive ROI decisive | [[sources/2024-08-13-schwaeke-new-normal-ai-adoption-smes]] | ## Key claims (resources, compatibility, ROI) |
| [W2] | Readiness easy to build but does not pay; only implementation reaches performance | [[sources/2025-06-15-cimino-ai-adoption-sustainable-growth-smes]] | ## TL;DR; ### Three findings worth carrying §1 |
| [W3] | Human traffic −35–40% (Cloudflare); vendor-reported; agents may own shop–shopper relationship | [[concepts/agentic-web]] | ## Key claims §1 |
| [W4] | HubSpot −80% traffic (140M visits) while leads +20%; buyers research in ChatGPT/Claude | [[sources/2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook]] | ## Key claims §1 |
| [W5] | AEO definition; long specific prompts; consensus across web; buyers arrive at decision stage; low-tech measurement from sales/support questions | [[concepts/answer-engine-optimization]] | ## Working definition; ## How AEO differs from SEO; ## Key claims §1–2 |
| [W6] | AI discovery surfaces niche brands ("good story for the long tail"); agents will buy; speaker has commercial interest | [[sources/2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet]] | ## TL;DR §2 |
| [W7] | Intent vs curiosity; meetings as AI-evaluation theatre; no-tension calls; SPRINT niche/problem/results/implementation; buyer fear | [[sources/2026-06-24-rubinstein-onyemah-startup-founders-new-sales-playbook]] | ## TL;DR (headline shift, new challenges, SPRINT table) |
| [W8] | Lighthouse (proof) vs landgrab (math); Meraki mid-market and free trials; open question on AI trials | [[sources/2026-08-13-a16z-lighthouse-or-landgrab-ai-sales-strategy]] | ## The framework; ## The historical case: Meraki |
| [W9] | Micro-productivity trap; FabricationCo quoting ~15× faster, +10pp win rate in 3 months; redesign + measure | [[concepts/micro-productivity-trap]] | ## Working definition; ### Worked cases; four-step framework |

## 7. Final answer

# The implications of AI for SME sales

Most small and medium-sized businesses meet AI in sales as a tool, such as an assistant that drafts emails. The evidence suggests the bigger change is on the buyer's side: customers find suppliers in new places, are persuaded by different things, and sometimes send software to buy for them.

A caveat: most of this evidence comes from startups, investors and software vendors, often while selling a product. None of it was gathered on SME *sales* specifically. Read it as strong signals, not settled findings.

## 1. Buyers now research where you cannot see them

The clearest change is where buying starts. HubSpot reports losing 80% of its web traffic, 140 million visits in a year from May 2024, while its leads grew 20% [W4]. Its explanation is that buyers who used to read blog posts and download ebooks now have "those conversations with ChatGPT, with Claude" [W4]. Cloudflare, whose network carries more than a fifth of the web, measured human traffic down 35–40% between June 2025 and April 2026 in retail, software, IT services and financial services [W3]. Both figures are vendor-reported, and neither separates AI from other causes [W3].

A website and a decent Google ranking used to get an SME onto a shortlist. Increasingly, an AI system draws up that shortlist before the buyer visits any site. A buyer who does reach you often arrives ready to decide, because the engine has already done the comparing [W5].

## 2. Being named in the answer is the new visibility

A new discipline has grown up around this: answer engine optimisation (AEO), which means getting your business named and cited in the answers AI systems give [W5]. It differs from SEO in ways that help some SMEs and hurt others. Prompts are long and specific, such as "what are the best CRMs for SMBs in Spain?" rather than "best CRM", and that favours a firm with a clear niche over a generalist [W5]. But an engine recommends a brand only when the wider web agrees about it: reviews, press, social posts and other people's sites, not just your own pages [W5]. A small firm that barely exists outside its own website is hard for an engine to recommend.

You don't need a platform to start. Put the questions customers ask in sales calls and support tickets to the main AI assistants, and note whether you are named and who is named instead [W5].

## 3. The long tail may gain, if machines can read it

There is a hopeful reading for small businesses. Stripe co-founder John Collison argues that AI product research "often actually surfaces niche brands or businesses you haven't heard of", which he calls "quite a good story for the long tail" [W6]. He expects people's agents to make a large share of their purchases [W6]. This is a forecast from someone whose company gains if it comes true [W6]. Other sources expect agents to sit between shop and shopper and own the relationship instead [W3]. Either way, the practical requirement is the same: product information, prices and terms that a machine can read and compare.

## 4. Interest is cheap, and buyers are afraid

Once a conversation starts, selling has become harder in a specific way. Rubinstein and Onyemah interviewed more than 250 founders in over 30 countries. They found that the main problem in 2026 is "the growing inability to distinguish real buying intent from curiosity" [W7]. Prospects take meetings to show colleagues they are evaluating AI, so the pipeline looks full while holding little, and a pleasant call without tension rarely produces a deal [W7].

Their remedy suits SMEs, which seldom have the budget to compete on volume. Pick a narrow niche: "one buyer type, one problem, one motion that repeats". Describe the buyer's problem more precisely than the buyer can. Promise specific, observable outcomes. And answer the risk question before it is asked, because late in a deal the buyer's fear of AI failing in front of leadership is what kills it [W7].

## 5. Choose markets where your proof carries

a16z's "lighthouse or landgrab" framework adds a choice about whom to sell to [W8]. Where buyers are exposed and few, as in regulated sectors and among big names, you sell on proof from reference customers. Where buyers already have a budget for the service, you sell on the numbers compared with what they pay today, for people or for software [W8]. Meraki is the case most relevant to SMEs. Large corporations were locked up by Cisco and HP, so it won the mid-market by being simpler and faster to deploy, and gave away free trial hardware [W8]. It is an open question whether free trials work as proof for AI products that are hard to set up [W8].

## 6. AI inside your own sales team: watch for the trap

SMEs should still use AI in their own selling, within known limits. Research on SME AI adoption names money, specialists and expertise as the most-cited barriers, and a positive return as decisive [W1]. A survey of 210 small Italian startups found that willingness to adopt AI was easy to build but did not pay; only actual implementation improved performance [W2]. Firms that bolt AI onto existing tasks often get task-level gains that never reach the bottom line, a pattern called the "micro-productivity trap" [W9]. The counter-example comes from sales. A large manufacturer rebuilt its quoting around AI, produced quotes about 15 times faster, and raised its win rate by 10 percentage points in three months [W9]. The lesson is to redesign one sales workflow end to end and measure it against a baseline, rather than hand everyone a chatbot [W9].

## What this means for an SME

- **Find out what AI assistants say about you** and your competitors, using your customers' real questions [W5].
- **Build your presence beyond your own site**: reviews, partner pages, press [W5].
- **Narrow your offer** until a buyer, or an engine, can describe it in one sentence [W5][W7].
- **Sell on reduced risk and specific outcomes**, not on features [W7].
- **Redesign one sales process with AI** and measure the result [W9].

AI moves the first, invisible part of the sale out of your hands. What you still control is how clearly and consistently the world describes you, and how well you settle a nervous buyer's doubts once they arrive.

---

**Sources (wiki):** [W1] [[2024-08-13-schwaeke-new-normal-ai-adoption-smes|Schwaeke et al. 2024]] · [W2] [[2025-06-15-cimino-ai-adoption-sustainable-growth-smes|Cimino et al. 2025]] · [W3] [[agentic-web|Agentic web]] · [W4] [[2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook|Bodnar & Flanagan, HubSpot 2026]] · [W5] [[answer-engine-optimization|Answer engine optimization]] · [W6] [[2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet|Collison, Browserbase 2026]] · [W7] [[2026-06-24-rubinstein-onyemah-startup-founders-new-sales-playbook|Rubinstein & Onyemah, HBR 2026]] · [W8] [[2026-08-13-a16z-lighthouse-or-landgrab-ai-sales-strategy|a16z, Lighthouse or Landgrab 2026]] · [W9] [[micro-productivity-trap|Micro-productivity trap]]

## 8. Trace artifact
Machine-readable provenance: [`2026-10-12-implications-of-ai-for-sme-sales-query-trace.json`](2026-10-12-implications-of-ai-for-sme-sales-query-trace.json)
