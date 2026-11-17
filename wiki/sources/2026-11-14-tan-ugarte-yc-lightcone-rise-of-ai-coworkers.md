---
type: source
kind: video
title: "The Rise Of AI Coworkers"
author: ["Y Combinator"]
publisher: "Y Combinator (YouTube channel), Lightcone podcast; hosts Garry Tan, Diana Hu and Jared Friedman (named in the closing credits; only Garry Tan is named in the transcript); guests Lauren Tan and Roman Ugarte, who incubated Grok Bot and are on its core team"
url: "https://www.youtube.com/watch?v=y1-9yeYLJUo"
date_published: 2026-11-14
date_ingested: 2026-11-16
length: "~1:00:06 (transcript ~475 lines + 6 stills; ASR auto-generated track, 16 chapters)"
raw: "../../raw/videos/the-rise-of-ai-coworkers.md"
stills: "../../raw/videos/the-rise-of-ai-coworkers.stills.md"
tags: [y-combinator, lightcone, grok-bot, lauren-tan, roman-ugarte, garry-tan, ai-coworkers, ai-teammates, team-bots, bot-identity, agent-permissions, scoped-credentials, trust-ladder, bot-to-bot-communication, slack, quartermaster, moltbook, abliterated-models, agentic-pull-requests, self-merging-agents, pstack, gstack, software-factory, outer-loop, agents-check-own-work, inverted-pyramid, static-analysis, lint-rules, code-review-token-cost, electron, cursor-cloud-agents, cursor-projects, execution-abundance, intent-specification, product-judgment, internal-product-market-fit, jack-dorsey, player-coach, podcast]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - strategic-renewal/collaborative-approach
relationships:
  - type: supports
    target: 2026-09-07-yc-paper-club-why-the-harness-matters-more-than-the-model
    via: "both describe Slack-resident agents for a whole company: the Paper Club's QM segment describes YC's open-source harness, an agent with 'no social context' about where information may go, and a brain 'bounded by how good your permission system is'; here a YC host describes YC's Quartermaster inheriting each user's per-channel permissions, and the guests describe bots that do not know whom to listen to in a shared thread"
    confidence: 0.75
  - type: supports
    target: 2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook
    via: "both address agents used by teams in the open: Koomen describes YC broadcasting every agent conversation to an internal channel; Ugarte and Lauren Tan describe team bots shared across functions and agent work in public Slack threads that colleagues copy. Both are YC Lightcone episodes"
    confidence: 0.7
  - type: supports
    target: 2026-02-11-lopopolo-codex-harness-engineering
    via: "both address mechanically enforced codebase constraints for agent-written code: Lopopolo's team enforces layer dependency directions with custom linters in a five-month, ~1,500-PR build; Lauren Tan describes a dependency-graph checker that forbids imports between Electron's main and renderer threads, and an 'inverted pyramid' that puts codebase and static analysis before review"
    confidence: 0.8
  - type: supports
    target: 2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot
    via: "both address how much review agent-written pull requests get: Vo scores each PR on six risk dimensions and auto-approves the low band; Lauren Tan lets her agents merge their own PRs, keeps human review for infrastructure, databases and deployment, and moves review effort into the codebase"
    confidence: 0.7
  - type: supports
    target: 2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack
    via: "both describe personal skill sets for coding agents: Garry Tan's GStack, and Lauren Tan's PStack, which she says GStack inspired; here Garry Tan also reports the token cost of GStack's review skill. Garry Tan hosts this episode, so the two are not independent"
    confidence: 0.65
---

# Tan and Ugarte on YC's Lightcone — The Rise of AI Coworkers

> Lauren Tan and Roman Ugarte join this episode of the Lightcone to go in deep on how they built and deployed Grok Bot. They explain how automated tests and codebase guardrails help agents check their own work, why bots should earn broader access over time, and why faster and cheaper execution makes direction and clear goal setting even more important.
>
> *— Channel description, Y Combinator*

## TL;DR

