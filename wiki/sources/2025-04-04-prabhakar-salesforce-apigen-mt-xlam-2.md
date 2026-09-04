---
type: source
kind: paper
title: "APIGen-MT: Agentic Pipeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay"
author: ["Akshara Prabhakar", "Zuxin Liu", "Ming Zhu", "Jianguo Zhang", "Tulika Awalgaonkar", "Shiyu Wang", "Zhiwei Liu", "Haolin Chen", "Thai Hoang", "Juan Carlos Niebles", "Shelby Heinecke", "Weiran Yao", "Huan Wang", "Silvio Savarese", "Caiming Xiong"]
publisher: "Salesforce AI Research; arXiv:2504.03601v2 [cs.CL], CC BY 4.0. Models and data open-sourced as the xLAM-2-fc-r series"
url: "https://arxiv.org/abs/2504.03601"
project_page: "https://apigen-mt.github.io"
date_published: 2025-04-04
date_revised: 2025-04-08
date_ingested: 2026-09-04
length: "~25 pages (full text read: §1–6, tables 1–3, appendices skimmed)"
raw: "../../raw/papers/apigen-mt-agentic-pipeline-multi-turn-data-generation.md"
tags: [xlam, salesforce, small-language-models, synthetic-data, multi-turn, function-calling, tool-use, ai-agents, ai-benchmarks, berkeley-function-calling-leaderboard, tau-bench, behavioral-cloning, supervised-fine-tuning, llm-as-judge, review-committee, rejection-sampling, open-weight-models, model-specialization]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
  - digital-transforming/navigating-innovation-ecosystems
relationships:
  - type: uses
    target: 2025-07-13-patil-berkeley-function-calling-leaderboard
    via: "BFCL v3 is one of the paper's two headline evaluations — the ranking screenshot in Table 1 *is* the Berkeley leaderboard as of 3 April 2025, with xLAM-2-70b and xLAM-2-32b at ranks 1 and 2. The paper is also a live example of the leaderboard's own finding: xLAM-2's margin over frontier models is concentrated almost entirely in the multi-turn column, the category BFCL's authors identify as unsolved"
    confidence: 0.9
  - type: supports
    target: 2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai
    via: "the strongest single piece of evidence in the NVIDIA position paper's capability roster, and cited there by name — *'the 8bn model achieves state-of-the-art performance on tool calling despite its relatively modest size'*. It substantiates argument A1 (SLMs are already powerful enough) and demonstrates A7 (agentic interaction traces are the natural data source for specialising a smaller model) as a working pipeline rather than a proposal"
    confidence: 0.85
  - type: supports
    target: 2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1
    via: "a concrete instance of the self-improvement machinery that course covers: an LLM committee judging generated tasks against a rubric, reflection-driven regeneration on failure, and rejection sampling of trajectories against executable ground truth. The 2.5× lift in Phase-1 yield (28% → 70%) from adding the agentic feedback loop is a rare published measurement of what the critique loop is actually worth"
    confidence: 0.7
---

# Prabhakar et al. (Salesforce AI Research) — APIGen-MT and the xLAM-2 models

The training-methodology paper behind **xLAM-2**, the open-weight model family [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Serhii Sokolenko actually runs in his PyCon DE demo]] and the model the [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|NVIDIA SLM position paper]] cites as its cleanest proof that small models can match frontier tool-calling. Fifteen authors from **[[Salesforce AI Research]]** (including **[[Juan Carlos Niebles]]**, **Silvio Savarese** and **Caiming Xiong**). April 2025.

Sokolenko compresses the whole paper to one sentence on stage — *"they used a synthetic data set with function calls and they used a process called supervised fine-tuning"* — and adds the point that matters for a practitioner: *"you can actually do it yourself if you generate synthetic data and use this process."* This page is the long version of that sentence.

## TL;DR

The bottleneck in training agents is **data**, not architecture: high-quality multi-turn human–agent interaction traces are scarce and expensive to collect by hand. APIGen-MT manufactures them in two phases, and the sequencing is the whole idea.

- **Phase 1 — build a verified blueprint first.** Generate a task *configuration*: user intent `q`, ground-truth actions `a_gt`, expected outputs `o_gt`. Validate it hard before anyone speaks. Only then—
- **Phase 2 — simulate the conversation against that blueprint.** An LLM plays a persona-driven human revealing details incrementally; `gpt-4o` in function-calling mode plays the agent; the executable environment supplies feedback. Keep only trajectories that reach the ground-truth state.

The reason for the ordering is stated plainly: *"direct conversation simulation often leads to inconsistencies or task deviations."* Verify the destination, then generate the journey.

Train on the result (filtered behavioural cloning over Llama 3.1/3.2 and Qwen 2.5 backbones) and you get the **xLAM-2-fc-r** family at 1B, 3B, 8B, 32B and 70B. Both the data and the models are open-sourced.

## Phase 1: how a blueprint gets verified

The validation stack is the part worth borrowing, because it is a general recipe for making synthetic agent data trustworthy.

