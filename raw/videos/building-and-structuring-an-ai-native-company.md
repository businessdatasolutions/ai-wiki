---
title: "Building And Structuring An AI Native Company"
video_id: Z3JyAqh4ixg
url: "https://www.youtube.com/watch?v=Z3JyAqh4ixg"
channel: "YC Root Access"
channel_id: UCxIJaCMEptJjxmmQgGFsnCg
channel_url: "https://www.youtube.com/channel/UCxIJaCMEptJjxmmQgGFsnCg"
publish_date: '2026-08-14T07:00:37-07:00'
upload_date: '2026-08-14T07:00:37-07:00'
category: "Entertainment"
duration: '21:20'
length_seconds: 1280
view_count: 20702
is_live: false
thumbnail: "https://i.ytimg.com/vi/Z3JyAqh4ixg/maxresdefault.jpg"
caption_tracks:
  - language_code: en
    name: "English (auto-generated)"
    kind: asr
    is_translatable: true
chapters:
  - {title: "Intro", start: '0:00', start_ms: 0}
  - {title: "Why Roman Legions Built Your Org Chart", start: '1:53', start_ms: 113000}
  - {title: "Humans as the Bottleneck", start: '3:56', start_ms: 236000}
  - {title: "What a Real AI Loop Looks Like", start: '5:28', start_ms: 328000}
  - {title: "The Data Agent That Changed Everything", start: '7:51', start_ms: 471000}
  - {title: "The Self-Improving System", start: '8:39', start_ms: 519000}
  - {title: "Office Hours → Living User Manual", start: '10:32', start_ms: 632000}
  - {title: "The AI Employee With a VM", start: '12:22', start_ms: 742000}
  - {title: "What \"Company Brain\" Actually Means", start: '14:08', start_ms: 848000}
  - {title: "Humans at the Edge", start: '15:52', start_ms: 952000}
  - {title: "Burn Tokens, Not Headcount", start: '17:44', start_ms: 1064000}
  - {title: "Make Everything Legible to AI", start: '18:29', start_ms: 1109000}
  - {title: "Simulating Investor Calls", start: '19:29', start_ms: 1169000}
description: |
  In this presentation from Startup School Paris, Y Combinator General Partner Tom Blomfield shares findings from his research on how companies are being built with AI infrastructure placed in from the start. 

  Apply to Y Combinator: https://www.ycombinator.com/apply
  Work at a startup: https://www.ycombinator.com/jobs

  Chapters:

  00:00 — Intro
  01:53 — Why Roman Legions Built Your Org Chart
  03:56 — Humans as the Bottleneck
  05:28 — What a Real AI Loop Looks Like
  07:51 — The Data Agent That Changed Everything
  08:39 — The Self-Improving System
  10:32 — Office Hours → Living User Manual
  12:22 — The AI Employee With a VM
  14:08 — What "Company Brain" Actually Means
  15:52 — Humans at the Edge
  17:44 — Burn Tokens, Not Headcount
  18:29 — Make Everything Legible to AI
  19:29 — Simulating Investor Calls
notes: |
  Acquired 2026-08-20 via the youtube-transcript skill (Playwright route), auto-generated (ASR) English track.
  ASR cleanups applied: "contouium" -> contubernium and "contouia" -> contubernia (Roman army units);
  "darnis" -> decanus; "carpathy" -> Karpathy; "Hadron's wall" -> Hadrian's Wall; "open claw" -> OpenClaw;
  "Andre Horitz" -> Andreessen Horowitz; "Post Hog" -> PostHog; "mo" -> moat; "DRR" -> DRI (directly responsible
  individual); and the repeated "rooting"/"roots" -> "routing"/"routes" where the sense is information routing.
  Speaker: Tom Blomfield, General Partner at Y Combinator, at Startup School Paris. He opens by saying the talk is
  an update of one he gave "about a month, maybe six weeks ago" and caveats that "no one knows how to do this."
  The ASR-inserted "[snorts]" and "[gasps]" markers are scraper artifacts on audience/mic noise and were left in place.
---

## [0:00] Intro

[0:03] How's your day going so far?

