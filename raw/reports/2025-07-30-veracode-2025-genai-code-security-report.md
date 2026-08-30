# 2025 GenAI Code Security Report

**Publisher:** Veracode
**Blog post title:** "We Asked 100+ AI Models to Write Code. Here's How Many Failed Security Tests."
**Author of the announcement:** Jens Wessling, Chief Technology Officer, Veracode
**Date:** 30 July 2025
**Blog URL:** https://www.veracode.com/blog/genai-code-security-report/
**Report PDF:** https://www.veracode.com/wp-content/uploads/2025_GenAI_Code_Security_Report_Final.pdf
**Captured:** 2026-08-30 (WebFetch of the announcement blog post)
**fulltext_source:** web-extract of the announcement — the full PDF report was not converted (no local PDF toolchain). Figures below are those stated in the announcement.

---

## Design

Over **100 large language models**, of varying sizes, release dates and training sources spanning several years, asked to complete **80 curated coding tasks** across **Java, Python, C# and JavaScript**, each task designed so that a secure and an insecure completion are both plausible. Output scanned for OWASP Top 10 classes of flaw.

## Headline

**45% of code samples failed security tests**, introducing OWASP Top 10 vulnerabilities.

## By language

| Language | Security failure rate |
| --- | ---: |
| Java | **72%** (worst by a wide margin) |
| C# | 45% |
| JavaScript | 43% |
| Python | 38% |

## By vulnerability class

- **Cross-site scripting (CWE-80): models failed to defend in 86% of relevant samples**
- Log injection: **88%** failure (the figure carried in the request that prompted this ingest; the announcement page emphasises XSS)
- Other classes covered: SQL injection and weak cryptographic algorithms, where models performed materially better

## The finding that matters most

**Scaling did not help.** Newer and larger models were "no better" at generating secure code; performance was "flat, regardless of model size or training sophistication." Security is not on the curve that capability is on — it does not arrive as a free side-effect of the next model generation.
