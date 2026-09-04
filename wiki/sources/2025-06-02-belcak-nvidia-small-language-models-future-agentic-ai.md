---
type: source
kind: paper
title: "Small Language Models are the Future of Agentic AI"
author: ["Peter Belcak", "Greg Heinrich", "Shizhe Diao", "Yonggan Fu", "Xin Dong", "Saurav Muralidharan", "Yingyan Celine Lin", "Pavlo Molchanov"]
publisher: "NVIDIA Research (with Georgia Institute of Technology); arXiv:2506.02153v2 [cs.AI], position paper, CC BY 4.0"
url: "https://arxiv.org/abs/2506.02153"
project_page: "https://research.nvidia.com/labs/lpr/slm-agents"
date_published: 2025-06-02
date_revised: 2025-09-15
date_ingested: 2026-09-04
length: "~20 pages (full text read: §1–7, alternative views, barriers, conversion algorithm, appendices A–B; reference list skimmed)"
raw: "../../raw/papers/small-language-models-are-the-future-of-agentic-ai.md"
tags: [small-language-models, slm, agentic-ai, ai-agents, position-paper, nvidia, georgia-tech, inference-economics, heterogeneous-agents, fine-tuning, lora, edge-deployment, tool-calling, instruction-following, scaling-laws, model-specialization, llm-to-slm-conversion, open-source-ai]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/improving-digital-maturity
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2
    via: "cited by the paper as evidence for its central capability claim — *'Salesforce xLAM-2-8B. The 8bn model achieves state-of-the-art performance on tool calling despite its relatively modest size, surpassing frontier models like GPT-4o and Claude 3.5.'* The position paper argues SLMs are already good enough; xLAM-2 is one of the seven model families it points to as proof, and the only one whose training recipe the wiki also holds"
    confidence: 0.85
  - type: supports
    target: 2025-07-13-patil-berkeley-function-calling-leaderboard
    via: "the paper's argument turns on evaluating models by *agentic* capability rather than generalist benchmarks — it names that reliance on generalist benchmarks as barrier B2 — and BFCL is the benchmark that makes the alternative measurable. The two are complementary halves of the same claim: the position paper says size is the wrong variable, BFCL is the instrument that shows what the right one looks like"
    confidence: 0.75
  - type: supports
    target: 2026-07-29-ng-washington-post-china-open-source-ai-competitiveness
    via: "arrives at the democratisation argument from the compute side rather than the geopolitics side — *'when more individuals and organizations can participate in developing language models… the aggregate population of agents is more likely to represent a more diverse range of perspectives'*. Both treat cheap, ownable, locally-runnable models as the condition for broad participation"
    confidence: 0.7
  - type: contradicts
    target: 2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai
    via: "same company, opposite emphasis, and worth holding side by side. NVIDIA Research argues the industry over-provisions frontier LLMs for work that a fine-tuned sub-10B model handles, and that the centralised-inference build-out is largely inertia (barrier B1); NVIDIA's CEO argues sovereign owners should build and own frontier-scale intelligence. The papers are not strictly incompatible — one is about per-invocation model choice, the other about who owns the stack — but the rhetorical direction on how much compute agentic work needs is opposite, and both are NVIDIA speaking"
    confidence: 0.6
---

# Belcak et al. (NVIDIA Research) — Small Language Models are the Future of Agentic AI

A **position paper**, not an empirical study — and the wiki should read it as such. Eight authors from **[[NVIDIA]] Research** (with **Yingyan Celine Lin** of Georgia Institute of Technology) argue that the industry's default of routing every agentic language-model call to a generalist frontier LLM is a **misallocation**, and that small language models are the natural substrate for most of what agents actually do. Published 2 June 2025, revised 15 September 2025.

