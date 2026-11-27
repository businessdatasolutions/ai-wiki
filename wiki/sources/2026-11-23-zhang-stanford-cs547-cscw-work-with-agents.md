---
type: source
kind: video
title: "Stanford CS547 HCI Seminar | Autumn 2026 | What can CSCW Teach us About How to Work with Agents?"
author: ["Stanford Online"]
publisher: "Stanford Online (YouTube); Stanford CS547 Human-Computer Interaction Seminar, 23 October 2026; speaker Amy X. Zhang, University of Washington"
url: "https://www.youtube.com/watch?v=e1VYwgm9-_s"
date_published: 2026-11-23
date_ingested: 2026-11-27
length: "~56:46 minutes (transcript ~504 lines + 16 stills; human-written caption track, no chapters)"
raw: "../../raw/videos/stanford-cs547-what-can-cscw-teach-us-about-how-to-work-with-agents.md"
stills: "../../raw/videos/stanford-cs547-what-can-cscw-teach-us-about-how-to-work-with-agents.stills.md"
tags: [stanford-online, cs547, hci-seminar, cscw, computer-supported-cooperative-work, amy-x-zhang, social-futures-lab, human-agent-collaboration, boundary-objects, mutual-awareness, sociotechnical-gap, continuous-alignment, computational-wear, cocoa, ream, compass, paperping, social-rag, case-law, institutional-design, alignment, agents, long-running-agents]
relationships:
  - type: supports
    target: 2026-11-20-chase-langchain-future-of-agents
    via: "Shared topic: agents that run for hours or days in the background, and how people stay in the loop with them. Chase from the agent platform side (goals, triggers, feedback); Zhang from CSCW (shared artifacts, awareness, continuous alignment)."
  - type: supports
    target: 2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder
    via: "Shared topic: the human load of managing many parallel agent threads. Carson describes his own queue of 10–15 agents; Zhang reports engineers' days spent switching between agent threads and proposes peripheral awareness instead of live views."
---

# Zhang — What can CSCW teach us about how to work with agents? (Stanford CS547, Oct 2026)

