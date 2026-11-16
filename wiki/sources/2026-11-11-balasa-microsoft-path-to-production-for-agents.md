---
type: source
kind: video
title: "Your Path to Production for Agents"
author: ["Microsoft Developer"]
publisher: "Microsoft Developer (YouTube channel), Path to Production for Agents master class, episode 1; Adelina Balasa, AI Global Strategy Lead, Microsoft"
url: "https://www.youtube.com/watch?v=VZPAjGP3EH0"
date_published: 2026-11-11
date_ingested: 2026-11-16
length: "~1:02:29 minutes (transcript ~470 lines; ASR auto-generated track, 14 chapters)"
raw: "../../raw/videos/your-path-to-production-for-agents.md"
tags: [microsoft, microsoft-developer, azure, path-to-production-for-agents, adelina-balasa, master-class, pilot-to-production, demo-to-production, ai-center-of-excellence, intake-funnel, hub-and-spoke, citizen-developers, ai-governance, responsible-ai-council, agent-registry, shadow-agents, maturity-model, ai-landing-zones, infrastructure-as-code, zero-trust, ai-security, agent-identity, least-privilege, indirect-prompt-injection, red-teaming, pyrit, prompt-shields, agentops, canary-release, prompt-versioning, model-deprecation, llm-as-judge, golden-datasets, slo, error-budget, finops, solution-optimization, model-routing, semantic-caching, iteration-limits, agent-architectures, mcp, rag, edge-inference]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: 2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail
    via: "both address why an agent that works as a demo or pilot fails in production: the InfoQ talk names four engineering failure patterns inside one app-generation platform (context overload, tool explosion, orchestration hand-offs, no observability); Balasa names six organisational and platform pillars drawn from Microsoft customer engagements"
    confidence: 0.7
  - type: supports
    target: 2026-05-09-chase-agent-development-lifecycle
    via: "both lay out how agents are run once built: Chase's Build, Test, Deploy, Monitor loop inside a governance ring; Balasa's AgentOps pillar of versioned CI/CD, a model and prompt lifecycle, tracing and evaluations, and production controls"
    confidence: 0.75
  - type: supports
    target: 2026-10-19-smith-cohen-techcrunch-disrupt-okta-nanoco-agent-security
    via: "both treat agent access as an identity question: Smith and Cohen call agents the new insider and place enforcement outside the agent; Balasa describes agents as digital employees with their own managed identity, least-privilege access and on-behalf-of permissions"
    confidence: 0.7
  - type: supports
    target: 2026-08-26-chatterjee-agentic-governance-gap
    via: "both list controls for agents that take actions: Chatterjee's agent inventory, kill switches, red-teaming and action-scoped permissions as a board-level capability; Balasa's agent registry with named owners, emergency stop, red-teaming in the release pipeline and least-privilege identities, each told through an anonymised customer case"
    confidence: 0.7
  - type: supports
    target: 2026-09-29-bayer-rosmarin-chari-bcg-ai-agents-business-of-complexity
    via: "both describe a register of agents with owners and monitoring: Bayer Rosmarin's system of record for agents, modelled on HR and risk systems; Balasa's central agent registry with a named owner per agent, detection of unregistered agents and alerts on policy breaches"
    confidence: 0.65
---

# Balasa (Microsoft Developer) — six walls between an agent demo and production

> Building an AI agent that impresses as a demo has never been easier. Building one that is secure, governable, cost-effective, and capable of delivering consistent business value in production is a very different challenge. In this first episode in our Path to Production for Agents master class series, Adelina Balasa, AI Global Strategy Lead at Microsoft, shares a practical framework developed from working with hundreds of customers and partners, helping organizations navigate the journey from AI experimentation to enterprise-scale deployment. Rather than focusing solely on models, the series explores the architectural, operational, security, and organizational foundations required to successfully move agents from concept to production and beyond.
>
> The Path to Production for Agents series is built around six essential pillars that help organizations overcome the most common barriers to production success: AI Center of Excellence, AI Governance, AI Landing Zones, AI Security & Trust, Agent Ops, and Solution Optimization. Together, these pillars provide a roadmap for establishing the right people, processes, platforms, and practices to deploy and scale AI responsibly and efficiently. Each episode dives deeper into one of these pillars, offering practical guidance and actionable steps that teams can apply immediately.
>
> *— Channel description, Microsoft Developer*

