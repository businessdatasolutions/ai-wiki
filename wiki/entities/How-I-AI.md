---
type: entity
kind: venue
aliases: ["How I AI", "How-I-AI", "How I AI podcast", "howiaipod"]
tags: [how-i-ai, podcast, claire-vo, ai-product-management, ai-workflows, practitioner-demos, vibe-coding, agent-loops]
since: 2025
confidence: 0.8
last_confirmed: "2026-06-23"
accessed_at: "2026-06-23"
source_count: 3
relationships:
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

The wiki sources from How I AI span its range: a **guest worked-example** (Marily Nika on the AI-enhanced PM toolkit), a **host explainer** (Vo on agent loops), and a **technical guest deep-dive** (Brian Grinstead on Mozilla's agentic security-bug harness). All translate engineer practice — vibe-coding tools, agent harnesses, self-prompting loops — into legible framings (PRD-as-input; loops as *designing jobs*; harness-as-simple-wrapper).

## Appears in this wiki via

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

## Open questions

- Whether How I AI sits inside the broader [[Lenny's Podcast|Lenny]] media network (the campaign tag `lennys_howiai` in episode descriptions suggests a distribution relationship) — worth a typed edge if a source confirms it.
