# Effective Strategies for Asynchronous Software Engineering Agents

**Authors:** Jiayi Geng, Graham Neubig
**arXiv:** 2603.21489 (v1 23 Mar 2026; v2 8 Jul 2026)
**URL:** https://arxiv.org/abs/2603.21489
**Code:** https://github.com/JiayiGeng/CAID
**Captured:** 2026-08-30 (WebFetch of the arXiv abstract page)
**fulltext_source:** abstract-only — abstract verbatim below.

---

## Abstract (verbatim)

> AI agents have become increasingly capable at isolated software engineering (SWE) tasks such as resolving issues on Github. Yet long-horizon tasks involving multiple interdependent subtasks still pose challenges both with respect to accuracy, and with respect to timely completion. A natural approach to solving these long-horizon tasks in a timely manner is asynchronous multi-agent collaboration, where multiple agents work on different parts of the task at the same time. But effective application of multi-agent systems has proven surprisingly difficult: concurrent edits by multiple agents interfere with each other, dependencies are difficult to synchronize, and combining partial progress into a coherent whole is challenging. On the other hand, human developers have long relied on mature collaboration infrastructure to manage these challenges in large software projects. Inspired by these collaboration primitives, we introduce Centralized Asynchronous Isolated Delegation (CAID), a structured multi-agent coordination paradigm grounded in three core SWE primitives: centralized task delegation, asynchronous execution, and isolated workspaces. CAID constructs dependency-aware task plans through a central manager, executes subtasks concurrently in isolated workspaces, and consolidates progress via structured integration with executable test-based verification. In empirical evaluation, we find that CAID improves accuracy over single-agent baselines by 25.6% absolute on paper reproduction tasks (PaperBench) and 14.7% on Python library development tasks (Commit0).

## Key numbers

- **CAID = Centralized Asynchronous Isolated Delegation**, built on three SWE primitives: centralized task delegation, asynchronous execution, isolated workspaces
- **+25.6% absolute** over single-agent baselines on PaperBench (paper reproduction)
- **+14.7% absolute** on Commit0 (Python library development)
- Integration is verified by executable tests, not by a judge model

## Correction note

Frequently cited (including in the request that triggered this ingest) as "+26.7% / +14.3%". The abstract as published states **25.6% and 14.7%**.