[0:06] Good. Great. Um,

[0:10] so I've got about 25 minutes or

[0:12] something. Um, and I'm going to try and

[0:15] talk about building AI native companies.

[0:18] This is based on a talk I gave about a

[0:20] month, maybe six weeks ago. It's on

[0:21] YouTube. Um, I've updated it. I've added

[0:24] some thoughts. I think the main caveat I

[0:26] want to start with is

[0:29] no one knows how to do this. And so this

[0:32] is um very theoretical. It's based on

[0:37] hundreds of YC companies that we're

[0:38] working with right now. Um lots and lots

[0:41] of people are trying things and I think

[0:43] if anyone tells you they've got it all

[0:45] figured out, they are probably lying. I

[0:47] think internally at YC, we have an

[0:49] amazing software team. We've been

[0:50] pushing the boundaries of I think what

[0:52] LLMs can do for a couple of years now. I

[0:55] think we have a bunch of really

[0:56] interesting use cases um which and I'll

[1:00] give examples of those as we go through,

[1:01] but I I don't think we've got it I don't

[1:03] think we've yet got it fully figured

[1:05] out. But I expect

[1:07] um by the end of 2026 or possibly by the

[1:12] first batch in 2027,

[1:14] we it will be possible I don't know if

[1:17] we'll take the PR risk of it. It will be

[1:19] possible to from end to end have an AI

[1:23] fully read all the applications, pick

[1:25] the companies to interview, conduct the

[1:27] interview, select the companies to fund,

[1:30] give them advice throughout the batch on

[1:32] how to do like run their companies more

[1:33] effectively, introduce them to

[1:35] investors, review their pitch decks, and

[1:38] then debug their pitch meetings. I think

[1:41] an AI will be able to do all of that end

[1:43] to end

[1:45] probably by the end of this year if not

[1:47] by the first three months of next year.

[1:49] We've got quite a lot of it working

[1:51] already and we're exposing a lot to our

[1:52] founders. I'll tell you more about that,

## [1:53] Why Roman Legions Built Your Org Chart

[1:53] but that's sort of where this talk has

[1:55] come from. So what is an AI native

[1:58] company? Well, the first thing to start

[2:00] with is what is not an AI native

[2:02] company. This is how the Roman legions

[2:06] were were structured. The smallest unit

[2:09] was the contubernium. So eight soldiers who

[2:12] share a tent equipment and a mule and

[2:14] there's a decanus and then 10 of these

[2:16] things called a contubernia form a century

[2:20] which is actually 80 men not 100 which

[2:21] is very confusing but you see this kind

[2:24] of hierarchical um way of organizing

[2:27] humans right the Roman legions used this

[2:31] to project power across North Africa

[2:34] across um near Asia up into the UK up to

[2:37] Hadrian's Wall this was the way that the

[2:40] Roman Empire projected connected power

[2:42] and they would pass information down and

[2:45] receive reports up and a human being was

[2:48] responsible for being that conduit the

[2:49] whole way and bizarrely

[2:53] like 2,000 years later we're still

[2:55] basically running the same kind of thing

[2:56] and like they look slightly different

[2:58] this is a Karpathy tweet which I thought

[3:00] is very good but um like they're all

[3:02] organized slightly differently but the

[3:04] same principle is true which is that

[3:07] humans are the conduit for information

[3:09] going up and down um up and down the

[3:12] rungs, right? And so there's a Jack

[3:14] Dorsey tweet which kicked this whole

[3:16] thing off about 2 months ago. There's an

[3:17] underlying assumption that organizations

[3:19] have to be hierarchically

[3:21] organized with humans as a coordinating

[3:24] mechanism. And I think basically AI

[3:28] breaks that apart. So you don't have to

[3:30] have humans as a coordinating mechanism

[3:34] any longer. And I basically think most

[3:37] companies have misunderstood is the

[3:40] wrong word. Most companies sort of

[3:42] experienced chat GPT as a Q&A bot. They

[3:45] put put questions in, they get answers

[3:48] out and then maybe they've sort of moved

[3:50] to longer running

[3:53] perhaps what you might call an agentic

