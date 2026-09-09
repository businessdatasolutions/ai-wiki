# Query trace — the concepts students must learn each AIBS week

## §1 — The question

> Which ai-wiki concepts are the most important things students must learn in each teaching
> week of the AIBS module, so that they can be named in Part 8 of the integrated LRD?

Asked in order to add a **week → concepts** mapping to `site/integrated-lrd.html` Part 8 (the
weekly programme: six teaching weeks over five themes, plus a week-7 consolidation).

**Facets.** One per teaching theme, taken verbatim from the LRD's Part 8 table rather than invented:

1. **W1** — applied research and the problem analysis; the intern analogy as shared vocabulary.
2. **W2** — the geopolitical field and the vendors' business models.
3. **W3** — can the SME trust AI? (Trustworthy AI: its data, the output, its people).
4. **W4** — what regional SMEs know, and what they need to know.
5. **W5** — where the first opportunities are; the five kinds of use.
6. **W6** — successful use cases at SMEs.

Week 7 is consolidation and carries no new theme, so it takes no concepts.

Language: English (question language) — matches the LRD.

## §2 — Paths explored

Retrieval ran six times through the single entry point, one query per facet:

```sh
node scripts/wiki-retrieve.mjs --json -n 12 "<facet query>"
```

| Facet | Query | candidates | qmd hits | graph |
|---|---|---|---|---|
| W1 | applied research methodology problem analysis AI intern analogy expert generalist | 56 | 10 | available |
| W2 | AI geopolitics Draghi report Europe innovation gap open versus closed weights vendor business models | 58 | 11 | available |
| W3 | Trustworthy AI EU requirements SME data protection sovereignty local models responsible AI | 52 | 10 | available |
| W4 | what knowledge do SMEs need before adopting AI maturity adoption barriers literacy | 63 | 10 | available |
| W5 | where AI creates value in business processes automation versus augmentation productivity trap | 58 | 11 | available |
| W6 | successful AI use cases at small and medium enterprises manufacturing industrial adoption | 54 | 11 | available |

`graph_warning` was `null` on all six runs — both streams (qmd relevance and typed-edge
traversal) contributed; no degraded qmd-only run.

**Gap expansion (Step 5, one round).** `wiki/index.md` proved too large to scan usefully, so the
expansion instead enumerated `wiki/concepts/` (49 pages), `wiki/syntheses/` (5) and
`wiki/threads/` (7) directly, to catch pages retrieval missed by name. This promoted two W6
pages (`industrial-ai-agents`, `industry-4-0`) and confirmed the W2 gap recorded in §4.

## §3 — How the ignore decision was made

The ledger is source-dominated: across the six runs, roughly 300 candidates, of which the large
majority are `type: source` — individual ingested talks, reports and papers. The question asks
what a student must **learn**, not what the wiki has **read**, so the triage rule was:

- **Concept, synthesis and thread pages are eligible.** They are the wiki's units of transferable
  understanding — the thing a student can be examined on.
- **Sources are IGNORE by default** (reason-class `wrong-granularity`), however high their
  `fused_score`. A source belongs in a reading list, not in a list of concepts. The LRD's Part 8
  "Grounding" column already carries reading-level material.
- **Entities are IGNORE** (reason-class `wrong-granularity`): an organisation or person is not a
  concept a student learns.
- **Off-facet concepts are IGNORE** (`off-facet`) — mostly the agent-engineering cluster
  (`agent-harness`, `agentic-engineering`, `agent-development-lifecycle`, `reward-hacking`,
  `graph-engineering`), which is AEL's technical spine, not AIBS's research themes. These would be
  the right USE set for a question about the AEL harness ladder; they are the wrong one here.
- **Low `effective_confidence` is a caution, not a veto.** `analogical-reasoning` (0.359) and
  `industrial-ai-agents` (0.75, self-declared stub) are USE because they are the only pages
  covering their facet — flagged as thin in §7 rather than dropped.
