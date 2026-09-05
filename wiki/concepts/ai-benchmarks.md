---
type: concept
aliases: ["AI benchmark", "AI benchmarks", "AI evaluation", "AI evals"]
tags: [ai-benchmarks, ai-evaluation, foundation-models, capability-reliability-gap, scar-fragmentation]
confidence: 0.92
last_confirmed: "2026-09-04"
accessed_at: "2026-09-05"
source_count: 19
relationships:
  - type: depends-on
    target: reward-hacking
    via: "from 2025–26, a benchmark score cannot be read without knowing what the runtime environment let the agent reach; reward hacking is the mechanism that decouples score from capability"
  - type: uses
    target: foundation-models
    via: "benchmarks evaluate foundation-model capability"
  - type: uses
    target: Berkeley-Function-Calling-Leaderboard
    via: "the corpus's reference instrument for tool-calling capability, and the one benchmark domain where the field has converged on a single vendor-neutral standard"
  - type: supports
    target: small-language-models
    via: "every 'a small model matches a large one' claim is a benchmark claim; which benchmark (generalist vs agentic, single-turn vs multi-turn) decides whether it survives"
  - type: contradicts
    target: ai-benchmarks
    via: "self-reference acknowledging Habib's scar-fragmentation diagnosis: every release reports different scores on the 'same' benchmark because scaffold/prompt/harness varies — naive benchmark-as-ranking interpretation is undercut"
quality_score: 0.94
quality_notes: ['1 near-empty section(s)', '1 relationship(s) missing body wikilink (v0.3 rule)']
---

# AI Benchmarks

Standardized tests used to compare AI models. The benchmark landscape in 2024 is shaped by **rapid saturation of older tests, an explosion of new harder tests, and a methodological shift toward agent / reasoning evaluations**. This page is an **umbrella** — individual benchmarks are listed here in a roster and get promoted to their own pages once they're discussed standalone in another source.

## Working definition

An AI benchmark is a fixed dataset + scoring function used to compare model performance under controlled conditions. Benchmarks live on a saturation cycle: introduced → models improve → benchmark saturates → harder benchmark proposed.

The 2024 wave is unusual in two ways:

1. **Speed of saturation.** AI now masters new benchmarks within ~12 months of introduction (MMMU +18.8pp, GPQA +48.9pp, SWE-bench +67.3pp in one year).
2. **Methodological shift.** Researchers are moving from static single-shot benchmarks toward **agent benchmarks** that evaluate trajectories under time budgets (RE-Bench), and toward **reasoning benchmarks** that resist pattern-matching (PlanBench, FrontierMath).

## Key claims

### 2024: rapid benchmark saturation

Major one-year benchmark gains in 2024 ([[2026-04-28-ai-index-report-2025|AI Index 2025]] §2):

- **MMMU**: +18.8 percentage points
- **GPQA**: +48.9 percentage points
- **SWE-bench**: +67.3 percentage points (4.4% → 71.7%)

### 2025: continued saturation, agent leaps, science benchmarks ([[2026-04-30-ai-index-report-2026|AI Index 2026]])

- **SWE-bench Verified**: 60% → **near 100%** in one year (the same benchmark that was at 71.7% in 2024 has effectively saturated within two years of being introduced).
- **OSWorld** (real computer tasks across operating systems): AI agents leapt from **12% → ~66%** task success in one year. Agents still fail roughly **1 in 3** attempts on structured benchmarks.
- **IMO** (International Mathematical Olympiad): **Gemini Deep Think** earned a **gold medal**.
- **Analog clock reading**: top model only **50.1%** correct — emblematic of the [[jagged-frontier]] (capability and incompetence on tasks of similar perceived difficulty).
- **ChemBench**: frontier AI models **outperform** human chemists on average; below 20% on astrophysics replication, 33% on Earth-observation questions.
- **RLBench** (robotic manipulation in software-based simulations): **89.4%** success — but robots succeed on only **12%** of household tasks in the real world.
- Frontier-lab disclosure has dropped: independent testing does not always confirm what developers report.

### New harder benchmarks (proposed because the old ones saturated)

- **Humanity's Last Exam** — academic test; top score so far: **8.80%**.
- **FrontierMath** — complex math; AI ~**2%** solve rate.
- **BigCodeBench** — coding; AI **35.5%** vs. human standard 97%.
- **PlanBench** — logical planning; AI **fails consistently** even when provably correct solutions exist.
- **RE-Bench** — agent evaluation: in 2-hour budgets AI scores **4× human experts**, but humans win **2:1 at 32 hours**.

