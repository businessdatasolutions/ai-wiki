---
type: source
kind: report
title: "2025 DORA Report: State of AI-assisted Software Development"
author: ["Nathen Harvey", "Derek DeBellis"]
publisher: "DORA (DevOps Research and Assessment) / Google Cloud"
url: "https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report"
date_published: 2025-09-23
date_ingested: 2026-08-30
length: "announcement blog post only (~1,500 words); the full report was not converted"
raw: "../../raw/reports/2025-09-23-dora-2025-state-of-ai-assisted-software-development.md"
tags: [dora, google-cloud, devops, throughput, delivery-stability, ai-adoption, platform-engineering, team-profiles, amplifier-thesis, survey, trust]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
  - digital-transforming/redesigning-internal-structures
  - contextual/internal-enablers
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-03-30-liu-debt-behind-the-ai-boom
    via: "the survey signal and the repository-level mechanism for the same phenomenon. DORA reports that AI adoption retains a negative relationship with delivery *stability* even as throughput turns positive; Liu et al. show where that instability physically lives — 484,366 issues introduced across 302.6k AI-authored commits, 22.7% still present at the latest revision. DORA says the delivery system destabilises; Liu et al. say what is accumulating inside it"
    confidence: 0.8
  - type: supports
    target: 2026-02-27-cui-demirer-generative-ai-high-skilled-work-three-field-experiments
    via: "the correlational and the causal read on the throughput half. DORA's 2025 wave flips AI adoption's association with delivery throughput from negative to positive; Cui et al.'s pre-registered RCTs give a magnitude (+26.08% completed tasks). Neither addresses stability"
    confidence: 0.7
  - type: contradicts
    target: 2025-07-10-becker-metr-early-2025-ai-experienced-developer-productivity
    via: "not on findings but on instrument. DORA's productivity claim rests on self-report — >80% of respondents *believe* AI increased their productivity — and METR's RCT shows that exact belief off by roughly 39 points in a known direction for experienced developers. DORA's delivery metrics are behavioural and survive this; its perception metrics should not be read as productivity evidence"
    confidence: 0.7
---

# DORA — 2025 State of AI-assisted Software Development

## TL;DR

DORA's annual survey, this year focused entirely on AI: **~5,000 technology professionals worldwide** plus **100+ hours of qualitative data**. It is the largest-sample source in this ingest, and the one whose central finding is a **split**, not a direction.

**Adoption is effectively universal.** 90% of respondents use AI at work, up from 76% in 2024. 90% of organisations have adopted at least one platform. **Trust has not kept pace: 70% report trusting AI-generated code, meaning 30% report little or none** — a striking number given near-total adoption. People are using a tool a third of them do not trust.

**The central thesis: *"AI doesn't fix a team; it amplifies what's already there."*** Strong teams get more efficient; struggling teams find AI surfaces the problems they already had. This is the report's answer to why AI-adoption studies produce such scattered effect sizes — the moderator is the delivery system, not the tool.

**The throughput/stability split — the finding that matters.**

| Relationship with AI adoption | 2024 | 2025 |
| --- | --- | --- |
| Software delivery **throughput** | negative (~1.5% drop per 25% adoption rise) | **positive** |
| Software delivery **stability** | negative (~7.2% drop per 25% adoption rise) | **still negative** |

> "AI adoption does continue to have a negative relationship with software delivery stability."

The mechanism, in the report's own words: *"AI accelerates software development, but that acceleration can expose weaknesses downstream. Without robust control systems, like strong automated testing, mature version control practices, and fast feedback loops, an increase in change volume leads to instability."*

**Read that carefully, because it relocates the problem.** Throughput turning positive year-over-year means the *authoring* constraint has been relieved. Stability staying negative means the **absorptive capacity of the delivery system** — review, testing, rollback, observability — has not moved with it. That is the same structural claim the practitioner material arrives at independently: [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Claire Vo]] builds a risk-scoring reviewer because review, not authoring, is now the bottleneck, and [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Carson]] gates 40 daily PRs on a two-loop automated review plus a video he watches himself. DORA's prescription and their practice are the same prescription.

**Seven team profiles.** Cluster analysis yields seven archetypes, including **"Foundational challenges"** (survival mode — low performance, high instability, high burnout and friction) and **"Harmonious high achievers"** (strong across well-being, product outcomes, and delivery). The profiles are the operational form of the amplifier thesis: the same AI intervention lands differently depending on which cluster you are in.

**The DORA AI Capabilities Model** names seven capabilities that amplify AI's positive impact: clarify and socialise AI policies; connect AI to internal context; prioritise foundational practices; **fortify your safety nets**; invest in your internal platform; focus on end-users; plus one further capability in the model visual. Two framing insights sit behind them: **user-centricity is a prerequisite** (AI is most useful pointed at a clear problem), and **platform engineering is the foundation** — internal platform quality correlates directly with the ability to unlock AI value.

**Two other sources sit directly underneath these two numbers.** For throughput, [[2026-02-27-cui-demirer-generative-ai-high-skilled-work-three-field-experiments|Cui et al.]] give a pre-registered causal magnitude — +26.08% completed tasks across 4,867 developers — for the half of the story that turned positive. For stability, [[2026-03-30-liu-debt-behind-the-ai-boom|Liu et al.]] show what is physically accumulating in the repositories: 484,366 issues introduced across 302.6k AI-authored commits, 22.7% still present at the latest revision. DORA says the delivery system destabilises; Liu et al. say what is piling up inside it.

## Dynamic-capabilities reading

- **`digital-transforming/improving-digital-maturity`** — the capabilities model is a maturity ladder, and the report's claim is that position on it, not tool choice, determines the return.
- **`digital-transforming/redesigning-internal-structures`** — the platform-engineering finding is a structural prescription: build the internal platform before expecting AI leverage.
- **`contextual/internal-enablers`** — safety nets (automated testing, mature version control, fast feedback) are named as the conditions under which higher change volume does not become instability.
- **`contextual/internal-barriers`** — the seven profiles, especially "Foundational challenges," describe the barrier state directly: AI makes an already-unstable delivery system worse.

## Linked entities and concepts

- Entities: [[Google]], [[DORA]]
- Concepts: [[concepts/ai-coding-productivity-evidence|ai-coding-productivity-evidence]], [[concepts/agentic-pull-requests|agentic-pull-requests]], [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]], [[concepts/agentic-engineering|agentic-engineering]], [[concepts/micro-productivity-trap|micro-productivity-trap]]
- **Dangling** (single-source mention, deferred): Nathen Harvey, Derek DeBellis

## Scope and reliability

**The announcement blog post only** — the full report (including the complete seven-profile chapter and the seventh AI capability) was not converted. Cross-sectional self-report survey: the adoption, trust and perceived-productivity numbers are **beliefs**, and [[2025-07-10-becker-metr-early-2025-ai-experienced-developer-productivity|METR's RCT]] establishes that developer beliefs about AI productivity are systematically and substantially wrong. The **delivery** metrics (throughput, stability) are behavioural and more trustworthy. Published by Google Cloud, whose commercial interest runs toward both AI adoption and platform engineering; the stability finding cuts against that interest, which is a point in its favour. The 2024 baseline figures (1.5% / 7.2% per 25% adoption) come from the prior year's report and are carried here as context, not re-verified.
