# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not** a software project. It is a personal **LLM wiki** repository following the pattern described in `llm-wiki.md` (Andrej Karpathy's "LLM Wiki" idea). The pattern: Claude incrementally builds and maintains a persistent, interlinked markdown knowledge base from raw sources the user curates. The wiki is a compounding artifact — knowledge is compiled once and kept current, not re-derived per query.

`llm-wiki.md` is the conceptual spec. **This CLAUDE.md is the schema layer** — the disciplined, repo-specific instantiation of that spec. Claude owns the wiki layer entirely; the user owns sourcing, exploration, and direction.

## Current state

The wiki has **not been instantiated yet**. The repo currently contains only `llm-wiki.md` and this file. There is no `raw/`, no `wiki/`, no `index.md`, no `log.md`. On the first real session, co-evolve the directory layout and conventions with the user before writing pages — do not invent structure unilaterally. Once decisions are made, record them in this file so future sessions inherit them.

Conventions to negotiate on first use (and then document below):
- Directory layout for raw sources vs. wiki pages (the spec suggests `raw/` and `wiki/` but does not mandate it).
- Page taxonomy (entities, concepts, summaries, comparisons, syntheses).
- Frontmatter conventions (tags, dates, source counts) — relevant if Obsidian Dataview will be used.
- Log entry prefix format. The spec recommends `## [YYYY-MM-DD] <op> | <title>` so `grep "^## \[" log.md` works as a CLI.
- Whether to use Obsidian-style `[[wikilinks]]` or standard markdown links.
- Whether/when to add a search tool (e.g. `qmd`) — index-only is fine at small scale.

## The three layers (architecture)

1. **Raw sources** — user-curated, immutable. Claude reads but never modifies. Source of truth.
2. **The wiki** — LLM-generated, LLM-owned markdown. Summaries, entity pages, concept pages, syntheses, an index, a log. Claude creates, updates, cross-references, and keeps consistent.
3. **The schema** — this file. The contract that turns Claude into a disciplined maintainer.

## The three operations

These replace "build / lint / test" for this repo. Apply them whenever the user invokes the corresponding intent.

### Ingest
A new source has been added to the raw collection.
1. Read the source.
2. Discuss key takeaways with the user before writing (default to one source at a time, supervised — unless the user says batch).
3. Write a summary page in the wiki.
4. Update **every** affected entity, concept, and topic page across the wiki — a single ingest may touch 10–15 files.
5. Update `index.md` (catalog of pages, one-line summaries, organized by category).
6. Append an entry to `log.md` using the agreed prefix format.
7. When new data contradicts an older claim, flag it explicitly on the affected page rather than silently overwriting.

### Query
The user asks a question against the wiki.
1. Read `index.md` first to locate relevant pages, then drill into them. Embedding-based RAG is unnecessary at moderate scale.
2. Synthesize an answer **with citations** (link back to wiki pages and, where relevant, raw sources).
3. Output format follows the question — markdown page, comparison table, slide deck (Marp), chart (matplotlib), canvas. Don't default to prose.
4. **File good answers back into the wiki as new pages.** Comparisons, analyses, discovered connections are valuable artifacts — they should not disappear into chat history. Update `index.md` and `log.md` accordingly.

### Lint
Periodic health check of the wiki.
- Detect contradictions between pages.
- Find stale claims superseded by newer sources.
- Flag orphan pages (no inbound links).
- Identify concepts mentioned but lacking their own page.
- Note missing cross-references and data gaps that warrant a web search or new source.
- Suggest new questions to investigate.
Report findings; let the user decide what to act on.

## Working principles

- **The wiki is Claude's codebase.** Touching 15 files in one ingest is normal and expected. Don't be timid about cross-cutting updates — that's the point of the pattern.
- **Cross-references are the product.** A page without links is undermaintained. Always check what should link to what when adding or updating a page.
- **Bookkeeping is the job.** Humans abandon wikis because maintenance grows faster than value. Claude's value here is precisely doing the bookkeeping — index updates, log entries, cross-reference repair, consistency sweeps — without being asked twice.
- **Sources are immutable.** Never edit files in the raw collection. Only read.
- **Co-evolve the schema.** When a workflow turns out to work well (or badly), update this file so future sessions inherit the lesson. The schema is meant to drift toward the user's actual workflow over time.
- **Citations beat assertions.** Wiki claims should be traceable to a source. When synthesizing across sources, say so.

## Tools and environment

- The wiki is intended to be browsed in **Obsidian** alongside the LLM session — graph view, backlinks, and Dataview (if frontmatter is used) are part of the user's reading experience. Prefer Obsidian-friendly conventions (e.g. `[[wikilinks]]`, attachment folder under `raw/assets/`) once that is confirmed with the user.
- **Obsidian Web Clipper** is the expected pipeline for getting web articles into the raw collection as markdown.
- **Marp** (markdown slide decks) and **matplotlib** charts are first-class output formats for query answers, alongside markdown pages.
- The repo is plain markdown in git — version history, branches, and diffs apply normally to wiki edits.

## Reference

`llm-wiki.md` — the upstream conceptual spec. Re-read it whenever a workflow question comes up that this file doesn't answer, then consider promoting the resolution into this file.