A one-hour episode of [[Y Combinator]]'s *Lightcone* podcast. The guests, Lauren Tan and Roman Ugarte, incubated **Grok Bot**, a product for creating "AI teammates", and took it *"from the first line of code to launch in just seven weeks."* [[Garry Tan]] is the only host named in the transcript. Below, "Tan" alone means Lauren Tan. **Auto-generated transcript with no speaker labels**: attribution is inferred from context, and names are corrected in quotation only: the product's many ASR spellings ("Grockbot", "Grabbot", "GraphBot", "Crockpot", "graphite") → Grok Bot; "light cone" → Lightcone; "Kursa" → Cursor; "PAC", "peace stack" → PStack; "GSAC", "Gack" → GStack; "Gary" → Garry; "Maltbook" → Moltbook; "obliterated" → abliterated; "DRRI" → DRI; "lit rules" → lint rules; "quarter master" → Quartermaster.

What it adds to the wiki:

1. **A product built on the AI-coworker framing.** Work is organised around bots; each has its own computer, identity and credentials, and is *"always on."* The permissions rule is *"what would you do for a human?"*
2. **A three-step trust ladder:** read-only bots, then bots that act end to end, then bots that own a job, which Ugarte says *"we're still quite far away from."*
3. **One engineer at about 4,000 PRs a month**, with agents merging their own PRs. Tan credits an "inverted pyramid" that puts the codebase, static analysis and lint rules ahead of skills and a little human review.
4. **The smallest loop.** An agent that runs its code like a user can check its own work. That gives correct code, she says, not necessarily good code.
5. **A token cost for AI review.** Garry Tan's GStack review skill uses tens of millions of tokens a run.
6. **Product alignment as the constraint** once execution is cheap, with an *"internal product market fit"* gate on user-facing changes.

The guests describe their own product on YC's channel, every figure is self-reported, and Tan works with *"unlimited tokens"* at a lab.

## What Grok Bot is

Grok Bot began as an internal prototype built *"in about seven weeks"* to ask what long-running agents would look like *"for non-engineers... for the rest of the company."* Ugarte gives three design rules (1:54–2:43): work *"organized around bots as the key operative principle, not around chats or around files"*; bots with the tools a person has, including *"their own computer"* (*"we don't work every day with MCPs"*); and bots that are *"always on"* and bring you ideas unprompted. A host notes it is now built into the default DMs on X. Tan's goal for 2027 is bots with *"their own identity, their own telephone number, credit card, like basically almost anything a human can do"* (34:06).

