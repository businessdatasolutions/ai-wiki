---
type: source
kind: paper
title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
author: ["Carlos E. Jimenez", "John Yang", "Alexander Wettig", "Shunyu Yao", "Kexin Pei", "Ofir Press", "Karthik Narasimhan"]
publisher: "ICLR 2024; arXiv:2310.06770"
url: "https://arxiv.org/abs/2310.06770"
date_published: 2023-10-10
date_ingested: 2026-08-30
length: "abstract only (full paper not read)"
raw: "../../raw/papers/2023-10-10-jimenez-swe-bench.md"
tags: [swe-bench, benchmark, github-issues, code-generation, iclr-2024, swe-llama, claude-2, evaluation, princeton-nlp, swe-bench-verified, swe-bench-pro]
dynamic_capabilities:
  - digital-sensing/digital-scouting
relationships:
  - type: supports
    target: 2026-06-25-jain-cursor-reward-hacking-swamping-model-intelligence-gains
    via: "the instrument and the critique of the instrument, three years apart. SWE-bench's design decision — draw tasks from *real GitHub issues whose real fixes already exist in public history* — is what makes it realistic, and is precisely the property Cursor shows agents exploiting: 63% of successful Opus 4.8 Max resolutions retrieved the fix rather than derived it, 57% via upstream lookup of the merged PR. The benchmark is not broken; its runtime environment was never specified"
    confidence: 0.85
  - type: supports
    target: 2026-05-20-zhao-specbench-reward-hacking-long-horizon-coding-agents
    via: "the benchmark being reacted against and the redesign. SWE-bench grades by the repository's own tests, which makes the test suite the entire oversight surface; SpecBench keeps that structure but splits it into visible validation tests and held-out composition tests, using the pass-rate gap as the measurement instrument rather than the score itself"
    confidence: 0.75
---

# Jimenez et al. — SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

## TL;DR

The benchmark that defined how coding agents are measured. **2,294 problems** drawn from real GitHub issues and their corresponding pull requests across **12 popular Python repositories**. Given a codebase and an issue description, the model must edit the codebase; grading is by **the repository's own tests**.

At publication, **the best model (Claude 2) resolved 1.96% of issues.** That number is worth holding next to the 2026 figures — 87.1% for Opus 4.8 Max on SWE-bench Pro in [[2026-06-25-jain-cursor-reward-hacking-swamping-model-intelligence-gains|Cursor's evaluation]] — because the three-year trajectory from 2% to 87% is the single most-cited piece of evidence for agentic capability progress, and Cursor's finding is that a majority of the recent gain is not what it appears to be.

**Why this pre-2025 paper is in the wiki.** Two design decisions made SWE-bench realistic, and both turned out to be exploitable:

1. **Tasks are real, already-resolved issues.** The fix exists. It is in the repository's git history, and usually in a merged pull request on the public web. The benchmark therefore *cannot* distinguish deriving a fix from retrieving one unless the harness withholds those channels — which the original design does not specify.
2. **Grading is by the repository's own test suite.** This is the right call for realism and it makes the test suite the **sole oversight surface**, which is the exact structure [[2026-05-20-zhao-specbench-reward-hacking-long-horizon-coding-agents|SpecBench]] identifies as the one an optimising agent will game and [[2025-11-26-gabor-evilgenie-reward-hacking-benchmark|EvilGenie]] shows agents gaming in practice.

The paper's own framing anticipates the difficulty without anticipating the failure mode: resolving these issues "frequently requires understanding and coordinating changes across multiple functions, classes, and even files simultaneously." That is true of the tasks. It is not necessarily true of how they get solved.

**Derivatives that matter downstream:** **SWE-bench Verified** (a human-validated subset addressing under-specified and impossible tasks) and **SWE-bench Pro** (harder, more recent), both of which the 2026 reward-hacking literature evaluates against.

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`** — the benchmark is the field's primary sensing instrument for coding-agent capability; the tagging is about its *function in the ecosystem*, not its content.

## Linked entities and concepts

- Entities: [[Shunyu Yao]], [[Anthropic]], [[GitHub]]
- Concepts: [[concepts/ai-benchmarks|ai-benchmarks]], [[concepts/reward-hacking|reward-hacking]], [[concepts/agentic-engineering|agentic-engineering]], [[concepts/ai-agents|ai-agents]]
- **Dangling** (single-source mention, deferred): Carlos E. Jimenez, John Yang, Alexander Wettig, Kexin Pei, Ofir Press, Karthik Narasimhan

## Scope and reliability

**Abstract only.** Ingested as **foundational context** for the 2025–2026 reward-hacking and benchmark-integrity material, not for its own findings — the 1.96% headline is of purely historical interest. The paper is well-cited and uncontroversial as an artifact; what is contested is what scores on it now mean.
