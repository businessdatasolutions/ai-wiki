---
type: source
kind: video
title: "Why your AI agents keep failing, according to ClickUp's Head of AI"
author: ["Browserbase"]
publisher: "Browserbase — Navigators series, host Paul Klein IV"
url: "https://www.youtube.com/watch?v=K7vXh17lBOE"
date_published: 2026-10-28
date_ingested: 2026-10-30
length: "~38:02 minutes (transcript ~383 lines)"
raw: "../../raw/videos/why-your-ai-agents-keep-failing-according-to-clickups-head-of-ai.md"
tags: [browserbase, navigators, paul-klein, clickup, jay-hack, codegen, context-silos, context-graph, super-agents, evals, subagents, ultra-coding, skills-as-memory, programmatic-tool-calling, specialised-models, closing-the-loop, stagehand, rag, chat-interface, mechanistic-interpretability, podcast]
dynamic_capabilities:
  - contextual/internal-barriers
  - digital-seizing/balancing-digital-portfolios
relationships:
  - type: supports
    target: 2026-06-11-kilpatrick-sequoia-model-eats-the-harness
    via: "agent techniques built around current models being replaced as models improve, and a bet on the general model"
    confidence: 0.6
  - type: supports
    target: 2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet
    via: "agents using the web through a browser where no API exists; same channel and host"
    confidence: 0.65
  - type: supports
    target: 2026-10-27-chase-langchain-interrupt-london-agents-improve-over-time
    via: "evals as the first step, and smaller models trained for a firm's own subtasks"
    confidence: 0.55
---

# Hack & Klein (Browserbase, Navigators) — why agents keep failing

> Jay Hack cofounded CodeGen, one of the first companies building autonomous coding agents, before ClickUp acquired it and made him head of AI. In this episode of Navigators, Paul sits down with him to ask why, with models this capable, so few problems have actually been solved.
>
> Jay's answer centers on one word: siloing. He argues the biggest thing preventing companies from operationalizing agents isn't model quality, it's that sales data lives in Salesforce, chats live in Slack, and docs live somewhere else, each platform incentivized to keep your data locked in. ClickUp's bet is the opposite: put tasks, docs, and chat in one place, build a dense context graph on top of it, and let subagents pull from it cheaply and fast. He connects that same philosophy to why he's bullish on skills as memory, why curing cancer hits the same closed-loop problem as shipping software, and why an agent recently ordered him a pizza using nothing but a browser.

## TL;DR

A 38-minute *Navigators* interview on the [[Browserbase]] channel. **Paul Klein IV** talks with **Jay Hack**, founder of Codegen and now head of AI at **ClickUp**, which acquired it. Six claims:

1. **Silos are the biggest blocker.** Corporate America has not *"caught up to fully squeezing the juice"* from models because *"the thing that holds you back is the sort of siloing of context."* Each SaaS vendor *"has an incentive to silo your data."* ClickUp is a work suite, so it says it can build *"this very dense context graph."*
2. **Evals come first.** *"Step one, you got to have evals."* He treats the agent stack as *"a context engine"*: assembly and indexing at the bottom, then tools and compression, then specialised models.
3. **Top model plus trained subagents.** The executive function goes to a frontier model, and *"one layer beneath that, the winning paradigm right now is sub agents."* Search subagents can be trained on infinite synthetic data: a large model writes question-answer pairs from a document, and a small one is trained to find the answers.
4. **Skills are memory.** *"Skills are a first class citizen in ClickUp. It basically functions as memory."* An agent documents a repeated workflow as a skill, and it is preloaded next time.
5. **The bottleneck is closing the loop.** What stops agents curing cancer and what stops ClickUp moving faster are the same: an agent cannot run the experiment and see reality. At ClickUp that means Kubernetes clusters and security clearance, *"hard, thorny problems that at the end of the day don't even come down to technology."*
6. **Humans are close to done, on agent development.** *"When you say are we done, I take that to mean are humans done? And I think we're close."* He expects all agent and software development to be done by agents in *"a couple years,"* with people working at a higher level of abstraction, as with the C compiler.

## Key claims

### Two kinds of start-up

Either massive capital for model labs, or a *"team of like two people extremely locked in,"* running every function with hundreds of agents.

### What Codegen learned

From GPT-3.5 on, Codegen built asynchronous agents that open pull requests. Early models could do little, so it went narrow on refactors: large blast radius, simple change. *"There wasn't really enough juice to squeeze,"* it had overinvested in one type of application, and it popped out to a generalist agent. It built on existing work platforms rather than a new UI, which led to the partnership and then acquisition.

### Evolution of agent action

*"Text in, text out"*, then JSON tool calls, then **programmatic tool calling**, where the agent writes a script against an SDK. That is better because it can *"dynamically compose its own tools at runtime"* and *"pass data between different tools without it entering into context."* He has been surprised how much generalist agents rely on code for non-code tasks such as deep research.

### Ultra coding

