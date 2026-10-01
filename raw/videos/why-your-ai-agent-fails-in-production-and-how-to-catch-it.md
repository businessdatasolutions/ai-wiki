---
title: "Why Your AI Agent Fails in Production (And How to Catch It)"
video_id: wPdoZRbvaF4
url: https://www.youtube.com/watch?v=wPdoZRbvaF4
channel: Google Cloud Tech
channel_id: UCJS9pqu9BzkAMNTmzNMNhvg
channel_url: https://www.youtube.com/channel/UCJS9pqu9BzkAMNTmzNMNhvg
publish_date: '2026-09-30T08:04:16-07:00'
upload_date: '2026-09-30T08:04:16-07:00'
category: Science & Technology
duration: '26:07'
length_seconds: 1567
view_count: 8981
is_live: false
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
chapters:
  - {title: "Intro", start: '0:00', start_ms: 0}
  - {title: "The AI Agent Clinic: Eval Edition", start: '1:02', start_ms: 62000}
  - {title: "Meet DocsHound, a LangGraph Agent", start: '2:11', start_ms: 131000}
  - {title: "Making Agent Traces Evaluation-Ready (OTel & OpenInference)", start: '3:40', start_ms: 220000}
  - {title: "Beyond the “Vibe Check”", start: '5:02', start_ms: 302000}
  - {title: "The 60-Minute Challenge Begins", start: '5:51', start_ms: 351000}
  - {title: "Step 1: Mapping Agent Architecture with Antigravity", start: '6:47', start_ms: 407000}
  - {title: "Step 2: Setting Up the Open-Source Agent Eval Tool", start: '11:18', start_ms: 678000}
  - {title: "Measuring Quality, Latency & Token Cost", start: '17:14', start_ms: 1034000}
  - {title: "Step 3: Translating Quality Definitions into Metrics", start: '18:34', start_ms: 1114000}
  - {title: "Step 4: Visualizing Results & Spotting the 0.33 Failure", start: '21:40', start_ms: 1300000}
  - {title: "Finding Where the Agent Needs Improvement", start: '22:36', start_ms: 1356000}
  - {title: "Why Evals Change How You Build Agents", start: '24:08', start_ms: 1448000}
  - {title: "Are AI Agent Evals for Everyone?", start: '25:03', start_ms: 1503000}
description: |
  Manual code  tweaking isn't a testing strategy. Here is how to actually evaluate AI agents for production. In this episode of AI Agent Clinic, Google Cloud engineer Dani Zamora and Matthew Feroz (Merge) take DocsHound, an open-source LangGraph agent, and build an end-to-end evaluation pipeline in 60 minutes.
  
  🔗 Repositories & Resources:
  • Open-Source Agent-Eval Toolkit (GitHub):  https://g.dev/cloud/agent-eval 
  • DocsHound Agent Code: https://g.dev/cloud/docshound 
  • Gemini Enterprise Agent Platform Docs: https://g.dev/cloud/agent-evaluation 
  
  Most autonomous loops look great in local demos but fail silently in production. In this hands-on clinic, we compress weeks of testing setup into one hour by:
  1. Mapping agent execution flow and inner workings using Antigravity
  2. Standardizing multi-turn traces with OpenTelemetry & OpenInference (making your evals work across agentic frameworks like ADK, LangGraph, CrewAI, AutoGen, or custom implementations)
  3. Pairing custom LLM-as-a-judge evaluation rubrics and deterministic checkers for quality and performance assessment
  4. Additionally, tracking  signals like: latency, token usage, and API cost
  5. Ensuring zero vendor lock-in by building on open-source standards
  
  Along the way, our automated scorecard catches a blind spot: a 33% documentation quality score that while eye-balling the results we initially missed.
  
  Chapters:
  0:00 — Intro
  01:02 — The AI Agent Clinic: Eval Edition
  02:11 — Meet DocsHound, a LangGraph Agent
  03:40 — Making Agent Traces Evaluation-Ready (OTel & OpenInference)
  05:02 — Beyond the “Vibe Check”
  05:51 — The 60-Minute Challenge Begins
  06:47 — Step 1: Mapping Agent Architecture with Antigravity
  11:18 — Step 2: Setting Up the Open-Source Agent Eval Tool
  17:14 — Measuring Quality, Latency & Token Cost
  18:34 — Step 3: Translating Quality Definitions into Metrics
  21:40 — Step 4: Visualizing Results & Spotting the 0.33 Failure
  22:36 — Finding Where the Agent Needs Improvement
  24:08 — Why Evals Change How You Build Agents
  25:03 — Are AI Agent Evals for Everyone?
  
  
  Watch more of the AI Agent Clinic →  youtube.com/playlist?list=PLAz2I7PJjFtA 
  🔔 Subscribe to Google Cloud Tech → https://goo.gle/GoogleCloudTech
  
  #GoogleCloud #LangGraph #AIAgents #OpenTelemetry #SoftwareEngineering #GenerativeAI # AIDevelopment #OpenSource #Antigravity #GeminiAgentPlatform #GeminiEnterprise #AgentEvals #AgentsCLI
  
  Tech Stack Featured: LangGraph, OpenTelemetry (OTel), OpenInference, Gemini 3.7 , Python
  Speakers: Dani Zamora, Matthew Feroz
  Products Mentioned: Antigravity, Gemini, Google Cloud, Gemini Enterprise Agent Platform (Vertex AI), Agents CLI
