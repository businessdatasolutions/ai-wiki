---
video_id: GojQtxCT3dg
url: https://www.youtube.com/watch?v=GojQtxCT3dg
transcript: raw/videos/the-future-of-agents-with-harrison-chase.md
stills_dir: raw/images/the-future-of-agents-with-harrison-chase
stills_count: 25
extractor:
  method: hand-picked (no Gemini call)
  reason: Gemini API returned 402 (prepayment credits depleted)
  sampling: 275 frames at 360p, one every 10 s, into 275 tiles (no consecutive repeats merged), read as six 6x8 contact sheets; scene detection found 15 cuts, and the 3 shots shorter than 10 s that the grid missed were read as one extra sheet
  frames: yt-dlp stream URL (<=1080p) seeked with ffmpeg
  crop: published stills cropped to the slide area (crop=1406:792:31:145), removing the camera inset and the dark frame
acquired: '2026-11-23'
---

# Stills manifest (hand-picked)

Each still was chosen from the contact sheets and then read at full resolution (1920x1080). The readings below were made by viewing the pixels; the source page carries the verified transcriptions. The webinar is a screen-shared slide talk with Chase's camera inset on the right, followed by a Q&A in which audience questions appear as banners under the survey slide. Reviewed and not cut: the LangSmith promotional video that opens the recording (0:00–1:55: animated logos, product-UI mock-ups of a trace, an Engine fix and an LLM Gateway, the "Every Company Owns Its Intelligence" card), the full-camera intro (1:57–2:18), the title slide, section cards ("What is a persistent agent?", "How to build persistent agents?", "Owning your intelligence", "New in LangSmith"), the text-only recap slides of 12:20–16:40 whose bullets Chase reads out, and the survey slide with QR code that stays up from 33:50 to the end. Six Q&A frames (34:35, 36:30, 38:10, 39:40, 41:15, 44:10) were cut to the scratchpad only to read the askers' names and question texts for the transcript fixes; they are not kept here.

