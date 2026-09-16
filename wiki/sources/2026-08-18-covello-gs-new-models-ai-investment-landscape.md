---
type: source
kind: video
title: "How New Models Are Changing the AI Investment Landscape"
author: ["Goldman Sachs"]
url: "https://www.youtube.com/watch?v=n4ZwTSQKETs"
date_published: 2026-08-18
date_recorded: 2026-07-30
date_ingested: 2026-09-16
length: "~16:59 minutes (publisher transcript PDF, 58 speaker turns; no caption track exists)"
raw: "../../raw/videos/how-new-models-are-changing-the-ai-investment-landscape.md"
tags: [jim-covello, sharmin-mossavar-rahmani, goldman-sachs, equity-research, investment-strategy-group, ai-capex, enterprise-roi, value-chain, semiconductors, hyperscalers, circular-financing, vendor-financing, model-router, model-optimization-layer, data-management-layer, open-source-ai, open-weight-models, capital-discipline, internet-bubble]
dynamic_capabilities:
  - contextual/external-triggers
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: 2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs
    via: "companion interviews in the same Goldman Sachs Private Wealth series with the same interviewer, recorded two weeks apart. Covello treats the value chain and where the CapEx lands; Hatzius treats the macro aggregates and cites Covello by name for the C-suite-versus-worker exhibit"
    confidence: 0.85
  - type: supports
    target: 2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company
    via: "both address whether enterprises are realising returns on AI spending. The BBC panel cites survey figures (a PwC survey of ~4,500 CEOs finding 56% yet to see a return); Covello states the same conclusion from Goldman's own survey work and adds where the value has gone instead — 'all of the economic value is accrued to the semiconductor companies'"
    confidence: 0.75
  - type: supports
    target: 2026-05-20-agrawal-stanford-mse435-economics-of-generative-ai
    via: "both analyse AI as a layered value chain and ask which layer captures the economics. Agrawal's seminar walks the stack from semis to infrastructure to foundation models to applications; Covello argues the economics are currently stuck at the semiconductor layer and names the missing layer as data management plus model orchestration"
    confidence: 0.75
  - type: supports
    target: 2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai
    via: "both describe routing between rented frontier models and owned or open models as a per-query economic decision. Huang frames it as own-versus-rent per capability for startups; Covello frames it as a model-optimization layer routing high-consequence queries to frontier models and low-consequence queries to open-source models"
    confidence: 0.8
  - type: supports
    target: 2026-07-10-hugging-face-ceo-companies-done-renting-their-ai
    via: "both argue open weights improve enterprise economics. Delangue argues it from inspectability and national positioning; Covello argues it from margin — open models reduce the compute the enterprise must pay the semiconductor layer for, which is how value moves up the chain"
    confidence: 0.75
  - type: contradicts
    target: 2026-08-10-maza-a16z-kavak-rebuilding-a-company-around-ai
    via: "both address whether enterprises are yet making or saving money on AI. Covello, from Goldman's survey work across companies: 'enterprises collectively are not making or saving money on their AI implementations.' Maza reports a single firm handling 96% of interactions and 95% of transactions with agents at 2.1x human conversion and stated profitability. The comparison differs in unit — a cross-sectional aggregate against one firm that rebuilt itself around agents — and Covello's own diagnosis of what is missing is close to what Kavak says it built"
    confidence: 0.8
---

# How New Models Are Changing the AI Investment Landscape

> As consumer adoption and corporate investment in artificial intelligence accelerate, markets are demanding greater transparency into profitable enterprise adoption. Sharmin Mossavar-Rahmani, chief investment officer of Wealth Management and head of the Investment Strategy Group (ISG), and Jim Covello, head of Global Equity Research for Goldman Sachs, unpack what investors should consider about increasing corporate AI capital expenditures, the impact of open-source and open-weight models, and why Covello believes many of the sector's biggest winners may still lie ahead.
>
> Recorded on July 30, 2026.

