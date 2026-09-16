---
type: entity
kind: product
aliases: ["Claude Code", "Claude Cowork", "Claude Co-work"]
tags: [claude-code, anthropic, coding-agent, agent-harness, agentic-engineering, cli, routines, goal-loop, hooks, subagents, agents-md, auto-mode, permission-classifier, dynamic-workflows, claude-cowork, vertex-ai]
affiliation: "Anthropic"
confidence: 0.9
last_confirmed: "2026-09-16"
accessed_at: "2026-09-16"
source_count: 8
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

## Auto mode and dynamic workflows, explained by the team (July 2026)

[[2026-07-06-google-cloud-agent-factory-intent-driven-development|Lydia Hallie]] — on the Claude Code team, interviewed on Google's own channel — supplies the mechanism behind two features the wiki previously carried as names.

**Auto mode is a classifier, not a preset.** He's throwaway aside above dated the feature; Hallie says what it does. The prior product offered two bad options — ask on everything, which produces what Hallie calls **permission fatigue** (*"after a while you're just like, yeah, go ahead. Whatever"*, and *"[you] won't read them as much anymore"*), or `--dangerously-skip-permissions`, where *"if it's about to delete your root file, there's no going back."* Auto mode

> *"sits in between your denial list and allow list. So auto mode runs a different classifier between all the tool calls."*

It triages each call by danger, reads the session so that an explicitly requested deletion is not treated as dangerous, and — as a side effect of interposition — catches prompt-injection attempts in tool results. The purpose is autonomy: *"this actually enables you to run Claude Code way more autonomously in these longer running sessions."* On Google's Agent Platform it is **off by default**, behind `CLAUDE_CODE_ENABLE_AUTO_MODE`. No calibration data is reported. See [[agent-oversight-and-delegation]].

**Dynamic workflows trades non-determinism for a generated program.** Hallie concedes the defect plainly — ad-hoc subagent spawning *"is very non-deterministic. Sometimes it might spin up four subagents, sometimes it might not even use subagents. The other time it uses 10 subagents"* — and describes the fix: Claude Code **writes a JavaScript file** describing the run (*"I didn't type this. This is all Claude"*), with parallel build agents inside sequentially-gated phases (build → integration → review → verify). The file is editable, including **per-subagent model choice**, and saveable as a named command that re-runs identically. Design target: *"hundreds of subagents… for tasks that takes hours or days."* On camera the feature was too slow to demo live. See [[agent-fleet-management]].

**Cowork is the same runtime.** Asked about the non-coding expansion, Hallie dates it to December 2025 — Anthropic staff using Claude Code for marketing and data-science work — and states the architecture: *"we wanted to build a better harness for these types of tasks… Cowork came out in a week… It still uses the Claude Code runtime underneath, so it can still do coding… but we just have better connectors and better system prompts in Cowork."* This confirms the alias at the top of this page as an architectural fact rather than a branding one, and corroborates [[2026-08-31-blum-how-i-ai-claude-cowork-pm-system|Blum's]] *"it's not Cowork in itself."*

**Distribution.** The episode demonstrates Claude Code running on **Google Cloud Vertex AI**, set up either by hand (`gcloud`, Vertex AI API, environment variables) or through a built-in `/setup-vertex` wizard that enumerates the available models and pins a working model and context window. Anthropic's coding agent shipping as a first-class citizen inside a competitor's platform, demonstrated on that competitor's channel.

Claude Code is also named first among example harnesses by a **competitor's** developer relations in [[2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness|Google Cloud Tech's harness explainer]] — *"so like a Claude Code or an Antigravity or a Codex"* — used there to make the harness/interface decoupling point.

## Appears in this wiki via

- [[2026-08-19-he-databricks-anthropic-primitives-to-production-agents]] — the first-party mechanical account above.
- [[2026-07-06-google-cloud-agent-factory-intent-driven-development]] — auto mode, dynamic workflows, Cowork's origin, Vertex AI distribution.
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
