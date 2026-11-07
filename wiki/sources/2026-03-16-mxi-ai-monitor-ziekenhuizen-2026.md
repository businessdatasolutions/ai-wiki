---
type: source
kind: report
title: "AI Monitor Ziekenhuizen 2026: Wat is de stand van zaken van AI bij Nederlandse ziekenhuizen?"
author: ["M&I/Partners"]
publisher: "M&I/Partners"
url: "https://mxi.nl/uploads/files/publication/ai-monitor-ziekenhuizen-2026.pdf"
date_published: 2026-03-16
date_ingested: 2026-11-07
length: "46 slides (read in full, including the two interviews on pp. 40–44; chart pages 11–12, 25–28, 30–32 and 35–38 checked as images against the pdftotext extract)"
raw: "../../raw/reports/2026-03-16-mxi-ai-monitor-ziekenhuizen-2026.md"
tags: [mxi, m-and-i-partners, ai-monitor-ziekenhuizen, netherlands, dutch-hospitals, santeon, health-care, hospital-ai-adoption, ai-scale, innovation-funnel, pilot-to-scale, generative-ai, ai-agents, ambient-listening, speech-driven-reporting, quintuple-aim, realised-impact, ai-readiness, ai-governance, ai-board, ai-act, high-risk-ai, self-assessment, survey-errata, living-series]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/redesigning-internal-structures
  - contextual/internal-barriers
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-04-28-mit-sloan-ai-maturity
    via: "most AI work sits before scale: in Dutch hospitals 8% report AI 'op grote schaal' and the average hospital has 1 of 18 applications in scaling; MIT CISR's Stage 2 (pilots) to Stage 3 (scaled) step across enterprises"
    confidence: 0.65
  - type: supports
    target: 2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals
    via: "hospital administration as the main site of AI: administration and billing is the most common AI process in Dutch hospitals (80%, +32 points); Luminai builds agents for US hospital back-office work"
    confidence: 0.6
  - type: supports
    target: 2025-12-11-deloitte-2026-global-health-care-outlook
    via: "breadth versus depth in health systems: 90% of Dutch hospitals use generative AI while 8% apply AI at large scale (M&I); Deloitte surveys 180 health-system executives in six countries including the Netherlands on scaled and organisation-wide AI use"
    confidence: 0.65
  - type: supports
    target: 2025-05-05-poon-jamia-health-system-ai-adoption
    via: "the gap between starting and full use, per use case: speech-driven reporting started in 69% of Dutch hospitals with 21% of intended clinicians active (M&I); Poon et al. measure any versus full deployment per use case in 43 US health systems"
    confidence: 0.65
  - type: supports
    target: 2025-07-15-european-commission-ai-deployment-healthcare-final-report
    via: "hospital AI deployment measured by survey in Europe; the EC study warns that surveys may overstate deployment, and M&I is a self-assessment by hospital IT and AI leads"
    confidence: 0.6
---

# AI Monitor Ziekenhuizen 2026 (M&I/Partners)

## TL;DR

The eighth annual survey of AI in Dutch hospitals by M&I/Partners, an ICT consultancy. A record 52 hospitals took part (73% of the total), including all seven Santeon hospitals. Five findings:

1. **Breadth is high.** 90% of hospitals use generative AI, up 15 points on 2025. Traditional AI holds at 83% (p. 30).
2. **Scale is rare.** Asked *"Op welke schaal wordt AI binnen uw ziekenhuis toegepast?"* ("At what scale is AI applied in your hospital?"), 8% answer large scale and 0% very large scale. The middle grew: "gemiddeld" (average) went from 33% to 46% (p. 25).
3. **Few applications get past the pilot.** Of the average hospital's 18 AI applications, 1 is in implementation and 1 in scaling (p. 26).
4. **Use is thin even where it started.** 69% have started with speech-driven reporting, but on average 21% of the intended clinicians use it actively (p. 31). For AI agents, 0% are scaling (p. 32).
5. **Expectations outrun results.** On the new question about realised impact over the past three years, 55% report a positive effect on staff experience, and 47% report that AI raised care costs. For four of the five quintuple-aim goals, "neutral" is the most common answer; on costs only narrowly (about 49% against 47%, read from the chart, p. 37).

The report has an error that the press repeated: its conclusion gives 53% small-scale use, which is the 2025 value. The 2026 value is 42% (see *Scope and reliability*).

## Key data

