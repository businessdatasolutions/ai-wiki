---
title: "Spec-Driven Development: The Discipline Behind Reliable AI Coding"
video_id: Gv4hd49lI4E
url: https://www.youtube.com/watch?v=Gv4hd49lI4E
channel: deepsense
channel_id: UCp6CS32dzZtnU6RqKDtXnkg
channel_url: https://www.youtube.com/channel/UCp6CS32dzZtnU6RqKDtXnkg
publish_date: '2026-05-26T05:09:54-07:00'
upload_date: '2026-05-26T05:09:54-07:00'
category: Science & Technology
duration: '18:12'
length_seconds: 1092
view_count: 7742
is_live: false
is_family_safe: true
thumbnail: https://i.ytimg.com/vi_webp/Gv4hd49lI4E/maxresdefault.webp
keywords:
  - "ai coding agents"
  - "spec driven development"
  - "ai assisted software development"
  - "ai code generation"
  - "coding agent workflows"
  - "maintainable ai codebases"
  - "ai software engineering"
  - "specification driven engineering"
  - "vibe coding"
  - "ai coding reliability"
  - "ai dev workflows"
  - "coding agents architecture"
caption_tracks:
  - language_code: en
    name: "English (auto-generated)"
    kind: asr
    is_translatable: true
chapters:
  - {title: "Intro&Agenda", start: '0:00', start_ms: 0}
  - {title: "Why vibe coding breaks at scale", start: '2:08', start_ms: 128000}
  - {title: "What SDD actually means", start: '3:35', start_ms: 215000}
  - {title: "Spec-driven workflow in practice", start: '6:25', start_ms: 385000}
  - {title: "Benefits and drawbacks", start: '10:05', start_ms: 605000}
  - {title: "Best practices and takeaways", start: '13:38', start_ms: 818000}
description: |
  AI coding agents, spec-driven development, AI-assisted software development, AI code generation, maintainable AI codebases and specification-driven engineering workflows.

  In this Tech Experts Webinar, Paweł Kmiecik, Senior Staff ML Engineer, explains how specification-driven development (SDD) helps teams build more reliable software with AI coding agents.

  The webinar focuses on the practical limitations of “vibe coding” and shows how structured specifications improve consistency, maintainability, and long-term development workflows.

  The session also compares dedicated SDD tools, lightweight methodologies, and agent-native approaches for specification-driven engineering.

  🔗 Check out our website: https://deepsense.ai/?utm_source=YouTube&utm_medium=Video_26_05_2026&utm_campaign=Opis
  🔗 Linkedin: https://www.linkedin.com/showcase/applied-ai-insider

  00:00 Intro&Agenda
  02:08 Why vibe coding breaks at scale
  03:35 What SDD actually means
  06:25 Spec-driven workflow in practice
  10:05 Benefits and drawbacks
  13:38 Best practices and takeaways

  #AICoding #AIEngineering #SoftwareEngineering #CodingAgents
notes: |
  Acquired 2026-09-19 via youtube-transcript-skill (Playwright). Only an
  auto-generated (ASR) English track exists; no human-curated track.
  Single speaker; the transcript's opening 14 seconds are a cold-open teaser
  repeating lines from 5:54 and 9:13.
  ASR cleanup applied: speaker and employer ("Pavo Kitik" -> "Paweł Kmiecik",
  "Dibson's AI" -> "deepsense.ai", both confirmed by the channel description);
  "VIP coding" / "v coding" / "pipe coding" -> "vibe coding"; "SDDD" -> "SDD";
  "specdriven" -> "spec-driven"; "agents MD" -> "AGENTS.md"; "clock MD" ->
  "CLAUDE.md"; "ears" -> "EARS"; "gerkin" / "girking" -> "Gherkin"; "Cairo" ->
  "Kiro"; "opensp spec" / "open spec" -> "OpenSpec"; "spec kit" -> "Spec Kit";
  "spec anort" -> "spec-anchored" (4:47, and the elided term at 4:12 restored
  from context); "somethingational" -> "something aspirational"; "Bramfield" ->
  "brownfield"; "PUC's" -> "PoCs"; "cloud skills" -> "Claude skills";
  "Andre Karpathy" -> "Andrej Karpathy"; "for text" -> "for tech [stack]".
  UNRESOLVED: at 8:39 the verb heard as "skewed" is rendered "[steered?]".
  Short ASR segments were grouped into paragraphs of six; each paragraph keeps
  the timestamp of its first segment. Chapter headings are the channel's own.
  The talk is slide-driven and the slides are not in the transcript: the
  spec examples at 6:49 ("what you see on the left... on the right") and the
  tooling-landscape grouping are described but not shown.
