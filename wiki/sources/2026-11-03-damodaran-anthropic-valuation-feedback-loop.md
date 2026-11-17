---
type: source
kind: video
title: "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation"
author: ["Aswath Damodaran"]
publisher: "Aswath Damodaran (YouTube channel); solo session by Aswath Damodaran, professor of finance at NYU Stern (slides and datasets hosted on pages.stern.nyu.edu)"
url: "https://www.youtube.com/watch?v=W0JDfYSpjnM"
date_published: 2026-11-03
date_ingested: 2026-11-16
length: "~51:38 minutes (transcript ~399 lines + 15 stills; ASR auto-generated track, 30 chapters)"
raw: "../../raw/videos/heeding-the-feedback-loop-a-follow-up-to-my-anthropic-valuation.md"
stills: "../../raw/videos/heeding-the-feedback-loop-a-follow-up-to-my-anthropic-valuation.stills.md"
tags: [aswath-damodaran, nyu-stern, anthropic, ipo, valuation, dcf, feedback-loop, devils-advocate, value-drivers, target-revenues, corporate-governance, moats, switching-costs, compute-commitments, failure-risk, regulatory-risk, margin-of-safety, diversification, cost-of-capital, cost-of-equity, equity-risk-premium, implied-equity-risk-premium, cost-of-debt, credit-rating, sector-cost-of-capital, hurdle-rates, venture-capital, private-equity, private-company-valuation, build-up-approach, coreweave]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - digital-seizing/strategic-agility
  - strategic-renewal/business-model
relationships:
  - type: depends-on
    target: 2026-10-28-damodaran-anthropic-ipo-valuation
    via: "the same author's follow-up to that session: it restates the $1.45–1.5 trillion result with its inputs unchanged, ranks the five inputs he is least sure of, and answers viewers' pushback on the 9.74% cost of capital"
    confidence: 0.95
  - type: contradicts
    target: 2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going
    via: "both address whether frontier-model labs can hold pricing power: Evans argues models lack network effects and compares them to AWS rather than Windows; Damodaran answers viewers who see no visible moat with first-mover stickiness, citing Windows and Office, and assumes Anthropic builds it by embedding premium products in customers' data and usage"
    confidence: 0.6
  - type: supports
    target: 2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas
    via: "both concern returns on capital against the cost of capital: MGI names sustained ROIC above the cost of capital as the open question behind AI-foundation valuations; Damodaran reports that fewer than 30% of listed companies globally earn more than his cost-of-capital estimates and argues against raising hurdle rates above them"
    confidence: 0.55
---

# Damodaran revisits his Anthropic valuation: five fragile inputs and the cost of capital

> I valued Anthropic, after its prospectus filing and ahead of its IPO, at $1.475 trillion about a week ago, and was open about the fact that I was telling a big story, with inputs and value to match. I encouraged people to push back and come up with their own stories, inputs and values for the company and many did. In this session, I start by playing devil's advocate with my own valuation, and list what I believe are the five biggest drivers of its value - target revenues tops the list, followed by governance, profitability, reinvestment and regulatory risk. I then look at your valuations and feedback, and note that the input that received the most pushback was my cost of capital of 9.74%, which some thought was too low. Since the cost of capital is much misunderstood concept that many use without frames of reference, I look at what a reasonable cost of equity (capital) is for a US firm in September 2026, and follow up with a table that lists out ranges for costs of capital, by sector. I argue that setting too high a cost of equity (capital) handicaps investors and businesses, creating more harm than good.
>
> Slides: https://pages.stern.nyu.edu/~adamodar/pdfiles/blog/AnthropicFollowUp.pdf · Blog post: https://aswathdamodaran.blogspot.com/2026/11/the-anthropic-feedback-loop-cost-of.html · Cost of capital by industry group: https://pages.stern.nyu.edu/~adamodar/pc/blog/waccUS.xlsx · Historical returns on stocks: https://pages.stern.nyu.edu/~adamodar/pc/datasets/histretSP.xlsx · Market-implied expected returns history: https://pages.stern.nyu.edu/~adamodar/pc/datasets/histimpl.xlsx
>
> *— Channel description, Aswath Damodaran*

## TL;DR

