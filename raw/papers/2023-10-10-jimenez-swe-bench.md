# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**Authors:** Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan (Princeton NLP / University of Chicago)
**arXiv:** 2310.06770 (v1 10 Oct 2023; v3 11 Nov 2024)
**URL:** https://arxiv.org/abs/2310.06770
**Venue:** ICLR 2024
**Captured:** 2026-08-30 (WebFetch of the arXiv abstract page)
**fulltext_source:** abstract-only — abstract verbatim below.

---

## Abstract (verbatim)

> Language models have outpaced our ability to evaluate them effectively, but for their future development it is essential to study the frontier of their capabilities. We find real-world software engineering to be a rich, sustainable, and challenging testbed for evaluating the next generation of language models. To this end, we introduce SWE-bench, an evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popular Python repositories. Given a codebase along with a description of an issue to be resolved, a language model is tasked with editing the codebase to address the issue. Resolving issues in SWE-bench frequently requires understanding and coordinating changes across multiple functions, classes, and even files simultaneously, calling for models to interact with execution environments, process extremely long contexts and perform complex reasoning that goes far beyond traditional code generation tasks. Our evaluations show that both state-of-the-art proprietary models and our fine-tuned model SWE-Llama can resolve only the simplest issues. The best-performing model, Claude 2, is able to solve a mere 1.96% of the issues. Advances on SWE-bench represent steps towards LMs that are more practical, intelligent, and autonomous.

## Key numbers

- **2,294 problems** from real GitHub issues + their pull requests, across **12 popular Python repositories**
- Task: given a codebase and an issue description, edit the codebase to resolve it; graded by the repository's own tests
- **Best model at publication (Claude 2): 1.96% resolved**
- Later derivatives that matter downstream: **SWE-bench Verified** (human-validated subset) and **SWE-bench Pro**

## Why it is here

Pre-2025 and foundational: SWE-bench is the measuring instrument that the 2025–2026 reward-hacking and benchmark-contamination literature is arguing about. Its design — resolve a real issue in a real repo whose *real fix already exists in public git history* — is precisely the property Cursor's 2026 analysis shows agents exploiting.
