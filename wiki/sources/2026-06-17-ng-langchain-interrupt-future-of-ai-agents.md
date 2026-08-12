---
type: source
kind: video
title: "The Future of AI Agents with Andrew Ng (LangChain Interrupt '26)"
author: ["LangChain"]
url: "https://www.youtube.com/watch?v=OaRhpwz_TGM"
date_published: 2026-06-17
date_ingested: 2026-06-20
zotero_item_key: JUUQZGWX
zotero_collection: ai-wiki
length: "~31:39 minutes (transcript ~1035 lines; manual English captions, kind: manual — human-curated; the fetch returned the transcript doubled and the duplicate tail was disregarded at ingest)"
raw: "../../raw/videos/the-future-of-ai-agents-with-andrew-ng-interrupt-26.md"
tags: [andrew-ng, harrison-chase, langchain, interrupt-26, coding-agents, product-management-bottleneck, everything-becomes-a-bottleneck, generalist-teams, high-context-generalists, building-blocks, lego-bricks, context-hub, deeplearning-ai, enterprise-ai-adoption, bottom-up-vs-top-down, thousand-flowers, loan-underwriting, cost-savings-vs-growth, swing-for-the-fences, forward-deployed-engineers, vendor-lock-in, optionality, langsmith, open-weight-models, data-architecture, unstructured-data, rearchitecture, nosql, mongodb, ai-fund, ai-aspire]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-seizing/strategic-agility
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - strategic-renewal/business-model
  - contextual/external-triggers
  - contextual/internal-enablers
roles: [ceo, cso, cdo, cto, transformation-lead]
relationships:
  - type: supports
    target: 2026-06-16-anthropic-economic-index-agentic-coding-returns-to-expertise
    via: "Ng's *product-management bottleneck* and *high-context generalists* are the practitioner-side picture of the AEI's measured division of labour — humans decide *what* (planning, scoping, judgement), agents do *how* (execution). Both conclude the scarce, value-bearing input is domain judgement and the ability to decide what to build, not implementation throughput."
    confidence: 0.8
  - type: supports
    target: 2026-06-18-dumra-mit-smr-dbs-everyone-an-innovator
    via: "Ng's central enterprise claim — *bottom-up 'thousand flowers' innovation generates point solutions and incremental efficiency, but the transformation needs a top-down motion to redesign the whole workflow* (the 10-minute-loan example) — is the diagnosis that DBS's playbook model operationalises: top-down transformation KPI (20% of scorecard) meeting bottom-up delivery (journeys, agents). Two enterprise-transformation sources naming the same bottom-up/top-down complementarity."
    confidence: 0.75
  - type: supports
    target: 2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler
    via: "Both argue AI value comes from *redesigning work at scale*, not deploying tools task-by-task. Ng's small teams of *high-context, empowered generalists given wide guardrails* who cross functional boundaries is a concrete org pattern for Beutler's *architecting AI-native organizations* thesis. Shared cell: redesigning-internal-structures."
    confidence: 0.7
  - type: supports
    target: 2026-05-21-allen-aws-london-exec-forum-agentic-team-structures
    via: "Both address how teams restructure around agents. Allen (AWS) traces the builders-to-orchestrators role-shift and end-to-end W&W operationalisation from the vendor chair; Ng supplies the practitioner version — generalist multi-role teams of 1–10, the product-management-bottleneck-becomes-everything-bottleneck dynamic. Shared cells: redesigning-internal-structures, strategic-agility."
    confidence: 0.65
  - type: supports
    target: 2026-06-11-kilpatrick-sequoia-model-eats-the-harness
    via: "Optionality and vendor-neutrality from two angles. Ng's practitioner discipline — *never sign longer than a one-year contract regardless of discount, because I don't know which model/coding-agent will lead in a year* + open-weight support + a vendor-neutral observability layer (LangSmith) — is the buyer-side counterpart to Kilpatrick's supply-side claim that model capability erodes harness/provider lock-in over time. Both treat the leading model as a fast-moving target that punishes lock-in."
    confidence: 0.65
