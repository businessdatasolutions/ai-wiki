---
type: entity
kind: product
aliases: ["Claude Code", "Claude Cowork", "Claude Co-work"]
tags: [claude-code, anthropic, coding-agent, agent-harness, agentic-engineering, cli, routines, goal-loop, hooks, subagents, agents-md]
affiliation: "Anthropic"
confidence: 0.9
last_confirmed: "2026-06-22"
accessed_at: "2026-06-22"
source_count: 6
relationships:
  - type: part-of
    target: Anthropic
    via: "Anthropic's coding-agent product / CLI"
  - type: instance-of
    target: agent-harness
    via: "a productised agent harness — the reference coding agent practitioners benchmark other harnesses against"
---

# Claude Code

**[[Anthropic]]'s coding agent** — a terminal/CLI-first agent (with a desktop "Claude Cowork" surface) that has become, across the wiki's 2026 sources, the **reference [[agent-harness|harness]] practitioners benchmark other tools against**. It is mentioned in ~45 wiki sources and is the named instantiation behind much of the [[agentic-engineering]] and [[agent-harness]] literature: [[2026-05-15-osmani-agent-harness-engineering|Osmani]] names it in the convergence observation (*top coding agents — Claude Code, Cursor, Codex, Aider, Cline — look more like each other than their underlying models do*); [[2026-06-19-chou-yc-lightcone-40-year-old-solo-founder|Chou]] cites it as the model of a purpose-built harness (*"Anthropic did it wonderfully for Claude Code"*).

Its harness primitives recur throughout the wiki: **AGENTS.md**-style instruction files, **hooks**, **subagents**, **skills**, and — per [[2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex|Vo's How I AI loops explainer]] — **"routines"** (scheduled loops) and the **`/goal`** primitive (a goal loop: run against a measurable outcome until validated or blocked), shipped at parity with [[OpenAI]] Codex's "automations."

## Appears in this wiki via

- [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack]] — dedicated how-to: making Claude Code an AI engineering team.
- [[2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex]] — routines + `/goal` loop primitive; live build of a daily aging-PR review routine.
- [[2026-05-15-osmani-agent-harness-engineering]] — named in the cross-agent convergence observation.
- [[2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook]], [[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering]], [[2026-04-11-nodus-labs-fix-karpathys-llm-wiki-knowledge-graph-infranodus]] — referenced as a candidate coding-agent / harness tool.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "claude-code")
SORT file.name ASC
```

## Open questions

- `source_count` here counts inbound wikilinks; ~45 source pages mention Claude Code in prose without linking. Worth a future lint pass to convert prominent prose mentions to wikilinks now that the page exists.
- **Codex** ([[OpenAI]]'s coding agent) is the recurring sibling product and is referenced as a `[[Codex]]` wikilink without a page — a parallel promotion candidate if a second substantive source lands.
