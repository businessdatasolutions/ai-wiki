---
type: entity
kind: organization
aliases: ["Defense Innovation Unit", "DIU"]
tags: [defense-innovation-unit, diu, defense-acquisition, us-department-of-war, commercial-solutions-opening, prize-challenges, open-weights, inference-compute, yc-root-access]
confidence: 0.75
last_confirmed: "2026-10-03"
accessed_at: "2026-10-03"
source_count: 3
---

# Defense Innovation Unit

The **Defense Innovation Unit (DIU)** is the Pentagon unit, based in Mountain View, that brings commercial and non-traditional vendors into US defense acquisition. The speakers at the event that brought it into the wiki call the department it belongs to the *Department of War*.

Promoted to an entity page on 3 October 2026, after appearing on three source pages. All three come from one event, YC Root Access's [[2026-09-30-yc-root-access-startup-industrial-base-dc|The Startup Industrial Base]] (Washington, D.C., 30 September 2026), and all describe DIU from inside defense buying: its own CTO, the Under Secretary responsible for the department's innovation funding, and the event page. The wiki has no outside view of DIU yet.

## How it buys, as described at the event

- **Routes.** Commercial Solutions Openings leading to prototype and production OTAs, prize challenges, and a drone programme (Drone Dominance) scored on *"a public leaderboard"* ([[2026-09-30-murphy-koomen-diu-defense-ai-adoption|Murphy & Koomen]]). The amount of one prize challenge is captioned *"$und00 million"* and read as $100 million; it is the speaker's figure and was not checked.
- **Where it sits.** Under Secretary Emil Michael names DIU as one of the department's innovation funding routes, with SBIR/STTR small grants, APFIT and the Office of Strategic Capital, that he wants run from one office, his own; previously they were *"all over the department"* ([[2026-09-30-michael-miller-department-of-war-ai-adoption|Michael & Miller]]).
- **From the vendor side.** Eric Alborg, author of *Build for Defense* and formerly at DIU, where his job was diligence on contract decisions, says the second to fourth contracts are harder to win than the first ([[2026-09-30-yc-root-access-startup-industrial-base-dc|event page]], 3:24:31).

## Its position on AI (Chris Murphy, CTO)

From [[2026-09-30-murphy-koomen-diu-defense-ai-adoption|Murphy's fireside]] with [[Pete Koomen]] of [[Y Combinator]]. Murphy worked on AI at INDOPACOM before DIU.

- **Compute is the limit.** Power and inference compute are named as the binding constraint, with compute to be pooled and served across vendors.
- **Open weights for failover.** Asked whether DIU uses open-weight models when a system fails over: *"absolutely"*. He reports that a weekend of tuning a US open-weights model lifted track detection from *"something like 40-something%"* to 78%. Metric, test set and comparison are not stated. See [[concepts/open-source-ai|open-source-ai]] and [[concepts/ai-sovereignty|ai-sovereignty]].
- **Assurance.** A programme captioned *Mystic Depot* tests models (refusals, guardrails); the name is as captioned and unverified. See [[concepts/ai-benchmarks|ai-benchmarks]].

## Appears in this wiki via

- [[2026-09-30-murphy-koomen-diu-defense-ai-adoption]]: the main source; DIU's CTO on how DIU buys and on defense AI adoption.
- [[2026-09-30-michael-miller-department-of-war-ai-adoption]]: DIU as one of the funding routes the Under Secretary wants under one office.
- [[2026-09-30-yc-root-access-startup-industrial-base-dc]]: the event page; Murphy's fireside and a former DIU staffer's view of contracting.

## Open questions

- Every description here comes from people inside defense buying, at one YC-hosted event. A source from outside (an audit, DIU's own published reports, press coverage) would test the claims about reach, the prize challenge and the open-weights result.
- What the 40% to 78% track-detection figure measures, on what data, and against which baseline.
