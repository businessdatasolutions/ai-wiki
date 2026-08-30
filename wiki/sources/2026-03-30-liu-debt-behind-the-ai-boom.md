---
type: source
kind: paper
title: "Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild"
author: ["Yue Liu", "Ratnadira Widyasari", "Yanjie Zhao", "Ivana Clairine Irsan", "Junkai Chen", "David Lo"]
publisher: "Singapore Management University; arXiv:2603.28592"
url: "https://arxiv.org/abs/2603.28592"
date_published: 2026-03-30
date_ingested: 2026-08-30
length: "abstract only (full paper not read)"
raw: "../../raw/papers/2026-03-30-liu-debt-behind-the-ai-boom.md"
tags: [technical-debt, ai-generated-code, static-analysis, code-smells, issue-lifecycle, survival-analysis, github, maintenance-cost, quality-assurance, empirical-software-engineering]
dynamic_capabilities:
  - contextual/internal-barriers
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: 2025-09-23-dora-2025-state-of-ai-assisted-software-development
    via: "the repository-level mechanism for DORA's survey-level finding. DORA reports AI adoption keeping a negative relationship with delivery *stability* even as throughput turns positive, and attributes it to change volume outrunning control systems; this paper shows what is physically accumulating — 484,366 issues introduced across 302.6k AI-authored commits, with 22.7% still present at the latest revision"
    confidence: 0.8
  - type: supports
    target: 2025-07-30-veracode-2025-genai-code-security-report
    via: "the controlled measurement and the in-the-wild follow-through on AI code quality. Veracode establishes that 45% of AI-generated samples introduce OWASP Top 10 flaws under test conditions; this study tracks what happens to comparable defects after they land in production repositories — 89.3% of introduced issues are maintainability smells rather than security flaws, but 22.7% of everything introduced is never fixed"
    confidence: 0.75
  - type: contradicts
    target: 2026-02-27-cui-demirer-generative-ai-high-skilled-work-three-field-experiments
    via: "the same activity scored on different ledgers. Cui et al. measure *completed tasks* and find +26.08%; this paper measures what those completions leave behind and finds >15% of commits from every assistant introduce at least one issue, with 22.7% surviving to the latest version. Neither result refutes the other — but a productivity figure computed on task completion alone is incomplete by exactly this amount"
    confidence: 0.7
---

# Liu et al. — Debt Behind the AI Boom

## TL;DR

The study that follows AI-generated code *after* it lands. Prior work showed AI code has quality problems under controlled conditions; this asks whether those problems get fixed or accumulate.

**Method — and the method is the contribution.** A dataset of **302.6k verified AI-authored commits** from **6,299 GitHub repositories**, covering five widely used AI coding assistants. For each commit: **run static analysis before and after the change**, to attribute precisely which code smells, correctness issues and security issues the AI introduced. Then **track each introduced issue from its introducing commit to the latest repository revision** to study its lifecycle. The before/after differencing is what makes the attribution credible rather than correlational.

**Results:**

| | |
| --- | ---: |
| Distinct issues identified | **484,366** |
| Share that are code smells (maintainability) | **89.3%** |
| Commits introducing ≥1 issue, per assistant | **>15%** for every assistant (rates vary by tool) |
| **AI-introduced issues still alive at the latest revision** | **22.7%** |

**The 22.7% is the finding.** Roughly one in five defects that AI introduces is *never fixed*. Not "found late" — still present when the researchers looked. This is what makes the paper about **technical debt** rather than about code quality: a defect that gets fixed next sprint is a cost; a defect that survives indefinitely is a liability sitting on the balance sheet, and it compounds with every subsequent change to the same code.

**The 89.3% code-smell share cuts both ways.** Reassuring: most of what AI introduces is maintainability, not security or correctness. Unreassuring: maintainability debt is precisely the category with **no forcing function** — nothing breaks, no test fails, no incident fires, so nothing makes anyone fix it. That is a plausible explanation for the 22.7% survival rate, and it means the debt is concentrated in the category least likely to be paid down voluntarily.

**Where this sits in the corpus.** [[2026-02-27-cui-demirer-generative-ai-high-skilled-work-three-field-experiments|Cui et al.]] measure +26.08% completed tasks. [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes|Abujadallah et al.]] measure 46.41% of agent fixes rejected before merge. This paper measures what happens to what *does* merge. Reading the three together: **a large fraction of agent output is discarded at review, and a meaningful fraction of what survives review carries defects that are never repaired.** The throughput number is real; so is everything downstream of it, and only the first is usually counted.

**Two sources bracket this one.** [[2025-07-30-veracode-2025-genai-code-security-report|Veracode]] measures what AI writes under test conditions — 45% of samples introducing OWASP Top 10 flaws, flat across model size and vintage — and this study measures what survives after those changes merge. [[2025-09-23-dora-2025-state-of-ai-assisted-software-development|DORA]] observes the consequence at survey scale: AI adoption's relationship with delivery *stability* stayed negative even as throughput turned positive. This paper names what is accumulating inside that instability.

## Dynamic-capabilities reading

- **`contextual/internal-barriers`** — accumulating unfixed maintainability debt is a compounding barrier to future change velocity, and it is invisible to the metrics that justified adopting the tooling.
- **`digital-transforming/improving-digital-maturity`** — the paper's closing call for "stronger quality assurance in AI-assisted development" is a maturity prescription, and the before/after static-analysis method is itself an adoptable maturity practice.

## Linked entities and concepts

- Entities: [[GitHub]]
- Concepts: [[concepts/ai-generated-code-quality|ai-generated-code-quality]], [[concepts/agentic-pull-requests|agentic-pull-requests]], [[concepts/ai-coding-productivity-evidence|ai-coding-productivity-evidence]], [[concepts/agentic-engineering|agentic-engineering]]
- **Dangling** (single-source mention, deferred): Yue Liu, Ratnadira Widyasari, Yanjie Zhao, Ivana Clairine Irsan, Junkai Chen, David Lo

## Scope and reliability

**Abstract only** — the per-tool breakdown, the issue-severity distribution, and the survival curve shape were **not read**. The per-tool rates in particular are worth recovering, since ">15% for every assistant, rates vary" is doing a lot of work without disclosing the range. Two methodological limits to hold: **static analysis defines what counts as an issue**, so the 484,366 figure is "issues a static analyser flags," which over-counts style and under-counts logic; and **"verified AI-authored" depends on commit attribution**, which will miss AI-assisted code a human committed under their own name — biasing toward the most visibly agentic work. Survival is measured against *the latest revision at study time*, so an issue in a recent commit has had less opportunity to be fixed than one in an old commit; whether the analysis adjusts for exposure time is not visible from the abstract.
