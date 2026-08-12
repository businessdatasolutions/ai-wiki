---
type: source
kind: video
title: "How Toyota Uses Deep Agents to Speed Up R&D and Manufacturing Research"
author: ["LangChain"]
url: "https://www.youtube.com/watch?v=oK_wPTUshRc"
date_published: 2026-08-11
date_ingested: 2026-08-12
length: "~2:12 minutes (transcript ~19 lines; human-curated captions) — a short vendor customer-testimonial clip, not a talk"
raw: "../../raw/videos/how-toyota-uses-deep-agents-to-speed-up-rd-and-manufacturing-research.md"
tags: [ravi-chandu-ummadisetti, toyota, langchain, deep-agents, langsmith, polly, insights, rd-gpt, institutional-knowledge, skills, agent-observability, paint-corrosion, manufacturing-research]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
  - digital-transforming/redesigning-internal-structures
relationships:
  - type: supports
    target: 2026-08-10-banholzer-laberge-mckinsey-how-to-maximize-competitive-advantage
    via: "a target-firm instance of the ontology prescription published a day earlier — Banholzer argues firms should encode 'what makes your business unique and special' so agents have railroad tracks to navigate, and Ummadisetti describes Toyota doing exactly that: curated skills per function (branding, research, manufacturing, supply chain) fed to agents as 'the institutional knowledge that we have at Toyota'"
    confidence: 0.65
  - type: supports
    target: 2026-07-24-turnbaugh-motherduck-context-layers-explained
    via: "both treat codified institutional knowledge as the thing that makes an agent useful over a company's own data rather than the model; Turnbaugh argues the case from a data platform, Ummadisetti reports an enterprise doing it — Toyota's per-function skills library is a working instance of the context layer Turnbaugh says has to exist"
    confidence: 0.6
---

# How Toyota Uses Deep Agents to Speed Up R&D and Manufacturing Research

> Ravi Chandu Ummadisetti, Director of Agentic AI and Product Research at Toyota North America, explains how his team built R&D GPT, an internal agent that searches Toyota's research, paint, and manufacturing data to answer engineering questions. He breaks down how Deep Agents' single command and harness pull in skills from across Toyota's research, branding, and supply chain teams, and why Polly and Insights inside LangSmith are the tools he relies on most to understand what his agents are actually doing in production.

## TL;DR

A **~2-minute customer-testimonial clip** on the **[[LangChain]]** channel, published 11 August 2026 — **Ravi Chandu Ummadisetti**, Director of Agentic AI and Product Research at **Toyota** North America. Read this page for what it is: a short vendor-produced clip with seven chapter markers across 132 seconds, not a talk. Its value to the wiki is as a **named enterprise deployment** in a manufacturer, a sector under-represented in the corpus relative to software and services.

1. **The use case: R&D GPT.** An internal agent that searches Toyota's research, paint and manufacturing data to answer engineering questions. Ummadisetti's framing of why R&D specifically: *"Toyota puts a lot of… efforts into research, because the quality that you see outside cars is because of these efforts… if you look at Toyota paint or Toyota seats, it's all because of the work that we do at research with R&D."*
2. **What Deep Agents contributes, in his words.** *"Deep Agents is one beautiful concept where deep agents is like **one single command**… and that one single command is having this **entire ecosystem of harness**. That is really bringing the deep agents more powerful, especially in working on these use cases like R&D GPT, where we do a lot of deep research and the existing documents that we have at Toyota."* The harness is what pulls tools in from across the organisation: *"the harness is really bringing a lot of these tools coming in from different wings, like the paint corrosion… we're bringing that entire system and then giving it to deep agents."*
3. **The query pattern.** Engineers ask in plain language — *"How can I fix this paint issue for this particular car?"* — and the agent retrieves across connected sources, *"from SQL data or anything, all the tools that are connected with these deep agents."*
4. **Skills as the institutional-knowledge carrier — the most transferable claim.** *"We have a lot of skills that we have created at Enterprise AI. We have our own skills, especially in terms of **branding**, or in terms of the **research**, or in terms of the **manufacturing**, in terms of the **supply chain**. All of these are… our own curated skills, and we're trying to give those skills as an input to the agents. That way, we are trying to **feed in the institutional knowledge that we have at Toyota**."* Note the structure: skills are organised **per business function**, authored centrally by an Enterprise AI group, and supplied to agents as input — a concrete organisational answer to the codification problem other sources in the corpus argue about in the abstract.
5. **Observability is what he singles out.** Asked what he relies on in LangSmith: *"I really love **Polly** in LangSmith and **Insights**… Insights is really pretty good, because we can see the end-to-end ecosystem of the dashboard of the agent, as well as what's happening **inside the depth of the agent** — meaning what the users are using [it] for, and what are the **outliers** that we as a team [need] to fix."* The two things he names wanting to see are usage composition and outliers, which is a production-operations framing rather than an evaluation one.