**Generation inputs.** APIs are modelled as a **directed dependency graph** — an edge from API `A` to `B` where `B`'s inputs can consume `A`'s outputs *and* domain policy permits the pairing — and tasks are produced by random walks over it. Five samplers feed the generator: an **API sampler** (deliberately distinguishing state-*exploring* `read` calls from state-*changing* `write` calls, and anchoring ground truth on the writes), a **policy sampler**, a **domain-data sampler**, a **persona sampler** (from PersonaHub), and an **example sampler** for few-shot structure.

**Three-stage validation:**

| Stage | Check |
| --- | --- |
| **1 — Action** | *format* (are `<thought>/<instruction>/<actions>/<outputs>` present and well-formed JSON); *execution* (simulate every action in the real environment; capture the cumulative state change as a `diff_patch`, "similar to git diff"); *policy compliance* (**domain policies translated into Python unit tests**, run against the execution trace — catching violations that only arise from action interactions, e.g. action B being invalid given the state A created) |
| **2 — Alignment** | does the state change actually satisfy the stated intent? Judged by a **committee of diverse LLM judges** on Correctness, Completeness, Satisfaction and Creativity, aggregated by **majority vote** — explicitly to avoid single-judge bias |
| **3 — Semantic review & refinement** | above-threshold tasks are accepted; below-threshold tasks send consolidated committee feedback back to the generator, which **reflects and revises** |

