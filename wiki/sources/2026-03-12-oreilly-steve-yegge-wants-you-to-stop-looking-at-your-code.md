---
type: source
kind: article
title: "Steve Yegge Wants You to Stop Looking at Your Code"
subtitle: "A conversation about agent orchestration, AI vampires, and why your bike ride is all hills now"
author: ["Tim O'Reilly"]
publisher: "[[O'Reilly Media]]"
section: "O'Reilly Radar"
url: "https://www.oreilly.com/radar/steve-yegge-wants-you-to-stop-looking-at-your-code/"
date_published: 2026-03-12
date_ingested: 2026-07-09
length: "~11 minute read (8-page PDF print, full article)"
raw: "../../raw/articles/steve-yegge-wants-you-to-stop-looking-at-your-code.md"
tags: [steve-yegge, gas-town, eight-levels-of-coder-evolution, ai-vampire, bitter-lesson, taste-is-the-moat, mentors-all-the-way-down, agent-orchestration, burnout, oreilly-radar, ai-codecon]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
  - strategic-renewal/organizational-culture
relationships:
  - type: supports
    target: 2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy
    via: "This is the primary-source interview substantiating what Böckeler cited secondhand — the eight-stages-of-dev-evolution-to-AI framework and the Gas Town name. Böckeler's own Open Questions section flagged that 'a primary-source ingest would substantiate the eight-stages model and the Cloud Flow rename' — this source is that ingest."
    confidence: 0.9
  - type: supports
    target: 2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack
    via: "Tan invokes Yegge's 'level 7 vs level 8' terminology explicitly ('GStack does not get you to level seven... I do think it gets you to level seven'); this source is the primary articulation of that same eight-level framework Tan is applying."
    confidence: 0.85
  - type: supports
    target: 2026-03-26-osmani-code-agent-orchestra-multi-agent-coding
    via: "Same AI Codecon event series (this article explicitly promotes Osmani's 26 March talk 14 days later); Osmani's piece picks up directly where this one leaves off, building levels 5-8 into concrete operational patterns (subagents, Agent Teams, orchestration tiers)."
    confidence: 0.9
---

# Steve Yegge Wants You to Stop Looking at Your Code

> My "Live with Tim" conversation with Steve Yegge this week was one of those sessions where you could imagine the audience leaning forward in their chairs. And on more than one occasion, when Steve got particularly colorful, I imagined them recoiling. Steve has always been one of the most provocative thinkers in our industry, going all the way back to his legendary 2011 platform rant that leaked from inside Google.

## TL;DR

Tim O'Reilly's write-up of a live "Live with Tim" conversation with **Steve Yegge** (12 March 2026) — the wiki's **first primary-source Yegge treatment**, after four earlier sources cited his work secondhand (Loukides, Böckeler, Tan/GStack, Tan&Hu/CS153). Six load-bearing threads:

1. **The Eight Levels of Coder Evolution.** Yegge's framework from the Gas Town launch post — levels 1-4 track increasingly sophisticated IDE use, levels 5-8 track coding-agent orchestration. The key transition is **level 5**: your IDE goes away and you never open it again. The full eight-stage detail (with named activities and key features per stage) is captured in the accompanying infographic — see the table below, transcribed from `raw/assets/image-6.png` (an O'Reilly-produced slide, "created with Nano Banana 2," not authored by Yegge himself).
2. **"We all have a chief of staff now."** Once agents can write pieces of code, developers start running several in parallel — Yegge's analogy is Amazon VPs with executive-assistant support: freed from low-value coordination work to focus entirely on hard problems.
3. **The "AI vampire."** A new kind of burnout: not a boss piling on hours, but an AI assistant that keeps asking "anything else you'd like me to do?" — and you keep saying yes because it's fun and productive. The twist: AI solves the easy problems and leaves only hard ones, so *"everyone's Jeff Bezos now"* — a relentless diet of only-hard-problems is exhausting even though throughput is up. Yegge naps daily, sometimes twice, from the cognitive intensity.
4. **The bitter lesson as daily operating principle.** Not Sutton's paper treated as history — Yegge thinks about it "at least five times a day." His practical test: if you're writing heuristics/parsers/regex to make the AI smarter, i.e. handling what a model could handle itself, you're on the wrong side of the bitter lesson. O'Reilly's own 1993 GNN-vs-Yahoo-vs-Google curation anecdote is offered as an earlier instance of the same pattern.
5. **"Code is a liquid. You spray it through hoses. You don't freaking look at it."** Yegge's answer to why leave the IDE: looking at code while agents work is like parking your Formula One car mid-race to inspect the engine. He frames resistance to this shift explicitly as **grief** (first phase: denial), naming Hacker News as "the home of the new Amish."
6. **"Taste is the moat" + mentors all the way down.** Against the fear that capital-rich corporations dominate the AI era: Yegge argues creativity beats capital — companies will burn millions of tokens on tasteless, undirected generation while a well-directed solo entrepreneur wins. On the future-seniors question (if juniors are replaced by AI, where do new seniors come from?): today's junior engineers become mentors to a new bottom layer of AI-augmented non-engineers (PMs, SDRs, sales) building things themselves — "mentors all the way down," citing Matt Beane's research that people learn from someone one or two levels ahead, not forty levels above.

