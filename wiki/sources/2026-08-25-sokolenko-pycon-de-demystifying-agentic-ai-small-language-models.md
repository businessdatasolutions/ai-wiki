---
type: source
kind: video
title: "Demystifying Agentic AI Using Small Language Models [PyCon DE & PyData 2026]"
author: ["PyData"]
publisher: "PyCon DE & PyData 2026 (Darmstadt, recorded 15 April 2026); published on the PyData YouTube channel 25 August 2026. Presenter: Serhii Sokolenko, co-founder of Tower"
url: "https://www.youtube.com/watch?v=nk5BNz8v_9E"
talk_page: "https://2026.pycon.de/talks/YZM8TA/"
date_published: 2026-08-25
date_recorded: 2026-04-15
date_ingested: 2026-09-04
length: "~32:00 minutes (auto-generated transcript, ASR-cleaned; 299 segments, no channel chapters)"
raw: "../../raw/videos/demystifying-agentic-ai-using-small-language-models.md"
tags: [small-language-models, slm, agentic-ai, ai-agents, tool-calling, function-calling, berkeley-function-calling-leaderboard, xlam, salesforce, nvidia, georgia-tech, langchain, llama-cpp, quantization, local-inference, apache-iceberg, open-source-ai, pycon-de, pydata, serhii-sokolenko, tower, agentic-hype, reasoning-loop, chain-of-thought, business-rules-over-dags]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-sensing/digital-mindset-crafting
  - digital-seizing/rapid-prototyping
  - digital-seizing/balancing-digital-portfolios
relationships:
  - type: supports
    target: 2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai
    via: "this talk is the applied reading of that position paper — Sokolenko presents it on stage as 'a paper on small language models as the future of agentic AI' by 'researchers from Nvidia and Georgia Tech', restates its three value claims (V1 sufficiently powerful / V2 more suitable / V3 more economical) as his three slide bullets, and reproduces its four agentic capabilities almost verbatim. He also **moves the definition**: the paper says 'most models below 10bn parameters' as of 2025; Sokolenko argues for a time-indexed device-memory definition that lands at 10–30bn in 2026 — the same working definition (WD1) run forward one hardware generation"
    confidence: 0.9
  - type: supports
    target: 2025-07-13-patil-berkeley-function-calling-leaderboard
    via: "the talk's only quantitative evidence is a BFCL screenshot. Sokolenko uses the leaderboard exactly as its authors intend it (a ranking of tool-calling ability across ~110 model families, refreshed roughly quarterly) and, in the Q&A, correctly defends its Overall Accuracy column as a composite index rather than a per-question hit rate — *'it's a combined score of four other scores. Think of it as an index, and accuracy is the wrong name for it'*"
    confidence: 0.85
  - type: supports
    target: 2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2
    via: "the model Sokolenko actually runs in the demo is xLAM-2-32B at 4-bit quantization, and his one-line account of how it was built — *'they used a synthetic data set with function calls and they used a process called supervised fine-tuning'* — is APIGen-MT's pipeline compressed to a sentence. The talk is the field evidence that the paper's open-sourcing decision paid off: a practitioner picking the model *because* it is open, small and near the top of BFCL"
    confidence: 0.85
  - type: supports
    target: 2022-10-06-yao-et-al-react-synergizing-reasoning-acting
    via: "Sokolenko's whiteboard account of an agent — prompt in, reasoning loop, plan decomposed into tool calls, loop until a literal `final_answer` token is emitted, write prompt and output to memory, loop again — is ReAct's reason→act→observe cycle described from the runtime side, four years on and without naming it"
    confidence: 0.75
  - type: supports
    target: 2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness
    via: "same boundary drawn from the model side rather than the runtime side. Sokolenko's stack — inference server, Python runtime, orchestrator, framework, business rules in the prompt — is a harness by another name, and his claim that LangChain routes tool selection off *function names, argument names and docstrings* is a concrete statement of what the harness feeds the model"
    confidence: 0.7
  - type: supports
    target: 2026-07-29-ng-washington-post-china-open-source-ai-competitiveness
    via: "an independent European practitioner arriving at the same own-vs-rent conclusion from the laptop end: the reason to care about open weights is that you cannot experiment with a proprietary model — *'they are all proprietary, so you cannot use them for local experimentation'*"
    confidence: 0.7
---

