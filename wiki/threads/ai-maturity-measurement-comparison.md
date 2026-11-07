---
type: thread
status: open
opened: 2026-04-28
tags: [ai-maturity, ai-adoption, methodology, cross-source-comparison]
---

# Thread: How do different sources measure AI maturity, and where do they agree or diverge?

## The question

Multiple authoritative sources are publishing **adoption** and **maturity** numbers for enterprise AI, using different instruments, samples, and definitions. Sometimes they appear to converge ("most orgs aren't really mature"); sometimes they appear to diverge (78% adoption vs. 7% Stage 4). Is there a coherent meta-story across these sources, or are they measuring fundamentally different things?

## What we know so far

### From [[2026-04-28-ai-index-report-2025|AI Index 2025]] (adoption from two McKinsey surveys in 2024; the 1% from a separate C-suite survey)

- **78% of orgs use AI** in at least one business function (vs. 55% in 2023).
- **71% of orgs use [[generative-ai|generative AI]]** in at least one function (vs. 33% in 2023).
- **Only 1% of C-suite executives describe their GenAI rollouts as "mature."**
- Most reported financial impact: cost savings <10%, revenue gains <5%.
- Methodology: McKinsey Global AI Survey instrument; "use" = at least one business function; "mature" = self-reported by C-suite.
- **Correction (2026-11-07).** The n=2,854 is the two 2024 State of AI surveys combined (February–March, n=1,363; July, n=1,491; AI Index 2025, PDF pp. 262, 441). The 78% comes from the July survey alone. The 1% comes from what the AI Index calls *"a complementary survey of C-suite executives in developed markets"* (PDF p. 266) and does not cite. It is most likely McKinsey's *Superagency in the workplace* (January 2025): *"just 1 percent believe they are at maturity"*, where mature means AI fully integrated into workflows and driving substantial business outcomes. That report could not be reached for this check; its sample (reported as 238 C-level executives and 3,613 employees) is secondary.

### From [[2026-04-28-mit-sloan-ai-maturity|MIT Sloan / MIT CISR]] (Future Ready Survey 2022, n=721, plus 2024 interviews at 9 enterprises)

- **Four-stage AI maturity distribution:** Stage 1 (Experiment) 28%, Stage 2 (Pilots) 34%, Stage 3 (Ways of working) 31%, **Stage 4 (Future-ready) 7%.**
- Stages 1–2 below industry-average financial performance; Stages 3–4 above.
- Maturity score = equally-weighted combination of three measures: AI effectiveness for (i) operations, (ii) customer experience, (iii) ecosystem support.
- **Greatest financial impact in moving Stage 2 → Stage 3.**

### Apparent convergence

| Question | AI Index (McKinsey) | MIT CISR | Convergence |
|---|---|---|---|
| Are most orgs "using AI"? | 78% (any function) | 100% (Stages 1–4 are *all* using AI in some sense) | Both say yes — high adoption breadth |
| Are most orgs *mature*? | 1% mature (C-suite self-report on GenAI) | 7% Stage 4 | Both say no — maturity is rare |
| Is there a clear value gradient? | Cost savings <10%, revenue <5% | Stages 1–2 below avg, Stages 3–4 above | Both say yes — but CISR locates the inflection (Stage 2→3) |

### Apparent divergence (or methodological)

- **Definition of "mature."** AI Index uses C-suite self-report on GenAI specifically. CISR uses a triangulated AI-effectiveness score across operations, CX, and ecosystem support — and mature is Stage 4, the top 7%. These are not the same metric.
- **Sample.** McKinsey's adoption figures: n=1,491 (July 2024; 2,854 across both 2024 surveys). The 1% comes from a separate C-suite sample, probably *Superagency*'s (not verified). CISR Future Ready n=721, **2022** — 2 years older. The 2022 baseline predates the GenAI explosion; current CISR distributions might look quite different.
- **Adoption granularity.** AI Index: binary (used in ≥1 function or not). CISR: 4 stages with explicit progression criteria. The CISR view is *richer* but the AI Index view is *more comparable across years*.

