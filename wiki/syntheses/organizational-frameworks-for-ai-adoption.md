---
type: synthesis
aliases: ["organizational frameworks for AI adoption synthesis", "AI adoption frameworks synthesis"]
tags: [enterprise-ai-adoption, organizational-frameworks, synthesis, cross-source-comparison, decision-tree]
derived_from: [organizational-frameworks-for-ai-adoption]
opened: 2026-04-28
closed: 2026-05-05
confidence: 0.90
last_confirmed: "2026-05-05"
source_count: 6
relationships:
  - type: instance-of
    target: enterprise-ai-adoption
    via: "synthesizes 6 frameworks describing different decision layers within enterprise AI adoption"
  - type: supports
    target: micro-productivity-trap
    via: "the layered framing makes the trap legible — most failures are layer mismatches"
---

# Synthesis: Organizational frameworks for AI adoption

Closes [[threads/organizational-frameworks-for-ai-adoption|organizational-frameworks-for-ai-adoption]]. Six frameworks have now been ingested describing how organizations should think about AI adoption — the original four ([[2026-04-28-mit-sloan-ai-maturity|MIT CISR]], [[2026-04-28-anand-wu-genai-playbook|Anand-Wu]], [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]], [[2026-04-28-werner-lebrun-octopus-organization|Werner-Le-Brun]]) plus two added since the thread opened ([[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Bain/OpenAI]] and [[2026-05-03-rewired-second-edition-sample|McKinsey *Rewired* 2nd ed]]). Closes per the thread's stated trigger ("when a 5th or 6th comparable framework appears").

## Question

When advising an executive on enterprise AI adoption, which framework should inform which decision — and where do they genuinely disagree rather than say the same thing in different vocabulary?

## Findings

### The frameworks operate on different layers

The six frameworks are **mostly complementary, not competing**. Each names a different layer of AI-adoption decision-making, with overlap rather than conflict. Stack them top-down:

| Layer | Framework | Question it answers | Source |
| ----- | --------- | ------------------- | ------ |
| **Org-design** | Tin Man / Octopus | Is your organization structurally capable of adapting? | [[2026-04-28-werner-lebrun-octopus-organization\|Werner-Le-Brun]] |
| **Readiness** | Cisco 5 Foundations (Strategy / Infrastructure / Data / Governance / Culture) | Do you have the prerequisites? | [[2026-04-28-mittri-cisco-ai-enabled-enterprise\|MITTRI/Cisco]] |
| **Capability progression** | MIT CISR Four Stages + Four S | What stage are you at, and what blocks the next transition? | [[2026-04-28-mit-sloan-ai-maturity\|MIT CISR]] |
| **Transformation playbook** | McKinsey *Rewired* 6 capabilities | How do you actually execute the journey? | [[2026-05-03-rewired-second-edition-sample\|Lamarre, Smaje, Levin et al. 2026]] |
| **Trap escape** | Bain/OpenAI 4-step transformation | How do you avoid the [[micro-productivity-trap]]? | [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation\|Dutt, Chatterji et al. 2026]] |
| **Task deployment** | Anand-Wu 2×2 (cost of errors × type of knowledge) | For *this specific task*, deploy AI today and how? | [[2026-04-28-anand-wu-genai-playbook\|Anand-Wu]] |
| **Diagnostic** | Anand-Wu 6 leakage points | If gains aren't showing up in P&L, where are they leaking? | [[2026-04-28-anand-wu-genai-playbook\|Anand-Wu]] |

### A decision tree for which framework to use

Sequenced by the typical executive question:

1. **"Are we organizationally capable of changing?"** → Werner-Le-Brun (Tin Man vs Octopus). If you're a Tin Man, lower frameworks won't stick.
2. **"Do we have the foundations?"** → Cisco 5 Foundations. Infrastructure, data, governance must clear a bar before pilots scale.
3. **"Where are we in the maturity curve?"** → MIT CISR Four Stages. Locate your stage; the Four S diagnostic identifies what blocks the next transition. *The financial inflection sits specifically at Stage 2 → Stage 3.*
4. **"What's our transformation playbook?"** → McKinsey *Rewired* 6 capabilities (business-led roadmap, talent, operating model, technology, data, adoption-and-scaling). Anchor: ~20% EBITDA uplift, $3:$1 ROI, 1–2yr breakeven across deep-dive AI-leader companies.
5. **"How do we avoid the common failure mode?"** → Bain/OpenAI 4-step (narrow possibilities; reimagine workflows; engage those closest to the process; measure outcomes plus evals). Names the trap (offering lock-in / process lock-in) explicitly. Anchor: 10–25% EBITDA gains.
6. **"Which task do we point AI at first?"** → Anand-Wu 2×2. *No regrets zone* (low cost of errors / explicit data) is where to start; agents thrive there today.
7. **"Why isn't our investment paying off in P&L?"** → Anand-Wu 6 leakage points. Diagnostic, not prescriptive. Trace which of the 6 points is leaking.

