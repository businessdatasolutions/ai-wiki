---
type: entity
kind: product
aliases: ["Devin", "Devin AI"]
tags: [devin, cognition, cloud-agent, coding-agent, playbooks, devin-review, isolated-workspace, fresh-vm, agentic-pr]
affiliation: "Cognition"
role: "Cloud-hosted autonomous software engineering agent"
confidence: 0.75
last_confirmed: "2026-08-30"
accessed_at: "2026-08-30"
source_count: 3
relationships:
  - type: part-of
    target: Cognition
    via: "Devin is Cognition's product"
  - type: instance-of
    target: agent-harness
    via: "a commercial harness — cloud runtime, tools, session isolation, review product and a reusable-procedure layer around a frontier model"
---

# Devin

**Cognition's cloud-hosted autonomous software engineering agent**, and the substrate under the corpus's most detailed practitioner account of running many agents at once.

## The properties that matter to this wiki

**A fresh VM per session.** Devin runs in the cloud with an isolated workspace per session rather than on the developer's machine. This is the property practitioners cite as load-bearing: concurrent agents cannot collide in a shared working tree, which is what makes 10–15 parallel sessions possible at all. [[2026-03-23-geng-neubig-caid-asynchronous-software-engineering-agents|CAID]] isolates the same primitive — *isolated workspaces* — as one of three coordination mechanisms and measures its contribution experimentally. Practice arrived first; the controlled evidence followed.

**Playbooks.** A reusable, shareable prompt that steers Devin through a repeated multi-step workflow with a defined procedure and success criteria — effectively a custom system prompt for a recurring task. Sections a playbook can carry include **Procedure**, **Specifications** (postconditions: what should be true when done), **Advice**, **Forbidden Actions** and **Required from User**. Invoked by selecting from a Team or Community library, by attaching a `<name>.devin.md` file, or via an assigned macro (e.g. `!data-tutorial`). Cognition's guidance is to iterate them — running a playbook surfaces places the instructions can be tightened.

Two of those section names — **Advice** and **Forbidden Actions** — line up precisely with what [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes]] concludes agents need from 306 hand-coded rejected PRs: hints about the approach to follow, and explicit statements of approaches not to take.

**Devin Review.** A first-party PR review product distinct from the coding session, which [[Ryan Carson]]'s Land PR playbook triggers with up to two review loops before recording a narrated video walkthrough with a red/green test list.

## Where it shows up in the evidence

Devin is one of the five agents in the [[2026-02-09-li-aidev-studying-ai-coding-agents-on-github|AIDev]] dataset (932,791 agent-authored PRs across 116,211 repositories), and one of the four whose fixes are **rejected 46.41% of the time** in [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes]]. It is also the tool [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Carson]] uses for non-coding work — deal desk, quoting, operations documentation, customer triage — on the framing *"what would you do with somebody who both knew your code base and could write code to solve anything in your business?"*

Practitioner limits noted on the record: Devin is described as *"terrible"* at design work, and its video-verification feature is reported as unreliable by at least one heavy user.

Structurally, Devin is a commercial [[agent-harness|agent harness]] — cloud runtime, tool surface, session isolation, a review product and a reusable-procedure layer wrapped around a frontier model — and it is [[Cognition]]'s single product, so the two pages carry the vendor and the artifact respectively.

## Appears in this wiki via

- [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder]] · [[2026-07-25-darroman-profitable-founder-managing-ai-agents-25-prs-a-day]] · [[2026-02-09-li-aidev-studying-ai-coding-agents-on-github]] · [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes]]

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "devin")
SORT file.name ASC
```