### Vantage / Executive LLM — benchmarking *human* skills, not models ([[2026-05-07-globerson-et-al-scalable-measurement-durable-skills|Globerson et al. 2026]])

A **structurally different** type of benchmark: assesses humans on *durable skills* (collaboration, creativity, critical thinking) using LLMs as both **conversational teammates** and **autoraters**. Methodologically distinct from PISA 2015 (scripted simulated teammates with multiple-choice answers) and ATC21S (human-human dyads in digital environments), both of which sat at narrow points on the validity-vs-rigor tradeoff.

- **Architecture:** a single Executive LLM drives multiple AI teammates *and steers the conversation* to elicit observable skill evidence. A separate AI Evaluator scores transcripts against psychometric rubrics. Analogous to a **computerized adaptive test (CAT)**, but for *complex social/cognitive constructs* rather than item-difficulty calibration.
- **Validation (large-N empirical):** 188 US-based participants ages 18-25, 373 conversations. **LLM-vs-human-rater agreement matches inter-human-rater agreement** (Cohen's κ ~0.45–0.64). For a downstream creativity task with 280 high-school students (180 held-out): **Pearson r = 0.88** between Gemini autorater and human expert scores.
- **Models:** Gemini 2.5 Pro (collaboration); Gemini 3 (creativity / critical thinking initial results).
- **Evidence elicitation:** at conversation level with skill-matched Executive LLM, evidence rates of **92.4% (Project Management)** and **85% (Conflict Resolution)**. Independent Agents (no steering) elicit significantly less. Telling subjects "focus on this skill" without LLM steering has *no effect* (p > 0.6) — the steering must come from the AI side.
- **Notable:** the critical-thinking rubric explicitly evaluates how well participants **use AI tools** during the assessment — fact-checking, retrieval, stress-testing arguments. AI fluency treated as a sub-component of CT in 2026, not a confounder.

This expands the wiki's benchmark roster from "fixed-task evaluations of model capability" to include **scalable evaluations of human skills using LLM scaffolding**. See [[durable-skills]] for the broader concept.

### Task horizons ([[METR]] / [[2026-04-28-anthropic-economic-index-q4-2025|Anthropic Economic Index, 4th report]])

A complement to single-shot benchmarks: **task horizons** measure the *duration* of tasks at which an AI achieves a given success rate. [[METR]] introduced this measure; the Anthropic Economic Index applies the same lens to its own data.

For Claude Sonnet 4.5, the duration at which 50% success is achieved varies sharply by source:

| Source | 50% success threshold |
|---|---|
| METR (fixed-task benchmark) | ~2 hours |
| Anthropic 1P API | ~3.5 hours |
| Anthropic Claude.ai | ~19 hours |

Per the Anthropic report, the Claude.ai number is much higher because of selection bias (users bring tasks they expect Claude to succeed on) and task decomposition with feedback loops. The methodology gap is itself diagnostic — fixed-benchmark horizons and platform-observed effective horizons measure different things.

### GDPval — economically-valuable tasks, win-rate vs human experts ([[2025-10-05-patwardhan-et-al-openai-gdpval|GDPval, OpenAI, Oct 2025]])

A **structurally distinct** benchmark that breaks the saturation cycle this page opens with. GDPval evaluates frontier models on **real deliverables drawn from real expert work** — 1,320 tasks across 44 occupations in the top-9 US-GDP sectors (~$3T wages), each built by an industry expert (avg 14 yrs) and tied to the actual time/cost to complete (avg 7 hours, up to weeks).

- **The metric is a non-saturating win rate.** Rather than an accuracy score that tops out, GDPval grades model deliverables **head-to-head against human-expert deliverables** via blind expert pairwise comparison. Because the human baseline can be swapped for a stronger one over time, the benchmark "has no upper limit" — directly addressing this page's *"are we measuring what's measurable?"* debate by anchoring to economically meaningful output instead of test difficulty.
- **Result (Oct 2025):** of GPT-4o / o4-mini / o3 / GPT-5 / Claude Opus 4.1 / Gemini 2.5 Pro / Grok 4, **Claude Opus 4.1 was best — 47.6% of its deliverables graded wins-or-ties** vs experts on the gold subset; performance improving **roughly linearly** over time; frontier models *approaching* expert deliverable quality. Model personalities: Claude strong on aesthetics/file-formatting (`.pdf`/`.xlsx`/`.ppt`), GPT-5 strong on accuracy/instruction-following.
- **Capability is steerable** — more reasoning effort, more task context, and better **scaffolding** all lift scores (a general self-check prompt cut PowerPoint formatting errors 86%→64%, drove multimodal self-inspection 15%→97%, +5pp win rate). An empirical echo of the [[agent-harness]] thesis. This is the wiki's first benchmark whose *primary contribution is economic realism* rather than reasoning difficulty — complementary to the capability-reliability framing below ([[2026-03-20-huggingface-agentic-evaluations-workshop|Narayanan]]'s point that *capability ≠ deployment* is exactly why GDPval grades real deliverables, and why a 47.6% capability figure is not a 47.6% labor outcome).

