---
title: "Agentic video understanding in Gemini"
video_id: ytjgy30Cono
url: "https://www.youtube.com/watch?v=ytjgy30Cono"
channel: "Google for Developers"
channel_id: UC_x5XG1OV2P6uZZ5FSM9Ttw
channel_url: "https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw"
publish_date: '2026-09-01T10:00:12-07:00'
upload_date: '2026-09-01T10:00:12-07:00'
category: "Science & Technology"
duration: '3:19'
length_seconds: 199
view_count: 13342
is_live: false
thumbnail: "https://i.ytimg.com/vi_webp/ytjgy30Cono/maxresdefault.webp"
keywords:
  - "Google"
  - "developers"
caption_tracks:
  - language_code: ar
    name: "Arabic (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: bn
    name: "Bangla (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: nl-NL
    name: "Dutch (Netherlands) (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: en
    name: "English"
    kind: manual
    is_translatable: true
  - language_code: en
    name: "English (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: fr-FR
    name: "French (France) (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: de-DE
    name: "German (Germany) (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: iw
    name: "Hebrew (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: hi
    name: "Hindi (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: id
    name: "Indonesian (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: it
    name: "Italian (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: ja
    name: "Japanese (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: ko
    name: "Korean (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: ml
    name: "Malayalam (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: pl
    name: "Polish (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: pt-BR
    name: "Portuguese (Brazil) (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: pa
    name: "Punjabi (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: ru
    name: "Russian (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: es-US
    name: "Spanish (United States) (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: ta
    name: "Tamil (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: uk
    name: "Ukrainian (auto-generated)"
    kind: asr
    is_translatable: true
description: |
  Processing long videos can use a lot of tokens. Learn how to do this more efficiently using our latest agentic video understanding capability available in Gemini 3.7 Flash, 3.6 Flash, and 3.5 Flash-Lite. In this video, Google DeepMind’s Maarten Grootendorst explains how agentic video understanding works, and how  this approach reduces token costs while improving accuracy on the parts of the video that actually matter.

  Resources: https://goo.gle/4xzZaxJ

  Subscribe to Google for Developers → https://goo.gle/developers   

  Products Mentioned: Gemini
  Speaker: Maarten Grootendorst
notes: |
  Acquired 2026-09-09 via the youtube-transcript skill (Playwright route). Transcript scraped from the
  auto-generated (ASR) caption track; 66 segments, timestamps preserved verbatim.
  No chapters published by the channel.
---

## Transcript

[0:03] Welcome to this video of Agentic Video

[0:06] Understanding with Gemini.

[0:09] When we have a video that we want Gemini to parse for us

[0:13] to give certain information about,

[0:15] what we generally would do is we would try

[0:17] to split it up into frames.

[0:20] And there are a number of frames extracted from those

[0:22] that we can give to the model.

[0:25] It's a decent way of giving model the context it needs

[0:28] to answer the query that we might have.

[0:31] But here's the thing. If we give the entire video

[0:35] to Gemini, there will be already more than 100,000 tokens.

[0:40] That's a lot, and there's a lot of information

[0:42] that we really don't need

[0:43] because what if I only want information in frame 900,

[0:48] or a couple of seconds here, a couple of seconds there?

[0:52] Then there's really no need for the model

[0:54] to see the entire video.

[0:56] That means that this naive way of processing

[1:01] is very expensive

[1:02] and there should be a way

[1:04] that we can do this easier and more efficiently.

[1:07] Surprise, surprise, there is.

[1:10] With agentic video understanding,

[1:13] we don't give the model the entire video.

[1:16] We give the reference to the video

[1:18] and a model can then decide, "Oh, maybe I can use

[1:22] a get transcript function to extract a small piece

[1:27] of information about the video already

[1:30] before I zoom in. It gets this transcript

[1:34] and then it continues on with potentially a new tool call.

[1:38] For example, get frames.

[1:40] Ah, there's this something happening at the five-minute mark

[1:43] and I need to increase the number of frames per seconds

[1:46] to really see what's happening.

[1:48] This idea of agentic video understanding reduces the cost

[1:51] significantly because it doesn't need

[1:53] to see the entire video.

[1:55] But how does that work?

[1:56] Well, normally you would have this query

[1:59] and video that you give to the model and it gives an answer.

[2:03] With this new agentic video understanding pipeline,

[2:06] what happens is that the model first thinks about which

[2:10] tools it might want to use to process this video.

[2:13] It can use get transcripts like we saw before.

[2:18] We can use get frames,

[2:20] and again, specify which frames it wants

[2:23] and at which frames per second, which is a great way

[2:26] of getting either a very global

[2:28] or localized perspective of the video.

[2:31] And we can even get the audio. It runs those tools.

[2:36] I mean, this is an agentic loop,

[2:38] and it gets an observation in return frames, for instance.

[2:41] And this information is then given back to the model

[2:44] where it can decide to do another loop.

[2:47] And then we have this very traditional agentic loop

[2:50] of thinking, acting, observing,

[2:53] and looping until it finally derives at the answer.

[2:57] And what's so great about this technique is

[3:00] that not only does it reduce the number

[3:03] of tokens it really needs, the performance increases

[3:06] because it can zoom in on certain functions

[3:09] and really pay attention to the things in the video

[3:12] that are actually important to the query.

[3:15] And that's how agentic video understanding

[3:18] works with Gemini.