[3:55] system or something. But basically you

## [3:56] Humans as the Bottleneck

[3:57] tell you ask the agent to go and do

[3:59] something. It goes away until it gets

[4:01] stuck and it comes back to you. And you

[4:03] as a human are like the gating

[4:05] mechanism. And so while you are asleep,

[4:09] the the thing can't work, right? Like if

[4:11] it stops halfway through at 3 in the

[4:12] morning, like it's waiting on input from

[4:14] you, it can't go anymore. You as a human

[4:15] are the gating mechanism. And so you you

[4:17] know, you can do things like making

[4:19] engineers 20% more productive. You can

[4:21] add co-pilots for lawyers to make their

[4:23] existing workflows go a little better.

[4:25] You can ship more software with AI. But

[4:27] really, all of these things, um, the men

[4:29] in the suits are coming from me. I don't

[4:31] know what I know.

[4:33] um uh really

[4:37] it's dependent on humans being the

[4:39] coordinating mechanism in all of these

[4:40] places. And if you think about it not

[4:42] just as like increasing productivity but

[4:45] in terms of new capabilities

[4:49] that's interesting. Oh, there we go. Um

[4:53] where basically

[4:55] a single person can do way more work

[4:57] than previously thousands of people.

[5:00] your entire company becomes queryable

[5:02] and you're not just shipping more

[5:04] software, but the the software you ship

[5:05] is like agent native. These are a lot of

[5:07] buzzwords. I'm going to go into more

[5:09] detail about what I mean. AI at the

[5:12] moment AI a lot of companies like

[5:13] bolting AI onto the side of their

[5:14] company, right? In all the ways we've

[5:16] spoken about. They're cute question

[5:17] answer bots. They're sort of very um

[5:21] lightweight agents that can call tools

[5:23] effectively like a web search or

[5:24] something like that. Um

[5:27] but if you think about the company

## [5:28] What a Real AI Loop Looks Like

[5:31] as a series of self-improving AI loops

[5:33] from the ground up, you actually get to

[5:34] a very very different conclusion. Okay,

[5:37] previously AI is like make each person

[5:39] 20% more productive or 30% more

[5:41] productive. What happens if we reimagine

[5:43] the company as a series of AI loops?

[5:46] What is an AI loop?

[5:50] It's basically like um so at the top

[5:54] you've got um product telemetry, inbound

[5:57] messages. This is like data from the

[5:59] real world, right? Like billing signals,

[6:01] support tickets, code changes, stuff

[6:04] that gets you information in and then

[6:06] you go down to the perhaps a policy

[6:08] layer which is like what rules can it um

[6:11] what rules constrain the AI? What things

[6:12] it must ask for approval for? What does

[6:14] it have to log? um you have a tool layer

[6:16] where it can call perhaps internal a

[6:18] APIs um send emails update the billing

[6:23] um and you might have APIs for this or

[6:25] MCP or whatever and then you have a

[6:27] series of quality gates which which

[6:29] could be a human and I'd argue probably

[6:31] should not be a human in all but the

[6:33] most extreme cases but the quality gate

[6:35] can often be a second adversarial LLM it

[6:37] might be something that's that's looking

[6:38] at the output saying are we suffering

[6:40] from prompt injection here or in a case

[6:44] of a bank are we giving financial advice

[6:45] here, yes or no? And if we are, we

[6:46] can't, you know, like constrain it. Or a

[6:49] really easy example for engineers is

[6:50] like um the quality gate might simply be

[6:53] a second model doing code review. Um and

[6:57] then a learning mechanism which is

[6:59] basically you loop back around, right?

[7:00] You deploy the thing, you make the

[7:01] change and you see how it impacts the

[7:03] real world. If you can do this entire

[7:06] loop without a human, your product

[7:09] starts improving itself when you're

[7:11] sleeping. Can you scroll down a little

[7:12] bit to the bottom of this, please? Yeah.

[7:14] All the way to the bottom. Thank you

[7:15] very much. So, um,

[7:19] the first time I saw these things, it

[7:20] like broke my brain a little bit. Um,

[7:23] internally at YC, we got a lot. We got a