notes: |
  Acquired 2026-10-01 via youtube-transcript-skill, the first fetch after the
  view-model transcript-panel fix (commit 7a2a4c7). 251 ASR segments, complete
  0:00-26:04 of 26:07; 14 creator chapters. Stills manifest alongside:
  why-your-ai-agent-fails-in-production-and-how-to-catch-it.stills.md.
  ASR cleanup at acquire (names checked against the description and the
  on-screen slides): Antigravity (anti-gravity), LangGraph (langraph),
  DocsHound (Docs Hound / doc count / Doc Sound / Doxound / Doound / Docound /
  dogs hound / dox count), agent-eval (agent evil / agental / agent table), ADK (APK / ad),
  CrewAI (crew), OpenTelemetry / OpenInference, Vertex AI (vert.xi / Vert.x),
  T3 Code / OpenCode / Pi (g3 code / op code / PI), evals (evils / evos /
  evolves / "email out"), managed metrics, custom LLM judge (custom element
  judge), autorater(s), groundedness, Dani (Danny), Matt Feroz (Matt Fero),
  agentic tooling (aic tooling), GUI (guey), agent (age). "evalu.jl" at 20:17 is
  eval_config.yaml, read from the screen (stills 33-35).
  Left verbatim, unclear: "let's use 2,000 metrics like Justin" (19:25),
  "a bunch of your surveillance running" (25:03), and "it's the open code that
  you created" (7:07): the existing scenario was the ADK one (still 23), so
  "open code" there may not mean OpenCode.
---

## [0:00] Intro

[0:00] Everybody says evaluations are all we need. Evaluating. Evaluation. Evaluation.
[0:06] In this episode of the AI agent clinic, we're going to show you how you can build evals in four simple steps. Step
[0:13] one, pointing Antigravity to the agent source code so it understands its inner workings. Step two, we will use an
[0:20] evaluation toolkit [music] that reduces the setup from weeks to one single hour.
[0:26] Step three, we will teach Antigravity [music] what quality outcome looks like.
[0:31] So it helps us curate the perfect eval metrics. Step four, we will actually run evaluations and get a quantified
[0:38] direction to [music] improve the next version of our agent.
[0:41] I honestly think like having eval here and just like [music] looking at them makes me want to just go back and start playing with my agent again and like changing the system prompt, changing as
[0:49] much things as I can just to see how it works.
[0:51] I am Dani, your host, [music] a Google engineer obsessed with agentic tooling. This is the AI agent clinic, the eval edition.

## [1:02] The AI Agent Clinic: Eval Edition

