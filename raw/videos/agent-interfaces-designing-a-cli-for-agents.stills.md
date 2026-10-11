---
title: 'Agent Interfaces: designing a CLI for agents'
video_id: dXDhjhnt2EY
url: https://www.youtube.com/watch?v=dXDhjhnt2EY
channel: MotherDuck
duration: '17:56'
transcript: agent-interfaces-designing-a-cli-for-agents.md
stills_dir: ../images/agent-interfaces-designing-a-cli-for-agents/
stills_count: 30
extractor:
  model: gemini-3.8-flash
  processing: static
  resolution: default
  processing_rounds: 0
  frame_rule: end of display window minus 1s
  frames: 0 frames by stream seek, 30 from a full download (fallback)
acquired: '2026-10-08'
usage:
  total_tokens: 104982
  total_input_tokens: 98196
  total_cached_tokens: 0
  total_output_tokens: 3910
  total_thought_tokens: 2876
  total_tool_use_tokens: 0
notes: |
  Machine-read by gemini-3.8-flash; unverified. Stills are gitignored (raw/**/*.png).
  At Process, view each PNG, correct the reading against the pixels, and
  publish the selected stills as webp under wiki/assets/<source-page-slug>/.
---

# Stills: Agent Interfaces: designing a CLI for agents

Machine-read by `gemini-3.8-flash` (static processing) on 2026-10-08. **Unverified**: view each PNG and correct the reading before it reaches the wiki.

## 01 · [0:37] Interacting with Agents

- Kind: slide
- On screen: 0:26–0:38 · still taken at 0:37
- File: `../images/agent-interfaces-designing-a-cli-for-agents/01-00m37-interacting-with-agents.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=37s

On-screen content (machine-read):

```text
Agents have become a common way to interact with products and tools.
How do you know whether an interface to an agent actually works well?
```

Adds vs. narration (machine-read): Frames the central question of the talk regarding evaluating agent interfaces.

## 02 · [0:46] Introduction

- Kind: slide
- On screen: 0:39–0:47 · still taken at 0:46
- File: `../images/agent-interfaces-designing-a-cli-for-agents/02-00m46-introduction.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=46s

On-screen content (machine-read):

```text
Quack, quack, ...
Adithya Krishnan
Software Engineer
𝕏 @krish_adi_
in adithyakrishnan
```

Adds vs. narration (machine-read): Provides the speaker's name and social media handles.

## 03 · [0:53] Duck SQooL

- Kind: slide
- On screen: 0:48–0:54 · still taken at 0:53
- File: `../images/agent-interfaces-designing-a-cli-for-agents/03-00m53-duck-sqool.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=53s

On-screen content (machine-read):

```text
... Duck SQooL ...
```

Adds vs. narration (machine-read): nothing beyond the narration

## 04 · [0:59] What is MotherDuck?

- Kind: slide
- On screen: 0:55–1:00 · still taken at 0:59
- File: `../images/agent-interfaces-designing-a-cli-for-agents/04-00m59-what-is-motherduck.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=59s

On-screen content (machine-read):

```text
What is MotherDuck?
A serverless Data Platform built on DuckDB...
```

Adds vs. narration (machine-read): nothing beyond the narration

## 05 · [1:20] What is DuckDB?

- Kind: code
- On screen: 1:01–1:21 · still taken at 1:20
- File: `../images/agent-interfaces-designing-a-cli-for-agents/05-01m20-what-is-duckdb.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=80s

On-screen content (machine-read):

```text
What is DuckDB?
Analytical database Engine
pip install duckdb
import duckdb
cursor = duckdb.connect()
cursor.execute('CREATE TABLE tbl AS SELECT * FROM data/*parquet;')
df = cursor.execute('SELECT * FROM tbl;').fetchdf()
```

Adds vs. narration (machine-read): Demonstrates basic Python syntax for connecting and querying DuckDB.

## 06 · [1:37] MotherDuck Cloud Architecture

- Kind: diagram
- On screen: 1:25–1:38 · still taken at 1:37
- File: `../images/agent-interfaces-designing-a-cli-for-agents/06-01m37-motherduck-cloud-architecture.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=97s

