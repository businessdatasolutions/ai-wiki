---
type: source
kind: video
title: "Google's approach to security review with agents"
author: ["Google Cloud Tech"]
publisher: "Google Cloud Tech livestream; Mollie Pettit, Aron Eidelman and Nick Galloway (Google)"
url: "https://www.youtube.com/watch?v=czKuoutcwYc"
date_published: 2026-10-20
date_ingested: 2026-10-25
length: "~1:02:10 (transcript ~536 segments; auto-generated captions, corrected in quotes)"
raw: "../../raw/videos/googles-approach-to-security-review-with-agents.md"
tags: [google, google-cloud-tech, mollie-pettit, aron-eidelman, nick-galloway, mantis, codemender, antigravity, security-review, vulnerability-discovery, false-positives, threat-modeling, skills, hooks, test-driven-development, secure-coding, side-quests, adversarial-review, sandbox-verification, model-refusals, cyber-verification, time-to-exploit, shift-left, devsecops, engineering-culture, mythos, livestream]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
  - strategic-renewal/organizational-culture
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-06-22-grinstead-how-i-ai-mozilla-firefox-agentic-security-harness
    via: "both describe production harnesses for AI vulnerability finding, where the hard part is removing false positives through staged review and verification rather than finding candidate bugs"
    confidence: 0.75
  - type: supports
    target: 2026-10-21-lewis-nadeau-mckinsey-strategy-room-frontier-ai-cybersecurity
    via: "both concern the collapse of time-to-exploit and the claim that the harness around a model matters more than the model for security work"
    confidence: 0.7
  - type: supports
    target: 2026-09-30-chow-metalware-ai-firmware-vulnerability-research
    via: "both concern defenders building on frontier and open models after Mythos showed AI could find real vulnerabilities at scale"
    confidence: 0.6
---

# Pettit, Eidelman & Galloway (Google Cloud Tech) — security review with agents

> How are security engineers at Google using agents to review code for vulnerabilities? How are they making the process more proactive and developer friendly? We will explore tools like Mantis, a multi-agent framework that automates security auditing and uses multi-step reasoning and a verification pipeline to minimize false positives.
>
> We will also demonstrate how to use Antigravity CLI with custom skills and hooks to perform interactive code reviews, catching vulnerabilities that may slip through "vibe-coded" or manually written features the moment the code is written.

## TL;DR

A one-hour livestream on the *Google Cloud Tech* channel ([[Google]]), 20 October 2026. **Mollie Pettit** (developer relations) moderates; **Nick Galloway**, a security engineer, describes **Mantis**, Google's agent framework for security review; **Aron Eidelman**, a developer security advocate, shows how he builds security into a test-driven agent workflow. Five claims:

1. **Asking an agent to "find vulnerabilities" floods you.** It returns *"maybe 20, maybe 30, hundreds,"* of which *"maybe a few percent"* are real, because the model does not know the code's context. Mantis finds the same bugs, then strips false positives using a threat model and architecture built up front.
2. **Divide the work by agenda, not persona.** Not *"the security engineer agent"* but separate skills for threat modelling, critique, and particular vulnerability classes, which is also *"very efficient from a token perspective."* Never let the agent that wrote code review it: *"if you give an agent a job to… disprove this thing, it'll work really hard to do that."*
3. **Deterministic where possible.** Skills can fail to fire, so a hook forces a deterministic scan before every push (Semgrep, regex rules for API keys, then an agent review). *"For some things you actually don't want to use agents… we have really good tools for this. It's called a regex."* Sandbox verification of an exploit happens in about 0.1% of cases.
4. **The harness matters more than the model.** Teams at other companies say *"the harness that you have really makes the difference. And you can even get away with pretty light frontier model."* Every code change in Google Cloud is now scanned by Mantis.
5. **The window has closed.** Citing Mandiant and Verizon's DBIR: average time to exploit a new CVE fell from 62 days in 2018 to seven days in 2025, with about a third exploited within 24 hours. *"For the first time in history, code exploitation is now an easier way to start a breach than phishing or credential theft."*

## Key claims

### Mantis

Galloway began around Christmas 2025 trying a local Gemma model on the Linux kernel: *"it went horribly and it didn't find anything,"* but taught him to break the problem into chunks an agent can handle. *"A few months later, Mythos comes out… It's quite clear, this can really work,"* and Mantis became an internal project built on the advice of many Google security engineers, later open-sourced with a reference harness on Google's Agent Development Kit. Engineers had been asking agents naively and drowning in false positives; Mantis puts process around it: threat model and architecture first, so *"we can know where those trust boundaries are and then drop those off if they're not relevant later."* For learning, it keeps a knowledge base with a self-reflection step, and uses *"decay of memory"* so a wrongly learned false positive fades. A quick pull-request scan *"has to be done in a minute or two."*

### Security inside a test-driven workflow

