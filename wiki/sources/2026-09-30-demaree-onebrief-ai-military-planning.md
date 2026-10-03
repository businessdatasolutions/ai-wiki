---
type: source
kind: video
title: "Onebrief: Simulation as the Missing Error Signal for AI Military Planning, and a Reported 45x from Going Agentic"
author: ["YC Root Access"]
publisher: "YC Root Access (YouTube livestream), The Startup Industrial Base: Building for the Next 250, Washington, D.C.; chapter 2:34:40–2:51:18; Grant Demaree (CEO, Onebrief; YC Summer 2021; former US Army officer)"
url: "https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9280s"
date_published: 2026-09-30
date_ingested: 2026-10-03
length: "~15:59 minutes (chapter 2:34:40–2:51:18 of an 8:01:10 livestream; ~390 ASR segments + 9 stills, quotes lightly corrected)"
raw: "../../raw/videos/the-startup-industrial-base-building-for-the-next-250-washington-dc.md"
stills: "../../raw/videos/the-startup-industrial-base-building-for-the-next-250-washington-dc.search-slides-diagrams-and-product-screens.stills.md"
tags: [yc-root-access, startup-industrial-base, onebrief, defense-software, military-planning, war-gaming, simulation, error-signal, verifiability, after-action-review, agentic-development, feature-delivery, devsecops, task-horizons, self-reported-productivity]
dynamic_capabilities:
  - digital-sensing/digital-scenario-planning
  - digital-transforming/improving-digital-maturity
  - contextual/external-triggers
relationships:
  - type: part-of
    target: 2026-09-30-yc-root-access-startup-industrial-base-dc
    via: "Chapter 2:34:40-2:51:18, a founder talk in the morning block: a live demo of Onebrief followed by four minutes of reflections on defense software"
  - type: supports
    target: 2026-03-11-allen-mcdonald-how-well-can-ai-do-strategy-simulation-benchmark
    via: "Both use a simulation to judge AI decisions in a multiperiod setting with delayed feedback. Allen and McDonald score 34 LLMs on the Back Bay Battery business simulation against MBA students and report the results; this talk demos AI-generated military plans played out in a planet-scale physics-based war game, with the after-action review fed back into the plan, and reports no results."
    confidence: 0.7
  - type: supports
    target: 2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering
    via: "Both tie AI's progress in software to a verification signal. Karpathy says LLMs automate what you can verify and that founders can build their own RL environments where the labs are not; this talk says military operations lack the fast error signal that code has and proposes a war-game simulation to supply it, described as a loop for revising plans, without saying whether models are trained on it."
    confidence: 0.7
  - type: supports
    target: 2026-09-25-charles-lennys-podcast-what-product-looks-like-when-coding-is-solved
    via: "Both describe the constraint moving once agents speed up software delivery. Charles walks Ramp's product cycle and names the internal agent built at each new bottleneck; this talk names one blocker Onebrief hit, a DevSecOps pipeline that breaks under 180,000-line pull requests, after a reported 45x rise in feature delivery."
    confidence: 0.75
  - type: supports
    target: 2026-08-06-garry-tan-own-your-intelligence
    via: "Both report a large multiple from agentic software development, from inside one organisation and without a published method. Tan gives about 400x his own 2013 output in lines of code, discounted on stage to an 8x floor; this talk gives about 45x in the rate of feature delivery to customers across Onebrief's best teams from January 2026, described as measured."
    confidence: 0.65
---

# Onebrief: Simulation as the Missing Error Signal for AI Military Planning, and a Reported 45x from Going Agentic

> The defense industrial base of the future will be built by small, fast-moving teams working on some of the hardest problems in national security.
>
> Live from Washington, D.C., Y Combinator brings together founders, senior government officials, and military leaders for a day of conversations about rebuilding America's defense industrial base, working with the government, and closing critical capability gaps across autonomy, munitions, space, secure communications, manufacturing, and more.
>
> *— Channel description, [[Y Combinator|YC Root Access]] (event description; this page covers one chapter)*

**Grant Demaree**, CEO of **Onebrief**, gives a 16-minute talk in the morning block of YC Root Access's day on the defense industrial base (see [[2026-09-30-yc-root-access-startup-industrial-base-dc|the event page]]). Onebrief sells planning software to military headquarters, covering the work from *"receipt of mission until roughly the issuance of their order."* Demaree went through YC's Summer 2021 batch. Before that he was a US Army officer: a second lieutenant in the 101st during the Ebola epidemic, attached to the planning section (J5) of the joint task force in Liberia, and later on task forces in Baghdad for the counter-ISIS mission. The talk has two parts. The first is a live product demo. The second is a few minutes of "defense software reflections" for people who buy or build it.

It earns its own page for two AI claims the wiki can use. The first is an argument about **why AI got good at software and what it would take elsewhere**. Software has a fast feedback loop that tells you whether code is good. Military operations have no such error signal, and Onebrief proposes to supply one with a planet-scale war-game simulation. The second is a figure from Onebrief's own engineering: **about 45x in the rate of feature delivery to customers** across its best teams since January 2026, after the company went agentic, followed by the next blocker it hit. The defense context (the Army's NGC2 programme, procurement reform, defense-startup revenue growth) appears below only where it bears on these two claims.

## TL;DR

