---
type: source
kind: video
title: "The Prospectus is here: My (but not the) Anthropic IPO Valuation!"
author: ["Aswath Damodaran"]
publisher: "Aswath Damodaran (YouTube channel); solo session by Aswath Damodaran, professor of finance at NYU Stern (slides and spreadsheet hosted on pages.stern.nyu.edu)"
url: "https://www.youtube.com/watch?v=cd1xrO2q9HU"
date_published: 2026-10-28
date_ingested: 2026-11-16
length: "~47:44 minutes (transcript ~365 lines + 12 stills; ASR auto-generated track, no chapters)"
raw: "../../raw/videos/the-prospectus-is-here-my-but-not-the-anthropic-ipo-valuation.md"
stills: "../../raw/videos/the-prospectus-is-here-my-but-not-the-anthropic-ipo-valuation.stills.md"
tags: [aswath-damodaran, nyu-stern, anthropic, ipo, s-1-prospectus, valuation, dcf, narrative-and-numbers, run-rate, gross-vs-net-revenue, customer-concentration, compute-costs, compute-commitments, economies-of-scale, stock-based-compensation, total-addressable-market, premium-vs-mass-market, operating-margin, sales-to-capital, cost-of-capital, failure-risk, regulatory-risk, corporate-governance, dual-class-shares, public-benefit-corporation, benefit-trust, lock-up, circular-financing, openai, broadcom]
dynamic_capabilities:
  - strategic-renewal/business-model
relationships:
  - type: supports
    target: 2026-08-18-covello-gs-new-models-ai-investment-landscape
    via: "both address the economics of the AI build-out from an investor's seat: Covello asks whether enterprise buyers make or save money on AI and separates circular financing used as a discount from financing a customer could not do without; Damodaran values one frontier lab from its prospectus, counts its contractual compute commitments as debt, and calls the industry's circularity self-interest that makes the numbers opaque"
    confidence: 0.7
  - type: supports
    target: 2026-10-15-lin-stanford-ai-club-building-in-the-ai-era
    via: "both discuss circular money among AI companies and the obligations behind compute: Lin compares NVIDIA's investments in its customers to bank lending and names data-centre debt as the larger concern; Damodaran calls the circularity self-interest rather than a cabal, notes the risk of double counting, and treats Anthropic's contractual compute commitments as debt in the valuation"
    confidence: 0.65
  - type: supports
    target: 2026-05-20-agrawal-stanford-mse435-economics-of-generative-ai
    via: "both address the unit economics of the model layer: Agrawal notes that an AI user is not marginally free because of GPU cost, against SaaS gross margins of 80–90%; Damodaran reads from Anthropic's prospectus a gross margin close to 80% and compute costs falling from 250% to under 50% of revenue in six quarters, which he ties to compute moving from a variable to a fixed cost"
    confidence: 0.65
  - type: contradicts
    target: 2026-05-10-ries-lennys-force-destroys-companies-within
    via: "both describe Anthropic's public-benefit-corporation status and benefit trust: Ries, who advised the founders on the structure, recommends it as protection of a company's mission against shareholder pressure; Damodaran reads the same structure, with the founders holding 50.1% of the votes through one Class F share, as removing shareholders' power to change management, and wants a larger discount before he would buy"
    confidence: 0.65
---

# Damodaran values Anthropic from its IPO prospectus

> The long-awaited Anthropic prospectus is now public, and as promised, I value the company. I start with an examination of what we can learn from the prospectus about revenue growth, profitability, reinvestment and risk at Anthropic, noting that both optimists (glass half full) and pessimists (glass half empty) will find reasons to celebrate, but that it is still a snapshot of a young company that is evolving. To value Anthropic, you have to leave the safety of reported numbers, and make your estimates of target revenues, end-game profit margins, reinvestment needed to deliver growth and risk, and I do, with a caveat. These represent my story for the company and I will not only be wrong 100% of the time, but your decision on whether to invest in Anthropic has to come from your story, and value, not mine. During the session, I try (but may fail) to do this, by providing you a framework to make your own choices, and assess your own value!
>
> Slides: https://pages.stern.nyu.edu/~adamodar/pdfiles/blog/AnthropicIPO.pdf · Blog post: https://aswathdamodaran.blogspot.com/2026/10/the-anthropic-prospectus-arrives-ipo.html · Anthropic prospectus: https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm · Valuation spreadsheet: https://pages.stern.nyu.edu/~adamodar/pc/blog/AnthropicIPO.xlsx · Shared Google spreadsheet for viewers' inputs: https://docs.google.com/spreadsheets/d/1oux4pQo8bLnx5tvVH25j8yCXrFK0_5qviiAzuXqk-Fg/edit?usp=sharing
>
> *— Channel description, Aswath Damodaran*

## TL;DR

A 48-minute solo session by [[Aswath Damodaran]], recorded two days after [[Anthropic]] filed its IPO prospectus. He reads the 416-page filing along four dimensions (revenue growth, profitability, reinvestment, risk), then values the company with his own inputs and lands at an equity value of **about $1.48 trillion**, which he expects to be below the offering price. The session follows two earlier ones that are not in the wiki: one on AI as a business, one on how the IPO will be priced. A week later he answered viewers' feedback in [[2026-11-03-damodaran-anthropic-valuation-feedback-loop|a follow-up session]], which keeps the valuation, ranks the five inputs he is least sure of and defends the cost of capital. **Auto-generated transcript.** The quotations below needed no word corrections. Elsewhere the ASR renders Anthropic as "Enthropic", "entropic" or "philanthropic" and prospectus as "prospectors", and it doubles some digits ("72.6 6 billion", "1.48 48 trillion"); figures are given as spoken and flagged under Source quality.

What it adds to the wiki:

