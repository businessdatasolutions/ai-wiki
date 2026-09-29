---
type: query-trace
question: "Outline a 3-slide intro deck on AI Agents for the AI-in-Business module (with LRD)"
date: 2026-09-18
language: en
trace: "2026-09-18-ai-agents-intro-deck-outline-query-trace.json"
pages_used: 11
pages_ignored: 93
---

# Query trace — AI agents intro deck outline

## 1. Question
- **Original:** I need to give a concise introduction to my student of the ai-in-business course on AI Agents. Can you make an outline for a 3 page slide deck that gives the enough information to start? Here is the LRD of the whole module. Try and make references to related topics as much as possible. [LRD: https://datadrivendecisions.github.io/ai-in-business/integrated-lrd.html]
- **Restated:** Outline a three-slide introduction to AI agents for students of the integrated AIBS/AEL AI-in-Business module, cross-referencing the module weeks and related wiki concepts.
- **Facets:** 1) What an AI agent is (definition, autonomy, the loop, intern analogy) 2) How an agent is built (harness, simplicity, vibe coding vs agentic engineering) 3) What agents mean for a business/SME (where they pay off, trust and oversight, value capture) 4) Cross-references to the module weeks in the LRD
- **Retrieval query used:** `introduction to AI agents for business students: what is an agent, agent harness, agentic workflows, business adoption and risks` (the verbatim request is mostly about deck format; the query was framed around its content facets)
- **External input:** the integrated LRD (v1.8), read from the local copy of the URL the user supplied; it is not a wiki page and is cited as *LRD §…*.

## 2. Paths explored

qmd hits: 12 · candidates: 101 · graph available: True · hops: 1

**qmd hits** (relevance stream)

