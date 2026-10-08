---
type: entity
kind: organization
aliases: ["DW News", "DW", "Deutsche Welle"]
tags: [dw, deutsche-welle, news, public-broadcaster, germany, the-dip, podcasts]
website: "https://www.dw.com/en/"
confidence: 0.75
last_confirmed: "2026-10-08"
accessed_at: "2026-10-08"
source_count: 2
---

# DW News

The English-language news service of Deutsche Welle, Germany's international public broadcaster. In this wiki it appears as the publisher (and frontmatter `author:`) of two videos on its YouTube channel. Promoted to an entity on 2026-10-08, on its second source as author.

## Appears in this wiki via

- [[2026-10-01-dw-news-estonia-young-people-entry-level-jobs|Estonia: Why young people can't find entry-level jobs (Oct 2026)]]: a television report from Tallinn on youth unemployment of 22.7% against an EU average of 15.5%, with AI as one of five named causes.
- [[2026-10-04-chu-liu-dw-the-dip-how-china-is-viewing-the-ai-race|The Dip — How China is viewing the AI race (Oct 2026)]]: the business podcast *The Dip*, hosted by Kassandra Sundt, with Claire Chu (Janes) and Zongyuan Zoe Liu (Council on Foreign Relations) on China's open-weight strategy abroad, tech finance and AI governance.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(author, "DW News")
SORT file.name DESC
```
