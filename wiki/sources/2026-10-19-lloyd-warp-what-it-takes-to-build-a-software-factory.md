---
type: source
kind: video
title: "What it takes to build a software factory"
author: ["Warp"]
publisher: "Warp — recorded talk with product demo by Zach Lloyd, founder and CEO"
url: "https://www.youtube.com/watch?v=x-PK3yx_MJg"
date_published: 2026-10-19
date_ingested: 2026-10-25
length: "~25:51 minutes (transcript ~61 segments + 5 stills; human-curated captions)"
raw: "../../raw/videos/what-it-takes-to-build-a-software-factory.md"
stills: "../../raw/videos/what-it-takes-to-build-a-software-factory.stills.md"
tags: [warp, zach-lloyd, software-factory, warp-factories, factory-engineering, product-engineering, agentic-development, cloud-agents, sandboxing, factory-as-code, open-infrastructure, ai-sovereignty, foreman-agent, orchestration, llm-as-judge, scoring, self-improvement, internal-benchmarks, model-routing, cost-per-pr, pareto-curve, factories-stack, slack, linear, github]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
  - digital-seizing/balancing-digital-portfolios
relationships:
  - type: supports
    target: 2026-05-05-stanford-ai-club-chamath-on-how-to-win-in-the-ai-era
    via: "both describe software production reorganised as a 'software factory' in which agents carry work from intent to shipped code under human review points"
    confidence: 0.6
  - type: supports
    target: 2026-10-20-hamalainen-lala-takkar-mckinsey-economics-of-enterprise-ai
    via: "both concern measuring AI by cost per successful outcome rather than usage, and routing each task to the cheapest model that does it well enough"
    confidence: 0.65
---

# Lloyd (Warp) — what it takes to build a software factory

> Software factories are the next step after interactive coding agents. Warp founder and CEO Zach Lloyd covers what a cloud software factory is, why it should be treated as open infrastructure defined in code, and how "factory engineering" helps your agents improve over time.

## TL;DR

A 26-minute recorded talk with a product demo on the **Warp** channel, published 19 October 2026. **Zach Lloyd**, Warp's founder and CEO and formerly a principal engineer who ran engineering for Google Docs, describes the *software factory* as the next stage after developers prompting coding agents on their laptops, and demonstrates Warp's product for it, Warp Factories. Five claims:

1. **Local interactive agents have three problems:** they are *"bottlenecked by people,"* their costs cannot be optimised collectively, and *"there's no central layer for governing them"*; a compromise acts *"as the logged-in user."* Sandbox them in the cloud.
2. **A software factory is a measurable loop.** Ideas come in; agents triage, write a spec, implement, review, verify with computer use, ship and monitor; people are looped in at review points. It runs in the cloud, because *"you can't have automations running off your laptops."*
3. **Treat it as open infrastructure defined in code.** The factory's agents, MCPs, repositories and skills are declared and versioned, so it can be tested and rolled back; it should accept *"any model, any harness,"* run on your own compute, and keep the data, because *"that data is what you're going to use to improve your agents."*
4. **Factory engineering** is a second kind of engineering beside product engineering: tune the factory using cost and flow metrics, LLM-judge *scoring* of every run, a *self-improvement* loop in which agents propose changes to the factory's own definition, and *internal benchmarks* that replay real tasks against different models.
5. **Warp's result:** cost per pull request from about $55 to around $15 *"in the last six weeks,"* PR throughput up about 40%, with a lower revert rate: *"So this isn't just putting out slop."*

## Key claims

### From autocomplete to factories

Lloyd's arc: Cursor-style autocomplete a couple of years ago; then, *"about a year ago,"* every developer running Claude Code or Codex locally and prompting features into pull requests; next, *"much more automated development."* Interactive agents leave productivity bounded by people, scatter cost, and lack governance. The factory he proposes is not one fixed process: *"This loop is going to look different in its details at every company, on every team."*

### Open, in code, and sovereign

He holds the factory should be infrastructure *"as flexible as GCP or AWS,"* composable and pluggable, working with the tools a company already has (work enters through Slack, Teams, Linear, Jira, GitHub or a local agent). Defining it in code *"creates opportunities: how do you test different versions of a factory? How do you let agents self-improve a factory?"* He uses the term *AI sovereignty* for keeping the factory's data, compute, inference gateway and model choice under the company's own control: *"open is going to win here, as opposed to a walled garden, single-vendor solution."*

### Factory engineering

The product engineer works *through* the factory; the factory engineer makes it *"more efficient… a lot of performance tuning: figuring out what skills and MCPs, what model mix, and what workflow are right."* Three tools:

- **Metrics:** human interactions per PR, degree of automation, time to ship, and cost per PR by source, user, agent and model, *"and having a plan in place to drive it down."*
- **Scoring:** LLM-as-judge over stored agent runs, sampled because it is expensive. Warp's example is *redundant tests*, a failure mode where agents *"waste a bunch of money, time, and context writing unnecessary tests."*
- **Self-improvement:** agents read the failed scores, find repeated problems (*"a problem with our triage agent. We saw this 54 times"*) and open a pull request against the factory definition so it does not recur.

### Your own benchmark

Recorded tasks can be added to a benchmark suite and replayed against different models and harnesses, producing *"a correctness-versus-cost trade-off curve"* for the company's own work rather than relying on SWE-bench or Terminal-Bench. In his run, GPT-5.6 Sol cost $6.23 on average for 95% correct; GLM-5.3 Flash cost about a third and was *"just a little less correct"*; *"we would probably choose GLM-5.3 Flash for this, honestly,"* and the result feeds a model-routing rule. Lloyd on the public conversation about models: *"It's hard to tell who has a conflict of interest."*

## Visual canon

### 1 · More AI usage is not more business value

![[assets/2026-10-19-lloyd-warp-what-it-takes-to-build-a-software-factory/04-03m12-more-ai-usage-more-business-value.webp|More AI usage is not more business value]]

