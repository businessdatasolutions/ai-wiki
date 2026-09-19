---
type: concept
title: Agentic web
aliases: ["agentic web", "agentic Internet", "agentic internet", "zero-click", "zero-click search", "Google Zero", "AI crawlers", "AI crawler traffic", "content licensing for AI", "pay-per-crawl", "agentic commerce", "machine payments", "x402"]
tags: [agentic-web, agentic-internet, zero-click, google-zero, referral-traffic, ai-crawlers, training-crawlers, bot-traffic, content-licensing, pay-per-crawl, x402, web-bot-auth, agentic-commerce, open-web, publishers, search-to-answers]
confidence: 0.75
last_confirmed: "2026-09-19"
accessed_at: "2026-09-19"
source_count: 5
relationships:
  - type: depends-on
    target: ai-agents
    via: "the agentic web is what the open web becomes once agents, not people, do most of the fetching, reading and buying; ai-agents holds what agents are, this page holds what they do to the economics of the web"
  - type: supports
    target: enterprise-ai-adoption
    via: "a case of adoption forced from outside: a firm's customers adopt AI assistants first, and the firm's discovery, marketing and revenue model have to follow whether or not it planned to adopt anything"
  - type: supports
    target: responsible-ai
    via: "the data-commons question in market form. Default blocking of AI training crawlers shrinks what models can learn from, and licensing decides who is paid for what they do learn from"
quality_score: 0.99
quality_notes: ['1 near-empty section(s)']
---

# Agentic web

## Working definition

The open web as it is being reshaped by the fact that **software agents, not people, increasingly do the fetching, reading and choosing.** Search engines used to send visitors; AI systems now answer in place. The corpus holds three linked observations, and the page is organised around them:

1. **The referral bargain has broken.** The web's old exchange was content for search visibility, visibility for referral traffic, and traffic for revenue. Content is still crawled and used, but visitors no longer arrive in proportion.
2. **Non-human traffic now dominates, and its purpose has shifted toward training.** Crawling used to be mostly for search indexing. It is now mostly for AI training or mixed use.
3. **A market is forming to price access.** Crawler blocking, attribution and licensing on the publisher side, and machine-payment rails on the agent side.

The term is Cloudflare's ("the agentic Internet"). The page uses "agentic web" for the phenomenon, independent of any vendor's product framing. It opened on 2026-09-19 with five sources: two network-layer reports from [[Cloudflare]], one firm's own numbers, and two earlier predictions of the same shift.

## Key claims

### 1. Discovery has moved from search to answers, and the traffic did not follow

The first measurement comes from a single firm. [[2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook|HubSpot]] lost **80% of its web traffic, 140 million visits in a year**, from May 2024, as buyers *"are having those conversations with ChatGPT, with Claude"* instead of reading its blog. Leads still grew 20%, because what disappeared was low-intent traffic.

