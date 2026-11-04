---
type: source
kind: video
title: "How to build an agentic self improvement loop"
author: ["Warp"]
publisher: "Warp — recorded talk with product demo by Benjamin Holmes, DevEx engineering lead"
url: "https://www.youtube.com/watch?v=PMRlYAB8kkI"
date_published: 2026-11-02
date_ingested: 2026-11-04
length: "~18:34 minutes (transcript ~188 lines + 5 stills)"
raw: "../../raw/videos/how-to-build-an-agentic-self-improvement-loop.md"
stills: "../../raw/videos/how-to-build-an-agentic-self-improvement-loop.stills.md"
tags: [warp, benjamin-holmes, software-factory, warp-factories, self-improvement, outer-loop, llm-as-judge, scoring, rubrics, redundant-tests, tautological-tests, verbosity, efficiency, skill-doctor, agent-skills, traces, conversation-storage, cron, factory-as-code, ai-engineer-new-york]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: 2026-10-19-lloyd-warp-what-it-takes-to-build-a-software-factory
    via: "the scoring and self-improvement steps Lloyd lists as factory engineering, shown step by step with the rubrics, the report and the approval rate"
    confidence: 0.75
  - type: supports
    target: 2026-10-27-chase-langchain-interrupt-london-agents-improve-over-time
    via: "agents improved from traces and evals, with harness and context changes going through human review rather than applied automatically"
    confidence: 0.7
  - type: contradicts
    target: 2026-05-08-bratanic-unified-agentic-memory-hooks
    via: "how an agent should learn from past sessions: Holmes scores runs against rubrics and turns repeated failures into reviewable skill changes, 'instead of asking the agent to dream overnight or using memory systems that operate like a black box'; Bratanic distils sessions into memory in a nightly dream phase"
    confidence: 0.5
---

# Holmes (Warp) — how to build an agentic self-improvement loop

> Build a self-improvement loop for agents in 4 steps:
> 1. Aggregate your team's conversations in one place
> 2. Score runs using LLM-as-a-judge
> 3. Isolate failures
> 4. Have an agent review painpoints to suggest improvements to your skills and code architecture

## TL;DR

