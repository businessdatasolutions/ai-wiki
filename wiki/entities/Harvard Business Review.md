---
type: entity
kind: org
aliases: ["Harvard Business Review", "HBR"]
tags: [publisher, business-magazine, management-research, harvard]
parent: "[[Harvard Business School]]"
website: "https://hbr.org"
confidence: 0.85
last_confirmed: "2026-05-02"
source_count: 6
---

# Harvard Business Review

**Harvard Business Review** (HBR) is the management magazine published by Harvard Business Publishing, an affiliate of [[Harvard Business School]]. Founded 1922. Long-form articles aimed at executives and managers, blending academic research with practitioner perspectives.

A primary publishing venue for academic strategy and management work intended to reach C-suite readers.

## Role in the wiki

This wiki's two HBR ingests so far (Nov–Dec 2025 issue):

| Article | Authors | Reprint | Topic |
|---|---|---|---|
| [[2026-04-28-anand-wu-genai-playbook\|The Gen AI Playbook for Organizations]] | [[Bharat N. Anand]], [[Andy Wu]] | R2506K | Strategy: where to deploy GenAI today |
| [[2026-04-28-werner-lebrun-octopus-organization\|Become an Octopus Organization]] | [[Jana Werner]], [[Phil Le-Brun]] | R2506C | Change management: org adaptability |

HBR articles in the wiki use this convention: source `kind: article`, frontmatter includes `hbr_reprint`, body cites by HBR pagination.

## Article structure (recurring "Idea in Brief")

HBR articles open with a "Idea in Brief" panel: **The Problem / The Solution / The Payoff** (or variants like Problem / Why It Happens / The Solution). Useful when summarizing — the panel often distills the entire argument in 50–100 words.

## Cross-referenced HBR articles (not yet ingested)

The Anand-Wu article cites two earlier HBR pieces worth tracking:
- *"How Generative AI Can Augment Human Creativity"* (HBR Jul–Aug 2023) — relevant to [[generative-ai]] creative-catalyst quadrant.
- *"How Is Your Team Spending the Time Saved by Gen AI?"* (HBR Mar–Apr 2025) — relevant to [[enterprise-ai-adoption]] productivity-redeployment question.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "hbr")
SORT file.name ASC
```

## Open questions

- HBR's editorial process for AI-strategy articles (peer review? practitioner review?). Worth investigating once a third HBR source is ingested.
- Distinguishing HBR's flagship articles from HBR Press books and HBR.org "online" pieces — different rigor levels.
