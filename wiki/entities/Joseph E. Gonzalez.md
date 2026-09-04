---
type: entity
kind: person
aliases: ["Joseph E. Gonzalez", "Joseph Gonzalez", "Joey Gonzalez"]
tags: [joseph-gonzalez, uc-berkeley, sky-computing-lab, gorilla, berkeley-function-calling-leaderboard, mast, vllm, chatbot-arena, ai-benchmarks, multi-agent, function-calling]
confidence: 0.75
last_confirmed: "2026-09-04"
accessed_at: "2026-09-04"
source_count: 2
relationships:
  - type: part-of
    target: UC-Berkeley
    via: "Professor of Electrical Engineering and Computer Sciences; co-director of the Sky Computing Lab"
---

# Joseph E. Gonzalez

Professor of EECS at [[UC Berkeley]] and co-director of the **Sky Computing Lab**; a principal investigator behind the **Gorilla** project (LLMs connected to APIs) from which the [[Berkeley Function Calling Leaderboard]] grew, and a co-author on the lab's line of work on serving and evaluating LLM systems.

Promoted on the **second-source rule**, alongside [[Ion Stoica]], as senior author on both of the corpus's Berkeley agentic-evaluation papers.

## Appears in this wiki via

- [[2025-07-13-patil-berkeley-function-calling-leaderboard]] — senior author on the BFCL paper (ICML 2025); the Gorilla project's evaluation instrument.
- [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail]] — senior author on **MAST**, the multi-agent failure taxonomy (NeurIPS 2025 D&B).

Both papers converge on the same diagnosis from opposite methods — see [[multi-agent-failure-modes]] and [[ai-benchmarks]].

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "joseph-gonzalez")
SORT file.name ASC
```
