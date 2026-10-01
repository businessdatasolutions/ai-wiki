---
title: Why Your AI Agent Fails in Production (And How to Catch It)
video_id: wPdoZRbvaF4
url: https://www.youtube.com/watch?v=wPdoZRbvaF4
channel: Google Cloud Tech
duration: '26:07'
transcript: why-your-ai-agent-fails-in-production-and-how-to-catch-it.md
stills_dir: ../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/
stills_count: 38
extractor:
  model: gemini-3.8-flash
  processing: static
  resolution: default
  processing_rounds: 0
  frame_rule: end of display window minus 1s
acquired: '2026-10-01'
usage:
  total_tokens: 153251
  total_input_tokens: 142897
  total_cached_tokens: 0
  total_output_tokens: 7784
  total_thought_tokens: 2570
  total_tool_use_tokens: 0
notes: |
  Machine-read by gemini-3.8-flash; unverified. Stills are gitignored (raw/**/*.png).
  At Process, view each PNG, correct the reading against the pixels, and
  publish the selected stills as webp under wiki/assets/<source-page-slug>/.
---

# Stills: Why Your AI Agent Fails in Production (And How to Catch It)

Machine-read by `gemini-3.8-flash` (static processing) on 2026-10-01. **Unverified**: view each PNG and correct the reading before it reaches the wiki.

## 01 · [0:12] Four Steps to Build Evals

- Kind: slide
- On screen: 0:09–0:13 · still taken at 0:12
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/01-00m12-four-steps-to-build-evals.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=12s

On-screen content (machine-read):

```text
1 Antigravity meets Docshound (a LangGraph agent)
2 Standardizing (to reuse) our eval toolsets
3 Translating quality definitions into metrics
4 Visualizing evaluation results
```

Adds vs. narration (machine-read): Outlines the four-step agenda for the episode's evaluation process.

## 02 · [0:17] Step 1: High-Level Architecture & Execution Flow

- Kind: diagram
- On screen: 0:14–0:18 · still taken at 0:17
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/02-00m17-step-1-high-level-architecture-execution-flow.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=17s

On-screen content (machine-read):

```text
1. High-Level Architecture & Execution Flow
Docshound is an autonomous documentation gap agent built with LangGraph (StateGraph), deployed on Google Cloud Vertex AI Agent Runtime (Reasoning Engine) and Cloud Run, and driven by Gemini 3.7 Flash.
Run Request -> llm_decide Gemini 3.7 Router
action: research (Fetch GitHub Issues & PRs)
action: analyze (Gemini 3.7 Cluster & Gap Analysis)
action: search_docs (Inspect Repo Docs & Coverage)
action: store (Persist State & Audit Trail)
action: draft (Web-Browser UI 8080) -> Completed / Ready for Review -> Human-in-the-Loop Review -> Approve Finding -> Generate Unified Diff Patch -> Create GitHub Pull Request
```

Adds vs. narration (machine-read): Displays the complete architectural execution flow and state transitions of DocsHound.

## 03 · [0:25] Step 2: The Battle-Tested Baseline

- Kind: slide
- On screen: 0:19–0:26 · still taken at 0:25
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/03-00m25-step-2-the-battle-tested-baseline.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=25s

On-screen content (machine-read):

```text
OPEN-SOURCE EVALUATION TOOLKIT
Production Baseline
The Battle-Tested Baseline
Pre-Built Scripts & CLI (Ready-to-run telemetry converters & adaptors) [ZERO GLUE CODE]
Guided Evaluation Workflow (1. Scenario Input -> 2. Harvest Traces -> 3. Rubric Scoring) [STEP-BY-STEP]
Native GenAI Eval Bridge (Vertex AI GenAI Evaluation Service & Agent Platform) [ENTERPRISE]
Don't build from scratch. Start with a production baseline. [INSTANT LAUNCH]
TIME-TO-EVALUATION
FROM SCRATCH: WEEKS
Custom Parsers | Manual Judges | Bespoke UI
WITH BASELINE: 1 SINGLE HOUR
BASELINE INGESTION: ADK-Tested
"Could we use it for other agentic frameworks?"
LangGraph, CrewAI & custom agents via universal OTel
SETUP EFFORT COMPRESSION: Weeks -> 1 Single Hour
```

