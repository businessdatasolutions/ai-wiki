---
type: source
kind: paper
title: "The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models"
author: ["Shishir G. Patil", "Huanzhi Mao", "Fanjia Yan", "Charlie Cheng-Jie Ji", "Vishnu Suresh", "Ion Stoica", "Joseph E. Gonzalez"]
publisher: "University of California, Berkeley (Sky Computing Lab / Gorilla project); Proceedings of the 42nd International Conference on Machine Learning (ICML 2025), PMLR 267:48371–48392"
url: "https://proceedings.mlr.press/v267/patil25a.html"
leaderboard: "https://gorilla.cs.berkeley.edu/leaderboard.html"
date_published: 2025-07-13
date_ingested: 2026-09-04
length: "~22 pages including appendices (full text read; Table 1 read against the live leaderboard because pypdf extraction flattens its columns)"
raw: "../../raw/papers/berkeley-function-calling-leaderboard.md"
tags: [berkeley-function-calling-leaderboard, bfcl, ai-benchmarks, function-calling, tool-use, ai-agents, uc-berkeley, gorilla, ast-evaluation, multi-turn, agentic-evaluation, memory, data-contamination, icml-2025, ion-stoica, joseph-gonzalez]
dynamic_capabilities:
  - digital-sensing/digital-scouting
relationships:
  - type: supports
    target: 2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2
    via: "BFCL is one of the two benchmarks (with τ-bench) that xLAM-2 reports against, and the xLAM family appears in BFCL's own Table 1 across five sizes — so the two papers are instrument and instrument-user. Read together they also show the instrument working as intended: xLAM-1b-fc-r scores 18.7 overall while xLAM-8x7b-r scores 44.2, i.e. the benchmark does *not* simply reward small models, which is what makes a small model placing high on it informative"
    confidence: 0.85
  - type: supports
    target: 2023-10-10-jimenez-swe-bench-real-world-github-issues
    via: "the same benchmark-design problem solved for a different capability. SWE-bench made software-engineering ability measurable by executing real repository tests; BFCL made tool-calling measurable by replacing execution with Abstract Syntax Tree sub-string matching, then validating that proxy against execution on a subset. Both papers' contribution is the evaluation method more than the ranking it produces"
    confidence: 0.75
  - type: supports
    target: 2025-03-17-cemri-why-do-multi-agent-llm-systems-fail
    via: "independent evidence for the same conclusion from opposite methods. MAST taxonomises multi-agent failures by hand-annotating traces; BFCL finds the same fault line numerically — top models score in the 90s on single-turn calls and collapse on multi-turn and agentic categories (best memory score in Table 1 is 12.0 out of 100). Both locate the failure in state, memory and long-horizon coordination rather than in the individual call"
    confidence: 0.8
---

# Patil et al. (UC Berkeley) — The Berkeley Function Calling Leaderboard (BFCL)

The **UC Berkeley research** [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Serhii Sokolenko points his PyCon DE audience at]], and the reason the wiki now holds it: BFCL is the instrument almost every "this small model calls tools as well as a frontier model" claim is measured on, including the ones in the [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|NVIDIA SLM position paper]].

Seven authors from **[[UC Berkeley]]** — including **Ion Stoica** and **Joseph E. Gonzalez**, out of the Gorilla project / Sky Computing Lab. ICML 2025. The paper is a retrospective: BFCL had already run through four public versions by the time it was written, and the paper *"collapses the timeline and condenses all the learnings."*

## TL;DR

Function calling — an LLM invoking external functions, APIs or tools — is the capability agentic applications are built on, and until BFCL there was no standard way to measure it. Two reasons it was hard: **deciding when a function call is valid is genuinely difficult**, and **acquiring diverse real-world functions is difficult**. BFCL's answers to those two problems are its actual contributions.

> *"While state-of-the-art LLMs excel at single-turn calls, memory, dynamic decision-making, and long-horizon reasoning remain open challenges."* — Abstract

That sentence is the finding this wiki should carry forward. The leaderboard's headline column is not the interesting part; the **gap between its columns** is.

## What's in it

**5,551 question–function–answer pairs** across Python, Java, JavaScript, REST APIs and SQL, in four sections:

