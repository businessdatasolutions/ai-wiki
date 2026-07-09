---
type: source
kind: video
title: "Hannah Foxwell - The Reinvention of the Dev Team - AI Native DevCon June 2026"
author: ["AI Native Dev"]
url: "https://www.youtube.com/watch?v=pyYKOLEnsZk"
date_published: 2026-07-08
date_ingested: 2026-07-09
length: "~35:22 minutes (transcript 268 segments; auto-generated captions)"
raw: "../../raw/videos/hannah-foxwell-reinvention-of-the-dev-team-ai-native-devcon.md"
tags: [hannah-foxwell, ai-native-devcon, team-design, team-ratios, forward-deployed-engineer, product-engineer, vibe-coding-pm, platform-engineering, sre, minimum-viable-human, code-review, broken-comb-skills]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - strategic-renewal/organizational-culture
  - digital-seizing/strategic-agility
roles: [ceo, chro, cto, transformation-lead, product-manager]
relationships:
  - type: supports
    target: 2026-03-12-oreilly-steve-yegge-wants-you-to-stop-looking-at-your-code
    via: "Foxwell references Yegge's eight-levels framework directly (via a slide she credits to Luke Marsden), using it to reassure her audience that being at level 2-3 is normal — an independent, audience-facing confirmation that the framework has become common vocabulary across the AI-native-dev conference circuit by mid-2026."
    confidence: 0.7
  - type: supports
    target: 2026-06-19-lopopolo-ai-native-devcon-harness-engineering
    via: "Same conference (AI Native DevCon, June 2026) — Lopopolo supplies the technical-harness layer (how agents execute); Foxwell supplies the team-and-organizational layer (how humans reorganize around them). Complementary altitudes on the same event, not overlapping claims."
    confidence: 0.65
  - type: supports
    target: 2026-06-18-dumra-mit-smr-dbs-everyone-an-innovator
    via: "Both address team-ratio and role redesign under increased velocity — Dumra/DBS's innovation-pyramid and mini-CEO structure is the large-incumbent-bank lived instance; Foxwell's 2-dev:1-PM ratio experiments and her own 2-person-startup build are the small-team, real-time-experimentation instance of the same redesigning-internal-structures microfoundation."
    confidence: 0.6
---

# Hannah Foxwell - The Reinvention of the Dev Team

> I'm going to be talking about agentic software development, but I'm not going to be talking about the tools or technology. I'm going to be talking about what it means for our teams and how we organize ourselves with these new capabilities.

## TL;DR

A ~35-minute AI Native DevCon (June 2026) talk by **Hannah Foxwell** (independent advisor, writer, founder — building accessible AI learning experiences). Structured around **three anchors**: build something worth building / speed requires safety / people matter. Eight load-bearing claims:

1. **References Yegge's eight-levels framework** (via a slide credited to Luke Marsden) to orient the audience — explicitly reassures that being at level 2-3 is normal: *"I don't know many people who are operating at level eight, and I certainly don't know anybody who could say credibly that they're doing it safely."*
2. **Team-ratio experiments are underway, in both directions.** Some teams are trying 2 developers : 1 PM (vs. the traditional 6-8 engineers : 1 PM); Andrew Ng reportedly proposed the *inverse* at Davos — 2 PMs : 1 developer — on the logic that decision-making speed, not coding speed, is now the constraint on a single developer's backlog.
3. **New role patterns reducing the user-feedback loop.** The **vibe-coding product manager** (validates ideas with real working prototypes before work reaches the dev team); the **forward-deployed engineer** (not sales engineering — an empowered engineer embedded with users who can fix the product directly; Google was reportedly building this capability for its AI products); the **product engineer** (per Incident.io's writing — engineers who don't need PM permission to improve the product, working well specifically when building for a developer audience you already understand).
4. **Her own lived case.** Foxwell built a 2-person startup (a container base-image management platform) in two weeks to first working version; ran out of planned work by lunch on day one. The bulk of subsequent time went to platform engineering, security, and scalability — not feature work. Lesson: unlocked velocity forces *more ambitious* product thinking, not less — she had to "throw out" ruthless-prioritization habits and think several steps further ahead.
5. **Speed requires safety.** Manual steps anywhere on the path to production become the new bottleneck once code generation itself is fast; investment in pipelines, automated testing, feature flags, and progressive delivery (blue-green deployments) is what converts raw velocity into safely-shippable velocity. Names SRE vocabulary (SLIs, error budgets) as already having the right language for balancing velocity against reliability, and predicts **platform engineering and SRE headcount grows in relative importance**, not shrinks, as feature-team velocity increases.
6. **Mandatory code review is being questioned.** Some organizations have publicly dropped mandatory review on every change, shifting oversight left to spec-writing time instead. Quotes (attribution ASR-uncertain, rendered "Joseph Russia" — see Source quality): *"The mistake would be to treat unread code as a failure of discipline, rather than a signal that the discipline itself must change."*
7. **"Minimum viable human."** An agent can't hold an on-call pager. Sustainable on-call rotas (no one on-call more than 50% of the time, always a primary + secondary) become a structural floor on how small a team can actually get, independent of how much coding velocity agents provide.
8. **"Broken comb," not T-shaped.** Citing Sophie Weston (QCon), argues career development should aim for people with a broad base and *several* areas of depth (a "broken comb") rather than the classic T-shape — matches the shift toward product-leaning vs. platform-leaning generalist-engineer archetypes she's observing.

## What was actually ingested

The full auto-generated (ASR) English caption track — 268 segments, no chapters. Fetched cleanly on the first headless attempt (60s timeout, no retry needed) — notably the only one of this ingest batch's two videos that did *not* hit the known transcript-panel-timeout failure mode.

## Why this source matters to the wiki

This is the wiki's most direct **team-and-org-design companion** to its existing harness-engineering and agentic-engineering material — where most of the wiki's Yegge/Osmani-cluster sources describe *how agents are orchestrated technically*, Foxwell describes *how the humans around them have to reorganize*. It's also a same-conference companion to [[2026-06-19-lopopolo-ai-native-devcon-harness-engineering|Lopopolo's]] existing AI Native DevCon source, giving the wiki its first two-source view of a single event across two altitudes (technical harness layer vs. team/org layer).

## Linked entities and concepts

- [[Steve Yegge]] — independent confirmation of the eight-levels framework's spread across the conference circuit.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — team-ratio experimentation and role redesign as `digital-transforming/redesigning-internal-structures` instances.
- [[concepts/agentic-engineering|agentic-engineering]] — the org-design consequences of the practices that concept already documents at the individual-practitioner level.
- **Dangling** (single-source mention, deferred): **Hannah Foxwell**, **Luke Marsden**, **Andrew Ng** [note: already a wiki entity via [[Andrew Ng]] — the Davos/2-PM-to-1-developer claim is a *new* attributed claim on the existing entity page, not a promotion trigger], **Sophie Weston**, **Joseph Russia** (ASR-uncertain attribution — see Source quality), **AI Native Dev** (channel — see entity promotion below).

## Source quality

**Auto-generated (ASR) captions**, standard fidelity, fetched without retry. Light ASR cleanup applied: "Hannah Fox is" → "Hannah Foxwell is" (self-introduction). One quote attribution — rendered "Joseph Russia" in the ASR transcript — could **not** be confidently resolved to a known public figure or a plausible name correction; left as transcribed and flagged uncertain rather than corrected. Similarly, "Andrew Noon" (the Davos/2-PM-ratio claim) is left as transcribed; despite the topical proximity to [[Andrew Ng]], the name as spoken does not match closely enough phonetically to justify silently substituting a different real person's name, so it is **not** treated as an [[Andrew Ng]] attribution. First-party conference-talk source — personal/practitioner perspective, not a peer-reviewed or vendor-commissioned source; her own case study (the 2-person startup) is n=1 and self-reported.
