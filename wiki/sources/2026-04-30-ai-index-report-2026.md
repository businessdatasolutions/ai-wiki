---
type: source
kind: report
title: "Artificial Intelligence Index Report 2026"
author: ["Sha Sajadieh", "Loredana Fattorini", "Raymond Perrault", "Yolanda Gil", "Vanessa Parli", "Lapo Santarlasci", "Juan Pava", "Nestor Maslej", "Russ Altman", "Erik Brynjolfsson", "Carla Brodley", "Jack Clark", "Virginia Dignum", "Vipin Kumar", "James Landay", "Terah Lyons", "James Manyika", "Juan Carlos Niebles", "Yoav Shoham", "Elham Tabassi", "Russell Wald", "Toby Walsh", "Dan Weld"]
publisher: "Stanford Institute for Human-Centered AI (Stanford HAI)"
journal_volume: "9th edition, April 2026"
url: "https://hai.stanford.edu/ai-index/2026-ai-index-report"
license: "CC BY-ND 4.0"
date_published: 2026-04-01
date_ingested: 2026-04-30
tags: [ai-index, stanford-hai, annual-report, AI-sovereignty, jagged-frontier, GenAI-adoption, AI-investment, china-us-gap, schmidt-sciences, medicine-ai, sha-sajadieh, yolanda-gil]
length: "~430 pages (read pp. 1-19: front matter, top takeaways, Chapter 1 highlights and notable-models section; on 2026-11-07 also Chapter 4 Economy pp. 171-175 and §4.3 Corporate AI Adoption pp. 193-203, the rest of Chapter 4 searched but not read; Chapter 6 Medicine pp. 255-257 and p. 278 only; chapters 2, 3, 5, 7-9 deferred)"
raw: "../../raw/reports/ai_index_report_2026.pdf"
---

# Artificial Intelligence Index Report 2026 (9th edition)

## TL;DR

The **9th** annual [[AI Index]] from [[Stanford HAI]]. Cite as: Sajadieh et al. 2026.

**Headline framing** (from Co-chairs [[Yolanda Gil]] and [[Raymond Perrault]]):

> "The data does not point in a single direction. It reveals a field that is scaling faster than the systems around it can adapt."

The report tracks "the gap between what AI can do and how prepared we are to manage it" — running through every chapter. New in 2026: standalone chapters on **AI in Science** (Ch 5) and **AI in Medicine** (Ch 6, in collaboration with [[Schmidt Sciences]]); an analytical framework on **AI sovereignty**; new estimates of generative AI's economic value alongside emerging labor-market evidence.

This page summarizes the **front matter and the 15 Top Takeaways**; per-chapter deep-reads of the ~430-page report are deferred.

**Companion live talk-track** on the Stanford HAI YouTube channel ([[2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report]]): a ~73-minute presentation on 27 May 2026 by EiC [[Sha Sajadieh]] with a 42-minute panel Q&A featuring [[Raymond Perrault]] (Co-chair) and [[Russell Wald]] (Stanford HAI Executive Director). The talk-track restates this report's headline numbers and adds editorial / interpretive material not in the published artifact: the **absorption-gap** as the single observation running through the report, the **acceptability-threshold research gap** (Perrault: *how reliable must AI be to be acceptable in legal / medical / finance?*), an academic-vs-industry transparency argument, the founding-mission *facts-only* discipline, and Perrault's disclosure of a joint **World-Bank / IMF global-AI-adoption measurement initiative** with [[Yolanda Gil]] (agreement-in-principle from major US companies; *not in time for the next edition*).

## What's new vs. the [[2026-04-28-ai-index-report-2025|2025 edition]]

- **Chapter structure**: Medicine split out from Science (was combined as one chapter in 2025); ninth chapter added.
- **Editorial leadership**:
  - **Co-chairs**: [[Yolanda Gil]] (USC, ISI) — *new chair*, was chair-elect in 2025; [[Raymond Perrault]] (SRI International) — was chair in 2025, now co-chair.
  - **Editor-in-Chief**: [[Sha Sajadieh]] (Stanford) — *replaces* [[Nestor Maslej]] who led the 2025 edition (Maslej remains a contributor).
  - **Steering Committee additions**: Vipin Kumar (U Minnesota), Dan Weld (U Washington), Elham Tabassi (Brookings).
  - **Departures from steering committee** vs 2025: John Etchemendy (Stanford), Katrina Ligett (Hebrew U).
