---
type: query-trace
question: "How can we classify different levels of AI maturity for workers?"
date: 2026-08-31
language: en
trace: "ai-maturity-levels-for-workers-query-trace.json"
pages_used: 9
pages_ignored: 65
---

# Query trace — Classifying AI maturity for workers

## 1. Question

- **Original:** How can we classify different levels of AI maturity for workers?
- **Restated:** What defensible scheme does the wiki support for placing an individual knowledge worker on an AI-maturity scale, and what markers separate the levels?
- **Facets:**
  1. What maturity models already exist in the corpus, and at what unit of analysis?
  2. What observable markers distinguish levels for an individual worker?
  3. What moves a worker between levels, and what blocks them?
  4. What are the measurement caveats?

## 2. Paths explored

Retrieval: `node scripts/wiki-retrieve.mjs --json -n 12 "..."` — qmd hybrid ∪ graph traversal (1 hop), RRF-fused, re-ranked by `effective_confidence`. Graph available: **True**; `graph_warning`: **none**. **11 qmd hits → 72 fused candidates**, plus 2 added at gap-expansion.

**qmd hits** (relevance stream)

| # | Page | type | qmd score | fused | verdict |
|---|------|------|-----------|-------|---------|
| 1 | `wiki/concepts/enterprise-ai-adoption.md` | concept | 0.930 | 0.980 | **USE** |
| 2 | `wiki/threads/ai-maturity-measurement-comparison.md` | thread | 0.620 | 0.826 | **USE** |
| 3 | `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` | source | 0.540 | 0.910 | **USE** |
| 4 | `wiki/sources/2026-07-22-brown-wef-meet-the-leader-entry-level-jobs-in-an-ai-era.md` | source | 0.520 | 0.896 | IGNORE |
| 5 | `wiki/concepts/ai-employment-effects.md` | concept | 0.520 | 0.916 | IGNORE |
| 6 | `wiki/sources/2026-04-28-mit-sloan-ai-maturity.md` | source | 0.490 | 0.869 | **USE** |
| 7 | `wiki/sources/2026-04-28-brynjolfsson-canaries-coal-mine.md` | source | 0.480 | 0.856 | IGNORE |
| 8 | `wiki/threads/organizational-frameworks-for-ai-adoption.md` | thread | 0.470 | 0.754 | IGNORE |
| 9 | `wiki/sources/2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work.md` | source | 0.440 | 0.831 | IGNORE |
| 10 | `wiki/sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees.md` | source | 0.380 | 0.819 | IGNORE |
| 11 | `wiki/sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships.md` | source | 0.330 | 0.808 | IGNORE |

**graph neighbours** (1 hop, typed-edge stream) — 61 pages reached only via the graph. The ones that changed the answer or were explicitly weighed:

| Page | fused | effConf | verdict |
|------|-------|---------|---------|
| `wiki/concepts/automation-vs-augmentation.md` | 0.480 | 0.94 | IGNORE |
| `wiki/concepts/jagged-frontier.md` | 0.458 | 0.94 | IGNORE |
| `wiki/concepts/micro-productivity-trap.md` | 0.453 | 0.95 | **USE** |
| `wiki/concepts/dynamic-capabilities.md` | 0.446 | 0.84 | IGNORE |
| `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | 0.330 | 0.80 | **USE** |
| `wiki/concepts/durable-skills.md` | 0.324 | 0.94 | **USE** |
| `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | 0.306 | 0.53 | IGNORE |
| `wiki/concepts/ai-deskilling.md` | 0.297 | 0.69 | IGNORE |

The remaining 53 graph-only neighbours all fell to `below-threshold` (see §3).

**index.md / gap-expansion** (Step 5 — one round)

| Page | why added |
|------|-----------|
| `wiki/sources/2026-08-31-blum-how-i-ai-claude-cowork-pm-system.md` | Facet 2 (worker markers) was unanswerable from the ledger — every candidate was firm-level. This page holds the corpus's only narrated end-to-end worker trajectory. It **is** indexed in qmd (a targeted search scores it 97%) but did not reach the top-12 seeds for this phrasing. |
| `wiki/sources/2026-05-07-anthropic-economic-index-5-learning-curves.md` | Facet 2/3 needed a population-scale empirical anchor that individual proficiency is real and learnable, rather than one narrated case. Located by name via `durable-skills` [W7], which cites it. |

## 3. Ignore policy applied

Reason-classes that actually fired this run:

