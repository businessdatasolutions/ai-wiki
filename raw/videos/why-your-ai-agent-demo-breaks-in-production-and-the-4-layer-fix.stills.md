---
video_id: BKVDdL1InsA
url: https://www.youtube.com/watch?v=BKVDdL1InsA
transcript: raw/videos/why-your-ai-agent-demo-breaks-in-production-and-the-4-layer-fix.md
stills_dir: raw/images/why-your-ai-agent-demo-breaks-in-production-and-the-4-layer-fix
stills_count: 33
extractor:
  method: hand-picked (no Gemini call)
  reason: Gemini API returned 402 (prepayment credits depleted)
  sampling: 330 frames from the 360p copy (27:31), one every 5 s, consecutive repeats merged into 321 tiles, read as 6x8 contact sheets; ffmpeg scene detection found 55 cuts, of which 1 shot shorter than 10 s fell between grid frames (the closing logo card at 27:25, 6 s) and got its own tile
  dense_pass: 1 frame per second from the 360p copy in 12 windows, read as 6-column sheets, to find the fully built state of animated diagrams and overlay cards (0:55-1:19, 2:20-2:44, 2:50-3:02, 3:25-3:43, 3:52-4:04, 5:22-5:34, 7:58-8:10, 11:30-12:24, 15:12-16:48, 17:00-18:06, 18:15-19:03); speaker lower-thirds read at 1080p for names (not cut as stills)
  frames: yt-dlp stream URL (<=1080p) seeked with ffmpeg
acquired: '2026-11-23'
---

# Stills manifest (hand-picked)

Each still was chosen from the contact sheets and then read at full resolution; the readings below were made by viewing the pixels. Ten are published, cropped to the slide panel, overlay card or screen and converted to webp. The video is a produced explainer: six presenters on webcam, most with a slide panel beside them or an overlay card in the corner, plus screen recordings of GitHub, a terminal, a local web viewer and the Antigravity app. Talking-head stretches without graphics, the presenters' layer badges ("1: Learn … 4: Score", navigation), the progressive-disclosure stage labels (6:15–6:55, which repeat the narration's three words), intermediate build states and the closing logo card were reviewed and not cut.