On-screen content (machine-read):

```text
...scales to support complex apps and data.
DuckDB on laptop -> MotherDuck Cloud:
- Control Plane
- Compute
- Storage
```

Adds vs. narration (machine-read): Illustrates how local DuckDB offloads compute, storage, and control plane tasks to MotherDuck.

## 07 · [1:53] Using MotherDuck?

- Kind: code
- On screen: 1:39–1:54 · still taken at 1:53
- File: `../images/agent-interfaces-designing-a-cli-for-agents/07-01m53-using-motherduck.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=113s

On-screen content (machine-read):

```text
Using MotherDuck?
cursor = duckdb.connect('md:mydatabase')
cursor.execute('CREATE TABLE tbl AS SELECT * FROM data/*parquet;')
[Pointer to 'md:mydatabase']
```

Adds vs. narration (machine-read): Shows how switching the database connection string to 'md:...' points DuckDB to MotherDuck.

## 08 · [2:09] MotherDuck User Interfaces

- Kind: slide
- On screen: 1:55–2:10 · still taken at 2:09
- File: `../images/agent-interfaces-designing-a-cli-for-agents/08-02m09-motherduck-user-interfaces.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=129s

On-screen content (machine-read):

```text
MotherDuck
Everywhere you work...
there is a duck for you...
DuckDB (CLI)
MotherDuck (CLI)
MotherDuck UI
DuckDB (Python, Javascript, rust, go, Java...)
Human User Interfaces.
```

Adds vs. narration (machine-read): Catalogs the human-facing user interfaces and client libraries available.

## 09 · [2:25] How do agents interface?

- Kind: slide
- On screen: 2:21–2:26 · still taken at 2:25
- File: `../images/agent-interfaces-designing-a-cli-for-agents/09-02m25-how-do-agents-interface.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=145s

On-screen content (machine-read):

```text
How do agents interface?
```

Adds vs. narration (machine-read): nothing beyond the narration

## 10 · [2:41] UI/UX To AI/AX

- Kind: slide
- On screen: 2:27–2:42 · still taken at 2:41
- File: `../images/agent-interfaces-designing-a-cli-for-agents/10-02m41-ui-ux-to-ai-ax.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=161s

On-screen content (machine-read):

```text
UI/UX
To
AI/AX
```

Adds vs. narration (machine-read): Defines the transition from human UI/UX to AI Agent Interfaces and Agent Experience.

## 11 · [3:25] MotherDuck's Interfaces for Agents

- Kind: diagram
- On screen: 3:00–3:26 · still taken at 3:25
- File: `../images/agent-interfaces-designing-a-cli-for-agents/11-03m25-motherduck-s-interfaces-for-agents.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=205s

On-screen content (machine-read):

```text
MotherDuck's Interfaces
Agent Harnesses (OpenAI, Claude, Gemini, Perplexity, LangChain, Hugging Face) ->
MotherDuck-CLI (Local Compute Env / Sandbox) -> MotherDuck
MCP-Server-MotherDuck -> MotherDuck
```

Adds vs. narration (machine-read): Maps agent harnesses to MotherDuck via both CLI and MCP server pathways.

## 12 · [4:16] Designing the CLI for Agents

- Kind: slide
- On screen: 3:55–4:17 · still taken at 4:16
- File: `../images/agent-interfaces-designing-a-cli-for-agents/12-04m16-designing-the-cli-for-agents.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=256s

On-screen content (machine-read):

```text
Designing the CLI to bring a Duck Agent to Your Data
```

Adds vs. narration (machine-read): nothing beyond the narration

## 13 · [5:14] Agent Interface Evaluation Framework

