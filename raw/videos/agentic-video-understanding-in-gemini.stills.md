---
title: Agentic video understanding in Gemini
video_id: ytjgy30Cono
url: https://www.youtube.com/watch?v=ytjgy30Cono
channel: Google for Developers
duration: '3:19'
transcript: agentic-video-understanding-in-gemini.md
stills_dir: ../images/agentic-video-understanding-in-gemini/
stills_count: 15
extractor:
  model: gemini-3.8-flash
  processing: static
  resolution: default
  processing_rounds: 0
  frame_rule: end of display window minus 1s
acquired: '2026-10-01'
usage:
  total_tokens: 21465
  total_input_tokens: 18398
  total_cached_tokens: 0
  total_output_tokens: 1845
  total_thought_tokens: 1222
  total_tool_use_tokens: 0
notes: |
  Machine-read by gemini-3.8-flash; unverified. Stills are gitignored (raw/**/*.png).
  At Process, view each PNG, correct the reading against the pixels, and
  publish the selected stills as webp under wiki/assets/<source-page-slug>/.
---

# Stills: Agentic video understanding in Gemini

Machine-read by `gemini-3.8-flash` (static processing) on 2026-10-01. **Unverified**: view each PNG and correct the reading before it reaches the wiki.

## 01 · [0:13] Video Frame Representation

- Kind: diagram
- On screen: 0:05–0:14 · still taken at 0:13
- File: `../images/agentic-video-understanding-in-gemini/01-00m13-video-frame-representation.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=13s

On-screen content (machine-read):

```text
~20 minutes long
```

Adds vs. narration (machine-read): Shows a stack of video frames representing a 20-minute long input video.

## 02 · [0:20] Splitting Video into Extracted Frames

- Kind: diagram
- On screen: 0:15–0:21 · still taken at 0:20
- File: `../images/agentic-video-understanding-in-gemini/02-00m20-splitting-video-into-extracted-frames.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=20s

On-screen content (machine-read):

```text
~20 minutes long
↓
frame 1 | frame 2 | frame 3 | frame 4 | ... | frame n
```

Adds vs. narration (machine-read): Visualizes extracting sequential frames from the 20-minute video.

## 03 · [0:27] Feeding Extracted Frames into Gemini

- Kind: diagram
- On screen: 0:22–0:28 · still taken at 0:27
- File: `../images/agentic-video-understanding-in-gemini/03-00m27-feeding-extracted-frames-into-gemini.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=27s

On-screen content (machine-read):

```text
~20 minutes long
↓
frame 1 | frame 2 | frame 3 | frame 4 | ... | frame n
↓
Gemini
```

Adds vs. narration (machine-read): Illustrates all extracted frames being directed into the Gemini model.

## 04 · [0:40] Token Cost of Full Video Frames

- Kind: diagram
- On screen: 0:29–0:41 · still taken at 0:40
- File: `../images/agentic-video-understanding-in-gemini/04-00m40-token-cost-of-full-video-frames.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=40s

On-screen content (machine-read):

```text
~20 minutes long
↓
frame 1 | frame 2 | frame 3 | frame 4 | ... | frame n
↓
Gemini
~121,943 tokens
```

Adds vs. narration (machine-read): Quantifies the high token footprint (~121,943 tokens) of sending all frames.

## 05 · [0:52] Locating Relevant Information in Video Frames

- Kind: diagram
- On screen: 0:42–0:53 · still taken at 0:52
- File: `../images/agentic-video-understanding-in-gemini/05-00m52-locating-relevant-information-in-video-frames.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=52s

On-screen content (machine-read):

```text
~20 minutes long
↓
[frame 1 (inactive)] | [frame 300 (inactive)] | [frame 600 (inactive)] | frame 900 (highlighted) | ... | [frame n (inactive)]
frame 900 -> Relevant Information!
↓
Gemini
```

Adds vs. narration (machine-read): Highlights that only a specific frame (frame 900) contains the relevant information needed.

## 06 · [1:05] "Naive" Processing Overview

- Kind: diagram
- On screen: 0:54–1:06 · still taken at 1:05
- File: `../images/agentic-video-understanding-in-gemini/06-01m05-naive-processing-overview.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=65s

On-screen content (machine-read):

```text
"Naive" Processing
~20 minutes long
↓
frame 1 | frame 300 | frame 600 | frame 900 | ... | frame n
↓
Gemini
```

Adds vs. narration (machine-read): Categorizes the full-frame ingestion approach as 'Naive' Processing.

## 07 · [1:14] Naive Processing vs Agentic Video Understanding - URL Reference

