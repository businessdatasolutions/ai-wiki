---
title: "The Agentic Governance Gap: Why Autonomous AI Systems Demand a New Cybersecurity Discipline"
authors: ["Dave Chatterjee"]
venue: "Analytics Magazine (INFORMS) — 'Cyber Resilience in the Age of Intelligent Systems' column"
doi: "10.1287/LYTX.2026.03.04"
url: "https://doi.org/10.1287/LYTX.2026.03.04"
date_published: 2026-08-26
attachment: 2026-08-26-chatterjee-agentic-governance-gap-analytics-magazine.pdf
fulltext_source: pdf-converted
converter: "pdftotext -layout"
notes: |
  Acquired 2026-09-15 from a browser print-to-PDF the user placed in raw/articles/
  (print timestamp 15-09-2026 07:24 appears in the page header). Routing confirmed correct:
  a practitioner magazine column, not a peer-reviewed paper — stays in raw/articles/.
  8 pages; `pdftotext -layout`. Print-artifact chrome (SHARE / PRINT ARTICLE lines, nav
  furniture) is retained verbatim rather than stripped, so the extract is auditable against
  the PDF. NOTE: this Chatterjee is **Dave Chatterjee** (cybersecurity academic), NOT the
  **Abhishek Chatterjee** of wiki/sources/2026-05-07-chatterjee-anatomy-of-agent-harness.md —
  unrelated authors who share a surname.
---

15-09-2026, 07:24 The Agentic Governance Gap | Analytics Magazine

 

 August 26, 2026 in Cyber Resilience in the Age of Intelligent Systems

 The Agentic Governance Gap
 Why Autonomous AI Systems Demand a New Cybersecurity
 Discipline
 By Dave Chatterjee

 SHARE:    

 PRINT ARTICLE:

 https://doi.org/10.1287/LYTX.2026.03.04

 Enterprises are no longer deploying AI that merely drafts, summarizes, or recommends. A new
 generation of systems – AI agents – can plan multi-step tasks, invoke tools and APIs, move data
 between systems, and take consequential action with little or no human review in the loop.

 The shift sounds incremental. It is not. It is the difference between a system that produces a
 document and a system that executes a transaction, and most enterprise governance structures
 were never built for the latter.

 Generative AI’s first wave raised legitimate concerns about hallucination, bias, and data leakage –
 all serious risks, but also all contained within a single, familiar boundary: content. A human read
 the output before anything happened in the real world. Agentic AI erases that boundary. The
 output is not a paragraph for a person to evaluate; it is an action already taken – a record
 updated, a payment initiated, a support ticket resolved, a downstream agent instructed to
 proceed. By the time a human notices, the consequence has already occurred.

 The Core Problem
 Most current AI governance programs were designed around a copilot model: a system
 proposes, a person disposes. Approval workflows, review gates, and audit trails all assume that a
https://pubsonline.informs.org/do/10.1287/LYTX.2026.03.04/full/ 1/8

---

15-09-2026, 07:24 The Agentic Governance Gap | Analytics Magazine

 human sits between recommendation and consequence. Agentic architectures are quietly
 dismantling that assumption, not through malice or negligence, but because autonomy is the 
 entire value proposition. Organizations are adopting agents specifically to remove the human
 bottleneck. The governance model built to catch mistakes is being designed out of the system at
 the same moment the system’s capacity to cause harm is increasing.

 This is not a hypothetical concern. Enterprises have already reported agents that looped
 indefinitely on a flawed instruction, agents that invoked the wrong API with elevated credentials,
 and multi-agent systems where one agent’s error propagated into a second agent’s decision
 before any person was aware a problem existed. None of these required a sophisticated
 adversary. Ordinary operational fragility, once confined to human error, is now compounding at
 machine speed.

 Three Converging Forces
 Three trends are converging to make agentic governance an urgent enterprise priority, not a
 future concern.

 Autonomy creep: Agents are being granted broader permissions incrementally, often
 without a corresponding review of what those permissions, in aggregate, now allow the
 agent to do. A capability added for one workflow quietly becomes available to every task
 the agent touches.
 Tool and API sprawl: Agents derive their power from the tools they can call. As
 organizations connect agents to more internal systems – CRMs, ticketing platforms,
 financial systems, code repositories – the attack surface and error surface expand
 together. A single compromised or misconfigured agent can now reach far more of the
 enterprise than any single compromised employee account.
 Multi-agent coordination: Agents increasingly delegate to other agents, and human
 oversight recedes further with each additional hop. A flawed instruction, a poisoned data
 source, or a manipulated prompt can cascade through a chain of agents before a person is
 positioned to intervene.

 What Agentic Governance Means
 Agentic governance is not a policy document or an ethics checklist. It is an operational capability:
 the demonstrable ability to know, at any moment, what every agent in the enterprise is authorized
 to do, what it has done, and how quickly it can be stopped. In architectural terms, it rests on five
 interdependent capabilities.

 Action-scoped permissions limit each agent to the minimum set of tools and data required
 for its specific task, rather than inheriting broad, reusable credentials.
 Real-time action visibility gives security and business teams a live, auditable record of
 every action an agent takes, not just the prompts it receives.
 Circuit breakers and kill switches allow any agent, or any chain of agents, to be halted
 immediately when behavior deviates from expected patterns.
 Escalation thresholds define, in advance, which categories of action require human
 confirmation before execution, calibrated to consequence and reversibility, not
 convenience.