---

# The Future of AI Agents with Andrew Ng (LangChain Interrupt '26)

> Andrew Ng sat down with Harrison Chase for a wide-ranging fireside chat at Interrupt, the agent conference by LangChain. Watch the full session and get insights on: how fast coding agents have evolved and how the way small teams ship is being reshaped; the "product management bottleneck" and why accelerating software development just moves the constraint somewhere else; how enterprises are getting incremental AI wins but missing the bigger transformation; the data architecture rework most companies haven't started yet … and so much more.
>
> *— [LangChain YouTube channel](https://www.youtube.com/watch?v=OaRhpwz_TGM) (Interrupt '26 fireside, hosted by Harrison Chase)*

A **~32-minute fireside chat** at **Interrupt '26**, [[LangChain]]'s agent conference, between **[[Andrew Ng]]** (founder of [[DeepLearningAI|DeepLearning.AI]], AI Fund, AI Aspire; co-founder of Coursera) and host **[[Harrison Chase]]** (CEO of [[LangChain]]). Ng's second year on the Interrupt stage. The conversation spans coding agents, the future of software-engineering teams, enterprise AI adoption, vendor optionality, open-weight models, and the unstructured-data rearchitecture — most of it from the operator chair of someone running multiple AI companies and advising Fortune-50/G2000 businesses through AI Aspire.

## TL;DR

**1. Coding agents moved fastest; the rest of the hype/doom over-shot.** Ng: the *hype* and the *doom* (the "job apocalypse," which "I don't think is going to be a thing") both got more traction than he expected; on the positive side, **coding agents took off faster than he'd have guessed**. The "everything changes every three months" cliché is mostly false — *except* for coding agents, where it feels true. His own mix shifted from "almost all [[agentic-engineering|Claude Code]]" six months ago to a rotation of Claude Code + OpenAI Codex + Gemini CLI + open-source coding agents, "changing rapidly," including coding from his phone against a Mac Mini in his office.

**2. The product-management bottleneck became an *everything* bottleneck.** A year ago Ng wrote about the **product-management bottleneck**: when building gets fast, *deciding what to build* (scoping, customer feedback, prioritisation) becomes the constraint. Over the last year it got "much worse, in a good way" — and when software gets 10–100× faster, "pretty much everything else becomes a bottleneck": a **marketing bottleneck** (marketers can't keep up describing all the new features), a **legal-compliance bottleneck** (a week for legal sign-off is fine on a 3-month build, painful on a 1-day build), a design bottleneck, and so on.

**3. Small teams of high-context, empowered generalists.** Ng increasingly sets up teams of **1–10 people**, "high-context, highly empowered generalists" given **wide guardrails** to run inside — writing and shipping code *and* drifting into marketing copy, terms-of-service first drafts, design, etc. The **pigeonhole argument**: if a team of two humans must cover five functions, each human must play more than one role — and AI makes them "slightly less bad" at the roles they're weak in. Most people who do this well come from a **deep engineering background**, but he's seen product managers, marketers, and operations people learn to build effectively too.

**4. Building blocks / LEGO bricks + keeping agents current (Context Hub).** Ng's mental model for the future of software engineering: a proliferation of **building blocks** (AI ones — RAG, agent frameworks, evals, guardrails — and non-AI ones — UI components, auth, databases). Developers who master enough blocks combine them **combinatorially** ("exponentially as a function of the number of LEGO bricks"). The friction: coding agents don't know the *newest* blocks (a model's knowledge cutoff predates e.g. nano-banana's API). His fix is **Context Hub** (Rohit Prasad's — "a Stack Overflow for AI agents" serving the latest docs/SDKs to agents; note: name-collides with, and is distinct from, LangChain's own Context Hub), which loads current docs so the agent makes the API calls he'd rather not memorise.

**5. Education is changing — what to learn *and* how.** *What* developers must learn has shifted (coding agents, building blocks, a bit of product management). On *how*, Ng thinks the transformation of education has been over-hyped and "isn't quite here yet," but is iterating: DeepLearning.AI launched **CodeDream.ai / LearnDream.ai**, where instead of watching a course you have a *conversation* — a simulated one-on-one video call with an AI Ng you can interrupt, with interactive **JavaScript-instead-of-video** demos you can type your own prompts into. Newer courses (e.g. a just-launched Transformers course) lean on interactive visualisations over passive video.

**6. Enterprise adoption: bottom-up isn't paying off; the transformation needs top-down.** Via **AI Aspire** (his advisory firm with Chris Tann, advising Fortune-50/500/G2000), a consistent theme: everyone invested in **bottom-up "thousand flowers" innovation**, and "for the most part it is not paying off" — boards are asking *where's the ROI?* Keep doing bottom-up (it generates ideas and real incremental efficiency), **but** it yields *point solutions* and incremental gains, not transformation. The **loan-underwriting example**: automating the one-hour human loan-approval step is a small efficiency gain; *rethinking the whole workflow* into a **"get approved in 10 minutes" product** is the transformation — and that takes **someone with broad scope to redesign marketing, routing, diligence, and execution end-to-end**, i.e. a **top-down motion** complementing the bottom-up one.

**7. Cost savings vs. growth; swing-for-the-fences vs. incremental.** Cost savings are fine but capped; **growth has almost no ceiling**, so Ng pushes for growth ideas (the 10-minute loan, automated/augmented contact centres and drive-through ordering → more delightful service → growth). On ROI: "I wish I knew" — measuring ROI is as hard as measuring business. A counterintuitive lesson: **driving incremental gains can be harder than transformative gains** (you can't get people to "work 50% harder," so a 20–50% target forces creative solutions). Businesses send AI Aspire spreadsheets of 300+ ideas; narrowing to a **small portfolio of thoughtful bets** with meaningful resources takes hard technical *and* business analysis, and tends to need a **top-down** resource-allocation motion (the cost of prototyping has plummeted, but you still can't fund everything).

**8. Forward-deployed engineers: a good thing, slightly over-hyped.** FDEs are having a Silicon Valley moment; Ng likes them but expects most firms to have *many* in-house engineers and a *smaller* embedded FDE team. Building agent workflows is genuinely hard — it needs business understanding, customer-facing skill, observability/evals, change management — "deep technical judgment."

**9. Optionality and vendor lock-in.** Because "the leading AI model rapidly changes" and he has "no idea what would be the leading coding agent a year from now," **optionality is very valuable**. Ng's personal practice: **almost never sign longer than a one-year contract regardless of the 20–30% discounts vendors offer** for three-year deals. He values **vendor-neutral tools** (names **LangSmith**) for observability and preserving optionality, and supports **open-weight models** (his teams use them, sometimes fine-tuned; they sit ~6–9 months behind the frontier but are cheap enough to matter) — voicing concern about White-House noises on inspecting models before release as "a war on open source/open weight."

**10. Data strategy before agents — the coming unstructured-data rearchitecture.** A very common enterprise pain point: **rethinking the data architecture**. The last 10–20 years organised *structured* data (tables, relational); now AI can process **unstructured** data (text, images, PDFs, audio, video), and getting it to agents "at the right time, in the right place" is suddenly much more valuable. Ng has found *no* good off-the-shelf solution and is running internal experiments to rearchitect his own unstructured data. He predicts **"tens to hundreds of millions of dollars" of data-rearchitecture projects** across many businesses over the next few years — the blockers being **fragmentation, governance, no consensus schema, data on laptops, and permissions designed for humans not agents** (does an agent inherit my permissions?). A coding aside: he prefers **NoSQL (MongoDB)** for rapid prototyping because redesigning a relational schema mid-iteration is "so annoying," moving to relational/scalable stores only at large production scale.

## How this source touches the wiki (dynamic capabilities)

- **`digital-sensing/digital-scouting`** — Ng's continuous scan of the coding-agent frontier (the shifting Claude Code / Codex / Gemini CLI mix), the vendor landscape, and what's working vs. not across the G2000 via AI Aspire.
- **`digital-seizing/strategic-agility`** — the **optionality** discipline (≤1-year contracts, vendor-neutral observability, open-weight hedging) and the **top-down resource reallocation** behind a thoughtful portfolio of bets.
- **`digital-seizing/balancing-digital-portfolios`** — narrowing 300+ candidate ideas to a **small portfolio of high-conviction bets**; *swing-for-the-fences* vs *incremental* allocation; cheap prototyping but finite funding.
- **`digital-transforming/redesigning-internal-structures`** — **small teams of high-context generalists** with wide guardrails; the **10-minute-loan** end-to-end workflow redesign as the unit of transformation.
- **`digital-transforming/improving-digital-maturity`** — DeepLearning.AI's reskilling toward building-blocks mastery and product sense; the CodeDream/LearnDream interactive-learning push to raise workforce digital maturity.
- **`strategic-renewal/business-model`** — **drive growth, not just cost savings** (10-minute-loan product, contact-centre-as-growth) and the **unstructured-data rearchitecture** as the enabler of agent-era value creation.
- **`contextual/external-triggers`** — the coding-agent adoption wave that "took off faster than I would have guessed" as the external trigger reshaping software work.
- **`contextual/internal-enablers`** — getting the **data strategy** right before building agents; embedded **forward-deployed engineers**; executive scope to drive top-down redesign.

**Roles override** (`roles:` explicit): `ceo, cso, cdo, cto, transformation-lead`. The source's centre of gravity is *enterprise AI strategy + how to organise (engineering) teams + where the transformation ROI actually is* — the C-suite-strategy and transformation-ownership roles, plus the CTO for the software-engineering-org claims. The override drops the broad finance/HR/marketing cluster the eight cells would otherwise inherit.

## Linked entities and concepts

- Concepts this source informs: [[enterprise-ai-adoption]] (bottom-up vs top-down; the loan example; ROI; data rearchitecture), [[agentic-engineering]] (coding-agent rotation; building blocks), [[automation-vs-augmentation]] (the product-management/everything bottleneck; generalist multi-role teams), [[durable-skills]] (domain judgement + scoping as the scarce input), [[warner-wager-process-model]] / [[dynamic-capabilities]] (the enterprise-transformation reading).
- Entities (already in wiki): [[Andrew Ng]], [[Harrison Chase]], [[LangChain]], [[DeepLearningAI]].
- **Dangling** (single-source mentions, deferred per the second-source promotion rule): **Chris Tann** (AI Aspire co-founder; first appearance), **Rohit Prasad** (Context Hub; first appearance), **AI Aspire** / **AI Fund** (Ng's firms; concept-mentions), **Context Hub** / **CodeDream.ai** / **LearnDream.ai** / **LangSmith** (products named once — promote on a second source).

## Source-to-source relationships

- **Supports** [[2026-06-16-anthropic-economic-index-agentic-coding-returns-to-expertise]] — practitioner picture of the AEI's planning/execution division of labour; both elevate domain judgement and *deciding what to build* over implementation throughput.
- **Supports** [[2026-06-18-dumra-mit-smr-dbs-everyone-an-innovator]] — same bottom-up/top-down complementarity; Ng diagnoses it, DBS operationalises it.
- **Supports** [[2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler]] — redesign work at scale; small empowered generalist teams as the concrete org pattern.
- **Supports** [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures]] — team restructuring around agents (practitioner vs vendor angle).
- **Supports** [[2026-06-11-kilpatrick-sequoia-model-eats-the-harness]] — optionality/vendor-neutrality (buyer-side discipline vs supply-side lock-in erosion).

## Source-quality note

Transcript fetched via the [youtube-transcript-skill](../../.claude/skills/youtube-transcript-skill/SKILL.md) (Playwright/DOM route); the video carries **human-curated (manual) English captions** (`kind: manual`) alongside an ASR track, so transcript fidelity is high. The fetch returned the transcript **doubled** (the body repeats from ~0:00 a second time); the duplicate tail was disregarded at ingest. Transcript provenance does not feed confidence per [§Lifecycle].
