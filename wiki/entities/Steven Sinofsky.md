---
type: entity
kind: person
aliases: ["Steven Sinofsky", "Steve Sinofsky", "Sinofsky"]
tags: [steven-sinofsky, a16z, microsoft-windows, board-partner, enterprise-software, exception-handling, headless-software]
affiliation: "[[a16z]] (board partner); formerly Microsoft (led Windows)"
role: "Board partner at a16z; former President of the Windows Division at Microsoft"
confidence: 0.78
last_confirmed: "2026-07-09"
accessed_at: "2026-07-09"
source_count: 2
relationships:
  - type: part-of
    target: a16z
    via: "Board partner"
---

# Steven Sinofsky

**Steven Sinofsky** is a board partner at [[a16z]] and formerly led the Windows Division at Microsoft. Promoted to a wiki entity page on 9 July 2026 after his second appearance — first as a single quoted line in [[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Benedict Evans's Lenny's Podcast interview]], then as the primary guest on [[2026-07-07-sinofsky-amble-a16z-software-in-the-age-of-agents|a16z's own "Software in the Age of Agents" episode]].

## Role in the wiki

- **[[2026-07-07-sinofsky-amble-a16z-software-in-the-age-of-agents]]** — primary guest, in conversation with Seema Amble. Central claims: **"exception handling is the entire game"** in enterprise software (almost everything valuable is undocumented edge-case logic); **vibe-coding into enterprise fails** because the value is in embedded business logic, not the underlying database; **productivity creates new scenarios, not fewer jobs** (radiology-shortage correlation, Amazon-returns, expense-reporting-analysis examples); startup positioning advice to **aim for the middle between two incumbents** rather than compete head-on.
- **[[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going]]** — quoted once by Benedict Evans: *"incumbents always try and make the new thing a feature, and sometimes they're right, sometimes it's a feature."*

## Recurring analytical style

Consistently reasons from **historical technology-shift analogies** — the Excel-vs-Lotus-123 Goldman Sachs anecdote, the HTTP/HTML-vs-client-server comparison — to argue that incumbent software value survives disruption when it's embedded in logic/workflow rather than surface presentation, and that genuine platform shifts win by reimplementing underlying concepts differently rather than out-competing on the old terms.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```

## Open questions

- Sinofsky's own Microsoft-era writing (his *Learning by Shipping* blog, the *Hardcore Software* newsletter on the PC-era platform transitions) is not yet ingested — could sharpen the historical-analogy pattern he uses repeatedly if a future source draws on it directly.
