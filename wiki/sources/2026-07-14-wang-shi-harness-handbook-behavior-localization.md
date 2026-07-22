---
type: source
kind: paper
title: "Harness Handbook: Making Evolving Agent Harnesses Readable, Navigable, and Editable"
author: ["Ruhan Wang", "Yucheng Shi", "Zongxia Li", "Zhongzhi Li", "Yue Yu", "Junyao Yang", "Kishan Panaganti", "Haitao Mi", "Dongruo Zhou", "Wei Liang Leo"]
affiliations: ["Tencent HY LLM Frontier", "Indiana University", "University of Maryland College Park", "University of Georgia", "National University of Singapore"]
equal_contribution: ["Ruhan Wang", "Yucheng Shi"]
correspondence: "ruhwang@iu.edu, yuchengshi@tencent.com"
project_website: "https://ruhan-wang.github.io/Harness-Handbook/"
arxiv_id: "2607.13285v1"
url: "https://arxiv.org/abs/2607.13285"
doi: "10.48550/arXiv.2607.13285"
publisher: "arXiv (cs.AI preprint)"
date_published: 2026-07-14
date_ingested: 2026-07-22
length: "~29 pages (main text + appendices A–…); read in full (pdftotext extract)"
raw: "../../raw/papers/harness-handbook-making-evolving-agent-harnesses-readablenavigable-and-editable.pdf"
zotero_item_key: JITW7D7E
tags: [agent-harness, agentic-engineering, harness-evolution, behavior-localization, harness-handbook, bgpd, progressive-disclosure, static-analysis, code-representation, coding-agents, codex, terminus-2, tencent, indiana-university, repository-understanding]
relationships:
  - type: supports
    target: 2026-05-11-karten-zhang-continual-harness-online-adaptation
    via: "addresses the prerequisite Karten's Refiner performs implicitly — behavior localization (finding *where* in the harness to edit) before harness-state edits (Δp, ΔG, ΔK, ΔM) can be made. Directly answers Karten's open question 'does the Refiner architecture work on coding tasks?': Harness Handbook evaluates on Codex and Terminus-2 (Terminal-Bench harness), not embodied Pokémon"
  - type: supports
    target: 2026-03-26-pan-natural-language-agent-harnesses
    via: "shares the core finding that the *representation* — not the model — drives the gain. Pan rewrote a native-code harness in structured natural language for the OS-Symphony jump (30.4% → 47.2%); Harness Handbook reorganizes source around behavior (L1–L3 + state-register view) and reports localization/edit-plan improvements at *fewer* planner tokens. Both argue harness readability is an engineering lever, not cosmetics"
  - type: supports
    target: 2026-03-30-lee-meta-harness-end-to-end-optimization
    via: "complementary halves of harness evolution: Meta-Harness auto-*rewrites* the harness (edit generation); Harness Handbook localizes *where* the edit should go (behavior localization), which the paper frames as the prerequisite bottleneck that edit-generation approaches assume already solved"
  - type: supports
    target: 2026-03-05-lou-deepmind-autoharness-code-harness-synthesis
    via: "both treat the agent harness as a first-class code artifact that a model can operate on — AutoHarness *synthesizes* harness code, Harness Handbook builds a behavior-centric *representation* of an existing harness so a coding agent can navigate and edit it; two directions of the same 'harness-as-manipulable-codebase' thesis"
  - type: uses
    target: agent-harness
    via: "the paper's contribution is a behavior-centric representation (Harness Handbook) plus a modification workflow (BGPD) that operate over an existing agent harness codebase, formalizing behavior localization as the prerequisite step of harness evolution"
---

# Wang, Shi et al. — *Harness Handbook: Making Evolving Agent Harnesses Readable, Navigable, and Editable*

A **~29-page arXiv preprint** (cs.AI, **2607.13285v1**, posted **14 July 2026**) by **Ruhan Wang\*** (Indiana University; work done during an internship at Tencent Seattle; ruhwang@iu.edu), **Yucheng Shi†** (Tencent; lead project collaborator; yuchengshi@tencent.com), **Zongxia Li** (University of Maryland, College Park), **Zhongzhi Li** (University of Georgia), **Yue Yu** (Indiana University), **Junyao Yang** (National University of Singapore), **Kishan Panaganti**, **Haitao Mi**, **Dongruo Zhou** (Indiana University), and **Wei Liang Leo** — primarily **Tencent HY LLM Frontier** with academic collaborators. \* = equal contribution; † = lead project collaborator. Project website: [ruhan-wang.github.io/Harness-Handbook](https://ruhan-wang.github.io/Harness-Handbook/).

This is the wiki's first source to make **behavior localization** — finding *all* the code sites that implement a described behavior — the named, central bottleneck of **harness evolution**. The wiki's [[concepts/agent-harness|agent-harness]] page carries a deep literature on how to *build*, *optimise*, and *prune* a harness ([[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]]'s 4-layer build order; the [[2026-05-04-rethinking-agents-harness-is-all-you-need|subtraction principle]]; [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten's]] in-place Refiner edits) but nothing on the prior question every one of those edits assumes answered: *where in a large, tightly-coupled, behaviorally-distributed harness codebase should the edit be made?* Wang & Shi et al. name that gap, argue it is the real bottleneck, and propose a representation and a workflow to close it.

