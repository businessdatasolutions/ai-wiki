---
type: source
kind: video
title: "Interrupt NYC: Opening Keynote"
author: ["LangChain"]
publisher: "LangChain (YouTube channel) — opening keynote of Interrupt NYC, delivered 24 Sep 2026; speaker Harrison Chase, co-founder and CEO"
url: "https://www.youtube.com/watch?v=950byF7njfw"
date_published: 2026-10-05
date_ingested: 2026-10-05
length: "~32:10 minutes (transcript ~236 segments + 16 stills; manual English captions)"
raw: "../../raw/videos/interrupt-nyc-opening-keynote.md"
stills: "../../raw/videos/interrupt-nyc-opening-keynote.stills.md"
tags: [langchain, harrison-chase, interrupt-nyc, interrupt-26, vendor-keynote, product-launches, own-your-intelligence, model-neutral-harness, compounding, agent-governance, people-process-technology, platform-engineers, agent-engineers, non-technical-builders, agent-development-lifecycle, langsmith, deep-agents, managed-deep-agents, context-hub, agent-auth, user-level-memory, parallel-web-search, decision-models, jev, semif, typesafe-ai, llm-gateway, cost-controls, model-fallbacks, trajectories, fine-tuning, smithtune, fireworks-ai, baseten, smithdb, custom-apps, langsmith-engine, red-teaming, open-models, token-costs]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - strategic-renewal/business-model
relationships:
  - type: supports
    target: 2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents
    via: "Same speaker at the previous Interrupt (San Francisco, May 2026). Shared topics: open models (cost, trainability), agent identity and auth on behalf of a user or a fixed account, and learning from traces. This keynote names Managed Deep Agents and SmithDB as launched at that event."
  - type: supports
    target: 2026-05-09-chase-agent-development-lifecycle
    via: "Shared topic: the build / test / deploy / monitor loop inside a govern ring. The essay defines the phases; this keynote shows the same loop as a slide and assigns LangSmith product layers and LangSmith Engine actions to each phase."
  - type: supports
    target: 2026-09-17-runkle-lovell-langchain-building-a-harness-with-jev
    via: "Shared topic: TypeSafe's Jev decision model. The post documents the langchain-typesafe integration and its uses; this keynote lists evals, guardrails and model routing as uses and adds access through the LangSmith LLM Gateway."
  - type: supports
    target: 2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals
    via: "Shared topic: a decision model as an evaluator. The post measures Jev as an eval judge on five cases; this keynote names eval, in the loop or after the fact, as the first use case, without figures."
  - type: supports
    target: 2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai
    via: "Shared phrase and topic: 'own your intelligence' at company level. Huang lists the drivers at Sequoia's event of that name; Chase lists token costs, open models and data as the reasons the phrase is current. Both name Harvey."
  - type: supports
    target: 2026-08-06-garry-tan-own-your-intelligence
    via: "Shared phrase: 'own your intelligence'. Tan applies it to one person's context and harness; Chase applies it to a company's harness, data and post-trained models."
  - type: supports
    target: 2026-07-08-jensen-huang-why-companies-need-open-agent-systems
    via: "Shared topic: open-weight models post-trained for a company's domain, with Deep Agents as the harness. NVIDIA is one of three makers on this keynote's open-models slide."
  - type: supports
    target: 2026-08-11-ummadisetti-langchain-toyota-deep-agents-rd-research
    via: "Shared topic: Deep Agents as a company-wide harness with centrally provided tools and skills. Toyota describes one deployment; this keynote describes a platform-team ring and Managed Deep Agents as a 'company harness'."
  - type: supports
    target: 2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production
    via: "Shared topic: turning agent traces from different frameworks into one standard format for evaluation. Zamora & Feroz use OpenTelemetry with OpenInference labels; this keynote announces LangSmith Trajectories, a message-list format parsed from many SDKs."
---

# Chase — Interrupt NYC Opening Keynote (LangChain, 24 Sep 2026)

