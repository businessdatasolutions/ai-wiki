---
type: source
kind: video
title: "The Future of Agents with Harrison Chase"
author: ["LangChain"]
publisher: "LangChain (YouTube channel), webinar; speaker Harrison Chase, co-founder and CEO of LangChain, who also reads out the audience questions (no host or moderator)"
url: "https://www.youtube.com/watch?v=GojQtxCT3dg"
date_published: 2026-11-20
date_ingested: 2026-11-23
length: "~45:52 minutes (transcript ~351 lines + 15 stills; auto-generated (ASR) track, no chapters)"
raw: "../../raw/videos/the-future-of-agents-with-harrison-chase.md"
stills: "../../raw/videos/the-future-of-agents-with-harrison-chase.stills.md"
tags: [langchain, harrison-chase, langsmith, webinar, vendor-talk, persistent-agents, ambient-agents, always-on-agents, proactive-agents, tasks-vs-goals, goal-design, feedback-loops, event-triggers, crons, agent-memory, dreaming, multiplayer-agents, multi-surface, model-harness-context, deep-agents, base-harness, middleware, agent-runtime, durable-execution, agent-server, managed-deep-agents, context-hub, intended-observed-governed, evals, rubrics, missed-opportunities, regression-tests, annotation-queues, agent-governance, prompt-injection, permissions, tool-gateway, llm-gateway, audit-log, trace-data-controls, coding-agents, cost-per-merged-pr, own-your-intelligence, langsmith-engine, knowledge-factory, bitter-lesson, alignment, go-to-market-agents, state-of-agent-engineering-survey, science-technology]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-transforming/improving-digital-maturity
relationships:
  - type: depends-on
    target: 2026-10-05-chase-langchain-interrupt-nyc-opening-keynote
    via: "same speaker two months later; the webinar restates the keynote's 'own your intelligence', its split of an agent into business logic or context, harness and infrastructure, Managed Deep Agents, the LLM Gateway, LangSmith Engine and the shared-channel auth example, now arranged around persistent agents. A restatement by the same person, not independent support"
    confidence: 0.9
  - type: depends-on
    target: 2026-10-27-chase-langchain-interrupt-london-agents-improve-over-time
    via: "same speaker a month later on the improvement loop: traces and evals as its basis, choosing what to remember as its hardest part, LangSmith Engine as the agent that works it. Same authorship, not independent support"
    confidence: 0.85
  - type: depends-on
    target: 2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents
    via: "same speaker on the same question, the next year of agents: the May keynote's model, harness and context layers and its long-horizon agents that pursue goals return here as 'behavior comes from the whole system' and persistent agents"
    confidence: 0.8
  - type: depends-on
    target: 2026-05-09-chase-agent-development-lifecycle
    via: "same author; the essay's governed build-test-deploy-monitor loop and its durable execution reappear as the webinar's runtime, improvement loop and governance layer"
    confidence: 0.75
  - type: supports
    target: 2026-11-23-google-cloud-tech-why-agent-demos-break-in-production
    via: "both concern what a production agent needs around the model besides prompting: checks the model cannot override (Google's deterministic gates; Chase's identity, policy and approval at tool and model calls) and evals that grade actions and trajectories and are re-run when the prompt, model or harness changes"
    confidence: 0.65
  - type: supports
    target: 2026-05-07-anthropic-managed-agents-decoupling-brain-hands
    via: "both describe a hosted runtime for long-running agents in which the session is kept durable outside the harness, so a run survives a crash and the sandbox is a separate, replaceable part; Anthropic calls the parts brain, hands and session, Chase's slide front door, queue, execution, session state, recovery and environment"
    confidence: 0.65
  - type: supports
    target: 2026-05-08-bratanic-unified-agentic-memory-hooks
    via: "both describe agent memory kept as files that a separate background job, called dreaming or a dream phase, updates from what happened during sessions; Bratanic logs every event with hooks, Chase has the agent take notes and a curator agent merge them"
    confidence: 0.6
  - type: supports
    target: 2026-07-10-building-the-future-of-agentic-infrastructure
    via: "both concern agents that run ambiently, woken by events rather than user messages, and the identity and scoped access they then need; the Claude Platform team describes an agent negotiating access for a stated outcome, Chase permissions that depend on who acts, what action and on which surface"
    confidence: 0.6
  - type: supports
    target: 2025-07-31-wang-agentspec-runtime-enforcement-llm-agents
    via: "both place rules for what an agent may do outside the model, enforced at the moment it acts: AgentSpec as a rule language with triggers, predicates and enforcement; Chase as identity, policy and approval at the tool and model gateways, because 'a prompt is suggestions'"
    confidence: 0.6
  - type: supports
    target: 2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production
    via: "both concern evals built from an agent's own traces so that a change can be checked for regressions instead of judged by feel; Zamora and Feroz build the dataset with an agent and a Google toolkit, Chase with LangSmith annotation queues and subject-matter-expert rubrics"
    confidence: 0.6
---

# Chase (LangChain webinar) — persistent agents, and what it takes to run, improve and govern them