[1:02] Hi everyone, welcome to the agent clinic. Right now, this is going to be an episode completely focused on evaluations. What is the problem? We know eval is all we need.
[1:12] Mhm.
[1:12] But how to actually do them is the thing, right? No one tells you what data should you use to test. No one tells you
[1:19] how to actually test it, which evaluation tool to use. So, we're actually going to solve that issue today if it's okay with you. Yeah, for sure.
[1:27] So, Matt, can you introduce yourself?
[1:29] Yeah. Hey everybody, my name is Matt and I'm a developer advocate at Merge.
[1:32] Today, I'm bringing in DocsHound to the agent clinic, which is a tool to help you create documentation for your open source GitHub repositories.
[1:40] The agent, it's a LangGraph agent, right?
[1:43] Yeah. So, that's something that I was actually a little bit surprised about.
[1:45] I'm bringing like a completely different uh ADK and like tool uh to the Google agent clinic.
[1:51] That is amazing. One of the things that I wanted to show today is that whenever you think about evaluation or whenever you think about deployment, you can use
[1:59] Google Cloud. It doesn't matter if it's not an ADK agent. Of course, everything we tested internally with ADK agents. Uh but also the team is constantly working
[2:06] to make it available for other frameworks too, right? So, okay, let's let's see it in action. All you need to do, and I wanted to make it super simple, is you should just be able to

## [2:11] Meet DocsHound, a LangGraph Agent

[2:15] paste in a GitHub repository and an agent will go out, research the repository, look through the documentation, find any gaps, and then it has like a beautiful GUI over here
[2:24] that you can interact with and actually fill in those gaps and open PRs for.
[2:28] Okay. Can we see in here what's happening? So, the agent is working.
[2:31] Yeah. Uh, essentially, you can see over here all of the traces of what the agent's doing. Uh, you can see that it actually took a look at 50 issues and 30
[2:38] PRs and actually traced through the official Google documentation to see what issues there were. Um, it looks like the agent found a gap about audio
[2:46] stream and support. So, I'm not going to read through the entire piece of documentation over here, but if we take a look at the finding, we can see that
[2:53] this is exactly where documentation is missing this implementation. And then we can actually find the exact PR where that issue was open and merged.
[3:02] Wow. Yeah, this is amazing. Yeah.
[3:05] So, that's the end of the episode, folks. This is already amazing. We're not going [laughter] to do any evaluation.
[3:10] I think I think the cooler thing is like actually going through seeing how like everything works. You can see here like you can actually edit the markdown, edit
[3:18] how like the actual documentation is going to look. At the very end, you can approve and open and then you can see like what it looks like and then you can
[3:25] like merge it in as you can see over here like it's preparing and open a pull request.
[3:30] Yep. And you can just publish it and then it should it should work. Okay, let's see if it opened.
[3:36] Yep, it looks like it opened up a pull request. So amazing.
[3:39] Yeah. So I will say this uh telemetry and these traces over here, I actually built out the agent to like publish all those and save those in a very compatible manner.

## [3:40] Making Agent Traces Evaluation-Ready (OTel & OpenInference)

[3:49] Making the telemetry compatible. Can you tell us a little bit more about OpenTelemetry, OpenInference?
[3:54] Yeah. Yeah. The way that OpenTelemetry and OpenInference works is they're just like uh converters for you to get all of your agent traces data and everything
[4:02] like that all into one place that can then be like shared and spread out to like any other runtime or any other ADK or something like that.
[4:09] Yeah. Like basically and this is what we're going to do today is if you use a LangGraph agent, if you use an ADK agent, your agent may have a specific kind of
[4:18] of outputs, right? It might have a specific kind of telemetry. OpenTelemetry is a standard for the standard. And then why can't we use open
[4:25] telemetry? Because maybe uh the LangGraph agent, the CrewAI agent, the ADK agent stream differently, right?
[4:30] Maybe the telemetry, the spans and the arguments might be different. So in order to solve that, we use OpenInference. So OpenInference is a standard for that. Yes.
[4:38] So this is a a knowledge nugget. Yes.
[4:41] So uh right now what you did is already make your agent OpenInference compatible and that's something that you can do like with any kind of framework.
[4:48] Why did you do it? So that whenever we did evaluations, we don't need to redo the work if you change that inner workings, right?
[4:56] The it doesn't matter how it like looks at the very end. It's like the actual data itself is all compatible.

## [5:02] Beyond the “Vibe Check”

[5:02] Matt, you have a lot of experience with open source. You have a lot of experience knowing specifically if this agent is working correctly.
[5:09] [clears throat]
[5:09] But if you ask me for example and I needed to evaluate your agent, that's going to be a little bit difficult, right? So right now, for example, if you make changes in your
[5:17] agent and you test a new version, you're going to vibe it, right? You're going to feel like, "Yeah, it's what looks right. Yeah, [laughter] I understand."
[5:25] Uh the problem is for example if I want to contribute to this and I create a pull request and [clears throat] I do some improvements in my head of the
[5:33] agent. What if that isn't what you expected? there needs to be a way so that we can translate what you have in your mind as quality to something that we can run as
[5:42] actual numbers so that if you change something or if someone else changes something you can always measure those improvements or even regressions. Right?
[5:49] We don't want regressions in the agent.