> Harrison Chase, Co-Founder and CEO of LangChain, uses examples from Rogo, Harvey, and JPMorgan Chase to explain owning your intelligence, which means building domain-specific pieces in and around the model, and the three pillars it takes: an open, model-neutral harness such as LangGraph or Deep Agents, a loop that compounds what you learn from how people use your agents, and governance for internal agents.
>
> He then walks through the LangSmith platform layer by layer: a new Managed Deep Agents release with auth primitives, user-level memory, and built-in web search via Parallel, decision models like Jev and SemIf through the LangSmith LLM Gateway, and three launches for observability and evals: LangSmith Trajectories, LangSmith Fine-Tuning with the smithtune CLI, and LangSmith Custom Apps. He closes with LangSmith Engine v2, which adds red teaming and tests its own fixes on LangSmith Deployment, and shares that Engine has scanned over 70 million traces and detected over 21,000 issues.
>
> This session was captured at Interrupt New York City, the agent conference by LangChain.
>
> — channel description, LangChain (chapter list and resource links omitted)

## TL;DR

A ~32-minute opening keynote by **[[Harrison Chase]]**, co-founder and CEO of **[[LangChain]]**, at **Interrupt NYC**, the first New York edition of LangChain's agent conference. It was delivered on **24 September 2026** (per [LangChain's event page](https://interrupt.langchain.com/nyc)) and published on 5 October. The captions are the channel's manual English track. The talk is slide-led throughout, and the slides carry figures the narration leaves out, so this page publishes **16 verified stills**.

The talk has two halves. The first nine minutes argue for a phrase, ***own your intelligence***, and the conditions for it. The remaining 23 minutes walk through LangSmith in three layers (runtime, observability and evals, and an "intelligence" layer above them) and announce seven releases. Every product claim and figure here is the vendor's own; none comes with a method.

**1. Agents moved into the application layer, and the value sits around the model (0:35–2:43).** Chase's timeline runs from prototypes in 2023 through single-call LLM apps in 2024 and agent exploration in 2025 to 2026, when *"agents have transformed the application layer."* His three examples: **Rogo** (*"a specialized harness with model routing"* for finance), **Harvey** (*"fine-tuned models for specialized tasks"* in legal) and **JPMorgan Chase** (*"customizing the harness around the model"* for internal agents in its *"Jarvis assembly line"*). *"It's not just the model that they're providing to their customers. It's everything around the model… these domain-specific agents, they're not just wrappers."* Still 1 names what "around the model" contains.

**2. Three reasons the phrase is current (2:43–4:25).** (a) *"Token costs are rising a lot… being able to control and monitor token costs is really important."* (b) Open models are *"a really cheap alternative"* and customisable: *"as these base open-weight models get better and better, you can start to post-train them."* (c) *"The models themselves are becoming somewhat commoditized, and it's all of this stuff around the model, in particular the data… this is becoming the differentiator."* The slide (still 2) attaches a headline, three open-model makers and a quote to each reason. None of the three is discussed aloud.

**3. Three pillars: open, compounding, governed (4:25–7:22).**

- **An open, controllable harness.** It must be **model-neutral**, which Chase calls *"both offensive and defensive"*: *"When the best new model comes out, whether it's from OpenAI or Anthropic or TypeSafe with some of their Jev models, you want to be able to switch your harness to that as quickly as possible… It's also defensive. You don't want to get locked into a single model provider so that they can raise rates."* It must also be controllable: *"you need a way to control really in real detail what's going into the model."* LangGraph's directed graphs and Deep Agents' *middleware* are the two LangChain routes.
- **Compounding.** *"When you launch an agent, that is far from having a successful agent."* Learning from use can be manual (fix code or prompts) or automatic (memory, prompt optimisation). *"If you can define what better and what best looks like for your domain better than anyone else, you will be able to build the best agent for that domain."*
- **Governed.** *"Really crucial for internal agents"*: know how many agents exist, control their costs, and handle auth so that *"different people accessing it only have access to what they should have access to."*

**4. People and process (7:22–9:20).** Chase describes an organisation in three rings (still 3). **Platform engineers** provide the tools for governance and the eval loop. **Agent engineers** are *"the weird hybrid mix of data scientist and engineer and machine learning engineer… a new skill set."* The outer ring is spoken of as *"subject matter experts… often the best people to decide what good looks like for an agent"*, and the slide labels it *non-technical builders*. The process is the build / test / deploy / monitor loop, governed: *"You first launch an agent, it's not going to be good. You need to iterate."*

**5. Runtime: business logic, harness, infrastructure (10:38–15:51).** An agent has **business logic** (instructions, tools, skills, hooks), a **harness** that *"wires it all up so that the model can see the right context at the right point in time"*, and **infrastructure**: a durable runtime, a tool server, sandboxes and model access. *"We see a lot of agents writing code even if they're not coding agents."* **Deep Agents** is LangChain's *"off-the-shelf agent harness"*, launched about a year earlier; *"it learns a lot from what coding agents do"* (still 4). LangSmith supplies each infrastructure piece (still 5). **Managed Deep Agents** combines harness and managed infrastructure, so *"you just provide your business logic"*. Chase calls it *"this company harness"*. The new release adds:
- **Auth primitives:** *connections* (how end users authenticate to tools), *identity* (an agent runs as the user or as a service), and *channels*. On channels: *"If I message it in a shared public channel and my coworker messages it, whose auth is used for which runs?"*
- **User-level memory**, alongside the existing agent-level memory.
- **Built-in web search via Parallel**, billed through the LangSmith API key.

Still 6 shows the whole assembly.

**6. Decision models (15:51–18:00).** On **Jev** from **[[TypeSafe AI]]**: *"It's a decision model… It can't generate text, but it can make decisions."* Chase sets it beside frontier models: *"absolutely there will be these frontier models that are driving these really complex harnesses… But there's also a ton of other decisions that need to be made."* He gives three uses:
- **Evals**, after the fact or in the loop: *"if you can score it quickly according to some criteria as it's running… you can catch mistakes in real time."*
- **Guardrails**: *"One of the downsides of guardrails is that it always adds latency."*
- **Routing**: choosing *"which agents or which models or which skills or tools to load."*

Jev is reachable through the LangSmith LLM Gateway, as is **SemIf**, *"an open source decision model that we're hosting."* *"There's been a massive explosion in these open source decision models since Jev launched."* SemIf is the only one named. Stills 7 and 8.

**7. LLM Gateway (18:00–19:50).** In beta *"about a month or two ago."* It normalises requests to the OpenAI and Anthropic message formats, allows straight pass-through, and integrates with Codex, Claude Code and Cursor. The prescription: *"for governance and cost control reasons… you should be routing all of it through a single LLM gateway."* Features: spend limits per team, user and API key; rate limiting; provider fallbacks. Announced as coming soon are **stateful fallbacks**: *"if you notice that requests are failing and Anthropic might be down, you don't even try them… You just switch over to OpenAI for the next 10 minutes or 30 minutes."*

**8. Trajectories, fine-tuning, SmithDB, Custom Apps (19:50–26:03).**
- **Traces** are *"the system of record."* Runs, traces and threads give way to **LangSmith Trajectories**, because most agents *"run an LLM in a loop and compile this list of messages."* LangChain parses *"really complicated… trace formats that come in from all these different SDKs and different coding agents"* into that one format. Chase claims three benefits: faster debugging, simpler annotation, and data ready for post-training.
- **LangSmith Fine-Tuning** with the **smithtune** CLI turns selected trajectories into a trained model on **Fireworks AI** or **Baseten** (still 9), *"whether it's on agents or classification tasks or guardrails."*
- Trajectories are stored in **SmithDB**, an in-house database *"launched at Interrupt a few months ago"* (still 10).
- **LangSmith Custom Apps** is *"Lovable, but for your data that's already on LangSmith"* (still 11). It is built on LangChain's open-sourced design system and respects workspace RBAC/ABAC.

**9. LangSmith Engine v2 (26:03–30:45).** Engine *"sits on top of your traces in a tracing project… and it basically does all the things that an AI engineer would do."* It clusters issues onto an issue board, tries fixes in code, and adds evaluators and dataset examples (still 12). Version 2 adds two things:
- **Proactive fix testing** on LangSmith Deployment preview branches (still 13).
- **Red teaming**, which simulates hypothesised issues against the deployed agent (still 14). Chase: *"bad could be it learned something that it shouldn't have… It is off-brand in some way"*, and red teaming is *"really good for creating an initial eval dataset… we've heard for a while that creating evals is really hard and really painful."*

Usage to date: *"over 70 million traces"* scanned, *"over 21,000 issues"* detected; the improvement figures are on still 15. Engine comes to self-hosted LangSmith with bring-your-own-key in *"V17… in a week or two."* The closing slide (still 16) shows the three layers as launched.

## Visual canon

All 64 stills in the manifest were viewed. 38 were dropped: section cards, one-word pillar slides, earlier build states, and camera shots in which Chase stands in front of the slide. The 16 below carry content the narration does not. Four of them (3, 12, 14, 16) were **re-grabbed**: the frame Gemini picked was a camera shot. The same slide was found full-frame a few seconds earlier in its display window, by sampling the stream every 3 s. Each entry was transcribed from the pixels. Gemini's reading was wrong in two places that matter. On the Jev slide it read a `"bool"` question returning `false`, where the slide shows a `"noul"` probability of `0.999` from `jev-1.13.0`. On the SmithDB table five of the sixteen latency values were misread.

### 1 · Eight things around the model

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/07-02m26-components-around-the-model.webp|A model glyph in the centre, ringed by skills, tools, context, controls, fine tuning, system prompt, memory and model routing]]