**Reverse task recombination** builds hard tasks out of easy ones rather than generating them directly: take several independently-validated simple tasks sharing a persona, concatenate their actions and outputs, **re-run only the policy check** (to catch newly-conflicting combinations — the paper's example is returning and cancelling the same order), have the LLM synthesise one coherent overarching instruction, and re-validate from Stage 2. Compositionality as a data-generation strategy, with validation effort concentrated on the seam.

## Phase 2: keeping the simulated human honest

The known failure mode of user simulation is drift — the simulated human forgets the task or gets talked into the agent's framing. APIGen-MT's fix is **Best-of-N (N=4) sampling with a self-critique step** on the human LLM's turns. Trajectories are collected by **rejection sampling** (`r=1` only: final environment state matches `a_gt`, final response matches `o_gt`), three attempts per task, union of unique successes.

**The BoN result is independently useful as an *evaluation* finding, not just a training one.** Table 3: on τ-retail across five trials, `gpt-4o` under a naive user simulator scores 62.8% with variance **11.1**; under the BoN user simulator, **67.0% with variance 2.6**. Same agent — better user simulation raises both the score and the stability. Anyone using an LLM to simulate users in an eval harness should read that as a warning about their own numbers.

## The yield numbers

| Metric | Value |
| --- | --- |
| Phase 1 task-config success rate | **70%** |
| Phase 1 success rate **without** the agentic feedback loop | **28%** |
| Phase 2 trajectory simulation success rate | 67% |
| Total validated trajectories | **3,820** |
| Turns per trajectory | 1–29 (avg. 12 for `gpt-4o` to complete) |
| Avg. tool calls per trajectory | 7 |
| Avg. user turns per trajectory | 6 |

The machinery this measures — an LLM committee judging against a rubric, reflection-driven regeneration on failure, rejection sampling against executable ground truth — is the self-improvement apparatus [[2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1|Chowdhery & Mirhoseini's Stanford CS329A]] covers at course altitude, here running in anger with its yield reported.

**28% → 70% is the single most transferable number in the paper**: a 2.5× lift in usable synthetic data from adding a review committee and a reflection loop. It is one of the few published measurements of what critique-and-retry is actually worth.

Also worth noting the scale: **3,820 trajectories** is a small dataset by pretraining standards. The claim is that verified beats voluminous.

## Results

**BFCL v3 (as of 3 April 2025)** — [[2025-07-13-patil-berkeley-function-calling-leaderboard|the Berkeley leaderboard]]:

| Rank | Overall | Model | Multi-turn |
| ---: | ---: | --- | ---: |
| 1 | **78.19** | xLAM-2-70b-fc-r | **75.12** |
| 2 | **75.83** | xLAM-2-32b-fc-r | 66.38 |
| 4 | 72.83 | xLAM-2-8b-fc-r | 69.25 |
| 5 | 72.08 | GPT-4o-2024-11-20 (Prompt) | 47.62 |
| 7 | 69.58 | GPT-4o-2024-11-20 (FC) | 41.00 |
| 11 | 67.87 | o1-2024-12-17 (Prompt) | 36.00 |
| 14 | 65.11 | xLAM-2-3b-fc-r | 56.00 |
| 36 | 58.90 | xLAM-2-1b-fc-r | 43.12 |

Read the **multi-turn column**, not the overall one. On single-turn AST, xLAM-2-70b (88.48) and GPT-4o (88.1) are indistinguishable — single-turn is saturated. The entire margin is multi-turn: **75.12 vs 41–47**. Even the **1B** model, ranked 36th overall, beats `o1` and `gpt-4o` on multi-turn. The specialisation is narrow and real, and it lands exactly where BFCL's own authors say the open problem is.

**τ-bench** (pass@1, averaged over ≥5 trials, retail + airline):

| Model | Overall |
| --- | ---: |
| xLAM-2-70b-fc-r | **56.2** |
| xLAM-2-32b-fc-r | 54.6 |
| gpt-4o-2024-11-20 | 52.9 |
| xLAM-2-8b-fc-r | 46.7 |
| DeepSeek v3 | 40.6 |
| Llama 3.1 70B Instruct (the untuned backbone) | 38.2 |
| xLAM-2-3b-fc-r | 38.2 |
| Claude 3.5 Sonnet (new) | 60.1 |
| Claude 3.7 Sonnet + optimized prompt | **69.8** |
| o1 | 63.9 |

Two honest readings. The tuning is worth a lot — **38.2 → 56.2 on the same 70B backbone**, and the 3B model matches the untuned 70B. And the frontier still wins: Claude 3.5 Sonnet (new), Claude 3.7 and `o1` all beat xLAM-2-70b, and Claude 3.7 with an optimised prompt beats it by 13.6 points. **The paper's own framing — "on par with proprietary models" — is generous to itself on τ-bench, and precise on BFCL.**

**Consistency.** The `pass^k` curves (probability all *k* trials succeed) degrade more slowly for xLAM-2 than for the baselines; on the harder airline domain xLAM-2-70b has a *higher* `pass^5` than Claude despite a slightly lower `pass^1`. Reliability under repetition, which is the property that matters in deployment, is a different ranking from single-shot accuracy.

**Where it loses.** §5.4 is candid: on long-horizon tasks xLAM-2-70b beats `gpt-4o` but *lags Claude*, and it needs more user interactions than Claude to complete a task because it retrieves user details in stages.

## Dynamic capabilities (Warner & Wäger)

- **`digital-seizing/rapid-prototyping`** — the whole paper is a manufacturing process for the scarce input (verified interaction data), which collapses the cost of producing a specialised agent model from "collect human traces for months" to a pipeline run. That is prototyping capacity applied to model development itself.
- **`digital-transforming/navigating-innovation-ecosystems`** — open-sourcing both the synthetic dataset and the trained xLAM-2 weights is an ecosystem move by a large enterprise vendor, and it is what makes the model reachable by an independent practitioner on a laptop. The path from this paper to [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Sokolenko's 4-bit quantized demo]] is the ecosystem working.

## Linked entities and concepts

- Concepts: [[small-language-models]], [[ai-agents]], [[ai-benchmarks]], [[agent-harness]], [[open-source-ai]], [[foundation-models]]
- Entities: [[Salesforce AI Research]], [[xLAM]], [[Berkeley Function Calling Leaderboard]], [[Juan Carlos Niebles]], [[UC Berkeley]], [[Hugging Face]], [[OpenAI]], [[Anthropic]], [[NVIDIA]]
- **Dangling** (single-source mention, deferred): Akshara Prabhakar, Zuxin Liu, Caiming Xiong, Silvio Savarese, Shelby Heinecke, τ-bench, PersonaHub, LLaMA-Factory, DeepSpeed

## Scope and reliability

A **vendor research paper reporting its own models' scores**, which is the standard caveat and applies here — but the mitigations are unusually strong: both benchmarks are third-party and public, the BFCL leaderboard is externally maintained by [[UC Berkeley]] with independent verification, the weights and the synthetic data are open-sourced so the results are reproducible, and §5.4 states where the models lose.

The genuine limits: **the models are trained on data generated in the very environment (τ-bench domains, retail and airline) that one of the two evaluations uses.** The paper is explicit that Phase 1 sources its APIs and policies from τ-bench, so the τ-bench numbers measure in-distribution specialisation, and BFCL is the more informative of the two evaluations. Both are simulated-environment benchmarks; there is **no production deployment evidence** here. And the pipeline itself depends on `gpt-4o` and DeepSeek V3/R1 as generators, judges and test agent — a specialised small model distilled, in effect, from frontier models.

## Debates and supersession

- **"Small models beat frontier models at tool calling" needs its qualifier attached every time.** It is true on BFCL's *multi-turn* column and true in-domain on τ-bench; it is not true on τ-bench overall against Claude 3.5 Sonnet (new), Claude 3.7 or `o1`, and it is not a claim about general capability. When [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|the NVIDIA paper]] cites xLAM-2-8B as evidence for argument A1, this is the fine print.
- **Prompt optimisation is a confound the benchmark community has not settled.** Claude 3.7 gains 10 points on τ-bench from an optimised prompt (59.8 → 69.8) while the xLAM-2 numbers are reported with *"no prompt optimizations."* Comparing a tuned model under a plain harness against an untuned model under a tuned harness is comparing two different things — the same scaffold-versus-model confound [[ai-benchmarks]] tracks.
- **Numbers here are dated.** Table 1 is a leaderboard snapshot from 3 April 2025; by the December 2025 snapshot [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Sokolenko showed]], xLAM-2 had fallen to roughly position 18 of ~110 as frontier models improved and the benchmark added its agentic sections. **The model did not get worse; the leaderboard moved.** Treat every rank in this page as an artefact of its date.
- Open: nobody has published what happens when an xLAM-2-class model is dropped into a real production harness in place of a frontier model — the same gap [[small-language-models]] records.
