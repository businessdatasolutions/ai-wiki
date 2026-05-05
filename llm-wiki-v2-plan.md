# LLM Wiki v2 — Staged Release Plan

## Context

`llm-wiki-v2.md` extends Karpathy's original LLM Wiki pattern with patterns proven by the agentmemory engine. It introduces nine feature clusters (lifecycle, knowledge graph, hybrid search, automation hooks, quality/self-correction, multi-agent collaboration, privacy/governance, crystallization, output formats) and explicitly says you don't need everything on day one — pick an entry point on its "implementation spectrum."

The current `ai-wiki/` repo is the v1 instantiation: 93 pages (54 entities, 17 concepts, 20 sources, 2 open threads, 0 syntheses), strict log conventions, alias-aware Quartz publishing, and a CLAUDE.md that already encodes ingest/query/lint operations and source-verification preflight. Several v2 ideas are *partly* present in disguise: `kind:` is proto-entity-typing, `log.md` is proto-audit-trail, "Debates / contradictions" prose sections are proto-supersession, the open `wiki/threads/` are proto-crystallization-targets.

The user has chosen "all v2 features, full build, staged release plan." The work below stages the spec into six small versions (v0.2 → v0.7) plus an optional v0.8+. Each version is small enough to absorb in days-to-weeks of single-user evolution, lands schema before tooling, and either ends with a clean migration of existing pages or doesn't touch them at all. The scale-down from "all features" comes from two honest cuts: (a) multi-agent / mesh-sync infrastructure is YAGNI for a single user — only the `scope: shared|private` flag is kept; (b) the four consolidation tiers from v2 are reduced to *naming the tiers in CLAUDE.md prose* rather than building separate storage layers, because raw → source → concept/entity → CLAUDE.md already maps onto them.

## Approach at a glance

| Version | Theme | Schema lands | Tooling lands | Migration |
| ------- | ----- | ------------ | ------------- | --------- |
| v0.2    | Lifecycle metadata | confidence, last_confirmed, source_count, supersedes/superseded_by, status: stale | `inject-stale-banner.tsx`, `lint-confidence.mjs` | 71 pages bulk-edited (concepts + entities) |
| v0.3    | Typed entity graph + synthesis contract | relationships block (YAML object), formalized `kind:` enum, `type: synthesis` page contract, derived_from | `inject-relationships.tsx`, `graph-export.mjs`, `synthesize` operation | 54 entities gain relationships; 2 open threads close into syntheses |
| v0.4    | Automation hooks | `§Hooks` in CLAUDE.md, `auto-` log prefix | `.claude/settings.json` hooks (SessionStart, Stop, PostToolUse), `session-start.mjs`, `session-end.mjs`, `lint-page.mjs`, `lint-orphans.mjs`, `repair-xrefs.mjs` | None (additive) |
| v0.5    | Hybrid search + retention | `accessed_at`, `quality_score`, `§Retention` curve | qmd install + index, scheduled lint hook, `quality-score.mjs` | Seed accessed_at; score concepts |
| v0.6    | Crystallization + LLM-as-judge | `crystallize` operation, `type: lesson` pages, `§Quality review` | `/crystallize` slash command, `judge-quality.mjs`, thread-aging hook | Crystallize 2 existing threads |
| v0.7    | Output formats + scoping | `scope: shared\|private`, `sensitive: true`, bulk-ops governance | `exclude-private.ts`, `/compare`, `/timeline`, `/marp-deck`, `/export-csv`, `ingest-filter.mjs` | None unless private flagged |
| v0.8+   | Deferred (mesh sync, external graph DB, on-query hook, consolidation infra) | — | — | only if forced |

Three principles run through every version:
1. **Schema-first.** CLAUDE.md sections + frontmatter contracts land before any tooling that depends on them.
2. **Hooks may not silently edit content.** They write to `log.md` and lint reports; content edits to `wiki/**/*.md` always require explicit user approval. This protects the "Claude owns the wiki, user owns direction" contract.
3. **Migrations are supervised.** Bulk edits to existing pages happen in batches of ~10, with Claude reading each page and writing defensible values — never via blind script.

---

## v0.2 — Lifecycle metadata: confidence, supersession, dates

**Goal.** Give every wiki claim a vocabulary for "how sure" and "what replaced what." Schema only, no automation, no decay math.