*Still at [2:26](https://www.youtube.com/watch?v=950byF7njfw&t=146s) from LangChain, "Interrupt NYC: Opening Keynote".*

A model glyph at the centre, ringed by eight components: **Skills · Tools · Context · Controls · Fine Tuning · System Prompt · Memory · Model Routing**.

*Still vs. transcript:* Chase says companies are *"building a lot of stuff around"* the model. The slide names eight things, and puts fine-tuning and model routing in the same ring as the system prompt, skills and memory.

### 2 · Three reasons, with the evidence the slide cites

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/11-03m53-data-models.webp|Three panels: token economics with a Fortune headline on Uber, open models from NVIDIA, Kimi and DeepSeek, and a Larry Ellison quote on data over models]]

*Still at [3:53](https://www.youtube.com/watch?v=950byF7njfw&t=233s) from LangChain, "Interrupt NYC: Opening Keynote".*

| Token economics | Open models | Data > Models |
|---|---|---|
| **FORTUNE** — *"Uber burned through its entire 2026 AI budget in four months."* — Jake Angelo, May 26, 2026 | NVIDIA · Kimi · DeepSeek (logos) | *"All models are trained on publicly available data. To reach full value…you need to make privately owned data available to them as well."* — Larry Ellison |

*Still vs. transcript:* the narration states the three reasons in general terms. The slide attaches a press headline about Uber's AI budget, three open-model makers and an Ellison quote. None is mentioned aloud. The wiki has not checked the Fortune article or the quote's source.

### 3 · People: three rings

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/17-08m21-people-organizational-rings.webp|People: ring one platform engineers, ring two agent engineers, ring three non-technical builders]]

