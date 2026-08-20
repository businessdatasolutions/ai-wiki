---
type: concept
aliases: ["AI washing", "AI-washing", "AI wash", "AI washing layoffs"]
tags: [ai-washing, ai-employment-effects, labor-market, narrative, greenwashing, attribution, layoffs]
confidence: 0.77
last_confirmed: "2026-08-20"
accessed_at: "2026-08-20"
source_count: 3
relationships:
  - type: part-of
    target: ai-employment-effects
    via: "the attribution/narrative confound layer of the AI-employment question — why the AI-as-cited-reason-for-layoffs signal is hard to take at face value"
quality_score: 0.99
quality_notes: ['1 near-empty section(s)']
---

# AI Washing

**AI washing** is the practice of a company **citing AI as the reason for layoffs (or other unpopular changes) it would have made anyway** — using a new, market-favoured technology as the narrative cover for a decision driven by something else (overhiring, a bad quarter, macro-economic pressure). The term is built by explicit analogy to **greenwashing**: just as firms once dressed cost-driven or compliance-driven choices in climate language, firms now dress headcount cuts in AI language.

This page is the **attribution-and-narrative layer** that sits beside [[ai-employment-effects]] (the empirical record of AI's measured effect on jobs, hiring, and wages). Where that page asks *"what is AI actually doing to employment?"*, this concept asks the prior question: *"how much of what companies attribute to AI is real, and why would they over-attribute?"* It is a confound on the entire AI-layoffs narrative, not a measurement of it.

## The mechanism: a stock-market valuation premium

The load-bearing claim, from labor economist **Kathryn Anne Edwards** ([[2026-06-22-bbc-what-if-were-wrong-about-ai-layoffs|BBC / "New Normal with Katty Kay", June 2026]]): AI is **not treated neutrally by the stock market**. A company "seen to embrace AI or be an AI company… is seen as being a better investment, and their value goes up." Therefore:

- Saying you laid people off because you **overhired** "is probably not going to do much for your shareholders."
- Saying you laid people off because you **pivoted to AI** "could make your company seem more valuable."

AI washing is thus a *narrative-for-shareholders* move. Edwards frames it as routine ("a tale as old as time in the US economy" — the *iPads-instead-of-clerks-because-of-the-minimum-wage* analogy; "fall guys and narratives are just part and parcel of the U.S. economy"), amplified by **downturn peer pressure**: when several public companies announce 5% layoffs citing AI, the unstated question to the others becomes "are you doing AI?" — a coordination signal even when "we can't measure it and we can only sense it."

This supplies the *why* under the data the wiki already holds: the [[2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs|Giles / WP Intelligence]] report's Challenger, Gray & Christmas finding that *"AI is the #1 cited reason for job cuts"* in March and April 2026 (alongside NACE's survey showing only **14%** of employers had considered replacing entry-level roles with AI, most citing economic outlook), and the [[2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering|Everitt]] talk's *"mega-layoffs at Atlassian / Block / Stripe / Amazon… why do they do it? Their stock price goes up."*

## The executive-altitude counter-framing ([[Sam Altman]] via [[2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering|Everitt 2026]])

The term entered the wiki before it had a page, via [[Sam Altman]]'s public use of it: Altman "accused some firms of *AI washing* — using AI as justification for headcount cuts that were planned independently," cited by Paul Everitt ([[2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering|Everitt 2026]]) as the counter-anchor to the *"more code, fewer people"* mega-layoff narrative. That an AGI-bull OpenAI CEO is among the loudest voices naming AI washing is itself notable — it is the wiki's clearest **executive-altitude public pushback** on the AI-justifies-layoffs framing, and it converges with Edwards's labor-economist mechanism from the opposite end of the credibility spectrum.

## Why attribution is near-unmeasurable

Edwards's second claim: the labor-market data on AI's effect "is just very inconclusive, and it'll likely stay inconclusive forever." The reasoning is historical-analogical — ask how many jobs were lost to **"computers"** since 1955, and a few cases are clean (typists, phone operators, the occupation "computer" that was largely women — see [[ai-deskilling]]), but the *total* attributable job loss is not recoverable "with any degree of certainty." Same for the internet; same for Microsoft Office. This is the popular-explainer twin of the methodologically disciplined stance in [[2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai|Massenkoff & McCrory (Anthropic)]] — *establish the measure before effects emerge, because past labor forecasts over-predicted* — and of Tim O'Reilly's [[2026-01-09-baron-signals-for-2026|"AI is not taking jobs: the decisions of people deploying it are"]] attribution framing. AI washing is the *corporate-incentive* explanation for why the attribution noise runs in one direction (toward over-crediting AI).

## Weak market penalty

Unlike greenwashing — where upset consumers can switch to a competitor's retail shelf — many AI-washing firms "don't necessarily have customers" in the consumer-discipline sense, so even amid "incredible pushback" against AI (e.g. community rejection of data centres) there is little market mechanism to punish the misattribution. The narrative cost is low and the valuation benefit is real, which is precisely why the practice persists.

## The narrative-distortion harm

Edwards's normative worry is that the **amplified narrative itself distorts decisions** — "narrative is everything," even to an economist who "cares about numbers." Two harms:

- **Career mis-optimisation.** Young people optimise for "AI-proof" majors and careers, but "that may not be the reason that some companies are slimming down their workforces anyway" — they are hedging against a cause that may be misattributed.
- **Ignored counter-data.** Edwards's cited datapoint: **Indeed software-development job postings** went from much *lower* than overall postings at the start of 2024 to **four times as high** by mid-2026, outperforming overall jobs over the prior ~year — *"so not the narrative that's out there."* This is a journalist-surfaced counterweight to the [[2026-04-30-ai-index-report-2026|AI Index 2026]] / [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson Canaries]] entry-level-decline finding, aligned with the lump-of-labor pole ([[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Evans]]) and the [[2026-05-01-lf-state-of-tech-talent-global-2026|Linux Foundation "not a jobs crisis"]] surveys. It is *narrative critique*, not a new measurement (single chart, single platform), and should be weighted accordingly.

## "These are not outcomes, they're outputs" — the output/outcome confusion as the enabling condition ([[2026-08-19-rohrer-goto-modern-enterprise-architecture-architecting-for-outcomes|Rohrer / GOTO Copenhagen 2025]])

A third source for this page, and a useful one because it is not about AI and predates most of the corpus's return-gap material.

Rohrer, listing the outcomes a modern enterprise-architecture practice should target, pauses on the wrong answers: *"Maybe we're looking for — we want to move everybody to cloud, or **we want to get everybody using AI these days**, or we want to move everybody to Kubernetes or microservices. **No, these are not outcomes. They're outputs.**"*

Two things this adds to the page.

**It locates the mechanism upstream of the marketing.** AI-washing is usually treated here as a claim problem — a firm asserting AI capability it does not have. Rohrer's line points at the condition that makes such claims *legible as achievements in the first place*: an organisation that measures technology penetration rather than business result will reward "we are using AI" as a completed objective, internally and externally, with no dishonesty required at any step. Washing is easiest where the scorecard already counts outputs.

**It generalises the pattern out of the AI era.** AI appears in his list alongside cloud migration, Kubernetes and microservices — i.e. as the current instance of a recurring enterprise-technology failure rather than something new. That is a mild but real counterweight to the corpus's tendency to treat AI-washing as a novel phenomenon; the wiki should expect the same dynamics documented for prior technology waves to transfer.

His replacement — *better value sooner, safer, happier*, anchored on the firm's actual value proposition — is the constructive half, and it is the same move the return-gap sources make when they insist on business-outcome measurement over adoption metrics. See [[enterprise-ai-adoption]], where the quote is recorded alongside the other August-2026 adoption-gap material.

**Confidence raised 0.72 → 0.77** on the third independent source, with the caveat that this one addresses the mechanism obliquely — it is a talk about enterprise architecture, and the AI reference is a single clause in a list.

## Debates and supersession
## Debates and supersession

- **AI washing vs. real AI displacement — not mutually exclusive.** The concept is a confound, not a denial. The empirical record on [[ai-employment-effects]] (Brynjolfsson's ~13% relative early-career decline; the AI Index's −20% software-dev employment from 2024; Massenkoff & McCrory's ~14% junior job-finding-rate drop) is load-bearing and independent of attribution games. AI washing says *some* of the AI-cited layoffs are misattributed and the true share is unknowable — not that AI has no labor-market effect. The two readings coexist: real displacement at the entry-level margin, plus a layer of over-attribution on top.
- **How big is the washing share?** Genuinely unknown and, per Edwards, possibly unknowable "with any degree of certainty." The Giles/Challenger "AI #1 cited reason" data and the NACE "only 14% considered it" data are the two poles bracketing the uncertainty; the gap between them "is where the empirical noise lives" (per [[ai-employment-effects]]).
- **Does the valuation premium persist?** The mechanism depends on the stock market continuing to reward AI affiliation. If "incredible pushback" against AI matures into investor skepticism, the premium — and thus the incentive to AI-wash — could invert. Worth tracking.
- **Source-tier caveat.** Both current sources are non-peer-reviewed: one journalistic explainer-interview (Edwards/BBC) and one second-hand citation of an executive's public statement (Altman via Everitt). Confidence is held at 0.72 pending an empirical study that *quantifies* the misattribution share. The specific Altman statement(s) Everitt cites are not pinned to a date — an open tracking item on the [[Sam Altman]] page.

## Related concepts

- [[ai-employment-effects]] — the empirical record this concept is the attribution-confound layer of.
- [[ai-deskilling]] — the clean historical displacement cases (typists, phone operators, the "computer" occupation) Edwards uses to argue attribution is hard.
- [[enterprise-ai-adoption]] — AI washing is a signalling distortion in the same market where genuine adoption is measured.
- [[responsible-ai]] — misattributing layoffs to AI is a corporate-narrative integrity concern adjacent to the labor-disruption RAI thread.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "ai-washing")
SORT file.name ASC
```

## Open questions

- **Quantifying the washing share.** No source yet measures what fraction of AI-cited layoffs were planned independently. A difference-in-differences design (layoff announcements with vs. without AI framing, controlling for prior hiring and quarter performance) would be the natural instrument.
- **Does AI washing inflate the measured "AI exposure → layoffs" correlation?** If firms selectively *attribute* layoffs to AI in AI-exposed occupations, naïve attribution studies would over-estimate the causal effect. Worth flagging to any future [[ai-employment-effects]] measurement ingest.
- **Primary source for Altman's statement.** Carried second-hand via [[2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering|Everitt]]; a direct Altman source would substantiate it.
