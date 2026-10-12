---
type: source
kind: video
title: "Agents will use the internet - Navigate 2026 Keynote"
author: ["Browserbase"]
publisher: "Browserbase (YouTube) — opening keynote of Browserbase's first Navigate conference (2026); speaker Paul Klein IV, founder and CEO"
url: "https://www.youtube.com/watch?v=-2lu8BS2gPM"
date_published: 2026-09-14
date_ingested: 2026-10-12
length: "~18:25 minutes (transcript ~517 lines + 9 stills)"
raw: "../../raw/videos/agents-will-use-the-internet-navigate-2026-keynote.md"
stills: "../../raw/videos/agents-will-use-the-internet-navigate-2026-keynote.stills.md"
tags: [browserbase, navigate-2026, paul-klein, vendor-keynote, product-launches, computer-use, browser-agents, headless-browsers, stagehand, playwright, search-api, fetch-api, model-gateway, model-routing, action-caching, managed-agents, web-bot-auth, agent-identity, agent-authentication, iam, okta, 1password, clerk, ramp, checkr, commure, capabilities-overhang, diffusion, waymo-analogy, long-tail-web, science-technology]
dynamic_capabilities:
  - contextual/external-triggers
  - digital-transforming/navigating-innovation-ecosystems
relationships:
  - type: supports
    target: 2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet
    via: "Same conference (Navigate 2026), same host. Shared topics: computer use as the way agents reach sites that will never ship an API or MCP (both use the DMV as the example), and telling good agents from bad bots. Klein gives the infrastructure vendor's product answer; Collison speaks from the payments side."
  - type: supports
    target: 2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet
    via: "Shared topic: Web Bot Auth and the good-bot / bad-bot problem. Cloudflare reports non-human traffic above 50% and builds bot authentication on the site side; Klein says Browserbase signs its agents with Web Bot Auth and that Cloudflare, Vercel and reCAPTCHA accept its verified traffic."
  - type: supports
    target: 2026-06-09-cloudflare-investor-day-2026
    via: "Shared topic: cryptographic agent identity as web infrastructure. Cloudflare's deck pitches Web Bot Auth as the way to monetise trusted automated demand; Klein presents Browserbase as an issuer of that identity for its customers' agents."
  - type: contradicts
    target: 2026-04-25-masad-replit-ceo-only-two-jobs-left
    via: "Where the computer-use bottleneck sits. Masad (April 2026) calls computer-use agents a 'mystery' that matured more slowly than he expected, a model-capability lag. Klein (September 2026) says 'the models are ready, but the web isn't': the gap is access, identity and authentication on the web side. Both reach for the self-driving analogy."
---

# Klein — Agents will use the internet (Browserbase Navigate 2026 keynote)

> *(The video carries no channel description on YouTube; the chapters are: Introduction · The case for AI agents · Browserbase mission and impact · Core infrastructure primitives · Control and intelligence layer · Customer success stories · Managed agents product · Trust, identity, and access · Vision and call to action.)*
>
> — Browserbase channel metadata

## TL;DR

The 18-minute opening keynote of **Navigate 2026**, the first conference run by [[Browserbase]], which sells cloud browsers and related infrastructure for AI agents. The speaker is **Paul Klein IV**, Browserbase's founder and CEO (introduced on stage as founder and CEO; the full name is on his own identification-card slide). It is a vendor keynote: the thesis, the benchmark chart and the customer figures all come from the company selling the platform, and none is independently sourced.

The argument has three steps:

1. **The models are ready, the web isn't.** Klein calls it a *"capabilities overhang"*: Browserbase has *"saturated some of our tasks on frontier models in sandboxes,"* but agents struggle on the live web [1:52–2:25]. The web was built by and for humans, and he does not expect it to be rebuilt: *"Waymo didn't have to rebuild the roads for AI. They just taught it how to drive like a human"* [3:05–3:37].
2. **A platform of primitives for the web as it is.** Browsers, a Search API, a Fetch API, the open-source **Stagehand** framework, a model gateway that routes and caches, a code runtime next to the browser, and a managed-agents API built from all of them [4:39–13:05].
3. **Identity and authentication are the next gate.** Sites cannot tell *"bad bots"* from *"good agents"*; Browserbase signs its agents with **Web Bot Auth**, partners with Okta, 1Password and Clerk on logins, and launches an **Agentic Identity Suite** in early access [13:18–15:49].

He closes on a policy-shaped claim: if agents can only use sites that ship APIs or MCP servers, *"it could be a walled garden of … gatekeepers and tollkeepers,"* and *"the DMV, my local barbershop"* will be left out [15:49–16:50].

## The thesis: a capabilities overhang on the web

Klein opens with the company's core belief: *"In the next 12 months, every task humans do will be assisted by AI"* [1:06]. The slide narrows it to tasks done *online*, assisted *by agents*. His explanation for why this has not happened yet is the overhang: *"intelligence is advancing faster than the world can put it to work"* (the slide's wording) [1:52]. Models solve tasks in isolation, *"but then when we see our agent go out into the real world web, it gets a little more complicated"* [2:12].

Why the web specifically: humans spend *"over 4.45 trillion hours"* browsing a year (slide and narration; no source given) [2:31]. Browserbase reports **500 million sessions** run *"across four different geographies"*, which it converts to *"2,000 human years of browsing"*, with a team of 75 [4:10–4:37]. That reach is *"7% of the active web"*; the remaining 93% is the stated target [4:39]. How "active web" or "touched" is measured is not explained.

He calls Browserbase *"not just an infrastructure company. We're a diffusion company"* [3:45]: the fastest way to get AI into daily tasks is to give it the same capability people use, a browser.

## The platform

The architecture slide (Visual canon 1) stacks the products in two columns over three shared layers. **Retrieve** (Fetch, Search) and **Interact** (Agents, Browsers) sit on a model gateway, agent identity and a runtime.

- **Browsers.** *"I've spent most of my career getting browsers to run on servers"* [5:49]. Running a browser at cloud scale needs file upload and download, screenshots, recordings and replays.
- **Search API** (launched earlier in 2026): one query in, a list of URLs out, *"to help your agent know where to start"* [6:30]. The slide adds that it queries the live web rather than a cached index.
- **Fetch API**: a URL in, structured content out, running on the same browser infrastructure, which Klein says makes it *"more reliable, performant, and accurate than other providers"* [6:56]. The slide specifies markdown output and JavaScript rendering.
- **Stagehand**, the open-source browser-automation framework. Puppeteer, Playwright and Selenium *"fall short in AI workloads because they weren't built for AI. They were built for humans writing tests"* [7:41]. Claimed: **1.4 million downloads a week, 80% more token-efficient than Playwright, twice as fast** [8:02].
- **Model gateway**, *"optimized for the domain of browsing the web"*: it routes simple pages to cheap models and hard tasks (*"doing your taxes or interacting with iframes"*) to frontier ones, and caches actions *"using a proprietary caching strategy that actually won't blow up the cache keys if the page subtly changes"* [8:41–9:21]. The slide claims up to 50% lower token spend.
- **Functions**, a sandbox for agent-written code that runs next to the browser, because *"roundtrip latency from your code to the browser and back is the bane of performance"* [9:33].
- **Browserbase Agents**, a managed agent with the primitives built in, which *"will optimize over time … by looking at the traces it's generated"* [12:25]. The claim: *"with a great harness, Browserbase Agents is able to match frontier-level intelligence at half the cost because it's not just using inference every time"* [12:43]. The chart behind it (Visual canon 7) shows a success rate but names no benchmark and shows no cost.

## Customer cases (vendor-reported)

Klein says Browserbase is a customer of all three.