## What was actually ingested

The **complete** clip — all 19 caption segments, consistent with `duration: 2:12` / `length_seconds: 132` — from the human-curated track (the video also carries an auto-generated track). All 7 chapter markers present, which at ~19 seconds per chapter is itself a signal of how compressed the piece is. Nothing was truncated; there simply is not much here.

**Scope warning, load-bearing for anyone citing this page.** This is a promotional clip, and it contains **no numbers of any kind** — no deployment scale, no user counts, no latency or accuracy figures, no before/after comparison, no cost. It names no failure modes and no limitations. Every claim is a first-person description of an internal system that cannot be inspected. Treat it as evidence that Toyota North America *has* an agentic R&D-search deployment and as a description of its shape; treat it as no evidence at all about how well it works.

## Dynamic-capabilities tagging

- **`digital-transforming/improving-digital-maturity`** — the deployment's substance is making decades of dispersed research, paint-corrosion and manufacturing data queryable in natural language by the engineers who need it, and codifying per-function institutional knowledge as reusable skills so agents inherit it. That is a digital-maturity build in the specific sense the wiki tracks: the constraint being addressed is the accessibility and machine-readability of the firm's own knowledge, not model capability.
- **`digital-transforming/redesigning-internal-structures`** — a named **Enterprise AI** function authors curated skills on behalf of branding, research, manufacturing and supply chain, and a director-level role ("Director of Agentic AI and Product Research") exists to run it. Both are structural changes rather than tooling ones: a central group producing knowledge artifacts that distributed teams' agents consume.

## Linked entities and concepts

- [[LangChain]] — publisher, and vendor of both Deep Agents and LangSmith. Updated in this ingest.
- [[2026-08-10-banholzer-laberge-mckinsey-how-to-maximize-competitive-advantage|Banholzer & LaBerge / McKinsey]] — a target-firm instance of the ontology-encoding prescription published one day earlier; see this source's `relationships:`.
- [[2026-07-24-turnbaugh-motherduck-context-layers-explained|Turnbaugh / MotherDuck]] — the context-layer argument, here observed in production.
- [[concepts/agent-harness|agent-harness]] — "one single command… having this entire ecosystem of harness" is a customer-side restatement of the harness framing the wiki tracks from vendors and practitioners; skills-as-institutional-knowledge is the context layer of that harness.
- [[concepts/ai-agents|ai-agents]] — Deep Agents as a named product pattern, and the multi-source retrieval shape of R&D GPT.
- [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] — a manufacturer-sector deployment with a named owning function (Enterprise AI) and a production-observability practice.
- [[concepts/knowledge-graphs|knowledge-graphs]] — per-function curated skills as the codification mechanism for institutional knowledge.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the two cells tagged above.

**Dangling** (single-source mention, deferred per [author-entity promotion](../../CLAUDE.md#author-entity-promotion)): Ravi Chandu Ummadisetti, **Toyota** (first appearance; the wiki's first Japanese-manufacturer deployment — promote on a second source), LangSmith, Deep Agents, Polly, Insights.

## Source quality note

Human-curated caption track, so transcription is clean; three minor ASR-style corrections were applied at acquire time (see the raw file's `notes:`).

**This is vendor marketing.** It is published on LangChain's channel, the speaker names LangChain products favourably throughout ("I really love Polly"), and the clip's structure — seven chapters in 132 seconds, each landing one product benefit — is a testimonial format. It should not be cited for any claim about Deep Agents' or LangSmith's effectiveness.

What it *can* support, and the reason it earns a page: it is a **named, on-the-record enterprise deployment** in automotive manufacturing, by an identified director who describes the system's organisational shape (a central Enterprise AI group authoring per-function skills) in enough detail to compare against other sources' prescriptions. The wiki's corpus skews heavily toward software, consulting and services; a manufacturer describing what it actually built is worth holding even at this length, with the scope warning above attached.