*Still at [8:21](https://www.youtube.com/watch?v=950byF7njfw&t=501s) from LangChain, "Interrupt NYC: Opening Keynote". Re-grabbed.*

Concentric rings, inner to outer: **Ring 1 — Platform Engineers · Ring 2 — Agent Engineers · Ring 3 — Non-technical builders**.

*Still vs. transcript:* the spoken ring 3 is *"subject matter experts inside and outside the company who are often the best people to decide what good looks like for an agent."* The slide calls the same ring *non-technical builders*. One wording puts them in the role of judging quality; the other has them building.

### 4 · The Deep Agents harness

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/24-11m50-runtime-deep-agents-harness.webp|Business logic, harness and infrastructure, with the Deep Agents harness broken into execution environment, context management, steering and delegation]]

*Still at [11:50](https://www.youtube.com/watch?v=950byF7njfw&t=710s) from LangChain, "Interrupt NYC: Opening Keynote".*

Left: **Business Logic → Harness** (highlighted) **→ Infrastructure**. Right, **Deep Agents Harness**:

- **Execution environment:** Filesystem · Sandboxes
- **Context management:** Skills · Memory · Summarization · Context offloading · Prompt caching
- **Steering:** Human-in-the-loop
- **Delegation:** Planning · Subagents

*Still vs. transcript:* the narration mentions the file system, the sandbox and compaction. The slide gives four groups, and files human-in-the-loop under the harness as *steering*.

### 5 · What LangSmith supplies as infrastructure

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/26-12m41-runtime-langsmith-infrastructure-components.webp|LangSmith infrastructure: runtime, tool server, sandboxes and LLM gateway, each with its components]]

