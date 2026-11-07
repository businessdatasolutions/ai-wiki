---
type: source
kind: paper
title: "Adoption of artificial intelligence in healthcare: survey of health system priorities, successes, and challenges"
author: ["Eric G Poon", "Christy Harris Lemak", "Juan C Rojas", "Janet Guptill", "David Classen"]
publisher: "Journal of the American Medical Informatics Association (JAMIA) 32(7):1093–1100"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC12202002/"
doi: "10.1093/jamia/ocaf065"
date_published: 2025-05-05
date_ingested: 2026-11-07
length: "~8 journal pages (full text read from PMC HTML, incl. Tables 1–2 and Figure 1; supplementary appendices not accessible)"
raw: "../../raw/papers/2025-05-05-poon-jamia-health-system-ai-adoption.md"
tags: [jamia, scottsdale-institute, health-systems, hospitals, united-states, use-case-adoption, ambient-notes, ambient-scribes, clinical-documentation, sepsis-prediction, fall-risk, imaging-radiology, risk-stratification, ai-barriers, peer-reviewed, survey, ai-maturity]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-transforming/improving-digital-maturity
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care
    via: "imaging AI: deployed in at least limited areas by 90% of 43 US health systems, yet 19% report high success with diagnostic AI; Peron says the predicted displacement of radiologists did not play out"
    confidence: 0.6
  - type: supports
    target: 2025-09-17-astp-hospital-predictive-ai
    via: "use-case-level AI use in US hospitals, incl. predictive models in the EHR; Poon et al. cite Nong et al.'s hospital-survey work on predictive models (ref. 20)"
    confidence: 0.7
  - type: supports
    target: 2025-04-15-bessemer-healthcare-ai-adoption-index
    via: "ambient documentation as the fastest-moving use case, measured on different stage scales"
    confidence: 0.65
---

# Adoption of AI in healthcare: survey of health system priorities, successes, and challenges — Poon et al., JAMIA 2025

> Ambient Notes is rapidly advancing in US healthcare systems and demonstrating early success. Other AI use cases show varying degrees of adoption and success, constrained by barriers such as immature AI tools, financial concerns, and regulatory uncertainty.
>
> — the abstract's conclusion

## TL;DR

A peer-reviewed survey of **43 large US non-profit health systems** (Scottsdale Institute members, fall 2024). It reports adoption **per use case** in four stages, which separates trying AI from running it fully.

1. **Any deployment and full deployment are far apart.** For **fall-risk prediction**, 36% deploy at least in limited areas but **19%** have deployed it fully. For **Ambient Notes**, 60% deploy (47% limited, **14%** full), while **all 43** have at least started developing or piloting it (Table 2).
2. **Imaging is the most widely deployed clinical AI**: 90% in at least limited areas, 40% fully. Early sepsis detection: 67% deploy, 48% fully.
3. **Reported success is modest outside documentation.** A "high degree of success": clinical documentation 53%, clinical risk stratification 38%, revenue cycle 23%, diagnosis 19% (Figure 3, among organisations active in each category).
4. **Goals are about staff and safety, not money.** Top-two goals: caregiver burden 72%, **patient safety/quality 56% in the text (58% in Figure 1)**, workflow efficiency 53%, margin improvement 12%, market share 0%.
5. **The top barrier is immature tools** (77%), then financial concerns (47%) and regulatory uncertainty (40%). Leadership support (7%) is rarely the issue.

## Key data

Table 2 (n = 43; some items 40–42 answering), stage shares per use case:

| Use case | No activity | Developing or piloting | Deploying in limited areas | Deployed fully | Any deployment |
| --- | ---: | ---: | ---: | ---: | ---: |
| Ambient Notes | 0% | 40% | 47% | **14%** | 60% |
| Imaging and radiology | 5% | 5% | 50% | 40% | 90% |
| Early detection of sepsis | 12% | 21% | 19% | 48% | 67% |
| Risk of clinical deterioration | 9% | 35% | 19% | 37% | 56% |
| Risk of patient falls | 21% | 43% | 17% | **19%** | 36% |
| In-basket automation | 7% | 42% | 37% | 14% | 51% |
| Medical coding | 17% | 38% | 21% | 24% | 45% |
| Inpatient chart summarization | 21% | 71% | 7% | 0% | 7% |
| Drug discovery | 61% | 39% | 0% | 0% | 0% |

"Any deployment" = limited + full; the paper's Figure 2 reports it as "deployed in at least limited areas".