A 19-minute recorded talk with a product demo on the [[Warp]] channel, published 2 November 2026, a version of a talk given at AI Engineer in New York. **Benjamin Holmes**, Warp's DevEx engineering lead (*"Ben"* on camera; his full name appears in the product's sidebar), describes the *outer loop* around a software factory: the meta-engineering that makes the factory itself improve. It is the detailed version of the scoring and self-improvement steps in [[2026-10-19-lloyd-warp-what-it-takes-to-build-a-software-factory|Lloyd's talk]] on the same channel two weeks earlier. Four steps:

1. **Store every conversation where an agent can read it.** Transcripts, tool and MCP calls, and code outputs, for the whole team rather than each laptop's `~/.claude` or `~/.codex` folder. Scrappy version: everyone uploads traces to an S3 bucket on a cron; better: a cloud runner where all runs happen.
2. **Score runs with LLM judges against rubrics.** Each scorer runs in its own context window with a markdown rubric that grades from zero to one. Examples: redundant or tautological tests, verbosity in replies and code comments, and efficiency in tool calls.
3. **Isolate the failures** below a dividing line on the rubric.
4. **Have an agent propose improvements** from the failures on a schedule (*"say on a 24-hour cron job"*), citing evidence across several runs. *"It's best to have a large dataset … otherwise, it might over-index on individual failures."*

## Key claims

### Rubrics as code

A scorer is *"pretty opinionated"*: you turn a failure you keep seeing into a definition of good and bad. For tests he cites **Kent C. Dodds**'s test pyramid and **Matt Pocock**'s *tautological tests* (asserting that a constant returns its value). The efficiency rubric counts the cost to the human (*"a lot of steers in a conversation"*) and information gathering, such as an agent poking around for free port numbers before it can verify its work. Rubrics and scorers *"get checked in as code alongside everything else,"* so an agent can introspect its own setup and change it.

### Skill Doctor, single-player

Warp released the method as an open-source skill, **Skill Doctor**, for any harness. Run on his own recent conversations on a project called Hubble, it graded each one, produced a report card, and proposed skill changes with evidence. Two examples: agents repeatedly fought for a port to test on, so the fix tells the agent which environment variable overrides the port; he kept steering changelog wording, so the fix makes the changelog skill prescriptive. *"Both of these will save me time … and save tokens."*

### Warp Factories, team-wide

In the factory product, runs from the whole team are scored by a lightweight model, plotted over time per scorer, and costed; a self-improvement agent opens pull requests against the factory definition. His example: the triage agent could not spawn a subagent because of missing harness configuration, and *"kept wasting tool calls trying to figure out what was wrong."* The point of visible scores: you can see whether a shipped skill change improved anything, or whether a model change degraded a scorer. *"They'll always report back that something worked."*

## Visual canon

### 1 · Outer loop around the core factory loop

![[assets/2026-11-02-holmes-warp-agentic-self-improvement-loop/01-03m50-outer-loop-improve-the-factory.webp|Outer loop, improve the factory]]

*Still at [3:50](https://www.youtube.com/watch?v=PMRlYAB8kkI&t=230s) from Warp, "How to build an agentic self improvement loop".*

Title: **Outer loop – improve the factory**. A dashed outer circle around an inner *Core factory loop*, with four steps clockwise: **Review agent conversations → Score quality → Isolate failures → Propose improvements**, the last marked *Every 24 hr*. Side boxes: *Scoring rubrics* (✓ efficiency, ✓ code quality, ✗ test coverage); a failure note, *✗ 5 conversations wrote redundant tests*; and the proposed change, `test-writing/SKILL.md +57 −20`, *+Coverage pyramid — When to add unit vs. integration tests…*

*Still vs. transcript:* the narration names the four steps; the diagram shows the cycle as one artefact, with a worked failure (five conversations) leading to a specific diff on a skill file.

### 2 · A scorer's labels and scores

![[assets/2026-11-02-holmes-warp-agentic-self-improvement-loop/02-09m35-efficiency-rubric-labels.webp|The efficiency scorer, efficiency.md]]

*Still at [9:35](https://www.youtube.com/watch?v=PMRlYAB8kkI&t=575s) from Warp, "How to build an agentic self improvement loop".*

`skill-doctor/scorers/efficiency.md`. *name:* Efficiency. *description:* "Whether the agent worked directly toward its result, or wasted effort on redundant steps, avoidable rework, or unnecessary back-and-forth."

| Label | Description | Score |
| --- | --- | ---: |
| highly_efficient | The agent took a direct path: nothing re-read or re-run, independent steps batched, no work redone. | 1 |
| mostly_efficient | The agent slipped once or twice: a duplicated read, an early retry, or a small correction — with no knock-on cost. | 0.8 |
| mostly_inefficient | The agent wasted effort repeatedly, or caused a round of rework an earlier check would have prevented. | 0.4 |
| highly_inefficient | The agent's waste dominated the run: the same defect reworked across cycles, repeated user correction, or extended flailing / looping. | 0.2 |

Rubric (partly visible): *"You are scoring one condensed transcript of a local coding-agent conversation. Evaluate the full cost of reaching the result: the steps the agent … caused, and human attention it consumed. Score against what a competent engineer with the same tools would have needed … A mistake that looks unavoidable in context still counts if better tooling, a skill, or a check would have [prevented it] … name that cause in the reason."*

*Still vs. transcript:* the narration describes a zero-to-one scale with a failing middle; the file gives the four labels, their exact definitions and scores, and the instruction to judge against a competent engineer rather than against the agent's circumstances.

### 3 · The single-player report card

![[assets/2026-11-02-holmes-warp-agentic-self-improvement-loop/03-13m20-agent-skill-report.webp|Agent Skill Report from Skill Doctor]]

*Still at [13:20](https://www.youtube.com/watch?v=PMRlYAB8kkI&t=800s) from Warp, "How to build an agentic self improvement loop".*

**Agent Skill Report**, generated 14 October 2026, harness: codex. Grade **B**, overall 83. Efficiency 73, code quality 75, procedure compliance 80, verbosity 100, skill coverage 100. **12** conversations scored, **19** skills installed, **16** skills used. Findings (first two in full): *"Agents push to the wrong PR branch. In 3 of 12 sessions, the agent pushed to origin instead of the contributor fork, made a new upstream branch, or force-pushed a contributor's branch without asking."* *"Skills that exist do not trigger. writing-tests did not load in 3 sessions that added tests, and changelog did not load in 2 wrap-ups."*

*Still vs. transcript:* the narration mentions a report card; the still gives the scores and two findings the talk does not read out, including a safety-relevant one (force-pushing a contributor's branch) and skills that exist but never load.

### 4 · What scoring costs, per run

![[assets/2026-11-02-holmes-warp-agentic-self-improvement-loop/05-16m20-scorer-cost-and-runs.webp|Scorer cost and recent runs]]

*Still at [16:20](https://www.youtube.com/watch?v=PMRlYAB8kkI&t=980s) from Warp, "How to build an agentic self improvement loop".*

All-time scorer cost **$2,755.94**. Pass-rate trend over 30 days (23 Sep – 22 Oct 2026, UTC), mostly between about 50% and 100%, with one day at 0% (17 Oct). Agents covered: code-review, foreman, implementation, spec, triage, design. Recent runs on 22 October: four of seven failed; scores 1.0, 0.4, 0.4, 0.2, 1.0, 1.0, 0.4; run times 2 to 4.5 minutes; cost **$0.15 to $0.31 per scored run**.

*Still vs. transcript:* *"the bill is a bit higher"* becomes a figure: about $2,756 to date at roughly 15 to 31 cents a run, which is why he advises sampling and a lightweight judge.

### 5 · How many proposed changes get accepted

![[assets/2026-11-02-holmes-warp-agentic-self-improvement-loop/06-16m50-self-improvement-inbox.webp|Self-improvement inbox in Warp Factories]]

*Still at [16:50](https://www.youtube.com/watch?v=PMRlYAB8kkI&t=1010s) from Warp, "How to build an agentic self improvement loop".*

*Self-improvement* overview for the `mobile-factory`: **13/53 approved (25%)**, with the rest split between rejected and pending review, *"changes grouped by PR or review opened time."* Inbox items include *Report failed task closeout instead of silently ending*, *Deliver the final reply before completing the task*, *Keep Go module files tidy after dependency changes*, *Report only findings and unexamined dimensions in reviews*, *Handle CI failure follow-ups without a plan-only skill*.

*Still vs. transcript:* the talk presents the inbox as a stream of useful fixes; the counter shows that a person approved about one in four of the agent's proposals, so the loop as shown has a human gate with a high rejection rate.

## Dynamic-capabilities reading

- **`digital-transforming/improving-digital-maturity`**: leveraging the knowledge held in the team's own agent conversations, by storing them centrally and turning repeated failures into shared skills.

## How it connects

- [[concepts/agent-development-lifecycle|agent-development-lifecycle]] — the evaluate-and-improve stage, with scorers, sampling and cost.
- [[concepts/agent-harness|agent-harness]] — skills and harness configuration as what the loop edits.
- [[concepts/agent-fleet-management|agent-fleet-management]] — team-wide scoring of a fleet of factory agents.
- [[concepts/agentic-engineering|agentic-engineering]] — the outer loop as engineering work on the factory, not the product.

## Related in this wiki

- [[2026-10-19-lloyd-warp-what-it-takes-to-build-a-software-factory|Lloyd (Warp)]] — the factory talk that names scoring and self-improvement; this talk is its worked example.
- [[2026-10-27-chase-langchain-interrupt-london-agents-improve-over-time|Chase (LangChain, Interrupt London)]] — improvement from traces and evals, with harness changes behind human review; Warp's 25% approval rate is one measure of how much review is needed.
- [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic on agent memory with hooks]] — a nightly *dream* pass that distils sessions into memory notes. Holmes positions scoring against exactly that: *"instead of asking the agent to dream overnight or using memory systems that operate like a black box, here we get visibility into how the agent is improving."* The two differ in what is learned (scored failures turned into skill diffs, against distilled preferences and facts) and in what a person sees.
- [[2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals|Shea & Roche (LangChain)]] — judges compared on variance and cost; Warp uses one lightweight LLM judge per rubric.

## What was actually ingested

The full talk (18:34, `length_seconds: 1114`) from the transcript panel, 188 lines; the channel also carries a human-written caption track. **Stills were picked by hand**, not by the skill's Gemini scan: this machine has no Gemini key. 74 frames sampled every 15 seconds from the stream, then 6 candidates grabbed at 1080p and read at full size; 5 published, and a scorer-trend panel (efficiency 82%, code quality 22%) left out as overlapping still 4. See the manifest.

## Linked entities and concepts

- [[Warp]] — channel and publisher. Promoted to an entity page in this ingest (second `author:` source).
- [[concepts/agent-development-lifecycle|agent-development-lifecycle]], [[concepts/agent-harness|agent-harness]], [[concepts/agent-fleet-management|agent-fleet-management]], [[concepts/agentic-engineering|agentic-engineering]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the cell tagged above.

**Dangling** (single-source mention, deferred): Benjamin Holmes, Skill Doctor, Warp Factories, Kent C. Dodds, Matt Pocock, AI Engineer (New York).

## Scope and reliability

A vendor demonstrating its own product, with calls to request access. The method is general and the skill is open source, so the steps can be checked independently. The numbers on screen come from Warp's own staging factory and one engineer's project; they describe a demo, not a measured improvement. The talk claims no before-and-after figure for agent quality.