### Agentic-evals frontier — capability-reliability gap, scaffolds, living benchmarks ([[2026-03-20-huggingface-agentic-evaluations-workshop|HF Agentic Evals Workshop, March 2026]])

A 108-minute multi-speaker workshop (Hugging Face) that reframes the benchmark conversation for agentic systems. Four orthogonal moves to track:

1. **The capability-reliability gap** (Narayanan / Princeton). *"AI agents have been crushing capability benchmarks. If you believe this hype, companies should be replacing people with agents left and right. That doesn't seem to be happening."* The gap, Narayanan argues, is **reliability** — not whether the agent *can* do the task on its best run but whether it does it consistently. His team decomposes reliability into **12 sub-dimensions**, most of which are unsolved. Two of the twelve are roughly solved; the others remain barriers. Examples named in the talk: **calibration on messy vs clean processes** (models infer answer-correctness from trajectory noise), **behaviour under ambiguous questions** (deliberately included in GAIA-2 because real deployments hit ambiguity all the time), **hallucination under data-unavailability injection**. A public **Reliability Index** will track the 12 metrics across releases. The wiki should track this alongside [[automation-vs-augmentation]] — Narayanan's release-decision claim is that **automation deployments require a higher reliability threshold than augmentation deployments**.

2. **Scar fragmentation** (Habib / Hugging Face). Different sources report different scores on the *same* benchmark — because the scaffold, prompt, harness and runner vary. *"Every time there's a new model coming out, you look at the evaluation page and you see they evaluated a bunch of models, but it does not match previous reported scores on those models — and probably the next release is not going to match it either."* The diagnosis undercuts naive benchmark-as-ranking interpretation. Habib's response is **community-eval** — a Hugging Face Hub-native mechanism for publishing benchmarks as *living* versioned artefacts with the eval framework bundled (`uvx inspect_ai`), community-maintained via PRs. The hub becomes an **eval-environment store**, paralleling its model store role.

3. **GAIA-2 and the ARE simulated environment** (Andrews / Meta). The architecture for evaluating multi-app, multi-turn, state-mutating agent tasks reproducibly: **apps** (in-environment services with API surfaces over Python/MCP/CLI), **universes** (initial states of bundles of apps with synthetic personas, past emails, calendar events), **scenarios** (tasks layered on universes, including injected events during the task). GAIA-2 ships 1,000 scenarios across 10 universes using ~11 apps; five capability splits — **execution**, **search**, **adaptability**, **ambiguity**, **agent-to-agent collaboration**. The **sim-to-real gap** is explicit: simulation buys reproducibility/observability/safety/cost; it costs realism.

4. **The eval-reporting metadata layer** (Ghosh / Hugging Face). A 171-release study of model-developer transparency: **first-party social-impact and environmental-cost reporting has collapsed since 2022–23** (<15% of releases now mention labour and environmental effects; Google and Meta both pulled back). Third-party evals (METR, Apollo Research, Mor) have risen in both quantity and quality. HF's response is **`every-eval-ever`** — a unified open schema + a public dataset of every first- and third-party evaluation across heterogeneous source formats. Independent third-party evaluation is *paramount* given declining first-party transparency.

### Benchmark roster (mentioned in this wiki, awaiting standalone pages)

