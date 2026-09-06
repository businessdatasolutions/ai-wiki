---
type: thread
status: closed
opened: 2026-08-31
closed: 2026-08-31
tags: [ai-worker-maturity, ai-fluency, worker-skills, maturity-levels, cross-source-comparison, self-assessment]
---

# Thread: How can we classify different levels of AI maturity for workers?

## The question

The wiki holds a dense cluster of **organizational** AI-maturity instruments (see [[ai-maturity-measurement-comparison]] — MIT CISR four stages, AI Index/McKinsey self-report, Cisco readiness, Augmented Learners 2×2). But the user's 2026-08-31 query targets the **individual worker**: is there a defensible way to classify *a person's* maturity in working with AI, and what would move someone from one level to the next?

Opened and closed in the same session: unlike most threads, the evidence base was already in the corpus when the question arrived — seven independent ladder/stage framings plus a skills-and-behaviour literature — so the thread went straight to synthesis.

## What the corpus already held

Retrieval: qmd BM25 search (`ai-wiki` collection; semantic/vector legs unavailable in the remote session — no model downloads) plus grep sweeps on `maturity | fluency | autonomy | up-level` and follow-the-wikilinks reading. Worker-level ladder fragments found:

- **[[Steve Yegge]]'s Eight Stages of AI-assisted development** ([[2026-03-12-oreilly-steve-yegge-wants-you-to-stop-looking-at-your-code|primary source]]) — the most granular *tool-relationship* ladder (IDE completions → YOLO agents → CLI multi-agent → own orchestrator); coder-specific.
- **Ask → Assist → Automate** ([[2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler|Beutler / OpenAI]]) — a *deployment* ladder (how much agency the AI gets), re-readable as a worker-delegation ladder.
- **Human in-the-loop / on-the-loop / out-of-the-loop** ([[2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life|Randell & Gousset / Microsoft]] — collaboration spectrum; the four VS Code modes Ask/Edit/Agent/Plan as its product form).
- **Anthropic Economic Index learning curves** ([[2026-05-07-anthropic-economic-index-5-learning-curves|AEI 5]]) — the only *measured* worker progression: high-tenure users shift from directive mode toward iteration/validation/learning and gain +4 pp task success under controls.
- **Vibe coding → agentic engineering** ([[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy]]) plus the five patterns of top AI-native engineers ([[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren & Macvean]]).
- **Operator → supervisor → mentor** ([[2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset|Argenti / Goldman Sachs]]).
- **Fleet-of-agents ceiling** ([[2026-08-24-carson-vo-how-i-ai-manage-15-ai-agents-solo-founder|Carson]]; Brynjolfsson's "CEO of their own little entity" in [[concepts/durable-skills|durable-skills]]).
- The skills substrate: [[concepts/durable-skills|durable-skills]] (evaluation as the terminal skill), [[concepts/ai-deskilling|ai-deskilling]], [[concepts/jagged-frontier|jagged-frontier]], [[concepts/expert-generalist|expert-generalist]], AI fluency as a universal career-ladder overlay ([[2026-07-19-why-netflix-is-betting-on-systems-thinkers-not-specialists-in-the-ai-era|Netflix / Stone]]), evaluation-capacity-not-adoption as the youth gap ([[2026-06-16-mollick-simon-sinek-ai-skills-experience-edge|Mollick]]).

## Closed

Resolved into [[syntheses/ai-worker-maturity-levels|the AI Worker Maturity synthesis]] (2026-08-31): a six-level model (L0 Bystander → L5 Multiplier) across six assessable dimensions, with per-dimension next-level actions. An interactive self-assessment tool was built from the synthesis the same night; on 2026-09-04 it was **folded** with the local session's independently built, calibrated gate instrument into [**The AI Worker Maturity Scale v3**](../../inspiration/ai-worker-maturity-model.html) — the v2 gate engine (15 gates, conjunctive levels, inversion and contradiction detection) in the remote edition's design, with the synthesis's cited action layer and its L0 floor. The Scale's level names (Experimenting → Compounding) are the operational vocabulary; this synthesis's names (Conversationalist → Multiplier) remain the corpus-derived fragment map.

*Same-day convergence.* While this thread was being synthesized in the remote session, the local session independently ingested [[2026-08-31-blum-how-i-ai-claude-cowork-pm-system|Blum / How I AI]] on `main` — the corpus's first complete single-worker trajectory, raising the very question this thread answers (via [[ai-maturity-measurement-comparison]]'s new worker-level axis). Merged in as the synthesis's eighth fragment the same evening.

## Related pages

- [[ai-maturity-measurement-comparison]] — sister thread (open) on *organizational* maturity instruments; this thread is its worker-level counterpart.
- [[syntheses/organizational-frameworks-for-ai-adoption]] — the org-level frameworks stack; the deployment-maturity rung (Beutler) reappears here at worker altitude.
- [[concepts/durable-skills|durable-skills]], [[concepts/agentic-engineering|agentic-engineering]] — the two concept pages carrying most of the evidence.
