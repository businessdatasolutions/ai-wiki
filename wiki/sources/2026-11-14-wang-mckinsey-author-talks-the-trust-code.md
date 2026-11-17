---
type: source
kind: video
title: "AI Is Advancing. Is Our Judgment Keeping Up?"
author: ["McKinsey & Company"]
publisher: "McKinsey & Company (YouTube channel), *Author Talks*; guest Tiffany Xingyu Wang, president and cofounder of Oasis Consortium and World Economic Forum Young Global Leader, on her book *The Trust Code* (Wiley, September 2026)"
url: "https://www.youtube.com/watch?v=x0yS3gtBpsI"
date_published: 2026-11-14
date_ingested: 2026-11-16
length: "~18:26 minutes (transcript ~132 lines; ASR auto-generated track, 7 chapters)"
raw: "../../raw/videos/ai-is-advancing-is-our-judgment-keeping-up.md"
tags: [mckinsey, author-talks, tiffany-xingyu-wang, the-trust-code, oasis-consortium, book-interview, trust-in-ai, calibrated-trust, overtrust, undertrust, trustworthiness, competence-truthfulness-benevolence-context, pilot-as-belief, enterprise-accountability, ai-procurement, aviation-analogy, human-judgment, hourglass-workflow, single-cell-genomics, creative-work, parenting]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
relationships:
  - type: supports
    target: 2026-05-14-pochampally-assistant-or-actor-delegation-regret
    via: "both treat trust in AI as set per task rather than per system: Pochampally et al. measure 20 students' trust and approval demands across five agent tasks and find them tracking irreversibility and external visibility; Wang argues the question is how much trust a system deserves 'under which conditions and for what tasks'"
    confidence: 0.7
  - type: supports
    target: 2025-04-28-gillespie-kpmg-trust-attitudes-and-use-of-ai-2025
    via: "both address whether trust in AI is set too high or too low: Gillespie et al. survey 48,340 people in 47 countries (54% wary of trusting AI; 66% of employees have relied on AI output without evaluating it); Wang separates a system's trustworthiness from people's trust in it and calls the match between the two calibration"
    confidence: 0.7
  - type: supports
    target: 2026-04-28-dellacqua-jagged-technological-frontier
    via: "both address reliance on AI output that reads well but is wrong: Dell'Acqua et al. measure a 19-point drop in correct answers outside the frontier, with higher-rated coherence; Wang says a 'very charming but unreliable system can be wildly overtrusted' and that AI triggers trust rather than earning it"
    confidence: 0.65
  - type: supports
    target: 2026-08-26-chatterjee-agentic-governance-gap
    via: "both address what a deploying enterprise owes for the AI it buys: Chatterjee sets out board-level risk appetite, single ownership of agent behaviour, vendor diligence and tested kill switches; Wang names enterprises as the accountability layer between labs and regulators and lists three questions for vendors: a contained failure, time to detection, recourse"
    confidence: 0.65
---

# Wang on McKinsey's *Author Talks* — AI is advancing; is our judgment keeping up?

> Can we unlock AI's promise without surrendering human judgment? As AI becomes more capable of making decisions on our behalf, technology leader Tiffany Xingyu Wang says the answer lies in learning not whether to trust AI, but when—and how much.
>
> In this edition of *Author Talks*, Wang, president and cofounder of Oasis Consortium and World Economic Forum Young Global Leader, discusses her book, *The Trust Code: How to Unlock AI's Promise Without Losing Humanity* (Wiley, September 2026).
>
> Wang examines why our instincts for trust can misfire when applied to increasingly capable AI systems. She argues that learning to calibrate trust can help individuals and organizations use AI with intention, preserve human judgment, and capture its benefits without sacrificing agency.
>
> *— Channel description, McKinsey & Company*

## TL;DR