### Where they genuinely disagree

Most apparent disagreements are vocabulary differences, but a few real splits:

- **Stage 2 → Stage 3 financial inflection (MIT CISR-specific).** MIT CISR claims firms in Stages 1–2 underperform their industry; Stages 3–4 outperform. The other frameworks don't make this stage-gradient claim — they describe the *destination* of transformation but not where the inflection lives. **If true, the inflection is the most actionable framing.**
- **"Reinvent the business" vs. incremental capability building.** McKinsey *Rewired* and Bain/OpenAI both push *aggressive* posture: process redesign first, technology second; business-led, not IT-led; "we don't have a single success story where senior business leaders weren't in the driver's seat." MIT CISR is more incremental — the Four Stages permit gradual progression. The Bain/OpenAI thesis explicitly contradicts the incremental approach by naming the [[micro-productivity-trap]] (offering lock-in, process lock-in).
- **Org-design as upstream prerequisite (Werner-Le-Brun) vs. downstream outcome.** Tin Man / Octopus treats org structure as the precondition for AI adoption to work. The other frameworks largely assume the org can act, then prescribe what to do. If Werner-Le-Brun is right, frameworks 2–7 may not stick on a Tin Man without org-design work first.
- **Pilots as a stage (MIT CISR) vs. pilots as a trap (Bain/OpenAI).** MIT CISR Stage 2 ("Build pilots and capabilities") frames piloting as a needed phase. Bain/OpenAI argue most companies *get stuck* in pilots — exactly because they don't reimagine workflows. Same observation, opposite valence.

### Cross-framework agreement

All six converge on a few claims, with different vocabularies:

- **Adoption breadth ≠ transformation depth.** AI Index pegs maturity at 1%; MIT CISR pegs Stage 4 at 7%; Cisco pegs ready at 13%; Werner-Le-Brun's 12% transformation-success baseline. Same diagnostic, four numbers. See [[ai-maturity-measurement-comparison]].
- **Process redesign is the main cost, not technology.** Bain/OpenAI: "process redesign is the most challenging part of AI deployment and creates most of the value." McKinsey *Rewired*: "business-led roadmap" and "operating model" are 2 of the 6 capabilities. MIT CISR Four S "Synchronization" is reskilling and role redesign. Anand-Wu 2×2's strategic value comes from picking the *right tasks*, not the technology.
- **Senior-leader ownership is non-negotiable.** McKinsey: "We don't have a single success story where senior business leaders were not in the driver's seat." Bain/OpenAI: "boardroom imperative." MIT CISR: united front of CEO / CIO / CSO / Head of HR. Cisco: "Strategy" pillar means top-down. Werner-Le-Brun: org-design ownership at C-level.
- **Talent density shifts over hiring breadth.** McKinsey *Rewired*'s 70% benchmarks (70%+ in-house, 70%+ "doer" engineers, 70%+ at competent-or-expert skill levels) — distinctive but consistent in spirit with MIT CISR's "Synchronization" and Cisco's "Culture and Talent."
- **Most enterprise tasks today are augmentative, not automative.** Anand-Wu's "no regrets zone" (where agents thrive) is the *minority* of business tasks. MITTRI/Cisco's chatbot → agent → multi-agent progression places multi-agent as future-state. The empirical record ([[2026-04-30-ai-index-report-2026|AI Index 2026]]) confirms: agent deployment in single digits across nearly all business functions.

### Where empirical validation is missing

Of the six frameworks:

| Framework | Empirical anchor |
| --------- | ---------------- |
| MIT CISR Four Stages | **2022 Future Ready Survey, N=721** — 28%/34%/31%/7% distribution (pre-GenAI baseline) |
| Anand-Wu 2×2 | Conceptual framework; cited prior tech cycles (e-ticketing, CAD/ERP, Big Law) but no per-quadrant empirical baseline |
| Cisco 5 Foundations | Cisco's own 2025 readiness survey; vendor-instrument data, methodology not fully disclosed |
| Werner-Le-Brun Octopus | Case examples (Netflix, Google, Coca-Cola, U.S. Army); no distributional data; AWS-affiliated authorship |
| McKinsey *Rewired* | ~20 deep-dive AI-leader companies (selected from ~200 study set); 20% EBITDA uplift; **vendor-of-deployment data — selection-effect-aware** |
| Bain/OpenAI 4-step | Bain client work; 10–25% EBITDA gains; **vendor-of-deployment data — selection-effect-aware** |