[7:26] data on 7,000 companies, 20,000

[7:28] founders, like many hundreds of

[7:30] thousands of applications. So, a year or

[7:32] two ago, we built an AI agent that it

[7:36] basically human, it's like English to

[7:38] SQL, right? Like it's a simple data

[7:40] querying agent. You can be like, "What

[7:42] was a split of European versus uh

[7:45] American founders dispatch?" And it

[7:46] would go and translate that human query

[7:48] into SQL and run it and come back with

[7:49] the answer. It's like, "Yeah, pretty

## [7:51] The Data Agent That Changed Everything

[7:51] magical." But that feels like a tool

[7:53] that kind of makes a data analyst 20 or

[7:55] 30% more productive or actually makes me

[7:57] as a partner 10 or 20% more productive

[8:00] and I don't have to hire a data analyst.

[8:02] It was fine and it would keep hitting

[8:05] edge cases or like not be able to do

[8:07] certain things and I'd be like, "Oh,

[8:08] that's annoying." And then we shipped

[8:11] something about two or three months ago

[8:13] which for me was like the head explosion

[8:15] moment which was a second agent which uh

[8:19] sort of lives on top of this um data

[8:21] query agent and the second agent runs

[8:23] overnight and it looks for all the

[8:24] queries that any human has done during

[8:26] the day and it looks for success and

[8:30] failure. So the success is like yeah I

[8:32] copy it, I send the email I do whatever.

[8:34] the failure is like ah this didn't

[8:35] work or it I hit a permission issue or

[8:37] whatever like the database index doesn't

## [8:39] The Self-Improving System

[8:39] work or it has to it requests some

[8:41] permission it doesn't have and then that

[8:43] second AI agent overnight goes and puts

[8:46] in pull requests to fix all of the

[8:49] problems from the day before and so if

[8:51] you go back as a human on the second day

[8:53] and run the same query as yesterday it

[8:56] now works and so this process of like

[8:59] evaluating what the system is doing and

[9:01] then proposing changes to the system and

[9:02] updating the

[9:04] makes a whole thing self-improving.

[9:06] And that for me was like a head

[9:08] explosion moment. I think if you were

[9:10] here earlier for um James' talk from

[9:13] PostHog, they basically have the same

[9:15] thing for products. Now they take in all

[9:17] your product telemetry and they see

[9:20] where it's breaking and then they put in

[9:21] pull requests and eventually you'll

[9:23] automerge those pull requests. So your

[9:25] entire product surface will become

[9:27] self-improving. It will just dynamically

[9:28] you'll have a a bunch of headline

[9:30] metrics you want to optimize for. You'll

[9:32] have a bunch of product like vision

[9:34] documents which says this is the kind of

[9:36] thing we want to build. This is in scope

[9:37] and out of scope and the AI will

[9:39] basically look at your product

[9:40] telemetry, come up with ideas, deploy

[9:43] those ideas, test them with humans and

[9:45] see if it moved the needle or not and

[9:46] just self-improve. Karpathy um uh bit

[9:51] had a great tweet about three weeks ago

[9:53] now on like the auto research thing.

[9:54] Basically applying this to machine

[9:56] learning just having the AI I think it

[9:58] was on GPT2 equivalent or something like

[10:00] that but coming up with research ideas

[10:02] testing it running overnight and just

[10:04] hill climbing. All this is is hill

[10:05] climbing. If you have a an end

[10:07] measurable outcome that you can just

[10:09] come up with ideas, you can test it. Did

[10:11] we go up the hill or down the hill? If

[10:12] downhill, discard. If up, like keep and

[10:14] just keep hill climbing. And computer

[10:18] systems are really, really good at this

[10:20] kind of hill climbing work because they

[10:22] never stop. They will just run

[10:24] indefinitely indefinitely until you

[10:26] reach local maximum. It's kind of cool

[10:28] because you they don't have to sleep.

[10:30] Um,

[10:31] another example from YC, we started

## [10:32] Office Hours → Living User Manual

[10:34] recording office hours about 6 months

[10:36] ago. Um and I was given the job of

