---
type: source
kind: video
title: "How I manage 15 AI agents 24/7 as a solo founder | Ryan Carson"
author: ["How I AI"]
publisher: "How I AI (podcast by ChatPRD), hosted by Claire Vo; guest Ryan Carson, founder of Untangle. Written companion published the same day as Lenny's Newsletter, \"I spent $20,000 on Devin in a month. Here's what I learned\""
url: "https://www.youtube.com/watch?v=zPfxlcVpFgs"
date_published: 2026-08-24
date_ingested: 2026-08-30
length: "~44:14 minutes (transcript ~424 segments; auto-generated captions, ASR-cleaned)"
raw: "../../raw/videos/how-i-manage-15-ai-agents-24-7-as-a-solo-founder-ryan-carson.md"
tags: [ryan-carson, claire-vo, untangle, devin, cognition, codex, claude-code, cloud-agents, agent-fleet-management, folder-queue, playbooks, watchdog, land-pr, merge-mommy, decision-fatigue, solo-founder, product-market-fit, hiring, bugbot, merge-queue, claude-design, openclaw]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-seizing/rapid-prototyping
  - strategic-renewal/business-model
  - contextual/internal-enablers
relationships:
  - type: supports
    target: 2026-07-25-darroman-profitable-founder-managing-ai-agents-25-prs-a-day
    via: "same practitioner, same operating system, one month apart and through two different interviewers. The written piece supplies the numbers the conversation skips — the 25-minute check cadence, the ~$60-per-run signup test, the ~$5k/month sustainable target — while the video supplies the reasoning and the anti-thesis. Read together they are the fullest account of one person's agent-fleet practice in the corpus"
    confidence: 0.9
  - type: supports
    target: 2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot
    via: "the review-side counterpart, described in this episode by its own author. Carson's Land PR playbook and Vo's Merge Mommy solve the same bottleneck — 40 PRs a day against one human reviewer — by opposite routes: Carson gates on a narrated video walkthrough he watches, Vo gates on a six-dimension risk score that auto-approves the low band. Both keep a human on the high-risk tail"
    confidence: 0.85
  - type: contradicts
    target: 2026-08-14-blomfield-yc-building-structuring-ai-native-company
    via: "both are AI-native-company arguments from experienced founders, and they split on whether the loop should close without a human. Blomfield: the quality gate *\"probably should not be a human in all but the most extreme cases.\"* Carson, running the thing at 40 PRs a day, reports the opposite conclusion from experience — *\"I think we all wanted these sort of like automatic improvement loops to and they just don't work with product… we're nowhere near any frontier model having the intelligence to know what to ship.\"* The disagreement is specifically about *product* judgement, not code review, where Carson does automate"
    confidence: 0.75
  - type: supports
    target: 2026-05-08-running-an-ai-native-engineering-org
    via: "the solo-founder limit case of the same claim. Where the AI-native-org material describes managers learning to run agent-augmented teams, Carson has removed the team entirely and kept only the management layer — *\"how do you effectively manage 10, 20, 100, 500 employees? This is the whole reason that organizations were built as pyramids.\"* He is explicitly reasoning from org design, not from tooling"
    confidence: 0.7
---

# Carson & Vo — How I manage 15 AI agents 24/7 as a solo founder

> Ryan Carson is a five-time founder and the current solo founder of Untangle, a B2B SaaS platform for family law firms. Before Untangle, he co-founded Treehouse, an online coding education platform, and has spent the better part of two decades building and leading tech companies. He's active on X, where he shares his solo founder journey in real time, including what he actually spends on AI tools each month.
>
> *What you'll learn:*
> 1. Why Ryan manages 15 concurrent Devin agents with a folder system and a piece of paper, not a dashboard
> 2. The Watchdog playbook: what he built to replace a customer success team across every law firm account
> 3. How his LAN PR skill closes the loop on 40 daily PRs without a QA team reviewing a single one
> 4. Why he moved off local agents almost entirely

## TL;DR

A **~44-minute screen-share episode** of *[[How-I-AI|How I AI]]* in which **[[Ryan Carson]]**, solo founder of **[[Untangle]]**, walks **[[Claire Vo]]** through his live agent setup. Its value to the wiki is that it is a **working system operated at volume by one person**, shown on screen, with the costs stated — not a vendor demo and not a survey. The written companion is Lenny's Newsletter, *"I spent $20,000 on Devin in a month. Here's what I learned"* (same date; raw copy at `raw/articles/2026-08-24-carson-vo-lennys-i-spent-20000-on-devin-in-a-month.md`), which carries the framing and takeaway list while the video carries the reasoning.