> Organizations are in a very different phase of agent development than they were a year ago. So what does the next chapter look like in 2027?
>
> New challenges are emerging in agent development and context engineering. How can teams better understand the impact and value of their agents? How is the rise of proactive, always-on agents surfacing new obstacles? How can developers manage growing complexity while maintaining control over performance and costs?
>
> Hear from Harrison Chase, Co-founder and CEO of LangChain, for a conversation on the future of AI agents, what's changing in how they're built, and what it will take to make them more capable, reliable, and scale in production.
>
> Get a look at what's next, the opportunities ahead, and how to prepare for the future of agent development in 2027.
>
> *— Channel description, LangChain*

## TL;DR

A 46-minute webinar by **[[Harrison Chase]]**, co-founder and CEO of **[[LangChain]]**, published on 20 November 2026. The description promises *"a conversation"*. The recording is Chase alone: he shares slides for 32 minutes, then reads audience questions from a Q&A panel and answers them for 11. The first 1:55 is a LangSmith promotional video. Most of the talk restates Chase's earlier keynotes, now arranged around one new term. Six claims:

1. **A new step: persistent agents.** After LLMs, tool calling, reasoning models and coding agents, *"we're at the start of a new step change"*: agents that are **goal-oriented**, **always on**, **accumulate context over time** and are **multiplayer and multi-surface**. Chase prefers *persistent* to *ambient*, *always-on* or *proactive* and credits the term to Dylan Patel. *"In a few years we won't call them persistent agents. We'll just call them agents."*
2. **Design the goal around the feedback.** A goal such as *"maintain inbox zero"* runs open-ended, unlike a bounded task. The hardest thing such an agent needs is user feedback, so goals should be cut where users find it natural to give feedback. His example is a sales-agent company that went from one agent per account to one agent per sales motion.
3. **The harness is half of it.** Behaviour comes from model, harness and context. Most teams take the model and a base harness off the shelf and bring their own context. *"The harness ... really only gets you about like half"*. The rest is an **agent runtime** around the harness: durable execution, message queuing and steering, a scheduler, session state, reliable streaming and an environment.
4. **Intended, observed, governed.** The runtime sets intended behaviour, but *"even if you tell an agent what to do, there's zero guarantee that it's actually going to do that."* An improvement loop tests observed behaviour, including the cases where the right action is to wait or stay silent, and turns failures caught in production into regression tests. Governance sets what the agent may do, and it is enforced at the choke points (tool calls, network and model calls), not in the prompt: *"A prompt is suggestions."*
5. **Three launches.** Trace data controls (masked inputs and outputs, user-group permissions, metadata-based access policies), **LangSmith for Coding Agents** (spend tied to merged PRs) and the **LangSmith Tool Gateway** (identity, token, policy, audit log).
6. **Memory: deciding what to keep, not storing it.** *"The actual storage of memory is not that hard ... The hard part is really deciding what to remember and then curating that over time."* He expects complex memory systems to get *"bitter lessoned"* into a coding agent with skills and tools. His sketch is agents that always take notes, a background curator (*"dreaming"*) that merges them, and company *"knowledge factories."*

## The promotional opening (0:00–1:55)

The recording opens with a LangSmith promo video, before Chase speaks: *"Right now, everyone is building agents, but only a handful of them are transforming businesses. Those that do are proactive, specialized, and they get better over time."* Its claims are unsourced: Workday's time to deploy a new agent *"went from 5 months to under a day"*; *"Teams using LangSmith Engine improve their agents five times faster"*; LangSmith *"processes billions of traces a month with more than 7,000 customers."* It offers Engine free to new Plus subscribers through the end of the year.

## Persistent agents: the step after coding agents (2:18–4:30)

Chase opens with a progression in five steps (LLMs, tool calling, reasoning models, coding agents, persistent agents). With coding agents, *"it wasn't just single model calls doing a lot of the work. It was these agents interacting with the environment."* Several names have circulated for what comes next. LangChain's own *ambient agents* post dates from January 2025. He credits Anthropic with a guide to *always-on agents*, and the slide also shows a Slack article on *proactive* agents. He credits *persistent agents* to Dylan Patel, *"or at least he's the first person I heard say it."* The slide shows Patel's post: *"Our spend on AI is now 45% persistent agents"* (still 1). Chase does not repeat the figure.

## Four traits, and goal design (4:30–9:12)

- **Goal-oriented.** A task (*"write this email"*) is a bounded action. A goal (*"maintain a blog or ... maintain inbox zero"*) is ongoing, optimises for an outcome and breaks itself into tasks (still 2). *"I think we'll talk a lot more about goal engineering or goal design."* His example is Actively AI, which builds sales agents: *"the hardest thing ... that is needed for these persistent agents is user feedback."* It moved from one agent per account to agents per stage shared across accounts (outbounding, early-stage deal progression), *"because their customers needed to basically teach the agent how to outbound,"* and feedback given across many accounts transfers (still 3).
- **Always on.** The agent wakes on real-world events, on schedules set by the developer or the user, and on schedules *"that the agent itself might set up"*. Waking up *"really what that means is just sending another message to the agent,"* from an event system rather than a person at a chat box (still 4).
- **Learns over time.** With longer horizons and vaguer goals, *"they need to keep that memory someplace so that it maintains consistency and makes progress towards its goal"* (still 5).
- **Multiplayer and multi-surface.** LangChain's internal agent **Robin** works in Slack with several users at once, and also through a desktop and a web app.

