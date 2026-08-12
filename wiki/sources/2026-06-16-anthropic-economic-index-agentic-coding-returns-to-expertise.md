---
type: source
kind: report
title: "Agentic coding and persistent returns to expertise"
author: ["Zoe Hitzig", "Maxim Massenkoff", "Eva Lyubich", "Ryan Heller", "Peter McCrory"]
publisher: "Anthropic (Anthropic Economic Index)"
url: "https://www.anthropic.com/research/research/claude-code-expertise"
date_published: 2026-06-16
date_ingested: 2026-06-17
zotero_item_key: N6KSNEQM
length: "~18 pages, full ingest (figures 1–6 read from captions; appendix deferred — published separately)"
raw: "../../raw/reports/agentic-coding-and-persistent-returns-to-expertise.pdf"
tags: [anthropic, anthropic-economic-index, agentic-coding, claude-code, returns-to-expertise, domain-expertise, division-of-labor, planning-vs-execution, human-ai-collaboration, autonomy, occupation, soc-taxonomy, task-value, success-measurement, ai-employment-effects, automation-vs-augmentation]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-transforming/redesigning-internal-structures
  - strategic-renewal/business-model
  - contextual/external-triggers
relationships:
  - type: published-by
    target: Anthropic
    via: "Anthropic research note; part of the Anthropic Economic Index program; based on ~400,000 Claude Code sessions"
  - type: part-of
    target: Anthropic-Economic-Index
    via: "the agentic-coding installment of the AEI; extends the prior Claude Code autonomy work and the AEI usage reports to who-decides-what and success-by-expertise"
  - type: supports
    target: 2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai
    via: "same authors (Massenkoff, McCrory); the observed-exposure report measures occupation-level displacement risk, this measures session-level success — both find coding-occupation boundaries blurring"
  - type: supports
    target: 2026-05-07-anthropic-economic-index-5-learning-curves
    via: "sibling AEI report; longitudinal usage/skill framing — this report extends the series to the division of labor and returns to expertise"
  - type: supports
    target: 2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset
    via: "Argenti's mindset-over-skillset thesis is empirically echoed here: domain understanding, not coding proficiency, is what amplifies the tool"
  - type: supports
    target: 2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces
    via: "augmentation-dominant reshaping: every occupation succeeds at coding within points of software engineers — work is reshaped (composition shifts, task value rises), not wholesale replaced"
  - type: contradicts
    target: 2026-04-28-anthropic-economic-index-q4-2025
    via: "tension within the AEI program — the Q4 report's first-order deskilling (remaining task mix has lower education content as AI covers high-education tasks) sits against this report's finding that returns to domain expertise persist and even sharpen; different measures, partially opposing readings"
---

# Agentic coding and persistent returns to expertise

The **agentic-coding installment of the [[Anthropic Economic Index]]**, published by **[[Anthropic]]** (16 June 2026), based on a privacy-preserving analysis of **~400,000 interactive [[agentic-engineering|Claude Code]] sessions from ~235,000 people, October 2025 – April 2026**. Authors: **Zoe Hitzig**, **[[Maxim Massenkoff]]**, **[[Eva Lyubich]]**, **[[Ryan Heller]]**, and **[[Peter McCrory]]**. It extends the program's earlier Claude Code autonomy work from *how autonomous* the agent is to *who decides what*, *who is doing the work*, and *whether it succeeds* — and frames coding as "a leading case" for where agentic knowledge work is headed.

## Key findings

