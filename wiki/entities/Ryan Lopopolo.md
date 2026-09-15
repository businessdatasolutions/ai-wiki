---
type: entity
kind: person
aliases: ["Ryan Lopopolo"]
tags: [ryan-lopopolo, google, google-cloud, openai, codex, harness-engineering, agent-first-engineering, capability-overhang, loop-size]
affiliation: "[[Google]] Cloud (since ~July 2026); previously [[OpenAI]] (Member of Technical Staff, Codex)"
role: "Engineer at Google Cloud building agents to operate Cloud; coiner of the terms 'harness engineering' and 'agent harness'"
confidence: 0.8
last_confirmed: "2026-09-15"
accessed_at: "2026-09-15"
source_count: 3
---

# Ryan Lopopolo

**Ryan Lopopolo** is the **coiner of the term "harness engineering"** — the wiki's canonical name for the discipline of building software where humans steer and agents execute. The wiki promotes him from Dangling to an entity page on **2026-06-20** after the second substantive source.

Promoted on the second source per the [author-entity-promotion rule](../../CLAUDE.md#author-entity-promotion):

1. **First source** — [[2026-02-11-lopopolo-codex-harness-engineering|Harness Engineering (OpenAI Codex blog, Feb 2026)]]: the wiki's first **vendor-side production case study** of harness engineering — five months, ~1M LOC, ~1,500 PRs, 7 engineers, **0 manually-written lines**, with the operational invariants the [[agent-harness]] concept now carries (repository-as-system-of-record, AGENTS.md as table-of-contents, layered architecture mechanically enforced, golden-principles + scheduled GC, doc-gardening agent).
2. **Second source (the promotion)** — [[2026-06-19-lopopolo-ai-native-devcon-harness-engineering|Harness Engineering: How to Build Software When Humans Steer and Agents Execute (AI Native DevCon, Jun 2026)]]: the conference-talk articulation — the **named definition**, the **three-phase context-delivery model** (ground → just-in-time-steer-via-tool-calls → LM-as-judge review), the **shift-right** counter-prescription, and the **"never give the same review feedback twice → make every mistake statically impossible"** governing rule.

> **Employer correction (2026-09-15).** This page carried him as *Member of Technical Staff at [[OpenAI]] (Codex)* from his June promotion until now. **He has been at [[Google]] Cloud since roughly mid-July 2026**, confirmed on camera in [[2026-09-14-google-cloud-agent-factory-agent-harnesses-explained|The Agent Factory]]: introduced as *"a Googler"*, and *"Holding strong here at Google — it's been eight weeks here for me."* His two OpenAI-era sources remain accurate as of their dates and are **not** superseded; the work they describe was done at OpenAI.

## Google Cloud, and why he moved ([[2026-09-14-google-cloud-agent-factory-agent-harnesses-explained|Sep 2026]])

> *"I am working on Google Cloud. I am trying to build the best agents to help you operate your Cloud… my entire motivation working in AI has been to chase after deployment. It's my belief that today we have what's called **capability overhang**, where the models are so good beyond what we are able to extract from them in terms of useful work today."*

The stated ambition is to make Cloud *"the best computer for agents"* — *"part of having an agent be successful is to give it a computer… and we want to give the agents a big somebody else's computer."*

### Three things this interview adds or corrects

1. **"I have never built a harness."** The most corrective line in his corpus, against the name of his own discipline: *"I think this is a big misnomer with what I term harness engineering. I have always kept the [[Antigravity]]-like thing in your agentic system as fixed."* Harness engineering is curating **tools and context** around a fixed harness — *"all harnesses expose essentially a file read, a grep and an arbitrary command execution tool"*, so investment there *"will never become obsolete"* while models and harnesses are swapped freely.
2. **Loop size as the unit of seniority.** *"All of harness engineering is an increasingly sophisticated set of tricks to bring the agent back to baseline"* — small PRs → agent-reviewable PRs → narrowed state space → longer horizons, until *"wholesale language migrations are tractable."* Then: *"I want, from junior to senior to staff engineers with agents, think about how far in advance they can unblock their agentic team."*
3. **Over-scaffolding as a named risk** — the first in the corpus: *"you can very much over-scaffold around them, which constrains them unnecessarily as they get better and gets you into sunk cost fallacy around not wanting to throw this stuff away."*

He also extends the no-manual-code streak well past what the corpus had recorded: the February essay reported five months; here it is *"I don't think I've actually opened an editor at all since around May of last year"* — over a year, across an employer change.

## Role in the wiki

Lopopolo is the wiki's **practitioner-origin voice on [[agent-harness|harness engineering]]** — the person whose vocabulary the rest of the harness corpus relays (e.g. [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler]] propagates the *harness engineering* name explicitly crediting the Codex team). His three sources are complementary: the blog is the **artifact-shape inside one repo**; the DevCon talk is the **discipline definition + operating loop**; the Google interview is the **retrospective and the correction** — what he got wrong about how people would read the name, and what the discipline reduces to once you stop treating the harness as the thing you build.

### The harness-engineering definition (his own words)

> *"Harness engineering is making context around what it means to do a good job legible, and then just-in-time surfacing it to the agent over the course of its trajectories in order to steer and refine its output."*

Governing rule: **"I never want to give the same review feedback twice"** — every correction is driven down a durability ladder (trash-and-reprompt → write it down → reviewer agent judges every diff → statically-verifiable lints/guardrails/tests).

### Distinctive contributions

- **Three foundational limits** that remain in a human+agent team: human time (the scarce resource — remove your own synchronous attention), human/model attention ("attention must sum to one"), and the context window (still scarce despite auto-compaction).
- **Automate context delivery rather than front-loading prompts** — agents auto-discover the relevant guardrails by change category, and the aspiration is to be *"an incredibly lazy prompter"*. **Note the metaphor is unstable in his own usage**: the June 2026 DevCon talk framed this as *shift right, not left*; [[2026-09-14-google-cloud-agent-factory-agent-harnesses-explained|September 2026]] frames the identical substance as *shifting left* (with prompt-appending as *"basically as far to the right as we can go"*), and he corrects himself mid-sentence at ~18:52. **The direction is not load-bearing; the prescription is.**
- **All code is prompts** — unify the codebase on consistent patterns so the model doesn't burn attention disambiguating (one observability stack, not six); **prune latent space** to tell the model which of the choices it has seen in training to make.
- **Coarse structural guardrails** — snapshot tests with 100% branch coverage; statically banning `any`/`unknown`; reviewer agents as "a matrix CI job that points at a bunch of markdown files to judge."
- **The group-tech-lead operating mode** — care about invariants, interfaces, and whether components "do what they say on the tin," not every keystroke; **vibe coding** is part of what makes this possible.

## Career snapshot

- **[[Google]] Cloud** (since ~July 2026) — building agents to operate Google Cloud; motivated by *capability overhang* and the aim of making Cloud *"the best computer for agents."*
- **[[OpenAI]]** (through ~mid-2026) — Member of Technical Staff (Codex). Early adopter of Codex CLI for end-to-end engineering work; the Codex blog's named author.
- **Open source** — maintains Rust crates from his **Artichoke** project (a Ruby interpreter in Rust), e.g. `artichoke-rand-mt` (a Mersenne Twister implementation), where he is now applying Codex-app automations to maintenance.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "ryan-lopopolo")
SORT file.name ASC
```
