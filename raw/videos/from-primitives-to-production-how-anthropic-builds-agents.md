---
title: "From Primitives to Production: How Anthropic Builds Agents"
video_id: 8pzHCfsSaYQ
url: "https://www.youtube.com/watch?v=8pzHCfsSaYQ"
channel: "Databricks"
channel_id: UC3q8O3Bh2Le8Rj1-Q-_UUbA
channel_url: "https://www.youtube.com/channel/UC3q8O3Bh2Le8Rj1-Q-_UUbA"
publish_date: '2026-08-19T11:51:48-07:00'
upload_date: '2026-08-19T11:51:48-07:00'
category: "Science & Technology"
duration: '25:20'
length_seconds: 1520
view_count: 1168
is_live: false
thumbnail: "https://i.ytimg.com/vi/8pzHCfsSaYQ/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLDsE0kjS1Hk6abqr8yys5kIHqPj9g"
keywords:
  - "#databricks"
  - "#agentic"
  - "#aiobservability"
caption_tracks:
  - language_code: en
    name: "English (auto-generated)"
    kind: asr
    is_translatable: true
chapters:
  - {title: "Evolution of LLMs", start: '0:00', start_ms: 0}
  - {title: "Defining an Agent", start: '2:45', start_ms: 165000}
  - {title: "How Claude Code Works", start: '3:15', start_ms: 195000}
  - {title: "The Claude Agent SDK", start: '5:50', start_ms: 350000}
  - {title: "Utilizing Agent Skills", start: '6:58', start_ms: 418000}
  - {title: "Benefits of Sub-Agents", start: '8:50', start_ms: 530000}
  - {title: "Governance and Safety Hooks", start: '11:10', start_ms: 670000}
  - {title: "Evaluation with Evals", start: '13:56', start_ms: 836000}
  - {title: "Site Reliability Engineer (SRE) Agent Demo", start: '16:48', start_ms: 1008000}
  - {title: "Introduction to Managed Agents", start: '24:01', start_ms: 1441000}
description: |
  Recorded at: Agentic + AI Observability Meetup | SF | April 9, 2026

  Speaker: Isabella He (Member of Technical Staff, Anthropic)

  Session: ​Skills and Security

  Large Language Models (LLMs) are evolving from simple "tokens in/out" processors into autonomous agents. This session breaks down the engineering principles and frameworks used at Anthropic to build agents capable of navigating complex environments without human-encoded logic.
  The talk highlights the transition from orchestrated workflows to modern agentic systems, featuring tools like Claude Code and the Claude Agent SDK.

  Key Takeaways:
  -Anthropic defines an agent as an LLM placed in a loop with a specific goal and a set of tools.
  -Effective agents are built using core primitives like code execution and web search that apply across any domain.
  -Developers use modular "Skills" to prevent context pollution by loading instructions only when relevant.
  -Systems utilize the Model Context Protocol (MCP) for external connections and sub-agents for parallel workstreams.
  -Security is managed through hooks for human approvals and restricted sandboxing environments.
  -Evals function as essential unit tests to provide objective measurements of agent quality.
  -Managed infrastructure abstracts the complexities of deployment so developers can focus on core logic.

  0:00 — Evolution of LLMs
  2:45 — Defining an Agent
  3:15 — How Claude Code Works
  5:50 — The Claude Agent SDK
  6:58 — Utilizing Agent Skills
  8:50 — Benefits of Sub-Agents
  11:10 — Governance and Safety Hooks
  13:56 — Evaluation with Evals
  16:48 — Site Reliability Engineer (SRE) Agent Demo
  24:01 — Introduction to Managed Agents
notes: |
  Acquired 2026-08-20 via the youtube-transcript skill (Playwright route), auto-generated (ASR) English track.
  Two scraper artifacts were present in this file's raw segments and were cleaned at acquire time:
  (1) YouTube's accessibility time label ("1 minute, 4 seconds") leaked into 184 of 194 segment texts and was stripped;
  (2) the ten chapter titles were appended mid-sentence into segment text and were removed from the prose (they are
  preserved as `chapters:` above and as body headings). Neither artifact appeared in the other five videos acquired
  in the same batch, so this looks video-specific rather than a general skill regression.
  ASR cleanups applied: "Enthropic"/"Anthropics" -> Anthropic; "cloud code" -> Claude Code; "cloud agent SDK" ->
  Claude Agent SDK; "sub aents"/"sub agents" -> subagents; "grap"/"gp" -> grep; "haik coup" -> Haiku;
  "page duty"/"pedag duty" -> PagerDuty; "SR bot" -> SRE bot; "progressive enclosion disclosure" ->
  progressive disclosure; "remove RF" -> rm -rf; plus several incident/instance confusions.
  Speaker (named in the description, not the audio): Isabella He, Applied AI, Anthropic. Recorded at the
  Agentic + AI Observability Meetup, San Francisco, 9 April 2026; published by Databricks 19 August 2026.
