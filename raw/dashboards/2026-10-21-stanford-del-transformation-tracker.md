---
title: "Transformation Tracker"
series: "The AI Economic Indicators"
publisher: "Stanford Digital Economy Lab"
authors: ["Stanford Digital Economy Lab"]
url: "https://digitaleconomy.stanford.edu/project/indicators/transformation-tracker/"
citation_url: "https://transformation.stanford.edu/"
last_updated: "2026-10-21"
update_cadence: "monthly"
data_through: "2026-09 (evidence heatmap); series end between 2024 (capital share) and 2026-10-16 (real interest rates)"
accessed: "2026-11-04"
acquired_via: "curl of the page's static HTML (all prose is server-rendered); chart data read from each Flourish embed (flo.uri.sh/visualisation/<id>/embed, variable _Flourish_data)"
notes: |
  Snapshot of a living dashboard that updates monthly. The page's own citation URL (citation_url) redirects to url.
  The methodology is described as forthcoming in a working paper ('We will further describe this method in a forthcoming working paper').
  Converted from HTML by a BeautifulSoup walk of <main>: headings, paragraphs and list items in page order; navigation, buttons and footer dropped.
charts_count: 13
charts:
  - id: "29265222"
    title: "Takeoff: Heatmap"
    csv: "2026-10-21-stanford-del-transformation-tracker/29265222-takeoff-heatmap.csv"
    rows: 264
  - id: "29251438"
    title: "Takeoff: Output Growth Rate"
    csv: "2026-10-21-stanford-del-transformation-tracker/29251438-takeoff-output-growth-rate.csv"
    rows: 115
  - id: "29251606"
    title: "Takeoff: TFP Growth Rate"
    csv: "2026-10-21-stanford-del-transformation-tracker/29251606-takeoff-tfp-growth-rate.csv"
    rows: 29
  - id: "29251770"
    title: "Takeoff: Labor Productivity Growth Rate"
    csv: "2026-10-21-stanford-del-transformation-tracker/29251770-takeoff-labor-productivity-growth-rate.csv"
    rows: 115
  - id: "29252076"
    title: "Takeoff: Real Risk Free Interest Rates"
    csv: "2026-10-21-stanford-del-transformation-tracker/29252076-takeoff-real-risk-free-interest-rates.csv"
    rows: 334
  - id: "29252202"
    title: "Takeoff: Capital Share"
    csv: "2026-10-21-stanford-del-transformation-tracker/29252202-takeoff-capital-share.csv"
    rows: 28
  - id: "29252245"
    title: "Takeoff: NAPCS, Electronics Manufacturing"
    csv: "2026-10-21-stanford-del-transformation-tracker/29252245-takeoff-napcs-electronics-manufacturing.csv"
    rows: 29
  - id: "29252304"
    title: "Takeoff: NAPCS, Max across Industries"
    csv: "2026-10-21-stanford-del-transformation-tracker/29252304-takeoff-napcs-max-across-industries.csv"
    rows: 29
  - id: "29252389"
    title: "Takeoff: IP in Capital Stock"
    csv: "2026-10-21-stanford-del-transformation-tracker/29252389-takeoff-ip-in-capital-stock.csv"
    rows: 29
  - id: "29265038"
    title: "Takeoff: Software in IP"
    csv: "2026-10-21-stanford-del-transformation-tracker/29265038-takeoff-software-in-ip.csv"
    rows: 29
  - id: "29265101"
    title: "Takeoff: Software and R&D in Capital Stock"
    csv: "2026-10-21-stanford-del-transformation-tracker/29265101-takeoff-software-and-randd-in-capital-stock.csv"
    rows: 29
  - id: "29252609"
    title: "Takeoff: Energy Consumption"
    csv: "2026-10-21-stanford-del-transformation-tracker/29252609-takeoff-energy-consumption.csv"
    rows: 343
  - id: "29252698"
    title: "Takeoff: Electricity Capacity and Generation"
    csv: "2026-10-21-stanford-del-transformation-tracker/29252698-takeoff-electricity-capacity-and-generation.csv"
    rows: 343
