---
type: source
kind: report
title: "The GenAI Divide: State of AI in Business 2025"
author: ["Aditya Challapally", "Chris Pease", "Ramesh Raskar", "Pradyumna Chari"]
publisher: "MIT NANDA (Project NANDA, MIT Media Lab)"
url: "https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf"
date_published: 2025-07-01
date_ingested: 2026-11-07
length: "~26 pages (full report read; dated 'July 2025' on the cover, day unknown; public from mid-August 2025)"
raw: "../../raw/reports/2025-07-01-mit-nanda-genai-divide-state-of-ai-in-business-2025.md"
tags: [mit-nanda, project-nanda, genai-divide, state-of-ai-in-business-2025, enterprise-ai-roi, pilot-to-production, 95-percent, shadow-ai, build-vs-buy, learning-gap, agentic-web, preliminary-findings, convenience-sample, self-report]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/navigating-innovation-ecosystems
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-05-21-allen-aws-london-exec-forum-agentic-team-structures
    via: "the report behind Allen's '95% of organizations are getting zero return' citation; Allen reads out the executive summary's first sentence, including the $30-40 billion"
    confidence: 0.75
  - type: supports
    target: 2025-12-02-allen-brozovich-davis-aws-reinvent-advanced-team-structures
    via: "the report Allen cites in the December 2025 edition of the same talk for 95% zero return against $30-40 billion of enterprise GenAI investment"
    confidence: 0.7
  - type: supports
    target: 2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company
    via: "the 'MIT finding' Grant calls a canary in the coal mine and faults for its small sample; the report's survey is 153 senior leaders at four conferences, plus interviews at 52 organisations, not 153 companies"
    confidence: 0.65
---

# The GenAI Divide: State of AI in Business 2025 (MIT NANDA)

## TL;DR

The source of the widely quoted "95% of organizations get zero return" figure. Four authors from Project NANDA at MIT label it *"Preliminary Findings"* (p. 2). The research period was January to June 2025 (p. 2). The cover says July 2025, and the report reached the press in mid-August 2025.

1. **The headline.** *"Despite $30–40 billion in enterprise investment into GenAI, this report uncovers a surprising result in that 95% of organizations are getting zero return"* (p. 3). The same paragraph says *"Just 5% of integrated AI pilots are extracting millions in value"* (p. 3).
2. **The funnel.** For general-purpose LLMs, 80% of organisations investigated, 50% piloted and 40% *"successfully implemented"*. For embedded or task-specific GenAI it was 60%, 20% and **5%** (exhibit, p. 6; text, p. 3).
3. **The success definition.** *"We define successfully implemented for task-specific GenAI tools as ones users or executives have remarked as causing a marked and sustained productivity and/or P&L impact"* (p. 7). The appendix gives a second definition: *"deployment beyond pilot phase with measurable KPIs. ROI impact measured 6 months post-pilot"* (p. 24).
4. **The authors' own caveat.** *"These figures are directionally accurate based on individual interviews rather than official company reporting. Sample sizes vary by category, and success definitions may differ across organizations"* (p. 6).
5. **Buy beats build.** External partnerships reached deployment *"~67% of the time, compared to ~33% for internally built tools"* (p. 19). The authors add that the gap *"may reflect organizational capabilities rather than implementation approach alone"* (p. 19).
6. **Shadow AI.** Only 40% of companies bought an official LLM subscription, yet workers at *"over 90%"* of the companies surveyed use personal AI tools for work (p. 8).

## Key data

