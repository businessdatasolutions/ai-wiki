---
type: entity
kind: org
aliases: ["Amazon Web Services", "AWS"]
tags: [tech-vendor, cloud, ai-infrastructure, hyperscaler]
parent: "[[Amazon]]"
ticker: "AMZN (Amazon)"
website: "https://aws.amazon.com"
---

# Amazon Web Services

**Amazon Web Services** (AWS) is the cloud-computing subsidiary of Amazon. Launched 2006. The dominant public-cloud provider by revenue alongside Microsoft Azure and Google Cloud — a major hyperscaler hosting much of the world's enterprise AI workload.

## Role in the wiki

Two distinct angles on AWS surface across the ingested sources:

### 1. As an AI infrastructure provider

[[2026-04-28-ai-index-report-2025|AI Index 2025]] §4.1 timeline: Anthropic's partnership with AWS expanded by an additional **$4 billion investment from Amazon** in November 2024, bringing the total to **$8 billion**. Significant signal of AWS's commitment to frontier model partnerships.

### 2. As a thought-leadership platform

AWS runs an "Executives in Residence" program advising Fortune 500 leadership teams. [[Jana Werner]] and [[Phil Le-Brun]] (authors of [[2026-04-28-werner-lebrun-octopus-organization|"Become an Octopus Organization"]] in HBR Nov–Dec 2025) hold these positions. The Octopus framework is implicitly AWS-aligned: customer-centricity, distributed systems, microservices, decoupling — all align with AWS's core selling points (cloud microservices, serverless, decoupled architectures).

Discount the Octopus framing slightly for AWS's commercial interest, but the underlying argument is well-supported by examples external to AWS (Netflix, Google, Coca-Cola, U.S. Army).

## Notable people (mentioned in this wiki)

- [[Jana Werner]] — Executive in Residence, AWS; co-author of the Octopus Org book and HBR article.
- [[Phil Le-Brun]] — Executive in Residence, AWS; co-author of the Octopus Org book and HBR article.

## AWS's positioning vs. competitors (note for future ingests)

In the AI infrastructure layer:
- **AWS** — cloud + Anthropic partnership ($8B); SageMaker; Bedrock for foundation-model access
- **Microsoft Azure** — OpenAI partnership; Copilot integration
- **Google Cloud** — Gemini family; deep ML expertise via Google DeepMind

The wiki's [[foundation-models]] page lists notable models from each parent company. The AWS-Anthropic partnership likely deepens further; future ingests should track.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "aws")
SORT file.name ASC
```

## Open questions

- AWS's strategic AI roadmap beyond the Anthropic partnership — Bedrock model selection, Q business agent, Trainium/Inferentia silicon.
- The AWS Executives in Residence program — how many residents, how selected, what outputs.
- Conflict-of-interest framing: how to evaluate AWS-affiliated authors writing about org design / customer-centricity / distributed systems.