The narration does not say which company makes Grok Bot. The only company name on screen is in the title of a sales diagram Tan shows from *"our Grok Bot blog"*: *"How the SpaceXSI Sales team uses Shared Bots"* (12:30, see [Visual canon](#visual-canon)). The guests mention *"our model teams and harness teams"* and *"working at a lab"*, and speak of [[Cursor]] in the first person (*"one of the lessons we learned from building Cursor"*). This page does not infer a corporate structure from that.

## Bots with real jobs, and how many

Ugarte describes adoption that moves with trust: from a task to *"an outcome or an objective"* to *"a full job"* (4:00). The performance-marketing team gave its bot its own logins to Google Ads and Facebook Ads and a budget, and had it A/B test assets made by the design team's bot. A host says small businesses, *"the ones who struggle the most with hiring,"* set up a bookkeeping bot *"within the course of probably hours."* Tan uses Grok Bot as her *"outer loop"*: bots sit in the Slack thread where bug reports and feature requests arrive, so she no longer pastes that context into her coding agents by hand.

Ugarte prefers a small team of specialists, each *"solely dedicated to caring about a particular thing,"* to *"one superstar superhuman person who simultaneously cares about a hundred things"*: *"I want it to be managed by the domain expert at the company who knows the most about that problem so that they can kind of treat it like an apprentice"* (10:12). That is `digital-transforming/redesigning-internal-structures` at team level: the bot joins the organisation as a member with an owner and a remit. **Team bots**, launched two weeks before recording, let one person build a bot and share it; the builders include *"GTM engineers or support engineers."* A host credits [[Steve Yegge]]'s Gas Town with starting "software factories" and calls their extension to other functions *"an everything factory."*

## Identity, permissions and the trust ladder

In a shared Slack thread a bot *"doesn't really know who to listen to... who has decision-making power. It's as if you were to onboard an employee who has no EQ... Just the models weren't trained that way. The harness wasn't built that way"* (15:11). The fix has to come at product, [[agent-harness|harness]] and model level. Each bot has an owner, a manager and invited collaborators.

On permissions Ugarte says *"I don't think anyone has the silver bullet answer yet,"* and gives the team's heuristic: *"You hire a person, you give them a computer. You give them access to credentials. You maybe scope those credentials based on their role, maybe how new they are. As they build more trust, you maybe expand their access level"* (16:40). A YC host describes YC's own open-source project, Quartermaster, which inherits the user's permissions in each Slack channel: *"me as a GP has certain access as opposed to, let's say, a software engineer."* [[2026-09-07-yc-paper-club-why-the-harness-matters-more-than-the-model|YC Paper Club's harness night]] describes YC's open-source Slack harness under the name QM and covers the same two topics: an agent with *"no social context,"* and a brain *"bounded by how good your permission system is."* QM and Quartermaster are probably one project; neither source says so.

The ladder, in Ugarte's account (21:20–22:29):

| Step | What the bot may do | Example |
| --- | --- | --- |
| 1 | Read only | Databot, with read access to the database, answering ad-hoc analysis requests in Slack; a vendor-procurement bot |
| 2 | Act, and complete a task end to end | none given |
| 3 | Own *"an entire job responsibility"* | *"we're still quite far away from those"* |

[[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees|Kropp et al.]] measure, in a 1,261-manager experiment, how calling an agent an AI teammate changes managers' accountability and error-catching; this episode describes a product designed around that label. Bots holding logins, budgets and card numbers fall within [[attack-surface-management]]; the episode discusses scoping and gradual trust and no other controls. See [[agent-oversight-and-delegation]].

## Bot-to-bot communication

Bots have *"a first-class tool"* to chat, and users can read it. Tan told a lead engineer bot to supervise her other engineer bots and found it relaying her feedback *"kind of like a disciplinarian."* A host describes a chat system for YC's coding agents, *"like an internal Stack Overflow"* where bots talk *"without any human prompting them,"* and calls it *"Moltbook internally at YC."* Tan's answer to the risk is visibility: her bots talk in Slack under their own identities, and agents given *"a first class way"* to communicate will use it *"rather than try to do something like back channeling."* A host worries more about abliterated models, which *"won't refuse"* malicious instructions. Neither gives data; see [[multi-agent-failure-modes]].

## 4,000 pull requests a month

A host recalls that Tan shipped *"about 2,000 plus PRs per month"* at an earlier talk and is *"now over 4,000."* Her demo (23:18–25:37): in a public Slack channel she asked her bot what a feature seen on X would take. The bot spawned a Cursor cloud agent with *"its own virtual machine,"* which ran the app and returned videos and screenshots. She, a colleague and a PM iterated in that thread, about 200 messages, and shipped: *"I didn't even look at Cursor for this project."* Getting there *"took us actually quite a while"*: review time is *"encoded into your codebase and your static analysis and your tooling,"* and *"I essentially have my agents merge their own pull requests."* In this case she did not read the PR; *"we just looked at the artifact"* (26:48). The [[2026-02-09-li-aidev-studying-ai-coding-agents-on-github|AIDev dataset]] counts 932,791 agent-authored PRs across 116,211 public repositories; Tan's figure is one engineer's month, with no revert or defect rates. See [[agentic-pull-requests]].

Her skills live in PStack (*"potato stack"*), open-sourced on the Cursor plugins repository, which *"teaches agents how to do engineering work rigorously the same way that I did when I was writing code."* She names Garry Tan's GStack ([[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|his April 2026 talk]]) as the inspiration, a personal set of *"chef knives."* Garry Tan describes his software factory, Cappy: a captain agent over *"10 or 15 threads working all the time"* that learns from his transcripts *"when do I intervene, when do I say just do it."*

Ugarte notes that agent work has moved into Slack, so colleagues copy it: *"the next day I see someone who was in that thread do the same thing,"* and the company is *"lifted up by the top 1% power users."* That is `digital-transforming/improving-digital-maturity`, leveraging digital knowledge inside the firm through imitation. [[2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook|Koomen's earlier Lightcone episode]] covers the same topic at YC, which broadcasts every agent conversation to an internal channel. A feature built by an engineer, a PM and bots in one thread, and marketing and design bots passing work between teams, are the episode's `strategic-renewal/collaborative-approach` material: cross-team work carried by shared bots and shared threads.

## The smallest loop, review, and the inverted pyramid

Tan's minimal loop (40:17–42:46): *"teach your agent to run the code empirically, take CPU traces, performance metrics, run the application like a real user would,"* so it *"has the ability to check its own work."* The result *"certainly will be correct,"* but *"maybe it's like very slow or very resource inefficient"*; *"the new job of a software engineer"* is getting agents to write good code by default. An outer loop follows: an alert fires a bot or a Cursor automation that reproduces and fixes the issue. With Cursor's new projects feature a coordinator agent runs sub-agents: *"I don't even manage the project myself anymore."* See [[agentic-engineering]] and [[agent-fleet-management]].

**How much review.** GStack's ship skill *"always consumes like tens of millions of tokens,"* Garry Tan says (43:37). He wants 10 million; his agent has come down from 50 to 30 million and, citing held-out evals on 30 bug types, will go no lower. Tan has *"tried to downplay some of the review skills."* Cross-model adversarial review risks overfitting, because the reviewer may lack *"enough judgment to determine what's actually good feedback"* and *"complete knowledge of your goals... your wider product vision."* [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Vo's Merge Mommy]] addresses the same question at the merge gate, scoring each PR on six risk dimensions. [[2026-10-24-skidmore-cloudflare-connect-build-not-buy|Skidmore]] reports a median $0.67 per AI review at Cloudflare, a cost in different units on a different workload.

**The inverted pyramid** (45:52–48:14), *"not a very scientific chart"*: most effort into the codebase (architecture, API design), then static analysis, then rules and skills (`AGENTS.md`), then *"a little bit of human review,"* kept for *"infrastructure or databases, deployment."* *"Your codebase is a form of memory,"* and lint rules and compilers that helped humans write good code *"also help agents."* Her example: on Electron, a task over 8–16 ms on the renderer thread breaks 60 fps, so *"we'll actually build it as like a lint rule"*: a dependency-graph checker forbids imports between main and renderer code, *"tokens I don't have to spend anymore."* She says the app's performance has *"stayed very consistent,"* while majority-AI-written apps *"accumulate a lot of slop and performance problems"*, without measurements. [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo's Codex team]] also enforces dependency directions with custom linters, over about 1,500 PRs. See [[ai-generated-code-quality]].

## Execution abundance, and product judgment as the constraint

Ugarte separates code from other work (35:34): code *"compiles or it doesn't and it passes CI or it doesn't,"* and its context lives in a codebase, while elsewhere it is *"stuck in people's heads... stuck in pen and paper."* A host cites Jack Dorsey's three roles for Block: IC, DRI, and a *"player coach"* who teaches everyone, *"which I think might be just temporary."* [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu's Startup School talk]] also attributes three roles to Dorsey, the third named "AI founder type." Ugarte: *"the gap is probably not going to be an execution failure. It will probably be an intent specification failure or a goal failure,"* and companies must decide *"what those KPIs are... who's responsible for defining those things"* as they *"shift to execution abundance."* See [[spec-driven-development]].

