---
type: source
kind: video
title: "The New Way To Build A Startup"
author: ["Y Combinator"]
url: "https://www.youtube.com/watch?v=rWUWfj_PqmM"
date_published: 2026-02-14
date_ingested: 2026-09-28
length: "~7:51 minutes (transcript ~208 segments; auto-generated captions, ASR-cleaned)"
raw: "../../raw/videos/the-new-way-to-build-a-startup.md"
tags: [y-combinator, garry-tan, main-function, 20x-company, compound-startup, internal-automation, lean-teams, gigaml, legion-health, phaseshift, claude-code, headcount, science-technology]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
relationships:
  - type: supports
    target: 2026-08-14-blomfield-yc-building-structuring-ai-native-company
    via: "both concern structuring a startup around AI across all internal functions, drawing on YC portfolio companies"
    confidence: 0.8
  - type: supports
    target: 2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up
    via: "both concern building a company with AI in every internal workflow from the start"
    confidence: 0.75
  - type: supports
    target: 2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer
    via: "same presenter on the same theme: small teams made far more productive by AI"
    confidence: 0.75
---

# Tan / Y Combinator — The New Way To Build A Startup

> In the AI era, startups aren't winning by hiring faster — they're winning by automating as many internal functions as possible. In this episode of Main Function, Garry breaks down how tiny teams are beating companies 20x their size by building automations into every workflow, from engineering to ops to customer support.

## TL;DR

An eight-minute episode of *Main Function* on the [[Y Combinator]] channel, presented by [[Garry Tan]]. It opens with an Anthropic engineer's post that Claude wrote Claude Cowork and that each developer manages *"anywhere between three and eight Claude instances"*, and generalises from it: *"the best teams aren't automating one or two internal functions. They're automating all of them."*

Tan names these **"20x companies"**, a term he credits to the founders of GigaML, and presents it as an evolution of Parker Conrad's **"compound startup"** (Rippling): Conrad's idea applied to internal automation instead of product breadth. Automating code, support, marketing, sales, hiring and QA *"allows them to postpone hiring additional sales and ops staff for much longer, keeping payroll down and culture from drifting."*

Three patterns, each from a YC company:

1. **An AI teammate — GigaML's Atlas.** GigaML builds voice agents for enterprise customer service. It won DoorDash with *"approximately like four to five engineers going against players who had like 100x engineers."* Its internal agent Atlas *"can use browsers, it can edit the policies, it can write code"*. Engineers say their scope *"doubled or tripled"*, and the company runs pilots with 10+ Fortune 500 firms with *"only a single human FTE"* on the customer side.
2. **One source of truth — Legion Health.** An AI-native psychiatry network built a single internal interface over patient history, scheduling, insurance codes and messages. *"We've grown 4x in the past year, but we haven't hired a single net new person"*: one clinical lead, one patient-support person and one billing person, where *"in a typical healthcare company, those are all departments."*
3. **A custom agent per employee — Phaseshift.** A 12-person accounts-receivable automation company asks staff to write down their manual tasks, then builds quick agents for them. It has *"avoided hiring a design person"* by using Magic Patterns for front-end design.

Tan's close: the three *"aren't mutually exclusive"*, and *"this is the new way to build."*

## Dynamic-capabilities reading

- **`digital-transforming/redesigning-internal-structures`** — the episode is about building the company's internal functions (support, ops, billing, design) as agents and interfaces instead of departments, and about the headcount structure that results.

## How it connects

- [[2026-08-14-blomfield-yc-building-structuring-ai-native-company|Tom Blomfield's Startup School talk]] covers the same ground from YC six months later, with a much stronger caveat (*"no one knows how to do this"*). [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Diana Hu's episode]] is the earlier YC version of the same theme.
- [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan's Stanford CS153 lecture]] extends the claim to the single-founder "1000x engineer".
- Legion Health's flat headcount at 4x growth is the firm-level claim that [[concepts/ai-employment-effects|ai-employment-effects]] tracks against aggregate labour data. The "one AI teammate plus one human" pattern is a case for [[concepts/agent-fleet-management|agent-fleet-management]], and all three patterns are small-firm entries in [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]].

## What was actually ingested

The full 7:51 episode from auto-generated English captions with background music. Cleaned for names: Claude Cowork, Rippling and Zenefits, DoorDash, GigaML's Atlas, Magic Patterns. "Phaseshift" is spelled as heard.

## Linked entities and concepts

- Entities: [[Y Combinator]], [[Garry Tan]], [[Anthropic]], [[Claude Code]]
- Concepts: [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]], [[concepts/ai-employment-effects|ai-employment-effects]], [[concepts/agent-fleet-management|agent-fleet-management]]
- **Dangling** (single-source mention, deferred): Parker Conrad, GigaML, Legion Health, Phaseshift

## Scope and reliability

**YC promoting its own portfolio.** All three companies are YC-funded, and each founder is quoted in a cut-together clip, not interviewed. The figures (4x growth, one FTE, 12 people vs. competitors with hundreds) are the founders' own, with no revenue or headcount data behind them. "20x" is a slogan from a sales win, not a measured productivity ratio. The episode is useful as a list of three internal-automation patterns and a vocabulary ("20x company"), not as evidence that the patterns produce the growth.
