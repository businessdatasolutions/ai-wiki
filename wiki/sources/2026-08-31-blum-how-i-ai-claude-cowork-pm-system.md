---
type: source
kind: video
title: "I built a Claude Cowork system that does a week of PM work in a day"
author: ["How I AI"]
url: "https://www.youtube.com/watch?v=p2qmX6TM0kw"
date_published: 2026-08-31
date_ingested: 2026-08-31
length: "~46:08 minutes (transcript ~9,300 words / 360 ASR segments, 18 chapters; auto-generated transcript, ASR-cleaned for proper nouns)"
raw: "../../raw/videos/i-built-a-claude-cowork-system-that-does-a-week-of-pm-work-in-a-day.md"
tags: [how-i-ai, claire-vo, daniel-blum, melio, claude-cowork, claude-enterprise, notion, slack, granola, jira, workstation-plugin, personal-ai-infrastructure, context-engineering, self-improvement-loop, skills, plugins, morning-brief, weekly-prep, scheduled-tasks, chrome-connector, mcp, onboarding-ux, roi-j-curve, individual-ai-maturity, agent-harness, agentic-engineering]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-sensing/digital-mindset-crafting
  - digital-seizing/rapid-prototyping
  - digital-transforming/improving-digital-maturity
  - digital-transforming/redesigning-internal-structures
  - contextual/internal-enablers
  - contextual/internal-barriers
roles: [product-manager, transformation-lead, chro, cdo, innovation-lab-lead]
relationships:
  - type: supports
    target: 2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex
    via: "Same channel, same host, and an explicit in-episode citation: Blum runs Vo's designing-loops episode through his own Improve skill on camera, and the skill's verdict is that his scheduled tasks already *are* loops in Vo's taxonomy while he lacks her goal loops. Vo supplies the loop vocabulary; Blum supplies a non-engineer's production deployment of it (weekly prep = cron loop, morning brief = cron loop, self-improvement loop = weekly cron loop over the agent's own telemetry)."
    confidence: 0.9
  - type: supports
    target: 2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont
    via: "Two How I AI episodes on the AI-augmented PM, nine months apart, at opposite ends of the same arc. Nika demonstrates tool-hopping — five best-of-breed tools stitched by hand across a 20-minute workflow. Blum demonstrates the consolidation that follows: one harness holding persistent context, running 70–80% of screen time, with the human no longer the integration layer."
    confidence: 0.8
  - type: supports
    target: 2026-07-24-turnbaugh-motherduck-context-layers-explained
    via: "Turnbaugh names the problem — institutional knowledge is uncodified, so agents infer (i.e. guess) — and worries that skills fail because humans forget to invoke them. Blum's morning brief is a worked answer to both halves: the agent itself detects terms it does not know (a payments-domain 'settlement cap'), asks the human, and writes the answer back into its own context files. Invocation is scheduled rather than remembered, and authorship is the agent's."
    confidence: 0.8
  - type: supports
    target: 2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1
    via: "The same phrase at two altitudes, worth holding apart. CS329A's self-improvement is weight-level — sample, verify, fine-tune on winning traces. Blum's self-improvement loop leaves the model fixed and improves the *harness*: it diffs his sent messages against the drafts Claude wrote, mines interaction friction logged by the skills themselves, and proposes new skills. Both close a generate–evaluate–update loop; only one of them touches parameters."
    confidence: 0.7
  - type: supports
    target: 2025-11-26-anthropic-effective-harnesses-long-running-agents
    via: "Blum's stated blocker for the last 20–30% is exactly the long-running-agent problem: everything he runs 'still has to happen online', tied to his laptop being open. He names cloud-resident execution (Claude Tag, OpenClaw, Hermes) as the missing capability that would let the system act rather than only prepare."
    confidence: 0.7
---

# I built a Claude Cowork system that does a week of PM work in a day

> Daniel Blum is a product manager at Melio, a B2B payments company, and one of the most systematic thinkers I've had on the show when it comes to personal AI infrastructure. He's spent the past year building a Claude- and Cowork-based productivity system that manages his Notion board, processes his Slack and email, and runs self-improvement loops every week without needing to be prompted. Beyond his own workflow, Daniel built and scaled a "Workstation" onboarding plugin that gets any Melio employee up and running with a personalized Claude setup in about 15 minutes.
>
> *— Channel description, [[How-I-AI|How I AI]] (episode hosted by [[Claire Vo]])*

