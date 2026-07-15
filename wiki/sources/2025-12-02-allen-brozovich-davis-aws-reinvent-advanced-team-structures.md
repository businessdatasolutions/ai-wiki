---
type: source
kind: video
title: "AWS re:Invent 2025 — A leader's guide to advanced team structures in an agentic world (SNR307)"
author: ["AWS Events"]
publisher: "Amazon Web Services (AWS Events YouTube channel); AWS re:Invent 2025, Las Vegas"
url: "https://www.youtube.com/watch?v=j5TOWVNJx50"
date_published: 2025-12-02
date_ingested: 2026-07-14
length: "~57:32 minutes (transcript ~538 ASR lines; auto-generated transcript, ASR-cleaned at ingest)"
raw: "../../raw/videos/aws-reinvent-2025-a-leaders-guide-to-advanced-team-structures-in-an-agentic-world-snr307.md"
tags: [aws-reinvent-2025, aws-events, jonathan-allen, stephen-brozovich, richard-davis, danske-bank, agentic-team-structures, day-after-tomorrow, four-mental-model-shifts, business-lifecycle-phases, asymmetric-resource-allocation, pdlc, cloud-buddy, checkmate, expert-generalists, builders-to-orchestrators, mit-nanda, p-engineers, change-vs-run, conference-talk]
dynamic_capabilities:
  - digital-sensing/digital-scenario-planning
  - digital-seizing/rapid-prototyping
  - digital-seizing/strategic-agility
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - strategic-renewal/organizational-culture
  - strategic-renewal/business-model
  - contextual/external-triggers
  - contextual/internal-enablers
relationships:
  - type: supports
    target: 2026-05-21-allen-aws-london-exec-forum-agentic-team-structures
    via: "**The earlier draft of the same Jonathan Allen keynote.** The London Executive Forum source page already records Allen's own disclosure that the London deck was 'a continuation of a deck he first presented at AWS re:Invent in Las Vegas in December 2025, with 400 hours of revision between then and now.' This source is that original re:Invent deck (2 Dec 2025), captured before the USE/COMPOSE/BUILD framework, the hourglass-organization term, the moats-erosion thesis, and Project Mantle entered Allen's material — those are all London-edition (May 2026) additions. What survives unchanged across both editions: the peanut-butter-and-jam cloud/agile framing, the Scott Galloway 'AI won't take your job, someone using AI will' quote, the MIT NANDA 95%-zero-return citation, the Anthropic Claude-conversation economic-tasks report, builders-to-orchestrators, Martin Fowler's expert-generalist framing, and the data-engineers-become-critical thesis. The re:Invent edition's second half (Stephen Brozovich's org-scientist frameworks + Richard Davis/Danske Bank's customer case) does not recur in the London edition at all — replaced there by Nick Francis/Brooklyn Solutions."
    confidence: 0.85
  - type: supports
    target: 2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world
    via: "Third sibling in the same AWS Enterprise Strategy 'advanced team structures' talk franchise (re:Invent Dec 2025 → London May 2026 → Sydney Jun 2026), sharing the Scott Galloway framing quote, the builders-to-orchestrators mental-model shift, the Martin Fowler expert-generalist / Werner Vogels renaissance-developer talent thesis, and the MIT NANDA 95%-pilots-fail citation across all three editions."
    confidence: 0.75
  - type: supports
    target: 2026-06-18-dumra-mit-smr-dbs-everyone-an-innovator
    via: "Two bank-sector digital-transformation case studies told at CTO/operator altitude with concrete production-agent evidence: Richard Davis names Danske Bank's 10 Big Wins, the PDLC friction-removal initiative, Cloud Buddy (reliability-agent, ~75% triage-time cut), and CheckMate (hackathon-to-production agent); Bidyut Dumra names DBS's Managing Through Journeys, innovation pyramid, and mini-CEO/agent-building culture. Both banks report an accelerating-versus-most-competitors self-framing (Davis: 'catching up to winning'; Dumra: 'best bank in the world') and both pair a cloud-migration or platform foundation with the AI-adoption story."
    confidence: 0.65
  - type: supports
    target: 2026-07-09-nyc-executive-forum-2026-a-leaders-guide-to-agentic-ai
    via: "Reciprocal edge: Ishit Vachhrajani, credited above (dangling list) as the source of the four-mental-model-shifts framework Brozovich restates, is the sole speaker of the AWS NYC Executive Forum talk — delivering that exact framework first-hand and in full, reorganized as an organization/trust/culture keynote. Genuinely different talk (title, event, speaker-of-record, governing structure) from this source's 'advanced team structures' franchise, not a re-delivery."
    confidence: 0.75
