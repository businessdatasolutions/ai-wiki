---
type: concept
title: Spec-driven development
aliases: ["spec-driven development", "Spec-driven development", "specification-driven development", "SDD", "spec-first development", "spec-anchored development", "spec-as-source", "truth-driven development", "agent specs"]
tags: [spec-driven-development, sdd, specifications, spec-first, spec-anchored, spec-as-source, spec-kit, kiro, openspec, ears, gherkin, rfc-2119, constitution, spec-drift, under-specification, intent, vibe-coding, agentic-engineering, coding-agents, review-shift]
confidence: 0.75
last_confirmed: "2026-09-19"
accessed_at: "2026-09-19"
source_count: 6
relationships:
  - type: part-of
    target: agentic-engineering
    via: "the practice by which agentic engineering fixes what the agent is building before it builds it; agentic-engineering holds the discipline as a whole, this page holds its specification half"
  - type: uses
    target: agent-harness
    via: "dedicated SDD tools inject the spec, plan and project-wide rules into the agent's context and enforce them, which is harness work. Kmiecik calls the tool 'a given spec-driven development harness'"
  - type: contradicts
    target: 2026-05-08-running-an-ai-native-engineering-org
    via: "Anthropic's Claude Code team replaced design documents with prototypes. SDD keeps the document and makes it the reviewed input to the agent"
    confidence: 0.7
quality_score: 0.99
quality_notes: ['1 near-empty section(s)']
---

# Spec-driven development

## Working definition

A way of working with coding agents in which **a written specification, not the prompt history and not the code, fixes what is being built.** The spec is written (usually with the agent's help), reviewed by a human, and then used as the agent's input for planning and implementation. Its purpose is to stop the failure [[2026-05-26-kmiecik-deepsense-spec-driven-development-reliable-ai-coding|Kmiecik]] describes in one sentence about [[vibe-coding]]: *"the AI did exactly what it was asked to, but what it was asked kept changing over time."*

The starting observation is that every prompt is already a specification. *"Any 'please implement' prompt… is some kind of a specification — just a really low quality one."* What SDD changes is how precise the spec is and how long it lasts.

The page opened on 2026-09-19. The term had appeared in the corpus since late 2025 — as *truth-driven development* in a YC interview, as Notion's working practice, as one item in O'Reilly's 2026 vocabulary list, and as part of AWS's Kiro pitch — but without definitions or costs. Kmiecik's talk supplied both, and six sources now carry the concept substantively.

## Key claims

### 1. Specs differ by how long they live

The one taxonomy in the corpus comes from [[2026-05-26-kmiecik-deepsense-spec-driven-development-reliable-ai-coding|Kmiecik (deepsense.ai, May 2026)]]:

| Level | What happens to the spec | Where the corpus finds it |
| --- | --- | --- |
| **Spec-first** | Written for one task, then discarded | What most teams do (Kmiecik). A Claude Design wireframe handed to Claude Code once ([[2026-07-06-google-cloud-agent-factory-intent-driven-development\|Hallie, Agent Factory]]) is spec-first |
| **Spec-anchored** | Committed next to the code and kept in sync | Where most tools sit (Kmiecik); Notion's `agent-specs` folder ([[2026-05-11-nystrom-how-i-ai-spec-driven-development-notion\|Nystrom]]) |
| **Spec-as-source** | Only the spec is maintained; code is treated like a compiled binary | Wu's stated direction ([[2026-03-23-wu-an-yc-momentic-qa-layer-ai-coding-era\|Momentic]]); *"still something aspirational… it doesn't work yet"* (Kmiecik) |

The taxonomy appears to originate with Birgitta Böckeler (martinfowler.com, October 2025), which Kmiecik does not cite and the corpus does not hold. Treat that attribution as unverified here.

### 2. AI makes vague specs more costly, not less

Two sources arrive at this independently. [[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering|Ivers (SEI / Carnegie Mellon)]], asked which bad practice AI amplifies most, names under-specification: given a loose requirement, the model *"would decide what corner cases worth handling, what weren't, what I really meant by that requirement. Terrible idea."* [[2026-03-23-wu-an-yc-momentic-qa-layer-ai-coding-era|Wu (Momentic)]] reaches the same place from a testing product: *"the spec is the source of truth. Your code is just an implementation of that source of truth."*

A vague prompt does not leave the spec unwritten. It leaves the model to write it, without review.

### 3. The spec travels with rules and skills

The spec for one feature sits inside a project-wide layer. [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren and Macvean (Google, 2026)]]: *"Goals, Constraints, Rationale become critical context… The Specs, combined with the agent rules and skills, are the source of truth for what and the why of the system you are building."* Dedicated tools make that layer a feature — GitHub Spec Kit's *constitution*, a *"project memory bank"* applied to every feature. Kmiecik claims its enforcement is stronger than an `AGENTS.md` file's *"because it's built into the given tool"*. That claim is unmeasured and bears on an open question in [[agent-harness]]: how reliably a harness applies the context it is given.

### 4. The workflow is stable across tools

