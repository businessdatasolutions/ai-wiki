---
video_id: I4X91GKLgNk
url: https://www.youtube.com/watch?v=I4X91GKLgNk
transcript: raw/videos/building-ai-agent-workflows-to-automate-industrial-operations.md
stills_dir: raw/images/building-ai-agent-workflows-to-automate-industrial-operations
stills_count: 28
extractor:
  method: hand-picked (no Gemini call)
  reason: Gemini API returned 402 (prepayment credits depleted)
  sampling: 438 frames at 360p, one every 10 s over the 1:13:01 stream, consecutive repeats merged into 342 tiles and read as 8 contact sheets; scene detection found 69 cuts, and the 9 shots shorter than 10 s that the grid missed were added as one extra sheet
  dense_pass: about 60 further frames cut at 1080p (not 360p) inside the Falkor deck (19:50-53:50) and the Q&A, to find a frame of each slide without the YouTube player overlay or the slide tool's page bar over the text, the built state of each demo video, and the readable state of the agent workbench (52:00-53:20, checked every 2 to 5 s)
  frames: yt-dlp stream URL (<=1080p) seeked with ffmpeg
  crop: published stills cropped to the shared slide area (1544x868 at 365,105), which drops the camera strip on the left
acquired: '2026-11-23'
---

# Stills manifest (hand-picked)

Each still was chosen from the contact sheets and then read at full resolution, small print zoomed 2x to 4x. The readings below were made by viewing the pixels; the source page carries the verified transcriptions. Reviewed and not cut: the opening animation and series card, the video-call gallery and two-up host shots (0:20-4:10, 14:00-19:20, 54:00-1:12:40), the NVIDIA segment's screen share (Ashley's Blender model of her house built from architect's plans and the OVRTX viewport, 6:20-11:00; Max's real-time viewer skills reel: capped section, exact circular edge, stylised rendering, CFD streamlines, XR hand grab, an S1 arm in OV Newton, 11:20-13:50), the "Agent Traces" section card (46:30-47:50), the community shout-out of a LinkedIn post on marine dynamics for Isaac Sim (1:11:20-1:12:10) and the end card. The NVIDIA reel shows the features the narration names one by one, so nothing from it was cut.

