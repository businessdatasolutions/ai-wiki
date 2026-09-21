---
type: source
kind: paper
title: "The role of the level of artificial intelligence adoption on business model innovation, sustainable competitive advantage, and firm performance: Integrating the TOE framework and Dynamic Capabilities theory"
author: ["Nguyen Thi Phuong Anh", "Bui Huy Khoi", "Nguyen Quang Thu", "Tran Nha Ghi"]
publisher: "Green Technologies and Sustainability (KeAi Communications; publishing services by Elsevier)"
journal_volume: "Vol. 4 (2026), article 100384"
peer_reviewed: true
url: "https://doi.org/10.1016/j.grets.2026.100384"
doi: "10.1016/j.grets.2026.100384"
date_published: 2026-03-28
date_ingested: 2026-09-21
length: "~16 pages (complete article read; Tables 7–10 reconstructed from flattened pdftotext output; Figures 1–4 are images that did not survive conversion)"
raw: "../../raw/papers/2026-03-28-nguyen-ai-adoption-toe-dynamic-capabilities.md"
tags: [ai-adoption, adoption-intensity, toe-framework, dynamic-capabilities, business-model-innovation, sustainable-competitive-advantage, firm-performance, government-support, top-management-support, pls-sem, vietnam, sme, emerging-economies, adoption-theory]
dynamic_capabilities:
  - contextual/internal-enablers
  - strategic-renewal/business-model
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: 2025-06-15-cimino-ai-adoption-sustainable-growth-smes
    via: "implementation depth, not readiness, is what reaches performance. Nguyen's level-of-adoption construct is close to Cimino's AI adoption intensity — 'AI technologies have significantly transformed our firm's business processes' against 'AI has substantially changed our business processes' — and in both models it is the adoption measure with a significant path to firm performance. The two place dynamic capabilities on opposite sides of adoption: Cimino as its cause, Nguyen as the mechanism that turns it into value"
    confidence: 0.7
  - type: supports
    target: 2025-01-08-khanfar-factors-influencing-ai-adoption-slr
    via: "top-management support as the leading organisational factor. It is the strongest antecedent of adoption level here (β = 0.286) and also raises perceived cost-effectiveness; Khanfar's review counts it among the most-cited factors and one of the few that act at both the firm and employee level"
    confidence: 0.7
  - type: supports
    target: 2024-08-13-schwaeke-new-normal-ai-adoption-smes
    via: "government support matters for small firms specifically. The multi-group analysis finds the government-support path to adoption level positive among SMEs (β = 0.247) and absent among large firms (−0.01; difference p = 0.036). Schwaeke's regulation cluster argues that policy should offset SMEs' financial constraints; this is a measured instance"
    confidence: 0.65
  - type: supports
    target: 2026-07-09-catlin-mckinsey-podcast-real-ai-advantage
    via: "value from AI arrives through redesign, not deployment. Catlin argues efficiency gains from bolted-on AI are competed away and advantage comes from redesigning what the firm does and offers; here the direct path from AI adoption level to performance is small (β = 0.125) while business-model innovation (0.417) and competitive advantage (0.321) carry most of the explained variance, which the authors read as AI's value being realised indirectly"
    confidence: 0.6
---

# Nguyen, Bui, Nguyen & Tran — AI adoption level, business-model innovation, competitive advantage and firm performance

## TL;DR

**The one paper in the wiki that puts the two firm-level theories into a single model.** TOE explains how far firms adopt AI; dynamic capabilities explain what that adoption turns into. It is a PLS-SEM survey of **325 middle and senior managers of Vietnamese firms that already use AI**: 28% small, 45% medium and 27% large firms, all in the Southeast region. It closes the open question [[technology-adoption-theories]] recorded when the paper could not first be retrieved.

The model runs in two halves:

- **TOE side — what drives the level of adoption.** Top leadership support → AI adoption level (β = 0.286), government support → AI adoption level (β = 0.177), and government support → top leadership support (β = 0.270) and → perceived cost-effectiveness (β = 0.303). Cost-effectiveness → adoption is only marginal (β = 0.106, p = 0.063).
- **Dynamic-capabilities side — what adoption turns into.** AI adoption level → business-model innovation (BMI, β = 0.200), → sustainable competitive advantage (SCA, β = 0.249), and → firm performance (FP, β = 0.125). BMI (β = 0.417) and SCA (β = 0.321) are the strongest drivers of performance.

**The distinctive result is a moderation**: the level of AI adoption strengthens the link from competitive advantage to performance (β = 0.123, p = 0.008). The authors read AI as an **amplifier** of advantages a firm already has, not as a source of advantage in itself. It does *not* moderate the BMI → performance link (β = 0.067, n.s.).

## Key claims

**Adoption as a level, not a yes/no.** The sample is restricted by design to firms already using at least one AI activity — analytics, process automation, decision support, forecasting or a chatbot. The dependent variable is therefore how deeply AI is integrated, not whether it was adopted. By self-report, 30% of firms are at a basic (experimental) level, 45% intermediate and 25% advanced. The authors present this as their first contribution: most adoption research asks *whether*; this asks *how far*.

**Government support works through leadership and cost.** Government support is the model's environmental factor, and it acts mostly indirectly: it raises leadership support and perceived cost-effectiveness more than it raises adoption directly. The authors tie this to Vietnam's national AI strategy and digital-transformation programmes as a strongly supportive institutional setting.