A 52-minute solo follow-up by [[Aswath Damodaran]] to [[2026-10-28-damodaran-anthropic-ipo-valuation|his valuation of Anthropic a week earlier]]. The first third is self-critique: he restates the valuation, ties up loose ends, and ranks the five inputs by how wrong they could be. The middle reports what about 70 viewers sent back. The last half is a general lecture on the cost of capital, prompted by the most common objection to his 9.74%. **Auto-generated transcript, ASR-cleaned in quotation**: "modes" → moats, "Enthropic" → Anthropic, "core weave" → CoreWeave, "PES" → PE, "going concerned" → going concern, "closer than 20" → closer to 20, "madeup" → made-up, and repeated words dropped. Fifteen of his slides, among them the restated valuation spreadsheet, the sector cost-of-capital table and the private-equity and venture-capital returns, are transcribed under [Visual canon](#visual-canon).

What it adds to the wiki:

1. **The valuation's inputs ranked by fragility**, each split into the assumptions it rests on.
2. **A technology-moat argument for a frontier lab**: first-mover stickiness, on the model of Windows and Office.
3. **Reality checks for a cost of equity**, with figures to September 2026: historical returns, the market-implied expected return (8.99% at the start of October), and sector ranges.
4. **The costs of hurdle rates set too high**, for VC and PE funds, CFOs, individual investors and private businesses.
5. **Viewer feedback**: about 70 alternative valuations, 65–70% of them lower than his.

The valuation does not change; the session is about method and defends his numbers.

## Keeping the feedback loop open

The last step of his valuation process, from his book on turning stories into numbers, is *"keeping the feedback loop open"*: *"Listening to people who disagree with you. learning from them but not always accepting what they suggest you should do"* (0:19). He values companies *"for an audience of one."* Devil's advocacy needs a model small enough to trace: *"When you have 400 line items, God knows what each input is doing. With my 15 to 20 line items, I know exactly where each input goes"* (2:06). The restated result is $1.45–1.5 trillion, *"an insanely large number"* but below the expected pricing range of $1.5–2 trillion (3:28).

**Loose ends** (3:45–5:52):

- The per-share value is a placeholder until the share count is set; the aggregate equity value will not change. Restricted shares are counted.
- The cost of debt rests on a **BB+** rating, below investment grade, which a Financial Times story *"on Friday, 3 days ago"* reported as likely (4:25).
- **Compute commitments**: *"by my count about 450 billion"* contractually set, plus *"another couple of hundred billion"* with more flexibility. *"The present value of the contractual commitments is about 373 billion. I do include that as debt"* (4:55).
- **Dilution**: options are valued and subtracted; convertibles are treated as converting at the IPO; future share issues are already priced, because *"you issue new shares only if you have negative free cash flows,"* and those are discounted.

## Five inputs, ranked by how wrong they could be

*"I'm going to be wrong 100% of the time"* (6:21), so he orders the assumptions by where he could be most wrong:

| Rank | Input | What he assumed | What could go wrong |
| --- | --- | --- | --- |
| 1 | Target revenues | $1 trillion by year 10 | Any of four stacked assumptions fails (below) |
| 2 | Governance | that it will not *"come back and bite us"* | Seven founders in an echo chamber resist correcting mistakes |
| 3 | Profitability | 32.5% pre-regulation margin | Gross margin falls below 80%, scale economies weaken, no moat |
| 4 | Reinvestment | $3 of revenue per $1 of capital | Power and other costs rise as chip costs fall; new businesses need more capital |
| 5 | Risk | 9.74% cost of capital, 10% failure, −5 points for regulation | Regulation becomes more onerous; this is the risk input that worries him most |

**Target revenues** rest on four layers (7:10–9:21). A $5–10 trillion market needs *"more employee replacement than tools and customers being willing to pay high prices."* The premium segment could shrink because *"open-source models might be able to do a lot of what these premium models do."* Anthropic's lead could go if the segment is *"splintered, perhaps even disrupted."* And add-on markets such as drugs may need skills it lacks: *"Google has been able to build self-driving cars. But does that mean Google wants to be a ride sharing company? I don't think so."*

**Governance** is second although it carries no number. Management *"has to be willing to change and adapt and sometimes go back and reverse policies that they themselves adopted,"* and *"really smart people hate admitting mistakes. You need somebody acting as a check"* (10:18). With seven founders who *"think the same way about the world and operate in an echo chamber, change is going to be really difficult."* It shows up *"in how much below the value the price has to drop before I'm willing to buy."*

**Profitability** assumes gross margins of 80% or more, economies of scale, and margins that last. Many viewers saw no moat. His answer (12:02): *"In technology, the moats aren't like moats that you find in consumer products which could be brand name or in commodities which could be cost advantages."* First movers win by stickiness: Windows beat a better Apple operating system *"because it became the default,"* and *"once you're into Excel and Windows and PowerPoint, it gets sticky to switch up."* Anthropic would get there with *"premium products that embed themselves in their customers' data and usage."* He adds: *"This could be a pipe dream. There might be no moats."* [[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Benedict Evans on Lenny's Podcast]] asks the same pricing-power question and compares models to AWS rather than Windows, on the grounds that they show no network effects.

**Reinvestment** assumes signed commitments cover near-term compute and added compute gets cheaper. **Risk**: he is comfortable with the cost of capital and the 10% failure risk: *"Anthropic is no CoreWeave,"* not a company with *"a 40 or 50% failure risk"* (15:20). *"The risk I feel least comfortable about is my regulatory risk assumption… political change pressures might build on those regulations."*

## Investing under uncertainty

Three responses to an uncertain stock: avoid it, demand a margin of safety, or rely on the law of large numbers (16:12). A 40% **margin of safety** on $1.5 trillion means buying at $900 billion. A higher margin cuts type I errors (buying the wrong stock) and adds type II errors (missing the right one): *"If your portfolio right now is 50% in cash or 70% in cash, your margin of safety has been set too high"* (18:02). His own margin for Anthropic is *"more for the governance risk than for uncertainty."* **Diversification** lets him hold it: not with a sole $1 million, but as *"one of 20, one of 25 stocks"* (19:27).

## What viewers sent back

About 70 people had entered their own inputs in the shared spreadsheet by the morning of recording. Roughly 65–70% found his value too high; *"only two out of the 70"* came in above two (trillion, by context) (20:34); within 10–15% counts as agreement. The commonest reason for a lower value was gut feeling; the second, that 9.74% is too low.

## Why the cost of capital is not the hill he dies on

He is *"disappointed but not surprised"* by the objection: the cost of capital *"should never be the biggest number in your valuation,"* yet for many analysts it is *"the receptacle for their hopes, their fears, their fantasies"* (22:34). He calls it *"the Swiss army knife of finance"*: a hurdle rate in corporate finance, a discount rate in valuation. A cost of equity is *"what an investor can make on an investment of equivalent risk elsewhere in the market"* (25:12). It is subjective, but *"you got to live in the world you're in, not the world you wished you were in."*

**His reality checks, as stated:**

| Check | Figure | Time |
| --- | --- | --- |
| Average annual US equity return, last 25 years | 8.74% | 26:31 |
| … last 50 years | 11.92% | 26:41 |
| … 1928–2025 | 10.13% | 26:41 |
| Geometric equity premium over T-bonds, 1928–2025 | 5.54% | 27:25 |
| T-bond rate now | about 4.9% (4.9 + 5.54 = 10.44%) | 27:30 |
| S&P 500, 30 September 2026 | 7,651.54 | 28:28 |
| Implied expected return on US equities, start of October 2026 | 8.99% (November update: 8.83%) | 28:53 |
| Implied equity risk premium, start of October | about 3.7% | 29:32 |
| Last time the implied expected return exceeded 10% | before 1994 (*"not… in 32 years"*) | 30:01 |
| Market P/E implied by a 15% cost of equity (5% growth, 20% ROE) | about 7.27, against a market P/E *"closer to 20"* | 31:30 |
| Cost of debt used for Anthropic | about 6.5% pre-tax (BB+) | 34:00 |
| Energy, cost of capital: first decile / median / ninth decile | 7.16% / 7.6% / 10.96% | 35:17 |
| Technology: first decile / first quartile / median / third quartile / ninth decile | 9.88% / 9.92% / 10.75% / 12.3% / 14.5% | 35:50 |

He adds a caution about selection bias: the US was *"one of the most successful equity markets of the 20th century."* On debt, he separates the cost of borrowing from the chance of default: even for CoreWeave he would use *"a much more reasonable going concern cost of debt, maybe seven or 8%, but attach a really large failure risk."* His 9.74% with a 10% failure risk has about the effect of an 11% cost of capital without it (34:36). A viewer who wants 12% should revisit the failure rate, because 12% plus a 10% failure risk is in effect 13.5–14%, and should let the rate fall as the company grows from under $100 billion to $1 trillion of revenue. *"If Anthropic doesn't scale up revenues and doesn't make money, it'll die on its own. You don't need a high cost of capital to destroy its value"* (38:01). Once a company is public, the range is narrow, so *"finessing the cost of capital is a misdirection of resources."*

## Hurdle rates set too high

The second half of the session applies the argument beyond Anthropic (38:17–48:39).

- **Venture capital and private equity.** VCs cite target returns of 25–50% and PE funds IRRs of 20–30%; *"Both VCs and PE investors are lying"* (39:54), because their actual returns, in a table through September 2026, are *"close to or under what the market delivers."* A target set too high pushes them to *"go for that 100 bagger."*
- **Public companies.** CFOs commenting on his valuation said they use 14%. Setting hurdle rates *"2 to 3% higher than justified by market numbers"* is routine (41:37). The result is under-investment as a company ages, and managers who inflate growth and margins to clear the bar, until *"you're taking made-up cash flows and discounting them at a made-up discount rate"* (43:09). His yearly check: fewer than 30% of listed companies globally earn more than his cost of capital; at a 15% cost of equity and 12.5% cost of capital, *"you probably will get 5% of companies"* (44:17). The [[2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas|McKinsey Global Institute's 2026 arenas report]] names whether AI-foundation valuations will be backed by returns above the cost of capital as an open question.
- **Individual investors.** At a 20% cost of equity *"there isn't a single firm in the S&P 500 that would be undervalued"* (45:04), so the investor holds cash or becomes a target for scams, because the only ones promising to beat 20% are *"scam artists."*
- **Private businesses.** Appraisers build the rate up with thinly sourced premiums: a small-cap premium that has not existed since 1981, a liquidity premium that double-counts a later illiquidity discount, and a *"company specific risk premium… It's just [a] made-up number"* (47:58). At 20–25%, an owner selling to a public company gives the buyer a gift, because *"all of these premiums disappear."*

He closes with currency: in high-inflation currencies such as the Turkish lira or the kwacha, a 20% cost of equity can be right (50:20). His conclusion on Anthropic: the revenue assumption is the one to watch, and of the third-quarter revenue released that day: *"that's not the number that's going to make or break the endgame here"* (49:12).

## Visual canon

Hand-picked from contact sheets of all 42 slide windows (the Gemini stills scan was unavailable); 23 slides were cut at full resolution and 15 are published here. Figures were read from the pixels; values marked *about* are read from bar heights.

### 1 · The restated valuation, line by line

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/01-02m30-restated-valuation-spreadsheet.webp|Restated Anthropic valuation spreadsheet]]

*Still at [2:30](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=150s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

Title: **Claude's Bar Mitzvah Moment**. Story, with parts hidden behind the webcam inset: *"Anthropic will continue to deliver scorching growth in the near term delivering revenues of close to $100 billion next year on its way to generating revenues of $1 trillion of an AI market […] labor and revenues from niche businesses like pharmaceuticals, with its own division. The company has high gross margins, with compute costs becoming fixed costs, and as revenues rise, […] should move higher, with revenues tilted towards premium pricing, but adjusted for higher costs as regulatory risks rise. The main reinvestment will be in compute power, and that cost […] ease over time. The high compute commitments will create the risk of failure, if revenues do not rise near term, but costs of capital will decrease to that of a risky US company (third qua[rtile])."*

| The assumptions | Base year | Next year | Years 2–5 | Years 6–10 | After year 10 | Link to story |
| --- | --- | --- | --- | --- | --- | --- |
| Revenues (a) | $19,708.00 | 400.0% | 43.00% | Changes to | 4.90% | High growth leading into IPO will push [revenues] significantly next year, and as AI products displace labor in selected industries, [the market …] allow for more growth. In some niche businesses, like drugs, Anthropic has potential to generate its own revenues. (partly hidden) |
| Operating margin (b) | −238.39% | 5.0% | Moves to | 27.50% | 27.50% | Margins improve, with pricing power on premium products, and compute costs are largely grow at rates lower than revenues. |
| Tax rate | 0.00% | | 0.00% | Changes to | 25.00% | Global/US marginal tax rate over time |
| Sales to capital (c) | | 3.00 | 3.00 | 3.00 | 32.67% | Compute costs scarcity and costs will ease over time, allowing for lower reinvestment to sustain growth. |
| Return on capital | −8.80% | Marginal ROIC = | 79.69% (years 2–10) | | 15.00% | Closed frontier models with client data create stickiness that will create long term competitive advantages for Anthropic. |
| Cost of capital (d) | | | 9.74% | | 9.13% | Cost of capital starts at about the 90th percentile and moves close to the 75th percentile company over time |

Cash flows, selected years (the slide shows all ten):

| Year | Revenues | Operating margin | EBIT | EBIT (1−t) | Reinvestment | FCFF |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | $98,540.00 | 5.00% | $4,927.00 | $4,927.00 | $14,124.07 | −$9,197.07 |
| 2 | $140,912.20 | 14.00% | $19,727.71 | $19,727.71 | $20,197.42 | −$469.71 |
| 5 | $412,056.44 | 27.50% | $113,315.52 | $113,315.52 | $48,595.19 | $64,720.33 |
| 10 | $1,010,645.76 | 27.50% | $277,927.59 | $208,445.69 | $16,507.21 | $191,938.47 |
| Terminal year | $1,060,167.41 | 27.50% | $291,546.04 | $218,659.53 | $71,428.78 | $147,230.75 |

| The value | | Note on the slide |
| --- | ---: | --- |
| Terminal value | $3,480,632.35 | |
| PV (terminal value) | $1,397,222.59 | |
| PV (CF over next 10 years) | $418,401.53 | |
| Value of operating assets | $1,815,624.12 | |
| Adjustment for distress | $90,781.21 | Probability of failure = 10.00% |
| − Debt & minority interests | $472,335.56 | *Includes lease, purchase and compute commitments, discounted back to today.* |
| + Cash & other non-operating assets | $216,318.00 | *Includes estimated $100 billion from offering with share count adjusted to instrinsic value* |
| Value of equity | $1,468,825.35 | |
| − Value of equity options | $472.30 | *Value of existing employee options* |
| Number of shares | 3,299.29 | *Share count is still tentative, but includes restricted shares to employees* |
| Value per share | $445.05 | Stock was trading at = $525.00 |

No unit is printed; with base-year revenue of $19,708 and an equity value he calls $1.45–1.5 trillion, the figures are in millions of dollars.

*Still vs. transcript:* the narration gives the story's inputs and the result. The spreadsheet adds the path and the bridge: free cash flow is negative in years 1 and 2 and reaches about $192 billion in year 10; the cost of capital falls to 9.13% after year 10; and the $472.3 billion subtracted as debt *"includes lease, purchase and compute commitments."* So the present value of about $373 billion that he gives for the contractual compute commitments is one part of the debt line, with leases and purchase commitments making up the rest. The "Stock was trading at = $525.00" cell is not mentioned.

### 2 · The compute commitments and the 90th percentile, in writing

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/02-03m40-some-added-details.webp|Some added details on the valuation]]

*Still at [3:40](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=220s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

**Some added details**

- **Value per share:** the share count adds the shares outstanding in the balance sheet to the restricted shares granted to employees, and *"will change before the public offering, as bankers adjust it to deliver on a per share value that they believe will make the company more 'sellable'."*
- **Cost of capital choices:** *"I used a 9.74% cost of capital which incorporates risky technology cost of equity and a cost of debt based on a BB+ rating for the company, putting the company at close to the 90th percentile of US companies in 2026."*
- **Compute commitments:** *"my estimate of contractual commitments results in an aggregated value of just over $450 billion and a present value of about $373 billion. It is possible that these numbers will need revisiting as details emerge of these commitments, but this will remain a long-term issue for anyone valuing or pricing the company."*
- **Dilution risk:** Anthropic has used its equity as currency, paying employees with restricted stock and options, and as an add-on to borrowing through convertible bonds; future capital raises will add shares, *"and the larger its ambitions, the greater these issuance will be."*

*Still vs. transcript:* the slide confirms the spoken $373 billion as the present value of the contractual compute commitments alone, from an aggregate of just over $450 billion, and says the numbers may need revisiting. It also places 9.74% near the 90th percentile of US companies, which the narration does not say.

### 3 · Four layers under the $1 trillion revenue target

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/04-06m40-target-revenues-what-can-go-wrong.webp|Target revenues, assumptions and what can go wrong]]

*Still at [6:40](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=400s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

| Layer | Assumptions to get to $1 trillion target revenue | What can go wrong? |
| --- | --- | --- |
| Total market for AI products & services | The AI product and service market will find widespread use across business, increasing productive in some and replacing workers in others, with customers willing to pay high prices to have access to them | The AI products and services may find use only in a subset of businesses, and mostly as a tool. |
| Market for premium products & services | A significant segment of the AI products market will be premium, i.e., for high powered and expesnive models that use customer data and on-the-job learning to become sticky. | The premium part of the AI market may be a small percent of the total market. |
| Anthropic's positioning in premium market | Anthropic is a winner (with a dominant market share) in the premium AI product market, partly because of its fast start in that segment, and partly because it is expending resources (compute power) to build a product moat. | The premium market even if large is splintered and competitive, making it difficult to get and hold large market share. |
| Anthropic's add-on markets | Anthropic will use its success at building premium AI models and agents to become players in businesses, such as pharamaceuticals and some tech, competing and claiming revenues from existing players. | Anthropic may be ill-equipped to operate in tangential businesses, for regulatory, operating and legal reasons. |
| Anthropic's end revenues | Target revenues of $1 trillion in year 10 | Revenues well below $1 trillion |

*Still vs. transcript:* the narration walks the same four layers. The slide adds the mechanisms he does not speak: premium models become sticky through customer data and on-the-job learning, and Anthropic builds its moat by spending on compute. For add-on markets it gives regulatory, operating and legal reasons where the narration uses the Google analogy.

### 4 · Three conditions for a 32.5% margin

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/06-10m50-profitability-what-can-go-wrong.webp|Profitability, assumptions and what can go wrong]]

