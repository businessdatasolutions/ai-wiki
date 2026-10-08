import { QuartzTransformerPlugin } from "../quartz/plugins/types"
import { Root as HtmlRoot, Element } from "hast"
import { visit } from "unist-util-visit"
import fs from "fs"
import path from "path"

// Marks catalogue entries whose page contains images with a small picture
// icon, so a reader scanning the landing page can tell which sources carry
// visual content (published video stills, diagrams).
//
// index.md is hand-maintained plain wikilinks, so nothing on the index page
// knows what the linked pages contain. This plugin scans the page folders for
// image embeds at build time and, on the `index` page only, appends an inline
// SVG after every link whose target is one of those pages. Source files stay
// clean; new ingests with stills get the icon automatically.
//
// Registered AFTER Plugin.Description() so the icon markup never reaches
// og:description / meta description.
const SCAN_DIRS = ["wiki/sources", "wiki/syntheses", "wiki/concepts"]
const IMAGE_EXT = "(?:png|jpe?g|webp|gif|svg|avif)"
const IMAGE_EMBED = new RegExp(
  `!\\[\\[[^\\]]+?\\.${IMAGE_EXT}(?:\\|[^\\]]*)?\\]\\]|!\\[[^\\]]*\\]\\([^)]+?\\.${IMAGE_EXT}[^)]*\\)`,
  "i",
)

function pagesWithImages(): Set<string> {
  const slugs = new Set<string>()
  for (const dir of SCAN_DIRS) {
    const abs = path.resolve(dir)
    if (!fs.existsSync(abs)) continue
    for (const name of fs.readdirSync(abs)) {
      if (!name.endsWith(".md")) continue
      const raw = fs.readFileSync(path.join(abs, name), "utf8")
      // Skip frontmatter so a `stills:` path is not mistaken for an embed.
      const body = raw.replace(/^---\n[\s\S]*?\n---\n/, "")
      if (IMAGE_EMBED.test(body)) slugs.add(name.replace(/\.md$/, ""))
    }
  }
  return slugs
}

const ICON: Element = {
  type: "element",
  tagName: "svg",
  properties: {
    className: ["image-icon"],
    viewBox: "0 0 16 16",
    width: 14,
    height: 14,
    fill: "none",
    stroke: "currentColor",
    strokeWidth: 1.8,
    strokeLinecap: "round",
    strokeLinejoin: "round",
    role: "img",
    ariaLabel: "Contains images",
  },
  children: [
    { type: "element", tagName: "title", properties: {}, children: [{ type: "text", value: "Contains images" }] },
    { type: "element", tagName: "rect", properties: { x: 1.5, y: 2.5, width: 13, height: 11, rx: 1.5 }, children: [] },
    { type: "element", tagName: "circle", properties: { cx: 5.5, cy: 6, r: 1.2 }, children: [] },
    { type: "element", tagName: "path", properties: { d: "M1.8 12 L6 8.2 L9 11 L11 9.2 L14.2 12" }, children: [] },
  ],
}

export const InjectImageIcon: QuartzTransformerPlugin = () => ({
  name: "InjectImageIcon",
  htmlPlugins() {
    return [
      () => (tree: HtmlRoot, file) => {
        if (file.data.slug !== "index") return
        const withImages = pagesWithImages()

        // Only a bullet's own entry link (its first anchor) is marked; links
        // to other sources inside the bullet's prose are cross-references.
        visit(tree, "element", (li: Element) => {
          if (li.tagName !== "li") return
          let done = false
          visit(li, "element", (node: Element, index, parent) => {
            if (done || node.tagName !== "a" || parent == null || index == null) return
            done = true
            const href = node.properties?.href
            if (typeof href !== "string" || /^[a-z]+:/i.test(href)) return
            const slug = decodeURIComponent(href.split("#")[0]).split("/").pop() ?? ""
            if (!withImages.has(slug)) return
            parent.children.splice(index + 1, 0, { type: "text", value: " " }, structuredClone(ICON))
          })
        })
      },
    ]
  },
})
