---
type: source
kind: video
title: "Kavak's Playbook for Rebuilding a Company Around AI"
author: ["a16z"]
url: "https://www.youtube.com/watch?v=n34CIw3gk1k"
date_published: 2026-08-10
date_ingested: 2026-09-16
length: "~36:31 minutes (transcript 346 segments / 11 chapters; auto-generated captions, ASR-cleaned)"
raw: "../../raw/videos/kavaks-playbook-for-rebuilding-a-company-around-ai.md"
tags: [alejandro-maza, kavak, a16z, angela-strange, gabriel-vasquez, latin-america, mexico, used-car-marketplace, agent-per-customer, long-running-agents, agentic-transformation, evals, superhuman-agents, ai-ceo, cuernavaca, jedi-academy, creative-destruction, schumpeter, ford-factory, electrification, token-tiering, org-design, middle-management, inverted-human-in-the-loop, opus-4-5]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - digital-seizing/strategic-agility
  - digital-seizing/rapid-prototyping
  - strategic-renewal/business-model
  - strategic-renewal/organizational-culture
relationships:
  - type: contradicts
    target: 2026-08-18-covello-gs-new-models-ai-investment-landscape
    via: "both address whether enterprises are yet making or saving money on AI. Covello, from Goldman's cross-company survey work: 'enterprises collectively are not making or saving money on their AI implementations.' Maza reports one firm handling 96% of interactions and 95% of transactions with agents, at 2.1x its human team's conversion, describing the architecture as having 'brought us to profitability'. The unit differs — a cross-sectional aggregate against a single firm that rebuilt itself around agents — and the layer Covello names as missing is close to what Kavak describes building"
    confidence: 0.8
  - type: supports
    target: 2026-05-07-kiron-schrage-compound-benefits
    via: "both argue that returns come from redesigning work around the technology rather than layering it onto existing process. Maza states the counterfactual as a historical mechanism — factories that swapped a coal engine for an electric one got roughly 6% while those rebuilt around small dynamos got 3x"
    confidence: 0.75
  - type: supports
    target: 2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai
    via: "both describe a firm investing engineering effort in the layer above the model — Huang in post-training and owned intelligence, Maza in the harness, evals and memory around a rented frontier model"
    confidence: 0.7
  - type: contradicts
    target: 2025-03-17-cemri-why-do-multi-agent-llm-systems-fail
    via: "both address whether multi-agent decomposition is the right architecture. MAST derives failure modes from observed multi-agent systems and treats them as engineering defects to be designed against. Maza reports abandoning a working multi-agent graph at scale on the view that decomposition itself constrains a sufficiently capable model — 'the intelligence now doesn't need the graph and the multi-agent lattice work and harness because it will constrain this level of intelligence'"
    confidence: 0.7
  - type: supports
    target: 2026-09-14-google-cloud-agent-factory-agent-harnesses-explained
    via: "both treat the harness as the durable investment and the model as swappable. Kavak rebuilt its harness to absorb new models as they ship — 'leverage recursive self-improvement or new models more intelligent models coming out every month' — and Maza uses the term harness unprompted throughout"
    confidence: 0.75
---

# Kavak's Playbook for Rebuilding a Company Around AI

> Angela Strange and Gabriel Vasquez are joined by Alejandro Maza Ayala, Chief Product & AI Officer at Kavak, to unpack how the Latin American used-car marketplace rebuilt itself around AI agents, with 96% of customer interactions and 95% of transactions now handled by agents.
>
> Alejandro explains why Kavak decided that simply giving employees AI tools wasn't enough, and instead redesigned the company's systems, teams, and customer experience around agents. They discuss why Kavak spends as much engineering effort on evals as it does building agents, how its AI sellers outperform its human teams, and an experiment where an AI "CEO" increased profits in one city by 50% in its first month.
>
> The conversation also explores what happens to organizational structure when agents do most of the work, why Kavak trains everyone from executives to mechanics to build with AI, and Alejandro's argument that companies looking for incremental AI adoption may be missing the larger opportunity: redesigning the organization itself.

## TL;DR

