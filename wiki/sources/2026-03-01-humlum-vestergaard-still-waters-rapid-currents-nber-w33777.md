---
type: source
kind: paper
title: "Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI"
author: ["Anders Humlum", "Emilie Vestergaard"]
publisher: "National Bureau of Economic Research (NBER Working Paper 33777); first version also Becker Friedman Institute Working Paper 2025-56"
url: "https://www.nber.org/papers/w33777"
doi: "10.3386/w33777"
date_published: 2026-03-01
date_first_issued: 2025-05-09
date_ingested: 2026-11-07
length: "~131 pages (March 2026 revision: body pp. 1-34 read in full, appendices not read; the May 2025 BFI version read for its abstract and introduction)"
raw: "../../raw/papers/2026-03-01-humlum-vestergaard-still-waters-rapid-currents.md"
aliases: ["Large Language Models, Small Labor Market Effects"]
tags: [nber, bfi, working-paper, denmark, statistics-denmark, register-data, linked-survey-register, ai-chatbots, chatgpt, difference-in-differences, earnings, hours, null-effects, employer-encouragement, enterprise-chatbots, training, task-reorganization, new-tasks, occupational-mobility, early-career-employment, productivity-j-curve, ai-employment-effects, version-history]
dynamic_capabilities:
  - contextual/internal-enablers
  - digital-transforming/redesigning-internal-structures
relationships:
  - type: contradicts
    target: 2026-04-28-brynjolfsson-canaries-coal-mine
    via: "both see early-career employment falling in AI-exposed occupations (US payroll data; Danish registers). Canaries groups workers by occupational exposure; Humlum and Vestergaard split by whether the workplace actually adopted chatbots and find the decline is not at adopting workplaces, ruling out effects above a third of a percentage point on the early-career share"
    confidence: 0.7
  - type: supports
    target: 2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai
    via: "both find no measurable labour-market effect of AI yet with difference-in-differences designs: US unemployment by exposure quartile (CPS) there; Danish earnings and hours by actual chatbot adoption here"
    confidence: 0.7
  - type: supports
    target: 2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs
    via: "both report little or no employment effect of AI to date. Hatzius from occupation-level correlations without a published method; Humlum and Vestergaard from worker- and workplace-level register data with adoption measured directly"
    confidence: 0.65
  - type: supports
    target: 2026-10-01-yotzov-barrero-bloom-nber-w34836-firm-data-on-ai
    via: "both find wide adoption with no net employment effect so far: Danish workers' earnings and hours unchanged; executives in seven countries report about zero own-firm employment change. The paper cites Yotzov et al. for the firm-level pattern"
    confidence: 0.7
---

# Still Waters, Rapid Currents (Humlum and Vestergaard, NBER w33777)

## TL;DR

A working paper by Anders Humlum (University of Chicago Booth) and Emilie Vestergaard (University of Copenhagen). With Statistics Denmark they surveyed about 25,000 workers in 11 AI-exposed occupations, twice, and linked the answers to administrative records of earnings, hours and jobs. This is the March 2026 revision. The paper first circulated in May 2025 as *"Large Language Models, Small Labor Market Effects"*.

1. **No effect on earnings or hours, two years after ChatGPT.** *"We estimate precise null effects on earnings and recorded hours at both the worker and workplace levels, ruling out effects larger than 2% two years after the launch of ChatGPT"* (abstract, p. 2). Registers run to December 2024 (p. 5).
2. **The early-career decline is not at adopting firms.** Denmark shows a fall in early-career employment in several exposed occupations, as the US does. But workplaces that encourage chatbots show no different change in their early-career share, with bounds of a third of a percentage point (p. 32).
3. **Employers drive adoption.** 43% of employers encourage chatbot use and 6% ban it (p. 12). Where the employer does nothing, about 41% of workers have used chatbots at work; with encouragement, enterprise tools and training together, 93% have, and 28% use them daily (p. 15).
4. **Work changes before pay does.** About 8% of users take on new tasks with no employer initiative, about 18% with one (p. 16). 85% of users move saved time to other tasks (p. 16). The authors call this *"rapid currents"* under *"still waters"* (p. 3).
5. **Occupational mobility is the one visible margin.** Adopters are more likely to switch occupation; switchers' earnings grow 12 points faster, but they are too few to move the average (pp. 5-6).

## Key data

| Measure | Figure | Page (PDF, March 2026) |
| --- | --- | --- |
| Survey | ~25,000 valid responses per round (115,000 invited), Nov-Dec 2023 and 2024, 11 occupations, ~7,000 workplaces | 3, 9, 11 |
| Register window | Monthly earnings, hours, occupations through December 2024 | 5 |
| Earnings effect bound (pooled DiD) | rules out effects > 2% | 2, 5, 25 |
| Earnings effect bound (dynamic DiD) | rules out changes > 3% | 25 |
| Workplace hours (encouraging workplaces) | rules out effects > 2% | 32 |
| Early-career share at adopting workplaces | rules out effects > 1/3 percentage point | 32 |
| Job churn at encouraging workplaces | rules out effects > 0.5% of employment a month | 33 |
| Employer policy | 43% encourage, 21% allow, ~6% prohibit | 12 |
| Among encouraging employers | 61% enterprise chatbot, 39% training, 29% both | 12 |
| Workers who used chatbots at work: no initiative / encouraged / all three initiatives | ~41% / 76% / 93% | 15 |
| Daily use: no initiative / encouraged / all three | 7% / 18% / 28% | 15 |
| Users reporting new tasks | ~8% (no initiative) to ~17-18% (with initiatives) | 4, 16 |
| Workers saying chatbots did not affect their earnings | 97.7% of adopters, 99.5% of non-adopters | 34 |

