---
type: entity
kind: organization
aliases: ["EY", "Ernst & Young", "EY.ai"]
tags: [ey, big-four, professional-services, consulting, audit, tax, frontier-firm]
website: "https://www.ey.com"
confidence: 0.75
last_confirmed: "2026-10-25"
accessed_at: "2026-10-25"
source_count: 5
---

# EY

**EY** (Ernst & Young) is one of the Big Four professional-services firms, working in audit, tax and consulting. In the wiki it appears in five roles: an incumbent describing its own AI transformation, a report sponsor, a customer, the source of a CEO survey, and a former employer.

## Role in the wiki

- **Its own transformation.** [[2025-12-16-diasio-wood-worklab-agentic-ai-corporate-ladder|Diasio on WorkLab (Dec 2025)]]: EY's Global Consulting AI Leader describes a firm of 400,000 people with 100 years of history. A couple of months after ChatGPT it set up **EY.ai** (*"move from the old business EY.com to EY.ai"*). He reports more than $1 billion invested in a year, a **Client Zero** programme that applies EY's methods to EY before its clients, and membership of the inaugural class of the Frontier Firm AI Initiative run by the [[HBS AI Institute]] with [[Microsoft]]. He names the billable hour as the firm's hardest change: *"through AI, start to break that business model."*
- **Sponsor.** [[2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs|Giles (WP Intelligence, May 2026)]]: EY paid for the free distribution of the report, which carries ads for *"EY.ai Value Blueprints."* Diasio also describes an EY *"blueprint"* for an AI-native function; neither source says whether it is the same offering.
- **Customer.** [[2026-05-05-stanford-ai-club-chamath-on-how-to-win-in-the-ai-era|Chamath at the Stanford AI Club (May 2026)]]: named as the flagship customer of 8090, which rebuilds legacy enterprise systems. The talk gives no operational detail.
- **Survey source.** [[2026-10-17-dw-shift-how-ai-is-changing-the-working-world|DW Shift (Oct 2026)]]: in an EY survey, the share of CEOs expecting AI to cause significant job cuts fell from 46% in early 2025 to 20% in May 2026.
- **Former employer.** [[2025-10-30-bornet-wood-worklab-ai-agents-leaders|Bornet]] built intelligent-automation practices at McKinsey and EY.

The Big Four are also the incumbents that AI-native tax and audit start-ups say they are targeting; see [[2026-03-07-vitucci-onshore-next-industry-ai-will-disrupt|Vitucci (Onshore)]].

## Why it is an entity (promotion note)

EY was listed as a dangling mention on three source pages (Giles, Chamath, DW Shift) and is the subject of the Diasio episode, so it was promoted on that fourth source. It is never an `author:`; the promotion follows the second-source spirit of [§Author-entity promotion](../../CLAUDE.md#author-entity-promotion) for an organisation that keeps recurring.

## Reading its sources

Most of the EY material in the wiki is EY speaking for itself (Diasio) or paying for distribution (Giles). Its figures, such as headcount, investment and its own polls, are given without method. The DW Shift survey figure is cited by a broadcaster, also without method.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```