**1. The thesis: the job is now agent management, and it is an org-design problem.** *"All of us have to uplevel our ability to manage agents. Like that is our job."* Carson reaches for the organisational analogy immediately and unprompted: *"How do you effectively manage 10, 20, 100, 500 employees? This is the whole reason that organizations were built as pyramids — humans can't scale and have a thousand directs."* The corollary he draws is a **claim about who is advantaged right now**: *"the reason why I think folks of a certain level of experience are ready to cook right now with AI is all those management skills that you have developed over your career… How do you structure? How do you team? How do you prioritize? How do you delegate? Where do you micromanage? Where do you let go?"* This is the sharpest statement in the corpus of experience-as-advantage in agentic work, and it comes from someone with no team to manage.

**2. Cloud over local, stated as a hard position.** *"If you're out there listening and you are doing engineering, you're doing your work locally, you really need to open your eyes. I think the future is pretty much 100% cloud agents."* The mechanism is not preference but **workspace isolation**: a fresh VM per [[Devin]] session means concurrent agents cannot collide in a shared working tree, so parallelism scales horizontally instead of being capped by one laptop and one attention span. He spent **$5,000/month on Devin, then $20,000 in a single month**, then negotiated credits from [[Cognition]] on the strength of his audience — a detail worth keeping, because it means his reported spend is not the price a normal buyer pays.

**3. The control surface is a folder tree and a piece of paper.** He runs *"probably 10, 15 threads"* in Devin, bucketed into folders — **bugs, P0, P1, P2, investors** — because *"I remember one of your shows was saying it's sort of like four or five concurrent tasks you can actually keep track of. And I agree with that."* The folders hold the agents; a **handwritten weekly priority list** (he holds it up on camera) holds the human. *"The way I stay focused is by also having this piece of paper which has weekly priorities on it."* The pattern generalises: **the queue is machine-side, the priorities are human-side, and they are deliberately kept in different media.**

**4. Playbooks as the reusable unit.** Two are named. **Watchdog** — run *"when that moment where you feel like I need to know what's going on in the business right now, I feel stressed"* — iterates a per-firm skill across every customer account, pulls activity and Sentry errors since the last run, and then does the part that matters: *"you don't want just data. You want it to be transposed and filtered and sorted for you. So then it comes up with the top three things that are going wrong."* And it closes the loop against his own shipping: *"did it get fixed, or is it currently being fixed, or is there an open PR that never got merged?"* **Land PR** — triggered when an agent reports a PR done — runs a fresh Devin Review, allows **up to two review loops**, then records a **narrated video walkthrough** with captions and a red/green test list. *"It has to show me that video and then I say video approved, land it, and then it will merge."* An **investor-update skill** rounds out the set. Cognition's playbook documentation is summarised at `raw/articles/2026-08-30-cognition-devin-playbooks-and-cloud-agents.md`.

**5. Cloud agents are not coding agents.** *"People have still bucketed these cloud coding agents as coding agents… In fact, Devin runs Deal Desk for me. Devin's doing quoting, custom quoting… operations, documentation, customer triage."* His framing question: *"what would you do with somebody who both knew your code base and could write code to solve anything in your business?"* This is the episode's most portable idea for non-engineering readers, and Vo agrees: *"more than engineers need to get hands-on with background agents."*

**6. The anti-thesis, which is why this episode matters most.** Vo's own summary is *"maybe the most anti-AI episode of How I AI."* Carson, who spends $20k/month on agents, argues output is not the constraint:

> *"I know I'm a token maxer and you should let your agents run 24 hours a day and ship as much code as humanly possible… And I really don't ship more than I think the market wants. I really try to constrain my output — not quality, not on bugs — because I don't think I get multiples of quality off of multiples of output."*

And on self-improving product loops specifically: *"I think we all wanted these sort of like automatic improvement loops and they just don't work with product… we're nowhere near any frontier model having the intelligence to know what to ship."* Vo extends it to markets: *"all of this intelligence has not magically created markets where there were none before, other than AI markets… there's a mismatch between the quantity of output of code and commercializable product."* Carson's prescription is unglamorous and physical — he found Untangle's PMF by emailing a prospect, taking a Google Meet, landing them, and then asking *"can I come to your office?"* — *"because we can ship so much and build so much digital product, we're not getting out of our chairs enough."*

