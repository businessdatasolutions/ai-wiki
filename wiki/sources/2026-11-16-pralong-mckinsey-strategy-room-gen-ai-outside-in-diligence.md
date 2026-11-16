---
type: source
kind: video
title: "Using Generative AI To Conduct Outside-In Diligence"
author: ["McKinsey & Company"]
publisher: "McKinsey & Company (YouTube channel), Inside the Strategy Room; host Sean Brown; David Pralong (senior partner, global leader of the transformation practice), William Bundy (partner, co-lead of private capital value creation), Chase Covington (partner, transformation and strategy and corporate finance practices), Laura Borton (consultant, transformation practice)"
url: "https://www.youtube.com/watch?v=tZA9Bi1m_rk"
date_published: 2026-11-16
date_ingested: 2026-11-16
length: "~49:28 minutes (transcript ~377 lines; ASR auto-generated track, 17 chapters)"
raw: "../../raw/videos/using-generative-ai-to-conduct-outside-in-diligence.md"
tags: [mckinsey, inside-the-strategy-room, sean-brown, david-pralong, william-bundy, chase-covington, laura-borton, generative-ai, due-diligence, outside-in-diligence, private-equity, value-creation-plan, bankable-plan, proprietary-data, data-room, confidential-information-memorandum, wave, citations, traceability, buy-vs-build, prompting, agentic-workflows, critic-agent, reviewer-role, change-management, staffing-model, pyramid-compression, trust, podcast]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/improving-digital-maturity
  - digital-transforming/redesigning-internal-structures
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-11-08-covington-slaney-mckinsey-strategy-room-agentic-transformation
    via: "two Inside the Strategy Room episodes eight days apart, both with Chase Covington: this one on gen AI in outside-in diligence, the other on agents in the transformation office; both name McKinsey's Wave platform and human review of agent output"
    confidence: 0.7
  - type: supports
    target: 2026-10-30-houssard-kordestani-liu-lundberg-mckinsey-ma-ai-value-creation
    via: "both describe AI in the deal process on the same show: Houssard et al. on diligence that reads all documents instead of a sample and on always-on sourcing; Pralong et al. on data-room synthesis, deal scanning for roll-ups and value-creation plans drawn from McKinsey's initiative database"
    confidence: 0.7
  - type: supports
    target: 2026-04-28-anand-wu-genai-playbook
    via: "both place due diligence where AI drafts and a human checks: Anand and Wu's quality-control zone, and Borton's 'reviewer role, not the doer role' with every number paired with a source"
    confidence: 0.65
  - type: supports
    target: 2025-11-05-mckinsey-state-of-ai-2025
    via: "both give McKinsey figures on breadth against depth of adoption: the 2025 survey reports 88% regular AI use and 7% fully scaled; Covington cites 88% that have launched an AI or digital transformation effort and under 10% operating at scale, without naming his survey"
    confidence: 0.6
  - type: supports
    target: 2025-07-01-mit-nanda-genai-divide-state-of-ai-in-business-2025
    via: "both address buying against building AI capability: NANDA reports external partnerships reaching deployment about 67% of the time against 33% for internal builds; Borton's rule is to buy for speed and build for differentiation"
    confidence: 0.55
---

# Pralong, Bundy, Covington & Borton (McKinsey, Inside the Strategy Room) — gen AI for outside-in diligence

> Generative AI is changing the economics of outside-in diligence, enabling investors to move faster, uncover overlooked opportunities, and sharpen their investment theses. But gaining an edge requires more than automating manual analysis. It demands a new approach to data, benchmarking, and human judgment.
>
> In this episode of Inside the Strategy Room, McKinsey senior partner David Pralong, partners William Bundy and Chase Covington, and consultant Laura Borton explore how gen AI is reshaping the diligence process. They discuss how organizations can harness proprietary data, develop more effective prompts, deploy specialized AI agents, and combine technology with experienced judgment to make more informed investment decisions.
>
> *— Channel description, McKinsey & Company*

## TL;DR

