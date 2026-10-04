---
type: source
kind: video
title: "Lockheed Taps OpenAI to Solve F-35 Challenges"
author: ["Bloomberg Tech"]
publisher: "Bloomberg Tech (YouTube); host Ed Ludlow with Dr. Sarah Hiza (SVP Technology and Strategic Innovation, Lockheed Martin), recorded at Skunk Works"
url: "https://www.youtube.com/watch?v=I_bNMyxDgvo"
date_published: 2026-10-02
date_ingested: 2026-10-04
length: "~8:14 minutes (transcript ~115 segments; manual English captions, names corrected in quotes)"
raw: "../../raw/videos/lockheed-taps-openai-to-solve-f-35-challenges.md"
tags: [lockheed-martin, skunk-works, defense, multi-model, model-agnostic, ai-testing, assurance, autonomy, crewed-uncrewed-teaming, interoperability, openai, f-35, quantum, bloomberg-tech]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/navigating-innovation-ecosystems
  - digital-sensing/digital-scouting
relationships:
  - type: supports
    target: 2026-09-30-murphy-koomen-diu-defense-ai-adoption
    via: "Both describe how a defense organisation chooses and comes to trust models. Murphy (DIU) asks for assurance of the model a system fails over to and uses open-weight models for failover; Hiza describes Lockheed running 55 LLMs without committing to one lab and testing AI 'the same way we go about, say, a missile system or an aircraft'."
    confidence: 0.7
  - type: supports
    target: 2026-09-30-luo-null-labs-synthetic-data-ai-testing
    via: "Both treat testing of AI and autonomous systems as a condition for deployment. Luo pitches a common test environment because buyers have no shared standard; Hiza describes Lockheed's in-house practice of testing 'corners of the box', as in flight testing."
    confidence: 0.65
  - type: supports
    target: 2026-09-30-yc-root-access-startup-industrial-base-dc
    via: "Same week and same subject: AI and autonomy in US defense. The YC event gathers startups and officials on the defense industrial base; Hiza speaks for an incumbent prime, from Skunk Works, on autonomy, interoperability and work with a frontier lab."
    confidence: 0.6
---

# Lockheed Taps OpenAI to Solve F-35 Challenges

> Lockheed Martin is taking a model-agnostic approach to AI, using 55 different large language models across its business while applying the technology to everything from internal operations to autonomous weapons systems. SVP of Technology and Strategic Innovation Sarah Hiza discusses how Lockheed tests AI before deploying it, the growing role of autonomy and crewed-uncrewed teaming, and reveals that OpenAI is working alongside the F-35 team to tackle complex math and physics challenges tied to advanced sensor capabilities. She joins Ed Ludlow on "Bloomberg Tech."
>
> *— Channel description, [[Bloomberg Podcasts|Bloomberg Tech]] (subscription links omitted)*

A short interview recorded at Lockheed Martin's Skunk Works. Host **Ed Ludlow** talks to **Dr. Sarah Hiza**, Lockheed's senior vice president of technology and strategic innovation. It is the first time the wiki hears from a large defense prime rather than from startups and officials, and it lands two days after the [[2026-09-30-yc-root-access-startup-industrial-base-dc|YC defense-tech day]] covered the same ground from the startup side.

It earns a source page for three things the wiki can use: a stated multi-model strategy (*55 different large language models*), a stated way of testing AI before deployment, and a new collaboration between [[OpenAI]] and the F-35 team, announced on air.

## TL;DR

