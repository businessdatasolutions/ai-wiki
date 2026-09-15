---
type: source
kind: video
title: "Garry Tan: New Rules for Founders"
author: ["a16z"]
publisher: "a16z (The a16z Show); host Anish Acharya (General Partner, a16z); guest Garry Tan, President & CEO of Y Combinator"
url: "https://www.youtube.com/watch?v=fsTtKywmWlU"
date_published: 2026-08-12
date_ingested: 2026-09-15
length: "~51:28 minutes (auto-generated transcript, ASR-cleaned; 447 segments across the channel's own 12 chapters)"
raw: "../../raw/videos/garry-tan-new-rules-for-founders.md"
tags: [garry-tan, a16z, anish-acharya, y-combinator, token-maxing, skillify, markdown-file-is-an-employee, business-loops, harness-wars, above-the-api-line, agentic-companies, gbrain, gstack, openclaw, provenance, saas-economics, solo-founders, vibe-coding, toyota-production-system, middle-management, venkatesh-rao, san-francisco-politics, vendor-adjacent]
dynamic_capabilities:
  - digital-sensing/digital-mindset-crafting
  - digital-seizing/rapid-prototyping
  - digital-transforming/redesigning-internal-structures
  - strategic-renewal/business-model
relationships:
  - type: supports
    target: 2026-08-06-garry-tan-own-your-intelligence
    via: "the same speaker six days later to a different audience, and the overlap is close enough that the pair should be read as one position stated twice. Startup School gave the founder-facing version (skillify, GBrain, own your skills); this gives the investor-facing version and adds what the keynote did not — **token maxing** as a deliberate spend ('$50 or $100,000 a year to use the agents at full strength'), the provenance-and-conflict problem that appears once you have many skill files, and the **harness wars** prediction for 2027"
    confidence: 0.9
  - type: supports
    target: 2026-08-14-blomfield-yc-building-structuring-ai-native-company
    via: "two YC voices two days apart on the same structural claim — that the org layer AI removes is the middle. Tan's version is blunter and has a mechanism attached: 'the mid level of bureaucracy should be agents', because the constraint being relieved is that 'the business becomes too big to fit in one person's head.' Blomfield describes the resulting company shape; Tan names what the agents are replacing and why"
    confidence: 0.8
  - type: supports
    target: 2026-09-07-yc-paper-club-why-the-harness-matters-more-than-the-model
    via: "the president of YC predicting, four weeks before YC's own Paper Club made harnesses the subject of a research night, that 'next year 2027 will be like the harness wars.' Read together they are an institution's leadership and its technical community converging on the harness as the contested layer — Tan from consumer-market economics ('it's really a cost thing, it's just too expensive right now'), the Paper Club from research genealogy"
    confidence: 0.75
  - type: supports
    target: 2026-08-31-blum-how-i-ai-claude-cowork-pm-system
    via: "the same self-improving-skill-file loop described from the CEO seat rather than the PM seat, and reaching the same two disciplines. Blum's system rewrites its own context files and detects terms it does not know; Tan describes turning each feat of strength into 'a markdown file plus code plus tests that can be reused and put into a cron job', and independently names the maintenance problem Blum solves by hand — provenance and conflict resolution across accumulated files"
    confidence: 0.75
  - type: contradicts
    target: 2026-07-31-collison-yc-startup-school-is-ai-breaking-the-lean-startup-playbook
    via: "not on facts but on tempo, and both are YC-platformed within a fortnight. Tan's white pill is that everything is *slower* than Silicon Valley thinks — 'it's going to be 20 years', 'there are real moats… a Microsoft isn't going anywhere', and he calls this 'a little antithetical to what most people in Silicon Valley would say.' Collison's is that the founder's window is unusually open right now. They are reconcilable (incumbent inertia is exactly what creates the window) but they point founders at opposite time horizons"
    confidence: 0.65
---

# Garry Tan — New Rules for Founders (The a16z Show, August 2026)

> Garry reflects on turning down an early opportunity to join Palantir, why chasing what's "hot" is often the wrong strategy… They also explore how AI changes the economics of company building, why traditional SaaS may be losing its advantage, and how tiny teams equipped with hundreds of agents can build businesses at a scale that once required entire organizations. The conversation goes deeper into agentic companies, taste and agency, why "a markdown file is an employee," and how AI could remove layers of bureaucracy that have historically limited organizations… the coming "harness wars," why AI adoption may take longer than Silicon Valley expects.
>
> *— Channel description, [[a16z]] (The a16z Show); host Anish Acharya, guest [[Garry Tan]]*

## TL;DR

