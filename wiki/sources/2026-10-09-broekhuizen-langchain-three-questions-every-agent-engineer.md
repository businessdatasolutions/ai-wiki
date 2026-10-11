---
type: source
kind: video
title: "Three Questions Every Agent Engineer Should Be Able To Answer"
author: ["LangChain"]
publisher: "LangChain (YouTube channel) — talk at LangChain's new office; speaker Jake Broekhuizen, LangChain Labs"
url: "https://www.youtube.com/watch?v=oVKGKdIAgtg"
date_published: 2026-10-09
date_ingested: 2026-10-11
length: "~14:07 minutes (transcript ~92 segments + 8 stills; manual English captions)"
raw: "../../raw/videos/three-questions-every-agent-engineer-should-be-able-to-answer.md"
stills: "../../raw/videos/three-questions-every-agent-engineer-should-be-able-to-answer.stills.md"
tags: [langchain, langchain-labs, jake-broekhuizen, own-your-intelligence, agent-evaluation, production-traces, llm-as-judge, fine-tuned-judges, environment-backed-evaluation, world-spec, task-spec, reward-hacking, rl-environments, post-training, harness-vs-model, regression-testing, gtm-agent, vendor-talk]
relationships:
  - type: supports
    target: 2026-10-05-chase-langchain-interrupt-nyc-opening-keynote
    via: "Shared topic: 'owning your own intelligence'. Chase's keynote names the phrase and its conditions at the level of a platform; Broekhuizen restates it as three engineering questions about where an agent fails, how to reproduce it, and what fixes it."
  - type: supports
    target: 2026-05-09-chase-agent-development-lifecycle
    via: "Shared topic: production traces fed back into evaluation. Chase's lifecycle has traces backfill eval datasets in the Monitor → Iterate loop; Broekhuizen describes turning traces into world and task specs."
  - type: supports
    target: 2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals
    via: "Shared topic: specialised judges as an alternative to frontier LLM-as-judge for agent evaluation. Shea and Roche test a non-generative model as judge; Broekhuizen describes a fine-tuned judge for perceived errors in production traces."
  - type: supports
    target: 2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production
    via: "Shared topic: deriving agent evaluations from production traces and scenarios rather than hand-written input/output pairs."
  - type: supports
    target: 2026-06-11-kilpatrick-sequoia-model-eats-the-harness
    via: "Shared topic: harness components being absorbed into the model layer as models improve. Broekhuizen names long-task decomposition and dynamic tool routing as examples, and treats the eval environment as the way to detect it."
---

# Broekhuizen — Three questions every agent engineer should be able to answer (LangChain, Oct 2026)

> Jake Broekhuizen of LangChain Labs argues that owning your own intelligence comes down to three questions every agent engineer should be able to answer: where is your agent failing, how can you reliably make it fail again, and what needs to happen so it stops failing. He covers using a fine-tuned judge to mine production traces when frontier LLM-as-judge evaluators get expensive at scale, building world specs and tasks that mimic production with LangChain's internal GTM agent as the example, and making fixes at both the harness and the model layer. He also explains why application teams, who see how real people use their agents, can build tasks and environments that a frontier lab never could.
>
> — channel description, LangChain (chapter list omitted)

## TL;DR