1. **The corpus's first reading of Anthropic's own financials**, second-hand: 1,300–1,400% revenue growth, more than $16 billion of revenue in the last reported quarter (as spoken; his own chart shows about $11.6 billion for 2026 Q2, see Source quality), compute costs down from 250% to under 50% of revenue, and more than $450 billion of contractual compute commitments.
2. **A worked valuation of a frontier lab**, every input stated, with the compute commitments counted as debt.
3. **A way to size the AI market**: four questions that put it below $2 trillion or above $10 trillion.
4. **A margin model** that splits the AI market into a commoditised mass segment (~10%) and a premium segment (~40%).
5. **A critical account of Anthropic's governance**: five share classes, a public benefit corporation, and a founders' share with 50.1% of the votes.

He calls the inputs his story, says they will be wrong, and invites viewers to enter their own in a shared spreadsheet. The prospectus figures are his reading of the S-1, spoken over slides; the S-1 itself is not ingested. Twelve of his slides, among them the valuation spreadsheet's output, are transcribed under Visual canon below, hand-picked from contact sheets.

## What the prospectus shows, read both ways

Damodaran's method for the filing is to read each dimension as a "glass half full" and a "glass half empty" case. He first complains about its length: 416 pages, in line with Airbnb and Uber, against about 80 for Apple in 1980 and 66 for Microsoft. He calls this "disclosure diarrhea" and says the risk section is *"completely useless but designed to protect companies from getting sued"* (3:22).

**Numbers he reads from the prospectus** (and from what Anthropic has told investors):

| Item | As stated | Time |
| --- | --- | --- |
| Prospectus length | 416 pages | 2:26 |
| Revenue growth, last year to this year | "up 1,300 to 1,400%" | 4:00 |
| Quarterly revenue | "from basically nothing to 16 billion plus in the last quarter" | 4:15 |
| Annualised run rate | could reach "a hundred billion at least" by year end | 4:25 |
| Customers | 11,900, of which about 1,900 spend more than $1 million | 4:42 |
| Third quarter | not in the prospectus; investor meetings indicate growth "seemed to have stalled" | 5:12 |
| Concentration | top five customers ≈ 25% of revenue | 6:12 |
| Revenue reporting | Anthropic reports gross revenue; the 15–20% owed to big-tech partners is booked as a marketing expense. OpenAI has moved to net revenue | 6:25 |
| Compute costs | 250% of revenue six quarters ago, now under 50% | 7:24 |
| Operating result | operating profit in the last quarter reported | 7:49 |
| Gross margin | close to 80%, after he moves the partner share into cost of goods sold | 8:12 |
| Capex and invested capital | small, because compute is bought through commitments | 10:00 |
| Compute commitments | contractual: more than $450 billion; total: more than $600 billion; Broadcom the largest single beneficiary | 10:30 |
| Capital raised | $114 billion, raised recently and held as cash | 12:54 |
| Convertible expense | $72.6 billion, a conversion option kicking in | 18:08 |
| Revenue mix | 80% from usage rather than subscriptions, and from enterprises | 22:14 |
| Credit rating | BB+, below investment grade | 30:10 |

**Revenue growth.** Fast growth and repeat customers who spend more, against a missing third quarter. Anthropic blames the stall on a compute constraint; Damodaran adds two reasons he thinks more dangerous: 100% quarter-on-quarter growth stops being feasible at scale, and OpenAI is *"competing on pricing power."*

**Profitability.** Expenses grow more slowly than revenue in almost every category, *"the essence of economies of scale"* (7:34). But the 80% gross margin came from moving compute, the largest expense, *"from the variable cost category to the fixed cost category"* (8:33), so the company must keep growing to stay profitable. Stock-based compensation is *"a pretty expensive feature."*

**Reinvestment.** Capex is small because investment takes the form of compute commitments. The optimist sees compute locked in, a catch-up with OpenAI, and cheaper chips; the pessimist asks how *"a young money losing company with $600 billion in commitments"* (11:42) meets them without growth.

**Risk.** Sticky, possibly *"non-discretionary"* revenue, about $200 billion of cash after the offering, and regulation as a moat against cheaper Chinese rivals; against that, high fixed costs, commitments that *"are like debt"*, and rules that could *"take quite a bite out of operating income."*

On circularity, with so much business coming from other players in the space: *"I don't think it's a conspiracy but it does make the numbers more opaque and creates a potential for double counting"* (14:59). The filing is *"a report card on a kindergartener, a very precocious and smart kindergartener"* (17:02), too early to answer the big questions. He rejects theories of a cabal of hyperscalers, NVIDIA and the labs, and reads the $72.6 billion convertible expense as what success costs when you pay with options: *"those expenses are going to be massive."*

## From the prospectus to a value

*"The prospectus… is still about the past. Valuation is about the future"* (19:10). He takes four inputs and, for each, gives viewers a menu of alternatives.

**His own assumptions** (none of these is in the prospectus):

| Input | His value | Viewer menu | Time |
| --- | --- | --- | --- |
| Total market for AI products and services | $5–10 trillion | below $2T to above $10T | 21:47 |
| Anthropic revenue in 2036 | $1 trillion (about $700–800 billion from the core business, plus add-on markets such as pharmaceuticals) | $200B, $500B, $800B, $1T, $1.5T, $2T, $2.5T | 23:02 |
| Margin by segment | mass market ~10% (business services), premium ~40% (enterprise software) | 10–40% via the mix | 24:47 |
| Segment mix | 75% premium, 25% mass market → 32.5% unadjusted margin | all mass to all premium | 25:29 |
| Regulatory effect | −5 points → 27.5% target margin | 0 or larger cuts | 32:11 |
| Sales-to-capital ratio | 3 ($3 of revenue per $1 of capital) | 1 up to higher values | 27:09 |
| Cost of capital | 9.74% at the start, converging to the US median of 9.13% | technology median; 7.79%; a bounded direct input | 28:58, 33:43 |
| Failure risk | 10%, with the business sold at half its value if it fails | 0% or other | 30:51 |
| Debt | present value of contractual commitments, $473 billion | — | 34:33 |

