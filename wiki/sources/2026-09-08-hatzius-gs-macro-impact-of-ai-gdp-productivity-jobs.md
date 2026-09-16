---
type: source
kind: video
title: "How AI is Affecting GDP Growth, Productivity, and Jobs"
author: ["Goldman Sachs"]
url: "https://www.youtube.com/watch?v=rrUQl_AoV3U"
date_published: 2026-09-08
date_recorded: 2026-08-13
date_ingested: 2026-09-16
length: "~17:46 minutes (publisher transcript PDF, 52 speaker turns; no caption track exists)"
raw: "../../raw/videos/how-ai-is-affecting-gdp-growth-productivity-and-jobs.md"
tags: [jan-hatzius, sharmin-mossavar-rahmani, goldman-sachs, investment-strategy-group, global-investment-research, macroeconomics, gdp-growth, ai-capex, measurement-error, intermediate-inputs, adoption-survey, census-bureau, labor-productivity, task-exposure, unemployment, david-autor, railway-boom]
dynamic_capabilities:
  - contextual/external-triggers
  - digital-transforming/improving-digital-maturity
relationships:
  - type: contradicts
    target: 2026-04-28-brynjolfsson-canaries-coal-mine
    via: "both measure the relationship between occupational AI exposure and employment, and report different magnitudes. Canaries, from ADP payroll microdata: employment for workers aged 22-26 in the most AI-exposed occupations down ~13% at first measurement. Hatzius, from correlations across occupations: 'the correlation is quite small. And in many cases we don't find anything', with an economy-wide magnitude of 'maybe 10,000 jobs a month, 15,000 jobs a month'. The comparison differs in unit (age-cohort within exposure quintile versus occupation-level aggregate) and in whether an offset for AI-driven job creation is netted out"
    confidence: 0.75
  - type: contradicts
    target: 2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity
    via: "the same disagreement as above, restated: Brynjolfsson reports the entry-level effect growing over time ('up to 16 or 17%'), Hatzius reports no large effect anywhere in the occupation-level data as of August 2026"
    confidence: 0.75
  - type: supports
    target: 2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity
    via: "both state that AI's measured macroeconomic effect to date is small. Frey argues from the gap between rising inventive output and flat transformational output; Hatzius quantifies the GDP-growth contribution at about a tenth of a percentage point and attributes part of the headline discrepancy to national-accounts treatment"
    confidence: 0.7
  - type: supports
    target: 2026-05-21-jones-stanford-gsb-ai-and-our-economic-future
    via: "both model AI's productivity effect as slow-diffusing. Jones supplies the weak-links argument for why benefits arrive slowly; Hatzius supplies a diffusion estimate — a ~15% level uplift relative to a no-AI world, spread over roughly a decade"
    confidence: 0.7
  - type: supports
    target: 2026-08-18-covello-gs-new-models-ai-investment-landscape
    via: "companion interviews in the same Goldman Sachs Private Wealth series with the same interviewer; Hatzius cites Covello by name for the C-suite-versus-worker expectations exhibit. Hatzius covers the macro aggregates, Covello the value chain"
    confidence: 0.85
---

# How AI is Affecting GDP Growth, Productivity, and Jobs

> The transition to an AI-driven economy represents a multi-decade structural shift rather than an overnight revolution. Sharmin Mossavar-Rahmani, chief investment officer of Wealth Management and head of the Investment Strategy Group (ISG), and Jan Hatzius, chief economist and head of Global Investment Research, cut through the noise to deliver a data-driven reality check on AI's impact on US economic growth, productivity, and the labor market. They uncover why investors may need to balance near-term hype with long-term potential and argue that the US unemployment rate should remain stable over the next decade as AI creates new jobs to offset displacement.
>
> Recorded on August 13, 2026.

## TL;DR

A ~18-minute **Goldman Sachs** Private Wealth Management interview, **recorded 13 August 2026** and published 8 September. **Sharmin Mossavar-Rahmani** — CIO of Wealth Management and head of the **Investment Strategy Group** — interviews **Jan Hatzius**, Goldman's chief economist and head of **Global Investment Research**.

This is the corpus's **first macroeconomic-aggregate treatment of AI from a sell-side chief economist**, and its function here is as a *deflator*. Almost every claim is a downward revision of a widely circulated number.

1. **AI investment contributes about a tenth of a percentage point to US GDP growth — not a full point, and not half the total.** The correction is the interview's headline: *"There is a contribution from AI investment to GDP growth, but it is much smaller than the one percentage point or half of the total that people have sometimes argued."* Put concretely against the ~2% headline: *"So without that it would be 1.9%. So these are not big numbers."*

