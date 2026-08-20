---
type: entity
kind: product
aliases: ["Claude Code", "Claude Cowork", "Claude Co-work"]
tags: [claude-code, anthropic, coding-agent, agent-harness, agentic-engineering, cli, routines, goal-loop, hooks, subagents, agents-md]
affiliation: "Anthropic"
confidence: 0.9
last_confirmed: "2026-08-20"
accessed_at: "2026-08-20"
source_count: 7
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

## The first-party mechanical account (He, August 2026)

[[2026-08-19-he-databricks-anthropic-primitives-to-production-agents|Isabella He's meetup talk]] is the corpus's most concrete **vendor-side** description of how Claude Code works under the hood, from someone who works on its internals (compaction, tool-result clearing, the `/init` experience):

- **Tool count and composition.** *"Claude Code has access to about 14 or 15 tools, things like bash, edit, grep, glob. And these are actually tools that you all have at your disposal in your terminal as a developer as well."*
- **The retrieval-architecture choice, stated as a deliberate break with prior art.** *"What a lot of agents did before Claude Code was essentially semantic search over a particular file, which is looking for things like keyword phrasing, and you had to feed it a specific file to edit. But Claude Code instead essentially has the same set of tools that you have access to as a developer… You can run Claude Code on a codebase that is millions or hundreds of millions lines of code."* This is a first-party statement that **developer-grade navigation tools replaced embedding search** in the reference harness — relevant to [[syntheses/is-rag-dead|is-rag-dead]].
- **Model tiering inside the harness.** *"The Claude Code default subagent for the explore mode is a Haiku subagent"*, reporting back to Opus or Sonnet.
- **Claude Code as substrate for non-coding domains.** *"Claude Code could power a customer support agent. It could power an incident response agent"* — the same core primitives (code execution, file system, web search, to-do list) plus domain skills. The SRE demo in the same talk is that claim executed.
- **Auto mode**, offered as a throwaway aside but dated: *"we recently announced an auto mode as well in Claude Code… I haven't seen a permission prompt in a long time."*

Claude Code is also named first among example harnesses by a **competitor's** developer relations in [[2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness|Google Cloud Tech's harness explainer]] — *"so like a Claude Code or an Antigravity or a Codex"* — used there to make the harness/interface decoupling point.

## Appears in this wiki via

- [[2026-08-19-he-databricks-anthropic-primitives-to-production-agents]] — the first-party mechanical account above.
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
