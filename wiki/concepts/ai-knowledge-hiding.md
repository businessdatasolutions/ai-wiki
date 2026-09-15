---
type: concept
aliases: ["AI knowledge hiding", "ai-knowledge-hiding", "AI knowledge hoarding", "suppression of solutions", "hidden AI use", "shadow AI knowledge hiding"]
tags: [ai-knowledge-hiding, shadow-ai, organizational-trust, psychological-safety, enterprise-ai, disclosure-culture, knowledge-management, micro-productivity-trap]
confidence: 0.75
last_confirmed: "2026-09-15"
accessed_at: "2026-09-15"
source_count: 2
relationships:
  - type: instance-of
    target: enterprise-ai-adoption
    via: "a named human-factor failure mode of adoption — individually-discovered AI workflows stay private, so collective productivity gains never materialize even when individual adoption is high"
  - type: supports
    target: micro-productivity-trap
    via: "supplies the individual-level mechanism behind the trap: when efficiency gains are 'taxed' (saved time refilled with more work) and disclosure threatens standing, employees rationally hide their best workflows, so task-level gains never aggregate to firm-level value"
quality_score: 0.87
quality_notes: ['citation density 1.8/1000 words (2 source links in 1128 words; target ≥3.0)']
---

# AI Knowledge Hiding

**AI knowledge hiding** ([[2026-06-10-anicich-brouwers-why-employees-arent-transparent-ai-usage|Anicich & Brouwers, HBR 2026]]) is the deliberate withholding — by employees — of the AI workflows, prompts, and techniques they discover through private experimentation. The authors frame it as **"the suppression of solutions"**: where the classic organizational-silence literature studied the hiding of *problems* (bad news, risks, ethical concerns), AI introduces the hiding of *solutions*.

## Why it is newly consequential

Productivity gains "used to scale by default" — embedded in shared systems, standardized processes, and formal tools that spread improvements structurally. With AI, the most valuable gains come from **individual experimentation**: a prompt sequence that produces client-ready output in a fraction of the time. That knowledge is **portable, easy to refine in private, and easy to keep to yourself**. When an individually-discovered workflow cuts a three-hour task to twenty minutes and is trivial to conceal, silence becomes economically consequential in a way it was not before. This is why AI knowledge hiding is a distinct failure mode of [[enterprise-ai-adoption]] rather than a restatement of generic knowledge hoarding: high *individual* adoption can coexist with near-zero *collective* capability gain.

## The empirical claim: trust, not governance

The headline finding is that the binding driver is **organizational trust**, working largely *through* **psychological safety** — not formal AI policy or approved tooling.

- KPMG / University of Melbourne (48,000+ respondents): **57% admit hiding their AI use** at work.
- Anicich & Brouwers' own survey (604 daily-AI users): **30.3%** intentionally withheld AI knowledge; the lowest-trust quartile was **~4× more likely to hide** than the highest (**47% vs 14%**); psychological safety showed the same gap (**45% vs 17%**).
- Trust survived controls for job insecurity, internal competition, distributive fairness, AI policy, sanctioned tools, age, gender, tenure, and job level. **Having an AI policy or approved tools, on its own, predicted nothing.** Trust mattered *more* where a shared sanctioned toolset existed ("trust creates the willingness to share; a common toolset creates the opportunity").
- Corroboration: a 104-study meta-analysis (~31,800 employees) links psychological safety to less knowledge hiding, and abusive supervision / mistreatment / job insecurity to more; a Stanford 51-deployment study found **77% of the hardest adoption challenges were non-technical**.

## The three rational costs of disclosure

Employees make a rational calculation about the cost of making their AI workflows visible:

1. **Reputational** — being judged as less capable, or having the work discredited ("a computer did it").
2. **Workload** — efficiency treated as spare capacity to fill: *"if I automate A and B, they make me do D, E, F."* This is the [[micro-productivity-trap]] at the individual level.
3. **Replaceability** — enterprise tools log prompts and workflows, so a method can be extracted and routed to a cheaper replacement; hence the (perverse) advice to use *personal* AI tools so learning "stays with you."

