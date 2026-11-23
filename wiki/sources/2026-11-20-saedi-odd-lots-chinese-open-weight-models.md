---
type: source
kind: video
title: "How an American AI Company Uses Chinese Open-Weight Models | Odd Lots"
author: ["Bloomberg Podcasts"]
publisher: "Bloomberg Podcasts (YouTube channel), Odd Lots; hosts Joe Weisenthal and Tracy Alloway; guest Daniel Saedi, co-founder of Minerva (AI agents for marketing), formerly at Bridgewater"
url: "https://www.youtube.com/watch?v=nKOs2G5QdS8"
date_published: 2026-11-20
date_ingested: 2026-11-23
length: "~49:11 minutes (transcript ~420 lines; human-written track, 13 chapters)"
raw: "../../raw/videos/how-an-american-ai-company-uses-chinese-open-weight-models-odd-lots.md"
tags: [bloomberg, odd-lots, joe-weisenthal, tracy-alloway, daniel-saedi, minerva, open-weight-models, open-source-ai, chinese-ai-models, deepseek, qwen, kimi, fine-tuning, post-training, cost-per-task, model-routing, ai-sovereignty, abliteration, distillation, ai-benchmarks, training-data, rl-environments, harvey, fireworks-ai, reflection-ai, compute-shortage, gpu-rental-prices, ai-native-company, marketing-ai, podcast, news-politics]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - strategic-renewal/business-model
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai
    via: "both describe application companies post-training open-weight models on their own data for particular tasks, and both name Harvey: Huang frames it as owning intelligence per capability, with cost first of four drivers; Saedi describes Minerva's fine-tuned Qwen for audience queries and ranks cost, then sovereignty, then competition"
    confidence: 0.75
  - type: supports
    target: 2026-07-10-hugging-face-ceo-companies-done-renting-their-ai
    via: "both describe frontier APIs used first and open models taking over repeatable production work on cost: Delangue as a flow he sees across enterprises, Saedi as Minerva's own split between building with frontier models and serving fine-tuned open weights"
    confidence: 0.7
  - type: supports
    target: 2026-10-05-chase-langchain-interrupt-nyc-opening-keynote
    via: "both name Harvey's fine-tuned models and the post-training of open-weight models on hosted services such as Fireworks AI: Chase as a harness vendor launching a fine-tuning route, Saedi as a Fireworks customer quoting what fine-tuning costs"
    confidence: 0.7
  - type: supports
    target: 2026-10-20-hamalainen-lala-takkar-mckinsey-economics-of-enterprise-ai
    via: "both say model choice should be judged per task rather than per million tokens, Hämäläinen from enterprise AI spend reviews and Saedi from an application company's margin on each completed marketing task"
    confidence: 0.7
  - type: supports
    target: 2026-09-18-bloomberg-originals-how-china-plans-to-win-global-ai-race
    via: "both concern US companies using Chinese open-weight models on cost: Bloomberg Originals reports OpenRouter usage, a per-task price comparison and a startup's switch; on Odd Lots a host says large US companies name Qwen in private but not in public, and Saedi describes Minerva's fine-tuned Qwen"
    confidence: 0.7
  - type: supports
    target: 2026-09-18-reuters-on-assignment-inside-chinas-ai-race
    via: "both treat distillation by Chinese labs as real and its share of their progress as unsettled: Reuters' correspondents call it widespread and its contribution very hard to determine; Saedi uses Reflection AI's US open-weight model, trailing the Chinese ones, as a rough gauge"
    confidence: 0.65
  - type: supports
    target: 2026-09-30-chow-metalware-ai-firmware-vulnerability-research
    via: "both concern open-weight models with near-frontier offensive cyber capability whose safeguards are removed by abliteration: Chow relays an Anthropic report on GLM-5.3; Saedi describes an abliterated DeepSeek model at about $0.30 per million tokens and an online theory that swarms of such models run current hacks"
    confidence: 0.65
  - type: supports
    target: 2026-11-10-ai100-ai-goes-mainstream-2026
    via: "both state the gap between open-weight and frontier models in months: the AI100 report gives three to six months; Saedi puts the Chinese open-weight models about three months behind the public frontier and Reflection AI's US model three to six months behind them"
    confidence: 0.6
  - type: supports
    target: 2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free
    via: "both describe an application company running open-weight models beside OpenAI and Anthropic models, chosen task by task, to lower cost: Fireflies passes the savings to its free tier; Minerva keeps them as margin and fine-tunes for speed"
    confidence: 0.65