> This lecture covers:
>
> - How CSCW theories about shared artifacts, mutual awareness, and formalizing social requirements can inform the design of systems that coordinate human and AI agent activity
> - Four novel systems built on these lessons: Cocoa (flexibly delegating agency around a shared notebook-like artifact), Ream (a workspace for mutual awareness between humans and agents), Compass (aligning social media feed algorithms to changing user preferences), and Social-RAG (aligning an agent to a team's social norms)
> - A case for drawing on institutional design, including governments, communities, and organizations, to shape future human-AI institutions, with a case study on building precedent-aligned AI systems inspired by case law
>
> Amy X. Zhang is an Associate Professor of Computer Science at the University of Washington's Allen School of Computer Science & Engineering, where she leads the Social Futures Lab.
>
> — channel description, Stanford Online (links omitted)

## TL;DR

A ~57-minute slide talk by **Amy X. Zhang** in the Stanford CS547 Human-Computer Interaction Seminar, given on 23 October 2026. **[[Stanford Online]]** published it on 23 November 2026. Her title slide lists her as lead of the Social Futures Lab, associate professor at UW's Allen School and visiting researcher at Ai2, *"on sabbatical, Google DeepMind"* ([[Google DeepMind]]). The caption track is human-written.

Her claim is that CSCW, the field of computer-supported cooperative work, already has theories for problems people now meet working with agents. It has studied coordination and alignment among people since the 1980s. She sees agents changing in three ways and pairs each with an old CSCW theory, a system from her lab and a design idea (still 1). Her test for where the theory stops working: CSCW applies *"as long as there's a human"* somewhere in the interaction.

1. **Long-running agents need boundary objects.** A boundary object (Star & Griesemer, 1989) is a structured artifact, such as a form, record or map, that different groups use in their own way while it keeps one meaning. Collaboration moves from chat and meetings, through *boundary-negotiating artifacts* that sort out who does what, to boundary objects that carry the routine. Informal coordination never fully disappears (still 2). Work with agents is still at the chat stage. That suits short one-off delegation and fails for long, interleaved work (still 3).
2. **Cocoa** (CHI 2026 Best Paper) puts an agent's plan inside a document editor as an *agent notebook* (still 4). Each step can be assigned to the user or an agent, edited, rerun from a checkpoint, or taken over. The agent asks for help inside the plan, and planning and execution interleave. A lab study (n=16) and a one-week field study (n=7) found it more steerable with equal ease of use (still 5).
3. **Where the theory breaks.** For agent-to-agent coordination, CSCW has little to say, because the artifacts agents make for each other will look *"very alien"*. When two people coordinate through their agents, the agents themselves become the boundary object (still 6). She invites work on agents as boundary objects that show each community its own view of a shared substrate.
4. **Agents embedded in workspaces need mutual awareness.** Awareness of others gives coordination without talk, common ground and accountability (Dourish & Bellotti, 1992). The mechanisms are feedthrough, consequential communication and intentional communication. Today agents mostly use the last: a fast, jargon-laden log. Some add a cursor, which she finds distracting. Changes made by agents lose their history.
5. **Ream** (in submission to CHI 2027) builds on two design principles from the literature (still 7). One is *social translucence*: the frosted-glass door, aware enough without a full view. The other is *edit wear and read wear*: traces that, like a worn book, show where attention went. Every open, read and edit becomes a signal, shown as attention bars per file and on citations (still 8). Agents read the same history through a `read_signals` tool. Lab (n=12) and field (n=6) studies found that users changed behavior in different ways: some divided the work, some followed the agent. Agents read each other's signals, and users wanted per-agent attribution (still 9).
6. **Her take on awareness:** real-time, fine-grained agent activity is *"not the way to go"*. Human and agent speeds differ too much, and agents are always available. She describes engineers' current days as *"miserable"*, spent switching between agent threads, and calls for peripheral awareness and fewer interruptions (still 10).
7. **Social agents need continuous alignment.** Mark Ackerman's *sociotechnical gap* is the divide between what must be supported socially and what can be supported technically. It can be narrowed and never closed. So alignment is a loop, not a one-time act (still 11):
   - start from a first-order approximation;
   - notice a gap, or let users point one out;
   - adjust;
   - repeat as preferences drift.
8. **Compass** (UIST 2026) aligns a YouTube Shorts feed to preferences users state in natural language. It works through DOM edits and simulated activity, and asks in situ when behavior drifts from the stated preferences. In a 10-day study with 15 participants, it improved alignment at no cost to usability. Without its prompts, people rarely refined their preferences (still 12). **PaperPing** (Social-RAG, CHI 2025) learns a research group's norms from its Slack history to time and explain paper recommendations. Across 18 channels and 500+ researchers, 11 channels kept it for over a year, until the lab turned it off. In quiet channels it crowded out human talk (still 13).
9. **Aligning AI at scale is a governance problem.** Model constitutions are underspecified and cannot list every edge case. Case law offers a pattern for this: decide new cases by grounding them in precedent, building a *"living constitution"* (still 14). Further examples: juries, citizen assemblies, federalism, and inquisitorial versus adversarial courts. From these come evaluation principles: procedural justice, legitimacy, subsidiarity, plurality, democracy (still 15). She calls the programme *sociotechnical institutional design*, after Elinor Ostrom's work on governing the commons (still 16).

An audience member reframed awareness in organizational-behavior terms. Today's agent work is *sequential* interdependence: hand off, wait, hand back. Awareness matters for *reciprocal* interdependence, where both move at once. Zhang agreed, citing merge conflicts with an agent editing her own slides. Another attendee described running many agents as playing *"30 slot machines"* at once.

## Visual canon

The frame is a composite of slide and speaker. Stills below are the slide region only, at native 1280×720.

### 1 · The talk map: three trends, three theories, four systems

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/05-06m40-talk-map-three-trends-three-theories-four-systems.webp|Talk map with three agent trends, CSCW theories, systems and design ideas]]

*Still at [6:40](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=400s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

| How agents are changing | CSCW theory | System | Design idea |
| --- | --- | --- | --- |
| 01 Long-running: minutes → hours, days | Boundary objects: what artifacts should shape human-agent work? | Cocoa | Interactive plans that interleave people + agents, planning + doing |
| 02 Embedded: chat → shared workspace | Mutual awareness: how should workspaces support coordination? | Ream | Computational wear: glanceable traces of agent activity |
| 03 Social: private → social spaces | Sociotechnical gap: how do agents align to social preferences? | Compass, PaperPing | Continuous alignment loops between agent and people |

*Still vs. transcript:* she names the three trends and promises a theory and a system for each; the grid of questions and design ideas is only on the slide.

### 2 · Boundary objects form as work becomes routine

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/07-09m04-boundary-objects-form-as-work-becomes-routine.webp|Boundary objects form as work becomes routine]]

