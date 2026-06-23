---
type: source
kind: video
title: "How to write AI agent loops in Claude Code and Codex"
author: ["How I AI"]
url: "https://www.youtube.com/watch?v=JoXbk2fm7jM"
date_published: 2026-06-17
date_ingested: 2026-06-22
length: "~29:07 minutes (transcript ~750 ASR segments; auto-generated transcript, ASR-cleaned for proper nouns)"
raw: "../../raw/videos/how-to-write-ai-agent-loops-claude-code-codex.md"
tags: [claire-vo, how-i-ai, agent-loops, self-prompting, heartbeat, cron, hooks, goal-loop, loop-engineering, subagents, work-trees, skills, connectors, state-tracking, onboarding-an-employee, claude-code, codex, claude-cowork, routines, automations, openclaw, chatprd, addy-osmani, token-burn, agentic-engineering, agent-harness]
relationships:
  - type: supports
    target: 2026-06-19-lopopolo-ai-native-devcon-harness-engineering
    via: "Two June-2026 practitioner agentic-engineering talks at different altitudes. Lopopolo is engineer-altitude — designing harnesses so agents execute at production scale (~1M LOC, 0 hand-written lines). Vo is product-leader-altitude — making the *self-prompting loop* legible to non-engineers via the four loop types and the onboarding-an-employee framework. Both land the same load-bearing move: the human stops typing each prompt and instead designs the automation that prompts the agent."
    confidence: 0.75
  - type: supports
    target: 2026-05-15-osmani-agent-harness-engineering
    via: "Vo explicitly cites Osmani's *loop engineering* article as the best breakdown of what an effective loop needs, and reproduces its five-element checklist (work trees, skills, plugins/connectors, subagents, state). Osmani's *Ralph loop* and Vo's *goal loop* are the same self-prompting-until-done primitive named from the engineer side vs. the product side."
    confidence: 0.8
  - type: supports
    target: 2025-11-26-anthropic-effective-harnesses-long-running-agents
    via: "Vo's *goal loop* — set a measurable outcome, run the agent against it until validated or blocked — is the product-facing name for the long-running agent Anthropic engineers vendor-side. Vo's warnings (goal loops burn tokens until a too-thin validation criterion is satisfied; precise success criteria are everything) are the practitioner echo of Anthropic's reliability concerns for long-running loops."
    confidence: 0.7
---

# How to write AI agent loops in Claude Code and Codex

> I break down every loop type from scratch—what a heartbeat, cron, hook, and goal loop actually are, when each one fits, and the five things any effective loop needs before it touches production. Then I build two live loops: a daily aging-PR reviewer in Claude Code that schedules itself at 10:15 a.m. and spins off its own subagents, and a weekly skills-identification loop in Codex that spawns goal-based subagents to validate its own output in real time.
>
> *— Channel description, [[How-I-AI|How I AI]] (episode hosted by [[Claire Vo]])*

A **~29-minute explainer episode** of the [[How-I-AI|How I AI]] podcast, hosted by [[Claire Vo]] (creator of ChatPRD), demystifying the practitioner term **"loop"** — an *automated prompt*, where an agent prompts itself rather than waiting for a human to type each turn. The episode's framing claim, borrowed from a tweet by "Pete at OpenClaw," is deliberately provocative — *"prompts are out and loops are in"* — but Vo's substantive contribution is the opposite of hype: a plain-English taxonomy of loop types, a checklist of what every effective loop needs, a management mental model for *designing* loops, two live builds, and an honest set of warnings about cost. It sits at the **product-leader / accessibility** altitude of the wiki's [[agentic-engineering]] cluster, complementing the engineer-altitude treatments by [[2026-06-19-lopopolo-ai-native-devcon-harness-engineering|Lopopolo]] and [[2026-05-15-osmani-agent-harness-engineering|Osmani]].

## TL;DR

