---
type: entity
kind: person
aliases: ["Peter Steinberger", "P. Steinberger", "Steinberger", "steipete"]
tags: [peter-steinberger, openclaw, clawdbot, agent-harness, loop-engineering, agentic-engineering, open-source]
confidence: 0.7
last_confirmed: "2026-09-03"
accessed_at: "2026-09-03"
source_count: 2
---

# Peter Steinberger

Creator of **OpenClaw** — the always-on persistent agent the wiki has tracked since [[2026-02-03-loukides-radar-trends-february-2026|February 2026]], originally released as *Clawdbot* in November 2025, and characterised by [[Andrej Karpathy]] (via [[2026-03-03-loukides-radar-trends-march-2026|Loukides, March 2026]]) as *"the next layer on top of AI agents."* Promoted to an entity page on second named mention per the CLAUDE.md cross-page-presence rule; the wiki holds no first-person Steinberger source.

## Where the wiki has him on record

- [[2026-05-11-karten-zhang-continual-harness-online-adaptation]] — cited as **reference [19]** in Karten et al.'s *Continual Harness* paper, with the concrete project link (`github.com/psteinb/openclaw`, originally Clawdbot, November 2025). This is the wiki's first mention of him by name and the reason the academic harness literature treats OpenClaw as a citable artifact rather than a hobby project.
- [[2026-09-02-github-podcast-demystifying-ai-terms-loop-engineering-squads-harness|The GitHub Podcast, S02E02]] — named as one of two people whose public framing drove the *loop engineering* discussion: *"Peter Steinberger, who created OpenClaw, also said the same thing. He was just like, stop prompting your agents, you should be designing loops instead."* The hosts describe the tweet as having reached roughly **8 million views**, and offer that reach — not any technical argument — as the reason the term entered general circulation.

## Why he matters for the wiki's argument

Steinberger is the wiki's cleanest instance of a **vocabulary-propagation vector that is neither a vendor nor a researcher**. The corpus's account of how *harness* entered the language runs through two labs ([[2026-02-11-lopopolo-codex-harness-engineering|OpenAI Codex]] and [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|LangChain]]) and one popularising engineer ([[Addy Osmani]]). *Loop engineering* took a different route: an independent developer's viral post, which two Google Cloud advocates ([[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails|Thurium & Wang]]) and three GitHub advocates then had to define after the fact. The reach came before the definition, which is exactly the sequence the GitHub episode complains about.

His artifact matters on a second axis too: OpenClaw is the corpus's recurring worked example of a **persistent, always-on agent** — the reset-free regime [[concepts/agent-harness|agent-harness]] treats as structurally, not merely conveniently, different from session-scoped agents.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(file.content, "Steinberger")
SORT file.name ASC
```

## Open questions

- **No first-person source.** Both mentions are third-party. The viral post itself, or any OpenClaw design write-up, would be a far better anchor than either — and would let the wiki state the *"design loops, don't prompt"* claim in its author's own words rather than in a podcast's paraphrase of it.
- **OpenClaw has no entity page.** It is named in **fifteen** source pages and has been the subject of a monthly-digest headline twice; it is the largest un-promoted entity the wiki currently carries. Promoting it needs a survey across those fifteen sources rather than a side-effect of this ingest.
- **The second name in the podcast's attribution is unresolved.** The GitHub hosts credit the same framing to a second person whose name the ASR renders *"Baris Turnier"* and whose pronunciation the speaker herself flags as a guess. Deliberately not matched to any person; see that source's *Loose ends*.
