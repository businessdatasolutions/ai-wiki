---
type: source
kind: report
title: "Hospital Trends in the Use, Evaluation, and Governance of Predictive AI, 2023-2024"
author: ["Wei Chang", "Priscilla Owusu-Mensah", "Jordan Everson", "Chelsea Richwine"]
publisher: "Office of the Assistant Secretary for Technology Policy (ASTP/ONC), U.S. Department of Health and Human Services; ASTP Data Brief No. 80"
url: "https://www.healthit.gov/data/data-briefs/hospital-trends-use-evaluation-and-governance-predictive-ai-2023-2024"
date_published: 2025-09-17
date_ingested: 2026-11-07
length: "17 pages (9 pages of findings and summary + definitions, methods and appendix), read in full"
raw: "../../raw/reports/2025-09-17-astp-hospital-predictive-ai-2023-2024.md"
tags: [astp, onc, hhs, aha-it-supplement, hospitals, predictive-ai, machine-learning, ehr, clinical-decision-support, ai-governance, model-evaluation, model-bias, post-implementation-monitoring, digital-divide, government-statistics, united-states, healthcare]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-transforming/redesigning-internal-structures
relationships:
  - type: supports
    target: 2026-04-30-ai-index-report-2026
    via: "clinical AI deployed faster than it is evaluated: the AI Index on published studies (5% use real clinical data), ASTP on hospitals' own model checks (71% evaluate all or most models for accuracy, 57% for bias, 2024)"
    confidence: 0.65
---

# Hospital trends in the use, evaluation and governance of predictive AI, 2023–2024 (ASTP Data Brief 80)

## TL;DR

A federal data brief on US hospitals, based on the American Hospital Association's annual IT survey. Five findings:

1. **71% of hospitals use predictive AI in their EHR**, up from **66%** in 2023, a significant rise (p. 1–2). "Hospitals" means non-federal acute care hospitals, and "predictive AI" includes non-machine-learning predictive models (p. 13).
2. **A digital divide.** 86% of system-affiliated hospitals use it against 37% of independent ones; 96% of large hospitals against 59% of small ones; **90% of hospitals on the market-leading EHR** against 50% on other vendors (2024, p. 3).
3. **Administrative uses grow fastest.** Among users, predictive AI for billing rose from 36% to 61% and for scheduling from 51% to 67% between 2023 and 2024 (p. 4, p. 8). Inpatient risk prediction is the most common use and stayed flat (p. 4).
4. **Most hospitals evaluate, fewer evaluate everything.** In 2024, 82% evaluated models for accuracy, 74% for bias and 79% monitored after go-live. Only **71%** checked all or most models for accuracy and **57%** for bias (p. 6). Between 15% and 21% answered "don't know" (p. 6).
5. **Governance by committee.** 74% name more than one entity accountable for evaluating predictive AI. A dedicated AI committee or task force (66%) and department leaders (60%) are named most; IT staff least (41%) (p. 7).

## Key data

| Measure (non-federal acute care hospitals) | 2023 | 2024 | Page |
| --- | ---: | ---: | --- |
| Use predictive AI integrated with the EHR | 66% | **71%** | p. 2 |
| System-affiliated / independent | 81% / 31% | 86% / 37% | p. 3 |
| Large (400+ beds) / small (<100) | 90% / 53% | 96% / 59% | p. 3 |
| Market-leading EHR vendor / all others | 87% / 48% | 90% / 50% | p. 3 |
| Users applying it to billing | 36% | 61% | p. 4, p. 8 |
| Users applying it to scheduling | 51% | 67% | p. 4, p. 8 |
| Evaluated for accuracy (any / all or most models) | 80% / 63% | 82% / **71%** | p. 6 |
| Evaluated for bias (any / all or most models) | 73% / 44% | 74% / **57%** | p. 6 |
| Post-implementation evaluation or monitoring (any / all or most) | not asked | 79% / 58% | p. 6 |
| Multiple entities accountable for evaluation | not asked | 74% | p. 7 |
| Model source: EHR developer / third party / self-developed | 79% / 59% / 54% | 80% / 52% / 50% | p. 5, p. 15 |

