---
type: source
kind: paper
title: "Measuring Human Leadership Skills with Artificially Intelligent Agents"
author: ["Ben Weidmann", "Yixian Xu", "David J. Deming"]
publisher: "arXiv preprint 2508.02966v1 (Harvard Kennedy School); also NBER Working Paper 33662"
url: "https://arxiv.org/abs/2508.02966"
date_published: 2025-08-05
date_ingested: 2026-10-15
length: "~19 pages (pdftotext extract, read in full; Tables 1–2 transcribed from the page image; supplementary materials not included)"
raw: "../../raw/papers/2025-08-05-weidmann-measuring-human-leadership-skills-with-ai-agents.md"
tags: [leadership, leadership-measurement, ai-agents-as-followers, silicon-samples, hidden-profile, pre-registered, lab-experiment, gpt-4o, social-skills, emotional-perceptiveness, fluid-intelligence, questions, turn-taking, plural-pronouns, positive-affect, overconfidence, harvard-skills-lab, harvard-kennedy-school]
dynamic_capabilities:
  - digital-transforming/improving-digital-maturity
roles: [chro, ceo, transformation-lead]
relationships:
  - type: supports
    target: 2026-05-07-globerson-et-al-scalable-measurement-durable-skills
    via: "both measure soft skills at scale by having a person work with LLM teammates; Globerson et al. validate against human raters' scores of the transcript, Weidmann et al. against each leader's causal effect on randomly assigned human teams"
    confidence: 0.75
  - type: supports
    target: 2026-06-12-dellacqua-cybernetic-teammate-field-experiment-genai-teamwork
    via: "both are Harvard experiments on GPT-4-class models inside team problem-solving; the Cybernetic Teammate has AI assist human teams in the field, this study has AI agents replace the human followers in the lab"
    confidence: 0.6
  - type: supports
    target: 2025-11-24-sadun-wood-worklab-hard-to-become-ai-first-organization
    via: "both concern leading AI agents as a managerial skill; Sadun describes the agent as an apprentice the manager must question and onboard, this study measures how well leading agents tracks leading people"
    confidence: 0.6
---

# Weidmann, Xu & Deming (2025) — measuring human leadership skills with AI agents

## TL;DR

A pre-registered lab experiment from the Harvard Skills Lab at Harvard Kennedy School by **Ben Weidmann**, **Yixian Xu** and **David J. Deming** (arXiv 2508.02966, August 2025; also NBER Working Paper 33662). It asks whether leading a team of AI agents measures the same skill as leading a team of people. **249 leaders** each led six teams of three randomly assigned human followers and six teams of three GPT-4o agents, in counterbalanced order, on new "Hidden Profile" puzzles where the clues needed are split across team members. Findings:

1. **The leader matters a lot, on both tests.** Leader identity alone explains more than half the variation in group performance (R² 0.57 on the AI test, 0.50 on the human test). Replacing an average leader with one 1 SD better raises team performance by about **0.65 SD**, and still about 0.55 SD after controlling for the leader's own task skill, fluid IQ and typing speed. A "good" leader (+1 SD) solves 53% of problems, a "bad" one (−1 SD) 10%, close to guessing.
2. **The same people succeed on both.** Each leader's score on the AI test correlates with their causal contribution to human teams at **0.81** after correcting for measurement error (raw 0.67; 95% CI 0.72–0.88). Controlling for hard skills, the correlation is 0.69 (raw 0.52).
3. **The same traits predict success on both:** fluid IQ, emotional perceptiveness and economic decision-making skill; **not** gender, age, ethnicity or education.
4. **The same behaviours predict success on both.** Good leaders do not talk more. They **ask more questions**, have more **conversational turn-taking**, and use **plural pronouns** ("we", "us").
5. **Emotion matters less with AI followers.** Positive, warm language helps human teams clearly but AI teams only marginally. This is the main way the AI test differs from the human one.
6. **Cost.** The human version cost **$114 per participant** and needed two researchers to run it. The AI version cost **$23** and ran on its own.

## Key claims

### The design: a causal ground truth for leadership

Most leadership measures rate people (by survey, by supervisor) rather than measure what they do to a team's output. This study uses the repeated random assignment method from the authors' earlier work (Weidmann & Deming, *Econometrica* 2021): put each leader in front of several randomly drawn teams, predict each team's score from the members' individual skills, and attribute the consistent over- or under-performance to the leader. That is the **ground truth**. The **AI leadership test** is the same procedure with three GPT-4o agents as followers.

The task is a modified Hidden Profile problem, a standard paradigm for group decision-making. Each member gets eight clues per puzzle, half shared and half private, some ruling options out and some irrelevant distractors (*"Greenfish migrate to access seasonal food resources"*). Two changes make it a leadership test: a **star network** in which followers can talk only to the leader, who must gather information, manage time and decide; and **probabilistic answers**, where the leader spreads 100 points of credence over five options, which reduces ceiling effects and gives a continuous score. Every puzzle was written for the study, in two parallel forms of matched difficulty, so the model could not have seen the answers in training. Each leader first took individual tests: typing speed, an individual version of the puzzle, fluid IQ (Culture Fair Intelligence Test), emotional perceptiveness (the PAGE test) and economic decision-making (the Assignment Game).

### Three pre-registered predictions, all confirmed

