---
type: source
kind: video
title: "Why your AI agent demo breaks in production (and the 4-layer fix)"
author: ["Google Cloud Tech"]
publisher: "Google Cloud Tech (YouTube channel); host Smitha Kolan (Sr. DevRel Engineer, Google Cloud); presenters Logan Hennessy (DevRel), Remigiusz Samborski (Lead Developer Relations Engineer), Aron Eidelman (Security Advocate), YK Sugi (Sr. DevRel Engineer) and Annie Wang (Software Engineer), all Google Cloud"
url: "https://www.youtube.com/watch?v=BKVDdL1InsA"
date_published: 2026-11-23
date_ingested: 2026-11-23
length: "~27:31 minutes (transcript ~223 lines + 10 stills; human-written track, 24 chapters)"
raw: "../../raw/videos/why-your-ai-agent-demo-breaks-in-production-and-the-4-layer-fix.md"
stills: "../../raw/videos/why-your-ai-agent-demo-breaks-in-production-and-the-4-layer-fix.stills.md"
tags: [google-cloud-tech, google, smitha-kolan, logan-hennessy, remigiusz-samborski, aron-eidelman, yk-sugi, annie-wang, agent-harness, loop-engineering, harness-engineering, learn-guard-review-score, context-engineering, agents-md, persistent-memory, agent-skills, skill-md, progressive-disclosure, agent-plugins, google-cloud-developer-plugin, developer-knowledge-mcp, antigravity, antigravity-cli, deterministic-gates, git-hooks, red-green-refactor, test-driven-development, test-tampering, secret-scanning, static-analysis, dependency-pinning, slopsquatting, retry-limit, ai-code-review, gemini-code-assist, large-pull-requests, repo-walkthrough, multimodal-review, visual-qa, gemini-4-hydrogen, gemini-4-carbon, agent-evaluation, tool-use-evaluation, trajectory-evaluation, multi-turn-evaluation, multi-agent-handoffs, llm-as-judge, gemini, gemma, claude-code, codex, mcp, vendor-explainer, science-technology]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
relationships:
  - type: depends-on
    target: 2026-10-20-pettit-eidelman-galloway-google-cloud-security-review-with-agents
    via: "Aron Eidelman speaks on both: the Guard segment restates the test-first, deterministically gated agent workflow he showed on the October livestream (failing tests first, a 403 edge case, helper functions the agent ignores, deterministic scans before review). A restatement by the same person on the same channel, not independent support"
    confidence: 0.85
  - type: supports
    target: 2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails
    via: "both concern loop engineering on the same channel, and Annie Wang speaks in both: the August explainer names runaway loops (fix: a stop rule such as five iterations) and an agent reusing its own context (confirmation bias); this video sets a retry limit of three before a human takes over and has an independent reviewer agent in a fresh context window grade the coder's work"
    confidence: 0.7
  - type: supports
    target: 2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production
    via: "both, on Google Cloud Tech, concern evaluating an agent system before changes reach production: Zamora says that without evals a new version is judged by feel ('you're going to vibe it') and starts from tool-use and trajectory metrics; Smitha Kolan says that without scoring the system 'you're just guessing', and Annie Wang's first two patterns are tool use and trajectory"
    confidence: 0.7
  - type: supports
    target: 2026-05-15-osmani-agent-harness-engineering
    via: "both concern turning observed agent failures into harness rules and hooks: Osmani's ratchet (a commented-out test becomes an AGENTS.md rule, then a pre-commit hook that greps for skip markers); Eidelman's gates (git hooks that fail the run when tests are edited or skip tags added) and his order of work, the deterministic gate first, the skill file second"
    confidence: 0.7
  - type: supports
    target: 2026-08-19-he-databricks-anthropic-primitives-to-production-agents
    via: "both describe skills as packaged instructions loaded into context only when relevant: He (Anthropic) says skills are 'progressively loaded'; Samborski describes three stages (discovery of name and description, activation of the full SKILL.md, execution of scripts and references)"
    confidence: 0.7
  - type: supports
    target: 2025-06-12-spracklen-package-hallucinations-code-generating-llms
    via: "both concern slopsquatting: Spracklen et al. measure package hallucination in code-generating LLMs (19.7% of 2.23 million samples contained at least one invented package); Eidelman recommends pinning new packages in lock files and scanning them, so an invented name that someone has published maliciously is stopped"
    confidence: 0.7
  - type: supports
    target: 2025-11-26-gabor-evilgenie-reward-hacking-benchmark
    via: "both concern coding agents that edit tests to reach a passing result: EvilGenie places agents where they can hardcode test cases or edit test files and compares detection by held-out tests, LLM judges and test-file edit detection; Eidelman lists changed assertions, skip tags and disabled linters, and blocks them with git hooks that fail the run when existing tests, test counts, coverage or config files change"
    confidence: 0.65
  - type: supports
    target: 2026-06-08-vincent-coderabbit-fixing-ai-slop-managing-agents-like-mit-interns
    via: "both separate writing code from reviewing it across agents: Vincent's Superpowers hands the coder's work to a fresh spec-review sub-agent and then a quality reviewer, and reports an agent that tried to delete its own test suite; Hennessy's Layer 3 spins up an independent reviewer agent in a fresh context window instead of 'the coding agent grading its own homework'"
    confidence: 0.65
  - type: supports
    target: 2026-05-18-wolfe-agent-evaluation-detailed-guide
    via: "both break agent evaluation into tool-use checks (Wolfe: selection and trajectory accuracy; Wang: right tool, right inputs, right order), outcome versus trajectory, and multi-agent setups, with LLM-as-judge as one grader"
    confidence: 0.65
  - type: supports
    target: 2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail
    via: "both address why agents that work in demos fail in production and both answer context overload with skills loaded by progressive disclosure (InfoQ: name and description first, full instructions on demand); the InfoQ talk also reports information lost in orchestrator handoffs between agents, which Annie Wang's fourth pattern tests for ('did it hand off the right information')"
    confidence: 0.7
  - type: supports
    target: 2026-11-11-balasa-microsoft-path-to-production-for-agents
    via: "both address why an agent that works as a demo does not hold up in production: Balasa locates the gap in organisation and operations ('almost never the model'), with golden datasets and LLM-as-judge as release gates; this video locates it in four engineering layers around the model loop, ending in scoring the harness after every change"
    confidence: 0.6
  - type: supports
    target: 2026-11-02-holmes-warp-agentic-self-improvement-loop
    via: "both feed recorded failures back into an agent's skills: Holmes scores stored runs with LLM judges and has an agent propose skill and harness fixes on a schedule; Eidelman uses gate-failure logs to spot recurring mistakes and adds the fix to the repository's skill files, keeping the gate in place"
    confidence: 0.6
