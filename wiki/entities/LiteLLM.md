---
type: entity
kind: library
aliases: ["LiteLLM", "litellm"]
tags: [litellm, agent-harness, model-routing, observability, llm-tooling, open-source]
confidence: 0.75
last_confirmed: "2026-06-26"
accessed_at: "2026-06-26"
source_count: 2
relationships:
  - type: part-of
    target: agent-harness
    via: "the model-API abstraction / routing seam of the harness's swappable model layer; the OpenAI-compatible interface a harness calls instead of a vendor SDK directly"
---

# LiteLLM

An **open-source Python library** that exposes a single **OpenAI-compatible interface** over many LLM providers, so application code calls one `completion()` API and swaps the underlying model/provider by configuration rather than by rewriting integration code. It is the model-routing seam practitioners reach for when they want the "rented, swappable model" property of an [[agent-harness]] to be a config change rather than a code change.

## Why LiteLLM matters in this wiki

LiteLLM is a concrete instance of the **model layer's swap-not-marriage** discipline the [[agent-harness]] concept argues for: by routing every model call through one OpenAI-compatible surface, the harness keeps its [[foundation-models|foundation-model]] dependency loose. Two wiki sources cite it, from two different angles:

- **[[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe 2026]]** inlines the Sierra-published τ-bench `solve()` loop built on `litellm.completion()` — the wiki's first concrete worked example of *the agentic loop as a Python function*, and the reason LiteLLM first entered the corpus as a dangling mention.
- **[[2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail|InfoQ "From Demo to Production" 2026]]** names LiteLLM as the **model-call capture point paired with [[Langfuse]]** for observability — every request/response routed through LiteLLM becomes traceable, feeding the harness's observability layer. This second mention crossed the second-source threshold for entity promotion (per CLAUDE.md §Author-entity promotion, applied to recurring named tools).

The pairing is the load-bearing pattern: **[[LiteLLM]] routes and captures the model traffic; [[Langfuse]] stores and visualises it** — together they are the open-source spine of the observability layer a small team can stand up on day one, which the InfoQ talk argues is a non-negotiable investment for any agentic system headed to production.

## Sources referencing LiteLLM

- [[2026-05-18-wolfe-agent-evaluation-detailed-guide]] — τ-bench agent-loop code listing uses `litellm.completion()`.
- [[2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail]] — LiteLLM + Langfuse + LangGraph as the open-source observability stack.

## Open questions

- **Routing vs. observability — which role dominates in practice?** The two wiki sightings split cleanly (Wolfe = routing seam; InfoQ = capture point). A third source would help establish whether teams adopt LiteLLM primarily for provider-portability or for telemetry.
- **LiteLLM-proxy vs. LiteLLM-SDK.** The wiki sources reference the library/SDK surface; the gateway/proxy deployment mode is not yet covered by an ingested source.
