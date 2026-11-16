---
type: source
kind: video
title: "The Prospectus is here: My (but not the) Anthropic IPO Valuation!"
author: ["Aswath Damodaran"]
publisher: "Aswath Damodaran (YouTube channel); solo session by Aswath Damodaran, professor of finance at NYU Stern (slides and spreadsheet hosted on pages.stern.nyu.edu)"
url: "https://www.youtube.com/watch?v=cd1xrO2q9HU"
date_published: 2026-10-28
date_ingested: 2026-11-16
length: "~47:44 minutes (transcript ~365 lines; ASR auto-generated track, no chapters)"
raw: "../../raw/videos/the-prospectus-is-here-my-but-not-the-anthropic-ipo-valuation.md"
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

A 48-minute solo session by [[Aswath Damodaran]], recorded two days after [[Anthropic]] filed its IPO prospectus. He reads the 416-page filing along four dimensions (revenue growth, profitability, reinvestment, risk), then values the company with his own inputs and lands at an equity value of **about $1.48 trillion**, which he expects to be below the offering price. The session follows two earlier ones that are not in the wiki: one on AI as a business, one on how the IPO will be priced. **Auto-generated transcript.** The quotations below needed no word corrections. Elsewhere the ASR renders Anthropic as "Enthropic", "entropic" or "philanthropic" and prospectus as "prospectors", and it doubles some digits ("72.6 6 billion", "1.48 48 trillion"); figures are given as spoken and flagged under Source quality.

What it adds to the wiki:

1. **The corpus's first reading of Anthropic's own financials**, second-hand: 1,300–1,400% revenue growth, more than $16 billion of revenue in the last reported quarter, compute costs down from 250% to under 50% of revenue, and more than $450 billion of contractual compute commitments.
2. **A worked valuation of a frontier lab**, every input stated, with the compute commitments counted as debt.
3. **A way to size the AI market**: four questions that put it below $2 trillion or above $10 trillion.
4. **A margin model** that splits the AI market into a commoditised mass segment (~10%) and a premium segment (~40%).
5. **A critical account of Anthropic's governance**: five share classes, a public benefit corporation, and a founders' share with 50.1% of the votes.

He calls the inputs his story, says they will be wrong, and invites viewers to enter their own in a shared spreadsheet. The prospectus figures are his reading of the S-1, spoken over slides; the S-1 itself is not ingested.

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

## Dynamic-capabilities reading

- **`strategic-renewal/business-model`**: the prospectus reading describes a value-capture logic still being formed: 80% usage-based enterprise revenue, compute moved from a variable to a fixed cost through commitments, partner revenue shares booked as marketing, and Anthropic's stated intent to enter businesses such as pharmaceuticals as a participant, not only a supplier (22:45).

## Related in this wiki

- **AI capex and circular financing.** [[2026-08-18-covello-gs-new-models-ai-investment-landscape|Covello (Goldman Sachs)]] asks whether enterprise buyers make or save money and sorts circular financing into a discount and a dependency. [[2026-10-15-lin-stanford-ai-club-building-in-the-ai-era|Lin (Sequoia)]] compares circular investment to bank lending and points to data-centre debt. This source counts one lab's compute commitments as debt in its valuation. [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs|Hatzius (Goldman Sachs)]] raises the same double-counting caution for ecosystem revenue estimates.
- **Model-layer unit economics.** [[2026-05-20-agrawal-stanford-mse435-economics-of-generative-ai|Agrawal (Stanford MS&E435)]] asks which layer of the stack keeps the margin and notes the GPU cost of each AI user; this source gives one model lab's gross margin and compute-cost trend as reported in its filing.
- **The follow-up.** [[2026-11-03-damodaran-anthropic-valuation-feedback-loop]] ranks these inputs by fragility and answers the pushback on the cost of capital.

## Linked entities and concepts

- **Entities:** [[Aswath Damodaran]] (channel and speaker), [[Anthropic]] (subject), [[OpenAI]] (competitor; net-revenue reporting), [[Google]] (dual-class precedent; Alphabet holds Class N shares), [[Amazon]] (holds Class N shares), [[Microsoft]] (66-page prospectus), [[NVIDIA]] (named in the conspiracy theories he rejects).
- **Concepts:** [[foundation-models]], [[generative-ai]], [[automation-vs-augmentation]], [[responsible-ai]], [[warner-wager-process-model]].
- **Dangling** (single-source mention, deferred): Broadcom, Dario Amodei, Facebook, Tesla, Apple.

## Source quality

- **Auto-generated ASR transcript**, cleaned in quotation only. The session is led by slides and a spreadsheet. The transcript holds only what he says aloud; tables, footnotes and the spreadsheet's intermediate steps are not captured. **Stills deferred**: the stills scan failed on 2026-11-16 (Gemini 402) before any call ran.
- **The prospectus figures are second-hand**: his reading of the S-1, partly from slides the transcript does not show. The third-quarter stall comes from Anthropic's meetings with investors, not from the filing.
- **Figures that could not be pinned down from speech:**
  - Customer count: 11,900 is spoken without the spending threshold that defines it.
  - Growth: "1,300 to 1,400%" is rendered "1300 to,400%" in the ASR.
  - Convertible expense: spoken "72.6 6 billion", read here as $72.6 billion.
  - Revenue mix: "80%… from usage not subscription models and from enterprises" may be one share or two.
  - Median US cost of capital: given as 9.16% at 29:07 and as 9.13% (the convergence target) at 33:53.
  - The technology-sector option: he calls the technology median "lower" than 9.74% (29:28). His follow-up session puts it at 10.75%.
  - Debt: $473 billion here is described as the present value of the contractual commitments. The follow-up gives that present value as about $373 billion, so either the $473 billion includes other debt or one figure is a slip. The number 373 also appears here, as the worst-case equity value (−$373 billion).
  - The spoken bridge does not reproduce the result: about $1.7 trillion + $220 billion − $473 billion is about $1.45 trillion before the failure adjustment, which lowers value. The final $1.48 trillion (described elsewhere as $1.475 trillion) therefore rests on unrounded figures in the spreadsheet.
  - Per-share value: "447" is spoken without a unit and is a placeholder by his own account.
- **Standing.** Damodaran teaches valuation and values companies as an investor. The shares are not yet traded; he says he will not buy at the expected price. The inputs are his story; he states that they will be wrong and invites alternatives. His spreadsheet and the S-1 are linked in the description and were not fetched.
