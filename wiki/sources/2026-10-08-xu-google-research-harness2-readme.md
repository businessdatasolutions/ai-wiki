---
type: source
kind: repository
title: "Harness²: Recursive Agent Harnessing for an Open World (README)"
author: ["Ruiyao Xu", "Yanfei Chen", "Zhongying CuiZhu", "Bhavana Dalvi Mishra", "Yifei Ming", "Han Yu", "Rujun Han", "Chen-Yu Lee", "Tomas Pfister"]
publisher: "Google Research (GitHub organisation google-research); Apache-2.0; not an officially supported Google product"
url: "https://github.com/google-research/harness2/blob/main/README.md"
date_published: 2026-10-08
date_ingested: 2026-11-28
length: "~9.4 KB README, 209 lines, read in full (blob a5e9120, last changed 14 Oct 2026); figures read from their alt text; paper, website and docs not ingested"
raw: "../../raw/repos/2026-10-08-google-research-harness2-readme.md"
tags: [harness2, google-research, agent-harness, harness-optimization, recursive-harnessing, self-improving-agents, propose-probe-compose, improvement-harness, open-world, jobbench, lab-benchmark, workbuddy-bench, opencode, codex, glm-5, gemini-3-5-flash, test-time-adaptation, benchmark-contamination, open-source]
relationships:
  - type: supports
    target: 2026-03-30-lee-meta-harness-end-to-end-optimization
    via: "Shared topic: optimizing the harness around a fixed model automatically. Meta-Harness searches harnesses for a benchmark using a coding agent with the full history on a filesystem; Harness² refines the harness per unseen task, without ground-truth feedback, and keeps lessons across tasks."
  - type: supports
    target: 2026-03-05-lou-deepmind-autoharness-code-harness-synthesis
    via: "Shared topic: the model writing its own harness, with weights unchanged. AutoHarness synthesizes code that blocks illegal actions in games; Harness² edits eight components (prompt, guardrails, memory, tool guidance, subagents, skills, scripts, plugins) for professional tasks."
  - type: supports
    target: 2026-05-11-karten-zhang-continual-harness-online-adaptation
    via: "Shared topic: a harness that adapts while the agent works, without a human rewriting it. Continual Harness adapts online within long game runs; Harness² refines per task and carries an improvement harness across tasks."
  - type: supports
    target: 2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness
    via: "Shared topic: what a harness is made of. Trivedy names five categories around the model; Harness² defines the harness as the system around the model and exposes eight editable components."
  - type: supports
    target: 2026-11-02-holmes-warp-agentic-self-improvement-loop
    via: "Shared topic: an outer loop that turns evidence from past agent runs into lessons for the next ones. Holmes describes it for a team's software factory; Harness² calls it harnessing-level recursion."
---

# Xu et al. (Google Research) — Harness²: Recursive Agent Harnessing for an Open World (README, Oct 2026)

## TL;DR

The README of **Harness²**, an open-source framework from the **[[Google Research]]** GitHub organisation. It was first committed on 8 October 2026 and last changed on 14 October; the repository had about 25,500 stars when fetched. The framework is licensed Apache-2.0, and the README disclaims it as *"not an officially supported Google product."* Authors are taken from its citation block: Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu, Bhavana Dalvi Mishra, Yifei Ming, Han Yu, Rujun Han, Chen-Yu Lee and Tomas Pfister. The method and results are in the paper (arXiv 2610.14224), which is not ingested; this page covers what the README claims.

1. **Definitions.** A *harness* is *"the system around a model that enables it to act as an agent"*: prompts, tools, memory, skills, orchestration. *Harnessing* is the process of optimizing that system. This is the [[agent-harness]] definition the wiki already uses, with a verb added.
2. **Built for an open world.** The target setting is agents that meet tasks nobody anticipated when the harness was designed. Model weights stay fixed throughout.
3. **Two levels of recursion.**
   - *Task-level recursion* refines the harness for the task in hand through **Propose–Probe–Compose**: propose edits, probe their effects by running them on the same task, then compose a refined harness from the behavioral contrasts between those runs. It works *"without ground-truth feedback"*.
   - *Harnessing-level recursion* updates a persistent **improvement harness** after each task, with the adopted harness and *"evidence-supported lessons,"* to guide the next refinement.
4. **Eight editable components:** system prompt, guardrails, memory, tool guidance, subagents, skills, scripts, plugins. The figure groups them by runtime role:
   - prompt, guardrails, memory and skills construct context;
   - tool guidance and scripts define the tool interface;
   - subagents orchestrate delegated work;
   - plugins are middleware.
5. **Two ways to spend more compute.** *Parallel* recursion probes *k* general and *k* domain-specific candidate harnesses and composes *k* refinements from the shared evidence (*"explores wider"*). *Sequential* recursion carries the refined harness and its evidence through *k* successive steps (*"refines deeper"*). The budget is the `--k` flag.
6. **Headline results, as stated in the README.** Across three professional benchmarks and four model–harness configurations, a single step improves **GLM-5** and **Gemini 3.5 Flash** over their base harnesses. The gains are up to 11.5 points on **WorkBuddy-Bench**, 4.5 points on **JobBench**, and 11.8 percentage points on **LAB**'s partial pass rate. A larger recursion budget brings further gains (no figures given).
7. **What ships.** OpenCode (default) and Codex as executors; JobBench (professional work), LAB (legal work) and WorkBuddy-Bench (office, web and code) as benchmarks. A local demo runs both recursion modes with deterministic editors and needs no model credentials. Model-backed runs use Vertex AI and *"incur API costs"*.
8. **A warning about its own benchmarks.** Executor network access is unrestricted, and Codex runs with its sandbox disabled. *"Public benchmark rubrics may be accessible online"*, so users must restrict network access before evaluating, or the agent can find answers and grading criteria.