| Section | Content |
| --- | --- |
| **Single-turn** | five scenario types — *simple* (one tool, one call), *multiple* (several tools, one call each), *parallel* (one tool, several calls), *parallel multiple*, and *irrelevance* (tools available but none should be invoked) |
| **Crowd-sourced** | **2,251 entries curated from >67,000 community-contributed real-life datapoints** (64,517 real user queries collected 26 Feb – 1 Apr 2024), deduplicated by ROUGE-L and embedding similarity, minimally edited by human experts. **The first benchmark to put genuine user queries into function-calling evaluation** — and multilingual, with 15+ languages represented |
| **Multi-turn** | eight curated API suites, 1,000 queries, in four categories — *base*, *missing parameters*, *missing functions*, *long context* — with human-annotated ground-truth trajectories |
| **Agentic** | three categories — **web search** (DuckDuckGo + fetch), **memory** (five domains: college advising, customer support, medical assistant…, with snapshot-then-probe evaluation across short- and long-term gaps), and **SQL** (a JSON schema of SELECT/INSERT/UPDATE/DELETE with WHERE/LIMIT/JOIN, so a natural-language question becomes a deterministic composition of function calls) |

## The methodological contribution: AST matching

The problem: validating a function call deterministically usually means **executing** it, which caps how many functions you can include and how fast you can evaluate.

BFCL's solution — borrowed from programming-language tooling, and structurally the same move [[2023-10-10-jimenez-swe-bench-real-world-github-issues|SWE-bench]] made for software engineering (find a deterministic oracle, then build the benchmark around it) — is **Abstract Syntax Tree sub-string matching**. Restrict the model's output to Python-callable calls, parse with Python's `ast` module, extract function name and parameters, then check that the name matches exactly and every parameter value falls inside a predefined set of valid values. No execution, so it *"can easily scale to thousands of functions."*

The paper does not just assert the proxy is sound — it **validates it**, evaluating a subset both ways and reporting a strong correlation between AST scores and execution-based scores (Figure 3). That validation is what makes the shortcut respectable, and it is the part most worth borrowing.

Multi-turn entries get a **double check**: *state-based* (does the world end up in the ground-truth state after each turn — catches modifications like creating a file) plus *response-based* (did the model actually take the minimal viable call path — catches read-only requests where it could have guessed). An entry is correct only if it passes both, in every turn. Agentic entries are scored by strict exact match on an isolated answer field, precisely so that *"I am not sure because no relevant information was found"* isn't scored as a "no".

## What the numbers say

Two findings matter more than the ranking.

**1. The cliff between single-turn and everything else.** Top models sit in the high 80s and 90s on single-turn AST categories and fall off a cliff on multi-turn and agentic. In the paper's Table 1, `gpt-4o-2024-11-20` leads on overall score at **66.4** while scoring 95.5 on single-turn simple AST — and **6.0 on memory**. The best memory score anywhere in the table is **12.0 out of 100**. Long-horizon state, not call syntax, is where tool use is unsolved.

This is the same fault line [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail|MAST]] found by hand-annotating multi-agent traces, reached here by measurement.