# Sokolenko — Demystifying Agentic AI Using Small Language Models (PyCon DE & PyData 2026)

> 🎓 Watch Serhii Sokolenko demystify agentic AI as he reveals how to build powerful, scalable data agents using Small Language Models and Iceberg tables—without the need for a GPU farm.
>
> Agentic AI utilizes language models as decisioning engines to perceive environments, make decisions, and execute actions to achieve specific goals. While large language models (LLMs) are often used for these reasoning loops, they are computationally expensive and contain redundant data. Small language models (SLMs), defined as models with 10 to 30 billion parameters that fit within 16 to 32 gigabytes of consumer RAM, provide a cost-effective, private alternative for agentic workflows.
>
> *— Channel description, [[PyData]] (PyCon DE & PyData 2026)*

## TL;DR

A 32-minute conference talk by **Serhii Sokolenko** — co-founder of **Tower**, previously Google (Cloud Dataflow), Snowflake and Databricks — arguing that the way to survive the agentic hype cycle is to stop reading about it and run an agent on your own laptop, which small language models now make possible. It is the wiki's **first source about model *size* as an agentic design variable**, and its first to name a concrete open-weight tool-calling stack a practitioner can reproduce in an afternoon.

The talk's own framing is a hype-cycle joke: 150 years ago Bay Area billboards sold clipper passage to the Gold Rush; today they sell Agentforce. His prescription is one line and he says it is the only thing to take away —

> *"If you take anything away from this talk… it's this phrase of getting your hands dirty. Use the tools from the talk, use the ideas that we'll present on your laptop today, and lean on small language models as a way of experimenting."* — ~2:25

The substance underneath is a compressed reading of three research artefacts the wiki now holds as separate sources: the [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|NVIDIA / Georgia Tech position paper]], the [[2025-07-13-patil-berkeley-function-calling-leaderboard|Berkeley Function Calling Leaderboard]], and the [[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2|Salesforce xLAM-2 / APIGen-MT]] model family.

## The argument, in four moves

**1. Agents are not new; LLM-as-decisioning-engine is.** Sokolenko dates the agent concept to Russell & Norvig (1995) — *"an entity that perceives its environment, makes decisions and takes actions"* to achieve goals — and points at elevator dispatch (Otis, Schindler) as pre-LLM agents running on utility theory and reinforcement learning. What changed ~5 years ago is that **language models became the decisioning engine**, and he gives a two-step genealogy for how: GPT-3 was trained on corpora dense with *reasoning-shaped* text (Stack Overflow threads, coding tutorials, forum answers — *"it's a tree-like structure, it's a reasoning structure"*), and then chain-of-thought work put **intermediate reasoning steps into the training data itself**. *"This is how reasoning got injected into large language models."*

**2. The loop, described from the runtime side.** Prompt in → reasoning loop → plan → tool calls (APIs, analytical or operational database access) → loop continues *"until a token is emitted in one of the outputs… it's literally `final_answer`, `final_underscore_answer`"* → final textual output → prompt and output written to memory → loop begins again. This is [[react-reasoning-acting|ReAct]]'s reason→act→observe cycle narrated as plumbing; see [[2022-10-06-yao-et-al-react-synergizing-reasoning-acting|Yao et al.]] for the origin.

**3. Most of an LLM is dead weight in that loop.** The rhetorical hinge of the talk, repeated twice:

> *"Does it really matter to know who the queen of England was in the 1980s in order to make a decision whether to call a data access API? Probably not."* — ~10:32

Large models compress information you are not using; that makes inference expensive; expense makes them un-experimentable *"because they don't fit on the hardware that is readily available to you."* The cost argument is framed as an **experimentation** argument, not a unit-economics one — a different emphasis from the NVIDIA paper, which leads with the 10–30× serving-cost figure.

**4. What "small" means — a moving, hardware-indexed definition.** Sokolenko explicitly prefers a definition that is *independent of time* in form and therefore *moves* in value: **whatever fits in the memory of a regular consumer device**. In 2026 that is 16–32 GB, which lands at roughly **10–30 billion parameters**. Strengths: privacy (your hardware), cost (*"I can literally run many of these models on this laptop which is already two years old… it costs me zero"*). The named weakness is exactly the discarded knowledge: *"it doesn't know who the queen of England was in the 1800s… it will probably fake some name out of its weights."*

