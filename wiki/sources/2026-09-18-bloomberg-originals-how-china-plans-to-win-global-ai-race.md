---
type: source
kind: video
title: "How China Plans to Win the Global AI Race"
author: ["Bloomberg Originals"]
publisher: "Bloomberg Originals — short documentary accompanying the Bloomberg graphics piece 'US Lead in the AI Race With China Is Rapidly Narrowing'"
url: "https://www.youtube.com/watch?v=eVUYCiRLgB4"
date_published: 2026-09-18
date_ingested: 2026-09-19
length: "~11:54 minutes (transcript ~99 segments; creator-uploaded captions; nine YouTube chapters)"
raw: "../../raw/videos/how-china-plans-to-win-the-global-ai-race.md"
tags: [bloomberg, bloomberg-originals, china, us-china-ai-race, open-weight-models, deepseek, kimi-k3, moonshot, openrouter, token-share, price-performance, cost-per-task, polsia, model-switching, monetization, race-to-the-bottom, iphone-android, gpt-5-6-luna, price-cut, export-controls, distillation, developing-world, industrial-policy]
dynamic_capabilities:
  - contextual/external-triggers
  - digital-seizing/balancing-digital-portfolios
relationships:
  - type: supports
    target: 2026-07-10-hugging-face-ceo-companies-done-renting-their-ai
    via: "China's open-model lead measured two ways. Delangue cites Chinese models at about 41% of Hugging Face downloads in spring 2026; Bloomberg cites OpenRouter data showing global usage of Chinese models overtaking US models in June 2026, and more Chinese than US model use in Singapore, Germany and the US itself. Downloads and routed tokens are different quantities pointing the same way"
    confidence: 0.75
  - type: supports
    target: 2026-07-29-ng-washington-post-china-open-source-ai-competitiveness
    via: "price-sensitive markets defaulting to Chinese open models. Ng says DeepSeek adoption is 'through the roof' in Africa and that American under-investment in open models cedes those markets; Bloomberg calls the developing world 'a tremendous battleground' and adds the US version — hundreds of US startups lobbying against a ban because 'they're a lot cheaper'"
    confidence: 0.75
  - type: supports
    target: 2026-08-18-covello-gs-new-models-ai-investment-landscape
    via: "the cost-versus-capability split. Covello predicts no enterprise runs on frontier models alone, with open models taking everything but high-consequence queries; Bloomberg quotes 'you don't need God to write your emails' and shows a startup cutting its model bill roughly tenfold by moving routine agent work to Chinese open models"
    confidence: 0.7
  - type: supports
    target: 2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china
    via: "diffusion as the measure of success. Ognibeni argues China wins by deploying AI across industry rather than chasing AGI; Bloomberg closes on the same point — 'the effective use of AI across industry to drive up productivity may well turn out to be a more important indicator of a country's success'"
    confidence: 0.7
  - type: supports
    target: 2026-09-18-reuters-on-assignment-inside-chinas-ai-race
    via: "published the same day with the same conclusion: whether China is 'winning' depends on whether you measure the frontier, where both say the US leads, or adoption across the economy, where both say China's strategy is aimed"
    confidence: 0.75
---

# Bloomberg Originals — How China Plans to Win the Global AI Race

> China's low-cost, open-weight artificial intelligence models are rapidly gaining ground on US rivals such as OpenAI and Anthropic. In June, global usage of Chinese AI models surpassed US models for the first time, according to OpenRouter data.
>
> From DeepSeek to Kimi K3, Chinese AI companies are attracting users around the world, including in Silicon Valley, where hundreds of startup founders urged the Trump administration not to restrict access to Chinese AI models.
>
> The shift comes as concerns grow over the risks of advanced AI, with company CEOs including Dario Amodei of Anthropic and Sam Altman of OpenAI calling for stronger safeguards and slower development.

## TL;DR

A 12-minute Bloomberg Originals documentary, published 18 September 2026, made to accompany a Bloomberg graphics feature on the narrowing US lead. It is a produced explainer (narration, reporter and analyst interviews, one founder case) rather than an interview.

Its contributions to the wiki are **one usage figure, one cost comparison, one switching case and one price response**, all four new to the corpus:

1. **Usage:** per OpenRouter data (the routing platform whose token counts [[2026-06-11-kilpatrick-sequoia-model-eats-the-harness|Kilpatrick]] also reads as a market signal), global usage of Chinese models overtook US models **in June 2026**, and Singapore, Germany and the US each use more Chinese than US models.
2. **Cost per task:** Bloomberg's "coffee-shop website" test cost about **$50 with Claude Fable 5, $12 with Kimi K3**, and later **just over $4 with OpenAI's GPT-5.6 Luna**.
3. **A switching case:** a San Francisco agent-automation startup, **Polsia**, moved to Chinese open models when its Anthropic bill reached **$1–1.5 million a month**, bringing it to roughly **$100,000**.
4. **The response:** OpenAI launched **GPT-5.6 Luna** in July 2026 as its most cost-efficient model, and the founder reports a price cut of about **80%**, which brought frontier-lab pricing back into the range of the Chinese alternatives.

The fourth item matters most to [[open-source-ai]]. That page records that the migration to open models has three possible drivers (cost, data control, strategic autonomy), each reversed by a different event. This is the first case in the corpus where the **cost-reversal mechanism** is observed: a frontier lab cut its price and a switched customer started testing the frontier model again.

## Key claims

### 1. The ecosystem, and the moment it was noticed

China's landscape mirrors the US in structure: incumbents (Baidu, Alibaba, Tencent) and startups (Moonshot, DeepSeek, Zhipu, MiniMax), *"very aggressive in terms of how they're approaching the market."* Chinese firms had built models for years without traction; the perception that China was behind *"changed in early 2025"* with DeepSeek's reasoning model, made *"allegedly at a very low cost."* In 2026 Moonshot's **Kimi K3**, a 2.8-trillion-parameter model it claims competes with OpenAI's and Anthropic's best, *"made people realize actually the gap was even narrower."* The film's performance chart shows the gap narrowing through 2026 but does not close it.

### 2. Cost has become the axis of competition

*"Cost has become a very, very important factor in this AI race, and in that sense, China's offerings are a lot more attractive right now."* The line the film builds on: *"you don't need God to write your emails. So it comes down to really a balance between cost and capability."* Its example of work that does not need the frontier is AI-assisted customer service.

The coffee-shop test is the film's own experiment: the same small-business website built with each model. It is one task, run once, and it measures API price, not quality. It shows the price ordering, not a price-performance curve.

### 3. The switching case: what happens at scale

Polsia (as captioned) automates business workflows with agents. Its founder started on Anthropic *"even though the models were really expensive"*, because *"I need to give my customers the absolute best."* Then the platform went viral:

> *"At the beginning, you know, I had my bills were like 10,000 bucks a month, 20,000 bucks a month. But when that became a million dollars a month, $1.5 million a month, that's when I was like, 'I'm just going to go bankrupt straight up.' … when I switched to the open source models it became pretty much 10X less, so around $100,000 a month."*

This is the [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|own-vs-rent flow]] in its plainest form: the frontier API for launch, open models once volume makes cost the binding constraint. The film also reports a change in norms: using Chinese models was *"very hush-hush"* and *"now it's totally shifted"*, with hundreds of US startups rallying behind them when a ban was threatened.

### 4. Why Chinese AI is cheap, and the catch

Cheaper electricity and cheaper engineering talent help, *"but there's something else. Open weight models."* The film explains open weights with a cake analogy (a closed model is a slice eaten in the shop; an open-weight model you take home, customise and can resell) and credits openness with letting *"a lot of different eyes … look at the technology at the same time,"* giving China *"a better shot at really closing the gap."*

The disadvantage: *"Nobody has quite figured out how to make money."* Chinese providers have been in *"a race to the bottom for more than a year now,"* undercutting each other, and Chinese consumers *"are not willing to pay for AI services that much."* The analogy offered: *"Anthropic and OpenAI have built the iPhone. The Chinese companies are more like Android. iPhone makes by far the most money, but Android has the larger market share."*

### 5. Beijing's reasons

Affordability serves the state's goal of fast adoption *"within the economy"*. Abroad, *"the developing world is a tremendous battleground,"* and Chinese AI offers *"an alternative to sort of US big tech, which amid trade wars and tariffs, more countries … want options."* At home, AI is one of the new growth drivers replacing a faltering property sector, whose contribution to GDP growth has declined since 2018 while high-tech and green industries have risen, alongside adjacent bets such as humanoid robotics. A second analyst adds a standards motive: leading in AI would give China *"more say over the standards, over the rulemaking."*

### 6. The US position, and the price response

