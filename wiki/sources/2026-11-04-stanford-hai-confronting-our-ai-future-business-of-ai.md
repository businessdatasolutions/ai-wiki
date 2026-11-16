---
type: source
kind: video
title: "Confronting Our AI Future: The Business of AI"
author: ["Stanford HAI"]
publisher: "Stanford HAI (YouTube channel), *Confronting Our AI Future: Hope, Fear, and the Choices Ahead* conference (Stanford campus, 28 October 2026); moderator Ina Fried (chief technology correspondent, Axios); panellists Andrew Bosworth (CTO, Meta), Erik Brynjolfsson (Stanford HAI senior fellow; director, Stanford Digital Economy Lab), Melissa Valentine (Stanford HAI senior fellow; professor of management science), Anahita Tafvizi (chief data and AI officer, Snowflake)"
url: "https://www.youtube.com/watch?v=-yJ9onp6zjk"
date_published: 2026-11-04
date_ingested: 2026-11-16
length: "~30:38 minutes (transcript ~243 lines; ASR auto-generated track, 10 chapters)"
raw: "../../raw/videos/confronting-our-ai-future-the-business-of-ai.md"
tags: [stanford-hai, confronting-our-ai-future, panel, ina-fried, axios, andrew-bosworth, meta, erik-brynjolfsson, melissa-valentine, anahita-tafvizi, snowflake, ai-and-organizations-lab, workhelix, enterprise-ai-layers, jagged-frontier, ai-native-engineering, in-house-coding-tool, closed-loop, coding-as-verifiable, human-inertia, productivity-statistics, power-law-adoption, task-taxonomy, canaries, entry-level-jobs, business-formation, amplifying-intention, automation-vs-augmentation, deterministic-answers, access-control, continuous-education, turing-trap]
dynamic_capabilities:
  - digital-seizing/strategic-agility
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-04-28-brynjolfsson-canaries-coal-mine
    via: "Brynjolfsson summarises the paper on the panel and names its co-authors: a noticeable drop in entry-level hiring in coding, customer service and other highly exposed occupations, and job loss associated with 'do this task for me' usage but not with 'teach me' usage. He gives no figures here; the paper reports a ~13% relative decline for ages 22–25. Same author, so not independent"
    confidence: 0.7
  - type: supports
    target: 2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity
    via: "the same speaker three months apart, with the same student's question ('is my generation doomed?'), the same 'amplifying intention' reframe and a power-law spread of AI benefit inside firms. The McKinsey interview gives the ADP figure (13%, then 16–17%); the panel adds Workhelix's 2–3% of employees 'crushing it' and a claim about new business formation"
    confidence: 0.7
  - type: supports
    target: 2026-10-21-stanford-del-transformation-tracker
    via: "both address whether AI shows in US productivity statistics: the Tracker (October 2026) rates output, TFP and labour-productivity growth neutral against pre-2020 history; on the panel Brynjolfsson, whose lab publishes it, says of the statistics that 'they've barely budged' and expects productivity growth to rise"
    confidence: 0.65
  - type: supports
    target: 2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering
    via: "both explain why AI improves fastest at coding: Karpathy says LLMs 'can easily automate what you can verify', trained in large reinforcement-learning environments; Bosworth says 'AI loves a closed loop' in which a prediction is tested immediately against ground truth, a property code has and most work does not"
    confidence: 0.7
  - type: supports
    target: 2026-07-22-brown-wef-meet-the-leader-entry-level-jobs-in-an-ai-era
    via: "both address what AI does to entry-level work: Brown reports employers asking for seven times more 'seniorized' skills and one firm hiring 25% more juniors; on the panel Valentine says no one has an answer to what happens when junior tasks go to AI, Brynjolfsson points to entrepreneurship and Tafvizi to an AI-native intern cohort"
    confidence: 0.6
---

# Stanford HAI, *Confronting Our AI Future* — The Business of AI

> This panel examines what AI is actually doing to organizations and jobs as it gets deployed at massive scale — from shipping it to billions of users, to measuring its real effect on productivity and employment, to redesigning how teams and workflows function day to day. Together, these vantage points push past abstract debates about the future of work toward the concrete tradeoffs organizations are making right now.
>
> *Confronting Our AI Future: Hope, Fear, and the Choices Ahead* is a Stanford HAI conference examining the anxiety that AI's rapid acceleration has raised for students, workers, and leaders, and the choices that will shape what comes next. It took place on October 28, 2026, on the Stanford campus.
>
> *— Channel description, Stanford HAI* (speaker list summarised in the frontmatter)

## TL;DR

