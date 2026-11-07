---
type: source
kind: article
title: "Monitoring AI Adoption in the U.S. Economy"
author: ["Jeffrey S. Allen"]
publisher: "Board of Governors of the Federal Reserve System (FEDS Notes)"
url: "https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html"
doi: "10.17016/2380-7172.4032"
date_published: 2026-04-03
date_ingested: 2026-11-07
length: "~3,300 words (full note read, with its accessible-data page for the four figures)"
raw: "../../raw/articles/2026-04-03-allen-fed-feds-note-monitoring-ai-adoption-us-economy.md"
tags: [federal-reserve, feds-notes, census-bureau, btos, business-trends-and-outlook-survey, real-time-population-survey, survey-of-business-uncertainty, atlanta-fed, firm-ai-adoption, worker-genai-adoption, question-wording, series-break, employment-weighting, firm-size, industry-adoption, health-care, survey-methodology, social-desirability-bias, shadow-ai]
dynamic_capabilities:
  - digital-sensing/digital-scouting
relationships:
  - type: supports
    target: 2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs
    via: "both read the jump in the Census BTOS firm-adoption figure (legacy series about 10%, new series about 18-20%) as the product of the November 2025 wording change from 'producing goods or services' to 'any of its business functions'"
    confidence: 0.8
  - type: supports
    target: 2026-07-01-stanford-del-adoption-monitor
    via: "both set several US adoption surveys side by side and attribute their spread to the instrument. Both use the Real-Time Population Survey (Bick, Blandin and Deming) and the executive survey; the FEDS Note adds the Census BTOS and quantifies the size and weighting effects"
    confidence: 0.75
  - type: supports
    target: 2026-10-26-rendtorff-smith-chin-bcg-creating-ai-value-adoption
    via: "official firm-count statistics put adoption near one firm in five: the BTOS at about 18% of US firms (December 2025, new wording) and the OECD at about 20% of firms (2025); both show adoption rising with firm size"
    confidence: 0.7
---

# Monitoring AI Adoption in the U.S. Economy (FEDS Note, April 2026)

## TL;DR

A FEDS Note by Jeffrey S. Allen, Federal Reserve Board staff, published 3 April 2026. It sets three US surveys side by side and explains why they differ.

1. **About 18% of US firms use AI** (Census Business Trends and Outlook Survey, BTOS, end of 2025). Over 20% expect to in the first half of 2026.
2. **The series breaks in November 2025.** The Census Bureau changed its question from AI use *"in producing goods or services"* to use *"in any of its business functions."* The legacy series ended at about 10%; the first four surveys under the new wording average about 18% (accessible figure data). Before the change, adoption had grown 68% (3.9 points) in the year to September 2025.
3. **Workers and executives give much higher figures.** 41% of workers use generative AI for their job (Real-Time Population Survey, November 2025). The Atlanta Fed's executive survey estimates that **78% of the labour force works at firms that use AI**, and 54% at firms that use LLMs (November 2025).
4. **Most of the gap is who is counted.** 95% of US firms have fewer than 50 employees, but 56% of employment is in firms with 250 or more. The BTOS mirrors the firm population; the executive survey and a household survey draw more from large firms, which adopt more.
5. **Each survey answers a different question.** BTOS for the share of businesses, RPS for the share of workers, the executive survey as *"a good upper bound on the scope of access to AI tools at work."*

## Key data

| Survey | Date | Unit | Weighting | Estimate |
| --- | --- | --- | --- | --- |
| Census BTOS, AI in any business function | Dec 2025 | Firms | Firm-weighted | **18%** |
| Census BTOS, legacy wording (production) | last obs. before Nov 2025 | Firms | Firm-weighted | ~10% |
| Census BTOS, planned use within 6 months | Dec 2025 | Firms | Firm-weighted | ~21% |
| Real-Time Population Survey, GenAI for the job | Nov 2025 | Workers | Share of labour force | **41%** (40.7) |
| RPS, daily use at work last week | Nov 2025 | Workers | | 12% |
| Survey of Business Uncertainty, any AI | Nov 2025 | Firms | Employment-weighted | **78%** |
| SBU, LLMs | Nov 2025 | Firms | Employment-weighted | 54% |
| SBU, any AI / LLMs, equal-weighted | Nov 2025 | Firms | Unweighted | 69.4% / 46.4% |

Sector, BTOS new series: professional services about 33%, finance about 30%; information 37%, real estate 24%, wholesale 13%, accommodation and food 8%. The note says health care and social assistance *"lags behind"* finance and professional services, partly because pharmaceutical and life-science firms are classified elsewhere. The note gives no health-care figure.