confidence: 0.75
last_confirmed: "2026-07-15"
accessed_at: "2026-07-15"
source_count: 1
---

# AWS re:Invent 2025 — A leader's guide to advanced team structures in an agentic world (SNR307)

> As AI agents transform the workplace, organizations must adapt their structures and methodologies to harness new opportunities. The probabilistic nature of AI requires continuous iteration and intelligent oversight, creating new ways of working across business functions. To thrive, organizations must combine clear capability assessment with agile planning while leveraging their unique domain expertise and data assets. This keynote explores how leadership is evolving to meet these needs, covering new organizational models and roles that coordinate human-AI hybrid teams. Leaders will learn strategies for balancing rapid decision-making with strategic oversight, finding the optimal mix of centralized guidance and decentralized innovation.
>
> (Channel description, AWS Events.)

A 57:32 senior-leaders-track session (code **SNR307**) filmed at **AWS re:Invent 2025** in Las Vegas, published to the AWS Events YouTube channel on 2 December 2025. Three speakers in series:

- **Jonathan Allen**, [[Amazon Web Services|AWS]] Executive in Residence (~0:00–27:43), delivering the headline keynote — eight-plus years at AWS, previously divisional CTO at Capital One during its cloud migration. *Auto-generated transcript, ASR-cleaned at ingest.*
- **Stephen Brozovich** (~27:47–47:50), Amazon employee since August 1999, presenting Amazon's internal organizational-science research on operating models and human/AI resource allocation.
- **Richard Davis**, CTO of **Danske Bank** (~47:57–57:00), giving a customer case study.

