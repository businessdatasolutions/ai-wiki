---
type: source
kind: video
title: "What is an Agentic Harness?"
author: ["Google Cloud Tech"]
publisher: "Google Cloud (Google Cloud Tech YouTube channel — *AI Builder Essentials* series); speakers Greg Baugues and Tilde Thurium"
url: "https://www.youtube.com/watch?v=W9BX0jyzd2k"
date_published: 2026-07-16
date_ingested: 2026-08-20
length: "~2:55 minutes (human-curated en-US captions; transcript ~121 lines / ~580 words) — a two-person conversational explainer, not a talk"
raw: "../../raw/videos/what-is-an-agentic-harness.md"
tags: [google-cloud, google-cloud-tech, ai-builder-essentials, greg-baugues, tilde-thurium, agent-harness, harness-definition, simon-willison, agent-definition, function-calling, tool-use, agent-loop, harness-vs-interface, antigravity, claude-code, codex, vendor-explainer, definitional-source]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: 2026-05-07-chatterjee-anatomy-of-agent-harness
    via: "Baugues' *\"the harness is everything after the LLM\"* is a compressed restatement of Chatterjee's layered anatomy, arrived at independently and from a competing vendor. Chatterjee supplies the layer-by-layer decomposition and the *model is rented, harness is owned* claim; Baugues supplies the same boundary as a single sentence plus the components he enumerates to fill it (tools, the loop, the programmatic output-evaluator). The convergence matters because the two sources share no lineage — a Google DevRel explainer and an independent practitioner essay draw the boundary in the same place"
    confidence: 0.75
  - type: supports
    target: 2026-05-04-rethinking-agents-harness-is-all-you-need
    via: "both treat the harness as the locus of agent behaviour rather than the model, and both explicitly decouple the harness from the surface a user touches. The Prompt Engineering video establishes this empirically (same model, 6× outcome variance across harnesses; harness transfers between models); Baugues states the same separation definitionally — *\"if you decouple the harness from the interface, the important piece here is how we control the logic and the behavior of the LLM\"* — and names Claude Code, Antigravity and Codex as harnesses that can each carry multiple interfaces"
    confidence: 0.7
  - type: supports
    target: 2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness
    via: "vocabulary ratification across vendors. Trivedy (LangChain, March 2026) is the wiki's source-of-vocabulary for *agent harness*; this Google Cloud explainer is the term appearing four months later as settled enough for a vendor's introductory-education series, with no hedging and no competing coinage offered. The definitional content agrees — harness as the tool-provision plus loop-control plus completion-evaluation layer around a model"
    confidence: 0.65
---

# Baugues & Thurium — What is an Agentic Harness?

> Demystify the concept of an Agentic Harness and learn how they power modern AI systems. In this conversational breakdown, we explore the definition of agents and harnesses, and how both differ from the core LLM and user interfaces.
>
> Watch more AI Builder Essentials → https://goo.gle/AI-Building-101
>
> Speakers: Greg Baugues, Tilde Thurium
> Products Mentioned: Antigravity

## TL;DR

A **2 minute 55 second** two-person explainer on the **Google Cloud Tech** channel, part of the *AI Builder Essentials* introductory series, published 16 July 2026. **Tilde Thurium** asks; **Greg Baugues** answers. Read this page for what it is — a short vendor-produced definitional piece with no evidence, no case study and no numbers. Its value to the wiki is precisely its brevity and its provenance: it is the **agent-harness construct stated as settled vocabulary by a vendor other than the one that coined it**, in a format aimed at newcomers.

Four claims, in the order they are made:

1. **The agent definition is borrowed, and attributed.** Baugues opens by naming his source: *"My favorite is [[Simon Willison]]'s definition. An agent is an LLM with tools running in a loop to accomplish a goal."* He then unpacks each clause — next-token prediction as the model's only native act, function calling as the mechanism that lets the model reach outside its training data, and the loop as the programmatic part.

2. **Tools exist to import context, not to act.** His gloss on function calling is unusually context-flavoured for a tool-use explanation: *"generally speaking, what you're doing is using these functions or tools to go grab context that's external to the LLM, and then to feed that context into the context of your conversation with the LLM, so that it can augment its response. That's the tool portion. How do we give the LLM access to information that's not baked into its training data?"* Action-taking is left implicit; retrieval-into-context is named as the purpose.

3. **The loop's load-bearing part is the evaluator, not the repetition.** *"There's some mechanism there where we are programmatically evaluating the output of the large language model to determine is it done? Has it reached the goal? And if it's not then we feed it more instructions programmatically and then we have it just run in that loop."* The word doing the work is **programmatically** — the completion judgement sits outside the model.

4. **The definition itself — the reason this source earns a page.** *"My definition of an agentic harness: the harness is everything after the LLM. The harness is how do you give it tools? The harness is what programming do you have that's running it in the loop? What programming do you have that is evaluating the output of the LLM to determine if it completed its task or not? And all of that infrastructure — which doesn't have to be a lot, but that is the agentic harness. All that stuff you put around an LLM to turn it into an agent."*