The film is explicit that the US still leads on the frontier (*"the biggest, smartest, baddest AI models out there"*), on compute and chip access, and on capital. Chinese firms' market valuations are *"a fraction of some of the top US players."* US export controls on chips and chipmaking equipment *"have definitely had an impact on slowing China's AI development,"* while US officials allege backdoor chip access and distillation, *"to basically shoplift their capabilities,"* and Washington has discussed banning Chinese open models.

Then the response: OpenAI's **GPT-5.6 Luna**, launched in July, built the coffee-shop site *"for just over $4, matching the pricing of budget-friendly Chinese alternatives."* The Polsia founder is testing it: *"The cost of Luna starts to be similar than open source. It decided to lower the price by 80%, which is a massive price drop. This open-source Chinese models, you know, showed that like there was an alternative."*

### 7. The framing the film ends on

Both governments reject slowing down: President Trump dismisses AI-risk fears as *"a hoax"*, and China calls US tech leaders' warnings *"AI fearmongering"*, so *"the race right now is tremendously competitive, and that's unlikely to stop just because some CEOs have said we must slow down."* The closing judgment: *"It's probably still too early to call whether China or the US will win the AI race, but China's AI development has demonstrated that the effective use of AI across industry to drive up productivity may well turn out to be a more important indicator of a country's success."*

## Neighbour sources

- [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|Delangue (Hugging Face)]] measured China's open-model lead by downloads; this film measures it by routed usage on OpenRouter. The two measures agree in direction, and neither is a census of enterprise inference.
- [[2026-07-29-ng-washington-post-china-open-source-ai-competitiveness|Ng]] warned that price-sensitive markets would default to Chinese open models. The film calls the developing world a battleground and shows the same behaviour among US startups.
- [[2026-08-18-covello-gs-new-models-ai-investment-landscape|Covello]] predicts a split in which frontier models handle high-consequence queries and open models the rest. *"You don't need God to write your emails"* is that split stated as a slogan, and Polsia is a firm acting on it.
- [[2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china|Ognibeni]] and the film end on the same judgment: diffusion across industry, not the frontier, may be the better measure of national AI success.
- [[2026-09-18-reuters-on-assignment-inside-chinas-ai-race|Reuters' On Assignment]], published the same day, reaches the same conclusion from correspondents in China and adds what this film lacks: how Chinese models are tested before release.

## What was actually ingested

The creator-uploaded English caption track, 99 segments across nine chapters, complete to 11:31 of 11:54. The captions are manual, so cleanup was limited to one correction (*"this stealing"* → *"distilling"*). Two items are left as captioned and unverified: *"China's OpenAI models"* at 4:37, which almost certainly means open AI models, and the Polsia founder's name. The interviewed reporters and analysts are not named in the captions, so their claims are attributed to the film. The performance and GDP charts are described in narration only.

## Dynamic-capabilities reading

- **`contextual/external-triggers`**: a disruptive change in model economics (a roughly tenfold price gap, falling fast), policy exposure in both directions (export controls, a possible US ban on Chinese open models), and a shift in norms that made Chinese models acceptable to US startups.
- **`digital-seizing/balancing-digital-portfolios`**: the Polsia case is the firm-level decision this cell names (balancing internal and external options, setting the speed of execution). A single-supplier frontier choice made at launch was rebalanced to open models when scale made cost binding, and is being rebalanced again as frontier prices fall. *"You don't need God to write your emails"* is the portfolio rule behind it: match capability to the task instead of buying the frontier for everything.

## Linked entities and concepts

- Entities: [[Anthropic]], [[OpenAI]]
- Concepts: [[open-source-ai]], [[foundation-models]], [[ai-sovereignty]]
- **Dangling** (single-source mention, deferred): Bloomberg Originals, Moonshot AI, Polsia.

## Scope and reliability

**The numbers are single observations.** The coffee-shop test is one task run once per model and prices a single job. The Polsia figures are one founder's recollection. The OpenRouter figures come from a routing platform whose users are developers who already choose models on price, so the platform over-represents cost-sensitive traffic. None of these is a measure of enterprise inference overall, which [[open-source-ai]] still lacks.

**Model names are as reported.** The film names Anthropic's Claude Fable 5, Moonshot's Kimi K3 and OpenAI's GPT-5.6 Luna; the wiki has no independent source on Kimi K3's parameter count or on Luna's launch pricing.

**Produced journalism, not advocacy.** Bloomberg has no stake in the open-versus-closed question, and the film gives the US case (frontier lead, compute, capital, the Luna price response) as much time as the Chinese one.