## [5:51] The 60-Minute Challenge Begins

[5:51] So here's the challenge. We will have 60 minutes to run evaluations on Matt's LangGraph [music] base agent. First, we will be pointing Antigravity to the doc
[6:00] count source code. You will see how you can guide a coding [music] agent to create useful traces to assess or evaluate the agents performance. Second,
[6:09] we will use a tool created by a Google Cloud team to scaffold and run evaluations using Gemini Enterprise Agent Platform and we will adapt this
[6:16] toolkit to be compatible with any [music] agentic framework. Third, we will jump start another session to help us translate Matt's quality [music]
[6:24] definitions into actual evaluation metrics. And we will learn a reproducible pattern which uses AI to create the metrics quickly [music] while
[6:32] always guided by human expertise. And finally, we will show how we can visualize our evaluation results. [music] So 60 minutes.
[6:40] Are we recording right now?
[6:42] I think we're recording. Okay. So 3 2 1 60 minutes. Okay.
[6:46] Okay. Let's do it. So first of all just for the setup in here we have Antigravity. Okay. So we're going to start using it. Probably you have used it in the past. [clears throat]

## [6:47] Step 1: Mapping Agent Architecture with Antigravity

[6:54] Uh so we have already downloaded your repository. Yep.
[6:59] And what we're going to do is first tell Antigravity to analyze the traces. We have already here up and running your
[7:07] code. So this is a perfect thing to start with because you have already a scenario right that it's the open code that you created it. That that's what we
[7:14] need for evaluation. But we need a couple more scenarios for that.
[7:17] So in this case, for example, what we're going to do is just ask if we understand that scenario that you have and let's ask it to create more. Right. So for
[7:26] that, first let's prompt it to um hi friend. [laughter] You always start off with hi friend.
[7:32] Hi friend. Um can you please analyze the traces from the run and understand how the agent is working?
[7:44] So in this case, what we're going to do is try to use um Antigravity to understand the traces. Yeah. And to tell us what kind of scenarios we can
[7:52] use so that we can actually like nicely evaluate it. Yeah, for sure. Does that make sense?
[7:56] I think like yeah, having an LLM as a judge like actually go through and and look at traces is probably going to be like the way that most people are going to be improving their agents in the
[8:04] future. So I'm excited that we're doing this now because I definitely was not doing it before. [music] Okay.
[8:12] One of the things that I wanted to mention as we let this run is that we already have deployed your agent. Oh, sweet.
[8:17] So in here uh what I want to show you is how you can actually see this agent in the agent platform. Perfect.
[8:25] So in here we see this and we can go into our deployments.
[8:30] So in deployments we are already going to be able to see the DocsHound LangGraph agent. Yeah, look at that. It's right there.
[8:35] One of the things that I want to to make sure is that we are able to test the agent before deploying new versions of
[8:42] it. Yeah. Right. So in here, let's just go to the logs and let's try to see if it can actually like analyze those logs
[8:51] to make sure it's it's analyzing everything. You just got to let it work sometimes, I guess. Yeah.
[8:55] So this is the part where we take coffee, where we chat about live, where we let it.
[8:59] Eight different agents also going on at the same time.
[9:01] Yes. Yes. Analyzing the stuff. And here we see that it's thinking and it's just kind of like okay oh wow okay that is why yeah [laughter]
[9:09] an entire like documentation piece okay this makes sense yeah yeah so I didn't realize that Gemini could render Mermaid inside
[9:17] that's actually pretty cool so it's cool to see that's the entire architecture of the actual application so one of the things that we want to do is
[9:26] this is specifically for one of the runs right so as the scenario of the ADK agent We want
[9:33] to create several extra scenarios. Do you typically like have a list of repositories that you think it could be nice? Oh my god. Yeah, that'd be great. Yeah.
[9:41] So, I think some of my favorite uh open source repositories that I can mention are like T3 Code, which is uh a harness for harnesses that like I'm a maintainer
[9:48] of and I use a ton, OpenCode, which is another open source AI agent harness, and then uh Pi agent, which I think is like one of the really the simplest AI
[9:57] agent harness. And like it's again one of my favorites. I have too many favorites.
[10:01] Okay. So why don't you like or type down in here for Antigravity so that you can have it create scenarios like understand how scenarios are used so that we can
[10:09] create similar scenarios as the ADK one uh for projects that you are mentioning.
[10:14] Yeah for sure. So I can just say can you run DocsHound on T3 Code and create it in a reproducible way.
[10:21] Yeah. [music] In in the meantime also we can start seeing what it created in here. Mhm.
[10:29] So this is the high level architecture and this is a great part about using Antigravity.
[10:34] So if I for example don't have like any idea of how DocsHound works we can actually use this to explain the code to us right so not only based on
[10:42] the source code itself but also based on your telemetry. Yes.
[10:45] So in here we can see we have a DB there's this analysis on how it works under the hood. If we're [clears throat] going to set up evaluations for your agent and then people like me or other
[10:54] people that are contributing to DocsHound [clears throat] want to run, it needs to actually reflect what you have in in DocsHound. So in [clears throat] here we
[11:02] can see also more of the information like you can go over this and see if it's actually like working in terms of it understood specifically your agent.
[11:11] Oh, it's already trying to run evals.
[11:13] We're going to see what it does. But let's see it. Yeah. Yeah. [laughter] Let's see. Let's see it in action. So Matt, [clears throat] we are running out of time. We're going to let right now

