---
type: source
kind: video
title: "AI Agent Memory Architecture: Structured SQL, Semantic Vector Search & Memory Bank"
author: ["Google Cloud Tech"]
publisher: "Google Cloud Tech — The Omni App series, presented by Annie Wang"
url: "https://www.youtube.com/watch?v=8C4bh59FtsI"
date_published: 2026-10-28
date_ingested: 2026-11-04
length: "~12:26 minutes (transcript ~77 lines + 4 stills)"
raw: "../../raw/videos/ai-agent-memory-architecture-structured-sql-semantic-vector-search-memory-bank.md"
stills: "../../raw/videos/ai-agent-memory-architecture-structured-sql-semantic-vector-search-memory-bank.stills.md"
tags: [google-cloud-tech, annie-wang, the-omni-app, agent-memory, long-term-memory, short-term-memory, structured-memory, semantic-memory, cloud-sql, postgres, pgvector, alloydb, memory-bank, vertex-ai-agent-engine, gemini-live-api, multimodal-agents, voice-agents, async-extraction, hot-path]
relationships:
  - type: supports
    target: 2026-05-08-bratanic-unified-agentic-memory-hooks
    via: "write cheap records at once and distil understanding in a separate model pass off the live path: Wang's async extraction into a memory service, Bratanic's dream phase after hooks have logged the events"
    confidence: 0.65
---

# Wang (Google Cloud Tech) — agent memory: facts in SQL, understanding in a vector store

> In this episode, you'll learn the critical difference between Structured Facts and Semantic Understanding, why they should never live in the same database, what to do with raw audio/video perception, and how to read and write memory asynchronously without blocking latency-sensitive voice streams.
>
> Watch along and learn: Short-Term (RAM) vs. Long-Term Agent Memory · Facts (Exact Lookup) vs. Understanding (Semantic Recall) · Why dumping exact facts into a vector store breaks your agent · Where to store Structured Memory (PostgreSQL, MySQL, Google Cloud SQL) vs. Semantic Memory (pgvector, AlloyDB, Vertex AI Agent Engine Memory Bank) · How to handle raw multimodal perception (camera frames & audio waveforms) · The Two-Track Read/Write Loop: Synchronous tool calls for facts vs. asynchronous off-the-hot-path extraction for understanding

## TL;DR

A 12-minute explainer on the [[Google]] channel *Google Cloud Tech*, published 28 October 2026, in its series *The Omni App*, presented by **[[Annie Wang]]**. The demo is a personal styling agent with a voice interface that remembers a user's wishlist and taste across sessions. Four rules:

1. **Session memory is RAM.** *"The real design question is not can we save everything. The real question is, what is worth carrying into the next session."*
2. **Two kinds of long-term memory, two stores.** Facts (*"you bought the blue jacket"*) are exact, have IDs and dates, and belong in a structured database such as Cloud SQL or Postgres. Understanding (*"you prefer simple over flashy"*) is a pattern and belongs in a store searched by meaning: pgvector, AlloyDB, or a managed service such as Vertex AI Agent Engine's **Memory Bank**, which also extracts and updates memories from sessions.
3. **Raw perception is not memory.** Camera frames and audio waveforms may be kept for replay, audit or training, but agent memory keeps the meaning extracted from them.
4. **Two tracks for reading and writing.** At session start, load both. Write facts at once through a tool call; extract understanding asynchronously, *"off the live path,"* because extraction needs a model and a voice agent cannot wait for it.

## Key claims

### The common mistake

*"They hear semantic memory and they put everything into the vector store."* Similarity is useful when the question is fuzzy and *"dangerous when the answer must be exact."* Asked *"what did I buy,"* the agent should query the database, not guess from a similar memory.

### Judgment before writing to memory

Understanding is not updated from one sentence: *"If I say maybe I like yellow today, that does not mean yellow is … my whole style."* A memory service reviews the conversation and keeps only strong signals, such as a reason the user gives or a pattern repeated across sessions. Extraction can run per turn or at intervals, not only at session end; per-turn extraction gives cleaner memories and keeps what a user said before dropping off.

### Not tied to one product

*"The lesson is not, you must use memory bank. The lesson is understanding goes in a system that can search by meaning."* With a plain vector store you write the extraction logic yourself; with Memory Bank it is managed.

## Visual canon

### 1 · The rule: exact or fuzzy?

![[assets/2026-10-28-wang-google-cloud-tech-agent-memory-architecture/01-05m17-the-rule-exact-or-fuzzy.webp|The rule, exact or fuzzy]]