- **Graph-only candidates need a higher bar**, per the skill. Two cleared it
  (`automation-vs-augmentation`, `dynamic-capabilities`) because they are the named targets of
  `uses` edges from `enterprise-ai-adoption`, the strongest hit on two separate facets.

## §4 — What was ignored, and why

| Reason-class | Count (approx.) | Examples |
|---|---|---|
| `wrong-granularity` — source page, not a learnable concept | ~230 | `2026-04-30-ai-index-report-2026`, `2026-05-02-dutt-chatterji-ai-experimentation-to-transformation`, `2026-04-28-dellacqua-jagged-technological-frontier` |
| `wrong-granularity` — entity page | ~12 | `entities/Martin Fowler`, `entities/McKinsey & Company`, `entities/Microsoft`, `entities/GitHub` |
| `off-facet` — AEL technical spine, not an AIBS theme | 9 | `agent-harness` (0.969), `agentic-engineering` (0.949), `agent-development-lifecycle`, `reward-hacking`, `ai-generated-code-quality`, `ai-coding-productivity-evidence` |
| `off-facet` — adjacent but not on any theme | 8 | `strategy`, `infinite-game`, `strategic-centering`, `theory-based-view` (0.268), `founder-led-sales`, `osint`, `knowledge-graphs`, `document-intelligence` |
| `duplicate` — alias page of a USE page | 1 | `entities/Martin-Fowler` (duplicate of `entities/Martin Fowler`) |
| `superseded-by-USE` — narrower than a page already in USE | 2 | `generative-ai` (0.313), `ai-benchmarks` — subsumed by `foundation-models` for this purpose |

The AEL exclusion is the load-bearing judgement in this trace. `agent-harness` scored **0.969
effective confidence**, the single highest of any candidate, and appeared on three of six facets.
It is nonetheless IGNORE: Part 8's AEL column is a *harness ladder* fixed by ADR-0010, not a list
of concepts to be researched, and this mapping is for the AIBS themes only.

**A genuine coverage gap, not an ignore.** Facet W2 has **no concept page for AI geopolitics, the
Draghi report, European competitiveness or the EU AI Act.** The 49-page concept inventory was
checked by name: nothing under geo-, EU-, regul-, policy-, sovereign- or europe-. The W2 run
returned only sources on the theme. This is exactly the dependency ADR-0004 and NFR-10 already
name — two W2 pages to be written before the module runs — so retrieval **confirms** the LRD's
existing risk rather than contradicting it. `open-source-ai` covers the second half of W2 (vendor
business models, own-vs-rent, sovereignty) well; the geopolitical half is uncovered.

## §5 — What was used

22 pages. All verified present on disk and live at the published wiki.

| # | Page | Type | eff. conf. | Facet |
|---|---|---|---|---|
| W1 | `concepts/durable-skills` | concept | 0.899 | 1 |
| W2 | `concepts/expert-generalist` | concept | 0.686 | 1 |
| W3 | `concepts/jagged-frontier` | concept | 0.889 | 1, 5 |
| W4 | `concepts/analogical-reasoning` | concept | 0.359 | 1 |
| W5 | `concepts/open-source-ai` | concept | 0.890 | 2, 3 |
| W6 | `concepts/foundation-models` | concept | 0.870 | 2 |
| W7 | `concepts/enterprise-ai-adoption` | concept | 0.899 | 2, 4, 6 |
| W8 | `concepts/responsible-ai` | concept | 0.950 | 3 |
| W9 | `concepts/small-language-models` | concept | 0.742 | 3 |
| W10 | `concepts/agent-oversight-and-delegation` | concept | 0.765 | 3 |
| W11 | `concepts/ai-knowledge-hiding` | concept | 0.700 | 3, 4 |
| W12 | `concepts/dynamic-capabilities` | concept | 0.795 | 4 |
| W13 | `syntheses/organizational-frameworks-for-ai-adoption` | synthesis | 0.505 | 4 |
| W14 | `threads/ai-maturity-measurement-comparison` | thread | — (open) | 4 |
| W15 | `concepts/automation-vs-augmentation` | concept | 0.889 | 5 |
| W16 | `concepts/micro-productivity-trap` | concept | 0.899 | 5, 6 |
| W17 | `concepts/ai-employment-effects` | concept | 0.899 | 5 |
| W18 | `concepts/ai-deskilling` | concept | 0.651 | 5 |
| W19 | `concepts/ai-washing` | concept | 0.770 | 5 |
| W20 | `concepts/lean-4-0` | concept | 0.670 | 6 |
| W21 | `concepts/industry-4-0` | concept | 0.456 | 6 |
| W22 | `concepts/industrial-ai-agents` | concept | 0.750 | 6 |

