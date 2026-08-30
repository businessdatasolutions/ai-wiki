# Managing AI Agents: How One Founder Ships 25 PRs a Day, Solo

**Author:** Florian Darroman
**Publication:** Profitable Founder
**Date:** 25 July 2026
**URL:** https://www.profitablefounder.xyz/blog/managing-ai-agents
**Captured:** 2026-08-30 (WebFetch — HTML-to-markdown extraction)
**fulltext_source:** web-extract

---

## Subject

Ryan Carson runs **Untangle** (legal technology for divorce law firms) entirely solo, shipping **22–25 pull requests a day, sometimes 40**, by managing a team of cloud-based AI agents instead of hiring employees.

## Lesson 1 — Cloud work over local development

> "If you are working locally, I honestly think you are a caveman."

The argument: local coding caps parallelism at what one machine and one attention span can hold. Cloud agents solve the collision problem by giving **an isolated virtual machine per session**. Carson runs **5–10 cloud agents simultaneously** — "at least 5, often 10." The PR volume comes from **horizontal scaling of ordinary agents, not from one super-agent**.

## Lesson 2 — Decision load explodes before output does

Where a developer might make 2–3 high-stakes decisions a day, Carson faces **10–20 before lunch**. Countermeasures:

- **Pin priority threads** — only **3 of ~25 daily PRs** get focused attention
- **A 25-minute check cadence** — regular but bounded review intervals, to bound decision fatigue
- **Analog task tracking** — a paper to-do list holds the week's priorities
- **Mobile work** — roughly half his work happens in an iPhone browser
- **Production access controls** — agents never hold production credentials; sensitive actions are manually approved

## Lesson 3 — Three "sleeping automations"

1. **End-to-end signup test** — runs three times weekly; an agent completes the full user workflow, records video, identifies bugs, files fixes. **~$60 per run.**
2. **Production watchdog** — daily at 9am; reviews the previous 24 hours of customer activity, summarising insights and anomalies with session links. Executive-level visibility into actual usage.
3. **Self-improvement loop** — daily grading of conversations held by **Grace** (Untangle's AI paralegal) against a quality rubric; substandard interactions trigger child agents that generate fix PRs. **~$5 per session; ~3 loop-generated fixes ship per day.**

## Economics

- Monthly token spend: **$20,000** — Carson calls this unsustainable
- Estimated sustainable level: **~$5,000/month per engineer-equivalent**
- Route there: **model routing** — expensive frontier models for complex reasoning, fine-tuned coding models for repetitive work; **parent-child agent patterns** keep premium models off routine tasks
- Business-model prediction: **$200/month all-you-can-eat plans will not survive.** Carson favours independent platforms (Devin, Factory, Amp) that optimise model economics for production use

## Implementation ladder (the article's on-ramp)

1. Run a single cloud agent session
2. Operate three agents simultaneously
3. Build one automation — **the production watchdog is the recommended highest-signal entry point**
4. Add a quality-grading loop on your core product surface

## Core thesis

Managing AI agents is the emerging founder skill set. Technical depth now develops through **delegation and judgement** rather than through typing lines of code.
