---
type: source
kind: paper
title: "Artificial Intelligence Adoption for Sustainable Growth in SMEs: An Extended Dynamic Capability Framework"
author: ["Antonio Cimino", "Vincenzo Corvello", "Ciro Troise", "Asha Thomas", "Mario Tani"]
publisher: "Corporate Social Responsibility and Environmental Management (ERP Environment / John Wiley & Sons)"
journal_volume: "Vol. 32, No. 5 (2025), pp. 6120–6138"
peer_reviewed: true
url: "https://onlinelibrary.wiley.com/doi/10.1002/csr.70019"
doi: "10.1002/csr.70019"
date_published: 2025-06-15
date_ingested: 2026-09-17
length: "~19 pages (journal pp. 6120–6138; full text read, all seven tables recovered; Figures 1–2 are images that did not survive PDF conversion, so R² values are not recoverable from the held copy)"
raw: "../../raw/papers/2025-06-15-cimino-ai-adoption-sustainable-growth-smes.md"
tags: [dynamic-capabilities, teece, sme, startups, ai-adoption, pls-sem, triple-bottom-line, italy, readiness-vs-implementation, survey-research]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-sensing/digital-mindset-crafting
  - digital-seizing/rapid-prototyping
  - digital-seizing/strategic-agility
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-04-28-warner-wager-dynamic-capabilities-digital-transformation
    via: "the first quantitative test in this corpus of the spine W&W derived qualitatively. Same sense/seize/transform decomposition, inverted on every methodological axis — 210 surveyed Italian startups and PLS-SEM against seven German incumbent MNCs and 18 interpretive interviews. The sensing/seizing/transforming construct loads cleanly as a second-order factor (AVE 0.750), which is external support for the spine being a real construct and not an artefact of W&W's coding scheme"
    confidence: 0.8
  - type: supports
    target: 2026-07-10-when-ai-becomes-common-organizational-capability-becomes-the-advantage-ep-16
    via: "the symposium's thesis is that once AI access is universal, organizational capability becomes the differentiator; this paper is that claim with coefficients on it. Dynamic capabilities predict technological (β = 0.447), collaborative (β = 0.615) and sustainable (β = 0.662) performance, and the AI-adoption paths mediate rather than replace them"
    confidence: 0.8
  - type: supports
    target: 2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company
    via: "the same gap measured on two different instruments. Grant's index reports roughly 30% of enterprise AI in production versus pilot; this paper splits adoption into acceptance (AIAR) and implementation intensity (AIAI) and finds capabilities produce the former nearly twice as readily as the latter (β = 0.523 vs 0.279), while only the latter reaches economic performance"
    confidence: 0.8
  - type: supports
    target: 2026-04-28-anand-wu-genai-playbook
    via: "Anand and Wu's leakage points 2 (employee adoption) and 3 (resource redeployment) name the mechanism this paper's null results measure. AIAR captures a firm at leakage point 2 — trained and willing — and the insignificant AIAR paths to economic (β = 0.094) and collaborative (β = −0.108) performance are the value evaporating before it reaches the P&L"
    confidence: 0.75
  - type: contradicts
    target: 2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset
    via: "whether mindset is the operative lever. Argenti's framing puts readiness and identity shift first — mindset, not skillset. This paper measures firm-level readiness directly as AIAR and finds it does not reach economic or collaborative performance at all; only intensity of actual implementation does. The authors' own conclusion is the rebuttal: fostering enthusiasm for AI is insufficient if not supported by resource allocation and strategic alignment. Note the two constructs are adjacent rather than identical — Argenti argues individual professional identity, Cimino measures organizational openness — and Argenti's other two ingredients (evals, data mastery) are implementation, not mindset"
    confidence: 0.65
---

# Cimino, Corvello, Troise, Thomas & Tani — AI Adoption for Sustainable Growth in SMEs

## TL;DR

**The wiki's first quantitative test of the dynamic-capabilities spine.** No other source in the corpus contains a path coefficient or a structural model; [[dynamic-capabilities]] and [[warner-wager-process-model]] have until now rested entirely on Teece's conceptual work and on W&W's seven-case interpretive study. This is PLS-SEM on **210 Italian innovative startups** (survey November 2024 – January 2025; 234 collected, 210 usable after listwise deletion; 81% with ≤10 employees, 58% in services), testing fourteen hypotheses.

**The contribution is a split.** AI adoption is decomposed into two mediators instead of one:

- **AIAI — AI Adoption Intensity**: the extent to which AI is actually embedded in the firm's processes ("AI has substantially changed our business processes").
- **AIAR — AI Acceptance Rate**: the firm's openness and readiness to adopt ("my company is ready to adopt AI technology to generate innovations").