- **A loop is just an automated prompt.** The reframe: you do not need *human fingers* typing a prompt for an agent to do work. Automated prompting predates AI — we already triggered automations on schedules, crons, and webhooks; loops apply the same triggers to an LLM agent.
- **Four ways to automate a prompt** — (1) **heartbeat** (recurring interval: "every 5 min, check for a new Jira ticket"); (2) **cron** (fixed schedule: "at 9:00 a.m."); (3) **hooks** (internal-lifecycle events like tool-called / session-started, or external webhooks like "every email received"); (4) **goal** — the *new first-class loop* shipped in both [[Claude Code]] and Codex: set an outcome, run the agent until the outcome is measured-and-validated *or* the agent is blocked.
- **Five things every effective loop needs** (crediting [[Addy Osmani]]'s *loop engineering* article): **work trees** (isolate each agent's work in a sandbox), **skills** (reusable ways to do common tasks), **plugins/connectors** (the tools the agent can reach — GitHub, Slack, Google Docs/Calendar), **subagents** (federate work off the main thread, especially validation), and **state tracking** (a to-do list — markdown or Linear).
- **The "onboarding an employee" framework.** Designing a loop = designing a job. Imagine onboarding an EA, a support agent, or a software engineer and writing their recurring duties: "Every Friday, review my calendar and Slack me the follow-ups" *is* a loop; "every PR, iterate until all checks are green and it's ready to deploy" *is* a goal loop.
- **Two live builds** — (1) in Claude Code, a **daily aging-PR review routine** (10:15 a.m., local) that finds PRs open >12h, spins up a subagent thread to babysit each until merge checks are green, and Slacks the team about the rest; (2) in Codex, a **weekly skills-identification automation** that reads recent PRs/commits, proposes missing skills, and spawns **goal-based subagents** to validate each new skill against the base branch — a loop that designs and runs its own sub-loops.
- **Warnings.** Loops **burn tokens** — goal loops especially, because they run validation until a threshold *the agent decides* is met; a thin validation criterion is a money pit. And **goal/loop prompts are harder to write well** than conversational prompts — success and evaluation criteria must be precise (Vo points to OpenAI's *Using Goals in Codex* guide, and often has Codex write its own goals).

## Why this matters to the wiki

This source is the wiki's first **product-leader-altitude, non-engineer-facing** treatment of the self-prompting loop, and it does three useful things for the [[agent-harness]] / [[agentic-engineering]] cluster:

1. **A clean loop taxonomy.** Heartbeat / cron / hook / goal gives the wiki a vocabulary for *how an agent gets prompted without a human turn*. The first three are pre-AI automation triggers re-pointed at an LLM; the fourth — the **goal loop** — is the genuinely new primitive, now first-class in both [[Claude Code]] and Codex. This sharpens the [[agent-harness]] page's account of the [[react-reasoning-acting|reason–act–observe]] loop by naming the *trigger* layer that kicks the loop off.
2. **The goal loop as a named primitive.** Vo's definition — *run against a measurable outcome until validated or blocked* — is the product-facing name for the long-running agent that [[2025-11-26-anthropic-effective-harnesses-long-running-agents|Anthropic]] engineers vendor-side and that Osmani calls a *Ralph loop*. Three independent vocabularies converging on one construct is exactly the kind of cross-source ratification the wiki tracks.
3. **The "onboarding an employee" management frame.** Designing loops as *jobs to be done* is a memorable bridge between the [[automation-vs-augmentation]] discussion and the day-to-day practice of [[agentic-engineering]] — and it operationalises the recurring "manager of agents" motif (cf. [[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers|Jassy on the changing role of managers]]).

## The four loop types

| Type | Trigger | Example from the episode |
| --- | --- | --- |
| **Heartbeat** | Recurring interval | "Every 5 minutes, check for a new Jira ticket; if one exists, start a coding agent to triage and fix it." |
| **Cron** | Fixed/defined schedule | "At 9:00 a.m." — more precisely scheduled than a heartbeat's regular cadence. |
| **Hook** | Internal lifecycle event (tool-called, session-started/reset) or external webhook | "Every time I receive an email, fire a webhook and kick off an agent." |
| **Goal** | Run until outcome validated or blocked | "Iterate on this PR until all lints/checks are green and it's ready to deploy." — the new first-class loop in Claude Code (`/goal`) and Codex. |

Vo's synthesis: a loop kicks off an automatic prompt and *keeps it going until the job is done* — done either because **time's up** (scheduled loops) or because **the job's done** (goal loops) — then empowers the kicked-off agent with the isolation (work trees) and tools (connectors, subagents) it needs.

## The two live builds

- **Build #1 — Daily aging-PR review (Claude Code routine).** Runs locally, daily at 10:15 a.m., scoped to one branch. Instruction: find PRs open >12h on the ChatPRD app; for any that can be babysat, *spin up a thread* to watch the PR until merge checks are green; otherwise Slack the product channel ("be mean"). Demonstrates a **scheduled loop that spawns subagent threads** — not all work happens in the master thread.
- **Build #2 — Weekly skills-identification (Codex automation).** Built from a Codex **template**, runs Fridays weekly. Reads recent PRs/commits, proposes missing **skills** (especially around internal CLI/MCP validation tools), then *spawns a goal-based subagent per skill* to validate it against the base branch. Vo watches Codex assign named subagents (it scaffolds its own memory) and confirm a candidate — "a loop with subagents that generates its own loop." This is the episode's "mega loop": a scheduled loop → that sets up a team → that does work on goal sub-loops.

## What was actually ingested

Full ~29-minute episode transcript (auto-generated English captions, ASR-cleaned for proper nouns: OpenClaw, ChatPRD, Codex, Claude Cowork, chat-smoke CLI). Two sponsor reads (WorkOS, Runway) are present in the transcript and were not treated as content. Host identity (Claire Vo), tool names, and the Osmani/OpenClaw references were confirmed against the video description's link block, not inferred.

## Linked entities and concepts

- Concepts: [[agent-harness]], [[agentic-engineering]], [[react-reasoning-acting]], [[ai-agents]], [[automation-vs-augmentation]].
- Entities: [[Claire Vo]] (host), [[How-I-AI|How I AI]] (channel/podcast), [[Addy Osmani]] (cited for the *loop engineering* article), [[OpenAI]] (Codex), [[Anthropic]] (Claude Code / Claude Cowork).
- **Dangling** (single-source mention, deferred per the second-source promotion rule): **OpenClaw** (the agent harness whose "feels alive" framing seeded the loops discourse), **ChatPRD** (Vo's product, the demo target).

(Note: [[Claire Vo]] and [[How-I-AI|How I AI]] were promoted to entity pages on this ingest — both reached their second source here, the first being [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont|the Marily Nika episode]].)

## Related sources

- [[2026-06-19-lopopolo-ai-native-devcon-harness-engineering]] — engineer-altitude companion: designing the harness so agents execute at production scale (`supports`).
- [[2026-05-15-osmani-agent-harness-engineering]] — the *loop engineering* / *Ralph loop* article Vo explicitly cites; the five-element checklist originates here (`supports`).
- [[2025-11-26-anthropic-effective-harnesses-long-running-agents]] — vendor-engineering treatment of the long-running (goal) loop Vo names (`supports`).
