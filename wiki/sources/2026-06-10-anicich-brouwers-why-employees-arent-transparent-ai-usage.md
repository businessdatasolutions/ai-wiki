---
type: source
kind: article
title: "Why Employees Aren't Transparent About Their AI Usage"
author: ["Eric Anicich", "Jeslyn Brouwers"]
publisher: "[[Harvard Business Review]]"
section: "HBR.org (AI and Machine Learning)"
url: "https://hbr.org/2026/06/why-employees-arent-transparent-about-their-ai-usage"
date_published: 2026-06-10
date_ingested: 2026-06-16
length: "~3,000 words (PDF, pdftotext extract)"
raw: "../../raw/articles/why-employees-arent-transparent-about-their-ai-usage.md"
zotero_item_key: WXQ3Y3IA
tags: [ai-knowledge-hiding, shadow-ai, organizational-trust, psychological-safety, enterprise-ai-adoption, micro-productivity-trap, disclosure-culture, side-quests, amy-edmondson, exploratory-testing, hbr]
dynamic_capabilities:
  - contextual/internal-barriers
  - contextual/internal-enablers
  - strategic-renewal/organizational-culture
relationships:
  - type: instance-of
    target: ai-knowledge-hiding
  - type: supports
    target: 2026-04-28-mit-sloan-ai-maturity
    via: "both locate the binding constraint on AI value capture in organizational/human factors rather than technology — Anicich & Brouwers cite a Stanford 51-deployment study finding 77% of the hardest adoption challenges are non-technical (incl. earning trust from skeptical teams), the same human-maturity gap the MIT Sloan maturity work documents"
  - type: supports
    target: 2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life
    via: "develops the 'trust gap' Randell & Gousset name as the binding adoption constraint — here the gap is between employee and employer (will my disclosed AI method be used against me?), and trust/psychological safety are the strongest predictors of whether workers disclose vs. hide their workflows"
---

# Why Employees Aren't Transparent About Their AI Usage

