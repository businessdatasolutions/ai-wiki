---
type: concept
aliases: ["small language model", "small language models", "SLM", "SLMs", "SLM-first", "heterogeneous agentic systems"]
tags: [small-language-models, slm, agentic-ai, ai-agents, inference-economics, edge-deployment, quantization, model-specialization, fine-tuning, open-weight-models, tool-calling, function-calling, heterogeneous-agents]
confidence: 0.75
last_confirmed: "2026-10-05"
accessed_at: "2026-10-05"
source_count: 11
relationships:
  - type: instance-of
    target: foundation-models
    via: "SLMs are foundation models selected by deployment footprint rather than by capability ceiling — the same object class, a different point on the size axis"
  - type: supports
    target: ai-agents
    via: "the claim that most agentic invocations are narrow enough to be served by a small specialised model rather than a generalist frontier LLM — model size as an agent design variable"
  - type: supports
    target: open-source-ai
    via: "the own-vs-rent argument reaches the laptop through small open-weight models: you cannot experiment with a model you can only rent, and small is what makes local ownership practical"
  - type: depends-on
    target: ai-benchmarks
    via: "every claim that a small model matches a large one is a benchmark claim, and which benchmark (generalist vs agentic, single-turn vs multi-turn) decides whether it holds"
  - type: part-of
    target: agent-harness
    via: "model selection is a harness decision — heterogeneous systems route each invocation to the cheapest model that can serve it, and the harness is what does the routing"
quality_score: 1
---

# Small Language Models (SLMs)

Language models chosen by **deployment footprint** rather than capability ceiling: small enough to run on hardware you already own, at latency low enough to serve one user's agentic requests in real time. The wiki tracks SLMs as a **design variable for [[ai-agents|agents]]** — the claim that most of what an agent asks a model to do is narrow enough that a generalist frontier model is over-provisioned for it.

The position was stated as a research argument by [[NVIDIA]] Research and Georgia Tech ([[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|Belcak et al., 2025]]), demonstrated as a working model family by [[Salesforce AI Research]] ([[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2|xLAM-2 / APIGen-MT]]), measured on an academic instrument by [[UC Berkeley]] ([[2025-07-13-patil-berkeley-function-calling-leaderboard|BFCL]]), and carried to a practitioner audience by [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Sokolenko at PyCon DE 2026]].

## The definition is device-indexed, so it moves

The canonical working definition (WD1) is deliberately **not** a parameter count:

> *A SLM is a LM that can fit onto a common consumer electronic device and perform inference with latency sufficiently low to be practical when serving the agentic requests of one user.*
> — [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|Belcak et al. 2025]]

An LLM is then simply "a model that is not a SLM." Any number attached to this is a **dated instance** of the definition, not the definition:

| Stated | Threshold | Hardware assumed |
| --- | --- | --- |
| Belcak et al., mid-2025 | *"most models below 10bn parameters"* | consumer device, 2025 |
| [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models\|Sokolenko, 2026]] | **10–30B**, 4-bit quantized, in 16–32 GB of consumer RAM | laptop, 2026 |

The wiki holds the definition, not the number. Sokolenko adds a field observation the papers do not: **8B models "are still stupid and dumb" for agentic work; things get interesting around 30B at 4-bit quantization** — including the point at which the model reliably *terminates* its loop.

## Why agents are the case where small works

Five arguments, in rough order of how well they hold up.