- Kind: diagram
- On screen: 4:18–5:15 · still taken at 5:14
- File: `../images/agent-interfaces-designing-a-cli-for-agents/13-05m14-agent-interface-evaluation-framework.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=314s

On-screen content (machine-read):

```text
EVAL framework ???
Choose useful tasks -> Expose capabilities -> Observe how it's used -> Measure the outcome
Measure the outcome -> Improve Interface -> Expose capabilities
```

Adds vs. narration (machine-read): Details the iterative evaluation loop used to refine agent CLI interfaces.

## 14 · [6:19] Agent Interface Evaluation Framework (Revisited)

- Kind: diagram
- On screen: 5:56–6:20 · still taken at 6:19
- File: `../images/agent-interfaces-designing-a-cli-for-agents/14-06m19-agent-interface-evaluation-framework-revisited.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=379s

On-screen content (machine-read):

```text
EVAL framework ???
Choose useful tasks -> Expose capabilities -> Observe how it's used -> Measure the outcome
Measure the outcome -> Improve Interface -> Expose capabilities
```

Adds vs. narration (machine-read): nothing beyond the narration

## 15 · [6:34] Inspired by the following work...

- Kind: slide
- On screen: 6:21–6:35 · still taken at 6:34
- File: `../images/agent-interfaces-designing-a-cli-for-agents/15-06m34-inspired-by-the-following-work.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=394s

On-screen content (machine-read):

```text
Inspired by the following work...
Tau Bench
Evaluate tool-using agents through realistic user interactions, final-state correctness, and reliability across repeated trials.
ToolSandbox
Test stateful workflows with required steps ("milestones"), forbidden actions ("minefields"), and missing-information scenarios.
AXI (Agent eXperience Interface)
A design framework for experiments with CLI output, errors, help, and discoverability.
and a few more...
```

Adds vs. narration (machine-read): Lists foundational research benchmarks and frameworks informing agent CLI evaluation.

## 16 · [7:10] How does that translate to the CLI?

- Kind: diagram
- On screen: 6:49–7:11 · still taken at 7:10
- File: `../images/agent-interfaces-designing-a-cli-for-agents/16-07m10-how-does-that-translate-to-the-cli.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=430s

On-screen content (machine-read):

```text
How does that translate to the CLI?
Tasks + Test Data -> AI Agent -> Answer + Traces -> Grading -> Results -> (improve interface) -> CLI
AI Agent -> CLI <-> MotherDuck -> Expected outcome -> Grading
```

Adds vs. narration (machine-read): Illustrates the grading pipeline comparing agent actions against expected outcomes.

## 17 · [8:18] Grading using the AXI

- Kind: slide
- On screen: 7:38–8:19 · still taken at 8:18
- File: `../images/agent-interfaces-designing-a-cli-for-agents/17-08m18-grading-using-the-axi.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=498s

On-screen content (machine-read):

```text
Grading using the AXI
• Token efficient output : Use less tokens for a task
• Minimal schemas : Show fewer fields by default
• Truncation : Capability to shorten large outputs
• Aggregates : Include summarise for quick digestible information
• Structured errors : Standardize error objects and exit codes
• Explicit empty states : 0 results are explicit
• Context disclosure : Suggest follow up commands after results
• Consistent help : Make sub command help concise and uniform
```

Adds vs. narration (machine-read): Lists design heuristics and evaluation criteria under the Agent Experience Interface rubric.

## 18 · [8:47] Grading using the AXI (Revisited)

- Kind: slide
- On screen: 8:38–8:48 · still taken at 8:47
- File: `../images/agent-interfaces-designing-a-cli-for-agents/18-08m47-grading-using-the-axi-revisited.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=527s

On-screen content (machine-read):

```text
Grading using the AXI
• Token efficient output : Use less tokens for a task
• Minimal schemas : Show fewer fields by default
• Truncation : Capability to shorten large outputs
• Aggregates : Include summarise for quick digestible information
• Structured errors : Standardize error objects and exit codes
• Explicit empty states : 0 results are explicit
• Context disclosure : Suggest follow up commands after results
• Consistent help : Make sub command help concise and uniform
```

Adds vs. narration (machine-read): nothing beyond the narration

## 19 · [9:47] Grading using the AXI (Revisited 2)