*Still at [3:12](https://www.youtube.com/watch?v=x-PK3yx_MJg&t=192s) from Warp, "What it takes to build a software factory".*

**More AI usage != more business value.**

1. Ad hoc interactive usage, no automation
2. No systematic way to optimize cost and quality
3. No central layer for governance and control

Press clippings beside the list: *Forbes*, "Is The Cult Of 'Tokenmaxxing' Just Another Fad Or The New Normal?" (13 April 2026); *VentureBeat*, "The AI governance mirage: Why 72% of enterprises don't have the control and security they think they do"; *Forbes*, "Uber Burns Its 2026 AI Budget In Four Months On Claude Code."

*Still vs. transcript:* the narration names the three problems; the slide adds the press evidence Lloyd uses to motivate them, including the Uber budget headline.

### 2 · The cloud software factory loop

![[assets/2026-10-19-lloyd-warp-what-it-takes-to-build-a-software-factory/08-05m06-a-cloud-software-factory-lifecycle-loop.webp|The cloud software factory loop]]

*Still at [5:06](https://www.youtube.com/watch?v=x-PK3yx_MJg&t=306s) from Warp, "What it takes to build a software factory".*

A loop around *A cloud software factory*: Triage → Spec → Implement → Verify → Ship → Monitor, entered by **"New product idea or bug reported."** Three human touch points sit on the loop: **Reviewing the spec** (after Spec), **Reviewing the code** (between Implement and Verify), **Reviewing the product** (between Verify and Ship).

*Still vs. transcript:* the narration lists the steps; the diagram places the three human review points on the loop.

### 3 · Cost per pull request, by component

![[assets/2026-10-19-lloyd-warp-what-it-takes-to-build-a-software-factory/36-14m05-factory-spending-analytics.webp|Cost per pull request, by component]]

*Still at [14:05](https://www.youtube.com/watch?v=x-PK3yx_MJg&t=845s) from Warp, "What it takes to build a software factory".*

The factory dashboard's *Spending* tab, last 7 days: **cost per PR $16.42** ($5,351.38 total, approximate, 326 PRs). Hover on 13 October: $16.65 per PR average over 88 PRs, split **compute $5.22, platform $2.61, inference $8.82**. Below: *Spend by source* $4,988.78 ($498.88 per source, 10 sources: Slack, Warp Web, Scorer, Factory MCP, Scheduled, Linear, GitHub, Self-improvement, Other).

*Still vs. transcript:* the narration says to know your cost per PR; the dashboard shows a figure consistent with his ~$15 claim and that inference is about half of it, with compute and platform the rest. The workspace is labelled *wilson*; whether it is Warp's own production factory is not said.

### 4 · Benchmark: correctness against average cost

![[assets/2026-10-19-lloyd-warp-what-it-takes-to-build-a-software-factory/50-21m40-benchmark-results-correctness-vs-average-cost.webp|Benchmark correctness against average cost]]

*Still at [21:40](https://www.youtube.com/watch?v=x-PK3yx_MJg&t=1300s) from Warp, "What it takes to build a software factory".*

*WarpBench 0.1*, run of 2 September. Correctness (y, 87.2%–97.2%) against average cost (x, about $0–15), read from the plot: **gpt-5.6-sol (high)** ≈ 94.8% at ≈ $6; **glm 5.3 flash** ≈ 92.8% at ≈ $2; **grok 4.6 (high)** ≈ 92.8% at ≈ $8.5; **claude opus 5 (high)** ≈ 91.3% at ≈ $14; **gemini 3.7 flash** ≈ 89.6% at ≈ $3.7. A warning notes grok 4.6 and glm 5.3 flash had 28 of 29 tasks scored. The table below lists gpt-5.6-sol (high) at 0.95 correctness.

*Still vs. transcript:* the narration names only the two Pareto candidates; the plot shows all five configurations, with the most expensive model (Opus 5) neither the most correct nor on the frontier for this task set.

### 5 · The factories stack

![[assets/2026-10-19-lloyd-warp-what-it-takes-to-build-a-software-factory/51-24m38-the-factories-stack.webp|The factories stack]]

*Still at [24:38](https://www.youtube.com/watch?v=x-PK3yx_MJg&t=1478s) from Warp, "What it takes to build a software factory".*

| Layer | Components on the slide |
| --- | --- |
| 06 Access | Via Factory MCP (any coding agent) · Comms platform (Slack, Teams) · Task tracker (Jira, Linear) · Code forge (GitHub, GitLab) · Any device (web, mobile) · Programmatic (API, SDK) |
| 05 Orchestration | Native orchestration (triage / spec / impl / review / verify) · Multi-agent (Warp, Claude Code, Codex) · Human in the loop (live steering + handoff) · Automations (trigger / cron) |
| 04 Improvement | Metrics (autonomy, cost, cycle time) · Scorers (evaluate completed runs) · Benchmarks (compare models / skills per task set) · Self-improvement (automatic observer loop) |
| 03 Inference | Warp-hosted inference (multi-model, frontier + open-weight) · Bring your own inference (Bedrock, Vertex) · Custom model routing (LLM routing rules, self-improving) |
| 02 Compute | Sandbox (Docker image, Kubernetes, any remote env) · Agent runner (Mac / Linux / Windows, configurable disk/RAM/CPU) · Computer use (video / image) |
| 01 Data & context | Runs + transcripts (agent traces) · Agent memory (vector store) · Agent artifacts (PRs, reports, attachments) · MCPs / internal knowledge · (one item hidden by the speaker's video) |
| 00 Factories-as-code | Factory.yaml · Agent definitions · Automation definitions · Launch config (cut off) |

Layers 00–03 are marked *"Warp hosted or customer hosted."*

*Still vs. transcript:* the narration names the layers; the slide gives what goes in each, including the choice of hosted or customer-hosted for the lower four.

## Dynamic-capabilities reading

- **`digital-transforming/improving-digital-maturity`** — factory engineering as a managed capability: metrics, scoring, self-improvement and benchmarks applied to how software gets made.
- **`digital-seizing/balancing-digital-portfolios`** — model and harness choices made per task class from internal benchmarks, trading correctness against cost.

## How it connects

- [[concepts/agent-harness|agent-harness]] — the factory as a harness defined in code, with its own improvement loop.
- [[concepts/agent-fleet-management|agent-fleet-management]] — from scattered local agents to one governed fleet with fleet metrics.
- [[concepts/small-language-models|small-language-models]] — routing to the cheaper model when the benchmark shows it is close enough.
- [[concepts/ai-benchmarks|ai-benchmarks]] — internal, replayed benchmarks instead of public ones.
- [[2026-05-05-stanford-ai-club-chamath-on-how-to-win-in-the-ai-era|Chamath (8090)]] — another "software factory," from the requirements side.
- [[2026-10-20-hamalainen-lala-takkar-mckinsey-economics-of-enterprise-ai|McKinsey's Explainer on AI costs]] — cost per successful outcome and routing, from the buyer's side.

## What was actually ingested

The full talk (25:51, `length_seconds: 1551`) from the human-curated caption track, fetched with yt-dlp after the transcript panel failed. A Gemini static scan found 54 visuals (149,997 tokens); five were verified against their pixels and published. Most of the rest are demo screens whose content the narration covers; still 53 (a recap slide) was dropped because its two-second display window caught a transition.

## Linked entities and concepts

- [[concepts/agent-harness|agent-harness]], [[concepts/agent-fleet-management|agent-fleet-management]], [[concepts/small-language-models|small-language-models]], [[concepts/ai-benchmarks|ai-benchmarks]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the two cells tagged above.

**Dangling** (single-source mention, deferred): Zach Lloyd, Warp, Warp Factories.

## Scope and reliability

A vendor's talk and product demo on its own channel; Lloyd says so: *"Obviously, I'm not unbiased here."* The headline results (cost per PR $55 to $15, +40% throughput, fewer reverts) are Warp's own, without method; the dashboard shown is consistent with the cost figure. The benchmark is one 29-task suite on Warp's work, two of whose configurations were incompletely scored. The value for this wiki is the concept of factory engineering, a concrete stack for it, and the practice of benchmarking models on one's own recorded tasks.