A **~46-minute demo episode** of the [[How-I-AI|How I AI]] podcast in which **Daniel Blum**, a product manager at the B2B payments company **Melio**, walks through the personal AI system he has built on **Claude Cowork** — and then through the org-wide plugin that packages it for every colleague. It is the wiki's most detailed account of an *individual knowledge worker's* AI operating system: not a vendor demo, not an engineering harness, but a working PM's answer to coordination overhead, built under ordinary enterprise constraints (fixed tool stack, token budgets, bureaucracy).

Its value to the wiki is that it supplies the **worker-level** counterpart to a corpus that is otherwise heavily firm-level. Where [[micro-productivity-trap|the micro-productivity trap]] describes firms capturing task gains that never reach the P&L, Blum describes what escaping that trap looks like from inside a single job — and is unusually candid that the first few weeks feel worse, not better.

## TL;DR

- **The headline claim, stated carefully.** *"I'm really able to do in a day now what used to take me a week."* Blum flags the LinkedIn-hype resemblance himself — *"it sounds like a hype-y LinkedIn post headliner, but it's true"* — and then makes the more defensible version of the claim: the bigger change is **depth**, not speed. *"There's things that I do today that I just wasn't able to do before"* — in-depth research, competitive analysis, working *"less off of hunches and more off of facts."* Pre-AI, moving fast meant operating on hunches and thin documentation; the trade between speed and rigour is the thing he says has actually dissolved.
- **The two rules, and the explicit claim that the tool doesn't matter.** Asked whether Cowork was the unlock, he refuses the vendor framing: *"While I love Cowork, it's not Cowork in itself… Codex could be great for this as well."* What makes a system powerful is (a) **the system can rewrite its own core files**, so it keeps improving, and (b) **it has connections and integrations to as much of your ecosystem as possible**. Everything else in the episode follows from those two properties.
- **70–80% of screen time runs through one harness — deliberately, for context reasons.** *"Anything that I don't do in Cowork, then the context is not as well caught as if I do it through Cowork."* Centralisation is not a preference here; it is the mechanism by which the system stays current. Consolidation is the price of context.
- **Notion is read-only for the human.** The board (Top of mind / This week / Inbox) was *built by Cowork on its own* — it got tired of his messy Google Doc — and is *maintained* by Cowork on his behalf. He looks at it to focus; the agent writes it. This inverts the usual tool relationship and is the single most concrete illustration in the wiki of an agent owning a system of record while the human owns direction.
- **Two anchoring scheduled tasks.** **Weekly prep** (Sunday) pulls from Notion, calendar, Slack and Granola meeting transcripts, recommends what to add/remove/finish, and walks him through which meetings need real preparation versus a reminder versus nothing. **Morning brief** (daily) summarises yesterday's meetings from Granola transcripts into one-liners plus action items.
- **The context-repair move, which is the episode's most original contribution.** The morning brief scans recent Slack, email and notes **for terms the agent does not understand** and asks about them. On camera it flags *"settlement cap"*: *"I read the thread and understand it's a limit… want me to save?"* He says yes; it writes the definition into its own context files. Vo stops the demo to mark it: *"so many of us work inside companies where the things that we say are not in the training data."* The agent, not the human, notices the gap.
- **The self-improvement loop** — a weekly scheduled task with four parts, all of which mine signals the human never has to volunteer:
  1. **How my drafts landed.** Claude looks for drafts it wrote that he didn't respond to, checks whether he sent something different instead, and learns the delta. *"Claude doesn't learn what the gap is between the draft that it wrote and what I actually sent"* — unless you build the loop that closes it.
  2. **Skills worth building.** It watches for things he does repeatedly and proposes turning them into skills. *"Many of my skills actually ended up being from this flow."*
  3. **Fixes to the existing setup.** Every skill and recurring task carries instructions to **log friction** during use; the weekly task surfaces the top frictions and proposes fixes. Vo singles this out: *"build in feedback or telemetry into your skills and then review that over time."*
  4. **The Improve skill.** A deliberately critical auditor for the *"endless flood of tips… from X and LinkedIn and newsletters."* He forwards posts to a Slack channel Claude reads and asks: is this real, is this powerful, does it fit what we already have, is it needed? Demonstrated live against Vo's own [[2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex|designing-loops episode]], which it judged a good video whose loops he was already running as scheduled tasks — while noting he lacks goal loops, *"so this is something I can adapt."*
