---
type: entity
kind: organization
aliases: ["TypeSafe AI", "TypeSafe", "typesafe.ai", "Jev"]
tags: [typesafe-ai, jev, system-one-models, classification, calibrated-decisions, model-vendor]
affiliation: "Independent AI startup"
role: "Builder of Jev, a non-generative \"System One\" decision model"
confidence: 0.7
last_confirmed: "2026-10-05"
accessed_at: "2026-10-05"
source_count: 4
---

# TypeSafe AI

**TypeSafe AI** is a startup that in September 2026 released **Jev**, which it calls a **System One model**: *"a class of AI models built to make fast, structured decisions that software can use directly. A System One model evaluates a state and returns typed answers and probabilities."* The name borrows Kahneman's *System 1 / System 2* distinction. Jev is cast as fast intuition; generative LLMs are the slow, step-by-step reasoning.

The wiki knows TypeSafe only **through [[LangChain]]**. All four sources are LangChain publications: three about the integration, and a keynote that features it. No TypeSafe primary source (its launch post, docs or model card) has been ingested. The alias `Jev` is recorded here because the wiki has no separate product page for it.

## What is claimed about Jev

- **Interface.** A *state* (text, structured data or chat messages) plus typed *questions* of three kinds: **Choice** (pick one option), **Score** (rate on ordered levels) and **Noul** (yes/no probability). All questions in one request are evaluated in parallel.
- **Training.** *"Reinforcement learning for calibrated decisions (RLCD)."* Size, architecture and training data are not disclosed.
- **Speed and cost.** *"Up to 200x faster inference and 400x lower cost than comparable LLMs on classification tasks"*, or as a range, *"20 to 200 times faster and 40 to 400 times cheaper"*. These are TypeSafe's figures, repeated by LangChain without a method.

## What has been measured

Only one measurement exists in the wiki: [[2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals|LangChain's Jev-as-a-Judge experiment]]. On five fixed weather-agent traces, Jev agreed with a human rater on all 500 binary judgements and had by far the lowest score variance. It cost **$0.00035 per call against $0.00039 for GPT-5.6 Luna and $0.02811 for Claude Sonnet 4.6**, at 0.44 s latency against 2.16–2.83 s. That is 1.1× to 80× cheaper and ~5–6× faster on this setup. See that page's scope section before citing it.

## Role in the wiki

- [[2026-09-17-runkle-lovell-langchain-building-a-harness-with-jev]]: the integration post; model routing and tool-risk gating as harness middleware.
- [[2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals]]: Jev as an eval judge, the one measurement.
- [[2026-09-21-runkle-langchain-building-a-harness-with-jev]]: video version; the Kahneman framing and the PII demo.
- [[2026-10-05-chase-langchain-interrupt-nyc-opening-keynote]]: Harrison Chase's Interrupt NYC keynote (24 Sep 2026). Jev as one of three uses in a portfolio beside frontier models (evals, guardrails, routing), served through the LangSmith LLM Gateway. A slide shows `jev-1.13.0` returning a `noul` of 0.999 for an urgency question. Chase dates the launch to *"the weekend"* before the talk (19–20 September), and his Google Trends slide peaks on 20 September. Chase also names TypeSafe beside OpenAI and Anthropic as a provider a model-neutral harness should be able to switch to.

Concepts touched: [[concepts/small-language-models|small-language-models]] (specialised models inside heterogeneous agent systems), [[concepts/agent-development-lifecycle|agent-development-lifecycle]] (judges), [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]] (risk classifiers).

## Open questions

- **Independent evidence.** Every source is from a distribution partner. A TypeSafe primary source, or a third-party benchmark, would be the next thing to ingest.
- **Launch date.** The earliest LangChain post is dated 17 September; Chase says Jev launched the weekend of 19–20 September. A TypeSafe primary source would settle it.
- **Is it a small model?** The wiki files Jev under the specialised-model argument, not the small-model one, because its size is unknown.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```
