---
type: entity
kind: product
aliases: ["xLAM", "xLAM-2", "xLAM-2-fc-r", "Salesforce xLAM", "Large Action Model", "Large Action Models"]
tags: [xlam, salesforce, small-language-models, open-weight-models, function-calling, tool-use, large-action-model, apigen-mt, quantization, local-inference]
confidence: 0.8
last_confirmed: "2026-09-04"
accessed_at: "2026-09-04"
source_count: 3
relationships:
  - type: authored-by
    target: Salesforce-AI-Research
    via: "trained, released and open-sourced by Salesforce AI Research"
  - type: instance-of
    target: small-language-models
    via: "the corpus's reference example of an open-weight small model that is competitive on agentic tool-calling; the 1B–32B sizes are SLMs under the device-fit definition"
  - type: uses
    target: Berkeley-Function-Calling-Leaderboard
    via: "xLAM-2 is reported and ranked on BFCL v3; the leaderboard is how its tool-calling claim is substantiated"
---

# xLAM

**Salesforce's open-weight "Large Action Model" family** — language models post-trained specifically for tool calling and multi-turn agentic interaction, released by [[Salesforce AI Research]] with weights and training data public on [[Hugging Face]].

The **xLAM-2-fc-r** generation ships at **1B, 3B, 8B, 32B and 70B** parameters on Llama 3.1/3.2 and Qwen 2.5 backbones, trained by filtered behavioural cloning on synthetic multi-turn trajectories produced by the **APIGen-MT** pipeline — see [[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2]] for the method and the numbers.

## Why the wiki tracks it

xLAM is the corpus's **worked example of the [[small-language-models]] argument**: an open, small, locally-runnable model that is genuinely competitive with frontier models on the narrow capability agents actually need.

- The [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|NVIDIA position paper]] cites xLAM-2-8B by name as evidence for its central claim: *"achieves state-of-the-art performance on tool calling despite its relatively modest size, surpassing frontier models like GPT-4o and Claude 3.5."*
- On [[Berkeley Function Calling Leaderboard|BFCL v3]] as of April 2025, xLAM-2-70b and xLAM-2-32b held **ranks 1 and 2**, and even the **1B** model beat `o1` and `gpt-4o` on the multi-turn column.
- [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Sokolenko runs xLAM-2-32B at 4-bit quantization on a two-year-old laptop]] — the model chosen precisely because it is *"not only open-source but also smallish"* while sitting in BFCL's top 20 of ~110.

## The qualifier that travels with it

The advantage is **narrow and dated**. It is concentrated in BFCL's multi-turn column (75.12 vs 41–47 for GPT-4o); on single-turn AST it is indistinguishable from frontier models because that category is saturated. On τ-bench overall it is beaten by Claude 3.5 Sonnet (new), Claude 3.7 and `o1`. And its April-2025 top-of-board position had slipped to roughly 18th by December 2025 as the frontier moved. See [[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2|the source page]] for the full reading.

## Appears in this wiki via

- [[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2]] — the APIGen-MT training pipeline and the xLAM-2 results (primary).
- [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai]] — cited as capability evidence for SLMs in agents.
- [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models]] — the model actually deployed in a local-inference demo stack.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "xlam")
SORT file.name ASC
```