- **Planning is the lever because it drives decisions.** From his Army posts Demaree concluded that *"planning drives almost every major military decision. So fixing planning isn't really about fixing planning. It's about fixing decisions"* ([2:36:41](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9401s)). His second conclusion: *"the status quo is nowhere near the frontier of what's possible."*
- **The product is one connected staff workspace that AI can operate.** An edit to the sync matrix (*"basically a militarized Gantt chart"*) or the map flows through to the slides and the operations order. Integrations such as Maven Smart System are set up by drag and drop, so that someone on a military staff *"can just do this sort of thing without an engineer present"* ([2:39:52](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9592s)). Approval routing produces the comment-resolution matrix automatically. Then: *"everything that a human can do is fully operable with AI"* ([2:41:55](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9715s)), because *"user interfaces are converging to interact directly with the LLM."*
- **The argument: superhuman needs an error signal, and simulation is the only source of one.** *"In order to get to truly superhuman, like we've seen in software engineering, what made that possible with AI was an error signal where you could tell is this code good or not through a fast feedback loop. That's generally missing in military operations. And our view is that the only way to get there is through simulation"* ([2:42:44](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9764s)).
- **The loop: generate a plan, war-game it, review, revise.** The simulation models *"a full planet"* down to individual vehicles, missile trajectories, radar cross-sections and terrain. The demo runs *"at 300x real time"* ([2:44:03](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9843s)), and Demaree says it scales *"to many hundreds of thousands of entities."* Put together: *"AI generate a plan, set up the war game, let the AIs play the AI, get an after-action review … and then use the after-action review to improve everything about your plan"* ([2:44:53](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9893s)), *"again and again until you've achieved true superhuman decisions"* ([2:35:53](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9353s)). The stills show the war game, an after-action review and a ranking of courses of action, not a plan being revised (see *Visual canon*). The demo does not show how much a plan improves.
- **A reported 45x from going agentic.** *"Transforming our own company into agentic was a huge bear. But it also works. We measured about a 45x increase in the rate of feature delivery to customers across our best teams from January of this year to present"* ([2:48:09](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=10089s)). And: *"I would not have said 45x would have been practically achieved"* ([2:48:27](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=10107s)). Nothing else is said about how it was measured (see *Debates*).
- **Each unblocked constraint reveals the next.** *"Each time you unblock something, you earn the right to find out what the next blocker is"* ([2:48:42](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=10122s)). His example: features *"are now delivered so fast that the DevSecOps pipeline basically breaks because you're shipping PRs that are, you know, 180,000 lines of code"* ([2:48:55](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=10135s)).
- **Expectations for buyers, stated conditionally.** *"If it's true that the task length that a frontier model can do, at least in software, is growing super exponentially and then the doubling time is actually getting less than 4 months, then our expectations of software over the next 6 months should just be stratospheric"* ([2:49:20](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=10160s)). On what superhuman command and control is worth: *"is it about as valuable as a 10% increase in your force structure or is the frontier of what's possible about as valuable as a 10x increase in force structure? I think it's closer to a 10x"* ([2:50:02](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=10202s)). He says he maintains his own estimate and asks government to evaluate the question independently.

## Visual canon

The stills are screens from the live product demo (2:35–2:51). A targeted search cut 19, and the nine below carry what the narration only points at; ten were dropped as near-duplicates, map views or transitional screens. Each entry was transcribed from the still and checked against it, and Gemini's reading was wrong where it mattered: it named COA 3 the recommended course of action (the screen recommends COA 1, and COA 3 has no review), invented a close-air-support form with aircraft counts and altitudes where the frame shows a squadron-and-weapon menu, missed a "Disconnected from server" dialog, misread DIVARTY as "SHAPITY" and two phase statuses, and garbled place and unit names throughout. The manifest has all 19.

### 1 · The sync matrix, and the scenario the demo runs

![[assets/2026-09-30-demaree-onebrief-ai-military-planning/04-158m11-operation-eagle-strike-force-flow-matrix.webp|Force Flow sync matrix for the exercise Operation Eagle Strike: enemy courses of action above friendly land, air and maritime deployments on one day grid]]

