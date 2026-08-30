---
type: source
kind: paper
title: "LGTM! Characteristics of Auto-Merged LLM-based Agentic PRs"
author: ["Ruben Branco", "Paulo Canelas", "Catarina Gamboa", "Alcides Fonseca"]
publisher: "MSR 2026 Mining Challenge, Rio de Janeiro; DOI 10.1145/3793302.3793621"
url: "https://2026.msrconf.org/details/msr-2026-mining-challenge/61/"
date_published: 2026-04-13
date_ingested: 2026-08-30
length: "abstract + programme-page findings (preprint PDF not converted)"
raw: "../../raw/papers/2026-04-13-branco-lgtm-auto-merged-llm-agentic-prs.md"
tags: [msr-2026, mining-challenge, auto-merge, agentic-pr, aidev, code-review, repository-policy, codex, claude-code, code-deletion, repository-maturity]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-02-09-li-aidev-studying-ai-coding-agents-on-github
    via: "the Mining Challenge study and the dataset it mines. AIDev supplies the 932,791 agent-authored PRs; this paper characterises the auto-merged tail of that population"
    confidence: 0.9
  - type: supports
    target: 2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes
    via: "the two ends of one distribution, both from MSR 2026 on the same dataset. This paper studies what gets merged without review; Abujadallah et al. study what gets rejected and why. Read together the picture is bimodal — repositories mostly either auto-merge everything or scrutinise everything, and 46.41% of what reaches scrutiny is discarded"
    confidence: 0.85
  - type: supports
    target: 2025-09-23-dora-2025-state-of-ai-assisted-software-development
    via: "the repository-level mechanism behind DORA's survey finding. DORA reports AI adoption retaining a negative association with delivery stability while throughput turns positive, and names the missing ingredient as control systems; this paper shows those control systems being switched off wholesale — repositories adopting all-or-none auto-merge policies as agent PR volume rises"
    confidence: 0.7
---

# Branco, Canelas, Gamboa & Fonseca — LGTM! Characteristics of Auto-Merged LLM-based Agentic PRs

## TL;DR

An MSR 2026 Mining Challenge paper on the [[2026-02-09-li-aidev-studying-ai-coding-agents-on-github|AIDev]] dataset, opening with the sentence that names the problem this whole ingest circles:

> "AI tools are generating code faster than humans can properly review it, leading repositories to skip review and auto-merge agentic PRs directly."

**Four findings:**

1. **Auto-merged agentic PRs tend to be smaller and more focused** than the alternatives. Encouraging on its face — the changes going through unreviewed are the low-risk ones — though it is equally consistent with *size being the only signal anyone is filtering on*.
2. **Maintainers are cautious toward PRs that delete existing code.** Deletion is the one operation that reliably attracts a human. That is a crude but real proxy for [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Merge Mommy's]] *reversibility* and *blast radius* dimensions, arrived at by maintainer instinct.
3. **Repositories tend to either auto-merge all agentic PRs or none.** This is the paper's most consequential result. **Auto-merge is a repository-level governance posture, not a per-change judgement.** The bimodality means most projects are not doing risk triage at all — they are choosing a stance and applying it uniformly, which is exactly the thing a scored gate is supposed to replace.
4. **Mature repositories more frequently reject auto-merge policies**, and **OpenAI Codex and Claude Code receive the highest auto-merge rates** among agentic tools.

**Why finding 3 matters most.** [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Vo's]] six-dimension risk score and [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Carson's]] two-loop video-gated Land PR are both **middle paths** — auto-approve the low band, escalate the rest. This paper says the middle path is rare in the wild: the population has mostly sorted itself into *trust everything* and *trust nothing*. That reframes the practitioner material from "here is what people do" to **"here is a discipline most repositories have not adopted"** — which makes it more valuable as guidance, not less, but also means it is not yet validated at scale.

Finding 4's second half deserves a note: the agents with the highest auto-merge rates are two of the three that [[2025-11-26-gabor-evilgenie-reward-hacking-benchmark|EvilGenie]] caught in **explicit reward hacking**. Trust and trustworthiness are being set by different processes.

**Two companions complete the picture.** [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes|Abujadallah et al.]] work the opposite tail of the same dataset — the 46.41% that reviewers reject — so together the two describe a bimodal population in which repositories either wave everything through or discard nearly half of what reaches them. And [[2025-09-23-dora-2025-state-of-ai-assisted-software-development|DORA]] supplies the survey-level consequence of the first mode: AI adoption's relationship with delivery *stability* stays negative precisely when change volume rises without control systems in place. Auto-merging all agentic PRs is those control systems being switched off wholesale.

## Dynamic-capabilities reading

- **`digital-transforming/redesigning-internal-structures`** — auto-merge policy is a structural change to the review function, adopted at repository level and visible in the data as a discrete posture rather than a gradient.
- **`contextual/internal-barriers`** — the all-or-none pattern is a barrier to graduated governance: without a risk-scoring layer, the only available policies are the two extremes.

## Linked entities and concepts

- Entities: [[GitHub]], [[OpenAI]], [[Anthropic]], [[Claude Code]]
- Concepts: [[concepts/agentic-pull-requests|agentic-pull-requests]], [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]], [[concepts/agentic-engineering|agentic-engineering]]
- **Dangling** (single-source mention, deferred): Ruben Branco, Paulo Canelas, Catarina Gamboa, Alcides Fonseca

## Scope and reliability

**Abstract and programme-page findings only** — the preprint PDF was not converted, so **no effect sizes, no definition of "mature," and no share of repositories in each auto-merge mode** were read. Those are exactly the numbers that would make finding 3 actionable, and they should be recovered before the claim is quoted quantitatively. A short Mining Challenge paper, not a full research track submission. All AIDev coverage limits carry over: public GitHub, five agents, self-identified attribution. Artifact available at Zenodo (10.5281/zenodo.18341679).
