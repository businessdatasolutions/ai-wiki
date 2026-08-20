---
type: entity
kind: person
aliases: ["Tom Blomfield", "Blomfield"]
tags: [tom-blomfield, y-combinator, monzo, gocardless, ai-native-company, self-improving-loops, company-brain, burn-tokens-not-headcount, legibility, quality-gates, startup-school]
affiliation: "[[Y Combinator]] (General Partner)"
role: "General Partner at Y Combinator; previously co-founder of Monzo and GoCardless"
confidence: 0.72
last_confirmed: "2026-08-20"
accessed_at: "2026-08-20"
source_count: 2
relationships:
  - type: part-of
    target: Y Combinator
    via: "General Partner; speaks at Startup School and on the YC Root Access channel"
  - type: authored-by
    target: 2026-08-14-blomfield-yc-building-structuring-ai-native-company
    via: "sole speaker; the talk is his own research framing rather than an interview"
---

# Tom Blomfield

General Partner at **[[Y Combinator]]**; previously co-founder of the UK banks **Monzo** and **GoCardless**. Within this wiki he is the author of the corpus's most structural statement of the **AI-native company** thesis — the argument that the hierarchical org chart is an artifact of humans having been the information-routing mechanism, and that AI removes the constraint the hierarchy was built to solve.

## The argument, in his own terms

From [[2026-08-14-blomfield-yc-building-structuring-ai-native-company|*Building And Structuring An AI Native Company*]] (Startup School Paris, August 2026):

- **The historical premise.** The Roman legion's *contubernium*-to-century hierarchy existed so that *"they would pass information down and receive reports up, and a human being was responsible for being that conduit the whole way. And bizarrely, like 2,000 years later, we're still basically running the same kind of thing."* Credited to a [[Andrej Karpathy|Karpathy]] tweet and a Jack Dorsey tweet.
- **The diagnosis of the common failure.** Most deployments cap out because *"you as a human are like the gating mechanism. So while you are asleep, the thing can't work"* — which yields 20–30% productivity gains and nothing structural.
- **The unit of analysis he proposes instead: the loop.** Five parts — signal in (telemetry, tickets, billing, code changes) → policy layer → tool layer → quality gate → learning mechanism. *"If you can do this entire loop without a human, your product starts improving itself when you're sleeping."*
- **The contrarian position on quality gates.** The gate *"could be a human, and I'd argue **probably should not be a human** in all but the most extreme cases. The quality gate can often be a second adversarial LLM."* This is a live disagreement with the human-in-the-loop default most of the corpus assumes; see the source page and [[concepts/agent-harness|agent-harness]].
- **Hill climbing as the reduction.** *"All this is is hill climbing… computer systems are really really good at this kind of hill climbing work because they never stop."*
- **Company brain.** Borrowing Dorsey's phrasing: *"in a conventional company, intelligence is spread throughout the people and the hierarchy routes it. In this new model, intelligence lives in the system."* Humans relocate to the edge — sales calls, client reassurance, ethical and existential-stakes judgement — *"but the humans are no longer necessary to do the information routing."*
- **Four prescriptions.** Burn tokens, not headcount. No middle management; ICs who *"come to meetings with working prototypes, not decks"*, plus a DRI whose *"head is on the block."* Make everything legible to AI — transcribe every meeting, ban Slack DMs, *"every action needs to create an artifact… otherwise it basically didn't happen to the AI."* On-demand internal software for all operations.

## The caveat he attaches, and why it should travel with the citations

He opens with it and it is stronger than the genre requires: *"no one knows how to do this. And so this is very theoretical. It's based on hundreds of YC companies that we're working with right now… if anyone tells you they've got it all figured out, they are probably lying."* Nothing in the talk is measured, no failure mode is described, and the evidence base is early-stage, greenfield, self-selected companies advised by his own firm.

## Appears in this wiki via

- [[2026-08-14-blomfield-yc-building-structuring-ai-native-company|*Building And Structuring An AI Native Company*]] (Startup School Paris / YC Root Access, 14 August 2026) — his own talk; the source above.
- [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|Garg / YC Root Access, May 2026]] — named as a prior speaker in the same multi-talk agent-harness session (*"as Pete and Tom and Gary mentioned"*), on the *thin harness* point. This first mention is what flagged him for promotion under the [author-entity promotion rule](../../CLAUDE.md#author-entity-promotion).

## Concepts he contributes to

- [[concepts/ai-agents|ai-agents]] — the five-part AI loop; the AI-employee-with-a-VM construction.
- [[concepts/agent-harness|agent-harness]] — the quality-gate-as-adversarial-LLM position and the policy layer.
- [[concepts/automation-vs-augmentation|automation-vs-augmentation]] — the explicit case for moving past augmentation to closed-loop automation with humans relocated rather than assisted.
- [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] — the human-as-gating-mechanism diagnosis.
- [[concepts/knowledge-graphs|knowledge-graphs]] — company brain, and the SOP-versus-actual-practice gap as the codification problem.

## Open questions

- The **earlier version of this talk** — Blomfield says on camera that this is an update of one given *"about a month, maybe six weeks ago"*, separately on YouTube. Worth locating and diffing: he says he *"added some thoughts"*, and knowing which parts are new would date the claims more precisely.
- His **Monzo and GoCardless** operating experience surfaces only once in the talk (the anti-committee aside: *"I worked at a bank and we had so many committees for everything"*). A source where he applies the loop thesis to a regulated incumbent rather than to early-stage startups would be a much stronger test of it.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "tom-blomfield")
SORT file.name ASC
```