*Still at [10:50](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=650s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

| Layer | Assumptions to get to 32.5% target margin | What can go wrong? |
| --- | --- | --- |
| Unit economics | With compute costs moved mostly into the fixed costs column, the gross margin for Anthropic on its AI premium products will remain high (>80%) and most of its revenues will come from the premium products | Competition in the premium market can lead to pricing wars, which will lower gross margins. |
| Economies of scale | As revenues grow, the fixed costs at Anthropic (which include compute and employee costs) will grow at a slower rate, leading to improving margins and with enough scale, to higher margins. | Compute costs and employee costs grow at or higher rates than revenues. |
| Sustainability of profits | Once Anthropic gets to its dominant market share, with pricing power, it will be able to hold on to both, in the face of competition, because its agents once embedded in companies becomes sticky and/or regulations keep competition at bay (i.e. moats). | There may be no product stickiness and customers shift to cheaper models (closed or open). |
| Anthropic's target margin | Target operating margin of 32.5% in year 10 | Margins will be much lower than 32.5% |

*Still vs. transcript:* the narration's moat is first-mover stickiness, argued from Windows and Office. The slide names agents embedded in companies as the sticky product and adds a second source of moat the narration leaves out: regulation that keeps competition at bay. It names the failure as customers moving to cheaper closed or open models.

### 5 · What viewers' valuations came to

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/10-20m00-viewer-value-distribution.webp|Value distribution across users of the shared sheet]]

