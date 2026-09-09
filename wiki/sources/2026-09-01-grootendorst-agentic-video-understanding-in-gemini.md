---
type: source
kind: video
title: "Agentic video understanding in Gemini"
author: ["Google for Developers"]
publisher: "Google for Developers (YouTube); speaker Maarten Grootendorst, Google DeepMind"
url: "https://www.youtube.com/watch?v=ytjgy30Cono"
date_published: 2026-09-01
date_ingested: 2026-09-09
length: "~3:19 minutes (transcript ~520 words / 66 ASR segments; auto-generated transcript) — a short technical explainer, not a talk"
raw: "../../raw/videos/agentic-video-understanding-in-gemini.md"
tags: [gemini, google-deepmind, maarten-grootendorst, agentic-video-understanding, multimodal, tool-use, get-transcript, get-frames, variable-fps, agentic-loop, react-loop, context-economy, token-cost, retrieval-over-stuffing, selective-attention, reference-not-payload]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
relationships:
  - type: supports
    target: 2022-10-06-yao-et-al-react-synergizing-reasoning-acting
    via: "A vendor implementation of exactly the loop ReAct named, four years on and in a modality ReAct never addressed. Grootendorst narrates it in ReAct's own terms — the model thinks about which tool to use, acts, gets an observation back, and decides whether to loop again — and the payoff is ReAct's too: grounding the answer in retrieved observations rather than in what the model can infer from a fixed dump of context."
    confidence: 0.8
  - type: supports
    target: 2026-06-03-chopra-headroom-context-optimization-layer-for-llm-applications
    via: "The same economics argued at two layers of the stack. Headroom optimises what reaches the context window in a text application; this applies the identical logic to video, where the naive path costs 100,000+ tokens for a single file and most of it is irrelevant to the query. Both make the non-obvious claim that reducing what the model sees improves accuracy rather than trading it away — here because the agent can spend its budget on high-FPS sampling of the seconds that matter."
    confidence: 0.7
---

# Agentic video understanding in Gemini

> Processing long videos can use a lot of tokens. Learn how to do this more efficiently using our latest agentic video understanding capability available in Gemini 3.7 Flash, 3.6 Flash, and 3.5 Flash-Lite. In this video, Google DeepMind's Maarten Grootendorst explains how agentic video understanding works, and how this approach reduces token costs while improving accuracy on the parts of the video that actually matter.
>
> *— Channel description, [[Google]] for Developers*

A **3-minute technical explainer** by **Maarten Grootendorst** of [[Google DeepMind]], describing a capability shipped in the Gemini Flash line: instead of passing a video to the model as payload, pass a **reference** to it plus tools, and let the model run an agentic loop that fetches only the parts it needs.

Short, but it earns a source page because it is the cleanest small statement in the corpus of a principle the wiki holds in many long-form versions: **give the model a handle and the means to fetch, not the whole artifact** — and because it reports the counterintuitive half of that claim, that fetching less *improves* accuracy rather than trading it for cost.

## TL;DR

- **The naive baseline and its cost.** The standard approach splits a video into frames and passes them all: *"If we give the entire video to Gemini, there will be already more than 100,000 tokens. That's a lot, and there's a lot of information that we really don't need — because what if I only want information in frame 900, or a couple of seconds here, a couple of seconds there?"*
- **The move: a reference plus tools instead of payload.** *"With agentic video understanding, we don't give the model the entire video. We give the reference to the video"* — and the model decides what to pull. Three tools are named: **`get_transcript`** (cheap, coarse, usually first), **`get_frames`** (with the model specifying *which* frames and at what **frames-per-second** — *"a great way of getting either a very global or localized perspective"*), and **`get_audio`**.
- **It is an explicit agentic loop.** *"The model first thinks about which tools it might want to use to process this video… It runs those tools — I mean, this is an agentic loop — and it gets an observation in return, frames for instance. And this information is then given back to the model where it can decide to do another loop. And then we have this very traditional agentic loop of thinking, acting, observing, and looping until it finally arrives at the answer."*
- **The worked trajectory.** Pull the transcript first to locate roughly what happens where; notice something at the five-minute mark; then re-sample *that* region at a higher frame rate to see it properly. Variable FPS is the mechanism by which the agent trades breadth for depth where it matters.
- **The claim that makes it interesting.** *"Not only does it reduce the number of tokens it really needs, the performance increases — because it can zoom in on certain functions and really pay attention to the things in the video that are actually important to the query."* Cost and accuracy move together rather than trading off.

