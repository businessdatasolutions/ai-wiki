---
type: source
kind: video
title: "First Proof: A Nuanced Assessment of AI's Ability to Solve Math Problems"
author: ["Harvard Mathematics Department"]
publisher: "Harvard Mathematics Department (YouTube channel), short documentary by filmmaker Oly Ralfe; speaker Lauren Williams, Harvard mathematics professor and First Proof participant"
url: "https://www.youtube.com/watch?v=4RDv_g2NFf0"
date_published: 2026-10-28
date_ingested: 2026-11-16
length: "~8:12 minutes (transcript ~56 lines; human-written track (en-US); last ~52 s music and credits)"
raw: "../../raw/videos/first-proof-a-nuanced-assessment-of-ais-ability-to-solve-math-problems.md"
tags: [first-proof, mathematics, research-mathematics, ai-benchmarks, proofs, lemmas, benchmark-contamination, human-grading, harness, chatgpt-pro, citations, plagiarism, exposition, arxiv, harvard, documentary]
relationships:
  - type: supports
    target: 2026-03-11-allen-mcdonald-how-well-can-ai-do-strategy-simulation-benchmark
    via: "both address contamination when building a benchmark: Allen and McDonald mask the identifying terms of a strategy simulation whose solutions are public; First Proof uses lemmas its setters had proved but not published, so the solutions are not on the internet"
    confidence: 0.7
  - type: supports
    target: 2026-04-30-ai-index-report-2026
    via: "both address AI performance on mathematics and the checking of lab-reported results: the AI Index reports Gemini Deep Think's IMO gold medal and notes that declining lab disclosure makes some performance figures estimates; Williams says companies announce results before humans have gone through the AI-generated solutions, and First Proof has mathematicians grade them"
    confidence: 0.65
  - type: supports
    target: 2026-03-30-lee-meta-harness-end-to-end-optimization
    via: "both address harnesses for LLMs on mathematics: Lee et al. search for a retrieval harness on 200 IMO-level problems and report its transfer across five held-out models; First Proof's second batch tested ChatGPT's pro model and three harnesses built by teams at UCLA, Princeton and in Switzerland, with no per-harness results given in the film"
    confidence: 0.6
---

# Williams (Harvard): First Proof, an assessment of AI on research mathematics

> Less than a year ago, a Harvard math professor joined a handful of world-leading scholars on an ambitious experiment designed to better define the capabilities of AI systems and delineate the boundaries with human expertise. Lauren Williams reflects on her work as part of First Proof, what she has learned from the experience, and the future of the project.
>
> Learn more about First Proof Project and keep up with the latest batches here: https://1stproof.org/
>
> *— Channel description, Harvard Mathematics Department*

## TL;DR

An eight-minute documentary from the Harvard Mathematics Department, filmed by Oly Ralfe. The only speaker is **Lauren Williams**, a Harvard mathematics professor (algebraic combinatorics, math and AI), on **First Proof** ([1stproof.org](https://1stproof.org/)): mathematicians set research-level problems and grade AI answers themselves. **Human-written caption track** (en-US), quoted as captioned. One probable captioning slip is flagged below.

What it adds to the wiki:

1. **A benchmark built against contamination.** Each problem was a lemma the setter *"had recently proved in our own research, but had not made public in any way. It wasn't published. It wasn't on the arXiv."* Answers are proofs, *"as opposed to numerical answers."*
2. **How two batches were run**, and why the second was run in-house.
3. **A grading result**: some mathematically correct solutions had serious citation problems, close to plagiarism, although every prompt and harness asked for attributions. The third batch scores correctness, citations and exposition separately.

**What the film does not give:** any score, solve rate or per-model result. On batch 2 she says only *"it was quite interesting to see how they did."* A participant on her own project, in a film by her own department.

## Why mathematicians built it

*"A year ago, I would say they were mostly quite bad at proving simple mathematical statements, and now, here we are today where an AI model has produced a proof of a Millennium Prize Problem"* (0:43). She names neither the problem nor the model. Mohammed Abouzaid and Rachel Ward started First Proof as a benchmark *"by and for the mathematical community"*, partly to *"take a little bit more control of the narrative"*: *"The AI companies are using math as a tool to show how good their product is, aiming towards a spectacular IPO… They're rushing so fast to put out big announcements that humans have not gone through these AI-generated solutions"* (1:56–2:12). The [[2026-04-30-ai-index-report-2026|2026 AI Index]] reports Gemini Deep Think's IMO gold medal and notes that falling lab disclosure makes some performance figures estimates.

## Two batches

**Batch 1.** Setters met in December 2025; in February 2026 they opened the problems to anyone, with solutions due a week later. Participants were to collect their LLM's response *"but not provide further feedback."* *"Some people indeed did a one-shot approach. Other groups, we are rather sure, did not and had feedback"* (3:47). [[2026-03-11-allen-mcdonald-how-well-can-ai-do-strategy-simulation-benchmark|Allen and McDonald]] handle contamination on a strategy simulation with public solutions by masking its names; First Proof uses results no one had published.

**Batch 2 (May 2026).** First Proof ran the tests itself. [[OpenAI]] *"wanted us to test the pro model of ChatGPT"*, and there were three harnesses, *"some code that tells an LLM how to interact with a prompt"*, from mathematicians at UCLA, at Princeton and in Switzerland (4:18–4:46). See [[agent-harness]]; [[2026-03-30-lee-meta-harness-end-to-end-optimization|Meta-Harness]] searches for a harness on IMO-level problems. Batches now come every three months: *"the increase in AI capabilities is very fast."*

## Grading

Thirty mathematicians graded batch 2 for two days at Harvard's Center of Mathematical Sciences and Applications. *"There were mathematically correct solutions that had either massive problems with exposition or massive problems with citations, or what you might call, if a human created it, plagiarism"* (5:34). This was *"quite alarming because all of the prompts and harnesses had told the models to provide full and accurate attributions and citations."* Batch 3 gets three scores: correctness, attributions and citations, exposition. See [[ai-benchmarks]], and [[jagged-frontier]] on mathematics as a domain where correctness can be checked.

## The profession

First Proof is now a nonprofit, the First Proof Foundation. Williams calls AI *"both a threat and an opportunity."* Journals and the arXiv receive *"exponentially many more"* papers (the captions read "solutions"; "submissions" is the likely word), and *"the only way to deal with that volume of stuff is to use an LLM. But if people now start producing math using AI models, and then evaluating math using AI models, this is a pretty messed-up situation"* (6:47–7:03). The project's aim is a mathematical ecosystem *"still for humans, by humans."*

## Linked entities and concepts

- **Entities:** [[OpenAI]].
- **Concepts:** [[ai-benchmarks]], [[agent-harness]], [[jagged-frontier]].
- **Dangling** (single-source mention, deferred): Harvard Mathematics Department (channel), Lauren Williams, Mohammed Abouzaid, Rachel Ward, Oly Ralfe, First Proof / First Proof Foundation.

## Source quality

Human-written en-US caption track, served by the transcript panel; its text is identical to the en-US track fetched separately with yt-dlp. A short institutional film: one participant, no figures, one named model tier. The Millennium Prize claim is made in passing and checked neither in the film nor in the wiki. That some batch-1 groups used feedback is her inference (*"we are rather sure"*). A documentary, so no stills are needed.
