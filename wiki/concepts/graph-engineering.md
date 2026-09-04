---
type: concept
aliases: ["graph engineering", "graph workflow", "agent graph", "workflow graph", "fan-out join router"]
tags: [graph-engineering, loop-engineering, agent-orchestration, control-flow, fan-out, join, router, shared-state, determinism, debuggability, agent-swarm, agent-development-kit, google-cloud, multi-agent]
confidence: 0.75
last_confirmed: "2026-09-04"
accessed_at: "2026-09-04"
source_count: 5
relationships:
  - type: part-of
    target: agent-harness
    via: "the graph is the orchestration layer inside the harness: harness = everything around the model, loop = the cycle running inside it, graph = the workflow of nodes those loops sit in. Google Cloud states the three-layer nesting explicitly"
  - type: uses
    target: ai-agents
    via: "agent nodes are one of the two node types in a graph, alongside function nodes carrying deterministic logic"
  - type: contradicts
    target: agent-fleet-management
    via: "the corpus resolved squad / fleet / orchestra / graph into one primitive (role-specialised parallelism) on 2026-09-03; the vendor that supplied the wiki's use of *graph* contrasts graph engineering with exactly that. Parallelism is one pattern inside a graph, not what a graph is — the defining property is engineer-specified control flow with history-free nodes"
    confidence: 0.75
  - type: depends-on
    target: multi-agent-failure-modes
    via: "the whole case for a graph is that determinism buys predictability and debuggability; whether it does is the question that literature measures, and its answer is that decomposition has costs of its own"
quality_score: 1
---

# Graph Engineering

The practice of **structuring agentic work as an explicit workflow graph** — nodes the engineer defines, edges the engineer specifies, state passed from node to node — rather than as a single agent looping until it satisfies a goal. Its stated payoff is **predictability, debuggability and control**; its precondition is that you already know the workflow before you build it.

The corpus's primary source is [[2026-09-03-thurium-wang-google-cloud-graph-engineering-101|Google Cloud's *Graph Engineering 101*]] (3 Sep 2026), the third video in an *AI Builder Essentials* arc that also supplied the wiki's harness boundary and its loop-failure taxonomy.

## The three-layer nesting

The most useful thing this vocabulary does is stack cleanly, which the wiki's three Google Cloud sources establish one layer at a time:

| Layer | What it is | Source |
| --- | --- | --- |
| **Harness** | *"everything around the model including its tools, memory and guardrails"* | [[2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness\|Baugues & Thurium, Jul 2026]] |
| **Loop** | *"the cycle of the agent running inside that harness"* — reason, decide, pick a tool, re-pick, until the goal is met | [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails\|Thurium & Wang, Aug 2026]] |
| **Graph** | *"the organization chart"* — a workflow of **agent nodes** and **function nodes** (*"which can be a deterministic logic"*) | [[2026-09-03-thurium-wang-google-cloud-graph-engineering-101\|Thurium & Wang, Sep 2026]] |

A loop can be a node in a graph — *"you can put loop as part of the graph"* — so these are not competing architectures but nested scopes. See [[agent-harness]].

The mechanism that makes traversal meaningful is **shared state**: *"when you traverse the graph, you're passing memory or information down the graph to the next node."* In [[Agent Development Kit|ADK]] this exists both across agents in a multi-agent system and across nodes in a workflow.

## The three patterns

Named in the primary source's PR-review walkthrough, and worth holding as the working vocabulary:

- **Fan-out** — split one task into *n* independent sub-tasks and run them simultaneously. *"Much faster than running them one after another and waiting for them all to finish."*
- **Join** — a synchronisation node that *"waits for the slowest processing"* and then synthesises the parallel results into something downstream nodes can consume.
- **Router** — a conditional edge: take the input, dispatch to a different sub-agent, specialist or sub-workflow. The example's condition is risk-asymmetric — **failure routes to a specialised fixer agent; success routes to human approval.**

Wang's own summary of what these are: *"we're taking basic principles of control flow and applying them to AI engineering."*

## What it is not — three disambiguations

**Not a knowledge graph.** They share a word and nothing else: *"Knowledge Graph emphasises on the **data**, and Graph Engineering emphasises on the **behavior** — basically what goes in, in what order, and then what happens next."* GraphRAG sits on the data side too. See [[knowledge-graphs]].

**Not loop engineering.** A loop is one running cycle to a goal; a graph is nodes and edges. The stated threshold is a complexity heuristic rather than a principle — a one-paragraph summary is loop work, *"a 50 page PDF with a bunch of graphics"* is graph work — and it is the same example the loop-failure taxonomy used for its *complexity overflow* mode.

