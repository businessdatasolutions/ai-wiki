---
type: source
kind: video
title: "Spec-Driven Development: The Discipline Behind Reliable AI Coding"
author: ["deepsense"]
publisher: "deepsense.ai (YouTube channel *deepsense*, Tech Experts Webinar series); speaker Paweł Kmiecik, Senior Staff ML Engineer"
url: "https://www.youtube.com/watch?v=Gv4hd49lI4E"
date_published: 2026-05-26
date_ingested: 2026-09-19
length: "~18:12 minutes (auto-generated ASR transcript, cleaned; 375 segments across the channel's 6 chapters; slides not captured)"
raw: "../../raw/videos/spec-driven-development-the-discipline-behind-reliable-ai-coding.md"
tags: [deepsense, pawel-kmiecik, spec-driven-development, sdd, vibe-coding, spec-first, spec-anchored, spec-as-source, spec-kit, kiro, openspec, ears, gherkin, rfc-2119, constitution, project-memory-bank, spec-drift, brownfield, waterfall, intent-fidelity, context-survival, review-shift, coding-agents, tech-webinar]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: 2026-05-11-nystrom-how-i-ai-spec-driven-development-notion
    via: "Notion's agent-specs folder is the spec-anchored mode Kmiecik describes, running in a product codebase: specs committed alongside code, changes made to the spec and the code regenerated. Nystrom's practice of having Codex format a dictated idea against the existing spec library is also Kmiecik's advice to author specs together with the assistant rather than by hand"
    confidence: 0.85
  - type: contradicts
    target: 2026-03-23-wu-an-yc-momentic-qa-layer-ai-coding-era
    via: "on whether spec-as-source works yet. Wu presents it as the direction of travel: 'the spec is the source of truth. Your code is just an implementation of that source of truth.' Kmiecik names the same position spec-as-source, calls it 'still something aspirational — it doesn't work yet', and says most dedicated tools sit at spec-anchored. They agree on the destination and disagree on whether anyone has arrived"
    confidence: 0.75
  - type: supports
    target: 2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering
    via: "Ivers names under-specification as the practice AI amplifies most: given a loose requirement the model 'would decide what corner cases worth handling'. Kmiecik starts from the same point — any 'please implement' prompt is already a specification, 'just a really low quality' one — and his remedy is the formal requirement languages (EARS, Gherkin, RFC 2119) Ivers's audience would recognise"
    confidence: 0.8
  - type: supports
    target: 2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer
    via: "Forsgren and Macvean: 'the Specs, combined with the agent rules and skills, are the source of truth for what and the why of the system.' Kmiecik's project memory bank (Spec Kit's constitution) is that combination as a tool feature, with a warning they do not give — that anything in it which makes no difference is 'only a noise in the context'"
    confidence: 0.75
  - type: contradicts
    target: 2026-05-08-running-an-ai-native-engineering-org
    via: "on whether the written artefact survives. Anthropic's Claude Code team took design documents out and put prototypes in; Kmiecik makes the written spec the thing a human reviews before any code is generated, and the thing the team shares with product owners and new hires. The same disagreement Notion's account has with Anthropic's, from a third team"
    confidence: 0.7
  - type: supports
    target: 2026-07-06-google-cloud-agent-factory-intent-driven-development
    via: "Kmiecik's closing claim — 'we no longer type code but we describe the intent… more precisely' — is the intent-driven development YK Sugi names in that episode, and Lydia Hallie's Claude Design wireframe (plan, prompt and acceptance criterion in one file) is a spec in everything but format. Kmiecik supplies what the Agent Factory episode lacks: a vocabulary for how durable the spec is meant to be"
    confidence: 0.7
---

# Kmiecik (deepsense.ai) — Spec-Driven Development: The Discipline Behind Reliable AI Coding

> In this Tech Experts Webinar, Paweł Kmiecik, Senior Staff ML Engineer, explains how specification-driven development (SDD) helps teams build more reliable software with AI coding agents. The webinar focuses on the practical limitations of "vibe coding" and shows how structured specifications improve consistency, maintainability, and long-term development workflows. The session also compares dedicated SDD tools, lightweight methodologies, and agent-native approaches for specification-driven engineering.
>
> *— Channel description, deepsense*

## TL;DR

An 18-minute practitioner talk by Paweł Kmiecik, a senior staff ML engineer at deepsense.ai, a Polish AI consultancy. It is short and plain, and its value to the wiki is that it gives [[spec-driven-development]] a structure the corpus did not have. Several sources already use the term; none defined its variants or set out its costs. This talk does both, and its arrival is why the concept now has its own page.

Four things it contributes:

1. **A three-level taxonomy of how long the spec lives.** Spec-first (written for one task, then discarded), spec-anchored (kept in the repository and synchronised with the code), and spec-as-source (only the spec is maintained; code is treated like a compiled binary). Most teams do the first. Most tools sit at the second. The third *"is still something aspirational — it doesn't work yet."*
2. **A workflow that is the same across tools under different names.** Specify, plan, tasks, implement, following GitHub's Spec Kit. Kiro and OpenSpec differ *"mainly about the names but the fundamentals keep the same."*
3. **An honest list of drawbacks**, which is rarer than the benefits: markdown files multiply and all need review; workflows are not standardised and some tools have already been abandoned; **spec drift**, because *"non-deterministic LLMs can ignore what… our tools are telling them"*; most tools are poor on brownfield code; and it is partly waterfall.
4. **One diagnosis of vibe coding that the corpus can reuse:** *"the AI did exactly what it was asked to, but what it was asked kept changing over time."*

No measurements. The one empirical claim — that vibe coding makes code quality *"worse and worse"* at scale — cites unnamed studies.

## The problem it starts from

Kmiecik opens with a line that sums up the argument: *"teams produce code faster but they create software slower."* He quotes [[Andrej Karpathy]]'s 2023 remark that *"the hottest new programming language is English"*, then qualifies it: English has become the most common language for programming, *"but we shouldn't forget that it's not replacing the software development. So the hard part, like deciding what to build, what done looks like, it's still there."*

On [[vibe-coding]] he is not dismissive. It is *"a great tool for quick prototypes, some scripts and fast PoCs"*, but *"it breaks down at scale."* He places the fault in usage, not tools: *"this is not the problem with AI tools that we use but this is the problem how we use them."* The diagnosis is that the specification was never fixed. The model did what it was told each time, and what it was told drifted.

## What counts as a specification

His definition is deliberately broad: *"any 'please implement' prompt you write down to your AI agent or AI assistant is some kind of a specification — just a really low quality one."* The question is therefore not whether to specify but how precisely and how durably. [[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering|Ivers (SEI)]] makes the same point from the other side: given a loose requirement, the model *"would decide what corner cases worth handling, what weren't"*. A vague prompt does not leave the spec unwritten; it leaves the model to write it.

For precision, he points to existing formal requirement languages, familiar from behaviour-driven development:

- **EARS** (Easy Approach to Requirements Syntax)
- **Gherkin** (Given / When / Then)
- **RFC 2119** (the MUST / SHOULD / MAY keywords)

For durability, the taxonomy:

| Level | What happens to the spec | Status, per Kmiecik |
| --- | --- | --- |
| **Spec-first** | Written to perform one task, then thrown away; never committed | What most teams do |
| **Spec-anchored** | Committed alongside the code; the two are kept in sync | Where most dedicated tools sit |
| **Spec-as-source** | Only the spec is maintained; generated code is treated *"like compiled binaries"* | *"Still something aspirational… it doesn't work yet"* |

He does not say where the taxonomy comes from. It matches the three levels Birgitta Böckeler set out on martinfowler.com in October 2025 in her comparison of Kiro, Spec Kit and Tessl. That attribution comes from outside the corpus and has not been checked against a source page here.

## The workflow

Using GitHub Spec Kit's names:

1. **Constitution** — a project-wide memory bank applied to every feature, *"similar to AGENTS.md or CLAUDE.md but something more powerful, because it's built into the given tool. So the enforcement is higher."* Tech-stack preferences, security rules and whatever else matters most go here.
2. **Specify** — the tool turns an informal request into a formal spec. **This is the step to review by hand**, because *"based on the specification it will just create or generate the plan and implementation for you."*
3. **Plan** — the spec is broken into research, API contracts and similar parts.
4. **Tasks** — the plan is broken into single tasks, which some tools run in parallel.
5. **Implement** — ordinary code generation, with the earlier artefacts injected into context and enforced by the tool.

He spends almost no time on step 5: *"it's just generation. So it will take like 20 minutes to give you a working feature."* His point is that the effort moves up the list. *"Your job here shifts from typing the code to reviewing the code… we don't have for now an approach that fully replaces a human being from that part."*

