---
type: source
kind: video
title: "How to Build Agents That Improve Over Time: Model, Harness, Context | Interrupt London"
author: ["LangChain"]
publisher: "LangChain — Interrupt London"
url: "https://www.youtube.com/watch?v=xy_7SzwsIjM"
date_published: 2026-10-27
date_ingested: 2026-10-30
length: "~20:20 minutes (transcript ~130 lines + 1 still)"
raw: "../../raw/videos/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london.md"
stills: "../../raw/videos/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london.stills.md"
tags: [langchain, harrison-chase, interrupt-london, langsmith, langsmith-engine, smithtune, fine-tuning, reinforcement-learning, deep-agents, openwiki, smithdb, traces, trajectories, evals, evals-are-the-new-prd, simulation-environments, red-teaming, hex, profound, self-improving-agents]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: 2026-10-05-chase-langchain-interrupt-nyc-opening-keynote
    via: "the same speaker a month apart on compounding, LangSmith Engine, and learning from use"
    confidence: 0.8
  - type: supports
    target: 2026-05-09-chase-agent-development-lifecycle
    via: "the same author's loop of building, testing, monitoring and iterating on agents"
    confidence: 0.75
  - type: supports
    target: 2026-05-11-karten-zhang-continual-harness-online-adaptation
    via: "automating the human-in-the-loop refinement of a harness"
    confidence: 0.6
  - type: supports
    target: 2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production
    via: "evals built from traces, and defining what good looks like for an agent"
    confidence: 0.6
---

# Chase (LangChain, Interrupt London) — agents that improve over time

> Harrison Chase, Co-Founder and CEO of LangChain, splits an agent into three parts, the model, the harness, and the context, and explains how each one can improve over time: the model's weights through supervised fine-tuning with LangSmith Fine-Tuning and its smithtune CLI, or through RL for more complex tasks; the harness through LangSmith Engine, a deep agent that runs over traces, clusters issues, and proposes fixes with a human in the loop; and the context through memory, where he points to Hex and Profound as companies he thinks do this well and to LangChain's open source OpenWiki project. He argues that traces and evals are the common foundation of all three loops, which is why LangChain built SmithDB and the new LangSmith AI Search for trace data, then covers what makes evals hard (realistic inputs, defining what good looks like, simulation environments) and how red teaming in LangSmith Engine looks for agent mistakes proactively. He closes with what he calls a North Star vision: an agent that notices its own mistakes, creates its own eval data points, and suggests its own fixes.

## TL;DR

A 20-minute talk by **[[Harrison Chase]]**, co-founder and CEO of **[[LangChain]]**, at Interrupt London. It organises agent improvement on two axes: **what** improves (model, harness, context) and **how** (by hand, with a human approving, or fully automated). Fully automated is *"maybe the North Star or the Holy Grail,"* and *"I don't think we're there right now by any stretch of the imagination."* Four claims:

1. **Each part improves differently, and context is the easiest.** Model weights are slow and costly, so almost always human-initiated. Harness changes touch code that reaches every user, so they want human review. Context is *"just text,"* and can improve per user or per organisation.
2. **Traces and evals are common to all three.** *"The hardest part of the improvement loop is oftentimes choosing what to remember and what not to remember,"* and that is domain-specific; traces and evals are where a platform can help.
3. **Evals are *"the new PRD,"* and hard.** They need realistic inputs, a definition of good and an environment to run in. There is *"not really a silver bullet."*
4. **There is no universal judge of correctness.** If there were, *"you just do it as part of the agent loop."* LangSmith's red teaming probes around that, for example by sending two semantically similar queries and investigating when the answers differ.

## Key claims

### Model

Supervised fine-tuning takes filtered traces (usually good ones) and trains on them. It suits narrow tasks such as classification, extraction and summarisation. LangSmith Fine-Tuning's `smithtune` CLI pulls and formats trajectories and hands off to Fireworks, Baseten or similar. RL runs the agent on tasks, scores rollouts and backpropagates. It has *"a higher ceiling"*, and there is *"no managed offering"* that is really good.

### Harness

The harness *"is responsible for deciding what the model sees, for actually taking the actions … for observing and verifying results, for persisting things."* The process is to read traces, identify issues and change the code, prompts or tools. **LangSmith Engine** does this in the background: it clusters traces into issues, proposes fixes, opens a PR and adds tests and eval data points. It is *"nothing more than a deep agent in a sandbox with LangSmith CLI and some specialized subagents."* A human stays in the loop.

### Context

Chase names two companies doing this well. **Hex**'s review agent finds context gaps and suggests fixes to its unified context layer. **Profound** builds *Brand Records* at company level and *Personal Records* from interactions with its AI marketer. LangChain's own experiment is **OpenWiki**, open source and built for coding: a brain for an agent, populated from the repo and updated from Codex or Claude Code traces showing what the agent struggled with.

### Traces

