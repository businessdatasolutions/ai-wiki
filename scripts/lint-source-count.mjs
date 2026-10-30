#!/usr/bin/env node
// Read-only check of `source_count` on concept and entity pages against the
// number of wiki/sources/ pages that actually cite each page.
//
// CLAUDE.md §Lifecycle defines source_count as the count of source pages that
// cite or substantiate the page. In practice ingests added +1 per new source,
// which misses every source that links a concept without "updating" it, so the
// stored values drifted: on 2026-10-25, 41 of 54 concepts and 70 of 206
// entities disagreed with the count. Nothing checked it, the same silent
// failure mode as the index gap that lint-index-completeness.mjs exists for.
//
// A source cites a page when it:
//   1. wikilinks it in the body: [[slug]], [[concepts/slug]], [[slug|text]],
//      [[slug#heading]], or [[alias]] for any of the page's `aliases`
//      (case-insensitive; image embeds `![[...]]` do not count);
//   2. names it as a typed `relationships:` target in frontmatter; or,
//      for entities only,
//   3. lists it in `author:`, or
//   4. names it as the leading part of `publisher:` (before " — ", "(", ","
//      or ";"), e.g. "Microsoft — WorkLab podcast" cites Microsoft.
//
// Never edits files. Fixing a mismatch is an in-session edit. Run from repo root:
//   node scripts/lint-source-count.mjs           # mismatches + summary
//   node scripts/lint-source-count.mjs --json    # every page, machine-readable
//
// Exits 1 when any page disagrees, 0 otherwise. session-start.mjs imports
// checkSourceCounts() to surface the mismatch count in the session snapshot.

import { readdir, readFile } from "node:fs/promises"
import { join, dirname, basename } from "node:path"
import { fileURLToPath } from "node:url"
import matter from "gray-matter"

const REPO_ROOT = join(dirname(fileURLToPath(import.meta.url)), "..")
const WIKI_DIR = join(REPO_ROOT, "wiki")

const norm = (s) => String(s).trim().toLowerCase().replace(/\s+/g, "-")
const WIKILINK = /!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]/g

async function readPages(subdir) {
  const dir = join(WIKI_DIR, subdir)
  const names = (await readdir(dir)).filter((f) => f.endsWith(".md") && !f.startsWith("."))
  return Promise.all(
    names.map(async (f) => {
      const { data, content } = matter(await readFile(join(dir, f), "utf8"))
      return { slug: basename(f, ".md"), data, content }
    }),
  )
}

function citedKeys({ data, content }) {
  const links = new Set()
  for (const m of content.matchAll(WIKILINK)) {
    if (m[0].startsWith("!")) continue
    links.add(norm(m[1].replace(/^(\.\.\/)*(concepts|entities)\//, "").replace(/\.md$/, "")))
  }
  for (const r of data.relationships || []) if (r && r.target) links.add(norm(r.target))
  const credits = new Set([].concat(data.author || []).map(norm))
  if (typeof data.publisher === "string") {
    const lead = data.publisher.replace(/\[\[([^\]|]+)(\|[^\]]*)?\]\]/g, "$1").split(/ — |\(|,|;/)[0]
    if (lead.trim()) credits.add(norm(lead))
  }
  return { links, credits }
}

export async function checkSourceCounts() {
  const sources = (await readPages("sources")).map(citedKeys)
  const rows = []
  for (const kind of ["concepts", "entities"]) {
    for (const page of await readPages(kind)) {
      const keys = [page.slug, ...(page.data.aliases || [])].map(norm)
      const counted = sources.filter(
        (s) => keys.some((k) => s.links.has(k) || (kind === "entities" && s.credits.has(k))),
      ).length
      const stored = typeof page.data.source_count === "number" ? page.data.source_count : null
      rows.push({ kind, slug: page.slug, stored, counted })
    }
  }
  const mismatches = rows.filter((r) => r.stored !== r.counted)
  return { rows, mismatches }
}

const isMain = process.argv[1] && import.meta.url === `file://${process.argv[1]}`
if (isMain) {
  const { rows, mismatches } = await checkSourceCounts()

  if (process.argv.includes("--json")) {
    console.log(JSON.stringify(rows, null, 2))
  } else {
    console.log(`source_count disagrees with the citing sources — ${mismatches.length}`)
    console.log("------------------------")
    if (mismatches.length === 0) console.log("  (none — every stored count matches)")
    const byGap = [...mismatches].sort((a, b) => Math.abs(b.counted - (b.stored ?? 0)) - Math.abs(a.counted - (a.stored ?? 0)))
    for (const r of byGap) {
      const gap = r.stored === null ? "missing" : `${r.counted - r.stored > 0 ? "+" : ""}${r.counted - r.stored}`
      console.log(`  ${`${r.kind}/${r.slug}`.padEnd(48)} stored ${String(r.stored ?? "—").padStart(4)}  counted ${String(r.counted).padStart(4)}  ${gap}`)
    }
    console.log()
    console.log("Summary")
    console.log("------------------------")
    for (const kind of ["concepts", "entities"]) {
      const all = rows.filter((r) => r.kind === kind)
      const off = mismatches.filter((r) => r.kind === kind)
      const low = off.filter((r) => r.stored !== null && r.stored < r.counted).length
      console.log(`  ${kind.padEnd(9)} ${all.length} pages, ${all.length - off.length} match, ${low} stored too low, ${off.length - low} stored too high or missing`)
    }
  }

  process.exit(mismatches.length > 0 ? 1 : 0)
}
