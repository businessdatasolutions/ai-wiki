---
type: query-trace
question: "Please give me an overview of AI maturity frameworks discussed in the wiki"
date: 2026-07-01
language: en
trace: "2026-07-01-ai-maturity-frameworks-overview-query-trace.json"
pages_used: 3
pages_ignored: 78
---

# Query trace — AI maturity frameworks overview

## 1. Question

- **Original:** Please give me an overview of AI maturity frameworks discussed in the wiki
- **Restated:** What named AI-maturity / AI-adoption frameworks does the wiki hold, what do they claim, and how do they relate to each other?
- **Facets:**
  1. Which sources measure AI *maturity* numerically, with what instrument, and what number do they report?
  2. What is the wiki's central staged-maturity model (MIT CISR Four Stages), and what does it claim?
  3. Beyond maturity-as-a-number, what is the full cluster of organizational AI-adoption frameworks the wiki tracks, and where does "maturity" sit among them?
  4. Are there well-known maturity frameworks (Gartner, Deloitte) the wiki does *not* yet cover?

## 2. Paths explored

Retrieval ran via `node scripts/wiki-retrieve.mjs --json -n 12 "Please give me an overview of AI maturity frameworks discussed in the wiki"` — qmd hybrid search (11 hits) ∪ `wiki/.graph.json` 1-hop typed-edge traversal, fused via RRF, re-ranked by `effective_confidence`. `graph_available: true`, no `graph_warning`. 81 total candidates surfaced.

**qmd hits** (relevance stream, sorted by qmd rank)

| # | Page | type | qmd score | fused | verdict |
|---|------|------|-----------|-------|---------|
| 1 | `wiki/threads/ai-maturity-measurement-comparison.md` | thread | 0.93 | 0.840 | **USE** |
| 2 | `wiki/concepts/enterprise-ai-adoption.md` | concept | 0.44 | 0.948 | **USE** |
| 3 | `wiki/threads/organizational-frameworks-for-ai-adoption.md` | thread | 0.43 | 0.813 | IGNORE |
| 4 | `wiki/sources/2026-04-28-reitz-higgins-spacious-thinking.md` | source | 0.40 | 0.896 | IGNORE |
| 5 | `wiki/concepts/agent-harness.md` | concept | 0.37 | 0.931 | IGNORE |
| 6 | `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | synthesis | 0.37 | 0.887 | **USE** |
| 7 | `wiki/sources/2026-04-28-mittri-cisco-ai-enabled-enterprise.md` | source | 0.36 | 0.856 | IGNORE |
| 8 | `wiki/sources/2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair.md` | source | 0.36 | 0.843 | IGNORE |
| 9 | `wiki/sources/2026-05-21-bender-google-io-software-engineering-tipping-point.md` | source | 0.35 | 0.831 | IGNORE |
| 10 | `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | source | 0.35 | 0.767 | IGNORE |
| 11 | `wiki/concepts/founder-led-sales.md` | concept | 0.35 | 0.773 | IGNORE |

**graph neighbours** (1-hop typed-edge stream, qmd_rank null — selected rows; ~65 more below the shown set, all bulk-ignored, see §4)

| Page | reached via | fused | verdict |
|------|-------------|-------|---------|
| `wiki/concepts/automation-vs-augmentation.md` | enterprise-ai-adoption --uses--> this | 0.470 | IGNORE |
| `wiki/concepts/ai-employment-effects.md` | enterprise-ai-adoption --caused--> this | 0.460 | IGNORE |
| `wiki/concepts/jagged-frontier.md` | enterprise-ai-adoption --uses--> this | 0.449 | IGNORE |
| `wiki/concepts/dynamic-capabilities.md` | enterprise-ai-adoption <--supports<-- this | 0.446 | IGNORE |
| `wiki/concepts/micro-productivity-trap.md` | enterprise-ai-adoption --caused--> this | 0.446 | IGNORE |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | enterprise-ai-adoption --supports--> this | 0.422 | IGNORE |
| … (≈65 further `agent-harness`/RAG/harness-cluster graph neighbours, all fused ≤ 0.42) | 1-hop from `concepts/agent-harness` seed, off-facet | ≤0.42 | IGNORE (bulk) |

**index.md / gap-expansion (Step 5)** — not run. Facets 1–3 were fully answered by the USE set; facet 4 (Gartner/Deloitte maturity models) is answered directly by the thread's own "What's missing" section stating they are **not yet ingested** — no expansion needed to confirm an absence the wiki already documents.

## 3. Ignore policy applied

- `off-facet` (by far the dominant reason this run) — the query embeds near the wiki's large `agent-harness` / agentic-engineering / RAG cluster (shared vocabulary: "framework", "capability", "stack"), which qmd's vector leg and the graph's 1-hop traversal from `concepts/agent-harness` both pulled in. None of that cluster is about organizational AI-maturity measurement.
- `redundant` — candidates whose content is already fully covered, at equal or greater detail, by a higher-ranked USE page.
- No `decayed`, `superseded`, or `wrong-granularity` verdicts fired this run — no candidate in the USE-adjacent set carries `status: stale`, and no entity card was in contention (the facets need claims/models, not identity cards).

