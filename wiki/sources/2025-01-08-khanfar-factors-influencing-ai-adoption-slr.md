---
type: source
kind: paper
title: "Factors influencing the adoption of artificial intelligence systems: a systematic literature review"
author: ["Ahmad A. Khanfar", "Reza Kiani Mavi", "Mohammad Iranmanesh", "Denise Gengatharen"]
publisher: "Management Decision (Emerald Publishing)"
journal_volume: "Vol. 63, No. 10 (2025), pp. 3727–3755"
peer_reviewed: true
url: "https://doi.org/10.1108/MD-05-2023-0838"
doi: "10.1108/MD-05-2023-0838"
date_published: 2025-01-08
date_ingested: 2026-09-18
length: "~40 pages (author accepted manuscript from ECU Research Online, read in full; Figure 3 — the proposed model — is an image that did not survive PDF conversion)"
raw: "../../raw/papers/2025-01-08-khanfar-factors-influencing-ai-adoption-slr.md"
tags: [ai-adoption, systematic-literature-review, adoption-theory, toe-framework, tam, utaut, multi-level, firm-level, employee-level, top-management-support, resistance-to-change, prisma]
dynamic_capabilities:
  - contextual/internal-enablers
  - contextual/internal-barriers
  - contextual/external-triggers
  - digital-transforming/improving-digital-maturity
  - digital-transforming/redesigning-internal-structures
relationships:
  - type: supports
    target: 2024-08-13-schwaeke-new-normal-ai-adoption-smes
    via: "two systematic reviews that organise AI adoption with the same TOE frame and land on overlapping factor lists — compatibility, infrastructure and technical readiness, top-management support, culture, competitive pressure, regulation. Khanfar reviews organisations of any size; Schwaeke restricts to SMEs; Khanfar adds the individual level that Schwaeke folds into compatibility"
    confidence: 0.8
  - type: supports
    target: 2025-06-09-krakowski-human-centered-ai-field-experiment
    via: "the review's central claim is that firm-level choices shape employee-level adoption rather than operating independently of it. Krakowski et al. test exactly that in the field: four firm-set parameters — work procedure, decision authority, training, incentives — decide whether the same AI system raises or lowers sales performance"
    confidence: 0.75
  - type: supports
    target: 2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company
    via: "both start from the same shortfall — AI projects that do not deliver their promised benefits (70% in the review's cited figure; 56% of CEOs without a return in the PwC survey BBC prefers) — and both put training and educational resources among the load-bearing gaps"
    confidence: 0.7
  - type: contradicts
    target: 2026-05-07-carucci-resistance-as-data
    via: "what resistance to change is. The review files it as a factor that negatively influences adoption, to be overcome through involvement, training and management support. Carucci argues all resistance is meaningful data about the change, and that sorting it into legitimate versus kneejerk is the leader's mistake. Barrier to remove versus signal to read"
    confidence: 0.6
---

# Khanfar, Kiani Mavi, Iranmanesh & Gengatharen — Factors influencing the adoption of AI systems

## TL;DR

**A systematic review of 90 papers on AI adoption *in organisations*, and the one source in the wiki that argues the two levels of adoption theory belong together.** Information-systems research explains firm adoption with TOE, institutional theory and the resource-based view, and employee adoption with TAM, UTAUT and the expectation–confirmation model. The field's working assumption, the authors write, is "that the firm- and individual-level factors are independent of each other." The review challenges it.

**The method.** PRISMA protocol on Scopus (search run 12 July 2022): 4,775 records → 2,051 journal articles in English → 158 after title/abstract screening → 90 after full text. Studies of consumers and students were **excluded**; only adoption by firms and their employees counts. 96.7% of the included papers date from 2019–2022.

**The output** is a catalogue of factors in five groups — individual, social, technological, organisational, environmental — with each factor marked as influencing the **firm-level** decision (to invest), or **both** the firm decision and the **employee-level** decision (to use). That second marking is the contribution: some TOE factors are not just inputs to a manager's investment decision but reach into how employees perceive and use the system. See [[technology-adoption-theories]].

## Key claims

### The factors, by level

| Group | Firm-level only | Firm **and** employee level |
|---|---|---|
| **Technological** | return on investment, cost, benefits, integration, compatibility with IT infrastructure, system maturity, reliability and accuracy | system complexity, privacy and security, trust in technology, task–technology fit |
| **Organisational** | organisational readiness, AI governance system, financial readiness, firm size, technical readiness, reliability/accuracy concerns | clarity of roles and responsibilities, innovation culture, resistance to change, collaboration and communication culture, skilled resources, education and training, task complexity, effective operations, managerial capabilities, top-management support, technology-implementation experience |
| **Environmental** | competitive pressure, market uncertainty, skilled resources in the market, market demand, industry and government regulation, government support, political issues, AI vendor availability, CSR | AI vendor support, business-partner support |

