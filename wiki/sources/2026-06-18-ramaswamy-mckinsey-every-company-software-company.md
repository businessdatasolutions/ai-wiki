---
type: source
kind: video
title: "AI Is Turning Every Company Into a Software Company (McKinsey Podcast — Sridhar Ramaswamy)"
author: ["McKinsey & Company"]
url: "https://www.youtube.com/watch?v=Epi-GQUoNrg"
date_published: 2026-06-18
date_ingested: 2026-06-20
zotero_item_key: PMSZEARN
zotero_collection: ai-wiki
length: "~25:46 minutes (transcript ~700 segments / ~1370 lines; auto-generated ASR transcript, light cleanup applied to proper nouns)"
raw: "../../raw/videos/ai-is-turning-every-company-into-a-software-company.md"
tags: [sridhar-ramaswamy, snowflake, mckinsey-podcast, eric-kutcher, industrialization-of-intelligence, every-company-a-software-company, when-anyone-can-code, uber-programmers, 50x-100x, critic-agent, security-critic-agent, cortex-code, snowwork, agentic-enterprise, consumption-pricing, not-every-token-same-value, beneath-vs-above-the-model, open-source-models, ai-with-roi, support-automation, business-transformation-not-technology, viral-adoption, snowhouse, demo-team-redeployment, growth-not-headcount, protect-your-career, malleability, first-principles-generalist, neeva, google-ads]
dynamic_capabilities:
  - digital-sensing/digital-scenario-planning
  - digital-seizing/rapid-prototyping
  - digital-seizing/strategic-agility
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - strategic-renewal/business-model
  - contextual/external-triggers
  - contextual/internal-enablers
roles: [ceo, coo, cto, cdo, transformation-lead]
relationships:
  - type: supports
    target: 2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer
    via: "Ramaswamy's *uber programmers 50–100× more productive than a year ago* is the CEO-of-a-public-data-company instance of Tan & Hu's *1000× engineer* / AI-native-company thesis. Both relocate the unit of value to a small class of agent-fluent builders and argue the org reorganises around them (Ramaswamy: *no org silos in a world of agents*)."
    confidence: 0.75
  - type: supports
    target: 2026-06-17-ng-langchain-interrupt-future-of-ai-agents
    via: "Two same-week (mid-June 2026) enterprise reads converging: coding agents 50×-ing good programmers; the redeploy-don't-cut response (Ramaswamy moves the demo team into other roles; Ng's small generalist teams); growth over headcount-reduction; open-weight models hosted alongside frontier as a buyer hedge (Ng's optionality ↔ Ramaswamy's *beneath-vs-above-the-model* + open-source hosting)."
    confidence: 0.7
  - type: supports
    target: 2026-05-21-bender-google-io-software-engineering-tipping-point
    via: "*AI is turning every company into a software company / when anyone can code* is the CEO-vantage statement of Bender's programming-vs-software-engineering *tipping point* — software creation cost collapses, the installed-base lock-in of the *cottage industry* dissolves, and the discipline shifts from typing code to directing critic/security-critic agents."
    confidence: 0.7
  - type: supports
    target: 2026-05-13-jha-emergent-democratizing-app-building-with-claude
    via: "Both name *anyone-can-code democratization* at the floor-raising end — Ramaswamy's sales reps *shipping a new visualization dashboard or application by describing it in English* is the inside-an-enterprise instance of Emergent's domain-experts-shipping-apps thesis; the conversational interface replaces *bespoke web interfaces*."
    confidence: 0.65
---

# AI Is Turning Every Company Into a Software Company (McKinsey Podcast — Sridhar Ramaswamy)

> AI is dramatically reducing the cost and complexity of software creation. But when anyone can code, what does that mean for engineers and business leaders? Snowflake CEO Sridhar Ramaswamy sees an "industrialization of intelligence" that's fundamentally changing work. While this has terrified him at times, he also sees it as a tremendous opportunity for individuals and companies to scale their work. Ramaswamy tells McKinsey's North America Chair Eric Kutcher that he's seen a new class of "uber programmers" who are 50 to 100 times more productive than they were a year ago. They discuss how AI agents are changing software development, the future of pricing models, and how organizations can adapt to rapid technological changes.
>
> *— Channel description, [[McKinsey & Company]] (the McKinsey Podcast)*

