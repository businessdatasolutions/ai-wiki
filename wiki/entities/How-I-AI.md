---
type: entity
kind: venue
aliases: ["How I AI", "How-I-AI", "How I AI podcast", "howiaipod"]
tags: [how-i-ai, podcast, claire-vo, ai-product-management, ai-workflows, practitioner-demos, vibe-coding, agent-loops]
since: 2025
confidence: 0.85
last_confirmed: "2026-08-31"
accessed_at: "2026-08-31"
source_count: 6
relationships:
  - type: published-by
    target: 2026-08-31-blum-how-i-ai-claude-cowork-pm-system
    via: "Daniel Blum (PM, Melio) on the Claude Cowork system running 70–80% of his workday, and the Workstation plugin that ships it to colleagues — Vo hosting (31 Aug 2026)"
  - type: published-by
    target: 2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder
    via: "Ryan Carson (solo founder, Untangle) screen-sharing his 15-concurrent-Devin-agent setup — folder priority queue, Watchdog and Land PR playbooks, and the episode's anti-thesis that more output does not make a better product (24 Aug 2026)"
  - type: published-by
    target: 2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot
    via: "Claire Vo's own build: Merge Mommy, a Vercel Eve agent that scores every PR on six risk dimensions, auto-approves the low band and escalates the rest to Slack (5 Aug 2026)"
  - type: published-by
    target: 2026-06-22-grinstead-how-i-ai-mozilla-firefox-agentic-security-harness
    via: "Brian Grinstead (Mozilla, Firefox) on the production agentic security-bug harness behind ~500 Firefox fixes — Vo hosting (22 Jun 2026)"
  - type: published-by
    target: 2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex
    via: "Claire Vo's solo explainer on the four loop types (heartbeat / cron / hook / goal) and the goal loop as a first-class primitive in Claude Code + Codex (17 Jun 2026)"
  - type: published-by
    target: 2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont
    via: "Marily Nika (Google AI Product Lead) demonstrating an end-to-end AI-enhanced PM workflow — Reddit-debate research → PRD → v0 prototype → Veo/Sora mockups (1 Dec 2025)"
---

# How I AI

A **practitioner podcast / YouTube channel** hosted by [[Claire Vo]] ([howiaipod.com](https://www.howiaipod.com/), produced by penname.co) that demonstrates concrete AI workflows for product and engineering audiences. Episodes lean toward *worked examples and live builds* rather than abstract commentary — the show's value to the wiki is the **product-leader / non-engineer altitude** on patterns the engineer-altitude sources document in more technical terms.

The wiki sources from How I AI span its range: a **guest worked-example** (Marily Nika on the AI-enhanced PM toolkit), a **host explainer** (Vo on agent loops), a **technical guest deep-dive** (Brian Grinstead on Mozilla's agentic security-bug harness), two **host and guest builds** on agent fleets and PR review (Vo's Merge Mommy; Ryan Carson's 15 concurrent agents), and a **personal-infrastructure demo** (Daniel Blum on the Cowork system running most of his workday). All translate engineer practice — vibe-coding tools, agent harnesses, self-prompting loops — into legible framings (PRD-as-input; loops as *designing jobs*; harness-as-simple-wrapper).

## Appears in this wiki via

- [[2026-08-31-blum-how-i-ai-claude-cowork-pm-system]] — guest demo: Daniel Blum's Cowork system — agent-maintained Notion board, a morning brief that asks about company jargon it doesn't know, a weekly self-improvement loop, and the Workstation onboarding plugin for all of Melio.
- [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder]] — returning guest: [[Ryan Carson]] on managing 15 concurrent [[Devin]] agents at [[Untangle]] with a folder queue and a paper priority list, plus the show's most contrarian segment on why more shipped code does not produce a better product.
- [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot]] — host build: **Merge Mommy**, a risk-scoring PR reviewer built in one Codex session, escalating medium and high risk to Slack.
- [[2026-06-22-grinstead-how-i-ai-mozilla-firefox-agentic-security-harness]] — guest deep-dive: Brian Grinstead (Mozilla) on the LLM-judge → analyzer → verifier → patch harness behind ~500 Firefox security fixes, and the ~50/50 model-vs-harness split.
- [[2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex]] — host explainer: the four loop types and the goal loop as a first-class Claude Code / Codex primitive.
- [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont]] — guest demo: Marily Nika's end-to-end AI-enhanced PM workflow.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "how-i-ai")
SORT file.name ASC
```

## Distribution and catalogue

The show is hosted by ChatPRD and distributed on YouTube, Spotify and Apple Podcasts, with written companions published on **[[Lenny's Podcast|Lenny's Newsletter]]** — the 2026 episodes ingested here appeared on both surfaces the same week, which resolves the open question below in favour of a real distribution relationship. An episode-index snapshot is held at `raw/articles/2026-08-30-chatprd-how-i-ai-episode-index.md` (captured 30 Aug 2026).

Note a **dating discrepancy** worth remembering when citing episodes: the ChatPRD index dates the Carson episode 20 August 2026 and titles it *"How Ryan Carson Manages 40 PRs a Day with Devin and Codex"*, while the YouTube release is dated 24 August 2026 and titled *"How I manage 15 AI agents 24/7 as a solo founder."* Same episode, two titles, four days apart. The wiki uses the YouTube publish date and title.

## Open questions

- Whether the newsletter relationship is formal co-publication or syndication — the campaign tag `lennys_howiai` and the same-week dual release both point to a real arrangement, but no source states its shape.
