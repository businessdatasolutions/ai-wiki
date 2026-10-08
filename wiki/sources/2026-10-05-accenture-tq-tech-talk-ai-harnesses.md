---
type: source
kind: video
title: "AI harnesses | The secret behind every AI agent"
author: ["Accenture"]
publisher: "Accenture (YouTube), TQ Tech Talk series"
url: "https://www.youtube.com/watch?v=Yhr-ZlCrNHw"
date_published: 2026-10-05
date_ingested: 2026-10-08
length: "~12:47 minutes (transcript ~128 segments + 7 stills; creator-uploaded en-US captions)"
raw: "../../raw/videos/ai-harnesses-the-secret-behind-every-ai-agent.md"
stills: "../../raw/videos/ai-harnesses-the-secret-behind-every-ai-agent.stills.md"
tags: [accenture, udacity, tq-tech-talk, explainer, agent-harness, harness-engineering, model-vs-harness, engine-analogy, failure-attribution, enterprise-chatbot, anthropic-game-maker-experiment, planner-generator-evaluator, subtraction-principle, swappable-models, science-technology]
dynamic_capabilities:
  - digital-sensing/digital-mindset-crafting
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: 2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness
    via: "Shared topic: a short definition of the harness for newcomers. Google Cloud: 'everything after the LLM'. Accenture: 'the machinery built around an AI model: what it can see, use and remember, and how its work gets checked'."
  - type: supports
    target: 2026-09-14-google-cloud-agent-factory-agent-harnesses-explained
    via: "Shared topic: when an agent disappoints, whether the model or the stack around it is at fault. Google Cloud interviews the term's coiner; Accenture gives a non-engineer's checklist for telling the two apart."
  - type: supports
    target: 2026-09-07-yc-paper-club-why-the-harness-matters-more-than-the-model
    via: "Shared topic: the same model weights giving different results under different harnesses. YC cites ARC-AGI (about 30% vs 95%+); Accenture retells Anthropic's game-maker runs (unplayable vs playable, $9 vs $200)."
  - type: supports
    target: 2026-05-04-rethinking-agents-harness-is-all-you-need
    via: "Shared topic: same-model variance and Anthropic's line that every harness component encodes an assumption about what the model can't do. The Prompt Engineering video reports ablation numbers from two papers; Accenture shows which two components Anthropic removed for a newer model."
  - type: supports
    target: 2026-05-15-osmani-agent-harness-engineering
    via: "Shared topic: what happens to a harness as models improve. Osmani: 'harnesses don't shrink; they move'. Accenture: 'this problem space doesn't go away as the models get better. It just moves.' Both draw on Anthropic's March 2026 harness-design post."
  - type: supports
    target: 2026-05-07-chatterjee-anatomy-of-agent-harness
    via: "Shared topic: who owns which half of an AI system, and which half to blame. Chatterjee: the model is rented, the harness owned, and most production failures are harness failures. Accenture: the model is 'supplied by the AI vendor', the harness 'owned by your organisation'."
  - type: supports
    target: 2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness
    via: "Shared topic: the agent as model plus harness. Trivedy states it as an engineering boundary; Accenture states it as an equation for a general audience ('model + harness = agent')."
  - type: contradicts
    target: 2026-06-11-kilpatrick-sequoia-model-eats-the-harness
    via: "Whether better models retire the harness. Kilpatrick expects the model to absorb today's harness within about 12 months. Accenture: removed components are replaced by new ones, 'simpler, not gone', and the problem space 'just moves'."
---

# Accenture — AI harnesses: the secret behind every AI agent (Oct 2026)

> Ever wonder why two AI applications can use the same AI model but deliver completely different results?
>
> The answer might not be the AI model at all.
>
> In our latest TQ Tech Talk, you'll discover the AI harness -- the technology that connects AI models to tools, data, memory, permissions, and actions. It's also the key ingredient behind AI agents and agentic systems.
>
> Watch now to learn why the most interesting part of an AI system may not be the model. It may be the harness built around it.
>
> — channel description, Accenture (chapter list, recruitment text and links omitted)

## TL;DR

