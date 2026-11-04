---
type: source
kind: dashboard
title: "Transformation Tracker (The AI Economic Indicators)"
author: ["Stanford Digital Economy Lab"]
publisher: "Stanford Digital Economy Lab — The AI Economic Indicators"
url: "https://digitaleconomy.stanford.edu/project/indicators/transformation-tracker/"
date_published: 2026-10-21
date_accessed: 2026-11-04
date_ingested: 2026-11-04
length: "one dashboard page (~2,300 words of prose + 13 charts, all chart data captured; snapshot of the 21 October 2026 monthly update, evidence verdicts through September 2026)"
raw: "../../raw/dashboards/2026-10-21-stanford-del-transformation-tracker.md"
tags: [stanford-digital-economy-lab, ai-economic-indicators, transformation-tracker, dashboard, transformative-ai, economic-singularity, nordhaus, explosive-growth, gdp-growth, tfp, labor-productivity, real-interest-rates, tips, capital-share, napcs, information-capital, software-and-rnd, energy, electricity, bootstrap, evidence-classification, phil-trammell, connacher-murphy, living-source]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-sensing/digital-scenario-planning
relationships:
  - type: published-by
    target: Stanford-Digital-Economy-Lab
  - type: supports
    target: 2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs
    via: "both find AI not yet visible in the aggregates: the Tracker rates output growth, TFP growth and labour-productivity growth 'Neutral' through September 2026; Hatzius puts AI investment at about 0.1pp of GDP growth"
    confidence: 0.75
  - type: supports
    target: 2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity
    via: "the Tracker's productivity indicators show 'no break from recent levels', the measured absence Frey sets out to explain"
    confidence: 0.7
  - type: supports
    target: 2026-05-21-jones-stanford-gsb-ai-and-our-economic-future
    via: "the Tracker monitors the takeoff scenario Jones models (capital share rising toward one, growth accelerating) and finds no decisive evidence of it, consistent with his weak-links case for slow arrival; Phil Trammell, on the Tracker team, works with Jones"
    confidence: 0.7
---

# Transformation Tracker — Stanford Digital Economy Lab

> In a 2021 paper, Nobel laureate William D. Nordhaus asked, "Are We Approaching an Economic Singularity?" … At the time, Nordhaus concluded, "the economic singularity is not near." Since then, the world of AI has advanced at a pace few anticipated, demanding ongoing monitoring of signals and fresh reassessment of what the indicators should be.
>
> — the Tracker's own introduction, *"Tracking the economic singularity"*

## TL;DR

A monthly dashboard from the [[Stanford Digital Economy Lab]] that asks whether the US economy is entering *transformative AI*: *"a technology-powered economic transformation at least as significant as the Industrial Revolution but unfolding in a vastly shorter time."* It tracks **twelve macroeconomic indicators** where such a transformation *"should ultimately become visible"*, and rates each from *contradictory* to *strong* evidence against its own pre-2020 history. This snapshot is the 21 October 2026 update.

1. **The verdict: *"We see no decisive evidence of transformation at present."*** Three indicators are rated strong, two mild, seven neutral, none contradictory.
2. **The growth indicators are all neutral.** Output growth (real GDP, 2.35% in Q2 2026), TFP growth (0.8% in 2025) and labour-productivity growth (2.5% in Q2 2026) show *"no break from recent levels."* These are the measures in which explosive growth would show first.
3. **The strong signals are long-running trends.** The capital share (41.7% in 2024, from 33.8% in 1997), information-processing equipment's share of the equipment stock (25.3% in 2025) and software and R&D's share of fixed assets (13.3%, from 7.8% in 1997) are all rated strong. All three trends began long before generative AI, and the method counts their persistence as evidence on purpose.
4. **The mild signals are prices and power.** The 10-year real interest rate (2.13% on 16 October 2026) is *"elevated relative to the historical distribution."* Electricity-generation growth shows *"a slight uptick."*
5. **It narrows Nordhaus's six tests to three and adds nine.** It keeps three of Nordhaus's six tests for an economic singularity and drops three as unmeasurable or ambiguous in sign. It adds output, labour productivity, interest rates, network-adjusted capital shares and energy.

## The twelve indicators (snapshot)