**The headline result is a readiness–implementation gap, quantified.** Dynamic capabilities buy willingness roughly twice as cheaply as they buy implementation (DC→AIAR β = 0.523 against DC→AIAI β = 0.279) — and only the implementation leg reaches the P&L. The authors' own closing line is the sharpest statement of it:

> "Simply fostering enthusiasm for AI is insufficient if not supported by resource allocation and strategic alignment."

## Key claims

### The model

A second-order construct **DC** (reflective on Sensing, Seizing, Transforming — items adapted from Kump & Kessler 2019) predicts two AI-adoption mediators, which in turn predict four performance dimensions: **TP** technological, **EP** economic, **CP** collaborative, **SP** sustainable. The four-way performance split is itself a claim — prior work, the authors argue, treats firm performance as a single construct and so cannot see the trade-offs between dimensions.

### Results (Table 7 — the authoritative verdicts)

| # | Path | β | T | 95% CI | Supported |
|---|---|---:|---:|---|---|
| H1 | DC → TP | 0.447 | 6.487 | [0.315, 0.577] | Yes |
| H2 | DC → EP | 0.138 | 1.834 | [−0.013, 0.281] | **No** |
| H3 | DC → CP | 0.615 | 10.35 | [0.491, 0.721] | Yes |
| H4 | DC → SP | 0.662 | 16.19 | [0.577, 0.737] | Yes |
| H5 | DC → AIAI | 0.279 | 5.033 | [0.174, 0.391] | Yes |
| H6 | DC → AIAR | 0.523 | 8.550 | [0.398, 0.637] | Yes |
| H7 | AIAI → TP | 0.390 | 7.973 | [0.290, 0.480] | Yes |
| H8 | AIAI → EP | 0.498 | 6.218 | [0.339, 0.652] | Yes |
| H9 | AIAI → CP | 0.268 | 4.480 | [0.151, 0.385] | Yes |
| H10 | AIAI → SP | −0.079 | −1.570 | [−0.179, 0.016] | **No** |
| H11 | AIAR → TP | 0.192 | 3.056 | [0.080, 0.325] | Yes |
| H12 | AIAR → EP | 0.094 | 1.264 | [−0.053, 0.242] | **No** |
| H13 | AIAR → CP | −0.108 | −1.550 | [−0.238, 0.033] | **No** |
| H14 | AIAR → SP | 0.213 | 3.601 | [0.098, 0.330] | Yes |

### Three findings worth carrying

**1. Only implementation pays.** AIAI reaches technological, economic and collaborative performance. AIAR reaches none of the operational dimensions — its path to collaborative performance is signed *negative*. Readiness is a necessary but demonstrably insufficient condition.

**2. Dynamic capabilities do not produce economic performance in early-stage firms.** H2 fails. The authors read this as a stage effect — capabilities in startups are directed at experimentation, product development and market entry rather than immediate financial return — and align it with Wilden et al. (2013), who found dynamic capabilities can even depress sales growth outside organic structures and high-competition environments. It is a boundary condition on the DC→performance link, not a refutation.

**3. The sustainability inversion.** Actually implementing AI does *not* improve sustainable performance (H10, negative-signed); being *open* to AI does (H14, β = 0.213). The authors' explanation is that startups adopt AI experimentally rather than for sustainability ends, while AIAR captures broader strategic intent. See [Scope and reliability](#scope-and-reliability) — this page does not carry that explanation forward as established.

## Dynamic-capabilities reading

The paper is a rare case of a source that is *about* the tagging vocabulary rather than merely classifiable by it — but the mapping is at Teece's generic level, not W&W's digital microfoundations. See the caveat under [Scope and reliability](#scope-and-reliability).

- **`digital-sensing/digital-scouting`** — the five Sensing items are scanning verbatim: knowing market best practices, being current on the market situation, systematically searching for market information, and keeping "an eye on our competitors' activities."
- **`digital-sensing/digital-mindset-crafting`** — AIAR *is* this cell operationalised as a survey construct: organisational readiness and willingness to adopt AI to generate innovations. The paper's practical advice reinforces it — cultivate internal AI champions, integrate AI into the company vision, build shared ownership to reduce resistance.
- **`digital-seizing/rapid-prototyping`** — §6.2 recommends "agile decision-making frameworks such as iterative prototyping or lean experimentation," and the discussion repeatedly attributes startups' AI use to an "experimental or developmental focus."
- **`digital-seizing/strategic-agility`** — the Seizing items measure how quickly the firm relates to and acts on outside knowledge, turning new technological knowledge into process and product innovation.
- **`digital-transforming/redesigning-internal-structures`** — the Transforming items are pure change-execution (clear responsibilities, seeing change projects through despite interruptions, running change alongside daily business), and §6.2 prescribes cross-functional AI task forces pairing technical experts with domain specialists.
- **`digital-transforming/improving-digital-maturity`** — AIAI is a digital-maturity measure by another name, and the training prescription is explicitly role-differentiated: operations teams in process automation, sales in AI-enabled CRM, leadership in adoption planning.
- **`contextual/internal-barriers`** — resource constraint is the authors' explanation for *every* null result: limited financial and technical resources block conversion of acceptance into intensive use, and underdeveloped sustainability strategies keep AI implementation from reaching sustainable performance.

## Neighbour sources

Four supporting edges and one contradiction.

The parent framework is [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation|Warner & Wäger 2019]], which this paper supports from the opposite methodological direction — survey instrument and structural model against interpretive case work, early-stage SMEs against incumbent MNCs. The MIT Sloan CIO Symposium's [[2026-07-10-when-ai-becomes-common-organizational-capability-becomes-the-advantage-ep-16|Episode 16]] argues that organizational capability becomes the differentiator once AI access is universal; this paper puts coefficients on that argument.

