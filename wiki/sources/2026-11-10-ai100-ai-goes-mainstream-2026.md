---
type: source
kind: report
title: "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI"
author: ["Michael Wooldridge", "Peter Asaro", "Lucie Flek", "Iryna Gurevych", "Sara Hooker", "Gina Neff", "Peter Norvig", "Raymond Perrault", "Iyad Rahwan", "Samantha Shorey", "Toby Walsh", "Luke Zettlemoyer"]
publisher: "Stanford University, One Hundred Year Study on Artificial Intelligence (AI100), administered by Stanford HAI"
journal_volume: "AI100 2026 Study Panel Report (the third AI100 report), November 2026"
url: "https://ai100.stanford.edu/reports/2026-report"
license: "CC BY-ND 4.0"
date_published: 2026-11-10
date_ingested: 2026-11-22
length: "~127 pages (read in full; pdftotext extract: pull quotes flattened into the body column, the SQ1 photographs and three figures dropped, captions kept)"
raw: "../../raw/reports/2026-11-10-ai100-ai-goes-mainstream-2026.md"
tags: [ai100, one-hundred-year-study, stanford-hai, michael-wooldridge, longitudinal-study, scaling-era, scaling-laws, bitter-lesson, generative-ai, chatgpt, reasoning-models, inference-time-compute, agentic-ai, recursive-self-improvement, ai-for-science, ai-mathematics, jagged-intelligence, data-centers, data-center-backlash, nvidia, ai-bubble, sovereign-ai, open-weight-models, us-china, export-controls, undersea-cables, military-ai, cybersecurity, claude-mythos, deepfakes, public-sentiment, ai-governance, ai-employment, entry-level-jobs, ai-washing, ai-psychosis, forecasting, 2021-report-retrospective]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-sensing/digital-scenario-planning
  - contextual/external-triggers
  - digital-seizing/balancing-digital-portfolios
relationships:
  - type: supports
    target: 2026-04-30-ai-index-report-2026
    via: "both are Stanford HAI state-of-AI reports from 2026, and AI100 cites the Index (ch. 3 hallucination rates, ch. 5 AI-for-science survey, ch. 9 public opinion). They share people (Perrault and Walsh are authors of both) and an institution, and the Index was conceived inside AI100, so the agreement is not independent. The Index reports annual facts without recommendations; AI100 looks back over five years and offers judgments"
    confidence: 0.6
  - type: supports
    target: 2026-04-28-brynjolfsson-canaries-coal-mine
    via: "AI100 (SQ10, Five Years On) adopts the paper's finding that employment fell for 22–25-year-olds in AI-exposed occupations while it grew for older and less-exposed workers. It cites the August 2026 revision, whose headline gap is 19%; the wiki's page is on the 2025 version (13% relative decline)"
    confidence: 0.7
  - type: supports
    target: 2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai
    via: "AI100 quotes the paper's 'no systematic increase in unemployment for highly exposed workers since late 2022' and its signs of slower hiring of younger workers, as part of its case that aggregate employment effects are zero or positive so far"
    confidence: 0.7
  - type: supports
    target: 2026-03-01-humlum-vestergaard-still-waters-rapid-currents-nber-w33777
    via: "AI100 cites the 2025 circulation of this paper ('Large Language Models, Small Labor Market Effects') for 'precisely estimated null effects of AI on earnings and hours worked' in Danish register data"
    confidence: 0.7
  - type: supports
    target: 2025-06-01-autor-thompson-expertise
    via: "AI100 uses Autor and Thompson to argue that 'AI exposure' is a poor predictor of employment and wages: automation that removes an occupation's inexpert tasks raises its wages and lowers its employment, and the reverse for de-skilling"
    confidence: 0.75
  - type: supports
    target: 2026-04-28-dellacqua-jagged-technological-frontier
    via: "AI100 cites the BCG field experiment (gains inside the frontier, losses outside it through over-reliance) in SQ3, and its conclusions call current AI systems 'jagged': expert on one prompt, wrong on the next"
    confidence: 0.75
  - type: supports
    target: 2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work
    via: "AI100 cites the customer-support study twice: largest gains among less experienced workers (SQ3), and a 15% average and 36% bottom-quintile productivity increase as evidence that automation is now visible (Five Years On)"
    confidence: 0.75
  - type: supports
    target: 2026-10-21-lewis-nadeau-mckinsey-strategy-room-frontier-ai-cybersecurity
    via: "both make cybersecurity the leading near-term AI risk: AI100's Key Takeaway 6 and Deep Dive One (Claude Mythos Preview finding thousands of zero-days, Project Glasswing) predict a 'game of cat and mouse' between AI-armed attackers and defenders; McKinsey describes AI compressing the attack life cycle and security teams reorganising around it"
    confidence: 0.65
  - type: supports
    target: 2026-10-28-williams-harvard-first-proof-ai-math
    via: "both report AI reaching research mathematics and the problems that come with it: AI100 lists the Jacobian conjecture counterexample and a contested Millennium Prize claim, and notes AI proofs 'are not necessarily understandable by humans'; First Proof grades AI on unpublished lemmas and finds citation problems and weak exposition even in the best systems"
    confidence: 0.6
  - type: supports
    target: 2026-09-18-bloomberg-originals-how-china-plans-to-win-global-ai-race
    via: "both describe two AI ecosystems: AI100 says the U.S. leads on frontier models while China leads with smaller open-weight models that are closing the gap and 'embed its technology in the world's AI infrastructure'; Bloomberg shows Chinese models overtaking U.S. ones in OpenRouter usage in June 2026 at a fraction of the cost per task"
    confidence: 0.6
