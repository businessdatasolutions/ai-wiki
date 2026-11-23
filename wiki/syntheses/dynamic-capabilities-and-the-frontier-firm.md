---
type: synthesis
aliases: ["Warner-Wäger and the Frontier Firm", "dynamic capabilities and the Frontier Firm", "W&W x Frontier Firm"]
tags: [dynamic-capabilities, warner-wager, frontier-firm, frontier-playbook, sensing-seizing-transforming, strategic-renewal, lock-in, codification, inimitability, diffusion-engine, cross-framework-mapping]
derived_from: [dynamic-capabilities-and-the-frontier-firm]
opened: 2026-11-22
closed: 2026-11-22
confidence: 0.70
last_confirmed: "2026-11-22"
accessed_at: "2026-11-22"
source_count: 14
relationships:
  - type: uses
    target: warner-wager-process-model
    via: "reads the Frontier Firm sources against the W&W cell vocabulary, cell by cell"
  - type: uses
    target: dynamic-capabilities
    via: "uses Teece's distinction between ordinary and dynamic capabilities to locate where the Frontier Firm puts competitive advantage"
  - type: supports
    target: syntheses/organizational-frameworks-for-ai-adoption
    via: "answers, for one framework, that synthesis's open question on a cross-walk with academic strategy theory"
  - type: uses
    target: enterprise-ai-adoption
    via: "the Frontier Firm material it maps is recorded on the enterprise-ai-adoption concept page"
quality_score: 1
---

# Synthesis: Dynamic capabilities and the Frontier Firm

## Question

