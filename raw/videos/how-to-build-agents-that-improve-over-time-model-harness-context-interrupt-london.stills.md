---
title: 'How to Build Agents That Improve Over Time: Model, Harness, Context | Interrupt London'
video_id: xy_7SzwsIjM
url: https://www.youtube.com/watch?v=xy_7SzwsIjM
channel: LangChain
duration: '20:20'
transcript: how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london.md
stills_dir: ../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/
stills_count: 46
extractor:
  model: gemini-3.8-flash
  processing: static
  resolution: default
  processing_rounds: 0
  frame_rule: end of display window minus 1s
  frames: 46 frames by stream seek, no download
acquired: '2026-10-30'
usage:
  total_tokens: 118713
  total_input_tokens: 111308
  total_cached_tokens: 0
  total_output_tokens: 5048
  total_thought_tokens: 2357
  total_tool_use_tokens: 0
notes: |
  Machine-read by gemini-3.8-flash; unverified. Stills are gitignored (raw/**/*.png).
  At Process, view each PNG, correct the reading against the pixels, and
  publish the selected stills as webp under wiki/assets/<source-page-slug>/.
---

# Stills: How to Build Agents That Improve Over Time: Model, Harness, Context | Interrupt London

Machine-read by `gemini-3.8-flash` (static processing) on 2026-10-30. **Unverified**: view each PNG and correct the reading before it reaches the wiki.

## 01 · [0:32] Building agents that improve over time

- Kind: slide
- On screen: 0:32–0:32 · still taken at 0:32
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/01-00m32-building-agents-that-improve-over-time.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=32s

On-screen content (machine-read):

```text
Building agents that improve over time
Harrison Chase
Co-founder & CEO, LangChain
```

Adds vs. narration (machine-read): nothing beyond the narration

## 02 · [0:41] What is an agent?

- Kind: slide
- On screen: 0:33–0:42 · still taken at 0:41
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/02-00m41-what-is-an-agent.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=41s

On-screen content (machine-read):

```text
What is an agent?
```

Adds vs. narration (machine-read): Introduces a geometric isometric cube illustration representing an agent architecture.

## 03 · [0:50] What is an agent? - Model

- Kind: diagram
- On screen: 0:43–0:51 · still taken at 0:50
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/03-00m50-what-is-an-agent-model.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=50s

On-screen content (machine-read):

```text
What is an agent?
MODEL
Astra, Sonnet, Gemini, etc.
```

Adds vs. narration (machine-read): Points to the central core sphere inside the agent cube architecture.

## 04 · [1:04] Model

- Kind: chart
- On screen: 0:52–1:05 · still taken at 1:04
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/04-01m04-model.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=64s

On-screen content (machine-read):

```text
Model
Coding
Price | $/M tokens (blended 3:1) | log scale
```

Adds vs. narration (machine-read): Displays an empirical scatter plot comparing coding capabilities against token cost across various foundation models.

## 05 · [1:18] What is an agent? - Harness

- Kind: diagram
- On screen: 1:14–1:19 · still taken at 1:18
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/05-01m18-what-is-an-agent-harness.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=78s

On-screen content (machine-read):

```text
What is an agent?
MODEL
Astra, Sonnet, Gemini, etc.
HARNESS
Claude Code, Codex, Deep Agents, PI, etc.
```

Adds vs. narration (machine-read): Shows the harness enclosing the model within the agent architecture diagram.

## 06 · [1:41] What is a harness?

- Kind: diagram
- On screen: 1:20–1:42 · still taken at 1:41
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/06-01m41-what-is-a-harness.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=101s

On-screen content (machine-read):

```text
What is a harness?
Context Injection: Prompts, Memory, Skills, Conversation -> Model
Control: Compaction, Orchestration, Reloop loops -> Model
Model (Reasons -> Decides) -> Action: Calls bash, Tools, MCP -> Results back to context
Model -> Persist: Filesystem, Git, Progress files
Model -> Observe & Verify: Browser screenshots, Test results, Logs
```

Adds vs. narration (machine-read): Maps the exact components and feedback loops surrounding the model in an agent harness.

## 07 · [2:12] deepagents

- Kind: diagram
- On screen: 1:46–2:13 · still taken at 2:12
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/07-02m12-deepagents.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=132s

On-screen content (machine-read):

```text
deepagents
Execution Environment: Filesystem | Sandboxes
Context Management: Skills | Memory | Summarization | Context offloading | Prompt caching
Steering: Human-in-the-loop
Delegation: Planning | Subagents
```