**7. Tool split, stated as a division of labour.** **Devin** for cloud/background work, ops, and one-off fixes. **Codex** for pair-programming and long front-end grinds — *"the low latency plus the browser on my machine plus basically infinite tokens"* — and notably **for verification**: *"write user stories, use Chrome, pull up the preview branch, go through it as a user, list which user stories pass, identify bugs, fix them."* **Claude Design** for design systems, where he says Devin is *"terrible"* and Codex *"hilariously bad"*; the pipeline is Claude Design → design tokens as Markdown → Codex builds the technical design system and shared components. Also in the stack: **Bugbot** for PR review, **merge queues** on GitHub, and — separately — **Merge Mommy**, Vo's own risk-scoring auto-approver (see [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot]]).

**8. Hiring becomes verification.** Carson's open engineer role has **no phone screen and no interview**. *"All I want you to do is record a video full screen of you building a new feature for an app that already exists… I just want to see how good of an agent manager you are."* Phase two gives finalists Devin access and asks for the same recording on a real task. Vo's read: *"you're almost hiring a human like you would hire an agent… you're doing a verification loop."*

**Where this sits against the rest of the corpus.** The numerate companion is [[2026-07-25-darroman-profitable-founder-managing-ai-agents-25-prs-a-day|Darroman's write-up]] a month earlier, which supplies the cadences and per-run costs this conversation skips. At the organisational level it is the **solo limit case** of [[2026-05-08-running-an-ai-native-engineering-org|the AI-native engineering org]] — the team removed, the management layer kept. And it disagrees sharply with [[2026-08-14-blomfield-yc-building-structuring-ai-native-company|Tom Blomfield]], who argues the quality gate *"probably should not be a human in all but the most extreme cases"*; Carson, running the thing at volume, reports the opposite from experience — though note the disagreement is about *product* judgement, not code review, where he does automate.

## What was actually ingested

The full ~44-minute auto-generated transcript, ASR-cleaned. Speaker labels are **not** present in YouTube's captions, so attribution above was reconstructed from context; the Merge Mommy passage in particular is **Vo speaking, not Carson** (she built it; he had not seen the episode). Two transcription artefacts corrected here: *"Devon"* → **Devin**, and *"LAN PR"* / *"land PR"* → **Land PR** (as in landing a pull request — the episode title metadata's "LAN PR" is an ASR slip carried into the show notes). Sponsor reads for WorkOS and Jira were skipped.

## Dynamic-capabilities reading

- **`digital-transforming/redesigning-internal-structures`** — the episode is, at bottom, about org design under agent abundance: folders as an org chart, playbooks as standard operating procedures, and the explicit pyramid analogy for why a span-of-control problem appears at all. Carson also plans to route multi-user work through Devin threads rather than Slack, to keep context in one place.
- **`digital-seizing/rapid-prototyping`** — 40 PRs/day with a two-loop automated review gate is a prototyping cadence applied to production software.
- **`strategic-renewal/business-model`** — a venture-scale B2B SaaS run by one person, with agent spend substituting for headcount, is a business-model claim, not just a tooling one.
- **`contextual/internal-enablers`** — the paper list and the folder buckets are the enabling constraint: without a deliberate human-side attention limit the fleet is unmanageable.

## Linked entities and concepts

- Entities: [[Ryan Carson]], [[Claire Vo]], [[Untangle]], [[Cognition]], [[Devin]], [[How-I-AI]], [[Lenny's Podcast]], [[OpenAI]], [[Anthropic]], [[GitHub]]
- Concepts: [[concepts/agent-fleet-management|agent-fleet-management]], [[concepts/agentic-pull-requests|agentic-pull-requests]], [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]], [[concepts/agentic-engineering|agentic-engineering]], [[concepts/agent-harness|agent-harness]], [[concepts/durable-skills|durable-skills]]
- **Dangling** (single-source mention, deferred): Linda Douglas, Renée C. Bauer, Florian Darroman

## Scope and reliability

**One practitioner, one company, self-reported, on a podcast that exists to showcase working setups.** No measurements beyond spend and PR counts; no controls; no counterfactual. The $20k figure is a *pre-credit* number and Carson has since been given credits, so it does not represent what an unsponsored buyer pays. Treat everything here as an **existence proof and a source of mechanisms** — the folder queue, the two-loop video-gated merge, the watchdog pattern, the cloud/local split — not as evidence that the approach outperforms alternatives. The corpus's counterweights are direct: [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes]] finds **46.41% of agent fixes rejected** at population scale, and [[2026-03-30-liu-debt-behind-the-ai-boom]] finds **22.7% of AI-introduced issues still alive** at the latest revision. Carson's own anti-thesis in point 6 is the most credible part of the episode precisely because it cuts against his interest.