Adds vs. narration (machine-read): Quantifies the reduction in evaluation setup time from weeks to one hour using the baseline toolkit.

## 04 · [0:32] Step 3: Translating Quality Definitions into Metrics

- Kind: code
- On screen: 0:27–0:33 · still taken at 0:32
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/04-00m32-step-3-translating-quality-definitions-into-metrics.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=32s

On-screen content (machine-read):

```text
# Option 2: Custom LLM Judges (Evaluated with Structured Sub-Rubrics for Metric-Grid)
docshound_documentation_quality:
  kind: custom_llm_judge
  prompt_template: |
    You are evaluating the quality of an AI-generated documentation update or developer answer for DocsHound.
    User Question: {prompt}
    Agent Response: {response}
    Evaluation Criteria:
    1. Structure & Formatting: Uses clear Markdown headings, bullet points, and code backticks/fenced blocks.
    2. Actionability: Provides concrete, copy-pasteable configuration keys, commands, or code snippets.
    3. Technical Precision: Explains the "why" and "how" with accurate developer terminology.
    Score 1 (Pass) if the response is well-structured, actionable, and ready for a documentation PR.
    Score 0 (Fail) if it is poorly formatted, vague, or contains confusing instructions.
    Return ONLY valid JSON with keys "score" and "explanation". The "score" must be a float and "explanation" a string.
    Example:
    {
      "score": 1.0,
      "explanation": "{\"rubric\": {\"Structure & Formatting\": {\"verdict\": true, \"reasoning\": \"Uses clear...
```

Adds vs. narration (machine-read): Shows the exact YAML configuration defining custom LLM judge sub-rubrics and scoring criteria.

## 05 · [0:40] Step 4: Agent Evaluation Dashboard

- Kind: screen
- On screen: 0:35–0:41 · still taken at 0:40
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/05-00m40-step-4-agent-evaluation-dashboard.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=40s

On-screen content (machine-read):

```text
{Agent Evaluation} backend
At a glance: ESTIMATED COST $0.0003 | WALL-CLOCK 3.0s | CACHE HIT RATE 0% | TOTAL TOKENS 585
LLM-judge metrics radar chart
Score table:
docshound_general_quality: 0.48 | Low
docshound_documentation_quality: 0.50 | Low
docshound_groundedness_and_attribution: 0.67 | Mixed
docshound_confidence_calibration: 1 | Pass
docshound_langgraph_trajectory: 1 | Pass
docshound_graph_validity: 1 | Pass
docshound_markdown_structure: 0.34 | Low
docshound_citation_fidelity: 1 | Pass
Metrics over time line chart
```

Adds vs. narration (machine-read): Presents summary evaluation metrics, pass/fail status, radar breakdown, and historical trend charts.

## 06 · [1:39] DocsHound Overview

- Kind: slide
- On screen: 1:34–1:40 · still taken at 1:39
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/06-01m39-docshound-overview.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=99s

On-screen content (machine-read):

```text
DocsHound
LangGraph Agent that turns open issues and merged pull requests into grounded, reviewable documentation updates.
WEBSITE: MATTHEWFEROZ.COM
YOUTUBE: @MATTFEROZ
```

Adds vs. narration (machine-read): Defines DocsHound's primary function and author links.

## 07 · [2:01] Gemini Enterprise Agent Platform Integration

- Kind: diagram
- On screen: 1:55–2:02 · still taken at 2:01
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/07-02m01-gemini-enterprise-agent-platform-integration.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=121s

On-screen content (machine-read):

```text
Gemini Enterprise Agent Platform
OPEN-SOURCE & CUSTOM AGENT FRAMEWORKS [UNIVERSAL INGESTION]:
- Agent Development Kit (ADK) [Google Native]
- LangGraph [StateGraph]
- LangChain [Chains & Tools]
- LlamaIndex [Data & RAG]
- CrewAI [Multi-Agent]
- AG2 (AutoGen) [Multi-Agent]
- Any Python Agent [Universal OTel]
DEPLOYS TO ->
MANAGED PLATFORM SERVICES [PLATFORM CORE]:
- Agent Runtime [Execution]
- Agent Retrieval & RAG [Grounding]
- Evaluations & Quality [Evals SDK]
- Context & Memory Bank [State]
- Code Execution [Sandbox]
- Cloud Observability [OTel]
```

