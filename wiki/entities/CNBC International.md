---
type: entity
kind: organization
aliases: ["CNBC International", "CNBC", "Managing Asia"]
tags: [cnbc, cnbc-international, managing-asia, business-news, broadcaster, asia]
website: "https://www.cnbc.com/world/"
confidence: 0.75
last_confirmed: "2026-11-23"
accessed_at: "2026-11-23"
source_count: 2
relationships:
  - type: employs
    target: Christine-Tan
    via: "anchor and presenter of Managing Asia, interviewer on both CNBC sources in the wiki"
---

# CNBC International

The international business-news arm of CNBC. In this wiki it appears as the publisher (and frontmatter `author:`) of videos from its YouTube channel, both episodes of *Managing Asia*, a CEO-interview programme presented by [[Christine Tan]]. Promoted to an entity on 2026-11-23, on its second source as author.

## Appears in this wiki via

- [[2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells|How One of Asia's Biggest Retailers Is Reinventing the Way It Sells (May 2026)]]: Tan interviews Scott Price, CEO of DFI Retail Group, on portfolio pruning, the Yuu loyalty platform and agentic AI as a threat to the retailer's customer relationship.
- [[2026-11-20-liu-cnbc-managing-asia-foxconn-beyond-iphone|How Foxconn is moving beyond Apple's iPhone empire with AI (Nov 2026)]]: Tan interviews Young Liu, chairman of Foxconn, at Hon Hai Tech Day on AI servers, NVIDIA, no overcapacity, EVs and satellites.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(author, "CNBC International")
SORT file.name DESC
```
