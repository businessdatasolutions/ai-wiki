---
type: source
kind: video
title: "Demystifying AI terms: loop engineering, squads, and harness | S02E02 | The GitHub Podcast"
author: ["GitHub"]
publisher: "GitHub (The GitHub Podcast, Season 2 Episode 2); hosts Cassidy Williams, Marlene Mhangami and Gwyneth Peña-Siguenza — all developer advocates at GitHub"
url: "https://www.youtube.com/watch?v=7oqYIRbB6Rc"
date_published: 2026-09-02
date_ingested: 2026-09-03
length: "~25:26 minutes (auto-generated transcript, ASR-cleaned; ~655 segments across the channel's own 10 chapters)"
raw: "../../raw/videos/demystifying-ai-terms-loop-engineering-squads-and-harness.md"
tags: [github, github-podcast, cassidy-williams, marlene-mhangami, gwyneth-pena-siguenza, agent-harness, loop-engineering, ralph-loop, squads, fleets, hill-climbing, forward-deployed-engineer, open-weight-models, open-source-ai, github-copilot, langchain, vocabulary-churn, terminology, deflationary-reading, developer-advocacy]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-sensing/digital-mindset-crafting
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails
    via: "two independent vendor podcasts eight days apart landing on the same definition of loop engineering from opposite rhetorical directions. Google Cloud's Annie Wang inflates it — *\"you replacing yourself with a system\"*; GitHub's Peña-Siguenza deflates it — *\"this is literally just an automation… you kick off something you've built before on some kind of cron schedule\"*. The mechanics they describe are identical (a scheduled trigger, a durable prompt, a validating sub-agent, a human checking the outputs), which is what makes the pair useful: the disagreement is entirely about whether the mechanics deserve a new name"
    confidence: 0.85
  - type: supports
    target: 2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex
    via: "the same loop primitive at two altitudes, and both credit [[Addy Osmani]] as the reference text. Vo supplies the trigger taxonomy (heartbeat / cron / hook / goal) and the five things a loop needs; this supplies the *why does it need engineering in the name* answer — Mhangami's decomposition (a repeatable prompt, a cron trigger, skills so the agent can reliably act, a validating sub-agent in the loop) is Vo's list arrived at independently. Both also name the same cost warning: loops burn tokens"
    confidence: 0.8
  - type: supports
    target: 2026-05-15-osmani-agent-harness-engineering
    via: "named on air as the best writing on the topic — *\"there's a guy called Addy Osmani who wrote a blog post on loop engineering. I think that's the best blog post I've read on this topic so far.\"* Third-party evidence of the diffusion path this wiki already models (Trivedy coins, Osmani popularises), observed from outside the vendor cluster that produced both"
    confidence: 0.8
  - type: supports
    target: 2026-05-07-kokane-agent-harness-vs-systems-design
    via: "the deflationary reading of the harness, arrived at independently. Kokane argues 90% of harness engineering is mature systems design on a new substrate; Mhangami says the same of LangChain's own history — *\"historically with LangChain you could build an agent and basically you were already building a harness… to me it's very similar to what we already had with just an agent. In my opinion, not that much different.\"* Kokane's is the reasoned version, this is the practitioner-reflex version, and they agree"
    confidence: 0.75
  - type: contradicts
    target: 2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness
    via: "not on the definition — the hosts land on *\"scaffolding around the LLM\"*, which is Trivedy's boundary almost verbatim, and they credit Trivedy and [[Harrison Chase]] by name as where they first saw it defined. The disagreement is about **novelty**: Trivedy's load-bearing move is that the harness is a distinct engineering surface worth its own discipline (*\"if you're not the model, you're the harness\"*), and Mhangami — a LangChain-literate engineer — denies exactly that, reading harness engineering as a renaming of what LangChain users were already building in 2023. A credited coiner being told by a friendly audience that the construct is not new"
    confidence: 0.7
---

# The GitHub Podcast S02E02 — Demystifying AI terms: loop engineering, squads, and harness

> AI terminology is evolving fast, with new terms like loop engineering, harness engineering, and squads popping up constantly. In episode 2 of season 2, Cassidy, Marlene, and GPS break down what these terms actually mean and how they apply to real agentic workflows. They also explore the differences between closed models, open weight models, and true open source AI. Stick around until the end for open source picks including Astro v7, RAE API, and Hugging Face Tao.
>
> *— Channel description, [[GitHub]] (The GitHub Podcast, S02E02)*

## TL;DR

Three [[GitHub]] developer advocates — **Cassidy Williams** (senior director of developer advocacy), **Marlene Mhangami** and **Gwyneth Peña-Siguenza** (senior developer advocates) — spend 25 minutes trying to define the vocabulary this wiki has spent 90-odd sources building on, and repeatedly conclude that most of it is a renaming of something older. The episode's value is **not** its definitions, which are thinner than a dozen sources already in the corpus. Its value is that it is the wiki's first source **about the terminology churn itself**, recorded by people who are paid to stay current and admit on air that they cannot.

