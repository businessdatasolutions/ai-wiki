---
type: source
kind: video
title: "The Economics of Enterprise AI Explained"
author: ["McKinsey & Company"]
publisher: "McKinsey & Company — Explainer; Lari Hämäläinen, Wasim Lala and Kaavini Takkar"
url: "https://www.youtube.com/watch?v=qYefxlsfXAU"
date_published: 2026-10-20
date_ingested: 2026-10-25
length: "~19:27 minutes (transcript ~519 segments; auto-generated captions, corrected in quotes)"
raw: "../../raw/videos/the-economics-of-enterprise-ai-explained.md"
tags: [mckinsey, mckinsey-explainer, lari-hamalainen, wasim-lala, kaavini-takkar, ai-cost, ai-spend, tokens, token-pricing, consumption-based-pricing, per-seat-licensing, pilot-to-production, jevons-paradox, cost-per-task, cost-per-successful-output, agent-cost, stateless-models, context-window, reasoning-tokens, model-routing, open-weight-models, ai-control-plane, ai-finops, value-leakage, own-your-ai, roi, cursor]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/improving-digital-maturity
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-08-25-lukic-goydan-bcg-so-what-ai-costs-a-fortune
    via: "both concern enterprise AI bills rising as pricing moves from licences to consumption: frontier models on routine work (BCG's 'teenage driver' in a Ferrari, McKinsey's users moving from Sonnet to Opus), waste in the existing stack, and cost tied to measured outcomes"
    confidence: 0.75
  - type: supports
    target: 2026-10-01-chesky-silicon-valley-girl-people-who-know-what-to-build-with-ai
    via: "both date the turn from pushing AI usage to questioning AI spend to the first half of 2026: Chesky's token leaderboards that worked 'for a couple months', and Hämäläinen's 'up until end of Q1 this year everybody was worried about are we getting enough usage'"
    confidence: 0.65
  - type: supports
    target: 2026-10-06-kropp-bcg-so-what-lessons-from-an-all-ai-company
    via: "both concern token consumption as something to manage by its result rather than its volume: Kropp's productive use of tokens, and this episode's cost per successful outcome"
    confidence: 0.6
---

# Hämäläinen, Lala & Takkar (McKinsey Explainer) — the economics of enterprise AI

> Moving an AI tool from pilot to production can nearly quadruple its cost. Why is enterprise AI spending rising so quickly—and how can companies determine whether the investment is worth it?
>
> As generative AI moves from pilots into everyday work, the question of what it actually costs has become harder to answer. When companies first started using AI tools, they were mostly buying flat-rate licenses, which made budgets easy to predict. That era is ending. In 2026, AI providers are moving to consumption-based pricing, meaning companies now pay for every request a model handles. With more—and more complex—agents than ever, requests can quickly stack up. The costs of running AI also show up in cloud bills, software subscriptions, and the hours people spend checking outputs.
>
> In this Explainer, McKinsey's Lari Hämäläinen, Wasim Lala, and Kaavini Takkar break down why AI bills keep climbing, how token-based pricing works, and what it takes to run an AI agent. They draw on examples from their client work, including one bank where projected AI spend jumped from $3 million a year to more than $25 million once employees had access to every tool and model with no guardrails in place.

## TL;DR

A 19-minute *Explainer* on the [[McKinsey & Company]] channel, published 20 October 2026: three McKinsey consultants interviewed separately and cut together, **Lari Hämäläinen** (senior partner), **Wasim Lala** (partner) and **Kaavini Takkar** (associate partner). The ASR captions name no speaker; attributions below come from the on-screen name captions and a frame check at each turn. Five claims:

1. **Production costs about four times the pilot.** Takkar: *"Our research alone says on average, you move away from pilot into production, your AI spend goes four times."* The spend comes from three places: model providers, cloud compute for every model call, and AI embedded in SaaS tools.
2. **Pricing moved from seats to consumption in early 2026.** *"A lot of the frontier companies in quarter 1 of this year switched from per seat licensing… to now all consumption based,"* so the same use can cost *"two to three times more… instantaneously."* Takkar calls the order of events *"a very smart move"*: per-seat pricing got users *"hooked"* and prompting inefficiently first.
3. **Cheaper tokens, bigger bills.** Per-token prices fell *"almost by 90%,"* but usage rose faster: *"your standard Jevons paradox."* Agents, and agents running sub-agents, multiply the calls. Hämäläinen: *"it's not just about cost per token, it's really about cost per task."*
4. **Measure cost per successful outcome.** An agent's cost is model calls times token price, plus human review, observability, vector storage and orchestration, plus the reruns its failures cause. Compare that with the fully loaded alternative, and weigh how often the agent runs.
5. **Visibility first, then control.** A bank's projected AI spend rose from $3 million a year to more than $25 million once everyone had every tool and model *"without any ROI checks in place, any governance guardrails."* Its answer was *"one AI control plane"* across providers, cloud and SaaS, down to the individual user.