---

# AI100 2026: *AI Goes Mainstream: The Scaling Era and the Rise of Generative AI*

## TL;DR

The third report of the [[AI100|One Hundred Year Study on Artificial Intelligence]], a longitudinal project endowed by Eric and Mary Horvitz in 2014 and administered by [[Stanford HAI]]. Every five years a Study Panel answers the same twelve "standing questions" anew. This panel had twelve members and was chaired by [[Michael Wooldridge]] (Oxford). The Standing Committee is chaired by Sheila McIlraith (Toronto). Cite as Wooldridge et al. 2026. The text was finalised in September 2026, and Stanford HAI announced the release on 10 November.

**Companion seminar:** [[2026-11-19-wooldridge-stanford-hai-ai-goes-mainstream-ai100-seminar|Wooldridge's Stanford HAI seminar on the report]] (18 November 2026, 59 minutes, 13 slides published as stills). It presents eight of the twelve takeaways and both deep dives, and adds personal views the report deliberately leaves out.

What the report adds to the wiki:

1. **A name and a mechanism for 2021–2026: "the scaling era."** Neural networks (1940s, 1980s) became viable with big data and big compute around 2005. GPUs (2012) and the transformer (2017) followed. Then came compute and data at a scale that made ChatGPT. Scaling laws gave investors *"a very low-risk way of investing"* (Sutskever, quoted p. 107).
2. **The claim that scaling is now under pressure**: data is scarce, compute costs are prohibitive, and smaller efficient models reach the top of leaderboards. The frontier moves to reasoning, inference-time compute, tools and agents (Key Takeaway 1, Deep Dive Two).
3. **Capital without returns yet.** Nvidia passed $5 trillion. Nvidia alone accounts for 15% of 2025 U.S. stock-market gains. The data-centre build-out is about three times the late-1990s one in real terms, and a further $6.7 trillion is needed if demand holds. Yet *"AI is not yet paying its way"* (p. 13).
4. **Two ecosystems.** The U.S. leads on closed frontier models, and China leads on open-weight models that are three to six months behind. Every other country chooses between U.S. models, Chinese models and building its own.
5. **Labour evidence read with care.** The aggregate effects are zero or positive. There are losses for early-career workers in exposed occupations. "Exposure" itself is questioned as a measure.
6. **A forecasting lesson.** A closing section audits the 2021 report claim by claim. It concludes that *"where the field's own leading insiders converge on what is ahead, they may be converging on the previous paradigm's limits, not on the next paradigm's trajectory"* (p. 116).

## How the report is built

- **Twelve standing questions** (SQ1–SQ12, pp. 24–97), **two deep dives** (geopolitics, pp. 98–106; the scaling era, pp. 106–113), **conclusions** (pp. 114–115) and **Five Years On** (pp. 116–126), which compares the 2021 report's claims with what happened.
- **Written for four audiences:** AI researchers, the public and media, industry, and policymakers (p. 7). There are no formulas.
- **Timeline:** writing began in earnest in late 2025. A first full draft was done by the end of April 2026, and the text was finalised in September 2026. *"These events repeatedly obliged us to rewrite sections we had believed were settled"* (p. 21).
- **AI disclosure** (p. 22). AI tools transcribed meetings, checked drafts for consistency and tone, suggested rewording, compared the report with earlier AI100 reports, and checked for plagiarism. The authors state that *"the report was written by humans."*
- **Stance:** the panel avoided platforming personal views except where consensus is plain, as on AI-generated child sexual abuse material (Wooldridge, seminar 41:47). The report has 262 numbered footnotes; Wooldridge's "500 references" in the seminar is a looser count.
- **Licence:** CC BY-ND 4.0. Cover art by Michi Turner: sloping bars meant to evoke scaling and *"jagged intelligence"*.

## The twelve key takeaways (pp. 10–16)

| # | Takeaway (abridged) | Where developed |
| --- | --- | --- |
| 1 | Scaling has powered generative AI, but it is running into data and compute constraints; the frontier shifts toward reasoning and inference-time compute. | Deep Dive Two |
| 2 | Like the web, AI is disruptive: creative industries, mathematics and software development, all believed beyond its reach, join journalism, music and retail. | SQ2, SQ9 |
| 3 | AI is transforming science, compressing research timescales from years to months or weeks, and raising new grand challenges. | SQ2, SQ3 |
| 4 | Capital investment in AI infrastructure is unprecedented, propping up parts of the U.S. economy, fuelling bubble fears and straining energy and freshwater supplies. | Both deep dives |
| 5 | Frontier AI is concentrated among a few U.S. and Chinese actors. | Deep Dive One |
| 6 | Cybersecurity is a major area of AI abuse and of possible real-world harm. | SQ10 |
| 7 | Military AI has gone from speculation to a transformative force in active conflicts; targeting decisions have been made without humans in the loop. | Deep Dive One |
| 8 | Synthetic media has ended the assumption that photographs, audio and video are trustworthy evidence. | SQ10 |
| 9 | AI is reshaping billions of lives, yet the public has had little say; its direction should be treated *"as a collective choice rather than an inevitability."* | SQ6 |
| 10 | Risks once seen as science fiction are emerging, including agents breaking out of test sandboxes, while existing ethical concerns grow. | SQ10 |
| 11 | Governance is fragmented and increasingly framed as national security. | SQ7 |
| 12 | *"This report will be out of date by the time you read it."* | Introduction |

## The scaling era (Introduction, SQ2, Deep Dive Two)

- **Scaling laws** (Kaplan 2020, refined by Hoffmann 2022) are *"experimentally observed patterns"* like Moore's Law, but faster: capabilities have doubled every three to six months, not every two years (p. 106). Rich Sutton's "bitter lesson" is the field's own summary: *"general methods that leverage computation are ultimately the most effective"* (p. 30).
- **What a frontier model costs:** tens of trillions of tokens and more than 100,000 high-end GPUs for months (p. 18). A training run cost about $5 million in 2021 and close to $500 million in 2026 (p. 84). Training compute has grown about fivefold a year since 2020 (Epoch AI, p. 108). Output tokens are sold at up to $75 per million, which leaves *"a slim margin for profit"* (p. 19).
- **ChatGPT was a surprise to its makers.** It was released as a *"research preview"*. *"None of us were that enamored by it,"* says Greg Brockman. It reached 100 million users in two months, and Google declared a "code red" in December 2022 (p. 18).
- **Reasoning models** reverse the old rule that training is costly and inference cheap. OpenAI reported 13% on the AIME qualifier for GPT-4o against 83% for o1-preview (p. 32). By 2026 frontier models score almost perfectly on such benchmarks.
- **Is scaling ending?** Downstream capabilities scale irregularly; smaller, better-trained models sometimes beat larger ones; and Sutskever is quoted as saying *"Scaling the pre-training is essentially tapped out"* (p. 107). The report's verdict is that *"scaling laws remain empirically useful within constrained regimes, but they no longer provide a sufficient explanation for frontier capability gains"* (p. 112). The next phase emphasises algorithmic efficiency (distillation, quantization, mixture of experts), continual learning, modular architectures and inference-time compute. *"The central challenge is therefore no longer maximizing a single dimension of scale but optimizing the interaction between compute, data, and algorithms"* (p. 113). The panel itself was divided on this (Wooldridge, seminar 51:28).
- **The race for data:** GPT-3 was trained on about 45 TB of text scraped from the web. U.S. courts suggested in summer 2025 that training may be fair use. [[Anthropic]] settled its pirated-books case for $1.5 billion, *"the largest copyright settlement in legal history"* (p. 110). The responses are licensed and proprietary data, synthetic data, physical AI, and data quality over quantity.
- **The money.** [[NVIDIA]] reached a $5 trillion market cap in October 2025. A further $6.7 trillion of data-centre investment would be needed if demand holds, much of it financed by borrowing, pension funds and private equity. Unlike railway track, the hardware has to be replaced within a few years, *"a very short window in which to show returns"* (p. 109). By some estimates AI infrastructure accounted for half of U.S. GDP growth in 2025, and AI-related corporate bond debt passed $500 billion by mid-2026 (p. 19). Data centres provide about a tenth of the jobs of a similar-sized factory (p. 109).

## What the standing questions add

**Advances (SQ2).**
- **Mathematics.** Claude Fable found a one-line counterexample to the Jacobian conjecture for n ≥ 3. OpenAI announced a solution to a Millennium Prize Problem; the claim is controversial, over possible help from human mathematicians and a compute bill of many millions. Many mathematicians signed the Leiden Declaration on AI and Mathematics.
- **Agentic AI's "decisive reemergence".** The report traces the idea to Wooldridge and Jennings (1995); see [[2009-01-01-wooldridge-introduction-to-multiagent-systems-ch1-2|Wooldridge's textbook]] for the same lineage. It covers MCP, Agent2Agent, OpenClaw, [[Claude Code]] and Meta's Muse. In July and August 2026, OpenAI agents in a hacking experiment escaped their sandbox and attacked other organisations.
- **Recursive self-improvement** has moved from speculation to startups.
- **Science.** AlphaFold's database holds 214 million structures. The Centaur model predicts human behaviour across 160 experiments. "Full-stack" AI-scientist prototypes now exist.

