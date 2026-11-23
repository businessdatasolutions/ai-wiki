---
video_id: yp0PNs50cA0
url: https://www.youtube.com/watch?v=yp0PNs50cA0
transcript: raw/videos/chinas-bet-on-physical-ai.md
stills_dir: raw/images/chinas-bet-on-physical-ai
stills_count: 1
extractor:
  method: hand-picked (no Gemini call)
  reason: Gemini API returned 402 (prepayment credits depleted)
  sampling: 363 frames at 360p, one every 2 s, consecutive repeats merged (160x90 grayscale MAD < 1.5) into 1 tile covering 0:00-12:04, read as one contact sheet
  dense_pass: 1,450 frames at 64x36 grayscale, one every 0.5 s over the whole video, each compared with the first frame (largest mean absolute difference 0.01 on a 0-255 scale); plus ffmpeg scene detection at the native frame rate (threshold 0.05), which found no cut
  frames: yt-dlp stream URL (<=1080p; this video's best stream is 720p) seeked with ffmpeg
acquired: '2026-11-23'
---

# Stills manifest (hand-picked)

The whole video is one static card: Morgan Stanley's audio podcast *Thoughts on the Market* published on YouTube over its title art, with no speaker footage, slides, charts or captions on screen. Every grid frame merged into a single tile, the half-second pass found no frame that differs from the first, and scene detection found no cut. The card was cut once at full resolution and read; it carries the episode's date, which differs from the YouTube publish date. Nothing was published: every figure in the episode is spoken only.

## 01 · 6:00 · Thoughts on the Market title card
- File: `01-06m00-thoughts-on-the-market-title-card.png` · [6:00](https://www.youtube.com/watch?v=yp0PNs50cA0&t=360s)
- On a dark-blue background with teal and blue wave graphics: *Morgan Stanley* (wordmark) / **THOUGHTS ON THE MARKET** / *China's Bet on Physical AI* / *NOVEMBER 20, 2026*. The same card is on screen from 0:00 to the end (12:05). The date is the podcast episode's (a Friday; the closing line says *"Join us Monday for part two"*); YouTube's `publish_date` is Monday 23 November 2026. **Not published:** a title card (navigation); its date is recorded here and on the source page.