*Still at [20:00](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=1200s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

**Value Distribution – Across Users (of Google Shared Sheet)**. Red bars below $1.25 trillion, a yellow bar for his own range, green bars above.

| Value | Number |
| --- | ---: |
| <0 | 3 |
| 0 to $500 billion | 8 |
| $500 billion – $750 billion | 6 |
| $750 billion – $1 trillion | 5 |
| $1 trillion – $1.25 trillion | 13 |
| $1.25 trillion – $1.5 trillion (yellow) | 12 |
| $1.5 trillion – $2 trillion | 4 |
| >$2 trillion | 2 |

*Still vs. transcript:* he speaks of about 70 valuations; the chart counts 53. Of those, 35 (66%) are below $1.25 trillion, which fits his "65% 70%" too high, and three are negative. The "two out of the 70" above "two" are the two above $2 trillion.

### 6 · Why viewers disagreed

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/11-21m00-viewer-pushback-reasons.webp|Viewer assessment and reasons for disagreement]]

*Still at [21:00](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=1260s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

**And your pushback!** Left pie, *Your assessment of my Anthropic Valuation*: value is too high 51%, value is just right 30%, value is too low 19%. An arrow leads from "too high" to the right pie, *Reasons for Disagreement with my Anthropic Valuation*:

| Reason | Share |
| --- | ---: |
| Gut tells me value is too high | 37% |
| Cost of capital is too low | 23% |
| You are an "academic" | 12% |
| Target revenues are too high | 10% |
| Profit margin is too high (pricing pressures) | 8% |
| No moats | 6% |
| Regulatory apocalypse | 4% |

*Still vs. transcript:* the narration names the top two reasons. The pie gives their shares and the rest of the list: dismissing him as an "academic" (12%) ranks third, and objections to revenues, margins, moats and regulation together make 28%. The left pie puts "too high" at 51%, below the 65–70% he speaks of and the 66% in still 5, so the two charts count differently.

### 7 · A century of US returns, compounded

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/14-26m00-historical-returns-1928-2025.webp|Historical returns on US stocks, bills and bonds]]