- **The ROI answer is a J-curve, stated without hedging.** *"In the beginning… the ROI is not going to look great."* Before the system knows your "business logic," everything is frictionful, *"you're going to lose trust and you're going to be very skeptical and then you're going to double-check everything. But the value tremendously compounds"* — if you power through the first weeks doing two things: **contextualise ruthlessly** and **centralise whatever work you can** in the harness. Vo generalises it to the firm: *"you got to go through the pain of switching your systems and it's not going to be as efficient… the old way will be faster because it's muscle memory."*
- **Scaling to the org: the Workstation plugin, and a UX lesson learned the hard way.** Melio's internal **Workstation** — chosen on Cowork rather than Claude Code specifically because PMs trying the terminal route *"[took] 3 days to install everything and run all the dependencies"* — is a shared plugin whose onboarding chat connects tools, confirms your role, maps your colleagues and management, reads your calendar and Slack, captures your goals, and **builds your writing voice** so you are not writing like a stranger from day zero. About 15 minutes, no terminal. It started for PMs and expanded to all Melio workers. The lesson behind it: a year earlier he built a spec-writing gem ("Spectacular"), thought it was finished, then watched PMs struggle with it live because *"it was completely adjusted to how I work."* The fix was not more capability but a guided UX.
- **The missing 20–30%.** Two named gaps. (1) **Cloud residency** — everything *"still has to happen online,"* tethered to his open laptop; he wants Claude Tag / OpenClaw / Hermes-style execution while away. (2) **Acting rather than preparing** — he is deliberately teaching the system to recognise what a *closed* task looks like (a Slack item unsaved means done; a Gmail item out of the inbox means read) so that eventually it can resolve the small annoying asks itself.
- **Where the reclaimed time goes.** Customer and user conversations, and research — plus a third he names as genuinely new: **improving the system itself.** *"If a system is built correctly and on the right pillars, it can grow and improve over time."*

## Why this matters to the wiki

**1. It is the corpus's clearest worker-level maturity ladder.** The wiki measures AI maturity at firm level in [[2026-04-28-mit-sloan-ai-maturity|MIT CISR's four stages]] and the instruments compared in [[ai-maturity-measurement-comparison|the maturity-measurement thread]]. Blum supplies the individual analogue, and unusually he narrates *the whole trajectory* rather than an end state: bound to whatever tools the company bought → improving isolated artifacts with Gemini Gems → centralising work into one harness → agent-maintained systems of record → agent-maintained *context* → agent-proposed improvements to the system → packaging the system for colleagues. That is a progression with observable transition markers, which is what the thread has been missing on the individual axis. (The same-day synthesis [[syntheses/ai-worker-maturity-levels|ai-worker-maturity-levels]] fuses this trajectory with seven published ladders into a six-level worker scale; this source is its eighth fragment and only lived case.)

**2. It supplies a non-vendor mechanism for the context problem.** [[2026-07-24-turnbaugh-motherduck-context-layers-explained|Turnbaugh]] argues institutional knowledge goes uncodified, agents therefore *infer* (her word for guess), and skills files fail because humans forget to invoke them. Blum's morning brief answers both objections at once: the **agent** detects its own ignorance and asks, and invocation is **scheduled** rather than remembered. It is the same context-layer argument relocated from the database to the individual.

**3. It gives the [[micro-productivity-trap]] an escape narrative at N=1.** The trap's structure is task-level gains that don't compound. Blum's account of *why* they compound for him is specific and testable: centralisation makes context accumulate, accumulated context reduces friction, reduced friction increases centralisation. The J-curve warning — that the loop runs *negative* before it runs positive — is the part most adoption advice omits, and it is the mechanism by which honest firms abandon systems just before they start paying.

**4. It is a rare account of internal distribution.** Most of the wiki's adoption sources describe what firms should do; this describes what one employee actually shipped to colleagues, and why the first attempt failed (built around its author's workflow) and the second worked (guided onboarding UX, no terminal, 15 minutes).

## Dynamic-capabilities reading

The source sits mostly in **transforming** and **contextual** cells, with a sensing component that is unusually concrete.

- **`digital-sensing/digital-scouting`** — The **Improve skill** *is* a scouting function, miniaturised and personal: a standing pipeline that ingests external signals (X, LinkedIn, newsletters, podcasts) and adjudicates *"is this real, is this powerful, is this needed"* against the current system. Blum built it because the flood was *"incredibly overwhelming"* — scouting here is as much a filter against hype as a search for signal.
- **`digital-sensing/digital-mindset-crafting`** — Vo's company-level argument, which Blum endorses: accept a period of *worse* performance to reach a higher level, and the payoff is not only a better system but *"everybody will have more skills."* Mindset before machinery.
- **`digital-seizing/rapid-prototyping`** — Skills are prototyped continuously rather than specified up front; the self-improvement loop *proposes* candidates from observed repetition, and he builds them. Prototyping is the delivery mode of the system's own evolution.
- **`digital-transforming/improving-digital-maturity`** — The Workstation plugin is a maturity intervention aimed at the workforce: every Melio employee reaches a personalised, connected, voice-calibrated baseline in ~15 minutes rather than by individual heroics.
- **`digital-transforming/redesigning-internal-structures`** — Notion demoted to read-only with an agent as its maintainer; Workstation described as *"an operating system"* for workers. The unit of redesign is the individual's workflow, but it is distributed as shared infrastructure.
- **`contextual/internal-enablers`** — Claude Enterprise plus Cowork arriving in the stack is the named inflection (*"that's when things really changed for me"*); the plugin library is what makes one person's system reachable by everyone.
- **`contextual/internal-barriers`** — Named explicitly and without complaint: *"the constraints of an average PM… not endless tokens, needing to work within budgets and bureaucracy."* Plus the failed Claude Code rollout — three days of dependency installation — as a UX barrier that killed adoption before value could be judged.

