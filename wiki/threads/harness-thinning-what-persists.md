---
type: thread
status: closed
opened: 2026-07-15
closed: 2026-07-15
tags: [agent-harness, harness-thinning, meta-harness, subtraction-principle, model-eats-the-harness, runtime-security, agent-identity, cross-vendor-convergence]
---

# Thread: Why do independent vendors converge on "harnesses thin as models improve" — and what does thinning actually leave behind?

## The question

A same-day 7-video batch (2026-07-15 ingest) landed three sources that each touch the [[agent-harness]] concept's existing "subtraction principle" material from a different angle: [[2026-07-08-jensen-huang-why-companies-need-open-agent-systems|Jensen Huang (NVIDIA), interviewed by Harrison Chase (LangChain)]] frames companies as built "on harnesses, not business processes" and describes post-training a model *inside* a harness; [[2026-07-10-building-the-future-of-agentic-infrastructure|Anthropic's own Claude Platform team]] gives the wiki's first first-party interview account of harnesses getting thinner as models improve, and names "meta-harnesses" as what teams build once individual harnesses thin; [[2026-07-09-nyc-executive-forum-2026-a-leaders-guide-to-agentic-ai|Ishit Vachhrajani (AWS)]] doesn't use "thinning" vocabulary directly but describes Amazon Bedrock AgentCore as a trust-infrastructure layer that hardens even as the "advanced team structures" franchise's own economics (USE/COMPOSE/BUILD) assume the business-logic layer keeps shrinking.

This lands on top of an **existing, unresolved wiki debate**: [[agent-harness]]'s Debates section already holds a live tension between [[2026-06-11-kilpatrick-sequoia-model-eats-the-harness|Kilpatrick (Google DeepMind, June 2026)]] — who predicts the model **absorbs the harness natively within ~12 months**, so harness-alpha is transient — and [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]]'s "model rented, harness owned" framing, where the harness is a durable, compounding asset. Both agree on the *mechanism* (harness components encode assumptions about model limitations, and those assumptions expire); they disagree on the *strategic conclusion* (does the harness eventually vanish, or does it persist in a different shape?).

**The question this thread tracks:** *Do the three new July 2026 sources settle, sharpen, or merely restate the Kilpatrick/Chatterjee tension — and specifically, when a harness thins, what (if anything) is left, and does it thin uniformly or by layer?*

## Why this thread opened-and-closed in the same session

The three sources, plus the wiki's existing agent-harness material (subtraction principle, the Prompt Engineering empirical anchor, the Kilpatrick debate), were fully read and cross-referenced during the same-day ingest that landed them — see the [[2026-07-14-khan-academy-ceo-the-real-ai-opportunity-is-in-boring-industries-sal-khan|7-video batch]] processed 2026-07-15. No further sourcing was needed to answer the question at hand; per CLAUDE.md §Synthesis, this thread is the schema-compliant antecedent to the synthesis below rather than a substantive open investigation.

## Closed

Filed [[harness-thinning-what-persists]] synthesis on 2026-07-15. Headline finding: **thinning is layer-specific, not uniform — the business-logic content of a harness thins as models improve, while the identity/trust/access-control substrate around it hardens.** This resolves the Kilpatrick/Chatterjee tension partially: Kilpatrick is right about the *business-logic* layer (it does erode toward the model); Chatterjee is right about the *governance* layer (it does not — if anything, three independent vendors are actively building more of it, not less). Neither "the harness vanishes" nor "the harness is the permanent moat" is correct as a single claim about the whole harness; both are correct about different halves of it.
