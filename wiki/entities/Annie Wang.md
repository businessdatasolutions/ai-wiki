---
type: entity
kind: person
aliases: ["Annie Wang"]
tags: [annie-wang, google-cloud, google-cloud-tech, ai-builder-essentials, agent-development-kit, adk, loop-engineering, graph-engineering, developer-relations, vendor-explainer]
affiliation: "Google Cloud"
role: "Presenter on the AI Builder Essentials series; the ADK-side voice in the loop- and graph-engineering explainers"
confidence: 0.7
last_confirmed: "2026-09-04"
accessed_at: "2026-09-04"
source_count: 2
relationships:
  - type: part-of
    target: Google
    via: "presents Google Cloud's AI Builder Essentials series on the Google Cloud Tech channel, speaking for the Agent Development Kit"
  - type: uses
    target: Agent-Development-Kit
    via: "ADK is the framework she explains and demonstrates throughout the series; the graph-engineering video's shared-state mechanism is described in ADK terms"
---

# Annie Wang

Presenter at [[Google]] Cloud on the **AI Builder Essentials** series, paired with [[Tilde Thurium]] in the two-person conversational explainers the wiki tracks. Promoted on the second-source rule.

The pairing is consistent across both videos and is part of what makes them useful: **Thurium plays the sceptic** — asking what the terms mean, admitting she confused graph engineering with knowledge graphs, closing the second video by asking whether the field is *"just reinventing data structures and algorithms for the agentic age"* — while **Wang supplies the [[Agent Development Kit|ADK]]-side definitions.** She is the source of most of the vocabulary the corpus quotes from this series.

Her definitions, as the wiki cites them:

- **Loop engineering** — *"you replacing yourself with a system… set a goal and let the system keep retrying until it's meeting the goal."*
- **Harness** — *"everything around the model including its tools, memory and guardrails."*
- **Graph engineering** — *"the organization chart"*: a workflow of agent nodes and function nodes, *"basically what goes in, in what order, and then what happens next."*
- **Knowledge graph vs graph engineering** — *"Knowledge Graph emphasises on the data and Graph Engineering emphasises on the behavior."*

She also supplies the corpus's sharpest one-liner on self-evaluating agents (*"it's like asking a kindergartner to grade its own homework"*), and — asked what the next vocabulary trend will be — the reply **"abstraction-maxxing."**

## Appears in this wiki via

- [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails]] — the four-mode loop failure taxonomy; the loop-engineering definition; the escalation to graph engineering.
- [[2026-09-03-thurium-wang-google-cloud-graph-engineering-101]] — the harness / loop / graph layering, the fan-out / join / router patterns, and the three disambiguations that gave the corpus its [[graph-engineering]] page.

## Referenced by

- [[2026-09-02-github-podcast-demystifying-ai-terms-loop-engineering-squads-harness]] — her loop-engineering definition is the inflationary half of the pairing the wiki draws against GitHub's deflationary one.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "annie-wang")
SORT file.name ASC
```
