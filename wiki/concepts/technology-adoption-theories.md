---
type: concept
title: Technology adoption theories
aliases: ["technology adoption theories", "adoption theories", "classical adoption theories", "TAM", "Technology Acceptance Model", "UTAUT", "UTAUT2", "Unified Theory of Acceptance and Use of Technology", "diffusion of innovations", "Diffusion of Innovation", "DOI theory", "Rogers' diffusion of innovations", "TOE framework", "technology-organization-environment", "technology–organization–environment framework"]
tags: [adoption-theory, tam, utaut, diffusion-of-innovations, rogers, toe-framework, tornatzky-fleischer, information-systems-research, firm-level, individual-level, ai-adoption]
confidence: 0.85
last_confirmed: "2026-10-08"
accessed_at: "2026-10-08"
source_count: 6
relationships:
  - type: supports
    target: enterprise-ai-adoption
    via: "supplies the explanatory models the adoption concept had lacked. The wiki described enterprise AI adoption through practitioner maturity frameworks and the dynamic-capabilities spine; these are the information-systems theories that predict whether a firm decides to adopt and whether its people use what was adopted"
quality_score: 1
---

# Technology adoption theories

## Working definition

The four models that information-systems and innovation research has used for decades to explain **why a technology gets adopted**: the **Technology Acceptance Model (TAM)**, the **Unified Theory of Acceptance and Use of Technology (UTAUT)**, **Rogers' diffusion of innovations (DOI)**, and the **technology–organization–environment (TOE) framework**. Until September 2026 the wiki had none of them. A 2026-09-17 auditable query on AI adoption models found the corpus explained [[enterprise-ai-adoption]] entirely through practitioner maturity frameworks and the [[dynamic-capabilities]] spine. This page was opened on 2026-09-18 with three peer-reviewed sources that apply the theories to AI.

The one distinction that organises everything else is the **level of analysis**:

| Level | Theories | Dependent variable | Typical sample |
|---|---|---|---|
| **Individual** | TAM, UTAUT (and UTAUT2), expectation–confirmation | a person's intention to use, and use | users, employees — very often students |
| **Innovation** | DOI | the rate at which an innovation spreads through a social system | adopters of one innovation |
| **Firm** | TOE (often with institutional theory or the resource-based view) | the organisation's decision to adopt | managers answering for their firm |

[[2025-01-08-khanfar-factors-influencing-ai-adoption-slr|Khanfar et al. (2025)]] state the assumption this split carries: firm-level and individual-level factors are treated "as independent of each other." Their review of 90 organisational AI-adoption studies argues they are not.

## The four models

*The one-line formulations below are how the ingested sources summarise the models. The original works — Davis (1989), Venkatesh et al. (2003), Rogers (2003, first edition 1962), Tornatzky & Fleischer (1990) — are not in the wiki. Where this page goes beyond what the ingested sources state, it says so.*

**TAM.** Two perceptions drive the intention to use a system: **perceived usefulness** (it will improve my job performance) and **perceived ease of use**. In [[2024-08-13-schwaeke-new-normal-ai-adoption-smes|Schwaeke et al.]] both appear as sub-factors of compatibility; Khanfar et al. find perceived usefulness the single most-cited individual factor in organisational AI adoption (31 of 90 studies), ahead of ease of use (19).

**UTAUT.** A consolidation of eight earlier acceptance models. Khanfar et al. use its labels as synonyms for TAM's — *performance expectancy* for perceived usefulness, *effort expectancy* for ease of use — and list social influence among the social factors. *Not stated in the ingested sources: UTAUT's fourth construct is facilitating conditions, its moderators are age, gender, experience and voluntariness, and UTAUT2 (2012) adds hedonic motivation, price value and habit for consumer settings.*

**DOI.** Diffusion is "the transmission of innovation over a period among the individuals within a social system", as [[2025-07-25-albishri-breaking-barriers-genai-adoption|Albishri et al.]] quote Rogers. Five attributes of an innovation reduce uncertainty and so drive adoption: **relative advantage**, **compatibility**, **complexity**, **trialability** and **observability**. Adoption passes through five stages: knowledge, persuasion, decision, implementation, confirmation. *Not detailed in the ingested sources: Rogers' adopter categories (innovators, early adopters, early majority, late majority, laggards) and the S-shaped diffusion curve.*

**TOE.** Three contexts shape an organisation's adoption decision: the **technological** (technologies inside and outside the firm), the **organisational** (size, structure, resources, people) and the **environmental** (industry, competitors, government). Schwaeke et al. note TOE's looseness as a strength and a weakness: researchers agree on the three contexts but "have identified unique sets of factors or measures for each specific technology or context being studied."