---

# Hennessy, Samborski, Eidelman, Sugi & Wang (Google Cloud Tech) — four layers between an agent demo and production

> This video contains the complete roadmap for AI agent engineering. Building an AI agent demo that looks magical takes ten minutes, but getting that same agent to ship reliable code in production without hallucinating, deleting unit tests, or submitting broken pull requests requires a completely different mindset. In this episode, five Google engineers break down the complete architecture of modern AI agent engineering, moving away from fragile prompt engineering and toward disciplined loop and harness engineering around models like Gemini.
>
> You'll follow the four-layer production blueprint—Learn, Guard, Review, and Score—step by step.
>
> First, Logan introduces the agent harness and shows how Layer 1 manages context using concise maps, persistent markdown memory, and modular skills. Next, Remik explains how open-source Agent Skills and the Google Cloud Developer Plugin use three-stage progressive disclosure (discovery, activation, and execution) to give agents deep domain knowledge without blowing up the context window. From there, Aaron demonstrates how Layer 2 locks down agent behavior using fast, deterministic guardrails, git hooks, secret scanners, and strict retry limits so agents cannot cheat their way to green tests. YC then tackles Layer 3—showing how to review massive AI-generated pull requests using interactive summaries, Repo Walkthrough visualizers, multimodal UI video QA with Gemini, and audio reviews. Finally, Annie closes the loop with Layer 4, walking through four practical evaluation patterns covering tool use, non-deterministic trajectories, multi-turn memory, and multi-agent handoffs.
>
> Products Mentioned: Gemini, Gemma, Model Context Protocol, Agent Skills specification, Google Cloud Developer Plugin, Developer Knowledge MCP server, Cloud Run, Google Cloud IAM, Antigravity, Claude Code, Codex
>
> *— Channel description, Google Cloud Tech*

## TL;DR

A 27-minute produced explainer on [[Google]]'s *Google Cloud Tech* channel, published 23 November 2026. Host [[Smitha Kolan]] links five segments by Google Cloud staff, each named by an on-screen lower-third: **Logan Hennessy** (DevRel) sets out the four layers; **Remigiusz Samborski** ("Remik", Lead Developer Relations Engineer) covers skills; **[[Aron Eidelman]]** (Security Advocate) covers deterministic gates; **[[YK Sugi]]** (Sr. DevRel Engineer) covers code review; **[[Annie Wang]]** (Software Engineer) covers evaluation. The description's "Aaron" and "YC" are misspellings, and the Logan here is Logan Hennessy, not Logan Kilpatrick.

