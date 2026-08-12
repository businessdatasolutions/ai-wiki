---
type: source
kind: paper
title: "Expertise"
subtitle: "Joseph R. Schumpeter Lecture, European Economic Association, Rotterdam, 29 August 2024"
author: ["David Autor", "Neil Thompson"]
publisher: "National Bureau of Economic Research (NBER)"
nber_working_paper: "No. 33941"
jel_codes: "E24, J11, J23, J24"
url: "https://www.nber.org/papers/w33941"
raw: "../../raw/papers/expertise-autor-thompson-2025.md"
date_published: 2025-06
date_ingested: 2026-07-14
tags: [david-autor, neil-thompson, nber, expertise, task-bundling, occupational-task-model, automation, wages, employment, garicano, labor-economics, schumpeter-lecture, expertise-framework]
length: "~74 pages (full text, references, and appendix)"
relationships:
  - type: authored-by
    target: Neil-Thompson
  - type: supports
    target: 2026-05-21-jones-stanford-gsb-ai-and-our-economic-future
    via: "both formalize why partial task automation raises wages for workers in the un-automated remainder — Jones's macro *weak-links* model (jobs are bundles of tasks; automating 75% of them makes the remaining 25% scarce) and Autor-Thompson's micro *expertise-hierarchy* model (task bundling + a rankable expertise ladder) are independent formalizations of the same underlying mechanism, at growth-theory and occupational-labor-economics altitude respectively"
  - type: supports
    target: 2026-04-28-brynjolfsson-canaries-coal-mine
    via: "Autor-Thompson's expertise framework supplies a theoretical mechanism for Brynjolfsson et al.'s empirical codified-vs-tacit-knowledge finding — codified, procedural knowledge is disproportionately the *inexpert* task content that gets automated first and lowers wages, while tacit, judgment-heavy knowledge is disproportionately the *expert* task content whose removal (or retention) raises wages, matching why young workers (who supply relatively more codified than tacit knowledge) are hit hardest"
---

# Autor & Thompson — Expertise

## TL;DR

An NBER working paper (No. 33941, June 2025; delivered as the **Joseph R. Schumpeter Lecture** to the European Economic Association, Rotterdam, 29 August 2024, under the title *"Does Automation Replace Experts or Complement Expertise? The Answer is Yes."*) by **David Autor** (MIT Economics) and **Neil Thompson** (MIT FutureTech / CSAIL / Initiative on the Digital Economy). It proposes and empirically tests an **expertise framework** that explains a puzzle the canonical automation literature cannot: why routine-task automation has simultaneously **lowered employment but raised wages** in some routine-task-intensive occupations, while doing the reverse in others.

**The two theoretical pillars:**

1. **Expertise** — a worker's capability to perform specific tasks, rankable along a single hierarchical dimension (following Garicano 2000; Garicano & Rossi-Hansberg 2006): a higher-expertise worker can always perform a lower-expertise task, never the reverse. Expertise is a wage premium *and* a barrier to entry.
2. **Occupational task bundling** — all tasks bundled into an occupation must be performed by every worker in that occupation, and expertise requirements *differ* across the bundled tasks. Some are the occupation's expert tasks; others are its inexpert tasks. (This departs from canonical task models, which assume atomistic task assignment with no two skill groups performing the same task.)

**The core prediction, worked through the paper's canonical contrast (accounting clerks vs. inventory clerks — both extensively computerized, both facing similar automation exposure):** automation that removes an occupation's *inexpert* tasks raises the expertise required for what remains → **wages rise, employment falls** (fewer workers qualify). Automation that removes an occupation's *expert* tasks lowers the expertise required for what remains → **wages fall, employment rises** (more workers can now qualify). Wage and employment effects move in **opposite directions**, and the direction itself is set by *which* tasks — expert or inexpert — are automated, not by *how much* automation occurs.