This is the **origin edition** of the talk the wiki already holds in two later, revised forms: [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|London Executive Forum, 21 May 2026]] (Allen discloses in that recording that the deck began here, with "400 hours of revision" since) and [[2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world|AWS Summit Sydney, 12 June 2026]] (delivered by Stephen Brozovich under the ASR spelling "Steven Brovich" — see [[Steven Brovich]]'s entity page for the alias note). See this page's `relationships:` block for what carried forward unchanged and what is genuinely new here.

**Authors / dangling list.** Per [author-entity promotion](../../CLAUDE.md#author-entity-promotion) (second-source rule): **Jonathan Allen** and **Steven Brovich** (as "Stephen Brozovich") are each cited a second time by this ingest — Allen via the London source, Brozovich via the Sydney source — and are promoted to entity pages on this ingest. New dangling entries (first mention, deferred): **Richard Davis** (CTO, Danske Bank), **Danske Bank** (organization), **Anthony Liguori**-adjacent AWS internals are not named in this edition (Project Mantle does not appear here — a London-edition addition), **Peter Hinssen** (author, *The Day After Tomorrow* — cited by Brozovich), **Scott Galloway** (quote source, also cited in the later editions). **Ishit Vachhrajani** — named here as the source of the four-mental-model-shifts framework Brozovich restates — is **promoted to an entity page on the 2026-07-15 ingest** of [[2026-07-09-nyc-executive-forum-2026-a-leaders-guide-to-agentic-ai|his own AWS NYC Executive Forum talk]], where he delivers that framework first-hand.

## TL;DR

Four substantive contributions warrant ingest, split between what survives into the later editions (context only) and what is genuinely new to the wiki:

1. **Confirmation this is the origin talk.** Allen's core arc — peanut-butter/agile-jam framing, determinism-vs-non-determinism as the leadership mental-model challenge, the Scott Galloway "AI won't take your job, someone using AI will" quote, the MIT NANDA 95%-zero-return citation, the Anthropic Claude-conversation economic-tasks breakdown, "change versus run doesn't work in an agentic world," builders-to-orchestrators, Kiro/spec-driven development, data-engineers-become-context-architects, and Martin Fowler's expert-generalist framing — all appear here in materially the same form later recorded on the [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|London]] page. This source does **not** duplicate that page's cross-cutting updates; it only adds delta content below.

2. **Stephen Brozovich's organizational-science frameworks (~27:47–47:50) — the wiki's first sighting of all four.** None of these recur in the London or Sydney editions:
   - **The "Day After Tomorrow" work-time framework** (crediting Peter Hinssen's book of the same name): leaders juggle *the work of today* (current value), *the work of tomorrow* (future value), and *the work of the day after tomorrow* (long-term value) — plus the unaccounted-for *"stuff of yesterday"* (tech debt). Today systematically crowds out tomorrow and the day after tomorrow.
   - **Four mental-model shifts** (crediting a same-conference session by Ishit Vachhrajani): operational-execution culture → research-lab/continuous-learning culture; govern-through-gates → strategic-direction-plus-guardrails-plus-feedback-loops; factory-floor management → trading-floor management (autonomy + real-time risk visibility + adaptive circuit breakers); functional silos → immune-system responsiveness (swarming around customer needs, not hierarchy).
   - **The business-lifecycle-phase organizational model** (Amazon's internal "team of organizational scientists," advising across 1,500+ organizations annually): five phases from early-adopter *depth* (small dedicated teams, direct customer access) through hybrid dedicated-plus-shared structures, to mainstream-customer *breadth* (horizontal platform teams + federated product teams), to late-majority optimization-and-efficiency (where "most organizations stop" and become vulnerable to disruption), to a fifth phase requiring **deliberate reinjection of innovation** via dual operating models — Amazon's own examples span from NFL-on-Prime (phase-1-like) to home delivery (mature, still needing phase-5 reinvention). Headline claim: *"organizations that align their operating model with their business lifecycle phase outperform those that do not."* Three cross-cutting tensions organizations must resolve at each phase, none reducible to a centralize-vs-decentralize binary: **speed** (consistency vs. agility), **resourcing** (shared/centralized scale vs. dedicated teams), **connections** (interdependent coordination vs. autonomous modularity).
   - **Asymmetric human/AI resource allocation across four work types**, with observed Amazon allocation percentages: *strategic differentiated work* (executive-critical, ~25% AI workload, near-zero automation/outsourcing — "we would never want to outsource our differentiator"); *strategic enabling work* (leadership shifts to auditing/advising, AI takes a greater share via insight generation/anomaly detection, TPMs and solution architects lead technical implementation, automation begins); *business essential work* (agentic systems handle routine analysis/reporting, humans move to operations/account-management/BI-oversight roles); *business compliant work* (skews heavily to deterministic automation, human contribution is dedicated regulatory-context expertise for human-in-the-loop decisions). Headline claim: *"organizations that asymmetrically allocate human AI resources based on the type of work outperform those that do not."*

3. **Richard Davis / Danske Bank customer case (~47:57–57:00) — the wiki's first Danske Bank-as-primary-subject source** (Danske Bank appears elsewhere only incidentally, as a Brooklyn Solutions client, on the London-edition source page). A 150-year-old Copenhagen bank, self-positioned in the "winning" 5% of [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|MIT NANDA's]] 95%-zero-return finding, having migrated 850 applications to AWS over 18 months as the foundation for its "AI-first bank" ambition. **10 Big Wins** (formerly "Big Bets"): one is a new **product development lifecycle (PDLC)**, triggered when live-engineering-tooling analysis found developers spending only **35% of their time on coding** despite AI coding assistants cutting change lead time by ~50% — the bottleneck was everywhere else in the delivery process (Kanban boards, handover meetings, documentation, testing). Agents already in production: a **business-analysis agent** (spec automation), a **QA agent** (test-case generation), and **Cloud Buddy**, a reliability-engineering agent that cuts triage time by ~75% and improves root-cause accuracy (log analysis only — does not yet take autonomous action). A GenAI-hackathon program with a **guaranteed production path for winners** produced **CheckMate**, now in daily production use by the team that built it. A change-management taxonomy of employee reactions to GenAI rollout, decoded via corporate-jargon euphemisms ("I'll circle back to you" = *why replace me?*; "let's take it offline" = *where do I even start?*), counters "why should I use something that can replace me?" with the same Scott-Galloway-derived reframe Allen opens with: *"GenAI won't necessarily replace your role, but people using GenAI potentially will."*

4. **Confirms and slightly reframes Allen's earlier team-composition thinking**, ahead of the later editions' pod/platform-team vocabulary: an emerging **"agentic software engineer"** title; explicit skepticism toward collapsing a delivery team down to "a product manager, one or two SDEs, and business analysis is now an agent" ("not quite so fast" — production support and 24/7 on-call still require a full team); Amazon's internal **P-level engineer** (principal software engineer) role as the technical-goals owner per team, contrasted with the more familiar architect-led model most customers still run; a **"two in the box" model** pairing a technical delivery team with a sister business-process-expert team (architect, legal representative, financial analyst, data owner) for established, complex-process transformations.

## What was actually ingested

Full transcript (~57:32 of dialogue, ~538 ASR-cleaned lines/segments). The talk has no chapter markers; speaker switches at ~27:43 (Allen → Brozovich) and ~47:50 (Brozovich → Davis). Allen references dense, slide-driven content not extracted here (e.g. the full five-question framework he poses at ~10:26 is only partially enumerated in the ASR transcript — the first question, "what tooling do I need for the teams," is the one he develops at length via Kiro and AgentCore).

## Allen — the keynote (0:00–27:43)

Substantially the same material later recorded in detail on the [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|London Executive Forum page]]; summarized here rather than re-transcribed, with emphasis on what is *absent* relative to the later editions.