- Kind: diagram
- On screen: 1:07–1:15 · still taken at 1:14
- File: `../images/agentic-video-understanding-in-gemini/07-01m14-naive-processing-vs-agentic-video-understanding-url-referenc.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=74s

On-screen content (machine-read):

```text
"Naive" Processing | Agentic Video Understanding
[Naive processing diagram] | https://www.youtube.com/watch?v=sDPDGQFoUMM
| ↓
| Gemini
```

Adds vs. narration (machine-read): Shows that agentic video understanding passes a URL reference instead of raw video frames.

## 08 · [1:28] Agentic Video Understanding - Transcript Retrieval Tool

- Kind: diagram
- On screen: 1:16–1:29 · still taken at 1:28
- File: `../images/agentic-video-understanding-in-gemini/08-01m28-agentic-video-understanding-transcript-retrieval-tool.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=88s

On-screen content (machine-read):

```text
"Naive" Processing | Agentic Video Understanding
[Naive processing diagram] | https://www.youtube.com/watch?v=sDPDGQFoUMM
| ↓
| Gemini
| ↓
| get_transcript()
| ↓
| 0:00 Welcome to a visual guide to Mixture of Experts!
| 0:03 My name is Maarten and today, we are going through ...
| 0:12 So, keep in mind that whatever your learn about LLMs ...
```

Adds vs. narration (machine-read): Demonstrates the model invoking `get_transcript()` to inspect video content before extracting visual frames.

## 09 · [1:52] Agentic Video Understanding - Targeted Frame Extraction Tool

- Kind: diagram
- On screen: 1:30–1:53 · still taken at 1:52
- File: `../images/agentic-video-understanding-in-gemini/09-01m52-agentic-video-understanding-targeted-frame-extraction-tool.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=112s

On-screen content (machine-read):

```text
"Naive" Processing | Agentic Video Understanding
[Naive processing diagram] | [URL -> Gemini -> get_transcript() -> transcript text]
| ↓
| get_frames(start, end, fps)
| ↓
| frame 1 | frame 300
```

Adds vs. narration (machine-read): Shows the `get_frames(start, end, fps)` tool call targeting specific timestamps and frame rates.

## 10 · [2:03] Standard Question Answering Flow

- Kind: diagram
- On screen: 1:54–2:04 · still taken at 2:03
- File: `../images/agentic-video-understanding-in-gemini/10-02m03-standard-question-answering-flow.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=123s

On-screen content (machine-read):

```text
Query (video input) -> Gemini -> Answer
```

Adds vs. narration (machine-read): Illustrates the baseline one-pass query-to-answer architecture.

## 11 · [2:09] Agentic Pipeline - Think Step

- Kind: diagram
- On screen: 2:05–2:10 · still taken at 2:09
- File: `../images/agentic-video-understanding-in-gemini/11-02m09-agentic-pipeline-think-step.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=129s

On-screen content (machine-read):

```text
Query (video input) -> Gemini -> Think
```

Adds vs. narration (machine-read): Shows Gemini entering a 'Think' reasoning step instead of answering immediately.

## 12 · [2:26] Agentic Pipeline - Available Tools: Transcript and Frames

- Kind: diagram
- On screen: 2:11–2:27 · still taken at 2:26
- File: `../images/agentic-video-understanding-in-gemini/12-02m26-agentic-pipeline-available-tools-transcript-and-frames.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=146s

On-screen content (machine-read):

```text
Query (video input) -> Gemini -> Think
Think -> get_transcript()
Think -> get_frames(start, end, fps)
```

Adds vs. narration (machine-read): Lists available tool options: `get_transcript()` and `get_frames(start, end, fps)`.

## 13 · [2:33] Agentic Pipeline - Available Tools: Audio Added

- Kind: diagram
- On screen: 2:28–2:34 · still taken at 2:33
- File: `../images/agentic-video-understanding-in-gemini/13-02m33-agentic-pipeline-available-tools-audio-added.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=153s

On-screen content (machine-read):

```text
Query (video input) -> Gemini -> Think
Think -> get_transcript()
Think -> get_frames(start, end, fps)
Think -> get_audio(start, end)
```

Adds vs. narration (machine-read): Adds `get_audio(start, end)` to the list of inspectable modalities.

## 14 · [2:50] Agentic ReAct Loop with Observation

- Kind: diagram
- On screen: 2:35–2:51 · still taken at 2:50
- File: `../images/agentic-video-understanding-in-gemini/14-02m50-agentic-react-loop-with-observation.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=170s

On-screen content (machine-read):

```text
Query (video input) -> Gemini -> Think
Think -> Tools:
- get_transcript()
- get_frames(start, end, fps)
- get_audio(start, end)
Tools -> Observation (video frames) -> Gemini
```

Adds vs. narration (machine-read): Diagrams the cyclic observation loop returning extracted frames to Gemini.

## 15 · [2:53] Agentic ReAct Loop Final Output

- Kind: diagram
- On screen: 2:52–2:54 · still taken at 2:53
- File: `../images/agentic-video-understanding-in-gemini/15-02m53-agentic-react-loop-final-output.png`
- At this moment: https://www.youtube.com/watch?v=ytjgy30Cono&t=173s

On-screen content (machine-read):

```text
Observation -> Gemini -> Answer
Gemini <-> Think / Tools / Observation loop
```

Adds vs. narration (machine-read): Shows the agentic cycle terminating with the final generated answer.
