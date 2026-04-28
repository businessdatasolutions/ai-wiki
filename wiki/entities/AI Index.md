---
type: entity
kind: project
aliases: ["AI Index", "AI Index Report", "Stanford AI Index"]
tags: [ai-index, stanford-hai, ai-research, annual-report]
parent: "[[Stanford HAI]]"
since: 2017
---

# AI Index

The **AI Index** is an independent initiative at [[Stanford HAI]] that produces an annual report on the state of artificial intelligence. Conceived in 2017 within the [[One Hundred Year Study on AI]] (AI100). The 2025 edition was the 8th annual.

Mission (per the report): equip policymakers, journalists, executives, researchers, and the public with **accurate, rigorously validated, globally sourced data** on AI's development, adoption, and impact.

## What it tracks

| Domain | Mapped to wiki concept |
|---|---|
| Research and Development (publications, patents, models) | [[foundation-models]] |
| Technical Performance (benchmarks) | [[ai-benchmarks]] |
| Responsible AI (incidents, transparency, governance) | [[responsible-ai]] |
| Economy (adoption, investment, jobs, robots) | [[enterprise-ai-adoption]] |
| Science and Medicine | _no concept page yet_ |
| Policy and Governance | _no concept page yet_ |
| Education | _no concept page yet_ |
| Public Opinion | _no concept page yet_ |

## Editions

Only the 2025 edition has been ingested into this wiki so far.

| Year | Edition | Status |
|---|---|---|
| 2017–2024 | 1–7 | Not yet ingested |
| 2025 | 8 | [[2026-04-28-ai-index-report-2025|Ingested]] — adds AI hardware deep-dive, novel inference cost estimates, fresh corporate adoption of [[responsible-ai]] data, expanded science/medicine coverage |

(Earlier editions to be filled in as / if they're ingested.)

## Steering Committee (2025 edition)

- **Chair:** [[Raymond Perrault]] (SRI International)
- **Chair-elect:** [[Yolanda Gil]] (USC, Information Sciences Institute)
- **Members:** [[Erik Brynjolfsson]] (Stanford), [[Jack Clark]] (Anthropic, OECD), [[John Etchemendy]] (Stanford), [[Katrina Ligett]] (Hebrew University), [[Terah Lyons]] (JPMorgan Chase & Co.), [[James Manyika]] (Google, University of Oxford), [[Juan Carlos Niebles]] (Stanford, Salesforce), [[Vanessa Parli]] (Stanford), [[Yoav Shoham]] (Stanford, AI21 Labs), [[Russell Wald]] (Stanford), [[Tobi Walsh]] (UNSW Sydney)
- **Editor-in-Chief:** [[Nestor Maslej]] (Stanford)

## Data partners (2025 edition)

[[Accenture]], [[Center for Research on Foundation Models]], Digital Policy Alert, [[CSET]] (Center for Security and Emerging Technology), CSTA, [[Epoch AI]], GitHub, [[International Federation of Robotics]] (IFR), Kapor Foundation, [[Lightcast]], LinkedIn, [[McKinsey & Company]], PIT-UN, RAISE Health, studyportals, [[Quid]].

## Supporting funders (2025 edition)

Google, NSF (National Science Foundation), [[OpenAI]], Open Philanthropy, [[Quid]].

## Methodological notes

- The report uses external surveys (notably [[McKinsey & Company]]'s Global AI Survey for §4.4 corporate-activity data) rather than original surveys for most adoption and use-case data. When citing AI Index "78% of orgs use AI," it's worth noting the underlying instrument is McKinsey's, not a Stanford instrument.
- The 2025 report acknowledges using ChatGPT and Claude for copy-editing the drafts; original analysis is human.
- License: CC BY-ND 4.0. Public data and chart files released alongside the report.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "ai-index")
SORT file.name ASC
```

## Open questions

- Year-over-year stability of methodology (e.g., does the 78% adoption number compare apples-to-apples with prior editions, given the McKinsey instrument may have changed).
- The interactive **Global AI Vibrancy Tool** (~30 countries) — is it useful enough to file as its own resource page once we engage with it?
