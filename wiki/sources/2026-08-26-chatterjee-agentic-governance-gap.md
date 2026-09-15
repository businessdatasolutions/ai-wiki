---
type: source
kind: article
title: "The Agentic Governance Gap: Why Autonomous AI Systems Demand a New Cybersecurity Discipline"
author: ["Dave Chatterjee"]
publisher: "Analytics Magazine (INFORMS) — 'Cyber Resilience in the Age of Intelligent Systems' column"
url: "https://doi.org/10.1287/LYTX.2026.03.04"
date_published: 2026-08-26
date_ingested: 2026-09-15
length: "~8 printed pages (~1,900 words; full text read)"
raw: "../../raw/articles/2026-08-26-chatterjee-agentic-governance-gap-analytics-magazine.md"
tags: [agentic-governance, cybersecurity, dave-chatterjee, informs, analytics-magazine, autonomy-creep, tool-sprawl, multi-agent-coordination, action-scoped-permissions, circuit-breakers, kill-switches, escalation-thresholds, cross-agent-provenance, cpd-framework, board-oversight, red-teaming, agent-inventory, reversibility]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - contextual/internal-barriers
  - digital-sensing/digital-scenario-planning
relationships:
  - type: supports
    target: 2025-03-17-cemri-why-do-multi-agent-llm-systems-fail
    via: "the governance-side restatement of MAST's inter-agent misalignment category. Chatterjee's third converging force is multi-agent coordination — *'a flawed instruction, a poisoned data source, or a manipulated prompt can cascade through a chain of agents before a person is positioned to intervene'* — which is MAST's failure taxonomy read as an enterprise control problem rather than a research finding. His proposed control (cross-agent identity and provenance) is a direct answer to the seam MAST identifies"
    confidence: 0.8
  - type: supports
    target: 2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails
    via: "the same failure modes at board altitude rather than developer altitude. Google Cloud's runaway loop with no exit condition is Chatterjee's *'agents that looped indefinitely on a flawed instruction'*; their prescription is stop rules and cost caps in the runtime, his is tested circuit breakers and kill switches with a measured halt time. A vendor teaching engineers and an academic addressing the C-suite arriving at the same control set"
    confidence: 0.75
  - type: supports
    target: 2026-09-01-cfa-institute-agentic-ai-finance-workflows-governance
    via: "two independent 2026 sources placing agentic governance in regulated-industry terms within a month of each other, both concluding that the governance model has to move upstream of the model. The CFA roundtable supplies the sector-specific finding (LLM biases mirror investor biases, so delegating judgment does not launder the bias); this supplies the architectural control set that would have to exist for such delegation to be auditable"
    confidence: 0.75
---

# Chatterjee — The Agentic Governance Gap (Analytics Magazine, August 2026)

A short practitioner column by **Dave Chatterjee** in INFORMS' *Analytics Magazine*, and the clearest statement in the corpus of **why AI governance designed for the copilot era structurally fails for agents**.

> **Not to be confused** with [[2026-05-07-chatterjee-anatomy-of-agent-harness|Abhishek Chatterjee]], author of the wiki's four-layer harness taxonomy. Different people, unrelated work, shared surname.

## TL;DR

The argument turns on one boundary:

> *"It is the difference between a system that produces a document and a system that executes a transaction, and most enterprise governance structures were never built for the latter."*

Generative AI's first wave raised real risks — hallucination, bias, data leakage — but all of them were *"contained within a single, familiar boundary: content. A human read the output before anything happened in the real world."* Agents erase that boundary: **the output is not a paragraph to evaluate, it is an action already taken.**

And the reason this is hard is not negligence. It is that the control being removed *is the product*:

> *"Organizations are adopting agents specifically to remove the human bottleneck. The governance model built to catch mistakes is being designed out of the system at the same moment the system's capacity to cause harm is increasing."*

That sentence is the most useful thing in the article and belongs on [[agent-oversight-and-delegation]]: **oversight and value are in direct tension by construction**, which is why exhorting organisations to keep humans in the loop does not work.

## Three converging forces

- **Autonomy creep** — permissions granted incrementally per workflow, *"often without a corresponding review of what those permissions, in aggregate, now allow."* A capability added for one task quietly becomes available to every task the agent touches.
- **Tool and API sprawl** — *"the attack surface and error surface expand together"*, and **a single misconfigured agent now reaches further than any single compromised employee account.**
- **Multi-agent coordination** — each delegation hop pushes human oversight further away, and errors cascade before anyone is positioned to intervene. This is [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail|MAST's]] inter-agent misalignment, seen from the security side.

The first two are, at board altitude, the failures [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails|Google Cloud teaches engineers]] as runaway loops and unverified autonomy — and the regulated-industry version arrives a week later in [[2026-09-01-cfa-institute-agentic-ai-finance-workflows-governance|the CFA Institute roundtable]], which reaches the same conclusion that governance has to move upstream of the model.

Chatterjee is careful that these are **observed, not hypothetical**: enterprises have already reported *"agents that looped indefinitely on a flawed instruction, agents that invoked the wrong API with elevated credentials, and multi-agent systems where one agent's error propagated into a second agent's decision."* His framing of why that matters — *"ordinary operational fragility, once confined to human error, is now compounding at machine speed"* — is the article's second most quotable line.

## The definition, and the five capabilities

> *"Agentic governance is not a policy document or an ethics checklist. It is an operational capability: the demonstrable ability to know, at any moment, what every agent in the enterprise is authorized to do, what it has done, and how quickly it can be stopped."*