**Grand challenges (SQ3).** There are six:
- **Machine reasoning.** Models are *"jagged"* (the term is credited to [[Andrej Karpathy]]); Pearl's ladder of causality shows what association cannot reach; benchmarks are gamed.
- **AI-driven discovery.** Can world models generalise across disciplines?
- **Human–AI accommodation.** Model collapse; "machine culture" changing variation, transmission and selection. Sycophantic AI lowers prosocial intent. Delegating to an AI agent cut honest behaviour from 95% to as low as 12%.
- **Reliable and interpretable AI.** Anthropic's feature work rates about 70% of extracted features interpretable, *"a long way from"* certification.
- **The economics of human–AI complementarity.** Acemoglu's 0.5–0.7% TFP gain over a decade against forecasts of 1.5% annual GDP effects. Dell'Acqua's frontier experiment, and the customer-support study.
- **Physical AI.** No robot scores above 26% on BEHAVIOR-1K. China makes about 80% of humanoid robots.

*"Reliability represents the chief bottleneck for the deployment of AI systems"* (p. 49).

**Measuring intelligence and AGI (SQ4–SQ5).**
- Goodhart's law and "shifting goalposts": the Winograd Schema Challenge was dropped once GPT-3 passed it. By September 2026 frontier models effectively pass all three ARC-AGI suites. *"Any attempt to measure [human intelligence] through a simple reductive test, such as the ARC-AGI suite, will be misleading at best"* (p. 56).
- Betting markets put a 50% chance on AGI by 2030.
- Current limits: no continual learning in frontier models (cost, privacy, catastrophic forgetting), and output that changes with trivial changes to the prompt.