- **Model-agnostic on purpose.** *"We have chosen to be agnostic when it comes to frontier labs. That's an intentional part of our strategy. We see it a little bit like a horse race"* ([0:51](https://www.youtube.com/watch?v=I_bNMyxDgvo&t=51s)). *"We have 55 different large language models that we're using to run Lockheed Martin"* ([1:05](https://www.youtube.com/watch?v=I_bNMyxDgvo&t=65s)): for internal operations *"whether that's human resources, financial analysis"* ([1:16](https://www.youtube.com/watch?v=I_bNMyxDgvo&t=76s)), and for fielded systems, *"aircraft, missile systems"*, to extend them and make them more reliable.
- **Compute was the bottleneck.** Lockheed has worked with AI and machine learning *"for two decades"* ([2:03](https://www.youtube.com/watch?v=I_bNMyxDgvo&t=123s)); *"the log jam was around compute capability,"* overcome *"in the last three to five years with GPUs, TPUs"* ([2:07](https://www.youtube.com/watch?v=I_bNMyxDgvo&t=127s)).
- **Test AI like an aircraft.** *"We understand harnessing. But really critical to the way we go about AI is the same way we go about, say, a missile system or an aircraft. We put it through rigorous testing, including corners of the box, so that we understand its capability and to ensure the harnessing is sufficient"* ([2:22](https://www.youtube.com/watch?v=I_bNMyxDgvo&t=142s)). Asked how an AI agent near weapon systems is kept under control, this is the whole answer; no test method or criterion is named.
- **Autonomy and interoperability.** The near-term change is *"crewed, uncrewed teaming"* ([3:01](https://www.youtube.com/watch?v=I_bNMyxDgvo&t=181s)): a piloted F-35 working with the Vectis drone. The second is a data layer across systems from different contractors, which *"all don't really talk to each other"*: *"having the right data layer to have interoperability between all of those systems will be enabled by AI"* ([3:17](https://www.youtube.com/watch?v=I_bNMyxDgvo&t=197s)).
- **OpenAI beside the F-35 team.** Adding a more advanced sensor to the F-35 surfaced *"math and physics challenges, and we've actually reached out to OpenAI"* ([7:26](https://www.youtube.com/watch?v=I_bNMyxDgvo&t=446s)), prompted by OpenAI's reported solution of a long-standing math problem. *"Their team is working right beside us"* ([7:58](https://www.youtube.com/watch?v=I_bNMyxDgvo&t=478s)). No result is claimed yet.
- **Quantum, for sensing.** Lockheed has just opened a quantum innovation center ([5:54](https://www.youtube.com/watch?v=I_bNMyxDgvo&t=354s)), aimed at sensing, secure communications and positioning, with demonstrations from space planned for next year.

## Why this matters to the wiki

**1. A large organisation that refuses to pick one lab.** Most adoption sources in [[enterprise-ai-adoption]] describe a firm standardising on one vendor or building its own model. Hiza describes the opposite: a deliberate portfolio of 55 models, chosen per use because *"there are pros and cons to each."* [[2026-09-30-murphy-koomen-diu-defense-ai-adoption|Murphy (DIU)]] reaches a similar place from the buyer's side: open-weight models as fallbacks, and compute pooled across vendors.

**2. Testing as the answer to the control question.** The answer to *"what if an AI agent does something that relates to weapon systems"* is borrowed from flight testing: test to the edges before deployment. That is the practice [[ai-benchmarks]] keeps asking for and rarely sees described by a deployer. It sits beside [[2026-09-30-luo-null-labs-synthetic-data-ai-testing|Luo's]] argument that defense has no common test standard for AI. Hiza describes an internal practice, not a shared one, which is consistent with Luo's point.

**3. A frontier lab as an engineering partner.** The OpenAI collaboration is the wiki's first case of a frontier lab's team working inside a prime contractor's engineering programme on a domain problem (sensor physics), not supplying a model or a chat product. Recorded on [[OpenAI]].

**Dynamic capabilities.** **`digital-seizing/balancing-digital-portfolios`**: 55 models held as a portfolio, with the bet spread because it is *"like a horse race"* and each model has *"pros and cons."* **`digital-transforming/navigating-innovation-ecosystems`**: work *"beyond the walls of Skunk Works"* with venture companies, large commercial tech companies and now OpenAI's team on the F-35. **`digital-sensing/digital-scouting`**: the quantum innovation center, opened because quantum is judged to be *"moving outside of the lab,"* is scouting turned into an organisation.

## Linked entities and concepts

- **Entities**: [[Bloomberg Podcasts|Bloomberg Tech]] (channel), [[OpenAI]] (working with the F-35 team).
- **Sources**: [[2026-09-30-murphy-koomen-diu-defense-ai-adoption|Murphy & Koomen / DIU]], [[2026-09-30-luo-null-labs-synthetic-data-ai-testing|Luo / Null Labs]], [[2026-09-30-yc-root-access-startup-industrial-base-dc|YC Root Access, The Startup Industrial Base]]; and, without a typed edge, [[2026-09-30-singh-botha-bloomberg-flow-engineering-ai-hardware-design|Flow Engineering on Bloomberg Tech]], the same host two days earlier.
- **Concepts**: [[enterprise-ai-adoption]], [[ai-benchmarks]].
- **Dangling** (single-source mention, deferred): **Lockheed Martin**, **Skunk Works**, **Sarah Hiza**, **Ed Ludlow** (host; also on the Flow interview), **Vectis**, **Aegis**.

## Debates and supersession

- **A test practice described, not shown.** Testing *"corners of the box"* is named as the safeguard, but no method, criterion or result is given, and the 55 models are not named. This is a senior executive describing her company's practice in a short broadcast interview.
- **"Harnessing."** Hiza uses the word for keeping a model's behaviour within bounds. It overlaps with, but is not the same as, the wiki's [[agent-harness]] sense of the runtime around a model; the page does not treat it as evidence for that concept.
- **The OpenAI collaboration is new and unreported in detail.** Announced on air, with no scope, terms or outcome. The motivating *"math problem"* OpenAI solved is not named in the interview and is not ingested.

## What was actually ingested

The full transcript (manual English captions, 115 segments, 0:00–8:13). Corrected in quotes: *Vectrus* → Vectis, *f 35* → F-35, *open I... OpenAI* → OpenAI. A question that names an outside partner (captioned *Fortum* and later *Fordham*) is left out because the name could not be identified. No stills: a studio interview at Skunk Works, with nothing on screen beyond the speakers.
