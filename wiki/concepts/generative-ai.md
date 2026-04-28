---
type: concept
aliases: ["GenAI", "generative AI", "generative artificial intelligence"]
tags: [generative-ai, foundation-models, ai-adoption]
---

# Generative AI

AI systems that produce novel content (text, images, code, video, audio) by sampling from learned distributions over training data. Practically: large language models, image diffusion models, video generators, and the orchestrating systems built on top of them. As of 2024, GenAI represents **>20% of all AI-related private investment** ($33.9B globally) and is the dominant force behind the 2024 jump in [[enterprise-ai-adoption]].

## Working definition

In the [[AI Index]] taxonomy, "Generative AI" is a sub-class of AI distinguished by content generation rather than pattern recognition or prediction. It typically rests on [[foundation-models]] — large pretrained models adapted via prompting, fine-tuning, or retrieval. Generative AI is also where **agent** workflows are increasingly built (Salesforce's Agentforce, autonomous coding agents, etc.).

## Key claims

### Investment

- **$33.9B private investment in GenAI in 2024**, up 18.7% from 2023, **8.5× 2022 levels**. Now >20% of all AI-related private investment.
- U.S. GenAI investment **exceeded the combined total of China + EU + UK by $25.4B** in 2024 (gap was $21.8B in 2023).
- Source: [[2026-04-28-ai-index-report-2025|AI Index 2025]] §4.3 Chapter Highlights 2–3.

### Enterprise use

- **71% of orgs use GenAI** in at least one business function in 2024, up from 33% in 2023 — more than doubled. Source: [[2026-04-28-ai-index-report-2025|AI Index 2025]] §4.4.
- **U.S. AI-job postings citing GenAI skills tripled YoY** in 2024 (Lightcast data).
- Top use cases (% of orgs deploying GenAI for this function): marketing strategy content (27%), knowledge management (19%), personalization (19%), design (14%), code creation (13%).
- **Only 1% of C-suite executives describe their GenAI rollouts as "mature."** Most are still capturing value at small scale. See [[enterprise-ai-adoption]].

### Capability gains in 2024

- **AI video generation** breakthroughs: OpenAI's SORA, Stable Video Diffusion 3D and 4D, Meta's Movie Gen, Google DeepMind's Veo 2.
- **Test-time compute** (e.g., OpenAI's o1, o3) — models that iteratively reason — dramatically improved performance: **o1 = 74.4% on IMO qualifier** vs. GPT-4o's 9.3%, but at **~6× the cost and 30× the latency**.
- **Inference cost crashed**: GPT-3.5-equivalent cost dropped **280× in 18 months** (Nov 2022 $20/M tokens → Oct 2024 $0.07/M tokens via Gemini-1.5-Flash-8B).
- **Smaller models matching big ones**: Microsoft's Phi-3-mini (3.8B params) matched the 60% MMLU threshold previously held by PaLM (540B) — **142× reduction in 2 years**.
- AI agents show early promise: **RE-Bench** results — top systems score 4× human experts in 2-hour budgets, but humans win 2:1 at 32 hours. Already match human expertise on select tasks (e.g., writing Triton kernels).

### Agents (now its own concept page)

GenAI is the substrate for autonomous agents — see the dedicated [[ai-agents]] page covering the chatbot → agent → multi-agent progression, RE-Bench results, deployment examples (Salesforce Agentforce, Italgas DANA, Harvey, GitHub Copilot), and the cross-source debate over where agents fit in org maturity. [[2026-04-28-mit-sloan-ai-maturity|MIT CISR]] places autonomous agents as a Stage 3+ attribute; [[2026-04-28-anand-wu-genai-playbook|Anand-Wu]] places them in the "no regrets zone" of the task-suitability 2×2; [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]] frames them as the near-term productivity story for everyone.

### The access democratization (Anand-Wu)

[[2026-04-28-anand-wu-genai-playbook|Anand-Wu]] argue GenAI's most underrated change is **access**, not intelligence:

1. **Nontechie employees can use GenAI without expert support.** For decades AI was the domain of engineers, programmers, data scientists. ChatGPT changed that with natural-language interaction.
2. **GenAI is increasingly embedded into existing tools** — email, videoconferencing, spreadsheets, CRM, ERP — lowering adoption barriers further.

Anand-Wu compare this to the **MS-DOS → GUI transition** of the 1980s: not necessarily more powerful, but dramatically more accessible. The strategic implication: **competitive advantage will not come from access to the technology** (everyone has it) but from **complementary assets** — proprietary data, unique people/processes/culture. See [[enterprise-ai-adoption]].

### Tools and embeddings (mentioned across sources)

| Tool | Function | Citation |
|---|---|---|
| **ChatGPT** ([[OpenAI]]) | The democratization breakthrough | [[2026-04-28-anand-wu-genai-playbook\|Anand-Wu]] |
| **Harvey** | Legal contract drafting; quality-control zone | [[2026-04-28-anand-wu-genai-playbook\|Anand-Wu]] |
| **GitHub Copilot** | Code generation, debugging | [[2026-04-28-anand-wu-genai-playbook\|Anand-Wu]] |
| **Salesforce Agentforce** | Business operations agents | [[2026-04-28-ai-index-report-2025\|AI Index 2025]] |
| **Microsoft Copilot** | Embedded productivity assistant | [[2026-04-28-ai-index-report-2025\|AI Index 2025]] (job-postings data) |
| **Italgas DANA** | Generative-AI network control | [[2026-04-28-mit-sloan-ai-maturity\|MIT Sloan]] |

### Limits

- **Complex reasoning remains brittle.** AI excels at IMO problems but **fails PlanBench** (logical planning) even when provably correct solutions exist. Limits effectiveness in high-stakes settings where precision is critical.
- **Bias persists.** GenAI continues to exhibit implicit biases (race, gender, occupation) despite explicit-bias mitigation. See [[responsible-ai]].
- **The data commons is shrinking** — domains restricting AI training scrapers jumped from 5–7% to 20–33% in one year. Implications for training data quality and diversity.

### Automation vs. augmentation: a load-bearing distinction

The strategic choice for any GenAI deployment is whether it **automates** work (substitutes for labor) or **augments** it (complements labor). [[automation-vs-augmentation]] tracks this as a standalone analytical lens. The empirical record (per [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson et al. 2025]]) shows the choice has real labor-market consequences: automation uses are correlated with declining entry-level employment in highly-exposed occupations, while augmentation uses are not.

## Debates / contradictions

- **Will inference-cost decline continue?** Hardware (-30%/yr) and energy efficiency (+40%/yr) trends support it; data-commons shrinkage (see [[responsible-ai]]) cuts the other way; energy-supply constraints (driving nuclear partnerships) are a third force.
- **Test-time compute as a new scaling axis.** Promising but expensive (o1: 6× cost, 30× latency vs. GPT-4o). Open question: economic viability for routine enterprise use, or only for high-value reasoning tasks.
- **Hype vs. value gap.** 71% adoption + 1% maturity + revenue gains mostly <5% per function. The dollar productivity story is real but smaller than the discourse implies.

## Related concepts

- [[foundation-models]] — the substrate
- [[enterprise-ai-adoption]] — the deployment context
- [[responsible-ai]] — the governance overlay
- [[ai-benchmarks]] — how capabilities are measured

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "generative-ai")
SORT file.name ASC
```
