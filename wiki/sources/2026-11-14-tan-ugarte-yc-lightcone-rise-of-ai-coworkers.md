---
type: source
kind: video
title: "The Rise Of AI Coworkers"
author: ["Y Combinator"]
publisher: "Y Combinator (YouTube channel), Lightcone podcast; hosts Garry Tan and other YC partners (only Tan is named in the transcript); guests Lauren Tan and Roman Ugarte, who incubated Grok Bot and are on its core team"
url: "https://www.youtube.com/watch?v=y1-9yeYLJUo"
date_published: 2026-11-14
date_ingested: 2026-11-16
length: "~1:00:06 (transcript ~475 lines; ASR auto-generated track, 16 chapters)"
raw: "../../raw/videos/the-rise-of-ai-coworkers.md"
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

The episode does not say which company makes Grok Bot. The guests mention *"our model teams and harness teams"* and *"working at a lab"*, and speak of [[Cursor]] in the first person (*"one of the lessons we learned from building Cursor"*). This page does not infer a corporate structure from that.

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

## Linked entities and concepts

- **Entities:** [[Y Combinator]] (channel; Quartermaster; the internal agent forum), [[Garry Tan]] (host; GStack, Cappy), [[Cursor]] (cloud agents, projects, plugins repository), [[Steve Yegge]] (Gas Town).
- **Concepts:** [[agentic-engineering]], [[agentic-pull-requests]], [[agent-harness]], [[ai-generated-code-quality]], [[agent-oversight-and-delegation]], [[agent-fleet-management]], [[ai-agents]], [[multi-agent-failure-modes]], [[attack-surface-management]], [[spec-driven-development]].
- **Dangling** (single-source mention, deferred): Lauren Tan, Roman Ugarte, Grok Bot, the unnamed Lightcone hosts, Quartermaster, PStack, Cappy, Sandy, Moltbook (also in [[2026-02-03-loukides-radar-trends-february-2026|Loukides, Feb 2026]]), Jack Dorsey and Block (referenced in several YC sources, never as a subject), Tom Dale, Leah Silber.

The bots described here are [[ai-agents]] placed inside a company's chat and identity systems.

## Source quality

ASR track with no speaker labels; attribution among Tan, Ugarte and the hosts is inferred from content, and only Garry Tan among the hosts is named. The page uses the channel description's spelling, "Grok Bot." The guests describe their own product on a YC channel, and every number is self-reported: seven weeks, 2,000+ then 4,000+ PRs a month, thousands of feedback items a day. Quality claims come without measurements, and there are no defect, revert or incident figures for self-merged PRs. Tan calls her position unusual: unlimited tokens, *"the explorer"* of engineering *"6 months to a year from now."* What she shows on screen is known only from what is said about it.