## TL;DR

A 62-minute master class on [[Microsoft]]'s *Microsoft Developer* channel, published 11 November 2026: episode 1 of the *Path to Production for Agents* series. One speaker, **Adelina Balasa**, AI Global Strategy Lead at Microsoft per the description; she introduces herself as leading *"the global delivery strategy for AI apps and agents."* The talk is slide-led. **Auto-generated transcript, ASR-cleaned in quotation**: "Balasha" → Balasa, "a apps" → AI apps, "A governance" → AI governance, "PC" → PoC, "MOOPS to NLM ops" → MLOps to LLMOps, "list privilege access sculpt" → least-privilege access scoped, "individual colors permissions" → individual callers' permissions, "pirate" → PyRIT, "prom shields" → Prompt Shields, "duplication" → deprecation, "Phops" → FinOps, "rack" → RAG, "sold for months" → stalled for months.

What it adds to the wiki:

1. **The production gap stated as an organisational problem.** *"The thing standing in our way is almost never the model. Reaching for the newest, biggest model fixes none of this."* Teams that close the gap see value in about 12 weeks; the others are *"still trying about a year later or they just quietly gave up"* (1:14). No source is given.
2. **A six-pillar framework** (AI Center of Excellence, AI governance, AI landing zones, AI security and trust, AgentOps, solution optimization), each with three or four moves, one anonymised customer story per move, and KPIs; plus agent architectures as a layer underneath.
3. **An agent registry with a first-week count**: three ownerless agents surfaced at a national tax agency (19:15).
4. **Agents as digital employees**: own managed identity, least privilege, on-behalf-of permissions.
5. **AgentOps release mechanics**: prompts, code and model config versioned together; a bad change caught by a canary on 5% of traffic; golden datasets and LLM-as-judge as release gates; SLOs with error budgets.

A Microsoft employee on a Microsoft channel, opening a Microsoft delivery series. Most advice is product-neutral; the red-teaming and jailbreak-defence tools she names (PyRIT, Prompt Shields) are Microsoft's.

## The gap is not the model

*"It is genuinely easy these days to build an AI demo that makes a room say, 'Wow.' It is really hard to take that same agent into production and keep it running well."* A demo says nothing about thousands of simultaneous users, behaviour that *"isn't perfectly predictable"*, tools *"that take real actions"*, or answers that drift. Her conclusion: *"these are architectural and organizational problems. They're not model problems, which means they are yours to solve."* Teams *"almost never get stuck at build"* (3:06); they get stuck between a working build and one that is safe, fast and affordable in production. For each pillar she asks of a customer story: *"Why did the demo lie to us here?"*

The [[2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail|InfoQ talk on agentic systems failing in production]] covers the same demo-to-production gap from inside one platform's engineering, with four failure patterns and their fixes. Balasa's account is organisational and platform-level, drawn from customer engagements.

## The framework