## 01 · 0:30 · Cast lower-thirds
- File: `01-00m30-cast-lower-thirds.png` · [0:30](https://www.youtube.com/watch?v=I4X91GKLgNk&t=30s)
- Eight tiles: **Edmar | Community Manager**; **Ashley | NVIDIA | Tech Marketing**; **Ganesh Sivaraman | NVIDIA**; **Shashi Bhushan | NVIDIA**; **Max Bickley | NVIDIA**; **Christopher Dyken | Falkor**; **Jeppe Sverdrup | Falkor**; **Thanh Pham | Falkor**. **Not published**: names over faces; used to fix the transcript's names.

## 02 · 19:50 · Title slide
- File: `02-19m50-agentic-spatial-engineering-title.png` · [19:50](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1190s)
- Falkor logo, "a KONGSBERG company". **Agentic spatial engineering.** *Agents that see, build and check an industrial plant, with NVIDIA Omniverse libraries.* NVIDIA Omniverse developer livestream · November 18, 2026 · Falkor product engineering team. **Not published**: title card; its date and team name are recorded on the source page.

## 03 · 21:10 · About Falkor
- File: `03-21m10-about-falkor.png` · [21:10](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1270s)
- Three cards. KONGSBERG: a Norwegian technology group, founded in 1814, more than 200 years of industrial heritage; protects people and critical infrastructure "from deep sea to outer space" (kongsberg.com). Falkor: a KONGSBERG company, trusted by operators, engineers and asset managers across energy, processing, power and renewables; helps heavy-asset industries design, operate and optimize assets across the lifecycle (falkor.com). Product: Falkor Surface (shared operational environment), Falkor Platform (the foundation that connects industrial data and systems), industrial simulators (physics-based, high-fidelity, dynamic process and multiphase flow) (falkor.com/products/falkor-suite). Banner: "Shaping the future of work for heavy asset industries by connecting people, systems, and workflows". **Published.**

## 04 · 22:15 · Agenda
- File: `04-22m15-agenda.png` · [22:15](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1335s)
- 01 Context; 02 What we bring; 03 Product demos, "From drawing to reality"; 04 Agent traces, "Two runs replayed through scene edits, the user's view in Surface, and the agents' tool calls"; 05 Q&A. **Not published**: navigation.

## 05 · 23:20 · Autonomy needs a machine-readable plant first
- File: `05-23m20-autonomy-needs-a-machine-readable-plant.png` · [23:20](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1400s)
- Subtitle "Five challenges operators face in making a plant legible to an agent", six cards: Contextualization, Standards, Ecosystem, Simulation, Many systems many protocols, The aim: physical AI. Banner: "A machine-readable plant lets an agent follow the same equipment across systems and trace each connection back to its source." **Published.**

## 06 · 24:40 · Agents raise the bar on context
- File: `06-24m40-agents-raise-the-bar-on-context.png` · [24:40](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1480s)
- Before: applications / Now: human to agent / Next: agent to agent, with one paragraph each. Banner: "An engineer can supply a missing connection from experience. An agent needs a way to discover it." **Published.**

## 07 · 26:20 · What we bring
- File: `07-26m20-what-we-bring.png` · [26:20](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1580s)
- Industrial graph (Falkor Platform twin graph as source of truth; asset ID on tagged geometry; Falkor SDK and MCP servers). Tools (CAD Import Engine in-house since 2018, as the Semantic Reasoner 28 tools, 11 skills; Point Cloud Engine, as the Point Cloud Reasoner 21 tools, 7 skills; three working days to a first Semantic Reasoner). Frontier models, NVIDIA libraries, Microsoft Azure (GPT-6 Astra through Microsoft Foundry, in Codex; ovstage, ovrtx, ovphysx, ovstream and OpenUSD; RTX PRO 6000 GPUs in Azure). **Published.**

## 08 · 28:10 · How it fits together
- File: `08-28m10-how-it-fits-together.png` · [28:10](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1690s)
- Architecture in five rows: Interaction (Agent, Operator, Surface client), Access (MCP Gateway, MCP bridge), Spatial reasoning (As-built, Semantic, Scene reasoners), Engines (Point Cloud Engine, CAD Import Engine with embedded NVIDIA libraries, Cogs Engine, NVIDIA ov* libraries), Data (Laser scans, Engineering CAD, Graph as source of truth, USD stage as derived projection). Small print read at 4x zoom. **Published.**

## 09 · 29:25 · Demo 1 map: the plant becomes observable
- File: `09-29m25-demo1-the-plant-becomes-observable.png` · [29:25](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1765s)
- The architecture with CAD Import Engine, ovrtx, Engineering CAD and USD stage highlighted. Caption: "What does it take to light an entire facility using only the fixtures documented in its engineering CAD?" **Not published**: a highlighted copy of still 08; the highlights are listed under still 08 on the source page.

## 10 · 30:45 · Semantic mining
- File: `10-30m45-semantic-mining.png` · [30:45](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1845s)
- Night render of a plant; caption "The whole facility, lit only by its documented fixtures". What you saw: more than six thousand fixtures found by semantic mining; bulb type sets colour, wattage intensity. Under the hood: light rules used to be written by hand, per site, over hours; on an earlier model an agent built the light-type taxonomy from the fixtures' free-text descriptions. **Published.**

## 11 · 31:13 · Demo 2 map: from a process drawing to a maintenance decision
- File: `11-31m13-demo2-process-drawing-to-maintenance-decision.png` · [31:13](https://www.youtube.com/watch?v=I4X91GKLgNk&t=1873s)
- Agent, Surface client, Semantic reasoner and Scene reasoner highlighted. Caption: "The agent follows the process across three drawings, then tests how much room there is to remove a strainer cover." **Not published**: highlighted copy of still 08.

## 12 · 34:50 · Strainer cover: nozzle detail
- File: `12-34m50-strainer-cover-nozzle-detail.png` · [34:50](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2090s)
- The same slide as still 13, with the video at "Nozzle detail": four nozzle tags (pressure differential transmitters 80 mm, level gauges 50 mm) around a vessel; "16 verified connections. The surrounding plant is hidden so the nozzles can be checked against the source data". **Not published**: the slide text is the same as still 13, and the narration gives the 16 connections.

## 13 · 35:10 · Strainer cover: a longer zone meets the railing
- File: `13-35m10-strainer-cover-longer-zone-meets-railing.png` · [35:10](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2110s)
- Video: "A longer zone meets the railing", "DQE-48 enters at about 1.0 m", "The same envelope extended to 1.2 m intersects the railing at about 1.0 m". What you saw / Under the hood (two channels into geometry; nodes out of 100k+). Banner question about the railing at about a metre. **Published.**

## 14 · 37:05 · Demo 3 map: information on the geometry
- File: `14-37m05-demo3-information-on-the-geometry.png` · [37:05](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2225s)
- Surface client, Scene reasoner, ovstage and Graph highlighted. Caption: "Recorded readings and simulation results appear on the equipment they describe." **Not published**: highlighted copy of still 08.

## 15 · 37:40 · From a pixel back to the asset
- File: `15-37m40-from-a-pixel-back-to-the-asset.png` · [37:40](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2260s)
- Video: "Put operating state on the machine": MOTOR POWER 35.14 MW; CG-38-8988 / SPEED FEEDBACK 3470.1 rpm, 07 APR 2026, 87 samples. Under the hood: asset IDs written into the USD as labels; ovrtx renders a separate ID image; on an open-data plant 229k prims and 84,527 asset IDs. **Published.**

## 16 · 38:40 · Demo 4 map: a plant without CAD
- File: `16-38m40-demo4-a-plant-without-cad.png` · [38:40](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2320s)
- Semantic reasoner, Graph and USD stage highlighted. Caption: "What can an agent build from the drawings, and what does it still have to assume?" **Not published**: highlighted copy of still 08.

## 17 · 42:25 · A small symbol becomes a 17-meter cooler
- File: `17-42m25-small-symbol-becomes-17-meter-cooler.png` · [42:25](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2545s)
- Video panels: original evidence (drawing 62-2E-MK-W86-56354, a data table); what the evidence establishes, "DT-26-7342 / ID 1025 mm x 17,106 mm"; illustrative process layout; accumulating process graph "09 entities 09 relations", legend main gas, recycle, shared drive, unknown. Slide text on six P&IDs, the plot plan and assumed parts. Other frames of the same slide (39:10-42:20) show "A second drawing changes the silhouette" (14 entities, 15 relations), "Forty boxes become 160 cyclones" and "The process also returns upstream" (23 entities, 31 relations). **Published.**

## 18 · 42:55 · Demo 5 map: ground the model against reality
- File: `18-42m55-demo5-ground-the-model-against-reality.png` · [42:55](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2575s)
- As-built reasoner, Point Cloud Engine and Laser scans highlighted. Caption: "How closely does the modeled geometry fit the measured points?" **Not published**: highlighted copy of still 08.

## 19 · 44:15 · Checking vessel geometry against a laser scan
- File: `19-44m15-laser-scan-measure-the-fit.png` · [44:15](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2655s)
- Video: "Measure the fit, clutter included"; 53,871 active measured points; legend 0-20 mm, 20-80 mm, over 80 mm; "Cyan: within 20 mm of the fitted cylinder. Pink: more than 80 mm away, mostly surrounding structure". Under the hood: on another site, 23 scans, about 600 million points, merged at 5 cm in about 30 s; tank shell within about 2 cm of the CAD; scan and CAD disagreed by 11 cm; RMS 2.36 mm on its own points; p95 30.79 mm on held-out points. **Published.**

## 20 · 48:35 · Lights from CAD: layer by layer
- File: `20-48m35-lights-from-cad-layer-by-layer.png` · [48:35](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2915s)
- Demo 6a. A USD viewer replays the run beside a Changes panel. What to notice: "Every step is an edit to one small layer file, `lights_state.usda`: module by module the lights switch on, then the fixture colors change. Applied in place." **Not published**: the narration describes the layer-by-layer view; the slide adds only the layer file's name, recorded on the source page.

## 21 · 49:32 · Lights from CAD: Surface view
- File: `21-49m32-lights-from-cad-surface-view.png` · [49:32](https://www.youtube.com/watch?v=I4X91GKLgNk&t=2972s)
- Demo 6b in Falkor Surface: session explorer, 3D viewer with posted pictures, chat, reasoning overview. Chat (read at 4x): "Task: the Huldra platform's USD scene has no lights of its own"; task runner to run coordinator: all 986 lights on at the same white light, relative intensity 10000, the descriptions name fluorescent fittings, SON/T floodlights, navigation lanterns, red aviation lights and helicopter wave-off lights; "Does the host want anything more shown about the lights?" How it works: "The person's answer was written in advance." **Published.**

## 22 · 52:27 · Workbench: result validator running
- File: `22-52m27-workbench-result-validator-running.png` · [52:27](https://www.youtube.com/watch?v=I4X91GKLgNk&t=3147s)
- Demo 6c, full screen, 15:53 of 18:15. "All 986 exported fixture lights are on." Agents: Run coordinator, Claude, opus-5-5 (step 2 of 4, "Result validator: blind recount from h..."); Task runner, Codex, gpt-6.2-astra ("done in 13 min 43 s, handed over 6 findings"); Result validator, Claude, sonnet-5-5 ("review running, 0 of 5 claims judged"). Timeline lanes Host, Run coordinator, Task runner, Result validator, Memory manager (Claude), markers START, REPLACED x2, CHECKED x2, ASKED, ANSWER, HANDOVER. The later memory-manager stage (52:30-52:45) appears only under the YouTube overlay. **Published.**

## 23 · 53:15 · Workbench: the task runner's plan
- File: `23-53m15-workbench-task-runner-plan.png` · [53:15](https://www.youtube.com/watch?v=I4X91GKLgNk&t=3195s)
- 11:42 of 18:15, step 8 of 8 "Render the topside". Plan 7 of 8 done (show the original scene; test the EL2- rule; identify and count fixtures; export and recount USD lights; compose and show all lights off; switch on seven modules; check in with the coordinator; render the topside), with times. Log lines: rejected el2.png (first CAD render blank), withdrew claim C1, two logged failures, check_export.py and check_scene.py passed with exit 0. Claims: "5 claims: 2 test passed, 2 from a source, 1 assumed; 1 withdrawn", each with its evidence and where the evidence came from. Before/after: "HU - 37 lights switched on" vs "Fixture temperature demonstration", "All 986 intensities stay at 10000". **Published.**

## 24 · 53:35 · Lights from CAD: Workbench view (slide)
- File: `24-53m35-lights-from-cad-workbench-view.png` · [53:35](https://www.youtube.com/watch?v=I4X91GKLgNk&t=3215s)
- What the agents did / What to notice / How it works (four agents and one human; the Host lane is the human; tools: Semantic Reasoner over MCP, OpenUSD scripts, vision, the shell). The embedded video shows the player overlay; the three text cards are clear. **Published.**

## 25 · 55:40 · Chat card: BIM to Omniverse
- File: `25-55m40-chat-bim-to-omniverse-question.png` · [55:40](https://www.youtube.com/watch?v=I4X91GKLgNk&t=3340s)
- LinkedIn User: "we have a BIM to Omniverse pipeline where this problem has been a headache. Is there a doc I could review to see this solution in detail?" **Not published**: the narration reads the question out; quoted on the source page.

## 26 · 59:10 · Chat card: vibe coding or deterministic?
- File: `26-59m10-chat-vibe-coding-question.png` · [59:10](https://www.youtube.com/watch?v=I4X91GKLgNk&t=3550s)
- LinkedIn viewer: "Is "building the model from drawings" akin to vibe coding with a really strong model, or is it a repeatable, deterministic process? (I know LLMs are not deterministic in their outputs)". **Not published**: the narration paraphrases it; quoted on the source page.

## 27 · 1:02:55 · Chat card: time and effort
- File: `27-62m55-chat-time-and-effort-question.png` · [1:02:55](https://www.youtube.com/watch?v=I4X91GKLgNk&t=3775s)
- LinkedIn viewer: "Question for Falkor: for this one industrial installation, how much time and how many man weeks or months did it take to create the digital twin?" **Not published**: quoted on the source page.

## 28 · 1:05:20 · Chat card: changes over time
- File: `28-65m20-chat-changes-over-time-question.png` · [1:05:20](https://www.youtube.com/watch?v=I4X91GKLgNk&t=3920s)
- YouTube viewer: "also how about projects changes overtime, does it track those ? It would be a lifesaver across engineering teams". **Not published**: quoted on the source page.