`industrial-ai-agents` and `industry-4-0` were promoted `gap-expansion` (Step 5); neither appeared
in the W6 qmd stream.

## §6 — Where the used facts live

| Anchor | Page | Section relied on |
|---|---|---|
| W1 | durable-skills | "Working definition" — the three criteria (open-ended, socially situated, slow-changing) |
| W2 | expert-generalist | "The six characteristics" table |
| W3 | jagged-frontier | "Working definition" + "Empirical anchor" — inside/outside frontier, the 19pp reversal |
| W4 | analogical-reasoning | "Working definition" — rhetorical vs. generative roles; predictive-analogy structure |
| W5 | open-source-ai | "The own-vs-rent thesis"; "Open vs. closed as a safety question" |
| W6 | foundation-models | Front matter + opening definition |
| W7 | enterprise-ai-adoption | Opening — adoption breadth vs. modest realised impact; `uses`/`caused` relationships |
| W8 | responsible-ai | "Working definition"; "Risk acknowledgment > mitigation"; "Incidents are rising" |
| W9 | small-language-models | "The definition is device-indexed, so it moves" — WD1 |
| W10 | agent-oversight-and-delegation | "The failure mode that is not about accuracy" — delegation regret |
| W11 | ai-knowledge-hiding | "Why it is newly consequential"; "The empirical claim: trust, not governance" |
| W12 | dynamic-capabilities | "Working definition"; "The three-cluster framework" — sense/seize/transform |
| W13 | organizational-frameworks-for-ai-adoption | Front matter — six frameworks as decision layers |
| W14 | ai-maturity-measurement-comparison | "The question"; "What we know so far" — 78% use vs. 1% mature |
| W15 | automation-vs-augmentation | Opening — the three layers (strategy, task design, labour markets) |
| W16 | micro-productivity-trap | "Working definition" — the two lock-ins |
| W17 | ai-employment-effects | "Working definition" — displacement / reduced hiring / compositional shift |
| W18 | ai-deskilling | Opening — task-composition shift, distinct from displacement |
| W19 | ai-washing | "The mechanism: a stock-market valuation premium" |
| W20 | lean-4-0 | "Working definition"; the 23 × 23 mapping |
| W21 | industry-4-0 | "Working definition" — the four revolutions |
| W22 | industrial-ai-agents | "Working definition" — the three distinguishing properties |

## §7 — Answer-element → wiki-element map

The answer is the week-by-week concept list added to LRD Part 8. Each row's anchors:

| LRD week | Concepts named | Anchors |
|---|---|---|
| 1 | durable skills; expert generalist; jagged frontier; analogical reasoning | W1, W2, W3, W4 |
| 2 | open-source AI (own vs. rent); foundation models; enterprise AI adoption | W5, W6, W7 |
| 3 | responsible AI; small language models; agent oversight and delegation; AI knowledge hiding | W8, W9, W10, W11 |
| 4 | enterprise AI adoption; dynamic capabilities; the adoption-frameworks synthesis; the AI-maturity thread | W7, W12, W13, W14 |
| 5 | automation vs. augmentation; the micro-productivity trap; AI employment effects; AI deskilling; AI washing | W15, W16, W17, W18, W19 |
| 6 | Lean 4.0; Industry 4.0; industrial AI agents; the micro-productivity trap (returning) | W20, W21, W22, W16 |
| 7 | — no new concepts; consolidation | — |