2. **Two reasons, and the second is an accounting artifact rather than an economic fact.**
   - **Imports net it out.** *"A lot of the equipment that is used in AI investment is imported. So it contributes a lot to Taiwanese GDP or Korean GDP… But an imported semiconductor or server does not show up in the US GDP. It shows up as investment, but it also shows up as imports and therefore gets basically taken out."*
   - **Semiconductors are not counted as final goods at all.** *"Semiconductors actually don't show up in US GDP because they're treated as intermediate inputs as opposed to final goods. **That's a measurement error.** But it does mean that it does not show up in the 2% or so US GDP growth numbers that we've been seeing."* He calls it an error and still works within it — the number a reader sees in the national accounts is understated for a knowable reason.

   He is explicit that none of this diminishes the technology: *"That doesn't mean AI is not important. We do think that there is a significant impact on productivity growth down the road. But at the moment, AI investment is not the driving force of US GDP growth."* What is driving it: *"a lot of other, maybe more prosaic things like consumer spending and investment and equipment and intellectual property."*

3. **Why the CapEx numbers in circulation disagree — three methods, none clean.** (a) **Hyperscaler CapEx** — *"probably the most popular approach, but you have to adjust for the fact that the hyperscalers always did capital spending, even pre-GPT moment,"* and it misses smaller investors. (b) **Ecosystem revenues** — *"you have to be careful about double counting, because one company might be selling to another company, which then sells to the final consumer."* (c) **National income and product accounts** — *"a little bit open to debate as well, what should be incorporated and what shouldn't."* Goldman triangulates: **~$600 billion in the US, ~$1 trillion globally.**

4. **The $5–7 trillion-by-2030 headline is not unprecedented once you normalise it.** Two adjustments: relate it to the size of the economy, and look at annual rather than cumulative spend. *"The peak level of AI investment in a particular year as a share of GDP… somewhere in the two and a half to 3% range… for maybe 2027, 2028. And that would be within the range of past technological revolutions. In fact, **the railway booms of the 19th century were at the high end of that range** — towards 5% of GDP, although that, of course, was in a dramatically smaller economy."* On why "unprecedented" persists: *"it is unprecedented in nominal dollars. But then again, almost everything is unprecedented in nominal dollars in a growing economy."*

5. **The 10%→20% adoption jump is a survey-wording artifact, not a step change.** The Commerce Department survey *"originally asked, are you using AI for current production. Then they changed that. Are you using AI in any business function."* Production was the higher bar — *"you're using AI to produce goods and services, and you were only at 10% of companies saying that they did."* The new phrasing *"is a much lower bar because it might be relatively ancillary activity that are being captured by this."* Goldman's own estimate sits *"just over 20% if you look at all industries,"* with a wide sectoral spread.

6. **Productivity: a ~15% level uplift, diffusing over about a decade — before offsets.** *"Our estimate in terms of the impact on the level of productivity relative to what you would see in a world without AI is about 15%. And we expect that to basically diffuse and show up over about a decade. So that gives you something like a percentage point and a half of additional growth in productivity from AI."* The offsets he names are not usually in the frame: **CapEx crowd-out** (*"if they invest more in AI, they're probably going to invest less in other things that otherwise would have created significant productivity gains"*), **lower immigration**, and **slowing labour-force growth**. Net of all that, Goldman has still revised long-run US productivity and GDP growth up — *"we're now at about 2.3% from 1.75% prior to 2020 or 2022. And we think that number could rise somewhat further into the mid-twos or a little above."*

7. **On the C-suite/worker expectations gap, he declines to pick a side and reads it as incentives.** Asked why leadership reports large productivity effects while employees report few hours saved: *"workers have a bit of an incentive to underestimate the amount of help that they're getting, because after all, otherwise they're going to be asked to do more with these new tools. Whereas in the C-suite, perhaps there's a tendency to get more positive reports on the investments that firms have already undertaken. So it might be that the truth is somewhere in the middle."* The exhibit he is responding to is attributed to **Jim Covello** — the guest of [[2026-08-18-covello-gs-new-models-ai-investment-landscape|the companion interview]].

8. **Labour market: he reports finding very little, and says so plainly.** *"If we look at the correlation between AI adoption or AI exposure on the one hand, and then employment growth or unemployment rates across occupations on the other hand, **the correlation is quite small. And in many cases we don't find anything.** When you cut the numbers in a somewhat different way, sometimes you get some effect, but it's never big."* Magnitude: *"maybe something like 10,000 jobs a month, 15,000 jobs a month that are being lost to AI. But then there are also other sectors where data center construction, for example, where you're getting a boost to jobs. So I think at the moment we can say that this is not yet a huge deal in terms of the labor market impact."*

9. **The decomposition that makes the 25% figure readable.** *"Our 25% relates to work tasks. And you can think of it as work hours that are potentially exposed. That is obviously a big number, but **most of that number is accounted for by many people in the economy getting 20 or 30% of their time back**, and then being able to redeploy that time… But it doesn't lead to the elimination of a job. Now, there's also going to be some portion of that 25%, and we've said maybe 6 or 7, that is going to result in job elimination."* With the arithmetic guard attached: *"it doesn't mean that the unemployment rate rises by 6 or 7 percentage points, because for that you also need to look at how many jobs are being created."*

