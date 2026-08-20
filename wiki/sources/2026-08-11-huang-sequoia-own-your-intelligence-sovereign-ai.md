---
type: source
kind: video
title: "How Companies Are Building Their Own Intelligence | Sonya Huang, Sequoia Capital"
author: ["Sequoia Capital"]
publisher: "Sequoia Capital (YouTube channel) — opening keynote of the *Own Your Intelligence* event; speaker Sonya Huang (partner)"
url: "https://www.youtube.com/watch?v=bMMv0bZzONg"
date_published: 2026-08-11
date_ingested: 2026-08-20
length: "~17:29 minutes (transcript ~491 segments; auto-generated captions, ASR-cleaned) — a keynote framing talk opening a workshop day"
raw: "../../raw/videos/how-companies-are-building-their-own-intelligence-sonya-huang-sequoia-capital.md"
tags: [sonya-huang, sequoia-capital, sovereign-ai, own-your-intelligence, own-vs-rent, open-weight-models, not-your-weights-not-your-product, neolabs, application-layer, intelligence-layer, post-training, harness-engineering, online-learning, rl-environments, synthetic-data, evals, context, kimi-k3, glm, harvey, legibility, decentralized-intelligence, vc-framework]
dynamic_capabilities:
  - digital-sensing/digital-scenario-planning
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/redesigning-internal-structures
  - strategic-renewal/business-model
relationships:
  - type: supports
    target: 2026-07-10-hugging-face-ceo-companies-done-renting-their-ai
    via: "the same own-vs-rent thesis one month apart, from a platform CEO and a venture investor, converging on the same memorable formulation. Delangue: companies *\"need to own AI and own models instead of renting them\"*, with cost-at-scale as the switching driver and concentration-of-power as the risk. Huang: *\"not your weights, not your product\"*, with cost listed first among four drivers and centralized-vs-decentralized intelligence as the framing. They differ usefully on WHERE the frontier sits — Delangue's flow is frontier-API-for-experimentation → open-model-for-production because frontier cost is prohibitive; Huang's stronger 2026 claim is that owning can now BEAT frontier performance in-domain, which reframes the choice from a cost sacrifice to a performance edge"
    confidence: 0.8
  - type: supports
    target: 2026-07-08-jensen-huang-why-companies-need-open-agent-systems
    via: "a substrate vendor and a venture investor making the same specialize-on-open-weights argument, and both naming the harness as a component of the owned stack rather than a bought one. Jensen Huang argues for building proprietary specialized super-agents on an open substrate and treats model + harness + post-training as a joint specialization; Sonya Huang's production stack is literally *\"a harness on top of a model\"*, with the harness listed among the things you configure yourself once you leave the closed-API path. Note both are talking their book — NVIDIA sells the compute for post-training, Sequoia owns the portfolio being urged to do it"
    confidence: 0.7
  - type: supports
    target: 2026-07-29-ng-washington-post-china-open-source-ai-competitiveness
    via: "both treat open-weight availability as the enabling condition for enterprise ownership of AI capability rather than as a licensing preference, and both name specific Chinese open-weight releases as the reason the calculus changed. Ng argues US competitiveness depends on open weights remaining available; Huang cites *\"the newest open-weight models, especially Kimi K3 and GLM-5.2, being extremely good\"* as why *\"owning your stack is no longer a performance sacrifice\"* — and separately notes Jensen Huang leading a push to keep open-weight models available in the US. The two sources approach the same dependency from policy and from portfolio-strategy vantages"
    confidence: 0.7
---

# Huang — How Companies Are Building Their Own Intelligence

> Sequoia Capital partner Sonya Huang opens our Own Your Intelligence event with the case for why more companies are choosing to own their intelligence, down to the weights. She lays out the four forces driving the shift: cost, speed, performance, and controlling your own destiny, and explains why the race for the application layer is becoming the race for the intelligence layer itself.
>
> Sonya shares an opinionated framework for deciding what to own vs. rent when assembling your AI stack, and another for how to get going from zero to one. With today's open-weight models near the frontier, she argues, owning your stack is no longer a performance sacrifice. It may be your performance edge.

## TL;DR

A **~17.5-minute opening keynote** by **Sonya Huang**, partner at **[[Sequoia Capital]]**, framing the firm's *Own Your Intelligence* event for *"about 80 portfolio company founders and AI leaders in the room."* She describes the day as *"half a rallying call and half technical how-to"* and flags her own limits twice — *"I'm not technical and so take this with a giant giant grain of salt."* The talk is a framework, not evidence.

