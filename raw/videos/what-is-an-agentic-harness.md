---
title: "What is an Agentic Harness?"
video_id: W9BX0jyzd2k
url: "https://www.youtube.com/watch?v=W9BX0jyzd2k"
channel: "Google Cloud Tech"
channel_id: UCJS9pqu9BzkAMNTmzNMNhvg
channel_url: "https://www.youtube.com/channel/UCJS9pqu9BzkAMNTmzNMNhvg"
publish_date: '2026-07-16T09:00:13-07:00'
upload_date: '2026-07-16T09:00:13-07:00'
category: "Science & Technology"
duration: '2:55'
length_seconds: 175
view_count: 40887
is_live: false
thumbnail: "https://i.ytimg.com/vi/W9BX0jyzd2k/maxresdefault.jpg"
keywords:
  - "agent harness"
  - "AI agents"
  - "LLM tools"
  - "function calling"
  - "autonomous agents"
  - "agentic workflows"
  - "artificial intelligence"
  - "software development"
  - "Claude Code"
  - "Antigravity"
  - "developer tools"
  - "large language models"
  - "tech concepts"
  - "GenAI"
  - "tech definitions"
  - "Google Cloud Tech"
  - "understanding AI"
  - "AI 101"
  - "introduction to AI"
caption_tracks:
  - language_code: en
    name: "English (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: en-US
    name: "English (United States)"
    kind: manual
    is_translatable: true
description: |
  Experience an agentic harness in action → https://goo.gle/4f3PFjs

  Demystify the concept of an Agentic Harness and learn how they power modern AI systems. In this conversational breakdown, we explore the definition of agents and harnesses, and how both differ from the core LLM and user interfaces. 

  Watch more AI Builder Essentials → https://goo.gle/AI-Building-101
  🔔 Subscribe to Google Cloud Tech → https://goo.gle/GoogleCloudTech

  Speakers: Greg Baugues, Tilde Thurium
  Products Mentioned: Antigravity
notes: |
  Acquired 2026-08-20 via the youtube-transcript skill (Playwright route). This video carries BOTH an auto-generated
  (ASR) English track and a human-curated `en-US` track; the scraped panel text matches the curated track (correct
  punctuation, the curly apostrophe in "Simon Willison's", proper casing of Claude Code / Codex / Antigravity), so
  transcription quality here is high and effectively no ASR cleanup was needed.
  Speakers (named in the description, not the audio): Greg Baugues and Tilde Thurium, Google Cloud Developer Relations.
  The two voices are not individually attributed in the transcript; Baugues is the one who supplies the definitions
  (he is addressed as "Greg" in the opening line), Thurium asks the questions.
  No chapters. Very short (2:55) — this is a conversational explainer, not a talk.
---

## Transcript

[0:00] So, Greg, I've just been wondering.

[0:01] I've been hearing so much talk

[0:02] recently about harnesses.

[0:04] What is a harness?

[0:05] So when we talk about harness, we're

[0:06] talking about an agentic harness.

[0:08] That begs the question:

[0:09] What is an agent?

[0:10] My favorite is Simon Willison’s

[0:11] definition.

[0:12] An agent is an LLM with tools

[0:15] running in a loop to accomplish a goal.

[0:19] The main thing

[0:19] a large language model does is next

[0:21] token prediction.

[0:22] You feed it a bunch of tokens

[0:23] or a bunch of words,

[0:24] and it does fancy autocomplete

[0:26] to figure out

[0:27] what should complete that sentence

[0:28] or statement or string of text.

[0:30] We came up with function calling,

[0:31] and so the idea here was

[0:32] that you could

[0:33] sort of prime

[0:33] the LLM, you could say, hey,

[0:35] I have these functions

[0:36] that you can run,

[0:37] the function signature looks like this.

[0:39] You pass it these parameters.

[0:40] Those functions

[0:41] could do all sorts of things right.

[0:42] But generally speaking,

[0:43] what you're doing

[0:44] is using these functions

[0:45] or tools to go grab context

[0:48] that's external to the LLM,

[0:50] and then to feed that context

[0:52] into the context

[0:53] of your conversation with the LLM,

[0:55] so that it can augment its response.

[0:57] That's the tool portion.

[0:58] How do we give the LLM access

[1:02] to information

[1:02] that's not baked into

[1:03] its training data?

[1:04] And then there's this portion

[1:05] of running in the loop right.

[1:06] So it's not just a one for one.

[1:08] There's some mechanism there

[1:09] where we are

[1:10] programmatically evaluating

[1:12] the output of the large language model

[1:14] to determine is it done?

[1:16] Has it reached the goal?

[1:17] And if it's not then

[1:18] we feed it

[1:19] more instructions

[1:20] programmatically and then we have it

[1:22] just run in that loop.

[1:23] Those are the portions of

[1:25] like what is an agent.

[1:25] And my definition

[1:27] of an agentic harness,

[1:29] the harness

[1:29] is everything after the LLM.

[1:32] The harness is

[1:33] how do you give it tools?

[1:34] The harness is what programming

[1:36] do you have

[1:37] that's running it in the loop?

[1:38] What programming do you have

[1:39] that is evaluating

[1:40] the output of the LLM

[1:42] to determine

[1:43] if it completed its task or not?

[1:44] And all of that infrastructure,

[1:46] which doesn't have to be a lot,

[1:47] but that is the agentic harness.

[1:49] All that stuff

[1:49] you put around an LLM

[1:51] to turn it into an agent.

[1:52] That makes so much sense,

[1:53] because I had been thinking

[1:54] of the harness as like,

[1:55] it's like the IDE or it's like,

[1:56] what what's running your agent.

[1:57] But it sounds like your definition

[1:59] is lower level of that.

[2:00] If you think about the most popular

[2:01] agentic harnesses today.

[2:03] So like a Claude Code or an Antigravity

[2:05] or a Codex, right.

[2:07] There are different interfaces

[2:08] that you can use

[2:09] to interact with that harness.

[2:12] So I think it's really interesting

[2:13] that if you decouple the harness

[2:16] from the interface,

[2:17] you're saying

[2:17] the important piece

[2:18] here is how we control the logic

[2:22] and the behavior of the LLM.

[2:24] And then you can sort of like swap in

[2:26] what interface does the user prefer?

[2:28] Totally. And every use case.

[2:30] And every use case. Absolutely.

[2:31] There's probably actually

[2:32] a lot of use cases

[2:34] where you don't even need

[2:35] a user interface.

[2:37] You just need a programmatic interface

[2:38] to the agent, like an autonomous agent.

[2:40] And then coding

[2:41] your interface

[2:42] is going to look different

[2:43] than it is with a consumer chat app.

[2:45] But it might be the same

[2:47] agentic harness

[2:48] powering all those interactions.

[2:49] Awesome. Thank you so much. Thank you.
