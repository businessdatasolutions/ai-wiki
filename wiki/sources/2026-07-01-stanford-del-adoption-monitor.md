---
type: source
kind: dashboard
title: "Adoption Monitor (The AI Economic Indicators)"
author: ["Stanford Digital Economy Lab"]
publisher: "Stanford Digital Economy Lab — The AI Economic Indicators"
url: "https://digitaleconomy.stanford.edu/project/indicators/adoptionmonitor/"
date_published: 2026-07-01
date_accessed: 2026-11-04
date_ingested: 2026-11-04
length: "one dashboard page (~800 words of prose + 4 charts, all chart data captured; snapshot of the 1 July 2026 update, individual surveys through June 2026, firm survey fielded November 2025 to January 2026)"
raw: "../../raw/dashboards/2026-07-01-stanford-del-adoption-monitor.md"
tags: [stanford-digital-economy-lab, ai-economic-indicators, adoption-monitor, dashboard, generative-ai-adoption, individual-adoption, firm-adoption, extensive-margin, intensive-margin, daily-use, work-use, bick-blandin-deming, gallup, pew-research, hartley, yotzov-barrero-bloom, nicholas-bloom, executive-survey, text-generation, robotics, autonomous-vehicles, survey-methodology, living-source]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - contextual/external-triggers
relationships:
  - type: published-by
    target: Stanford-Digital-Economy-Lab
  - type: supports
    target: 2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs
    via: "both treat adoption figures as products of their instrument: the Monitor shows three US work-use surveys diverging (one falling to 33%, two rising toward 50%) and attributes it to population and elicitation; Hatzius attributes the Census 10%→20% firm jump to a change of question wording"
    confidence: 0.75
  - type: supports
    target: 2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity
    via: "the Monitor's own caveat that 'widespread adoption is neither necessary nor sufficient for broader economic impact' is Frey's 'adoption for what?'"
    confidence: 0.7
  - type: contradicts
    target: 2026-04-30-ai-index-report-2026
    via: "level of US individual adoption: the Monitor's Bick-Blandin-Deming series puts US generative-AI use at 58–62% of adults (February–May 2026), while the AI Index ranks the US 24th at 28.3%. The gap turns on instrument, not date"
    confidence: 0.6
  - type: contradicts
    target: 2026-10-26-rendtorff-smith-chin-bcg-creating-ai-value-adoption
    via: "level of firm adoption: 69% of firms use some AI in the Monitor's executive survey of four high-income countries, against the OECD's 20% of firms in 2025. The gap turns on instrument and on which firms are counted: the OECD reports 50%+ for big firms and ~17% for small ones"
    confidence: 0.6
---

# Adoption Monitor — Stanford Digital Economy Lab

> How fast are individuals and firms adopting AI and related technologies? Many contemporary AI tools are low- or no-cost and available digitally, allowing for rapid adoption. Capturing a rich picture of AI adoption requires drawing on a number of sources. Here, we track individual- and firm-level trends across surveys and countries.
>
> While widespread adoption is neither necessary nor sufficient for broader economic impact, such adoption can indicate growing or shrinking importance of the technology in everyday and economic life.
>
> — the Monitor's own introduction

## TL;DR

The [[Stanford Digital Economy Lab]]'s adoption indicator. It collects published surveys rather than running its own: four US surveys of individuals and one executive survey of firms in four high-income countries. This snapshot is the 1 July 2026 update.

1. **Individual adoption keeps rising.** In the Bick, Blandin & Deming survey, **61.8%** of US adults used generative AI in May 2026, up from 44.6% in August 2024.
2. **Daily use is still low.** Nearly 90% of users use it weekly, but only **about a quarter use it daily**: 15.4% of all adults. The page calls the extensive margin (who uses it at all) and the intensive margin (how often) *"distinct."*
3. **Work-use surveys disagree.** Gallup (52%) and Bick, Blandin & Deming (45%) show work use still rising toward half of workers. Hartley et al. show it **falling**, from a 45.9% peak in June 2025 to 32.7% in June 2026.
4. **Firm adoption is high and expected to grow only a little.** In Yotzov, Barrero, Bloom et al. (NBER 34836), **68.6%** of firms use some AI technology, and 74.7% expect to within three years. On net, only about 6% of firms expect to move from no AI to some.
5. **Firms expect to use LLM text generation less.** Firms expect more use of every AI application except one: LLM text generation, which they expect to fall from 41.5% to 31.4% of firms. US firms expect it to fall from 53.5% to 28.8%. The page reports this without explaining it.
6. **US firms lead, but not by much.** Current adoption is 77.5% in the US, 71.3% in the UK, 64.7% in Germany and 59.3% in Australia. Executives expect the gaps to narrow.

