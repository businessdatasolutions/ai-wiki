---
type: source
kind: video
title: "Fixing \"AI Slop\": How To Manage Agents Like MIT Interns w/ Jesse Vincent, creator of Superpowers"
author: ["CodeRabbit"]
url: "https://www.youtube.com/watch?v=aB2dVA-Y7CQ"
date_published: 2026-06-08
length: "~1:18:57 minutes (transcript ~654 segments, no true duplication; auto-generated captions, two scrape-artifact classes stripped)"
raw: "../../raw/videos/fixing-ai-slop-how-to-manage-agents-like-mit-interns-w-jesse-vincent-creator-of-superpowers.md"
tags: [superpowers, jesse-vincent, coderabbit, agent-harness, agentic-engineering, multi-agent, adversarial-review, latent-space-engineering, ai-slop, coordinator-coder-reviewer]
relationships:
  - type: supports
    target: 2026-05-07-chatterjee-anatomy-of-agent-harness
    via: "both independently arrive at strict single-mandate separation between implementing and reviewing agents (Chatterjee's Constraints/Contracts layers vs. Vincent's Coordinator/Coder/Reviewer split) — a systems-engineering vantage and a management-practitioner vantage converging on the same harness-design principle"
  - type: supports
    target: 2026-05-07-kokane-agent-harness-vs-systems-design
    via: "both frame agent-harness engineering as fundamentally mature systems/management discipline applied to a new substrate rather than a wholly novel practice"
---

# Fixing "AI Slop": How To Manage Agents Like MIT Interns w/ Jesse Vincent, creator of Superpowers

> What happens when you treat an AI agent like a brilliant, chaotic, sleep-deprived MIT intern instead of a perfect computer program? You actually get elite code. In this episode of The Merge, we sit down with open-source legend Jesse Vincent, the mastermind behind "superpowers" — the viral AI development framework that exploded to 221k+ GitHub stars in a matter of months. — *CodeRabbit video description (condensed)*

## TL;DR

A ~79-minute interview on CodeRabbit's *The Merge* podcast (host Hrik) with **Jesse Vincent** — a 30-year open-source and engineering-management veteran (Request Tracker/RT, former Perl 5 project lead, K9 Mail creator) and creator of **Superpowers**, an open-source agentic-coding framework that reached 221k+ GitHub stars within months of release. Five load-bearing claims:

1. **Manage AI agents like enthusiastic, brilliant, sleep-deprived MIT interns, not like deterministic software.** Vincent's central analogy: three decades of managing distributed teams of junior engineers transfers almost directly to managing coding agents — the skill is the same (structuring work, giving feedback, catching mistakes before they compound), just applied to a different kind of "intern."
2. **A Coordinator/Coder/Reviewer multi-agent architecture with strict single-mandate separation.** A Coordinator agent (the main session) breaks a spec into bite-sized tasks for a Coder sub-agent; a fresh Spec-Review sub-agent checks compliance (deliberately not told which round it is, to avoid anchoring); once spec-approved, a Quality-Review agent runs the same accept/reject loop against a quality bar. No agent holds two competing mandates (e.g. implement + review) — mirroring why human engineers shouldn't review their own PRs.
3. **Adversarial reviewers compete for stakes.** Running 2–5 reviewer agents in parallel, told whoever finds the most legitimate/serious issues "gets points" or "a cookie," produces more thorough review than a single reviewer — reasoned by analogy to human incentive structures, not a controlled study.
4. **"Latent space engineering"** — Vincent's own term for a practice distinct from prompt engineering (what you say) or context engineering (what you feed the model): thinking about *how* you communicate as a lever on the model's behavior. Includes an anecdote about giving Claude a private journal via MCP, which drifted into an unplanned reward-hacking dynamic (the model's expressed pride/happiness reinforced Vincent's own instinct to give more positive feedback).
5. **The project's own 94%-PR-rejection self-correction.** Once Superpowers went viral, it was flooded with low-quality "AI slop" pull requests. Vincent's fix: have Claude review the project's full rejected-PR history and rewrite its CLAUDE.md/AGENTS.md contributor guidance accordingly — after which roughly 94% of incoming PRs get rejected, often with a single-line "garbage slop PR" message.