The chart values on p. 4 and p. 6 are read from flattened bar labels; the 2023→2024 billing and scheduling figures are confirmed in the summary text (p. 8).

## Method and definitions

- **Data.** The American Hospital Association (AHA) IT Supplement to its Annual Survey, which ASTP funds. Each hospital's CEO is invited; the person who knows its health IT best, typically the CIO, answers by mail or online (p. 11).
- **Fieldwork.** 2024: April to September 2024, response rate 51% of 2,253 non-federal acute care hospitals. 2023: March to August 2023, 58% of 2,547 (p. 11). Results are weighted by the inverse of each hospital's predicted response propensity (p. 11).
- **Denominators.** Adoption: hospitals answering the question, n = 2,425 (2023) and 2,080 (2024), with "don't know" excluded (p. 2). Use cases and evaluation: hospitals using predictive AI, n = 1,696 and 1,587 (p. 4, p. 6).
- **What counts.** *"Does your hospital use any machine learning or other predictive models that display output or recommendations (e.g., risk scores or clinical decision support) in your EHR or an App embedded in or launched by your EHR?"* Non-ML models such as APACHE IV count (p. 13). Generative AI is not asked about.
- **Evaluation** means the share of models checked "using data from your hospital or health system," on a five-step scale from all to none (p. 14).

## Scope and reliability

- **Strong instrument for its scope.** A long-running, weighted, near-census survey of US hospitals, published by the federal health-IT office.
- **Self-report by one person per hospital**, usually the CIO. "Don't know" runs at 15–21% on the evaluation questions and is excluded from the denominator (p. 6), so the evaluation shares may be high.
- **Broad definition.** "Predictive AI" spans sepsis alerts, fall-risk scores, readmission risk and no-show prediction, and includes classical scores. The 71% says that a hospital runs at least one such model in its EHR, not how many or how deeply.
- **Question change.** In 2024 the use question was asked separately for ML and non-ML models; in 2023 as one choice list (p. 13). The brief does not discuss whether this affects the trend.
- **Governance question is new in 2024** (p. 7), so there is no trend yet.

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`**: a national scan of how far US hospitals have taken up predictive AI, by hospital type and EHR vendor.
- **`digital-transforming/redesigning-internal-structures`**: the governance findings describe new structures, a dedicated AI committee or task force (66%) and a designated senior executive such as a CMIO or CIO (55%), accountable for evaluating models (p. 7).

## How it connects

- [[enterprise-ai-adoption]] — a sector-wide adoption figure with an exact question, comparable year on year.
- [[ai-maturity-measurement-comparison]] — "use" here means at least one predictive model in the EHR; the brief also measures depth (all or most models evaluated), which is lower.
- [[2026-04-30-ai-index-report-2026|AI Index 2026]] — its Medicine chapter takeaway: clinical AI is widely deployed while the published evidence base stays thin (5% of 500+ studies use real clinical data). This brief measures the hospital side: how many hospitals check their own models.
- [[responsible-ai]] — local accuracy and bias checks, post-go-live monitoring and accountable committees, measured across a whole sector. The brief points to the NIST AI Risk Management Framework and compares the multi-party set-up with the "three lines of defense" in financial-services model governance (p. 8–9).
- [[2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals|Dinakaran (Luminai)]] and [[2026-10-20-parikh-google-cloud-hippocratic-ai-voice-agents-healthcare|Parikh (Hippocratic AI)]] — vendors selling administrative and outreach automation into US hospitals, the use cases this brief finds growing fastest.
- [[ai-in-health-care]]: the concept page that sets the health-care sources in this wiki side by side.

## What was actually ingested

The full 17-page PDF and the web page that hosts it. Bar-chart values (Figures 1–4, A1–A2) were read from the flattened text; where a label's position was ambiguous, only values confirmed in the text are given.

## Linked entities and concepts

- [[enterprise-ai-adoption]], [[responsible-ai]] — concepts.

**Dangling** (single-source mention, deferred): Wei Chang, Priscilla Owusu-Mensah, Jordan Everson, Chelsea Richwine (authors); Office of the Assistant Secretary for Technology Policy (ASTP, formerly ONC); American Hospital Association (data source); NIST AI Risk Management Framework.