---

- ← Research

- ← All Work

- ← The AI Economic Indicators

# Transformation Tracker

#### Tracking the economic singularity

In a 2021 paper, Nobel laureate William D. Nordhaus asked, “ Are We Approaching an Economic Singularity? ”

Nordhaus defined economic singularity as the case where “rapid growth in information technology and artificial intelligence will cross some boundary, after which economic growth will rise rapidly as an ever-increasing pace of improvements cascade through the economy.”

At the time, Nordhaus concluded, “the economic singularity is not near.”

Since then, the world of AI has advanced at a pace few anticipated, demanding ongoing monitoring of signals and fresh reassessment of what the indicators should be.

The Transformation Tracker focuses on direct measures of economic impact rather than more leading, speculative indicators. If AI is driving a transformative shift in growth and productivity, these are the measures where the effects should ultimately become visible.

Evidence for Transformation

We summarize our 12 indicators of transformation, assessing the extent to which each points towards explosive economic growth. By tracking these series over time, we can contextualize recent changes against longer-running economic trends. We see no decisive evidence of transformation at present.

> **[Chart: Takeoff: Heatmap]** Flourish 29265222; data snapshot: `2026-10-21-stanford-del-transformation-tracker/29265222-takeoff-heatmap.csv` (264 rows)

## Last updated October 21, 2026. Results are updated on a monthly basis.

We track progress toward “transformative AI”: a technology-powered economic transformation at least as significant as the Industrial Revolution but unfolding in a vastly shorter time. There are several ways this could happen, but a key example is a regime in which economic output is no longer bottlenecked by a need for labor, and growth is driven instead by the rapid proliferation and self-improvement of intelligent machines. It seems probable that throughout the transition, capital–especially IT capital, including software–would comprise an increasing cost share of the inputs to both research and production, and interest rates and growth rates would greatly rise.

Nordhaus (2021) proposed six indicators of whether we are approaching an “economic singularity”: a regime of rapid, automation-driven growth.

- Gross substitutability of capital for labor

- A rising rate of productivity growth

- A rising capital share

- A rising, and even accelerating, capital-to-output ratio

- A rising information capital share

- A rising amount of productivity growth not captured in standard economic accounts

We include three of these indicators:

- A rising rate of productivity growth

- A rising capital share

- A rising information capital share

We exclude the remaining three indicators:

- Gross substitutability of capital for labor: Timely and consistent estimates of the substitutability of capital and labor are difficult to maintain and interpret. (Measurement challenge)

- A rising (and even accelerating) capital-to-output ratio: We may see certain forms of capital proliferate before automation grows extensive enough to greatly increase output. Ultimately, however, each unit of capital would likely be able to produce ever more output under a regime in which growth is driven by capital accumulation. This expansion in output per unit of capital would lead to a falling capital-to-output ratio. (Ambiguity about the direction of the effect)

- A rising amount of productivity growth not captured in standard economic accounts: Given that these gains are definitionally not included in standard accounts, it is difficult to source regularly maintained estimates. However, we plan to use the Lab’s GDP-B project to add this indicator to future versions of this project. (Measurement challenge)

We supplement the original indicators proposed by Nordhaus with additional series. More detailed explainers for each metric accompany the charts below, but we provide some context here.

- Output growth: We aim to track whether we are approaching a world of rapid, automation-driven growth.

- Labor productivity growth: With output growing and labor inputs constant or falling, labor productivity rises mechanically.

- Real risk-free interest rates: In anticipation of rising incomes from explosive economic growth, individuals are disinclined to save unless they receive outsize interest. Chow et al. (2025) formalize this argument. Additionally, a rising marginal product of capital should raise interest rates mechanically.

- Network-adjusted private capital shares (NAPCS): A good’s network-adjusted private capital share is the answer to the question: of a given dollar spent on that good, what share of it is ultimately paid out in exchange for value added by capital (as opposed to labor), all the way down the supply chain? We look at the NAPCS in specific industries to assess progress toward fully self-replicating production loops.

