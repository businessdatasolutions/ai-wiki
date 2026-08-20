---
title: "How Companies Are Building Their Own Intelligence | Sonya Huang, Sequoia Capital"
video_id: bMMv0bZzONg
url: "https://www.youtube.com/watch?v=bMMv0bZzONg"
channel: "Sequoia Capital"
channel_id: UCWrF0oN6unbXrWsTN7RctTw
channel_url: "https://www.youtube.com/channel/UCWrF0oN6unbXrWsTN7RctTw"
publish_date: '2026-08-11T05:00:09-07:00'
upload_date: '2026-08-11T05:00:09-07:00'
category: "Science & Technology"
duration: '17:29'
length_seconds: 1049
view_count: 44951
is_live: false
thumbnail: "https://i.ytimg.com/vi_webp/bMMv0bZzONg/maxresdefault.webp"
caption_tracks:
  - language_code: en
    name: "English (auto-generated)"
    kind: asr
    is_translatable: true
chapters:
  - {title: "What is sovereign AI (and what it isn't)", start: '0:00', start_ms: 0}
  - {title: "Centralized vs. decentralized intelligence", start: '1:24', start_ms: 84000}
  - {title: "Four reasons companies own their models: cost, speed, performance, destiny", start: '2:54', start_ms: 174000}
  - {title: "Not your weights, not your product", start: '4:22', start_ms: 262000}
  - {title: "The application companies are the newest neo labs", start: '5:32', start_ms: 332000}
  - {title: "Step 1: Deciding what to own vs. rent", start: '7:05', start_ms: 425000}
  - {title: "Step 2: Build the team (and don't shoehorn your platform team)", start: '9:51', start_ms: 591000}
  - {title: "Step 3: Legibility – why your research has to be visible", start: '11:17', start_ms: 677000}
  - {title: "Step 4: The technical roadmap", start: '12:33', start_ms: 753000}
  - {title: "The stack: production vs. development", start: '13:56', start_ms: 836000}
  - {title: "Opening Pandora's box – base models, harnesses, context", start: '15:16', start_ms: 916000}