A ~36-minute **a16z Podcast** episode (10 Aug 2026) with **Alejandro Maza Ayala**, Chief Product & AI Officer at **Kavak** — the Latin American used-car marketplace — interviewed by **Angela Strange** and **Gabriel Vasquez**. Maza previously founded **OPI Analytics** and was building ML systems *"pre-transformers… like 2013."*

**This is the corpus's first end-to-end account of a company that rebuilt itself around agents and reports operating figures.** Nearly everything else the wiki holds on enterprise adoption is survey data, vendor testimony, or framework. Treat the numbers with the caution in §Source quality — they are unaudited and self-reported on a portfolio-company podcast — but the *architecture and the reasoning* are documented in unusual detail.

### The reported figures, in one place

| Measure | Reported |
| --- | --- |
| Customer interactions handled by agents | **96%** |
| Transactions handled by agents | **95%** |
| Agents instantiated per day | **100,000–200,000**, each with its own virtual machine |
| Agent lifetime | *"sometimes three minutes, sometimes eight hours, sometimes three days"* |
| AI seller vs human team conversion | **+50%** initially, **2.1×** now |
| NPS / customer satisfaction | **tripled** |
| Car-loan approval time | **under 3 minutes** (against *"two months or more"* typical in Mexico) |
| AI "CEO" of Cuernavaca, first month | target 2× profit, achieved **1.5×** |
| Warranty claims after mechanic sidekick | down ~**26%** |
| Eval investment | *"about the same amount of engineer time, tokens, and money on building the evals as building the agents"* |
| Customers in database | **10 million** |
| Mechanics in Mexico | **~800** |

## The three bets

Maza organises the transformation as three decisions, and is explicit that the first is where most companies stop.

1. **Redesign the company, not the workflow.** *"The first instinct is, okay, let's adopt AI, and you basically leave your structure as it is and just give ChatGPT or your Claude to your team — and then there's no efficiencies, your customers have the same problems and nothing happens. So you need to redesign your whole company around the agents and around the future capabilities. And this means really rebuilding most of your APIs, rebuilding your system so the agents can use them."* The design question he says they asked: *"how would we build Kavak in 2035 with Fable 10 or GPT-10 level intelligence"* — and *"actually that company looks very different than what we had built."*

2. **Build superhuman agents, defined against your own best hire.** *"By every dimension that matters — conversion, lifetime value, customer experience — our agents would outperform the best human we had ever hired. And we put them in front of the hardest problems."*

3. **Change what the company measures.** *"Kavak was a transactional company. We used to measure how many cars we bought, how many cars we sold, how many brake pads we needed to buy. And we moved to a relational company where now I have 10 million customers in my database and I have agents assigned to most of them with the task of maximizing their lifetime value."* The economics he attaches: *"just activating 1% of this customer base, it's like hundreds of millions of dollars."*

## The architecture, and the decision to destroy the previous one

**What runs now.** One long-running agent **per customer**, not per task: *"a virtual machine with an agent with access to memory and evals and the CLI where they can access every tool and every API in my company, and the long-term goal."* It *"will remember years of interaction of this customer with Kavak — what they visited on the web page, or a call they had two years ago,"* then *"come up with a strategy and set a long-term goal to maximize the lifetime value of this customer."* Agents sleep and wake: *"they set an alarm clock for their next task and they go back to sleep."*

**What was destroyed, and why.** Kavak had *"tens of thousands of these agents working at scale running the business back in December"* as multi-agent systems decomposed by function. Then *"Opus 4.5 came out and I realized this isn't the right paradigm anymore — the intelligence now doesn't need the graph and the multi-agent lattice work and harness, because **it will constrain this level of intelligence**."* So they *"decided to destroy everything we had been building for two years — that was working, that brought us to profitability, that brought us amazing growth — and start over with a harness that we thought would be robust and scalable."*

His generalised advice is unusually direct: ***"if I could advise everyone, don't build agentic workflows to graphs."***

**The stated reason to prefer one long-running agent:** it lets the organisation absorb model improvements instead of re-architecting around them — *"leverage recursive self-improvement or new models, more intelligent models coming out every month."*