1. **Leader effects are as large on the AI test as on the human test.** The confidence intervals are narrow and overlap, both before and after conditioning on hard skills. The authors read this as evidence that both tests measure soft skills, not only task ability.
2. **The same characteristics predict both.** The correlation between emotional perceptiveness and success is 0.45 on the human test and 0.37 on the AI test; the difference is not significant. On the AI test it survives conditioning on fluid IQ (0.24).
3. **Individual leaders rank the same on both:** the 0.81 / 0.69 correlations above.

### Exploratory: how good leaders talk

Table 1 of the paper (transcribed in the raw file) regresses each leader's contribution on five communication measures:

| Measure | Human test (each alone) | AI test (each alone) |
| --- | --- | --- |
| Number of words | 0.094, n.s. | 0.028, n.s. |
| Number of questions | 0.130\*\* | 0.150\*\* |
| Conversational turns | 0.202\*\*\* | 0.175\*\*\* |
| Plural pronouns | 0.172\*\*\* | 0.156\*\* |
| Positive affect | 0.245\*\*\* | 0.115\* |

Standardized coefficients; \*\* p<0.05, \*\*\* p<0.01; the single star is not defined in the paper's caption. **Volume of talk predicts nothing; questions, turn-taking and "we" do, on both tests.** The text says positive affect is *"robustly associated with team success on the human test, but not so with the AI measure."* The table is slightly less clear-cut: the AI coefficient is about half the size and only marginally significant. Bad leaders' answers look like an uninformed guess spread evenly over the options, which the authors read as *"they learn relatively little from interacting with their team."*

The AI test also reproduces two substantive findings: overconfident people are more willing to lead, whether the team is AI (ρ 0.29) or human (ρ 0.27); and leaders who judge their own performance more accurately contribute more (ρ 0.16 AI, 0.21 human). The authors argue the second is unlikely to be in any model's training data, since no prior study could estimate it.

### What the authors claim it is for

- **Selection.** Because leader impact is not predicted by demographics, *"current selection processes are overlooking many high-potential leaders,"* and a cheap standardised test could improve both performance and equity.
- **Training evaluation.** Most leaders get no formal training, and the training that exists is rarely evaluated causally; a performance-based test makes evaluation possible.
- **Research.** One-fifth of the cost, no need to schedule groups of people at the same time.

### Limitations stated by the authors

The AI agents are not people: emotion plays a smaller role, and some leaders said strong human followers were *"better to work with"*, better at filtering information and at offering strategy. The agents were not built to reproduce the variety of human behaviour; that is future work. And the crucial step is still to come: **external validation against leadership success in real organisations.** The study validates the AI test against a lab ground truth, not against careers.

## Dynamic-capabilities reading

- **`digital-transforming/improving-digital-maturity`** — the cell covers identifying workforce capability. The paper gives a cheap, performance-based way to identify one of the scarcest capabilities, leadership, and the skill it measures (directing AI agents through questions and synthesis) is itself part of the workforce's maturity for agentic work.

## How it connects

- [[concepts/durable-skills|durable-skills]] — a measured version of the claim that social skills are durable and valuable: leadership is large in effect, measurable, and made of questions, turn-taking and inclusive language rather than volume. [[2026-05-07-globerson-et-al-scalable-measurement-durable-skills|Globerson et al. (Google)]] use AI teammates to measure collaboration skills the same way, validated against human raters instead of team outcomes.
- [[concepts/agent-fleet-management|agent-fleet-management]] — evidence that the skill of directing agents is not a separate technical skill: people who lead agents well lead people well, and vice versa. It bears on [[2025-11-24-sadun-wood-worklab-hard-to-become-ai-first-organization|Sadun's]] point that managing agents rests on management skill that is unevenly distributed.
- [[2026-06-12-dellacqua-cybernetic-teammate-field-experiment-genai-teamwork|The Cybernetic Teammate]] — a Harvard field experiment with AI inside teams, from the other direction (AI helping human teams rather than standing in for them).
- [[2026-09-03-hbs-ai-institute-think-youre-a-good-leader-try-leading-an-ai-team|HBS AI Institute summary]] — a practitioner write-up of this paper that adds the "AI as a leadership practice environment" reading.

## What was actually ingested

The full arXiv v1 PDF, 19 pages, converted with `pdftotext`: main text, Methods, references, acknowledgments. Tables 1 and 2 are images in the PDF and were transcribed by hand from the rendered page; the figures (leader-effect plot, predictor scatter, flow diagram) survive only as captions. The Supplementary Materials (agent prompts, puzzles, interface screenshots) are on OSF and were not read.

## Linked entities and concepts

- [[concepts/durable-skills|durable-skills]], [[concepts/agent-fleet-management|agent-fleet-management]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the cell tagged above.
- [[HBS AI Institute]] — published the practitioner summary; Deming is a 2026 institute associate.

**Dangling** (single-source mention, deferred): Ben Weidmann, Yixian Xu, David J. Deming, Harvard Skills Lab, Harvard Kennedy School, Walmart Foundation (funder).

## Scope and reliability

A pre-registered lab experiment with n=249 leaders and about 750 human followers, with data, code and materials public on OSF. Strong internal design: random assignment, counterbalanced order, purpose-written puzzles, hard-skill controls, correction for measurement error. The limits are the ones the authors name: one task type (text-chat information pooling under time pressure), one model (GPT-4o), followers prompted without behavioural variety, and no external validation against real-world leadership outcomes. A preprint, not yet peer-reviewed in this version. Funded by the Walmart Foundation; the authors declare no competing interests.
