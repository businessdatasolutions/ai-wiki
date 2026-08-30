---
type: source
kind: paper
title: "Effective Strategies for Asynchronous Software Engineering Agents"
author: ["Jiayi Geng", "Graham Neubig"]
publisher: "Carnegie Mellon University; arXiv:2603.21489"
url: "https://arxiv.org/abs/2603.21489"
date_published: 2026-03-23
date_ingested: 2026-08-30
length: "abstract only (full paper not read)"
raw: "../../raw/papers/2026-03-23-geng-neubig-caid-asynchronous-software-engineering-agents.md"
tags: [caid, asynchronous-agents, multi-agent, isolated-workspaces, centralized-delegation, paperbench, commit0, dependency-aware-planning, branch-and-merge, test-based-verification]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
  - digital-transforming/redesigning-internal-structures
relationships:
  - type: supports
    target: 2025-03-17-cemri-why-do-multi-agent-llm-systems-fail
    via: "the prescription answering the diagnosis, category by category. MAST's three failure clusters are system design, inter-agent misalignment and task verification; CAID's three primitives are centralized task delegation, isolated workspaces and executable test-based verification. The correspondence is close enough to read CAID as a constructive reply to the taxonomy, even though it is not framed that way"
    confidence: 0.75
  - type: contradicts
    target: 2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-under-equal-budgets
    via: "opposite headline conclusions about multi-agent systems, ten days apart, and the disagreement is real but bounded. Tran & Kiela: under matched reasoning-token budgets, single agents match or beat multi-agent systems on multi-hop reasoning. CAID: structured multi-agent coordination beats single-agent baselines by 25.6% on PaperBench and 14.7% on Commit0. The reconciliation is in Tran & Kiela's own prediction — MAS become competitive when a single agent's effective context utilisation degrades, which is exactly what happens on a long-horizon SWE task that will not fit one context window. Neither paper normalises against the other's variable"
    confidence: 0.75
  - type: supports
    target: 2026-07-25-darroman-profitable-founder-managing-ai-agents-25-prs-a-day
    via: "the same primitive, validated experimentally and adopted commercially. CAID isolates *isolated workspaces* as one of three coordination primitives and measures the gain; Carson's practice rests on Devin's fresh-VM-per-session model for the identical reason — *\"cloud agents solve collision problems by providing isolated virtual machines per session\"* — and it is what makes 5–10 concurrent agents feasible at all. Practice arrived first; this is the controlled evidence"
    confidence: 0.75
---

# Geng & Neubig — Effective Strategies for Asynchronous Software Engineering Agents (CAID)

## TL;DR

The clearest statement in the corpus of **why parallel agents interfere, and what infrastructure fixes it** — and the fix is borrowed wholesale from how human teams already work.

**The problem, stated precisely.** Agents are good at isolated SWE tasks. Long-horizon tasks with interdependent subtasks are still hard, on both accuracy and elapsed time. Asynchronous multi-agent collaboration is the obvious answer and it is *"surprisingly difficult"*:

- concurrent edits interfere with each other
- dependencies are hard to synchronise
- combining partial progress into a coherent whole is hard

**The move.** *"Human developers have long relied on mature collaboration infrastructure to manage these challenges."* Branches, code review, merge queues, CI — decades of accumulated coordination machinery. CAID ports the primitives rather than inventing new ones.

**CAID = Centralized Asynchronous Isolated Delegation.** Three primitives:

The three primitives map almost one-for-one onto the three failure categories in [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail|MAST]], the multi-agent failure taxonomy published a year earlier — which is why this paper reads as a constructive reply to it even though it is not framed that way.

| Primitive | What it does | Which failure it closes |
| --- | --- | --- |
| **Centralized task delegation** | A central manager builds dependency-aware task plans | System-design failures — someone owns the decomposition |
| **Asynchronous execution** | Subtasks run concurrently | Latency, not accuracy |
| **Isolated workspaces** | Each subtask gets its own workspace | Inter-agent interference — concurrent edits cannot collide |

Progress is consolidated via **structured integration with executable test-based verification** — the merge is gated by tests that actually run, not by an agent's assertion that it is done.

**Results:** **+25.6% absolute** over single-agent baselines on **PaperBench** (paper reproduction) and **+14.7% absolute** on **Commit0** (Python library development).

> **Correction on the numbers.** These are frequently cited as +26.7% and +14.3%, including in the request that prompted this ingest. The published abstract states **25.6%** and **14.7%**.

**Why this is the architectural spine of the practitioner material.** [[2026-07-25-darroman-profitable-founder-managing-ai-agents-25-prs-a-day|Carson's 5–10 concurrent cloud agents]] work for exactly the reason CAID isolates: a fresh VM per session *is* an isolated workspace. His folder hierarchy and paper priority list *are* a centralized delegation layer, implemented in a human. His Land PR loop *is* structured integration with test-based verification. The practitioner built the architecture by feel; this paper names the primitives and measures each one's contribution. That correspondence is the most useful thing in this ingest for anyone designing an agent pipeline: **the three things worth building first are the three things CAID names.**

**Where it sits against [[2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-under-equal-budgets|Tran & Kiela]].** Ten days apart, opposite headlines. The reconciliation is in Tran & Kiela's own theory: multi-agent systems become competitive when a single agent's effective context utilisation degrades. Reproducing a research paper or building a Python library from scratch will not fit one context window, so the degradation condition holds by construction. **Multi-agent architecture is not a general win; it is a response to a context-capacity constraint** — and where that constraint does not bind, the extra agents are pure overhead.

## Dynamic-capabilities reading

- **`digital-seizing/rapid-prototyping`** — asynchronous execution targets *timely completion* as an explicit goal alongside accuracy; the paper treats wall-clock as a first-class outcome.
- **`digital-transforming/redesigning-internal-structures`** — the whole method is organisational transfer: human software-team coordination structures reimplemented as agent infrastructure.

## Linked entities and concepts

- Concepts: [[concepts/multi-agent-failure-modes|multi-agent-failure-modes]], [[concepts/agent-fleet-management|agent-fleet-management]], [[concepts/agent-harness|agent-harness]], [[concepts/ai-agents|ai-agents]], [[concepts/agentic-engineering|agentic-engineering]]
- **Dangling** (single-source mention, deferred): Jiayi Geng, Graham Neubig

## Scope and reliability

**Abstract only** — no ablations were read, so **which of the three primitives carries the gain is unknown from this page.** That is the most important open question here: if isolation alone accounts for most of it, the prescription is much cheaper than full CAID. Two benchmarks, both unusually structured (PaperBench has a written specification to work from; Commit0 has a known target API), so transfer to open-ended feature work in a live codebase is not established. Code is public at `github.com/JiayiGeng/CAID`.