**Not an agent swarm** — and this is the load-bearing contrast:

| | **Graph engineering** | **Agent swarm** |
| --- | --- | --- |
| Who specifies the structure | the engineer, node by node, including *"how the data looks"* | nobody: *"each agent just gets its own personality and that's it"* |
| Node's relationship to history | *"an agent that's at a certain node doesn't need to know what happened before"* | agents hold the problem, not a position in it |
| Payoff | *"really good predictability, debuggability and control"* | flexibility |
| Fits | *"problems that can be really strictly defined"* | *"not all problems are easily defined like that"* |

## Against the wiki's earlier resolution

On 2026-09-03 [[agent-fleet-management]] folded *squad*, *fleet*, *orchestra* and *graph* into a single primitive — role-specialised parallelism — and instructed future ingests not to proliferate sub-concepts. **Three of those four still belong together; graph does not**, and the correction comes from the vendor that supplied the wiki's use of the term.

The distinction is not pedantic. Parallelism is *one pattern inside* a graph (fan-out), while what makes a graph a graph is engineer-specified control flow over **history-free nodes**. A squad of role-specialised agents passing a task between them is much closer to the *swarm* end of the primary source's own contrast — the thing graph engineering is defined against. Resolve *squad / fleet / orchestra* to [[agent-fleet-management]]; resolve *graph* here.

## When it is actually justified

The vendor's answer is a precondition plus a size heuristic: use a graph *"if you already know the workflow ahead of time,"* and when the output is large and structured. The corpus's evidence suggests the precondition is the real criterion and the size heuristic is decoration:

- [[2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-under-equal-budgets|Tran & Kiela]] find single agents beat multi-agent decompositions **at equal token budgets**, so decomposition is not free and must be paid for by something other than parallel wall-clock.
- [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail|MAST]] locates a whole failure category in *inter-agent misalignment* — the seam between nodes is where multi-agent systems break.
- [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails|Google Cloud's own loop taxonomy]] is notable for a vendor arguing **against** reaching for the more elaborate architecture by default: escalate only when a single loop stops coping.

The convergent reading: **a graph is justified when the decomposition is knowable in advance, not when the task is big.** Nobody has measured where that threshold sits.

## The deflationary reading, from the vendor

The primary source closes with its own presenters undercutting the vocabulary:

> **Thurium:** *"Are we just reinventing data structures and algorithms for the agentic age?"* — **Wang:** *"Yeah, maybe."* — **Thurium:** *"Maybe hash table engineering or stack engineering."* — **Wang:** *"Abstraction-maxxing."*

Held next to [[2026-09-02-github-podcast-demystifying-ai-terms-loop-engineering-squads-harness|GitHub's developer advocates]] the day before and [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane]]'s argument that most harness engineering is mature systems design on a new substrate, this is the first-party version of the same claim. The terms are real and first-class in vendor materials; they are also, by their own authors' admission, control flow with new nouns. Weight them accordingly.

## Related concepts

[[agent-harness]] (the layer this sits inside) · [[ai-agents]] (agent nodes) · [[agent-fleet-management]] (the adjacent primitive it is *not*) · [[multi-agent-failure-modes]] (what breaks at the seams) · [[knowledge-graphs]] (the homonym) · [[agentic-pull-requests]] (the worked example's domain) · [[agent-oversight-and-delegation]] (the router's human-approval branch)

## Debates and supersession

- **Determinism versus capability is an untested trade.** The claim that history-free nodes buy debuggability is plausible and matches isolation prescriptions elsewhere in the corpus. But [[2025-07-13-patil-berkeley-function-calling-leaderboard|BFCL]] finds memory and long-horizon state to be the unsolved half of agentic capability, and MAST finds the seams between agents to be where systems fail. Discarding history has a cost that no source here quantifies.
- **The swarm side of the contrast is unsourced.** The wiki holds no primary material on agent swarms as a named architecture — the category enters the corpus only as the thing graph engineering is defined against. Treat *swarm* as a placeholder until a real source lands.
- **Every claim on this page is vendor-asserted.** Predictability, debuggability and control are stated, never demonstrated: no latency numbers, no cost comparison, no evidence that a graph-structured pipeline outperforms a single loop on the same job. Confidence is capped at 0.75 for that reason, per the vendor-source rule.
- Open: does the harness/loop/graph layering survive contact with other vendors' vocabularies, or is it Google Cloud's local taxonomy? [[2026-09-02-github-podcast-demystifying-ai-terms-loop-engineering-squads-harness|GitHub's hosts]] say *"there's no standard again — no standards in AI"*, which is at least consistent with the latter.
