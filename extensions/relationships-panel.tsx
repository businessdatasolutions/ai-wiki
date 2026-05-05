import {
  QuartzComponent,
  QuartzComponentConstructor,
  QuartzComponentProps,
} from "../quartz/components/types"
import { resolveRelative } from "../quartz/util/path"
import { classNames } from "../quartz/util/lang"

interface Options {
  hideWhenEmpty: boolean
}

const defaultOptions: Options = { hideWhenEmpty: true }

interface Relationship {
  type: string
  target: string
  via?: string
  confidence?: number
}

// Display labels for the closed v0.3 vocabulary. Unknown types fall through
// to their raw string.
const RELATIONSHIP_LABELS: Record<string, string> = {
  supports: "Supports",
  contradicts: "Contradicts",
  caused: "Caused",
  fixed: "Fixed",
  supersedes: "Supersedes",
  uses: "Uses",
  "depends-on": "Depends on",
  "part-of": "Part of",
  "instance-of": "Instance of",
  "authored-by": "Authored by",
  "published-by": "Published by",
  employs: "Employs",
}

// Order in which relationship-type groups appear, when present. Types not
// listed appear afterward in insertion order.
const TYPE_ORDER = [
  "instance-of",
  "part-of",
  "supports",
  "contradicts",
  "caused",
  "supersedes",
  "uses",
  "depends-on",
  "fixed",
  "authored-by",
  "published-by",
  "employs",
]

// Renders a typed-relationships panel in the right sidebar, reading the
// page's `relationships:` frontmatter (v0.3 schema). Targets are matched
// against allFiles by slug basename, so `target: Erik-Brynjolfsson` resolves
// to the entity page at `entities/Erik-Brynjolfsson`. Hides when no
// relationships are defined; an explicit "broken-relationship" span renders
// when a target slug doesn't match any file in the wiki (useful as a lint
// signal during migration).
export default ((opts?: Partial<Options>) => {
  const options: Options = { ...defaultOptions, ...opts }

  const RelationshipsPanel: QuartzComponent = ({
    fileData,
    allFiles,
    displayClass,
  }: QuartzComponentProps) => {
    const rawRels = fileData.frontmatter?.relationships
    const rels: Relationship[] = Array.isArray(rawRels)
      ? (rawRels as Relationship[]).filter(
          (r) => r && typeof r.type === "string" && typeof r.target === "string",
        )
      : []

    if (rels.length === 0) {
      if (options.hideWhenEmpty) return null
    }

    // Group by type, preserving insertion order within each type
    const byType = new Map<string, Relationship[]>()
    for (const rel of rels) {
      const list = byType.get(rel.type) ?? []
      list.push(rel)
      byType.set(rel.type, list)
    }

    // Sort types by TYPE_ORDER, with unknown types appended in insertion order
    const orderedTypes = [
      ...TYPE_ORDER.filter((t) => byType.has(t)),
      ...Array.from(byType.keys()).filter((t) => !TYPE_ORDER.includes(t)),
    ]

    if (orderedTypes.length === 0) {
      if (options.hideWhenEmpty) return null
    }

    // Match a relationship target (e.g. "Erik-Brynjolfsson" or
    // "ai-employment-effects") against a file in allFiles. Try exact slug,
    // then slug basename match.
    const findTargetFile = (target: string) => {
      const normalized = target.replace(/\s+/g, "-")
      return allFiles.find((f) => {
        if (!f.slug) return false
        if (f.slug === normalized) return true
        const basename = f.slug.split("/").pop() ?? f.slug
        return basename === normalized
      })
    }

    return (
      <div class={classNames(displayClass, "relationships-panel")}>
        <h3>Relationships</h3>
        <div class="relationships-body">
          {orderedTypes.map((type) => {
            const list = byType.get(type) ?? []
            return (
              <div class="relationships-group">
                <h4>{RELATIONSHIP_LABELS[type] ?? type}</h4>
                <ul>
                  {list.map((rel) => {
                    const targetFile = findTargetFile(rel.target)
                    const targetTitle =
                      (targetFile?.frontmatter?.title as string | undefined) ?? rel.target
                    const href =
                      targetFile?.slug && fileData.slug
                        ? resolveRelative(fileData.slug, targetFile.slug)
                        : null
                    return (
                      <li>
                        {href ? (
                          <a href={href} class="internal">
                            {targetTitle}
                          </a>
                        ) : (
                          <span class="broken-relationship">{rel.target}</span>
                        )}
                        {rel.via ? (
                          <span class="relationship-via">
                            {" — "}
                            <em>{rel.via}</em>
                          </span>
                        ) : null}
                      </li>
                    )
                  })}
                </ul>
              </div>
            )
          })}
        </div>
      </div>
    )
  }

  // Scrollable body so a page with many relationships doesn't push the rest of
  // the right sidebar (Backlinks, etc.) off-screen. Uses viewport-relative
  // max-height (40vh) rather than `calc(100% - …)` because the panel's parent
  // in Quartz's flex sidebar doesn't always have a bounded height — a percent
  // max-height resolves to auto in that case and the body never scrolls.
  RelationshipsPanel.css = `
.relationships-panel > h3 {
  font-size: 1rem;
  margin: 0 0 0.5rem;
}
.relationships-panel > .relationships-body {
  max-height: 40vh;
  overflow-y: auto;
  overscroll-behavior: contain;
}
.relationships-panel .relationships-group + .relationships-group {
  margin-top: 0.5rem;
}
.relationships-panel .relationships-group > h4 {
  font-size: 0.7rem;
  margin: 0 0 0.25rem;
  opacity: 0.75;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.relationships-panel .relationships-group > ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.relationships-panel .relationships-group > ul > li {
  margin: 0.2rem 0;
  line-height: 1.35;
}
.relationships-panel .relationship-via {
  opacity: 0.7;
  font-size: 0.85em;
}
.relationships-panel .broken-relationship {
  opacity: 0.5;
  font-style: italic;
}
`

  return RelationshipsPanel
}) satisfies QuartzComponentConstructor<Partial<Options>>
