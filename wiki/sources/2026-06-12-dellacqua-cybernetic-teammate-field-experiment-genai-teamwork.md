---
type: source
kind: paper
title: "The Cybernetic Teammate: A Field Experiment on Generative AI and Teamwork"
author: ["Fabrizio Dell'Acqua", "Charles Ayoubi", "Hila Lifshitz", "Raffaella Sadun", "Ethan Mollick", "Lilach Mollick", "Yi Han", "Jeff Goldman", "Hari Nair", "Stew Taub", "Karim R. Lakhani"]
publisher: "Organization Science 37(4):1217–1242 (July–August 2026), INFORMS; Harvard Business School / HBS AI Institute, ESSEC, Warwick Business School, The Wharton School, and Procter & Gamble. Preregistered. CC BY 4.0"
url: "https://doi.org/10.1287/orsc.2025.20702"
date_published: 2026-06-12
date_ingested: 2026-09-15
length: "~26 pages (full text read: abstract, §1 introduction, §5 results incl. Tables/Figures 9–11, §6 discussion with caveats and scope conditions, §7 conclusion; appendix and reference list skimmed)"
raw: "../../raw/papers/cybernetic-teammate-field-experiment-generative-ai-teamwork.md"
tags: [cybernetic-teammate, dellacqua, lakhani, ethan-mollick, sadun, procter-and-gamble, field-experiment, preregistered, randomised-controlled-trial, teamwork, functional-silos, boundary-spanning, expertise-integration, new-product-development, innovation, perception-gap, top-decile, emotional-response, flash-teams, organization-science, peer-reviewed]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-seizing/rapid-prototyping
  - strategic-renewal/collaborative-approach
relationships:
  - type: supports
    target: 2026-04-28-dellacqua-jagged-technological-frontier
    via: "the same first author and overlapping team, two experiments apart. The BCG study measured *individuals* against a jagged capability boundary; this measures *teams*, and the papers cite each other's construct — the discussion names 'whether [humans' mental models] track the technology's jagged capabilities (Dell'Acqua et al. 2023)' as an open frontier. Read as a pair they are the corpus's strongest single line of field-experimental evidence on GenAI and knowledge work"
    confidence: 0.9
  - type: contradicts
    target: 2025-07-10-becker-metr-early-2025-ai-experienced-developer-productivity
    via: "not on the direction of the productivity effect but on the **sign of the perception gap**, which the wiki had treated as settled. METR's developers were slowed 19% and believed they had been sped up 20%. Here the gap inverts: AI users performed measurably *better* (+0.37 SD) and were **9.2 percentage points less likely** to expect a top-10% placement (p<0.05) — objectively better, subjectively less confident. Any claim that self-report is biased in a consistent direction now has a counter-example in a preregistered 791-person experiment"
    confidence: 0.8
  - type: supports
    target: 2026-02-27-cui-demirer-generative-ai-high-skilled-work-three-field-experiments
    via: "two large-N field experiments on high-skilled knowledge work reaching compatible conclusions about where the gains land. Cui et al. find the largest gains among juniors — where the marginal work is acquiring context; this finds AI substituting for the *cross-functional* context a teammate would have supplied, which is the same mechanism read at the team rather than the seniority level"
    confidence: 0.75
  - type: supports
    target: 2026-06-16-mollick-simon-sinek-ai-skills-experience-edge
    via: "the underlying study behind a claim [[Ethan Mollick]] — a co-author here — makes for a general audience. His 'evaluation, not generation, is the bottleneck' line is this paper's decomposition finding stated without the numbers: AI 'primarily enhances the quality of generated ideas, shifting the distribution of creative output upward, whereas human judgment retains value in evaluative selection'"
    confidence: 0.8
  - type: supports
    target: 2025-07-02-joshi-venkatraman-fowler-expert-generalists
    via: "field-experimental support for a thesis the corpus held only as practitioner argument. Thoughtworks argues organisations over-value narrow specialists; this shows AI mechanically produces the generalist output — R&D professionals stopped producing predominantly technical solutions and commercial professionals stopped producing predominantly commercial ones, converging on balanced proposals regardless of background"
    confidence: 0.75
---

# Dell'Acqua et al. — The Cybernetic Teammate (Organization Science, 2026)

