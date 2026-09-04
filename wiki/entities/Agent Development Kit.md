---
type: entity
kind: library
aliases: ["Agent Development Kit", "ADK", "Google ADK", "Google Agent Development Kit"]
tags: [adk, agent-development-kit, google, google-cloud, agent-framework, python, multi-agent, sequential-agents, loop-engineering, graph-engineering, react]
affiliation: "Google / Google Cloud"
role: "Google's open framework for building, composing and orchestrating LLM agents"
confidence: 0.75
last_confirmed: "2026-09-04"
accessed_at: "2026-09-04"
source_count: 5
relationships:
  - type: part-of
    target: Google
    via: "Google Cloud's agent-building framework, and the product referenced throughout the AI Builder Essentials series"
  - type: instance-of
    target: agent-harness
    via: "ADK is a framework-layer harness — it supplies the loop, the tool wiring, the agent composition primitives and the orchestration graph around a model"
---

# Agent Development Kit

**[[Google]]'s framework for building and orchestrating LLM agents** (usually "ADK"), and the product that sits underneath most of the wiki's Google-sourced agent material. It occupies the **framework** slot in the vocabulary [[Harrison Chase]] sharpened on [[2026-05-09-chase-agent-development-lifecycle|the agent development lifecycle]] — *frameworks / runtimes / harnesses / no-code* — supplying agent composition primitives rather than a finished product surface. That distinguishes it from [[Antigravity]], Google's *harness and IDE* ecosystem, which the wiki tracks separately and which should not be conflated with ADK.

## What the corpus shows it doing

- **Wiring up the reason-act loop in practice.** [[2026-06-10-google-cloud-tech-ai-agents-explained-first-agent]] builds a self-correcting multi-agent blog-writing system in Python on ADK, pairing the [[concepts/react-reasoning-acting|ReAct]] theory with a hands-on build — the operational bookend to the [[2022-10-06-yao-et-al-react-synergizing-reasoning-acting|2022 ReAct paper]]. Three agent patterns are demonstrated: sequential, reactive, and planning.
- **Composing loops into graphs.** [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails]] is the ADK team's account of when a single loop stops coping and the work should move to **graph engineering** — *"you can put loop as part of the graph, or you can create your own nodes and edges."*
- **Shared state as the graph's traversal mechanism.** [[2026-09-03-thurium-wang-google-cloud-graph-engineering-101]] names what ADK actually supplies for [[graph-engineering|graph engineering]]: *"if you build a multi-agent system we have this shared state among different agents; if you build a workflow, we have shared state among nodes in this workflow as well."* Two granularities, one primitive — and it is what makes *"passing memory or information down the graph to the next node"* work. The video ships with a companion codelab (`g.dev/ai/adk-2-orchestration`) and the **fan-out / join / router** pattern vocabulary the corpus now uses for ADK workflows.
- **Alongside the CLI surface.** [[2026-04-22-cheung-ippolito-secchi-google-agents-cli]] covers Google's agents CLI in the same product family.

## Why it matters to the wiki

ADK is one of the few named frameworks the corpus can watch across a full arc — theory ([[concepts/react-reasoning-acting|ReAct]]), a build, a failure taxonomy, and an escalation path from loops to graphs — all from the same vendor within five months of 2026. That makes it a useful **worked instance** of [[concepts/agent-harness|agent-harness]] claims that are otherwise stated abstractly, with the standard caveat that every one of those sources is vendor-produced and none of them measures anything.

## Appears in this wiki via

- [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails]] · [[2026-06-10-google-cloud-tech-ai-agents-explained-first-agent]] · [[2026-04-22-cheung-ippolito-secchi-google-agents-cli]] · [[2026-05-07-kokane-agent-harness-vs-systems-design]]

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "adk")
SORT file.name ASC
```
