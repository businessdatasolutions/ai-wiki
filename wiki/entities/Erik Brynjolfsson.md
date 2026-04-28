---
type: entity
kind: person
aliases: ["Erik Brynjolfsson"]
tags: [stanford, nber, ai-research, digital-economy, labor-economics, productivity]
affiliation: "[[Stanford Digital Economy Lab]] / [[Stanford HAI]] / [[NBER]]"
role: "Director, Stanford Digital Economy Lab; AI Index Steering Committee member"
contact: "erikb@stanford.edu"
---

# Erik Brynjolfsson

**Erik Brynjolfsson** is a leading academic on the economics of digital technology and AI. Stanford University and NBER affiliated. **Director of the [[Stanford Digital Economy Lab]]**. Member of the [[AI Index]] Steering Committee at [[Stanford HAI]] (so cross-affiliated between Stanford's two major AI-research initiatives).

## Role in the wiki

Brynjolfsson recurs across multiple sources and is the author of two of the most-cited empirical findings in the wiki:

### 1. The "Equalizing Effect" customer-support study (2023)

**Brynjolfsson, Li & Rock (2023)**, NBER 31161, published in *Quarterly Journal of Economics* 2025. Field experiment with 5,179 customer support agents finding:
- **+14.2% issues resolved per hour** with generative AI assistant.
- Productivity gains **emerged quickly** after AI introduction.
- AI-exposed workers maintained **higher efficiency during AI outages** — the workers learned generalizable skills.
- **Equalizing effect**: low-skill workers gained **34%**, high-skill workers gained ~0%.

Cited via [[2026-04-28-ai-index-report-2025|AI Index 2025]] §4.4 as the canonical productivity-gains study underwriting much of the AI-Index productivity narrative.

### 2. The "Canaries in the Coal Mine" employment study (2025)

[[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson, Chandar & Chen (2025)]], Stanford Digital Economy Lab working paper, Aug 26, 2025. Six facts using ADP payroll data showing:
- **Early-career workers (22–25) in AI-exposed occupations: ~13% relative decline** since late 2022.
- Older workers and less-exposed occupations stable or growing.
- Declines concentrated in **automation** uses, not **augmentation** uses.
- Adjustments visible in **employment more than wages** (wage stickiness).

This is the wiki's headline empirical evidence for AI labor displacement.

### Cross-paper synthesis

The two papers together describe the **task-level vs. occupation-level paradox** of AI's labor impact:
- *At the task level (within a job)*: AI raises productivity of low-skill / early-career workers more — equalizing.
- *At the occupation level (across firms)*: AI is reducing entry-level employment in occupations where it can substitute for labor — disequalizing.

Both can be true simultaneously. The mechanism: when AI raises individual productivity, total employment in that role depends on how elastic demand is for the role's output. See [[ai-employment-effects]] and [[automation-vs-augmentation]].

## Notable affiliations

- **Stanford University** — faculty
- **[[Stanford Digital Economy Lab]]** — director
- **[[Stanford HAI]]** — affiliated; member of [[AI Index]] Steering Committee
- **NBER** (National Bureau of Economic Research) — research associate

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "brynjolfsson")
SORT file.name ASC
```

## Open questions

- Brynjolfsson's books (*The Second Machine Age* with Andrew McAfee; *Race Against the Machine*; *Machine, Platform, Crowd*) — to be filled in as more sources reference them.
- The **Productivity J-Curve** (Brynjolfsson, Rock, Syverson) framework — relevant to the time-lag between AI investment and measurable productivity. Mentioned only obliquely in the wiki so far.
- His earlier work on **IT productivity paradox** — which his AI-productivity work builds on intellectually.