## [11:18] Step 2: Setting Up the Open-Source Agent Eval Tool

[11:21] Antigravity think a little bit, but I just wanted to quickly show you this tool. I created this with my team. Okay.
[11:27] So, the idea of this tool is that we can have those steps of evaluation running. Yeah.
[11:33] Um in a reproducible way, right? Like to place some of the knowledge in here. So, we're going to try to use that repository. So, we have it as an open
[11:40] source tool. Now that you love open source, I know that you love open source. That makes me happy.
[11:45] So, in here we have agent-eval. As you see, we are actively contributing to this.
[11:49] Like just last week, a colleague pushed some things.
[11:52] So the idea of this is that uh we can scaffold the evaluations and we can also run evaluations in a way that we know it works. Right? For example, Antigravity
[12:00] is trying to run evaluations itself. But what we're going to try to do is ground it a little bit into something that we know will actually like make sense, right? That makes sense.
[12:09] So that's why we created this. One of the things and why I told you that you helped me with my backlog is because this right now is tested with ADK. Yeah.
[12:17] So what we're going to do is try to run this part of the evaluations but try to run it with LangGraph. Yeah. Yeah. This sounds good. Yeah.
[12:25] So I think we probably need to take a step back. We started like going right into the DocsHound code. I already have a clone version of this repository.
[12:33] Why don't we don't go there?
[12:34] Yeah. And we actually uh try to prompt Antigravity to understand this code and see how it can make that connection.
[12:41] Yeah, sure. Of using agent evaluation with the LangGraph agent.
[12:44] I also really think that like you're hitting on a really important note like agents being able to like understand the context of these like great open source tools that you already like built and things like that.
[12:53] Yeah.
[12:53] Like that's the whole philosophy behind DocsHound as well. It's like you can literally take anything that's like available on the internet, point an agent at it, understand exactly
[13:02] how it works, and then create outcomes for yourself that will improve your software as well.
[13:06] So, let's start in here. Uh, I'm going to start another chat just to tell Antigravity like, hey, [music]
[13:15] [music]
[13:17] I think in here you can also use voice, but for right now, let's just see. Okay, it's analyzing the tool and it's already seeing how it can help us uh use these
[13:26] specific scripts that we already have to evaluate your agent. On the other side, we also have an Antigravity agent understanding the traces to see how it can help us generate scenarios.
[13:36] Do you want to check how it's doing?
[13:37] Let's check how it's doing. So in here, it has identified the repositories. It has configured the pipeline parameters and it has executed the DocsHound across
[13:45] these three specifications. So Pi, T3 and OpenCode.
[13:49] Okay, perfect. So we understood that. So this is a summary of the execution. This is specifically for this scope 50 issues. Okay.
[13:56] So right now we have made sure that we actually have data to evaluate it. So in real life what happens is that you need of course more examples to make sure
[14:04] that we have the appropriate data to run evaluation. Right now let's just use this that we currently have. Yeah.
[14:10] So the following files have been created. Okay. It created an eval set.json. Amazing. So it already created a lot of data for us.
[14:19] Yeah. to us to look at. Yeah. [laughter] Yeah. To us to look at. If we actually go into here, we can see the type of data that it created. Okay. So, in here
[14:26] you can see like this is the actions that it took. This is the reason of the actions.
[14:30] So, let's just go in here and let's see how this [music] is doing.
[14:42] So, in here it's already on the DocsHound folder. So it can already see what the other agent has created and that data it has created.
[14:49] So now you think it's going to run it on that data.
[14:51] Yeah. So right now for example it's analyzing that we have a trace converters. This is what I was this is what I was talking about.
[14:57] Yeah that's what I was talking about. So whenever you have for example ADK it expose some certain kind of traces from the traces. We get a lot of information
[15:04] like metadata like the latency token usage, cached tokens and we also get information from how the agent is working inside. So where we're
[15:13] getting all that information is from the traces. Gotcha.
[15:16] So in this case specifically for agent-eval what we did is that we had the traces specifically for ADK.
[15:23] Yes. Yeah. And our goal now is to make sure that anything can Yeah. So we're going to try to see if we can do two collaborations. The
[15:31] first collaboration is actually doing evals for DocsHound and the part of the deployment to cloud that we already did.
[15:38] And the second piece is is if we can collaborate to agent-eval. Yeah. to actually make it compatible.
[15:43] Yeah. So, wow. We're actually doing a lot in this. [laughter] That's great. I think eval are like the next step in making sure that agents
[15:51] work, right? Like if a company creates their own harness or is like using their own tools, having those robust evals and like making sure that they understand what the agent's doing is how they're going to improve it later on the future.
[16:01] Yeah.
[16:01] So, we are letting this work Matt and [clears throat] you can see that we have a lot of things happening in here. Yes.
[16:07] So, in here it come up with an implementation plan. Yeah. So as you can see we have LangGraph an OpenInference trace conversion for agent-eval. That is amazing. Yeah. Perfect.
[16:15] Okay. So as you can see it already identified that we have a local version of the tool. We also have a local version of DocsHound already installed.
[16:22] That is where our other agent is working on running the traces so that we can have data to work with. Perfect.
[16:28] And then in here you're going to see the trace converter enhancements blah blah blah. Some things that it needs about our approval.
[16:34] Yeah. I love that it has this architecture overview every single time because you can just see exactly how it's going to be actually implemented. Yes. Just so nice.
[16:40] Right now, for example, we let it run as it is because we are time constrained.
[16:44] Yes. [laughter] Half an hour to go.
[16:46] Uh so that's why we just let it do its thing. Y but it understands pretty well and it also lets you as you can see like add
[16:53] small comments to the implementation plan if you think of them. I see. Perfect.
[16:56] Yes. So imagine making all of these things by ourselves. Yeah.
[17:00] This is kind of like crazy, right? In my mind this is like just so crazy. Like so many things that we need to consider.
[17:06] This is one of the things that I like about Antigravity. Yeah, if you see here, this is helping us with a lot of things that we would have to consider if doing these conversions. So

