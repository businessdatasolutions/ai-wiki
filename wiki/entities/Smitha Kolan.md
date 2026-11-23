---
type: entity
kind: person
aliases: ["Smitha Kolan", "Smitha"]
tags: [smitha-kolan, google-cloud, google-cloud-tech, agent-factory, developer-relations, agent-development-kit, vendor-explainer]
affiliation: "Google Cloud (Developer Relations)"
role: "Developer advocate at Google Cloud; host of The Agent Factory on the Google Cloud Tech channel"
confidence: 0.7
last_confirmed: "2026-11-23"
accessed_at: "2026-11-23"
source_count: 4
relationships:
  - type: part-of
    target: Google
    via: "developer relations at Google Cloud; presents and hosts on the Google Cloud Tech channel"
---

# Smitha Kolan

A **developer advocate at [[Google]] Cloud** and the host of ***The Agent Factory***, the Google Cloud Tech channel's interview-plus-demo series on agent engineering. She is the recurring presence across four of the wiki's Google Cloud sources and, unlike [[Tilde Thurium]], her function is mostly **framing and product round-up** rather than definition.

Her four appearances split cleanly by format:

- **[[2026-06-10-google-cloud-tech-ai-agents-explained-first-agent]]** — solo tutorial. She builds a self-correcting multi-agent blog writer in Python, pairing [[react-reasoning-acting|ReAct]] theory with a live [[Agent Development Kit|ADK]] build. The only one of the four where she is the technical content rather than its host.
- **[[2026-07-06-google-cloud-agent-factory-intent-driven-development]]** — host, interviewing [[Lydia Hallie]] and [[YK Sugi]]. Her contribution is the interrogation: she is the one who puts the Hacker News craft-and-technical-debt backlash to both guests, asks whether Claude Code's expansion beyond coding was intentional, and closes the automation thread with the episode's one deflating line — on an app built to reply to someone's partner, *"maybe we're optimizing too much."*
- **[[2026-09-14-google-cloud-agent-factory-agent-harnesses-explained]]** — the product segment, and the source of the series' compressed thesis: *"your coding agent doesn't need a smarter model, it needs a better stack."*
- **[[2026-11-23-google-cloud-tech-why-agent-demos-break-in-production]]** (Nov 2026) — host of a five-presenter explainer on four layers around a coding-agent loop; her lower-third reads *Sr. DevRel Engineer, Google Cloud*. Again the framing voice: *"if you aren't scoring the system itself, you're not really engineering, you're just guessing."*

**How to cite her.** For the series' **framing claims** and as the interviewer who extracts first-party detail from guests — the permission-fatigue and Cowork-origin material in the July episode arrives in answer to her questions. Not for evidence: the format carries no measurements, and the product segments are straightforwardly promotional.

**Promotion note.** Promoted 2026-09-16 on her third appearance, clearing a **Dangling** entry carried on [[2026-09-14-google-cloud-agent-factory-agent-harnesses-explained]] and a single-mention deferral noted on the June tutorial. Her full name was first available in the July episode's channel description; the two earlier sources name her only as "Smitha". Video sources take the *channel* as `author:`, so the automated dangling-author check cannot see presenters — this is a judgement call on recurrence.

## Appears in this wiki via

- [[2026-06-10-google-cloud-tech-ai-agents-explained-first-agent]] · [[2026-07-06-google-cloud-agent-factory-intent-driven-development]] · [[2026-09-14-google-cloud-agent-factory-agent-harnesses-explained]] · [[2026-11-23-google-cloud-tech-why-agent-demos-break-in-production]]

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "smitha-kolan")
SORT file.name ASC
```