*Still at [9:04](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=544s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

**Informal coordination** (new collaborations run on chat and meetings; e.g., messages, notes) → **Boundary negotiating artifacts** (evolving artifacts sort out who does what; e.g., sketches, lists) → **Boundary objects** (structured artifacts carry the routine; e.g., forms, records, maps).
*↺ Informal coordination never fully disappears: there are always edge cases.*
Lee (2007), Boundary Negotiating Artifacts, JCSCW · Lutters & Ackerman (2007), Beyond Boundary Objects, JCSCW.

*Still vs. transcript:* the narration walks the axis; the slide gives each stage its examples and the two sources.

### 3 · We need boundary objects in human-agent collaboration

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/08-09m56-we-need-boundary-objects-in-human-agent-collaboration.webp|We need boundary objects in human-agent collaboration]]

*Still at [9:56](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=596s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

**Today:** a lot of work with agents still happens in informal chat; fine when tasks are short (minutes), one-offs, and purely delegation. **Increasingly:** long-horizon, interleaved work could benefit from **shared artifacts** to reduce coordination friction. Left: a chat ("Find papers on feedback tools" · "Okay! Searching again…" · "Ugh. Start over from #3"). Right: a shared plan with owners per step (1 Search papers: agent ✓ · 2 Pick key ones: you ▶ · 3 Summarize: agent).

*Still vs. transcript:* the two mock-ups show the shift from chat to a plan with owners per step, which the narration only states.

### 4 · Cocoa: an agent notebook inside a document editor

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/10-10m28-cocoa-agent-powered-document-editor-with-agent-notebooks.webp|Cocoa, an agent-powered document editor with agent notebooks]]

*Still at [10:28](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=628s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

The plan, labelled *boundary object*, sits in the document under the question *"What are new ways for AI agents to interactively elicit human feedback?"*, with *Update and run*, *Collapse* and *Delete all*. Each step has a toggle for agent or user. One step is marked *Edited* by the user; one says *User guidance requested*. A side panel lists retrieved papers to save.

*Still vs. transcript:* the interface itself: per-step ownership toggles, the edit marker and the agent's request for guidance.

### 5 · Cocoa: lab study and field study

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/11-13m12-cocoa-lab-study-and-field-study.webp|Cocoa lab study and field study]]

*Still at [13:12](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=792s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

**Lab study** · n=16 · Cocoa vs. chat panel. **Field study** · n=7 researchers, one week.
- Many examples of interleaving.
- People found the system more steerable, while maintaining an equivalent ease of use.

Real plans from P3 and P5: user and agent steps interleaved (details redacted).

*Still vs. transcript:* the sample sizes and the comparison condition (a chat panel) are only on the slide.

### 6 · Where boundary-object theory stops applying

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/12-14m46-human-ai-boundary-objects-going-forward-my-take.webp|How should we think about human-AI boundary objects going forward]]

*Still at [14:46](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=886s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

**My take:** CSCW work on boundary objects is only useful as long as there is a human interacting with the artifact. Traditional CSCW does not translate to boundary objects for agent-agent coordination. Same for human-human coordination facilitated by agents: in this case, *the agents themselves* are arguably serving as the boundary object between people.
Four configurations: human–document–human · human–document–agent · agent–?–agent · human–agent–?–agent–human.

*Still vs. transcript:* the four-row diagram, which makes the boundary of the claim visible.

### 7 · Translucent, not transparent; peripheral, not attention-grabbing

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/18-26m44-design-for-user-awareness-translucent-and-peripheral.webp|How should we design for user awareness of agents]]

*Still at [26:44](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1604s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

**Translucent, not transparent:** awareness doesn't need a full, real-time view of the agent to be useful (doors: opaque, transparent, translucent). **Peripheral awareness, not attention-grabbing:** digital things look new forever; edit wear and read wear are lightweight ways to provide awareness of agent attention (wear marks on scroll bars).
Erickson & Kellogg (2000), Social Translucence, ACM TOCHI · Hill et al. (1992), Edit Wear and Read Wear, CHI.

*Still vs. transcript:* the two principles side by side, with their sources.

### 8 · Agent computational wear

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/19-27m32-agent-computational-wear.webp|Agent computational wear in the Ream workspace]]

*Still at [27:32](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1652s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

- Every action (open, read, edit) = a signal of interest from user or agent.
- Signals drive small visualizations in the workspace.

**File tree attention bars:** two bars per file, user vs. agent activity. **Inline reference chips:** citations carry both bars too.

*Still vs. transcript:* the rule that every action is a signal, and the two-bar encoding (user vs. agent) per file and per citation.

### 9 · Ream: lab and field study

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/22-29m12-ream-lab-and-field-study.webp|Ream lab and field study]]

