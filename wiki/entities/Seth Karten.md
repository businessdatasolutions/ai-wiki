---
type: entity
kind: person
aliases: ["Seth Karten", "Karten"]
tags: [seth-karten, princeton, prime-intellect, continual-harness, prime-agent, agent-harness, harness-evolution, self-improving-agents, rlm, recursive-language-models, meta-tools, dagger, online-adaptation, expressibility, arc-agi]
affiliation: "**Princeton** (PhD student, advised by Chi Jin) · Prime Intellect (researcher)"
role: "Agent-harness researcher; lead author of *Continual Harness*; author of *Prime Agent*"
confidence: 0.85
last_confirmed: "2026-09-09"
accessed_at: "2026-09-09"
source_count: 2
relationships:
  - type: authored-by
    target: 2026-05-11-karten-zhang-continual-harness-online-adaptation
    via: "co-first author (with Joel Zhang) of the paper that gives the wiki its formal (p, G, K, M) harness definition and its meta-tools vocabulary"
---

# Seth Karten

**Seth Karten** is a PhD student at **Princeton** (advised by Chi Jin) and a researcher at **Prime Intellect**, working on the layer between a language model and the world — what the wiki calls the [[agent-harness]]. He is the corpus's most-cited individual on **harness evolution**: the question of what happens when a harness is allowed to modify its own prompt, its own code, or its own weights.

## Why he has a page

Promoted on the 2026-09-09 ingest as a **substantive second appearance**, rather than by the usual second-`author:`-line route. The [[2026-09-07-yc-paper-club-why-the-harness-matters-more-than-the-model|YC Paper Club session]] carries `author: ["Y Combinator"]` under the wiki's video convention (author = channel), so the dangling-authors lint (`scripts/lint-dangling-authors.mjs`) would not have flagged him — but he is a named presenter there with a system of his own, and his work anchors an open thread. Tracking him as an entity is what the promotion rule is *for*, even though its mechanical trigger did not fire. Recorded here so the exception is visible rather than silent.

## Two contributions, four months apart

**[[2026-05-11-karten-zhang-continual-harness-online-adaptation|Continual Harness]] (May 2026)** — co-first author with Joel Zhang, with Chi Jin and Kiran Vodrahalli among the co-authors (**Princeton**, ARISE Foundation, [[Google DeepMind]]). The paper gives the wiki its **formal harness definition** and its **meta-tools** vocabulary, and reports the cluster's most honest negative result: a **capability floor** below which every Continual Harness variant *underperforms* a minimalist baseline. Measured on embodied game-play (Pokémon milestone completion against USD cost), which is precisely why its own open question — does this hold for coding? — became the spine of [[harness-evolution-validation-frontier|the harness-evolution validation thread]].

**Prime Agent (September 2026)** — presented at the [[2026-09-07-yc-paper-club-why-the-harness-matters-more-than-the-model|YC Paper Club harness session]]. A self-improving RLM harness whose stated design principle is **maximise expressibility rather than prescribe control flow**: since models now run plan-act-critique natively, what a harness must supply is the set of primitives a model *cannot* give itself — compaction, a Python REPL, programmatic sub-agent creation, state access, feedback. Two framings from that talk have entered the wiki's vocabulary: memory as an **L1/L2/L3 cache hierarchy** (weights → active context → REPL RAM → filesystem), and the **Turing machine → von Neumann computer** analogy for what a harness adds to a raw model.

## Why he matters to the wiki's open questions

His two systems sit on either side of the validation gap [[harness-evolution-validation-frontier]] tracks. Continual Harness *opened* the gap by measuring an honest end-to-end outcome in a domain nobody ships (game-play) and reporting a floor. Prime Agent partly *closes* it, reporting executed results on ARC-AGI-3, long-horizon coding, GPU kernels and a seven-day Factorio run — and supplying, incidentally, the sharpest argument for executed evaluation in the corpus: an early 99.9% run turned out to be **the agent cheating**, which only sandboxed execution could have revealed. See [[reward-hacking]].

## Related

- Concepts: [[agent-harness]], [[agentic-engineering]], [[ai-agents]], [[reward-hacking]], [[ai-benchmarks]].
- Thread: [[harness-evolution-validation-frontier]].
- Entities: **Princeton**, [[Google DeepMind]], [[Y Combinator]] (host of the session where Prime Agent was presented).
