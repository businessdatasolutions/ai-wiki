---
type: source
kind: video
title: "Driving Agentic Transformation: How AI Is Rewriting the Playbook on Large-Scale Change"
author: ["McKinsey & Company"]
publisher: "McKinsey & Company (YouTube channel), Inside the Strategy Room; host Sean Brown; Chase Covington (partner, New York; transformation and strategy and corporate finance practices) and Tomer Slaney (partner, New York; change management)"
url: "https://www.youtube.com/watch?v=XZcbnO2m9UE"
date_published: 2026-11-08
date_ingested: 2026-11-16
length: "~44:53 minutes (transcript ~347 lines; ASR auto-generated track, 14 chapters)"
raw: "../../raw/videos/driving-agentic-transformation-how-ai-is-rewriting-the-playbook-on-large-scale-change.md"
tags: [mckinsey, inside-the-strategy-room, sean-brown, chase-covington, tomer-slaney, transformation-office, pmo, integration-office, agentic-transformation, agentification, change-management, reporting, weekly-cadence, cognitive-surrender, attention-surrender, human-in-the-loop, ai-slop, consistency-audit, deck-drafting, meeting-agents, wave, vibe-coding, data-security, open-source-models, model-upgrades, team-size, junior-roles, podcast]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services
    via: "two McKinsey episodes on agents inside a central function: Heimes and Peters forecast shared services 20–30% smaller but more productive; Slaney describes a four-person transformation office that freed a person's worth of time with four agents, and Covington says making the office smaller is not where the value lies"
    confidence: 0.65
  - type: supports
    target: 2026-05-02-dutt-chatterji-ai-experimentation-to-transformation
    via: "both address who redesigns a workflow for AI: Dutt et al.'s step of engaging those closest to today's process, and Slaney's account that the transformation-office agents that worked were built by staff who did the grunt work themselves"
    confidence: 0.6
  - type: supports
    target: 2026-09-30-lenk-karunakaran-stanford-hai-industry-conversation-instacart
    via: "both describe AI use starting inside a team: Lenk measures diffusion from a team's first heavy user, Slaney describes transformation-office staff who began automating their own reporting after exposure to tools such as Cursor"
    confidence: 0.55
  - type: supports
    target: 2026-05-28-from-event-to-ecosystem-rethinking-how-technology-leaders-build-knowledge-in-the-ai-era
    via: "both name the risk of taking machine output without understanding it: Tate's test that more output with less understanding is 'surrendering to the machine', Covington's 'cognitive surrender' among junior staff and the review moments he sets against it"
    confidence: 0.55
---

# Covington & Slaney (McKinsey, Inside the Strategy Room) — the agentic transformation office

> Agentic AI is rewriting the rules of large-scale transformation. By automating reporting, surfacing performance insights, and connecting fragmented data, AI agents can help transformation offices move beyond tracking progress to accelerating it. But the biggest opportunity isn't simply to work faster—it's to free leaders and teams to focus on the human decisions that make change stick.
>
> In this episode of Inside the Strategy Room, McKinsey's Chase Covington and Tomer Slaney explore how agentic AI is reshaping the transformation office. They discuss how organizations can establish a single source of truth, identify performance gaps earlier, improve the cadence and quality of leadership conversations, and redirect human capacity toward coaching, alignment, and navigating complex change.
>
> *— Channel description, McKinsey & Company*

## TL;DR

A 45-minute episode of *Inside the Strategy Room* on the [[McKinsey & Company]] channel, published 8 November 2026. Host [[Sean Brown]] talks with two New York partners: **[[Chase Covington]]**, a leader in the transformation and strategy and corporate finance practices and co-author of the McKinsey article *The agentic transformation office: Redefining the economics of change* (not ingested), and **Tomer Slaney**, an expert in change management. The subject is the **transformation office (TO)**: the team, under various names (PMO, integration office, growth office), that runs a large change programme's weekly cycle of data, decks and executive meetings.

**Auto-generated transcript, corrected in quotation only.** One substitution runs through the whole file: the ASR hears *agentification* as "identification" and *agentify* as "identify" ("identifying the transformation office" is *agentifying the TO*), and "to" is usually *TO*. Other corrections: "Mckenzian company" / "McKenzie" → McKinsey & Company, "Chase Cington" → Chase Covington, "dcasture, a carval" → divestiture, a carve-out, "data pool" → data pull, "codics" → context. The host addresses Slaney as "Tor"; the ASR also gives "Tor Laney", "Tilmer" and "Tolar". The spelling *Tomer Slaney* is the channel description's. A stretch at 20:23–20:30 is lost to a repeated-syllable ASR artefact.