---

## [0:00] Evolution of LLMs

[0:00] Agents in Anthropic are actually very simply defined where essentially you want to give the model and lean in on model intelligence [music] as much as possible. And then as we see models get more and more intelligent.

[0:09] What we see is an evolution in how we think about agents in general. So agents today we think about as having essentially a task that you give it then you give it the same core primitives

[0:17] things [music] like code execution, file system, web search, to-do list. You put it into a loop and you can almost think about the power of Claude [music] code powering agents in any domain.

[0:29] excited to be here and talk about essentially Anthropic position and point of view on how to build agents.

[0:35] All right, so for today's agenda, the main thing that I want to leave everyone with is hopefully just speedrun exactly how Anthropic thinks about agents, how we build agents internally, how we

[0:44] govern and build effective agents, leverage evals, and also show you a quick demo at the end of an actual agent built on our Anthropic perspective on

[0:50] our agent SDK. A little bit of quick introduction. My name is Isabella. I'm on our applied AI team at Anthropic.

[0:56] Essentially what this means is that I spend about half my time working internally. So I've contributed to Claude Code designer news/init experience if you've seen that out in

[1:04] beta testing. I work on context engineering. So things like compaction and tool result clearing. But I spend the other half of my time working with

[1:11] our customers. So I work personally with a mixture of our big tech and startup customers and essentially work to see how we can help them stay on the

[1:18] frontier and leverage Claude in their models and build agents effectively within different domains as well. So let me go ahead and jump in into exactly how

[1:26] Anthropic looks at agents around as we're evolving from different models. As we've seen, LLMs have progressed very significantly and rapidly in the past

[1:34] couple of years. I'm sure a lot of you might know this chart already, but if we think back to first when the initial LLM started coming out, a lot of them were

[1:42] single LLM features. So essentially tokens in and then tokens out. And then we move to more of a workflow state where LLMs are essentially orchestrated

[1:50] by code. This was a little bit more complex where you essentially take the input of one LLM, you run some logic of it, bring it to another LLM and you

[1:58] chain together different LLM calls orchestrated by code. But this was still very deterministic relying on human encoded logic to guide LLMs around where

[2:05] they were going. But as we have seen models get more and more capable, that brings us to what we think about as agents at Anthropic, which is really

[2:14] where LLMs are actually deciding their own trajectories. So instead of a workflow style approach where you're encoding exactly where the LLM is going

[2:21] to go, agents actually essentially are able to look at complex environments, look at the tools it has at its disposal

[2:29] and essentially work in a loop in order to uh strive towards a particular goal without deterministic elements encoded in. So essentially just to break this

[2:37] down, I think there are a lot of different definitions of agents as you all might have experienced as well, but at Anthropic we kind of think about agents very very simply. Essentially 

## [2:45] Defining an Agent

[2:46] what an agent is is it is a large language model. It is then put into a loop. It uses tools at its disposal and

[2:53] it has a particular goal that it's optimizing towards. So if you look here, agents in Anthropic are actually very simply defined where essentially you

[3:01] want to give the model and lean in on model intelligence as much as possible and give the model the ability to change its own trajectory based on the information that it acquires. And then

[3:09] at Anthropic we've written a lot of agent loops. So specifically, one of our most popular agents is Claude Code. For those of you who love Claude Code, you 

## [3:15] How Claude Code Works

[3:18] might have experienced the power of Claude Code already with how Claude Code essentially leans on our Claude models to essentially enable developers to achieve

[3:26] tasks that they might never have achieved before. Claude Code, working and running Claude Code for hours on end. Can I get a quick raise of hands? How many people here have used Claude Code personally? Okay, lots of hands raised.

[3:37] Um, if we actually talk really quickly about what Claude Code looks like under the hood, I want to just quickly touch base on exactly actually how Claude Code

