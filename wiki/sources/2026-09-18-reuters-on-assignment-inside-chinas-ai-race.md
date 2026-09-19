---
type: source
kind: video
title: "Inside China's AI race | On Assignment"
author: ["Reuters"]
publisher: "Reuters — On Assignment podcast episode; correspondents Eduardo Baptista and Laurie Chen interviewed by the show's host"
url: "https://www.youtube.com/watch?v=brm1SWV27CE"
date_published: 2026-09-18
date_ingested: 2026-09-19
length: "~22:26 minutes (transcript ~171 segments; auto-generated captions, ASR-cleaned; ~21 min conversation + credits)"
raw: "../../raw/videos/inside-chinas-ai-race-on-assignment.md"
tags: [reuters, on-assignment, eduardo-baptista, laurie-chen, china, us-china-ai-race, ai-diffusion, agi, distillation, export-controls, cyberspace-administration-of-china, pre-release-testing, ai-safety, energy, data-centres, trump-xi-summit, global-south, ai-governance, journalism]
dynamic_capabilities:
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china
    via: "the same two-race reading from two unrelated vantages. Ognibeni, an e-commerce practitioner, says the West chases AGI while China pursues diffusion that already earns revenue; Chen, a Reuters China correspondent, says the US is 'very focused on trying to reach AGI' while Beijing pushes AI 'throughout various different sectors of the economy' to lift productivity against a demographic decline"
    confidence: 0.8
  - type: supports
    target: 2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity
    via: "export controls as the cause of China's strategy rather than ideology. Frey says chip controls forced China into an open-weight, efficiency-first path; Baptista says China 'can't really access even a fraction of the most advanced compute' even with unlimited money, which is why distillation is something it will 'keep relying on in the coming years'"
    confidence: 0.75
  - type: supports
    target: 2026-07-29-ng-washington-post-china-open-source-ai-competitiveness
    via: "both decline to treat distillation as the explanation for China's catch-up. Ng calls the claim 'vastly overstated'; Chen says the share is 'very hard to determine' and gives a counter-example — US companies distil too, Meta spends millions on Anthropic tokens a month, and its model has not caught up. The Reuters account is more cautious than Ng's: it confirms the practice is widespread"
    confidence: 0.7
  - type: supports
    target: 2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai
    via: "state-administered model governance in China. Sundararajan describes top-down algorithmic governance enforced 'through administrative directives'; Chen describes the mechanism — pre-release testing coordinated by the Cyberspace Administration of China, with further technical-safety benchmarks from the industry and science ministries — and adds that independent in-lab safety testing is thin"
    confidence: 0.7
---

# Reuters *On Assignment* — Inside China's AI race

> As the US and China race to dominate artificial intelligence, Reuters correspondents Eduardo Baptista and Laurie Chen say the two countries aren't even playing the same game. On this episode of On Assignment, they take us inside China's AI industry - from Beijing's push to weave AI into every corner of society, to the murky world of chip access, distillation and export controls. Hear what it takes to report on one of the most fast-moving industries on Earth, and why the answer to "who's winning" may depend entirely on how you define the race.

## TL;DR

A ~21-minute episode of Reuters's *On Assignment* podcast, published 18 September 2026, in which the show's host interviews two Reuters journalists based in China: **Eduardo Baptista**, chief technology correspondent for Greater China, and **Laurie Chen**, a China correspondent who moved to the AI beat earlier in 2026 from politics, diplomacy and security.

Its value to the wiki is its **vantage**. The corpus's China material so far comes from a Western practitioner ([[2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china|Ognibeni]]), open-model advocates ([[2026-07-29-ng-washington-post-china-open-source-ai-competitiveness|Ng]], [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|Delangue]]), an academic economist ([[2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity|Frey]]), and a WEF episode **co-produced with the Chinese state broadcaster CGTN** ([[2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai|Sundararajan]]). This is the first account from wire-service reporters working inside China, and the only one in the corpus that describes **how Chinese models are tested before release**.