## Behaviour comes from the whole system (9:12–12:20)

An agent has three layers. The **model** brings reasoning and tool calling. The **harness** is *"how that model interacts with the environment"*: tools, the loop, the sandbox or file system. The **context** is the application-specific part: instructions, facts, feedback, memory and application-specific tools. Most builders *"will use a model off the shelf, whether it's a frontier model or an open-weight model,"* start from a base harness, and *"bring all of your own context ... that's the key part that makes the agent really domain-specific."* Deep Agents is LangChain's open-source, model-agnostic base [[agent-harness|harness]], with file system, sandbox and browser tools, context management (skills, summarisation, context offloading, prompt caching), human-in-the-loop and subagents. *"We want you to modify it"*, through middleware or by forking it.

## What each trait needs, and the agent runtime (12:20–20:50)

Chase goes back over the four traits and says what each needs:

- **Goal-oriented** needs prompting that makes the agent *"creative"*, not brute force: *"If you're waking up on a schedule and doing the same thing every 30 minutes, you're not going to make a bunch of progress."* It also needs alignment: *"if you give an agent a goal of kind of like removing all bugs from the codebase, it might accomplish that goal by just deleting the whole codebase."*
- **Always on** needs crons, tools that let an agent set its own reminders, event listeners (a new email, a Slack message), and a rule for messages that arrive mid-run: queue them or use them to steer.
- **Learning over time** needs a decision about user-, org- or agent-level memory, and about whether the agent *"can write to memory directly as it's running or does it write to notes ... a buffer that is then incorporated during dreaming."* Dreaming is *"a process where the agent runs in the background and looks at previous runs, previous notes ... and then updates its memory."*
- **Multiplayer** needs auth: *"if I start a thread and my coworker adds on the next message, it shouldn't be able to access my Notion or my email even though I started it."* **Multi-surface** needs state and streams that every surface can reach.

*"The harness ... really only gets you about like half of the stuff."* The rest is an **agent runtime** that *"sits outside"* the agent loop. It provides durable execution (*"if the agent fails halfway through a run, it doesn't just like start back from the beginning"*), APIs that decide whether a new message is rejected, queued or used to steer, a scheduler, state kept in the cloud, streaming that can be resumed on another device, and the environment (still 6). LangSmith Deployments supplies this as an *agent server*, with sandboxes, a context hub for skills, crons, threads, auth, a task queue with *"four different ways of multitexting"*, and checkpoints. **Managed Deep Agents** goes one level higher and bundles the harness with that infrastructure, so *"you just define the logic of your agents"* (still 7). *"If you want to run any harness you want, use the agent server."*

## Intended, observed and governed behaviour (20:50–25:25)

Chase names three kinds of agent behaviour.

**Intended behaviour** is what the runtime is told to do.

**Observed behaviour** is what actually happens, and it needs an improvement loop:

- **Test the whole agent.** Check tool calls, messages and state edits, and check that it does not do too much. *"If you have an agent waking up every 30 minutes and it reaches out to the user every 30 minutes, that's too spammy"* (still 8).
- **Grade traces and the end state against a rubric**, online without ground truth and offline with it (still 9).
- **Test silence as well as action.** *"You're going to want to test that it acts when it's worth acting on and it's also silent when it's not worth acting on"* (still 10).
- **Turn failures into tests.** Failures caught in production become evaluations *"that you can then basically use as unit tests for when you're making changes"* (still 11).

**Governed behaviour** is what the agent may never do. *"You should not define this in a prompt. A prompt is suggestions. The agent can ignore it. It can get prompt injected."* Policy, identity and approval are enforced *"at basically like the choke points"*: tool calls and network requests, including calls to models (still 12). Permissions depend on who is acting, what the action is and on which surface. In one of LangChain's own Slack agents, a DM may send email within the user's personal scope; a shared channel may not, *"because there's other people ... in the channel and there might be sensitive information."* See [[agent-oversight-and-delegation]].

## Own your intelligence, and three launches (25:25–33:48)

*"As agents become more powerful, you need to own how they behave. And that's what we really mean when we say own your intelligence"*: specify, observe and enforce. The slide maps LangSmith onto the three kinds of behaviour (still 13). **LangSmith Engine** is *"an agent that we actually built in LangSmith"* that monitors traces for issues and writes evals and fixes in the codebase. The reason given: *"you can send thousands or millions of traces to LangSmith and ... you can't look at them by hand anymore."* The **LLM Gateway** is where costs, model access and fallbacks are controlled. The three launches of *"this past week"*:

- **Trace data controls.** Traces *"contain a ton of sensitive information,"* and customers may have *"policies or contracts that don't allow you or your developers to see"* inputs and outputs. LangSmith now shows a masked *"skeleton"* by default, with permissions per user group, and opens inputs and outputs for traces whose metadata matches a policy. The typical use: open one complaining user's traces to a few people.
- **LangSmith for Coding Agents.** Connecting GitHub *"so you can associate coding agent spend with outcomes"*: cost per merged PR, cost over time by model, threads classified as bug fix or exploration. It integrates with *"things like Claude Code, pi, open code, Codex"* (still 14). See [[agent-fleet-management]].
- **LangSmith Tool Gateway.** For LangGraph agents, coding agents or any framework: it records which identity calls which tool, attaches an OAuth token, checks policy (allow, deny, or human-in-the-loop), forwards the call and writes an audit log *"on which human's behalf"* (still 15).