An 18-minute edition of the *Author Talks* series on the [[McKinsey & Company]] channel. Tiffany Xingyu Wang speaks to camera in seven chaptered segments about her book *The Trust Code*; no interviewer is heard, though the title card reads *"Chats with Adam Volk"*. She says she has spent *"over a decade building trust and safety systems for big enterprises."* **Auto-generated transcript, ASR-cleaned in quotation**: "overrust"/"underrusted" → overtrust/undertrusted, "Whimos" → Waymos, "McKenzie" → McKinsey, "at scare"/"end scale" → at scale, "Steven Quick" → Stephen Quake, "19% experimental" → 90% experimental, "alpha you know" → AlphaFold, "boweapon" → bioweapon, "narrow waste of our glass" → narrow waist of the hourglass, "unscentimental" → unsentimental.

What it adds to the wiki:

1. **Three terms kept apart.** *Trustworthiness* is a property of the system; *trust* is our willingness to rely on it; *calibration* is whether the two match. Over-trust *"exposes us to harm"* and under-trust *"traps us in paralysis for innovation."*
2. **Four dimensions of AI trustworthiness**: competence, truthfulness, benevolence and contextual fit. The common error she names is mistaking competence for trustworthiness.
3. **"A pilot is a statement of belief."** What shows that an enterprise trusts AI is whether it changes workflows, trains staff and changes incentives.
4. **Enterprises as the missing accountability layer** between the labs that build models and the regulators that write rules, with an aviation analogy and three questions to put to any vendor.
5. **Judgment moves; it does not disappear.** Two examples from her interviews: biology moving from 90% experimental to 90% computational, and creative work shaped like an hourglass with judgment at the narrow waist.
6. **A personal practice**: *"binary trust is lazy trust"*; *"I trust AI precisely but not generally."*

It is a book-promotion piece on a consultancy's channel. The frameworks are the author's own and are not tested in the talk, and it reports no data.

## Calibration instead of "do we trust AI?" (0:00–6:57)

Wang's opening claim is that *"Do we trust AI?"* is *"a question that's almost too big to be useful."* AI is already trusted invisibly, in card fraud detection and grid balancing; what is new is that models draft our work and *"increasingly the agents are acting on our behalf."* Her replacement question: *"how much trust does a system deserve and under which conditions and for what tasks."*

She defines trust as accepting *"vulnerabilities today in hope of promise in the future,"* and turns it into a question a user can answer: what vulnerability am I accepting today, for what promise, in what situation? Until that is spelled out, *"trust will keep being this very vague sentiment"*; once it is, trust *"becomes a decision that you can examine and you can measure and you can improve on."*

