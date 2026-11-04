---
type: entity
kind: project
aliases: ["Stanford Digital Economy Lab", "Digital Economy Lab"]
tags: [stanford, ai-research, digital-economy, labor-economics, working-papers]
parent: "Stanford University"
director: "[[Erik Brynjolfsson]]"
website: "https://digitaleconomy.stanford.edu"
confidence: 0.9
last_confirmed: "2026-11-04"
accessed_at: "2026-11-04"
source_count: 8
relationships:
  - type: employs
    target: Erik-Brynjolfsson
    via: "Director"
---

# Stanford Digital Economy Lab

The **Stanford Digital Economy Lab** is a research initiative at Stanford University focused on the economics of digital technology and AI — productivity, labor markets, market structure, measurement of intangible capital. Directed by [[Erik Brynjolfsson]].

**Distinct from [[Stanford HAI]] and the [[AI Index]]**, though personnel overlap: Brynjolfsson is on the AI Index Steering Committee and the Digital Economy Lab director.

## Role in the wiki

**Bumped to source_count: 2 on 12 August 2026** via [[2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity|Brynjolfsson's *McKinsey Talks Talent* appearance]], where he speaks as the lab's director and gives the current state of its **ADP payroll partnership** — the entry-level employment decline in the most AI-exposed occupations now at 16–17%, collected monthly and still growing. The underlying papers remain un-ingested; the lab's output reaches the wiki so far only through interviews.

Publisher of [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson, Chandar & Chen (2025) "Canaries in the Coal Mine?"]] — the wiki's primary empirical source on AI's recent employment effects.

Likely future-recurring as a source of empirical AI-economics research. Brynjolfsson's earlier customer-support productivity study (Brynjolfsson, Li & Rock 2023, NBER 31161 → QJE 2025) also originated from this research stream; not yet ingested as its own source page (currently summarized via [[Erik Brynjolfsson]] entity page).

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "stanford-digital-economy-lab")
SORT file.name ASC
```

## Open questions

- Lab's funding model and full personnel roster.
- Other published Digital Economy Lab papers worth ingesting standalone (vs. cited via Brynjolfsson entity page).
- Relationship to Stanford's broader economics department (HAI vs. Digital Economy Lab vs. econ dept — overlapping AI-economics communities).

## The Canaries series extended to mid-2026 (added 2026-10-08)

[[2026-10-07-richardson-reuters-econ-world-ai-at-work|Richardson on Reuters Econ World (Oct 2026)]]: ADP's chief economist describes the lab as ADP's research partner on payroll data by AI exposure and career stage. Reuters' charts, credited to the lab and ADP Research, run the [[2026-04-28-brynjolfsson-canaries-coal-mine|Canaries]] occupation series to mid-2026: employment of 22–25-year-old software developers at about 80 and of customer service reps at about 82 (Nov 2022 = 100), against about 123 for home health aides of the same age. The source count above is recounted from inbound links on this date.

## The AI Economic Indicators (added 2026-11-04)

The lab publishes four public dashboards under the name *The AI Economic Indicators*. They are run by a team under research manager Connacher Murphy, whose work *"to turn their research on the economic impacts of AI into low-latency, regularly updated measures"* is to be housed in a forthcoming **Stanford AI Economics Observatory**. Three are now in the wiki, each as a snapshot of a living page:

- [[2026-10-21-stanford-del-canaries-dashboard|Canaries Dashboard]] — with [[ADP]] Research. Monthly employment by AI exposure, age, occupation and gender, from a balanced panel of 25,000 ADP firms. September 2026: early-career employment in the most exposed occupations at 87.7 (November 2022 = 100), against 103.9 across all ages.
- [[2026-10-21-stanford-del-transformation-tracker|Transformation Tracker]] — twelve US macro indicators of transformative AI, rated against their pre-2020 history. October 2026: three strong, two mild, seven neutral; *"no decisive evidence of transformation."*
- [[2026-07-01-stanford-del-adoption-monitor|Adoption Monitor]] — published adoption surveys of US individuals and of firms in four high-income countries. 62% of US adults use generative AI; 69% of firms use some AI.
- **GDP-B: Surplus Observer** — consumer surplus from generative AI tools over time. Not yet ingested; the Transformation Tracker plans to use it for the productivity growth that standard accounts miss.

**Answers an open question above.** The lab's output now reaches the wiki first-hand, not only through interviews. The indicators also point to two later Canaries papers not yet ingested: a February 2026 update on interest rates and timing, and an August 2026 revision headlined *"No Widespread Displacement, but the AI Employment Gap for Young Workers Has Widened to 19%."*
