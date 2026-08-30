---
type: entity
kind: organization
aliases: ["Cognition", "Cognition Labs", "Cognition AI"]
tags: [cognition, devin, cloud-agents, coding-agents, playbooks, devin-review, agent-vendor]
affiliation: "Independent AI company"
role: "Builder of Devin, a cloud-hosted autonomous software engineering agent"
confidence: 0.7
last_confirmed: "2026-08-30"
accessed_at: "2026-08-30"
source_count: 3
relationships:
  - type: part-of
    target: Devin
    via: "Cognition is the vendor; Devin is the product"
---

# Cognition

The AI company behind **[[Devin]]**, the cloud-hosted autonomous software engineering agent. Cognition matters to this wiki mainly through Devin's presence in two places: as the substrate under the corpus's most detailed practitioner account of [[concepts/agent-fleet-management|agent fleet management]], and as one of the five agents tracked in the [[2026-02-09-li-aidev-studying-ai-coding-agents-on-github|AIDev]] population dataset.

Two product decisions are load-bearing for the arguments in this corpus:

- **Cloud-first with a fresh VM per session.** This is the workspace-isolation property that makes concurrent agents possible without collisions — validated independently as a coordination primitive in [[2026-03-23-geng-neubig-caid-asynchronous-software-engineering-agents|CAID]] and cited by practitioners as the reason to work in the cloud at all.
- **Playbooks and a first-party review product.** Playbooks are reusable prompts for recurring workflows; **Devin Review** is a separate PR-review product inside Devin that [[Ryan Carson]]'s Land PR loop triggers, with up to two review iterations before a narrated video walkthrough.

Cognition granted Carson roughly $20,000/month in credits after he publicised his spend — a commercial detail worth remembering when reading his cost figures, since they are not what an unsponsored buyer pays.

## Appears in this wiki via

- [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder]] — Devin as the primary cloud agent, with playbooks, folders and Devin Review shown on screen.
- [[2026-07-25-darroman-profitable-founder-managing-ai-agents-25-prs-a-day]] — Devin among the independent platforms Carson expects to survive on production-oriented model economics.
- [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes]] — Devin among the four agents whose fixes are rejected 46.41% of the time at population scale.

Vendor documentation snapshot at `raw/articles/2026-08-30-cognition-devin-playbooks-and-cloud-agents.md`, captured 30 August 2026. **Deep links into Cognition's docs move — re-resolve before citing.**

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "cognition")
SORT file.name ASC
```