| Capability | What it requires |
| --- | --- |
| **Action-scoped permissions** | minimum tools and data per task, not inherited broad credentials |
| **Real-time action visibility** | live auditable record of every *action*, not just the prompts received |
| **Circuit breakers and kill switches** | any agent or chain halted immediately on deviation |
| **Escalation thresholds** | defined in advance, *"calibrated to consequence and reversibility, not convenience"* |
| **Cross-agent identity and provenance** | when one agent acts on another's output, origin, authorization and confidence are traceable |

**The escalation-threshold criterion is a direct hit on the corpus's existing finding.** [[agent-oversight-and-delegation]] already records that trust is calibrated per task, and that the trigger is **irreversibility × external visibility, not stakes**. Chatterjee, coming from cybersecurity with no apparent contact with that literature, lands on *consequence and reversibility* — a fifth independent arrival at the same control axis.

## Commitment–Preparedness–Discipline

The article maps its own **CPD framework** onto agentic governance, and each pillar comes with the failure it exposes:

- **Commitment** (leadership and intent) — the C-suite defines in *business* terms which decisions an agent may make unsupervised. *"Board-level visibility into what autonomous systems are authorized to do is now as material as visibility into financial controls."* **Common failure: agents deployed team by team with no enterprise view of cumulative exposure.**
- **Preparedness** (capability) — a live inventory of every production agent, its permissions, tool access and failure modes; plus **red-teaming agentic workflows the way security teams red-team networks**. **Common failure: organisations cannot produce a complete list of the agents running in their environment.**
- **Discipline** (execution) — ongoing permission audits, *tested* kill switches, logged and reviewed actions, and drills. **Hardest failure: "kill switches that exist on paper but have never been exercised under realistic conditions."**

And the metric, which is the contribution this wiki was missing:

> *"Regular drills that simulate an agent behaving badly, measuring not whether it can be stopped, but **how long it takes**."*

[[agent-oversight-and-delegation]] has carried an open question that **nobody reports a false-approve rate for any risk-scored gate**. This does not close it, but it proposes the adjacent measurable — **time-to-halt** — and it is the first concrete oversight metric in the corpus.

The article's single test for whether any of this is working: *"Can the enterprise show, for any agent action, that it was bounded, authorized, and reversible — not as a one-time launch review, but as a standing operational capability?"*

## Dynamic capabilities (Warner & Wäger)

- **`digital-transforming/redesigning-internal-structures`** — the prescription is explicitly structural and cross-functional: board-level risk appetite, clear single ownership for agent behaviour (*"fragmented accountability… is a root cause of agentic risk"*), and vendor diligence extended to autonomous capability.
- **`contextual/internal-barriers`** — the three pillars are each introduced by the organisational failure they expose: no enterprise view of cumulative exposure, no agent inventory, untested kill switches. These are governance-capability gaps, not technical ones — *"the capability gap is not technical sophistication. It is the absence of inventory, visibility, and rehearsed control."*
- **`digital-sensing/digital-scenario-planning`** — the recommended practice is rehearsal under adverse scenarios: red-teaming agentic workflows, running failure drills against a misfiring agent, a poisoned input, a cascading multi-agent error, and *measuring actual detection and response time rather than assuming it*.

## Linked entities and concepts

- Concepts: [[agent-oversight-and-delegation]], [[responsible-ai]], [[multi-agent-failure-modes]], [[attack-surface-management]], [[ai-agents]], [[enterprise-ai-adoption]], [[agent-harness]]
- **Dangling** (single-source mention, deferred): Dave Chatterjee, Analytics Magazine, INFORMS, the CPD framework

## Scope and reliability

**A practitioner column, not research.** Roughly 1,900 words, no citations, no data, no methodology. The incident classes are described in aggregate (*"enterprises have already reported…"*) with **no source, no counts and no named organisations**, so they function as illustration rather than evidence. The CPD framework is the author's own, carried over from his prior columns on quantum readiness and crypto-agility, and the article is partly an argument that the same organisational failure repeats across security transitions.

**What it is good for:** vocabulary (autonomy creep, tool and API sprawl, action-scoped permissions, cross-agent provenance), the copilot-governance-fails-for-agents framing, the CPD mapping, and the **time-to-halt** metric. **What it is not:** a source for how common any of these failures are, or for whether the five capabilities work. Cite [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail|MAST]] for measured failure taxonomy.

The INFORMS DOI gives it a citable identity that most practitioner writing in this corpus lacks, which is worth noting but should not be mistaken for peer review — *Analytics Magazine* is INFORMS' membership publication, not one of its journals.

## Debates and supersession

- **Oversight and value are structurally opposed**, per the quote above. The corpus's oversight material has generally treated weak oversight as a discipline failure. This reframes it as an incentive problem: the organisation is *paying* to remove the control. If that reading is right, prescriptions that rely on organisational willpower will keep failing, and only architectural constraints (action-scoped credentials, circuit breakers) will hold.
- **Consequence-and-reversibility now has five independent arrivals** (a regulator, a solo founder, a product executive, a human-factors study, and a cybersecurity academic). At some point convergence this broad stops being corroboration and starts being a sign that the axis is obvious; the wiki should watch for a source that *disagrees* rather than counting more agreements.
- Open: nothing here is measured. Time-to-halt is proposed as a metric and reported by nobody — including this article. The corpus still has zero numbers on any oversight gate's performance.