| # | Page | type | qmd score | fused | verdict |
|---|------|------|-----------|-------|---------|
| 1 | `wiki/sources/2009-01-01-wooldridge-introduction-to-multiagent-systems-ch1-2.md` | source | 1 | 0.940 | USE |
| 2 | `wiki/concepts/ai-agents.md` | concept | 0.630 | 0.964 | USE |
| 3 | `wiki/sources/2026-05-03-rewired-second-edition-sample.md` | source | 0.610 | 0.910 | IGNORE |
| 4 | `wiki/sources/2026-05-07-chatterjee-anatomy-of-agent-harness.md` | source | 0.610 | 0.858 | IGNORE |
| 5 | `wiki/sources/2026-05-15-osmani-agent-harness-engineering.md` | source | 0.610 | 0.882 | IGNORE |
| 6 | `wiki/concepts/industrial-ai-agents.md` | concept | 0.600 | 0.794 | USE |
| 7 | `wiki/sources/2024-12-19-anthropic-building-effective-agents.md` | source | 0.600 | 0.856 | USE |
| 8 | `wiki/sources/2026-07-10-building-the-future-of-agentic-infrastructure.md` | source | 0.600 | 0.843 | IGNORE |
| 9 | `wiki/sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs.md` | source | 0.600 | 0.831 | IGNORE |
| 10 | `wiki/sources/2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success.md` | source | 0.590 | 0.819 | IGNORE |
| 11 | `wiki/concepts/micro-productivity-trap.md` | concept | 0.570 | 0.835 | USE |
| 12 | `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | source | 0.540 | 0.779 | IGNORE |

**graph neighbours** (`--hops 1`, typed-edge stream)

| Page | reached via | hops | fused | verdict |
|------|-------------|------|-------|---------|
| `wiki/sources/2022-10-06-yao-et-al-react-synergizing-reasoning-acting.md` | sources/2009-01-01-wooldridge-introduction-to-multiagent-systems-ch1-2 --supports--> this | 1 | 0.470 | IGNORE |
| `wiki/sources/2025-03-17-cemri-why-do-multi-agent-llm-systems-fail.md` | sources/2009-01-01-wooldridge-introduction-to-multiagent-systems-ch1-2 --supports--> this | 1 | 0.462 | IGNORE |
| `wiki/sources/2026-05-14-pochampally-assistant-or-actor-delegation-regret.md` | sources/2009-01-01-wooldridge-introduction-to-multiagent-systems-ch1-2 --supports--> this | 1 | 0.455 | IGNORE |
| `wiki/sources/2026-05-18-wolfe-agent-evaluation-detailed-guide.md` | sources/2009-01-01-wooldridge-introduction-to-multiagent-systems-ch1-2 --supports--> this | 1 | 0.448 | IGNORE |
| `wiki/sources/2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness.md` | sources/2009-01-01-wooldridge-introduction-to-multiagent-systems-ch1-2 --contradicts--> this | 1 | 0.441 | IGNORE |
| `wiki/sources/2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1.md` | sources/2009-01-01-wooldridge-introduction-to-multiagent-systems-ch1-2 --supports--> this | 1 | 0.434 | IGNORE |
| `wiki/concepts/agent-harness.md` | concepts/ai-agents --part-of--> this | 1 | 0.433 | USE |
| `wiki/sources/2026-08-19-he-databricks-anthropic-primitives-to-production-agents.md` | sources/2009-01-01-wooldridge-introduction-to-multiagent-systems-ch1-2 --supports--> this | 1 | 0.428 | IGNORE |
| `wiki/concepts/generative-ai.md` | concepts/ai-agents --instance-of--> this | 1 | 0.414 | IGNORE |
| `wiki/concepts/foundation-models.md` | concepts/ai-agents --uses--> this | 1 | 0.410 | IGNORE |
| `wiki/concepts/react-reasoning-acting.md` | concepts/ai-agents --uses--> this | 1 | 0.407 | USE |
| `wiki/concepts/agent-development-lifecycle.md` | concepts/ai-agents --part-of--> this | 1 | 0.406 | IGNORE |
| `wiki/concepts/multi-agent-failure-modes.md` | concepts/ai-agents --part-of--> this | 1 | 0.377 | USE |
| `wiki/concepts/small-language-models.md` | concepts/ai-agents --uses--> this | 1 | 0.372 | IGNORE |
| `wiki/sources/2026-05-12-techlatest-hacker-search-engines-osint-tools-2026.md` | concepts/ai-agents --uses--> this | 1 | 0.372 | IGNORE |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | sources/2026-05-03-rewired-second-edition-sample --supports--> this | 1 | 0.368 | IGNORE |
| `wiki/concepts/graph-engineering.md` | concepts/ai-agents --uses--> this | 1 | 0.367 | IGNORE |
| `wiki/concepts/industry-4-0.md` | concepts/ai-agents --uses--> this | 1 | 0.364 | IGNORE |
| `wiki/sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage.md` | sources/2026-05-03-rewired-second-edition-sample --supports--> this | 1 | 0.363 | IGNORE |
| `wiki/sources/2025-07-31-wang-agentspec-runtime-enforcement-llm-agents.md` | sources/2026-05-07-chatterjee-anatomy-of-agent-harness --supports--> this | 1 | 0.358 | IGNORE |
| `wiki/sources/2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness.md` | sources/2026-05-07-chatterjee-anatomy-of-agent-harness --supports--> this | 1 | 0.354 | IGNORE |
| `wiki/sources/2026-05-11-karten-zhang-continual-harness-online-adaptation.md` | sources/2026-05-07-chatterjee-anatomy-of-agent-harness --supports--> this | 1 | 0.350 | IGNORE |
| `wiki/sources/2026-06-08-vincent-coderabbit-fixing-ai-slop-managing-agents-like-mit-interns.md` | sources/2026-05-07-chatterjee-anatomy-of-agent-harness --supports--> this | 1 | 0.341 | IGNORE |
| `wiki/sources/2026-06-22-grinstead-how-i-ai-mozilla-firefox-agentic-security-harness.md` | sources/2026-05-07-chatterjee-anatomy-of-agent-harness --supports--> this | 1 | 0.337 | IGNORE |
| `wiki/sources/2025-11-26-anthropic-effective-harnesses-long-running-agents.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.333 | IGNORE |
| `wiki/sources/2026-06-03-chopra-headroom-context-optimization-layer-for-llm-applications.md` | sources/2026-05-07-chatterjee-anatomy-of-agent-harness --supports--> this | 1 | 0.331 | IGNORE |
| `wiki/sources/2026-02-17-langchain-improving-deep-agents-harness-engineering.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.330 | IGNORE |
| `wiki/sources/2026-03-26-osmani-code-agent-orchestra-multi-agent-coding.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.326 | IGNORE |
| `wiki/sources/2026-03-30-lee-meta-harness-end-to-end-optimization.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.322 | IGNORE |
| `wiki/sources/2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.319 | IGNORE |
| `wiki/sources/2026-05-05-loukides-radar-trends-may-2026.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.315 | IGNORE |
| `wiki/sources/2026-02-11-lopopolo-codex-harness-engineering.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.312 | IGNORE |
| `wiki/sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.302 | IGNORE |
| `wiki/sources/2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.302 | IGNORE |
| `wiki/sources/2026-05-07-anthropic-managed-agents-decoupling-brain-hands.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.299 | IGNORE |
| `wiki/sources/2026-05-08-bratanic-unified-agentic-memory-hooks.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.293 | IGNORE |
| `wiki/sources/2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.287 | IGNORE |
| `wiki/sources/2026-05-04-rethinking-agents-harness-is-all-you-need.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.286 | IGNORE |
| `wiki/sources/2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.284 | IGNORE |
| `wiki/sources/2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.281 | IGNORE |
| `wiki/sources/2026-09-02-github-podcast-demystifying-ai-terms-loop-engineering-squads-harness.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.278 | IGNORE |
| `wiki/sources/2026-05-07-kokane-agent-harness-vs-systems-design.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.277 | IGNORE |
| `wiki/sources/2026-05-19-garg-yc-internal-ai-agent-evolves-itself.md` | sources/2026-05-15-osmani-agent-harness-engineering --supports--> this | 1 | 0.277 | IGNORE |
| `wiki/sources/2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide.md` | concepts/industrial-ai-agents --supports--> this | 1 | 0.276 | IGNORE |
| `wiki/sources/2026-03-26-pan-natural-language-agent-harnesses.md` | sources/2024-12-19-anthropic-building-effective-agents --supports--> this | 1 | 0.273 | IGNORE |
| `wiki/sources/2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail.md` | sources/2024-12-19-anthropic-building-effective-agents --supports--> this | 1 | 0.270 | IGNORE |
| `wiki/sources/2026-06-17-priest-atlantic-pwc-ai-agents-changing-business.md` | sources/2026-07-10-building-the-future-of-agentic-infrastructure --supports--> this | 1 | 0.268 | IGNORE |
| `wiki/sources/2026-07-08-jensen-huang-why-companies-need-open-agent-systems.md` | sources/2026-07-10-building-the-future-of-agentic-infrastructure --supports--> this | 1 | 0.265 | IGNORE |
| `wiki/sources/2026-07-19-why-netflix-is-betting-on-systems-thinkers-not-specialists-in-the-ai-era.md` | sources/2026-07-10-building-the-future-of-agentic-infrastructure --supports--> this | 1 | 0.263 | IGNORE |
| `wiki/sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.258 | IGNORE |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.256 | IGNORE |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.254 | IGNORE |
| `wiki/sources/2026-04-28-brynjolfsson-canaries-coal-mine.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.251 | IGNORE |
| `wiki/sources/2026-05-01-lf-state-of-tech-talent-global-2026.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.250 | IGNORE |
| `wiki/sources/2026-04-30-ai-index-report-2026.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.249 | IGNORE |
| `wiki/sources/2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.245 | IGNORE |
| `wiki/sources/2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.243 | IGNORE |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.242 | IGNORE |
| `wiki/sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --contradicts--> this | 1 | 0.241 | IGNORE |
| `wiki/sources/2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.239 | IGNORE |
| `wiki/sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.235 | IGNORE |
| `wiki/sources/2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.233 | IGNORE |
| `wiki/sources/2026-06-22-bbc-what-if-were-wrong-about-ai-layoffs.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.231 | IGNORE |
| `wiki/sources/2022-06-29-martin-hbr-a-plan-is-not-a-strategy.md` | sources/2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success --supports--> this | 1 | 0.228 | IGNORE |
| `wiki/sources/2026-06-01-lf-state-of-tech-talent-europe-2026.md` | sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs --supports--> this | 1 | 0.227 | IGNORE |
| `wiki/concepts/enterprise-ai-adoption.md` | concepts/micro-productivity-trap --caused--> this | 1 | 0.227 | IGNORE |
| `wiki/sources/2026-02-01-manditereza-ontology-driven-industrial-ai.md` | sources/2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success --supports--> this | 1 | 0.226 | IGNORE |
| `wiki/sources/2026-05-15-sterman-systems-thinking-for-leaders-designing-solutions-that-work.md` | sources/2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success --supports--> this | 1 | 0.224 | IGNORE |
| `wiki/concepts/automation-vs-augmentation.md` | concepts/micro-productivity-trap --contradicts--> this | 1 | 0.224 | IGNORE |
| `wiki/concepts/ai-coding-productivity-evidence.md` | concepts/micro-productivity-trap --supports--> this | 1 | 0.220 | IGNORE |
| `wiki/sources/2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers.md` | concepts/micro-productivity-trap --supports--> this | 1 | 0.216 | IGNORE |
| `wiki/entities/MIT-Sloan-Executive-Education.md` | sources/2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success --published-by--> this | 1 | 0.215 | IGNORE |
| `wiki/sources/2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs.md` | concepts/micro-productivity-trap --supports--> this | 1 | 0.214 | IGNORE |
| `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | concepts/micro-productivity-trap --supports--> this | 1 | 0.213 | IGNORE |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | concepts/micro-productivity-trap --supports--> this | 1 | 0.212 | IGNORE |
| `wiki/sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era.md` | concepts/micro-productivity-trap --supports--> this | 1 | 0.211 | IGNORE |
| `wiki/concepts/ai-knowledge-hiding.md` | concepts/micro-productivity-trap --supports--> this | 1 | 0.209 | IGNORE |
| `wiki/entities/Google.md` | sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer --published-by--> this | 1 | 0.209 | IGNORE |
| `wiki/sources/2025-06-09-krakowski-human-centered-ai-field-experiment.md` | sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer --supports--> this | 1 | 0.206 | IGNORE |
| `wiki/sources/2025-07-02-joshi-venkatraman-fowler-expert-generalists.md` | sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer --supports--> this | 1 | 0.205 | IGNORE |
| `wiki/sources/2026-05-07-globerson-et-al-scalable-measurement-durable-skills.md` | sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer --supports--> this | 1 | 0.203 | IGNORE |
| `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` | sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer --supports--> this | 1 | 0.200 | IGNORE |
| `wiki/sources/2026-05-07-kiron-schrage-compound-benefits.md` | sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer --supports--> this | 1 | 0.198 | IGNORE |
| `wiki/sources/2026-05-09-chase-agent-development-lifecycle.md` | sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer --supports--> this | 1 | 0.198 | IGNORE |
| `wiki/sources/2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai.md` | sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer --supports--> this | 1 | 0.196 | IGNORE |
| `wiki/sources/2026-05-08-running-an-ai-native-engineering-org.md` | sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer --supports--> this | 1 | 0.195 | IGNORE |
| `wiki/sources/2026-05-21-bender-google-io-software-engineering-tipping-point.md` | sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer --supports--> this | 1 | 0.195 | IGNORE |
| `wiki/sources/2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering.md` | sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer --supports--> this | 1 | 0.194 | IGNORE |
| `wiki/sources/2026-06-24-mckinsey-ai-supercharging-software-development.md` | sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer --supports--> this | 1 | 0.192 | IGNORE |

