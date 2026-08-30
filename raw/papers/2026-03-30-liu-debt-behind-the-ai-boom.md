# Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild

**Authors:** Yue Liu, Ratnadira Widyasari, Yanjie Zhao, Ivana Clairine Irsan, Junkai Chen, David Lo
**arXiv:** 2603.28592 (v1 30 Mar 2026; v2 26 Apr 2026)
**URL:** https://arxiv.org/abs/2603.28592
**Captured:** 2026-08-30 (WebFetch of the arXiv abstract page)
**fulltext_source:** abstract-only — abstract verbatim below.

---

## Abstract (verbatim)

> AI coding assistants are now widely used in software development. Software developers increasingly integrate AI-generated code into their codebases to improve productivity. Prior studies have shown that AI-generated code may contain code quality issues under controlled settings. However, we still know little about the real-world impact of AI-generated code on software quality and maintenance after it is introduced into production repositories. In other words, it remains unclear whether such issues are quickly fixed or persist and accumulate over time as technical debt. In this paper, we conduct a large-scale empirical study on the technical debt introduced by AI coding assistants in the wild. To achieve that, we built a dataset of 302.6k verified AI-authored commits from 6,299 GitHub repositories, covering five widely used AI coding assistants. For each commit, we run static analysis before and after the change to precisely attribute which code smells, correctness issues, and security issues the AI introduced. We then track each introduced issue from the introducing commit to the latest repository revision to study its lifecycle. Our results show that we identified 484,366 distinct issues, and that code smells are by far the most common type, accounting for 89.3% of all issues. We also find that more than 15% of commits from every AI coding assistant introduce at least one issue, although the rates vary across tools. More importantly, 22.7% of tracked AI-introduced issues still survive at the latest version of the repository. These findings show that AI-generated code can introduce long-term maintenance costs into real software projects and highlight the need for stronger quality assurance in AI-assisted development.

## Key numbers

- **302.6k verified AI-authored commits** across **6,299 GitHub repositories**, five AI coding assistants
- Method: static analysis **before and after** each commit, to attribute issues precisely to the AI change; then track each issue to the latest revision
- **484,366 distinct issues** identified
- **89.3% are code smells** (maintainability), the rest correctness and security
- **>15% of commits from every assistant** introduce at least one issue (rates vary by tool)
- **22.7% of AI-introduced issues still survive at the latest repository version** — the debt is not being paid down
