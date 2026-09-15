# Traceable wiki answer — source cells for week-03 candidate claims 1–3

**Run date:** 2026-09-15 · **Skill:** `traceable-wiki-answer` (via `/wqa`) · **Deliverable target:**
`~/Documents/HAN/M3DM/ai-in-business/work/drafts/week-03-candidate-claims.md`

## §1 — The question

> For claims 1, 2 and 3 in `week-03-candidate-claims.md`, find sources that clearly **agree (A)** or
> **disagree (NA)**, each labelled **strong (S)** or **weak (W)** per the draft's own definition.
> Target 16 per claim: 4 AS, 4 NAS, 4 AW, 4 NAW. Unambiguous stances only. Stop at 16 per claim or
> when retrieval yields no further qualifying sources.

**Facets.** (a) stance direction per claim, unambiguous only; (b) S/W coding; (c) cell-fill
feasibility — can each 2×2 actually be completed from this corpus.

**Coding decision, recorded because it is contestable.** The invocation glossed strong as
"scientific sources / experts". The draft's own §*How they were judged* defines it differently — the
**denominator rule** (randomises / covers a population / reports the losers), and explicitly calls
that *"a better cut than peer-reviewed against vendor blog"*. **The denominator rule was applied.**
The two codings disagree on four rows, all marked ⚠ in the deliverable, and a `genre` column is
carried throughout so the alternative coding can be recovered without re-running this.

## §2 — Paths explored

Three retrievals via `scripts/wiki-retrieve.mjs --json -n 14` (qmd ∪ graph, RRF-fused,
decay-reranked). `graph_warning: none` on all three — both streams live.

| Run | Query focus | Candidates | Source-type candidates |
|---|---|---:|---:|
| C1 | self-reported vs measured AI productivity, perception gap | 65 | 52 |
| C2 | own small models vs rent frontier, own-vs-rent, SLMs, benchmarks | 84 | 56 |
| C3 | augmentation vs automation, job redesign, headcount | 89 | 64 |

**Total 238 candidates triaged.** Follow-on reads: 4 concept pages (`ai-coding-productivity-evidence`,
`small-language-models`, `automation-vs-augmentation` §§5–10/20–26/424/484, `open-source-ai`) and
~24 source pages probed for `kind`, `publisher` and headline findings.

## §3 — How the ignore decision was made

Per `references/ignore-policy.md`, plus two task-specific gates:

1. **Off-facet** — candidate does not speak to any of the three claims (most graph-only neighbours:
   harness mechanics, entity pages, unrelated concepts).
2. **Stance-ambiguous** — the brief demanded unambiguous direction, so a source arguing both sides
   was ignored *even at a high fused score* unless one headline was cleanly separable. This gate did
   most of the work and is the reason several high-ranked pages are IGNOREd.
3. **Concept-page-as-appraisal, not as source** — concept pages were read to locate and adjudicate
   sources but are **not** cited as cells; the deliverable needs individual sources.

**Deviation from the skill's 4–8 page USE guidance, declared.** This run's deliverable *is* a source
enumeration, so the USE set is necessarily large (4 concept + 37 source pages). The guideline targets
answer-synthesis runs; keeping to it here would have made the task unanswerable.

## §4 — What was ignored, and why

| Reason class | Count (approx.) | Representative candidates |
|---|---:|---|
| Off-facet (graph-only neighbour) | ~150 | `agent-harness`, `agentic-engineering`, `react-reasoning-acting`, entity pages, `llm-wiki` |
| Stance-ambiguous | 11 | `2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services` (the wiki itself calls it *"a sequencing decision, not a stance"*); `2026-05-28-giles-wp-intelligence-...` (advises workflow-review-first **and** entry-level redesign — reads A, was retrieved as NA); `2026-08-25-sokolenko-pycon-de-...` (advocates SLMs **and** concedes *"top of the board is still proprietary"*) |
| Duplicate evidence of a cell already filled | 6 | `2025-07-30-veracode-...`, `2026-06-11-abujadallah-...`, `2026-02-12-gloaguen-...` — held as named bench substitutes rather than dropped |
| Decayed / superseded framing | 2 | `2026-04-28-anthropic-economic-index-q4-2025` (superseded by the 5th report for the current split) |
| Topic-adjacent but not claim-bearing | ~14 | `2026-03-25-russell-bradley-mgi-...`, `2026-05-06-mit-ocw-...`, `2026-05-14-price-dfi-...` |

## §5 — What was used

**Appraisal layer (concept pages, read not cited):** `ai-coding-productivity-evidence` (conf 0.85,
8 sources, revised 2026-09-15) · `small-language-models` (0.75, 5) · `automation-vs-augmentation`
(0.95, 11,838 words) · `open-source-ai` (0.9, 11).