A ~14-minute talk on the **[[LangChain]]** channel, published 9 October 2026, by **Jake Broekhuizen** of **LangChain Labs**, given at an event in *"our new office"*; he mentions that a colleague, *"Charlie"*, follows him to cover post-training. The captions are the channel's human-curated English track. The talk is slide-led and the slides are denser than the narration, so this page publishes **8 verified stills**. It is a practitioner's restatement of the *own your intelligence* theme from [[2026-10-05-chase-langchain-interrupt-nyc-opening-keynote|Harrison Chase's Interrupt NYC keynote]]; the claims about LangChain's own judge and GTM agent come without numbers or method.

**1. Three questions (0:35–1:30).** *"Any person who's building an agent needs to have a very solid grasp of"*: did it fail, can we make it fail again, and what changes make it stop failing. *"If they can answer them well, then they can definitively say that they do own their own intelligence."*

**2. Did it fail? Mine production traces (1:30–2:27).** Traces hold *"a lot of valuable signal"*: a tool called correctly or incorrectly, a user frustrated *"because it didn't have the right context."* The slide (still 2) shows evaluators scanning 12,482 traces and labelling three failure classes: tool failure, loop and perceived error.

**3. Fine-tuned judges for scale (2:27–4:05).** Frontier LLM-as-judge and online evaluators are *"very effective, but also very expensive at scale"* when an agent runs *"thousands of runs a day, millions of runs a day."* LangChain fine-tuned a judge *"to go and actually classify whether or not an agent was giving users a delightful experience, whether or not there was any perceived error."* The output lets teams *"cluster the behaviors and the failure mechanisms."* This is the same direction as the [[2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals|Jev-as-a-judge experiment]]: a specialised judge in place of a frontier model.

**4. Can we make it fail again? Input/output evals are "the shallow way" (4:10–5:25).** Over *"the past six or seven months"* teams he works with have shifted. An input→output eval misses failures caused by the environment: *"the state of the database that it's interacting with, the permissions that it has access to, the particular schemas … or even the past actions that it's taken."* What is needed is *"a way for us to be able to mock out the broader application machinery of your agent as it stands in production."*

**5. World spec + task spec (5:25–7:45).** A **world spec** holds what does not change across the agent's actions (tools and APIs, domain rules, prompts and skills, shared graders); a **task spec** is one attempt (request, initial state, expected outcome, allowed actions). His example is LangChain's internal **GTM agent**, used by sellers for competitive research and pipeline work. Its world is *"Gong, Salesforce, Calendly, you know, Google Calendar"*; a task is *"research all of the Gong transcripts for a particular customer … and help me draft a next best reach-out."*

**6. Keep tasks hard and hard to game (7:45–8:41).** Coding agents that help build these worlds *"need actual constant supervision."* Tasks must be *"reliably hard"*, and there must not be *"methods where the agent has designed tasks that are easy to reward hack"* (see [[reward-hacking]]). The slide names three failure modes: leakage, difficulty and reward.

**7. The application team's data advantage (8:41–11:08).** Frontier labs can outspend app companies on data: his example is *"Google making a $10 million tender offer to Spirit Airlines not to buy the company, but to buy the internal Slack memos, the emails, the documentation"* (asserted, no source given). But *"this is a bit of a David and Goliath situation"*: application owners *"see the spiky edges around the ways that people are using their agents"* and can build tasks and environments *"that a frontier lab never could."* Turning traces into tasks is *"a data-wrangling problem"*: deduplication and quality gates.

**8. What makes it stop failing? Two layers of change (11:08–12:34).** Changes come at the **harness** (prompts, tool schemas, how context is injected) and at the **model** (post-training of your choice). Owning both is where *"owning your own intelligence … really begins to compound."* Then rerun the same task to show the fix holds.

**9. Staying ahead (12:34–13:58).** Regressions will appear as models change, and *"parts of what we designed for … will be absorbed as part of the model. … We've constantly seen parts of the harness, whether it's, you know, long task decomposition or whether it's dynamic tool routing, be absorbed into the model layer."* User interaction patterns change too; the environment is what lets you notice either.

## Visual canon

Gemini found 12 visuals. Eight are published: the three-question frame and seven diagrams. Dropped: the two build-up states of the question list (1:02, 1:20), the first frame of *Mining Production Traces* (identical to the later one), and a repeat of *World Spec + Task Spec* at 8:39. Gemini's readings matched the pixels except one trace ID, corrected below (#0441, not #0641).

### 1 · Three questions

![[assets/2026-10-09-broekhuizen-langchain-three-questions-every-agent-engineer/03-01m29-what-changes-make-it-stop-failing.webp|The three questions: did it fail, can we make it fail again, what changes make it stop failing]]

*Still at [1:29](https://www.youtube.com/watch?v=oVKGKdIAgtg&t=89s) from LangChain, "Three Questions Every Agent Engineer Should Be Able To Answer".*

01 Did it fail? · 02 Can we make it fail again? · 03 What changes make it stop failing?

*Still vs. transcript:* the narration states the questions loosely; the slide gives the exact wording that heads each later section.

### 2 · Mining production traces

![[assets/2026-10-09-broekhuizen-langchain-three-questions-every-agent-engineer/05-02m26-mining-production-traces.webp|Mining production traces: evaluators scan traces and label failures]]

*Still at [2:26](https://www.youtube.com/watch?v=oVKGKdIAgtg&t=146s).*

| `my_agent` (12,482 traces) | | Selected + labeled |
| --- | --- | --- |
| #0142 user → agent → tool · *tool error* | **Evaluators scan** (run · trace · thread) → | #0142 Tool failure |
| #0318 user → agent → tool ↻ · *loop* | | #0318 Loop |
| #0441 user → agent → user · *correction* | | #0441 Perceived error |
| #0526 user → agent → tool · *unlabeled* | | Search · cluster · promote to eval task |

*Still vs. transcript:* the slide names the three failure classes and the last step, *promote to eval task*, which links question 1 to question 2.

### 3 · Example: perceived error

![[assets/2026-10-09-broekhuizen-langchain-three-questions-every-agent-engineer/06-03m06-example-perceived-error.webp|Example of a perceived error and the judge that detects it]]

*Still at [3:06](https://www.youtube.com/watch?v=oVKGKdIAgtg&t=186s).*

- USER: Asks the agent to complete a task.
- AGENT: Returns a plausible response.
- USER: *No — check the account history first, flag the renewal risk, then draft the reply.* (callout: *Evidence about the earlier response appears later in the thread.*)

| | |
| --- | --- |
| Evidence | Explicit or inferred |
| Output | Label + explanation |
| Judge | Specialized model trained on labeled conversational traces |

**Signals across the thread:** correction · repeated request · rejected action · contradiction · acknowledged mistake · unresolved outcome.

*Still vs. transcript:* the narration says only "perceived error"; the slide defines it as a judgement made from *later* turns in the thread, and lists the six signals the judge reads.

### 4 · Reproducing agent failures

![[assets/2026-10-09-broekhuizen-langchain-three-questions-every-agent-engineer/07-04m50-reproducing-agent-failures.webp|Input-output evaluation versus environment-backed evaluation]]

*Still at [4:50](https://www.youtube.com/watch?v=oVKGKdIAgtg&t=290s).*

- **Input–output evaluation:** Input → Output → Score.
- **Environment-backed evaluation:** Initial state · Tools · Permissions → *trajectory + state transitions* → Final state → Score.

*"Context, tool semantics, permissions, and state changes may all be part of the failure being reproduced."*

*Still vs. transcript:* the slide scores the **final state** of the environment, not the output text, which the narration implies but does not say.

### 5 · World spec + task spec

![[assets/2026-10-09-broekhuizen-langchain-three-questions-every-agent-engineer/08-06m15-world-spec-task-spec.webp|World spec and task spec combine into a runnable environment]]

*Still at [6:15](https://www.youtube.com/watch?v=oVKGKdIAgtg&t=375s).*

| World spec (shared across tasks) | Task spec (one attempt) |
| --- | --- |
| Tools + APIs · Domain rules · Prompts + skills · Shared graders | User request · Initial state · Expected outcome · Allowed actions |

↓ **Runnable environment + task**

- **Leakage:** Task reveals a shortcut.
- **Difficulty:** Generated tasks are too easy.
- **Reward:** Grader rewards the wrong behavior.

*Still vs. transcript:* the two spec lists are on the slide only, and the three failure modes are named more precisely than in the narration's "hard" and "easy to reward hack".

### 6 · Turning production data into tasks

![[assets/2026-10-09-broekhuizen-langchain-three-questions-every-agent-engineer/10-09m13-turning-production-data-into-tasks.webp|Turning production data into tasks: frontier labs versus application teams]]

*Still at [9:13](https://www.youtube.com/watch?v=oVKGKdIAgtg&t=553s).*

- **Frontier labs can acquire:** demonstrations · trajectories · preference labels · verifiers · expert review.
- **Application teams observe:** real workflows · domain state · permissions and constraints · corrections · edge cases.
- → **Task candidates** (selected behavior) → 01 *Specify the task* (request · initial state · expected outcome) → 02 *Build environment + grader* (tools · permissions · state · success criteria) → 03 *Run repeated attempts* (compare trajectories, outcomes, and variance).
- **Quality gates:** Deduplicate · Remove leakage · Calibrate difficulty · Human review.

*Still vs. transcript:* the narration says "data-wrangling"; the slide gives the pipeline and its four gates, including human review.

### 7 · A fix has to beat the same failure

![[assets/2026-10-09-broekhuizen-langchain-three-questions-every-agent-engineer/11-12m21-a-fix-has-to-beat-the-same-failure.webp|A fix has to beat the same failure: harness change or model change, then validation]]

*Still at [12:21](https://www.youtube.com/watch?v=oVKGKdIAgtg&t=741s).*

- **Starting point:** reproduced failure (same task, same environment).
- **Harness change** — change the system around the model: tool schemas · context · prompts · state or memory representation · routing + control flow · model selection.
- **Model / weight change** — change the policy itself: **SFT / distillation** (strong demonstrations or target trajectories) · **RL** (a reliable reward or verifier).
- **Validation** — rerun the same task: repeated trials · held-out variants · regression tasks.

*Still vs. transcript:* the slide states what each model-layer method needs as input (demonstrations for SFT, a verifier for RL) and counts *model selection* as a harness change.

### 8 · Re-evaluating after a harness or model change

![[assets/2026-10-09-broekhuizen-langchain-three-questions-every-agent-engineer/12-13m34-re-evaluating-after-a-harness-or-model-change.webp|Re-evaluating after a harness or model change]]

*Still at [13:34](https://www.youtube.com/watch?v=oVKGKdIAgtg&t=814s).*

Harness change *or* model change → **existing tasks + environments** →

- **Known failures:** which are fixed, and which are still present?
- **Regressions:** what previously worked but now fails?
- **Harness still required?** Which prompts, tools, context, routing, or model choices can be removed or simplified?

*New production behavior updates the task and environment set.*

*Still vs. transcript:* the third question turns the eval set into a test for *removing* harness components, a step the narration only implies.

## Related in this wiki

- [[2026-10-05-chase-langchain-interrupt-nyc-opening-keynote|Chase — Interrupt NYC keynote]] introduces *own your intelligence* as LangChain's positioning; this talk is the engineering version.
- [[2026-05-09-chase-agent-development-lifecycle|Chase — the agent development lifecycle]] has traces backfill eval datasets; this talk goes one step further, from traces to whole environments.
- [[2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals|Shea & Roche — Jev as a judge]] tests a non-frontier judge; Broekhuizen reports a fine-tuned one, without numbers.
- [[2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production|Zamora & Feroz — why your agent fails in production]] builds evals from traces and scenarios on an open-source agent.
- [[2026-06-11-kilpatrick-sequoia-model-eats-the-harness|Kilpatrick — the model eats the harness]] predicts the absorption Broekhuizen reports seeing (long-task decomposition, dynamic tool routing).

## Linked entities and concepts

- Entities: [[LangChain]], [[Harrison Chase]] (via the keynote).
- Concepts: [[agent-development-lifecycle]], [[agent-harness]], [[reward-hacking]], [[ai-benchmarks]].
- **Dangling** (single-source mention, deferred): Jake Broekhuizen.

## Debates and supersession

- **Vendor talk, no figures.** The fine-tuned judge, the GTM agent and the world/task-spec method are described, not measured. The *$10 million Spirit Airlines* example is asserted without a source.
- **Where the eval set's value lives.** The talk's argument (application teams see failures that labs cannot) sits beside the [[agent-harness]] page's open question of whether harness work is durable or gets absorbed by the model. Broekhuizen holds both: components get absorbed, and the trace-derived environment is what survives the change.

## What was actually ingested

The full 14:07 talk, from the channel's human-curated English caption track, fetched with yt-dlp after the transcript panel failed to render. The Gemini still scan found 12 visuals; all were viewed and 8 are published here as webp.