## Key claims

### 1. Two races, not one

Chen's thesis, and the episode's frame: *"I think that the US and China are running two very different races. The US is very focused on trying to reach AGI and dominate the frontier of AI. Whereas the Chinese government … they're very focused on pushing **AI diffusion** throughout society."* Diffusion means adoption *"throughout various different sectors of the economy and even things like education, healthcare, government services"*, including enterprise agents *"integrated into pre-existing infrastructure"*.

The stated aim is macroeconomic: that AI *"will eventually increase China's economic productivity and sort of enable it to overcome like a demographic crisis"* and move up the global value chain. Chen contrasts rural America, where *"you don't really see like everyone using or adopting AI to the same extent."* Baptista's version: China is *"probably the best place in the world to see where AI is actually changing people's lives on the ground."*

Chen adds that Chinese state media and officials **reject the race framing itself**, reading US calls for a frontier slowdown as *"an attempt to constrain China's AI development"*, a political weapon.

### 2. Distillation is widespread, forced by compute scarcity, and its contribution cannot be measured

The episode gives both halves of the argument, which is why it is useful here.

- **The practice is real and structural.** Chen: *"from what we understand it's pretty widespread."* Baptista explains why: China, *"even if it had all the money in the world, it can't really access even a fraction of the most advanced compute that US AI giants can procure"*, so distillation from frontier systems such as Claude Fable 5 or OpenAI's GPT models *"is something that the Chinese are going to keep relying on in the coming years."*
- **Its share of China's progress is unknown.** Chen: *"It's very hard to determine the exact proportion … US companies also distill … Meta spends millions of Anthropic tokens every month but their model has not really caught up to the frontier."* The White House and National Security Council treat distillation as a main reason Chinese models caught up; the Chinese embassy in Washington calls the allegations baseless.
- **It is hard to report.** Researchers in Chinese labs are reluctant to discuss distillation *"because obviously it's not really something they want to draw attention to."*

### 3. How Chinese models are tested before release

This is the claim the corpus had no other source for. Chen: *"China does have already … a very extensive pre-release testing system in place that's coordinated by … the **Cyberspace Administration of China**."* The CAC supplies internal benchmarks covering *"political speech or censorship … child safety safeguards"*; the industry ministry and the Ministry of Science and Technology add *"more sort of technical safety assessment benchmarks that the models will have to pass first before their release."*

What is missing is the part US labs do themselves: *"there's not really a lot of independent testing by the Chinese AI labs … unlike in the US where you know Anthropic and OpenAI have … huge amounts of compute and a ton of resources to dedicate to in-house safety testing."* Chinese policy analysts are pushing for in-house testing for catastrophic, cyber, biological, chemical and nuclear risk *"in line with American standards."*

Baptista's reading of the regulatory stance: any technology *"as long as it's properly managed and the state can intervene whenever they want … can be brought under control"*, which he offers as one reason for the absence of *"existential kind of panic"* in Chinese public debate, alongside the less open public conversation.

### 4. Safety debate exists, and a bilateral track is forming

Baptista says the risk debate inside China's policymaking system is real but *"not as loud or perhaps free flowing as in the states."* Experts on both sides are calling for *"nuclear weapons-style safeguards"* so that competition does not produce *"an accidental world war"*: AI-driven nuclear escalation or an accidental missile strike. Ahead of a Trump–Xi summit, Treasury Secretary Scott Bessent was due to meet Vice Premier He Lifeng. Chen expects AI safety on the agenda, *"especially … managing frontier AI risks"* and monitoring AI-linked cyber attacks, while noting the Trump administration has *"pushed back against … Dario Amodei's calls to pace the frontier."*

### 5. Energy is not a clean Chinese advantage

Against the common US framing that China offsets weaker chips with cheap power, Baptista is *"a bit more nuanced"*: the US *"can actually generate power more cheaply than China"* in some places, and it depends on the region (*"Are you comparing Texas to Inner Mongolia or Texas to Fujian"*). The advantage he concedes is **state capacity**: if China can use *"its state-led economic model to push for a huge expansion of electricity generation capacity"* for new data centres, *"that could definitely help."*