| Other measure | Figure | Where |
| --- | ---: | --- |
| Top-two goal: caregiver burden / safety and quality / workflow efficiency | 72% / 56% (text) or 58% (Fig. 1) / 53% | Results, Figure 1 |
| High success: documentation / risk stratification / revenue cycle / diagnosis | 53% / 38% / 23% / 19% | Figure 3 |
| Top-two barrier: immature tools / financial / regulatory | 77% / 47% / 40% | Figure 4 |
| Always measure uptake / always measure equity | 74% / 17% | Results |

## Method and definitions

- **Sample.** All 67 Scottsdale Institute member systems were invited; 46 started and **43 completed** (64%). One response per system, from the CMIO/CHIO/CCIO (50%), CIO/CDO (13%) or chief AI or data officer (13%).
- **Fieldwork.** Invitations sent 27 September to 20 October 2024 (SurveyMonkey). IRB approval at the University of Alabama at Birmingham.
- **Instrument.** 37 AI use cases in 10 categories, each rated: no activity, developing or piloting, deploying in limited areas, deployed fully. Perceived success per category, six goals and six barriers ranked, nine performance metrics.
- **Definitions.** "Deployed fully" and "limited areas" are the respondent's own reading; the paper gives no threshold.
- **Funding and conflicts.** No funding. Rojas and Poon report consulting fees (Truveta, Triomics).

## Scope and reliability

- **Peer-reviewed, small N, non-random.** Members of a quality-improvement collective, mostly $1–10B net patient revenue and 67% major teaching. The authors say their AI adoption *"may be more advanced compared to their average peer."*
- **A snapshot of fall 2024**, less than two years after ChatGPT.
- **Clinician-heavy respondents** may understate business and revenue-cycle use, as the authors note.
- **Internal inconsistency.** The text says patient safety/quality was a top-two goal for "56% (n = 25)"; 25 of 43 is 58%, and Figure 1 shows 58%.
- **US only.** No European data.

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`**: a census-style scan of which AI use cases US health systems are trying, piloting and running.
- **`digital-transforming/improving-digital-maturity`**: the four-stage scale per use case is a maturity measure; full deployment is rare except for sepsis, deterioration and imaging.
- **`contextual/internal-barriers`**: financial concerns, low clinician adoption and missing expertise are ranked as barriers alongside the external ones (immature tools, regulation).

## How it connects

- [[enterprise-ai-adoption]] — per-use-case evidence for breadth without depth in one sector: many systems try a use case, few run it fully.
- [[ai-maturity-measurement-comparison]] — a stage scale per use case, from a peer-reviewed survey, unlike the organisation-level maturity scores in most sources.
- [[technology-adoption-theories]] — the authors say Ambient Notes *"appears to have swiftly crossed the 'chasm'"* to the early majority.
- [[2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care|Peron (Philips)]] — imaging AI from a vendor's side; this survey finds it the most widely deployed clinical AI, with few reporting high diagnostic success.
- [[2026-04-30-ai-index-report-2026|AI Index 2026]] — reports that few clinical AI studies use real clinical data; Poon et al. call for *"robust evaluations"* and find equity rarely measured.
- In this batch: [[2025-04-15-bessemer-healthcare-ai-adoption-index|Bessemer / AWS / Bain]] reports ambient-scribe deployment among providers on a different scale. [[2025-09-17-astp-hospital-predictive-ai]] tracks predictive AI in US hospital EHRs; the paper cites the Nong et al. hospital-survey work in that line (ref. 20).
- [[ai-in-health-care]]: the concept page that sets the health-care sources in this wiki side by side.

## What was actually ingested

The complete article text from PMC (HTML), with Tables 1–2. Figure 1 was viewed; Figures 2–4 were not, but their values are in the text. The PDF and the supplementary appendices (use-case list, instrument, metrics) were behind a browser challenge and were not read. PMC HTML has no page numbers, so figures are cited by table, figure and section.

## Linked entities and concepts

- [[enterprise-ai-adoption]], [[technology-adoption-theories]] — concepts. [[ai-maturity-measurement-comparison]] — thread.

**Dangling** (single-source mention, deferred): Eric G Poon (Duke University Health System), Christy Harris Lemak (University of Alabama at Birmingham; Scottsdale Institute), Juan C Rojas (Rush University System for Health), Janet Guptill (Scottsdale Institute), David Classen (University of Utah), Scottsdale Institute (survey host), JAMIA (journal).