It is the research backbone of [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Serhii Sokolenko's PyCon DE talk]], which is how it entered the corpus.

## TL;DR

> *"The rise of agentic AI systems is… ushering in a mass of applications in which language models perform a small number of specialized tasks repetitively and with little variation."* — Abstract

The position, stated as three value claims the paper labels **V1/V2/V3**, is that SLMs are

1. **V1 — sufficiently powerful** to handle the language-modelling errands of agentic applications;
2. **V2 — inherently more operationally suitable** for agentic systems than LLMs;
3. **V3 — necessarily more economical** for the vast majority of LM uses in agentic systems.

Where general conversational ability genuinely matters, the paper's answer is not "use an LLM" but **heterogeneous agentic systems** — SLMs by default, LLMs invoked selectively.

The authors are explicit that this is a **value statement**, not a prediction and not a recommendation: *"we make a statement of what we see as a faithful reflection of the community's values in this context."* They also go further than most position papers are comfortable going, calling the shift *"a Humean moral ought"* on sustainability grounds. That sentence is the tell that this is advocacy with an institutional interest attached — see *Scope and reliability* below.

## The definition (WD1) — and why it moves

> **WD1.** *A SLM is a LM that can fit onto a common consumer electronic device and perform inference with latency sufficiently low to be practical when serving the agentic requests of one user.*
>
> **WD2.** *An LLM is a LM that is not a SLM.*

Note what this does: it defines "small" by **deployment target**, not by parameter count, and then notes only in passing that *"as of 2025, we would be comfortable with considering most models below 10bn parameters in size to be SLMs."* The number is an instance of the definition at a hardware moment, not the definition. This is exactly the point on which Sokolenko, reading the same definition against 2026 laptops, lands at **10–30B** — see [[small-language-models]] for how the wiki holds the two.

## The seven arguments

| # | Argument | Supports |
| --- | --- | --- |
| **A1** | SLMs are already powerful enough to replace LLMs in agents | V1 |
| **A2** | SLMs are more economical in agentic systems | V3 |
| **A3** | SLMs are more flexible (cheap to fine-tune, deploy, specialise) | V2, V3 |
| **A4** | Agents expose only a very narrow slice of LM functionality | V1, V2 |
| **A5** | Agentic interactions require close behavioural alignment (one output format, reliably) | V2 |
| **A6** | Agentic systems are naturally heterogeneous — any call can pick any model | V2 |
| **A7** | Agentic interactions are themselves a data source for future specialisation | V2 |

**A4 is the load-bearing one** and the most quotable claim in the paper:

> *"An AI agent is essentially a heavily instructed and externally choreographed gateway to a language model… the underlying large language model that was engineered to be a powerful generalist is, through a set of tediously written prompts and meticulously orchestrated context management, restricted to operate within a small section of its otherwise large pallet of skills."* — §3.4

This is the same boundary the wiki's [[agent-harness]] page draws, read from the opposite direction: the harness's job of constraining the model is *evidence* that a smaller model would have sufficed.

**A5** is the argument most likely to be underrated. Agentic calls are consumed by code, so a single, reliably-produced output format matters more than format versatility: *"it is undesirable for the model to make the occasional hallucinatory mistake and respond in a format different from that being expected by the 'code parts' of the agentic system."* A model post-trained on one format beats a generalist that can do six.

**A3** (flexibility) carries a **democratisation** claim the wiki has met before from the geopolitics side in [[2026-07-29-ng-washington-post-china-open-source-ai-competitiveness|Andrew Ng's open-weights case]], and reaches here from the compute side: *"when more individuals and organizations can participate in developing language models… the aggregate population of agents is more likely to represent a more diverse range of perspectives and societal needs."*

**A7** closes a loop the wiki has seen elsewhere: instrument the agent's own non-HCI calls, and you accumulate exactly the specialised instruction data needed to fine-tune the SLM that replaces the LLM on that call. Self-improvement by logging — cf. [[2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1|CS329A on self-improving agents]].

## The capability evidence (§3.1)

The paper's support for V1 is a **roster of published model results**, not experiments the authors ran. Worth recording verbatim, because it is what "SLMs are good enough" actually rests on:

| Model family | Claim as stated |
| --- | --- |
| Microsoft **Phi-2** (2.7B) | commonsense reasoning and code generation *on par with 30B models*, ~15× faster |
| Microsoft **Phi-3 small** (7B) | language understanding / commonsense on par with, code generation up to, **70B** models of the same generation |
| NVIDIA **Nemotron-H** (2 / 4.8 / 9B) | instruction following and code generation comparable to dense 30B LLMs at an order-of-magnitude fewer inference FLOPs |
| Hugging Face **SmolLM2** (125M–1.7B) | matches 14B contemporaries on understanding, tool calling and instruction following; matches 70B models of two years prior |
| NVIDIA **Hymba-1.5B** | best instruction accuracy in its class, 3.5× token throughput; outperforms 13B models on instruction following |
| **DeepSeek-R1-Distill** (1.5–8B) | the 7B Qwen distill outperforms Claude-3.5-Sonnet-1022 and GPT-4o-0513 on reasoning |
| DeepMind **RETRO-7.5B** | GPT-3 (175B) language-modelling performance with 25× fewer parameters (retrieval-augmented) |
| Salesforce **xLAM-2-8B** | state-of-the-art tool calling, surpassing GPT-4o and Claude 3.5 → [[2025-04-04-prabhakar-salesforce-apigen-mt-xlam-2|APIGen-MT paper]] |

Four of the eight entries are NVIDIA's own models. That is not disqualifying — they are published, externally benchmarked results — but it is the shape of the evidence.

**The economics claim (A2)**, similarly, is cited rather than measured: *"serving a 7bn SLM is 10–30× cheaper (in latency, energy consumption, and FLOPs) than a 70–175bn LLM."* Fine-tuning agility is put at *"a few GPU-hours,"* letting behaviours be *"added, fixed, or specialized overnight rather than over weeks."*

## Where the paper is unusually honest: alternative views (§4)

Position papers rarely steelman the opposition this carefully, and this section is the most useful part of the paper for a sceptical reader.

- **AV1 — the generalist always wins on any single language task.** Grounded in scaling laws (CA1) and the "semantic hub" hypothesis (CA2: LLMs integrate meaning across languages and modalities in a way small models structurally cannot). **Rebuttal:** scaling-law studies hold architecture constant (A8) while SLM work shows architecture matters differently at small sizes; fine-tuning for the specific task is unaccounted for (A9); test-time compute scaling is cheap on a small model (A10); and — the sharpest one — agentic systems *decompose problems*, so *"any general abstract understanding due to the hub would be of little utility"* on subtasks that simple (A11).
- **AV2 — centralised LLM inference wins on economy of scale anyway.** Load-balancing a fleet of expert SLM endpoints is harder than one generalist endpoint (CA3), and infrastructure plus talent costs are routinely omitted from per-token comparisons (CA4). The authors **concede this is a valid view** — *"the jury is still out"* — and offer only that inference scheduling is improving (A12) and setup costs are falling (A13). This is the most important admission in the paper: the economic case is directionally argued, not settled.
- **AV3 — both worlds are possible; LLM-first has a head start and industry inertia.** Acknowledged as *"a distinct possibility."*

## The three barriers (§5)

Why hasn't this already happened? The paper's own answer, and its most testable set of claims:

1. **B1 — sunk investment.** Large capital bets on centralised LLM inference (the paper cites ~USD 57bn in hosting infrastructure) mean the tooling was built for that paradigm and *"omitting any considerations"* for decentralised or on-device inference.
2. **B2 — SLMs are evaluated on generalist benchmarks.** SLM development *"follows the tracks of LLM design, focusing on the same generalist benchmarks"* — and the paper notes that when you measure agentic utility specifically, the small models win. This is the direct argument for why something like the [[2025-07-13-patil-berkeley-function-calling-leaderboard|Berkeley Function Calling Leaderboard]] matters more than a general knowledge benchmark for this question.
3. **B3 — lack of popular awareness.** SLMs don't get the marketing.

All three are called *"practical hurdles and far from being fundamental flaws."*

## The LLM→SLM conversion algorithm (§6)

The paper's operational contribution — six steps, and the part a practitioner can act on:

| Step | What it is |
| --- | --- |
| **S1** | **Secure usage data collection** — instrument and log all non-HCI agent calls (prompts, responses, tool-call contents, latency), encrypted, role-based access, anonymised |
| **S2** | **Data curation and filtering** — 10k–100k examples is the stated rule of thumb; strip PII/PHI; paraphrase sensitive application-specific inputs |
| **S3** | **Task clustering** — unsupervised clustering over collected prompts and actions to find recurring operations (intent recognition, extraction, summarisation, tool-specific code generation) |
| **S4** | **SLM selection** — per task, on capability, benchmark fit, licensing, deployment footprint |
| **S5** | **Specialised fine-tuning** — LoRA / QLoRA or full fine-tune; optionally distil from the incumbent LLM |
| **S6** | **Iteration and refinement** — retrain periodically on new data; a continuous loop back to S2 or S4 |

## Dynamic capabilities (Warner & Wäger)

- **`digital-seizing/balancing-digital-portfolios`** — the paper is, structurally, a portfolio argument: heterogeneous agentic systems that route each invocation to the cheapest model that can serve it, with frontier LLMs reserved for the calls that genuinely need generality. §3.6 (A6) states it directly.
- **`digital-transforming/improving-digital-maturity`** — §6's conversion algorithm is a maturity path for an organisation already running LLM agents: instrument, cluster, specialise, iterate. It presumes an existing deployment and describes how to industrialise it.
- **`contextual/internal-barriers`** — §5 names three adoption barriers explicitly, two of which (sunk infrastructure investment, benchmark habits) are organisational inertia rather than technical limits.

## Linked entities and concepts

- Concepts: [[small-language-models]], [[ai-agents]], [[foundation-models]], [[ai-benchmarks]], [[agent-harness]], [[open-source-ai]]
- Entities: [[NVIDIA]], [[xLAM]], [[Salesforce AI Research]], [[Hugging Face]], [[Berkeley Function Calling Leaderboard]], [[Microsoft]], [[Google DeepMind]]
- **Dangling** (single-source mention, deferred): Peter Belcak, Pavlo Molchanov, Yingyan Celine Lin, Georgia Institute of Technology, Phi, Nemotron-H, SmolLM2, Hymba, DeepSeek-R1-Distill, RETRO, NVIDIA Dynamo

## Scope and reliability

**Genre first: this is a position paper.** It runs no experiments, reports no new measurements, and says so. Its evidence is a curated reading of other people's published results, four of eight from the authors' own lab, and its economics are cited ranges (10–30×) rather than a costing the authors performed.

**The institutional interest is real and points both ways.** NVIDIA sells the GPUs that serve frontier LLMs *and* the consumer/edge hardware that runs SLMs locally, and §3.2 promotes NVIDIA Dynamo and ChatRTX by name as the enabling infrastructure. A reader should not treat "an NVIDIA paper arguing against big models" as automatically disinterested; it is an argument that more inference happens in more places.

**What it is genuinely good for:** the WD1 definition; the A4 narrow-gateway argument; A5 on format alignment; the §4 alternative views (unusually well-argued against itself, and the AV2 concession is load-bearing); the §5 barriers; and the §6 conversion algorithm, which is the most concrete migration recipe in the corpus. Cite it for **framing and mechanism**; do not cite it for magnitudes.

## Debates and supersession

- **AV2 is unresolved by the paper's own admission.** Whether the per-token savings of specialised SLMs survive the loss of centralised load-balancing and the addition of self-hosted infrastructure and staffing costs is, in the authors' words, *"highly case-specific"* and *"the jury is still out."* No source in the wiki settles it.
- **The 10B threshold is already dated.** See [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Sokolenko (2026)]], who applies the same WD1 definition to 2026 consumer hardware and gets 10–30B, and who reports that 8B models *"are still stupid and dumb"* for agentic work in practice. The wiki treats WD1 as the durable claim and any parameter number as a dated instance of it.
- **Same-vendor tension.** Read against [[2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai|Jensen Huang on sovereign AI]]: NVIDIA Research says most agentic work is over-provisioned; NVIDIA's CEO says own your intelligence at frontier scale. Different levels of the same stack, but the two documents pull in opposite rhetorical directions on how much compute agentic work requires.
- Open: nobody has published a **like-for-like task comparison** — same agent, same harness, same evaluation, LLM swapped for a fine-tuned SLM. Until then V1 rests on benchmark transfer, which is precisely what the paper's own barrier B2 warns is unreliable.