## 01 · 3:25 · From LLMs to persistent agents
- File: `01-03m25-from-llms-to-persistent-agents.png` · [3:25](https://www.youtube.com/watch?v=GojQtxCT3dg&t=205s)
- A rising curve of five S-shaped steps: LLMs → Tool Calling → Reasoning Models → Coding Agents → Persistent Agents, with "(We are here)" pointing at the start of the last step. **Not published**: the narration names the same five steps in the same order.

## 02 · 4:15 · Four names for persistent agents
- File: `02-04m15-four-names-for-persistent-agents.png` · [4:15](https://www.youtube.com/watch?v=GojQtxCT3dg&t=255s)
- Collage of four cards: LangChain blog "Introducing ambient agents" (tags "Harrison's In the Loop", "LangGraph"; Harrison Chase, January 14, 2025, 6 min); a post by Dylan Patel (@dylan522p): "Persistent Agents are the next unlock of AI usage / Our spend on AI is now 45% persistent agents / Unfortunately for Anthropic, Claude Tags sucks / OpenAI's Slack agent is even worse"; a dark card "Building always-on agents: Always-on agents run indefinitely, deciding how and when to act across many sessions. This guide walks through their core primitives and how they fit together." (publisher not shown; Chase attributes it to Anthropic); and "Proactive AI Agents: Definition, Core Components, and Business Value", Productivity, by the team at Slack, January 30th, 2026. **Published.**

## 03 · 4:40 · The characteristics of a persistent agent
- File: `03-04m40-characteristics-of-a-persistent-agent.png` · [4:40](https://www.youtube.com/watch?v=GojQtxCT3dg&t=280s)
- '"Persistent agent" is a new noun defined by the following traits.' Four empty cards: Goal oriented · Always on · Accumulates context over time · Multi-player and multi-surface. **Not published**: the narration names the four traits; the cards carry no further text.

## 04 · 5:45 · Tasks vs goals
- File: `04-05m45-tasks-vs-goals.png` · [5:45](https://www.youtube.com/watch?v=GojQtxCT3dg&t=345s)
- "Persistent agents execute a responsibility." Task: "Write this email" → Done. Goal: "Maintain a blog" → a loop emitting "Pick a topic", "Draft a post", "Reply to readers". Below: Action → Outcome; Bounded → Ongoing. **Published.**

## 05 · 7:25 · Goal design
- File: `05-07m25-goal-design.png` · [7:25](https://www.youtube.com/watch?v=GojQtxCT3dg&t=445s)
- "Design goals around feedback loops." Before: one agent per account (Sales rep → Account A / B / C agents, each with its own Learnings). After: one agent per motion (Sales rep → Outbounding and Early-stage deal progression agents, each with shared Learnings across accounts A, B, C), fed "Account context" by "Context-gathering agents". **Published.**

## 06 · 7:58 · Always on
- File: `06-07m58-always-on.png` · [7:58](https://www.youtube.com/watch?v=GojQtxCT3dg&t=478s)
- "React to events and crons - not messages." Proactive agent triggers: Real-world events (New email; Pull request opened), Developer schedules (Nightly memory update; Weekly stale PR sweep), Agent schedules (Follow up tomorrow; Daily brief you asked for), all feeding "Agent"; a loop labelled "schedules its own" runs from the agent back to Agent schedules. **Published.**

## 07 · 8:28 · Learns over time
- File: `07-08m28-learns-over-time.png` · [8:28](https://www.youtube.com/watch?v=GojQtxCT3dg&t=508s)
- Subtitle repeats the previous slide's "React to events and crons - not messages". "The memory lifecycle": Seed → Memory (AGENTS.md, contacts.md, voice.md, projects.md) → Agent proposes → Feedback → Agent acts → Outcomes; Feedback and Outcomes feed "Dreaming: background job that updates memory", which writes back to Memory. **Published.**

## 08 · 8:45 · Multi-player
- File: `08-08m45-multi-player.png` · [8:45](https://www.youtube.com/watch?v=GojQtxCT3dg&t=525s)
- "Works alongside humans (many at the same time)." A Slack-style message from "Robin AGENT", 4:03 PM: Review requested, langchainplus#65558 (GitHub), "fix(ui): preserve agent work timer across navigation", by @Sam Crowder, +62 −20 in 5 non-test files, robin/action-timer → main, Auto-merge enabled, Reviewers: @Mason reviewing; buttons "I'll review" / "Dismiss"; "Web thread". **Not published**: illustrates a spoken point with one message; no claim beyond it.

## 09 · 9:02 · Multi-surface
- File: `09-09m02-multi-surface.png` · [9:02](https://www.youtube.com/watch?v=GojQtxCT3dg&t=542s)
- "Access the same intelligence from multiple places." The same Slack message beside a desktop app "Robin" (sidebar: New, Skills, Connections, Automations, Pull Requests; pinned "Review Agent Server category"; recent threads incl. "Persistent agents blog post", "LongMemEval benchmark ove…", "Evaluate robin/ai-sdr sellability", "Data fabric definition"; prompt "What should we work on?"). **Not published**: product screenshot of a spoken point.

## 10 · 10:25 · Behavior comes from the whole system
- File: `10-10m25-behavior-comes-from-the-whole-system.png` · [10:25](https://www.youtube.com/watch?v=GojQtxCT3dg&t=625s)
- Model (Capabilities; Reasoning and judgment) + Harness, highlighted (Tools and execution; State and interactions) + Context (Instructions and facts; Feedback and memory). **Not published**: the narration covers all three layers with the same content.

## 11 · 12:05 · LangChain Deep Agents
- File: `11-12m05-langchain-deep-agents.png` · [12:05](https://www.youtube.com/watch?v=GojQtxCT3dg&t=725s)
- Deep Agents Harness → Execution Environment (Filesystem, Sandboxes); Context Management (Skills, Memory, Summarization, Context offloading, Prompt caching); Steering (Human-in-the-loop); Delegation (Planning, Subagents). **Not published**: the same four groups are already published from the Interrupt NYC keynote (still 4 there), and the narration lists the items.

## 12 · 18:05 · An agent runtime
- File: `12-18m05-an-agent-runtime.png` · [18:05](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1085s)
- Dark diagram, eight numbered steps. Your app (users, channels, other agents) → Front door (takes every message, applies your policy) → Queue (one turn at a time per session, in order) → Execution (Your agent: your code, your harness; frees its worker while the session waits); Session state (conversation, progress and history, kept durable); Scheduler (crons, reminders and wake-ups); Recovery (carries on after crashes and deploys); Live stream (every event out, rejoin after a drop); Environment (sandbox and files, tied to the session); outside: Models and tools (your keys, your MCPs), Sandboxes (run model-written code). Around it: Deploys and versions, Tracing and metrics, Identity and secrets, Scaling. Runs in: Managed, Your cloud, Self-hosted. Legend 1–8 and "Dashed line: after a crash or a deploy, recovery puts the work back in the queue". **Published.**

## 13 · 19:35 · LangSmith makes building always-on agents easy
- File: `13-19m35-langsmith-always-on-agents.png` · [19:35](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1175s)
- "LangSmith makes building always-on agents that complete work, easy." Agent needs (Long-running; Tools and agents; Browser, files, code; Memory; Channels; Triggers) mapped to LangSmith: Agent Server, Task queue, Checkpoints, MCP + A2A, Agent Auth, Custom auth, Sandboxes, Allowlists, Snapshots, Context Hub, Threads, Memory store, Slack adapter, Streaming, Cron jobs, Webhooks. **Not published**: a product inventory, most items spoken; the runtime diagram (12) and the Managed Deep Agents slide (14) carry the architecture.

## 14 · 20:35 · Managed Deep Agents on LangSmith
- File: `14-20m35-managed-deep-agents.png` · [20:35](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1235s)
- Your project (agent.py, tools/ └ mcp.py; instructions.md, skills/, memory.py; schedules/, channels/ └ slack.py; sandbox/) → `mda deploy` → Managed Deep Agents on LangSmith: Agent Server (runs the Deep Agents harness; threads and streaming runs), Context Hub (instructions and skills; durable memory), Schedules and channels (cron jobs; runs started from Slack), Sandbox (isolated filesystem and shell). **Published.**

## 15 · 21:55 · Test the agent responsibility
- File: `15-21m55-test-the-agent-responsibility.png` · [21:55](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1315s)
- "A background agent often does the right thing by waiting, so those decisions need evals too." Output: "This message looks good." Test the decisions around it: Same event returns → Does it avoid duplicate outreach? No useful signal → Does it stay quiet? Human has not approved → Does it wait? Access is revoked → Does it stop acting? **Published.**

## 16 · 22:35 · Grade traces against a rubric
- File: `16-22m35-grade-traces-against-a-rubric.png` · [22:35](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1355s)
- "Give subject matter experts a rubric to grade traces against." Trace: Trigger = Account event; Context = Launch and prior outreach; Decision = Draft, then wait for review. Rubric: Was the signal relevant? Was the research grounded? Was the next step useful? Did the boundaries hold? **Published.**

## 17 · 23:05 · Evaluate missed opportunities + noise
- File: `17-23m05-missed-opportunities-and-noise.png` · [23:05](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1385s)
- 2x2, rows Acts / Stays quiet, columns Worth acting on / Not worth acting on: Useful action (surfaces a relevant opportunity); Noise (repeats a known product launch); Missed opportunity (ignores a timely customer need); Useful silence (nothing has changed that matters). **Published.**

## 18 · 23:38 · Turn observed failures into regression tests
- File: `18-23m38-observed-failures-into-regression-tests.png` · [23:38](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1418s)
- "Each failure you catch in production becomes a test, so it stays fixed when you change the prompt or the model." Sample traces (actual behavior, including non-actions) → Review a rubric (human judgment against explicit criteria; labelled "LangSmith annotation queues") → Keep useful cases (build an eval dataset from recurring failures) → Compare changes (prompt, model, harness, or context) → back to Sample traces. **Published.**

## 19 · 24:02 · Governed behavior: Governance
- File: `19-24m02-intended-observed-governed.png` · [24:02](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1442s)
- Section card: "Governed behavior / Governance", three boxes Runtime · Improvement · Governance (highlighted: "What is the agent allowed to do?"). **Not published**: navigation; the earlier cards for Runtime and Improvement show only their own box's text.

## 20 · 24:25 · A prompt can't enforce a rule
- File: `20-24m25-a-prompt-cant-enforce-a-rule.png` · [24:25](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1465s)
- Prompt only: Agent: "Do not send without approval" - - → Email API, labelled "Relies on the model holding back". Enforced action path: Agent → Identity, policy and approval ("Denies any call that fails a check") → Email API. **Published.**

## 21 · 25:05 · Permissions depend on the context
- File: `21-25m05-permissions-depend-on-the-context.png` · [25:05](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1505s)
- Who is acting? + What action? + On which surface? Private DM: Potentially allowed (personal email, within the person's granted scope). Shared channel: Not inherited (posting there doesn't grant access to personal email). **Not published**: the narration gives the same DM / shared-channel example and the same three questions.

## 22 · 27:25 · LangSmith is built for and powered by agents
- File: `22-27m25-langsmith-built-for-and-powered-by-agents.png` · [27:25](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1645s)
- "LangSmith provides the foundation for companies to own and control their agent systems." Agent Runtime: Open Source (deepagents, langgraph, langchain) and LangSmith (Agent Server, Managed Agents, Fleet, Sandboxes). Agent Improvement: LangSmith (Engine, Observability, Evaluation, Fine Tuning; SmithDB beneath). Agent Governance: LangSmith (LLM Gateway, Tool Gateway). **Published.**

## 23 · 30:25 · Trace data controls
- File: `23-30m25-trace-data-controls.png` · [30:25](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1825s)
- "New in LangSmith. Trace data controls. Manage who can access sensitive trace data." Bullets: control who can see trace inputs and outputs (i.e., user messages and model responses); manage team-by-team permissions with user groups; set trace-level access policies using metadata. Screenshot: a trace of "patient_intake_agent" (14.24s, 11.77K tokens / $0.0432) with ChatAnthropic calls (claude-sonnet-5-5) and tools lookup_patient_record, check_insurance_eligibility, schedule_appointment; Input "No inputs", Output "No outputs"; metadata environment production, agent_version 2.4.1, clinic_id clinic_0142, intake_channel web_chat. Slide counter "35". **Not published**: the narration reads out the three bullets and describes the masked view.

## 24 · 32:15 · LangSmith for Coding Agents
- File: `24-32m15-langsmith-for-coding-agents.png` · [32:15](https://www.youtube.com/watch?v=GojQtxCT3dg&t=1935s)
- "Reporting built for coding agents that ties their spend to the PRs they produce." Dashboard for "Robin" (Coding; GitHub Connected; Last 7 days): LLM cost $21.3K (49.5B tokens, ↑39% vs. previous 7d); Cost / merged PR $34.65 ($4.97 direct · 614 merged PRs, ↓62% vs. previous 7d); Cache rate 93% (45.6B of 49.3B input tokens, ↓1 pts vs. previous 7d); Time to merge 5 hrs (89% merge rate · 614 of 692 reso…, ↓92% vs. previous 7d); Threads 22.8K (avg $1.00 / thread, ↑34% vs. previous 7d); Turns / thread 2.9 (67.2K turns, ↑1% vs. previous 7d). Cost over time by model, Nov 9–16, stacked bars up to about $4K a day; legend claude-opus-5-5, gpt-6.1-sol, gpt-6.1-terra, gpt-6-astra, claude-sonnet-5-5, claude-fable-5-1, gemini-4-carbon, typesafe/jev-1.13.0, Other. Read from a 2x zoom of the frame. **Published.**

## 25 · 33:35 · LangSmith Tool Gateway
- File: `25-33m35-langsmith-tool-gateway.png` · [33:35](https://www.youtube.com/watch?v=GojQtxCT3dg&t=2015s)
- "Secure, governed tool use for agents." Agents and clients: Agents (LangGraph, Deep Agents, Managed agents); Coding agents (Claude Code, Codex, Cursor); Your backend (calls for end users) → Tool Gateway in LangSmith: Identify (user, agent or profile) → Attach token (stored in LangSmith) → Apply policy (deny or HITL) → Forward + log (to the MCP server); "Reads credential" → Connections (tokens stored and refreshed); "Records call" → Tool call traces (audit log on Enterprise) → Your tools: Built-in tools (Parallel, Google, and more); Remote servers (any MCP server, by URL); Private servers (in your network, via Tunnels). **Published.**
