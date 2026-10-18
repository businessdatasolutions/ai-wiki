---
type: query-trace
question: "Wat zegt de wiki over world models, synthetische data en de datakloof bij robotica?"
date: 2026-10-15
language: nl
trace: "2026-10-15-world-models-synthetische-data-robotica-query-trace.json"
pages_used: 10
pages_ignored: 83
---

# Query trace — World models, synthetische data en de datakloof bij robotica

## 1. Question
- **Original:** Wat zegt de wiki over world models, synthetische data en de datakloof bij robotica?
- **Restated:** Wat zegt de wiki over world models, over synthetische versus echte data, en over de kloof tussen simulatie en de echte wereld bij robotica?
- **Facets:** 1) world models: definitie, spelers, verwachtingen 2) synthetische versus echte data 3) sim-to-real/datakloof bij robotica en embodied agents

## 2. Paths explored
Retrieval: `node scripts/wiki-retrieve.mjs --no-bump --json -n 12 "<question>"` (graph available: true; 11 qmd hits, 85 candidates). `--no-bump` because the caller forbade modifying wiki pages.

**qmd hits** (relevance stream)
| # | Page | type | qmd score | fused | verdict |
|---|------|------|-----------|-------|---------|
| 1 | `wiki/sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering.md` | source | 1.00 | 0.92 | IGNORE |
| 2 | `wiki/sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company.md` | source | 0.50 | 0.93 | IGNORE |
| 3 | `wiki/concepts/ai-agents.md` | concept | 0.33 | 0.94 | IGNORE |
| 4 | `wiki/concepts/llm-wiki.md` | concept | 0.25 | 0.92 | IGNORE |
| 5 | `wiki/sources/2026-02-01-manditereza-ontology-driven-industrial-ai.md` | source | 0.20 | 0.88 | IGNORE |
| 6 | `wiki/concepts/software-3.0.md` | concept | 0.14 | 0.80 | IGNORE |
| 7 | `wiki/concepts/industrial-ai-agents.md` | concept | 0.13 | 0.79 | USE |
| 8 | `wiki/sources/2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era.md` | source | 0.11 | 0.84 | IGNORE |
| 9 | `wiki/concepts/agent-harness.md` | concept | 0.10 | 0.85 | IGNORE |
| 10 | `wiki/sources/2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained.md` | source | 0.09 | 0.82 | IGNORE |
| 11 | `wiki/sources/2026-05-11-huber-chroma-rag-is-dead-agentic-search.md` | source | 0.08 | 0.81 | IGNORE |

