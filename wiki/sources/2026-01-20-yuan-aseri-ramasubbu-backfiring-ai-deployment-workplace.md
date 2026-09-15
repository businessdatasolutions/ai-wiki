---
type: source
kind: paper
title: "Backfiring AI? AI Deployment in Workplace"
author: ["Di Yuan", "Manmohan Aseri", "Narayan Ramasubbu"]
publisher: "SSRN working paper (id 6103949); Harbert College of Business, Auburn University · Robert H. Smith School of Business, University of Maryland · Joseph M. Katz Graduate School of Business, University of Pittsburgh"
url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6103949"
date_published: 2026-01-20
date_ingested: 2026-09-15
length: "~37 pages of body plus proof appendix (read: abstract, §1 introduction, §2 model setup, Propositions 1–7 with their stated interpretations, §7 conclusion and results-summary table; formal proofs in Appendix A not verified — see Scope)"
raw: "../../raw/papers/backfiring-ai-ai-deployment-in-workplace.md"
tags: [backfiring-ai, game-theory, analytical-model, pay-for-performance, employee-incentives, knowledge-transfer, tangible-skills, intangible-skills, soft-skills, rank-order-tournament, ai-efficacy, workforce-heterogeneity, compensation-design, working-paper, unrefereed]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - contextual/internal-barriers
  - strategic-renewal/organizational-culture
relationships:
  - type: supports
    target: 2026-06-10-anicich-brouwers-why-employees-arent-transparent-ai-usage
    via: "the formal model of the incentive Anicich & Brouwers observe empirically. They find employees hiding AI workflows because disclosure is individually costly; this derives the same logic one step upstream — an AI system that codifies and redistributes a high performer's tangible skill erodes their rank under pay-for-performance, so withholding is the rational response and firm profit falls. Survey finding plus game-theoretic mechanism for the same behaviour"
    confidence: 0.8
  - type: contradicts
    target: 2025-07-07-tambe-reskilling-workforce-for-ai-domain-expertise-algorithmic-literacy
    via: "opposite conclusions about firm value from the same mechanism. Tambe measures financial markets rewarding the dispersion of algorithmic expertise among domain experts; this models that dispersion demotivating the employees whose advantage it dilutes and *lowering* profit. The reconciliation is probably the compensation regime — the harm here exists only inside a rank-order pay-for-performance tournament, which Tambe neither models nor observes — but the wiki should not cite either result alone"
    confidence: 0.7
  - type: supports
    target: 2026-06-12-dellacqua-cybernetic-teammate-field-experiment-genai-teamwork
    via: "converging on which capability AI does not level. Dell'Acqua et al. find AI substituting for the cross-functional knowledge a teammate supplies while human judgment retains value in evaluative selection; this model's entire result rests on AI transferring *tangible* skill while leaving *intangible* skill (communication, coordination) untouched — so the workers who rise are the ones strong in what AI cannot copy. Different methods, same boundary"
    confidence: 0.7
---

# Yuan, Aseri & Ramasubbu — Backfiring AI? AI Deployment in Workplace

An **analytical (game-theoretic) working paper** arguing that deploying AI to spread best practice across a workforce can **reduce firm profit** — not through any technical failure, but because it dismantles the competitive position of the high performers it learns from.

The corpus has plenty of evidence that AI adoption underdelivers. This is its first source offering a **formal mechanism** for why, located in compensation design rather than in tooling, skills, or change management.

## TL;DR

> *"The AI system can learn from high-performing employees and make that knowledge available to others. In a competitive environment, this can disincentivize high-performing employees and ultimately backfire, leading to a decline in overall firm productivity."* — Abstract

The setup is deliberately spare. Employees differ on two independent dimensions, each high or low:

- **Tangible ("hard") skill** — the technical capability AI can observe, codify and redistribute.
- **Intangible ("soft") skill** — communication, coordination, bridging; **AI cannot transfer it, by assumption.**

That gives four types — **HH, HL, LH, LL** — and the firm pays under a **pay-for-performance (PFP)** regime, i.e. rank-order competition on task output.

## The core result

**Proposition 1 (output).** After AI deployment, **HL output falls**, **LH and LL output rises**, **HH is unchanged.**

**Proposition 2 (welfare).** HH unaffected; **HL worse off** — *"their high tangible skills are no longer advantageous in the presence of AI-induced knowledge transfer"*; LH better off because *"AI cannot easily transfer such skills"*; LL better off from the productivity boost.

The authors' own illustration is a software-engineering one, and it is the sharpest paragraph in the paper:

> *"Employees with high technical skills but low interpersonal skills (HL type) may find their traditional competitive advantage eroding. The very technical tasks that once defined their value — like writing code, debugging errors, or performing data queries — can now be learned by AI. As a result, the output they once generated independently can be produced more efficiently using an AI assistant… by employees with low technical skills but high people skills (LH type)."*

The firm loses because the HL group — previously its top producers — rationally cuts effort once the ranking flips, and the gains to LH and LL do not cover it.

## The three managerial results

**Guaranteeing wages does not fix it (Propositions 3–4).** The intuitive remedy — protect the pay of the employees AI disadvantages — *"can be lower"* in profit than doing nothing. Proposition 7 closes the obvious objection: the profit drop is **not** caused by the higher salary bill.

**The optimal AI is deliberately not the best available AI (Proposition 5).** The profit-maximising choice is an efficacy level *"just enough to avoid the flipping in the performance ranking of HL and LH employees."* Stated flatly by the authors: ***"pursuing the most advanced AI system is not always optimal."*** Firms should *"calibrate AI capabilities to balance the enhancement in employee technical skills with their motivation."*

