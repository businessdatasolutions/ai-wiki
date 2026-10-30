---
type: source
kind: video
title: "Building an open agentic Internet: Discoverable, callable, and payable (Cloudflare Connect 2026)"
author: ["Cloudflare Developers"]
publisher: "Cloudflare — Cloudflare Developers channel, Cloudflare Connect 2026"
url: "https://www.youtube.com/watch?v=_LYr4dSmdsk"
date_published: 2026-10-25
date_ingested: 2026-10-30
length: "~33:33 minutes (transcript ~255 lines + 4 stills)"
raw: "../../raw/videos/building-an-open-agentic-internet-discoverable-callable-and-payable-cloudflare-connect-2026.md"
stills: "../../raw/videos/building-an-open-agentic-internet-discoverable-callable-and-payable-cloudflare-connect-2026.stills.md"
tags: [cloudflare, cloudflare-connect, michael-tremante, agentic-web, ai-crawlers, crawl-to-referral, publishers, pay-per-use, monetization-gateway, x402, net-dollar, open-index, crawl-endpoint, web-bot-auth, content-licensing, residential-proxies, content-resellers, nieman-lab]
dynamic_capabilities:
  - strategic-renewal/business-model
  - digital-transforming/navigating-innovation-ecosystems
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet
    via: "the same company's account of crawler traffic, publisher losses and the move from blocking to monetising"
    confidence: 0.8
  - type: supports
    target: 2026-06-09-cloudflare-investor-day-2026
    via: "human-traffic declines, x402 and signed agents, from the same company to different audiences"
    confidence: 0.75
  - type: supports
    target: 2026-10-17-roth-verge-websites-closing-doors-to-ai-agents
    via: "sites controlling agent access, the signed-agent route, and agents that get round the controls"
    confidence: 0.6
  - type: contradicts
    target: 2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet
    via: "whether agents need new rails on the site side (a crawl endpoint, an index, payment on request) or should use the existing web through browsers"
    confidence: 0.55
---

# Tremante (Cloudflare Connect) — building an open agentic Internet

> Agents are a new kind of visitor. They don't render your CSS or click your ads, but there's a paying human on the other end of every request — block them and you block your customer. Today, billions of those requests are bots re-fetching pages that haven't changed, which is machine effort with no outcome for either side. This talk lays out the four primitives of a web reshaped around this visitor — readable, discoverable, callable, and payable — plus the identity layer underneath and why they have to be built on open standards. How agents read, discover, call, and pay will decide whether the Internet stays open or whether a handful of stacks own discovery, identity, and payments and everyone else routes through them.

## TL;DR

A 33-minute talk with Q&A at Cloudflare Connect 2026 by **Michael Tremante**, VP and Field CTO at [[Cloudflare]]; the title slide names him and the narration does not. Five claims:

1. **Most requests for web pages are bots.** 66.0% of HTTP requests for HTML pages, on Cloudflare Radar. Training and combined training-and-search crawling make up about 80% of declared crawl purpose; search alone 12.8%.
2. **The crawl gives little back.** For every human it refers, Perplexity crawls 3,400 times, OpenAI 606.5 and Anthropic 486.6. Publishers lost human traffic: Digital Trends fell 97% from peak, per Nieman Lab.
3. **A deal market is forming at the top.** Tremante says most large news publishers now have deals with frontier-model providers, public or not. The smaller players need something else.
4. **Cloudflare offers tools on both sides.** A `/crawl` endpoint serving markdown to signed bots, an opt-in open index of sites behind its proxy, and new-domain signals shared with OpenAI, which he says surfaced several million domains.
5. **Two ways to get paid, of different maturity.** The **Monetization Gateway** charges at access (HTTP 402, x402 protocol) and is in private beta. **Pay Per Use** pays on each reuse of crawled content, relies on trust, and is still in development: *"a frontier model provider only needs to crawl you once and they may reuse that content a 100,000 times."*

## Key claims

### The premise