## Evals as the brake that permits speed

*"I like to move extremely fast, but in order to move fast, you need to have brakes. Imagine a car — you'll hit on the gas just if you have the right brakes. And I've seen many companies get this wrong because they try to go slow because they don't have the right brakes. So I thought about it the other way around: **how fast can we go? Well, it depends on the quality of our evals.**"*

The resourcing rule — *"about the same amount of engineer time, tokens, and money on building the evals as building the agents"* — and the measurement rule, which is a direct attack on process metrics: *"I see companies measuring number of calls, or minutes during the call, or some superficial KPIs that give you some information but that doesn't really work. **The important thing is: did this customer convert? Is it bringing value to the customer, and is the customer happy to re-engage with us after a while?**"*

## The AI CEO experiment

They carved out a single city — **Cuernavaca, Mexico** — and *"put an agent in one of our harnesses as a CEO."* At six weeks: *"the goal of the first month was to double the profits. It didn't reach it, but it was 1.5x — like 50% more profits."*

What the agent does is closer to intense micromanagement than strategy: *"going into every single number, every single customer, making the perfect forecast, and going to micromanage every single thing that needs to be executed every day to reach a plan. So it'll literally send messages to all the physical workers in Cuernavaca with their plans for the day, and ask them to send voice notes back to know their progress."* Reported effects: customer satisfaction up, better inventory rotation, better financing penetration — *"every KPI started to improve."*

His framing of why this is notable: *"that was the last job AI was supposed to take, and no, it isn't really."*

## What humans still do, and the inverted human-in-the-loop

**The physical world is the boundary.** *"The jobs where we're still training and hiring humans, those are related to the physical world… when we talk about mechanics, Kavak has around 800 mechanics in Mexico. There's lots of dexterity and senses that's super hard to substitute."* Those mechanics get a sidekick agent — *"like the movie Ratatouille, the mouse that's actually a chef collaborating with a human"* — which *"tells them how to inspect a car and gives them tips."*

**The escalation path runs the other way from the standard pattern.** Maza's criticism of conventional human-in-the-loop: *"usually if an agent hits a wall or can't perform anymore, it'll send this case to a tier-2 support and forget about it. That doesn't really work, because you don't close the loops — so you don't generate the data to train the agent to do this better."* What Kavak does instead: the agent *"will call this API saying I need help. And on the other side, it's not an agent or software, it's a human helping them out."* The org-chart consequence he draws: ***"if you map this out in an org chart, it's really human teams that have an agent."*** And elsewhere: *"sometimes agents are the bosses of humans, and sometimes humans are designing the agents."*

## The Jedi Academy

*"We launched a program inside Kavak that's called the Jedi Academy, where anyone from Kavak — from the CEO to AI engineers to mechanics"* goes through six weeks and *"they launch state-of-the-art AI agents to production."* Maza designed and led it himself, and says it must be rewritten continuously *"because everything's changing so fast, and you can't send these people outside to Stanford to learn this because it's new stuff."*

The stated goal is not to produce engineers: *"maybe this person won't become an AI engineer — some of them have — but they know how to collaborate with this new technology."* The change-management framing was explicitly not optional: *"there's no way back. This is the way Kavak is going… You have the choice to train and get the skills to perform in this new reality, **or maybe leave Kavak if this is not for you**, but this is the way we're going."*

**Resulting org shape:** *"very flat teams, very senior teams, super empowered. If you look at a team, you'll have engineering, AI, operations — everything. And they're either building the agents, working for the agents, or being in the physical world in front of the customer."*

## Token tiering — a framework the corpus does not otherwise hold

Asked what he tells leaders who report high adoption and high spend, Maza distinguishes tokens by whether their return is measurable:

- **Tier 3 (most valuable)** — tokens spent by agents doing the organisation's actual work, *"where you can get the ROI of each specific token… because it goes to agents that are performing the job of the organization. These are the best tokens."*
- **Tier 2** — measurable indirectly: *"do I see devs in the codebase, and I can evaluate the value of these tokens at least indirectly."*
- **Tier 1 (where he says most companies are)** — *"people are just using Claude Code or ChatGPT or Cowork or whatever. What happens with those? **I have no idea.**"*