*"When the agent programmatically spawns a bunch of sub agents to go off and complete tasks that can be verified."* His example, from memory, is a rewrite of Bun to Rust by its creator with thousands of agents and on the order of $120,000. ClickUp has used versions of it to rewrite test suites and refactor its agent tool set. He advises revisiting projects previously *"infeasible."*

### Browsers

Browser use improves with coding because *"the substructure of manipulating a browser is actually the same thing as manipulating a codebase."* An all-company demo had an agent order a pizza through a browser. Top sales requests concern systems outside ClickUp such as ServiceNow, and his fix is to *"give the agent a browser, give it your credentials … and let it rip."* Klein adds that agent identity and trust on the web are *"people problems and policy problems."*

### Overrated and underrated

- **Overrated: bespoke retrieval.** *"The RAG industrial complex … has been pretty much eradicated."* Better is good data in one place plus tools such as SQL or vector queries, with the agent deciding what to retrieve at runtime. He calls himself *"very bitter-lesson-pilled."*
- **Overrated: new interfaces.** He is *"net very bullish on chat"*, because *"people systematically overrate what they think their contribution to work will be."* Rather than build a dashboard for a person to read, the agent should read it and recommend.
- **Almost there: voice.** It sounds right, but the voice model calling a smarter model mid-conversation breaks the flow.
- **Underrated: mechanistic interpretability.** LLMs *"form a world model"* that can be influenced causally, with uses in alignment and in detecting planted behaviour in open-weight models.

## Dynamic-capabilities reading

- **`contextual/internal-barriers`**: context split across vendor silos; security clearance, credentials and development environments that keep agents from closing the loop.
- **`digital-seizing/balancing-digital-portfolios`**: frontier model on top and specialised models beneath, consolidation onto one suite, and staying open to new memory methods as labs release them.

## How it connects

- [[concepts/agent-harness|agent-harness]] — skills as memory, subagents, and evals before optimisation.
- [[concepts/ai-agents|ai-agents]] — programmatic tool calling, and agents writing code for non-code work.
- [[concepts/knowledge-graphs|knowledge-graphs]] — a *"dense context graph"* over a firm's own work data, and scepticism of pre-retrieval.
- [[concepts/small-language-models|small-language-models]] — small models trained on synthetic data for retrieval subtasks.
- [[concepts/agentic-web|agentic-web]] — a browser and credentials as the integration of last resort.
- [[concepts/agentic-engineering|agentic-engineering]] — ultra coding, and closing the development-environment loop.

## Related in this wiki

- [[2026-06-11-kilpatrick-sequoia-model-eats-the-harness|Kilpatrick (Sequoia)]] — scaffolding absorbed into the model.
- [[2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet|Klein's Navigate keynote]] — the host's own case for agents on the existing web.
- [[2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free|Ramineni (Fireflies)]] — the same series, with another software vendor.
- [[2026-10-27-chase-langchain-interrupt-london-agents-improve-over-time|Chase (Interrupt London)]] — evals, fine-tuning and the improvement loop.
- [[2026-10-25-tremante-cloudflare-connect-open-agentic-internet|Tremante (Cloudflare)]] — rails on the site side rather than browsers on the agent side.
- [[2026-10-23-grinberg-gill-claude-factory-autonomous-software|Grinberg (Factory)]] — a parallel history in coding agents, and less oversight of plans.

## What was actually ingested

The full interview (38:02, `length_seconds: 2282`) from the transcript panel, auto-generated captions, 383 lines. ASR fixed in quotes (*"codecs"* is Codex, *"Claw code"* is Claude Code). Three names in the captions are unsure and are not asserted: *"GPG 5.6 Soul"*, *"Astra"* and *"SUI 1.7"* from Cognition. The host is identified from the [[2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free|Ramineni page]]'s reading of the same series. No stills: a frame probe showed a fireside conversation.

## Linked entities and concepts

- [[Browserbase]] — publisher. Updated in this ingest.
- [[Claude Code]], [[Anthropic]], [[OpenAI]] — named as tools and model suppliers.
- [[concepts/agent-harness|agent-harness]], [[concepts/ai-agents|ai-agents]], [[concepts/knowledge-graphs|knowledge-graphs]], [[concepts/small-language-models|small-language-models]], [[concepts/agentic-web|agentic-web]], [[concepts/agentic-engineering|agentic-engineering]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the two cells tagged above.

**Dangling** (single-source mention, deferred): ClickUp, Jay Hack, Codegen, Paul Klein IV (host, never `author:`), Stagehand, Periodic Labs, Morph.

## Scope and reliability

Hack sells a consolidated suite, and his diagnosis (silos) is the problem his product addresses. He offers no benchmark for ClickUp's context graph against connected tools; when Klein asks, the answer moves on. The host sells browsers to agents and is a partner, and the pizza demo used Browserbase. The Bun figure is recalled, not sourced. *"Humans are close to done"* is a forecast from someone whose firm benefits from it, and he qualifies it within the same answer. The interview is useful for naming current patterns precisely: programmatic tool calling, skills as memory, trained subagents.
