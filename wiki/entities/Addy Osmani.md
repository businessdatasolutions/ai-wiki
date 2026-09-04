---
type: entity
kind: person
aliases: ["Addy Osmani", "Addi Osmani", "@addyosmani"]
tags: [addy-osmani, google-chrome, web-developer-advocate, agent-harness-engineering, oreilly-radar, agentic-engineering-blog, ralph-loop, agents-md, hooks-compaction, code-agent-orchestra, agent-teams, factory-model]
affiliation: "Google (Chrome team)"
role: "Software engineer at Google working on Chrome; web-developer advocate; prolific blogger on web performance, JavaScript, and (since 2025) AI-assisted software engineering; O'Reilly Radar contributor"
confidence: 0.85
last_confirmed: "2026-09-03"
accessed_at: "2026-09-03"
source_count: 5
---

# Addy Osmani

**Software engineer at Google** working on the Chrome team and a prolific web-developer advocate. Blog at [addyosmani.com](https://addyosmani.com); books on web performance and JavaScript patterns. From 2025 onward, his blog and O'Reilly Radar contributions have shifted substantially toward **AI-assisted software engineering and agentic engineering as a discipline**.

Osmani's wiki anchor is **harness engineering as a named discipline** — his [[2026-05-15-osmani-agent-harness-engineering|Agent Harness Engineering article on O'Reilly Radar (15 May 2026)]] is the wiki's first article-altitude treatment of harness engineering as a deliberate practice, covering: the **Ralph Loop** pattern, `[[AGENTS.md]]` convention, hooks, sandboxes, compaction, and *harness-as-a-service*. The article positions harness engineering as the *scaffolding-around-the-model-as-real-artifact-that-tightens-every-time-the-agent-slips* discipline — convergent with [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's Anatomy of an Agent Harness]] (Osmani credits Viv as the originator of the *harness engineering* term).

Paul Everitt at [[2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering|AI Dev 26 SF]] (one week later) cites Osmani as an influence: *"Addy Osmani wrote a blog post about Agentic Engineering. And as I tell you these blah-blah wrote a blah-blah in your mind you should be thinking it's entering the hype cycle. I should put this on my LinkedIn as a global recognized expert."* The self-deprecating framing notwithstanding, Everitt's nine-element agentic-engineering practice taxonomy includes *harness engineering* as a discrete element — Osmani's article is a direct conceptual predecessor.

## Appears in this wiki via

- [[2026-03-26-osmani-code-agent-orchestra-multi-agent-coding]] — *The Code Agent Orchestra*, write-up of his O'Reilly AI CodeCon talk (26 Mar 2026) — **chronologically his earliest wiki source**, predating the Agent Harness Engineering article below by seven weeks. Explicitly builds [[Steve Yegge]]'s eight-levels framework into concrete patterns: Subagents vs. Agent Teams vs. a 3-tier orchestration-tool landscape, the **factory model** (Plan/Spawn/Monitor/Verify/Integrate/Retro), the Ralph Loop, and a citable empirical claim (Gloaguen et al., ETH Zurich) that LLM-written AGENTS.md files underperform human-curated ones.
- [[2026-05-15-osmani-agent-harness-engineering]] — first-party article: *Agent Harness Engineering* on O'Reilly Radar; the wiki's first article-altitude treatment of harness engineering as a named practitioner discipline.
- [[2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering]] — cited by Everitt as influence on the nine-element agentic-engineering practice taxonomy.
- [[2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex]] — Claire Vo cites Osmani's *loop engineering* article as the best breakdown of what an effective loop needs, reproducing its five-element checklist (work trees, skills, plugins/connectors, subagents, state). Confirms Osmani's *loop/harness engineering* writing as a reference practitioners reach for at the product-leader altitude, not only the engineer altitude.

## Named on air as the reference text on loop engineering (2026-09-03)

[[2026-09-02-github-podcast-demystifying-ai-terms-loop-engineering-squads-harness|The GitHub Podcast, S02E02]] recommends Osmani's writing without qualification while trying to define *loop engineering*: *"there's a guy called Addy Osmani who wrote a blog post on this, on loop engineering. I think that's the best blog post I've read on this topic so far"* — followed by a promise to put it in the show notes. This is the **second** wiki source to route its audience to Osmani for this specific topic; [[2026-06-17-vo-how-i-ai-ai-agent-loops-claude-code-codex|Claire Vo]] credits him for the same thing three months earlier, at a different venue and to a different audience.

The two together substantiate the diffusion path [[concepts/agent-harness|agent-harness]] models — Trivedy coins, Osmani popularises — with evidence from the receiving end rather than from Osmani's own citations. See [[2026-05-15-osmani-agent-harness-engineering|Agent Harness Engineering]].

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "addy-osmani")
SORT file.name ASC
```

## Open questions

- Osmani's pre-2025 web-performance + JavaScript-patterns writing — substantial body of work but pre-AI-agent context. Worth flagging if a wiki concern surfaces around *web-performance + AI-coding-agent intersection* (the *AI-generated front-end performance regression* pattern).
- Osmani's specific *Ralph Loop* origin — Everitt mentions Osmani citing Viv as the originator of harness engineering; the precise attribution chain (Ralph Loop → AGENTS.md → harness engineering) is partly traced in the wiki via [[2026-05-07-chatterjee-anatomy-of-agent-harness]] but worth tracking further.