## The four capabilities that matter for agents

Sokolenko's restatement of the paper's capability list — worth quoting because it is the cleanest short answer in the corpus to *what an agentic model actually has to be good at*:

| # | Capability | His gloss |
| --- | --- | --- |
| 1 | **Task decomposition** | *"the ability to break down a task into subtasks. This is what reasoning is."* |
| 2 | **Tool calling** | *"the ability to initiate, pass parameters, and format your output"* |
| 3 | **Glue-code generation** | for the cases *"where you don't have the tools to solve a problem"* |
| 4 | **Instruction following** | *"the ability to follow guard rails"* |

And the headline he draws from the paper's comparison table: **for these four tasks, SLMs of size *x* are now as good as LLMs of ten times that size.**

## The leaderboard segment (the UC Berkeley research)

The talk's only numbers come from the [[2025-07-13-patil-berkeley-function-calling-leaderboard|Berkeley Function Calling Leaderboard]], which he describes accurately: a UC Berkeley leaderboard tracking ~110 model families, vendor-supplied runs with verification, refreshed roughly every three months. Reading the December 2025 snapshot he showed:

- **Top of the board is still proprietary** — Claude Opus 4.5, Gemini 3, GLM 4.6 — *"but they are all proprietary. So you cannot use them for local experimentation."* This is the own-vs-rent argument of [[2026-07-29-ng-washington-post-china-open-source-ai-competitiveness|Ng's open-weights case]] reached from the laptop end rather than the competitiveness end: the reason to care about open weights is that you cannot iterate on a model you can only rent.
- **Positions ~10–20 are where open weights start** — Kimi K2, DeepSeek V3.2, and at **position 18, Salesforce xLAM-2**.
- xLAM-2 is *"the first model that is not only open-source but also smallish"* — **32B parameters**, overall accuracy comparable to state of the art, in the top 20 of 110.

The best moment in the Q&A is an audience member catching a benchmark-literacy trap: if the top score is ~70%, are 30% of agent responses garbage? Sokolenko's answer is correct and matters for how this wiki reads leaderboards generally:

> *"The 77.47 doesn't mean that 23% of your questions will be answered wrongly. It's a combined score of four other scores. Think of it as an index. It's just an index, and accuracy is the wrong name for it. It should be called overall index."* — ~31:16

That is a caveat the [[ai-benchmarks]] page should carry: BFCL's **Overall Accuracy is a composite**, not a per-call success rate.

## The reproducible stack

Five components, named with reasons — the most concretely actionable list in the corpus for running an agent locally:

| Layer | Choice | Why (his stated reason) |
| --- | --- | --- |
| Model | **Salesforce xLAM-2, 32B, 4-bit quantization** | open source, small, top-20 on BFCL, fits 16 GB RAM |
| Local inference | **llama.cpp** | uses Apple-silicon GPUs (*"whereas vLLM for example does not"*); simple Hugging Face model naming conventions |
| Remote inference | **Together AI**, **Hugging Face** | for moving the workload to production |
| Python runtime | **Tower** (or Modal, fly.io) | package laptop Python into an app, run it in production, feed production logs back |
| Framework | **LangChain** (or LlamaIndex) | orchestration; personal preference |

Two design claims travel with it:

- **Tool selection is driven by your code's surface text.** *"If you use LangChain, it uses information in your code including names of functions, including the arguments you have, and also including even your docstrings, to feed it into the decisioning process and determine which tool is the best one."* A concrete statement of what the [[agent-harness|harness]] actually hands the model — the same boundary [[2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness|Baugues & Thurium]] draw from the runtime side (*"the harness is everything after the LLM"*), here drawn from the model side by someone assembling one from parts.
- **Business rules replace DAGs.** *"We don't do our typical Airflow DAGs anymore. We write business rules… you can take stock data from an external source, but you should probably take it from a cached source if it exists."* The demo agent chooses between an Apache Iceberg lakehouse cache and the Yahoo Finance API on exactly that rule. His stated reason for putting real data behind the agent at all is the 2023 New York fabricated-legal-brief episode: *"people realized we have to give agents access to real business data."*

## The demo's honest failure

The demo is Claude writing a Tower application from example code plus an MCP server, deploying it, failing, and being fixed by its own production logs:

> *"The first version of the app will kind of work, but not really… this is something that you will see a lot in your development of agents using other agents, AI assistants. The first versions will probably fail… but runtime services like Tower are able to feed production logs back into Claude so that Claude can learn and adjust."* — ~26:26

He runs out of time and asks the audience to *"trust me on the successful execution of the second app"* — worth flagging: **the successful run is not shown on camera.**

## On multi-agent SLM use (Q&A)

Asked whether each agent in a multi-agent workflow needs its own SLM: **no** — start with one existing SLM (xLAM-2) and vary the prompt and business rules; fine-tune a per-task copy on synthetic data only later, if at all.

On the quantization trade-off: **8B "are still stupid and dumb"; things get interesting around 30B at 4-bit**, which is also the point at which *"they terminate correctly, they don't run infinite loops."* He names non-termination as a characteristic SLM agentic failure with a mechanism attached:

> *"These agentic loops can never terminate… because the SLMs are incentivized to call as many tools as they can."* — ~30:07

That is a size-conditioned version of the runaway-loop failure mode in [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails|Google Cloud's loop-engineering failure taxonomy]], and the wiki's first claim that **loop termination is a model-capability threshold**, not only a harness-design problem.

## Dynamic capabilities (Warner & Wäger)

- **`digital-sensing/digital-scouting`** — the talk *is* a scouting artefact: a practitioner reading the SLM research frontier (NVIDIA/Georgia Tech, UC Berkeley, Salesforce) and reporting back what is deployable now versus still proprietary.
- **`digital-sensing/digital-mindset-crafting`** — the explicit hype-versus-substance framing (Gold Rush billboards → Agentforce) and the *"get your hands dirty"* prescription are aimed at changing how an audience thinks about agentic claims, not at selling a product.
- **`digital-seizing/rapid-prototyping`** — the entire second half is a prototype-on-your-laptop recipe: quantized open model + local inference server + framework + runtime, explicitly justified as the cheapest way to learn.
- **`digital-seizing/balancing-digital-portfolios`** — the SLM-versus-LLM choice is presented as a portfolio decision across cost, latency, privacy and deployability, with proprietary frontier models kept for what only they can do.

## Linked entities and concepts

- Concepts: [[small-language-models]], [[ai-agents]], [[ai-benchmarks]], [[agent-harness]], [[react-reasoning-acting]], [[open-source-ai]], [[foundation-models]]
- Entities: [[PyData]], [[Berkeley Function Calling Leaderboard]], [[xLAM]], [[NVIDIA]], [[Salesforce AI Research]], [[UC Berkeley]], [[LangChain]], [[Hugging Face]], [[Google]], [[Anthropic]]
- **Dangling** (single-source mention, deferred): Serhii Sokolenko, Tower, PyCon DE, llama.cpp, Together AI, Modal, fly.io, LlamaIndex, Marimo, dlt, Snowflake, Databricks, Salesforce (the parent company, as distinct from [[Salesforce AI Research]])

## Scope and reliability

**What this is good for:** the applied reading of the SLM position; the reproducible local stack; the BFCL-as-index caveat; the 30B/4-bit termination threshold; the business-rules-instead-of-DAGs framing.

**What it is not:** evidence. There are **no measurements of his own** — no latency numbers, no cost comparison he ran, no accuracy figure from his agent. Every number in the talk is read off someone else's leaderboard. The demo's successful run is asserted, not shown. The speaker is a vendor founder and the runtime layer of his recommended stack is his own product, disclosed on stage (*"I work on Tower but you can also use Modal or fly.io"*) — the disclosure is clean, but the stack recommendation is not disinterested. Cite this page for **framing, vocabulary, and the deployable-today stack**; cite the three research sources it points at for anything load-bearing.

## Debates and supersession

- **What counts as "small" is now contested inside the wiki.** The [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|NVIDIA paper]] wrote "most models below 10bn parameters" as of 2025; Sokolenko argues 10–30B in 2026 and says 8B models *"are still stupid and dumb"* for agentic work. Both are applying the *same* definition (fits a consumer device, practical latency for one user) to different hardware years. The wiki records the definition as **device-indexed and therefore moving**, and treats any fixed parameter count as a dated instance of it — see [[small-language-models]].
- Open: no source in the corpus yet measures an SLM-based agent against an LLM-based one **on the same task under the same harness**. Until one does, "as good as models ten times the size" is a benchmark claim, not a deployment claim.