- Kind: slide
- On screen: 9:20–9:48 · still taken at 9:47
- File: `../images/agent-interfaces-designing-a-cli-for-agents/19-09m47-grading-using-the-axi-revisited-2.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=587s

On-screen content (machine-read):

```text
Grading using the AXI
• Token efficient output : Use less tokens for a task
• Minimal schemas : Show fewer fields by default
• Truncation : Capability to shorten large outputs
• Aggregates : Include summarise for quick digestible information
• Structured errors : Standardize error objects and exit codes
• Explicit empty states : 0 results are explicit
• Context disclosure : Suggest follow up commands after results
• Consistent help : Make sub command help concise and uniform
```

Adds vs. narration (machine-read): nothing beyond the narration

## 20 · [10:42] Grading using the AXI (Revisited 3)

- Kind: slide
- On screen: 10:33–10:43 · still taken at 10:42
- File: `../images/agent-interfaces-designing-a-cli-for-agents/20-10m42-grading-using-the-axi-revisited-3.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=642s

On-screen content (machine-read):

```text
Grading using the AXI
• Token efficient output : Use less tokens for a task
• Minimal schemas : Show fewer fields by default
• Truncation : Capability to shorten large outputs
• Aggregates : Include summarise for quick digestible information
• Structured errors : Standardize error objects and exit codes
• Explicit empty states : 0 results are explicit
• Context disclosure : Suggest follow up commands after results
• Consistent help : Make sub command help concise and uniform
```

Adds vs. narration (machine-read): nothing beyond the narration

## 21 · [11:15] Grading using the AXI (Revisited 4)

- Kind: slide
- On screen: 11:13–11:16 · still taken at 11:15
- File: `../images/agent-interfaces-designing-a-cli-for-agents/21-11m15-grading-using-the-axi-revisited-4.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=675s

On-screen content (machine-read):

```text
Grading using the AXI
• Token efficient output : Use less tokens for a task
• Minimal schemas : Show fewer fields by default
• Truncation : Capability to shorten large outputs
• Aggregates : Include summarise for quick digestible information
• Structured errors : Standardize error objects and exit codes
• Explicit empty states : 0 results are explicit
• Context disclosure : Suggest follow up commands after results
• Consistent help : Make sub command help concise and uniform
```

Adds vs. narration (machine-read): nothing beyond the narration

## 22 · [11:45] Principles Found on the Way

- Kind: slide
- On screen: 11:40–11:46 · still taken at 11:45
- File: `../images/agent-interfaces-designing-a-cli-for-agents/22-11m45-principles-found-on-the-way.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=705s

On-screen content (machine-read):

```text
And, some principles we found on the way
• Discovery : Command structure instructive on available products
• Context : Upfront context on what can be achieved, how to use it and where to get more info
• Non-interactive : Headless login for example
• Structured outputs : Gives the agent the ability to traverse output
• Instructive error : What should be done differently
```

Adds vs. narration (machine-read): Summarizes key practical guidelines learned while adapting CLIs for agents.

## 23 · [12:42] Principles Found on the Way (Revisited)

- Kind: slide
- On screen: 12:33–12:43 · still taken at 12:42
- File: `../images/agent-interfaces-designing-a-cli-for-agents/23-12m42-principles-found-on-the-way-revisited.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=762s

On-screen content (machine-read):

```text
And, some principles we found on the way
• Discovery : Command structure instructive on available products
• Context : Upfront context on what can be achieved, how to use it and where to get more info
• Non-interactive : Headless login for example
• Structured outputs : Gives the agent the ability to traverse output
• Instructive error : What should be done differently
```

Adds vs. narration (machine-read): nothing beyond the narration

## 24 · [13:34] Principles Found on the Way (Revisited 2)

- Kind: slide
- On screen: 13:13–13:35 · still taken at 13:34
- File: `../images/agent-interfaces-designing-a-cli-for-agents/24-13m34-principles-found-on-the-way-revisited-2.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=814s

On-screen content (machine-read):