## TL;DR

A ~17-minute **Goldman Sachs** Private Wealth Management interview, **recorded 30 July 2026** and published 18 August. **Sharmin Mossavar-Rahmani** interviews **Jim Covello**, head of **Global Equity Research** at Goldman — a semiconductor analyst for about 16 years, ranked #1 by *Institutional Investor* for nine of them.

The interview has a single organising question and everything else hangs off it.

1. **The question that subsumes the rest.** *"It all starts with: does the end customer, does the end user make or save money implementing AI or not?"* His answer for today is unambiguous: *"right now, **enterprises collectively are not making or saving money on their AI implementations**."* Not that nothing works — *"there's certainly a lot of use cases where it's been successful"* and *"thousands and thousands of applications that are being used by enterprises"* — but that it *"is not resulting yet in net savings."*

2. **Consumer adoption cannot pay for the infrastructure.** *"On the consumer side, the adoption of the technology has been magnificent, faster than anything any other technology we've ever seen. But… **95% of consumers are using a free version of AI**. So we're not going to monetize the significant infrastructure investment on the consumer side. It's going to have to come from profitable enterprise adoption."*

3. **The analogy that defines what "working" would look like.** *"If you and I go on Amazon, that's a cheaper option for us than going to the store… The advertisers are getting a better ROI bang for their buck advertising on Google than on print advertising. **And that's what's missing right now.**"* The benchmark is not capability; it is a demonstrable cost or revenue advantage to the buyer.

4. **Where the money has actually gone — and why he calls it unsustainable.** *"According to all of the survey work that we've done, **all of the economic value is accrued to the semiconductor companies**, and that's great for now for the semiconductor companies. But that's completely unsustainable unless the end customer or the end user or the enterprises start to make or save money implementing AI. That's where I think everybody's research and focus should be at this point."* He explicitly subordinates the other debates to it: hyperscaler ROI, *"the circular financing issue, all the societal issues around where data centers are — look, all of those things are **byproducts** of is the end customer making or saving money."*

5. **The missing layer, and the reason he thinks the model-capability framing misses.** *"People talk about this technology will get unlocked when the new, more capable model comes out. I think the models are incredibly powerful and incredibly capable. I think a lot of the agents are very powerful and very capable, but right now **I think we're building agents on top of data that isn't ready to be agents**. And the bigger the organization, the more complex that issue is."* What he says is needed instead is two layers: a **data management layer**, and a **model optimization or orchestration layer** — *"I think you're going to have a model optimization layer built into all enterprises that routes the **high-consequence queries** to the big frontier models that are a little more expensive to use, and then it'll route the **low-consequence queries** to the open source model."* His assessment of its maturity: *"That model optimization or model router really is yet to be developed in most organizations. It's really important. **It's not talked about enough.** There's a whole lot of really interesting companies, mostly private companies, working on it. And I think that's going to be one of the big keys to unlocking the economic value of AI in the enterprise."*

6. **Open weights are an enterprise-margin argument, and a threat to the semiconductor layer.** *"Open source really benefits the enterprise customer. I think open source models will make it more likely that enterprises can profitably implement AI."* The value-chain consequence is the part worth keeping: *"I think it's really good for the hyperscalers because it's more likely then you're going to be able to profitably fill up all this capacity that you're adding. And then I think it's **more of a challenge to the semiconductor layer** that's benefited from the massive compute power that the frontier models require. If you can build models that don't require as much compute power, then the customers can start to shift some of the economic value from the semiconductor companies… further up in the chain."*

7. **He rejects the China-versus-US framing of open source outright.** *"This has become a little bit of an issue of open source is China and frontier is the US. I don't actually see that as being the long-term dynamic here. Open source has been around forever in different flavors. Linux was an open source operating system. Red Hat on top of Linux was an open source software company. Meta's model is an open-weight model. **This isn't a China versus US thing.** I think ultimately you're going to have US open source and open weight as well."* And on distillation: *"it's not to me about distillation or stealing code… **smaller, faster, cheaper is what powered technology innovation since the beginning of time.**"* The strategic question he substitutes: *"how long of an advantage do you have by having that expensive frontier model versus how quickly the fast followers can come with cheaper technology?"*