**Lands.** Cluster 1 (lifecycle) partial: confidence + supersession schema. Cluster 7 (privacy/governance) partial: codify `log.md` as the audit trail (already true — just declare it).

**Schema changes — `CLAUDE.md` adds new section §Lifecycle.**
- New frontmatter on **concepts and entities**:
  - `confidence: 0.0–1.0` (default 0.7 for one-source pages; rules: +0.05 per additional source, −0.1 if any contradicting source).
  - `last_confirmed: YYYY-MM-DD` (most recent ingest that reinforced the page).
  - `source_count: N` (computed from inbound source links).
- New frontmatter on **source pages**: `supersedes: [[old-source]]` (optional list).
- New frontmatter on **any page**: `status: stale` + `superseded_by: [[new-page]]` for retired-but-preserved pages.
- Promote in-prose "Debates" pattern to a **required `## Debates and supersession` section** on concept pages with >1 source.
- Update §Ingest to require setting/bumping `last_confirmed` and `source_count` on every touched concept/entity page.

**Tooling.**
- New extension `extensions/inject-stale-banner.tsx`: when frontmatter has `status: stale`, render a yellow callout at top of page linking to `superseded_by`. Mirrors the simple frontmatter-reading pattern of [`extensions/inject-type-tags.ts`](/Users/witoldtenhove/Projects/ai-wiki/extensions/inject-type-tags.ts).
- Optional: graph-view filter chip via the existing `inject-type-tags.ts` (`status/stale` already auto-emerges if status is added to tags).
- New script `scripts/lint-confidence.mjs` — read-only walker that prints distribution of confidence values and flags concepts >30 days old without a `last_confirmed` bump.

**Migration.**
- 71 pages (17 concepts + 54 entities) gain three new fields each. Done in supervised batches of ~10 per session. Claude reads page, counts inbound sources from `wiki/index.md` and `log.md`, sets defensible values. Highest-risk step in v0.2 — script-based defaults would be wrong half the time.
- Sources don't get `confidence` (sources are evidence, not claims).
- One-time scan of `log.md` for "supersedes / contradicts / replaces" wording; back-fill `supersedes:` on the few sources where it applies (Brynjolfsson Canaries vs the equalizing-effect framing is the obvious one).

**Prereqs.** None — this is the foundation.

**Cuts vs. v2 spec.**
- No retention/forgetting curve (deferred to v0.5).
- No four-tier consolidation pipeline. CLAUDE.md prose names the implicit tiers: `raw/` → sources → concepts/entities → CLAUDE.md. No directories or scripts for them.
- No quality_score (deferred to v0.5).

**Verification.**
- `npm run build` green.
- All 71 pages have all three new fields, no defaults left at 0.0.
- `lint-confidence.mjs` runs, prints distribution.
- Stale banner renders on a hand-picked test page (e.g. a sample-only source like `2026-05-03-rewired-second-edition-sample.md` once superseded by a full ingest).
- A `log.md` entry documents the bulk migration as `bulk-refactor | v0.2 lifecycle migration`.

---

## v0.3 — Typed entity graph + synthesis contract

**Goal.** Make relationships first-class and queryable, without breaking Quartz's wikilink resolver.

**Lands.** Cluster 2 (knowledge graph) most of it — typed relationships in frontmatter, formalized entity types, derived graph JSON. Cluster 8 (crystallization) schema slice — define what a synthesis page looks like; first synthesis is the v0.3 acceptance test.

