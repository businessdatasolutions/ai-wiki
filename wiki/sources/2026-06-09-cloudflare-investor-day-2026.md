---
type: source
kind: report
title: "Cloudflare Investor Day 2026"
author: ["Cloudflare"]
publisher: "Cloudflare, Inc. — investor presentation, New York Stock Exchange, 9 June 2026; presenters Phil Winslow, Matthew Prince, Rita Kozlov, Sam Rhea, Stephanie Cohen, Mark Anderson, Thomas Seifert"
url: "https://cloudflare.net/files/doc_downloads/Presentations/2026/06/15/New/Master-Deck-2026-Investor-Day-FINAL.pdf"
date_published: 2026-06-09
date_ingested: 2026-09-19
length: "193 slides (full deck read via pdftotext; slide text only — no spoken commentary; seven image-only or table slides checked visually)"
raw: "../../raw/reports/2026-06-09-cloudflare-investor-day-2026.md"
tags: [cloudflare, investor-day, agentic-internet, agentic-web, agentic-cloud, agents, code-mode, tool-calling, context-window, isolates, cpu-bottleneck, agent-execution, ai-code-review, vinext, emdash, 1000x-engineer, cloudflare-os, skill-files, context-layer, magic-inbox, ai-first-operating-model, workforce-reduction, gtm-ratios, ai-crawlers, x402, web-bot-auth, pay-per-crawl, machine-payments, time-to-exploit, mythos, project-glasswing, publisher-traffic, open-web, vendor-report]
dynamic_capabilities:
  - contextual/external-triggers
  - strategic-renewal/business-model
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - digital-transforming/navigating-innovation-ecosystems
relationships:
  - type: authored-by
    target: Cloudflare
    via: "the company's own investor presentation"
  - type: supports
    target: 2026-09-10-alim-pydata-ai-security-paradox-asymmetric-threats
    via: "exploitation now outpaces patching. Alim argues exploit generation became nearly free while patching stayed slow; Cloudflare's chart has the average time from vulnerability disclosure to confirmed exploitation falling from 2.3 years in 2018 to 23 days in 2025 and under 24 hours in 2026, which is the attacker half of the race his argument needs measured"
    confidence: 0.7
  - type: supports
    target: 2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering
    via: "code mode: agents should write code rather than call tools. Everitt lists Anthropic and Cloudflare code mode as a layer of the agentic-engineering stack; Cloudflare's deck gives the reasons — its own REST API needs 2.5 million tokens as a single MCP server against a 1-million-token context window, tool calling is 'an artificial injection that happens post-training', and models were trained on far more code than tool calls"
    confidence: 0.75
  - type: supports
    target: 2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot
    via: "AI review on every change once AI writes the code. Vo built a multi-dimension review bot because review, not authoring, becomes the bottleneck; Cloudflare runs up to seven specialised review agents (security, performance, code quality, documentation, compliance) on every merge request — 131,246 reviews across 48,095 merge requests in 5,169 repos in the first 30 days, median 3 min 39 s and $0.98 a review"
    confidence: 0.75
  - type: supports
    target: 2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer
    via: "the 1000x engineer, with a price attached. Hu frames AI-native companies around one engineer doing the work of a team; Cloudflare's deck uses the same phrase and supplies examples — a senior director reimplementing Next.js in under a week for about $1,100 in tokens, and a PM and one engineer rebuilding WordPress in two months"
    confidence: 0.65
---

# Cloudflare — Investor Day 2026

## TL;DR

The 193-slide deck from [[Cloudflare]]'s Investor Day at the New York Stock Exchange on **9 June 2026**. It is a company pitch to investors: every claim is made in favour of the stock, and **the spoken commentary is not in the file**. The CEO's "Vision" section is one photograph.

It is still one of the densest sources the corpus has on what the **agentic Internet** looks like from the infrastructure underneath it, and it states several things in numbers that other sources in the wiki only assert. The deck runs in seven acts:

1. **Agents need execution, not just intelligence.** Cloudflare argues **the CPU for execution, not the GPU, is "the next bottleneck to AI adoption"**. Its reasoning: agents create *"infinite ephemeral applications, many per user,"* which the hyperscalers' microservice model cannot scale. At 1 billion knowledge workers × 10 agents each ÷ 10 agents per CPU, that is **1 billion CPUs, about 20× current global server CPU production**.
2. **Agents must write code, not call tools** (code mode), because tool definitions overflow the context window and tool calling is a post-training add-on.
3. **Cloudflare runs itself on agents.** *"We are our own most demanding AI customer."*
   - An internal agentic workspace (**Cloudflare OS**) gives every employee an agent harness.
   - A **central context layer of skill files** is built through a "magic inbox" staffed by AI agent operators.
   - **AI code review runs on every merge request.**
