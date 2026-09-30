---
type: concept
title: Answer engine optimization
aliases: ["answer engine optimization", "answer engine optimisation", "AEO", "generative engine optimization", "generative engine optimisation", "GEO", "AI search optimization", "LLM visibility", "AI visibility", "brand visibility in AI answers"]
tags: [aeo, geo, seo, answer-engines, ai-search, citations, brand-visibility, share-of-voice, prompt-tracking, consensus, earned-media, entity-richness, bot-accessibility, buyer-journey]
confidence: 0.75
last_confirmed: "2026-09-30"
accessed_at: "2026-09-30"
source_count: 5
relationships:
  - type: part-of
    target: agentic-web
    via: "AEO is the brand-side practice within the agentic web: once AI answers replace search results as the place buyers learn about products, being cited in the answer replaces ranking on the results page"
  - type: supports
    target: enterprise-ai-adoption
    via: "a case of adoption forced from outside: a firm's buyers adopt answer engines first, and its marketing has to build new measurement and content routines in response"
quality_score: 0.99
quality_notes: ['1 near-empty section(s)']
---

# Answer engine optimization

## Working definition

**Answer engine optimization (AEO)** is the practice of getting a brand, product or source **named and cited inside the answers AI systems give**: ChatGPT, Gemini and Google's AI Mode, Claude, Perplexity. It does for answer engines what search engine optimization (SEO) did for search results pages, and much of its craft comes from SEO. **Generative engine optimization (GEO)** names the same thing; this page treats the two terms as synonyms.

The shift underneath it is recorded in [[agentic-web]]: buyers now do their research in a conversation with an AI system rather than by clicking through results, and the referral traffic that sustained SEO has not followed. AEO is what a brand does about that on its own side.

Most of the fundamentals on this page come from one practitioner session, [[2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook|Amiel & Sanders (HubSpot UNBOUND, Sep 2026)]]. Beeri Amiel co-founded XFunnel, one of the first AEO platforms, before HubSpot bought it. The page keeps their explanation of how the channel works and leaves out the product demo and the outcome figures (see *Debates*).

## How AEO differs from SEO

| | SEO | AEO |
| --- | --- | --- |
| **Unit of demand** | Keyword, 3–5 words on average | Prompt: a full question, often 15+ words, inside a multi-turn conversation |
| **Demand data** | Search volumes (Search Console, Semrush, Ahrefs) | **None.** No provider publishes prompt volumes |
| **Result** | A ranked list of links | One synthesised answer, with citations |
| **Goal** | Rank high, win the click | Be **mentioned** in the answer, and be a **cited** source |
| **Main signal** | The page's relevance and authority | **Consensus**: how often and how consistently the brand is described across the web |
| **Where the work happens** | Mostly on the site | On the site, then social, reviews and earned media |
| **Buyer's arrival stage** | Often awareness (a blog visit) | Often decision: the engine has done the comparison |
| **Personalisation** | Low: the same results for everyone | High: the engine uses the user's history and connected tools |

Two rows carry most of the difference. Without demand data, AEO cannot start from what people search for, so it **tests the engine** instead. And because the engine synthesises across sources, it **needs agreement across sources** before it recommends a brand. A page on the brand's own site is not enough.

## Key claims

### 1. Anatomy of an answer

Amiel breaks an answer into four parts:

- **Prompt**: what the user types. It is longer and more specific than a keyword: *"what are the best CRMs for SMBs in Spain?"*, not *"best CRM"*.
- **Response**: the answer text the user reads.
- **Citations**: the sources the engine used, shown to build user trust. These are the lever: they show *which* sources the engine drew on for a given question.
- **Brand mention**: the goal. The brand named, with reasons, as a fit for the user's problem. Competitor mentions sit alongside it.

The framing Amiel builds on this: treat the answer engine as **your best sales rep**, one that already has the buyer's trust. AEO is *training* that rep, and measurement is *testing* it: does it know the product, the use cases, and whom it is for?

