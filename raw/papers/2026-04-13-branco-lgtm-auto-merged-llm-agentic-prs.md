# LGTM! Characteristics of Auto-Merged LLM-based Agentic PRs

**Authors:** Ruben Branco, Paulo Canelas, Catarina Gamboa, Alcides Fonseca
**Venue:** MSR 2026 Mining Challenge, 13–14 April 2026, Rio de Janeiro, Brazil
**Programme page:** https://2026.msrconf.org/details/msr-2026-mining-challenge/61/
**Preprint:** https://pcanelas.com/assets/papers/2026-msr-lgtm.pdf
**DOI:** https://doi.org/10.1145/3793302.3793621
**Artifact:** https://doi.org/10.5281/zenodo.18341679
**Captured:** 2026-08-30 (WebFetch of the MSR 2026 programme page)
**fulltext_source:** abstract + programme-page findings — the preprint PDF itself was not converted.

---

## Framing (quoted from the abstract)

> AI tools are generating code faster than humans can properly review it, leading repositories to skip review and auto-merge agentic PRs directly.

Built on the **AIDev** dataset (Li, Zhang & Hassan 2026); compares auto-merged agentic PRs against human-authored PRs and against reviewed agentic PRs.

## Key findings

- **Auto-merged agentic PRs tend to be smaller and more focused** than the alternatives
- **Maintainers are cautious toward PRs that delete existing code**
- **Repositories tend to either auto-merge all agentic PRs or none** — the policy is repo-level, not PR-level. Auto-merge is a *governance posture*, not a per-change judgement
- **Mature repositories more frequently reject auto-merge policies**
- **OpenAI Codex and Claude Code receive the highest auto-merge rates** among the agentic tools studied
