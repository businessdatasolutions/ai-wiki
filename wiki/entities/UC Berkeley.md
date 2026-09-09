---
type: entity
kind: organization
aliases: ["UC Berkeley", "University of California, Berkeley", "Berkeley", "UC Berkeley Sky Computing Lab", "Sky Computing Lab"]
tags: [uc-berkeley, sky-computing-lab, gorilla, berkeley-function-calling-leaderboard, ai-benchmarks, function-calling, academic-research]
confidence: 0.75
last_confirmed: "2026-09-04"
accessed_at: "2026-09-04"
source_count: 2
relationships:
  - type: part-of
    target: Berkeley-Function-Calling-Leaderboard
    via: "BFCL is built and maintained by Berkeley's Gorilla project out of the Sky Computing Lab; the leaderboard lives at gorilla.cs.berkeley.edu"
---

# UC Berkeley

Public research university; in this wiki it appears as the **institutional home of the [[Berkeley Function Calling Leaderboard]]** — the benchmark that has become the de-facto standard for measuring an LLM's tool-calling ability, and therefore the instrument behind most "small model matches frontier model on tool use" claims in the corpus.

BFCL comes out of the **Gorilla project** in Berkeley's **Sky Computing Lab**, led by **Shishir G. Patil** with **[[Ion Stoica]]** and **[[Joseph E. Gonzalez]]** as senior authors — the same lab lineage behind Spark, Ray and vLLM. The leaderboard is hosted at `gorilla.cs.berkeley.edu/leaderboard.html` and the evaluation code is open on GitHub.

What makes Berkeley's role structurally important to this wiki is **neutrality**: BFCL is maintained by an academic group rather than a model vendor, which is why vendor papers ([[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2|Salesforce]]) and vendor position papers ([[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|NVIDIA]]) alike cite it as the arbiter, and why a practitioner picking a locally-runnable model ([[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Sokolenko]]) can use it as a shopping list.

The lab's two contributions to this corpus reach the same diagnosis by opposite methods, which is why it is worth tracking Berkeley as an institution rather than only as a leaderboard host: **MAST** hand-annotates multi-agent traces and locates failure in coordination, state and long-horizon reasoning; **BFCL** measures single models and finds single-turn calling saturated while memory sits at 12/100. Same lab, same fault line, one qualitative and one quantitative. See [[multi-agent-failure-modes]].

## Appears in this wiki via

- [[2025-07-13-patil-berkeley-function-calling-leaderboard]] — *The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models*, ICML 2025. Patil, Mao, Yan, Ji, Suresh, [[Ion Stoica|Stoica]], [[Joseph E. Gonzalez|Gonzalez]].
- [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail]] — *Why Do Multi-Agent LLM Systems Fail?* (MAST), NeurIPS 2025 Datasets & Benchmarks; Sky Computing Lab / BAIR, with the same two senior authors.

## Referenced (not authored) by

- [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models]] — the "UC Berkeley research" a PyCon DE audience is pointed at.
- [[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2]] — reports xLAM-2 against BFCL v3.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "uc-berkeley")
SORT file.name ASC
```
