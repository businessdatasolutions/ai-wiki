# Log

Append-only chronological record of wiki operations. Strict prefix format so `grep "^## \[" wiki/log.md | tail -10` works as a CLI. Format (indented to keep grep clean):

    ## [YYYY-MM-DD] <op> | <title>

Permitted operations: `ingest`, `query`, `lint`, `synthesize`, `refactor`, `bulk-refactor` (added v0.2 — for any operation touching >10 wiki pages, with affected slug list and reversibility note). See [the design doc, §9.2](../docs/superpowers/specs/2026-04-28-llm-wiki-design.md#92-wikilogmd) for details.

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

## [2026-04-28] ingest | Anthropic Economic Index — fourth report (summary article)

Ingested Anthropic's 15 Jan 2026 Economic Research blog post summarizing the fourth Anthropic Economic Index report. The article is a summary of an underlying full report which is *not* separately ingested; claims here are flagged as drawn from the summary, with the parent report cited.

**Pages added:**

- [[2026-04-28-anthropic-economic-index-q4-2025]] — source page
- [[Anthropic]] — entity (organization)
- [[Anthropic Economic Index]] — entity (project; previously a dangling wikilink referenced from `automation-vs-augmentation` and `ai-employment-effects`)
- [[METR]] — entity (organization)
- [[ai-deskilling]] — concept (new)

**Pages enriched:**

- [[automation-vs-augmentation]] — added longitudinal Claude.ai augmentation/automation split table (Jan 2025 → Nov 2025: 55/41 → 55/42 → 47/49 → 52/45); appended Anthropic 4th-report row to the four-source convergence table; existing section numbering shifted (old §6 became §7).
- [[ai-employment-effects]] — added three new sections: aggregate productivity reliability adjustment (+1.0 to +1.2 pp/yr); effective AI coverage at occupation level (radiologists, data entry keyers above the 45° line; teachers, software developers below); task-content shift / deskilling pointer to the new concept page. Added [[ai-deskilling]] to Related concepts.
- [[generative-ai]] — added "Measurement framework: economic primitives" section before the capability-gains section. Lists the five primitives + headline numbers (9× / 12× speedup; 70% / 66% success; +1.0–1.2 pp/yr).
- [[ai-benchmarks]] — added "Task horizons (METR / Anthropic Economic Index 4th report)" section before the benchmark roster. METR ~2hr / API ~3.5hr / Claude.ai ~19hr table for Sonnet 4.5.

**Index + log updated.**

**Key new findings carried into the wiki:**

- **Economic primitives framework** — five population-scale measurements (task complexity, skill level, use case, AI autonomy, success) derived from Claude classifying its own conversations.
- **Speedup-by-complexity gradient** — 9× HS-level / 12× college-level on Claude.ai; greater on API; success rate falls slightly with complexity (70% → 66%).
- **METR comparison** — first benchmark referenced where wiki has the methodology gap: fixed-task ~2hr vs. observed-platform ~19hr (Claude.ai), with selection-bias and decomposition explanations.
- **Effective AI coverage** — new occupation-level metric, success-weighted; outliers identified.
- **Task-composition deskilling** — first-order effect, distinct from displacement; new concept page anchored on this single source.
- **Augmentation reversal** — Nov 2025 Claude.ai sample at 52/45 (augmentation lead) reverses the Aug 2025 47/49 (automation lead). Longer arc still shows automation gaining share since Jan 2025 (when split was 55/41).
- **Aggregate productivity revision** — Anthropic walks back its own 1.8 pp/yr estimate by ~⅓ to 1.0–1.2 pp/yr once reliability is accounted for.

**Cross-source neutrality applied:** per the cross-source neutrality preference saved this session, cross-references to other sources (Brynjolfsson 2025 papers, AI Index) describe what each measures without drawing comparative conclusions ("complementary," "tension," "contradicts," etc.). Reader infers; backlinks surface neighbours.

**Notable choices:**

- Wrote **two Anthropic entities** rather than one — `[[Anthropic]]` (the organization) and `[[Anthropic Economic Index]]` (the research initiative), parallel to `[[Stanford HAI]]` / `[[AI Index]]`. The Economic Index page resolves a previously dangling wikilink from `automation-vs-augmentation` line 15 and `ai-employment-effects` line 40.
- **Did not** add a back-pointing interpretive section to the Brynjolfsson 2025 source pages — the alias-aware Backlinks extension surfaces the connection automatically; per cross-source neutrality, no editorialization.
- **Did not** create a synthesis/thread page on skill-bias-vs-equalizing-effect — earlier draft proposed it, but on closer inspection the two findings address different units of analysis (across-task vs. within-occupation) and there is no clear contradiction to synthesize. Deferred until a third source weighs in.
- Dangling wikilinks left intentionally: [[Claude]], [[Claude Sonnet 4.5]], [[Claude Opus 4.5]], [[Jack Clark]] — single-source coverage so far. Stub indicators per CLAUDE.md.

**Contradiction check:** no contradictions with prior wiki claims. The 52/45 Nov 2025 augmentation lead refines the wiki's understanding of the longer arc (automation has been gaining share since Jan 2025 even though the latest sample is augmentation-led). The aggregate productivity revision (1.8 → 1.0–1.2 pp/yr) is a tightening of Anthropic's own prior estimate, not a contradiction with another source.

**Total file touch: 11** (1 source + 3 entities + 1 new concept + 4 concept enrichments + index + log; raw PDF on disk under `raw/articles/` but not committed per the gitignore rule).

## [2026-04-28] ingest | Batch: 7 sources (Bansal-Birkinshaw, Reitz-Higgins, Webb, Warner-Wäger, Dell'Acqua et al., Carroll-Sørensen, FTSG Convergence Outlook)

User invoked **batch ingest, full depth, all six** (later +1: FTSG Convergence Outlook 2026 added mid-batch). Total seven sources. Per CLAUDE.md, batch supervised default suspended for this batch by user instruction; cross-source neutrality preference (saved earlier this session) applied throughout.

**Pages added:**

- [[2026-04-28-bansal-birkinshaw-systems-thinking]] — HBR Sept–Oct 2025; systems thinking as third innovation mode beyond breakthrough/design.
- [[2026-04-28-reitz-higgins-spacious-thinking]] — HBR.org July 2025; doing-mode vs. spacious-mode attention.
- [[2026-04-28-webb-strategic-foresight]] — HBR.org Jan 2024; FTSG 10-step methodology.
- [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation]] — Long Range Planning 2019; nine digital microfoundations under Teece.
- [[2026-04-28-dellacqua-jagged-technological-frontier]] — Org Sci 2026; 758-BCG-consultant RCT; "jagged frontier" concept.
- [[2026-04-28-carroll-sorensen-strategy-analogy]] — Strategy Science 2024; analogical reasoning tools.
- [[2026-04-28-ftsg-convergence-outlook-2026]] — FTSG 1st edition Jan 2026; intro/framing only ingested (~5% of 317 pages).

