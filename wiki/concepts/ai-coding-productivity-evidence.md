---
type: concept
title: AI coding productivity — the evidence
aliases: ["AI coding productivity", "AI developer productivity", "developer productivity evidence", "productivity paradox in coding", "throughput vs stability"]
confidence: 0.8
last_confirmed: "2026-08-30"
source_count: 6
accessed_at: "2026-08-30"
tags: [rct, productivity, metr, copilot, dora, throughput, delivery-stability, perception-gap, heterogeneity, seniority, measurement]
relationships:
  - type: part-of
    target: automation-vs-augmentation
  - type: supports
    target: micro-productivity-trap
  - type: contradicts
    target: ai-generated-code-quality
    via: "productivity studies score completed tasks and delivery throughput; the code-quality literature scores what those completions leave behind — 22.7% of AI-introduced issues never fixed, 45% of samples carrying OWASP flaws. The activity is the same; the ledgers are different, and only one of them is usually reported"
    confidence: 0.75
quality_score: 1
---

# AI coding productivity — the evidence

What randomised and population-scale studies actually find when AI is put in front of software developers. The corpus contains two RCTs with **opposite signs**, and reconciling them is more useful than picking one.

## The two randomised results

| | [[2025-07-10-becker-metr-early-2025-ai-experienced-developer-productivity\|METR (2025)]] | [[2026-02-27-cui-demirer-generative-ai-high-skilled-work-three-field-experiments\|Cui et al. (2026)]] |
| --- | --- | --- |
| Design | RCT, task-level randomisation | 3 field experiments, pre-registered |
| N | **16 developers**, 246 tasks | **4,867 developers** |
| Population | Experienced OSS maintainers, ~5 years on their own repos | Microsoft, Accenture, a Fortune 100 firm |
| Outcome | Completion **time** | Completed **tasks** |
| Result | **+19% time — slower** | **+26.08% tasks — faster** (SE 10.3%) |

**These are compatible, and the reconciling variable is stated in Cui et al.'s own heterogeneity result: less experienced developers adopted more and gained more.** METR studied the far tail of the experience distribution — maintainers who already hold the model of the system in their heads — which is exactly where this paper's gradient predicts the smallest gain. The synthesis is a **gradient claim**: *assistance is worth most where the marginal work is acquiring context, and least — possibly negative — where the developer already has it.*

Two cautions before either number is quoted. Cui et al.'s **standard error of 10.3%** puts the 95% interval roughly from +6% to +46%: the finding is "positive and probably substantial," not "26%." And METR's tooling vintage is **February–June 2025 Cursor Pro + Claude 3.5/3.7 Sonnet in an IDE** — not the cloud-agent parallelism the 2026 practitioner material is about.

## The perception gap, which is the finding with the widest reach

METR's participants forecast **−24%** before, estimated **−20%** after finishing, and were measured at **+19%**. **After personally doing the work, they were wrong by ~39 points, in a consistent direction.** Economics experts predicted −39%; ML experts −38%.

This is not a curiosity. It invalidates the instrument most organisations use. [[2025-09-23-dora-2025-state-of-ai-assisted-software-development|DORA 2025]] reports that **>80% of ~5,000 respondents believe AI increased their productivity** — a belief METR shows to be systematically wrong for experienced developers. DORA's *delivery* metrics are behavioural and survive this; its *perception* metrics should not be read as productivity evidence.

## The population signal, and its split

[[2025-09-23-dora-2025-state-of-ai-assisted-software-development|DORA 2025]]: **90% AI adoption** (up from 76% in 2024), **70% trust** in AI-generated code — meaning **30% do not trust the tool they are using**.

| Relationship with AI adoption | 2024 | 2025 |
| --- | --- | --- |
| Delivery **throughput** | negative (~1.5% drop per 25% adoption rise) | **positive** |
| Delivery **stability** | negative (~7.2% drop per 25% adoption rise) | **still negative** |

> "AI adoption does continue to have a negative relationship with software delivery stability."

**Throughput turning positive means the authoring constraint has been relieved. Stability staying negative means the delivery system's absorptive capacity — review, testing, rollback, observability — has not moved with it.** DORA's central thesis follows: *"AI doesn't fix a team; it amplifies what's already there."*

## What the productivity ledger leaves out

A completed-task count is a gross measure. Against it:

- **46.41% of agent-proposed fixes are rejected** ([[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes]]) — consuming review, CI and tokens on discarded work
- **22.7% of AI-introduced issues are never fixed** ([[2026-03-30-liu-debt-behind-the-ai-boom]])
- **45% of AI-generated samples introduce OWASP Top 10 flaws**, flat across model size and vintage ([[2025-07-30-veracode-2025-genai-code-security-report]])
- **Context files raise inference cost >20% for no measured success gain** ([[2026-02-12-gloaguen-evaluating-agents-md-repository-level-context-files]])

None of these refutes the productivity findings. They are **different points in the same pipeline**, and only the first one is flattering — which is why it is the one that gets cited.

## The practical position

The defensible reading of the whole corpus: **AI coding tools reliably increase output volume; whether they increase delivered value depends on the receiving system.** That is DORA's amplifier thesis, METR's context gradient, and [[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Carson's own anti-thesis]] — *"I don't get multiples of quality off of multiples of output"* — all saying the same thing from three different methodologies.

## Related concepts

[[concepts/automation-vs-augmentation|automation-vs-augmentation]], [[concepts/micro-productivity-trap|micro-productivity-trap]], [[concepts/ai-generated-code-quality|ai-generated-code-quality]], [[concepts/agentic-pull-requests|agentic-pull-requests]], [[concepts/jagged-frontier|jagged-frontier]], [[concepts/ai-employment-effects|ai-employment-effects]], [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]].

## Debates and supersession

- **METR vs Cui et al.** — reconciled above as a context gradient. That reconciliation is this wiki's inference; neither paper makes it. **Open:** a study that randomises across the experience distribution within one setting.
- **Vendor proximity.** Two of Cui et al.'s three sites are Microsoft (which owns GitHub) and a large systems integrator. Randomisation and pre-registration mitigate this; they do not eliminate it.
- **No study measures net value.** Every design here scores volume (tasks, time, throughput). **Nobody has measured AI-assisted development against a value or defect-adjusted outcome.** This is the largest gap in the concept.
- **Everything is pre-agentic.** METR measures IDE assistance; Cui et al. measure Copilot. **No RCT in the corpus measures cloud agent fleets**, which is what the 2026 practitioner material is about.