- Energy: Rapid automation-driven growth, and the concomitant expansion of the stock of capital (especially information capital), are likely to be energy intensive, even if the energy efficiency of AI systems and other information technologies improve rapidly.

We assign each indicator to “contradictory evidence”, “neutral evidence”, “mild evidence”, or “strong evidence” in stages:

- We first transform each indicator such that increases in the indicator point toward transformation. We take the logits of the “share” indicators, so that, like the “growth rate” indicators, their ranges are unbounded above and below. Each indicator begins in the neutral evidence category; we then assign it to contradictory, mild, or strong evidence according to the following conditions.

- We fit a linear time trend with AR(p) residuals to each indicator on data from the beginning of the sample period (typically 1997) to 2019. We tune the AR lag p on this sample.

- We next bootstrap a distribution for each indicator. In each bootstrap draw, we first simulate a synthetic history from the fitted trend with AR(p) residual after burn-in. We then refit the same model (linear trend with AR(p) residuals) to this synthetic history. This stage allows us to account for estimation uncertainty in fitting the linear trend with AR(p) residuals.

- Conditional on this refitted model, we simulate post-2019 predictive values, centered at each draw’s refitted 2010 value. In other words, we hold the trend held flat after a 2010 kink date. Accordingly, this post-2019 predictive distribution is centered around each draw’s refitted 2010 level, according to the linear trend, rather than around the trend extrapolated forward to the target date.

- We use the 2010 fitted value to center these draws, rather than extrapolating forward a trend, (a) to require indicators with a downward [upward] trend through 2019 to revert to a higher [lower] level before being assigned to the mild or strong [contradictory] evidence categories and (b) to consider the persistence of trends—or the maintenance of level gains [losses] from 2010 through 2019—as evidence.

- We compare a one-year moving average of the realizations of the data to a one-year moving average of the distribution of simulated draws from the AR process.

- We assign realizations at or below the 20th percentile of this distribution to the contradictory evidence category. Realizations at or above the 80th percentile but below the 95th percentile are assigned to the mild evidence category, while any realization at the 95th percentile or higher is classified as strong evidence.

#### Summary of recent results

- Ten-year real interest rates remain elevated and in the mild evidence category.

- Electricity generation returned to the mild evidence category, bouncing back from a brief reversion to neutral evidence category.

- In aggregate, we still see no strong indication of transformation.

Under explosive economic growth driven by AI, output is directly proportional to the capital stock, no longer constrained by labor. With a

level of technological capability, the growth rate would be constant, and growth would be exponential. However, as soon as we allow for technological

, the growth rate increases over time, yielding faster-than-exponential growth. See the methodology section below for the tests we apply to each indicator. We will further describe this method in a forthcoming working paper.

Evidence notes: Output growth remains around its historical average.

> **[Chart: Takeoff: Output Growth Rate]** Flourish 29251438; data snapshot: `2026-10-21-stanford-del-transformation-tracker/29251438-takeoff-output-growth-rate.csv` (115 rows)

Total Factor Productivity (TFP) Growth

Total factor productivity (TFP) captures output growth not directly attributable to labor input or the capital stock. TFP is commonly used as a proxy for economy-wide efficiency. Accordingly, increases in TFP growth underlie a transformation scenario. See the methodology section below for the tests we apply to each indicator. We will further describe this method in a forthcoming working paper.

Evidence notes: Productivity growth shows no break from recent levels.

> **[Chart: Takeoff: TFP Growth Rate]** Flourish 29251606; data snapshot: `2026-10-21-stanford-del-transformation-tracker/29251606-takeoff-tfp-growth-rate.csv` (29 rows)

While explosive economic growth driven by AI and technological progress should increase all measures of productivity, labor productivity is especially inclined to increase. The move from labor to capital in production will mechanically increase output for each hour of labor. See the methodology section below for the tests we apply to each indicator. We will further describe this method in a forthcoming working paper.

Evidence notes: Labor productivity growth shows no break from recent levels.

