---
type: source
kind: article
title: "Building a Harness with Jev"
author: ["Sydney Runkle", "Hunter Lovell"]
publisher: "[[LangChain]]"
section: "LangChain Blog"
url: "https://www.langchain.com/blog/building-a-harness-with-jev"
date_published: 2026-09-17
date_ingested: 2026-09-22
length: "~1,060 words (5-minute web post; full body captured via curl + html2text, code blocks verbatim)"
raw: "../../raw/articles/2026-09-17-runkle-lovell-langchain-building-a-harness-with-jev.md"
tags: [langchain, typesafe-ai, jev, system-one-models, sydney-runkle, hunter-lovell, agent-harness, middleware, model-routing, auto-mode, tool-risk-gating, classification, structured-outputs, tool-calling, langchain-typesafe, kahneman, vendor-integration-post]
dynamic_capabilities:
  - digital-sensing/digital-scouting
relationships:
  - type: supports
    target: 2026-09-21-runkle-langchain-building-a-harness-with-jev
    via: "companion video by the same lead author, four days later, covering the same three use cases; the video adds the live PII demo, the Kahneman framing and a first-person anecdote about auto-mode latency"
    confidence: 0.9
  - type: supports
    target: 2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals
    via: "same vendor integration, a third use case: this post covers routing and tool-risk gating, the companion post measures Jev as an eval judge"
    confidence: 0.85
  - type: supports
    target: 2026-07-06-google-cloud-agent-factory-intent-driven-development
    via: "both describe a classifier interposed between an agent and its tool calls to block risky actions: Hallie describes Claude Code's auto mode, this post ships an open middleware version built on a third-party classifier"
    confidence: 0.8
  - type: supports
    target: 2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai
    via: "both concern routing narrow decisions inside an agent to a specialised, cheaper model rather than a generalist LLM"
    confidence: 0.7
  - type: supports
    target: 2026-09-14-google-cloud-agent-factory-agent-harnesses-explained
    via: "both concern per-call latency and cost inside the agent loop as a reason to use a cheaper model for part of the work"
    confidence: 0.65
  - type: supports
    target: 2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness
    via: "same company's harness vocabulary; Trivedy defines the harness layers, this post adds two middleware components to it"
    confidence: 0.65
---

# Runkle & Lovell — Building a Harness with Jev

## TL;DR

A LangChain integration post announcing `langchain-typesafe`, which wraps **Jev**, a model released by **[[TypeSafe AI]]** in September 2026. The authors are [[Sydney Runkle]] (product manager, LangChain open-source) and Hunter Lovell. Jev is **not a text generator**. TypeSafe calls it a *"System One model"*: you send it a **state** (text, structured data or LangChain messages) and a set of typed **questions**, and it returns typed answers with probabilities. The post's argument is that many decisions an agent currently makes with a full LLM call are really **classification tasks**. Those can be moved off the main model into a cheaper, faster one without changing what the agent can do.

The headline numbers (*"up to 200x faster inference and 400x lower cost than comparable LLMs on classification tasks"*) are **TypeSafe's claims, attributed as such**. This post does not measure them. The companion eval post does measure latency and cost, and gets much smaller ratios (see [§Scope and reliability](#scope-and-reliability)).

## What Jev is, per the post