- `below-threshold` — graph-only neighbour (`qmd_rank: null`) whose fused score is low and which no facet requires. The long tail: 55 of the 72 candidates.
- `off-facet` — semantically adjacent (usually "AI + workers") but addresses none of the four facets. The dominant false positive here: the ledger is full of *labour-market-effect* pages, which are about what AI does **to** workers, not about classifying a worker's maturity.
- `redundant` — the claim is already carried, with its figures, by a higher-ranked USE page. Fired three times, all against `durable-skills` [W7] and `enterprise-ai-adoption` [W8], which aggregate their sources.
- `wrong-granularity` — firm/organisation-level framing where the facet needs individual markers.
- `decayed` — `effective_confidence < 0.5` with the same ground covered by a fresher USE page. Fired once.

Not fired: `superseded` (no candidate carried `status: stale`).

## 4. Information ignored

The twelve judgement calls (the other 48 ignores are `below-threshold` tail):

| Page | reason-class | one-line reason |
|------|--------------|-----------------|
| `wiki/concepts/ai-employment-effects.md` | `off-facet` | labour-market outcomes of AI, not a maturity classification of individuals |
| `wiki/sources/2026-07-22-brown-wef-meet-the-leader-entry-level-jobs-in-an-ai-era.md` | `redundant` | its human-skills-demand finding is already carried, with figures, inside durable-skills [W7] |
| `wiki/sources/2026-04-28-brynjolfsson-canaries-coal-mine.md` | `off-facet` | entry-level employment decline; about who gets hired, not how mature a worker is |
| `wiki/sources/2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work.md` | `off-facet` | productivity/equalising effects of one deployment, not a maturity scale |
| `wiki/sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees.md` | `off-facet` | anthropomorphising risk in agent framing, not worker maturity |
| `wiki/sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships.md` | `redundant` | the MGI Skill Change Index is summarised with its figures inside durable-skills [W7] |
| `wiki/threads/organizational-frameworks-for-ai-adoption.md` | `wrong-granularity` | organisational frameworks; the firm-level facet is better served by W2 and W8 |
| `wiki/concepts/automation-vs-augmentation.md` | `off-facet` | per-task deployment lens; does not classify the worker |
| `wiki/concepts/jagged-frontier.md` | `off-facet` | model capability unevenness, not human maturity |
| `wiki/concepts/dynamic-capabilities.md` | `wrong-granularity` | firm-level capability theory; the worker facet needs individual markers |
| `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | `decayed` | effective_confidence 0.53 and the same ground is covered fresher by W2/W8 |
| `wiki/concepts/ai-deskilling.md` | `redundant` | the productive-struggle countermeasure is cited via W6, which states it operationally |

The notable ignore is `concepts/ai-employment-effects` — the **second-highest-ranked qmd hit of the whole run** (rank 5, fused 0.916). It was ignored because the question asks how to *classify a worker's maturity*, and that page is about employment outcomes. High rank on a shared vocabulary ("AI", "workers") is not relevance to the facet.

## 5. Information used

| Anchor | Page | type | effConf | contribution |
|--------|------|------|---------|--------------|
| [W1] | `wiki/threads/ai-maturity-measurement-comparison.md` | thread | — | the instrument problem, the four firm-level success rates, and the worker-level axis this thread now carries |
| [W2] | `wiki/sources/2026-04-28-mit-sloan-ai-maturity.md` | source | — | the four-stage ladder form and the between-stage inflection finding |
| [W3] | `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` | source | 0.85 | the two-axis (2x2) maturity structure and the non-additivity of combining two capabilities |
| [W4] | `wiki/sources/2026-08-31-blum-how-i-ai-claude-cowork-pm-system.md` | source | — | the corpus's only narrated end-to-end worker trajectory, with observable transition markers |
| [W5] | `wiki/concepts/micro-productivity-trap.md` | concept | 0.95 | the J-curve trough and why cross-sectional measurement cannot see it |
| [W6] | `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | source | 0.80 | what the top level looks like as behaviour: five patterns, the T-shape, delegate-tasks-not-judgment |
| [W7] | `wiki/concepts/durable-skills.md` | concept | 0.94 | what is being matured - the judgment/evaluation bundle, and AI fluency as a learnable meta-skill |
| [W8] | `wiki/concepts/enterprise-ai-adoption.md` | concept | 0.95 | firm-level composition and why worker maturity does not sum to firm maturity |
| [W9] | `wiki/sources/2026-05-07-anthropic-economic-index-5-learning-curves.md` | source | — | the empirical anchor that individual AI proficiency is real, learnable and measurable at population scale |

## 6. Answer-element map

