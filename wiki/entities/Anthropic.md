---
type: entity
kind: organization
aliases: ["Anthropic", "Anthropic PBC", "Claude"]
tags: [anthropic, ai-lab, foundation-models, claude, public-benefit-corporation, long-term-benefit-trust]
since: 2021
confidence: 0.95
last_confirmed: "2026-11-23"
accessed_at: "2026-11-23"
source_count: 99
---

# Anthropic

AI safety and research company; publisher of the [[Claude]] family of models and the [[Anthropic Economic Index]] research series. Founded 2021 by **Dario Amodei** and **Daniela Amodei** (with a cohort of OpenAI departures) following the Amodei team's exit from [[OpenAI]] *"two or three OpenAI crises ago"* per [[2026-05-10-ries-lennys-force-destroys-companies-within|Ries 2026]]. **Public Benefit Corporation** with a **two-tier governance structure** (see [§Governance structure](#governance-structure) below). Partnered with [[Amazon Web Services]] (~$8B total invested as of 2024 per [[2026-04-28-werner-lebrun-octopus-organization]]). A new (not-yet-fully-released) Anthropic model, **Mythos**, surfaces in [[2026-06-22-grinstead-how-i-ai-mozilla-firefox-agentic-security-harness|Grinstead / How I AI (June 2026)]] as the model credited with Mozilla's Firefox security-bug spike — though Grinstead splits the credit ~50/50 between the model and the harness/pipeline.

## Governance structure

Per [[2026-05-10-ries-lennys-force-destroys-companies-within|Ries 2026]] (who advised the Amodeis on the structure during Anthropic's founding):

> *"Anthropic has directors on its for-profit board who are appointed by and are accountable to an outside group of trustees who are AI safety experts who do not have equity in Anthropic."*

The mechanism: **Long-Term Benefit Trust (LTBT)** as the **mission guardian** entity. Two-tier:

1. **For-profit board** — the standard corporate governance layer; directors operate under PBC fiduciary obligations.
2. **Long-Term Benefit Trust** — outside trustees who (a) are AI safety experts, (b) hold *no equity* in Anthropic, and (c) **appoint and hold accountable** the for-profit board's directors.

The novel structural property: trustee accountability **flows the right direction with respect to mission-relevant decisions** — directors are accountable to the trust (not to shareholders) on the mission axis. Ries' first-hand framing of what this buys: *"Whenever you see Anthropic do the right thing, like when they refuse to release a model because they think it's too dangerous, think about how much that's costing them."*

Ries (who plays *"no important role"* but *"a very big role"* in the founding-advice phase) was approached by *"one of their investors"* and told the Amodeis *"if you don't get this right, here's what's going to happen"* — the early framing that became the LTBT. Per Ries' framework, **PBC + LTBT** is **strictly stronger** than **PBC alone** ([[OpenAI]]'s post-2025 structure) because the LTBT introduces *outside trustee accountability* that PBC-alone does not.