The second is at the level of a network carrying more than 20% of the web. [[2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet|Cloudflare's one-year report]] and [[2026-06-09-cloudflare-investor-day-2026|its Investor Day deck]] find:

- **human (non-bot) traffic down 35–40%** between June 2025 and April 2026 in retail, computer software, IT & services and financial services;
- ten named tech publications down **30% to 97%** in Google traffic from peak (Growtika, from Ahrefs estimates);
- the open web's share of online attention put at about **25% in the AI era**, down from 55% in 2015–22. The deck itself marks this figure *illustrative*, not a measured series.

The consequence the sources draw is the same. Publishers are planning for **"Google Zero"**, a world with little or no search referral, and HubSpot's CMO describes the change as moving *"from … volume of visits … to … value of visits."*

Both outcomes had been predicted in the corpus. [[2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china|Ognibeni]] warned in May 2026 that search-driven e-commerce would be the first format agents take over (*"Nobody will show up in your store"*). The same month [[2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells|DFI's CEO]] described the retailer's version: an agent between the store and its shopper, owning the relationship.

### 2. Most traffic is now non-human, and crawling is for training

Cloudflare reports that **more than 50% of Internet traffic is non-human**, a threshold crossed in 2026. Daily AI agent requests on its network rose **1,700%+** between June 2025 and May 2026. By purpose:

- **52% of crawler requests are for AI training** (June 2026), up from 22% in spring 2025;
- **mixed-use crawlers** that combine search, agent and training access make up more than 36%;
- pure search crawling is *"a small and declining share."*

Mixed-use crawlers are the structural problem, and Google is the largest one. Google carries about **88% of referral traffic** but uses a single crawler for search and AI, so *"it [is] difficult for customers to participate in Google's search ecosystem without also participating in Google's AI ecosystem."* Cloudflare puts Google's resulting information advantage at about 2× that of other leading AI companies. Most other AI firms separate discovery from training crawlers, which lets a publisher stay findable without handing over content for training.

### 3. Scarcity created a licensing market, which does not yet replace what was lost

In July 2025 Cloudflare began **blocking AI training crawlers by default** on new domains ("Content Independence Day"). Its account of the year that followed: *"Transparency created scarcity. Scarcity created leverage. Leverage accelerated licensing."* Publishers gained operator-level data on which models crawled what and at what **crawl-to-referral ratio**, and used it in negotiations. People Inc. reported deal progress *"much further along"* after blocking. More than **50 publisher–AI agreements** have been signed since 2023, and collective licensing is emerging.

The same report is candid about the limit. Licensing is *"largely bespoke and unlikely to fully replace lost referral, advertising, and affiliate revenue,"* and *"content valuation is still unresolved."* Its proposed next steps are declared crawl intent, freshness signals, and *"discovery before pricing"*. These are the preconditions for a market, not evidence that one works.

This is the market-side face of a trend [[responsible-ai]] already records from the data side. The [[2026-04-28-ai-index-report-2025|AI Index 2025]] found AI-training restrictions on actively maintained domains in the C4 corpus rising from 5–7% to 20–33% in a year. Those figures predate Cloudflare's July 2025 default block; the block carries the same trend to network scale, where it is applied by default rather than site by site.

### 4. Machine payments: pricing each request

The agent-side counterpart is paying for access in the request itself. Cloudflare's **x402** (a foundation co-founded with Coinbase and Stripe) revives HTTP status 402 *Payment Required*: the server returns a price, the agent signs and retries, and payment is verified at the edge before the content is served. Cloudflare reports serving **2 billion 402 responses a day**. **Web Bot Auth** cryptographically binds an agent's identity to a transaction so that merchants can verify who is buying. The strategic framing is explicit: *"from protecting websites from bots to monetizing trusted automated demand,"* with *"every agent request [as] a metered event."*

These are infrastructure claims from the vendor building the infrastructure. The corpus holds no independent measure of how much money actually moves over these rails.

### 5. Adaptation on the publisher's side: value over volume, and content that cannot be generated

What a content-producing firm does about it is, so far, only visible in [[2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook|HubSpot's]] account. It concentrated on conversion rather than visits, on content with *"unique data, unique customer stories, unique examples"* that a general model cannot produce, and on distribution through the channels where buyers now are (AI search, creators, paid platforms). The Cloudflare report points the same way from the market side: AI companies increasingly license *"differentiated and premium content."* The common thread is that **generic content has lost its traffic value, and only differentiated content has a price.** See [[generative-ai]] for the *sea of sameness* argument behind this.

## Debates and supersession

- **How much of the evidence is independent?** Three of the five sources are vendors with a stake. Cloudflare sells the blocking, analytics and payment products, and HubSpot sells the marketing software for the new playbook. Cloudflare's network data is real measurement from an unusually large vantage point, but it is neither audited nor reproducible outside the company, and "traffic" is not defined. The two predictions (Ognibeni, DFI) are independent but are predictions. **Confidence is held at 0.75**, the ceiling the schema sets for vendor sources without independent replication. A third-party measurement of referral traffic, such as the Pew click-through study the Cloudflare deck cites as its anchor, is the ingest target that would move it.
- **Is the traffic loss caused by AI answers, or does it coincide with them?** Cloudflare attributes category-level declines to AI consumption. Its data shows human traffic falling and crawler traffic rising together, which is consistent with substitution but also with other causes: seasonality, bot-classification changes, and shifts in how Cloudflare's customer base is composed. HubSpot's own account is causal but single-firm. **Open.**
- **Does licensing replace referral revenue?** Cloudflare says no, not yet. No source in the corpus sizes the licensing market against the referral economy it is meant to replace. **Open.**
- **Who captures the relationship?** Ognibeni and DFI frame the agent as a disintermediator that takes over the customer relationship. Cloudflare frames itself as a neutral market maker that keeps publishers paid. These are different predictions about where value settles: with the agent operator, the infrastructure layer, or the content owner. The corpus cannot yet distinguish them.

## Related concepts

- [[ai-agents]] — what agents are; this page holds what they do to the web's economics. Its *agentic commerce at consumer scale* section (Ognibeni) is the consumer-side counterpart.
- [[enterprise-ai-adoption]] — HubSpot's case of adoption forced by customers' behaviour.
- [[responsible-ai]] — the shrinking data commons, of which default crawler blocking is one mechanism.
- [[generative-ai]] — the *sea of sameness*: why generic content loses value when generation is free.
- [[open-source-ai]] — the other place the corpus tracks who pays whom for model inputs and outputs.

## Sources consulted

- [[2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet]] — non-human traffic above 50%, crawler purpose, Google's mixed-use crawler, the licensing market and its limits.
- [[2026-06-09-cloudflare-investor-day-2026]] — adoption speed, attention share, industry human-traffic declines, x402 and Web Bot Auth, agent requests +1,700%.
- [[2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook]] — one firm's traffic −80% with leads +20%, and the playbook that followed.
- [[2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china]] — the prediction that agents kill search-driven e-commerce first.
- [[2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells]] — the incumbent retailer's fear of agentic disintermediation.