Lower-thirds (read at 1080p, recorded in the transcript's `notes:`): Smitha Kolan, Sr. DevRel Engineer, Google Cloud (host); Logan Hennessy, DevRel, Google Cloud; Remigiusz Samborski, Lead Developer Relations Engineer, Google Cloud; Aron Eidelman, Security Advocate, Google Cloud; YK Sugi, Sr. DevRel Engineer, Google Cloud; Annie Wang, Software Engineer, Google Cloud.

## 01 · 1:03 · AI Stack
- File: `01-01m03-ai-stack.png` · [1:03](https://www.youtube.com/watch?v=BKVDdL1InsA&t=63s)
- Badge *Loop Engineering*; title *AI Stack*. Four layers, top to bottom: **Applications** (the finished app on top); **Harness** (software around the model · loops live here), outlined in red; **Models** (Gemini · Gemma); **Silicon**. **Published** (cropped to the slide panel): the narration names applications, harness and models but not the silicon layer, and only the slide says loops live in the harness.

## 02 · 1:18 · The harness
- File: `02-01m18-the-harness-while-loop.png` · [1:18](https://www.youtube.com/watch?v=BKVDdL1InsA&t=78s)
- *Loop engineering · The harness*: a `while loop` box around **Model** (Gemini) ⇄ **Tools** (CLI · files · MCP), arrows labelled *tool call* and *result*; footer *repeats until the task is done*. **Not published**: the narration says the same (*"equip it with tools like a command line, file system access, or MCP servers, and wrap it in a while loop"*).

## 03 · 1:52 · Context map
- File: `03-01m52-context-map.png` · [1:52](https://www.youtube.com/watch?v=BKVDdL1InsA&t=112s)
- *Layer 1 · Learn — 1. Context map*: **Massive manual** (goes out of date), crossed out → **Repo structure** under an `AGENTS.md` tab; the caption *where to look next* is still fading in. **Not published**: build state, and the narration says it word for word.

## 04 · 2:07 · Persistent memory
- File: `04-02m07-persistent-memory.png` · [2:07](https://www.youtube.com/watch?v=BKVDdL1InsA&t=127s)
- *Layer 1 · Learn — 2. Persistent memory*: Run 1 → `plan.md` (Done, Failed), Run 2 to the right; *On disk*. The third item, *Next*, visible on the 360p grid, is not drawn in this frame. **Not published**: narration word for word.

## 05 · 2:26 · Modular skills
- File: `05-02m26-modular-skills.png` · [2:26](https://www.youtube.com/watch?v=BKVDdL1InsA&t=146s)
- *Layer 1 · Learn — 3. Modular skills*: *Skills on disk* (Cloud Run, highlighted; IAM; SQL) → *Loaded on demand* → **Context window**. **Not published**: narration word for word.

## 06 · 2:33 · Learn
- File: `06-02m33-learn-map-memory-skills.png` · [2:33](https://www.youtube.com/watch?v=BKVDdL1InsA&t=153s)
- *Layer 1 · Learn*: 1. Map, 2. Memory, 3. Skills, each arrowed into **Context window**. **Not published**: narration word for word.

## 07 · 2:57 · Guard
- File: `07-02m57-guard-deterministic-checks.png` · [2:57](https://www.youtube.com/watch?v=BKVDdL1InsA&t=177s)
- *Layer 2 · Guard*: a ring of **Deterministic checks** around the `while loop` model, with three green ticks: Compiles, Unit tests, Module boundaries. **Not published**: the narration names the same three checks.

## 08 · 3:33 · Review
- File: `08-03m33-review-fresh-reviewer-human-sign-off.png` · [3:33](https://www.youtube.com/watch?v=BKVDdL1InsA&t=213s)
- *Layer 3 · Review*: **Coding agent** → **Fresh reviewer agent** (Code diff; UI visuals) → **Human sign-off**. **Not published**: narration word for word.

## 09 · 3:58 · Score
- File: `09-03m58-score-diagnostic-test-bench.png` · [3:58](https://www.youtube.com/watch?v=BKVDdL1InsA&t=238s)
- *Layer 4 · Score — Diagnostic test bench*: a gauge tagged *Evaluates the harness*, fed by Agent file, MCP tool, New model. **Not published**: narration word for word.

## 10 · 5:07 · Overloaded context
- File: `10-05m07-overloaded-context.png` · [5:07](https://www.youtube.com/watch?v=BKVDdL1InsA&t=307s)
- *The problem — Overloaded context*: **50 pages of docs** → **Context window** (red, bursting) → **Worse coding**. **Not published**: narration word for word.

## 11 · 5:28 · Agent Skills, open specification
- File: `11-05m28-agent-skills-open-specification.png` · [5:28](https://www.youtube.com/watch?v=BKVDdL1InsA&t=328s)
- Overlay card: **Agent Skills** — *Open specification*; *Supported across*: Claude Code, Codex, Antigravity, *+ most coding harnesses*. (At 5:15–5:22 the same card carries the tag *Open-sourced: December 2025*, checked at 1080p; the narration gives the same date.) **Not published**: narration word for word.

## 12 · 5:52 · Inside a skill
- File: `12-05m52-inside-a-skill.png` · [5:52](https://www.youtube.com/watch?v=BKVDdL1InsA&t=352s)
- *Agent Skills — Inside a skill*: a `SKILL.md` file with **Metadata** (When to use it) above **Instructions** (How to do the job). **Not published**: narration word for word.

## 13 · 8:09 · Antigravity: Customizations marketplace
- File: `13-08m09-antigravity-build-with-google.png` · [8:09](https://www.youtube.com/watch?v=BKVDdL1InsA&t=489s)
- Screen recording of the Antigravity app, *Customizations* page, *Marketplace* tab (Remigiusz Samborski in a picture-in-picture circle). Entries, each with an add button, descriptions truncated on screen: Science (*Curated collection of agent skills for scien…*), Google Antigravity SDK (*Using the Google Antigravity Python SDK t…*), Google Developer Knowledge (*Search and retrieve official documentatio…*), Modern Web Guidance (*Keep your coding agent up to date with th…*), Google Maps Platform (*Integration skill and tools for Google Maps…*), Dart and Flutter (*Official plugin for Dart and Flutter that inst…*), Data Agent Kit (*This plugin provides a specialized suite of …*), Google Cloud Developer (*Google Cloud guidance for coding agents:…*, under the cursor), Elephant-Goldfish Model (*Develop ideas with context and review do…*). The frames at 7:58–8:07 (checked at 1080p) show the empty chat (*Hey Remigiusz, what should we build today?*, model selector *Gemini 3.8 Flash Medium*), a featured Firebase card, a *Google Workspace* section (Google Docs, Sheets, Slides, Drive, Calendar) and the top of the *Build with Google* section (*"Build on Google's developer platforms, including Android, Chrome, Gemini, and Google Cloud"*): Gemini API, Chrome DevTools, Android CLI, Firebase. **Published** (border cropped): the narration names only the Google Cloud Developer plugin and the click path; the screen shows it as one entry in a marketplace of Google plugins and skill collections.

## 14 · 9:47 · Deterministic checks
- File: `14-09m47-deterministic-checks.png` · [9:47](https://www.youtube.com/watch?v=BKVDdL1InsA&t=587s)
- Overlay card *Layer 2 · Guard — Deterministic checks — Same result, every time*: Compilers; Type checkers; Test suite with fixed inputs; Lint rules; Secret scanners; Source component analysis; Security tests based on defined rules. **Not published**: the narration lists the same seven, in the same words (including *source component analysis*).

## 15 · 10:02 · Why it matters
- File: `15-10m02-why-it-matters.png` · [10:02](https://www.youtube.com/watch?v=BKVDdL1InsA&t=602s)
- Overlay card *Why it matters — for agents*: **Cheaper than tokens** (Fast to run on every loop); **Clear feedback** (Exactly where it broke: file, line number, error message). **Not published**: narration word for word.

## 16 · 10:42 · The new test has to fail first
- File: `16-10m42-new-test-must-fail-first.png` · [10:42](https://www.youtube.com/watch?v=BKVDdL1InsA&t=642s)
- *Execution with small, test-first commits — The new test has to fail first*: New test → **Run it before writing code** → **Fails** (Good: now write the code) or **Passes right away** (Not testing anything new: kick it back). **Not published**: narration word for word.

## 17 · 10:52 · Small, test-first commits
- File: `17-10m52-small-test-first-commits.png` · [10:52](https://www.youtube.com/watch?v=BKVDdL1InsA&t=652s)
- *Execution with small, test-first commits — Tiny red → green → refactor steps*: **Plan** (Articulate the design and divide into stages) → Stage 1, Stage 2, Stage 3, each Red → Green → Refactor; footer *Small commits: if something breaks, you know exactly what caused it*. **Published** (cropped to the slide panel): the planning step that precedes the stages is on the slide only.

## 18 · 12:14 · When a gate fails
- File: `18-12m14-when-a-gate-fails.png` · [12:14](https://www.youtube.com/watch?v=BKVDdL1InsA&t=734s)
- Overlay card *Layer 2 · Guard — When a gate fails — Send the raw error log back*: `gate · tests · FAILED`; Rule ID `tenant-filter-required`; File `api/invoices.py`; Line number `87`; Failing assertion `assert status == 403` → **Straight back to the agent**. (A first cut at 12:13 caught the assertion half drawn; re-cut at 12:14.6.) **Published** (cropped to the card): the narration lists the fields; the card fills them with a worked failure, a tenant-isolation rule failing on an HTTP 403 check.

## 19 · 12:21 · Retry limit: 3
- File: `19-12m21-retry-limit-three.png` · [12:21](https://www.youtube.com/watch?v=BKVDdL1InsA&t=741s)
- Overlay card *Retry limit: 3 — Then stop and hand it over*: *The agent retries with the log*: Attempt 1 ✕, Attempt 2 ✕, Attempt 3 ✕ → **Hand it to a human** (with the log attached); *No infinite retry loops: they waste time and tokens*. **Not published**: narration word for word.

## 20 · 15:27 · One-shot AI code review on a merged PR
- File: `20-15m27-one-shot-ai-code-review.png` · [15:27](https://www.youtube.com/watch?v=BKVDdL1InsA&t=927s)
- GitHub, `github.com/GoogleCloudPlatform/devrel-demos/pull/1567`: **Merged — Add repo-walkthrough #1567**, *ykgl merged 2 commits into main from add-repo-walkthrough*. `gemini-code-assist` (Bot) *reviewed on Oct 9* and left a comment, **Code Review**: *"This pull request adds the `repo-walkthrough` agent skill, enabling the generation of interactive codebase architecture graph websites and voice-narrated MP4 walkthrough videos. It includes repository analysis, a build pipeline, Gemini TTS audio generation, video rendering, and an interactive web viewer, backed by automated tests. The review feedback provides valuable recommendations to enhance robustness and security: sequentially executing acoustic alignment in `generate_live_audio.mjs` to avoid API rate limits, URL-encoding branch names and file paths in `fetch_repo.py` to handle special characters, using robust regex for `.env` parsing, and hardening input validation in `index.html` against Local File Inclusion (LFI) vulnerabilities."* Below it, five inline threads on `agents/repo-walkthrough/scripts/generate_live_audio.mjs` and `fetch_repo.py`, each marked *Resolved*. **Published** (border cropped): the narration describes one-shot review in general; the screen shows the bot, the PR and the kind of findings it returns.

## 21 · 16:12 · Antigravity CLI with the PR link
- File: `21-16m12-terminal-gemini-hydrogen.png` · [16:12](https://www.youtube.com/watch?v=BKVDdL1InsA&t=972s)
- Terminal: **Antigravity CLI 1.5.9**, *(Agent Platform)*, a GCP project id, model *Gemini 4 Carbon (Low)*; a banner *Introducing Gemini 4 Hydrogen — Our daily driver for rapid coding and dependable agentic execution!* with a docs link on model availability; prompt holding `https://github.com/GoogleCloudPlatform/devrel-demos/pull/1567`; status line *Gemini 4 Carbon (Low) | yksu | 0% of 1M tokens*. **Not published**: the frame shows a staff account e-mail and project id; the product and model names are recorded here and on the source page.

## 22 · 17:32 · repo-walkthrough visualizer
- File: `22-17m32-repo-walkthrough-visualizer.png` · [17:32](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1052s)
- Local web page (`localhost:8794/index.html`): **PR #1567: Add repo-walkthrough** — *GoogleCloudPlatform/devrel-demos · 24 files added (+11,150 / -0) · Diff Walkthrough*. A five-band graph of the added files with line counts: *Skill & docs entry* (README.md +83 Quickstart & Skill Install; SKILL.md +104 Agent Skill Workflow; data-schema.md +96 5-Layer Grid & Cue Spec); *Diff & build engine* (fetch_repo.py +715 Repo & Git Diff Analyzer; build_walkthrough.mjs +361 Geometry & Cue Builder); *Interactive graph UI* (web/index.html +1506 SVG Graph & Diff Viewer; web/data-adk.js +470 Default ADK Graph Preset); *TTS audio & MP4 video* (generate_live_aud… +502 Gemini TTS & WAV Cache; render_video.mjs +341 24fps Chromium → FFmpeg; render_video.sh +19 Video CLI Entrypoint); *Examples & test suite* (cymbal…/dat… +433 Monorepo Subpath Example; diff-5984e02… +364 Git Diff Mode Example; test_pipeline… +327 Schema, TTS & Fetch Tests; test_ui_e2e.m… +740 Playwright Geometry & MP4). Caption panel *STEP 1 / 6 — PR #1567 Overview: Adding agents/repo-walkthrough (+11,150 Lines)*, with player controls and speeds 0.8×–1.2×; the diff of the README on the right. **Published** (border cropped): the narration describes the layers in passing; the screen shows the tool's output and the size of the PR under review.

## 23 · 18:34 · Six Gemini 4 Hydrogen critics
- File: `23-18m34-hydrogen-critics-watch.png` · [18:34](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1114s)
- Slide *6 Gemini 4 Hydrogen critics watch*: phone, tablet and desktop recordings of a 3D cycling game each fan out to two critics (video, stills). **Not published**: superseded by still 24, which shows the same six critics and what follows them.

## 24 · 18:42 · Gemini 4 Carbon merges the bug reports
- File: `24-18m42-carbon-merges-bug-reports.png` · [18:42](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1122s)
- Slide *Gemini 4 Carbon merges the bug reports*: six **Gemini 4 Hydrogen** critics (Phone video, Phone stills, Tablet video, Tablet stills, Desktop video, Desktop stills) → **Gemini 4 Carbon** (*Merges 6 reports*) → Fix 1 *Top bar covers the score*; Fix 2 *Dock covers the radar*; Fix 3 *Top bar blocks UI text*. **Published** (border cropped): the narration says critics watch videos and screenshots and report to a *"main thread"*; the slide names the two models, the six critic inputs and the three fixes.

## 25 · 18:47 · Fix 1: top bar covers the score
- File: `25-18m47-fix-top-bar-covers-score.png` · [18:47](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1127s)
- Slide *Fix 1 Top bar covers the score*: Before (*Bar overlaps card, hides 0% label*) and After (*Card clear, 0% label visible*) on a game HUD (*0 / 16 TPU 8i*, *Gradient Canopy*, Director, X-Ray). Fix 2 (*Dock covers the radar*) and Fix 3 (*Top bar blocks UI text*) follow at 18:48–18:55 in the same layout. **Not published**: still 24 names all three fixes; one before/after adds little to it.

## 26 · 19:02 · Hydrogen catches more UI bugs
- File: `26-19m02-hydrogen-catches-more-ui-bugs.png` · [19:02](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1142s)
- Slide *Hydrogen catches more UI bugs*: **Gemini 4 Hydrogen 26 of 33 (79%)**; **Gemini 3.8 Flash 23 of 33 (70%)**. Footnote: *"Internal test: 33 real UI bug checks on internal apps, median of 3 runs, scored by 3 blinded judges. Results may vary."* **Published** (border cropped): the comparison and its method are not spoken.

## 27 · 23:12 · Pattern 1: tool use
- File: `27-23m12-pattern-1-tool-use.png` · [23:12](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1392s)
- *Pattern 1: Tool use — Like a unit test for an agent's actions*: agent → *Mocked tools · sample data*: 1 `check_eligibility` (`order_id: 101`) → 2 `issue_refund` (`order_id: 101`); ticks: Right tool (the one the task needs), Right inputs (exact order ID), Right order (eligibility before refund). **Not published**: narration word for word.

## 28 · 24:17 · Pattern 2: outcome
- File: `28-24m17-pattern-2-outcome.png` · [24:17](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1457s)
- *Pattern 2: Outcome and trajectory — Same test, different replies*: *refund order 101* → agent → Run 1 *"Your refund is done."* ≠ Run 2 *"I've refunded order 101."*; Exact match (word for word) ✕; Similarity (close to the expected answer) ✓; Refund policy (followed it) ✓. **Not published**: narration word for word.

## 29 · 24:37 · Pattern 2: trajectory
- File: `29-24m37-pattern-2-trajectory.png` · [24:37](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1477s)
- *Pattern 2: Outcome and trajectory — Trajectory: how it got there, step by step*: agent → *Trace*: 1 `lookup_order` (`order_id: 101`) → 2 `check_eligibility` → 3 `issue_refund`; ticks: Exact sequence (tool calls match), Required order (eligibility before refund). **Published** (cropped to the slide panel): the trace has a third call, `lookup_order`, before the two of pattern 1, and the slide shows two trajectory checks where the narration also offers LLM-as-judge.

## 30 · 25:37 · Pattern 3: single-turn vs. multi-turn
- File: `30-25m37-pattern-3-multi-turn.png` · [25:37](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1537s)
- *Pattern 3: Single-turn vs. multi-turn*: single-turn *"I'm Annie. Refund order 101."* → agent → reply ✓; multi-turn 1 *"I'm Annie. I want a refund."* 2 *"Order 101."* 3 *"Wait, order 202!"* → *Memory*: Annie · refund, ~~order 101~~ **order 202**; ticks Remembers Annie, Keeps the request. **Not published**: narration word for word.

## 31 · 26:38 · Pattern 4: workflow handoffs
- File: `31-26m38-pattern-4-workflow-handoffs.png` · [26:38](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1598s)
- *Pattern 4: Workflows and multi-agent systems — Workflows: test the handoffs between code and agents*: `load_order` (code) → *Data in* handoff ✓ → agent → *Data out* handoff ✓ → `issue_refund` (code). **Not published**: narration word for word.

## 32 · 26:52 · Pattern 4: multi-agent handoffs
- File: `32-26m52-pattern-4-multi-agent-handoffs.png` · [26:52](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1612s)
- *Multi-agent: test agent-to-agent handoffs*: agent → `Annie · order 202` → **refund agent** ✓, with billing agent and shipping agent greyed; ticks Right specialist (Level 1 · who gets the task), Right information (Level 2 · order 202, not 101). **Published** (cropped to the slide panel): the narration gives the two levels but not the specialists the router chooses between.

## 33 · 27:07 · Pattern 4: end to end
- File: `33-27m07-pattern-4-end-to-end.png` · [27:07](https://www.youtube.com/watch?v=BKVDdL1InsA&t=1627s)
- *Then zoom out: end to end*: first message *"Hi, I'm Annie. I want a refund."* → *The whole system* (code → agent → agent → code) → **Refund done** (order 202, *completed refund*); tick End to end (the whole system works together). **Not published**: narration word for word.