On his own team (52:20–55:02) the bottleneck is *"alignment... what do we want the product roadmap to be?"* Someone in a planning discussion often says *"Oh, I have a PR for that,"* and merging it all would give *"a bit of a Frankensteiny product."* Two paths result. Sandy, a pipeline Tan built, takes in *"thousands of pieces of customer feedback every day"* and *"just fixes it, like repros, fixes, merges... It goes out automatically at 3 in the morning."* Changes to *"the core pixels"* get dogfooding and a gate: *"Even if it gets like mixed internal product market fit, we don't ship it."*

The seven-week build and the in-thread prototype are `digital-seizing/rapid-prototyping`. The internal-PMF gate and the refusal to merge every PR are `digital-seizing/balancing-digital-portfolios`, setting an appropriate speed of execution when building is fast. Tan points her own factories at maintenance (performance, bugs, quality of life), not features, because for software used by humans, *"human judgment and taste"* should shape it.

## Lauren Tan's route in

Tan grew up in Singapore and studied accounting and finance in Australia; an Excel and VBA course showed her she preferred building the macros. After a startup, she blogged about learning Ember, was invited by Tom Dale and Leah Silber to speak at a conference in Portland, and later worked on the React compiler. She credits posting on X.

## Visual canon

### 1 · Three shared sales bots and the hand-offs between them

