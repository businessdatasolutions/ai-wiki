---
type: query-trace
question: "Please give me an overview of AI maturity frameworks discussed in the wiki"
date: 2026-11-04
refreshes: 2026-07-01
language: en
trace: "2026-11-04-ai-maturity-frameworks-overview-query-trace.json"
pages_used: 4
pages_ignored: 51
---

# Query trace — AI maturity frameworks overview (refresh, 4 Nov 2026)

## 1. Question

- **Original:** Please give me an overview of AI maturity frameworks discussed in the wiki
- **Restated:** Four months after the 2026-07-01 run, which AI-maturity and AI-adoption frameworks does the wiki hold? What changed in their claims, and what has been added?
- **Purpose of this refresh:** to update the visual atlas built from the July answer (`2026-07-01-ai-maturity-frameworks-visuals.html`).
- **Facets** (as in July):
  1. Which sources measure AI *maturity* numerically, with what instrument, and what number do they report?
  2. What is the wiki's central staged-maturity model (MIT CISR Four Stages), and what does it claim?
  3. Beyond maturity as a number, what is the full cluster of organisational AI-adoption frameworks, and where does "maturity" sit among them?
  4. Which well-known maturity frameworks does the wiki *not* yet cover?

## 2. Paths explored

Retrieval ran via `node scripts/wiki-retrieve.mjs --json -n 12 "Please give me an overview of AI maturity frameworks discussed in the wiki"`: qmd hybrid search (10 hits) ∪ 1-hop graph traversal, RRF-fused, decay-ranked, `today` = 2026-11-04. The graph was available and there was no `graph_warning`; the run returned 55 candidates. No gap expansion was needed.

**qmd hits** (relevance stream)