His conclusion: *"it's not just about adoption. It's really about having a very clear vision and then measuring that each token you spend is bringing you those benefits."*

## Creative destruction, and the Ford factory argument

Maza's explanation for why incumbents under-realise, via **Schumpeter**: innovation reaches the economy *"not by companies adopting the new technology but by [entrants] with the new technology destroying the old companies."*

The worked historical case is the strongest passage in the episode. *"The technologies for Ford's production line were developed in 1879 and 1881 — Edison started commercializing electricity in New York and then London, and he invented a dynamo that was extremely efficient. **So you could have built Ford's factory 40 years before Ford.** The technology was there, everything was there. But the way people adopted electricity and Edison's dynamo was: okay, I'm going to leave my factory like four floors, shafts and belts, and just change my coal engine for an electric engine. And this will bring you benefits, yes, **but like 6% efficiency**. What needed to be done was to destroy that factory, build it on a flat surface, not in the center of New York but in Connecticut or New Jersey, and redesign your whole factory around small dynamos and electricity. And then you get the **3x improvement in productivity** that powered the US during the 20th century."*

His application: *"the same is happening again today. People want to adopt it, but they're not willing to redesign the whole company and they just adopt it superficially. And in the end, that'll give you a **6% or a 10% improvement, not a 10x improvement.** It's like the innovator's dilemma at an industrial scale."*

Why he thinks incumbents structurally can't: *"it's really hard for a CEO today, especially of a large company or public company, to go and say, hey, I'm betting everything on AI… I'll destroy and rebuild everything I've been building for the past 40 years. **How many CEOs will do that in a company at scale?**"*

## Two further framings worth keeping

- **On the unit of self-improvement.** *"People are super obsessed with RSI now… But if you look at it this way, economic value in humanity for the past 4,000 years has been delivered by **organization**, not by individuals. So what you want to self-improve is the organization that can deliver more economic value."*
- **On what he is actually buying.** The episode's opening line: ***"I'm investing more today in tokens than in knowledge workers."***

## How this source touches the Warner & Wäger cells

- **`digital-transforming/redesigning-internal-structures`** — the cell's canonical case. Not a new reporting line but a rebuilt one: flat senior cross-functional teams, middle management largely gone, and the inverted escalation path where humans staff a queue that agents call (~22:45–25:15). *"Rebuilding most of your APIs, rebuilding your system so the agents can use them"* (~5:41) is the same claim at the systems layer.
- **`digital-transforming/improving-digital-maturity`** — the **Jedi Academy** (~20:13–22:40) is a workforce-maturity programme in the cell's exact sense: everyone from CEO to mechanic trained, six weeks, shipping to production, curriculum rewritten continuously because no external provider teaches it.
- **`digital-seizing/strategic-agility`** — *"rapidly reallocating resources; accepting redirection and change"* describes the December decision to scrap two years of working multi-agent architecture after a model release (~28:44–30:20).
- **`digital-seizing/rapid-prototyping`** — the AI-CEO experiment (~16:13–20:10) is a scoped pilot in a single city with a stated target and a six-week readout.
- **`strategic-renewal/business-model`** — the transactional-to-relational shift (~6:35–7:20) is a value-capture change, not a tooling one: the unit moves from the car sold to the customer lifetime, and the addressable economics move with it.
- **`strategic-renewal/organizational-culture`** — the *"train, or maybe leave Kavak"* framing (~21:49–22:10) plus *"we strengthened the culture, everyone was super excited"* is a deliberate culture reset attached to the transformation.

## Related in this wiki