### 2. Measuring without demand data

Since prompt volumes do not exist, measurement is a **constructed test set**:

- **Build a prompt matrix of persona × buying-journey stage × region.** A VP of marketing and a freelancer ask different questions about the same product, care about different things (compliance and reporting against content editing), and get different answers. Journeys also differ by region.
- **Source the prompts from what the firm already knows**: sales calls, support tickets, customers talking on social media, and the longer, conversational queries now appearing in search-console data.
- **Track three numbers**: **brand visibility** (the share of tracked prompts whose answer mentions the brand), **share of voice** (the brand's mentions against competitors'), and **citations** (which sources, of which type, each answer drew on).
- **Measure per engine.** Usage differs: a Similarweb analysis the session cites puts ChatGPT and Claude at about 15–16 words per prompt and about five prompts per session, against shorter, more transactional use of Google AI Mode and Gemini. Perplexity sits between them, used more for research.

The low-tech version works too. Fresha started with ten people in a room typing the same buyer question into ChatGPT, reading the citations, and building pages and PR to match the cited sources.

### 3. Consensus across the web is the main signal

The session's central claim: *"By far the most important factor for showing up on answer engines is how often your brand is mentioned across the web. Not how many pages you have on your website."* Answer engines try to reach a consensus before recommending, so a brand's claim about itself counts only when other sources repeat it.

HubSpot's citation analysis gives the shape: the brand's **own site is about 8%** of citations, **PR and news about 30%**, **social media about 10%**. The unsourced figures are less important than their implication, which is that most of what the engine reads about a brand is written by others.

### 4. The own site as source of truth

The own site is a small share of citations but has a specific role: it is the **source of truth** the engine checks third-party claims against, and the only place the brand fully controls the narrative. It is also the material that gets repurposed for every other channel. Six content signals:

1. **Clear, direct answers.** Lead with the answer; don't bury it.
2. **Original expertise.** Case studies, testimonials, reviews and the firm's own data: things a model cannot produce from its training data. This is the same *unique data* argument that [[2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook|Bodnar & Flanagan]] make against the *sea of sameness*.
3. **Entity richness.** Content has to say what the product is, what it does and for whom. The test is to read one paragraph out of context: if it doesn't say what the product does and for whom, rewrite it. Engines retrieve chunks, not whole articles, and they are *"impatient readers"*. A 30,000-word post can fail this test.
4. **Full-funnel coverage.** Answer the specific questions of every stage, industry and use case, not only the high-volume top-of-funnel ones.
5. **Freshness.** *"You don't want to be the best answer two years ago. You want to be the best answer today."*
6. **Bot accessibility.** Crawlers must be able to read the page: not blocked in robots.txt, and not dependent on JavaScript rendering.

