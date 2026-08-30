---
type: source
kind: paper
title: "The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers"
author: ["Kevin Zheyuan Cui", "Mert Demirer", "Sonia Jaffe", "Leon Musolff", "Sida Peng", "Tobias Salz"]
publisher: "Management Science (INFORMS), published online 27 February 2026; DOI 10.1287/mnsc.2025.00535"
url: "https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535"
date_published: 2026-02-27
date_ingested: 2026-08-30
length: "publisher abstract + headline estimates only (paywalled; working-paper PDF not converted)"
raw: "../../raw/papers/2026-02-27-cui-demirer-generative-ai-high-skilled-work-three-field-experiments.md"
tags: [rct, field-experiment, github-copilot, developer-productivity, microsoft, accenture, management-science, heterogeneity, seniority, pre-registration]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
  - contextual/internal-enablers
relationships:
  - type: contradicts
    target: 2025-07-10-becker-metr-early-2025-ai-experienced-developer-productivity
    via: "opposite signs from two randomised designs. This study finds +26.08% completed tasks (SE 10.3%) across 4,867 developers at Microsoft, Accenture and a Fortune 100 firm; METR finds +19% completion *time* — slower — for 16 experienced maintainers on their own mature repositories. The reconciling variable is visible in this paper's own heterogeneity result: gains concentrate in *less experienced* developers, i.e. exactly the population METR excluded by design"
    confidence: 0.85
  - type: supports
    target: 2025-09-23-dora-2025-state-of-ai-assisted-software-development
    via: "the causal estimate underneath DORA's correlational turn. DORA's 2025 data shows AI adoption moving from a negative to a positive relationship with delivery throughput; this pre-registered multi-site RCT gives a magnitude for the throughput half of that story. Both leave the stability half untouched — completed tasks and delivery throughput are volume measures, and neither study tracks what the volume costs downstream"
    confidence: 0.7
---

# Cui, Demirer, Jaffe, Musolff, Peng & Salz — The Effects of Generative AI on High-Skilled Work

## TL;DR

**Three randomised field experiments**, at **Microsoft, Accenture, and an anonymous Fortune 100 electronics manufacturer**, measuring what happens when developers are granted access to GitHub Copilot. **4,867 developers.** Pre-registered as AEARCTR-0014530; published in *Management Science*.

**Headline: a 26.08% increase (standard error 10.3%) in completed tasks** for developers granted access.

Two things about that number deserve emphasis over the number itself.

**1. The standard error is large.** 10.3% on a 26.08% point estimate means the 95% interval runs roughly from +6% to +46%. The finding is that the effect is **positive and probably substantial** — not that it is 26%. Citing "26%" as a settled figure overstates what three experiments with this much variance can establish.

**2. The heterogeneity is the real finding.** **Less experienced developers adopted the tool at higher rates and gained more from it.** That single result is what makes this study and [[2025-07-10-becker-metr-early-2025-ai-experienced-developer-productivity|METR's RCT]] compatible rather than merely contradictory: METR studied 16 maintainers with five years of context on their own repositories — the far tail of the experience distribution, where this paper's own gradient predicts the smallest gain. The two studies together support a **gradient claim**: assistance is worth most where the marginal work is acquiring context, and worth least — possibly negative — where the developer already holds it.

**3. Note what the outcome variable is.** *Completed tasks*, not shipped value and not defect-free code. The measure is a **volume** measure. [[2026-03-30-liu-debt-behind-the-ai-boom]] measures what a comparable volume of AI-authored change costs downstream (22.7% of introduced issues still alive at the latest revision), and [[2025-09-23-dora-2025-state-of-ai-assisted-software-development|DORA]] finds throughput and stability moving in opposite directions. None of these studies is wrong; they are measuring different points in the pipeline, and only the first one is flattering.

## Dynamic-capabilities reading

- **`digital-transforming/improving-digital-maturity`** — three large firms measuring a tool rollout with randomisation rather than a satisfaction survey is itself the maturity behaviour the corpus keeps prescribing.
- **`contextual/internal-enablers`** — the adoption gradient by seniority is an enabling-condition finding: who takes up the tool determines where the return lands.

## Linked entities and concepts

- Entities: [[Microsoft]], [[GitHub]]
- Concepts: [[concepts/ai-coding-productivity-evidence|ai-coding-productivity-evidence]], [[concepts/automation-vs-augmentation|automation-vs-augmentation]], [[concepts/ai-employment-effects|ai-employment-effects]], [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]]
- **Dangling** (single-source mention, deferred): Kevin Zheyuan Cui, Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng, Tobias Salz

## Scope and reliability

**Publisher abstract and headline estimates only.** The journal article is paywalled and the working-paper PDF could not be converted in this environment (no local PDF toolchain), so the per-experiment breakdowns, the secondary outcomes (commits, pull requests, builds), and the robustness checks were **not read**. Two of the three sites are the tool vendor (Microsoft, which owns GitHub) and a large systems integrator; the vendor-site issue is mitigated by randomisation and pre-registration but not eliminated. **Before quoting the 26.08% figure in print, read the full paper** — in particular to confirm whether the headline pools all three experiments and how the Microsoft site alone behaves.