## 4. Information ignored

| Page | reason-class | one-line reason |
|------|--------------|-----------------|
| `wiki/threads/organizational-frameworks-for-ai-adoption.md` | redundant | Closed thread (`synthesized_into: organizational-frameworks-for-ai-adoption`); its 4-framework MIT CISR / Anand-Wu / Cisco / Werner-Le-Brun comparison and the MIT CISR "Four S" breakdown are both reproduced, with more detail, in the USE'd synthesis and the USE'd concept page. |
| `wiki/sources/2026-04-28-mittri-cisco-ai-enabled-enterprise.md` | redundant | Cisco's "5 Foundations" readiness framework and its 13%/68%/98%/85% figures are already summarized in both USE'd pages (Readiness lens). |
| `wiki/concepts/agent-harness.md` | off-facet | Runtime-engineering concept (context/constraints/contracts/compounding for coding agents) — a different lens entirely from organizational maturity; only reached top ranks via vector proximity on "framework". |
| `wiki/sources/2026-04-28-reitz-higgins-spacious-thinking.md` | off-facet | Leadership attention/"spacious thinking" piece — no maturity-framework content. |
| `wiki/sources/2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair.md` | off-facet | LLM eval tooling (Braintrust), not an org-maturity framework. |
| `wiki/sources/2026-05-21-bender-google-io-software-engineering-tipping-point.md` | off-facet | Software-engineering-with-AI talk; no maturity-model content. |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | off-facet | Startup founder interview (Emergent); adoption-velocity anecdote, not a maturity framework. |
| `wiki/concepts/founder-led-sales.md` | off-facet | Sales-motion concept; reached only via a `supports` edge into `enterprise-ai-adoption`. |
| `wiki/concepts/automation-vs-augmentation.md` | off-facet | Adjacent per-task deployment distinction cited *by* several frameworks, but not itself a maturity/adoption framework. |
| `wiki/concepts/ai-employment-effects.md` | off-facet | Downstream employment-impact concept, not a maturity framework. |
| `wiki/concepts/jagged-frontier.md` | off-facet | Task-capability-variance concept; adjacent, not a framework. |
| `wiki/concepts/dynamic-capabilities.md` | off-facet | Academic strategy-theory bridge the frameworks *don't* directly engage with (per the synthesis's own open questions) — not itself one of the discussed maturity frameworks. |
| `wiki/concepts/micro-productivity-trap.md` | off-facet | Named failure mode several frameworks target, not itself a framework. |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | off-facet | Macro AI-investment scale data (MGI), not an organizational maturity model. |
| ≈65 further graph-only candidates (`concepts/agentic-engineering`, `concepts/ai-agents`, `concepts/software-3.0`, `concepts/knowledge-graphs`, `concepts/llm-wiki`, `sources/*-harness-*`, `sources/*-rag-*`, entities `Claude-Code`/`Cline`/`Antigravity`/`LiteLLM`/`Langfuse`, etc.) | off-facet | All reached exclusively via 1-hop graph traversal from the `agent-harness` seed (agentic-engineering / RAG / knowledge-graph / harness-benchmark cluster); none address organizational AI-maturity measurement or adoption frameworks. Not enumerated individually — bulk-ignored as a single off-facet cluster; no unique claim among them was dropped (verified by scanning all 81 `retrieval_reasons` and `graph[].via` fields in the ledger). |

## 5. Information used

