---
type: concept
aliases: ["foundation model", "foundation models", "FM", "frontier model", "frontier models"]
tags: [foundation-models, generative-ai, ai-research]
---

# Foundation Models

Large pretrained models — typically transformer-based — that serve as the substrate for downstream AI applications via prompting, fine-tuning, or retrieval. Foundation models drive most modern [[generative-ai]] capability and are the locus of the "frontier" debate (capability, safety, transparency).

## Working definition

A **foundation model** is a model trained on broad data at scale that can be adapted to a wide range of downstream tasks. The term, coined by Stanford's [[Center for Research on Foundation Models]] (CRFM), foregrounds the *adaptation* role — the model is a foundation other things are built on, not the end product.

**Frontier model** is a near-synonym foregrounding *capability* (top of the leaderboard). The two terms diverge in policy/regulatory contexts: "frontier" often implies the regulator-relevant subset of foundation models above a capability threshold.

## Key claims

### Industry has decisively taken the frontier

- **~90% of notable AI models in 2024 came from industry** (vs. 60% in 2023). Academia remains the leading source of *highly cited* research, but not of new notable models. Source: [[2026-04-28-ai-index-report-2025|AI Index 2025]] §1 Highlight 1.
- **U.S. produces the most notable models** (40 in 2024) vs. **China** (15), **Europe** (3). Total quantity gap is wide. But by *performance* the U.S.-China gap has shrunk to near parity (see below).

### Compute is scaling fast

- Training compute for notable models doubles every **~5 months**.
- Dataset size for training LLMs doubles every **~8 months**.
- Power required for training doubles **annually**.
- Carbon emissions trajectory:
  - AlexNet (2012): 0.01 tons
  - GPT-3 (2020): 588 tons
  - GPT-4 (2023): 5,184 tons
  - Llama 3.1 405B (2024): 8,930 tons
  - (Reference: average American = 18 tons/year.)

### Open-weight catching up to closed-weight

- Performance gap between top closed-weight and top open-weight models on the **Chatbot Arena Leaderboard**: **8.0% in early Jan 2024 → 1.7% by Feb 2025** on some benchmarks.
- The frontier is also tightening overall: **top-2 model gap = 0.7%, top-10 gap = 5.4%** (down from 4.9% / 11.9% the year before).

### U.S.-China performance gap narrowing fast

- End-2023 vs. end-2024 gaps on major benchmarks:
  - **MMLU**: 17.5pp → 0.3pp
  - **MMMU**: 13.5pp → 8.1pp
  - **MATH**: 24.3pp → 1.6pp
  - **HumanEval**: 31.6pp → 3.7pp

### Transparency improving

- **Foundation Model Transparency Index** (CRFM): avg score among major developers **37% (Oct 2023) → 58% (May 2024)**. Substantial progress, ~42% gap remaining. See [[responsible-ai]].

### Smaller is mighty

- **142× model-size reduction for the same MMLU >60% threshold** in two years: **PaLM (540B params, 2022) → Phi-3-mini (3.8B, 2024)**.

## Notable foundation model series (mentioned via [[2026-04-28-ai-index-report-2025|AI Index 2025]])

To be promoted to standalone entity pages when discussed in depth in another source. Currently noted here as a roster:

- **OpenAI**: GPT-4, GPT-4o, **o1**, o3 (test-time compute reasoning), **SORA** (video).
- **Google DeepMind**: Gemini family (Gemini-1.5-Flash-8B is the 280×-cost-reduction marker), Veo 2 (video).
- **Anthropic**: Claude 3 family (incl. Sonnet — implicit-bias study).
- **Meta**: Llama 3.1 405B (the 8,930-ton-CO2 marker), Movie Gen (video).
- **Microsoft**: Phi-3-mini (the 3.8B-param-MMLU marker).
- **Mistral AI**: French open-source.
- **xAI**: Grok family.

## Debates / contradictions

- **"Frontier" vs. "foundation" framing.** "Frontier" emphasizes capability gap; "foundation" emphasizes adaptation role. Different policy/regulation implications — frontier-model bills target capability thresholds; foundation-model bills target the broader pretraining-then-adapt pattern.
- **Compute-scaling sustainability.** Data-commons shrinkage (see [[responsible-ai]]) plus rising energy demands (driving nuclear-energy partnerships — Microsoft's Three Mile Island, Google's SMRs, Amazon's SMRs) raise structural questions about the 5-month-compute-doubling trajectory continuing.
- **Open-weight closing the gap.** As open-weight performance catches closed-weight, the policy logic for restricting model release weakens — but so does the commercial moat for closed-weight providers. Open question how 2025–2026 plays out.

## Related concepts

- [[generative-ai]] — the dominant *use* of foundation models today
- [[ai-benchmarks]] — how foundation-model capabilities are evaluated
- [[responsible-ai]] — the transparency, safety, and governance overlay
- [[enterprise-ai-adoption]] — the deployment context

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "foundation-models") OR contains(tags, "frontier-models")
SORT file.name ASC
```