[3:45] works. Essentially, Claude Code has access to about 14 or 15 tools, things like bash, edit, grep, glob. And these are actually tools that you all have at

[3:53] your disposal in your terminal as developer as well. What a lot of agents did before Claude Code was essentially semantic search over a particular file,

[4:01] which is looking for things like keyword phrasing, and you had to feed it a specific file to edit. But Claude Code instead essentially has the same set of tools that you have access to as a

[4:09] developer. So if it wants to search for a particular file to edit, you don't have to tell it exactly which file to edit. You can run Claude Code on a codebase that is millions or hundreds of

[4:18] millions lines of code. And essentially Claude Code will use list, grep, glob bash commands to navigate the codebase just as you as a developer would. And then as

[4:25] we see models get more and more intelligent, what we see is an evolution in how we think about agents in general.

[4:31] I think a couple of months maybe around a year ago we thought about agents as needing very specialized domains across different expertise areas. So you had

[4:39] like a specialized coding agent that might be a Claude Code. We used to think you might need almost an entire new harness for something like a research agent or a customer service agent or a

[4:47] site reliability agent. But as we all might have seen just across different model launches, they're also coming out quicker and quicker. You see this

[4:54] progress accelerating. Where we are now is that with every new model that we see, we can unlock a whole new set of capabilities. So instead of breaking

[5:02] down agents by domain, we actually see that it's more effective if we just think about agents as this really almost general purpose but with essentially

[5:11] access to different tools that you can then tailor to specific domains. So agents today we think about as having essentially a task that you give it.

[5:18] Then you give it the same core primitives, things like code execution, file system, web search, to-do lists.

[5:23] You put it into a loop and you can almost think about the power of Claude Code powering agents in any domain. So Claude Code could power a customer

[5:31] support agent. It could power an incident response agent. It could power domains essentially beyond code but running the same core primitives of Claude Code giving Claude an access to a computer.

[5:41] So now let's go ahead and get tactical.

[5:42] I want to everyone to hopefully leave with just a little bit of a playbook of if you were to leave this room, how would you actually go and build agents?

[5:49] Um specifically the way that for instance Claude Code is built today. The Claude Agent SDK is a product that we offer at Anthropic. It is essentially 

## [5:50] The Claude Agent SDK

[5:56] the same building blocks as Claude Code, but allows you to put in your custom tools and custom system prompts and custom skills and essentially leverage

[6:04] the power of Claude Code for any agent that you might be building for your own domain. So, this involves things like system prompt, skill, tool descriptions, hooks and guardrails that you can

[6:12] customize. And I want to just break down a couple of these specifically to talk about how you can leverage the Claude Agent SDK and Claude Code, but specifically for agents that y'all may

[6:20] be building yourself. So if you think about essentially if we take the harness that is Claude Code, if we take the ability to essentially execute tools, use a computer, what is actually missing

[6:29] between just running Claude Code versus a very purpose-built agent that you might build, let's say a finance or an audit agent. The key thing that is actually

[6:37] missing is domain expertise and context engineering is something that I've spent a lot of time on Anthropic and it's a huge part of just making agents effective

[6:46] beyond just running a general purpose Claude Code and really making it tailored to specific use cases. Now, there are variety of different ways in order to leverage context and leverage domain

[6:54] expertise. One of them, something that we're very excited about, Anthropic is something called agent skills. Skills are essentially almost like just 

## [6:58] Utilizing Agent Skills

[7:02] packaged instructions that you can give to Claude. And the key thing here is that they're progressively loaded. So, essentially, if you think about a system prompt, if you're designing, let's say,

[7:11] a customer support agent, you might tell the agent, hey, you know, you're in charge of doing XYZ things. Customer members might say this, you're responsible in answering these types of

[7:19] questions. But maybe you have a specific type of question that a customer support bot has to answer, which is for instance starting a new ticket for a customer.

[7:28] You don't actually want the instructions about how to open a new ticket for that customer injected into your system prompt because that would pollute the context and that would let you read

[7:36] those useless instructions for a customer asking any other question into that system prompt instruction on every single prompt to Claude. Instead, what

[7:44] skills let you do is essentially have those instructions only loaded in when it's relevant to the prompt. So only when the customer says, "Hey, I want to

[7:51] open this new ticket." That's when that skill is invoked in. And Claude can read those instructions into context. Skills can also include scripts and executable

