---
type: concept
title: Agentic pull requests
aliases: ["agentic pull requests", "agentic PRs", "agent-authored PRs", "Agentic-PR", "auto-merge", "AI code review"]
confidence: 0.85
last_confirmed: "2026-09-19"
source_count: 11
accessed_at: "2026-09-19"
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

## Two opposite conventions, in one episode (added 2026-09-16)

[[2026-07-06-google-cloud-agent-factory-intent-driven-development|The Agent Factory, July 2026]] puts two practices for agent-authored PRs side by side, twenty minutes apart, without noticing that they point in opposite directions.

**Make authorship conspicuous.** [[YK Sugi]]'s convention: have the agent open the PR as a **draft**, review it, then mark it ready.

> *"You can just ask the agent to create a draft PR… and then check it before marking it as ready for review so that people will [know] OK, this PR maybe was created by the agent. It's not ready for review yet."*

This is an **out-of-band provenance marker built from existing GitHub semantics** — no new tooling, no bot, no label taxonomy. Given that this page's central finding is that reviewer attention is the scarce resource, a zero-cost signal that says *"do not spend attention here yet"* is a cheaper intervention than anything else the corpus records.

**Make authorship invisible.** [[Lydia Hallie]] describes the opposite as standard practice inside [[Anthropic]] — the Claude GitHub app installed across their repositories, so that

> *"if your CI fails or someone leaves a comment, Claude will automatically try to fix it until your CI is green."*

with the stated goal *"to be as out of the loop as possible."* A teammate's review comment becomes an input to an automated fix loop rather than a request to a human author.

**The conflict is about what green CI certifies.** Making a passing pipeline the loop's terminal state assumes CI failure is the failure mode. [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes|Abujadallah et al.]] find **46.41%** of agent-proposed fixes rejected across four categories, only one of which is CI/test failure — *incorrect implementation* and *low priority* are both invisible to a green pipeline, and this page's existing `contradicts` edge to [[reward-hacking]] says a passing suite is precisely what an optimising agent produces either way. An auto-fix loop that halts on green therefore halts on the signal least able to distinguish a good fix from a plausible one.

The reconciliation neither speaker offers is the one [[agent-oversight-and-delegation]] has converged on: **calibrate to consequence and reversibility.** Draft PRs for changes that reach production; auto-fix for CI-green plumbing. Both conventions are defensible inside their band and neither is defensible as a default.

## CI speed as the ceiling on agent PR throughput (added 2026-09-18)

[[2026-05-11-nystrom-how-i-ai-spec-driven-development-notion|Nystrom and Vo (How I AI, May 2026)]] put the constraint upstream of review. An agent facing an hour-long CI run "is just going to sit there and spin"; at three minutes, a human and "your little swarm of agents" get far more done. Vo cites Stripe's roughly 1,300 agent PRs a week — "you like cannot do that if your CI is slow" — and states it as a rule: there is "a true mathematical limit on your capacity to ship code to production that is a reflection of how fast your CI pipeline is." Notion's response is a project (Afterburner) to cut CI time to a quarter. The episode also shows an agent PR produced from a four-sentence task comment in about ten minutes, and the reviewer's reply to a CI type error was simply "I don't get it."

## AI review on every merge request, at company scale (added 2026-09-19)

The review-capacity bottleneck this page describes has a large-scale response on record. At Cloudflare, per [[2026-06-09-cloudflare-investor-day-2026|Cloudflare Investor Day 2026]], **every merge request** on the standard CI pipeline gets an AI review. Up to **seven specialised agents** (security, performance, code quality, documentation, compliance and others) run in parallel, and *"a top-tier model"* coordinates them and posts a single structured review. The first 30 days:

| Reviews | Merge requests | Repos | Median time | Median cost | Coverage |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 131,246 | 48,095 | 5,169 | 3 min 39 s | $0.98 | 100% |

Two things this adds. First, a **unit cost** for machine review, under a dollar per review, which puts the economics of the gate on the page for the first time. Second, the architecture: **specialist reviewers per concern, merged by a coordinator**, which is the multi-dimension scoring of [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Merge Mommy]] run as separate agents. It is the same answer Adobe's security leader reached from the other direction in [[2026-09-10-alim-pydata-ai-security-paradox-asymmetric-threats|Alim's talk]]. Loading every team's guidance into the *authoring* agent crowds its context, so checking each concern in a separate *reviewing* agent keeps it out of the authoring agent's context.

What the deck does not report is the outcome: how many reviews found something real, how many were dismissed, and whether change failure rates moved. Coverage and cost describe the gate, not what it catches.