---

# Saedi (Bloomberg Odd Lots) — how a US AI-native company uses Chinese open-weight models

> This week, we got news that the Trump administration is reportedly considering a requirement for US companies to publicly disclose their use of Chinese AI models. Any effort to discourage US businesses from using Chinese open-source could be a big deal for both the AI industry and the market, where investors are still debating whether customers will ultimately be willing to pay for pricier homegrown frontier models versus cheaper alternatives. Everyone remembers last year's 'DeepSeek moment' for AI, when a Chinese company released a cheaper model that seemed nearly as good as cutting-edge US ones. So why do businesses actually use open-source? In this episode, we talk to Daniel Saedi, co-founder of Minerva, to better understand how an AI native company chooses its models. He breaks down how exactly his company mixes and matches models for specific use cases, the risk of obliterated models, and the issue of data sovereignty.
>
> *— Channel description, Bloomberg Podcasts*

## TL;DR

A 49-minute episode of Bloomberg's *Odd Lots*, published 20 November 2026 and, by a host's remark, recorded on 3 November. **Joe Weisenthal** and **Tracy Alloway** interview **Daniel Saedi**, co-founder of **Minerva**, a startup founded in 2023 that builds AI agents for marketing teams, from campaign planning to execution. Before Minerva he spent about five and a half years at Bridgewater. The hosts' question: how much value a company building on AI gets from cheaper Chinese open-weight models, and when the frontier premium is worth paying.

What it adds to the wiki:

1. **A buyer's model mix, stated as an operating rule.** Frontier models while building the product (the hosts call it the CapEx side), open-weight models for repeatable tasks in production (the OpEx side), judged by *"cost per completed task"* rather than price per million tokens.
2. **A worked fine-tune.** Minerva fine-tuned Qwen on *"a few thousand"* graded examples of natural-language audience queries turned into SQL, and reports a model faster than the closed ones *"for our use case"* and better at the task.
3. **The benefits of open weights, ranked by a user:** cost first, sovereignty and control second, bargaining power against the labs third.
4. **Costs the corpus did not have:** the durability problem (a fine-tune does not carry over to the next release), fine-tuning prices at Fireworks AI, Harvey's reported $6 million in compute for its legal model, and what a data broker pays for a company's data.
5. **An abliterated DeepSeek model** at about $0.30 per million tokens, *"1/100 of the cost"* of Anthropic's Fable, and the guest's view that this, not data leaking to China, is the risk of open weights.
6. **A distillation gauge and a compute heuristic.** Reflection AI's US open-weight model trailing the Chinese ones, and *"about a GPU's worth of token consumption per year"* per AI-native knowledge worker.

One founder's account of his own company, plus hosts' commentary. No figures are shown on screen; the stills review found only talking heads (see *Source quality*). The news hook in the description, a reported US plan to make companies disclose their use of Chinese models, is not discussed in the conversation, which was recorded 17 days before publication.

## Framing: will frontier intelligence be commodified? (0:00–5:04)

The cold open replays the guest's compute heuristic from 40:06 (see *Token budgets and compute* below). The hosts then set the question. Since *"the DeepSeek scare, back in January 2025,"* the open question for [[Anthropic]] and [[OpenAI]] is *"will frontier or near frontier intelligence be commodified,"* which would stop them charging the premium that justifies their CapEx. Chinese open models *"seem to be getting pretty close to the frontier on some of their benchmark exercises,"* and the hosts list the standard objections: that they distil Western models, that they are tuned to benchmarks, that they are six months to a year behind, and that they may have been trained on Nvidia chips abroad. For a startup the interest is plain: *"you like price competition, you like downward price pressure."*

Saedi worked at Bridgewater for about five and a half years, first raising money for Pure Alpha, then overseeing trading in banks, REITs and insurers. Minerva is *"an AI company focused on marketing"* that builds agents *"to automate everything from pre campaign planning all the way down to execution,"* and uses *"both open source and closed source models in that process."*

## Frontier to build, open weights to run (5:04–8:06)

