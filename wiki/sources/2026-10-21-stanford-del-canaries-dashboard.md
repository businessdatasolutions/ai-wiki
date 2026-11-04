---
type: source
kind: dashboard
title: "Canaries Dashboard (The AI Economic Indicators)"
author: ["Stanford Digital Economy Lab", "ADP Research"]
publisher: "Stanford Digital Economy Lab — The AI Economic Indicators, in collaboration with ADP Research"
url: "https://digitaleconomy.stanford.edu/project/indicators/canaries-dashboard/"
date_published: 2026-10-21
date_accessed: 2026-11-04
date_ingested: 2026-11-04
length: "one dashboard page (~2,600 words of prose + 14 charts, all chart data captured; snapshot of the 21 October 2026 monthly update, data through September 2026)"
raw: "../../raw/dashboards/2026-10-21-stanford-del-canaries-dashboard.md"
tags: [stanford-digital-economy-lab, adp, adp-research, ai-economic-indicators, canaries, dashboard, payroll-data, early-career-workers, ai-exposure, eloundou-exposure, anthropic-economic-index, automation-ratio, augmentation-ratio, software-developers, customer-service, home-health-aides, gender, occupational-composition, balanced-sample, correlation-not-causation, living-source]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-transforming/improving-digital-maturity
relationships:
  - type: published-by
    target: Stanford-Digital-Economy-Lab
  - type: uses
    target: ADP
    via: "five-year balanced sample of firms on ADP payroll; ADP Research is co-author of the dashboard"
  - type: uses
    target: Anthropic-Economic-Index
    via: "groups occupations by the Index's automation and augmentation shares of Claude usage"
  - type: supports
    target: 2026-04-28-brynjolfsson-canaries-coal-mine
    via: "updates the paper's descriptive series monthly to September 2026: the early-career decline in the most exposed quintile persists and deepens. It also narrows the paper's reading: the dashboard calls itself correlational, and cites the February 2026 update finding significance only from 2024 onward"
    confidence: 0.85
  - type: supports
    target: 2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity
    via: "the monthly series Brynjolfsson describes as 'collecting every month since then', published; the effect keeps growing through September 2026"
  - type: supports
    target: 2026-10-07-richardson-reuters-econ-world-ai-at-work
    via: "same ADP/DEL series; Reuters' chart values (software developers ~80, customer service ~82, home health aides ~123 for ages 22–25) match the dashboard's 81.4, 80.8 and 122.0"
    confidence: 0.85
  - type: supports
    target: 2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs
    via: "at the all-ages occupation level the dashboard's own exposure gradient is 'modest' (most-exposed quintile 103.9 against 107–110 for the rest), consistent with Hatzius's small aggregate correlation; the large effect lives in the 22–25 cell, which held 7.4% of sample employment"
    confidence: 0.65
  - type: supports
    target: 2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai
    via: "two datasets (ADP payroll, CPS) find the young-worker slowdown concentrated in exposed occupations, and both build on Anthropic Economic Index usage shares"
    confidence: 0.7
---

# Canaries Dashboard — Stanford Digital Economy Lab and ADP Research

> In collaboration with ADP Research, we summarize live labor market trends for a sample workers in firms using ADP payroll services. Following *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence* (Brynjolfsson, Chandar, and Chen, 2025), we explore how recent employment changes vary with work experience and exposure to AI.
>
> — the dashboard's own introduction

## TL;DR

The [[Stanford Digital Economy Lab]] turned the [[2026-04-28-brynjolfsson-canaries-coal-mine|Canaries in the Coal Mine]] paper into a monthly dashboard built on [[ADP]] payroll data. It is one of four *AI Economic Indicators*, beside the [[2026-10-21-stanford-del-transformation-tracker|Transformation Tracker]], the [[2026-07-01-stanford-del-adoption-monitor|Adoption Monitor]] and a consumer-surplus tracker (GDP-B) not yet in the wiki. This snapshot is the 21 October 2026 update, with data through September 2026.