Tremante runs the news site for his home town in Italy for a friend and has watched human traffic and ad and subscription revenue fall in the logs. That morning he had asked Claude when a PHP patch came out rather than visit php.net: *"Did I as a human go to php.net? No."* Those who earn from human visits suffer first, and he expects it to reach research journals, weather, e-commerce and small blogs. AI browsers add a detection problem, since they can crawl while looking like *"legitimate humans."*

He frames this as a business-model change with precedents (Napster to Spotify, Blockbuster to Netflix, print to online), and frames Cloudflare as *"the impartial party"* between publishers and model providers. Direct deals suit both sides: the provider stops fighting mitigations and gets fresher data, and fresh data matters because stale answers mislead (his example is AI Overviews on health advice).

### Three tools before any payment

- **Easier to crawl.** A dashboard option gives signed, verified bots a `/crawl` endpoint that returns the site as markdown, so the crawl does not hit the origin server. He had sites taken down by Meta's crawlers while trying to give them product catalogues.
- **Easier to search.** A planned open index of sites behind Cloudflare's proxy, *"give or take … 20% of the internet"*, opt-in, so providers can use the index rather than crawl. Still *"very much under development."*
- **Easier to discover.** New domains that opt in are signalled to providers. A trial with OpenAI on a small share of traffic surfaced *"several million new domains."* He calls this the win for small players, who otherwise are *"no one on the landscape."*

A separate standard for declaring what bots may do with content (training, inference, referral required) is *"trust-based"* and still being pushed through the industry.

### Getting paid

| | Monetization Gateway | Pay Per Use |
| --- | --- | --- |
| Charges for | access, at request time | each later use of crawled content |
| Mechanism | 402 response, payment, retry with proof | provider accepts a price set on the dashboard |
| Depends on | cryptographic proof | trust, for now |
| Status | private beta | in trial with some large content providers |
| Pricing | owner sets it per endpoint | *"more of a bidding system"*, like Google AdWords |

The gateway can also charge for API calls (*"1 cent for every API call"*) and suits players too small for signed agreements. x402 is an open standard from a foundation built with Coinbase and other firms, and it can run without a proxy. Cloudflare's stablecoin, NET Dollar, is *"one piece of the puzzle"* for micropayments at scale.

### From the Q&A

- **Pricing.** *"Most people have no idea how to price."* Gateway owners choose; the bidding system for reuse is unfinished.
- **Discoverability against monetisation.** *"It's your decision."* A small news agent may give access away to grow while a large one charges from day one.
- **Structure.** Markdown is the format agents accept, and the big publishers keep agent-optimised alternatives; he calls agent optimisation the new SEO.
- **Resellers.** Agents sign up to subscriptions, crawl everything and redistribute it. Residential proxies are the simple case of evasion, and the web archive is being abused. Without bot detection *"it's a race to the bottom."*
- **Freshness.** An election office wants to be crawled and asks how updates reach agents. Change notifications are planned, not live.
- **Old content against new.** *"I don't have the perfect answer."* He expects value to fall over time and the system to price it so.

## Dynamic-capabilities reading

- **`strategic-renewal/business-model`**: advertising and subscriptions tied to human visits giving way to licensing deals, payment on access and payment on reuse.
- **`digital-transforming/navigating-innovation-ecosystems`**: open standards (x402, signed agents) and an index as shared rails among publishers, model providers and a proxy in the middle.
- **`contextual/external-triggers`**: AI crawlers and chat answers cutting human traffic across a whole industry.

## Visual canon

### 1 · More than half of all traffic on the Internet is automated

![[assets/2026-10-25-tremante-cloudflare-connect-open-agentic-internet/03-03m06-more-than-half-of-all-traffic-on-the-internet-is-automated.webp|More than half of all traffic on the Internet is automated]]

