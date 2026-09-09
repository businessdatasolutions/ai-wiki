---
type: source
kind: video
title: "Graph Engineering 101"
author: ["Google Cloud Tech"]
publisher: "Google Cloud (Google Cloud Tech YouTube channel — *AI Builder Essentials* series); speakers Tilde Thurium and Annie Wang; product referenced: Agent Development Kit (ADK). Companion codelab: https://g.dev/ai/adk-2-orchestration"
url: "https://www.youtube.com/watch?v=IrW0_f-w4kA"
date_published: 2026-09-03
date_ingested: 2026-09-04
length: "~5:56 minutes (human-curated en-US captions; 48 segments across the channel's own 6 chapters) — a two-person conversational explainer"
raw: "../../raw/videos/graph-engineering-101.md"
tags: [google-cloud, google-cloud-tech, ai-builder-essentials, tilde-thurium, annie-wang, graph-engineering, loop-engineering, agent-harness, agent-development-kit, adk, fan-out, join, router, control-flow, shared-state, agent-swarm, knowledge-graphs, graphrag, orchestration, determinism, debuggability, vendor-explainer, vocabulary-churn, abstraction-maxxing]
dynamic_capabilities:
  - digital-sensing/digital-mindset-crafting
  - digital-seizing/rapid-prototyping
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: 2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails
    via: "the direct sequel, nine days later — same channel, same series, same two presenters. The August video's fourth failure mode was *complexity overflow*, whose prescribed fix was *\"escalate from loop engineering to graph engineering… you can put loop as part of the graph\"*; this video is that escalation explained. Read as a pair they are one argument: when a single loop stops coping, here is the thing you move to and here are its three patterns"
    confidence: 0.9
  - type: supports
    target: 2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness
    via: "restates the harness boundary from the July video almost verbatim — *\"harness part is everything around the model including its tools, memory and guardrails\"* against July's *\"the harness is everything after the LLM\"* — and then nests two further constructs inside it. The three videos together are the wiki's most compact vendor statement of the harness/loop/graph layering, built one layer per video over seven weeks"
    confidence: 0.85
  - type: supports
    target: 2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-under-equal-budgets
    via: "a vendor arriving at the same restraint from the design side. Tran & Kiela show single agents beat multi-agent decompositions at equal token budgets; this video gives the condition under which the more elaborate structure is nonetheless right — *\"if you already know the workflow ahead of time\"* — and explicitly reserves the flexible, non-decomposed option (agent swarm) for problems that cannot be specified. Both push against reaching for orchestration by default"
    confidence: 0.75
  - type: supports
    target: 2026-09-02-github-podcast-demystifying-ai-terms-loop-engineering-squads-harness
    via: "the deflationary reading of the 2026 vocabulary, made by the vendor itself. The GitHub hosts spend an episode reducing new terms to older ones; this video closes with Thurium asking *\"are we just reinventing data structures and algorithms for the agentic age?\"* — answered *\"yeah, maybe\"* — and joking about *hash table engineering*, *stack engineering* and *abstraction-maxxing*. First-party corroboration that the churn is visible to the people producing it"
    confidence: 0.8
  - type: supports
    target: 2026-03-26-osmani-code-agent-orchestra-multi-agent-coding
    via: "the same PR-review workload as the corpus's orchestra source, structured deterministically rather than by role personality. Osmani's orchestra assigns specialised agents to review stages; this decomposes the same job into fan-out / join / router with the engineer specifying each node and its data shape. Useful side by side because they show the two ends of the specification spectrum this video names — engineer-defined graph versus personality-defined swarm"
    confidence: 0.7
---

# Thurium & Wang — Graph Engineering 101 (Google Cloud Tech, *AI Builder Essentials*)

> Learn about Graph Engineering and how it provides the predictability and control needed for complex, multi-agent AI systems. In this conversational breakdown, we cover the differences between: Agent harnesses, loops, and graphs; Walk through an automated pull request (PR) review pipeline using fan-out, join, and router patterns; How graph engineering differs from knowledge graphs, loop engineering, and agent swarms, and how to orchestrate shared state using Google's Agent Development Kit (ADK).
>
> *— Channel description, Google Cloud Tech (*AI Builder Essentials*); speakers Tilde Thurium and Annie Wang*

## TL;DR

Six minutes, and the **third and final layer** of an argument Google Cloud has been building one video at a time since July: [[2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness|the harness]] (16 Jul) drew the boundary, [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails|the four loop failures]] (25 Aug) populated it and named *complexity overflow* as the reason to escalate, and this (3 Sep) is the thing you escalate to.

Its value to the wiki is **not** the definition — it is the **disambiguation**. Graph engineering arrives in 2026 colliding with three neighbouring terms, and this is the corpus's first source that separates all four cleanly, on the record, from the vendor shipping the framework.

## The three-layer stack, stated in one breath

The clearest thing in the video, and the reason it earns a page:

| Layer | Wang's definition |
| --- | --- |
| **Harness** | *"everything around the model including its tools, memory and guardrails"* |
| **Loop** | *"the cycle of the agent running inside that harness"* — the LLM reasoning, deciding, picking and re-picking tools *"until it solves the problem and until it's meeting the goal"* |
| **Graph** | *"the organization chart"* — a workflow whose nodes are **agent nodes**, **function nodes** (*"which can be a deterministic logic"*) *"and more"* |

Note the harness definition is July's boundary restated with a different preposition (*around* the model rather than *after* the LLM) and the same contents. Three videos, one consistent boundary — see [[agent-harness]].

The mechanism that makes the graph a graph rather than a list:

> *"When you traverse the graph, you're passing memory or information down the graph to the next node."* — Thurium, ~1:07, confirmed by Wang

In [[Agent Development Kit|ADK]] this is **shared state**, and Wang is explicit that it exists at both granularities: *"if you build a multi-agent system we have this shared state among different agents; if you build a workflow, we have shared state among nodes in this workflow as well."*

## The worked example: PR review as fan-out → join → router

The video's one concrete artefact, and the reason it is more than a glossary. Thurium sets it up honestly — *"unfortunately yes, I hate code review"* — and the premise for using a graph at all is stated as a precondition:

> *"Because you already know exactly how to do the PR review, you know the workflow ahead of the time. So you're creating this workflow."*

| Stage | What it does |
| --- | --- |
| **Fan-out** | *"five parallel processing to pull the information for the PR"* — one task split five ways, run simultaneously, *"much faster than running them one after another"* |
| **Join** | *"basically to synthesize the result… it's waiting for the slowest processing"*, then consolidates so downstream nodes can use it |
| **Router** | takes the request input and *"routes to a different sub-agent or specialist or different workflow."* The stated condition: **if the check fails → a specialised fixer agent; if it passes → human approval** |

Thurium's analogy — a server router matching a URL to a page — is accepted by Wang as *"very similar,"* and she draws the conclusion the video is actually about:

> *"So it sounds like we're taking basic principles of control flow and applying them to AI engineering."*

