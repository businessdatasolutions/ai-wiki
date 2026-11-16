---
type: source
kind: video
title: "The Future of AI Infrastructure"
author: ["Google Cloud Tech"]
publisher: "Google Cloud Tech (YouTube channel), recorded livestream; Amin Vahdat (Google SVP and Chief Technologist of AI and Infrastructure); Mark Lohmeyer (Google Cloud VP and GM, AI and Computing Infrastructure); Maria Biggs (engineering director, Project Suncatcher)"
url: "https://www.youtube.com/watch?v=pabDkNR7jIs"
date_published: 2026-11-09
date_ingested: 2026-11-16
length: "~39:51 minutes (transcript ~205 lines; human-written track (en-US), 14 chapters)"
raw: "../../raw/videos/the-future-of-ai-infrastructure.md"
tags: [google, google-cloud, google-cloud-tech, amin-vahdat, mark-lohmeyer, maria-biggs, ai-hypercomputer, co-design, tpu, tpu-8t, tpu-8i, tpu-8tx, tpu-8i-max, agentic-inference, kv-cache, memory-wall, hbm, confidential-computing, energy-efficiency, pue, project-suncatcher, torchtpu, pytorch, vllm, sglang, llm-d, gke-inference-gateway, nvidia, vera-rubin, agent-compute-engine, microvm, sandbox, agent-substrate, kubernetes, cncf, agent-gateway, agent-registry, agent-identity, agent-governance, axion, cpu, jevons-paradox, livestream, vendor-keynote, science-technology]
dynamic_capabilities:
  - contextual/external-triggers
  - digital-transforming/navigating-innovation-ecosystems
relationships:
  - type: supports
    target: 2026-05-07-anthropic-managed-agents-decoupling-brain-hands
    via: "both describe hosted runtimes for long-running agents that keep sandboxed execution apart from the model and keep session state across pauses: Anthropic's Managed Agents splits brain, hands and session; Google's Agent Compute Engine runs each sandbox as a microVM that pauses and resumes with its memory and disk state"
    confidence: 0.75
  - type: supports
    target: 2026-06-09-cloudflare-investor-day-2026
    via: "both address CPU demand for agent execution: Cloudflare names the execution CPU as the next bottleneck to AI adoption and estimates 1 billion CPUs at ten agents each; Google says 'CPUs are making a comeback' and runs its agent runtimes on x86 and Arm (Axion) instances"
    confidence: 0.7
  - type: supports
    target: 2026-07-08-jensen-huang-why-companies-need-open-agent-systems
    via: "both present a secure runtime for enterprise agents as a required layer, offered in open form: NVIDIA's OpenShell sandbox in a blueprint with LangChain Deep Agents; Google's Agent Compute Engine and the open-source Agent Substrate on Kubernetes"
    confidence: 0.65
  - type: supports
    target: 2026-10-20-hamalainen-lala-takkar-mckinsey-economics-of-enterprise-ai
    via: "both describe agent workloads multiplying token use as unit costs fall, and both name the Jevons paradox: McKinsey cites per-token prices down about 90% with use growing faster; Google cites agent-driven traffic up 7,800% in a year and a forecast 24-fold rise in token demand by 2030"
    confidence: 0.65
---

# Vahdat & Lohmeyer (Google Cloud Tech) — The Future of AI Infrastructure

> Join Google SVP and Chief Technologist of AI and Infrastructure Amin Vahdat and Google Cloud VP and GM of AI and Computing Infrastructure Mark Lohmeyer on November 9 at 9:00 AM PT for a first look at AI infrastructure built for 24/7 AI agents. See how Google Cloud's AI Hypercomputer combines custom silicon, networking, and open software like PyTorch, vLLM, and Kubernetes to maximize performance.
>
> Speakers: Amin Vahdat, Mark Lohmeyer, Maria Biggs. Products Mentioned: Cloud TPUs, NVIDIA GPUs, Agent Compute Engine, GKE Inference Gateway
>
> *— Channel description, Google Cloud Tech*

## TL;DR

A 40-minute recorded livestream on the *Google Cloud Tech* channel ([[Google]]), 9 November 2026. **Amin Vahdat**, head of Google's AI and Infrastructure organisation, presents the hardware (0:00–21:16); **Maria Biggs**, engineering director of Project Suncatcher, gives a two-minute update on TPUs in orbit; **Mark Lohmeyer**, VP and GM of AI and Computing Infrastructure at Google Cloud, presents the software and agent runtimes (21:16–39:51). Scripted and slide-led, with a lab segment showing TPU boards.