*Still at [26:00](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=1560s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

**Historical Returns on Equities – US from 1928 to 2025** (y-axis: compounded annual return)

| Period | US equities | US small cap | 3-month T-bill | 10-year T-bond |
| --- | ---: | ---: | ---: | ---: |
| 1928–2025 | 10.13% | 12.11% | 3.41% | 4.58% |
| 1976–2025 | 11.92% | 12.12% | 4.31% | 6.13% |
| 2001–2025 | 8.74% | 9.65% | 1.77% | 3.34% |

| Period | US equities minus T-bill | US equities minus T-bond |
| --- | ---: | ---: |
| 1928–2025 | 6.72% | 5.54% |
| 1976–2025 | 7.61% | 5.79% |
| 2001–2025 | 6.97% | 5.40% |

*Still vs. transcript:* he reads the three equity returns as averages; the axis labels them compounded annual returns. The chart adds small caps, bills and bonds, and the premium for each window: the premium over T-bonds stays between 5.40% and 5.79% in all three.

### 8 · How the 8.99% and the 3.7% are computed

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/15-28m20-implied-expected-return-on-stocks.webp|Implied expected return on US stocks]]

*Still at [28:20](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=1700s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

**2. The market – an implied expected return on stocks**

- S&P 500 on 9/30/26 = 7651.54.
- Base-year cash flow, last 12 months, across all companies in the index: dividends 81.61 + buybacks 116.56 = cash to investors 198.17.
- Expected earnings and cash-flow growth: 14.59% a year for five years, based on analyst estimates, dropping to 5.29% after.

| | 2025 (actual) | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Earnings | 271.29 | 310.87 | 356.23 | 408.21 | 467.77 | 536.03 | 564.38 |
| Cash payout (%) | 63.52% | 63.52% | 63.52% | 63.52% | 63.52% | 63.52% | 63.52% |
| Dividends + buybacks | 172.32 | 197.47 | 226.28 | 259.30 | 297.13 | 340.48 | 358.50 |

- Equation: `7651.54 = 197.47/(1+r) + 226.28/(1+r)^2 + 259.30/(1+r)^3 + 297.15/(1+r)^4 + 340.48/(1+r)^5 + 340.48(1.0529)/[(r − .0529)(1+r)^5]`. The last term is the expected index level at the end of year 5; after that, earnings and cash flows grow at 5.29%, *"set equal to US T.Bond rate"*, forever.
- Solve for r: **implied expected return on stocks = 8.99%**.
- US $ risk-free rate = 10-year T-bond rate on 9/30/26 minus the default spread for an Aa1 rating = 5.29% − 0.22% = 5.07%.
- **Implied ERP with the US Treasury rate as risk-free = 8.99% − 5.29% = 3.70%**; with the adjusted risk-free rate, 8.99% − 5.07% = 3.92%.
- *Modified payout*: if the payout ratio moves to a sustainable g/ROE in stable growth, the ERP is 4.40%.

*Still vs. transcript:* he gives the index level, the 8.99% and a premium of "about 3.7%", and a T-bond rate "right now" of about 4.9%. The slide shows that the 3.7% is 8.99% minus a 10-year T-bond rate of 5.29% on 30 September 2026. It also gives the forecast behind the 8.99% and two alternative premiums, 3.92% and 4.40%.

### 9 · Implied expected returns since 1960

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/16-29m50-implied-expected-returns-1960-2025.webp|Implied expected return on US equities by year]]

