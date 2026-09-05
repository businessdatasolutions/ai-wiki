---
type: concept
aliases: ["analogical reasoning", "analogical-reasoning", "strategy by analogy", "predictive analogy"]
tags: [analogical-reasoning, strategy-theory, theory-based-view, carroll, sorensen]
confidence: 0.8
last_confirmed: "2026-06-25"
accessed_at: "2026-09-05"
source_count: 2
relationships:
  - type: supports
    target: strategic-foresight
    via: "disciplined analogies are a sensing/scenario tool"
  - type: supports
    target: theory-based-view
    via: "[[2026-04-28-carroll-sorensen-strategy-analogy|Carroll & Sørensen 2024]] position disciplined analogy as the practical methodology for [[theory-based-view]] (TBV) theory-discovery — analogies aid theory discovery, wider-team theory engagement, identifying unique aspects, and communication"
quality_score: 0.99
quality_notes: ['1 near-empty section(s)']
---

# Analogical Reasoning (in Strategy)

The use of **analogies between a known source case and an unknown target case** to inform strategy formulation, communication, or evaluation. Logicians regard analogy as a weak inductive form, yet practitioners use it pervasively. The wiki's anchor source ([[2026-04-28-carroll-sorensen-strategy-analogy|Carroll & Sørensen 2024]]) argues analogies should be *disciplined*, not banished.

## Working definition

Two roles of analogy in strategy discourse (Gentner 1982):

| Role | Use |
|---|---|
| **Rhetorical / persuasive** | Vivid metaphor for stakeholders ("Glassdoor is Tripadvisor for jobs") |
| **Generative / problem-solving** | Surface candidate causal mechanisms; develop firm-specific theory of value |

A **predictive analogy** has the structure: source A has features a₁, a₂, … and outcome a_c; target B has features b₁, b₂, … (where b_n is similar to a_n); therefore the unknown b_c is *plausibly* similar to a_c.

## Key claims

### Why analogies dominate strategy discourse despite weak logical foundations

1. **Efficient communication** — a one-phrase analogy carries vast detail.
2. **Concrete and memorable** — material analogies vivid; abstract theories aren't.
3. **Predictive even when conceptual understanding is limited**.
4. **Generative problem-solving tool** — best solutions often generalize from familiar puzzles.
5. **Intermediate-level abstraction** — neither too specific nor too abstract; matches how busy executives reason.
6. **Success-story anchoring** — the source firm worked, providing existence proof.

### Practical tools for disciplining strategy analogies ([[2026-04-28-carroll-sorensen-strategy-analogy|Carroll & Sørensen 2024]])

1. **Decompose** the global analogy into atomic feature premises.
2. **Add negative analogies** (where source and target *differ*).
3. **Distinguish horizontal vs. vertical relations** (Hesse 1966):
   - Horizontal = surface similarity between source and target features.
   - Vertical = causal relationships within source that produced its outcome.
4. **Test the vertical relations** — does the source's success theory plausibly transfer?
5. **Build multiple analogies in parallel** — increases predictive ability.

### Connection to the theory-based view of strategy

The **theory-based view (TBV)** of strategy (Felin & Zenger 2009, 2017) asks executives to develop firm-specific theories of value:

1. What is your firm's theory of value?
2. Is your theory novel, simple, elegant?
3. Is it falsifiable / generalizable / generative?
4. Who must you convince for your theory to be realized?

Analogies aid TBV in **theory discovery**, **wider-team theory engagement**, **identifying unique aspects**, and **communication**.

### Worked example: Glassdoor / Tripadvisor

| Tripadvisor (source) | Glassdoor (target) |
|---|---|
| experiential-good info (hotels) | experiential-good info (jobs) |
| free + open access | free + open access |
| user-generated content | user-generated content |
| five-star ratings + detailed reviews | same |
| collects data → reports + trend prediction | same |
| ad/referral revenue | same |
| **market success** | **plausibly similar** |

Negative premises (where the analogy *fails* or weakens): travel events vs. ongoing employment; willingness to disclose negative experiences; user registration requirements.

### AI-related analogy noted in passing

The paper's footnote-level example: a leaked Google memo (Patel & Ahmad 2023) characterized the open-source AI threat to GPT-4 as *"if GPT-4 is the Walmart you go to for apples, what happens when a fruit stand opens in the parking lot?"* — illustrating the analogy form in a current AI strategy debate.