- **A clear division of labor: people decide *what*, the agent decides *how*.** Using a privacy-preserving decision-attribution classifier, the report splits each session's decisions into **planning** (what to do, which approach, what counts as done) and **execution** (which files, what code, which commands). On average people make **~70% of planning** decisions but only **~20% of execution** decisions. "People decide what to build, and the agent decides how to build it."
- **Action volume tracks who holds control.** A typical session is ~4 turns; each user prompt sets off **~10 Claude actions** on average (the tail is long — ~2% of sessions average >100 actions/prompt). When the user keeps execution control (>80% of execution decisions), Claude takes ~8 actions/turn; when Claude controls planning (>80%), it takes ~16. Claude writes ~2,400 words of output per turn.
- **Returns to expertise persist — but it's *domain* expertise, not coding skill.** A task-specific expertise classifier (novice→expert, five-point) keys on how precisely the user frames directions, what they ask Claude to verify, and who corrects whom. Expertise is explicitly *not* job title and *not* general ability: "A senior engineer asking their first Rust question is a beginner at Rust." More expertise → Claude does more per instruction: novice sessions ~5 actions / ~600 words per prompt; expert sessions ~12 actions / ~3,200 words (+9% actions, +13% output per expertise level, robust to controls; p < 0.001).
- **Competence captures most of the benefit; mastery adds little.** Verified success (judged success *plus* a hard verifiable signal — commits/PRs, passing tests, explicit user affirmation) rises from **15% (novice) to 28–33% (intermediate and up)**; partial success 77% → 91–92%. Most of the gain is **novice→intermediate**; the intermediate→expert slope flattens. Among troubled sessions, verified success rises 4% (novice) → 15% (expert), and **novices abandon ~19% of troubled sessions vs 5–7% for everyone else** — *steering* is the expertise premium.
- **Occupation matters less than expertise.** Occupation is inferred from transcript signals (project context, file names, referenced artifacts, vocabulary), mapped to 23 BLS SOC major groups, and explicitly *not* inferred from the act of coding. In code-producing sessions, **every one of the ten largest occupations lands within seven points of software engineers** on success (≈34% vs 29%); the gap is small and has neither widened nor narrowed. Management occupations score slightly *above* software engineers (possibly transferable delegation skill, possibly a measurement artifact of managers confirming success more explicitly). "Coding agents are making a coding background less relevant to successful programming."
- **Work composition shifted in seven months.** Sessions spent **fixing broken code fell 33% → 19%**; **operating software grew 14% → 21%**; **writing and data analysis roughly doubled (~10% → ~20%)**. Usage moved toward more end-to-end agentic use (deploying/running code, analyzing data, non-code documents). ~56% of sessions write/fix/test/orchestrate code; ~17% operate software; ~14% plan or explore; ~13% produce analysis or prose. ~⅕ of sessions touch no codebase at all.
- **Task value rose ~25–27%.** Each session's value is approximated against a public dataset of freelance-marketplace postings (relative, not literal dollars). Average session value rose **~27%** Oct→Apr; building, operating, and fixing tasks each grew ~⅓ or more (≈43%, 34%, 32%).

## The nine modes of work

Each session is classified into the single mode that best describes its goal: **building** new code, **fixing** broken code, **testing**, **orchestrating** agents/pipelines, **operating** software (deploy/configure/run/monitor), **understanding** an existing system, **planning** a change, **analyzing** data, and **communicating** (presentations/prose). The classifier (Claude Sonnet 4.6) agrees with automatic telemetry on >90% of code-change labels.

## How success is measured (worth importing)

The report cannot observe real-world outcomes, so it relies on transcript-based proxies: **judged success** (a classifier reads the full transcript: succeeded / partially / failed / no clear goal), then **verified success** = judged success *and* at least one hard signal from a **success-signal classifier** (git commits/PRs matching the work, passing test suites, explicit user affirmation; scored 1–5) with a parallel **failure-signal** classifier (errors, failed tests, retries, user pushback). Sessions with "no clear goal" (~7.7%) are excluded from the success analysis. This is a reusable scaffolding for evaluating agent sessions where ground-truth outcomes are unobservable.

## Looking ahead (the authors' framing)

Anthropic frames the report as an early read on labor-market transitions: agentic coding **amplifies domain knowledge while substituting for implementation-heavy work**. Two leading indicators they will track: (1) if **returns to expertise begin to fall**, that would signal models are starting to supply the judgment users currently bring (gains broadening beyond domain experts); (2) if **non-software occupations' success keeps rising**, software production may be becoming ordinary work in every field. "Coding is a leading case — what happens in software is likely a preview of what may come as agentic tools take on other forms of knowledge work."

## What was actually ingested