How does the Frontier Firm, as Microsoft and Harvard Business School describe it, relate to [[warner-wager-process-model|Warner & Wäger's process model]] of [[dynamic-capabilities|dynamic capabilities]]? Where do the two coincide, where do they diverge, and what does reading one through the other add?

## Findings

The two are not rival frameworks. [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation|Warner & Wäger (2019)]] is a peer-reviewed process model. It explains how incumbents renew themselves through nine microfoundations under sensing, seizing and transforming, with renewal of the business model, the collaborative approach and the culture as outcomes. The Frontier Firm is a practitioner concept: *"a new organizational blueprint for companies that are AI-powered but human-led"* ([[2026-09-16-microsoft-becoming-a-frontier-firm-second-edition|Microsoft's Frontier Playbook, 2026]]). Its fullest statement is that playbook and the [[2026-11-19-george-hrncirik-ignite-becoming-a-frontier-firm|Ignite 2026 session]] presenting it. Read against each other, they show six things.

### 1. The Frontier Firm fills W&W's transforming cluster, and gives it machinery

Mapped element by element, the playbook lands mostly in the transforming cluster and in one seizing cell:

| Frontier Firm element | W&W cell | Fit |
| --- | --- | --- |
| A named executive owner per goal; goals *"cascaded from the top"*; CEO and top team set vision | `contextual/internal-enablers` (executive support) | Close |
| An AI Transformation Office in every function, plus a central "learning accelerator" | `digital-transforming/redesigning-internal-structures` (W&W: *hiring a CDO; team-based structures*) | Close; the playbook distributes what W&W placed in one CDO |
| Recipe 1, persona acceleration: role-based huddles, Camp AIR, power users as coaches | `digital-transforming/improving-digital-maturity` (*identifying workforce maturity; leveraging digital knowledge inside the firm*) | Close, and far more specific than W&W |
| Recipe 2, process redesign: end-to-end value streams, "lean before agents", work organised *"not reinforcing the siloes of our org chart"* | `redesigning-internal-structures` | Close |
| Recipe 3, AI-first possibility: small expert squads in sandboxes, *"the incubator recipe"* | `digital-seizing/rapid-prototyping` (*MVPs; lean start-up; digital innovation lab*) | Close; the sandbox is W&W's innovation lab |
| People: a *"culture of continuous experimentation, adaptation, and learning"*, Growth Mindset, Model-Coach-Care | `strategic-renewal/organizational-culture` | Close |
| Codify advantage and controls: private evals, the hill-climbing machine | No W&W cell (see finding 4) | None |
| Safeguard security | No W&W cell | None |

What W&W name in one or two words per cell, the playbook turns into routines: three recipes, three levels of AI, a four-layer measurement pipeline with impact timelines, and a train-the-trainer Learn-Do-Teach cycle. W&W's thinnest cell, *improving digital maturity*, is where the Frontier Firm material is richest. Read this way, the Frontier Firm is an operationalisation of W&W's transforming cluster for the AI era.

### 2. Sensing, portfolios and ecosystems are almost absent

Across the nine Frontier Firm sources in the wiki, the `dynamic_capabilities:` tags fall like this:

| W&W cell | Sources tagged (of 9) |
| --- | ---: |
| `digital-transforming/improving-digital-maturity` | 8 |
| `digital-transforming/redesigning-internal-structures` | 6 |
| `digital-seizing/rapid-prototyping` | 6 |
| `digital-sensing/digital-mindset-crafting` | 4 |
| `contextual/internal-barriers` | 4 |
| `strategic-renewal/organizational-culture`, `contextual/internal-enablers` | 3 each |
| `strategic-renewal/business-model`, `contextual/external-triggers` | 2 each |
| `digital-seizing/strategic-agility` | 1 |
| `digital-sensing/digital-scouting`, `digital-sensing/digital-scenario-planning`, `digital-seizing/balancing-digital-portfolios`, `digital-transforming/navigating-innovation-ecosystems`, `strategic-renewal/collaborative-approach` | 0 |

The tags are the wiki's own coding, applied by the same ingests, so the zeros are partly an artefact. Hrncirik's finance funnel at Ignite (130 ideas, about 12 business cases, six chosen by the CFO) is a portfolio decision that was tagged as prototyping. The pattern holds on a reading of the texts, though. No Frontier Firm source discusses scanning markets or competitors, building scenarios, or working with external partners as part of what makes a Frontier Firm.

The reason is visible in how the sources open. The external trigger is taken as given: AI is the technology, and the question is how to diffuse it. Sensing survives in two forms:
- **As mindset.** [[2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm|Nadella]] asks CEOs to hold a worldview *"long before conventional wisdom"*.
- **As operational discovery from below.** Hrncirik: *"All of our best ideas, all of them come from people closest to the work."* Microsoft's power users find the uses; at Ignite, an audience member's "starfish" model used a shared backlog to reveal value streams nobody had named.

This matches [[2025-12-02-bevilacqua-ai-strategic-leadership-skills-top-managers|Bevilacqua et al. (2025)]], whose executives report that the most impactful AI initiatives came from middle managers and frontline teams.

What has no owner in the Frontier Firm is W&W's *strategic* sensing: where the market is going, and which digital competitors and business models are coming. The playbook tells firms to *"cascade goals from the top, not use cases from the bottom"*, but it does not say where the goals come from. The ecosystem gap has an irony. The Frontier Firm AI Initiative is itself an innovation ecosystem: member firms, Harvard researchers and Microsoft ([[2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about|HBS AI Institute]]). Its content still describes one firm transforming itself.

### 3. Different outcomes of renewal: operating model, not business model

W&W define digital transformation as *"an ongoing process… which recognizes agility as the core mechanism for the strategic renewal of an organization's (1) business model, (2) collaborative approach, and eventually the (3) culture."* The Frontier Firm's outcome framework, the Success Framework, names different outcomes:

- enrich employee experiences;
- reinvent customer engagement;
- reshape business processes;
- bend the curve on innovation.

Its example metrics are performance metrics inside the existing business: revenue per rep, cycle time, cost per transaction, time from idea to market. Business-model renewal appears only at the edges:
- the playbook's AI-first recipe says firms need *"mechanisms to disrupt their own business model"*;
- EY's Dan Diasio, a member of the initiative, names the billable hour as EY's hardest change ([[2025-12-16-diasio-wood-worklab-agentic-ai-corporate-ladder|Diasio on WorkLab]]).

Read through W&W, the Frontier Firm is mostly renewal of the **operating model**. W&W call business-model adaptation without the digital microfoundations *"nondigital-based strategic change."* The Frontier Firm material is close to the mirror image: rich microfoundations, with business-model renewal mostly left out.

On culture, the two agree on substance and differ on order. W&W observed culture changing *"eventually"*, as the last of the three renewals. The playbook calls its people section *"the most important,"* and George says Microsoft *"initially focused too much on technology alone, when the biggest effort we needed to make is with people."* [[2025-11-24-sadun-wood-worklab-hard-to-become-ai-first-organization|Sadun]] calls reskilling *"bloody hard"* because it asks people *"to change who they are."* Both locate culture as the slowest layer. W&W describe that; the Frontier Firm prescribes starting on it first.

### 4. AI moves the line between ordinary and dynamic capabilities, and the playbook moves inimitability with it

W&W build on Teece: ordinary capabilities are *"doing things right,"* are replicable and can be *"outsourceable to the cloud"*, so they no longer give durable advantage. Dynamic capabilities are *"doing the right things"* and are hard to replicate. The Frontier Firm sources push more capabilities into the ordinary category:

- *"CI alone gives you a leaner version of your old company."* Continuous improvement, the ordinary capability, is necessary but not distinctive.
- The *"law of hill-climbing"*: *"Any enterprise whose competitive advantage cannot be measured by its own evals, improved through its own expertise, and preserved across any foundation model will be arbitraged."*
- Nadella: tacit knowledge, *"the unique ways that you are able to operate, pass judgment, have taste,"* is now extractable by models *"through human trajectories,"* and leaking it is *"a one-way door."*

This is a real departure from the dynamic-capabilities logic. In Teece and W&W, a capability is hard to imitate partly because it is tacit and embedded in routines. The playbook's prescription is to codify the tacit into private evals, skills and even model weights, which makes it easier to copy. It then protects the result by architecture rather than by tacitness: tenant isolation, data residency, model independence. Inimitability moves from *"nobody else knows how we do this"* to *"nobody else can reach where we have written down how we do this."* That is a testable claim, and no source tests it. It is also the claim most aligned with what the publisher sells.

### 5. Lock-in: the transforming capability turned into a routine

The bridge between the two already exists, through the Frontier Firm's own research partner. [[2025-08-05-hbs-ai-institute-mastering-change-resilience-key-to-ai-driven-success|Lakhani, Stave, Ng and Martines (2025)]], from the HBS AI Institute that co-runs the initiative, call the missing ingredient in AI value **change resilience**. They split it into sensing, *rewiring* (*"redeploy talent, data, capital, and decision rights in days or weeks, not fiscal quarters"*) and *lock-in* (*"codify what a team learns… so the next initiative starts from a higher baseline"*). The three match Teece's triad one to one; the institute's summary, which is what the wiki holds, cites neither Teece nor W&W.

Lock-in is what the Frontier Firm's practices mostly are:
- the Customer Zero Council that carries learning between functions;
- *"Experience Cards"* that codify sales best practice;
- the AI-first *"innovation flywheel"* in which *"each sandbox publishes to a shared library"*;
- the hill-climbing machine, which turns lock-in into a reinforcement-learning loop.

Two things are added to W&W:
- **A time scale.** Days or weeks, where W&W leave speed unstated.
- **A reading of transforming as continuous.** In W&W, renewal is ongoing but its microfoundations read as programmes: hire a CDO, design team structures. In the Frontier Firm, transforming is a standing routine. Huddles are *"now rhythm of business"*, and the playbook calls change management *"a permanent part of the new rhythm of business."*

### 6. The evidence gap is shared, but shaped differently

Neither side has shown that its capabilities produce performance in AI adoption:

- **W&W.** The nine microfoundations rest on seven German incumbents and 18 consultant interviews from 2016–17, and have never been tested quantitatively. The generic sense–seize–transform spine has been: [[2025-06-15-cimino-ai-adoption-sustainable-growth-smes|Cimino et al. (2025)]] find it loads as one construct in 210 Italian startups. Dynamic capabilities predict AI *acceptance* (β = 0.523) about twice as strongly as AI *implementation intensity* (β = 0.279), and do not predict economic performance (β = 0.138, not significant). [[2026-03-28-nguyen-ai-adoption-toe-dynamic-capabilities|Nguyen et al. (2026)]] model it the other way round: adoption first, capabilities after, with AI as an amplifier of advantage that already exists.
- **Frontier Firm.** Every figure is Microsoft's account of itself, under a footer limiting it to *"the context of our company"*. The sales gains (9.4% revenue per head, 20% higher close rates) are *"within the pilot group"*. The supply-chain 75% is *"across selected workflows"*. The HBS case behind the initiative's early insights was unpublished when the wiki captured them.

Combined, they suggest a hypothesis. The dynamic-capabilities literature explains readiness better than implementation. The Frontier Firm's diffusion engine is almost entirely about implementation: turning licences into changed work. If the Frontier Firm is a specification of the implementation leg that the capability literature leaves thin, then Cimino's asymmetry is the gap it claims to fill. Nothing in the wiki tests that.

### What the coupling is good for

**W&W as a diagnostic on a Frontier Firm programme.** The empty cells are the questions a Frontier Firm programme does not ask:
- Who senses where the market and competitors are going (scouting, scenario planning)?
- How are AI bets balanced against the core, and with what reallocation (portfolios, strategic agility)?
- Which partners does the firm need (ecosystems)?
- Does the business model change, or only the operating model?

A firm can run excellent diffusion and still miss the change Diasio and Nadella point to, where AI alters how the firm earns money.

**The Frontier Firm as operational content for W&W's transforming cluster.** The recipes, the levels of AI and the measurement pipeline give *improving digital maturity* and *redesigning internal structures* concrete mechanisms, metrics and time scales they lack in the 2019 paper. They are vendor mechanisms, to be read as hypotheses, not findings.

## Sources consulted

- [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation]] — the process model, its definition of digital transformation, and Teece's ordinary/dynamic distinction.
- [[2026-09-16-microsoft-becoming-a-frontier-firm-second-edition]] — the Frontier Playbook: five elements, recipes, levels, CI + AI = CA, the measurement pipeline, the hill-climbing machine.
- [[2026-11-19-george-hrncirik-ignite-becoming-a-frontier-firm]] — the playbook presented, with the finance funnel and the floor discussion.
- [[2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about]] — the initiative as a Microsoft–Harvard ecosystem; guided rather than self-discovered adoption.
- [[2025-08-05-hbs-ai-institute-mastering-change-resilience-key-to-ai-driven-success]] — sensing, rewiring, lock-in, from the initiative's research partner.
- [[2025-11-24-sadun-wood-worklab-hard-to-become-ai-first-organization]] — the Frontier Firm as a learning firm; reskilling as the hard part; each firm on its own J-curve.
- [[2026-07-27-george-wood-worklab-future-of-work-has-no-org-chart]] — George's account of the practice before the playbook.
- [[2025-10-30-bornet-wood-worklab-ai-agents-leaders]] — four Frontier Firm traits.
- [[2025-12-16-diasio-wood-worklab-agentic-ai-corporate-ladder]] — a member firm's business-model problem (the billable hour).
- [[2026-10-30-lakhani-silicon-valley-girl-people-most-at-risk-from-ai]] — the initiative's co-founder on firms that redesign work and the rest.
- [[2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm]] — token capital and the leakage of tacit knowledge.
- [[2025-06-15-cimino-ai-adoption-sustainable-growth-smes]] — the only quantitative test of the dynamic-capabilities spine in the wiki; the readiness–implementation asymmetry.
- [[2026-03-28-nguyen-ai-adoption-toe-dynamic-capabilities]] — capabilities after adoption; AI as amplifier.
- [[2025-12-02-bevilacqua-ai-strategic-leadership-skills-top-managers]] — sensing signals that come from middle managers and frontline teams.

## Lessons

- The Frontier Firm is best read as an AI-era operationalisation of W&W's transforming cluster, not as a new theory of the firm.
- A Frontier Firm programme leaves W&W's strategic sensing, portfolio balancing, ecosystem and business-model cells empty, so those are the questions to add to it.
- The Frontier Firm renews the operating model; W&W's definition also asks for renewal of the business model, and only one member firm's account in the wiki reaches that.
- Lock-in, the codification of what a team learns, is the shared mechanism, and it is what makes transforming a standing routine rather than a programme.
- The playbook moves inimitability from tacit knowledge to protected codified knowledge; that is a claim to test, and its author sells the protection.
- Neither side has shown its capabilities cause performance in AI adoption; the Frontier Firm addresses implementation, the leg where the capability literature is weakest.

## Open questions

- **Does codification erode or protect advantage?** The playbook says codifying tacit knowledge into private evals and weights, behind a tenant boundary, keeps it inimitable. Teece's logic suggests codified knowledge is easier to copy. Evidence on what happens to a firm's advantage once its standards are written into evals would decide this.
- **Do Frontier Firm practices predict implementation intensity?** A test in Cimino's design, with the recipes, manager role-modelling and lock-in practices as predictors of AI implementation intensity, would test the hypothesis in finding 6.
- **Who owns strategic sensing in a Frontier Firm?** No source places scouting or scenario planning inside the AI Transformation Offices or the top team's role. A source on how a Frontier Firm sets the goals it cascades would fill the gap.
- **Business-model renewal.** Does any member firm of the initiative report a changed revenue model, beyond EY's stated intention on the billable hour?
- **Independent evidence.** The forthcoming HBS case by Bojinov, Sadun and Zhang is the first chance to see Frontier Firm practices described by researchers rather than by the vendor.

## Related pages

- [[warner-wager-process-model]] — the cell vocabulary used above.
- [[dynamic-capabilities]] — the broader Teece framework, including the sensing–rewiring–lock-in mapping.
- [[enterprise-ai-adoption]] — where the Frontier Firm material is recorded.
- [[syntheses/organizational-frameworks-for-ai-adoption|organizational-frameworks-for-ai-adoption]] — the framework stack whose open question on academic strategy theory this synthesis takes up for one framework.
- [[threads/dynamic-capabilities-and-the-frontier-firm|The originating thread]].
