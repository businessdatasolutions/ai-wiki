---
video_id: y1-9yeYLJUo
url: https://www.youtube.com/watch?v=y1-9yeYLJUo
transcript: raw/videos/the-rise-of-ai-coworkers.md
stills_dir: raw/images/the-rise-of-ai-coworkers
stills_count: 8
extractor:
  method: hand-picked (no Gemini call)
  reason: Gemini API returned 402 (prepayment credits depleted)
  sampling: 361 frames at 360p, one every 10 s, consecutive repeats merged (160x90 grayscale MAD < 1.5) into 350 tiles, read as 5x6 contact sheets; second pass: ffmpeg scene detection (threshold 0.3), the 69 shots shorter than 10 s tiled from their middle frames
  frames: yt-dlp stream URL (<=1080p) seeked with ffmpeg
acquired: '2026-11-17'
---

# Stills manifest (hand-picked)

All 350 tiles were viewed. The episode is a studio conversation; Lauren Tan's screen, a page in a whiteboard document titled *quality & quantity*, is inserted full-frame with the studio as picture-in-picture at four points: a sales diagram (12:30), her Slack demo thread (23:20–24:49), the "smallest loop" drawing (40:20–42:49) and the inverted pyramid (45:50, shown again at 47:20, 48:20 and 51:30). Each still was cut at full resolution and read from the pixels; the source page carries the verified transcriptions. Skipped as navigation: the *Lightcone* title card (0:20) and a ycombinator.com/apply insert (32:00).

## 01 · 12:30 · Loops for sales
- File: `01-12m30-loops-for-sales-shared-bots.png` · [12:30](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=750s)
- "loops for sales": "How the SpaceXSI Sales team uses Shared Bots to automate the deal cycle". Account Intel Bot → (requests quotes) → Quote Bot ⇄ Deal Bot (escalates exceptions / returns approved terms). Frame cut at 12:38, where the heading is still in view. **Published.**

## 02 · 23:20 · Slack thread in #grok-bot-canvas
- File: `02-23m20-slack-thread-grok-bot-canvas.png` · [23:20](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=1400s)
- Lauren Tan asks her bot @poteto what it would take for Grok Bot canvas to build arbitrary UI inside the chat transcript; poteto starts an "inline UI scoping agent" in the cloud; a colleague comments; the agent recommends bringing Glass's `visualize` feature to Grok Bot. Messages dated Oct 11th. **Published.**

## 02b · 23:56 · The bot's report: gated prototype and a security gap
- File: `02b-23m56-prototype-done-and-security-gap.png` · [23:56](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=1436s)
- Two later poteto messages in the thread (Oct 11th, 6:54 PM and 10:40 PM): prototype built behind an off-by-default gate; draft PR #1123299 behind the `sand_visualizations` gate; inline D3 and three.js visuals working; "One security gap before the gate goes on for anyone": agent-written HTML can reach an outside server over WebRTC. On screen for about a second while scrolling; the 10-second grid skipped it, and the short-shot pass (added 2026-11-17 by the orchestrator) found it. **Published.**

## 03 · 24:00 · Thread attachments, inline visuals
- File: `03-24m00-thread-attachments-inline-visuals.png` · [24:00](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=1440s)
- Two screenshot attachments from the cloud agent: Grok Bot rendering an interactive D3 line chart and an interactive 3D desk scene inline, in chats titled "Visualize D3 proof (inline visuals PR)" and "Visualize 3D proof (inline visuals PR)"; below them a demo video, "…3D visuals in Grok Bot: interacting, scrolling past, and scrolling back". Frame cut at 24:28 (zoomed in, legible). **Published.**

## 04 · 40:20 · Smallest loop, inner loop only
- File: `04-40m20-smallest-loop-inner-loop.png` · [40:20](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=2420s)
- write good code → run the code → find issues with code → (back). Frame cut at 42:01, the last view before the outer loop is added. **Not published:** earlier build state of still 05; kept because it shows the "find issues with code" label that the picture-in-picture covers in 05.

## 05 · 42:00 · Smallest loop with the outer loop
- File: `05-42m00-smallest-loop-with-outer-loop.png` · [42:00](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=2520s)
- The inner loop plus "datadog alert → repros → run the code". Fully built state, cut at 42:09; later frames (42:20–42:49) zoom in and crop the left side. **Published.**

## 06 · 45:50 · Inverted pyramid
- File: `06-45m50-inverted-pyramid-whenever-you-correct-your-agent.png` · [45:50](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=2750s)
- "whenever you correct your agent": codebase / static analysis / prose (rules, skills, agents.md) / human review, widest to narrowest. Cut at 46:08; the reappearances at 47:20, 48:20 and 51:30 show the same drawing unchanged. **Published.**

## 07 · 59:50 · Closing credits
- File: `07-59m50-closing-credits.png` · [59:50](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=3590s)
- Hosts: Garry Tan, Diana Hu, Jared Friedman. Guests: Lauren Tan, Roman Ugarte. Producer: Matt Kang. Editor: Amanda Deisler. Camera: Chris Hall, Ryan Loughlin. **Not published:** credits card (navigation); it names the hosts the transcript leaves unnamed, which the source page records in prose.