**Small firms lean on the state; large firms do not.** The multi-group analysis finds the structure largely the same across firm sizes except for one path: government support → adoption level is positive for SMEs (β = 0.247) and absent for large firms (β = −0.01), with a significant difference (p = 0.036).

**AI's value is mostly indirect.** Because BMI and SCA outweigh the direct AI → FP path, the conclusion is that "the value of AI is primarily realized indirectly through business model transformation and the strengthening of competitive positioning." The authors also concede that AI plays "a complementary rather than a primary role in driving BMI", since AI adoption explains only 4% of the variance in BMI.

## Dynamic-capabilities reading

- **`contextual/internal-enablers`** — top leadership support is W&W's "executive support" in TOE clothing. Its items are managers' willingness to risk AI adoption, knowing how AI can boost performance, and commitment to acquiring management and technical skills. It is the strongest antecedent of adoption level.
- **`strategic-renewal/business-model`** — business-model innovation is an outcome construct in its own right: redesigning customer value, adding participants to value generation, inventing new revenue streams. AI adoption level drives it, weakly.
- **`digital-transforming/improving-digital-maturity`** — the adoption-level construct is a maturity measure, with its basic / intermediate / advanced split. The model asks what raises it (leadership, government, cost) and what it produces.

The dynamic-capabilities theory is used at Teece's generic level — sensing, seizing, reconfiguring — and only as the *explanation* for the outcome paths. No sensing, seizing or transforming capability is measured. That is the difference from [[2025-06-15-cimino-ai-adoption-sustainable-growth-smes|Cimino et al.]], who measure the capability construct directly.

## Neighbour sources

[[2025-06-15-cimino-ai-adoption-sustainable-growth-smes|Cimino et al. (2025)]] is the closest neighbour and the mirror image. Cimino runs dynamic capabilities → AI adoption → performance; this paper runs TOE antecedents → AI adoption → dynamic-capability outcomes → performance. The adoption measures nearly coincide: Nguyen's "AI technologies have significantly transformed our firm's business processes" and Cimino's "AI has substantially changed our business processes". In both models, that implementation-depth measure is what reaches performance.

On the antecedent side it lines up with the two TOE reviews. Top leadership support is the strongest driver here, as it is among the most-cited both-level factors in [[2025-01-08-khanfar-factors-influencing-ai-adoption-slr|Khanfar et al. (2025)]]. The SME-only government-support effect is a measured instance of what [[2024-08-13-schwaeke-new-normal-ai-adoption-smes|Schwaeke et al. (2024)]] ask of policy in their regulation cluster.

On outcomes, the small direct AI → performance path next to large BMI and SCA paths fits [[2026-07-09-catlin-mckinsey-podcast-real-ai-advantage|Catlin's argument (McKinsey, 2026)]] that bolted-on efficiency gets competed away and advantage comes from redesign.

## Linked entities and concepts

- Concepts: [[technology-adoption-theories]], [[dynamic-capabilities]], [[enterprise-ai-adoption]]
- **Dangling** (single-source mention, deferred per the second-source promotion rule): Nguyen Thi Phuong Anh, Bui Huy Khoi, Tran Nha Ghi (corresponding author) — Industrial University of Ho Chi Minh City; Nguyen Quang Thu — University of Economics Ho Chi Minh City. The journal's running head cites the paper as "Anh et al."; the wiki uses the Vietnamese family name, "Nguyen et al."

## Scope and reliability

**What was read.** The complete article (user-supplied PDF from ScienceDirect). The tables were reconstructed from flattened text; Figures 1–4 are images. A first download attempt delivered a different paper (Dukhaykh & Alangri 2026, *Sustainability*), caught by the identity check and deleted before conversion.

**The outcome side explains little.** R² is 0.040 for business-model innovation and 0.062 for competitive advantage. AI adoption level is a significant predictor of both, but it accounts for a small share of either. The model explains firm performance moderately (R² = 0.438), mostly through BMI and SCA, not through AI.

**Reporting inconsistencies in the paper itself**, all recorded in the raw file:

- H11 and H12 swap labels between the hypotheses section and the results table.
- Cost-effectiveness → adoption is marked "Accepted" at p = 0.063.
- The estimated model's SRMR is 0.130 against the paper's own 0.10 threshold, and only the saturated model's 0.053 is reported in the text.
- The control-variable table's "before" and "after" columns do not match the main results.

This page cites the paths and confidence intervals, not the hypothesis verdicts.

**Competitive advantage and performance overlap in content.** One retained competitive-advantage item is "Our company's profits are better"; performance is ROA, ROE, ROS, market share and sales growth. The constructs separate statistically (HTMT 0.509), but part of the SCA → FP path relates profit to profit.

**Sample and method.** Adopters only, recruited by targeted rather than stratified sampling, from one region of one country. There is one respondent per firm, and performance is perceptual. The survey is cross-sectional, which the authors concede cannot show the resource reconfiguration over time that dynamic-capabilities theory describes. Common-method bias was checked by VIF only. The authors also flag that Vietnamese norms of respect for authority may inflate reported leadership support. Mean scores sit around 2.2–3.4 on a five-point scale, which the authors read as adoption still being early for many firms.
