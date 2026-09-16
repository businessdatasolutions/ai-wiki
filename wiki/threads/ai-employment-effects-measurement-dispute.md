---
type: thread
status: open
opened: 2026-09-16
tags: [ai-employment-effects, measurement, methodology, entry-level, labor-economics, cross-source-comparison, identification-strategy]
---

# Thread: Why do credible measurements of AI's employment effect disagree by an order of magnitude?

## The question

Two well-resourced empirical shops have looked for AI's effect on employment and reported findings that are hard to reconcile. **Brynjolfsson and co-authors**, from ADP payroll microdata, report a **13% decline** in employment for workers aged 22–26 in the most AI-exposed occupations, growing to *"16 or 17%"* by August 2026. **Jan Hatzius and Goldman's Global Investment Research**, looking across occupations, report that *"the correlation is quite small. And in many cases we don't find anything"* — with an economy-wide magnitude of **10,000–15,000 jobs per month**.

Both are credible. Both are recent. **Is this a genuine empirical disagreement, or are they measuring different things and being read as if they were measuring the same thing?**

This thread exists because [[ai-employment-effects]] is the wiki's largest concept page and it now carries three positions on this question without a way to adjudicate between them. The concept page records the disagreement; this thread is where the work of resolving it belongs.

## Why it matters

Nearly everything downstream in the corpus depends on which reading is right:

- If the Brynjolfsson reading holds, the entry-level rung is being removed now, and [[durable-skills]], [[2026-07-22-brown-wef-meet-the-leader-entry-level-jobs-in-an-ai-era|the apprenticeship-pipeline argument]] and the [[micro-productivity-trap]] prescriptions are urgent.
- If the Hatzius reading holds, the labour-market story is a decade-scale adjustment comparable to ordinary technological change, and the current alarm is mostly narrative — which is roughly what [[ai-washing]] predicts we should expect to see.
- The policy and curriculum consequences differ completely, and this is the question the user's teaching work most directly touches.

## The three positions currently in the wiki

| | [[2026-04-28-brynjolfsson-canaries-coal-mine\|Canaries]] / [[2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity\|Brynjolfsson]] | [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs\|Hatzius / Goldman]] | [[2026-07-22-brown-wef-meet-the-leader-entry-level-jobs-in-an-ai-era\|Brown / WEF–PwC]] |
| --- | --- | --- | --- |
| **Finding** | 13% → 16–17% decline, ages 22–26, most-exposed occupations | Correlation *"quite small"*; often nothing. 10–15k jobs/month | Dire headlines *"not backed up by evidence and data"*; some employers hiring 25% more juniors |
| **Unit** | Age cohort **within** exposure quintile | Occupation-level aggregate | Employer intentions |
| **Data** | ADP payroll microdata, monthly, 3.5–5M workers | **Unstated** | WEF–PwC employer survey |
| **Nets out AI-driven job creation?** | No | **Yes** (data-centre construction cited) | N/A |
| **Method published?** | **Yes**, in a paper | **No** | Report not ingested |
| **Direction** | Effect is real and growing | Effect is small or absent | Effect is overstated |

## The leading hypothesis

**These are not contradictory findings; they are findings at different levels of aggregation, and the disagreement may dissolve under decomposition.**

An effect concentrated in one narrow cohort (22–26) inside one slice of the distribution (the top exposure quintile) can be simultaneously:

- large and statistically robust *within that cell*, and
- invisible in an occupation-level aggregate, because the cell is small relative to the occupation, and because Hatzius explicitly nets the loss against AI-driven job creation elsewhere (data-centre construction) while Canaries does not.

If that is right, **both numbers are correct and the dispute is about which question you asked.** *"Is AI removing entry-level jobs in exposed occupations?"* and *"Is AI moving the aggregate employment level?"* have different answers, and conflating them produces the appearance of a fight.

**Nothing currently in the corpus tests this.** It is the most plausible reconciliation, not an established one.

## A complicating third factor

[[2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai|Sundararajan]] adds a confound that neither measurement separates out: COVID-era remote restructuring independently lowered the return on junior hires, on the same timeline. *"It's one thing if you're in the organization 5 days a week absorbing from these senior people. It's another if you're in strategically two or three days a week."*

This matters for the identification strategy specifically: **AI-exposed occupations are disproportionately the ones that went remote.** An occupation-exposure design that compares exposed against less-exposed occupations may be partly picking up an attendance effect rather than an automation effect. Sundararajan does not claim this defeats the payroll finding, and neither does this thread — but no source in the corpus separates the two.

## What would resolve this

In rough order of how decisive each would be:

1. **The Goldman methodology.** Hatzius states results without showing any method — no data source, no specification, no sample. If GIR has published the underlying note, ingesting it would let the two designs be compared directly instead of compared through an interview. **This is the single highest-value acquisition for this thread.**
2. **A replication of Canaries at the occupation level.** Does the Brynjolfsson effect survive aggregation from the 22–26 cell to whole occupations? If the authors or anyone else has run this, it tests the leading hypothesis directly.
3. **A source that nets job creation the same way on both sides.** Hatzius offsets against data-centre construction; Canaries does not offset at all. A like-for-like comparison would isolate how much of the gap is the offset.
4. **Anything separating the remote-work confound from the AI confound.** A design exploiting variation in return-to-office policy within exposure level would do it. Nothing in the corpus attempts this.
5. **Non-US evidence.** Both measurements are US. [[2026-06-01-lf-state-of-tech-talent-europe-2026|The Linux Foundation's European survey]] and [[2026-06-25-raboresearch-ai-it-zakelijke-dienstverlening|RaboResearch's Netherlands sectoral work]] are in the corpus and use different instruments again; whether the disagreement replicates outside the US is untested.

## How this thread should resolve

Into a **synthesis page** if items 1 or 2 arrive and the decomposition hypothesis can be confirmed or rejected. The synthesis would state: what each design measures, at what unit, with what offsets, and under what conditions each number is the right one to quote.

If the evidence does not arrive, the thread stays open. **It should not be closed by picking the more congenial number**, which is the specific failure mode it exists to prevent — the corpus currently leans sceptical (Hatzius, Brown, [[2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity|Frey]]) and the one source with a published method points the other way.

## Related pages

- [[ai-employment-effects]] — the concept page carrying all three positions.
- [[ai-washing]] — the attribution-confound layer; relevant if the sceptical reading holds.
- [[automation-vs-augmentation]] — Hatzius's 25%-of-tasks decomposition (most exposure returns as time saved, 6–7% as elimination) is the augmentation reading of the same data.
- [[durable-skills]] — what the answer implies for what to teach.
- [[ai-maturity-measurement-comparison]] — the corpus's other open thread about instruments disagreeing; the same methodological lesson may apply to both.