- **New supporting partner**: Infosys; remaining: Google, NSF, OpenAI, Open Philanthropy, Quid.
- **New analytics/research partner**: [[Schmidt Sciences]] (collaborated on Medicine chapter).
- **Same data partners as 2025**, plus Zeki (was already there, may have been newer).

## The 15 Top Takeaways

### 1. AI capability is not plateauing

- Industry produced **>90%** of notable frontier models in 2025.
- **SWE-bench Verified**: 60% → near 100% in one year.
- Several models meet/exceed human baselines on PhD-level science questions, multimodal reasoning, competition mathematics.
- **Organizational adoption: 88%** (up from 78% in 2024, per the [[2026-04-28-ai-index-report-2025|2025 edition]]). Source: McKinsey's State of AI 2025 ([[2025-11-05-mckinsey-state-of-ai-2025]]), reprinted in Chapter 4 (pp. 193–197). McKinsey changed the question from "adopted" (2024) to "regular use" (2025); the AI Index does not note this.
- **4 in 5** university students now use generative AI.

### 2. The U.S.-China AI model performance gap has effectively closed

- DeepSeek-R1 briefly **matched** the top U.S. model in February 2025.
- As of March 2026, [[Anthropic]]'s top model leads by just **2.7%**.
- U.S. still produces more top-tier models and higher-impact patents.
- China leads in publication volume, citations, patent output, industrial robot installations.
- **South Korea leads in AI patents per capita.**

### 3. United States hosts the most AI data centers, fabricated by one Taiwanese foundry

- **5,427** U.S. data centers — more than 10× any other country.
- U.S. AI data center energy consumption higher than any other country.
- **TSMC** fabricates almost every leading AI chip → global supply chain dependent on one foundry in Taiwan.
- TSMC-U.S. expansion began operations in 2025.

### 4. The "jagged frontier" is now an AI Index narrative

- **Gemini Deep Think** earned a **gold medal at IMO**, yet the top model reads analog clocks correctly only **50.1%** of the time.
- **AI agents on OSWorld**: 12% → ~66% task success in one year (real computer tasks across operating systems).
- Still fail roughly **1 in 3** attempts on structured benchmarks.
- This is the same concept introduced empirically in [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua et al. 2026]] — see [[jagged-frontier]].

### 5. Robots still fail at most household tasks

- Robots succeed in only **12%** of household tasks.
- **RLBench** robotic manipulation (software-based simulations): **89.4%** success.
- Wide gap between predictable lab settings and unpredictable household environments.

### 6. Responsible AI not keeping pace with capability

- **Documented AI incidents: 362 in 2025**, up from **233 in 2024**.
- Almost all leading frontier developers report capability benchmarks; reporting on responsible AI benchmarks remains spotty.
- Recent research finds **improving one RAI dimension (e.g., safety) can degrade another (e.g., accuracy)** — a tension previously implicit but now empirical.

### 7. United States leads in AI investment, but talent attraction is declining

- **U.S. private AI investment: $285.9B in 2025**, ~23× China's $12.4B.
  - For context, [[2026-04-28-ai-index-report-2025|the 2025 edition]] reported $109.1B for U.S. private investment in 2024 — a ~2.6× year-on-year increase.
- **1,953 newly funded AI companies** in U.S. in 2025 — more than 10× the next country.
- **AI researchers/developers moving to the U.S. dropped 89% since 2017, with an 80% decline in the last year alone.**
- China's $12.4B figure likely *understates* total spending given government guidance funds.

### 8. AI adoption spreading at historic speed

- **Generative AI: 53%** population adoption within three years — faster than the PC or the internet.
- Adoption correlates strongly with **GDP per capita**.
- Outliers: **Singapore (61%)**, **UAE (54%)** higher than expected; **U.S. ranks 24th at 28.3%**.
- **Estimated value of GenAI tools to U.S. consumers: $172B annually by early 2026.**
- Median value per user **tripled** between 2025 and 2026.

### 9. Productivity gains and entry-level employment decline coincide

