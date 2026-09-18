---
type: source
kind: book
title: "An Introduction to MultiAgent Systems (2nd ed.) — Chapter 1: Introduction; Chapter 2: Intelligent Agents"
author: ["Michael Wooldridge"]
publisher: "John Wiley & Sons"
edition: "2nd edition"
date_published: 2009-01-01
date_ingested: 2026-09-18
length: "~42 PDF pages (Ch. 1 complete, 15 pp.; Ch. 2 complete, 27 pp. — including the Part I and Part II openers, notes, class readings, mind maps and footnotes). Two chapters of a book of at least 17; the remaining chapters (deductive, practical-reasoning and reactive architectures; communication, cooperation, negotiation, game theory, logics) were not supplied. Scanned pages with an OCR text layer: a handful of short passages are garbled and the formal notation in §2.5–2.6 is partly mangled."
raw:
  - "../../raw/books/michael-wooldridge-an-introduction-to-multiagent-systems-2009_ch1.md"
  - "../../raw/books/michael-wooldridge-an-introduction-to-multiagent-systems-2009_ch2.md"
tags: [multiagent-systems, intelligent-agents, agent-definition, autonomy, adjustable-autonomy, reactivity, proactiveness, social-ability, agents-vs-objects, intentional-stance, task-specification, utility-functions, bounded-optimality, achievement-tasks, maintenance-tasks, agent-environment, textbook, pre-llm]
relationships:
  - type: supports
    target: 2024-12-19-anthropic-building-effective-agents
    via: "both locate the agent/non-agent line in who decides how a task gets done. Anthropic separates workflows (LLMs orchestrated through predefined code paths) from agents (LLMs that dynamically direct their own processes); Wooldridge separates giving a system 'a fully elaborated program to execute' from delegating a goal and letting the system decide how to accomplish it"
    confidence: 0.8
  - type: supports
    target: 2026-08-19-he-databricks-anthropic-primitives-to-production-agents
    via: "both make trajectory choice the discriminator. He's progression runs from single LLM calls through code-orchestrated workflows to agents 'where LLMs are actually deciding their own trajectories'; Wooldridge defines the autonomy that matters as 'the ability and requirement to decide how to act so as to accomplish our delegated goals'"
    confidence: 0.8
  - type: contradicts
    target: 2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness
    via: "the scope of the word 'agent'. Baugues adopts Willison's 'an LLM with tools running in a loop to accomplish a goal', which names an implementation; Wooldridge's 'a computer system that is situated in some environment, and that is capable of autonomous action in this environment in order to meet its delegated objectives' is implementation-neutral and admits thermostats and Unix daemons. The two agree on goal and loop; they differ on whether the LLM is part of the definition"
    confidence: 0.7
  - type: supports
    target: 2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1
    via: "both define an agent by the same ingredients: a delegated goal, an environment the agent acts in, feedback from that environment, and the agent deciding what to do next. Chowdhery adds deciding when to stop; Wooldridge adds that the agent must be prepared for its actions to fail in environments it only partially controls"
    confidence: 0.75
  - type: supports
    target: 2022-10-06-yao-et-al-react-synergizing-reasoning-acting
    via: "the interleaved agent–environment sequence. Wooldridge formalises a run as alternating environment states and actions and names the balance between goal-directed and reactive behaviour as the open problem of agent design; ReAct's thought–action–observation trajectory interleaves plan-level reasoning with environment observations inside one loop"
    confidence: 0.7
  - type: supports
    target: 2026-05-14-pochampally-assistant-or-actor-delegation-regret
    via: "the boundary of delegated authority. Wooldridge's agent may pick subgoals only 'in the furtherance of our delegated goals', and the adjustable-autonomy conditions he cites (Scerri et al. 2003) hand control back when a decision might cause harm or the human would decide better; Pochampally's delegation regret is users' response to agents acting beyond what they would have authorised, withdrawn most for irreversible, externally visible actions"
    confidence: 0.75
  - type: supports
    target: 2025-03-17-cemri-why-do-multi-agent-llm-systems-fail
    via: "run-time coordination between agents. Wooldridge's first distinction between multiagent and ordinary concurrent systems is that coordination is 'not hardwired in at design time' and needs run-time mechanisms; MAST's system-design and inter-agent-misalignment categories catalogue how LLM multi-agent systems fail at that coordination"
    confidence: 0.7
  - type: supports
    target: 2026-05-18-wolfe-agent-evaluation-detailed-guide
    via: "how success is specified for an agent. Wooldridge distinguishes utility over individual states from utility and predicates over whole runs, and achievement tasks from maintenance tasks; Wolfe's evaluation components separate outcome goals (final environment state) from process goals judged over the transcript"
    confidence: 0.7