4. **The web's business model is breaking**, with publication traffic down 30–97% from peak and human traffic down 35–40% in four industries within a year. Cloudflare's pitch is to become the market maker: crawler control, **Web Bot Auth**, and **x402** machine payments (co-founded with Coinbase and Stripe), with **2 billion HTTP 402 responses a day** and **AI agent requests up 1,700%+ in a year**.
5. **The attacker's window has collapsed.** Average time from vulnerability disclosure to confirmed exploitation fell from **2.3 years (2018) to under 24 hours (2026)**.
6. **An AI-first operating model.** The illustrative sales model shifts support headcount into quota carriers. The long-term model cuts **G&A from 10% to 3–5% of revenue** and **S&M from 36% to 23–25%**, and the safe-harbor slide discloses a planned **reduction of the current workforce**.
7. **Targets:** $5B annualized revenue before year-end 2028 (from $2.4B at year-end 2025) and GAAP profitability by 2028.

## Key claims

### 1. The coding-output explosion (Kozlov, developer platform)

- Generative AI *"has driven the cost of writing code to near zero"*, and *"it's now cheaper to rebuild a legacy app from scratch with AI than to migrate it. The economics have flipped."*
- **Growth indicators** (slide 15, year on year):

  | Indicator | Growth |
  | --- | ---: |
  | New websites (gTLD registrations, Verisign) | +34% |
  | New iOS apps (SensorTower) | +68% |
  | Merged GitHub PRs in public repos | +153% |
  | Cloudflare's Wrangler CLI downloads | +942% |

- **OpenClaw** is *"the fastest-growing repository in GitHub history"*: what React reached in 13 years, OpenClaw passed in 3 months.
- **Developers on Cloudflare** grew from 350,000 (Nov 2021) to 5.5M+ (Mar 2026). Its Vite plugin takes more than 10% of Vite's downloads because *"when AI coding agents generate modern web applications, they increasingly default to Vite."*

### 2. Why agents must write code

*"AI + Workflows + APIs = Agents"*, and agents are a function of **intelligence/reasoning** and **execution**. The case for code mode has three parts:

1. **Context-window limits.** *"Cloudflare's REST API requires 2.5 million tokens as a single MCP server. The most capable models today have a context window of 1 million tokens."* Even with larger windows, loading everything in-prompt floods the model *"with raw noise, skyrocketing token costs."*
2. **Lack of accuracy.** Models lack situational context such as the date and time, and supplying it costs extra tool calls or *"workarounds in the agent harness."*
3. **LLMs are bad at tool calling.** *"'Tool calling' is an artificial injection that happens post-training."* Too many tools collide (a CRM exposing both `create_contact` and `update_contact` produces duplicates), and it costs *"50,000 tokens per tool call for a simple task."* The metaphor: tool calling is *"like putting Shakespeare through a month-long class in Mandarin and then asking him to write a play in it."* But *"LLMs were trained on writing lots and lots of code."* The deck cites Anthropic's engineering post on code execution with MCP.

### 3. Execution is the next bottleneck

Microservices scaled by running many copies of *one* application; agents generate a new application on each run, *"infinite ephemeral applications, many per user."* Hence the CPU arithmetic in the TL;DR (1B knowledge workers × 10 agents ÷ 10 per CPU = 1B CPUs, against 35–45M server CPUs produced a year), and the claim that *"unpredictable CPU workloads driven by agents is the next bottleneck to AI adoption."* Cloudflare's answer is the V8 **isolates** it bet on in 2017: up to 100× more efficient because they reshare the runtime across runs, with a claimed **50% lower TCO** for agents against AWS and Vercel on its own pricing analysis. The agentic cloud *"needs new primitives"*: Durable Objects, isolates and Workflows, positioned as the 2026 counterpart to AWS's 2006 S3/EC2/SQS.

### 4. Cloudflare as its own AI customer (Rhea, CIO)

**Cloudflare OS** has four parts:

- a **one-click agent workspace**: *"full agent harness running in a Cloudflare container available to every employee seconds after they start work"*;
- a **centrally managed context layer**;
- **scoped access to systems of record**;
- **model optionality by use case and role**, with dynamic routing mapping *"employee roles and skill files to specific models"* to control cost.

The context layer is built by a five-step process that is new to the corpus:

1. Experts document workflows as **skill files**.
2. A **"magic inbox"** email alias takes everyone else's work.
3. The inbox is staffed by **AI agent operators** who run it as a service.
4. They collect and curate the use cases and convert them into skill files.
5. Everything is surfaced in Cloudflare OS.

The engineering examples (slide 184, "Supercharging a 10x engineer into a 1000x engineer"):

