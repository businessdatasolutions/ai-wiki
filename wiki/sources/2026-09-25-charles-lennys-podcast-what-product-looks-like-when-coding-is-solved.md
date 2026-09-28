---
type: source
kind: video
title: "What product looks like when coding is solved | Geoff Charles (Ramp CPO)"
author: ["Lenny's Podcast"]
url: "https://www.youtube.com/watch?v=ZG8Mf3P9xzI"
date_published: 2026-09-25
date_ingested: 2026-09-28
length: "~19:31 minutes (transcript ~499 segments; auto-generated captions, ASR-cleaned)"
raw: "../../raw/videos/what-product-looks-like-when-coding-is-solved-geoff-charles-ramp-cpo.md"
tags: [ramp, geoff-charles, lenny-and-friends-summit, product-management, bottlenecks, software-factory, internal-agents, coding-agents, code-review-agents, qa-agents, customer-insight, pm-role, formula-one, science-technology]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-seizing/rapid-prototyping
relationships:
  - type: supports
    target: 2026-05-08-running-an-ai-native-engineering-org
    via: "both concern the bottleneck moving away from engineering bandwidth once agents write code, and redesigning the processes around it"
    confidence: 0.8
  - type: supports
    target: 2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot
    via: "both describe an internal code-review agent built because review capacity became the constraint after AI took over authoring"
    confidence: 0.8
  - type: supports
    target: 2026-05-07-singhal-stanford-cs153-product-management-in-ai-era
    via: "both concern how the product manager's role changes in the AI era"
    confidence: 0.7
---

# Charles / Lenny's Podcast — What product looks like when coding is solved

> At Lenny and Friends Summit, Ramp's CPO Geoff Charles explains why building faster with AI means finding bottlenecks across the entire product development process. He shows how Ramp uses AI agents to uncover customer problems, shape ideas, review and test code, coordinate launches, and fix UX issues. As each bottleneck shifts, he argues that product leaders need to keep improving the system they use to build and rethink the PM's role within it.
>
> Recorded live at Lenny and Friends Summit on September 10, 2026, in San Francisco.

## TL;DR

A 19-minute conference talk on the [[Lenny's Podcast]] channel by **Geoff Charles**, chief product officer of **Ramp** (the US corporate-card and spend-management company). The talk runs on a Formula One analogy: pit stops went from 67 seconds in the 1950s to 1.8 today, *"certainly not by asking the mechanic to work 37 times harder"*, but by finding each bottleneck and removing it. His claim is that **AI does not remove the bottleneck in product development, it moves it**: *"AI simply removes the bottleneck but moves it. And the best team, the winning team is the team that can find the bottleneck faster, remove it, and move on to the next one."* Once coding got cheap, *"the bottleneck has shifted to us"*, meaning product managers: more to define, coordinate, test and release.

The body of the talk walks the product life cycle and names the internal agent Ramp built at each step. Figures are Charles's own, unaudited.

| Step | Bottleneck | Ramp's internal agent | Figure given |
| --- | --- | --- | --- |
| Identify | Customer pain spread over Gong, Zendesk, LogRocket, surveys; a 1M-token window is *"less than 0.5% of Gong transcripts at Ramp"* | A customer-insight agent (ETL, vector search, clustering), exposed as Slack bot, dashboard and a daily *"hate podcast"* | — |
| Define | A blank *"what do you want to build?"* prompt | **Glass**, connected to Snowflake, user research, strategy, spec templates and the codebase; acts as *"your tech lead"* and builds prototypes in the design system | — |
| Build | Coding | **Inspect**, an in-house coding agent in Slack returning deploy previews | *"75% of our PRs"*; ~1,000 PRs in a month from non-engineers |
| Review | Engineers combing through agent code | **Review Buddy**, which knows quality and security checks and reads the prompts that produced the code | *"93% of our PRs are now automatically handled"* |
| Test | Manual QA environments | **Testo**, a browser QA agent running the product in ~100 configurations from production data | 425 bugs caught in 30 days |
| Coordinate | Human attention; PMs flooded with questions | **Gadget**, which answers status and sales questions from Notion, Slack, Linear and tickets, updates the roadmap and pings late owners | 85% of questions to PMs answered by AI |
| Improve | PMs drawn to small reactive fixes | Autonomous loops that triage, dedupe, rank, code, test and ship small UX fixes with a light human check in Slack | 60% of UX issues fixed within 24 hours |

Two claims carry the talk beyond the table:

- **The organisation has to be legible to agents.** *"Every question is an API… For you to empower an agent, the agent needs to be able to understand and read the organization. And the organization needs to be legible to your agents."*
- **The PM role splits three ways.** The **technical PM** who builds *"the factory"* (*"They're not shipping products for the customer. They're shipping the product that helps you build the product"*), the **taste maker** who holds the quality bar, and the **GM** who owns a business outcome across marketing, sales and operations.

His closing line on budget constraints borrows Audi's Le Mans wins on fuel efficiency: *"embrace your constraints but not your bottlenecks."*

## Dynamic-capabilities reading

- **`digital-transforming/redesigning-internal-structures`** — the whole talk is about rebuilding the internal product-development process around agents, one step at a time, and about the PM role splitting into factory-builder, taste maker and GM.
- **`digital-seizing/rapid-prototyping`** — Glass produces working prototypes inside the design system and codebase, and Inspect returns a deploy preview the PM can use, so the define-to-prototype step is compressed into one session.

## How it connects

- The claim that the bottleneck moves once code is cheap is the same observation as [[2026-05-08-running-an-ai-native-engineering-org|Running an AI-native engineering org]], which argues that processes *"quietly stopped working"* once engineering bandwidth stopped being the constraint.
- Review Buddy is a company-scale instance of what [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Claire Vo's Merge Mommy]] builds in 30 minutes: an agent reviewer added because review, not authoring, became the constraint. See [[concepts/agentic-pull-requests|agentic-pull-requests]].
- The three-track PM future sits next to [[2026-05-07-singhal-stanford-cs153-product-management-in-ai-era|Nikhyl Singhal's Stanford CS153 lecture]] on product management in the AI era.
- Inspect is built in-house *"because we wanted to have a strong harness"*; see [[concepts/agent-harness|agent-harness]]. The whole setup is an example of [[concepts/agentic-engineering|agentic engineering]] extended past engineering, and a firm-level data point for [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]].
- The bottleneck-chasing frame is a plain case of [[concepts/systems-thinking|systems thinking]]: improve the constraint, then look for the next one.

## What was actually ingested

The full 19:31 talk from the auto-generated English captions, cleaned for names (Ramp was transcribed as "RAM"; Niki Lauda, Le Mans, Zendesk, LogRocket, Notion, Linear). Agent names are as heard; the spelling of "Testo" is unverified. No slides were available, so the metrics come from the spoken track only.

## Linked entities and concepts

- Entities: [[Lenny's Podcast]]
- Concepts: [[concepts/agentic-pull-requests|agentic-pull-requests]], [[concepts/agent-harness|agent-harness]], [[concepts/agentic-engineering|agentic-engineering]], [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]], [[concepts/systems-thinking|systems-thinking]]
- **Dangling** (single-source mention, deferred): Geoff Charles, Ramp

## Scope and reliability

**A conference talk by an executive about his own company, with no method behind the numbers.** The percentages (75% of PRs, 93% auto-handled reviews, 85% of questions, 60% of UX issues in 24 hours) are self-reported and undefined: "handled by Review Buddy" could mean approved, commented on or routed. Charles says himself that *"everything you've seen here is outdated"*, and that the talk is meant to be copied, so read it as a map of where one fast-moving firm has put agents, not as a measured result.