| Anchor | Answer element (claim) | Wiki page | Section / span used |
|--------|------------------------|-----------|---------------------|
| [W1] | Every AI-maturity instrument in the wiki measures the firm, not the worker; their success rates span 1%-13%. | [[threads/ai-maturity-measurement-comparison]] | ## What we know so far; ## Updated cross-walk; ## A different unit of analysis: the individual worker |
| [W2] | The four-stage ladder form, its 28/34/31/7 distribution, and the financial inflection sitting between Stage 2 and Stage 3 rather than at the top. | [[sources/2026-04-28-mit-sloan-ai-maturity]] | ### The four stages of enterprise AI maturity; ### The financial inflection is at Stage 2 -> Stage 3 |
| [W3] | Maturity is better modelled on two axes than one; combining both produces non-additive gains (1.6x-2.2x); 59% score low on both; quadrants are median splits. | [[sources/2026-05-07-ransbotham-augmented-learners]] | ## The 2x2 taxonomy; ## Headline outcomes; ## Limitations the report acknowledges |
| [W4] | The observable transition markers for an individual: share of work inside one harness, who writes the system of record, whether the agent detects its own context gaps, whether skills log their own friction, whether the system has been distributed. | [[sources/2026-08-31-blum-how-i-ai-claude-cowork-pm-system]] | ## TL;DR; ## Why this matters to the wiki; ## Debates and supersession |
| [W5] | The J-curve trough: ROI runs negative first, trust falls, the worker double-checks everything; a cross-sectional measurement cannot tell a worker mid-climb from one who has failed. | [[concepts/micro-productivity-trap]] | ## The J-curve narrated from inside a single job; ## The J-curve, and "honestly, I think it's a little lazy" |
| [W6] | What the top of the ladder looks like as behaviour: higher altitudes, shift-left on intent, designing environments rather than prompting, verification as the bottleneck, and "delegate tasks, not judgment". | [[sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer]] | ## Five patterns of top AI-native engineers; ## The evolved T-shape - four skill domains |
| [W7] | What is maturing is the judgment/evaluation bundle rather than tool knowledge; evaluation is named the terminal skill; AI fluency is a learnable meta-skill. | [[concepts/durable-skills]] | ## Working definition; ## Human skills growing twice as fast, and evaluating a fleet as the terminal skill |
| [W8] | Worker maturity does not sum to firm maturity; distribution is a UX problem (3 days terminal vs 15-minute guided chat). | [[concepts/enterprise-ai-adoption]] | ## Adoption from the bottom up: one worker's system, then a plugin for everyone |
| [W9] | Individual AI proficiency is empirically real and learnable: high-tenure users show higher task-success rates after controls, and model selection tracks task value. | [[sources/2026-05-07-anthropic-economic-index-5-learning-curves]] | ## TL;DR (chapter 2, Learning curves) |

## 7. Final answer

### The short answer

**The wiki does not contain a worker-level AI-maturity instrument — and that gap is itself the finding.** Every maturity model in the corpus measures the *firm*: MIT CISR's four stages, the AI Index's C-suite self-report, Cisco's readiness survey, and the HBR transformation baseline. Their "success" rates span 1% / 7% / 12% / 13% — a single order of magnitude across radically different instruments, which mostly tells you that *whatever you call success, it's rare* [W1]. None of them can say where a given person stands [W1].

What the corpus *does* support is a defensible worker-level scale **composed** from three pieces it holds separately: a ladder *form*, a two-axis *structure*, and a set of observable *markers*. Below is that composition, with the joins made explicit.

### 1. Borrow the ladder's shape from the firm-level model — including its most useful finding

MIT CISR's enterprise ladder runs Experiment (28%) → Pilots (34%) → AI ways of working (31%) → AI future-ready (7%) [W2]. Two properties are worth carrying over to individuals:

- **Stages are defined by *ways of working*, not by tool count.** The jump from Stage 2 to Stage 3 is "expanding process automation, architecting for reuse" — a change in how work is organised, not in which product is licensed [W2].
- **The value is in the middle, not at the top.** The greatest financial impact comes from moving Stage 2 → Stage 3; Stages 1–2 sit below industry-average performance and 3–4 above [W2]. A worker scale should therefore locate its own inflection rather than treat the top rung as the only thing that matters.

### 2. Make it two-dimensional, not one

The single strongest structural argument against a one-dimensional scale is Ransbotham et al.'s 2×2 [W3]. Scoring 3,467 respondents on *organisational learning* × *AI-specific learning* produces four quadrants — and the gains are **non-additive**: either capability alone helps somewhat, but combining them compounds (1.6× on uncertainty preparedness, up to 2.2× on talent disruption) [W3]. The majority — 59% — are low on both [W3].

Transposed to the individual, the two axes become:

- **AI fluency** — can you get good work out of the model? This is empirically real and *learnable*: after controlling for task type, model choice and conversation complexity, high-tenure users show systematically higher task-success rates, and their model selection tracks task value [W9]. It is a genuine meta-skill, not a personality trait [W7].
- **Work-system design** — have you restructured *your own work* so the AI has context, reach and a place to put its output? This is the axis that firm-level instruments capture as "ways of working" [W2] and that the worker-level evidence shows is where the compounding actually happens [W4].

