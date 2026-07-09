---
type: source
kind: article
title: "The Code Agent Orchestra - what makes multi-agent coding work"
author: ["Addy Osmani"]
publisher: "AddyOsmani.com"
url: "https://addyosmani.com/blog/code-agent-orchestra/"
date_published: 2026-03-26
date_ingested: 2026-07-09
length: "~36-page PDF print, full article (write-up of an O'Reilly AI CodeCon talk)"
raw: "../../raw/articles/code-agent-orchestra-what-makes-multi-agent-coding-work.md"
tags: [addy-osmani, subagents, agent-teams, orchestration, conductor-to-orchestrator, ralph-loop, factory-model, agents-md, quality-gates, plan-approval, hooks, ai-codecon, claude-code]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
  - digital-seizing/strategic-agility
  - digital-seizing/balancing-digital-portfolios
relationships:
  - type: supports
    target: 2026-03-12-oreilly-steve-yegge-wants-you-to-stop-looking-at-your-code
    via: "Explicitly builds on Yegge's eight-levels framework ('this talk covered levels 5 through 8'), delivered at the same AI Codecon event Yegge's interview promotes 14 days earlier."
    confidence: 0.9
  - type: supports
    target: 2026-05-15-osmani-agent-harness-engineering
    via: "Same author, same discipline, chronologically earlier (26 Mar vs 15 May) — this article supplies the concrete multi-agent operational patterns (subagents, Agent Teams, 3-tier orchestration, factory model) that the later, more definitional Agent Harness Engineering article assumes as background."
    confidence: 0.85
  - type: supports
    target: 2026-06-19-lopopolo-ai-native-devcon-harness-engineering
    via: "Both name AGENTS.md-as-compounding-memory and quality-gate discipline (plan approval / hooks / review personas) as load-bearing harness components, converging independently on the same architecture from different practitioner vantages (Google/Chrome vs OpenAI/Codex)."
    confidence: 0.75
---

# The Code Agent Orchestra - what makes multi-agent coding work

> I spoke about orchestrating coding agents at O'Reilly AI CodeCon today. The talk covered the landscape of patterns for coordinating AI coding agents in real-world software workflows — from spawning your first subagent to running parallel agent teams with quality gates that keep everything trustworthy.

## TL;DR

Addy Osmani's write-up of his O'Reilly AI CodeCon talk (26 March 2026), delivered the same day Tim O'Reilly's Yegge interview promoted it. Explicitly picks up Yegge's eight-levels framework at **levels 5-8** and operationalizes it into concrete patterns. Eight load-bearing contributions:

1. **Conductor → orchestrator.** The shift from pair-programming-with-one-agent (synchronous, your context window is the ceiling) to managing an ensemble of asynchronous agents, each with its own context window, while you plan and check in. Requires different skills: clear specs, work decomposition, output verification — not writing code yourself.
2. **The single-agent ceiling: three walls.** Context overload (large codebases overwhelm one context window), no specialization (a jack-of-all-trades agent writes worse code than a focused one), no coordination (spawned helpers can't communicate or share a task list).
3. **Pattern 1 — Subagents.** The Task tool spawns focused child agents with specific briefs and file ownership; the parent manages the dependency graph manually. Concrete worked example (a bookmarks-manager build) shows two independent subagents running in parallel and a third waiting on both. Pro-tip: **hierarchical subagents** — spawn feature leads that spawn their own specialists, mirroring how real engineering orgs delegate through tech-lead layers rather than one person assigning to everyone directly.
4. **Pattern 2 — Agent Teams.** Claude Code's experimental feature (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) adds what subagents lack: a shared task list with dependency tracking, peer-to-peer messaging (teammates message each other directly, not through the lead), and file locking. Three-layer architecture (Team Lead → Shared Task List → Teammates, each an independent Claude Code instance in its own tmux pane). Reliability pro-tips: hard `MAX_ITERATIONS=8` + forced reflection prompt cuts stuck agents; a dedicated `@reviewer` teammate (read-only, lint/test/security-scan only, 1 per 3-4 builders) means the lead only ever sees green-reviewed code.
5. **Pattern 3 — Orchestration at scale, a 3-tier tool landscape.** Tier 1 (in-process subagents/teams, start here) → Tier 2 (local orchestrators: Conductor, Vibe Kanban, Gastown, Claude Squad, Antigravity — 3-10 agents, dashboards + diff review) → Tier 3 (cloud async: Claude Code Web, Copilot Coding Agent, Jules, Codex Web — assign and walk away). Most developers in 2026 use all three tiers for different purposes.
6. **The bottleneck has shifted from generation to verification.** Agents produce impressive output fast; knowing with confidence whether it's *correct* is the hard part — tests can pass without catching regressions, context limits mean agents miss constraints outside their view, and flaky tests that are an annoyance for one developer become systemic blockers at forty-agent scale.
7. **The Ralph Loop and the factory model.** The Ralph Loop (Huntley/Carson) — pick, implement, validate, commit-if-pass, reset context, repeat — is "stateless but iterative," avoiding context-accumulation confusion. Four memory channels persist across resets: git history, a progress log, `tasks.json`, and AGENTS.md. The **factory model** reframes the developer's job as building the production line itself: Plan → Spawn → Monitor → Verify → Integrate → Retro.
8. **Human-curated AGENTS.md only — with a citable empirical claim.** Cites Gloaguen et al. (ETH Zurich): LLM-generated AGENTS.md files offer *no benefit* and can *marginally reduce* success rates (~3% average) while increasing inference cost 20%+; developer-written context files provide a ~4% improvement. Prescription: never let an agent write to AGENTS.md directly — the lead must approve every line.

## Why this source matters to the wiki

This is a **dense, concrete companion to the wiki's existing harness-engineering corpus**, distinct from Osmani's own later (15 May) [[2026-05-15-osmani-agent-harness-engineering|Agent Harness Engineering]] article in being organized around *operational patterns* (subagents vs. Agent Teams vs. orchestration tiers) rather than *definitional* harness vocabulary. It supplies:

- A **named citable claim** on AGENTS.md authorship (Gloaguen et al., ETH Zurich) that the wiki did not previously have in this specific form — most prior AGENTS.md coverage was practitioner-anecdotal.
- The **factory model** (Plan/Spawn/Monitor/Verify/Integrate/Retro) as a new reusable framework name, not previously present in the wiki under this exact vocabulary.
- The clearest wiki articulation yet of the **conductor-to-orchestrator mental-model shift**, complementing [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen/AWS's]] builders-to-orchestrators role-shift framing from a different (vendor-advisory) altitude.
- A concrete worked instantiation of Yegge's levels 5-8, closing the gap between the abstract framework ([[2026-03-12-oreilly-steve-yegge-wants-you-to-stop-looking-at-your-code|Yegge/O'Reilly]]) and lived practice.

## Linked entities and concepts

- [[Addy Osmani]] — 4th wiki source under this author; see entity page update.
- [[Steve Yegge]] — explicit level-5-through-8 build-out of his framework.
- [[concepts/agent-harness|agent-harness]] — Agent Teams architecture, quality gates, Ralph Loop, AGENTS.md discipline all slot directly into this concept's existing coverage.
- [[concepts/agentic-engineering|agentic-engineering]] — the factory model and spec-as-leverage claims bear on what the discipline of agentic engineering actually consists of.

## Source quality

**Full article** (36-page PDF print; matches a full conference-talk write-up with four embedded demo descriptions). First-party practitioner source — Osmani discloses his Google/Chrome affiliation but writes in a personal capacity; the article promotes his own O'Reilly book (*Beyond Vibe Coding*) at the close, a minor commercial framing that doesn't affect the substantive technical content. The Gloaguen et al. AGENTS.md claim is a named citable study, not anecdotal — but the wiki has not independently verified the study itself at ingest time.