1. **The early-career divergence persists and deepens.** For workers aged 22–25, employment in the most AI-exposed fifth of occupations stands at **87.7** (November 2022 = 100). The fourth quintile is at 92.3. The three less-exposed quintiles are at **106.7–110.1**. The page says the declines in exposed occupations *"not only persist, but deepen"*, with *"muted evidence of similar patterns for workers up to age 34."*
2. **Across all ages the gap is modest.** All-ages employment in the most exposed quintile is at **103.9**, against 107.1–110.3 for the others. The dashboard's own words: *"modest differences between the five exposure groups."* Workers aged 22–25 were **7.4%** of sample employment in November 2022.
3. **Specific occupations carry it.** Early-career software developers are at **81.4** and customer service representatives at **80.8**. Early-career home health aides, a low-exposure occupation, are at **122.0**. Software developers aged 41–49 are at **120.2**.
4. **The automation share predicts the decline; the augmentation share does not.** Among early-career workers, occupations where a larger share of [[Anthropic Economic Index]] usage is automation show declines or weaker growth. The augmentation share shows *"no clear relationship."*
5. **The gender gap is mostly occupational mix.** Early-career women work more often in exposed occupations: 43.8% in the most exposed quintile, against 32.4% of men. Women's employment in that quintile has contracted 4.5% a year since November 2022, men's 2.5%. The page attributes most of the difference to composition rather than to *"disproportionate impact within the most-exposed occupations."*
6. **It says it measures correlation, not cause.** *"The Canaries Dashboard measures the correlation between occupational exposure measures and employment trends in our sample, rather than a causal link between the two."* It cites the authors' February 2026 update: with the broadest controls, *"declines in AI-exposed occupations become statistically significant in 2024. The earlier declines are likely driven by non-AI factors."*

## Key data (snapshot, September 2026; November 2022 = 100)

Employment index by AI-exposure quintile (Eloundou et al. 2024) and age:

| Exposure quintile | 22–25 | 26–30 | 31–34 | 35–40 | 41–49 | 50+ | All ages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 (least exposed) | 108.4 | 105.7 | 106.6 | 114.3 | 108.5 | 106.9 | 108.2 |
| 2 | 110.1 | 108.0 | 106.9 | 115.0 | 110.0 | 103.0 | 107.8 |
| 3 | 106.7 | 109.7 | 108.2 | 117.8 | 113.1 | 107.5 | 110.3 |
| 4 | **92.3** | 96.2 | 99.9 | 110.8 | 114.0 | 109.0 | 107.1 |
| 5 (most exposed) | **87.7** | 96.4 | 101.6 | 109.0 | 109.8 | 105.1 | 103.9 |
| All occupations | 97.1 | 100.4 | 102.8 | 111.4 | 111.0 | 106.0 | — |

Four occupations the page singles out:

| Occupation (exposure) | 22–25 | 26–30 | 35–40 | 41–49 |
| --- | ---: | ---: | ---: | ---: |
| Software developers (most exposed) | **81.4** | 95.8 | 112.8 | 120.2 |
| Customer service representatives (most exposed) | **80.8** | 89.2 | 112.9 | 107.5 |
| Stock clerks (second least) | 106.4 | 104.1 | 112.8 | 110.5 |
| Home health aides (least / second least) | **122.0** | 113.3 | 115.4 | 113.3 |

The trajectories differ. Early-career software developers fell to about 79 by April 2025 and have stayed between 79 and 83 since. Early-career customer service representatives are still falling: 89.0 in April 2025, 84.0 in April 2026, 80.8 in September 2026. The most-exposed quintile for ages 22–25 has fallen steadily: 98.1 (April 2023), 95.4 (April 2024), 91.2 (April 2025), 88.0 (April 2026), 87.7 (September 2026).

## Method, and what the dashboard says it is not

