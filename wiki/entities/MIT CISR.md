---
type: entity
kind: org
aliases: ["MIT CISR", "MIT Center for Information Systems Research", "Center for Information Systems Research"]
tags: [mit-sloan, mit, ai-research, business-research, digital-transformation]
parent: "MIT Sloan"
website: "https://cisr.mit.edu"
confidence: 0.8
last_confirmed: "2026-11-07"
accessed_at: "2026-11-07"
source_count: 4
relationships:
  - type: employs
    target: Stephanie-Woerner
    via: "Director"
  - type: employs
    target: Peter-Weill
    via: "Chairman"
  - type: employs
    target: Ina-Sebastian
    via: "Research scientist"
---

# MIT CISR

The **MIT Center for Information Systems Research** is a research center at the MIT Sloan School of Management, focused on how organizations use technology and data to compete and create value. Studies digital business models, IT investment portfolios, AI maturity, and large-enterprise transformation.

## Role in the wiki

A primary research source for **enterprise transformation in the digital economy** — methodologically distinct from McKinsey-style consulting research (which underpins much of the [[2026-04-28-ai-index-report-2025|AI Index]] adoption data). MIT CISR's lens is **stage-based maturity models** rather than per-function adoption rates.

Key methodological instruments mentioned in the wiki:

- **Future Ready Survey** (last published wave used: 2022, N=721) — large-N quantitative input.
- **Executive interviews** (e.g., 2024: 16 executives at 9 enterprises) — qualitative depth on transitions.
- Combined into **maturity scoring** (0–100% Total AI Effectiveness scale, banded into stages).

## Frameworks attributed to MIT CISR (in the wiki)

- **Four Stages of Enterprise AI Maturity** — see [[2026-04-28-mit-sloan-ai-maturity|MIT Sloan article]] and [[enterprise-ai-adoption]].
- **Four S Framework** (Strategy / Systems / Synchronization / Stewardship) — challenges to scale Stage 2 → Stage 3.
- **Digital Business Models** (Weill & Woerner, *What's Your Digital Business Model?*, HBR Press 2018): Supplier, Omnichannel, Modular Producer, Ecosystem Driver. Tracked in survey waves from 2013 to 2025 (2,378 company observations); Ecosystem Driver rose from 12% to 58% of companies.
- **Business Models in the AI Era** (2025): the 2018 framework redrawn with new axes (*action on behalf of customers*: assist or represent; *business execution*: structured or adaptive) into Existing+, Customer Proxy, Modular Curator and Orchestrator. See [[2025-10-16-weill-cisr-business-models-ai-era|Weill, Sebastian, Woerner & Benedict (Research Briefing No. XXV-10, Oct 2025)]], the wiki's first first-party CISR publication; the maturity model reached the wiki only through MIT Sloan's summary.

## Notable people (mentioned in this wiki)

- [[Stephanie Woerner]] — Principal research scientist at MIT Sloan, **Director of MIT CISR**.
- [[Peter Weill]] — Senior research scientist at MIT Sloan, **Chairman of MIT CISR**.
- [[Ina Sebastian]] — Research scientist at MIT CISR (digital partnering, value creation, value capture).
- Evgeny Káganer — Research collaborator (also professor at IESE Business School).
- Gayan Benedict — Industry Research Fellow; co-author of the AI-era business-models briefing (Dangling).

## Research briefings (added 2026-11-07)

CISR publishes a monthly *Research Briefing* for its member organisations. The full text is readable on the web without login; login gates only the PDF download. Briefings are short (around 1,500 words), present a framework with one or two company cases, and end with questions for leaders. The recommended use is as a shared language for a senior-leadership discussion. They are written for members of a consortium funded by large firms (ANZ, Barclays, BNP Paribas, JPMorgan Chase, PwC and others), and the frameworks tend to be tested in executive meetings rather than statistically.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "mit-cisr")
SORT file.name ASC
```

## Open questions

- Funding model and member organizations of CISR (it's typically a member-funded research center; details to fill in as more sources reference it).
- Earlier Future Ready Survey waves (pre-2022) and how methodology has evolved.

## AI-maturity and health-care sources (added 2026-11-07)

- [[2025-08-21-mit-cisr-grow-enterprise-ai-maturity]] — the August 2025 research briefing that re-measured the four-stage model: Stage 4 at 18% in a 2025 survey (N=152) against 7% in the 2022 Future Ready Survey (N=721), with the same scoring rule. The March 2026 follow-up is members-only.
