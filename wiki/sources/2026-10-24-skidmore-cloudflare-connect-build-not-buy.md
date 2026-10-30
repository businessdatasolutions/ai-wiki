---
type: source
kind: video
title: "It's time to build, not buy (Cloudflare Connect 2026)"
author: ["Cloudflare Developers"]
publisher: "Cloudflare — Cloudflare Developers channel, Cloudflare Connect 2026"
url: "https://www.youtube.com/watch?v=-_qUn_LfJ6M"
date_published: 2026-10-24
date_ingested: 2026-10-30
length: "~22:13 minutes (transcript ~592 lines + 6 stills)"
raw: "../../raw/videos/its-time-to-build-not-buy-cloudflare-connect-2026.md"
stills: "../../raw/videos/its-time-to-build-not-buy-cloudflare-connect-2026.stills.md"
tags: [cloudflare, cloudflare-connect, ryan-skidmore, build-vs-buy, internal-tools, personal-software, ai-code-review, merge-requests, opencode, saas-inflation, vendor-lock-in, token-prices, metr-time-horizon, disposable-software, non-determinism, developer-productivity]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - digital-seizing/rapid-prototyping
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-06-09-cloudflare-investor-day-2026
    via: "the same internal reviewer, reported at 30 days in the Investor Day deck and at seven months here"
    confidence: 0.8
  - type: supports
    target: 2026-07-06-sevilla-emarketer-custom-ai-coded-apps-trim-saas-expenses
    via: "firms replacing bought software with software they build using AI"
    confidence: 0.6
  - type: supports
    target: 2026-05-05-nishar-nohria-end-of-one-size-fits-all
    via: "AI changing the economics that made standard bought software the default"
    confidence: 0.6
  - type: supports
    target: 2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot
    via: "building an AI pull-request reviewer rather than buying one, because review became the bottleneck"
    confidence: 0.65
  - type: contradicts
    target: 2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free
    via: "whether AI-built software replaces bought SaaS: Skidmore's 'you can build it' and a grid for when to, against a SaaS founder's 'I don't think you can vibe code a CRM'"
    confidence: 0.55
---

# Skidmore (Cloudflare Connect) — it's time to build, not buy

> "Don't reinvent the wheel" has always been one of the golden tenants of software engineering — but what happens when the wheel becomes really cheap to reinvent? In the past, buying off-the-shelf software almost always made more sense than building something from scratch, but over the last 12 months, the economics have shifted dramatically, and now all it takes is an engineer getting a little too frustrated with janky SaaS software to build a custom replacement in an afternoon. In this talk, we walk through how we've been navigating the build-vs.-buy debate at Cloudflare and how it's changed a lot of our procurement decisions. We use our custom AI code reviewer as a case study of how we built something from the ground up instead of buying something off the shelf, and we discuss the challenges and hurdles we ran into along the way.

## TL;DR

A 22-minute talk at Cloudflare Connect 2026 by **Ryan Skidmore**, who works on developer productivity and AI at [[Cloudflare]] and built the company's internal AI code reviewer. The title overstates the talk: its conclusion is a grid in which two of four cells say buy. Five claims:

1. **The old rule was right for its time.** Building meant months of work, a team and an on-call rota; buying meant someone else was woken at 3 a.m. Buying now has costs of its own (SaaS inflation of 16.4%).
2. **Building got cheaper in two ways.** Token prices for a given capability fell about 75 times in two years, and the tasks agents can finish grew, on [[METR]]'s measure, from 4 minutes (GPT-4) to 12 hours (Claude Opus 4.6).
3. **The case study is large.** Cloudflare's reviewer has run 1,024,037 reviews across 345,797 merge requests since March, at a median $0.67 and 1 min 34 s per review. It started as a git diff and *"a dumb prompt"*, built in an afternoon after off-the-shelf tools proved not flexible enough.
4. **Owning is the part that stays hard.** *"Building got cheap, but owning it is still kind of a problem for now."* A thousand people each building personal software means *"a thousand versions of slightly different but kind of the same software."*
5. **Expect to throw it away.** The answer to the tech-debt objection is that a replacement in six months will take *"probably half the time with 100% better features,"* so a tool need not last.

## Key claims

### Why the sums changed