**graph neighbours** (`--hops 1`, typed-edge stream)
| Page | reached via | hops | fused | verdict |
|------|-------------|------|-------|---------|
| `wiki/sources/2026-01-09-baron-signals-for-2026.md` | sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering --supports--> this | 1 | 0.46 | IGNORE |
| `wiki/sources/2026-04-11-nodus-labs-fix-karpathys-llm-wiki-knowledge-graph-infranodus.md` | sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering --supports--> this | 1 | 0.45 | IGNORE |
| `wiki/entities/Andrej-Karpathy.md` | sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering --authored-by--> this | 1 | 0.44 | IGNORE |
| `wiki/entities/Sequoia-Capital.md` | sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering --published-by--> this | 1 | 0.43 | IGNORE |
| `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering --supports--> this | 1 | 0.43 | IGNORE |
| `wiki/sources/2026-05-15-osmani-agent-harness-engineering.md` | sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering --supports--> this | 1 | 0.43 | IGNORE |
| `wiki/sources/2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer.md` | sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering --supports--> this | 1 | 0.42 | IGNORE |
| `wiki/sources/2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering.md` | sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering --supports--> this | 1 | 0.42 | IGNORE |
| `wiki/sources/2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering.md` | sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering --supports--> this | 1 | 0.41 | IGNORE |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering --supports--> this | 1 | 0.41 | IGNORE |
| `wiki/sources/2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook.md` | sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering --supports--> this | 1 | 0.40 | IGNORE |
| `wiki/sources/2026-09-30-demaree-onebrief-ai-military-planning.md` | sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering --supports--> this | 1 | 0.40 | IGNORE |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company --supports--> this | 1 | 0.39 | IGNORE |
| `wiki/sources/2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals.md` | sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company --supports--> this | 1 | 0.39 | IGNORE |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company --supports--> this | 1 | 0.38 | IGNORE |
| `wiki/sources/2026-05-05-nishar-nohria-end-of-one-size-fits-all.md` | sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company --supports--> this | 1 | 0.38 | IGNORE |
| `wiki/sources/2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero.md` | sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company --supports--> this | 1 | 0.37 | IGNORE |
| `wiki/sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs.md` | sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company --supports--> this | 1 | 0.37 | IGNORE |
| `wiki/sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going.md` | sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company --supports--> this | 1 | 0.36 | IGNORE |
| `wiki/sources/2026-07-31-collison-yc-startup-school-is-ai-breaking-the-lean-startup-playbook.md` | sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company --supports--> this | 1 | 0.36 | IGNORE |
| `wiki/concepts/agent-development-lifecycle.md` | concepts/ai-agents --part-of--> this | 1 | 0.35 | IGNORE |
| `wiki/concepts/foundation-models.md` | concepts/ai-agents --uses--> this | 1 | 0.35 | IGNORE |
| `wiki/concepts/agentic-web.md` | concepts/ai-agents --depends-on--> this | 1 | 0.34 | IGNORE |
| `wiki/concepts/generative-ai.md` | concepts/ai-agents --instance-of--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-05-12-techlatest-hacker-search-engines-osint-tools-2026.md` | concepts/ai-agents --uses--> this | 1 | 0.32 | IGNORE |
| `wiki/concepts/small-language-models.md` | concepts/ai-agents --uses--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks.md` | concepts/llm-wiki --supports--> this | 1 | 0.32 | IGNORE |
| `wiki/sources/2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers.md` | concepts/llm-wiki --supports--> this | 1 | 0.31 | IGNORE |
| `wiki/concepts/react-reasoning-acting.md` | concepts/ai-agents --uses--> this | 1 | 0.31 | IGNORE |
| `wiki/sources/2026-06-12-mcveety-hormati-google-cloud-open-knowledge-format.md` | concepts/llm-wiki --instance-of--> this | 1 | 0.31 | IGNORE |
| `wiki/concepts/vibe-coding.md` | concepts/software-3.0 --instance-of--> this | 1 | 0.30 | IGNORE |
| `wiki/sources/2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success.md` | sources/2026-02-01-manditereza-ontology-driven-industrial-ai --supports--> this | 1 | 0.30 | IGNORE |
| `wiki/concepts/agentic-engineering.md` | concepts/software-3.0 --instance-of--> this | 1 | 0.29 | IGNORE |
| `wiki/concepts/multi-agent-failure-modes.md` | concepts/ai-agents --part-of--> this | 1 | 0.29 | IGNORE |
| `wiki/sources/2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide.md` | concepts/industrial-ai-agents --supports--> this | 1 | 0.29 | IGNORE |
| `wiki/concepts/graph-engineering.md` | concepts/ai-agents --uses--> this | 1 | 0.29 | IGNORE |
| `wiki/sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships.md` | sources/2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era --supports--> this | 1 | 0.29 | IGNORE |
| `wiki/concepts/industry-4-0.md` | concepts/ai-agents --uses--> this | 1 | 0.28 | IGNORE |
| `wiki/sources/2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering.md` | sources/2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era --supports--> this | 1 | 0.28 | IGNORE |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | sources/2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era --supports--> this | 1 | 0.28 | IGNORE |
| `wiki/concepts/open-source-ai.md` | concepts/agent-harness --supports--> this | 1 | 0.28 | IGNORE |
| `wiki/syntheses/is-rag-dead.md` | concepts/llm-wiki --supports--> this | 1 | 0.27 | IGNORE |
| `wiki/syntheses/knowledge-architectures-for-llm-agents.md` | concepts/llm-wiki --supports--> this | 1 | 0.27 | IGNORE |
| `wiki/concepts/agent-fleet-management.md` | concepts/agent-harness --depends-on--> this | 1 | 0.27 | IGNORE |
| `wiki/entities/Agent-Development-Kit.md` | concepts/agent-harness --instance-of--> this | 1 | 0.25 | IGNORE |
| `wiki/entities/Antigravity.md` | concepts/agent-harness --instance-of--> this | 1 | 0.25 | IGNORE |
| `wiki/sources/2024-12-19-anthropic-building-effective-agents.md` | concepts/agent-harness --uses--> this | 1 | 0.25 | IGNORE |
| `wiki/sources/2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers.md` | concepts/agent-harness --supports--> this | 1 | 0.25 | IGNORE |
| `wiki/entities/Claude-Code.md` | concepts/agent-harness --instance-of--> this | 1 | 0.25 | IGNORE |
| `wiki/entities/Cursor.md` | concepts/agent-harness --instance-of--> this | 1 | 0.25 | IGNORE |
| `wiki/sources/2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair.md` | concepts/agent-harness --supports--> this | 1 | 0.24 | IGNORE |
| `wiki/concepts/knowledge-graphs.md` | concepts/agent-harness --part-of--> this | 1 | 0.24 | IGNORE |
| `wiki/sources/2025-07-31-wang-agentspec-runtime-enforcement-llm-agents.md` | concepts/agent-harness --uses--> this | 1 | 0.24 | IGNORE |
| `wiki/sources/2025-09-28-husain-ai-evaluations-clearly-explained-50-min.md` | concepts/agent-harness --supports--> this | 1 | 0.24 | IGNORE |
| `wiki/sources/2025-11-26-anthropic-effective-harnesses-long-running-agents.md` | concepts/agent-harness --uses--> this | 1 | 0.24 | IGNORE |
| `wiki/concepts/spec-driven-development.md` | concepts/agent-harness --uses--> this | 1 | 0.24 | IGNORE |
| `wiki/sources/2026-02-17-langchain-improving-deep-agents-harness-engineering.md` | concepts/agent-harness --uses--> this | 1 | 0.24 | IGNORE |
| `wiki/entities/Devin.md` | concepts/agent-harness --instance-of--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-03-05-lou-deepmind-autoharness-code-harness-synthesis.md` | concepts/agent-harness --uses--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness.md` | concepts/agent-harness --uses--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-03-20-huggingface-agentic-evaluations-workshop.md` | concepts/agent-harness --supports--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-03-26-pan-natural-language-agent-harnesses.md` | concepts/agent-harness --uses--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-03-30-lee-meta-harness-end-to-end-optimization.md` | concepts/agent-harness --uses--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack.md` | concepts/agent-harness --supports--> this | 1 | 0.23 | IGNORE |
| `wiki/entities/Cline.md` | concepts/agent-harness --instance-of--> this | 1 | 0.23 | IGNORE |
| `wiki/sources/2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy.md` | concepts/agent-harness --supports--> this | 1 | 0.22 | IGNORE |
| `wiki/sources/2026-05-11-blank-mit-6s191-three-laws-of-ai.md` | concepts/agent-harness --supports--> this | 1 | 0.22 | IGNORE |
| `wiki/sources/2026-05-11-karten-zhang-continual-harness-online-adaptation.md` | concepts/agent-harness --uses--> this | 1 | 0.22 | USE |
| `wiki/entities/LiteLLM.md` | concepts/agent-harness --part-of--> this | 1 | 0.22 | IGNORE |
| `wiki/sources/2026-05-18-wolfe-agent-evaluation-detailed-guide.md` | concepts/agent-harness --supports--> this | 1 | 0.22 | IGNORE |
| `wiki/entities/Langfuse.md` | concepts/agent-harness --part-of--> this | 1 | 0.22 | IGNORE |
| `wiki/sources/2026-07-14-wang-shi-harness-handbook-behavior-localization.md` | concepts/agent-harness --uses--> this | 1 | 0.22 | IGNORE |
| `wiki/sources/2026-05-14-ebbelaar-hybrid-search-rag-bm25-embeddings-reranker.md` | sources/2026-05-11-huber-chroma-rag-is-dead-agentic-search --supports--> this | 1 | 0.20 | IGNORE |
| `wiki/syntheses/harness-thinning-what-persists.md` | concepts/agent-harness --instance-of--> this | 1 | 0.19 | IGNORE |

**index.md / gap-expansion** (Step 5: one round, rg keyword sweep over `wiki/` for robot/humanoid/embodied/physical AI/world model/synthetic data/licensing/etc.)
| Page | why added |
|------|-----------|
| `wiki/sources/2026-05-11-karten-zhang-continual-harness-online-adaptation.md` | graph-only candidate promoted: Gemini Plays Pokémon: embodied gameplay, reset-free leren uit ruwe trajecten |
| `wiki/sources/2026-04-30-ai-index-report-2026.md` | not in ledger; found by keyword sweep: robots slagen in 12% van huishoudtaken vs 89,4% in RLBench-simulatie; synthetische data vervangt echte data nog niet in pre-training |
| `wiki/entities/Omni.md` | not in ledger; found by keyword sweep: term world model vervaagt van "action-conditioned video model" naar "model with understanding of the world"; vibe-coded games = coding agent + game engine |
| `wiki/sources/2026-06-11-kilpatrick-sequoia-model-eats-the-harness.md` | not in ledger; found by keyword sweep: Omni: één any-to-any-model; Demis noemt het een world model; games-categorie in AI Studio (~20%) |
| `wiki/sources/2026-02-03-loukides-radar-trends-february-2026.md` | not in ledger; found by keyword sweep: Genie 3 (interactief 3D world model); FlashWorld (tekst/beeld naar 3D-scène in seconden) |
| `wiki/sources/2026-03-03-loukides-radar-trends-march-2026.md` | not in ledger; found by keyword sweep: Waymo World Model voor simulatie van verkeersgedrag |
| `wiki/sources/2026-04-07-loukides-radar-trends-april-2026.md` | not in ledger; found by keyword sweep: "World models become a category"; LeWorldModel eerste stabiele JEPA-world model |
| `wiki/sources/2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china.md` | not in ledger; found by keyword sweep: LeCun: LLMs dood spoor voor embodied AI, world models volgende frontier; kans voor Europa |
| `wiki/sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing.md` | not in ledger; found by keyword sweep: risico: overtrainen op synthetische data, synthetische artefacten; digitale testrange |

## 3. Ignore policy applied
- `off-facet` — semantically adjacent but answers none of the facets.
- `below-threshold` — low fused score and no facet needs the page (graph-only long tail).

## 4. Information ignored
| Page | reason-class | one-line reason |
|------|--------------|-----------------|
| `wiki/concepts/ai-agents.md` | off-facet | agentbegrip; noemt world models of robotdata niet |
| `wiki/sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company.md` | off-facet | AI-native dienstverleners; semantische vals-positief op "model/data" |
| `wiki/sources/2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering.md` | off-facet | vibe coding/agentic engineering, niet world models |
| `wiki/concepts/llm-wiki.md` | off-facet | kennisbank-patroon; "world model" matcht hier ten onrechte op "kennismodel" |
| `wiki/sources/2026-02-01-manditereza-ontology-driven-industrial-ai.md` | off-facet | ontologie-/datalaag voor industriële agents; geen sim-to-real of synthetische data |
| `wiki/concepts/agent-harness.md` | off-facet | harness-engineering; het embodied-onderdeel komt via Karten |
| `wiki/sources/2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era.md` | off-facet | softwarelevering |
| `wiki/sources/2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained.md` | off-facet | RAG versus LLM-wiki |
| `wiki/sources/2026-05-11-huber-chroma-rag-is-dead-agentic-search.md` | off-facet | agentic search |
| `wiki/concepts/software-3.0.md` | off-facet | software-paradigma |
| `wiki/sources/2026-01-09-baron-signals-for-2026.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-11-nodus-labs-fix-karpathys-llm-wiki-knowledge-graph-infranodus.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/entities/Andrej-Karpathy.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/entities/Sequoia-Capital.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-15-osmani-agent-harness-engineering.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-09-30-demaree-onebrief-ai-military-planning.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-05-nishar-nohria-end-of-one-size-fits-all.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-07-31-collison-yc-startup-school-is-ai-breaking-the-lean-startup-playbook.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/agent-development-lifecycle.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/foundation-models.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/agentic-web.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/generative-ai.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-12-techlatest-hacker-search-engines-osint-tools-2026.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/small-language-models.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/react-reasoning-acting.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-06-12-mcveety-hormati-google-cloud-open-knowledge-format.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/vibe-coding.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/agentic-engineering.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/multi-agent-failure-modes.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/graph-engineering.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/industry-4-0.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/open-source-ai.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/syntheses/is-rag-dead.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/syntheses/knowledge-architectures-for-llm-agents.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/agent-fleet-management.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/entities/Agent-Development-Kit.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/entities/Antigravity.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2024-12-19-anthropic-building-effective-agents.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/entities/Claude-Code.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/entities/Cursor.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/knowledge-graphs.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2025-07-31-wang-agentspec-runtime-enforcement-llm-agents.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2025-09-28-husain-ai-evaluations-clearly-explained-50-min.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2025-11-26-anthropic-effective-harnesses-long-running-agents.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/concepts/spec-driven-development.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-02-17-langchain-improving-deep-agents-harness-engineering.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/entities/Devin.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-03-05-lou-deepmind-autoharness-code-harness-synthesis.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-03-20-huggingface-agentic-evaluations-workshop.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-03-26-pan-natural-language-agent-harnesses.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-03-30-lee-meta-harness-end-to-end-optimization.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/entities/Cline.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-11-blank-mit-6s191-three-laws-of-ai.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/entities/LiteLLM.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-18-wolfe-agent-evaluation-detailed-guide.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/entities/Langfuse.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-07-14-wang-shi-harness-handbook-behavior-localization.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/sources/2026-05-14-ebbelaar-hybrid-search-rag-bm25-embeddings-reranker.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |
| `wiki/syntheses/harness-thinning-what-persists.md` | below-threshold | graph-only neighbour with low fused score; no facet needs it |

