# We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs

**Authors:** Joseph Spracklen, Raveen Wijewickrama, A H M Nazmus Sakib, Anindya Maiti, Bimal Viswanath, Murtuza Jadliwala (University of Texas at San Antonio; University of Oklahoma; Virginia Tech)
**Venue:** 34th USENIX Security Symposium (USENIX Security '25), pp. 3687–3706
**USENIX page:** https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen
**arXiv preprint:** 2406.10279 (v1 12 Jun 2024; v3 2 Mar 2025)
**Code/data:** https://github.com/Spracks/PackageHallucination
**Captured:** 2026-08-30 (WebFetch of the arXiv abstract page; the USENIX page and PDF both returned HTTP 403, so the camera-ready numbers below come from the USENIX *;login:* write-up and secondary reporting)
**fulltext_source:** abstract-only + secondary — see the scope note.

---

## Abstract of the arXiv preprint (verbatim)

> The reliance of popular programming languages such as Python and JavaScript on centralized package repositories and open-source software, combined with the emergence of code-generating Large Language Models (LLMs), has created a new type of threat to the software supply chain: package hallucinations. These hallucinations, which arise from fact-conflicting errors when generating code using LLMs, represent a novel form of package confusion attack that poses a critical threat to the integrity of the software supply chain. This paper conducts a rigorous and comprehensive evaluation of package hallucinations across different programming languages, settings, and parameters, exploring how a diverse set of models and configurations affect the likelihood of generating erroneous package recommendations and identifying the root causes of this phenomenon. Using 16 popular LLMs for code generation and two unique prompt datasets, we generate 576,000 code samples in two programming languages that we analyze for package hallucinations. Our findings reveal that that the average percentage of hallucinated packages is at least 5.2% for commercial models and 21.7% for open-source models, including a staggering 205,474 unique examples of hallucinated package names, further underscoring the severity and pervasiveness of this threat. To overcome this problem, we implement several hallucination mitigation strategies and show that they are able to significantly reduce the number of package hallucinations while maintaining code quality. Our experiments and findings highlight package hallucinations as a persistent and systemic phenomenon while using state-of-the-art LLMs for code generation, and a significant challenge which deserves the research community's urgent attention.

## Key numbers

- **16 code-generating LLMs**, Python and JavaScript, two prompt datasets
- **2.23 million code samples** in the final USENIX camera-ready (the arXiv v3 abstract above still reports the earlier 576,000-sample figure)
- **440,445 samples (19.7%)** contained at least one hallucinated package
- **205,474 unique hallucinated package names**
- Hallucination rate: **≥5.2% commercial models, 21.7% open-source models**
- Framed by the authors as a **"novel form of package confusion attack"** — the mechanism the security community later named **slopsquatting** (an attacker pre-registers a name the model reliably invents)
- Mitigation strategies tested reduce hallucination substantially while maintaining code quality

## Scope note

The USENIX camera-ready (2.23M samples / 440,445 / 19.7%) could not be fetched directly — both the USENIX abstract page and the paper PDF return HTTP 403 to automated fetches. Those three figures come from the USENIX *;login:* article and consistent secondary reporting; the 576,000 / 5.2% / 21.7% / 205,474 figures are verbatim from the arXiv preprint abstract. **Re-verify against the camera-ready PDF before quoting the 2.23M figure in print.**