**Schema changes — `CLAUDE.md` adds §Graph and §Synthesis.**
- Formalize `kind:` enum on entities: `person | organization | product | project | place | event | library | dataset | benchmark | venue`. Migrate any drift.
- New frontmatter on entities + concepts: `relationships:` as a YAML object list — **NOT** wikilinks-in-frontmatter (Quartz's link resolver doesn't traverse those reliably; you'd get partial/silent broken links).
  ```yaml
  relationships:
    - type: contradicts
      target: ai-employment-effects
      via: "occupation-level vs task-level"
      confidence: 0.7
    - type: authored-by
      target: Erik-Brynjolfsson
  ```
- Closed relationship vocabulary: `uses, depends-on, contradicts, supports, caused, fixed, supersedes, part-of, instance-of, authored-by, published-by, employs`.
- **Hard rule (load-bearing).** Every typed relationship in frontmatter must also appear as a body `[[wikilink]]` with a sentence of context. Frontmatter is the *typed* layer; body is the *navigable* layer; both are required. Lint enforces this from v0.4.
- New page type `type: synthesis`. Required sections: Question / Findings / Sources consulted / Lessons / Open questions. Required frontmatter: `derived_from: [[thread-A]], [[thread-B]]`, plus the standard lifecycle fields from v0.2.
- New CLAUDE.md operation **synthesize** (already in `log.md`'s permitted-ops enum but undefined): close a thread → produce a synthesis page → file under `wiki/syntheses/`.

**Tooling.**
- New extension `extensions/inject-relationships.tsx`: render the typed relationships as a structured panel on the page (separate from backlinks); group by relationship type.
- New script `scripts/graph-export.mjs`: walks all pages, emits `wiki/.graph.json` (gitignored) with nodes (slug, type, kind, confidence) and edges (type, source, target, confidence, via). This is the input format for any future hybrid search, agent traversal, or external visualization. Don't skip it — v0.5/v0.6 depend on it existing.

**Migration.**
- 54 entities gain a `relationships:` block (most small: org X `employs` person Y, person Y `authored` source Z, source Z `published-by` venue W). Batches of ~10 per session, supervised.
- 17 concepts gain relationships where they exist (mostly `supports` / `contradicts` between concepts; `authored-by` doesn't apply).
- The two open threads — [`organizational-frameworks-for-ai-adoption`](/Users/witoldtenhove/Projects/ai-wiki/wiki/threads/organizational-frameworks-for-ai-adoption.md) and [`ai-maturity-measurement-comparison`](/Users/witoldtenhove/Projects/ai-wiki/wiki/threads/ai-maturity-measurement-comparison.md) — close into the first two synthesis pages. The "How this thread should resolve" section in the threads is already a written-out crystallization plan; v0.3 just executes them.

**Prereqs.** v0.2 (relationships carry their own `confidence`).

**Cuts vs. v2 spec.**
- No external graph DB. Graph lives in frontmatter + `.graph.json`. Revisit only if the wiki crosses ~1000 pages.
- No automatic entity extraction beyond what Claude does manually during ingest.

**Verification.**
- `wiki/.graph.json` builds cleanly; ~54 entity nodes, ~17 concept nodes, 2-5 edges per node.
- Quartz build green; relationship panel renders; no broken links.
- `wiki/syntheses/` is no longer empty — at least one synthesis page closes one of the open threads, citing the thread + 5+ source pages.
- `index.md` Syntheses section drops the "(empty)" placeholder.

---

## v0.4 — Automation hooks (the bookkeeping cliff drops)

**Goal.** Move from "user remembers to ask for lint" to "lint runs on session-end automatically." This is where v2's promise of near-zero maintenance actually lands.

**Lands.** Cluster 4 (automation hooks) most of it — on-new-source / on-session-start / on-session-end / on-edit. Defer scheduled jobs to v0.5. Cluster 5 (quality / self-correction) partial — hook-driven self-healing for cheap cases (orphan detection, broken xref repair).

**Schema changes — `CLAUDE.md` adds §Hooks.**
- Hard rule: hooks may write to `log.md` and lint reports; hooks may NOT edit any `wiki/**/*.md` content page without explicit user approval in-session. Encoded in CLAUDE.md as a non-negotiable.
- New log entry convention: prefix `auto-` for hook-fired operations (`auto-lint`, `auto-supersession-check`).

**Tooling.**
- `.claude/settings.json` gains a `hooks` block:
  - `SessionStart` → `scripts/session-start.mjs`: load `wiki/index.md` head, last 10 `log.md` entries, list of `status: stale` pages, list of `confidence < 0.5` pages, into the conversation context.
  - `Stop` → `scripts/session-end.mjs`: diff staged wiki changes, append a single `log.md` entry summarizing the session.
  - `PostToolUse` filter on `Edit|Write` matching `wiki/**/*.md` → `scripts/lint-page.mjs <file>`: checks frontmatter contract, broken wikilinks, missing required sections, the v0.3 frontmatter-relationship-must-have-body-wikilink rule.
- New scripts under `scripts/`:
  - `session-start.mjs`, `session-end.mjs`
  - `lint-page.mjs` (single-file lint, fast)
  - `lint-orphans.mjs` (whole-wiki orphan scan)
  - `repair-xrefs.mjs` (read-only proposer; outputs diffs to stdout, doesn't apply)
- The session-end hook also calls `scripts/graph-export.mjs` from v0.3 so `.graph.json` stays current.

**Migration.** Minimal — one-time pass to make sure every page already passes `lint-page.mjs` so the hook doesn't fire warnings on unrelated edits.

**Prereqs.** v0.2 (so session-start can highlight low-confidence pages), v0.3 (so hooks have a current graph).

**Cuts vs. v2 spec.**
- No on-query hook yet (file-back-as-page is human-judgment, not a hook target).
- No scheduled retention decay (deferred to v0.5).
- Hooks remain read-mostly + log writes only.

**Verification.**
- Stop a session mid-edit; reopen Claude; SessionStart injects staged-changes summary and last log entries.
- Save a page with a deliberately broken `[[wikilink]]`; PostToolUse lint surfaces it pre-commit.
- `log.md` contains `auto-lint` entries with timestamps.

---

## v0.5 — Hybrid search + retention/forgetting

**Goal.** At ~93 pages and growing, `index.md` is starting to creak (v2 says scale features kick in past 100-200 pages). Add real search before flat index actually breaks. Land the long-promised retention curve, now that hooks can run it on schedule.

**Lands.** Cluster 3 (hybrid search) full — qmd or equivalent (BM25 + vector + RRF), with graph traversal as the third stream from v0.3. Cluster 1 remainder — Ebbinghaus retention, scheduled lint, decay surfaces. Cluster 4 remainder — scheduled hooks. Cluster 5 down-payment — mechanical quality_score (LLM-judged version comes in v0.6).

**Schema changes — `CLAUDE.md` adds §Retention and updates §Lifecycle.**
- New frontmatter on concepts/entities: `accessed_at: YYYY-MM-DD` — bumped by SessionStart hook when the page is read into context. This is the reinforcement signal.
- New CLAUDE.md §Retention: simple curve `effective_confidence = stored_confidence * exp(-days_since_access / tau)` with tau ≈ 90 days for concepts, 365 for entities, never decays sources. Surfaced via lint — never auto-deletes, never auto-rewrites.
- New `quality_score: 0.0–1.0` field on concepts + syntheses. Lint computes mechanically: structure (required sections present?) + citation density (each major claim near a `[[source]]`?) + cross-consistency (no contradictions with linked pages without a Debates section?).
- CLAUDE.md gains §Search: rule "for any query that would touch >5 pages from `index.md`, run qmd first to narrow to top 10."

**Tooling.**
- Install qmd; configure index over `wiki/`. Either CLI shell-out or MCP server (MCP is cleaner — pick that if available).
- Scheduled hook (cron-style or `/loop` invocation if no cron in environment): daily run that touches `accessed_at` on referenced pages, surfaces decay candidates, **proposes** stale-marking via log entry but doesn't apply.
- New script `scripts/quality-score.mjs`: structure check, citation check, consistency check. Writes `quality_score` and `quality_notes` to frontmatter (this is the only auto-write from a hook in the whole rollout — and it's a derived field, not editorial content).

**Migration.**
- One-time qmd index build (minutes).
- Seed `accessed_at` from each page's `last_confirmed`.
- Compute `quality_score` for all 17 concepts; expect 2-3 below threshold needing structural cleanup. Cleanup happens in v0.5 itself.

**Prereqs.** v0.4 (hooks fire the schedule).

**Cuts vs. v2 spec.**
- Quality scoring stays mechanical here. LLM-as-judge defers to v0.6.
- Retention is read-only — no auto-deletion, ever. v2's "moved to a bottom drawer" = "appears in lint output, not on the homepage."

**Verification.**
- qmd `query "jagged frontier"` returns the Dell'Acqua source + jagged-frontier concept + relevant entities, fused-rank.
- Daily lint produces a "decay candidates" list as a log entry; nothing changes on those pages.
- All concept pages have `quality_score`; bottom 3 cleaned up.

---

## v0.6 — Crystallization + LLM-as-judge quality

**Goal.** Make exploration itself a first-class source. Every closed thread becomes a synthesis. Every query worth filing back is filed back. Quality is now scored by reasoning, not just structure.

**Lands.** Cluster 8 (crystallization) full — thread → synthesis is a named, hooked, instrumented operation, plus extracted lessons. Cluster 5 remainder — LLM-as-judge quality scoring + contradiction-resolver-as-proposer.

**Schema changes — `CLAUDE.md` adds §Crystallization and §Quality review.**
- New named operation **crystallize**: closed thread → synthesis page → extracted lessons under `wiki/lessons/`. Each lesson is `type: lesson`, ≤200 words, one canonical claim, source list, inherits lifecycle fields from v0.2. Lessons decay aggressively (tau ≈ 60 days).
- §Quality review: a second-pass Claude API call with reviewer prompt evaluates each new/edited concept/synthesis against rubric; score lands in `quality_score`, notes in `quality_notes`. Replaces the mechanical scorer from v0.5 for these page types (entities still use mechanical).
- Contradiction resolver: when supersession-check finds a candidate, it produces a **proposed diff** in `log.md` (not an edit). Human approves before any page change.

**Tooling.**
- New `/crystallize <thread-slug>` slash command in `.claude/commands/`.
- `scripts/judge-quality.mjs` — Claude API call with reviewer prompt; writes back `quality_score` and `quality_notes`.
- Hook addition (extends v0.4 set): on session-end, if a `type: thread, status: open` page hasn't been edited in 14 days but its referenced sources have grown, propose closing/crystallizing in the session-end log entry.

**Migration.**
- Crystallize the two threads closed in v0.3 *again* under the new operation if needed (the v0.3 syntheses become the baseline; v0.6 adds the lessons extraction).
- LLM-judge pass over all 17 concepts and any syntheses; expect 3-5 needing rewrites.

**Prereqs.** v0.3 (synthesis schema), v0.4 (hooks), v0.5 (quality_score field exists).

**Cuts vs. v2 spec.**
- LLM-judge runs on edits + on-demand, not nightly over the whole wiki (cost).

**Verification.**
- `wiki/lessons/` directory exists with at least 3-5 lessons extracted from the two crystallized threads.
- A lesson page is reachable via graph view from its parent concept.
- `quality_score` distribution is plausible (most pages 0.7-0.9, outliers <0.5 with cleanup tickets).

---

## v0.7 — Output formats + privacy/scoping

**Goal.** Stop forcing every answer into a markdown page. Land the small bits of governance that actually matter for a single user.

**Lands.** Cluster 9 (output formats) full — comparison tables, timelines, dep graphs, Marp decks, JSON/CSV exports — as **slash-command templates**, not auto-generated artifacts. Cluster 7 remainder — filter-on-ingest stub, shared/private scoping, bulk-ops governance via `log.md`. Cluster 6 partial — only `scope: shared|private` is kept; mesh-sync is deferred indefinitely.

**Schema changes.**
- New frontmatter `scope: shared | private` (default `shared`; private pages excluded from `npm run build`, still visible in Obsidian).
- New frontmatter on sources `sensitive: true` → triggers ingest-time filter.
- Bulk ops governance: any operation touching >10 pages must log as `bulk-refactor | <intent>` with affected slug list and reversibility note. Codify the precedent established in the v0.2 migration.

**Tooling.**
- New extension `extensions/exclude-private.ts`: drops `scope: private` pages from the Quartz build.
- New slash commands in `.claude/commands/`:
  - `/compare <a> <b>` — comparison table.
  - `/timeline <concept>` — markdown or Mermaid timeline.
  - `/marp-deck <synthesis>` — generate Marp slides from a synthesis page.
  - `/export-csv <query>` — JSON/CSV export from the graph + qmd.
  Each is a templated output recipe Claude follows, not infrastructure.
- `scripts/ingest-filter.mjs` — regex-based PII/secret strip on raw markdown before Claude reads it. Conservative defaults; configurable in CLAUDE.md.

**Migration.** Minimal — `scope: shared` is default; nothing changes for existing pages until something is marked private.

**Prereqs.** v0.4 (hooks fire ingest-filter), v0.6 (synthesis pages give Marp something to render).

**Cuts vs. v2 spec.**
- No mesh sync, no work coordination, no shared/private *promotion* workflow. Revisit only if a second user appears.
- No JSON/CSV export "infrastructure" — slash commands ask Claude to write the right shape and stop.

**Verification.**
- A test page marked `scope: private` is invisible on the published Quartz site, visible in Obsidian, queryable by Claude.
- One Marp deck builds from a synthesis page.
- `ingest-filter.mjs` passes on a planted-secret fixture.

---

## v0.8+ — Deferred

Revisit only if forced.
- **Mesh sync** (cluster 6 remainder): if a coauthor or second machine appears.
- **Consolidation tier infrastructure** (cluster 1 deferred piece): if the wiki crosses ~500 pages and the four-tier model starts paying its weight.
- **External graph DB**: if `.graph.json` exceeds a few MB and traversal queries get slow.
- **On-query hook** (cluster 4 remainder): if the user finds they're forgetting to file good answers back.

---

## Cross-version risks

1. **Bulk migration consistency (v0.2, v0.3).** Adding confidence to 71 pages or relationships to 54 entities is the single most likely place to introduce silent drift — half rich, half rubber-stamped 0.7. Mitigation: supervised batches of ~10, treat the migration itself as multi-session work, never a single-shot script.
2. **Quartz link resolver vs. typed-relationships frontmatter (v0.3).** Quartz crawls body wikilinks; YAML object relationships are invisible to it. If relationships are ever encoded as `[[...]]` strings inside frontmatter, partial resolution + silent broken links result. The split-layer rule ("typed in frontmatter, navigable in body, both required") is load-bearing — `lint-page.mjs` (v0.4) enforces it.
3. **Hook-driven auto-edits (v0.4-v0.6).** Strong temptation to let session-end auto-mark stale or auto-rewrite low-quality pages — exactly the wrong move. A hook that silently changes content destroys the "Claude owns the wiki, user owns direction" contract. Mitigation: hard CLAUDE.md rule, encoded from v0.4 onward — hooks may write to `log.md` and lint reports only; the only frontmatter-write exception is the derived `quality_score` field in v0.5/v0.6.

## Critical files to touch

Each version edits these (in order of frequency):
- [/Users/witoldtenhove/Projects/ai-wiki/CLAUDE.md](/Users/witoldtenhove/Projects/ai-wiki/CLAUDE.md) — every version adds a section before its tooling lands.
- [/Users/witoldtenhove/Projects/ai-wiki/wiki/log.md](/Users/witoldtenhove/Projects/ai-wiki/wiki/log.md) — every migration and bulk-op logs here.
- [/Users/witoldtenhove/Projects/ai-wiki/wiki/index.md](/Users/witoldtenhove/Projects/ai-wiki/wiki/index.md) — synthesis section (v0.3), lesson section (v0.6), private-scope handling (v0.7).
- [/Users/witoldtenhove/Projects/ai-wiki/quartz.config.ts](/Users/witoldtenhove/Projects/ai-wiki/quartz.config.ts) — register new extensions in v0.2, v0.3, v0.7.
- [/Users/witoldtenhove/Projects/ai-wiki/extensions/](/Users/witoldtenhove/Projects/ai-wiki/extensions/) — new files added in v0.2, v0.3, v0.7. Pattern follows [`inject-type-tags.ts`](/Users/witoldtenhove/Projects/ai-wiki/extensions/inject-type-tags.ts).
- [/Users/witoldtenhove/Projects/ai-wiki/.claude/settings.json](/Users/witoldtenhove/Projects/ai-wiki/.claude/settings.json) — hooks block in v0.4, scheduled hook in v0.5.
- New `/Users/witoldtenhove/Projects/ai-wiki/scripts/` directory created in v0.2 (`lint-confidence.mjs`); each subsequent version adds scripts to it.

Per-version migration targets:
- v0.2: 17 concepts under `wiki/concepts/` + 54 entities under `wiki/entities/` (71 pages).
- v0.3: same 71 pages gain relationships; both threads in `wiki/threads/` close into new files in `wiki/syntheses/`.
- v0.6: new `wiki/lessons/` directory.

## Verification strategy across versions

After each version lands:
1. `npm run build` succeeds with no warnings.
2. `npm run serve` shows the new behavior on a representative page (e.g. stale banner in v0.2; relationship panel in v0.3; rendered Marp deck in v0.7).
3. `lint-confidence.mjs` (v0.2) / `lint-page.mjs` (v0.4+) passes on all `wiki/**/*.md`.
4. The version's acceptance test runs (e.g. v0.3 closes a thread into a synthesis; v0.6 produces lessons; v0.7 hides a private page).
5. A `log.md` entry records the version landing as `bulk-refactor | v0.X <theme>`.

## Sequencing recommendation

Treat each version as one or two focused sessions, not one big push. Suggested cadence: v0.2 over 2-3 sessions (because of the bulk migration), v0.3 over 2 sessions, v0.4 in 1 session, v0.5 in 2 sessions (qmd install + retention), v0.6 in 2 sessions, v0.7 in 1 session. Each version is independently shippable — pause between any two and the wiki keeps working.