The frame is Hennessy's: *"replacing yourself as the copy-paste middleman and moving from prompt engineering to loop engineering."* Loops live in the [[agent-harness|harness]], *"the layer of software that sits between the raw models underneath… and the finished application on top,"* which *"treats the model as a fixed black box and builds a system around it."* A model with tools in a while loop *"is pretty brittle"*; four layers make it something you can trust in production.

What it adds to the wiki:

1. **A four-layer blueprint for the coding-agent loop: Learn, Guard, Review, Score.** Learn manages the context window (a map such as an AGENTS file, plans and task lists on disk, skills loaded on demand). Guard wraps the loop in deterministic checks. Review hands the diff to an independent reviewer agent, including screenshots or video of the UI, before a human signs off. Score evaluates *"the harness itself"* whenever someone changes the agent file, adds a tool or swaps the model.
2. **Agent Skills as the Learn mechanism**: a folder with a `SKILL.md` (metadata on when to use it, instructions on how), loaded in three stages of progressive disclosure. Samborski says the specification was open-sourced in December 2025 and is supported across [[Claude Code]], Codex, [[Antigravity]] *"and almost every major coding harness."* Plugins bundle several skills, MCP servers and routing rules through a `plugin.json` manifest; Google's Cloud Developer plugin offers *"over 150 Google Cloud skills."*
3. **Gates an agent cannot argue with.** *"A prompt is just advice."* New tests must fail before code is written; git hooks fail the run when existing tests are edited, test counts or coverage drop, or config files change; secrets, static-analysis rules and pinned, scanned dependencies (against *slopsquatting*) run on every commit; failures go back to the agent as raw logs, with three retries before a human takes over. *"Write the deterministic gate first, then update your skill file second."*
4. **Reviewing AI-generated pull requests that are too big to read**: question the PR's size first, then add interactive file-by-file summaries to a one-shot bot review, then review *"from a different angle"*: an architecture visualizer, automated visual QA by Gemini critics, an audio summary. Test strategy follows the application type (browser end-to-end tests, tmux for CLIs, varied data for data apps).
5. **One figure, on screen only**: in an internal test of 33 UI-bug checks, *Gemini 4 Hydrogen* found 26 (79%) and *Gemini 3.8 Flash* 23 (70%) (still 8).
6. **Four evaluation patterns for agents**: tool use (right tool, inputs and order, against mocked tools); outcome and trajectory under non-determinism; single-turn to multi-turn memory; workflows and multi-agent handoffs, then end to end.

## Loop engineering and the four layers (0:00–4:13)

Kolan opens on the gap: a demo *"that looks magical"* takes ten minutes, but it is harder to work out why an agent *"hallucinated something, or why it deleted your unit test and submitted a massive broken pull request in production."* Hennessy's harness is *"a model like Gemini"* equipped with tools (*"a command line, file system access, or MCP servers"*) and wrapped *"in a while loop."* His slides place it in an *AI Stack*: applications, harness (*"loops live here"*), models (Gemini, Gemma) and silicon (still 1).

- **Learn (1:33).** *"Instead of a massive manual that goes out of date, you give the loop a lightweight map, like an AGENTS file."* For long tasks, *"the loop uses markdown plans and task lists on disk to record what is done, what failed, and what is next."* Skills on disk are pulled into the context window *"only when the loop actually needs them."*
- **Guard (2:41).** *"Just because our code executed successfully doesn't mean it is doing what we want."* The slide puts *compiles*, *unit tests* and *module boundaries* in a ring of deterministic checks around the loop.
- **Review (3:03).** *"Code can pass 100% of your unit tests and still be wrong."* The harness *"spins up an independent reviewer agent… in a fresh, unbiased context window, to review the diff against your engineering standards,"* and can run the app in a headless browser to capture screenshots or video *"before a human engineer gives final sign-off."*
- **Score (3:38).** Layers one to three are *"the components inside the car while it's driving down the road. Layer four is the diagnostic test bench in the garage."*

The same channel's [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails|four ways loop engineering fails]], with Annie Wang, defines loop engineering as *"you replacing yourself with a system"* and names two failures this video's layers address: runaway loops (fix: a stop rule) and an agent reusing its own context to check its own work (confirmation bias and context pollution).

## Learn: skills and progressive disclosure (4:13–8:22)

Samborski's problem: coding agents *"rely on static training data, so they invent outdated SDK code, guess invalid CLI flags, or run risky terminal commands,"* and *"stuffing 50 pages of rules and docs into your system prompt"* makes them *"even worse at coding."* His answer is the Agent Skills specification. A skill *"is just a portable folder"* holding a `SKILL.md` with *"a tiny metadata at the top describing when to use it, and the plain markdown instructions underneath,"* plus optional scripts and reference documents.