The reason a worker can be highly fluent and still low-maturity is that these are independent. Someone who writes excellent prompts all day into a stateless chat window is high on axis 1 and near-zero on axis 2 — and by the 2×2's logic gets a fraction of the available return [W3].

### 3. The level markers — what to actually observe

The corpus's only end-to-end *narrated* worker trajectory supplies markers that are observable rather than self-assessed [W4]. Composed with the ladder form [W2], they yield five levels:

| Level | Name | The marker that separates it from the level below |
|---|---|---|
| 1 | **Experimenting** | AI is used, but nothing survives the session — no saved context, no reusable artifact. |
| 2 | **Repeating** | Reusable prompts/workflows exist, but the *human is the integration layer*, carrying context between tools by hand [W4]. |
| 3 | **Integrating** | Work is centralised in one system that holds persistent context and reaches your real tools. The marker is a share: what fraction of your screen time happens inside it (Blum's is 70–80%) [W4]. |
| 4 | **Delegating** | Work happens when you are not typing — scheduled tasks — and the agent *writes* to a system of record rather than only reading it. Blum's Notion board is "almost read-only" for him [W4]. The boundary that defines this level is Forsgren & Macvean's: **"delegate tasks, not judgment"** [W6]. |
| 5 | **Compounding** | The system improves itself with your approval: it detects context it lacks and asks [W4], its skills log their own friction for weekly review [W4], and it has been packaged so someone else can use it [W4]. |

Two of these markers are worth singling out because they are unusually hard to fake. **Who writes the system of record** is binary and externally visible [W4]. And **whether the agent notices its own ignorance** — flagging a term it doesn't understand and asking you to define it — is the sharpest single indicator that context has become infrastructure rather than a habit [W4].

### 4. What is actually maturing

Not tool knowledge. The corpus converges hard on **judgment and evaluation** as the durable content [W7]. Brynjolfsson's framing is that almost everyone will manage a fleet of agents and "the ones who are good at pointing them in the right direction and then *evaluating* them are going to really thrive" — evaluation, not direction, is named the terminal skill [W7]. Forsgren & Macvean reach the same boundary from inside Google: top performers "are not vibe coding… they are designing environments, setting the guardrails," and verification, not authoring, is the bottleneck [W6]. A worker scale that measures tool adoption rather than evaluation capacity is measuring the wrong variable [W7].

### 5. Four caveats that any honest scale has to carry

- **The trough is invisible to a snapshot.** Maturity growth runs *negative* first: before the system knows your working context, everything is frictionful, trust falls, and you double-check everything — which consumes exactly the time the tool was supposed to return [W5]. A one-off assessment cannot distinguish a worker who is mid-climb from one who has failed [W5]. This is the individual-scale version of the productivity J-curve [W5].
- **The evidence base for the worker axis is thin.** The level markers rest substantially on **one self-reported, unaudited, single-subject account** selected for being broadcast-worthy [W4]. The mechanism is credible and the markers are observable; the associated "a week's work in a day" multiplier is an anecdote and should not be used as a target [W4].
- **Worker maturity does not sum to firm maturity.** A company of Level-4 individuals is not a Level-4 company — which is precisely why Blum's personal system had to be repackaged as a shared onboarding plugin before it spread [W8]. Distribution turned out to be a *UX* problem, not a capability problem: the terminal-based route took colleagues three days and failed; a 15-minute guided chat succeeded [W8].
- **Self-report is the default failure mode.** Every firm-level instrument in the corpus that relies on it produces numbers that are hard to compare [W1], and Ransbotham's own quadrants are median splits — "high" and "low" are relative to the sample, not to an external benchmark [W3]. A worker scale should ask for *observable facts* ("does the agent write to your task system?") rather than agreement statements ("I use AI effectively").

### 6. Where this leaves you

The scale above is a **defensible composition, not a validated instrument.** Its ladder form and inflection logic are borrowed from a firm-level model with a 2022 survey base [W2]; its two-axis structure is transposed from an organisational construct [W3]; its markers come from one narrated case [W4] plus one population-scale measurement of learning effects [W9]. That is enough to build a self-assessment that is honest about its own status — and the thread tracking this question now carries the open request for a real worker-level instrument, because nothing in the corpus is one [W1].


## 8. Trace artifact

Machine-readable provenance: [`ai-maturity-levels-for-workers-query-trace.json`](ai-maturity-levels-for-workers-query-trace.json)

**Invariants checked.** Every `[W#]` in §7 resolves to a §6 row and to a `verdict: "use"` candidate in the JSON (9/9). Every §5 page exists on disk. Every §4 row carries a reason-class from the ignore policy. §4 is non-empty (65 ignores).
