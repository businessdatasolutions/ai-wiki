---
type: concept
title: Multi-agent failure modes
aliases: ["multi-agent failure modes", "MAST", "multi-agent system failure taxonomy", "why multi-agent systems fail", "agent coordination failure"]
confidence: 0.8
last_confirmed: "2026-08-30"
source_count: 4
accessed_at: "2026-08-30"
tags: [mast, multi-agent, failure-taxonomy, coordination, inter-agent-misalignment, task-verification, data-processing-inequality, isolated-workspaces, caid, token-budget]
relationships:
  - type: part-of
    target: ai-agents
  - type: depends-on
    target: agent-harness
  - type: contradicts
    target: agent-fleet-management
    via: "fleet practice assumes more parallel agents produce more delivered value; this literature shows decomposing one problem across agents loses information at equal compute and that coordination failures are structural rather than capability gaps. The reconciliation is that fleets parallelise *independent* tasks, which is not the case the critique addresses"
    confidence: 0.7
quality_score: 1
---

# Multi-agent failure modes

Why systems of cooperating LLM agents underperform expectations — and the specific structures that fix it. The literature converges on an uncomfortable and useful conclusion: **most multi-agent failure is organisational, not model-quality**, so a better model does not repair it.

## The deflation

[[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail]] opens on it: *"Despite enthusiasm for Multi-Agent LLM Systems (MAS), their performance gains on popular benchmarks are often minimal."*

[[2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-under-equal-budgets]] explains why. The reported gains are **confounded with test-time compute** — multi-agent systems run more inference. Normalise the reasoning-token budget and the advantage largely disappears. The theoretical basis is the **Data Processing Inequality**: under a fixed budget with perfect context utilisation, a single agent is more **information-efficient**, because each agent in a chain conditions on a lossy summary rather than the source, and post-processing cannot add information. Tested across Qwen3, DeepSeek-R1-Distill-Llama and Gemini 2.5, single-agent systems consistently match or outperform on multi-hop reasoning at matched tokens.

**The escape clause is the useful part**, and it is a decision rule: multi-agent systems become competitive when **a single agent's effective context utilisation degrades** — the problem no longer fits, the model handles long context poorly, or the context is polluted — or when you are simply willing to spend more compute. **Reach for multiple agents when one context window stops being enough, and not before.**

## The taxonomy

[[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail]] built **MAST** — the Multi-Agent System Failure Taxonomy — from 1,600+ annotated traces across 7 MAS frameworks, with the taxonomy derived from close analysis of 150 traces at **inter-annotator agreement κ = 0.88**. **14 failure modes in 3 categories:**

| Category | What breaks |
| --- | --- |
| **System design issues** | The architecture — role definitions, termination conditions, information flow |
| **Inter-agent misalignment** | Agents on divergent assumptions, talking past each other, undoing each other's work |
| **Task verification** | Nobody checks, or the check is inadequate — failures accepted as successes |

Two of the three are **coordination** failures, which is why model upgrades do not fix them: they are properties of how work was divided. The third, **task verification**, is the seam every other part of this corpus runs into — [[2026-05-20-zhao-specbench-reward-hacking-long-horizon-coding-agents|SpecBench's]] collapsed oversight surface, [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Merge Mommy's]] verification-gap dimension, and the [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes|46.41% of agent fixes rejected]] after the agent declared them done.

## The prescription

[[2026-03-23-geng-neubig-caid-asynchronous-software-engineering-agents]] answers the taxonomy almost category-for-category, by porting coordination primitives human software teams already use:

| CAID primitive | MAST category it closes |
| --- | --- |
| **Centralized task delegation** (dependency-aware plans from a central manager) | System design |
| **Isolated workspaces** (one per subtask) | Inter-agent misalignment / interference |
| **Executable test-based verification** at structured integration | Task verification |

Result: **+25.6% absolute** over single-agent baselines on PaperBench, **+14.7%** on Commit0. *(Frequently miscited as +26.7% / +14.3%.)*

**The two results are compatible**, and the seam is Tran & Kiela's own condition: reproducing a research paper or building a Python library from scratch will not fit one context window, so the degradation condition holds by construction. CAID measures inside the regime where multi-agent wins. Neither paper normalises against the other's variable — CAID does not equalise compute, Tran & Kiela do not test context-exceeding tasks — so the honest summary is: **multi-agent architecture is a response to a context-capacity constraint, and where that constraint does not bind, the extra agents are overhead.**

## What practitioners already do

[[2026-07-25-darroman-profitable-founder-managing-ai-agents-25-prs-a-day|Carson's setup]] instantiates all three CAID primitives without naming them: a fresh VM per Devin session *is* an isolated workspace; the folder hierarchy plus paper priority list *is* a centralized delegation layer implemented in a human; the [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Land PR loop]] *is* structured integration with test-based verification. **The three things worth building first are the three things CAID names.**

## Related concepts

[[concepts/ai-agents|ai-agents]], [[concepts/agent-fleet-management|agent-fleet-management]], [[concepts/agent-harness|agent-harness]], [[concepts/agent-development-lifecycle|agent-development-lifecycle]], [[concepts/agentic-engineering|agentic-engineering]], [[concepts/reward-hacking|reward-hacking]].

## Debates and supersession

- **CAID vs Tran & Kiela** — reconciled above as a regime distinction, but the reconciliation is this wiki's inference, not either paper's claim. **Open:** a study that equalises compute *and* varies whether the task fits one context window.
- **Which CAID primitive carries the gain?** No ablation was read. If isolation alone accounts for most of it, the prescription is far cheaper than full CAID. **Open, and the highest-value question here.**
- **MAST's 14 modes are not enumerated in this wiki** — only the three categories, from the abstract. Anyone building a checklist must read the paper.
- **Vintages:** MAST studies GPT-4 / Claude 3 / Qwen2.5 / CodeLlama on the 2024–25 framework generation. Incidence rates will have moved; the taxonomy is the durable artifact.