| Pillar | The sentence she hears | Moves | What she would measure |
| --- | --- | --- | --- |
| **1. AI Center of Excellence** (4:29) | *"We've got 40 AI pilots and none of them is in production."* | business strategy alignment; technical direction; enablement; community and operating model | time from idea to production (*"ideally in about 3 months"*); share of pilots that reach production |
| **2. AI governance** (13:39) | *"We had an audit and we couldn't explain what our agents did."* | responsible AI and ethics; policy and standards; agent inventory and lifecycle; monitoring, alerting and maturity | agents registered and reviewed; shadow agents (*"ideally zero"*); audit readiness |
| **3. AI landing zones** (23:16) | *"The proof of concept worked, but then production stalled for months."* | infrastructure as code; networking and connectivity; reliability and resiliency; platform operations | time to stand up a new agent environment; share of agents on the governed zone |
| **4. AI security and trust** (32:00) | 80% fear data leakage, 88% worry about indirect prompt injection, about 50% don't know how AI will be regulated (unsourced) | identity and access; data protection and compliance; threat protection and adversarial testing | agents with their own identity; access scope; red-team pass rate; data leaks; incidents |
| **5. AgentOps** (38:39) | *"It looked good last week, but we can't prove that the next version is safe to release."* | CI/CD and deployment; model and prompt lifecycle; tracing, observability and evaluations; production controls | releases with evaluation evidence; change failure rate; time to recover |
| **6. Solution optimization** (45:42) | *"Why is it slow now? And why is the invoice much bigger than anyone had forecast?"* | model and tool selection; orchestration and workflow design; scaling and cost; performance and user experience | cost per successful task; perceived speed; use of capacity already paid for |

She introduces the pillars *"in no particular order"* (3:53). In the recap she says *"I think the sequence really matters"* (53:33): decide well (CoE), stay in control (governance), solid ground (landing zones), trust (security), ship like software (AgentOps), fast and affordable (optimization). She does not say which reading applies.

## Pillar 1: the AI Center of Excellence

A bank had about 40 pilots across a dozen teams; three had built the same policy Q&A bot, and when the CFO asked what the investment returned, *"no one was able to answer."* *"Organizations don't fail for lack of AI tools. They fail for lack of connected systems."* The cost of leaving it: *"12 months of value instead of 12 weeks"*, duplicated spend, *"the loudest voice wins"*, skills *"trapped in different pockets."*

- **Business strategy alignment.** At a retail bank a business strategy board ran a single intake funnel: every agent idea scored on value, feasibility, data readiness and risk *"before a single dollar… was committed."* In the first quarter it merged duplicate use cases, killed eight low-value experiments and fast-tracked two; the CFO now reviews projected against realised value per use case, and the first prioritised agent reached production in 10 weeks. This is `digital-seizing/balancing-digital-portfolios`: fewer bets, scored before funding. [[2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over|Krishna (IBM)]] addresses the same dispersion of pilots, with a budget split across 100 experiments as his example.
- **Technical direction.** An insurer with six teams building agents six ways got a reference architecture, an approved-patterns catalogue (*"a blessed agent framework, a standard RAG pattern"*) and a starter accelerator; a claims team then shipped a document agent in days.
- **Enablement.** A manufacturer with almost 200 ideas waiting on IT added role-based skilling, a governed on-ramp for citizen developers and a *"graduation path from a personal prototype to a supported production app"*: over 30 trained AI makers in two quarters. This is `digital-transforming/improving-digital-maturity`: building digital skills inside the firm.
- **Community and operating model.** A telecom company chose hub and spoke: the hub sets standards and funds shared assets, the business-unit spokes build, and a monthly community of practice shares components. *"There is no way we can have AI transformation without change management."* This is `digital-transforming/redesigning-internal-structures`.

## Pillar 2: AI governance

AI governance is *"the connective tissue that makes AI trustworthy and traceable."* A regulator asks an insurer how a claims-triage agent reached a decision three months ago; the team cannot reconstruct the prompt, model version, approver or data. Trust *"needs to be designed in from the beginning. It is not something that can be bolted on."*

