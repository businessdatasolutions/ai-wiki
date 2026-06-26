---
type: source
kind: video
title: "From Demo to Production: Why Agentic AI Systems Fail — and How to Fix Them"
author: ["InfoQ"]
url: "https://www.youtube.com/watch?v=yCIl1-dIVnc"
date_published: 2026-06-24
length: "~39:08 minutes (transcript ~368 lines)"
raw: "../../raw/videos/from-demo-to-production-why-agentic-ai-systems-fail.md"
tags: [agent-harness, agentic-engineering, progressive-disclosure, skills, tool-search-tool, context-engineering, agent-orchestration, observability, mcp, langfuse, litellm, infoq]
relationships:
  - type: supports
    target: 2024-12-19-anthropic-building-effective-agents
    via: "tool/agent-count discipline + MCP as the integration substrate — the talk opens on Anthropic's Nov-2024 MCP release and reaches the same simplicity-over-sprawl conclusion from production"
  - type: supports
    target: 2026-05-04-rethinking-agents-harness-is-all-you-need
    via: "the subtraction principle in production — fewer tools/instructions in context; the talk independently cites Anthropic's '>50 tools → −30% performance' and the Tool Search Tool's 40%→2% context reduction"
  - type: supports
    target: 2026-04-22-cheung-ippolito-secchi-google-agents-cli
    via: "skills as progressive-disclosure units — both treat a skill as a name+description loaded on demand, with full instructions disclosed only when the model asks"
  - type: supports
    target: 2026-06-03-chopra-headroom-context-optimization-layer-for-llm-applications
    via: "context-window budgeting as a first-class harness problem — Headroom optimises context at runtime; this talk solves the same overflow via progressive disclosure of context and tools"
---

# From Demo to Production: Why Agentic AI Systems Fail — and How to Fix Them

> Most agentic AI systems look great in demos — and collapse in production. This talk reveals why: it's a systems problem, not a model problem. Through hard lessons building a platform for 10M+ users, learn how to master context management, tool exposure, agent boundaries, and observability to ship AI that actually works. — *InfoQ video description*

## TL;DR

An InfoQ conference talk by an engineer who built an **agentic app-generation platform** (a cloud, browser-based builder for mobile/web apps, driven by both a visual editor and a chat/"vibe-coding" interface, serving 10M+ users). The 2025-era architecture was **10 agents, 200+ tools, thousands of instructions**, wired together by an **orchestrator** that delegates to per-feature domain agents and talks to platform APIs via an [[2024-12-19-anthropic-building-effective-agents|MCP]] server. The pilot was fast and impressed the CEO — but **pilots prove nothing about production** for agentic systems, because the artificial constraints (small scope, few tools, limited context) that make a pilot work disappear in production, and LLM behaviour isn't deterministic the way a Salesforce rollout is.

The talk names **four failure patterns** and the fixes, all of which independently reproduce claims the wiki already holds on [[agent-harness]]:

1. **Context overload** → **progressive disclosure** via **skills** (name + description loaded; full instructions loaded on demand — "lazy loading for LLMs"). All agents were rebuilt as skill-based systems.
2. **Tool explosion** (200+ tools ≈ 6–7k tokens; GitHub MCP 35 tools/26k tokens; Jira 17k; a full integration ≈ 72k = 36% of a 200k window; Anthropic: >50 tools → −30% performance) → **progressive disclosure of tools / the Tool Search Tool** (semantic search over tools, *not* loaded into context; Anthropic report: 40% → 2% context share, ~85% token reduction). Use only above ~20–30 tools (it adds a hop/latency).
3. **Agent-orchestration complexity** — orchestrator hand-offs lose information because **agents can't share context windows** (the manager-ID-nullable validation discovered by the DB agent never reached the backend/UI agents → business rule silently dropped despite every agent reporting success) → **prefer skills over small agents** for shared context, and **decide agent vs. skill vs. tool** (agent = end-to-end ownership/"a manager"; skill = a capability/"how"; tool = the action). New shape: **one agent, multiple skills, each skill carrying its own tools**.
4. **The execution black box** — a 10-step orchestrator plan that drifts after step ~4–5, then loops and hallucinates, with no way to inspect the context at the failing step → **invest early in observability**: traces, per-step context inspection, tool-call capture, using **Langfuse + LiteLLM** (works with LangGraph).

Closing thesis: **agentic systems are built through engineering** — "the model is just one component… the industry says only builders are required, but engineers are still required." (See [[agentic-engineering]].)

## What was actually ingested