[[2026-10-28-damodaran-anthropic-ipo-valuation|Aswath Damodaran's reading of the IPO prospectus (Oct 2026)]] adds the share classes: Class A for the public (one vote per share); employee shares that vote only on changes affecting the benefit trust; non-voting Class N shares with a share of profits and cash flows, held by Alphabet and [[Amazon]]; Class T shares held by the benefit trust, which appoints the majority of the board; and one Class F share held by the seven co-founders with 50.1% of the votes. He says the trust will be made up of people the founders picked, calls the structure *"dictator level corporate governance"*, and would still buy, but at *"a much bigger discount."* In Ries's account the trustees are AI-safety experts without equity; in Damodaran's, they are people the founders chose. The wiki has not ingested the S-1 itself.

## Research initiatives appearing in this wiki

- [[Anthropic Economic Index]] — recurring measurement of real-world Claude usage on Claude.ai (consumer) and 1P API (enterprise). Five usage reports plus the **labor-market-impacts** branch ([[2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai|Massenkoff & McCrory, March 2026]] — the "observed exposure" measure) through March 2026.
- Rwanda partnership with **ALX** — AI literacy + Claude Pro access program for African graduates ([[2026-04-28-anthropic-economic-index-q4-2025|fourth Economic Index report]]).
- [[Jack Clark]] — co-founder; serves on the [[AI Index]] steering committee.

## Platform / product engineering

- **Claude Platform** — Anthropic's developer-facing platform.
  - **Claude Managed Agents** — hosted service for long-horizon agent work; brain/hands/session decoupled architecture; published April 2026 ([[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Engineering blog]]); by July 2026 the service carries a shipped **outcomes** primitive (rubric + iteration/spend budget), a **"dreaming"** memory-distillation concept, and an evolving **agent identity / service-account** model — per the Claude Platform team's own panel discussion ([[2026-07-10-building-the-future-of-agentic-infrastructure|Building the future of agentic infrastructure]], the wiki's first first-party Claude Platform interview: **Jess Yann** — PM, Claude Managed Agents; **Katelyn Lesse** — Head of Engineering, Claude Platform; **Angela Jiang** — Head of Product, Claude Platform; all three dangling, single-source, deferred).
  - **Claude Agent SDK** — the packaging of Claude Code's building blocks for third-party agents. Described first-hand by **Isabella He** (Applied AI) in [[2026-08-19-he-databricks-anthropic-primitives-to-production-agents|*From Primitives to Production*]] (recorded April 2026, published August 2026) as *"the same building blocks as Claude Code, but allows you to put in your custom tools and custom system prompts and custom skills."* The same talk is the wiki's fullest first-party account of Anthropic's **agent design intent**: the LLM → code-orchestrated-workflow → agent progression; the **domain-specialisation reversal** (*"we used to think you might need almost an entire new harness for something like a research agent… instead of breaking down agents by domain, we actually see that it's more effective if we just think about agents as this really almost general purpose"*) with **code execution, file system, web search and to-do list** named as the domain-invariant primitives; **skills** as progressive disclosure against context pollution; **subagents** as context isolation rather than delegation; **hooks** as *"a way for you to inject a little bit of determinism into your agent"*; sandboxing as permission-prompt reduction; and **evals framed as the model-upgrade mechanism** rather than as a quality mechanism. Includes a live SRE-agent demo that closes the loop end to end (detect → diagnose → edit → redeploy → verify → resolve the page → publish a postmortem via MCP). No measurements of any kind — see the source page's scope warning.
  - **Claude Code** — agentic coding harness; described as "an excellent harness" in the Managed Agents post; its agentic architecture (splits coding work into smaller API calls labeled as distinct tasks) is the empirical signature of agent-mediated work in the [[2026-05-07-anthropic-economic-index-5-learning-curves|5th Economic Index report]]. Engineering leadership: [[Boris Cherny]] (10–15 concurrent Claude instances + CLAUDE.md as in-workflow learning capture per [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage 2026]]) and *Fiona Fung* (Director of Engineering; documents the Claude Code team-norms rewrite — JIT planning, code-wins-over-whiteboard debate, manager-starts-as-IC dogfooding, "Claudify everything", "explicit permission to kill processes" — in [[2026-05-08-running-an-ai-native-engineering-org]]). **Founder-vantage worked examples on Claude Code as substrate**: at $100M-ARR product scale by [[2026-05-13-jha-emergent-democratizing-app-building-with-claude|Jha at Emergent]] (multi-agent Kubernetes harness, system rewritten 4× in 9 months); at 2-FTE-startup-internal-ops scale by [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|Garg at AnswerThis]] (Claude Code CLI wrapped in Python with a self-extending coding sub-agent and an agent-editable `instructions.md`).