*Still at [5:17](https://www.youtube.com/watch?v=8C4bh59FtsI&t=317s) from Google Cloud Tech, "AI Agent Memory Architecture: Structured SQL, Semantic Vector Search & Memory Bank".*

**THE RULE.** *"What did I buy?"* and *"What do I usually like?"* both enter *exact or fuzzy?* — **exact** → **Cloud SQL**, *the actual row*; **fuzzy** → **vector store**, *similar memories*.

*Still vs. transcript:* the narration gives the two example questions separately; the diagram makes the routing decision the single test that sends each question to one store.

### 2 · Session start reads both stores

![[assets/2026-10-28-wang-google-cloud-tech-agent-memory-architecture/02-06m53-session-start-read-both.webp|Session start, read facts and search by meaning]]

*Still at [6:53](https://www.youtube.com/watch?v=8C4bh59FtsI&t=413s) from Google Cloud Tech, "AI Agent Memory Architecture: Structured SQL, Semantic Vector Search & Memory Bank".*

**SESSION START.** Lanes: User, Agent, Cloud SQL, vector store. Agent → Cloud SQL: *read facts*, ← *rows*. Agent → vector store: *search by meaning*, ← *memories*. The User lane has no traffic yet.

*Still vs. transcript:* the sequence diagram shows that both reads happen before the user has said anything.

### 3 · Judgment: only strong signals

![[assets/2026-10-28-wang-google-cloud-tech-agent-memory-architecture/04-08m41-judgment-only-strong-signals.webp|Judgment, only strong signals kept]]

*Still at [8:41](https://www.youtube.com/watch?v=8C4bh59FtsI&t=521s) from Google Cloud Tech, "AI Agent Memory Architecture: Structured SQL, Semantic Vector Search & Memory Bank".*

**JUDGMENT.** Three signals enter a *memory service*: *simple > flashy ×3*, *no wool, I run warm*, *maybe yellow today*. It **keeps** *simple > flashy* and *runs warm* in **long-term memory**; *✗ yellow, dropped*. Caption: *only strong signals*.

*Still vs. transcript:* the slide shows the repetition count (×3) as what makes a preference strong, and the explicit drop of the one-off remark.

### 4 · Keep extraction off the live path

![[assets/2026-10-28-wang-google-cloud-tech-agent-memory-architecture/05-09m53-keep-extraction-off-the-live-path.webp|Off the live path, extraction in the background]]

*Still at [9:53](https://www.youtube.com/watch?v=8C4bh59FtsI&t=593s) from Google Cloud Tech, "AI Agent Memory Architecture: Structured SQL, Semantic Vector Search & Memory Bank".*

**OFF THE LIVE PATH.** *live audio*: turn 1, turn 2, turn 3. *background*: *✦ extract* after turn 1 and after turn 3. Caption: *keep extraction off the live path*.

*Still vs. transcript:* the timeline shows extraction triggered by turns but running beneath them, not after every turn, and never in the audio lane.

## How it connects

- [[concepts/agent-harness|agent-harness]] — memory as a harness component, with a design split by what the memory is for.
- [[concepts/ai-agents|ai-agents]] — long-term memory for multimodal, voice-first agents.
- [[concepts/knowledge-graphs|knowledge-graphs]] — a neighbouring answer to the same question (structure for exact relations, retrieval for meaning).

## Related in this wiki

- [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic on agent memory with hooks]] — hooks log events deterministically with no model call, and a separate *dream* pass distils them into memory. Wang's design has the same split: cheap synchronous writes, model-based extraction kept off the latency-sensitive path.
- [[2026-11-02-holmes-warp-agentic-self-improvement-loop|Holmes (Warp)]] — the other way to learn from past sessions in this batch: scoring runs and changing skills, not storing what the user is like.
- Annie Wang's earlier explainers on the same channel: [[2026-09-03-thurium-wang-google-cloud-graph-engineering-101|graph engineering]] and [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails|four ways loop engineering fails]].

## What was actually ingested

The full video (12:26, `length_seconds: 746`), 77 lines, through the yt-dlp fallback from a track listed as human-written. Its quality is closer to ASR (*"Facts instruction"* for *facts in structured*, *"like classical"* for *like Cloud SQL*, *"Anaia"* for Annie); quotes here are corrected against the slides and the description. **Stills were picked by hand**: no Gemini key on this machine. 62 frames sampled every 12 seconds, 6 candidates read at 1080p, 4 published; two were caught mid-animation and dropped. See the manifest. The demo's code (linked as *fashion-mind*) was not read.

## Linked entities and concepts

- [[Google]] — publisher (Google Cloud Tech channel). Updated in this ingest.
- [[Annie Wang]] — presenter. Updated in this ingest.
- [[concepts/agent-harness|agent-harness]], [[concepts/ai-agents|ai-agents]] — updated in this ingest.

**Dangling** (single-source mention, deferred): Memory Bank (Vertex AI Agent Engine), Cloud SQL, AlloyDB, Gemini Live API, The Omni App.

No `dynamic_capabilities:`: an architecture explainer, outside the Warner & Wäger lens.

## Scope and reliability

A vendor explainer that names its own products, though it says the pattern works without them. The design is reasoned, not measured: nothing here compares memory quality or latency between the single-store and two-store designs. The demo is a consumer styling agent; the advice is aimed at voice agents, where latency rules out synchronous extraction.