---
## [0:00] Intro&Agenda

[0:00] You can think of it like something similar to AGENTS.md or CLAUDE.md but something more powerful. Something about the tooling landscape. I wouldn't focus on given tools but I group them into some areas and I would like to share my

[0:14] best practices with you. [music] [music] Hello, my name is Paweł Kmiecik. uh I work as senior staff machine learning engineer at deepsense.ai and today I'm going to tell you something about

[0:31] specification uh driven development. Uh so let's start with the agenda for today. Uh first I try to define the problem with vibe coding then I tell you about the spec-driven development how it works what it is. Uh then we'll go to

[0:46] benefits drawbacks my recommendations and where to start. So uh why SDD? Uh maybe some um short um introduction. So I see that teams uh produce code faster but they create software slower and the spec-driven development um tries to uh

[1:07] mitigate this issue and tries to solve the most common uh issues with the uh v coding. Yeah, maybe something about the gen AI revolution. So uh we can say for now that the most hottest new programming language is English. Uh

[1:23] that's the statement from Andrej Karpathy in 2023. Uh and three years later uh we see the environment our environment looks like. So most of us use um AI tools uh and some startups are even generating almost all their code they

[1:41] create. Uh so it looks like the English is now the the most common um uh commonly used language while uh programming but we shouldn't forget that it's not replacing the software development. So the hard part uh like

[1:58] deciding what to build what done looks like uh it's still be there and will be for for next decades I think. uh so or

## [2:08] Why vibe coding breaks at scale

[2:08] the vibe coding and why do we have a problem uh with that maybe some of you don't think that there is any problem in vibe coding but in my opinion it's a great tool for uh quick prototypes uh some scripts and fast PoCs uh but from

[2:24] my experience it's break it breaks down at scale so if we want to uh create something for production uh we have some examinations that show that uh well just vibe coding uh makes the uh quality of the code uh worse and worse. Uh and well

[2:42] this is not the problem with AI tools that we use but this is the problem how we um how we uh use them. So uh the AI did exactly what it was asked to but uh what it was asked kept changing over time. So going to the spec-driven

[3:00] development we should start with the specification and its definition. I can say that uh generally speaking uh any please implement prompt you write down uh to your AI agent or AI assistant is some kind of a specification just uh a

[3:16] really low quality uh and uh for specification uh we have some formalized languages like uh EARS or Gherkin or RFC uh 2119 uh which tell us how to create a good precise uh specifications

[3:33] uh you may know it from for example

## [3:35] What SDD actually means

[3:35] behavioral driven development um for the uh spec-driven development and what is the uh status of this field for now uh we can uh say we have like three approaches to that uh first is is spec first and this is when uh we just uh

[3:54] prompt our AI assistant some kind of specification is created to uh to perform a given task but when it's on when our code is generated uh then this specification is like thrown away. It's not used or committed to the uh uh to

[4:10] the repository. Then we have spec-anchored, when we uh keep both specification in our repository and uh also of course the code generated and we try to uh keep them in sync and the last one is spec as source. So we only care about the

[4:26] specification and we treat the code generated like a compiled binaries. So in practice most of the teams do the first one. Uh the spec as source is still something aspirational. So uh it doesn't work yet. Uh and most

[4:42] of the spec-driven uh tools that I will show you uh they are something in the middle. So like spec-anchored um about the workflows and the uh how the spec spec driven uh development tools define them uh they differ uh

