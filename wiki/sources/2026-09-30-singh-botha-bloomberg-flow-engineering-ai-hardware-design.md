---
type: source
kind: video
title: "AI Moves From Writing Code to Designing Hardware"
author: ["Bloomberg Tech"]
publisher: "Bloomberg Tech (YouTube); host Ed Ludlow with Pari Singh (founder and CEO, Flow Engineering) and Roelof Botha (Flow investor and board member, formerly Sequoia Capital)"
url: "https://www.youtube.com/watch?v=aROkbSLnLNc"
date_published: 2026-09-30
date_ingested: 2026-10-04
length: "~10:42 minutes (transcript ~136 segments; manual English captions, names corrected in quotes)"
raw: "../../raw/videos/ai-moves-from-writing-code-to-designing-hardware.md"
tags: [flow-engineering, hardware-engineering, ai-agents, requirements, verification, continuous-verification, cad, simulation, reindustrialisation, ai-as-employees, sequoia-capital, roelof-botha, pari-singh, bloomberg-tech, defense-tech]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
  - digital-transforming/redesigning-internal-structures
  - contextual/external-triggers
relationships:
  - type: contradicts
    target: 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees
    via: "Both address whether AI agents should sit in the organisation as employees. Kropp et al. randomise that framing for 1,261 managers and find lower accountability and fewer errors caught, with no gain in adoption; Singh describes Flow's own organisation as one where 'AIs live as employees', counting humans and agents in one headcount."
    confidence: 0.7
  - type: supports
    target: 2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering
    via: "Both describe AI producing code at a pace without precedent. Singh states that 'nearly a 100% of code in Silicon Valley is written by AI' and that design cycles went from two weeks to two hours; the SEI speakers describe the same rate of generation and add that technical debt is now generated at that rate too."
    confidence: 0.6
  - type: supports
    target: 2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable
    via: "Both place AI's next value in the physical world. Hines-Pierce argues from real estate and energy that the constraint has moved to execution on the ground; Botha argues that 26 of the 35 technology companies among the world's 100 most valuable depend on hardware."
    confidence: 0.6
  - type: supports
    target: 2026-09-30-yc-root-access-startup-industrial-base-dc
    via: "Same day and same subject: startups building for defense and US manufacturing. Flow names Anduril among its customers and treats reindustrialisation as a tailwind; the YC event is a full day on rebuilding the US defense industrial base."
    confidence: 0.6
---

# AI Moves From Writing Code to Designing Hardware

> As AI is moving beyond software and deeper into the physical world, Flow Engineering just raised $50 million at a $750 million valuation to help companies use AI agents to design and build hardware. Flow Engineering founder and CEO Pari Singh and Roelof Botha, Flow investor and board member - formerly at Sequoia Capital - join Ed Ludlow to discuss how faster hardware development could support a broader revival of US manufacturing. They speak on "Bloomberg Tech."
>
> *— Channel description, [[Bloomberg Podcasts|Bloomberg Tech]] (subscription links omitted)*

A short studio interview on Bloomberg Tech. Host **Ed Ludlow** talks to **Pari Singh**, founder and CEO of **Flow Engineering**, and **Roelof Botha**, who led Flow's Series A at [[Sequoia Capital]], has since left the firm, and now invests in and sits on Flow's board with his own capital. The occasion is Flow's $50M round at a $750M valuation, co-led by Antonio Gracias (Valor Equity) and Gavin Baker.

It earns a source page for two reasons. It is the wiki's first source on **AI agents applied to hardware engineering**: requirements, CAD, simulation and verification, upstream of the factory floor that [[industrial-ai-agents]] covers. And its founder describes his own company in exactly the terms an experiment already in the wiki tested and found harmful: AI agents as employees on the org chart.

## TL;DR