*Still at [29:50](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=1790s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

**Implied Expected Return on US Equities: 1960 to 2025**, one stacked bar a year: T-bond rate (orange) plus implied ERP (green). Read from the bars: above 15% in every year from 1979 to 1984, peaking at about 19.7% in 1981 on a T-bond rate of about 14%; the last bar above 10% is 1994, at about 11.3%; 2022 comes close at about 9.8%; 2025 is about 8.4%. The lowest bars are about 5.3% (1961) and 5.6% (2020, on a T-bond rate under 1%).

*Still vs. transcript:* he says the expected return last exceeded 10% before 1994 and exceeded 15% only in the late 1970s and early 1980s, when T-bond rates were 10–12%. The chart shows the split year by year: the peak years rest mostly on the bond rate, while from 2008 to 2021 the bond rate was low, the premium made up most of the total, and no bar reached 9%.

### 10 · The algebra behind the PE test

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/17-30m50-link-to-pricing.webp|A link to pricing, forward PE formula]]

*Still at [30:50](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=1850s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

**3. And a link to pricing**

- Value of stock = Expected dividends next year / (Cost of equity − Growth rate) = Expected earnings × Payout ratio / (Cost of equity − Growth rate) = Expected earnings × (1 − Growth rate / Return on equity) / (Cost of equity − Growth rate)
- Value of stock / Expected earnings = **Forward PE = (1 − Growth rate / Return on equity) / (Cost of equity − Growth rate)**
- *"If you believe that the cost of equity should be 15% for the average US firm, given that nominal growth in the US economy is about 5% and that the average return on equity across US firms is about 20% (and that is a generous estimate), the PE ratio for US firms today should be roughly 7.27."*
- *"Given that the actual forward PE ratio is closer to 20, you have two choices. One is to sell all your equities, though I am not sure where you would put that money, and the other is to revisit your cost of equity assessment."*

*Still vs. transcript:* the narration skips the algebra (*"trust me on this one"*); the slide gives the derivation. With the inputs as stated (5% growth, 20% return on equity, 15% cost of equity) the formula gives (1 − 0.25) / 0.10 = 7.5 rather than 7.27; 7.27 is what it gives with 4% growth. The conclusion, a PE far below 20, holds either way.

### 11 · Cost of debt by bond rating

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/18-33m20-cost-of-debt-and-bond-ratings.webp|Cost of debt and bond ratings for ten-year bonds]]

*Still at [33:20](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=2000s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

**Cost of Debt and Bond Rating – Ten-year Bonds**: one stacked bar per rating, a 10-year T-bond rate of about 4.9% (the same for every rating) plus the default spread. Total cost of debt, read from the bars:

| Rating | Cost of debt (about) |
| --- | ---: |
| Aaa/AAA | 5.2% |
| A2/A | 5.7% |
| Baa2/BBB | 6.0% |
| Ba1/BB+ | 6.5% |
| Ba3/BB- | 7.4% |
| B2/B | 8.2% |
| B3/B- | 11.0% |
| Caa1/CCC+ | 13.8% |
| Caa2/CCC | 16.7% |
| Caa3/CCC- | 19.5% |
| Ca/CC | 22.3% |

*Still vs. transcript:* the narration says spreads rise as ratings fall and puts Anthropic near BB+ at about 6.5%. The chart shows the shape: the cost of debt stays under about 8.2% down to B2/B, then jumps to about 11% at B3/B- and passes 20% only at Ca/CC. The 10% or more that some viewers proposed corresponds to a B3/B- rating or lower.

### 12 · Why the cost of debt is not a value destroyer

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/19-34m10-anthropic-cost-of-debt-estimates.webp|My Anthropic cost of debt estimates]]

*Still at [34:10](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=2050s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

**My Anthropic cost of debt estimates**

- *"My estimate for the cost of debt for Anthropic reflects their bond rating of BB+, and it is not a value destroyer for two reasons."*
  - *"First, Anthropic may owe a lot in commitments, but they are spread out over time, with about $60 billion coming due next year and $76 billion the year after. Those are large commitments, but Anthropic has a cash balance of $114 billion, which will increase to over $200 billion after the IPO."*
  - *"Second, I am not ignoring the risk of default, because I am incorporating a failure risk of 10%, where Anthropic does run into headwinds, is unable to meet its contractual obligations and has to make fire sale. If your concerns about default are higher, that is the number you should be moving, not the cost of capital."*
- *"In fact, if you ignore failure risk, as many analysts do, and try to jam default risk it into cost of capital, you would need a cost of capital of about 11% to arrive at an estimate of value close to mine."*

*Still vs. transcript:* the narration makes the failure-risk point and the 11% equivalence. The slide adds the schedule and the cash cover he does not speak: about $60 billion of commitments due next year and $76 billion the year after, against cash of $114 billion, rising to over $200 billion after the IPO.

### 13 · Costs of equity and capital by sector

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/20-35m00-cost-of-capital-cross-section.webp|Cost of capital cross section by sector]]

