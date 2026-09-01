---
type: concept
title: AI-generated code quality and security
aliases: ["AI-generated code quality", "AI code security", "slopsquatting", "package hallucination", "AI technical debt", "AI-introduced defects"]
confidence: 0.85
last_confirmed: "2026-08-30"
source_count: 5
accessed_at: "2026-09-01"
tags: [code-quality, security, owasp, slopsquatting, package-hallucination, technical-debt, code-smells, supply-chain, static-analysis, flat-scaling]
relationships:
  - type: part-of
    target: agentic-engineering
  - type: depends-on
    target: attack-surface-management
  - type: caused
    target: agentic-pull-requests
  - type: contradicts
    target: ai-coding-productivity-evidence
    via: "productivity studies measure completed tasks and delivery throughput; this concept measures what those completions leave behind. Neither refutes the other, but a productivity figure computed on task completion alone is incomplete by the amount of defect and debt that survives review"
    confidence: 0.75
quality_score: 1
---

# AI-generated code quality and security

What AI-written code is actually like once it exists — measured under test conditions and traced in production repositories. The corpus supports three claims here, and the third is the one that changes planning.

## 1. A large fraction is insecure, and it is not evenly distributed

[[2025-07-30-veracode-2025-genai-code-security-report]]: **100+ models**, **80 coding tasks**, four languages, each task designed so a secure and an insecure completion are both plausible. **45% of samples introduced OWASP Top 10 vulnerabilities.**

| Language | Failure rate |
| --- | ---: |
| **Java** | **72%** |
| C# | 45% |
| JavaScript | 43% |
| Python | 38% |

Nearly a two-fold spread within the same models on the same tasks — most plausibly training-corpus composition, since decades of public Java predate modern secure-coding norms. **The risk an agent carries depends on which language it is writing**, which is a variable almost no AI policy accounts for. By flaw class, **XSS (CWE-80) fails in 86% of relevant samples**; models do materially better on SQL injection and weak cryptography — the classes with the longest history of tooling and education, i.e. the ones where the public corpus was already cleaned up.

## 2. Hallucinated dependencies are a supply-chain attack surface

[[2025-06-12-spracklen-package-hallucinations-code-generating-llms]]: **16 models**, Python and JavaScript, **2.23 million code samples** in the USENIX camera-ready, of which **440,445 (19.7%)** contained at least one hallucinated package — **205,474 unique fictional package names**. Rates: **≥5.2% commercial models, 21.7% open-source.**

The mechanism is what matters. A one-off invented import is a harmless error. **The same model inventing the same name repeatedly** turns a random error into a predictable one — and a predictable name is one an attacker can register in advance. The authors call it *"a novel form of package confusion attack"*; the security community's name is **slopsquatting**, by analogy with typosquatting, except the developer never made a typo. 205,474 names is the size of the attack surface, and it is freely derivable by anyone who can run the same models.

Mitigations work: the authors show hallucination-reduction strategies that preserve code quality. The operational answer is available today and unglamorous — **verify every dependency an agent adds against the registry before it merges.**

## 3. The defects persist — this is debt, not error

[[2026-03-30-liu-debt-behind-the-ai-boom]] traces what happens after the code lands. **302.6k verified AI-authored commits** across **6,299 repositories**, five assistants, with static analysis run **before and after each change** to attribute issues precisely, then each issue tracked to the latest revision:

- **484,366 distinct issues** introduced
- **89.3% are code smells** (maintainability)
- **>15% of commits from every assistant** introduce at least one issue
- **22.7% of AI-introduced issues are still present at the latest revision**

**One in five defects is never fixed.** The 89.3% smell share cuts both ways: reassuring that most of it is maintainability rather than security, unreassuring because maintainability debt has **no forcing function** — nothing breaks, no test fails, no incident fires. That is the most plausible explanation for the survival rate, and it means the debt concentrates in the category least likely to be paid down voluntarily.

## The finding that governs planning

**Security is not on the capability curve.** Veracode's models spanned varying sizes, release dates and training sources over several years, and performance was **"flat, regardless of model size or training sophistication."** Newer and larger models were *"no better."* Spracklen et al. point the same way: the four-fold hallucination gap is between model **classes** (commercial vs open-source), not along a capability gradient.

Every other measure in this corpus improves with model generation — SWE-bench resolution ran from **1.96%** in [[2023-10-10-jimenez-swe-bench-real-world-github-issues|2023]] to **87.1%** in [[2026-06-25-jain-cursor-reward-hacking-swamping-model-intelligence-gains|2026]]. Security does not move. There is no version of *"wait for the next model"* that resolves this, because scaling optimises for benchmarks that do not price a vulnerability.

**The consequence: security and quality review are a permanent cost of agentic development, not a transitional one.** That is [[2025-09-23-dora-2025-state-of-ai-assisted-software-development|DORA's]] "fortify your safety nets" capability, [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Merge Mommy's]] *data security* dimension, and the reason [[2026-04-13-branco-lgtm-auto-merged-llm-agentic-prs|mature repositories decline auto-merge policies]].

## Related concepts

[[concepts/attack-surface-management|attack-surface-management]], [[concepts/agentic-pull-requests|agentic-pull-requests]], [[concepts/agentic-engineering|agentic-engineering]], [[concepts/ai-coding-productivity-evidence|ai-coding-productivity-evidence]], [[concepts/responsible-ai|responsible-ai]], [[concepts/foundation-models|foundation-models]], [[concepts/vibe-coding|vibe-coding]].

## Debates and supersession

- **Vendor interest.** [[2025-07-30-veracode-2025-genai-code-security-report|Veracode]] sells application security testing, and "AI writes insecure code and always will" is good for that business. The flat-scaling finding is corroborated in shape by [[2025-06-12-spracklen-package-hallucinations-code-generating-llms|independent academic work]], which is the main reason to take it seriously. **Open:** an independent replication of the 45% figure.
- **Static analysis defines the defect.** The 484,366 figure is "issues a static analyser flags" — over-counting style, under-counting logic. And "verified AI-authored" depends on commit attribution, missing AI-assisted code committed under a human's name.
- **Model vintages are 2024–early 2025** across all three studies. The mechanisms should hold; the specific rates will have moved and nobody has re-measured. **Open.**
- **No source here reports a human baseline.** 45% insecure and 22.7% unfixed are alarming, but the corpus contains no comparable measurement of human-authored code under the same instruments. **This is the single largest interpretive gap in the concept.**
