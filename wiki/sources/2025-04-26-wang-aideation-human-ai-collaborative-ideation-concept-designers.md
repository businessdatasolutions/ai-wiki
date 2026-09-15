---
type: source
kind: paper
title: "AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers"
author: ["Wen-Fan Wang", "Chien-Ting Lu", "Nil Ponsa i Campanyà", "Bing-Yu Chen", "Mike Y. Chen"]
publisher: "CHI Conference on Human Factors in Computing Systems (CHI '25), Yokohama, Japan — ACM; National Taiwan University. CC BY 4.0"
url: "https://doi.org/10.1145/3706598.3714148"
date_published: 2025-04-26
date_ingested: 2026-09-15
length: "~28 pages (read: abstract, §1 introduction, §6 summative study, §8 field study incl. Tables 2–3 and continued-production usage, §9 discussion and limitations; system-implementation sections and related work skimmed)"
raw: "../../raw/papers/aideation-human-ai-collaborative-ideation-concept-designers.md"
tags: [aideation, chi-2025, human-ai-collaboration, creativity-support-tool, concept-design, entertainment-industry, ideation, generative-ai, image-generation, reference-gathering, breadth-and-depth-exploration, field-study, design-tools, controllability, peer-reviewed, hci]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
  - digital-sensing/digital-scouting
  - contextual/internal-enablers
relationships:
  - type: supports
    target: 2026-06-12-dellacqua-cybernetic-teammate-field-experiment-genai-teamwork
    via: "the same generation-versus-selection split, found in a creative domain by a different method. Dell'Acqua et al. decompose innovation and find AI lifts the *quality distribution of generated ideas* while human judgment retains value in evaluative selection; AIdeation's studios generated 1,092 ideas across 98 cycles and selected 60 — a ~5% selection rate with the designer doing every selection. The tool is built around exactly that division of labour, and its measured wins are all on the generation side"
    confidence: 0.75
  - type: supports
    target: 2026-04-28-dellacqua-jagged-technological-frontier
    via: "a domain-level map of where the frontier actually sits for visual concept work. AIdeation wins decisively on breadth (reference gathering, variation generation, direction-finding) and fails on exactly the fine control professionals need to finish — 'the system covers 70-80% for client communication, but control over lighting, atmosphere, and camera angles is needed for the final 20%.' Jaggedness stated as a workflow boundary rather than as a task-score distribution"
    confidence: 0.7
  - type: supports
    target: 2025-07-02-joshi-venkatraman-fowler-expert-generalists
    via: "the formative study is a statement of what domain expertise buys in an AI-assisted workflow: the 12 designers' complaints are not that GenAI cannot render, but that generic tools 'do not align with the creative intentions of designers.' AIdeation's contribution is encoding concept-design domain knowledge into the tool's phases — the expert's judgment is what makes the general-purpose model useful, which is the expert-generalist thesis at tool-design altitude"
    confidence: 0.65
---

# Wang et al. — AIdeation: A Human-AI Collaborative Ideation System for Concept Designers (CHI '25)

A **peer-reviewed HCI systems paper** from National Taiwan University, and the corpus's **first source on AI in a visual-creative profession** — concept design for films, TV and games. It matters here less for the system than for the **evidence design**: a formative study (12 professionals), a controlled summative study (16 professionals), a **one-week field study in four commercial studios**, and — the part that is hard to fake — **continued unpaid production use after the study ended**.

## TL;DR

Concept designers work in two phases: an **early ideation ("blue sky") phase** of research, brainstorming and visual exploration, then a **final concept phase** where approved directions are refined into production blueprints. The ideation phase is where the pain is: designers are expected to deliver multiple designs daily, so research depth and reference breadth both get squeezed.

The formative study's diagnosis of why off-the-shelf GenAI did not fix this is the most reusable finding in the paper, because it generalises past concept art:

> *"Participants noted critical limitations, including difficulties in formulating prompts, low diversity in outputs, AI hallucinations, lack of detailed information, and limited flexibility for refining results."*

AIdeation's answer is to split the tool along the **phases of the actual workflow** — brainstorming for **breadth**, research for **depth**, then flexible recombination of reference images — rather than treating the job as text-to-image generation.

## What the evidence shows

**Lab (16 professional designers).** AIdeation significantly improved creativity, ideation efficiency and satisfaction versus current tools and workflows, **all p < .01**.

The formative complaints are also a statement of what domain expertise buys: the problem is not that the models cannot render, but that generic tools *"do not align with the creative intentions of designers"* — the [[2025-07-02-joshi-venkatraman-fowler-expert-generalists|expert-generalist]] claim at tool-design altitude, where encoding the professional's workflow into the tool is the contribution.

**Field (4 studios, one week).** Usage intensity varied a lot (40% to 100% of tools used), and so did the result:

| Studio | Domain | Time with AIdeation | Estimated original | Difference |
| --- | --- | --- | --- | ---: |
| 1 | Animation / film / TV | 1.5 working days | 2 working days | **−25%** |
| 2 | Art outsourcing (matte painting) | 5 hours | 4 hours | **+25%** |
| 3 | Game visual development | 2 working days | 5 working days | **−60%** |
| 4 | Game environment design | 6 working days | 14 working days | **−57%** |

