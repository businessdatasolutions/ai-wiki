---
type: source
kind: video
title: "Using 'Flexibility' to Solve AI's Energy Bottleneck with Varun Sivaram, Founder and CEO - Emerald AI"
author: ["Boston Consulting Group"]
publisher: "BCG — Pitching Progress podcast (title card: Episode 5), host Vinay Shandal; segment with BCG's Stevan Jovanovic"
url: "https://www.youtube.com/watch?v=xAO3eh9hOMk"
date_published: 2026-10-16
date_ingested: 2026-10-17
length: "~28:30 minutes (transcript ~237 segments; human-curated captions)"
raw: "../../raw/videos/using-flexibility-to-solve-ais-energy-bottleneck-with-varun-sivaram-emerald-ai.md"
tags: [varun-sivaram, emerald-ai, vinay-shandal, stevan-jovanovic, pitching-progress, bcg, nvidia, aurora-ai-factory, manassas-virginia, pjm, epri, dcflex, ferc, chris-wright, data-center-flexibility, power-flexible-ai-factory, stranded-capacity, temporal-flexibility, spatial-flexibility, resource-flexibility, time-to-power, interconnection-queue, ai-energy-trilemma, power-prices, independent-power-producers, gas-turbines, training-vs-inference, nvidia-mission-control, first-mover, podcast]
dynamic_capabilities:
  - contextual/external-triggers
relationships:
  - type: supports
    target: 2026-04-30-ai-index-report-2026
    via: "both put a number on US AI data-centre power demand: the AI Index's 29.6 GW of AI data-centre capacity, and the 80–100 GW of further demand cited in this episode"
    confidence: 0.65
  - type: supports
    target: 2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going
    via: "both address the electricity-price backlash against data centres and place it in local siting decisions and household bills"
    confidence: 0.6
  - type: supports
    target: 2026-10-04-chu-liu-dw-the-dip-how-china-is-viewing-the-ai-race
    via: "both describe placing AI workloads where power is available: China routing training to Inner Mongolia, Xinjiang and Gansu, Emerald moving workloads between data centres when a local grid is stressed"
    confidence: 0.6
---

# Sivaram & Shandal (BCG Pitching Progress) — flexible data centres and AI's power bottleneck

> Billions of dollars are being spent on new CapEx to satisfy the growing energy needs of AI data centres. But one firm is convinced that the answer isn't building new capacity, but being smarter in utilizing the power we already have.
>
> Varun Sivaram is the Founder and CEO of Emerald AI, a company whose software aims to make data centres more 'flexible', by intelligently modulating their computational load, and avoiding demand spikes that could overload the grid.
>
> So what does a truly flexible data centre look like? How much capacity could Emerald's software actually hope to free up? And what happens to everyone who bet big on an explosion in power demand that may never materialize?

## TL;DR

An episode of *Pitching Progress*, a [[Boston Consulting Group]] podcast on climate companies, uploaded to YouTube on 16 October 2026. Host **Vinay Shandal** (BCG) interviews **Varun Sivaram**, founder and CEO of **Emerald AI**, formerly America's lead clean-energy diplomat and an executive at Ørsted; a middle segment is with **Stevan Jovanovic**, introduced as *"one of BCG's leading experts on power and utilities."* **The conversation is older than the upload**: Sivaram says he founded Emerald in late 2024, *"so just 11 months ago,"* and calls an [[NVIDIA]] announcement of *"October 29th"* recent, which places the recording around November 2025.

1. **The constraint is peak capacity, not energy.** The grid is truly stressed *"on the order of 1% per year or less."* *"There's 100 gigawatts of existing stranded capacity that just doesn't get used over the course of the year,"* which he says is enough for all AI data-centre growth over five to ten years on BCG's estimates.
2. **A data centre that can ramp down can connect sooner.** Utilities make a new data centre wait up to ten years for lines, substations and peaker plants sized for its worst moment. One that promises to cut consumption in those rare moments fits on the existing grid.
3. **Three kinds of flexibility.** *Temporal* (pause or slow batchable work such as fine-tuning or a deep-research query), *spatial* (move time-sensitive work to a data centre whose grid is not stressed) and *resource* (on-site batteries). Emerald's *Conductor* software orchestrates them.
4. **Time to power is the value.** Power-cost savings are *"minuscule."* A 200 MW site connected a year earlier and upsized to 230 MW gains *"a 15% NPV uplift… a $2 billion net present value increase."*
5. **Jovanovic's arithmetic agrees on capacity:** about 1,200 GW installed in the US, average utilisation *"between 40 and 50%,"* 80–100 GW of new data-centre demand. If it works, power prices fall, which hurts generators and turbine makers.

## Key claims

### From building supply to managing demand

Sivaram spent fifteen years on multibillion-dollar supply projects (offshore wind, solar and storage at Ørsted) and as a clean-energy diplomat. His conclusion: *"just building more supply… was only half the equation,"* and supply alone could not reconcile AI's demand growth with *"affordable power prices and reliable and stable grids."* Emerald AI aims to make data centres *"the best friend a grid could have."* He reports raising *"north of 40 million"* from backers including Jeff Dean, Fei-Fei Li, Crusoe's Chase Lochmiller, John Doerr and John Kerry, and says that eleven months earlier *"nobody was talking about AI data center flexibility."* He cites Energy Secretary Chris Wright directing FERC to look at fast-tracking grid connections for flexible data centres: *"Flexible AI data centers will soon have a leg up as a matter of national American policy."*

### The Aurora facility

