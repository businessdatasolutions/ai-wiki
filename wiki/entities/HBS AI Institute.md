---
type: entity
kind: organization
aliases: ["HBS AI Institute", "Harvard Business School AI Institute", "HBS AI Content & Learning", "HBS and HBS AI Affiliate Research", "Frontier Firm AI Initiative"]
tags: [harvard-business-school, research-institute, frontier-firm, microsoft-partner, research-summaries]
website: "https://aiinstitute.hbs.edu"
confidence: 0.75
last_confirmed: "2026-10-25"
accessed_at: "2026-10-25"
source_count: 5
relationships:
  - type: published-by
    target: 2026-09-03-hbs-ai-institute-think-youre-a-good-leader-try-leading-an-ai-team
    via: "research summary of Weidmann, Xu & Deming's AI leadership test (3 Sep 2026)"
  - type: published-by
    target: 2025-08-05-hbs-ai-institute-mastering-change-resilience-key-to-ai-driven-success
    via: "research summary of Lakhani et al.'s HBR article on change resilience (5 Aug 2025)"
  - type: published-by
    target: 2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about
    via: "institutional page of the Frontier Firm AI Initiative run with Microsoft (captured 15 Oct 2026)"
---

# HBS AI Institute

**The Harvard Business School AI Institute**, a research institute at HBS co-founded and chaired by [[Karim Lakhani]], with Jen Stave as executive director. Its site publishes short research summaries of work by HBS faculty and associates, bylined **HBS AI Content & Learning**. With [[Microsoft]] it runs the **Frontier Firm AI Initiative**, in which member companies run AI experiments with Harvard and Microsoft researchers, starting with sales, IT and finance, and attend C-suite programmes. [[Raffaella Sadun]] is a research leader in the initiative.

The wiki's existing Harvard pages call Lakhani's institute the **Digital Data Design Institute at Harvard (D^3)**. Staff photos on the AI Institute's site are still filed under that name, and Lakhani's bio now calls him co-founder and faculty chair of the HBS AI Institute. That suggests the institute was renamed, but no source in the corpus says so. Treat the identification as likely, not confirmed. One more data point (added 2026-10-25): in December 2025, [[2025-12-16-diasio-wood-worklab-agentic-ai-corporate-ladder|WorkLab]] introduced the same initiative as *"the Digital Data Design Institute at Harvard Frontier Firm AI Initiative, hosted by Harvard Business School in collaboration with Microsoft."* So the initiative was attributed to D^3 in December 2025 and to the HBS AI Institute in October 2026, which fits a rename between the two dates. Neither source states one.

## Wiki contributions

- [[2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about]] — the Frontier Firm definition and four early insights from a forthcoming case: structured experimentation, the managerial problems of running it, the Skill–Will 2×2, and agents as a sharpener of winners and losers.
- [[2026-09-03-hbs-ai-institute-think-youre-a-good-leader-try-leading-an-ai-team]] — summary of [[2025-08-05-weidmann-xu-deming-measuring-leadership-skills-ai-agents|Weidmann, Xu & Deming]], adding the proposal that AI teams become a leadership practice environment.
- [[2025-08-05-hbs-ai-institute-mastering-change-resilience-key-to-ai-driven-success]] — summary of Lakhani, Stave, Ng & Martines's HBR article: sensing, rewiring, lock-in; Learn–Do–Imagine–Act–Care.

## Why it is an entity (promotion note)

Its byline appears in `author:` on two source pages in the same ingest, and it hosts the initiative behind a third, so the second-source promotion rule is met on creation.

## Reading its sources

The institute summarises work by its own faculty, associates and leadership, and runs the Frontier Firm initiative with a vendor. Its pages are accurate digests but not independent. Cite the underlying paper or article where the wiki holds it.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```

## Cited from Microsoft's side (added 2026-10-17)

[[2026-07-27-george-wood-worklab-future-of-work-has-no-org-chart|Katy George (Microsoft) on WorkLab, July 2026]] refers to *"this fabulous collaboration with Harvard Business School around the frontier firm research initiatives"* and says HBS *"did a case example of our initial rollout of Copilot into our own Salesforce,"* a rollout that failed as a product launch before it was redesigned. Whether that is the forthcoming Bojinov, Sadun and Zhang case summarised on the [[2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about|initiative's About page]] is not stated in either source.

## A member firm on its own transformation (added 2026-10-25)

[[2025-12-16-diasio-wood-worklab-agentic-ai-corporate-ladder|Diasio on WorkLab (Dec 2025)]] names [[EY]] as a member of the initiative's inaugural class. EY's Global Consulting AI Leader describes its route to becoming a Frontier Firm: more than $1 billion invested in a year, a Client Zero programme, a curriculum for all staff, and a blueprint for AI-native functions. This is a member's own account, on the co-runner's podcast.