- **Sample.** A five-year *balanced* panel of firms on ADP payroll, rolled forward each month, limited to workers matched to an occupation code. At launch, with the window ending in April 2026, that was **25,000 firms** employing **4.6 million** matched workers in November 2022, across **730+ occupations**. ADP pays more than 26 million US workers in all.
- **What balancing removes.** Firm entry and exit, reallocation between firms, and firms switching payroll provider all fall outside the sample. This is the margin on which AI-native start-ups would show up, so the dashboard cannot see it.
- **Not representative.** *"Our sample represents neither the entire U.S. labor market nor the universe of firms using ADP payroll services."* It departs from ADP's own National Employment Report methodology. The page calls it a complement to nationally representative data, faster and more granular, not a substitute.
- **Exposure.** Occupations are matched through the BLS 2018 SOC crosswalk to Eloundou et al. (2024) and to the Anthropic Economic Index. Quintiles weight occupations equally, not by employment. So the most exposed fifth of occupations holds **38.3%** of sample employment and the least exposed fifth **6.4%**; the middle three hold 13.7%, 13.9% and 27.7%.
- **Correlation, not cause.** The page sets its descriptive aggregates beside the paper's event-study regressions and says the dashboard reports the former. *"Future versions of this work will use an expanded and reweighted sample."*
- **Newer papers, linked but not in the wiki.** The page links two later papers by the same authors. One is the **February 2026 update**, *"Canaries, Interest Rates, and Timing: More on the Recent Drivers of Employment Changes for Young Workers"*. The other is an **August 2026 revised version** of the paper, headlined *"No Widespread Displacement, but the AI Employment Gap for Young Workers Has Widened to 19%."* Only the dashboard's one-sentence summary of the February update has been read.

## Reading the snapshot

**It tests the open thread's leading hypothesis.** The [[ai-employment-effects-measurement-dispute]] thread asks whether the large payroll effect and the small aggregate effect reported by [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs|Hatzius (Goldman Sachs)]] are measurements at different levels rather than a disagreement. The dashboard publishes both levels from one sample. At ages 22–25 the most-exposed quintile trails the least exposed by about 21 index points (87.7 against 108.4). Across all ages the gap is about 4 points (103.9 against 108.2), in a cell that held 38% of employment. A large effect in a cohort holding 7.4% of employment and a small effect in the aggregate are both visible here, in one dataset, on one method. This is the decomposition the thread called *"the most plausible reconciliation, not an established one."* It does not yet settle the thread: the all-ages series still nets nothing against job creation elsewhere, and it still does not separate remote work from AI.

**The augmentation result has moved since the paper.** The paper reported that in the most augmentation-heavy quintile, young workers' employment grew fastest. In this snapshot that quintile stands at **90.2** for ages 22–25, close to the most automation-heavy quintile (**89.1**). The other augmentation quintiles run from 91.7 to 102.0, in no order. The dashboard summarises this as *"no clear relationship"* and does not comment on the change. Two cautions. The most-augmentation quintile is a small cell (0.59% of sample employment, about 8% of 22–25 employment, against 2.54% for the most-automation quintile). And the sample has rolled forward since the paper. Still, the automation half of the paper's Fact 3 holds and the augmentation half no longer looks like the mirror image. See [[automation-vs-augmentation]].

**Where the losses are, by age.** Mid-career workers in the most exposed quintile are at 109.0 (35–40) and 109.8 (41–49), close to their age groups' averages (111.4 and 111.0). Past about age 34 the sample shows little or no exposure penalty. This is evidence about age, not about role. It bears on, but does not test, [[2026-10-30-lakhani-silicon-valley-girl-people-most-at-risk-from-ai|Lakhani's]] view that middle management is more exposed than junior work, because the dashboard does not separate managers.