- **Framing.** Cloud-is-peanut-butter/agile-is-jam; the leadership mental-model challenge of shifting from determinism (industrial-revolution-era optimization) to treating non-determinism as *"a feature, not a bug"* in agentic systems, akin to managing high-agency people — moving "from gates to guardrails." The river-bursting-its-banks metaphor for agentic memory/context. An (unattributed-by-name-here, but recognizably Rory Sutherland-style) quote on business being fundamentally probabilistic despite spreadsheets pretending otherwise. Scott Galloway: *"AI won't take your job, somebody using AI will."*
- **Evidence base.** MIT NANDA's headline 95%-of-organizations-getting-zero-return finding (despite $30–40B enterprise GenAI investment); an Anthropic report on "which economic tasks are performed with AI, evidence from millions of Claude conversations" (computer/mathematical tasks dominate; office/administration, education, life/social science, and business/financial follow); a US-jobs-market disruption-representation breakdown.
- **Change-vs-run breakdown.** *"Change versus run models don't make sense in a cloud world... Agentic destroys the old model."* Customers are organizing around business outcomes rather than functional silos; execution-path size for agentic systems is doubling roughly every seven months.
- **Tooling.** Kiro's spec-driven development as the discipline that keeps agentic build output aligned to reliability/DR/determinism requirements customers still need; **Amazon Bedrock AgentCore** as the production/observability layer. *"Production systems don't run on laptops."*
- **Builders → orchestrators.** The mental-model shift Allen frames as personally difficult (30 years in IT, started coding on a Commodore 64 at age nine). Traditional on-call ("human gets paged, human investigates, human fixes") is shifting toward "AI agent gets alerted, AI investigates, proposes an RCA" with a human still closing the loop — Allen has "not yet witnessed customers passing over" full autonomy here. AI-assisted log analysis is producing "dramatic" mean-time-to-problem-finding improvements (unquantified in this edition, unlike London's SecOps 6h→7min figure).
- **Team composition.** No "massive strict formula" — teams are built to the business outcome, typically FinOps/SDE/security/data/cloud-DevOps/UX roles plus product management and a business analyst, with security often matrix-resourced across multiple teams. Explicit pushback on the tempting-but-premature idea that a "product strategist + one or two SDEs + business-analysis-is-now-an-agent" team is sufficient — production support and 24/7 on-call require more. Amazon's internal **P-level engineer** (principal engineer, one per team, owns technical goals) contrasted with the architect-led model ("we don't have architects inside Amazon — we have solution architects" for AWS customers). A **"two in the box" model**: a technical delivery team paired with a sister team of business-process experts, an architect, a legal representative, a financial analyst, and a data owner for complex, established-process transformations.
- **Data.** Data's organizational importance is "increasing exponentially," not diminishing, in an agentic world; most customers still lack a unified data catalog; an IDC North American IT-leaders report finds 55% difficulty filling data-engineer roles. The Nvidia "small language models are the future of agentic AI" paper is cited approvingly, with a customer example of a 20,000-parameter model trained in SageMaker AI and run economically on CPU rather than GPU. Data mesh principles (crediting the Thoughtworks-originated approach) and Amazon's zero-ETL investment both get a mention. Data analysts "haven't gone away" — context engineering is rising in importance instead.
- **Talent.** Martin Fowler's *expert generalist* framing (quoted at length, unattributed to the specific 2025 article in this transcript) as the emerging talent profile; context engineering and prompt engineering named as new roles. A cross-functional-skills Venn diagram (software engineer / data engineer / data scientist / data analyst) is used to illustrate the T-shaped-skills trend. Allen references a companion same-conference talk ("Johnny['s] leader's guide to agentic AI") not otherwise identified or ingested in the wiki.

**What is absent here relative to the London/Sydney editions** (useful for dating any future Allen-franchise source that surfaces): the USE/COMPOSE/BUILD economic-decision framework, the term "hourglass organization," the moats-erosion thesis, Project Mantle, the junior-hiring-crisis statistics, and the Singapore AI-governance citation. These are all London-edition (May 2026) additions per that page's own account of "400 hours of revision."