---

# Wooldridge — An Introduction to MultiAgent Systems, Ch. 1–2 (2nd ed., 2009)

The two opening chapters of **Michael Wooldridge's** standard textbook on multiagent systems: Chapter 1, *Introduction* (Part I, *Setting the Scene*), and Chapter 2, *Intelligent Agents* (the first chapter of Part II, *Intelligent Autonomous Agents*). The book predates large language models by more than a decade. It is the **first pre-LLM source in the wiki's agent material** — every other source behind [[ai-agents]] describes LLM agents from 2022 onward — and it supplies the vocabulary those sources mostly use without citing: autonomy, delegation, environment, reactivity, proactiveness, social ability, and task specification.

## TL;DR

- **The definition.** *"An agent is a computer system that is situated in some environment, and that is capable of autonomous action in this environment in order to meet its delegated objectives"* (adapted from Wooldridge & Jennings 1995). It names no implementation. A thermostat and the Unix mail-watcher `xbiff` both qualify, as simple agents but not intelligent ones.
- **Autonomy is a spectrum, and the useful point on it is narrow.** Humans sit at one end, a Java method at the other. The agents the book is about sit in between: an entity *"to which we can delegate goals in some high-level way (i.e. not just by giving it a fully elaborated program to execute), and then have this entity decide for itself how best to accomplish its goals."* It cannot choose its own goals, only subgoals in furtherance of delegated ones.
- **Adjustable autonomy** (citing Scerri et al. 2003): control passes from agent to human when the human would decide with substantially higher benefit, when the environment is highly uncertain, when the decision might cause harm, or when the agent lacks the capability. *"An agent that always comes back to its user or owner for help with decisions will be unhelpful, while one that never seeks assistance will probably also be useless."*
- **Intelligent agents are reactive, proactive and social**, and the hard part is the combination. Pure goal-direction is easy (every procedure is one) and so is pure reaction. Balancing the two, so that an agent pursues plans systematically but drops them when their preconditions fail or the goal becomes invalid, *"is one of the key problems facing the agent designer… the problem is essentially still open."*
- **"Objects do it for free; agents do it because they want to."** With objects, the caller decides whether a method runs. With agents, the receiver decides whether to act on a request. Classical multiagent systems assume agents built by different parties, **self-interested**, with no common goal.
- **How to tell an agent what to do** without telling it how: utility functions over states or over whole runs, maximising expected utility, **bounded optimality** (the best agent the actual machine can run), predicate task specifications, and the split between **achievement tasks** (bring about a goal state) and **maintenance tasks** (never enter a failure state).

## Key claims

### Chapter 1 — why multiagent systems