A **12:47 explainer** in Accenture's *TQ Tech Talk* series, published 5 October 2026. The description also promotes Udacity, *"now part of Accenture"*, and its Agentic AI Nanodegree. The presenter is not named in the metadata; the Claude account in their screen recording at 5:10 reads *"SA · Simon"*. The audience is **non-engineers**: people who use or buy an internal AI assistant and want to know why it disappoints. It is the corpus's plainest-language statement of the [[agent-harness]] construct, and it is heavily illustrated: 35 visuals in under 13 minutes, drawn as engineering sheets with parts lists and revision blocks.

The argument, in order:

1. **The opening case: same model, useful app and useless app.** A company launches an internal assistant (*"AcmeGPT"*, fictional), and a few weeks later most people have *"quietly stopped using it"*, while the app on their phone *"seems to run rings around it"*. The easy conclusion, that the company bought the cheap AI, is often wrong: *"It's using the same model from the same company, even the same version… the difference isn't the AI part of it. It's everything built around the AI."*
2. **The engine analogy.** A model is an engine on a stand: *"an extraordinary piece of engineering. It is also kind of useless."* On its own it takes text in and puts text out; *"it can't open a document… can't send an email. It can't even remember what happened 5 minutes ago."* Put wheels around it and you have a car; a rotor, a helicopter; a hose, a pump. *"Same engine, completely different machines."* The on-screen definition card (1:02): ***"harness — the machinery built around an AI model: what it can see, use and remember, and how its work gets checked."***
3. **What the harness contains.** Tools, permissions (*"what is it allowed to do without stopping to ask you"*), initial prompts, memory, handling of conversations that get too long, checks after changes, and logs *"so that somebody afterwards can see what it actually did."* The parts list is in the [Visual canon](#7--the-harness-as-a-set-of-decisions). An agent *"is exactly this. It is a model plus a harness. The model does the thinking, but the harness is what lets it actually do anything."*
4. **Swappable engines are the goal, not the reality.** Built well, the machinery lets you swap the engine (*"bolted, not welded"*, says the sheet). *"I'll be accurate about this. That is the goal rather than the current reality… AI models can be increasingly tuned to work well with one particular harness."* It is still *"the difference between an organization that could take advantage of a better AI the month it arrives and one that would have to rebuild everything first."*
5. **Consumer apps are harnesses too.** ChatGPT, Claude and Gemini are *"somebody else's harness wrapped around the same kind of model"*, and *"a great deal of the reason why these feel so much more capable than they used to is because of the harness rather than just the AI model underneath it."*
6. **The evidence: Anthropic's game-maker runs.** Retold from Anthropic Engineering's *Harness design for long-running application development* (24 March 2026, not ingested). One prompt (*"Create a 2D retro game maker with features including a level editor, sprite editor, entity behaviors, and a playable test mode"*), the same model, twice. Alone, the model produced an editor with a play button where *"nothing happened… Parts of it had never been fully connected and nothing on screen would tell you that."* In a harness with a planner, a generator and an evaluator that would *"click every button the way a person would, and file a bug against anything that didn't behave correctly"*, the game was playable. The cost: *"about 20 times as much and it took 6 hours to do instead of 20 minutes… It's not a free upgrade."*
7. **Which half to blame.** The model is responsible for *"understanding what you ask, doing the reasoning, the judgment call, and the quality of what comes back. But the harness is responsible for very nearly everything else."* Then a list of complaints, each assigned: outdated prices → missing information, *"that's the harness"*; made something up → *"usually the harness"*, because nothing told it *"don't answer if you're unsure"*; did something it shouldn't → permissions; said the job was done when it wasn't → nobody evaluated the result. Only *"we gave the AI all the results and context it needed and the results were still awful"* gets *"Okay, that one might be the model."* Hence: *"we're waiting for a better AI model to come along. That is often misplaced… if the real problem is the AI can't see your documents, then the best model in the world won't fix that problem."*
8. **A harness is never finished.** Here the engine analogy breaks: nobody re-engineers a car's chassis for a better engine, but *"a lot of what you put in a harness is only there because of something the model couldn't do at the time."* Quoting Anthropic: *"every component in a harness encodes an assumption about what the model can't do on its own"*, and *"those assumptions quickly go stale."* Anthropic removed a mechanism added because the model *"would often lose the thread on longer tasks"*, then the part that broke work into chunks. *"This is not a story about harnesses slowly going away… this problem space doesn't go away as the models get better. It just moves."* The second definition card (10:46): ***"harness engineering — the ongoing discipline of designing what surrounds an AI model, and redesigning it as models change."***
9. **The takeaway is about control, not importance.** Both halves matter: *"An extraordinary engine that's dropped into a badly built machine is going to disappoint you. But conversely, the best engineered machine in the world can't do much with a weak engine."* The difference is that *"you don't get to edit the model"*. You choose a vendor and a version, *"but what you can't do is reach inside it and change how it reasons."* The harness is the opposite: *"Every part of that is a decision… made by people in your organization. Possibly this week, possibly by you. So the harness isn't only the important part. It's the part you have any say over at all."* The closing card: ***"Is this the model's job — or the harness's job?"***

## Visual canon

Gemini found 35 visuals (77,314 tokens). Seven are published here. Navigation cards, the engine-analogy build-up, consumer-app screenshots without annotation and the closing question card are left out because the narration says the same thing. The two definition cards are quoted in the TL;DR, not published.

Corrections against the pixels: Gemini read the model selector at 5:10 as *"Opus 3.5 High"*; it says **Opus 5.5 High**. It listed Run 01's agents as *"1 (planner)"*; the receipt says **1**. For the governance diagram it reported a question on every part and an *"APPROVED: you?"* stamp; only parts 02, 04, 05 and 06 get handwritten questions, and no stamp appears in the frames checked. Two frames are re-cut from a local download: the scan's frame for the revised harness (10:13) caught the diagram mid-animation, and its frame for the governance diagram (12:03) was a zoomed crop of the title block.

### 1 · Which parts of a chat app are harness

![[assets/2026-10-05-accenture-tq-tech-talk-ai-harnesses/19-05m10-claude-interface-harness-vs-model-breakdown.webp|The Claude desktop app annotated: sidebar features, an artifact card and the attach button labelled harness; the model selector labelled model]]

*Still at [5:10](https://www.youtube.com/watch?v=Yhr-ZlCrNHw&t=310s) from Accenture, "AI harnesses | The secret behind every AI agent".*

The presenter's own Claude desktop app, chat *"Technical Training Course Production Workflow"*, with callouts:

- **HARNESS:** the sidebar group *Projects, Artifacts, Scheduled, Dispatch (Beta), Design, Customize*; the artifact card *"Video Frame Extraction Script — Code"*; the **+** (attach) button in the message box.
- **MODEL:** the selector *Opus 5.5 High*.

*Still vs. transcript:* the narration says the app is *"somebody else's harness"*. The still draws the line inside one real product: everything you click is harness, and the model is one dropdown. It also places interface features (Projects, Scheduled, Dispatch) inside the harness, a boundary question taken up under [Debates](#debates-and-supersession).

### 2 · The game-maker harness, as Anthropic built it

![[assets/2026-10-05-accenture-tq-tech-talk-ai-harnesses/22-06m30-fig-07-the-full-harness.webp|The full harness: planner, generator and evaluator, each the same model, with sprints, context resets and bug reports fed back to the build]]

*Still at [6:30](https://www.youtube.com/watch?v=Yhr-ZlCrNHw&t=390s) from Accenture, "AI harnesses | The secret behind every AI agent".*

**FIG. 07 — The full harness.** PLANNER (*writes the spec*) → SPRINTS → GENERATOR (*builds to the spec*, with a CONTEXT RESETS loop) → EVALUATOR (*tests it like a person*, pointing at an app window with NEW / EDIT / SAVE and a play button). BUG → BUG: *"Bug reports → back to the build"*, from evaluator to generator.

| Part | Note |
|---|---|
| 00 Model | *the same one, ×3* |
| 01 Planner | |
| 02 Generator | |
| 03 Evaluator | |
| 04 Sprints | *work split into chunks* |
| 05 Context resets | *a clean slate between sessions* |

Title block: *Game maker harness · Sheet 07 · After Anthropic, Mar 2026 · Rev C.*

*Still vs. transcript:* the narration names three tasks (spec, build, evaluate). The sheet adds the two parts that are later removed, sprints and context resets, and shows that all three roles are the same model.

### 3 · The two runs as receipts

![[assets/2026-10-05-accenture-tq-tech-talk-ai-harnesses/24-06m55-game-maker-experiment-run-comparison.webp|Two receipts: run one solo, twenty minutes, nine dollars, unplayable; run two full harness, six hours, two hundred dollars, playable]]

*Still at [6:55](https://www.youtube.com/watch?v=Yhr-ZlCrNHw&t=415s) from Accenture, "AI harnesses | The secret behind every AI agent".*

| Game maker | Run 01 · Solo | Run 02 · Full harness |
|---|---|---|
| Prompt | same | same |
| Model | same | same |
| Harness | none | full |
| Agents | 1 | 3 (planner, generator, evaluator) |
| Checked by | — | evaluator |
| Fix-and-retest | — | yes |
| Time | 20 min | 6 hr |
| Total | $9.00 | $200.00 |
| Result | UNPLAYABLE | PLAYABLE |

Handwritten: *"≈ 20× the cost"*. Source line (from the preceding still): *Anthropic Engineering, "Harness design for long-running application development," Mar 2026.*

*Still vs. transcript:* the narration gives the ratio (*"about 20 times"*) and the times. The dollar amounts, $9 and $200, are only on screen.

### 4 · The harness's job description

![[assets/2026-10-05-accenture-tq-tech-talk-ai-harnesses/26-07m38-role-the-model-vs-the-harness.webp|Job description card: role the harness, owned by your organisation, responsible for very nearly everything else]]

*Still at [7:38](https://www.youtube.com/watch?v=Yhr-ZlCrNHw&t=458s) from Accenture, "AI harnesses | The secret behind every AI agent".*

Two job-description cards. The model's card is read from its fully built frame at [7:22](https://www.youtube.com/watch?v=Yhr-ZlCrNHw&t=442s), since it slides off-screen as the harness card builds.

| | Role: the model | Role: the harness |
|---|---|---|
| | **Supplied by** the AI vendor | **Owned by** your organisation |
| **Responsible for** | the thinking | very nearly everything else |
| | ✓ Understanding what you asked | ✓ What information it's handed |
| | ✓ Reasoning | ✓ What it's allowed to touch |
| | ✓ The judgement call | ✓ What it remembers |
| | ✓ The quality of the answer | ✓ Whether the work gets checked |
| | | ✓ A record of what it did |

*Still vs. transcript:* the checklists are spoken almost word for word. *Supplied by the AI vendor* and *owned by your organisation* are not: the ownership split is only on the cards, and it is the talk's closing argument in two lines.

### 5 · Five complaints, four stamped "harness"

![[assets/2026-10-05-accenture-tq-tech-talk-ai-harnesses/27-08m32-acmegpt-feedback-analysis.webp|A feedback channel with five complaints; four stamped harness with context, guardrails, permissions and verification, the fifth unstamped]]

*Still at [8:32](https://www.youtube.com/watch?v=Yhr-ZlCrNHw&t=512s) from Accenture, "AI harnesses | The secret behind every AI agent".*

A mock team-chat channel, *#acmegpt-feedback* (*"Tell us how AcmeGPT is working for you · 214 members"*, Week 3):

| Complaint | Stamp |
|---|---|
| *"Asked it for the Enterprise tier price. It quoted last year's."* | HARNESS · context |
| *"It cited a returns policy we don't have. Very confidently."* | HARNESS · guardrails |
| *"Why is it able to email customers directly?? It just sent one."* | HARNESS · permissions |
| *"It said the Q3 summary was done. Half the sections were empty."* | HARNESS · verification |
| *"Gave it the full brief and every source doc. The analysis was still shallow."* | — (no stamp) |

*Still vs. transcript:* the narration walks through the same cases. The stamps name the harness layer for each (context, guardrails, permissions, verification), and the fifth complaint is the only one left unstamped: the case the narration says *"might be the model"*.

### 6 · The same harness, revised for a newer model

![[assets/2026-10-05-accenture-tq-tech-talk-ai-harnesses/29b-10m20-fig-07-the-full-harness-revised.webp|The full harness redrawn for a newer model, with sprints and context resets struck through and the note simpler, not gone]]

*Still at [10:20](https://www.youtube.com/watch?v=Yhr-ZlCrNHw&t=620s) from Accenture, "AI harnesses | The secret behind every AI agent". Re-cut from a local download.*

FIG. 07 redrawn. The sprints box and the context-resets loop are gone from the diagram. Parts list: *00 Model — a newer one, ×3*; 01 Planner, 02 Generator, 03 Evaluator unchanged; ~~04 Sprints — work split into chunks~~ and ~~05 Context resets — a clean slate between sessions~~ struck through. Handwritten: ***"simpler, not gone"***. A few seconds later the title block's *Rev C* is stamped **Rev D**.

*Still vs. transcript:* the narration describes the removed parts by function (*"lose the thread on longer tasks"*, *"broke work into different chunks"*). The sheet names them as context resets and sprints, and shows planner, generator and evaluator all surviving.

### 7 · The harness as a set of decisions

![[assets/2026-10-05-accenture-tq-tech-talk-ai-harnesses/34b-11m59-fig-05-the-harness-exploded-with-questions.webp|The harness exploded into seven parts around the engine, with handwritten questions on permissions, memory, context and checks]]

*Still at [11:59](https://www.youtube.com/watch?v=Yhr-ZlCrNHw&t=719s) from Accenture, "AI harnesses | The secret behind every AI agent". Re-cut from a local download.*

**FIG. 05 — The harness, exploded.** The engine (00) with seven parts drawn around it. First shown at 2:52–3:19 with printed captions; at 11:47 the talk returns to it and replaces four captions with handwritten questions, circling those parts.

| Part | Caption at 3:18 | Question at 11:59 |
|---|---|---|
| 00 Model | *supplied as-is* | |
| 01 Tools | *what it can reach* | |
| 02 Permissions | *what it may do unasked* | *does it need to ask first?* |
| 03 Instructions | *how to approach the task* | |
| 04 Memory | *what carries over* | *what should it keep?* |
| 05 Context | *what fits in view* | *what can it see?* |
| 06 Checks | *verifying its changes* | *who checks the output?* |
| 07 Logs | *a record of what it did* | |

*01–07 = the harness.* The instructions part is drawn as an operating-instructions plate: *"1. You support Acme customers. 2. Cite the policy you used. 3. Escalate refunds over $500. 4. Never promise delivery dates."* Title block: *Harness assembly · Sheet 03 · Scale 1:8 · Rev A*, with empty Drawn / Checked / Approved boxes.

*Still vs. transcript:* the spoken list of decisions (*"What information can this thing see? What is it allowed to do without asking? What does it remember…? And who checks the output…?"*) maps onto four of the seven parts. The sheet shows which four, keeps the other three, and gives the only example of instructions in the talk.

## Dynamic-capabilities reading

- **`digital-sensing/digital-mindset-crafting`.** The talk is *promoting a digital mindset* in a general workforce: it gives people who are not engineers a way to read AI failures (*"is this part of the system the model's job or the harness's job?"*) and argues against the habit of waiting for a better model.
- **`digital-transforming/improving-digital-maturity`.** It locates the controllable part of an AI system inside the firm: the harness is *"owned by your organisation"*, and its parts are decisions *"made by people in your organization. Possibly this week, possibly by you."* That is *leveraging digital knowledge inside the firm*, framed as an ownership claim. It also notes *harness engineering* turning up *"in job ads and articles"*, a workforce-maturity signal, though an anecdotal one.

## Related in this wiki

- [[2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness|Baugues & Thurium / Google Cloud (Jul 2026)]]: a three-minute definition, *"the harness is everything after the LLM"*, which decouples the harness from the interface.
- [[2026-09-14-google-cloud-agent-factory-agent-harnesses-explained|Google Cloud Agent Factory (Sep 2026)]]: the term's coiner, [[Ryan Lopopolo]], on where the word came from and what a harness is.
- [[2026-09-07-yc-paper-club-why-the-harness-matters-more-than-the-model|YC Paper Club (Sep 2026)]]: researchers on the same-weights, different-harness gap (ARC-AGI about 30% vs 95%+) and self-improving harnesses.
- [[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering (May 2026)]]: ablation and transfer results from two papers, and the same Anthropic *"encodes an assumption"* line.
- [[2026-05-15-osmani-agent-harness-engineering|Osmani (May 2026)]]: the practitioner synthesis of harness engineering, including *"harnesses don't shrink; they move"*.
- [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee (May 2026)]]: the model rented, the harness owned, and a worked example of a harness failure read as a model failure.
- [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy / LangChain (Mar 2026)]]: the source of the agent = model + harness boundary.
- [[2026-06-11-kilpatrick-sequoia-model-eats-the-harness|Kilpatrick / Sequoia (Jun 2026)]]: the expectation that models absorb today's harness within about a year.
- [[2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company|BBC AI Decoded (Aug 2026)]]: the same opening question, why enterprise AI isn't paying off, answered with training, imagination and workflow gaps rather than system design.
- [[2026-06-16-mollick-simon-sinek-ai-skills-experience-edge|Mollick (Jun 2026)]]: a general-audience layering of model, app and harness.

## Linked entities and concepts

- **Concepts:** [[agent-harness]], [[ai-agents]], [[enterprise-ai-adoption]].
- **Entities:** [[Anthropic]] (the retold experiment and quotation).
- **Dangling** (single-source mention, deferred): Accenture (channel), Udacity; the presenter (unnamed; on-screen account *"SA · Simon"*). *AcmeGPT*, Acme Corp and the feedback-channel names are fictional.

## Debates and supersession

- **The evidence is second-hand.** The talk's one measured result is Anthropic's game-maker comparison, retold. The primary post, *Harness design for long-running application development* (Anthropic Engineering, 24 March 2026), is not in the wiki; [[agent-harness]] already quotes its *"encodes an assumption"* line through Osmani and the Prompt Engineering video. The $9 / $200 and 20 min / 6 hr figures should be checked against the post before they are cited on their own.
- **The comparison bundles harness with budget.** Run 02 had three roles, an evaluator loop, 18 times the wall-clock time and about 22 times the money. The talk says so (*"a real engineering decision with a real bill attached"*), but the two runs cannot show which part of the harness made the difference, or whether a solo model given the same budget would have closed part of the gap.
- **The usage chart is a dramatization.** The opening's *"weekly active users"* chart (about 1,200 at launch, 38 by week 10) belongs to the fictional AcmeGPT. It illustrates the story; it is not data about enterprise assistants.
- **Where the harness ends.** The annotated Claude screen counts interface features (Projects, Scheduled, Dispatch, the attach button) as harness. [[2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness|Baugues & Thurium]] separate the harness from the interface, and [[2026-06-16-mollick-simon-sinek-ai-skills-experience-edge|Mollick]] treats apps as the access layer distinct from harnesses. The boundary is drawn differently by audience; the talk's broad version suits its purpose, telling a user what is not the model.
- **Do better models retire the harness?** The talk's answer is *"simpler, not gone"*: components are removed as models improve, and the problem moves. [[2026-06-11-kilpatrick-sequoia-model-eats-the-harness|Kilpatrick]] expects today's harness to be absorbed by the model. The reconciliation the wiki holds is on [[agent-harness]] (*Debates*).
- **Swappability is stated as a goal.** The talk is explicit that models are *"increasingly tuned to work well with one particular harness"*, so swapping one can *"produce unexpected results"*. That is narrower than the transfer result recorded on [[agent-harness]] from the Prompt Engineering source.
- No supersession.

## What was actually ingested

The full caption track: 128 segments, 0:00–12:33 of 12:47, under the channel's 12 chapters. The panel text is punctuated and quotes reported speech, consistent with the creator-uploaded en-US track (an English ASR track also exists). One cleanup at acquire (*"chat GPT"* → *ChatGPT*). A full Gemini stills scan found 35 visuals for 77,314 tokens. Stream seeking returned HTTP 403, so the scan cut all frames from a full download. Every published still was viewed and its reading corrected against the pixels; seven are published, two of them re-cut at 10:20 and 11:59 from a second local download (saved as `29b-…` and `34b-…` beside the scan's stills, gitignored). The page slug avoids the word in the video's title that the repo's file-protection hook blocks in filenames; the raw slug keeps it.