| Indicator | Latest value | Verdict | The page's evidence note |
| --- | --- | --- | --- |
| Output growth rate (real GDP) | 2.35% (Q2 2026) | Neutral | *"remains around its historical average"* |
| TFP growth | 0.8% (2025) | Neutral | *"no break from recent levels"* |
| Labour-productivity growth | 2.5% (Q2 2026) | Neutral | *"no break from recent levels"* |
| 10-year real interest rate (TIPS) | 2.13% (16 Oct 2026) | **Mild** | *"elevated relative to the historical distribution"* |
| Capital share | 41.7% (2024) | **Strong** | *"continues its historical upward trend without signs of abatement"* |
| Network-adjusted private capital share (NAPCS), electronics | 43.9% (2025) | Neutral | *"remains flat or is slightly decreasing"* |
| NAPCS, maximum across industries | 73.5% (2025) | Neutral | *"flat and below its maximum from earlier in the millennium"* (82.4% in 2008) |
| Information-processing equipment / nonresidential equipment stock | 25.3% (2025) | **Strong** | *"recovered to levels last achieved in the early 2000s"* |
| Software / software + R&D stock | 25.3% (2025) | Neutral | *"recovered since the pandemic"* |
| Software + R&D / private nonresidential fixed assets | 13.3% (2025) | **Strong** | *"continues its historical upward trend without signs of abatement"* |
| Primary energy consumption growth | — | Neutral | *"fluctuates around its historical average"* |
| Electricity generation growth | — | **Mild** | *"a slight uptick from its historical average"* |

**The verdicts have barely moved since tracking began in December 2024.** TFP and labour-productivity growth were mild in December 2024 and have been neutral since January 2025. Electricity generation has switched between mild and neutral four times. Energy consumption was mild for one month (November 2025). Every other indicator has held the same verdict throughout.

## How the evidence is assigned

1. Each indicator is transformed so that a rise points toward transformation. Shares are logit-transformed so that, like growth rates, they are unbounded.
2. A linear trend with AR(p) residuals is fitted to each series from the start of the sample (usually 1997) to 2019.
3. A bootstrap simulates synthetic histories from the fitted model, refits it, and draws post-2019 predictions **centred on each draw's fitted 2010 level**, with the trend held flat after 2010. This is deliberate. A series that fell through 2019 has to recover before it can count as evidence. A series that kept rising from 2010 to 2019 earns evidence for having kept the gain.
4. The one-year moving average of the data is compared with that of the simulated draws. At or below the 20th percentile is *contradictory*; at or above the 80th is *mild*; at or above the 95th is *strong*.

The method is to be described in *"a forthcoming working paper."*

**What this means for reading the verdicts.** Step 3 explains why the three strong verdicts sit on trends that predate generative AI. A capital share that has risen since the 1990s clears the 95th percentile of a distribution centred on its 2010 level. *Strong* here means *"consistent with the transformation scenario and beyond the 2010 baseline"*, not *"caused by AI"*. The neutral verdicts on growth and productivity are the more informative result.

## Why these twelve

Nordhaus (2021) proposed six signs of an approaching singularity. The Tracker keeps three: a **rising productivity-growth rate**, a **rising capital share**, and a **rising information-capital share**. It drops three:

- **Gross substitutability of capital for labour** — no timely, consistent estimates (*measurement challenge*).
- **A rising capital-to-output ratio** — under capital-driven growth each unit of capital would produce more output, so the ratio could *fall* (*ambiguity about the direction of the effect*).
- **Productivity growth missing from standard accounts** — by definition hard to source; the lab plans to add it from its GDP-B project.

It adds **output growth**, **labour-productivity growth** (mechanically rising as labour leaves production), **real risk-free interest rates** (people expecting much higher future incomes save less unless paid more, following Chow et al. 2025; and a rising marginal product of capital raises rates), **network-adjusted private capital shares** (how much of a dollar spent on a good goes, all the way down the supply chain, to capital; 100% would be a fully self-replicating production loop) and **energy** (automation-driven growth and a growing information-capital stock are likely to be energy-intensive).

## Reading the snapshot

**The lab's two flagship indicators point in different directions, at different levels.** The [[2026-10-21-stanford-del-canaries-dashboard|Canaries Dashboard]] finds a clear labour-market signal in one cohort of workers. This Tracker finds no growth or productivity signal in the economy as a whole. The two are compatible: a large shift in early-career hiring in exposed occupations need not move national productivity. Together they say AI is visible in *who gets hired* before it is visible in *how much is produced*.

