---
video_id: e1VYwgm9-_s
url: https://www.youtube.com/watch?v=e1VYwgm9-_s
transcript: raw/videos/stanford-cs547-what-can-cscw-teach-us-about-how-to-work-with-agents.md
stills_dir: raw/images/stanford-cs547-what-can-cscw-teach-us-about-how-to-work-with-agents
stills_count: 39
extractor:
  method: hand-picked (no Gemini call)
  reason: Gemini API returned 402 (prepayment credits depleted)
  sampling: 341 frames at 360p, one every 10 s over 56:46, consecutive repeats merged into 164 tiles, read as six contact sheets; scene detection (threshold 0.3) found only 4 cuts, because the slide sits at a fixed place in a composite frame (slide left, speaker inset right) and a slide change barely moves the whole-frame average
  dense_pass: slide region only (x 0-424, y 62-298 of the 640x360 copy), one frame every 2 s (1,703 frames), changes at mean absolute difference >= 3; 87 change points, every one of them on a slide the grid already shows (the run from 11:10 to 12:46 is Cocoa's screen-recorded demo, 39:18-39:26 a cut to the speaker when the Compass demo video failed)
  frames: yt-dlp stream URL (<=1080p) seeked with ffmpeg, each frame taken just before the next slide change so builds are complete
  crop: the slide occupies x 0-1280, y 180-900 of the 1920x1080 frame; published stills are that region at native 1280x720, without the speaker inset
acquired: '2026-11-27'
---

# Stills manifest (hand-picked)

A seminar talk recorded by Stanford Online. The frame is a composite: the slide fills the left two-thirds and a camera on the speaker the right third. 39 stills were cut and every one was read at full resolution from its slide crop. 16 are published on the source page; the rest are title cards, section cards, or slides whose text the speaker reads out.

## 01 · 0:34 · Title slide
- File: `01-00m34-title-slide.png` · [0:34](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=34s)
- "What can CSCW teach us about how to work with agents?" Amy X. Zhang: Lead, Social Futures Lab; Associate Professor, UW CSE; Visiting Researcher, Ai2; "*on sabbatical, Google DeepMind". Logos: Social Futures Lab, Ai2, UW Paul G. Allen School of Computer Science & Engineering. **Not published:** title card; affiliations recorded on the source page.

## 02 · 4:02 · We are in the early days of working with agents
- File: `02-04m02-we-are-in-the-early-days-of-working-with-agents.png` · [4:02](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=242s)
- Four questions (what should I do versus agents; how do I know what agents are doing and vice versa; how can agents understand social preferences and norms; how should agents fit into teams, organizations and societies) beside an agent log (`read_full_text(paper_14)`, `search_papers("feedback elicitation")`, "thinking…"), captioned "How we know what the agent is doing today". **Not published:** spoken.

## 03 · 5:02 · What will the agents of tomorrow be like?
- File: `03-05m02-what-will-the-agents-of-tomorrow-be-like.png` · [5:02](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=302s)
- 01 Long-running: minutes → hours, days. 02 Embedded: chat → shared workspace. 03 Social: private → social spaces. **Not published:** the same row heads the talk map (05).

## 04 · 6:08 · CSCW is uniquely able to address many new questions of human-agent interaction design
- File: `04-06m08-cscw-is-uniquely-able-to-address-human-agent-interaction-design.png` · [6:08](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=368s)
- "As agents get more embedded in work and social life, more of CSCW applies. Agents are not humans… but there are useful parallels." / "Models will keep improving, but as long as humans are involved in work, coordination and alignment challenges remain. & CSCW has studied coordination and alignment for decades!" **Not published:** spoken.

## 05 · 6:40 · Talk map: three trends, three theories, four systems — **Published**
- File: `05-06m40-talk-map-three-trends-three-theories-four-systems.png` · [6:40](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=400s)
- Table, rows × columns. How agents are changing: 01 Long-running (minutes → hours, days) · 02 Embedded (chat → shared workspace) · 03 Social (private → social spaces). CSCW theory: Boundary objects (what artifacts should shape human-agent work?) · Mutual awareness (how should workspaces support coordination?) · Sociotechnical gap (how do agents align to social preferences?). System: Cocoa · Ream · Compass, PaperPing. Design idea: interactive plans that interleave people + agents, planning + doing · computational wear: glanceable traces of agent activity · continuous alignment loops between agent and people.

## 06 · 7:54 · What are boundary objects?
- File: `06-07m54-what-are-boundary-objects.png` · [7:54](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=474s)
- The Star & Griesemer (1989) definition in a speech bubble; diagram of Group A (museum workers) and Group B (amateur collectors) linked by a document. "Examples: forms, records, maps. Each side uses it differently, yet it holds a shared meaning." Reference: Star & Griesemer (1989), Social Studies of Science. **Not published:** the definition is read out word for word.

## 07 · 9:04 · Boundary objects form as work becomes routine — **Published**
- File: `07-09m04-boundary-objects-form-as-work-becomes-routine.png` · [9:04](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=544s)
- Three boxes with arrows: Informal coordination (new collaborations run on chat and meetings; e.g., messages, notes) → Boundary negotiating artifacts (evolving artifacts sort out who does what; e.g., sketches, lists) → Boundary objects (structured artifacts carry the routine; e.g., forms, records, maps). Footer: "↺ Informal coordination never fully disappears: there are always edge cases." References: Lee (2007), Boundary Negotiating Artifacts, JCSCW; Lutters & Ackerman (2007), Beyond Boundary Objects, JCSCW.

## 08 · 9:56 · We need boundary objects in human-agent collaboration — **Published**
- File: `08-09m56-we-need-boundary-objects-in-human-agent-collaboration.png` · [9:56](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=596s)
- Today: a lot of work with agents still happens in informal chat; fine when tasks are short (minutes), one-offs, and purely delegation. Increasingly: long-horizon, interleaved work could benefit from shared artifacts to reduce coordination friction. Illustration: a chat ("Find papers on feedback tools" / "Okay! Searching again…" / "Ugh. Start over from #3") against a shared plan (1 Search papers, agent ✓; 2 Pick key ones, you ▶; 3 Summarize, agent).

## 09 · 10:04 · Cocoa title
- File: `09-10m04-cocoa-title-chi-2026-best-paper.png` · [10:04](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=604s)
- "System · 01 Long-running. Cocoa: Co-Planning and Co-Execution with AI Agents · CHI 2026 · Best Paper Award." Surnames visible (first names blank in this frame): Feng, Pu, Latzke, August, Bragg, Siangliulue, Weld, Amy X. Zhang, Chang. Affiliations: University of Washington, University of Toronto, Allen Institute for AI, UIUC. Slide counter 12/55. **Not published:** title card; venue recorded on the source page.

## 10 · 10:28 · Cocoa: an agent-powered document editor with agent notebooks — **Published**
- File: `10-10m28-cocoa-agent-powered-document-editor-with-agent-notebooks.png` · [10:28](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=628s)
- Screenshot of a document editor with an agent plan inside it, arrow-labelled "boundary object". Plan for "What are new ways for AI agents to interactively elicit human feedback?" with buttons Update and run / Collapse / Delete all; steps with per-step agent/user toggles; one step "Edited" by the user; one "User guidance requested"; a sidebar of retrieved papers with Save / Cancel.

## 11 · 13:12 · Cocoa: lab study and field study — **Published**
- File: `11-13m12-cocoa-lab-study-and-field-study.png` · [13:12](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=792s)
- Lab study · n=16 · Cocoa vs. chat panel. Field study · n=7 researchers, one week. "Many examples of interleaving." "People found the system more steerable, while maintaining an equivalent ease of use." Two real plans (P3, P5) with user and agent steps interleaved, details redacted.

## 12 · 14:46 · How should we think about human-AI boundary objects going forward? (my take) — **Published**
- File: `12-14m46-human-ai-boundary-objects-going-forward-my-take.png` · [14:46](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=886s)
- "…and when does drawing from traditional CSCW break down?" My take: CSCW work on boundary objects is only useful as long as a human interacts with the artifact; traditional CSCW does not translate to boundary objects for agent-agent coordination. Same for human-human coordination facilitated by agents: there, the agents themselves are arguably the boundary object between people. Diagram of four configurations: human–document–human; human–document–agent; agent–?–agent; human–agent–?–agent–human.

## 13 · 21:38 · Future work: agents as boundary objects
- File: `13-21m38-future-work-agents-as-boundary-objects.png` · [21:38](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1298s)
- "Future work: how could agents be better boundary objects? Could they help maintain common ground? With coding, agents could also serve and mutate coordination artifacts to different communities. Let's do more theoretical + design work on agents as boundary objects!" Diagram: person–document–agent–?–agent–document–person, the middle braced as "boundary object?". **Not published:** spoken at 14:48–15:35.

## 14 · 22:54 · Workspace awareness
- File: `14-22m54-workspace-awareness.png` · [22:54](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1374s)
- Dourish & Bellotti (1992) definition; why design for mutual awareness: coordination, common ground, accountability. References: Dourish & Bellotti (1992); Clark & Brennan (1991); Erickson & Kellogg (2000). **Not published:** spoken.

## 15 · 23:40 · Mechanisms for staying aware of each other
- File: `15-23m40-mechanisms-for-staying-aware-of-each-other.png` · [23:40](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1420s)
- Feedthrough (seeing the artifact itself change), consequential communication (watching a collaborator's digital body: cursor, telepointer, selection box), intentional communication (explicit messages: "I'm moving this photo"). Beside it, Gutwin & Greenberg's elements of awareness about the present: Who (presence, identity, authorship), What (action, intention, artifact), Where (location, gaze, view, reach), each with its question. Reference: Gutwin & Greenberg (2002), JCSCW. **Not published:** the three mechanisms are spoken; the table is background literature.

## 16 · 24:44 · Mutual awareness in human-agent workspaces
- File: `16-24m44-mutual-awareness-in-human-agent-workspaces-today.png` · [24:44](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1484s)
- Users' awareness of agents today: mostly intentional communication via a chat log that outputs too fast; some systems give agents a digital body via a moving cursor ("This can be distracting!"); instant feedthrough, but changes lose their history. Agents' awareness of users: most are not continuously aware of user activity. **Not published:** spoken.

## 17 · 25:02 · Ream title
- File: `17-25m02-ream-title.png` · [25:02](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1502s)
- "System · 02 Embedded. Ream: Unfolding Mutual Awareness in Human-Agent Workspaces · in submission to CHI 2027." Surnames: Jiang, Suh, Kishore, Bragg, Xia, Siangliulue, Weld, Amy X. Zhang, Chang. Affiliations: University of Washington, UC San Diego, Allen Institute for AI. **Not published:** title card; status recorded on the source page.

## 18 · 26:44 · How should we design for user awareness of agents? — **Published**
- File: `18-26m44-design-for-user-awareness-translucent-and-peripheral.png` · [26:44](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1604s)
- Translucent, not transparent: "Awareness doesn't need a full, real-time view of the agent to be useful" (doors: opaque, transparent, translucent). Peripheral awareness, not attention-grabbing: "Digital things look new forever. Edit wear and read wear are lightweight ways to provide awareness of agent attention" (edit and read wear on scroll bars). References: Erickson & Kellogg (2000), ACM TOCHI; Hill et al. (1992), Edit Wear and Read Wear, CHI.

## 19 · 27:32 · Agent computational wear — **Published**
- File: `19-27m32-agent-computational-wear.png` · [27:32](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1652s)
- "Every action (open, read, edit) = a signal of interest from user or agent. Signals drive small visualizations in the workspace." Screenshot of the workspace (file tree, document "Interacting with LLMs and AI agents", chat pane). File tree attention bars: two bars per file, user vs. agent activity. Inline reference chips: citations carry both bars too.

## 20 · 28:14 · Per-file signal history and PDF read wear
- File: `20-28m14-per-file-signal-history-and-pdf-read-wear.png` · [28:14](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1694s)
- Per-file signal history (who did what to this file, and when); PDF read wear (text the agent extracted gets highlighted). Caption: "Left: a file's action history. Right: PDF passages the agent quoted." **Not published:** spoken at 27:35–27:58; 19 shows the interface.

## 21 · 28:34 · Awareness for the agent
- File: `21-28m34-awareness-for-the-agent.png` · [28:34](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1714s)
- "The agent reads the same history. A `read_signals` tool returns: papers you read recently; papers you revisited, noted, or wrote about; report papers you have / haven't touched. Proactive suggestions: next tasks drawn from recent activity." Screenshot of four suggested tasks. **Not published:** the tool's name is the only addition; recorded on the source page.

## 22 · 29:12 · Ream: lab and field study — **Published**
- File: `22-29m12-ream-lab-and-field-study.png` · [29:12](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1752s)
- Lab study · n=12. Field study · n=6, one week. Agent awareness changed user behavior in different ways; agents read each other's signals and adjusted their behavior accordingly; wanted: per-agent attribution. Activity traces of user (blue) and agent (orange) for P7 and P9: "P7 delegated, then read; P9 interleaved throughout".

## 23 · 30:50 · Human-agent mutual awareness in the future (my take) — **Published**
- File: `23-30m50-human-agent-mutual-awareness-in-the-future.png` · [30:50](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=1850s)
- My take: real-time fine-grained agent activity is rarely needed for coordination, because human and agent speeds are too different and agents are always available, unlike humans; "live" agent identifiers are usually overkill. Future work: agents will always be running in the background with cross-app awareness of user behavior; how should agents adjust to user activity; what agent indicators support peripheral awareness; how to rethink notifications about agent work. Sketches: three agent cursors plus "You" in a document; a status list (You: focus mode, writing the intro, back at 3pm; Agent 1: done, waiting for your review; Agent 2: waiting for you to pick key papers; Agent 3: checking citations…).

## 24 · 36:10 · The sociotechnical gap
- File: `24-36m10-the-sociotechnical-gap.png` · [36:10](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2170s)
- Ackerman's definition; social life is fluid, systems need explicit, rigid representations; "the central intellectual challenge of CSCW"; can only be reduced, never fully closed. Example: who gets my home phone number (colleagues share, students hide, except a prized honors student, share) against a technical encoding with fixed roles. Reference: Ackerman (2000), Human–Computer Interaction. **Not published:** spoken, example included.

## 25 · 37:02 · How do we design with the gap in mind?
- File: `25-37m02-how-do-we-design-with-the-gap-in-mind.png` · [37:02](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2222s)
- Design first-order approximations (tractable, partial solutions with known trade-offs; e.g., a set of fixed privacy roles). Keep a back channel / manual fallback (e.g., a specific permission outside one's role). Incremental formalization (e.g., unstructured notes before asserting a schema). References: Ackerman (2000); Shipman & Marshall (1999), Formality Considered Harmful, CSCW journal. **Not published:** spoken.

## 26 · 37:54 · Mitigating the sociotechnical gap when aligning social agents — **Published**
- File: `26-37m54-mitigating-the-gap-continuous-alignment.png` · [37:54](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2274s)
- "Instead of alignment being a 1-time action, we need to build in continuous alignment loops." 1 Start with a first-order approximation that bootstraps agent behavior. Loop: 2 Agent is embedded and acting in the social environment; 3 a monitoring system notices a gap, or lets users point to one; 4 agent addresses the gap and adjusts its behavior; 5 over time, the gap widens as social preferences or the technical encoding changes (arrow back to 2).

## 27 · 38:06 · Compass title
- File: `27-38m06-compass-title.png` · [38:06](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2286s)
- "System · 03 Social. Compass: Continuously Aligning Social Media Feeds via In-Situ Reflections · UIST 2026." Surnames: Barua (UT Austin, starred), Wang, Amy X. Zhang (University of Washington). **Not published:** title card.

## 28 · 39:16 · Compass: the problem
- File: `28-39m16-compass-the-problem.png` · [39:16](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2356s)
- A post by Sam Altman (@sama), 27 Dec 2024: "algorithmic feeds are the first at-scale misaligned AIs". The problem: feeds optimize for immediate impulses, not what people would have wanted upon reflection. Explicit controls help, but: they assume reflective preferences are known and statable on demand; preferences evolve and the feed drifts back; control UIs are cumbersome. "How can we continuously align a feed without overburdening the user?" **Not published:** spoken.

## 29 · 41:32 · Compass's continuous alignment loop
- File: `29-41m32-compasss-continuous-alignment-loop.png` · [41:32](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2492s)
- 1 First-order approximation: the platform's behavior-based feed algorithm plus an initially empty list of preferences in natural language. 2 Agent monitors user behavior while scrolling. 3 User inputs reflective preferences (in-situ suggestions from behavior such as video skips, or volunteered). 4 Agent re-aligns the feed (DOM edits + simulated behavior). 5 Over time the gap widens; the agent notices drift between stated and behavior and asks whether to update. **Not published:** the generic loop (26) is published, and this instance is spoken at 39:46–41:30.

## 30 · 42:04 · PaperPing title
- File: `30-42m04-paperping-title-chi-2025.png` · [42:04](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2524s)
- "System · 03 Social. PaperPing. Social-RAG: Retrieving from Group Interactions to Socially Ground AI Generation · CHI 2025." Surnames: Wang, Zhou, Qiu (University of Washington), Chang, Bragg (Allen Institute for AI), Amy X. Zhang. Slide counter 46/55. **Not published:** title card. (First cut labelled as the Compass field study; renamed after viewing.)

## 30a · 41:58 · Compass: field study — **Published**
- File: `30a-41m58-compass-field-study.png` · [41:58](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2518s)
- 10 days · n=15 · Compass vs. manual alignment. Improved alignment, with no cost to system usability; using social media was still fun; without Compass's in-situ suggestions, few people bothered to refine their preferences once entered. Session timelines over five sessions: Compass users C2 and C6 keep refining; baseline users B1 and B4 rarely refine. Legend: preference created, refinement, deleted, manual alignment, like/dislike video, notification interaction, periodic update seen, watching videos.

## 31 · 42:48 · Agents lack social intelligence
- File: `31-42m48-agents-lack-social-intelligence-social-rag.png` · [42:48](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2568s)
- The problem: proactive agents in group chats can be irrelevant, badly timed, or intrusive. Can we learn social norms from the group? Social-RAG: retrieve norms and preferences from the group's chat history to ground the agent. **Not published:** spoken.

## 32 · 43:58 · PaperPing's continuous alignment loop
- File: `32-43m58-paperpings-continuous-alignment-loop.png` · [43:58](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2638s)
- 1 First-order approximation: collect prior conversations in the group chat into a database of preferences and norms. 2 Agent retrieves from it to align each recommendation with group norms, with an explanation grounded in the group (e.g., @-mentions of members likely to be interested). 3 Group reacts and replies while discussing the paper. 4 These signals update the database. Diagram: chat → social signals (emoji, links, …) → relevant item + social signals → LLM → agent post. **Not published:** spoken.

## 33 · 44:40 · PaperPing: field study — **Published**
- File: `33-44m40-paperping-field-study.png` · [44:40](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2680s)
- 18 Slack channels. Participants · 500+ researchers. Interviews · n=28. "11 of 18 channels kept on using it voluntarily for over a year (until we shut it down)!" "88% said it took little effort to integrate into the group." "One drawback we saw was that in quiet channels, it could crowd out human conversation."

## 34 · 45:30 · Sociotechnical gap in the future? (my take)
- File: `34-45m30-sociotechnical-gap-in-the-future.png` · [45:30](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2730s)
- My take: I agree with Ackerman that the gap will not fully go away; until we can 100% simulate people and society ("never??"), AI alignment will be a moving target. If so, continuous alignment strategies are needed wherever agents interface with or reflect society. Ongoing and future work: how to align an LLM chatbot used by millions of people? **Not published:** spoken almost word for word.

## 35 · 46:28 · Taking a step back: aligning AI at scale is a governance problem
- File: `35-46m28-aligning-ai-at-scale-is-a-governance-problem.png` · [46:28](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2788s)
- "04 · Conclusion: From organizations → institutions." CSCW's ties to social-science studies of institutions: Organizations (how we work together productively; most of the work cited so far), Communities (how we gather socially; e.g., Elinor Ostrom), and, for technologies at scale such as social media and LLMs, Governments (how we make decisions about how to live together). **Not published:** spoken; the slide title is quoted on the source page.

## 36 · 48:32 · Example: case law as inspiration for AI alignment — **Published**
- File: `36-48m32-case-law-as-inspiration-for-ai-alignment.png` · [48:32](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2912s)
- The problem: constitutions are underspecified; edge cases cannot all be enumerated; time changes judgments and conditions. From law: case law decides new cases by grounding to past ones; a continuous alignment loop where precedents are set, relitigated and overturned; a "living constitution". How the lab used this: in-context learning and RLAIF experiments showing examples improve alignment over principles (1, ongoing); metrics for case retrieval beyond semantic similarity (2); benchmarking models on reasoning from precedent (ongoing); community AI bots aligned to a community (3); cases to help domain experts reason about model behavior (4, 5). References: 1 Chen & Zhang (2025), Case Law Grounding, Collective Intelligence; 2 Chen, Feng, Park & Zhang (2025), SPICA, Findings of ACL; 3 Kuo et al. (2026), Botender, CHI; 4 Feng et al. (2023), Case Repositories, NeurIPS MP2 Workshop; 5 Feng et al. (2026), PolicyPad, CHI.

## 37 · 49:54 · Other examples, and principles from institutions — **Published**
- File: `37-49m54-other-examples-principles-from-institutions.png` · [49:54](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=2994s)
- Jury Learning, Digital Juries ← offline juries; Collective Constitutional AI ← citizen assemblies; PolicyKit, MLSGov ← federalism, "laboratories of democracy"; online reporting systems ← inquisitorial vs. adversarial judicial systems. Principles that inform evaluation metrics: procedural justice (is the decision process transparent, fair, consistent?); legitimacy (do people accept outcomes they disagree with?); subsidiarity (is each decision made at the most local level possible?); plurality (room for multiple perspectives and values?); democracy (can the people impacted give input?). References: Gordon et al. (2022) CHI; Fan & Zhang (2020) CHI; Huang et al. (2024) FAccT; Zhang, Hugh & Bernstein (2020) UIST; Namavari et al. (2024) IEEE S&P; Wang, Wu, Que, Tyagi & Zhang (2025) arXiv.

## 38 · 51:14 · Towards sociotechnical institutional design? — **Published**
- File: `38-51m14-towards-sociotechnical-institutional-design.png` · [51:14](https://www.youtube.com/watch?v=e1VYwgm9-_s&t=3074s)
- "Instead of taking the technology as a given, research on offline institutions can provide lessons and inspiration for how to reimagine online sociotechnical institutions." We should do more of this; CSCW provides a blueprint: Ostrom's principles from *Governing the Commons* were generative for online peer production and community moderation, though her work was on farmers and villagers. Not everything applies: take the pattern or spirit, not always the details; existing institutions have their problems. Close the loop: build prototypes, deploy, evaluate. Online affords more opportunity to iterate than offline; new forms of institutions and new theories can be built from the offline starting point.