## Method and definitions

- **Data.** Two surveys distributed by Statistics Denmark through the national digital mailbox, in November-December 2023 and 2024, linked by (de-identified) personal number to matched employer-employee registers (pp. 9, 11). The main analysis uses the 2024 round; the 2023 round identifies early adopters (p. 11).
- **Occupations.** Accountants, customer support specialists, financial advisors, HR professionals, IT support specialists, journalists, legal professionals, marketing professionals, office clerks, software developers and teachers (p. 3, footnote 2). These are chosen because they are *highly exposed*, where effects should show first.
- **Design.** Difference-in-differences: adopters against comparable non-adopters, before and after November 2022, at worker and workplace level (pp. 18-20). Employer encouragement serves as the main workplace treatment and as a source of variation in worker adoption less tied to individual earnings paths (pp. 20, 25).
- **"Adoption"** means having used AI chatbots at work; intensity is measured as daily use and self-reported time savings.
- **Funding:** Center for Applied Artificial Intelligence and Polsky Center, University of Chicago (NBER page acknowledgements).

## Scope and reliability

- **Register outcomes, not self-reports.** The central finding rests on administrative earnings and hours, which is rare in this literature. Adoption and benefits are self-reported.
- **One country, eleven occupations, two years.** Denmark has flexible hiring and frequent wage negotiation, so pay could have moved (p. 9). The results may not carry to other settings, or to later and more capable tools.
- **The headline tightened, then loosened, across versions.** The May 2025 version (also BFI Working Paper 2025-56) said *"precise zeros"*, with confidence intervals *"ruling out effects larger than 1%"*, on registers through June 2024, *"one and a half years after ChatGPT's launch"* (BFI version, pp. 2, 5). The October 2025 and March 2026 versions extend registers to December 2024 and state a 2% bound. The May 2025 version also reported average time savings of 2.8% of work hours and a 3-7% pass-through of productivity gains to earnings (BFI version, pp. 4-5). A text search of the March 2026 version finds neither figure.
- **A null at the margin is not a null overall.** The design compares adopters with non-adopters, so effects on everyone at once (the *"missing intercept"*) are differenced out. The authors argue, with a model, that such spillovers are also small (p. 22).
- **Working paper, not peer-reviewed.**

## Dynamic-capabilities reading

- **`contextual/internal-enablers`**: employer encouragement, enterprise chatbots and training raise take-up from about 41% to 93% and raise reported benefits. The paper treats these firm initiatives as complementary organisational investments.
- **`digital-transforming/redesigning-internal-structures`**: firms absorb chatbots by reorganising tasks: new work in content generation, AI quality review and compliance, and AI integration, rather than by changing headcount or hours.

## How it connects

- [[ai-employment-effects]] and the thread [[ai-employment-effects-measurement-dispute]]: non-US evidence that splits the early-career decline by actual adoption. The thread's item 5 asked for non-US evidence.
- [[2026-04-28-brynjolfsson-canaries-coal-mine|Canaries in the Coal Mine]] and its [[2026-10-21-stanford-del-canaries-dashboard|dashboard]] measure the same early-career decline in US payroll data by occupational exposure. This paper measures it by firm adoption.
- [[2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai|Massenkoff and McCrory]] find no systematic US unemployment effect by exposure quartile.
- [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs|Hatzius (Goldman Sachs)]] reports small occupation-level correlations.
- [[2026-10-01-yotzov-barrero-bloom-nber-w34836-firm-data-on-ai|Yotzov et al. (NBER 34836)]] report near-zero net employment change from the executive side.
- [[micro-productivity-trap]]: workers report benefits, registers show no change in pay or hours, and the authors name the productivity J-curve as one reading.
- [[enterprise-ai-adoption]]: employer encouragement as the main lever on worker adoption.

## What was actually ingested

The March 2026 NBER version (131 pages): abstract, introduction, sections 1-4 and the conclusion (PDF pp. 2-36). Appendices (models, robustness, the questionnaire) were not read. The May 2025 version (BFI Working Paper 2025-56, 117 pages), which the Dutch report links, was read for its abstract and introduction (PDF pp. 2-6) to record the version differences. The October 2025 version was checked for its abstract only.

## Linked entities and concepts

- Concepts: [[ai-employment-effects]], [[micro-productivity-trap]], [[enterprise-ai-adoption]], [[automation-vs-augmentation]].
- Entities: [[Erik Brynjolfsson]] (Canaries co-author, cited), [[Daron Acemoglu]] (cited for a forecast of under 0.07 points a year of extra TFP growth, p. 3).
- **Dangling** (single-source mention, deferred): Anders Humlum, Emilie Vestergaard, Statistics Denmark, Becker Friedman Institute, University of Chicago Booth School of Business, University of Copenhagen, National Bureau of Economic Research.