[7:59] files on top of instructions. So, one good example of this that I like to give is our open source PowerPoint skill, which essentially other than instructing

[8:07] Claude how to create PowerPoints, it actually also has scripts to edit the actual PowerPoint files itself. And it's just an effective way when you

[8:14] essentially want instructions and scripts and templates given to Claude on progressive disclosure as well. The other elements here in terms

[8:22] of all different ways you can give Claude context other than skills, we also have MCP servers. So MCP servers are essentially our default way to talk to external

[8:31] systems. Of course, you can also leverage skills essentially to run scripts or bash commands or CLI commands to also talk to external systems. But

[8:39] MCP is our open standard for how you can leverage essentially existing and approved external integrations to things like Google Drive and Slack and

[8:47] essentially connect your agent to different external systems as well. Sub agents is another way of essentially giving your agent very specific domain 

## [8:50] Benefits of Sub-Agents

[8:54] context and also is a very powerful lever for context engineering. Sub agents are something that I like to talk about as just essentially a way to kick

[9:02] off a parallel workstream for Claude but also have their own context window. You might imagine that this is useful let's say if you're designing an agent that

[9:11] essentially maybe it's a finance agent and you're looking through essentially a really really large context of a really large document. You might launch a bunch

[9:18] of different subagents to read different aspects of the document. They can each write, you know, their kind of own version of writing summaries of that portion of the document, then report

[9:27] back to a main agent. What this does, it essentially prevents the main agent from having to read in that entire document into context. It makes sense so that the

[9:34] subagents are responsible for their own portion of their world and can essentially report back to the main agent. We also see a very effective pattern where you can kind of couple

[9:42] different subagents with different models. Um so the Claude Code default subagent for the explore mode is a Haiku subagent. So the Haiku will kind of

[9:50] come in and explore different aspects of the codebase and then report back to maybe a more intelligent model like a Opus or Sonnet. Now this is something that our team is actively working on. We

[9:58] merged custom commands and skills recently if any of you have seen it but um I know there's some confusion around hey when do I use a skill versus MCP

[10:06] versus subagent. I would think about it essentially as thinking about skills whenever you want procedural knowledge that you always want to persist and you

[10:14] want to call on. Another example I like to give is our front-end design skill at Claude Code, which essentially whenever Claude does front-end design work, it can invoke a front-end design skill to make Claude better at frontend design.

[10:24] That's like a repeatable workflow that you essentially want to inject additional instructions into Claude. MCP servers are kind of the maybe the first

[10:31] place you think when you think about integrating with an external system.

[10:34] There's some cases where it might be more effective to do this as a script or a skill, but MCP servers are really actionable when you want to essentially take action in an external system. Now, subagents

[10:44] here, I think you can use them as sort of specialized worker agents, but the main thing is just for parallel exploration and also fresh context windows. Now I want to talk a little bit

[10:52] about governance, security and observability which I know is a hot topic for just today overall because we don't want to design and deploy AI

[10:59] agents that are not secure and that is a huge point that we also emphasize in Anthropic. Um safety is really really important to us and that's something

[11:06] that we encode into the model itself but also design primitives around. So the first one here is hooks. Hooks are essentially a way so that you can secure 

## [11:10] Governance and Safety Hooks

[11:15] the tool calls that an agent is going to make. You could imagine let's say if an agent is trying to run a like rm -rf command that can be something that you

[11:23] can guard against with sandboxing and with hooks. Hooks can also essentially allow you to enforce human in the loop.

[11:29] So for instance, if you want an agent to call out for human approval before running a command like writing to a certain system. Let's say you're writing to a Salesforce system or writing to a

[11:38] Jira ticket. before that command is actually able to execute or before that tool can execute, you can put a pre-tool use hook on it to make sure that the

[11:46] agent is asking for permission deterministically every single time. So hooks are essentially a way for you to inject a little bit of determinism into

[11:54] your agent, otherwise letting the kind of the model decide its own trajectory and be flexible and be dynamic. But hooks are a way to add some of those guardrails back into the system. The other element here is permissions.

[12:04] Permissions we think about a lot as well with our agent SDK and this is something that you might have also seen in Claude Code. We recently announced an auto mode as well in Claude Code. That is my pro

[12:13] tip for the day if you haven't seen it already. I haven't seen a permission prompt in a long time just using the auto mode in Claude Code. Um but permissions are something that you want