> As employees increasingly develop valuable AI workflows through private experimentation, many are choosing not to share what they've learned—not mainly because of weak governance or inadequate tools, but because they don't trust what their organizations will do with that knowledge once it becomes visible. Survey and interview data suggest that organizational trust and psychological safety are among the strongest predictors of whether workers disclose or withhold AI-related methods… capturing AI's collective productivity gains depends less on increasing adoption than on creating a culture in which disclosure feels safe, worthwhile, and professionally rewarding.
>
> *— [Harvard Business Review summary](https://hbr.org/2026/06/why-employees-arent-transparent-about-their-ai-usage) (Eric Anicich & Jeslyn Brouwers, 10 June 2026)*

A Harvard Business Review article by **Eric Anicich** (USC Marshall) and **Jeslyn Brouwers** arguing that the chief obstacle to capturing AI's collective gains is not governance or tooling but **organizational trust** — employees rationally **hide** the AI workflows they discover. It is the primary source for the new [[ai-knowledge-hiding]] concept and a trust/culture complement to the wiki's [[enterprise-ai-adoption]] and [[micro-productivity-trap]] pages.

## TL;DR

- **The construct — *AI knowledge hiding* / "the suppression of solutions."** Organizational-silence research has focused on hiding *problems* (bad news, risks). AI introduces hiding of *solutions*: when an individually-discovered prompt sequence cuts a 3-hour task to 20 minutes and is trivial to conceal, silence becomes **economically consequential** in a new way. Productivity gains "used to scale by default" (embedded in shared systems); now the most valuable gains are **portable, private, and easy to keep to yourself**.
- **Trust is the driver, not governance.** A KPMG/University of Melbourne study (48,000+) found **57% admit hiding their AI use**. The authors' own survey of **604 daily-AI users**: **30.3%** intentionally withheld AI knowledge; the lowest-trust quartile was **~4× more likely** to hide than the highest (**47% vs 14%**); psychological safety showed the same pattern (**45% vs 17%**). Trust survived controls for job insecurity, competitiveness, fairness, AI policy, sanctioned tools, age, tenure, etc. — and operated **largely through psychological safety**. Having an AI policy or approved tools, alone, predicted nothing.
- **Three rational costs of disclosure:** **reputational** (seen as less capable; "the work was discredited because a computer did it"), **workload** ("if I automate A and B, they make me do D, E, F" — efficiency treated as spare capacity to fill, the [[micro-productivity-trap]] at the individual level), and **replaceability** (enterprise tools log prompts/workflows → your method gets extracted and routed to a cheaper replacement; one cited professor advises using *personal* AI tools so learning "stays with you").
- **The misclassification at the core.** Per **Amy Edmondson**, organizations confuse *praiseworthy exploratory testing* with *blameworthy deviance* — and so punish the experimentation they most need. A Stanford Digital Economy Lab study of **51 enterprise deployments** found **77% of the hardest adoption challenges were non-technical**.
- **Leader prescriptions:** (1) **earn the disclosure you want** — remove ambiguity; lightweight templates / "show me how you built this" demos, not process memos; attach the contributor's name. (2) **stop taxing efficiency gains** — an explicit norm for how saved time is reinvested. (3) **reward multiplier behavior** — credit for *adopted* workflows + team incentives + pro-sharing norms (comparison-heavy climates amplify retaliatory hiding). (4) **legitimize experimentation, then surface it** — Anthropic's Claude Code **"side quests"** ≈ 3M's 15% / Google's 20% time. (5) **treat disclosure as a contribution** — the manager's reaction in the 30 seconds after someone shows their work is "the most decisive trust signal"; don't convert one demo into a standing obligation to bring everyone up to speed. (6) **a tooling warning** — sanctioned tools log work, which both *credits* and *extracts*; logging amplifies the trust→hiding relationship.

## What was actually ingested

Full article (~3,000 words, `pdftotext` extract of the HBR PDF). All quantitative claims (KPMG/Melbourne 57%, the authors' 604-respondent survey, the 104-study meta-analysis, the Stanford 51-deployment 77%, the Anthropic 69% social-stigma figure) are reported as the source states them; the wiki treats them as second-hand to the underlying studies.

## How this source touches the wiki (dynamic capabilities)

- **contextual/internal-barriers** — low organizational trust, weak psychological safety, job insecurity, and competitive internal climates are the *barriers* that suppress AI-knowledge sharing; the article's central finding is that these dominate formal-infrastructure factors.
- **contextual/internal-enablers** — trust + psychological safety + a *shared sanctioned toolset* + legitimized experimentation ("side quests") + multiplier rewards are the *enablers* that convert private workflows into collective capability ("trust creates the willingness to share; a common toolset creates the opportunity").
- **strategic-renewal/organizational-culture** — the thesis that "AI stress-tests culture" and that disclosure culture (not adoption rate) is the real lever is a culture-renewal claim: capturing AI's gains requires changing the implicit deal about what happens to employees who reveal how they work.

## Linked entities and concepts

- Concepts: [[ai-knowledge-hiding]] (primary source), [[enterprise-ai-adoption]] (trust/culture as the binding constraint), [[micro-productivity-trap]] (efficiency-tax at the individual level), [[durable-skills]] / [[ai-deskilling]] (the replaceability fear), [[responsible-ai]] (the tooling-surveillance trade-off).
- **Dangling** (single-source mention, deferred per author-entity rule): Eric Anicich, Jeslyn Brouwers (authors), Amy Edmondson (psychological-safety / exploratory-testing framing), Matthew Call.

## Source-to-source relationships

- **Supports** [[2026-04-28-mit-sloan-ai-maturity]] — both put the binding constraint on AI value capture in **human/organizational** factors, not technology; the Stanford "77% of hard adoption challenges are non-technical" figure is the same maturity gap from the disclosure-culture angle.
- **Supports** [[2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life]] — develops the **"trust gap"** they name as the binding adoption constraint, specifying it as an *employee↔employer* trust problem with measured predictors (trust/psychological safety).
- Other adoption-cluster neighbours considered — [[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees|Kropp/BCG]], [[2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset|Argenti/HBR]], [[2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler|Beutler/OpenAI]] — share the [[enterprise-ai-adoption]] concept but no direct source-to-source edge added: this source's specific claim (trust→disclosure of *solutions*) is distinct from theirs and is carried via the concept page. *(Not every co-occurrence is a relationship.)*