Specify → plan → tasks → implement, in Spec Kit's names; Kiro and OpenSpec differ *"mainly about the names"* (Kmiecik). Notion's version is the same shape with fewer steps: dictate an idea, have Codex format it against the existing spec library, revise it, then tell Codex to *"build it"* ([[2026-05-11-nystrom-how-i-ai-spec-driven-development-notion|Nystrom]]). The step every source stresses is the human review of the spec before any code exists.

### 5. The review moves upstream

Every source puts the human effort before generation rather than after it. Kmiecik: *"your job here shifts from typing the code to reviewing the code"*, and the spec is the part to check by hand, because the plan and code are generated from it. Nystrom: *"if the verification's a little hazy, that's the first thing you should be going and doing."* Claire Vo, on the same episode, says the design document was always written; what agents remove is the wait for review.

This is the same shift [[agentic-engineering]] records as the *review inversion*, with one difference: SDD tries to move part of the review from code to spec, where it is cheaper. Whether the total review burden goes down is not measured anywhere in the corpus (see Debates).

### 6. The costs are known and mostly unsolved

From Kmiecik, the only source that lists them:

- **Markdown sprawl** — spec, plan and task files multiply, and all need review.
- **No standard** — tools differ and some have already been abandoned.
- **Spec drift** — *"non-deterministic LLMs can ignore what… our tools are telling them"*, so code and spec diverge.
- **Greenfield bias** — most tools handle brownfield code badly. OpenSpec is his recommendation because it can start mid-project.
- **Partial waterfall** — requirements, then plan, then build, defended on the grounds that the loop takes *"minutes or hours"*, not a year.

## When it is and is not the right tool

Kmiecik's boundary matches the one [[vibe-coding]] already draws. Vibe coding is *"a great tool for quick prototypes, some scripts and fast PoCs"* and *"breaks down at scale."* SDD is for work that will be maintained, and is wasted on trivial tasks. His learning sequence is also a useful rule: write a few specs by hand in a formal style (EARS, Gherkin, RFC 2119) to learn to judge them, then stop editing by hand and refine them in conversation with the assistant, *"because it can find some more ambiguities than you will find."*

## Debates and supersession

- **Does the written artefact survive?** [[2026-05-08-running-an-ai-native-engineering-org|Anthropic's Claude Code team]] replaced design documents with prototypes. Notion and Kmiecik make the document the reviewed input. The two positions may fit different work — a prototype answers "is this the right thing?", a spec answers "is this built as intended?" — but no source argues that. Recorded as `contradicts`.
- **Spec-as-source: here, or not yet?** Wu presents it as where the field is going; Kmiecik says it does not work yet and places the tools at spec-anchored. Nobody in the corpus reports running spec-as-source in production.
- **Spec drift is conceded, not solved.** If models often ignore the spec, spec-anchored decays toward spec-first as code and document diverge. No source measures drift rates or offers a mechanism beyond review.
- **Does SDD reduce review, or move it?** The case rests on spec review being cheaper than code review. Kmiecik also reports that the reviewable markdown grows fast. No source measures total review time with and without SDD.
- **Confidence is held at 0.75.** Six sources agree that the practice exists and roughly what it looks like, and one is institutional (SEI). None measures an outcome: every benefit reported — one-shot builds, cheap pivots, context that survives sessions — is self-reported by a practitioner or vendor. The schema caps vendor and anecdotal support at 0.75 without independent replication, and there is also an open contradiction (above). A study comparing defect or rework rates with and without committed specs would move it.

## Related concepts

- [[agentic-engineering]] — the discipline SDD sits inside; holds the review inversion and the maintenance tax on skill files.
- [[vibe-coding]] — the mode SDD is defined against, and which it accepts for prototypes.
- [[agent-harness]] — where the spec and project rules are injected and enforced.
- [[software-3.0]] — spec-as-source is Software 3.0 taken literally: the natural-language document becomes the program and the code becomes its compiled output.
- [[ai-generated-code-quality]] — what spec review is meant to prevent downstream.

## Sources consulted

- [[2026-05-26-kmiecik-deepsense-spec-driven-development-reliable-ai-coding]] — the taxonomy, the workflow, the tooling groups, the costs and the practice recommendations.
- [[2026-05-11-nystrom-how-i-ai-spec-driven-development-notion]] — spec-anchored SDD in a large product codebase: `agent-specs`, spec as changelog, verification section.
- [[2026-03-23-wu-an-yc-momentic-qa-layer-ai-coding-era]] — *truth-driven development*; the spec-as-source thesis from a testing vendor.
- [[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering]] — under-specification as the practice AI amplifies most.
- [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer]] — specs plus rules plus skills as the source of truth for what and why.
- [[2026-07-06-google-cloud-agent-factory-intent-driven-development]] — intent-driven development and a design wireframe used as spec, prompt and acceptance test.

Mentioned without substance, not counted: [[2026-01-09-baron-signals-for-2026|Baron / O'Reilly]] lists *eval- and spec-driven development* in its 2026 vocabulary, and [[2025-12-02-allen-brozovich-davis-aws-reinvent-advanced-team-structures|AWS re:Invent]] names Kiro alongside it.