### Two more instruments (added 2026-04-28 batch)

#### From [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]] (the Cisco AI Readiness Index 2024, reprinted by MITTRI in 2025)

A **third measurement type** — *readiness and urgency*, distinct from adoption breadth or maturity stage:
- **13%** of companies globally are ready to leverage AI to its full potential.
- **68%** say their infrastructure is at best moderately ready.
- **98%** feel increased urgency over the past year.
- **85%** give themselves <18 months to deploy a strategy or face negative business effects.
- **50%** have already dedicated 10–30% of IT budget to AI.

These numbers are **complementary, not competing** with AI Index/CISR. They describe a **gap analysis** between what orgs are doing (high adoption, low maturity) and what they think they need to do (massive urgency, short deadlines, high IT spend). Caveat: Cisco's survey instrument; Cisco-favorable framing on "infrastructure readiness."

#### From [[2026-04-28-werner-lebrun-octopus-organization|Werner-Le-Brun]] (HBR Nov–Dec 2025)

A **broader org-change baseline**, not AI-specific:
- **Just 12% of transformation efforts** show sustainable performance gains, even after three years.
- Despite trillions in investment over the past 20 years.

This contextualizes the AI maturity numbers. If only 12% of *general* transformations succeed, then **CISR's 7% Stage 4 + AI Index's 1% mature is actually consistent with — possibly even worse than — the broader transformation-success baseline.** AI maturity may be even harder than general transformation, given the speed of capability change and the depth of org-redesign required. *Caveat (2026-11-07):* the 12% is not an AI measurement. It matches McKinsey's 2022 Global Implementation Survey, and its denominator is unclear (see [[2026-04-28-werner-lebrun-octopus-organization|the source page]]).

### Updated cross-walk (revised 2026-11-07)

| Source | What it measures | "Successful" % | Sample / instrument | Newest edition (checked 2026-11-07) |
|---|---|---|---|---|
| McKinsey *Superagency*, relayed by AI Index 2025 | GenAI rollout described as "mature" (C-suite self-report) | **1%** mature | C-level executives, Oct–Nov 2024 (secondary: 238 executives); not the 2,854 adoption sample | Not repeated: Chapter 4 of the [[2026-04-30-ai-index-report-2026\|AI Index 2026]] has no maturity figure. Nearest McKinsey measures: about 6% "AI high performers" and 7% of AI users "fully scaled" ([[2025-11-05-mckinsey-state-of-ai-2025\|State of AI 2025]]); the 2026 edition reportedly keeps 6% (secondary only) |
| MIT CISR | Stage 4 "AI future-ready": Total AI Effectiveness score of 100% | **7%** Stage 4 | Future Ready Survey 2022, N=721 | **18%** in 2025, same scoring rule, Real-Time Business Survey N=152 ([[2025-08-21-mit-cisr-grow-enterprise-ai-maturity\|August 2025 briefing]]) |
| Cisco AI Readiness Index | "Pacesetters": readiness score of 86+ on 49 indicators | **13%** | 7,985 leaders, 30 markets, Aug–Sep 2024 ([[2024-11-19-cisco-ai-readiness-index-2024\|2024 index]]); MITTRI reprinted it in 2025 | About 13% for the third year, now defined as outperforming peers on AI value ([[2025-10-14-cisco-ai-readiness-index-2025\|2025 index]]); Netherlands 7% in 2024 |
| Werner-Le-Brun (HBR 2025) | Transformations of any kind whose gains last more than three years | **12%** | McKinsey Global Implementation Survey 2022 (uncited in the article) | No newer edition; not an AI measure |
| MIT SMR–BCG (Ransbotham, Kiron) | "Augmented Learners": high on organisational and AI-specific learning | **15%** | 3,467 respondents, spring 2024 | Not repeated in the [[2025-11-18-ransbotham-kiron-mit-smr-bcg-emerging-agentic-enterprise\|ninth report]] (November 2025), which reports adoption only |

