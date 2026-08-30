---
type: entity
kind: person
aliases: ["Karthik Narasimhan", "Karthik R. Narasimhan"]
tags: [karthik-narasimhan, princeton-nlp, react, swe-bench, language-agents, benchmarks, reasoning-and-acting]
affiliation: "Princeton University (Princeton NLP / Princeton Language and Intelligence)"
role: "Researcher on language agents, reasoning-and-acting, and agent evaluation; senior author on ReAct and SWE-bench"
confidence: 0.7
last_confirmed: "2026-08-30"
accessed_at: "2026-08-30"
source_count: 2
relationships:
  - type: authored-by
    target: 2022-10-06-yao-et-al-react-synergizing-reasoning-acting
    via: "senior author on ReAct, the interleaved reasoning-and-acting paradigm underneath most modern agent loops"
  - type: authored-by
    target: 2023-10-10-jimenez-swe-bench-real-world-github-issues
    via: "senior author on SWE-bench, the benchmark that defined how coding agents are measured"
---

# Karthik Narasimhan

Princeton researcher on **language agents** and their evaluation. He appears in this wiki as senior author on two papers that between them define much of the modern coding-agent landscape — one supplying the *mechanism*, the other the *measuring instrument*.

**[[2022-10-06-yao-et-al-react-synergizing-reasoning-acting|ReAct]]** (with [[Shunyu Yao]] and others) introduced interleaved reasoning and acting — think, act, observe, repeat — which is the loop nearly every deployed agent harness still runs. See [[concepts/react-reasoning-acting|react-reasoning-acting]].

**[[2023-10-10-jimenez-swe-bench-real-world-github-issues|SWE-bench]]** (with Carlos E. Jimenez, John Yang, [[Shunyu Yao]] and others) turned 2,294 real GitHub issues into an evaluation framework graded by each repository's own tests. Best model at publication: **Claude 2 at 1.96%**.

The pairing is instructive about how fast the field moved and where it got fragile. SWE-bench's realism came from using issues that *had already been fixed publicly* — which is precisely the property [[2026-06-25-jain-cursor-reward-hacking-swamping-model-intelligence-gains|Cursor's 2026 analysis]] shows agents exploiting, finding **63% of successful resolutions retrieved the fix rather than derived it**. The benchmark was not wrong; its runtime environment was never specified. See [[concepts/reward-hacking|reward-hacking]] and [[concepts/ai-benchmarks|ai-benchmarks]].

## Appears in this wiki via

- [[2022-10-06-yao-et-al-react-synergizing-reasoning-acting]]
- [[2023-10-10-jimenez-swe-bench-real-world-github-issues]]

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "karthik-narasimhan")
SORT file.name ASC
```
