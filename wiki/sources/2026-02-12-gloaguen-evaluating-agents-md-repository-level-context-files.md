---
type: source
kind: paper
title: "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"
author: ["Thibaud Gloaguen", "Niels Mündler", "Mark Müller", "Veselin Raychev", "Martin Vechev"]
publisher: "ETH Zürich (SRI Lab); arXiv:2602.11988"
url: "https://arxiv.org/abs/2602.11988"
date_published: 2026-02-12
date_ingested: 2026-08-30
length: "abstract only (full paper not read)"
raw: "../../raw/papers/2026-02-12-gloaguen-evaluating-agents-md-repository-level-context-files.md"
tags: [agents-md, claude-md, context-files, repository-context, swe-bench, inference-cost, negative-result, eth-zurich, context-engineering, prompt-engineering]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes
    via: "the same decomposition of what context is worth, reached from opposite directions. Gloaguen et al. find that instructions in context files *are* followed while repository overviews are not helpful; Abujadallah et al. conclude from 306 rejected agent PRs that what agents need is hints about the approach and explicit statements of forbidden approaches. Both say procedural constraint earns its tokens and general background does not"
    confidence: 0.75
  - type: supports
    target: 2025-07-10-becker-metr-early-2025-ai-experienced-developer-productivity
    via: "two rigorous negative results against interventions the field assumed were obviously beneficial, both surviving robustness checks. METR: AI assistance slows experienced developers on familiar code. Gloaguen et al.: repository context files do not improve success while costing >20% more inference. Together they are the corpus's strongest evidence that in agentic software engineering, plausible and measured diverge routinely"
    confidence: 0.7
---

# Gloaguen, Mündler, Müller, Raychev & Vechev — Evaluating AGENTS.md

## TL;DR

A rigorous negative result against a practice **every agent vendor recommends** and most teams have adopted: writing a repository-level context file (`AGENTS.md`, `CLAUDE.md`, and their equivalents) to tailor coding agents to a codebase.

**Two evaluation settings**, chosen to close the obvious objection that LLM-written context files are strawmen:

1. Established **SWE-bench** tasks from popular repositories, with **LLM-generated** context files
2. A **novel collection** of issues from repositories containing **developer-committed** context files

**Findings:**

- **Context files do not generally improve task success rates.**
- **Inference cost rises by over 20% on average.**
- This holds **across different LLMs, different coding agents, and both LLM-generated and human-written context files.**

**The decomposition is the actionable part, and it rescues the practice from being simply wrong:**

> "While instructions in the context files are well followed by coding agents, repository overviews, although popular and recommended by model providers, are not helpful."

So the file is not useless — **its most popular section is.** Agents *do* follow explicit instructions. What they do not benefit from is the architectural tour, the module inventory, the "here's how this codebase is organised" preamble that sits at the top of nearly every `AGENTS.md` in existence and is exactly what model providers' templates ask for. That section is pure token cost, paid on every single invocation.

The authors' conclusion is measured, not dismissive: context files are useful for specifying **non-standard coding practices**, and *"any attempts to improve performance should be rigorously evaluated before deployment."*

**The practical prescription — practitioner shorthand calls it a "lean AGENTS.md," which is not the paper's phrase:** keep the imperatives, delete the description. Say *"run `make lint` before committing"* and *"never modify files under `generated/`."* Delete *"this repository implements a three-tier architecture with a service layer that…"* — the agent can read the code, and it is charging you 20% to be told about it first.

This lands next to [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes|Abujadallah et al.]], who conclude independently from 306 rejected agent PRs that what agents need is **hints about the approach** and **explicit statements of forbidden approaches** — both imperative, neither descriptive. Two studies, different methods, same shape of answer.

It belongs beside [[2025-07-10-becker-metr-early-2025-ai-experienced-developer-productivity|METR's RCT]] as the corpus's second rigorous negative result against an intervention the field assumed was obviously beneficial — one on assistance, one on context — both surviving robustness checks.

## Dynamic-capabilities reading

- **`digital-transforming/improving-digital-maturity`** — the paper's real prescription is evaluative discipline: measure the harness intervention before standardising it, rather than adopting what the vendor's documentation recommends.
- **`contextual/internal-barriers`** — a universally recommended practice that raises cost >20% for no measured gain is a barrier hiding inside a best practice.

## Linked entities and concepts

- Concepts: [[concepts/agent-harness|agent-harness]], [[concepts/agentic-engineering|agentic-engineering]], [[concepts/agent-development-lifecycle|agent-development-lifecycle]], [[concepts/ai-benchmarks|ai-benchmarks]], [[concepts/llm-wiki|llm-wiki]]
- **Dangling** (single-source mention, deferred): Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev

## Scope and reliability

**Abstract only** — the models and agents tested, the effect-size confidence intervals, and how "repository overview" was distinguished from "instructions" in the analysis were **not read**. That last point is the one that would most change the prescription's precision. **Measured on issue-resolution success**, which is a narrow outcome: a context file might reduce review burden, improve style conformance, or lower rejection rates without moving SWE-bench pass@1 at all — none of which this design would detect. Strong provenance (ETH Zürich SRI Lab). Worth noting reflexively: **this wiki's own `CLAUDE.md` is a repository context file**, and it is overwhelmingly imperative rather than descriptive — which is the shape the paper's evidence supports.