- Productivity gains of **14–26%** in customer support and software development.
- Weaker or *negative* effects in tasks requiring more judgment.
- AI agent deployment remains in **single digits** across nearly all business functions.
- **U.S. software developers ages 22–25: employment fell nearly 20% from 2024**, even as headcount for older developers continues to grow.
- Mirrors the [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson Canaries paper]]'s finding via different methodology and a more recent timeframe; see [[ai-employment-effects]].

### 10. AI's environmental footprint is expanding

- **Grok 4 training emissions: 72,816 tons CO₂eq.**
- AI data center power capacity: **29.6 GW** — comparable to New York state at peak demand.
- **Annual GPT-4o inference water use alone may exceed the drinking water needs of 1.2 million people.**

### 11. AI for science can outperform human scientists, but bigger isn't always better

- Frontier models **outperform** human chemists on average on **ChemBench**.
- Score **<20%** on replication in astrophysics, **33%** on Earth observation questions.
- **MSAPairformer** (111M params) beat previous protein methods on ProteinGym.
- **GPN-Star** (200M params, genomics) outperformed a model nearly 200× larger.
- Most AI foundation models for science come from **cross-sector collaborations**, contrasting with the industry-dominated landscape of general-purpose AI.

### 12. AI is transforming clinical care, but rigorous evidence remains limited

- Ambient AI scribes saw substantial 2025 adoption: physicians reported up to **83% less time** spent writing notes; significant burnout reductions.
- Of 500+ clinical AI studies reviewed: **nearly half rely on exam-style questions** rather than real patient data; only **5% use real clinical data** (p. 278, citing the ARISE Network's *State of Clinical AI Report*, January 2026; not the Index's own analysis).
- The evidence base for clinical AI remains thin despite mass deployment.

### 13. Formal education lagging; people learning AI skills at every life stage

- **>80% of U.S. high school and college students** use AI for school-related tasks.
- Only **half** of middle and high schools have AI policies; just **6% of teachers** say those policies are clear.
- AI engineering skills accelerating fastest in **UAE, Chile, South Africa**.
- New AI PhDs in U.S. and Canada **+22%** from 2022 to 2024 — and the new PhDs took jobs in **academia, not industry** (a notable reversal).

### 14. AI sovereignty as a defining feature of national policy

- Expansion of national AI strategies, particularly in developing economies.
- State-backed AI supercomputing investments rising in parallel.
- Open-source contributions from rest-of-world now **outpace Europe** and approach the U.S. on GitHub.
- Fueling more linguistically diverse models and benchmarks.

### 15. Expert-public trust gap is large; institutional trust is fragmented

- On AI's impact on jobs: **73% of experts** expect a positive impact vs **23% of public** — a **50-point gap**.
- Globally, the **EU is trusted more than the U.S. or China** to regulate AI effectively.
- The **U.S. reported the lowest level of trust in its own government** to regulate AI (31%).

## Key claims by chapter (highlights only)

### Chapter 1 — Research and Development

- Industry produced **91.18%** of notable AI models in 2025; Industry-academia collaboration 4.90%; Other 1.96%; pure Academia 1.96%.
- 2025 by country: **United States 59 notable models, China 35, South Korea 8.**
- 2025 by organization: **OpenAI 20, Google 14, Alibaba 11, Anthropic 7, xAI 5, DeepSeek 4, LG AI Research 4, Meta 4, Tsinghua University 4** (the only academic institution in the top 9).
- **Disclosure dropping**: training code, dataset sizes, parameter counts increasingly withheld for the most capable systems.
- **Parameters** stable in the trillion-parameter range for three years; training compute (estimable independently) continues to rise.
- **Synthetic data** still not replacing real data in pre-training, but **OLMo 3.1 Think 32B** with ~90× fewer parameters than Grok 4 achieves comparable benchmark results via pruning, deduplication, curation alone.
- **Global AI compute capacity: 17.1M H100-equivalents**, growing **3.3× per year** since 2022.
- **Nvidia: >60%** of total compute. Google and Amazon supplying much of the remainder; Huawei holding small but growing share.
- Open source: **5.6M projects on GitHub**; **Hugging Face uploads tripled since 2023**; U.S.-based projects still attract most engagement (30M cumulative GitHub stars on projects past the 10-star threshold).
- Talent: **AI researchers/developers moving to U.S. -89% since 2017, -80% last year alone.**
- Per-capita researcher density: **Switzerland and Singapore lead.**
- Female AI researcher representation: **Saudi Arabia 32.3%, Canada 29.6%, Australia 30.1%** — no country approaches parity.