## What the AI-adoption literature does with them

**TOE as a map of the organisational literature.** [[2024-08-13-schwaeke-new-normal-ai-adoption-smes|Schwaeke et al. (2024)]] sort 106 studies of SME AI adoption into eight clusters under TOE's three contexts. Compatibility and culture are the largest (19 each), then resources (17) and infrastructure (16); ecosystem, competition and regulation trail with 8–9. The environmental context is the most thinly studied.

**TOE factors reach into employee adoption.** Khanfar et al. mark each factor as affecting either the firm's investment decision alone, or that decision **and** the employee's decision to use the system. Return on investment, cost and firm size are firm-only. System complexity, privacy and security, trust, task–technology fit, top-management support, innovation culture, training and role clarity reach both levels. Top-management support is the clearest case: it is budget for the firm and training and resources for the employee. [[2025-06-09-krakowski-human-centered-ai-field-experiment|Krakowski et al.]] are the experimental evidence for the bridge: four firm-set parameters decide whether the same AI system raises or lowers the performance of the same employees.

**DOI rewired as a chain.** Rogers treats the five attributes as parallel predictors. Albishri et al., testing generative-AI continued use among 342 managers in Saudi organisations, order them instead: relative advantage and compatibility → **trialability** → observability and social influence → continued use. Trialability mediates everything, and complexity moderates only the compatibility route. Compatibility is the stronger driver (β = 0.325 vs 0.256 for relative advantage), which fits compatibility being Schwaeke's largest cluster.

## How the theories relate to the wiki's dynamic-capabilities spine

The spine and TOE answer different questions. [[dynamic-capabilities]] and the [[warner-wager-process-model|Warner & Wäger process model]] explain how a firm **renews** itself — sensing, seizing, transforming. The adoption theories explain whether a firm or person **takes up** a technology. [[2025-06-15-cimino-ai-adoption-sustainable-growth-smes|Cimino et al. (2025)]] join them in one structural model: dynamic capabilities → AI adoption → performance. Their split of adoption into acceptance and implementation intensity is the bridge to this page, because acceptance is roughly what TAM, UTAUT and DOI's continued-use measures capture.

Schwaeke et al. make the one explicit link from the TOE side: their culture cluster credits leadership with "a strong role in the dynamic capabilities of firms through the ongoing development of new practices."

**The two joined in one model (added 2026-09-21).** [[2026-03-28-nguyen-ai-adoption-toe-dynamic-capabilities|Nguyen et al. (2026)]] put the two theories on either side of adoption, in a PLS-SEM study of 325 managers of Vietnamese firms that already use AI.

- **TOE explains how far a firm adopts.** Top leadership support (β = 0.286) and government support (β = 0.177) raise the level of AI adoption. Government support also works indirectly, through leadership support and perceived cost-effectiveness. Cost-effectiveness itself is only marginal (p = 0.063).
- **Dynamic capabilities explain what adoption becomes.** Adoption level leads to business-model innovation and sustainable competitive advantage, and those two carry most of the effect on firm performance. AI adoption also *amplifies* the advantage → performance link (interaction β = 0.123).

Two things limit what the model shows. First, it explains little on the outcome side: AI adoption accounts for 4% of the variance in business-model innovation and 6% in competitive advantage. Second, no dynamic capability is actually measured — the theory is invoked to interpret the outcome paths. Cimino et al. are the reverse on both counts: they measure the capability construct and put it *before* adoption. Read together, the two papers bracket adoption with capabilities on both sides. In both, the adoption measure that reaches performance is implementation depth, not readiness.

## Debates and supersession

- **From intention to value is an assumption, not a finding.** TAM, UTAUT and DOI studies measure intention and continued use. Albishri et al. draw organisational advice from continued-use intention. Cimino et al. find that firm-level readiness — the closest organisational analogue — does not reach economic or collaborative performance; only implementation does. Any use of these theories to argue business value inherits this gap. This is recorded as a `contradicts` edge between the two source pages.
- **Resistance: barrier or data?** Khanfar et al. file resistance to change as a negative factor, to be reduced by involving employees early. [[2026-05-07-carucci-resistance-as-data|Carucci (HBR, 2026)]] argues all resistance is data about the change and should be read, not overcome.
- **Do the theories survive generative AI?** Khanfar's search closed in July 2022 and Schwaeke's sample includes blockchain and IoT under "AI-related technologies"; both evidence bases predate ChatGPT. TOE puts the firm's decision first. Generative AI is often adopted bottom-up by individuals before any firm decision — a sequence the multi-level model has not been tested against. Albishri et al. is the one generative-AI study here, and it measures individuals.
- **Measurement quality.** The individual-level studies are almost all PLS-SEM on self-report surveys. Albishri's constructs separate only narrowly (HTMT up to 0.898 against a 0.90 ceiling), which inflates the paths between neighbouring constructs. The two TOE reviews count research attention, not effect sizes.
- **Sample skew (query observation, not a source claim).** A 2026-09-18 OpenAlex query found that about 36% of 2025–26 TAM/UTAUT papers on AI mention students and 13% teachers, against a few hundred each for employees, managers and firms. Most of the AI-acceptance evidence comes from convenience samples of people who adopt freely at no cost — the conditions least like enterprise adoption. The query is recorded in the 2026-09-18 log entry.

