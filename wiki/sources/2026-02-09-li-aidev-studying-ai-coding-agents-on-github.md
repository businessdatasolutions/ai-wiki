---
type: source
kind: paper
title: "AIDev: Studying AI Coding Agents on GitHub"
author: ["Hao Li", "Haoxiang Zhang", "Ahmed E. Hassan"]
publisher: "Queen's University (SAIL); MSR 2026; arXiv:2602.09185"
url: "https://arxiv.org/abs/2602.09185"
date_published: 2026-02-09
date_ingested: 2026-08-30
length: "abstract only (full paper not read)"
raw: "../../raw/papers/2026-02-09-li-aidev-studying-ai-coding-agents-on-github.md"
tags: [aidev, dataset, agentic-pr, github, msr-2026, codex, devin, copilot, cursor, claude-code, mining-software-repositories, mining-challenge]
dynamic_capabilities:
  - digital-sensing/digital-scouting
relationships:
  - type: supports
    target: 2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes
    via: "the dataset and one of the two MSR 2026 studies built on it. AIDev supplies the 932,791 agent-authored pull requests; Abujadallah et al. sample 306 non-merged PRs from it and find 46.41% of agent fixes rejected, with 14 reasons in four categories"
    confidence: 0.9
  - type: supports
    target: 2026-04-13-branco-lgtm-auto-merged-llm-agentic-prs
    via: "the dataset and the other MSR 2026 Mining Challenge study built on it. LGTM works the merged tail — what auto-merged agentic PRs look like — where Abujadallah et al. work the rejected tail. Together they cover both ends of the same population"
    confidence: 0.9
---

# Li, Zhang & Hassan — AIDev: Studying AI Coding Agents on GitHub

## TL;DR

The **population dataset** underneath the agentic-PR literature, and the reason the 2026 findings in this ingest are population statements rather than case studies.

| | |
| --- | ---: |
| Agent-authored pull requests ("Agentic-PRs") | **932,791** |
| Repositories | **116,211** |
| Developers involved | **72,189** |
| Agents covered | **5** — OpenAI Codex, Devin, GitHub Copilot, Cursor, Claude Code |
| Curated subset | **33,596** PRs from **2,807** repos with >100 stars, enriched with comments, reviews, commits and related issues |

**Why the numbers themselves are the finding.** Nearly a million agent-authored pull requests across 116,211 repositories is not an emerging practice — it is an established one, measured in early 2026. The involvement of **72,189 developers** is the other half: these PRs are landing in front of humans who have to do something about them. That is the volume that makes review capacity, not authoring capacity, the binding constraint — the premise [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Merge Mommy]] and [[2026-04-13-branco-lgtm-auto-merged-llm-agentic-prs|LGTM]] both start from.

**The curated subset is the methodological contribution.** 33,596 PRs from repositories with >100 stars, with comments, reviews, commits and linked issues attached, is what makes *qualitative* work on agent failure possible at all — it is the sampling frame [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes|Abujadallah et al.]] draw their 306 hand-coded rejections from.

**Note that the five agents named here are exactly the five that recur across this ingest** — Codex, Devin, Copilot, Cursor, Claude Code. The same products appear in [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Carson's stack]], in [[2025-11-26-gabor-evilgenie-reward-hacking-benchmark|EvilGenie's]] reward-hacking evaluation, and in [[2026-03-30-liu-debt-behind-the-ai-boom|Liu et al.'s]] technical-debt study. The corpus is converging on one small set of tools, which is convenient for cross-study comparison and a reason to be careful about generalising beyond them.

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`** — the dataset's entire function is making an emerging practice observable; it is scouting infrastructure for the research community.

## Linked entities and concepts

- Entities: [[GitHub]], [[OpenAI]], [[Anthropic]], [[Cursor]], [[Devin]], [[Cognition]], [[Claude Code]]
- Concepts: [[concepts/agentic-pull-requests|agentic-pull-requests]], [[concepts/agentic-engineering|agentic-engineering]], [[concepts/ai-agents|ai-agents]]
- **Dangling** (single-source mention, deferred): Hao Li, Haoxiang Zhang, Ahmed E. Hassan

## Scope and reliability

**Abstract only.** A dataset paper — it makes no causal claims and should not be cited for any. Coverage limits worth holding: **public GitHub only** (so no enterprise or private-repo behaviour), **five agents** (so no coverage of in-house or less popular tooling), and attribution depends on agents identifying themselves in PR metadata, which will undercount agent involvement where a human takes credit. The >100-star curated subset skews toward visible, well-maintained projects — which is precisely the population [[2026-04-13-branco-lgtm-auto-merged-llm-agentic-prs|LGTM]] finds *least* willing to auto-merge, so findings from the subset will understate laissez-faire practice in the long tail.
