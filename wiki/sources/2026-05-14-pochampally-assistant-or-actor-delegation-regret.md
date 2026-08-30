---
type: source
kind: paper
title: "Assistant or Actor? Student Trust, Control, and Delegation Regret When Using a General-Purpose AI Agent"
author: ["Shiva Pochampally", "Shengwei An", "Yan Chen"]
publisher: "arXiv:2607.18257"
url: "https://arxiv.org/abs/2607.18257"
date_published: 2026-05-14
date_ingested: 2026-08-30
length: "abstract only (full paper not read)"
raw: "../../raw/papers/2026-05-14-pochampally-assistant-or-actor-delegation-regret.md"
tags: [delegation-regret, trust-calibration, per-task-autonomy, reversibility, external-visibility, openclaw, human-agent-interaction, approval-preference, action-boundaries, qualitative-study]
dynamic_capabilities:
  - contextual/internal-barriers
  - digital-transforming/redesigning-internal-structures
relationships:
  - type: supports
    target: 2026-01-22-imda-model-ai-governance-framework-for-agentic-ai
    via: "the empirical finding and the regulatory prescription arriving at the same design, four months apart and from opposite directions. The framework's second pillar requires *\"defining significant checkpoints at which human approval is required\"*; this study finds users spontaneously demanding exactly that, and identifies the trigger — irreversibility combined with external visibility, not stakes alone. The framework says place checkpoints; this says where"
    confidence: 0.8
  - type: supports
    target: 2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot
    via: "the human-factors basis for two of Merge Mommy's six risk dimensions. Vo scores *reversibility* and *blast radius* as escalation triggers; this study finds irreversibility and external visibility are precisely what drive users to withdraw trust and demand approval, and that a high-stakes but *verifiable* task does not produce the same response. The scoring axes practitioners chose by instinct are the ones users actually react to"
    confidence: 0.75
---

# Pochampally, An & Chen — Assistant or Actor? Delegation Regret

## TL;DR

The paper that names the failure mode nobody had a word for.

> **Delegation regret**: "a pattern in which users regret not that the agent erred, but that it acted beyond what they would have authorized."

That distinction is the contribution. Every existing framework for agent quality measures **whether the agent was right**. This measures **whether the agent was authorised** — and the two come apart. Finding 3 is the sharp version: *"delegation regret appeared consistently when the agent executed actions without preview, even when the output was rated as successful."* **A correct outcome does not repair an unauthorised action.**

**Design.** 20 university students, five common daily tasks with an agent (**OpenClaw**), tasks chosen to vary in **privacy, stakes and reversibility**. Trust, perceived control, transparency, supervision burden and approval preference measured on 5-point Likert scales, plus thematic coding of free-text reflections.

**Three findings:**

1. **Trust is calibrated per task, not per agent.** Participants granted wide autonomy for advisory and low-stakes work and demanded confirmation for irreversible, externally visible actions. There is no such thing as "how much do you trust this agent" — the question is malformed. This is the empirical basis for **per-task autonomy policies**, and it is why a single global permission setting will always be wrong in both directions.

2. **Irreversibility × external visibility drives trust withdrawal — not stakes.** The moderate-stakes **email** task produced the sharpest trust drop (**M = 3.10**) and the highest approval demand (**M = 4.65**), while a *high*-stakes but **verifiable** task did not. Sending an email is not high-stakes; it is *unrecallable and seen by someone else*. That combination, not consequence magnitude, is what people actually guard.

3. **Preview is the mechanism, not permission.** Regret appeared whenever the agent acted without preview. The design implication is specific: it is not enough to have granted the agent permission in advance — users want to see what it is about to do.

**Why this belongs next to the software-engineering material.** [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Merge Mommy]] scores **reversibility** and **blast radius** among its six dimensions and escalates on them; [[2026-07-25-darroman-profitable-founder-managing-ai-agents-25-prs-a-day|Carson]] keeps production credentials out of agent hands and approves sensitive actions by hand; [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|his Land PR loop]] gates on **watching a video of what the agent did** before merging — which is preview, exactly as finding 3 prescribes. Practitioners converged on these controls commercially; this study explains why they feel necessary, and [[2026-01-22-imda-model-ai-governance-framework-for-agentic-ai|Singapore's regulator]] arrives at the same place from policy.

> **Terminology note.** The paper frames **trust calibration** and **per-task autonomy**. It does not use the phrase "span of control"; any manuscript attributing that phrase to this paper should be corrected.

## Dynamic-capabilities reading

- **`contextual/internal-barriers`** — delegation regret is an adoption barrier that persists *even when the agent works*, so it cannot be engineered away by improving quality.
- **`digital-transforming/redesigning-internal-structures`** — the design implications (expose action boundaries, per-task autonomy policies, separate advisory output from agentic execution) are structural prescriptions for how agent authority is organised.

## Linked entities and concepts

- Concepts: [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]], [[concepts/agent-fleet-management|agent-fleet-management]], [[concepts/responsible-ai|responsible-ai]], [[concepts/ai-agents|ai-agents]]
- **Dangling** (single-source mention, deferred): Shiva Pochampally, Shengwei An, Yan Chen

## Scope and reliability

**Abstract only.** **N = 20 university students, one agent, five tasks** — this is a mechanism-naming qualitative study, not a population estimate, and the Likert means (M = 3.10, M = 4.65) should be read as descriptive of this sample rather than as effect sizes. The student population is a real limit: professional users with accountability for outcomes may calibrate differently, plausibly *more* conservatively. The concept — delegation regret, and the irreversibility × visibility trigger — is the durable contribution and transfers well beyond the study's scope; the numbers do not.

**Date discrepancy, recorded rather than resolved:** the arXiv identifier is **2607.\*** (July 2026) while the listing page states a v1 submission of **Thu, 14 May 2026**. This page uses the stated submission date; the identifier is the citable handle.