## The figures, from their alt text

The README's three diagrams were not downloaded. Their alt text is detailed enough to record:

- **Pipeline.** In task-level recursion, an agent executor runs the initial harness, a harness editor proposes invariant and domain edits, candidate probes execute them, and a harness composer combines them into the final harness. In harnessing-level recursion, an experience reflector reflects on the step and updates the improvement harness used for the next task.
- **Components.** The eight components, grouped by runtime role (claim 4).
- **Recursion modes.** Parallel: probe *k* general and *k* domain-specific candidates, then produce *k* compositions from shared evidence. Sequential: *k* Propose–Probe–Compose steps carrying the refined harness and accumulated evidence.

## How it sits next to the wiki's harness-optimization sources

All five neighbours keep the model fixed and change what is around it. They differ in what is optimized, against what signal, and over what horizon.

| Source | What changes | Signal | Horizon |
| --- | --- | --- | --- |
| [[2026-03-30-lee-meta-harness-end-to-end-optimization\|Meta-Harness]] (Lee et al., Mar 2026) | The whole harness, as code | Scores on a task set, with full traces on a filesystem | One task domain at a time (e.g. classification, math, TerminalBench-2) |
| [[2026-03-05-lou-deepmind-autoharness-code-harness-synthesis\|AutoHarness]] (Lou et al., Mar 2026) | A code harness: action filter, action verifier or policy | The environment's rules (illegal moves) | One game |
| [[2026-05-11-karten-zhang-continual-harness-online-adaptation\|Continual Harness]] (Karten, Zhang et al., May 2026) | System prompt, subagents, skills, memory | The run itself | Within a long episode |
| Harness² (this page) | Eight components per task, plus a persistent improvement harness | Contrasts between probe runs, no ground truth | Per task, and across tasks |
| [[2026-11-02-holmes-warp-agentic-self-improvement-loop\|Holmes (Warp)]] (Nov 2026) | Improvements to the team's agent setup, proposed by an agent | Stored transcripts scored by LLM judges against rubrics | Across a team's work, on a schedule |

[[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy's anatomy]] gives the vocabulary all of them use. The README's eight components refine his five categories: guardrails split from prompts, and tool guidance split from the tools themselves.

## Why no dynamic-capabilities tags

A research framework for optimizing agent harnesses is agent engineering. It has no use case in a firm's digital transformation, so the field is left off per the schema's *"purely methodological"* rule.

## Related in this wiki

- [[2026-03-30-lee-meta-harness-end-to-end-optimization|Lee et al., Meta-Harness]]: end-to-end harness search by a coding agent that reads the full history of earlier candidates.
- [[2026-03-05-lou-deepmind-autoharness-code-harness-synthesis|Lou et al. (DeepMind), AutoHarness]]: a model synthesizing the code harness that keeps its own actions legal.
- [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten, Zhang et al., Continual Harness]]: online harness adaptation inside long game runs, automating what was human-in-the-loop refinement.
- [[2026-11-02-holmes-warp-agentic-self-improvement-loop|Holmes (Warp), an agentic self-improvement loop]]: a team's outer loop that scores stored runs and proposes improvements on a schedule.
- [[agent-harness]]: the concept page this definition belongs to.
- [[ai-benchmarks]]: three professional-work benchmarks new to the wiki (JobBench, LAB, WorkBuddy-Bench).
- [[reward-hacking]]: the README's warning that agents with open web access can reach benchmark rubrics.
- [[2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1|Stanford CS329A, Self-Improving AI Agents]]: the course frame for self-improvement at inference time.

## Linked entities and concepts

- **Entities:** [[Google Research]].
- **Concepts:** [[agent-harness]], [[ai-benchmarks]], [[reward-hacking]].
- **Dangling** (single-source mention, deferred): all nine authors; the benchmarks JobBench, LAB and WorkBuddy-Bench; GLM-5; OpenCode.

## Debates and supersession

- **README claims, not paper results.** The gains (up to 11.5, 4.5 and 11.8 points) are stated without baselines, variance, number of runs or cost. Two of the four configurations are not named. *"A single Harness² step"* hides how many probe runs a step spends; the parallel mode runs 2*k* candidates. Treat the numbers as the authors' summary until the paper is ingested.
- **"Without ground-truth feedback."** Propose–Probe–Compose compares executions on the same task, so a refinement is judged by behavioral contrasts. The README does not say what makes one run better than another without a grader. That is the question the paper must answer, and the reason the method could also learn the wrong lesson.
- **Contamination is left to the user.** Networking is open by default, and the README says public rubrics may be reachable. Any result reported from a default run could include agents finding grading criteria. This is the [[reward-hacking|reward-hacking]] concern in benchmark form.
- **Popularity is not evidence.** About 25,500 stars in under two months say the release drew attention, not that it works.

## What was actually ingested

The README in full, verbatim at blob `a5e9120`, fetched with the GitHub API on 28 November 2026, plus the repository's metadata and the README's commit history. Not ingested: the arXiv paper (2610.14224), the project website, the docs folder (benchmark, setup and experiment guides), the code, the setup GIF and the video overview. The three diagrams are recorded from their alt text, not viewed.
