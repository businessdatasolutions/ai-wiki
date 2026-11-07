---
type: entity
kind: org
aliases: ["Cisco", "Cisco Systems"]
tags: [tech-vendor, networking, ai-infrastructure, ai-security, enterprise-tech]
ticker: "CSCO"
website: "https://www.cisco.com"
confidence: 0.8
last_confirmed: "2026-11-07"
accessed_at: "2026-11-07"
source_count: 3
---

# Cisco

**Cisco Systems** (NASDAQ: CSCO) is a global enterprise technology company. Historically the dominant networking-equipment vendor; now positioning itself as a leader in **AI infrastructure, AI security, and enterprise AI deployment**. Founded 1984.

## Role in the wiki

- **Sponsor of [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MIT Technology Review Insights' "Building the AI-enabled enterprise of the future"]]** (2025).
- Source of the framing: **5 foundations** for AI-readiness — Strategy / Infrastructure / Data / Governance / Culture and Talent. See [[syntheses/organizational-frameworks-for-ai-adoption|organizational-frameworks-for-ai-adoption]].
- Source of the **chatbot → agent → multi-agent system** progression frequently cited in [[ai-agents]].
- Source of the **AI-readiness gap** stat: only 13% of organizations globally are ready to leverage AI to its full potential (per Cisco's 2025 data).

## Notable people (mentioned in this wiki)

- **Jeetu Patel** — President & Chief Product Officer (quoted on AI inflection point and on safety/security as adoption blockers).
- **Liz Centoni** — EVP & Chief Customer Experience Officer (quoted on agentic CX and "giving agency with human oversight").

## Strategic positioning (note for future ingests)

Cisco's commercial interest in this wiki's themes is direct:
- **Network/infrastructure** for AI workloads (datacenter networking, on-prem AI infrastructure)
- **AI security** (the AI security fundamentals sidebar in MITTRI/Cisco)
- **Splunk** (Cisco acquired Splunk in 2024; observability for AI workloads)

Discount Cisco-sourced framings on infrastructure and security accordingly. Other Cisco-attributed claims (e.g., the readiness/urgency stats) come from Cisco's own surveys and should be flagged as Cisco-instrument data when cited.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "cisco")
SORT file.name ASC
```

## Open questions

- Cisco's 2025 readiness survey methodology — sample size, geography, instrument design.
- The Splunk integration into Cisco's AI story — observability data is increasingly important for AI ops.
- Cisco's competitive positioning vs. NVIDIA / hyperscalers in the AI infrastructure stack.

## AI-maturity and health-care sources (added 2026-11-07)

- [[2024-11-19-cisco-ai-readiness-index-2024]] — the index behind the much-cited 13%: Pacesetters 14% (2023) and 13% (2024), 7,985 leaders in 30 markets; the Netherlands 7%.
- [[2025-10-14-cisco-ai-readiness-index-2025]] — the 2025 edition: Pacesetters "about 13% … for the last three years", now defined as outperforming peers on AI value. The full report was not read.