## Key data (snapshot)

**Individuals, United States** (share of adults; work-use rows share of workers):

| Survey | Measure | Earliest | Latest |
| --- | --- | ---: | ---: |
| Bick, Blandin & Deming (BBD) | Any generative-AI use | 44.6% (Aug 2024) | **61.8%** (May 2026) |
| BBD | Used in the last week | 36.1% (Aug 2024) | 54.2% (May 2026) |
| BBD | Used every day | 12.1% (Aug 2024) | 15.4% (May 2026) |
| Pew Research Center | Ever used ChatGPT (only) | 18% (Jul 2023) | 44% (Feb 2026) |
| BBD | Any use at work | 33.3% (Aug 2024) | 45.2% (May 2026) |
| Gallup | Use at work a few times a year or more | 21% (May 2023) | **52%** (May 2026) |
| Gallup | … a few times a week or more | 11% (May 2023) | 30% (May 2026) |
| Gallup | … daily | 4% (May 2023) | 15% (May 2026) |
| Hartley, Jolevski, Melo et al. (HJMM) | Use at work | 30.1% (Dec 2024); peak 45.9% (Jun 2025) | **32.7%** (Jun 2026) |

**Firms, four countries** (share of firms, reported by senior executives November 2025 to January 2026; "expected" is in three years):

| Technology | All firms now → expected | U.S. | UK | Germany | Australia |
| --- | --- | --- | --- | --- | --- |
| Any AI technology | **68.6% → 74.7%** | 77.5 → 76.6 | 71.3 → 79.2 | 64.7 → 72.5 | 59.3 → 64.3 |
| Text generation using LLMs | **41.5% → 31.4%** | 53.5 → 28.8 | 33.5 → 29.8 | 46.0 → 34.3 | 30.1 → 30.9 |
| Data processing using ML | 28.1% → 40.1% | 36.9 → 45.9 | 33.2 → 43.5 | 21.3 → 36.6 | 22.1 → 31.6 |
| Visual content creation | 28.9% → 32.7% | 32.5 → 32.8 | 29.0 → 35.1 | 29.5 → 31.8 | 20.1 → 28.4 |
| Image processing using ML | 19.7% → 29.5% | 26.7 → 31.6 | 24.5 → 32.4 | 14.5 → 27.2 | 11.8 → 24.8 |
| Robotics | 9.1% → 20.7% | 13.0 → 22.3 | 13.6 → 21.3 | 3.9 → 18.4 | 7.5 → 23.6 |
| Autonomous vehicles | 3.5% → 15.9% | 4.5 → 14.5 | 3.0 → 13.6 | 2.6 → 17.5 | 6.6 → 20.3 |

## Method, as the page states it

- **Individuals.** Self-reported adoption from several surveys. They *"differ in their sample size, the populations they represent, and elicitation strategy."* Self-reports capture use people recognise as generative AI and *"might fail to capture embedded or ambient use, as well as integrated tools like spell checking and autocomplete."*
- **Firms.** Use of AI *in production*, reported by company leadership. The page argues this, and the cost firms take on, *"could provide a more reliable signal of the value of the technology for economically meaningful tasks,"* though adoption and diffusion frictions blur it.
- **Sources.** Bick, Blandin & Deming (2026, *Management Science*); Gallup's AI indicator (April 2026); Pew Research Center (2025); Hartley, Jolevski, Melo et al. (2026, SSRN); Yotzov, Barrero, Bloom et al. (2026, NBER Working Paper 34836). Nicholas Bloom, a co-author of the firm survey, is the page's featured affiliate.

## Reading the snapshot

**The corpus now holds adoption figures that differ by a factor of three or more, and the Monitor shows why.** It shows several instruments side by side, for individuals and for firms:

| Unit | Figure | Instrument | Source |
| --- | --- | --- | --- |
| US adults | 61.8% use generative AI (May 2026) | Household survey, any use | this Monitor (BBD) |
| US adults | 44% have used ChatGPT (Feb 2026) | Survey, one product only | this Monitor (Pew) |
| US population | 28.3%, 24th in the world | Cross-country diffusion measure; instrument not stated in the wiki's page | [[2026-04-30-ai-index-report-2026\|AI Index 2026]] |
| Firms, US/UK/DE/AU | 68.6% use some AI (late 2025) | Executive survey, use in production | this Monitor (Yotzov et al.) |
| Organisations, global | 88% (2025) | Organisational survey; the 2025 edition's 78% came from McKinsey's survey, counting use in at least one business function | [[2026-04-30-ai-index-report-2026\|AI Index 2026]] |
| Firms, OECD | 20% (2025); 50%+ of big firms, ~17% of small | Official firm statistics | [[2026-10-26-rendtorff-smith-chin-bcg-creating-ai-value-adoption\|Rendtorff-Smith (OECD) on BCG]] |
| Firms, US | ~10% (use in current production) → ~20% (any business function) | Census survey, before and after a wording change | [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs\|Hatzius (Goldman Sachs)]] |