Adds vs. narration (machine-read): Shows which open-source agent frameworks map into managed services on Gemini Enterprise Agent Platform.

## 08 · [2:26] DocsHound Agent Tool Architecture

- Kind: diagram
- On screen: 2:18–2:27 · still taken at 2:26
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/08-02m26-docshound-agent-tool-architecture.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=146s

On-screen content (machine-read):

```text
DocsHound Agent Tool Architecture
LangGraph coordinates the guarded loop, each action invokes observable tools
LANGGRAPH AGENT LOOP -> LLM ROUTER
- Research: research_repo, research_pull_requests, docs-repo activity (optional)
- Analyse: cluster_issues, Groups evidence into gaps and shipped changes
- Search docs: search_official_docs, Checks coverage and recommends an action
- Draft: draft_review_documents, Writes reviewable Markdown
- Store: Finalizes graph state, No external tool
HUMAN CONTROLLED APPLICATION WORKFLOW:
Edit -> Approve Markdown -> Preview file & Patch -> PR -> Create GitHub branch
```

Adds vs. narration (machine-read): Illustrates the agent tool loop and the human-in-the-loop review workflow.

## 09 · [2:43] DocsHound UI: Agent Timeline & Gaps Discovered

- Kind: screen
- On screen: 2:32–2:44 · still taken at 2:43
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/09-02m43-docshound-ui-agent-timeline-gaps-discovered.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=163s

On-screen content (machine-read):

```text
DocsHound
AGENT TIMELINE (Run 24175614):
50 issues | 30 PRs | 24 of 24 pages read | 8 findings
- Run started
- Agent decision - research
- research_repo complete (1644.5 ms)
- research_pull_requests complete (3855.9 ms)
- 50 issues fetched, 30 merged pull requests fetched
- Agent decision - analyze
- search_official_docs (12316.4 ms)
- 24 documentation pages inspected
- Agent decision - draft
- draft_review_documents (17162.3 ms)
- Documentation finding discovered
GAPS DISCOVERED:
- Release 2.7.1 (HUMAN REVIEW DRAFT: Release Notes: ADK Python 2.7.1)
- forward_safety_settings_from_generate_content_config to the Live API
```

Adds vs. narration (machine-read): Demonstrates the execution timeline, performance durations, and gap discovery results in the web UI.

## 10 · [2:57] DocsHound Finding Detail

- Kind: screen
- On screen: 2:51–2:58 · still taken at 2:57
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/10-02m57-docshound-finding-detail.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=177s

On-screen content (machine-read):

```text
DocsHound Finding | google/adk-python
support audio_stream_end for realtime input
Review repository evidence -> Check existing documentation -> Refine the Markdown -> Approve document -> Create docs PR
DOCUMENTATION COVERAGE: No matching page found
Proposed action: Create a focused documentation page.
Candidate documentation pages:
- LlmAgent Single-Turn Mode
- ReflectAndRetryModelPlugin
- Dynamic Node Scheduling
- Function Nodes
- JoinNode
- LlmAgent Task Mode
- RemoteA2Agent Task Mode
- App
REPOSITORY EVIDENCE: Merged PR #6699 feat: support audio_stream_end for realtime input
```

Adds vs. narration (machine-read): Shows DocsHound identifying missing documentation topics against candidate repository pages.

## 11 · [3:01] GitHub Merged PR Reference

- Kind: screen
- On screen: 2:59–3:02 · still taken at 3:01
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/11-03m01-github-merged-pr-reference.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=181s

On-screen content (machine-read):

```text
google / adk-python
feat: support audio_stream_end for realtime input #6699
Merged into main
Summary: ADK supports sending audio_stream_end signal in realtime input for Gemini Live API.
Testing Plan: All unit tests pass locally.
```

Adds vs. narration (machine-read): Shows the underlying GitHub pull request analyzed by DocsHound to generate documentation.

## 12 · [3:25] DocsHound Markdown Review and Approval

- Kind: screen
- On screen: 3:15–3:26 · still taken at 3:25
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/12-03m25-docshound-markdown-review-and-approval.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=205s

On-screen content (machine-read):

