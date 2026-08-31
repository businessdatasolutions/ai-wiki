---
type: entity
kind: person
aliases: ["Claire Vo", "@clairevo"]
tags: [claire-vo, how-i-ai, chatprd, product-management, ai-pm, vibe-coding, agent-loops, prd-as-input, podcast-host, merge-mommy, code-review, risk-scoring, vercel-eve]
affiliation: "ChatPRD (founder); How I AI (host)"
role: "Product leader; founder/creator of ChatPRD (an AI PRD-authoring tool); host of the How I AI podcast"
confidence: 0.85
last_confirmed: "2026-08-31"
accessed_at: "2026-08-31"
source_count: 6
relationships:
  - type: part-of
    target: How-I-AI
    via: "host of the How I AI podcast"
---

# Claire Vo

**Product leader** and creator of **ChatPRD** (chatprd.ai), an AI tool for authoring product requirements documents that integrates with vibe-coding tools (v0 and others). She hosts the [[How-I-AI]] podcast, a practitioner show that demonstrates concrete AI workflows for product and engineering audiences.

Vo's wiki anchor is the **product-leader / non-engineer altitude** on AI practice — she consistently translates engineer-discovered patterns into management and product framings. Two motifs recur across her wiki appearances:

- **PRD-as-input, not output.** In the [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont|Marily Nika episode]] she and her guest independently converge on the claim that *"a PRD is a higher-quality input to vibe-coding tools"* — repositioning the PRD from a terminal artifact engineers read into a structured prompt-input a prototype tool consumes. ChatPRD is built around this insight.
- **Loops as designing jobs.** In her own [[2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex|How I AI explainer on agent loops]] she frames loop design as an *"onboarding an employee"* exercise: a loop is just an automated prompt, and designing one is designing a recurring job for an agent. This is the product-leader-altitude restatement of [[agentic-engineering]]'s *"agents are intern entities the human coordinates"* claim.

**Risk-scored autonomy.** Her 2026 addition to the corpus is **Merge Mommy** ([[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot]]) — a PR review agent built in a single Codex session on Vercel Eve, which reads each PR after CI passes, scores it on **six risk dimensions** (blast radius, reversibility, data security, ops impact, verification gap, change surface), auto-approves the low band and escalates the rest to Slack. It is the corpus's most explicit operational statement of *where the human checkpoint goes*, and two of its six axes turn out to be exactly what [[2026-05-14-pochampally-assistant-or-actor-delegation-regret|human-factors research]] finds drives users to withdraw trust from an agent. Her framing of the constraint is the reason it exists: once AI writes most of the code, **review capacity, not authoring capacity, is the bottleneck.**

## Appears in this wiki via

- [[2026-08-31-blum-how-i-ai-claude-cowork-pm-system]] — host; interviews Daniel Blum on his Cowork system. Notable for a reflexive turn: Blum runs *her own* loops episode through his Improve skill on camera, and the skill's critique (his scheduled tasks are already loops; he lacks goal loops) is delivered back to her live.
- [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder]] — host; interviews [[Ryan Carson]] on running 15 concurrent [[Devin]] agents, and contributes the episode's counter-argument that shipping more code does not produce better product.
- [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot]] — host/builder; Merge Mommy, the six-dimension risk-scoring PR reviewer.
- [[2026-06-22-grinstead-how-i-ai-mozilla-firefox-agentic-security-harness]] — host; interviews Mozilla's Brian Grinstead on the production agentic security-bug harness, drawing the explicit link to her own prior goal-loop episode.
- [[2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex]] — host/presenter; her own explainer on the four loop types (heartbeat / cron / hook / goal) and the five things an effective loop needs.
- [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont]] — host; guest Marily Nika demonstrates an AI-enhanced PM workflow, with Vo's running product-eye commentary (persona-debate prompting, PRD-as-input, demo-day AI judges).

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "claire-vo")
SORT file.name ASC
```

## Open questions

- **ChatPRD** is referenced across both sources but not yet its own entity (single-product, deferred). Worth promoting if a third source engages it substantively.
- Vo's relationship to the broader Lenny network (How I AI carries `lennys_howiai` campaign tags) — whether [[Lenny's Podcast]] and How I AI share a media-network edge worth recording.
