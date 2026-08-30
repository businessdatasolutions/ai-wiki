---
type: source
kind: paper
title: "We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs"
author: ["Joseph Spracklen", "Raveen Wijewickrama", "A H M Nazmus Sakib", "Anindya Maiti", "Bimal Viswanath", "Murtuza Jadliwala"]
publisher: "USENIX Security '25, pp. 3687–3706; arXiv preprint 2406.10279"
url: "https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen"
date_published: 2025-06-12
date_ingested: 2026-08-30
length: "arXiv preprint abstract verbatim + camera-ready headline figures from secondary sources (both PDFs returned HTTP 403)"
raw: "../../raw/papers/2025-06-12-spracklen-package-hallucinations-code-generating-llms.md"
tags: [package-hallucination, slopsquatting, supply-chain, usenix-security-2025, package-confusion, pypi, npm, dependency-attack, open-source-models, mitigation]
dynamic_capabilities:
  - contextual/external-triggers
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2025-07-30-veracode-2025-genai-code-security-report
    via: "two 2025 security measurements of AI-generated code, weeks apart, converging on the same structural point: the flaw class is systematic rather than incidental, and it does not shrink with model quality. Veracode finds 45% of samples introducing OWASP Top 10 flaws with performance flat across model size and vintage; this finds hallucinated dependencies at 5.2% (commercial) to 21.7% (open-source), i.e. varying by model *class* rather than improving with capability"
    confidence: 0.8
  - type: supports
    target: 2026-03-30-liu-debt-behind-the-ai-boom
    via: "the controlled measurement of an AI code defect class and the in-the-wild study of what happens to such defects afterwards. This paper identifies the mechanism by which a hallucinated import becomes an exploitable supply-chain entry point; Liu et al. show that 22.7% of AI-introduced issues are never fixed at all"
    confidence: 0.65
---

# Spracklen et al. — We Have a Package for You! Package Hallucinations by Code Generating LLMs

## TL;DR

The empirical foundation for **slopsquatting** — the supply-chain attack in which an adversary registers a package name that language models reliably invent.

**The mechanism, which is what makes this different from ordinary hallucination.** An LLM writing code invents an import for a package that does not exist. Normally this is a harmless error: the install fails and the developer notices. It stops being harmless when **the same model invents the same name repeatedly**, because that turns a random error into a *predictable* one — and a predictable name is a name an attacker can register in advance. The authors name it correctly in the abstract: *"a novel form of package confusion attack."* The security community's later coinage, **slopsquatting**, is the typosquatting analogy, except the developer never made a typo. The model did, on their behalf, consistently.

**Scale of the measurement:**

| | |
| --- | ---: |
| Code-generating LLMs tested | **16** |
| Languages | Python, JavaScript |
| Code samples generated (USENIX camera-ready) | **2.23 million** |
| Samples containing ≥1 hallucinated package | **440,445 (19.7%)** |
| **Unique hallucinated package names** | **205,474** |
| Hallucination rate, commercial models | **≥5.2%** |
| Hallucination rate, open-source models | **21.7%** |

**205,474 distinct fictional package names is the number that should alarm anyone.** That is the size of the attack surface — a list of names, freely derivable by anyone who can run the same models, each one a slot on PyPI or npm waiting to be filled with whatever the registrant likes.

**The commercial/open-source gap (5.2% vs 21.7%) is a four-fold difference**, and it is a *class* difference rather than a capability gradient — which puts it alongside [[2025-07-30-veracode-2025-genai-code-security-report|Veracode's]] finding that security performance is flat across model size and vintage. Neither result supports "wait for the next model."

**Mitigations exist.** The authors implement several hallucination-mitigation strategies and show they *"significantly reduce the number of package hallucinations while maintaining code quality"* — this is not a counsel of despair, and the operational answer for a team is unglamorous and available today: **verify every dependency an agent adds against the registry before it merges.** That is a mechanical check, and it belongs on the list next to [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Merge Mommy's]] *data security* risk dimension.

And the defects do not get cleaned up on their own: [[2026-03-30-liu-debt-behind-the-ai-boom|Liu et al.]] find **22.7% of AI-introduced issues still present at the latest repository revision**, so an unverified hallucinated import is not a transient error but a candidate for permanent residence.

## Dynamic-capabilities reading

- **`contextual/external-triggers`** — a genuinely new attack surface created by the technology's adoption, external to any single organisation's choices.
- **`contextual/internal-barriers`** — an unverified agent-authored dependency is a direct path into a production build, and the practitioner setups in this ingest merge dependency changes at volume.

## Linked entities and concepts

- Concepts: [[concepts/ai-generated-code-quality|ai-generated-code-quality]], [[concepts/attack-surface-management|attack-surface-management]], [[concepts/agentic-pull-requests|agentic-pull-requests]], [[concepts/responsible-ai|responsible-ai]], [[concepts/open-source-ai|open-source-ai]]
- **Dangling** (single-source mention, deferred): Joseph Spracklen, Raveen Wijewickrama, A H M Nazmus Sakib, Anindya Maiti, Bimal Viswanath, Murtuza Jadliwala

## Scope and reliability

**A split-provenance page, and the split matters.** The **arXiv preprint abstract** (verbatim in the raw file) reports **576,000 samples**; the **USENIX camera-ready** reports **2.23 million samples / 440,445 hallucinating / 19.7%**. Both the USENIX abstract page and the paper PDF return **HTTP 403** to automated fetches, so the camera-ready figures here come from the USENIX *;login:* write-up and consistent secondary reporting, **not from the paper itself**. The 5.2% / 21.7% / 205,474 figures are verbatim from the preprint. **Re-verify the 2.23M and 19.7% figures against the camera-ready PDF before quoting them in print.** Model vintage is 2024–early 2025 and the specific rates will have moved; the mechanism and the attack surface have not. Code and data are public at `github.com/Spracks/PackageHallucination`.