Adds vs. narration (machine-read): Categorizes deep agent architectural capabilities into four structured tiers.

## 08 · [2:38] What is an agent? - Context

- Kind: diagram
- On screen: 2:14–2:39 · still taken at 2:38
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/08-02m38-what-is-an-agent-context.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=158s

On-screen content (machine-read):

```text
What is an agent?
MODEL
Astra, Sonnet, Gemini, etc.
HARNESS
Claude Code, Codex, Deep Agents, PI, etc.
CONTEXT
Markdown, Notion, etc.
```

Adds vs. narration (machine-read): Adds the context layer entering the agent harness and model.

## 09 · [2:48] How do agents improve over time?

- Kind: slide
- On screen: 2:40–2:49 · still taken at 2:48
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/09-02m48-how-do-agents-improve-over-time.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=168s

On-screen content (machine-read):

```text
How do agents improve over time?
They can improve in any of these three dimensions
MODEL | HARNESS | CONTEXT
```

Adds vs. narration (machine-read): Categorizes improvement dimensions into Model, Harness, and Context.

## 10 · [2:51] How do agents improve over time? - Manually

- Kind: diagram
- On screen: 2:50–2:52 · still taken at 2:51
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/10-02m51-how-do-agents-improve-over-time-manually.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=171s

On-screen content (machine-read):

```text
How do agents improve over time?
They can improve in any of these three dimensions
MODEL | HARNESS | CONTEXT
They can improve either:
MANUALLY (Human driven)
```

Adds vs. narration (machine-read): Introduces concentric feedback loop rings around the agent cube, starting with manual improvement.

## 11 · [3:20] How do agents improve over time? - Full spectrum

- Kind: diagram
- On screen: 3:20–3:20 · still taken at 3:20
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/11-03m20-how-do-agents-improve-over-time-full-spectrum.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=200s

On-screen content (machine-read):

```text
How do agents improve over time?
They can improve in any of these three dimensions
MODEL | HARNESS | CONTEXT
They can improve either:
MANUALLY (Human driven)
HUMAN-IN-THE-LOOP (AI driven, but human approval)
FULLY AUTOMATED
```

Adds vs. narration (machine-read): Presents three concentric tiers of automation for agent improvement.

## 12 · [3:22] MODEL

- Kind: slide
- On screen: 3:21–3:23 · still taken at 3:22
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/12-03m22-model.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=202s

On-screen content (machine-read):

```text
MODEL
```

Adds vs. narration (machine-read): nothing beyond the narration

## 13 · [3:27] Model - Updating weights

- Kind: slide
- On screen: 3:24–3:28 · still taken at 3:27
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/13-03m27-model-updating-weights.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=207s

On-screen content (machine-read):

```text
Model
• Models improve by updating weights
```

Adds vs. narration (machine-read): nothing beyond the narration

## 14 · [3:42] Model - Multiple models

- Kind: diagram
- On screen: 3:29–3:43 · still taken at 3:42
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/14-03m42-model-multiple-models.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=222s

On-screen content (machine-read):

```text
Model
• Models improve by updating weights
• Agents use multiple models
• Choose which to update
```

Adds vs. narration (machine-read): Illustrates peripheral model nodes positioned around the central agent core.

## 15 · [3:58] Model - Human-initiated

- Kind: diagram
- On screen: 3:44–3:59 · still taken at 3:58
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/15-03m58-model-human-initiated.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=238s

On-screen content (machine-read):

```text
Model
• Models improve by updating weights
• Agents use multiple models
• Choose which to update
• Usually human-initiated
```

Adds vs. narration (machine-read): Adds a human actor targeting specific model nodes for updates.

## 16 · [4:06] Model - Fine-Tuning and RL

- Kind: diagram
- On screen: 4:00–4:07 · still taken at 4:06
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/16-04m06-model-fine-tuning-and-rl.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=246s

On-screen content (machine-read):

```text
Model
• Models improve by updating weights
• Agents use multiple models
• Choose which to update
• Usually human-initiated
• Supervised Fine-Tuning or Reinforcement Learning
SUPERVISED FINE-TUNING
REINFORCEMENT LEARNING
```

Adds vs. narration (machine-read): Diagrams the two training pathways applied to the model weights.

## 17 · [4:31] Supervised Fine-Tuning

- Kind: diagram
- On screen: 4:08–4:32 · still taken at 4:31
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/17-04m31-supervised-fine-tuning.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=271s

On-screen content (machine-read):

```text
Supervised Fine-Tuning
Take traces -> Filter -> Good option for simpler tasks -> Model update
```

