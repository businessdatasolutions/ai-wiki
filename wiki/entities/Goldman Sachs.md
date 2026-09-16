---
type: entity
kind: organization
aliases: ["Goldman Sachs", "The Goldman Sachs Group", "Goldman Sachs Group, Inc.", "GS"]
tags: [goldman-sachs, financial-services, investment-banking, enterprise-ai-adoption, agentic-ai, marco-argenti, data-readiness]
since: 1869
confidence: 0.8
last_confirmed: "2026-09-16"
accessed_at: "2026-09-16"
source_count: 4
---

# Goldman Sachs

Global investment bank and financial-services firm. In this wiki Goldman appears in two roles: as a **first-party enterprise-AI practitioner** (via its CIO's account of firmwide agentic-AI deployment) and as a **named analyst voice** on occupational AI exposure. Promoted to an entity on 2026-06-13 on its second substantive wiki appearance.

## Appears in this wiki via

- [[2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset|Argenti (HBR, June 2026)]] — **Marco Argenti**, Goldman's **Chief Information Officer** (ex-AWS VP), authors the *mindset-not-skillset* essay. Draws directly on Goldman's own AI work: applying agentic AI to **client onboarding** by first codifying "what good looks like" (process-quality metrics + experienced-operator decisions), then building evals comparing agent outputs to desired outcomes with feedback loops. Argenti's load-bearing operating claim — *"AI transformation follows data transformation, not the other way around"* — is the wiki's clearest first-party CIO articulation of data-readiness as the gate on [[enterprise-ai-adoption]].
- [[2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs|Giles / WP Intelligence (May 2026)]] — cited as the source of the **legal-firms-and-life-sciences-most-exposed** occupational-exposure analysis.

## Notable people (in this wiki)

- **Marco Argenti** *(dangling — single-source author; Goldman CIO, ex-AWS VP; strong promotion candidate on second-source coverage)* — author of the HBR *mindset-not-skillset* essay.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link)
SORT file.name ASC
```

## As a publisher of AI commentary (added 2026-09-16)

Goldman entered the wiki as an *adopter* of AI (via Marco Argenti and the data-readiness material). Two sources ingested on 2026-09-16 add a second and quite different role: Goldman as a **publisher of house views on AI's economics**, through its Private Wealth Management video series, interviewed in both cases by **Sharmin Mossavar-Rahmani**, CIO of Wealth Management and head of the **Investment Strategy Group**.

- [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs]] — **Jan Hatzius**, chief economist and head of **Global Investment Research**, on the macro aggregates: AI investment contributing ~0.1pp to US GDP growth, ~$600bn US / ~$1tn global CapEx, a ~15% productivity uplift diffusing over a decade, and an occupation-level employment correlation that is *"quite small."*
- [[2026-08-18-covello-gs-new-models-ai-investment-landscape]] — **Jim Covello**, head of **Global Equity Research**, on the value chain: *"enterprises collectively are not making or saving money on their AI implementations,"* with all the economic value accruing to the semiconductor layer, and a missing data-management plus model-orchestration layer as the bottleneck.

**A provenance caveat that applies to both, and that a reader should not skip.** Each video's description states it *"represents the views of the Wealth Management Investment Strategy Group and is not a product of Goldman Sachs Global Investment Research (GIR). It is not research and is not intended as such."* Yet **Hatzius heads GIR** and **Covello heads Global Equity Research within it**, and the numbers they quote are GIR estimates and GIR survey work. The practical consequence: these figures are **research-derived but relayed in a format Goldman explicitly declines to stand behind as research**, and none of the underlying notes has been ingested. Cite them as reported in an interview, never as published Goldman research.

Note also that Goldman runs substantial businesses on every side of the trade being discussed — it is an adopter, an underwriter, a market-maker and a research publisher in the same subject.

## Open questions

- **No underlying Goldman research has been ingested** — only two interviews relaying it. The GIR notes behind the 0.1pp GDP contribution, the 15% productivity uplift, the 25%/6–7% task decomposition and the *"all the economic value"* survey work are all uncited and unexamined.
- Whether the ISG/GIR separation is meaningful in practice, or a disclaimer formality, is not something the wiki can judge from the sources it holds.