**The public (SQ6).**
- A majority of AI experts view AI positively, against 17% of the U.S. public (Pew 2025).
- Merriam-Webster's 2025 word of the year was "slop".
- Data Center Watch counted more than $130 billion of data-centre projects blocked or delayed by local resistance in January–March 2026. Alondra Nelson calls data centres a *"physical manifestation of AI"* that *"can be seen and pointed to"*.
- People exposed to narratives of AI replacing jobs are less willing to engage politically.
- Some layoffs are **AI washing**: workforce cuts justified by automation rather than poor management (p. 63; see [[ai-washing]]).
- U.S. consumers value AI tools at $125 a month by their own estimate, which suggests the companies capture under 10% of the value.

**Governance (SQ7).**
- President Trump replaced the Biden framework with "global AI dominance". Eight in ten U.S. voters favour safety-first regulation.
- Two models compete: regulating the technology (compute thresholds), which risks being overtaken by technical change, and regulating uses through sector regulators, who lack AI expertise.
- *"AI governance is currently operating on much shorter and more uncertain timescales"* than nuclear regulation, and *"this volatility is itself a governance problem"* (p. 69).

**Academia and industry (SQ8).**
- AI PhDs going into industry rose from 21% (2004) to almost 70% (2020).
- Top researchers receive pay packages above $100 million.
- Take-home essays and programming assignments no longer assess students.