He closes with LangChain's annual **State of Agent Engineering** survey, whose questions are kept the same year to year *"so we have this good continuity."*

## Questions from the audience (34:18–45:52)

The askers' names and questions appear on screen; Chase reads them aloud.

- **Use cases beyond assistants** (Artur Serra). *"I think every use case will become a persistent agent ... I very strongly believe that."* Go-to-market is *"one category that will kind of like pop off the most"*: Actively, Clay, and LangChain's own GTM agent. Inside LangChain there is also a marketing agent, Content Studio, which maintains links and blogs and *"scheduled and sent a tweet that I do every Friday,"* and a coding agent for reviews and incidents.
- **Memory and scale** (João Valério). The squeeze is compute, not memory, because these agents run in sandboxes (*"we use Google under the hood"*). Storing memory is not the hard part. *"Most people have like pretty small memory things."* The hard part is deciding what to remember and keeping it fresh.
- **Rules for agents taking actions such as payments** (Tridris Tech). You *"absolutely need"* an audit log of every action, for auditors among others. Rules come from tool permissions in a policy layer (allow, deny, or human approval), possibly *"semantic policy"* on inputs, and from alignment. On alignment: *"I think it's way more of an issue than with these shorter task-based things because now these things are running in the background. You don't see what they're doing."*
- **Confidence in the continuous-learning loop** (Rico Romero). Three pieces: evals (offline before a change, online as A/B tests and regression checks), traces as *"the system of record of what agents done,"* and a *"bitter lesson"* view of tooling. Engine *"under the hood it's just a coding agent"* with particular skills, tools and CLIs. *"I think a lot of these complex systems for doing memory are going to get bitter lessoned."* A launch to make Engine *"more goal oriented and even more persistent"* is promised for the first week of December.
- **Memory architecture, and whether LangChain builds a wiki** (Erin Springmeyer). *"I actually don't think the storage format of memory matters that much."* *"Skills are procedural memory"* with their own format. Knowledge might live in OKF, markdown, a wiki or a graph database; he cites Hex's use of graphs. What matters is whether an agent can update memory while running (it can always take notes) and whether notes are visible at once or wait for a curator, *"the dreaming agent."* Traces are the best source for skills. For general knowledge, Notion and Slack are sources too, feeding a company knowledge base. *"One term that I used yesterday is like a knowledge factory."* See [[llm-wiki]].
- **One long session or many** (Kyle Estlick). *"I don't know if there's a right answer here."* One visible thread can hide separate threads underneath with good memory. Either way, give the agent search across past conversations.

## Relation to Chase's earlier talks

The wiki holds four earlier talks and essays by Chase, besides the interviews he conducted with Jensen Huang and Andrew Ng. Most of the webinar's architecture was in those four; the webinar groups it around persistent agents:

- [[2026-05-09-chase-agent-development-lifecycle|The Agent Development Lifecycle essay (May 2026)]] set out the governed loop of building, testing, deploying and monitoring, and named durable execution. The webinar sorts the same ground into runtime, improvement loop and governance.
- [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|The Interrupt 26 keynote (May 2026)]] asked the same question, what agents look like a year out. It had the model, harness and context layers and long-horizon agents that pursue goals.
- [[2026-10-05-chase-langchain-interrupt-nyc-opening-keynote|The Interrupt NYC keynote (Sept 2026)]] introduced *own your intelligence*, Managed Deep Agents, the LLM Gateway, Engine v2 and the shared-channel auth question that the webinar answers with a slide (permissions by who, what and surface). Its product map had three layers, *intelligence*, *runtime* and *observability and evals*. The webinar's map (still 13) is drawn as *runtime*, *improvement* and *governance*: Engine sits under improvement, and a governance layer holds the LLM Gateway and the new Tool Gateway.
- [[2026-10-27-chase-langchain-interrupt-london-agents-improve-over-time|The Interrupt London talk (Oct 2026)]] covered the improvement loop and called *"choosing what to remember"* its hardest part. The webinar's memory answers continue from there.

New here are the four traits of a persistent agent, goal design around feedback, the eval cases for an agent that should wait or stay silent, the agent-runtime diagram, and the three launches.

## Related in this wiki

