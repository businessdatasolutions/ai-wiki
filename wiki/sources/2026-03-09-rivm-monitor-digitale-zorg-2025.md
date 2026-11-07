---
type: source
kind: report
title: "Monitor Digitale Zorg 2025: Stand van zaken van de digitale zorg in Nederland"
author: ["E.E. Alblas", "J.J. Keuper", "M. Vugts", "L. van Tuyl", "M. Villalobos", "K.E.F. Leenaars"]
publisher: "RIVM (Rijksinstituut voor Volksgezondheid en Milieu), with Nivel and NeLL"
url: "https://www.rivm.nl/bibliotheek/rapporten/2025-0176.pdf"
date_published: 2026-03-09
date_ingested: 2026-11-07
length: "70 pages (read: summaries pp. 3–10, chapter 1 including definitions pp. 11–13, chapter 2 pp. 15–18 with the AI section §2.2 on pp. 16–17, §7.1–7.1.1 p. 45, method appendix pp. 53–59; the rest searched for AI mentions only)"
raw: "../../raw/reports/2026-03-09-rivm-monitor-digitale-zorg-2025.md"
tags: [rivm, nivel, nell, knmg, monitor-digitale-zorg, netherlands, health-care, digital-health, ai-use-by-clinicians, doctors, nurses, gps, medical-specialists, self-report, panel-survey, question-wording, series-break, government-statistics]
dynamic_capabilities:
  - digital-sensing/digital-scouting
relationships:
  - type: supports
    target: 2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs
    via: "an adoption figure that moves with the question: Dutch doctors' AI use went from 13% (2024) to 53% (2025) after answer options were added or reworded, and RIVM says the years cannot be compared well; Hatzius describes the US Census firm figure doubling after its wording changed"
    confidence: 0.75
  - type: supports
    target: 2026-03-16-mxi-ai-monitor-ziekenhuizen-2026
    via: "AI uptake in Dutch health care, measured on different units: 53% of doctors and 41% of nurses use at least one AI application (RIVM, individuals), against 90% of hospitals using generative AI (M&I, organisations); RIVM cites the 2025 AI Monitor as consistent with its finding"
    confidence: 0.7
---

# Monitor Digitale Zorg 2025 (RIVM, Nivel, NeLL)

## TL;DR

The annual Dutch government monitor of digital care, commissioned by the Ministry of Health (VWS) and run since 2021 by RIVM, Nivel and NeLL. It surveys doctors, nurses and the public through four national panels. Only its AI section is summarised here.

1. **Doctors.** 53% of doctors (GPs, medical specialists and social physicians) say they use one or more AI applications in 2025 (p. 16).
2. **Nurses.** 41% of nurses do. They were asked for the first time in 2025 (p. 16).
3. **The jump is not comparable.** In 2024, 13% of doctors used AI. RIVM writes that in 2025 *"enkele antwoordopties toegevoegd of anders verwoord, waardoor er geen goede vergelijking tussen beide jaren te maken is"* ("some answer options were added or reworded, so the two years cannot be compared well", p. 16). The section heading and the summary still say AI use by doctors rose.
4. **What they use it for.** Looking up information is the most common use in all four groups. Administration follows, including speech-driven reporting; then education and training. GPs also use AI for triage (pp. 16–17).
5. **Context.** The report sets this next to the 2025 AI Monitor Ziekenhuizen, in which three quarters of hospitals used generative AI (p. 45).

## Key data

| Measure | 2024 | 2025 | Page |
| --- | ---: | ---: | --- |
| Doctors using one or more AI applications | 13% | **53%** | p. 16 |
| Nurses using one or more AI applications | not asked | **41%** | p. 16 |
| Doctors analysed (KNMG panel): GPs 162 · medical specialists 164 · social physicians 63 | 345 | 389 | pp. 54–55 |
| Nurses analysed (Nivel panel) | 579 | 582 | pp. 54–55 |

**Top three AI uses among AI users, 2025** (Figure 2, p. 17; weighted shares, counts as printed):

| Group (AI users) | 1st | 2nd | 3rd |
| --- | --- | --- | --- |
| Nurses (n=238–239) | Information lookup (n=159) | Education or training (n=71) | Administration (n=62) |
| GPs (n=92–99) | Information lookup (n=74) | Administration (n=33) | Triage (n=30) |
| Medical specialists (n=83–85) | Information lookup (n=65) | Education or training (n=21) | Administration (n=17) |
| Social physicians (n=32–34) | Information lookup (n=28) | Education or training (n=18) | Administration (n=13) |

