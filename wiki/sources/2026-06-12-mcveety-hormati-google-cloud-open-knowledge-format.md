---
type: source
kind: article
title: "How the Open Knowledge Format can improve data sharing"
author: ["Sam McVeety", "Amir Hormati"]
publisher: "Google Cloud (Data Cloud / Data Analytics Blog)"
url: "https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing"
date_published: 2026-06-12
date_ingested: 2026-06-18
zotero_item_key: XRZZ9MTA
length: "~2,000 words (full blog post; Zotero-extracted text, verified against the live URL framing)"
raw: "../../raw/articles/how-the-open-knowledge-format-can-improve-data-sharing.md"
tags: [open-knowledge-format, okf, llm-wiki, google-cloud, bigquery, knowledge-catalog, knowledge-as-infrastructure, markdown-frontmatter, agent-context, interoperability, open-standard, metadata-as-code, karpathy-llm-wiki, vendor-format-as-standard]
dynamic_capabilities:
  - contextual/internal-enablers
relationships:
  - type: instance-of
    target: llm-wiki
    via: "OKF v0.1 is the first major-vendor formalization of the LLM Wiki pattern into a portable open spec — directory of markdown files + YAML frontmatter, one concept per file, file-path-as-identity, optional index.md / log.md; it explicitly cites Karpathy's LLM Wiki gist as antecedent"
  - type: supports
    target: 2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained
    via: "OKF standardizes the same three-layer markdown-wiki pattern Raju explains (raw / wiki / schema becomes producer / bundle / consumer); the conventions Raju describes informally (frontmatter, cross-links, index.md, log.md) are exactly what OKF v0.1 makes into an interoperability contract"
  - type: supports
    target: 2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers
    via: "Liu predicted convergence and named enterprise LLM-wiki implementation (semantic graph + RBAC) as the missing piece; OKF is a concrete step toward that interoperability layer — a format (not a service) that lets wikis written by one producer be consumed by any agent"
  - type: published-by
    target: Google
    via: "Google Cloud Data Cloud / Data Analytics Blog; Google Cloud's Knowledge Catalog updated to ingest OKF and serve it to its agents"
---

# How the Open Knowledge Format can improve data sharing

The **first major-vendor formalization of the [[llm-wiki|LLM Wiki]] pattern into an open specification.** Published on the **[[Google]] Cloud Data Analytics blog**, 12 June 2026, by **Sam McVeety** (Tech Lead, Data Analytics) and **Amir Hormati** (Tech Lead, BigQuery). The post introduces the **Open Knowledge Format (OKF) v0.1** — *"an open specification that formalizes the LLM-wiki pattern into a portable, interoperable format ... a vendor-neutral, agent- and human-friendly standard for representing the metadata, context, and curated knowledge that modern AI systems need."*

## TL;DR

- **OKF v0.1 is a format, not a platform or service.** A bundle is *"just markdown"* (renderable on GitHub, indexable by any tool), *"just files"* (a tarball / git repo / filesystem mount), and *"just YAML frontmatter"* for the small set of queryable structured fields: `type`, `title`, `description`, `resource`, `tags`, `timestamp`.
- **The structure is the LLM-Wiki three-layer pattern made interoperable.** A bundle is a directory of markdown files representing *concepts* (tables, datasets, metrics, playbooks, runbooks, APIs — anything you want to capture). **Each concept is one file; the file path is the concept's identity.** Concepts link to one another with normal markdown links, *"turning the directory into a graph of relationships."* Bundles may include `index.md` (progressive disclosure as agents navigate) and `log.md` (chronological change history) — the same two catalogue files this repository maintains.
- **The only required field is `type`.** Everything else (what types exist, what other fields a concept carries, what sections the body has) is left to the producer. *"The spec defines the interoperability surface, not the content model."*
- **It explicitly descends from Karpathy's LLM Wiki gist** (quoted: *"LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass"*), and names the pattern's recurring instances: *"Obsidian vaults wired to coding agents, the AGENTS.md / CLAUDE.md family of convention files, repos full of index.md and log.md artifacts that agents consult before doing real work, and 'metadata as code' repositories inside data teams."*
- **The problem it solves is fragmented enterprise context.** Internal knowledge — *"the schema of a table, your business' meaning of a metric, the runbook for an incident, the join paths between two systems"* — lives scattered across metadata catalogs, wikis, shared drives, code comments, and *"the heads of a few senior engineers."* Every agent builder re-solves the same context-assembly problem from scratch; OKF is meant to make that knowledge portable across products and organizations.

