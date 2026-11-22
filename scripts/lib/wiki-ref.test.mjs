// Tests for parseWikiRef: turning a qmd hit path or a graph slug into a wiki page reference.
// Run: node --test scripts/lib/wiki-ref.test.mjs
//
// The fixtures are real pages in this repo, so the tests also prove the files resolve on disk.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { existsSync } from 'node:fs';
import { basename } from 'node:path';
import { parseWikiRef } from './wiki-ref.mjs';

// Break caught: qmd returns paths URL-encoded; without decoding, the slug is "HBS%20AI%20Institute"
// and bump-accessed.mjs reports "page not found" (seen 2026-11-22).
test('decodes a URL-encoded qmd path to the page name on disk', () => {
  const ref = parseWikiRef('qmd://ai-wiki/entities/HBS%20AI%20Institute.md');
  assert.equal(ref.name, 'HBS AI Institute');
  assert.equal(ref.dir, 'entities');
});

// Break caught: wiki-retrieve keys qmd hits and graph nodes in one map. graph-export.mjs writes
// "entities/HBS-AI-Institute"; if the qmd hit is keyed any other way, the same page becomes two
// candidates and its graph edges never attach to the qmd seed.
test('keys a qmd hit and a graph node for the same page identically', () => {
  assert.equal(parseWikiRef('qmd://ai-wiki/entities/HBS%20AI%20Institute.md').fullSlug, 'entities/HBS-AI-Institute');
  assert.equal(parseWikiRef('entities/HBS-AI-Institute').fullSlug, 'entities/HBS-AI-Institute');
});

// Break caught: diskPath built from the encoded or dasherised name points at a file that does not
// exist, so effective_confidence silently falls back to "no frontmatter".
test('resolves the real file for both the qmd form and the graph form', () => {
  for (const raw of ['qmd://ai-wiki/entities/HBS%20AI%20Institute.md', 'entities/HBS-AI-Institute']) {
    const ref = parseWikiRef(raw);
    assert.equal(basename(ref.diskPath), 'HBS AI Institute.md', raw);
    assert.ok(existsSync(ref.diskPath), raw);
  }
});

// Break caught: turning every dash back into a space finds "Irving Wladawsky Berger.md",
// which does not exist; the real file keeps its hyphen.
test('resolves a graph slug whose page name contains both a space and a hyphen', () => {
  const ref = parseWikiRef('entities/Irving-Wladawsky-Berger');
  assert.equal(basename(ref.diskPath), 'Irving Wladawsky-Berger.md');
  assert.ok(existsSync(ref.diskPath));
});

// Break caught: a regression in the common case, plain kebab-case pages.
test('leaves an ordinary concept path unchanged', () => {
  const ref = parseWikiRef('qmd://ai-wiki/concepts/lean-4-0.md');
  assert.equal(ref.fullSlug, 'concepts/lean-4-0');
  assert.equal(ref.slug, 'lean-4-0');
  assert.ok(existsSync(ref.diskPath));
});

// Break caught: a stray "%" makes decodeURIComponent throw and would abort the whole query.
test('does not throw on a path with a malformed percent escape', () => {
  const ref = parseWikiRef('qmd://ai-wiki/concepts/100%-sure.md');
  assert.equal(ref.slug, '100%-sure');
});

test('returns null for a path outside the wiki page folders', () => {
  assert.equal(parseWikiRef('qmd://ai-wiki/index.md'), null);
  assert.equal(parseWikiRef(''), null);
});
