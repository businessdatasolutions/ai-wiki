---
type: source
kind: video
title: "How Factory is building autonomous software with Claude"
author: ["Claude"]
publisher: "Anthropic — Claude channel, customer story"
url: "https://www.youtube.com/watch?v=N6FkmdL0Lg0"
date_published: 2026-10-23
date_ingested: 2026-10-30
length: "~10:38 minutes (transcript ~64 lines)"
raw: "../../raw/videos/how-factory-is-building-autonomous-software-with-claude.md"
tags: [anthropic, claude, factory, droids, matan-grinberg, kai-gill, dark-factory, software-factory, cobol-modernization, human-oversight, plan-trust, model-eats-harness, opus, fable, customer-story]
dynamic_capabilities:
  - digital-seizing/strategic-agility
  - strategic-renewal/collaborative-approach
relationships:
  - type: supports
    target: 2026-10-19-lloyd-warp-what-it-takes-to-build-a-software-factory
    via: "the software factory as the stage after engineers supervising single agents"
    confidence: 0.65
  - type: supports
    target: 2026-06-11-kilpatrick-sequoia-model-eats-the-harness
    via: "models absorbing what the harness used to do, and rebuilding the harness as they improve"
    confidence: 0.7
  - type: supports
    target: 2026-10-27-chase-langchain-interrupt-london-agents-improve-over-time
    via: "the model and the harness as distinct layers of an agent, each changing over time"
    confidence: 0.55
---

# Grinberg & Gill (Claude channel) — Factory and the dark factory

> Factory is bringing autonomy to software engineering with Droids, AI coding agents that handle enterprise work. In this conversation, Co-founder and CEO Matan Grinberg sits down with Anthropic's Kai Gill to talk about his journey founding Factory, how Claude's frontier models handle long-horizon tasks across large codebases so teams can trust agent plans with less oversight, and what it will take to build a fully autonomous "dark factory" for software.

## TL;DR

A 10-minute customer interview on the [[Anthropic]] **Claude** channel. **Matan Grinberg**, co-founder and CEO of **Factory**, who left a physics PhD on string theory in 2023, talks with Anthropic's **Kai Gill**. Factory's agents are called Droids. Four claims:

1. **Reduced oversight is the unlock.** The biggest gain from Opus is *"reducing human oversight."* Plans used to be closely monitored; now *"you literally might not even look at them,"* and going back to one is *"a very crazy corner case."* A bad plan may only show up *"billions of tokens down the line."*
2. **The dark factory.** Droids *"lights off 24 hours a day, 7 days a week"* would monitor a deployment, see a fall in a completion rate, test in a sandbox, propose a fix, ping a person, deploy and monitor again. *"We're not fully there yet."*
3. **A lesson-carrying migration.** At one bank, a Factory engineer sat beside the bank's engineers for a first COBOL modernisation while the Droid extracted lessons. On the next one, *"the amount of human involvement was 90% less."*
4. **The harness has to keep being replaced.** *"A model today could do what a model plus a harness could do 2 years ago."* As models improve, *"if you are lazy, and you don't change your harness, it's going to be superseded."* Hence *"in one hand a sledgehammer"* and a monthly rethink.

## Key claims

### Why industry, and being early

Code generation is most interesting in *"the world's largest enterprises, some of the messiest codebases where some of the code is 30 years old,"* which is why he left academia. Gill recalls him saying that being too early is the same as being wrong. Grinberg calls 2023–25 a blessing in disguise, since he knew nothing about running a company and *"would have missed the opportunity."*

### Trust as behaviour change

*"As you get used to delegating tasks to agents that can go for days or weeks on end,"* people get used to not touching something for days. Seeing meaningful output builds trust. He also says the product must *"respect their intelligence as developers"* and be configurable *"to the silhouette of their organization."*

### Which model where

*"If you have the CTO of a company implement every line of code, that is not an efficient use of their time."* Grinberg uses Opus for planning and for orchestrating many moving parts.

### Three hundred things

*"Every company wants to ship 30 things, but they can only ship three and a quarter … Well, now you can ship 300 things. But will those 300 things actually make a difference?"* The human question becomes *"what really is our core competency?"*

### What blocks it

*"Three concentric circles. At the core, there's the model, then there's the harness, and then there's the company and the workflows of the company as a whole."* The interview does not say what in the outer circle is blocking; the answer stays on the harness and on the partnership with Anthropic.

## Dynamic-capabilities reading

- **`digital-seizing/strategic-agility`**: rethinking the harness monthly, with *"a sledgehammer to whatever we thought was the best solution."*
- **`strategic-renewal/collaborative-approach`**: engineers delegating multi-day work, trust built through output, and a Factory engineer beside a bank's engineers on the first pass.

## How it connects

- [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]] — plans no longer read, and trust as behaviour change.
- [[concepts/agent-harness|agent-harness]] — the model absorbing the harness, in a harness vendor's words.
- [[concepts/agent-fleet-management|agent-fleet-management]] — the dark factory as an always-on monitoring loop.
- [[concepts/agentic-engineering|agentic-engineering]] — a legacy migration with lessons carried forward.

## Related in this wiki

- [[2026-10-19-lloyd-warp-what-it-takes-to-build-a-software-factory|Lloyd (Warp)]] — another vendor's software factory, with the loop defined in code.
- [[2026-06-11-kilpatrick-sequoia-model-eats-the-harness|Kilpatrick (Sequoia)]] — *"the model eats the harness,"* and the lock-in objection.
- [[2026-10-27-chase-langchain-interrupt-london-agents-improve-over-time|Chase (Interrupt London)]] — model, harness and context as what improves.
- [[2026-10-28-hack-klein-browserbase-navigators-clickup-why-agents-keep-failing|Hack (ClickUp)]] — another former coding-agent founder on building through the same model generations.

## What was actually ingested

The full interview (10:38, `length_seconds: 638`) from the human-written caption track via the yt-dlp fallback, 64 lines. The edit cuts between speakers and the track has no speaker labels; attributions follow the sense and the description. No stills: a frame probe showed two people talking.

## Linked entities and concepts

- [[Anthropic]] — publisher; Claude is the supplier in the story.
- [[concepts/agent-oversight-and-delegation|agent-oversight-and-delegation]], [[concepts/agent-harness|agent-harness]], [[concepts/agent-fleet-management|agent-fleet-management]], [[concepts/agentic-engineering|agentic-engineering]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the two cells tagged above.

**Dangling** (single-source mention, deferred): Factory, Matan Grinberg, Kai Gill.

## Scope and reliability

A customer story published by the supplier, with a link to a marketing write-up in the description. The bank is unnamed, and the 90% is one before-and-after comparison reported by the vendor, on a second migration that also benefited from the first having been done. Whether plans *should* go unread is not examined. The interview is useful as a plain statement of what a coding-agent vendor now sells: less human oversight.