**[[Garry Tan]]**, President and CEO of [[Y Combinator]], interviewed by a16z's Anish Acharya six days after [[2026-08-06-garry-tan-own-your-intelligence|his Startup School keynote]]. Roughly the first third is career narrative (turning down Palantir; leaving web programming in 2003 for Windows Mobile) and the last sixth is San Francisco local politics. **The middle twenty-five minutes are the reason to hold this page.**

Its distinctive contributions over the Startup School talk are three: **token maxing** as an explicit budget decision, the **provenance and conflict** problem that emerges once a company runs on accumulated markdown, and the **harness wars** call for 2027.

## Token maxing — the operating-cost claim

The frontier labs are, in Tan's account, rationing:

> *"The frontier model labs that are letting you use ChatGPT or Claude — I think that they're still pretty constrained on cost and pretty constrained on amount of compute they want to give you. And so if you really want to token max, you actually have to use something like Hermes agent or OpenClaw… let me load a million tokens or 800,000 tokens into any given request."*

The stated price and the stated payoff:

> *"It costs, I don't know, 50 or $100,000 a year to use the agents at full strength… but for a CEO or for a founder it actually makes a lot of sense to do that. And you have to give yourself permission to token max in that way… you can live in 2028 today."*

This is the corpus's most explicit statement that **the frontier is a spending decision rather than a capability date** — adjacent to [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Ryan Carson's]] $5k→$20k/month on Devin, but framed as buying forward in time rather than buying throughput.

## Business loops, and the maintenance problem nobody else names

The skillify loop, stated more mechanically than in the keynote:

> *"You do some feat of strength and then you turn it into a markdown file plus code plus tests that can be reused and like put into a cron job… a markdown file is an employee. And it's an employee that will do the job perfectly every single time."*

> *"Any business process that you need in your company, you just do it once perfectly. And the first time you try to do it, it's going to be bad. Expensive. Many iterations."*

Applied, per Tan, to *"sales, marketing, customer support — everything."* The claimed result: *"zero to 15 mil ARR in about four months with like two or three people and… a few hundred skill files."* **Unnamed company, unverified, second-hand.**

What makes this page worth more than the keynote is the **failure mode he volunteers when asked whether errors compound**:

> *"Once you get a lot of markdown files… that's where provenance matters, that's where conflict management [matters] — when you have two facts. If you have provenance then you're like, well this is the more recent one, this is the one that wins. You need a cron job that's sweeping through that and making sure that things are accurate and from the right places."*

That is a **knowledge-base maintenance problem**, and it is the same one [[2026-08-31-blum-how-i-ai-claude-cowork-pm-system|Blum]] solves by hand and this wiki solves with a schema. The corpus's [[llm-wiki]] page should carry it: the thing that breaks a markdown-run company is not agent capability but **stale, conflicting context with no provenance**.

## The bureaucracy thesis, and the Toyota inversion

Tan's structural claim is that the layer AI removes is the middle:

> *"It's almost like the mid level of bureaucracy should be agents."* (Acharya) — *"Yeah… the business becomes too big to fit in one person's head, and this is like the most profound form of — you have agents, you have memory, you have retrieval."*

[[2026-08-14-blomfield-yc-building-structuring-ai-native-company|Tom Blomfield]] describes the resulting company shape two days later; Tan's contribution is naming what the agents replace and why. The constraint being relieved is stated as a cognitive limit, repeatedly: *"human beings can only keep seven plus or minus two things in their head at any given time… you plus an agent can keep basically three Harry Potter books in your head."* And the whole built world, in his framing, *"is basically still built on a world that is predicated by… limited human beings."*

The Microsoft anecdote is the concrete version — two engineers walking to another building **with a baseball bat** to get a P3 bug fixed across seven levels of org chart — and it resolves into the line the channel put in the cold open: *"an org like Microsoft can't [work this way]. But a startup can. And every startup must."*

Against that, he reaches for the **Toyota Production System**: the line worker should be allowed to change the line *"because you are the person with the most amount of context."* An interesting tension the conversation notices but does not resolve — a hierarchical society produced a bottom-up method, and Tan wants AI to do to middle management what TPS did to it.

He pairs this with **Venkatesh Rao's "above the API line"** and inverts it: *"I actually think AI erases the API line."* The worked example is a YC-funded company shipping **a bug-report endpoint intended for agents, not humans**, which replies in real time with a triage verdict and a workaround. Agent-to-agent commerce as the successor to being above or below the API.

## Two predictions, and one anti-prediction