![[assets/2026-11-14-tan-ugarte-yc-lightcone-rise-of-ai-coworkers/01-12m30-loops-for-sales-shared-bots.webp|Loops for sales, three shared bots in the deal cycle]]

*Still at [12:30](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=750s) from Y Combinator, "The Rise Of AI Coworkers".*

Heading: **loops for sales**. Title: *"How the SpaceXSI Sales team uses Shared Bots to automate the deal cycle"*.

| Bot | Remit |
| --- | --- |
| Account Intel Bot | Account research, meeting prep, and sales follow-up |
| Quote Bot | Pricing proposals, approvals, and order forms |
| Deal Bot | Special terms, deal review, and approvals |

Account Intel Bot *requests quotes* from Quote Bot; Quote Bot *escalates exceptions* to Deal Bot, which *returns approved terms*.

*Still vs. transcript:* Tan says the example comes from *"our Grok Bot blog"* and mentions a quote bot and a deal bot shared across the team; the diagram adds a third bot, each bot's remit, the hand-offs between them, and the team's name, "SpaceXSI Sales".

### 2 · The demo thread: request, scoping agent, recommendation

![[assets/2026-11-14-tan-ugarte-yc-lightcone-rise-of-ai-coworkers/02-23m20-slack-thread-grok-bot-canvas.webp|Slack thread in the grok-bot-canvas channel]]

*Still at [23:20](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=1400s) from Y Combinator, "The Rise Of AI Coworkers".*

Slack, *Thread in #grok-bot-canvas*:

- **Lauren Tan**, Oct 11th at 5:22 PM: *"@poteto what would it take for grok bot canvas to be able to support this? ie building arbitrary ui inside of the chat transcript, maybe through RSCs or something"*
- **poteto** (APP), 5:22 PM: *"Good question. I'm having a cloud agent go through how canvas and the transcript render today, then scope what inline agent-built UI would take. I'll post the writeup here."* Then: *"The cloud agent is running now: inline UI scoping agent. It's comparing a few ways to do it, like RSCs, a sandboxed iframe running agent-written code, a component schema the agent emits, or embedding canvas inline. It'll also cover sandboxing, how interactions get back to the agent, replay, and what Slack and mobile show instead. I'll post the recommendation and the smallest first slice here when it's done."*
- **A colleague** (named on screen), 5:40 PM: *"i do really like the idea of it rendering inline and not having the page preview"* / *"curious what poteto will say. although might be something to fast follow w/ and not ship for tuesday launch"*
- A later message, partly behind the picture-in-picture: *"… agent recommends bringing Glass's `visualize` feature to Grok Bot, not using RSCs or … one HTML fragment, and the transcript renders it fully inline in a sandboxed frame that can … network access. That's what @[the colleague] wanted, with no page preview to open first."*