```text
And, some principles we found on the way
• Discovery : Command structure instructive on available products
• Context : Upfront context on what can be achieved, how to use it and where to get more info
• Non-interactive : Headless login for example
• Structured outputs : Gives the agent the ability to traverse output
• Instructive error : What should be done differently
```

Adds vs. narration (machine-read): nothing beyond the narration

## 25 · [13:45] Following the tokens...

- Kind: slide
- On screen: 13:36–13:46 · still taken at 13:45
- File: `../images/agent-interfaces-designing-a-cli-for-agents/25-13m45-following-the-tokens.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=825s

On-screen content (machine-read):

```text
Following the tokens...
```

Adds vs. narration (machine-read): nothing beyond the narration

## 26 · [14:03] Example Prompt

- Kind: slide
- On screen: 13:47–14:04 · still taken at 14:03
- File: `../images/agent-interfaces-designing-a-cli-for-agents/26-14m03-example-prompt.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=843s

On-screen content (machine-read):

```text
Create a scheduled flight in motherduck for every monday for ~/monday_flight/main.py
```

Adds vs. narration (machine-read): Provides an example natural language task prompt given to an agent.

## 27 · [14:48] MotherDuck CLI Help Output

- Kind: screen
- On screen: 14:05–14:49 · still taken at 14:48
- File: `../images/agent-interfaces-designing-a-cli-for-agents/27-14m48-motherduck-cli-help-output.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=888s

On-screen content (machine-read):

```text
>>> motherduck
Usage: motherduck [options] [command]
MotherDuck CLI (v1.3.5-2026-09-160)
Options:
  -v, --version Output the version number
  -h, --help display help for command
Commands:
  login [options] Authenticate via OAuth device flow; use --headless for browserless login or set MOTHERDUCK_TOKEN
  new [options] Create a new MotherDuck account and organization, and save the new token
  dive Create and manage Dives, interactive visualizations over your data
  flight Create and manage Flights, Python data pipelines that run on a schedule or on demand
  guide Create and manage Guides, Markdown documents that capture context and guidance about your data
  help [command] display help for command
[Highlight on dive, flight, guide: Product Discoverability]
```

Adds vs. narration (machine-read): Shows the CLI root help output designed with discoverability for agent consumption.

## 28 · [15:57] Agent First from the Start?

- Kind: slide
- On screen: 15:36–15:58 · still taken at 15:57
- File: `../images/agent-interfaces-designing-a-cli-for-agents/28-15m57-agent-first-from-the-start.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=957s

On-screen content (machine-read):

```text
Agent first from the start?
```

Adds vs. narration (machine-read): nothing beyond the narration

## 29 · [16:54] motherduck new Command

- Kind: screen
- On screen: 16:29–16:55 · still taken at 16:54
- File: `../images/agent-interfaces-designing-a-cli-for-agents/29-16m54-motherduck-new-command.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=1014s

On-screen content (machine-read):

```text
>>> motherduck new
MotherDuck created a new account and organization in aws-us-east-1.
The CLI saved the new token as your login credentials.
To claim the organization, sign up with your email address at this URL:
https://app.motherduck.com/claim-org?inviteTo=abcdefgh-xxxx-xxxx-hell-o-oo00000000
The URL is valid for 72 hours.
To show the URL again, run 'motherduck new claim'.
An account for your agent.
```

Adds vs. narration (machine-read): Demonstrates CLI account provisioning designed to allow agents immediate headless access.

## 30 · [17:27] One-Prompt MotherDuck Access

- Kind: slide
- On screen: 17:14–17:28 · still taken at 17:27
- File: `../images/agent-interfaces-designing-a-cli-for-agents/30-17m27-one-prompt-motherduck-access.png`
- At this moment: https://www.youtube.com/watch?v=dXDhjhnt2EY&t=1047s

On-screen content (machine-read):

```text
Fetch https://new.motherduck.com
```

Adds vs. narration (machine-read): Shows the minimal URL prompt used to provision MotherDuck access.