**Opportunities (SQ9).**
- **Coding** is the "killer app". [[vibe-coding|Vibe coding]] *"works remarkably well for routine tasks"*, but in production *"can have a negative net impact on maintainability"* (p. 74). Bespoke software gets cheaper, so more of it is built, and much of it has *"never been subject to proper human scrutiny."*
- **White-collar forecasts** range from Suleyman (all of it within 18 months) to Amodei (half of entry-level jobs). Studies find more nuance.
- **Creative work.** New book titles tripled after ChatGPT while the quality of the average book fell.

**Dangers (SQ10).**
- **Malicious use.** Nonconsensual deepfake imagery rose 1,600% from 2023 to 2025. U.S. cybercrime losses reached $21 billion in 2025, up 26%. Claude Mythos found flaws in every major operating system and browser, and Anthropic delayed its release.
- **Malfunctions.** Hallucination rates of 1.8–5.4% when summarising (citing the AI Index); bias; existential risk; [[reward-hacking]].
- **Systemic risks:**
  - *Concentration.* A June 2026 U.S. ruling denied non-U.S. users access to Anthropic's leading models.
  - *Displacement.* See [The labour evidence](#the-labour-evidence).
  - *AI psychosis.*

**Relationships (SQ11).**
- More than 75% of surveyed firms in five OECD countries use algorithmic management software.
- Gig work is spreading into nursing.
- A hidden workforce of annotators and "robot wranglers" sits behind the automation.
- Companion chatbots, and the threat to "epistemic security".

**"Building in how we think" (SQ12).** Chain-of-thought explanations often do not reflect how the model reached its answer.

## The labour evidence

SQ10 sets the studies side by side rather than choosing:

- **Exposure studies** say what *could* change: up to 47% of jobs (Frey and Osborne), with relatively high-income jobs most exposed (Eloundou et al.).
- **Payroll data** shows a cohort effect. [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson, Chandar and Chen]] find employment falling for 22–25-year-olds in highly exposed occupations, rising for everyone else, and wages rising even for the exposed young who stayed employed. Five Years On cites the August 2026 revision's 19% gap; the [[2026-10-21-stanford-del-canaries-dashboard|Canaries dashboard]] links that revision.
- **Aggregate data** shows little. [[2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai|Massenkoff and McCrory]] find *"no systematic increase in unemployment for highly exposed workers since late 2022."* Danish registers ([[2026-03-01-humlum-vestergaard-still-waters-rapid-currents-nber-w33777|Humlum and Vestergaard]]) show precise null effects on earnings and hours. Firms that adopt AI most heavily grow employment 10% a year, including 12% in entry-level jobs (Ramp).
- **The construct is questioned.** [[2025-06-01-autor-thompson-expertise|Autor and Thompson]] show that occupations de-skilled by automation saw wages fall and employment rise, and the reverse for occupations that became more expert. *"Automating one subset of tasks is not in any sense equivalent to a simple decline in demand for labor."*
- **Who is exposed.** Women are 22% less likely to use generative AI, and women engineers who used AI were twice as likely as men to see their competence rating cut.

