---
type: source
kind: video
title: "Building AI Agent Workflows to Automate Industrial Operations"
author: ["NVIDIA Omniverse"]
publisher: "NVIDIA Omniverse (YouTube channel), developer livestream; host Edmar, NVIDIA community manager; NVIDIA's Ashley (tech marketing), Max Bickley (Omniverse product), Ganesh Sivaraman (Omniverse strategic partnerships) and Shashi Bhushan (system software architect); guests Jeppe Sverdrup (head of the product team's research arm), Christopher Dyken (spatial intelligence lead) and Thanh Pham (Surface team) of Falkor, a Kongsberg company"
url: "https://www.youtube.com/watch?v=I4X91GKLgNk"
date_published: 2026-11-19
date_ingested: 2026-11-23
length: "~1:13:01 (transcript ~569 lines + 14 stills; auto-generated track, no chapters)"
raw: "../../raw/videos/building-ai-agent-workflows-to-automate-industrial-operations.md"
stills: "../../raw/videos/building-ai-agent-workflows-to-automate-industrial-operations.stills.md"
tags: [nvidia, nvidia-omniverse, omniverse-libraries, openusd, ovrtx, falkor, kongsberg, falkor-surface, falkor-platform, industrial-ai-agents, digital-twins, spatial-intelligence, spatial-reasoning, p-and-id, engineering-cad, point-clouds, laser-scans, as-built, semantic-mining, reasoners, mcp, multi-agent, result-validator, memory-manager, human-in-the-loop, agent-traces, energy, offshore-platform, gpt-6-astra, claude-opus-5-5, codex, microsoft-foundry, azure, rtx-pro-6000, blender, agent-skills, livestream, science-technology]
dynamic_capabilities:
  - digital-transforming/navigating-innovation-ecosystems
  - digital-seizing/rapid-prototyping
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-02-01-manditereza-ontology-driven-industrial-ai
    via: "both concern grounding industrial agents in a graph of asset identity and relationships drawn from fragmented plant systems: Manditereza's HiveMQ paper proposes an ontology-based semantic data layer under the agents; Falkor shows agents traversing its digital-twin graph through MCP servers, with each asset ID carried into the OpenUSD scene"
    confidence: 0.7
  - type: supports
    target: 2026-09-30-singh-botha-bloomberg-flow-engineering-ai-hardware-design
    via: "both concern agents that read engineering data spread across CAD and simulation tools: Flow's agents follow changes in CAD, simulation and Git to assess their impact on a hardware design; Falkor's agents read engineering CAD, P&IDs, data tables and laser scans to build and check a plant model"
    confidence: 0.6
  - type: supports
    target: 2026-11-23-google-cloud-tech-why-agent-demos-break-in-production
    via: "both separate the agent that does the work from one that reviews it: Google's engineers describe an independent reviewer agent in a fresh context window and objective checks before human review; Falkor's run has a result validator on a different model recount the task runner's claims blind before the human validates"
    confidence: 0.6
  - type: supports
    target: 2026-11-20-chase-langchain-future-of-agents
    via: "both concern a separate step that decides what an agent keeps between runs: Chase describes 'dreaming', a background process that reads earlier runs and notes and updates memory, and calls deciding what to remember the hard part; Falkor's memory manager agent condenses a run's findings so unrelated facts do not carry over to later runs"
    confidence: 0.55
---

# Sverdrup, Dyken and Pham (Falkor) on NVIDIA Omniverse — agents that build and check an industrial plant model

> How do you give AI agents the data and tools they need to understand the physical world?
>
> Join Falkor developers to explore how they connect frontier AI agents to specialized engineering data, including piping and instrumentation diagrams (P&ID), CAD models and point-cloud scans. See how agents use industrial tools, OpenUSD and NVIDIA Omniverse libraries, to transform industrial workflows.
>
> You'll learn how to:
> - Give AI agents access to specialized industrial tools and foundational data.
> - Enable agents to use engineering data to build and modify OpenUSD scenes.
> - Structure human-to-agent workflows with separate execution and validation steps for human review.
>
> Explore real-world industry use cases and how digital twins and AI agents can help engineering and operations teams anticipate issues, make informed decisions, and improve facility performance.
>
> *— Channel description, NVIDIA Omniverse*

## TL;DR