**Pull quote.** The page carries one quote from [[Erik Brynjolfsson]] with no date or source: *"We are now transitioning out of this investment phase into a harvest phase where those earlier efforts begin to manifest as measurable output."* It is his productivity J-curve. The lab's own [[2026-10-21-stanford-del-transformation-tracker|Transformation Tracker]] does not yet show that harvest in its productivity indicators.

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`**: a monthly, low-latency instrument for sensing how AI is changing the labour market, built to give an early signal before national statistics do.
- **`digital-transforming/improving-digital-maturity`**: the data are about which workers firms hire and keep. Falling early-career employment in exposed occupations is evidence about the workforce side of maturity: entry-level recruiting and the pipeline that produces experienced staff.

## How it connects

- [[ai-employment-effects]] — the corpus's main labour-market evidence, now as a time series to September 2026.
- [[automation-vs-augmentation]] — the automation share still predicts decline; the augmentation share no longer predicts growth.
- [[ai-employment-effects-measurement-dispute]] — the aggregate-versus-cohort comparison the thread asked for, from one sample.
- [[durable-skills]] — the occupations growing for young workers (home health aides) are relational and physical.

## Related in this wiki

- [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson, Chandar & Chen (2025)]] — the paper this dashboard updates and extends with the same balanced-sample method.
- [[2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity|Brynjolfsson on McKinsey Talks Talent]] — his "16 or 17% now" figure comes from this monthly series.
- [[2026-10-07-richardson-reuters-econ-world-ai-at-work|Richardson (ADP) on Reuters Econ World]] — Reuters' charts of the same series, from ADP's side of the partnership. The values match.
- [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs|Hatzius (Goldman Sachs)]] — the aggregate-level sceptic. The dashboard's all-ages chart agrees with him at his level of aggregation.
- [[2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai|Massenkoff & McCrory (Anthropic)]] — the same young-worker signal on CPS data, also built on Anthropic Economic Index usage.
- [[2026-10-21-stanford-del-transformation-tracker|Transformation Tracker]] and [[2026-07-01-stanford-del-adoption-monitor|Adoption Monitor]] — the other two indicators ingested with this one.

## What was actually ingested

The full page as served on 4 November 2026, and the full data of all 14 Flourish charts, saved as CSV beside the raw file. The prose has three dates: the headline charts were updated 21 October 2026, the gender section 22 July 2026, and the sample description refers to the launch window ending April 2026. The *"See annualized results"* toggle re-presents the same index series and adds no data. Three embedded videos are related talks and were not fetched: the lab's own *Canaries* talk, Bloomberg Tech's *"New Tracker Traces AI's Real-Time Impact on Work"*, and an Infosys Knowledge Institute interview with Ruyu Chen. Values in the tables above are read from the chart data, not from the page prose; the prose's percentages come from the July 2026 release and can differ slightly.

## Linked entities and concepts

- [[Stanford Digital Economy Lab]] — publisher. Updated in this ingest.
- [[ADP]] — data provider; ADP Research is co-author. New entity page in this ingest.
- [[Erik Brynjolfsson]] — lab director and lead of the research team. Updated in this ingest.
- [[Anthropic Economic Index]] — source of the automation and augmentation shares. Updated in this ingest.
- [[ai-employment-effects]], [[automation-vs-augmentation]], [[durable-skills]] — concepts; the first two updated in this ingest.
- [[ai-employment-effects-measurement-dispute]] — thread, updated in this ingest.

**Dangling** (not in `author:`; deferred): Bharat Chandar and Ruyu Chen (co-authors of the paper, named as researchers), Sarah Bana, J. Frank Li and Andrew Wang (research team), Tyna Eloundou (exposure measure).

## Scope and reliability

The data are payroll records, not surveys, for a large sample that is not representative of US employment. The method is documented on the page and follows a public working paper; the classification of an occupation as exposed is inherited from two external measures. The page is careful about its claims: it states the sample's limits, calls its results correlational, and points to the authors' own later finding that the earlier part of the decline was not driven by AI. This is a living source. The numbers above are a snapshot; the page will have moved by the next monthly update.