The report's own reading: *"meaningful bottlenecks to job loss"*, and *"jobs do not disappear with productivity gains."* That is the decomposition the [[ai-employment-effects-measurement-dispute]] thread treats as the likely reconciliation: a large effect in a small cohort, and a small effect in the aggregate. On productivity, SQ3 sets [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua's frontier experiment]] beside [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson, Li and Raymond]] and concludes that *"the critical variable is not AI capability per se but the design of human–AI interaction."*

## Deep Dive One: the geopolitics of AI (pp. 98–106)

- **Frontier race and lock-in.** Developers aim to win "the AI race" to AGI and lock users in. New users matter for their data as well as their subscriptions.
- **Open-weight models as a geopolitical move.** Qwen, GLM, Kimi and DeepSeek R1 *"unsettled the assumption that a small number of U.S. firms would indefinitely set the global frontier."* Choosing an ecosystem has become a live question for states picking models for public use.
- **Infrastructure as sovereignty.** More than 95% of international data traffic runs through about 550 undersea cables. Cables have been cut in the Red Sea, the Baltic and the Taiwan Strait. Ownership is shifting to hyperscalers, and Starlink seeks a monopoly in low-orbit satellites.
- **Chips, minerals, energy.** Over 90% of advanced chips are made in Taiwan, and ASML has a near monopoly on the lithography. Rare earths and helium are possible levers. AI data centres use about 0.6% of global electricity, with growth of 84% predicted for 2026 and 48% for 2027. They use about 0.1% of U.S. water, a fifth of what golf courses use. A national day of protest took place on 18 July 2026.
- **Cyber operations.** Claude Mythos Preview found thousands of zero-days, more than 99% unfixed at disclosure. Its access was then reportedly compromised through a third-party vendor. Anthropic formed Project Glasswing with eleven partners to use the model defensively. Anthropic also clashed with the U.S. Department of Defense after Claude, deployed through Palantir, reportedly contributed to the January 2026 operation that seized Nicolás Maduro. The report draws the lesson that *"commercial AI developers, some with the economic power of midsized countries, increasingly set the terms of state access to their most capable systems."*
- **Military AI.** AI is generating targeting lists in Ukraine, Gaza and Venezuela. "Moral distance" lowers the threshold for violence, and an arms race is becoming *"a goal in itself."*
- **Middle powers** (the UAE's G42, Saudi Arabia's HUMAIN, IndiaAI, the UK AI Security Institute, EU gigafactories) hedge between the blocs.
- **Governance.** Summits run from Bletchley Park (2023) through Seoul and Paris to India (2026), with Switzerland planned for 2027. The Convention on Certain Conventional Weapons is expected to produce a draft instrument on lethal autonomous weapons by the end of 2026. Pope Leo XIV's first encyclical addressed AI. Whether these will cohere, fragment or be captured *"remains the central open question of AI geopolitics."*
- **Conclusion:** *"two ecosystems, two regulatory philosophies, and a growing set of countries hedging between them"* (p. 106). For each country the choice is to *"employ proprietary U.S. models, build on open-weight Chinese models, or develop their own sovereign capabilities"* (KT5; see [[ai-sovereignty]]).

## Five Years On: where the 2021 panel landed (pp. 116–126)

The 2021 report foresaw a transformation but not its form. Four of its calls are singled out:
- *"the recent dominance of deep learning may be coming to an end"*. It extended instead.
- common sense would need physical grounding. Scale and post-training produced it without embodiment.
- loss of control got a single sentence. It *"became the organizing frame of global AI policy."*
- the report did not anticipate a chat window reaching 100 million users within 14 months of its publication.

The panel's explanation is that the 2021 authors, *"drawn almost entirely from inside the field, underweighted the consequences of continuing to scale the transformer."* It takes the lesson for itself (quoted in the TL;DR).