**index.md / gap-expansion** (Step 5)

| Page | why added |
|------|-----------|
| `wiki/concepts/agent-oversight-and-delegation.md` | named in LRD Part 8 concept column (AIBS/AEL weeks); not surfaced by retrieval; located by name in index.md |
| `wiki/concepts/agentic-engineering.md` | named in LRD Part 8 concept column (AIBS/AEL weeks); not surfaced by retrieval; located by name in index.md |
| `wiki/concepts/vibe-coding.md` | named in LRD Part 8 concept column (AIBS/AEL weeks); not surfaced by retrieval; located by name in index.md |

## 3. Ignore policy applied

- `below-threshold` — low fused score, graph-only long-tail neighbour, no facet needs it.
- `off-facet` — adjacent, but addresses none of the four facets at intro altitude — or is AEL debrief reading the LRD says not to pre-teach.
- `redundant` — a USE page already synthesises the same claim; keep the stronger page, ignore the echo.
- `wrong-granularity` — entity catalogue card where the facet needs a claim.
- Graph-only candidates needed a higher bar; three were kept (agent-harness, react-reasoning-acting, multi-agent-failure-modes) because they are the synthesised concept pages for facets 1–2.
- The one `contradicts` edge touching a USE page (Wooldridge ↔ Baugues on whether the LLM belongs in the definition) is carried as content on slide 1 via concepts/ai-agents, so the Baugues source itself is `redundant`.