Skidmore's slide on buying costs cites Vertice and Zylo: 16.4% SaaS price inflation in June 2026, about four times US CPI; 65% of licences unused or underused; 79% of IT leaders hit with price rises at renewal (see [Visual canon](#visual-canon)). On capability, he compares two models scoring about the same on the MMLU benchmark, March 2023 and April 2025, and gets a 75-fold fall in input-token price, adding that it *"isn't like an apples to apples comparison."* On task length he uses METR's time horizon, and says the measure has *"hit its limit"* with Opus 5 and 5.5. The slide is more exact: those models are marked *"not measured"*, because METR's suite tops out at 16 hours for a reliable score.

### The reviewer

Review is good at catching bugs and sharing knowledge and is also *"one of the most reliable ways to slow down an engineering team."* Before the tool, the median wait for a first review *"was often measured in hours"*; now it is *"measured in minutes."*

The route to building it had three steps:

1. Off-the-shelf reviewers. *"Some of them were really good,"* but *"none of them were flexible enough."* Sales staff said yes to every requirement, *"but that doesn't come with any guarantees."*
2. A git diff and a prompt telling the model to go and find problems. *"It wasn't that effective, but it was better than nothing."*
3. An *"overengineered"* reviewer on the OpenCode harness, used for six to nine months. He says he studied how [[Claude Code]]'s review tool worked and built his own version on GitLab.

About 500 merge requests to the reviewer's own code have come from people across the company. *"If someone in the company sees a bug … they can just make the change."* Every merge request has had to be approved by it for about nine months, which has made some engineers *"really quite angry."* It has blocked about 16,000 merges in four months. There are failover and *"break glass"* routes for when a provider goes down.

Early versions flagged everything. After feedback the team flagged only what people act on, and people acted on more of it. A blog post the day before the talk reported a 68% cut in the inference bill.

### What it cannot do

It sees the diff, not the design. Checking cross-system impact across up to about a hundred services *"would probably take about 3 hours"*, an unacceptable delay on a merge request. Races need a race checker. Some merge requests run to millions of lines. *"It doesn't replace human review."*

### When to build

The grid has two axes: how critical the software is, and how much you need to bend it to how you work. His checks before building are: name the problem, build the smallest test, count the whole job, reuse what exists, measure from day one, keep a way out. *"Just because you can build it doesn't necessarily mean it's the right idea."* He advises an afternoon's prototype over committing people to *"a very big maybe."*

### From the Q&A

- **Why review in CI if the developer's laptop runs the same model?** *"If AI was deterministic, that would be fantastic."* It is not, so the reviewer reviews *"from like five different angles"*. A local version exists.
- **Standards.** Cloudflare passes linters and RFCs to agents as skills, which *"don't necessarily always get invoked when they should."* Recent models wait for CI after opening a merge request, read the comments and *"loop until everything's good to go."*

## Dynamic-capabilities reading

- **`digital-seizing/balancing-digital-portfolios`**: the build-or-buy grid, keeping an exit from every vendor, and weighing token spend against a licence.
- **`digital-seizing/rapid-prototyping`**: an afternoon's first version, small enough to throw away, shown to people before anyone commits to it.
- **`contextual/external-triggers`**: falling token prices, longer agent task horizons and SaaS price inflation changing a procurement rule.

## Visual canon

### 1 · But buying has its own costs

![[assets/2026-10-24-skidmore-cloudflare-connect-build-not-buy/04-03m49-but-buying-has-its-own-costs.webp|But buying has its own costs]]