## [17:14] Measuring Quality, Latency & Token Cost

[17:14] the trace for example, mapping the data also to something that is acceptable by the Vertex AI evaluation service also for example how to extract the deterministic metrics.
[17:24] Yeah.
[17:24] And that is a good cue for me to tell you that I talk about Vertex AI eval as a judge. Yes.
[17:32] But the thing is that we don't only need those kind of signals whenever we're working with agents. We don't only need to measure quality, we also need to measure some things that are like
[17:40] performance based in the sense of latency. Yeah.
[17:43] Token usage cost if you make a change and you were saying that earlier.
[17:47] Yeah. So like I was saying, oh why don't we just try adding Gemini 3.7 Pro or like the strongest model possible to it and we'll see how it does. And you were
[17:55] explaining to me like, hey, having like the information and the background behind how the agent's performing now with this smaller agent might help us like be able to decide between which one to use or not.
[18:05] Exactly. Okay. Okay. So it finished. So this is the conversion of OpenInference OpenTelemetry for evaluation with Google Cloud tool is complete.
[18:12] Nice. High five.
[18:14] Okay. So OpenInference OpenTelemetry implemented. Perfect. Perfect. Test verification. All CLI is passing. Running evaluation on DocsHound traces.
[18:23] Amazing. Okay. So this already let's point it to where the other model yes has already created the traces.
[18:32] So let's just say it alone. agent-eval needs to work the data but it also needs the metrics. So why don't we focus right