## 5. Information used
| Page | type | effConf | contribution |
|------|------|---------|--------------|
| `wiki/concepts/industrial-ai-agents.md` | concept | 0.66 | synthetische data voor zeldzame defecten + Null Labs-case (geen echte beelden om te hertrainen) |
| `wiki/sources/2026-05-11-karten-zhang-continual-harness-online-adaptation.md` | source | — | Gemini Plays Pokémon: embodied gameplay, reset-free leren uit ruwe trajecten *(promoted: gap-expansion)* |
| `wiki/sources/2026-04-30-ai-index-report-2026.md` | source | — | robots slagen in 12% van huishoudtaken vs 89,4% in RLBench-simulatie; synthetische data vervangt echte data nog niet in pre-training *(promoted: gap-expansion)* |
| `wiki/entities/Omni.md` | entitie | — | term world model vervaagt van "action-conditioned video model" naar "model with understanding of the world"; vibe-coded games = coding agent + game engine *(promoted: gap-expansion)* |
| `wiki/sources/2026-06-11-kilpatrick-sequoia-model-eats-the-harness.md` | source | — | Omni: één any-to-any-model; Demis noemt het een world model; games-categorie in AI Studio (~20%) *(promoted: gap-expansion)* |
| `wiki/sources/2026-02-03-loukides-radar-trends-february-2026.md` | source | — | Genie 3 (interactief 3D world model); FlashWorld (tekst/beeld naar 3D-scène in seconden) *(promoted: gap-expansion)* |
| `wiki/sources/2026-03-03-loukides-radar-trends-march-2026.md` | source | — | Waymo World Model voor simulatie van verkeersgedrag *(promoted: gap-expansion)* |
| `wiki/sources/2026-04-07-loukides-radar-trends-april-2026.md` | source | — | "World models become a category"; LeWorldModel eerste stabiele JEPA-world model *(promoted: gap-expansion)* |
| `wiki/sources/2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china.md` | source | — | LeCun: LLMs dood spoor voor embodied AI, world models volgende frontier; kans voor Europa *(promoted: gap-expansion)* |
| `wiki/sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing.md` | source | — | risico: overtrainen op synthetische data, synthetische artefacten; digitale testrange *(promoted: gap-expansion)* |