- **Whether enterprise AI is paying.** [[2026-08-18-covello-gs-new-models-ai-investment-landscape]] states that enterprises collectively are not making or saving money and names a missing data-management and model-orchestration layer. This source reports one firm's figures and describes building that layer. [[micro-productivity-trap]] and [[enterprise-ai-adoption]] hold the question.
- **Whether multi-agent decomposition is right.** [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail]] catalogues multi-agent failure modes as engineering defects; this source reports abandoning the pattern on capability grounds. [[multi-agent-failure-modes]] holds both.
- **The harness as the durable investment.** [[2026-09-14-google-cloud-agent-factory-agent-harnesses-explained]] argues for a fixed harness with curated tools and context; [[agent-harness]] holds the engineering account, [[agent-fleet-management]] the scale question, and [[agent-oversight-and-delegation]] the escalation design.
- **Where a firm puts engineering effort above the model.** [[2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai]] describes startups investing in post-training and owned weights; Kavak rents the frontier model and invests instead in the harness, memory and evals around it. Two different answers to the same question about which layer a firm should own.
- **Redesign versus adoption.** [[2026-05-07-kiron-schrage-compound-benefits]] and [[2026-07-22-brown-wef-meet-the-leader-entry-level-jobs-in-an-ai-era]] both argue returns follow work redesign.
- **The macro backdrop.** [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs]] reports economy-wide effects far smaller than anything here, which is the reconciliation question [[ai-employment-effects]] now carries.

## Linked entities and concepts

- Entities: [[a16z]] (publisher), [[Kavak]] (subject; entity page created on this ingest), [[Anthropic]] (Opus 4.5 is the release that triggered the re-architecture).
- Concepts: [[agent-harness]], [[multi-agent-failure-modes]], [[agent-fleet-management]], [[agent-oversight-and-delegation]], [[micro-productivity-trap]], [[enterprise-ai-adoption]], [[automation-vs-augmentation]], [[ai-employment-effects]], [[ai-benchmarks]], [[warner-wager-process-model]].
- **Dangling** (single-source mention, deferred): **Alejandro Maza Ayala**, **Angela Strange**, **Gabriel Vasquez**, **OPI Analytics**, **Joseph Schumpeter** (cited).

## Source quality

- **Every number is self-reported, unaudited, and delivered on the podcast of a firm with an interest in the outcome.** a16z is a venture capital firm; the format is promotional in the ordinary sense. None of the figures in the table above has a stated definition, baseline, or measurement window:
  - **"2.1× conversion"** — against which human cohort, over what period, on which segment, with what selection into agent-handled leads? Not stated.
  - **"96% of interactions / 95% of transactions"** — an interaction is undefined, and a firm that has redesigned its funnel around agents partly determines its own denominator.
  - **"1.5× profits"** in Cuernavaca — one city, six weeks, no control city, no baseline seasonality, and the profit base is unstated. This is an anecdote with a number attached, not a result.
  - **"warranties down ~26%"** — the raw ASR reads *"around like 20 26%"*; the single figure is the safer reading and is not certain.
- **Kavak's own financial position is not disclosed here.** Maza says the prior architecture *"brought us to profitability,"* which is the only profitability claim in the episode and is made about the system he then discarded. The company's overall economics are not discussed.
- **The strongest content is not the numbers.** The architecture decisions, the eval-resourcing rule, the token tiering, the inverted escalation path and the Ford/Edison argument are all independently useful and do not depend on the figures being accurate. Cite those; cite the figures as claims.
- **Transcript quality: ASR only.** The auto-generated captions mangled the Spanish proper nouns badly — *Kavak* appears as Kabak, Kaak, Karak and **Quebec**; the AI-CEO city appears as Quavaka/Guavaka/Cornabaka and is **Cuernavaca**; and the word *evals* — central to the episode — is never once transcribed correctly. All normalised at acquire time and itemised in the raw file. **Four readings are inferred rather than certain** and are flagged there: *"Edison's dynamo"*, the Schumpeter *entrants*-versus-*incumbents* sentence, the warranty figure, and the mechanics' sidekick name *"El Mike"*.
- **One dating note.** Maza says the multi-agent architecture was running at scale *"back in December"* and was replaced after *"Opus 4.5 came out"*; the episode does not date the rebuild precisely, so the two-year and December references are approximate as stated.
- **Scope.** Full episode ingested, 0:00–36:15 of a 36:31 runtime.