The full 18-page PDF. (Originally hand-acquired under the non-descriptive content-management name `CCEconReport-G.pdf`; re-acquired 2026-06-18 via the [zotero-acquire](../../CLAUDE.md) channel — Zotero key `N6KSNEQM` — which supplied the descriptive filename now recorded in `raw:` and consolidated the duplicate. Zotero mis-typed the item `journalArticle`; it is a research report, routing corrected to `raw/reports/`.) Figures 1–6 were read from their captions and surrounding text, not reproduced. The **Appendix** (classifier full text, validation results, regression details, task-estimator construction) is **published separately** ("Available here") and was not ingested; classifier-validation claims here rest on the body's summary. All classifiers use **Claude Sonnet 4.6** unless noted. The report excludes non-interactive / headless (`claude -p`) and third-party-IDE/SDK usage — "a substantial share of activity" the authors flag as future work.

## Why this matters to the wiki

This report sharpens several live threads:

- It is the **division-of-labor primary** for [[automation-vs-augmentation]] at the *task-within-session* grain — the planning/execution split operationalises "who is doing the work" more finely than the AEI's Directive/Feedback-Loop vs Iteration/Learning/Validation taxonomy.
- It is the **strongest evidence yet for the "domain expertise, not coding proficiency" claim** that [[durable-skills]] has been assembling — and it empirically echoes [[2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset|Argenti's mindset-over-skillset]] thesis.
- It complicates the [[ai-deskilling]] story: the AEI's [[2026-04-28-anthropic-economic-index-q4-2025|Q4 report]] found first-order deskilling (the remaining human task mix has *lower* education content as AI covers high-education tasks), whereas this report finds that **domain understanding becomes more pivotal**, not less. The two are not strictly contradictory (deskilling is about task composition within a job; returns-to-expertise is about who succeeds with the tool) but they pull in opposite rhetorical directions — captured as a `contradicts` edge with a clarifying `via`.
- It corroborates the occupation-blurring direction of [[2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai|the observed-exposure report]] (same authors) and the augmentation-dominant reshaping of [[2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces|BCG's reshaping report]] from the usage side.

## Dynamic-capabilities reading

- **digital-sensing/digital-scouting** — Anthropic scouts emerging labor-market and knowledge-work signals directly from agent usage telemetry (work modes, decision attribution, success rates), a usage-data sensing instrument for where agentic work is heading.
- **digital-transforming/redesigning-internal-structures** — the planning/execution division of labor is, in effect, a template for how knowledge work is being restructured around human-agent collaboration: humans concentrate on framing and verification, agents on implementation.
- **strategic-renewal/business-model** — the "software production may become ordinary work in every field" framing implies business-model-level renewal of who performs technical work and how technical capability is sourced.
- **contextual/external-triggers** — the agentic-coding adoption wave (GitHub coding-agent activity more than doubled since late 2025; Claude Code users averaging ~20 hours/week) is the external trigger reshaping the knowledge-work context this report reads.

## Linked entities and concepts

- Publisher: [[Anthropic]]; program: [[Anthropic Economic Index]].
- **Promoted to entities this ingest** (second-source rule — both also co-author the [[2026-05-07-anthropic-economic-index-5-learning-curves|5th AEI report]]): [[Eva Lyubich]], [[Ryan Heller]].
- Already entities: [[Maxim Massenkoff]] (Naval Postgraduate School), [[Peter McCrory]] (Anthropic).
- **Dangling** (single-source mention, deferred): Zoe Hitzig (lead author; first appearance in the corpus — promote on a second source).
- Concepts: [[ai-employment-effects]], [[automation-vs-augmentation]], [[durable-skills]], [[agentic-engineering]], [[ai-deskilling]].

## Relationships

- *published-by* [[Anthropic]]; *part-of* [[Anthropic Economic Index]].
- *supports* [[2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai]] — same-author sibling; occupation-level exposure ↔ session-level success.
- *supports* [[2026-05-07-anthropic-economic-index-5-learning-curves]] — sibling AEI report.
- *supports* [[2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset]] — empirical echo of mindset/domain over skillset.
- *supports* [[2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces]] — augmentation-dominant reshaping.
- *contradicts* [[2026-04-28-anthropic-economic-index-q4-2025]] — deskilling vs persistent returns to expertise; a tension *within* the AEI program (see `via`).