Adds vs. narration (machine-read): Visualizes the pipeline funnel from raw traces through a filter to model fine-tuning.

## 18 · [4:53] LangSmith Fine-Tuning

- Kind: diagram
- On screen: 4:33–4:54 · still taken at 4:53
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/18-04m53-langsmith-fine-tuning.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=293s

On-screen content (machine-read):

```text
LangSmith Fine-Tuning
pip install smithtune
LangSmith (Tracing project: Trajectories -> User messages, Model responses, Tool calls + results)
SmithTune CLI:
01 Trace selection
02 Data preprocessing
03 Model training (Fireworks AI, baseten)
04 Model evaluation
Output: Optimized model
Your coding agent
```

Adds vs. narration (machine-read): Specifies CLI architecture and third-party training providers (Fireworks AI, Baseten) used in SmithTune.

## 19 · [5:50] Reinforcement Learning

- Kind: diagram
- On screen: 5:09–5:51 · still taken at 5:50
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/19-05m50-reinforcement-learning.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=350s

On-screen content (machine-read):

```text
Reinforcement Learning
Agent -> Rollouts -> Environment -> Scores (0.31, 0.64, 0.12, 0.47, 0.92, 0.28) -> Train on the scores, run again
• Good for complicated agents
• Harder to do
• Can start with SFT, then RL
```

Adds vs. narration (machine-read): Depicts an RL rollout scoring bar graph alongside key takeaways.

## 20 · [5:52] HARNESS

- Kind: slide
- On screen: 5:52–5:53 · still taken at 5:52
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/20-05m52-harness.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=352s

On-screen content (machine-read):

```text
HARNESS
```

Adds vs. narration (machine-read): nothing beyond the narration

## 21 · [6:00] Harness - Logic

- Kind: slide
- On screen: 5:54–6:01 · still taken at 6:00
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/21-06m00-harness-logic.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=360s

On-screen content (machine-read):

```text
Harness
• Change logic (code, tools, prompt)
```

Adds vs. narration (machine-read): nothing beyond the narration

## 22 · [6:11] Harness - Process

- Kind: diagram
- On screen: 6:02–6:12 · still taken at 6:11
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/22-06m11-harness-process.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=371s

On-screen content (machine-read):

```text
Harness
• Change logic (code, tools, prompt)
Process:
1. Look at a bunch of traces -> 2. Identify issues -> 3. Make changes -> (repeats)
```

Adds vs. narration (machine-read): Outlines a three-step cyclical harness improvement process.

## 23 · [6:25] Harness - Human-in-the-loop

- Kind: diagram
- On screen: 6:13–6:26 · still taken at 6:25
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/23-06m25-harness-human-in-the-loop.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=385s

On-screen content (machine-read):

```text
Harness
• Change logic (code, tools, prompt)
• Want a human-in-the-loop
Process:
1. Look at a bunch of traces -> 2. Identify issues -> 3. Make changes
```

Adds vs. narration (machine-read): Inserts a human reviewer into the harness iteration cycle.

## 24 · [7:10] LangSmith Engine

- Kind: diagram
- On screen: 6:27–7:11 · still taken at 7:10
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/24-07m10-langsmith-engine.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=430s

On-screen content (machine-read):

```text
LangSmith Engine
• Deep Agents in a sandbox with:
  • LangSmith CLI
  • Skills
  • Subagents
  • Prompt
• Create clusters of issues
• Suggests fixes, things to add to dataset, evals to create
Cycle:
Monitor (Cluster and diagnose issues) -> Build (Propose fix via PR) -> Test (Create eval and add to eval dataset) -> Deploy (Ship tested changes) -> Monitor
```

Adds vs. narration (machine-read): Details the automated CI/CD-style loop (Monitor -> Build -> Test -> Deploy) for agent logic maintenance.

## 25 · [7:13] CONTEXT

- Kind: slide
- On screen: 7:12–7:14 · still taken at 7:13
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/25-07m13-context.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=433s

On-screen content (machine-read):

```text
CONTEXT
```

Adds vs. narration (machine-read): nothing beyond the narration

## 26 · [7:24] Context - Properties

- Kind: slide
- On screen: 7:15–7:25 · still taken at 7:24
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/26-07m24-context-properties.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=444s

On-screen content (machine-read):

```text
Context
• Easiest to update! (It's just text)
• User or org level
```

Adds vs. narration (machine-read): nothing beyond the narration

## 27 · [7:46] Context - Process

- Kind: diagram
- On screen: 7:26–7:47 · still taken at 7:46
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/27-07m46-context-process.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=466s

