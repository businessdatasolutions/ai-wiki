---
type: source
kind: video
title: "Mohamed Rashad - Building a production-ready agentic harness from scratch and scaling it"
author: ["PyData"]
publisher: "PyData (NumFOCUS) — conference talk by Mohamed Rashad, co-founder and engineering lead; the channel does not name the event"
url: "https://www.youtube.com/watch?v=ZrO55sK3d2I"
date_published: 2026-09-17
date_ingested: 2026-09-18
length: "~56:12 minutes (transcript ~429 segments; auto-generated captions, ASR-cleaned; ~45 min talk + ~11 min Q&A; slides not visible)"
raw: "../../raw/videos/mohamed-rashad-building-a-production-ready-agentic-harness-from-scratch-and-scaling-it.md"
tags: [mohamed-rashad, pydata, agent-harness, research-agent, embedded-runtime, run-state-machine, task-contracts, plan-versioning, agent-memory, execution-ledger, context-assembly, tool-policy, durable-execution, crash-recovery, transactional-outbox, idempotency, token-budget, latency-budget, capacity-planning, retry-probability, control-systems]
relationships:
  - type: supports
    target: 2026-05-07-kokane-agent-harness-vs-systems-design
    via: "Kokane's claim is that anyone who has shipped backend systems is 80% of the way to a harness, because retries, state machines, idempotency and observability transfer directly. Rashad's talk is that claim carried out: a run as a state machine, IDs on every step and operation, a transactional outbox before each action, and crash-point rules for which operations are safe to repeat"
    confidence: 0.85
  - type: supports
    target: 2026-05-07-anthropic-managed-agents-decoupling-brain-hands
    via: "both treat the run's record as something that must outlive the process running it. Anthropic keeps a durable session log outside the harness so a new process can wake and resume; Rashad commits each model decision to a store before the action executes, so a restarted run knows what was decided and what was already done"
    confidence: 0.75
  - type: supports
    target: 2025-11-26-anthropic-effective-harnesses-long-running-agents
    via: "resuming interrupted work without redoing it. Anthropic persists a progress file and a feature list across context windows; Rashad versions the plan (plan one, two, three) so a steered or interrupted run edits only what changed, and warns that coding agents degrade when they repeat a task they already did"
    confidence: 0.7
  - type: supports
    target: 2026-05-07-chatterjee-anatomy-of-agent-harness
    via: "contracts as the harness's organising unit. Chatterjee names contracts as formal, evaluable specifications of successful output that make failures debuggable; Rashad designs his research agent around three — an evidence contract, a completion contract and an action contract — and adds a per-task contract with an output schema and an allowed-tool list"
    confidence: 0.75
  - type: supports
    target: 2026-09-03-thurium-wang-google-cloud-graph-engineering-101
    via: "when to hand the model the graph. Rashad's three levels of planning — a fixed workflow, bounded planning over known tasks, and a fully dynamic task graph built at runtime — are the same escalation Thurium and Wang describe from loop to engineered graph, with the same trade: the more of the graph the model builds, the more contract you have to write around it"
    confidence: 0.7
---

# Rashad (PyData) — Building a production-ready agentic harness from scratch and scaling it

> www.pydata.org — PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other.