```text
DocsHound Finding
Edit the Markdown before approving
## Realtime Input: audio_stream_end Support
## Overview
## Shipped Changes
## Sources
[Reject] [Approve and open]
Rendered view | Markdown view
NEXT STEP: Send this to the documentation repository
Upstream documentation repository: google/adk-python
[Prepare documentation PR]
```

Adds vs. narration (machine-read): Demonstrates the draft markdown editing and PR staging interface.

## 13 · [3:33] DocsHound Repository Change Review

- Kind: screen
- On screen: 3:28–3:34 · still taken at 3:33
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/13-03m33-docshound-repository-change-review.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=213s

On-screen content (machine-read):

```text
Review the repository change
Upstream documentation repository: google/adk-python
Base branch: main
New branch: docshound/realtime-input-audio-stream-end-support-24175614
Exact patch diff view
[Publish upstream PR]
Pull request #6768 is ready! [Open pull request]
```

Adds vs. narration (machine-read): Displays the generated patch diff and pull request submission confirmation.

## 14 · [3:38] GitHub PR Created by DocsHound

- Kind: screen
- On screen: 3:35–3:39 · still taken at 3:38
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/14-03m38-github-pr-created-by-docshound.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=218s

On-screen content (machine-read):

```text
google / adk-python
docs: Realtime Input: audio_stream_end Support #6768
Open | 1 commit | 1 file changed
Documentation update: Generated documentation update based on PR #6699
Evidence: Merged PR #6699 feat: support audio_stream_end for realtime input
```

Adds vs. narration (machine-read): Confirms successful automated PR creation on GitHub.

## 15 · [3:48] DocsHound Architecture with Observability

- Kind: diagram
- On screen: 3:40–3:49 · still taken at 3:48
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/15-03m48-docshound-architecture-with-observability.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=228s

On-screen content (machine-read):

```text
DocsHound Agent Tool Architecture
LangGraph coordinates the guarded loop, each action invokes observable tools
LLM ROUTER: Research, Analyse, Search docs, Draft, Store
HUMAN CONTROLLED APPLICATION WORKFLOW
OBSERVABILITY:
- OpenTelemetry records one trace
- OpenInference labels AGENT / TOOL / LLM spans
- LangSmith displays it
```

Adds vs. narration (machine-read): Highlights the telemetry and trace instrumentation integration in the architecture.

## 16 · [4:25] Definition: OpenTelemetry (OTel)

- Kind: text-overlay
- On screen: 4:19–4:26 · still taken at 4:25
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/16-04m25-definition-opentelemetry-otel.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=265s

On-screen content (machine-read):

```text
Agent Evaluation Definition
OpenTelemetry (OTel)
An open-source standard designed to capture, format, and transport data about a software system's internal behavior.
It passes data using structural blocks called Spans.
```

Adds vs. narration (machine-read): Defines OpenTelemetry and its use of spans for system behavior data.

## 17 · [4:40] Definition: OpenInference

- Kind: text-overlay
- On screen: 4:36–4:41 · still taken at 4:40
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/17-04m40-definition-openinference.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=280s

On-screen content (machine-read):

```text
Agent Evaluation Definition
OpenInference
While OpenTelemetry provides the pipeline and the structural boxes (Spans), it doesn't standardize application interactions with AI systems.
To solve that, OpenInference extends OTel by assigning consistent semantic tags:
AGENT, TOOL, LLM, RETRIEVER...
```

Adds vs. narration (machine-read): Explains how OpenInference extends OpenTelemetry with AI-specific semantic tags.

## 18 · [4:57] Why OpenInference Matters

- Kind: text-overlay
- On screen: 4:49–4:58 · still taken at 4:57
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/18-04m57-why-openinference-matters.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=297s

On-screen content (machine-read):

```text
Why It Matters?
If your agent emits OpenInference spans, changes in the agentic module do not affect downstream systems that consume from its telemetry (e.g. evaluation).
```

Adds vs. narration (machine-read): Explains that standardized spans decouple agent internal changes from downstream evaluation systems.

## 19 · [6:06] Review Step 1: Prompt and Architecture Mapping

- Kind: diagram
- On screen: 5:58–6:07 · still taken at 6:06
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/19-06m06-review-step-1-prompt-and-architecture-mapping.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=366s

On-screen content (machine-read):

