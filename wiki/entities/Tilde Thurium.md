---
type: entity
kind: person
aliases: ["Tilde Thurium"]
tags: [tilde-thurium, google-cloud, google-cloud-tech, ai-builder-essentials, developer-relations, agent-harness, loop-engineering, vendor-explainer]
affiliation: "Google Cloud (Developer Relations)"
role: "Developer advocate at Google Cloud; recurring presenter on the AI Builder Essentials series"
confidence: 0.75
last_confirmed: "2026-09-04"
accessed_at: "2026-09-04"
source_count: 3
relationships:
  - type: part-of
    target: Google
    via: "developer relations at Google Cloud; presents the AI Builder Essentials explainer series"
---

# Tilde Thurium

A **developer advocate at [[Google]] Cloud** and a recurring presenter on the **AI Builder Essentials** series on the Google Cloud Tech channel — short, two-person conversational explainers aimed at developers starting to build agents.

She is on all three of the wiki's Google Cloud harness/loop/graph videos, and her function in the format is consistent and worth naming: **she plays the sceptic**, while [[Annie Wang]] supplies the [[Agent Development Kit|ADK]]-side definitions. Thurium is the one who asks what the terms mean, admits on camera that she had confused graph engineering with knowledge graphs, and closes [[2026-09-03-thurium-wang-google-cloud-graph-engineering-101|*Graph Engineering 101*]] by asking whether the field is *"just reinventing data structures and algorithms for the agentic age"* — then proposing *"hash table engineering or stack engineering"* as the next trends. That is a vendor advocate deflating her own employer's vocabulary, and it is the most quotable first-party corroboration the corpus holds for the terminology-churn reading in [[2026-09-02-github-podcast-demystifying-ai-terms-loop-engineering-squads-harness|The GitHub Podcast]] and [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane]].

Thurium's value to this wiki is that she appears at the **definitional** layer twice, six weeks apart, in a series that states things compactly enough to quote:

- **[[2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness]]** — with Greg Baugues, the source of the corpus's most compact statement of the harness boundary (*"the harness is everything after the LLM"*). Her contribution is the **harness ≠ interface** decoupling, stated unusually sharply because it arrives as her correcting her own model on camera: *"I had been thinking of the harness as, it's like the IDE."*
- **[[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails]]** — with Annie Wang, the four-mode loop failure taxonomy. Hers is the framing that gives runaway loops their 2026 stakes (*"you're not just crashing your stack, you're burning tokens, and those cost real money"*) and the line the whole piece turns on: *"it's like asking a kindergartner to grade its own homework."*

Read together, the two sources are one argument: the July video draws the boundary, the August one populates it with the ways the loop inside it breaks. Both are vendor explainers with **no evidence of any kind** — cite Thurium for definitions and vocabulary, never for magnitudes.

**Promotion note.** Promoted 2026-09-01 on her second appearance. She does not appear in `author:` frontmatter on either source (video sources take the *channel* as author per the schema's video convention, so the automated dangling-author check cannot see presenters), which makes this a judgement call rather than a lint result — justified by her being a **named, recurring presenter carrying quotable definitional content** in both.

## Appears in this wiki via

- [[2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness]] · [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails]] · [[2026-09-03-thurium-wang-google-cloud-graph-engineering-101]]

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "tilde-thurium")
SORT file.name ASC
```