[12:20] to think a lot about as well because we of course want to govern agents to make sure they're not taking actions that a human wouldn't want. The first place that agents um go for permissions in the

[12:29] Claude Agent SDK is to hooks. So that's that layer I talked about where we can enforce human in loop. You can also make sure that you're just adding like rules

[12:37] of what the agent is not allowed to do when to ask for permission. You can essentially think about it almost as the same way for Claude Code agents where you

[12:44] want to essentially do like allow edits or if you want to make sure that Claude Code is asking for permission every single time. The other element here is sandboxing. And I think this is

[12:52] something that I also really recommend looking into for anyone looking into how to design a secure agent. And essentially what a sandbox is is we want to give an agent sort of the free realm

[13:01] to reduce permission prompts and also execute commands within an existing environment. But anytime the agent tries to exit that sandbox environment, run a

[13:10] command that it's not allowed to or access a network that it's not supposed to access, that's when a permission prompt is triggered. So there's native sandboxing built into Claude Code that's also extensible to the Claude Agent SDK.

[13:20] So, we've talked a little bit about how the Claude Agent SDK is kind of built on Claude Code, but one point that I think I really want to make is just the way we think about agents and Anthropic both

[13:28] with the agent SDK and with our new managed agents that we just released is that a lot of these core primitives actually do translate really well across domains. So, you think about like a

[13:37] contract review agent, they may also access the file system. They're reading in a contract just instead of a codebase. And then they execute a lot of the same model logic but with custom

[13:46] skills, custom prompts, and custom tooling to make it tailored to that domain. Next thing that I want to talk about a little bit here is just to make sure now that we've discussed a little

[13:54] bit about how to build an agent is how to make sure that the agent is actually executing the capabilities that you want it and how you can actually evaluate the 

## [13:56] Evaluation with Evals

[14:01] effectiveness and capabilities of your agent. And that is where evals come in.

[14:05] And an eval is something that I talk a lot about with the different teams I work with just because I feel like a lot of times people are just behind on building evals with how quickly agents are

[14:13] evolving and models are evolving. But evals are actually a really really important way of helping you stay on that path of model progression. And that

[14:21] is because without evals, let's say a new model comes out, you have your existing agent, you have your existing prompts and your existing tooling. You don't know objectively in a quick way to

[14:29] test if a new model put into your system is actually going to help you achieve new capabilities. But with evals, essentially what you can do is define a

[14:36] test a set of use cases. They're almost like unit tests, but for built for agents and built for dynamic paths. And say you're building like a customer

[14:44] support agent, you can essentially run evals to check if that response given to the customer is actually something that is high quality both on the response

[14:51] content itself and on the style. And eval signal over the things that you're building. So here is the Anthropic agents playbook. And I know I went

[15:00] through everything a little bit quickly just cuz I want to leave time for a demo if we can get to it. I think the various elements here are essentially giving an agent agentic frameworks that are

[15:08] actually leveraging the power of the model. I think a lot of other frameworks that exist, I think usually I think the danger here is when the frameworks themselves become too workflow based or

[15:17] don't give the model the capability to actually execute the tools that it needs. This is just because if you think about agents as a proxy for how we at

[15:24] humans think about solving tasks, you wouldn't want a human to be essentially be restricted in how much it can do. If I didn't have access to all the

[15:31] different tools at my disposal, like all the different commands inside of a terminal, then I wouldn't be able to be as effective of a developer and actually be able to solve a problem by leveraging

[15:40] all the different tools and skills and materials that I have at my disposal. So that is a really really huge part of just making sure your agentic framework

[15:47] is well levered to capture that model intelligence. The other aspects here are essentially it's really really powerful when you give your agent access to a

[15:55] computer. That's kind of what makes Claude Code magical just because Claude Code can actually come in and access different elements of your computer and why we saw so many people nontechnical

[16:03] users using Claude Code as their primary entry point to Claude before we release Claude Cowork just because Claude can kind of do so much more when you just give it access to everything that you have going

[16:11] on on your computer and the same kind of works for different agents in different domains as well. The next part here, domain expertise is where I think a lot

[16:19] of builders focus on today. That's where, you know, at Anthropic, we can only build so many agents, but there's infinite amount of domains to tackle in

[16:26] the world. And that's where custom agent skills, tools, and system prompts come in. And the last part here is eval, which is just a quick reminder that as

[16:33] you're building agents, evals are a huge part to make sure that you're actually checking the capabilities of the agent and figuring out where the agent is falling and where it's succeeding in