## The three design principles

1. **Minimally opinionated.** OKF requires exactly one thing of every concept — a `type` field. *"The spec defines the interoperability surface, not the content model."*
2. **Producer/consumer independence.** A human-authored bundle can be consumed by an AI agent; a metadata-export-pipeline bundle can be browsed in a visualizer; an LLM-synthesized bundle can be queried by another LLM. *"The format is the contract; the tooling at each end is independently swappable."*
3. **Format, not platform.** Not tied to any cloud, database, model provider, or agent framework; *"will never require a proprietary account or SDK to read, write, or serve."* Published as an open standard because *"the value of a knowledge format comes from how many parties speak it, not from who owns it."*

## What ships with the spec

OKF is published with reference implementations at both ends, *"deliberately"* proofs of concept:

- **An enrichment agent** that walks a BigQuery dataset, drafts an OKF concept document for every table and view, then runs a second LLM pass that *"crawls authoritative documentation and enriches each concept with citations, schemas, and join paths."* (A two-pass produce-then-enrich loop structurally similar to this wiki's Acquire → Process split.)
- **A static HTML visualizer** that turns any OKF bundle into an interactive graph view in a single self-contained file — *"no backend, no install on the viewing side, no data leaves the page."*
- **Three ready-to-browse sample bundles**: GA4 e-commerce, Stack Overflow, and Bitcoin public datasets.
- Google Cloud's own **Knowledge Catalog** was updated to ingest OKF and serve it to its agents. The repo, spec, and samples are on GitHub; the v0.1 spec *"fits on a single page."*

## What was actually ingested

Full blog post, acquired via the [zotero-acquire](../../CLAUDE.md) channel (Zotero key `XRZZ9MTA`, collection `ai-wiki`). Zotero typed the item `webpage` with no PDF attachment, so the body is **Zotero-extracted text** (`fulltext_source: zotero-extracted`) — complete and clean here (the extraction captured the full article through the footer). The `date_published` was blank in the Zotero stub and recovered from the post body (*"June 12, 2026"*). No spec document or GitHub repo was ingested — only the announcement blog post; the v0.1 spec itself, the reference-implementation code, and the sample bundles are open follow-up targets.

## Why this matters to the wiki

This is the wiki's **most directly self-referential source.** This repository *is* an LLM Wiki built on exactly the conventions OKF v0.1 standardizes:

- **`type:` frontmatter** on every page (`type: source | entity | concept | thread | synthesis`) — OKF's single required field.
- **`index.md` and `log.md`** as the catalogue + history files — OKF's two named optional files, by the same names.
- **Concept-per-file with markdown cross-links** forming a relationship graph — OKF's core structure (this wiki adds a *typed* layer on top via `relationships:`, which OKF's minimally-opinionated stance permits as producer-specific extension).
- **`tags`, `title`, `description`/`timestamp`-style fields** — OKF's reserved queryable set.

So OKF is the **interoperability-standard vantage** on the [[llm-wiki|LLM Wiki]] concept — the eighth wiki source on the pattern and the first that asks *"how do wikis written by different producers get consumed by different agents without translation?"* It is a partial answer to the concept page's standing open question on **enterprise-scale LLM-Wiki implementations**, arriving from the largest-cloud-vendor vantage. Where [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase]] shipped a *vendor implementation* (a database that serves a wiki) and [[2026-04-18-mysore-medium-wikizz-extending-karpathy-llm-wiki|Mysore's WikiZZ]] a *single-author UI extension*, OKF ships a *format* — the layer that would let any of those implementations interoperate.

