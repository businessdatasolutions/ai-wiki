---
type: entity
kind: benchmark
aliases: ["Berkeley Function Calling Leaderboard", "BFCL", "BFCL v3", "BFCL v4", "Gorilla leaderboard", "function calling leaderboard"]
tags: [berkeley-function-calling-leaderboard, bfcl, ai-benchmarks, function-calling, tool-use, ast-evaluation, multi-turn, agentic-evaluation, uc-berkeley, gorilla]
confidence: 0.85
last_confirmed: "2026-09-04"
accessed_at: "2026-09-04"
source_count: 3
relationships:
  - type: part-of
    target: ai-benchmarks
    via: "the corpus's reference benchmark for tool-calling capability; listed on the ai-benchmarks roster"
  - type: published-by
    target: UC-Berkeley
    via: "built and maintained by the Gorilla project in Berkeley's Sky Computing Lab; paper at ICML 2025"
---

# Berkeley Function Calling Leaderboard (BFCL)

The **de-facto standard benchmark for LLM function calling / tool use**, built and maintained by the Gorilla project at [[UC Berkeley]]'s Sky Computing Lab. Live at `gorilla.cs.berkeley.edu/leaderboard.html`; evaluation code open on GitHub; refreshed roughly quarterly, tracking on the order of **110 model families** with vendor-supplied runs plus verification.

On the [[ai-benchmarks]] roster it is the one domain where the field has converged on a single vendor-neutral instrument. Full treatment on the source page: [[2025-07-13-patil-berkeley-function-calling-leaderboard]].

## What it measures

**5,551 question–function–answer pairs** across Python, Java, JavaScript, REST and SQL, in four sections: **single-turn** (simple / multiple / parallel / parallel-multiple / irrelevance), **crowd-sourced** (2,251 entries curated from >67,000 real community-contributed queries, 15+ languages), **multi-turn** (eight API suites, 1,000 queries, with missing-parameter, missing-function and long-context variants), and **agentic** (web search, memory, SQL).

Its methodological signature is **Abstract Syntax Tree sub-string matching** as a proxy for executing the call — validated against execution on a subset, which is what makes the shortcut defensible. Multi-turn entries are scored by both final-state match and required-call-path match.

Version history: **v1** introduced AST evaluation, **v2** added enterprise and community-contributed functions, **v3** added multi-turn, **v4** added holistic agentic evaluation.

## Two things to know before citing a BFCL number

1. **"Overall Accuracy" is a composite index, not a per-call success rate.** It weights sections of wildly different difficulty. A model at 66 overall can be at 95 on single-turn calls and at 6 on memory. Stated cleanly by [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Sokolenko]] answering exactly this audience question: *"It's a combined score of four other scores. Think of it as an index… accuracy is the wrong name for it."*
2. **Every rank is an artefact of its date.** xLAM-2-70b and -32b held ranks 1 and 2 in April 2025 ([[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2|APIGen-MT, Table 1]]); by the December 2025 snapshot the top was Claude Opus 4.5 / Gemini 3 / GLM 4.6 and xLAM-2 sat around position 18. The models did not regress; the board moved.

## The structural finding

Single-turn function calling is **saturated** — frontier models cluster in the high 80s and 90s. Multi-turn state, memory and long-horizon reasoning are **not**: the best memory score in the paper's Table 1 is 12.0 out of 100. Any claim of agentic parity between two models that rests on single-turn numbers is resting on the saturated half.

## Appears in this wiki via

- [[2025-07-13-patil-berkeley-function-calling-leaderboard]] — the ICML 2025 paper (primary).
- [[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2]] — [[xLAM]]-2 evaluated on BFCL v3; ranks 1, 2 and 4 as of 3 April 2025.
- [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models]] — used on stage as the shopping list for a locally-runnable tool-calling model; the composite-index caveat.
- [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai]] — argues (barrier B2) that measuring SLMs on *agentic* benchmarks rather than generalist ones is what reveals their sufficiency; BFCL is the instrument that makes this possible.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "bfcl")
SORT file.name ASC
```