**Target revenues.** The four questions: is AI *"just a tool or will it replace employees?"*; highly paid or all employees; some businesses or all; the US and parts of Europe or global. His priors are some industries, white-collar and highly paid work, and Anthropic as a lead player in the premium segment. No company today has revenue of $1 trillion. Growth rates are *"just a pathway to an end."*

**Margins and reinvestment.** The premium market is *"powered by client data"* and stickier; he cannot see Anthropic ignoring the mass market, hence 75/25. Compute ages fast, so the investment is not *"one and done"*; chips may get cheaper while power, real estate, energy and water get dearer.

**Risk.** He gives Anthropic *"the risk of large technology companies with the burden of compute commitments,"* near the third quartile for US companies (median 9.16%, third quartile 9.88%, September 2026). Above about 10% *"you're pushing the limits on what a public company should have as a cost of capital."* Failure is priced separately and offset by the cash and by size (*"too big to fail"*). On regulation he cites Facebook: the rules *"might have made it more impregnable"* but raised its costs.

## The value: $1.48 trillion, bracketed

- **Operating assets:** about $1.7 trillion (34:17).
- **Plus cash:** about $220 billion, counting close to $100 billion of expected IPO proceeds.
- **Minus debt:** $473 billion, the present value of the contractual commitments. Is that allowed in accounting? *"I don't know and I don't care."* He capitalised leases from 1992; accountants followed in 2019.
- **Equity, after the failure adjustment:** $1.48 trillion (35:15), *"pretty close to the lower end of the offering price number"* in circulation; later $1.47 trillion. Per share: 447, a placeholder, on a count that includes restricted shares and the IPO shares, with options valued separately.
- **Worst case** (mass-market AI, AI as a tool, cost of capital 9.88%): equity of **−$373 billion**. *"The company won't exist. It'll go bankrupt."*
- **Best case** ($1.5 trillion of revenue, 40% margins, cheap compute, first-quartile cost of capital): **$4 trillion**.

He ends the valuation with his "3P test" for a viewer's own story: is it possible, plausible, probable?

## Governance: five share classes and a public benefit corporation

Corporate governance, for him, is *"a measure of how much power shareholders have to change the way a company is run when they don't like the way it's run."* Until [[Google]]'s 2004 IPO with ten-vote founder shares, new US listings had one share class; investors did not push back, and Facebook and other tech companies followed.

Anthropic, in his words *"a corporate governance quagmire"* (40:18), will have five classes:

- **Class A:** offered to the public, one vote per share.
- **Employee shares:** votes limited to changes that affect the benefit trust.
- **Class N:** held by Alphabet and [[Amazon]], no votes, a share of profits and cash flows.
- **Class T:** held by the benefit trust, which appoints the majority of the board.
- **Class F:** one share, held by the seven co-founders, with 50.1% of the votes.

As a Delaware public benefit corporation, Anthropic gets in his reading legal cover for decisions that leave shareholders worse off. He calls it *"naive"* to give seven people the power to do right by society, cites ESG as a precedent, and says the trust will be made up of people the founders picked: *"dictator level corporate governance… It's in perpetuity"* (43:27). He would still buy, at *"a much bigger discount."*