Firm size and samples (percent):

| Size (employees) | Share of firms | Share of employment | BTOS sample | SBU sample |
| --- | ---: | ---: | ---: | ---: |
| 1-49 | 95 | 26.6 | 89.6 | 38.2 |
| 50-99 | 2.6 | 7.6 | 5.1 | 14.9 |
| 100-249 | 1.5 | 9.7 | 3.2 | 19.5 |
| 250+ | 0.9 | 56.2 | 2.2 | 27.4 |

## Method and definitions

- **BTOS.** Census Bureau, fortnightly, 1.2 million businesses in rotating cohorts; about 20,000 responses per survey at the end of 2025. Legacy question: *"In the last two weeks, did this business use Artificial Intelligence (AI) in producing goods or services?"* From November 2025: use *"in any of its business functions."* The note uses a four-period moving average. About 10-11% of respondents answer *"do not know."*
- **RPS.** Bick, Blandin and Deming's quarterly household survey since August 2024, 5,000-6,000 responses: *"Do you use Generative AI for your job?"*
- **SBU.** Atlanta Fed's monthly executive survey, run with Steven Davis and Nicholas Bloom; AI questions asked once, November 2025, 1,032 responses. Firms tick from seven AI categories, including *"Text generation using large language models."* Employment weighting approximates the share of the labour force at adopting firms.
- **Status.** FEDS Notes are staff views, *"shorter and less technically oriented"* than working papers, and do not represent the Board.

## Scope and reliability

- **US only, up to December 2025.** The note is a comparison of published sources, not new data.
- **The BTOS break limits trend reading.** Growth rates are for the legacy series. The new series has four observations by year-end 2025, and its size pattern differs: the legacy U-shape by firm size, with high use among the smallest firms, has moderated (footnote 3).
- **Other explanations the note weighs:** question framing and how material the reported use is; respondents who do not know; *"shadow AI"* used without management's knowledge, judged no longer a major driver; and social desirability bias, which may now push executives to over-report.
- **The SBU figure has since been recoded.** The October 2026 revision of the paper that reports this executive survey ([[2026-10-01-yotzov-barrero-bloom-nber-w34836-firm-data-on-ai|Yotzov et al., NBER 34836]]) counts firms that skipped the question as missing, not as non-users, and reports 94% for November 2025 (its footnote 13). The note's 78% matches the paper's first version.

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`**: a central-bank scan of how widely US firms and workers use AI, with a guide to which number answers which question.

## How it connects

- [[enterprise-ai-adoption]] and the thread [[ai-maturity-measurement-comparison]]: the most explicit account in the corpus of why firm adoption figures range from about one in five to more than three in four.
- [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs|Hatzius (Goldman Sachs)]] names the same Census wording change: about 10% of firms under the old question, and a Goldman estimate of *"just over 20%"* across all industries.
- [[2026-07-01-stanford-del-adoption-monitor|The Adoption Monitor]] uses the same worker survey and the same executive survey; this note adds the official firm count.
- [[2026-10-26-rendtorff-smith-chin-bcg-creating-ai-value-adoption|Rendtorff-Smith (OECD)]] reports 20% of firms in 2025 and a large-firm/small-firm gap.
- [[2026-10-01-yotzov-barrero-bloom-nber-w34836-firm-data-on-ai|Yotzov et al. (NBER 34836)]]: the executive survey's own paper, with a different coding of the same November 2025 wave.
- [[2026-06-10-anicich-brouwers-why-employees-arent-transparent-ai-usage|Anicich and Brouwers]] on hidden AI use, the "shadow AI" the note discusses.
- [[technology-adoption-theories]]: the extensive margin (any use) against the intensive margin (daily use, 12% of workers).

## What was actually ingested

The full note as served on 7 November 2026: summary, all sections, the appendix with question wording, references and footnotes. The four figures are images; their values come from the note's separate accessible-data page. Figure 1 (AI investment: hyperscaler capex of $412 billion in 2025, about 1.31% of GDP) is background and not used here.

## Linked entities and concepts

- Concepts: [[enterprise-ai-adoption]], [[technology-adoption-theories]].
- **Dangling** (single-source mention, deferred): Jeffrey S. Allen, Federal Reserve Board, U.S. Census Bureau, Federal Reserve Bank of Atlanta, Alexander Bick, Adam Blandin, David Deming (all three also named on the Adoption Monitor, not in `author:`), Nicholas Bloom, Steven J. Davis.