## 4. Information ignored

| Page | reason-class | one-line reason |
|------|--------------|-----------------|
| `wiki/sources/2026-05-03-rewired-second-edition-sample.md` | off-facet | digital-transformation playbook; agents incidental to it |
| `wiki/sources/2026-05-15-osmani-agent-harness-engineering.md` | redundant | synthesised on concepts/agent-harness (W5) |
| `wiki/sources/2026-05-07-chatterjee-anatomy-of-agent-harness.md` | redundant | 4-C anatomy and Friday-in-March case carried on concepts/agent-harness (W5) |
| `wiki/sources/2026-07-10-building-the-future-of-agentic-infrastructure.md` | off-facet | vendor infrastructure outlook; not needed for an intro |
| `wiki/sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs.md` | off-facet | labour-market framing belongs to AIBS wk5 employment, not the agent intro |
| `wiki/sources/2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success.md` | redundant | Carrier heuristics carried on concepts/industrial-ai-agents (W9) |
| `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | off-facet | developer skills, not agent definition or business use |
| `wiki/sources/2022-10-06-yao-et-al-react-synergizing-reasoning-acting.md` | redundant | primary paper synthesised on concepts/react-reasoning-acting (W4) |
| `wiki/sources/2025-03-17-cemri-why-do-multi-agent-llm-systems-fail.md` | redundant | MAST carried on concepts/multi-agent-failure-modes (W8) |
| `wiki/sources/2026-05-14-pochampally-assistant-or-actor-delegation-regret.md` | redundant | delegation regret carried on concepts/agent-oversight-and-delegation (W6) |
| `wiki/sources/2026-05-18-wolfe-agent-evaluation-detailed-guide.md` | off-facet | agent evaluation detail; AEL wk4 debrief material, not intro |
| `wiki/sources/2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness.md` | redundant | contradicts-edge to Wooldridge (LLM in the definition or not) is reproduced on concepts/ai-agents four-clause section (W1); slide 1 shows both sides |
| `wiki/sources/2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1.md` | redundant | course-altitude definition summarised on concepts/ai-agents (W1) |
| `wiki/sources/2026-08-19-he-databricks-anthropic-primitives-to-production-agents.md` | redundant | who-chooses-the-trajectory progression summarised on concepts/ai-agents (W1) |
| `wiki/concepts/generative-ai.md` | below-threshold | parent category; no facet needs it |
| `wiki/concepts/foundation-models.md` | below-threshold | covered by the harness CPU analogy |
| `wiki/concepts/agent-development-lifecycle.md` | off-facet | AEL wk4 debrief reading; pre-teaching it contradicts LRD Part 8 |
| `wiki/concepts/small-language-models.md` | below-threshold | AIBS wk3 local-model question; not an intro facet |
| `wiki/sources/2026-05-12-techlatest-hacker-search-engines-osint-tools-2026.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/concepts/graph-engineering.md` | below-threshold | beyond intro altitude |
| `wiki/concepts/industry-4-0.md` | below-threshold | industrial framing covered by W9 |
| `wiki/sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2025-07-31-wang-agentspec-runtime-enforcement-llm-agents.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-11-karten-zhang-continual-harness-online-adaptation.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-06-08-vincent-coderabbit-fixing-ai-slop-managing-agents-like-mit-interns.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-06-22-grinstead-how-i-ai-mozilla-firefox-agentic-security-harness.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2025-11-26-anthropic-effective-harnesses-long-running-agents.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-06-03-chopra-headroom-context-optimization-layer-for-llm-applications.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-02-17-langchain-improving-deep-agents-harness-engineering.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-03-26-osmani-code-agent-orchestra-multi-agent-coding.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-03-30-lee-meta-harness-end-to-end-optimization.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-05-loukides-radar-trends-may-2026.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-02-11-lopopolo-codex-harness-engineering.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-07-anthropic-managed-agents-decoupling-brain-hands.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-08-bratanic-unified-agentic-memory-hooks.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-04-rethinking-agents-harness-is-all-you-need.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-09-02-github-podcast-demystifying-ai-terms-loop-engineering-squads-harness.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-07-kokane-agent-harness-vs-systems-design.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-19-garg-yc-internal-ai-agent-evolves-itself.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-03-26-pan-natural-language-agent-harnesses.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-06-17-priest-atlantic-pwc-ai-agents-changing-business.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-07-08-jensen-huang-why-companies-need-open-agent-systems.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-07-19-why-netflix-is-betting-on-systems-thinkers-not-specialists-in-the-ai-era.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-04-28-brynjolfsson-canaries-coal-mine.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-01-lf-state-of-tech-talent-global-2026.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-04-30-ai-index-report-2026.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-06-22-bbc-what-if-were-wrong-about-ai-layoffs.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2022-06-29-martin-hbr-a-plan-is-not-a-strategy.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-06-01-lf-state-of-tech-talent-europe-2026.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/concepts/enterprise-ai-adoption.md` | off-facet | adoption breadth is AIBS wk2/wk4 material, not agent intro |
| `wiki/sources/2026-02-01-manditereza-ontology-driven-industrial-ai.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-15-sterman-systems-thinking-for-leaders-designing-solutions-that-work.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/concepts/automation-vs-augmentation.md` | off-facet | contradicts-edge from micro-productivity-trap concerns productivity framing (AIBS wk5), not what an agent is; named via LRD only |
| `wiki/concepts/ai-coding-productivity-evidence.md` | off-facet | coding-productivity evidence; not an intro facet |
| `wiki/sources/2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/entities/MIT-Sloan-Executive-Education.md` | wrong-granularity | publisher card |
| `wiki/sources/2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | off-facet | adoption frameworks (AIBS wk4), not agents |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-07-singhal-stanford-cs153-product-management-in-ai-era.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/concepts/ai-knowledge-hiding.md` | off-facet | AIBS wk3 people dimension; not needed for 3 slides |
| `wiki/entities/Google.md` | wrong-granularity | organisation card |
| `wiki/sources/2025-06-09-krakowski-human-centered-ai-field-experiment.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2025-07-02-joshi-venkatraman-fowler-expert-generalists.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-07-globerson-et-al-scalable-measurement-durable-skills.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-07-kiron-schrage-compound-benefits.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-09-chase-agent-development-lifecycle.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-08-running-an-ai-native-engineering-org.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-21-bender-google-io-software-engineering-tipping-point.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |
| `wiki/sources/2026-06-24-mckinsey-ai-supercharging-software-development.md` | below-threshold | graph-only long-tail neighbour, low fused score, no facet needs it |