[5:02] somehow. So for example Spec Kit uh from GitHub operates on constitution specify uh plans tasks uh and implementation. uh for Kiro or OpenSpec the um the workflow looks a bit different uh but from my perspective it's mainly about

[5:21] the about the names but the fundamentals uh keep the same. So most of these tools use something uh similar to a project memory bank. So this is the uh the context that will be used for um for implementation phase or planning phase.

[5:39] Uh that uh applies to all the features uh that we uh develop not only a current one uh we are uh we are specifying. Um the naming as you see is different and you can think of it like something similar to AGENTS.md or uh CLAUDE.md but

[5:59] something more powerful because it's um it's built into the uh the given tool. So the enforcements enforcement is higher than the the in this fi the config files I mentioned. So you can you can for example um um put like your your

[6:16] preferences for tech [stack] or the security uh and the most important things to you during the development um and uh how this um workflow looks

## [6:25] Spec-driven workflow in practice

[6:28] like when you go to implementation on a given uh on a given of a given uh feature. So first thing and the most important thing you should um you should focus on is the specification. So uh I'm going with the Spec Kit uh

[6:45] nomenclature. So first command is specify um and well we can we can start with something uh what you see on the left but most of the tool will create something what you see on the right. So

[6:58] something more strict and formal in language. And uh this is the thing the artifacts um that the uh given tool will uh will create to you or generate for you that you should review manually. That's something important because based

[7:14] on that on the specification it will just create or generate the uh plan and implementation for you. Uh that's why this is after after the uh specification is generated you should uh focus on reviewing it and correcting be uh before

[7:30] the next steps. And next uh next um items let's say in the workflow are most commonly plan and tasks. So for a given specification a given let's say scenario a plan is being um is being generated. So it's it's broken down into smaller

[7:49] pieces and more uh precise parts. So research or some API contracts etc. Then it's even uh even uh the granularity is even uh higher with the tasks when it's broken down into single tasks. Some of the

[8:06] tools uh can um uh perform these tasks in parallel. Um it's not so important because the whole thing is just generation. So it will take like 20 minutes to give you a working feature. And the last part is the implementation.

[8:21] Um so um and again I wouldn't spend much time here because uh well it's uh it's just generating code uh what you probably know from um AI assistance that you know. that uh all the things uh things that I mentioned before are um uh

[8:39] injected into context and also [steered?] by a given spec-driven development harness or tool. Uh so uh it's the enforcements are higher than in uh than in uh standard vibe coding. So your job here it shifts from typing the code to

[8:57] reviewing the code. So well uh still we have specifications but uh reviewing the code uh we don't have for now a uh an approach that replace fully replaces human being from that part. Um and uh something about the tooling landscape I

[9:15] wouldn't um focus on given tools but I group them into some uh some some uh areas let's say. So first group is the dedicated uh spec-driven development platforms or tools. Uh then we have uh lightweight frameworks and method

[9:33] methodologies. So the are more like manifests or of how you should use your um AI assistants. Then we have agent native things. So you can create spec-driven workflows using for example Claude skills and just DIY. So

[9:50] create specifications, put them in docs folder and um reference them from AGENTS.md uh might work in many many uh many cases maybe the uh simpler ones. Um so for benefits um

## [10:05] Benefits and drawbacks

[10:08] first the uh intent fidelity. So when we have the artifact as uh of a specification um the intent is clear you can even show it to someone else uh not just during it's not um forgotten during your AI

[10:25] assistant session. Um so uh you can you can and you should review the specifications before next parts. Uh this is the probably the part which we uh skip uh during just vibe coding. Uh what also is nice is that the context

[10:43] survives. So uh we don't need to um care about the uh the the sessions and plans that we create during vibe coding. The context survives because we have the specification files committed in our uh repository. Uh team alignment is also

[11:01] something uh additional. So additional benefit uh if we have a new hire in our team or we want to show or um um or assess the the specification with someone outside our team, we have this specification written down. We can show

[11:17] it to someone and of course um uh they are also used for implementation by AI agents. And now pivots are cheap because well if the change uh the specification changes we just regenerate basing uh on that. But the drawbacks well uh if you