*Still at [3:06](https://www.youtube.com/watch?v=_LYr4dSmdsk&t=186s) from Cloudflare Developers, "Building an open agentic Internet".*

**Bot traffic**, share of HTTP requests for HTML pages: **6.6 in 10**. 66.0% of HTTP requests for HTML pages are generated from bots.

| Crawl purpose (share of automated crawl traffic, by declared purpose) | |
| --- | ---: |
| Training | 41.8% |
| Training & Search | 38.4% |
| Search | 12.8% |
| User action | 5.2% |
| Undeclared | 1.8% |

Source: radar.cloudflare.com

*Still vs. transcript:* the purpose table, of which the talk gives only search at about 13%. The measure is HTML page requests, narrower than the slide's title (*"all traffic"*).

### 2 · Human traffic is declining

![[assets/2026-10-25-tremante-cloudflare-connect-open-agentic-internet/04-04m42-human-traffic-is-declining.webp|Human traffic is declining]]

*Still at [4:42](https://www.youtube.com/watch?v=_LYr4dSmdsk&t=282s) from Cloudflare Developers, "Building an open agentic Internet".*

| Publication | Peak traffic | Peak month | Jan 2026 | Decline |
| --- | ---: | --- | ---: | ---: |
| Digital Trends | 8,530,891 | Mar 2024 | 264,861 | −97% |
| ZDNet | 7,610,480 | Feb 2024 | 768,792 | −90% |
| The Verge | 5,322,037 | Feb 2024 | 790,002 | −85% |
| HowToGeek | 1,974,331 | Feb 2024 | 293,898 | −85% |
| TechRadar | 15,577,298 | Jul 2024 | 4,045,783 | −74% |
| Wired | 7,754,067 | Nov 2024 | 2,976,994 | −62% |
| Tom's Guide | 16,013,790 | Jul 2024 | 7,986,572 | −50% |
| CNET | 20,294,300 | Nov 2024 | 10,655,803 | −47% |
| PCMag | 12,667,236 | Jul 2025 | 7,449,728 | −41% |
| Mashable | 16,114,803 | May 2024 | 11,331,018 | −30% |

Source: Nieman Lab

*Still vs. transcript:* the table. The talk names only Digital Trends, and only as *"a third party organization."* All ten are technology publications, and the slide does not say what share of the fall comes from AI.

### 3 · Crawl-to-referral ratios

![[assets/2026-10-25-tremante-cloudflare-connect-open-agentic-internet/05-06m00-so-how-much-value-is-training-generating-for-website-owners.webp|So how much value is training generating for website owners?]]

*Still at [6:00](https://www.youtube.com/watch?v=_LYr4dSmdsk&t=360s) from Cloudflare Developers, "Building an open agentic Internet".*

| Company | Crawls per referral | Change | Bots |
| --- | ---: | ---: | --- |
| Perplexity | 3.4K : 1 | +4.4% | PerplexityBot 87.7%, Perplexity-User 12.3% |
| OpenAI | 606.5 : 1 | −60.5% | GPTBot 67.7%, OAI-SearchBot 24.8%, ChatGPT-User 7.6% |
| Anthropic | 486.6 : 1 | +3.9% | ClaudeBot 85.3%, Claude-SearchBot 14.4%, Claude-User 0.3% |
| Baidu | 59.7 : 1 | +18.1% | Baiduspider 100% |
| Microsoft | 39.9 : 1 | −1.5% | Bingbot 100% |
| ByteDance | 12.3 : 1 | +48.9% | Bytespider 100% |
| Yandex | 5.8 : 1 | −69.9% | YandexBot 99.9%, YandexImages 0.1%, Other <0.1% |
| DuckDuckGo | 4.7 : 1 | +2.4% | DuckAssistBot 79.1%, DuckDuckBot 20.9% |
| Google | 4.4 : 1 | −10.7% | Googlebot 89.8%, GoogleOther 9.8%, Other 0.5% |
| Mistral | No referrals | | MistralAI-User 100% |

Crawl-to-referral ratio, on Cloudflare Radar. The slide gives no period for the change column.

*Still vs. transcript:* every value but Perplexity's, and the ratios for traditional search engines, which are far lower than for AI companies. The talk does not say so.

### 4 · Under the hood: x402

![[assets/2026-10-25-tremante-cloudflare-connect-open-agentic-internet/18-20m36-under-the-hood-x402.webp|Under the hood: x402]]

*Still at [20:36](https://www.youtube.com/watch?v=_LYr4dSmdsk&t=1236s) from Cloudflare Developers, "Building an open agentic Internet".*

Sequence among Client, Server, Facilitator and Blockchain:

1. Client → Server: `GET /api`. Server → Client: `402 PAYMENT-REQUIRED`.
2. The client creates a payment payload. Client → Server: `GET /api` with `PAYMENT-SIGNATURE`.
3. Server → Facilitator: `POST /verify`. Facilitator → Server: `200 Verification`.
4. The server does the work.
5. Server → Facilitator: `POST /settle`. Facilitator → Blockchain: `Submit tx`; `tx confirmed`. Facilitator → Server: `200 Settled, tx_hash`.
6. Server → Client: `200 Ok`, `PAYMENT-RESPONSE`, content.

*Note on the slide:* facilitators are optional; all logical steps could be performed by the server when accepting stablecoins or crypto.

*Still vs. transcript:* the whole sequence, and that settlement follows the work. The talk skips it: *"I'm not going to go into the details of this right now."*

## How it connects

- [[concepts/agentic-web|agentic-web]] — bot share, crawl-to-referral by company, a publisher table, and two payment models of different maturity.
- [[concepts/answer-engine-optimization|answer-engine-optimization]] — agent optimisation as the new SEO, and markdown alternatives kept for agents.

## Related in this wiki

- [[2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet|Cloudflare's one-year report]] and [[2026-06-09-cloudflare-investor-day-2026|Cloudflare Investor Day 2026]] — earlier accounts from the same firm, for publishers and for investors.
- [[2026-10-17-roth-verge-websites-closing-doors-to-ai-agents|Roth (The Verge)]] — a newsroom's report of sites blocking consumer agents, with Cloudflare among the means.
- [[2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet|Klein (Browserbase)]] — agents should use the web as it is, through browsers.
- [[2026-10-28-hack-klein-browserbase-navigators-clickup-why-agents-keep-failing|Hack (ClickUp)]] — an agent given a browser and credentials, and identity on the web as a policy problem.
- [[2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet|Collison (Stripe)]] — agent purchases and bot detection, from a payments company.

## What was actually ingested

The full talk and Q&A (33:33, `length_seconds: 2013`) from the transcript panel, auto-generated captions, 255 lines. ASR corrected in quotes and prose: *"X42 Foundation"* is x402, *"net dollar"* is Cloudflare's stablecoin NET Dollar; the spoken *"new CEO of the agents"* reads as *"new SEO."* He says he used to work at *"Necra"* on an internet survey, probably Netcraft, which the talk does not confirm. A model he calls *"Cleric"* could not be verified from the talk and is left out. A full static Gemini scan (189,599 tokens, 19 stills) was blocked once by a recitation error and worked on retry.

**Gemini's readings were unreliable on these slides, and the tables above come from the images.** It invented a training/search split for the crawl-ratio panel (the bars are per bot), read *"Nieman Lab"* as *"Newman Lab"*, got many figures in the traffic table wrong and redrew the x402 diagram with a Cloudflare proxy in place of the Server and Facilitator.

## Linked entities and concepts

- [[Cloudflare]] — employer and publisher. Updated in this ingest.
- [[OpenAI]], [[Anthropic]], [[Google]], [[Microsoft]] — in the crawl-to-referral table. [[OpenAI]] is also the partner in the domain-signal trial.
- [[concepts/agentic-web|agentic-web]], [[concepts/answer-engine-optimization|answer-engine-optimization]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the three cells tagged above.

**Dangling** (single-source mention, deferred): Michael Tremante, Nieman Lab, Coinbase, People Inc., Perplexity.

## Scope and reliability

A Cloudflare executive presents Cloudflare's data and products at Cloudflare's conference; Cloudflare sells the blocking, the crawl endpoint and the gateway, and calls itself impartial. Radar's view is limited to traffic crossing its network. The publisher table is from a third party, covers technology titles, and shows a fall, not its cause. The claim that most large publishers have deals is unsourced. Pay Per Use and the open index are in development, so their descriptions are plans.