His closing summary puts the same shift in terms of intent: *"the bottleneck moved. We no longer type code but we describe the intent… more precisely, then the results are better."* That is the intent-driven development YK Sugi names in [[2026-07-06-google-cloud-agent-factory-intent-driven-development|Google Cloud's Agent Factory episode]], where Lydia Hallie also uses a Claude Design wireframe as plan, prompt and acceptance test at once. That episode does not say how long the spec should live. Kmiecik's taxonomy does: a wireframe handed over once and not kept is spec-first.

The claim that a tool's built-in memory is enforced more strongly than an `AGENTS.md` file is asserted, not shown. It is relevant to [[agent-harness]], where the question of how reliably a harness applies its context is open.

## Tools, grouped rather than ranked

He declines to review individual tools and sorts them into three groups instead:

- **Dedicated SDD platforms** — Spec Kit (GitHub), Kiro, OpenSpec.
- **Lightweight frameworks and methodologies** — *"more like manifests"* for how to use an assistant.
- **Agent-native, do-it-yourself** — specs written into a `docs` folder and referenced from `AGENTS.md`, or workflows built from Claude skills. Enough *"in many cases, maybe the simpler ones."*

His one recommendation is **OpenSpec**, *"the most flexible for now, because you can start even in the middle of your project"* — a brownfield argument.

## Benefits and costs

| Benefits | Costs |
| --- | --- |
| **Intent fidelity** — the intent exists as an artefact you can review and show to others | **Markdown sprawl** — *"the number of markdown files grows really fast"*, and every one needs review |
| **Context survives** sessions, because the spec is committed | **No standard** — tools differ, and *"I've observed some tools that were not developed anymore"* |
| **Team alignment** — new hires and outsiders can read what is being built | **Spec drift** — even precise specs are ignored by non-deterministic models, and code and spec diverge |
| **Cheap pivots** — change the spec, regenerate | **Greenfield bias** — most tools are *"not so good in brownfield projects"*; some will not start mid-project |

**Is it waterfall?** He answers yes, partly — requirements, then planning, then implementation — *"but the iteration loop is much faster. So it's not taking a year… we can measure it in minutes or hours."* That is an honest answer, and it moves the question to whether a fast waterfall keeps the costs waterfall was criticised for. He does not address that.

## Practice recommendations

1. **Do not use SDD for trivial tasks**, except to learn a tool.
2. **Audit the constitution.** It is the tool form of what [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren and Macvean]] call "the Specs, combined with the agent rules and skills" — the source of truth for what the system is and why. Check what is in it and whether each item changes the output; *"if you put there some things that don't make a change, then it's only a noise in the context."* This is the maintenance tax on context files the wiki has recorded for [[agentic-engineering|skill files]], applied to the spec layer.
3. **Write specs by hand first**, in Gherkin or RFC 2119 style, to build the skill needed to review the ones the AI produces.
4. **Once competent, stop editing specs by hand.** Edit them in conversation with the assistant, *"because… it can find some more ambiguities than you will find."*
5. **Always review spec, plan and tasks before implementation**, or *"the code generated might be just a trash sometimes and you will just waste time and tokens."*
6. **Show the spec to a product owner or manager** to check it is readable by a non-engineer, since *"specifications were meant to close the gap between the business and the engineering."*

Points 3 and 4 are in tension on purpose, and the sequence is the useful part: learn to write specs so that you can judge the ones you then stop writing.

## Dynamic capabilities (Warner & Wäger)

- **`digital-seizing/rapid-prototyping`** — the talk draws a boundary around prototyping practice. Vibe coding is endorsed for *"quick prototypes, some scripts and fast PoCs"* and rejected for production, and SDD is offered as what replaces it when a prototype needs to become a product.
- **`digital-transforming/improving-digital-maturity`** — the talk is a maturity step for an engineering team already using AI tools: from throwaway prompts (spec-first) to committed, reviewed specs (spec-anchored), learned in stages — start small, write specs by hand, then adopt a tool.

## Linked entities and concepts

- Concepts: [[spec-driven-development]], [[vibe-coding]], [[agentic-engineering]], [[agent-harness]], [[software-3.0]]
- Entities: [[Andrej Karpathy]], [[GitHub]] (Spec Kit)
- **Dangling** (single-source mention, deferred): Paweł Kmiecik, deepsense.ai, Kiro, OpenSpec, Spec Kit, Birgitta Böckeler

## Scope and reliability

**A short vendor-adjacent talk with no data.** deepsense.ai sells AI engineering services, and the webinar is part of its marketing, though no product is promoted and no tool is sold. Kmiecik speaks from his own use of the tools; nothing is measured. The claim that vibe coding degrades quality at scale refers to *"some examinations"* that are not named.

**The slides are missing.** The talk is built around them: the spec examples at 6:49 (*"what you see on the left… on the right"*), the workflow diagrams of Kiro and OpenSpec, and the tool groupings are described but not shown. What is recorded here is what was said.

**Transcript:** auto-generated only. The speaker's name and employer were garbled (*"Pavo Kitik"*, *"Dibson's AI"*) and are corrected from the channel description. Tool names (*"Cairo"* for Kiro, *"opensp spec"* for OpenSpec) and requirement languages (*"ears"*, *"gerkin"*) were corrected from context. One verb at 8:39 remains uncertain. All corrections are listed in the raw file's `notes:`.

## Debates and supersession

- **Spec-as-source: here now, or not yet?** [[2026-03-23-wu-an-yc-momentic-qa-layer-ai-coding-era|Wu (Momentic)]] describes it as the direction the field is taking; Kmiecik says it does not work yet. They agree on the destination. Recorded as `contradicts` above.
- **Does the written artefact survive?** [[2026-05-08-running-an-ai-native-engineering-org|Anthropic's Claude Code team]] replaced design documents with prototypes. Kmiecik and [[2026-05-11-nystrom-how-i-ai-spec-driven-development-notion|Nystrom (Notion)]] make the document the reviewed input. Three teams, two answers.
- **Spec drift is conceded, not solved.** Kmiecik states that models ignore specs and code diverges from them, and offers no remedy beyond review. If drift is common, spec-anchored degrades towards spec-first over time. The corpus has no measurement of how often it happens.
- **Open: what does SDD cost in review time?** The case for SDD is that reviewing a spec is cheaper than reviewing the code it produces. Kmiecik also says the markdown multiplies and all of it needs review. Nobody in the corpus has measured whether the total review burden goes down.