| Figure | Exact wording or definition | Page |
| --- | --- | ---: |
| 95% | "of organizations are getting zero return" | 3 |
| $30–40 billion | "enterprise investment into GenAI" (no source given) | 3 |
| 5% | "of integrated AI pilots are extracting millions in value" | 3 |
| 60% → 20% → 5% | organisations that evaluated, piloted, and put into production enterprise-grade (custom or vendor) GenAI systems | 3, 6 |
| 80% → 50% → 40% | the same funnel for general-purpose LLMs (ChatGPT, Copilot); text says "nearly 40 percent report deployment" | 3, 6 |
| 5% | "of enterprises have AI tools integrated in workflows at scale" (Myth 2) | 7 |
| ~83% | pilot-to-implementation rate for generic LLM chatbots | 7 |
| 2 of 8 / 7 of 9 | sectors with structural disruption vs sectors without (the report uses both counts; the bar chart shows seven industries, the table eight) | 3, 4, 5 |
| 0.5 of 5 | Healthcare & Pharma on the disruption index: "Documentation/transcription pilots; clinical models unchanged" | 5 |
| ~67% vs ~33% | deployment rate, external partnerships vs internal builds | 19 |
| 40% vs 90%+ | companies with an official LLM subscription vs companies whose workers use personal AI tools | 8 |
| ~50% (text) / ~70% (survey) | share of a hypothetical $100 GenAI budget going to sales and marketing | 9, 10, 20 |
| 90 days vs 9+ months | pilot-to-implementation time, top mid-market firms vs enterprises (>$100M revenue) | 7 |
| 5–20% | workforce reductions in customer support and administrative processing at affected companies | 21 |

## Method and definitions

- **Design** (p. 2): *"a systematic review of over 300 publicly disclosed AI initiatives, structured interviews with representatives from 52 organizations, and survey responses from 153 senior leaders collected across four major industry conferences."* The appendix repeats this as *"52 structured interviews ... 300+ public AI initiatives ... surveys with 153 leaders"* (p. 24). The four conferences are not named.
- **Who answered.** Executive sponsors and frontline users (p. 11). A *"lightweight survey supplemented these interviews"* (p. 25). The interview guides are printed (pp. 25–26).
- **Unit.** The 95% is a share of *organizations*. The 5% figures are shares of *pilots*, of *organisations reaching production*, and of *enterprises with tools integrated at scale*. The report moves between these without reconciling them.
- **Enterprise** means a firm with more than $100 million in annual revenue (p. 7).
- **Disruption index.** Each industry is scored 0–5 on five indicators, *"triangulated from public indicators and interview-derived assessments"* (p. 4).
- **Reviewers.** *"Pradyumna Chari, Project NANDA"* (p. 2), who is also a co-author. There is no external peer review.

## Scope and reliability

- **Small, self-selected sample.** 153 survey respondents met at conferences and 52 interviewed organisations. The authors list selection bias themselves (p. 24): firms willing to talk about AI problems *"may systematically differ"* from those that decline.
- **Self-report, not company data.** The authors call the figures *"directionally accurate"* (p. 6). Several exhibits are coded from interview notes (p. 15), and budget sub-categories *"should be treated as directional at best"* (p. 10).
- **Two success definitions.** The 95% rests on *"zero return"*. The p. 7 definition requires a *"marked and sustained"* impact remarked on by users or executives. The p. 24 definition requires measurable KPIs six months after the pilot. A six-month window *"may be insufficient"*, *"potentially understating success rates"* (p. 24).
- **A stricter bar than other surveys.** Stefano Puntoni, a co-author of the [[2025-10-28-wharton-gbk-ai-adoption-report-2025|Wharton/GBK 2025 report]], told Big Technology: *"Our definition is very different from the MIT report. Theirs is much more stringent"* (Kantrowitz, 31 Oct 2025; raw at `raw/articles/2025-10-31-kantrowitz-big-technology-are-74-percent-of-businesses-seeing-genai-roi.md`).
- **Method reported differently in the press.** Fortune's 18 August 2025 story (read with WebFetch) described *"150 interviews with leaders, a survey of 350 employees, and an analysis of 300 public AI deployments."* The PDF says 52 organisations and 153 senior leaders. This page follows the PDF.
- **Interest in the conclusion.** Project NANDA builds agent-interoperability infrastructure. The report's prescription ends with *"Systems like NANDA, MCP, and A2A represent early infrastructure for this web"* (p. 23).
- **Provenance.** No copy on an MIT domain was found on 7 November 2026; nanda.media.mit.edu redirects to the Media Lab group page. The file used is a third-party copy whose metadata names Aditya Challapally as author (created 14 July 2025).