*Still vs. transcript:* Tan says she gave her bot a video from X and asked what supporting such a feature would take; the thread shows the actual request (arbitrary UI inside the chat transcript), the four approaches the cloud agent was set to compare, the colleague's caution about a Tuesday launch, and the recommendation that came back: reuse Glass's `visualize` feature and render one HTML fragment inline in a sandboxed frame.

### 3 · The report that came back: a gated prototype and a security gap

![[assets/2026-11-14-tan-ugarte-yc-lightcone-rise-of-ai-coworkers/02b-23m56-prototype-done-and-security-gap.webp|The bot's report in the thread, prototype behind an off-by-default gate]]

*Still at [23:56](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=1436s) from Y Combinator, "The Rise Of AI Coworkers".*

Two later messages in the same thread, on screen for about a second while Tan scrolls:

- **poteto** (APP), Oct 11th at 6:54 PM, to the colleague: *"On it. The same cloud agent is building the prototype now, behind an off-by-default gate. It includes a new visualize tool, an inline sandboxed card in the transcript, and Glass's D3 runtime. It'll also add three.js if that fits cleanly. I'll post the draft PR here with a screenshot and video of a real agent turn once it's working."*
- **poteto** (APP), Oct 11th at 10:40 PM: *"The prototype works end to end: draft PR #1123299. It's behind the `sand_visualizations` gate, which is off by default. With it on, Grok Bot calls a new `Visualize` tool and the visual renders inline in the desktop transcript. Real agent turns produced an interactive D3 chart with hover tooltips and a three.js 3D scene with drag to rotate and camera tabs. Scrolling away and back reloads the visual from its saved copy with no layout jump, and Slack gets the title and summary as text."* Then, in bold: *"One security gap before the gate goes on for anyone:"* *"agent-written HTML in the frame can still reach an outside server over WebRTC. That can leak the user's public IP and anything typed into the visual, and the frame's no-network …"* (cut off at the frame's edge).

*Still vs. transcript:* Tan says the cloud agent would *"prototype and come back with videos and screenshots and then uh it actually did"*; the narration does not mention the draft PR, the off-by-default gate or the security gap. The frame shows the bot reporting all three, about four hours after the request, and naming the gap itself as the condition for turning the gate on. Found on a second pass over shots shorter than 10 seconds, which the 10-second contact sheets skipped.

### 4 · What came back: inline visuals running in the app

![[assets/2026-11-14-tan-ugarte-yc-lightcone-rise-of-ai-coworkers/03-24m00-thread-attachments-inline-visuals.webp|Thread attachments, inline D3 and 3D visuals in Grok Bot]]

*Still at [24:00](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=1440s) from Y Combinator, "The Rise Of AI Coworkers".*

Two screenshots posted to the thread (*2 attachments*), each a Grok Bot window with a dev chat named after the pull request:

- **Visualize D3 proof (inline visuals PR)**: the prompt *"Use your Visualize tool to show me an interactive D3 line chart of weekly active users for two teams over 12 weeks…"*, the chart rendered inline (Team A and Team B, W1–W12, tooltip at Week 8: Team A 210, Team B 158), and the reply *"Here's your interactive chart — hover anywhere to see both teams' numbers for that week, and click Team A or Team B in the legend to toggle its line on or off."*
- **Visualize 3D proof (inline visuals PR)**: *"On it — building the interactive 3D scene now."* A 3D desk with the tabs *Whole desk / Close-up of clamp / From underneath*, a legend (wood desktop 120 × 60 × 2.5 cm; black metal frame; crossbar 6 cm deep, 4 cm in from back; blue C-clamp on back edge), and a fit check: *"I drew the clamp's lower jaw reaching exactly 4 cm, so it just clears — but it's tight."*

Below them, a video attachment: *"…3D visuals in Grok Bot: interacting, scrolling past, and scrolling back"* (`demo.mp4`).

*Still vs. transcript:* Tan says the cloud agent ran the app and came back with *"videos and screenshots"*, and that the team *"just looked at the artifact"* rather than the PR; the still shows that artifact: the feature working in the app on test prompts, in chats labelled with the PR they came from.

### 5 · The smallest loop, and the alert that starts it

![[assets/2026-11-14-tan-ugarte-yc-lightcone-rise-of-ai-coworkers/05-42m00-smallest-loop-with-outer-loop.webp|The smallest loop with a Datadog alert feeding it]]

*Still at [42:00](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=2520s) from Y Combinator, "The Rise Of AI Coworkers".*

Hand-drawn cycle: **write good code → run the code → find issues with code → write good code**. Outside it: **datadog alert → repros → run the code**. The picture-in-picture covers the end of "find issues with code"; the label is read from the frame at 42:01.

*Still vs. transcript:* the narration builds the loop step by step from 40:17 and speaks of *"an alert for some metric or monitor"*; the drawing shows the whole as one figure, names Datadog as the alert source, and has the repro enter at "run the code", the step Tan says agents usually leave to the human.

### 6 · Where a correction should go: the inverted pyramid

![[assets/2026-11-14-tan-ugarte-yc-lightcone-rise-of-ai-coworkers/06-45m50-inverted-pyramid-whenever-you-correct-your-agent.webp|Inverted pyramid, whenever you correct your agent]]

*Still at [45:50](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=2750s) from Y Combinator, "The Rise Of AI Coworkers".*

Title: **whenever you correct your agent**. An inverted triangle in four bands, widest at the top:

1. codebase
2. static analysis
3. prose *(rules, skills, agents.md)*
4. human review

*Still vs. transcript:* Tan reads the chart as where an engineer should spend time; the title adds the trigger, a correction to the agent, and the bands group rules, skills and `agents.md` as one tier, "prose", below static analysis.

## Linked entities and concepts

- **Entities:** [[Y Combinator]] (channel; Quartermaster; the internal agent forum), [[Garry Tan]] (host; GStack, Cappy), [[Diana Hu]] (host, named in the closing credits), [[Cursor]] (cloud agents, projects, plugins repository), [[Steve Yegge]] (Gas Town).
- **Concepts:** [[agentic-engineering]], [[agentic-pull-requests]], [[agent-harness]], [[ai-generated-code-quality]], [[agent-oversight-and-delegation]], [[agent-fleet-management]], [[ai-agents]], [[multi-agent-failure-modes]], [[attack-surface-management]], [[spec-driven-development]].
- **Dangling** (single-source mention, deferred): Lauren Tan, Roman Ugarte, Grok Bot, Jared Friedman (host, named in the closing credits), Quartermaster, PStack, Cappy, Sandy, Moltbook (also in [[2026-02-03-loukides-radar-trends-february-2026|Loukides, Feb 2026]]), Jack Dorsey and Block (referenced in several YC sources, never as a subject), Tom Dale, Leah Silber.

The bots described here are [[ai-agents]] placed inside a company's chat and identity systems.

## Source quality

ASR track with no speaker labels; attribution among Tan, Ugarte and the hosts is inferred from content, and only Garry Tan among the hosts is named in the audio; the closing credits name Diana Hu and Jared Friedman as the other hosts. The page uses the channel description's spelling, "Grok Bot." The guests describe their own product on a YC channel, and every number is self-reported: seven weeks, 2,000+ then 4,000+ PRs a month, thousands of feedback items a day. Quality claims come without measurements, and there are no defect, revert or incident figures for self-merged PRs. Tan calls her position unusual: unlimited tokens, *"the explorer"* of engineering *"6 months to a year from now."* Six stills of what Tan shows on screen (a sales diagram, the demo thread, the bot's report and its attachments, and two drawings) were hand-picked from contact sheets of the whole video, plus a pass over its short shots, and read at full resolution; see [Visual canon](#visual-canon). The closing credits (59:50) list the hosts as Garry Tan, Diana Hu and Jared Friedman; the transcript names only Garry Tan, and this page does not attribute the other hosts' remarks.