## Related concepts

- [[enterprise-ai-adoption]] — the practitioner side of the same question: maturity stages, leakage points, pilot-to-production ratios.
- [[dynamic-capabilities]] and [[warner-wager-process-model]] — the wiki's organisational spine; renewal rather than uptake.
- [[automation-vs-augmentation]] — what adoption is for, which none of the four theories addresses.

## Open questions

- ~~A paper integrating TOE with dynamic capabilities could not be retrieved.~~ **Resolved 2026-09-21**: [[2026-03-28-nguyen-ai-adoption-toe-dynamic-capabilities|Nguyen et al. (2026)]], ingested; see the section above. What it leaves open is a longitudinal design, which it concedes it cannot supply, and a measured capability construct on the outcome side.
- None of the three sources tests UTAUT or TAM on employees using generative AI at work. A study with an organisational sample, not students, would fill that gap.
- Does trialability matter as much when the tool is free and already on every desk? Rogers' attribute assumed trial was costly; for generative AI, trial is nearly costless, and Albishri's large trialability paths may measure something else. **Partly answered 2026-10-08:** in [[2026-09-30-lenk-karunakaran-stanford-hai-industry-conversation-instacart|Lenk's]] firm, a year of free access left use uneven, and a peer, not trial, moved it (see *Pioneers* below).


## Diffusion inside one firm (added 2026-09-21)

[[2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over|Krishna / IBM on Bain's Winning with AI, September 2026]]. IBM's internal rollout, as its CEO tells it, follows a diffusion curve at the level of process owners. Of about 200 processes, owners volunteered; five went first, then ten; about 60 were done in two and a half years; the next 70 were *"raring to go because they saw what their friends had done"*; the last 30–40 are *"recalcitrant."* Observability of peers' results drives the second wave, as in diffusion of innovations. For the laggards he offers three explanations without choosing between them: distrust of the AI, AI not ready, or genuinely harder processes. An anecdote, not a study; useful as a firm-internal illustration of a theory the page otherwise applies across firms.

## Pioneers: a causal estimate of peer diffusion inside one firm (added 2026-10-08)

[[2026-09-30-lenk-karunakaran-stanford-hai-industry-conversation-instacart|Lenk (Instacart Economics) at a Stanford HAI seminar, September 2026]] presents a working paper that turns the IBM anecdote above into an estimate. Engineering and data-science teams (over 1,000 employees in about 200 teams) had free access to agentic AI tools throughout 2025. A **pioneer** is the first team member to cross a heavy-use threshold, roughly eight days of use in two weeks. Pioneers emerged at staggered times, which a staggered difference-in-differences design exploits. Teammates' use rises by about 4.6 days after a pioneer emerges, with no pre-trend; pioneers account for about 23% of the year's rise in use; experiments, launches and resolved tickets rise too.

Three findings bear on the theories on this page:
- **Observability through a person.** Pioneers do not differ in seniority; they differ in earlier enthusiasm for the firm's chatbot. Their influence is larger when they hold authority, which Lenk attributes in the Q&A to personal trust rather than a mandate. That is the opinion-leader role in diffusion of innovations, estimated rather than described.
- **Trial was free and use still varied.** Access cost nothing for a year; what moved use was a colleague (see the open question on trialability above).
- **Task complexity changes who can transmit.** For experiments, only pioneers already skilled at experimentation raised their teammates' output; for routine ticket work any pioneer did. Adoption of the tool and transfer of the skill to use it on a hard task travel together.

In the Q&A, Karunakaran adds why peers matter more for generative AI than for ERP: an ERP system has features a vendor can teach, while generative AI is open-ended and its valuable uses must be discovered. Citing his colleague Michael Bernstein, he says it suits *"rough-edged problems"* with many right answers, which call for social learning. Limits: one firm, outcome measures that are proxies for value, and a paper not ingested.