https://pubsonline.informs.org/do/10.1287/LYTX.2026.03.04/full/ 2/8

---

15-09-2026, 07:24 The Agentic Governance Gap | Analytics Magazine

 Cross-agent identity and provenance ensure that when one agent acts on another agent’s
 output, the origin, authorization, and confidence of that input can be traced and verified. 
 Most organizations are not one policy memo away from agentic safety. They are years of
 architectural discipline away from being able to answer a basic question: what can our agents do,
 right now, across the enterprise? The quantum-readiness and crypto-agility challenges this
 column examined previously share the same root failure. The capability gap is not technical
 sophistication. It is the absence of inventory, visibility, and rehearsed control.

 A Leadership and Organizational Challenge
 As with cryptographic agility, the deeper reframing this moment demands is that agentic AI risk is
 not a problem to delegate to a data science or platform engineering team. It is a governance
 challenge that begins at the board level and cascades through every function that deploys,
 connects to, or depends on an autonomous system. The commitment-preparedness-discipline
 (CPD) framework maps directly onto the structural requirements of agentic governance:

 Commitment: Leadership and Intent. Executive ownership of agent risk appetite cannot be
 delegated to the teams building the agents. The C-suite must define, in business terms,
 which categories of decisions an agent may make unsupervised, and which categories
 always require a human. Board-level visibility into what autonomous systems are
 authorized to do is now as material as visibility into financial controls.
 Preparedness: Building the Capability. Organizations must maintain a live inventory of
 every agent in production, its permissions, its tool access, and its failure modes, before they
 can govern it. Preparedness also requires red-teaming agentic workflows the way security
 teams red-team networks, deliberately probing for permission creep, prompt manipulation,
 and cascading multi-agent failure.
 Discipline: Consistent Execution. Agentic governance is not a launch review; it is a
 continuously managed program. Discipline means ongoing permission audits, tested kill
 switches, logged and reviewed agent actions, and regular drills that simulate an agent
 behaving badly, measuring not whether it can be stopped, but how long it takes.

 The commitment pillar surfaces the most common early failure: agents are deployed by
 individual product or engineering teams without an enterprise view of cumulative exposure. The
 preparedness pillar exposes the second most common failure: organizations frequently cannot
 produce a complete list of every agent operating in their environment, let alone what each one
 can touch. The discipline pillar reflects the hardest and most durable failure: kill switches that
 exist on paper but have never been exercised under realistic conditions. Applied consistently, the
 three pillars converge on a single test: Can the enterprise show, for any agent action, that it was
 bounded, authorized, and reversible – not as a one-time launch review, but as a standing
 operational capability?

https://pubsonline.informs.org/do/10.1287/LYTX.2026.03.04/full/ 3/8

---

15-09-2026, 07:24 The Agentic Governance Gap | Analytics Magazine

 

 First Steps Toward Agentic Governance
 Inventory every agent and its permissions. Identify what each agent can access, what tools it can
 invoke, and what actions it can take without human confirmation. This is the foundation every
 subsequent step depends on.

 1. Classify actions by consequence and reversibility. Not every action carries the same risk.
 Sort agent-eligible actions into tiers and require human confirmation for anything high-
 consequence or difficult to reverse.
 2. Build circuit breakers before scaling autonomy. Every agent granted broader authority
 should be paired with a tested mechanism to halt it immediately – not one designed after
 an incident.
 3. Establish clear ownership for agent behavior. Fragmented accountability, where no single
 function owns an agent’s real-world actions, is a root cause of agentic risk, just as it was for
 cryptographic fragility.
 4. Run agentic failure drills. Simulate a misfiring agent, a poisoned input, or a cascading
 multi-agent error, and measure actual detection and response time rather than assuming it.
 5. Extend vendor diligence to agentic capability. Ask every AI vendor what actions their
 systems can take autonomously and what controls exist to constrain them. The answer is a