- **vinext.** A senior director managing 80+ engineers reimplemented Next.js on Vite with AI agents in under a week, for about **$1,100 in tokens**. It is claimed to build up to 4× faster with bundles up to 57% smaller.
- **EmDash.** One PM and one engineer rebuilt WordPress in TypeScript in **two months**, with plugins sandboxed in isolates (*"solving the security flaw behind 96% of WordPress vulnerabilities"*) and built-in x402 payments.
- **AI code review on every merge request.** Up to seven specialised agents (security, performance, code quality, documentation, compliance), coordinated by a top-tier model that posts one structured review. In the first 30 days: **131,246 reviews, 48,095 merge requests, 5,169 repos, median 3 min 39 s, median $0.98 a review, 100% coverage.**

Sales examples: agents research prospects for BDRs, give each seller a daily plan, generate custom decks, and let sellers draft their own solution-architecture proposals.

### 5. The business model of the Internet (Cohen, CSO)

- **Adoption speed:** generative AI reached 1 billion users in **2.5 years**, against 6 for smartphones, 8.5 for social media and 14 for the Internet.
- **Share of online attention on the open web:** 100% (2000s) → 55% (2015–22) → **25% (AI era)**, with social and AI taking 75%. The slide is labelled *"illustrative / directional … not a single measured series,"* anchored on a Pew click-through study.
- **Tech publications' Google traffic** fell **30% to 97%** from peak to January 2026 across ten named titles (Growtika, from Ahrefs estimates).
- **Human traffic fell 35–40%** between June 2025 and April 2026 in **retail, computer software, IT & services and financial services** (Cloudflare Radar).

Cloudflare's positioning is as the **"control plane for the Agentic Internet"**: a neutral market maker (*"no frontier LLM, no publisher competition"*) providing the six things it says a functioning market needs: reliable scarcity, analytics, value discovery, streamlined workflows, neutrality, and a payment system.

- **Crawl imbalance.** The top AI crawler sees up to **100×** more unique pages than others.
- **Agent traffic.** Daily AI agent requests rose **1,700%+** between 1 June 2025 and 31 May 2026.
- **Payments.** **x402** returns an HTTP 402 with a price, and the agent signs and retries. It runs at **2 billion 402 responses a day**, and Cloudflare frames *"every agent request [as] a metered event"* — *"from protecting websites from bots to monetizing trusted automated demand."*
- **A named deal case.** People Inc. blocked AI crawlers with Cloudflare and said its deal progress was *"much further along"* afterwards.
- **Media revenue.** The media vertical grew 37%+ year on year with 117% dollar-based net retention.

### 6. Security: the attacker's window

Slide 123, *"Frontier AI models change the attack landscape"*, charts the **average time between vulnerability disclosure and confirmed exploitation**:

| 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2.3 yrs | 1.9 yrs | 1.3 yrs | 11 mo | 10 mo | 5 mo | 56 days | 23 days | **<24 hrs** |

It is projected to fall further in 2027. **No source is cited on the slide**; the inset is Cloudflare's own blog post *"Project Glasswing: what Mythos showed us"*, about testing security-focused models on its infrastructure. Around it: Gartner's CIO Agenda 2026 has **IT budgets growing 2.8%** and **tech headcount 1.3%**, while **88% of organisations are increasing AI investment** (84% security, 72% cloud, 69% application modernisation). A revenue slide asserts that *"autonomous agents will automate a double-digit percentage of all work"* in the next 12 months.

### 7. The AI-first operating model (Anderson, revenue; Seifert, CFO)

- **Sales ratios.** *"Every GTM metric across the technology industry has historically scaled based on a ratio"* of quota-carrying account executives to support functions. *"AI is fundamentally changing these long-standing ratios."* The illustrative model (slide 183) keeps S&M cost flat at $18.275M:

  | Role | Before | After |
  | --- | ---: | ---: |
  | Account executives | 30 | 40 |
  | BDRs | 10 | 10 |
  | Solution engineers | 20 | 13 |
  | RevOps | 15 | 13 |
  | Marketing | 30 | 20 |
  | **Total** | **105** | **98** |

  Support roles fall by a quarter, account executives rise by a third, and ACV rises **35%**. It is labelled illustrative and is *"framework inspired by Battery Ventures."*
- **Long-term operating model, 2025 actual → updated long-term target:**

  | Line (% of revenue) | 2025 | Long-term target |
  | --- | ---: | ---: |
  | G&A | 10% | **3–5%** (previous target 8–10%) |
  | S&M | 36% | 23–25% |
  | R&D | 16% | 15–17% |
  | Operating margin | 14% | 30% |
  | Gross margin | 76% | 70–77% (widened down, because developer-platform products are "not optimized for gross margin") |

- **The workforce disclosure.** The safe-harbor slide's forward-looking statements include *"the plan to further accelerate our evolution to an agentic AI-first operating model and align our organizational structure with this new operating model, the estimated reduction of our current workforce, the estimated charges in connection with this plan."* The deck gives no number.

