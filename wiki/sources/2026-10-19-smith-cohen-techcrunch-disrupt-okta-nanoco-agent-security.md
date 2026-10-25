---
type: source
kind: video
title: "Why Application-Level Permissions Won't Secure AI Agents With Okta's & NanoCo | Disrupt 2026"
author: ["TechCrunch"]
publisher: "TechCrunch — Disrupt 2026 stage session; Ric Smith (Okta) and Gavriel Cohen (NanoCo)"
url: "https://www.youtube.com/watch?v=4FZTk2J4tc0"
date_published: 2026-10-19
date_ingested: 2026-10-25
length: "~28:30 minutes (transcript ~122 segments; auto-generated captions, corrected in quotes)"
raw: "../../raw/videos/why-application-level-permissions-wont-secure-ai-agents-okta-nanoco-disrupt-2026.md"
tags: [techcrunch, disrupt-2026, okta, nanoco, nanoclaw, openclaw, ric-smith, gavriel-cohen, agent-security, agent-identity, insider-threat, least-privilege, cross-app-access, sandboxing, enforcement-outside-the-agent, intent-based-authorization, judge-model, plan-approval, shadow-ai, kill-switch, agent-owner, agent-teams, security-debt, cve-backlog, n-1-patching, vm-escape, mythos]
dynamic_capabilities:
  - contextual/external-triggers
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-10-13-romeo-bloomberg-new-economy-wrong-ai-race
    via: "both concern the controls an agent needs to be accountable: Romeo's identity, permission, accountability and revocability; Cohen's named owner per agent and kill switches at every layer"
    confidence: 0.65
  - type: supports
    target: 2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet
    via: "both concern agents acting with a person's identity and permissions: Klein's agent identity and logins (with Okta as a partner), Smith's agents that inherit the scoped grants of the human they act for"
    confidence: 0.6
  - type: supports
    target: 2026-08-25-lukic-goydan-bcg-so-what-ai-costs-a-fortune
    via: "both concern shadow AI: banning unapproved use does not work, and the safer course is to give people governed alternatives"
    confidence: 0.6
  - type: supports
    target: 2026-10-21-lewis-nadeau-mckinsey-strategy-room-frontier-ai-cybersecurity
    via: "both treat agents as non-human identities and potential insiders, and old unpatched vulnerabilities as newly exploitable at machine speed"
    confidence: 0.65
---

# Smith & Cohen (TechCrunch Disrupt 2026) — why application-level permissions won't secure AI agents

> Enterprises are learning to rebuild the basics of cybersecurity from scratch for agentic AI. Okta's President of Products and Technology Ric Smith and NanoCo Co-Founder and CEO Gavriel Cohen explain what agent security takes at the infrastructure level and which architectural choices matter most.

## TL;DR

A 28-minute stage conversation at TechCrunch Disrupt 2026, on the **[[TechCrunch]]** channel, 19 October 2026. **Ric Smith**, president of products and technology at **Okta**, and **Gavriel Cohen**, co-founder and CEO of **NanoCo**, maker of the open-source **NanoClaw** agent. Okta invested in NanoCo's seed round, as both disclose. Five claims:

1. **Agents are the new insider.** We give employees access through onboarding but have not done the same for agents, *"yet we personify agents in the same way that we do a human worker."* *"Identity's always been the last perimeter."* Some companies now treat AI spend and headcount *"interchangeably"* in team budgets.
2. **"Don't trust AI agents."** Not a reason to avoid them, but a design rule: enforcement *"outside of the agent's training, outside of the agent's instructions, and outside of the agent's environment."* Put the agent in a box, connect it on purpose, and ask for human approval only at the consequential step, typically *"when it's going to send that spreadsheet out to somebody else."*
3. **Check actions against the approved plan.** NanoCo has the agent state its plan, the user approves it, and a judge model checks every action, asking not *"is this safe or unsafe"* but *"is this aligned with the plan."* Okta's version starts from deterministic fine-grained access and treats intent as a further narrowing.
4. **Locking agents out can make security worse.** An employee at a large enterprise, unable to connect an agent to the data lake, exports *"tens of thousands of records"* of customer data each week and uploads them to Claude on the web. Smith has seen a company's SOX compliance compromised the same way.
5. **Old debt is now dangerous.** Unpatched CVEs are *"time bombs"*: anyone can run an open-weight model on *"a rack of Mac minis"* against them. Agents *"look at your infrastructure like it's Swiss cheese."* Smith's first advice: run an N-1 patch programme.

## Key claims

### Why NanoClaw exists