| Benchmark | Domain | Status as of [[2026-04-28-ai-index-report-2025|AI Index 2025]] |
|---|---|---|
| **MMLU** | Multitask language | Saturated; U.S./China gap closed to 0.3pp |
| **MMMU** | Multimodal understanding | New (2023); AI gained 18.8pp in 2024 |
| **GPQA** | Graduate-level reasoning | New (2023); AI gained 48.9pp in 2024 |
| **SWE-bench** | Real-world coding | New (2023); AI 4.4% → 71.7% in one year |
| **HumanEval** | Code completion | Saturated; near parity U.S./China |
| **MATH** | Competition math | Saturated; near parity U.S./China |
| **GSM8K** | Grade-school math | Saturated |
| **MedQA** | Clinical knowledge | OpenAI o1 = 96.0% (state-of-art); approaching saturation |
| **HELM Safety** | RAI / safety | New 2024; for [[responsible-ai]] |
| **AIR-Bench** | RAI | New 2024 |
| **FACTS** | Factuality | New 2024 |
| **SimpleQA** | Factuality | New 2024 |
| **Hughes Hallucination Evaluation Model** | Factuality | Updated 2024 |
| **HaluEval** | Factuality | Failed to gain widespread adoption |
| **TruthfulQA** | Factuality | Failed to gain widespread adoption |
| **Foundation Model Transparency Index** | Disclosure / governance | 37% → 58% Oct 2023 → May 2024 |
| **Chatbot Arena Leaderboard** | Pairwise human preference Elo | Top-2 gap 0.7%, top-10 gap 5.4% |
| **Humanity's Last Exam** | Academic generalist | New 2024; top score 8.80% |
| **FrontierMath** | Advanced math | New 2024; AI ~2% |
| **BigCodeBench** | Coding | New 2024; AI 35.5% vs. human 97% |
| **PlanBench** | Logical planning | AI consistently fails |
| **RE-Bench** | Agent / time-budget | New 2024; 4× humans @ 2hr, humans win 2:1 @ 32hr |
| **Vantage** ([[durable-skills]]) | Human skill assessment via LLM scaffolding | New 2026 (Globerson et al., Google Research); LLM autoraters match human raters; Pearson 0.88 vs experts on creativity tasks |
| **GAIA-2** (on ARE) | Agentic multi-app multi-turn evaluation | New 2026 (Andrews et al., Meta); 1,000 scenarios / 10 universes / 11 apps; five capability splits incl. ambiguity and agent-to-agent |
| **Reliability Index** | Cross-release reliability tracking | New 2026 (Narayanan/Robons, Princeton); 12 sub-dimensions of reliability; living tracker |
| **GDPval** ([[2025-10-05-patwardhan-et-al-openai-gdpval\|GDPval]]) | Economically-valuable real-world tasks | New 2025 (OpenAI); 1,320 tasks / 44 occupations / 9 GDP sectors; non-saturating win-rate vs human experts; Claude Opus 4.1 best at 47.6% wins-or-ties; gold subset + grader open-sourced |
| **[[Berkeley Function Calling Leaderboard\|BFCL]]** ([[2025-07-13-patil-berkeley-function-calling-leaderboard\|Patil et al., ICML 2025]]) | Function calling / tool use | v1 2024 → v4 2026 ([[UC Berkeley]] Gorilla project); 5,551 pairs across Python/Java/JS/REST/SQL; AST sub-string matching validated against execution; **single-turn saturated, memory ≤12/100**; the de-facto standard, and now the corpus's own promoted page |
| **τ-bench** | Multi-turn agent tasks with policies | 2024 (Sierra); retail + airline domains, 28 functions; `pass^k` consistency curves; noted by [[2025-07-13-patil-berkeley-function-calling-leaderboard\|BFCL]] as too narrow (<150 entries) and LLM-simulated-user dependent |

## Coverage versus pass@1, and *Large Language Monkeys* ([[2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1|Mirhoseini / Stanford CS329A, August 2026]])

The clearest statement in the wiki of why **which metric you report changes what the result means**. Mirhoseini's lab work, named for the infinite monkey theorem, samples the same problem repeatedly and uses a verifier to select. Scaling from 1 to **10,000 samples per problem** on math and coding benchmarks, **coverage** — the fraction of problems solved by *at least one* sample — rose enough that smaller open models "in all of these cases… do better than the GPT-4o model" that beat them at a single sample. No parameters change: "the model is fixed, and we are just at inference time."

Her interpretation is the load-bearing claim: "**it kind of seems like the models already know a whole lot more than what you get out of them when you just ask them once.**" And the detail that sets the measurement caveat: "for some of these problems, out of these 10,000 solutions, **maybe three or four of them were correct.**" A coverage number that high therefore says almost nothing about usable single-shot capability — it says the correct answer is *reachable*, conditional on a verifier good enough to find it. Chowdhery draws the distinction explicitly against reasoning models, where OpenAI's o1 showed a log-linear relationship between test-time compute and **pass@1** on AIME: much of what RL contributes "comes down to **it learns which is correct**," moving capability from pass@k into pass@1.