https://pubsonline.informs.org/do/10.1287/LYTX.2026.03.04/full/ 4/8

---

15-09-2026, 07:24 The Agentic Governance Gap | Analytics Magazine

 proxy for how much of your operational risk you are delegating to their engineering
 choices. 
 Five Years From Now: Who Succeeds, Who Struggles
 Organizations that navigate the agentic transition successfully will not be distinguished by which
 AI models they adopted. They will be distinguished by whether they treated agent autonomy as a
 continuously governed capability or as a feature rollout evaluated once at launch and left
 unmonitored. Organizations that succeed will maintain real-time visibility into agent actions,
 enforce tiered escalation by consequence, and treat kill-switch readiness as a rehearsed
 operational discipline rather than a design assumption.

 Organizations that struggle will discover, after an incident, that an agent had accumulated
 permissions no one had reviewed, that no one owned the decision to grant those permissions,
 and that stopping the agent took hours rather than seconds. The pattern is familiar. It is the same
 preparedness gap that has defined cybersecurity underperformance for a generation, now
 operating at the speed of autonomous execution.

 Removing the Buffer
 Agentic AI does not introduce an entirely new category of risk so much as it removes the buffer
 that has, until now, absorbed the consequences of AI error: the human reviewer standing between
 recommendation and action. That buffer is being designed out of enterprise systems deliberately,
 because removing it is the point. The organizations that will navigate this transition are those that
 recognize now that autonomy without governance is not efficiency. It is exposure with a faster
 clock.

 That capability requires sustained commitment from senior leadership, deliberate investment in
 agent inventory and tiered control, and the disciplined execution of continuous monitoring. It is, in
 that sense, a governance challenge before it is a technical one. Autonomous systems will only be
 as trustworthy as the organizational discipline built around them.

 Dave Chatterjee

 Dave Chatterjee, PhD, is an adjunct associate professor at Duke University and the creator of
 the commitment-preparedness-discipline framework. His research and advisory work focus
 on cybersecurity leadership, AI-driven risk and operational resilience under real-world stress.
 He is the author of Cybersecurity Readiness: A Holistic and High-Performance Approach and
 The DeepFake Conspiracy.
https://pubsonline.informs.org/do/10.1287/LYTX.2026.03.04/full/ 5/8

---

15-09-2026, 07:24 The Agentic Governance Gap | Analytics Magazine

 SHARE:    
 
 Keywords: Agentic AI

 Sign Up for Analytics Magazine Updates and
 News

 SUBSCRIBE CONTACT ADVERTISE CONTRIBUTE

https://pubsonline.informs.org/do/10.1287/LYTX.2026.03.04/full/ 6/8

---

15-09-2026, 07:24 The Agentic Governance Gap | Analytics Magazine

 

 Institute for Operations Research and the Management Sciences

 5521 Research Park Drive, Suite 200
 Catonsville, MD 21228 USA

 INFORMS (Institute for Operations Research and the Management Sciences) is a U.S. 501(c)(3) nonprofit organization; EIN: 52-
 1898636.

 phone 1 443-757-3500

 phone 2 800-4INFORMS (800-446-3676)

 fax 443-757-3515

 email informs@informs.org

 Get the Latest Updates

 Email Address Submit

 Discover INFORMS
 Explore OR & Analytics
 Get Involved
 Impact
 Join Us

 Recognizing Excellence
 Professional Development
 Resource Center
 Meetings & Conferences
 Publications
 About INFORMS
 Communities

 PubsOnLine
 2024 INFORMS/ALIO/ASOCIO International Conference
 Certified Analytics Professional
 Career Center
 INFORMS Connect

 Copyright 2026 INFORMS. All Rights Reserved
 INFORMS Code of Conduct Terms of Use Privacy Contact INFORMS Sitemap

https://pubsonline.informs.org/do/10.1287/LYTX.2026.03.04/full/ 7/8

---

15-09-2026, 07:24 The Agentic Governance Gap | Analytics Magazine
 Follow INFORMS on:
 X Facebook Linked In Bluesky
 

https://pubsonline.informs.org/do/10.1287/LYTX.2026.03.04/full/ 8/8

---
