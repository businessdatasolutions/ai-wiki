---
type: source
kind: video
title: "Stop the Silent Traffic Drop: A Hands-On AEO Playbook | UNBOUND 2026 | HubSpot Live"
author: ["HubSpot Live"]
publisher: "HubSpot Live — UNBOUND 2026 breakout session by Beeri Amiel and Bradley Sanders (HubSpot product), with Elliott Braund (Fresha) as customer guest"
url: "https://www.youtube.com/watch?v=7UFQQldXSuo"
date_published: 2026-09-29
date_ingested: 2026-09-30
length: "~45:29 minutes (transcript ~364 segments; auto-generated captions, lightly ASR-cleaned; slides not visible)"
raw: "../../raw/videos/stop-the-silent-traffic-drop-a-hands-on-aeo-playbook-unbound-2026-hubspot-live.md"
tags: [hubspot, unbound-2026, beeri-amiel, bradley-sanders, elliott-braund, fresha, xfunnel, aeo, answer-engine-optimization, geo, ai-search, zero-click-search, citations, share-of-voice, brand-visibility, prompt-tracking, buyer-journey, personas, consensus, earned-media, trustpilot, youtube, reddit, content-agent, vendor-keynote]
dynamic_capabilities:
  - contextual/external-triggers
  - digital-sensing/digital-scouting
  - digital-transforming/redesigning-internal-structures
roles: [cmo, ceo, product-manager]
relationships:
  - type: supports
    target: 2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook
    via: "same firm and conference, eleven days apart, on the same shift of buyer research from search into answer engines; Bodnar and Flanagan give the marketing operating model, this session gives the procedure for being cited in AI answers"
    confidence: 0.8
  - type: supports
    target: 2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet
    via: "both concern discovery moving from search results to AI answers without the referral traffic following; Cloudflare measures it at network level, this session describes one vendor's response on the brand side"
    confidence: 0.65
---

# Amiel & Sanders (HubSpot UNBOUND 2026) — a hands-on AEO playbook

> As AI answer engines reshape discovery, many teams are seeing organic traffic decline without a clear plan for how to respond. This hands-on session walks through how to use AEO to understand your brand visibility, assess competitors, and identify the actions that matter most. You'll learn how to interpret key dashboards, analyze citations and competitor patterns, and turn those insights into a practical 30-day execution plan connected to HubSpot's content tools.

## TL;DR

A 45-minute breakout at HubSpot's UNBOUND 2026 conference, published on the HubSpot Live channel on 29 September 2026. The speakers are **Beeri Amiel**, senior director of product management at [[HubSpot]] and co-founder of XFunnel, an **answer engine optimisation (AEO)** start-up HubSpot acquired in December 2025; **Bradley Sanders**, a former HubSpot marketer now on the AEO product; and **Elliott Braund**, VP of revenue operations at Fresha, a booking platform for beauty and wellness businesses, as customer guest.

It is the corpus's first source on **what a brand does to be named in AI answers**. The central instruction: treat ChatGPT and Gemini as *"your best sales rep"*, which you have to train. The central empirical claim: *"By far the most important factor for showing up on answer engines is how often your brand is mentioned across the web. Not how many pages you have on your website."* Answer engines look for **consensus** across sources, so AEO is a cross-channel task: the firm's own website first, then social media, then earned media and reviews.

## Key claims

### 1. Why answer-engine leads matter

Amiel's account of the change: Google was a *"router"* that gave a firm several shots at a buyer across awareness, consideration and evaluation. An answer engine now carries the buyer through all of them in one conversation, with context from the user's history and connected tools, and gives a personalised recommendation. Two HubSpot claims follow:

- **Coming from an answer engine is HubSpot's strongest predictor of purchase.** *"Our number one indicator is coming from an answer engine today… a channel that didn't exist three years ago."*
- **Scale.** *"60% of Google searches now end without a click"*; ChatGPT and Gemini each have *"1 billion weekly active users."* He calls the shift *"a one-way door."*

Because these buyers arrive at the decision stage, not at awareness, the website's conversion job changes too. The session names this and leaves it out of scope.

### 2. Measuring visibility without search volumes

There is no prompt-volume data: OpenAI does not publish it, and Google's Search Console still shows keywords, not Gemini prompts. The replacement is a **test of the sales rep**: build a set of prompts and check what the engines say. The vocabulary:

- **Prompt**: the question typed; much longer than a Google query (Google averages three to five words).
- **Response**, with two parts: the answer text and the **citations**, the sources the engine used.
- **Brand visibility**: the share of tracked prompts in which the brand is mentioned. **Competitor mentions** are tracked alongside, giving **share of voice**.

Prompt sets are built as a **matrix of persona × buying-journey stage × region**, because a VP of marketing and a freelancer ask different questions about the same product, and journeys differ by region. The inputs are data the firm already has: sales calls, support tickets, customers' social posts, and the longer, prompt-like queries now appearing in Search Console.

A Similarweb chart (not shown in the transcript) is cited for engine differences: ChatGPT and Claude sessions run to about **15–16 words per prompt and about five prompts per session**, richer than Google AI Mode and Gemini, which are still used more transactionally. Amiel attributes the difference to ChatGPT and Claude being used as *"harnesses"* with connected tools.

### 3. On-site content: the source of truth

Sanders gives HubSpot-customer figures: **organic traffic down 27% year on year**, and **referral traffic up 20%** for customers optimising for AEO. Customers who started AEO report **170% more MQLs and 82% more closed deals**. Their own website accounts for about **8% of AI citations**, against about **30% for PR and news**, but it is where the brand *"control[s] the narrative"*: when engines find claims on third-party sites, they check them against the brand's own pages.

