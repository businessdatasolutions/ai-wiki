---
type: source
kind: article
title: "Websites are closing their doors to AI agents"
author: ["Emma Roth"]
publisher: "The Verge"
url: "https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web"
date_published: 2026-10-17
date_ingested: 2026-10-18
length: "~900 words (web extract, read in full; 11 paragraphs against a CMS word count of 916)"
raw: "../../raw/articles/2026-10-17-roth-verge-websites-closing-doors-to-ai-agents.md"
tags: [the-verge, emma-roth, agentic-web, browser-agents, consumer-agents, meta-muse, openai-dots, instinct, xai-grok, site-blocking, agent-access, amazon-v-perplexity, agentic-shopping, yelp-data-licensing, delta, jpmorgan-chase, charles-schwab, anti-bot-systems, captcha, cloudflare, shopify, retail-partnerships, equistamp, chris-canal, agent-usefulness]
dynamic_capabilities:
  - contextual/external-triggers
  - strategic-renewal/business-model
  - digital-transforming/navigating-innovation-ecosystems
relationships:
  - type: supports
    target: 2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet
    via: "both concern whether sites let agents in: Klein's 'the models are ready, but the web isn't' and his principle that an agent may do what its human may, against the sites and anti-bot systems that are now turning agents away"
    confidence: 0.7
  - type: supports
    target: 2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet
    via: "both concern bot detection once much of the traffic is agents acting for customers: Collison's question of how to tell good bots from bad, and the reports of agents tripping safeguards built for scammers"
    confidence: 0.7
  - type: supports
    target: 2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet
    via: "both concern sites taking control over which AI systems may access them and on what terms, including paid access; the article reports Cloudflare's crawler blocking as one of the tools"
    confidence: 0.65
  - type: supports
    target: 2026-10-13-romeo-bloomberg-new-economy-wrong-ai-race
    via: "both concern the shift from human attention to machine permission: Romeo's 'power follows permission', and sites deciding whether to grant agents access at all"
    confidence: 0.6
---

# Roth (The Verge) — websites are closing their doors to AI agents

> *OpenAI, Meta, and Google want AI agents to do everything for you. But popular services on the web aren't letting that happen.* (The article's dek.)

## TL;DR

