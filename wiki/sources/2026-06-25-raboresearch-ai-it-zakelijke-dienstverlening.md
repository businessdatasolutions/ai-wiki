---
type: source
kind: article
title: "Hoe AI de sectoren IT en zakelijke dienstverlening verandert"
author: ["Mark van Kampen", "Reinder Koelewijn", "Jesse Groenewegen", "Floris Jan Sander"]
publisher: "RaboResearch (Rabobank)"
url: "https://www.rabobank.nl/kennis/d011532294-hoe-ai-de-sectoren-it-en-zakelijke-dienstverlening-verandert"
date_published: 2026-06-25
date_ingested: 2026-06-27
length: "~2,400-word web article + 13 figures (full prose via Zotero extract; figure data read from the live page)"
raw: "../../raw/articles/hoe-ai-de-sectoren-it-en-zakelijke-dienstverlening-verandert.md"
tags: [raboresearch, rabobank, netherlands, ai-employment-effects, automatiseringspotentieel, occupational-exposure, ilo-gmyrek, productivity, productiviteitspotentieel, it-sector, business-services, zakelijke-dienstverlening, cbs, task-level-automation, predictive-generative-agentic-ai, eu-comparison, personeelsschaarste, accountancy, advocatuur, consultancy, software-development]
dynamic_capabilities:
  - digital-sensing/digital-scenario-planning
  - digital-sensing/digital-mindset-crafting
  - digital-transforming/improving-digital-maturity
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-04-28-brynjolfsson-canaries-coal-mine
    via: "occupational-exposure measurement of automation potential (ILO/Gmyrek) corroborating the entry-level/compositional shift — RaboResearch's NL/sector vantage echoes the executing→advisory role shift and the decline of junior roles that the US ADP-payroll Canaries finding documents"
  - type: supports
    target: 2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces
    via: "reshape ≫ replace at sector altitude — RaboResearch finds roles shift (accountants, lawyers, consultants, developers move from executing to advisory/judgment work) and value concentrates in complex judgment while junior/instap tasks decline, not aggregate elimination"
  - type: supports
    target: 2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai
    via: "method-cousin: both build occupational-exposure measures of AI capability (Massenkoff & McCrory weight Eloundou task ratings by AEI usage; RaboResearch maps Gmyrek et al. ILO task scores onto CBS occupations) and both stress potential ≫ realised deployment"
---

# Hoe AI de sectoren IT en zakelijke dienstverlening verandert