Cohen started at the end of January 2026 by connecting frontier agents (through OpenClaw) *"to everything,"* setting security aside. *"I got tremendous value from it. It did the work of an employee,"* but with *"major major security gaps,"* so he built NanoClaw to give the same value without the compromise. Agents also need protecting: *"If the agent has a browser, that browser has to be patched,"* or an attacker can take over the agent's accounts.

### Two layers of control

Okta takes the broad view: agents get only specific toolkits, and an agent acting for a person receives that person's grants, scoped, with every claim audited. NanoCo works around the agent itself: IT and security set the outer boundary of what agents may do; employees can tighten it; agents get least privilege by default, with policies on specific actions such as sending or searching email. The common mistake Smith sees is companies *"running towards value"* and discovering their exposure later, because the basic mapping of data, toolkits, applications and roles was never done.

### Assume the agent escapes

Cohen: build least privilege into infrastructure as well as access, assuming container and even VM escapes (he cites a recently reported VM-escape zero-day): *"what can this pod access? What can this node access? What can this VPC or this whole account access?"* Smith: Mythos *"put the nail in the coffin"* on postponing the fundamentals, and creates *"a tyranny in the system"*: large firms can afford AI to find and patch vulnerabilities, while *"a regional hospital out in the middle of Midwest… constantly barraged with ransomware… they've got no hope."*

### Kill switches and owners

Both say agents need kill switches *"at varying degrees"*: revoking an employee's access, changing a policy, cutting a tool, cutting inference, and a global switch for a whole account. But most companies are *"very far from the kill switch because employee agents are running on laptops… where there's no isolation."* NanoCo's rule: *"every agent needs to have an owner, somebody who is taking ultimate responsibility for it."*

### Agent teams

Cohen expects the next three to six months to be about teams of agents, *"probably a new scaling law"* after training and test-time compute: *"I'm running probably 32 agents on a team at the moment,"* and he expects hundreds. Some labs argue agents will make better decisions than people and *"we work for them"*; he wants to build the future *"where I'm still directing agents."* Smith's customers are moving from agents acting for a user to agent-to-agent interaction and agent commerce. Cohen's advice to founders: enterprise security reviews take *"3, 4, 6 months,"* so build for the problems of four to six months from now, and be *"more ambitious."*

## Dynamic-capabilities reading

- **`contextual/external-triggers`** — Mythos-level offensive capability and cheap open-weight models turning old vulnerabilities into live risks.
- **`contextual/internal-barriers`** — years of security debt, access never mapped before deployment, agents running on laptops without isolation, and lockdowns that push staff to riskier workarounds.

## How it connects

- [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]] — enforcement outside the agent, approval only at the consequential step, plan-and-judge checking, owners and kill switches.
- [[concepts/attack-surface-management|attack-surface-management]] — CVE backlogs as time bombs, assumed container escape, and N-1 patching.
- [[concepts/agent-fleet-management|agent-fleet-management]] — teams of tens of agents per person as the next frontier.
- [[2026-10-13-romeo-bloomberg-new-economy-wrong-ai-race|Romeo (Oliver Wyman Forum)]] — license plates for agents: identity, permission, accountability, revocability.
- [[2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet|Klein (Browserbase)]] — agent identity and logins, with Okta named as a partner.
- [[2026-08-25-lukic-goydan-bcg-so-what-ai-costs-a-fortune|Lukic & Goydan (BCG)]] — shadow AI cannot be banned.
- [[2026-10-21-lewis-nadeau-mckinsey-strategy-room-frontier-ai-cybersecurity|Lewis & Nadeau (McKinsey)]] — agents as non-human identities, and the same old-vulnerability problem.

## What was actually ingested

The full session (28:30, `length_seconds: 1710`) from auto-generated captions; names and products are corrected in quotes. The moderator is not named in the captions. No stills: a stage conversation.

## Linked entities and concepts

- [[TechCrunch]] — publisher. Entity created in this ingest (second source as `author:`).
- [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]], [[concepts/attack-surface-management|attack-surface-management]], [[concepts/agent-fleet-management|agent-fleet-management]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the two cells tagged above.

**Dangling** (single-source mention, deferred): Ric Smith, Gavriel Cohen, Okta (also named on the Klein page), NanoCo, NanoClaw.

## Scope and reliability

Two vendors who sell agent security, one an investor in the other, on a conference stage. The anecdotes (the weekly customer-data export, the SOX case) are unverified, and the claims about agent teams as a scaling law are Cohen's expectation. Its value is a concrete, current account of how agent access is being controlled in practice, including the argument that lockdowns can raise risk.
