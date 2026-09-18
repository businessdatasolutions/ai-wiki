---
type: concept
title: Multi-agent failure modes
aliases: ["multi-agent failure modes", "MAST", "multi-agent system failure taxonomy", "why multi-agent systems fail", "agent coordination failure"]
confidence: 0.85
last_confirmed: "2026-09-18"
source_count: 12
accessed_at: "2026-09-18"
tags: [mast, multi-agent, failure-taxonomy, coordination, inter-agent-misalignment, task-verification, data-processing-inequality, isolated-workspaces, caid, token-budget]
relationships:
  - type: part-of
    target: ai-agents
  - type: depends-on
    target: agent-harness
  - type: contradicts
    target: agent-fleet-management
    via: "fleet practice assumes more parallel agents produce more delivered value; this literature shows decomposing one problem across agents loses information at equal compute and that coordination failures are structural rather than capability gaps. The reconciliation is that fleets parallelise *independent* tasks, which is not the case the critique addresses"
    confidence: 0.7
quality_score: 1
---

# Multi-agent failure modes

Why systems of cooperating LLM agents underperform expectations — and the specific structures that fix it. The literature converges on an uncomfortable and useful conclusion: **most multi-agent failure is organisational, not model-quality**, so a better model does not repair it.

## The deflation

[[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail]] opens on it: *"Despite enthusiasm for Multi-Agent LLM Systems (MAS), their performance gains on popular benchmarks are often minimal."*

[[2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-under-equal-budgets]] explains why. The reported gains are **confounded with test-time compute** — multi-agent systems run more inference. Normalise the reasoning-token budget and the advantage largely disappears. The theoretical basis is the **Data Processing Inequality**: under a fixed budget with perfect context utilisation, a single agent is more **information-efficient**, because each agent in a chain conditions on a lossy summary rather than the source, and post-processing cannot add information. Tested across Qwen3, DeepSeek-R1-Distill-Llama and Gemini 2.5, single-agent systems consistently match or outperform on multi-hop reasoning at matched tokens.

**The escape clause is the useful part**, and it is a decision rule: multi-agent systems become competitive when **a single agent's effective context utilisation degrades** — the problem no longer fits, the model handles long context poorly, or the context is polluted — or when you are simply willing to spend more compute. **Reach for multiple agents when one context window stops being enough, and not before.**

## The taxonomy

[[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail]] built **MAST** — the Multi-Agent System Failure Taxonomy — from 1,600+ annotated traces across 7 MAS frameworks, with the taxonomy derived from close analysis of 150 traces at **inter-annotator agreement κ = 0.88**. **14 failure modes in 3 categories:**

| Category | What breaks |
| --- | --- |
| **System design issues** | The architecture — role definitions, termination conditions, information flow |
| **Inter-agent misalignment** | Agents on divergent assumptions, talking past each other, undoing each other's work |
| **Task verification** | Nobody checks, or the check is inadequate — failures accepted as successes |

Two of the three are **coordination** failures, which is why model upgrades do not fix them: they are properties of how work was divided. The third, **task verification**, is the seam every other part of this corpus runs into — [[2026-05-20-zhao-specbench-reward-hacking-long-horizon-coding-agents|SpecBench's]] collapsed oversight surface, [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Merge Mommy's]] verification-gap dimension, and the [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes|46.41% of agent fixes rejected]] after the agent declared them done.

## The prescription

[[2026-03-23-geng-neubig-caid-asynchronous-software-engineering-agents]] answers the taxonomy almost category-for-category, by porting coordination primitives human software teams already use:

| CAID primitive | MAST category it closes |
| --- | --- |
| **Centralized task delegation** (dependency-aware plans from a central manager) | System design |
| **Isolated workspaces** (one per subtask) | Inter-agent misalignment / interference |
| **Executable test-based verification** at structured integration | Task verification |

Result: **+25.6% absolute** over single-agent baselines on PaperBench, **+14.7%** on Commit0. *(Frequently miscited as +26.7% / +14.3%.)*

**The two results are compatible**, and the seam is Tran & Kiela's own condition: reproducing a research paper or building a Python library from scratch will not fit one context window, so the degradation condition holds by construction. CAID measures inside the regime where multi-agent wins. Neither paper normalises against the other's variable — CAID does not equalise compute, Tran & Kiela do not test context-exceeding tasks — so the honest summary is: **multi-agent architecture is a response to a context-capacity constraint, and where that constraint does not bind, the extra agents are overhead.**

