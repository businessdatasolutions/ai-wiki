---
type: entity
kind: project
aliases: ["DORA", "DevOps Research and Assessment", "DORA report", "State of DevOps"]
tags: [dora, devops, google-cloud, delivery-metrics, throughput, stability, platform-engineering, team-profiles, annual-survey, nathen-harvey]
affiliation: "Google Cloud"
role: "Long-running research programme on software delivery performance; publisher of the annual State of DevOps / State of AI-assisted Software Development report"
confidence: 0.75
last_confirmed: "2026-08-30"
accessed_at: "2026-08-30"
source_count: 1
---

# DORA

**DevOps Research and Assessment**, now within Google Cloud — the longest-running research programme on software delivery performance, and the source of the throughput/stability metric vocabulary the industry uses.

Its **2025 report**, refocused entirely on AI, is the corpus's largest-sample source on AI in software development: nearly **5,000 technology professionals** plus 100+ hours of qualitative data. Two contributions matter here.

**The amplifier thesis:** *"AI doesn't fix a team; it amplifies what's already there."* Strong teams get more efficient; struggling teams find AI surfaces problems they already had. This is DORA's explanation for why AI-adoption studies produce such scattered effect sizes — the moderator is the delivery system, not the tool. The **seven team profiles** derived by cluster analysis are its operational form.

**The throughput/stability split:** in 2025 AI adoption's relationship with delivery **throughput** turned positive, while *"AI adoption does continue to have a negative relationship with software delivery stability."* The mechanism they name is that acceleration exposes downstream weakness: without strong automated testing, mature version control and fast feedback, higher change volume becomes instability. That single finding is the survey-scale statement of what nearly every other source in this ingest describes locally.

The **DORA AI Capabilities Model** names seven amplifying capabilities, including *fortify your safety nets* and *invest in your internal platform*; DORA's position is that internal platform quality correlates directly with the ability to unlock AI value.

Caveat worth carrying: DORA's adoption, trust and *perceived productivity* figures are self-report, and [[2025-07-10-becker-metr-early-2025-ai-experienced-developer-productivity|METR's RCT]] shows developer perception of AI productivity to be wrong by roughly 39 points for experienced developers. DORA's **delivery** metrics are behavioural and survive this.

The 2025 announcement was authored by **Nathen Harvey** (DORA Lead) and **Derek DeBellis** (Researcher).

## Appears in this wiki via

- [[2025-09-23-dora-2025-state-of-ai-assisted-software-development]]

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "dora")
SORT file.name ASC
```
