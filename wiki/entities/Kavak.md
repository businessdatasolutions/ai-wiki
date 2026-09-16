---
type: entity
kind: organization
aliases: ["Kavak", "Kavak.com"]
tags: [kavak, latin-america, mexico, used-car-marketplace, e-commerce, fintech, agentic-transformation, agent-per-customer, ai-native-company, vertical-integration]
since: 2016
confidence: 0.7
last_confirmed: "2026-09-16"
accessed_at: "2026-09-16"
source_count: 1
---

# Kavak

Latin American used-car marketplace, founded in Mexico. Its stated business is buying, refurbishing, selling and financing used cars — but because the supporting infrastructure did not exist regionally, it built the adjacent businesses itself: *"we also had to build a fintech and a logistics company and a Carfax, and basically all the infrastructure for this to work didn't exist in LatAm. So we had to build everything vertically."*

**Why the wiki holds it:** Kavak is the corpus's **first end-to-end account of a company that rebuilt itself around agents and reports operating figures**. Almost everything else here on enterprise adoption is survey data, vendor testimony, or framework. That makes this page valuable and also makes its single-source status worth stating plainly — see Open questions.

## Appears in this wiki via

- [[2026-08-10-maza-a16z-kavak-rebuilding-a-company-around-ai]] — **Alejandro Maza Ayala**, Chief Product & AI Officer, on the [[a16z]] Podcast (10 Aug 2026), interviewed by Angela Strange and Gabriel Vasquez. The full account of the transformation: three bets (redesign the company, build superhuman agents, change the metrics), the agent-per-customer architecture, the eval-resourcing rule, the AI-CEO experiment in Cuernavaca, the Jedi Academy, the token tiering, and the Schumpeter/Ford argument for why incumbents under-realise.

## What Kavak reports

All figures are **self-reported by one executive on a venture-capital podcast, unaudited, and without stated definitions or baselines.** Recorded here as claims:

| Measure | Reported |
| --- | --- |
| Customer interactions handled by agents | 96% |
| Transactions handled by agents | 95% |
| Agents instantiated per day | 100,000–200,000, each with its own VM |
| AI seller vs human team conversion | +50% initially, 2.1× at time of recording |
| NPS / customer satisfaction | tripled |
| Car-loan approval | under 3 minutes |
| AI "CEO" of Cuernavaca, first month | 1.5× profit against a 2× target |
| Warranty claims after mechanic sidekick | down ~26% |
| Customers in database | 10 million |
| Mechanics in Mexico | ~800 |

## The architecture, in brief

**One long-running agent per customer**, not per task — a virtual machine with memory, evals, a CLI, access to every internal tool and API, and a long-horizon goal of maximising that customer's lifetime value. Agents sleep and wake on their own schedule, running from minutes to days.

This replaced a working multi-agent system of *"tens of thousands"* of function-decomposed agents, discarded after the Opus 4.5 release on the view that decomposition now constrains rather than enables a sufficiently capable model. Kavak spends *"about the same amount of engineer time, tokens, and money"* on evals as on agents.

**Humans remain where the physical world does** — ~800 mechanics, who work with a sidekick agent — and the escalation path is inverted: agents call an API for help and a human answers it, so *"if you map this out in an org chart, it's really human teams that have an agent."*

## Why it matters to the wiki's open questions

Kavak sits directly on the corpus's largest unresolved question. [[2026-08-18-covello-gs-new-models-ai-investment-landscape|Covello]] states that *"enterprises collectively are not making or saving money on their AI implementations"* and names the missing piece as a data-management plus model-orchestration layer. Kavak reports the opposite outcome and describes building something close to that layer. Whether Kavak is the exception that proves the aggregate, the leading edge of it, or a case whose numbers would not survive audit is **not settled by anything the wiki currently holds**. See [[micro-productivity-trap]] and [[enterprise-ai-adoption]].

## Open questions

- **Single source, and an interested one.** Everything on this page comes from one podcast episode produced by a venture firm. No filing, report, customer account, competitor view, or independent measurement corroborates any figure. A second source is the highest-value addition this page could get.
- **Financial position undisclosed.** The only profitability claim in the episode is that the *prior* architecture *"brought us to profitability"* — made about the system Kavak then discarded. Current economics are not discussed, and Kavak's funding history and valuation are outside what the wiki has ingested.
- **The 2.1× conversion figure has no stated baseline.** Against which human cohort, over what window, with what selection into agent-handled leads? Unstated, and the firm controls the funnel.
- **The AI-CEO result is one city over six weeks with no control.** Whether it survives a longer window or generalises beyond Cuernavaca is unknown.
- **Headcount effects are alluded to but not quantified.** The interviewer notes Kavak *"had to downsize dramatically"*; Maza does not give figures, and the episode does not return to it. Relevant to [[ai-employment-effects]].

## Related pages

- Concepts: [[agent-harness]], [[multi-agent-failure-modes]], [[agent-fleet-management]], [[agent-oversight-and-delegation]], [[micro-productivity-trap]], [[enterprise-ai-adoption]], [[automation-vs-augmentation]].
- Entities: [[a16z]] (publisher of the only source), [[Anthropic]] (Opus 4.5 triggered the re-architecture).