Across the four studios: **1,092 ideas generated across 98 ideation cycles, 60 selected**, contributing to **12 environments**.

**The negative case is reported rather than buried**, and the wiki should note that approvingly. Studio 2 got *slower*: *"The client didn't seem to favor the artistic style generated by AIdeation, and the image generation process was somewhat time-consuming."* House style and client taste are constraints the tool could not absorb.

**The strongest signal is the one the authors did not design.** After the study, **Studios 1 and 4 kept using AIdeation in commercial production** — Studio 1 iterating 35 cycles / 221 ideas to build 6 scenes in two weeks at roughly **40% time saved**, Studio 4 running 69 cycles / 590 ideas for 22 scenes in six weeks (no time saving measurable against a fixed deadline, but quality reported as improved). Voluntary continued adoption on paid work is a far better adoption signal than a post-study questionnaire.

## The ceiling, stated by a professional

The limitation section is unusually concrete about where the tool stops:

> *"The system covers 70-80% for client communication, but control over lighting, atmosphere, and camera angles is needed for the final 20%."* — P4

and the failure mode designers actually hit:

> *"Sometimes I just wanted to remove one element from the idea or adjust the composition, but the whole image changed."* — S4

Breadth is solved; **fine-grained controllability is not**. That is the same shape as the corpus's [[2026-04-28-dellacqua-jagged-technological-frontier|jagged-frontier]] result, expressed as a workflow boundary rather than a score distribution — and it is why the designers remain in the loop at exactly the selection-and-refinement step where [[2026-06-12-dellacqua-cybernetic-teammate-field-experiment-genai-teamwork|Dell'Acqua et al.]] find human judgment retains its value.

## Dynamic capabilities (Warner & Wäger)

- **`digital-seizing/rapid-prototyping`** — the entire contribution is compressing the explore-and-vary loop in early-stage design: 1,092 ideas across 98 cycles in a week, with the measured wins being time-to-direction (*"can quickly provide multiple directions for our team to explore and develop"*).
- **`digital-sensing/digital-scouting`** — the "research: supporting depth exploration" component is scouting made a tool feature: the designers' stated bottleneck is gathering diverse, relevant references for *"unique or poorly defined topics"*, which is environmental scanning inside a creative workflow.
- **`contextual/internal-enablers`** — the formative study identifies what has to be true for a general-purpose generative model to be usable by professionals (domain-shaped phases, reference recombination, iterative refinement), which is an enabling-conditions finding rather than a capability claim.

## Linked entities and concepts

- Concepts: [[jagged-frontier]], [[automation-vs-augmentation]], [[generative-ai]], [[expert-generalist]], [[ai-employment-effects]], [[document-intelligence]]
- **Dangling** (single-source mention, deferred): Wen-Fan Wang, Chien-Ting Lu, Nil Ponsa i Campanyà, Bing-Yu Chen, Mike Y. Chen, National Taiwan University, CHI, Midjourney, Pinterest, DALL·E 3

## Scope and reliability

Peer-reviewed at CHI, with a rare four-part evidence chain and an honest negative case. Cite it for **the shape of AI-assisted creative work**, not for effect sizes.

The authors' own limits, and they are substantial:

- **The summative study relied mainly on self-reported data.** They say so directly: comparing ideation *outcomes* between conditions is hard, so the p<.01 results are on perceived creativity, efficiency and satisfaction, not on independently judged output quality.
- **The field study had no quantitative measures and less control than the lab.** Every number in the time table above is **actual time against the designer's own estimate of what the original workflow would have taken** — a counterfactual supplied by an interested party, unblinded. Treat −57% as a practitioner's impression, not a measurement.
- **N is small and the domain is narrow**: 4 studios, one week, environment concept design specifically (chosen because it is the most resource-intensive).
- **Conversion caveat:** this is a figure-heavy HCI paper and `pdftotext` is text-only, so the system's interface — which is most of the contribution — is not in the raw markdown. Figure captions survive inline. Read the PDF for anything visual.

One thing the paper does **not** engage, which is conspicuous in a paper about generative AI in commercial art: **copyright and the provenance of reference imagery** goes essentially unaddressed, despite the tool being built around searching and recombining references. Its own reference list contains work on early-career game developers' ethical scepticism about GenAI; the body does not take it up.

## Debates and supersession

- **The time savings are self-estimated counterfactuals.** The wiki has been careful about this class of number elsewhere ([[ai-coding-productivity-evidence]]'s perception-gap material exists precisely because practitioners misjudge their own speed-up, in both directions). The −25% / −57% / −60% figures should never be quoted alongside randomised effect sizes without the caveat attached.
- **Does tool-encoded domain knowledge keep paying, or does model capability absorb it?** AIdeation's advantage over raw DALL·E 3 comes from encoding concept-design workflow structure into the tool. Whether that advantage survives more capable base models is the standard [[agent-harness|harness-versus-model]] question, arriving here from HCI rather than from agent engineering — and this paper is a 2025 data point on the harness side.
- Open: the paper measures ideation speed and satisfaction, never whether AI-assisted concepts are *better* by an independent judge, and never what a year of this does to a junior designer's skill development — the [[ai-deskilling]] question in a domain where the craft is the career.