A 49-minute episode of *Inside the Strategy Room* on the [[McKinsey & Company]] channel, published 16 November 2026. Host [[Sean Brown]] talks with **David Pralong** (senior partner; global leader of the transformation practice; co-led the evolution of McKinsey's AI-enabled value-creation platform **Wave**), **William (Will) Bundy** (partner; co-lead of private capital value creation; author of *Creating Value in Portfolio Company Operations*), **[[Chase Covington]]** (partner; transformation and strategy and corporate finance practices) and **Laura Borton** (consultant, transformation practice). It accompanies the McKinsey article *From potential to performance: Using gen AI to conduct outside-in diligence*, which is not ingested.

**Auto-generated transcript, corrected in quotation only**: "Mckenzian company" / "McKenzie" → McKinsey & Company, "Sha Brown" → Sean Brown, "Chase Cington" → Chase Covington, "Genai" / "JAI" → gen AI, "outside induligence" → outside-in diligence, "SIM" → CIM (confidential information memorandum), "GAA strategy" → gen AI strategy, "anatomize" → anonymize, "chat GBT5" → ChatGPT-5. The transcript has no speaker labels; attribution follows the host's handovers.

What it adds to the wiki:

1. **A consultancy's diligence data turned into an AI product.** About 15 years of weekly initiative tracking; Bundy puts the stock at **1,600 transformations, 500,000 initiatives and 250,000 expert interviews**, and says a tool turns a downloaded data room into a value-creation plan *"in about 10 minutes."* Pralong claims an asset's financial trajectory can be predicted *"for about 36 months."*
2. **Adoption figures for investors.** Of 40 general partners across 200 investment teams, about half report some improvement, **6%** call the results transformational, and **95% or more** expect transformational impact within five years (Covington).
3. **A ratio for the non-technical cost:** *"of every $1 spent on technology, firms often need $5 for adoption and workforce readiness."*
4. **The staffing effect depends on the kind of organisation.** Lean private-equity teams get faster without a new staffing model; IT services and outsourcing see *"a much higher degree of compression of those pyramids."*
5. **Buy for speed, build for differentiation** (Borton), five prompting habits, and a multi-agent diligence workflow where preparing the data takes months and building the agents weeks.
6. **Trust among the senior people who decide** as the remaining gap (Pralong).

A consultancy's podcast about work it sells: McKinsey runs Wave and the diligence and transformation services described. The survey figures come without the survey's name, dates or method, and every client example is anonymised.

## From weekly tracking to a plan at the push of a button

McKinsey uses diligence *"as a way to underwrite our transformations,"* Pralong says, and it *"got into AI-assisted diligence almost … incidentally … some 15 years ago"* by tracking every initiative in its large value-creation plans (*"we call that bankable plan"*) every week. The result is *"millions of data points"* on each initiative's value, ramp-up speed, resource use and red flags. Gen AI made it possible to produce a bankable plan *"at the push of a button,"* and taught the firm *"the limitations of doing this."*

His most specific claim: with good data from past plans *"you could literally get now to a month-by-month P&L that reflects the improvements that you have identified at the diligence phase,"* with *"a distribution of outcomes around that"* because *"stuff happens in implementation."* He asks whether *"a very precise financial trajectory of the asset … with a good degree of predictability for about 36 months"* is fair; Covington says it is. No accuracy figure is given.

## What changed in the models (Bundy)

Bundy compares speeds: personal computers *"needed about 25 to 30 years from the late 1970s all the way to the early 2010s to hit ubiquity. When we think about AI, it has done that in literally about two years."* For diligence the change that mattered was **citation**. In 2023 he used chat models *"basically like an advanced Google search"* and kept them off diligence: *"I've had massive hallucinations… where it… literally just gave me a completely false narrative."* Now *"if you upload a confidential information memorandum it will… provide you all the initiatives, fact-check what the management team is telling you with data that we have,"* and cite the source. The gain is speed in ideation: it removes *"that first four to five days"* and gives *"a rough order of magnitude on that initiative within 5 minutes,"* but *"never… fully removes the analyst step."* The remaining limits are accuracy, bias and complex reasoning, partly engineered around with fact-checking or *"a red or a blue agent."*

## Adoption: broad, shallow, and cultural (Covington)

Covington's answer to what successful adopters do differently: *"it's cultural."* *"Most everybody's talking a very big game about AI, but if you ask people confidentially, pretty much everyone tells you they're struggling to implement AI."* His figures, from *"some survey and research work we've done"*:

| Claim | Figure |
| --- | --- |
| Organisations that have launched some AI or digital transformation effort | 88% |
| … of which feel there has been meaningful progress | under 25% |
| … of which operate at scale using AI | under 10% |
| Lacking a comprehensive gen AI strategy or clear success measures | 75% |
| Transformations that fail | 70% |
| Spend on adoption and workforce readiness per $1 of technology | $5 |

McKinsey's [[2025-11-05-mckinsey-state-of-ai-2025|State of AI 2025]] survey reports 88% of respondents using AI regularly and 7% of AI users fully scaled; Covington does not name the survey behind his figures.

Two failures: a client automated its analysts' first diligence steps at great cost, but *"when you forget the change management and just roll out the tool you don't get the adoption."* A medtech company's legal team and its clinical and medical affairs teams disagreed on what its agent should do; *"poor governance and a silo[ed] decision"* made the output *"unacceptable."* His conclusion: *"it's the cultural elements… more so than better models or better LLMs that enable the scale deployment of AI."* That is `contextual/internal-barriers` as change resistance and siloed governance. Pralong adds the professionals' side: people *"who've been doing this for a living for 25 years"* are, unless they built the tool, entitled to *"a degree of skepticism."*

For investors, Covington cites a survey of 40 general partners *"across 200 investment teams."* About half report gains in research speed, drafting investment-committee memos and synthesising data rooms. *"Only 6%"* call the results transformational, while *"95% plus"* expect it within five years. *"The problem isn't awareness, it's depth."* Firms use gen AI for *"basic efficiency"* on tasks *"they often have their most junior associates do,"* but *"haven't really embedded these [gen AI] tools into the thinking and critical processes of the investment process… and really the decision models."* That bears on the [[micro-productivity-trap]]. For skeptics: *"seeing is believing,"* an initial value-creation answer *"in two days versus two weeks,"* and *"start small, one agent here, one agent there."*

## Proprietary data as the edge

Covington: *"Anybody can get a LLM enterprise license and they're not very expensive … they're almost commoditizing."* The investors who stand out *"take that LLM and build into it proprietary data."* McKinsey's version: expert interviews recorded, logged and catalogued for its gen AI tools, and transformation work anonymised into a database. His example: an investment committee hears *"I think we can save 10% on indirect procurement"*; the AI-assisted version names five to eight categories for that business, capital cycle and seasonality, with *"the typical savings range and implementation cost and implementation time frame"* per lever, a granularity beyond *"four really smart analysts and they got an Excel file and a data room."*

Firms without a 15-year data store differ by age: the largest private-equity firms, *"around since the 80s,"* against a middle-market investor of five or ten years. McKinsey's codification is partly meant *"to level that playing field."* The untapped source is the portfolio itself: a middle-market consumer-retail investor compares same-store sales across its portfolio companies to form its own view of category trends. This is `digital-transforming/improving-digital-maturity` as leveraging knowledge already inside the firm, made readable by a model.

## Across the deal life cycle

Covington's examples. **The data room**: *"you got a data room on Friday afternoon. You then spend the next five, six days trying to digest everything… You generally understood two-thirds of it."* With gen AI a team can *"query the data room"* for trends in gross margin, market share or profit pools *"in a matter of minutes."* **Deal scanning for a roll-up**: *"we can buy for eight times, we trade at 10 times, post-synergies acquisitions are six times,"* and AI drafts *"a list of 500, a list of 200, a list of 100 companies"* with location, estimated revenue, owner and CEO. Bundy adds the investment committee: have an agent challenge the IC memo as an IC would, to *"shadow box"* beforehand.

The same show's October M&A episode, [[2026-10-30-houssard-kordestani-liu-lundberg-mckinsey-ma-ai-value-creation|Houssard, Kordestani, Liu and Lundberg]], also covers AI in sourcing, diligence and integration; there Houssard says diligence that once sampled about 15% of documents now reads all of them.

## Who reorganises, and who does not

Asked whether firms now hire fewer junior analysts, Covington splits by organisation type. A private-equity firm is lean, *"not a dramatic pyramid,"* with judgment-heavy work and low spans of control; the tools make people *"more effective and faster but not necessarily changing the staffing model."* In tech services and IT outsourcing, with higher spans of control and work *"more repetitive and rule-based,"* McKinsey sees *"a much higher degree of compression of those pyramids."* For investors, *"going from five analysts to four analysts on your investor team; that's irrelevant."* Returns come from a slightly better call on *"what price you pay or which deal you pass on,"* decisions worth *"hundreds of millions of dollars."* (Bundy's follow-up, *"the only other thing I'd add there, Chase,"* confirms the speaker.) This is the `digital-transforming/redesigning-internal-structures` question asked of two kinds of firm, with two answers. See [[automation-vs-augmentation]].

## Buy for speed, build for differentiation

Borton: *"you really want to buy for speed and build for differentiation."* Converting data into *"a usable format for AI"* is *"largely an outsourcable thing for most firms."* What to build is the firm's own lens: *"custom kind of light layers that you overlay on existing solutions like open models."* Bundy adds the portfolio-company rule (outsource what is not core, as McKinsey would not build its own travel booking) and concedes the build side's cost: McKinsey's data set *"takes 40 years"* to assemble. This is `digital-seizing/balancing-digital-portfolios` as balancing internal and external options. [[2025-07-01-mit-nanda-genai-divide-state-of-ai-in-business-2025|MIT NANDA]] reports external partnerships reaching deployment about 67% of the time, against about 33% for internally built tools.

Bundy's build: download a data room, apply McKinsey's accumulated expertise, and get a value-creation plan *"in about 10 minutes"* covering *"the five to six major levers, initiatives, relative sizing, typical timeline to achieve, and actual cash flow impact."*

## Five prompting habits

Borton starts from *"garbage in and garbage out"* and *"over-expectations of what [gen AI] can do without explicit instructions"*:

1. **Define role and success.** Treat the model *"like a smart, bright … junior analyst who's great at execution, but only if you're clear about the role, goal, and context."*
2. **Prioritise your sources**, because to the model *"all of it is the same"*: name the 10-K or the investor-day deck.
3. **Standardise the output** with examples of *"what great looks like."*
4. **Pair every number with proof**: confidence intervals, rationale and sources, so you *"take the reviewer role, not the doer role."*
5. **Enable clarifying questions.** Models are *"penalized in their training for not having an answer"*; she cites [[OpenAI]]'s deep research, which asks before it starts.

*"Good prompting is really disciplined thinking in text form."* [[2026-04-28-anand-wu-genai-playbook|Anand and Wu]] place *"conducting due diligence of records"* in their quality-control zone, where AI produces and a human verifies; habit four is addressed to the person doing the checking.

## Building an agentic diligence workflow

Borton splits the build into system design (*"the compilation of prompts and decision trees"*) and data. Clients underrate the second: *"just transforming things that are in SharePoint to a usable … data set by an AI system could take months,"* while turning what a team does into an agentic flow takes skilled people *"a matter of a few weeks."* Change management comes first: domain experts on the corpus, feedback loops and usage KPIs, *"just as important if not more so sometimes than the tech build."*

In McKinsey's workflow the agents *"self-organize"*, split the request into subtasks and *"converse with each other,"* with roles such as *"an engineer who's going to pull down the financials"* and *"a critic that is going to help pressure test some findings."* The output is a value-creation memo with levers and expected EBIT impact. After each output the user says *"is that a good response yes or no and why,"* because *"this is really all v1."* For funds with a limited stack she recommends no-code tools and a small prompting team, starting with diligence because *"there's already a playbook."* The [[2026-09-01-cfa-institute-agentic-ai-finance-workflows-governance|CFA Institute's]] episode covers analyst workflows from the investment profession's side, with skill files and evaluations as its route to trust. See [[ai-agents]].

