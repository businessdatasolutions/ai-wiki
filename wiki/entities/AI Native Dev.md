---
type: entity
kind: organization
aliases: ["AI Native Dev", "AI Native DevCon"]
tags: [ai-native-dev, ai-native-devcon, conference, harness-engineering, team-design]
confidence: 0.75
last_confirmed: "2026-07-09"
accessed_at: "2026-07-09"
source_count: 2
relationships:
  - type: authored-by
    target: 2026-06-19-lopopolo-ai-native-devcon-harness-engineering
    via: "Ryan Lopopolo's AI Native DevCon talk on harness engineering (technical-harness altitude)"
  - type: authored-by
    target: 2026-07-08-foxwell-ai-native-devcon-reinvention-of-the-dev-team
    via: "Hannah Foxwell's AI Native DevCon talk on team/organizational redesign (team-and-org altitude)"
---

# AI Native Dev

**AI Native Dev** is the YouTube channel publishing talks from **AI Native DevCon** (held June 2026), a conference focused on agentic software development practice. Promoted to a wiki entity page on 9 July 2026 on its **second source under this `author:` channel value** — the channel-as-entity promotion convention (cf. [[Lenny's Podcast]], [[DeepLearningAI]], [[Y Combinator]] / *YC Root Access*).

## AI Native DevCon (the conference)

The wiki holds two sources from the June 2026 edition, spanning two distinct altitudes on the same underlying shift:

| Source | Speaker | Altitude | Substantive contribution |
|---|---|---|---|
| [[2026-06-19-lopopolo-ai-native-devcon-harness-engineering]] | [[Ryan Lopopolo]] (OpenAI) | Technical harness layer | Named definition of harness engineering; three-phase context-delivery model; shift-right review discipline |
| [[2026-07-08-foxwell-ai-native-devcon-reinvention-of-the-dev-team]] | Hannah Foxwell | Team / organizational layer | Team-ratio experiments, forward-deployed/product-engineer role patterns, minimum-viable-human for sustainable on-call, code-review discipline shift |

Together these give the wiki its first two-source view of a single AI-engineering conference across both the *how agents execute* and *how humans reorganize around them* layers — a useful structural pairing distinct from [[DeepLearningAI]]'s AI Dev 26 (educator/keynote-plus-practitioner-track altitude) or [[Y Combinator]]'s Startup School (founder/accelerator altitude).

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "ai-native-devcon")
SORT file.name ASC
```

## Open questions

- **Conference scale and curation** — the wiki has no first-party data on AI Native DevCon's size, format, or how speakers are selected; useful context for calibrating how representative its two ingested talks are of the broader event.
- **Organizer identity** — not yet established in the wiki (unclear whether AI Native Dev is an independent media outlet, a vendor-run event, or community-organized).