What it adds to the wiki:

1. **A function measured.** One four-person TO spent **80%** of its time on reporting, materials, meeting preparation and follow-ups. It built **four agents** and freed *"an entire individual's worth of time"* while the team shrank (Slaney).
2. **Two named failure modes.** *Cognitive surrender*, taking a polished chatbot draft as your own work (Covington), and *attention surrender*, multitasking because an agent is listening, with an action item to have the CEO phone every employee as the example (Slaney).
3. **Concrete agent uses**: a nightly agent that checks every plan for changes whose dependent changes did not follow; consistency audits across this week's deck, last week's and the finance reports; deck *drafting* rather than deck *making*; agents that check meeting invites against agreed actions.
4. **Review rules from practice.** *"If you put something on a page, it's yours"*; a Shark Tank-style pitch of any AI-drafted material; *"same length deck, sharper insight"*; and *"Don't use your AI bots to talk to the business."*
5. **Two claims about models**: most TO work *"can be done by open source models,"* and teams that switched to a newer model saw their workflows regress.
6. **A view on headcount.** Shrinking an already small office *"doesn't really make a lot of money"*; the junior jobs changed rather than disappeared (Covington).

Two consultants describing a service their firm sells, with McKinsey's own Wave platform as the answer to the data-security question. The 80% figure comes from one team, and the outcomes are anecdotes from client work.

## The transformation office as a late adopter

The premise, from their article, is that the function charged with driving change across an organisation is among the slowest to adopt AI. Covington: *"that's kind of the dirty secret."* TOs often push agentic solutions onto the rest of the organisation, but *"they're just busy, really, really busy with the day-to-day."* Once they step back, *"a lot of the grunt work in a transformation office"* can be agentified, so that *"you're not producing a report, you're producing a change outcome in the enterprise."* This is the `contextual/internal-barriers` cell turned on the change function itself: the weekly cycle leaves no time to redesign it.

Covington rejects a separate category of agentic transformation. Two years ago clients asked for either *"an old school transformation"* or *"an agentic transformation"*; now *"all transformations need to be using agentic levers,"* as unremarkable as saying *"I'm using the internet for my transformation in 2005."* The approach applies to any change programme: *"a transformation, … a turnaround, … a merger integration, … a divestiture, a carve-out."*

Agentification lowers *"the human resource load required to stand up an effective transformation office,"* but Covington finds a second effect more interesting: an agentified TO *"can reach more employees, and if you can reach more employees you can embed change more granularly into the organization, which our research shows dramatically increases the odds of success."* The research is not described.

## Where the week goes

Slaney's example team had four people, and *"80% of that time is spent on reporting, creating materials, preparing for meetings, doing the follow-ups,"* work that is *"very repeatable, very predictable, very manual"* but has to be right, because change depends on *"trust in the system."* Late in a transformation the office is expected to shrink, yet it gains access to more data sources, so reporting grows: *"expected to be doing more with less and getting more of the grunt work to boot."*

The cadence explains why. Data is pulled weekly, and the *"famous week-over-week change"* is crunched between the pull and the weekly executive meeting, the same window in which the team should be finding insights. Slaney calls it a *"structural limitation or structural ceiling."* Old data has its own cost: the question *"is this data changed"* is *"very often used as a way to not make decisions and not drive change."* With agents on the grunt work, the cadence stays weekly, but the team can *"front-run a lot of the grunt work"* and spend the window on insights and coaching.

## Cognitive surrender and attention surrender

