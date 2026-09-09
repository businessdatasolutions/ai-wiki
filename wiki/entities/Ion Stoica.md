---
type: entity
kind: person
aliases: ["Ion Stoica"]
tags: [ion-stoica, uc-berkeley, sky-computing-lab, amplab, rise-lab, spark, ray, vllm, databricks, anyscale, ai-benchmarks, multi-agent, function-calling]
confidence: 0.75
last_confirmed: "2026-09-04"
accessed_at: "2026-09-04"
source_count: 2
relationships:
  - type: part-of
    target: UC-Berkeley
    via: "Professor of Computer Science; co-director of the Sky Computing Lab, successor to AMPLab and RISELab"
---

# Ion Stoica

Professor of Computer Science at [[UC Berkeley]] and co-director of the **Sky Computing Lab** — the successor to AMPLab and RISELab, and the group whose systems output (Spark, Ray, vLLM, Chi) has shaped much of the infrastructure the rest of this wiki's sources run on. Co-founder of Databricks and Anyscale.

Promoted to an entity page on the **second-source rule**: he is a senior author on two of the corpus's most-cited agentic evaluation papers, both from the same lab, and they turn out to say the same thing by opposite methods.

## Appears in this wiki via

- [[2025-07-13-patil-berkeley-function-calling-leaderboard]] — senior author on the [[Berkeley Function Calling Leaderboard]] paper (ICML 2025), the de-facto standard for measuring tool calling.
- [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail]] — senior author on **MAST**, the hand-annotated taxonomy of multi-agent failure (NeurIPS 2025 Datasets & Benchmarks).

The pairing is the point: MAST locates agent failure in coordination, state and long-horizon reasoning by reading traces; BFCL finds the same fault line by measurement (single-turn calling saturated, memory at 12/100). Same lab, same conclusion, two methods — see [[multi-agent-failure-modes]] and [[ai-benchmarks]].

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "ion-stoica")
SORT file.name ASC
```
