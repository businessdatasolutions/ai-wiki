---
type: source
kind: video
title: "Spec-driven development: the AI engineering workflow at Notion | Ryan Nystrom"
author: ["How I AI"]
publisher: "How I AI (podcast by ChatPRD), hosted by Claire Vo; guest Ryan Nystrom, engineering manager / tech lead manager at Notion"
url: "https://www.youtube.com/watch?v=pUHA_jNwuYE"
date_published: 2026-05-11
date_ingested: 2026-09-18
length: "~47:53 minutes (transcript ~459 segments; auto-generated captions, ASR-cleaned)"
raw: "../../raw/videos/spec-driven-development-the-ai-engineering-workflow-at-notion-ryan-nystrom.md"
tags: [ryan-nystrom, claire-vo, notion, notion-ai, custom-agents, codex, claude-code, spec-driven-development, agent-specs, background-agents, boxy, software-factory, ci-speed, devex, standup, engineering-managers, verification-loop, sycophancy, progressive-disclosure]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - digital-seizing/rapid-prototyping
relationships:
  - type: supports
    target: 2026-03-23-wu-an-yc-momentic-qa-layer-ai-coding-era
    via: "the spec as source of truth, and code as its implementation. Wu calls it truth-driven development — 'your code is just an implementation detail'; Nystrom runs it inside Notion's own codebase, with an agent-specs folder of markdown files that agents implement and that are updated in place of the code. Both make the verification loop, not the code, the engineer's product"
    confidence: 0.8
  - type: supports
    target: 2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering
    via: "Ivers names under-specification as the failure AI magnifies — give it a loose requirement and it decides the corner cases for you. Nystrom's specs are the working answer: code pointers and a verification section written down before the agent starts, which is why he reports a one-shot build"
    confidence: 0.7
  - type: supports
    target: 2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex
    via: "same host, a month apart. The standup pre-read agent is a cron-triggered loop in Vo's own taxonomy — scheduled at 9:00, fanned out to subagents, writing to one permitted database — run by a manager rather than a solo builder"
    confidence: 0.75
  - type: supports
    target: 2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder
    via: "firing off many cloud agents and managing them round-robin rather than pair-programming with one. Carson runs fifteen Devin agents from a folder queue; Nystrom runs Codex in VMs he can mention from a task comment. Same shape, one inside a company's internal tooling and one in a solo founder's"
    confidence: 0.7
  - type: contradicts
    target: 2026-05-08-running-an-ai-native-engineering-org
    via: "whether the design document survives. Anthropic's Claude Code team took design docs out and put prototypes in — generate three PRs rather than argue on a whiteboard. Notion kept the document and made it the agent's input: the spec is written first, checked into the repo, and becomes the source of truth the code is regenerated from. Both remove the review meeting; they disagree on whether the written artefact goes with it"
    confidence: 0.65
---

# Nystrom & Vo — Spec-driven development: the AI engineering workflow at Notion

> Ryan Nystrom is a software engineer at Notion. He joined in December 2024 after Notion acquired Campsite, the team communication platform he co-founded with Brian Lovin. At Notion, he's been a core builder of Notion AI and the Custom Agents feature launched in February 2026. He manages a team of six to seven engineers while still writing code himself, currently running Project Afterburner, a push to cut Notion's CI time to a quarter of its current duration.
>
> *What you'll learn:* how to build a Notion AI custom agent that auto-generates your daily standup pre-read; how to configure subagents and MCP integrations within Notion AI; how Notion's internal "Boxy" system lets engineers @mention Codex from within Notion comments and get a full pull request with screenshots in 20 minutes; the spec-first development workflow; why fast CI is absolutely critical in the age of AI coding agents; how to prompt AI coding agents to defend their reasoning under pushback; why engineering managers and even senior executives should keep writing code.

## TL;DR

A 48-minute [[How-I-AI|How I AI]] episode in which [[Claire Vo]] interviews **Ryan Nystrom**, a tech lead manager at Notion, through three workflows. It is a practitioner account from inside a company that builds an agent product and also uses agents to build it.

1. **The standup nobody preps for.** A Notion AI custom agent runs at 9:00 every day and fans out to subagents: one pulls the latest CI metric through the Honeycomb MCP, others read the project Slack channel, the task database, merged pull requests and yesterday's meeting transcript. It writes a pre-read into the day's meeting page and posts a link to Slack. It has read-only access to everything except the meetings database. The meeting then discusses problems, decisions and findings rather than status. Nystrom puts the saving at about 20 minutes a day, "protecting my brain from like having to context shift."
2. **Boxy, the internal "software factory."** VMs with Codex and Claude Code installed, which an engineer invokes by @-mentioning Codex in a comment on a Notion task. A friend texted a feature request in the morning. Nystrom wrote four sentences and dropped a screenshot on a task, and about ten minutes after implementation started, Codex replied with a pull request, a preview URL and screenshots of its own UI verification. A CI type error was fixed after a reply that amounted to "I don't get this."
3. **Spec-first development.** Notion rebuilt its Notion AI agent harness — the second rewrite in about six months — because of "tool and instruction fatigue" and a bloated system prompt, borrowing skills and progressive disclosure from coding agents. The team decided to start with specs, not code. The repo now has an `agent-specs` folder of markdown documents. For the feature he shows (Ask mode, which bans all mutating tools), Nystrom dictated his idea into Whisper, had Codex turn it into a spec in the format of the existing library, revised it, then told Codex to "build it." It "basically one-shotted" a couple of thousand lines over a couple of hours.