A 30-minute panel from the [[Stanford HAI]] conference *Confronting Our AI Future* (28 October 2026). Ina Fried of Axios moderates Andrew Bosworth, Meta's CTO (at the company since 2006); [[Erik Brynjolfsson]], director of the [[Stanford Digital Economy Lab]]; Melissa Valentine, Stanford professor of management science; and Anahita Tafvizi, Snowflake's chief data and AI officer. **Auto-generated transcript, ASR-cleaned in quotation**: "Ena Frerieded" → Ina Fried, "Anita"/"Anito" → Anahita, "Eric" → Erik, "Bos"/"Biles" → Boz (Bosworth), "Beth Bachki" → Beth Bechky, "work helix" → Workhelix, "Barach and Ruy Chen" → Bharat and Ruyu Chen, "lingua frana" → lingua franca, "chat GPT" → ChatGPT.

What it adds to the wiki:

1. **Snowflake's four layers of enterprise AI**, from individual proficiency to transforming the organisation.
2. **A jagged frontier of companies**: Valentine sorts firms by the problem they face.
3. **Meta from the inside**: a 200-person team surpassing in eight months what 1,200 people built over four or five years, and an in-house coding tool writing most of Meta's code three weeks after launch.
4. **Why coding leads**: *"AI loves a closed loop."*
5. **Capability far ahead of use**: in a typical firm 2–3% of people get two to five times the productivity; the typical user gets 1–2% of the possible benefit.
6. **Entry-level work with no agreed answer**, and data tasks that got easier next to ones that got harder.

Two panellists describe their own companies (Meta, and Snowflake as its own "customer zero"), and Brynjolfsson cites data from Workhelix, a company he co-founded.

## Four layers, and where companies stall (1:28–6:51)

Tafvizi's four layers (2:41): **individual proficiencies**, tools to *"do the same job faster"*; **functional agents**, such as Snowflake's go-to-market assistant, which *"has answered more than two million questions in just a little bit over a year"*; **cross-functional workflows**, *"instead of all these handoffs between different functions… rethink your workflow with this AI native lens in mind"*; and **transforming the organisation**: *"If I were to build a data team today from scratch, how big does it need to be? Do I need a BI team?"* The last two layers are the panel's `digital-transforming/redesigning-internal-structures` content: workflows rebuilt without handoffs, and team size decided from scratch.

Valentine co-founded the AI and Organizations Lab with Bob Sutton and co-directs it with Beth Bechky; through it she talks to *"probably hundreds of companies"* and arranges them *"along the jagged frontier"* (4:26). At frontier labs building software agentically, the problem is speed: teams plan, build, and find themselves *"really misaligned."* At legacy enterprises *"the conversation is much more about integration and accuracy."* Where firms hand licences to frontline workers and tell them to reinvent their work, the training *"is like a little overfocused on prompting"* rather than on the interfaces the models sit in. [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua et al.]] coined the term for tasks; see [[jagged-frontier]] and [[enterprise-ai-adoption]].

## Meta: uneven, and replacing its own tools (6:51–13:44)

*"What we're doing today is unrecognizable one year ago."* Some Meta staff have *"completely gone native in a new style of development"*; others run *"very conventional business processes where you're just trying to get 5% faster."* His headline case: *"200 people have now surpassed the thing in 8 months that had taken 1,200 people four or five years to build."*

Meta builds tools on two tracks, for people with *"tremendously valuable skills but… not technical skill sets"* and *"power tools"* for *"the most cracked coders,"* and passes lessons from the second group to the first. That is `digital-transforming/improving-digital-maturity`: lifting the whole workforce with what its leading users learn. *"We launched a new coding tool three weeks ago. It is now the way the majority of code is written inside of our company."* It is Meta's own, and *"I'd be surprised if this coding tool was even in use 6 months from now. Like that's just the rate at which we're leaning into the disrupting of our own processes."* That is `digital-seizing/strategic-agility`: replacing what was adopted weeks earlier. See [[ai-coding-productivity-evidence]].

Asked about a reported programme that watched employees so AI could learn from them, Bosworth says it ("MCI" in the ASR) *"never actually ended up going anywhere."* A separate effort had engineers fix bugs for models to learn from; within *"a couple of weeks"* the models had absorbed it, then features, then whole products, and those engineers now build *"synthetic pipelines."* His explanation:

> *"Coding is a weird cheat code inside of AI learning… AI loves a closed loop. It loves the ability to have a hypothesis and then an ability to immediately test that hypothesis against ground truth. That's why data is the lingua franca of AI… Most things that we do don't have this property."* (11:27)

[[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy]] explains coding's lead by verifiability: LLMs *"can easily automate what you can verify."*

On people: *"humans have inertia… They want to have an idea of what their identity is,"* and there is *"a uneven inertia among human systems"*, in individuals, teams and the systems themselves. This is the panel's `contextual/internal-barriers` content: resistance rooted in identity and continuity, not in the tools.

## Capability far ahead of use (13:45–17:18)