[16:41] your prompts and systems today. All right, so now I'm going to jump ahead to a demo. And the demo that I'll be showing today is essentially a site 

## [16:48] Site Reliability Engineer (SRE) Agent Demo

[16:49] reliability engineer, an agent that can actually come in here and debug things when your production cases fail, when you're seeing error spike. Um, bit of a

[16:56] risky demo, so everyone can cross their fingers and hope that the agent is actually able to debug the incident. Um, but just to set the stage here, I'm sure

[17:04] with the technical audience we have today, a lot of you are familiar with this. But the pain point that the agent is trying to solve is that for

[17:11] engineers, half their life is spent on building new features. They, you know, have exciting new features come out, are

[17:18] advancing the product capabilities, but the other half of their time is actually spent on debugging production incidents.

[17:24] Whenever a new feature is launched, this means that you might be on call again.

[17:28] You might be, you know, woken up at 2 a.m. and you have to come in and look at an incident that has been raised. You need to wake up from your bed, come in and triage and investigate. And another

[17:37] huge pain point is that maybe once you're done with all this investigation, you actually also have to go and write a post-mortem about it. So again, just very painful steps and is a huge pain

[17:46] point that we're going to try to automate away with our agent. And if we think about everything that we talked about previously in this talk so far, we

[17:53] talked about skills, we talked about Claude Code, we talked about tools and MCP servers, the site reliability engineer actually maps really well to

[18:00] all those components that we talked about. So if we think about what exactly is going to happen for this agent under the hood, the agent is going to come in and receive an event. Then it's going to

[18:08] run inside of this core loop in the Claude Agent SDK. It has access to Claude Code. So it can actually access your codebase and debug things live within

[18:16] your codebase. Then it has skills for things like runbook adherence. So runbooks being like, hey, previously when you saw this similar incident, what

[18:23] are the steps you took to debug it? The agent is going to be able to read those skills in as well as like say how to write a postmortem. It also has all these MCP servers to access all these external

[18:32] systems and do things like ingest logs just as how you as a human developer would be able to look up things like Kubernetes and look up things like your observability to debug what's going

[18:40] wrong with the agent. Okay, so we have here is a sample codebase here. You can see we have different elements and we have an API server environment. What we're going to do here is actually break

[18:49] this agent. Don't worry, there's only kind of one important element which is this database pool size. So here what we're going to do is we're going to break this um codebase. We're going to

[18:57] actually drop that database pool size down to one. Essentially, what we're doing here is we're making it so that there aren't enough resources to allocate to this codebase. And then

[19:06] we're going to come in um actually before I do that, let me just go ahead and flip. You can see here that we're logging all the 500 errors that we're calling. And let me come in and just redeploy this on Docker.

[19:17] In fact, this might take a second here.

[19:24] Okay, there we go. Hopefully in a second here we're going to see the errors start to spike. We're waiting for the metrics to pick up a little bit here. Um the graph that you're looking at is

[19:32] essentially just a log of all the 500 errors that you're seeing. So here we just saw that big spike that just happened because we're no longer allocating enough database pool

[19:39] resources. So therefore we're seeing a lot of spikes that the user is then going to experience because the service is going to be down. So now if we actually then flip over, usually again

[19:48] what the engineer is going to have to do at this point is they might get woken up by a PagerDuty call. they have to wake up at 3:00 a.m. and come manually debug.

[19:55] But instead, what we're going to do is we're going to hand this off to the SRE bot. So, let me just go ahead and type this in. Okay, so as you can see here, we've told the SRE bot that the 500 errors are spiking and for them to

[20:03] create an incident. Of course, we could do a little bit more here. We could actually have this just automatically polling for incidents. So, we don't even have to come in and tag the bot. But for

[20:11] purpose of this demo, it's just also a little bit more illustrative here that we're going to come in and create an incident and keep the human in the loop.

[20:17] For those of you who might be able to see here, PagerDuty is actually calling me right now. Let's see. It's kind of an annoying sound.

[20:24] You have one triggered incident on SRE agent demo. The failure is 500.

[20:30] Okay. So, as you can imagine, that's not a super pleasant noise to wake up to when you're woken up in the middle of the night. But thankfully, we have the SRE bot. So, let's go ahead and just say

[20:39] yes. It's going to come in and start to kick off an investigation to find the root cause of my 500 spikes. You can see here that the bot is kind of reacting to