*Still at [35:00](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=2100s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

**Cost of capital: the cross section!**

| Primary sector | Number | CoE 1st decile | CoE 1st quartile | CoE median | CoE 3rd quartile | CoE 9th decile | CoC 1st decile | CoC 1st quartile | CoC median | CoC 3rd quartile | CoC 9th decile |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Communication Services | 2,193 | 6.87% | 8.26% | 9.20% | 10.68% | 17.28% | 6.16% | 7.21% | 8.26% | 8.99% | 9.31% |
| Consumer Discretionary | 6,358 | 7.10% | 7.75% | 8.61% | 10.96% | 17.34% | 6.62% | 6.85% | 7.47% | 7.93% | 9.10% |
| Consumer Staples | 3,202 | 6.37% | 6.65% | 7.39% | 8.20% | 10.96% | 6.03% | 6.33% | 6.76% | 7.39% | 7.72% |
| Energy | 1,402 | 7.16% | 7.16% | 7.60% | 8.71% | 10.96% | 6.59% | 6.98% | 7.16% | 7.27% | 7.51% |
| Financials | 5,278 | 5.30% | 5.47% | 6.11% | 6.49% | 7.77% | 5.02% | 5.14% | 5.27% | 6.26% | 6.44% |
| Health Care | 4,452 | 8.39% | 8.94% | 9.29% | 9.98% | 12.45% | 7.40% | 8.39% | 8.95% | 9.19% | 9.35% |
| Industrials | 9,007 | 7.35% | 7.99% | 9.20% | 10.34% | 12.94% | 6.76% | 7.32% | 7.93% | 9.53% | 9.89% |
| Information Technology | 6,234 | 9.88% | 9.92% | 10.75% | 12.30% | 14.49% | 9.02% | 9.71% | 9.88% | 10.86% | 12.27% |
| Materials | 6,457 | 8.41% | 8.94% | 9.43% | 10.32% | 11.80% | 7.48% | 8.09% | 8.60% | 8.94% | 10.08% |
| Real Estate | 2,671 | 5.95% | 6.22% | 6.67% | 7.85% | 11.83% | 5.16% | 5.36% | 5.49% | 6.00% | 6.23% |
| Utilities | 902 | 6.12% | 6.46% | 6.83% | 7.48% | 10.10% | 5.24% | 5.62% | 5.74% | 5.96% | 6.45% |
| All firms | 6,006 | 5.97% | 7.02% | 8.77% | 10.10% | 12.94% | 5.26% | 6.41% | 7.79% | 9.16% | 9.88% |

CoE = cost of equity, CoC = cost of capital, both in US$. Footnote: *"In US $. To convert into another currency, add the differential inflation rate.. With Indian rupees, for instance, this will add 2-2.5% to every number and with Swiss francs, it would reduce each number by 1.5-2%."* The sector counts add up to 48,156, while the "All firms" row reads 6,006.

*Still vs. transcript:* the figures he reads aloud as cost of capital, for energy (7.16%, 7.6%, 10.96%) and technology (9.88%, 9.92%, 10.75%, 12.3%, 14.5%), are the table's cost-of-equity columns. The cost of capital for technology runs from 9.02% (1st decile) through a 9.88% median to 12.27% (9th decile), which matches his *"between 9 and 12.3%"*; for energy it runs from 6.59% to 7.51%. His 9.74% sits just below the all-firm 9th decile of 9.88%, and the 9.13% that the spreadsheet in still 1 moves to after year 10 is close to the all-firm 3rd quartile of 9.16%.

### 14 · What private equity and venture capital actually returned

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/22-39m10-pe-and-vc-returns-vs-market.webp|Private equity and VC returns against the S&P and Nasdaq]]