*Still at [2:38:11](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9491s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

**Force Flow** board in the plan *Operation Eagle Strike*, marked **EXERCISE**. Columns are days, with three header rows: calendar date (June 13 to July 5), ATO day codes (GH … HD) and relative days (−1 … +21). Key dates: **D-Day** at +0, **C-Day** at +6.

| Row | Cards legible in the still |
| --- | --- |
| EMLCOA (…) | Deploy SOF (Mactan) · PLA-Air Force Deployment, Clark to Mactan / to Palawan / to Cagayan · PLA-Army Coastal Defense Battery to Palawan |
| EMDCOA (…) | Deploy SOF (Negros) · 3rd Division Deployment to Negros · PLA-Air Force Deployment, Clark to Mactan / to Palawan / to Cagayan · PLA-Army Coastal De… (cut off) · PLA-Army Coastal Defense Battery to Palawan |
| Land Comp… | 1st Special Forces Group (-) · 5 SFAB (-) · 2/82 BCT (A) · 25 CAB · 25 DIVARTY · MP BN · 1st MDTF · I MEF (FWD) · 25 ID (-), selected, with an arrow to 2/25 IBCT · 25 Sustainment Brigade · 11 AD BDE · 3/25 IBCT (-) |
| Air Compon… | Strategic Airlift Squadron · 35th Fighter Wing · F-15, F-16 and F-35 Squadrons · Air Refueling Wing · Tactical Airlift Squadron |
| Maritime Co… | CTF-70 (CSG) · SEAL Platoon 2 · TF-72 (Patrol, Reconnaissance, Logistics) · attack submarine · C-130 and C-17 movements to Gen. Santos, Zamboanga and Lumbia Airfield · 1x CONSOL Carrier to West… |

*Still vs. transcript:* the narration calls this *"a sync matrix … basically a militarized Gantt chart. Who does what and when"* and says a change flows to everything that depends on it. The still adds the layout and the scenario. The enemy's courses of action sit on the same day grid as the friendly component deployments; the row labels are cut off, and in staff usage EMLCOA and EMDCOA are the enemy's most likely and most dangerous courses of action. The scenario, which the talk never names, is an exercise set in the Philippines (Mactan, Negros, Palawan, Cagayan). Demaree's spoken examples are Taiwan and Ukraine.

### 2 · An integration as a field mapping

![[assets/2026-09-30-demaree-onebrief-ai-military-planning/09-160m10-foundry-connection-alpha-interactive-field-mapping-modal.webp|Connection mapping editor wiring Onebrief List and Card objects field by field to Foundry objects, with one link switched to inbound]]

*Still at [2:40:10](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9610s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

**Foundry Connection Alpha / Mappings (3)** · Plan ID: 15995 · *Unsaved changes*. Buttons **+ Onebrief object** (blue) and **+ Foundry object** (orange). Two banners: *"This mapping has previous unsaved edits, would you like to restore? Saved 9/30/2026, 9:33:31 AM"* and *"This change will permanently remove 1 mapping — confirm you understand before saving."*, with the button **I understand, proceed with saving**.

- Left, blue headers: **List** (filter: All 193 lists; Primary Key, Title, Color, Card Count, Created At, Updated At, Card) and **Card** (All 757 cards; fields from Primary Key and Classification to Unit Rank, plus graphic fields Geometry, Position, SIDC, Symbol Anchor Points).
- Right, orange headers: **List**, **Card To List Link** and **Card** (uuid, Classification, created_at, geospatial_symbol_anchor, plan_id, SIDC, text, updated_at, version), each with Create / Edit / Delete actions.
- Open on one link: **node_count → cardCount** · *value set by OB* · **Outbound | Bidirectional | Inbound**, with Inbound selected · *Remove*.

*Still vs. transcript:* the narration calls this *"integration with Maven Smart System"* and changes a mapping *"from bidirectional to one way"*. On screen the connection is labelled a **Foundry** connection, and the integration is a field-by-field mapping between Onebrief's list and card objects and Foundry objects, each link with its own direction. The editor also warns that saving will permanently remove one mapping.

### 3 · A warning order that cites the plan

![[assets/2026-09-30-demaree-onebrief-ai-military-planning/10-160m16-warning-order-001-document-view.webp|Opening page of Warning Order 001 to Operation Eagle Strike in a coordination packet]]

*Still at [2:40:16](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9616s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

> EXERCISE
>
> WARNING ORDER 001 TO OPERATION EAGLE STRIKE
>
> Issuing Headquarters: I CORPS (JTF EAGLE). · Place of Issue: Not provided in available source material. · Date-Time Group of Signature: 301640ZSEP26. · MRN: JTF-EAGLE-WARNORD-001.
>
> References: USINDOPACOM WARNORD 001 to OPERATION EAGLE STRIKE; JFC COMREL; Force Flow; Chief of Staff Planning Guidance.
>
> Task Organization: Use JFC COMREL as the baseline. INDOPACOM has COCOM of I CORPS (JTF EAGLE). 1st MDTF is direct support to I CORPS (JTF EAGLE). CTF-70 (JFMCC) is TACON to I CORPS (JTF EAGLE). 1st SFG(A) (CJSOTF-P) is OPCON to I CORPS (JTF EAGLE). 35th Fighter Wing (JACCE) is TACON to I CORPS (JTF EAGLE). 25th ID (TJFLCC) is OPCON to I CORPS (JTF EAGLE).
>
> 1.A. Enemy Forces. Available force-flow data identifies enemy SOF deployments to Mactan and Negros at C-Day to conduct reconnaissance and disruption operations against critical lodgment points. It also identifies enemy air and air-defense deployments: MiG-29 and SA-10 to Mactan at C+5, MiG-23 to Palawan at C+6, SA-11 to Cagayan at C+6, KH-35 coastal defense to Palawan at C+10, and 3rd Division deployment to Negros at C+4.
>
> 1.B. Friendly Forces. Force flow builds JTF combat power through land, air, and maritime arrivals from D-Day through D+16, including 2/82 IBCT, 25 ID elements, I MEF (FWD), CTF-70, TF-76, 35th Fighter Wing/JACCE, 1st MDTF, and 1st SFG(A) … *(cut off at the page edge)*

Side panel: stage *Coordination open*; *Comment resolution matrix*; *Coordination*; *Formal approval*.

*Still vs. transcript:* the narration says only that this is *"a warning order that came out of this plan."* The page shows the link. It lists the command-relationships board and the force-flow matrix among its references, and its task organization restates the command relationships drawn in still 4. Its enemy paragraph cites "available force-flow data", and a field with no source is marked "Not provided in available source material" rather than filled in. Nothing on screen or in the narration says whether staff or the AI wrote this text.

### 4 · The prompt behind an AI-built warning order

![[assets/2026-09-30-demaree-onebrief-ai-military-planning/13-162m27-jpc-commel-diagram-with-ai-copilot-assistant.webp|Onebrief AI panel beside the JFC COMREL command-relationships diagram, showing a prompt for WARNORD 001 and the agent's first steps]]

*Still at [2:42:27](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9747s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

Left, the **JFC COMREL** board: a command-relationships diagram running SECDEF → Joint Staff → INDOPACOM, with TRANSCOM and SOCOM joined to INDOPACOM by dashed arrows. Below INDOPACOM: USARPAC, PACFLT, MARFORPAC, PACAF, SOCPAC, SPACEFORPAC and 1st MDTF; further down 7th Fleet, I MEF, I CORPS (JTF EAGLE), CTF-70 (JFMCC), 1st SFG (A), 35th Fighter Wing (JACCE), 25th ID and I MEF (FWD). Legend: COCOM, OPCON, TACON, Direct Support, Supporting, Coordinating, Organic, TYCOM. Some unit subtitles are illegible.

Right, the AI panel **Joint Task Force Warning Order Developm…** (title cut off), with the user's prompt:

> I want to create a new document called WARNORD 001 to OPERATION EAGLE STRIKE. This is the JTF level WARNORD. Note that a USINDOPACOM level WARNORD already exists; and you should use that as a source
>
> Be sure to include specific preliminary tasks to each of the subordinate units. Create a new section called "WARNORD 001." Inside of it, create a list board with the various lists that are reasonable elements of WARNORD 001. Once you're done writing those, assemble them into a properly formatted new document, WARNORD 001.
>
> Be sure to fix the numbering in your doc. A common mistake is that there's way too many base level paragraphs in your warnord doc, and that obscures the numbering of (1) situation, (2) mission, etc

Steps so far: ✓ Ran retrieve · Inspected the section schema · Inspected the list schema · Inspected the board schema · Inspected the card sch… (cut off). Footer: *Referencing this page · Searching entire plan*.

*Still vs. transcript:* the narration says *"everything that a human can do is fully operable with AI"* and that *"in a second you're going to see some analysis for our approval on the warning order one that this AI has created for us."* The still shows what was asked. The prompt is a multi-step instruction: build a list board, then a formatted order, using the higher-level order as a source, with a correction for a formatting error the author expects. The agent's log shows it reading the plan's schemas before it writes anything.

### 5 · The board the agent filled

![[assets/2026-09-30-demaree-onebrief-ai-military-planning/15-163m06-fresh-warnord-001-working-board-populated-kanban.webp|Fresh WARNORD 001 Working Board filled with situation, mission, subordinate-unit task and coordinating-instruction cards]]

*Still at [2:43:06](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9786s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

**Fresh WARNORD 001 Working Board**, four lists visible (a fifth is off-screen to the right), each *Updated just now*:

| Situation and Assumptions | Mission and Intent | Subordinate Unit Tasks | Coordinating Instructions |
| --- | --- | --- | --- |
| PRL seizure of resources and maritime disruption threaten ROM sovereignty and regional stability | JFC mission is to re-establish ROM control of sovereign territory while deterring adversarial opportunism across the theater | 25th ID / TJFLCC: secure General Santos force-flow nodes and prepare operations to restore control on Negros | JTF staff begins mission analysis and running estimates immediately upon receipt |
| USINDOPACOM establishes JTF Eagle with I Corps as the supported command for operations in the JOA | JTF Eagle will defeat LPA forces in the Visayas and Sulu Sea to restore ROM control and freedom of navigation | CTF-70 / JFMCC: re-establish freedom of navigation in the Sulu Sea and support JTF maritime maneuver | Initial information collection focuses on LPA SOF, air defense, coastal defense, and force movement indicators |
| | | I MEF (FWD): integrate with CTF-70 and TF-76 for amphibious operations and littoral maneuver | Risk guidance prioritizes lodgment force protection and minimizing collateral damage to local infrastructure |
| | | 1st SFG(A) / CJSOTF-P: maintain partner-force coordination and reconnaissance around Negros access points | |
| | | 35th Fighter Wing / JACCE: coordinate air support with 613th AOC and protect force-flow nodes | |
| | | 1st MDTF: prepare direct-support effects and target nominations for JTF operations | |

The AI panel on the right shows the same prompt as still 4.

*Still vs. transcript:* the narration says *"these cards are going to start to populate and we're going to see an audit trail for our approval."* The still shows the output: one task card per subordinate unit in the command-relationships diagram, plus situation, mission and coordinating-instruction cards. The scenario's parties appear only as abbreviations (PRL, ROM, LPA), not expanded on screen. The frame before (2:42:47, not published) shows the same board empty. In it the agent's log reports a section "WARNORD 001 Demo", five "Demo WARNORD" lists, a "Demo WARNORD 001 Working Board" and 19 cards whose titles differ from the cards here. The stills do not show which run produced this "Fresh" board, nor the assembled order the prompt asked for.

### 6 · Tasking a strike in the war game

![[assets/2026-09-30-demaree-onebrief-ai-military-planning/16-164m00-atomengine-air-support-configuration.webp|AtomEngine war game over the Arctic coast: a menu tasking a close air support mission to named squadrons and weapon loads]]

*Still at [2:44:00](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9840s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

**AtomEngine** (the earlier global view at 2:35:44 carries the mark *AtomEngine by Battle Road*), served from a onebrief.com address. Team **White**, **Day 1**, **Paused**; timeline *D+ 0d 11:05:00.000 · 2026-09-01 · x300.0*. The map shows the Arctic coast from northern Norway eastward, with no place names on screen. A menu is open on a unit:

- **Air Missions** › Air Assault · Air Strike Mission · **CAS Air mission** · DCA Air mission · ISR Mission · OCA Mission · Reassign Airbase
- **CAS Air mission** › F-18, VFA-2 Bounty Hunters · F-18, VFA-113 Stingers · F-18, VFA-136 Knighthawks · VAQ-130 Zappers · *greyed:* HSC-4 Black Knights, HSM-78 Raging Wasp, VRC-30 (Det. 1) Providers, E-2D VAW 113, F-35C VFA-97 120D · F-35C, VFA-97, GBU-31 · F-35C, VFA-9…, JASSM (partly under the cursor) · F-35C, VFA-97, JSM · F-35C, VFA-97, LRASM
- Rest of the first menu: Tactical Missions, Composition, Movements, Edit Entity, Clear commands, Debug, Logistics, Fire Missile Salvo (greyed), White Cell Actions

Entity details: **CVN-69 USS Dwight D. Eisenhower (1)**, ID 3562 · Combat Value CV: 3.0 · Operational Status 100.0%. Forces panel, Blue Team: **Forces Deployed 112681/31325**.

*Still vs. transcript:* the narration says *"I'm just going to briefly conduct a air strike"* and that the model covers *"every missile trajectory, every radar cross-section."* The menu shows how finely a strike is tasked: by named squadron and by weapon (GBU-31, JASSM, JSM, LRASM), from a carrier with a combat value and an operational status. The forces counter reads 112681/31325; the screen does not say what the two numbers count. The war game is set in the European Arctic, not in the Philippines exercise of stills 1–5.

### 7 · The war game at 300x, and a dropped connection

![[assets/2026-09-30-demaree-onebrief-ai-military-planning/17-164m46-atomengine-active-combat-simulation-view.webp|AtomEngine war game set to 300x with a Disconnected from server dialog over the map]]

*Still at [2:44:46](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9886s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

Clock indicator **Day 1 ▶ 300.0X**; timeline *D+ 0d 11:59:50.000 · 2026-09-01 · x300.0*. Units and sensor rings on the map, among them a ship labelled *AN/SPQ-9 Radar, RIM-162 ESSM*. Same entity and forces panels as still 6. In the centre:

> Disconnected from server
>
> Try reconnect · ProjectBrowser · Download server logs

*Still vs. transcript:* the narration says *"This is running at uh 300x real time"*, and the indicator shows that setting. The narration does not mention the dialog. This is the last frame of its display window; the stills do not show how long the disconnection lasted, or the strike's outcome. The next still (2:44:58) is back in the planning application.

### 8 · Ranking courses of action from after-action reviews

![[assets/2026-09-30-demaree-onebrief-ai-military-planning/18-164m58-course-of-action-analysis-summary.webp|Course of Action Analysis comparing three courses of action on mission, effects on enemy, risk to force and tempo, with COA 1 recommended]]

*Still at [2:44:58](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=9898s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

**COA Comparison · Course of Action Analysis** (banner: *Unclassified – classification markings for illustration purposes only*).

- **Recommended COA:** COA 1: Central Penetration. *"Lowest weighted total across AAR-derived criteria. Treat as staff evidence for commander dialogue, not an automatic decision."*
- **Evidence:** 8 AARs / 8 runs. *"Only completed, COA-linked runs are scored."*
- **Scoring, recommendation basis:** *"Only AAR-backed values shared by at least two COAs receive ranks."*

| Criterion | COA 1: Central Penetration (recommended; last run Sep 24, 2026, 1:36 AM) | COA 2: Western Envelopment (last run Sep 30, 2026, 11:29 AM) | COA 3: Double Envelopment |
| --- | --- | --- | --- |
| Mission | 5/5 tasks complete · Rank 1, Score 3 | 1/6 tasks complete · Rank 2, Score 6 | — |
| Effects on Enemy | 1.58:1 LER; 38.0 red units lost on average · Rank 2, Score 4 | 4.56:1 LER; 10.0 red units lost on average · Rank 1, Score 2 | — |
| Risk to Force | 24.0 blue losses: "Blue lost 24 of ~961 systems (~2.5%) … Aggregate combat power ~86% of starting strength" · Rank 2, Score 4 | 1.3 blue losses: "Blue lost 9 of ~961 systems (~1%) … Aggregate combat power ~95% of starting strength" · Rank 1, Score 2 | — |
| Tempo | 3/4 phases on sequence; 88% sequence adherence | 7/24 phases on sequence; 40% sequence adherence | — |

The Tempo ranks are below the fold. Each COA's mission row lists its tasks with a status dot. COA 3 offers *Setup Wargame*, but its *View AAR* is greyed out.

*Still vs. transcript:* the narration goes from *"get an after-action review"* straight to *"use the after-action review to improve everything about your plan."* This screen sits between the two and is never described. It scores four criteria, gives a rank and a score per criterion, and recommends by lowest weighted total, with the caveat that the result is evidence for the commander, not a decision. The ranks split: COA 2 ranks first on effects on enemy and risk to force, COA 1 on mission and overall. The weights are not shown. The report list in still 9 shows the evidence base: seven reports for COA 2, one for COA 1. The same screen opens the talk at 2:35:41 (not published).

### 9 · The after-action review: plan against actual, phase by phase

![[assets/2026-09-30-demaree-onebrief-ai-military-planning/19-170m43-coa-2-western-envelopment-scheme-of-maneuver-detailed-aar.webp|After-action report for COA 2 Western Envelopment setting planned against actual outcomes per phase, beside the list of eight reports]]

*Still at [2:50:43](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=10243s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

Per the manifest, the screen is up from 2:45:00 (*"get an after-action review … shown here"*) to the end of the talk; the same report is previewed at 2:36:00 (not published).

Left, **After-action reports**: COA 2: Western Envelopment, Sep 30, 2026 at 11:28 AM, 11:17 AM, 11:10 AM, 9:23 AM, 8:56 AM and 8:27 AM, and Sep 24, 2026, 1:36 AM; COA 1: Central Penetration, Sep 24, 2026, 1:36 AM.

Summary (first line cut off): *"… envelopment's critical preconditions (DP 2 fires threshold, 1st BCT's flank assault) are unconfirmed or unexecuted. The operation is in-progress and not yet failed, but it is at a sequencing inflection point — if DP 2 cannot be confirmed and the assault does not close on OBJ HAMMER, the envelopment will culminate short of its objective exactly as the plan's primary risk identified. Immediate action is required to confirm shaping effectiveness and commit the main effort before enemy defensive coherence hardens or the mobile reserve repositions."*

**Scheme of Maneuver — Plan vs. Actual**

| Phase | Status | Planned | Actual |
| --- | --- | --- | --- |
| I — DIVARTY Shaping Campaign (H-72:00 – H+00:00) | PARTIAL | DIVARTY conducts 72-hour fires campaign to degrade OBJ ANVIL to 50% threshold (DP 2 go/no-go), suppress enemy ADA and C2 nodes, and set conditions for the assault. DP 2 must be met before H-Hour commit. | No battle damage is recorded against OBJ ANVIL or any enemy formation. Zero enemy losses reported. DP 2 status (50% degradation threshold) cannot be confirmed as met or failed from available data. |
| II — Line of Departure Crossing and Envelopment Initiation (H+00:00 – H+XX:XX) | PARTIAL | At H-Hour, 1st BCT crosses LD along AXIS SABER moving north on the western flank. 2nd BCT demonstrates against the central obstacle belt. Division Cavalry Squadron screens forward. Combat Aviation Brigade establishes eastern flank guard. Engineer Brigade provides mobility along AXIS SABER. | No maneuver engagement data exists. Zero blue or red losses recorded. The operation is assessed in-progress, meaning H-Hour may have been executed but decisive contact has not been established or reported. |
| III — OBJ HAMMER Assault (H+XX:XX – H+XX:XX) | OFF SEQUENCE | 1st BCT turns east onto OBJ HAMMER, strikes the forward battalion in flank and rear. DIVARTY weights fires west and northwest onto OBJ HAMMER. Combat Aviation Brigade attack aviation augments the assault. DP 1 decision: if forward battalion is collapsing, commit 3rd BCT to exploit north. | HPTL destruction (enemy forward battalion and mobile reserve) scored 0/1 — not met. No engagement BDA recorded. OBJ HAMMER has not been taken. |
| IV — OBJ DEPTH Exploitation (H+XX:XX – H+XX:XX) | OFF SEQUENCE | *(below the fold)* | *(below the fold)* |

Each phase also carries an **Assessment**. Phase III: *"The decisive phase has not executed or has not produced the required effect. The forward battalion at OBJ HAMMER remains intact (0 red losses). This is the critical gap in mission accomplishment — the battle has not reached the culminating point of the envelopment."*

*Still vs. transcript:* the narration names the after-action review and says it is used to improve the plan. The still shows its form: the plan's own phases, decision points and objectives set against what the war game recorded, with a status and a written assessment per phase. In this report the war game recorded no engagement (zero losses on either side), and the assessment says the outcome cannot be confirmed instead of scoring one. The reports are timestamped Sep 24 and Sep 30, 2026. The stills show neither a report produced from the air strike flown on stage nor a revised plan.

## Why this matters to the wiki

**1. A domain outside the verifiable circuits, and a founder's plan to build the check function.** [[jagged-frontier]] carries [[Andrej Karpathy]]'s mechanism from [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Sequoia AI Ascent 2026]]: LLMs automate what you can verify, models peak where labs have built verification into training, and a founder outside those domains can build their own environment. The Karpathy source page lists a startup actually doing this as something the wiki has not yet seen. Demaree applies the same reasoning to military planning. The fast *"is this code good or not"* signal is what made AI strong in software. Military operations lack it, and simulation is *"the only way to get there."* Two limits. The talk presents the simulator as a loop for revising plans and does not say whether models are trained or fine-tuned on it. And it reports no measurement of what the loop achieves.

**2. A simulation used two ways.** [[2026-03-11-allen-mcdonald-how-well-can-ai-do-strategy-simulation-benchmark|Allen and McDonald]] use a business simulation as a **benchmark**. They score LLM decisions over eight simulated years with delayed and noisy feedback, and report that mid-to-late-2025 frontier models fell below both earlier models and MBA students through an exploitation bias. Onebrief uses a military simulation as the **feedback** in a plan-improvement loop. In the paper, a program fed each model structured information and each run was scored once. In Onebrief's design, plans pass through the simulator repeatedly. Both treat a simulation as the way to judge decisions whose real outcomes come late or never. See [[strategy]] and [[ai-benchmarks]].

**3. A firm-level multiple from going agentic.** [[ai-coding-productivity-evidence]] keeps controlled studies apart from practitioner self-report. It notes that no RCT in the corpus measures agent fleets, and it records [[2026-08-06-garry-tan-own-your-intelligence|Tan's Startup School keynote]] (about 400x his 2013 output in lines of code, discounted on stage to an 8x floor) as self-report. Demaree's 45x is the same kind of evidence from one company, but with a different metric: features delivered to customers rather than lines of code. He calls it measured. [[agentic-engineering]] has an open question on whether the "far more than 10×" ceiling holds under measurement. This figure bears on it, but the talk gives no method that would let it answer the question. Details are in *Debates*.

**4. The bottleneck moves to the delivery pipeline.** [[agentic-pull-requests]] records review capacity, not authoring, becoming the constraint once agents write the code. [[2026-09-25-charles-lennys-podcast-what-product-looks-like-when-coding-is-solved|Charles (Ramp CPO)]] describes the same movement as a chain of bottlenecks, each removed by a new internal agent. Demaree states the same rule (*"each time you unblock something, you earn the right to find out what the next blocker is"*) and gives one link in the chain: the DevSecOps pipeline breaking under 180,000-line pull requests. [[2026-05-11-nystrom-how-i-ai-spec-driven-development-notion|Nystrom and Vo]] make CI *speed* the ceiling on agent PR throughput; here the pipeline broke on PR *size*. He does not say how those pull requests are reviewed or how the pipeline was fixed (*"you solve that and I expect that there's a next problem"*).

**5. The pace of model capability as a trigger for buyers.** Demaree tells government to expect *"stratospheric"* software within six months, conditional on task length doubling in under four months. The measure he refers to is the task-horizon measure introduced by [[METR]] (he does not name a source). The wiki's [[ai-benchmarks]] page records task-horizon levels for one model, not a doubling time, so the premise cannot be checked against the corpus.

**Dynamic capabilities.** **`digital-sensing/digital-scenario-planning`**: Onebrief's product interprets possible futures before commitment: AI drafts a plan, a simulated war game plays it out, and the after-action review shapes the next version. It is a digital instrument for testing options against scenarios, at scales from defending Taiwan to *"what do we do tomorrow in Ukraine."* **`digital-transforming/improving-digital-maturity`**: Onebrief's own move to agentic development (*"a huge bear"*) is a firm raising its digital working practice, and the talk shows the follow-on work that requires. Each gain exposes a new limit, the delivery pipeline first. **`contextual/external-triggers`**: the talk treats AI progress as the outside force changing defense software. Progress in the last year is a *"discontinuity"*, *"part of that is that AI got good"*, and the task-length trend should raise buyers' expectations.

## Linked entities and concepts

- **Entities**: [[Y Combinator]] (host of YC Root Access; Demaree's own batch, Summer 2021), [[Andrej Karpathy]] (not named in the talk; his verifiability argument is the comparison in point 1), [[METR]] (not named in the talk; the task-length measure Demaree cites is the one METR introduced).
- **Sources**: [[2026-09-30-yc-root-access-startup-industrial-base-dc|the event page]], [[2026-03-11-allen-mcdonald-how-well-can-ai-do-strategy-simulation-benchmark|Allen & McDonald 2026]], [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy / Sequoia AI Ascent 2026]], [[2026-09-25-charles-lennys-podcast-what-product-looks-like-when-coding-is-solved|Charles / Lenny's Podcast 2026]], [[2026-08-06-garry-tan-own-your-intelligence|Tan / Startup School 2026]], and, without a typed edge, [[2026-05-11-nystrom-how-i-ai-spec-driven-development-notion|Nystrom & Vo 2026]] (CI speed as the ceiling), [[2026-04-13-branco-lgtm-auto-merged-llm-agentic-prs|Branco et al. 2026]] (which agentic PRs get auto-merged), [[2025-07-10-becker-metr-early-2025-ai-experienced-developer-productivity|METR 2025]] and [[2026-02-27-cui-demirer-generative-ai-high-skilled-work-three-field-experiments|Cui et al. 2026]] (the controlled studies the 45x sits beside).
- **Concepts**: [[jagged-frontier]] (verifiability, and building the check function where labs are not), [[ai-coding-productivity-evidence]] (the 45x as firm-level self-report), [[agentic-pull-requests]] (the pipeline as the next bottleneck), [[agentic-engineering]] (the "more than 10×" ceiling question), [[strategy]] and [[ai-benchmarks]] (simulation as instrument), [[reward-hacking]] (see *Debates*).
- **Dangling** (single-source mention, deferred): **Grant Demaree**, **Onebrief**, **Maven Smart System**, **NGA** (National Geospatial-Intelligence Agency), **NGC2** (the US Army's Next Generation Command and Control programme).

## Debates and supersession

- **What the 45x measures, and what is not said.** Spoken: *"about"* 45x; the metric is *"the rate of feature delivery to customers"*; the population is *"our best teams"*; the period is *"January of this year to present"*, about nine months up to the talk; the attributed cause is *"transforming our own company into agentic"*; the method is *"we measured"*. Not said: what counts as a feature or how features are sized; the January baseline; how many teams, and whether "best" was defined before or after the results; whether 45x compares the rate now with the rate in January or something cumulative; whether defects, rollbacks or customer use were tracked; and how the company's own changes were separated from the model releases of the same nine months. The narration does not refer to a slide for the number, and the stills search over the chapter found none: per its manifest, the after-action review screen stays up from 2:45:00 to the end of the talk. The number is a CEO's figure about his own company, given in a talk that is half product demo. In the wiki's controlled evidence, [[2025-07-10-becker-metr-early-2025-ai-experienced-developer-productivity|METR's RCT]] measured experienced developers 19% *slower* with early-2025 IDE tools, and [[2026-02-27-cui-demirer-generative-ai-high-skilled-work-three-field-experiments|Cui et al.]] measured +26% completed tasks with Copilot. Both predate agentic tooling. The 45x comes from a different design (one firm, before and after, selected teams) and a different tool generation, so the figures are not measurements of the same thing.
- **The 180,000-line pull request.** It is given as an example of the next blocker, not as a practice. The talk does not say whether such PRs are reviewed by people, split, or merged as they stand. [[2026-04-13-branco-lgtm-auto-merged-llm-agentic-prs|Branco et al.]] find that the agentic PRs auto-merged in public repositories are small and focused, so a 180,000-line PR belongs to a different regime from the one the population data describe.
- **"Superhuman" is the aim, not a result.** The demo shows parts of the loop: an AI agent building a warning-order board from a prompt, a war game, after-action reviews that set plan against actual phase by phase, and a ranking of courses of action on four criteria (see *Visual canon*). It does not show a plan being revised, how much plans improve, or any comparison with human staffs. *"Superhuman decisions"*, planning D-Day in *"seconds to minutes"* and *"decision dominance"* describe the vision. [[2026-03-11-allen-mcdonald-how-well-can-ai-do-strategy-simulation-benchmark|Allen and McDonald]] measured the newest frontier models regressing on a business strategy simulation. Their setting (single scored runs, structured inputs) differs from Onebrief's iterative loop, so neither result speaks directly to the other.
- **A simulator as verifier.** A war game can only score a plan on what it models. Demaree raises this himself: most simulations did not model commercial shipping in the Strait of Hormuz, so Onebrief's is built to be *"very very easy to add things."* The wiki's [[reward-hacking]] page records optimisers scoring well on the grader rather than the task. The talk does not discuss whether optimising plans against a simulator carries a similar risk.
- **The task-length premise is conditional and unsourced.** Demaree frames it with *"if it's true"* and cites no study. The wiki holds no doubling-time figure for task horizons, so the claim should not be quoted as his statement of fact.
- **Estimates and anecdotes.** The *"closer to a 10x"* force-structure estimate is his own, and he says so. The revenue anecdotes (defense software startups going *"from 0 to 12 million of ARR in one year"*, a friend going from 1 to 50) name no companies. The product claims (planet scale, *"300x real time"*, *"many hundreds of thousands of entities"*, the Maven Smart System integration, labelled a Foundry connection on screen) are the vendor's, shown in a live demo that stalled once on the integration step and, in one war-game frame, showed a "Disconnected from server" dialog (see *Visual canon*).

## What was actually ingested

The chapter 2:34:40–2:51:18 of the 8:01:10 livestream. The talk itself runs to 2:50:39, followed by applause and the stage changeover. Source text: 387 raw auto-caption (ASR) segments, not cleaned at acquire. Quotes were checked against the segments at the cited timestamps and corrected only lightly: ASR errors in names and terms (*Demaree* for "Demeury", *Onebrief* for "One Brief", *Y Combinator*, *agentic* for "a Gent", *DevSecOps*, *Gantt*, *Strait of Hormuz* for "straight of Hormuz"), plus fillers and repeated words removed. One phrase is left as transcribed because its meaning is unclear: *"let the AIs play the AI"* (2:44:56), which may mean AI playing against AI. Demaree's role (CEO), his YC batch and his Army background are as he states them in the talk. Nothing else about him or Onebrief was checked.

**The first half depends on the screen.** The narration points at the sync matrix, maps, the Maven integration mapping, the comment-resolution matrix, the AI-built cards, a simulated air strike and the after-action review (*"shown here"*, 2:45:03), and it pauses while these load. A targeted stills search over 2:34:35–2:50:44 cut 19 screens from this chapter; nine are published in *Visual canon*, each transcribed and checked against the pixels, and the rest of the page relies on them only where it points there. The reflections section (2:46:03 onward) does not refer to slides. Not checked: the 45x figure and its method, the ARR anecdotes, the NGC2 programme details, the simulation's capabilities, and any Onebrief material outside the talk.
