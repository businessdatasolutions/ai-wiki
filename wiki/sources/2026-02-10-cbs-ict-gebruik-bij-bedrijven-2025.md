---
type: source
kind: report
title: "ICT-gebruik bij bedrijven (Digitalisering en kenniseconomie 2025, hoofdstuk 3)"
author: ["Centraal Bureau voor de Statistiek"]
publisher: "Centraal Bureau voor de Statistiek (CBS)"
url: "https://www.cbs.nl/nl-nl/longread/rapportages/2026/digitalisering-en-kenniseconomie-2025/3-ict-gebruik-bij-bedrijven"
date_published: 2026-02-10
date_accessed: 2026-11-07
date_ingested: 2026-11-07
length: "one longread chapter (~800 words of text and 4 tables, read in full) plus the AI size-class and sector split from CBS StatLine tables 86118NED and 86120NED"
raw: "../../raw/articles/2026-02-10-cbs-ict-gebruik-bij-bedrijven-2025.md"
tags: [cbs, statistics-netherlands, official-statistics, netherlands, ict-usage-survey, enterprise-ai-adoption, firm-adoption, firm-size, sector-breakdown, health-care-sector, text-mining, natural-language-generation, definition-change, series-break, provisional-figures]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-11-04-eurostat-use-of-ai-in-enterprises
    via: "the same harmonised EU enterprise survey: CBS's 33% (2025) and 23% (2024) match Eurostat's Netherlands figures of 33.21% and 23.06%, which Eurostat flags as a 2025 break in series"
    confidence: 0.8
  - type: supports
    target: 2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening
    via: "Dutch firm-level AI use from the CBS enterprise survey: this chapter gives the national total and the sector split (ICT 70%, specialist business services 55%); RaboResearch uses the same survey for AI use by business function in IT and business services, against the EU"
    confidence: 0.7
---

# ICT-gebruik bij bedrijven 2025 (CBS)

## TL;DR

Chapter 3 of the CBS report *Digitalisering en kenniseconomie 2025*. It reports how Dutch firms with 10 or more employed persons use ICT, including AI.

1. **One in three firms uses AI.** In 2025, 33% of firms with 10 or more employed persons used at least one of eight specified AI technologies. That was 23% in 2024 and 14% in 2023. The 2025 figure is provisional.
2. **Language technology leads.** Text mining is used by 22% of firms and natural language generation by 16% (2024: 14% and 12%).
3. **Sectors differ fourfold.** Information and communication 70%, financial services 59%, specialist business services 55%. Hotels and restaurants, transport and storage, and construction: 16% to 21%.
4. **10% considered AI but did not use it** (2024: 9%).
5. **The 2025 definition is wider.** An eighth technology, generating images, video or sound, was added in 2025; until 2024 seven were asked.
6. **Size matters (StatLine).** Use rises from 25% of firms with 10–20 employed persons to 73% of firms with 500 or more. Health and welfare (sector Q) is at 28%, health care (SBI 86) at 26%.

## Key data

**AI use by Dutch firms with 10 or more employed persons** (table 3.4)

| Year | Use AI | Considered, not used |
| --- | ---: | ---: |
| 2020 | 13% | – |
| 2021 | 13% | 5% |
| 2022 | 16% | 5% |
| 2023 | 14% | 6% |
| 2024 | 23% | 9% |
| 2025 (provisional) | **33%** | 10% |

2022–2024 are labelled "nader voorlopig" (revised provisional).

**By size class, 2025** (StatLine 86118NED): 10–20 persons 25% · 20–50 33% · 50–100 43% · 100–250 52% · 250–500 61% · **500+ 73%**.

**By sector, 2025** (StatLine 86120NED; total covers sectors C–N and Q): information and communication 70% · insurers 75% · banks 50% · specialist business services 55% · manufacturing 29% · trade 30% · **health and welfare 28%**, of which **health care 26%** and care and welfare 29% · construction 21% · transport 20% · hotels and restaurants 16%.