[11:36] start using these spec-driven development tools you notice that the number of markdown files uh grows really fast and all these files are additional uh text that you need to review. Yeah. So there is additional overload. Um also as I

[11:54] mentioned the workflows are not standardized yet. Uh so there are there are um different approaches uh created by different tools and uh well you can quickly go into some into some maybe not a trap but I've observed some tools that

[12:13] were not developed anymore. Uh and then you need to switch to something else which is which might be much different. uh we also have a problem of spec drift. So uh while we have even precise specifications still non-deterministic

[12:27] LLMs can uh can ignore what you what we are telling them or our tools are telling them and the generated code uh and the specifications can just diverge um and well most of the tools uh that I use work nice in greenfield projects by

[12:46] but not so they are not so good in brownfield projects. So if you would like to start in the middle of the project, some of tools might uh not even allow that but not all of them. So there is also the question um well if we have the

[13:01] specification of everything of every feature or the whole or the whole project isn't that just a waterfall? Well, uh the answer is well it is somehow because um because we have the requirements gathered then we plan the

[13:17] tasks and we implement but the iteration loop is much faster. So it's not taking a year like in in some uh ancient projects but now it's more we can measure it in minutes or hours maybe. So we still can iterate fast uh if we pick

[13:34] the right uh tool for that. Um and I

## [13:38] Best practices and takeaways

[13:39] would like to share my best practices with you. So uh you should avoid using SDD for trivial tasks and this is the recommendation that you probably will find uh on the net until you just want to um learn a given tool. You can uh

[13:54] start small um and uh also what is important is to uh keep your the general memory of the tool. So for example uh for Spec Kit uh from GitHub it will be the constitution. Um first you should uh take close look into what you put there

[14:13] and also you should evaluate if what you put there makes any difference uh because well if you put there some uh things that uh doesn't uh make a change then it's only a noise in the context. Um second thing is the uh spec

[14:32] authorship and specific specificity. So um I recommend um creating some specifications manually at first using maybe Gherkin or RFC 2119 uh language to um be just better to exercise in that. um then you can you can switch to you

[14:53] can switch to for example OpenSpec or or Spec Kit which will create that for you. Um but uh you should uh create a skill uh in yourself that uh that will help you uh also reviewing the specifications created by the AI. And um

[15:14] um you should also always verify the specification files and plan and tasks files uh as well before hitting implementation because if you will make a mistake there the code generated uh might be just a trash sometimes and you

[15:28] will just waste time and tokens. Um u and uh after the the point two when you will be just good in creating specifications you shouldn't edit them uh manually. Why is that? Because if you chat with the AI assistant on a given

[15:46] specification, it can find some more um ambiguities than you will find. So, it's good to cooperate with AI assistants in um in uh creating and and uh editing the specifications as well. Most of the tools have something um additional to

[16:04] standard workflow uh that help you uh with that. And uh the last thing is you should share your spec specifications with uh managers or maybe with your product owner. Um just to just to uh check if this if it is readable uh by a

[16:23] normal standard human being. And uh it's also worth uh remembering that specifications were meant to uh close the gap between the business and uh the engineering. And you probably know this uh this approach from example from

[16:39] behavioral driven development when uh a similar specifications are created. Um so key takeaways from today. Um now we see that the bottleneck moved. We no longer type code but we describe the intent precisely more precisely uh then

[16:58] the results are better. Uh now the specification is becoming the source of truth. Maybe you are in the middle of this of this uh process. Um but we can treat the code generated as maybe not yet as artifact uh or like a compiled

[17:14] binary but something which can be easily easily modified by AI. Uh what is important specs survive across agent and agents and sessions. uh no more context decay and uh what I recommend to you as a starting point create your EARS uh

[17:33] language specification manually first then check some dedicated tool from my experience OpenSpec seems to be the most flexible for now because you can start even in the middle of your project um so that's uh that's the takeaways

[17:47] from my presentation uh if you uh liked this content please hit the like button uh and don't forget to subscribe our channel, share uh the video and if you have any questions or thoughts uh don't hesitate to comment. So, thank you very

[18:03] much for today. Bye.
