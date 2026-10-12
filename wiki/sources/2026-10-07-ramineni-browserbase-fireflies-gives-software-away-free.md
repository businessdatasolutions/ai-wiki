---
type: source
kind: video
title: "The $1B founder of Fireflies on why he gives his software away for free and what he charges for"
author: ["Browserbase"]
publisher: "Browserbase (YouTube) — Navigators interview series; Krish Ramineni (co-founder & CEO, Fireflies.ai) with host Paul Klein IV (founder & CEO, Browserbase)"
url: "https://www.youtube.com/watch?v=DtSf7cvG8is"
date_published: 2026-10-07
date_ingested: 2026-10-12
length: "~26:59 minutes (transcript ~819 lines; auto-generated captions)"
raw: "../../raw/videos/the-1b-founder-of-fireflies-on-why-he-gives-his-software-away-for-free-and-what-he-charges-for.md"
tags: [browserbase, navigators, krish-ramineni, paul-klein, fireflies, meeting-intelligence, ai-notetaker, saas-commoditization, free-tier, seat-based-pricing, usage-based-pricing, outcome-pricing, headless-software, salesforce, crm, vibe-coding-enterprise, model-routing, model-agnostic, open-weight-models, on-device-models, voice-agents, support-agent, customer-data-training, context-graph, capital-efficiency, founder-lessons, science-technology]
dynamic_capabilities:
  - strategic-renewal/business-model
  - digital-transforming/redesigning-internal-structures
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-09-08-gauch-bcg-so-what-will-ai-agents-replace-your-crm
    via: "Shared topic: whether agents or AI-built software replace the CRM, and whether CRMs go headless. Gauch (BCG) says agents replace the CRM's screen but not its governed record, and that CRMs move towards headless; Ramineni says 'I don't think you can vibe code a CRM' and that Salesforce 'had to make a hard decision like do we go headless'."
  - type: supports
    target: 2026-07-07-sinofsky-amble-a16z-software-in-the-age-of-agents
    via: "Shared topic: vibe-coding your way into enterprise software, and Salesforce going headless. Sinofsky points to undocumented exception handling and business logic; Ramineni points to 'how much workflow business logic … needs to exist' and uses Dropbox versus an S3 bucket as his analogy."
  - type: contradicts
    target: 2026-07-06-sevilla-emarketer-custom-ai-coded-apps-trim-saas-expenses
    via: "Shared topic: replacing CRM SaaS with AI-coded apps. Sevilla reports small firms (55-70 staff) that replaced Salesforce with vibe-coded apps; Ramineni says 'I don't think you can vibe code a CRM', while naming homebrew software in the SMB and mid-market as the open question. The disagreement turns on firm size, which both sources raise."
  - type: supports
    target: 2026-08-12-tan-a16z-new-rules-for-founders
    via: "Shared topic: the future of per-seat SaaS pricing. Tan says pure per-seat SaaS is 'not totally clear it will exist in another five or 10 years'; Ramineni asks what happens to seat-based revenue 'when more companies have fewer headcounts' and expects charging for agentic work instead."
  - type: supports
    target: 2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet
    via: "Shared topic: several models inside one business, and usage-based billing because of inference costs. Collison explains Stripe's OpenRouter and Metronome acquisitions this way; Ramineni describes routing across seven to ten model and speech providers and moving from seat to usage pricing. Same channel, published two days apart."
---

# Ramineni (Fireflies) — giving the software away and charging for agentic work (Browserbase Navigators, Oct 2026)

> Fireflies gives away unlimited meeting recordings and transcriptions. Krish Ramineni (Co-Founder & CEO of Fireflies) says that was the plan from day one: commoditize yourself before someone else does it for you.
>
> In this episode of Navigators, Paul sits down with Krish to talk about what happens to software when models drive most of the interaction. Krish thinks most SaaS will be given away for free and that companies will charge for the agentic work instead. If you don't become agentic, you become a data source or a connector inside someone else's model, and all the value goes to them. He explains why you can't vibe code a CRM, why seat-based pricing breaks when companies run with fewer people, and why Salesforce had to decide whether to go headless.
>
> They also cover how Fireflies hit unicorn status on $19M raised, how open weight models made the free tier possible, and why Fireflies routes across seven to 10 model providers.
>
> Browserbase gives AI agents a browser to operate in. Navigators is our series of conversations with the people building the agentic future.
>
> — channel description, Browserbase

## TL;DR

A 27-minute interview on the [[Browserbase]] channel, published 7 October 2026, in the channel's **Navigators** series. **Krish Ramineni**, co-founder and CEO of **Fireflies.ai** (an AI meeting notetaker), talks with **Paul Klein IV**, founder and CEO of Browserbase. The description names the host only as "Paul"; the keynote on the same channel introduces him as Browserbase's founder and CEO, and the host here speaks of Browserbase as *"being an infrastructure company"*. The video has title cards only and no slides.