## Key claims

### Why costs are hard to predict

Lala opens with *"napkin math"*: estimates of what AI in a workflow will cost are still rough. Pilots run on licences, which are predictable; what is not predictable is open-ended access. Hämäläinen's example is McKinsey's own: many colleagues use [[Cursor]], and given a choice *"they choose the latest frontier models,"* which makes costs *"quite unpredictable… if you never control how much candy they eat, they might eat endless candy."* Lala's client: usage and spend both doubled between months two and four, and *"in the first couple of months, Sonnet was the model being used. Month 3, 4, 5, all of that usage had switched to Opus. I'm pretty sure all those users didn't need… a much more advanced model."* Takkar: *"AI cost is perhaps not hard to decipher. It's very complicated."*

### Tokens, and what makes them add up

A token is *"the smallest unit of what a model sees"* (Lala), comparable to *"a syllable"* of a word or a set of pixels (Hämäläinen), and the unit providers bill in, per million (Takkar). *"Hi ChatGPT, how are you?"* is about six tokens. Costs grow through output tokens, which are *"way more expensive"* than input; through context windows that are *"ballooning up because people are just throwing in as much reference as possible"*; and through the hidden *"intermediate thinking tokens"* of reasoning models. Hämäläinen adds that models are *stateless*: to remember anything they must be sent everything again, so *"the longer you… discuss… the more costs compound."*

### Consumption pricing and the Jevons paradox

Hämäläinen: *"It is simply economics."* The labs have raised or held prices and are moving tools to consumption pricing. Takkar's analogy for the result is mobile data: as the price per gigabyte fell, people moved from email to video calls. Per-token prices are down about 90%, but *"the volume, the consumption… has drastically gone up."* Lala describes the next multiplier: from chat windows, to agents, to *"an agent orchestrating four sub agents."* Hämäläinen dates the turn: *"up until end of Q1 this year everybody was worried about are we getting enough usage… And then the coding models… people suddenly woke up that hey a single user can rack thousands of dollars of bill literally in a day."*

### What an agent costs

*"It's hard to say how much an agent costs… like asking… what color is water?"* (Lala). A poorly designed agent can vary *"up to 30x in the number of tokens it consumes."* In IT ticket resolution, *"not all parts of this process need an agent"*: many steps are fixed if-this-then-that rules, where generative AI *"would be a waste of the token cost."* Takkar's full cost list is model calls times token price, plus human time to validate, observability, vector storage and orchestration. Her airline rebooking example shows failure as a cost: a customer who takes long to decide fills the context window, the seat is gone, and the process runs again.

### Measuring cost and value

Takkar's metric is **cost of the agent per successful output**, compared with the fully loaded cost of a person or the tool it replaces, and weighed against frequency: an airline's rebooking agent runs thousands of times a day; an agent that audits employees' tax filings runs once or twice a year.

Hämäläinen splits "AI" into three kinds with different value equations: **personal tooling**, whose value is indirect, *"more a cost of doing business"*; **automation**, judged on savings against build and maintenance; and **rebuilding** the business for AI. His example of the gap between speed and value: a five-engineer network-operations team got diagnosis and a proposed fix with every incoming ticket, which freed *"20 to 30% capacity."* *"Was there any dollar value here? Not really. I still need those five engineers. It is not enough to just create an agent and do something faster. You have to be able to link it to some sort of outcome that measurably improved. Otherwise, it's like building roads… you'll just fill up the roads with more cars."*

### Getting costs under control