**The strongest source in the corpus on what generative AI does to *teams*** — a **preregistered 2×2 field experiment with 791 professionals at Procter & Gamble**, published in *Organization Science* and licensed CC BY. Eleven authors across Harvard Business School's AI Institute, ESSEC, Warwick, Wharton and P&G itself, with **[[Fabrizio Dell'Acqua]]** first, **[[Ethan Mollick]]** and **[[Karim Lakhani]]** among them.

It is the sequel to the [[2026-04-28-dellacqua-jagged-technological-frontier|BCG jagged-frontier study]] the wiki already holds, and it answers a different question: not *how well does an individual do with AI*, but **can AI stand in for a teammate**.

## TL;DR

> *"Individuals with AI matched the performance of teams without AI, suggesting that AI can effectively replicate certain benefits of human collaboration."* — Abstract

The design is unusually clean for organisational research, and the wiki should say so plainly: **randomised, preregistered, real business problems from participants' own units, a full working day of effort, professional stakes** (the best proposals went to business-unit leaders, and the best ideas entered P&G's actual innovation pipeline), and **evaluation by multiple independent assessors under a protocol validated by P&G managers**. Four arms: individual alone, human pair, individual + GenAI, human pair + GenAI. Every pair was one commercial professional and one R&D professional, so cross-functional collaboration was structural rather than incidental.

## The four results

**1. AI substitutes for a teammate — and the second human adds almost nothing on top.**

| Condition | Effect vs. individual working alone |
| --- | --- |
| Team, no AI | **+0.24 SD** (~6.3%), p<0.05 |
| Individual + AI | **+0.37 SD** (~9.6%), p<0.01 |
| Team + AI | **+0.39 SD** (~10.2%), p<0.01 — *not significantly different from individual + AI* |

The authors read this as **diminishing marginal returns to team expansion** once AI is present: going individual → dyad → AI-augmented individual → AI-augmented dyad is a sequential head-count expansion, and the fourth step buys nothing on the average. Their own gloss is worth keeping: AI's effect *"appears to stem more from its capacity to bolster individual cognitive capabilities than affecting human-to-human collaboration."*

Two readings the corpus should hold alongside this. [[2026-02-27-cui-demirer-generative-ai-high-skilled-work-three-field-experiments|Cui et al.]] find the largest gains among juniors, where the marginal work is acquiring context — and what AI substitutes for here is precisely context the *other* professional would have supplied, so the two results are the same mechanism read at the seniority and the cross-functional level. And the silo result below is the [[2025-07-02-joshi-venkatraman-fowler-expert-generalists|expert-generalist]] thesis produced mechanically rather than cultivated.

**2. AI dissolves functional silos — the finding the authors call their most noteworthy.** Without AI, the silos are visible in the output: commercial professionals submitted predominantly commercial solutions, R&D professionals predominantly technical ones. Pairing a commercial with an R&D professional produced balanced solutions — that is what cross-functional teams are *for*. **Individuals using AI achieved the same balance alone.** AI acts *"not just as an information provider but as an effective boundary-spanning mechanism."*

**3. The emotional result, which is the one most likely to be dismissed and probably shouldn't be.** Positive emotions rose **+0.457 SD** for individuals with AI and **+0.635 SD** for teams with AI (both p<0.01); negative emotions fell. The mechanism proposed is the language interface itself — an LLM *"trained on human language and often act[ing] more like a person than a machine"* fills part of the social and motivational role of a human teammate. The wiki should hold this as *self-reported affect*, which is what it is, but note that it is measured under randomisation.

**4. Breakthroughs need the pair *and* the AI.** On a binary *Top 10% Solutions* measure, **Team + AI were 9.2 percentage points more likely** to land in the top decile against a control mean of **5.8%** — roughly **three times** the rate. Individuals with AI showed a small, **statistically insignificant** effect. So the average-performance story (where the second human is redundant) and the tail story (where the second human is decisive) point in opposite directions. If an organisation cares about exceptional outcomes rather than mean quality, the pair still earns its cost.

## The perception gap, inverted

The single most important thing this paper does for this wiki. Participants using AI were **9.2 percentage points less likely** to expect their solution to place in the top 10% (p<0.05) — *while objectively performing better*.

The corpus's standing claim, from [[2025-07-10-becker-metr-early-2025-ai-experienced-developer-productivity|METR]], is that developers slowed 19% believed they had been sped up 20%, and that the survey instrument most organisations use is therefore invalid. That finding stands. But the inference many readers draw from it — *self-report is inflated by AI use* — does not survive this paper. Here the bias runs the other way, in a larger, preregistered sample. **The transferable claim is narrower than the wiki has been stating it: self-assessment is decoupled from performance under AI, in a direction that is not predictable from the technology alone.** Recorded on [[ai-coding-productivity-evidence]].

