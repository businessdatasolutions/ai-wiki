---
type: entity
kind: person
aliases: ["Ryan Carson", "Carson"]
tags: [ryan-carson, untangle, treehouse, devin, cognition, solo-founder, agent-fleet-management, cloud-agents, legal-tech, playbooks, watchdog, land-pr]
affiliation: "Untangle (founder & CEO); previously Treehouse, DropSend, Carsonified; formerly Launch Darkly"
role: "Five-time founder; currently solo founder building Untangle, an AI legal-workflow product for divorce attorneys"
confidence: 0.8
last_confirmed: "2026-08-30"
accessed_at: "2026-08-30"
source_count: 3
relationships:
  - type: part-of
    target: Untangle
    via: "founder and CEO; runs the company solo"
  - type: uses
    target: Devin
    via: "his primary cloud agent — 10–15 concurrent threads, bucketed into priority folders, with Watchdog and Land PR playbooks"
---

# Ryan Carson

**Five-time founder**, currently the **solo** founder of **[[Untangle]]** — AI legal-workflow software for divorce attorneys. Previously co-founded **Treehouse** (online coding education), plus DropSend and Carsonified; he also spent time at Launch Darkly, where he first deployed background agents into public Slack channels as a change-management move. He founded Untangle after watching his parents and two sisters go through what he describes as painful and confusing divorces.

Carson is the wiki's anchor for **[[concepts/agent-fleet-management|agent fleet management]]** — the claim that the human's job in agentic software work is *managing agents*, and that this is an organisational-design problem rather than a tooling one:

> "All of us have to uplevel our ability to manage agents. Like that is our job… How do you effectively manage 10, 20, 100, 500 employees? This is the whole reason that organizations were built as pyramids — humans can't scale and have a thousand directs."

Three things make him unusually useful as a source. **He publishes his costs** — $5,000/month on [[Devin]] rising to $20,000 in a single month, before he negotiated credits from [[Cognition]] on the strength of his audience. **He shows the actual screen** rather than describing a workflow. And **he argues against his own interest**: the practitioner spending $20k/month on agents is also the one saying output is not the constraint.

## The operating system, as documented

- **Cloud over local, on isolation grounds** — *"if you are working locally, I honestly think you are a caveman."* A fresh VM per Devin session means concurrent agents cannot collide in a shared working tree.
- **Folders for the fleet, paper for the human** — 10–15 Devin threads bucketed into `bugs / P0 / P1 / P2 / investors`, with a handwritten weekly priority list held up on camera. The queue is machine-side; the priorities are deliberately in a different medium.
- **Playbooks as the reusable unit** — **Watchdog** (per-firm account monitoring: activity, Sentry errors, top three problems, checked against open PRs), **Land PR** (fresh Devin Review, up to two loops, then a narrated video walkthrough he watches before approving the merge), and an investor-update skill.
- **Standing automations** — a thrice-weekly end-to-end signup test (~$60/run), a daily 9am production watchdog, and a nightly quality-grading loop over **Grace**, Untangle's AI paralegal (~$5/session, ~3 fix PRs/day).
- **Least privilege by instinct** — agents never hold production credentials; sensitive actions are approved by hand.
- **Hiring as verification** — no phone screen, no interview: candidates submit a full-screen video of themselves building a feature, because the signal he wants is *how good an agent manager they are*.

## The anti-thesis

The most-cited line from his 2026 appearances cuts against the position everyone expects him to hold:

> "I really try to constrain my output — not quality, not on bugs — because I don't think I get multiples of quality off of multiples of output."

And on self-improving product loops: *"we're nowhere near any frontier model having the intelligence to know what to ship."* His prescription for finding product-market fit is unglamorous — he emailed a prospect, took a call, landed them, then asked to sit in their office. This puts him in direct disagreement with [[2026-08-14-blomfield-yc-building-structuring-ai-native-company|Tom Blomfield]] on whether the quality gate should be human.

## Appears in this wiki via

- [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder]] — guest on *[[How-I-AI|How I AI]]* with [[Claire Vo]]; the primary screen-share account of the whole setup.
- [[2026-07-25-darroman-profitable-founder-managing-ai-agents-25-prs-a-day]] — subject of Florian Darroman's write-up; the numerate version, with cadences, per-run costs and token economics.
- [[2026-02-09-li-aidev-studying-ai-coding-agents-on-github]] — not a subject, but his stack (Devin, Codex, Claude Code, Cursor, Copilot) is exactly the five-agent set the AIDev dataset covers.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "ryan-carson")
SORT file.name ASC
```
