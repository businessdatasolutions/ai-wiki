---
type: entity
kind: person
aliases: ["Sydney Runkle", "Runkle"]
tags: [langchain, open-source, product-management, agent-harness, jev, typesafe-ai]
affiliation: "[[LangChain]]"
role: "Product manager, LangChain open-source team"
confidence: 0.75
last_confirmed: "2026-09-22"
accessed_at: "2026-09-22"
source_count: 2
relationships:
  - type: part-of
    target: LangChain
    via: "product manager for LangChain's open-source team"
---

# Sydney Runkle

**Sydney Runkle** is product manager for the open-source team at [[LangChain]]. Promoted to an entity page on 22 September 2026, when she appeared on two sources in the same ingest: as lead author of a blog post and as presenter of its companion video. For the video, the `author:` field holds the channel, so her name appears in the prose.

## Role in the wiki

- **[[2026-09-17-runkle-lovell-langchain-building-a-harness-with-jev]]** (17 Sep 2026): co-author, with Hunter Lovell, of the post introducing the `langchain-typesafe` integration for [[TypeSafe AI]]'s Jev model. The post ships two harness middleware components, a model router and a tool-risk gate.
- **[[2026-09-21-runkle-langchain-building-a-harness-with-jev]]** (21 Sep 2026): presenter of the video version. It adds a first-person account of **disabling auto mode in her coding agent because the risk classifier was too slow**, and re-enabling it once a faster classifier was available. The wiki records this on [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]].

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```