**Thin ground, stated plainly.** Three of these are weaker than the rest and the LRD says so:
`analogical-reasoning` (0.359 effective confidence, 2 sources), `industry-4-0` (0.456, 4 sources)
and `industrial-ai-agents` (0.75 but self-declared a stub on a single source). The
`organizational-frameworks-for-ai-adoption` synthesis is closed and last refreshed 15 July 2026
(0.505). **Week 2's geopolitical half has no page at all** — see §4.

## §8 — Final answer

Six of the seven weeks have a defensible concept spine in the wiki, and one week does not.

- **Week 1** rests on `durable-skills` (the three criteria that define a skill AI does not
  substitute) and `expert-generalist` (its six characteristics), which together give the intern
  analogy a vocabulary; `jagged-frontier` supplies the reason a problem analysis must be
  task-by-task; `analogical-reasoning` is the discipline the intern analogy itself needs, and is
  the wiki's thinnest USE page.
- **Week 2** rests on `open-source-ai` — the own-vs-rent thesis, open-vs-closed as a *safety*
  rather than a licensing question, and sovereignty — with `foundation-models` for what is being
  sold and `enterprise-ai-adoption` for who buys it. **The geopolitical half of the theme has no
  concept page**, which is the ADR-0004 dependency already on the LRD's risk list.
- **Week 3** rests on `responsible-ai` (the governance overlay; incidents rising 233 → 362),
  `small-language-models` (the device-indexed definition, which is what makes "when is local
  better" answerable), `agent-oversight-and-delegation` (delegation regret — a correct outcome
  does not repair an unauthorised action) and `ai-knowledge-hiding` (trust inside the firm:
  57% admit hiding their AI use; a policy alone predicts nothing).
- **Week 4** rests on `enterprise-ai-adoption` and the `ai-maturity-measurement-comparison` thread,
  whose 78%-use-versus-1%-mature spread is the sharpest available answer to "is knowledge the
  bottleneck at all"; `dynamic-capabilities` gives sense/seize/transform as the capability frame,
  and the adoption-frameworks synthesis maps six frameworks onto decision layers.
- **Week 5** is the wiki's strongest week: `automation-vs-augmentation` is precisely the analytical
  lens the theme's five kinds of use need, `micro-productivity-trap` names why task gains do not
  become firm value, and `ai-employment-effects`, `ai-deskilling` and `ai-washing` between them
  let a team answer the jobs question with evidence rather than with the public debate.
- **Week 6** rests on `lean-4-0` and `industry-4-0` — the right frame for regional manufacturing
  SMEs, and the wiki's only manufacturing-specific pages — plus `industrial-ai-agents` (a stub) and
  `micro-productivity-trap` returning as the test of whether a use case actually worked.
- **Week 7** takes none: it is consolidation, not a theme.

The result is added to LRD Part 8 as a **week → concepts** table linking each page at its published
wiki URL, with a note recording the week-2 gap and the three thin pages.


---

# Addendum — the AEL half (same day, second pass)

The first pass answered an AIBS-shaped question and ignored the agent-engineering cluster as
`off-facet`; §4 records `agent-harness` at 0.969 as the example. That was right for the question
asked and wrong for the document: it left LRD Part 8 saying what the AIBS research rests on and
what the AEL ladder builds, but not what the ladder *teaches*. This addendum closes that.

## A2.1 — Retrieval

Three further runs through the same entry point:

| Query | concept/synthesis candidates |
|---|---|
| agentic harness context engineering rules skills memory hooks vibe coding | 23 |
| knowledge architecture RAG knowledge graph skills for LLM agents | 8 |
| evaluation LLM as judge eval harness agent testing reward hacking | 4 |

