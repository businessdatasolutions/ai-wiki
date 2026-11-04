---
type: source
kind: video
title: "Remote bouwt alles zelf met AI en koopt geen software meer | De Grote Tech Show"
author: ["BNR Tech"]
publisher: "BNR Nieuwsradio — De Grote Tech Show, hosts Joe van Burik and Ben van der Burg"
url: "https://www.youtube.com/watch?v=LUgXBVu2tKE"
date_published: 2026-10-29
date_ingested: 2026-11-04
length: "~32:57 minutes (transcript ~302 lines; Dutch)"
raw: "../../raw/videos/remote-bouwt-alles-zelf-met-ai-en-koopt-geen-software-meer-de-grote-tech-show.md"
tags: [bnr, de-grote-tech-show, dutch, remote, job-van-der-voort, global-payroll, employer-of-record, compliance, build-not-buy, saas, internal-tools, claude-code, single-database, ai-written-code, productivity-self-report, token-spend, ai-budgets, model-routing, local-models, remote-work, hybrid-work, change-management, ai-for-actual-work, mandatory-ai-training, cybersecurity, device-management]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/improving-digital-maturity
  - strategic-renewal/organizational-culture
relationships:
  - type: supports
    target: 2026-10-24-skidmore-cloudflare-connect-build-not-buy
    via: "companies building internal tools with coding agents instead of buying SaaS; Remote adds one shared database under every internal app, the answer to Skidmore's 'a thousand versions' worry"
    confidence: 0.7
  - type: supports
    target: 2026-07-06-sevilla-emarketer-custom-ai-coded-apps-trim-saas-expenses
    via: "firms replacing bought SaaS with AI-built apps; Remote, at 2,000 staff, is larger than the small firms Sevilla reports"
    confidence: 0.6
  - type: contradicts
    target: 2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free
    via: "whether firms will build their own software instead of buying SaaS: Remote's CEO says 'we basically don't buy software any more'; Ramineni: 'I don't think you can vibe code a CRM'"
    confidence: 0.6
  - type: supports
    target: 2026-10-20-hamalainen-lala-takkar-mckinsey-economics-of-enterprise-ai
    via: "AI spend growing fast enough to need budgets and routing to cheaper models: Remote's spend doubles about every month and staff hit daily budgets"
    confidence: 0.6
---

# Van der Voort (Remote) on BNR's De Grote Tech Show — building everything with AI, buying no software

> Bij Remote schrijft AI inmiddels 100 procent van de code. Aan het begin van dit jaar was dat nog zo'n 40 procent, zegt CEO Job van der Voort. Het bedrijf, dat in 2019 begon en wereldwijd salarisadministratie en HR regelt voor tienduizenden werkgevers, koopt daarom nauwelijks nog software in. Medewerkers bouwen hun eigen interne apps met Claude Code, allemaal op één gedeelde database.
>
> De productiviteit van een gemiddelde medewerker is volgens hem twee tot vijf keer zo hoog als een jaar geleden, en bij sommigen een factor 10 tot 100. Een van zijn AI-agents bouwt al drie weken aan één stuk aan een interne app en stuurt collega's een berichtje in Slack als hij een vraag heeft. Dat heeft een prijs: de uitgaven aan AI verdubbelen ongeveer elke maand, en Van der Voort loopt zelf ook tegen zijn dagbudget aan.

## TL;DR

A 33-minute Dutch-language episode of BNR Nieuwsradio's *De Grote Tech Show*, published 29 October 2026 on the BNR Tech channel. Hosts **Joe van Burik** and **Ben van der Burg** interview **Job van der Voort**, CEO and co-founder of **Remote**, a fully remote company founded in 2019 that runs payroll and HR for employers in most countries, with about 2,000 staff in more than 90 countries. Quotes below are translated from Dutch. Six claims, all his own estimates:

1. **AI writes all of Remote's code.** About 40% at the start of 2026, *"now we're at 100%."* *"Programming is simply solved. Full stop."* Code review is almost entirely automated too.
2. **Remote buys almost no software any more.** Staff build their own internal apps with Claude Code in a scaffold called **Labs**, which goes through normal, partly automated code review and inherits permissions. Every app points at **one shared database** instead of thousands of SaaS tools that need integrating.
3. **Productivity: 2 to 5 times per person, year on year**, and 10 to 100 times for some, depending on *"how much initiative they take."* He calls it *"very hard to measure."*
4. **AI spend doubles about every month.** Staff have budgets; *"my budget reset at 9 this morning and I'm already up against it."* Remote built its own harness that switches to cheaper models when it can, and runs local models for meeting transcription, but finds them not good enough for most of its work, which runs mainly on Anthropic's models.
5. **Training was made compulsory.** A suggestion reached only the enthusiasts, so every employee had to take Remote's own course, *AI for Actual Work* (free to the public since late August), which ends with building something in Claude Code. *"It's as if someone hasn't got their swimming certificate."*
6. **No change management, because change is constant.** *"There's no longer a job, at least at our company, where you can do the same thing for five years."*

## Key claims

### How the payroll platform was built

Remote set up a company in each country by *"literally flying there"*, visiting the bank and the town hall, and then wrote software for what it learned: a large calculator over country-specific inputs, continuously checked for compliance. In the Netherlands and the UK the average customer is now *"fully automated"*; payments run on Remote's own treasury system. What remains is exceptions, such as a pregnant employee working from home in England for a US company who falls down the stairs. He estimates, as *"a very rough estimate,"* that about 40% of staff work on exceptions and compliance. Remote automates by scoring each action on frequency and pain.

