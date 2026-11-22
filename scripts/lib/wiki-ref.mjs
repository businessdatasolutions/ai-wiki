// Parse a qmd hit path or a graph slug into a wiki page reference.
//
// Two naming forms reach the retrieval scripts for the same page:
//   qmd:    "qmd://ai-wiki/entities/HBS%20AI%20Institute.md"  (URL-encoded file path)
//   graph:  "entities/HBS-AI-Institute"                        (graph-export.mjs dasherises spaces)
// The file on disk is "wiki/entities/HBS AI Institute.md". parseWikiRef maps both forms to one key
// (`fullSlug`, the graph form) and to the real file (`diskPath`).
import { existsSync, readdirSync } from 'node:fs';
import { join, resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const REPO_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..', '..');
const TYPE_DIRS = 'concepts|entities|syntheses|sources|threads';
const PATH_RE = new RegExp(`(?:^|/)(?:wiki/)?(${TYPE_DIRS})/([^/]+?)(?:\\.md)?$`);

const dasherise = (s) => s.replace(/\s+/g, '-');

function decode(raw) {
  try {
    return decodeURIComponent(raw);
  } catch {
    return raw; // a stray "%" is part of the name, not an escape
  }
}

// dir -> Map(dasherised stem -> absolute path), built once per folder on first miss.
const stemIndex = new Map();
function findOnDisk(dir, name) {
  const direct = join(REPO_ROOT, 'wiki', dir, `${name}.md`);
  if (existsSync(direct)) return direct;
  if (!stemIndex.has(dir)) {
    const index = new Map();
    const folder = join(REPO_ROOT, 'wiki', dir);
    for (const f of existsSync(folder) ? readdirSync(folder) : []) {
      if (f.endsWith('.md')) index.set(dasherise(f.slice(0, -3)), join(folder, f));
    }
    stemIndex.set(dir, index);
  }
  return stemIndex.get(dir).get(dasherise(name)) ?? direct;
}

// Returns { dir, name, slug, fullSlug, diskPath } or null when the path is not a wiki page.
//   name      the page name as on disk when it exists ("HBS AI Institute")
//   slug      the graph-form name ("HBS-AI-Institute"); bump-accessed.mjs resolves either form
//   fullSlug  "<dir>/<slug>", the key shared with wiki/.graph.json
export function parseWikiRef(raw) {
  if (!raw) return null;
  const m = decode(raw).match(PATH_RE);
  if (!m) return null;
  const dir = m[1];
  const diskPath = findOnDisk(dir, m[2]);
  const name = existsSync(diskPath) ? diskPath.split('/').pop().slice(0, -3) : m[2];
  const slug = dasherise(name);
  return { dir, name, slug, fullSlug: `${dir}/${slug}`, diskPath };
}
