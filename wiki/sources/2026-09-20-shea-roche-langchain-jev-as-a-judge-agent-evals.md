---
type: source
kind: article
title: "Jev-as-a-Judge for Agent Evals"
author: ["Daniel Shea", "Seán Roche"]
publisher: "[[LangChain]]"
section: "LangChain Blog"
url: "https://www.langchain.com/blog/jev-agent-evals-langsmith"
date_published: 2026-09-20
date_ingested: 2026-09-22
length: "~1,680 words plus five results tables (9-minute web post; body via curl + html2text, image tables transcribed by hand into the raw file)"
raw: "../../raw/articles/2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals.md"
tags: [langchain, langsmith, deep-agents, typesafe-ai, jev, system-one-models, daniel-shea, sean-roche, llm-as-judge, agent-evaluation, online-evals, evaluator-variance, repeatability, eval-cost, gpt-5-6, claude-sonnet-4-6, signal-value, vendor-experiment, small-n]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
  - digital-seizing/balancing-digital-portfolios
relationships:
  - type: supports
    target: 2026-09-17-runkle-lovell-langchain-building-a-harness-with-jev
    via: "same vendor integration; the harness post covers routing and tool-risk gating, this post measures a third use: Jev as an eval judge"
    confidence: 0.85
  - type: supports
    target: 2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair
    via: "both split evaluators into code-based and LLM-as-judge and discuss online scoring of production traces under a cost constraint"
    confidence: 0.75
  - type: supports
    target: 2025-09-28-husain-ai-evaluations-clearly-explained-50-min
    via: "both concern binary pass/fail judges validated against human labels; Husain covers the construction and agreement metrics, this post compares judge models on that setup"
    confidence: 0.75
  - type: supports
    target: 2026-03-20-huggingface-agentic-evaluations-workshop
    via: "both concern rubric-based judging of agent outputs that cannot be checked deterministically"
    confidence: 0.7
  - type: supports
    target: 2026-05-09-chase-agent-development-lifecycle
    via: "same company's lifecycle framing; this post is an experiment inside its Test and Monitor phases, run on LangSmith datasets"
    confidence: 0.7
---

# Shea & Roche — Jev-as-a-Judge for Agent Evals

## TL;DR

A small LangChain experiment asking whether **Jev**, the non-generative *"System One"* model from **[[TypeSafe AI]]**, can serve as a third kind of agent evaluator next to **code-based checks** and **LLM-as-judge**. Daniel Shea and Seán Roche (LangChain) froze five runs of a [[LangChain]] Deep Agents weather agent into a LangSmith dataset. They then had four judges score each run **100 times**: Jev, GPT-5.6 Luna, GPT-5.6 Terra and Claude Sonnet 4.6. Scores were compared with one human reviewer's labels.

On this setup, Jev matched the human label on **all 500** binary decisions and had the **lowest score variance by two to three orders of magnitude**. It was also the cheapest and fastest judge. The authors call the result **observational**, and it rests on five cases.

## The argument

Code evaluators are *"cheap, quick, and reliable"* but narrow: they can check *that* an agent called a tool, not whether it then *used the result well*, because *"there can be several valid ways to use the same tool result."* LLM judges handle unstructured traces but are *"inherently non-deterministic systems, which are not a solid foundation for a trustworthy testing apparatus"*, and they are slower and costlier. The post's framing claim: **evaluation is a decision task**, which is what Jev is built for. It evaluates typed questions against a state and returns typed answers with probabilities, instead of reaching a judgement through token-by-token generation.

Jev's three question types, mapped to eval use:

| Type | Eval example | Returns |
|---|---|---|
| **Choice** | *"Which search outcome best describes this run?"* → `searched_appropriately` / `searched_unnecessarily` / `failed_to_search` | option probabilities + confidence |
| **Score** | *"How useful is the answer?"* on a 1–5 rubric | score, distribution, confidence |
| **Noul** (yes/no) | *"Is the final answer grounded in the retrieved evidence?"* | probability 0.0–1.0 |

Several atomic questions can be scored in parallel against one trace. This matters because the corpus's eval sources recommend breaking scoring into focused criteria ([[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair|Guthrie]]) and using binary judges ([[2025-09-28-husain-ai-evaluations-clearly-explained-50-min|Husain]]).

## The experiment

- **Target agent:** a weather agent built on Deep Agents with Tavily search.
- **Test set (5 cases):** current conditions (Seattle), weekend forecast (Austin), decision support (*"Should I bring an umbrella?"*, Dublin), longer-range forecast (Tokyo), and an **ambiguous location** (Springfield).
- **Fixed outputs.** Each agent response was captured once and stored as a fixed LangSmith example, so every judge scored **identical behaviour**. This separates judge variance from agent variance.
- **Two signals:** `quality`, a 0–1 scalar combining grounding, appropriate search behaviour and usefulness; and `does_pass`, a binary verdict.
- **Oracle:** one human reviewer labelled each fixed response against the same rubric.
- **Repetitions:** 100 per judge per case.

## Results

| Judge | `does_pass` accuracy vs human | Mean quality variance (× Jev) | Cost / call | Latency | Signal value* | 30-day cost at 10k traces/day |
|---|---|---|---|---|---|---|
| **Jev** | 100% (500/500) | 0.0000149 (1×) | $0.00035 | 0.44 s | 100.0% | $103.59 |
| GPT-5.6 Luna | 96.4% | 0.00647 (433×) | $0.00039 | 2.50 s | 90.1% | $117.24 |
| GPT-5.6 Terra | 99.8% | 0.01364 (913×) | $0.00289 | 2.83 s | 99.4% | $866.61 |
| Claude Sonnet 4.6 | 80.0% | 0.00137 (92×) | $0.02811 | 2.16 s | 80.0% | $8,434.08 |

