# Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?

**Authors:** Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev (ETH Zürich / SRI Lab)
**arXiv:** 2602.11988 (submitted 12 February 2026)
**URL:** https://arxiv.org/abs/2602.11988
**Captured:** 2026-08-30 (WebFetch of the arXiv abstract page)
**fulltext_source:** abstract-only — abstract verbatim below.

---

## Abstract (verbatim)

> A widespread practice in software development is to tailor coding agents to repositories using context files, such as AGENTS.md. Although this practice is strongly encouraged by agent developers, there is currently no rigorous investigation into whether such context files are actually effective for real-world tasks. In this work, we study this question and evaluate coding agents' task completion performance in two complementary settings: established SWE-bench tasks from popular repositories, with LLM-generated context files, and a novel collection of issues from repositories containing developer-committed context files. Surprisingly, we find that providing context files does not generally improve task success rates, while increasing inference cost by over 20% on average. This observation holds across different LLMs, coding agents, and for both LLM-generated and developer-committed context files. Specifically, we find that while instructions in the context files are well followed by coding agents, repository overviews, although popular and recommended by model providers, are not helpful. We conclude that while context files are useful for specifying non-standard coding practices, any attempts to improve performance should be rigorously evaluated before deployment.

## Key points

- Two settings: **SWE-bench tasks with LLM-generated context files**, and a **novel collection of issues from repos with developer-committed context files**
- **Context files do not generally improve task success rates**
- **Inference cost rises by >20% on average**
- Holds across different LLMs, different coding agents, and both LLM-generated and human-written context files
- **Decomposition of the effect: explicit instructions ARE followed; repository overviews — the most popular and provider-recommended section — are not helpful**
- Conclusion: context files earn their place for **non-standard coding practices**; anything beyond that must be measured before deployment

## Terminology note

"Lean AGENTS.md" is practitioner shorthand for the prescription this paper's evidence supports (keep the instructions, drop the repository overview). It is not the paper's own phrase.
