---
type: entity
kind: organization
aliases: ["Veracode"]
tags: [veracode, application-security, owasp, static-analysis, genai-code-security, vendor-research, jens-wessling]
affiliation: "Application security vendor"
role: "Application security testing company; publisher of the annual GenAI Code Security Report"
confidence: 0.7
last_confirmed: "2026-08-30"
accessed_at: "2026-08-30"
source_count: 1
---

# Veracode

An **application security testing vendor**, present in this wiki as the publisher of the **2025 GenAI Code Security Report** — the largest systematic scan of AI-generated code security in the corpus.

The study asked **over 100 large language models**, spanning several years of sizes and vintages, to complete **80 curated coding tasks** in Java, Python, C# and JavaScript, each designed so that a secure and an insecure completion were both plausible. **45% of samples introduced OWASP Top 10 vulnerabilities**, with a near two-fold spread by language (**Java 72%**, Python 38%) and **XSS failing in 86% of relevant samples**.

Its most consequential finding is the negative one: **security performance was "flat, regardless of model size or training sophistication."** Newer and larger models were *"no better."* This is the corpus's primary evidence that **security is not on the capability curve** — the one dimension that has not improved as SWE-bench resolution ran from 1.96% to 87%.

Veracode sells the remediation for the problem it measures, which is a real interest to hold in view. The flat-scaling result is corroborated in shape by independent academic work ([[2025-06-12-spracklen-package-hallucinations-code-generating-llms|Spracklen et al.]]), which is why it is treated as credible here. The announcement was authored by **Jens Wessling**, Veracode's CTO.

## Appears in this wiki via

- [[2025-07-30-veracode-2025-genai-code-security-report]]

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "veracode")
SORT file.name ASC
```