> **In het kort (RaboResearch's own framing):** In de sectoren IT en zakelijke dienstverlening wordt AI gezien als een belangrijke versneller om de productiviteit te verhogen en personeelstekorten op te vangen. Het automatiseringspotentieel is groot: zo'n **86% van IT-taken** en **64% van taken in de zakelijke dienstverlening** kan (deels) worden geautomatiseerd. AI zal vooral routinematige, analytische en tekstgebaseerde werkzaamheden sterk beïnvloeden. Experimenten tonen aanzienlijke productiviteitswinsten van circa **10% tot soms meer dan 50%**, afhankelijk van taak en toepassing. Bedrijven die AI goed integreren kunnen hun productiviteit structureel verhogen en personeelstekorten opvangen; bedrijven die dit niet doen verliezen terrein.

## TL;DR

A Dutch-market sector study from **RaboResearch** (Rabobank's research arm), published 25 June 2026, applying the **ILO occupational-exposure methodology** ([[entities/Erik-Brynjolfsson|Gmyrek et al. 2025, ILO Working Paper 140]] — *not* Brynjolfsson; see note below) to Dutch CBS occupation data to estimate AI's automation and productivity potential for the **IT** (Informatie & communicatie) and **zakelijke dienstverlening** (business services) sectors. It is the wiki's first **Dutch national / sectoral** source on AI labour and productivity, and its first source to quantify automation potential against the **CBS Nederlandse Beroepsclassificatie**. The substantive payload is in 13 figures: a task-level automation-potential breakdown (86% IT / 64% business services), a per-business-function decomposition, a 18-study productivity-gain spread that spans **+73% down to negative**, NL-vs-EU adoption rates, and per-occupation automation rankings. The closing prescription names **three conditions** for capturing the potential — strategic ownership, a data/IT/process base, and governance/trust — that map cleanly onto the [[concepts/warner-wager-process-model|Warner & Wäger]] digital-transformation primitives.

## What was actually ingested

- **Full article prose** came through the Zotero local-API extract (`fulltext_source: zotero-extracted`) — the complete running text, the *In het kort* summary, all section prose, the *Onderzoeksverantwoording* appendix, and the single literature reference (Gmyrek et al. 2025).
- **The 13 figures were image charts** dropped by the text extract. Because the figures carry the load-bearing quantitative content, they were fetched from the live page (the rabobank.nl host bot-blocks plain fetchers; rendered in a real browser, the `media.rabobank.com` CDN serves the chart images directly) and read visually. Figure data below is transcribed from those charts (Figuren 4, 5a, 5b, 6, 7a, 9a, 9b read in full; Figuren 1–3, 7b, 8a, 8b are context/trend charts adequately described by the body prose).
- **Honest scoping:** this is a ~2,400-word web research article, not a long report. No body chapters are deferred — the whole article is ingested.

## Key findings

### Automation potential at task level (Figuur 4)

RaboResearch scores each task in the Dutch occupation classification on a 0–1 GenAI-automatability scale (mapping Gmyrek et al.'s ILO/ISCO task scores onto the CBS Nederlandse Beroepsclassificatie), then bins tasks into four categories: **hoog potentieel** (score > 0.5), **potentieel** (0.375–0.5), **laag potentieel** (0.2–0.375), **niet mogelijk** (< 0.2). "(Hoog) potentieel" = the first two bins combined.

| Sector | Hoog | Potentieel | (Hoog) potentieel | Laag | Niet mogelijk |
|---|---:|---:|---:|---:|---:|
| **Informatie & communicatie (IT)** | 49% | 37% | **86%** | 11% | 3% |
| **Zakelijke dienstverlening** | 33% | 31% | **64%** | 27% | 9% |
| Totale economie | ~22% | ~22% | ~44% | ~28% | ~28% |

IT and business services are among the **most exposed** sectors in the whole economy (financial services is the only sector with a comparable or higher share); the least-exposed sectors are agriculture, horeca, and construction. The scores are a measure of *potential when the technology is further developed and implemented* — not current deployment.

### Where the potential sits, by business function (Figuren 5a / 5b)

Decomposing each sector's high-potential tasks into Eurostat/CBS business functions:

- **IT (of all tasks in the sector):** ICT **41%**, Marketing/verkoop **10%**, R&D/innovatie **9%**, Anders 7%, Productie/serviceprocessen 7%, Administratie 6%, Boekhouding 5%, Logistiek 2% (≈86% total).
- **Zakelijke dienstverlening:** Boekhouding/financieel beheer **14%**, Marketing/verkoop **10%**, ICT **9%**, Productie/serviceprocessen 9%, Anders 8%, Administratie 7%, R&D 5%, Logistiek 2% (≈64% total).

### The productivity-gain spread (Figuur 6) — a task-level vs firm-level gap

RaboResearch's clearest contribution is a single chart collating ~18 productivity studies, which lays the **[[concepts/micro-productivity-trap|task-level-vs-firm-level gap]]** bare in one view — task-level/occupational experiments cluster high, firm-level studies cluster near zero:

| Study (domain) | Reported gain |
|---|---|
| Ju & Aral 2025 (advertising) | **+73%** |
| Peng, Kalliamvakou, Chion & Demirer 2023 (software dev) | +55.8% |
| Gambacorta, Qiu, Shan & Rees 2024 (software dev) | +55% |
| Yeverechayou, Mayya & Oestericher-Singer 2024 (software dev) | +37–55% |
| Noy & Zhang 2023 (writing) | +0.8 SD |
| Goldman Sachs Research 2026 (firm-level) | +30% |
| Cui, Demirer, Jaffe, Musolff, Peng & Salz 2025 (software dev) | +26% |
| Dell'Acqua et al. 2025 (consulting) | +25.1% |
| Paradis et al. 2024 (software dev) | +21% |
| METR 2025 (software dev) | +18% |
| Fang, Yuan, Zheng, Donati & Sarvary 2025 (e-commerce) | +16% |
| Brynjolfsson, Li & Raymond 2024 (customer service) | +14% |
| Dell'Acqua et al. 2024 (product dev) | quality+ |
| Bloom, Barrero, Davis et al. 2026 (**firm-level**) | **+1.4%** |
| Otis, Clarke, Delecourt, Holtz & Koning 2023 (entrepreneurship) | ~0% |
| Babina, Fedyk, He & Hodson 2023 (**firm-level**) | **0% TFP** |
| Atlassian Research 2025 (**firm-level**) | **96% report no ROI** |
| Niederhoffer, Teevan & Jaffe 2025 (knowledge work) | −2 units/incident |

RaboResearch's own caveat is explicit: *"het is onzeker of deze effecten standhouden buiten experimenten"* — implementation, integration and skills determine whether experimental gains survive into daily practice. (Note: the METR row is plotted **+18%**; METR's own widely-cited July-2025 RCT found experienced OSS developers were ~19% *slower* with AI — the sign is worth flagging as a possible RaboResearch reading/metric difference, not taken at face value.)

### Netherlands ahead of the EU average, not in the lead group (Figuren 7a/7b)

On a CBS enterprise survey (firms >10 employees), Dutch firms in both sectors use AI **above the EU average** in every business function, but **below the EU leader** in every function. For business services: e.g. administratieve processen NL **25%** vs EU-leader 33% vs EU-avg 14%; marketing NL **16%** vs 31% vs 10%.

### Per-occupation automation potential (Figuren 9a/9b)

- **Business services** (most → least exposed): boekhoudkundig medewerkers (~100% hoog), secretaresses, administratief medewerkers, receptionisten/telefonisten, financieel specialisten, boekhouders, accountants — down to architects and managers (mid), and **schoonmakers / beveiligingspersoneel at the bottom** (mostly *niet mogelijk* / *laag*).
- **IT** (most → least exposed): callcentermedewerkers outbound (~88% hoog), databank-/netwerkspecialisten (~70%), gebruikersondersteuning ICT (~56%), marketing/PR/sales-adviseurs (~55%), **software- en applicatieontwikkelaars (~42% hoog, ~100% (hoog) potentieel)** — down to managers ICT, procesoperators, and algemeen directeuren (no *hoog*, mostly *potentieel/laag*).

The pattern: routine administrative, financial, and text-based roles are most exposed; physical and top-management roles least. Senior developers shift toward quality assurance, architecture and IT governance ("context waarbinnen AI en agents opereren"); junior/instap functions decline.

### The three AI types and the three conditions

RaboResearch distinguishes **Predictive AI** (decades old — capacity planning, fraud detection), **Generative AI** (post-2022 — documentation, code generation), and **Agentic AI** ((semi-)autonomous — resolving incidents, continuously testing software) (Figuur 3). It names **three conditions** for an organisation to capture the potential:

1. **Strategic ownership** — leadership positions AI explicitly in the business strategy and actively drives employee adoption, supported by new core skills (data literacy, critical AI use).
2. **A data/IT/process base** — AI only delivers value when data is reliable, secure and well-governed *and* applications are embedded in daily workflows; many initiatives fail on poor integration and weak fit to the business context.
3. **Governance, risk management and trust** — clear frameworks for privacy, ethics and explainability so employees, clients and regulators can trust AI-supported services (see [[concepts/responsible-ai|responsible AI]]).

## Dynamic-capabilities reading (Warner & Wäger)

The source is tagged against four [[concepts/warner-wager-process-model|W&W process-model]] cells:

- **`digital-sensing/digital-scenario-planning`** — the study *is* a scenario-planning artifact: it scouts AI's task-level automation signal, interprets a forward scenario for two sectors, and formulates the strategic implication (*"groei komt niet langer uit extra mensen, maar uit slimmer werken"*).
- **`digital-sensing/digital-mindset-crafting`** — condition 1 names exactly this work: leadership establishing AI as part of strategy and *promoting a digital/AI mindset* across the workforce, underpinned by new core skills.
- **`digital-transforming/improving-digital-maturity`** — condition 2 (a reliable, governed data/IT/process base; embedding AI in workflows; leveraging digital knowledge inside the firm) and condition 3 (governance of sensitive data) are digital-maturity work.
- **`contextual/external-triggers`** — the study's macro framing is a set of external pressures: structural **personeelsschaarste** (high vacancy rates), a consolidation wave squeezing margins, and rising client expectations at lower cost — the triggers making productivity growth a necessity rather than an option.

(The governance/trust condition has no dedicated W&W cell; it is folded into *improving-digital-maturity* prose above and linked to [[concepts/responsible-ai|responsible AI]] rather than stretching the vocabulary.)

## Linked entities and concepts

- **Concepts:** [[concepts/ai-employment-effects|AI employment effects]], [[concepts/automation-vs-augmentation|automation vs augmentation]], [[concepts/enterprise-ai-adoption|enterprise AI adoption]], [[concepts/micro-productivity-trap|micro-productivity trap]], [[concepts/generative-ai|generative AI]], [[concepts/ai-agents|AI agents]], [[concepts/responsible-ai|responsible AI]], [[concepts/warner-wager-process-model|Warner & Wäger process model]].
- **Entity (incidental):** [[entities/Erik-Brynjolfsson|Brynjolfsson]] appears only as one row in the productivity table (Brynjolfsson, Li & Raymond 2024, customer service, +14%); the study's actual methodological anchor is **Gmyrek et al. (2025), ILO**.
- **Dangling** (single-source authors, deferred per the second-source promotion rule): Mark van Kampen (Sectormanager Tech, Media & Telecom), Reinder Koelewijn (Sectormanager Commercial Services), Jesse Groenewegen, Floris Jan Sander. **RaboResearch / Rabobank** and **CBS** and the **ILO / Gmyrek et al.** working paper are likewise single-source mentions, not yet promoted to entity pages.

## Source-to-source relationships

- **supports → [[sources/2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson, Chandar & Chen — Canaries in the Coal Mine?]]** — both measure AI's labour impact through occupational exposure; RaboResearch's Dutch sector vantage (executing→advisory role shift, declining junior/instap tasks, value concentrating in complex judgment) corroborates the US ADP-payroll entry-level/compositional finding from a different instrument and geography.
- **supports → [[sources/2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces|BCG — AI Will Reshape More Jobs Than It Replaces]]** — same *reshape ≫ replace* headline at sector altitude: roles transform (accountants, lawyers, consultants, developers move up the value chain) and junior tasks decline, rather than aggregate job elimination.
- **supports → [[sources/2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai|Massenkoff & McCrory / Anthropic — Labor Market Impacts of AI]]** — method cousins: both convert task-level capability ratings into an occupational-exposure measure (Anthropic weights Eloundou ratings by AEI usage; RaboResearch maps Gmyrek/ILO task scores onto CBS occupations) and both stress that *potential exposure ≫ realised deployment*.
- *Considered and deferred (no typed edge):* [[sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|MGI Agents, Robots, and Us]] (>50% of work-hours theoretically automatable, shift-not-elimination) and [[sources/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Evans]] (lump-of-labor counter-frame) are thematic neighbours but already well-connected through the [[concepts/ai-employment-effects|AI employment effects]] concept page; no additional source-to-source edge added.

## Provenance

Acquired from the local Zotero `ai-wiki` collection via `zotero-acquire` (`zotero_item_key: 7A3RK8MR`, itemType `webpage` → `raw/articles/`). The raw stub carries the Zotero text extract; figure data was read from the live rabobank.nl page at Process time. Original article: RaboResearch, 25 June 2026.
