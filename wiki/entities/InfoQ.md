---
type: entity
kind: venue
aliases: ["InfoQ", "InfoQ.com"]
tags: [infoq, qcon, conference, software-engineering-media, agent-harness, venue]
confidence: 0.75
last_confirmed: "2026-06-26"
accessed_at: "2026-06-26"
source_count: 2
---

# InfoQ

A **software-engineering news site and practitioner community** (run by C4Media) that publishes technical articles, news, and conference talks for senior developers and architects, and organises the **QCon** international conference series and the **InfoQ Dev Summit**. In this wiki it surfaces as the **publishing venue / channel** for recorded conference talks on agent engineering — the `author:` attribution on video source pages whose presenters speak under the InfoQ/QCon banner.

## Why InfoQ matters in this wiki

InfoQ is the **venue through which two of the wiki's [[agent-harness]] practitioner talks reached the corpus** — promoted to an entity on its second source mention per the [§Author-entity promotion](../../CLAUDE.md#author-entity-promotion) rule (the `author = channel` convention for videos means InfoQ is the recurring author):

- **[[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler — "The Engineering of AI Agents" (QCon London 2026)]]** — [[Thoughtworks]]' Birgitta Böckeler propagating the *harness engineering* term to the broader engineering audience; published to the InfoQ YouTube channel.
- **[[2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail|"From Demo to Production: Why Agentic AI Systems Fail"]]** — an unnamed practitioner's four-production-failure-patterns war-story on an agentic app-generation platform; an InfoQ conference talk.

Both are **practitioner-conference** sources rather than vendor announcements or academic papers — InfoQ's editorial niche (senior-engineer-facing, implementation-focused, vendor-neutral) is why its talks tend to land in the wiki's [[agent-harness]] and [[agentic-engineering]] clusters as independent, outside-the-vendor-cluster vantages.

## Sources published via InfoQ

- [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy]] — QCon London 2026 keynote-style talk.
- [[2026-06-24-from-demo-to-production-why-agentic-ai-systems-fail]] — production failure-patterns talk.

## Open questions

- **InfoQ vs. QCon attribution.** The wiki currently attributes both talks to `author: ["InfoQ"]` (the YouTube channel). If a future source distinguishes a QCon-stage talk from InfoQ-original editorial content, the attribution convention may need a `series:`-style refinement.