While building the product Minerva uses the frontier, because *"you honestly don't want your developers to be spending time dealing with loops and with mistakes."* The captions name the models as *"cloud"* (read here as Claude) and *"Astra"*. Astra is probably OpenAI's GPT-6 Astra: Saedi later cites an *"Astra 6.2"* benchmark score, and the workbench slide on [[2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations|Falkor's NVIDIA Omniverse stream]] names a task runner on Codex *gpt-6.2-astra*. Once a task is repeatable, the economics change:

> *"You get into a different set of economics where you care about cost per completed task, which is a lot different than … cost per million tokens, it's purely an input output thing … How do I make sure that I get the minimum acceptable task completion for the lowest amount of costs? Because everything outside of that is our margin."*

The same distinction between cost per task and cost per token is drawn in [[2026-10-20-hamalainen-lala-takkar-mckinsey-economics-of-enterprise-ai|McKinsey's Explainer on the economics of enterprise AI]] (*"it's not just about cost per token, it's really about cost per task"*), from enterprise spend reviews rather than one product's margin. [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|Clem Delangue (Hugging Face)]] describes the same sequence across enterprises: frontier APIs to experiment and launch, then open models *"when they really hit production and they hit scale."*

This is the `digital-seizing/balancing-digital-portfolios` cell of the W&W model ([[dynamic-capabilities]]) at the level of a single product: per task, Minerva balances an external option (renting a frontier API) against an internal one (owning a fine-tuned open-weight model), and revisits the choice as costs move.

## Open source is not open weight (8:06–9:05)

Saedi separates the two terms, which he says *"are really used synonymously right now"*. Open source means *"disclosing all of the code, all of the data, the exact recipe that was used to train a model. And that's not what the Chinese labs are doing."* They release the weights, *"essentially the end artifact,"* which can be downloaded and self-hosted, unlike an API where *"I send in data … I get data back. I have no idea how I got the data there."* Even with the weights, *"other than the papers they release, I have no idea how they actually went from … data in an architecture to an actual artifact."* This is the middle tier of the closed / open-weight / open-source spectrum on [[open-source-ai]], and his last point returns as the durability problem below.

## Fine-tuning as the application layer's advantage (9:05–12:37)

Weisenthal says he is *"personally still unclear whether fine tuning for local data is actually going to be economically valuable."* Saedi: *"this is the primary benefit to the application layer right now."* Startups lack *"these like billions of dollars of data that the labs have,"* so they *"have to get crafty"*: Minerva's customers let it train on their data, and fine-tuning turns *"a model that's trained to be generalized"* into one *"specialized in a very specific task."*

His example is building an audience from a request such as *"find everyone who works at OpenAI and likes football."* Minerva used to have an OpenAI model interpret the request, turn it into SQL and query the database; it was slow and needed *"a very expensive model."* Qwen out of the box did *"roughly as good as the OpenAI model,"* but below the top closed models. So:

> *"We have a few thousand of these labeled examples where you have a very complicated query, and then you have a very, you know, right result. You grade those and then you fine tune the model … And now we have a model that's faster than the closed source models for our use case [and] is better."*

He calls the result *"a very small advantage."* Larger application companies do the same with their distribution data; he names Harvey and Cognition as fine-tuning Kimi (the captions run the two together, so which company tuned which model is unclear). The result is *"better results at cheaper costs,"* an advantage *"that you can start to charge a margin for. And that's really the benefit of the open weight models for American companies."*

[[2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai|Sonya Huang's Sequoia keynote]] argues the same move from the investor side, as owning intelligence per capability, and names Harvey among the application companies publishing post-training research. [[2026-10-05-chase-langchain-interrupt-nyc-opening-keynote|Harrison Chase at Interrupt NYC]] cites Harvey's *"fine-tuned models for specialized tasks"* and launches a route from agent traces to a model post-trained on Fireworks AI or Baseten. [[2026-10-15-lin-stanford-ai-club-building-in-the-ai-era|Alfred Lin (Sequoia)]] says Harvey started on frontier models and now trains its own.

## Three benefits, ranked (12:37–15:17)

Alloway asks him to order the benefits.

1. **Cost.** *"I have to pay some upfront costs and then some operating costs. And is that cheaper than paying OpenAI and Anthropic? And in many cases it's true. In some cases it's not true."*
2. **Sovereignty and control.** *"You see Karp and Satya talking a lot about this,"* and he expects it to be *"a huge issue in '27 as companies realize they're sending their data out to Anthropic and OpenAI, and they're not getting anything in return."* When a host notes that the labs say they do not train on corporate client data, he agrees: *"I don't want to be on this podcast saying there's any guidance that's been violated."* His point is different: *"The model doesn't get any better based on your use case,"* whereas with your own weights *"maybe I should be training it on my data as well so that it gets better."* See [[ai-sovereignty]].
3. **Competition.** A homegrown model lets a company tell Anthropic and OpenAI *"you have to now engage in value based pricing for me,"* because the choice is no longer between automation and none. *"It gives the leverage back to the smaller companies in a way that we didn't have in the early part of the AI boom."*

## Fine-tunes do not carry over (15:17–16:37)

Alloway asks how durable a fine-tune is. Saedi calls it *"the biggest decision point right now for founders"* and part of the operating cost: *"It doesn't simply transfer over. I can't … say, okay, listen, I fine tuned Kimi 3, Kimi 3.1 weights are coming out this week. Actually let me just transfer it over."* The graded data set does carry over, but *"I have no idea how they actually got to those weights. So whether or not it's going to converge to an optimal set of weights with the same training data set, I don't know."* He says this uncertainty belongs in the build-or-rent calculation, and describes himself as *"much more of an applied than … an AI researcher."*

## The economics of hosting, and the price of data (16:37–24:48)

**Hosting is now a service.** A year earlier, after the DeepSeek paper, a startup that wanted to fine-tune and host its own model needed enough concurrent GPUs and serving software (*"Sgt Lang or BLM"* in the captions, presumably SGLang or vLLM), so *"you actually would need a team of inference engineers."* That is why only research groups and *"large companies like Uber"* tried, *"even though Llama has been open source for two years."* Now companies such as Fireworks (which Minerva uses), Thinking Machines and Modal take a training set and return a fine-tuned model. Fireworks charges *"around 7 to $9 per million input and million output tokens"* for fine-tuning, and *"there are people out there who have fine tuned models that perform really well for as low as $90 on their final training run."* Weisenthal says he has fine-tuned BERT on Modal himself, with no technical background.

**Comparable costs**, as Saedi has heard them (he declines to give Minerva's own): Harvey *"spent about $6 million in compute to get to the absolute frontier of legal tasks"* with its fine-tuned model. Set against what the new Fable model costs (the captioned sentence is garbled), *"we're off by, you know, 2 or 3 orders of magnitude."* He puts Fireworks and Modal *"both … at $1 billion"* in annual revenue (captioned *"error"*; read as ARR).

**The data is the scarce part.** *"What actually separates a good fine tune from a bad fine tune is the data and the actual evals,"* which is why the labs pay data companies billions: *"the alpha … is in the data right now."* Marketing has plenty: call logs, ads and the creative process behind them, website activity. It can be built into *"what the market is now calling an RL environment,"* a simulation of the task: *"I show an ad to an AI, does it actually get the AI to click on the link to go to the website to actually buy the thing?"* Construction is the counter-example: a firm has the blueprints, but not the comments between architect, contractor and client that led to each change, and the model needs those: *"your teachers used to tell you, I don't care if you got the right answer. I need you to show your work."* As a price signal he cites the data company micro1, which he says paid *"anywhere from 250 to 500K per complete data set from a company"* and *"50 to $100,000 just for referring the companies."*

These figures bear on the `strategic-renewal/business-model` question for any firm with operational data: such data now has a price outside the firm, and a fine-tune is only as good as the graded data behind it.

## Abliterated models (24:48–28:13)

Alloway raises cybersecurity. Saedi, preparing for the episode, tried *"the newest DeepSeek model, and [its] uncensored form"*: *"what somebody did to the DeepSeek model that was released is they turned off the neurons that tell the model to say no."* The show calls it an *"obliterated"* model; the technique is usually spelled *abliteration*.

> *"The model is probably not as capable as Mythos back in February of this year, but it's up there and it's really cheap to run. It's about $0.30 per million [tokens] blended … about ten [times] cheaper than Sonnet, which is about ten [times] cheaper than Fable. So it's … 1/100 of the cost."*

*"The theory on the internet is people are running swarms of these DeepSeek obliterated models"* in current hacks. He separates this from the data worry: *"there's actually like no risk to the Chinese getting your data from this."* The risk is that *"I can just turn off a few parameters in this model"* and have *"a thousand of these Mr. Robots now running in the cloud, and I can tell them to hack anything."* On policy he has no answer, floats *"you have to KYC before you can download the weights,"* and wants a middle ground that preserves *"the dynamism of the U.S. startup community"* so companies like his can still download and fine-tune. Weisenthal calls them *"weapons when used for offensive hacking purposes."* Saedi agrees, has *"yet to see like a really compelling proposal,"* and adds that he still wants to be able to download the weights.

[[2026-09-30-chow-metalware-ai-firmware-vulnerability-research|Chow (Metalware)]] relays an Anthropic report that an open-weight model, GLM-5.3, has Mythos-level cyber results, with its safeguards bypassed in 64–100% of tests, abliteration among the methods. [[2026-10-21-lewis-nadeau-mckinsey-strategy-room-frontier-ai-cybersecurity|Lewis (McKinsey)]] expects open-weight models to *"start catching up"* on offence. On [[2026-11-14-tan-ugarte-yc-lightcone-rise-of-ai-coworkers|YC's Lightcone]] a host worries about abliterated models that *"won't refuse."* For defenders this is a `contextual/external-triggers` change: cheap, near-frontier offensive capability outside any lab's control. See [[attack-surface-management]].

## Distillation (28:13–32:21)

Weisenthal asks how far the open models are *"subsidized"* by distillation, that is, by terms-of-service violations against the US labs, and suggests that is why Llama *"didn't go anywhere"*: an American company *"is not going to go around violating the terms of service of Anthropic and OpenAI."* Saedi offers a gauge. Reflection AI, *"allegedly … being bought by Nvidia"* and *"probably the preeminent US open weight model company,"* trained its flagship on *"a cluster of 12 or 14,000"* Blackwell GPUs and released it about a month before the recording. It was *"about 3 to 6 months behind the Chinese open source models, which were about, at the time, three months behind the publicly released frontier,"* so *"6 to 9 months behind the frontier."* His inference: *"distillation is not the pure reason that the Chinese labs are where they are."*

Weisenthal asks how that is evidence, since an Nvidia-owned US company would *"really play it by the book with regards to distillation."* Saedi's answer: if the Chinese labs played by the book, *"they would probably be neck and neck with Reflection, if not maybe a little bit further ahead because they have the backing of the Chinese state."* *"Distillation is real … How much distillation is responsible for the quality of these models, I think is really up for debate."* He credits Chinese research: prolific publishing, sparse rather than dense models, and DeepSeek publishing *"their entire inference framework a few weeks ago,"* which Fireworks and Modal use: *"These guys are doing a public service."* He grants *"big allegations"* over the similarity between Kimi and *"Astra"*, and concludes: *"I wouldn't say we're subsidized by distillation."*

[[2026-09-18-reuters-on-assignment-inside-chinas-ai-race|Reuters' On Assignment]] holds the same open question from China: distillation is *"pretty widespread"* and its contribution *"very hard to determine."* The [[2026-11-10-ai100-ai-goes-mainstream-2026|AI100 2026 report]] puts open-weight models *"three to six months behind"* the frontier; Saedi's figures are the same order. His gauge rests on one US model released a month earlier, and the transcript does not show how he measured either gap.

## What "catching up" would mean (32:21–34:23)

Alloway asks what the next DeepSeek moment would look like, since benchmarks *"can be gamed."* Saedi: *"it's really hard for me even to tell the difference between a 5.1 and a five. And therefore, how am I supposed to be able to tell the difference between a five and a Kimi 3.1?"* As companies care more about their own tasks than about benchmarks, *"the benchmarks are starting to become meaningless … if I see that Kimi 3.2 has a higher Terminal Bench score than Astra 6.2, what does that actually mean to me? Does it mean anything? Probably not."* His test is substitution: *"if I can take Kimi 3.2 and start replacing it as my daily driver … Am I, you know, yelling expletives into the terminal anymore?"* See [[ai-benchmarks]].

## Pricing models and margins (34:23–37:12)

Weisenthal's summary: *"frontier closed source for CapEx building and … cheap open source for [OpEx] intelligence"* (the captions say *CapEx* twice; the chapter title says OpEx), with the hope of selling at a recurring price *"while the token price collapses 90% year after year"* and keeping the margin. Saedi: the first question is *"what am I charging my customer?"* His example is two legal-AI companies: Harvey charges a fixed price per seat, and a rival (captioned *"Lagos"*) charges by usage and is now also exploring fine-tuning. Harvey moved first, which he explains: *"when you have a fixed revenue coming in and a variable cost, you want to reduce that variable cost as much as you can."* Its fine-tuned model serves either to answer users or *"to get better leverage from the labs,"* and either way *"it's coming from a place of I need to increase my operating margins."* Minerva asks the same of its own product: where are *"the highest kind of variable components of [spend] within our product that aren't tied to usage,"* and can a fine-tuned or plain open model replace them. His break-even: per-token cost paid to the labs times the number of tasks must exceed the up-front cost of training plus the monthly cost of running the model.

This is the `strategic-renewal/business-model` cell: the revenue model (per seat or per use) decides whether falling inference costs become margin, and so whether owning a model is worth it.

## Token budgets and compute (37:12–42:09)

Minerva's token budget has gone up, *"mainly because we've just gotten more money."* Founded in 2023 and cautious about AI then, the team moved to agentic coding *"when Opus 4.5 came out in October of last year,"* but is *"not spending like ten, 15, $20,000 per engineer … We're not token [maxxing] … we are output max or outcome max or something."*

Weisenthal notes that GPU rental prices have not fallen during the AI-trade volatility: the Silicon Data H100 rental index is *"still going up."* Saedi says Minerva needs little compute to fine-tune and finds it *"always there"*; it was tight two years ago, when H100s were *"just unavailable."* His long-run view is the heuristic from the cold open:

> *"A fully kind of like AI native employee should have about a GPU's worth of token consumption per year … somewhere between 5 to 10 million right now in the US, of Blackwells. And how many knowledge workers are there? There's, you know, by some measures, around 100 million … if you think that every knowledge worker needs a GPU to actually fully automate all of their tasks and have an agent running at all times, then we're massively short of that need in the future."*

Four years out he expects *"one [B300] worth of computational capacity for every knowledge working employee."* His last data point is gossip, flagged as *"allegedly"*: at a White House medal ceremony Greg Brockman asked Elon Musk for compute, which would show *"the labs are still fundamentally short compute relative to their needs."* See [[foundation-models]].

## The hosts' coda (42:09–49:11)

After Saedi leaves, the hosts draw out the points:
- **What counts as cheap depends on whose time is spent.** If engineers' time is scarce, a lagging model is not cheap; for a repeatable harness that, say, A/B-tests two images on Instagram, *"why do you need the frontier intelligence?"* The open question is whether AI use ends up *"more like CapEx or OpEx."* One host would *"place my bets on the cheaper models winning out"*; the other notes the closed labs have cheaper models too.
- **Private use, public posture.** Asked privately what models they use, people at large US companies *"[will] talk about like [Qwen] … but not in public."* Conversely, some firms signal to Anthropic and OpenAI that *"we don't need you"*; Coinbase's Brian Armstrong is cited as having named a Chinese model his company uses. Still, *"a lot of companies are paying an Ant[hropic] tax or an OpenAI tax."* [[2026-09-18-bloomberg-originals-how-china-plans-to-win-global-ai-race|Bloomberg Originals]] measured the same shift in use: on OpenRouter, Chinese models overtook US models in June 2026.
- **Abliterated models and the information firewall.** Weisenthal: information such as how to build a bomb has become *"almost impossible to find on the internet,"* but *"in theory, that all exists in obliterated models,"* which *"aren't easy to come by"* yet; the firewall *"maybe, perhaps won't hold that long."*
- **Models editing models.** He mentions an MIT researcher's report in which a frontier model (*"after six"* in the captions) was given Qwen's weights and told to make it better at math; it changed some weights, but *"it was sort of like fixed a bug."* The closing joke: *"It's AI all the way."*

## Linked entities and concepts

- **Concepts:** [[open-source-ai]], [[ai-sovereignty]], [[foundation-models]], [[ai-benchmarks]], [[attack-surface-management]], [[dynamic-capabilities]].
- **Entities:** [[Bloomberg Podcasts]] (author), [[Anthropic]], [[OpenAI]], [[NVIDIA]], [[Cognition]].
- **Neighbour sources (typed):** [[2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai]], [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai]], [[2026-10-05-chase-langchain-interrupt-nyc-opening-keynote]], [[2026-10-20-hamalainen-lala-takkar-mckinsey-economics-of-enterprise-ai]], [[2026-09-18-bloomberg-originals-how-china-plans-to-win-global-ai-race]], [[2026-09-18-reuters-on-assignment-inside-chinas-ai-race]], [[2026-09-30-chow-metalware-ai-firmware-vulnerability-research]], [[2026-11-10-ai100-ai-goes-mainstream-2026]], [[2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free]].
- **Also cited in the body (no typed edge):** [[2026-10-15-lin-stanford-ai-club-building-in-the-ai-era]], [[2026-10-21-lewis-nadeau-mckinsey-strategy-room-frontier-ai-cybersecurity]], [[2026-11-14-tan-ugarte-yc-lightcone-rise-of-ai-coworkers]].
- **Dangling** (single-source mention, deferred): Odd Lots (the show; Bloomberg Podcasts is the author), Joe Weisenthal, Tracy Alloway, Daniel Saedi, Minerva, Bridgewater, Reflection AI, Modal, Thinking Machines, micro1, Silicon Data, Coinbase / Brian Armstrong, Greg Brockman. Named in several sources but without entity pages: Harvey, Fireworks AI, DeepSeek, Qwen (Alibaba), Kimi (Moonshot AI).

## Source quality

- **Transcript.** YouTube's human-written English track (`kind: manual`), with no speaker labels. Speakers are attributed from context and from the camera cuts on the contact sheets; where that is unclear the page says *a host*. The track mishears many names. DeepSeek (nine places) and one *"GPA's"* → GPU's were fixed in the raw file, confirmed by the description and by the replayed passage at 40:16 (listed in its `notes:`). Read but not fixed in the raw file: *"Quinn"* → Qwen, *"Kimmie"/"gimme"* → Kimi, *"cloud"* → Claude, *"fable"/"Fabo"* → Fable, *"mythos"* → Mythos, *"model"/"Modo"* → Modal. *"Astra"* (a frontier model named four times, with versions 6 and 6.2) is read as OpenAI's GPT-6 Astra, from the *gpt-6.2-astra* model name on a slide in [[2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations|Falkor's NVIDIA stream]]; the captions alone do not confirm it. **Not identified:** *"tenant"* (Harvey's fine-tuned model), *"Lagos"* (Harvey's usage-priced rival) and the data companies captioned *"McCaw and Serge"*.
- **Stills.** None published. All 197 grid tiles and 45 short-shot tiles were reviewed, with a 2-second pass around the introductions and the GPU-index passage. The episode is a three-camera studio podcast with no inserted charts or screens; one lower-third was cut to confirm the guest's name and company. Manifest: `raw/videos/how-an-american-ai-company-uses-chinese-open-weight-models-odd-lots.stills.md`.
- **Self-report and interest.** Saedi describes his own company and gives no Minerva figures (he does not want *"to release any of our own numbers right now"*). The fine-tune's gains are stated without a metric or test set. Minerva benefits from cheap open weights and from fine-tuning staying easy, and his KYC suggestion is offered as a compromise that keeps both.
- **Figures the transcript cannot settle:** Harvey's ~$6 million compute; Fireworks' $7–9 per million tokens and the $90 training run; Fireworks and Modal at ~$1 billion each in revenue (the captions say *"error"*); micro1's $250–500K per data set and $50–100K referral fees; the abliterated DeepSeek at ~$0.30 per million tokens and the *"1/100"* ratio to Fable; Reflection AI's 12–14,000 GPUs and its three-to-six-month lag (and *"allegedly"* being bought by Nvidia); 5–10 million Blackwells against ~100 million knowledge workers; Opus 4.5 *"in October of last year"*; the Brockman anecdote; the MIT weight-editing report; and a host's aside that *"Google bought Spirit Airlines for $10 million"* for its data, which this page does not repeat as fact.
- **Value.** The corpus's open-weight sources are mostly vendors, investors and analysts. This is a user of open weights explaining his own choice task by task, with prices, a worked fine-tune, and a cost (the durability problem) that the advocates do not mention.