The corollary matters for how the corpus reads model comparisons. A model whose advantage is concentrated in the multi-turn column — as [[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2|xLAM-2's]] is — is claiming something narrow and real; a model claiming parity on the overall column is usually claiming parity on the saturated half.

**2. Native function-calling mode is not uniformly better than prompting.** Models that support both a `tools` API field ("FC mode") and system-prompt-driven structured output ("prompting mode") often do **better prompted**. Prompting models produce ~3× more decoding errors (412.93 vs 182.5 out of 4,251 entries) — the structured mode is easier to parse — but among successfully decoded responses FC models make *more* incorrect calls in the multiple-function category (77.5 vs 21 on average). The paper's explanation: FC mode's structural constraints limit flexibility in complex scenarios. Concrete example given: Claude cannot execute parallel function calls in FC mode but can when prompted; and for Java or JavaScript, prompting generally beats FC.

That is a **harness-design finding disguised as a benchmark result** — see [[agent-harness]]. Which interface you hand the model changes its measured capability.

**3. Contamination is checked, not assumed.** Because BFCL was released in phases, the authors compare model familiarity (via CharNLL / perplexity ratios) with the single-turn set against the crowd-sourced set released six months later, as a test for training-data leakage into the older split. A benchmark that instruments its own decay is rare and worth noting.

## How to read the Overall Accuracy column

The single most useful caveat about BFCL for this wiki does not come from the paper but from [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Sokolenko's Q&A]], answering an audience member who assumed a 70-ish top score meant 30% of agent responses are garbage:

> *"It's a combined score of four other scores. Think of it as an index. It's just an index, and accuracy is the wrong name for it. It should be called overall index."*

The paper's own structure confirms this: Overall Accuracy aggregates across single-turn, crowd-sourced, hallucination-measure, multi-turn and agentic sections, which have wildly different difficulty. A 66.4 overall is a model at ~95 on single-turn calls and ~6 on memory. **Never read the overall column as a per-call success rate**, and prefer the sub-scores when the question is about a specific capability. Recorded on [[ai-benchmarks]].

## Why it exists — the prior art it rejects

The related-work section is a useful map of why previous tool-use benchmarks weren't sufficient, and the objections are methodological rather than territorial:

- **APIBench / Gorilla** (the same group's own earlier work), **AppBlend** — single-turn only; metrics focus on functional correctness and miss semantic errors or usage variation.
- **τ-bench** — only 28 functions across two domains (airline, retail); **RestBench** — TMDB and Spotify only. Narrow coverage (<150 entries) invites overfitting.
- **ToolSandbox, τ-bench** — rely on an LLM to simulate the user, and *"LLM-based users remain prone to hallucination and instruction-following errors, which confound evaluation."*
- **ToolBench** — depends on live RapidAPIs with high performance variance, so results don't reproduce. **StableToolBench** caches responses but then uses an LLM judge, risking model-induced bias (GPT-family judges favouring GPT-family answers).
- **TinyAgent** — handles nested calls with placeholder variables rather than real execution output, so it's effectively still single-turn.

The through-line: **deterministic evaluation, real functions, real user queries, no LLM in the judging loop.**

## Dynamic capabilities (Warner & Wäger)

- **`digital-sensing/digital-scouting`** — BFCL is infrastructure *for* scouting: a continuously-refreshed, vendor-neutral instrument that lets an organisation see which models can actually call its tools, including which open-weight models are close enough to substitute for a frontier API. That is precisely how [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Sokolenko uses it]] — to find the highest-ranked model he is allowed to run locally.

No other W&W cell fits: this is a measurement instrument, not a transformation programme.

## Linked entities and concepts

- Concepts: [[ai-benchmarks]], [[ai-agents]], [[small-language-models]], [[agent-harness]], [[multi-agent-failure-modes]]
- Entities: [[UC Berkeley]], [[Berkeley Function Calling Leaderboard]], [[xLAM]], [[Salesforce AI Research]], [[Anthropic]], [[OpenAI]], [[Google]]
- **Dangling** (single-source mention, deferred): Shishir G. Patil, Ion Stoica, Joseph E. Gonzalez, Sky Computing Lab, Gorilla, τ-bench, ToolBench, ToolSandbox, APIBench

## Scope and reliability

The strongest kind of source this wiki holds: **peer-reviewed (ICML 2025), method-first, self-validating** (the AST proxy is checked against execution), **contamination-aware**, and with the artefact publicly inspectable and continuously updated.

Two limits to state honestly. First, **the paper is a snapshot of a moving target**: it condenses BFCL v1–v4, and the live leaderboard has moved on — the model rankings quoted here and in Sokolenko's talk are already historical, and the wiki should cite the *method and the structural findings*, not the ordering. Second, **vendors supply their own runs**; there is verification, but the leaderboard is not an adversarial audit, and a benchmark this influential is a target for optimisation (which is the point of the contamination check, and also the reason to keep watching it). On the raw side, the co-located PDF's Table 1 does not survive `pypdf` extraction with columns intact — figures quoted above were read against the live leaderboard.

## Debates and supersession

- **Does a high BFCL score mean a model works as an agent?** The paper's own answer is no, and it is the finding: single-turn competence has saturated while multi-turn state, memory and long-horizon reasoning have not. Any source citing BFCL to claim general agentic parity between a small and a large model — including [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|the NVIDIA position paper]]'s capability roster — is leaning on the sub-score where saturation already happened.
- **FC mode vs prompting** unsettles the assumption that a model's native tool API is the best way to use it. The wiki records this as an open harness-design question, not a resolved one.
- Open: BFCL evaluates the *model*, holding the harness fixed. Nothing here separates model capability from scaffold quality — the same confound the [[ai-benchmarks]] page tracks under scar-fragmentation.
