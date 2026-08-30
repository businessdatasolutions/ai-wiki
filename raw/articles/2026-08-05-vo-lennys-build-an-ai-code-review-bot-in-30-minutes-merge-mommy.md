# Build an AI code review bot in 30 minutes

**Author / host / guest:** Claire Vo
**Publication:** Lenny's Newsletter (*How I AI*)
**Date:** 5 August 2026 (the ChatPRD episode index dates the video 4 August 2026)
**URL:** https://www.lennysnewsletter.com/p/build-an-ai-code-review-bot-in-30
**Captured:** 2026-08-30 (WebFetch — HTML extraction)
**fulltext_source:** web-extract

---

## What it is

**Merge Mommy** — an AI pull-request review bot Claire Vo built to address the bottleneck that appears once AI writes most of the code: **review capacity, not authoring capacity, becomes the constraint.**

## Platform

Runs on **Vercel Eve**, which Vo describes as "the simplest framework I've found for deploying AI agents in Slack and GitHub." She built the whole bot in **a single Codex session** from one prompt plus "a few steering turns," using Chrome browser automation to handle the Slack-bot and GitHub-app configuration. She argues it is **SOC 2 compatible** because "the process is auditable, queryable, and in your risk policy."

## The loop (four steps)

1. **Read** each PR after its CI checks pass
2. **Score** it across six risk dimensions
3. **Auto-approve** the low-risk ones
4. **Escalate** medium/high-risk ones to Slack for a human decision

## The six risk dimensions

- Blast radius
- Reversibility
- Data security
- Ops impact
- Verification gap
- Change surface

## Outcomes claimed

- Cleared Vo's PR backlog on deployment
- Two-click merge from the Slack escalation
- Cited comparison: **Intercom "5x'd PR approval speed and reduced revert rates"** after putting AI into their review process

## Tools referenced

Vercel Eve, Vercel AI SDK, Vercel Chat SDK, OpenAI Codex.
