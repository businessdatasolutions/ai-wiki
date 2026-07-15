---
type: source
kind: video
title: "Building the future of agentic infrastructure"
author: ["Claude"]
publisher: "Anthropic (Claude YouTube channel); Jess Yann (Product Manager, Claude Managed Agents), Katelyn Lesse (Head of Engineering, Claude Platform), and Angela Jiang (Head of Product, Claude Platform)"
url: "https://www.youtube.com/watch?v=ksfm6jeTg3Q"
date_published: 2026-07-10
date_ingested: 2026-07-15
length: "~16:33 minutes (transcript ~330 dialogue lines; auto-generated captions used — a manual English track also exists per the raw file's `caption_tracks:` but was not the fetched track; the raw transcript file contains the same dialogue twice, once unwrapped and once line-wrapped by the fetch tool, per the known `youtube-transcript-skill` doubling artifact — disregarded at ingest)"
raw: "../../raw/videos/building-the-future-of-agentic-infrastructure.md"
tags: [anthropic, claude-platform, claude-managed-agents, agent-identity, agent-to-agent, mcp, agent-harness, thinner-harnesses, meta-harness, adversarial-agents, agentic-roi, hyper-independence, sprawl, invisible-substrate, outcomes, video-7-of-7]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-seizing/rapid-prototyping
relationships:
  - type: supports
    target: 2026-07-08-jensen-huang-why-companies-need-open-agent-systems
    via: "Both are Claude-Platform-adjacent accounts of harness evolution and agent-to-agent interoperability published two days apart — Huang's 'companies built on harnesses' framing and this video's 'thinner harnesses / meta-harnesses' account describe the same harness-thinning-as-models-improve mechanism from substrate-vendor (NVIDIA) vs first-party-platform (Anthropic) vantages; both also independently name a thin MCP server as the agent-to-agent interface"
    confidence: 0.65
  - type: supports
    target: 2026-05-07-anthropic-managed-agents-decoupling-brain-hands
    via: "Direct continuity — this video is the Claude Platform team's own follow-up account of Managed Agents' evolution (memory, outcomes, 'dreaming', agent identity / service-account provisioning), extending the brain/hands/session architecture the engineering blog documented three months earlier"
    confidence: 0.75
  - type: supports
    target: 2026-05-08-bratanic-unified-agentic-memory-hooks
    via: "Angela Jiang's passing mention of 'dreaming' as a Claude Managed Agents concept independently names the same offline-distillation mechanism Bratanic's dream-phase pattern documents (hooks log online; a dream phase distills events into durable memory) — first-party Anthropic corroboration of third-party-observed architecture vocabulary"
    confidence: 0.55
  - type: supports
    target: 2026-06-17-priest-atlantic-pwc-ai-agents-changing-business
    via: "Both describe agents becoming invisible operational infrastructure rather than discrete tools — this video's 'agents as an invisible substrate... more like an operating system' vision parallels Priest's task-registration 'operating system' for PwC's internal agent deployment, from platform-vendor and enterprise-operator vantages respectively"
    confidence: 0.55
---

# Building the future of agentic infrastructure

> Agents are moving from tools you prompt to infrastructure that runs your business. But what does it take to run them in production? Jess Yann (Product Manager, Claude Managed Agents), Katelyn Lesse (Head of Engineering, Claude Platform), and Angela Jiang (Head of Product, Claude Platform) discuss how teams are building agentic infrastructure, including identity, permissions, memory, and agent-to-agent communication. They also share how organizations should think about agentic ROI and designing human-agent teams that adapt to evolving model intelligence.
>
> Learn more about the Claude Platform: https://claude.com/platform/api

## TL;DR

A ~16.5-minute panel (video 7 of a same-day-origin 7-video batch, and the wiki's **first first-party Claude Platform team interview** — as distinct from Anthropic's engineering blog posts and public-facing individual accounts already in the wiki) published on Anthropic's own **[[Anthropic|Claude]]** YouTube channel, 10 Jul 2026. Panelists: **Jess Yann** (PM, Claude Managed Agents, moderating), **Katelyn Lesse** (Head of Engineering, Claude Platform), and **Angela Jiang** (Head of Product, Claude Platform). Six substantive threads:

1. **Agent identity, separate from workflow identity.** Jiang: agent identity is moving toward an outcome-negotiation model — the agent listens to a stated outcome, comes back and asks for the specific access it needs ("I need access to A, B, C, and D"), the human grants a subset ("A, B, and C are okay, but not D"), and the agent then effectively creates **a service account for itself** — auditable, scoped, distinct from a human's identity or a workflow's identity.
2. **Agent-to-agent communication is API-first, and thin.** Lesse: teams increasingly expose an agent via a plain API or a **thin MCP server**, and another agent calls in "the same way that a person might interact with that agent" — no special agent-to-agent protocol beyond what already exists for human-facing integrations. Why this is legitimate *now* rather than a year ago: models got better (less scaffolding/SOP-style logic needed to compensate for non-determinism) and infrastructure now lets agents run **ambient and long-horizon** — triggered by an event, running for a while, returning when ready.
3. **Thinner harnesses, and "meta harnesses" that combine strategies.** Jiang's harness-evolution account: a few months ago, teams built **very complex boxes of business processes** (step A only proceeds to step B if X and Y and Z) to compensate for model unreliability — fragile, and it boxed in the model's actual intelligence. As models get smarter and more agentic in tool-calling and reasoning, teams can **delete the restrictive parts of the harness** — harnesses get thinner over time. The flip side: thinner-harness teams are building **meta harnesses** (Jiang, tentatively: "maybe they're like saddles") that *combine* strategies rather than picking one — multiple agents **competing** to solve the same problem; **adversarial generator/critic pairs** (one agent proposes, a second is adversarial to it); an **advisor strategy** (a stuck agent "calls a friend" — a smarter model or agent — for help). Lesse frames the trajectory as converging toward **hybrids**: start with an expansive best-of-N search across strategies, then once a framework proves out, iterate within that single framework rather than continuing to search broadly.
4. **Worked examples: industrial knowledge capture and full-stack agentic development.** A hackathon winner ("Urrea," per Jiang, name possibly mis-transcribed) built an agentic system that ingests standard operating procedures plus live machine-monitoring signals to **mimic the judgment of a retiring factory expert** — redundancy for decades of undocumented tacit knowledge, an [[industrial-ai-agents|industrial-AI-agents]]-adjacent case. Lesse's example: development teams moving beyond "write me some code" toward full end-to-end agentic systems that also write the PR/requirements doc up front and run QA testing after — citing **Shopify's "River"** (Lesse's recollection of the name) as a named example of a company building a custom end-to-end agentic development platform.
5. **Barriers, ROI staging, and the redefined engineering team.** Named barriers to broader adoption: **security and compliance guardrails** built on security assumptions "that prevailed 20 years ago," and **evals**. On ROI: Jiang argues against jumping straight to a 120-item "agentify everything" laundry list; instead **stage the measurement** — individual speed first, then team-level speed/productivity, only then cross-team process ROI, and only *after* that shift toward financial/user metrics — because speed-and-productivity signals are more leading and more tractable to attribute than financial ones early on. Lesse's parallel claim about "engineering teams": headcount and roles haven't changed much on paper, but the *shape* has — from one technical lead with opinions plus engineers picking up tickets, toward **most of the team holding end-to-end design opinions** while "orchestrating their Claudes" to execute.
6. **Failure modes, and the future as an invisible substrate.** Jiang names **hyper independence** (cheap parallel prototyping tempts everyone into "launch all ten and let the market pick," bypassing systematic evaluation) and **sprawl** (individual hyper-independence without coordination toward a concrete direction) as the two named organizational failure modes of agent reliance. On where "the puck is going": agents becoming **deeply embedded, invisible infrastructure** rather than discrete named tools reached for — "some common substrate," possibly proactive (an agent that notices something broke, fixes it, and either asks for review or — per prior instruction — just ships it), closer to **an operating system than a toolbox**. The closing platform pitch is the **outcomes** primitive already shipped in Claude Managed Agents: state the outcome, give a rubric for "good," set an iteration/spend budget, and let Claude run — the stated goal is removing the need to "think hard" about how to set the work up at all.

## What was actually ingested

Full ASR transcript (auto-generated captions), ~16:33 runtime, 9 chapters (per the raw file's `chapters:` field, mirrored below as section headings). A manual English caption track also exists per the raw file's `caption_tracks:` but was not the track fetched; treat transcript wording as ASR-cleaned, not verbatim-manual. Speaker attribution in the transcript is not diarized — Jiang and Lesse are identifiable from being addressed by name mid-conversation ("Angela, what has been...", "Katelyn, you keep saying..."); Yann is inferred as the (unnamed-in-transcript) moderator asking the framing questions.

## Chapters

- [0:00] Intro
- [1:00] Building Claude Managed Agents in production
- [2:15] How agents talk to each other
- [3:00] The future of agentic infrastructure: thinner harnesses and adversarial agent pairs
- [8:20] Barriers to agentic adoption: security, compliance, and evals
- [9:15] How to measure agent ROI
- [12:45] Failure modes: hyper independence and sprawl
- [13:30] The future: agents as an invisible substrate
- [15:15] What's next for the Claude Platform

## Linked entities and concepts

- Channel/publisher: **[[Anthropic|Claude]]** (Anthropic's own YouTube channel — first-party source).
- **Dangling** (single-source mention, deferred, per the person-entity second-source rule): **Katelyn Lesse** (Head of Engineering, Claude Platform), **Angela Jiang** (Head of Product, Claude Platform), **Jess Yann** (Product Manager, Claude Managed Agents, likely moderator).
- Concepts: [[agent-harness]], [[enterprise-ai-adoption]], [[ai-employment-effects]], [[dynamic-capabilities]], [[industrial-ai-agents]].
- Products/terms new to the wiki, held in body prose rather than promoted to entities: **Claude Managed Agents** (extends [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|the April 2026 engineering blog post]]), the **outcomes** primitive (rubric + iteration budget), **"dreaming"** (Claude Managed Agents' own term for what appears to be the same offline-distillation mechanism as [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic's dream-phase pattern]]), Shopify's **"River"** (named, not independently verified spelling), the hackathon system **"Urrea"** (named, not independently verified spelling).

## Relationships

See frontmatter. Four typed `supports` edges: one to [[2026-07-08-jensen-huang-why-companies-need-open-agent-systems|Huang/NVIDIA (video 6)]] on the shared harness-thinning-as-models-improve mechanism and MCP-as-agent-to-agent-interface; one to [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic's Managed Agents engineering blog]] as this video's own direct follow-up account; one to [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic's dream-phase pattern]] on the "dreaming" terminology convergence; one to [[2026-06-17-priest-atlantic-pwc-ai-agents-changing-business|Priest/PwC]] on the shared agents-as-invisible-operating-system framing. Considered but not linked: [[2026-05-09-chase-agent-development-lifecycle|Chase/LangChain (ADLC)]] and [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase/Interrupt 26]] (both name MCP and harness/runtime layering, but no specific shared claim, quote, or worked example beyond generic thematic proximity — too thin for a typed edge); [[2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail|"From Demo to Production" (InfoQ)]] (shares MCP-server and agent-orchestration vocabulary but addresses a different failure-mode layer — tool/context sprawl inside one agent rather than agent-to-agent identity and ROI staging).