1. **Five trends drive the field**: ubiquity, interconnection, intelligence, **delegation** ("delegation implies that we give control to computer systems"), and human-orientation (programming abstractions moving from machine code toward concepts closer to how people think).
2. **Two design problems, micro and macro.** *Agent design*: how to build agents capable of independent, autonomous action on delegated tasks. *Society design*: how to build agents that can cooperate, coordinate and negotiate with other agents, *"particularly when the other agents cannot be assumed to share the same interests/goals."*
3. **Three motivating visions**: an autonomous space probe that diagnoses its own fault (NASA's DS1, 1998, was the first probe with an agent-based control system); peer air-traffic control systems taking over for a failed one; and a personal digital assistant that negotiates a package holiday across vendor sites. The last is described as *"perhaps the closest of the three scenarios to actually being realized."*
4. **"Isn't it all just distributed systems?"** No, for two reasons. Coordination between autonomous agents is not hardwired at design time and needs run-time mechanisms, and agent encounters are *economic*: between self-interested parties, not components sharing one system goal.
5. **"Isn't it all just AI?"** No. Oren Etzioni: *"Intelligent agents are ninety-nine percent computer science and one percent AI."* You do not need to solve planning or learning to build an agent. *"For some applications, capabilities such as learning may even be undesirable."* Classical AI also ignored social ability until about 1980.
6. **"Isn't it all just game theory?"** Game-theoretic solution concepts are descriptive and often computationally hard (NP-complete or worse); multiagent systems research brings complexity theory to bear on computing them.
7. **Agents also serve as a tool for simulating societies** (the EOS project on emergent social complexity in Palaeolithic France), distinct from their use as a software-engineering paradigm.

### Chapter 2 — intelligent agents

8. **Environments vary along named axes** (after Russell & Norvig): accessible vs inaccessible, deterministic vs non-deterministic, static vs dynamic, discrete vs continuous, plus episodic and real-time. The hardest environment is inaccessible, non-deterministic, dynamic and continuous — which describes the Internet.
9. **Agents act without full control of their environment.** *"The same action performed twice in apparently identical circumstances might appear to have entirely different effects… agents in all but the most trivial of environments must be prepared for the possibility of failure."*
10. **Reactive systems are harder than functional ones** because an agent in a non-terminating relationship with its environment makes decisions with long-term consequences. A printer controller that always defers one process "until later" never serves it; a locally reasonable choice can be wrong over the system's whole history.
11. **Agents vs expert systems.** Expert systems like MYCIN are *disembodied*: they act through a human middleman, not on an environment, and do not cooperate with other agents.
12. **The intentional stance** (Dennett; McCarthy; Shoham) — describing a system in terms of beliefs, desires and intentions — is *"nothing more than an abstraction tool"*, legitimate when it compresses what is known about a system and pointless when a simpler mechanistic description exists. A light switch can be described this way; doing so buys nothing.
13. **The abstract model.** An environment is a set of states with an initial state and a history-dependent, non-deterministic state-transformer. An agent maps runs (histories) to actions. A *run* is an interleaved sequence of environment states and actions. Purely reactive agents ignore history; agents with internal state (the `see` / `next` / `action` decomposition) are no more expressive than history-based agents, but are easier to build.
14. **Utility over runs beats utility over states** for agents operating over long periods, because state-level utility cannot express a long-term view. The Tileworld testbed (Pollack 1990) scores runs as holes filled over holes that appeared, and tests whether an agent notices when its current objective has become pointless or a better opportunity has appeared.
15. **Optimal is not implementable; bounded optimal is the target.** Maximising expected utility over all agents defines an agent that may not run on any real machine. Restricting the search to agents implementable on the machine at hand (Russell & Subramanian 1995) gives the bounded optimal agent.
16. **Predicate task specifications and task environments.** A task is a predicate over runs, and a task environment pairs an environment with that predicate. Success can be pessimistic (every run satisfies it), optimistic (some run does) or probabilistic.
17. **Agent synthesis is automatic programming.** A synthesis algorithm is *sound* if every agent it returns succeeds, and *complete* if it returns an agent whenever one exists. *"Of the two conditions, soundness is probably the more important; there is not much point in complete synthesis algorithms that deliver 'buggy' agents."*

## What this adds to the wiki

**A definition older than the implementation.** The wiki's default agent definition is Willison's *"an LLM with tools running in a loop to accomplish a goal"*, which by August 2026 is shared across [[2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness|Google (Baugues)]] and [[2026-08-19-he-databricks-anthropic-primitives-to-production-agents|Anthropic (He)]] developer material. Wooldridge's definition keeps the goal and the loop but leaves the LLM out, which makes it a definition of the category rather than of the current way of building one. The two readings are recorded as a debate on [[ai-agents]]. The discriminator He names, **who chooses the trajectory**, and [[2024-12-19-anthropic-building-effective-agents|Anthropic's workflows-versus-agents split]] both land on Wooldridge's account of autonomy: deciding *how*, not *what*. [[2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1|Chowdhery & Mirhoseini's]] course-altitude definition (goal, environment, feedback, deciding when to stop) lists the same ingredients.