> *"I fully admit we work in AI all the time and we're working on open source things, we're using these tools. And yet there's so many new terms — I feel like I'm behind, and it's really hard to keep up sometimes."* — Williams, ~0:47
>
> *"I went into this being just like, wow, we're really going to teach people. And now I'm just like: do I know anything?"* — Williams, ~17:16

That second line lands after the harness segment, and it is the most honest thing in the corpus about what the vocabulary layer costs the people downstream of it.

## The deflationary pass, term by term

The episode's method is consistent: take a 2026 term, find the pre-2026 thing it renames, and say so.

| Term as discussed | The hosts' reduction | What the wiki holds |
|---|---|---|
| **Loop engineering** | *"Literally just an automation"* — a prompt or skill on a cron schedule, with someone checking the outputs | Converges with [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails\|Google Cloud]] and [[2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex\|Vo]] on mechanics; those two treat the engineering as substantive |
| **Ralph loop** | A `while` loop over a PRD until the work is done — *"a bit of a brute-force type thing"*; died back because it burns tokens | Matches [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness\|Trivedy's]] definitional version (hook-intercepted exit, prompt reinjected into a clean context window) |
| **Squad** | *"Each agent does a specific task… everyone has a specific job"* — planner, tester, implementer, reviewer | Same shape as [[2026-03-26-osmani-code-agent-orchestra-multi-agent-coding\|Osmani's orchestra]] and [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures\|Allen's team structures]] |
| **Harness** | *"The scaffolding around the LLM"* — and, per Mhangami, *"not that much different"* from a LangChain agent circa 2023 | The wiki's [[concepts/agent-harness\|agent-harness]] page holds the same boundary and the same sceptical counterweight via [[2026-05-07-kokane-agent-harness-vs-systems-design\|Kokane]] |
| **Hill climbing** | Improving the harness against evals until the agent responds the way you want; *"came from model training but it's now translating to the harness"* | Consistent with [[2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent\|Anthropic's evals-for-taste]] usage |
| **Forward deployed engineer** | *"It's like a solution architect"* — *"you're literally a solutions engineer that uses AI"* | Sharper deflation than any FDE source in the corpus, incl. [[2026-06-03-warren-yc-how-to-build-an-ai-native-services-company\|Warren / YC]] |

The pairings matter more than the reductions. On loop engineering the episode and [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails|Thurium & Wang / Google Cloud]] — recorded eight days apart at two competing clouds — describe *identical* mechanics and disagree only about whether they warrant a new word; [[2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex|Claire Vo]] supplies the trigger taxonomy both are gesturing at, and all three routes lead back to [[2026-05-15-osmani-agent-harness-engineering|Addy Osmani's essay]], which Mhangami names on air as the best thing written on the subject. On the harness, Mhangami's *"not that much different"* is the practitioner-reflex form of the argument [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane]] makes carefully: most of harness engineering is mature systems design meeting a new substrate.

The recurring refrain is the one worth recording as a claim in its own right, because it is repeated three separate times by two different hosts:

> *"There's no standard again — no standards in AI. Maybe in tech in general."*

Offered once as a joke (*"except for MCP"*), twice as a straight observation. It is the mechanism behind the churn: with no standards body, each vendor's marketing surface becomes a competing dictionary, and the terms propagate faster than the practices they name.

## The three things worth citing this source for

### 1. A third-party attribution of the harness vocabulary to LangChain

Unprompted, and from outside the vendor cluster that produced the term, Mhangami names the origin:

> *"The first time I saw harness and harness engineering defined, I'm pretty sure was Harrison from LangChain… and I think Viv from their team was one of the first people as well to start using that term. I think they have a researcher on their team, I think his name is Viv."*

That is [[Harrison Chase]] and **Vivek Trivedy** — the author of [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|The Anatomy of an Agent Harness]], which the wiki already holds as the source-of-vocabulary. **This is independent corroboration of the wiki's attribution map**, from a competitor's developer-advocacy team recalling it from memory. It is also *incomplete* in an informative way: the wiki holds [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo / OpenAI Codex, Feb 11]] and Trivedy / LangChain, Feb 17 as near-simultaneous co-coiners, and the OpenAI half of that pair has evidently not propagated. What practitioners remember is the LangChain half.

### 2. "GitHub Copilot itself is the harness" — a first-party product claim

The episode's one piece of genuinely first-party information, worked out live on air:

> **Peña-Siguenza:** *"We have the GitHub Copilot harness for agents to run on code bases. So you can use a harness with your squad to do loop engineering."*
> **Williams:** *"GitHub Copilot itself is the harness."*
> **Peña-Siguenza:** *"GitHub Copilot is the harness for the SDK to run agents with various models."*

Recorded because it puts [[GitHub]] on the same side of the boundary as [[2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness|Google Cloud]], [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic]] and [[2026-02-11-lopopolo-codex-harness-engineering|OpenAI]]: the product is the harness, the model is swappable underneath it, and the SDK is how you reach it. The hosts' visible uncertainty while assembling that sentence — three attempts, with checking questions between them — is itself the episode's thesis in miniature.