### 6. The correspondents' own risk ranking

Asked where they sit between doomer and optimist:

- **Baptista** expects guardrails to be built, as nuclear war has been averted *"for now 80 years"*, and ranks the nearer risks higher: *"job disruption and people relying too much on AI in a way that numbs critical thinking"* and makes social interaction less common. He points to Chen's reporting on AI in the Chinese education system.
- **Chen** disagrees with *"a lot of the calls … for AI doomsday … coming from the US"* and makes a governance point: *"the vast majority of the world does not have the capacity to control advanced AI"*, so *"a very small number of countries and very powerful corporations"* are deciding how AI is governed. Other countries, especially in the Global South, *"should have a say"*, and capacity building should share the productivity dividend more widely.

## Neighbour sources

- [[2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china|Ognibeni (May 2026)]] made the AGI-versus-diffusion distinction from a Western e-commerce practitioner's vantage; Chen makes it from inside China, four months later, about state policy rather than company behaviour. They are independent routes to the same claim.
- [[2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity|Frey]] reads China's open-weight path as a consequence of chip export controls. Baptista gives the same cause for continued reliance on distillation. The episode does not discuss open weights directly.
- On distillation, [[2026-07-29-ng-washington-post-china-open-source-ai-competitiveness|Ng]] calls its role *"vastly overstated"*. Chen agrees the share is undetermined and uses a similar "everyone does it" argument, but unlike Ng she confirms the practice is widespread in China.
- [[2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai|Sundararajan]] describes Chinese AI governance as administrative and top-down. This episode supplies the mechanism (CAC-coordinated pre-release testing) from a source with no Chinese state co-producer, which partly closes the gap [[ai-sovereignty]] had recorded.
- Published the same day: [[2026-09-18-bloomberg-originals-how-china-plans-to-win-global-ai-race|Bloomberg Originals' film]] reaches the same conclusion, that who is "winning" depends on whether you measure the frontier or diffusion.

## What was actually ingested

The full auto-generated transcript, 171 segments, from the episode's opening through the production credits. ASR cleanup covered the correspondent's name (captioned as Lorie, Lori and Larry), Jensen Huang, Dario Amodei, Scott Bessent, He Lifeng, the Cyberspace Administration of China and Fujian; `[music]` tags were removed. The host's name is captioned *"Kim Vanell"* and has not been verified, so the page refers to "the host". The *"Read the story here"* link in the description is empty.

## Dynamic-capabilities reading

- **`contextual/external-triggers`**: the episode is about the external conditions firms operating in or with China face. It covers export controls on chips that shape which models exist, US allegations and possible bans that make Chinese-model dependence a political exposure, a state diffusion programme that pushes AI into every sector, and a bilateral safety track that could change the rules. No firm-level microfoundation is discussed, so no other cell is tagged.

## Linked entities and concepts

- Entities: [[Anthropic]], [[OpenAI]]
- Concepts: [[ai-sovereignty]], [[open-source-ai]], [[responsible-ai]]
- **Dangling** (single-source mention, deferred): Reuters, Eduardo Baptista, Laurie Chen.

## Scope and reliability

**Journalists describing their beat, not a report.** No figures are given for the diffusion programme, the testing regime or distillation, and the pre-release-testing account names the institutions and benchmark categories without describing pass criteria or enforcement. It is the most specific description of Chinese model governance in the corpus, but still a description.

**Reuters has no stake in either side of the open-versus-closed or US-versus-China question**, which is the reason to weight it above the CGTN-co-produced account on the governance mechanics. The correspondents' own risk views (claim 6) are opinions and are recorded as such.

**Timing.** The episode refers to *"the past few weeks"* of apocalyptic AI rhetoric and to Dario Amodei's essay calling for external oversight, and it precedes the Trump–Xi summit it previews. What was agreed there is not known to the wiki.