**Entities added (15):** [[Amy Webb]], [[Future Today Strategy Group]], [[Boston Consulting Group]], [[Ethan Mollick]], [[Karim Lakhani]], [[Fabrizio Dell'Acqua]], [[Tima Bansal]], [[Julian Birkinshaw]], [[Ivey Business School]], [[Megan Reitz]], [[John Higgins]], [[Karl S.R. Warner]], [[Maximilian Wager]], [[Glenn R. Carroll]], [[Jesper B. Sorensen]].

**Concept pages added (5):** [[jagged-frontier]], [[systems-thinking]], [[dynamic-capabilities]], [[strategic-foresight]], [[analogical-reasoning]].

**Concept pages enriched:** [[automation-vs-augmentation]] (added Dell'Acqua jagged-frontier row to four-source convergence table), [[ai-employment-effects]] (added Dell'Acqua equalizing-effect among elite knowledge workers; subjective-coherence-vs-correctness decoupling), [[generative-ai]] (added Dell'Acqua field-experiment GPT-4 evidence), [[enterprise-ai-adoption]] (added capabilities lens via Warner-Wäger and foresight lens via Webb/FTSG).

**Index + log updated.**

**Cross-source notes (descriptive only, per cross-source neutrality preference):**

- Webb's HBR article and FTSG's *Convergence Outlook* are author/firm pair; the 10-step methodology is the underlying mechanism for the convergence-clustered framing.
- Warner-Wäger dynamic capabilities, MIT CISR Four Stages, Werner-Le-Brun Octopus/Tin Man, and MITTRI/Cisco five foundations all address how organizations adapt under environmental change — wiki cross-references describe topic overlap without ranking the frameworks.
- Dell'Acqua's "equalizing effect within elite professionals" and Brynjolfsson, Li & Raymond's "equalizing effect within customer support" are at different units of analysis (across-task, elite-only vs. within-occupation, broad-skill); both source pages and the relevant concept pages note the topic without drawing comparative conclusions.
- Bansal-Birkinshaw systems thinking and Reitz-Higgins spacious thinking address related but distinct phenomena — the former is methodological (innovation mode), the latter is attentional (cognitive mode); cross-references note the adjacent framing without conflating them.

**Notable choices:**

- **File-naming mismatch flagged**: the raw PDF for [[2026-04-28-dellacqua-jagged-technological-frontier]] is on disk as `Mitchell and Dino - 2011 - In Search of Research Excellence Exemplars in Entrepreneurship.pdf` but the actual content is the Dell'Acqua et al. (2026) Jagged Frontier paper. The `raw:` frontmatter field preserves the literal filename; recommend renaming on disk for clarity. The wiki source page is named for the actual content.
- **FTSG Convergence Outlook only intro-ingested (pp. 1–15 of 317)**: the per-section deep-reads (Compute Shock, Polycompute, Agentic Economies, New Labor Equation, Human Augmentation, Living Intelligence, Programmable Biology, Autonomous Care, Emotional Outsourcing, Corporate Panopticon) are deferred to future per-section ingests. The wiki source page documents this scope explicitly.
- **Warner & Wäger 2019** is the oldest source ingested (pre-GenAI). Included because the dynamic-capabilities framework is foundational and applies equally to AI adoption today; marked in the open-questions sections of [[dynamic-capabilities]] and [[enterprise-ai-adoption]] that updating the framework for the 2026 GenAI context is a natural follow-up.
- **Carroll-Sørensen 2024** is off-direct-theme but anchors a useful concept ([[analogical-reasoning]]) that may matter for AI strategy work (e.g., FTSG's reliance on historical convergence-cycle analogies; LLMs as potential analogy generators).
- Many BCG / Henderson Institute co-authors of the Jagged Frontier paper ([[François Candelon]], [[Saran Rajendran]], [[Lisa Krayer]], [[Edward McFowland III]], [[Hila Lifshitz]], [[Katherine C. Kellogg]]) left as dangling wikilinks — single-source coverage so far. Stub indicators per CLAUDE.md.

**Contradiction check:** no direct contradictions with prior wiki claims. The Dell'Acqua finding that *top-half-skill* knowledge workers gain meaningfully (+11%) refines the prior wiki framing that some sources (notably Brynjolfsson, Li & Raymond customer support) show ~0% gain at the top — these are at different units of analysis (within-occupation customer-service vs. across-task elite consulting) so the refinement is additive, not contradictory. Existing source pages already correctly bound their claims to their own samples.

**Total file touch (this batch): 33** (7 sources + 15 entities + 5 new concepts + 4 concept enrichments + index + log; raw PDFs on disk under `raw/articles/`, `raw/papers/`, `raw/reports/` but not committed per the gitignore rule).

## [2026-04-29] ingest | Boussioux, Lane, Zhang, Jacimovic & Lakhani — The Crowdless Future? (Org Sci 2024)

Single-source ingest under auto mode. Brief takeaway plan surfaced before writing per CLAUDE.md "discuss before writing" preference (compressed for auto mode).

**Pages added:**

- [[2026-04-29-boussioux-crowdless-future]] — source page
- [[Leonard Boussioux]], [[Jacqueline N. Lane]], [[Miaomiao Zhang]], [[Vladimir Jacimovic]] — author entities
- [[Continuum Laboratory]] — partner organization (San Francisco AI firm; ContinuumLab.AI)

**Pages enriched:**

- [[automation-vs-augmentation]] — added the Boussioux row to the cross-source convergence table; added §7 on differentiated vs. independent search as fine-grained augmentation patterns; existing §7 (Pareto-improvement caveat) became §8.
- [[jagged-frontier]] — added the Boussioux finding (HAI in incremental search space, HC at extreme novelty) to the convergence section.
- [[generative-ai]] — added field-experimental cost/time data ($27 / 5.5 hrs vs $2,555 / 2,520 hrs; ≈94× cost reduction) and HC/HAI per-dimension table.
- [[ai-employment-effects]] — added crowdsourcing labor markets section: HAI substitution dynamics on Freelancer.com–style platforms; novelty advantage retained by HC at top decile.

**Index + log updated.**

**Key findings carried into the wiki:**

- **HC/HAI trade-off** — HC higher novelty (3.508 vs 3.230 multi / 3.469 single); HAI higher strategic viability, environmental, financial, quality. Mixed-effects models with N=3,900 evaluator-solution pairs, 18 blocks, 300 evaluators.
- **Differentiated > independent search** — single-instance with iterative differentiation prompts beats multi-instance independent search on quality/viability while preserving novelty.
- **94× cost reduction** ($27 vs $2,555); ~458× time reduction (5.5 hrs vs 2,520 human-hours).
- **Failure modes flagged**: formal-rationality bias, training-data confinement, confabulation/hallucination.
- **Three solution sources tested**: HC (n=54 after filtering), HAI multi-instance (n=90), HAI single-instance (n=90).

**Cross-source notes (descriptive only, per cross-source neutrality preference):**

- Same publication and shared author ([[Karim Lakhani]]) as [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua et al. 2026 Jagged Frontier]]; both are GPT-4 field-experimental evidence in different settings (consulting tasks vs ideation crowdsourcing).
- The HC/HAI novelty-vs-value pattern is one face of the [[jagged-frontier]] — describes which parts of solution space AI inhabits well.
- The differentiated-search pattern parallels the *task-iteration* augmentation mode in the [[Anthropic Economic Index]] taxonomy.
- The circular-economy framing connects topically to [[2026-04-28-bansal-birkinshaw-systems-thinking]] (sustainability as a wicked-problem domain).

**Notable choices:**

- **Date prefix `2026-04-29`** — following the date-of-ingest convention; today is the first new ingest at a date other than the wiki's instantiation day.
- **No new concept page**: HC vs HAI is a finding rather than a standalone concept; folded into existing concepts via enrichment. If a third source on creative-problem-solving arrives, a dedicated `creative-problem-solving` concept page would be warranted.
- Dangling wikilinks left intentionally: [[Harvard Business School]] (mentioned as affiliation; would be its own entity under broader coverage); [[LISH]] (Laboratory for Innovation Science at Harvard).

**Contradiction check:** no direct contradictions with prior wiki claims. The Boussioux finding that HC retains a novelty advantage over GPT-4 in creative ideation is consistent with the [[jagged-frontier]]'s description of AI as occupying incremental search space, and with [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua's]] outside-the-frontier degradation result (in different domain). No revisions to existing source pages needed.

**Total file touch: 11** (1 source + 5 entities + 4 concept enrichments + index + log; raw PDF on disk under `raw/papers/` but not committed per the gitignore rule).

## [2026-04-30] ingest | Artificial Intelligence Index Report 2026 (9th edition)

Single-source ingest of the 9th annual [[AI Index]] from [[Stanford HAI]] (Sajadieh et al., April 2026). The 2025 edition is already in the wiki; this ingest layered the 2026 numbers and structural changes on top, rather than treating the 2026 edition as an independent source. Front matter and the 15 Top Takeaways were ingested in full; chapters 2–9 (~360 of ~430 pages) deferred to per-chapter or thematic deep-reads.

**Pages added:**

- [[2026-04-30-ai-index-report-2026]] — source page
- [[Sha Sajadieh]] — new EiC entity (replaces [[Nestor Maslej]] as 2026 EiC; Maslej remains a contributor)
- [[Yolanda Gil]] — entity (now chair; was chair-elect in 2025)
- [[Schmidt Sciences]] — new analytics/research partner; collaborated on standalone Medicine chapter

**Pages substantially updated:**

- [[AI Index]] — replaced "What it tracks" table to mirror the 2026 9-chapter structure (Medicine spun off from Science); replaced Steering Committee section to reflect Yolanda Gil → chair, Perrault → co-chair, Sajadieh → EiC, plus joins (Altman, Brodley, Dignum, Kumar, Landay, Tabassi, Weld) and departures (Etchemendy, Ligett); added 2026 row to editions table; added Schmidt Sciences (data partner) and Infosys (supporting funder); updated AI-tooling acknowledgement (Claude/ChatGPT for editing, Gemini 3 for image generation).
- [[generative-ai]] — added 2026 numbers section: 53% population adoption in 3 years; $172B U.S. consumer value; $285.9B U.S. private AI investment (~2.6× the 2024 figure); 88% organizational adoption; >80% U.S. high-school + college students use AI.
- [[foundation-models]] — added 2025 notable-model counts (U.S. 59, China 35, South Korea 8, Europe 2); top organizations (OpenAI 20, Google 14, Alibaba 11, Anthropic 7, etc.); 17.1M H100-equivalent global compute; 5,427 U.S. data centers; 29.6 GW power capacity; Grok 4 emissions 72,816 t CO2eq; OLMo 3.1 Think 32B as data-quality counter-evidence to scale; disclosure-decline section.
- [[ai-benchmarks]] — added 2025 saturation block: SWE-bench Verified 60% → ~100%; OSWorld agents 12 → 66%; Gemini Deep Think IMO gold; analog clock 50.1%; ChemBench frontier vs human chemists; RLBench 89.4% vs household 12%.
- [[responsible-ai]] — incidents 233 → 362 in 2025; new RAI dimension trade-off finding (e.g., safety improvement degrading accuracy).
- [[enterprise-ai-adoption]] — 88% organizational adoption; productivity gains 14–26% in customer support / software development; AI agent deployment in single digits per business function; education-policy gap (80% students use AI vs 6% teachers say policies are clear).
- [[ai-employment-effects]] — added section on U.S. software developers ages 22–25: -20% from 2024 (extends the [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson Canaries]] finding to a more recent timeframe via different methodology).
- [[jagged-frontier]] — added AI Index 2026 row to the convergence section: IMO gold + analog clock 50.1%; OSWorld leap; the term "jagged frontier" is now part of the AI Index narrative (Top Takeaway #4).

**Index updated** (1 new source line; 3 new entity lines).

**Key claims carried into the wiki:**

- AI capability not plateauing: SWE-bench 60→100%, OSWorld 12→66%, organizational adoption 88%.
- U.S.-China model gap effectively closed (DeepSeek-R1 briefly matched top US model Feb 2025; 2.7% lead as of March 2026).
- U.S. private investment $285.9B in 2025 (~2.6× 2024); 1,953 newly funded AI companies; AI talent immigration -89% since 2017.
- GenAI 53% population adoption in 3 years (faster than PC or internet); U.S. ranks 24th at 28.3%; consumer value $172B.
- AI agent deployment in single digits per function; software dev 22–25 employment -20%.
- AI environmental footprint: 72,816 t CO2eq for Grok 4 training; 29.6 GW data center capacity; GPT-4o inference water use exceeds 1.2M people's drinking water.
- Frontier AI for science outperforms human chemists on ChemBench; protein/genomics models with 100M-200M params beat 200× larger general models.
- Documented AI incidents 233 → 362; RAI dimension trade-offs.
- Trust gap: 73% experts vs 23% public expect positive AI impact on jobs (50pp gap); EU trusted more than US/China globally.

**Cross-source notes (descriptive only, per cross-source neutrality preference):**

- The "jagged frontier" term, originally introduced in the wiki via [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua et al. 2026]] (BCG consultants RCT), is now part of the AI Index's official narrative — same concept name, different data path (Index uses benchmark gaps; Dell'Acqua uses field experiment).
- The AI Index 2026's software-developer-22–25 employment finding is the same labor-market pattern documented by [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson et al. 2025]] via ADP payroll data; both source pages note the topic without ranking the methodologies.
- The [[2026-04-28-anthropic-economic-index-q4-2025|Anthropic Economic Index]] is the parallel measurement initiative; both surface complementary numbers on adoption, productivity, employment.