[10:41] rewriting a section of we have a user

[10:43] manual internally

[10:44] um which is written over the last 15

[10:47] years and it's like

[10:49] 500 pages long and a lot of it was very

[10:52] very good like 5 years ago and then AI

[10:55] happened and like honestly a bunch of

[10:56] the advice is just not relevant anymore

[10:58] and I had the job of rewriting a bunch

[11:00] of this stuff and I like procrastinated

[11:02] and procrastinated and procrastinated

[11:04] and we started recording the office

[11:06] hours 6 months ago and now we have like

[11:08] I don't know 3 or 4 thousand hours of

[11:10] office hours recorded and someone on the

[11:12] team Hajj I think it was had the idea of

[11:14] like what if we just transcribe and then

[11:16] mine all of the advice we actually give

[11:18] in office hours and then use that to

[11:20] rewrite the user manual and so [snorts]

[11:23] when the advice changes the AI will see

[11:26] what the humans are saying extract the

[11:28] insight and just rewrite the user manual

[11:29] and push it so it becomes this like

[11:32] living guide of how we actually advising

[11:34] companies and then obvious Obviously,

[11:36] once you've got it in the user manual,

[11:38] you just make the entire thing queryable

[11:40] to an advice agent, right? Like if a if

[11:42] a founder asks us a question in Slack

[11:45] and we get a lot of questions that are

[11:46] pretty similar honestly like how should

[11:49] I price my first customer or my third

[11:51] customer is is about to churn what

[11:54] should I do or this customer has asked

[11:55] for this esoteric feature what and just

[11:57] like we've answered versions of this

[11:59] question like 500 times and so now the

[12:03] AI can give not just Tom's answer but

[12:07] like here's how Nicolo would answer it

[12:09] or here's how would answer it. I think

[12:11] you can actually get superhuman advice

[12:13] from this thing because it's able to

[12:15] recall perfectly and access the

[12:17] intelligence of 16 partners, not just

[12:19] one with fallible memory. And so you can

## [12:22] The AI Employee With a VM

[12:22] kind of see how this these like loops

[12:25] can run in the background and get better

[12:28] and better and better and better and

[12:31] then I think

[12:35] you give them a virtual machine. So you

[12:39] give your agent a virtual machine with

[12:42] things like tools. So search the web,

[12:45] crawl your internal company directory,

[12:47] search your slack history, persistent

[12:50] file storage. So it can write it can

[12:52] come up with a plan and write the plan

[12:53] to disk. So if it fails halfway through,

[12:54] it can resume and then it needs to it

[12:58] can write code and execute the code to

[13:01] solve a problem and then see how that

[13:03] worked against the plan and adjust and

[13:06] repeat. And now you've basically got an

[13:09] AI employee.

[13:10] And I we're at the very very early

[13:13] stages of this with something like open

[13:14] claw or Hermes is a basically VMs with

[13:16] an agent living inside on a on basically

[13:18] on a repeating loop. [gasps]

[13:22] So where we are now, I think YC has a

[13:24] few of these loops internally. I think

[13:27] the next thing that happens

[13:29] like it occasionally a human has to

[13:31] intervene right be like well the loop's

[13:33] going wrong or whatever or like let's

[13:34] take some insight from there and put it

[13:35] over there. I think the thing that

[13:37] happens afterwards is the loops start

[13:39] talking to each other or the AI

[13:41] employees start communicating with each

[13:42] other to share ideas and replan and

[13:47] assess and and whatever and you end up

[13:49] with this like

[13:52] I mean company brain is is like an

[13:55] overused term now. It got very very

[13:57] popular about six weeks ago and as of

[13:59] like two weeks ago it's I see people in

[14:01] the audience with company brain written

[14:03] on a t-shirt now. There he is.

[14:05] [laughter]

[14:06] Um, but so what is this as an idea? It's

## [14:08] What "Company Brain" Actually Means

[14:10] the

[14:12] I'm going to steal some of Jack Dorsey's

[14:14] words, but in a conventional company,

[14:16] intelligence is spread throughout the

[14:18] people and the hierarchy routes it. So in

[14:23] this new model, intelligence lives in

