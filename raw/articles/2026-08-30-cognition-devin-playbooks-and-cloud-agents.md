# Devin (Cognition) — playbooks and cloud-agent model

**Vendor:** Cognition
**Docs:** https://docs.devin.ai/ (playbooks: https://docs.devin.ai/product-guides/using-playbooks and .../creating-playbooks)
**Captured:** 2026-08-30 (WebFetch of the Devin docs, supplemented by web search; `docs.devin.ai/product-guides/playbooks` 404s — the live paths are `using-playbooks` and `creating-playbooks`)
**fulltext_source:** web-extract, partial — vendor documentation, fetched shallowly. **Re-resolve deep links at build time; Cognition reorganises these docs.**

---

## Why this file exists

Devin is the substrate under most of the practitioner material in this ingest (Carson's 15 concurrent agents, the Watchdog playbook, the Land PR skill, Devin Review). This is a thin vendor reference so those claims have something to point at — not a full documentation ingest.

## The cloud-agent model

Devin runs **in the cloud with a fresh VM per session**, not on the developer's machine. That is the property practitioners cite as load-bearing: isolated workspaces mean concurrent agents don't collide in a shared working tree, which is what makes running 10–15 sessions in parallel possible at all. (This is the same primitive that Geng & Neubig's CAID paper isolates as "isolated workspaces" and validates experimentally.)

## Playbooks

A **playbook** is a reusable, shareable prompt that steers Devin through a repeated multi-step workflow with a defined procedure and success criteria — effectively a custom system prompt for a recurring task.

**Sections a playbook can carry** (from Cognition's guidance and community write-ups): **Procedure**, **Specifications**, **Advice**, **Forbidden Actions**, **Required from User**. The Procedure covers the whole task scope — at minimum setup, the task itself, and delivery. Specifications state **postconditions**: what should be true after Devin is done.

**Invocation:** select from the Team or Community library (a blue pill confirms attachment); attach a `<filename>.devin.md` file when starting a session; or type an assigned **macro** (e.g. `!data-tutorial`) in the prompt box. Playbooks are also creatable via API (`body`, `title`, `macro`).

**When Cognition recommends them:** for recurring or standardised tasks, and iteratively — running a playbook surfaces "opportunities to improve the instructions" so it completes more reliably next time.

## Devin Review

A first-party PR review product inside Devin, distinct from the coding session. Carson's "Land PR" playbook triggers it and allows up to two review loops before recording a narrated video walkthrough of the change.

## Verification note

The **Forbidden Actions / Required from User** section names come from Cognition's guidance as relayed through community documentation, not from a verbatim read of the current docs page — the fetched `using-playbooks` page did not enumerate section names. Verify before quoting as official structure.