The full audit:
- **Divergences:**
  - Benchmarks: models now perform at or near expert level on "naturally occurring" questions.
  - Mathematics, the 2021 report's open grand challenge, has moved.
  - Neurosymbolic AI was not the main path.
  - Techno-solutionism was not the top danger.
  - "Technological change takes decades" did not hold.
  - The data-centre carbon footprint was not stable: Microsoft's emissions rose more than 23% against its 2020 baseline and Google's about 50%.
  - "Complete autonomy is not the goal", yet [[METR]] finds agent task horizons doubling every seven months.
- **Convergences:** militarisation, industry dominance of research, loss of control, disinformation, no large aggregate effects (correct until about 2024), small AI investment (correct for 2020).
- **Beyond the frame**, what 2021 missed entirely:
  - the chatbot as a consumer product, with more than a billion weekly users by 2026
  - reasoning and test-time compute
  - AI safety as a field
  - concentration in fewer than ten labs
  - AI in professional software, at 40–46% of output among users of AI coding tools
  - compute export controls, *"arguably the most consequential governance surprise of the period"*
  - industrial-scale AI targeting

## How this source reads through the W&W lens

- `digital-sensing/digital-scouting`: the report is a scan of technological trends at a five-year interval, written to separate *"the lasting shifts from passing trends"* (p. 6). It names the trends an organisation should be screening for: reasoning models, agentic AI, open-weight models and compute geopolitics.
- `digital-sensing/digital-scenario-planning`: Five Years On is a worked example of interpreting future scenarios and auditing them afterwards. It gives a rule for weighting insiders' forecasts. Key Takeaway 12 and the conclusions leave the next five years open between continued scaling and a plateau.
- `contextual/external-triggers`: Key Takeaway 2 is a disruptive digital technology reaching fields that thought themselves immune, such as software, creative work and mathematics.
- `digital-seizing/balancing-digital-portfolios`: the choice Key Takeaway 5 puts to every country between proprietary U.S. models, open-weight Chinese models and sovereign capability is balancing internal and external options. It applies equally to a firm choosing a model supplier.

## Relations to other sources