1. **Agents expose a narrow slice of the model.** The strongest one, and it is really an observation about the [[agent-harness|harness]]: *"an AI agent is essentially a heavily instructed and externally choreographed gateway to a language model… restricted to operate within a small section of its otherwise large pallet of skills."* The work the harness does to *constrain* a generalist is evidence a specialist would have sufficed.
2. **Format alignment beats format versatility.** Agentic output is parsed by code, so one output format produced reliably is worth more than six produced occasionally. A model post-trained on a single convention is *better suited*, not merely cheaper.
3. **Economics.** Serving a 7B model is cited at **10–30× cheaper** than a 70–175B model in latency, energy and FLOPs; fine-tuning is a few GPU-hours rather than weeks. Sokolenko reframes this as an *experimentation* argument rather than a unit-cost one — the binding constraint is that you cannot iterate on a model that will not fit on your machine.
4. **Heterogeneity is free.** Any call in an agentic system can pick any model, and a model can be a tool called by another model. So SLM-first does not mean LLM-never: the recommended shape is **SLMs by default, frontier LLMs invoked selectively**.
5. **The agent generates its own specialisation data.** Instrument the non-HCI calls and you accumulate exactly the narrow instruction data needed to fine-tune the model that replaces the incumbent on that call — a live example being APIGen-MT's synthetic-trajectory pipeline. Cf. [[2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1|self-improving agents]].

## The four capabilities that actually matter

The corpus's cleanest short answer to *what an agentic model has to be good at* — and the reason generalist benchmarks are the wrong instrument here:

1. **Task decomposition** — breaking a prompt into subtasks. *"This is what reasoning is."*
2. **Tool calling** — initiating a call, passing parameters, formatting output.
3. **Glue-code generation** — for cases where no tool covers the problem.
4. **Instruction following** — staying inside guardrails.

The headline claim drawn from these: for these four, an SLM of size *x* is now roughly as capable as a generalist LLM of **ten times** that size.

## What the evidence actually shows

The strongest and best-measured instance is [[xLAM]]-2 on [[Berkeley Function Calling Leaderboard|BFCL]] — and reading it carefully is a lesson in how to read every claim in this area:

- On **single-turn** function calling, xLAM-2-70b (88.48) and GPT-4o (88.1) are indistinguishable. **That category is saturated**, so parity there means little.
- On **multi-turn**, xLAM-2-70b scores **75.12** against 41–47 for GPT-4o and 36 for `o1`. The entire margin lives here — and multi-turn is exactly the category BFCL's own authors identify as unsolved.
- Even the **1B** model, ranked 36th overall, beats `o1` and `gpt-4o` on multi-turn.
- But on **τ-bench overall**, xLAM-2-70b (56.2) loses to Claude 3.5 Sonnet new (60.1), `o1` (63.9) and Claude 3.7 with an optimised prompt (69.8).

So: **narrow, real, and measured on the axis that matters — not general parity.** And every rank is dated: xLAM-2 held BFCL ranks 1–2 in April 2025 and roughly position 18 of ~110 by December 2025.

## The counter-arguments worth keeping

- **Scaling laws and the "semantic hub."** Larger models are better at general language understanding, full stop, and may integrate meaning across domains in a way small models structurally cannot. The rebuttal is that scaling-law studies hold architecture constant, ignore task-specific fine-tuning, and — the sharper move — that agentic systems *decompose* problems until the subtasks are simple enough that general abstraction buys nothing.
- **Centralised inference may win on economy of scale anyway.** Load-balancing a fleet of specialised endpoints is harder than balancing one generalist endpoint, and self-hosting adds infrastructure and staffing costs routinely omitted from per-token comparisons. **The proponents concede this is unresolved** — *"the jury is still out."* This is the honest state of the economic case.
- **Inertia may simply win.** Roughly USD 57bn of capital is committed to centralised LLM inference, tooling was built for that paradigm, and SLM development still evaluates itself on generalist benchmarks. Named as barriers, not refutations — but barriers with balance sheets behind them.

## The practical stack (2026)

What running an SLM agent locally actually takes, per [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Sokolenko]]:

| Layer | 2026 choice | Reason given |
| --- | --- | --- |
| Model | [[xLAM]]-2 32B, 4-bit quantized | open weights, top-20 on [[Berkeley Function Calling Leaderboard\|BFCL]], fits 16 GB |
| Local inference | `llama.cpp` | uses Apple-silicon GPUs; simple Hugging Face naming |
| Remote inference | Together AI, [[Hugging Face]] | when the workload graduates to production |
| Framework | [[LangChain]] / LlamaIndex | orchestration; routes tool choice off function names, argument names and docstrings |