## 5. Information used

| Anchor | Page | type | effConf | contribution |
|---|------|------|---------|--------------|
| W1 | `wiki/concepts/ai-agents.md` | concept | 0.950 | working definition, 3-stage ladder, intern entities, four-clause definition, CIO reality check, no-regrets zone |
| W2 | `wiki/sources/2009-01-01-wooldridge-introduction-to-multiagent-systems-ch1-2.md` | source | — | implementation-neutral definition; autonomy = deciding how, not what |
| W3 | `wiki/sources/2024-12-19-anthropic-building-effective-agents.md` | source | — | workflows vs agents; start simple; proven domains (support, coding) |
| W7 | `wiki/concepts/micro-productivity-trap.md` | concept | 0.929 | task-level gains without firm-level value |
| W9 | `wiki/concepts/industrial-ai-agents.md` | concept | 0.649 | data grounding as binding problem; pick-the-right-agent-level; stub |
| W5 | `wiki/concepts/agent-harness.md` | concept | 0.950 | harness definition, 4 Cs, OS analogy, rented vs owned, Friday-in-March failure |
| W4 | `wiki/concepts/react-reasoning-acting.md` | concept | 0.900 | reason-act-observe loop; legible thoughts enable correction |
| W8 | `wiki/concepts/multi-agent-failure-modes.md` | concept | 0.850 | add agents only when one context window stops being enough |
| W6 | `wiki/concepts/agent-oversight-and-delegation.md` | concept | — | delegation regret; irreversible x externally visible; preview over permission *(gap-expansion)* |
| W10 | `wiki/concepts/agentic-engineering.md` | concept | — | raises the ceiling; quality bar at agent speed *(gap-expansion)* |
| W11 | `wiki/concepts/vibe-coding.md` | concept | — | raises the floor; democratisation *(gap-expansion)* |

