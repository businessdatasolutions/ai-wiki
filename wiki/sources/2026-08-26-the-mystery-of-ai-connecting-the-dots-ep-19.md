---
type: source
kind: video
title: "The Mystery of AI: From Next-Token Prediction to Connecting the Dots | Ep. 19"
author: ["MIT Sloan CIO Symposium Videos"]
publisher: "MIT Sloan CIO Symposium Videos (YouTube); the symposium's podcast, Collective Sensemaking series, part 1 of 4"
url: "https://www.youtube.com/watch?v=5KIHgVg7_3Y"
date_published: 2026-08-26
date_ingested: 2026-10-12
length: "~1:05:21 minutes (transcript ~1,287 lines; en-orig auto-captions, not ASR-cleaned)"
raw: "../../raw/videos/the-mystery-of-ai-connecting-the-dots-ep-19.md"
tags: [mit-sloan-cio-symposium, allan-tate, irving-wladawsky-berger, collective-sensemaking, connecting-the-dots, next-token-prediction, emergence, post-training, ai-as-editor, thread-memory, memory-records, cognitive-partner]
relationships:
  - type: published-by
    target: MIT-Sloan-CIO-Symposium
    via: "the symposium's own podcast; episode 19, part 1 of the four-part Collective Sensemaking series"
  - type: authored-by
    target: Allan-Tate
    via: "co-host; runs the conversation and supplies the symposium-planning use cases"
  - type: authored-by
    target: Irving-Wladawsky-Berger
    via: "co-host; supplies the LLM explainer and the blog-editing story"
---

# The Mystery of AI: From Next-Token Prediction to Connecting the Dots | Ep. 19

> Episode 19: The Mystery of AI: From Next-Token Prediction to Connecting the Dots (Part 1 of 4)
>
> Why can large language models, often described as systems that simply predict the next token, function as remarkably useful thinking partners?
>
> In the first installment of this three-part conversation, Allan Tate and Irving Wladawsky-Berger explore the evolution of modern large language models, from the role of scale and attention mechanisms to the additional training that transformed raw models into conversational AI assistants.
>
> The conversation then moves from theory to practice, with real-world examples of AI being used as an editorial partner, travel planner, study companion, and strategic advisor for the MIT Sloan CIO Symposium. These experiences point to a larger idea: AI's value may come not simply from choosing better words, but from recognizing relationships across ideas and "connecting the dots."
>
> This episode sets the stage for the next installment and a bigger question: If AI can identify patterns across a document, could it also recognize recurring themes across many conversations and help organizations learn collectively?
>
> — channel description, MIT Sloan CIO Symposium Videos (excerpt; event and community notices omitted)

## TL;DR

A ~65-minute episode of the [[MIT Sloan CIO Symposium]]'s podcast, published 26 August 2026 and recorded on 5 August. The hosts are [[Allan Tate]], the symposium's executive chair, and [[Irving Wladawsky-Berger]]. It opens a four-part series the hosts later name **Collective Sensemaking** (episodes 19–22). This first part is a plain-language account of how large language models work, followed by the hosts' own uses of them. Its end point is the question the rest of the series answers: if a model can connect ideas across one article, can it connect them across many conversations?

**The "three-part" label is wrong.** The description calls this *"the first installment of this three-part conversation"* while its own title line says *"Part 1 of 4"*. Tate says on air that the story *"may take multiple episodes. Um we think it'll take about three, but we're flexible"* [3:03]. In episode 21 he confirms it grew to four. The description reflects the original plan.

**1. The mystery: why does next-token prediction work so well? (3:03–23:00).** Tate poses it: models are *"described as nothing more than next token predictors… so if that's true, why are they so intelligent?"* Wladawsky-Berger's answer is scale. Models grew *"by many orders of magnitude"* between the early 2010s and ChatGPT in 2022, and the attention paper let a model focus *"on this specific area where you need to analyze it"* [8:03]. Fluent conversation is *"almost an emergent behavior from scale"* [14:00]. His analogies are quantum mechanics, special relativity and aerodynamics. All work, all sit outside everyday experience, and people got used to them. Tate adds a psychological reason people underrate the models: machines doing reasoning feels threatening, so there is *"a tendency perhaps uh to want to undervalue synthetic intelligence"* [20:01]. This is a lay account by two non-specialists in model internals, and some details are loose: the attention description, and quantum mechanics dated to the *"late 18th century"* (the 1890s–1920s are meant).

**2. Post-training as "finishing school" (23:00–29:00).** Tate brings in the second training step. Wladawsky-Berger: *"the model in the wild was too wild for humans"*, so OpenAI *"went through a second phase of training for socializing the model"*, with *"hundreds maybe thousands of people"* telling it what humans do not do [25:03–26:02]. His image is domesticated wolves: *"We domesticated the AIs, but that took work."*