**1. The definition, and the boundary she draws around it.** *"A sovereign is an independent state that has total self-governance. And so sovereign AI refers to companies owning their own intelligence without external dependencies down to the weights."* Immediately followed by the disclaimer that does most of the useful work: *"we are definitely not telling our companies to get off Opus or GPT. That is definitely not the message. For coding agents, for desktop work, for frontier-level APIs, the closed model APIs are wonderful."* The observed behaviour she is generalising from is **partial vertical integration** — companies *"wanting to build their own AI capabilities in parts of their products."*

**2. The framing: centralized vs. decentralized intelligence.** *"On one hand, you have centralized intelligence where a single all-powerful AI powers more and more of the world's GDP as a black box, sucking in all the data exhaust, all the data flywheels from the rest of the world. On the other hand, you have decentralized intelligence where the whole world builds on top of a solid core, but every individual person, company builds their own intelligence on top — bespoke to their own data, their own industries, their own personalization, their own way of working, their own taste, and so the ecosystem flourishes and individuality triumphs. No single company swallows the rest."* She names the zeitgeist support: Alex Karp, Satya Nadella, and *"just last week, Jensen led the charge in making sure that open-weight models remain available in the US."*

**3. Four drivers, in her stated order** —

- **Cost.** *"Especially for low, zero, negative margin companies, sovereign AI isn't a nice-to-have, it's a must-have."* With the inversion that makes it interesting: *"ironically, the more successful your AI product is, the higher your AI COGS tend to be. And so it's actually the companies that have been most advanced in their deployment of AI that have been the first to go on this journey."*
- **Speed.** *"In certain domains — coding is one of them, security is another one — a small distilled custom model can beat a large general one because speed is so important."*
- **Performance** — flagged as **new**: *"this is a relatively newer one. I would say last year most companies were not choosing to own their intelligence to generate better performance. But we're now at the point where open models can outperform closed ones on your domain."*
- **Controlling your own destiny.** Notably generous to the labs: *"Anthropic and OpenAI, I actually think to their credit, they've been really wonderful partners to a lot of the ecosystem, but companies are increasingly finding that they want their own set of independent legs to stand on as well."*

**4. The slogan, and its lineage.** She explicitly ports it from crypto: *"in the crypto days, there was this meme for the DeFi degens — not your keys, not your crypto. If somebody was custodying your crypto for you, it fundamentally wasn't yours. I hereby present the AI version of this meme: **not your weights, not your product**."*

**5. The strategic reframe — the race moves down a layer.** Building on a prior Sequoia slide about the AGI labs and application companies converging on the user-facing product from opposite ends: *"I think we're seeing a new dynamic emerge now, which is actually that battleground is increasingly becoming not just the race for the application layer but **the race for the intelligence layer**… It's actually about who can own the intelligence itself and shape better intelligence in the product. So the product is the intelligence."* Her evidence is applied research shipping from application companies: *"the hottest neolabs in my opinion are actually the applied research that we see coming out of companies right now like Harvey, like Factory, Glean, OpenEvidence, Sourcegraph… the research is spanning everything from evals and benchmarks to harness engineering to new algorithmic techniques for fine-tuning."* Hence: **"the application companies are the newest neolabs."**

**6. The four-step roadmap.**

- **Step 1 — Strategy: own vs. rent, per capability.** *"Sovereign AI isn't binary. You're not 0% or 100% sovereign."* Four decision factors: **cost** (how large a COGS line), **speed/latency** (*"is it a P0 or not?"*), **performance** (*"it used to be that you would choose open weights when you didn't care about performance"* — now potentially inverted in-domain), and **proprietary data**. Her worked examples are unusually crisp: in coding, **agents are still mostly rented** (*"you want strong out-of-the-box performance and latency isn't a P0"*) while **tab-autocomplete is mostly owned** (*"you really really care about speed and these API calls are so frequent that the costs really rack up"*). She adds a security company owning for speed/performance and post-training control, and bio companies owning because of proprietary-data value.
- **Step 2 — Team, with a specific anti-pattern.** *"Traditionally AI teams have frequently been organized hub-and-spoke — a single platform team supporting different AI application product teams. And what I've seen is that a lot of companies are shoehorning this AI platform team into doing the sovereign AI stuff as well. **I'd encourage folks not to do this.** Start from scratch here, because this fundamentally is not a platform-services capability. You want people that are able to think on their feet, think on the frontier and produce frontier-level research. And you want them to be playing offense, not just servicing teams."* Evidence offered is thin but concrete: *"Harvey, for example, has published a ton of research. They have just a team of seven."* On leader profile she notes both research-track and engineering-track backgrounds work.
- **Step 3 — Legibility**, which she flags as the most under-rated step. *"My guess is a lot of people in this room are doing wonderful research in-house internally and that not all of it is very externally legible."* The mechanism is buyer-side: *"every single buyer right now is choosing their AI champion… they're getting the same pitch over and over again, they're trying to discern which vendor is sophisticated enough to take me to the promised land. Increasingly that means putting out your own research."* Concretely: technical marketing, a separately-branded labs or research group, *"publishing research with high taste."* She credits Winston Weinberg for the CEO framing — drive substantive results, and control the narrative.
- **Step 4 — Technical roadmap.** The sequence she observes: strategy → **evals** (*"this is so important. It is unglamorous work. It is not fun work, but the more that you do up front the better positioned you are for everything after"*) → model routers and harnesses → post-training → in rarer cases mid-training and pre-training → **online learning**, *"setting that machine up so that live customer data is actually creating a feedback loop where your model, your intelligence is improving with every customer interaction."*