[14:26] the system.

[14:28] What I mean by that basically is that um

[14:33] lots and lots of companies try and write

[14:34] down standard operating procedures,

[14:36] right? Like the way things should be

[14:37] done, but then when you actually observe

[14:39] people how they actually do the job,

[14:41] they were like, "Oh, well, in this edge

[14:42] case really I should do this other

[14:43] thing." And there's a lot of stuff in

[14:45] people's heads that if it weren't in

[14:48] people's heads and it was actually

[14:49] written down, you'd get a lot of value

[14:51] out of it. And so [snorts] this idea of

[14:53] a company brain I think is the

[14:55] combination of like basically taking all

[14:56] of the data in your company and that's

[14:59] things like YC's application data. It's

[15:01] it's transcripts of every call with with

[15:03] every meeting with every founder. It's

[15:05] the advice we give um the way we pick

[15:09] companies and then you record that and

[15:11] make it legible. you make you make it so

[15:13] that the AI can access all of it and

[15:16] then you have a bunch of these

[15:17] reinforcing loops that run indefinitely

[15:20] and then are able to talk to each other

[15:22] and the entire thing becomes a

[15:24] self-improving company. I think that's

[15:26] basically where we're going that you

[15:28] just pump tokens in, you get access to

[15:30] all of your data and the entire thing

[15:31] becomes selfimproving

[15:33] [snorts] and people live at the edge,

[15:36] right? So you have this kind of company

[15:38] brain, this data, these self-reinforcing

[15:40] loops and then the human beings live

[15:42] around the edge where this intelligence

[15:44] makes contact with reality. So I think

[15:47] Jack Dorsey said people reach into

[15:48] places the model can't yet go. They

[15:51] sense things the model can't perceive.

## [15:52] Humans at the Edge

[15:53] Intuition

[15:55] opinionated direction, cultural context,

[15:57] trust dynamic, the feeling in a room.

[16:00] Um, they make the calls a model

[16:01] shouldn't make on its own, especially

[16:03] ethical decisions, novel situations, and

[16:04] high stakes moment where the cost of

[16:06] being wrong is existential.

[16:09] A world model, this company brain that

[16:11] can't touch the real world is just a

[16:13] database.

[16:15] And so these humans, what what he's

[16:17] saying, I think, is the humans are in

[16:19] the sales calls, right? They're like

[16:20] visiting the client office to reassure

[16:23] people, to convince the CEO, to pitch

[16:26] the investor. It's all of the

[16:29] emotional uh kind of interpersonal stuff

[16:32] that the humans are there for, but the

[16:34] humans are no longer necessary to do the

[16:36] information routing, right? Like all of

[16:38] the information is routed automatically

[16:40] to the person who needs it. They don't

[16:41] need to go and through layers and layers

[16:43] of management to get approved.

[16:46] Um, and so that's basically what I think

[16:50] companies are going to be. They're going

[16:51] to be much much smaller. They're going

[16:52] to be centered around a kind of company

[16:54] brain and the people will interface with

[16:56] the real world and then feed all that

[16:57] information back into into the brain. A

[17:01] reasonable question is sounds great in

[17:03] theory. How do like this seems like

[17:06] sci-fi kind of like will it happen? Who

[17:08] knows? What can we actually do now to

[17:10] make it happen? Um, and so practically

[17:14] these are the tips we're giving founders

[17:16] right now. The first is I'd burn tokens,

[17:20] not headcount. So we're seeing founders

[17:23] get to demo day with a million dollars

[17:26] of revenue and some getting to series A

[17:28] um with 10 million of revenue with like

[17:30] a fraction of the the people they had

[17:32] before. You can argue about whether it's

[17:34] a thousand x or whatever, but it's

[17:36] multiple times more, right? like someone

[17:37] a polyglot who really knows how to use

[17:38] these tools is worth many many times uh

[17:41] the people before um and you can just do

## [17:44] Burn Tokens, Not Headcount

[17:44] this as a result it means the headcount

[17:46] of the whole company is going to be less

[17:49] in particular it means no middle

[17:51] management I just don't think you need

