---
type: source
kind: paper
title: "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
author: ["Joel Becker", "Nate Rush", "Elizabeth Barnes", "David Rein"]
publisher: "METR (Model Evaluation & Threat Research); arXiv:2507.09089"
url: "https://arxiv.org/abs/2507.09089"
date_published: 2025-07-10
date_ingested: 2026-08-30
length: "abstract + reported headline results only (full paper not read)"
raw: "../../raw/papers/2025-07-10-becker-metr-early-2025-ai-experienced-oss-developer-productivity.md"
tags: [metr, rct, developer-productivity, slowdown, forecasting-error, cursor, claude-sonnet, open-source, experienced-developers, self-report-bias]
dynamic_capabilities:
  - contextual/internal-barriers
  - digital-transforming/improving-digital-maturity
relationships:
  - type: contradicts
    target: 2026-02-27-cui-demirer-generative-ai-high-skilled-work-three-field-experiments
    via: "the corpus's cleanest empirical disagreement about AI and developer output, and both are randomised. METR: 16 experienced maintainers on their own mature repositories, +19% completion time (slower). Cui et al.: 4,867 developers across three corporate field experiments, +26.08% completed tasks (faster). The disagreement is not about whether the studies are sound but about *population and task*: deep familiarity with a mature, high-standards codebase versus onboarding-heavy corporate work, and self-chosen issues versus assigned tasks. Cui et al.'s own heterogeneity result — juniors gain most — points at the same seam from the other side"
    confidence: 0.85
  - type: supports
    target: 2026-02-12-gloaguen-evaluating-agents-md-repository-level-context-files
    via: "two rigorous negative results against interventions the field assumed were obviously positive, and both survive robustness checks. METR finds AI assistance slows experienced developers on familiar code; Gloaguen et al. find repository context files don't improve success while costing >20% more. Together they are the corpus's strongest evidence that in agentic software engineering, *plausible* and *measured* diverge routinely"
    confidence: 0.7
  - type: supports
    target: 2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes
    via: "the same overhead seen from the two ends of the pipeline. METR measures the time cost falling on the developer who must review and repair AI output; the rejection study measures the 46.41% of agent-authored fixes that absorb human review and CI cycles and are then discarded. Both are accounting for work the productivity story does not count"
    confidence: 0.7
---

# Becker et al. (METR) — Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity

## TL;DR

A **randomised controlled trial** — rare in this literature — in which **16 experienced open-source developers** completed **246 real tasks** on **mature projects they had worked on for an average of five years**, with each task randomly assigned to allow or forbid early-2025 AI tooling (mostly **Cursor Pro** with **Claude 3.5/3.7 Sonnet**).

**The headline result is a reversal of everyone's expectations, including the participants':**

| Estimate | Direction | Magnitude |
| --- | --- | ---: |
| Developers' forecast *before* | faster | **−24%** completion time |
| Economics experts' forecast | faster | −39% |
| ML experts' forecast | faster | −38% |
| Developers' estimate *after finishing* | faster | −20% |
| **Measured effect** | **slower** | **+19%** completion time |

The most important row is the fourth. **After doing the tasks, developers still believed AI had sped them up by 20% — while the clock said it had slowed them by 19%.** That is a ~39-point gap between felt and measured productivity, held by people who had just personally performed the work. Any organisation relying on developer self-report to evaluate AI tooling — which is most organisations, and is the methodology behind the adoption and satisfaction figures in [[2025-09-23-dora-2025-state-of-ai-assisted-software-development]] — is measuring the felt number.

**The authors did the hard part.** They collected and evaluated evidence for **20 properties of the setting** that could a priori explain the slowdown — project size and quality standards, prior AI experience, task selection, and so on. Their conclusion: *"Although the influence of experimental artifacts cannot be entirely ruled out, the robustness of the slowdown effect across our analyses suggests it is unlikely to primarily be a function of our experimental design."*

**What the result does and does not license.** It is a small-N study (16 developers) on a deliberately hard case: **high-context, high-standards, mature repositories where the developer already holds the model of the system in their head.** That is exactly the condition under which AI's contribution — supplying context and plausible code — is worth least and its cost — reading, verifying, correcting — is worth most. The correct reading is not "AI slows developers down"; it is **"the size and sign of the effect depend on how much of the work is context acquisition,"** which is precisely the seam [[2026-02-27-cui-demirer-generative-ai-high-skilled-work-three-field-experiments|Cui et al.]] land on from the opposite direction when they find juniors gain most.

**Two companion results reinforce the general lesson** — that in agentic software engineering, *plausible* and *measured* diverge routinely. [[2026-02-12-gloaguen-evaluating-agents-md-repository-level-context-files|Gloaguen et al.]] find repository context files raise inference cost >20% with no measured gain in success, and [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes|Abujadallah et al.]] find 46.41% of agent-proposed fixes rejected — both are the same overhead METR measures, accounted for at different points in the pipeline.

## Dynamic-capabilities reading

- **`contextual/internal-barriers`** — the perception gap is itself the barrier: an organisation cannot allocate correctly against a signal that is 39 points wrong in a known direction.
- **`digital-transforming/improving-digital-maturity`** — the study is a template for what measuring digital maturity honestly requires (randomisation and clocks, not surveys).

## Linked entities and concepts

- Entities: [[METR]], [[Elizabeth Barnes]], [[Anthropic]]
- Concepts: [[concepts/ai-coding-productivity-evidence|ai-coding-productivity-evidence]], [[concepts/micro-productivity-trap|micro-productivity-trap]], [[concepts/jagged-frontier|jagged-frontier]], [[concepts/agentic-engineering|agentic-engineering]]
- **Dangling** (single-source mention, deferred): Joel Becker, Nate Rush, David Rein

## Scope and reliability

**Abstract and reported headline results only** — the full paper, including the 20-property analysis and the per-developer breakdowns, was not read. Strong internal validity (randomised, clocked), limited external validity (16 developers, open-source, February–June 2025 tooling — a frontier that has since moved twice). The tooling vintage is the most perishable part: this measures Cursor Pro + Claude 3.5/3.7 Sonnet in an IDE, **not** the cloud-agent parallelism that the 2026 practitioner material is about.
