---
type: entity
kind: project
aliases: ["Anthropic Economic Index", "Economic Index", "AEI"]
tags: [anthropic-economic-index, ai-research, anthropic, claude, ai-adoption]
parent: "[[Anthropic]]"
since: 2025
confidence: 0.75
last_confirmed: "2026-04-28"
source_count: 2
relationships:
  - type: part-of
    target: Anthropic
    via: "Recurring research initiative published by Anthropic"
---

# Anthropic Economic Index

A research initiative by [[Anthropic]] that measures real-world AI use through privacy-preserving analysis of [[Claude]] conversations on Claude.ai (consumer) and the 1P API (enterprise). Recurring report cadence (four reports through Jan 2026).

Stated mission (per Anthropic): provide ongoing, empirical measurement of how AI is changing tasks, occupations, and the labor market.

## What it tracks

| Domain | Mapped to wiki concept |
|---|---|
| Task speedup, success, complexity | [[generative-ai]] |
| Automation vs. augmentation share | [[automation-vs-augmentation]] |
| Aggregate productivity impact | [[ai-employment-effects]] |
| Task-composition shift | [[ai-deskilling]] |
| Cross-country adoption | [[enterprise-ai-adoption]] |
| Task-horizon time scaling | [[ai-benchmarks]] |

## Reports

| Report | Sample period | Status in this wiki |
|---|---|---|
| First | January 2025 | Not separately ingested; numbers cited |
| Second | (early 2025) | Not separately ingested |
| Third | August 2025 | Not separately ingested; numbers carried over |
| **Fourth** | November 2025 | [[2026-04-28-anthropic-economic-index-q4-2025\|Ingested]] — introduces "economic primitives" framework |

## Economic primitives (introduced in fourth report)

Five measurements per conversation, derived by Claude classifying its own conversation samples:

1. **Task complexity** — human time required without AI; whether multiple tasks were handled within one conversation.
2. **Human and AI skill level** — years of education needed to understand prompts and Claude's responses.
3. **Use case** — work / education / personal.
4. **AI autonomy** — degree of user delegation, from collaboration to fully directive.
5. **Task success** — Claude's own assessment of whether the task was completed.

See [[2026-04-28-anthropic-economic-index-q4-2025|the fourth-report source page]] for definitions and applications.

## Methodology notes

- **Privacy-preserving** — random samples (typically 1M conversations on Claude.ai + 1M API transcripts).
- **Tasks mapped to O*NET** taxonomy.
- **Models change report-to-report** — fourth report uses [[Claude Sonnet 4.5]] predominantly; this affects comparability across editions.

## Cited by external research

- [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson et al. 2025 (Canaries)]] uses the Anthropic Economic Index automation/augmentation classification at the occupation level for Fact 3.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "anthropic-economic-index")
SORT file.name ASC
```

## Open questions

- Earlier reports (1st through 3rd) are referenced indirectly through the fourth-report carry-over data; first-party ingestion of any prior report would clarify the longitudinal methodology.