## Oversight, and where judgment stays

Borton: analysts move to *"the reviewer mindset… trust but verify,"* with procedures for when humans step in, and security, legal and compliance staff in the design phase because *"we have sensitive deal data that's non-public information."* Bundy: *"you can't rely on [gen AI] to make decisions,"* the output *"doesn't capture value on its own,"* and getting a portfolio company's management to act on a memo *"is going to be the harder step."*

Pralong closes on judgment: the tools *"are merely instruments of sharpening your judgment,"* none leads to *"an automatic decision,"* and *"the most profound gap still is the trust in those systems."* Inside McKinsey too, the full benefit comes only *"once the senior firm members, those who will eventually exercise the judgment… have actually had their hands on tools enough to trust these tools."* See [[agent-oversight-and-delegation]].

Eight days earlier, Covington appeared on the same show with [[2026-11-08-covington-slaney-mckinsey-strategy-room-agentic-transformation|Tomer Slaney on the agentic transformation office]]: agents inside the office that runs a transformation, with Wave as the data platform there too.

## Linked entities and concepts

- **Entities:** [[McKinsey & Company]] (channel; all speakers), [[Sean Brown]] (host), [[Chase Covington]] (guest; also on [[2026-11-08-covington-slaney-mckinsey-strategy-room-agentic-transformation|the transformation-office episode]]), [[OpenAI]] (deep research and ChatGPT-5 as examples).
- **Concepts:** [[enterprise-ai-adoption]], [[micro-productivity-trap]], [[automation-vs-augmentation]], [[agent-oversight-and-delegation]], [[ai-agents]], [[dynamic-capabilities]].
- **Neighbour sources:** [[2026-10-30-houssard-kordestani-liu-lundberg-mckinsey-ma-ai-value-creation]], [[2025-11-05-mckinsey-state-of-ai-2025]], [[2026-04-28-anand-wu-genai-playbook]], [[2025-07-01-mit-nanda-genai-divide-state-of-ai-in-business-2025]], [[2026-09-01-cfa-institute-agentic-ai-finance-workflows-governance]].
- **Dangling** (single-source mention, deferred): David Pralong, William Bundy, Laura Borton, Wave (McKinsey's value-creation and transformation platform; also named in the transformation-office episode).

## Source quality

Auto-generated ASR transcript, corrected in quotation only; speakers are identified from the host's handovers. Consultants discussing their own platform and services, with no outside voice. Every figure (88/25/10, 75%, 70%, $1:$5, the 40-GP survey) is a verbal citation of unnamed McKinsey research without dates, sample or method. The 36-month predictability, the 10-minute plan and the 1,600/500,000/250,000 data stock are self-reported. Pralong dates the tracking to about 15 years ago and Bundy says the data set *"takes 40 years"*; the second may refer to the firm's wider history. Useful for its concrete description of an AI-assisted diligence workflow and for the staffing distinction by organisation type.
