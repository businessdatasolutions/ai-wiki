---
type: entity
kind: person
aliases: ["Aswath Damodaran", "Damodaran"]
tags: [aswath-damodaran, nyu-stern, valuation, corporate-finance, cost-of-capital, equity-risk-premium, dcf, anthropic, ipo]
affiliation: "NYU Stern School of Business (his slides, spreadsheets and datasets are hosted on pages.stern.nyu.edu)"
role: "Finance professor; teaches corporate finance and valuation; publishes valuations, slides and datasets on his blog and YouTube channel"
confidence: 0.75
last_confirmed: "2026-11-16"
accessed_at: "2026-11-16"
source_count: 2
---

# Aswath Damodaran

**Aswath Damodaran** is a professor of finance at NYU Stern who teaches three classes in finance, among them corporate finance and valuation. He publishes his valuations with slides, spreadsheets and datasets on his blog and YouTube channel, and values companies as an investor *"for an audience of one."* Promoted to an entity page on 16 November 2026 under the second-source rule: he is the author, channel and sole speaker of both sources below.

## Role in the wiki

1. [[2026-10-28-damodaran-anthropic-ipo-valuation|The Anthropic IPO valuation (28 Oct 2026)]]: a reading of [[Anthropic]]'s S-1 prospectus and his own valuation of its equity at about $1.48 trillion, made before the shares listed, with every input stated, the compute commitments counted as debt, and a critical account of the five-class share structure.
2. [[2026-11-03-damodaran-anthropic-valuation-feedback-loop|The follow-up (3 Nov 2026)]]: his inputs ranked by fragility, viewers' alternative valuations, and a lecture on the cost of capital and on hurdle rates set above market levels.

## Method, as he describes it

- **Story to numbers.** A valuation turns a story into inputs: target revenues, end-state margins, reinvestment and risk. Growth rates are *"just a pathway to an end."* Of his own inputs: *"I'm going to be wrong 100% of the time."* He asks viewers to enter their own inputs, offers a "3P test" for their stories (possible, plausible, probable), and names the last step of his process *"keeping the feedback loop open."*
- **Small models.** *"With my 15 to 20 line items, I know exactly where each input goes."*
- **Price and value.** Anthropic's stock, at its IPO, *"will be traded, it won't be valued"*; he buys only when the price falls far enough below his value.
- **Risk in its place.** He prices failure risk separately and keeps the cost of capital within market-tested bounds: historical returns, the market-implied expected return, and sector ranges.
- **Governance as power.** Corporate governance is *"a measure of how much power shareholders have to change the way a company is run when they don't like the way it's run."*

## Datasets linked from the sources (not ingested)

Cost of capital by US industry group (`waccUS.xlsx`), historical returns on US stocks (`histretSP.xlsx`), and the history of market-implied expected returns (`histimpl.xlsx`), all on pages.stern.nyu.edu.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "aswath-damodaran")
SORT file.name ASC
```

## Open questions

- Two earlier sessions he refers to, on AI as a business and on pricing the Anthropic IPO, are not in the wiki.
- His Anthropic spreadsheet and the S-1 are not ingested. The two sessions give the present value of Anthropic's compute commitments as $473 billion and $373 billion, and the difference is unresolved.