- **Harness wars, 2027.** *"My guess is like next year 2027 will be like the harness wars… but it's really a cost thing, it's just too expensive right now."* Gated on inference economics: *"the frontier model compute of today will be like maybe 50 or 100 bucks in like two or three years."* Acharya adds the shape of the curve — *"the price per token of frontier is going to infinity… and the price per token of the model that was frontier a week ago is collapsing to zero."*
- **SaaS.** *"A pure per-seat SaaS thing — not totally clear it will exist in another five or 10 years… it's perfectly fine as a wedge but… you better hope that that's a leap to some sort of moat around data or network effects."*
- **The anti-prediction, which is the most interesting thing he says.** Asked whether the constraints are intelligence-bound: *"It's all human… actually I'm realizing this might be a white pill."* All the bureaucracy and slowness that AI discourse treats as the problem is, he argues, what prevents the disruption people fear. *"It's going to be 20 years. And that's not a bad thing, that's actually a good thing… there are real moats to these things, there are structural reasons why a Microsoft isn't going anywhere."* And he flags it as heterodox: *"this is sort of a little antithetical to what most people in Silicon Valley would say."*

## Dynamic capabilities (Warner & Wäger)

- **`digital-sensing/digital-mindset-crafting`** — the entire interview is aimed at changing how founders think about ambition and tempo: don't LARP, don't chase what's hot, give yourself permission to token max, and expect twenty years rather than two.
- **`digital-seizing/rapid-prototyping`** — the prescription for building intuition is to *"use every model and build completely trivial things for no other reason [than] to have a chassis with which to learn the new technology"*, and his own GStack/GBrain tools are described as having started as messing around.
- **`digital-transforming/redesigning-internal-structures`** — the middle-management thesis is a structural claim with a proposed replacement (agents in the organising layer, executives setting direction, individuals executing) and a historical model (the Toyota Production System).
- **`strategic-renewal/business-model`** — the per-seat SaaS argument is a business-model claim: the pricing model that defined a decade of software is, in his reading, a wedge rather than a moat under AI.

## Linked entities and concepts

- Concepts: [[agentic-engineering]], [[agent-harness]], [[llm-wiki]], [[enterprise-ai-adoption]], [[agent-fleet-management]], [[open-source-ai]], [[ai-employment-effects]], [[strategy]]
- Entities: [[Garry Tan]], [[Y Combinator]], [[a16z]], [[Claude Code]], [[Boris Cherny]], [[Peter Steinberger]], [[Microsoft]]
- **Dangling** (single-source mention, deferred): Anish Acharya, Palantir, Pedro Franceschi (Brex), Brex, Crabtrap, OpenClaw, ClawVisor, Hermes agent, GBrain, GStack, garryslist.org, Venkatesh Rao, Chris Dixon, Joe Lonsdale, Stephen Cohen, Peter Thiel, Derek Sivers, Daniel Lurie, Mario Savio

## Scope and reliability

**A venture-capital podcast interview with the head of a venture accelerator.** Both parties are talking their book: a16z and YC both profit if founders believe the window is open and the tooling is transformative. The disclosure is structural rather than stated.

**Zero measurements of any kind.** The one quantitative claim — zero to $15M ARR in four months with two or three people — is unnamed, unsourced and second-hand. *"400 of that person"* is rhetoric, not a multiplier. The $50–100k token-max figure is his own spend, unverified. Nothing in the 51 minutes is independently checkable.

**Transcript quality is the lowest of any source in this ingest.** ASR-only (no human captions), and the raw file documents ~40 proper-noun corrections plus **three uncertain spellings** (OpenClaw, ClawVisor, Crabtrap) and a **~14-second gap at 29:44–29:58** in the middle of the Franceschi example. Do not quote across that boundary, and check those three names before citing them.

**Cite this for:** the token-maxing frame, the provenance/conflict failure mode, the harness-wars-2027 call, the middle-management thesis, and the slower-than-you-think anti-prediction. **Do not cite for:** any number, or for whether agentic companies actually work.

## Debates and supersession

- **Tempo, against [[2026-07-31-collison-yc-startup-school-is-ai-breaking-the-lean-startup-playbook|Collison]].** Two YC-platformed voices within a fortnight, pointing founders at opposite horizons — incumbents are dead men walking versus *"a Microsoft isn't going anywhere… it's going to be 20 years."* Reconcilable, but only if you read incumbent inertia as the thing that creates the startup window, which neither says explicitly.
- **"A markdown file is an employee" is a claim the corpus cannot currently evaluate.** It is asserted here and in the Startup School keynote by the same person, and the strongest adjacent evidence — [[2026-08-31-blum-how-i-ai-claude-cowork-pm-system|Blum's]] n=1 system, [[2026-09-07-yc-paper-club-why-the-harness-matters-more-than-the-model|YC's own QM]], whose code review was *rubber-stamped* — shows skill files working under close human maintenance, not autonomously. The provenance problem Tan names is the reason to be sceptical of his own slogan.
- **Self-consistency worth flagging:** Tan argues simultaneously that a founder can be *"400 of that person"* and that societal change will take twenty years. Both may be true (individual capability versus institutional absorption), but the interview does not reconcile them, and the two halves get quoted separately by people who want different things.
