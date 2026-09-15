---
type: source
kind: paper
title: "Reskilling the Workforce for AI: Domain Expertise and Algorithmic Literacy"
author: ["Prasanna B. Tambe"]
publisher: "Forthcoming, Management Science; The Wharton School, University of Pennsylvania (SSRN id 3776492, version dated 7 July 2025)"
url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3776492"
date_published: 2025-07-07
date_ingested: 2026-09-15
length: "~24 pages of body plus appendices (full text read: abstract, §1 introduction, the three empirical findings, §7 conclusions with stated limitations; regression tables read in outline only — see Scope)"
raw: "../../raw/papers/reskilling-the-workforce-for-ai-domain-expertise-algorithmic-literacy.md"
tags: [tambe, wharton, management-science, algorithmic-literacy, domain-expertise, decentralization, reskilling, no-code, ai-literacy, workforce-complements, it-workforce, job-postings, lightcast, revelio, o-net, compustat, firm-value, peer-reviewed, labour-economics]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - contextual/internal-enablers
relationships:
  - type: supports
    target: 2025-07-02-joshi-venkatraman-fowler-expert-generalists
    via: "the labour-market measurement behind a thesis the corpus held as consultancy argument. Thoughtworks argues firms over-value narrow specialists and should cultivate breadth; Tambe shows employers doing exactly that in hiring data — by 2016 only one-third of listings requiring algorithmic expertise were for IT occupations, and the skill spreads in a pattern resembling office software rather than database administration. The [[expert-generalist]] page gains an empirical leg"
    confidence: 0.8
  - type: supports
    target: 2026-06-12-dellacqua-cybernetic-teammate-field-experiment-genai-teamwork
    via: "the same boundary-dissolution claim from opposite methods and opposite directions. Dell'Acqua et al. show AI letting a commercial professional produce technically balanced work inside a one-day experiment; Tambe shows the labour market repricing that combination across eight years of hiring and workforce data, and financial markets paying for it. Experimental mechanism plus observational scale"
    confidence: 0.75
  - type: supports
    target: 2026-08-06-garry-tan-own-your-intelligence
    via: "an academic statement of the ownership argument Tan makes to founders. Tan's *'own your skills, because if you don't, your job becomes a skill file'* is about individuals capturing algorithmic capability; Tambe measures the firm-side complement — that value accrues where algorithmic expertise sits **with the domain expert** rather than in a central IT or data-science function, and that no-code tooling accelerates the spread"
    confidence: 0.7
  - type: contradicts
    target: 2026-01-20-yuan-aseri-ramasubbu-backfiring-ai-deployment-workplace
    via: "two papers on the same mechanism — AI redistributing codified technical skill across a workforce — reaching opposite conclusions about firm value. Tambe measures markets rewarding the dispersion of algorithmic expertise; Yuan et al. model that same dispersion demotivating the employees it dilutes and *lowering* firm profit under pay-for-performance. The disagreement turns on whether compensation is competitive: Tambe's firms are not modelled as rank-order tournaments, and Yuan et al.'s harm exists only inside one. Neither refutes the other, and the pair is the sharpest open question this ingest adds"
    confidence: 0.7
---

# Tambe — Reskilling the Workforce for AI: Domain Expertise and Algorithmic Literacy

**Prasanna B. Tambe** (Wharton), forthcoming in *Management Science*. The corpus's first **labour-market measurement** of the claim that AI's complement is not more IT specialists but **algorithmic expertise dispersed among the people who already hold the domain knowledge**.

The paper opens with a [[NVIDIA]] epigraph that the rest of the paper then tests rather than asserts — Jensen Huang's *"the people that understand how to solve a domain problem in digital biology or in education of young people or in manufacturing or in farming, those people who understand domain expertise now can utilize technology that is readily available to you."*

## TL;DR

> *"The value generated from AI and algorithms is amplified when the skills required to use these technologies are dispersed among workers with domain knowledge. This decentralization of technical expertise stands in contrast to other business technologies for which the complementary skills are primarily embodied in IT specialists."* — Abstract

Two definitions do the work:

- **Algorithmic expertise** — the ability to use and interact with tools *"capable of autonomously generating decisions or content"*: ML and data-science algorithms, predictive software, generative AI, AI-powered analytics. Deliberately **excludes** relational databases and web technologies, which lack that autonomy and need more human input to produce output.
- **Domain expertise** — knowledge required to work in a specialised field: nursing, sales, marketing, accounting.

The argument is that algorithms are unlike prior enterprise IT because they must be *adapted to specialised business processes*, which requires the two kinds of human capital to be **integrated in one head** rather than coordinated across a boundary.

## Three findings, three datasets

**1. Employers moved the skill out of IT (US job listings, 2013–2016).** Demand for algorithmic expertise grew fastest in **non-technical occupations**, and the diffusion pattern *"more closely resembles general-purpose office software skills (e.g., word processing tools) than technical skills like database administration."* The headline number: **by 2016, only one-third of listings requiring algorithmic expertise were for IT occupations.** In non-IT occupations, these skills were particularly likely to appear in listings that also required domain expertise.

**2. The workforce followed, and no-code accelerated it (worker-reported panel, 2015–2021, large public firms).** Algorithmic skills spread among **non-technical domain experts with decision-making responsibilities** — and specifically not in the pattern other information technologies follow. *"The proliferation of software innovations that make it easier to use algorithms, such as 'no-code' tools, increased the likelihood that domain experts acquired these skills."*