The announcement *"we just made on October 29th"*, with NVIDIA, EPRI, Digital Realty and the PJM grid operator, was for what he calls *"the world's first power-flexible AI factory"*: Aurora, a 96 MW commercial facility in Manassas, Virginia, due to launch the following year. It will first be proven *"in what's called simulation mode,"* then actually flex consumption, within EPRI's DCFlex initiative. Emerald's software is being built into NVIDIA Mission Control, aiming at a reference architecture for future AI factories: *"It's not just about this first commercial deployment, it's about the next thousand."*

### How the flexing works

*"Some of these things are what we call batchable workloads"*: fine-tuning a model, or a deep-research query that can finish in 30 or 35 minutes, can be slowed or paused. Time-sensitive inference can be moved to another data centre whose local grid is not stressed. Batteries add more. *"We have an AI running that behind the scenes autonomously… so the user doesn't notice, and the grid gets the relief when it needs it."* Asked whether real-time agentic inference erodes the room to flex, he expects a roughly *"50/50 split between training and inference"* in power use through the end of the decade, with inference itself a spectrum from latency-critical (serving a world model to a user) to batchable (protein-folding simulations due in 24 to 72 hours). The software will have to adapt, *"but we will always have knobs that we can turn."*

### The BCG view: arithmetic, and who loses

Jovanovic agrees *"100%"*. The US has *"probably now 1,200 gigawatts of installed capacity,"* used on average *"between 40 and 50%,"* so a perfectly levelled load would need 500–600 GW; data centres want another 80–100 GW. *"We could 5x what we need for the data centers if we could perfectly levelize the load."* The obstacle is the chip: *"By the time you put that chip in, you just want to run every single second of the day,"* and operators accept flexibility only because interconnection takes *"four, five, seven, or 10 years."* *"As soon as the supply side… catches up, that business case falls apart,"* though that is *"10 plus years away."*

On politics: power prices are *"becoming a election topic,"* and the perception, *"right, wrong or different,"* is that a data centre in your neighbourhood raises your bill. Removing the incremental demand would lower prices, delighting customers and hurting *"anyone who's supplying electricity today"* and turbine makers counting on a buildout.

### Sivaram's three mountains and three fallacies

The mountains he had to climb: prove the technology works (he says it has been *"peer-reviewed in one of the world's top journals"*), get utilities to agree, and get the AI industry to accept flexibility. He names a **trilemma**: *"You cannot have AI boom, low prices, and highly reliable national secure grids at the same time"* without flexibility.

He does not claim generation is unnecessary: *"we're still gonna need an all of the above strategy,"* and flexibility *"buys us time to more prudently expand the grid."* The three fallacies he sees among AI builders:

1. *"We can just bully our way to getting the grid capacity we want."* The largest players may, but others are *"in a race for a diminishing set of power connections."*
2. *"We'll just go off grid."* Technically and financially complex; *"I don't think it's the way that we will scale 100 gigawatts of AI data centers."*
3. Silicon Valley hubris about space or underwater data centres: *"we will have double digit gigawatts of flexible AI data centers before we have a gigawatt of space-deployed data centers."*

On competition: Emerald has a first-mover lead and *"now may be the most perilous time."* His career advice is to treat life as *"a series of eight to 10, five-year sprints"* and take big swings.

## Dynamic-capabilities reading

- **`contextual/external-triggers`** — power availability as an outside constraint on how fast organisations can deploy AI, together with the policy response (FERC fast-tracking for flexible data centres) and the political pressure from electricity prices. The episode is about infrastructure supply, not about how firms adopt AI, so it touches only this cell.

## How it connects

- [[concepts/foundation-models|foundation-models]] — the energy side of compute scaling. The page already notes rising power demand and nuclear deals; this episode adds the argument that the binding constraint is peak capacity and grid connection, and that demand flexibility could ease it.
- [[2026-04-30-ai-index-report-2026|AI Index 2026]] — 29.6 GW of AI data-centre capacity; this episode's 80–100 GW is the further demand on top.
- [[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Benedict Evans]] — the electricity-bill backlash as a local siting issue; Jovanovic describes the same perception from the utilities' side.
- [[2026-10-04-chu-liu-dw-the-dip-how-china-is-viewing-the-ai-race|Chu & Liu (DW)]] — China sends training workloads to regions with surplus wind and solar, a national version of the spatial flexibility described here.

## What was actually ingested

The full episode (28:30, `length_seconds: 1710`), from the creator-uploaded caption track. Caption errors corrected in quotes and names: "Electric Power Association" is EPRI, the Electric Power Research Institute; "caveat Mtor" is caveat emptor. **Dating:** the recording date is not stated; the internal references above put it around November 2025, about eleven months before the YouTube upload. Sivaram's "11 months", "next year" and "pilots" refer to that time, not to October 2026. No stills: the video is a static audiogram card throughout.

## Linked entities and concepts

- [[Boston Consulting Group]] — publisher (*Pitching Progress*); the host and the utilities expert are both from BCG. Updated in this ingest.
- [[NVIDIA]] — partner and investor; Aurora and NVIDIA Mission Control. Updated in this ingest.
- [[concepts/foundation-models|foundation-models]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the one cell tagged above.

**Dangling** (single-source mention, deferred): Varun Sivaram; Emerald AI; Vinay Shandal; Stevan Jovanovic; PJM; EPRI.

## Scope and reliability

A founder pitching his company on a consultancy's podcast, with an investor's (NVIDIA's) project as the proof point. The 100 GW of stranded capacity, the $4 trillion of unlocked investment and the 15% NPV uplift are his figures, not independently shown; the peer-reviewed paper is mentioned but not named. Jovanovic's capacity arithmetic is rough and assumes load could be perfectly levelled, which he states. The episode is roughly eleven months old at upload, so Aurora's results and later policy are not covered. Its value for this wiki is a clear statement that AI's power problem is about peak capacity and connection queues, with numbers attached.