description: |
  Sequoia Capital partner Sonya Huang opens our Own Your Intelligence event with the case for why more companies are choosing to own their intelligence, down to the weights. She lays out the four forces driving the shift: cost, speed, performance, and controlling your own destiny, and explains why the race for the application layer is becoming the race for the intelligence layer itself.

  Sonya shares an opinionated framework for deciding what to own vs. rent when assembling your AI stack, and another for how to get going from zero to one. With today's open-weight models near the frontier, she argues, owning your stack is no longer a performance sacrifice. It may be your performance edge.

  00:00 What is sovereign AI (and what it isn't)
  01:24 Centralized vs. decentralized intelligence
  02:54 Four reasons companies own their models: cost, speed, performance, destiny
  04:22 "Not your weights, not your product"
  05:32 The application companies are the newest neo labs
  07:05 Step 1: Deciding what to own vs. rent
  09:51 Step 2: Build the team (and don't shoehorn your platform team)
  11:17 Step 3: Legibility – why your research has to be visible
  12:33 Step 4: The technical roadmap
  13:56 The stack: production vs. development
  15:16 Opening Pandora's box – base models, harnesses, context
notes: |
  Acquired 2026-08-20 via the youtube-transcript skill (Playwright route), auto-generated (ASR) English track.
  ASR cleanups applied to proper nouns and jargon: "GBT" -> GPT; "Satia" -> Satya; "nail labs" -> neolabs;
  "eels and benchmarks" -> evals and benchmarks; "spine tuning" -> fine-tuning; "sam grep" -> Sourcegraph;
  "DeFi DJs" -> DeFi degens; "cussing your crypto" -> custodying your crypto; "Kimmy K3" -> Kimi K3;
  "GLM52" -> GLM-5.2; "doing your own valves" -> doing your own evals; "Ral environments" -> RL environments;
  "Meror" -> Mercor; "turbo puffer" -> Turbopuffer; "glean" -> Glean; "cogs" -> COGS.
  Two named individuals could not be verified and are left as the ASR rendered them: "Nico" and "Alex", cited as
  example lab-leader profiles. The company name transcribed as "south Alain" is uncertain.
  Speaker: Sonya Huang, partner at Sequoia Capital. Opening keynote of Sequoia's "Own Your Intelligence" event;
  roughly 80 portfolio founders and AI leaders in the room. She flags twice that she is not technical and that the
  framework is opinionated.
---

## [0:00] What is sovereign AI (and what it isn't)

[0:00] Okay, good morning everyone. Thank you

[0:02] all so much for being here. We have

[0:04] about 80 portfolio company founders and

[0:06] AI leaders uh in the room to explore a

[0:09] very timely topic, owning your

[0:11] intelligence or sovereign AI. Uh today's

[0:14] event is meant to be half a rallying

[0:16] call and half technical how-to. And so

[0:19] we have stacked the agenda with I think

[0:21] high high substance technical talks and

[0:23] demos so that we don't just talk the

[0:25] talk of building your own AI but

[0:27] actually learn how to get there

[0:28] together. Uh so thank you all for taking

[0:30] the time out of your mornings to join

[0:31] us. I know your time is incredibly

[0:33] precious and let's dive right in.

[0:37] So let's start with the opportunity.

[0:39] What is sovereign AI? Uh a sovereign is

[0:42] an independent state that has total

[0:43] self-governance. And so sovereign AI

[0:46] refers to companies owning their own

[0:48] intelligence without external

[0:50] dependencies down to the weights. An

[0:52] important nuance here is we are

[0:54] definitely not telling our companies to

[0:55] get off Opus or GPT. That is definitely

[0:58] not the message. Uh for coding agents,

[1:01] for desktop work, uh for frontier level

[1:03] APIs, the closed model APIs are

[1:06] wonderful. But what we've observed is

[1:08] that more and more of our companies are

[1:10] going down the path of wanting to build

[1:12] their own AI capabilities in parts of

[1:14] their products and vertically

[1:16] integrating towards owning more of this

[1:17] intelligence. And so today's session is

[1:20] meant to equip companies that are

[1:21] starting to go down that journey.

## [1:24] Centralized vs. decentralized intelligence

[1:24] We're obviously not alone in this idea.

[1:27] In the last month, uh, the rhetoric

[1:29] around sovereign AI has escalated

[1:31] sharply with folks like Alex Karp and

[1:33] Satya speaking up in support of

[1:35] companies owning their own intelligence.

[1:38] Just last week, Jensen led the charge in

[1:40] making sure that open-weight models

[1:41] remain available in the US and it was

[1:44] awesome to see the near unanimous wave

[1:46] of support. I think the message is very

[1:48] clear that companies want to own their

[1:51] intelligence. They want to own not rent

[1:53] their weights. And I think it's simply

[1:55] because intelligence is too core, too

[1:57] fundamental of a property to just

[1:59] outsource.

[2:02] We're glad that sovereign AI is in the

[2:04] zeitgeist right now. Uh because we think

[2:05] it's a good thing for the world. On one

[2:07] hand, you have centralized intelligence

[2:09] where a single all powerful AI powers

[2:12] more and more of the GD the world's GDP

[2:14] as a black box sucking in all the data

[2:17] exhaust, all the data flywheels from the

[2:18] rest of the world. On the other hand,

[2:21] you have decentralized intelligence

[2:23] where the whole world builds on top of a

[2:26] solid core, but every individual person

[2:29] company builds their own intelligence on

[2:30] top bespoke to their own data, their own

[2:34] industries, their own personalization,

[2:36] uh their own way of working, their own

[2:37] taste and so the ecosystem flourishes

[2:40] and individuality triumphs. No single

[2:43] company swallows the rest. I think this

[2:45] is a much more optimistic view of the

[2:47] world.

[2:49] And so we work with dozens of companies

[2:51] that are going down the journey of

[2:52] building their own AI. Um here are the

## [2:54] Four reasons companies own their models: cost, speed, performance, destiny

[2:55] biggest reasons that we've seen people

[2:56] move. Reason number one is cost. Uh

[3:00] especially for low zero negative margin

[3:03] companies, sovereign AI isn't a nice to

[3:05] have, it's a mustave. Um ironically, the

[3:09] more successful your AI product is, the

[3:11] higher your AI COGS tend to be. And so

[3:13] it's actually the companies that have

[3:15] been most advanced in their deployment

[3:17] of AI that have been the first to go on

[3:19] this journey of of owning their own

[3:21] models. Reason number two is speed. And

[3:24] so in certain domains, coding is one of

[3:27] them. Uh security is another one. A

[3:30] small distilled custom model can beat a

[3:32] large general one because speed is so

[3:34] important.

[3:36] Num reason number three is performance.

[3:39] And this is a relatively newer one. I

[3:41] would say last year most companies were

[3:43] not choosing to own their intelligence

[3:44] to generate better performance. Uh but

[3:47] we're now at the point where open models

[3:48] can outperform closed ones on your

[3:50] domain and we're going to spend a lot of

[3:52] today's agenda talking about how to get

[3:54] there. And then reason number four,

[3:56] controlling your own destiny. Uh

[3:58] anthropic and open AI, I actually think

[4:00] to their credit, they've been really

[4:02] wonderful partners to a lot of the

[4:03] ecosystem, but companies are

[4:05] increasingly finding that they want

[4:07] their own set of independent legs to

[4:08] stand on as well.

[4:11] Um, does anybody here come from the

[4:13] crypto days or remember the crypto days?

[4:15] Okay. Um, do you guys remember this

[4:17] meme? Okay. Uh, in the crypto of the

[4:20] days, there was this meme for the DeFi

## [4:22] Not your weights, not your product

[4:22] DJs. Uh, not your keys, not your crypto.

[4:25] And so, if somebody was cussing your

[4:27] crypto for you, it fundamentally wasn't

[4:29] yours.

[4:30] I hereby present the AI version of this

[4:32] meme. Not your weights, not your

[4:34] product. Um, I think that for a product

[4:37] to be truly yours, I think it's

[4:38] reasonable to think that you need to be

[4:40] able to control control and custody your

[4:42] own weights.

[4:45] Pat shows this slide at AI ascent

[4:47] talking about the race for the

[4:48] application layer. Uh, the you look so

[4:51] proud of yourself. Uh, the punch line is

[4:53] that both the AGI labs and the

[4:55] application companies are racing to be

[4:57] the userfacing product from different

[4:59] ends. the foundation model labs from the

[5:01] model side and the application companies

[5:03] from the user back. I think we're seeing

[5:06] a new dynamic emerge now which is

[5:08] actually that battleground is

[5:10] increasingly becoming not just the race

[5:12] for the application layer but the race

[5:14] for the intelligence layer. And so this

[5:17] this battleground is no longer just

[5:18] about who gets to control the product,

[5:20] the UI, the go to markets, the wrapping.

[5:22] It's actually about who can own the

[5:24] intelligence itself and shape better

[5:27] intelligence in the product. So the

[5:28] product is the intelligence and the

[5:30] newest battleground is for not just the

## [5:32] The application companies are the newest neo labs

[5:33] product surface but for the intelligence

[5:35] layer itself.

[5:37] And so the hottest neolabs in my

[5:38] opinion are actually uh the applied

[5:41] research that we see coming out of

[5:43] companies right now like Harvey,

[5:46] like factory,

[5:48] Glean,

[5:51] open evidence,

[5:54] Sourcegraph

[5:57] the list goes on and on and I think the

[5:59] research is spanning everything from

[6:00] evals and benchmarks to harness

[6:02] engineering to new algorithmic

[6:04] techniques for fine-tuning and a a lot

[6:07] lot more and we started this uh we

[6:09] started this morning talking about

[6:11] centralized versus decentralized

[6:12] intelligence. I think it's really

[6:14] wonderful to see the amount of

[6:15] innovation that is happening in the

[6:18] democratized intelligence world. Like I

[6:20] actually think the application companies

[6:22] are the newest neolabs.

[6:25] Okay. So I assume that everyone here

[6:27] today is pretty bought into this

[6:28] journey. Let's assume that you want to

[6:30] build your own lab, build your own

[6:31] models. How do you go from zero to one

[6:33] to 100? We're going to do something a

[6:35] little bit different today here. Um, I'm

[6:37] going to lay out an opinionated

[6:38] framework and technical roadmap. And so,

[6:41] take that with a giant grain of salt.

[6:43] Uh, every company is different and and

[6:45] I'm not technical and so take this with

[6:47] a giant giant grain of salt, but I hope

[6:49] it provides a useful starting point for

[6:51] how to think about building your own

[6:52] intelligence.

[6:55] Uh, step one um to owning your

[6:58] intelligence is strategy. What parts of

[7:01] your AI do you want to own? what parts

[7:03] do you want to rent? Step two is team.

## [7:05] Step 1: Deciding what to own vs. rent

[7:06] Figuring out how to staff and organize

[7:08] people towards the production of

[7:10] intelligence. Step three is legibility.

[7:12] I really think this gets glossed over um

[7:15] and is incredibly important. So more on

[7:17] this later. And then finally, step four,

[7:19] we're going to talk about a technical

[7:20] road map. What are the building blocks

[7:22] you need to assemble in order to build

[7:23] your own intelligence? So let's dig in.

[7:27] Um step one, defining which capabilities

[7:29] you want to own versus rent. Sovereign

[7:32] AI isn't binary. Uh you're not 0% or

[7:34] 100% sovereign. Um an important part of

[7:37] the strategy is to draw the lines for

[7:39] which intelligence you want to own and

[7:40] which you're comfortable outsourcing.

[7:42] And so here's a useful framework to

[7:44] think about um what parts you want to

[7:47] own versus rent. I think there are four

[7:49] important factors that go into this. Uh

[7:52] one is cost. Like how how important is

[7:54] this cost line item to your overall

[7:56] COGS. Uh two is speed and latency. Is it

[7:59] a P0 or not? Um, factor three is

[8:03] performance. And this is where it gets

[8:04] very interesting. It used to be that you

[8:06] would choose open weights when you

[8:09] didn't care about performance. Now we're

[8:10] getting to the point where in certain

[8:12] domains, you may get better performance

[8:14] by tuning models on your own data. And

[8:17] then finally, proprietary data. Are you

[8:19] in a domain where the data you're giving

[8:21] the model to improve it is super

[8:22] proprietary, super proprietary to your

[8:25] business or less so? Um, so here are

[8:28] some examples of how companies have

[8:29] decided to make this trade-off. In

[8:31] coding, you have both agents and you

[8:33] have autocomplete. On the agent side,

[8:36] this these are still mostly rented today

[8:38] because you want strong out-of-the-box

[8:40] performance and latency isn't a P zero.

[8:44] Um, on the other hand, for tab

[8:45] autocomplete models in coding, you

[8:48] really really care about speed and these

[8:50] uh these API calls are so frequent that

[8:52] the costs really rack up. And so most

[8:54] tab auto complete models now run on

[8:57] sovereign intelligence. I work at a

[8:59] cyber security company in South Alain I

[9:01] think I saw you earlier uh that owns its

[9:04] models primarily for speed and

[9:06] performance um and the ability to post

[9:08] train the model in very bespoke ways. Um

[9:10] bio companies are moving to their own

[9:13] models because of the value of

[9:14] proprietary data in that space. And so I

[9:16] think this is just a useful framework to

[9:18] think about which AI capabilities do I

[9:21] want to own versus rent. Step two,

[9:24] assemble a team. I've shown two profiles

[9:27] of labs leaders here just as examples.

[9:29] Uh Nico comes more from the research

[9:31] side of the house, having done uh

[9:33] research at Apple and then at Google

[9:35] Brain. Alex comes more from the

[9:37] engineering side, having held multiple

[9:38] engineering roles at Microsoft and then

[9:40] ramp. And I I show this just to say

[9:42] there's multiple paths to Nirvana and

[9:44] depending on the flavor of research

[9:46] you're going to be doing at your company

[9:48] um whether it's going to be more

[9:48] fundamental or applied there are

[9:50] different profiles uh that work for a

## [9:51] Step 2: Build the team (and don't shoehorn your platform team)

[9:52] labs leader. I also think it's important

[9:55] to think about how to design your

[9:56] organization. Um traditionally AI teams

[10:00] have frequently been organized hub and

[10:02] spoke. So you have a single platform

[10:04] team supporting different uh different

[10:06] AI product uh different application uh

[10:09] product teams. And what I've seen is

[10:11] that a lot of companies are shoehorning

[10:13] this AI platform team into doing the

[10:16] sovereign AI stuff as well. Um, I'd

[10:18] encourage folks not to do this. Uh, I'd

[10:21] encourage people to start from scratch

[10:22] here because this fundamentally is not a

[10:25] platform services capability. You want

[10:28] people that are able to think on their

[10:30] feet, think on the frontier and produce

[10:32] frontier level research. And it's such a

[10:34] different flavor of research and you

[10:35] want them to be playing offense, not

[10:37] just servicing teams. And so we've seen

[10:40] uh small denovo teams get very far here.

[10:42] Harvey, for example, has published a ton

[10:45] of research. They have just a team of

[10:46] seven. And so start small. I'd say start

[10:49] from scratch. Um consider making it uh

[10:52] your own lab.

[10:54] Step three, legibility. I think this is

[10:56] totally underestimated and how important

[10:58] it is because my guess is a lot of

[11:00] people in this room are doing wonderful

[11:02] research inhouse internally and that not

[11:05] all of it is very externally legible.

[11:07] And Winston Weinberg talks about how the

[11:09] responsibility of a CEO is twofold. One,

[11:12] drive substantive results, but two,

[11:15] control the narrative, control

[11:16] legibility around what you're building.

## [11:17] Step 3: Legibility – why your research has to be visible

[11:18] And I totally agree. Um, when it comes

[11:21] to owning your AI stack, legibility

[11:23] really matters because every single

[11:25] buyer right now is choosing their AI

[11:27] champion. And so they're trying to

[11:30] they're they're getting the same pitch

[11:31] over and over again. They're trying to

[11:32] discern which vendor is sophisticated

[11:34] enough to take me to the promised land.

[11:37] Um, and you know, they want to they want

[11:39] to choose people that know what they're

[11:40] doing. Increasingly, that means putting

[11:42] out your own research. And so being

[11:44] legible here means doing excellent

[11:46] technical marketing, maybe having your

[11:48] own separate branded labs or research

[11:51] group, publishing research with high

[11:53] taste. All of this matters a lot. I

[11:55] think it goes overlooked. And so, um,

[11:57] for the all the Sequoia companies in

[11:59] this room, I would really really push on

[12:00] us to think about this.

[12:02] And then finally, step four, setting

[12:04] your technical road map. Um at a high

[12:06] level the uh the rough journey that I

[12:08] see companies take and every company

[12:10] goes on a different journey but first

[12:11] you set your strategy. Um second

[12:14] defining eval this is so important. Um

[12:17] it is unglamorous work. It is not fun

[12:19] work but the more that you do up front

[12:21] the better positioned you are for

[12:22] everything after. And so I think this is

[12:24] a really really crucial to get right at

[12:25] the beginning. Um next we see companies

[12:28] starting to play with model routers with

[12:30] harnesses. Um, some companies find they

[12:32] can get good performance with out- of-

## [12:33] Step 4: The technical roadmap

[12:34] the-box models. Um, others are finding

[12:37] strong performance gains from

[12:38] post-training. In some rarer cases,

[12:40] needing to move into mid-training,

[12:41] pre-training, and then finally setting

[12:44] that machine up so that live customer

[12:46] data is actually creating a feedback

[12:48] loop where your model, your intelligence

[12:50] is improving with every customer

[12:52] interaction. And so, this is the rough

[12:54] journey that I see people go on. Um,

[12:56] again, every company is very, very

[12:58] different. And I'd encourage everyone in

[13:00] the in the audience today is just

[13:01] compare notes with with people around

[13:03] you. Everyone is everyone's somewhere on

[13:05] this journey.

[13:07] The beauty of owning your stack is that

[13:09] you can actually drive frontier level

[13:11] performance now. And so this is somewhat

[13:12] new and in large part this is thanks to

[13:15] the newest open-weight models uh

[13:17] especially Kimi K3 and GLM-5.2 being

[13:21] extremely good. um because the weights

[13:24] are available, they're actually much

[13:26] more malleable than working with the

[13:27] closed APIs. And so you start with a

[13:30] baseline that's already close to

[13:32] frontier and then within with a good

[13:34] enough technical roadmap. So with strong

[13:37] uh post- training, prompt harness

[13:39] engineering, online learning, you can

[13:41] actually reach better than frontier

[13:43] performance by owning your stack. And so

[13:45] this is new for 2026. I think this is

[13:46] very very important. This is a big part

[13:48] of why people are starting to think

[13:50] about owning their intelligence.

[13:52] Um I like diagrams and so in an attempt

[13:54] to orient us all here is how I think

## [13:56] The stack: production vs. development

[13:56] about the stack from an infrastructure

[13:58] perspective. On the left hand side this

[14:00] is production. This is your userfacing

[14:02] intelligence. This is the stack that

[14:05] drives um every every uh token that your

[14:08] user ends up seeing. And fundamentally I

[14:10] think of the production stack as a

[14:12] harness on top of a model. Alongside

[14:15] that you have a development stack. These

[14:17] are the tools and vendors that you use

[14:18] to get your intelligence good. In the

[14:21] closed model ecosystem, this entire

[14:22] stack is very simple. You have

[14:24] foundation models like Opus, GPT. Um,

[14:26] and you have the harnesses that come out

[14:28] of the box with each and you can get

[14:30] quite far with the stack, including

[14:32] building your own harnesses, prompts,

[14:34] feeding contexts into the models, doing

[14:36] your own valves. Um, but you're not

[14:38] really having to collect a ton of data.

[14:40] You're not really having to train your

[14:41] own models. And so it's much simpler

[14:43] stack. And so I'd say this is a higher

[14:45] floor, but it's a lower ceiling because

[14:47] you don't actually have the ability to

[14:49] take your own data, to take online

[14:51] production data and improve your own

[14:53] intelligence.

[14:55] The minute that you start to think about

[14:57] owning your own intelligence, it is like

[14:59] opening a Pandora's box because that

[15:01] beautiful clean API call is now um

[15:04] having to train your own models. And so

[15:07] instead of having a single model API and

[15:09] some uh good performance out of the box,

[15:12] you have to choose a open source base,

[15:15] do a lot of post training on top. For

## [15:16] Opening Pandora's box – base models, harnesses, context

[15:17] your harness, you got a choice of

[15:19] several open harnesses and then it's up

[15:20] to you to configure the harness, the

[15:22] logic, the tools, the context, uh versus

[15:25] taking an agent that just works out of

[15:26] the box. Um I just an aside here,

[15:29] context is really really important to

[15:31] driving performance. Um, and there's

[15:33] several different flavors of context

[15:35] that that that are uh driving these

[15:37] these models. Um, a vector database like

[15:39] a Turbopuffer, an enterprise knowledge

[15:41] graph like a Glean. Um, open source

[15:44] connectors obviously via MCP. Um, and

[15:46] then even novel approaches to context.

[15:48] Uh, Dan Beerman from Engram is

[15:51] here. Uh, they're doing novel research

[15:53] around encoding context in in the

[15:55] weights themselves. Um, so I'd encourage

[15:57] anyone that wants to chat about memory

[15:58] to go find Dan during one of the breaks.

[16:01] Um, and then alongside the production

[16:03] stack, the development stack becomes way

[16:05] more important when you own your own AI.

[16:08] You have to carefully monitor eval to

[16:10] know how your intelligence measures up

[16:12] um, and watch how the model performance

[16:14] is drifting in production. You need a

[16:16] lot of highquality data to post-train

[16:19] the models for your domain. Sometimes

[16:21] this is expert trajectories. U, uh,

[16:23] sometimes it's synthetic data, sometimes

[16:25] it's RL environments. And then finally,

[16:27] you need to think about how to set up

[16:29] online learning for your system so that

[16:31] your intelligence gets better and better

[16:32] with every single user interaction.

[16:35] And so the way that we've set up today

[16:36] is we've picked a series of technical

[16:38] workshops to give you deep dives into

[16:40] everything you need to build your own AI

[16:42] other than pre-training your own models.

[16:44] Uh Lin from Fireworks is going to lead

[16:46] a workshop on post-training. Harrison

[16:49] from Langchain is going to lead a

[16:51] workshop on harnesses and evals. Brendan

[16:54] from Mercor is going to lead a workshop

[16:56] on RL environments, synthetic data, and

[16:58] more. And then finally, Trajectory is

[17:00] going to lead a workshop on online

[17:02] learning.

[17:04] And then to bring it all together,

[17:05] Harvey's going to lead a workshop on how

[17:07] they approach building their entire AI

[17:09] stack and strategy. And just yesterday,

[17:11] they announced Harvey Research. You'll

[17:14] see that um uh many of their technical

[17:16] partners are actually speaking today.

[17:18] And so we've really gone all out to get

[17:20] the best possible lineup of speakers

[17:21] today, both inside and outside the

[17:23] portfolio. [applause]
