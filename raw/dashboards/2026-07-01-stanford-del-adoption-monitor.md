---
title: "Adoption Monitor"
series: "The AI Economic Indicators"
publisher: "Stanford Digital Economy Lab"
authors: ["Stanford Digital Economy Lab"]
url: "https://digitaleconomy.stanford.edu/project/indicators/adoptionmonitor/"
citation_url: "https://digitaleconomy.stanford.edu/project/indicators/adoption/"
last_updated: "2026-07-01"
update_cadence: "as new survey data are released"
data_through: "2026-06 (individual surveys); firm survey fielded 2025-11 to 2026-01"
accessed: "2026-11-04"
acquired_via: "curl of the page's static HTML (all prose is server-rendered); chart data read from each Flourish embed (flo.uri.sh/visualisation/<id>/embed, variable _Flourish_data)"
notes: |
  Snapshot of a living dashboard. The page's own citation URL (citation_url) redirects to url.
  Section-level dates on the page: 'Last updated July 1, 2026'; firm summary 'Last update of this summary: June 10, 2026'.
  Converted from HTML by a BeautifulSoup walk of <main>: headings, paragraphs and list items in page order; navigation, buttons and footer dropped.
charts_count: 4
charts:
  - id: "29224364"
    title: "Adoption: Individual, Any Use"
    csv: "2026-07-01-stanford-del-adoption-monitor/29224364-adoption-individual-any-use.csv"
    rows: 11
  - id: "29906270"
    title: "Adoption: Frequency"
    csv: "2026-07-01-stanford-del-adoption-monitor/29906270-adoption-frequency.csv"
    rows: 23
  - id: "29239295"
    title: "Adoption: Individual, Work Use"
    csv: "2026-07-01-stanford-del-adoption-monitor/29239295-adoption-individual-work-use.csv"
    rows: 21
  - id: "29239570"
    title: "Adoption: Firms"
    csv: "2026-07-01-stanford-del-adoption-monitor/29239570-adoption-firms.csv"
    rows: 40
---

- ← Research

- ← All Work

- ← The AI Economic Indicators

# Adoption Monitor

#### How fast are individuals and firms adopting AI and related technologies?

Many contemporary AI tools are low- or no-cost and available digitally, allowing for rapid adoption. Capturing a rich picture of AI adoption requires drawing on a number of sources. Here, we track individual- and firm-level trends across surveys and countries.

While widespread adoption is neither necessary nor sufficient for broader economic impact, such adoption can indicate growing or shrinking importance of the technology in everyday and economic life.

We report individual-level, self-reported adoption rates from a variety of surveys. These surveys can differ in their sample size, the populations they represent, and elicitation strategy. This portfolio of surveys provides multiple signals on self-reported adoption.

Self-reported adoption captures specific forms of AI use that individuals are likely to consider generative AI. They might fail to capture embedded or ambient use, as well as integrated tools like spell checking and autocomplete.

We complement the individual results with surveys of firms across a number of high-income countries. These results capture the use of AI in production, as reported by company leadership. The use of AI in production and the cost incurred could provide a more reliable signal of the value of the technology for economically meaningful tasks. However, this signal is mitigated by adoption and diffusion frictions.

## Generative AI Adoption by Individuals in the U.S.

Generative AI Use in Personal or Work Life

Self-reported adoption of generative AI tools for work and personal use cases continues its steady upward trend, reaching 62% adoption in May 2026

> **[Chart: Adoption: Individual, Any Use]** Flourish 29224364; data snapshot: `2026-07-01-stanford-del-adoption-monitor/29224364-adoption-individual-any-use.csv` (11 rows)

Generative AI tools are used often in personal or work life, but self-reported daily use remains low. Nearly 90% of generative AI users report using these tools every week, but only a quarter of users report using them every day.

> **[Chart: Adoption: Frequency]** Flourish 29906270; data snapshot: `2026-07-01-stanford-del-adoption-monitor/29906270-adoption-frequency.csv` (23 rows)

Generative AI Use for Work

Self-reported adoption rates of generative AI for work diverge in recent surveys: Hartley et al. report a decrease in adoption, while Gallup and Bick, Blandin, and Deming report continued increases towards 50% adoption.

> **[Chart: Adoption: Individual, Work Use]** Flourish 29239295; data snapshot: `2026-07-01-stanford-del-adoption-monitor/29239295-adoption-individual-work-use.csv` (21 rows)

## Generative AI Adoption by Firms in Select Countries

Current and Expected Firm-Level AI Adoption

> **[Chart: Adoption: Firms]** Flourish 29239570; data snapshot: `2026-07-01-stanford-del-adoption-monitor/29239570-adoption-firms.csv` (40 rows)

Adoption is Widespread and Led by US Firms

Last update of this summary: June 10, 2026

Across all applications excluding text generation using LLMs, firms expect to increase adoption in the next three years. Robotics and autonomous vehicles see relatively large gaps between current and expected adoption.

Adoption trends for text generation using LLMs include forecasted decreases.

U.S. firms report slightly higher adoption at present, but level differences are ultimately modest. Respondents expect these between-country gaps to narrow slightly in coming years.

These data were reported by senior executives between November 2025 and January 2026.