*(The channel's description is PyData boilerplate and carries no talk abstract.)*

## TL;DR

A 45-minute conference talk plus Q&A by **Mohamed Rashad**, a co-founder and engineering lead who builds AI products, on the [[PyData]] channel. It is the most backend-engineering-centred account of an [[agent-harness]] in the wiki. It builds a research agent — "similar to the deep research function" — from a single run up to a multi-user service, and it spends its time on the parts most harness writing skips: what the run's state machine looks like, what gets written to a store before an action executes, which operations are safe to repeat after a crash, and how many runs a token budget actually allows.

His framing of what a harness is: the model "cannot do anything more than the text prediction"; the harness is what you build around it "so it can take the input correctly … give me some output correctly and remember what we're doing." He draws the analogy to control engineering, where the concept comes from. His recurring observation: "usually the LLM part is the smallest part and we are trying to build many things to control it because it's nondeterministic" — so every added component should be justified, because each one adds complexity.

## Key claims

### The design, component by component

- **Three contracts first.** Before any code, the research agent needs an **evidence contract** (how evidence is extracted from web, documents or user text), a **completion contract** (when the question is answered — "give me numbers" means numbers must come back), and an **action contract** (which tools it may use: web search, local documents, asking the user).
- **Four kinds of harness.** Interactive coding environments (Codex, OpenCode), embedded runtimes that run inside an application as an SDK (the talk's focus), minimal single-loop agents, and persistent agents that remember across sessions and improve their own skills (Hermes, OpenClaw).
- **The run is the atomic unit**, modelled as a state machine: ready → claimed → active; active waits either for a tool or for user input; results, decisions or timeouts return it to active; it ends verified, failed, cancelled or budget-exhausted. "This state machine works well for 80% of the cases" — coding, research, a company's knowledge base.
- **Three levels of planning.** A fixed workflow (code it by hand or in a graph library); bounded planning, where the tasks are known and the model manages the queries fed to them; and a fully dynamic task graph built at runtime, which is what coding agents and open-ended research need. Each needs a contract — at the dynamic end, a contract on which graph operations are allowed, "so for example you don't want your agent to … remove the home directory of your MacBook." Per-task contracts carry an ID, an output schema, completion criteria and the tools allowed for that task alone, "for context one and for safety second."
- **Versioned plans make steering cheap.** Saving plan versions lets a user interrupt mid-run ("add one more requirement") and the harness edits only the affected part. A fixed workflow cannot do this and must restart.
- **Four kinds of memory**: an execution ledger (the transcript), the working state (which step finished or failed), usable memory (decisions and produced artefacts), and an evidence corpus ("what some people previously will refer as RAG"). "The recalling part is much harder than storing the data" — and pruning what is no longer relevant is the hardest part of memory design.
- **Model output as typed events**, not text: tool candidates, refusal, truncation, failure. Each tool call gets a JSON contract covering model input, harness metadata (operation, user, read/write policy) and the shapes of success and failure. "If you left it for text only, every time will give you something. I cannot guarantee the something."
- **Tool policy** accepts or rejects each action against user permissions, resource scope and action policy before it reaches a sandbox; no privilege escalation. He surveys how vendors differ — model-managed approval in Codex, JSON rules in Gemini, HTTP permissions in OpenCode, shadow git checkpoints elsewhere — and prefers rule-based decisions.

### Recovery: what gets written before the action

Every run, step, operation and artefact gets an ID, and each level has its own recovery question: which task to continue; which decision was already accepted; whether the current action is still the same intended action (a web page read ten minutes ago may have changed); and which evidence was used.

The mechanism is deliberately minimal: **one database transaction that snapshots the model's decision, plus an outbox relay, before execution.** That yields rules by crash point:

| Crash after… | Safe response |
|---|---|
| nothing committed | restart from the beginning — there is no reference |
| the outbox commit | repeat the operation, which is already recorded |
| a remote call | keep the result, or retry without new data |
| the result commit | nothing to do |

Reads can be repeated freely; writes must be checked first, because coding agents "have the tendency if they repeat the task many times it will degrade."

### Scaling: the arithmetic

- **Budget is a weight.** Nested runs (four sub-searches, three sources each, twelve concurrent calls) share one token and latency budget, weighted by how much research each branch needs.
- **Latency is the critical path**: queue time plus the slowest of the parallel operations plus the final step. Operations that finish early but cannot be used may not really be parallel.
- **Provider capacity bounds concurrency.** 120,000 tokens per minute at 10,000 tokens per run allows twelve runs; a local GPU at 1,000 tokens per second allows six. "The provider by the way is not only the cloud ones."
- **Retries are a probability, not a count.** Measure failure empirically; at a 20% failure probability, twelve runs of capacity becomes nine or ten. Assume a uniform failure distribution only until observability data (Langfuse, Grafana) shows where failures cluster — in one of his projects it was memory that failed to capture and recall, not the model.

He is explicit that the design is "not a final one. I cannot say it's an ultimate best practice cuz also this changing over the day", but reports applying it to projects of different scales.

### From the Q&A

- **Agent-to-agent communication**: a shared message board every agent reads and writes, "like Reddit or Twitter", which he says has replaced more elaborate Kafka-style designs and scales to very large agent counts.
- **Caching** of the model belongs to the provider or inference engine, not the harness; harness-level caching pays only for stateful runs over a stable corpus.
- **Compounding error** (an audience member's example: a 96%-accurate step seven layers deep gives 75%) is handled by modelling each component's failure rate from runs, not by design.
- **An open problem he names**: what happens when the agent's own configuration updates mid-run.

## Neighbour sources

[[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane (May 2026)]] argued that backend instincts — retries, state machines, idempotency, observability — transfer directly to harness engineering; this talk is that argument worked through. [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's anatomy]] names contracts as a harness layer, and Rashad designs his agent around three of them.

On recovery, [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic's managed-agents architecture]] keeps a durable session log outside the harness so a new process can resume, and [[2025-11-26-anthropic-effective-harnesses-long-running-agents|Anthropic's long-running-agents post]] persists progress across context windows; Rashad's commit-before-act transaction and versioned plans are the same concern built from database primitives.

His three planning levels match the loop-to-graph escalation in [[2026-09-03-thurium-wang-google-cloud-graph-engineering-101|Thurium & Wang's Graph Engineering 101]].

## What was actually ingested

The full auto-generated transcript, 429 segments. The caption track duplicates every timestamp as screen-reader text, which was left in the raw file. Tool and product names were ASR-cleaned (the list is in the raw file's `notes:`); the running example's city is very likely Yerevan but was left uncorrected. **The slides are not available**: the talk is built on diagrams ("this part", "here"), so the colour-coded full-harness diagram and the state-machine drawing are reconstructed from speech only. The speaker's company names are garbled in the captions and are not recorded here.

## Dynamic-capabilities reading

Not tagged. The talk is harness engineering with no organisational or digital-transformation use case attached, which is the case CLAUDE.md lists for leaving the field off.

## Linked entities and concepts

- Entities: [[PyData]]
- Concepts: [[agent-harness]], [[graph-engineering]], [[multi-agent-failure-modes]]
- **Dangling** (single-source mention, deferred): Mohamed Rashad.

## Scope and reliability

**A practitioner's reference design, not an evaluation.** No measurements of the harness itself are reported; the capacity numbers are illustrative arithmetic, not benchmarks. The crash-point rules are the speaker's design, not a surveyed consensus, and he says as much.

**The message-board claim is the weakest in the talk.** It is attributed to research work proven on "tens of thousands of agents", but the attribution is garbled in the captions and no source is given; treat it as the speaker's opinion.

**The event is not named.** PyData's channel carries no abstract or event name, and the talk's upload date (2026-09-17) is used as `date_published`; the talk itself may have been given earlier.