*Still at [3:49](https://www.youtube.com/watch?v=-_qUn_LfJ6M&t=229s) from Cloudflare Developers, "It's time to build, not buy".*

- **16.4%** SaaS price inflation, a new record! June 2026, about 4x US CPI
- **65%** of SaaS licences unused or underused, Q2 2026
- **79%** of IT leaders hit with price rises at renewal in the past 12 months

Vertice: SaaS inflation (Jun 2026), licence use (Q2 2026) / Zylo: 2026 SaaS Management Index

*Still vs. transcript:* the sources, and *"about 4x US CPI"*. The speaker says 65% of people *"just never use"* a licence; the slide says *"unused or underused."*

### 2 · Agents keep finishing longer tasks

![[assets/2026-10-24-skidmore-cloudflare-connect-build-not-buy/06-05m36-agents-keep-finishing-longer-tasks.webp|Agents keep finishing longer tasks]]

*Still at [5:36](https://www.youtube.com/watch?v=-_qUn_LfJ6M&t=336s) from Cloudflare Developers, "It's time to build, not buy".*

Task length a model finishes half the time, log scale, 2023 to 2026:

| Model | Task length |
| --- | ---: |
| GPT-4 | 4 min |
| Claude 3.7 Sonnet | 1 hr |
| GPT-5 | 3.4 hr |
| Claude Opus 4.6 | 12 hr |

16 hr: METR's limit for a reliable score. Mythos Preview, Opus 5, Opus 5.5: not measured. **12x in one year:** Claude 3.7 Sonnet to Opus 4.6; METR's suite topped out before Opus 5 shipped.

METR Time Horizon 1.1 (last updated Sep. 2026) / Anthropic: Opus 5 (Jul. 2026), Opus 5.5 (Sep. 2026)

*Still vs. transcript:* all the values except GPT-4's and Opus 4.6's, the 16-hour limit, and the wording *"not measured"* where the talk says the benchmark *"can't measure it anymore."*

### 3 · 1,024,037 reviews since March

![[assets/2026-10-24-skidmore-cloudflare-connect-build-not-buy/12-12m07-1-024-037-reviews-since-march.webp|1,024,037 reviews since March]]

*Still at [12:07](https://www.youtube.com/watch?v=-_qUn_LfJ6M&t=727s) from Cloudflare Developers, "It's time to build, not buy".*

**1,024,037** reviews since March, across 345,797 merge requests. **6,907** repositories since 10 March. **$0.67** median cost per review, since 5 October. **1m 34s** median review time, since 5 October.

Reviewer telemetry, 10 Mar.–12 Oct. 2026 / costs at list price

*Still vs. transcript:* the exact counts, the review time, and two scoping notes: the cost and time medians cover only the week since 5 October, and costs are at list price. The narration rounds to *"just over a million"*, *"about 350,000"* and *"just under 7,000."*

### 4 · It flags very little, on purpose

![[assets/2026-10-24-skidmore-cloudflare-connect-build-not-buy/13-12m46-it-flags-very-little-on-purpose.webp|It flags very little, on purpose]]

*Still at [12:46](https://www.youtube.com/watch?v=-_qUn_LfJ6M&t=766s) from Cloudflare Developers, "It's time to build, not buy".*

**1.2** findings per review in the first month.

| Category | Findings |
| --- | ---: |
| Code quality | 74,898 |
| Documentation | 26,432 |
| Performance | 14,615 |
| Security | 11,985 |
| Engineering standards | 9,654 |
| AGENTS.md | 6,878 |
| Release | 745 |

Security: fewer findings, 4% of them critical. Cloudflare blog (Apr. 2026) / 145,207 specialist findings of 159,103 total

*Still vs. transcript:* the whole breakdown; the talk gives none of it. The rows sum to the slide's 145,207, and 159,103 findings over the 131,246 first-month reviews in the [[2026-06-09-cloudflare-investor-day-2026|Investor Day deck]] gives the 1.2.

### 5 · What it can't do

![[assets/2026-10-24-skidmore-cloudflare-connect-build-not-buy/14-14m21-what-it-can-t-do.webp|What it can't do]]

*Still at [14:21](https://www.youtube.com/watch?v=-_qUn_LfJ6M&t=861s) from Cloudflare Developers, "It's time to build, not buy".*

| Limit | Why |
| --- | --- |
| Architecture | It sees the diff, not the design behind it |
| Cross-system impact | It can't check the three consumers downstream |
| Timing-dependent races | Hard to spot in a static diff |
| Very large diffs | Seven frontier-model calls still cost money |

**Importantly, it doesn't replace human code review.** Cloudflare blog, "Orchestrating AI Code Review at scale" (Apr. 2026)

*Still vs. transcript:* the seven frontier-model calls per review. The narration speaks of up to a hundred services, the slide of three downstream consumers.

### 6 · Where building makes sense

![[assets/2026-10-24-skidmore-cloudflare-connect-build-not-buy/16-17m07-where-building-makes-sense.webp|Where building makes sense]]

*Still at [17:07](https://www.youtube.com/watch?v=-_qUn_LfJ6M&t=1027s) from Cloudflare Developers, "It's time to build, not buy".*

| | It fits | More need to bend it to how you work |
| --- | --- | --- |
| **More critical** | **Buy it, keep an exit** | **Build it** (nothing on sale fits) |
| **Less critical** | **Buy it** | **Build something small** (it needs bending; expect to replace it) |

*Still vs. transcript:* the axes. The narration walks the four cells without naming what separates them.

## How it connects

- [[concepts/agentic-pull-requests|agentic-pull-requests]] — seven months of reviewer telemetry after the 30-day figures already on that page, and the findings breakdown.
- [[concepts/vibe-coding|vibe-coding]] — personal software, an afternoon's prototype, and the cost of a thousand near-identical tools.
- [[concepts/ai-coding-productivity-evidence|ai-coding-productivity-evidence]] — first-review wait from hours to minutes, self-reported.
- [[concepts/ai-benchmarks|ai-benchmarks]] — METR's time-horizon suite topping out at 16 hours.
- [[concepts/agentic-engineering|agentic-engineering]] — agents that wait for CI, read review comments and loop.

## Related in this wiki

- [[2026-06-09-cloudflare-investor-day-2026|Cloudflare Investor Day 2026]] — the same reviewer at 30 days: 131,246 reviews, a median $0.98 and 3 min 39 s.
- [[2026-07-06-sevilla-emarketer-custom-ai-coded-apps-trim-saas-expenses|Sevilla (EMARKETER)]] — named firms that replaced SaaS tools with apps they coded with AI.
- [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar & Nohria (HBR)]] — AI dissolving the logic of standardised enterprise software.
- [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Vo (Merge Mommy)]] — a pull-request reviewer built in one Codex session.
- [[2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free|Ramineni (Fireflies)]] — *"I don't think you can vibe code a CRM."* Skidmore's examples are internal tools, and he names no system of record; he says only that some legacy SaaS products *"I don't think I'm allowed to name"* could be examined for replacement.
- [[2026-07-07-sinofsky-amble-a16z-software-in-the-age-of-agents|Sinofsky (a16z)]] and [[2026-09-08-gauch-bcg-so-what-will-ai-agents-replace-your-crm|Gauch (BCG)]] — where the difficulty of replacing enterprise software lies.

## What was actually ingested

The full talk and Q&A (22:13, `length_seconds: 1333`) from the transcript panel, auto-generated captions, 592 lines; ASR cleaned in quotes (*"remitt"*, *"llinters"*). The speaker names himself in the talk. A full static Gemini scan (131,850 tokens, 18 stills) was verified against the pixels for the six published here. Gemini had misread two findings counts on still 4 (78,908 and 14,815) and a footer on still 2, so the readings above are from the images. The slide's GPT-4 and GPT-4.1 mini prices were not re-verified and are not quoted.

## Linked entities and concepts

- [[Cloudflare]] — employer and publisher; `Cloudflare Developers` recorded as an alias. Updated in this ingest.
- [[METR]] — the time-horizon measure on the slide.
- [[Anthropic]] and [[Claude Code]] — models on the chart; the review tool he studied.
- [[concepts/agentic-pull-requests|agentic-pull-requests]], [[concepts/vibe-coding|vibe-coding]], [[concepts/ai-coding-productivity-evidence|ai-coding-productivity-evidence]], [[concepts/ai-benchmarks|ai-benchmarks]], [[concepts/agentic-engineering|agentic-engineering]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the three cells tagged above.

**Dangling** (single-source mention, deferred): Ryan Skidmore, OpenCode, Vertice, Zylo.

## Scope and reliability

An engineer describes a tool he built, at his employer's conference, and Cloudflare also sells parts of the stack it runs on (Workers, KV, AI Gateway). The telemetry is Cloudflare's own and unaudited. Volume, cost and speed are reported; the share of findings that were correct, and any effect on change failure rates, are not. *"People do act on them"* has no number. The value of the talk is that it sets a build-it case beside the costs a builder inherits, from the person on call for it.
