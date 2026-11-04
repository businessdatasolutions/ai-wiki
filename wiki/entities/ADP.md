---
type: entity
kind: organization
aliases: ["ADP", "ADP Research", "Automatic Data Processing"]
tags: [adp, adp-research, payroll-data, labor-market-data, canaries, stanford-digital-economy-lab, national-employment-report]
confidence: 0.8
last_confirmed: "2026-11-04"
accessed_at: "2026-11-04"
source_count: 4
---

# ADP

The largest payroll processor in the United States, paying more than 26 million US workers. **ADP Research** is its research arm, which publishes the monthly National Employment Report. Promoted to an entity on 4 November 2026, when ADP Research became co-author of a source in the wiki. It had been named as a data provider in three sources before that.

## Role in the wiki

ADP's payroll records are the data behind the corpus's most-cited empirical claim about AI and jobs: that early-career workers in the most AI-exposed occupations are losing employment. Everything in the wiki on that claim from ADP's side comes through its partnership with the [[Stanford Digital Economy Lab]].

- [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson, Chandar & Chen (2025)]] — the *Canaries in the Coal Mine* paper, built on ADP microdata for January 2021 to July 2025.
- [[2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity|Brynjolfsson on McKinsey Talks Talent]] — the lab director on the monthly ADP series: the early-career decline *"up to 16 or 17% now."*
- [[2026-10-07-richardson-reuters-econ-world-ai-at-work|Richardson on Reuters Econ World]] — Nela Richardson, ADP's chief economist, on the partnership from ADP's side: tasks rather than jobs, and wage premiums for job switchers.
- [[2026-10-21-stanford-del-canaries-dashboard|Canaries Dashboard]] — the monthly public dashboard of the series, co-authored by ADP Research and the lab. Data through September 2026.

## What the data can and cannot show

- **Strengths.** Payroll records, not survey answers. Monthly, with little lag. Granular enough to track 730+ occupations by age.
- **Limits.** ADP's client base does not match the US economy's firm distribution. The Canaries work uses a five-year balanced panel of firms, so it excludes firm entry and exit and firms changing payroll provider. It departs from the methodology of ADP's own National Employment Report. The dashboard says its sample *"represents neither the entire U.S. labor market nor the universe of firms using ADP payroll services."*
- **Independence.** Richardson speaks for the data's supplier, so her account is not an independent check on the Canaries findings. The Reuters source page makes the same point.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```
