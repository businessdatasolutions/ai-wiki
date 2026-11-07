---
type: source
kind: article
title: "AMA 2026 Physician Survey on Augmented Intelligence (read via secondary coverage)"
author: ["American Medical Association"]
publisher: "American Medical Association, Center for Digital Health and AI; read via The ASCO Post (19 March 2026) and Healthcare Innovation (15 March 2026)"
url: "https://www.ama-assn.org/practice-management/digital-health/more-80-physicians-use-ai-professionally-ama-survey"
date_published: 2026-03-12
date_ingested: 2026-11-07
length: "two news articles (~720 and ~440 words), read in full; the AMA's own article, press release and report PDF were not accessible (HTTP 403)"
raw: "../../raw/articles/2026-03-19-ascopost-ama-survey-physician-ai-adoption.md"
tags: [american-medical-association, physicians, physician-survey, ai-adoption, augmented-intelligence, clinical-documentation, burnout, skill-loss, patient-chatbots, ai-training, liability, united-states, healthcare, secondary-coverage]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: 2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care
    via: "clinicians' attitudes to AI: Philips's Future Health Index, as Peron cites it, has 79% of healthcare professionals optimistic; the AMA has 76% of US physicians saying AI enhances their ability to care for patients"
    confidence: 0.65
  - type: supports
    target: 2026-07-14-keneally-bcg-so-what-llm-or-md-patient-journey
    via: "patients using general-purpose AI for health questions: BCG's consumer survey as Keneally describes it, and the AMA physicians' estimates of their own patients' chatbot use"
    confidence: 0.6
---

# AMA 2026 Physician Survey on Augmented Intelligence (secondary coverage)

## TL;DR

The American Medical Association's third survey of US physicians on AI. The AMA's own pages were blocked to this fetch, so this page rests on two news reports of the AMA's release. Five points:

1. **81% of physicians use AI in their practice**, against **38% in 2023** (ASCO Post; Healthcare Innovation). The AMA's headline says "use AI professionally."
2. **More uses per physician.** The average number of AI use cases rose from 1.1 (2023) to 2.3 (2026) (Healthcare Innovation). The top use is summarising medical research and standards of care, at **39%**, up from 13% in 2024 (ASCO Post).
3. **Optimism with conditions.** 76% say AI enhances their ability to care for patients; about 40% are as concerned as they are excited; 70% see AI as a way to automate tasks that drive burnout (ASCO Post).
4. **Skill loss is the big worry.** **88%** are concerned about potential skill loss, mostly for early-career physicians (ASCO Post; Healthcare Innovation).
5. **Training lags use.** 92% want more education and training on AI; 27% have had none from any source (ASCO Post).

## Key data

| Measure | 2023 | 2026 | Reported by |
| --- | ---: | ---: | --- |
| Physicians using AI in their practice | 38% | **81%** | ASCO Post, HCI |
| Average AI use cases per physician | 1.1 | 2.3 | HCI |
| Use AI to summarise research and standards of care | 13% (2024) | 39% | ASCO Post |
| AI enhances ability to care for patients | n/a | 76% | ASCO Post |
| Equally excited and concerned | n/a | ~40% | ASCO Post, HCI |
| Concerned about potential skill loss | n/a | 88% | ASCO Post, HCI |
| Want more AI education and training / had none | n/a | 92% / 27% | ASCO Post |
| None of their patients disclosed chatbot use / at least half their patients use them | n/a | 29% / 30% | ASCO Post |
| Want to be involved in AI implementation decisions | n/a | 55% (ASCO Post); 85% "consulted or directly involved" (HCI) | both |

The 2024 wave (fielded November 2024) reported 66% using AI, per Medical Economics (19 February 2025). That article was checked but not acquired.

## Method and definitions

- **Sample.** 1,692 physicians across specialties, practice settings and career stages, surveyed from 15 January to 2 February 2026; voluntary and confidential (ASCO Post).
- **Earlier waves.** 2023 (n = 1,081) and 2024 (n = 1,183) (ASCO Post).
- **Respondents.** Median 20 years in practice, 35 hours a week of direct patient care, practices with a median of 26 physicians; 38% in group practices, 24% in hospitals; 23% practice owners; 25% primary care (ASCO Post).
- **What counts as "use."** Not stated in the coverage. The two articles say "using AI in their practices" and "use AI professionally." The question wording, its denominator and any weighting could not be checked.
- **New topics in 2026:** patient-facing chatbots and other patient-directed uses of AI (ASCO Post).
- **Sponsor.** The AMA's Center for Digital Health and AI.

## Scope and reliability

- **Secondary only.** The AMA article cited in the Dutch report, the AMA press release and the report PDF on ama-assn.org all returned HTTP 403 (a Cloudflare challenge) to curl and WebFetch. The figures here are as two trade outlets report them. The publication date (12 March 2026) comes from search-result metadata for the AMA pages, not from the pages themselves.
- **Self-selected sample.** Participation was voluntary. The coverage gives no response rate and no weighting.
- **The two outlets differ.** On involvement in AI decisions, ASCO Post reports 55% and Healthcare Innovation 85% "consulted or directly involved"; they may measure different answers. On skill loss, ASCO Post says the concern is *about* early-career physicians, Healthcare Innovation that it is highest *among* physicians with 10 years or less in practice. Healthcare Innovation's first sentence says "Eighty percent," its body 81%.
- **Trend across waves.** 38% (2023) → 66% (2024, per Medical Economics) → 81% (2026). Whether the question stayed the same across waves is not stated.

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`**: an annual scan of how far, and for what, US physicians use AI.
- **`digital-transforming/improving-digital-maturity`**: the workforce side of maturity. 92% of physicians want more AI training and 27% have had none, while 81% already use AI.

## How it connects

- [[enterprise-ai-adoption]] — individual-level adoption among physicians: broad (81%) and mostly for documentation and summarising.
- [[ai-maturity-measurement-comparison]] — another "any use" figure, here counted per physician rather than per organisation.
- [[ai-deskilling]] — 88% concern about skill loss, focused on early-career physicians.
- [[2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care|Peron (Philips) on MIT SMR]] cites Philips's Future Health Index: 79% of healthcare professionals optimistic about AI. The AMA's 76% is a US-physician measure of a similar attitude.
- [[2026-07-14-keneally-bcg-so-what-llm-or-md-patient-journey|Keneally (BCG)]] on patients using LLMs as a first step in care. The AMA asks the physicians' side: 30% believe at least half their patients use AI chatbots.
- [[2026-07-01-stanford-del-adoption-monitor|Stanford DEL Adoption Monitor]] — adoption figures depend on the instrument; the same caution applies to "81% use AI."
- [[ai-in-health-care]]: the concept page that sets the health-care sources in this wiki side by side.

## What was actually ingested

Two full news articles: The ASCO Post (19 March 2026; methods, respondent profile and most figures) and Healthcare Innovation by David Raths (15 March 2026; use cases per physician, involvement, liability). Raw files: `raw/articles/2026-03-19-ascopost-ama-survey-physician-ai-adoption.md` and `raw/articles/2026-03-15-raths-hci-ama-survey-ai-usage-doubles.md`. Not ingested: the AMA's article, press release and PDF report (blocked).

## Linked entities and concepts

- [[enterprise-ai-adoption]], [[ai-deskilling]] — concepts.

**Dangling** (single-source mention, deferred): American Medical Association (Center for Digital Health and AI); John Whyte (AMA CEO, quoted); David Raths (Healthcare Innovation); The ASCO Post.