[[2026-05-10-ries-lennys-force-destroys-companies-within|Eric Ries on Lenny's Podcast]] describes the same structure: he advised the founders on it and recommends public-benefit status and an outside trust as protection of a company's mission. In Ries's account the trustees are AI-safety experts without equity; in Damodaran's, they are people the founders chose.

## Pricing, lock-ups, and when he would buy

He expects an offering price between $1.5 and $2 trillion: *"this stock will be traded, it won't be valued"* (44:02). Insiders other than founders and key figures may sell up to 10% on day one, the rest unlocks in tranches through day 180, and founders and key figures may trade after 365 days; he doubts unlocks move prices, *"because markets know the unlock is coming."* He will not buy well above $1.48 trillion. He expects the price to fall far enough below his value at some point, as Tesla's did after he judged it overvalued from 2013 to 2018.

## Visual canon

Twelve of the session's 31 slides, the valuation spreadsheet among them, hand-picked from contact sheets and transcribed from the pixels. Slides the narration reads out are left out; the stills manifest (frontmatter `stills:`) lists all 30 saved. Amounts are as on the slides; where a slide gives no unit, the scale is millions of dollars.

### 1 · Quarterly revenue and growth, read both ways

![[assets/2026-10-28-damodaran-anthropic-ipo-valuation/03-04m00-revenue-growth.webp|Revenue growth slide with quarterly revenue chart]]

*Still at [4:00](https://www.youtube.com/watch?v=cd1xrO2q9HU&t=240s) from Aswath Damodaran, "The Prospectus is here: My (but not the) Anthropic IPO Valuation!".*

Slide 4, **1. Revenue growth**. Chart *Anthropic: Quarterly Revenues in 2025 and 2026*: bars for quarterly revenue (left axis, $ million) and a line for growth over the prior quarter (right axis). The bars and points carry no labels; the values below are read off the axes and are approximate.

| Quarter | Revenue (≈ $ billion) | Growth over prior quarter (≈) |
| --- | ---: | ---: |
| 2025 Q1 | 0.4 | 93% |
| 2025 Q2 | 0.8 | 109% |
| 2025 Q3 | 1.4 | 75% |
| 2025 Q4 | 2.0 | 47% |
| 2026 Q1 | 4.7 | 132% |
| 2026 Q2 | 11.6 | 144% |

- *The glass half full:* 1. Revenues have *grown >1300% between 2025 the 2026 (first 2 quarters)*. 2. The *enterprise customer base has expended*, with 1900 customers who spend more than $1 million a year on agents and are returning to spend more. 3. *Return customers are spending far more* on repeate sales, suggesting stickiness.
- *The glass half empty:* 1. *Revenue growth slowed down in 3rd quarter of 2026*, as compute constraints and competition from OpenAI and open source models picked up. 2. *Revenues are still concentrated* with five customers account for 25% of revenues. 3. The *revenues are gross revenues*, not net of payments to partners.

*Still vs. transcript:* the narration says revenue went "from basically nothing to 16 billion plus in the last quarter"; the chart's last bar, 2026 Q2, stands at about $11.6 billion. The chart also shows the quarterly path, with growth falling to about 47% in 2025 Q4 before rising again, and the slide defines the 1,900 customers by spending of more than $1 million a year on agents.

### 2 · Every expense line as a share of revenue, quarter by quarter

![[assets/2026-10-28-damodaran-anthropic-ipo-valuation/04-07m10-profitability.webp|Profitability slide with expense ratios by quarter]]

*Still at [7:10](https://www.youtube.com/watch?v=cd1xrO2q9HU&t=430s) from Aswath Damodaran, "The Prospectus is here: My (but not the) Anthropic IPO Valuation!".*

Slide 5, **2. Profitability**. Chart *Anthropic: Expenses and Profits* ($ million): stacked bars for compute costs, employee compensation, marketing and other G&A, a revenue line and an operating-income line that is negative through 2026 Q1 and turns positive in 2026 Q2. Table, *As percent of revenues*:

| Period | Compute costs | Employee compensation | Marketing | Other G&A | Gross margin | Operating margin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2025 Q1 | 251.06% | 57.98% | 6.38% | 33.24% | 17.84% | −248.67% |
| 2025 Q2 | 176.62% | 40.66% | 12.20% | 23.00% | 42.69% | −152.48% |
| 2025 Q3 | 148.12% | 35.38% | 14.62% | 16.86% | 53.29% | −114.98% |
| 2025 Q4 | 144.36% | 39.80% | 12.06% | 42.79% | 23.62% | −139.02% |
| 2026 Q1 | 71.59% | 27.37% | 21.83% | 14.44% | 62.47% | −35.24% |
| 2026 Q2 | 48.10% | 16.07% | 18.48% | 8.92% | 77.52% | 8.43% |

- *The glass half full:* rising gross margins, "pointing to improving unit economics"; operating losses narrowing, "with perhaps a turn towards profits in the most recent quarters"; growth generated efficiently, "with compute cost decreasing as a percent of revenues to 48% from over 251% and generating almost $6.6 million in revenue per employee."
- *The glass half empty:* 1. The gross margin is high only *because compute costs have become fixed costs*. 2. The company may generate operating profits, but will *need to continue to grow revenues to cover rising compute costs*. 3. The company *spends hefty amounts on stock-based compensation*, mostly in restricted stock, manageable as long as revenues continue to grow and employee count stays low.

*Still vs. transcript:* the narration gives the endpoints: compute from 250% to under 50% of revenue, a gross margin close to 80%, an operating profit in the last quarter. The table gives every quarter and every expense line, including the setback in 2025 Q4 (gross margin 23.62%, other G&A 42.79% of revenue) and the 8.43% operating margin in 2026 Q2. The revenue per employee, almost $6.6 million, is not spoken.

### 3 · Compute commitments by counterparty

![[assets/2026-10-28-damodaran-anthropic-ipo-valuation/05-09m50-reinvestment-compute-commitments.webp|Compute commitments by counterparty]]

*Still at [9:50](https://www.youtube.com/watch?v=cd1xrO2q9HU&t=590s) from Aswath Damodaran, "The Prospectus is here: My (but not the) Anthropic IPO Valuation!".*

Slide 6, **3. Reinvestment**, panel *Reinvestment for Growth*. Pie chart *Anthropic: Compute Commitments (in billions of dollars)*:

| Counterparty | $ billion |
| --- | ---: |
| Broadcom | 161.20 |
| SpaceX | 120.50 |
| Google | 114.50 |
| Amazon | 110.00 |
| Microsoft | 45.00 |
| Niscale (as spelled on the slide) | 44.60 |
| Lambda | 41.30 |
| One small slice, unlabelled | — |

The labelled slices add up to $637.1 billion.

- *The glass half full:* 1. The company *has locked in significant compute capacity*, a key ingredient in developing and selling its frontier models, and is closing a gap it had on this front with OpenAI. 2. The *compute investment cost should become lower over time,* as chips become cheaper and more capacity is built. 3. Some of these commitments have *flexibility built into them*, allowing for cancellation or change.
- *The glass half empty:* 1. The commitments that the company has for compute capacity exceed $650 billion, most of which are contractually set, and are thus analogous to debt. 2. If opposition to data centers continues to build, compute power may become more expensive over time. 3. The compute investments will need renewal and growth, creating an ongoing reinvestment need.

*Still vs. transcript:* the narration names only Broadcom, as the largest beneficiary, and gives the totals as more than $450 billion contractual and more than $600 billion in all. The pie names seven counterparties with amounts, three of them other than Broadcom above $100 billion (SpaceX, Google, Amazon), and the slide puts the total above $650 billion. That some commitments can be cancelled or changed is not spoken.

### 4 · The commitment schedule and its value as debt

![[assets/2026-10-28-damodaran-anthropic-ipo-valuation/06-12m30-risks-commitments-as-debt.webp|Commitment schedule and its present value as debt]]

*Still at [12:30](https://www.youtube.com/watch?v=cd1xrO2q9HU&t=750s) from Aswath Damodaran, "The Prospectus is here: My (but not the) Anthropic IPO Valuation!".*

Slide 7, **4. Risks**, panel *Risk – Operating, Financing and Regulatory*:

| Year | Compute & purchase commitment | Present value @ 6.28% (BB+ rate) |
| --- | ---: | ---: |
| 1 | $63,168.00 | $59,433.89 |
| 2 | $98,128.00 | $86,869.43 |
| 3 | $60,832.00 | $50,669.09 |
| 4 | $58,304.00 | $45,692.66 |
| 5 | $50,000.00 | $36,868.47 |
| 6 and beyond | $62,000.00 | $83,486.03 |
| **Debt value of commitments** | | **$363,019.56** |

The present value of the last row is larger than the amount shown, so "6 and beyond" is not a single payment. Below the table, under *What AI Risks Are Currently Being Governed?*, a *Risk Domain Coverage* chart whose source the slide does not name: the share of documents per risk domain, split into enacted, defunct and proposed. AI system safety, failures and limitations has the largest share (about 31%), then socioeconomic and environmental (about 26%), privacy and security, malicious actors, discrimination and toxicity, human-computer interaction and misinformation (each under 10%).

- *The glass half full:* 1. Once embedded in their client's business, *AI agents will be difficult to dislodge or cut back on, making revenues stable*. 2. The company has *$114 billion in cash*, likely to be augmented with another $100 billion from the offering, and *continued access to capital*. 3. There are regulatory risks, but *even if regulations are in place, it will keep competition out*, even as it makes a dent in profits.
- *The glass half empty:* 1. It remains to be seen *whether the money spent on AI agents is discretionary* and cut by clients when times are bad. 2. The company is money-losing and is *currently rated BB+, indicating that there is default risk*. 3. If *regulations and restrictions are extensive*, they will impede growth (which the company needs to be stay whole) and cause margin pressure.

*Still vs. transcript:* the narration says the commitments "are like debt" and later subtracts $473 billion of debt in the valuation. This slide values the commitments alone at $363 billion, discounted at 6.28%, the rate for a BB+ borrower, and shows the year-by-year schedule behind it. The governance chart is not discussed.

### 5 · Five sizes of the AI market and the four axes behind them

![[assets/2026-10-28-damodaran-anthropic-ipo-valuation/10-20m10-target-revenues-market-for-ai.webp|Total addressable market for AI products and services]]

*Still at [20:10](https://www.youtube.com/watch?v=cd1xrO2q9HU&t=1210s) from Aswath Damodaran, "The Prospectus is here: My (but not the) Anthropic IPO Valuation!".*

Slide 11, **1. Target revenues – the market for AI products and services**. *Total Addressable Market (TAM) for AI products and services*:

| TAM | Scenario |
| --- | --- |
| $250 billion | Estimate (most upbeat) of current size of market for AI products & services |
| <$1 trillion | AI almost entirely a tool for mass market use in a small subset of industries |
| $2 to $5 trillion | AI tool in many businesses & replaces skilled highly paid workers in some geographies |
| $5–$10 trillion | AI replaces skilled workers across many industries and across geographies |
| >$10 trillion | AI replaces most workers across many industries and across geographies |

Four axes, each running from small TAM to large TAM: *AI tool* → *AI as employee replacement*; *highest paid workers* → *all employees*; *technology and service industries* → *all industries*; *mostly US* → *global*.

*Still vs. transcript:* the narration poses the four questions and says the answers put the market below $2 trillion or above $10 trillion. The slide adds the steps in between, each tied to a scenario, and a starting point: the current market for AI products and services, at its most upbeat, is $250 billion.

### 6 · Target revenue options and the growth each implies

![[assets/2026-10-28-damodaran-anthropic-ipo-valuation/12-23m40-your-pick-on-target-revenues.webp|Your pick on target revenues]]

*Still at [23:40](https://www.youtube.com/watch?v=cd1xrO2q9HU&t=1420s) from Aswath Damodaran, "The Prospectus is here: My (but not the) Anthropic IPO Valuation!".*

Slide 13, **Your pick on target revenues**:

| Expected revenues in 2036 | $ revenues in 2036 ($ billion) | CAGR (years 2–5) |
| --- | ---: | ---: |
| A1: $200 billion, AI as tool | $200 | 9.00% |
| A2: $500 billion, AI as job replacement in future | $500 | 26.80% |
| A3: $800 billion, AI as selective job replacement | $800 | 36.71% |
| A4: $1,200 billion, AI as broad job replacement | $1,200 | 46.00% |
| A5: $1,500 billion, AI as industry player | $1,500 | 51.25% |
| **A6: Direct input (enter CAGR & check year 10 revenues)** (highlighted) | **$1,011** | **42.00%** |

The first column's header reads "(in $ millions)"; the amounts are in billions.

*Still vs. transcript:* the narration lists 200, 500 and 800 billion and 1, 1.5, 2 and 2.5 trillion and calls growth rates "a pathway to an end". The table offers $1.2 trillion instead of $1, $2 and $2.5 trillion, shows the growth rate for years 2–5 that each target implies (9% to 51.25%), and shows that his own $1 trillion is entered as a 42% growth rate, which gives $1,011 billion.

### 7 · Usage-based enterprise revenue and the 32.5% margin

![[assets/2026-10-28-damodaran-anthropic-ipo-valuation/14-25m20-my-anthropic-twist.webp|My Anthropic twist]]

*Still at [25:20](https://www.youtube.com/watch?v=cd1xrO2q9HU&t=1520s) from Aswath Damodaran, "The Prospectus is here: My (but not the) Anthropic IPO Valuation!".*

Slide 15, **My Anthropic twist**:

- Anthropic is targeting the premium market, as reflected not only in its current revenue breakdown, with almost 80% from enterprises paying based on usage, but also in its focus on using its newly acquired compute power to build next generation models rather than service current clients.
- **I will assume an end-mix of 75% of revenues from premium products, and 25% from the mass market, giving me an unadjusted pre-tax operating margin of 32.5%; that would put them at the ninth decile of US companies in 2026.**

*Still vs. transcript:* the spoken "80% of their revenues come from usage not subscription models and from enterprises" is a single share on the slide: almost 80% from enterprises paying by usage. The slide adds two points the narration does not make: a 32.5% margin would rank in the ninth decile of US companies, and the new compute goes to next-generation models rather than to current clients.

### 8 · Cost-of-capital options, with the technology median

![[assets/2026-10-28-damodaran-anthropic-ipo-valuation/19-29m20-your-operating-risk-story.webp|Your operating risk story, cost of capital options]]

*Still at [29:20](https://www.youtube.com/watch?v=cd1xrO2q9HU&t=1760s) from Aswath Damodaran, "The Prospectus is here: My (but not the) Anthropic IPO Valuation!".*

Slide 20, **Your operating risk story…**:

| Cost of capital | Initial cost of capital |
| --- | ---: |
| **D1: Company-specific inputs** (highlighted) | **9.74%** |
| D2: Technology median | 9.34% |
| D3: All companies – first quartile | 7.79% |
| D4: All companies – median | 9.16% |
| D5: All companies – third quartile | 9.88% |
| D6: Direct input | 10.00% |

Comments: "Don't overthink this. Given that AI will serve a range of businesses, this cost of capital will not be through the roof. Your concerns about regulatory risk can be reflected in margins and about lease commitments in failure risk on input page."

*Still vs. transcript:* the narration calls the technology median "lower" than 9.74% without a number; the slide gives 9.34%. The comment also says where the other risks belong: regulation in the margin, the commitments in the failure risk.

### 9 · The valuation spreadsheet

![[assets/2026-10-28-damodaran-anthropic-ipo-valuation/24-33m00-valuation-spreadsheet.webp|Anthropic IPO valuation spreadsheet]]

*Still at [33:00](https://www.youtube.com/watch?v=cd1xrO2q9HU&t=1980s) from Aswath Damodaran, "The Prospectus is here: My (but not the) Anthropic IPO Valuation!".*

Spreadsheet **Anthropic (IPO S-1)**, $ million. On screen from 33:00 to about 36:20, unchanged.

*Base year and comparison* (company; industry): revenue growth 1920.19% (14.84%); revenue $20,608; operating margin −227.98% (27.41%); operating income −$46,981; EBIT (1−t) −$46,981.

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Terminal year |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Revenue growth | 400.00% | 42.00% | 42.00% | 42.00% | 42.00% | 34.58% | 27.16% | 19.74% | 12.32% | 4.90% | 4.90% |
| Revenue | 103,040 | 146,317 | 207,770 | 295,033 | 418,947 | 563,819 | 716,952 | 858,479 | 964,243 | 1,011,491 | 1,061,054 |
| Operating margin | 5.00% | 14.00% | 18.50% | 23.00% | 27.50% | 27.50% | 27.50% | 27.50% | 27.50% | 27.50% | 27.50% |
| Operating income | 5,152 | 20,484 | 38,437 | 67,858 | 115,210 | 155,050 | 197,162 | 236,082 | 265,167 | 278,160 | 291,790 |
| EBIT (1−t) | 5,152 | 20,484 | 38,437 | 67,858 | 115,210 | 147,298 | 177,446 | 200,669 | 212,134 | 208,620 | 218,842 |
| Reinvestment | 14,426 | 20,484 | 29,088 | 41,305 | 48,291 | 51,044 | 47,175 | 35,255 | 15,749 | 16,521 | 71,489 |
| FCFF | (9,274) | – | 9,350 | 26,553 | 66,920 | 96,253 | 130,270 | 165,415 | 196,384 | 192,099 | 147,354 |
| Cost of capital | 9.74% | 9.74% | 9.74% | 9.74% | 9.74% | 9.62% | 9.50% | 9.37% | 9.25% | 9.13% | |
| Cumulated WACC | 0.9112 | 0.8304 | 0.7567 | 0.6895 | 0.6283 | 0.5732 | 0.5235 | 0.4786 | 0.4381 | 0.4014 | |
| Sales to capital | 3.00 | 3.00 | 3.00 | 3.00 | 3.00 | 3.00 | 3.00 | 3.00 | 3.00 | 3.00 | |
| ROIC | 0.97% | 3.74% | 6.76% | 11.35% | 18.03% | 21.43% | 24.03% | 25.54% | 25.84% | 24.94% | 15.00% |

Terminal value, under year 10: $3,483,544.00.

| From cash flows to value per share | |
| --- | ---: |
| PV (terminal value) | $1,398,391 |
| PV (CF over next 10 years) | $424,657 |
| Probability of failure | 10.00% |
| Value of operating assets | $1,731,896 |
| − Debt | $472,336 |
| − Minority interests | $0 |
| + Cash | $212,389 |
| + Non-operating assets | $3,929 |
| Value of equity | $1,475,879 |
| − Value of options | $472 |
| Value of equity in common stock | $1,475,406 |
| Number of shares | 3,298.14 |
| Estimated value / share | $447.34 |
| Price per share | Not priced yet |

The story boxes:

- *Growth story:* "High growth leading into IPO will push revenues up significantly next year, and as AI products and services displace labor in selected industries, the market expands to allow for more growth. In some niche businesses, like drugs, Anthropic has potential to generate its own revenues."
- *Profitability story:* "Margins improve, with pricing power on premium products, and compute costs are largely grow at rates lower than revenues."
- *Growth efficiency story:* "Compute costs scarcity and costs will ease over time, allowing for lower reinvestment to sustain growth."
- *Risk story:* "Cost of capital starts at about the 75th percentile and moves close to median company over time."
- *Competitive advantages:* "Closed frontier models with client data create stickiness that will create long term competitive advantages for Anthropic."

*Still vs. transcript:* the spoken bridge (about $1.7 trillion, plus about $220 billion of cash, minus $473 billion of debt) does not reach the result; the sheet does: $1,731,896 − $472,336 + $212,389 + $3,929 = $1,475,879 million. The failure adjustment is already inside the operating-asset value, which is 95% of the $1,823,048 million in discounted cash flows (a 10% chance of failure, with half the value recovered). The sheet also shows what is not spoken: base-year revenue of $20.6 billion at a −228% operating margin, 400% growth in year 1, the margin reaching 27.5% in year 5, after-tax operating income equal to pre-tax for years 1–5, a terminal value that makes up about three-quarters of the value, and the 3,298.14 shares (millions) behind the $447.34 per share.

### 10 · The worst and best cases, input by input

![[assets/2026-10-28-damodaran-anthropic-ipo-valuation/25-36m20-and-yours-worst-and-best-case.webp|Worst-case and best-case Anthropic stories]]

*Still at [36:20](https://www.youtube.com/watch?v=cd1xrO2q9HU&t=2180s) from Aswath Damodaran, "The Prospectus is here: My (but not the) Anthropic IPO Valuation!".*

Slide 26, **And yours?**:

- The **worst-case Anthropic story**, where target revenues limp to $200 billion in 2036, margins converge on the mass market (10%), compute power stays scarce and costly (sales to capital of one), cost of capital rises to the third quartile for US companies (9.88%) and the regulatory effect on margins is drastic yields worthless equity. In fact, **the value of equity is −$373 billion**, and the company will cease to exist.
- The **best-case Anthropic story**, where target revenues surge to $1.5 trillion in 2036, margins converge on the premium market (40%), compute power becomes cheap (sales to capital of four), cost of capital falls to the first quartile for US companies (7.79%) and the regulatory effect on margins is non-existent **yields a value of $4.04 trillion for equity.**
- While I believe that the best case and worse case scenarios are both unlikely, **you can assess your own story for the company, with the resulting value**, applying what I call the 3P test: Is it **possible**? Is it **plausible**? Is it **probable**? Investing is a personal decision, and whether you choose to buy Anthropic, sell it short or sit on the sidelines, you should base it on your own assessment.

*Still vs. transcript:* the narration gives the worst case as a mass market, AI as a tool and a 9.88% cost of capital, and the best case as $1.5 trillion of revenue, 40% margins, cheap compute and the first quartile, worth "4 trillion". The slide completes both sets of inputs: $200 billion of revenue, a sales-to-capital ratio of one and a drastic regulatory cut for the worst case; a ratio of four, 7.79% and no regulatory cut for the best. It puts the best case at $4.04 trillion.

### 11 · Five share classes and their voting rights

![[assets/2026-10-28-damodaran-anthropic-ipo-valuation/27-40m20-voting-right-structure.webp|Anthropic voting right structure]]

*Still at [40:20](https://www.youtube.com/watch?v=cd1xrO2q9HU&t=2420s) from Aswath Damodaran, "The Prospectus is here: My (but not the) Anthropic IPO Valuation!".*

Slide 28, **Anthropic: a voting right structure**:

| Share class | Voting rights |
| --- | --- |
| A | **Only share class available to public.** *Standard economic and voting rights*, but with little or no influence on board composition or major corporate actions. |
| E | **Employee shares**, with *voting rights limited to changes that affect the benefit trust* (which runs the company) or in the event of disputes. |
| N | **Corporate holder shares**, which are *nonvoting shares* held by Alphabet and Amazon, giving them share of profits and cash flows, but no say in how the company is run. |
| T | **Held by benefit trust,** which has no voting rights, but has the power to *choose and elect the majority of the members of the board* and oversee the public benefit mission. |
| F | **Single share held by Anthropic's seven co-founders** (Dario & Daniela Amodei, Tom Brown, Jared Kaplan, Sam McCandlish & Jack Clark) with 50.1% of the voting rights. |

*Still vs. transcript:* the narration describes the five classes. The slide adds the employee class's letter (E), that the trust's class T carries no votes of its own, that class A has little or no influence on the board, and the founders' names: six people named for "seven co-founders".

### 12 · The prospectus on decisions that may hurt shareholders

![[assets/2026-10-28-damodaran-anthropic-ipo-valuation/28-41m30-public-benefit-corporation-twist.webp|With a public benefit corporation twist]]

*Still at [41:30](https://www.youtube.com/watch?v=cd1xrO2q9HU&t=2490s) from Aswath Damodaran, "The Prospectus is here: My (but not the) Anthropic IPO Valuation!".*

Slide 29, **With a public benefit corporation twist**:

- [T]he company has **structured itself as a public benefit corporation**, and in its prospectus, it states that "*we may make decisions that we believe appropriately balance the pecuniary interests of our stockholders, the best interests of those materially affected by our conduct, and the Company Purpose, but that negatively impact the short-, medium-, or long-term performance of our business or the market price*".
- Given **the worries that people have about AI being a force for destruction**, a concern that Dario Amodei has actively cultivated, this protection against shareholder power may seem to be a good thing, but we need to be open eyed about what this structure does.
- It **does not protect society from AI's evils, but puts that power in the hands of the few** (the founders and members of the benefit trust) at the top of Anthropic, hoping that they use that power well. If you, as an investor, have had bad experiences with top management at companies using corporate responsibility and ESG as cover for self-serving activity and hypocrisy, the Anthropic structure is that structure on steroids.

*Still vs. transcript:* the narration paraphrases the public benefit corporation as legal cover for decisions that leave shareholders worse off. The slide quotes the prospectus sentence itself, which names the market price among the things such decisions may hurt.

## Dynamic-capabilities reading

- **`strategic-renewal/business-model`**: the prospectus reading describes a value-capture logic still being formed: 80% usage-based enterprise revenue, compute moved from a variable to a fixed cost through commitments, partner revenue shares booked as marketing, and Anthropic's stated intent to enter businesses such as pharmaceuticals as a participant, not only a supplier (22:45).

## Related in this wiki

- **AI capex and circular financing.** [[2026-08-18-covello-gs-new-models-ai-investment-landscape|Covello (Goldman Sachs)]] asks whether enterprise buyers make or save money and sorts circular financing into a discount and a dependency. [[2026-10-15-lin-stanford-ai-club-building-in-the-ai-era|Lin (Sequoia)]] compares circular investment to bank lending and points to data-centre debt. This source counts one lab's compute commitments as debt in its valuation. [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs|Hatzius (Goldman Sachs)]] raises the same double-counting caution for ecosystem revenue estimates.
- **Model-layer unit economics.** [[2026-05-20-agrawal-stanford-mse435-economics-of-generative-ai|Agrawal (Stanford MS&E435)]] asks which layer of the stack keeps the margin and notes the GPU cost of each AI user; this source gives one model lab's gross margin and compute-cost trend as reported in its filing.
- **The follow-up.** [[2026-11-03-damodaran-anthropic-valuation-feedback-loop|Heeding the Feedback Loop (3 Nov 2026)]] ranks these inputs by fragility and answers the pushback on the cost of capital.

## Linked entities and concepts

- **Entities:** [[Aswath Damodaran]] (channel and speaker), [[Anthropic]] (subject), [[OpenAI]] (competitor; net-revenue reporting), [[Google]] (dual-class precedent; Alphabet holds Class N shares), [[Amazon]] (holds Class N shares), [[Microsoft]] (66-page prospectus), [[NVIDIA]] (named in the conspiracy theories he rejects).
- **Concepts:** [[foundation-models]], [[generative-ai]], [[automation-vs-augmentation]], [[responsible-ai]], [[warner-wager-process-model]].
- **Dangling** (single-source mention, deferred): Broadcom, Dario Amodei, Facebook, Tesla, Apple.

## Source quality

- **Auto-generated ASR transcript**, cleaned in quotation only. The session is led by slides and a spreadsheet. The transcript holds only what he says aloud. **12 stills were hand-picked from contact sheets** on 2026-11-17, after the Gemini stills scan failed on 2026-11-16 (HTTP 402) before any call ran; they carry the slides' tables and charts and the spreadsheet's output sheet (see Visual canon). The spreadsheet's input sheet is not shown in the session.
- **The prospectus figures are second-hand**: his reading of the S-1, partly from slides the transcript does not show. Those slides are now transcribed under Visual canon; their figures are still his reading and his charts, not the filing. The third-quarter stall comes from Anthropic's meetings with investors, not from the filing.
- **Figures that could not be pinned down from speech:**
  - Customer count: 11,900 is spoken without the spending threshold that defines it. The revenue slide (still 1) gives only the 1,900 who spend more than $1 million a year on agents.
  - Quarterly revenue: spoken as "16 billion plus in the last quarter" (4:15), but the revenue chart on his slide (still 1) shows about $11.6 billion for 2026 Q2, its last bar. The same slide's text box says *"Revenue growth slowed down in 3rd quarter of 2026"*, so he had a third-quarter figure the chart does not plot, and the spoken "last quarter" may be that one. Which is right is not settled here.
  - Growth: "1,300 to 1,400%" is rendered "1300 to,400%" in the ASR. The slide says ">1300% between 2025 the 2026 (first 2 quarters)"; the spreadsheet's base-year growth is 1920.19% (stills 1 and 9).
  - Convertible expense: spoken "72.6 6 billion", read here as $72.6 billion.
  - Revenue mix: "80%… from usage not subscription models and from enterprises" may be one share or two. Slide 15 (still 7) makes it one: "almost 80% from enterprises paying based on usage".
  - Median US cost of capital: given as 9.16% at 29:07 and as 9.13% (the convergence target) at 33:53. Both are on screen: 9.16% is the September 2026 median on the cost-of-capital slide (still 8), 9.13% the year-10 cost of capital in the spreadsheet (still 9).
  - The technology-sector option: he calls the technology median "lower" than 9.74% (29:28). His follow-up session puts it at 10.75%. The slide in this session gives 9.34% (still 8).
  - Debt: $473 billion here is described as the present value of the contractual commitments. The follow-up gives that present value as about $373 billion, so either the $473 billion includes other debt or one figure is a slip. The number 373 also appears here, as the worst-case equity value (−$373 billion). The stills separate the two: the spreadsheet subtracts debt of $472,336 million (still 9), while the risks slide values the compute and purchase commitments alone at $363,019.56 million, discounted at 6.28%, the BB+ rate (still 4). The slides do not show what makes up the difference. The follow-up's restated spreadsheet subtracts the same $472,335.56 million and labels it *"lease, purchase and compute commitments"*; its "Some added details" slide puts the contractual compute commitments alone at about $373 billion, not this slide's $363 billion.
  - The spoken bridge does not reproduce the result: about $1.7 trillion + $220 billion − $473 billion is about $1.45 trillion before the failure adjustment, which lowers value. The final $1.48 trillion (described elsewhere as $1.475 trillion) therefore rests on unrounded figures in the spreadsheet. The spreadsheet still (9) reconciles it: operating assets of $1,731,896 million already include the failure adjustment, cash is $212,389 million, and $3,929 million of non-operating assets completes the sum to $1,475,879 million.
  - Per-share value: "447" is spoken without a unit and is a placeholder by his own account. The spreadsheet shows $447.34 per share on 3,298.14 (million) shares (still 9).
- **Standing.** Damodaran teaches valuation and values companies as an investor. The shares are not yet traded; he says he will not buy at the expected price. The inputs are his story; he states that they will be wrong and invites alternatives. His spreadsheet and the S-1 are linked in the description and were not fetched; the spreadsheet's output sheet is transcribed from the video (still 9).
