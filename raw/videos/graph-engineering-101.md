---
title: Graph Engineering 101
video_id: IrW0_f-w4kA
url: https://www.youtube.com/watch?v=IrW0_f-w4kA
channel: Google Cloud Tech
channel_id: UCJS9pqu9BzkAMNTmzNMNhvg
channel_url: https://www.youtube.com/channel/UCJS9pqu9BzkAMNTmzNMNhvg
series: AI Builder Essentials
speakers:
- Tilde Thurium
- Annie Wang
products_mentioned:
- Agent Development Kit
- Graph Engineering
codelab: https://g.dev/ai/adk-2-orchestration
publish_date: '2026-09-03T12:15:32-07:00'
upload_date: '2026-09-03T12:15:32-07:00'
category: Science & Technology
duration: '5:56'
length_seconds: 356
view_count: 24137
default_language: null
is_live: false
thumbnail: https://i.ytimg.com/vi/IrW0_f-w4kA/maxresdefault.jpg
keywords:
- what is graph engineering
- graph engineering vs loop engineering
- graph engineering vs agent swarm
- difference between harness loop and graph
- google agent development kit tutorial
- how to build multi agent workflows with adk
- graph engineering vs knowledge graph
- automate code review with AI agents
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
- language_code: en-US
  name: English (United States)
  kind: manual
  is_translatable: true
chapters:
- title: 'Intro: What is graph rngineering?'
  start: 0:00
  start_ms: 0
- title: 'Demystifying terms: Harness vs. loop vs. graph'
  start: 0:29
  start_ms: 29000
- title: 'Real-world example: PR review with fan-out, join & router patterns'
  start: '1:29'
  start_ms: 89000
- title: Graph engineering vs. knowledge graphs
  start: '3:17'
  start_ms: 197000
- title: Graph engineering vs. loop engineering
  start: '3:44'
  start_ms: 224000
- title: Graph engineering vs. agent swarms
  start: '4:19'
  start_ms: 259000
description: 'Try out the Codelab → https://g.dev/ai/adk-2-orchestration


  Learn about Graph Engineering and how it provides the predictability and control needed for complex, multi-agent AI systems. In this conversational breakdown, we cover the differences between:

  * Agent harnesses, loops, and graphs

  * Walk through an automated pull request (PR) review pipeline using fan-out, join, and router patterns.

  * How graph engineering differs from knowledge graphs, loop engineering, and agent swarms, and how to orchestrate shared state using Google''s Agent Development Kit (ADK).


  Chapters:

  00:00 - Intro: What is graph rngineering?

  00:29 - Demystifying terms: Harness vs. loop vs. graph

  01:29 - Real-world example: PR review with fan-out, join & router patterns

  03:17 - Graph engineering vs. knowledge graphs

  03:44 - Graph engineering vs. loop engineering

  04:19 - Graph engineering vs. agent swarms


  Speakers: Tilde Thurium, Annie Wang

  Products Mentioned: Agent Development Kit, Graph Engineering'
notes: 'Acquired 2026-09-04 via youtube-transcript-skill (Playwright/Chromium). 48 segments across the channel''s own 6 chapters. The video carries BOTH an auto-generated (asr) and a human-curated en-US (manual) English track; the scraped panel is the manual one — punctuation, capitalised product names (ADK, GraphRAG, Agent Swarm) and inline chapter labels are all present, so transcript quality is high. Clean-up applied: YouTube''s accessibility duration read-outs (''1 minute, 3 seconds'') stripped from the head of segments; leaked ''Chapter N: ...'' labels removed from segment text and re-emitted as headings; four transcription slips corrected (''the arm doing the reasoning'' -> ''the LLM doing the reasoning''; ''handle is more flexible'' -> "it''s more flexible"; ''inside the results'' -> ''it consolidates the results''; ''waiting for the slowest, the processing'' -> ''waiting for the slowest processing''). Timestamps preserved verbatim. Note the channel''s own chapter 1 title contains
  a typo — ''What is graph rngineering?'' — preserved as published in the chapters: block above. Third entry in the AI Builder Essentials arc already in raw/videos/: ''What is an Agentic Harness?'' (2026-07-16), ''4 ways loop engineering fails'' (2026-08-25), and this.'
---

## [0:00] Intro: What is graph rngineering?

[0:00] So if you've been following trends, you might have seen that the words graph engineering are suddenly everywhere. Annie, what's graph engineering?

[0:06] Graph engineering is you can think of you’re creating a graph workflow in the system. The graph can be something like, you know, organizational chart.

[0:13] And inside of this graph each node can be agent node. It can be a function node which can be a deterministic logic. It can be more.

[0:21] And then you’re basically creating this graph in the system to solve the problem. So I'm still a little confused about all this terminology.

[0:28] Can you clarify, like, what is the harness, what is the the loop and what is the graph? Yeah, that is a good question. It can be very confusing.

## [0:29] Demystifying terms: Harness vs. loop vs. graph

[0:36] So if you take a look at this picture we have this harness part.

[0:39] So harness part is everything around the model including its tools, memory and guardrails. And the loop can be the cycle of that agent is running inside that harness.