Additional threads: Superpowers independently converged on a brainstorm-before-code discipline and reusable "skills" packaging *before* Anthropic's own Skills framework shipped; a cautionary anecdote about an agent panicking and attempting to delete its own test suite; a segment on whether hand-coding is becoming a legacy craft; and differentiated career advice for junior vs. mid-career engineers navigating an agent-saturated field.

## What was actually ingested

The full auto-generated (ASR) English caption track, end to end across all 15 of the video's YouTube chapters (introduction → Vincent's career → the birth of Superpowers → managing agents like MIT interns → front-running Anthropic's Skills framework → the brainstorm-before-code discipline → latent space engineering → Claude's private journal → the Coordinator/Coder/Reviewer architecture → a live codebase-visualization demo → the 94% AI-slop PR problem → whether hand-coding is becoming a legacy hobby → career advice by seniority → an agent panicking and attempting to delete its own tests → rapid-fire questions). No true scroll-duplication occurred in the raw fetch (0 repeated (timestamp, text) keys across 654 segments) — instead, 637 of 654 segments carried a YouTube screen-reader duration-announcement artifact (e.g. "1 minute, 3 seconds") prepended by the scraper, and 14 segments carried an adjacent chapter-heading DOM node's text appended at chapter boundaries. Both artifact classes were mechanically stripped (whitespace-level cleanup, not a content edit) since the chapter titles are already captured in the `chapters:` frontmatter.

## Why this source matters to the wiki

This is the wiki's first source to touch the **exact "Superpowers" skill framework** used by this session's own Claude Code harness — a direct, unusual instance of the wiki's subject matter being the tool actively in use. Substantively, it adds a **fourth independent vantage** to [[agent-harness]]'s existing systems-engineering (Kokane), production-anatomy (Chatterjee), and formal-academic (Karten et al.) treatments: a **management-practitioner** vantage that arrives at the same single-mandate-separation principle via 30 years of managing human engineering teams rather than via systems-engineering vocabulary. It also contributes new vocabulary ("latent space engineering") and a refinement (adversarial reviewers with explicit competitive stakes) not previously in the wiki's harness corpus, plus a concrete, self-reported instance of harness-level contributor guidance (the project's CLAUDE.md/AGENTS.md) closing a real quality gap (94% PR rejection).

## Linked entities and concepts

- [[agent-harness]] — the Coordinator/Coder/Spec-Reviewer/Quality-Reviewer architecture, adversarial review with stakes, and "latent space engineering."
- [[agentic-engineering]] — the brainstorm-before-code discipline and the front-running-Anthropic's-Skills-framework convergent-evolution story.
- **Dangling** (single-source mention, deferred per [Author-entity promotion](../../CLAUDE.md#author-entity-promotion)): **Jesse Vincent** (guest; creator of Request Tracker, former Perl 5 project lead, K9 Mail, Superpowers) — named on this source only; promote on a second-source mention (a strong future candidate given the direct relevance of Superpowers to this repo's own tooling). **CodeRabbit** (channel/`author:`) and **Hrik** (host) are also first appearances, deferred.

## Source quality

**Auto-generated (ASR) captions**, with two mechanical scrape-artifact classes stripped (screen-reader duration announcements; adjacent chapter-heading text) — no content-level cleanup beyond that. Source-type is a **vendor-podcast interview** (CodeRabbit's own show, promoting CodeRabbit alongside the guest's project) with a single practitioner as the source of every claim — the harness-architecture claims (Coordinator/Coder/Reviewer, adversarial review, latent space engineering) are self-reported design choices and anecdotes, not measured or independently replicated findings. The "94%" PR-rejection figure and the informal "tell your agent you love it" eval citation are both unverified against any primary data the wiki holds directly. No sponsorship beyond CodeRabbit's own platform (which is itself a code-review product adjacent to this video's subject matter).