```text
Prompt: Hi AntiGravity, go through the code and understand it before we implement evals
1. High-Level Architecture & Execution Flow diagram
[!] DEVELOPMENT PATTERN: Guide coding agents to understand inner workings & emit user traces for downstream evaluation.
```

Adds vs. narration (machine-read): Summarizes Step 1's goal of prompting an agent to trace and understand architecture.

## 20 · [6:19] Review Step 2: Standardizing Eval Toolsets

- Kind: diagram
- On screen: 6:09–6:20 · still taken at 6:19
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/20-06m19-review-step-2-standardizing-eval-toolsets.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=379s

On-screen content (machine-read):

```text
Evaluation Toolkit: reusable scripts & CLI
Visual Studio Code: trace_converters.py
AGENT COMPATIBILITY:
BEFORE: ADK Only
AFTER (NOW) [Universal OTel]: ADK Agents: ACCEPTED | LangGraph: ACCEPTED | Any OTel Agent: ACCEPTED
```

Adds vs. narration (machine-read): Shows the compatibility expansion from ADK-only to universal OpenInference agents.

## 21 · [6:39] Review Step 4: Visualizing Evaluation Results

- Kind: screen
- On screen: 6:35–6:40 · still taken at 6:39
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/21-06m39-review-step-4-visualizing-evaluation-results.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=399s

On-screen content (machine-read):

```text
{Agent Evaluation} backend dashboard overview, radar metrics, score table, and metrics over time.
```

Adds vs. narration (machine-read): Recaps the final visualization dashboard for evaluation runs.

## 22 · [7:17] Definition: Scenario

- Kind: text-overlay
- On screen: 7:13–7:18 · still taken at 7:17
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/22-07m17-definition-scenario.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=437s

On-screen content (machine-read):

```text
Agent Evaluation Definition
Scenario
A structured, reproducible test case or simulated situation designed to assess an agent's behavior under a specific set of initial conditions and target objectives.
```

Adds vs. narration (machine-read): Defines a scenario in the context of AI agent evaluations.

## 23 · [7:25] DocsHound Scenario JSON

- Kind: code
- On screen: 7:19–7:26 · still taken at 7:25
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/23-07m25-docshound-scenario-json.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=445s

On-screen content (machine-read):

```text
Matt created two reproducible scenarios to prepare to demo DocsHound
File: opencode.json / adk-dan.json
{
  "title": "OpenCode CLI documentation catch-up",
  "source_repository": "anomalyco/opencode",
  "public_issues": 50,
  "public_pull_requests": 30,
  "issues": [...],
  "pull_requests": [...],
  "documentation": [...]
}
```

Adds vs. narration (machine-read): Shows the exact JSON format used to define reproducible test scenarios for DocsHound.

## 24 · [8:34] Google Cloud Console: Agent Platform Deployments

- Kind: screen
- On screen: 8:23–8:35 · still taken at 8:34
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/24-08m34-google-cloud-console-agent-platform-deployments.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=514s

On-screen content (machine-read):

```text
Google Cloud - Gemini Enterprise Agent Platform
Deployments on Agent Runtime
Name: docshound-langgraph-agent
Framework: LangGraph
Dashboard: Overview | Evaluation | Traces | Topology | Security | Sessions | Playground | Memories
Agent latency | Avg turns per session | Agent invocations | Agent request count | Agent error rate
```

Adds vs. narration (machine-read): Demonstrates DocsHound running on Google Cloud's managed Agent Runtime dashboard.

## 25 · [9:59] Target Repositories to Run Against DocsHound

- Kind: screen
- On screen: 9:43–10:00 · still taken at 9:59
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/25-09m59-target-repositories-to-run-against-docshound.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=599s

On-screen content (machine-read):

```text
Repositories to run against DocsHound
- T3 (t3-oss)
- opencode (anomalyco/opencode)
- Pi (earendil-works/pi)
```

Adds vs. narration (machine-read): Lists the three open-source target repositories selected for automated benchmarking.

## 26 · [11:38] agent-eval Toolkit Architecture

- Kind: slide
- On screen: 11:28–11:39 · still taken at 11:38
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/26-11m38-agent-eval-toolkit-architecture.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=698s

On-screen content (machine-read):