- **Responsible AI and ethics.** A health customer's patient-reply agent went through a responsible AI council *"with a real charter and decision rights"* and a pre-deployment impact assessment; a clinician approves every draft. A fairness review found the model underserved non-English speakers, so the team added a check and a fallback.
- **Policy and standards.** A pharma company's policy pack sets which data classes an agent may touch, which models are approved, and a model card per model, readable *"in a matter of minutes, not a 100-page PDF that nobody wanted to open."*
- **Agent inventory and lifecycle.** A national tax agency found shadow bots no one had catalogued or could switch off. Its registry gives every agent a named owner who approves deployment and retirement, and detects anything unregistered; three ownerless agents surfaced in the first week, and when a model is deprecated the registry lists which agents must migrate. [[2026-08-26-chatterjee-agentic-governance-gap|Chatterjee]] writes that most organisations cannot produce a complete list of the agents running in their environment; [[2026-09-29-bayer-rosmarin-chari-bcg-ai-agents-business-of-complexity|Bayer Rosmarin]] describes a start-up building a system of record for agents.
- **Monitoring, alerting and maturity.** An energy company with *"governance on paper"* added alerts on policy breaches, ungrounded answers and blocked topics, so data, prompt or model drift is caught *"before your customers do."* It set quarterly targets on a five-level maturity model; her advice is to move one level at a time.

## Pillar 3: AI landing zones

A retailer's returns-assistant proof of concept took two weeks; four months later it was not live, because networking, private endpoints and capacity sat with the platform team and security would not sign off a one-off setup. A landing zone is *"the city's shared utilities that every workload can plug into."* Her four moves: landing zones in Terraform with self-service vending (a governed environment in hours, security reviewing the modules once rather than each project); zero-trust networking through private endpoints; active-active regions with provisioned throughput and pay-as-you-go spillover; and one owner, consistent tags and cost tracking per deployment, which let a logistics firm trace one agent's spend spike to one team.

## Pillar 4: AI security and trust

A help-desk agent on a shared API key with broad permissions reads a support ticket that hides an instruction to email customer records to an outside address. *"The agent is doing exactly as it was asked. No alarm sounds because technically nothing broke."* Because agents act, call tools and hold memory, *"the attack surface for agents just explodes"*: intent breaking, agent drift, tool misuse and memory poisoning on top of prompt injection and jailbreaks. *"Now we need to treat agents like digital employees."*

- **Identity and access.** The agent gets its own managed identity, least-privilege access scoped to the systems it needs, and on-behalf-of flow, so *"when an analyst queries the agent, it can only see what the analyst is allowed to see."* One misbehaving identity can be disabled without touching anything else. [[2026-10-19-smith-cohen-techcrunch-disrupt-okta-nanoco-agent-security|Smith (Okta) and Cohen (NanoCo)]] frame agent security around identity as well, calling agents the new insider.
- **Data protection and compliance.** An insurer under the EU AI Act and GDPR redacts PII on every input and output and adds data-loss prevention; a test caught the agent trying to put a member's full record into a summary.
- **Threat protection and adversarial testing.** A government digital-services team runs Prompt Shields, output validation and continuous red-teaming with PyRIT in the pipeline: *"they attack themselves on every release."*

The narration names three moves here, where the framework promises three to four per pillar.

## Pillar 5: AgentOps

*"We can ship, version, evaluate, and operate agents like software."* The story: one line of a prompt edited on a Friday afternoon, wrong refund amounts by Monday, and no way to say what changed or roll it back. She traces the discipline from DevOps through MLOps and LLMOps, because *"DevOps was never built for tool calling, memory, multi-step behavior."*

- **CI/CD and deployment.** Agent code, prompts and model config are versioned together, released behind a canary, with an emergency stop that reverts to the last known good version. The next bad change was caught on 5% of traffic and rolled back in minutes (41:51).
- **Model and prompt lifecycle.** A newsroom agent broke when its model was retired. Every model, prompt and tool definition now sits in a versioned inventory, and a deprecation process flags what is affected before a model sunsets.
- **Tracing, observability and evaluations.** A telecom company could not tell whether a new version was *"actually better than the previous version or was it just different."* Every candidate release now runs against golden datasets and LLM-as-judge evaluations as quality gates, with drift detection in production; a prompt that looked good in a demo failed the grounding evaluation and never shipped. The [[2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production|Google Cloud Tech eval clinic]] builds such a harness on screen for one agent.
- **Production controls.** A bank attached release evidence to every deployment and added SLOs with error budgets, an AI incident process and FinOps; a latency breach sent the on-call engineer to a runbook, and the spent error budget paused risky releases.