**7. The stack diagram — production vs. development.** *"Fundamentally I think of the production stack as **a harness on top of a model**."* Alongside it sits a *development stack*: *"the tools and vendors that you use to get your intelligence good."* Her comparison of the two regimes is the sharpest thing in the talk:

- **Closed-API regime**: foundation models plus out-of-box harnesses; you can still build your own harnesses, prompts, context and evals. *"I'd say this is a **higher floor, but it's a lower ceiling**, because you don't actually have the ability to take your own data, to take online production data and improve your own intelligence."*
- **Owned regime**: *"the minute that you start to think about owning your own intelligence, it is like **opening a Pandora's box**, because that beautiful clean API call is now having to train your own models. So instead of having a single model API and some good performance out of the box, you have to choose an open-source base, do a lot of post-training on top. For your harness, you've got a choice of several open harnesses and then it's up to you to configure the harness, the logic, the tools, the context."* And the development stack becomes load-bearing: eval monitoring and drift-watching, high-quality post-training data (*"sometimes this is expert trajectories, sometimes it's synthetic data, sometimes it's RL environments"*), and online learning.

**8. The 2026-specific claim.** *"The beauty of owning your stack is that you can actually drive frontier-level performance now. And so this is somewhat new, and in large part this is thanks to the newest open-weight models, especially **Kimi K3** and **GLM-5.2**, being extremely good. Because the weights are available, they're actually much more malleable than working with the closed APIs. And so you start with a baseline that's already close to frontier and then with a good enough technical roadmap — so with strong post-training, prompt harness engineering, online learning — you can actually reach **better than frontier** performance by owning your stack. And so this is new for 2026."*

**9. Context as a performance lever**, mentioned as an aside but worth recording: *"context is really really important to driving performance"*, with four flavours named — a vector database (Turbopuffer), an enterprise knowledge graph (Glean), open-source connectors via MCP, and *"even novel approaches to context… encoding context in the weights themselves"* (Engram).

## What was actually ingested

The **complete** keynote — all 491 caption segments across `duration: 17:29` / `length_seconds: 1049`, with all eleven chapter markers. The talk ends by introducing the day's workshop lineup (Fireworks on post-training, LangChain on harnesses and evals, Mercor on RL environments and synthetic data, Trajectory on online learning, Harvey on their full stack); **none of those workshops are in this recording.** This is the framing keynote only.

