---
type: source
kind: video
title: "Building a Harness with Jev"
author: ["LangChain"]
url: "https://www.youtube.com/watch?v=VE5dsWll06M"
date_published: 2026-09-21
date_ingested: 2026-09-22
length: "~9:14 minutes (transcript ~153 segments; human-curated captions)"
raw: "../../raw/videos/building-a-harness-with-jev.md"
tags: [langchain, typesafe-ai, jev, system-one-models, sydney-runkle, kahneman, thinking-fast-and-slow, agent-harness, model-routing, auto-mode, llm-as-judge, online-evals, pii-detection, langchain-typesafe, science-technology, vendor-explainer]
dynamic_capabilities:
  - digital-sensing/digital-scouting
relationships:
  - type: supports
    target: 2026-09-17-runkle-lovell-langchain-building-a-harness-with-jev
    via: "video version of the blog post by the same lead author; same three question types and same routing and auto-mode middleware"
    confidence: 0.9
  - type: supports
    target: 2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals
    via: "the video's third use case summarises the Jev-as-a-Judge experiment and points to it"
    confidence: 0.85
  - type: supports
    target: 2026-07-06-google-cloud-agent-factory-intent-driven-development
    via: "both concern a risk classifier gating an agent's tool calls, and both speak to the human cost of the gate: Hallie on permission fatigue, Runkle on classifier latency"
    confidence: 0.75
---

# Runkle / LangChain — Building a Harness with Jev (video)

> Learn all about Jev, a new System One model from TypeSafe AI, and how you can use it in your agent harness. Jev is up to 200x faster and 400x cheaper than LLMs on classification style tasks, which makes it great for applications like model routing and "jev as a judge" online evals.

## TL;DR

A nine-minute slide-and-demo explainer from [[LangChain]], presented by [[Sydney Runkle]], product manager on LangChain's open-source team. It is the video version of [[2026-09-17-runkle-lovell-langchain-building-a-harness-with-jev|Runkle & Lovell's blog post]]: what **Jev** from **[[TypeSafe AI]]** is, its three question types, the `langchain-typesafe` integration, and three uses (model routing, auto mode, Jev-as-judge). Most of it repeats the post. Four things are only here:

**1. The name comes from Kahneman.** *"System One"* is borrowed from Daniel Kahneman's *Thinking, Fast and Slow*: *"fast and cheap, System 1 intuition, versus slow and expensive, System 2 reasoning."* TypeSafe positions Jev as the System 1 half, *"returning almost instant typed decisions instead of generating text"*. Standard LLMs *"behave more like System 2, slower and pricier, but adhering to more of this step-by-step reasoning over open-ended problems."* This is the vendor's branding, not a claim about cognition. It still gives a compact picture of how the two model types split the work in a harness.

**2. A side-by-side demo.** The question *"is there PII in this text?"* goes to an LLM with structured output (about five seconds) and to Jev (*"almost immediately, chance that there's PII is 98%"*). One example, timed by eye.

**3. The speed and cost claim is stated as a range.** *"20 to 200 times faster and 40 to 400 times cheaper on classification style tasks compared to an LLM."* The blog post and the video description quote only the top of the range.

**4. A first-person account of turning oversight off because it was slow.** This is the most useful minute in the video:

> *"Anecdotally, I actually turned off auto mode in my coding agent recently, because the classification step of whether a given tool call was risky was too slow for my coding agent to feel productive. But it's back on now that Jev can make these decisions so quickly."*

So a safety gate was switched off because of **its latency**, not because it was wrong. It came back on when the gate got faster. This is the same class of cost as the *permission fatigue* that [[2026-07-06-google-cloud-agent-factory-intent-driven-development|Lydia Hallie described for Claude Code's auto mode]]. Hallie's gate is ignored because it asks too often; Runkle's was dropped because it answered too slowly. See [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]].

On routing, Runkle adds an internal use: LangChain wants *"our internal coding agents to switch between fast and cheap models and more expensive and powerful models depending on the complexity of a given question or coding task"*. That is the heterogeneous-model argument on [[concepts/small-language-models|small-language-models]], as a stated intention, not a reported result. On evals she summarises [[2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals|the Jev-as-a-Judge experiment]] as *"much cheaper and much faster, but also… much more reliable and consistent"*. That goes beyond what its five-case result supports (see that page's scope section). She places it as *"an evolution of LLM-as-a-judge online evals"* on the Test/Monitor stages of [[concepts/agent-development-lifecycle|agent-development-lifecycle]].

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`** — a vendor introducing a new model class to its developer audience days after release, and mapping where it fits in the [[concepts/agent-harness|agent-harness]]. This is technology scouting done in public.

## What was actually ingested

The full transcript from the **creator-uploaded (manual) English caption track**, human-curated, so no ASR cleanup was needed. The slides themselves were not captured; the example state (*"Hi, I've been trying to connect my Stripe account for three days…"*) and the scores quoted for it (billing 0.84 with confidence 0.596; frustration score 1.035; urgency 0.999) are read aloud in the transcript.

## Linked entities and concepts

- Entities: [[LangChain]], [[TypeSafe AI]], [[Sydney Runkle]]
- Concepts: [[concepts/agent-harness|agent-harness]], [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]], [[concepts/small-language-models|small-language-models]], [[concepts/agent-development-lifecycle|agent-development-lifecycle]]

## Scope and reliability

**Vendor explainer, no measurements.** The demo is one prompt. The multipliers are TypeSafe's. The auto-mode anecdote is one person's experience, useful as a mechanism (latency as a reason to disable a gate) and not as evidence of how often it happens. The evals claim overstates its own source.