8. **A prediction with a clear shape: nobody runs on frontier models alone.** *"**I don't think enterprises will ever successfully implement AI only using frontier models.** I think they're going to have to use frontier models, because the high-consequence queries are going to demand the most powerful models, but then there will be open source and open weight models that can take care of a lot of the rest of the queries."*

9. **The market has become the forcing mechanism, and he welcomes it.** *"Up until relatively recently, every time one of these companies would announce higher CapEx, the market would reward that company. Over the last quarter or so, you've really seen a significant shift, where the market is questioning that a lot more. I think that's really healthy… the market is now demanding more line of sight, more visibility on an immediate ROI. **We're in a different part of the AI investment cycle today than at any time over the last couple of years.**"* The interviewer supplies the price action he is responding to: from mid-May peaks to end-July, S&P 500 down ~2%, hyperscalers down low-teens, semiconductors high-teens, large GPU manufacturers nearly 20%.

10. **Two scenarios, and they point in opposite directions for the two layers.** If enterprises start implementing profitably, cash flows back to the hyperscalers and *"they would outperform the semiconductor companies."* If they don't, capital discipline forces hyperscalers to slow — *"we're not talking about companies going from $200 billion a year to zero. We're talking about just digesting some of the capacity that they've added. I think that would be very bullish for the hyperscaler companies. And obviously a lot more problematic for the semiconductor companies who are getting all the revenue from those hyperscalers."* Note that **the hyperscalers do better in both** — the asymmetry is entirely on the semiconductor side.

11. **Two kinds of circular financing, only one of which worries him.** *"If the company is subsidizing the investment of one of their customers in order to incentivize that customer to use their chips instead of somebody else's chips, I think that's okay. That's just another form of discounting. That's very different from: **if I don't give this customer this money, they're not going to be able to make those investments.** That's much more problematic. I don't think that's the sign of a very healthy supply chain."*

12. **His forecasting stance, and the lesson he carries from 1999.** Asked how he reconciles forecasting with Geoffrey Hinton's *"nobody should do any forecast"*: *"I take my responsibility to be very fundamentally driven as opposed to thematically driven… I'm using the current state of play to drive a lot of the forecasting, as opposed to blind belief."* And: *"I grew up covering tech stocks as the internet bubble was bursting… **my lesson from the internet is it was a different group of companies that were the ultimate winners.** Google, one of the greatest companies in the world, came out of that era. There was a whole lot of companies that Google was competing with in that era that nobody ever heard of again."* His applied version: *"the data management, orchestration, model optimization layer is a bunch of companies that most people have never heard of yet."*

13. **Why enterprise adoption is slow, read off a safety incident.** Asked about a model escaping its sandbox in testing: *"My big takeaway from that is, when people want to understand why enterprise adoption has been so much slower than maybe people thought three years ago… **This is why.** You have to be so careful. You have to have so many guardrails. You have to put things in a sandbox. And even then, sometimes it's dangerous. If you're a consumer, you can use this and feel comfortable… If you're an enterprise, you can't do that."*

## How this source touches the Warner & Wäger cells

- **`digital-seizing/balancing-digital-portfolios`** — claim 5 is the cell almost exactly: the model-optimization layer is a standing capital-allocation decision made per query, routing high-consequence work to expensive frontier models and low-consequence work to cheap open ones (~4:17–5:03). Claims 9–10 are the same decision at the investor's altitude — whether hyperscaler CapEx budgets are disciplined by visible ROI.
- **`digital-transforming/improving-digital-maturity`** — claim 5's *"we're building agents on top of data that isn't ready to be agents"* (~4:04) is a maturity diagnosis rather than a technology one, and claim 13 attributes the slow pace to the guardrail and sandbox work enterprises must do before agents can touch anything consequential (~14:00–14:30).
- **`contextual/external-triggers`** — the shift in market posture toward CapEx over "the last quarter or so" (~7:46–8:42) is an external condition now disciplining firm behaviour, not a choice any single firm made.