## Steve Yegge's Eight Stages of AI-Assisted Software Development

Transcribed from the accompanying infographic (`raw/assets/image-6.png`) since Quartz does not publish `raw/`. Three named clusters:

**I. The Early Adopter (IDE-based)**

| # | Stage | Activities | Key feature |
|---|---|---|---|
| 1 | Zero or Near-Zero AI | Occasional code completions; using an LLM chat to ask coding questions. | — |
| 2 | IDE Coding Agent (With Permissions) | A narrow agent operates in the IDE sidebar. | The agent asks permission before executing any tools. |
| 3 | IDE Agent, YOLO Mode | Permissions are turned off; trust in the agent increases. | The agent's scope and impact grow wider. |
| 4 | IDE, Wide Agent | The agent expands to take over the primary coding interface. | Code display is used primarily for diffing. |

**II. The Power User (CLI-based)**

| # | Stage | Activities | Key feature |
|---|---|---|---|
| 5 | CLI, Single Agent (YOLO) | Workflow moves to the command line. | Diffs scroll by rapidly, perhaps with minimal review. |
| 6 | CLI, Multi-Agent (YOLO) | Parallel operations using 3 to 5 simultaneous agents. | High-speed, highly concurrent workflow. |

**III. The Orchestrator (Scale & Automation)**

| # | Stage | Activities | Key feature |
|---|---|---|---|
| 7 | 10+ Agents, Hand-Managed | Managing large clusters of active agents manually. | Approaching the practical limit of human oversight. |
| 8 | Building Your Own Orchestrator | Developing personal software to coordinate and automate agent groups. | Operating at the frontier of automated workflows. |

## Why this source matters to the wiki

This is the **primary-source anchor** the wiki's Gas Town / eight-levels citation cluster has been missing. Four prior sources cited the framework secondhand:

- [[2026-02-03-loukides-radar-trends-february-2026|Loukides (Feb 2026)]] — pointed to Gas Town as the month's exemplar of multi-agent orchestration.
- [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler (May 2026)]] — named "agent swarms à la Yegge's Gas Town stage 6+" and explicitly flagged that a primary-source ingest was needed.
- [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|Tan/GStack (Apr 2026)]] — invoked "level 7" by name to describe his own parallel-Claude-Code workflow.
- [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan & Hu/CS153 (May 2026)]] — referenced Yegge again in passing, explicitly flagged as "technically promotable" at that point.

With this source plus [[2026-03-26-osmani-code-agent-orchestra-multi-agent-coding]] and [[2026-07-08-foxwell-ai-native-devcon-reinvention-of-the-dev-team]] (both also citing the eight-levels framework), the wiki now holds **seven sources** touching Yegge's work — comfortably past the entity-promotion threshold. See [[Steve Yegge]].

## Linked entities and concepts

- [[Steve Yegge]] — promoted to an entity page on this ingest (subject of this primary-source interview; 7th source touching his work).
- [[concepts/agent-harness|agent-harness]] — Gas Town as a named agent-orchestrator; the eight-levels framework as a maturity model for harness sophistication.
- [[concepts/agentic-engineering|agentic-engineering]] — the bitter-lesson-as-daily-practice and taste-is-the-moat claims bear on what skills remain durable.
- **Dangling** (single-source mention, deferred): **Matt Beane** (skills-acquisition research, "one or two levels ahead" mentoring claim).

## Source quality

**Full article** (8 pp., matches the ~11-minute read time in the byline) — a first-party O'Reilly Radar piece by Tim O'Reilly himself, summarizing a live public conversation. Quotable claims are transcribed directly from Yegge's own speech (not paraphrased secondhand), which is why this source out-ranks the four prior secondhand citations for definitional accuracy. No sponsorship beyond O'Reilly's own platform; O'Reilly explicitly promotes his own AI Codecon event inside the piece (minor commercial framing, doesn't affect the substantive content).