*Still at [29:12](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1752s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

**Lab study** · n=12. **Field study** · n=6, one week.
- Agent awareness changed user behavior in different ways.
- Agents read each other's signals also and adjusted their behavior accordingly.
- Wanted: per agent attribution.

Activity traces, user and agent: *"P7 delegated, then read; P9 interleaved throughout."*

*Still vs. transcript:* sample sizes, and the two participants' traces that show the two styles.

### 10 · Human-agent mutual awareness in the future

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/23-30m50-human-agent-mutual-awareness-in-the-future.webp|Human-agent mutual awareness in the future]]

*Still at [30:50](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1850s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

**My take:** real-time fine-grained agent activity is rarely needed for coordination because human and agent speeds are too different, and agents are always available, unlike humans. "Live" agent identifiers are usually overkill.
**Future work:** agents will just always be running in the background, with cross-app awareness of user behavior. How do we want agents to adjust their behavior based on user activity? What are useful agent indicators that support peripheral awareness? How can we rethink the ways users are notified about agent work?
Sketch: a status list. *You:* focus mode, writing the intro, back at 3pm · *Agent 1:* done, waiting for your review · *Agent 2:* waiting for you to pick key papers · *Agent 3:* checking citations…

*Still vs. transcript:* the status-list sketch, her alternative to live cursors, is only on the slide.

### 11 · Continuous alignment

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/26-37m54-mitigating-the-gap-continuous-alignment.webp|Mitigating the sociotechnical gap when aligning social agents]]

*Still at [37:54](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2274s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

*Instead of alignment being a 1-time action, we need to build in **continuous alignment** loops.*
1. Start with a first-order approximation that bootstraps agent behavior.
2. Agent is embedded and acting in the social environment.
3. There is a monitoring system that notices a gap, or lets users point to one.
4. Agent addresses the gap and adjusts its behavior.
5. Over time, the gap widens as social preferences or the technical encoding changes. (Back to 2.)

*Still vs. transcript:* the loop as five numbered steps; both systems that follow are instances of it.

### 12 · Compass: field study

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/30a-41m58-compass-field-study.webp|Compass field study]]

*Still at [41:58](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2518s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

**10 days · n=15 · Compass vs. manual alignment.**
- Improved alignment, with no cost to system usability.
- Using social media was still fun.
- Without Compass's in-situ suggestions, few people bothered to refine their preferences once entered.

Session timelines over five sessions: Compass users (C2, C6) keep refining; baseline users (B1, B4) rarely refine.

*Still vs. transcript:* duration, sample size and the timelines.

### 13 · PaperPing: field study

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/33-44m40-paperping-field-study.webp|PaperPing field study]]

*Still at [44:40](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2680s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

18 Slack channels · Participants: 500+ researchers · Interviews: n=28.
- 11 of 18 channels kept on using it voluntarily for over a year (until we shut it down)!
- 88% said it took little effort to integrate into the group.
- One drawback we saw was that in quiet channels, it could crowd out human conversation.

*Still vs. transcript:* she says *"over 500 researchers"* and a three-month deployment; the 11-of-18 retention, the 88% and the interview count are on the slide only.

### 14 · Case law as inspiration for AI alignment

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/36-48m32-case-law-as-inspiration-for-ai-alignment.webp|Case law as inspiration for AI alignment]]

*Still at [48:32](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2912s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

**The problem:** constitutions are underspecified; impossible to enumerate all edge cases; time leads to changes in judgments and new conditions. **From law:** case law decides new cases by grounding to past ones; a continuous alignment loop where precedents are set, relitigated and overturned over time; becomes a "living constitution".
**How the lab used it:** in-context learning and RLAIF experiments showing examples improve alignment over principles; metrics for case retrieval beyond semantic similarity; benchmarking models on reasoning from precedent; community AI bots aligned to a community; cases that help domain experts reason about model behavior.
Chen & Zhang (2025), Case Law Grounding · Chen, Feng, Park & Zhang (2025), SPICA, Findings of ACL · Kuo et al. (2026), Botender, CHI · Feng et al. (2023), Case Repositories · Feng et al. (2026), PolicyPad, CHI.

*Still vs. transcript:* the five research lines and their papers; she says she could give a whole talk on it and moves on.

### 15 · Institutions as sources of evaluation principles

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/37-49m54-other-examples-principles-from-institutions.webp|Other examples, and principles from institutions]]