## 6. Answer-element map
| Anchor | Answer element (claim) | Wiki page(s) | Section / span used |
|--------|------------------------|--------------|---------------------|
| [W1] | robots slagen in 12% van huishoudtaken vs 89,4% in RLBench-simulatie; synthetische data vervangt echte data nog niet in pre-training | [[sources/2026-04-30-ai-index-report-2026]] | Top Takeaway #5; Chapter 1 |
| [W2] | term world model vervaagt van "action-conditioned video model" naar "model with understanding of the world"; vibe-coded games = coding agent + game engine | [[entities/Omni]] | entity body |
| [W3] | Omni: één any-to-any-model; Demis noemt het een world model; games-categorie in AI Studio (~20%) | [[sources/2026-06-11-kilpatrick-sequoia-model-eats-the-harness]] | Key claims |
| [W4] | Genie 3 (interactief 3D world model); FlashWorld (tekst/beeld naar 3D-scène in seconden) | [[sources/2026-02-03-loukides-radar-trends-february-2026]] | **AI.** lijst |
| [W5] | Waymo World Model voor simulatie van verkeersgedrag | [[sources/2026-03-03-loukides-radar-trends-march-2026]] | **AI (10 items).** |
| [W6] | "World models become a category"; LeWorldModel eerste stabiele JEPA-world model | [[sources/2026-04-07-loukides-radar-trends-april-2026]] | trends-lijst |
| [W7] | LeCun: LLMs dood spoor voor embodied AI, world models volgende frontier; kans voor Europa | [[sources/2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china]] | open vragen |
| [W8] | synthetische data voor zeldzame defecten + Null Labs-case (geen echte beelden om te hertrainen) | [[concepts/industrial-ai-agents]] | ### Synthetic data for rare-event training |
| [W9] | risico: overtrainen op synthetische data, synthetische artefacten; digitale testrange | [[sources/2026-09-30-luo-null-labs-synthetic-data-ai-testing]] | ## TL;DR |
| [W10] | Gemini Plays Pokémon: embodied gameplay, reset-free leren uit ruwe trajecten | [[sources/2026-05-11-karten-zhang-continual-harness-online-adaptation]] | Key findings |