- **The pitch.** *"Flow is doing for hardware engineering what AI has already done for software engineering"* ([0:53](https://www.youtube.com/watch?v=aROkbSLnLNc&t=53s)). The premise is stated as fact: *"We've gone from design cycles of two weeks to design cycles of two hours. And today, nearly a 100% of code in Silicon Valley is written by AI"* ([0:39](https://www.youtube.com/watch?v=aROkbSLnLNc&t=39s)). No source is given for either figure.
- **From waterfall to continuous verification.** Customers move *"from this traditional waterfall model where a design cycle might be two or three years to this continuous verification cycle where engineers are able to make changes in CAD, simulation, Git, and our AI agents are able to listen to those, understand them, integrate them, and understand the impact of that change very, very quickly"* ([2:56](https://www.youtube.com/watch?v=aROkbSLnLNc&t=176s)). Flow calls itself *"the default platform and system of record for requirements and verification in frontier hardware"* ([8:03](https://www.youtube.com/watch?v=aROkbSLnLNc&t=483s)).
- **The problem it targets.** From Singh's own time as a mechanical engineer: *"10% of the time would go into the actual innovation and the architecture, and 90% of the time would go into digital manual labor. Rebuilding that CAD model for the eleventh time, rebuilding an Excel model, go into a huge regulatory PDF of 200 pages and find that one bit of data"* ([3:51](https://www.youtube.com/watch?v=aROkbSLnLNc&t=231s)).
- **AI agents as employees.** *"The way we think about AI is AIs live as employees in our [organisation]. So we today can go from a 50 headcount team with 25 humans to a 100 or a 200 headcount team with 50 humans, and AI is taking up real roles"* ([4:33](https://www.youtube.com/watch?v=aROkbSLnLNc&t=273s)).
- **Customers and adoption.** Named customers include Anduril, Rivian, Joby and Stoke Space, and incumbents are arriving: General Motors and the Rivian–Volkswagen joint venture *"were pre AI, and they're completely retooling their core development practices with Flow and AI at the center"* ([8:24](https://www.youtube.com/watch?v=aROkbSLnLNc&t=504s)). Botha: *"96% of the customers that the company has found them"* ([1:50](https://www.youtube.com/watch?v=aROkbSLnLNc&t=110s)). No revenue figure is given when Ludlow asks.
- **The investor's case for hardware.** Botha: of the 100 most valuable companies, *"35 of those are technology companies, and 26 of those 35 are either predominantly hardware businesses or have meaningful components of their business that depend on hardware development"* ([6:49](https://www.youtube.com/watch?v=aROkbSLnLNc&t=409s)). On reindustrialisation policy as a tailwind: *"I don't think it's enough, though. You know, government administrations can change"* ([10:15](https://www.youtube.com/watch?v=aROkbSLnLNc&t=615s)).

## Why this matters to the wiki

**1. Agents on engineering data, before anything reaches the plant.** [[industrial-ai-agents]] describes agents working on a factory's operational data (MES, maintenance, quality systems). Flow works one step earlier, on the engineering record: requirements, CAD changes, simulation results and code, kept consistent by agents as they change. The shared idea is that the data layer is the product: Flow's claim to be the *"system of record for requirements and verification"* is the engineering-side version of the data-fabric argument on that page.

**2. The employee framing, in a founder's own words.** [[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees|Kropp et al.]] tested what happens when AI is presented to managers as a colleague rather than a tool: personal accountability fell by 9 percentage points, escalations rose 44%, and 18% fewer errors were caught, with no gain in adoption. Singh describes Flow's organisation in exactly the framing that experiment tested, with humans and agents counted in one headcount. The interview gives no data on how accountability works at Flow, so the page records the two positions side by side.

**3. The code claim.** *"Nearly a 100% of code in Silicon Valley is written by AI"* joins the practitioner self-reports on [[ai-coding-productivity-evidence]]. [[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering|The SEI/CMU talk]] describes the same pace and adds the cost: technical debt generated at the same rate, and no one yet maintaining AI-written code for five years.

**4. Value moving into the physical world.** Botha's hardware argument and [[2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable|Hines-Pierce's]] real-estate and energy argument both say the next constraint is physical. Flow's customer list (Anduril, Stoke Space, Joby) overlaps the defense and aerospace companies at [[2026-09-30-yc-root-access-startup-industrial-base-dc|YC's defense-tech day]] the same day.

**Dynamic capabilities.** **`digital-seizing/rapid-prototyping`**: the whole pitch is iteration speed, replacing multi-year waterfall design cycles with continuous verification and a team that *"iterate[s] on a nearly daily basis."* **`digital-transforming/redesigning-internal-structures`**: Singh's own organisation counts AI agents in its headcount, and incumbents such as GM are *"retooling their core development practices."* **`contextual/external-triggers`**: the reindustrialisation push and the arrival of agentic AI in software are named as the triggers, with Botha's caveat that policy can turn.

## Linked entities and concepts

- **Entities**: [[Bloomberg Podcasts|Bloomberg Tech]] (channel), [[Sequoia Capital]] (Botha led Flow's Series A there).
- **Sources**: [[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees|Kropp et al. 2026]], [[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering|SEI/CMU 2026]], [[2026-07-30-hines-pierce-mckinsey-ai-physical-world-more-valuable|Hines-Pierce 2026]], [[2026-09-30-yc-root-access-startup-industrial-base-dc|YC Root Access, The Startup Industrial Base]]; and, without a typed edge, [[2026-09-30-demaree-onebrief-ai-military-planning|Demaree / Onebrief]], another defense-adjacent founder reporting a large speed-up from going agentic.
- **Concepts**: [[industrial-ai-agents]], [[ai-coding-productivity-evidence]].
- **Dangling** (single-source mention, deferred): **Flow Engineering**, **Pari Singh**, **Roelof Botha**, **Ed Ludlow** (host; also on [[2026-10-02-hiza-bloomberg-lockheed-ai-openai-f35|the Lockheed interview]]), **Antonio Gracias** / Valor Equity, **Gavin Baker**, Anduril, Rivian, Joby, Stoke Space.

## Debates and supersession

- **Unsourced headline figures.** *"Nearly a 100% of code in Silicon Valley"* and *"two weeks to two hours"* are stated without a source, by a founder selling the hardware version of that shift. They are recorded as claims, not evidence.
- **The employee framing against the experiment.** See *Why this matters* §2 and the `contradicts` edge. The two sources differ in kind: a randomised experiment on managers' behaviour, and a founder's description of his own company.
- **Funding interview.** The occasion is a fundraise, and the investor on the panel holds the stock. The customer list and the *"96% inbound"* figure are the company's; Ludlow's question about revenue gets growth language, not a number.

## What was actually ingested

The full transcript (manual English captions, 136 segments, 0:00–10:35). The caption track spells several names wrongly; quotes above use the corrected forms: *Square Capital* → Sequoia Capital, *Andoril / Andrew* → Anduril, *Rithian* → Rivian, *Stokespace* → Stoke Space, *Perry* → Pari, *Antonio Grasias* → Antonio Gracias, *GIT* → Git. Where the captions drop a word (*"AIs live as employees in our."*), the bracketed word is an inference. A reference to a GM division, captioned *"PPU"*, is left out because it could not be identified. No stills: a studio interview with nothing on screen beyond the speakers.