```text
agent-eval
A hand-on-shoulder CLI walkthrough of the Vertex AI Generative AI Evaluation Service for ADK agents.
An opinionated Evaluation ToolKit (within Google Professional Services repo) containing pre-built scripts & a guided workflow to drastically accelerate your evaluation setup
Gemini Enterprise Agent Platform GenAI Client in Agent Platform SDK
agents-cli: CLI and tools for building AI agents on Google Cloud
```

Adds vs. narration (machine-read): Details the components and workflow of Google's open-source `agent-eval` toolkit.

## 27 · [11:55] agent-eval Command Workflow

- Kind: diagram
- On screen: 11:47–11:56 · still taken at 11:55
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/27-11m55-agent-eval-command-workflow.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=715s

On-screen content (machine-read):

```text
1 - agent-eval setup (once per shell)
- walks gcloud auth + ADC
- picks your project + location
- enables the Vertex AI API
- binds the autorater IAM role so Vertex can grade your traces
2 - agent-eval init (once per agent)
- auto-detects your local ADK Agent (or FastAPI URL)
- picks metrics - 18 managed (Vertex's catalog)
- AI-drafted custom (binary by default)
- generates tests/eval/dataset.json
3 - agent-eval run (every iteration)
- collect - drives simulate User(SIM) + Interact (DIY)
- score - two-step: Vertex AI GenAI Eval API + Deterministic (local)
- analyze + view Gemini diagnoses what changed, opens a self-contained report.html
```

Adds vs. narration (machine-read): Details the sequential commands and actions in the `agent-eval` lifecycle.

## 28 · [13:55] AntiGravity Execution Summary: Scenario Analysis

- Kind: screen
- On screen: 13:38–13:56 · still taken at 13:55
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/28-13m55-antigravity-execution-summary-scenario-analysis.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=835s

On-screen content (machine-read):

```text
1. Target Repositories & Canonical Documentation Roots:
- Pi Agent | earendil-works/pi | packages/coding-agent/docs
- T3 Code | pingdotgg/t3code | agent/docs
- OpenCode CLI | anomalyco/opencode | packages/web/src/content/docs
2. Execution Summary & Findings:
Each target repository was analyzed with standard reproducible parameters (50 GitHub issues, 30 pull requests, canonical docs resolution, using Gemini-3.7-Flash with Vertex AI Reasoning Engine).
DOCSHOUND EVALUATION RUN SUMMARY: 3 runs, 150 issues, 90 pull requests, 38 official doc pages inspected.
```

Adds vs. narration (machine-read): Presents findings and scraping statistics from running DocsHound across three open-source repositories.

## 29 · [14:23] AntiGravity Generated Evaluation Datasets & Scripts

- Kind: screen
- On screen: 14:12–14:24 · still taken at 14:23
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/29-14m23-antigravity-generated-evaluation-datasets-scripts.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=863s

On-screen content (machine-read):

```text
3. Generated Evaluation Datasets & Scripts
1. Master Eval Dataset:
- data/evals/eval_dataset.json (Combined benchmark dataset containing all findings, coverage analysis, evidence citations, and synthesized Markdown drafts)
2. Target-Specific Run JSONs:
- data/evals/pi_eval_run.json
- data/evals/t3code_eval_run.json
- data/evals/opencode_eval_run.json
3. Execution Scripts:
- demo/eval_pipeline.py
- demo/export_eval_dataset.py
4. Running for Evals (bash commands)
```

Adds vs. narration (machine-read): Enumerates the benchmark datasets and conversion scripts generated by the agent.

## 30 · [16:38] Implementation Plan: Trace Conversion for Agent-Eval

- Kind: diagram
- On screen: 16:10–16:39 · still taken at 16:38
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/30-16m38-implementation-plan-trace-conversion-for-agent-eval.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=998s

On-screen content (machine-read):

```text
LangGraph & OpenInference Trace Conversion for Agent-Eval
Architecture Overview:
DocsHound (LangGraph Agent) -> LangGraph Workflow -> OpenInference / OpenTelemetry Tracing -> OpenInference Trace JSON/JSONL ->
agent-eval (Local PSS Tool) -> dataset.json / Golden Dataset -> OpenInferenceToOtConverter -> Canonical AgentData & Evaluator Row -> data_mapper_agents -> Vertex AI GenAI Eval & Deterministic Metrics -> eval_summary.json & Rich CLI Report
Proposed Changes:
Component 1: agent-eval Core Trace Converters & Data Mapper
Component 2: LangGraph / OpenInference Converter
Component 3: LangGraph Trajectory Validator
```