None of these is wrong. They count different things: any use or production use, one product or all, firms weighted by number or by size, executives or employees. A figure about "AI adoption" should not be quoted without its instrument. The Monitor is the first source in the corpus to set them side by side for one country.

**The work-use split is the open question.** Two surveys show work use still rising and one shows it falling by a third in a year. The page reports this without resolving it. A self-report that falls while use spreads into tools people no longer call "AI" is one possible reading, and the page's own caveat about embedded use points that way. [[2026-06-10-anicich-brouwers-why-employees-arent-transparent-ai-usage|Anicich & Brouwers]] give another reason self-reports undercount: employees hide their AI use.

**The expected fall in text generation needs explaining.** US firms expect the share using LLM text generation to roughly halve while every other application grows. The page gives no reason. Possible readings: firms expect text generation to be absorbed into other tools or agents and no longer reported separately, or the question was read as stand-alone chatbot use. Treat it as unexplained.

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`**: a standing scan of how fast people and firms are taking up AI, across surveys and countries.
- **`contextual/external-triggers`**: individual adoption at 62% of US adults is a change in consumer behaviour that firms meet whether or not they adopt AI themselves. The firm survey describes the competitive field: a large majority of firms in four high-income economies already use some AI.

## How it connects

- [[enterprise-ai-adoption]] — the firm figures, and the spread of adoption figures across instruments.
- [[technology-adoption-theories]] — the extensive and intensive margins of adoption, measured separately.
- [[micro-productivity-trap]] — adoption without impact; the page's *"neither necessary nor sufficient."*

## Related in this wiki

- [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs|Hatzius (Goldman Sachs)]] — the Census wording change, the clearest case in the corpus of an adoption figure made by its question.
- [[2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity|Frey on Trumponomics]] — *"adoption for what?"*: high adoption for email does not drive growth.
- [[2026-04-30-ai-index-report-2026|AI Index 2026]] — a US adoption figure (28.3%) about half the Monitor's, and an organisational figure (88%) above it.
- [[2026-10-26-rendtorff-smith-chin-bcg-creating-ai-value-adoption|Rendtorff-Smith (OECD) on BCG]] — official firm adoption at 20%, and the gap by firm size.
- [[2026-06-10-anicich-brouwers-why-employees-arent-transparent-ai-usage|Anicich & Brouwers]] — why self-reported work use may undercount.
- [[2025-04-28-gillespie-kpmg-trust-attitudes-and-use-of-ai-2025|Gillespie et al. (KPMG)]] — a 47-country survey: 66% use AI intentionally on a regular basis, with emerging economies ahead.
- [[2026-10-21-stanford-del-canaries-dashboard|Canaries Dashboard]] and [[2026-10-21-stanford-del-transformation-tracker|Transformation Tracker]] — the other two indicators ingested with this one.

## What was actually ingested

The full page as served on 4 November 2026, and the full data of all four Flourish charts, saved as CSV beside the raw file. The page's last update is 1 July 2026; its firm summary was last updated 10 June 2026. The underlying surveys were not read; the figures are as the Monitor reports them. The Gallup frequency rows come from the frequency chart, which plots Gallup's three frequency thresholds separately.

## Linked entities and concepts

- [[Stanford Digital Economy Lab]] — publisher. Updated in this ingest.
- [[enterprise-ai-adoption]], [[technology-adoption-theories]], [[micro-productivity-trap]] — concepts, updated in this ingest.

**Dangling** (not in `author:`; deferred): Nicholas Bloom (featured affiliate, firm-survey co-author; also acknowledged in the Canaries paper), Alexander Bick, Adam Blandin, David Deming, Jonathan Hartley, Ivan Yotzov, Jose Maria Barrero, Gallup, Pew Research Center, Connacher Murphy.

## Scope and reliability

A curated collection of other people's surveys. Its value is the side-by-side view and the methodological notes, not new data. It does not reconcile the surveys that disagree. Two of the five sources are peer-reviewed or NBER working papers; Gallup and Pew are established pollsters; the Hartley et al. paper is an SSRN working paper. The firm survey covers four high-income countries and asks senior executives, who may report adoption more generously than official firm statistics do. This is a living source; the snapshot will move as new survey waves are released.