The three-term split is the core of the talk: *"A technically very strong system can be undertrusted and a very charming but unreliable system can be wildly overtrusted and that's what's happening everywhere now… both are actually failures."* [[2026-05-14-pochampally-assistant-or-actor-delegation-regret|Pochampally et al.]] measured trust per task with students using an agent; trust and approval demands varied by task. [[2025-04-28-gillespie-kpmg-trust-attitudes-and-use-of-ai-2025|Gillespie et al.'s 47-country survey]] measures the population side of the same topic, including the share of employees who relied on AI output without evaluating it (66%). See [[agent-oversight-and-delegation]].

Her explanation for miscalibration is an *"evolutionary mismatch between a stone age brain… evaluating the space age systems"* (3:19). The systems *"sound warm, very confident, very empathetic"* without the understanding, responsibility or intention those signals carry between humans. They *"are not earning our trust by delivering the track record and proven evidence… They are simply triggering our trust"* (8:58).

## Four dimensions, and the behaviour test (6:57–9:10)

Her four dimensions are **competence, truthfulness, benevolence and contextual fit**. AI is *"so capable that it will sound so competent and so aligned with you while it has nothing to be benevolent to maximize your well-being."* [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua et al.]] measured reliance on AI output in their BCG experiment: outside the frontier, consultants using AI gave fewer correct answers while their answers were rated more coherent. See [[jagged-frontier]].

For enterprise leaders she asks *"does our behavior match what we say we trust?"* Studies of low pilot ROI, *"including McKinsey"*, prompt the line *"a pilot is a statement of belief."* The state of trust shows *"whether we change the workflow, whether we train the staff, whether we changed the incentives."* McKinsey's [[2025-11-05-mckinsey-state-of-ai-2025|State of AI 2025]] puts the share of AI-using organisations that have fully scaled at 7%. This is the source's `digital-transforming/redesigning-internal-structures` content: Wang reads redesigned workflows, training and incentives as the evidence of trust, and pilots alone as belief. See [[enterprise-ai-adoption]].

## Enterprises as the accountability layer (9:10–11:51)

*"In today's AI age, accountability means owning the conditions around the unpredictability."* The usual map, she says, has two poles: labs that build models and regulators that write rules. It leaves out the enterprises that *"decide what gets bought, what's connected to real systems… give access to real data and… actually deploy it at scale."* Her analogy is aviation: manufacturers design and test aircraft, airlines are responsible for how they are operated and who is in control, and regulators *"set a floor nobody gets to opt out of."* *"Labs build capabilities and regulators set floor but it is the enterprise who decide how much authority we give it."*

Her procurement advice replaces *"is this model safe?"* with three requests: *"show me a failure or failures and show me how you contained it,"* *"show me how quickly I will know,"* and *"show me what recourse I have if it cost me the money or reputation."* [[2026-08-26-chatterjee-agentic-governance-gap|Chatterjee]] writes about the same deploying-enterprise layer from cybersecurity: board-level risk appetite, single ownership of agent behaviour, vendor diligence and tested kill switches. See [[responsible-ai]].

## Where judgment moves (11:51–15:31)

Two examples from her book interviews:

- **Biology.** Stephen Quake (Stanford, single-cell genomics) described biology to her as *"historically 90% experimental and 10% computational,"* with the ambition to flip it. AlphaFold is her example of the first step; a cell, with 20,000 protein-coding genes, is high-dimensional data no human can process unaided. Her conclusion: *"the more AI can surface and search the hypothesis for us cheaper faster and at scale the more important human judgment becomes,"* in choosing which hypothesis to test and in keeping out uses such as a bioweapon.
- **Creative work.** From interviews with designer Brian Collins and a second agency head (surname unclear in the ASR), *"the workflow is becoming like an hourglass."* The top (variations, research) and the bottom (distribution) get cheaper and faster; *"the narrow waist of the hourglass is our taste, our care for the audiences and our judgment of what would work."*

Both examples locate judgment at the point of selection. See [[durable-skills]].

## A practice, not a position (15:31–18:26)

Her own relationship with AI is *"intimate but unsentimental… I use AI every day and… I trust almost none of it by default."* Writing the book made her *"more specific,"* not more or less cautious, and she rejects the optimist-to-doomer spectrum: *"binary trust is lazy trust. The question is… trust it to do what… under which conditions and with what recourse?"* As a parent, she wants her children to hear an adult say *"Let's check it out"* out loud, because *"a judgment isn't taught in lecture… Children watch someone practice it and then they learn it."* Her closing formulation: *"I trust AI precisely but not generally."*

## Linked entities and concepts

- **Entities:** [[McKinsey & Company]] (channel; *Author Talks* series).
- **Concepts:** [[agent-oversight-and-delegation]], [[responsible-ai]], [[jagged-frontier]], [[enterprise-ai-adoption]], [[durable-skills]].
- **Dangling** (single-source mention, deferred): Tiffany Xingyu Wang, Oasis Consortium, Stephen Quake, Brian Collins, Wiley.

## Source quality

Auto-generated ASR transcript of a single speaker, cleaned in quotation only. A book-promotion interview on a consultancy channel: the three-term model, the four dimensions and the procurement questions are the author's frameworks, stated without evidence in the talk. The Quake and designer examples are second-hand, from her interviews. Two transcription problems remain. The AlphaFold figure appears as *"more than 20 million protein structures"*, while the AlphaFold database is usually cited at over 200 million, so the speaker or the ASR is off by a factor of ten. The second designer's name is rendered "Greg Cammy" and could not be confirmed. Talking-head interview; no on-screen material is lost.