Six content signals:

1. **Clear, direct answers**, not buried in the text.
2. **Original expertise**: case studies, testimonials, reviews, the firm's own data.
3. **Entity richness.** Test: read one paragraph out of context. Does it say what the product does and for whom? If not, rewrite it. *"These bots are impatient readers."*
4. **Full-funnel coverage**: specific questions from awareness to decision, by industry and use case.
5. **Freshness**: *"You don't want to be the best answer two years ago."*
6. **Bot accessibility**: robots.txt not blocking crawlers; content not rendered only in JavaScript.

The demo shows HubSpot's AEO tool: a prompt list (*"your keyword list for LLMs"*), a competitor winning a prompt (Zendesk), a recommendation, and a **content agent** that drafts a post from the cited sources plus a stored brand-context profile, then tracks the post's citation rate after publishing. HubSpot reports an **8% month-on-month visibility gain** for users following the recommendations.

### 4. Off-site: consensus across the web

Because mention frequency across the web is the main factor, owned content has to be **amplified**:

- **Social media**, about **10% of citations**. Which platform matters shifts over time (*"sometimes Reddit is the most important source… sometimes it goes down"*), so the citation analysis decides where to post.
- **Earned media and reviews**: industry publications, G2, Trustpilot. The engines use these as the independent confirmation that makes a brand's claim credible.

### 5. One customer's practice: Fresha

Braund's account:

- **Before any tooling**, ten people in a room typed the same question (*"what's the best booking software for my beauty and wellness business?"*) into ChatGPT, read its citations, and built landing pages and PR to match those sources.
- **Organisation.** AEO sits across product (which owned SEO) and marketing (which owns content). There is one on-site team (blog, knowledge base, landing pages) and one off-site social team.
- **What works now.** **YouTube**: all knowledge-base videos are published there because it is public and heavily cited, especially by Google's AI Overviews. **Trustpilot**: the support team moved to 24/7 live chat and phone, follows up with customers after scored calls, and is incentivised on reviews; the rating is now 4.8.
- **Results.** **86% brand visibility, 16% share of voice**, and higher conversion from answer-engine leads than from any other source. No baseline or counts are given.

The session closes with a five-step plan: **define the brand → find gaps → create → publish everywhere → evolve.** This is the same shape as the Express → Tailor → Amplify → Evolve loop from HubSpot's main-stage keynote.

## Dynamic-capabilities reading

- **`contextual/external-triggers`** — buyers moving their research into answer engines is the trigger. The firm did not choose it, and its search traffic fell as a result.
- **`digital-sensing/digital-scouting`** — prompt tracking is a sensing routine: a structured, repeated check of what the market's new intermediary says about the brand and its competitors, by persona and region.
- **`digital-transforming/redesigning-internal-structures`** — at Fresha, AEO spans product and marketing, with separate on-site and off-site teams, and the support team's incentives are tied to review volume. Amiel describes the same move in other firms, from an SEO or content-team task to *"a marketing team problem"*.

## How it connects

- The fundamentals from this session, without the product demo and vendor figures, are kept on [[concepts/answer-engine-optimization|answer-engine-optimization]], the AEO counterpart of an SEO page.
- Eleven days earlier HubSpot's CMO gave the main-stage version: [[2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook|Bodnar & Flanagan]] on the traffic collapse and the marketing loop. This session is the operational layer under their *Amplify* stage.
- [[2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet|Cloudflare's one-year report]] measures the same shift at network level. It argues from the publisher's side that access to content should be priced; this session is about getting content used and cited. See [[concepts/agentic-web|agentic-web]].
- The *train your sales rep* framing and the persona × stage matrix are the marketing counterpart of the context-layer argument in [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]]: the model knows only what it has been given.

## What was actually ingested

The full 45:29 session from YouTube's auto-generated English captions. Cleanups at acquire: YouTube's spoken-timestamp artefacts were stripped, and speech-recognition errors in names and terms were corrected (AO → AEO, ChatGPT variants, Barry → Beeri, Fresher → Fresha, Zindesk → Zendesk, Trust Pilot → Trustpilot). The slides and demo screens are not in the transcript, so the Similarweb chart and the dashboard figures are known only from what the speakers read out.

## Linked entities and concepts

- Entities: [[HubSpot]]
- Concepts: [[concepts/answer-engine-optimization|answer-engine-optimization]] (the fundamentals from this session, without the product), [[concepts/agentic-web|agentic-web]], [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]]
- **Dangling** (single-source mention, deferred): Beeri Amiel, Bradley Sanders, Elliott Braund, Fresha, XFunnel, Similarweb

## Scope and reliability

**A product session by the vendor that sells the tool.** Every figure except the Similarweb chart and the 60% zero-click figure comes from HubSpot or its customer and is given without method: the answer-engine purchase predictor, −27% organic, +20% referral, +170% MQLs, +82% closed deals, +8% monthly visibility, and Fresha's 86% / 16%. The MQL and deal figures in particular are likely to reflect which customers chose to adopt AEO, not only what AEO did for them. The 8% own-site / 30% PR citation shares and the claim that *"how often your brand is mentioned across the web"* is the strongest factor are stated without a source; they come from XFunnel/HubSpot's own analysis. The session's lasting contribution is the vocabulary (prompt, citation, visibility, share of voice), the persona × stage × region matrix, and the consensus argument, not the numbers.
