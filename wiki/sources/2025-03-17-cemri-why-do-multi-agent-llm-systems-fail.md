---
type: source
kind: paper
title: "Why Do Multi-Agent LLM Systems Fail?"
author: ["Mert Cemri", "Melissa Z. Pan", "Shuyi Yang", "Lakshya A. Agrawal", "Bhavya Chopra", "Rishabh Tiwari", "Kurt Keutzer", "Aditya Parameswaran", "Dan Klein", "Kannan Ramchandran", "Matei Zaharia", "Joseph E. Gonzalez", "Ion Stoica"]
publisher: "UC Berkeley (Sky Computing Lab / BAIR); NeurIPS 2025 Datasets & Benchmarks; arXiv:2503.13657"
url: "https://arxiv.org/abs/2503.13657"
date_published: 2025-03-17
date_ingested: 2026-08-30
length: "abstract only (full paper not read)"
raw: "../../raw/papers/2025-03-17-cemri-why-do-multi-agent-llm-systems-fail.md"
tags: [mast, multi-agent, failure-taxonomy, neurips-2025, berkeley, llm-as-judge, inter-agent-misalignment, task-verification, system-design, annotation, kappa]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-under-equal-budgets
    via: "the empirical failure catalogue and the theoretical account of why the failures are structural. MAST opens by noting that MAS performance gains on popular benchmarks 'are often minimal' and taxonomises 14 ways they break; Tran & Kiela explain the minimal gains information-theoretically — under a fixed reasoning-token budget, decomposing across agents can only lose information. One says *here is how it breaks*, the other says *here is why it was never free*"
    confidence: 0.8
  - type: supports
    target: 2026-03-23-geng-neubig-caid-asynchronous-software-engineering-agents
    via: "the diagnosis and the prescription, a year apart and pointed at the same three categories. MAST's failure clusters are system design, inter-agent misalignment, and task verification; CAID's three primitives answer them almost one-for-one — centralized delegation against design failures, isolated workspaces against inter-agent interference, and executable test-based verification against verification failures. CAID does not cite the taxonomy as its frame, but the correspondence is close enough to be worth recording"
    confidence: 0.7
---

# Cemri et al. — Why Do Multi-Agent LLM Systems Fail?

## TL;DR

The paper that gave multi-agent failure a vocabulary. Its premise is a deflation stated in the first sentence: *"Despite enthusiasm for Multi-Agent LLM Systems (MAS), their performance gains on popular benchmarks are often minimal."*

[[2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-under-equal-budgets|Tran & Kiela supply the theory a year later]]: the minimal gains were never structurally available, because under a fixed reasoning-token budget decomposing work across agents can only lose information relative to one agent spending the same tokens.

**What was built:**

- **MAST-Data** — 1,600+ annotated execution traces across **7 popular MAS frameworks**; the first dataset of multi-agent failure dynamics
- **MAST** — the **Multi-Agent System Failure Taxonomy**, developed from rigorous analysis of 150 traces with expert human annotators, validated at **inter-annotator agreement κ = 0.88** (high, and reported, which is rarer than it should be)
- An **LLM-as-a-Judge annotation pipeline** with high agreement against the human labels, so the taxonomy can be applied at scale

**The taxonomy: 14 failure modes in 3 categories.**

| Category | What breaks |
| --- | --- |
| **System design issues** | The architecture itself — role definitions, termination conditions, information flow |
| **Inter-agent misalignment** | Agents working from divergent assumptions, talking past each other, or undoing each other's work |
| **Task verification** | Nobody checks, or the check is inadequate — failures are accepted as successes |

Failures were analysed across models (GPT-4, Claude 3, Qwen2.5, CodeLlama) and tasks (coding, math, general agent).

**Why the three-category split is the durable contribution.** It says the problem is **organisational, not model-quality**. Two of the three categories — system design and inter-agent misalignment — are *coordination* failures that a better model does not fix, because they are properties of how the work was divided. The third, task verification, is the one the rest of this ingest keeps running into from every direction: it is [[2026-05-20-zhao-specbench-reward-hacking-long-horizon-coding-agents|SpecBench's]] collapsed oversight surface, [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Merge Mommy's]] verification-gap dimension, and the 46.41% of agent fixes that [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes|reviewers reject]] after the agent declared them done.

**The authors' own conclusion is anti-quick-fix:** the identified failures *"require more sophisticated solutions"* than prompt tuning. [[2026-03-23-geng-neubig-caid-asynchronous-software-engineering-agents|CAID]] is the closest thing in this ingest to what that looks like — and its three primitives map almost one-for-one onto MAST's three categories.

## Dynamic-capabilities reading

- **`digital-seizing/rapid-prototyping`** — the taxonomy is a debugging instrument for teams prototyping multi-agent systems; its practical use is turning "it didn't work" into a named mode.
- **`contextual/internal-barriers`** — coordination failures that persist across model upgrades are a structural barrier, not a capability gap.

## Linked entities and concepts

- Concepts: [[concepts/multi-agent-failure-modes|multi-agent-failure-modes]], [[concepts/ai-agents|ai-agents]], [[concepts/agent-harness|agent-harness]], [[concepts/agent-development-lifecycle|agent-development-lifecycle]], [[concepts/agentic-engineering|agentic-engineering]]
- Entities: [[UC Berkeley]] (Sky Computing Lab / BAIR), [[Ion Stoica]], [[Joseph E. Gonzalez]] — the latter two **promoted on 2026-09-04** by the second-source rule, when [[2025-07-13-patil-berkeley-function-calling-leaderboard|BFCL]] entered the corpus with the same two senior authors from the same lab.
- **Dangling** (single-source mention, deferred): Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt Keutzer, Aditya Parameswaran, Dan Klein, Kannan Ramchandran, Matei Zaharia

## Scope and reliability

**Abstract only** — the 14 individual failure modes are *not* enumerated here, only the three categories. **Anyone building on this taxonomy must read the paper for the mode list**; the three categories alone are a framing, not a checklist. Model vintage is early 2025 (GPT-4, Claude 3, Qwen2.5, CodeLlama) and the frameworks studied are the 2024–25 generation, so the specific incidence rates will have moved; the taxonomy is the durable artifact. Strong provenance — Berkeley Sky Computing / BAIR, NeurIPS Datasets & Benchmarks, with data, taxonomy and annotator publicly released.
