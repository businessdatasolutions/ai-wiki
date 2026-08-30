---
type: source
kind: paper
title: "Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets"
author: ["Dat Tran", "Douwe Kiela"]
publisher: "arXiv:2604.02460"
url: "https://arxiv.org/abs/2604.02460"
date_published: 2026-04-02
date_ingested: 2026-08-30
length: "abstract only (full paper not read)"
raw: "../../raw/papers/2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-equal-token-budgets.md"
tags: [multi-agent, single-agent, token-budget, data-processing-inequality, information-efficiency, multi-hop-reasoning, qwen3, deepseek-r1, gemini-2-5, test-time-compute, confounding]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2025-03-17-cemri-why-do-multi-agent-llm-systems-fail
    via: "the theory behind MAST's opening deflation. MAST observes that multi-agent gains on popular benchmarks 'are often minimal' and catalogues 14 ways the systems break; this paper argues from the Data Processing Inequality why the gains were never structurally available under a fixed budget — decomposition across agents can only lose information relative to one agent using the same tokens"
    confidence: 0.8
  - type: contradicts
    target: 2026-03-23-geng-neubig-caid-asynchronous-software-engineering-agents
    via: "opposite headlines ten days apart. CAID reports +25.6% / +14.7% for structured multi-agent coordination on long-horizon SWE tasks; this paper reports single agents matching or beating multi-agent systems on multi-hop reasoning at matched token budgets. The papers do not normalise against each other's key variable — CAID does not equalise compute, this paper does not test tasks that exceed one context window — and this paper's own prediction (MAS win when single-agent context utilisation degrades) is the seam"
    confidence: 0.75
---

# Tran & Kiela — Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets

## TL;DR

The paper that removes the confound from the multi-agent debate. Its claim is not that multi-agent systems are bad — it is that **most reported multi-agent gains are gains from spending more compute, and they have not been separated from gains from the architecture.**

**The theoretical argument.** Grounded in the **Data Processing Inequality**: under a *fixed reasoning-token budget* and with *perfect context utilisation*, a single agent is more **information-efficient**. Splitting a problem across agents means each agent's output is a lossy summary of what it saw, and downstream agents condition on the summary rather than the source. Post-processing cannot add information — it can only lose it. So the multi-agent architecture starts at an information deficit that its coordination benefits must pay back.

**The theory's own escape clause, which is the most useful part of the paper.** Multi-agent systems become competitive under exactly two conditions:

1. when a **single agent's effective context utilisation is degraded** — the problem no longer fits, or the model handles long context badly, or the context is polluted; or
2. when **more compute is expended** — you are simply willing to pay more.

That is a decision rule, not just a finding. **Reach for multiple agents when a single context window stops being enough, and not before.** It also dissolves most of the apparent conflict with [[2026-03-23-geng-neubig-caid-asynchronous-software-engineering-agents|CAID]]: reproducing a research paper or building a Python library from scratch guarantees condition (1) holds, so CAID's +25.6% is measured squarely inside the regime where this paper predicts multi-agent wins. Where the two genuinely disagree is on burden of proof — CAID does not equalise compute across arms, and this paper does not test tasks large enough to break a context window.

This also supplies the theory behind [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail|MAST's]] opening deflation — that multi-agent gains on popular benchmarks are *"often minimal."* MAST catalogues fourteen ways such systems break; this explains why the gains were never structurally available at a fixed budget in the first place.

**The experiment.** Three model families — **Qwen3, DeepSeek-R1-Distill-Llama, Gemini 2.5** — comparing single-agent systems against multiple multi-agent architectures at **matched reasoning-token budgets** on multi-hop reasoning. Result: **single-agent systems consistently match or outperform.**

**The practical consequence for agent-fleet work** is worth stating plainly, because it cuts against the direction the practitioner material pulls. [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Running 15 agents in parallel]] is justified by *throughput and isolation* — independent tasks, no shared context, wall-clock parallelism — which this paper does not challenge at all. It is justified *not at all* by "more agents reason better on one problem," which this paper says is false at equal spend. **Parallelism across independent tasks: supported. Decomposition of a single reasoning problem: pay for it deliberately.**

> **Date correction.** This paper is dated **April 2026**, not 2025. Any citation attributing it to 2025 is wrong.

## Dynamic-capabilities reading

- **`digital-seizing/balancing-digital-portfolios`** — a direct allocation rule for inference spend: the paper says where extra agents are worth buying and where they are overhead.
- **`contextual/internal-barriers`** — the confounding of architecture with compute is a barrier to evaluating agent architectures honestly, and it is endemic in the published comparisons.

## Linked entities and concepts

- Entities: [[Google]]
- Concepts: [[concepts/multi-agent-failure-modes|multi-agent-failure-modes]], [[concepts/agent-fleet-management|agent-fleet-management]], [[concepts/ai-agents|ai-agents]], [[concepts/ai-benchmarks|ai-benchmarks]], [[concepts/agent-harness|agent-harness]]
- **Dangling** (single-source mention, deferred): Dat Tran, Douwe Kiela

## Scope and reliability

**Abstract only** — effect sizes, which MAS architectures were tested, and how "perfect context utilisation" is operationalised were **not read**. The theoretical argument rests on an idealisation (perfect context utilisation) that no deployed system satisfies, and the paper is explicit that relaxing it is what lets multi-agent systems win — so the theory is best read as establishing **where the burden of proof sits**, not as a general impossibility result. Evaluated on **multi-hop reasoning only**; software engineering, tool use, and long-horizon agentic work are out of scope, and those are precisely where the practitioner interest lies.
