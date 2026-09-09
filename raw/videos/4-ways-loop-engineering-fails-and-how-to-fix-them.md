---
title: 4 ways loop engineering fails (and how to fix them)
video_id: ruNekO9De8E
url: https://www.youtube.com/watch?v=ruNekO9De8E
channel: Google Cloud Tech
channel_id: UCJS9pqu9BzkAMNTmzNMNhvg
channel_url: https://www.youtube.com/channel/UCJS9pqu9BzkAMNTmzNMNhvg
publish_date: '2026-08-25T12:00:01-07:00'
upload_date: '2026-08-25T12:00:01-07:00'
category: Science & Technology
duration: '4:38'
length_seconds: 278
view_count: 4939
is_live: false
is_upcoming: false
is_private: false
is_family_safe: true
default_language: null
thumbnail: https://i.ytimg.com/vi/ruNekO9De8E/maxresdefault.jpg
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
- title: 'Intro: What is Loop Engineering?'
  start: 0:00
  start_ms: 0
- title: 'Failure #1: Runaway loops'
  start: 0:35
  start_ms: 35000
- title: 'Failure #2: Unverified autonomy'
  start: '1:27'
  start_ms: 87000
- title: 'Failure #3: Vague or uncheckable goals'
  start: '2:29'
  start_ms: 149000
- title: 'Failure #4: Complexity overflow & graph engineering'
  start: '3:05'
  start_ms: 185000
- title: Summary & best practices
  start: '3:52'
  start_ms: 232000
description: "Try out the Loop Engineering Codelab → https://g.dev/cloud/loop-lab-table\n\nExplore four\
  \ common errors that every developer should watch out for when building loop engineering projects, and\
  \ practical strategies to mitigate them. In this video, the team breaks down why runaway loops burn\
  \ tokens, how unverified autonomy leads to confirmation bias, why vague goals cause models to fail,\
  \ and when developers need to transition from single loops to multi-node graph engineering. \n\nTell\
  \ us in the comments below if you've experienced any loop failures! \n\nChapters: \n00:00 - Intro: What\
  \ is Loop Engineering?\n00:35 - Failure #1: Runaway loops\n01:27 - Failure #2: Unverified autonomy\n\
  02:29 - Failure #3: Vague or uncheckable goals\n03:05 - Failure #4: Complexity overflow & graph engineering\
  \ \n03:52 - Summary & best practices \n\nMore resources:\nLoop engineering sample in ADK → https://g.dev/cloud/adk-loop-engineering\n\
  AI Builder Essentials playlist → https://www.youtube.com/playlist?list=PLUtwsPnFtFfU\n\nSpeakers: Tilde\
  \ Thurium, Annie Wang\nProducts Mentioned: Agent Development Kit"
notes: 'Fetched via youtube-transcript-skill (Playwright). Headless failed; --headed succeeded on the
  second attempt (transcript panel render timeout is the recurring failure mode, and it returns a silent
  "transcript": null alongside good metadata).

  The video carries BOTH an auto-generated (asr) and a human-curated en-US (manual) caption track; the
  fetched text reads as the human-curated one — full punctuation, curly apostrophes, no ASR proper-noun
  damage. No cleanup was needed.

  Two speakers, unlabelled in the captions: Tilde Thurium and Annie Wang (per the video description).

  '
---

## [0:00] Intro: What is Loop Engineering?

In this video to learn about four ways Loop Engineering fails and how to fix them. So if you've been following AI developer trends, maybe you've heard about Loop Engineering, but Annie what is Loop Engineering? Yeah, that is a good question. You can think of it as you replacing yourself with a system. So instead of you keep typing and trying to solve a problem. You'll create a system and set a goal and let the system keep retrying until it's meeting the goal. And that whole process, that system, you can think of it as a Loop Engineering. That sounds really useful until it's not. Let's talk about four common ways that loops tend to break down.

## [0:35] Failure #1: Runaway loops

Yeah. The first is Runaway Loops. Have you ever written a Runaway Loop? Yeah. Of course. You know, once that I'm trying to create a retry logic. And I just put all the retry logic in a loop and I forget to add exit condition. And then my application just froze, and I was like, what's going on? I realized, oh, I run into the infinite loop. It's like a classic developer experience that many people run into when they're first learning to code. But the problem is, now that we're in the age of AI, you're not just burning through memory, you're not just crashing your stack, you're burning tokens. And those cost real money. What do we do? So that is why a clear stop rule is very important. For example, you can set like maximum iteration number to be five to stop the loop, or you set a time limit or set a limit on the token or the cost, so that you won't burn your token. That's pretty much the first failure pattern. The second failure pattern is the Unverified Autonomy.

## [1:27] Failure #2: Unverified autonomy

So what does it mean is think of you have an agent and you let the agent do a certain job. And in the same conversation you ask the same agent to do the same job again. And then because it's already do the job before, so it has a memory, has a context, and then later on the job the agent tend to reuse a context, reuse the memory it has before. Now what if in the first try it made a mistake? What if it's not a good dataset to reuse? And that way you're not like getting a good answer if you just keep running something in the loop. So this is also what we call confirmation bias. Yeah. And in addition to confirmation bias and context pollution, there's just plainly an issue with asking an agent to evaluate its own work. It's like asking a kindergartner to grade its own homework. No, we don't want to do that. Instead, you can have agent A evaluating work for agent B and vice versa. And that way we have a separation of concerns and it's just cleaner and more accurate. So you can have it as a job or you can set a clear matrix to evaluate your system. What is the third common pattern?

## [2:29] Failure #3: Vague or uncheckable goals

The third issue comes from uncheckable goals. Oh, what is that? That is, if I, for example, asked a Loop Engineering workflow to make this summary better. Okay, what is better? That's completely vague. And the LLM is just going to crash out trying to understand what we mean by that. Yeah. So in this scenario you should have explicit and checkable criteria. So what I mean by checkable means is non-debatable, non-negotiable. For example it has to be less than ten what counts, is very clear. Or has a zero compilation errors, things like that. What is the last common failure we have?

## [3:05] Failure #4: Complexity overflow & graph engineering

The fourth failure mode is complexity. So if I ask a single loop to make me a one paragraph summary, it’d probably do pretty okay. But if I asked a single loop, hey, I need a 50 page PDF with a bunch of generated images and tables, it would probably choke. So if we need a large, you know, complex problem like that, what's a better way of handling it? So that is a best time for us to move from Loop Engineering to Graph Engineering. So instead of you have one agent doing the one running process, right? You have an organization chart. You have this whole graph workflow to orchestrate everything. You can put loop as part of the graph. Or you can create your own nodes and edges to design your own system. And that way you can add in more control and you can handle more complex situation like we just mentioned before.

## [3:52] Summary & best practices

Very cool. And if you want to learn more about Graph Engineering you can check out Annie's tutorial. So to summarize, Loop Engineering is very useful for contained, verifiable and repetitive tasks. To keep your loops running smoothly always enforce stop rules and cost caps. Never let an agent rubber stamp its own work. Define clear, verifiable goals and when single loops hit context limits, orchestrate them into graphs. Yeah. And thank you so much for watching this video. And if you have faced any failure trying Loop Engineering or you have any other experience with Loop Engineering or Graph Engineering, feel free to share them in the comments and we will see you in the next video. Bye!