10. **Ten years out, his unemployment forecast is roughly where we are now.** He expects *"disruption, upward pressure on the unemployment rate, a half a percentage point or a percentage point"* offset by *"an increased pace of job creation."* The forecast: *"my best guess for the unemployment rate is that it's not going to be that different from where we are now, which is 4.1%."* His historical warrant is **David Autor's** finding that *"if you look at the jobs that are currently in existence, about 60% of them are in occupations that did not exist in 1940."*

11. **The scale comparison he closes on.** Asked whether the adjustment is gradual or a shock: *"In the average US recession, you get an increase in the unemployment rate by 2 or 3 percentage points. And in the deep recession, you've gotten a 5 or 6 percentage point increase… relative to that, my expectation would be that the upward pressure that we might see from AI is going to be probably smaller than that."*

## How this source touches the Warner & Wäger cells

- **`contextual/external-triggers`** — the whole interview treats AI as a macro-level external condition firms and policymakers respond to rather than choose: the investment wave (~2:45), the adoption curve (~7:46), and the labour-market adjustment (~12:35). The measurement argument is specifically about how badly that external trigger is read from the headline aggregates.
- **`digital-transforming/improving-digital-maturity`** — the adoption discussion (~7:18–9:15) is about how far firms have actually got, and the wording artifact is a direct caution about maturity self-reports: a survey that asks "any business function" rather than "current production" measures a different and much lower bar. Any maturity instrument built on self-reported adoption inherits that problem.

## Related in this wiki

- **The entry-level and exposure question.** [[2026-04-28-brynjolfsson-canaries-coal-mine]] and [[2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity]] measure employment by age cohort within occupation-exposure quintiles in ADP payroll records. This source reports occupation-level correlations between exposure and employment growth, and states an economy-wide monthly magnitude net of AI-driven job creation. [[ai-employment-effects]] holds both.
- **Productivity and its absence.** [[2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity]] and [[2026-05-21-jones-stanford-gsb-ai-and-our-economic-future]] address why measured productivity has not moved. This source supplies a diffusion estimate and a set of offsets.
- **The value chain beneath the aggregates.** [[2026-08-18-covello-gs-new-models-ai-investment-landscape]] is the companion interview and asks where the CapEx in claim 3 ends up.
- **Firm-level adoption.** [[2026-08-10-maza-a16z-kavak-rebuilding-a-company-around-ai]] is a single firm reporting figures far outside anything in this source's aggregates; [[enterprise-ai-adoption]] and [[micro-productivity-trap]] hold the reconciliation question.

## Linked entities and concepts

- Entities: [[Goldman Sachs]] (publisher and employer of both speakers).
- Concepts: [[ai-employment-effects]], [[automation-vs-augmentation]], [[enterprise-ai-adoption]], [[micro-productivity-trap]], [[warner-wager-process-model]].
- **Dangling** (single-source mention, deferred): **Jan Hatzius**, **Sharmin Mossavar-Rahmani**, **Jim Covello** (named here, guest of the companion source — promotes to an entity if a third source cites him), **David Autor** (cited for the 1940 statistic), **Investment Strategy Group**, **Global Investment Research**.

## Source quality

- **Transcript provenance is unusually good, and unusually fiddly.** Neither this video nor its companion carries **any caption track**, so the wiki's normal YouTube path cannot serve them. The text is **Goldman's own published transcript PDF**, converted with `pdftotext`. The PDF is co-located with the raw file and gitignored; `transcript_url` in the raw frontmatter records its origin.
- **The publisher's transcript still contained meaning-inverting errors.** Two were corrected at acquire time and are itemised in the raw file. The consequential one: *"the equipment that is used in AI investment is **important**"* should read *"is **imported**"* — and imported equipment netting out of US GDP is the entire mechanism of claim 2. **Publisher-issued is not the same as verified.**
- **The disclaimer and the speakers do not line up, and this matters for how the numbers are cited.** The video description states it *"represents the views of the Wealth Management Investment Strategy Group and is not a product of Goldman Sachs Global Investment Research (GIR). It is not research and is not intended as such."* But Hatzius **heads GIR**, and the figures he quotes — the 0.1pp contribution, $600bn/$1tn, the 15% productivity uplift, the 25%/6–7% task decomposition — are GIR estimates. So these are **research-derived numbers relayed in a format Goldman explicitly declines to stand behind as research**. Cite them as reported by Hatzius in an interview, not as published Goldman research; the underlying GIR notes have not been ingested and their methods are not examined here.
- **No methodology is shown.** Every estimate is stated, none is derived. The 15% productivity figure, the 25% task-exposure share and the 6–7% elimination share are the load-bearing numbers and all three arrive without a stated method, sample or definition.
- **Recorded four weeks before publication** (13 Aug vs 8 Sep 2026). Nothing in it is acutely time-sensitive, but the unemployment rate he quotes as current (4.1%) is as of mid-August.
- **Scope.** Full interview ingested, 0:00–17:25 of a 17:46 runtime.
