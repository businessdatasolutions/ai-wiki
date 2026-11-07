---
type: source
kind: report
title: "Artificial intelligence is reshaping health systems: state of readiness across the WHO European Region"
author: ["Nicholas Letchford", "Hanna Dunning", "Nagui Salama", "Keyrellous Adib"]
publisher: "WHO Regional Office for Europe"
url: "https://www.who.int/europe/publications/i/item/WHO-EURO-2025-12707-52481-81028"
date_published: 2025-11-19
date_ingested: 2026-11-07
length: "76 pages (read: foreword, executive summary pp. ix–xvi, methods and limitations pp. 6–7, section 3.1 pp. 8–10; findings sections 3.2–3.6 searched for figures, not read in full)"
raw: "../../raw/reports/2025-11-19-who-europe-ai-health-systems-readiness.md"
tags: [who, who-europe, health-systems, national-ai-strategy, ai-governance, liability, legal-uncertainty, workforce-training, health-data-governance, eu, member-states, policy-readiness, ai-diagnostics, chatbots]
dynamic_capabilities:
  - digital-sensing/digital-scouting
relationships:
  - type: supports
    target: 2025-07-15-european-commission-ai-deployment-healthcare-final-report
    via: "legal uncertainty and liability as the leading European barrier: legal uncertainty is the top barrier for 43 of 50 states and 4 of 50 have AI liability standards for health; in the EC study 40% of hospital representatives cite unclear liability"
    confidence: 0.7
---

# Artificial intelligence is reshaping health systems: state of readiness across the WHO European Region — WHO/Europe, 2025

> This report presents the first assessment of AI integration into health systems across the whole of the WHO European Region, based on findings from the 2024–2025 survey on AI for health care.
>
> — the report's abstract

## TL;DR

WHO/Europe's first region-wide survey of national AI-for-health policy. The unit is the **country**, not the hospital: 50 of the 53 Member States answered, through government-nominated coordinators. It measures readiness (strategies, law, data governance, workforce), not how much AI hospitals use.

1. **Few health-specific AI strategies.** **4 of 50 (8%)** have published a national health-specific AI strategy; 7 (14%) are developing one. 33 (66%) have a cross-sector national AI strategy (pp. x, 9).
2. **Liability is unsettled.** **4 of 50 (8%)** have developed liability standards for AI in health; 3 (6%) have legal requirements for generative AI in health care (p. xii).
3. **Legal uncertainty is the top barrier** (43 of 50, 86%), then financial affordability (39 of 50, 78%). Clear liability rules are the most-cited enabler (46 of 50, 92%) (p. xv).
4. **Workforce training is thin.** 12 of 50 (24%) offer in-service AI training and 10 (20%) pre-service training; 21 (42%) have created new AI or data-science roles (p. xi).
5. **Use is reported at country level.** 32 of 50 (64%) report AI-assisted diagnostics and 25 (50%) chatbots for patient support. 26 (52%) have named priority areas for AI, and *"only just over half of these had allocated funding"* (p. xiv).

## Key data

| Measure | Member States | Share | Page |
| --- | ---: | ---: | --- |
| Responded (of 53) | 50 | 94% response rate | ix, 6 |
| Published national health-specific AI strategy | **4** | **8%** | x, 9 |
| … developing one | 7 | 14% | x, 9 |
| Health covered in a cross-sector AI strategy / AI in the digital health strategy / none | 16 / 17 / 6 | 32% / 34% / 12% | 9 |
| National cross-sector AI strategy | 33 | 66% | x, 10 |
| Engaged stakeholders on AI in health | 36 | 72% | xi |
| In-service AI training / pre-service AI training | 12 / 10 | 24% / 20% | xi |
| New professional roles for AI and data science | 21 | 42% | xi |
| Assessed legal gaps for AI in health | 23 | 46% | xii |
| Liability standards for AI in health | **4** | **8%** | xii |
| Legal requirements for generative AI in health care | 3 | 6% | xii |
| Regulatory agencies to assess and approve AI systems | 27 | 54% | xii |
| National health data strategy / health data hub | 33 / 33 | 66% / 66% | xiii |
| Guidance on secondary use of health data | 15 | 30% | xiii |
| Identified priority areas for AI in health | 26 | 52% | xiv |
| AI-assisted diagnostics in use / chatbots for patient support | 32 / 25 | 64% / 50% | xiv |
| Top barrier: legal uncertainty / second: financial affordability | 43 / 39 | 86% / 78% | xv |
| Enabler: liability rules / transparency and explainability guidance | 46 / 45 | 92% / 90% | xv |

## Method and definitions

- **Fieldwork.** June 2024 to March 2025, online or on paper, in English and Russian (p. 6).
- **Who answered.** Each Member State was asked to nominate a national survey coordinator, who gathered the views of national digital-health and AI experts. One response per state. The UK response covers England only. Bosnia and Herzegovina, Monaco and Turkmenistan did not take part (p. 6).
- **Definitions.** A national AI strategy in health is *"a high-level, government-endorsed document or framework"* for AI in the health sector (p. 9). Some questions were asked only of states that answered yes to a prior question, so some shares have smaller bases (p. 6).
- **Funding.** Co-funded by the European Union. External peer reviewers include three European Commission staff.

## Scope and reliability

- **Country-level self-report by government respondents.** The authors name the limits: broad terminology *"allowing for country-specific interpretations"*, dependence on the coordinators' expertise, and findings that *"may outdate quickly"* (p. 7). They claim *"documentary corroboration of submissions"* as a strength.
- **Not a measure of hospital adoption.** "64% report AI-assisted diagnostics" means a state reports such use somewhere in its system, not that 64% of hospitals use it.
- **No per-country figures in the main report.** Country profiles are published separately and were not fetched. The four states with a health-specific AI strategy are not named in the sections read.

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`**: a scan of the policy environment health organisations in 50 European countries work in, covering strategy, law, liability, data governance and workforce training.

## How it connects

- [[responsible-ai]] — liability standards, transparency guidance and post-market monitoring at national level; most states have not set them.
- [[enterprise-ai-adoption]] — context for the hospital-level figures: the rules hospitals deploy under are mostly unsettled.
- [[ai-maturity-measurement-comparison]] — a readiness measure at country level, a different unit from the organisational and worker measures in the thread.
- In this batch: [[2025-07-15-european-commission-ai-deployment-healthcare-final-report|European Commission deployment study]] surveys hospitals and clinicians in the same region and also finds unclear liability among the leading barriers.
- [[ai-in-health-care]]: the concept page that sets the health-care sources in this wiki side by side.

## What was actually ingested

The full 76-page PDF from WHO IRIS. Read closely: foreword, executive summary, methods and limitations, and section 3.1 on national strategies. Sections 3.2–3.6 were searched for the figures above but not read in full. Bar charts are flattened in the text conversion; the infographic percentages and counts survive.

## Linked entities and concepts

- [[responsible-ai]], [[enterprise-ai-adoption]] — concepts. [[ai-maturity-measurement-comparison]] — thread.

**Dangling** (single-source mention, deferred): WHO Regional Office for Europe (publisher; no entity page), Nicholas Letchford, Hanna Dunning, Nagui Salama (WHO consultants, main authors), Keyrellous Adib (WHO/Europe, main author), Natasha Azzopardi-Muscat and David Novillo Ortiz (technical conceptualization), Hans Henri P. Kluge (Regional Director, foreword).
