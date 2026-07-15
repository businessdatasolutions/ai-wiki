---
type: source
kind: video
title: "Jensen Huang: Why companies need open agent systems"
author: ["LangChain"]
publisher: "LangChain (LangChain YouTube channel); NVIDIA CEO Jensen Huang interviewed by Harrison Chase"
url: "https://www.youtube.com/watch?v=Yy3JH6dDugc"
date_published: 2026-07-08
date_ingested: 2026-07-15
length: "~26:35 minutes (transcript ~890 dialogue lines; auto-generated captions used — a manual English track also exists but was not the fetched track; the raw transcript file contains the same dialogue twice, once unwrapped and once line-wrapped by the fetch tool, per the known `youtube-transcript-skill` doubling artifact — disregarded at ingest)"
raw: "../../raw/videos/jensen-huang-why-companies-need-open-agent-systems.md"
tags: [jensen-huang, nvidia, harrison-chase, langchain, nemotron, deep-agents, openshell, open-weight-models, frontier-models, agent-harness, super-agents, sub-agents, runtime-security, access-control, anthropomorphizing-ai, ai-and-jobs, video-6-of-7]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-seizing/rapid-prototyping
relationships:
  - type: supports
    target: 2026-05-09-chase-agent-development-lifecycle
    via: "Harrison Chase, the interviewer here, is LangChain's co-founder/CEO and the author of the ADLC essay; Huang's account of post-training Nemotron 3 Ultra 'inside the harness' and tuning prompts/tools per model is a live vendor-CEO-to-vendor-CEO conversation that operationalises the same frameworks/runtimes/harnesses layering Chase names in the essay"
    confidence: 0.7
  - type: supports
    target: 2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents
    via: "extends Chase's model/harness/context three-layer continual-learning model with a concrete cross-company worked example — NVIDIA post-training Nemotron 3 Ultra against the LangChain Deep Agents harness, tuning the harness's prompts and tools per-model — and independently corroborates Chase's 'open-source models rising' driver with a named benchmark (Nemotron 3 Ultra 86% vs Claude Opus 87% on an internal Deep Agents eval, ~10x cheaper)"
    confidence: 0.65
  - type: supports
    target: 2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm
    via: "independent vendor-CEO convergence (NVIDIA vs Microsoft) on the same specialization doctrine — Huang's 'start with the frontier... as soon as it gets good enough, specialize' mirrors Nadella's 'don't use frontier models for non-frontier problems'; both frame the decision as a compute-cost/latency trade rather than a capability ceiling, and both use electricity-adjacent metaphors for the underlying compute substrate (Huang: 'it's electrons, not atoms'; Nadella: 'electrons-to-tokens' data centers)"
    confidence: 0.6
  - type: supports
    target: 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees
    via: "shared topic — how much to anthropomorphize agentic systems. Huang's explicit position ('it's electrons, not atoms... it's a tool, like my vacuum cleaner... we tend to imbue too much human properties to it') argues against employee-style framing, aligning with Kropp et al.'s core prescription, even as Huang separately uses HR-system and onboarding language ('we are creating an HR system, if you will, for AI... give them access control... a skills file') to describe agent access-provisioning — a nuance worth holding alongside Kropp et al.'s finding that employee-framing measurably changes accountability outcomes"
    confidence: 0.55
  - type: supports
    target: 2026-07-09-nyc-executive-forum-2026-a-leaders-guide-to-agentic-ai
    via: "both name runtime security and access control as the binding precondition for enterprise agent deployment — Huang's OpenShell ('a secure and open runtime... it's impossible to deploy' without solving access control) parallels Vachhrajani's Bedrock AgentCore as trust-pillar infrastructure, from two different vendor stacks (NVIDIA/LangChain vs AWS) converging on the same requirement"
    confidence: 0.55
  - type: supports
    target: 2026-07-10-building-the-future-of-agentic-infrastructure
    via: "both, two days apart, describe harnesses thinning as models improve and a thin MCP server as the agent-to-agent interface — Huang's 'companies built on harnesses' framing (substrate/silicon vendor) and the Claude Platform team's 'thinner harnesses / meta-harnesses' account (first-party platform vendor) converge on the same mechanism from different vantages"
    confidence: 0.65
---

# Jensen Huang: Why companies need open agent systems

> NVIDIA founder and CEO Jensen Huang sits down with Harrison Chase to discuss why the last six months finally made AI useful, and what it takes to turn a large language model into a real, deployable product. The path there, Jensen says, is building your own "super agents": domain-specific systems wrapped in an open harness, grounded in your data, and improved over time. NVIDIA and LangChain also announce a new blueprint for running Deep Agents with Nemotron 3 Ultra inside OpenShell, a secure, open runtime, giving every enterprise the building blocks to create and deploy super agents anywhere.

## TL;DR

A fireside interview (video 6 of a same-day-origin 7-video batch) between **NVIDIA CEO Jensen Huang** and **[[Harrison Chase]]** (LangChain co-founder/CEO), published on the **[[LangChain]]** YouTube channel, 8 Jul 2026. Huang's central claim: **"today, most companies are built on business processes. In the future, most companies will be built on harnesses."** The interview doubles as the launch of a joint **NVIDIA + LangChain blueprint** — running **[[LangChain|Deep Agents]]** with **Nemotron 3 Ultra** inside **OpenShell**, a secure open runtime — giving enterprises the building blocks (model, harness, blueprint, runtime) to build domain-specific "super agents" anywhere: cloud, on-prem, or on a DGX Spark next to a laptop.

Six substantive threads:

1. **Why NVIDIA invests in an open agent ecosystem.** Huang frames the last six months as the point where "everything came together" for agentic AI — foundation-model advances plus harness engineering (naming Claude Code and OpenClaw explicitly) plus LangChain's own build-up from promptable-API wrapper to RAG tooling to agents. NVIDIA's stated motive for openness: AI is "a fundamental technology" useful only when applied to many domain-specific use cases NVIDIA cannot build itself — scientists, digital biologists, roboticists, enterprise IT all need to build their own specialized, proprietary AIs on an open foundation.
2. **Specialization: model, harness, and post-training together.** Nemotron Ultra needs "intelligence that's good enough" first, but becomes useful only inside the LangChain harness, grounded on domain-specific information — and, looking forward, post-trained *inside* the harness so the model "becomes good at applying the harness around it." On an internal Deep Agents benchmark, **Nemotron 3 Ultra scores 86% vs. Claude Opus's 87%**, at roughly **10x lower cost** — DeepSeek and a Minimax model trail at 82-83%. Cheaper, faster inference lets an agent "iterate across a larger search space" and "find better answers," independent of raw capability.
3. **When to specialize: start with the frontier, then build super sub-agents.** Huang's own practice: start every task with a frontier model (Claude Code, Codex) "for as long as I can," then, once a domain (e.g. supply-chain or chip-design optimization) proves too hard for a general agent, build narrow **super sub-agents** on LangChain Deep Agents + Nemotron 3, connected to proprietary knowledge and tools. **"That thing is built for one job... now I think that defines a company. A company is really about a collection of a whole bunch of these super proprietary, super important workflows."**
4. **Companies built on harnesses, not business processes.** The interview's headline claim: LangChain becomes "the tool that creates the operating system for the company," and the harness inside a workflow "becomes autonomous, agentic, much more efficient." Every company's specialized intellectual property *is* its intelligence — "you can't possibly not continue to control it, improve it, make it better," and outsourcing that intelligence "makes no sense," whether for a person, company, or country. General skills (coding, writing) are foundation-model territory; the proprietary, specialized layer on top requires open tools you own.
5. **Runtime, security, and access control.** Huang frames the runtime as the unglamorous but load-bearing final layer — "without solving the security, the access control, it's impossible to deploy," drawing an explicit parallel to employee onboarding (access to files, networks, tools scoped by role). This is presented as the reason OpenShell exists: a secure sandbox IT organizations can control. In the same breath Huang uses HR-system language ("we are creating an HR system, if you will, for AI... a skills file") while, minutes later, explicitly rejecting deeper anthropomorphizing.
6. **How much to anthropomorphize agents, and why more AI means more jobs.** Huang's position: "it's electrons, not atoms... it's not biological, has no consciousness... it's a tool, like my vacuum cleaner." He predicts the discomfort fades the way "dishwasher" did. On employment: **"the more AI we use, somehow the more people we have to hire"** — software engineers now build and orchestrate agents (evals, benchmarks, guardrails) rather than write Python, work Huang says his engineers prefer. Chase adds the sharper framing: most current agent usage still automates what people did before; the larger unlock is doing what "we couldn't do before."

## What was actually ingested

Full ASR transcript (auto-generated captions), ~26:35 runtime, 15 chapters. A manual English caption track also exists per the raw file's `caption_tracks:` but was not the track fetched; treat transcript wording as ASR-cleaned, not verbatim-manual.

## Linked entities and concepts

- Channel/publisher: [[LangChain]] (8th source).
- **Interviewer:** [[Harrison Chase]] (4th source — LangChain co-founder/CEO).
- **Created [[NVIDIA]]** entity — first substantive source (central subject: NVIDIA's CEO, products, and joint blueprint announcement), following the same first-appearance-as-central-subject precedent as [[Khan Academy]] and [[PwC]]. NVIDIA had previously appeared only in passing, as silicon named alongside AMD, in [[2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm|Nadella/Hoffman]].
- **Dangling** (single-source mention, deferred, per the person-entity second-source rule — central-subject status does not itself trigger promotion for individuals, precedent: Sal Khan on the Khan Academy source): **Jensen Huang** (NVIDIA founder/CEO — central subject of this interview, but no prior wiki source; will promote on a second substantive Huang-authored or Huang-centric source).
- Concepts: [[agent-harness]], [[enterprise-ai-adoption]], [[ai-employment-effects]], [[dynamic-capabilities]].
- Products/terms new to the wiki, held in body prose rather than promoted to entities: **Nemotron 3 Ultra** (NVIDIA open-weight model), **OpenShell** (secure open agent runtime), the **Deep Agents + OpenShell blueprint** (joint NVIDIA/LangChain announcement), **DGX Spark** / **DGX station** (NVIDIA hardware named as deployment targets).

## Relationships

See frontmatter. Six typed `supports` edges: two to existing [[Harrison Chase]] / [[LangChain]] sources ([[2026-05-09-chase-agent-development-lifecycle|Chase/ADLC]], [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase/Interrupt 26]]) on the shared harness/model/context vocabulary; one to [[2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm|Nadella/Hoffman]] on independent vendor-CEO convergence around frontier-vs-specialized model choice; one to [[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees|Kropp et al./BCG]] on the anthropomorphizing-AI debate; one to [[2026-07-09-nyc-executive-forum-2026-a-leaders-guide-to-agentic-ai|Vachhrajani/AWS NYC]] on runtime security/access-control as an enterprise-deployment precondition; one to [[2026-07-10-building-the-future-of-agentic-infrastructure|the Claude Platform team's own agentic-infrastructure panel]] on the shared harness-thinning mechanism and MCP-as-agent-interface, published two days after this interview. Considered but not linked: [[2026-06-17-ng-langchain-interrupt-future-of-ai-agents|Ng/LangChain Interrupt]] (same conference-adjacent LangChain-channel cluster and shares an `open-weight-models` tag, but no specific shared claim, quote, or data point beyond generic thematic proximity — too thin for a typed edge).
