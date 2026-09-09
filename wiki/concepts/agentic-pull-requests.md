---
type: concept
title: Agentic pull requests
aliases: ["agentic pull requests", "agentic PRs", "agent-authored PRs", "Agentic-PR", "auto-merge", "AI code review"]
confidence: 0.85
last_confirmed: "2026-08-30"
source_count: 8
accessed_at: "2026-09-01"
tags: [agentic-pr, aidev, auto-merge, code-review, rejection-rate, risk-scoring, msr-2026, merge-queue, review-bottleneck, technical-debt]
relationships:
  - type: part-of
    target: agentic-engineering
  - type: depends-on
    target: agent-oversight-and-delegation
  - type: caused
    target: ai-generated-code-quality
  - type: contradicts
    target: reward-hacking
    via: "the auto-merge pipeline's premise is that a passing CI run is sufficient evidence of a correct change; the reward-hacking literature shows a passing test suite is precisely what an optimising agent produces whether or not the change works"
    confidence: 0.75
quality_score: 1
---

# Agentic pull requests

Pull requests **authored by AI coding agents** rather than by humans — and the review, merge and governance machinery that has grown up around them. As of early 2026 this is measurable at population scale, which makes it one of the few areas in this corpus where the practitioner claims can be checked against data.

## Scale

[[2026-02-09-li-aidev-studying-ai-coding-agents-on-github]] (the **AIDev** dataset) is the reference population:

| | |
| --- | ---: |
| Agent-authored PRs | **932,791** |
| Repositories | **116,211** |
| Developers involved | **72,189** |
| Agents | **5** — OpenAI Codex, Devin, GitHub Copilot, Cursor, Claude Code |

Nearly a million agent-authored PRs across 116k repositories is an established practice, not an emerging one. The 72,189 developers are the other half of the story: these land in front of humans who must do something about them.

## The bottleneck moved

Once agents author most changes, **review capacity — not authoring capacity — is the constraint.** [[2026-04-13-branco-lgtm-auto-merged-llm-agentic-prs]] opens on it: *"AI tools are generating code faster than humans can properly review it, leading repositories to skip review and auto-merge agentic PRs directly."* [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Claire Vo]] built a bot for exactly this reason; [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Carson]] ships ~40 PRs a day with *"no QA team reviewing a single one."* [[2025-09-23-dora-2025-state-of-ai-assisted-software-development|DORA]] sees the consequence at survey scale: throughput's relationship with AI adoption turned positive in 2025 while **delivery stability's remained negative** — volume is no longer the problem; the delivery system's absorptive capacity is.

## What actually happens to them

**Rejection is close to a coin flip.** [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes]]: **46.41% of fixes proposed by Copilot, Devin, Cursor and Claude are rejected**, in **14 reasons across 4 categories** — incorrect implementation, CI/test failure, agent unable to implement, and **low priority**. That fourth category is not an agent failure at all: the fix was fine and nobody wanted it. Rejected work is not free — it consumes reviewer attention, CI capacity and tokens.

**What merges without review is small and additive.** [[2026-04-13-branco-lgtm-auto-merged-llm-agentic-prs]]: auto-merged agentic PRs are **smaller and more focused**; maintainers are **cautious toward PRs that delete code**; **OpenAI Codex and Claude Code get the highest auto-merge rates**; and **mature repositories more often reject auto-merge policies** altogether.

**Governance is bimodal, and that is the most consequential finding.** *"Repositories tend to either auto-merge all agentic PRs or none."* Auto-merge is a **repository-level posture, not a per-change judgement**. The graduated middle path that [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Merge Mommy]] and [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Land PR]] represent is **rare in the wild** — which makes the practitioner material more valuable as guidance and less valid as description.

**What survives review still carries debt.** [[2026-03-30-liu-debt-behind-the-ai-boom]]: across 302.6k AI-authored commits in 6,299 repositories, **484,366 issues introduced**, **89.3% code smells**, **>15% of commits from every assistant** introducing at least one issue, and **22.7% still present at the latest revision**.

## The emerging gate design

The practitioner pattern that recurs is **risk-scored partial autonomy**: score each change, auto-approve a low band, escalate the rest to a human. [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Merge Mommy's]] six dimensions are the most explicit statement of the axes —

**blast radius · reversibility · data security · ops impact · verification gap · change surface**

Two of these have independent support. **Reversibility** and external visibility are what [[2026-05-14-pochampally-assistant-or-actor-delegation-regret]] finds actually drive humans to withdraw trust from an agent (more than stakes do), and both are what [[2026-01-22-imda-model-ai-governance-framework-for-agentic-ai|Singapore's framework]] would place a human checkpoint on. **Verification gap** is the practitioner name for the quantity [[2026-05-20-zhao-specbench-reward-hacking-long-horizon-coding-agents|SpecBench]] formalises and shows growing 28 points per tenfold increase in code size.

[[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Carson's Land PR]] is the same idea with a different gate: fresh agent review, up to two loops, then a **narrated video walkthrough with a red/green test list** that he watches before approving the merge. That is *preview*, which [[2026-05-14-pochampally-assistant-or-actor-delegation-regret|the delegation-regret study]] identifies as the specific thing whose absence produces regret even on successful outputs.

## What would make agentic PRs land better

[[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes|The rejection study's]] prescriptions: hint the approach, state forbidden approaches, instruct on CI validation without breaking changes, and **prioritise properly**. The first two align with [[2026-02-12-gloaguen-evaluating-agents-md-repository-level-context-files]], which finds that **instructions** in context files are followed while **repository overviews** are not helpful and cost >20% more inference. Specific procedural constraint earns its tokens; general background does not.

## Related concepts

[[concepts/agentic-engineering|agentic-engineering]], [[concepts/agent-fleet-management|agent-fleet-management]], [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]], [[concepts/ai-generated-code-quality|ai-generated-code-quality]], [[concepts/reward-hacking|reward-hacking]], [[concepts/ai-coding-productivity-evidence|ai-coding-productivity-evidence]].

## Debates and supersession

- **Is 46.41% rejection bad?** It is a rejection rate among *opened* PRs, not a defect rate, and the "low priority" category shows some rejections are targeting failures rather than quality failures. Against that, human PR rejection rates in comparable open-source projects are not reported in any source here, so **there is no baseline** — the number is alarming without being interpretable. **Open.**
- **Do practitioner gates generalise?** [[2026-04-13-branco-lgtm-auto-merged-llm-agentic-prs]] finds the wild is bimodal and mature repositories decline auto-merge. Neither [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Merge Mommy]] nor Land PR reports a **false-approve rate**, which is the only number that would establish whether the low-risk band is actually low-risk. **Open.**
- **All population data is public GitHub, five agents, self-identified attribution.** Enterprise and private-repo behaviour is entirely unobserved.
