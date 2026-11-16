---
type: entity
kind: organization
aliases: ["Reuters", "Thomson Reuters (news agency)", "Reuters Breakingviews"]
tags: [reuters, news-agency, journalism, podcasts, on-assignment, reuters-econ-world, breakingviews]
website: "https://www.reuters.com"
confidence: 0.80
last_confirmed: "2026-11-16"
accessed_at: "2026-11-16"
source_count: 3
---

# Reuters

International news agency. In this wiki it appears as the publisher (and frontmatter `author:`) of three videos on its YouTube channel: two video podcasts and one video news report. Promoted to an entity on 2026-10-08, on its second source as author.

## Appears in this wiki via

- [[2026-09-18-reuters-on-assignment-inside-chinas-ai-race|On Assignment — Inside China's AI race (Sep 2026)]]: two Reuters correspondents in China, Eduardo Baptista and Laurie Chen, on China's AI market and how Chinese models are tested before release.
- [[2026-10-07-richardson-reuters-econ-world-ai-at-work|Reuters Econ World — AI at work (Oct 2026)]]: host Carmel Crimmins interviews Nela Richardson, ADP's chief economist, on AI in payroll data. Reuters cut nine data charts into the video (ADP Research and Stanford Digital Economy Lab, OECD via Reuters Breakingviews, BLS JOLTS, Gallup and SCSP), published on the source page.
- [[2026-11-15-reuters-china-nationwide-ai-education-2030|China bets on nationwide AI education by 2030 (Nov 2026)]]: a 3:34 video report on China's target of universal AI literacy in schools by 2030, with Reuters' own review of more than 100 government procurement documents (over $31 million committed in a year).

Reuters is also cited as a news source on several other pages; those do not count toward the source count.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(author, "Reuters")
SORT file.name DESC
```