## [18:34] Step 3: Translating Quality Definitions into Metrics

[18:41] now on creating good metrics so that we can actually go over that file and good metrics I mean take into
[18:49] account the code of DocsHound, the LangGraph code of the inner workings of the agent and also [clears throat] you were saying quality in terms of how
[18:58] the information is displayed is important to us and confidence and confidence or groundedness
[19:04] [music]
[19:09] So it's creating. Did you see like already like all these metric definitions?
[19:12] Yep. And we can take a look at them afterwards. Yeah.
[19:14] What's your opinion? What is like the best way to actually eval agents? What have you found from your experience?
[19:19] That is a good question. We already have a bunch of managed metrics. What I recommend is starting simple. Yeah.
[19:25] Typically when we want to start evaluating agents, we say like let's use 2,000 metrics like Justin. It's impossible to actually like measure know which one's the most valuable. Exactly.
[19:35] So I would say start with some of the managed metrics like tool use quality right use use the trajectory quality
[19:43] like if if it's actually following an expected trajectory it's if it's actually calling correctly the tools those things are important to do
[19:50] and then also my biggest recommendation is sitting down with the developer sitting down with the user of agents for example and seeing what quality means
[19:58] for them for sure like having the the expert who understands the vibe like to be able to say like that doesn't look right Exactly. That doesn't look right. Right.
[20:07] So in here it already created this config yaml.
[20:11] So we can see in here we have your back end. We have your app. We have the traces. We can see that the agent has already created the test folder. Right.
[20:17] Yeah. Nice. I didn't see that folder there before. So it has already eval_config.yaml.
[20:25] So if we see these metrics, you're going to see that it already pre-selected some metrics for us.
[20:30] Perfect. Yeah. Question answering quality and this is a managed metric. Wow. So this is a metric that comes directly from the Vertex AI API.
[20:35] Perfect. That's crazy. So yeah, you guys already built it out essentially and it just puts those metrics straight into my agent.
[20:41] Exactly. Wow. Exactly. We can see in here that it has chosen some managed metrics, but it has also created some custom LLM judge. Awesome.
[20:48] So in here, as you can see, this is a criteria that I was mentioning. Right.
[20:52] So in here, these are things that it defines as criteria. Structural, formatting, actionability, technical precision. I really love the code blocks
[21:00] one because I feel like a lot of my docs weren't actually creating code blocks when they need them. So this is a great metric I feel like. Good job Antigravity. Yeah. Go ahead.
[21:07] Yes. So we also have for examples LangGraph inner workings and we also have deterministic python function checkers.
[21:13] Yeah. I think honestly that's pretty good. I just starting from there. I think we can run these evals and it would be great.
[21:18] Amazing. And you can see that it started like placing everything in here. The data set that we're going to use for evals.
[21:23] So in here it added your scenarios of how to run this for OpenCode. Uh oh, we run out of time. [laughter]
[21:32] No, that's it. Yeah. Okay. Please give us a break. Evaluations is super complicated.
[21:37] Yeah. And like there's so much that we're doing right here.

## [21:40] Step 4: Visualizing Results & Spotting the 0.33 Failure

[21:40] Okay. Okay. Great. Okay. Looks like it's done. Let's check it out. Okay.
[21:43] Let's see. Let's see. Okay. It says, "DocsHound evaluation complete. We have created, configure, and run automated evaluation suite for DocsHound." Okay. Why don't we just open up the HTML
[21:50] and take a look at it? I think it should be done, right? That is amazing. Open the [music] HTML.
[21:59] So from the metric that I chose, so we're not going to have time to actually like evaluate those metrics.
[22:05] How do you feel about this beautiful way of seeing the beautiful Yeah. Look at the Google colors, everything like that. We probably spent a lot of time designing
[22:11] [laughter]
[22:12] this HTML. Yeah. Yeah.
[22:13] This is super pretty, Matt. Yes, we already have this evaluation metrics in here. If this makes sense.
[22:18] Yeah. I'll say like it's doing good in some places, but some places not so much. It looks like the DocsHound documentation quality is actually pretty low. That's surprising to me. like I
[22:27] kind of now want to go back and actually change and update my agent to maybe make it perform a little bit better.
[22:32] You do have the numbers to actually go back to your code and have the direction of how to improve it, right? We achieved our purpose.

