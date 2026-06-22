---
type: entity
kind: person
aliases: ["Ryan Lopopolo"]
tags: [ryan-lopopolo, openai, codex, harness-engineering, agent-first-engineering, member-of-technical-staff]
affiliation: "[[OpenAI]] (Member of Technical Staff)"
role: "Member of Technical Staff, OpenAI (Codex); coiner of the term 'harness engineering'"
confidence: 0.8
last_confirmed: "2026-06-20"
accessed_at: "2026-06-20"
source_count: 2
---

# Ryan Lopopolo

**Ryan Lopopolo** is a Member of Technical Staff at [[OpenAI]] (on Codex) and the **coiner of the term "harness engineering"** — the wiki's canonical name for the discipline of building software where humans steer and agents execute. The wiki promotes him from Dangling to an entity page on **2026-06-20** after the second substantive source.

Promoted on the second source per the [author-entity-promotion rule](../../CLAUDE.md#author-entity-promotion):

1. **First source** — [[2026-02-11-lopopolo-codex-harness-engineering|*Harness Engineering* (OpenAI Codex blog, Feb 2026)]]: the wiki's first **vendor-side production case study** of harness engineering — five months, ~1M LOC, ~1,500 PRs, 7 engineers, **0 manually-written lines**, with the operational invariants the [[agent-harness]] concept now carries (repository-as-system-of-record, AGENTS.md as table-of-contents, layered architecture mechanically enforced, golden-principles + scheduled GC, doc-gardening agent).
2. **Second source (this promotion)** — [[2026-06-19-lopopolo-ai-native-devcon-harness-engineering|*Harness Engineering: How to Build Software When Humans Steer and Agents Execute* (AI Native DevCon, Jun 2026)]]: the conference-talk articulation — the **named definition**, the **three-phase context-delivery model** (ground → just-in-time-steer-via-tool-calls → LM-as-judge review), the **shift-right** counter-prescription, and the **"never give the same review feedback twice → make every mistake statically impossible"** governing rule.

## Role in the wiki

Lopopolo is the wiki's **practitioner-origin voice on [[agent-harness|harness engineering]]** — the person whose vocabulary the rest of the harness corpus relays (e.g. [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler]] propagates the *harness engineering* name explicitly crediting the Codex team). His two sources are complementary: the blog is the **artifact-shape inside one repo**; the talk is the **discipline definition + operating loop**.

### The harness-engineering definition (his own words)

> *"Harness engineering is making context around what it means to do a good job legible, and then just-in-time surfacing it to the agent over the course of its trajectories in order to steer and refine its output."*

Governing rule: **"I never want to give the same review feedback twice"** — every correction is driven down a durability ladder (trash-and-reprompt → write it down → reviewer agent judges every diff → statically-verifiable lints/guardrails/tests).

### Distinctive contributions

- **Three foundational limits** that remain in a human+agent team: human time (the scarce resource — remove your own synchronous attention), human/model attention ("attention must sum to one"), and the context window (still scarce despite auto-compaction).
- **Shift right, not left** — put interventions as far right as possible to minimise synchronous human time; agents auto-discover the relevant guardrails by change category.
- **All code is prompts** — unify the codebase on consistent patterns so the model doesn't burn attention disambiguating (one observability stack, not six); **prune latent space** to tell the model which of the choices it has seen in training to make.
- **Coarse structural guardrails** — snapshot tests with 100% branch coverage; statically banning `any`/`unknown`; reviewer agents as "a matrix CI job that points at a bunch of markdown files to judge."
- **The group-tech-lead operating mode** — care about invariants, interfaces, and whether components "do what they say on the tin," not every keystroke; **vibe coding** is part of what makes this possible.

## Career snapshot

- **OpenAI** — Member of Technical Staff (Codex). Early adopter of Codex CLI for end-to-end engineering work; the Codex blog's named author.
- **Open source** — maintains Rust crates from his **Artichoke** project (a Ruby interpreter in Rust), e.g. `artichoke-rand-mt` (a Mersenne Twister implementation), where he is now applying Codex-app automations to maintenance.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "ryan-lopopolo")
SORT file.name ASC
```