- **Claude Cowork** — the **non-coding surface on the Claude Code runtime**, not a separate product line. First-party origin and architecture from [[Lydia Hallie]] in [[2026-07-06-google-cloud-agent-factory-intent-driven-development|The Agent Factory, July 2026]]: Anthropic noticed *"back in December"* (2025) that *"a lot of our employees were using Claude Code for non-coding tasks — the marketing team was using it to create marketing files, data science, and so on"*, so *"we wanted to build **a better harness** for these types of tasks. And that's how Cowork came out in a week, because we of course use Claude Code to build Claude Cowork as well."* It *"still uses the Claude Code runtime underneath, so it can still do coding… we just have better connectors and better system prompts in Cowork to focus on that non-technical stuff."* Two things follow: the split is coding-vs-not by **context configuration**, not by engine, which is why [[2026-08-31-blum-how-i-ai-claude-cowork-pm-system|Blum's]] *"it's not Cowork in itself… Codex could be great for this as well"* is architecturally literal; and **Anthropic uses the [[agent-harness|harness]] vocabulary in its own voice**, for a term it did not coin. (An earlier characterisation of Cowork on this page as a *"collaborative-design product"* was wrong and has been corrected.) Also referenced by [[2026-04-26-how-to-win-when-software-is-not-a-moat-evan-spiegel-snapchat-ceo|Spiegel 2026]] in the *designers-shipping-code* discussion (alongside the named team member *Jenny Wen*, head of design at Claude, ex-Figma director — the move from Figma director to Claude IC designer is narrated by Spiegel as a case study in the *crits-as-core-skill* dimension of post-AI design work).

## Third-party uses of the Anthropic API

- **WikiZZ / LLM WikiZZ** ([[2026-04-18-mysore-medium-wikizz-extending-karpathy-llm-wiki|Mysore 2026]]) — single-author open-source browser-only extension of Karpathy's LLM Wiki pattern that routes API requests via a Cloudflare Worker CORS proxy to **NVIDIA NIM, Anthropic, and Gemini** as user-selectable provider backends. The wiki's first **third-party-developer-tool-uses-Anthropic-API** mention in the [[concepts/llm-wiki|LLM Wiki]] cluster. Surfaced here as a one-line context note; the substantive treatment is on the source page.
- **[[Khan Academy]]** ([[2026-07-14-khan-academy-ceo-the-real-ai-opportunity-is-in-boring-industries-sal-khan|Sal Khan interview, July 2026]]) — a **$1.2M/year** run rate; per Khan, Anthropic told the nonprofit it is "the top of the stack" among organizations leaning into agentic code review, with engineers "running five, six, seven, eight, nine, 10 agents simultaneously writing code, reviewing code."

- **Polsia** ([[2026-09-18-bloomberg-originals-how-china-plans-to-win-global-ai-race|Bloomberg Originals (Sep 2026)]]) — a San Francisco agent-automation startup whose founder chose Anthropic at launch (*"I need to give my customers the absolute best"*) and left when viral growth pushed the bill to **$1–1.5M a month**. Moving to Chinese open models cut it to about $100k. The corpus's clearest case of the scale point at which a frontier API stops being affordable. Bloomberg's cost test priced one task at about $50 on Claude Fable 5, against about $12 on Kimi K3 and about $4 on OpenAI's GPT-5.6 Luna.

## Models referenced in this wiki

- Claude Sonnet 4.5 — predominant model in the November 2025 Economic Index sample. Referenced as exhibiting "context anxiety" (premature task wrap-up) in the Managed Agents engineering post.
- **Claude Opus 4.5** — released between the 4th and 5th Economic Index sample windows. The Managed Agents engineering post notes that the "context anxiety" seen on Sonnet 4.5 was *not present* on Opus 4.5.
- **Claude Opus 4.6** — released coincident with the 5th Economic Index sample window (Feb 2026).
- Family-level cost/speed/performance tradeoff: Haiku (fast, cheap) → Sonnet (default) → Opus (most capable, higher per-token price). The 5th Economic Index report quantifies that users select Opus differentially for higher-value tasks: **+1.48 pp Opus per +$10/hour** task value (Claude.ai); **+2.79 pp per +$10** (1P API — about twice as steep).

## The Mythos restriction sequence (added 2026-09-15)

**Mythos** enters the wiki twice, and the two appearances are a year apart in tone. [[2026-06-22-grinstead-how-i-ai-mozilla-firefox-agentic-security-harness|Grinstead / How I AI (June 2026)]] credits it with Mozilla's Firefox security-bug spike, splitting the credit roughly evenly between model and harness. [[2026-09-10-sundararajan-wef-radio-davos-thrive-in-age-of-ai|Sundararajan / WEF Radio Davos (September 2026)]] treats the *same capability* as the reason the model became a governance object, and reads the sequence as **two phases with different governors**:

- **Phase one — self-restraint.** The code-generating capability *"posed a threat to the computer security of not just the country but of the globe, in terms of this capability could be harnessed to hack into any system,"* and *"the platform proactively said, as a responsible actor, we are not going to release it."*
- **Phase two — state control.** *"The US government has decided that it may be a threat to national security for non-US citizens — not just people in other countries but non-US citizens — to have access to it, and Anthropic has made the choice to simply not make it available to anyone… in part because they have a number of non-US citizens who work for them."*

Two details worth recording about Anthropic specifically. First, the compliance route — **withdrawing the model from everyone** — was determined by the company's own **workforce composition** rather than by any property of the risk: a restriction framed around who may *access* the model was satisfiable only by making it available to nobody. Second, the episode places Anthropic on both sides of the governance line within months: the actor exercising voluntary restraint in phase one, and the object of an involuntary instrument in phase two.

Sundararajan's reading of what it portends is explicitly provisional — *"we're going to be making it up as we go along, and it's going to be both the government doing that and the platforms doing it."* **Caveat:** this is an interview account, recalled from memory, with no document cited. The wiki has not ingested primary reporting on the restriction, and Anthropic's own account of it is not represented here at all. See [[responsible-ai]] for the governance-authority framing and [[ai-sovereignty]] for the state-capacity one.

**After the restriction: an open-weight match, as relayed (added 2026-10-03).** [[2026-09-30-chow-metalware-ai-firmware-vulnerability-research|Chow (Metalware), at YC Root Access on 30 September 2026]], told a defense audience that Anthropic *"published a report literally yesterday saying that Mythos-level capabilities are now available for download, open source, for all of our adversaries to use, with similar performance to Mythos."* The report he means appears to be Anthropic's post of 29 September 2026, *GLM-5.3 and the spread of advanced cyber capabilities* (read on the web 2026-10-03, not ingested). It compares Zhipu AI's open-weight GLM-5.3 with Mythos Preview on exploit benchmarks and argues for giving defenders wider access to Claude's cyber capabilities. If that identification holds, the sequence on this page has a third step: the company that withheld Mythos is now the one documenting a comparable capability in someone else's downloadable model. The wiki holds a forecast of this, from [[2026-05-21-jones-stanford-gsb-ai-and-our-economic-future|Jones]] on 1 May (*"in six months, in a year"*), and an earlier version of the claim, from [[2026-05-05-loukides-radar-trends-may-2026|Loukides's May digest]].

## A model release that triggered an architecture demolition (added 2026-09-16)

[[2026-08-10-maza-a16z-kavak-rebuilding-a-company-around-ai|Maza / Kavak, August 2026]] supplies an unusual datapoint about what a model release does downstream. Kavak had *"tens of thousands"* of function-decomposed agents running its business at scale. Then, in Maza's account, **Opus 4.5** changed the right architecture:

> *"Opus 4.5 came out and I realized this isn't the right paradigm anymore — the intelligence now doesn't need the graph and the multi-agent lattice work and harness, because it will constrain this level of intelligence."*

Kavak scrapped two years of working infrastructure and rebuilt around one long-running agent per customer. This is the wiki's first account of **a named Anthropic release causing a customer to remove scaffolding rather than add it** — the capability-overhang argument made concrete and expensive. Anthropic is otherwise absent from that episode; the claim is the customer's. See [[agent-harness]] and [[multi-agent-failure-modes]].

## As a flow-state organisation

Two recent sources name Anthropic specifically as a *flow-state organisation* — a place where structural pressure + lack of hierarchy strips away traditional thinking:

- [[2026-05-10-ries-lennys-force-destroys-companies-within|Ries 2026]] frames it from the **governance** layer: PBC + LTBT make the structural mission-protection real.
- [[2026-05-05-stanford-ai-club-chamath-on-how-to-win-in-the-ai-era|Chamath 2026]] names it from the **operating-structure** layer: *"if you find one of these places — Anthropic is such a place, OpenAI is such a place, Facebook was such a place, Google was such a place, SpaceX is such a place"* — alongside no-org-chart and chronic-under-hire as deliberate organisational design.

The two framings are at different layers (governance vs operating-structure) but converge on Anthropic as **the AI-era exemplar** of the category.

## Named from outside, September 2026 (added 2026-09-21)

- [[2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over]] — IBM's CEO agrees with Anthropic that LLMs are good at translating legacy code such as COBOL, but disputes the inference that this threatens the mainframe: mainframes are used for transaction volume, not because of language lock-in.
- [[2026-09-18-swisher-lafrance-atlantic-festival-tech-economy-is-ai-reshaping-america]] — Kara Swisher predicts the seven frontier labs will consolidate to two, and names Anthropic as *"probably"* one of the survivors alongside Google. Opinion, no figures.

- [[2026-09-30-michael-miller-department-of-war-ai-adoption]] — US Under Secretary of War Emil Michael names *"Anthropic's leadership"* among those who signed a White House compact *"for the safe development of superintelligence"* the day before the YC event (livestream published 30 September 2026), committing, in his account, to *"auditing and independent evaluations"*. His description only; the compact's text is not in the wiki. It is the wiki's second account this quarter of Anthropic in US AI governance, after the Mythos sequence above.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "anthropic")
SORT file.name ASC
```

## Open questions

- The wiki has multiple references to Claude as a measurement substrate but no primary source on Anthropic itself yet; this entity page is a stub awaiting first-party Anthropic source ingestion.

## Cited as its own customer (added 2026-09-28)

[[2026-02-14-tan-yc-the-new-way-to-build-a-startup|Garry Tan's "20x company" episode]] opens with an Anthropic engineer's post that Claude wrote Claude Cowork and that developers each manage *"anywhere between three and eight Claude instances"*. Tan uses it as the example that sets his whole argument up.

## Factory on the Claude channel (added 2026-10-30)

[[2026-10-23-grinberg-gill-claude-factory-autonomous-software|Grinberg (Factory, on the Claude channel, Oct 2026)]]: Matan Grinberg credits Opus with less human oversight of plans. [[2026-10-25-tremante-cloudflare-connect-open-agentic-internet|Tremante (Cloudflare Connect, Oct 2026)]] shows Anthropic's crawl-to-referral ratio at 486.6 : 1 on Cloudflare Radar.

## A 2,000-person company on Claude (added 2026-11-04)

[[2026-10-29-van-der-voort-bnr-remote-builds-everything-with-ai|Van der Voort (Remote) on BNR (Oct 2026)]]: Remote's CEO says it uses *"a lot of models from Anthropic and a few others,"* plus security-specialised models from Anthropic and OpenAI, and finds local models not good enough for most of its work.

## The IPO prospectus, as Damodaran reads it (added 2026-11-16)

[[Aswath Damodaran]] values Anthropic in [[2026-10-28-damodaran-anthropic-ipo-valuation|a session recorded two days after it filed its 416-page S-1 (Oct 2026)]]. The first four bullets are his reading of the filing, spoken over slides; the last two are his own valuation. The S-1 itself is not in the wiki.

- **Growth:** revenue up 1,300–1,400% year on year; more than $16 billion in the last reported quarter; a run rate that could reach $100 billion by year end. Third-quarter figures are not in the filing; investor meetings indicate that growth *"seemed to have stalled,"* which Anthropic attributes to a compute constraint.
- **Customers:** 11,900, about 1,900 of them spending more than $1 million (the threshold that defines the 11,900 is not spoken); the top five account for about 25% of revenue; 80% of revenue comes from usage rather than subscriptions, and from enterprises (the transcript leaves open whether that is one share or two).
- **Costs:** compute costs down from 250% of revenue six quarters earlier to under 50%; an operating profit in the last quarter reported; a gross margin close to 80% once the 15–20% revenue share owed to big-tech partners, which Anthropic books as marketing, is moved into cost of goods sold. The move is his adjustment.
- **Commitments and capital:** more than $450 billion of contractual compute commitments (more than $600 billion in all), with Broadcom the largest single beneficiary; $114 billion raised recently and held as cash.
- **His valuation:** his own assumptions, none of them in the prospectus. About $1.48 trillion of equity, on $1 trillion of revenue in 2036, a 27.5% target margin, a 9.74% cost of capital and a 10% failure risk, with the present value of the contractual commitments subtracted as debt (the figure differs between his two talks; see the next bullet). His worst case is −$373 billion, his best case $4 trillion. Anthropic had not listed when he spoke, so the $1.48 trillion is his estimate of value, not a market price. He expected the offering to be priced at $1.5–2 trillion.
- **The follow-up:** [[2026-11-03-damodaran-anthropic-valuation-feedback-loop|Damodaran (Nov 2026)]] keeps the valuation ($1.45–1.5 trillion) and ranks the inputs he is least sure of: target revenues, then governance (seven founders who *"operate in an echo chamber"*), profitability, reinvestment and regulatory risk. Here he gives the present value of the contractual commitments as about $373 billion; the first session subtracted $473 billion of debt, described there as the same present value. Neither transcript reconciles the two. He uses a pre-tax cost of debt of about 6.5%, on the BB+ rating that the Financial Times reported as likely, and on failure risk says *"Anthropic is no CoreWeave."*

## In the AI100 2026 report (added 2026-11-22)

The [[2026-11-10-ai100-ai-goes-mainstream-2026|AI100 2026 report]] returns to Anthropic repeatedly:
- **Claude Mythos Preview** found thousands of zero-day vulnerabilities across every major operating system and browser, more than 99% unfixed at disclosure, and was withheld from public release. Access was reportedly compromised through a third-party vendor. **Project Glasswing** brought eleven partners together to use the model defensively.
- **A dispute with the U.S. Department of Defense** over offensive use, after reports that Claude, deployed through Palantir, contributed to the January 2026 operation that seized Nicolás Maduro.
- **A June 2026 U.S. ruling** denying non-U.S. users access to Anthropic's leading models, which the report treats as the sharpest example of dependence on foreign-owned systems.
- **The $1.5 billion settlement** of the pirated-books case, *"the largest copyright settlement in legal history."*
- **Claude Fable's** one-line counterexample to the Jacobian conjecture.
- **Interpretability work** rating about 70% of extracted features interpretable.
- **Watermarking** announced in August 2026 in response to EU transparency rules.
- **An imminent IPO**, with Anthropic *"eyeing a market valuation of over $2 trillion."*

## Claude in an industrial multi-agent run (added 2026-11-23)

In [[2026-11-19-falkor-nvidia-omniverse-ai-agents-industrial-operations|Falkor's agent traces (NVIDIA Omniverse livestream, Nov 2026)]], three of the four agents run in Claude: the run coordinator on *"opus-5-5"*, the result validator on *"sonnet-5-5"*, and the memory manager. The task runner runs in Codex. NVIDIA's Ganesh Sivaraman credits the work to *"Astra and Opus 5.5."* The model names are from the workbench screen, not from Anthropic.

## In the Raise US coalition (added 2026-11-23)

At [[2026-11-19-raimondo-holcomb-harvard-iop-managing-unemployment-ai-economy|Harvard's Institute of Politics (Nov 2026)]], a student moderator names Anthropic as one of the AI companies in the coalition of Raise US, the workforce-transition nonprofit chaired by Gina Raimondo and Eric Holcomb, and asks whether Dario Amodei acts from altruism. Raimondo: *"you'd have to ask him"*; AI firms *"understand it's bad for their business if they don't figure out some solutions to the potential harms of AI,"* and *"I would think they're funding us so we can help find some solutions."* She criticises naming AI's harms *"without offering any solutions,"* which she says has created *"mass panic."* The moderator cites Amodei's prediction that half of entry-level white-collar jobs could go by 2027 or 2028, and a student, *"ahead of tomorrow's IPO,"* attributes to Anthropic a *"$40 trillion"* market opportunity, *"the aggregate of all knowledge work"*; the figure is not checked against the prospectus.

## Rented for building, priced against open weights (added 2026-11-23)

In [[2026-11-20-saedi-odd-lots-chinese-open-weight-models|Saedi's Odd Lots interview (Nov 2026)]], Minerva builds its product with Claude (*"cloud"* in the captions) and moves repeatable tasks to fine-tuned open weights. Saedi puts an abliterated DeepSeek model at about a hundredth of the price of Fable (*"about ten [times] cheaper than Sonnet, which is about ten [times] cheaper than Fable"*) and below Claude Mythos in capability. He accepts that the labs do not train on corporate client data, but says a rented model *"doesn't get any better based on your use case."* A host speaks of companies paying *"an Ant[hropic] tax or an OpenAI tax."*