**Human-written transcript**: the en-US caption track, on the video's own clock, with speaker changes marked (see the raw file's `notes:` for why the panel's CC track was replaced). Quotes below are verbatim from it.

What it adds to the wiki:

1. **Agents as an infrastructure workload, with a hyperscaler's numbers.** A human exchange uses about a thousand tokens; an agent doing the same task fires *"hundreds of model queries"* and consumes *"millions of tokens."* Agent-driven traffic rose more than 7,800% in a year; inference is 50–70% of AI compute, up from 40% two years ago.
2. **Accelerators split by stage of an agent's life cycle.** Four eighth-generation TPU systems, two announced here: **8TX** for confidential inference and **8i Max** for very long contexts.
3. **Agent execution as a CPU and sandbox problem.** *"Models reason, but agents also need to act. And so CPUs are making a comeback."* **Agent Compute Engine** runs each sandbox as its own microVM, pauses it with memory and disk state, and resumes it later: the first microVM-per-agent runtime described in the corpus.
4. **An open-source agent runtime donated to the CNCF**: **Agent Substrate**, on Kubernetes. *"The industry needs another Kubernetes moment."*
5. **Open serving software for proprietary chips**: TorchTPU, TPU support in vLLM and SGLang, and llm-d 1.0 for routing and KV-cache handling across mixed TPU and GPU fleets.
6. **A cross-cloud governance layer for agents**: gateway, registry, identity, observability and token budgets.

A vendor keynote announcing the vendor's products. Every performance, efficiency and security figure below is Google's claim, unaudited, and most come without a baseline.

## Why agents change the infrastructure (0:00–7:18)

Vahdat describes *"a fundamental inversion across three dimensions"*: from human scale to agent scale, from systems of record to systems of action, from simple requests to complex agentic workflows (3:44–3:56). A Google Search query *"coordinates across 10,000 servers in hundreds of milliseconds. It returns an answer and its job is complete."* An agent *"decomposes its goal, writes code, queries a model, calls external tools, inspects its output, and self-corrects"* (4:04–4:26).

