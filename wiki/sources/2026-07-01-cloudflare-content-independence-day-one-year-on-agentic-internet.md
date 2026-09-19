---
type: source
kind: article
title: "Content Independence Day, one year on: building the business model for the agentic Internet"
author: ["Arielle Weiss", "Zach Albertson", "Emily Lanfear"]
publisher: "The Cloudflare Blog (Cloudflare, Inc.) — company report; data from Cloudflare Radar and the Cloudflare Investor Day 2026 deck"
url: "https://blog.cloudflare.com/agentic-internet-bot-report/"
date_published: 2026-07-01
date_ingested: 2026-09-19
length: "~2,400 words (full post, Parts I–V + methodology; HTML-converted; 7 charts linked but not transcribed)"
raw: "../../raw/articles/2026-07-01-cloudflare-content-independence-day-one-year-on.md"
tags: [cloudflare, cloudflare-radar, content-independence-day, agentic-web, agentic-internet, ai-crawlers, training-crawlers, mixed-use-crawlers, bot-traffic, non-human-traffic, referral-traffic, zero-click, google-zero, open-web, publishers, content-licensing, pay-per-crawl, crawl-to-referral-ratio, google, data-commons, vendor-report]
dynamic_capabilities:
  - contextual/external-triggers
  - strategic-renewal/business-model
  - digital-transforming/navigating-innovation-ecosystems
relationships:
  - type: published-by
    target: Cloudflare
    via: "a company report on the Cloudflare blog, written by three Cloudflare staff"
  - type: depends-on
    target: 2026-06-09-cloudflare-investor-day-2026
    via: "the post's methodology note names two data sources, Cloudflare Radar and the Investor Day 2026 deck. The adoption-speed comparison, the open-web share of attention and the 35–40% industry traffic declines are the deck's slides restated"
    confidence: 0.9
  - type: supports
    target: 2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook
    via: "the collapse of search referral traffic, measured from both ends. Cloudflare sees human traffic fall as much as 40% in under a year in the most-crawled categories, with software among them; HubSpot, a software firm, reports losing 80% of its own traffic as buyers moved research into AI assistants"
    confidence: 0.8
  - type: supports
    target: 2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china
    via: "search-driven discovery giving way to agent answers. Ognibeni predicted agents would handle search-driven e-commerce so that 'nobody will show up in your store'; Cloudflare reports retail among the industries losing 35–40% of human traffic and agent traffic passing half of all Internet traffic"
    confidence: 0.7
  - type: supports
    target: 2026-04-28-ai-index-report-2025
    via: "the data commons closing. The AI Index reports AI-training restrictions on actively maintained C4 domains rising from 5–7% to 20–33% in a year; Cloudflare carries the trend forward at network scale — AI training crawlers blocked by default on new domains since July 2025, after the AI Index's measurement window — and reports publishers using that control to negotiate"
    confidence: 0.75
  - type: supports
    target: 2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells
    via: "the intermediary taking the customer relationship. DFI's CEO fears agents will sit between the retailer and its shopper; Cloudflare describes the same shift for any publisher of information — content consumed inside AI answers 'without audiences ever visiting the source'"
    confidence: 0.65
---

# Cloudflare — Content Independence Day, one year on

> One year after declaring Content Independence Day, a dynamic market for monetized content has officially emerged. In this report, we examine how the rise of autonomous AI agents is upending traditional search referrals and detail the new infrastructure required to support a sustainable web economy.

## TL;DR

A company report on the Cloudflare blog, published 1 July 2026 by **Arielle Weiss, Zach Albertson and Emily Lanfear**, a year after [[Cloudflare]] declared "Content Independence Day" and started **blocking AI training crawlers by default** on new domains. It is the corpus's first source measured from **the network layer**: what crosses a network carrying more than 20% of the web, not what a firm or a panel reports.

The claims it adds to the wiki:

- **Agent traffic now exceeds human traffic.** *"More than 50% of traffic on the Internet is now non-human."*
- **Crawling has changed purpose.** **52% of crawler requests are for AI training** as of June 2026, up from 22% in spring 2025; **mixed-use crawlers** (search, agent and training in one) make up more than 36%; pure search crawling is *"a small and declining share."*
- **The referral bargain is broken.** Content is still crawled and used, but traffic no longer comes back. The most-crawled categories (retail, software, IT, finance) have lost **as much as 40% of human traffic in under a year**. Publishers plan for **"Google Zero."**
- **Control created a market.** Default blocking created scarcity, scarcity created leverage, and leverage produced licensing: **more than 50 publisher–AI agreements since 2023**. But licensing is *"largely bespoke and unlikely to fully replace lost referral, advertising, and affiliate revenue."*
- **Google is the structural problem.** Google carries about **88% of referral traffic** and uses one mixed-use crawler, so a site cannot stay in Google Search without also feeding Google's AI. By Cloudflare's measure this gives Google **about 2× more information** than leading AI companies.

## Key claims

### Part I — the change

- **Adoption speed.** Generative AI reached **2.5 billion active users, over 30% of humanity, in 3.5 years**, *"more than 2x the speed that smartphones were adopted."*
- **Attention leaves the open web.** *"For every hour spent online searching for information, only 15 minutes is spent on the open web."* The deck this figure comes from labels it *"illustrative / directional … not a single measured series"*; see [[2026-06-09-cloudflare-investor-day-2026|the Investor Day deck]].
- **More than half of traffic is non-human**, a threshold crossed *"this year … for the first time."*
- **Crawler composition, by purpose:** training 52% (from 22%), mixed-use over 36%, search small and falling. Mixed-use crawlers put content owners in a bind: *"choose between remaining discoverable in the agentic era, and giving away their most valuable content without compensation."*
- **The old model:** content was exchanged for search visibility, which returned referral traffic, which funded the content. *"If content is consumed without audiences ever visiting the source, how do content creators sustain themselves?"*
- **It is no longer only media.** News was hit first; retail, software, IT and finance now show the same pattern.