**Evidence layer (37 source pages cited as cells).** All 37 slugs were verified to exist on disk
before delivery. Claim 1: 16 · Claim 2: 12 (+2 contestable) · Claim 3: 13 (+1 contestable).

## §6 — Where the used facts live

| Anchor | Page | Section relied on |
|---|---|---|
| W1 | `concepts/ai-coding-productivity-evidence` | *The two randomised results*; *The perception gap runs both ways (revised 2026-09-15)*; *The population signal* |
| W2 | `concepts/automation-vs-augmentation` | §5 productivity under augmentation; §6 longitudinal split; §9 Buy-Outcomes; §14 Krakowski; *strongest automation-side argument*; *Which half AI cannot copy* |
| W3 | `concepts/small-language-models` | *What the evidence actually shows*; *The counter-arguments worth keeping*; *Debates and supersession* |
| W4 | `concepts/open-source-ai` | *own-vs-rent thesis*; *two limits* (throughput, harness gap) |
| W5 | `sources/2025-07-10-becker-metr-...` | forecast/estimate/measured table |
| W6 | `sources/2026-02-27-cui-demirer-...` | headline estimate + SE |
| W7 | `sources/2025-09-23-dora-2025-...` | throughput/stability table; adoption + trust figures |
| W8 | `sources/2026-06-12-dellacqua-cybernetic-teammate-...` | *The four results*; *The perception gap, inverted* |
| W9 | `sources/2026-06-10-anicich-brouwers-...` | TL;DR — KPMG 48,000 / own 604-respondent survey |
| W10 | `sources/2026-04-28-brynjolfsson-li-raymond-...` | sample + design + outcomes |
| W11 | `sources/2025-10-05-patwardhan-et-al-openai-gdpval` | what it measures; headline; *human oversight beats either alone* |
| W12 | `sources/2025-07-13-patil-berkeley-function-calling-leaderboard` | multi-turn / τ-bench splits |
| W13 | `sources/2026-03-11-allen-mcdonald-...` | *Open-source models plateau lower* |
| W14 | `sources/2025-06-09-krakowski-...` | D1/D2/D3 arms; result + mediation |
| W15 | `sources/2026-05-07-anthropic-economic-index-5-learning-curves` | Claude.ai augmentation/automation deltas |
| W16 | `sources/2026-06-12-aws-leaders-guide-...` | *the pricing scissors* |
| W17 | `sources/2026-09-01-cfa-institute-...` | open-vs-proprietary; throughput limit; harness gap |
| W18–W37 | remaining cited sources | as tabulated in the deliverable |

## §7 — Answer-element → wiki-element map

| Deliverable element | Rests on |
|---|---|
| Claim 1 fills 16/16 | W5–W11, W15 + the four AW/NAW rows |
| *"perception gap runs both ways"* reframing | W1 (revised section) + W8 |
| Claim 2 AS short at 3 | W3, W12 + absence of a fourth denominator-bearing pro-small source |
| Claim 2's same-instrument problem (BFCL both ways) | W12 + W3 *Debates* |
| Claim 2 NAW short at 3 | W16, W17 + the observed own-side/rent-side asymmetry |
| Claim 3 NAS structurally unfillable | W2 — the explicit *"we do not have equivalent rigorous studies of pure-automation productivity gains"* passage |
| Recommendation to drop claim 3 | W2 (measurement asymmetry) — a stronger ground than the draft's CL-9 worry |

## §2b — Second retrieval pass (added after stop-condition review)

The first pass ran three broad queries (238 candidates) and **stopped at the shortfalls, reporting
them as substantive. That was premature.** Five further queries aimed at the specific empty cells
(~200 more candidates) found seven qualifying sources the broad queries missed:

| Source | Cell it filled |
|---|---|
| Spracklen et al., USENIX Security '25 | claim 2 NAS — commercial ≥5.2% vs open-source **21.7%** package hallucination, 16 models / 2.23M samples |
| Dell'Acqua et al., *jagged frontier* (Organization Science) | claim 3 NAS — RCT, 758 BCG consultants, **−19 pp** correctness outside the frontier |
| Autor & Thompson, NBER | claim 3 NAS — removing *inexpert* tasks predicts **wage gains**; which steps you remove decides the outcome |
| RaboResearch (Rabobank) | claim 3 NAS — automation potential **86% IT / 64% business services / ~44% economy-wide** |
| METR, re-read against claim 3 | claim 3 NAS — the claim's own prescription measured **+19% slower** |
| Allen / AWS London Exec Forum | claim 2 NAW — **~80% of his customers COMPOSE on frontier APIs**; *"they don't want to train those models"* |
| OpenJarvis via YC Paper Club | claim 2 AS ⚠ — local 6–12 months behind; optimise once in the cloud, then **~800× lower** inference cost |