A **run** is one model or tool call; runs make a **trace**; traces make a **thread**; a **trajectory** is a standardised view over a thread. What matters is *"the exact inputs, the exact outputs, and the exact sequence."* Agent failures are *"semantic failures"* and *"logic failures"* that *"don't show up in traditional logs,"* which is his case for SmithDB, a database built for this data, and AI Search, which scores each trajectory against a question.

### Evals

- **Good** can be an exact match, positive or negative criteria on the answer, the end state of the environment, or the sequence of tool calls. It is *"best done by domain experts or subject matter experts."*
- **Inputs** cannot all be predicted: *"you might not know what people will even ask your agent."*
- **Environments.** You do not want evals writing to production, and *"if it's interacting with Salesforce, what do you do there?"*

Finding mistakes from production traces means they have already happened; domain experts are costly. Red teaming is the proactive route, checking correctness, security and fairness.

### The flywheel

Run the agent; get feedback from a human or an online judge; inspect the trace; add an eval data point so as not to regress; suggest a change to weights, harness or context. In the *"really future version"*, the agent does all of this itself. *"This is very much a North Star vision."*

## Dynamic-capabilities reading

- **`digital-transforming/improving-digital-maturity`**: a staged path from manual to human-approved to automated improvement, and domain experts defining what good looks like for the agents their organisation runs.

## Visual canon

### 1 · What is a harness?

![[assets/2026-10-27-chase-langchain-interrupt-london-agents-improve-over-time/06-01m41-what-is-a-harness.webp|What is a harness?]]

*Still at [1:41](https://www.youtube.com/watch?v=xy_7SzwsIjM&t=101s) from LangChain, "How to Build Agents That Improve Over Time".*

The **Model** (*Reasons → Decides*) at the centre, with:

| Box | Contents | Flow |
| --- | --- | --- |
| Context Injection | Prompts, Memory, Skills, Conversation | into the model |
| Control | Compaction, Orchestration, Ralph loops | into the model (dotted) |
| Action | Calls bash, Tools, MCP | out of the model |
| Results back to context | | into the model (dotted) |
| Persist | Filesystem, Git, Progress files | out, and back (dotted) |
| Observe & Verify | Browser screenshots, Test results, Logs | out, and back (dotted) |

*Still vs. transcript:* the items in each box, including Ralph loops, compaction and progress files, and the return paths. The narration lists only the functions. Gemini read *"Ralph loops"* as *"Reloop loops."*

## How it connects

- [[concepts/agent-development-lifecycle|agent-development-lifecycle]] — the flywheel, and how far the Monitor-to-Build hop can be automated.
- [[concepts/agent-harness|agent-harness]] — model, harness, context as the units of improvement, and the harness diagram.
- [[concepts/ai-benchmarks|ai-benchmarks]] — evals as the product definition, and red teaming without a universal judge.
- [[concepts/llm-wiki|llm-wiki]] — OpenWiki, an agent knowledge base updated from coding-agent traces.

## Related in this wiki

- [[2026-10-05-chase-langchain-interrupt-nyc-opening-keynote|Chase at Interrupt NYC]] — the product launches, including Engine v2. This talk is the framework beneath them.
- [[2026-05-09-chase-agent-development-lifecycle|Chase's Agent Development Lifecycle]] — the same loop as four phases.
- [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten & Zhang (Continual Harness)]] — a paper on removing the human from harness refinement in game-playing agents.
- [[2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production|Zamora & Feroz]] — a practitioner's evals, with failed judges on the record.
- [[2026-10-23-grinberg-gill-claude-factory-autonomous-software|Grinberg (Factory)]] — model, harness and company as *"three concentric circles."*
- [[2026-10-26-schwaibold-epstein-yc-new-full-stack-designer|Schwaibold (Shopify, YC)]] — prototypes rather than evals as what replaces the PRD.

## What was actually ingested

The full talk (20:20, `length_seconds: 1220`) from LangChain's human-written caption track via the yt-dlp fallback, 130 lines. A full static Gemini scan (118,713 tokens, 46 stills) found mostly build states of simple slides. One still is published: the 3:20 frame Gemini described as a diagram shows the speaker in front of it, and the trace and eval slides add little to the narration.

## Linked entities and concepts

- [[LangChain]], [[Harrison Chase]] — publisher and speaker. Updated in this ingest.
- [[Claude Code]] — named as a harness and as a source of traces.
- [[concepts/agent-development-lifecycle|agent-development-lifecycle]], [[concepts/agent-harness|agent-harness]], [[concepts/ai-benchmarks|ai-benchmarks]], [[concepts/llm-wiki|llm-wiki]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the one cell tagged above.

**Dangling** (single-source mention, deferred): Hex, Profound, OpenWiki, SmithDB, Fireworks, Baseten.

## Scope and reliability

A vendor CEO at his own conference; every mechanism named is a LangChain product or a customer-facing example. No outcome is reported: no figure for how much Engine's fixes or fine-tuning improved any agent. The Hex and Profound descriptions come from those firms' marketing pages, shown as slides. The framework is useful regardless, and Chase is candid that automation is a North Star, that evals have no silver bullet and that correctness has no general judge.