**Notable choices:**

- **Date prefix `2026-04-30`** — date-of-ingest (today), consistent with the convention since the wiki was instantiated.
- **Single source page rather than treating 2026 as an update to 2025**: the 2026 source page is its own standalone artifact with its own slug, frontmatter, and quotes. Concept pages reference *both* editions where appropriate, with the 2026 numbers layered on top of 2025 ones rather than overwriting.
- **Chapters 2–9 deferred**: with ~430 pages and 60+ named figures per chapter, full ingestion would be expensive. The Top Takeaways and Chapter 1 highlights cover most of the cross-cutting findings; per-chapter deep-reads can be triggered later (Chapter 4 Economy and Chapter 6 Medicine are the most likely candidates given existing wiki coverage).
- **AI tooling disclosure** is more visible in 2026 (image generation explicitly attributed to Gemini 3.1 / Gemini 3) — a small but interesting signal about AI Index editorial norms.
- Many dangling wikilinks left intentionally for new steering-committee members ([[Russ Altman]], [[Carla Brodley]], [[Virginia Dignum]], [[Vipin Kumar]], [[James Landay]], [[Elham Tabassi]], [[Dan Weld]]) — single-source coverage so far. Stub indicators per CLAUDE.md.

**Contradiction check:** no direct contradictions. The 2026 numbers refine and extend 2025 numbers; a couple of figures revised retroactively (notable models in 2024: 2025 edition reported 40 U.S. / 15 China / 3 Europe; 2026 edition's longitudinal chart shows similar magnitudes). The AI Index 2026's adoption finding (88%) extends the 2025 figure (78%); both are consistent with McKinsey's underlying instrument.

**Total file touch: 14** (1 source + 3 entities + 1 entity rewrite (AI Index) + 7 concept enrichments + index + log; raw PDF on disk under `raw/reports/` but not committed per the gitignore rule).

## [2026-05-02] ingest | Dutt, Rapoport, Chatterji, Weeratunga & Satcher — How to Move from AI Experimentation to AI Transformation (HBR)

Single-source ingest of a Bain × OpenAI co-authored HBR Generative AI piece (30 April 2026). The article names a failure pattern ("micro-productivity trap") that the wiki had previously circled with multiple vocabularies but not given a structural name to. Auto-mode supervised ingest.

**Pages added:**

- [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation]] — source page
- [[Arjun Dutt]], [[Gene Rapoport]], [[Aaron Chatterji]], [[Gawesha Weeratunga]], [[Harrison Satcher]] — author entities
- [[Bain & Company]] — co-publishing partner; 10–25% client EBITDA gains
- [[OpenAI]] — co-publishing partner via Economic Research team; resolves a previously dangling wikilink referenced from many wiki pages
- [[Lowe's]] — case study (Mylow / Mylow Companion across 1,700+ stores)
- [[micro-productivity-trap]] — new concept page anchored on this source

**Pages enriched:**

- [[automation-vs-augmentation]] — added Dutt et al. row to the convergence table; "offering lock-in" and "process lock-in" as failure modes; "improve the task" vs "reinvent the business" as strategic framing.
- [[enterprise-ai-adoption]] — added "Transformation lens" section: micro-productivity trap as named diagnostic for the gap between 88% organizational adoption and single-digit agent-mediated workflow depth; 10–25% EBITDA range; four-step framework; Lowe's + FabricationCo cases.
- [[generative-ai]] — added field-deployment-evidence section: Bain client EBITDA, Lowe's outcomes (>2× online conversion, +200bps CSAT in-aisle), FabricationCo outcomes (~$30M, 15× faster quotes, +10pp win rate).

**Index updated** (1 new source, 7 new entity lines, 1 new concept line).

**Key claims carried into the wiki:**

- The "micro-productivity trap" — task-level AI gains failing to translate to firm-level results.
- Two lock-ins: offering lock-in (AI optimizes existing offerings) and process lock-in (AI automates current processes without redesigning them).
- "Reinvent the business" vs "improve the task" as the strategic posture distinction.
- Bain client EBITDA 10–25% for transformation-mindset deployments.
- Four-step framework: narrow possibilities strategically (4–5 critical domains; top-4 across Bain portfolio = software dev, customer support, knowledge worker efficiency, marketing); reimagine workflows; engage those closest to the process; measure what matters (concrete business outcomes + continuous evals).
- Lowe's: Mylow + Mylow Companion (1,700+ stores; >2× conversion; +200bps CSAT).
- FabricationCo (anonymized Fortune 1000 manufacturer): 14 use cases identified, ~$30M additional profit on track, ~15× faster quote generation, +10pp win rate increase in 3 months.
- Boardroom imperative: AI transformation cannot be delegated to technology groups without specific goals/metrics.

**Cross-source notes (descriptive only, per cross-source neutrality preference):**

- The micro-productivity trap is a *fifth or sixth named vocabulary* in the wiki for the "adoption breadth ≠ transformation depth" pattern, alongside [[2026-04-28-anand-wu-genai-playbook|Anand-Wu's 2×2]], [[2026-04-28-werner-lebrun-octopus-organization|Werner & Le-Brun's Octopus/Tin-Man]], [[2026-04-28-mit-sloan-ai-maturity|MIT CISR Four Stages + Four S]], [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco's chatbot→agent progression]], and [[2026-04-28-bansal-birkinshaw-systems-thinking|Bansal & Birkinshaw's systems thinking]]. The concept page describes the topical adjacencies without ranking them.
- The article's empirical claim (10–25% EBITDA gains) is from vendor-of-deployment data (Bain). Independent corroboration would come from the [[2026-04-30-ai-index-report-2026|AI Index 2026]]'s 14–26% productivity-gain range in customer support and software development — described as adjacent on each page, no comparative conclusion drawn.
- OpenAI Economic Research team (Chatterji, Weeratunga, Satcher) is the OpenAI counterpart to Anthropic's [[Anthropic Economic Index]] team — described as parallel measurement initiatives without comparative ranking.

**Notable choices:**

- **Date prefix `2026-05-02`** — date-of-ingest (today; the article itself is dated 30 April 2026).
- **New concept page** [[micro-productivity-trap]] rather than just enrichment because the article gives a structural name + four-step framework + EBITDA empirical anchor + worked cases. The page positions itself relative to the wiki's other organizational-frameworks-for-ai-adoption vocabularies without ranking them.
- **Filled in [[OpenAI]] entity** — previously dangling across many references. Now serves as a hub linking GPT-3 (Brynjolfsson), GPT-4 (Dell'Acqua, Boussioux), ChatGPT (Anand-Wu), Mylow (this source), and the OpenAI Economic Research team.
- **[[Aaron Chatterji]]** is the wiki's first cross-org figure (Duke + OpenAI Chief Economist). The OpenAI Economic Research team is now indexed as a wiki-level entity (via OpenAI's entity page).
- Dangling wikilinks left intentionally: [[Chandhu Nair]] (Lowe's SVP) — single-source mention.

**Contradiction check:** no direct contradictions. The 10–25% EBITDA range is consistent with the [[2026-04-30-ai-index-report-2026|AI Index 2026]]'s 14–26% productivity-gain range in customer support and software development (different metric — EBITDA vs productivity gain — but same order of magnitude and same direction). The "micro-productivity trap" diagnostic complements rather than contradicts the wiki's existing org-transformation frameworks.

**Total file touch: 14** (1 source + 5 author entities + 3 org entities + 1 new concept + 3 concept enrichments + index + log; raw PDF on disk under `raw/articles/` but not committed per the gitignore rule).

## [2026-05-03] ingest | Rewired 2nd ed (Lamarre, Smaje, Levin et al., Wiley/McKinsey 2026) — SAMPLE INGEST

**First ingest under the new "Verify before ingest" guardrail in CLAUDE.md.** The raw file (`raw/books/L-0029188561-pdf (1).pdf`) is a **30-page library/OverDrive sample** of a ~600-page book. The TOC references chapters out to page 591+, while the PDF has 30 pages — exactly the scope-mismatch pattern Check 1 of the new guardrail is designed to catch.

User confirmed the sample-only scope is intentionally useful in its own right ("front matter + intro + first 5 manifesto themes is enough; ingest as partial"). Following the FTSG and AI Index 2026 precedents for honestly-scoped partial ingests.

**Pages added:**

- [[2026-05-03-rewired-second-edition-sample]] — source page (clearly scoped; "Scope of this ingest" disclosure section at top; "What was NOT read" listed)
- [[Eric Lamarre]], [[Kate Smaje]], [[Rob Levin]], [[Alex Singla]], [[Alexander Sukharevsky]] — author entities
- [[McKinsey & Company]] — publisher; previously dangling, now filled in. The page also documents McKinsey's role as the data-partner-instrument behind several existing wiki adoption headlines (AI Index, MIT CISR Total AI Effectiveness).

**Pages enriched:**

- [[enterprise-ai-adoption]] — added the McKinsey "Rewired" 6-capability lens alongside the existing Anand-Wu / Werner-Le-Brun / MIT CISR / MITTRI-Cisco / Bain-OpenAI lenses. Includes the 20% EBITDA / $3:$1 / 1–2 yr breakeven / 70% talent-density-shifts numbers, with explicit cross-source comparison to AI Index 2026 (14–26% productivity range) and Bain/OpenAI 2026 (10–25% EBITDA) for independent-magnitude corroboration.
- [[micro-productivity-trap]] — added Rewired row to the cross-source positioning table (now 8 named vocabularies for the same broad "adoption breadth ≠ transformation depth" pattern).
- **Wiki cross-pollination flag**: Rewired's Index references [[Peter Weill]] (book p. 26) and [[Stephanie Woerner]] (book p. 286), both already in the wiki via [[2026-04-28-mit-sloan-ai-maturity|MIT CISR]]. Index lines for both updated to note the citation. This is genuine cross-source linkage — McKinsey's Rewired framework cites MIT CISR's research on technology platforms.

**Index updated** (1 new source line; 7 new entity lines; 2 entity lines amended for Peter Weill / Stephanie Woerner cross-citation).

**Key claims carried into the wiki (sample-scoped):**

- The **6-capability "Rewired" framework** (business-led roadmap, talent, operating model, technology, data, adoption-and-scaling) — companies must be strong across all six.
- **Definition of Tech & AI transformation**: "the process of developing organizational and technology-based capabilities that allow a company to continuously improve its customer experience and lower its unit costs; and over time sustain a competitive advantage."
- **Empirical anchor** (~20 deep-dive AI-leader companies from a study set of ~200): **20% EBITDA uplift average, 1–2 yr breakeven, $3:$1 ROI**, with concentration on **1–3 business domains**.
- **70% talent-density shifts**: 70%+ in-house, 70%+ "doer" engineers, 70%+ at competent-or-expert skill levels.
- **40% of 2nd ed entirely new**, 25% substantially expanded — reflecting the rise of agentic AI and the evolution of management practice.
- **Senior business leaders, not IT, drive transformation**: "We don't have a single success story where senior business leaders were not in the driver's seat."
- **Four case-study companies** named (but content NOT in the sample): DBS Bank, Freeport-McMoRan, LATAM Airlines, Toyota Motor North America.
- **Vocabulary preview** via the back-of-book Index: "domain-to-value delivery (DVD)", "talent win room (TWR)", "tech talent skill pyramid", "two-pizza teams", "stage-gating", "strangler fig", "value driver trees", "70% / 30–70 shifts", "workbenches", "zero-cost thinking", and the operating-model archetypes (digital factory, domain & platform, distributed, enterprise-wide).

**Cross-source notes (descriptive only, per cross-source neutrality preference):**

- The Rewired 6-capability framework adds an **8th named vocabulary** to the wiki's running cluster of "adoption breadth ≠ transformation depth" framings (alongside Anand-Wu 2×2, Werner-Le-Brun Octopus/Tin-Man, MIT CISR Four Stages + Four S, MITTRI/Cisco 5 Foundations, Bansal-Birkinshaw systems thinking, Warner-Wäger dynamic capabilities, Bain/OpenAI micro-productivity-trap). The [[organizational-frameworks-for-ai-adoption]] thread page would be a strong synthesis target now.
- **Three independent magnitude estimates** for AI-transformation EBITDA/productivity gains now in the wiki: McKinsey/Rewired 20% EBITDA, Bain/OpenAI 10–25% EBITDA, AI Index 2026 14–26% productivity. Same direction, similar magnitude, three different vantages (consulting deep-dives × 2, national-survey × 1).
- McKinsey's data-partner role in the AI Index makes this *not quite* an independent voice — the wiki's [[McKinsey & Company]] entity page documents the methodological dependency.

**Notable choices (per new CLAUDE.md guardrail):**

- **Date prefix `2026-05-03`** — date-of-ingest.
- **Frontmatter `length:` is honest**: "~600+ pages full book (read pp. 1–30 of 30-page sample…)". The "Scope of this ingest" section is the FIRST section of the source page, before TL;DR, to make sample-status maximally visible.
- **Frontmatter has `sample_source:` field** — new convention this ingest. Documents the file pattern as an OverDrive-style library sample.
- **Source-page slug includes `-sample`** — explicit signal in the URL/path.
- **No new concept page** for the 6-capability framework. McKinsey-branded vocabulary anchored on a single source warrants enrichment of [[enterprise-ai-adoption]] but not its own concept until corroborated by a second source. (If chapters are read later, the concept could be promoted.)
- **Dangling wikilinks left intentionally**: the case-study companies (DBS Bank, Freeport-McMoRan, LATAM Airlines, Toyota Motor North America) are referenced but not turned into entities — single-source coverage so far, and the chapter content describing them is not yet read.

**Contradiction check:** no direct contradictions. The 20% EBITDA / 14–26% productivity / 10–25% EBITDA cluster is consistent in magnitude. McKinsey's claim about "senior business leaders in the driver's seat" rhymes with Bain/OpenAI's "boardroom imperative" and MIT CISR's "Strategy" pillar of the Four S — same observation in three vocabularies.

**Total file touch: 12** (1 source + 6 entities + 2 concept enrichments + 1 entity index update for Peter Weill + 1 entity index update for Stephanie Woerner [via index.md edits] + index + log; raw PDF on disk under `raw/books/` but not committed per the gitignore rule).

## [2026-05-05] bulk-refactor | v0.2 lifecycle schema + tooling + batch 1

First version of [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md) v0.2 lands: lifecycle metadata (`confidence`, `last_confirmed`, `source_count`), supersession protocol (`status: stale`, `superseded_by`, `supersedes`), and the supporting Quartz extension + lint script.

**Schema changes (`CLAUDE.md`):**

- New §Lifecycle section — frontmatter contract, confidence rules, supersession protocol, debates-and-supersession section requirement, four-tier vocabulary.
- §Ingest step 4 now requires bumping `last_confirmed` and recomputing `source_count`/`confidence` on every touched concept/entity page.
- §Ingest step 7 rewritten to specify the supersession write-back (set `supersedes:` on new source; set `status: stale` + `superseded_by:` on retired page; never delete).
- "Custom extensions" list extended with `inject-stale-banner.ts`.
- "Current state" section refreshed to reflect actual repo state (was stale: claimed wiki not yet instantiated).
- "Reference" section now lists v1, v2, and the v2 staged plan.

**New files:**

- `extensions/inject-stale-banner.ts` — Quartz transformer; when frontmatter has `status: stale`, prepends an Obsidian-style `[!warning]` callout linking to `superseded_by`. Inserted in `quartz.config.ts` after `InjectTypeTags()`.
- `scripts/lint-confidence.mjs` — read-only walker; prints confidence distribution, flags pages missing v0.2 fields, flags pages with `last_confirmed > 30 days`, lists stale pages.
- Created `scripts/` directory.

**Migration batch 1 (10 pages of 71):**

| Page | confidence | last_confirmed | source_count |
|---|---|---|---|
| `concepts/automation-vs-augmentation.md` | 0.95 | 2026-05-02 | 10 |
| `concepts/enterprise-ai-adoption.md` | 0.95 | 2026-05-03 | 15 |
| `concepts/ai-employment-effects.md` | 0.95 | 2026-04-30 | 10 |
| `concepts/jagged-frontier.md` | 0.90 | 2026-04-30 | 5 |
| `concepts/lean-4-0.md` | 0.70 | 2026-04-28 | 3 |
| `entities/Erik Brynjolfsson.md` | 0.85 | 2026-04-28 | 3 |
| `entities/Anthropic.md` | 0.75 | 2026-04-28 | 2 |
| `entities/MIT CISR.md` | 0.75 | 2026-04-28 | 1 |
| `entities/Bain & Company.md` | 0.70 | 2026-05-02 | 1 |
| `entities/Lowe's.md` | 0.70 | 2026-05-02 | 1 |

Distribution: 5 pages at 0.85–1.0, 5 pages at 0.70–0.85. No defaults left at 0.0. Values set per the §Lifecycle confidence rules: 0.7 baseline + 0.05 per additional source (cap 0.95) + 0.05 once for peer-reviewed/empirical sources; vendor/single-case-study capped at 0.75.

**Reversibility:** all changes are additive frontmatter on existing pages plus three new files. To revert v0.2 entirely: remove the new frontmatter fields from the 10 migrated pages (`git diff main` would isolate them), revert `quartz.config.ts` and `CLAUDE.md`, delete `extensions/inject-stale-banner.ts`, `scripts/lint-confidence.mjs`, and `scripts/`. No source-page or content edits.

**Verification:**

- `node scripts/lint-confidence.mjs` — 71 → 61 pages missing fields; distribution 5 in 0.7–0.85, 5 in 0.85–1.0.
- `npm run build` — 95 input files, 653 emitted, no errors.
- Stale-banner extension: registered, no-op against current corpus (no page has `status: stale` yet).

**Total file touch: 14** (1 CLAUDE.md + 1 quartz.config.ts + 1 new extension + 1 new script + 5 concept pages + 5 entity pages + log).

61 pages still pending (12 concepts + 49 entities). Batch 2 will follow once batch 1 values are sanity-checked.

## [2026-05-05] bulk-refactor | v0.2 lifecycle migration batch 2

Second batch of v0.2 lifecycle migration (10 high-frequency hubs).

| Page | confidence | last_confirmed | source_count |
|---|---|---|---|
| `concepts/ai-agents.md` | 0.85 | 2026-04-28 | 4 |
| `concepts/generative-ai.md` | 0.95 | 2026-05-02 | 11 |
| `concepts/foundation-models.md` | 0.80 | 2026-04-30 | 2 |
| `concepts/responsible-ai.md` | 0.95 | 2026-04-30 | 6 |
| `concepts/dynamic-capabilities.md` | 0.90 | 2026-04-28 | 4 |
| `entities/Stanford HAI.md` | 0.80 | 2026-04-30 | 2 |
| `entities/OpenAI.md` | 0.85 | 2026-05-02 | 7 |
| `entities/McKinsey & Company.md` | 0.85 | 2026-05-03 | 4 |
| `entities/Boston Consulting Group.md` | 0.75 | 2026-04-28 | 1 |
| `entities/MIT Technology Review Insights.md` | 0.70 | 2026-04-28 | 1 |

After batch 2: 20/71 pages migrated. Distribution skews to high-confidence (11 at 0.85–1.0, 9 at 0.70–0.85), reflecting that batches 1–2 were chosen to be diverse-but-well-connected hubs. Single-source entities still cluster around 0.70–0.75 per the §Lifecycle vendor/single-source rule.

**Verification.** `node scripts/lint-confidence.mjs` → 51 pages still missing fields. `npm run build` clean (95 in, 653 out, no errors).

**Reversibility:** additive-frontmatter only.

51 pages still pending (7 concepts + 44 entities).

## [2026-05-05] bulk-refactor | v0.2 lifecycle migration batch 3

| Page | confidence | last_confirmed | source_count |
|---|---|---|---|
| `concepts/ai-benchmarks.md` | 0.85 | 2026-04-30 | 3 |
| `concepts/ai-deskilling.md` | 0.70 | 2026-04-28 | 1 |
| `concepts/industry-4-0.md` | 0.85 | 2026-04-28 | 4 |
| `concepts/micro-productivity-trap.md` | 0.70 | 2026-05-02 | 1 |
| `concepts/strategic-foresight.md` | 0.75 | 2026-04-28 | 2 |
| `entities/AI Index.md` | 0.85 | 2026-04-30 | 2 |
| `entities/Anthropic Economic Index.md` | 0.75 | 2026-04-28 | 2 |
| `entities/Future Today Strategy Group.md` | 0.70 | 2026-04-28 | 2 |
| `entities/Harvard Business Review.md` | 0.85 | 2026-05-02 | 6 |
| `entities/Stanford Digital Economy Lab.md` | 0.75 | 2026-04-28 | 1 |

After batch 3: 30/71 pages migrated. Distribution stable: 15 at 0.85–1.0, 15 at 0.70–0.85. Three single-source concepts (`ai-deskilling`, `micro-productivity-trap`, plus `lean-4-0` from batch 1) and three same-firm-cluster sources (FTSG/Webb counts as one author voice for confidence purposes) all sit at 0.70 — the floor on the §Lifecycle scale for a live page.

`npm run build` clean (95 in, 653 out). Lint: 41 pages still missing fields (2 concepts + 39 entities).

**Reversibility:** additive-frontmatter only.

## [2026-05-05] bulk-refactor | v0.2 lifecycle migration batch 4

| Page | confidence | last_confirmed | source_count |
|---|---|---|---|
| `concepts/analogical-reasoning.md` | 0.75 | 2026-04-28 | 1 |
| `concepts/systems-thinking.md` | 0.75 | 2026-04-28 | 1 |
| `entities/Cisco.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Amy Webb.md` | 0.75 | 2026-04-28 | 2 |
| `entities/Amazon Web Services.md` | 0.80 | 2026-04-28 | 2 |
| `entities/Fabrizio Dell'Acqua.md` | 0.75 | 2026-04-28 | 1 |
| `entities/Ethan Mollick.md` | 0.75 | 2026-04-28 | 1 |
| `entities/Karim Lakhani.md` | 0.75 | 2026-04-28 | 1 |
| `entities/METR.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Aaron Chatterji.md` | 0.70 | 2026-05-02 | 1 |

After batch 4: **40/71 pages migrated. All 17 concepts complete.** Remaining pool is 31 entities, mostly single-source author pages.

**Reversibility:** additive-frontmatter only.

## [2026-05-05] bulk-refactor | v0.2 lifecycle migration batches 5–7 (close-out)

Final 31 entities migrated in three batches. All single-source author/organization pages; values determined by source kind (peer-reviewed academic = 0.75; HBR practitioner / vendor / single-case = 0.70).

### Batch 5 (entities 41–50)

| Page | confidence | last_confirmed | source_count |
|---|---|---|---|
| `entities/Alex Singla.md` | 0.70 | 2026-05-03 | 1 |
| `entities/Alexander Sukharevsky.md` | 0.70 | 2026-05-03 | 1 |
| `entities/Andy Wu.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Arjun Dutt.md` | 0.70 | 2026-05-02 | 1 |
| `entities/Bharat N. Anand.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Continuum Laboratory.md` | 0.75 | 2026-04-29 | 1 |
| `entities/Eric Lamarre.md` | 0.70 | 2026-05-03 | 1 |
| `entities/Gawesha Weeratunga.md` | 0.70 | 2026-05-02 | 1 |
| `entities/Gene Rapoport.md` | 0.70 | 2026-05-02 | 1 |
| `entities/Glenn R. Carroll.md` | 0.75 | 2026-04-28 | 1 |

### Batch 6 (entities 51–60)

| Page | confidence | last_confirmed | source_count |
|---|---|---|---|
| `entities/Harrison Satcher.md` | 0.70 | 2026-05-02 | 1 |
| `entities/Ivey Business School.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Jacqueline N. Lane.md` | 0.75 | 2026-04-29 | 1 |
| `entities/Jesper B. Sorensen.md` | 0.75 | 2026-04-28 | 1 |
| `entities/John Higgins.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Julian Birkinshaw.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Karl S.R. Warner.md` | 0.75 | 2026-04-28 | 1 |
| `entities/Kate Smaje.md` | 0.70 | 2026-05-03 | 1 |
| `entities/Leonard Boussioux.md` | 0.75 | 2026-04-29 | 1 |
| `entities/Maximilian Wager.md` | 0.75 | 2026-04-28 | 1 |

### Batch 7 (entities 61–71, final)

| Page | confidence | last_confirmed | source_count |
|---|---|---|---|
| `entities/Megan Reitz.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Miaomiao Zhang.md` | 0.75 | 2026-04-29 | 1 |
| `entities/Nestor Maslej.md` | 0.75 | 2026-04-30 | 2 |
| `entities/Peter Weill.md` | 0.75 | 2026-05-03 | 2 |
| `entities/Rob Levin.md` | 0.70 | 2026-05-03 | 1 |
| `entities/Schmidt Sciences.md` | 0.70 | 2026-04-30 | 1 |
| `entities/Sha Sajadieh.md` | 0.70 | 2026-04-30 | 1 |
| `entities/Stephanie Woerner.md` | 0.75 | 2026-05-03 | 2 |
| `entities/Tima Bansal.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Vladimir Jacimovic.md` | 0.75 | 2026-04-29 | 1 |
| `entities/Yolanda Gil.md` | 0.80 | 2026-04-30 | 2 |

### v0.2 final state

**71/71 pages migrated.** Final lint output:

- `confidence` distribution: 56 pages at 0.70–0.85, 15 pages at 0.85–1.0, 0 below 0.70, 0 missing.
- 0 pages with `last_confirmed > 30 days` (all dates ≥ 2026-04-28, today is 2026-05-05).
- 0 pages marked `status: stale` (no supersession events triggered yet).

Lint script now exits 0 — the v0.2 lifecycle invariant holds. This becomes the pre-commit check contract for the v0.4 PostToolUse hook.

**The distribution shape** is informative: high-confidence (0.85–1.0) clusters are the well-substantiated *concept hubs* (`enterprise-ai-adoption`, `generative-ai`, `automation-vs-augmentation`, `ai-employment-effects`, `responsible-ai`); the long mid-confidence tail (0.70–0.85) is dominated by *single-source author/organization entities* — the natural shape of a wiki where most entities first appear via one substantiating ingest. As more sources land, those 0.70–0.75 entities will get nudged up by the "+0.05 per additional source" rule in §Lifecycle.

**Build:** `npm run build` clean (95 in, 653 out, no errors).

**Reversibility:** additive-frontmatter only across all 71 pages. Schema additions in [`CLAUDE.md`](../CLAUDE.md), [`quartz.config.ts`](../quartz.config.ts), one new extension ([`extensions/inject-stale-banner.ts`](../extensions/inject-stale-banner.ts)), one new script ([`scripts/lint-confidence.mjs`](../scripts/lint-confidence.mjs)), and the new `bulk-refactor` log op are reversible by removing the additions and reverting the two config files. No source-page or content edits.

v0.2 complete. Next version per [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md): v0.3 (typed entity graph + synthesis contract).