**3. Four use cases (29:00–46:00).**
- **Editor.** Wladawsky-Berger lost his *Wall Street Journal* editors when his blog moved off the paper. He asked ChatGPT to edit without rewriting: *"keep it in my style. Keep it in my voice."* The edits were *"far better than what I could have done on my own"*, and he kept telling Tate *"this is magical"* [31:01–34:00].
- **Travel planner.** Tate's European trip: cheaper flights, no connections, and a day-by-day comparison of departure dates ending in a table. A travel agent could do that, *"but very few travel agents would"* [39:01].
- **Study companion.** Reading a book with a model that links one period of history to another and sends the reader to further sources.
- **Symposium planning assistant.** This one matters for the rest of the series. A planning thread runs until it is *"exhausted"*, so Tate built a way to save each thread's state and memories and boot the next one from them: *"right now my symposium thread is number five… booted up from the last uh state and memory record of thread number four"* [43:03]. The new thread gets the gist, not everything: *"you can't initialize an LLM thread with every single bit of memory."* He calls the result a *"cognitive partner"* and describes it as an echo through the trained network.

**4. Connecting the dots (51:00–1:02:00).** The phrase comes from the hosts' own conversations. Tate's thread was asked how it edits so well. As Wladawsky-Berger reads out the reply: *"humans connect dots through lived experiences… I don't have any lived experiences. I have been trained with lots and lots and lots of sentences"* and *"I connect that by recognizing patterns"* [55:02–56:03]. For him, the new point is that judging a whole argument is also statistical: *"that kind of analysis of a whole article is something we associate with this very specific human quality that is not quantitative in nature and it turns out it is"* [1:02:02]. Tate's version is that the edits respond *"to the entire argument that you're making"*, not to one sentence. Tate also mentions research (not named) finding that the word "dog" in different languages activates the same internal connections.

**5. The bridge question (1:02:02–1:04:00).** *"If AI can connect the dots across one article, could it connect the dots across many many conversations?"* Could it find themes *"that no individual participant would naturally see"*, in the symposium community or in any organization? [[2026-09-02-from-conversation-to-institutional-understanding-ep-20|Episode 20]] takes this up.

## What this episode does and does not show

The evidence is first-person experience: two hosts reporting what worked for them. The account of how the model edits is the model's own description of itself, read out on air. That is not evidence of how it works inside. The hosts treat it as an explanation, and the page records it as their account. The thread-memory scheme in section 3 is the start of the architecture described in [[2026-09-02-from-conversation-to-institutional-understanding-ep-20|episode 20]] and [[2026-10-07-from-conversations-to-an-executive-learning-architecture-ep-22|episode 22]].

**Dynamic-capabilities tagging.** None. The episode is a lay explainer of model internals plus individual use cases. The [[warner-wager-process-model]] lens applies from episode 20 onward, where the subject becomes organizational learning.

## Related in this wiki

- The series continues in [[2026-09-02-from-conversation-to-institutional-understanding-ep-20|episode 20]] (cross-conversation synthesis), [[2026-09-15-from-debate-to-inquiry-designing-conversations-worth-preserving-ep-21|episode 21]] (the Inquiry Framework) and [[2026-10-07-from-conversations-to-an-executive-learning-architecture-ep-22|episode 22]] (the Executive Learning Architecture). Each later episode carries a `supports` edge back to the one before it.
- [[2026-07-10-when-ai-becomes-common-organizational-capability-becomes-the-advantage-ep-16|Episode 16]] is an earlier episode of the same podcast with the same hosts.
- On scale and post-training, [[foundation-models]] holds the technical accounts. This episode is the non-specialist version.

## Linked entities and concepts

- Entities: [[MIT Sloan CIO Symposium]], [[Allan Tate]], [[Irving Wladawsky-Berger]].
- Concepts: [[foundation-models]].
- **Dangling** (single-source mention, deferred): none new. Sponsors read in the housekeeping segment (a connectivity provider and a ransomware-protection vendor, names garbled by ASR) are not recorded.

## Caveats and source quality

- **Transcript.** YouTube auto-captions from the `en-orig` track, fetched with yt-dlp after the transcript panel failed to render. The video carries several AI-dubbed audio tracks; `en-orig` is the original English audio. Not ASR-cleaned at Acquire. Names are garbled ("Alan Tate", "Irving Vladki Berger", "Chad GPT"). Quotes on this page fix names only.
- **No visuals.** A split-screen video call with no slides; no stills scan was run.
- **Interested party.** The symposium's own channel, describing the symposium's own tooling and promoting its programmes.
- **Recording date vs publication.** Recorded 5 August 2026 (stated on air), published 26 August.
- **Series-length mismatch.** See the TL;DR: the description says three parts, the title line says four, and four were made.

## What was actually ingested

The full 1:05:21 episode, from auto-captions (~1,287 caption lines), read end to end.