This is the wiki's densest and best-maintained region: `agent-harness` 0.98, `agentic-engineering`
0.949, `ai-agents` 0.94, `llm-wiki` 0.89, `react-reasoning-acting` 0.89, `vibe-coding` 0.889,
`agent-development-lifecycle` 0.842, `multi-agent-failure-modes` 0.841.

## A2.2 — The framing constraint (this is the substantive judgement)

ADR-0010 makes each week's harness element the answer to a failure the team has **already met**.
A concept named in advance hands a team the answer before it has the problem, and the ratchet stops
ratcheting. The AEL column is therefore specified as **debrief reading** — consulted once the
element is in place — not as pre-reading. Week 3 is the stated exception: there the decision record
is the deliverable, and `knowledge-architectures-for-llm-agents` is that very decision
(RAG / LLM Wiki / Fat Skills) already worked through as a comparison.

This constraint is a property of the *consumer*, not of the wiki, and no retrieval score could have
surfaced it. It was put to the module owner and confirmed before the column was written.

## A2.3 — USE set (AEL), by week

| Wk | AEL element | Pages | eff. conf. |
|---|---|---|---|
| 1 | Vibe-coded spike + failure log | `concepts/vibe-coding`, `concepts/agentic-engineering` | 0.889, 0.949 |
| 2 | Context layer | `concepts/agent-harness`, `concepts/react-reasoning-acting` | 0.98, 0.89 |
| 3 | Decision log — knowledge architecture | `syntheses/knowledge-architectures-for-llm-agents`, `syntheses/is-rag-dead`, `concepts/llm-wiki`, `concepts/knowledge-graphs` | 0.90, 0.90, 0.89, 0.90 |
| 4 | Contracts layer — eval config | `concepts/agent-development-lifecycle`, `concepts/reward-hacking` | 0.842, 0.85 |
| 5 | Constraints layer — hooks | `concepts/agent-oversight-and-delegation`, `concepts/multi-agent-failure-modes` | 0.765, 0.841 |
| 6 | Compounding layer — skills and memory | `syntheses/harness-thinning-what-persists`, `concepts/agent-fleet-management` | 0.82, 0.75 |
| 7 | Capstone + ratchet retrospective | `concepts/agentic-engineering` (returning) | 0.949 |

`agent-oversight-and-delegation` is deliberately reused from AIBS week 3, read from the builder's
side: the same finding — a correct outcome does not repair an unauthorised action — is why a hook
fires *before* a tool call. `agent-fleet-management` and `multi-agent-failure-modes` carry a
recorded `contradicts` edge between them; that is kept rather than resolved, because a team that
must defend a choice benefits from an open disagreement.

## A2.4 — Ignored in this pass

| Reason-class | Pages |
|---|---|
| `off-facet` — AIBS-side, already placed in the first pass | `enterprise-ai-adoption`, `micro-productivity-trap`, `jagged-frontier`, `automation-vs-augmentation`, `open-source-ai` |
| `thin` — too low to carry a week | `software-3.0` (0.494) |
| `off-facet` — no AEL week deploys it | `industrial-ai-agents`, `attack-surface-management`, `agentic-pull-requests`, `ai-generated-code-quality`, `ai-coding-productivity-evidence`, `osint`, `document-intelligence` |

`ai-agents` (0.94) is a near-miss IGNORE: high confidence and on-facet, but it is the parent of
`agent-harness` and `agent-development-lifecycle` rather than a lesson any single week teaches.

## A2.5 — Second gap

**Loop engineering has no concept page.** It is discussed inside `agent-harness`,
`agentic-engineering`, `graph-engineering` and `multi-agent-failure-modes`, and two Google Cloud
sources state the nesting cleanly — harness ⊃ loop ⊃ graph-node — but a reader looking for the
layer between harness and orchestration will not find it under its own name. Same shape as the
week-2 geopolitics gap, lower stakes: unlike the week-2 pages this is not a hard dependency, since
no AEL week loses its element for want of it. It is a good candidate for the next wiki pass.
