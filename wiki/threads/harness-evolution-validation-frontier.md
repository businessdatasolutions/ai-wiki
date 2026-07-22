---
type: thread
status: open
opened: 2026-07-22
tags: [agent-harness, harness-evolution, behavior-localization, empirical-validation, benchmark-gap, meta-harness, continual-harness, executed-edits]
---

# Thread: How well-validated is harness evolution, really — does measured harness lift survive to executed, tested outcomes?

## The question

The [[agent-harness]] concept page now holds a substantial **harness-evolution** literature — sources that build, optimise, prune, and localize edits within an agent harness. Each reports a *lift* on some metric. But the metrics differ in how far they are from a real, shipped, tested outcome, and a recurring gap runs through the whole cluster: **the lift is measured at a proxy layer (plan quality, milestone completion, LLM-judged localization) rather than at the layer that matters in production (an edit that executes and passes the harness's own tests, or a task that a user would accept).**

This thread tracks one question across sources: *when a harness-evolution method reports an improvement, how well is that improvement validated against executed-and-tested outcomes — and where is the benchmark that would close the gap?*

## Why it's a thread and not a per-source note

The gap is not unique to any one paper — it recurs, and the individual open questions are currently **scattered across source and concept pages where no reader sees them together**:

- [[2026-07-14-wang-shi-harness-handbook-behavior-localization|Wang, Shi et al. — Harness Handbook (Jul 2026)]] reports localization/edit-plan gains (win rate 38.3/28.3 on Codex, 45.6/26.7 on Terminus-2; symbol-F1 +18.8 vs Opus 4.8 reference plans) — but plan quality is **LLM-judged against reference plans**, not measured by whether the executed edit lands green on the harness's own tests. This is the executed-edits gap in its sharpest form: the paper's own workflow ends at *plan*, with execution and test deferred.
- [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten et al. — Continual Harness (May 2026)]] measures a real end-to-end outcome (Pokémon milestone completion + USD cost) and reports a **capability floor** (every Continual Harness variant *underperforms* the minimalist baseline on Gemini Flash-Lite) — the strongest honest negative result in the cluster, but on **embodied game-play, not coding**. Its own open question ("does the Refiner architecture work on SWE-bench / Terminal-Bench?") is the coding-side of exactly this validation gap.
- [[2026-03-26-pan-natural-language-agent-harnesses|Pan et al. — Natural-Language Agent Harnesses (Mar 2026)]] reports the OS-Symphony migration jump (30.4% → 47.2%) and SWE-bench-verified ablations — but the wiki carries these **second-hand** via the [[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering synthesis]]; the primary source (arXiv:2603.25723) is an open **ingest target**.
- **Lee/Khattab et al. — Meta-Harness (arXiv:2603.28052)** reports Terminal-Bench-2 76.4% and cross-five-model transferability — also carried **second-hand**; primary-source ingest is open. Tracked on [[2026-03-30-lee-meta-harness-end-to-end-optimization|the Meta-Harness stub]] and in the [[agent-harness]] Open-questions section.
- [[2026-03-05-lou-deepmind-autoharness-code-harness-synthesis|Lou et al. — AutoHarness (Mar 2026)]] synthesises harness code; the same question applies (does synthesised harness code produce executed, tested improvements, or is the gain measured upstream?).

Put together, these are one frontier, not five footnotes: **the field measures harness lift at whatever proxy is cheapest to score, and the executed-and-tested end-to-end number is mostly missing or second-hand.**

## Candidate sources (to gather / ingest)

- **Primary-source ingest of Pan et al. (arXiv:2603.25723)** — would replace the second-hand SWE-bench-verified numbers with the paper's own methodology and let us check whether its lift is executed-and-tested or plan-level.
- **Primary-source ingest of Lee/Khattab Meta-Harness (arXiv:2603.28052)** — Terminal-Bench-2 76.4% is an *executed* benchmark; ingesting it would give the cluster its clearest executed-outcome anchor and let us verify the transferability claim.
- **Any end-to-end harness-evolution benchmark** that runs the full localize → plan → execute → test loop and reports a pass/fail (or accept-rate) outcome, not a judged plan score. None currently in the wiki. Watch SWE-bench / Terminal-Bench leaderboards and the Harness Handbook project page ([ruhan-wang.github.io/Harness-Handbook](https://ruhan-wang.github.io/Harness-Handbook/)) for a follow-up with execution results.
- **A replication of Karten's capability-floor result on coding harnesses** — would test whether "below a capability floor, harness engineering doesn't help" is a general property or a Pokémon-specific artifact.

## How this thread should resolve

Close into a `wiki/syntheses/` page when enough evidence is in to answer: *across the harness-evolution literature, how much of the reported lift is validated against executed, tested outcomes — and what is the honest current state of the evidence (which claims are executed-benchmark-anchored, which are plan/proxy-level, which are second-hand)?* A resolving synthesis would produce:

- A **validation-tier table** classifying each source's headline result by how far it sits from an executed-and-tested outcome (executed benchmark / real end-to-end proxy / LLM-judged plan / second-hand).
- A verdict on whether the **capability-floor** finding generalises beyond embodied game-play.
- A statement of what benchmark the field still lacks (the end-to-end localize→plan→execute→test number) and whether anyone has since published it.

Until then this thread stays **open** — it is a genuine gather-more-evidence investigation, not a same-session antecedent.

## Related

- Concept: [[agent-harness]] (§Behavior localization; §The empirical anchor; Open questions).
- Sibling synthesis: [[harness-thinning-what-persists]] — answers *what persists when a harness thins*; this thread asks the orthogonal question *how well-validated are the harness-evolution claims in the first place*.