## What practitioners already do

[[2026-07-25-darroman-profitable-founder-managing-ai-agents-25-prs-a-day|Carson's setup]] instantiates all three CAID primitives without naming them: a fresh VM per Devin session *is* an isolated workspace; the folder hierarchy plus paper priority list *is* a centralized delegation layer implemented in a human; the [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Land PR loop]] *is* structured integration with test-based verification. **The three things worth building first are the three things CAID names.**

## Benchmark corroboration: the same fault line, measured ([[2025-07-13-patil-berkeley-function-calling-leaderboard|BFCL, ICML 2025]], added 2026-09-04)

MAST located multi-agent failure by hand-annotating traces. [[2025-07-13-patil-berkeley-function-calling-leaderboard|BFCL]] reaches the same conclusion numerically and from the opposite method — measuring one model rather than a system of them.

Across ~110 model families, frontier models score in the high 80s and 90s on **single-turn** function calls and collapse on the multi-turn and agentic categories. In the paper's Table 1, the leading model on overall score is at 95.5 on single-turn simple calls and **6.0 on memory**; the best memory score anywhere in the table is **12.0 out of 100**. The paper's own summary:

> *"While state-of-the-art LLMs excel at single-turn calls, memory, dynamic decision-making, and long-horizon reasoning remain open challenges."*

This matters for the page's central claim. If sustained state, memory and long-horizon decision-making are unsolved *within a single agent*, then coordination failures observed across several agents are not purely a coordination problem — they are the same underlying deficit, compounded by having more places to lose state. Two independent methods, one fault line.

BFCL also supplies a **measurement caveat for this literature**: its multi-turn evaluation requires both a final-state match and a required-call-path match, precisely because *"multiple sequences of function calls can achieve the same result"* while non-state-changing calls (a lookup that should have preceded an action) leave no trace in the final state. Any taxonomy of agent failure built on outcome inspection alone will miss the class of failures where the agent guessed instead of checking.

## The determinism bet, and what it costs (added 2026-09-04)

[[2026-09-03-thurium-wang-google-cloud-graph-engineering-101|Google Cloud's graph-engineering explainer]] makes the clearest vendor statement of the architectural answer to this page's problem: specify the workflow yourself, node by node, and give each node's agent no view of history — *"an agent that's at a certain node doesn't need to know what happened before"* — in exchange for *"really good predictability, debuggability and control."*

That is a bet, and this page holds the reasons to check it. **[[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail|MAST]]'s inter-agent misalignment category is precisely the seam a graph creates**: every edge is a handoff, and handoffs are where the taxonomy locates a large share of failures. Meanwhile [[2025-07-13-patil-berkeley-function-calling-leaderboard|BFCL]] finds memory and long-horizon state to be the *unsolved* half of agentic capability, which cuts both ways — a history-free node cannot lose state it never had, but the graph's shared state now has to carry everything the node would otherwise have remembered, and nothing measures whether that trade nets out.

The honest position: determinism is a plausible mitigation for the failures on this page, asserted by a vendor with no measurement attached, against a literature that has measured the cost of decomposition ([[2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-under-equal-budgets|Tran & Kiela]]: single agents win at equal token budgets) but not the benefit of specifying it in advance. See [[graph-engineering]].

## Related concepts

[[concepts/ai-agents|ai-agents]], [[concepts/agent-fleet-management|agent-fleet-management]], [[concepts/agent-harness|agent-harness]], [[concepts/agent-development-lifecycle|agent-development-lifecycle]], [[concepts/agentic-engineering|agentic-engineering]], [[concepts/reward-hacking|reward-hacking]].

## Debates and supersession

- **CAID vs Tran & Kiela** — reconciled above as a regime distinction, but the reconciliation is this wiki's inference, not either paper's claim. **Open:** a study that equalises compute *and* varies whether the task fits one context window.
- **Which CAID primitive carries the gain?** No ablation was read. If isolation alone accounts for most of it, the prescription is far cheaper than full CAID. **Open, and the highest-value question here.**
- **MAST's 14 modes are not enumerated in this wiki** — only the three categories, from the abstract. Anyone building a checklist must read the paper.
- **Vintages:** MAST studies GPT-4 / Claude 3 / Qwen2.5 / CodeLlama on the 2024–25 framework generation. Incidence rates will have moved; the taxonomy is the durable artifact.

## A practitioner taxonomy alongside the empirical one (added 2026-09-01)

[[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails|Google Cloud's AI Builder Essentials]] offers a **four-mode loop failure taxonomy** derived from developer-support experience rather than from annotated traces. It carries no evidence, but the categories line up with [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail|MAST's]] three better than the difference in rigour would predict:

| Practitioner mode | The failure | MAST category it maps to |
| --- | --- | --- |
| **Runaway loops** | No exit condition — and in 2026 the cost is tokens, not just a hung stack | System design issues |
| **Unverified autonomy** | An agent reuses its own prior context and grades its own work — confirmation bias plus context pollution | Task verification |
| **Vague or uncheckable goals** | *"make this summary better"* — no criterion the loop can terminate against | System design issues |
| **Complexity overflow** | One loop asked to do what needs an orchestration graph | Inter-agent misalignment, once you decompose |

The fourth mode carries the operational decision this concept keeps returning to: **move from loop engineering to graph engineering only when a single loop stops coping** — *"you can put loop as part of the graph."* That is the vendor-side statement of the condition [[2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-under-equal-budgets|Tran & Kiela]] derive formally, and it is notable for being a vendor arguing *against* reaching for the more elaborate architecture by default.

## "Main character syndrome" in a self-improvement swarm (added 2026-09-09)

[[2026-09-07-yc-paper-club-why-the-harness-matters-more-than-the-model|YC's QM team]] report a failure mode from a specific and increasingly common configuration: **a fleet of agents dispatched to fix bugs found in the system's own accumulated traces, scored by an LLM judge.**

Centralising every agent conversation in Postgres gives them, as a side effect, a large eval set — *"you're accumulating this large eval set of all the traces that you have from the conversations that people are having with the agent. And in principle, you can think about going and hill climbing on that."* The result was mixed:

> *"Typically if you're just dispatching this like torrent of agents that are supposed to fix all of the bugs that they're encountering when you have the LLM as a judge, you start to get this kind of **main character syndrome** where the agents are making fixes that are only seeing their piece of the elephant effectively… they're not seeing the whole system."*

The shape is familiar to this page — locally sensible, globally incoherent edits — but two features are worth recording. First, **each individual agent is behaving correctly given its context**; the failure is entirely in the aggregation, which means it will not be caught by any evaluation that scores fixes one at a time. Second, **the LLM judge is part of the mechanism rather than the safeguard**: it validates each local fix against local evidence, and has no vantage from which to see the interaction. Their remedy is human-in-the-loop, which they report as *"continuing to be really important"* — while, in the same talk, reporting that human review of database writes has decayed into rubber-stamping (see [[agent-oversight-and-delegation]]).

This is a concrete instance of why [[2026-03-23-geng-neubig-caid-asynchronous-software-engineering-agents|CAID's]] isolated-workspaces result matters: the coordination primitive that pays is the one that prevents agents from acting on a partial view of shared state.

## The governance face of the same failures (added 2026-09-15)

[[2026-08-26-chatterjee-agentic-governance-gap|Chatterjee (Analytics Magazine, Aug 2026)]] restates this page's findings as an enterprise control problem, and the mapping is close enough to be worth recording. His third converging force is multi-agent coordination — *"a flawed instruction, a poisoned data source, or a manipulated prompt can cascade through a chain of agents before a person is positioned to intervene"* — which is MAST's **inter-agent misalignment** category with the security consequences attached.

The incident classes he reports enterprises hitting line up with the taxonomy: *"agents that looped indefinitely on a flawed instruction"* (runaway loops), *"agents that invoked the wrong API with elevated credentials"*, and *"multi-agent systems where one agent's error propagated into a second agent's decision before any person was aware a problem existed."* His framing of why decomposition raises the stakes is the most quotable line: **"ordinary operational fragility, once confined to human error, is now compounding at machine speed."**

His proposed control for the seam is **cross-agent identity and provenance** — when one agent acts on another's output, the origin, authorization and confidence of that input must be traceable. That is a direct architectural answer to the failure class this page identifies, and the corpus holds no evidence that it works. Note the source tier: a practitioner column with no data, reporting incident classes in aggregate with no counts and no named organisations.

## A production system abandoned the pattern on capability grounds, not failure grounds (added 2026-09-16)

Everything else on this page treats multi-agent trouble as **engineering defects to design against** — [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail|MAST]] derives a taxonomy from observed failures, and the corrective is better specification, verification and orchestration. [[2026-08-10-maza-a16z-kavak-rebuilding-a-company-around-ai|Maza / a16z, August 2026]] reports a different kind of decision, and it is worth keeping distinct.

Kavak ran *"tens of thousands"* of function-decomposed agents at production scale — *"working at scale running the business back in December."* They abandoned the architecture **not because it was failing**: it *"was working,"* it *"brought us to profitability,"* it *"brought us amazing growth."* The reason given is that a capability threshold made decomposition itself the constraint:

> *"Opus 4.5 came out and I realized this isn't the right paradigm anymore — the intelligence now doesn't need the graph and the multi-agent lattice work and harness, because **it will constrain this level of intelligence**."*

The replacement is a single long-running agent per customer with memory, evals, a CLI and a long-horizon goal. His advice: ***"if I could advise everyone, don't build agentic workflows to graphs."***

**Why this is a real addition and not just another opinion.** The page's existing sceptical evidence is largely about *equal-budget comparisons* — [[2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-under-equal-budgets|Tran & Kiela]] show single agents winning at matched token budgets. Maza's claim is **dated and tied to a specific model release**: the architecture was right in December and wrong afterwards. If that is correct, multi-agent decomposition is not a permanently inferior pattern but a **capability-dependent** one, and the failure modes this page catalogues may be partly artifacts of building around models that needed the scaffolding.

**What would falsify or confirm it.** Nothing here is measured. Kavak reports no A/B between the two architectures, no cost comparison, and no evidence beyond the executive's judgement that the old system constrained the new model. A firm that ran both concurrently and measured would settle it; **no source in the corpus has.** Treat this as one practitioner's dated architectural verdict, weighted by the fact that he paid two years of work for it. See [[agent-harness]] and [[Kavak]].

## The field's original premise: self-interested agents (added 2026-09-18)

"Multi-agent system" is an older term than this page's LLM sources, and in the literature that coined it the premise was different. In [[2009-01-01-wooldridge-introduction-to-multiagent-systems-ch1-2|Wooldridge, 2009]], a multiagent system is a society of agents that *"will be representing or acting on behalf of users or owners with very different goals and motivations."* Its two stated differences from ordinary concurrent systems:

- **Coordination is not hardwired at design time.** Autonomous agents need mechanisms to *"synchronize and coordinate their activities at run-time."*
- **Encounters are economic.** In a concurrent system *"all the computing elements are implicitly assumed to share a common goal"*; in a multiagent system agents *"are primarily concerned with their own welfare."* Hence the field's focus on negotiation, auctions and game theory.

Wooldridge's slogan for the second point, contrasting agents with objects: ***"Objects do it for free; agents do it because they want to."*** An agent that receives a request decides whether to act on it.

The systems [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail|MAST]] studies keep the first difference and drop the second. They are typically built by one team, for one goal, with roles assigned in a prompt, which in Wooldridge's terms is a concurrent system of agents rather than a society of them. MAST's system-design and inter-agent-misalignment failures therefore arise **without** the conflicting interests the classical field was designed around. Two readings follow, and nothing in the corpus separates them: either run-time coordination is hard enough to fail on its own, or LLM agents reproduce some of the behaviour of self-interested ones (talking past each other, undoing each other's work) without having interests at all. Only the chapters on cooperation and negotiation, not yet supplied, would show what the classical toolkit offers here.

## Compounding error handled by measurement, and the message board (added 2026-09-18)

In the Q&A of [[2026-09-17-rashad-pydata-production-ready-agentic-harness|Rashad's PyData talk (September 2026)]], an audience member put the compounding problem numerically — a 96%-accurate step seven layers deep gives about 75%. Rashad's answer is to model each component's failure probability from observed runs rather than design it away. In one of his projects the component that failed most was memory, not the model. For agent-to-agent communication he recommends a shared message board every agent reads and writes, "like Reddit or Twitter", over more elaborate message-bus designs. His claim that this scales to tens of thousands of agents comes without a source, so it is recorded here as opinion.