| Measure (question, unit) | 2025 | 2026 | n (2026) | Page |
| --- | ---: | ---: | --- | --- |
| Uses generative AI | 75% | **90%** | 52 hospitals | p. 30 |
| Scale: very small or none | 13% | 4% | 52 (2025: 40) | p. 25 |
| Scale: small ("kleine schaal") | 53% | **42%** | 52 | p. 25 |
| Scale: average ("gemiddeld") | 33% | 46% | 52 | p. 25 |
| Scale: large ("grote schaal") | 3% | **8%** | 52 | p. 25 |
| Scale: very large | 0% | **0%** | 52 | p. 25 |
| AI applications per hospital in funnel (mean): idea 8 · purchase/development 3 · pilot 3 · implementation 1 · scaling 1 · operations 2 | – | **18** | 51 | p. 26 |
| Speech-driven reporting started (pilot 42% + implementation 10% + scaling 17%) | – | **69%** | 52 | p. 31 |
| Share of intended clinicians actively using speech-driven reporting (mean) | – | **21%** | 34 | p. 31 |
| AI agents: none 38% · exploring 48% · purchase 2% · pilot 10% · implementation 4% · scaling **0%** · operations 2% | – | – | 52 | p. 32 |
| Has an AI vision and strategy | 28% | 48% | 52 | p. 15 |
| Has adopted AI policy | 50% | 76% | 52 | p. 16 |
| Uses high-risk AI systems (EU AI Act) | – | 53% | 51 | p. 33 |
| AI process: administration and billing (incl. reporting) · diagnostics · communication | – | 80% · 71% · 65% | 52 | p. 27 |
| Driver: reduce workload · improve quality of care · stay innovative · lower care costs | – | 100% · **88%** · 67% · 25% | 52 | p. 35 |
| Expected impact, next 5 years: positive on staff · on patients · negative on costs | – | 89% · 81% · 46% | 51 respondents | p. 36 |
| Realised impact, past 3 years: positive on staff · negative on costs ("hogere zorgkosten") | – | **55% · 47%** | 51 respondents | p. 37 |

Radiology still has the most important implementations (41%, down 21 points, p. 28). In speech-driven reporting, Autoscriber leads with 38% of hospitals; [[Microsoft]] Dragon Copilot has 8% (p. 31).

## Method and definitions

- **Who answered.** 56 respondents from 52 hospitals (22 general, 26 top-clinical, 4 university): 18 CIOs, 8 AI programme or project leads, 8 clinical informaticists, 3 CDOs or data managers, 3 CMIOs, 2 clinical physicists and 14 others (p. 12). CIOs are the largest group, not a majority.
- **Who took part.** The list on p. 11 includes all seven Santeon hospitals: Canisius Wilhelmina Ziekenhuis, Catharina Ziekenhuis, Maasstad Ziekenhuis, Martini Ziekenhuis, Medisch Spectrum Twente, OLVG and St. Antonius Ziekenhuis ("Antonius" is a separate entry). There are no results per hospital.
- **When.** The introduction dates the fieldwork *"januari tot en met februari 2025"* (p. 4). That must be 2026: the 2025 edition was fielded in February and March 2025, and every chart compares 2026 with 2025.
- **What counts as scale.** Five self-assessed categories, not defined in the 2026 report. The 2025 edition described small scale as *"bijvoorbeeld op specifieke afdelingen of als pilot"* ("for example in specific departments or as a pilot") and added "gemiddeld" that year. The funnel phases come from the *Tool Handelingsruimte Waardevolle AI*.
- **Units.** Changes marked "%" are percentage points. The base varies by question (see the n column).
- **Sponsor.** Self-published by M&I/Partners, an independent ICT consultancy of about 100 staff that advises health care and government (p. 46). The report ends with an offer of advice (p. 45).

## Scope and reliability

- **The 53% error.** The p. 25 chart shows small-scale use at 53% in 2025 and 42% in 2026. The same page's text (*"kleinschalige inzet substantieel (53%; -11% t.o.v. vorig jaar)"*) and the conclusion on p. 6 (*"Bij 53% blijft AI nog kleinschalig"*, "for 53%, AI remains small-scale") present the 2025 value as current. 53 minus 11 is 42, and 4 + 42 + 46 + 8 = 100. The 2025 edition confirms 53% for 2025. M&I's landing page and Consultancy.nl (14 April 2026) repeat 53%; Consultancy.nl's 53%, 46% and 8% add up to 107%. The p. 25 text also gives *"+23%"* for average scale, where the chart shows +13. The 8% and 0% agree everywhere.
- **Other 53%s.** 53% is also the share of hospitals using high-risk AI (p. 33) and of Dutch doctors using AI in [[2026-03-09-rivm-monitor-digitale-zorg-2025|the RIVM Monitor Digitale Zorg 2025]].
- **Self-report.** One or two respondents per hospital, mostly in IT and AI roles, judge their own hospital. Nothing is verified.
- **A changing panel.** 46 hospitals took part in 2025 (40 answered the scale question) and 52 in 2026. Part of any year-on-year shift may come from who took part.
- **"Neutral in most hospitals" needs a qualifier.** The p. 37 text calls impact neutral on *"alle vijf de aims"* (all five aims) in most hospitals. For staff experience, though, positive (55%) outnumbers neutral (about 40%, read from the chart). The "47% higher costs" is the share of respondents rating the realised impact on lower care costs as negative.
- **The agent bars add up to 104%** (p. 32), so some hospitals appear in more than one phase. One hospital (2%) has an agent in operational management, though none is scaling.
- **No quality or patient-safety domain.** Neither the process list (p. 27) nor the department list (p. 28) has one. Quality appears as a driver (88%, p. 35) and once as an AI-board role ("manager Kwaliteit", p. 21). The conclusion's agent use case *"(semi-)automatisch afhandelen van meldingen"* is spelled out on p. 32 as *"(Semi-)automatische screening en afhandeling mails en storingen bij medische techniek"*: e-mails and equipment malfunctions in medical technology. Patient-safety incident reports (VIM) appear nowhere in the report.