`roles:` overrides the inherited defaults because the source's altitude is the practitioner, not the C-suite: `product-manager` (the protagonist role), `transformation-lead` and `cdo` (internal distribution of a worker-level system), `chro` (onboarding, voice calibration, workforce maturity), `innovation-lab-lead` (the self-improvement loop as continuous internal R&D).

## Linked entities and concepts

- **Entities**: [[How-I-AI|How I AI]] (channel), [[Claire Vo]] (host), [[Anthropic]] (Claude, Cowork, Claude Enterprise, Claude Tag), [[Claude Code]] (the rejected alternative, and the terminal-UX cautionary tale).
- **Concepts**: [[agent-harness]] (Cowork as the harness; his two rules are harness-design criteria), [[agentic-engineering]] (scheduled tasks, skills, plugins, connectors at non-engineer altitude), [[micro-productivity-trap]] (the J-curve as the escape mechanism), [[enterprise-ai-adoption]] (internal distribution, onboarding UX), [[automation-vs-augmentation]] (the system prepares; he decides — and he is explicitly building toward it acting).
- **Dangling** (single-source mention, deferred): **Daniel Blum** (PM, Melio — first appearance in the corpus; promote on a second citing source per the author-entity promotion rule). **Melio**, **Notion**, **Granola**, **Workstation** likewise deferred.

## Debates and supersession

- **Is "a week in a day" a measurement or a feeling?** It is self-reported, single-subject, unaudited, and the speaker has an audience incentive — he acknowledges the resemblance to hype himself. The wiki should treat the *mechanism* claims (centralisation → context accumulation → friction reduction) as the transferable content and the multiplier as an anecdote. Note the tension with [[2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity|Frey]] and the wider return-gap cluster: vivid individual gains coexisting with absent aggregate productivity growth is precisely the pattern those sources are trying to explain, and this source is a data point *inside* that puzzle rather than a refutation of it.
- **Consolidation versus tool-hopping.** [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont|Nika (Dec 2025)]] treats fluent movement between five best-of-breed tools as the core skill; Blum treats *not* leaving the harness as the core discipline, because context is lost at every exit. Both were filmed for the same show nine months apart. The unresolved question is whether this is a genuine reversal, a difference between exploratory and operational work, or simply what changed when harnesses got persistent memory and connectors.
- **Two meanings of "self-improving."** Blum corrects himself mid-sentence — *"it's almost not self-improvement, but it's Claude helping me improve it"* — which is a sharper distinction than most practitioner talk manages, and worth preserving against [[2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1|CS329A's weight-level sense]]. His loop never changes a parameter; it changes files, and a human approves each change.
- **Open question — does the J-curve have a floor anyone has measured?** Blum says "a few weeks" of negative ROI from a single case. Nothing in the corpus quantifies the trough's depth or duration across workers, and a firm deciding whether to push through needs exactly that number. Carried to [[ai-maturity-measurement-comparison]].
- **Open question — does an individually-built system survive its builder?** Workstation is distributed as a plugin, but its design assumptions came from one PM's workflow, and the Spectacular failure shows what happens when they don't transfer. Whether colleagues' systems diverge usefully or decay is not addressed.

## What was actually ingested

Full ~46-minute episode transcript (auto-generated English captions). Cleanups applied at acquire time and recorded in the raw file's `notes:`: YouTube's accessibility timestamp label had leaked into 340 of 360 segments and was stripped; inline "Chapter N:" headings had leaked into segment text and were re-inserted as proper headings from the chapters metadata; proper nouns were corrected against the channel description as ground truth (Claire Vo, Daniel Blum, Melio, Cowork, Codex, Granola, CLAUDE.md). Two sponsor reads (Optimizely, Jira/Atlassian) are present in the transcript and were not treated as content. No screen content was ingested — the demo is visual and the transcript describes it only through the speakers' narration, so all system details here are as *narrated*, not as *observed*.
