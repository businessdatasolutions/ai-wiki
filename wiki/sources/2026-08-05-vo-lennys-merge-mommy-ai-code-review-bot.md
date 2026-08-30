---
type: source
kind: article
title: "Build an AI code review bot in 30 minutes"
author: ["Claire Vo"]
publisher: "Lenny's Newsletter / How I AI"
url: "https://www.lennysnewsletter.com/p/build-an-ai-code-review-bot-in-30"
date_published: 2026-08-05
date_ingested: 2026-08-30
length: "~900 words (web extract) — companion to a How I AI video episode dated 4 Aug 2026"
raw: "../../raw/articles/2026-08-05-vo-lennys-build-an-ai-code-review-bot-in-30-minutes-merge-mommy.md"
tags: [claire-vo, merge-mommy, vercel-eve, codex, code-review, risk-scoring, auto-merge, blast-radius, reversibility, slack, github, soc2, intercom, agentic-pull-requests]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
  - digital-transforming/redesigning-internal-structures
  - contextual/internal-enablers
relationships:
  - type: supports
    target: 2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder
    via: "two solutions to the same bottleneck, described to each other in that episode. Once agents author most PRs, review capacity — not authoring capacity — is the constraint. Vo scores risk on six dimensions and auto-approves the low band; Carson gates on a narrated video walkthrough from a two-loop Devin Review. Both keep a human on the high-risk tail, and neither auto-merges everything"
    confidence: 0.85
  - type: supports
    target: 2026-04-13-branco-lgtm-auto-merged-llm-agentic-prs
    via: "the practitioner instance and the population study of the same phenomenon, four months apart. LGTM's framing sentence — *\"AI tools are generating code faster than humans can properly review it, leading repositories to skip review and auto-merge agentic PRs directly\"* — is precisely the problem Merge Mommy exists to solve, and Merge Mommy is the disciplined version of the behaviour LGTM finds in the wild: risk-scored partial auto-merge, rather than the all-or-none repo-level policy LGTM observes most repositories adopting"
    confidence: 0.8
  - type: supports
    target: 2026-01-22-imda-model-ai-governance-framework-for-agentic-ai
    via: "an unwitting implementation of the framework's second pillar — *\"defining significant checkpoints at which human approval is required\"* — arrived at commercially rather than from regulation. Vo's six risk dimensions include reversibility and blast radius, the same two axes the framework and the delegation-regret literature both converge on as the ones that should trigger a human checkpoint"
    confidence: 0.7
---

# Vo — Build an AI code review bot in 30 minutes (Merge Mommy)

## TL;DR

**[[Claire Vo]]** built **Merge Mommy**, a pull-request review agent, to solve the bottleneck that appears once AI writes most of the code: **review capacity, not authoring capacity, becomes the constraint.** The build is the point — one **Codex** session, one prompt plus "a few steering turns," on **Vercel Eve**, which she calls *"the simplest framework I've found for deploying AI agents in Slack and GitHub."* Chrome browser automation handled the Slack-bot and GitHub-app configuration. She argues the result is SOC 2-compatible because *"the process is auditable, queryable, and in your risk policy"* — the audit trail is a byproduct of the agent writing down its score.

**The loop, in four steps:**

1. **Read** each PR once its CI checks pass
2. **Score** it across six risk dimensions
3. **Auto-approve** the low-risk band
4. **Escalate** medium and high risk to Slack for a human decision (two clicks to merge)

**The six risk dimensions** — the transferable artifact here, and the reason this page exists:

| Dimension | What it asks |
| --- | --- |
| **Blast radius** | How much of the system does this touch if it's wrong? |
| **Reversibility** | Can this be rolled back cleanly? |
| **Data security** | Does it touch secrets, PII, or access boundaries? |
| **Ops impact** | Does it change runtime, deploy, or infrastructure behaviour? |
| **Verification gap** | How much of this change is *not* covered by the tests that just passed? |
| **Change surface** | How large and how diffuse is the diff? |

Two of these — **reversibility** and **blast radius** — are the same axes that [[2026-05-14-pochampally-assistant-or-actor-delegation-regret]] finds empirically drive users to withdraw trust from an agent, and that [[2026-01-22-imda-model-ai-governance-framework-for-agentic-ai]] prescribes as the basis for placing human checkpoints. **Verification gap** is the most interesting of the six because it is the only one that treats *the passing test suite itself* as incomplete evidence — the exact failure mode [[2026-05-20-zhao-specbench-reward-hacking-long-horizon-coding-agents]] measures as the reward-hacking gap.

**Outcomes claimed:** cleared Vo's PR backlog on deployment. She cites Intercom as a comparison point — *"5x'd PR approval speed and reduced revert rates"* after putting AI into their review process.

**The counterpart gate.** [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Ryan Carson's Land PR playbook]] — described to Vo in the episode two weeks later — solves the same bottleneck by the opposite route: instead of a scored risk band, it runs a fresh agent review with up to two loops and then produces a narrated video walkthrough the human watches before approving the merge. Scored triage and mandatory preview are two answers to one question, and neither auto-merges everything.

## Dynamic-capabilities reading

- **`digital-seizing/rapid-prototyping`** — the headline claim is 30 minutes from idea to a deployed, production-facing governance agent, in one Codex session. The build cost being near zero is what makes a bespoke risk policy viable at all.
- **`digital-transforming/redesigning-internal-structures`** — this is a review *policy* encoded as software: the decision of which changes need a human is moved out of team norms and into a scored, auditable pipeline.
- **`contextual/internal-enablers`** — the SOC 2 argument is the enabling condition: the bot is adoptable in a regulated shop precisely because its reasoning is written down and queryable.

## Linked entities and concepts

- Entities: [[Claire Vo]], [[How-I-AI]], [[Lenny's Podcast]], [[OpenAI]], [[GitHub]]
- Concepts: [[concepts/agentic-pull-requests|agentic-pull-requests]], [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]], [[concepts/agent-fleet-management|agent-fleet-management]], [[concepts/agentic-engineering|agentic-engineering]]

## Scope and reliability

**A build log by its author, published on her own show's newsletter.** No evaluation of the scorer's accuracy: nothing here reports how often Merge Mommy auto-approves a change that later reverts, which is the only number that would establish whether the low-risk band is actually low-risk. The Intercom figure is second-hand and uncited. The six dimensions are worth adopting as a **checklist**; the auto-approve threshold is not worth adopting without measuring your own false-approve rate against it — particularly given that [[2026-04-13-branco-lgtm-auto-merged-llm-agentic-prs]] finds mature repositories systematically *declining* auto-merge policies.