### Chapter 4 — Economy: §4.3 Corporate AI Adoption (pp. 193–203; read 2026-11-07)

The section draws on [[McKinsey & Company]]'s State of AI survey ([[2025-11-05-mckinsey-state-of-ai-2025]]) and says of it: *"the results are self-reported and should be viewed as directional rather than comprehensive"* (p. 193).

- **Breadth.** 88% of respondents say their organisation uses AI in at least one business function, up from 78% in 2024; over half use it in three or more functions. 79% say their organisation *"regularly"* uses generative AI in at least one function, up from 71% (p. 193, Figure 4.3.1). The chapter highlights give 70% instead (p. 173); the body and chart say 79%.
- **By region, 2023 → 2024 → 2025:** Europe 57 → 80 → 91%, North America 61 → 82 → 90%, Greater China 48 → 75 → 88%, Asia-Pacific 58 → 72 → 82% (p. 194, Figure 4.3.2).
- **Depth: deployment stage by revenue** (p. 197, Figure 4.3.6). "Fully scaled" is 5% of firms under US$100M, 4% at US$100–499M, 3% at US$500–999M, 9% at US$1–4.9B and 10% at US$5B+. The gradient is not monotonic. In every band below US$5B, most firms are experimenting or piloting.
- **Agents.** *"Scaled use was in the single digits for nearly all functions"*. Exception: technology firms in software engineering (24%), IT (22%) and service operations (21%) (pp. 197–198).
- **Outcomes** (organisations that use AI): 64% report improved innovation, 38% lower cost, 36% higher profitability, 33% organic revenue growth (p. 196, Figure 4.3.5).
- **No maturity figure.** The words "mature" and "maturity" do not occur in Chapter 4 (pp. 171–230). The 2025 edition's *"1% of C-suite … mature"* is not repeated. The deployment-stage chart is the closest measure of depth.
- **Population diffusion** (Microsoft AI Economy Institute data, pp. 200–201). The US is 24th at 28.3% in the second half of 2025; the Netherlands is 8th at 38.9%. The text gives the UAE as 54% (pp. 173, 200), the chart 64.0% (Figure 4.3.12).

For the [[ai-maturity-measurement-comparison]] thread: breadth rose (78% → 88%, across a change of question wording), and the only depth measure is McKinsey's stage question, with "fully scaled" at 3–10% by firm size.

### Chapters 2, 3, 5–9 and most of Chapter 4: not yet ingested

Chapter 4 (Economy) was read in part on 2026-11-07: overview, highlights and §4.3 (above). Its sections on investment, jobs and robots were searched, not read. From Chapter 6 (Medicine) only the overview (pp. 255–257) and the evidence-gaps passage (p. 278) were read; see [[ai-in-health-care]]. Chapters 2 (Technical Performance), 3 (Responsible AI), 5 (Science), 7 (Education), 8 (Policy and Governance) and 9 (Public Opinion) remain deferred.

## Methodology notes

- **AI tooling acknowledgement**: "The AI Index is written by a team of human researchers. The authors used ChatGPT and Claude to help refine and copy edit drafts. All images in this publication were generated with AI by Johanna Friedman (2026), Gemini 3.1 (W-Nanobanana2), Gemini 3 (W-Nanobanana Pro)." — visibly more AI-assistance disclosure than the 2025 edition.
- **Notable models** dataset: still curated by Epoch AI; year-over-year counts may differ from prior reports as new/historic models are continually added.
- **License**: **CC BY-ND 4.0** (no derivatives) — same as 2025.

## Quotes worth saving

> "A year ago, this report documented AI's arrival as a mainstream force. This year's data shows what happens after arrival." — Co-chairs

> "The data does not point in a single direction. It reveals a field that is scaling faster than the systems around it can adapt." — Co-chairs

> "AI capability is not plateauing. It is accelerating and reaching more people than ever." — Top Takeaway #1