[0:49] For example the LLM doing the reasoning trying to make a decision, picking a different tool and selecting a different tool until it solves the problem and until it's meeting the goal and graph can be the organization chart we were talking about earlier.

[1:03] It can contain an agent node containing function node and more. Makes sense.

[1:07] So when you traverse the graph, you're passing memory or information down the graph to the next node. Yeah, exactly.

[1:13] So if you build with Google Agent Development Kit, ADK, if you build a multi-agent system and we have this shared states among different agent, if you build a workflow, we have share states among nodes in this workflow as well.

[1:26] What would a real life example look like? Oh so Tilde, have you done PR review? Unfortunately yes I hate code review. Tell me there's a way to make it easier.

## [1:29] Real-world example: PR review with fan-out, join & router patterns

[1:35] Imagine you want to automate the PR review. You're creating this workflow to automate the process.

[1:39] And because you already know exactly how to do the PR review, you know the workflow ahead of the time. So you're creating this workflow.

[1:47] And just like the picture you're seeing right now, we have three parts. So the first part of this workflow including this fan out. And the second part is the join. And the third part is a router.

[1:55] So let's start with the fan-out part.

[1:57] The fan-out part is we're starting this five parallel processing to pull the information for the PR like a pull request.

[2:05] So you're probably familiar with the parallel processing, right? Yeah absolutely. You might take one task and break it into like five different parts.

[2:12] And then you run them each at the same time, which is much faster than running them one after another and waiting for them all to finish.

[2:17] And the next is once you finish the parallel processing, we want to have a join node. Join node is basically to synthesize the result.

[2:24] So it's waiting for the slowest processing, and then it's it consolidates the results that later on we can handle this information. And then we go to the last part which is the router part.

[2:32] So we're using a router pattern to handle this information. You’re probably familiar with router, right? I'm familiar with like a server router.

[2:40] Where you take a URL and then you know, you match it with the kind of web page that you want to serve up. How does that relate to AI graph engineering?

[2:47] Oh, it's very similar. For the router pattern basically you have this request input. And then we router to a different sub agent or specialist or different workflow.

[2:57] In our specific example, the condition is if the call fails we will go to the specialized fixer agent. If the call pass we will go to the human approval processing.

[3:07] So it sounds like we're taking basic principles of control flow and applying them to AI engineering. So this is a little embarrassing.

[3:15] But when I first heard about graph engineering, I thought that it was about knowledge graphs and the data model. But it sounds like that's not true. Yeah, it can be very confusing.

## [3:17] Graph engineering vs. knowledge graphs

[3:24] A lot of terminology has graphs. We have Graph Engineering, we have GraphRag, we have Knowledge Graph.

[3:30] But Knowledge Graph emphasizing on the data and Graph Engineering emphasizing on the behavior basically what goes in, in what order, and then what happens next.

[3:39] And just like the example we covered earlier. So how is graph engineering different than loop engineering? That's a good question. So loop engineering basically you have this one running loop.

## [3:44] Graph engineering vs. loop engineering

[3:48] And keep running until it's reaching the goal. And the graph engineer is you're creating this graph workflow.

[3:54] And then inside of the graph you have different node and different edge to solve the problem.

[3:59] Do you know when to use what? It sounds like, Loop Engineering is better for simple workflows. Like, I want a one paragraph summary, and Graph Engineering would be better for a much more complex workflow.

[4:12] Like I need a 50 page PDF with a bunch of graphics and different shiny things. I know there's another terminology called Agent Swarm.

## [4:19] Graph engineering vs. agent swarms

[4:19] What is the difference between Graph Engineering and Agent Swarm?

[4:22] They're both agent orchestration patterns, but under the hood they're pretty different. So in Graph Engineering you as the engineer, you define each node.

[4:31] What happens at each step of the workflow, how the data looks and everything.

[4:35] And also agent that it’s at a certain node, it doesn't need to know what happened before.

[4:40] And this whole thing gives you really good predictability, debuggability and control for problems that can be really strictly defined, like the PR workflow you mentioned earlier.

[4:50] What about Agent Swarm? Well, not all problems are easily defined like that. In an Agent Swarm you have each agent just gets its own personality and that's it.

[5:00] And then you just throw the problem to them.

[5:02] So sounds like if you want to solve an ambiguous problem, and we want to use Agent Swarm because a it's more flexible it can handle more ambiguous use cases.

[5:11] But if you already know the workflow ahead of time, like the PR review example, we can use Graph Workflow. Exactly. You got it.

[5:18] So that's graph engineering in a nutshell. Yeah.

[5:21] If you want to learn more, check out Annie’s tutorial video where she's going to build a system from start to finish using Google's Agent Development Kit. One last question.

[5:29] Are we just reinventing data structures and algorithms for the agentic age? Yeah, maybe. What trend do you think is going to be next?

[5:36] Maybe hash table engineering or stack engineering. What do you think? Abstraction-maxxing. Yeah could be.

[5:44] So let us know in the comments. What trend do you think is going to be next? Thanks so much for watching. Thank you. Bye.