Information lookup reaches roughly two-thirds to four-fifths of AI users in each group (weighted, read from the chart).

## Method and definitions

- **Panels and fieldwork.** Questionnaires through four panels, fielded April to July 2025, about the previous twelve months (p. 53). Doctors come from the KNMG Artsenpanel; nurses from the Nivel Panel Verpleging & Verzorging.
- **Who counts as what.** "Artsen" (doctors) means GPs, medical specialists and social physicians together (p. 13). "Medical specialists" includes hospital specialists but also, for example, elderly-care physicians and addiction physicians. "Nurses" includes carers, nurse specialists and practice nurses in elderly care, district nursing, hospitals, GP practices, mental health and disability care (p. 13). The figures are therefore not hospital figures.
- **What counts as AI use.** Since 2024 doctors are asked whether they use certain AI applications. The percentage is the share of respondents who ticked at least one option, excluding "ik weet het niet" (I don't know) (footnote f, p. 16). RIVM's examples of information lookup include *"zoekmachines die AI gebruiken"* (search engines that use AI).
- **Response.** For doctors, 2,284 were invited and 404 returned the questionnaire; for nurses, 2,257 and 599 (Table 1, p. 54). That is about 18% and 27%, a calculation not made in the report.
- **Weighting.** Doctors are weighted by specialism and nurses by sector. Weights apply only to questions asked of all respondents (p. 58).

## Scope and reliability

- **The 13% to 53% jump crosses a change in the question.** RIVM itself says the two years cannot be compared well. It still headlines the rise. Treat 53% as a 2025 level, not as a growth rate.
- **Low bar.** Ticking one application counts as use. That includes looking things up with an AI-assisted search engine. The question says nothing about frequency, depth or scale.
- **Self-report from volunteer panels** with response rates around a fifth to a quarter. Weighting corrects for specialism and sector, not for interest in digital care.
- **Not hospitals.** Doctors and nurses from all settings are pooled. The figure measures individual clinicians, not organisations.
- **Do not mix the 53%s.** The doctors' 53% is unrelated to the 53% small-scale value and the 53% high-risk-AI value in [[2026-03-16-mxi-ai-monitor-ziekenhuizen-2026|the M&I AI Monitor Ziekenhuizen 2026]].
- A small error in the source: Table 3 (p. 55) gives the average age of all providers as 28, while every group averages 53 to 57.

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`**: a standing national scan of how Dutch clinicians take up digital tools, now including AI, which hospitals and policymakers can use to read the field.

## How it connects

- [[enterprise-ai-adoption]] and the thread [[ai-maturity-measurement-comparison]]: an individual-level adoption measure in Dutch health care, with the instrument change stated by the publisher.
- [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs|Hatzius (Goldman Sachs)]]: the US Census firm-adoption figure also jumped after a wording change.
- [[2026-07-01-stanford-del-adoption-monitor|Stanford DEL Adoption Monitor]]: survey adoption figures that differ by sample, population and elicitation.
- [[2026-03-16-mxi-ai-monitor-ziekenhuizen-2026|M&I AI Monitor Ziekenhuizen 2026]]: hospital-level breadth, scale and impact in the same country and year.
- [[2026-02-10-cbs-ict-gebruik-bij-bedrijven-2025|CBS, ICT-gebruik bij bedrijven 2025]]: firm-level AI use, including the health-care sector.
- [[ai-in-health-care]]: the concept page that sets the health-care sources in this wiki side by side.

## What was actually ingested

The public and English summaries, the Dutch summary, chapter 1 (aims and definitions), chapter 2 up to §2.3.1, §7.1 and §7.1.1, and the method appendix with its respondent tables. Figure 2 was read from the page image. Chapters 3 to 6 (hybrid care, societal challenges, differences by age and education, users versus non-users) were searched for AI and contain no further AI results. They are not summarised here.

## Linked entities and concepts

- [[enterprise-ai-adoption]]: concept.

**Dangling** (single-source mention, deferred): RIVM, Nivel, NeLL (affiliated with LUMC), KNMG, Ministry of VWS, E.E. Alblas, J.J. Keuper, M. Vugts, L. van Tuyl, M. Villalobos, K.E.F. Leenaars.