## Key claims

**The spec is the source of truth, and the changelog.** The spec carries code pointers and a verification section, and sits in version control, so its history is "how this part of Notion AI works" in plain English. Changes are made to the spec, and the agent regenerates the code. Vo's gloss: the spec contains some code, "just not all the code", which makes it a bridge for experienced engineers into agent-written code while they keep the architecture and design work.

**Verification is the job.** Nystrom sees engineers becoming "systems thinkers and architects", and says the most important part is the verification loop: "if like the verification's a little hazy, it's like that's the first thing you should be going and doing." The team built a CLI so Codex can run Notion AI itself — send queries, toggle Ask mode, read the transcripts — once the tests pass.

**The document was always written; the waiting was the cost.** Vo: engineers wrote technical design documents anyway, then waited for review and for a meeting. "Now no more waiting for the meeting. No more waiting for review. Ship it. Have a verification loop."

**CI speed caps what agents can ship.** Fast CI mattered before agents; with agents it is "on steroids", because an agent waiting on an hour-long CI run "is just going to sit there and spin." Vo cites Stripe's roughly 1,300 agent pull requests a week and states the rule: "there is just a true mathematical limit on your capacity to ship code to production that is a reflection of how fast your CI pipeline is." She adds that "velocity plus your DevX plus your CI is a huge piece of AI adoption in engineering", and that a large engineering organisation without a VM and background-agent strategy should get one.

**Managers should write code.** Nystrom: line managers should "get in there" — not the P0 hero projects, but bugs and optimisations. Vo extends it to directors, VPs, CTOs and CPOs: "This is the era of the hard skill." She frames the automated pre-read as burnout protection — managers can code until the meeting starts instead of preparing for it.

**Why Codex, for this workflow.** Nystrom found that Claude Code "would just kind of like lose the plot" once its context window filled, while Codex "can grind for like hours"; he fires off several and manages them round-robin rather than iterating beside one. Vo adds work trees and ports "3000 through 3009 spoken for", and calls Codex a strong code and security reviewer.

**Prompting against sycophancy.** When he is out of his depth, Nystrom tells the agent "you're wrong" and asks it to defend its change with "the cited hard argument against it", because "even the best models … can sometimes be a little sycophantic."

## Dynamic-capabilities reading

- **`digital-transforming/redesigning-internal-structures`** — the team's operating rhythm is redesigned around agents: an automated pre-read replaces status updates in the daily meeting, a tech lead manager both manages six or seven engineers and writes code, and Vo argues the same for directors and executives.
- **`digital-transforming/improving-digital-maturity`** — the engineering infrastructure is treated as the adoption lever: Project Afterburner (cutting CI to a quarter), the Boxy VM fleet, a CLI that lets agents exercise the product, and Vo's claim that DevX and CI speed are "a huge piece of AI adoption in engineering."
- **`digital-seizing/rapid-prototyping`** — a feature request texted in the morning becomes a pull request with a preview environment about ten minutes after the agent starts.

## Neighbour sources

Spec-driven development already had a vendor voice in [[2026-03-23-wu-an-yc-momentic-qa-layer-ai-coding-era|Wu & An (Momentic, March 2026)]] — "the spec is the source of truth. Your code is just an implementation of that source of truth." This episode is the same practice inside a large product codebase. It also answers the under-specification failure [[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering|Ivers (SEI, May 2026)]] warns about, where a loose requirement lets the model decide the corner cases.

On the same channel, [[2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex|Vo's episode on agent loops]] gives the taxonomy the standup agent fits (a cron trigger), and [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Carson]] describes the same fire-and-manage pattern as Nystrom, outside a company.

The disagreement is with [[2026-05-08-running-an-ai-native-engineering-org|Anthropic's account of running the Claude Code team]], which took design docs out and put prototypes in. Notion kept the document and made it the agent's input. Both teams removed the review meeting; they differ on whether the written artefact survives.

## What was actually ingested

The full auto-generated transcript, 459 segments, with the channel's chapter markers as headings. Proper nouns were ASR-cleaned (Codex, Nystrom, WorkOS, Orkes, GPT-5.4, and others; the list is in the raw file's `notes:`). The screen demonstrations — the agent's instruction page, the permissions panel, the pull request and the spec file — are described in speech but not visible in the transcript. Two sponsor reads (WorkOS, Orkes) are omitted here.

## Linked entities and concepts

- Entities: [[How-I-AI]], [[Claire Vo]], [[OpenAI]] (Codex)
- Concepts: [[agentic-engineering]], [[agent-fleet-management]], [[agentic-pull-requests]], [[agent-harness]]
- **Dangling** (single-source mention, deferred): Ryan Nystrom (Notion; co-founder of Campsite). Notion as an organisation has no entity page.

## Scope and reliability

**One practitioner's workflows at one company**, from a builder of the product he demonstrates (Notion AI custom agents); the episode is a demo, not an evaluation. The time savings (20 minutes a day), the one-shot build and the 20-minute PR are self-reported, without a baseline or a failure count. The CI-capacity rule is stated as a mathematical limit but argued rather than measured; the Stripe figure is cited from another episode.

Vo's comparison of Codex and Claude Code, and Nystrom's, are preferences for their own working style, stated as such. The Boxy system is internal and, by Nystrom's account, may or may not ship as a product.
