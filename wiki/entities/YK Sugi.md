---
type: entity
kind: person
aliases: ["YK Sugi", "ykdojo", "CS Dojo", "Sugi"]
tags: [yk-sugi, cs-dojo, claude-code, claude-code-tips, intent-driven-development, voice-prompting, draft-pr, community-advocate, agentic-engineering]
affiliation: "Daft; creator of the CS Dojo channel"
role: "Software engineer and educator; author of the claude-code-tips repository (~8,000 stars)"
confidence: 0.7
last_confirmed: "2026-09-16"
accessed_at: "2026-09-16"
source_count: 1
relationships:
  - type: supports
    target: agentic-engineering
    via: "his claude-code-tips repository is a practitioner codification of agentic-engineering discipline — verification, commit selection, CLI fluency — maintained outside any vendor"
---

# YK Sugi

Creator of the **CS Dojo** channel and author of the **`claude-code-tips`** repository (*"over 8,000 stars"* as of July 2026) — one of the most-used community resources for [[Claude Code]], and the corpus's first **independent** practitioner codifier of coding-agent practice, as distinct from vendor documentation.

He enters the wiki through [[2026-07-06-google-cloud-agent-factory-intent-driven-development|The Agent Factory, July 2026]], where he popularises the term **intent-driven development** while declining to defend its novelty: *"there are many different terms for it. But I personally like this term because to me, it's not about the exact prompt… it's more about expressing what your intent is exactly."*

What survives the branding is a set of practitioner heuristics, delivered while building a 3D physics game live by voice:

- **Prompt by voice, tolerate the noise.** *"You might make mistakes… but it doesn't matter as long as you're able to express it"* — and, watching Claude recover from his own transcription errors, *"as long as your intent is clear enough… Claude is able to figure out what I mean."*
- **Ask more questions when you have less context.** *"the rule of thumb is you ask more questions when you have less context"* — he interrogated the agent about physics libraries before committing, then stopped once he had the vocabulary.
- **Draft PRs as an agent-authorship signal.** Ask the agent to open the PR as a draft, review, then mark ready — *"so that people will [know] OK, this PR maybe was created by the agent."* An out-of-band provenance marker built from existing GitHub semantics; see [[agentic-pull-requests]].
- **Colocate repositories** under one parent folder so the agent can cross-reference projects.
- **Learn Git and the `gh` CLI**, because *"it turns out CLI is really, really powerful."*

Taken together the repository is the corpus's first **non-vendor** codification of [[agentic-engineering]] discipline — verification, commit selection, CLI fluency — maintained by a practitioner with no product to sell.

His **tip 38 — *simplify overcomplicated code*** — is the corpus's cleanest practitioner statement of the over-generation problem [[ai-generated-code-quality]] tracks: code-generation models *"have a bias towards writing more code than needed."* The discipline he pairs with it is a commit filter, not a prompt fix:

> *"If you generate 100,000 lines of code, you don't have to commit 100,000 lines of code… Just commit what you think is right."*

And his answer to the craft-and-technical-debt debate is a norm rather than a technique: *"it is a tool… as a painter, instead of using a regular brush, you're using an electric automated brush. So you're responsible for the output."* He splits the regime explicitly — a casual one-off may go unreviewed ([[vibe-coding]]), production code gets a draft PR and a manual or AI review.

**How to cite him.** For **practitioner convention** and for the independent-community view of Claude Code practice. He reports no measurements, and his most quoted claim — saving `$10,000` on a property purchase by having Claude Code compile a realtor list — is a single unverifiable anecdote.

**Promotion note.** Promoted on a single source, 2026-09-16, on the same judgement-call grounds as [[Tilde Thurium]] and [[Lydia Hallie]]: a named presenter carrying quotable, reusable convention. Employer heard as "Daft" in an ASR transcript and recorded with low confidence.

## Appears in this wiki via

- [[2026-07-06-google-cloud-agent-factory-intent-driven-development]]

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "yk-sugi")
SORT file.name ASC
```
