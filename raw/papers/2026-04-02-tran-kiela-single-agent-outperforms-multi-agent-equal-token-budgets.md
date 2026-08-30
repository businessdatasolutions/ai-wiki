# Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets

**Authors:** Dat Tran, Douwe Kiela
**arXiv:** 2604.02460 (v1 2 April 2026; v2 11 April 2026)
**URL:** https://arxiv.org/abs/2604.02460
**Captured:** 2026-08-30 (WebFetch of the arXiv abstract page)
**fulltext_source:** abstract-only — abstract verbatim below.

---

## Abstract (verbatim)

> Recent work reports strong performance from multi-agent LLM systems (MAS), but these gains are often confounded by increased test-time computation. When computation is normalized, single-agent systems (SAS) can match or outperform MAS, yet the theoretical basis and evaluation methodology behind this comparison remain unclear. We present an information-theoretic argument, grounded in the Data Processing Inequality, suggesting that under a fixed reasoning-token budget and with perfect context utilization, single-agent systems are more information-efficient. This perspective further predicts that multi-agent systems become competitive when a single agent's effective context utilization is degraded, or when more compute is expended. We test these predictions in a controlled empirical study across three model families (Qwen3, DeepSeek-R1-Distill-Llama, and Gemini 2.5), comparing SAS with multiple MAS architectures under matched budgets. We find that SAS consistently match or outperform MAS on multi-hop reasoning tasks when reasoning tokens are held constant.

## Key points

- Reported MAS gains are **confounded by extra test-time compute**; normalise the budget and the gain largely disappears
- **Information-theoretic argument grounded in the Data Processing Inequality:** under a fixed reasoning-token budget with perfect context utilisation, a single agent is more information-efficient (decomposition across agents can only lose information)
- **Prediction:** MAS become competitive precisely when a single agent's *effective context utilisation degrades*, or when you are willing to spend more compute
- Tested across three model families — Qwen3, DeepSeek-R1-Distill-Llama, Gemini 2.5 — against multiple MAS architectures at matched budgets
- **Result: SAS consistently match or outperform MAS on multi-hop reasoning at equal reasoning tokens**

## Date note

Dated **April 2026**, not 2025. Any citation attributing this to 2025 is wrong.