Two things worth noticing about that PR pipeline, because the corpus tracks both. **The failure branch is an agent, the success branch is a human** — a risk-asymmetric gate of the kind [[agent-oversight-and-delegation]] catalogues, arrived at as a routing default rather than argued for. And it is the same workload as [[2026-03-26-osmani-code-agent-orchestra-multi-agent-coding|Osmani's orchestra]] and [[agentic-pull-requests|agentic PR review]], structured by control flow instead of by role.

## The three disambiguations

This is the part to cite.

**1. Graph engineering ≠ knowledge graphs.** Thurium admits the confusion first-hand — *"this is a little embarrassing, but when I first heard about graph engineering I thought that it was about knowledge graphs and the data model."* Wang's separation is the cleanest line in the video:

> *"A lot of terminology has graphs. We have Graph Engineering, we have GraphRAG, we have Knowledge Graph. But Knowledge Graph emphasises on the **data**, and Graph Engineering emphasises on the **behavior** — basically what goes in, in what order, and then what happens next."*

Data model versus control flow. They share a word and nothing else. See [[knowledge-graphs]].

**2. Graph engineering vs loop engineering — a complexity threshold.** *"Loop engineering, basically you have this one running loop and keep running until it's reaching the goal. And graph engineering is you're creating this graph workflow… different node and different edge to solve the problem."* The when-to-use answer is Thurium's, and it is a size heuristic rather than a principle:

> *"Loop engineering is better for simple workflows — like, I want a one paragraph summary. And graph engineering would be better for a much more complex workflow, like I need a 50 page PDF with a bunch of graphics and different shiny things."*

That is the **same example, in the same words**, that the August video used for its fourth failure mode. The pair is deliberate.

**3. Graph engineering vs agent swarms — the load-bearing distinction.** Both are *"agent orchestration patterns, but under the hood they're pretty different."*

| | **Graph engineering** | **Agent swarm** |
| --- | --- | --- |
| Who specifies | *"you as the engineer, you define each node — what happens at each step of the workflow, how the data looks and everything"* | *"each agent just gets its own personality and that's it"* |
| Node knowledge | *"an agent that's at a certain node doesn't need to know what happened before"* | agents hold the problem, not a position in it |
| What you get | *"really good predictability, debuggability and control"* | flexibility |
| When | *"problems that can be really strictly defined, like the PR workflow"* | *"not all problems are easily defined like that"* — you *"just throw the problem to them"* |

**This distinction corrects something the wiki got slightly wrong nine days ago.** [[agent-fleet-management]] resolved *squad*, *fleet*, *orchestra* and *graph* into one primitive — "role-specialised parallelism" — and told future ingests to stop proliferating sub-concepts. Three of those four still belong together. **Graph does not.** Parallelism (fan-out) is one *pattern inside* a graph, not what a graph is; a graph is engineer-specified control flow whose defining property is that node-local agents are **stateless with respect to history**, and whose payoff is determinism. A swarm of role-specialised agents is the thing graph engineering is explicitly contrasted *against*. See [[graph-engineering]], which the corpus now holds separately for exactly this reason.

## The ending, which is the most interesting 20 seconds

The video closes with the presenters deflating their own vocabulary, unprompted:

> **Thurium:** *"One last question. Are we just reinventing data structures and algorithms for the agentic age?"*
> **Wang:** *"Yeah, maybe. What trend do you think is going to be next?"*
> **Thurium:** *"Maybe hash table engineering or stack engineering. What do you think?"*
> **Wang:** *"Abstraction-maxxing."*

The corpus already holds the deflationary reading from outside the vendor cluster — [[2026-09-02-github-podcast-demystifying-ai-terms-loop-engineering-squads-harness|GitHub's developer advocates]] the day before, and [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane]] arguing most harness engineering is mature systems design on a new substrate. This is the **first-party** version: the people producing the terminology saying on camera that it may be the CS curriculum with new nouns. It does not make the terms useless — control flow really is what is being applied — but it is unusually good evidence for how to weight them.

## Dynamic capabilities (Warner & Wäger)

- **`digital-sensing/digital-mindset-crafting`** — the video's actual product is a vocabulary, aimed at changing how a developer audience parses four colliding terms (*"the words graph engineering are suddenly everywhere"*). The closing exchange is mindset-crafting against the vendor's own interest.
- **`digital-seizing/rapid-prototyping`** — it ships with a companion codelab (`g.dev/ai/adk-2-orchestration`) and points at a build-it-end-to-end tutorial; the whole series is scaffolding for getting something running rather than for deciding anything.
- **`digital-transforming/improving-digital-maturity`** — the loop→graph escalation is a maturity path: it presumes a working single-agent loop and describes the structure to move to when that loop stops coping, along with the properties (predictability, debuggability, control) that make the move worth its cost.

## Linked entities and concepts

- Concepts: [[graph-engineering]], [[agent-harness]], [[ai-agents]], [[agent-fleet-management]], [[multi-agent-failure-modes]], [[knowledge-graphs]], [[agent-oversight-and-delegation]], [[agentic-pull-requests]]
- Entities: [[Google]], [[Agent Development Kit]], [[Tilde Thurium]], [[Annie Wang]]
- **Dangling** (single-source mention, deferred): GraphRAG (as a named term distinct from the [[knowledge-graphs]] page's treatment), *AI Builder Essentials* (tracked as a series in the publisher line rather than as an entity)

## Scope and reliability

**Zero measurements.** No latency numbers, no cost comparison, no accuracy figure, no evidence that a graph-structured PR pipeline reviews better than a single loop or a human. The PR example is a diagram, not a deployment — nothing runs on camera. It is a **teaching artifact from the vendor whose framework it teaches**, and the "predictability, debuggability and control" claim is asserted rather than demonstrated.

**What it is genuinely authoritative for:** vocabulary. This is first-party Google Cloud usage of *graph engineering*, *loop engineering* and the harness boundary, from the team that ships [[Agent Development Kit|ADK]], with the fan-out / join / router pattern names attached. Cite it for **what these words mean and how they nest**; cite [[2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-under-equal-budgets|Tran & Kiela]] or [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail|MAST]] for whether the structure pays.

One small note on the artefact itself: the channel's own chapter 1 title ships with a typo — *"What is graph rngineering?"* — preserved in the raw file's `chapters:` block as published.

## Debates and supersession

- **The corpus's own conflation, corrected.** [[agent-fleet-management]]'s 2026-09-03 note treats *graph* as a fourth name for role-specialised parallelism. This source, from the vendor that coined the wiki's use of the term, contrasts graph engineering with exactly that (agent swarms) on the axis of who specifies the structure. The page has been amended and [[graph-engineering]] now holds the construct. **Not a supersession** — the squad / fleet / orchestra resolution stands; one of its four members was mis-assigned.
- **When is a graph actually justified?** The video's answer is a heuristic about output size (one paragraph vs a 50-page PDF) plus a precondition (*"you already know the workflow ahead of time"*). [[2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-under-equal-budgets|Tran & Kiela]] show that at **equal token budgets** a single agent beats decomposition, which suggests the real threshold is not output size but whether the decomposition is knowable in advance. Nobody has measured where it sits.
- **Determinism versus capability is an untested trade.** The claim that node-local agents *"don't need to know what happened before"* buys debuggability is plausible and matches the isolation prescriptions in [[agent-oversight-and-delegation]]. But [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail|MAST]]'s *inter-agent misalignment* failures and [[2025-07-13-patil-berkeley-function-calling-leaderboard|BFCL]]'s finding that memory and long-horizon state are the unsolved half both suggest that discarding history has a cost. No source in the corpus measures it.
- Open: the swarm side of the contrast is asserted and never sourced. The wiki holds no primary material on agent swarms as a named architecture — worth an ingest before the term is used as a settled category.