| # | Page | type | qmd score | fused | verdict |
|---|------|------|-----------|-------|---------|
| 1 | `wiki/threads/organizational-frameworks-for-ai-adoption.md` | thread (closed) | 0.33 | 0.840 | IGNORE |
| 2 | `wiki/concepts/enterprise-ai-adoption.md` | concept | 0.25 | 0.964 | **USE** |
| 3 | `wiki/sources/2026-04-28-mittri-cisco-ai-enabled-enterprise.md` | source | 0.20 | 0.910 | IGNORE |
| 4 | `wiki/threads/ai-maturity-measurement-comparison.md` | thread (open) | 0.17 | 0.801 | **USE** |
| 5 | `wiki/threads/ai-worker-maturity-levels.md` | thread (closed, new 2026-08-31) | 0.14 | 0.788 | IGNORE (resolved into its synthesis) |
| 6 | `wiki/sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage.md` | source (new) | 0.13 | 0.869 | IGNORE |
| 7 | `wiki/sources/2026-03-30-liu-debt-behind-the-ai-boom.md` | source | 0.11 | 0.856 | IGNORE |
| 8 | `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | synthesis | 0.10 | 0.730 | **USE** |
| 9 | `wiki/concepts/founder-led-sales.md` | concept | 0.09 | 0.831 | IGNORE |
| 10 | `wiki/sources/2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work.md` | source | 0.08 | 0.819 | IGNORE |

**Graph neighbours** (`--hops 1`). The table shows the neighbours that were used or discussed; the full list is in the JSON trace.

| Page | reached via | fused | verdict |
|------|-------------|-------|---------|
| `wiki/syntheses/ai-worker-maturity-levels.md` | enterprise-ai-adoption --supports--> | 0.283 | **USE** (the resolved form of qmd hit 5; graph-only, so it gets a manual bump) |
| `wiki/concepts/technology-adoption-theories.md` | enterprise-ai-adoption --supports--> | 0.365 | IGNORE (redundant: the synthesis records the gap it fills) |
| `wiki/concepts/jagged-frontier.md`, `micro-productivity-trap`, `responsible-ai`, `automation-vs-augmentation` | enterprise-ai-adoption --uses/caused/part-of/supports--> | 0.40–0.46 | IGNORE (off-facet) |
| *(about 40 further concepts and sources)* | | | IGNORE |

## 3. Ignore policy applied

- **`redundant`.** Two closed threads were resolved into syntheses that are in the USE set (`synthesized_into` / `derived_from`). Single-instrument sources are already carried in the cross-walk thread, and the synthesis's refresh notes already carry the Catlin source and the adoption-theories gap.
- **`off-facet`.** Adjacent concepts and sources reached by vocabulary or by graph edge (AI financing, sales, productivity RCTs, labour-market and runtime concepts).
- **`below-threshold`.** Low-scoring graph-only neighbours.
- **`wrong-granularity`.** Entity cards.

## 4. Information ignored

| Page | reason-class | one-line reason |
|------|--------------|------------------|
| `wiki/threads/organizational-frameworks-for-ai-adoption.md` | redundant | closed 2026-05-05, `synthesized_into` the USE synthesis |
| `wiki/threads/ai-worker-maturity-levels.md` | redundant | closed 2026-08-31; its answer is the USE synthesis `ai-worker-maturity-levels` |
| `wiki/sources/2026-04-28-mittri-cisco-ai-enabled-enterprise.md` | redundant | its 13% "ready" figure is carried in the cross-walk thread |
| `wiki/sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage.md` | redundant | restates McKinsey *Rewired*; carried in the synthesis's 2026-07-09 refresh |
| `wiki/concepts/technology-adoption-theories.md` | redundant | the synthesis names it as the gap (TAM / UTAUT / DOI / TOE); these theories predict uptake rather than prescribe |
| `wiki/sources/2026-03-30-liu-debt-behind-the-ai-boom.md` | off-facet | AI-infrastructure financing |
| `wiki/concepts/founder-led-sales.md` | off-facet | sales |
| `wiki/sources/2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work.md` | off-facet | productivity RCT, not a maturity instrument |
| ~45 further concepts, sources and entity cards | off-facet / below-threshold / wrong-granularity | see the JSON trace |

## 5. Information used

| Page | type | effConf | status since July | contribution |
|------|------|---------|-------------------|--------------|
| `wiki/threads/ai-maturity-measurement-comparison.md` | thread (open) | n/a | **extended** 2026-08-31 | the cross-walk (1% / 7% / 12% / 13%) is unchanged; adds a worker-level axis (Blum); the Gartner/Deloitte gap is still open |
| `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | synthesis | 0.90 stored (0.53 effective before this run's bump) | refreshed 2026-07-09 and 2026-07-15 (14 → 20 sources) | 11 layers, no twelfth added; "orchestration, not adoption" (Tate); three lived operator cases; TAM / UTAUT / DOI / TOE flagged as not yet in the synthesis |
| `wiki/concepts/enterprise-ai-adoption.md` | concept | 0.95 | heavily extended (≈450 lines since July) | the MIT CISR stages (unchanged); adjacent figures: ~30% of pilots reach production (BBC panel), "just 26% of organizations have achieved value from AI" (BCG via the HBS AI Institute), the adoption jump attributed to survey wording (Hatzius) |
| `wiki/syntheses/ai-worker-maturity-levels.md` | synthesis | 0.80 | **new** 2026-08-31 | a six-level worker scale (L0 Bystander → L5 Multiplier), six dimensions, Beutler's Ask / Assist / Automate mapped to L1 / L2 / L3 |

## 6. Answer-element map

| Anchor | Answer element (claim) | Wiki page(s) | Section / span used |
|--------|--------------------------|--------------|----------------------|
| [W1] | Four instruments still report "success" at 1% (AI Index / McKinsey), 7% (MIT CISR Stage 4), 12% (Werner-Le-Brun) and 13% (Cisco): "whatever you call success, it's rare". Every one of them measures the firm; a worker-level axis was added on 2026-08-31, with the caveat that it is N=1 and unvalidated; Gartner and Deloitte models are still not ingested | [[threads/ai-maturity-measurement-comparison]] | ## Updated cross-walk / ### A different unit of analysis: the individual worker / ## What's missing |
| [W2] | The synthesis still holds 11 complementary framework layers; its July refreshes added no new layer; Tate reframes the field's problem as "orchestration, not adoption"; the information-systems adoption theories (TAM, UTAUT, DOI, TOE) are a recorded gap | [[syntheses/organizational-frameworks-for-ai-adoption]] | Refreshed 2026-07-09 / 2026-07-15 / ## Open questions |
| [W3] | MIT CISR's Four Stages (28 / 34 / 31 / 7%) are unchanged. Adjacent figures since July: about 30% of pilots reach production (one firm's index, BBC *AI Decoded*); BCG's "just 26% of organizations have achieved value from AI"; Hatzius (Goldman Sachs) attributes the widely cited jump in US firm adoption (~10% → >20%) to a change in survey wording | [[concepts/enterprise-ai-adoption]] | ## The MIT CISR Four Stages / ## Return on intelligence / change-resilience paragraph / "The aggregate says adoption is lower than it looks" |
| [W4] | A six-level worker scale: L0 Bystander, L1 Conversationalist (≈ Ask), L2 Operator (≈ Assist), L3 Delegator (≈ Automate entry), L4 Orchestrator, L5 Multiplier. It scores six dimensions, defines each level by who produces, checks and decides, and is wiki-authored and unvalidated (confidence 0.80) | [[syntheses/ai-worker-maturity-levels]] | ### The synthesized model: six levels / ### Caveats |