*Still at [12:41](https://www.youtube.com/watch?v=950byF7njfw&t=761s) from LangChain, "Interrupt NYC: Opening Keynote".*

**Infrastructure** highlighted. **LangSmith**:

- **Runtime:** Streaming · Secrets Storage · Checkpointer · Task Queue
- **Tool server:** MCP · Auth Handler · Audit Log
- **Sandboxes:** Secret Proxy · Isolated Execution
- **LLM gateway:** Model Fallbacks · Cost Controls

*Still vs. transcript:* the narration names the four parts and says the tool server is *"something that we're working on."* The slide lists what each part contains. Two items appear only there: an **audit log** on the tool server and a **secret proxy** in the sandbox.

### 6 · A Managed Deep Agent, end to end

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/32-15m29-managed-deep-agent-on-langsmith-end-to-end-architecture.webp|Users reach a Managed Deep Agent on LangSmith through UI, Slack, Teams or GitHub; inside are Deployment, Context Hub, Sandboxes, LLM Gateway and Tracing plus Evals, connected to MCP servers and any model]]

*Still at [15:29](https://www.youtube.com/watch?v=950byF7njfw&t=929s) from LangChain, "Interrupt NYC: Opening Keynote".*

**Users → Agent Interface** (UI · Slack · Teams · GitHub) **↔ Managed Deep Agent on LangSmith**:

- **LangSmith Deployment:** Streaming · Runtime · Checkpointer · Auth Handler · MCP+A2A · Secrets Storage · Task Queue
- **Context Hub:** Instructions · Skills · Agent Memory · User Memory
- **LangSmith Sandboxes** · **LangSmith LLM Gateway** · **LangSmith Tracing + Evals**
- Below: **MCP Servers** · **Any Model**

*Still vs. transcript:* on screen for about seven seconds and not narrated. It names **Context Hub** as the store for instructions, skills and both levels of memory. It lists Teams and GitHub beside Slack as interfaces, and shows A2A next to MCP.

### 7 · Jev's launch in Google Trends

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/35-16m01-jev-launch-interest-over-time.webp|Jev launched: Google Trends interest over time, flat until mid-September, peaking at one hundred on September twentieth]]

*Still at [16:01](https://www.youtube.com/watch?v=950byF7njfw&t=961s) from LangChain, "Interrupt NYC: Opening Keynote".*

**Jev launched** — *Google Trends, interest over time*. The line sits at 0 from before Aug 30 to about Sep 11, rises from about Sep 13, and reaches the marked peak of **100 on Sep 20**.

*Still vs. transcript:* Chase says Jev *"launched over the weekend"*, and the chart dates the rise. Trends values are relative (100 = the series' peak), so the chart shows timing, not volume.

### 8 · What Jev takes and returns

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/36-16m22-what-is-jev.webp|What is Jev: a JSON request with a state and an is_urgent question, and a typed answer with probability 0.999, beside the claim 20 to 200 times faster and 40 to 400 times cheaper]]

*Still at [16:22](https://www.youtube.com/watch?v=950byF7njfw&t=982s) from LangChain, "Interrupt NYC: Opening Keynote".*

*You send a state and questions:*

```text
{
  "state": "Hi, I've been trying to connect   my Stripe...",
  "model": "jev-latest,
  "questions": {
    "is_urgent": {
      "type": "noul",
      "instructions": "The message conveys urgency or time-sensitivity"
    }
  }
}
```

*You get typed answers back (usage omitted):*

```text
{
  "model": "jev-1.13.0",
  "answers": {
    "is_urgent": {
      "type": "noul",
      "noul": 0.999
    }
  }
}
```

Beside it: **A decision model from TypeSafeAI** · **20-200x faster, 40-400x cheaper**. (The closing quote after `jev-latest` is missing on the slide.)

*Still vs. transcript:* the narration says *"You send it a state. You send it a list of questions."* The slide shows the shape and one answer: a support message scored **0.999** for urgency, as a probability rather than a yes/no. The speed and cost range is TypeSafe's and comes without a method, as in [[2026-09-21-runkle-langchain-building-a-harness-with-jev|Runkle's video]].

### 9 · The smithtune pipeline

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/49-24m05-langsmith-fine-tuning-pipeline.webp|LangSmith Fine-Tuning: trajectories from a tracing project pass through the SmithTune CLI's four steps, with training on Fireworks AI or Baseten, to an optimized model]]