> "AI models can win a gold medal at the International Mathematical Olympiad but cannot reliably tell time — an example of what researchers call the jagged frontier of AI." — Top Takeaway #4

> "Productivity gains from AI are appearing in many of the same fields where entry-level employment is starting to decline." — Top Takeaway #9

## Limitations / caveats (per report)

- Notable-model counts depend on Epoch AI's curation; not a census of all models.
- Disclosure decline among frontier labs makes some technical-performance metrics estimates rather than ground truth.
- Most-cited AI papers (top 100) lag 1–2 years; 2024 paper data is as recent as available.
- Public-opinion data gathered in survey years that may pre-date the latest model releases.

## Authorship and steering

The full author list is recorded in the source frontmatter and the citation block below. Promoted-to-entity contributors with steering or research-management roles on this edition:

- **Editor-in-Chief** — [[Sha Sajadieh]] (replacing [[Nestor Maslej]] from the 2025 edition).
- **Co-chairs of the Steering Committee** — [[Yolanda Gil]] (chair, USC ISI; co-author of the headline Co-chairs' message) and [[Raymond Perrault]] (co-chair, SRI International; co-author of the same message).
- **Steering Committee members** — [[Erik Brynjolfsson]] (Stanford Digital Economy Lab), [[James Manyika]] (Google / UN High-Level Advisory Body on AI), [[Yoav Shoham]] (Stanford CS / AI21 Labs), [[Russell Wald]] (Stanford HAI Executive Director), [[Terah Lyons]] (Partnership on AI), [[Juan Carlos Niebles]] (Salesforce / Stanford), [[Vanessa Parli]] (Stanford HAI), [[Jack Clark]] (Anthropic).
- **Research team contributors** — [[Loredana Fattorini]] (Stanford HAI Research Manager), [[Lapo Santarlasci]] (IMT School for Advanced Studies Lucca), [[Nestor Maslej]] (continuing contributor after handing off the EiC role).

Additional named co-authors on the 2026 edition (single-source mentions, deferred per [§Lifecycle "Author-entity promotion"](../../CLAUDE.md#author-entity-promotion)): Juan Pava, Russ Altman, Carla Brodley, Virginia Dignum, Vipin Kumar, James Landay, Elham Tabassi, Toby Walsh, Dan Weld.

## Related in this wiki

- [[AI Index]] — entity; updated to reflect 9th edition leadership and chapters
- [[Stanford HAI]] — publisher
- [[2026-04-28-ai-index-report-2025]] — prior (8th) edition; same pages now have 2026 updates
- [[2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report]] — companion talk-track on the Stanford HAI YouTube channel (27 May 2026); first-person editorial-interpretation layer with Perrault + Wald panel Q&A; *acceptability-threshold gap* and *World-Bank / IMF measurement initiative* disclosures
- [[Schmidt Sciences]] — new analytics/research partner
- [[generative-ai]] — 53% population adoption; $172B U.S. consumer value; $285.9B U.S. private investment
- [[foundation-models]] — 91.18% industry; 17.1M H100-equivalents; OLMo 3.1 Think 32B vs Grok 4
- [[ai-benchmarks]] — SWE-bench 60%→100%; OSWorld agents 12%→66%; ChemBench frontier vs human chemists; analog clock 50.1%
- [[responsible-ai]] — 362 incidents (up from 233); RAI dimension trade-offs
- [[enterprise-ai-adoption]] — 88% organizational adoption; AI agent deployment in single digits per function; §4.3: 79% regular GenAI use, "fully scaled" 3–10% by revenue band, no maturity figure
- [[ai-employment-effects]] — 14–26% productivity gains; software dev 22–25 -20% from 2024
- [[jagged-frontier]] — IMO gold + analog clock 50.1%; OSWorld leap; AI Index now uses the term
- [[2026-04-28-dellacqua-jagged-technological-frontier]] — original empirical anchor for the jagged-frontier concept
- [[2026-04-28-brynjolfsson-canaries-coal-mine]] — adjacent labor-market evidence (ADP payroll); the 2026 AI Index extends the same finding via a different data path
- [[2026-04-28-anthropic-economic-index-q4-2025]] — Anthropic's parallel measurement initiative
- [[ai-in-health-care]] — concept page (created 2026-11-07) that sets this source beside the hospital and health-system surveys.
