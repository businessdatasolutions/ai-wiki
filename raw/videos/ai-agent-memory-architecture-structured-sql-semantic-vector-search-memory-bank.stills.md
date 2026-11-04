---
video_id: 8C4bh59FtsI
url: https://www.youtube.com/watch?v=8C4bh59FtsI
transcript: raw/videos/ai-agent-memory-architecture-structured-sql-semantic-vector-search-memory-bank.md
stills_dir: raw/images/ai-agent-memory-architecture-structured-sql-semantic-vector-search-memory-bank
stills_count: 6
extractor:
  method: hand-picked (no Gemini call)
  reason: no Gemini API key on this machine (repo .env absent), so extract_stills.py could not run
  sampling: 62 frames at 360 px, one every 12 s from 0:05, read as 4x4 contact sheets
  frames: yt-dlp stream URL (<=1080p) seeked with ffmpeg, no download
acquired: '2026-11-04'
---

# Stills manifest (hand-picked)

Each still was chosen from the contact sheets and then read at full resolution. The video's slides animate in; frames were taken where the sheet showed the diagram complete.

## 01 · 5:17 · The rule: exact or fuzzy?
- File: `01-05m17-the-rule-exact-or-fuzzy.png` · [5:17](https://www.youtube.com/watch?v=8C4bh59FtsI&t=317s)
- "What did I buy?" → exact → Cloud SQL (the actual row); "What do I usually like?" → fuzzy → vector store (similar memories). **Published.**

## 02 · 6:53 · Session start
- File: `02-06m53-session-start-read-both.png` · [6:53](https://www.youtube.com/watch?v=8C4bh59FtsI&t=413s)
- Sequence diagram: Agent reads facts from Cloud SQL (rows), searches the vector store by meaning (memories). **Published.**

## 03 · 7:53 · Two tracks (partial)
- File: `03-07m53-two-tracks-write-facts.png` · [7:53](https://www.youtube.com/watch?v=8C4bh59FtsI&t=473s)
- Sequence diagram, synchronous fact write only ("add that blazer" → add_to_wishlist() → saved → "done"); the Memory Bank lane is still empty. **Not published**: build state.

## 04 · 8:41 · Judgment
- File: `04-08m41-judgment-only-strong-signals.png` · [8:41](https://www.youtube.com/watch?v=8C4bh59FtsI&t=521s)
- Three signals into a memory service; two kept as long-term memory, "maybe yellow today" dropped; "only strong signals". **Published.**

## 05 · 9:53 · Off the live path
- File: `05-09m53-keep-extraction-off-the-live-path.png` · [9:53](https://www.youtube.com/watch?v=8C4bh59FtsI&t=593s)
- Live audio turns on top, background extraction below; "keep extraction off the live path". **Published.**

## 06 · 11:29 · Recap (partial)
- File: `06-11m29-recap-architecture.png` · [11:29](https://www.youtube.com/watch?v=8C4bh59FtsI&t=689s)
- Agent over a MEMORY box with Cloud SQL and vector store; only the Cloud SQL caption has appeared. **Not published**: build state.