## Dynamic-capabilities reading

- **`digital-seizing/balancing-digital-portfolios`**: the report is about scaling up, from pilot to production. Its main contrast, external partnerships against internal builds, is the cell's *"balancing internal and external options."*
- **`digital-transforming/navigating-innovation-ecosystems`**: the successful buyers *"act like BPO clients, not SaaS customers"*, co-develop with vendors, and find tools through referrals and existing partners (pp. 17–19).
- **`contextual/internal-barriers`**: the rated barriers to scale are change management, lack of executive sponsorship, poor user experience, output quality and unwillingness to adopt new tools (p. 11). The report's own diagnosis is a *"learning gap"*: tools that do not keep feedback or adapt (p. 3).

## How it connects

- [[enterprise-ai-adoption]]: a value-capture figure, measured on a much stricter bar than adoption surveys.
- [[ai-maturity-measurement-comparison]]: a strict-definition instrument with a small conference sample. Its 95% and 5% figures use different denominators.
- [[micro-productivity-trap]]: the report's split between individual productivity (ChatGPT, Copilot) and P&L impact (p. 3) is the trap stated as data.
- [[ai-knowledge-hiding]]: the "shadow AI economy" (p. 8), workers using personal accounts *"often without IT knowledge or approval."*
- [[agentic-web]]: the closing section names the *"Agentic Web"* (pp. 22–23).
- [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen at the AWS London Executive Forum]] quotes the headline. His three failure modes (workflow alignment, wrong targets, missing integration) follow the report's text (pp. 3, 6, 9–10).
- [[2025-12-02-allen-brozovich-davis-aws-reinvent-advanced-team-structures|Allen, Brozovich and Davis at re:Invent 2025]]: the earlier edition of the same talk with the same citation. The [[2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world|Sydney edition]] repeats it as *"95% of AI pilots fail."*
- [[2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company|BBC AI Decoded]]: Peter Grant prefers the [[PwC]] CEO survey to this report on sample-size grounds.
- [[2025-10-28-wharton-gbk-ai-adoption-report-2025|Wharton/GBK 2025]], [[2025-09-30-bcg-widening-ai-value-gap-2025|BCG 2025]] and [[2025-05-06-accenture-front-runners-guide-scaling-ai|Accenture 2025]]: other 2025 measures of AI value, each with its own definition and sample.

## What was actually ingested

All 26 pages of the PDF, converted with `pdftotext -layout`. Exhibits whose values are drawn rather than typed (pp. 11, 12, 13, 15) lost their numbers in conversion; this page quotes only figures stated in the text. The copy comes from mlq.ai, a third-party host. Fortune's 18 August 2025 article was read only for its description of the method. The Big Technology article is kept in `raw/` as secondary commentary.

## Linked entities and concepts

- [[Jonathan Allen]]: cites the report in three editions of his AWS talk.
- [[PwC]]: the survey the BBC panel prefers to this one.
- [[enterprise-ai-adoption]], [[micro-productivity-trap]], [[ai-knowledge-hiding]], [[agentic-web]]: concepts.
- [[ai-maturity-measurement-comparison]]: thread.

**Dangling** (single-source mention, deferred): Aditya Challapally, Chris Pease, Ramesh Raskar, Pradyumna Chari (authors); MIT NANDA / Project NANDA (organisation; also named in the bodies of the three AWS sources and the BBC source); MIT Project Iceberg (cited p. 22); Stefano Puntoni (quoted via Big Technology; author of the Wharton/GBK report); Alex Kantrowitz (Big Technology); Fortune.