*Still at [24:05](https://www.youtube.com/watch?v=950byF7njfw&t=1445s) from LangChain, "Interrupt NYC: Opening Keynote".*

**LangSmith Fine-Tuning** · `pip install smithtune` · **Your coding agent**, with an arrow into the CLI.

**LangSmith** tracing project → trajectories (user messages · model responses · tool calls + results) → **SmithTune CLI**: 01 Trace selection · 02 Data preprocessing · 03 Model training (Fireworks AI · Baseten) · 04 Model evaluation → **Output: Optimized model**.

*Still vs. transcript:* the narration covers the four steps. The slide also shows *your coding agent* as the one driving the CLI, which the narration does not say.

### 10 · SmithDB query latency

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/51-24m20-performance-improvement-across-agent-workloads.webp|Performance improvement across agent workloads: P50 and P99 query latency before and after for four query types, with speedups of six to fifteen times]]

*Still at [24:20](https://www.youtube.com/watch?v=950byF7njfw&t=1460s) from LangChain, "Interrupt NYC: Opening Keynote".*

**Performance improvement across agent workloads** — query latency, P50 / P99:

| Query | Before | After | Speedup |
|---|---|---|---|
| Load single trace | 860 / 2140 ms | 71 / 358 ms | 12x |
| Scanning and filtering | 530 / 5690 ms | 82 / 434 ms | 6x |
| Threads filtering | 1160 / 2370 ms | 131 / 268 ms | 9x |
| Full text search | 6200 / 13485 ms | 400 / 870 ms | 15x |

*Still vs. transcript:* the narration says SmithDB is *"a lot faster to ingest and store and query."* The slide gives figures. The speedup column is the P50 ratio (860 → 71 ms ≈ 12x). The *before* system, the workload and the method are not stated.

### 11 · LangSmith Chat builds custom apps

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/54-26m01-langsmith-chat-and-custom-app-extensions.webp|LangSmith Chat asks what we are building, with arrows to experiments, annotation queues, trace and thread views, and summaries and analysis]]

*Still at [26:01](https://www.youtube.com/watch?v=950byF7njfw&t=1561s) from LangChain, "Interrupt NYC: Opening Keynote".*

**LangSmith Chat**: *"What are we building? Build and refine your custom app. Add features, update the design, or ask for help fixing an issue."* Options: Add a feature · Update the design · Improve the app · Fix an issue. Input: *"Ask about this workspace…"*, model picker set to **Sonnet 5**. Arrows to: **Experiments · Annotation queues · Trace and thread views · Summaries and analysis**.

*Still vs. transcript:* the Custom Apps demo video ran without narration, and this is the slide after it. It names the four kinds of view the builder produces, and shows the builder running on an Anthropic model.

### 12 · Engine across the ADLC

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/56-26m28-langsmith-engine-accelerates-the-adlc.webp|LangSmith Engine accelerates the ADLC: code changes at build, add to datasets at test, context changes at deploy, add to online evals at monitor, inside a govern ring]]

*Still at [26:28](https://www.youtube.com/watch?v=950byF7njfw&t=1588s) from LangChain, "Interrupt NYC: Opening Keynote". Re-grabbed.*

A loop inside a **Govern** ring: **Build** — *code changes* → **Test** — *add to datasets* → **Deploy** — *context changes* → **Monitor** — *add to online evals* → Build. Centre: **LangSmith Engine accelerates the ADLC**.

*Still vs. transcript:* the narration says Engine *"tries to fix it with code. It tries to add an evaluator, add things to a dataset."* The slide assigns one Engine action to each phase. Two of them have no spoken counterpart: *context changes* at Deploy and *online evals* at Monitor.

### 13 · Engine tests its fixes

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/58-28m46-engine-tests-fixes-proactively.webp|Engine tests fixes proactively: spot issue in traces, confirm issue in production deployment, test fix in preview deployment, ship the verified fix]]

*Still at [28:46](https://www.youtube.com/watch?v=950byF7njfw&t=1726s) from LangChain, "Interrupt NYC: Opening Keynote".*

**Spot issue in traces** (output 3 failing) → **Confirm issue in production deployment** → **Test fix in preview deployment** (all outputs passing) → **Ship the verified fix**.

*Still vs. transcript:* in speech, Engine *"will spin up a preview branch on your deployment. It will confirm that that issue is in fact an issue"*, then spins up a second preview branch to test the fix. The slide's second panel says the issue is confirmed in the **production** deployment.

### 14 · Engine red-teams an agent

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/59-29m30-engine-red-teams-your-agents.webp|Engine red teams your agents: it reads past traces and GitHub repos, forms three issue hypotheses, probes the customer's agent and confirms one issue]]

*Still at [29:30](https://www.youtube.com/watch?v=950byF7njfw&t=1770s) from LangChain, "Interrupt NYC: Opening Keynote". Re-grabbed.*

**LangSmith Engine reads** *previous agent traces* and *GitHub repos* *"to understand the agent"* → **Issue hypotheses #1–#3**, each with one or two **probes** → **Customer's agent** (on LangSmith Deployment) → **responses #1–#5** → *Issue #1 not detected* · **Issue #2 confirmed → Engine user** · *Issue #3 not detected*.

*Still vs. transcript:* the slide says what Engine reads to form its hypotheses: the agent's past traces and its GitHub repository. The narration does not.

### 15 · Engine v2 figures

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/60-30m08-engine-v2-performance-improvements.webp|Engine v2 performance improvements: twice as good at finding on IssueBench, a quarter better fixes on Terminal Bench, and lower cost]]

