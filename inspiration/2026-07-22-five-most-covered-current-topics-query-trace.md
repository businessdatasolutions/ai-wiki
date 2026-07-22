# Query trace — Five most covered & most current topics

**Date:** 2026-07-22 · **Skill:** `traceable-wiki-answer` (`/wqa`)

---

## §1 — Question

> What are the five most covered and most current topics in the wiki? Return a matrix with currency on the x-axis and coverage on the y-axis.

**Facets:** (a) coverage metric per topic, (b) currency metric per topic, (c) select top five, (d) plot on a coverage × currency matrix. **Language:** English.

This is a **meta / corpus-analytics** question, not a content question. "Coverage" maps to the concept-page frontmatter field `source_count` (how many wiki sources substantiate the page); "currency" maps to `last_confirmed` (the date of the most recent ingest that reinforced the page). So the authoritative data is frontmatter across `wiki/concepts/`, not the body text of any source.

## §2 — Paths explored

- **Mandated retrieval:** `node scripts/wiki-retrieve.mjs --json -n 12 "…"` — ran per skill contract. Graph available; 11 qmd hits, 28 fused candidates. **Every candidate was a single `source` page** (RAG/LLM-wiki explainers, Snapchat/Rolls-Royce CEO talks, quantization, distress-prediction). Correct behaviour for semantic search, but the **wrong granularity** for a topic-coverage ranking.
- **Supplemental scan (authoritative):** grep of `source_count` / `last_confirmed` / `confidence` / `accessed_at` across all 40 `wiki/concepts/*.md`, sorted by coverage.
- **Verification read:** the top-5 concept pages' frontmatter, read directly to confirm counts and dates.

## §3 — How the ignore decision was made

The retrieval ledger answers "which pages are semantically nearest to the query string" — but this question needs "which concept pages have the highest `source_count`." Those are different operations. All 28 retrieval candidates are therefore IGNORE under one of two reason-classes: **wrong-granularity** (a single source page can't express topic-level coverage) or **off-facet** (topically unrelated). The USE set is derived instead from the frontmatter scan: the five concept pages with the highest `source_count`, each verified by a direct read.

## §4 — What was ignored (with reason-class)

| Candidate | Reason-class |
|---|---|
| `concepts/micro-productivity-trap` (40 sources) | below-threshold (6th) |
| `concepts/durable-skills` (37 sources) | below-threshold (7th) |
| `sources/2026-04-27-liu-rag-llm-wiki-or-gbrain…` | wrong-granularity |
| `sources/2026-04-28-ftsg-convergence-outlook-2026` | wrong-granularity |
| `sources/2026-04-26-…-evan-spiegel-snapchat-ceo` | wrong-granularity |
| `sources/2026-04-18-mysore-…-extending-karpathy-llm-wiki` | wrong-granularity |
| `sources/2026-07-01-mcgrath-2026-power-of-strategic-centering` | wrong-granularity |
| `sources/2026-04-16-raju-rag-isnt-dead…` | wrong-granularity |
| `sources/2025-05-17-turc-…-quantization-fundamentals` | off-facet |
| `sources/2026-05-24-erginbilgic-…-rolls-royce-turnaround` | off-facet |
| `sources/2024-06-22-hajek-…-distress-prediction` | off-facet |
| `sources/2021-09-16-ten-things-corporate-culture` | off-facet |

(28 retrieval candidates total; representative rows shown. Full ledger in the `.json` trace.)

## §5 — What was used

| USE page | Exists | Coverage | Last confirmed |
|---|---|---|---|
| `wiki/concepts/enterprise-ai-adoption.md` | ✓ | 90 | 2026-07-22 |
| `wiki/concepts/agent-harness.md` | ✓ | 74 | 2026-07-15 |
| `wiki/concepts/ai-employment-effects.md` | ✓ | 67 | 2026-07-21 |
| `wiki/concepts/automation-vs-augmentation.md` | ✓ | 54 | 2026-07-14 |
| `wiki/concepts/agentic-engineering.md` | ✓ | 43 | 2026-07-01 |

## §6 — Where the facts live

| Anchor | Page | Fact | Location |
|---|---|---|---|
| W1 | enterprise-ai-adoption | 90 sources · confirmed 2026-07-22 | frontmatter `source_count` / `last_confirmed` |
| W2 | agent-harness | 74 sources · confirmed 2026-07-15 | frontmatter |
| W3 | ai-employment-effects | 67 sources · confirmed 2026-07-21 | frontmatter |
| W4 | automation-vs-augmentation | 54 sources · confirmed 2026-07-14 | frontmatter |
| W5 | agentic-engineering | 43 sources · confirmed 2026-07-01 | frontmatter |

## §7 — Final answer

See the reply / below.

## §8 — Answer-element → wiki-element map

Every cell placement in the matrix rests on the `source_count` (y) and `last_confirmed` (x) of exactly one USE concept page: W1→enterprise-ai-adoption, W2→agent-harness, W3→ai-employment-effects, W4→automation-vs-augmentation, W5→agentic-engineering. No claim is unanchored.

---

### The matrix

Coverage (y) × Currency (x). Currency = days since `last_confirmed` (today = 2026-07-22).

```
COVERAGE
 (sources)
   ^
90 |  [W1] enterprise-ai-adoption ·························· (0d)
   |
74 |  [W2] agent-harness ······················· (7d)
   |
67 |  [W3] ai-employment-effects ······················· (1d)
   |
54 |  [W4] automation-vs-augmentation ····· (8d)
   |
43 |  [W5] agentic-engineering ··· (21d)
   |
   +----------------------------------------------------------> CURRENCY
      AGING (>21d)      RECENT (8-21d)        FRESH (<=7d)
```

3×3 quadrant view:

|                    | **Aging (>21d)** | **Recent (8–21d)** | **Fresh (≤7d)** |
|--------------------|:---:|:---:|:---:|
| **High (≥50 src)** | — | automation-vs-augmentation [W4]; agentic-engineering [W5] | **enterprise-ai-adoption [W1]; ai-employment-effects [W3]; agent-harness [W2]** |
| **Mid (25–49)**    | — | — | *(near-misses: micro-productivity-trap, durable-skills)* |
| **Emerging (<25)** | — | — | — |

**Reading it:** all five best-covered topics also sit in the two freshest currency bands — the wiki has no "stale but heavily-covered" topic. Coverage and currency **correlate here**: the pages the wiki has invested most sources in are also the ones it keeps actively re-confirming. The densest cell is top-right (high coverage / fresh): [W1] enterprise-ai-adoption, [W3] ai-employment-effects, [W2] agent-harness.