## 7. Final answer
Over world models en de kloof tussen simulatie en de echte wereld is de wiki **dun en vooral signalerend**. De retriever vond de relevante pagina's niet; ze kwamen pas boven via een zoekronde op trefwoorden.

**World models.** Kilpatrick ziet de term vervagen: van "action-conditioned video model" naar "a model with understanding of the world" [W2]. Google's Omni vervangt acht modellen, en Demis Hassabis noemt het een world model. Games maken een groot deel uit van wat bouwers in AI Studio maken [W3]. De verwachting op korte termijn: vibe-coded games draaien op een coding agent plus een game-engine, nog niet op een puur world model [W2]. Radar-signalen van 2026:
- Genie 3, een interactief 3D world model, en FlashWorld, dat van tekst of een beeld in seconden een 3D-scène maakt [W4]
- het Waymo World Model, dat verkeersgedrag simuleert [W5]
- "World models become a category", met LeWorldModel als eerste stabiele JEPA-model [W6]

LeCun stelt dat LLMs voor embodied AI een dood spoor zijn en dat world models de volgende frontier vormen. Ognibeni ziet daarin een kans voor Europa [W7].

**Datakloof.** Robots slagen in 12% van de huishoudtaken, tegen 89,4% in de RLBench-simulatie [W1]. Synthetische data vervangt echte data nog niet in pre-training [W1]. Synthetische data is wel nuttig als echte data ontbreekt: bij zeldzame defecten of bij doelwitten die van uiterlijk veranderen [W8]. De risico's zijn overtraining en synthetische artefacten [W9]. Gemini Plays Pokémon laat zien dat agents in games leren uit ruwe, doorlopende trajecten, zonder reset [W10].

**Gaten.** De wiki heeft niets over General Intuition, World Labs, NVIDIA Cosmos/Isaac, sim-to-real-methoden, VR of digital twins van woningen.

## 8. Trace artifact
Machine-readable provenance: [`2026-10-15-world-models-synthetische-data-robotica-query-trace.json`](2026-10-15-world-models-synthetische-data-robotica-query-trace.json)