### An agent running for three weeks

One of his agents has run *"for three weeks without stopping"* on a complex internal app from a single high-level instruction. When it has a question it sends a Slack message to the colleague who is the subject-matter expert, stores the answer and continues; now and then it asks him to test. The result works but *"could be a bit more elegant"*; a stronger model or more reasoning effort would help, *"but I can't afford that, unfortunately."* He cites task costs falling 30 to 100 times in about nine months and a new frontier model every 18 days.

### What people do now

*"The original programmer wasn't busy implementing what was in his ticket"* but with the problem behind it, and that is now what everyone does: *"you say, this is the problem and this is what I want at the other end. Figure it out."* He would not hire as many people if he started again, but keeps the 2,000 *"so that they can do 100 times more."* He expects most office work done on computers today to *"disappear completely,"* and most people not to work 40 hours in an office in five to ten years.

### People, security and SaaS

First-line support is an AI agent; sensitive matters go to a person on a call. On security, *"those models can hack in so easily"* that the risk is now automated attacks rather than people; all devices are managed and wiped remotely if lost, and Remote uses security-specialised models from Anthropic and OpenAI. On SaaS vendors: many still earn well on long licences and *"now have to work very hard"* to show value.

## Dynamic-capabilities reading

- **`digital-seizing/balancing-digital-portfolios`**: the internal-versus-external choice decided for internal: software built in-house on one database instead of bought.
- **`digital-transforming/improving-digital-maturity`**: a compulsory, hands-on AI course for every employee, so that *"build it yourself"* can be expected of everyone.
- **`strategic-renewal/organizational-culture`**: constant change as the norm instead of change programmes, and the expectation that each person evaluates their own job.

## How it connects

- [[concepts/vibe-coding|vibe-coding]] — personal and internal software built by non-engineers, at company scale.
- [[concepts/agentic-engineering|agentic-engineering]] — "programming is solved", problem-first instructions, a three-week agent run.
- [[concepts/ai-coding-productivity-evidence|ai-coding-productivity-evidence]] — 40% to 100% AI-written code and a 2 to 5x self-estimate.
- [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] — mandatory training after a voluntary one failed.
- [[concepts/ai-employment-effects|ai-employment-effects]] — flat headcount kept on purpose, and a forecast that most office work disappears.
- [[concepts/small-language-models|small-language-models]] — local models for transcription, judged not good enough for core work.

## Related in this wiki

- [[2026-10-24-skidmore-cloudflare-connect-build-not-buy|Skidmore (Cloudflare Connect)]] — building got cheap, owning is the problem: *"a thousand versions of … the same software."* Remote's single database and scaffold are its answer to that.
- [[2026-07-06-sevilla-emarketer-custom-ai-coded-apps-trim-saas-expenses|Sevilla (EMARKETER)]] — small firms replacing Salesforce; the article limits the case to small companies and those with in-house engineering. Remote is both larger and engineering-heavy.
- [[2026-10-07-ramineni-browserbase-fireflies-gives-software-away-free|Ramineni (Fireflies)]] — *"I don't think you can vibe code a CRM."* Van der Voort's claim is the opposite, though he names no system of record that Remote replaced, and his examples are internal tools.
- [[2026-10-20-hamalainen-lala-takkar-mckinsey-economics-of-enterprise-ai|McKinsey on the economics of enterprise AI]] — a bank's spend rising from $3M to $25M without controls; Remote's monthly doubling and daily budgets are the same pressure in a 2,000-person firm.
- [[2026-10-19-lloyd-warp-what-it-takes-to-build-a-software-factory|Lloyd (Warp)]] — Remote's course includes a *software factory* module.

## What was actually ingested

The full episode (32:57, `length_seconds: 1977`) from the Dutch auto-generated transcript, 302 lines; quotes are translated here. ASR corrected against the description: *Job van de Voort* and *Job van der Voord* are Job van der Voort, *Joe van Buurik* is Joe van Burik, *Claud* and *clot* are Claude, *Entropic* is Anthropic, *aiualworkwork.com* is aiforactualwork.com. No stills: a radio-studio video.

## Linked entities and concepts

- [[Anthropic]], [[Claude Code]] — the models and tool Remote runs on.
- [[concepts/vibe-coding|vibe-coding]], [[concepts/agentic-engineering|agentic-engineering]], [[concepts/ai-coding-productivity-evidence|ai-coding-productivity-evidence]], [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]], [[concepts/ai-employment-effects|ai-employment-effects]], [[concepts/small-language-models|small-language-models]], [[concepts/agent-harness|agent-harness]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the three cells tagged above.

**Dangling** (single-source mention, deferred): BNR Tech (first `author:` source), BNR Nieuwsradio, De Grote Tech Show, Joe van Burik, Ben van der Burg, Remote, Job van der Voort, AI for Actual Work, Orange Cyberdefense (sponsor).

## Scope and reliability

A CEO describing his own company on a general-audience radio show, with no data shown. Every figure is his own estimate, several marked as rough. "100% of code" and "programming is solved" are claims about Remote's engineering, not measurements, and his productivity range is self-assessed. The build-not-buy claim is about internal tools; he does not say Remote replaced its own payroll engine or a system of record bought from a vendor. Remote also sells to HR buyers, so a message that it runs on AI is part of its brand.