## 6. Answer-element map

| Anchor | Answer element (claim) | Wiki page(s) | Section / span used |
|--------|------------------------|--------------|---------------------|
| [W1] | Four-clause agent definition shared by Google and Anthropic; chatbot→agent→multi-agent ladder; intern entities; no-regrets zone; CIO reality check / performative oversight | [[concepts/ai-agents]] | ## Working definition; ## The four-clause definition…; ### The human-agent collaboration reality |
| [W2] | Implementation-neutral definition; delegate what, agent decides how | [[sources/2009-01-01-wooldridge-introduction-to-multiagent-systems-ch1-2]] | ## TL;DR |
| [W3] | Workflows vs agents (who decides next step); start simple; support + coding as proven domains | [[sources/2024-12-19-anthropic-building-effective-agents]] | ## TL;DR |
| [W4] | Reason→act→observe loop; legible thoughts allow correction | [[concepts/react-reasoning-acting]] | ## The core mechanism; ## Why it mattered |
| [W5] | Harness definition, 4 Cs, OS analogy, model rented/harness owned, Friday-in-March failure | [[concepts/agent-harness]] | ## Working definition; ### The operating-system analogy; ### The model is rented…; ### The Friday-in-March pattern |
| [W6] | Delegation regret; irreversible × externally visible trigger; preview over permission | [[concepts/agent-oversight-and-delegation]] | ## The failure mode that is not about accuracy; ## Three findings… |
| [W7] | Task-level gains fail to become firm-level value | [[concepts/micro-productivity-trap]] | ## Working definition |
| [W8] | Multiple agents only when one context window is not enough | [[concepts/multi-agent-failure-modes]] | ## The deflation |
| [W9] | Industrial agents: data grounding is the binding problem; pick the right agent level; page is a stub | [[concepts/industrial-ai-agents]] | ## Working definition; ### Pick-the-right-agent-level heuristic |
| [W10] | Agentic engineering raises the ceiling | [[concepts/agentic-engineering]] | ## Working definition |
| [W11] | Vibe coding raises the floor | [[concepts/vibe-coding]] | ## Working definition; ### Vibe coding raises the floor |