And the migration path from an existing LLM agent, per Belcak et al. §6: **log non-HCI calls → curate and de-identify (10k–100k examples) → cluster into recurring tasks → select a candidate SLM per task → LoRA/QLoRA fine-tune (optionally distilling from the incumbent LLM) → iterate.**

## Related concepts

[[ai-agents]] · [[agent-harness]] · [[foundation-models]] · [[ai-benchmarks]] · [[open-source-ai]] · [[react-reasoning-acting]]

## Debates and supersession

- **What "small" means is contested by construction.** The definition is device-indexed and therefore moves with consumer hardware; treat 10B (2025) and 10–30B (2026) as the same definition evaluated in different years, and expect the number to move again. Nothing here is superseded — the *number* is.
- **The economic case is not settled, by the proponents' own admission.** Whether per-token savings survive the loss of centralised load-balancing plus self-hosted infrastructure and staffing is *"highly case-specific."* No source in the corpus resolves it, and any page citing the 10–30× figure should carry that caveat.
- **The capability case rests on benchmark transfer, which the same argument warns against.** Belcak et al. name reliance on the wrong benchmarks as adoption barrier B2 — and then support their own capability claim with a roster of benchmark results, four of eight from their own lab. Consistent, but it means V1 stands or falls on whether BFCL-style agentic benchmarks predict deployment.
- **A same-vendor tension worth holding open.** [[2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai|NVIDIA's CEO argues owners should build frontier-scale intelligence]] while NVIDIA Research argues most agentic work is over-provisioned. Different layers of the stack, opposite rhetorical directions, same company.
- **The gap nobody has closed:** no source measures an SLM-based agent against an LLM-based one **on the same task, under the same harness, with the same evaluation**. Until one does, "as good as models ten times the size" is a benchmark claim, not a deployment claim — and the [[ai-benchmarks]] page's scaffold-versus-model confound applies in full.
- **Loop termination may be size-conditioned.** Sokolenko reports that below ~30B, agentic loops *"can never terminate… because the SLMs are incentivized to call as many tools as they can."* If that holds, the runaway-loop failure in [[2026-08-25-thurium-wang-google-cloud-four-ways-loop-engineering-fails|Google Cloud's loop-engineering taxonomy]] is partly a model-capability threshold rather than purely a harness-design problem. Single-source, unmeasured, and worth confirming.

## The loop-count argument for a cheap model (added 2026-09-15)

[[2026-09-14-google-cloud-agent-factory-agent-harnesses-explained|Google Cloud's *Agent Factory*]] reaches this page's conclusion from an axis the corpus had not recorded: not device fit, not privacy, not experimentation cost, but **how many times the model runs per task**.

> *"Agents don't work like traditional single-turn prompt boxes. They run in continuous loops, so an agent might inspect a directory, update a function, execute unit tests, and then repeat that sequence 20, 40, or even 60 times just to finish one task. So when you have something that uses that many sequential hops, speed and cost compound dramatically. So a fast, cost-effective model isn't a downgrade — it is the exact thing that makes real-time agentic loops practical and responsive."*

The claim is narrower and more testable than the SLM position paper's: nothing here says a small model is *as capable*, only that **per-invocation latency and cost multiply by the loop count**, so the cheapest model that clears the task bar wins on wall-clock and spend. It is the vendor's argument for Gemini 3.8 Flash as a daily driver, and it is the same reasoning [[agent-harness]] records under heterogeneous routing — with the loop count supplying the multiplier that makes the routing decision material.

Note this is a vendor recommending its own cheaper tier, with no measurements attached.

## A security practitioner's bet on small, local models (added 2026-09-19)

[[2026-09-10-alim-pydata-ai-security-paradox-asymmetric-threats|Alim (PyData, Sep 2026)]] makes the SLM case from an unexpected direction, and labels it speculation: *"small language models that runs on consumer hardware is going to be the future … so small that … they run natively on macOS, on iOS, on your consumer laptops and phones."* His reason is competitive rather than technical. The frontier labs' moat is size, and *"that has not been working just because Chinese labs are able to produce very effective, smaller, much cheaper models,"* so *"the power is going to be taken away from large corporations and … be in the consumer's hands."*

It adds no evidence to this page (see [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|Belcak et al.]] for the careful version), and confidence is unchanged. It is worth recording for its vantage: someone whose job is securing software sees local, owned models as the likely end state. That bears on the security argument [[open-source-ai]] records, where open models measured worse on package hallucination. If deployment moves to the device, that gap becomes an endpoint-security problem.


## A specialised model that does not generate text (added 2026-09-22)

This page argues from **size**: a small model is enough for the narrow calls an agent makes. Three LangChain sources on [[TypeSafe AI]]'s **Jev** make the same heterogeneous-system argument from **output type**. Jev is a *"System One"* decision model. It takes a state and typed questions (choice / score / yes-no) and returns probabilities, with no text generation ([[2026-09-17-runkle-lovell-langchain-building-a-harness-with-jev|Runkle & Lovell]]; [[2026-09-21-runkle-langchain-building-a-harness-with-jev|Runkle video]]). The claim is that many agent decisions are classifications: which model to route to, whether a tool call is risky, whether an answer passes a rubric. So they can move off the generalist model. *"Use an LLM for open-ended reasoning and generation, and Jev for fast, structured decisions along the way."*

**Jev's size is not disclosed**, so it is not evidence for the *small*-model claim. It is evidence for the *specialised*-model one, which is the core of [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|Belcak et al.]]'s portfolio argument. The one measurement ([[2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals|Shea & Roche]], five cases, used as an eval judge) is instructive about the economics. Jev cost **$0.00035 per call against GPT-5.6 Luna's $0.00039**, but GPT-5.6 Terra's $0.00289 and Claude Sonnet 4.6's $0.02811. Latency was ~5–6× lower than every LLM. Against a cheap generalist tier, the per-call saving nearly disappears; the latency saving does not. That fits the [[2026-09-14-google-cloud-agent-factory-agent-harnesses-explained|loop-count argument]] above: in a loop, latency compounds. Confidence unchanged; all three sources come from the vendor distributing the integration.

## The buyer's version: frontier models on routine work (added 2026-09-28)

[[2026-08-25-lukic-goydan-bcg-so-what-ai-costs-a-fortune|Lukic & Goydan (BCG, Aug 2026)]] make the routing argument from the cost side, not the builder's side. Paul Goydan: *"A frontier model costs 30% more than a good enough model. Yet… we see more often than not very basic rudimentary tasks are being handed over to frontier models. It's like giving your teenage driver a brand-new Ferrari."* He calls model selection *"a whole new capability"* for companies, alongside controlling context-window size. The 30% figure is BCG's and is far smaller than list-price gaps between frontier and small models, so the direction of the claim is more useful than the number.

## Decision models beside frontier models, as a vendor's roadmap (added 2026-10-05)

[[2026-10-05-chase-langchain-interrupt-nyc-opening-keynote|Chase at Interrupt NYC (LangChain, 24 Sep 2026)]] places [[TypeSafe AI]]'s Jev in a portfolio rather than presenting it as a replacement: *"absolutely there will be these frontier models that are driving these really complex harnesses… But there's also a ton of other decisions that need to be made."* He names three uses, each tied to latency:

- **Evals in the loop**: *"if you can score it quickly according to some criteria as it's running… you can catch mistakes in real time."*
- **Guardrails**: *"One of the downsides of guardrails is that it always adds latency."*
- **Routing** among agents, models, skills or tools.

Two additions to the section above. First, LangChain's gateway now hosts a second decision model, **SemIf**, described as open source. Chase claims *"a massive explosion in these open source decision models since Jev launched"* but names no other. Second, the slide's worked example shows the output type concretely: a support message scored **0.999** on an `is_urgent` question by `jev-1.13.0`. Jev's size is still undisclosed and the *20–200x faster, 40–400x cheaper* range is still TypeSafe's, so this page's *specialised, not necessarily small* reading stands. Confidence unchanged.