## Neighbour sources

- **Security.** [[2026-09-10-alim-pydata-ai-security-paradox-asymmetric-threats|Alim]] argued that AI favours the attacker because exploit generation is nearly free while patching is slow. Slide 123 measures the first half: under 24 hours from disclosure to exploitation. The second half, time to patch, is still unmeasured. See [[attack-surface-management]].
- **Code mode.** [[2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering|Everitt]] lists Cloudflare's code mode in his agentic-engineering taxonomy; this deck gives Cloudflare's own reasons for it.
- **Review at scale.** [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Vo's Merge Mommy]] is the single-developer version of the review pipeline that Cloudflare runs across 5,169 repos. Both share the premise that review capacity, not authoring, is now the constraint.
- **The 1000x engineer.** [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan & Hu]] give the framing; vinext and EmDash are costed examples.
- **Downstream.** [[2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet|Cloudflare's Content Independence Day report]] reuses this deck's web-economy slides as data.

## What was actually ingested

The entire deck, 193 slides, as extracted slide text. Seven slides carrying data only in images or tables were checked visually: 6, 15, 50, 105, 123, 126 and 183 (the values are recorded in the raw file's `notes:`). **The presenters' spoken remarks are not available**, so the reasoning behind many slides is inferred from their headlines. The CEO's section is a single photograph, and most customer names in the product sections are logos that did not extract. Financial detail beyond the operating model (the GAAP reconciliation, cohort charts) was read but is not summarised here.

## Dynamic-capabilities reading

- **`contextual/external-triggers`**: the deck is built on external shifts it wants investors to price in. Agent traffic is up 1,700%, human traffic down 35–40% in four industries, exploitation windows under a day, and IT budgets flat while AI spending rises.
- **`strategic-renewal/business-model`**: Cloudflare is renewing its own value-capture logic. It is moving from *"protecting websites from bots"* to *"monetizing trusted automated demand"*, from requests as a cost to requests as metered commerce (x402, pay-per-crawl, a content marketplace), framed internally as its "Act IV."
- **`digital-transforming/redesigning-internal-structures`**: the AI-first operating model is a structural redesign stated with numbers. It covers the sales ratio model (support 75 → 56, AEs 30 → 40), G&A cut to 3–5% of revenue, and a planned workforce reduction to *"align our organizational structure with this new operating model."*
- **`digital-transforming/improving-digital-maturity`**: Cloudflare OS is an explicit programme for *"leveraging digital knowledge inside the firm."* Experts' workflows become centrally managed skill files, a magic inbox harvests new use cases, and every employee gets an agent harness on day one.
- **`digital-transforming/navigating-innovation-ecosystems`**: co-founding the x402 Foundation with Coinbase and Stripe, promoting Web Bot Auth as an open standard with payment-network adopters, and positioning as the neutral party between publishers and AI labs.

## Linked entities and concepts

- Entities: [[Cloudflare]], [[Anthropic]] (code execution with MCP; Mythos, via Project Glasswing)
- Concepts: [[agentic-web]], [[agent-harness]], [[agentic-pull-requests]], [[ai-coding-productivity-evidence]], [[attack-surface-management]], [[enterprise-ai-adoption]], [[ai-employment-effects]]
- **Dangling** (single-source mention, deferred): Matthew Prince, Rita Kozlov, Sam Rhea, Stephanie Cohen, Mark Anderson, Thomas Seifert, Phil Winslow.

## Scope and reliability

**An investor pitch, the least neutral kind of source in the corpus.** Every chart was chosen to support the stock. The TCO comparisons are Cloudflare's own analysis of published prices. The CPU-bottleneck arithmetic rests on three assumed ratios (agents per worker, agents per CPU, knowledge-worker counts). The unit-economics slides are *"illustrative diagram[s]."* The safe-harbor slide warns about exactly this.

**Where the numbers are stronger.** Third-party sources are cited for the coding-output indicators (Verisign, SensorTower, the GitHub API), the adoption-speed comparison, and the Gartner CIO figures. The network measurements (agent requests, 402 responses, industry human-traffic declines) come from Cloudflare's own telemetry: real data from a large vantage point, but neither audited nor reproducible outside the company.

**The weakest load-bearing claim is the security chart**, because it is the one other pages will want to cite. The series is plausible and consistent with public time-to-exploit reporting, but the slide names no source or method. The drop from 23 days to under 24 hours coincides with a model release Cloudflare has a commercial interest in dramatising. Cite it as Cloudflare's chart, not as a measured fact.

**The workforce reduction is disclosed, not described.** The size, timing and functions affected are not in the deck. The long-term model's G&A and S&M targets show where the reduction points; they do not show what happened.