> **[Chart: Takeoff: Labor Productivity Growth Rate]** Flourish 29251770; data snapshot: `2026-10-21-stanford-del-transformation-tracker/29251770-takeoff-labor-productivity-growth-rate.csv` (115 rows)

We limit this test to the 10-year real interest rate. With sustained technological progress and a continued trend towards explosive economic growth, the marginal product of capital—and therefore interest rates—will rise. Additionally, changing saving patterns could cause an increase in interest rates. If explosive economic growth is expected to increase incomes, then people

explosive economic growth will demand a higher return for forgoing consumption in the near-term. We use Treasury inflation-protected securities (TIPS) yields to proxy for real risk-free interest rates. See the methodology section below for the tests we apply to each indicator. We will further describe this method in a forthcoming working paper.

Evidence notes: Interest rates are elevated relative to the historical distribution.

> **[Chart: Takeoff: Real Risk Free Interest Rates]** Flourish 29252076; data snapshot: `2026-10-21-stanford-del-transformation-tracker/29252076-takeoff-real-risk-free-interest-rates.csv` (334 rows)

Under a move to explosive economic growth driven by AI, the shift away from human labor to capital in production will naturally drive capital’s share of factor income to 100%. See the methodology section below for the tests we apply to each indicator. We will further describe this method in a forthcoming working paper. We logit-transform this share so that it lives on the proper interval.

Evidence notes: The capital share continues its historical upward trend without signs of abatement.

> **[Chart: Takeoff: Capital Share]** Flourish 29252202; data snapshot: `2026-10-21-stanford-del-transformation-tracker/29252202-takeoff-capital-share.csv` (28 rows)

Network-Adjusted Private Capital Share for Electronics

Of a given dollar spent on a final good, how much is paid out in exchange for value added by capital, all the way down the supply chain? The network-adjusted private capital share (NAPCS) captures exactly this concept: what is capital’s ultimate contribution to value added? Similar to the capital share, the NAPCS will rise to unity in the move to explosive economic growth driven by AI. Further, a NAPCS of 100% reflects a full self-replication loop. We track the maximum NAPCS across sectors, as well as the NAPCS for electronics manufacturing. See the methodology section below for the tests we apply to each indicator. We will further describe this method in a forthcoming working paper. We logit-transform this share so that it lives on the proper interval.

Evidence notes: The NAPCS for the electronics sector remains flat or is slightly decreasing.

> **[Chart: Takeoff: NAPCS, Electronics Manufacturing]** Flourish 29252245; data snapshot: `2026-10-21-stanford-del-transformation-tracker/29252245-takeoff-napcs-electronics-manufacturing.csv` (29 rows)

Maximum Network-Adjusted Private Capital Share

Of a given dollar spent on a final good, how much is paid out in exchange for value added by capital, all the way down the supply chain? The network-adjusted private capital share (NAPCS) captures exactly this concept: what is capital’s ultimate contribution to value added? Similar to the capital share, the NAPCS will rise to unity in the move to explosive economic growth driven by AI. Further, a NAPCS of 100% reflects a full self-replication loop. We track the maximum NAPCS across sectors, as well as the NAPCS for electronics manufacturing. See the methodology section below for the tests we apply to each indicator. We will further describe this method in a forthcoming working paper. We logit-transform this share so that it lives on the proper interval.

Evidence notes: The maximum NAPCS remains flat and below its maximum from earlier in the millennium.

> **[Chart: Takeoff: NAPCS, Max across Industries]** Flourish 29252304; data snapshot: `2026-10-21-stanford-del-transformation-tracker/29252304-takeoff-napcs-max-across-industries.csv` (29 rows)

Information Processing Equipment Share of Nonresidential Equipment

Explosive economic growth driven by AI will necessitate a shift toward information capital, i.e., semiconductors and other computing equipment. We first measure the

in the capital stock: information processing equipment as a share of BEA’s current-cost net stock of private nonresidential equipment. See the methodology section below for the tests we apply to each indicator. We will further describe this method in a forthcoming working paper. We logit-transform this share so that it lives on the proper interval.