*Still at [39:10](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=2350s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

**Professional investors (managing other people's money)**. *"With subgroups of professional investors, especially venture capitalists and private equity, the numbers that they offer as target or expected returns are so staggeringly out of sync with reality that the cynic in you should wonder whether these numbers are marketing props and financial metrics."*

| | 6 months | 1 year | 3 years | 5 years | 10 years | 15 years | 20 years | 30 years |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Private equity | 4.50% | 8.70% | 8.70% | 11.70% | 15.20% | 15.00% | 13.20% | 12.40% |
| S&P 500 | 11.00% | 17.90% | 23.00% | 14.90% | 15.10% | 14.30% | 11.30% | 10.00% |
| VC | 14.10% | 21.10% | 8.70% | 10.20% | 14.90% | 15.50% | 12.90% | 8.10% |
| Nasdaq | 14.40% | 21.30% | 31.10% | 14.00% | 17.80% | 16.70% | 13.70% | 11.70% |

*"I believe that active investors who promise their clients too much (as a expected return) will overreach in terms of the risks they take, and if the target returns they promise are set too high (relative to what they should be), these equity investors will spend their time looking for ten or hundred baggers, rather than solid long term investments."*

*Still vs. transcript:* the narration says PE and VC perform *"close to or under what the market delivers."* The table gives the detail. Over 5 years and longer, private equity returned 11.7–15.2% and VC 8.1–15.5%, far below the 20–50% targets he cites. Both trail the Nasdaq from 5 to 20 years. Against the S&P 500, private equity is ahead over 10 (by 0.1 point), 15, 20 and 30 years, and VC over 15 and 20 years.

### 15 · How many companies beat their cost of capital

![[assets/2026-11-03-damodaran-anthropic-valuation-feedback-loop/23-43m20-returns-vs-cost-of-capital-by-region.webp|Returns against the cost of capital by region]]

*Still at [43:20](https://www.youtube.com/watch?v=W0JDfYSpjnM&t=2600s) from Aswath Damodaran, "Heeding the Feedback Loop: A follow-up to my Anthropic Valuation".*

**With some proof…**

| Sub-region | # firms | ROE | Cost of equity | % ROE > CoE | % ROE − CoE > 5% | ROIC | Cost of capital | % ROIC > WACC | % ROIC − WACC > 5% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Africa and Middle East | 1,958 | 9.71% | 10.82% | 41.01% | 29.83% | 7.84% | 9.23% | 41.22% | 28.14% |
| Australia & NZ | 1,559 | −14.19% | 8.71% | 17.25% | 11.87% | −11.33% | 8.67% | 19.37% | 12.51% |
| Canada | 2,392 | −17.86% | 8.83% | 12.12% | 8.32% | −12.29% | 8.68% | 13.21% | 7.94% |
| China | 7,451 | 3.26% | 10.08% | 20.91% | 10.56% | 2.69% | 8.96% | 23.51% | 13.64% |
| EU & Environs | 4,951 | 4.43% | 9.66% | 29.69% | 20.54% | 4.94% | 8.57% | 33.04% | 23.09% |
| Eastern Europe & Russia | 372 | 4.84% | 10.08% | 24.46% | 17.74% | 3.68% | 9.30% | 19.35% | 12.37% |
| India | 4,520 | 8.73% | 11.02% | 36.42% | 24.85% | 7.07% | 9.52% | 35.22% | 22.85% |
| Japan | 3,760 | 8.13% | 9.80% | 39.57% | 21.49% | 7.74% | 8.35% | 45.19% | 29.15% |
| Latin America & Caribbean | 807 | 7.68% | 11.62% | 32.09% | 21.07% | 7.75% | 9.05% | 39.53% | 24.41% |
| Small Asia | 9,503 | 4.78% | 10.82% | 25.34% | 15.44% | 3.86% | 9.15% | 26.09% | 15.67% |
| UK | 835 | 3.72% | 9.74% | 28.62% | 19.16% | 5.50% | 8.42% | 34.85% | 24.67% |
| United States | 4,770 | −0.20% | 9.24% | 22.12% | 16.06% | 3.41% | 8.38% | 26.62% | 18.66% |
| **Global** | **42,878** | **4.70%** | **9.93%** | **27.00%** | **17.10%** | **4.28%** | **8.78%** | **29.23%** | **18.78%** |

Region names are cut off on the slide ("Africa and Middle Eas", "Eastern Europe & Rus", "Latin America & Carib").

*Still vs. transcript:* the narration gives "less than 30%" globally. The table gives 29.23% of 42,878 firms with a return on capital above the cost of capital and 27.00% with a return on equity above the cost of equity, and only 18.78% beating the cost of capital by more than five points. Regions range from 13.21% (Canada) to 45.19% (Japan); in the United States 26.62% of firms beat the cost of capital, and the aggregate ROE is −0.20%.

## Dynamic-capabilities reading

- **`digital-seizing/balancing-digital-portfolios`**: the hurdle-rate section is about capital allocation: a rate set above what markets justify turns away investments, leads to under-investment as the company ages, and invites managers to inflate the cash flows of the projects they want.
- **`digital-seizing/strategic-agility`**: governance ranks second because his story needs management willing to accept redirection and *"reverse policies that they themselves adopted,"* which he thinks seven like-minded founders make harder.
- **`strategic-renewal/business-model`**: the revenue layers and the moat argument concern Anthropic's value-capture logic: share of a premium segment, add-on businesses beyond supplying models, and stickiness from embedding products in customers' data.

## Linked entities and concepts

- **Entities:** [[Aswath Damodaran]] (channel and speaker), [[Anthropic]] (subject), [[Google]] (self-driving cars as an analogy for add-on markets), [[Microsoft]] (Windows and Office as the model for a technology moat).
- **Concepts:** [[foundation-models]], [[strategy]], [[open-source-ai]], [[warner-wager-process-model]].
- **Dangling** (single-source mention, deferred): CoreWeave, Financial Times, Warren Buffett, Apple.

## Source quality

- **Auto-generated ASR transcript**, cleaned in quotation only; YouTube's 30 chapters are used for navigation. The session is slide-led, with tables of returns and sector costs of capital. The transcript holds what he reads out, not the tables in full. **Stills:** the Gemini stills scan failed on 2026-11-16 (HTTP 402). On 2026-11-17, 15 stills were hand-picked from contact sheets of all 42 slide windows (23 cut at full resolution), verified against the pixels and transcribed under [Visual canon](#visual-canon); they carry the tables in full.
- **Figures that could not be pinned down from speech** (with what the slides show, where they show it):
  - Present value of the compute commitments: about $373 billion here, against $473 billion of debt in the original session (see [[2026-10-28-damodaran-anthropic-ipo-valuation]]). *Resolved by the slides:* "Some added details" gives $373 billion as the present value of the contractual compute commitments alone, from an aggregate of just over $450 billion, and the restated spreadsheet subtracts $472.3 billion of debt that *"includes lease, purchase and compute commitments."* The $373 billion is part of the debt line, not a competing figure (stills 1 and 2). The first session's risks slide values the compute and purchase commitments at $363.0 billion, discounted at 6.28%; neither session's slides account for the $10 billion between the two.
  - Implied equity risk premium: about 3.7%. The implied return of 8.99% minus the ~4.9% T-bond rate he quotes as current gives about 4.1%; the T-bond rate behind the 3.7% is not spoken. *The slide shows it:* 8.99% minus a 10-year T-bond rate of 5.29% on 30 September 2026 = 3.70% (still 8).
  - Technology sector: he says 80% of technology companies sit *"between 9 and 12.3%"*, but the deciles he reads (9.88% and 14.5%) bound a wider range. The first decile, 9.88%, equals the all-US third quartile in the original session. *The slide shows why:* the figures he reads for technology and energy are the cost-of-equity columns; technology's cost of capital runs from 9.02% to 12.27% (median 9.88%), which matches the spoken range (still 13).
  - In the original session he called the technology median "lower" than 9.74%; here it is 10.75%. *On the slide,* 10.75% is the technology median cost of equity; the median cost of capital is 9.88%.
  - "Only two out of the 70 valuations came up with values greater than two": the unit (trillion) is inferred. *The histogram confirms it:* two valuations above $2 trillion, out of 53 counted on the slide (still 5).
  - The forward-PE example: 15% cost of equity, 5% growth and 20% return on equity give 7.5 in the formula on the slide, not the 7.27 spoken and printed; 7.27 corresponds to 4% growth (still 10).
  - The 40% margin-of-safety example is spoken as *"don't buy it unless it's 900 billion lower"*, read here as a price of $900 billion or less.
  - The November implied return was first spoken as 8.76%, then corrected to 8.83%.
- **Standing.** A valuation academic defending his own inputs to his audience. The market-return and sector figures are his own datasets, linked in the description and not fetched. The claim that VC and PE funds return close to or below the market rests on a table the transcript does not show. The table is now transcribed (still 14): over 5 to 30 years PE returned 11.7–15.2% and VC 8.1–15.5%, behind the Nasdaq from 5 to 20 years, but PE ahead of the S&P 500 over 10 to 30 years. No source for the fund returns is printed on the slide. The hurdle-rate section is general corporate-finance argument, not specific to AI.
