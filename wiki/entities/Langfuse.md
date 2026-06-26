---
type: entity
kind: product
aliases: ["Langfuse"]
tags: [langfuse, agent-harness, observability, tracing, llm-tooling, open-source, evals]
confidence: 0.7
last_confirmed: "2026-06-26"
accessed_at: "2026-06-26"
source_count: 1
relationships:
  - type: part-of
    target: agent-harness
    via: "an open-source implementation of the harness's observability layer — tracing, per-step context inspection, and tool-call capture for agentic systems"
---

# Langfuse

An **open-source LLM-engineering platform** for **observability and tracing** of LLM and agent applications — capturing the traces, per-request context, and tool-call request/response pairs that make an otherwise opaque agent run debuggable. It is the open-source tool a small team can self-host to answer the question the [[agent-harness]] concept calls the hardest in production: *what was in the context at the step where the agent went wrong?*

## Why Langfuse matters in this wiki

Langfuse is a concrete instance of the [[agent-harness]] **observability layer** — the layer the harness literature repeatedly names as a day-one investment rather than an afterthought. It enters the wiki through one source so far:

- **[[2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail|InfoQ "From Demo to Production" 2026]]** describes the *execution black box* failure pattern — a 10-step orchestrator plan that drifts after step ~4–5, then loops and hallucinates with no way to inspect the failing step. The team had been building custom monitoring "until Langfuse released its open-source platform," after which they adopted it (paired with [[LiteLLM]], composable with LangGraph) to capture traces, context, and tool execution. The talk's prescription — *"invest early in observability… otherwise debugging will be very tough in an agentic system because there are too many parts involved"* — is the practitioner statement of why a tool like Langfuse exists.

The operating pattern is the pairing: **[[LiteLLM]] routes and captures the model traffic; Langfuse stores and visualises it.** Together they are the open-source spine of the observability layer the InfoQ talk argues every agentic system needs before, not after, it ships.

> Single-source entity (confidence 0.70). Promoted on explicit user request rather than by the second-source threshold; a second independent source would substantiate the platform's role beyond the one practitioner account and lift confidence.

## Sources referencing Langfuse

- [[2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail]] — adopted as the open-source observability/tracing platform for a production agentic app-generation system.

## Open questions

- **Evals and prompt-management surfaces.** Langfuse ships observability *plus* evaluation and prompt-management features; the wiki's single source covers only the tracing/observability use. The eval surface would connect Langfuse to the [[agentic-engineering]] eval-discipline thread if a future source covers it.
- **Self-host vs. cloud.** The InfoQ account emphasises the open-source/self-host path; a source on the managed offering would round out the picture.