[[2026-06-19-chou-yc-lightcone-40-year-old-solo-founder|Bryant Chou's Ploy]], a YC-backed website platform, ships the technical part as defaults: FAQ sections, structured schema markup, and pages bots can crawl. That AEO is now a default feature of a site builder suggests the technical layer is already routine and the content layer is where the work is.

### 5. Off-site: amplify, then earn

Because consensus decides, owned content has to travel:

- **Owned social.** Tailor the site's content to each platform and post it. Which platform matters most shifts over time (*"sometimes Reddit is the most important source… sometimes it goes down"*), so the citation data, not habit, decides where.
- **Video.** Fresha publishes all its knowledge-base videos on YouTube because they are public and heavily cited by Google's AI Overviews and Gemini. Amiel's explanation: Google favours sources in its own ecosystem.
- **Reviews.** G2 and Trustpilot are read as independent confirmation. Fresha's support team follows up with customers after scored calls and is incentivised on review volume.
- **Earned media.** Industry publications and news, the largest citation category, and the hardest to control.

These channels also serve human buyers who read the same reviews and videos.

### 6. Downstream: a different visitor, a different team

Two consequences reach beyond content:

- **Visitors arrive late in the journey.** Buyers from answer engines have often done their comparison in the conversation and come ready to decide. The website's job shifts from education to conversion. The session names this and leaves it open; Bodnar & Flanagan describe the same thing as *"value of visits"* replacing *"volume of visits"*.
- **AEO is a marketing-wide job, not an SEO task.** At Fresha it spans product (which had owned SEO) and marketing (which owns content), with separate on-site and off-site teams. Amiel reports the same pattern at other firms: those still treating AEO as SEO *"are kind of still stuck in this on-site content stage."*

The loop is iterative: define the brand, find gaps, create, publish across channels, and **evolve** as the engines and citation patterns change.

## Debates and supersession

- **Measured, or one vendor's model of the engines?** The central claims (mentions across the web as the main factor; the 8% / 30% / 10% citation shares) come from XFunnel's and HubSpot's own analysis, presented without method, sample or date. Their outcome figures (+170% MQLs, +82% closed deals for AEO adopters, +8% monthly visibility) are omitted from the claims above: they come from a vendor selling the tool and do not separate what AEO did from which customers chose to adopt it. **Confidence is held at 0.75**, the schema ceiling for vendor sources without independent replication. An independent study of what AI answers cite, such as the academic GEO literature, is the ingest target that would move it.
- **Can a constructed prompt set stand in for demand?** Without published volumes, a prompt matrix measures the engine's answers to questions the firm *thinks* buyers ask. The inputs (sales calls, tickets) are real signals, but no source here validates a prompt set against actual usage. **Open.**
- **Personalisation undercuts measurement.** The same session says engines personalise heavily using each user's history and connected tools, and also that a firm can measure visibility with a fixed prompt set. A tracked answer is a generic-user answer, which the buyer may never see. **Open.**
- **Being crawled against being paid.** AEO asks brands to make content maximally crawlable. The [[2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet|Cloudflare one-year report]] documents publishers **blocking** AI crawlers by default to win licensing leverage. The two positions fit different businesses: a brand wants to be cited because the answer sells its product, while a publisher's product is the content itself. A firm that is both, such as a software company with a large editorial blog, faces a real choice. See [[agentic-web]].
- **Does the channel stay open?** [[2026-06-11-kilpatrick-sequoia-model-eats-the-harness|Kilpatrick (Google DeepMind)]] raises the SEO→GEO question from the platform side: Google aiming to maximise *"outcomes for customers,"* not eyeball time. If answer engines take on paid placement, as search did, organic AEO may shrink the way organic SEO did beneath the ads. No source in the corpus addresses this directly. **Open.**
- **Agents as buyers.** Chou describes the next step: agents choosing and signing up for products on a user's behalf (*"if the agents choose you… you're going to win huge"*). AEO as described here optimises an answer a human reads. Optimising for an agent that acts without a human reading anything may need different signals, such as an API, machine-readable pricing, or agent sign-up. **Open.**

## Related concepts

- [[agentic-web]] — the shift AEO responds to: search to answers, the broken referral bargain, crawler blocking and licensing.
- [[enterprise-ai-adoption]] — AEO as adoption forced by customers' behaviour rather than chosen.
- [[generative-ai]] — the *sea of sameness*: why original expertise is the content signal that differentiates.
- [[ai-agents]] — agents as the next kind of reader: from a human reading an answer to an agent acting on it.

## Sources consulted

- [[2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook]] — the fundamentals: anatomy of an answer, the prompt matrix, visibility / share of voice / citations, consensus, the six content signals, off-site channels, Fresha's practice.
- [[2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook]] — why it matters: traffic down, value of visits over volume, unique data against the sea of sameness.
- [[2026-06-19-chou-yc-lightcone-40-year-old-solo-founder]] — AEO as a platform default (FAQ, schema markup, crawlability), and agents as customers.
- [[2026-06-11-kilpatrick-sequoia-model-eats-the-harness]] — the platform view: the SEO→GEO question and outcomes over eyeballs.
- [[2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet]] — the publisher's opposite choice: blocking crawlers to price access.