### Part II — the market

Cloudflare's three commitments were **transparency and control** for site owners, **tools that create scarcity**, and **a marketplace** for licensing. Its account of what happened is a chain: *"Transparency created scarcity. Scarcity created leverage. Leverage accelerated licensing."*

The leverage came from information. Publishers gained **operator-level attribution**: which models crawled, how often, which URLs were most in demand, and their **crawl-to-referral ratios**. That *"reduced information asymmetry in licensing discussions."* Enforcement at the network layer is presented as *"far more effective than voluntary standards like robots.txt."*

The results: more than 50 publisher–AI agreements since 2023, major AI companies licensing *"differentiated and premium content"*, and collective licensing emerging. *"The conversation is no longer whether content should be compensated. The conversation now is how."* The limits are stated just as plainly: deals are bespoke, supply and demand are hard to match, and *"content valuation is still unresolved."*

**The Google convergence problem.** Most AI companies run separate discovery and training crawlers, so publishers can allow one and block the other. Google does not. Its mixed-use bot means a site *"cannot … participate in Google's search ecosystem without also participating in Google's AI ecosystem,"* and it hides from the publisher *why* a page is being fetched.

### Part III — Cloudflare's vantage

More than 20% of the web is behind Cloudflare, as are 36% of the most-visited sites, more than 40% of the Fortune 500, and nearly 80% of leading AI companies. *"We see the content owners creating content, the AI companies consuming it, and the signals increasingly connecting them."*

### Parts IV–V — what the market needs

1. **Transparency as the standard.** Verifiable bot self-identification and declared crawl intent. More than a third of crawler activity is still mixed-use, and Cloudflare says it aims to *"drive that number to zero by this time next year."*
2. **Better signals.** Real-time freshness and quality signals so AI companies crawl what changed, not everything. Indiscriminate crawling *"wastes compute for AI companies and creates unnecessary bandwidth burden for publishers."*
3. **Discovery before pricing.** *"Better discovery must precede better pricing."*

The end state it argues for is *"programmable, scalable mechanisms for content discovery and monetization"*, with permissions, licensing and payment handled in the request path. The Investor Day deck shows what that means in product terms (x402, Web Bot Auth, pay-per-crawl).

## Neighbour sources

- **Upstream data.** The post's methodology cites [[2026-06-09-cloudflare-investor-day-2026|Cloudflare's Investor Day 2026 deck]] alongside Radar, and several headline figures are that deck's slides restated. Read the two together. The deck is where the claims are qualified (the attention-share chart is marked illustrative) and where the commercial motive is explicit.
- **The same collapse, from a firm.** [[2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook|HubSpot]] lost 80% of its web traffic as buyers moved research into AI assistants. That is the single-firm version of the 35–40% category-level declines here.
- **Predicted, then measured.** [[2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china|Ognibeni]] predicted that agents would kill search-driven e-commerce, and [[2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells|DFI's CEO]] feared the same from the retailer's side. Cloudflare's retail figures are the first measurement of it in the corpus.
- **The data commons.** [[2026-04-28-ai-index-report-2025|The AI Index 2025]] reports websites restricting AI-training access at rising rates. Cloudflare's default block, introduced after the AI Index's 2023–24 measurement window, applies that restriction at network scale, and this post argues it turned a defensive measure into a market.

All five are gathered on [[agentic-web]].

## What was actually ingested

The full post (Parts I–V and the methodology note), converted from the page HTML. **The seven charts are linked but not transcribed**; only figures stated in the prose are recorded here. The post gives no sample definitions: "traffic" is not defined as requests or bytes, and "leading AI companies" is not listed.

## Dynamic-capabilities reading

- **`contextual/external-triggers`**: a textbook changing-consumer-behaviour trigger. Users *"simply type a prompt and receive a nearly instantaneous, consolidated answer"* instead of visiting sites, and non-human traffic now exceeds human traffic. Any organisation that publishes information online is exposed.
- **`strategic-renewal/business-model`**: the post is about the value-capture logic of the open web being replaced. The old logic was content for visibility for referral revenue. The candidate new ones are licensing, pay-per-crawl and programmatic content markets. Publishers are having to renew the business model itself, not optimise within it.
- **`digital-transforming/navigating-innovation-ecosystems`**: the market Cloudflare describes is an ecosystem of publishers, AI labs, collective-licensing bodies and an infrastructure intermediary. Its argument is about the rules of participation, such as declared crawl intent and separating discovery from training access.

## Linked entities and concepts

- Entities: [[Cloudflare]]
- Concepts: [[agentic-web]], [[responsible-ai]], [[ai-agents]]
- **Dangling** (single-source mention, deferred): Arielle Weiss, Zach Albertson, Emily Lanfear.

## Scope and reliability

**A vendor report with a product to sell.** Cloudflare sells the crawler controls, analytics and marketplace this post argues are needed. The causal chain (transparency → scarcity → leverage → licensing) is the company's account of its own product's effect, and the 50+ agreements are an industry count, not deals Cloudflare brokered.

**The network data is real but not audited.** Radar is a genuine measurement platform, and the crawler-purpose and non-human-traffic figures are the kind of thing only a large network can see. But Cloudflare's customer base is not the whole web, "traffic" is not defined, and the classification of crawler purpose is Cloudflare's own.

**Not every figure is measured.** The "15 minutes of every hour" figure matches the deck's attention-share chart, which the deck itself labels illustrative and not a single measured series. The 2× Google information advantage is asserted without its method. The +1,700% agent-request growth appears in the deck, not in this post.