Both speakers are founders talking about their own companies. Every figure in the episode (the unicorn valuation on $19M raised, 130 staff, the support agent's 90% accuracy, a trillion OpenAI tokens) is the founder's own and is not checked here. The host's company sells usage-priced infrastructure, and he says so when the talk turns to pricing.

The core claims:

1. **SaaS gets commoditised; agentic work gets paid** [18:00]. *"My personal take is SaaS will be commoditized. There will be a lot of regular SaaS that is going to be given away for free. That's something we're doing at Fireflies. And then companies are going to charge for the actual agentic work that is being done."* That *"can put into question seat-based pricing … What's going to happen when more companies have fewer headcounts?"* Fireflies *"grapple[s]"* with the move to usage pricing itself.
2. **"I don't think you can vibe code a CRM"** [16:22]. He cites *"the bloodbath in the public markets for SaaS companies"* and rejects the reading that vibe-coded software replaces them. His analogy: if that were true, *"a company like Dropbox or Box wouldn't exist because everyone would say, 'Oh, I'm just going to use an S3 storage bucket.'"* The open question he names is homebrew software in the SMB and mid-market. The threat he takes seriously comes from elsewhere: *"these AI labs are going to go up market. They're going to go after the SaaS layer."*
3. **Become infrastructure or become a connector** [19:47]. *"You either need to become an infrastructure company or you end up becoming a data source or connector that doesn't accrue a lot of value."* If a SaaS company is only *"some sort of connector in some other AI lab's model, you see where the value is accruing."* This is where *"Salesforce had to make a hard decision like do we go headless? Do we provide access to all of this data that we've been building for customers over the last 20 years, 25 years."*
4. **Open-weight models paid for the free tier** [11:34–13:17]. Trying open models for summarisation and other tasks brought costs down, and *"all of the cost benefits … we can give it back to users"*: unlimited recording, transcription and summaries on the free tier, capped only by storage. He also wants models that *"run on your device"* for an always-on assistant.
5. **Routing across seven to ten providers** [13:37–15:34]. Reasons given: enterprises that want their own private cloud, switching at scale, more than 100 languages and geographies, async versus real-time speech models, and a low-latency model for voice agents. *"The intelligence of the model is less important in the short term versus what I can do with a specific model for specific use cases. Like I don't need to distill the entire world to go solve something as simple as summarization."*

## The company, briefly

- **Years of failed products** [1:48–4:24]. Fireflies began around 2016–2018 with products for email relationship graphs and Slack task extraction, both in crowded markets. Meetings were picked because they were hard to capture at all; the bet was that *"over time the models will get better, transcription will get better."* *"We just stuck around long enough for it to become possible."*
- **A self-updating knowledge base** [5:44–6:12]. Some customers have six years of meetings in Fireflies, *"knowledge that you would not find in Notion or in your Google Docs"*, and it changes as decisions change, unlike static docs. He compares the strategy to Google: capture first, organise better over time.
- **The second act** [25:17–26:19]. Fireflies is going back to the email and Slack products that failed a decade ago, now as assistants that feed *"a better knowledge graph, context graph around what a knowledge worker does"*, aimed at enterprise search.

## Running Fireflies on Fireflies

[7:21–10:17]. The company has **130 employees**, which Ramineni contrasts with competitors at *"500 to a thousand"*, and he says it tries *"to rebuild every process from scratch."* His internal rule: *"I don't want to say something twice. Once I say it, Fireflies captures it."*

- **Knowledge of absent colleagues.** When someone leaves or is on holiday, the AI *"can actually answer questions on their behalf"*, including *"why did he not want to approve this decision a few weeks ago?"* He calls this a *"proactive manager"* for the work of reaching consensus.
- **A support agent.** Trained on the company's sales calls and support conversations rather than *"generic docs or wikis or FAQs"*, it answers *"at 90% accuracy"* and *"can handle more support tickets than any other human on our team."* No denominator or measurement method is given.
- **Meetings that do work.** With *"almost like a hundred different MCP connections and integrations"*, a feature discussed in a meeting gets designed in Figma or pushed to Replit or Lovable while the meeting runs; *"by the time I hit end on a meeting, all of my work is done."*
- **Voice agents** [14:37] take meetings on a user's behalf: screening interviews, customer surveys, testimonials, sales discovery calls.

## Data policy

[10:37–11:31]. Ramineni says many AI notetakers *"take your data and then train models on it without explicitly telling you"*. Fireflies decided early that it *"will not train on customer data. We will not license it or repackage it or sell it in any form, even anonymous form."* This is a vendor's own statement about its policy and about its competitors.

## Funding

[23:20–24:52]. A $5M seed and a $14M Series A, then no further raise before a valuation of about $1 billion. Fireflies was profitable, global and remote from the start, with *"no sales for the first three years"* and no marketing until *"10, 20 million in revenue."* He says giving so much away was the reason to raise at all: *"like if we don't do that, someone else will do that for us."*

## The host's position

Klein makes two claims of his own. First, *"every application layer company becomes an infrastructure company"* [19:40], because the value of a company like Fireflies sits in the ingestion and context work beneath the app. Second, he is *"super bullish on model agnostic application layer companies"* [22:34] because *"the switching cost between moving models needs to be as low as possible"*, especially *"as the open source becomes more and more competitive."* He prefers usage pricing because *"when you win, we win."* He also reports that Ramp *"just launched a model router today for financial agents"* [13:24]; that is not checked here.

## Dynamic-capabilities reading

- **`strategic-renewal/business-model`** — the main subject. Ramineni gives the core product away, plans to charge for agentic work, and questions seat-based pricing when customers have fewer staff. He frames the free tier as deliberate self-cannibalisation.
- **`digital-transforming/redesigning-internal-structures`** — a 130-person company rebuilding processes around its own product: a support agent handling more tickets than any person, recall of absent colleagues' reasoning, and meetings that hand work to design and coding tools.
- **`contextual/external-triggers`** — the falling SaaS valuations, cheaper open-weight models, and AI labs moving into the application layer are the outside pressures he responds to.

## Related in this wiki

- [[2026-09-08-gauch-bcg-so-what-will-ai-agents-replace-your-crm|Gauch (BCG)]] asks whether agents replace the CRM and answers that they replace its screen, not its record; Ramineni says you cannot vibe code a CRM. Both mention CRMs going headless.
- [[2026-07-07-sinofsky-amble-a16z-software-in-the-age-of-agents|Sinofsky and Amble (a16z)]] discuss vibe-coding into enterprise software and Salesforce's headless move, placing the difficulty in undocumented exception handling; Ramineni places it in workflow business logic.
- [[2026-07-06-sevilla-emarketer-custom-ai-coded-apps-trim-saas-expenses|Sevilla (EMARKETER)]] reports small firms that replaced Salesforce with AI-coded apps. Ramineni says a CRM cannot be vibe coded, and names the SMB and mid-market as the place where homebrew might be viable.
- [[2026-08-12-tan-a16z-new-rules-for-founders|Tan (a16z)]] calls per-seat SaaS a wedge rather than a moat; Ramineni asks what happens to seat revenue as headcount falls.
- [[2026-10-05-collison-browserbase-will-agents-buy-things-on-the-internet|Collison (Stripe)]], on the same channel two days earlier, explains Stripe's purchases of OpenRouter (several models per business) and Metronome (usage-based billing). Ramineni describes running both practices at an application company.

## Linked entities and concepts

- Entities: [[Browserbase]], [[OpenAI]], [[Anthropic]].
- Concepts: [[open-source-ai]] (open weights as the cost base of a free tier), [[small-language-models]] (task-specific routing; on-device ambitions), [[vibe-coding]] (the CRM question), [[enterprise-ai-adoption]] (Fireflies' internal use), [[ai-agents]] (support and voice agents).
- **Dangling** (single-source mention, deferred): Krish Ramineni, Fireflies.ai, Paul Klein IV (host here and keynote speaker in the Browserbase Navigate 2026 keynote; not in `author:`), Salesforce, Ramp, Perplexity.

## Debates and supersession

- **Interested parties.** Ramineni is describing his own company's pricing as the direction of the industry. Klein runs a usage-priced infrastructure company and says application companies become infrastructure companies. Neither offers outside evidence for the general claims.
- **"You can't vibe code a CRM" versus small-firm replacements.** See the Sevilla edge above. Ramineni's own caveat (SMB and mid-market homebrew) is where the two sources meet.
- **Free software, paid agentic work.** The episode states the model but gives no pricing details, revenue split or usage figures, and Ramineni says Fireflies is still working out usage pricing.

## Source quality

YouTube's auto-generated English captions (track `en-orig`), fetched with yt-dlp after the transcript panel failed to render three times; not ASR-cleaned at acquire. Quotes here are corrected only for names and terms the captions garble: *Chris* → Krish, *SAS* → SaaS, *replet* → Replit, *acrue* → accrue. The host mentions an open-weight *"Kimmy K3"* model [10:27], read here as Moonshot's Kimi K3, which other wiki sources name. The host's self-introduction is cut at [0:54], so his surname comes from the keynote on the same channel. The episode runs 26:59 with the description's 13 chapters as headings; there are no slides or diagrams, so no stills were taken.
