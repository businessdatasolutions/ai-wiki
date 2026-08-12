---
type: entity
kind: person
aliases: ["Jonathan Allen"]
tags: [jonathan-allen, aws, executive-in-residence, agentic-team-structures]
affiliation: "Amazon Web Services — Executive in Residence"
role: "AWS Executive in Residence; former divisional CTO, Capital One"
confidence: 0.75
last_confirmed: "2026-07-14"
accessed_at: "2026-07-14"
source_count: 2
---

# Jonathan Allen

**AWS Executive in Residence**, with over eight years at [[Amazon Web Services|AWS]] as of mid-2026. Previously spent eight years at Capital One, ending as divisional Chief Technology Officer during the bank's cloud migration. The third holder of the AWS "Executive in Residence" title to appear in the wiki, after Jana Werner and Phil Le-Brun. Works alongside colleague **Stephen Brozovich / [[Steven Brovich]]** (see that entity page's alias note); together they and colleagues have spent over eight years working with 1,000+ AWS customers.

Delivers a recurring executive-forum keynote — **"A leader's guide to advanced team structures in an agentic world"** — on organizational design for agentic AI, first given at AWS re:Invent 2025 and revised across at least two later editions:

- [[2025-12-02-allen-brozovich-davis-aws-reinvent-advanced-team-structures|AWS re:Invent 2025]] (2 Dec 2025, Las Vegas) — the origin deck. Co-presented with Stephen Brozovich (Amazon org-science research) and customer Richard Davis (CTO, Danske Bank).
- [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|AWS London Executive Forum 2026]] (21 May 2026) — a revised edition ("400 hours of revision" per Allen's own disclosure), adding the USE/COMPOSE/BUILD framework, the hourglass-organization term, the moats-erosion thesis, and Project Mantle. Co-presented with customer Nick Francis (Brooklyn Solutions).

Recurring framing devices across editions: the peanut-butter-and-jam cloud/agile metaphor; Scott Galloway's "AI won't take your job, someone using AI will"; the MIT NANDA 95%-of-AI-pilots-fail citation; Martin Fowler's expert-generalist talent thesis; builders-to-orchestrators as the central leadership mental-model shift; non-determinism as "a feature, not a bug."

**Promoted to an entity page on the 2026-07-14 ingest** of the re:Invent edition, per the [second-source rule](../../CLAUDE.md#author-entity-promotion) — first cited (dangling) on the London source page.

## Appears in this wiki via

- [[2025-12-02-allen-brozovich-davis-aws-reinvent-advanced-team-structures]] — headline keynote speaker (~0:00–27:43), origin edition of the "advanced team structures" talk.
- [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures]] — headline keynote speaker (~0:07–33:20), revised edition.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "jonathan-allen")
SORT file.name ASC
```

## Open questions

- Does Allen's talk have further editions beyond re:Invent 2025 → London May 2026 (e.g. a version predating re:Invent, or later than London)?
- Who is "Johnny," referenced by Allen in the re:Invent edition as the speaker of a companion "leader's guide to agentic AI" session — a different person, not yet identified or ingested?
