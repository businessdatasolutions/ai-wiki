---
type: concept
aliases: ["micro-productivity trap", "micro-productivity-trap", "offering lock-in", "process lock-in"]
tags: [micro-productivity-trap, AI-transformation, EBITDA, process-redesign, workflow-redesign, enterprise-ai]
---

# Micro-Productivity Trap

A failure pattern in enterprise AI deployment, named in [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Dutt, Rapoport, Chatterji, Weeratunga & Satcher (2026)]]. Firms invest heavily in AI, treat it as plug-and-play SaaS with isolated use cases, and realize **task-level productivity gains** that **fail to translate into firm-level business value** — because the surrounding workflow still depends on tacit knowledge, manual handoffs, or legacy systems not built for AI.

The framing distinguishes this article's argument from generic "ROI of AI" complaints by giving the failure mode a structural name and two named sub-modes.

## Working definition

> "AI can accelerate a task, but unless companies address workflow bottlenecks, productivity gains may not translate into business value." — [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Dutt et al. 2026]]

Two specific lock-ins, frequently co-occurring:

| Lock-in | Definition |
|---|---|
| **Offering lock-in** | AI applied to optimize the *existing* product/service rather than reframe what value the firm provides |
| **Process lock-in** | AI applied to automate *current* processes step-by-step rather than rebuild around an outcome |

The escape from the trap is **"reinvent the business"**: an organization-wide, future-focused, outcome-oriented posture that explicitly assumes "we live in a world in which powerful AI tools exist" and rebuilds workflows on that premise.

## Key claims

### Empirical anchor: 10–25% EBITDA gains for the transformation mindset

[[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Bain client work]]: firms that escape the trap and adopt the four-step transformation framework (below) report **10–25% EBITDA gains** that continue to scale as programmes scale.

### The four-step framework for escape

1. **Narrow possibilities strategically** — pick 4–5 critical domains. Top-4 across Bain's portfolio: software development, customer support, knowledge worker efficiency, marketing.
2. **Reimagine workflows across the organization** — process redesign is "the most challenging part of AI deployment" and "creates most of the value." Cross-functional, not silo-by-silo.
3. **Engage those closest to today's process** — top-down + bottom-up; prototyping culture in *all* business areas, not just the tech team.
4. **Measure what matters** — concrete business-outcome metrics with non-AI baselines, *plus* continuous **evals** (evaluation suites for AI behaviour).

### Worked cases

- **[[Lowe's]] + [[OpenAI]] partnership** (Mylow / Mylow Companion, March 2025): >2× online conversion when customers engage Mylow; +200 bps customer satisfaction when associates use Mylow Companion; deployed across 1,700+ stores.
- **FabricationCo** (anonymized Fortune 1000 manufacturer; Bain client): 14 use cases identified, ~$30M additional profit on track; quote-generation **~15× faster**; **+10pp win-rate increase in 3 months**.

### The boardroom imperative

Lagging firms recognize AI as important but **delegate** it to technology groups without specific goals or metrics. The article argues this delegation pattern is a structural cause of the trap — AI transformation requires top-of-house ownership with ambitious, business-owned targets.

## Cross-source positioning (descriptive only, per cross-source neutrality)

The micro-productivity-trap framing sits among several wiki vocabularies addressing the same broad territory of "AI adoption breadth ≠ transformation depth":

- [[2026-04-28-anand-wu-genai-playbook|Anand-Wu's 2×2]] — *where* to deploy GenAI (cost-of-errors × type-of-knowledge).
- [[2026-04-28-werner-lebrun-octopus-organization|Werner & Le-Brun's Octopus / Tin-Man]] — *adaptive vs predictability-optimized* organizational design.
- [[2026-04-28-mit-sloan-ai-maturity|MIT CISR Four Stages + Four S]] — *staged maturity* (28%/34%/31%/7% distribution; only 7% Stage 4) and *Strategy / Systems / Synchronization / Stewardship* challenges.
- [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]] — *chatbot → agent → multi-agent* progression and 5-foundations readiness framework (only 13% AI-ready).
- [[2026-04-28-bansal-birkinshaw-systems-thinking|Bansal & Birkinshaw systems thinking]] — *flows and relationships* over products/services.
- [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation|Warner & Wäger]] — *digital sensing/seizing/transforming* nine microfoundations under Teece.
- [[2026-05-03-rewired-second-edition-sample|McKinsey "Rewired" 2nd ed (2026)]] — *6 capabilities* (business-led roadmap, talent, operating model, technology, data, adoption-and-scaling); 20% EBITDA uplift / $3:$1 / 1–2yr breakeven across ~20 deep-dive AI-leader companies; 70% talent-density shifts.
- [[2026-04-30-ai-index-report-2026|AI Index 2026]] — empirical context: 88% organizational AI adoption but **AI agent deployment in single digits per business function**.

Each names the same broad gap with a different vocabulary; the wiki's [[organizational-frameworks-for-ai-adoption|organizational-frameworks-for-ai-adoption]] thread tracks this convergence.

## Related concepts

- [[automation-vs-augmentation]] — *process lock-in* maps to automation-without-redesign; *reinvent the business* to outcome-oriented augmentation.
- [[enterprise-ai-adoption]] — broader concept; this is one diagnostic lens within it.
- [[dynamic-capabilities]] — escape from the trap requires the digital sensing/seizing/transforming microfoundations.
- [[systems-thinking]] — the workflow-redesign step is systems-thinking applied to AI.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "micro-productivity-trap")
SORT file.name ASC
```

## Open questions

- Single-source coverage so far. A second source measuring or naming the same failure pattern (e.g. via McKinsey or a different consultancy/academic vantage) would strengthen the concept.
- Empirical 10–25% EBITDA range is from Bain client work — vendor-of-deployment data, not independent measurement. Independent verification (academic field study, AI Index data) would be a useful counterweight.