A **~26-minute McKinsey Podcast episode** in which **Sridhar Ramaswamy** — CEO of **Snowflake**, ex-Google (16 years; IC → leader of the >10,000-person, $100B+ ads team), co-founder of the search startup **Neeva**, and a "reformed academic" in databases/query processing — is interviewed by **Eric Kutcher** (McKinsey's North America Chair). The conversation is a CEO-vantage read on AI's collapse of software-creation cost, the rise of "uber programmers," enterprise change management, AI pricing models, and career advice. Its load-bearing contribution to the wiki is the **"AI is turning every company into a software company"** thesis from a public-data-platform CEO's chair.

## TL;DR

**1. The "industrialization of intelligence."** Ramaswamy's framing: AI has a "fundamentally profound impact on the cost of software creation," cascading into how information is used/processed and what intelligence and decision-making mean. The only historical analogies "anywhere close" are the **printing press** and the **internet** — but AI's special aspect is that it also "brings intelligence," packed into the models: *"the industrialization of intelligence."*

**2. When anyone can code → "uber programmers."** Two predictions: (a) **many more people write software** — his sales reps "don't think twice about shipping a new visualization dashboard or honestly a new application … all they have to do is describe what they want done in English"; (b) a class of **"uber programmers"** who are **"50 to 100 times more productive"** than a year ago, who "intuitively understand what it means to use the power of coding agents." Thinking now is in terms of **agents** — a coder agent, a **critic agent** that criticises pieces of code, a **security critic** — so "industrial logic" is "subject to more criticism even before you share it with a single human being." Software shifts from a **"cottage industry"** (where an adopted product is sticky / not switched) to a world of much cheaper creation → "a lot of innovation but also a lot of disruption."

**3. Conversational interface as the new natural interface; "go to the god first."** Keeping up with the pace of change is eased because AI is **conversational** — "as long as one conceptually knows what it is we want to do, it's quite easy to learn by just asking the coding agents." The natural interface for software is migrating from "bespoke web interfaces … stylized to serve the masses" to a **free-flowing conversational interface**. His heuristic: treat most tasks like traffic — *"you go to the god first … ask Google Maps what you should do and then decide whether to do that or something else."* Learning loop: ask the AI, ask it to explain, ask it a different way, ask "why didn't you do this," debate it — "lo and behold you've learned something and probably made it better."

**4. The agentic enterprise / Snowwork — AI all the way down.** His thesis on the "agentic enterprise" (now a product, **Snowwork**) began as "effectively one long conversation with our coding agent" that he turned into a doc, pitched to CEOs, fed their feedback back into new versions, then turned into a deck via a coding agent — *"the amount of AI that goes into creating a document about AI was kind of surreal."*

**5. Pricing models — the consumption model and "not every token has the same value."** Software valuations have readjusted down because terminal value (90–95% of enterprise value) was repriced. Snowflake's **consumption model** ("customers pay only if they get value") is "inherently beneficial," and is what the major LLM providers use. But tokenization pricing "is not likely one that's going to last all that long" — *"not every token has the same value"* — and there will be push-back if **ROI doesn't keep pace** with the charge. Innovations: consumption pricing with **per-person + per-account limits** to avoid runaway spend (cf. Claude Code / Cursor charging per-user *and* per-token); some products go to subscriptions. **Demand is "very, very elastic"** for the coding agents that 50× good programmers. Open question: **what stays "beneath the model" vs "above the model"** — will disruption hit the layer close to end-users or a lower layer? **Open-source models** are "getting better and better"; Snowflake hosts them alongside frontier models and customers will use them "if they're as good."

**6. AI with ROI — two "surefire hits."** (a) **Software engineering** (Cortex Code next to Snowflake). (b) **Support** — the team "rolled our own support system … written in six weeks on top of Cortex Code," with "very little fanfare," and now "support queues are pretty much empty." The **SRE team** rewrote its alerting/observability platform on Cortex Code — problems that "would literally take 4 days … growling through Kubernetes logs" are "automated now." Beyond those, broader impact is in "making information flow a lot more smoothly."

**7. Business transformation > technology transformation.** *"This is more of a business transformation than a technology transformation"* (he gets "funny looks" for it). The point: it's **change management** and re-thinking organisation — *"I don't have to have the organizational silos … a certain reporting structure that doesn't have to happen in a world of agents."*

**8. Change management via *viral* adoption (a "happy accident").** Snowflake built Cortex Code (a.k.a. "Coco") with both a CLI and desktop version, didn't restrict it, and — because all company data already lives in Snowflake (the **Snowhouse** instance) — *"the entirety of the company became AI literate pretty much in a matter of six weeks … I did not have to mandate. I didn't have training programs. Coco was just so popular it spread virally because people got so much utility from it."* The lesson: **"make your team embrace AI without forcing it down everyone's throats."** Now: figuring out what AI means per function — e.g. *"we no longer need a demo making team because every account exec can make their own demo,"* so that team is **moved into other roles**; the work is identifying the **new jobs** AI creates and helping people transition.

**9. Growth, not headcount-cut (Kutcher's reframe, endorsed).** Kutcher notes Ramaswamy did *not* say "fewer developers" — he said "more code → grow my value proposition to clients at an outpaced rate," plus *"real opportunities for people I haven't been able to fill before."* Ramaswamy: *"that's absolutely the way I want things to work … the first option."* He won't pretend the other side doesn't exist — some people "struggle to adopt"; it affects performance management.

**10. Protecting your career.** Ramaswamy (a software engineer by training, with two software-engineer sons, 26 and 24) says he is *"terrified about their future employment"* and pushes technical people "to be at the cutting edge of how development should be done today." His appeal to Snowflake staff: *"not just make Snowflake better, it's also protect your livelihood. This is a time of massive change and you need to embrace it to thrive."*

**11. Career lessons + advice for future leaders.** From Google: Larry Page's maxim *"never aspire to be someone successful … find your own reason to succeed, bring your own imprint"*; the **mobile transition (~2009–10)** was "among the most terrifying things" as query growth flattened and "everyone was predicting the end of Google." Neeva was "an impetuous wild experiment" — competent product, hard to commercialise → acquired by Snowflake. Three pieces of advice: **hard work** ("I work seven days a week and I'm happy for it"); **malleability** (the interview question: *"tell me something meaningful you have changed in yourself over the past year"*); **don't set limits / don't self-censor** — think "from first principles about everything from communication to marketing to strategy to sales," driven by genuine **curiosity**.

## How this source touches the wiki (dynamic capabilities)

- **`digital-sensing/digital-scenario-planning`** — the *industrialization-of-intelligence* framing, the printing-press/internet analogies, the forecast that tokenization pricing won't last, and the *beneath-vs-above-the-model* disruption question are explicit future-state scenarios for the software industry.
- **`digital-seizing/rapid-prototyping`** — the support system built in **six weeks** on Cortex Code; the SRE observability rewrite; sales reps shipping dashboards/apps from an English description.
- **`digital-seizing/strategic-agility`** — **redeploying** the demo team into other roles; reorganising without org silos "in a world of agents"; experimenting with consumption-pricing guardrails (per-person/per-account limits); hosting open-source models alongside frontier.
- **`digital-transforming/redesigning-internal-structures`** — *"I don't have to have the organizational silos … reporting structure that doesn't have to happen in a world of agents"*; identifying new jobs and transitioning people.
- **`digital-transforming/improving-digital-maturity`** — the whole company becoming **AI-literate in six weeks** via viral Coco adoption (no mandate, no training program), enabled by company-wide data in Snowhouse.
- **`strategic-renewal/business-model`** — the **consumption pricing** logic ("pay only if you get value"), the *every-company-a-software-company* repricing of software, and the dissolution of the sticky-installed-base "cottage industry."
- **`contextual/external-triggers`** — the AI-driven collapse in the cost of software creation as the external trigger reshaping the whole industry.
- **`contextual/internal-enablers`** — **Snowhouse** (all company data in Snowflake) + an unrestricted **Cortex Code** as the standing enablers that made viral AI literacy possible.

**Roles override** (`roles:` explicit): `ceo, coo, cto, cdo, transformation-lead`. The source is a CEO-vantage account centred on *enterprise transformation + how software/engineering changes + change management*; the override focuses on the top-exec, technology, and transformation-ownership roles and drops the broader finance/HR/marketing cluster the eight cells would otherwise inherit (pricing is discussed but the CFO angle is secondary).

## Linked entities and concepts

- Concepts this source informs: [[vibe-coding]] (sales shipping apps from English; conversational interface), [[agentic-engineering]] (uber programmers 50–100×; critic/security-critic agents), [[enterprise-ai-adoption]] (business-transformation-not-technology; viral adoption; the two ROI "surefire hits"; consumption pricing), [[automation-vs-augmentation]] (growth-not-headcount; redeploy the demo team; support automation), [[software-3.0]] (industrialization of intelligence; cost-of-software collapse; conversational interface replacing bespoke apps), [[durable-skills]] (malleability, first-principles generalism, curiosity), [[ai-employment-effects]] (terrified-for-sons; uber programmers; protect-your-career; growth not cuts), [[foundation-models]] (open-source models hosted alongside frontier; beneath-vs-above-the-model).
- Entity (already in wiki): [[McKinsey & Company]] (channel/publisher — the McKinsey Podcast; source-count bump).
- **Dangling** (single-source mentions, deferred per the second-source promotion rule): **Sridhar Ramaswamy** (CEO, Snowflake — guest; first appearance), **Snowflake** (the company; **Cortex Code / "Coco"**, **Snowwork**, **Snowflake Intelligence**, **Snowhouse** are its products/instances), **Eric Kutcher** (McKinsey North America Chair — interviewer), **Neeva** (Ramaswamy's search startup, acquired by Snowflake), Larry Page / Sergey Brin / Eric Schmidt (Google-era mentions), Google ads (career context).

## Source-to-source relationships

- **Supports** [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer]] — *uber programmers 50–100×* ↔ *1000× engineer* / AI-native company.
- **Supports** [[2026-06-17-ng-langchain-interrupt-future-of-ai-agents]] — same-week enterprise read: coding-agent 50×, redeploy-don't-cut, open-weight hosting, growth-over-headcount.
- **Supports** [[2026-05-21-bender-google-io-software-engineering-tipping-point]] — *every company a software company / when anyone can code* is the CEO-vantage statement of the programming-vs-engineering tipping point.
- **Supports** [[2026-05-13-jha-emergent-democratizing-app-building-with-claude]] — anyone-can-code democratization (sales reps shipping apps from English).

*Neighbour-scan candidates surfaced but not edged* (no specific-claim engagement; logged to keep the cluster honest): [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu / YC]], [[2026-04-25-masad-replit-ceo-only-two-jobs-left|Masad / Replit]], [[2026-05-05-stanford-ai-club-chamath-on-how-to-win-in-the-ai-era|Chamath]] (software factory), [[2026-06-03-warren-yc-how-to-build-an-ai-native-services-company|Warren / YC]] — all share the *AI-native / anyone-can-code* theme but Ramaswamy doesn't engage their specific claims. (Not every co-occurrence is a relationship.)

## Source-quality note

Auto-generated (ASR) transcript fetched via the [[youtube-transcript-skill]] (Playwright/DOM route); light cleanup applied to proper nouns (the ASR renders "Sridhar Ramaswamy" variously as *"Sria Rama Swami / Sidar Ramaswami / Thriar"*, "Cortex Code/Coco" cleanly, "Neeva" as *"NEA"*, "McKinsey" as *"McKenzie"*). The transcript appears **doubled** (the intro repeats from ~0:00 a second time at the tail); the duplicate was disregarded at ingest. Transcript provenance (ASR) does not feed confidence per [§Lifecycle].