Individual factors (perceptions and feelings, personal characteristics) and social factors sit at the employee level only: **fear of job loss** is the most-cited individual factor after perceived usefulness and ease of use; self-efficacy, personal innovativeness, AI knowledge and ICT competence are the personal characteristics; subjective norms and image are the social ones.

### The worked example of the bridge

**Top-management support** is the review's clearest case. For the firm it means allocating budget; for the employee it means training and resources — so the same factor enters two decisions. **Innovation culture** runs the other way: it motivates employees to engage with the change, and their engagement "convinc[es] management to invest in AI systems."

### Five research directions

The authors ask for employee-level studies (most AI-adoption work is firm-level, but "a substantial proportion of AI adoption projects fail at the implementation stage"); for studies of how TOE factors shape employee perceptions; for heterogeneity between employees rather than assuming them homogeneous; for hedonic and social factors beside functional ones; and for methods that model interaction between factors (ANN, AHP, fsQCA, ANFIS).

## Dynamic-capabilities reading

- **`contextual/internal-enablers`** — top-management support, innovation culture, and collaboration and communication culture as factors that operate on both levels at once.
- **`contextual/internal-barriers`** — resistance to change, fear of job loss and technology anxiety.
- **`contextual/external-triggers`** — competitive pressure (the most-cited environmental factor, 18 studies), market demand and market uncertainty.
- **`digital-transforming/improving-digital-maturity`** — skilled resources and experts (the most-cited organisational factor, 26 studies), education and training resources, and ICT competence.
- **`digital-transforming/redesigning-internal-structures`** — clarity of roles and responsibilities and an AI governance system: "AI implementation results in changes in organisational processes; thus, it requires redefining the roles of employees."

## Neighbour sources

[[2024-08-13-schwaeke-new-normal-ai-adoption-smes|Schwaeke et al. (2024)]] is the sibling review: the same TOE frame and an overlapping factor list, restricted to SMEs, without the individual level. Read together they are the wiki's TOE evidence base.

[[2025-06-09-krakowski-human-centered-ai-field-experiment|Krakowski et al. (2025)]] is the experimental test of Khanfar's central claim. The review argues firm-level choices shape employee adoption; the field experiment shows four firm-set parameters — work procedure, decision authority, training, incentives — decide whether one AI system raises or lowers the performance of the same salespeople.

[[2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company|BBC AI Decoded (August 2026)]] starts from the same value shortfall and names training as a gap; the review's education-and-training factor is one of its most-cited.

[[2026-05-07-carucci-resistance-as-data|Carucci (HBR, 2026)]] disagrees on what resistance is. The review treats resistance to change as a negative factor to be reduced by involving employees early; Carucci argues all resistance is data about the change and should be read, not managed away.

## Linked entities and concepts

- Concepts: [[technology-adoption-theories]], [[enterprise-ai-adoption]]
- **Dangling** (single-source mention, deferred per the second-source promotion rule): Ahmad A. Khanfar (corresponding author), Reza Kiani Mavi, Mohammad Iranmanesh, Denise Gengatharen — all School of Business and Law, Edith Cowan University.

## Scope and reliability

**What was read.** The author accepted manuscript deposited at ECU Research Online (CC BY-NC), read in full. It is not the typeset version, so late copy-edits are not reflected. **Figure 3, the proposed firm/employee model, is an image and did not survive conversion**; the model above is reconstructed from the §4 prose, which describes it box by box. The repository cover sheet points to a wrong published-version DOI (`10.3109/13668250.2024.2424784`); the correct DOI is on the same sheet and in the citation.

**The evidence base predates generative AI.** The search ran on 12 July 2022, four months before ChatGPT. "AI" here means chatbots, robots, RPA, expert systems, and voice and face recognition. Whether the factor structure survives the shift to general-purpose generative tools — where adoption is often bottom-up and individual before it is a firm decision — is untested by this review.

**Mention counts, not effects.** Tables II–V list which studies name each factor; nothing is weighted by effect size or study quality. The 70% failure and 20%→40% cancellation figures in the introduction are cited to Makarius et al. (2020), not produced by the review.

**Scopus only, journal articles only.** The authors acknowledge both as limits.
