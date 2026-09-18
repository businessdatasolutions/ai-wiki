---
type: source
kind: paper
title: "Breaking barriers: investigating generative AI adoption and organizational use"
author: ["Norah Albishri", "Jaskirat Singh Rai", "Rekha Attri", "Muhammad Zafar Yaqub", "Steven T. Walsh"]
publisher: "Journal of Enterprise Information Management (Emerald Publishing)"
journal_volume: "Vol. 39, No. 1 (2026), pp. 267–288"
peer_reviewed: true
url: "https://doi.org/10.1108/JEIM-01-2025-0010"
doi: "10.1108/JEIM-01-2025-0010"
date_published: 2025-07-25
date_ingested: 2026-09-18
length: "~22 pages (journal pp. 267–288; full text read; Tables 7–9 reconstructed from flattened pdftotext output; Figures 1–3 are images that did not survive conversion)"
raw: "../../raw/papers/2025-07-25-albishri-breaking-barriers-genai-adoption.md"
tags: [generative-ai, ai-adoption, diffusion-of-innovations, rogers, trialability, relative-advantage, compatibility, complexity, observability, continued-use, pls-sem, saudi-arabia, managers, survey-research, adoption-theory]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2024-08-13-schwaeke-new-normal-ai-adoption-smes
    via: "compatibility first. The paper cites Schwaeke's eight TOE clusters directly, and its own estimates put compatibility ahead of relative advantage as a driver of trialability (β = 0.325 vs 0.256) — the individual-level counterpart of compatibility being the largest cluster in Schwaeke's review"
    confidence: 0.7
  - type: supports
    target: 2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life
    via: "trying the tool is how trust gets built. Randell & Gousset name a trust gap that closes only by working with the tool in one's own domain, and prescribe a progressive 30/60/90-day rollout; this paper measures trialability as the mediator between the tool's perceived advantages and continued use (indirect effects β = 0.083 and 0.105)"
    confidence: 0.65
  - type: contradicts
    target: 2025-06-15-cimino-ai-adoption-sustainable-growth-smes
    via: "whether acceptance-side measures license organisational conclusions. This paper stops at continued-use intention and still advises firms to be first movers and draws 'valuable insights to organizations'; Cimino, measuring firm-level readiness and implementation separately, finds readiness does not reach economic or collaborative performance — only implementation does. Not a contradiction of the estimates, which measure different things, but of the inference from the one to the other"
    confidence: 0.6
---

# Albishri, Rai, Attri, Yaqub & Walsh — Breaking barriers: investigating generative AI adoption and organizational use

## TL;DR

**The wiki's first test of Rogers' diffusion of innovations, and its first classical-adoption-theory study of generative AI with managers rather than students.** A PLS-SEM survey of **342 managers across Saudi organisations** (convenience/snowball sample, 7-point Likert scales) testing how Rogers' five innovation attributes drive the **continued use** of generative AI tools.

**The headline is trialability.** Everything runs through being able to try the tool:

- Relative advantage → trialability (β = 0.256) and compatibility → trialability (β = 0.325).
- Trialability → benefit observability (β = 0.817), → perceived social influence (β = 0.754), → continued use (β = 0.324).
- Observability → continued use (β = 0.216) and social influence → continued use (β = 0.419).

Trialability mediates both routes from the tool's attributes to continued use, directly and serially through observability and social influence. The model explains 78% of the variance in continued use. For the theory the paper is filed under, see [[technology-adoption-theories]].

## Key claims

**Rogers' model, rewired.** Rogers (2003) treats the five attributes — relative advantage, compatibility, complexity, trialability, observability — as parallel predictors of adoption. This paper orders them into a chain: advantage and compatibility make people willing to try; trying makes benefits visible and gets colleagues talking; visibility and talk sustain use. The authors present this as extending DOI with a mediation structure and "a comprehensive view of innovation diffusion in organizations."