### Analogy as a cognitive primitive, not just a strategy tool ([[2026-06-25-guilbeault-stanford-gsb-what-ai-cant-do-and-why|Guilbeault / Stanford GSB 2026]])

The wiki's second source widens the concept beyond strategy discourse. **Douglas Guilbeault** (Stanford GSB) names **metaphor and analogy** as one of the **non-statistical mechanisms** by which humans reason — alongside an aesthetic "vibes" sense and intuition — and uses this to argue a limit of LLMs. His claim: LLMs learn by brute-force statistical optimization over massive data, whereas humans "do a lot with a little" partly *because* they reason analogically and metaphorically, achieving **conceptual leaps** rather than smooth, within-distribution steps. This reframes analogy not as a weak inductive form to be disciplined (the Carroll & Sørensen strategy framing above) but as a **load-bearing primitive of human cognition** that current AI architectures may be structurally unable to reproduce. The two sources are complementary: Carroll & Sørensen treat analogy as a *strategy methodology to be made rigorous*; Guilbeault treats it as *evidence of a human cognitive capacity AI lacks*. Confidence rises to 0.8 on this second, cross-domain corroboration.

## Debates and supersession

- **Weak inductive form vs. load-bearing cognitive primitive.** Logicians treat analogy as a *weak* inductive inference (the Carroll & Sørensen framing: useful but to be *disciplined* with negative analogies and vertical-relation tests). [[2026-06-25-guilbeault-stanford-gsb-what-ai-cant-do-and-why|Guilbeault]] inverts the valence — analogy/metaphor is a *strength*, a primitive that lets humans leap where statistical optimizers cannot. Not a contradiction so much as two altitudes: *normative* (how to use analogy rigorously in strategy) vs. *descriptive* (what analogy reveals about human cognition).
- **Scope drift (2026-06-25).** The page began strategy-specific ("Analogical Reasoning (in Strategy)") on a single source; the Guilbeault ingest widens it toward analogy-as-general-cognition. If a third, cognitive-science source lands (Gentner's structure-mapping; Hofstadter), the page may warrant splitting the strategy-methodology layer from the cognition layer.
- **Open contradiction with LLM-analogy optimism.** Whether LLMs can do *generative/causal* analogy (not just *rhetorical*) is unsettled — see Open questions. Guilbeault is the pessimist anchor; a source demonstrating strong LLM analogical transfer would create a genuine `contradicts` edge.

## Related concepts

- [[2026-06-25-guilbeault-stanford-gsb-what-ai-cant-do-and-why|Guilbeault / Stanford GSB]] — analogy/metaphor as a non-statistical human cognitive mechanism and a proposed limit of LLM optimization.
- [[theory-based-view]] — the framework analogical reasoning supports in [[2026-04-28-carroll-sorensen-strategy-analogy|Carroll & Sørensen 2024]]'s framing. Disciplined analogy is the practical methodology for TBV theory-discovery; TBV is the falsifiability layer that disciplines what counts as a *good* analogy.
- [[strategic-foresight]] — analogies between historical convergence cycles and the current period are explicitly invoked in [[2026-04-28-ftsg-convergence-outlook-2026|FTSG 2026]] (industrial revolution, post-WWII, late-1990s).
- [[dynamic-capabilities]] — sensing involves analogizing across industries, contexts, time periods.
- [[2026-04-28-anand-wu-genai-playbook|Anand-Wu's 2×2]] — itself a kind of generative analogical structure for matching deployment context to AI use case.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "analogical-reasoning")
SORT file.name ASC
```

## Open questions

- Two sources now ([[2026-04-28-carroll-sorensen-strategy-analogy|Carroll & Sørensen]] on strategy methodology; [[2026-06-25-guilbeault-stanford-gsb-what-ai-cant-do-and-why|Guilbeault]] on analogy as cognition). Related Gavetti & Rivkin work (2005, 2014) and Felin & Zenger TBV writings would deepen the strategy side; a cognitive-science source on analogy-making (e.g. Hofstadter, Gentner's structure-mapping) would deepen the new cognitive-primitive side.
- Open question whether LLMs can serve as effective analogy-generation tools — the [[jagged-frontier]] suggests they may be good at the *rhetorical* role and weaker at the *generative/causal* role, and [[2026-06-25-guilbeault-stanford-gsb-what-ai-cant-do-and-why|Guilbeault]] argues their statistical-optimization approach is structurally weak at exactly the leaping/insight that analogy enables.
