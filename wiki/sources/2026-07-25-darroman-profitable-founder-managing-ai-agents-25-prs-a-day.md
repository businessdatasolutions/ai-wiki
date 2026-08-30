---
type: source
kind: article
title: "Managing AI Agents: How One Founder Ships 25 PRs a Day, Solo"
author: ["Florian Darroman"]
publisher: "Profitable Founder"
url: "https://www.profitablefounder.xyz/blog/managing-ai-agents"
date_published: 2026-07-25
date_ingested: 2026-08-30
length: "~1,400 words (web extract)"
raw: "../../raw/articles/2026-07-25-darroman-profitable-founder-managing-ai-agents-25-prs-a-day.md"
tags: [ryan-carson, untangle, devin, cloud-agents, agent-fleet-management, decision-fatigue, standing-automations, watchdog, self-improvement-loop, token-economics, model-routing, parent-child-agents, grace, solo-founder]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-seizing/balancing-digital-portfolios
  - strategic-renewal/business-model
relationships:
  - type: supports
    target: 2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder
    via: "the same operating system written up a month earlier by a different interviewer. This piece is the quantitative half — the 25-minute check cadence, 3-of-25 pinned threads, ~$60 per end-to-end signup run, ~$5 per grading session, ~3 loop-generated fixes a day, and the ~$5k/month-per-engineer-equivalent target the $20k spend is supposed to fall toward. The episode is the qualitative half"
    confidence: 0.9
  - type: supports
    target: 2026-05-19-garg-yc-internal-ai-agent-evolves-itself
    via: "a shipped instance of the self-improving-agent pattern, with the economics attached. Carson's third standing automation grades yesterday's Grace conversations against a rubric and spawns child agents that open fix PRs — the same overnight-improvement loop, but bounded to a *quality* rubric on one product surface rather than aimed at the product itself, which is exactly the boundary Carson defends in the How I AI episode"
    confidence: 0.7
---

# Darroman — Managing AI Agents: How One Founder Ships 25 PRs a Day, Solo

## TL;DR

A **third-party write-up of [[Ryan Carson]]'s operating system at [[Untangle]]**, published a month before the *[[How-I-AI|How I AI]]* episode that covers the same ground. It earns its own page because it is the **numerate** version: where the episode gives reasoning and on-screen demonstration, Darroman extracts the cadences, the per-run costs, and the target unit economics. Carson ships **22–25 PRs a day, sometimes 40**, alone.

**1. Cloud over local — the same hard line, with the mechanism named.** *"If you are working locally, I honestly think you are a caveman."* The argument is about collisions: cloud agents give **an isolated virtual machine per session**, so parallel work scales horizontally. Carson runs **5–10 cloud agents simultaneously** — "at least 5, often 10." The article makes the structural point explicitly: **the PR volume comes from many ordinary agents in parallel, not from one very good agent.** That is the same primitive Geng & Neubig isolate and test as *isolated workspaces* in [[2026-03-23-geng-neubig-caid-asynchronous-software-engineering-agents]].

**2. Decision load explodes before output does — the article's best contribution.** Where a developer might make 2–3 high-stakes decisions a day, Carson faces **10–20 before lunch**. The countermeasures are all *attention-rationing* devices rather than tooling:

- **Pin priority threads** — only **3 of ~25 daily PRs** get focused attention
- **A 25-minute check cadence** — bounded review intervals, not continuous supervision
- **A paper to-do list** for the week's priorities
- **Roughly half his work from an iPhone browser**
- **Agents never hold production credentials**; sensitive actions are approved by hand

The last of these is a **least-privilege posture arrived at by a practitioner from operational necessity**, matching what Singapore's regulator prescribes from first principles in [[2026-01-22-imda-model-ai-governance-framework-for-agentic-ai]] — its third pillar being technical controls including access limited to whitelisted services.

**3. Three standing automations ("sleeping automations").**

| Automation | Cadence | What it does | Cost |
| --- | --- | --- | ---: |
| End-to-end signup test | 3× weekly | Agent completes the full signup workflow, records video, identifies bugs, files fixes | **~$60/run** |
| Production watchdog | Daily, 9am | Reviews previous 24h of customer activity; summarises insights and anomalies with session links | — |
| Self-improvement loop | Daily | Grades **Grace** (Untangle's AI paralegal) conversations against a quality rubric; substandard interactions trigger child agents that open fix PRs | **~$5/session; ~3 fixes ship/day** |

**4. Token economics, and the number that matters.** Current spend **$20,000/month**, which Carson calls unsustainable; the estimated sustainable level is **~$5,000/month per engineer-equivalent**. The route from one to the other is **model routing** — frontier models for complex reasoning, fine-tuned coding models for repetitive work — enforced structurally through **parent–child agent patterns** that keep premium models off routine tasks. His business-model prediction: **$200/month all-you-can-eat plans will not survive**, and he favours independent platforms (Devin, Factory, Amp) that optimise model economics for production use rather than for a subscription price point.

**5. An implementation ladder.** Run one cloud agent session → run three simultaneously → build one automation (**the production watchdog is named as the highest-signal entry point**) → add a quality-grading loop on your core product surface. This is the most actionable on-ramp in the practitioner material, and it deliberately puts *observability* before *autonomy*.

**Core thesis:** managing AI agents is the emerging founder skill set; technical depth now develops through **delegation and judgement** rather than through typing lines of code.

The third automation is a shipped instance of the self-improving-agent pattern documented at [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|Garg / YC]] — with the important difference that Carson's loop is bounded to a **quality rubric on one product surface** rather than aimed at the product itself, which is the boundary he defends explicitly in the *How I AI* episode.

## Dynamic-capabilities reading

- **`digital-transforming/redesigning-internal-structures`** — the three standing automations replace what would otherwise be QA, customer success, and quality-assurance functions; the article is explicit that agents substitute for hires.
- **`digital-seizing/balancing-digital-portfolios`** — model routing and parent–child patterns are literally portfolio balancing at the inference layer: expensive capability reserved for where it changes the outcome.
- **`strategic-renewal/business-model`** — both Untangle's own model (one person, venture-scale SaaS) and Carson's prediction about agent-vendor pricing are business-model claims.

## Linked entities and concepts

- Entities: [[Ryan Carson]], [[Untangle]], [[Devin]], [[Cognition]]
- Concepts: [[concepts/agent-fleet-management|agent-fleet-management]], [[concepts/agentic-pull-requests|agentic-pull-requests]], [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]], [[concepts/agentic-engineering|agentic-engineering]]
- **Dangling** (single-source mention, deferred): Florian Darroman

## Scope and reliability

**Secondary reporting on a single self-reporting practitioner.** Darroman is summarising Carson's public accounts, not measuring anything; every figure traces back to Carson. Where this page and [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|the episode]] disagree — "5–10 agents" here versus "10, 15 threads" and "15 agents" there, "22–25 PRs" here versus "40 PRs" there — the discrepancy is a month of drift plus loose counting of *threads* versus *concurrently running agents*, not a contradiction worth resolving. Use the ranges, not the point estimates.
