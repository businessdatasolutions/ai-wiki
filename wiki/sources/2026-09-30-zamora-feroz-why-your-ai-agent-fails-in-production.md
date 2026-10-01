---
type: source
kind: video
title: "Why Your AI Agent Fails in Production (And How to Catch It)"
author: ["Google Cloud Tech"]
publisher: "Google Cloud Tech (YouTube), AI Agent Clinic series; hosts Dani Zamora (Google Cloud) and Matthew Feroz (Merge)"
url: "https://www.youtube.com/watch?v=wPdoZRbvaF4"
date_published: 2026-09-30
date_ingested: 2026-10-01
length: "~26:07 minutes (transcript ~251 lines + 14 stills; auto-generated transcript, ASR-cleaned)"
raw: "../../raw/videos/why-your-ai-agent-fails-in-production-and-how-to-catch-it.md"
stills: "../../raw/videos/why-your-ai-agent-fails-in-production-and-how-to-catch-it.stills.md"
tags: [google-cloud, ai-agent-clinic, agent-evaluation, evals, llm-as-judge, autorater, deterministic-checkers, trajectory-evaluation, opentelemetry, openinference, spans, langgraph, langsmith, antigravity, agent-eval, vertex-ai, gemini-enterprise-agent-platform, docshound, observability, scenarios, vibe-check]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: 2026-05-18-wolfe-agent-evaluation-detailed-guide
    via: "Both describe agent evaluation as grading a trajectory and an outcome with several grader families. This episode configures three of them on one LangGraph agent: a managed Vertex AI metric, custom LLM judges, and deterministic Python checks over the span sequence. Wolfe's human graders do not appear."
    confidence: 0.75
  - type: supports
    target: 2025-09-28-husain-ai-evaluations-clearly-explained-50-min
    via: "Both build binary pass/fail LLM judges around what the person who knows the domain calls quality. Husain derives the judges from open and axial coding of production traces and validates them against human labels; here Antigravity drafts them from the source code and a conversation with the developer, and no validation step is shown."
    confidence: 0.7
  - type: supports
    target: 2026-05-09-chase-agent-development-lifecycle
    via: "Both treat traces as the material evals are made from. This episode runs Chase's Test phase on camera: telemetry is made framework-neutral with OpenTelemetry and OpenInference, turned into scenarios and scored, and a run the product's own UI showed as finished scores low on documentation quality."
    confidence: 0.75
  - type: supports
    target: 2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway
    via: "Both present evals as a direction-finder rather than a verdict. Zamora's reading of the low score, that either the agent or the way it is evaluated may need improvement, is the same middle position applied to one's own dashboard."
    confidence: 0.7
  - type: supports
    target: 2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent
    via: "Both start from the gap between 'it seems to work' and a measured score, and both pair deterministic code graders with rubric-based model graders. Anthropic hill-climbs a slide agent on 0-5 judge scores; this episode's custom judges are binary, with a threshold of 1.0."
    confidence: 0.7
---

# Why Your AI Agent Fails in Production (And How to Catch It)

> Manual code tweaking isn't a testing strategy. Here is how to actually evaluate AI agents for production. In this episode of AI Agent Clinic, Google Cloud engineer Dani Zamora and Matthew Feroz (Merge) take DocsHound, an open-source LangGraph agent, and build an end-to-end evaluation pipeline in 60 minutes.
>
> Most autonomous loops look great in local demos but fail silently in production. In this hands-on clinic, we compress weeks of testing setup into one hour by:
> 1. Mapping agent execution flow and inner workings using Antigravity
> 2. Standardizing multi-turn traces with OpenTelemetry & OpenInference (making your evals work across agentic frameworks like ADK, LangGraph, CrewAI, AutoGen, or custom implementations)
> 3. Pairing custom LLM-as-a-judge evaluation rubrics and deterministic checkers for quality and performance assessment
> 4. Additionally, tracking signals like: latency, token usage, and API cost
> 5. Ensuring zero vendor lock-in by building on open-source standards
>
> Along the way, our automated scorecard catches a blind spot: a 33% documentation quality score that while eye-balling the results we initially missed.
>
> *— Channel description, [[Google]] Cloud Tech (links, chapter list and hashtags omitted)*