[20:47] my messages as well, which is also something that I think I would recommend just I know like you know latency is a huge concern for a lot of agents that people are building. But there are ways

[20:56] to leverage just response streaming as well as acknowledgement of an agent working on it that we can leverage also to pull on for threads like latency. And

[21:03] you can actually see here that the agent has pretty quickly determined that the user service is the culprit here that's actually causing the spikes. And it has

[21:11] come in and investigated everything here. It's found that hey, we deployed this here and it identified that the database pool size is the reason why

[21:19] this error is occurring. So, let's go ahead and say yes to this fix. But what I'm going to do is I'm going to open up the codebase side by side here.

[21:30] Okay. And this is kind of the risky part of the demo so everyone can hold their breath. But before I kick this off, I want everyone to keep their eyes on this

[21:38] line here. The database pool size equals to one. And what we're hoping for here is that the agent is actually going to come in and edit the codebase for us.

[21:46] And I think the key thing here is that I think right access or agents taking actions can feel pretty dangerous sometimes. But the important thing is just to add the appropriate guard rails

[21:55] around the agent. And you can see here that when this just went up to 20, that is kind of the power that we can unlock when we give agents access to the tools

[22:02] at its disposal. And it's actually not going to just stop there. the agent is going to come in and redeploy the server and make sure and verify its own work so

[22:11] that it actually can make sure it solved the issue effectively.

[22:16] So if we keep our eye on this graph here, we can see that now that we have resolved this issue, the 500 errors are going back down. The service is back up.

[22:23] Yay. So the agent has helped us avoid this incident response needed from a human and handed this off to an agent.

[22:31] You can also see here now that the agent has offered to resolve the PagerDuty for me and also create an postmortem.

[22:37] And again, this is another part of the element here. Usually for an on call engineer, it doesn't end when you resolve the incident. Now, you have to come in and write a postmortem so your

[22:45] team can actually know what you did and encode this for future practices. We're actually going to see here some of the power of those MCP server connections come in as well because our postmortm

[22:54] postmortem is going to be created inside of Jira or Confluence, which is where our team keeps all of our postmortems today. Okay, looks like the postmortem

[23:01] is getting published and the agent is also resolving the PagerDuty incident.

[23:06] And we can see here if we just open this up here, let's come in and open up the postmortem. There we go. We

[23:14] see the postmortem here. It talks about the PagerDuty incident that happens, the timelines, the root cause it documented, the remediation steps, and the action items as well. And again,

[23:23] this postmortem here is actually a skill, which means that the Claude agent is not going to read instructions about the postmortem into a system prompt

[23:31] until I actually say as a user that I want it to execute and kick off a postmortem for me. That means that we can make this postmortem skill instruction more detailed and encode

[23:39] things about like how you want your action items detailed. You can even include a template for the postmortem or if you want things really deterministic, you can have a script where you're, you

[23:46] know, deterministically injecting things into Jira or wherever your postmortems live for your team. So that's kind of the power of skills as well, which is that we're able to save on context by

[23:55] not having these repeatable knowledges added to the system prompt every single time we call Claude. All right, so just to end us off here, um, managed agents is 

## [24:01] Introduction to Managed Agents

[24:03] something that we really recently released, I think today or maybe yesterday. Um, just want to show a quick video of it just because everything that we talked about today is on the Claude

[24:11] agent SDK and just generally how we think about agents at Anthropic. But managed agents is our very new product which essentially allows you to kind of

[24:19] abstract away all the work that we didn't talk about today which is deployment and hosting of an agent.

[24:24] Usually that's a huge bottleneck especially when you think about giving Claude access to a computer or file system just because that is where you

[24:31] actually really start to think about how do you make sure everything is containerized and make sure that the access to computer is safe and deployed in a virtual machine and that is kind of

[24:39] the work that managed agents abstracts away for teams building agents today.

[24:43] All right, so that's all I have for you today, but Claude managed agents, you can see, has some more like observability and built-in capabilities just to make sure your agent is running. It kind of

[24:50] breaks things down more by session and environments rather than how you might think about agents as being very very decomposed via like our messages API for

[24:58] instance. So you can think about managing agents as just the environment you give to the agent and the sessions that you run on the agent. So encourage everyone to think about if you're building an agent from scratch, you're

[25:06] just prototyping something new, test out the manage agent and see where you can get with it as well.
