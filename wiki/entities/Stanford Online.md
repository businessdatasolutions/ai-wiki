---
type: entity
kind: organization
aliases: ["Stanford Online", "Stanford Online YouTube"]
tags: [stanford, education-channel, mooc, academic-lecture, online-education]
parent: "[[Stanford University]]"
website: "https://online.stanford.edu"
confidence: 0.85
last_confirmed: "2026-08-12"
accessed_at: "2026-08-12"
source_count: 6
---

# Stanford Online

**Stanford Online** is Stanford University's online-education delivery channel, encompassing the YouTube channel of the same name that publishes recorded lectures, conference talks, and course material from Stanford's graduate and professional programmes. The channel hosts material from foundational ML courses, frontier-systems guest lectures, and applied-AI programmes.

Promoted from Dangling to an entity page on 12 May 2026 after appearing as `author:` in two ingested sources.

## Role in the wiki

**Bumped to source_count: 6 on 12 August 2026** with two further Stanford recordings that widen the channel's range considerably. [[2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1|CS329A *Self-Improving AI Agents*, Part 1]] (published 3 Aug 2026; **lecture delivered 22 September 2025**) is a graduate course overview by **Aakanksha Chowdhery** and **Azalia Mirhoseini** covering scaling laws and their stated saturation, the post-training stack that separated ChatGPT from GPT-3, and the pivot the course is built on — inference as a frontier, via Mirhoseini's *Large Language Monkeys* repeated-sampling result — closing on verification as the binding bottleneck. [[2026-07-13-haghighi-stanford-cs547-toward-ontological-multiplicity-in-ai|CS547 HCI Seminar — *Toward Ontological Multiplicity in AI and Computing*]] (published 13 Jul 2026; **seminar delivered 15 May 2026**) is a doctoral job-talk by **Nava Haghighi** on how ontological assumptions get encoded into systems and then "risk becoming everyone's reality" — the wiki's first source at that altitude.

Note the **publication-lag pattern** this channel exhibits: both 2026 additions were recorded months before release (eleven months, in CS329A's case). Time-sensitive claims about the state of the art should be read against the delivery date recorded on each source page, not the publication date the filename carries.

The wiki has ingested two Stanford Online sources representing **two distinct course traditions**:

### 1. CS224W — Machine Learning with Graphs ([[2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings|Leskovec 2023]])

[[Jure Leskovec]]'s academic-foundation lecture on **knowledge graph embeddings** (TransE / TransR / DistMult / ComplEx; KG-completion task; relation-pattern taxonomy; FreeBase scale-and-incompleteness anchor). **The wiki's oldest video source by publish date** (December 2023) — pre-GenAI-era foundational reference for the [[knowledge-graphs]] construct. Stanford-graduate-level academic content.

### 2. CS153 — Frontier Systems ([[2026-05-07-singhal-stanford-cs153-product-management-in-ai-era|Singhal 2026]])

[[Mike Abbott]]'s frontier-systems course (Stanford CS153) featuring **Nikhyl Singhal** (Skip founder; ex-Google/Meta/Credit Karma VP-of-Product) as guest lecturer on **product management in the AI era**. Four-company-phases framework; AI-era role inversion (*product builder* vs *movement of information*); concrete operator-class employment numbers (30-70% layoffs / top-1% PM salaries doubled). Stanford-CS-undergraduate-elective-level guest-lecture content with Sequoia-aligned faculty (Abbott is also a Sequoia partner).

## Two-course pattern

The two ingests demonstrate Stanford Online's **two distinct content modes**:

| Mode | Example | Vantage |
|---|---|---|
| **Academic-foundation lectures** | CS224W (Leskovec) | Theoretical / mathematical / canonical-domain |
| **Frontier-systems guest lectures** | CS153 (Abbott + Singhal) | Industry-operator / current-event / opinionated |

The channel as a whole is the wiki's **load-bearing source of Stanford-faculty-mediated content** — both pre-GenAI-era academic foundations and current-era industry-frontier commentary land here.

## Notable courses / programmes featured

- **CS224W — Machine Learning with Graphs** ([[Jure Leskovec]]). Foundational; the wiki holds one lecture.
- **CS153 — Frontier Systems** ([[Mike Abbott]]). Industry-guest-lecture format; the wiki holds one lecture.
- **AI graduate / professional programmes** more broadly (per the channel description; not yet ingested).

## People associated (across the wiki)

- **[[Jure Leskovec]]** — CS224W instructor; SNAP Group lead; Stanford CS professor. Currently Dangling first-mention from the CS224W ingest.
- **[[Mike Abbott]]** — CS153 professor; Sequoia partner; ex-Twitter engineering VP. Currently Dangling first-mention from the CS153 ingest.
- **[[Nikhyl Singhal]]** — CS153 guest lecturer; Skip founder. Currently Dangling first-mention.
- **[[Erik Brynjolfsson]]** — Stanford Digital Economy Lab / Stanford HAI; substantively cited in multiple wiki sources via the Stanford research apparatus (separate entity page).

## Convergence with wiki sources

| Source | Connection |
|---|---|
| [[2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings\|Leskovec 2023]] | First Stanford Online ingest; academic-foundation vantage |
| [[2026-05-07-singhal-stanford-cs153-product-management-in-ai-era\|Singhal 2026]] | Second Stanford Online ingest; frontier-systems-guest-lecture vantage; **two-source threshold met** for this entity promotion |
| [[Stanford Digital Economy Lab]] / [[Stanford HAI]] | Sister entities within Stanford's broader AI-research apparatus. Stanford Online is the *content-delivery channel*; SDEL / HAI are the *research-output sources* |

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(file.outlinks, link("Stanford Online")) OR contains(tags, "stanford")
SORT file.name ASC
```

## Open questions

- **Channel content cadence** — Stanford Online publishes a substantial volume of lectures. Future ingest targets likely include later CS224W lectures, other CS153 guest sessions, and applied-AI programme content.
- **Cross-faculty mapping** — Leskovec (CS224W ML/graphs), Abbott (CS153 frontier-systems / Sequoia), and Brynjolfsson (Stanford Digital Economy Lab) operate in distinct sub-disciplines but converge on the wiki's existing concept clusters. Worth tracking whether a multi-faculty source ever produces a single ingest.