The contribution is also a clean parallel to a precedent already on the [[Google]] entity page: Google Brain's **Bfloat16** is the wiki's *"vendor-built-data-format-becomes-industry-standard"* example. OKF is Google attempting the same move one layer up — a **vendor-built knowledge-format proposed as an open standard.** Whether it earns standard status (OKF's own framing: *"a knowledge format earns its name"* only through multi-party adoption) is the open question.

## Dynamic-capabilities reading

- **contextual/internal-enablers** — OKF is pitched as an *internal enabler* for agentic systems: a standardized knowledge substrate that removes the fragmented-context barrier (*"foundation models ... still need the right information to produce accurate and actionable results"*). It is infrastructure that lets an organisation's internal knowledge become legible to agents, rather than a sensing/seizing/transforming capability in its own right — hence the single contextual tag rather than a fuller W&W trace (the source is a format spec, and per the skip-rather-than-stretch rule the other buckets would be forced).

## Cross-source positioning (descriptive, per cross-source neutrality)

OKF sits at the intersection of two wiki clusters:

- **The LLM-Wiki-pattern cluster** — [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju (explainer)]], [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu (RAG/Wiki/GBrain)]], [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase (vendor impl)]], [[2026-04-18-mysore-medium-wikizz-extending-karpathy-llm-wiki|Mysore (WikiZZ)]], [[2026-04-11-nodus-labs-fix-karpathys-llm-wiki-knowledge-graph-infranodus|Nodus Labs (KG augmentation)]], and the upstream [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy]]. OKF is the standardization vantage none of them supplied.
- **The knowledge-as-production-infrastructure theme** — [[2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook|Koomen / YC]] (*"Karpathy-style knowledge LLM wikis"*; shared tool/skill registries) and [[2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era|Moon / McKinsey]] (*"knowledge becomes production infrastructure ... a durable source of competitive advantage"*) both argue knowledge-as-infrastructure at the org level; OKF is the *file-format substrate* underneath that argument. (Mentioned, not typed-edged — OKF doesn't engage these sources directly.)

## Linked entities and concepts

- Publisher: [[Google]] (Google Cloud Data Cloud team). The Knowledge-Catalog OKF-ingestion update is a Google Cloud product change.
- Home concept: [[llm-wiki]] — OKF is an `instance-of` the pattern (the enterprise/standardization instance).
- Related concepts touched: [[agent-harness]] (OKF bundles are a persistent-context substrate a harness reads), [[knowledge-graphs]] (markdown-cross-links-as-graph), [[enterprise-ai-adoption]] (the fragmented-context problem is an enterprise-adoption barrier).
- **Dangling** (single-source mention, deferred per the author-entity-promotion rule): **Sam McVeety** (Tech Lead, Data Analytics, Google Cloud), **Amir Hormati** (Tech Lead, BigQuery, Google Cloud). Promote on a second-source mention.

## Open questions raised

- **The OKF v0.1 spec itself** — the single-page specification (conformance criteria, cross-linking rules, reserved filenames) is on GitHub but not ingested. Primary-source target; would let the wiki compare OKF's conformance surface against its own CLAUDE.md schema precisely.
- **Does OKF earn adoption beyond Google?** The format's value is multi-party adoption by its own framing. Track whether non-Google producers/consumers (catalog vendors, other clouds, agent frameworks) implement it.
- **OKF vs this repo's typed `relationships:` layer** — OKF is minimally opinionated (only `type` required); this wiki adds typed edges, lifecycle fields (`confidence`, `last_confirmed`), and quality scores. Are those producer-specific extensions OKF can carry, or do they exceed the interoperability surface? Worth resolving against the actual spec.
- **The enrichment-agent two-pass loop vs this wiki's Acquire → Process split** — structurally similar; a comparison could inform this repo's own tooling.