## [22:36] Finding Where the Agent Needs Improvement

[22:38] Yeah. Nice. [laughter] Okay. I definitely have to spend a lot of time um updating my system prompt, maybe changing the harness itself. But yeah, now that I know that, hey, maybe the
[22:46] documentation quality is a little bit low, I can go back and actually change my agent cuz like that's a complete blind spot that I had.
[22:52] It can be both ways. probably your code needs improvement or the way we are evaluating also may need improvement, right? The metrics you can you can change them in here. If we go over
[23:00] quickly by the report, you're going to see also like all the deterministic metrics.
[23:03] Yeah. And then questions. Wow, this is such a beautiful like actual score heat map. You can see like Yeah. I want to see you how you explore it because this is like this gives me a lot of happiness.
[23:12] Yeah. Like Yeah. Like that. Um per question deep dive. You can actually look at how all
[23:20] of these explained everything. The the front end is beautiful. It actually shows you each and every single trace where it failed or passed or something like that.
[23:27] Yeah. In here, for example, there's an error rendering the prompt. So, there's maybe like an error within how we are doing that. Yep. That's no worries.
[23:34] And this is for the autoraters specifically, right? We can see that that is the autorater metric. Perfect.
[23:39] Uh [snorts] but for the rest of it, the converter somehow still needs a little bit of tweaking.
[23:44] Yeah, that's absolutely fine. But I'm so glad that we at least able to check it out and see. It looks like you can also do iterations and see how it works as well. Exactly. In in the meantime, while
[23:53] that fixes, how do you feel about being able to see this in in action, the evaluations?
[23:58] I honestly think like having evals here and just like looking at them makes me want to just go back and start playing with my agent again and like changing the system prompt, changing the model,
[24:06] changing as much things as I can just to see how it works. It's so nice to have the knowledge that I have an actual framework that I can just jump back into and like update and change and that like

## [24:08] Why Evals Change How You Build Agents

[24:14] this is all pretty much here for me because it is open source and I can just go back and test it. Yeah.
[24:18] Yes. Yes. Exactly. and you can contribute to it. Yes.
[24:25] [music]
[24:25] What do you think are evals for everyone? I think yes and no. Yes or no? So like I'll explain my point, right?
[24:32] Like as a solo developer and somebody who really interacts with developer community, I feel like evals are great if you're trying to like get something into production or like using an
[24:39] enterprise. But like with this tool right over here, I'm glad that I ran it and I actually have like the agent telling me exactly what I need to upgrade. But what if the model gets
[24:48] better tomorrow? Or what if like the harness changes or something like that?
[24:51] I think eval are for when you really need the agent to perform production. If I do own a company one day, I'd love to have this tool helping me alongside it
[24:59] and maybe I'll fork my own, you know, and like create something as well. So yeah.

## [25:03] Are AI Agent Evals for Everyone?

[25:03] And I think you kind of like own a company right now because you have a bunch of your surveillance running. Yeah.
[25:08] So if you want to give a little bit more freedom to develop, they can have this dashboard up and running for you just to improve.
[25:17] Okay, great. Yeah, I'll try that out.
[25:18] You can try that out. We are done with this episode. We have finished and we have already like this beautiful dashboard. We can already know what the agent specifically needs to be improved.
[25:27] How do you feel about that?
[25:28] I feel great. I think it's like the best feeling ever that I know I can eval my agents using an open source tool and I can actually point my agents to this tool itself to maybe improve it. Matt,
[25:37] is there anything else that you would like to tell the audience?
[25:39] Yeah, I will say I do create technical content on YouTube. You guys can follow me, Matt Feroz, for more videos about this open source technology that I'm
[25:46] using, a lot about the ways to make your developer experience more agent-friendly and yeah, just more AI stuff in general.
[25:54] He's amazing. Follow him. And that's it, Matt. Thank you so much. We did it. We did it. See you on the next video. Yeah.
[26:04] [music]
