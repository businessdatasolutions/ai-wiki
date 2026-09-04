---
type: entity
kind: organization
aliases: ["Salesforce AI Research", "Salesforce Research", "Salesforce AI"]
tags: [salesforce, salesforce-ai-research, xlam, apigen-mt, synthetic-data, open-weight-models, function-calling, corporate-research-lab]
confidence: 0.75
last_confirmed: "2026-09-04"
accessed_at: "2026-09-04"
source_count: 2
relationships:
  - type: employs
    target: Juan-Carlos-Niebles
    via: "Research Director at Salesforce Research since 2021; co-author on the APIGen-MT / xLAM-2 paper"
  - type: authored-by
    target: xLAM
    via: "trains, releases and open-sources the xLAM Large Action Model family"
---

# Salesforce AI Research

The corporate research lab of Salesforce, and in this wiki the source of the **[[xLAM]]** open-weight "Large Action Model" family and the **APIGen-MT** synthetic-data pipeline that trains it — see [[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2]].

Notable for the wiki's purposes because of a strategic asymmetry: Salesforce's *product* side sells Agentforce, the agentic platform [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Sokolenko cites as an emblem of the agentic hype cycle]] ("Salesforce will try to sell you Agentforce"), while its *research* side open-sources small models and their training data — including the ones a practitioner uses to build an agent without buying any platform at all. Both things are true of the same company.

Researchers named in the corpus: **[[Juan Carlos Niebles]]** (Research Director, also Stanford), **Silvio Savarese** (Chief Scientist), **Caiming Xiong**, **Shelby Heinecke**, **Akshara Prabhakar**, **Zuxin Liu**.

## Appears in this wiki via

- [[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2]] — *APIGen-MT: Agentic Pipeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay*; the xLAM-2-fc-r model family.

## Referenced by

- [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai]] — cites xLAM-2-8B as evidence that small models reach state-of-the-art tool calling.
- [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models]] — xLAM-2-32B is the model in the demo stack.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "salesforce")
SORT file.name ASC
```
