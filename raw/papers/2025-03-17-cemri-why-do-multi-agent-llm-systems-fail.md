# Why Do Multi-Agent LLM Systems Fail?

**Authors:** Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt Keutzer, Aditya Parameswaran, Dan Klein, Kannan Ramchandran, Matei Zaharia, Joseph E. Gonzalez, Ion Stoica
**arXiv:** 2503.13657 (v1 17 Mar 2025; v2 22 Apr 2025; v3 26 Oct 2025)
**URL:** https://arxiv.org/abs/2503.13657
**Venue:** NeurIPS 2025 Datasets & Benchmarks track
**Captured:** 2026-08-30 (WebFetch of the arXiv abstract page)
**fulltext_source:** abstract-only — the abstract below is verbatim; the taxonomy detail is from the abstract's own enumeration, not from the full PDF.

---

## Abstract (verbatim)

> Despite enthusiasm for Multi-Agent LLM Systems (MAS), their performance gains on popular benchmarks are often minimal. This gap highlights a critical need for a principled understanding of why MAS fail. Addressing this question requires systematic identification and analysis of failure patterns. We introduce MAST-Data, a comprehensive dataset of 1600+ annotated traces collected across 7 popular MAS frameworks. MAST-Data is the first multi-agent system dataset to outline the failure dynamics in MAS for guiding the development of better future systems. To enable systematic classification of failures for MAST-Data, we build the first Multi-Agent System Failure Taxonomy (MAST). We develop MAST through rigorous analysis of 150 traces, guided closely by expert human annotators and validated by high inter-annotator agreement (kappa = 0.88). This process identifies 14 unique modes, clustered into 3 categories: (i) system design issues, (ii) inter-agent misalignment, and (iii) task verification. To enable scalable annotation, we develop an LLM-as-a-Judge pipeline with high agreement with human annotations. We leverage MAST and MAST-Data to analyze failure patterns across models (GPT4, Claude 3, Qwen2.5, CodeLlama) and tasks (coding, math, general agent), demonstrating improvement headrooms from better MAS design. Our analysis provides insights revealing that identified failures require more sophisticated solutions, highlighting a clear roadmap for future research. We publicly release our comprehensive dataset (MAST-Data), the MAST, and our LLM annotator to facilitate widespread research and development in MAS.

## Key numbers

- 1,600+ annotated traces; 7 popular MAS frameworks
- Taxonomy derived from rigorous analysis of 150 traces
- Inter-annotator agreement kappa = 0.88
- **14 failure modes in 3 categories:** (i) system design issues, (ii) inter-agent misalignment, (iii) task verification
- Models analysed: GPT-4, Claude 3, Qwen2.5, CodeLlama; tasks: coding, math, general agent