## TL;DR

- **The problem: behavior localization.** Modifying a harness (add a capability, adapt a behavior, refine a workflow) requires first identifying *all* implementation sites for the target behavior. This is hard because production harnesses are **large, tightly coupled, and behaviorally distributed** across files, functions, execution stages, and state transitions — while a modification request describes *what* the system should do, and repositories are organised by *files and modules*. Code search, repo indexing, and long-context all ease inspection but leave the **behavior→code mapping** to be recovered by hand. That recovery is the bottleneck.
- **The artifact: Harness Handbook.** A **behavior-centric representation** synthesized *automatically* from a harness codebase via **static program analysis + LLM-assisted behavioral structuring**. Instead of organising knowledge by files/functions, it organises it by *what the harness does* and links each behavior to the source that implements it. Structure: an **L1–L3 document tree** — L1 System Overview → L2 Component/Stage Overview → L3 source-backed Unit Deep Dive — plus a complementary **state-register view Z** recording state relationships that cross stage boundaries.
- **Two design rules keep it honest.** **Progressive disclosure** (readers descend L1→L3 only when the task needs the detail) and **behavior–implementation alignment** (every active L3 locator must still resolve to the *current* repository; a locator that cannot be revalidated is **frozen** and excluded from localization until refreshed). **The repository remains the authority for implementation details** — the handbook guides the search but never replaces source.
- **The workflow: BGPD.** **Behavior-Guided Progressive Disclosure** localizes a request coarse-to-fine: start at L1/L2 to find directly-relevant execution stages → follow Z to pull in stages coupled through shared state (catching mutually-dependent, structurally-distant stages) → select the most relevant L3 entries and their source locators → expand along the function-call graph (or induced file-call graph) → then **open the current repo, resolve the locators, and keep only sites still relevant to q**, yielding verified evidence *E_q*. A planner turns *E_q* into an edit plan *P* + action declarations Γ (modify/add/remove); a separate executor applies it.
- **Self-maintaining: automatic resynchronization.** Every **non-empty diff** triggers `Resync`: reparse changed source, refresh the program graph, match old/new units (line-number-independent fingerprints in function-as-leaf mode; content hashes + file-set diffs in file-as-leaf mode), refresh only affected entries when the stage skeleton still holds (else rebuild), and **freeze rather than guess** anything unparseable. Model calls in resync are limited to **four semantic steps** (classification, file assignment, within-stage organization, description revision); everything else is deterministic. This is what makes the handbook *evolving* rather than a stale doc.
- **Two construction modes.** Leaf granularity *g* ∈ {function, file}, fixed for the handbook's lifetime. **Function-as-leaf** starts from a trustworthy seed skeleton (used when execution stages are reliably known and function-level entries fit budget); **file-as-leaf** *infers* the skeleton (used at repository scale or when function-level would blow the budget). Construction runs three phases: **(I) Static Fact Extraction** (deterministic, no LLM — functions, call edges, state accesses, external boundaries; unresolved calls logged, never guessed), **(II) Behavioral Organization** (LLM proposer/reviewer maps source units to execution stages), **(III) Hierarchical Synthesis** (builds the L1–L3 tree + state-register view, each L3 entry statically linked and validated against the repo).
- **Evaluation: two open-source harnesses.** **Terminus-2** (function-as-leaf; reliable seed skeleton) and **Codex** (file-as-leaf; inferred at repo scale), **30 behavior-driven modification requests each**, grouped by type — **Query (Q)**, **Cross-file (CF)**, **Search-Hostile (SH)** — and labeled Easy/Medium/Hard by localization difficulty. A read-only planner (NexAU + DeepSeek-V4-Pro) produces edit plans; **three independent judges** (GPT-5.5, Opus 4.8, DeepSeek-V4-Pro) score plan quality on **Localization (0.5 weight) + Scope Control (0.25) + Reasoning (0.25)**.
- **Headline results — better plans at lower token cost.** Handbook-Assisted overall win rate **38.3% vs 28.3% on Codex** and **45.6% vs 26.7% on Terminus-2**, consistent across all three judges (gap 10.0 pts on every Codex judge; 13.3–26.7 pts on Terminus-2), **without increasing planner token use**. Gains are largest for **scattered implementation sites, rarely-executed paths, and cross-module interactions** (i.e. the Cross-file and Search-Hostile request types, and Hard difficulty).
- **Localization accuracy vs stronger-model reference plans (Table 1).** Predicted edit sites compared against independent reference plans from **Opus 4.8** and **GPT-5.5** at file and symbol granularity (Recall/Precision/F1/Wrong; *Wrong* = zero overlap, lower is better). Representative Codex-vs-Opus-4.8 gains: file **F1 46.6 → 61.8 (+15.2)**, symbol **F1 38.3 → 57.1 (+18.8)**, symbol **Wrong 44.4 → 18.5 (−25.9)**. Terminus-2-vs-GPT-5.5: file **F1 76.5 → 89.3 (+12.8)**, file **Wrong 20.0 → 6.7 (−13.3)**. **A weaker planner with the handbook produces file- and symbol-level predictions that align more closely with reference plans from substantially stronger models** (RQ2 — answered yes).
- **The thesis.** *"Evolving complex agentic systems depends not only on generating edits, but also on determining where those edits should be made."* Localization is a first-class, separately-optimizable step — not a free byproduct of a capable planner.