**Only MIT CISR has an N>500 representative-sample distribution** — and that baseline is now 4 years old, predating the GenAI explosion. The other five frameworks are prescriptive without distributional grounding. The two consulting-firm frameworks (McKinsey *Rewired*, Bain/OpenAI) carry the same magnitude of EBITDA claim (10–25% range) but from selected case work, not representative samples. Cross-validation between them strengthens magnitude confidence somewhat — see [[enterprise-ai-adoption]] *Six-capability lens* note on the McKinsey methodological dependency in the [[AI Index]].

## Sources consulted

- [[2026-04-28-mit-sloan-ai-maturity]] — Burnham (2025) reporting on Woerner, Weill, Sebastian, Káganer at [[MIT CISR]]. Four Stages + Four S; the only framework with a representative-sample distribution.
- [[2026-04-28-anand-wu-genai-playbook]] — Anand & Wu (HBR Nov–Dec 2025). 2×2 task framework + 6 leakage points; paradox-of-access argument.
- [[2026-04-28-mittri-cisco-ai-enabled-enterprise]] — MIT Tech Review Insights × [[Cisco]] (2025). 5 Foundations + chatbot → agent → multi-agent progression.
- [[2026-04-28-werner-lebrun-octopus-organization]] — Werner & Le-Brun (HBR Nov–Dec 2025). Tin Man / Octopus archetypes; AWS Executives in Residence.
- [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation]] — [[Bain & Company]] + [[OpenAI]] Economic Research (HBR.org, 30 Apr 2026). 4-step transformation framework; names the [[micro-productivity-trap]].
- [[2026-05-03-rewired-second-edition-sample]] — Lamarre, Smaje, Levin et al. (Wiley/[[McKinsey & Company]] 2026, sample-only). 6-capability framework; 70% talent-density shifts; 20% EBITDA uplift.

## Lessons

- **Pick a framework by the executive's question, not the framework's brand.** Each framework names a different layer; mismatched layers explain most "why didn't this work" stories.
- **The transformation-mindset frameworks (McKinsey *Rewired*, Bain/OpenAI) and the maturity-progression framework (MIT CISR) sit in tension on pilot stages.** *Rewired* and Bain treat pilots-as-trap; MIT CISR treats pilots-as-stage. Reconcile by treating MIT CISR's Stage 2 as a phase to pass through quickly, not dwell in.
- **Process redesign is the load-bearing decision across all 6 frameworks.** If your AI program treats redesign as something the technology team handles, it will land on the wrong side of the [[micro-productivity-trap]] regardless of which framework you cite.
- **Empirical maturity distributions older than 2024 are increasingly stale.** The MIT CISR 2022 baseline is the only non-vendor data point in this set, and the GenAI explosion may have shifted distributions substantially. Treat as load-bearing for *which* failure modes are common — but don't read 28%/34%/31%/7% as current.

## Open questions

- **No empirical validation of Anand-Wu, Cisco, Werner-Le-Brun, McKinsey *Rewired*, or Bain/OpenAI against a representative sample.** The prescriptive value is high; the distributional grounding is thin. A Gartner or Deloitte cross-walk with N>500 would substantially strengthen the cluster.
- **MIT CISR Stage distribution post-GenAI.** The 2022 baseline is now 4 years old. A 2025 or 2026 wave would tell us whether GenAI moved the median firm up the maturity ladder, or whether the distribution has stretched (Stage 4 firms pulled away while Stage 1 firms got stuck).
- **Whether the 6 frameworks converge on the same recommendation when applied to a specific firm.** The decision-tree above is a hypothesis. A worked example — pick a real firm, run all 6 frameworks against it, compare the prescriptions — would test the "complementary not competing" claim.
- **Cross-walk with academic strategy theory.** None of the 6 frameworks engage with [[dynamic-capabilities]] (Teece), [[systems-thinking]], or [[strategic-foresight]] explicitly. The wiki's existing concept pages already provide the bridges; a follow-up synthesis could integrate them.

## Related pages

- [[enterprise-ai-adoption]] — main concept page; the 6 frameworks all live here in summary form
- [[micro-productivity-trap]] — named failure mode that the trap-escape framework targets
- [[ai-maturity-measurement-comparison]] — sister thread (still open) on the *measurement* side; the 1% / 7% / 12% / 13% maturity spread
- [[automation-vs-augmentation]] — load-bearing distinction inside Anand-Wu's 2×2 quadrants
- [[dynamic-capabilities]] — academic-strategy bridge that none of the 6 frameworks engage with directly