[17:53] layers and layers of like directors and

[17:55] VPs anymore the key roles for me are the

[17:58] like the IC everyone has to be an

[18:00] individual contributor actually doing

[18:02] the work coming to meetings with working

[18:04] prototypes not decks and DR like DRI is

[18:08] for me actually the biggest thing a lot

[18:09] of companies are missing which is like a

[18:11] single person who head is on the block

[18:13] to make something happen. As soon as you

[18:15] have a committee I worked at a bank and

[18:17] we had so many committees for everything

[18:19] and it grinds things to a halt. So

[18:20] having a single person who's directly

[18:22] responsible for the outcome I think

[18:23] these are most two important the two

[18:25] most important roles and I think middle

[18:27] management is gone. Practically speaking

## [18:29] Make Everything Legible to AI

[18:30] um I would try to make and this is by

[18:32] the way easier when you're starting out.

[18:34] I would make everything in your

[18:35] organization legible to legible is like

[18:37] a really popular word in Silicon Valley

[18:39] right now. It means you can read it.

[18:41] Make all your data readable to AI.

[18:44] That means recording everything,

[18:46] transcribing literally every meeting.

[18:48] Um, if you can't get access to Slack

[18:51] DMs, I would ban Slack DMs. Make

[18:53] everything um in public channels the AI

[18:56] can access. Every action needs to create

[18:58] an artifact. It needs to create a uh

[19:01] written or recorded version. Otherwise,

[19:03] it basically didn't happen to the AI.

[19:05] Obviously, I think on demand internal

[19:07] software for all intern in all company

[19:09] operations is um absolutely necessary. A

[19:13] really cool thing we've just started

[19:15] doing, which I don't think we've spoken

[19:17] about yet, um is uh and it's inevitable

[19:21] it comes out anyway. So, um obviously

[19:24] you record all your um sales meetings,

[19:27] right?

## [19:29] Simulating Investor Calls

[19:29] And you can feed those sales meetings

[19:30] back into an AI to be like, "How did I

[19:32] do with my sales meeting?" What if you

[19:34] also recorded all your meetings with

[19:36] investors and you took those investor

[19:39] calls and you had access to several

[19:41] hundred or thousand companies that all

[19:43] meeting all the same investors every 3

[19:45] months. And the first thing you can do

[19:47] is tell founders, here's what's going

[19:48] wrong with your pitch. You spent 90% of

[19:51] the time talking or you really fumbled

[19:53] this question or you need to be much

[19:55] more concise on your go to market. very

[19:57] very easy to do and many of our founders

[19:59] are taking 40 or 50 or 60 investor

[20:01] calls. You just pump them in and the AI

[20:03] will if you're recording them tell you

[20:05] what's going well and what's going

[20:06] badly. But we also get data on the other

[20:08] side of that conversation. These

[20:10] founders are meeting the same investors.

[20:12] So investor X will definitely here's how

[20:16] like we could simulate the investment

[20:18] call, right? We could say here's exactly

[20:19] how Andreessen Horowitz does every single

[20:21] investment call whereas founders fund

[20:23] will ask you this question this question

[20:24] or this particular partner will always

[20:27] say what's your wedge or what is like

[20:30] what's your moat if Anthropic comes after

[20:32] this and here's a great way to answer

[20:34] that and I'm sure I'm I don't feel bad

[20:36] about doing this at all because I

[20:37] absolutely know that those investors are

[20:39] also recording this and pumping into

[20:40] their AI [snorts] and so anyway

[20:43] basically if you can record it if you

[20:46] make it legible then the AI can start to

[20:47] comprehend and give you superpowers. I

[20:50] will finish on this. If you were

[20:51] starting a company today, would you

[20:54] build it like this? And for this was a

[20:57] talk to very early stage YC founders.

[20:59] Most of you are even earlier stage and

[21:02] you're small enough to just build it

[21:03] right from the start. So anyway, I'll

[21:06] finish there. I think we have no we'll

[21:08] just do questions with all of us, I

[21:09] think, rather than me taking questions

[21:10] on my own. Why do we do that?

[21:13] Thank you. [applause]