The full ASR (auto-generated) transcript of the ~39-minute talk, including the closing Q&A (observability tooling; prompts-as-technical-debt across model updates; orchestrator global-info vs. summaries + the planner-agent pattern; monorepo-vs-multirepo correctness; and a deliberate **no-web-access** policy for the agents, with RAG over proprietary developer docs). The presenter is **not named** in the transcript or in YouTube's metadata; attribution is to the **InfoQ** channel. Light proper-noun cleanup was applied at ingest (MCP, Langfuse, LiteLLM, LangGraph, OAuth, "vibe coding", "visual editor"); see the raw file's `notes:`.

## Why this source matters to the wiki

This is the wiki's first **independent practitioner platform-builder** war-story on agentic-AI production failure that lines up, point for point, with the [[agent-harness]] concept's existing structure — but arrives at it from *outside* the Anthropic/Google/LangChain vendor cluster and the academic ablation papers. It is corroboration of the **subtraction principle** ([[2026-05-04-rethinking-agents-harness-is-all-you-need|fewer tools/instructions = better]]) and of **progressive disclosure** as the Context-layer discipline, observed live on a 200-tool / 10-agent system rather than asserted.

### Progressive disclosure of context (skills)

The "security agent that ships every auth provider's instructions even when the user only wants OAuth" example is a clean, concrete instance of the Context-overload problem the [[agent-harness]] page describes abstractly ("give the model what is required, not everything you have"). The fix — **skills** as on-demand instruction bundles (name + description in the prompt; body loaded only when the model asks) — is the same construct the [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Google Agents CLI]] source treats as per-stage skill specs, here cast explicitly as **"lazy loading."**

### Progressive disclosure of tools (the Tool Search Tool)

The talk supplies an unusually concrete **token-budget breakdown** of the tool-explosion problem (GitHub 35 tools/26k tokens; Jira 17k; a full integration ≈ 72k ≈ 36% of the window) and names the fix as the **Tool Search Tool** — a tool that indexes all tools, stays *out* of the context window, and returns only the semantically relevant few per request (Anthropic report: 40% → 2% context share). This is the production-tooling instantiation of the **subtraction principle** ([[2026-05-04-rethinking-agents-harness-is-all-you-need]]) — and the talk independently cites the same "Anthropic: >50 tools → −30% performance" datapoint, plus the caveat that the search hop is only worth its latency above ~20–30 tools.

### Agent vs. skill vs. tool, and the orchestrator information-loss failure

The **manager-ID-nullable** example is a sharp, memorable case of the multi-agent hand-off failure the [[agent-harness]] page records via [[2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world|the orchestrator-not-builder]] sources: a correct discovery made inside one agent's context is lost at the summary-hand-off boundary because **agents cannot share context windows**, so the validation lands nowhere and every agent still reports success. The resolution — collapse small agents into **skills under one agent** (shared context), and reserve a separate agent only for genuinely independent end-to-end jobs (their example: a separate code-**review** agent that needs only the git diff) — is a practitioner decision rule for the agent/skill/tool boundary the concept page treats as an open design question.

### Observability as a day-one harness investment

"There is no easy way to debug an agentic system unless you invest early" — traces, per-step context inspection, and tool-call capture (via **Langfuse + LiteLLM**, optionally with LangGraph) — ratifies the **Compounding/telemetry** and human-in-the-loop layers of [[agent-harness]] from the open-source-tooling vantage, naming the specific stack a small team actually reached for.

## Linked entities and concepts

- [[agent-harness]] — the primary concept this source ratifies (Context overload → progressive disclosure; tool explosion → tool search; orchestration hand-off loss; observability).
- [[agentic-engineering]] — the closing thesis ("engineers still required; the model is one component").
- [[ai-agents]] — the orchestrator / multi-agent / skill decomposition discussed throughout.
- [[Langfuse]] — open-source observability/tracing platform the team adopted for the *execution black box* fix (entity promoted on this ingest, by request).
- [[LiteLLM]] — OpenAI-compatible model-API abstraction, paired with Langfuse for model-call capture (entity promoted on this ingest — second source after [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe]]).
- [[InfoQ]] — the publishing venue/channel (`author:`); promoted to an entity on this ingest (second InfoQ-published source, after [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler / QCon London 2026]]).
- **Dangling** (single-source mentions, deferred per Author-entity promotion): the **presenter is unnamed**; **LangGraph** is a named tool without its own page yet — promote on a second-source mention.

## Source quality

Auto-generated (ASR) transcript, light-cleaned at ingest — proper nouns normalised but no human-curated caption track existed. Quantitative claims (the 26k/17k/72k token figures, the 40%→2% and −30% Anthropic numbers) are **the speaker's** restatements of publicly reported figures; treat as second-hand, directionally reliable, and consistent with the numbers already cross-checked on [[agent-harness]] via [[2026-05-04-rethinking-agents-harness-is-all-you-need]]. The presenter's identity and the platform's name are not stated, so the "10M+ users" scale claim is uncorroborated.