## Last updated July 1, 2026. Results are updated as new data are made available.

## Summary of Recent Results

### Individual adoption is growing but remains unevenly distributed

Two of three surveys show continued increases in individual adoption on the extensive margin. On the intensive margin, approximately one quarter of users report daily usage. Adoption patterns along the intensive and extensive margins are distinct.

### Firms forecast modest increases in adoption

While firms have quickly adopted LLMs for text generation, they forecast modest extensive margin adoption over the next three years. On net, 6% of firms expect to move from not using any AI technology to using such tools.

#### Cite the Adoption Monitor

Stanford Digital Economy Lab. "AI Economic Indicators: Adoption Monitor." Accessed [access date]. https://digitaleconomy.stanford.edu/project/indicators/adoption/

@misc{stanford-indicators-adoption, author = {{Stanford Digital Economy Lab}}, title = {AI Economic Indicators: Adoption Monitor}, year = {[access year]}, urldate = {[access-date]}, url = {https://digitaleconomy.stanford.edu/project/indicators/adoption/} }

#### Cite the Included Works

Bick, Alexander, Adam Blandin, and David J. Deming. 2026. "The Rapid Adoption of Generative AI." Management Science. https://doi.org/10.1287/mnsc.2025.02523.

Gallup. 2026. "Artificial Intelligence." April 2026. https://www.gallup.com/699797/indicator-artificial-intelligence.aspx.

Sidoti, Olivia, and Colleen McClain. 2025. "34% of U.S. Adults Have Used ChatGPT, About Double the Share in 2023." Pew Research Center, June 25, 2025. https://www.pewresearch.org/short-reads/2025/06/25/34-of-us-adults-have-used-chatgpt-about-double-the-share-in-2023/.

Hartley, Jonathan, Filip Jolevski, Vitor Melo, et al. 2026. "The Labor Market Effects of Generative Artificial Intelligence." SSRN, January 25, 2026. https://doi.org/10.2139/ssrn.5136877.

Yotzov, Ivan, Jose Maria Barrero, Nicholas Bloom, et al. 2026. "Firm Data on AI." NBER Working Paper No. 34836. National Bureau of Economic Research. https://doi.org/10.3386/w34836.

## Featured Affiliates

Nick Bloom’s research interests focus on measuring and explaining management practices across firms and countries.

His research includes collecting data from thousands of manufacturing firms, retailers, schools and hospitals across countries to develop a quantitative basis for management research. Recently, Nick has also been running management field experiments in India to identify clearly causal links between management and performance.

## The Indicators Team

Connacher Murphy is a research manager at DEL, where he works with lab scholars to turn their research on the economic impacts of AI into low-latency, regularly updated measures of the economic impacts of AI. He also pursues new research partnerships for this work. These efforts are housed under the forthcoming Stanford AI Economics Observatory.

Connacher is interested in the economic and social impacts of AI, both for their relevance to policy and as strong proxies for capabilities.

Erik Brynjolfsson is one of the world’s leading experts on the economics of technology and artificial intelligence. He is the Jerry Yang and Akiko Yamazaki Professor and Senior Fellow at the Stanford Institute for Human-Centered AI (HAI), and Director of the Stanford Digital Economy Lab. He also is the Ralph Landau Senior Fellow at the Stanford Institute for Economic Policy Research (SIEPR), Professor by Courtesy at the Stanford Graduate School of Business and Stanford Department of Economics, and a Research Associate at the National Bureau of Economic Research (NBER).

One of the most-cited authors on the economics of information, Brynjolfsson was among the first researchers to measure productivity contributions of IT and the complementary role of organizational capital and other intangibles.

## Explore the rest of the Indicators

The AI Economic Indicators

## Canaries Dashboard

A collaboration between ADP Research and the Stanford Digital Economy Lab, we track employment across occupations and worker groups with different levels of AI exposure.

## Transformation Tracker

Macroeconomic signals associated with advances in AI capabilities and broader economic change.

## GDP-B: Surplus Observer

We track consumer surplus from generative AI tools over time, allowing us to understand the dynamics and components of the consumer welfare contributions of AI.

## Chart data (snapshot)

Every chart on the page is a Flourish embed. Its full data series, as published on the access date, is saved as CSV in the folder named in each row. Index charts are rebased to November 2022 = 100 unless stated.

| Flourish id | Chart | Rows | CSV | Footer note |
| --- | --- | ---: | --- | --- |
| 29224364 | Adoption: Individual, Any Use | 11 | `2026-07-01-stanford-del-adoption-monitor/29224364-adoption-individual-any-use.csv` | Pew results are limited to ChatGPT, whereas BBD cover general use of generative AI tools. |
| 29906270 | Adoption: Frequency | 23 | `2026-07-01-stanford-del-adoption-monitor/29906270-adoption-frequency.csv` |  |
| 29239295 | Adoption: Individual, Work Use | 21 | `2026-07-01-stanford-del-adoption-monitor/29239295-adoption-individual-work-use.csv` | Gallup • Pew results are limited to ChatGPT, whereas other sources cover general use of generative AI tools. |
| 29239570 | Adoption: Firms | 40 | `2026-07-01-stanford-del-adoption-monitor/29239570-adoption-firms.csv` |  |