## Related in this wiki

- **Whether enterprise AI is paying.** [[2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company]] carries the survey figures the debate usually runs on; [[micro-productivity-trap]] holds the named failure mode; [[2026-08-10-maza-a16z-kavak-rebuilding-a-company-around-ai]] is a single firm reporting the opposite outcome, and reports building roughly the layer this source says is missing.
- **The value chain by layer.** [[2026-05-20-agrawal-stanford-mse435-economics-of-generative-ai]] walks the same stack in a seminar format.
- **Routing between owned and rented models.** [[2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai]] makes the per-capability version of claim 5; [[ai-sovereignty]] holds the layer-choice framing and [[open-source-ai]] the open-weights argument; [[small-language-models]] holds the case for what the cheap leg of the router runs on.
- **The open-weights case, argued differently.** [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai]] argues open weights from inspectability and national positioning; this source argues them from margin — cheaper models move economic value off the semiconductor layer and up the chain toward the buyer. Both also dismiss distillation as the explanation for cheap capable models.
- **The macro aggregates beneath this.** [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs]] is the companion interview.

## Linked entities and concepts

- Entities: [[Goldman Sachs]] (publisher and employer of both speakers).
- Concepts: [[micro-productivity-trap]], [[enterprise-ai-adoption]], [[agent-harness]], [[open-source-ai]], [[ai-sovereignty]], [[small-language-models]], [[warner-wager-process-model]].
- **Dangling** (single-source mention, deferred): **Jim Covello** (also named on the companion source, but as a cited colleague rather than an author — promotes on a third citation), **Sharmin Mossavar-Rahmani**, **Geoffrey Hinton** (quoted), **Investment Strategy Group**, **Global Equity Research**.

## Source quality

- **Transcript provenance.** No caption track exists on this video; the text is **Goldman's own transcript PDF**, converted with `pdftotext` and co-located with the raw file (gitignored). See the raw file's `notes:` for the fetch method, which needs a browser.
- **The publisher's transcript dropped a negation that reverses a premise.** *"We know consumers are paying that much"* should read *"**aren't** paying that much"* — the sentence is the setup for the 95%-on-the-free-tier point in claim 2. Corrected at acquire time and itemised in the raw file. One further correction is **inferred, not certain**: *"see it on the panel"* → *"see it on the **P&L**"* (~6:02).
- **Same disclaimer mismatch as the companion source.** The description states the video *"is not a product of Goldman Sachs Global Investment Research (GIR). It is not research."* Covello **heads Global Equity Research**, and the claim that *"all of the economic value is accrued to the semiconductor companies"* is explicitly sourced to *"all of the survey work that we've done"* — i.e. Goldman research. Treat the figures as reported in an interview, not as a citable research product; **the underlying survey work is not named, sized, or dated anywhere in the interview.**
- **The central empirical claim is unfalsifiable as stated.** *"Enterprises collectively are not making or saving money"* has no sample, no measure, no time window and no definition of "collectively." It is a strong claim from someone with access to the data, and it is not checkable from this source.
- **Standing and interest.** Covello is the most prominent sell-side sceptic on AI economics and has held this position publicly for roughly two years; that consistency is a virtue for interpreting his view and a caution against treating this as an independent update. Goldman also has a large business on every side of this trade.
- **Recorded on 30 July 2026**, nineteen days before publication, and claim 9's market-posture argument rests on price action through end-July. The market-cycle claims are the most perishable content here.
- **Scope.** Full interview ingested, 0:00–16:42 of a 16:59 runtime.