## Where the human stays

The decomposition analysis splits the innovation process and finds AI *"primarily enhances the quality of generated ideas, shifting the distribution of creative output upward, whereas human judgment retains value in evaluative selection."* Generation improves; selection does not. That is the evidentiary basis for the claim [[Ethan Mollick]] makes without numbers in [[2026-06-16-mollick-simon-sinek-ai-skills-experience-edge|his Sinek interview]] — evaluation, not generation, is the bottleneck.

A second detail worth keeping: the **AI-content retention analysis is polarised**, with a non-trivial share of participants retaining *zero* AI-generated sentences. Two distinct usage styles — AI as ghostwriter, and AI as sounding board — both inside the treatment arm. Averaged treatment effects hide that.

## Dynamic capabilities (Warner & Wäger)

- **`digital-transforming/redesigning-internal-structures`** — the paper's own stated implication: *"organizations may need to reevaluate optimal team sizes and compositions."* It is a measurement of whether a structural unit (the cross-functional dyad) is still load-bearing, which is exactly a redesign question.
- **`digital-seizing/rapid-prototyping`** — the experimental task *is* early-stage new product development, run as a one-day flash-team sprint that mirrors P&G's real ideation routine; the finding is about how fast an organisation can generate and screen viable product concepts.
- **`strategic-renewal/collaborative-approach`** — the silo-dissolution result is a claim about how expertise circulates across functional boundaries, which is the collaborative-approach cell read at the knowledge level rather than the partnership level.

## Linked entities and concepts

- Concepts: [[ai-coding-productivity-evidence]], [[jagged-frontier]], [[automation-vs-augmentation]], [[expert-generalist]], [[enterprise-ai-adoption]], [[durable-skills]], [[ai-employment-effects]]
- Entities: [[Fabrizio Dell'Acqua]], [[Ethan Mollick]], [[Karim Lakhani]]
- **Dangling** (single-source mention, deferred): Charles Ayoubi, Hila Lifshitz, Raffaella Sadun, Lilach Mollick, Yi Han, Jeff Goldman, Hari Nair, Stew Taub, Procter & Gamble, Harvard Business School, ESSEC Business School, Warwick Business School, The Wharton School, Organization Science, INFORMS

## Scope and reliability

**The highest evidential tier the wiki holds**: peer-reviewed, preregistered, randomised, N=791, real tasks with real stakes, independent evaluation, open access. Cite it for magnitudes, not just framing.

The authors' own limits, stated rather than buried — and they cut both ways:

- **The effects are probably a lower bound.** Participants were *"relatively inexperienced with AI prompting techniques"*, and the tools were not built for collaborative work.
- **One day, one company, one industry, one model.** Virtual collaboration between *largely unfamiliar* participants — the authors explicitly call these **flash teams**, not established teams with embedded relationships. Extended coordination and iterative rework cycles are absent by construction. Consumer packaged goods, early-stage NPD only.
- **Cross-functional pairs only.** Same-expertise pairs and larger teams may behave differently, and the paper does not test them.
- **A single AI model at a point in time.**

The practical consequence: **the "AI replaces a teammate" headline is an artifact of a one-day flash team as much as of AI.** What a human teammate contributes over weeks — relationship, memory, rework, disagreement that survives a night's sleep — is not what this experiment could measure.

## Debates and supersession

- **The perception gap is no longer a one-directional finding.** See above; this page and [[2025-07-10-becker-metr-early-2025-ai-experienced-developer-productivity|METR]] are both correct and point opposite ways, so the wiki now holds *decoupling* rather than *inflation*.
- **Average versus tail is an unresolved design question.** Individual + AI matches Team + AI on the mean and loses badly on the top decile (insignificant vs. 3×). An organisation optimising for throughput and one optimising for breakthroughs should read this paper differently, and the paper does not adjudicate.
- **Does boundary-spanning build expertise or only rent it?** The authors ask this themselves: *"Does AI-enabled boundary spanning foster genuine knowledge growth, or merely facilitate temporary access to existing expertise?"* Unanswered here, and directly load-bearing for [[ai-deskilling]] — a commercial professional producing technically balanced proposals has not thereby learned engineering.
- Open: every result is one-day. Nothing in the corpus measures what happens to team performance, silo structure, or affect after months of AI-augmented work.