Evidence notes: IP equipment’s share in the capital stock has recently recovered to levels last achieved in the early 2000s.

> **[Chart: Takeoff: IP in Capital Stock]** Flourish 29252389; data snapshot: `2026-10-21-stanford-del-transformation-tracker/29252389-takeoff-ip-in-capital-stock.csv` (29 rows)

Software as a Share of Software and R&D

Explosive economic growth driven by AI will increase the importance of software in intellectual property. We measure software as a share of BEA’s current-cost net stock of software and R&D. See the methodology section below for the tests we apply to each indicator. We will further describe this method in a forthcoming working paper. We logit-transform this share so that it lives on the proper interval.

Evidence notes: The concentration of software and R&D-related capital in software has recovered since the pandemic.

> **[Chart: Takeoff: Software in IP]** Flourish 29265038; data snapshot: `2026-10-21-stanford-del-transformation-tracker/29265038-takeoff-software-in-ip.csv` (29 rows)

Software and R&D as a Share of Private Nonresidential Fixed Assets

Explosive economic growth driven by AI could increase the importance of intellectual property in the capital stock. We measure software and R&D as a share of BEA’s current-cost net stock of private nonresidential fixed assets. See the methodology section below for the tests we apply to each indicator. We will further describe this method in a forthcoming working paper. We logit-transform this share so that it lives on the proper interval.

Evidence notes: The software and R&D share continues its historical upward trend without signs of abatement.

> **[Chart: Takeoff: Software and R&D in Capital Stock]** Flourish 29265101; data snapshot: `2026-10-21-stanford-del-transformation-tracker/29265101-takeoff-software-and-randd-in-capital-stock.csv` (29 rows)

Primary Energy Consumption

for this test. Explosive economic growth driven by AI would plausibly generate an increase in energy consumption, especially electricity consumption. See the methodology section below for the tests we apply to each indicator. We will further describe this method in a forthcoming working paper.

Evidence notes: Energy consumption growth fluctuates around its historical average.

> **[Chart: Takeoff: Energy Consumption]** Flourish 29252609; data snapshot: `2026-10-21-stanford-del-transformation-tracker/29252609-takeoff-energy-consumption.csv` (343 rows)

We use electricity generation

for this test. We do not test electricity capacity. Explosive economic growth driven by AI would plausibly generate an increase in energy consumption, especially electricity consumption. See the methodology section below for the tests we apply to each indicator. We will further describe this method in a forthcoming working paper.

Evidence notes: Electricity generation growth shows a slight uptick from its historical average.

> **[Chart: Takeoff: Electricity Capacity and Generation]** Flourish 29252698; data snapshot: `2026-10-21-stanford-del-transformation-tracker/29252698-takeoff-electricity-capacity-and-generation.csv` (343 rows)

## Research team

Erik Brynjolfsson is one of the world’s leading experts on the economics of technology and artificial intelligence. He is the Jerry Yang and Akiko Yamazaki Professor and Senior Fellow at the Stanford Institute for Human-Centered AI (HAI), and Director of the Stanford Digital Economy Lab. He also is the Ralph Landau Senior Fellow at the Stanford Institute for Economic Policy Research (SIEPR), Professor by Courtesy at the Stanford Graduate School of Business and Stanford Department of Economics, and a Research Associate at the National Bureau of Economic Research (NBER).

One of the most-cited authors on the economics of information, Brynjolfsson was among the first researchers to measure productivity contributions of IT and the complementary role of organizational capital and other intangibles.

Connacher Murphy is a research manager at DEL, where he works with lab scholars to turn their research on the economic impacts of AI into low-latency, regularly updated measures of the economic impacts of AI. He also pursues new research partnerships for this work. These efforts are housed under the forthcoming Stanford AI Economics Observatory.

Connacher is interested in the economic and social impacts of AI, both for their relevance to policy and as strong proxies for capabilities.