Brynjolfsson calls Meta *"very unusual… I've never seen such a gap between the capabilities and what's actually on the ground."* Of the productivity statistics: *"they've barely budged,"* *"bouncing along lower than they were in the 90s and early 2000s."* His lab's [[2026-10-21-stanford-del-transformation-tracker|Transformation Tracker]] rates US output and productivity growth neutral in October 2026.

At Workhelix, *"there's usually two or 3% of the people… that are really crushing it. They may be getting two, three, five times the productivity… but the typical user is getting one or 2% of the… benefits they could be,"* writing *"slightly more eloquent emails."* See [[micro-productivity-trap]]. Electricity took about 30 years; this will be *"nowhere near that long,"* though longer than the Bay Area expects. The [[Stanford Digital Economy Lab]] has built a new task taxonomy (its name is garbled in the ASR) from interviews an AI conducts with workers, which shows new tasks in coding and little change for dishwashers.

## Entry-level work (17:18–23:28)

Valentine: *"I don't have an answer… nobody does."* The nearest she has seen is a David Brooks piece in *The Atlantic*: those who will be fine force themselves to keep learning critical thinking, *"and it's a discipline."*

Brynjolfsson retells a student's question, *"Is my generation doomed?"*, and answers from *"the canaries in the coal mine research"* with his co-authors Bharat Chandar and Ruyu Chen: *"a significant noticeably drop in hiring of entry-level workers in coding and customer service, other highly exposed occupations."* That is [[2026-04-28-brynjolfsson-canaries-coal-mine|the Canaries paper]], built on [[ADP]] payroll data. The good news, he says, is *"about twice the rate right now of new business formation in the United States as there was back in 2019."* In his August [[2026-08-01-brynjolfsson-mckinsey-talks-talent-biggest-ai-opportunity|McKinsey Talks Talent]] interview he said there are *"fewer startups overall in the United States."* Neither statement names its series; [[ai-employment-effects]] has other figures on the question. His advice is again to read AI as *"amplifying intention,"* and he restates the Canaries split in prompt terms: *"If the prompt was do this task for me that was associated with job loss. If the prompt was teach me how to do something new… that was not associated with that same kind of job loss."* See [[automation-vs-augmentation]].

Bosworth dates the falling cost of starting a business to before AI (Stripe, AWS, Snowflake, Facebook advertising) and calls AI *"a tutor."* [[2026-07-22-brown-wef-meet-the-leader-entry-level-jobs-in-an-ai-era|Brown (WEF and PwC)]] covers the entry-level question from employer surveys.

## Jobs that got easier, and harder (23:28–26:20)

At Snowflake a dashboard *"no longer requires a week… write a PRD, give it to the AI agent, it builds it for you within a couple minutes."* Other work is harder: dashboard sprawl that *"potentially can have the wrong number,"* and *"a probabilistic technology"* answering *"very deterministic workflows"*: *"what was my Q1 revenue? There's only one correct answer… You ask ChatGPT the same question twice, you get two different answers."* Natural-language access ends *"security by obscurity,"* so access control has to be explicit. Tafvizi tells hires to *"be ready to rewrite your own job description"* and names *"curiosity, lifetime learning and resilience"* as the key skills. See [[durable-skills]].

## Closing (26:20–30:38)

Bosworth expects those who keep their jobs to be happier in them; some displaced people will become entrepreneurs and others will not. *"We failed to retrain workforces after… industrialization hit… I think we need to avoid making the same mistake again,"* so less up-front education and *"a lot more on an ongoing basis."* Brynjolfsson is *"very worried that it's going to lead to a more concentration of that… but it's not an inevitability. It's very much a choice,"* and points to his paper *The Turing Trap*. Valentine: *"we currently accept a level of dysfunction from our organizations… What if our employees could solve problems on the spot?"*

## Linked entities and concepts

- **Entities:** [[Stanford HAI]] (channel and conference host), [[Erik Brynjolfsson]], [[Stanford Digital Economy Lab]], [[ADP]] (Canaries data).
- **Concepts:** [[enterprise-ai-adoption]], [[jagged-frontier]], [[ai-coding-productivity-evidence]], [[micro-productivity-trap]], [[ai-employment-effects]], [[automation-vs-augmentation]], [[durable-skills]].
- **Dangling** (single-source mention, deferred): Andrew Bosworth, Melissa Valentine, Anahita Tafvizi, Ina Fried, Axios, Meta (no entity page yet, though named in many sources), Snowflake (no entity page yet), Workhelix, Bob Sutton, Beth Bechky.

## Source quality

Auto-generated ASR transcript, cleaned in quotation only. A moderated panel with no slides, so nothing on screen is lost. Meta's and Snowflake's figures are self-reported by executives about their own firms. Brynjolfsson's 2–3% and 1–2% figures come from his own company, Workhelix, and are not published; he gives no numbers for the Canaries drop or for business formation. The task taxonomy's name and the "MCI" programme could not be confirmed from the ASR. Fried cut off Brynjolfsson's remedies from *The Turing Trap* for time.