A news report of about 900 words by **Emma Roth** in *The Verge*, 17 October 2026. Consumer agents that act on the web for their users (Meta's **Muse**, xAI's **Grok**, [[OpenAI]]'s **Dots** and the startup **Instinct**) are, by users' reports, being blocked on major sites. The article sorts the refusals into three kinds and gives the two positions in the dispute:

1. **Deliberate blocks, for money or security.** Yelp told TechCrunch it admits only agents that pay for its data-licensing programme; Delta is keeping agents from booking tickets; JPMorgan Chase and Charles Schwab confirmed they block agents from customer accounts for security reasons. Users report that Cars.com and Amtrak, which used to work, no longer do.
2. **Litigation.** [[Amazon]] banned Perplexity's shopping agent and sued in 2025; a ban ordered by a court was overturned on appeal in August 2026, and Amazon has filed an amended complaint. Amazon now says Muse's *"continued access"* violates its site policies.
3. **Collateral blocks.** Anti-bot systems built against scammers catch agents too: *"These AI agents trigger those same safeguards."*

The two positions: Amazon says agents that buy for customers *"should operate openly and respect service provider decisions whether or not to participate"*; Perplexity says Amazon *"does not believe in your right to hire labor, to have an assistant or an employee acting on your behalf,"* and that the real motive is keeping human eyes on Amazon's ads. Meta's line is *"Turning away a personal agent means turning away the customer behind it,"* and it partners with retailers instead.

## Key claims

### Who is blocking, and why

The article's named cases, with the reason each gives:

| Site | What it does | Reason given | Basis |
| --- | --- | --- | --- |
| Yelp | admits only agents in its paid data-licensing programme | licensing | Yelp to TechCrunch |
| Delta Air Lines | prevents agents booking tickets for users | not stated | stated in the article |
| JPMorgan Chase, Charles Schwab | block agents from accessing accounts | security | confirmed by the firms |
| Cars.com, Amtrak | no longer reachable by agents that used to work | none given; *"suggesting other companies could be quietly blocking them"* | user reports |
| Amazon | banned Perplexity's agent and sued; says Muse violates its site policies; Grok, Instinct and Dots reportedly cannot use it | site policy; *"should operate openly"* | Amazon statements, court record |

### Amazon v. Perplexity: the dispute that set the terms

Amazon *"repeatedly requested"* that Perplexity stop its agents shopping on Amazon, then sued. Perplexity's reply framed the agent as *"an extension of the user"* and accused Amazon of protecting ad revenue, which the article calls *"an actual issue for the ecommerce giant."* A judge ordered Perplexity to stop; an appeals court overturned the order in August 2026; Amazon filed an amended complaint. The litigation *"didn't stop OpenAI, Meta, and Google from rolling out agents of their own,"* and they now meet the same refusals. Elon Musk's response to Amazon blocking Grok was that maybe he *"should start a competitor to Amazon."*

### Partner instead of fight

Meta answered the blocking of Muse in a post: *"We'd rather work with businesses to address the underlying concerns than see them lose that customer."* Rather than fight Amazon, it partnered with Walmart, Gap, Sephora, Best Buy and others so that Muse can shop on their sites. Shopify has opened its network of storefronts to agents. OpenAI and Google did not reply in time; Instinct declined to comment.

### Agents caught by defences built for bots

Even without a ban, agents run into anti-bot systems *"which have become ubiquitous across the web."* Reddit users report Google blocking some accounts that use Muse for *"suspicious activity,"* and checkout failures on Walmart despite its partnership with Meta. Chris Canal, CEO of the AI safety evaluator EquiStamp: *"There are all kinds of things that are set up not even to block agents, but to block in general bots or programs that are trying to scam or hack… These AI agents trigger those same safeguards."* [[Cloudflare]], after its one-click block for AI crawlers in 2025, now also blocks crawlers that scrape for both search indexing and AI training.

### What it costs

For the agent makers, usefulness: *"Does this impact the perceived value of the Anthropics and the OpenAIs? I would say absolutely… If there are companies that are actively working to make that not happen, there are just fewer useful things the agents can do"* (Canal). For everyone else, friction: as more sites add checks that a visitor is human, the web gets more *"annoying,"* possibly *"on a simple grocery shopping website soon, where you're having to jump through a bunch of hoops to prove that you're a human."*

## Dynamic-capabilities reading

- **`contextual/external-triggers`** — customers' agents arriving at a firm's site are an outside force the firm has to answer, whether by blocking, charging or partnering; for agent makers, the refusals are an outside limit on what their product can do.
- **`strategic-renewal/business-model`** — the refusals are business-model decisions: Yelp turns agent access into a paid licence, and Perplexity's case against Amazon is that agents threaten an ad-funded model built on human attention.
- **`digital-transforming/navigating-innovation-ecosystems`** — Meta's retailer partnerships and Shopify's opening of its storefronts are deals about which ecosystem an agent may operate in, made instead of litigating.

## How it connects

- [[concepts/agentic-web|agentic-web]] — the access side of the page's story, and the page's first source that is not a vendor. It bears on three of the page's open debates: who captures the customer relationship (sites refusing to cede it), whether agents should be taught the existing web (the existing web is refusing them), and bot detection once most traffic is bots.
- [[concepts/ai-agents|ai-agents]] — consumer agents from the largest labs, in use at scale, limited less by capability than by access.
- [[2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet|Klein (Browserbase)]] states the principle *"if a human is allowed to do a task so should their agent"*; Perplexity's argument against Amazon is the same principle in a courtroom.
- [[2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet|Collison (Stripe)]] asks what replaces bot detection now that *"it's increasingly all bots"*; this article reports agents caught by the old kind.
- [[2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet|Cloudflare's Content Independence Day report]] — the crawler-blocking and licensing market the article mentions, from the vendor running it.
- [[2026-10-13-romeo-bloomberg-new-economy-wrong-ai-race|Romeo (Oliver Wyman Forum)]] — *"power follows permission"*; here are the sites deciding whether to grant it.

## What was actually ingested

The full article: 11 paragraphs, about 900 words, extracted from the page's own content blocks with links kept. The Verge marks the post as paywall-eligible, but the complete text is served in the page and matches its JSON-LD body and CMS word count. Left out: a pull quote that repeats a sentence, and two related Verge posts listed at the end of the raw file (on Muse's data consent, and on Instinct), which were not captured.

## Linked entities and concepts

- [[Amazon]] — the Perplexity litigation and the block on Muse. Updated in this ingest.
- [[Cloudflare]] — crawler blocking, reported as one of the tools sites use. Updated in this ingest.
- [[OpenAI]] — its agent Dots, reportedly unable to use Amazon. Updated in this ingest.
- [[concepts/agentic-web|agentic-web]], [[concepts/ai-agents|ai-agents]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the three cells tagged above.

**Dangling** (single-source mention, deferred): Emma Roth; The Verge; Meta and its agent Muse; Instinct; xAI; Perplexity (also dangling on the Ramineni page, but never an `author:`); Yelp; JPMorgan Chase; Charles Schwab; Delta Air Lines; Shopify; Chris Canal; EquiStamp.

## Scope and reliability

A news report, not a measurement: no source in it counts how many sites block agents or how often agents fail. The evidence is of three grades. Confirmed by the companies: Yelp (to TechCrunch), JPMorgan Chase and Schwab, Amazon's statements, and Meta's post. From the court record: the Perplexity case. From user reports, mostly Reddit: Cars.com, Amtrak, Google's account blocks and Walmart's checkout failures. The one analyst quoted, Canal, runs an AI safety evaluator. The article is independent of the vendors whose numbers fill the rest of the [[concepts/agentic-web|agentic-web]] page, which is its main value here. The agents it names (Muse, Dots, Instinct) appear nowhere else in the wiki.