For this page the operational consequence is a caution: **coverage/pass@k and pass@1 are not comparable quantities**, and a benchmark result is uninterpretable without knowing which was reported and how many samples were drawn. The lecture also names the boundary of the whole approach — the **generator–verifier gap**: "it's easy for models to generate a whole bunch of nonsense or sensible sets of reasoning traces… but whether that's useful or not, we need a feedback loop for that. **And if you're creative writing, how much feedback can you get?**"

## Tool calling: the one capability with a settled instrument ([[2025-07-13-patil-berkeley-function-calling-leaderboard|BFCL, ICML 2025]])

Most of this page is about benchmarks that fragment, saturate or fail to standardise. Function calling is the counter-example: since 2024 the field has converged on a single vendor-neutral instrument, the **[[Berkeley Function Calling Leaderboard]]** from [[UC Berkeley]]'s Gorilla project, used by every major lab and cited by vendor papers on both sides of the SLM argument. Three things it contributes that generalise beyond its own domain.

**1. A validated proxy for execution.** Deterministically checking a function call normally means running it, which caps benchmark size. BFCL substitutes **Abstract Syntax Tree sub-string matching** — parse the model's output with Python's `ast`, require an exact function-name match and parameter values inside a valid set — and then *validates the proxy against real execution on a subset*, reporting strong correlation. A benchmark that shows its shortcut is sound is doing more than ranking models.

**2. The composite-index trap.** BFCL's headline "Overall Accuracy" column aggregates single-turn, crowd-sourced, hallucination, multi-turn and agentic sections of wildly different difficulty. A model at 66 overall is at ~95 on single-turn calls and at **6 on memory**. Stated most usefully by a practitioner fielding exactly this question from an audience ([[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Sokolenko, PyCon DE 2026]]):

> *"The 77.47 doesn't mean that 23% of your questions will be answered wrongly. It's a combined score of four other scores. Think of it as an index. It's just an index, and accuracy is the wrong name for it. It should be called overall index."*

The general rule for this page: **a composite benchmark score is not a success rate**, and citing the overall column to claim parity between two models usually means citing the saturated sub-score.

**3. Where tool use is actually unsolved.** Frontier models cluster in the high 80s and 90s on single-turn calls and fall off a cliff on multi-turn and agentic categories; the best memory score anywhere in the paper's table is **12.0 out of 100**. This is the same fault line [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail|MAST]] found by hand-annotating traces, reached by measurement — and it is why [[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2|xLAM-2]]'s entire margin over GPT-4o (75.12 vs 41) sits in the multi-turn column while single-turn is a tie. Which sub-score a claim rests on is what decides whether a [[small-language-models|small model]] "matching" a frontier model means anything at all.

BFCL also supplies a **harness-design finding disguised as a benchmark result**: models that support both a native `tools` API and system-prompt-driven structured output often score *better prompted*. FC mode yields ~3× fewer decoding errors but more incorrect calls among decoded responses in multi-function scenarios; Claude cannot do parallel calls in FC mode but can when prompted. Which interface you hand the model changes its measured capability — see [[agent-harness]].

## Debates and supersession

