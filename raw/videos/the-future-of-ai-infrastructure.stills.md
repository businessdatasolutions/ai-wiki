---
video_id: pabDkNR7jIs
url: https://www.youtube.com/watch?v=pabDkNR7jIs
transcript: raw/videos/the-future-of-ai-infrastructure.md
stills_dir: raw/images/the-future-of-ai-infrastructure
stills_count: 31
extractor:
  method: hand-picked (no Gemini call)
  reason: Gemini API returned 402 (prepayment credits depleted)
  sampling: 239 frames at 360p, one every 10 s, consecutive repeats merged (160x90 grayscale MAD < 1.5) into 237 tiles, read as 5x6 contact sheets
  frames: yt-dlp stream URL (<=1080p) seeked with ffmpeg
acquired: '2026-11-17'
---

# Stills manifest (hand-picked)

Each still was chosen from the contact sheets and then read at full resolution. The readings below were made by viewing the pixels; the source page carries the verified transcriptions of the published ones. Times are on the VOD clock, the same clock as the transcript. Where a slide builds up, the still is cut from its fully built state and the time given is the start of that state.

Viewed and not saved: stage shots, the Project Suncatcher launch and lab footage, the topology animations at 11:20–12:00 (unlabelled), title cards (Agent Compute Engine, Gemini + Agent Compute Engine, Agent Substrate + CNCF logo, the closing QR card), and the big-number slides and lower thirds whose figures the narration reads out (+7,800% agent traffic, 50–70% inference share, 55x compute intensity, 9,600-chip superpod, 2.7x, 288 GB HBM / 3x on-chip SRAM, up to 80% performance per dollar, 2x HBM bandwidth, PUE 1.09, >3x compute per unit of energy, up to 30% better price-performance).