The readiness–implementation gap has an independent measurement in [[2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company|BBC AI Decoded (August 2026)]], where Peter Grant reports roughly 30% of enterprise AI in production versus pilot — the same gap read off a different instrument. And [[2026-04-28-anand-wu-genai-playbook|Anand & Wu's leakage diagnostic]] supplies the mechanism: their leakage point 2 (employee adoption) is what a high AIAR score describes, and the insignificant AIAR→EP path is that value evaporating before the P&L.

Against these, [[2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset|Argenti's "mindset, not skillset"]] sits in tension with the central null result. Argenti puts readiness and identity shift first; this paper measures firm-level readiness and finds it insignificant for both economic and collaborative performance. The disagreement is real but narrower than the headlines suggest — Argenti argues individual professional identity where Cimino measures organizational openness, and two of Argenti's three ingredients (obsess over evals, master your data) are implementation rather than mindset.

## Linked entities and concepts

- Concepts: [[dynamic-capabilities]], [[warner-wager-process-model]], [[enterprise-ai-adoption]]
- **Dangling** (single-source mention, deferred per the second-source promotion rule): Antonio Cimino (University of Messina), Vincenzo Corvello (University of Messina), Ciro Troise (University of Turin, corresponding author), Asha Thomas (Wrocław University of Science and Technology), Mario Tani (University of Naples Federico II).

## Scope and reliability

**What was read.** The complete article, journal pages 6120–6138. All seven tables were recovered via a second `pdftotext -layout` pass. **Figures 1 and 2 are images and did not survive conversion — Figure 2 carries the R² values, so the model's explanatory power is not quotable from the held copy.**

**Discriminant validity of the paper's own contribution is marginal.** AIAI and AIAR correlate at **HTMT = 0.878**. That clears the liberal 0.90 threshold and fails the conservative 0.85 one, and the whole contribution rests on the two being distinct constructs. The sustainability sign-inversion (finding 3) is the shape one expects when two near-collinear constructs split shared variance, and the authors' explanation for it — that AIAR captures "broader strategic intent and long-term vision" — is asserted rather than tested. **This page carries the inversion as a result, not as an established mechanism.**

**Prose and Table 7 disagree; the table is cited here.** H1 is β = 0.47 in the discussion against 0.447 in the table; H9 is 0.288 against 0.268; H12 is called rejected while the prose quotes "p = 0.010" against a confidence interval that straddles zero; and the significance legend defines `**` and `***` but never the `*` it applies to H2. The full list is in the raw stub's data-quality note.

**The tagging maps to generic Teece, not to W&W's digital microfoundations.** The DC instrument (Kump & Kessler 2019) measures sensing, seizing and transforming in their *general* form — market scanning, knowledge absorption, change execution. Nothing in it is digital-specific. So the external support this source lends [[warner-wager-process-model]] is support for the **three-cluster spine**, not for the **nine digital microfoundations** layered on top of it. The `dynamic_capabilities:` cells above are the wiki's reading of the construct, not the paper's own claim.

**Generalisability, per the authors.** Italian innovative startups only; cross-sectional, so no dynamic evolution of adoption is observable; single-method self-report survey; no moderators tested (firm size, industry type). The authors note explicitly that early-stage innovative startups are "a distinct subset of SMEs" and that results "may not be directly generalizable to the broader SME sector." With 81% of the sample under eleven employees, this is evidence about micro-firms.

**Common-method bias** was addressed procedurally (anonymity guaranteed, academic purpose stated, items intermixed) but not statistically — no Harman single-factor test or marker variable is reported.