**And the calibration depends on the skill AI cannot touch (Proposition 6).** Optimal efficacy *increases* with the tangible-skill gap (more room to lift the weak) and **decreases with the intangible-skill gap**. Where soft skills vary a lot, LH employees will overtake HL as soon as AI carries their technical load, so the firm should hold AI back further. *"AI investment should account for the skills AI cannot replicate."*

| Stakeholder | No intervention | Guaranteed salary | Optimal AI efficacy |
| --- | :-: | :-: | :-: |
| **Firm** | – | – | **+** |
| HH employees | 0 | 0 | 0 |
| HL employees | – | – | 0 |
| LH employees | + | – | + |
| LL employees | + | 0 | + |

*(Authors' Table 6. Note that the guaranteed-salary "remedy" makes LH employees worse off and helps nobody.)*

## Why the wiki should keep this

Three reasons, in descending order of confidence.

1. **It supplies the mechanism under [[ai-knowledge-hiding]].** [[2026-06-10-anicich-brouwers-why-employees-arent-transparent-ai-usage|Anicich & Brouwers]] found employees withholding their AI workflows and traced it to trust and psychological safety. This derives the same incentive from compensation structure alone — no trust deficit required. If the AI observes your work and redistributes it, and you are paid on rank, hiding is not a culture problem.
2. **It names a design variable the corpus has not had: *AI efficacy as a choice*.** Every other source treats model capability as something to maximise. Here it is a dial with an interior optimum, set against workforce composition.
3. **The tangible/intangible split is independently corroborated.** [[2026-06-12-dellacqua-cybernetic-teammate-field-experiment-genai-teamwork|Dell'Acqua et al.]] find experimentally that AI lifts idea *generation* while *"human judgment retains value in evaluative selection"* — a boundary in the same place this model draws by assumption, reached by measurement rather than by definition.
4. **It predicts a specific winner.** The employee who gains is **LH — low technical, high interpersonal**. That is a sharper and more falsifiable claim than the corpus's usual "soft skills matter more now", and it is directly checkable against [[ai-employment-effects]] data as it accumulates.

## Dynamic capabilities (Warner & Wäger)

- **`digital-transforming/redesigning-internal-structures`** — the paper's prescriptions are structural: recalibrate compensation and deliberately bound AI capability, because the org's reward system and its technology choice interact. It treats AI deployment as an organisational-design decision rather than a procurement one.
- **`contextual/internal-barriers`** — the whole result *is* an internal barrier, formally derived: the firm's own pay-for-performance regime converts a productivity technology into a demotivator, and the barrier is invisible until the ranking flips.
- **`strategic-renewal/organizational-culture`** — competitive versus collaborative reward culture is the hinge on which the entire result turns; the model implies a firm can neutralise the harm by changing how it rewards, not what it deploys.

## Linked entities and concepts

- Concepts: [[ai-knowledge-hiding]], [[ai-employment-effects]], [[automation-vs-augmentation]], [[enterprise-ai-adoption]], [[durable-skills]], [[micro-productivity-trap]], [[ai-deskilling]]
- **Dangling** (single-source mention, deferred): Di Yuan, Manmohan Aseri, Narayan Ramasubbu, Auburn University, University of Maryland, University of Pittsburgh

## Scope and reliability

**The weakest evidential tier in this ingest, and it should be cited accordingly.**

- **It is a model, not a measurement.** There is no data. Every result is a theorem about a stylised firm with two binary skill dimensions, independent skill distributions, a normalised workforce of measure 1, and a specific PFP payoff structure. Whether real firms sit anywhere near those assumptions is untested here.
- **It is an unrefereed SSRN working paper**, and the wiki holds it at `confidence` accordingly on the pages it touches.
- **The load-bearing assumption is that AI transfers tangible but not intangible skill.** That is asserted by definition, and it is doing all the work: relax it and Propositions 1, 2, 5 and 6 all move. It is also increasingly arguable — a growing share of what the corpus documents AI doing (drafting a difficult message, preparing for a negotiation, summarising a meeting for someone who wasn't there) is exactly the intangible half.
- **Conversion caveat:** the body is dense with LaTeX-set mathematics that `pdftotext` flattens badly. Propositions are legible in outline; the formal model and proofs are **not** reliably reproduced in the raw markdown and were not verified. No equation is quoted on this page. Read the PDF before citing any formal result.

**What it is good for:** the mechanism, the vocabulary (tangible/intangible, ranking flip, optimal efficacy), and the three counter-intuitive managerial claims. **What it is not good for:** any magnitude, any prediction about a real firm.

## Debates and supersession

- **Head-on against [[2025-07-07-tambe-reskilling-workforce-for-ai-domain-expertise-algorithmic-literacy|Tambe]]** on whether dispersing codified technical skill creates or destroys firm value. Both papers are about the same mechanism. The likeliest reconciliation is that Tambe's firms are not rank-order tournaments and this paper's harm is *defined* inside one — which would make the practical claim "the dispersion pays **unless** you pay on relative rank." Neither paper tests that, and the wiki records it as open.
- **"Buy the less capable model" is a claim nobody else in the corpus makes,** and it sits awkwardly beside [[small-language-models]], which reaches a superficially similar conclusion (don't over-provision) from entirely unrelated premises (cost, latency, deployability). They should not be conflated: one is about inference economics, the other about employee motivation.
- Open: no empirical test exists. The paper's own predictions — HL welfare declines, LH welfare rises, profit falls under PFP without calibration — are all measurable in principle and measured nowhere.