- [[2026-11-23-google-cloud-tech-why-agent-demos-break-in-production|Google Cloud Tech: why agent demos break in production]]. Five Google engineers set out four layers for coding agents (Learn, Guard, Review, Score). Their *Guard* layer is deterministic gates the model *"cannot negotiate with or edit,"* and their *Score* layer re-evaluates the harness when the AGENTS file, a tool or the model changes. Chase puts the first at the governance choke points and the second in his regression loop (*"prompt, model, harness, or context"*).
- [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic, Managed Agents (April 2026)]]. Anthropic separates brain, hands and a durable session log so each can fail and be replaced on its own. Chase's runtime diagram keeps session state durable, recovers runs after crashes and deploys, and ties the sandbox to the session.
- [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic, unified agentic memory with hooks]]. Hooks log every session event and a periodic *dream phase* merges them into markdown notes. Chase describes agents that take notes while running and a background curator, *"the dreaming agent,"* that merges them.
- [[2026-07-10-building-the-future-of-agentic-infrastructure|Claude Platform team, building agentic infrastructure (July 2026)]]. The panel talks about agents that run ambient and long-horizon, triggered by events, and agents that negotiate their own scoped access. Chase lists event triggers and schedules, and permissions that change with the surface.
- [[2025-07-31-wang-agentspec-runtime-enforcement-llm-agents|AgentSpec (Wang et al.)]]. A rule language with triggers, predicates and enforcement, checked while the agent runs. Chase puts identity, policy and approval in the tool and LLM gateways, outside the prompt.
- [[2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production|Zamora and Feroz on catching agent failures]]. Evals built from an agent's traces so that changes are measured, not judged *"by feel."* Chase's version runs through LangSmith annotation queues and rubrics for subject-matter experts.

Concept pages: [[ai-agents]] (persistent agents as a category), [[agent-harness]] (the base harness and the runtime around it), [[agent-development-lifecycle]] (the improvement loop), [[agent-fleet-management]] (governance, gateways, spend), [[agent-oversight-and-delegation]] (enforcement outside the prompt, permissions by context), [[llm-wiki]] (memory format and knowledge factories).

## Visual canon

The talk is slide-led, and Chase's camera sits beside the slides throughout. Fifteen of 25 cut stills are published, each cropped to the slide. Left out: the progression curve and the list of four traits (both read aloud), the two screenshots of Robin in Slack and on the desktop, the model-harness-context slide, the Deep Agents harness slide (already published from [[2026-10-05-chase-langchain-interrupt-nyc-opening-keynote|Interrupt NYC]]), a LangSmith product inventory, a section card, the permissions slide (spoken in full) and the trace-data-controls slide. The stills were picked by hand from a 10-second contact sheet, because Gemini returned HTTP 402.

### 1 · Four names for one kind of agent

![[assets/2026-11-20-chase-langchain-future-of-agents/02-04m15-four-names-for-persistent-agents.webp|Four names for persistent agents: ambient, always-on, proactive and persistent]]