**It is the corpus's first quantified version of the "not yet" argument.** [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs|Hatzius (Goldman Sachs)]] puts AI investment at about a tenth of a point of GDP growth and expects a productivity uplift spread over a decade. [[2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity|Frey]] explains why the productivity boom has not come, through the verification tax and institutions. [[2026-05-21-jones-stanford-gsb-ai-and-our-economic-future|Jones]] argues through weak links that benefits arrive slowly while risks can arrive fast. Until now each made the case in an interview or talk. The Tracker publishes the test, with thresholds, monthly. Phil Trammell, on the Tracker team, is a postdoc working with both Brynjolfsson and Jones.

**What would change the verdict.** Under the Tracker's own logic, transformation would first show as output, TFP and labour-productivity growth leaving the neutral band together, while interest rates keep rising. A rise in the capital share alone would not show it, since that has been rising for decades.

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`**: a standing scan of macro signals for whether AI is moving from a technology trend to an economic one.
- **`digital-sensing/digital-scenario-planning`**: the Tracker is a scenario test. It names one future (transformative AI, explosive growth), states in advance which signals would show it arriving, and reports monthly whether they do. Strategy built on a near-term takeoff scenario can be checked against it.

## How it connects

- [[micro-productivity-trap]] — the economy-level version of the gap between individual time saved and measured output.
- [[ai-employment-effects]] — the labour half of the lab's indicators sits in the Canaries Dashboard; this is the output half.
- [[enterprise-ai-adoption]] — adoption is rising (see the [[2026-07-01-stanford-del-adoption-monitor|Adoption Monitor]]) without yet moving these aggregates.

## Related in this wiki

- [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs|Hatzius (Goldman Sachs)]] — the same "not yet in the aggregates" finding from a sell-side chief economist, with a diffusion estimate.
- [[2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity|Frey on Trumponomics]] — why measured productivity has not moved.
- [[2026-05-21-jones-stanford-gsb-ai-and-our-economic-future|Jones at Stanford GSB]] — the growth theory behind the scenario this Tracker tests.
- [[2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity|Brynjolfsson on McKinsey Talks Talent]] — the productivity J-curve. Brynjolfsson leads this Tracker, and the J-curve predicts the flat productivity readings seen here.
- [[2026-10-21-stanford-del-canaries-dashboard|Canaries Dashboard]] and [[2026-07-01-stanford-del-adoption-monitor|Adoption Monitor]] — the other two indicators ingested with this one.

## What was actually ingested

The full page as served on 4 November 2026, and the full data of all 13 Flourish charts (one evidence heatmap and twelve indicator series), saved as CSV beside the raw file. The heatmap's verdict history runs from December 2024 to September 2026. Series end at different dates: annual BEA stock and share series in 2024 or 2025, quarterly growth series in Q2 2026, energy in June 2026, interest rates on 16 October 2026. The units of the energy and electricity series are not labelled on the page.

## Linked entities and concepts

- [[Stanford Digital Economy Lab]] — publisher. Updated in this ingest.
- [[Erik Brynjolfsson]] — research team. Updated in this ingest.
- [[micro-productivity-trap]], [[ai-employment-effects]], [[enterprise-ai-adoption]] — concepts; [[micro-productivity-trap]] updated in this ingest.

**Dangling** (not in `author:`; deferred): Connacher Murphy (research manager for the indicators; on all three ingested pages), Phil Trammell (postdoc; acknowledged in the Canaries paper), William Nordhaus (2021 paper, *"Are We Approaching an Economic Singularity?"*), Chow et al. (2025, interest rates and transformative AI).

## Scope and reliability

The inputs are official US statistics (BEA, BLS, Treasury, energy data). The judgement is in the method, which is described on the page but whose working paper is not yet out; the 20/80/95 percentile thresholds and the 2010 centring are choices the reader should know before quoting a verdict. The page is explicit that it tracks direct measures of impact *"rather than more leading, speculative indicators"*. So it will be late by design: it confirms a transformation after it has started, it does not forecast one. This is a living source; the snapshot will move monthly.