The four "success rate" numbers (1% / 7% / 12% / 13%) span a single order of magnitude despite radically different instruments — which is itself useful information: **whatever you call success, it's rare.**

*Revised 2026-11-07.* Of the five numbers that later formed this cross-walk (the 15% was added on [[enterprise-ai-adoption]]), only CISR has been re-measured with the same rule, and it moved from 7% to 18% on a much smaller sample. The 1% and the 15% were not repeated. Two of the five are not independent measurements of AI maturity: the 12% measures change programmes in general, and the MITTRI 13% is Cisco's own index reprinted. "Five independent studies, all at 1–15%" therefore no longer holds as stated. "Adoption is high, maturity is rare" still holds; see the next section.

### A different unit of analysis: the individual worker (added 2026-08-31)

Every instrument above measures the **firm**. [[2026-08-31-blum-how-i-ai-claude-cowork-pm-system|Blum / How I AI (Aug 2026)]] raises a question the thread had not asked: *is the worker a separate unit of analysis, and does it have its own maturity ladder?*

Blum narrates a full individual trajectory rather than an end state — bound to whatever tools the company bought → improving isolated artifacts with Gemini Gems → centralising work into one harness → the agent maintaining his system of record → the agent maintaining its own *context* → the agent proposing improvements to the system → packaging the system for colleagues. Unlike the firm-level stages, each transition has an **observable marker**: the share of screen time inside the harness (his: 70–80%), whether the agent writes to the system of record or only reads, whether the agent detects its own context gaps unprompted, whether the system proposes its own improvements, and whether it has been distributed to anyone else.

Why this matters for the thread's question:

- **It may explain part of the 1%–13% spread.** Firm-level instruments count tools, budgets, and self-reported effectiveness. If maturity actually accrues to *individuals* first and only later to firms — Blum's system existed long before Workstation made it company infrastructure — then firm instruments would systematically under-observe early maturity and over-observe procurement.
- **It sharpens the CISR Stage 2→3 inflection.** CISR locates the greatest financial impact in moving Stage 2 (pilots) → Stage 3 (ways of working). "Ways of working" is precisely what Blum describes changing, and he supplies a candidate mechanism the firm-level data cannot: centralisation → context accumulation → friction reduction. That is a testable account of *why* the inflection sits there.
- **It supplies the trough the firm-level instruments hide.** Blum is explicit that ROI looks bad first, trust falls, and the human double-checks everything before the compounding starts. A cross-sectional survey cannot distinguish a firm in the trough from a firm whose programme has failed — which may be the single largest source of noise in all four numbers above.

Caveats: N=1, self-reported, unaudited, and selected for having a story worth broadcasting. This does not add a fifth instrument to the cross-walk; it argues the cross-walk is missing an **axis**.