## 01 · 1:30 · Gemini agent task with subagents
- File: `01-01m30-gemini-agent-task-and-subagents.png` · [1:30](https://www.youtube.com/watch?v=pabDkNR7jIs&t=90s)
- Gemini app: task "Prepare Q4 product launch materials"; four-step progress plan; plan.json and plan.md; three subagents running. **Published.**

## 02 · 4:10 · Search: request, lookup, response
- File: `02-04m10-search-request-lookup-response.png` · [4:10](https://www.youtube.com/watch?v=pabDkNR7jIs&t=250s)
- Three boxes, Request → Lookup (a server stack) → Response. **Not published:** the narration describes the search query in more detail than the diagram.

## 03 · 5:40 · AI Hypercomputer layers
- File: `03-05m40-ai-hypercomputer-layers.png` · [5:40](https://www.youtube.com/watch?v=pabDkNR7jIs&t=340s)
- Four layers: Flexible consumption, Open software, Purpose-built hardware, Data centers and energy. **Not published:** still 31 repeats the layers with the announcements mapped onto them.

## 04 · 7:10 · Google TPU generations
- File: `04-07m10-google-tpu-generations.png` · [7:10](https://www.youtube.com/watch?v=pabDkNR7jIs&t=430s)
- Ten TPU boards labelled with name and year, TPU v1 2015 to TPU 8i 2026. **Published.**

## 05 · 8:30 · Six TPU design principles
- File: `05-08m30-six-tpu-design-principles.png` · [8:30](https://www.youtube.com/watch?v=pabDkNR7jIs&t=510s)
- Larger cores, systolic arrays, compiler-controlled memory, optical switching, compact numerics, liquid cooling (fully built; builds from 7:20). **Not published:** the narration names and explains all six.

## 06 · 9:00 · TPU 8t board
- File: `06-09m00-tpu-8t-board.png` · [9:00](https://www.youtube.com/watch?v=pabDkNR7jIs&t=540s)
- Photo of the 8t board, two packages labelled TPU 8t. **Not published:** a product photo the narration describes.

## 07 · 14:00 · Three production bottlenecks
- File: `07-14m00-three-production-bottlenecks.png` · [14:00](https://www.youtube.com/watch?v=pabDkNR7jIs&t=840s)
- Enterprise trust and reinforcement learning (Hardware encryption + Unified clusters); Context and agent density (Million-token memory bandwidth); Software implementation (Native PyTorch support for TPUs). Builds from 13:20. **Not published:** the narration says the same, almost word for word.

## 08 · 15:20 · TPU 8tx and TPU 8i Max
- File: `08-15m20-tpu-8tx-and-8i-max.png` · [15:20](https://www.youtube.com/watch?v=pabDkNR7jIs&t=920s)
- Two icons: TPU 8tx, Secure & Confidential Inference; TPU 8i Max, Massive-Context, High-Throughput Inference. **Not published:** narration word for word.

## 09 · 15:50 · TPU 8tx specifications
- File: `09-15m50-tpu-8tx-specs.png` · [15:50](https://www.youtube.com/watch?v=pabDkNR7jIs&t=950s)
- Board render with lower third: 12.6 PFLOPS FP4 compute, TPU 8tx, 216 GB HBM3e. **Not published:** the narration gives both figures; the still adds only "HBM3e".

## 10 · 16:10 · Secure memory enclaves
- File: `10-16m10-secure-memory-enclaves.png` · [16:10](https://www.youtube.com/watch?v=pabDkNR7jIs&t=970s)
- Render of the 8tx board inside a glass box, captioned "Secure memory enclaves". **Not published:** illustration of a narrated term.

## 11 · 17:40 · TPU 8i Max specifications
- File: `11-17m40-tpu-8i-max-specs.png` · [17:40](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1060s)
- Lower third, fully built: 2x compute density, TPU 8i Max, 384 GB HBM, 17.2 TB/s HBM bandwidth, 768 MB SRAM. Builds from 17:00. **Not published:** every figure is spoken.

## 12 · 19:40 · Four eighth-generation TPU systems
- File: `12-19m40-four-tpu-systems.png` · [19:40](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1180s)
- TPU 8t Scale-Up Training, TPU 8i Low-Latency Reasoning, TPU 8tx Confidential Computing, TPU 8i Max Massive Context. **Not published:** narration word for word.

## 13 · 23:00 · TorchTPU: the code change
- File: `13-23m00-torchtpu-code-change.png` · [23:00](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1380s)
- Two code boxes: a typical PyTorch script (`"nccl"`, `"cuda"`) beside the same script on Cloud TPU (`"tpu_dist"`, `"tpu"`). **Published.**

## 14 · 23:40 · Open inference engines on TPU and GPU
- File: `14-23m40-open-inference-engines-stack.png` · [23:40](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1420s)
- Stack: Open-weight models | Frontier models; vLLM, SGL, inferact, RadixArk; TPU | GPU. **Not published:** the narration names the engines and partners. The slide spells the partner "RadixArk" (the caption track has "RadixArc").

## 15 · 24:10 · Two leading accelerator platforms
- File: `15-24m10-two-accelerator-platforms.png` · [24:10](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1450s)
- Ten TPU generations beside eight NVIDIA GPU instance families on Google Cloud (G2 to A4X Max). **Published.**

## 16 · 24:20 · NVIDIA GPU instances with A5X
- File: `16-24m20-nvidia-gpu-instances-a5x.png` · [24:20](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1460s)
- The GPU half alone, with A5X added as a ninth family. **Not published:** overlaps still 15; the addition is noted there.

## 17 · 25:40 · TPU Sync memory chart
- File: `17-25m40-tpu-sync-memory-chart.png` · [25:40](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1540s)
- Animated line chart, y-axis 0.00–0.25 without unit, legend TPU memory / Host CPU memory; footnote "TPU Sync supports v8, Ironwood (v7), Trillium (v6) and v5". **Published.**

## 18 · 27:10 · Disaggregation and caching
- File: `18-27m10-disaggregation-and-caching.png` · [27:10](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1630s)
- Agent request → GKE Inference Gateway (llm-d 1.0) → Prefill (Read prompt) / Decode (Generate response); three-tier KV cache below. **Not published:** first build of still 20.

## 19 · 27:40 · Multi-tenant quality of service
- File: `19-27m40-multi-tenant-quality-of-service.png` · [27:40](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1660s)
- Second build: background tasks and agent loops; gateway adds "Fair flow control"; prefill and decode in a "TPU pool". **Not published:** second build of still 20.

## 20 · 27:50 · vLLM and SGLang behind a single API
- File: `20-27m50-vllm-sglang-behind-single-api.png` · [27:50](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1670s)
- Final build: single API in front of the gateway; TPU and GPU pools each with prefill and decode; TPU memory ↔ (TPU Sync) host CPU memory ↔ KV cache storage. **Published.**

## 21 · 29:30 · Agents are a new workload
- File: `21-29m30-agents-are-a-new-workload.png` · [29:30](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1770s)
- Long-running, Stateful, Often idle; a timeline of one agent session: GPU/TPU inference bursts, CPU management bursts, state held throughout, t-0 to days. **Published.**

## 22 · 30:20 · Three runtime requirements
- File: `22-30m20-three-runtime-requirements.png` · [30:20](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1820s)
- Isolation and security, Instant activation, Statefulness. **Not published:** narration word for word.

## 23 · 31:30 · Sandbox isolation layers
- File: `23-31m30-sandbox-isolation-layers.png` · [31:30](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1890s)
- Nested boxes: Identity (an IAM principal for every sandbox) ⊃ Network (integrated gateway with egress controls) ⊃ Kernel (a microVM with its own kernel) ⊃ Agent-generated code. Builds from 31:10. **Published.**

## 24 · 32:30 · Your sandbox: pause and resume
- File: `24-32m30-your-sandbox-pause-resume.png` · [32:30](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1950s)
- Pauses when agents are idle (idle memory freed for others); Captures state (disk and memory saved); Reactivates instantly (same files, memory, and processes). Builds from 32:10. **Not published:** the narration says nearly the same.

## 25 · 32:50 · Titanium IPUs
- File: `25-32m50-titanium-ipus.png` · [32:50](https://www.youtube.com/watch?v=pabDkNR7jIs&t=1970s)
- Photo of a Titanium IPU card. **Not published:** product photo.

## 26 · 34:30 · Agent Compute Engine API
- File: `26-34m30-agent-compute-engine-api.png` · [34:30](https://www.youtube.com/watch?v=pabDkNR7jIs&t=2070s)
- Your harness → (Create · Snapshot · Suspend · Resume · Delete) → Agent Compute Engine API and SDK → Shared host pool, Google-run → Your sandbox: a Linux microVM. **Published.**

## 27 · 35:00 · Agent Substrate stack
- File: `27-35m00-agent-substrate-stack.png` · [35:00](https://www.youtube.com/watch?v=pabDkNR7jIs&t=2100s)
- Agent Substrate: Gateway (ingress/egress control), State persistence (suspend/resume), Kernel isolation (gVisor/microVM); over Storage, Kubernetes, Compute. **Published.**

## 28 · 36:50 · Agent governance model
- File: `28-36m50-agent-governance-model.png` · [36:50](https://www.youtube.com/watch?v=pabDkNR7jIs&t=2210s)
- Agent Registry, Agent Gateway (with Token management inside), Agent Identity, Agent Observability underneath, each with a one-line definition. Builds from 36:20. **Published.**

## 29 · 37:30 · Workload-optimized compute
- File: `29-37m30-workload-optimized-compute.png` · [37:30](https://www.youtube.com/watch?v=pabDkNR7jIs&t=2250s)
- Google Cloud machine families: general purpose (N-, C-, E-Series) and specialized (H-, Z-, M-, C*N-, M*N-, A-, G-Series, TPUs). **Not published:** a product catalogue; the narration's point is the CPU platform choice, which it states.

## 30 · 38:20 · Google Cloud customers around the world
- File: `30-38m20-google-cloud-customers.png` · [38:20](https://www.youtube.com/watch?v=pabDkNR7jIs&t=2300s)
- Logo wall of about 70 Google Cloud customers (Accenture, Deloitte, Goldman Sachs, PayPal, Siemens, Verizon, Walmart, Deutsche Bank and others). **Not published:** a logo wall of Google Cloud customers in general, not tied to any product in the talk.

## 31 · 39:30 · Recap: what's new
- File: `31-39m30-recap-whats-new.png` · [39:30](https://www.youtube.com/watch?v=pabDkNR7jIs&t=2370s)
- The four AI Hypercomputer layers with the announcements mapped onto three of them; Data centers and energy has none. Builds from 39:10. **Published.**