### 3. The closed / open-weight / open-source three-tier spectrum, stated cleanly

The clearest short statement of the spectrum in the corpus, and the one place where the deflationary method is *not* applied:

- **Closed** — *"everything is just exposed via API"*; the default most people have used ([[OpenAI]], [[Anthropic]]).
- **Open weight** — *"you can download the weights, you can use the model for free… but you don't have access to the data set and the training method."*
- **Open source** — *"every part of the model that was used to train the model… is available openly."*

Mhangami's framing of why this matters is the transferable part: *"when we think of open source traditionally we think of just software, the code — but now in this new AI phase there are more aspects to making a model work than just code."* Open weights are *"slightly different because it's not as open, but still kind of has that same ethos."* This refines [[concepts/open-source-ai|open-source-ai]], which has carried "open-weight models" as an alias without ever laying the three tiers out as a spectrum.

## Loose ends the episode leaves

- **The "I design loops" attribution is unresolved.** Mhangami credits the *"I don't prompt my agents anymore, I design loops"* framing to two people: **Peter Steinberger** (creator of OpenClaw), reliably, and a second name the ASR renders as *"Baris Turnier"* at ~2:52 — which the speaker herself flags as a pronunciation guess. **The wiki does not resolve that second name**; it is left verbatim in the raw file and should not be matched to a person without an external check. Steinberger's tweet is described as having *"like 8 million views"*, which the hosts offer as the reason the discussion exists at all.
- **Nobody knows whether "loop engineer" is a job.** *"I think it's more of a field… we got to scour LinkedIn right after this episode."* Left open on air, and worth tracking: the corpus has watched *prompt engineer* rise and fall as a title already.
- **Open-source picks** (not load-bearing, recorded for completeness): **Astro v7** (new Rust compiler, backwards-compatible); **RAE API** (community-built API / MCP server / Raycast integration over the Real Academia Española dictionary, which offers none officially); **Tao** from [[Hugging Face]] — a small open-source Python agent that teaches you how to use other coding agents.

## Dynamic-capabilities reading

- **`digital-sensing/digital-scouting`** — the episode *is* an act of scouting, performed in public: three people whose job is monitoring emerging technology work through ten terms in twenty-five minutes and triage which ones name something real. It is also the wiki's clearest evidence of what scouting costs when the vocabulary churns faster than the practice.
- **`digital-sensing/digital-mindset-crafting`** — the stated purpose is shared literacy (*"we're really going to teach people"*), which is mindset-crafting work aimed at a developer audience rather than an executive one. The deflationary method is itself a mindset prescription: check whether the new word names a new thing before adopting it.
- **`contextual/internal-barriers`** — Williams' admission that she feels behind *while working in AI full-time* is a barrier datapoint that the corpus's executive-altitude sources cannot supply. If the people paid to stay current cannot, terminology churn is an adoption barrier in its own right, not merely noise.

## Linked entities and concepts

- Entities: [[GitHub]], [[LangChain]], [[Harrison Chase]], [[Addy Osmani]], [[Hugging Face]], [[Peter Steinberger]], [[OpenAI]], [[Anthropic]], [[Microsoft]]
- Concepts: [[concepts/agent-harness|agent-harness]], [[concepts/agentic-engineering|agentic-engineering]], [[concepts/agent-fleet-management|agent-fleet-management]], [[concepts/open-source-ai|open-source-ai]], [[concepts/ai-agents|ai-agents]]
- **Dangling** (single-source mention, deferred): Cassidy Williams, Marlene Mhangami, Gwyneth Peña-Siguenza, The GitHub Podcast, Vivek Trivedy (named in body but not yet an entity), Astro, RAE API, Tao

## Scope and reliability

**A vendor-produced developer-advocacy podcast with no evidence, no measurements and no citations beyond one blog-post recommendation.** Every definition in it is offered tentatively, several are visibly assembled during the recording, and the hosts repeatedly disclaim expertise. Cite it for **vocabulary reception** — how these terms land on competent practitioners one step removed from the labs coining them — and for the two first-party items (the Copilot-as-harness claim, the LangChain attribution). Do not cite it for definitions where the corpus already holds a primary source; on every term it covers, a better source exists.

Its reliability is asymmetric in a useful way. On *what the terms mean* it is third-hand and thin. On *how confusing the terms are*, it is a first-hand primary source, because the confusion is being demonstrated rather than described.

**Transcript provenance:** auto-generated (ASR) English captions, 655 segments, deduped and cleaned for proper nouns and product names (Addy Osmani, Ralph loop, OpenClaw, LangChain, Copilot, cron job, RAE API, Real Academia Española). Section headings are YouTube's own creator-set chapters, not inferred. Speaker attribution of individual lines above was reconstructed from context and self-introductions — the captions carry no speaker labels, so attributions are probable rather than certain. One name is deliberately left unresolved; see *Loose ends*.
