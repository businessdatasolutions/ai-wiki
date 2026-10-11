// Shared qmd client for wiki-query.mjs and wiki-retrieve.mjs.
//
// Why this exists: every `qmd query` CLI call is a fresh process that loads ~2.3 GB
// of GGUF models (1.7B query-expansion + 0.6B reranker + 300M embedder). Five
// parallel callers (four drafting agents + the orchestrator's neighbour scan)
// exceeded this machine's 8 GB RAM and crashed the session (2026-10-11).
//
// Strategy, in order:
//   1. Daemon (default). One long-lived `qmd mcp --http --daemon` on localhost:8181,
//      started lazily on first use and left running (`npm run qmd:stop` ends it).
//      Models load once and are shared by every caller. The HTTP /query endpoint
//      takes typed lex/vec sub-queries, so the 1.7B expansion model never loads.
//      Rerank is OFF by default: on raw lex+vec queries the 0.6B reranker flattened
//      scores to ~0.63 and dropped the obvious hit (the agent-harness concept page
//      for "agent harness"), while plain RRF ranked it 3rd (tested 2026-10-11).
//      With rerank off only the 300M embedder loads.
//   2. CLI fallback (daemon unavailable, or `expand: true`). The original
//      `qmd query --json` route, serialised through a global mutex so at most one
//      model set is ever in RAM.
//
// Returns qmd's JSON shape either way: { results: [{ file, title, score, snippet, ... }] }.

import { spawn, spawnSync } from 'node:child_process';
import { mkdirSync, rmdirSync, statSync } from 'node:fs';
import { homedir } from 'node:os';
import { join } from 'node:path';

const PORT = Number(process.env.QMD_PORT || 8181);
const BASE = `http://localhost:${PORT}`;
const COLLECTION = 'ai-wiki';
const CACHE = join(homedir(), '.cache', 'qmd');
const START_LOCK = join(CACHE, '.daemon-start.lock');
const CLI_LOCK = join(CACHE, '.cli.lock');
const STALE_MS = 5 * 60 * 1000;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function healthy() {
  try {
    const res = await fetch(`${BASE}/health`, { signal: AbortSignal.timeout(1500) });
    return res.ok;
  } catch {
    return false;
  }
}

// mkdir is atomic, so it doubles as a cross-process mutex. A lock older than
// STALE_MS is assumed abandoned by a crashed holder and taken over.
async function withLock(dir, timeoutMs, fn) {
  const deadline = Date.now() + timeoutMs;
  for (;;) {
    try {
      mkdirSync(dir);
      break;
    } catch (e) {
      if (e.code !== 'EEXIST') throw e;
      try {
        if (Date.now() - statSync(dir).mtimeMs > STALE_MS) rmdirSync(dir);
      } catch {}
      if (Date.now() > deadline) throw new Error(`timed out waiting for lock ${dir}`);
      await sleep(250);
    }
  }
  try {
    return await fn();
  } finally {
    try {
      rmdirSync(dir);
    } catch {}
  }
}

async function ensureDaemon() {
  if (await healthy()) return true;
  return withLock(START_LOCK, 60_000, async () => {
    if (await healthy()) return true; // another caller started it while we waited
    console.error(`qmd: starting shared daemon on ${BASE} (stop with: npm run qmd:stop)`);
    const child = spawn('npx', ['--yes', '@tobilu/qmd', 'mcp', '--http', '--daemon', '--port', String(PORT)], {
      detached: true,
      stdio: 'ignore',
    });
    child.unref();
    for (let i = 0; i < 120; i++) {
      await sleep(250);
      if (await healthy()) return true;
    }
    return false;
  });
}

async function viaDaemon(query, { n, rerank }) {
  const res = await fetch(`${BASE}/query`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      // lex is always included: vec alone misreads ambiguous paraphrases (CLAUDE.md §Search).
      searches: [
        { type: 'lex', query },
        { type: 'vec', query },
      ],
      collections: [COLLECTION],
      limit: n,
      rerank,
    }),
  });
  if (!res.ok) throw new Error(`qmd daemon /query returned HTTP ${res.status}: ${await res.text()}`);
  return res.json();
}

async function viaCli(query, { n, rerank, cwd }) {
  // -c fixes a pre-existing leak: without it the CLI also returned other collections (cmr-wiki).
  const args = ['--yes', '@tobilu/qmd', 'query', query, '--json', '-n', String(n), '-c', COLLECTION];
  if (!rerank) args.push('--no-rerank');
  const out = await withLock(CLI_LOCK, 10 * 60_000, async () =>
    spawnSync('npx', args, { cwd, encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 }),
  );
  if (out.status !== 0) throw new Error(`qmd CLI failed:\n${out.stderr || out.stdout}`);
  return JSON.parse(out.stdout);
}

// opts: n (result count), rerank (default false; see header), expand (force CLI with LLM query
// expansion), cwd (for the CLI fallback).
export async function qmdQuery(query, { n = 8, rerank = false, expand = false, cwd } = {}) {
  if (!expand) {
    if (await ensureDaemon()) return viaDaemon(query, { n, rerank });
    console.error('qmd: daemon unavailable, falling back to serialised CLI query');
  }
  return viaCli(query, { n, rerank, cwd });
}