## Dynamic-capabilities reading

- **`digital-transforming/improving-digital-maturity`**: strategy (48%), policy (76%), AI literacy and a seven-element readiness score are the sector's own maturity yardstick.
- **`digital-seizing/balancing-digital-portfolios`**: the funnel (18 applications, 1 scaling) and the scale question track how a portfolio of AI applications moves from pilot to scale.
- **`digital-transforming/redesigning-internal-structures`**: 60% have an AI board, and AI is moving to a central position (63 to 68 on a 0–100 scale) and into the line organisation (52 to 59) (p. 23).
- **`contextual/internal-barriers`**: financial room (45% not in order), staff awareness (42%) and transformation capacity (39%) are the readiness gaps most often named (p. 38).
- **`contextual/external-triggers`**: the AI Act's high-risk obligations from 1 August 2026 reach the 53% of hospitals using high-risk AI (p. 33); staff shortages and financial pressure frame the introduction (p. 4).

## How it connects

- [[enterprise-ai-adoption]] and the thread [[ai-maturity-measurement-comparison]]: breadth (90%) and scale (8%) measured in one sector.
- [[2026-04-28-mit-sloan-ai-maturity|MIT CISR's four stages]]: the same pilot-to-scale step, here in one sector's innovation funnel.
- [[2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals|Dinakaran / Luminai]]: hospital administration as the place where AI is used most.
- [[2026-03-09-rivm-monitor-digitale-zorg-2025|RIVM Monitor Digitale Zorg 2025]]: AI use by Dutch doctors and nurses; it cites the 2025 edition of this monitor.
- [[2026-02-10-cbs-ict-gebruik-bij-bedrijven-2025|CBS, ICT-gebruik bij bedrijven 2025]]: official firm statistics, including the health-care sector (26%).
- [[2026-04-30-ai-index-report-2026|AI Index 2026]]: one of its top takeaways is that 5% of 500+ clinical AI studies use real clinical data.
- [[2026-10-20-parikh-google-cloud-hippocratic-ai-voice-agents-healthcare|Hippocratic AI]]: voice agents for patient calls, one of the monitor's agent use cases.
- [[2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care|Peron / Philips]]: radiology as the home of medical AI.
- [[generative-ai]], [[ai-agents]], [[responsible-ai]] (AI policy, AI boards and high-risk AI under the AI Act).
- [[2025-12-11-deloitte-2026-global-health-care-outlook|Deloitte 2026 Global Health Care Outlook]]: health-system executives in six countries, the Netherlands among them, on scaled and organisation-wide AI use (2% organisation-wide).
- [[2025-05-05-poon-jamia-health-system-ai-adoption|Poon et al., JAMIA 2025]]: any versus full deployment per use case in 43 US health systems, the same gap between starting and full use.
- [[2025-07-15-european-commission-ai-deployment-healthcare-final-report|European Commission study on AI deployment in healthcare]]: a European study that warns surveys may overstate hospital AI deployment; the M&I monitor is a self-assessment.
- [[ai-in-health-care]]: the concept page that sets the health-care sources in this wiki side by side.

## What was actually ingested

The full 46-slide PDF, including the interviews with Máxima MC and UMC Utrecht (pp. 40–44). Chart values were read from the page images. The 2025 edition was opened only for its scale page and fieldwork dates. The Consultancy.nl article of 14 April 2026 was read only to see whether the press repeated the 53%.

## Linked entities and concepts

- [[Microsoft]]: Dragon Copilot is used for speech-driven reporting in 8% of hospitals (p. 31).
- [[enterprise-ai-adoption]], [[generative-ai]], [[ai-agents]], [[responsible-ai]]: concepts.

**Dangling** (single-source mention, deferred): M&I/Partners (publisher), Wouter Gude, Laureanne van Dijk, Jordan Vasseur, Jeroen van Oostrum (M&I contacts), Santeon, Carlijn de Ruijter (Máxima MC), Roëlle de Koning and Firdaus Mohamed Hoesein (UMC Utrecht), Autoscriber, OurMind, NVZ, UMCNL, Consultancy.nl.