Underlying all three is **Amy Edmondson's** distinction: organizations confuse *praiseworthy exploratory testing* with *blameworthy deviance*, and so punish exactly the experimentation they need.

## What leaders can do (the source's prescriptions)

Earn the disclosure you want (remove ambiguity; lightweight demos over process memos; credit the contributor); **stop taxing efficiency gains** (an explicit norm for reinvesting saved time); reward **multiplier** behavior (credit for *adopted* workflows; team incentives + pro-sharing norms, since comparison-heavy climates amplify retaliatory hiding); **legitimize experimentation, then surface it** (Anthropic's Claude Code "side quests" ≈ 3M 15% / Google 20% time); treat disclosure as a contribution (the manager's 30-second reaction is the decisive trust signal; don't turn one demo into a standing obligation). A standing **tooling warning**: the same logging that lets you *credit* a discovery also lets you *extract* it.

## Debates and supersession

- **Is this distinct from classic knowledge hoarding?** The novel claim is the *suppression of solutions* (not problems) plus the *portability/concealability* of AI workflows that makes silence newly costly. Single-source so far; the supporting meta-analysis is about knowledge hiding in general, not AI specifically.
- **Single-source caveat.** Rests on one HBR article (with its own 604-respondent survey + cited studies). Confidence at the single-source floor pending independent corroboration.

## Related concepts

- [[enterprise-ai-adoption]] — hiding is why high individual adoption need not yield firm-level gains; trust/culture is the binding constraint, not tooling.
- [[micro-productivity-trap]] — the workload "tax" is the shared mechanism; hiding is the individual-level response that keeps task gains from aggregating.
- [[durable-skills]] / [[ai-deskilling]] — the replaceability fear (your logged method becomes someone else's, or an automation's).
- [[responsible-ai]] — the surveillance/credit-vs-extract trade-off in sanctioned-tool logging.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "ai-knowledge-hiding")
SORT file.name ASC
```

## Open questions

- Does the trust→disclosure finding replicate outside the U.S. / outside knowledge work?
- Do "side quests" and multiplier-reward schemes measurably raise *disclosed* (not just total) AI productivity?
- How does mandatory enterprise-tool logging net out — does the credit mechanism or the extraction fear dominate as trust varies?

## The formal mechanism (added 2026-09-15)

This page rested on a single survey source, which located the driver in **organisational trust working through psychological safety**. [[2026-01-20-yuan-aseri-ramasubbu-backfiring-ai-deployment-workplace|Yuan, Aseri & Ramasubbu (2026)]] derive the same behaviour from **compensation structure alone**, with no trust deficit required — and that is a materially different diagnosis with a different remedy.

Their game-theoretic model splits employees on two independent dimensions: **tangible skill**, which an AI system can observe, codify and redistribute, and **intangible skill** (communication, coordination), which it cannot. Under **pay-for-performance rank-order competition**, deploying an AI that learns from the high performers erodes exactly the advantage those performers are paid for. Output and welfare fall for the high-tangible/low-intangible group; low-tangible employees rise; **firm profit can fall.**

Read against this page, the implication is uncomfortable: **hiding is rational even in a high-trust organisation**, provided rewards are relative. An employee who discovers a workflow that triples their output, working under PFP, is not being paranoid when they keep it — disclosure is the mechanism by which their rank is competed away.

Two consequences worth carrying:

- **The prescriptions on this page are incomplete.** Trust-building and psychological safety address the disclosure *cost* the survey identified; they do not touch the rank-order incentive. A firm could do everything Anicich & Brouwers recommend and still get hiding, if it pays on a curve.
- **The proposed remedy is counter-intuitive and untested.** Yuan et al. find that *guaranteeing* the wages of disadvantaged employees can leave the firm **worse off** than doing nothing, and that the profit-maximising move is to bound AI capability deliberately — *"pursuing the most advanced AI system is not always optimal."*

Treat this as mechanism, not evidence: it is an unrefereed analytical model with no data, and its load-bearing assumption (AI transfers hard skill but not soft) is asserted rather than shown. But it is the first source in the corpus that explains hiding without appealing to culture.
