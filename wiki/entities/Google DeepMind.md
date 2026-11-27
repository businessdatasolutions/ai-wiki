---
type: entity
kind: organization
aliases: ["Google DeepMind", "DeepMind", "GDM"]
tags: [google-deepmind, gdm, ai-lab, gemini, antigravity, omni, autoharness, foundation-models, agent-harness, world-models, demis-hassabis]
since: 2023
confidence: 0.80
last_confirmed: "2026-11-27"
accessed_at: "2026-11-27"
source_count: 11
relationships:
  - type: part-of
    target: Google
    via: "Google's consolidated AI research division (DeepMind + Google Brain merged 2023); 'the engine room of Google'"
  - type: employs
    target: Logan Kilpatrick
    via: "Kilpatrick leads Google AI Studio and the Gemini API at GDM"
  - type: published-by
    target: 2026-03-05-lou-deepmind-autoharness-code-harness-synthesis
    via: "AutoHarness authored by a Google DeepMind team (Lou, Lázaro-Gredilla, Murphy et al.)"
---

# Google DeepMind

Google's consolidated AI research division (the 2023 merger of DeepMind and Google Brain), described from the inside as **"the engine room of Google"** ([[2026-06-11-kilpatrick-sequoia-model-eats-the-harness|Kilpatrick 2026]]). It is part of [[Google]] and produces the Gemini model family, the [[Antigravity]] agent harness, and the [[Omni]] multimodal model.

## What the wiki holds on GDM

- **Harness synthesis research.** [[2026-03-05-lou-deepmind-autoharness-code-harness-synthesis|AutoHarness]] (Lou et al., March 2026) shows a small model (Gemini-2.5-Flash) automatically synthesizing a code harness — up to the *harness-as-policy* extreme where the LLM is not called at runtime. Mechanism-level evidence for the "model subsumes the harness" direction.
- **The "model eats the harness" thesis.** Articulated by [[Logan Kilpatrick]] in the [[2026-06-11-kilpatrick-sequoia-model-eats-the-harness|Sequoia interview]]: the harness gets upstreamed into the model within ~12 months.
- **Antigravity + Omni.** [[Antigravity]] (from the Windsurf team) is the single agent harness now rebasing Google's products; [[Omni]] is the single any-input→any-output model replacing ~8 separate systems.
- **Culture.** Strong research portfolio under Demis Hassabis (Nobel laureate); explicitly non-zero-sum framing; deploying Gemini to billion-user products at a scale "only two companies in the world" can.

## Relationship to Google

GDM is the AI-lab role within [[Google]]; this wiki's broader Google footprint (Cloud, ADK, [[Google Research]]) is tracked on the [[Google]] page. GDM employs [[Logan Kilpatrick]] among ~100,000+ Google engineers who dogfood Gemini.

## In the AI100 2026 report (added 2026-11-22)

The [[2026-11-10-ai100-ai-goes-mainstream-2026|AI100 2026 report]] uses Google DeepMind for its science examples:
- **AlphaFold**: the 2024 Nobel Prize in Chemistry and 214 million predicted structures.
- **AlphaGenome** (Nature, early 2026).
- **GNoME**: 2.2 million predicted inorganic compounds.
- **AlphaProof and AlphaGeometry 2** at IMO silver level in 2024, then **Gemini Deep Think** at gold in 2025.
- **The AI Co-Scientist** as the model of human–AI collaboration in research.

It also notes that AlphaFold *"shifts the work elsewhere"* rather than eliminating the biologist's work.

## Named in a CSCW talk on agents (added 2026-11-27)

[[2026-11-23-zhang-stanford-cs547-cscw-work-with-agents|Amy X. Zhang's CS547 talk]] lists her as on sabbatical at Google DeepMind. It also cites a CSCW 2026 keynote by a GDM researcher (Merrie Morris) that made working with AI the conference's central topic. Neither is a GDM research claim; the page only records the affiliation.