On-screen content (machine-read):

```text
Context
• Easiest to update! (It's just text)
• User or org level
• Like harness but at context layer
Process:
1. Look at a bunch of traces -> 2. Identify issues -> 3. Make changes
```

Adds vs. narration (machine-read): Shows the same iterative trace-review process applied directly to context documents.

## 28 · [7:54] Hex - Product Overview

- Kind: screen
- On screen: 7:48–7:55 · still taken at 7:54
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/28-07m54-hex-product-overview.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=474s

On-screen content (machine-read):

```text
HEX
The fastest way to sharpen agents on your data
Unified context | Observable everywhere | Improves with use
```

Adds vs. narration (machine-read): Presents Hex's marketing landing page highlighting unified context and observable agent telemetry.

## 29 · [8:15] Hex - Improves with use

- Kind: screen
- On screen: 7:56–8:16 · still taken at 8:15
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/29-08m15-hex-improves-with-use.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=495s

On-screen content (machine-read):

```text
HEX
Improves with use
Fixes find you | Every change, evaluated | Your work is context
Suggestions | Q3 Enterprise Launch Readiness
```

Adds vs. narration (machine-read): Highlights Hex's automated review features: finding context gaps and evaluating every change.

## 30 · [8:37] Profound

- Kind: screen
- On screen: 8:17–8:38 · still taken at 8:37
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/30-08m37-profound.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=517s

On-screen content (machine-read):

```text
Profound
Constantly synthesis data into BrandRecords
Collect Personal Records informed by interactions with your AI Marketer
Personal memory: Your role, Your objectives, Your projects
```

Adds vs. narration (machine-read): Displays Profound's interface for synthesizing interactions into brand records and personal memory.

## 31 · [9:09] OpenWiki OSS

- Kind: screen
- On screen: 8:47–9:10 · still taken at 9:09
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/31-09m09-openwiki-oss.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=549s

On-screen content (machine-read):

```text
OpenWiki Platform
OSS | 7 source references
Graph | Pages
Agent Middleware, Interrupted Tools, and Multimodal State
```

Adds vs. narration (machine-read): Shows OpenWiki's knowledge graph and documentation interface built from codebase analysis.

## 32 · [9:13] Commonalities

- Kind: slide
- On screen: 9:11–9:14 · still taken at 9:13
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/32-09m13-commonalities.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=553s

On-screen content (machine-read):

```text
Commonalities
```

Adds vs. narration (machine-read): Displays the three agent cubes (Model, Harness, Context) side-by-side.

## 33 · [9:43] Commonalities - Traces and Evals

- Kind: diagram
- On screen: 9:15–9:44 · still taken at 9:43
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/33-09m43-commonalities-traces-and-evals.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=583s

On-screen content (machine-read):

```text
Commonalities
Traces
Evals
```

Adds vs. narration (machine-read): Identifies Traces and Evals as the foundational shared layers beneath Model, Harness, and Context.

## 34 · [9:45] TRACES

- Kind: slide
- On screen: 9:45–9:46 · still taken at 9:45
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/34-09m45-traces.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=585s

On-screen content (machine-read):

```text
TRACES
```

Adds vs. narration (machine-read): nothing beyond the narration

## 35 · [10:43] Traces - Hierarchy

- Kind: diagram
- On screen: 9:47–10:44 · still taken at 10:43
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/35-10m43-traces-hierarchy.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=643s

On-screen content (machine-read):

```text
Traces
• Exact inputs, outputs, sequence
Runs
Traces
Thread
Trajectories
```

Adds vs. narration (machine-read): Defines the hierarchical trace ontology: individual Runs compose Traces, Traces compose Threads, and Threads yield Trajectories.

## 36 · [11:15] Traces - Characteristics

- Kind: diagram
- On screen: 10:45–11:16 · still taken at 11:15
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/36-11m15-traces-characteristics.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=675s

On-screen content (machine-read):

```text
Traces
• Exact inputs, outputs, sequence
• Traces are a new type of data -> ingest, store, query
• Failures are semantic
• Queries are different
Runs -> Traces -> Thread -> Trajectories -> Database
```

Adds vs. narration (machine-read): Identifies semantic failures and non-traditional queries as defining attributes of trace datasets.

## 37 · [11:34] SMITHDB

- Kind: diagram
- On screen: 11:17–11:35 · still taken at 11:34
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/37-11m34-smithdb.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=694s

On-screen content (machine-read):

```text
SMITHDB
```