## Why this matters to the wiki

**1. It is a modality-crossing instance of the wiki's central retrieval claim.** The corpus establishes at length — [[is-rag-dead|in the RAG synthesis]], in [[agent-harness]]'s context layer, in [[knowledge-architectures-for-llm-agents]] — that stuffing a context window is inferior to letting an agent fetch selectively, and that this holds even as windows grow. Every one of those sources argues it over *text*. This argues it over *video*, where the token economics are an order of magnitude harsher and the tools are physically different (frame sampling, audio extraction), and reaches the same conclusion. Cross-modality convergence is worth more than another text instance.

**2. It is the tightest available illustration of latent-versus-deterministic computation.** [[2026-08-06-garry-tan-own-your-intelligence|Tan]], five weeks earlier, claims that confusing the two *"causes every agent failure I've ever seen"*: judgment belongs in latent space, exact retrieval belongs in code. Agentic video understanding is that rule applied to perception — *what happens at 5:03* is not something to infer from a subsampled global view, it is something to go and fetch at high FPS. Neither source cites the other; they are the same principle at different altitudes.

**3. Variable-FPS sampling is a concrete instance of an agent controlling its own resolution.** [[2026-09-07-yc-paper-club-why-the-harness-matters-more-than-the-model|Karten's expressibility argument]] is that a harness should expose primitives the model can drive rather than a fixed control flow — and that QM's win was *"pushing that decision into the agent itself rather than the harness."* Choosing frames-per-second per region is exactly that pattern in a perceptual setting: the harness does not pick a sampling rate, the model does, per query and per region.

## Dynamic-capabilities reading

`digital-seizing/rapid-prototyping` is the only cell that genuinely applies: this is a shipped capability announcement aimed at developers, whose function is to let builders try a cheaper architecture immediately. The source is otherwise **outside the Warner & Wäger lens** — it is a technical mechanism, not an account of organisational transformation — and the tagging is kept deliberately thin rather than stretched, per the schema's guidance not to force sources into the vocabulary.

## Linked entities and concepts

- **Entities**: [[Google DeepMind]] (the speaker's affiliation and the model's origin), [[Google]] (the developer channel and Gemini).
- **Concepts**: [[react-reasoning-acting]] (the loop, narrated in ReAct's own vocabulary), [[agent-harness]] (tool design and context economy), [[ai-agents]] (tool-driven selective perception), [[foundation-models]] (a capability of the Gemini Flash line), [[document-intelligence]] (extracting structure from an unstructured artifact by targeted retrieval).
- **Dangling** (single-source mention, deferred): **Maarten Grootendorst**, **Gemini 3.7 Flash / 3.6 Flash / 3.5 Flash-Lite**. Promote on a second citing source per the author-entity promotion rule.

## Debates and supersession

- **No numbers.** The performance claim — that accuracy *increases* while tokens fall — is asserted without a benchmark, a baseline comparison or an error bar, in a three-minute vendor explainer. The mechanism is plausible and consistent with the wiki's text-domain evidence, but the wiki should carry it as a **vendor claim about its own product**, not as a measured result. The linked resources page is an **ingest target** if it carries evaluation data.
- **Open question — what does the agent do when the transcript is misleading?** The described trajectory leans on `get_transcript` as the cheap first probe that tells the model where to look. For videos where the salient content is unspoken — a demonstration, a chart, a silent action — the cheap probe points nowhere useful, and the source does not say how the loop recovers or whether it degrades to dense sampling at full cost. This is the obvious failure mode of a coarse-to-fine strategy and it is unaddressed.
- **Scope note.** This is a capability of specific Gemini Flash models, not a general architectural claim about multimodal models. The wiki should not generalise it to "video understanding is now agentic" without further sources.

## What was actually ingested

Full 3:19 transcript (auto-generated English captions, 66 segments). The speaker is not named in the audio; the attribution to **Maarten Grootendorst** and the affiliation to Google DeepMind come from the channel description, as do the specific model versions. The video is heavily diagrammatic — the naive-versus-agentic pipeline comparison is carried visually — and **no slide content was ingested**; the architecture described here is as *narrated*. The linked resources page was not fetched.
