---
type: entity
kind: organization
aliases: ["NVIDIA", "Nvidia"]
tags: [nvidia, gpu, semiconductors, nemotron, openshell, dgx, open-weight-models, jensen-huang, nvidia-research, small-language-models, slm]
since: 1993
confidence: 0.80
last_confirmed: "2026-09-04"
accessed_at: "2026-09-04"
source_count: 2
relationships:
  - type: supports
    target: small-language-models
    via: "NVIDIA Research authored the field's reference position paper arguing SLMs are the future of agentic AI — read alongside the CEO-level sovereign-AI argument, the company is on both sides of the how-much-compute-does-agentic-work-need question"
  - type: supports
    target: LangChain
    via: "joint Deep Agents + OpenShell blueprint (July 2026), pairing NVIDIA's Nemotron 3 Ultra model with LangChain's Deep Agents harness"
---

# NVIDIA

GPU and AI-accelerator maker founded 1993; led by founder and CEO **Jensen Huang**. Entered the wiki as a **central-subject first appearance** via [[2026-07-08-jensen-huang-why-companies-need-open-agent-systems|Huang's interview with Harrison Chase]] (LangChain YouTube channel, 8 Jul 2026), following the same first-appearance-as-central-subject precedent used for [[Khan Academy]] and [[PwC]]. NVIDIA had previously surfaced only in passing — named alongside AMD as general-purpose silicon in [[2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm|Nadella/Hoffman]] — before this substantive first-party source.

## Why NVIDIA matters in this wiki

NVIDIA's pitch, in Huang's words, is that **"most companies will be built on harnesses"** rather than business processes, and that every company's durable value is its own specialized, proprietary intelligence — which it must own and improve, not outsource. NVIDIA's role in that world is supplying the open substrate (models + runtime) enterprises specialize on top of, rather than owning the specialization itself. This positions NVIDIA as an **infrastructure/substrate vendor** in the wiki's [[agent-harness]] vocabulary — adjacent to, but distinct from, [[LangChain]]'s harness/framework layer.

## NVIDIA Research, and a tension inside the company (added 2026-09-04)

NVIDIA enters the wiki a second time from a different altitude: **NVIDIA Research** (with Georgia Tech) authored [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|*Small Language Models are the Future of Agentic AI*]] — the reference statement of the [[small-language-models|SLM position]], and the paper carried to practitioners in [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Sokolenko's PyCon DE talk]]. Authors: Peter Belcak, Greg Heinrich, Shizhe Diao, Yonggan Fu, Xin Dong, Saurav Muralidharan, Yingyan Celine Lin (Georgia Tech), Pavlo Molchanov.

Held next to [[2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai|Huang's sovereign-AI argument]], the two documents pull in opposite rhetorical directions and both are NVIDIA speaking. Research argues the industry over-provisions frontier LLMs for agentic work that a fine-tuned sub-10B model handles, and that the centralised-inference build-out (~USD 57bn) persists largely as inertia — its **barrier B1**. The CEO argues sovereign owners should build and own frontier-scale intelligence.

They are not strictly incompatible: one is about *which model serves each invocation*, the other about *who owns the stack*. And the commercial reading reconciles them — NVIDIA sells the accelerators for centralised frontier inference **and** the consumer/edge silicon that runs SLMs locally, so "more inference in more places" is the position both documents serve. Worth stating plainly whenever either is cited: **neither is a disinterested source on how much compute agentic work needs.**

## Products referenced in this wiki

- **Nemotron (Nemotron 3 Ultra)** — NVIDIA's open-weight large language model family. On an internal Deep Agents benchmark, Nemotron 3 Ultra scores 86% vs. Claude Opus's 87%, at roughly 10x lower cost than Opus — cited by Huang as evidence that open-weight models are reaching frontier performance at a fraction of the cost. Improved not just by scale but by harness-side tuning (prompts, tools) and, prospectively, by post-training the model *inside* the LangChain harness.
- **OpenShell** — a secure, open agent runtime; the deployment layer of the Deep Agents + OpenShell blueprint, providing sandboxing and access control so enterprise IT organizations can safely run agents.
- **The Deep Agents + OpenShell blueprint** — a joint NVIDIA + LangChain announcement (8 Jul 2026): running LangChain Deep Agents with Nemotron 3 Ultra inside OpenShell, packaging model + harness + runtime + acceleration stack as a reusable enterprise starting point for building domain-specific "super agents."
- **DGX Spark / DGX station** — NVIDIA hardware named as deployment targets for enterprise agent systems, alongside cloud and on-prem options.
- **Nemotron Coalition** — named as a founding-team collaboration between NVIDIA and LangChain on Nemotron Ultra; not yet substantively detailed in the wiki.
- **Nemotron-H** (2 / 4.8 / 9B) and **Hymba-1.5B** — the small end of the family, cited in NVIDIA Research's own SLM paper as evidence that hybrid Mamba–Transformer architectures reach 30B-class instruction-following and code generation at an order-of-magnitude fewer inference FLOPs.
- **NVIDIA Dynamo** — the distributed inference framework the SLM paper names as what reduces its barrier B1 (sunk investment in centralised LLM serving) *"to a mere effect of inertia"* by supporting high-throughput low-latency SLM inference in cloud and edge.

## People

- **Jensen Huang** — Founder and CEO. Central subject of [[2026-07-08-jensen-huang-why-companies-need-open-agent-systems|the interview]] but **dangling** (single-source, deferred) per the person-entity second-source promotion rule — central-subject status on a first appearance does not itself trigger person promotion (precedent: Sal Khan on the Khan Academy source). Promote on a second substantive Huang-authored or Huang-centric source.

## Concepts NVIDIA touches in this wiki

- [[agent-harness]] — substrate/infrastructure vendor supplying the open model + runtime layers that harnesses like LangChain Deep Agents wrap.
- [[enterprise-ai-adoption]] — the "companies built on harnesses, not business processes" thesis and the specialize-after-frontier decision rule.
- [[dynamic-capabilities]] — `digital-transforming/redesigning-internal-structures` and `digital-seizing/rapid-prototyping` per the source page's W&W tags.
- [[small-language-models]] — NVIDIA Research is the origin of the position; see the tension noted above.
- [[foundation-models]] — the device-indexed definition of "small" that the SLM paper contributes to the page's size axis.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "nvidia")
SORT file.name ASC
```

## Open questions

- **NVIDIA's own harness/runtime engineering practices** beyond the LangChain partnership — the wiki holds only this one vendor-collaboration vantage.
- **Nemotron Coalition** — named but not substantively detailed; an open ingest target if NVIDIA or LangChain publish more about the collaboration structure.
- **Jensen Huang's independent voice** — this source is a fireside interview co-framed by Chase; a Huang solo keynote or NVIDIA-first-party essay would be a useful independent second source for promoting Huang himself.
