---
type: entity
kind: person
aliases: ["Aron Eidelman", "Eidelman"]
tags: [aron-eidelman, google-cloud, google-cloud-tech, security-advocate, developer-security, secure-coding, test-driven-development, deterministic-gates, agent-skills, threat-modeling]
affiliation: "Google Cloud"
role: "Security Advocate, Google Cloud (on-screen lower-third, Nov 2026); described as a developer security advocate on the October 2026 livestream"
confidence: 0.7
last_confirmed: "2026-11-23"
accessed_at: "2026-11-23"
source_count: 2
relationships:
  - type: part-of
    target: Google
    via: "security advocate at Google Cloud; presents on the Google Cloud Tech channel"
---

# Aron Eidelman

A **security advocate at [[Google]] Cloud** who presents developer-security practice for coding agents on the Google Cloud Tech channel. His theme in both appearances is the same: security built into an agent's test-driven loop with deterministic checks, not added afterwards with prompts.

- **[[2026-10-20-pettit-eidelman-galloway-google-cloud-security-review-with-agents]]** (Oct 2026), livestream with Mollie Pettit and Nick Galloway: a threat-model skill at planning; failing tests that include security edge cases (*"do I get a 403"*); a *defensive developer* skill that names the project's helper methods so agents do not go on *"side quests"*; deterministic scans before any agent review. He also explains why earlier shift-left efforts failed without a top-down mandate.
- **[[2026-11-23-google-cloud-tech-why-agent-demos-break-in-production]]** (Nov 2026), the Guard layer of a four-layer explainer: *"a prompt is just advice"*; new tests must fail first; git hooks fail the run when tests are edited or coverage drops; secret scanning, static analysis and pinned, scanned dependencies against slopsquatting; raw error logs back to the agent with a retry limit of three; *"write the deterministic gate first, then update your skill file second."*

**How to cite him.** For practitioner rules on gating agent-written code. Both appearances are vendor DevRel content on Google's channel and report no measurements; the second restates the first.

**Promotion note.** Promoted 2026-11-23 on his second appearance, clearing the **Dangling** entry on the October livestream. Video sources take the channel as `author:`, so the dangling-author check cannot see presenters; this is a recurrence judgement, as for [[Smitha Kolan]]. The November video's description spells his name "Aaron"; the lower-thirds and transcript say Aron.

## Appears in this wiki via

- [[2026-10-20-pettit-eidelman-galloway-google-cloud-security-review-with-agents]] · [[2026-11-23-google-cloud-tech-why-agent-demos-break-in-production]]

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "aron-eidelman")
SORT file.name ASC
```