**3. Markets pay for the combination, and only for this technology.** Investors assign **higher value to a firm's AI and data-science investments when made alongside decentralised algorithmic expertise**. The interaction appears for data science earlier in the panel and *"strengthens and becomes more pronounced for AI investments in the later period."* The robustness result is what makes it interesting: *"Similar patterns do not emerge for other technologies or for expertise in other categories of technical skill."* The complementarity is specific to algorithmic technology, not a general story about technical literacy.

Data sources: Lightcast (then Burning Glass) job postings; Revelio workforce panel; BLS **O\*NET** occupational knowledge content; Compustat-Capital IQ financials.

## Why this matters to the wiki

The corpus has a well-developed practitioner argument that breadth beats narrow specialisation under AI — [[expert-generalist]], built on [[2025-07-02-joshi-venkatraman-fowler-expert-generalists|Thoughtworks]]. It had **no labour-market evidence**. This is that evidence, and it arrives with a market-value test attached rather than only a hiring-demand test.

It is also the firm-side complement to an argument the corpus holds from the founder side. [[2026-08-06-garry-tan-own-your-intelligence|Garry Tan]] tells individuals to *"own your skills, because if you don't, your job becomes a skill file"*; Tambe measures the organisational version — value accrues where algorithmic capability sits **with the domain expert**, not in a central function — and identifies no-code tooling as what makes that migration possible.

It also gives the [[durable-skills]] and [[automation-vs-augmentation]] pages a mechanism at the **org-design** level rather than the individual level: the question is not *which skills survive* but **where in the org chart the technical skill should sit**. Tambe frames this as a skills-based version of the centralisation/decentralisation tradeoff studied for IT decision rights — and notes that distributing *skills* is harder than distributing *authority*, because it requires human-capital investment rather than a reorganisation.

## Dynamic capabilities (Warner & Wäger)

- **`digital-transforming/redesigning-internal-structures`** — the paper's core question is where technical capability sits in the organisation: centralised in IT/data science, or pushed out to domain experts with decision rights. Finding 2 measures that redistribution happening.
- **`digital-transforming/improving-digital-maturity`** — the managerial prescription is a maturity path: *"managers should consider how to develop algorithmic expertise among domain experts rather than solely relying on centralized IT departments or data science teams"*, especially in deep-domain contexts like healthcare and finance.
- **`contextual/internal-enablers`** — no-code tooling functions as a measured enabler: it raises the probability that a domain expert acquires algorithmic skill, which is an enabling condition rather than a capability in itself.

## Linked entities and concepts

- Concepts: [[expert-generalist]], [[durable-skills]], [[automation-vs-augmentation]], [[enterprise-ai-adoption]], [[ai-employment-effects]], [[dynamic-capabilities]]
- Entities: [[NVIDIA]] (via the Jensen Huang epigraph), [[Erik Brynjolfsson]] (cited throughout as the reference literature on IT-workforce complements)
- **Dangling** (single-source mention, deferred): Prasanna B. Tambe, The Wharton School, Management Science, Lightcast / Burning Glass, Revelio Labs, O\*NET, Compustat

## Scope and reliability

Peer-reviewed (forthcoming *Management Science*), multi-dataset, with a robustness test that rules out the obvious confound. That is a strong tier. Four limits, three of them the author's own:

- **It measures skill *bundles in jobs*, not capability.** The data *"does not distinguish between deep technological expertise and interactional expertise"* — the latter may be enough to talk to tool-builders but not enough to use the tools well. Every finding here is about what employers *ask for* and what workers *report*, not about what anyone can do.
- **The market-value result is an association.** Investors valuing the combination is not evidence the combination produces output. The author says so: *"more time is needed for firms to adapt to this new mode of production to gather stronger causal evidence of the impact of these workforce changes on performance."*
- **Static view.** No long-term labour-market consequences; the paper explicitly declines to model them.
- **The data predates the generative-AI wave.** Postings end 2016 and the workforce panel ends 2021. The definition of algorithmic expertise covers generative AI, but almost none of the measured variation can be generative AI. Applying these findings to 2026 LLM adoption is an extrapolation the paper does not make.

**Conversion note:** regression tables survive `pdftotext -layout` as whitespace-aligned text and coefficient/standard-error pairing is usually readable, but was **not** verified cell by cell. No coefficient is quoted on this page for that reason — the three findings above are stated in the author's own prose.

## Debates and supersession

- **Against [[2026-01-20-yuan-aseri-ramasubbu-backfiring-ai-deployment-workplace|Yuan, Aseri & Ramasubbu]].** Tambe finds markets rewarding the dispersion of algorithmic expertise; they model that same dispersion demotivating high performers and reducing firm profit. The reconciliation is probably the **compensation regime** — Yuan et al.'s harm exists only under pay-for-performance rank-order competition, which Tambe does not model or observe. Recorded as the open question this ingest adds; neither result is safe to cite without the other.
- **Does no-code dispersion produce competence or its appearance?** Tambe's limitation (deep vs interactional expertise) and [[2026-06-12-dellacqua-cybernetic-teammate-field-experiment-genai-teamwork|Dell'Acqua et al.'s]] open question (*"genuine knowledge growth, or merely temporary access to existing expertise?"*) are the same question asked from labour-market and experimental sides. Neither answers it, and [[ai-deskilling]] is where it lands.
- Open: whether the 2013–2021 pattern holds under generative AI, where the tool requires *less* algorithmic literacy than the no-code tooling Tambe measures. It is at least arguable that LLMs weaken the very complementarity this paper documents.