Adds vs. narration (machine-read): Diagrams the pipeline adapting DocsHound's OpenInference traces for `agent-eval` ingestion.

## 31 · [16:55] Implementation Verification Plan

- Kind: screen
- On screen: 16:49–16:56 · still taken at 16:55
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/31-16m55-implementation-verification-plan.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=1015s

On-screen content (machine-read):

```text
Verification Plan
Automated Tests:
1. Unit & Contract Tests:
pytest test/trace_converters.py
2. DocsHound Trace Generation & Conversion Test:
python -m demo.export_eval_dataset --dry-run
3. End-to-End Evaluation Test:
agent-eval run --dataset data/evals/eval_dataset.json
```

Adds vs. narration (machine-read): Shows test commands ensuring backward compatibility and trace conversion validity.

## 32 · [18:23] AntiGravity Key Accomplishments & Quick Start

- Kind: screen
- On screen: 18:07–18:24 · still taken at 18:23
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/32-18m23-antigravity-key-accomplishments-quick-start.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=1103s

On-screen content (machine-read):

```text
Key Accomplishments:
1. OpenInference / OpenTelemetry Trace Converter (agent-eval)
2. Deterministic & Semantic Metrics Support
3. DocsHound Agent Evaluation Pipeline
4. Testing & Verification: 110/110 unit & CLI tests passing (100% pass rate)
Quick Start: Running Evaluation on DocsHound Traces:
1. Convert OpenInference Traces with Golden Dataset Merging
2. Run Evaluation: agent-eval run --backend vertex-genai --results-dir eval/results
3. Generate Summary and HTML Report
```

Adds vs. narration (machine-read): Confirms passing 110 unit tests and provides exact commands to run the evaluation pipeline.

## 33 · [20:33] eval_config.yaml: Managed Vertex AI Autoraters

- Kind: code
- On screen: 20:24–20:34 · still taken at 20:33
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/33-20m33-eval-config-yaml-managed-vertex-ai-autoraters.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=1233s

On-screen content (machine-read):

```text
# Eval Configuration for DocsHound LangGraph Agent
# 1. Managed Vertex AI Autoraters
metrics:
  - name: question_answering_quality
    kind: managed_vertex_ai
    description: "Vertex AI managed judge evaluating answer completeness, technical clarity, and question fulfillment."
```

Adds vs. narration (machine-read): Shows configuration for native managed Vertex AI question-answering autorater metrics.

## 34 · [20:57] eval_config.yaml: Custom LLM Judges

- Kind: code
- On screen: 20:44–20:58 · still taken at 20:57
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/34-20m57-eval-config-yaml-custom-llm-judges.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=1257s

On-screen content (machine-read):

```text
# 2. Quality & Information Display (Custom LLM Judges)
docshound_documentation_quality:
  kind: custom_llm_judge
  rubric: |
    Evaluate the quality of the DocsHound response as a technical documentation patch or developer answer.
    Criteria:
    - Structure & Formatting: Uses clear Markdown with headings, bullet points, and fenced code blocks.
    - Actionability: Provides concrete, copy-pasteable configuration keys, commands, or code snippets.
    - Technical Precision: Explains the "why" and "how" with accurate developer-centric terminology.
# 3. Groundedness & Confidence (Custom LLM Judges)
docshound_groundedness_and_attribution:
  kind: custom_llm_judge
```

Adds vs. narration (machine-read): Shows the specific rubrics used by the custom LLM judge to evaluate documentation quality.

## 35 · [21:12] eval_config.yaml: Trajectory and Deterministic Checkers

- Kind: code
- On screen: 21:07–21:13 · still taken at 21:12
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/35-21m12-eval-config-yaml-trajectory-and-deterministic-checkers.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=1272s

On-screen content (machine-read):

```text
# 4. LangGraph Inner Workings & Trajectory (Custom LLM Judge)
docshound_langgraph_trajectory:
  kind: custom_llm_judge
  prompt: Evaluate whether the agent's problem-solving trajectory aligns with the DocsHound LangGraph architecture (Research -> Analyze -> Search Official Documentation -> Draft Documentation -> Store Audit Trail).
# 5. Deterministic Python Function Checkers
docshound_graph_validity:
  kind: python_function
  function: validate_langgraph_workflow_trajectory
docshound_markdown_structure:
  kind: python_function
  function: validate_markdown_documentation_structure
docshound_citation_fidelity:
  kind: python_function
  function: validate_citation_fidelity
```