*Still at [4:15](https://www.youtube.com/watch?v=GojQtxCT3dg&t=255s) from LangChain, "The Future of Agents with Harrison Chase".*

- **Introducing ambient agents.** LangChain blog, "Harrison's In the Loop", Harrison Chase, January 14, 2025.
- **Dylan Patel (@dylan522p):** *"Persistent Agents are the next unlock of AI usage / Our spend on AI is now 45% persistent agents / Unfortunately for Anthropic, Claude Tags sucks / OpenAI's Slack agent is even worse."*
- **Building always-on agents.** *"Always-on agents run indefinitely, deciding how and when to act across many sessions."* No publisher on the card; Chase attributes the guide to Anthropic.
- **Proactive AI Agents: Definition, Core Components, and Business Value.** By the team at Slack, January 30th, 2026.

*Still vs. transcript:* Chase names the four terms and their sources. The 45% spend figure, Patel's verdicts on Anthropic's and OpenAI's Slack agents, and the dates appear only on the slide.

### 2 · Tasks vs goals

![[assets/2026-11-20-chase-langchain-future-of-agents/04-05m45-tasks-vs-goals.webp|Tasks vs goals: persistent agents execute a responsibility]]

*Still at [5:45](https://www.youtube.com/watch?v=GojQtxCT3dg&t=345s) from LangChain, "The Future of Agents with Harrison Chase".*

**Persistent agents execute a responsibility.**

| Task | Goal |
| --- | --- |
| "Write this email" → Done | "Maintain a blog" → a loop: pick a topic, draft a post, reply to readers |
| Action | Outcome |
| Bounded | Ongoing |

*Still vs. transcript:* the narration gives the same contrast with inbox zero as a second example; the slide's subtitle, *"execute a responsibility,"* is not spoken.

### 3 · Goal design around feedback loops

![[assets/2026-11-20-chase-langchain-future-of-agents/05-07m25-goal-design.webp|Goal design: from one agent per account to one agent per motion]]

*Still at [7:25](https://www.youtube.com/watch?v=GojQtxCT3dg&t=445s) from LangChain, "The Future of Agents with Harrison Chase".*

**Design goals around feedback loops.**

- *Before: one agent per account.* A sales rep works with agents for Account A, B and C, each with its own learnings.
- *After: one agent per motion.* A sales rep works with an **Outbounding** agent and an **Early-stage deal progression** agent. Each keeps one set of learnings across accounts A, B and C. **Context-gathering agents** feed both with account context.

*Still vs. transcript:* the context-gathering agents beneath the motion agents appear only on the slide. The narration names the company (Actively AI) and the reason for the change; the slide does not.

### 4 · Always on: what wakes the agent

![[assets/2026-11-20-chase-langchain-future-of-agents/06-07m58-always-on.webp|Always on: proactive agent triggers from events, developer schedules and agent schedules]]

*Still at [7:58](https://www.youtube.com/watch?v=GojQtxCT3dg&t=478s) from LangChain, "The Future of Agents with Harrison Chase".*

**Always on. React to events and crons, not messages.** Proactive agent triggers:

| Real-world events | Developer schedules | Agent schedules |
| --- | --- | --- |
| New email | Nightly memory update | Follow up tomorrow |
| Pull request opened | Weekly stale PR sweep | Daily brief you asked for |

All three feed the agent, and a loop marked *"schedules its own"* runs from the agent back to the agent schedules.

*Still vs. transcript:* the narration names the three kinds of trigger; the six examples are on the slide only. One of them, a nightly memory update, is a developer-scheduled job.

### 5 · Learns over time: the memory lifecycle

![[assets/2026-11-20-chase-langchain-future-of-agents/07-08m28-learns-over-time.webp|The memory lifecycle: seed, memory files, propose, feedback, act, outcomes, dreaming]]

*Still at [8:28](https://www.youtube.com/watch?v=GojQtxCT3dg&t=508s) from LangChain, "The Future of Agents with Harrison Chase".*

**The memory lifecycle.** Seed → **Memory** (`AGENTS.md`, `contacts.md`, `voice.md`, `projects.md`) → Agent proposes → Feedback → Agent acts → Outcomes. Feedback and Outcomes both go to **Dreaming**, a *"background job that updates memory,"* which writes back to Memory.

*Still vs. transcript:* the narration says only that the agent must keep memory *"someplace"*. The slide shows memory as markdown files, a propose-feedback-act cycle and dreaming. Dreaming is explained aloud only later, at 15:15. The slide's subtitle repeats the previous slide's *"React to events and crons - not messages"*.

### 6 · An agent runtime

![[assets/2026-11-20-chase-langchain-future-of-agents/12-18m05-an-agent-runtime.webp|An agent runtime: front door, queue, execution, session state, scheduler, recovery, live stream, environment]]

*Still at [18:05](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1085s) from LangChain, "The Future of Agents with Harrison Chase".*

**An agent runtime.** Your app (users, channels, other agents) → **Front door** (takes every message, applies your policy) → **Queue** (one turn at a time per session, in order) → **Execution** (your agent: your code, your harness; frees its worker while the session waits). Around them: **Session state** (conversation, progress and history, kept durable), **Scheduler** (crons, reminders and wake-ups), **Recovery** (carries on after crashes and deploys), **Live stream** (every event out, rejoin after a drop), **Environment** (sandbox and files, tied to the session). Outside: Models and tools (your keys, your MCPs) and Sandboxes (run model-written code). *Around it:* deploys and versions, tracing and metrics, identity and secrets, scaling. *Runs in:* managed, your cloud, self-hosted.

1. A message, schedule or event arrives.
2. Your policy decides what a busy session does with it.
3. It's saved to the session state.
4. It waits its turn: one turn at a time per session.
5. Your agent runs, with its state restored.
6. Events stream out to every client watching.
7. Progress is saved as it goes.
8. It finishes, or waits without holding a worker.

*Dashed line: after a crash or a deploy, recovery puts the work back in the queue.*

*Still vs. transcript:* the narration lists the parts. Only the slide shows the order, one turn at a time per session, a worker freed while a session waits, and that the runtime can run managed, in the customer's cloud or self-hosted.

### 7 · Managed Deep Agents on LangSmith

![[assets/2026-11-20-chase-langchain-future-of-agents/14-20m35-managed-deep-agents.webp|Managed Deep Agents: a project folder deployed onto agent server, context hub, schedules and sandbox]]

*Still at [20:35](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1235s) from LangChain, "The Future of Agents with Harrison Chase".*

| Your project | → `mda deploy` → | Managed Deep Agents on LangSmith |
| --- | --- | --- |
| `agent.py`, `tools/` └ `mcp.py` | | **Agent Server:** runs the Deep Agents harness; threads and streaming runs |
| `instructions.md`, `skills/`, `memory.py` | | **Context Hub:** instructions and skills; durable memory |
| `schedules/`, `channels/` └ `slack.py` | | **Schedules and channels:** cron jobs; runs started from Slack |
| `sandbox/` | | **Sandbox:** isolated filesystem and shell |

*Still vs. transcript:* the narration lists what a team defines; the slide shows it as a project folder, the deploy command and where each part runs.

### 8 · Test the agent responsibility

![[assets/2026-11-20-chase-langchain-future-of-agents/15-21m55-test-the-agent-responsibility.webp|Test the agent responsibility: the decisions around an output]]

*Still at [21:55](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1315s) from LangChain, "The Future of Agents with Harrison Chase".*

**A background agent often does the right thing by waiting, so those decisions need evals too.** Output: *"This message looks good."* Test the decisions around it:

| Situation | Question |
| --- | --- |
| Same event returns | Does it avoid duplicate outreach? |
| No useful signal | Does it stay quiet? |
| Human has not approved | Does it wait? |
| Access is revoked | Does it stop acting? |

*Still vs. transcript:* the narration gives the spam example and asks for tests of tool calls, messages and state. The four situations, and the point that a good output can still be the wrong decision, are on the slide only.

### 9 · Grade traces against a rubric

![[assets/2026-11-20-chase-langchain-future-of-agents/16-22m35-grade-traces-against-a-rubric.webp|Grade traces against a rubric given to subject matter experts]]

*Still at [22:35](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1355s) from LangChain, "The Future of Agents with Harrison Chase".*

**Give subject matter experts a rubric to grade traces against.**

| Trace | | Rubric |
| --- | --- | --- |
| Trigger | Account event | Was the signal relevant? |
| Context | Launch and prior outreach | Was the research grounded? |
| Decision | Draft, then wait for review | Was the next step useful? |
| | | Did the boundaries hold? |

*Still vs. transcript:* the narration gives two of the questions as examples. The slide names subject-matter experts as the graders and adds *"Did the boundaries hold?"*

### 10 · Missed opportunities and noise

![[assets/2026-11-20-chase-langchain-future-of-agents/17-23m05-missed-opportunities-and-noise.webp|Evaluate missed opportunities and noise: acts or stays quiet, worth acting on or not]]

*Still at [23:05](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1385s) from LangChain, "The Future of Agents with Harrison Chase".*

| | Worth acting on | Not worth acting on |
| --- | --- | --- |
| **Acts** | *Useful action:* surfaces a relevant opportunity | *Noise:* repeats a known product launch |
| **Stays quiet** | *Missed opportunity:* ignores a timely customer need | *Useful silence:* nothing has changed that matters |

*Still vs. transcript:* the narration names noise and missed opportunities as failures. The 2x2, with *useful silence* as a success, is on the slide only.

### 11 · Turn observed failures into regression tests

![[assets/2026-11-20-chase-langchain-future-of-agents/18-23m38-observed-failures-into-regression-tests.webp|Turn observed failures into regression tests: sample, review, keep, compare]]

*Still at [23:38](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1418s) from LangChain, "The Future of Agents with Harrison Chase".*

**Each failure you catch in production becomes a test, so it stays fixed when you change the prompt or the model.** Sample traces (actual behaviour, *including non-actions*) → Review a rubric (human judgment against explicit criteria; **LangSmith annotation queues**) → Keep useful cases (build an eval dataset from recurring failures) → Compare changes (prompt, model, harness, or context) → back to sampling.

*Still vs. transcript:* the narration describes the loop. The slide adds that non-actions are sampled too, that a human reviews against explicit criteria in annotation queues, and the four things a change can touch.

### 12 · A prompt can't enforce a rule

![[assets/2026-11-20-chase-langchain-future-of-agents/20-24m25-a-prompt-cant-enforce-a-rule.webp|A prompt can't enforce a rule: prompt-only path versus enforced action path]]

*Still at [24:25](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1465s) from LangChain, "The Future of Agents with Harrison Chase".*

- *Prompt only:* Agent: *"Do not send without approval"* - - → Email API. *Relies on the model holding back.*
- *Enforced action path:* Agent → **Identity, policy and approval** (*denies any call that fails a check*) → Email API.

*Still vs. transcript:* the narration makes the same argument in general terms; the slide gives it as an email example with the check placed between agent and API.

### 13 · LangSmith mapped to runtime, improvement and governance

![[assets/2026-11-20-chase-langchain-future-of-agents/22-27m25-langsmith-built-for-and-powered-by-agents.webp|LangSmith is built for and powered by agents: runtime, improvement and governance layers]]

*Still at [27:25](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1645s) from LangChain, "The Future of Agents with Harrison Chase".*

**LangSmith provides the foundation for companies to own and control their agent systems.**

| Layer | Open source | LangSmith |
| --- | --- | --- |
| Agent Runtime | deepagents · langgraph · langchain | Agent Server · Managed Agents · Fleet · Sandboxes |
| Agent Improvement | | Engine · Observability · Evaluation · Fine Tuning, on SmithDB |
| Agent Governance | | LLM Gateway · Tool Gateway |

*Still vs. transcript:* the narration covers the runtime, Engine and the two gateways. Fleet and Fine Tuning appear only on the slide. The Interrupt NYC version of this map, two months earlier, had *intelligence*, *runtime* and *observability and evals* as its layers.

### 14 · LangSmith for Coding Agents

![[assets/2026-11-20-chase-langchain-future-of-agents/24-32m15-langsmith-for-coding-agents.webp|LangSmith for Coding Agents: spend tied to merged PRs, dashboard for Robin]]

*Still at [32:15](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1935s) from LangChain, "The Future of Agents with Harrison Chase".*

**Reporting built for coding agents that ties their spend to the PRs they produce.** Dashboard for *Robin* (type *Coding*, GitHub connected, last 7 days):

| Metric | Value | Detail | vs. previous 7 days |
| --- | ---: | --- | --- |
| LLM cost | $21.3K | 49.5B tokens | ↑ 39% |
| Cost / merged PR | $34.65 | $4.97 direct · 614 merged PRs | ↓ 62% |
| Cache rate | 93% | 45.6B of 49.3B input tokens | ↓ 1 pt |
| Time to merge | 5 hrs | 89% merge rate · 614 of 692 resolved (cut off) | ↓ 92% |
| Threads | 22.8K | avg $1.00 / thread | ↑ 34% |
| Turns / thread | 2.9 | 67.2K turns | ↑ 1% |

Below: cost over time by model, 9–16 November, up to about $4K a day. Legend: claude-opus-5-5, gpt-6.1-sol, gpt-6.1-terra, gpt-6-astra, claude-sonnet-5-5, claude-fable-5-1, gemini-4-carbon, typesafe/jev-1.13.0, other.

*Still vs. transcript:* the narration names the metrics but gives no figures. The slide does not say whether these are LangChain's own numbers for its internal agent Robin or demo data, and the figures are internally consistent (614 PRs × $34.65 ≈ $21.3K).

### 15 · LangSmith Tool Gateway

![[assets/2026-11-20-chase-langchain-future-of-agents/25-33m35-langsmith-tool-gateway.webp|LangSmith Tool Gateway: identify, attach token, apply policy, forward and log]]

*Still at [33:35](https://www.youtube.com/watch?v=GojQtxCT3dg&t=2015s) from LangChain, "The Future of Agents with Harrison Chase".*

**Secure, governed tool use for agents.**

- **Agents and clients:** agents (LangGraph, Deep Agents, managed agents); coding agents (Claude Code, Codex, Cursor); your backend (calls for end users).
- **Tool Gateway:** Identify (user, agent or profile) → Attach token (stored in LangSmith) → Apply policy (deny or HITL) → Forward + log (to the MCP server). It reads credentials from **Connections** (tokens stored and refreshed) and records calls in **Tool call traces** (*audit log on Enterprise*).
- **Your tools:** built-in tools (Parallel, Google, and more); remote servers (any MCP server, by URL); private servers (in your network, via Tunnels).

*Still vs. transcript:* the narration walks through the four steps. The slide adds that the audit log is an Enterprise feature, names Claude Code, Codex and Cursor as clients, and shows private tool servers reached through tunnels. In the Q&A Chase says an audit log is something *"you absolutely need."*

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`.** The first half of the talk is a technology-trend reading. It names a new agent category, says *"every use case will become a persistent agent,"* and puts four circulating names side by side with their sources and a third party's spend claim. It also names go-to-market as the category that *"will pop off the most."* A CSO or CTO scanning for the next step in agents gets a vendor's map of it, not neutral evidence.
- **`digital-transforming/improving-digital-maturity`.** The second half is about building a firm's capacity to run agents well and to keep what they learn. Subject-matter experts grade traces against rubrics, production failures become regression tests, and every change is compared across prompt, model, harness and context. On memory, Chase proposes company *"knowledge factories"* that curate knowledge from agent traces, Notion and Slack into a shared knowledge base: leveraging digital knowledge inside the firm.

## Linked entities and concepts

- [[Harrison Chase]]: the only speaker; his first webinar in the wiki.
- [[LangChain]]: the channel and the vendor whose products the talk presents.
- Concepts: [[ai-agents]], [[agent-harness]], [[agent-development-lifecycle]], [[agent-fleet-management]], [[agent-oversight-and-delegation]], [[llm-wiki]].
- **Dangling** (single-source mention, deferred): Dylan Patel, Actively AI, Clay, Workday, Hex, Slack (as publisher of the *proactive agents* article).

## Source quality

**Transcript.** YouTube's auto-generated (ASR) English track, taken from the transcript panel: 351 segments, no chapters, no speaker labels (none are needed, since only Chase speaks). The ASR misheard most product names. *LangSmith* came out as "Langmith", "Linksmith" and "Blingsmith", and *Managed Deep Agents* as "managed Jeep agents" and "manage GPA". These were corrected in the raw file against the slides and the on-screen question banners, and each fix is listed in its `notes:`. Quotations here drop fillers and repeated words (*"uh"*, *"and and and"*). Names not shown on screen are kept as heard: *Actively AI*, *Clay*, *Hex*, *Muse and Instinct* (two products Chase says run on one big thread), and the *"podcast with Max agency"* he mentions. One read-out question was misheard in a way the banner corrects: the ASR has *"the records in automated control"*, the banner *"the records an auditor can trust"*.

**Identity.** Title, channel and date match. The description calls the webinar *"a conversation"*; it is a solo presentation followed by questions Chase reads out himself. The first 1:55 is an advertisement.

**Vendor and self-report.** A vendor CEO presents his own products in a talk that ends with a launch list. Every product claim is LangChain's own, without method or comparison. The promo's figures (Workday's *"5 months to under a day"*, Engine users improving agents *"five times faster"*, *"more than 7,000 customers"*) are unsourced. The transcript cannot settle three figures shown on screen:

- the 45% share of AI spend on persistent agents comes from a third party's social-media post, which Chase does not repeat;
- the coding-agent dashboard (still 14) is not identified as real or demo data;
- the *"five times faster"* claim has no baseline.

The Actively AI and Content Studio examples are reported by Chase, not by the companies.

**What it adds.** The persistent-agent framing and its four traits; eval design for agents whose right move is often to wait; a concrete runtime diagram; and Chase's working view on memory (notes plus a dreaming curator, storage format secondary, *knowledge factories*). The architecture mostly restates his earlier sources; see *Relation to Chase's earlier talks*.