## Brozovich — Amazon's internal organizational science (27:47–47:50)

See TL;DR item 2 for the four frameworks in full. Two additional details worth preserving: Brozovich frames the whole segment around a leadership resource-constraint problem (limited time/attention/budget/talent, crediting Peter Hinssen's *The Day After Tomorrow*), and closes the phase-model discussion with Amazon's own "it's always day one" ethos as the discipline that keeps a mature business (home delivery) exercising phase-1-like reinvention rather than settling permanently into phase-4 optimization.

## Davis — Danske Bank customer case (47:57–57:00)

See TL;DR item 3. Additional detail: Danske Bank's overall AI program is CEO-mandated; a "champions" train-the-trainer program addresses the "let's take it offline" (uncertain-where-to-start) reaction; the youngest and most enthusiastic staff cohort's reaction is read as "it's about time we implemented some great processes here." Davis frames his own CTO role as evolving toward "expert generalist" / "connector of experts across both technology and the wide employee base" — the same talent-profile vocabulary Allen uses for individual contributors, now applied reflexively to the CTO role itself. Closing lesson: over-planning delayed Danske's GenAI rollout; committing to a guaranteed production path for hackathon winners (three of three finalists reached production) restored momentum — *"momentum being a profession."*

## Substantive contributions to the wiki

**To [[enterprise-ai-adoption]]:** the Day-After-Tomorrow work-time framework; the four mental-model shifts (deterministic/gates/factory-floor/silos → probabilistic/guardrails/trading-floor/immune-system); the five-phase business-lifecycle organizational-alignment model; the four-work-type asymmetric human/AI resource-allocation framework; Danske Bank's 10-Big-Wins / PDLC / hackathon-to-production program.

**To [[micro-productivity-trap]]:** Danske Bank's 35%-of-time-on-coding finding — a clean instance of the trap's core pattern (a task-level productivity gain — 50% shorter change lead time from AI coding assistants — does not translate into proportional delivery-process gains, because the bottleneck sits in the surrounding handoffs, documentation, and testing, not in coding itself).

**To [[dynamic-capabilities]]:** an earlier-draft data point in the AWS "leader's guide" franchise already anchored there via the London edition; Brozovich's speed/resourcing/connections tensions are a `digital-seizing/strategic-agility` instance, and the business-lifecycle-phase model is a `digital-transforming/redesigning-internal-structures` instance.

**To [[automation-vs-augmentation]]:** a third independent citation of the Scott Galloway "AI won't take your job, someone using AI will" reframe (after the London and Sydney editions), now echoed customer-side by Danske Bank's own change-management messaging; the asymmetric-allocation framework's "humans on judgment for differentiated work, agents absorb routine/compliant work" shape is a clean augmentation-calibration instance.

## What's *not* in this source

- **No USE/COMPOSE/BUILD, hourglass-organization, moats-erosion, or Project Mantle content** — all confirmed London-edition (May 2026) additions; see the relationships block.
- **No quantified MTTR or SecOps-log-analysis figures** — Allen's log-analysis-improvement claim is qualitative here ("dramatic") where the London edition supplies a 6h→7min figure.
- **No ingest of Peter Hinssen's *The Day After Tomorrow* or Ishit Vachhrajani's own talk/blog** — both are cited by Brozovich but not yet wiki sources in their own right. *Open follow-up.*
- **No ingest of the MIT NANDA report itself** — cited here for a third time across the AWS "leader's guide" franchise (also cited on the London and, per that source's relationship notes, likely the Sydney edition); still not an independent wiki source. *Open follow-up, now stronger given the repeat citation count.*

## Open questions for next ingest

- ~~Is Ishit Vachhrajani's four-mental-model-shifts talk itself available and worth ingesting as a primary source, given Brozovich (here) and Allen (implicitly, via the London edition's non-determinism doctrine) both lean on it?~~ **Resolved 2026-07-15**: yes — see [[2026-07-09-nyc-executive-forum-2026-a-leaders-guide-to-agentic-ai]], Vachhrajani's own AWS NYC Executive Forum keynote.
- Does Amazon's internal organizational-science team (Brozovich's "we have a team of organizational scientists... 1,500+ organizations annually") publish any of the business-lifecycle-phase research externally, beyond this conference restatement?
- Would a fourth Danske Bank data point (a published case study, if one exists) corroborate or extend the 35%-coding-time / Cloud Buddy / CheckMate claims presenter-reported here?
