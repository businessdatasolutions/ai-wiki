---
type: source
kind: report
title: "2025 GenAI Code Security Report"
author: ["Veracode"]
publisher: "Veracode; announcement authored by Jens Wessling, CTO"
url: "https://www.veracode.com/blog/genai-code-security-report/"
date_published: 2025-07-30
date_ingested: 2026-08-30
length: "announcement blog post only (~1,200 words); the full PDF report was not converted"
raw: "../../raw/reports/2025-07-30-veracode-2025-genai-code-security-report.md"
tags: [veracode, code-security, owasp-top-10, xss, log-injection, java, python, javascript, csharp, static-analysis, model-scaling, cwe-80, vendor-research]
dynamic_capabilities:
  - contextual/internal-barriers
  - digital-sensing/digital-scouting
relationships:
  - type: supports
    target: 2025-06-12-spracklen-package-hallucinations-code-generating-llms
    via: "two 2025 measurements of AI code security weeks apart, converging on the same structural finding: the defect class is systematic and does not shrink with model capability. Veracode's security performance is 'flat, regardless of model size or training sophistication'; Spracklen et al.'s hallucination rate varies four-fold by model *class* (5.2% commercial vs 21.7% open-source) rather than improving along the capability curve"
    confidence: 0.8
  - type: supports
    target: 2026-03-30-liu-debt-behind-the-ai-boom
    via: "controlled conditions and the wild, on the same defect population. Veracode measures what AI writes when asked (45% of samples introduce OWASP Top 10 flaws); Liu et al. measure what survives after it merges into production repositories, finding 22.7% of AI-introduced issues still present at the latest revision"
    confidence: 0.75
---

# Veracode — 2025 GenAI Code Security Report

## TL;DR

**Over 100 large language models**, of varying sizes, release dates and training sources, asked to complete **80 curated coding tasks** across **Java, Python, C# and JavaScript**, each designed so that a secure and an insecure completion are both plausible. Output scanned for OWASP Top 10 flaw classes.

**Headline: 45% of code samples failed security tests**, introducing OWASP Top 10 vulnerabilities.

**By language — the spread is the useful part:**

| Language | Security failure rate |
| --- | ---: |
| **Java** | **72%** |
| C# | 45% |
| JavaScript | 43% |
| Python | 38% |

**Java at 72% against Python at 38%** is nearly a two-fold difference within the same models on the same tasks. The most likely explanation is training-corpus composition — decades of public Java that predates modern secure-coding norms — which means **the risk you carry from an agent depends on which language it is writing**, a variable no one's AI policy accounts for.

**By vulnerability class:** cross-site scripting (CWE-80) is the worst, with models failing to defend in **86% of relevant samples**; log injection is reported at **88%**. Models do materially better on SQL injection and weak cryptographic algorithms — the classes with the longest history of tooling, linting and developer education. That pattern is itself informative: **models are safest exactly where the public corpus has already been cleaned up**, which is not a property that generalises to novel flaw classes.

**The finding that matters most, and the one to quote:**

> Newer and larger models were **"no better"** at generating secure code; performance was **"flat, regardless of model size or training sophistication."**

**Security is not on the capability curve.** Every other measure in this ingest improves with model generation — SWE-bench resolution from 1.96% to 87%, reasoning, tool use. Security does not. There is no version of "wait for the next model" that solves this, because scaling is optimising for benchmarks that do not price a vulnerability. The organisational consequence is that **security review is a permanent cost of agentic development, not a transitional one** — which is precisely the "fortify your safety nets" capability that [[2025-09-23-dora-2025-state-of-ai-assisted-software-development|DORA]] names, and precisely the *data security* dimension in [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Merge Mommy's]] risk score.

**What happens to these flaws afterwards** is measured by [[2026-03-30-liu-debt-behind-the-ai-boom|Liu et al.]]: across 302.6k AI-authored commits in the wild, **22.7% of AI-introduced issues are still present at the latest repository revision.** Veracode says the code arrives insecure; Liu et al. say it largely stays that way.

## Dynamic-capabilities reading

- **`contextual/internal-barriers`** — a 45% baseline flaw rate that does not improve with model choice is a standing barrier to autonomous merge, and it binds hardest in Java shops.
- **`digital-sensing/digital-scouting`** — a systematic scan across 100+ models is sensing infrastructure for a risk most adopters are not measuring themselves.

## Linked entities and concepts

- Entities: [[Veracode]]
- Concepts: [[concepts/ai-generated-code-quality|ai-generated-code-quality]], [[concepts/attack-surface-management|attack-surface-management]], [[concepts/responsible-ai|responsible-ai]], [[concepts/agentic-pull-requests|agentic-pull-requests]], [[concepts/foundation-models|foundation-models]]

## Scope and reliability

**The announcement blog post only** — the full PDF report was not converted (no local PDF toolchain), so the model list, per-model results, task construction and the CWE breakdown beyond XSS were **not read**. **Vendor research with a direct commercial interest**: Veracode sells application security testing, and "AI writes insecure code and always will" is straightforwardly good for that business. The scale (100+ models, 80 tasks) and the flat-scaling finding are consistent with the independent evidence in [[2025-06-12-spracklen-package-hallucinations-code-generating-llms|Spracklen et al.]], which is the main reason to take it seriously. The **88% log-injection figure** is carried from the ingest request and is **not** stated on the announcement page, which emphasises XSS at 86% — verify against the PDF before citing. Tasks are synthetic and single-file; they measure what a model writes when asked, not what survives a real review pipeline.