## 7. Final answer

**The core picture has not changed since July.**
- **Maturity is still rare.** The cross-walk still reports 1% (AI Index / McKinsey "mature"), 7% (MIT CISR Stage 4), 12% (Werner-Le-Brun transformation success) and 13% (Cisco "ready"). The headline still holds: "whatever you call success, it's rare" [W1].
- **The stage model is unchanged.** MIT CISR's Four Stages (28 / 34 / 31 / 7%) and its Four S blockers at the Stage 2→3 transition have not moved [W3].
- **The framework cluster is still 11 layers.** The organisational-frameworks synthesis grew from 14 to 20 sources but added no twelfth layer [W2].

**Three things are new.**

1. **A worker-level axis.** Every instrument in the cross-walk measures the *firm*. In August the wiki added the *individual worker* as a separate unit of analysis [W1] and resolved it into a six-level scale: L0 Bystander → L1 Conversationalist → L2 Operator → L3 Delegator → L4 Orchestrator → L5 Multiplier [W4].
   - The scale maps Beutler's ladder onto individuals: Ask ≈ L1, Assist ≈ L2, Automate (entry) ≈ L3 [W4].
   - It is wiki-authored and not validated against outcomes [W4].
   - The thread's caveat is that the evidence for the worker axis is a single self-reported case [W1].
2. **Adjacent figures, with a warning about what adoption numbers measure.**
   - About 30% of pilots reach production, in one firm's index [W3].
   - BCG finds "just 26% of organizations have achieved value from AI" [W3].
   - Goldman Sachs attributes the widely cited jump in US firm adoption (~10% → >20%) to a looser survey question: "any business function" instead of "current production" [W3].
   - These measure value and production, not maturity, so they sit beside the cross-walk rather than in it.
3. **A sharper governing question.** Tate's "the problem is no longer adoption of technology … it is orchestration of technology" names what the 11 layers are collectively for [W2].

**Gaps.**
- Gartner's and Deloitte's maturity models are still not in the wiki [W1].
- The information-systems adoption theories (TAM, UTAUT, Rogers' DOI, TOE) now have a concept page but are not yet placed in the synthesis [W2].

**Atlas changes that follow.**
- Section 0 keeps its five bars and gains a note on the worker axis and the adjacent figures [W1, W3].
- Section 9 gains the Ask/Assist/Automate → L1/L2/L3 mapping [W4].
- A new section 12 draws the worker scale [W4].

## 8. Trace artifact

Machine-readable provenance: `inspiration/2026-11-04-ai-maturity-frameworks-overview-query-trace.json` in the ai-wiki repository. The run this refreshes is `inspiration/2026-07-01-ai-maturity-frameworks-overview-query-trace.{md,json}`.