[[2026-05-09-chase-agent-development-lifecycle|Chase's agent development lifecycle]] describes this part of the work from LangChain's side, as test, deploy, monitor and govern stages.

## Pillar 6: Solution optimization

A customer-service copilot is *"snappy at 1:00 a.m. Painful at 2 p.m."*, and the first invoice lands at triple the forecast. Slowness has at least four sources (time to first token, inter-token latency, end-to-end time, concurrency), and a one-user demo cannot forecast any of them, so *"we never really finish optimizing."* The moves: model routing, with cheap models for classification and formatting and premium ones for hard reasoning; hard iteration limits, parallel lookups and focused sub-agents for a route-planning agent that ran *"an unbounded loop retrying a failing step and quietly burning money"* (*"faster and cheaper through the fact that they fixed coordination, not… the model"*); semantic and prompt caching with per-team quotas, whose cache hits absorbed *"a huge share of Black Friday traffic"*; and streaming and tuned retrieval to cut time to first token.

## The layer underneath: agent architectures

*"This is not a seventh wall. This is a layer that sits underneath all the other six pillars"* (54:44). Every agent is composed from four reference patterns: frameworks and orchestration; tools, function calling and MCP (*"the safe governed hands for your agents"*); knowledge, memory and context, including RAG; and multimodal, voice and edge. Her examples: an insurer whose *"one giant agent kept getting confused"*, split into intake, fraud-check and adjudication agents with a human at adjudication; a manufacturer's corporate tool catalogue on MCP shared by its maintenance and procurement agents; shared RAG standards and a shared vector store for a global firm's research agent; and a voice agent for car technicians with inference on the device.

She closes: *"Look at the wall you're stuck behind right now. Pick that pillar and start with one of the moves."*

## Linked entities and concepts

- [[Microsoft]] — channel owner (*Microsoft Developer*) and the speaker's employer.
- **Concepts:** [[agent-development-lifecycle]] (AgentOps), [[agent-fleet-management]] (agent registry), [[agent-oversight-and-delegation]] (agent identity, human in the loop), [[responsible-ai]] (governance pillar), [[enterprise-ai-adoption]] (pilots that never reach production), [[ai-agents]].
- **Neighbouring sources:** [[2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail]], [[2026-05-09-chase-agent-development-lifecycle]], [[2026-10-19-smith-cohen-techcrunch-disrupt-okta-nanoco-agent-security]], [[2026-08-26-chatterjee-agentic-governance-gap]], [[2026-09-29-bayer-rosmarin-chari-bcg-ai-agents-business-of-complexity]], [[2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over]], [[2026-09-30-zamora-feroz-why-your-ai-agent-fails-in-production]].
- **Dangling** (single-source mention, deferred): Adelina Balasa, Path to Production for Agents (series), AI landing zones, PyRIT, Prompt Shields, Terraform.

## Source quality

Auto-generated ASR track, cleaned in quotation only. The talk is slide-led and the narration points at slides (*"looking at the symptoms on the right"*, *"here's the idea in one picture"*) whose content is not captured; the stills scan failed (Gemini 402) and is deferred, so the framework table above is reconstructed from the narration. The customer stories are anonymised, with no names, dates or outcome data beyond the quoted figures; two are told twice (the shared-key help-desk agent, the Friday prompt edit). The 12-weeks figure and the three security percentages have no stated source. YouTube's chapter title *"AU Security and Trust"* is a typo for AI. Useful as a checklist with a concrete mechanism per pillar, not as evidence of their effect.
