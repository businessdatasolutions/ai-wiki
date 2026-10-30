---
type: concept
title: Agentic web
aliases: ["agentic web", "agentic Internet", "agentic internet", "zero-click", "zero-click search", "Google Zero", "AI crawlers", "AI crawler traffic", "content licensing for AI", "pay-per-crawl", "agentic commerce", "machine payments", "x402", "agent identity", "Web Bot Auth"]
tags: [agentic-web, aeo, answer-engines, agentic-internet, zero-click, google-zero, referral-traffic, ai-crawlers, training-crawlers, bot-traffic, content-licensing, pay-per-crawl, x402, web-bot-auth, agentic-commerce, open-web, publishers, search-to-answers, browser-agents, computer-use, agent-authentication]
confidence: 0.75
last_confirmed: "2026-10-30"
accessed_at: "2026-10-30"
source_count: 13
relationships:
  - type: depends-on
    target: ai-agents
    via: "the agentic web is what the open web becomes once agents, not people, do most of the fetching, reading and buying; ai-agents holds what agents are, this page holds what they do to the economics of the web"
  - type: supports
    target: enterprise-ai-adoption
    via: "a case of adoption forced from outside: a firm's customers adopt AI assistants first, and the firm's discovery, marketing and revenue model have to follow whether or not it planned to adopt anything"
  - type: uses
    target: answer-engine-optimization
    via: "AEO is how brands respond inside the agentic web: optimising to be cited in AI answers once search referral no longer delivers visitors"
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

### 6. The brand side: optimising to be cited (added 2026-09-30)

Sections 1–5 describe what the shift costs the sites that used to receive the traffic. The practice growing up on the other side, **answer engine optimization (AEO)**, getting a brand named and cited inside AI answers, has its own page: [[answer-engine-optimization]]. Its main source is [[2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook|Amiel & Sanders (HubSpot UNBOUND, Sep 2026)]]. Two points connect back to this page:

- **Consensus replaces referral.** Answer engines recommend what many sources agree on, so most of what they read about a brand is written by others: PR, reviews, social. The brand's own site is kept as the source of truth rather than as the destination for traffic.
- **The mirror of section 3.** Publishers block AI crawlers to gain licensing leverage; brands unblock them to be cited. Which side a firm is on depends on whether the content is its product or its advertising.

### 7. The payments side: AI discovery as the new aggregator (added 2026-10-11)

[[2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet|John Collison (Stripe, Oct 2026)]] describes the shift from the side that settles the transactions. First order, *"people's agents are going to be doing a huge amount of the commerce for them"*; second order, *"AI discovery is the new point of aggregation for commerce"*, which he expects to favour well-reviewed long-tail sellers and to turn over the top merchants, as Facebook and Instagram ad targeting once produced a native generation of sellers. Two further points connect to sections 2 and 4:

- **Bot detection when it is all bots.** *"Many sites do bot detection and bot prevention … but like it's increasingly all bots. And so, what is the new equivalent of … bot detection?"*, separating good bots from bad. Cloudflare's Web Bot Auth (section 4) is one answer.
- **Computer use instead of integrations.** Agents need no API from the site: computer use is *"the ultimate backwards compatibility layer"*. Stripe itself reports that *"no one actually really integrates the Stripe API by hand anymore … they send their coding agent to do it"*, so it is redesigning for AI rather than developer ergonomics.

Stripe and the conference host (Browserbase, which sells computer-use infrastructure) both benefit from this thesis; the talk gives no adoption figures.

### 8. The agent-infrastructure side: teach agents the existing web (added 2026-10-12)

[[2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet|Paul Klein IV (Browserbase, Navigate 2026 keynote)]] describes the shift from the side that sells agents their browsers. His thesis is that *"the models are ready, but the web isn't"*. He does not expect the web to be rebuilt for agents: *"Waymo didn't have to rebuild the roads for AI. They just taught it how to drive like a human."* Browserbase says its platform has run 500 million sessions but reached only *"7% of the active web"*. It sells browsers, search and fetch APIs, an open-source automation framework (Stagehand) and a routing and caching model gateway. Two points connect to sections 2 and 4:

- **Web Bot Auth from the issuer's side.** Section 4 describes [[Cloudflare]] verifying signed agents. Klein describes Browserbase signing them: *"an identification card for your agent"* that Browserbase issues. He names Cloudflare, Vercel and reCAPTCHA as accepting that verified traffic. This answers the bot-detection question in section 7 with a product.
- **Logins are the next gate.** *"Most systems on the internet actually live behind authentication."* Browserbase partners with Okta, 1Password and Clerk, and its Agentic Identity Suite (early access) manages an agent's secrets, inbox, cookies and sessions. Its stated principle is *"if a human is allowed to do a task so should their agent."*

Klein also gives the case against a protocol-only web: agents that can reach only API and MCP endpoints would make *"a walled garden of … gatekeepers and tollkeepers"*, leaving out *"the DMV, my local barbershop."* A browser vendor gains from this argument, and an identity issuer that sites are asked to trust is itself a gatekeeper of a kind.

### 9. Three eras at once, and from attention to permission (added 2026-10-15)

[[2026-10-14-longo-marchiaro-hubspot-unbound-ai-transforming-search|Paul Longo (Microsoft Advertising, HubSpot UNBOUND, Oct 2026)]] gives the advertiser's map of the shift as **three eras of the web**: the **human web** (*"help me find it"*: search), the **LLM web** (*"help me choose"*: an assistant compares and recommends) and the **agentic web** (*"do it for me"*: an agent books and pays). His point is that they run in parallel: *"We're not moving from one to the other. All three are happening at the same time."* Search is not shrinking in his account; Bing has passed one billion monthly users and *"the majority of clicks are still coming through the human web."* His slide draws the line between the second and third eras on one task: in the LLM web the assistant recommends a cabin and then tells the person which address to email to book it; in the agentic web it books flights, cabin and restaurant and pays.

Two numbers come with it. A Microsoft survey of 1,000 US adults finds 60% *"ready for AI agents to replace traditional websites,"* with consumers split 30 / 40 / 30 between those who want guidance and guardrails, the screen-first middle, and those with high expectations. And Human Security's 2026 benchmarks put AI traffic growing **8× faster than human traffic**, with agentic browser traffic up almost 8,000 year on year. Both are vendor figures without published method; they are a third measurer alongside Cloudflare (section 2).

[[2026-10-13-romeo-bloomberg-new-economy-wrong-ai-race|John Romeo (Oliver Wyman Forum, Oct 2026)]] puts what this does to marketing in one line: *"Give an agent your data, a budget, a mandate, and permission to act, and you've created an economic actor. When the travel agent that chooses an airline is no longer a human, then the battle that we fought for human attention shifts to a battle for machine permission, and power follows permission."* His remedy is on the governance side, Berners-Lee's *"license plates"* for agents (identity, permission, accountability, revocability); it sits next to the agent identity cards of section 8 and is covered under [[agent-oversight-and-delegation]].

### 10. Sites refuse: blocks, lawsuits and collateral checks (added 2026-10-18)

