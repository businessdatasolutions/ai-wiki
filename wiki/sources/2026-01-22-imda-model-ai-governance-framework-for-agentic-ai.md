---
type: source
kind: report
title: "Model AI Governance Framework for Agentic AI"
author: ["Infocomm Media Development Authority (IMDA)"]
publisher: "IMDA / Ministry of Digital Development and Information (MDDI), Singapore — announced at Davos"
url: "https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2026/new-model-ai-governance-framework-for-agentic-ai"
date_published: 2026-01-22
date_ingested: 2026-08-30
length: "announcement / press release only (~800 words); the framework document itself was not converted"
raw: "../../raw/reports/2026-01-22-imda-model-ai-governance-framework-for-agentic-ai.md"
tags: [imda, singapore, mddi, agentic-ai-governance, risk-bounding, human-accountability, technical-controls, whitelisting, end-user-responsibility, davos, regulation, first-mover]
dynamic_capabilities:
  - contextual/external-triggers
  - digital-transforming/redesigning-internal-structures
  - digital-sensing/digital-scenario-planning
relationships:
  - type: supports
    target: 2026-05-14-pochampally-assistant-or-actor-delegation-regret
    via: "regulation and human-factors evidence converging on the same control, four months apart. Pillar 2 requires defining checkpoints at which human approval is required; the delegation-regret study finds users demanding exactly those checkpoints and identifies the trigger as irreversibility combined with external visibility rather than stakes. The framework prescribes the control; the study supplies the placement rule"
    confidence: 0.8
  - type: supports
    target: 2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot
    via: "a commercial implementation of pillars 2 and 3 built without reference to the framework. Merge Mommy defines the approval checkpoint (escalate medium and high risk to a human in Slack) and makes the process *\"auditable, queryable, and in your risk policy\"* — the audit-trail property the framework's lifecycle controls require, arrived at through a SOC 2 argument rather than a regulatory one"
    confidence: 0.7
---

# IMDA — Model AI Governance Framework for Agentic AI

## TL;DR

Announced at Davos on **22 January 2026** and updated **20 May 2026**, this is presented as **the world's first governance framework specifically for agentic AI** — for systems that *take actions*, not just produce outputs. Singapore is doing what it did with the original Model AI Governance Framework in 2019: publishing a voluntary reference model early enough to shape how everyone else's rules get written.

**The four pillars, verbatim:**

1. *"Assessing and bounding the risks upfront by selecting appropriate agentic use cases and placing limits on agents' powers"*
2. *"Making humans meaningfully accountable for agents by defining significant checkpoints at which human approval is required"*
3. *"Implementing technical controls and processes throughout the agent lifecycle, such as baseline testing and controlling access to whitelisted services"*
4. *"Enabling end-user responsibility through transparency and education/training"*

**What is structurally interesting about this set.** Pillar 1 is **ex ante** — risk is bounded at the point of *use-case selection*, before deployment, by deciding what the agent is allowed to be for and what powers it holds. That is a materially different regulatory posture from the output-testing and disclosure regimes that dominate non-agentic AI governance, and it is the right one for systems whose failures are actions rather than statements. Pillar 2 makes **humans "ultimately accountable"** and operationalises it as *checkpoints*, not as general oversight — a checkpoint is a place, and places can be audited.

**The independent convergence is what makes this worth ingesting alongside the engineering material.** Nothing in the practitioner or academic sources here cites this framework, and yet:

- Pillar 1's *"placing limits on agents' powers"* is [[2026-07-25-darroman-profitable-founder-managing-ai-agents-25-prs-a-day|Carson keeping production credentials out of agent hands]]
- Pillar 2's approval checkpoints are [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Merge Mommy escalating medium- and high-risk PRs to Slack]] — and [[2026-05-14-pochampally-assistant-or-actor-delegation-regret|the delegation-regret study]] supplies the empirical rule for *where* to put them (irreversibility × external visibility)
- Pillar 3's *"controlling access to whitelisted services"* is the least-privilege posture arrived at independently by every practitioner in this ingest who touches production

**Four constituencies — a regulator, a solo founder, a product executive and a human-factors research group — converged on substantially the same control set.** That convergence is the strongest evidence in this ingest that the controls are load-bearing rather than cultural.

> **Terminology caution.** The announcement does **not** use the phrases *"least-privilege access"* or *"unique agent identity."* Pillar 3's *"controlling access to whitelisted services"* is the least-privilege idea in the framework's own words. Do not attribute either phrase to the framework without checking the full document.

## Dynamic-capabilities reading

- **`contextual/external-triggers`** — a first-mover regulatory instrument that will shape agentic-AI deployment norms well beyond Singapore, and that firms will be asked to map against.
- **`digital-transforming/redesigning-internal-structures`** — pillars 2 and 3 are organisational prescriptions: define approval checkpoints, instrument the agent lifecycle, control service access.
- **`digital-sensing/digital-scenario-planning`** — pillar 1's upfront risk-bounding *is* scenario planning as a governance requirement: decide what could go wrong before selecting the use case.

## Linked entities and concepts

- Entities: [[IMDA]]
- Concepts: [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]], [[concepts/responsible-ai|responsible-ai]], [[concepts/ai-agents|ai-agents]], [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]], [[concepts/attack-surface-management|attack-surface-management]]

## Scope and reliability

**The announcement only** — the framework document itself was **not converted**, so the pillars' sub-requirements, the worked examples, and any accompanying testing guidance were not read. The IMDA press-release page returned only navigation chrome to the fetcher; the pillar text quoted here comes from the **MDDI newsroom** version. **Voluntary and non-binding**: this is a model framework, not law, and its influence will come from adoption and from being cited in other jurisdictions' rulemaking — a mechanism whose effectiveness is not yet observable. The **20 May 2026 update** was noted but its contents were not retrieved; anyone relying on the framework should work from the current version rather than the launch announcement.