**The taxi-driver / proofreader worked pair** (the TEDx talk's central illustration, §below): GPS automated taxi drivers' single most *expert* task — memorizing streets (London's famous multi-year "Knowledge" test) — so driving became accessible to far more people: **wages grew more slowly than the economy; employment surged** (the Uber-era expansion). Spellcheck automated proofreaders' *least* expert task, leaving the harder judgment work (argument structure, evidence quality) intact: **wages grew significantly faster than the economy; employment shrank**.

**The empirical contribution:** a novel, **content-agnostic** method for measuring occupational task expertise from job-task text, grounded in the Efficient Coding Hypothesis (word frequency/entropy), plus a longitudinal method using word embeddings to track which tasks were added or removed from occupations across four decades — without requiring tasks to be described consistently over time. Applied to U.S. occupational employment and wage data (1980s–2020s):

- Changes in occupational expertise (from task removal *and* addition) **strongly predict changes in occupational wages**, independent of the sheer *quantity* of tasks added or removed.
- **Removing expert tasks** and **adding inexpert tasks** both predict *wage declines*; **removing inexpert tasks** and **adding expert tasks** both predict *wage gains* — the reverse of quantity effects (gaining tasks expands employment; losing tasks contracts it — opposite to the expertise-wage relationship).
- **Employment moves opposite to wages** on the expertise axis: occupations with rising expertise requirements see *falling* employment (fewer qualify) *despite* rising wages; occupations with falling expertise requirements see *rising* employment *despite* falling wages.
- Applied to the historical routine-task-automation literature specifically: automation **bifurcated** occupational outcomes depending on whether the automated routine tasks were relatively *expert* (→ lower wages, higher employment in that occupation) or relatively *inexpert* (→ higher wages, lower employment) — resolving the "why did routine automation lower employment but often raise wages" puzzle that canonical task models leave unexplained.
- The authors explicitly flag the AI era as a next natural application of the same framework (Conclusions, p.53): *"there is nothing in our model that is specific to the computer era… the rapidly advancing era of Artificial Intelligence"* is named as an equally applicable domain, though the empirical evidence in the paper itself covers the last four decades of computerization, not AI specifically.

## What was actually ingested

The **full 74-page working paper** — abstract, introduction, theoretical model, the novel expertise-measurement methodology, the four-decade empirical analysis, the routine-task-automation application, conclusions, references, and appendix (including the GPT-4.1 prompt used to classify tasks into the RC/RM/NC/NM/NI routine-vs-non-routine × cognitive-vs-manual taxonomy). Converted from the co-located PDF (`raw/papers/expertise-autor-thompson-2025.pdf`, gitignored) via `pdftotext -layout`; page count (74) and the presence of a complete References section and Appendix confirm no truncation.

## Why this source matters to the wiki

This is the wiki's **first primary academic paper formalizing occupational task bundling with an expertise hierarchy** — a theoretical grounding the wiki previously held only at the level of practitioner restatement ([[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Evans's task vs job]]) or a different formal tradition ([[2026-05-21-jones-stanford-gsb-ai-and-our-economic-future|Jones's macro weak-links growth model]]). It supplies:

- **The mechanism behind the wiki's "automation sometimes raises wages" puzzle.** [[ai-employment-effects|ai-employment-effects]] already documents that automation-exposed occupations show heterogeneous wage/employment outcomes; this paper is the theoretical account of *why*, keyed to which tasks (expert vs. inexpert) get automated — not merely *how much* of an occupation is automated.
- **A rigorous companion to [[2026-05-21-jones-stanford-gsb-ai-and-our-economic-future|Jones's weak-links model]].** Both predict that partial automation raises the wages of workers retained in the un-automated remainder; Jones's version is macro/growth-theoretic (jobs as generic task bundles, GDP-share accounting), Autor-Thompson's is micro/occupational (a rankable expertise hierarchy, tested against 40 years of U.S. occupational payroll and task data). The taxi-driver/proofreader pair is a sharper, more falsifiable worked example than Jones's radiologist anecdote.
- **A theoretical account for Brynjolfsson's codified-vs-tacit mechanism.** [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson et al.]] find AI displaces codified knowledge more than tacit knowledge, disproportionately hurting young workers who supply more of the former. Autor-Thompson's expert/inexpert task distinction is a formalization of the same codified/tacit intuition, with an explicit hierarchy and task-bundling structure that makes it empirically testable at the occupation level.
- **An accompanying TEDx talk** ([[2026-07-10-thompson-tedxboston-how-ai-will-reshape-jobs|Thompson, TEDxBoston, July 2026]]) that translates the same expertise framework — using the identical taxi-driver/proofreader pair — into an AI-era register, plus a new empirical layer (task-level LLM evaluation data) that projects expertise change forward rather than only measuring it retrospectively over the last four decades.

## Linked entities and concepts

- [[ai-employment-effects]] — primary target; adds the expertise-hierarchy/task-bundling theoretical model as the mechanism behind the page's heterogeneous automation wage/employment findings.
- [[automation-vs-augmentation]] — the expert/inexpert task distinction sharpens the *task vs job* analytical lever already on that page (Evans) with a formal, empirically-tested hierarchy.
- **Dangling** (single-source mention, deferred per [Author-entity promotion](../../CLAUDE.md#author-entity-promotion)): **David Autor** (MIT Economics; co-author) — named on this source only so far; promote on a second-source mention.

## Source quality

**Peer status**: an NBER working paper (circulated for discussion; not yet peer-reviewed, per NBER's standard disclaimer) delivered as an EEA Schumpeter Lecture — the format the discipline uses to showcase a senior economist's (here, joint) synthesis-and-new-result contribution. David Autor is one of the most-cited labor economists working on automation and task models (co-author of the canonical Autor-Levy-Murnane 2003 task model and the Acemoglu-Autor 2011 task-model literature this paper explicitly revises); Neil Thompson directs MIT FutureTech. Treat the theoretical model as rigorous and the empirical results as **illustrative rather than definitive** per the authors' own conclusion (p.53): a "relatively coarse set of occupations studied over a relatively short interval." No funding conflicts of the kind that would bias the automation-wage findings (funders: Hewlett Foundation, Google Technology and Society Visiting Fellows, NOMIS Foundation, Schmidt Sciences AI2050, Smith Richardson Foundation, Open Philanthropy).