**The harness/interface decoupling is the second substantive contribution**, and it is prompted by Thurium correcting her own prior mental model: *"I had been thinking of the harness as, it's like the IDE, or it's like what's running your agent. But it sounds like your definition is lower level than that."* Baugues confirms and generalises: *"If you think about the most popular agentic harnesses today — so like a Claude Code or an Antigravity or a Codex — there are different interfaces that you can use to interact with that harness."* Thurium restates the implication cleanly: *"if you decouple the harness from the interface, you're saying the important piece here is how we control the logic and the behavior of the LLM. And then you can sort of swap in what interface does the user prefer."* Baugues extends it to the headless case — *"there's probably actually a lot of use cases where you don't even need a user interface. You just need a programmatic interface to the agent, like an autonomous agent"* — and closes with the multiplexing claim: *"coding, your interface is going to look different than it is with a consumer chat app. But it might be the same agentic harness powering all those interactions."*

## What was actually ingested

The **complete** transcript — all 121 caption segments, consistent with `duration: 2:55` / `length_seconds: 175`. The video carries both an auto-generated track and a human-curated `en-US` track; the scraped text matches the curated one (correct casing on Claude Code / Codex / Antigravity, the curly apostrophe in *Simon Willison's*), so effectively no ASR cleanup was needed. No chapters — the video is too short to have them.

**Scope warning.** There is no evidence in this source of any kind: no benchmark, no deployment, no failure mode, no cost, no comparison. It is three minutes of two developer-advocates agreeing on a definition. Cite it for **what the term means and who was using it in July 2026**; do not cite it for any claim about whether harnesses work, which harness is better, or how any of them perform.

## Why a three-minute video earns a page

Two reasons, both about provenance rather than content.

**It is cross-vendor ratification of a construct the wiki has tracked mostly from its originating cluster.** The [[concepts/agent-harness|agent-harness]] page's vocabulary lineage runs through [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy at LangChain]] (source-of-vocabulary, March 2026) and its popularisation through Addy Osmani and the practitioner essays. Google is not in that lineage and is a competitor to both LangChain and Anthropic. When a competitor's introductory-education series uses the term with **no scare quotes, no alternative coinage offered, and no explanation of why the word exists**, that is evidence the construct has stabilised past any one vendor's marketing. Google's own [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Agents CLI announcement]] three months earlier described the same layer without using the word; this video uses the word as the title.

**The harness ≠ interface separation is stated more sharply here than anywhere else in the corpus.** The wiki has held this implicitly — the harness pages discuss CLIs, IDEs and SDKs as delivery surfaces over a common runtime — but Thurium's on-camera correction of her own model (*"I had been thinking of the harness as, it's like the IDE"*) and Baugues' one-line fix make the distinction explicit and quotable. It also names the failure mode the confusion produces: treating a *product* (Claude Code, Antigravity, Codex) as the unit of analysis when the unit is the runtime underneath, which can carry several products.

## Dynamic-capabilities tagging

- **`digital-transforming/improving-digital-maturity`** — the cell's activity list includes *"leveraging digital knowledge inside the firm"*, and this video is a small, literal instance: a vendor's education series doing vocabulary-levelling for builders so that a term used in engineering conversation resolves to the same referent for everyone. The whole artifact is a three-minute intervention on shared vocabulary, aimed at the same *AI Builder Essentials* audience Google is trying to move up the maturity curve. Tagged with one cell only — nothing here touches sensing, seizing, or renewal, and stretching it further would be over-fitting a definitional explainer to a strategy vocabulary.

## Sibling in the same series

[[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails|"4 ways loop engineering fails"]] (25 Aug 2026) is the follow-on from the same *AI Builder Essentials* series, with [[Tilde Thurium]] again presenting — this time with Annie Wang. Read as a pair: this video draws the harness boundary, that one populates it with the four ways the loop inside it breaks (runaway loops, unverified autonomy, uncheckable goals, complexity overflow) and the controls that stop each.

## Linked entities and concepts

- [[Google]] — publisher (Google Cloud Tech channel). Updated in this ingest.
- [[Simon Willison]] — the agent definition Baugues adopts and attributes on camera. Updated in this ingest.
- [[Antigravity]] — named alongside Claude Code and Codex as an example harness carrying multiple interfaces. Updated in this ingest.
- [[Claude Code]] — named as an example harness.
- [[concepts/agent-harness|agent-harness]] — the source's entire subject; *"the harness is everything after the LLM"* is now the corpus's most compact definition of the boundary, and the harness/interface decoupling is recorded there.
- [[concepts/ai-agents|ai-agents]] — the Willison definition (LLM + tools + loop + goal) as restated here.
- [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee / *Anatomy of an Agent Harness*]] — the layered decomposition this compresses; see this source's `relationships:`.
- [[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering — *Harness Is All You Need*]] — the empirical anchor for the same harness-over-model framing.
- [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy / LangChain]] — the vocabulary's origin point, four months earlier.
- [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Cheung, Ippolito & Secchi / Google]] — the same vendor productising the layer without naming it.

**Dangling** (single-source mention, deferred per [author-entity promotion](../../CLAUDE.md#author-entity-promotion)): Greg Baugues, Tilde Thurium, Google Cloud Tech (channel), *AI Builder Essentials* (series), Codex.

## Source quality note

Human-curated captions, so transcription is clean and no cleanup was required beyond none at all. **This is vendor content** — published on Google Cloud's channel, with a Google product (Antigravity) named among the examples and a call-to-action link to a Google product experience in the description. The definitional material is nonetheless vendor-neutral: Baugues names a competitor's product (Claude Code) first among his harness examples, and the definition he adopts is a third party's (Willison's), attributed on camera.

The correct use of this page is as a **dated definitional citation** — evidence of what "agentic harness" meant, and to whom, in mid-July 2026 — and as the cleanest available statement of the harness/interface distinction. It supports no empirical claim whatsoever.