Hämäläinen: *"Our clients need to be in control of their own AI."* They should own the workflow design, *"the harnesses, so the software… around the language model,"* and their data, and he expects open-source models run under their own control to be *"preferential… for many many of our clients."* Takkar's bank built a single control plane across model providers, cloud and SaaS, so spend can be traced to a team and a person: *"why didn't you route this particular request to an open weight model?"* Lala sees the same questions at other clients: the right model for the task, and prompts that do not paste in *"large documents… to get one or two facts"*, which at 100,000 employees doing it 20 times a day adds up. From thirteen years of cloud work he *"routinely"* finds 15–20% savings in cloud spend; *"executing it is the hard part,"* so the controls must be automated.

### Is it worth it? They disagree

Lala: *"absolutely worth it,"* if used for the right outcomes and with upskilling. Takkar: yes, if the organisation first redesigns its workflows, removes what is not needed and automates, and only then adds AI. Her example: two clients took the same customer-facing use case from pilot to production; one gained a lot, the other *"just threw a bunch of AI tools in the process."*

Hämäläinen dissents: *"In many ways… I personally feel it's not worth it. It's always worth it for an individual company… but it might not still be worth it for society."* His analogy is doping: if every sprinter is using growth hormones, *"you probably would be doing it as well… We as a society optimize today for profits… Then there's a different question: is that good?"*

## Dynamic-capabilities reading

- **`digital-seizing/balancing-digital-portfolios`** — choosing which model for which task (frontier, smaller, open-weight), which steps need an agent at all, and which use cases earn their cost by frequency and outcome.
- **`digital-transforming/improving-digital-maturity`** — the cost-management capability the episode describes: one control plane over all AI spend, traceability to team and person, automated controls, and teaching staff to prompt and manage context.
- **`contextual/external-triggers`** — the providers' switch from per-seat to consumption pricing in early 2026, which raised the cost of the same use from outside the firm.

## How it connects

- [[concepts/foundation-models|foundation-models]] — token pricing, consumption contracts and the Jevons paradox, next to the page's *cost per task as a competitive axis*.
- [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] — the ×4 jump from pilot to production, the end of the usage-push phase, and the control plane.
- [[concepts/micro-productivity-trap|micro-productivity-trap]] — the five engineers who gained 20–30% capacity and no dollar value, and two firms with the same use case and different results.
- [[concepts/small-language-models|small-language-models]] — routing to the right or open-weight model, and steps that need no generative AI at all.
- [[concepts/ai-sovereignty|ai-sovereignty]] — Hämäläinen's case for owning the workflow, the harness, the data and, increasingly, the model.
- [[2026-08-25-lukic-goydan-bcg-so-what-ai-costs-a-fortune|Lukic & Goydan (BCG)]] — the same cost story from another consultancy two months earlier.
- [[2026-10-01-chesky-silicon-valley-girl-people-who-know-what-to-build-with-ai|Chesky (Airbnb)]] — the token leaderboards that preceded the spending question.
- [[2026-10-06-kropp-bcg-so-what-lessons-from-an-all-ai-company|Kropp (BCG X)]] — token use as competition, with a warning about scripts that only run up the bill.

## What was actually ingested

The full Explainer (19:27, `length_seconds: 1167`) from auto-generated captions only; names and terms are corrected in quotes. The speakers are identified from on-screen name captions and frames sampled at each speaker turn; where a cut falls inside a passage the quote is left unattributed. The bank's starting spend is captioned as "23 million"; the video description's $3 million is used. No stills: interviews and one section card.

## Linked entities and concepts

- [[McKinsey & Company]] — publisher; the three speakers are its consultants, and McKinsey's own use of Cursor is one example. Updated in this ingest.
- [[Cursor]] — the coding tool whose users pick frontier models when they can. Updated in this ingest.
- [[concepts/foundation-models|foundation-models]], [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]], [[concepts/micro-productivity-trap|micro-productivity-trap]], [[concepts/small-language-models|small-language-models]], [[concepts/ai-sovereignty|ai-sovereignty]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the three cells tagged above.

**Dangling** (single-source mention, deferred): Lari Hämäläinen, Wasim Lala, Kaavini Takkar.

## Scope and reliability

A consultancy explainer whose speakers sell AI cost management. The figures are McKinsey's or from unnamed clients: ×4 from pilot to production (*"our research"*, no method given), a 90% fall in per-token price (*"what's quoted in the industry"*), up to 30× variance per agent, 15–20% cloud savings, and the bank's $3 million to $25 million-plus. None is sourced in the video. The value of the episode is a clear account of where AI costs come from, a usable metric (cost per successful outcome), and an open disagreement on whether AI is worth it for society.