- **Three question types.** *Choice* picks one of several options and returns a probability per option plus overall confidence. *Score* rates against ordered levels (e.g. low/medium/high) and returns a continuous score, the distribution and a confidence. *Noul* (TypeSafe's term for a yes/no question) returns the probability that a statement is true.
- **Parallel questions against one state.** *"System One models evaluate every question in a request in parallel. Adding questions barely changes the response time."* The post contrasts this with the sequential, token-by-token way an LLM reaches a judgement.
- **Training objective.** Jev was trained with *"reinforcement learning for calibrated decisions (RLCD)"*, according to TypeSafe. The post gives no model size, architecture or benchmark.
- **Where it sits.** *"Jev isn't a drop-in replacement for an LLM… use an LLM for open-ended reasoning and generation, and Jev for fast, structured decisions along the way."* It is a component inside the loop, not a model for the loop.

The post places this as the third step in making LLMs usable in software. Tool calling gave models structured requests and structured outputs gave them typed results, but *"the agent loop is still slow and costly: every decision requires another model call."*

## The two harness components it ships

Both are shipped as **middleware** under `langchain_typesafe.experimental.middleware`, the extension point that [[concepts/agent-harness|agent-harness]] records as the Constraints layer.

**1. `ModelRouterMiddleware` — model routing.** You declare model choices with plain-language criteria, e.g. `fast` for *"direct lookups, extraction, and localized changes"* and `powerful` for *"architecture and high-stakes decisions"*. Jev then picks one from the latest user message, with the instruction *"Choose the least costly model that can complete the task."* The choice is **made once per run**: *"The router selects a model from the latest user message and uses it throughout the run."* The probabilities stay in agent state. This puts in code the routing idea on [[concepts/small-language-models|small-language-models]]: send each request to the cheapest model that can serve it. It routes per run, not per step. For the per-model economics, see [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|Belcak et al. (NVIDIA)]] and [[2026-09-14-google-cloud-agent-factory-agent-harnesses-explained|Google Cloud's loop-count argument]].

**2. `AutoModeMiddleware` — tool-risk gating.** Jev checks each tool call (the example scopes it to `bash`) and blocks risky ones *before* the tool runs. The post frames it as open-sourcing something closed:

> *"Coding harnesses like claude, codex, cursor have shipped some kind of way to classify dangerous actions before they're taken which has slowly helped to build trust in agents. Up until now, this classifier step has been locked away in the closed source parts of the harness. Now that a cheap and performant classifier model exists, we can take the same pattern and adopt it to all agents!"*

The closed version it refers to is Claude Code's auto mode, whose design [[2026-07-06-google-cloud-agent-factory-intent-driven-development|Lydia Hallie described on The Agent Factory]]. The post's stated reason for gating is trust: *"Agents are still inherently untrustworthy. An agent can receive bad instructions (either naturally or from a motivated enough attacker)."* See [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]].

The harness framing matches LangChain's own vocabulary ([[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy, The Anatomy of an Agent Harness]]): both components are harness middleware, not changes to the model.

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`** — the post is a scouting artefact: a vendor spots a new model class in the week it appears and shows where it fits in an existing agent stack. That is the *identifying new technology options* activity, from the builder side.

## What was actually ingested

The full post body: prose, both JSON examples from TypeSafe's quickstart, and the three Python snippets. One figure (a three-panel illustration of the question types) is an image; the prose next to it covers the same content. The page's structured metadata names only a placeholder author (*"LangChain Accounts"*). The visible byline, *Sydney Runkle, Hunter Lovell, September 17, 2026*, is used here.

## Linked entities and concepts

- Entities: [[LangChain]], [[TypeSafe AI]], [[Sydney Runkle]]
- Concepts: [[concepts/agent-harness|agent-harness]], [[concepts/small-language-models|small-language-models]], [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]]
- Companion pieces: [[2026-09-21-runkle-langchain-building-a-harness-with-jev|the video walkthrough]] and [[2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals|Jev-as-a-Judge]]
- **Dangling** (single-source mention, deferred): Hunter Lovell

## Scope and reliability

**This is an integration announcement from a company that ships the integration.** It contains no measurements. The speed and cost multipliers are TypeSafe's own figures for classification tasks, quoted without method. Three things the reader cannot check from this post:

- **The multipliers.** LangChain's own measurement four days later ([[2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals|Shea & Roche]]) found Jev at **$0.00035 per call against GPT-5.6 Luna's $0.00039**, about 1.1× cheaper, and **0.44 s against 2.16–2.83 s**, about 5–6× faster. Jev was ~80× cheaper than Claude Sonnet 4.6. The "400×" figure depends on which LLM you compare against, and the post does not say which.
- **The gate's error rates.** `AutoModeMiddleware` blocks calls Jev scores as risky. No false-block or false-approve rate is reported, and no threshold is documented in the post.
- **The model.** Size, architecture and training data are not disclosed. Both middleware components are in an `experimental` namespace.

The social-proof paragraph (named builders using Jev for browser agents, a trading agent and email triage) links to X posts, not to any results.