Eidelman's inner loop: a threat-model skill at planning (a markdown file for a solo developer; a shared store for teams, where changes need justification); failing tests that include security edge cases (*"if I'm a normal user and not an admin and I try to access this admin endpoint, do I get a 403"*); and a *defensive developer* skill that names the project's own helper methods, to stop coding agents going on *"side quests"* and rewriting helper libraries, code that *"pass[es] all the tests, but… creates more technical debt."* A skill that proposes updates to other skills borrows from site reliability engineering, where manual work is a bug; but it tends to update every skill, so he reviews the proposals to avoid *"context rot,"* asking whether he is automating toil (repeated) or grunge work (rare).

### Skills, hooks and harnesses

A skill is task-specific instructions an agent loads when relevant, *"a non-deterministic substitute for… command primitives,"* or simply *"put this hat on for this specific moment."* A harness is the agent with its tools and loop; skills slot into an existing harness such as Antigravity or Claude Code. Static analysis keeps its place: *"agents are… not replacing everything,"* and if they tried *"they would just end up recreating those static tools themselves."* Static tools will never find a novel buffer overflow or an insecure direct object reference; agents can.

### Guardrails that block defenders

Model refusals stop defenders too, because defensive verification looks like offence: *"the defensive and the offensive stuff, it's kind of indistinguishable when you're trying to do that repro."* Programmes such as Anthropic's cyber verification programme, available on Google Cloud, give vetted defenders less-restricted models. Reverse engineering is now fast: a weekend take-home task Galloway once did, reversing a Windows patch into an exploit, *"wouldn't take very long… at all"* now, and a firmware blob can be understood *"in a matter of minutes."*

### Shift left, and culture

Eidelman on why earlier shift-left efforts failed: leadership treated it as a bottom-up task, bought tools, and left developers *"inundated"* with noise, so they worked around it. It worked where there was *"a top down mandate,"* security engineers in design meetings, and acceptance of six months to a year of friction. Culture decides it: in a *"generative culture where information flows very freely,"* this spreads; in a bureaucratic or *"pathological culture where people are very afraid of making mistakes,"* it does not. Their own example: a security engineer's project became a developer's workflow and is now taken to customers by *"500"* customer engineers and forward-deployed engineers.

## Dynamic-capabilities reading

- **`digital-transforming/improving-digital-maturity`** — security review moved into the development loop with skills, hooks and automated PR scanning across Google Cloud.
- **`strategic-renewal/organizational-culture`** — shift-left succeeds with a top-down mandate and a generative culture, and fails in a bureaucratic or fearful one.
- **`contextual/external-triggers`** — time-to-exploit falling to days, and exploitation overtaking phishing as the easier way in.

## How it connects

- [[concepts/attack-surface-management|attack-surface-management]] — 62 days to seven, a third within a day, and code exploitation easier than phishing.
- [[concepts/agent-harness|agent-harness]] — Mantis as a security harness, skills versus harness, deterministic hooks, and the claim that the harness outweighs the model.
- [[concepts/ai-generated-code-quality|ai-generated-code-quality]] — security tests written before the code, and agents' side quests as a source of debt.
- [[2026-06-22-grinstead-how-i-ai-mozilla-firefox-agentic-security-harness|Grinstead (Mozilla)]] — the other production security harness in the wiki, also built around a verifier.
- [[2026-10-21-lewis-nadeau-mckinsey-strategy-room-frontier-ai-cybersecurity|Lewis & Nadeau (McKinsey)]] — the same week, the same time-to-exploit argument from consultants.
- [[2026-09-30-chow-metalware-ai-firmware-vulnerability-research|Chow (Metalware)]] — Mythos-level capability, from defence.

## What was actually ingested

The full livestream (1:02:10, `length_seconds: 3730`) from captions that read as auto-generated; product and people names are corrected in quotes. The first 30 seconds are unrelated pre-roll. Audience questions are included where the speakers answer them. No stills: the screen shares are code, markdown files and a diagram that the speakers describe in words.

## Linked entities and concepts

- [[Google]] — publisher (*Google Cloud Tech* is an alias) and employer of all three speakers. Updated in this ingest.
- [[concepts/attack-surface-management|attack-surface-management]], [[concepts/agent-harness|agent-harness]], [[concepts/ai-generated-code-quality|ai-generated-code-quality]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the three cells tagged above.

**Dangling** (single-source mention, deferred): Mollie Pettit, Aron Eidelman, Nick Galloway, Mantis, CodeMender.

## Scope and reliability

Google engineers describing Google tools on Google's channel, partly to promote them (CodeMender is in gated preview). The 0.1% escalation rate is one developer's two months of use; the time-to-exploit figures are cited from Mandiant and DBIR from memory, not shown. The claim that the harness outweighs the model is reported from conversations with other companies. Its value is a detailed practitioner account of how agentic security review is built and where deterministic tools still win.