| Page | type | effConf | contribution |
|------|------|---------|--------------|
| `wiki/threads/ai-maturity-measurement-comparison.md` | thread (open) | n/a (thread, no confidence field) | The dedicated cross-instrument comparison: AI Index/McKinsey (1% "mature"), MIT CISR (7% Stage 4), Cisco (13% "ready"), Werner-Le-Brun (12% general transformation baseline); explicit note that Gartner/Deloitte maturity models are not yet in the wiki. |
| `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | synthesis | 0.90 | The 11-framework layered stack, the decision tree for which framework answers which executive question, and the cross-framework agreements/disagreements (incl. where MIT CISR's stage model sits relative to the other 10 lenses). |
| `wiki/concepts/enterprise-ai-adoption.md` | concept | 0.95 | The MIT CISR Four Stages table (28%/34%/31%/7%) + the "Four S" (Strategy/Systems/Synchronization/Stewardship) breakdown, worked examples (Guardian Life, Italgas, Ford, DBS Bank), and the explicit statement that seven-to-ten independent measurements converge on a 7–15% upper-tail maturity cohort. |

## 6. Answer-element map

| Anchor | Answer element (claim) | Wiki page(s) | Section / span used |
|--------|------------------------|--------------|---------------------|
| [W1] | MIT CISR's Four Stages of AI Maturity (Experiment 28% / Pilots 34% / Ways of Working 31% / Future-ready 7%), plus the Four S diagnostic (Strategy/Systems/Synchronization/Stewardship) for the Stage 2→3 transition | `concepts/enterprise-ai-adoption` | ## The MIT CISR Four Stages of Enterprise AI Maturity |
| [W2] | Four independent maturity/readiness instruments (AI Index 1% mature, MIT CISR 7% Stage 4, Cisco 13% ready, Werner-Le-Brun 12% transformation-success) measure different things but converge on "success is rare"; methodological caveats (sample age, definition mismatch) | `threads/ai-maturity-measurement-comparison` | ## What we know so far / Updated cross-walk |
| [W3] | The wiki tracks 11 organizational AI-adoption frameworks as complementary layers (org-design, readiness, capability progression/maturity, organizational learning, transformation playbook, firm-boundary, trap-escape, task deployment, deployment maturity, runtime engineering, plus the cross-cutting human-reaction lens); a decision tree maps executive questions to frameworks | `syntheses/organizational-frameworks-for-ai-adoption` | ## Findings — The frameworks operate on different layers / A decision tree |
| [W4] | Cross-framework agreement: adoption breadth (78–88%) vastly exceeds maturity depth (1–15% across five to seven instruments) — the strongest quantitative convergence in the cluster | `concepts/enterprise-ai-adoption`, `syntheses/organizational-frameworks-for-ai-adoption` | ## Working definition (closing paragraph) / ### Cross-framework agreement |
| [W5] | Gartner's and Deloitte's named AI-maturity models are explicitly flagged in the wiki as **not yet ingested** — a documented gap, not an oversight | `threads/ai-maturity-measurement-comparison` | ## What's missing / candidate sources to find |

## 7. Final answer

The wiki does not hold a single "AI maturity framework" page — it holds a **cluster of frameworks and a cross-instrument measurement comparison**, tracked across one concept page, one synthesis, and one open thread.

**The core staged-maturity model** is MIT CISR's **Four Stages of AI Maturity**: Experiment and prepare (28%, 2022 baseline) → Build pilots and capabilities (34%) → Develop AI ways of working (31%) → Become AI future-ready (7%) [W1]. The financial inflection point sits specifically at the Stage 2→3 transition; MIT CISR names four organizational blockers to that transition — **Strategy, Systems, Synchronization, Stewardship** ("the Four S") [W1].

**Four to seven other instruments measure "maturity" differently**, and the wiki keeps an explicit cross-walk of where they agree and diverge [W2]: AI Index/McKinsey pegs only **1%** of C-suite executives as calling their GenAI rollout "mature" (self-report); MIT CISR pegs **7%** at Stage 4 (a triangulated effectiveness score); Cisco's 2025 readiness survey pegs **13%** as "ready to leverage AI to its full potential" (a distinct readiness/urgency measure, not maturity or adoption); and a broader HBR study on general organizational transformation (Werner-Le-Brun) finds only **12%** of *any* transformation effort — AI or not — shows sustained gains [W2]. These four numbers span a single order of magnitude despite different instruments, samples, and definitions — the thread's headline finding is that **"whatever you call success, it's rare,"** and that citing any adoption/maturity number without naming its instrument loses meaning [W2].

**Beyond staged maturity, the wiki tracks ten further organizational-AI-adoption frameworks**, synthesized as mostly-complementary lenses on different decision layers rather than competing models [W3]: org-design (Werner-Le-Brun's Tin Man vs. Octopus), readiness (Cisco's 5 Foundations), organizational learning (Ransbotham/Kiron's Augmented Learners 2×2), transformation playbook (McKinsey *Rewired*'s 6 capabilities), firm-boundary (Nishar-Nohria's Build/Compose/Collaborate/Buy Outcomes), trap-escape (Bain/OpenAI's 4-step), task deployment (Anand-Wu's cost-of-errors × type-of-knowledge 2×2), deployment maturity (Beutler's Ask→Assist→Automate agency ladder), runtime engineering (the agent-harness Context/Constraints/Contracts/Compounding stack), plus Carucci's resistance-as-data lens applied cross-cutting to any of the above [W3]. The synthesis provides a decision tree mapping each executive question ("are we capable of changing?", "where are we in the maturity curve?", "which task first?"...) to the framework that answers it [W3].

**The one number every measurement instrument agrees on**: adoption breadth is high (78% in 2024, 88% in 2026) while maturity/readiness depth is low and clusters tightly in the **7–15%** range across now five-to-seven independent instruments (AI Index, MIT CISR, Cisco, Ransbotham/Kiron's Augmented Learners at 15%, Werner-Le-Brun) — the strongest quantitative convergence anywhere in this part of the wiki [W4].

**A documented gap**: the wiki explicitly notes it does **not** yet cover well-known consultancy maturity models such as **Gartner's AI maturity model** or **Deloitte's State of AI in the Enterprise** — flagged as missing sources to find, not silently absent [W5].

## 8. Trace artifact

Machine-readable provenance: [`2026-07-01-ai-maturity-frameworks-overview-query-trace.json`](2026-07-01-ai-maturity-frameworks-overview-query-trace.json)