*Still at [49:54](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2994s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

| System | Offline institution it draws on |
| --- | --- |
| Jury Learning, Digital Juries | offline juries |
| Collective Constitutional AI | citizen assemblies |
| PolicyKit, MLSGov | federalism, "laboratories of democracy" |
| Online reporting systems | inquisitorial vs. adversarial judicial systems |

| Principle | Question |
| --- | --- |
| procedural justice | What is the process for decision-making, and is it transparent, fair, and consistent? |
| legitimacy | Do people accept the outcomes of this process, even if they might disagree with it? |
| subsidiarity | To what degree is each decision made at the most local level possible? |
| plurality | Is there room for multiple perspectives and values? |
| democracy | How are the people impacted by a system able to give input into it? |

*Still vs. transcript:* the mapping of systems to institutions, and each principle's question; she names the principles only.

### 16 · Towards sociotechnical institutional design

![[assets/2026-11-23-zhang-stanford-cs547-cscw-work-with-agents/38-51m14-towards-sociotechnical-institutional-design.webp|Towards sociotechnical institutional design]]

*Still at [51:14](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=3074s) from Stanford Online, "What can CSCW Teach us About How to Work with Agents?".*

*Instead of taking the technology as a given, research on offline institutions can provide lessons and inspiration for how to reimagine online sociotechnical institutions.*
- **We should do more of this.** CSCW provides a blueprint: Ostrom's principles from *Governing the Commons* were generative for online peer production and community moderation, though her work was on farmers and villagers.
- Not everything applies: **take just the pattern or spirit of the approach**, not always the details. Existing institutions also have their problems.
- Close the loop: build prototypes of the systems, deploy, and evaluate them.
- Online affords more opportunity to iterate and experiment than offline. **New forms of institutions and new theories** can be built from the offline starting point.

*Still vs. transcript:* the four rules of the method in her own condensed wording; the slide stays up through the Q&A.

## Why no dynamic-capabilities tags

The talk is HCI research on human-agent coordination and alignment, not on how firms renew their capabilities. None of the Warner & Wäger cells fits without stretching, so the field is left off. The closest readers are the [[agent-oversight-and-delegation]] and [[agent-fleet-management]] pages, not the W&W lens.

## Related in this wiki

- [[2026-11-20-chase-langchain-future-of-agents|Chase, The Future of Agents]]: persistent agents that run for days, triggered by events, and goals designed around the user feedback they need.
- [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Carson on How I AI]]: one person's queue of 10–15 agents, run from folders and a handwritten list.
- [[agent-oversight-and-delegation]]: Cocoa's per-step ownership and Ream's peripheral awareness are designs for the delegation and review that page discusses.
- [[agent-fleet-management]]: her account of engineers switching between agent threads, and the status-list sketch (still 10).
- [[responsible-ai]]: case law, juries and citizen assemblies as patterns for aligning models used at scale.
- [[Sam Altman]]: his post calling algorithmic feeds *"the first at-scale misaligned AIs"* motivates Compass (slide at 39:16, not published).

## Linked entities and concepts

- **Entities:** [[Stanford Online]], [[Google DeepMind]], [[Sam Altman]].
- **Concepts:** [[agent-oversight-and-delegation]], [[agent-fleet-management]], [[responsible-ai]].
- **Dangling** (single-source mention, deferred): Amy X. Zhang; the Social Futures Lab (University of Washington); Ai2; Merrie Morris (Google DeepMind, CSCW 2026 keynote, mentioned in Q&A); Mark Ackerman; Susan Leigh Star; Elinor Ostrom; the systems Cocoa, Ream, Compass, PaperPing and Social-RAG.

## Debates and supersession

- **Real-time awareness or not.** Zhang argues live, fine-grained views of agents are rarely needed. An audience member argued the opposite: awareness matters most for reciprocal work, where human and agent act at the same time. That is where agentic work is heading. She agreed the direction is real. The two positions differ on the kind of interdependence, not on the facts.
- **CSCW's reach.** She reports boundary drawing in the field itself. One attendee, an editor at CSCW, said they are sometimes told to reject work on single-user AI as out of scope. Her own line is a human somewhere in the interaction.
- **Study sizes.** Cocoa (n=16 lab, n=7 field), Ream (n=12, n=6), Compass (n=15, 10 days) and PaperPing (18 channels, 28 interviews) are small, short deployments with researchers as users, typical of HCI systems papers. Ream is in submission. The talk presents the results, not the papers; none of the papers is ingested.

## What was actually ingested

The full transcript (human-written captions, three names corrected at acquire) and the slides. 39 stills were cut by hand because Gemini returned HTTP 402, and each was read at full resolution. 16 are published here; the [stills manifest](../../raw/videos/stanford-cs547-what-can-cscw-teach-us-about-how-to-work-with-agents.stills.md) records all 39 with readings. The Compass demo video failed to play in the room and is not in the recording.