Adds vs. narration (machine-read): Illustrates incoming event streams converging into the SmithDB storage architecture.

## 38 · [11:58] LangSmith Semantic Search UI

- Kind: screen
- On screen: 11:46–11:59 · still taken at 11:58
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/38-11m58-langsmith-semantic-search-ui.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=718s

On-screen content (machine-read):

```text
chat-langchain external
Filter: patrons about streaming
Threads | Traces | Runs
human: Current LangGraph docs... -> ai: StateGraph has...
human: Current LangGraph docs... -> ai: The `updates` stream...
```

Adds vs. narration (machine-read): Shows a live LangSmith interface performing natural-language semantic filtering over agent execution traces.

## 39 · [12:06] EVALS

- Kind: slide
- On screen: 12:00–12:07 · still taken at 12:06
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/39-12m06-evals.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=726s

On-screen content (machine-read):

```text
EVALS
```

Adds vs. narration (machine-read): nothing beyond the narration

## 40 · [12:22] Evals - The new PRD

- Kind: diagram
- On screen: 12:08–12:23 · still taken at 12:22
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/40-12m22-evals-the-new-prd.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=742s

On-screen content (machine-read):

```text
Evals
• Evals are the new PRD
```

Adds vs. narration (machine-read): Visualizes an evaluation checklist document positioned alongside the agent cube.

## 41 · [12:46] Evals - Defining good

- Kind: slide
- On screen: 12:24–12:47 · still taken at 12:46
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/41-12m46-evals-defining-good.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=766s

On-screen content (machine-read):

```text
Evals
• Evals are the new PRD
• Define what good looks like
```

Adds vs. narration (machine-read): nothing beyond the narration

## 42 · [13:10] Evals - Triad

- Kind: diagram
- On screen: 12:48–13:11 · still taken at 13:10
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/42-13m10-evals-triad.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=790s

On-screen content (machine-read):

```text
Evals
• Evals are the new PRD
• Define what good looks like
• Building evals is hard!
Realistic inputs | Simulation environment | Good answer
```

Adds vs. narration (machine-read): Breaks down evaluation complexity into realistic inputs, simulation environment, and defining good answers.

## 43 · [14:55] Evals - Realistic inputs

- Kind: diagram
- On screen: 13:12–14:56 · still taken at 14:55
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/43-14m55-evals-realistic-inputs.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=895s

On-screen content (machine-read):

```text
Evals
• Evals are the new PRD
• Define what good looks like
• Building evals is hard!
  • What are realistic inputs
Realistic inputs | Simulation environment | Good answer
```

Adds vs. narration (machine-read): Highlights the user-input component of the evaluation triad.

## 44 · [15:01] Evals - Full breakdown

- Kind: diagram
- On screen: 14:57–15:02 · still taken at 15:01
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/44-15m01-evals-full-breakdown.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=901s

On-screen content (machine-read):

```text
Evals
• Evals are the new PRD
• Define what good looks like
• Building evals is hard!
  • What are realistic inputs
  • What does good look like?
  • What does a "simulation environment" look like?
Realistic inputs | Simulation environment | Good answer
```

Adds vs. narration (machine-read): Enumerates all three core challenges in building agent evaluations.

## 45 · [17:26] LangSmith Red Teaming UI

- Kind: screen
- On screen: 16:44–17:27 · still taken at 17:26
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/45-17m26-langsmith-red-teaming-ui.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=1046s

On-screen content (machine-read):

```text
Controlled eval hook import would break frontend integration
Evidence & Reasoning | Code Diff
Expected:
The current official Vue documentation does not establish a useStream export...
Why the Judge Decided This:
This was a realistic developer request for an exact current import...
```

Adds vs. narration (machine-read): Shows an automated red-teaming report detecting a code hallucination with judge rationale and code diffs.

## 46 · [20:10] How to build agents that improve over time

- Kind: diagram
- On screen: 18:54–20:11 · still taken at 20:10
- File: `../images/how-to-build-agents-that-improve-over-time-model-harness-context-interrupt-london/46-20m10-how-to-build-agents-that-improve-over-time.png`
- At this moment: https://www.youtube.com/watch?v=xy_7SzwsIjM&t=1210s

On-screen content (machine-read):

```text
How to build agents that improve over time
Run agent -> Get feedback -> See what happened (trace) -> Add eval datapoint -> Suggest change to agent -> Run agent
Suggest change to agent:
• Update model weights
• Update harness code
• Update context
```

Adds vs. narration (machine-read): Summarizes the complete continuous improvement flywheel connecting runtime execution, traces, evals, and agent updates.
