# Log

Append-only chronological record of wiki operations. Strict prefix format so `grep "^## \[" wiki/log.md | tail -10` works as a CLI. Format (indented to keep grep clean):

    ## [YYYY-MM-DD] <op> | <title>

Permitted operations: `ingest`, `query`, `lint`, `synthesize`, `refactor`. See [the design doc, §9.2](../docs/superpowers/specs/2026-04-28-llm-wiki-design.md#92-wikilogmd) for details.

---

## [2026-04-28] refactor | scaffold initialized

Initial wiki scaffold built per [the design doc](../docs/superpowers/specs/2026-04-28-llm-wiki-design.md). Created `raw/` (articles, papers, lectures, books, images, assets) and `wiki/` (sources, entities, concepts, syntheses, threads) skeletons with `.gitkeep` placeholders, plus this log and a canonical `index.md`. Ready for first source ingest.

## [2026-04-28] refactor | added raw/reports/ and kind: report

Industry reports, government white papers, consultancy decks, and sell-side equity research didn't fit cleanly into `raw/papers/` (academic) or `raw/articles/` (web-clipped markdown). Added `raw/reports/` as a peer of `raw/papers/`, extended the source-page `kind:` enum to include `report`, and added a row to design doc §10 + decision log §18. Sub-types are disambiguated via tags (`consultancy`, `government`, `equity-research`, `ngo`).