**Complexity moderates only one route.** The interaction of complexity with compatibility is significant (β = −0.142, p = 0.007) and its interaction with relative advantage is not. The authors read the negative sign as "compatibility mitigates [complexity's] effects": for people whose work the tool fits, perceived complexity matters less. See [Scope and reliability](#scope-and-reliability) for why that reading does not match the hypothesis as written.

**Firm size and firm age do not matter.** Neither control variable affects trialability, observability, social influence or continued use. The authors turn this into a first-mover recommendation: adoption "must not be restricted by the firm's size or the firm's experience in the industry."

**Practical prescription**: train before you trial. Make employees aware of the benefits, "first … skill their employees and then use the technology on a trial basis", and use orientation programmes to contain fear of the technology.

## Dynamic-capabilities reading

- **`digital-transforming/improving-digital-maturity`** — the practical implications are a workforce-maturity argument: skill employees first, then trial the technology, because without the fit between employee skill and tool "they will not take the full advantage of technology"; the authors warn that a poor fit creates "a technological cage" around the employee.
- **`contextual/internal-barriers`** — complexity as the barrier to trial: the discussion attributes the null moderation on the advantage route to cognitive load and "the fear of making errors" inhibiting experimentation, plus data-leakage, misuse and ROI uncertainty in the introduction.

## Neighbour sources

The paper cites [[2024-08-13-schwaeke-new-normal-ai-adoption-smes|Schwaeke et al. (2024)]] for its list of adoption factors, and its estimates are consistent with Schwaeke's ranking: compatibility is the stronger driver here, as it is the largest cluster there.

[[2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life|Randell & Gousset (Microsoft, 2025)]] say from practice what this paper measures: a trust gap that only closes by using the tool in your own domain, handled through a progressive 30/60/90-day rollout.

[[2025-06-15-cimino-ai-adoption-sustainable-growth-smes|Cimino et al. (2025)]] is the caution. This paper measures intention to keep using a tool and draws organisational advice from it; Cimino separates firm-level readiness from implementation and finds that readiness alone does not reach economic or collaborative performance. The estimates do not conflict — they measure different constructs — but the leap from an individual's continued-use intention to organisational benefit is exactly the leap Cimino's data says cannot be assumed.

## Linked entities and concepts

- Concepts: [[technology-adoption-theories]], [[enterprise-ai-adoption]]
- **Dangling** (single-source mention, deferred per the second-source promotion rule): Norah Albishri (Princess Nourah bint Abdulrahman University), Jaskirat Singh Rai (Chitkara Business School), Rekha Attri (Jaipuria Institute of Management), Muhammad Zafar Yaqub (King Abdulaziz University), Steven T. Walsh (University of New Mexico).

## Scope and reliability

**What was read.** The complete article, journal pages 267–288 (user-supplied PDF). Tables 7–9 were reconstructed from `pdftotext`'s one-value-per-line output and cross-checked against the §5.3 prose. The Emerald download footer on every page carried a personal institutional access token and was stripped from the raw file.

**H8b's sign is reversed and still called supported.** The hypothesis predicts complexity *positively* moderates compatibility → trialability. The estimate is negative (β = −0.142, CI [−0.241, −0.039]) and §5.3.3 reports the hypothesis as supported, then reinterprets. The interaction is real; it contradicts the hypothesis as stated.

**The constructs barely separate.** HTMT ratios run 0.794–0.898 against the 0.90 ceiling; inter-construct correlations reach 0.832 (social influence with continued use). Several VIFs exceed 4. With six constructs this close, the high R² values and the very large trialability paths (β = 0.817, 0.754) partly reflect shared method variance between neighbouring items. The authors' Harman single-factor and marker-variable checks address common-method bias, but not this.

**"Executives" is a generous label.** 35% of respondents are entry-level and 46% are under 30; the authors concede the sample "may not fully capture perspectives of more traditionally tenured or senior executives." Convenience sample through one author's contacts; cross-sectional; single country.

**One adapted item gives the instrument away.** The compatibility scale was adapted from an m-wallet study, and the paper's own worked example reads "Using Generative AI fits well with my purpose of *learning*" — a student-context phrasing in a study of managers.