*Still at [30:08](https://www.youtube.com/watch?v=950byF7njfw&t=1808s) from LangChain, "Interrupt NYC: Opening Keynote".*

**Engine v2 Performance Improvements:** **2x better finding** — *benchmarked on IssueBench* · **25% better fixes** — *benchmarked on Terminal Bench* · **40% lower cost**.

*Still vs. transcript:* the narration says *"better at finding issues, better at fixing issues, and then also making it a lot cheaper."* The figures and benchmark names appear only on the slide. The baseline is presumably Engine v1, but no method is given, and IssueBench is not otherwise in the wiki.

### 16 · The stack as launched

![[assets/2026-10-05-chase-langchain-interrupt-nyc-opening-keynote/63-31m06-langsmith-complete-product-stack.webp|LangSmith: intelligence layer with Engine V2 above runtime with Managed Deep Agents and observability and evals with trajectories, custom apps and fine tuning]]

*Still at [31:06](https://www.youtube.com/watch?v=950byF7njfw&t=1866s) from LangChain, "Interrupt NYC: Opening Keynote". Re-grabbed.*

**LangSmith** — **Intelligence:** LangSmith Engine V2 · **Runtime:** Managed Deep Agents 0.8 · **Observability & Evals:** Trajectories · Custom Apps · LangSmith Fine Tuning.

*Still vs. transcript:* the narration recaps the three layers. The slide adds the Managed Deep Agents version (0.8), and leaves the LLM Gateway and decision models off the summary.

## Dynamic-capabilities reading

- **`digital-seizing/balancing-digital-portfolios`.** The talk's model argument is about portfolio management: keep the harness model-neutral so the firm can move between frontier, open-weight and decision models per call. It also routes every call through one gateway that enforces spend limits and fallbacks. Chase frames neutrality explicitly as protection against a provider that *"can raise rates."*
- **`digital-transforming/redesigning-internal-structures`.** The three rings (platform engineers, agent engineers, non-technical builders) are a proposed internal structure for building agents. They name *agent engineer* as a new hybrid role between data science, software and ML engineering.
- **`digital-transforming/improving-digital-maturity`.** The governed build / test / deploy / monitor loop, *"traces as the system of record"*, and Engine's claim to automate the issue-to-fix-to-eval cycle are a vendor's account of what a mature agent practice runs.
- **`strategic-renewal/business-model`.** *Own your intelligence* is a claim about where a company's differentiation sits once models commoditise: the data, the domain-specific harness and post-trained models. Rogo, Harvey and JPMorgan Chase are the named cases.

## Related in this wiki

- [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase, Sproul & di Vittorio — Interrupt 26 (San Francisco, May 2026)]]: the same speaker at the previous Interrupt. It covers open models (capability, cost, trainability), agent identity on behalf of a user or a fixed account, and continual learning at the model, harness and context layers. This keynote refers back to it as where Managed Deep Agents and SmithDB launched.
- [[2026-05-09-chase-agent-development-lifecycle|Chase — The Agent Development Lifecycle (May 2026)]]: the essay that defines the build / test / deploy / monitor phases and the governance ring. This keynote's process and Engine slides (stills 12–13) use the same loop.
- [[2026-09-17-runkle-lovell-langchain-building-a-harness-with-jev|Runkle & Lovell — Building a Harness with Jev (Sep 2026)]] and its [[2026-09-21-runkle-langchain-building-a-harness-with-jev|video version]]: the `langchain-typesafe` integration, Jev's question types, and its uses in routing, auto mode and judging.
- [[2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals|Shea & Roche — Jev-as-a-Judge (Sep 2026)]]: Jev measured as an eval judge against three LLMs on five cases, with cost and latency per call.
- [[2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai|Huang / Sequoia — How Companies Are Building Their Own Intelligence (Aug 2026)]]: the opening of Sequoia's *Own Your Intelligence* event, listing why companies own parts of their AI stack. It also names Harvey.
- [[2026-08-06-garry-tan-own-your-intelligence|Garry Tan — Own Your Intelligence (Aug 2026)]]: the same phrase applied to one person's context, skills and harness.
- [[2026-07-08-jensen-huang-why-companies-need-open-agent-systems|Huang / NVIDIA, interviewed by Chase (Jul 2026)]]: open-weight models post-trained against the Deep Agents harness, and the joint NVIDIA–LangChain blueprint.
- [[2026-08-11-ummadisetti-langchain-toyota-deep-agents-rd-research|Ummadisetti / Toyota (Aug 2026)]]: one company's Deep Agents deployment, with skills authored per function by a central group.
- [[2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production|Zamora & Feroz / Google Cloud Tech (Sep 2026)]]: a LangGraph agent's traces made framework-neutral with OpenTelemetry and OpenInference, then evaluated.

## Linked entities and concepts

- **Entities:** [[Harrison Chase]] (speaker), [[LangChain]] (channel and vendor), [[TypeSafe AI]] (Jev).
- **Concepts:** [[agent-development-lifecycle]] (the loop and Engine's place in it), [[agent-harness]] (business logic / harness / infrastructure; the Deep Agents harness groups), [[open-source-ai]] (the three reasons and model neutrality), [[small-language-models]] (decision models next to frontier models).
- **Dangling** (single-source mention in this role, deferred): Rogo, JPMorgan Chase, Parallel (web search), Fireworks AI, Baseten, SemIf, and the customer logos Kyth, Consensus, Listen, Clay and Cogent. Harvey is named across several sources but has no entity page; it is not an author, so the promotion rule does not apply.

## Debates and supersession

- **A vendor keynote throughout.** Every figure here comes from LangChain or TypeSafe and is stated without method. That covers Engine v2's 2x / 25% / 40%, SmithDB's speedups, the 70M traces and 21K issues, and Jev's 20–200x / 40–400x. The customer quotes on a *"What teams are saying"* slide (Kyth, Consensus; not published here) and the customer logos on the Engine slide (Listen, Clay, Cogent) are vendor-selected.
- **Slide and speech disagree twice.** Ring 3 is *subject matter experts* in speech and *non-technical builders* on the slide (still 3). The Engine confirms an issue on a *preview branch* in speech and in the *production deployment* on the slide (still 13). The source does not say which is meant.
- **When Jev launched.** Chase, speaking on 24 September, says Jev *"launched over the weekend"*, i.e. 19–20 September. The Trends chart on his slide peaks on 20 September. The wiki's earliest Jev source, [[2026-09-17-runkle-lovell-langchain-building-a-harness-with-jev|Runkle & Lovell]], is dated 17 September. The wiki holds no TypeSafe primary source that would settle the launch date.
- **"A massive explosion" of open decision models** is asserted with one example (SemIf). Not substantiated here.
- **Unverified slide citations.** The Fortune headline on Uber's AI budget and the Larry Ellison quote (still 2) are shown, not discussed, and not checked.
- No supersession. The keynote extends the [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|May keynote's]] product line rather than retiring any claim in it.

## What was actually ingested

- **Transcript:** the full manual English caption track, 236 segments covering 0:06–32:02 of 32:10, in 14 creator chapters. There is one short gap inside speech at 6:37–6:48. Three demo videos ran without captioned speech: LangSmith Trajectories (21:06–21:49), Custom Apps (24:44–25:31) and Engine v2 (26:49–28:04). Gemini's stills scan returned no stills from inside the Trajectories and Engine v2 demos, so their content is not in this page.
- **Stills:** a full static scan by `gemini-3.8-flash` (185,798 tokens; 64 stills, all cut by stream seek with no download). Every still was viewed. 16 are published as webp, four of them re-grabbed from the split-screen layout. The manifest at `raw/videos/interrupt-nyc-opening-keynote.stills.md` keeps Gemini's unverified readings. The corrections are on this page.
- **Date:** the delivery date (24 September 2026) is from LangChain's Interrupt site. The filename uses the YouTube publish date, per the video contract.