## 7. Final answer

**Deck: "AI Agents — what they are, how they're built, what they mean for an SME"** (3 slides, for the week-1 plenary of the integrated AIBS/AEL module)

References marked *LRD §…* point to the module's integrated LRD (external document, not a wiki page). Everything marked `[W#]` is a wiki page.

---

### Slide 1 — What is an AI agent? *(the intern you delegate a goal to)*

- **The definition.** The working definition is *"an LLM with tools running in a loop to accomplish a goal."* By mid-2026 Google and Anthropic developer material both use it [W1]. The older textbook definition leaves the LLM out: *"a computer system situated in some environment, capable of autonomous action … to meet its delegated objectives"* [W2]. Show both, because the gap between them is a good first question for students.
- **The ladder.** Chatbot (conversation) → agent (pursues goals autonomously, plans, adapts) → multi-agent system (several agents collaborating) [W1].
- **Where the line falls: who decides the next step.** In a *workflow*, code sets the path. In an *agent*, the model directs its own process and tool use [W3]. Wooldridge draws the same line fifteen years earlier: you delegate *what*, and the agent decides *how* [W2].
- **The loop under the hood.** Reason → act → observe → adjust. This is ReAct (2022), and the thoughts it writes down are what let a human inspect and correct the agent [W4].
- **The anchor metaphor.** The intern analogy stays unchanged as the week-1 anchor (*LRD App. A.1, Part 8 wk 1*). The wiki backs it up: Karpathy calls agents *intern entities* that need a human *"in charge of the aesthetics, the judgment, the taste, and a little bit of oversight"* [W1].
- **Links:** AIBS wk 1 (intern analogy, problem analysis). AEL wk 2 debrief (ReAct).

### Slide 2 — How is an agent built? *(the model is rented, the harness is owned)*