An episode of Google Cloud Tech's *AI Agent Clinic*. **Dani Zamora**, a Google Cloud engineer and the series host, and **Matthew Feroz**, a developer advocate at Merge, take **DocsHound**, Feroz's open-source [[LangChain|LangGraph]] agent, and build an evaluation pipeline for it against a 60-minute clock. DocsHound reads a GitHub repository's issues and pull requests, finds gaps in its documentation, and drafts documentation changes that a person approves before a pull request is opened.

It earns a source page for two reasons. It is the corpus's first **complete Test phase run on camera on one agent**, from raw telemetry to a scored dashboard, on a framework that is not the vendor's own. And it is the clearest case so far of a video whose **definitions exist only on screen**: the narration names *OpenTelemetry*, *OpenInference* and *scenario*, and the cards define them. Most of the substance below comes from the [Visual canon](#visual-canon).

## TL;DR

- **The problem, as framed.** Without evals, a change is judged by feel. *"If you make changes in your agent and you test a new version, you're going to vibe it, right? You're going to feel like, 'Yeah, it's what looks right.'"* For someone else's agent that does not work: *"there needs to be a way so that we can translate what you have in your mind as quality to something that we can run as actual numbers so that if you change something or if someone else changes something you can always measure those improvements or even regressions."*
- **Step 0: make the traces framework-neutral.** Feroz had already instrumented DocsHound with **OpenTelemetry** and **OpenInference**. The reason given: *"so that whenever we did evaluations, we don't need to redo the work if you change that inner workings."* The definitions are on the cards (entries 4–6 below).
- **Step 1: an agent reads the agent.** [[Antigravity]] analyses DocsHound's source and traces, draws its architecture as a Mermaid diagram, and runs DocsHound against three more repositories (T3 Code, OpenCode and Pi) to produce more **scenarios**: *"in real life what happens is that you need of course more examples to make sure that we have the appropriate data to run evaluation."*
- **Step 2: an existing toolkit, adapted.** Google's open-source **agent-eval** toolkit scaffolds and runs the evals against the Vertex AI evaluation service. It was tested with ADK agents only. During the episode Antigravity writes a LangGraph/OpenInference trace converter so the toolkit can read DocsHound's traces; Zamora calls it a second *"collaboration"*, making the toolkit framework-agnostic.
- **Step 3: metrics drafted by an agent, steered by the developer.** Antigravity proposes a managed Vertex AI metric, four custom LLM judges and three deterministic Python checkers (entries 10–11). Zamora's advice: *"start simple"*, beginning with managed metrics such as tool-use and trajectory quality, *"and then also my biggest recommendation is sitting down with the developer, sitting down with the user of agents for example and seeing what quality means for them."*
- **Quality is not the only signal.** *"We don't only need to measure quality, we also need to measure some things that are like performance based in the sense of latency … token usage, cost."* Feroz's example: before swapping in the strongest model, know how the current, smaller one performs, so the choice is made on data.
- **Step 4: the dashboard and the 0.33.** Documentation quality scores 0.33 and is flagged *Low*. Feroz: *"that's a complete blind spot that I had."* Zamora: *"It can be both ways. Probably your code needs improvement or the way we are evaluating also may need improvement."* The stills show what the 0.33 rests on (entries 12–14; see *Debates*).
- **Are evals for everyone?** Feroz: *"yes and no."* For a solo developer *"what if the model gets better tomorrow? Or what if like the harness changes?"*; *"I think eval[s] are for when you really need the agent to perform [in] production."*

## Visual canon

The episode is a screen-and-slide demo. The narration names terms and tools; the cards, slides and screens carry the definitions, the configuration and the numbers. Each entry below was transcribed from the still and checked against it. Gemini's machine reading was corrected in several places: two framework labels on the platform slide, a function name in the config, the fourth cell of the heatmap (read as *0*, it is empty) and the question in the deep-dive (read as 001, it is 004). It also filled in text cut off at the edge of a scrolled page. The manifest has all 38 stills.

### 1 · The battle-tested baseline

![[assets/2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production/03-00m25-step-2-the-battle-tested-baseline.webp|The Battle-Tested Baseline slide: an open-source evaluation toolkit, and setup time from weeks to a single hour]]

*Still at [0:25](https://www.youtube.com/watch?v=wPdoZRbvaF4&t=25s) from Google Cloud Tech, "Why Your AI Agent Fails in Production (And How to Catch It)".*

Left, **Open-Source Evaluation Toolkit · Production Baseline · The Battle-Tested Baseline**:

- **Pre-Built Scripts & CLI**: ready-to-run telemetry converters & adapters · *zero glue code*
- **Guided Evaluation Workflow**: 1. Scenario Input → 2. Harvest Traces → 3. Rubric Scoring · *step-by-step*
- **Native GenAI Eval Bridge**: Vertex AI GenAI Evaluation Service & Agent Platform · *enterprise*
- *Don't build from scratch: Start with a production baseline.* · *instant launch*

Right, **Time-to-Evaluation**: **From scratch: weeks** (× custom parsers · × manual judges · × bespoke UI). **With baseline: 1 single hour**. *Baseline ingestion: ✓ ADK-tested. "Could we use it for other agentic frameworks?" → LangGraph, CrewAI & custom agents via universal OTel.* **Setup effort compression: Weeks → 1 Single Hour.**

*Still vs. transcript:* the narration says *"an evaluation toolkit that reduces the setup from weeks to one single hour."* The slide names what the toolkit replaces (custom parsers, manual judges, a bespoke UI) and its three-step workflow. It also marks the baseline as **ADK-tested**, with other frameworks posed as a question.

### 2 · Frameworks in, platform services out

![[assets/2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production/07-02m01-gemini-enterprise-agent-platform-integration.webp|Gemini Enterprise Agent Platform: seven agent frameworks on the left deploy to six managed platform services on the right]]

*Still at [2:01](https://www.youtube.com/watch?v=wPdoZRbvaF4&t=121s) from Google Cloud Tech, "Why Your AI Agent Fails in Production (And How to Catch It)".*

| Open-source & custom agent frameworks *(universal ingestion)* | → deploys to → | Gemini Enterprise Agent Platform, managed services *(platform core)* |
|---|---|---|
| Agent Development Kit (ADK): *Google Native* ★ | | Agent Runtime: *Execution* |
| LangGraph: *Stateful Graphs* ✓ | | Agent Retrieval & RAG: *Grounding* |
| LangChain: *Chains & Tools* ✓ | | Evaluations & Quality: *Evals SDK* |
| LlamaIndex: *RAG & Data* ✓ | | Context & Memory Bank: *State* |
| CrewAI: *Multi-Agent* ✓ | | Code Execution: *Sandbox* |
| AG2 (AutoGen): *Conversational* ✓ | | Cloud Observability: *OTel* |
| Any Python Agent: *Universal OTel* ✓ | | |

*Still vs. transcript:* the narration hedges: *"It doesn't matter if it's not an ADK agent. Of course, everything we tested internally with ADK agents. But also the team is constantly working to make it available for other frameworks too."* The slide shows six non-Google frameworks with check marks, and puts evaluation and observability among the platform's six managed services.

### 3 · DocsHound's architecture, with the observability layer

![[assets/2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production/15-03m48-docshound-architecture-with-observability.webp|DocsHound agent tool architecture: a LangGraph loop of five stages, a human-controlled approval workflow, and an observability layer]]

*Still at [3:48](https://www.youtube.com/watch?v=wPdoZRbvaF4&t=228s) from Google Cloud Tech, "Why Your AI Agent Fails in Production (And How to Catch It)".*

**DocsHound Agent Tool Architecture.** *LangGraph coordinates the guarded loop, each action invokes observable tools.*

**LangGraph agent loop**, with an **LLM router** feeding *Search docs*:

1. **Research**: `Research_repo`, `Research_pull_requests`, docs-repo activity (optional)
2. **Analyse**: `Cluster_issues`; groups evidence into gaps and shipped changes
3. **Search docs**: `search_official_docs`; checks coverage and recommends an action
4. **Draft**: `draft_review_documents`; writes reviewable Markdown
5. **Store**: finalizes graph state; no external tool

**Human controlled application workflow** (after Store): Edit + Approve Markdown → Preview file & Patch + PR → Create GitHub branch.

**Observability**: OpenTelemetry records one trace ⇢ OpenInference labels AGENT / TOOL / LLM spans ⇢ LangSmith displays it.

*Still vs. transcript:* the narration demos the UI. The slide gives the tool behind each stage, puts a human approval before any branch is created, and states the telemetry chain in one line. An earlier build state (2:26) shows the same diagram without the observability layer.

### 4 · Definition: OpenTelemetry

![[assets/2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production/16-04m25-definition-opentelemetry-otel.webp|Agent Evaluation Definition card for OpenTelemetry (OTel)]]

*Still at [4:25](https://www.youtube.com/watch?v=wPdoZRbvaF4&t=265s) from Google Cloud Tech, "Why Your AI Agent Fails in Production (And How to Catch It)".*

> **Agent Evaluation Definition — OpenTelemetry (OTel)**
> An **open-source standard** designed to capture, format, and transport data about a software system's internal behavior.
> It passes data using structural blocks called Spans.

*Still vs. transcript:* the narration offers *"Open telemetry is a standard for the standard"* and, earlier, *"converters for you to get all of your agent traces data … into one place."* The definition, and the term *span*, appear only on the card.

### 5 · Definition: OpenInference

![[assets/2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production/17-04m40-definition-openinference.webp|Agent Evaluation Definition card for OpenInference, which extends OTel with semantic tags]]

*Still at [4:40](https://www.youtube.com/watch?v=wPdoZRbvaF4&t=280s) from Google Cloud Tech, "Why Your AI Agent Fails in Production (And How to Catch It)".*

> **Agent Evaluation Definition — OpenInference**
> While OpenTelemetry provides the pipeline and the structural boxes (Spans), it doesn't **standardize application interactions with AI systems**.
> To solve that, **OpenInference extends OTel** by assigning consistent semantic tags: `AGENT, TOOL, LLM, RETRIEVER…`

*Still vs. transcript:* the narration explains the need (*"the LangGraph agent, the CrewAI agent, the ADK agent stream differently … the spans and the arguments might be different"*) and then says only *"OpenInference is a standard for that."* What OpenInference adds, a fixed set of span kinds, is on the card.

### 6 · Why it matters

![[assets/2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production/18-04m57-why-openinference-matters.webp|Why It Matters card: OpenInference spans decouple downstream consumers such as evaluation from the agent's internals]]

*Still at [4:57](https://www.youtube.com/watch?v=wPdoZRbvaF4&t=297s) from Google Cloud Tech, "Why Your AI Agent Fails in Production (And How to Catch It)".*

> **Why It Matters?**
> If your agent emits OpenInference spans, changes in the agentic module do not affect downstream systems that consume from its telemetry (e.g. evaluation).

*Still vs. transcript:* the narration ties it to evals only (*"we don't need to redo the work if you change that inner workings"*). The card states it as a general decoupling: anything that consumes the telemetry, with evaluation as one example.

### 7 · Definition: Scenario

![[assets/2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production/22-07m17-definition-scenario.webp|Agent Evaluation Definition card for Scenario]]

*Still at [7:17](https://www.youtube.com/watch?v=wPdoZRbvaF4&t=437s) from Google Cloud Tech, "Why Your AI Agent Fails in Production (And How to Catch It)".*

> **Agent Evaluation Definition — Scenario**
> A structured, reproducible **test case** or **simulated situation** designed to assess an agent's behavior under a specific set of initial conditions and target objectives.

*Still vs. transcript:* *scenario* is used throughout (*"you have already a scenario … we need a couple more scenarios"*) and never defined aloud.

### 8 · The agent-eval toolkit

![[assets/2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production/26-11m38-agent-eval-toolkit-architecture.webp|The agent-eval README in Google's professional-services repository, with callouts for the GenAI client and agents-cli]]

*Still at [11:38](https://www.youtube.com/watch?v=wPdoZRbvaF4&t=698s) from Google Cloud Tech, "Why Your AI Agent Fails in Production (And How to Catch It)".*

The GitHub page `professional-services / tools / agent-eval`: *"agent-eval — A hand-on-shoulder CLI walkthrough of the Vertex AI Generative AI Evaluation Service for ADK agents."* The caption reads: *"An opinionated **Evaluation ToolKit** (within Google Professional Services repo) containing **pre-built scripts** & a **guided workflow** to drastically **accelerate your evaluation setup**."*

Two callouts. **Gemini Enterprise Agent Platform: GenAI Client in Agent Platform SDK**, with sample code that calls `client.evals.run_inference(model="gemini-2.5-flash", …)` and then `client.evals.evaluate(…, metrics=[types.RubricMetric.GENERAL_QUALITY])`. **agents-cli in Agent Platform**: *"CLI and skills for building agents on Google Cloud."* A footnote on the second:

> *As of now, we "use" agents-cli, but the scripts and modules of the presented toolkit are expected to be **integrated into the Agents CLI eval module** by the end of this year.

*Still vs. transcript:* the narration says *"I created this with my team … we have it as an open source tool."* The still says where it lives (a folder in Google's Professional Services repository, not a product), what it was written for (ADK agents), which SDK calls it wraps, and that it is meant to move into Agents CLI.

### 9 · Three commands

![[assets/2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production/27-11m55-agent-eval-command-workflow.webp|The agent-eval README workflow diagram: setup once per shell, init once per agent, run every iteration]]

*Still at [11:55](https://www.youtube.com/watch?v=wPdoZRbvaF4&t=715s) from Google Cloud Tech, "Why Your AI Agent Fails in Production (And How to Catch It)".*

The README's workflow diagram, scrolled. The heading of step 1 is above the frame (entry 8 shows it: *"1 · agent-eval setup, once per shell"*) and the end of step 3 is below it.

1. **`agent-eval setup`** (*once per shell*): walks gcloud auth + ADC · picks your project + location · enables the Vertex AI API · binds the autorater IAM role so Vertex can grade your traces
2. **`agent-eval init`** (*once per agent*): auto-detects your local ADK agent (or FastAPI URL) · picks metrics: 18 managed (Vertex's catalog) + AI-drafted custom (**binary by default**) · generates `tests/eval/dataset.jsonl`
3. **`agent-eval run`** (*every iteration*): **collect**, which drives simulate (UserSim) + interact (DIY) · **score**, two-step `run_inference` → `evaluate` · **analyze + view** (cut off)

*Still vs. transcript:* none of the commands or their cadence is spoken. The diagram also says that custom metrics are AI-drafted and binary by default, which is what the config in entries 10 and 11 shows.

### 10 · The custom LLM judges

![[assets/2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production/34-20m57-eval-config-yaml-custom-llm-judges.webp|eval_config.yaml: the documentation-quality and groundedness judges, each with criteria and a pass or fail rating]]

*Still at [20:57](https://www.youtube.com/watch?v=wPdoZRbvaF4&t=1257s) from Google Cloud Tech, "Why Your AI Agent Fails in Production (And How to Catch It)".*

`backend/tests/eval/eval_config.yaml`, lines 13–47 (a third judge, `docshound_confidence_calibration`, begins below):

```yaml
# 2. Quality & Information Display (Custom LLM Judges)
docshound_documentation_quality:
  kind: custom_llm_judge
  instruction: >
    Evaluate the quality of the DocsHound response as a technical documentation patch or developer answer.
    Assess structure (clear headings, bulleted steps), code/config formatting (proper backticks and fenced code blocks),
    technical clarity, and readiness for a GitHub documentation PR.
  criteria:
    StructureAndFormatting: "Uses clean Markdown with headings, bullet points, and fenced code blocks with language identifiers."
    Actionability: "Provides concrete, copy-pasteable configuration keys, commands, or code snippets rather than vague generalities."
    TechnicalPrecision: "Explains the 'why' and 'how' with accurate developer-centric terminology."
  rating_scores:
    "1": "Pass: Well-structured, actionable, beautifully formatted in Markdown, and ready for documentation review."
    "0": "Fail: Poorly formatted, lacks code/config clarity, vague, or contains confusing instructions."
  threshold: 1.0

# 3. Groundedness & Confidence (Custom LLM Judges)
docshound_groundedness_and_attribution:
  kind: custom_llm_judge
  instruction: >
    Evaluate whether the DocsHound response is strictly grounded in the reference documentation,
    retrieved code, or GitHub issues/PR context without hallucinating non-existent environment variables,
    flags, or methods.
  criteria:
    FactualGroundedness: "Every claim, setting name, and instruction is verified by reference documentation or retrieved context."
    ZeroHallucination: "Does not fabricate environment variables, command options, or system architecture features."
  rating_scores:
    "1": "Pass: 100% grounded in factual documentation; no hallucinated configurations or invalid claims."
    "0": "Fail: Contains hallucinated settings, non-existent parameters, or unsupported claims."
  threshold: 1.0
  requires_reference: true
```

*Still vs. transcript:* the narration lists the criteria (*"Structural, formatting, actionability, technical precision"*) and Feroz singles out code blocks. The still shows that each judge is **binary**, pass 1 or fail 0 against a threshold of 1.0, and that the groundedness judge **requires a reference**.

### 11 · The trajectory judge and the deterministic checkers

![[assets/2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production/35-21m12-eval-config-yaml-trajectory-and-deterministic-checkers.webp|eval_config.yaml: a LangGraph trajectory judge and three deterministic Python function checkers]]

*Still at [21:12](https://www.youtube.com/watch?v=wPdoZRbvaF4&t=1272s) from Google Cloud Tech, "Why Your AI Agent Fails in Production (And How to Catch It)".*

Lines 63–97 of the same file.

**`docshound_langgraph_trajectory`** (`custom_llm_judge`): *"Evaluate whether the agent's problem-solving trajectory aligns with the DocsHound LangGraph architecture (Research repository/PRs -> Analyze/Cluster Gaps -> Search Official Documentation -> Draft Documentation -> Store Audit Trail)."* Criteria: **WorkflowProgression**, *"The response shows evidence of synthesizing research and documentation lookup before proposing concrete documentation cha[nges]"* (cut off at the edge); **Efficiency**, *"Directly addresses the user's objective without redundant or circular reasoning."* Rated 1 / 0, threshold 1.0.

**Deterministic Python function checkers**, all in `tests/eval/metrics/custom_metrics.py`:

| Metric | Function | Description |
|---|---|---|
| `docshound_graph_validity` | `validate_langgraph_workflow_trajectory` | Deterministic validation of LangGraph execution span sequence (research -> analyze -> search_docs -> draft -> store). |
| `docshound_markdown_structure` | `validate_markdown_documentation_structure` | Deterministic scoring of Markdown formatting, code block syntax, and configuration actionability. |
| `docshound_citation_fidelity` | `validate_grounded_citation_fidelity` | Deterministic verification that all referenced issue/PR numbers are grounded in reference data. |

*Still vs. transcript:* the narration says *"we also have LangGraph inner workings and we also have deterministic Python function checkers."* The still shows the trajectory checked twice: by a judge reading the **response** for evidence of the steps, and by code reading the **span sequence**. The second check depends on the labelled spans of entries 4–6.

### 12 · The score table

![[assets/2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production/36-22m20-agent-evaluation-html-dashboard-overview.webp|The evaluation report overview: an LLM-judge radar chart and a score table with two metrics flagged Low]]

*Still at [22:20](https://www.youtube.com/watch?v=wPdoZRbvaF4&t=1340s) from Google Cloud Tech, "Why Your AI Agent Fails in Production (And How to Catch It)".*

The report's Overview tab (tabs: Overview · Per-Question (4) · Iteration History · AI Analysis). Radar chart of the LLM-judge metrics, run `20260817_125151`.

| Metric | Score | Range | Status |
|---|---|---|---|
| docshound_documentation_quality | 0.33 | 0–1 | Low |
| docshound_confidence_calibration | 75% | 0–1 | Pass |
| docshound_langgraph_trajectory | 1 | 0–1 | Pass |
| docshound_graph_validity | 1 | 0–1 | Pass |
| docshound_markdown_structure | 0.34 | 0–1 | Low |
| docshound_citation_fidelity | 1 | 0–1 | Pass |

Deterministic metrics: `token_usage.llm_calls` 1; `token_usage.total_tokens` 584.75.

*Still vs. transcript:* the narration reads it as *"the DocsHound documentation quality is actually pretty low."* The table lists **six** metrics. The config and the heatmap have **seven**: `docshound_groundedness_and_attribution` is not in the table. The run id is dated 17 August 2026, about six weeks before publication.

### 13 · The heatmap

![[assets/2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production/37-23m12-per-question-score-heatmap.webp|Per-question score heatmap: four questions against seven metrics, with empty cells for groundedness and one documentation-quality score]]

*Still at [23:12](https://www.youtube.com/watch?v=wPdoZRbvaF4&t=1392s) from Google Cloud Tech, "Why Your AI Agent Fails in Production (And How to Catch It)".*

| Question | doc. quality | groundedness | confidence | LangGraph trajectory | graph validity | markdown | citation |
|---|---|---|---|---|---|---|---|
| 001 · How do I configure Redis cache in DocsHound? | 1 | — | 100% | 1 | 1 | 0.45 | 1 |
| 002 · Where are the documentation sources configured for a repository? | 0 | — | 0% | 1 | 1 | 0.30 | 1 |
| 003 · How does DocsHound instrument OpenTelemetry and LangSmith traces? | 0 | — | 100% | 1 | 1 | 0.30 | 1 |
| 004 · What environment variables are required to connect DocsHound to… | — | — | 100% | 1 | 1 | 0.30 | 1 |

*Still vs. transcript:* this is how the headline was computed, and the narration never says it. The **0.33 is one pass out of three scored answers**; question 004 has no documentation-quality score. The 0.34 is the mean of 0.45, 0.30, 0.30 and 0.30, and the 75% is three passes out of four. The groundedness column is empty for every question.

### 14 · The autorater errors behind the empty cells

![[assets/2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production/38-23m43-per-question-deep-dive-autorater-errors.webp|Per-question deep dive for the environment-variables question: two autorater errors and two passing judge verdicts]]

*Still at [23:43](https://www.youtube.com/watch?v=wPdoZRbvaF4&t=1423s) from Google Cloud Tech, "Why Your AI Agent Fails in Production (And How to Catch It)".*

The deep dive for question **004**: the judges' reasoning concerns environment variables. From the top:

- A metric card whose name is above the frame: **Autorater error:** *Context has already been used to create a Connection, it cannot be mutated again.*
- **`docshound_groundedness_and_attribution` · FAILED · error.** *Autorater error: 400 INVALID_ARGUMENT … 'Error rendering metric prompt template: Variable reference is required but not provided..' … [truncated; original was 646 chars].*
- **`docshound_confidence_calibration` · Pass 1.00.** *"The agent provides a direct and specific list of required environment variables, along with their purpose (GitHub App authentication and webhook verification). … There are no signs of guessing or inventing details."*
- **`docshound_langgraph_trajectory` · Pass 1.00.** *"The agent's response directly and accurately identifies the required environment variables (GITHUB_APP_ID, GITHUB_PRIVATE_KEY, GITHUB_WEBHOOK_SECRET) … This precise information **strongly implies** that the agent successfully executed the 'Search Official Docs' and 'Analyze' steps of the workflow."*

*Still vs. transcript:* the narration says *"there's an error rendering the prompt … this is for the autoraters specifically"* and *"the converter somehow still needs a little bit of tweaking."* The still shows the errors behind the empty cells. It also shows the trajectory judge passing a trajectory by inference from the final answer (*"strongly implies"*), which is the gap the deterministic span check in entry 11 exists to close.

## Why this matters to the wiki

**1. The Test phase, run end to end on one agent.** The corpus describes the Test phase of the [[agent-development-lifecycle]] in many vocabularies. This is the first source that does all of it on camera on one agent: traces, scenarios, metrics, a scored report and a reading of the result. It matches [[2026-05-09-chase-agent-development-lifecycle|Chase's]] account of traces as the material evals are made from. DocsHound's own UI showed a finished run with a documentation pull request ready to open; the eval scored the documentation it drafts low. That is Chase's *"an agent can return a technically successful response and still fail the task itself"*, observed rather than asserted. The grader mix in entries 10–11 is [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe's]] grader families minus the human: a managed metric, rubric judges and deterministic code checks, with the trajectory graded twice.

**2. Framework-neutral traces as the precondition.** Entries 4–6 make an argument the [[agent-harness]] page holds from the evaluation side, that the eval harness should mirror the production harness. Here the bridge is the telemetry format: OpenInference's span kinds let an evaluator built for ADK read a LangGraph agent once a converter exists, and let the agent's internals change without breaking the evals. The span check in entry 11 depends on it.

**3. Metrics drafted by an agent.** [[Antigravity]] proposes the metrics from the code and from Feroz's description of what good documentation is, and the toolkit's own README says custom metrics are *"AI-drafted"* (entry 9). [[2025-09-28-husain-ai-evaluations-clearly-explained-50-min|Husain's]] workflow reaches binary judges by another route: open and axial coding of real traces, then validating each judge against human labels. Both end with binary judges built around the expert's notion of quality. The episode shows no validation step. [[2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent|Anthropic's evals-for-taste talk]] starts from the same gap between *"it seems to work"* and a number, and also pairs code graders with model graders, but its judges score 0–5 rather than pass/fail.

**4. Reading your own dashboard.** The cast frames the 0.33 as the blind spot the scorecard caught. The stills show it rests on three scored answers. Zamora's own hedge, that the code or the evaluation may need work, is the middle position of [[2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway|Khan's]] *evals are broken, use them anyway*, applied to one's own numbers. The judge can also fail operationally: here two autorater calls errored and a metric dropped out of the summary. [[2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals|Shea and Roche]] measure judge reliability as variance; this is the cruder failure, no verdict at all.

**Dynamic capabilities.** **`digital-seizing/rapid-prototyping`**: the episode's pitch is compressing eval setup from weeks to an hour, so that a developer can change the prompt, model or harness and see the effect in the next run (*"it makes me want to just go back and start playing with my agent again"*). **`digital-transforming/improving-digital-maturity`**: the move it argues for is from judging an agent by feel to a repeatable test that catches regressions, including when someone other than the original author makes the change.

## Linked entities and concepts

- **Entities**: [[Google]] (Google Cloud Tech is the channel; Vertex AI, the Gemini Enterprise Agent Platform and the agent-eval toolkit are Google's), [[Antigravity]] (the coding agent that maps DocsHound's architecture, generates scenarios, writes the trace converter and drafts the metrics), [[LangChain]] (LangGraph is DocsHound's framework; LangSmith displays its traces).
- **Sources**: [[2026-05-09-chase-agent-development-lifecycle|Chase 2026]], [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe 2026]], [[2025-09-28-husain-ai-evaluations-clearly-explained-50-min|Husain 2025]], [[2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent|Anthropic 2026]], [[2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway|Khan 2026]], and, without a typed edge, [[2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals|Shea & Roche 2026]] on judge reliability.
- **Concepts**: [[agent-development-lifecycle]] (the Test phase, run end to end), [[agent-harness]] (evaluation reads the production harness's telemetry).
- **Dangling** (single-source mention, deferred): **Dani Zamora**, **Matthew Feroz**, **Merge**, **DocsHound**, **agent-eval**, **OpenTelemetry**, **OpenInference**, **Gemini Enterprise Agent Platform**.

## Debates and supersession

- **What the headline number rests on.** The description presents *"a 33% documentation quality score"* as the blind spot the scorecard caught. The heatmap (entry 13) shows 0.33 is one pass among three scored answers, out of four questions, from a binary judge; the fourth answer was not scored after an autorater connection error (entry 14). The groundedness judge, configured with `requires_reference: true`, returned no score for any question, with an error about a required variable reference not provided, and it is absent from the summary table (entry 12). The presenters do say the evaluation itself may need work and that the converter needs tweaking. The page records both readings: a cheap, early signal worth acting on, and a figure resting on N = 3.
- **No judge validation shown.** The metrics are drafted by Antigravity and accepted after a quick read (*"I think honestly that's pretty good"*). Checking judges against human labels, the step [[2025-09-28-husain-ai-evaluations-clearly-explained-50-min|Husain]] treats as essential, is not part of the episode. In a 60-minute format that may be a time choice rather than a method claim.
- **"Weeks → one hour".** The slide's claim (entry 1) is the toolkit's. On camera the hour runs out mid-way (*"Uh oh, we run out of time"*) and the report has two failing autoraters. The video shows that a first report can be produced in a session; it does not measure setup time.
- **Vendor content.** Google's toolkit, platform and channel. The ADK-only testing is stated on screen (entries 1 and 8), and the toolkit is a Professional Services folder with a stated plan to move into Agents CLI *"by the end of this year"*: a roadmap statement, unverified.
- **Tooling note (2026-10-01; a measurement in this repo, not a source).** This page was processed with the stills pipeline (CLAUDE.md §Video stills). Gemini found all four definition cards; a pixel scan of every second for the cards' border found the same four and no others. Its reading was wrong in places where it matters for this page, including the heatmap cell behind the 0.33. Every transcription above was checked against the still.

## What was actually ingested

The full 26:07 transcript (auto-generated English captions, 251 segments, 0:00–26:04), ASR-cleaned at acquire; the corrections are listed in the raw file's `notes:`. Three passages were left verbatim as unclear. Presenter names and affiliations come from the description. Of 38 stills cut from the video, 14 are published above after checking each against the frame. Left out: DocsHound and GitHub demo screens, Antigravity and VS Code working screens, a loading console, the episode's step cards, and near-duplicate frames reused in the recap. The linked repositories (agent-eval, DocsHound) and the Gemini Enterprise Agent Platform docs were not fetched.
