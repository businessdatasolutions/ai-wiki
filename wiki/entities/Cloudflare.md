---
type: entity
kind: organization
aliases: ["Cloudflare", "Cloudflare, Inc.", "Cloudflare Inc", "NET"]
tags: [cloudflare, web-infrastructure, cdn, bot-management, ai-crawl-control, workers, isolates, agents-sdk, code-mode, x402, web-bot-auth, cloudflare-radar, agentic-internet]
website: "https://www.cloudflare.com"
since: 2009
confidence: 0.75
last_confirmed: "2026-09-19"
accessed_at: "2026-09-19"
source_count: 2
---

# Cloudflare

Web infrastructure and security company (NYSE: NET), co-founded by **Matthew Prince** (CEO) and **Michelle Zatlyn** (President). Its network sits in front of more than **20% of the web**, including 36% of the top 10,000 sites and 42% of the Fortune 500. By its own count it also serves about **78–80% of leading generative-AI products**. That position lets it see both sides of the agentic web: the publishers being crawled and the AI companies crawling them.

In this wiki it matters in three roles.

1. **An instrument.** Cloudflare Radar gives the corpus its only **network-layer measurements** of the agentic shift. They show agent traffic passing half of all Internet traffic, 52% of crawler requests being for AI training, human traffic down 35–40% in four industries within a year, and daily agent requests up 1,700%+. See [[2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet]] and [[agentic-web]].
2. **A market maker with a stake.** Since July 2025 ("Content Independence Day") it has **blocked AI training crawlers by default** on new domains. It sells the crawler controls, analytics and payment rails (**x402**, co-founded with Coinbase and Stripe; **Web Bot Auth**) that it argues the agentic web needs. Its data and its commercial interest point the same way, which is the main caution on everything it publishes about this.
3. **An AI-first operator.** Per its [[2026-06-09-cloudflare-investor-day-2026|Investor Day 2026 deck]]:
   - an internal agent workspace (**Cloudflare OS**) with a centrally managed skill-file context layer;
   - AI code review on every merge request (131,246 reviews in 30 days at a median $0.98);
   - a long-term model that cuts G&A to 3–5% of revenue;
   - a disclosed plan to reduce its workforce as it moves to an *"agentic AI-first operating model."*

   See [[enterprise-ai-adoption]] and [[ai-employment-effects]].

## Appears in this wiki via

- [[2026-06-09-cloudflare-investor-day-2026]] — the 193-slide Investor Day deck: code mode, the CPU-as-bottleneck argument, Cloudflare OS, the web-economy data, x402, the time-to-exploit chart, and the AI-first operating model.
- [[2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet]] — the one-year report on default crawler blocking and the licensing market it produced.

## Other mentions in the corpus

These sources mention Cloudflare without linking here:

- **Code mode.** [[2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering|Everitt]] names Anthropic and Cloudflare's code mode (the agent writes code and runs it in a sandbox) as the tooling layer of agentic engineering.
- **Mission.** [[2026-05-10-ries-lennys-force-destroys-companies-within|Ries]] uses Cloudflare's defence of pro-democracy protesters, when larger firms declined, as the book's mission-emergence case.
- **Tools.** O'Reilly's Radar Trends notes its *Markdown for Agents* HTML-to-markdown service ([[2026-03-03-loukides-radar-trends-march-2026|March 2026]]) and the EmDash WordPress alternative ([[2026-05-05-loukides-radar-trends-may-2026|May 2026]]).
- **In a demo.** A Cloudflare Worker is the CORS proxy in [[2026-04-18-mysore-medium-wikizz-extending-karpathy-llm-wiki|WikiZZ]].

## Open questions

- **How much of the licensing market is Cloudflare's doing?** The 50+ publisher–AI agreements it cites are an industry count. It does not say how many it brokered or enabled.
- **Is the time-to-exploit chart sourced?** The Investor Day slide showing exploitation windows under 24 hours in 2026 cites no data source; see [[attack-surface-management]].
- **What did the workforce reduction amount to?** It was disclosed as a plan with no size, timing or functions given.
