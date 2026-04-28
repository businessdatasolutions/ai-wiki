# Log

Append-only chronological record of wiki operations. Strict prefix format so `grep "^## \[" wiki/log.md | tail -10` works as a CLI. Format (indented to keep grep clean):

    ## [YYYY-MM-DD] <op> | <title>

Permitted operations: `ingest`, `query`, `lint`, `synthesize`, `refactor`. See [the design doc, §9.2](../docs/superpowers/specs/2026-04-28-llm-wiki-design.md#92-wikilogmd) for details.

---

## [2026-04-28] refactor | scaffold initialized

Initial wiki scaffold built per [the design doc](../docs/superpowers/specs/2026-04-28-llm-wiki-design.md). Created `raw/` (articles, papers, lectures, books, images, assets) and `wiki/` (sources, entities, concepts, syntheses, threads) skeletons with `.gitkeep` placeholders, plus this log and a canonical `index.md`. Ready for first source ingest.

## [2026-04-28] refactor | added raw/reports/ and kind: report

Industry reports, government white papers, consultancy decks, and sell-side equity research didn't fit cleanly into `raw/papers/` (academic) or `raw/articles/` (web-clipped markdown). Added `raw/reports/` as a peer of `raw/papers/`, extended the source-page `kind:` enum to include `report`, and added a row to design doc §10 + decision log §18. Sub-types are disambiguated via tags (`consultancy`, `government`, `equity-research`, `ngo`).

## [2026-04-28] refactor | folder placement: MITTRI_Cisco to raw/reports/

Confirmed Anand & Wu's "Gen AI Playbook for Organizations" is HBR (Nov–Dec 2025) → stays in `raw/articles/`. Moved MITTRI_Cisco to `raw/reports/` (sponsored research from MIT Tech Review Insights, not journalism). Final placement of the 6 pre-ingest sources: 3 articles, 1 paper, 2 reports.

## [2026-04-28] ingest | Artificial Intelligence Index Report 2025

First real ingest. Maslej et al., Stanford HAI, April 2025, 414 pp, CC BY-ND 4.0. Read in scope: Intro + Top 12 Takeaways + all chapter highlights + Ch 4 Economy in depth (incl. all of §4.4 Corporate Activity and §4.5 Robot Deployments) + Ch 3 RAI skim via highlights and §3.10 election-misinformation case studies.

- Source page created: [[2026-04-28-ai-index-report-2025]]
- Entity pages created: [[Stanford HAI]], [[AI Index]], [[Nestor Maslej]]
- Concept pages created: [[enterprise-ai-adoption]], [[responsible-ai]], [[generative-ai]], [[foundation-models]], [[ai-benchmarks]]
- Index updated: 1 source line + 3 entity lines + 5 concept lines = 9 new index entries.
- Notable choices: deferred ~30 wikilinkable mentions (companies like OpenAI/Anthropic/Google DeepMind, individuals like Brynjolfsson/Manyika, all individual benchmarks like MMLU/GPQA) to avoid stub-spam — they appear as dangling wikilinks ready to be promoted to standalone pages when the next theme-aligned source surfaces them. The `ai-benchmarks` concept page acts as a roster/umbrella for now.
- Total file touch: 11 (1 source + 3 entities + 5 concepts + index + log) — within the design's 10–15 expected for a moderately rich source.

## [2026-04-28] refactor | added kind: project to entity schema

The [[AI Index]] is a project/initiative within [[Stanford HAI]], not an org per se — but the entity-page `kind:` enum in design §5.2 only allows `person | org | product | place | event`. Extended to include `project`. Updated design doc §5.2 and decision log §18.

## [2026-04-28] ingest | MIT Sloan — How to boost your organization's AI maturity level

Second ingest. Kristin Burnham (writer), MIT Sloan / Ideas Made to Matter, Oct 7 2025 — reporting on a research briefing by [[Stephanie Woerner]], [[Peter Weill]], Ina Sebastian, Evgeny Káganer at [[MIT CISR]]. 3 pages of content. Underlying research: MIT CISR 2022 Future Ready Survey (N=721) + 2024 interviews at 9 enterprises.

- Source page created: [[2026-04-28-mit-sloan-ai-maturity]]
- Entity pages created: [[MIT CISR]], [[Stephanie Woerner]], [[Peter Weill]]
- Thread page opened: [[ai-maturity-measurement-comparison]] — for tracking the cross-source methodology question (AI Index vs. MIT CISR vs. future sources)
- Concept pages enriched:
  - [[enterprise-ai-adoption]] — major: added the Four Stages of AI Maturity framework, Four S challenges, Stage 2→3 financial inflection, Guardian + Italgas worked examples; updated Debates section with cross-source methodology comparison
  - [[responsible-ai]] — light: added "RAI as operationalized stewardship" subsection with Guardian + Italgas examples
  - [[generative-ai]] — light: added "Agents in enterprise AI maturity" subsection mapping autonomous-agent role to Stage 3+
- Index updated: 1 source + 3 entity + 1 thread = 5 new entries; concept summaries refreshed.
- **Contradiction check: no contradictions** with [[2026-04-28-ai-index-report-2025|AI Index 2025]]. Strong qualitative convergence on "high adoption, low maturity, value capture is hard" — though the two sources use different instruments and definitions. The methodology divergence is itself the topic of the new [[ai-maturity-measurement-comparison]] thread.
- Notable choices: Ina Sebastian, Evgeny Káganer, Kristin Burnham (writer), Guardian Life Insurance, Italgas, IESE Business School, MIT Sloan all left as dangling wikilinks for now — single-source coverage; will create pages when they recur.
- Total file touch: 11 (1 source + 3 entities + 1 thread + 3 concept enrichments + index + log + raw PDF).

## [2026-04-28] ingest | Batch (4 sources): MITTRI/Cisco, HBR Anand-Wu, HBR Werner-Le-Brun, Gomaa Lean 4.0

Third through sixth ingests in a single batch (user-requested override of the default supervised one-at-a-time mode per design §7). Total: 4 sources, ~50 pages of content combined, 26 files touched. Single commit.

**Sources ingested:**
1. [[2026-04-28-mittri-cisco-ai-enabled-enterprise]] — *Building the AI-enabled enterprise of the future* (MIT Tech Review Insights × Cisco, 2025, 8 pp). Sponsored research; 13% / 98% / 85% readiness-urgency triad; chatbot→agent→multi-agent progression; 5-foundations framework; Ford case study (63→0 defects, 15hr→10s fluid dynamics).
2. [[2026-04-28-anand-wu-genai-playbook]] — *The Gen AI Playbook for Organizations* (Anand & Wu, HBR Nov–Dec 2025, 11 pp). 2×2 task-suitability framework (cost of errors × type of knowledge); paradox of access; 4-move competitive advantage playbook; six leakage points exhibit.
3. [[2026-04-28-werner-lebrun-octopus-organization]] — *Become an Octopus Organization* (Werner & Le-Brun, HBR Nov–Dec 2025, 12 pp). Tin Man vs Octopus archetype; 12% transformation success baseline; 3 antipattern categories; learning loop with Donella Meadows leverage hierarchy.
4. [[2026-04-28-gomaa-lean-4-0]] — *Lean 4.0: Strategic Roadmap for Smart Manufacturing* (Gomaa, IJESE Apr 2025, 20 pp open access). Off-theme; 23×23 Lean ↔ Industry 4.0 tool mapping; 9-step implementation framework; 11 research gaps; complements MITTRI/Cisco manufacturing data and Italgas worked example.

**New entity pages (6):** [[Cisco]], [[MIT Technology Review Insights]], [[Harvard Business Review]], [[Amazon Web Services]], [[Bharat N. Anand]], [[Andy Wu]].

**New concept pages (3):**
- [[ai-agents]] — promoted now that 4 sources discuss agents substantively (AI Index, MIT Sloan, MITTRI/Cisco, Anand-Wu). Covers chatbot→agent→multi-agent progression, RE-Bench results, deployment examples (Salesforce Agentforce, Italgas DANA, Harvey, GitHub Copilot).
- [[lean-4-0]] — 23×23 mapping; 9-step framework.
- [[industry-4-0]] — referenced by MITTRI/Cisco (manufacturing data) and Gomaa.

**New thread (1):**
- [[organizational-frameworks-for-ai-adoption]] — tracks the cross-source comparison of MIT CISR Four Stages + Four S vs Anand-Wu 2×2 vs Cisco 5 Foundations vs Werner-Le-Brun Octopus/Tin Man. Initial reading: complementary, not competing — they target different layers (org design / readiness / capability progression / task deployment / diagnosis).

**Major enrichments to existing pages:**
- [[enterprise-ai-adoption]] — added the 5-lens working definition; full Anand-Wu 2×2 framework with examples; the leakage-points diagnostic; the paradox-of-access argument; Ford worked example.
- [[responsible-ai]] — added "AI security as a discipline" (Cisco fundamentals) and "Risk-vs-experimentation tradeoff" (Anand-Wu's JPMorgan example).
- [[generative-ai]] — refactored agents subsection to redirect to new [[ai-agents]] page; added "Access democratization" (MS-DOS→GUI analogy) and "Tools" table (ChatGPT, Harvey, Copilot, Agentforce, DANA).
- [[ai-maturity-measurement-comparison]] thread — added MITTRI/Cisco readiness instrument and Werner-Le-Brun's 12% transformation-success baseline; updated cross-walk table with 4 success-rate measurements (1%/7%/12%/13% spread).

**Deferred (dangling wikilinks pending recurrence):** [[Jana Werner]], [[Phil Le-Brun]], [[Attia Hussien Gomaa]] (single-source authors); [[Jeetu Patel]], [[Liz Centoni]], [[Patrick Milligan]] (quoted execs); [[Ford]], [[Harvey]], [[GitHub Copilot]], [[Capgemini]], [[PwC]] (recur-likely); plus ~15 case-study companies (Netflix, Coca-Cola, Capital One, Harrah's, JPMorgan, etc.).

**Contradiction check:** no contradictions. Strong cross-source convergence on "high adoption, low maturity, transformation hard, agents as near-term productivity story." Methodology divergences are tracked in the two open threads.

**Notable cross-source insights:**
- 4 different "success rate" measurements span a single order of magnitude (1% / 7% / 12% / 13%) — whatever you call success, it's rare.
- [[ai-agents]] now has 4-source convergent coverage and earned its standalone concept page.
- Concrete enterprise ROI numbers portfolio: Guardian RFP (1wk→24hr), Italgas WorkOnSite (+40%/-80%), Italgas €3M revenue commercialization, Ford squish tubes (63→0 defects), Ford fluid dynamics (15hr→10s).

**Total file touch: 26.** Source pages: 4 new. Entity pages: 6 new. Concept pages: 3 new + 4 enriched. Thread pages: 1 new + 1 enriched. Plus index.md, log.md, 4 raw PDFs.

## [2026-04-28] refactor | folder placement: Brynjolfsson Canaries paper to raw/papers/

User dropped the Brynjolfsson, Chandar & Chen "Canaries in the Coal Mine" Stanford Digital Economy Lab working paper (Aug 2025) into `raw/articles/` but it's an academic working paper (formal econometric methodology, references, ADP-payroll-data analysis). Moved to `raw/papers/` consistent with our convention (paper = academic; article = journalism/HBR-style). Surfaced a future schema-evolution candidate: source-page schema may benefit from explicit `working_paper` / `peer_reviewed` / `preprint` fields so rigor level is legible without reading the body.

## [2026-04-28] ingest | Brynjolfsson, Chandar & Chen — Canaries in the Coal Mine?

Seventh ingest. Stanford Digital Economy Lab working paper, Aug 26, 2025, by [[Erik Brynjolfsson]], Bharat Chandar, Ruyu Chen. ADP payroll data covering ~25M U.S. workers monthly, Jan 2021 – July 2025. Six empirical facts on AI's recent employment effects. Read in scope: pages 1–20 (intro, related literature, data description, Facts 1–4 with figures); Facts 5–6 captured from intro summary.

**Headline finding:** Early-career workers (ages 22–25) in the most AI-exposed occupations have experienced a **~13% relative decline in employment** since late 2022 (after firm-time-effects controls). Concentrated in **automation** uses, not **augmentation**. Adjustments visible in **employment more than wages** (wage stickiness). Robust to alternative samples and explanations.

- Source page created: [[2026-04-28-brynjolfsson-canaries-coal-mine]]
- Entity pages: [[Erik Brynjolfsson]] (promoted from dangling — major recurring author with both the customer-support productivity study and now this employment study), [[Stanford Digital Economy Lab]] (new institutional source, distinct from [[Stanford HAI]])
- Concept pages created:
  - [[ai-employment-effects]] — empirical/sociological lens on AI's labor consequences (job displacement, age, wages); now load-bearing on [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson 2025]] data and reconciling with [[2026-04-28-ai-index-report-2025|AI Index 2025]]'s task-level equalizing-effect studies
  - [[automation-vs-augmentation]] — conceptual/strategic lens; cross-references 4 sources (AI Index productivity studies, Anand-Wu 2×2, MITTRI/Cisco agent agency framing, Brynjolfsson Fact 3) all converging on the same cut
- Concept pages enriched:
  - [[enterprise-ai-adoption]] — added the equalizing-effect-vs-occupation-level reconciliation; added "Realized employment outcomes" subsection citing Brynjolfsson 2025 alongside McKinsey workforce-expectations data
  - [[responsible-ai]] — added "Labor-market disruption as an under-attended RAI concern" subsection — concrete questions for orgs about entry-level pipeline policy
  - [[generative-ai]] — added cross-reference to [[automation-vs-augmentation]] as load-bearing distinction
- Index updated: 1 source + 2 entity + 2 concept = 5 new entries; concept summaries refreshed.
- **Cross-source synthesis**: this ingest creates a substantive **task-level vs. occupation-level paradox** captured across [[Erik Brynjolfsson]] entity page, [[ai-employment-effects]], and [[enterprise-ai-adoption]] — AI raises productivity per worker (especially low-skill workers, the equalizing effect) while reducing the *number of workers* needed in automate-able roles. Both findings can be true; the popular reading of "AI helps low-skill workers most → equalizing → good for entry-level" has been over-extended.
- **Contradiction check**: complicates rather than contradicts prior wiki claims. The "equalizing effect" framing in the AI Index productivity studies and the entry-level employment decline in this paper are *both* true and *not* mutually exclusive — but the popular interpretation has elided the distinction. Captured explicitly in [[ai-employment-effects]] § Debates.
- Notable choices: [[Bharat Chandar]] and [[Ruyu Chen]] (co-authors), [[ADP]] (data provider), [[Daron Acemoglu]], [[David Autor]] (cited theory), [[Anthropic Economic Index]] (data source) all left as dangling wikilinks for now — single-source coverage; will create when they recur.
- Brynjolfsson 2023 customer-support paper noted on the [[Erik Brynjolfsson]] entity page but not yet ingested as its own source. Worth a future ingest if the user can locate it.
- Total file touch: 12 (1 source + 2 entities + 2 concepts + 3 enrichments + 1 thread enrichment hint via cross-references + index + log + 1 raw PDF moved). Within design's 10–15 envelope.

## [2026-04-28] refactor | folder placement: Canaries + Generative AI at Work to raw/papers/

After the GitHub push, user re-downloaded source PDFs (since `git filter-repo` had aggressively cleaned the local working tree). The re-downloads landed in `raw/articles/`; both Brynjolfsson papers belong in `raw/papers/`. Moved both. **Surfaced an 8th source the wiki had missed:** "Generative AI at Work" by Brynjolfsson, Li & Raymond, the canonical primary source for the customer-support productivity finding cited extensively across the wiki via secondary references through [[2026-04-28-ai-index-report-2025|AI Index 2025]]. Triggered the next ingest.

## [2026-04-28] ingest | Brynjolfsson, Li & Raymond — Generative AI at Work (QJE 2025)

Eighth ingest. **First peer-reviewed journal article** in the wiki: *Quarterly Journal of Economics* 140 (2025), pp. 889–942, advance access Feb 4 2025. CC BY-NC 4.0 open access via OUP. Working paper predecessor: NBER 31161 (2023) — the version cited via AI Index 2025 §4.4 throughout 2024.

**Headline:** Studies the staggered introduction of a GPT-3-based customer-support AI assistant at a Fortune 500 firm with 5,172 agents (mostly Philippines-based). +15% productivity (RPH); equalizing effect with low-skill workers gaining ~30%, top performers ~0% speed gains AND **small quality decline**; AI accelerates experience curve ~3×; durable learning (workers maintain efficiency during AI outages); convergence in communication patterns; reduced worker attrition (driven by retention of new workers).

This ingest is mostly a **primary-source upgrade** for productivity claims that have been load-bearing throughout the wiki via secondary citation from [[2026-04-28-ai-index-report-2025|AI Index 2025]] §4.4.

- Source page created: [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work]]
- Entity page enriched: [[Erik Brynjolfsson]] — promoted §1 from secondary citation to primary; updated headline number from +14.2% (NBER WP) to +15% (QJE); added top-performer-quality-decline nuance; added durable-learning detail.
- Concept pages enriched:
  - [[enterprise-ai-adoption]] — refined the equalizing-effect productivity table with QJE numbers and the small-quality-decline nuance for top performers
  - [[ai-employment-effects]] — added "Productivity gains alongside employment declines" subsection with primary-source citation; new "Convergence in communication patterns" subsection
  - [[automation-vs-augmentation]] — promoted to primary anchor for augmentation's positive productivity effects; added "Pareto-improvement caveat" subsection on top-performer quality decline + long-run training-data risk
  - [[generative-ai]] — added concrete primary-source numbers; clarified the augmentation-vs-automation empirical record

**Key new findings carried forward:**

- **+15.2%** RPH (preferred FE specification) — slight upward revision from +14.2% NBER WP
- **Top performers see small quality decline** alongside small speed gains — the equalizing effect is NOT "0% gain for high-skill" but rather "0% net gain WITH quality slightly worse" — the wiki previously missed this.
- **Long-run training-data risk**: if top performers reduce original contributions because they adhere more to AI suggestions, the AI's training data degrades over time. A subtle long-run feedback concern not previously in the wiki.
- **Augmentation by design**: the system was explicitly architected to augment (suggestions only to agent; agent has full discretion; system declines to suggest when training data is insufficient). This makes the paper a clean primary anchor for augmentation in [[automation-vs-augmentation]].
- **Customer-side effects** newly captured: customers more polite to AI-treated agents, less likely to escalate to manager.
- **Convergence finding**: low-skill agents begin communicating more like high-skill agents — a previously-missing skill-leveling dimension.

**Two-paper Brynjolfsson arc** is now load-bearing in the wiki: [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Generative AI at Work]] (productivity within a role, equalizing effect) + [[2026-04-28-brynjolfsson-canaries-coal-mine|Canaries in the Coal Mine]] (employment across occupations, entry-level decline) together describe the **task-level vs. occupation-level paradox**.

**Schema note (de facto change):** Source frontmatter now includes `peer_reviewed: true` and `working_paper_predecessor` for this paper. **Should be formalized in design doc §5.1 if a third peer-reviewed source is ingested**; for now treating it as a single-instance schema extension rather than a permanent change. Tracked in [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|the source page]]'s "Schema note" section.

**Contradiction check:** no contradictions; this ingest *refines and corrects* prior wiki claims rather than contradicting them. Updated specific numbers (14.2% → 15%) and added missing nuance (top-performer quality decline; communication-pattern convergence). Cited secondary references (via AI Index) remain valid; the wiki now has the primary source available for direct citation alongside.

**Notable choices:** [[Danielle Li]] and [[Lindsey Raymond]] left as dangling wikilinks (single-source coverage so far).

**Total file touch: 8** (1 source + 1 entity enrichment + 4 concept enrichments + index + log; raw PDF on disk but not committed per the gitignore rule established post-push).