\* *Signal value* is the authors' own metric: binary oracle agreement × binary repeatability. Repeatability is the chance that two independent calls on the same trace return the same verdict.

The authors separate the two properties carefully: *"Lower variance does not automatically mean higher accuracy: a judge can still be consistently wrong. But when a judge is accurate, lower variance makes that accuracy more dependable in production."* They also refuse to explain the variance gap: *"the result is observational, not evidence that its training objective caused the lower variance."*

Their conclusion is about the **economics of coverage**, not about accuracy: *"When evaluator calls are expensive, teams have to decide between coverage and their budget."* A cheap, stable judge lets a team score more production traces against more criteria and repeat judgements when confidence matters: *"The unlock is not just cheaper evals, but a tighter feedback loop."* This is the Test → Monitor → Iterate loop on [[concepts/agent-development-lifecycle|agent-development-lifecycle]], whose LangChain formulation is [[2026-05-09-chase-agent-development-lifecycle|Chase's ADLC essay]]. Rubric-scored judging of outputs that cannot be checked deterministically is also the subject of [[2026-03-20-huggingface-agentic-evaluations-workshop|the Hugging Face agentic-evals workshop]].

## Reading the numbers

Some things follow directly from the tables and are worth stating plainly:

- **Claude Sonnet 4.6's 80.0% is one case, not a scatter.** Its signal value equals its accuracy, so its repeatability is 1.0: it returned the same verdict every time. With five cases, that means it **disagreed with the human on exactly one case in all 100 repetitions** and agreed on the other four. The post does not say which case. The ambiguous-location request is the obvious candidate, but that is a guess.
- **The cost gap depends on the comparison.** Jev vs Luna is **1.1×** per call ($0.00035 vs $0.00039). Vs Terra it is ~8×; vs Sonnet 4.6, ~80×. Latency is **~5–6× lower** across the board. None approaches the *"200× faster, 400× cheaper"* TypeSafe figure the post repeats in its introduction. That figure is for classification tasks generally and is not this experiment's measurement.
- **Luna is the judge whose accuracy suffers from variance.** Its 96.4% accuracy against 90.1% signal value implies about 93.5% repeatability: it sometimes flips its verdict on identical input.
- **Sampling settings were left at provider defaults.** *"We did not set temperature, top-p, seed, or max tokens for the LLM judges."* Part of the LLM variance may be a configuration choice, not a property of the models.

The post does not report how many of the five fixed responses the human labelled pass vs fail. [[2025-09-28-husain-ai-evaluations-clearly-explained-50-min|Husain]] explains why accuracy alone is ambiguous without that base rate, and why he reports true-positive and true-negative rates separately.

## Dynamic-capabilities reading

- **`digital-transforming/improving-digital-maturity`** — the post is about evaluation practice: moving agent quality checks from occasional, expensive judgements towards continuous online scoring of production traces.
- **`digital-seizing/balancing-digital-portfolios`** — the explicit trade-off is *"coverage and their budget"*. Choosing a judge model is presented as allocating a fixed evaluation spend across more traces and more criteria.

## What was actually ingested

The full post body plus all five results tables. The tables are images on the page and were transcribed by hand into the raw file's appendix. Two further figures (per-case variance charts and an accuracy bar chart) are images whose headline values the prose states; they were not transcribed. The linked GitHub repository (`danielgshea/jev-as-a-judge`) was **not** inspected. Page metadata names only a placeholder author; the visible byline is used.

## Linked entities and concepts

- Entities: [[LangChain]], [[TypeSafe AI]]
- Concepts: [[concepts/agent-development-lifecycle|agent-development-lifecycle]], [[concepts/small-language-models|small-language-models]]
- Companion pieces: [[2026-09-17-runkle-lovell-langchain-building-a-harness-with-jev|Building a Harness with Jev]] and [[2026-09-21-runkle-langchain-building-a-harness-with-jev|the video walkthrough]]
- **Dangling** (single-source mention, deferred): Daniel Shea, Seán Roche

## Scope and reliability

**A five-case experiment, one human rater, run by a vendor that ships both the Jev integration and the eval platform it was run on.** The authors are frank about its limits. They say the results are observational, that *"we still need to see whether the results in this experiment carry over to other agents and production workflows"*, and that *"low cost can amplify mistakes — a consistently wrong evaluator can produce bad feedback at scale."* Specific limits:

- **n = 5.** Accuracy moves in 20-point steps per case. "100%" means Jev agreed with one person on five weather answers.
- **One domain, one agent, one rubric.** A weather agent with search is a well-bounded task. Nothing here tests long-horizon, coding or multi-turn traces.
- **Single human oracle.** No inter-rater agreement is reported, so "accuracy" means agreement with one reviewer.
- **Provenance gaps.** The Jev service version was *"not available in the experiment metadata"*, and LLM sampling settings were left at defaults.
- **Commercial interest.** LangChain distributes `langchain-typesafe` and sells LangSmith; the post ends by promoting a joint livestream with TypeSafe.

Cite it for the **experimental design**: fixed outputs, repeated scoring, accuracy separated from variance. Cite it for the **specific measured costs and latencies** on this setup. Do not cite it as evidence that decision models are better judges in general.
