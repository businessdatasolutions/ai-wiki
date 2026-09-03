---
type: entity
kind: organization
aliases: ["Hugging Face", "HuggingFace", "🤗"]
tags: [hugging-face, open-source-ai, open-weight-models, model-hub, datasets, ai-builders, clem-delangue, nemotron, reachy, agentic-evals, github-for-ai]
since: 2016
confidence: 0.75
last_confirmed: "2026-09-03"
accessed_at: "2026-09-03"
source_count: 3
relationships:
  - type: supports
    target: 2026-07-08-jensen-huang-why-companies-need-open-agent-systems
    via: "Hugging Face's own platform (via CEO Delangue) and NVIDIA (via Huang) both argue enterprises should own rather than rent core AI intelligence; both cite the Nemotron open-weight family as evidence open models reach frontier performance cheaply"
---

# Hugging Face

Open-source AI platform founded **2016**, co-founded and led by CEO **Clément "Clem" Delangue** — the "**GitHub for AI**," where AI builders share and download open models and datasets. As of mid-2026 it hosts almost **3 million public models** and **1 million public datasets** (a new repository "every 7 seconds"), serves **16–17 million AI builders**, and is used by **roughly half the Fortune 500**. It entered the wiki twice: first as the `author:` of the [[2026-03-20-huggingface-agentic-evaluations-workshop|Agentic Evaluations Workshop]] (Mar 2026), then promoted to a full entity on its **second source**, the [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|TechCrunch Equity interview with Delangue]] (Jul 2026), where it is the central subject.

## Why Hugging Face matters in this wiki

Hugging Face is the wiki's clearest institutional embodiment of the **[[open-source-ai]]** stance and the **own-vs-rent** thesis (see [[agent-harness]]: "the model is what you rent, the harness is what you own"). Delangue's account of the enterprise flow — **frontier APIs for experimentation, owned/open models for production at scale** once cost bites — is the platform-CEO vantage on the same argument [[NVIDIA]]'s Jensen Huang makes from the silicon/substrate side ([[2026-07-08-jensen-huang-why-companies-need-open-agent-systems|Huang interview]]). Positioned in the wiki's vocabulary, Hugging Face is a **collaboration/distribution platform** (models + datasets + services, "part GitHub, becoming a bit AWS") sitting beneath the [[agent-harness]] layer — the ecosystem enterprises specialize *on top of*.

## Products and initiatives referenced in this wiki

- **The Hub** — the model/dataset/Space sharing platform itself; the "GitHub for AI" core.
- **Open LLM Leaderboard / LightEval / Inspect AI / GAIA 2 on the ARE environment** — the open-evaluation stack showcased in the [[2026-03-20-huggingface-agentic-evaluations-workshop|Agentic Evaluations Workshop]] (see [[ai-benchmarks]]).
- **Reachy / Reachy Mini** — Hugging Face's **open-source robots**; Delangue's evidence that robotics needs open source even more than the rest of AI (petabyte-scale video/image data; a home robot shouldn't be "a black box controlled by a few").
- **Spring 2026 report** — Hugging Face's own download analysis finding **Chinese models at ~41% of downloads**, surpassing the US (cited in the Delangue interview; see [[open-source-ai]]).
- **Model licensing initiatives** — a license type introduced "a few years ago" to give open-weight models more use-case clarity (legal-clarity contribution to the field).

## People

- **Clément "Clem" Delangue** — co-founder and CEO. Central subject of the [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|Equity interview]] but **dangling** (single-source, deferred) per the person-entity second-source promotion rule — central-subject status on a first appearance does not itself trigger person promotion (precedent: Jensen Huang, Sal Khan). Promote on a second substantive Delangue-authored or Delangue-centric source.

## Concepts Hugging Face touches in this wiki

- [[open-source-ai]] — the platform is the institutional anchor for the open-weight / own-vs-rent / AI-sovereignty / concentration-of-power theme.
- [[foundation-models]] — hosts and distributes open-weight foundation models (GLM 5.2, Nemotron, OpenAI's open GPT, and millions more).
- [[enterprise-ai-adoption]] — the frontier-experiment → owned-production adoption flow; half the Fortune 500 as users.
- [[ai-benchmarks]] — the open-evals / agentic-evaluation stack (GAIA 2, LightEval, Open LLM Leaderboard).
- [[dynamic-capabilities]] — `digital-scouting`, `balancing-digital-portfolios`, `navigating-innovation-ecosystems`, `business-model`, and `external-triggers` per the interview's W&W tags.

## Tao — an agent that teaches you to use other agents (2026-09-03)

[[2026-09-02-github-podcast-demystifying-ai-terms-loop-engineering-squads-harness|The GitHub Podcast, S02E02]] closes on open-source picks, and Mhangami's is **Tao**: *"a project from Hugging Face… a small Python project that is supposed to be an assistant that can help you learn more about coding agents. So it's a small agent, it's open source, it's built with Python, that mainly has information in it about using other coding agents."*

A minor mention, recorded because the category is not otherwise represented in the corpus: an open-source agent whose payload is **onboarding material for agentic tooling** rather than a capability of its own. It sits alongside this page's [[2026-03-20-huggingface-agentic-evaluations-workshop|agentic-evaluations workshop]] as Hugging Face's developer-education output rather than its model-hosting output. No detail beyond the description above is in the source; treat the project's scope as unverified.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "hugging-face")
SORT file.name ASC
```

## Open questions

- **Financials and independence** — Delangue reports no funding round in 3 years (~$400M raised), a declined Nvidia investment, and near-profitability. An independent source on Hugging Face's revenue/business model would let the wiki corroborate the capital-efficiency claims.
- **The Evox Productions copyright suit** (Hugging Face with Stability and Runway) — ongoing; a resolution or filing would be a useful [[responsible-ai]]/legal-risk ingest.
- **The Spring 2026 report** itself — cited secondhand via the interview; ingesting the primary report would substantiate the ~41%-China-downloads figure and the broader open-vs-closed trend data.