Adds vs. narration (machine-read): Shows custom trajectory checks and deterministic Python validation rules.

## 36 · [22:20] Agent Evaluation HTML Dashboard: Overview

- Kind: screen
- On screen: 22:04–22:21 · still taken at 22:20
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/36-22m20-agent-evaluation-html-dashboard-overview.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=1340s

On-screen content (machine-read):

```text
{Agent Evaluation} backend
At a glance: ESTIMATED COST $0.0003 | WALL-CLOCK 3.0s | CACHE HIT RATE 0% | TOTAL TOKENS 585
LLM-Judge metrics radar chart
Score table:
- docshound_documentation_quality: 0.33 | Low
- docshound_confidence_calibration: 75% | Pass
- docshound_langgraph_trajectory: 1 | Pass
- docshound_graph_validity: 1 | Pass
- docshound_markdown_structure: 0.34 | Low
- docshound_citation_fidelity: 1 | Pass
```

Adds vs. narration (machine-read): Displays the full benchmark score table revealing low documentation quality (0.33) and markdown structure (0.34).

## 37 · [23:12] Per-Question Score Heatmap

- Kind: table
- On screen: 23:04–23:13 · still taken at 23:12
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/37-23m12-per-question-score-heatmap.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=1392s

On-screen content (machine-read):

```text
Question | docshound_documentation_quality | docshound_groundedness_and_attribution | docshound_confidence_calibration | docshound_langgraph_trajectory | docshound_graph_validity | docshound_markdown_structure | docshound_citation_fidelity
docshound_eval_001: How do I configure Redis cache in DocsHound? | 1 (Pass) | - | 100% | 1 | 1 | 0.45 | 1
docshound_eval_002: Where are the documentation sources configured for a repository? | 0 (Low) | - | 0% | 1 | 1 | 0.30 | 1
docshound_eval_003: How does DocsHound instrument OpenTelemetry and LangSmith traces? | 0 (Low) | - | 100% | 1 | 1 | 0.30 | 1
docshound_eval_004: What environment variables are required to connect DocsHound to... | 0 (Low) | - | 100% | 1 | 1 | 0.30 | 1
```

Adds vs. narration (machine-read): Provides a per-question heat map across all seven evaluation metrics.

## 38 · [23:43] Per-Question Deep Dive: docshound_eval_001

- Kind: screen
- On screen: 23:18–23:44 · still taken at 23:43
- File: `../images/why-your-ai-agent-fails-in-production-and-how-to-catch-it/38-23m43-per-question-deep-dive-docshound-eval-001.png`
- At this moment: https://www.youtube.com/watch?v=wPdoZRbvaF4&t=1423s

On-screen content (machine-read):

```text
docshound_eval_001 | How do I configure Redis cache in DocsHound? | [single-turn] 402 tok | 3.0s | 1 tools
RUN-TIME METRICS: TOTAL TOKENS 402 | PROMPT TOKENS 340 | COMPLETION TOKENS 62 | COST $0.0003 | WALL-CLOCK 3.00s | TURN LATENCY 1.20s
STATE & TRAJECTORY: AGENTS INVOLVED: model | MODELS USED: gemini-2.5-flash | TOOL CALL COUNTS: search_documentation x1
CONVERSATION & FINAL RESPONSE
PER-METRIC SCORES & RUBRIC VERDICTS:
- docshound_documentation_quality: Pass 1.00
- docshound_groundedness_and_attribution: FAILED (Autorater error 400: Error rendering metric prompt template)
- docshound_confidence_calibration: Pass 1.00
- docshound_langgraph_trajectory: Pass 1.00
- docshound_graph_validity: Pass 1.00
- docshound_markdown_structure: Low 0.45
- docshound_citation_fidelity: Pass 1.00
```

Adds vs. narration (machine-read): Breaks down individual turn latency, token costs, model prompts, and rubric verdicts for an eval question.

## Skipped

- [06:21–06:33] Review Step 3: Translating Quality Definitions into Metrics: same picture as still 04