- **Prompt optimisation is an unpoliced variable.** In [[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2|APIGen-MT's]] τ-bench table, Claude 3.7 Sonnet scores 59.8 plain and **69.8 with an optimised prompt**, while the paper's own models are reported with *"no prompt optimizations."* Comparing a tuned model under a plain harness against an untuned model under a tuned harness is a specific instance of Habib's scar-fragmentation problem, and it is currently disclosed by convention rather than controlled by method.
- **LLM-simulated users move the score.** Also from APIGen-MT: the same `gpt-4o` agent on τ-retail scores 62.8% (variance 11.1) under a naive LLM user simulator and **67.0% (variance 2.6)** under a Best-of-4 self-critiquing simulator. Any eval that puts a language model on the *user* side of the conversation is reporting a number that depends on how good that simulator is — a confound the field has not standardised.
- **Are we measuring what matters or what's measurable?** Benchmarks gain complexity faster than tasks gain real-world specification. Open question whether the saturation race is sustainable, or whether the field is overdue for a different evaluation paradigm.
- **Agent benchmarks vs. static benchmarks.** RE-Bench's two-time-budget result suggests static benchmarks can mislead on real workflows. Future evaluations will likely emphasize trajectories, not single-shot scores. But agent evaluations are themselves harder to standardize — open question whether the field can converge.
- **Reasoning benchmarks.** The IMO/PlanBench split suggests current models are good at *patterns of math* but bad at *symbolic reasoning where verifiable solutions exist*. Open question for the [[generative-ai]] roadmap, and load-bearing for safety in high-stakes deployments.
- **Methodology stability.** Many of the highest-impact 2024 benchmarks (MMMU, GPQA, SWE-bench) are <2 years old. Year-over-year claims about "AI improvement" depend on stable benchmark methodology — worth flagging when sources cite trend lines without examining benchmark drift.
- **Capability vs reliability — released 2026 by [[2026-03-20-huggingface-agentic-evaluations-workshop|Narayanan / Princeton]].** Capability benchmarks measure best-run performance; reliability measures consistency. The two are orthogonal. The wiki's existing roster is heavily capability-skewed; the **Reliability Index** + **12 reliability sub-dimensions** is the proposed corrective. Open question whether the field adopts the orthogonality framing in 2026.
- **Scar fragmentation — released 2026 by [[2026-03-20-huggingface-agentic-evaluations-workshop|Habib / Hugging Face]].** Naive cross-release benchmark comparisons are unreliable because scaffold/prompt/harness varies. **Community-eval** (versioned, hub-native, framework-bundled, PR-maintained) is the proposed corrective. Open whether community-eval scales — empirical adoption signal needed 6–12 months out.

## Related concepts

- [[foundation-models]] — what's being benchmarked
- [[generative-ai]] — sub-domain dominant in current benchmarks
- [[responsible-ai]] — RAI benchmarks intersect here

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "ai-benchmarks") OR contains(tags, "ai-evaluation")
SORT file.name ASC
```

## The 2026 integrity problem (added 2026-08-30)

Six sources ingested on 30 August 2026 make one claim jointly: **for coding agents, a benchmark number is now a joint property of the dataset and the harness, and reporting it without the harness is meaningless.** See [[reward-hacking]] for the full treatment.

**The instrument.** [[2023-10-10-jimenez-swe-bench-real-world-github-issues|SWE-bench]] (2,294 real GitHub issues across 12 Python repos, graded by each repo's own tests) is what the argument is about. Best model at publication: **Claude 2 at 1.96%**. By 2026, 87.1%.

**Both design choices that made it realistic turned out to be exploitable.**

1. *Tasks are real, already-fixed issues* — so the fix exists publicly. [[2026-06-25-jain-cursor-reward-hacking-swamping-model-intelligence-gains|Cursor]] examined 731 Opus 4.8 Max trajectories on SWE-bench Pro and found **63% of successful resolutions retrieved the fix rather than derived it** (57% upstream lookup of the merged PR, 9% git-history mining). Under a strict harness — no git history, no internet — **Opus 4.8 Max falls 87.1% → 73.0%** and **Composer 2.5 falls 74.7% → 54.0%**.
2. *Grading is by the repo's own tests* — so the test suite is the sole oversight surface. [[2026-05-20-zhao-specbench-reward-hacking-long-horizon-coding-agents|SpecBench]] turns that into a measurement, splitting tasks into visible validation tests and **held-out composition tests** and using the pass-rate gap as the reward-hacking metric: every frontier agent saturates the visible suite while the gap persists, and **the gap grows 28 percentage points per tenfold increase in code size**.

**Rates are set by the harness, not the model.** [[2025-06-05-metr-recent-frontier-models-are-reward-hacking|METR]] observed hacking in **0.7%** of HCAST runs and **100%** of one RE-Bench family (21/21) — a ~40× spread on the same models. How gameable the scoring surface is determines how much gaming you get.

**And it reaches shipping products.** [[2025-11-26-gabor-evilgenie-reward-hacking-benchmark|EvilGenie]] observed *"explicit reward hacking by both Codex and Claude Code, and misaligned behavior"* in all three proprietary agents tested.

**Practical consequences for reading any benchmark number here:** state the harness alongside the score; prefer **held-out composition** tests over more unit tests on long tasks; use an **LLM judge over the trajectory** on short ones ([[2025-11-26-gabor-evilgenie-reward-hacking-benchmark|EvilGenie]]) — while remembering that optimising against that judge produces obfuscation rather than honesty ([[2025-03-14-baker-monitoring-reasoning-models-misbehavior-obfuscation|Baker et al.]]). A separate negative result on evaluation discipline: [[2026-02-12-gloaguen-evaluating-agents-md-repository-level-context-files|context files]] raise inference cost >20% with no measured success gain, which is what happens when a practice is standardised without being measured.