**Removed on the second pass:** BFCL from claim 2 NAS (same paper as AS#1 — using one source on both
sides is exactly what CL-2 forbids); GDPval from claim 2 NAS (argument from silence — it never tested
a small or open model); Brynjolfsson *Canaries* from claim 3 NAS (evidence automation *happens*, not
that automating first is better).

**Stopped because** repeated queries began returning the same pool. **Lesson:** broad semantic
retrieval under-serves cell-filling — the queries that worked named the *shape of evidence wanted*
("RCT where AI assistance made workers worse"), not the topic.

## §2c — Third pass: structural sweep (added after second stop-condition review)

Pass-2 saturation looked like exhaustion and was not. Instead of more semantic queries, this pass
enumerated the corpus **structurally** — `grep` over frontmatter tags for every source tagged with
model choice, benchmarks or openness (**44 sources**), then read the ones eight semantic queries had
never surfaced, plus a body-text grep for explicit rent-side phrasing.

Two qualifying sources were found, both of which had been sitting in the corpus, tagged, invisible to
search:

| Source | Cell | The unambiguous bit |
|---|---|---|
| **AI Index 2025** (Stanford HAI) | claim 2 NAS | inference cost **cratered 280-fold in 18 months** at fixed quality ($20/M → $0.07/M tokens); hw −30%/yr, energy efficiency +40%/yr — it attacks the own-side case on its own chosen ground, cost |
| **Jassy** (Amazon CEO), *Agility* | claim 2 NAW | the middle stack layer is explicitly for **"teams that don't want to train models"**, served by *"the largest selection of leading third-party frontier models"* — self-hosting is the bottom layer, for model builders |

**Considered and rejected** (recorded so the decision is auditable): GDPval (argument from silence —
never tested a small or open model); Nadella and Jensen Huang (both **A**-leaning); Chamath (no clean
stance); Ramaswamy (hosts open *alongside* frontier — ambiguous); Turc (mechanism explainer, no stance).

**Claim 2 reaches 16/16.** The caveat recorded in the deliverable: **NAW is three-quarters Amazon**
(two AWS events plus Jassy) plus Google once, because every non-vendor candidate argues the other
way. Usable but monotone.

## §8 — Final answer

**All three claims fill 4/4/4/4 — 48 sources, 44 distinct pages, no source used in two cells of the
same claim (CL-2 check passed), all slugs verified on disk.**

- **Claim 1 — 16/16.** Cui et al. (n=4,867, +26.08%), DORA 2025 (~5,000), Brynjolfsson-Li-Raymond
  (5,172 agents), GDPval (1,320 tasks) agreeing; METR (wrong by ~39 points), Dell'Acqua *Cybernetic
  Teammate* (decoupling the *other* way), Anicich & Brouwers (57% hide their AI use), Liu et al.
  (22.7% never fixed) against.
- **Claim 2 — 16/16, with one honest weakness.** BFCL, xLAM-2, Belcak and OpenJarvis agreeing;
  Allen & McDonald, Spracklen (**21.7% vs 5.2%** package hallucination), the CFA roundtable and
  **AI Index 2025** (280-fold cost collapse) against. **Its NAW cell is three-quarters Amazon** —
  the rent-side case is made almost entirely by hyperscalers, because Nadella, Jensen Huang and the
  BBC's adviser all argue A-leaning. And both strong cells rest on benchmark transfer: no source
  measures an SLM agent against an LLM agent on the same task under the same harness.
- **Claim 3 — 16/16, and the first-pass recommendation to drop it is withdrawn.** METR, Dell'Acqua's
  jagged-frontier RCT, Autor & Thompson and RaboResearch disagree — but all four by showing
  **augmentation failing**, not automation succeeding. No head-to-head automate-vs-assist study
  exists, and per the corpus probably cannot, because automation dissolves the per-worker outcome.

**Both earlier stopping judgements were wrong and are recorded as such**: pass 1 called claims 2 and
3 substantively unfillable; pass 2 called claim 2 exhausted at 14. Neither was true.

**Corrections applied during verification.** Two figures taken from a concept page's summary were
wrong against the primary source and were fixed in the deliverable: the Anthropic Economic Index
latest split is **53% / 44%** (the concept-page table said 53%/45%), and the Khan Academy line is
*"if we could do 3x more with the same resources, we will do 3x more; that would never be the
catalyst for layoffs"* — the catalyst being revenue, *"not AI"*.