## Method and definitions

- **Unit.** The enterprise, with 10 or more "werkzame personen" (persons employed). Each firm counts once, whatever its size.
- **What counts as use.** At least one of eight technologies: text mining, speech recognition, natural language generation, image recognition, generating images, video or sound, machine learning, AI-based robotic process automation, and service robots or autonomous vehicles. The eighth, image, video and sound generation, was added in 2025 (pop-up definition on the chapter page).
- **Status.** 2025 figures are provisional. StatLine's 2025 tables note that *"vanaf dit jaar is de wegingsmethode verbeterd, waardoor de cijfers licht kunnen verschillen ten opzichte van eerdere jaren"* ("from this year the weighting method has been improved, so figures may differ slightly from earlier years").
- **Survey.** The chapter names no survey and gives no sample size. Its 2021–2025 totals equal [[2026-11-04-eurostat-use-of-ai-in-enterprises|Eurostat's Netherlands series]] for the same indicator to the rounded percent (13.1, 14.1, 23.06, 33.21). This is therefore the Dutch part of the EU survey on ICT usage in enterprises.

## Scope and reliability

- **Official statistics.** A national statistical office, a fixed list of technologies and a survey harmonised across the EU. Executive surveys of large firms sit at the other end of the scale.
- **The 23% to 33% step is not fully like-for-like.** Three things changed in 2025: an eighth technology was added, CBS changed its weighting, and Eurostat flags the Dutch 2025 figure as a break in series. The chapter mentions only the first.
- **Firm-weighted.** Small firms dominate the count, so the total sits far below the rate for large firms (73% at 500+).
- **Breadth only.** "Use" means at least one technology in use. The survey says nothing about how deeply, how widely within the firm, or with what result.
- **Sector coverage.** CBS's total includes financial services and health care. Eurostat's EU total excludes both. The Dutch figure in Eurostat's tables uses Eurostat's own scope.

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`**: an official, repeated scan of how many Dutch firms use which AI technologies, by sector and size.
- **`contextual/external-triggers`**: a third of Dutch firms with 10 or more employed persons, and nearly three quarters of the largest, already use some AI. That is the competitive field a firm operates in, whether or not it adopts AI itself.

## How it connects

- [[enterprise-ai-adoption]] and the thread [[ai-maturity-measurement-comparison]]: an official firm-level adoption figure for the Netherlands.
- [[2026-11-04-eurostat-use-of-ai-in-enterprises|Eurostat, Use of AI in enterprises]]: the EU-wide version of the same survey, 19.95% in 2025.
- [[2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening|RaboResearch (Rabobank)]]: AI use by business function in Dutch IT and business services, from the same CBS survey.
- [[2026-10-26-rendtorff-smith-chin-bcg-creating-ai-value-adoption|Rendtorff-Smith (OECD)]]: the gap between big and small firms in official statistics.
- [[2026-07-01-stanford-del-adoption-monitor|Stanford DEL Adoption Monitor]]: 69% of firms in an executive survey of four high-income countries.
- [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs|Hatzius (Goldman Sachs)]]: the US Census firm figure and its wording change.
- [[2026-03-16-mxi-ai-monitor-ziekenhuizen-2026|M&I AI Monitor Ziekenhuizen 2026]]: hospitals are large health-care organisations; CBS gives 26% for health-care firms as a whole.

## What was actually ingested

The full chapter as served on 7 November 2026: four sections and four tables (internet access, telework, e-commerce, AI), and the pop-up that defines the eight AI technologies. The report's erratum page corrects chapters 2 and 7 only. The size-class and sector split are not in the chapter. They were read from CBS StatLine tables 86118NED and 86120NED (published 12 December 2025) through the CBS open-data API and are appended to the raw file.

## Linked entities and concepts

- [[enterprise-ai-adoption]]: concept.

**Dangling** (single-source mention, deferred): Centraal Bureau voor de Statistiek (CBS; also named in the body of the RaboResearch source), Eurostat.
