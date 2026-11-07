---
type: source
kind: article
title: "Lucie Mussett - LFPSE Project Lead at NHS England Breaks Down the New Incident Recording System"
author: ["Emma Duggan"]
publisher: "MEG (megit.com), quality-management software vendor"
url: "https://megit.com/news-page/lfpse-interview-lucie-mussett"
date_published: 2023-03-08
date_ingested: 2026-11-07
length: "~1,900-word vendor-blog interview, read in full"
raw: "../../raw/articles/2023-03-08-meg-lfpse-mussett-interview.md"
tags: [patient-safety, incident-reporting, lfpse, nrls, nhs-england, machine-learning, free-text-analysis, taxonomy, psirf, vendor-blog, interview, 2023]
---

# Lucie Mussett on England's Learn From Patient Safety Events service (MEG interview, March 2023)

## TL;DR

A Q&A on the blog of MEG, a vendor of incident-reporting software, with **Lucie Mussett**, then Senior Project Owner and Lead for the Learn From Patient Safety Events (LFPSE) service at NHS England. LFPSE replaces the 20-year-old National Reporting and Learning System (NRLS). The interview is from **8 March 2023**. Four points:

1. **Reading capacity is the bottleneck.** *"We get over 2.6 million records annually; the free text is where all the essential information is. However, at the moment, we only have the capacity to manually read 10,000 a year (usually events classified as severe harm/death in the NRLS)."* That is about 0.4% of records.
2. **Machine learning to choose what gets read.** *"Machine Learning is going to flip that completely. It won't be automating the entire process, but instead identifying keywords, signals, and triggers to sort records that need to be read, in turn, allowing us to do more preventative work."*
3. **Feedback to the person who reported.** ML should also tag records and send reporters guidance, e.g. on preparing and giving a drug after a medication incident, so that reporting stops feeling like a *"black box."*
4. **A new taxonomy.** Multiple patients per event, multi-select "what" questions instead of one incident category (the NRLS's "OTHER" bucket hid under-recognised risks), estimated times, and separate event types: Incident, Risk, Good Care, Outcomes.

## Key data

| Item | Figure or fact | Note |
| --- | --- | --- |
| Records received per year | "over 2.6 million" | as stated, March 2023 |
| Records read by hand per year | 10,000 | mostly severe harm or death |
| NRLS database | "over 20 million reports" | on "20-year-old technology" |
| LFPSE national roll-out | July 2021 | per the post's standfirst |
| Mandatory event types | Incident, Good Care | Risk and Outcomes optional |

## Method and definitions

An interview, not a study. The questions and editing are MEG's. Mussett speaks as the project's lead; she had been with the National Patient Safety team since 2013 and led the agile team building LFPSE. The "we" who read 10,000 records is the national patient safety team. The interview does not say how many records the reporting organisations read themselves; local reviews and investigations fall under PSIRF, the Patient Safety Incident Response Framework.

## Scope and reliability

- **Dated.** The figures and the ML plans are from March 2023. The interview does not say whether machine learning was in use then, and it is no evidence of what LFPSE does now.
- **Vendor channel.** MEG says it is an LFPSE-compliant vendor and runs the series to explain the system to customers. Mussett's statements are hers; the framing is MEG's.
- **No numbers on ML performance.** "Flip that completely" is an expectation. The interview gives no accuracy, coverage or timeline.

## Dynamic-capabilities reading

Not tagged. The interview describes a public-sector reporting system; no Warner & Wäger cell fits without stretching it.

## How it connects

- [[2025-09-17-beidler-incident-report-severity-triage-radiotherapy|Beidler, Nguyen et al. (2025)]] test a machine screen that ranks radiotherapy incident reports by severity for human review, the kind of sorting Mussett describes. In-house it matches individual staff; on a multinational repository it fails until retrained on local data.
- [[agent-oversight-and-delegation]] — Mussett's design keeps people reading: the model selects what is read and does not decide on its own.
- [[responsible-ai]] — feeding learning back to the people who report, as a goal of the reporting system itself.
- [[ai-in-health-care]]: the concept page that sets the health-care sources in this wiki side by side.

## What was actually ingested

The full blog post, fetched on 7 November 2026 from the address cited in the Dutch report (`megsupporttools.squarespace.com`), whose canonical address is megit.com. Site navigation and footer left out.

## Linked entities and concepts

- [[agent-oversight-and-delegation]], [[responsible-ai]] — concepts.

**Dangling** (single-source mention, deferred): Emma Duggan (author, MEG); Lucie Mussett (interviewee, NHS England); MEG (publisher); NHS England; National Patient Safety Agency; NRLS and LFPSE (systems).