- **Ramp** uses browser agents to fetch receipts from merchant portals without APIs: *"5 million receipts every single month"* [10:40]. The slide adds 24,000+ hours of manual work saved a month.
- **Checkr** (identity verification and background checks) moved a legacy Playwright implementation, *"and a whole team maintaining it,"* onto Browserbase, so the team spends less time *"fixing broken connectors"* [10:53]. The still taken from this window is a camera shot, so the slide's figures could not be checked.
- **Commure** uses a browser agent to read insurers' websites and fill forms for healthcare providers [11:36]. The slide: 20× more claims processed daily and 8,000+ hours of manual work automated a month.

## Identity and access

The last product section is the one that connects to [[agentic-web]].

- **Bad bots vs good agents.** *"For the longest time, there were bad bots and the web now can't differentiate between bad bots and good agents"* [13:18]. **Web Bot Auth** *"allows us as Browserbase to sign our agents, say where they're coming from,"* and Vercel, reCAPTCHA and Cloudflare *"are working with us to help identify and accept our traffic from our verified agents"* [13:41]. He describes it as *"an identification card for your agent"*, issued by Browserbase, which then lobbies more sites to accept it [14:00].
- **Logins.** *"Most systems on the internet actually live behind authentication"* [14:29]. An agent acting for a person needs passwords, sessions, 2FA and one-time codes, cookies and location. Browserbase partners with **Okta, Clerk and 1Password** because *"we're only one side of the equation"* [14:59].
- **Agentic Identity Suite**, in early access: managed secrets, an email inbox per agent, stored cookies and managed authentication, so that customers *"don't have to think about identity and authentication ever again"* [15:20].

The governing principle, on its own slide: *"If a human is allowed to do a task so should their agent"*, because *"agents are delegates on our behalf"*, to be done *"responsibly with the right tracking, trust, and guardrails"* [15:40–15:54].

## The closing argument: diffusion, not a walled garden

*"If we don't do this, AI will only be able to integrate with people who build APIs and MCPs. And it could be a walled garden of, you know, gatekeepers and tollkeepers saying who's allowed to access what. We want to arm the rebels"* [16:11]. Small businesses and public services *"won't be launching an MCP or API anytime soon, but they should benefit from your agents transacting with them"* [16:36]. He mentions customers such as *"the lumber factory in Mexico, the shipping terminal in Singapore"* that *"want to make people's lives easier using AI agents, but they don't know how to start"* [17:17].

The argument cuts both ways for a browser vendor: a web of APIs and MCP servers would need less of what Browserbase sells.

## Dynamic-capabilities reading

- **contextual/external-triggers**: the keynote frames agents arriving on every website as an outside force that firms will have to accommodate, with an explicit twelve-month horizon for *"every task humans do online"*. For a site owner, the change is that a growing share of visitors are delegated agents that may carry a signed identity.
- **digital-transforming/navigating-innovation-ecosystems**: Klein says the identity problem *"requires a coalition of companies to solve it"*. The keynote names the partners: Vercel, reCAPTCHA and Cloudflare on Web Bot Auth, and Okta, 1Password and Clerk on agent authentication. Stagehand is open source. All three are ways of building an ecosystem around the platform.

## Related in this wiki

- [[2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet|Collison (Stripe), same conference]]: both use the DMV as the case for computer use over waiting for an MCP server, and both ask how the web will tell good bots from bad ones. Klein answers with Browserbase's own products; Collison speaks from the payments side.
- [[2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet|Cloudflare's one-year report]] and [[2026-06-09-cloudflare-investor-day-2026|Cloudflare's Investor Day deck]] describe Web Bot Auth from the side of the network that verifies the signature. Klein names [[Cloudflare]] as one of the parties accepting Browserbase's signed agents.
- [[2026-04-25-masad-replit-ceo-only-two-jobs-left|Masad (Replit), April 2026]] called computer-use agents a *"mystery"* that matured more slowly than he expected. Klein locates the gap on the web side instead. Both use self-driving as the comparison: Masad as the precedent that made him expect faster progress, Klein as the precedent for teaching AI to use infrastructure built for humans.