**New question carried by this thread:** does a defensible worker-level maturity scale exist, with observable markers and actions per level — and how does it compose with firm-level stages? (A firm of Stage-4 individuals is not automatically a Stage-4 firm; Blum's Workstation exists precisely to bridge that gap.)

*Partial answer, same day.* The first half was answered hours after this section was written, in the same-day sister thread [[threads/ai-worker-maturity-levels|ai-worker-maturity-levels]] → [[syntheses/ai-worker-maturity-levels|synthesis]]: a six-level scale (L0 Bystander → L5 Multiplier) across six assessable dimensions, fused from seven published ladders plus Blum's lived trajectory, operationalised — since the 2026-09-04 fold — as **The AI Worker Maturity Scale v3** (`inspiration/ai-worker-maturity-model.html`, published via Pages): the calibrated 15-gate engine from the local edition carrying the remote edition's design, cited action layer and L0 floor. Still open here: the scale is corpus-derived and **unvalidated against outcomes**, and the *composition* half — how worker-level maturity aggregates to firm stages — remains this thread's question.

### Adoption figures by instrument, side by side (added 2026-11-04)

The [[2026-07-01-stanford-del-adoption-monitor|Stanford Digital Economy Lab's Adoption Monitor]] is the first source in the corpus that sets several adoption instruments side by side for one country and says why they differ: *"sample size, the populations they represent, and elicitation strategy."* With what the wiki already holds, firm adoption runs from **~10–20%** (US Census, before and after a wording change, per Hatzius) and **20%** (OECD official statistics) to **69%** (an executive survey in four high-income countries, Yotzov et al.) and **88%** (AI Index). US individual adoption runs from **28%** (AI Index) to **62%** (Bick, Blandin & Deming). Three US work-use surveys diverge: two near 50% and rising, one at 33% and falling.

For this thread the lesson is the same one the maturity instruments taught: *adoption* is as instrument-bound as *maturity*. The high-adoption, low-maturity gap above may be partly a gap between generous adoption instruments and strict maturity ones. The Monitor also separates the extensive margin (any use) from the intensive margin (daily use: about a quarter of users). That is a first, crude step from adoption toward maturity.

### Newest editions and new instruments, 2025–2026 (added 2026-11-07)

An ingest of 34 sources on 2026-11-07 checked the cross-walk above against its primary sources and added the instruments published since January 2025. It was prompted by a Dutch research note that tested the five-bar chart for a presentation to hospital quality advisers.

**New instruments with a strict bar land at 5–13%.** All are executive self-reports unless noted.

| Bar | Instrument | % | What counts | Sample, year |
|---|---|---|---|---|
| Strict | [[2025-09-30-bcg-widening-ai-value-gap-2025\|BCG 2025]] → [[2026-09-30-bcg-applied-ai-index-2026\|BCG 2026]] | 5% → 7.5% | "Future-built" on 41 capabilities | 1,250 and 1,330 executives |
| Strict | [[2025-11-05-mckinsey-state-of-ai-2025\|McKinsey State of AI 2025]] | ~6% | "AI high performers": 5% or more of EBIT from AI plus "significant" value | 1,993 respondents, June–July 2025 |
| Strict | [[2025-05-06-accenture-front-runners-guide-scaling-ai\|Accenture]] | 8% | "Front-runners" scaling AI at enterprise level | 2,000 executives, firms above $1bn with an AI strategy; fieldwork 2024 |
| Strict | [[2026-01-19-pwc-global-ceo-survey-2026\|PwC CEO Survey 2026]] | 12% | CEOs reporting both cost and revenue benefits; 56% report no significant benefit | 4,454 CEOs, 95 countries, autumn 2025 |
| Strict | [[2026-10-19-gartner-cio-survey-2026\|Gartner]] | 13% | "Significant or transformational value" | 2,002 CIOs and technology executives, May–July 2026 |
| Middle | [[2025-05-06-ibm-ceo-study-2025\|IBM CEO Study 2025]] | 16% / 25% | Share of AI *initiatives* scaled enterprise-wide / delivering expected ROI | 2,000 CEOs, 2025 |
| Middle | [[2025-08-21-mit-cisr-grow-enterprise-ai-maturity\|MIT CISR 2025]] | 18% | Stage 4 | N=152, 2025 |
| Middle | [[2026-01-21-deloitte-state-of-ai-in-the-enterprise-2026\|Deloitte 2026]] | 25% | Moved 40% or more of their AI experiments into production | 3,235 leaders in firms already using AI, Aug–Sep 2025 |
| Broad | [[2026-09-24-kpmg-ai-pulse-q3-2026\|KPMG Q3 2026]] | 58% | "Measurable business value" | 314 US leaders, $1bn+ firms |
| Broad | [[2025-10-28-wharton-gbk-ai-adoption-report-2025\|Wharton and GBK 2025]] | 74% | Positive ROI (base: all respondents) | 801 US decision makers, large firms, mid-2025 |

Three more are quoted often and are weak on method: [[2025-07-01-mit-nanda-genai-divide-state-of-ai-in-business-2025|MIT NANDA]] (*"95% of organizations are getting zero return"*; 52 interviews, 153 senior leaders surveyed at four conferences, a strict success definition, figures the authors call *"directionally accurate"*), [[2025-06-16-servicenow-enterprise-ai-maturity-index-2025|ServiceNow]] (a vendor's average maturity score, down from 44 to 35) and [[2025-03-14-wilkinson-ciodive-ai-project-failure-rates-sp-global|S&P Global via CIO Dive]] (42% of firms abandoned most AI initiatives in the 2025 survey, against 17%; primary not seen).

**What each instrument counts.** The new instruments count three different things, and a bar chart should not mix them.

- *Executives, answering for their organisation:* PwC (CEOs; global figures weighted by country GDP), Gartner (CIOs and technology executives), KPMG (US leaders at $1bn+ firms), Deloitte (directors to C-suite, in firms already using AI daily). Deloitte asks each respondent what share of their experiments reached production, then reports respondents above a 40% cut-off.
- *Organisations, scored:* ServiceNow gives each organisation a 0–100 score and reports the average, not a share.
- *Initiatives or use cases:* IBM's 25% and 16% are shares of AI initiatives, as CEOs estimate them. Gartner's "one in five" is a success rate per use case, a different unit from its own 13%.

**Breadth, re-checked.** The AI Index 2026's 88% (up from 78%) crosses a change of question, from "adopted" (2024) to "regular use" (2025). The Index does not flag it; McKinsey mentions it only in an exhibit footnote (p. 4). Executive surveys and official statistics still diverge: [[2026-10-01-yotzov-barrero-bloom-nber-w34836-firm-data-on-ai|Yotzov, Barrero, Bloom et al.]] put firm use at 78% across seven executive surveys (N=8,879, May–July 2026), against [[2026-11-04-eurostat-use-of-ai-in-enterprises|Eurostat]]'s 19.95% of EU firms, [[2026-02-10-cbs-ict-gebruik-bij-bedrijven-2025|CBS]]'s 33% of Dutch firms (a break in series in 2025) and the US Census's ~18% after a November 2025 wording change ([[2026-04-03-allen-fed-feds-note-monitoring-ai-adoption-us-economy|FEDS Note]]). The same NBER paper puts AI's contribution to labour-productivity growth at about 0.2% a year, and [[2026-03-01-humlum-vestergaard-still-waters-rapid-currents-nber-w33777|Humlum and Vestergaard]] find null effects on earnings and hours in Danish register data.

**A sector distribution of scale.** The [[2026-03-16-mxi-ai-monitor-ziekenhuizen-2026|M&I AI Monitor Ziekenhuizen 2026]] gives the corpus its first distribution of organisations by self-assessed AI scale: of 52 Dutch hospitals (all seven Santeon hospitals among them), 4% apply AI at very small scale or not at all, 42% at small, 46% at average, **8% at large and 0% at very large scale** (2025: 13 / 53 / 33 / 3 / 0). Breadth on the same panel: 90% use generative AI. The report's conclusion misquotes the small-scale share as 53%, the 2025 value. Internationally the pattern repeats: 2% of large health systems have AI across the whole organisation ([[2025-12-11-deloitte-2026-global-health-care-outlook|Deloitte]]), and 4% of US health-system IT leaders report scaled AI with measurable outcomes ([[2026-04-09-qventus-cio-report-2026|Qventus]], vendor). See [[ai-in-health-care]].

**Reading.** The strict figures resemble each other because each sets a high bar, not because they share a yardstick. Where the bar is "value across the organisation", every instrument lands low; where it drops to "some return", every instrument lands high. The number moves with the bar. On the strict side, 2025 → 2026 movement is small: BCG 5% → 7.5%, McKinsey about 6% both years (2026 secondary), Cisco about 13% for three years. The middle moves more: BCG's scaling group went from 35% to 41%, and Dutch hospitals at average scale from 33% to 46%. Against that, S&P reports more abandonment.

## What's missing / candidate sources to find

- ~~**Updated CISR Future Ready Survey wave**~~ Filled 2026-11-07 by [[2025-08-21-mit-cisr-grow-enterprise-ai-maturity]] (18% Stage 4, but a different and much smaller survey, N=152). The March 2026 follow-up is members-only.
- ~~**Other organizational maturity frameworks**~~ Largely filled 2026-11-07: McKinsey's high performers, Deloitte's State of AI in the Enterprise, Gartner's CIO survey, BCG's future-built series, Accenture, PwC, IBM, KPMG, Wharton and ServiceNow (see the section above). Gartner's own AI maturity model is still not in the wiki.
- **Primary McKinsey reports.** *Superagency in the workplace* (the likely source of the 1%), *The state of AI* 2026 and *The State of Organizations 2026* (which reportedly repeats "only 1 percent of C-suite respondents"): mckinsey.com could not be reached on 2026-11-07, so these rest on secondary coverage.
- **Full reports behind four press releases:** Cisco AI Readiness Index 2025, BCG Applied AI Index 2026, PwC CEO Survey 2026, Gartner's CIO survey.
- **A survey of AI on patient-safety incident reports.** None found for 2025–2026; the M&I monitor has no quality or patient-safety domain.
- **A direct MIT Sloan/CISR ↔ AI Index methodology cross-walk** — if anyone has published one. Not yet found.
- **MITTRI_Cisco** (in `raw/reports/`, not yet ingested) is sponsored MIT Tech Review Insights research, likely to introduce a third framing. Will surface in the next ingest.
- **A worker-level maturity instrument.** ~~Nothing in the corpus measures individual AI maturity with defined levels and transition criteria.~~ Partially filled 2026-08-31: [[syntheses/ai-worker-maturity-levels|the AI Worker Maturity synthesis]] supplies a corpus-derived six-level scale with markers and per-level actions. Still wanted: an externally **validated** instrument — capability frameworks from L&D/HR research, digital-literacy scales adapted to AI, or vendor "AI fluency" rubrics — to test the synthesis against.
- **HBR Anand-Wu Gen AI Playbook** (in `raw/articles/`, not yet ingested). Authors are at NYU Stern / HBS — different academic lineage, may have a different framing.

## How this thread should resolve

When at least 3 sources are ingested with explicit adoption/maturity definitions, this thread should resolve into a syntheses page that:

1. Lists each source's instrument, sample, and definition side-by-side.
2. Maps each source's "mature" / "high-performer" definition to the others.
3. Notes where the numerical claims agree vs. disagree.
4. Identifies what the *practical* implication is for someone trying to assess where their own org stands.

*Status 2026-11-07:* the condition above is met many times over (fifteen instruments with explicit definitions, five of them re-checked against their newest edition). The thread is ready to be synthesized.

Until then, this thread stays open as a reminder to **always include the instrument when citing an adoption/maturity number** — "78% of orgs use AI" without saying "per McKinsey's at-least-one-function definition" loses important meaning.

## Related pages

- [[enterprise-ai-adoption]] — main concept page
- [[2026-04-28-ai-index-report-2025|AI Index 2025]] — first source
- [[2026-04-28-mit-sloan-ai-maturity|MIT Sloan article]] — second source
- [[2026-08-31-blum-how-i-ai-claude-cowork-pm-system|Blum / How I AI]] — the worker-level axis
- [[syntheses/ai-worker-maturity-levels|ai-worker-maturity-levels]] — sister synthesis (same day) answering the worker-scale half of this thread's new question
- [[micro-productivity-trap]] — the J-curve trough that firm-level cross-sections cannot distinguish from failure
- [[MIT CISR]] — institutional source
- [[McKinsey & Company]] — instrument source for AI Index adoption data
- [[ai-in-health-care]] — the sector page for the hospital and health-system figures (added 2026-11-07)