A 73-minute developer livestream on NVIDIA's Omniverse channel, held on 18 November 2026 (the date on Falkor's title slide) and published the next day. NVIDIA's community manager Edmar hosts. The first 15 minutes are NVIDIA's own update on its Omniverse libraries. Then three people from **Falkor**, a Kongsberg company that builds software and simulators for energy, processing, power and renewables, present their joint work with NVIDIA: frontier-model agents given access to a plant's engineering data and to Falkor's own engines through MCP servers. A 26-page deck carries five recorded demos and two replayed agent runs. **Auto-generated transcript**; names were fixed against the lower-thirds and slides (listed in the raw file's `notes:`).

What it adds to the wiki:

1. **A worked architecture for industrial agents.** A graph in Falkor Platform is the source of truth for asset identity and relationships. Engines that Falkor built over years (a CAD Import Engine *"since 2018"*, a Point Cloud Engine) are exposed to agents as **reasoners**: *"An engine is a machine. A reasoner is kind of a cockpit… The agent is kind of the pilot."* NVIDIA's Omniverse libraries render the resulting OpenUSD scene, and its ID image lets an agent go from a pixel back to the asset record.
2. **Five demos from engineering data to a decision**: lighting a plant from more than 6,000 fixtures found in its CAD; following one vessel across three P&IDs to a maintenance question; showing recorded and simulated readings on the equipment; building a plant model from drawings where no current CAD exists; and checking a model against a laser scan.
3. **A run with four agents and one human.** A run coordinator, a task runner, a result validator on a different model and a memory manager. The human steps in at three points: stating the intent, answering one question mid-run, and validating at the end. The workbench names the models: Claude opus-5-5, Codex gpt-6.2-astra and Claude sonnet-5-5.
4. **Speed claims.** A first version of the Semantic Reasoner in *"no more than three working days,"* and *"Astra was the first eye opener for us"* on spatial reasoning. Production use is the *aim* *"by March 2027"*; all data shown is neutral or open, not an operator's.

## NVIDIA's segment: libraries and skills for agents (4:14–15:30)

Ashley (NVIDIA tech marketing) and Max Bickley (Omniverse product team) present two releases. The second version of a Blender add-on now runs natively on Windows. It renders a Blender scene in an **OVRTX** viewport (ovrtx is NVIDIA's rendering library) by translating Blender's scene graph to USD and then sending only the changes. Ashley gave the plans her architect sent to her own agent with *"the Blender MCP"* and got a 3D model of her house to plan a renovation. The *"real-time viewer skills"* are agent skills that *"teach your agent how our libraries sort of interconnect and… build some of the glue code."* They cover boundary representations (USD BREP), section planes, stylised rendering, CFD and CAE results in Warp, XR hand tracking and OV Newton physics. Max's reason for the Blender route: *"if you've already taught your agent to use Blender, it now gets to take advantage… of our Omniverse libraries."*

Ganesh Sivaraman (Omniverse strategic partnerships) then frames Falkor's work. It rests on a *"strategic shift"* in which NVIDIA *"disaggregated all of the… core [Omniverse] capabilities into sets of libraries"* (ovstage, ovrtx, streaming), which Falkor, *"an energy focused ISV,"* has *"fully embraced"* over *"the last several months."* The *"[north star]"* for the industry is *"autonomous operations and autonomous system[s]."*

## Why a plant has to be machine-readable first (19:04–25:35)

Jeppe Sverdrup, who leads the research arm of Falkor's product team, starts from the plant: plants *"occupy physical space on an industrial scale and they operate for decades,"* and an engineer reads physics in their layout. *"So to help someone plan work in a plant, an agent need to understand what things are where they are in relation to one another and what happens over time."*

He follows an imaginary pump through the systems that describe it: a drawing, pressure readings, maintenance records, the vendor's performance curve, the contractor's design intent, what the operator installed. Today *"the engineer, the human does a lot of that joining in their head."* An agent has to *"discover those relationships as it works,"* and a specialist agent it hands work to *"needs to know which pump we mean, what we already checked, and what's still an assumption."* His answer is a starting point plus relationships to follow: *"an agent's working memory is small compared to a [plant]. It looks up a few pieces at a time… Contextualization ties the pieces together. So the agent… spends his memory on the work instead of guessing the structure."* Two slides condense this (stills 2 and 3).

## Engines, reasoners and the graph (25:35–29:08)

Falkor brings two things. The first is the graph in its digital-twin product: *"If an agent starts with a piece of equipment in the 3D model, its asset ID gives it a way back to the drawing, the operating data and the other equipment it connects to."* The second is its engines. The CAD Import Engine could already *"open a plant model, walk its hierarchy, inspect attributes… What's changed now recently was who could do the asking. We exposed those operations through MCP. In no more than three working days, we had the first version of what we now call the semantic reasoner."* Christopher Dyken, Falkor's spatial intelligence lead, says later that this was *"one of the motivations to actually start with the MCP server because I tried to kind of programmatically find this and it was quite complex and then huh let's try an agent on this and it worked really well."*

Three reasoners sit over the engines: as-built (what the laser scan captured), semantic (what the engineering data says an object is) and scene (the composed 3D scene, backed by Falkor's own engine and NVIDIA's libraries). *"The agent decide[s]… which reasoner to use next."* Shashi Bhushan (NVIDIA) adds that NVIDIA's role is *"technology enablement… we're not providing the end application."* The architecture slide (still 5) shows how the parts connect.

## Five demos (29:08–46:27)

1. **The plant becomes observable (29:08–33:43).** Every light in the render *"comes from a fixture documented in engineering CAD. There are more than 6,000 in this facility."* In what Falkor calls **semantic mining**, the agent reads the CAD hierarchy, attributes and free-text descriptions, and from those *"[derives] classification rules that engineers use[d] to write by hand."* The engine then applies the rules across the plant: bulb type sets colour, wattage sets intensity. Shashi names the problem it addresses: 3D twins usually lack real lighting, so builders *"throw in things like dome lights,"* which leaves artefacts that matter for robotics training. Jeppe credits the models: *"we use state-of-the-art models like GPT-6 Astra… we source it from Azure Foundry… that's a big step up for us in terms of spatial reasoning."*
2. **From a process drawing to a maintenance decision (33:43–36:54).** The agent starts from one suction scrubber and its process drawing, follows off-page connectors to further drawings, and checks *"16 connections… against the source data."* It then tests the room to withdraw a strainer cover: *"an assumed withdrawal length of… 0.8 m and the zone is clear,"* but at 1.2 m *"the railing will be in your way."* The planner's options appear in Falkor Surface. Ganesh, speaking from Microsoft Ignite, points to remote maintenance: the assets are *"thousands of miles away from subject matter experts."*
3. **Information on the geometry (36:56–38:16).** A simulated liquid level shown inside a vessel, recorded level history, motor power and speed, and simulated temperatures on three coolers. *"What ties all of this together is the asset ID,"* carried from the graph into OpenUSD; alongside the colour image, *"OVRTX produce[s] an ID image as well."*
4. **A plant without CAD (38:16–42:25).** Having no current CAD *"is quite [a] common scenario in the industry."* From a vessel symbol on a process drawing, a data table, an access drawing and the plot plan, the agent builds a model and *"continues to follow the process across six different drawings."* Christopher: a P&ID *"gives you the topology and the function"*; the data table gave the cooler's dimensions and the plot plan its place, but *"the route the pipe takes between those points, those are still an assumption."*
5. **Ground the model against reality (42:25–46:27).** The as-built reasoner fits cylinders to slices of a laser scan from a different platform, used *"for demonstration purposes."* Christopher: on a thin slice the radius matches *"within millimeters. But… on all the other points, match is not nearly as good,"* so the agent works back and forth between a detail and the whole scan until it *"ends up with a pretty good model,"* which is where he places trust. Asked whether the agents ever got it wrong, Jeppe says *"definitely yes,"* but the cases are from confidential operator data they cannot show. Operators who saw agent-built models asked first: *"how do we know it's right?"*

## Agent traces: four agents and one human (46:27–53:31)

Two real runs, *"recorded and sped up."* *"The agents run in Claude and Codex. And what we have added is a way to follow the work and inspect the evidence behind the claim."* Each run is shown three ways: layer by layer (the OpenUSD scene growing one edit at a time), the Surface view the user sees, and the workbench view of what the agents did and said. In the lighting run the agents found *"986 fixtures, seven modules,"* lit the modules one after another, and changed colours after the human answered a question.

Thanh Pham of Falkor's Surface team explains the team of four:

- a **coordinator** that splits the work among the others;
- a **task runner** that *"execute[s] most of the [tools], construct[s] the scene… [traverses] the graph"*;
- a **validator or reviewer** that *"will run on a different LM model[s,] look at the different findings of the task runner to approve or not,"* which Thanh likens to *"pair programming"*;
- a **memory manager** that sits *"at the very end of the process"* and consolidates the findings *"into a clear context. So we don't got like a massive amount of… unrelated fact[s] mix[ed] in over to the future run."*

The human steps in *"only [in] three place[s]"*: to state the intent (*"find all the light for me… and then add it to the USD scene"*), to answer the agent's question mid-run, and at the end *"to both validate or give feedback."* The slide for the Surface view adds that *"the person's answer was written in advance"* (still 11).

## Q&A (54:26–1:06:00)

- **Documentation.** A viewer with *"a BIM to Omniverse pipeline where this problem has been a headache"* asks for documentation. Jeppe: a blog post for GTC Berlin; *"our aim is to have this running in production for real live usage by March 2027."* Thanh: the agents' tools are documented as skills, prompts and MCP servers, still internal.
- **Vibe coding or a repeatable process?** A viewer asks whether *"building the model from drawings"* is *"akin to vibe coding with a really strong model, or is it a repeatable, deterministic process?"* Thanh: validation happens *"on multiple level[s]"*, agents checking each other, a human in the loop, and grounding against point clouds, pictures and video. Because *"Astra is very good at visual understanding,"* steps that used to need human refinement are now automated. Christopher adds a paper trail: whether the model *"can… reference a document where it got this number from or this dimension or is it kind of just inferred or guessed."*
- **Hardware.** An RTX PRO 6000 on a VM in Azure, sourced through Foundry, managed by its own agent; other agents run on Macs, backend servers and laptops, *"a semi-distributed system."*
- **Time and effort.** Asked how many person-weeks the twin took, Jeppe does not give a number: *"we can do a lot in a short while with a few humans powered by powerful agents if you have state-of-art agents you have the right harnesses… we already have all the scaffolding and the engines and the data all of that is already in place,"* which he calls *"the hard part of the answer I can't go into now."* Operators *"expect that speed and velocity."* And: *"even before Astra it was much harder… Astra was the first eye opener for us."*
- **Changes over time.** Facilities document changes, so contextualised data can be dated, but *"the data quality is a big issue"*: for plants that have run for 20 years, *"digitalization of data was not as… clear or rich."*

## Closing takeaways (1:06:00–1:09:20)

Shashi: frontier models' spatial reasoning *"has been an amazing unlock."* Jeppe: spatial reasoning on real data is *"a visible step"* towards spatial intelligence and autonomous operations. Thanh: *"context management"*; *"if one agent continues to do… a lot of task[s] it will get… overwhelmed quite easily,"* so a dedicated agent condenses the memory. Christopher: *"open your tools to the agents and see what happens."*

## Visual canon

Fourteen stills, all from Falkor's deck and the replayed runs (19:50–53:50). The deck's slides pair each demo video with *"What you saw"* and *"Under the hood"* text that the speakers mostly do not read out. Five slides repeat the architecture diagram with each demo's parts highlighted; these are summarised under still 5 rather than published. The stills were hand-picked from a 10-second contact sheet and 1080p checks (Gemini returned HTTP 402) and cropped to the slide.

### 1 · About Falkor

![[assets/2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations/03-21m10-about-falkor.webp|About Falkor, a Kongsberg company]]

*Still at [21:10](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1270s) from NVIDIA Omniverse, "Building AI Agent Workflows to Automate Industrial Operations".*

| KONGSBERG | Falkor | Product |
| --- | --- | --- |
| A Norwegian technology group, founded in 1814. More than 200 years of industrial heritage, delivering high-technology systems to demanding industries worldwide. KONGSBERG protects people and critical infrastructure, from deep sea to outer space. | A KONGSBERG company. Trusted by leading operators, engineers and asset managers across energy, processing, power and renewables. We help heavy-asset industries design, operate and optimize their assets across the lifecycle. | **Falkor Surface** is the shared operational environment where people turn the platform's intelligence into action. **Falkor Platform** is the foundation: it connects industrial data and systems, with the context and intelligence to build on. **Industrial simulators** are our heritage: physics-based, high-fidelity, dynamic process and multiphase flow simulators. |

Banner: *Shaping the future of work for heavy asset industries by connecting people, systems, and workflows.*

*Still vs. transcript:* the transcript renders the company as "Falcore", "Falco", "Falor" and "Valor" and the group as "the Kong group"; the slide gives both names, Kongsberg's founding year and the three products.

### 2 · Autonomy needs a machine-readable plant first

![[assets/2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations/05-23m20-autonomy-needs-a-machine-readable-plant.webp|Autonomy needs a machine-readable plant first]]

*Still at [23:20](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1400s) from NVIDIA Omniverse, "Building AI Agent Workflows to Automate Industrial Operations".*

*Five challenges operators face in making a plant legible to an agent:*

| Card | Text |
| --- | --- |
| Contextualization | What an asset is lives across CAD, drawings, documents, historians and work orders. Today people join them in their heads. |
| Standards | Standards exist, but every facility applies them its own way. Identifiers drift between systems. |
| Ecosystem | Owners, contractors, vendors and partners each hold part of the truth. Value comes when all of them work from the same data. |
| Simulation | Process and physics models exist. Setting them up from a facility's own data is still manual work. |
| Many systems, many protocols | Dozens of systems, each with its own API, protocol and identifiers. Access is a project in itself. |
| The aim: physical AI | Autonomous operations and autonomous systems. They need all of the above to be machine-readable and trusted. |

Banner: *A machine-readable plant lets an agent follow the same equipment across systems and trace each connection back to its source.*

*Still vs. transcript:* the narration walks through the pump example; the slide names the sources an asset is spread across (historians, work orders) and counts five challenges plus the aim.

### 3 · Agents raise the bar on context

![[assets/2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations/06-24m40-agents-raise-the-bar-on-context.webp|Agents raise the bar on context: before, now, next]]

*Still at [24:40](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1480s) from NVIDIA Omniverse, "Building AI Agent Workflows to Automate Industrial Operations".*

*The way people work with industrial software is changing, and the change makes the problem on the last slide more urgent.*

| Before: applications | Now: human to agent | Next: agent to agent |
| --- | --- | --- |
| A person learns each system, finds the data and joins it in their head. The knowledge stays with the people who know the plant. | A person states the intent. The agent works the systems, shows its reasoning and marks what it assumed. The person decides. | An agent can ask a specialist to investigate part of a problem. The specialist needs to know which asset is involved, what's already been checked, and which questions are still open. |

Banner: *An engineer can supply a missing connection from experience. An agent needs a way to discover it.*

*Still vs. transcript:* the narration has the third column almost word for word; the slide sets it in a three-stage sequence and gives the human-to-agent stage its rule: the agent marks what it assumed, the person decides.

### 4 · What we bring

![[assets/2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations/07-26m20-what-we-bring.webp|What we bring: industrial context, and engines agents can operate]]

*Still at [26:20](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1580s) from NVIDIA Omniverse, "Building AI Agent Workflows to Automate Industrial Operations".*

**An industrial graph that agents can traverse**
- The twin's graph in Falkor Platform is the source of truth: identity, relationships and semantics across CAD, drawings, documents and live data.
- Tagged geometry carries the asset ID that links it back to the graph.
- Agents query it through the Falkor SDK and MCP servers.

**Tools agents can use to inspect the plant**
- CAD Import Engine, in-house since 2018: load, traverse the hierarchy, mine attributes, render, pick. As the Semantic Reasoner: **28 tools, 11 skills**.
- Point Cloud Engine: merge, render and pick laser scans. As the Point Cloud Reasoner: **21 tools, 7 skills**.
- Three working days from first idea to a first version of the Semantic Reasoner. The engine already read the formats; we exposed it to agents.

**Frontier models, NVIDIA libraries, Microsoft Azure.** Agents run on frontier models such as GPT-6 Astra through Microsoft Foundry, in Codex. Together with NVIDIA Omniverse libraries (ovstage, ovrtx, ovphysx, ovstream) and OpenUSD, they lower the barrier to building a SimReady world. Larger simulations run on NVIDIA RTX PRO 6000 GPUs in Microsoft Azure.

Banner: *Agents follow an asset across drawings, CAD and scans, and build SimReady OpenUSD scenes to inspect it.*

*Still vs. transcript:* the tool and skill counts, the Falkor SDK, the four library names and "in Codex" are on the slide only.

### 5 · How it fits together

![[assets/2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations/08-28m10-how-it-fits-together.webp|How it fits together: Falkor's architecture for agents on plant data]]

*Still at [28:10](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1690s) from NVIDIA Omniverse, "Building AI Agent Workflows to Automate Industrial Operations".*

| Row | Components |
| --- | --- |
| Interaction | **Agent** (Reasoning Engine · or other agent harness) ⇢ **Operator** (watches · instructs the agent) ⇄ **Surface client** (browser viewport) |
| Access | **MCP Gateway** (authentication and data access), reached by the agent's tool calls; **MCP bridge** (acts on the live session) |
| Spatial reasoning | **As-built reasoner** (what is physically there; *Point Cloud Reasoner*) · **Semantic reasoner** (the source engineering data · structure, identity, meaning) · **Scene reasoner** (the composed 3D scene · Cogs for reach, Omniverse for fidelity) |
| Engines | **Point Cloud Engine** (runs at ingest; merges overlapping scans, one sample per grid cell) · **CAD Import Engine** (runs at ingest; ingest, hierarchy, metadata extraction, tessellation; *NVIDIA libraries embedded in the pipeline*: SimReady validation, USD optimizer, content + CAD ingestion) · **Cogs Engine** (our own 3D stack, backend and in-browser renderer) · **NVIDIA ov\* libraries**, composed per capability: ovrtx (render + identity AOV), ovphysx (rigid-body physics), ovstream (WebRTC transport), ovstage (scene data plane) |
| Data | **Laser scans** (E57 · tripod and SLAM; object IDs link to graph tags) · **Engineering CAD** (AVEVA RVM · Hexagon VUE and other formats) · **Graph**, *source of truth* (identity, relationships, semantics · mastered here) · **USD stage** (derived projection · asset identity resolves back to the graph) |

Arrows: CAD Import Engine writes *metadata + identity* to the Graph; the Graph is *projected* to the USD stage; the USD stage feeds *scene data* to ovstage; ovstream sends *WebRTC frames + input* to the Surface client.

Highlighted on the per-demo copies of this slide (not published): demo 1, CAD Import Engine, ovrtx, Engineering CAD, USD stage; demo 2, Agent, Surface client, Semantic and Scene reasoners; demo 3, Surface client, Scene reasoner, ovstage, Graph; demo 4, Semantic reasoner, Graph, USD stage; demo 5, As-built reasoner, Point Cloud Engine, Laser scans.

*Still vs. transcript:* the narration names the reasoners and the cockpit metaphor; the diagram adds the MCP gateway, the Cogs Engine, the CAD formats read, the scan formats, and the rule that the USD stage is a derived projection while the graph is mastered. The Agent box reads "or other agent harness": the agent is interchangeable.

### 6 · Semantic mining

![[assets/2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations/10-30m45-semantic-mining.webp|Semantic mining: a plant lit only by its documented fixtures]]

*Still at [30:45](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1845s) from NVIDIA Omniverse, "Building AI Agent Workflows to Automate Industrial Operations".*

Video caption: *The whole facility, lit only by its documented fixtures.*

- **What you saw.** OpenUSD built from the engineering CAD by the Falkor CAD Import Engine, light simulated by NVIDIA ovrtx. Agents found more than six thousand light fixtures by semantic mining. Each fixture's bulb type sets its color, its wattage its intensity.
- **Under the hood.** Light rules used to be written by hand, per site, over hours. On an earlier model, an agent read the fixtures' free-text descriptions and built the light-type taxonomy; the engine then applies it across the plant.

Banner: *The agent derives rules from CAD. The engine applies them at scale.*

*Still vs. transcript:* the slide adds what the rules used to cost (written by hand, per site, over hours) and that the taxonomy was built on an earlier model.

### 7 · Is there room to remove the strainer cover?

![[assets/2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations/13-35m10-strainer-cover-longer-zone-meets-railing.webp|A longer handling zone meets the railing]]

*Still at [35:10](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2110s) from NVIDIA Omniverse, "Building AI Agent Workflows to Automate Industrial Operations".*

Video, *Spatial reasoning · 02 / One asset, from drawing to work decision*: **A longer zone meets the railing.** A yellow strainer cover inside a green handling envelope; label *DQE-48 enters at about 1.0 m*; note *Analytical outlines shown through foreground objects; not physical moving parts*; caption *The same envelope extended to 1.2 m intersects the railing at about 1.0 m.*

- **What you saw.** One vessel across three P&IDs, its process put back into the plant, 16 nozzle connections verified. Then a maintenance job at a strainer: a 0.8 m handling zone is clear, extended to 1.2 m it meets the railing. The agent takes forward a conditional option with the open questions named, as an inspection proposal in Falkor Surface.
- **Under the hood.** Two channels into geometry. Text: query the hierarchy and attributes, steered by helpers so the agent reads only the nodes it needs out of 100k+. Vision: highlight confirms a hypothesis at a glance; pick answers "what is this?".

Banner: *The railing is about a meter from the cover. How far does the cover need to come out?*

*Still vs. transcript:* the narration gives 0.8 m and 1.2 m; the slide says what the agent hands on (a conditional option with its open questions named, as an inspection proposal) and how it reads a model of more than 100,000 nodes.

### 8 · From a pixel back to the asset

![[assets/2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations/15-37m40-from-a-pixel-back-to-the-asset.webp|From a pixel back to the asset: operating state on the machine]]

*Still at [37:40](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2260s) from NVIDIA Omniverse, "Building AI Agent Workflows to Automate Industrial Operations".*

Video: **Put operating state on the machine.** On a motor, *MOTOR POWER 35.14 MW*; beside it, *CG-38-8988 / SPEED FEEDBACK 3470.1 rpm, 07 APR 2026 12:07:32 UTC*, a trend line, *87 samples / linear display interpolation*. Caption: *Power and speed history projected onto the machine.*

- **What you saw.** In Falkor Surface: a simulated level, a recorded level with its history, motor power and speed on the machine, and at plant scale, a simulated temperature skin on three coolers.
- **Under the hood.** Asset IDs from the graph are written into the USD as labels; ovrtx renders a separate ID image, so the agent can pick a point on tagged equipment and recover its asset ID. On an open-data plant: **229k prims and 84,527 asset IDs**, every one carried as a label.

Banner: *The same asset ID connects what the agent sees to what the plant knows about it.*

*Still vs. transcript:* the scale figures (229k prims, 84,527 asset IDs) and the fact that they come from an open-data plant are slide-only.

### 9 · A small symbol becomes a 17-meter cooler

![[assets/2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations/17-42m25-small-symbol-becomes-17-meter-cooler.webp|Building an OpenUSD model from documentation: a symbol becomes a cooler]]

*Still at [42:25](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2545s) from NVIDIA Omniverse, "Building AI Agent Workflows to Automate Industrial Operations".*

Video, *04 / A plant without CAD*, three panels: **A / Original evidence**, drawing 62-2E-MK-W86-56354, a data table, and *What this evidence establishes: DT-26-7342 / ID 1025 mm x 17,106 mm*; **B / New USD / illustrative process layout**, a vessel and a long cooler; **C / Accumulating process graph**, *09 entities, 09 relations*, legend *main gas, recycle, shared drive, unknown*. Caption: *The ID x L table supplies a very different proportion from the schematic symbol.*

- **What you saw.** A facility that runs on drawings. The agent builds an OpenUSD model of the plant from the drawings, every part traced back to a drawing or marked as assumed.
- **Under the hood.** It reads symbols, data tables, access, section and detail drawings, joins six P&IDs into one process and places the equipment from the plot plan. Anything the agent infers is marked as assumed or unknown, so a reviewer sees exactly what the drawings support.

Banner: *Process schematics show what connects. The plot plan gives the equipment positions. The agent marks what it has to infer.*

*Still vs. transcript:* the narration says "a 17 m cooler"; the still shows the evidence for it (inner diameter 1,025 mm, length 17,106 mm from a data table) and the graph the agent builds as it goes. Later frames of the same video reach 23 entities and 31 relations.

### 10 · Checking vessel geometry against a laser scan

![[assets/2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations/19-44m15-laser-scan-measure-the-fit.webp|Checking vessel geometry against a laser scan, clutter included]]

*Still at [44:15](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2655s) from NVIDIA Omniverse, "Building AI Agent Workflows to Automate Industrial Operations".*

Video: **Measure the fit, clutter included.** A fitted cylinder in a point cloud; *Local fit distance, 53,871 active measured points*; legend *0–20 mm, 20–80 mm, over 80 mm*; caption *Cyan: within 20 mm of the fitted cylinder. Pink: more than 80 mm away, mostly surrounding structure.*

- **What you saw.** A vessel sized from its vendor drawing, connections from the P&ID, dashed where proposed. Then a real scan from a producing platform: slices find the vessel outlines, the model is fitted, and every point is colored by its distance to the fit.
- **Under the hood.** On another site, scan to CAD: **23 scans, about 600 million points, merged at 5 cm in about 30 s**. A tank shell from the scan alone came within about 2 cm of the CAD; **the scan and the CAD disagreed by 11 cm**. Fitted on its own points: **RMS 2.36 mm**. Checked on held-out points: **p95 30.79 mm**.

Banner: *Trust comes from checking whether the model still matches the scans.*

*Still vs. transcript:* none of the figures is spoken. Jeppe says only that "the two numbers on the slide come from a separate site"; the slide gives the fit on the points used (2.36 mm) and on held-out points (30.79 mm), which is the gap Christopher describes between a thin slice and the whole scan.

### 11 · Lights from CAD: Surface view

![[assets/2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations/21-49m32-lights-from-cad-surface-view.webp|Lights from CAD in Falkor Surface, the human-in-the-loop view]]

*Still at [49:32](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2972s) from NVIDIA Omniverse, "Building AI Agent Workflows to Automate Industrial Operations".*

Demo 6b, a recorded run in Falkor Surface: session explorer (run coordinator, task runner, their context and files), 3D viewer with the pictures the agents posted (*HU - 37 lights switched on* and further modules), chat, and a reasoning overview of tool calls. In the chat (small print, read zoomed): *"Task: the Huldra platform's USD scene has no lights of its own."* Then, from the task runner to the run coordinator: *"All 986 lights are on with the same white light at relative intensity 10000. The descriptions name fluorescent fittings (including battery and recessed versions), SON/T floodlights, navigation lanterns, red aviation lights and helicopter wave-off lights. Does the host want anything more shown about the lights?"*

- **What you see.** The run in a Surface layout: the session explorer, a 3D viewer with the pictures the agents posted, the chat and the reasoning overview.
- **What to notice.** The coordinator asks the human a question. The answer, in plain words, becomes the next step: show what kind of light it is, with an illustrative color temperature.
- **How it works.** A recorded run on its own timeline, built with Surface's own design system and components. **The person's answer was written in advance.**

*Still vs. transcript:* the narration says the human answered mid-run; the slide says that answer was scripted before the run. The question the agent asks, and the platform's name, are on screen only.

### 12 · Workbench: the result validator at work

![[assets/2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations/22-52m27-workbench-result-validator-running.webp|Agent workbench with the result validator running]]

*Still at [52:27](https://www.youtube.com/watch?v=I4X91GKLgNk&t=3147s) from NVIDIA Omniverse, "Building AI Agent Workflows to Automate Industrial Operations".*

Header: **All 986 exported fixture lights are on.** *Task: Find, count, export and light the fixtures; relay its check-in to the host · Result validator: review running, 0 of 5 claims judged · Nothing disputed, open or held.* Picture: *Huldra topside under fixture lighting.*

| Agent | Harness · model | State |
| --- | --- | --- |
| Run coordinator | Claude · opus-5-5 | working on step 2 of 4: Result validator: blind recount from h[andoff] |
| Task runner | Codex · gpt-6.2-astra | done in 13 min 43 s, handed over 6 findings |
| Result validator | Claude · sonnet-5-5 | review running, 0 of 5 claims judged; read handoff.json, read huldra_master.usda, wrote VERDICT.md |
| Memory manager | Claude | (timeline lane only at this point) |

Claims panel: *5 claims: validator agrees with 0, disagrees with 0, 5 not re-checked; 1 withdrawn*, each tagged *from a source*, *test passed* (evidence check_export.py or check_scene.py, *from the log*) or *assumed* (*"For the demonstration I chose 4200 K for named…"*). Tools used: CAD reasoner (MCP, 24 calls), OV reasoner (MCP), OpenUSD (API, 15 scripts), looked at pictures (vision), CLI (156 commands), file tools. Timeline 15:53 of 18:15, lanes *Host, Run coordinator, Task runner, Result validator, Memory manager*, with markers START, REPLACED, REPLACED, CHECKED, CHECKED, ASKED, ANSWER, HANDOVER.

*Still vs. transcript:* Thanh says the reviewer runs "on a different LLM model"; the screen shows which: the task runner on Codex with gpt-6.2-astra, the validator on Claude with sonnet-5-5, the coordinator on Claude with opus-5-5. It also shows that every claim carries its evidence and a label for where it came from, and that the human appears as its own lane, "Host".

### 13 · Workbench: the task runner's plan

![[assets/2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations/23-53m15-workbench-task-runner-plan.webp|Agent workbench showing the task runner's eight-step plan]]

*Still at [53:15](https://www.youtube.com/watch?v=I4X91GKLgNk&t=3195s) from NVIDIA Omniverse, "Building AI Agent Workflows to Automate Industrial Operations".*

*In progress: 8. Render the topside* (11:42 of 18:15). The task runner's plan, 7 of 8 done:

1. Show the original scene (0:51, 3 min 13 s)
2. Test the EL2- rule (1:12, 46 s)
3. Identify and count fixtures (1:58, 41 s)
4. Export and recount USD lights (2:39, 1 min 25 s)
5. Compose and show all lights off (4:04, 3 min 33 s)
6. Switch on seven modules (7:37, 55 s)
7. Check in with the coordinator (8:32, 1 min 38 s)
8. Render the topside (10:11, running)

Log: *Rejected el2.png: The first CAD render was blank…*; *Withdrew claim C1: The 507 matches comprise 357…*; two logged failures (*rg*; *a call, its command not recorded*); *Test passed: check_export.py, exit 0*; *Test passed: check_scene.py, exit 0*; *+91 more*. Claims: *5 claims: 2 test passed, 2 from a source, 1 assumed; 1 withdrawn.* Before and after: *HU - 37 lights switched on* and *Fixture temperature demonstration*, *"Amber pools flank the crane and stairs. All 986 intensities stay at 10000."* Timeline: the human's ASKED and ANSWER markers sit after the task runner's two REPLACED and two CHECKED events.

*Still vs. transcript:* the narration names the four roles; the still shows the run's own record of what went wrong (a blank first render rejected, a claim withdrawn, two failed calls logged) next to what passed.

### 14 · Lights from CAD: Workbench view

![[assets/2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations/24-53m35-lights-from-cad-workbench-view.webp|Lights from CAD, workbench view: what the agents did and how it works]]

*Still at [53:35](https://www.youtube.com/watch?v=I4X91GKLgNk&t=3215s) from NVIDIA Omniverse, "Building AI Agent Workflows to Automate Industrial Operations".*

| What the agents did | What to notice | How it works |
| --- | --- | --- |
| The task runner (Codex) selects the light fixtures by a tag rule, starts from a dark scene and switches the lights on module by module. The Semantic Reasoner exports them to OpenUSD. | Every claim shows its evidence: the check script and its exit code, from the log. The validator recounts blind and agrees; a first, wrong selection is replaced. The decision: accepted with named limits. | Four agents and one human share the run. The agents coordinate, do the task, check and remember; the Host lane is the human. Tools: the Semantic Reasoner over MCP, OpenUSD scripts, vision, the shell. |

*Still vs. transcript:* the outcome of the run, accepted "with named limits" after a blind recount, and the replaced first selection are on the slide only.

## Dynamic-capabilities reading

- **`digital-transforming/navigating-innovation-ecosystems`.** The work is a partnership across four vendors: Falkor's engines and graph, NVIDIA's Omniverse libraries (*"we're not providing the end application"*), OpenAI and Anthropic models run in Codex and Claude, and Microsoft's Foundry and Azure GPUs. NVIDIA's split of Omniverse into separate libraries is what Falkor builds on, and both companies publish skills so that agents can use their tools. The *Ecosystem* card names the industry's side of it: owners, contractors, vendors and partners each hold part of the truth.
- **`digital-seizing/rapid-prototyping`.** A first Semantic Reasoner in three working days by exposing an existing engine through MCP, started after a programmatic attempt proved *"quite complex"*; a small team iterating fast (*"you don't need many people to do it"*); and recorded demos on open data, with production use aimed for March 2027.
- **`contextual/external-triggers`.** The trigger is a model capability: *"Astra was the first eye opener for us"* on spatial reasoning, *"this was probably not possible… even last year,"* and operators who *"expect that speed and velocity to accelerate as the rest of the world do."*

## Related in this wiki

- [[2026-02-01-manditereza-ontology-driven-industrial-ai|Manditereza (HiveMQ), ontology-driven intelligence for industrial agents]] — both concern grounding industrial agents in a graph of asset identity and relationships drawn from fragmented plant systems. Manditereza proposes an ontology-based semantic data layer under the agents; Falkor shows agents traversing its digital-twin graph through MCP servers, with asset IDs carried into the OpenUSD scene.
- [[2026-09-30-singh-botha-bloomberg-flow-engineering-ai-hardware-design|Flow Engineering on Bloomberg Tech]] — both concern agents that read engineering data spread across CAD and simulation tools. Flow's agents follow changes in CAD, simulation and Git in hardware design; Falkor's read engineering CAD, P&IDs, data tables and laser scans of a plant.
- [[2026-11-23-google-cloud-tech-why-agent-demos-break-in-production|Google Cloud Tech, why agent demos break in production]] — both separate the agent that does the work from one that reviews it. Google's engineers describe an independent reviewer agent in a fresh context window and objective checks before human review; Falkor's run has a validator on a different model recount the task runner's claims blind, before the human validates.
- [[2026-11-20-chase-langchain-future-of-agents|Chase (LangChain) on the future of agents]] — both concern a separate step that decides what an agent keeps between runs. Chase describes "dreaming", a background process that updates memory from earlier runs, and calls deciding what to remember the hard part; Falkor's memory manager agent condenses a run's findings so unrelated facts do not carry into later runs.

## Linked entities and concepts

- [[NVIDIA]] — host channel and partner: the Omniverse libraries (ovrtx, ovstage, ovphysx, ovstream), OpenUSD, the Blender add-on, agent skills, RTX PRO 6000 GPUs. The channel, NVIDIA Omniverse, is proposed as an alias.
- [[Microsoft]] — Microsoft Foundry, through which Falkor sources GPT-6 Astra, and the Azure VM with the RTX PRO 6000; NVIDIA's Ganesh joins from Microsoft Ignite.
- [[OpenAI]] — GPT-6 Astra (slide) and gpt-6.2-astra in Codex, the task runner's model.
- [[Anthropic]] — Claude opus-5-5 (run coordinator) and sonnet-5-5 (result validator) on the workbench.
- Concepts: [[industrial-ai-agents]] (the main fit), [[knowledge-graphs]] (the graph as source of truth, projected into the scene), [[agent-oversight-and-delegation]] (three human touchpoints, a validator, claims with evidence), [[multi-agent-failure-modes]] (a coordinator, runner, validator and memory manager in one run), [[industry-4-0]] (digital twins of plants), [[agent-harness]] (the diagram's "or other agent harness"; *"the right harnesses"*).

**Dangling** (single-source mention, deferred): Falkor, Kongsberg, Jeppe Sverdrup, Christopher Dyken, Thanh Pham, Ganesh Sivaraman, Shashi Bhushan, Max Bickley, Ashley (NVIDIA tech marketing), Edmar (NVIDIA community manager), NVIDIA Omniverse (as a product), OpenUSD, Microsoft Foundry, Codex.

## Source quality

A partner showcase on the host vendor's channel: NVIDIA presents a software partner that builds on its libraries, and the partner presents its own products. The demos are recorded and sped up, built on *"neutral data or data that is not… confidential to any particular operator."* The agent-trace runs name their plant on screen as the Huldra platform; demo 3's slide gives its figures for *"an open-data plant"*. No operator outcome, cost, time saved or error rate is reported. Asked how many person-weeks the twin took, Jeppe gives no number. Production use is an aim for March 2027.

Every figure is the presenters' own and cannot be checked from the video: more than 6,000 fixtures in demo 1's facility; 986 in the Huldra run, a different plant; 28 and 21 reasoner tools; three working days; the scan figures from "another site". The slide on the Surface view says the human's mid-run answer *"was written in advance,"* so the run does not show a live human decision. The model names (GPT-6 Astra, Claude opus-5-5 and sonnet-5-5) come from the slide and the workbench screen; the transcript has *"GPT6 Astra"*, *"GPT62 Astra"*, *"Opus 5.5"* and *"OPOS 552"*. Slide 4 announces *"Five challenges"* and shows six cards, the sixth being the aim.

**Identity check.** The title and description match the content, with one omission: the description does not mention NVIDIA's own 15-minute segment on the Blender add-on and real-time viewer skills (4:14–15:30). The title slide dates the stream 18 November 2026; YouTube's publish date is 19 November (Pacific). The track is **auto-generated** (ASR); proper names were corrected in the raw file against the lower-thirds and slides, and every change is listed in its `notes:`. Quotations keep the speakers' wording, with bracketed repairs where the ASR dropped a word.