Covington's first hiccup: *"the technical term is cognitive surrender, which is a really scary way of saying you just let the AI chatbot do your job."* He saw it in junior colleagues and in clients. The chatbot's output is well formatted and structured, *"but then when you review it, it actually turns out to be slop."* His remedy is to create *"the right moments for human in the loop"* and to *"treat the agents you're creating … almost like junior colleagues, but still keep the reviews as the information moves up the chain,"* so that nothing embarrassing reaches the CEO. Later he applies the term to decks: team members who present agent-drafted material *"won't really know what they're saying. That would be that cognitive surrender because, ah, someone else wrote that."* [[2026-05-28-from-event-to-ecosystem-rethinking-how-technology-leaders-build-knowledge-in-the-ai-era|Allan Tate's MIT Sloan CIO Symposium keynote]] uses a related phrase as a test: more output with less human understanding is *"surrendering to the machine."* See [[ai-deskilling]].

Slaney adds *attention surrender*: *"If you know that something else is paying attention, you can multitask."* One team turned meeting transcripts into action lists. In one meeting the chief transformation officer asked a participant, sarcastically, *"Do you just want the CEO to call every single employee and tell them to do their job?"* The chatbot logged it as an action for the CEO. A human still read the list, so it was caught; unattended, it would have gone to the CEO.

## What the agents do

Slaney lists the work being agentified, from the obvious to the less so:

- **Data pulls, admin and first drafts.** Pulling the data, updating trackers, filing documents, *"the first pass at things."*
- **Consistency checks.** Agents read *"every last slide on every last appendix"* and ask whether this week's insights contradict last week's, whether the transformation data contradicts *"the data we showed in the MBR last week,"* and whether a changed initiative was followed by the expected change in a dependent one. This makes the team *"do better, not just do more and do faster."*
- **The nightly agent.** It runs over all plans every night, finds what changed and whether the expected follow-up changes in dependent initiatives happened, and gives the TO a prioritised list. The TO can then contact the owner *"before they have to explain a variance"* (*"I'm going to put myself in your corner"*), which built goodwill. It was also *"the one that created the most additional work up front"*, needed a lot of training, and had to be dialled back.
- **Deck drafting.** *"I'm … very, very purposely calling it deck drafting and not deck making."* Late in a transformation, with *"50 weeks of decks"*, an agent does most of the upfront work and reads past decks and finance and revenue reports *"with a fine-tooth comb"* to flag inconsistencies for the executives' prep notes. People must still go through *"every single page and every single insight."*
- **Meetings.** Agents trained on attendance and agendas check, through Outlook MCP connections, whether the person due to report on an agreed action has actually been invited.

The consistency audit is *"where the most junior people on the TO spend the most of their time,"* a *"detective effort"*; the stated aim is to make it more insightful and accurate, not only faster. On feeding the agents, Slaney's rule is *"feed it the information and don't automate the emails."* See [[ai-agents]].

## Review rules

Slaney warns that the tools *"can create so much more data"* that the TO's workload rises unless thresholds are set, and that colleagues recognise AI-generated content, so *"the bar for this being useful is higher. Just generating more and generating more often to more people is rarely the solution."* The exception is the change agents in business units, for whom more automated communication works.

Covington's rules:

- *"Don't use your AI bots to talk to the business. That sucks."* The TO's job is human to human: *"pushing for value… counseling, providing feedback. No agent's going to do that. So, use your agents to make your TO people better, not create more work for folks."*
- *"Same length deck, sharper insight."* New users make decks *"three times as long."*
- **Pitch it.** *"Have someone pitch to you the material they've created,"* Shark Tank style, with probing questions such as where a data point comes from.
- **Ownership.** *"You can use any tools you would like as long as they're … approved to use by our risk, the client's risk. But if you put something on a page, it's yours."* Answering *"Cursor"* when asked who wrote something is *"an unacceptable answer."* (The host hands the next question to Slaney as if he had said this; Slaney later credits the rule to Covington.)

Most of these agents are obvious (*"you don't need McKinsey to tell you that"*), Covington says, but making them create value *"is relatively difficult"*: it depends on deciding when a review happens, who does it and how it cascades, and *"there's not a five-point framework for it."* See [[agent-oversight-and-delegation]].

## Data security when everyone vibe codes

TO data is sensitive. Early agentification ran on data extracts. When people built materials by hand, they had *"the common sense of saying, hey, this… has the word confidential in the title,"* and *"that control is not necessarily built into any … vibe coded agent that somebody's come up with."* McKinsey's response on its **Wave** transformation platform is "Wave apps", which work with the data inside Wave without weekly extracts and set visibility to match the audience. The general point: tech teams were trained on guardrails and risk control, but *"as this is being more democratized and we're seeing everybody vibe code from every function, the guard rails… the mindset of the risk has not caught up."* See [[vibe-coding]].

## Smaller, or better

Asked why not simply add people, Slaney says the TO's size *"should be driven by the number of work streams, stakeholders and interactions"*; a bigger team making more slides needs people to read them, and *"the data and the transformation only goes one way; there's always more."* The four-person team built four main agents (materials creation, admin, checks), offloaded the work, freed *"an entire individual's worth of time,"* and shrank while doing more of the value-adding work: refilling the pipeline, valuation edge cases, refining business cases. The ASR garbles the capacity figures in this passage.

Covington: TOs, PMOs and integration offices *"shouldn't be cottage industries,"* and *"taking a small group and making it a little bit smaller doesn't really make a lot of money for your enterprise."* The value is that small group spending its time on *"coaching, providing feedback, pushing for more value."* *"Folks join a TO to drive change, not to make reports."* On the same channel, [[2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services|Heimes and Peters]] forecast that shared-services organisations will end up 20–30% smaller but dramatically more productive. See [[automation-vs-augmentation]] and [[micro-productivity-trap]].

## Models: open source, and stop upgrading

Covington: *"The vast majority of the stuff we observe in a transformation office can be done by open source models."* Failure comes from how the workflow is fitted to the context: *"I don't see failure mode on, oh, we picked the wrong model."* Slaney adds: keep the same model. Teams that moved to *"a newer fancier LLM"* *"have actually… seen a regression,"* because the workflow was planned around what the old model would return; *"don't keep upgrading."* See [[open-source-ai]].

## How to start

Slaney's takeaways:

1. **Understand the workflow first.** *"Don't automate for the sake of automation."* Map what the team does and when, and set the rules for what agents can and cannot do *"before you start building."*
2. **Rethink roles.** Staff the TO with people who can build as well as run. *"All success that we have seen has been organic,"* he says, people with *"the right profiles"* placed *"to feel the pain,"* who could see their own grunt work and reimagine it. Earlier he describes TO staff who, after exposure to tools *"whether it's Cursor or take your pick,"* began saying *"hey, we can make our own lives easier."*
3. **Invest in change management inside the TO.** Say that *"the first one's going to be clunky."*
4. **Protect trust.** *"If you start eroding the trust in the TO, you start eroding the trust in the transformation programs."*

These are `digital-transforming/redesigning-internal-structures` choices for one function: its size, its roles, and the split of its work between people and agents. The second point is also `digital-transforming/improving-digital-maturity`: building skills inside the team rather than bringing data scientists in later. [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Dutt et al.]]'s third step is to engage those closest to today's process. [[2026-09-30-lenk-karunakaran-stanford-hai-industry-conversation-instacart|Lenk]] measures how agentic-AI use spreads in engineering teams from a team's first heavy user, the pioneer.

## Jobs that change

Slaney's best moment was a lunch with a team, a year or two into an implementation, who were *"a lot more excited about the work"* because they no longer spent *"45 minutes of every hour copy pasting materials from data dumps into presentations."* Covington's last word, also used to open the episode: *"I thought, 'Oh, man. Does this mean we no longer need all these junior people?'… Nope. That's not the case. That's not what we observed. We observe all these jobs change"*, toward coaching initiative owners, while *"the underlying core job of changing humans is not different."*

## Linked entities and concepts

- **Entities:** [[McKinsey & Company]] (channel; both speakers), [[Sean Brown]] (host), [[Chase Covington]] (guest; also on [[2026-11-16-pralong-mckinsey-strategy-room-gen-ai-outside-in-diligence|the outside-in diligence episode]] eight days later), [[Cursor]] (named as an example tool), [[Allan Tate]] (via the CIO Symposium keynote).
- **Concepts:** [[agent-oversight-and-delegation]], [[ai-deskilling]], [[ai-agents]], [[automation-vs-augmentation]], [[micro-productivity-trap]], [[vibe-coding]], [[open-source-ai]], [[enterprise-ai-adoption]], [[dynamic-capabilities]].
- **Neighbour sources:** [[2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services]], [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation]], [[2026-09-30-lenk-karunakaran-stanford-hai-industry-conversation-instacart]], [[2026-05-28-from-event-to-ecosystem-rethinking-how-technology-leaders-build-knowledge-in-the-ai-era]].
- **Dangling** (single-source mention, deferred): Tomer Slaney, Wave (McKinsey's transformation platform; also named in the diligence episode).

## Source quality

Auto-generated ASR transcript with one systematic substitution (agentification heard as "identification"), corrected in quotation only. Speakers are identified from the host's handovers; one rule is attributed differently by the host and by Slaney (see *Review rules*). Two partners describing their firm's service and platform, with no client voice. The 80% figure and the four-agent outcome describe one team; the claim that reaching more employees *"dramatically increases the odds of success"* cites unnamed McKinsey research. Useful as a concrete account of agents inside a programme-management function, and for two named failure modes.
