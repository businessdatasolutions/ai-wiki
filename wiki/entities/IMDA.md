---
type: entity
kind: organization
aliases: ["IMDA", "Infocomm Media Development Authority", "Infocomm Media Development Authority of Singapore"]
tags: [imda, singapore, mddi, ai-governance, agentic-ai, model-framework, regulation, davos, risk-bounding, human-accountability]
affiliation: "Government of Singapore — Ministry of Digital Development and Information (MDDI)"
role: "Singapore's infocomm and media regulator; publisher of the Model AI Governance Framework series"
confidence: 0.7
last_confirmed: "2026-08-30"
accessed_at: "2026-08-30"
source_count: 1
---

# IMDA

Singapore's **Infocomm Media Development Authority**, operating under the Ministry of Digital Development and Information (MDDI). IMDA's significance to this wiki is its **Model AI Governance Framework** series — voluntary reference frameworks published early enough to shape how other jurisdictions' rules get written, a strategy Singapore has run since the original 2019 framework.

The **Model AI Governance Framework for Agentic AI**, announced at Davos on **22 January 2026** and updated **20 May 2026**, is presented as the world's first governance framework aimed specifically at systems that *take actions* rather than produce outputs. Its four pillars:

1. **Bound the risks upfront** — select appropriate agentic use cases and place limits on agents' powers
2. **Make humans meaningfully accountable** — define significant checkpoints at which human approval is required
3. **Implement technical controls across the agent lifecycle** — baseline testing, access controlled to whitelisted services
4. **Enable end-user responsibility** — through transparency and education/training

The structurally interesting move is pillar 1's **ex ante** posture: risk is bounded at use-case selection, before deployment, rather than detected through output testing afterwards. That is the right shape for systems whose failures are actions, and it is a different regime from the disclosure-and-testing frameworks that dominate non-agentic AI governance.

What makes it worth reading alongside the engineering literature is the **independent convergence**: nothing in the practitioner or academic material in this corpus cites the framework, yet [[concepts/agent-oversight-and-delegation|the same control set]] — bounded powers, approval checkpoints, least privilege, auditability — appears in a solo founder's production setup, a product executive's review bot, and a human-factors study of delegation regret.

## Appears in this wiki via

- [[2026-01-22-imda-model-ai-governance-framework-for-agentic-ai]]

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "imda")
SORT file.name ASC
```
