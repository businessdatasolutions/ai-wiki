---
type: concept
aliases: ["jagged frontier", "jagged-frontier", "jagged technological frontier", "AI capability frontier"]
tags: [jagged-frontier, AI-capabilities, knowledge-work, productivity, automation, augmentation]
confidence: 0.90
last_confirmed: "2026-04-30"
source_count: 5
---

# Jagged Frontier

The boundary of what current AI systems can do well — described as **"jagged"** because tasks of similar perceived difficulty for humans can fall on opposite sides. Inside the frontier, AI assistance helps; outside, it harms. The frontier is **invisible** (workers can't easily tell which side a task sits on without inspection) and **moving** (it expands with model improvements).

## Working definition

Per [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua et al. (2026)]], who introduced the term:

> "Tasks that appear to human knowledge workers to be of similar difficulty may be performed either better or worse by humans using AI. Within this jagged frontier, AI can complement human work. However, outside the frontier, AI output is inaccurate, is less useful, and can degrade human performance."

The "jagged" descriptor distinguishes it from a smooth, monotonic capability gradient: AI is unexpectedly good at some tasks (idea generation) and unexpectedly bad at others that look easy (e.g., basic math, multi-source triangulation requiring close reading).

## Key claims

### Empirical anchor: BCG field experiment ([[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua et al. 2026]])

- 758 [[Boston Consulting Group|BCG]] consultants, randomized into control / GPT-4 only / GPT-4 + overview, across two task arms (one inside-frontier, one outside-frontier).
- **Inside the frontier**: AI users +12.2% completion, +25.1% faster, +33.9% quality (Cohen *d* ≈ 0.96).
- **Outside the frontier**: AI users 19 percentage points *less* likely to be correct (84.5% control → 60.0% / 70.6% AI conditions).
- Same model (GPT-4), same elite users, same task domain — the jaggedness is a property of the *task-AI fit*, not user skill or model selection.

### Subjective coherence persists when correctness fails

- Outside-the-frontier AI users produced *more confident, more coherent* recommendations even when their answers were wrong (subjective coherence quality higher with AI in both correct- and incorrect-answer subgroups).
- Implication: AI improves *presentation* irrespective of *substance*, which can mask poor performance from supervisors and clients.

### Two adaptation patterns

The Dell'Acqua paper's qualitative analysis identifies two effective-user strategies:

- **Centaurs** — alternate between AI and human work, switching task-by-task.
- **Cyborgs** — deeply intertwine AI into the workflow with continuous human-AI co-production.

### Convergence with adjacent measurement frameworks

The jagged-frontier concept is consistent with and extended by:

- [[2026-04-28-anthropic-economic-index-q4-2025|Anthropic Economic Index]] — task-level success rate falls slightly with task complexity (70% → 66% from sub-HS to college-level), while speedup rises sharply; the speedup-times-success product is positive but uneven across tasks.
- [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson, Li & Raymond (2025)]] — within customer support, the AI declines to suggest when training data is insufficient, an explicit acknowledgement that the system has bounded reliability.
- [[ai-benchmarks]] — METR's task-horizon work measures the duration of tasks an AI can complete with 50% success, providing a related but methodologically distinct picture of capability scope.
- [[2026-04-29-boussioux-crowdless-future|Boussioux et al. (2024)]] — in creative ideation, HAI solutions occupy a more *incremental* search space proximal to existing ideas, while human-crowd solutions exhibit more variable search at both the bottom and top extremes of novelty. The paper attributes the pattern to LLMs' training-data confinement, formal-rationality bias, and convergence toward the statistical mean. This is one face of jaggedness: AI is strong on value/quality and weak on extreme-novelty.
- [[2026-04-30-ai-index-report-2026|AI Index 2026]] — the term "jagged frontier" is now part of the AI Index narrative (Top Takeaway #4). The report's anchoring example: **Gemini Deep Think wins gold at the IMO** while the top model reads analog clocks correctly only **50.1%** of the time. AI agents on **OSWorld** leapt from 12% → ~66% task success in one year, yet still fail roughly **1 in 3** structured-benchmark attempts. Robotic manipulation in software simulations (RLBench) reaches 89.4%, but real-world household-task success is only 12%.

### Mechanism: the frontier is invisible

Workers cannot reliably tell ex ante which side of the frontier a given task sits on. Effective use therefore requires:

- Workflow-level inspection to identify deviations from human-only baselines.
- Meta-cognitive skill to assess AI fit task-by-task.
- Calibration against demonstrated performance, not perceived task similarity.

## Practical implications

- **Don't generalize AI capability across tasks** that "feel similar."
- **Centaur/Cyborg strategies are post-hoc descriptions of effective use**, not prescriptions; both can fail when applied indiscriminately.
- **Familiarity training can backfire**: in the Dell'Acqua experiment, the GPT + overview condition performed *worse than GPT-only* on outside-the-frontier correctness — more familiarity led to more over-reliance.

## Related concepts

- [[automation-vs-augmentation]] — fit determines whether AI substitutes or complements; the frontier is the empirical boundary.
- [[ai-employment-effects]] — the jaggedness explains why some occupations see employment declines while others see growth.
- [[generative-ai]] — the underlying technology whose capability frontier is jagged.
- [[ai-benchmarks]] — fixed-task benchmarks measure one slice of the frontier.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "jagged-frontier")
SORT file.name ASC
```

## Open questions

- The frontier shifts with model improvements; longitudinal measurement is sparse. The [[Anthropic Economic Index]] is the closest current source for tracking shifts at population scale.
- The Centaur vs. Cyborg dichotomy comes from one paper's qualitative coding; replications across other domains and tools would strengthen it.