## Linked entities and concepts

- Entities: [[Browserbase]], [[Cloudflare]].
- Concepts: [[agentic-web]], [[ai-agents]], [[agent-harness]], [[small-language-models]] (model routing as a cost lever).
- **Dangling** (single-source mention, deferred): Paul Klein IV, Stagehand, Ramp, Checkr, Commure, Okta, 1Password, Clerk, Vercel, Waymo.

## Visual canon

All 36 stills in the manifest were viewed against their pixels. 27 were dropped:

- **Slogan and section slides** whose words the narration repeats (1, 4, 7, 8, 24, 30, 32–36), and the illustrative curve on slide 3.
- **Number slides spoken verbatim** (5, 9, 11, 16) and **lists Klein reads out** (27 credentials, 28 IAM partners).
- **Illustrations without content**: slide 6 (mock web forms), slide 12 (collage of old web pages) and slide 2 (eight industry tiles around the logo).
- **Camera shots with no slide** (10, 20, 31). For 10 and 31 Gemini returned slide text that is not in the frame. 20 was meant to be the Checkr case slide.
- **Slide 18** (Functions): the code sample is too small to read, and the narration makes its point.
- **Slide 29** (Agentic Identity Suite): caught mid-animation, showing only the first step.

The nine below carry content the narration does not. Six are room shots with the slide on the right-hand screen, so small print on them is legible only in the full-resolution original; each transcription was checked against a crop.

### 1 · One platform, two columns, three layers

![[assets/2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet/13-05m45-browserbase-one-platform-for-all-agentic-web-primitives.webp|Browserbase platform stack with Retrieve and Interact columns over model gateway, agent identity and runtime]]