- **Model plus harness.** The harness is the software that turns a model into a system that can pursue goals reliably [W5]. Analogy: the LLM is the CPU, the context window is the RAM, tools are the device drivers, and the harness is the operating system [W5].
- **The business argument.** *"The model is rented … the harness is what we own and what compounds."* [W5] This connects AEL to AIBS wk 2 (vendor business models, dependency).
- **Most failures happen in the harness, not the model.** In the "Friday in March" case, an agent told to *"clean things up"* archived two weeks of research. The model had reasoned correctly. The missing piece was a layer that recognised a destructive intent and asked first [W5].
- **Start simple.** *"Find the simplest solution possible … this might mean not building agentic systems at all."* [W3] Industrial practice says the same: *"no reason to jump to a level five agent when a simple rule-based agent will do"* [W9]. Add more agents only when one context window is no longer enough [W8].
- **Vibe coding versus agentic engineering.** Vibe coding raises the floor (anyone can build). Agentic engineering raises the ceiling (building fast *without* lowering quality) [W10][W11]. This is AEL's arc: vibe-coded spike in wk 1, ratchet retrospective in wk 7 (*LRD Part 8*).
- **Roadmap only (don't pre-teach):** Context · Constraints · Contracts · Compounding [W5] map onto AEL wk 2 / 5 / 4 / 6 (*LRD Part 8*). Show the four names as the route. The LRD makes the harness pages **debrief reading** and says handing them out in advance "removes the failure that gives each element its point" (*LRD Part 8, AEL column*).

### Slide 3 — What does it mean for a business? *(value, trust, and where to keep a human)*

- **Where agents pay off today.** In the low-error-cost, explicit-data *"no regrets zone"*, such as bulk inquiries, summaries and screening [W1]. Customer support and coding are the proven domains [W3].
- **The reality check.** Leaders report *"you have to check the output, recheck the output, re-prompt it."* They also warn about *performative oversight*: review that degrades into rubber-stamping [W1]. The same failure mode is in the LRD's risk register: a team deferring to its own agent's output (*LRD Part 12*).
- **Trust and delegation.** Users regret an agent that acted *beyond what they would have authorised*, even when the result was correct. The trigger is **irreversible × externally visible** (sending an email, for example), and preview works better than up-front permission [W6]. Links: AIBS wk 3 (can the SME trust AI?) and AEL wk 5 (hooks before a tool call).
- **Value is not automatic.** In the micro-productivity trap, tasks get faster and the firm doesn't gain, because the workflow around the task stays the same [W7]. Links: AIBS wk 5 and wk 6 (*LRD Part 8*: the productivity-trap page returns as the test for a claimed success).
- **Industrial SMEs.** For industrial SMEs the hard part is grounding scattered operational data (MES/ERP/SCADA), not engineering around the model [W9]. This is thin ground: the page is a single-source stub [W9]. Link: AIBS wk 6.
- **Closing line:** "Your team will build its own agent this semester (the research platform) and be questioned weekly by another one (the Socratic tutor)" (*LRD §1.2, §6.1, §6.4*).

---

**Gaps to know about:** the wiki has no page on the agent-to-regulation link (EU AI Act / Draghi, AIBS wk 2), and *loop engineering* has no page of its own. The LRD records both (*LRD Part 8 notes*). `industrial-ai-agents` is a stub [W9].

**Wiki pages cited:** [W1] [[ai-agents|AI Agents]] · [W2] [[2009-01-01-wooldridge-introduction-to-multiagent-systems-ch1-2|Wooldridge 2009]] · [W3] [[2024-12-19-anthropic-building-effective-agents|Anthropic — Building effective agents]] · [W4] [[react-reasoning-acting|ReAct]] · [W5] [[agent-harness|Agent harness]] · [W6] [[agent-oversight-and-delegation|Agent oversight and delegation]] · [W7] [[micro-productivity-trap|Micro-productivity trap]] · [W8] [[multi-agent-failure-modes|Multi-agent failure modes]] · [W9] [[industrial-ai-agents|Industrial AI agents]] · [W10] [[agentic-engineering|Agentic engineering]] · [W11] [[vibe-coding|Vibe coding]]


## 8. Trace artifact
Machine-readable provenance: [`2026-09-18-ai-agents-intro-deck-outline-query-trace.json`](2026-09-18-ai-agents-intro-deck-outline-query-trace.json)