## What was actually ingested

Full paper via `pdftotext` extraction of the 29-page PDF (main text §§1–4 + figures/tables + appendices). `pdftotext -layout` flattens the figure-heavy L1–L3 diagram (Figure 1) and the construction-pipeline diagram (Figure 2) into spaced text — the *structure* of the representation is recovered from the prose and Algorithm 1/2 pseudocode, not the rendered figures. Table 1 (reference-plan localization metrics) transcribed from the extract. Appendix A (full organization procedures + validation checks for both leaf modes) skimmed rather than fully verified against the PDF layout.

## Why this matters to the wiki — behavior localization as the missing prerequisite

The [[concepts/agent-harness|agent-harness]] page has, until now, treated harness evolution as an **edit-generation** problem: [[2026-03-30-lee-meta-harness-end-to-end-optimization|Meta-Harness]] auto-rewrites the whole harness from failed traces; [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Continual Harness]]'s Refiner emits per-component CRUD edits from a trajectory window; the [[2026-05-04-rethinking-agents-harness-is-all-you-need|subtraction principle]] prescribes *removing* structure the model outgrew. Every one of these assumes the editor already knows **which code implements the behavior in question**. Harness Handbook is the first wiki source to isolate that assumption and attack it directly:

- It **names the bottleneck** (behavior localization) and gives it metrics (Recall/Precision/F1/Wrong at file and symbol granularity against stronger-model reference plans).
- It supplies a **representation** whose gain — like [[2026-03-26-pan-natural-language-agent-harnesses|Pan et al.'s natural-language harness rewrite]] — comes from *reorganising the same information around behavior*, not from a better model. This is a second, independent data point for the wiki's *"representation is a lever"* thread.
- Its **evaluation harnesses are coding harnesses** (Codex, Terminus-2), directly answering [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten's]] explicit open question — *"whether the same Refiner architecture works on SWE-bench or Terminal-Bench is the obvious next experiment"* — on the localization half of the loop.

### Positioning against neighbouring harness-evolution sources

| Source | What it optimises | Relation to Harness Handbook |
|---|---|---|
| [[2026-05-11-karten-zhang-continual-harness-online-adaptation\|Karten — Continual Harness]] | In-place harness-state edits (Δp, ΔG, ΔK, ΔM) during a live episode | Handbook supplies the *localization* the Refiner does implicitly; Handbook targets coding harnesses, Karten targets embodied Pokémon |
| [[2026-03-30-lee-meta-harness-end-to-end-optimization\|Lee/Khattab — Meta-Harness]] | End-to-end harness rewrite from failed traces | Complementary: *where to edit* (Handbook) vs *what edit to generate* (Meta-Harness) |
| [[2026-03-26-pan-natural-language-agent-harnesses\|Pan — NL Agent Harnesses]] | Harness *representation* (native code → structured natural language) | Same "representation drives the gain" thesis, applied to navigation/localization rather than runtime execution |
| [[2026-03-05-lou-deepmind-autoharness-code-harness-synthesis\|Lou — AutoHarness]] | Synthesising harness code from scratch | Two directions of "harness-as-manipulable-codebase": synthesis (Lou) vs behavior-centric representation of an existing one (Handbook) |

## Named entities (this ingest)

All authors are **first mention → dangling** (single-source; no entity pages created per the [second-source promotion rule](../../CLAUDE.md#author-entity-promotion)):

- **Dangling** (single-source mention, deferred): [[Ruhan Wang]] (Indiana University / Tencent Seattle internship; co-equal, corresponding), [[Yucheng Shi]] (Tencent; lead project collaborator, corresponding), [[Zongxia Li]] (University of Maryland), [[Zhongzhi Li]] (University of Georgia), [[Yue Yu]] (Indiana University), [[Junyao Yang]] (National University of Singapore), [[Kishan Panaganti]], [[Haitao Mi]], [[Dongruo Zhou]] (Indiana University), Wei Liang Leo.
- **Affiliations** (dangling, not promoted): **Tencent HY LLM Frontier** — first wiki source from Tencent's LLM lab; **Indiana University** — first mention; University of Maryland College Park, University of Georgia, National University of Singapore.

**Reference-list systems the wiki already tracks**: [[2026-02-11-lopopolo-codex-harness-engineering|Codex]] and Terminus-2 appear as the two evaluation harnesses; the paper cites "Code as Agent Harness" (ref [15]) as the harness-as-executable-software-layer formalisation, plus **AutoGen** and **OpenHands** as modular runtime frameworks — consistent with the [[concepts/agent-harness|agent-harness]] page's framework/runtime layering.

## Source-quality notes

- **Genre**: arXiv preprint (cs.AI), pre-publication, not peer-reviewed. Named institutions, corresponding-author emails, and a project website. Empirical-systems paper aimed at peer review.
- **Empirical design**: two real open-source harnesses × 30 requests each × three request types × three difficulty levels, three independent LLM judges, reference plans from two frontier models. Reasonable rigour for a systems paper; **N is modest** (60 requests total) and the planner/judges are all LLMs, so the *"weaker planner matches stronger models"* claim (RQ2) rests on LLM-judged plan quality, not on executed-and-tested edits landing green.
- **Conflict-of-interest note**: primarily a **Tencent** paper evaluating on Tencent-external open-source harnesses (Codex/OpenAI, Terminus-2) — no obvious vendor-benchmark bias, but the method (Harness Handbook) is the authors' own artifact, judged by a rubric they designed (Localization weighted 0.5).
- **Sources do not carry `confidence`** per [§Lifecycle](../../CLAUDE.md#lifecycle); this is evidence, and its weight is captured by what cites it on [[concepts/agent-harness|agent-harness]].

## Open questions

- **Does localization gain survive to executed edits?** Plan quality and localization F1 are LLM-judged against reference plans; the paper does not report whether Handbook-Assisted edit plans, once *executed*, pass the harness's own tests at a higher rate than Baseline. The obvious next experiment is end-to-end (localize → plan → execute → test) with a pass/fail outcome. **Tracked in [[threads/harness-evolution-validation-frontier|the harness-evolution-validation-frontier thread]]**, which consolidates this executed-edits gap with the sibling validation questions across [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten]], [[2026-03-26-pan-natural-language-agent-harnesses|Pan]], and Meta-Harness.
- **Resync cost at production scale.** The four-semantic-step resync is bounded per diff, but the paper's harnesses (Codex, Terminus-2) are open-source research harnesses. Whether incremental resync stays cheap on a **1M-LOC production harness** (cf. [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo's OpenAI Codex]] scale) is untested.
- **Interaction with self-editing harnesses.** [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Continual Harness]]'s Refiner edits the harness *during* an episode. If the harness is mutating continuously, does the Handbook's resync keep up, or does the behavior→code mapping thrash? A Handbook-over-a-Continual-Harness experiment would test whether localization and in-place evolution compose.
- **Primary-source status of the cited harness-evolution literature.** The paper cites Meta-Harness-style and NL-harness work the wiki tracks second-hand ([[2026-05-04-rethinking-agents-harness-is-all-you-need|via the Prompt Engineering synthesis]]); worth cross-checking its reference IDs against the wiki's open primary-source ingest targets ([[2026-03-26-pan-natural-language-agent-harnesses|Pan]], [[2026-03-30-lee-meta-harness-end-to-end-optimization|Lee/Khattab]]).