*Still at [5:45](https://www.youtube.com/watch?v=-2lu8BS2gPM&t=345s) from Browserbase, "Agents will use the internet - Navigate 2026 Keynote".*

**Browserbase: one platform for all agentic web primitives**

| THE WEB (globe, top) | |
| --- | --- |
| **RETRIEVE**: Fetch · Search | **INTERACT**: Agents · Browsers |
| **MODEL GATEWAY** (faint subtitle, apparently "within Stagehand") | |
| **AGENT IDENTITY** | |
| **RUNTIME** | |
| **BROWSERBASE PLATFORM** | |

*Still vs. transcript:* the narration introduces the products one at a time. The slide shows the structure: a split between retrieving content and interacting with pages, both resting on shared model, identity and runtime layers.

### 2 · Search API

![[assets/2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet/14-06m48-search-api.webp|Search API slide: a query fans out to three lead records with ID, URL, title and meta]]

*Still at [6:48](https://www.youtube.com/watch?v=-2lu8BS2gPM&t=408s) from Browserbase, "Agents will use the internet - Navigate 2026 Keynote".*

**Search API**

- **Whole-web index.** Search spans the whole web, so your agent can discover sources on any topic.
- **Live, low-latency results.** Every query hits the live web rather than a cached index, so the data is current.

Diagram: query *"aftermarket car parts supplier"* → SEARCH → Lead #1, #2, #3, each with ID · URL · TITLE · META.

*Still vs. transcript:* Klein says only that it returns a list of URLs. The slide claims a live query instead of a cached index, and the example frames search as lead generation.

### 3 · Fetch API

![[assets/2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet/15-07m13-fetch-api.webp|Fetch API slide: a URL goes through the Fetch API into three markdown documents]]

*Still at [7:13](https://www.youtube.com/watch?v=-2lu8BS2gPM&t=433s) from Browserbase, "Agents will use the internet - Navigate 2026 Keynote".*

**Fetch API**

- **Token-optimized context.** Markdown output strips the boilerplate, sending just content in the shape your agent needs.
- **Live retrieval.** Fetch reads the current page using a live browser session with JavaScript support, not a cached copy.

Diagram: `HTTPS://WWW…` → FETCH API → three documents.

*Still vs. transcript:* the narration says "structured format". The slide says markdown, with the boilerplate stripped to save tokens, and JavaScript rendering through a live browser session.

### 4 · Model gateway: routing and action caching

![[assets/2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet/17-08m53-our-model-gateway-optimizes-token-spend.webp|Model gateway slide claiming up to half the token spend saved through routing and cached actions]]

*Still at [8:53](https://www.youtube.com/watch?v=-2lu8BS2gPM&t=533s) from Browserbase, "Agents will use the internet - Navigate 2026 Keynote".*

**Our model gateway optimizes token-spend**

- **The right model for each task.** Simple clicks go to fast, cheap models. Hard reasoning goes to frontier ones.
- **Never pay for the same action twice.** Cached actions return instantly, keeping token spend under control at scale.

Panel: **UP TO 50% TOKEN-SPEND REDUCTION**. The diagram shows the gateway with OpenAI and Anthropic marks on its ring.

*Still vs. transcript:* the 50% figure is on the slide only. No baseline or workload is given.

### 5 · Ramp

![[assets/2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet/19-10m27-ramp-case-study.webp|Ramp case slide: receipts fetched from merchant sites with no APIs]]

*Still at [10:27](https://www.youtube.com/watch?v=-2lu8BS2gPM&t=627s) from Browserbase, "Agents will use the internet - Navigate 2026 Keynote".*

**ramp** · *Every receipt, already filed.* Finance agents that pull receipts from merchant sites with no APIs.

| 5M+ | 24,000+ |
| --- | --- |
| receipts fetched every month | hours of monthly manual work saved |

*Still vs. transcript:* Klein gives the 5 million receipts. The 24,000-hour figure and the phrase *"merchant sites with no APIs"* are on the slide only.

### 6 · Commure

![[assets/2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet/21-11m50-commure-case-study.webp|Commure case slide: agents read claim status and EOBs across hundreds of providers]]

*Still at [11:50](https://www.youtube.com/watch?v=-2lu8BS2gPM&t=710s) from Browserbase, "Agents will use the internet - Navigate 2026 Keynote".*

**commure** · *Patients, not paperwork.* AI Agents read claim status and EOBs across hundreds of providers.

| 20x | 8,000+ |
| --- | --- |
| more claims processed daily | hours of manual work automated monthly |

*Still vs. transcript:* the narration gives no numbers and describes form filling. The slide names the task (reading claim status and explanation-of-benefits documents *"across hundreds of providers"*) and gives both figures. The 20× has no stated baseline.

### 7 · Managed agents API: a prompt in, structured data out

![[assets/2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet/22-12m42-managed-agents-api.webp|Managed agents API slide: a property-tax prompt returns a JSON record]]

*Still at [12:42](https://www.youtube.com/watch?v=-2lu8BS2gPM&t=762s) from Browserbase, "Agents will use the internet - Navigate 2026 Keynote".*

**Browserbase Agents · Managed agents API**

`POST /API/AGENTS/RUN`: *"Get the property tax owed for 500 W 2nd St, Austin TX from the Travis County portal"* → Browserbase (Browsers · Search · Fetch · Identity · Functions · Sandbox) → **returns structured data**:

```json
{
  "Parcel": "0203140419",
  "Owner": "2nd Street Holdings LLC",
  "taxYear": 2025,
  "taxDue": 5874210.42,
  "status": "paid"
}
```

*Still vs. transcript:* Klein says customers *"can use it in one prompt"*. The slide shows the contract: a natural-language task against a public-sector portal, and a typed JSON record back. The record is a demo example.

### 8 · The benchmark chart behind "half the cost"

![[assets/2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet/23-12m55-frontier-model-browsing-capabilities-at-half-the-cost.webp|Bar chart of browsing success rates for Browserbase Agents and three frontier models]]

*Still at [12:55](https://www.youtube.com/watch?v=-2lu8BS2gPM&t=775s) from Browserbase, "Agents will use the internet - Navigate 2026 Keynote".*

**Browserbase Agents** · *Frontier model browsing capabilities at half the cost.*

| Browserbase | Fable 5.1 | GPT 5.6 Sol | Gemini 3.5 |
| ---: | ---: | ---: | ---: |
| 92% | 92% | 85% | 74% |

*Still vs. transcript:* the narration has no numbers. The chart puts Browserbase Agents level with Anthropic's Fable 5.1 and ahead of OpenAI's and Google's models. It names no benchmark or task set, does not say whether the competitors ran in Browserbase's harness, and shows no cost axis, so the "half the cost" claim has no support on the slide.

### 9 · The agent's identification card

![[assets/2026-09-14-klein-browserbase-navigate-2026-keynote-agents-will-use-the-internet/25-14m11-web-bot-auth-identification-card.webp|Mock identification card for an AI agent issued by Browserbase under Web Bot Auth]]

*Still at [14:11](https://www.youtube.com/watch?v=-2lu8BS2gPM&t=851s) from Browserbase, "Agents will use the internet - Navigate 2026 Keynote".*

**We've partnered with leading web infrastructure companies on Web Bot Auth.**

| Browserbase · Identification card · No. 27697372273 | |
| --- | --- |
| Name | AI AGENT |
| Human | PAUL KLEIN IV |
| Date | AUGUST 28, 2025 |
| Intention | TRAVEL THE WEB |

*"This card certifies the bearer safe travels across the web. Issued by Browserbase<<<<<0008282025"*

*Still vs. transcript:* Klein uses the ID-card metaphor. The card shows what the metaphor binds together: the agent, the human it acts for, a date and a stated intention. It is a mock-up, not the Web Bot Auth wire format.

## Debates and supersession

- **Interested party throughout.** Browserbase sells every product in the keynote, and the event is its own. The overhang thesis, the 7% / 93% framing, the Stagehand-versus-Playwright figures, the 50% gateway saving, the benchmark chart and all customer figures are company claims. None comes with a method. Ramp, Checkr and Commure are named as both customers and suppliers of Browserbase.
- **Where is the bottleneck: model or web?** Klein says the web. [[2026-04-25-masad-replit-ceo-only-two-jobs-left|Masad]] described computer use as lagging on capability. These may describe different moments (April vs September 2026) or different task sets. The only evidence in the keynote is Browserbase's own unpublished internal tasks.
- **Rebuild the web, or teach agents the old one?** Klein argues against waiting for APIs and MCP servers. [[Cloudflare]]'s sources describe the site side building new rails (pay-per-crawl, x402). Web Bot Auth sits in both camps: it needs no change to a site's pages, but it does need the site, or its CDN, to verify signatures.
- **"Arm the rebels" and gatekeeping.** The walled-garden argument is made by a company whose agents need sites to let them in. Browserbase also issues the identity that sites are asked to trust and lobbies sites to adopt it. That makes it a gatekeeper of a kind too. The keynote does not address this.

## What was actually ingested

The full 18:25 keynote, from the YouTube transcript panel. The captions are auto-generated (ASR) and were not cleaned at Acquire. Quoted names were fixed: Klene → Klein, Whimo → Waymo, Stage Hand → Stagehand, Playright → Playwright, webbot off → Web Bot Auth, Versell → Vercel, recapture → reCAPTCHA, octa → Okta, Checker → Checkr, Commir → Commure. The 36-still Gemini manifest was verified against every frame; see the Visual canon for what was kept. The publish date (2026-09-14) is the video's; the conference date is not stated in the video.