**Delegation boundaries, stated in 2003.** The adjustable-autonomy conditions in Ch. 2 are a compact version of what [[agent-oversight-and-delegation]] assembles from 2026 sources. [[2026-05-14-pochampally-assistant-or-actor-delegation-regret|Pochampally's delegation regret]] concerns agents acting beyond what a user would have authorised; Wooldridge's agent is defined as free to choose subgoals only in furtherance of the goals delegated to it.

**The reactive/goal-directed balance.** [[2022-10-06-yao-et-al-react-synergizing-reasoning-acting|ReAct]] interleaves reasoning with environment observations inside one trajectory; Wooldridge's run is the same interleaving, formalised, and he names the balance as the open design problem.

**The multiagent premise.** Wooldridge's multiagent systems are societies of self-interested agents with different owners, and his first distinction from concurrent systems is that coordination happens at run time rather than being hardwired. [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail|MAST's]] failure categories describe coordination failures in LLM multi-agent systems, which are typically built by one team for one goal. See [[multi-agent-failure-modes]].

**Task specification.** Utility over runs, predicates over runs, and achievement versus maintenance tasks are the formal ancestors of the outcome-versus-process split in [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe's agent-evaluation guide]].

**The harness line, early.** Etzioni's *"ninety-nine percent computer science and one percent AI"* is recorded on [[agent-harness]].

## Neighbour sources

- `supports` [[2024-12-19-anthropic-building-effective-agents]] — workflows vs agents; who decides how a task gets done.
- `supports` [[2026-08-19-he-databricks-anthropic-primitives-to-production-agents]] — trajectory choice as the discriminator.
- `contradicts` [[2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness]] — whether the LLM is part of the definition of an agent.
- `supports` [[2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1]] — goal, environment, feedback, self-directed next step.
- `supports` [[2022-10-06-yao-et-al-react-synergizing-reasoning-acting]] — the interleaved agent–environment trajectory.
- `supports` [[2026-05-14-pochampally-assistant-or-actor-delegation-regret]] — the boundary of delegated authority.
- `supports` [[2025-03-17-cemri-why-do-multi-agent-llm-systems-fail]] — run-time coordination between agents.
- `supports` [[2026-05-18-wolfe-agent-evaluation-detailed-guide]] — specifying success over states versus whole runs.

Considered and not linked: [[2026-04-02-tran-kiela-single-agent-outperforms-multi-agent-under-equal-budgets]] (a compute-budget argument the chapters do not address) and the governance sources on [[agent-oversight-and-delegation]], whose overlap with the adjustable-autonomy passage is topical rather than a shared claim.

## Linked entities and concepts

- Concepts: [[ai-agents]], [[agent-oversight-and-delegation]], [[multi-agent-failure-modes]], [[agent-harness]], [[react-reasoning-acting]]
- **Dangling** (single-source mention, deferred per the second-source promotion rule): Michael Wooldridge (author). People cited in the chapters but not authors of this source, and so out of scope for promotion: Nicholas Jennings, Oren Etzioni, Paul Scerri, Stuart Russell, Peter Norvig, Daniel Dennett, Yoav Shoham, Martha Pollack.

## Scope and reliability

**What was read.** Chapters 1 and 2 in full, from the Part I and Part II openers through the notes, class readings, mind maps and footnotes. The book has at least 17 chapters (Ch. 2 points forward to Chapter 17 for knowledge theory); the agent architectures (deductive, practical-reasoning/BDI, reactive and hybrid) and everything on communication, cooperation, negotiation and game theory sit in chapters not supplied. **This page covers the definitions and framing, not the architectures or the multiagent mechanisms.**

**Edition and date.** Identified from the content: the Part I / Part II structure matches the 2nd edition, and the latest works cited are from 2007, after the 2002 1st edition. The excerpt carries no copyright page, so the publication date is recorded year-only as `2009-01-01`, following the precedent of [[2026-05-03-rewired-second-edition-sample]].

**Text quality.** The PDFs are scanned pages with an OCR text layer. A handful of short passages are garbled where figures or text boxes interrupt the page (in Ch. 1 around the §1.2.1 opener and the semantic-web box; in Ch. 2 around the `xbiff` example, the MYCIN paragraph and two passages in §2.5–2.6), and the mind-map figures come through as fragments. **The formal notation in §2.5–2.6 is partly mangled**, so this page paraphrases the run / state-transformer / utility model and does not quote its equations. Quotations above were checked against readable passages.

**Age.** Written in 2009, citing work up to 2007. The environment classification, the definition and the task-specification framework are foundational and unlikely to be superseded; the empirical remarks (e.g. that no website yet negotiates holiday packages in real time) are dated.