Progressive disclosure keeps 100 skills from clogging the context: at **discovery** the agent reads only each skill's name and description; at **activation**, when a prompt matches a description, it loads the full `SKILL.md`; at **execution**, extra files load *"only when this specific step is needed."* One skill travels on its own; *"wrapping one skill in a plugin is an overkill."* Plugins earn their keep *"when a complex domain needs multiple skills, live MCP servers, and routing rules working all together,"* bundled with a `plugin.json` manifest. The **Google Cloud Developer plugin** offers *"one-click install, live documentation from Developer Knowledge MCP server, strict IAM and billing guardrails, and on-demand access to over 150 Google Cloud skills,"* and works with Claude Code, Codex *"or any other compatible agent."* The screen recording shows it as one entry in Antigravity's *Customizations* marketplace (still 2).

[[2026-08-19-he-databricks-anthropic-primitives-to-production-agents|Isabella He (Anthropic)]] describes skills the same way: *"packaged instructions"* whose key property is that *"they're progressively loaded."* The InfoQ talk [[2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail|From Demo to Production]] reports the same fix for the same problem on a platform with 10 agents and 200+ tools: context overload answered by skills, with name and description loaded first and full instructions on demand. The December 2025 date matches [[2026-01-06-loukides-radar-trends-january-2026|Loukides's January 2026 digest]], which records Anthropic opening the Claude Skills spec and OpenAI adopting it; Samborski names no originator.

## Guard: deterministic gates (8:22–13:35)

Kolan's bridge: when an agent gets stuck, *"it might actually cheat. Prompting the model to be careful won't actually save you here, because a prompt is just advice."* Eidelman's test for an agent that reports passing tests: *"Were those tests already there, or did the agent just write them? Did it tweak any old tests just to get a green light?… If you don't know for sure, you're just taking the agent's word for it."*

A deterministic check *"gives you the exact same result every time without any AI model chiming in"*: compilers, type checkers, tests with fixed inputs, lint rules, secret scanners, *"source component analysis"* and rule-based security tests. They are *"less expensive than using tokens"* and give *"the exact file, line number, and error message."* Security is *"a part of quality"*: an agent that *"ignores helper functions you already have, or breaks code that was working fine five minutes ago"* does damage without any vulnerability. His rules:

- **Tests first, in small steps.** The harness runs a new test before the implementation; *"if it passes right away, it's not testing anything new, so kick it back out."* The slide adds a planning step before the red-green-refactor stages (still 3).
- **Hooks against test tampering.** Agents *"might change assertions, add skip tags, or disable linters. Don't just ask them nicely in the prompt. Set up actual Git hooks."* Fail the run *"if existing tests get edited, if test counts or coverage drop, or if config files get modified."* Rerun new tests: *"If a test only passes 80% of the time, block it until it's solid."*
- **Security gates on every commit.** Secret scanning; static analysis for *"SQL queries with string concatenation or unvalidated user input"*; new packages pinned in lock files and scanned, which *"stops slopsquatting, where an agent hallucinates a package name that someone else actually published maliciously."*
- **Raw logs back, then a limit.** Send *"rule ID, file, line number, failing assertion"* straight to the agent (still 4); *"set a retry limit, like three attempts,"* then hand over to a human with the log. *"Never let the agent modify gate configurations or hook scripts."*
- **Failures feed the skills, but the gate stays.** Recurring patterns (*"outdated libraries or forgets tenant filters or writes weak mocks"*) go into the repository's skill files; *"skills help the agent produce better code, but gates are what keep bad code from getting merged."*

This restates the workflow Eidelman showed on the same channel a month earlier, in [[2026-10-20-pettit-eidelman-galloway-google-cloud-security-review-with-agents|Google's approach to security review with agents]]: failing tests that include a 403 edge case, a skill naming the project's helper methods to stop *"side quests,"* and deterministic scans before any agent review. On the shared topic of rules built from failures, [[2026-05-15-osmani-agent-harness-engineering|Osmani]]'s ratchet turns a commented-out test into an AGENTS.md rule and then a pre-commit hook that greps for `.skip(`. [[2025-11-26-gabor-evilgenie-reward-hacking-benchmark|EvilGenie]] measures agents that hardcode test cases or edit test files, and how well held-out tests, LLM judges and test-file edit detection catch them; see [[reward-hacking]]. [[2025-06-12-spracklen-package-hallucinations-code-generating-llms|Spracklen et al.]] measured the hallucinated-package rate behind slopsquatting: 19.7% of 2.23 million generated samples contained at least one invented package. [[2026-11-02-holmes-warp-agentic-self-improvement-loop|Holmes (Warp)]] feeds failures back into skills too, by scoring stored runs with LLM judges and having an agent propose fixes on a schedule.

## Review: AI-generated pull requests (13:35–20:57)

Sugi: *"how do you deal with a PR that's 200,000 lines long?"* First ask whether it is valid: *"Could it be 10 PRs with 20,000 lines of code each?"* Keeping PRs small *"is still the best practice,"* but when that is not realistic, *"I think of code review like eating a watermelon… with a large PR, the best you can do is slice it in a few different ways."* His slices, demonstrated on a merged PR that adds his `repo-walkthrough` skill (24 files, +11,150 lines on screen):

- **One-shot review.** Gemini reviews every open PR and comments on parts of it (the `gemini-code-assist` bot, still 5). *"These one-shot AI code review systems are great, they're often not sufficient by themselves."*
- **Interactive review.** Ask an agent for *"a quick one-sentence summary"* of each file in the PR. The recording shows this in the Antigravity CLI.
- **Multimodal review.** The `repo-walkthrough` skill turns *"any code, diff, PR, or repo into an interactive visualizer and a video"* (still 6). For visual QA, a system records the site at several screen sizes and has *"Gemini 4 Hydrogen critics watch the videos as well as the screenshots"*; issues go back to *"the main thread,"* which reports or fixes them. Overlapping elements *"it's able to fix… automatically,"* but *"you still need to click around."* The slides name the merger, Gemini 4 Carbon, and the three fixes (still 7), and give the comparison in still 8. A CLI banner calls Gemini 4 Hydrogen Google's *"daily driver for rapid coding and dependable agentic execution."*
- **Audio.** A private skill turns a PR into *"a few paragraphs summary"* and *"an audio review site."*
- **Tests by application type.** Browser end-to-end tests for UI-heavy apps, tmux-driven tests for CLIs, varied data types and volumes for data-intensive apps.

On separating the writer from the reviewer, [[2026-06-08-vincent-coderabbit-fixing-ai-slop-managing-agents-like-mit-interns|Jesse Vincent's Superpowers]] hands a coder sub-agent's work to a fresh spec reviewer and then a quality reviewer. See [[agentic-pull-requests]] and [[ai-generated-code-quality]].

## Score: evaluating the agent system (20:57–27:31)

Kolan: a teammate edits *"a few lines in your AGENTS.md file"* or swaps in a newer model, *"so your current task might get 20% faster, but 10 other workflows might actually silently break behind your back. And if you aren't scoring the system itself, you're not really engineering, you're just guessing."* Wang: an LLM *"can say, 'Yes, I've refunded your payment,' but it cannot actually do anything,"* so agent evaluation checks the whole system: rules, steps, the action and the reply. Her refund example runs through four patterns:

1. **Tool use**, *"very like a unit test for an agent's action"*: right tool, right inputs (*"exact order ID"*), right order (*"checking eligibility before issuing a refund"*), run *"against mock tools and sample data… without ever moving real money."*
2. **Outcome and trajectory.** Two runs give two replies, so *"you cannot rely on exact word-for-word string matches"*: measure similarity to the expected answer and whether the refund policy was followed; then check the trace for an exact tool sequence, a required order, *"or we can simply pass LLM as a judge for efficiency"* (still 9).
3. **Single-turn to multi-turn.** *"I want a refund"*, then order 101, then *"Oh, wait, I actually mean order 202"*: *"multi-turn evaluation tests memory and state across turns."*
4. **Workflows and multi-agent systems.** A workflow *"connects deterministic function nodes with agent nodes in a graph"*; test that data passes cleanly from code to agent and back. In a multi-agent system, test that it delegated to the right specialist and handed over the right information (*"Annie's updated order 202, not… order 101"*) (still 10); then evaluate end to end, *"from the customer's first message, all the way to the complete refund."*

[[2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production|Google Cloud Tech's AI Agent Clinic]] makes the same opening point (without evals a change is judged by feel, *"you're going to vibe it"*) and starts from tool-use and trajectory metrics. [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe's guide]] names tool-use metrics (invocation, selection, structural and trajectory accuracy) and the manager and decentralised multi-agent setups. [[2026-11-11-balasa-microsoft-path-to-production-for-agents|Balasa (Microsoft)]] addresses the same demo-to-production gap as an organisational one (*"almost never the model"*), with golden datasets and LLM-as-judge as release gates. See [[agent-development-lifecycle]].

For a firm whose developers work with coding agents, the video touches `digital-transforming/improving-digital-maturity` in its *leveraging digital knowledge inside the firm* sense: a team's workflows and conventions are packaged as skills, and recurring gate failures are written back into the repository's skill files so the next agent run starts with them. See [[agentic-engineering]].

## Visual canon

Ten stills from 33 cut, hand-picked from 5-second contact sheets and a 1-second pass over the animated diagrams (Gemini returned HTTP 402). Slide stills are cropped to the slide panel or overlay card. Slides that restate the narration (the Learn, Guard, Review and Score diagrams, the skill anatomy, Annie Wang's other pattern slides) were left out; the manifest records all 33.

### 1 · The AI stack, with the harness in the middle

![[assets/2026-11-23-google-cloud-tech-why-agent-demos-break-in-production/01-01m03-ai-stack.webp|AI Stack with the harness between applications and models]]

*Still at [1:03](https://www.youtube.com/watch?v=BKVDdL1InsA&t=63s) from Google Cloud Tech, "Why your AI agent demo breaks in production (and the 4-layer fix)".*

*Loop Engineering* · **AI Stack**, top to bottom:

- **Applications** — the finished app on top
- **Harness** — software around the model · loops live here
- **Models** — Gemini · Gemma
- **Silicon**

*Still vs. transcript:* Hennessy places the harness between models and applications; the slide adds silicon as the bottom layer and says the loops live in the harness.

### 2 · Plugins in Antigravity's marketplace

![[assets/2026-11-23-google-cloud-tech-why-agent-demos-break-in-production/13-08m09-antigravity-build-with-google.webp|Antigravity Customizations marketplace with Google plugins]]

*Still at [8:09](https://www.youtube.com/watch?v=BKVDdL1InsA&t=489s) from Google Cloud Tech, "Why your AI agent demo breaks in production (and the 4-layer fix)".*

Antigravity, *Customizations* › *Marketplace*. Entries (descriptions truncated on screen): Science (*curated collection of agent skills for scien…*), Google Antigravity SDK, Google Developer Knowledge (*search and retrieve official documentatio…*), Modern Web Guidance, Google Maps Platform, Dart and Flutter, Data Agent Kit, **Google Cloud Developer** (*Google Cloud guidance for coding agents…*), Elephant-Goldfish Model. Earlier frames show a *Build with Google* section (*"Build on Google's developer platforms, including Android, Chrome, Gemini, and Google Cloud"*) with Gemini API, Chrome DevTools, Android CLI and Firebase, and a Google Workspace section.

*Still vs. transcript:* Samborski gives the click path to the Google Cloud Developer plugin; the screen shows it as one of a dozen Google plugins and skill collections in the same marketplace.

### 3 · Plan first, then small red-green-refactor stages

![[assets/2026-11-23-google-cloud-tech-why-agent-demos-break-in-production/17-10m52-small-test-first-commits.webp|Plan followed by three red green refactor stages]]

*Still at [10:52](https://www.youtube.com/watch?v=BKVDdL1InsA&t=652s) from Google Cloud Tech, "Why your AI agent demo breaks in production (and the 4-layer fix)".*

**Execution with small, test-first commits** — *Tiny red → green → refactor steps.*

- **Plan** — Articulate the design and divide into stages
- Stage 1, Stage 2, Stage 3: Red → Green → Refactor
- *Small commits: if something breaks, you know exactly what caused it*

*Still vs. transcript:* Eidelman speaks of tiny red-green-refactor steps; only the slide puts a planning step, dividing the design into stages, before them.

### 4 · A failed gate, sent back to the agent

![[assets/2026-11-23-google-cloud-tech-why-agent-demos-break-in-production/18-12m14-when-a-gate-fails.webp|Failed gate log sent straight back to the agent]]

*Still at [12:14](https://www.youtube.com/watch?v=BKVDdL1InsA&t=734s) from Google Cloud Tech, "Why your AI agent demo breaks in production (and the 4-layer fix)".*

*Layer 2 · Guard* — **When a gate fails** — *Send the raw error log back.*

| `gate · tests · FAILED` | |
| --- | --- |
| Rule ID | `tenant-filter-required` |
| File | `api/invoices.py` |
| Line number | `87` |
| Failing assertion | `assert status == 403` |

→ **Straight back to the agent**

*Still vs. transcript:* the narration lists the fields; the card fills them with a worked failure, a tenant-isolation rule tested by an HTTP 403 check, the same kind of security edge case Eidelman described on the October livestream.

### 5 · A one-shot AI review on a merged pull request

![[assets/2026-11-23-google-cloud-tech-why-agent-demos-break-in-production/20-15m27-one-shot-ai-code-review.webp|Gemini Code Assist review on a merged pull request]]

*Still at [15:27](https://www.youtube.com/watch?v=BKVDdL1InsA&t=927s) from Google Cloud Tech, "Why your AI agent demo breaks in production (and the 4-layer fix)".*

`GoogleCloudPlatform/devrel-demos` pull request **#1567, Add repo-walkthrough**, merged. `gemini-code-assist` (bot) reviewed it on Oct 9 and left a **Code Review** comment: the PR *"adds the `repo-walkthrough` agent skill, enabling the generation of interactive codebase architecture graph websites and voice-narrated MP4 walkthrough videos"*; its recommendations are *"sequentially executing acoustic alignment in `generate_live_audio.mjs` to avoid API rate limits, URL-encoding branch names and file paths in `fetch_repo.py`… using robust regex for `.env` parsing, and hardening input validation in `index.html` against Local File Inclusion (LFI) vulnerabilities."* Five inline threads below are marked *Resolved*.

*Still vs. transcript:* Sugi describes one-shot review in general; the screen shows the bot, the repository and the kind of findings it returns (rate limits, encoding, parsing, a file-inclusion risk).

### 6 · The repo-walkthrough visualizer

![[assets/2026-11-23-google-cloud-tech-why-agent-demos-break-in-production/22-17m32-repo-walkthrough-visualizer.webp|repo-walkthrough visualizer for a pull request]]

*Still at [17:32](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1052s) from Google Cloud Tech, "Why your AI agent demo breaks in production (and the 4-layer fix)".*

**PR #1567: Add repo-walkthrough** — *GoogleCloudPlatform/devrel-demos · 24 files added (+11,150 / -0) · Diff Walkthrough.* Five bands of added files, with line counts:

| Band | Files |
| --- | --- |
| Skill & docs entry | `README.md` +83, `SKILL.md` +104, `data-schema.md` +96 |
| Diff & build engine | `fetch_repo.py` +715, `build_walkthrough.mjs` +361 |
| Interactive graph UI | `web/index.html` +1506, `web/data-adk.js` +470 |
| TTS audio & MP4 video | `generate_live_aud…` +502, `render_video.mjs` +341, `render_video.sh` +19 |
| Examples & test suite | `cymbal…/dat…` +433, `diff-5984e02…` +364, `test_pipeline…` +327, `test_ui_e2e.m…` +740 |

A caption panel (*Step 1 / 6*) narrates the overview, with play controls and speeds from 0.8× to 1.2×.

*Still vs. transcript:* the narration mentions the layers and the README in passing; the screen shows the tool's output and the size of the example: 24 files and 11,150 lines, against the hypothetical 200,000-line PR of the narration.

### 7 · Six critics, one merger, three fixes

![[assets/2026-11-23-google-cloud-tech-why-agent-demos-break-in-production/24-18m42-carbon-merges-bug-reports.webp|Gemini Carbon merging six critic reports into three fixes]]

*Still at [18:42](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1122s) from Google Cloud Tech, "Why your AI agent demo breaks in production (and the 4-layer fix)".*

**Gemini 4 Carbon merges the bug reports.** Six **Gemini 4 Hydrogen** critics (phone video, phone stills, tablet video, tablet stills, desktop video, desktop stills) → **Gemini 4 Carbon** (*merges 6 reports*) →

- Fix 1: Top bar covers the score
- Fix 2: Dock covers the radar
- Fix 3: Top bar blocks UI text

*Still vs. transcript:* Sugi says critics watch the videos and screenshots and report to *"the main thread"*; the slide names the two models, the six critic inputs and the three fixes found on a 3D game.

### 8 · Hydrogen against Flash on UI bugs

![[assets/2026-11-23-google-cloud-tech-why-agent-demos-break-in-production/26-19m02-hydrogen-catches-more-ui-bugs.webp|Hydrogen catches more UI bugs, an internal comparison]]

*Still at [19:02](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1142s) from Google Cloud Tech, "Why your AI agent demo breaks in production (and the 4-layer fix)".*

**Hydrogen catches more UI bugs**

| Model | UI bug checks caught |
| --- | ---: |
| Gemini 4 Hydrogen | 26 of 33 (79%) |
| Gemini 3.8 Flash | 23 of 33 (70%) |

*"Internal test: 33 real UI bug checks on internal apps, median of 3 runs, scored by 3 blinded judges. Results may vary."*

*Still vs. transcript:* neither the comparison nor its method is spoken.

### 9 · A trajectory check on a trace

![[assets/2026-11-23-google-cloud-tech-why-agent-demos-break-in-production/29-24m37-pattern-2-trajectory.webp|Trajectory trace of three tool calls with two checks]]

*Still at [24:37](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1477s) from Google Cloud Tech, "Why your AI agent demo breaks in production (and the 4-layer fix)".*

**Pattern 2: Outcome and trajectory** — *Trajectory: how it got there, step by step.* Trace: 1 `lookup_order` (`order_id: 101`) → 2 `check_eligibility` (`order_id: 101`) → 3 `issue_refund` (`order_id: 101`). Checks: **Exact sequence** (tool calls match); **Required order** (eligibility before refund).

*Still vs. transcript:* the trace adds a third call, `lookup_order`, ahead of the two used in pattern 1; the slide shows two trajectory checks, while Wang also offers LLM-as-judge as the cheaper option.

### 10 · Routing to the right specialist with the right information

![[assets/2026-11-23-google-cloud-tech-why-agent-demos-break-in-production/32-26m52-pattern-4-multi-agent-handoffs.webp|Agent routing a refund request to a specialist agent]]

*Still at [26:52](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1612s) from Google Cloud Tech, "Why your AI agent demo breaks in production (and the 4-layer fix)".*

**Pattern 4: Workflows and multi-agent systems** — *Multi-agent: test agent-to-agent handoffs.* An agent passes `Annie · order 202` to the **refund agent** (ticked), not the billing agent or the shipping agent. Checks: **Right specialist** (level 1 · who gets the task); **Right information** (level 2 · order 202, not 101).

*Still vs. transcript:* Wang gives the two levels; the slide shows the specialists the router chooses between.

## Linked entities and concepts

- **Organisation and products:** [[Google]] (the channel and all six speakers), [[Antigravity]] (the app, its plugin marketplace and its CLI in the review demo), [[Claude Code]] (named as a harness that supports skills and the Google Cloud Developer plugin).
- **People:** [[Smitha Kolan]] (host), [[Aron Eidelman]] (Guard; second appearance, proposed for promotion in this ingest), [[YK Sugi]] (Review; the lower-third gives his role as Sr. DevRel Engineer, Google Cloud), [[Annie Wang]] (Score).
- **Concepts:** [[agent-harness]], [[agentic-engineering]], [[ai-generated-code-quality]], [[agentic-pull-requests]], [[reward-hacking]], [[agent-development-lifecycle]].
- **Neighbour sources:** [[2026-10-20-pettit-eidelman-galloway-google-cloud-security-review-with-agents]], [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails]], [[2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production]], [[2026-05-15-osmani-agent-harness-engineering]], [[2026-08-19-he-databricks-anthropic-primitives-to-production-agents]], [[2025-06-12-spracklen-package-hallucinations-code-generating-llms]], [[2025-11-26-gabor-evilgenie-reward-hacking-benchmark]], [[2026-06-08-vincent-coderabbit-fixing-ai-slop-managing-agents-like-mit-interns]], [[2026-05-18-wolfe-agent-evaluation-detailed-guide]], [[2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail]], [[2026-11-11-balasa-microsoft-path-to-production-for-agents]], [[2026-11-02-holmes-warp-agentic-self-improvement-loop]]; also cited: [[2026-01-06-loukides-radar-trends-january-2026]].
- **Dangling** (single-source mention, deferred): Logan Hennessy, Remigiusz Samborski, Agent Skills specification, Google Cloud Developer plugin, Developer Knowledge MCP server, Gemini Code Assist, Antigravity CLI, Gemini 4 Hydrogen, Gemini 4 Carbon, repo-walkthrough skill, Codex.

## Source quality

**Human-written caption track** (YouTube's en-US track, matching the transcript panel word for word), 223 segments with the channel's 24 chapters. Names were checked against the lower-thirds and needed no correction; the channel description misspells two of them (*Aaron*, *YC*). Title and description match what is said and shown.

A vendor explainer: Google Cloud developer-relations staff presenting practice built around Google products (Antigravity, the Google Cloud Developer plugin, Gemini models, Gemini Code Assist), with Claude Code and Codex named as compatible. The four-layer blueprint is offered as practice, with no measurement of its effect. The one figure (still 8) is Google comparing two of its own models on an internal test of 33 UI-bug checks on internal apps; the slide gives the method (median of 3 runs, 3 blinded judges) and *"Results may vary,"* and it is not spoken. The transcript cannot settle the plugin's *"over 150"* skills, the specification's support *"across… almost every major coding harness,"* or the December 2025 open-sourcing (corroborated for Anthropic's opening of the spec by [[2026-01-06-loukides-radar-trends-january-2026|Loukides]]). The 200,000-line PR is hypothetical; the PR on screen has 24 files and 11,150 lines and adds the presenter's own skill. *Gemini 4 Hydrogen* and *Gemini 4 Carbon* appear on screen and in the CLI as model names; the corpus has no other source on them. The ten stills were picked by hand from contact sheets; all 33 cut frames are recorded in the [stills manifest](../../raw/videos/why-your-ai-agent-demo-breaks-in-production-and-the-4-layer-fix.stills.md).