Phil is an economics postdoc working with Erik Brynjolfsson and Chad Jones (of Stanford GSB) on questions related to economic growth and AI. He’s mainly working on theoretical questions regarding the consequences of building machines intelligent and dextrous enough to automate essentially all work. With Erik and others at the lab, Phil is thinking about the macroeconomic trends that we should expect to observe at the beginning of such a transition, and about the extent to which we are starting to observe these trends today.

#### Cite the Transformation Tracker

Stanford Digital Economy Lab. "AI Economic Indicators: Transformation Tracker." Accessed [access date]. https://transformation.stanford.edu/

@misc{stanford-indicators-transformation, author = {{Stanford Digital Economy Lab}}, title = {AI Economic Indicators: Transformation Tracker}, year = {[access year]}, urldate = {[access-date]}, url = {https://transformation.stanford.edu/} }

## Explore the rest of the Indicators

The AI Economic Indicators

## Canaries Dashboard

A collaboration between ADP Research and the Stanford Digital Economy Lab, we track employment across occupations and worker groups with different levels of AI exposure.

## Adoption Monitor

Adoption trends for generative AI tools among individuals and firms across available surveys and datasets.

## GDP-B: Surplus Observer

We track consumer surplus from generative AI tools over time, allowing us to understand the dynamics and components of the consumer welfare contributions of AI.

## Chart data (snapshot)

Every chart on the page is a Flourish embed. Its full data series, as published on the access date, is saved as CSV in the folder named in each row. Index charts are rebased to November 2022 = 100 unless stated.

| Flourish id | Chart | Rows | CSV | Footer note |
| --- | --- | ---: | --- | --- |
| 29265222 | Takeoff: Heatmap | 264 | `2026-10-21-stanford-del-transformation-tracker/29265222-takeoff-heatmap.csv` |  |
| 29251438 | Takeoff: Output Growth Rate | 115 | `2026-10-21-stanford-del-transformation-tracker/29251438-takeoff-output-growth-rate.csv` |  |
| 29251606 | Takeoff: TFP Growth Rate | 29 | `2026-10-21-stanford-del-transformation-tracker/29251606-takeoff-tfp-growth-rate.csv` |  |
| 29251770 | Takeoff: Labor Productivity Growth Rate | 115 | `2026-10-21-stanford-del-transformation-tracker/29251770-takeoff-labor-productivity-growth-rate.csv` |  |
| 29252076 | Takeoff: Real Risk Free Interest Rates | 334 | `2026-10-21-stanford-del-transformation-tracker/29252076-takeoff-real-risk-free-interest-rates.csv` |  |
| 29252202 | Takeoff: Capital Share | 28 | `2026-10-21-stanford-del-transformation-tracker/29252202-takeoff-capital-share.csv` |  |
| 29252245 | Takeoff: NAPCS, Electronics Manufacturing | 29 | `2026-10-21-stanford-del-transformation-tracker/29252245-takeoff-napcs-electronics-manufacturing.csv` |  |
| 29252304 | Takeoff: NAPCS, Max across Industries | 29 | `2026-10-21-stanford-del-transformation-tracker/29252304-takeoff-napcs-max-across-industries.csv` |  |
| 29252389 | Takeoff: IP in Capital Stock | 29 | `2026-10-21-stanford-del-transformation-tracker/29252389-takeoff-ip-in-capital-stock.csv` |  |
| 29265038 | Takeoff: Software in IP | 29 | `2026-10-21-stanford-del-transformation-tracker/29265038-takeoff-software-in-ip.csv` |  |
| 29265101 | Takeoff: Software and R&D in Capital Stock | 29 | `2026-10-21-stanford-del-transformation-tracker/29265101-takeoff-software-and-randd-in-capital-stock.csv` |  |
| 29252609 | Takeoff: Energy Consumption | 343 | `2026-10-21-stanford-del-transformation-tracker/29252609-takeoff-energy-consumption.csv` |  |
| 29252698 | Takeoff: Electricity Capacity and Generation | 343 | `2026-10-21-stanford-del-transformation-tracker/29252698-takeoff-electricity-capacity-and-generation.csv` |  |