His demand figures (4:52–5:21) cite only *"recent industry forecasts"*: agent-driven traffic up more than 7,800% in a year; inference at 50–70% of all AI compute consumption; global token demand 24 times higher by 2030, above 120 quadrillion tokens a month, which he converts into *"a 55-fold surge in compute intensity."* Later he calls it *"a modern Jevons Paradox… When you cut the cost of intelligence, human ambition doesn't stay fixed. It expands"* (12:48). [[2026-10-20-hamalainen-lala-takkar-mckinsey-economics-of-enterprise-ai|McKinsey's explainer on enterprise AI economics]] also names the Jevons paradox, for per-token prices down about 90% while use grew faster. See [[foundation-models]].

Google's answer is the **AI Hypercomputer**, *"a co-design system open at every layer"* from facilities to frameworks. All 14 of Google's billion-user products now use Gemini on TPUs, and Gemini has become *"a universal AI agent"* that spins up sub-agents and *"works across multi-day tasks"* (1:21, 6:05). The TPU began as a scaling failure: in 2013, neural voice search implied that *"if every Android user spoke to their phone for just three minutes a day, we would have had to literally double the number of Google data centers"*; the first TPU gave *"30 times the throughput of comparable processors"* (6:39–7:00).

Biggs reports (2:11) that a prototype satellite carrying TPUs has run its first inference in low Earth orbit, a prompt sent up and the output checked on Earth, while gathering data on radiation and thermal management in vacuum. Two satellites to test laser links between them follow next year. The stated aim is near-constant solar power for future workloads.

## TPUs: principles and the eighth generation (7:18–10:47)

Six design principles: fewer, larger cores scheduled by the compiler; systolic arrays; compiler-controlled memory instead of caches; optical circuit switches; *"range over precision"* in formats such as bfloat16 and native FP4, *"while maintaining strict bit wise determinism"*; and liquid cold plates beside the silicon. The lab segment sets TPU v1 (2015, an air-cooled 75 W card) beside a TPU 8T board with two compute packages, twelve HBM3e stacks and an interconnect at *"19.2 terabits per second, bidirectional per chip, double our previous generation."* The optical transceivers are liquid-cooled for the first time: *"even the light needs a cold plate."* A 9,600-chip 8T superpod gives nearly three times the compute per pod, cutting training timelines *"from months to weeks at 2.7 times lower costs"* (10:27), against an unstated baseline.

## Inference for agents, and two new systems (10:47–19:31)

*"Most organizations aren't building new models,"* so the rest is inference, where *"response speed is everything."* The 3D torus that suits pre-training takes up to 16 hops across the cluster; when a model is sharded, partial sums are exchanged for every token, so *"latency grows and the agent stutters"* (11:43). TPU 8i's hierarchical low-diameter topology, which Google calls Boardfly, cuts the worst case to seven hops and interchip latency *"by up to half."*

Vahdat names three production bottlenecks (13:13–14:06): **trust and RL** (hardware encryption for data in use; inference and reinforcement learning on the same silicon); **context and agent density**, where memory bandwidth forces customers to *"truncate the context, run fewer concurrent agents, or accept multi-second latency stalls"*; and **implementation**, meaning compatibility with the software teams already use. Six months after 8T and 8i came *"a second hardware drop within the same generation"* (14:58):

| System | Stated role | Figures as stated |
| --- | --- | --- |
| TPU 8T | Scale-up training | 9,600-chip superpod; 19.2 Tb/s interconnect per chip |
| TPU 8i | Low-latency reasoning | 16 → 7 hops; 288 GB HBM (+50%); 3× SRAM; up to 80% better performance per dollar |
| **TPU 8TX** (new) | Confidential inference | 8T silicon (12.6 PFLOPs FP4, 216 GB HBM); custom AMD hosts; PCIe link encryption, attestation, secure enclaves; 8i network; *"2x lower latency"* than 8T |
| **TPU 8i Max** (new) | Massive-context inference, rack density | Two dies per package; 384 GB HBM (+33%); 17.2 TB/s HBM bandwidth, 768 MB SRAM and twice the FLOPs of 8i |

8TX moves trust *"from software into silicon,"* so customers can run *"proprietary models and agents"* with IP *"locked down at the hardware level"* (15:56–16:13). For 8i Max, per-token speed is unchanged; doubled bandwidth admits more concurrent agents, *"more lanes to avoid the traffic jams"* (18:05).

## Power (19:31–21:16)

Google reports fleet-wide **power usage effectiveness of 1.09** over the past twelve months, *"83% less overhead energy than the industry average,"* and *"more than three times more compute performance per unit of energy than five years ago"* (20:17–20:40). It is pitched as unit economics for customers. The grid-capacity question that [[2026-10-16-sivaram-shandal-bcg-pitching-progress-emerald-ai-flexibility|Sivaram (Emerald AI)]] raises is not addressed.

## Open software across TPUs and GPUs (21:16–28:56)

Lohmeyer: *"co-designed must never mean closed."*

- **TorchTPU**, launched two weeks earlier and *"built with a PyTorch team at Meta,"* makes TPUs a native PyTorch backend.
- **vLLM and SGLang**, *"the two most popular open source inference engines,"* now support TPUs out of the box, with Inferact and RadixArk.
- **Two accelerator platforms.** *"We invest equally in… Google TPUs and NVIDIA GPUs"* (24:11). A5X instances on [[NVIDIA]]'s Vera Rubin platform are generally available on Google Cloud, and Google Distributed Cloud with NVIDIA Blackwell serves *"sovereign workloads"* on premise and air-gapped (24:21–24:48); see [[ai-sovereignty]].
- **TPU Sync**, announced here, moves working memory to server memory *"the moment an agent pauses"* for a tool, a human approval or a model call.
- **llm-d 1.0** in GKE Inference Gateway. Agent traffic *"is the inverse of human interactions. Human prompts are short and the answers are long, whereas an agent's input context is massive, carrying system instructions, tool definitions, and its conversation history"* (26:00). llm-d adds prefix-cache-aware routing, separate prefill and decode serving, three-tier KV-cache offloading (accelerator, host CPU, storage) and fairness-driven flow control, so long agent loops share hardware *"without starving real-time interactive applications."*

The openness is in serving and orchestration software; Gemini itself is closed. [[open-source-ai]] holds the corpus's open-weights argument.

Google's own strategy here is `digital-transforming/navigating-innovation-ecosystems` in plain form: it joins the PyTorch, vLLM, SGLang and Kubernetes ecosystems, works with Meta, Inferact, RadixArk and NVIDIA, and offers a competitor's GPUs on its platform so that using TPUs does not require leaving those ecosystems.

## Agent execution: CPUs, microVMs and an open runtime (28:56–36:10)

Agents are *"long running, they're stateful, but they also frequently are idle, pausing for seconds or hours while waiting for an external API or a human reply"* (29:27). Lohmeyer's three requirements are isolation (*"when Agents execute code on your behalf, you need strictly enforced boundaries"*), instant activation and statefulness. Google built **Agent Compute Engine** because, for its own Gemini agents, *"yesterday's computing infrastructure just wouldn't cut it."* As described:

- each sandbox is a lightweight VM on Cloud Hypervisor with its own guest kernel; egress policy, including domain allow-lists, is enforced from outside the microVM; sandboxes hold *"zero hard coded credentials"* (31:09–31:32);
- root access, Hyperdisk storage, custom images and a mounted GCS FUSE directory for datasets;
- the microVM pauses when the agent goes quiet: *"unlike traditional serverless setups that force an agent to reboot from scratch, agent compute engine captures the entire working memory and disc state"* (32:16), allowing *"thousands of VMs per host"*;
- on Titanium IPUs, *"a minimal memory-safe Rust hypervisor"* with networking and encryption offloaded to separate silicon, which, he claims, *"eliminates entire classes of memory corruption and sandbox escape vulnerabilities by design."*

Gemini's agents run on it and *"can resume a day, a week, or a month later"* with their context intact (33:57). Customers get an API to *"create, pause, and delete secure sandboxes,"* or **Agent Substrate**, an open-source runtime driven through standard Kubernetes APIs on GKE, on premise or on other clouds, which Google is donating to the Cloud Native Computing Foundation: *"10 years ago, Google created an open sourced Kubernetes… The industry needs another Kubernetes moment. It needs an open foundation for agent native runtimes"* (35:33–35:45).

Other sources describe this layer. [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic's Managed Agents post]] describes a model lab's hosted runtime, with the model, the sandboxed tools and the session log kept apart. [[2026-06-09-cloudflare-investor-day-2026|Cloudflare's Investor Day deck]] names the execution CPU as *"the next bottleneck to AI adoption"* and estimates 1 billion CPUs for agents. In [[2026-07-08-jensen-huang-why-companies-need-open-agent-systems|Jensen Huang's interview with Harrison Chase]], NVIDIA's OpenShell is the secure open runtime without which *"it's impossible to deploy."* See [[ai-agents]] and [[agent-harness]] for how the corpus separates model, harness and execution environment.

## Governance and CPU platforms (36:10–39:51)

Google's governance model for agents across environments: **Agent Gateway**, *"the air traffic controller for all client-to-agent and agent-to-anywhere traffic"*; **Agent Registry**, a directory of approved tools and MCP servers; **Agent Identity**, *"a digital signature for access control and auditing"*; **Agent Observability**; and token management in the gateway to *"attribute spend, enforce budget guardrails"* and keep secrets away from agents (36:10–36:57). See [[agent-fleet-management]].

The runtimes run on Intel and AMD x86 and on Google's Arm-based **Axion**, whose N4A instances, Lohmeyer claims, give *"up to 30% better price performance than the next leading hyperscaler"* (37:48). The customers he describes (enterprises in banking, financial services, healthcare and telecom; digital natives; *"the top AI labs"*) are unnamed.

For a firm deciding where to run agents, this is a `contextual/external-triggers` source: a disruptive digital technology, infrastructure rebuilt around agent workloads, that changes the cost of inference, the isolation of agent-executed code and the governance tools on offer. It says nothing about how a customer organisation should change to use it.

## Linked entities and concepts

- [[Google]] — publisher (*Google Cloud Tech* is an alias) and employer of all three speakers; [[Google DeepMind]] named as the TPU co-design partner.
- [[NVIDIA]] — Vera Rubin and Blackwell platforms on Google Cloud.
- **Concepts:** [[ai-agents]], [[agent-harness]], [[agent-fleet-management]], [[foundation-models]], [[open-source-ai]], [[ai-sovereignty]], [[dynamic-capabilities]].
- **Dangling** (single-source mention, deferred): Amin Vahdat, Mark Lohmeyer, Maria Biggs, Project Suncatcher, AI Hypercomputer, Agent Compute Engine, Agent Substrate, llm-d, Cloud Native Computing Foundation, Meta, AMD, Intel, Inferact, RadixArk.

## Source quality

A scripted product keynote on the vendor's channel. The figures are Google's claims about Google's products, with no third-party benchmarks, few baselines (none for 8T's "2.7 times lower costs" or the runtime's efficiency) and unnamed customers; the demand figures come from unnamed forecasts. Human-written caption track, quoted verbatim; it spells one partner "RadixArc", given here as RadixArk. **Slides and on-screen specifications are not captured**: the stream is slide-led, and a stills scan on 2026-11-16 failed (Gemini billing), so stills are deferred. Its value is a dated, detailed statement of how one hyperscaler divides agent infrastructure: accelerators per life-cycle stage, serving software tuned for long agent contexts, and microVM sandboxes that pause and resume.