Sections 7–9 describe the agentic web from the sides that want agents to get in. [[2026-10-17-roth-verge-websites-closing-doors-to-ai-agents|Roth (The Verge, Oct 2026)]] reports what happened when consumer agents from the largest labs (Meta's Muse, OpenAI's Dots, xAI's Grok, Instinct) arrived at scale: many sites turned them away. It is the page's first source that is not a vendor. The refusals come in three kinds:

- **Deliberate, with a reason.** Yelp admits only agents that pay for its data-licensing programme, the licensing market of section 3 applied to agents rather than crawlers. JPMorgan Chase and Charles Schwab block agents from accounts for security. Delta keeps them from booking. Users report Cars.com and Amtrak closing without explanation.
- **Contested in court.** [[Amazon]] banned Perplexity's shopping agent and sued; a court-ordered ban was overturned on appeal in August 2026, and Amazon has filed an amended complaint. Amazon's position is that agents *"should operate openly and respect service provider decisions whether or not to participate."* Perplexity's is that Amazon *"does not believe in your right to hire labor, to have an assistant or an employee acting on your behalf,"* and protects ad revenue that depends on human eyes. Perplexity's argument is Klein's principle from section 8, *"if a human is allowed to do a task so should their agent,"* made in court.
- **Collateral.** Anti-bot systems catch agents that no one meant to block: *"These AI agents trigger those same safeguards"* (Chris Canal, EquiStamp). This is the answer, for now, to Collison's question in section 7: the old bot detection still runs, and agents fail it.

The response from the agent side is to partner rather than fight. Meta, *"Turning away a personal agent means turning away the customer behind it,"* signed Walmart, Gap, Sephora and Best Buy; Shopify opened its storefronts to agents. Canal names the cost on both sides: fewer useful things agents can do, which bears on *"the perceived value of the Anthropics and the OpenAIs,"* and a more *"annoying"* web for people, with human-verification checks spreading even to grocery sites.

## Debates and supersession

- **How much of the evidence is independent?** Three of the original five sources are vendors with a stake. Cloudflare sells the blocking, analytics and payment products, and HubSpot sells the marketing software for the new playbook. Cloudflare's network data is real measurement from an unusually large vantage point, but it is neither audited nor reproducible outside the company, and "traffic" is not defined. The two predictions (Ognibeni, DFI) are independent but are predictions. Four of the six sources are vendors once HubSpot's AEO session is counted. **Confidence is held at 0.75**, the ceiling the schema sets for vendor sources without independent replication. A third-party measurement of referral traffic, such as the Pew click-through study the Cloudflare deck cites as its anchor, is the ingest target that would move it. The October 2026 additions do not change this: Microsoft Advertising's survey and Human Security's traffic benchmarks (section 9) are also vendor figures without published method, and Human Security sells bot detection. [[2026-10-17-roth-verge-websites-closing-doors-to-ai-agents|The Verge (Oct 2026)]] is the first independent source, but it reports access refusals from company statements and user reports and measures no traffic, so it does not touch the referral claims that carry the cap.
- **Is the traffic loss caused by AI answers, or does it coincide with them?** Cloudflare attributes category-level declines to AI consumption. Its data shows human traffic falling and crawler traffic rising together, which is consistent with substitution but also with other causes: seasonality, bot-classification changes, and shifts in how Cloudflare's customer base is composed. HubSpot's own account is causal but single-firm. **Open.**
- **Does licensing replace referral revenue?** Cloudflare says no, not yet. No source in the corpus sizes the licensing market against the referral economy it is meant to replace. **Open.**
- **Is AEO measurement, or a vendor's model of the engines?** The AEO claims (mentions across the web as the main factor, the citation shares by source type) come from HubSpot/XFunnel's own analysis without method, and the outcome figures (+170% MQLs, +82% closed deals for adopters) do not separate what AEO did from which customers chose to adopt it. The persona × stage prompt matrix is a method; the ranking factors are a vendor's claim. **Open** until an independent study of what AI answers cite is ingested.
- **Who captures the relationship?** Ognibeni and DFI frame the agent as a disintermediator that takes over the customer relationship. Cloudflare frames itself as a neutral market maker that keeps publishers paid. These are different predictions about where value settles: with the agent operator, the infrastructure layer, or the content owner. The corpus cannot yet distinguish them. [[2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet|Collison]] (Oct 2026) adds a fourth: AI discovery becomes the new aggregator but widens reach for the long tail of sellers under it. [[2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet|Klein (Browserbase, Sep 2026)]] adds a fifth candidate: the issuer of agent identity, which vouches for agents to sites and negotiates their access. [[2026-10-17-roth-verge-websites-closing-doors-to-ai-agents|The Verge (Oct 2026)]] shows the largest merchant refusing to cede it at all: Amazon blocks outside agents and litigates, while Meta settles access retailer by retailer.
- **Rebuild the web, or teach agents the old one?** Cloudflare's sources describe new rails on the site side (pay-per-crawl, x402). [[2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet|Klein]] argues agents should use the web as it is, through browsers, without waiting for APIs or MCP servers. [[2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet|Collison]] makes the same DMV argument at the same conference. Web Bot Auth sits between the two: pages stay as they are, but the site or its CDN must verify signatures. Both positions come from vendors whose products depend on the answer. Section 10 adds what neither vendor controls: sites deciding whether to let agents in at all, by policy, by lawsuit, or by bot defences that catch them by accident. **Open.**
- **Rails or browsers, restated (added 2026-10-30).** [[2026-10-25-tremante-cloudflare-connect-open-agentic-internet|Tremante (Cloudflare Connect, Oct 2026)]] and [[2026-10-28-hack-klein-browserbase-navigators-clickup-why-agents-keep-failing|Hack (ClickUp, on Navigators, Oct 2026)]] give the two positions in the same month: a crawl endpoint, index and payment on the site side, or a browser and credentials on the agent side. Each speaker's firm sells its route.

## Related concepts

- [[ai-agents]] — what agents are; this page holds what they do to the web's economics. Its *agentic commerce at consumer scale* section (Ognibeni) is the consumer-side counterpart.
- [[enterprise-ai-adoption]] — HubSpot's case of adoption forced by customers' behaviour.
- [[responsible-ai]] — the shrinking data commons, of which default crawler blocking is one mechanism.
- [[answer-engine-optimization]] — the brand-side practice: being cited in AI answers rather than ranked in search results.
- [[generative-ai]] — the *sea of sameness*: why generic content loses value when generation is free.
- [[open-source-ai]] — the other place the corpus tracks who pays whom for model inputs and outputs.

## Sources consulted

- [[2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet]] — non-human traffic above 50%, crawler purpose, Google's mixed-use crawler, the licensing market and its limits.
- [[2026-06-09-cloudflare-investor-day-2026]] — adoption speed, attention share, industry human-traffic declines, x402 and Web Bot Auth, agent requests +1,700%.
- [[2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook]] — answer engine optimisation: prompt matrices, visibility and share of voice, consensus across the web, and the Fresha case.
- [[2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook]] — one firm's traffic −80% with leads +20%, and the playbook that followed.
- [[2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china]] — the prediction that agents kill search-driven e-commerce first.
- [[2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet]] — agentic commerce from the payments side: AI discovery as aggregator, bot detection, computer use.
- [[2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet]] — the agent-infrastructure side: browsers for the existing web, Web Bot Auth from the issuer's side, agent logins and the walled-garden argument.
- [[2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells]] — the incumbent retailer's fear of agentic disintermediation.
- [[2026-10-14-longo-marchiaro-hubspot-unbound-ai-transforming-search]] — the three eras of the web (human, LLM, agentic) running at once; consumer-readiness survey; Human Security's agent-traffic figures.
- [[2026-10-13-romeo-bloomberg-new-economy-wrong-ai-race]] — from human attention to machine permission; license plates for agents.
- [[2026-10-17-roth-verge-websites-closing-doors-to-ai-agents]] — the access side, from a newsroom: sites blocking consumer agents for licensing and security, Amazon v. Perplexity, anti-bot systems catching agents, and Meta's retailer partnerships.
- [[2026-10-25-tremante-cloudflare-connect-open-agentic-internet]] — bot share, crawl-to-referral by company, a publisher traffic table, x402 sequence, Monetization Gateway and Pay Per Use.
- [[2026-10-28-hack-klein-browserbase-navigators-clickup-why-agents-keep-failing]] — a browser and credentials as the integration of last resort.

## Bot share, crawl ratios, and two ways of being paid (added 2026-10-30)

[[2026-10-25-tremante-cloudflare-connect-open-agentic-internet|Tremante (Cloudflare Connect, Oct 2026)]] gives 66.0% of HTML page requests as bots on Cloudflare Radar, and crawl-to-referral ratios by company (Perplexity 3.4K : 1, OpenAI 606.5 : 1, Anthropic 486.6 : 1, Google 4.4 : 1; tables on the source page). A Nieman Lab table on his slide shows ten technology publications down 30–97% from peak by January 2026.

He separates two payment models. The **Monetization Gateway** charges at access through HTTP 402 and x402, with cryptographic proof, and is in private beta. **Pay Per Use** pays on each reuse of crawled content, depends on trust and a bidding system, and is still in development, because a provider *"only needs to crawl you once."* Before payment come a `/crawl` endpoint for signed bots, an opt-in open index, and new-domain signals, which he says surfaced several million domains for OpenAI. He also names the leak: agents that subscribe, crawl and resell.

[[2026-10-28-hack-klein-browserbase-navigators-clickup-why-agents-keep-failing|Hack (ClickUp, on Navigators, Oct 2026)]] is the other route: *"give the agent a browser, give it your credentials,"* for systems with no integration. Klein, the host, calls agent identity on the web a matter of people and policy.