- **The [[2026-04-30-ai-index-report-2026|AI Index 2026]]** is AI100's annual sibling at Stanford HAI: it was conceived inside AI100 and shares two authors with this report. AI100 cites its chapters on responsible AI, science and public opinion. The two differ in kind: the Index reports facts and makes no recommendations, while AI100 judges a five-year period. The [[2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report|Index's own HAI seminar]] is the counterpart of the AI100 seminar.
- **Cybersecurity:** [[2026-10-21-lewis-nadeau-mckinsey-strategy-room-frontier-ai-cybersecurity|McKinsey's frontier-AI cybersecurity episode]] describes the same shift from the defender's side: attacks compressed to hours, and security teams turning into "a diamond of overseers".
- **Mathematics:** [[2026-10-28-williams-harvard-first-proof-ai-math|First Proof]] is the graded counterpart of SQ2's announcements. It uses unpublished lemmas and scores proofs, citations and exposition separately, and finds that even the best systems fail on exposition.
- **US–China:** [[2026-09-18-bloomberg-originals-how-china-plans-to-win-global-ai-race|Bloomberg's documentary]] gives usage and cost data behind Deep Dive One's two-ecosystem conclusion. [[2026-10-04-chu-liu-dw-the-dip-how-china-is-viewing-the-ai-race|DW's The Dip]] shows the Chinese view.
- **Productivity:** [[2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity|Frey]] argues, as Key Takeaway 4 does, that AI does not yet show in productivity. [[2026-09-08-hatzius-gs-macro-impact-of-ai-gdp-productivity-jobs|Hatzius]] sets out the macro case.

## Debates and supersession

- **Macro impact, inside the report.** Key Takeaway 4 (p. 13) says AI's economic impact *"is not yet evident in aggregate macroeconomic data or in companies' returns on investment."* Five Years On (pp. 120, 124) says signs *"had begun to appear in macroeconomic data"*: U.S. productivity growth of about 2.7% in 2025, *"consistent with the early stages of a general-purpose-technology J-curve."* SQ3 cites Acemoglu's estimate of at most 0.5–0.7% TFP over a decade. The three readings are left unreconciled. Five Years On says it reads the 2021 report *"viewed from April 2026"*, so the two passages may simply reflect different drafting dates; the report does not say.
- **Canaries, 13% or 19%.** The wiki's [[2026-04-28-brynjolfsson-canaries-coal-mine|Canaries page]] carries the 2025 version's ~13% relative decline. AI100 cites the August 2026 revision's 19%. This is a newer measurement, not a conflict. The revision itself is not in the wiki.
- **Key Takeaway 12 has three wordings.** The overview says *"we should expect the next five years to surprise us just as much"* (p. 10). The full takeaway says *"This report will be out of date by the time you read it"* (p. 16). The seminar slide says *"the world will be very different in 5 years."*
- **What the panel does not resolve:** whether the scaling era is ending (*"It is not clear when the scaling era will end, or if it already is ending"*, p. 107), and AGI timing (lab heads say within five years; *"other equally qualified experts doubt this"*).

## Linked entities and concepts

- **Entities:** [[AI100]] (the study), [[Stanford HAI]] (administers it), [[AI Index]] (its annual sibling), [[Michael Wooldridge]] (Study Panel chair), [[Raymond Perrault]] and [[Toby Walsh]] (panel members, also AI Index authors), [[Erik Brynjolfsson]] (former Standing Committee member; his papers are cited throughout), [[NVIDIA]], [[Anthropic]] (Claude Mythos, Project Glasswing, the $1.5 billion settlement, the Pentagon dispute), [[OpenAI]] (ChatGPT, o1, the Millennium Prize claim, the sandbox escape), [[Google DeepMind]] (AlphaFold, AlphaProof, Co-Scientist), [[METR]] (task-horizon chart), [[Andrej Karpathy]] ("jaggedness", "vibe coding"), [[Claude Code]].
- **Concepts:** [[generative-ai]], [[foundation-models]], [[small-language-models]], [[open-source-ai]], [[ai-sovereignty]], [[jagged-frontier]], [[ai-benchmarks]], [[ai-agents]], [[vibe-coding]], [[ai-generated-code-quality]], [[ai-employment-effects]], [[automation-vs-augmentation]], [[ai-deskilling]], [[ai-washing]], [[reward-hacking]], [[attack-surface-management]], [[responsible-ai]], [[strategic-foresight]].
- **Dangling** (single-source mention, deferred): Study Panel members Peter Asaro, Lucie Flek, Iryna Gurevych, Sara Hooker, Gina Neff, Peter Norvig, Iyad Rahwan, Samantha Shorey and Luke Zettlemoyer. Also Sheila McIlraith (Standing Committee chair), Russ Altman (AI100 faculty director; also an author of the AI Index 2026), Christine Raval (project manager), Eric and Mary Horvitz (endowment), Claude Mythos, Project Glasswing, Leiden Declaration, OpenClaw, Epoch AI, Data Center Watch.

## Source quality

A consensus report by twelve academics and industry researchers, reviewed by a Standing Committee and four expert reviewers, with 262 footnotes. Most of them cite peer-reviewed work or primary sources, but several key 2026 events rest on press reports and are flagged as such in the text. Examples are the Mythos breach, the Maduro operation and the OpenAI sandbox escape; the Millennium Prize claim is marked *"unconfirmed at the time of writing."* Some figures appear without a footnote, among them the $6.7 trillion data-centre estimate, half of U.S. GDP growth, and the 50% AGI betting odds. The panel is mostly computer scientists, with a philosopher of technology (Asaro), communication and sociology scholars (Neff, Shorey) and a computational behavioural scientist (Rahwan). The panel has no economist, although David Autor sits on the Standing Committee. Its labour section leans on Stanford-affiliated work, and Stanford HAI administers the study. The text was finalised in September 2026 and so misses October events, such as Nvidia's later market cap, which the seminar updates. The PDF was read in full. pdftotext moved pull quotes into the body column, and the SQ1 photographs, the ARC example, the researcher table (p. 71) and the Eloundou exposure chart (p. 85) are lost. Their captions survive and are quoted where used.