ASR cleanup was applied to proper nouns and jargon (*GBT* → GPT, *nail labs* → neolabs, *eels* → evals, *spine tuning* → fine-tuning, *sam grep* → Sourcegraph, *Kimmy K3* → Kimi K3, *GLM52* → GLM-5.2, *Ral environments* → RL environments, and others; full list in the raw file's `notes:`). Two individuals cited as example lab-leader profiles — "Nico" and "Alex" — could not be verified and are left as the ASR rendered them; the company name transcribed as *"south Alain"* is uncertain.

**Scope warning, load-bearing.** This talk contains **no measurements**. Every claim about cost, speed, or performance is a characterisation of a pattern the speaker says she observes across a portfolio; not one is attached to a number, a company name plus a figure, or a before/after. The single quantitative fact in the talk is *"a team of seven"* at Harvey. The "better than frontier by owning your stack" claim — the talk's headline and the most consequential thing in it — is asserted, not demonstrated, and the speaker prefaces her framework with two explicit disclaimers about being non-technical and opinionated.

**And it is talking its book, structurally.** Sequoia is an investor in the companies named as evidence (Harvey, Factory, Glean, Sourcegraph, OpenEvidence, Turbopuffer, Engram and the workshop vendors are portfolio or ecosystem companies), the audience is its own portfolio, and the event exists to move that portfolio toward a strategy. Treat the four drivers and the own-vs-rent grid as a **useful decision framework**; treat the empirical claims underneath them as unevidenced.

## Dynamic-capabilities tagging

- **`digital-sensing/digital-scenario-planning`** — the centralized-vs-decentralized-intelligence slide is scenario work in the cell's literal sense: two interpreted futures for the same technology, with the firm's strategic posture derived from which one it wants to inhabit. *"Analyzing scouted signals; interpreting digital future scenarios; formulating digital strategies"* describes the talk's first six minutes exactly — she reads the Karp/Nadella/Huang statements as signals, interprets them as a directional shift, and converts that into a portfolio-wide strategy prescription.
- **`digital-seizing/balancing-digital-portfolios`** — Step 1 *is* the cell. *"Sovereign AI isn't binary… an important part of the strategy is to draw the lines for which intelligence you want to own and which you're comfortable outsourcing"*, decided per capability against cost, latency, in-domain performance and data proprietariness. The coding example (rent the agent, own the autocomplete) is *"balancing internal and external options"* stated as a worked case.
- **`digital-transforming/redesigning-internal-structures`** — Step 2 makes a structural claim with a named anti-pattern: do **not** extend the existing hub-and-spoke AI platform team into model ownership, because *"this fundamentally is not a platform-services capability"*; stand up a small de-novo research group instead, playing offense rather than servicing teams. Step 3 adds a second structural artifact — a separately branded labs or research group whose output is externally published.
- **`strategic-renewal/business-model`** — *"the product is the intelligence"* is a value-creation-logic claim, not a tooling one: the assertion is that the defensible layer migrates from the application surface to the intelligence underneath it, so a company whose value capture rests on UI, workflow and go-to-market over a rented model is renewing onto a substrate it does not own. *"The application companies are the newest neolabs"* names the resulting identity shift.

## Linked entities and concepts

- [[Sequoia Capital]] — publisher and the speaker's firm. Updated in this ingest.
- [[concepts/open-source-ai|open-source-ai]] — open-weight models as the enabling condition; the Kimi K3 / GLM-5.2 near-frontier claim is recorded there.
- [[concepts/agent-harness|agent-harness]] — *"the production stack as a harness on top of a model"*, the open-harness configuration burden, and *harness engineering* named as a research area application companies now staff for.
- [[concepts/strategy|strategy]] — the own-vs-rent grid, the four drivers, and the race-moves-down-a-layer reframe.
- [[concepts/foundation-models|foundation-models]] — the closed-API vs. open-weights regimes and the higher-floor/lower-ceiling trade.
- [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] — the COGS inversion (most advanced deployers switch first) and the four-step adoption roadmap.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the four cells tagged above.
- [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|Delangue / Hugging Face via TechCrunch]] — the same own-vs-rent thesis a month earlier; see `relationships:`.
- [[2026-07-08-jensen-huang-why-companies-need-open-agent-systems|Jensen Huang / NVIDIA via LangChain]] — the substrate-vendor version of the specialize-on-open-weights argument, and referenced inside this talk.
- [[2026-07-29-ng-washington-post-china-open-source-ai-competitiveness|Ng / Washington Post]] — the policy vantage on open-weight availability.

**Dangling** (single-source mention, deferred per [author-entity promotion](../../CLAUDE.md#author-entity-promotion)): Sonya Huang, Harvey, Factory, Glean, OpenEvidence, Sourcegraph, Turbopuffer, Engram, Mercor, Fireworks, Trajectory, Kimi K3, GLM-5.2, Winston Weinberg, Alex Karp.

## Source quality note

Auto-generated captions, ASR-cleaned (see the raw file's `notes:`). Delivery is fluent; the surviving uncertainty is limited to two first names and one company name, all flagged above.

**This is investor content addressed to its own portfolio at an event designed to change that portfolio's behaviour.** The speaker discloses her non-technical vantage and labels the framework opinionated, which is more candour than the format requires and is worth crediting — but it does not change what the source can bear. It supports claims about **what a major venture firm was telling founders in August 2026 and how it framed the decision**; it supports no claim about whether owning a model stack actually pays, for whom, or at what scale.

The reason it earns a page is the **framework quality relative to its length**: the own-vs-rent grid (four factors, applied per capability rather than per company), the higher-floor/lower-ceiling characterisation of closed vs. open regimes, the explicit team anti-pattern, and the legibility step are all reusable independently of whether Sequoia's directional bet is right. The wiki now holds three sources on the own-vs-rent question from a platform CEO, a substrate vendor and an investor — a cluster whose shared blind spot is that **all three sell something that gets more valuable if enterprises stop renting**, and none of them measures the outcome.
