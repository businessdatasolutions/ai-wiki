---
type: source
kind: video
title: "The era of experimentation is over, with Arvind Krishna, CEO of IBM"
author: ["Bain & Company"]
publisher: "Bain & Company (YouTube channel), *Winning with AI* podcast; hosts Sarah Elk (Bain) and Andrew Ng; guest Arvind Krishna, chairman and CEO of IBM"
url: "https://www.youtube.com/watch?v=bixk9UegzoI"
date_published: 2026-09-15
date_ingested: 2026-09-21
length: "~29:45 minutes (transcript ~1125 lines; auto-generated ASR, 747 segments across the channel's 11 chapters)"
raw: "../../raw/videos/the-era-of-experimentation-is-over-with-arvind-krishna-ceo-of-ibm.md"
tags: [bain, winning-with-ai, ibm, arvind-krishna, sarah-elk, andrew-ng, watson, experimentation-to-scale, focus, portfolio-concentration, monolith-vs-building-blocks, multi-llm, open-weight-models, on-premise, enterprise-operations, back-office, quote-to-cash, hr-automation, employee-verification-letter, process-portfolio, mainframe, quantum, ceo-curiosity, conviction, podcast]
dynamic_capabilities:
  - digital-seizing/balancing-digital-portfolios
  - digital-seizing/strategic-agility
  - digital-transforming/redesigning-internal-structures
  - strategic-renewal/business-model
relationships:
  - type: supports
    target: 2026-05-02-dutt-chatterji-ai-experimentation-to-transformation
    via: "same prescription from the client side and the consultant side: Dutt et al.'s first step is to narrow to 4–5 critical domains, Krishna's is 'pick three, four, five things which you can scale like crazy' instead of 100 experiments. Krishna adds the arithmetic — $200M spread over 100 experiments is 3–5 people each — and IBM's own process portfolio as the worked case"
    confidence: 0.85
  - type: supports
    target: 2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company
    via: "both take the stalled pilot as the central fact of enterprise AI in 2026. BBC measures the ~30% pilot-to-production ratio and puts the cause in chained workflows; Krishna puts it in dispersion — too many experiments, each too small to be scaled — and names the end-to-end process as the unit to aim at"
    confidence: 0.7
  - type: supports
    target: 2026-07-10-hugging-face-ceo-companies-done-renting-their-ai
    via: "Delangue's many-specialised-models reality and own-vs-rent flow is Krishna's 'and world': enterprises will use several LLMs plus open-weight models, and he urges running open weights on premise to keep proprietary IP in-house and to answer geopolitical data concerns"
    confidence: 0.75
  - type: supports
    target: 2026-07-29-ng-washington-post-china-open-source-ai-competitiveness
    via: "Krishna's first piece of CEO advice — pay attention to open-weight models, run on premise — is the enterprise-side version of the case Ng makes on policy grounds. Ng co-hosts this episode, so the two are not independent"
    confidence: 0.6
  - type: supports
    target: 2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services
    via: "both locate the large agentic opportunity in the back office, run end to end across functional silos. Krishna's quote-to-cash example — a dozen systems, handed between sales, distribution, finance and legal — is the workflow Heimes and Peters want shared services to own"
    confidence: 0.7
  - type: supports
    target: 2026-06-17-ng-langchain-interrupt-future-of-ai-agents
    via: "Ng's enterprise observation at Interrupt — bottom-up 'let a thousand flowers bloom' experimentation is not paying off, top-down workflow redesign is — is Krishna's '100 experiments' critique. Ng co-hosts this episode, so the agreement is not independent"
    confidence: 0.65
---

# Krishna (IBM) on Bain's *Winning with AI* — The era of experimentation is over

> In 2011, IBM's Watson won Jeopardy, changing the conversation about AI forever. The 15 years since have brought meaningful advances, though the path to broad impact has proved more complex than many expected. CEO Arvind Krishna joins Sarah and Andrew to discuss what the company has learned along the way—and how those lessons are shaping the IBM playbook.
>
> Arvind explains why the era of AI experimentation is over and why leaders should focus investment on a small number of high-impact areas rather than spread resources across dozens of experiments. He shares how IBM has put that approach to work in areas like HR and enterprise operations. And he makes some provocative predictions about the future of quantum and AI working together, promising that quantum advances are coming much sooner than many might expect.
>
> *— Channel description, Bain & Company*

## TL;DR

A 30-minute episode of [[Bain & Company]]'s *Winning with AI* podcast, co-hosted by Bain's Americas AI practice leader Sarah Elk and [[Andrew Ng]]. The guest is Arvind Krishna, chairman and CEO of IBM. **Auto-generated transcript, ASR-cleaned in quotation**: names and terms are corrected in the quotes below ("Arvin" → Arvind, "Bane" → Bain, "Andrew Ing" → Andrew Ng, "cobalt" → COBOL, "code to cache" → quote-to-cash, "peace pots" → piece parts, "hardnesses" → harnesses).

What it adds to the wiki:

1. **Concentration as the prescription, with numbers.** *"Please don't do a 100 experiments. Pick three, four, five things which you can scale like crazy."* A $200M annual budget spread across 100 experiments gives 3–5 people and about $2M each and no plan to scale; the alternative is 100 people and $15–20M on one. *"It is shocking to me that most people are in the first bucket, not the second."*
2. **A CEO's account of IBM's own AI failure.** Watson won *Jeopardy!* in 2011. IBM then made two mistakes: it built **monolithic vertical applications** when the first years of a technology call for *"piece parts that let people gain trust"*; and it chose **health**, where it knew neither the customer (doctors), the regulator, nor had medical staff. *"You should always try to at least get only one of those areas wrong."*
3. **IBM's internal portfolio, as a worked case.** About 200 enterprise processes at roughly $100M each. Owners volunteer; five first, then ten; about 60 done in two and a half years; the next 70 "raring to go"; 30–40 recalcitrant.
4. **The employee-verification letter**: 17 human touchpoints and ~30 minutes of work, replaced by an agent that takes 15 seconds of the employee's time.
5. **Enterprise operations as the next proven area**, after customer service and coding: agents working across the silos of an end-to-end process such as quote-to-cash.
6. **An "and world" for models**: several LLMs, plus open-weight models run on premise.

It is also a vendor CEO talking on a consultancy's podcast. IBM sells the platforms (hybrid cloud, watsonx, mainframe, quantum) that the advice points toward. The claims about IBM's internal results are self-reported and unaudited.

## The shift from experimentation to scale

Krishna's opening claim is that the experimentation era, which every new technology goes through *"because they don't fully trust it"*, *"has passed for AI."* He limits it straight away: *"perhaps the mistake some people make is that it's going to be incredibly productive in every single area. That's probably not quite true."* Customer service, customer experience and coding are *"proven out"*. His bet for the next one is **enterprise operations** — *"the back office, or how an enterprise functions."*

Elk cites Bain's 2026 CEO survey: **80% of CEOs are doing something with AI but not seeing the return they expect**. Krishna's explanation is dispersion. His arithmetic is the most quotable part of the episode:

> *"Let's say a reasonable enterprise is willing to spend a couple of hundred million dollars a year… If you now spread it across a 100 experiments, you probably have three to five people in each experiment. You got a couple of million dollars of total spend. And then you don't have the ability on how to scale it because you've not thought through all of it. If you instead put a hundred people on one of those things and you put 15 or 20 million of spend and you thought about scaling it, which one is going to be more successful?"*

This is the first step of [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Dutt et al.'s Bain/OpenAI framework]] — narrow to 4–5 critical domains — stated from the client side, with a budget attached. It reads as a direct account of the [[micro-productivity-trap]]: many small gains, none large enough to redesign anything. It also gives a cause for the stalled pilots [[2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company|BBC AI Decoded]] measures at a ~30% pilot-to-production ratio. For Krishna the pilots are too small and too many to have been designed for scale in the first place. His co-host made the same point at [[2026-06-17-ng-langchain-interrupt-future-of-ai-agents|LangChain Interrupt]] three months earlier: bottom-up *"thousand flowers"* experimentation is not paying off, and top-down workflow redesign is.

This is `digital-seizing/balancing-digital-portfolios` at its plainest: fewer bets, each funded to scale. He does not say how to choose them except by judgment, and that is where Elk ends the episode (below).

## What IBM got wrong with Watson

Ng asks for the insider view of IBM's flat decade after *Jeopardy!* Krishna's answer is unusually direct for a sitting CEO:

- **Mistake one: monoliths.** *"We took the approach that if we construct monolithic vertical applications in certain use cases then you can derive a lot of value… That has never been the first four to five years of any new technology. We should have decomposed it and come out with piece parts that let people gain trust, gain knowledge, get their own expertise."*
- **Mistake two: the wrong vertical.** Health, where IBM dealt with payers and insurers but *"not much with doctors… we didn't know the actual client. Second, we didn't know the regulator. And three, we don't have a lot of medical staff inside IBM."*

He also says the LLM era is different in kind: *"much more… brute force compute than it is about throwing hundreds of really smart people at a problem."*

The lesson he draws is the platform one: IBM now describes itself as **four platforms** — mainframe, hybrid cloud (Red Hat / OpenShift), AI, and quantum (*"a couple of years away from mainstream"*). This is `strategic-renewal/business-model`: a company redefining what it sells after a failed product strategy. Ng calls the building-blocks approach *"a very engineering way of thinking about it"*; it is the same framing Ng uses elsewhere in the corpus (see [[Andrew Ng]]).

## Many models, open weights, and the mainframe

*"People get into this debate of which LLM and I kind of say it's going to be an **and world**."* Enterprises will use several LLMs *"for various reasons — could be technical, could be political, could be diversity"*, plus open-weight models, a belief he has held for five years that has *"come true in the last 9 to 10 months."* Around them they need guardrails, cost optimisation, audit trails, evals and harnesses. This matches [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|Delangue's]] account of companies running many specialised models, and bears on [[foundation-models]] and [[open-source-ai]].

On hallucination he takes a stance the corpus rarely states this plainly: *"any statistical technique is always going to be somewhat imprecise. But if we can get it into the 95, 96% accuracy, we're probably beating humans. I think we just have this innate desire that machines have to be perfect and humans can be imperfect."*

Ng asks about his reported claim that only 2% of IBM could be automated. Krishna separates two statements the media merged. **2% of IBM's software revenue** is in products — interaction-style ones — that AI could easily replace; products built on deep data or transactions are not. And he agrees with [[Anthropic]] that LLMs are good at translating COBOL and similar code, but denies this threatens the mainframe: *"People don't use the mainframe because of language lock-ins."* Card authorisation at 15–20 billion transactions an hour would cost too much in tokens; the mainframe is *"probably a hundred times more cost effective."*

## Enterprise operations, across the silos

Elk raises the data and ontology work agents need and asks whether companies must rebuild the software-development capability they let wither. Krishna answers with a process:

> *"Let's take quote-to-cash. Somebody's prospecting a customer. Somebody's getting a price. Somebody is entering that order. You got to make sure that there is inventory… distribution… that you can invoice to go collect it… This is probably touching a half-dozen or a dozen different systems. Today, how do we do it? We organize the company into silos… And there's a lot of human touch-offs and handoffs. And that's what you could call friction or cost inside an enterprise. Well, agents can go deal with all these systems."*

That raises, in his words, *"how do you organize and how do you make sure your data is clean enough?"* — `digital-transforming/redesigning-internal-structures`. It is the same claim [[2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services|Heimes and Peters]] make for shared services: the value sits in the handoffs between functions, not in any one of them.

Elk adds that organisational silos reappear as technical ones: business units build agentic components separately that could have been shared. Krishna agrees and gives IBM's HR example.

## The 17-touchpoint letter

IBM began in early 2023 by putting an agent in front of HR systems. The example is the **employee verification letter** for a mortgage: the employee asked their manager, who asked the HR partner, who asked an HR back office that *"knew nothing about the employee"* and looked up three or four systems. *"We counted up, it was 17 different human touch points, probably maybe an hour of work in total."* Now: the network already knows who you are; you ask the agent for an EVL; it asks which address to send it to. *"What used to be 30 minutes of human work is now you spending 15 seconds."* (He gives both an hour and 30 minutes for the old process.)

It is a clean case of [[automation-vs-augmentation|automation]] of a coordination chain rather than of a task. No person in the old chain does anything in the new one.

## How IBM chose where to scale

The most reusable passage for anyone designing an adoption portfolio:

> *"If I think about running the enterprise, there's about 200 processes… if it's too small, like you're only spending a couple of million, it's too small to get a benefit. If it's too large, like you're spending a billion, that's too big. So let's call them about $100 million per area… you can't do them all. So you kind of see who raises their hand as the owner… We made progress on five. HR was actually one of the first ones. Then… it became 10. Over the first two and a half years, we got about 60 of them done… The next 70 kind of were now raring to go because they saw what their friends had done. The last 30 or 40 are probably a little recalcitrant."*

For the last group he offers three explanations without choosing: the human doesn't trust the AI, the AI isn't ready, or the process is more complicated. Two things stand out. Selection is by **volunteering owners**, not top-down assignment, so the first wave is also the most willing. And adoption spreads by example — the second wave moves *"because they saw what their friends had done."* That is the diffusion pattern [[technology-adoption-theories]] describes, observed inside one firm.

There is a tension with his opening advice. Sixty processes in two and a half years is not "three, four, five things". The two fit if the concentration is per unit of budget (each process a ~$100M area with an owner and a team), not in the total number. He does not reconcile them.

## Curiosity, conviction, and accountability

Asked whether CEOs need a technical background, he says no: *"curiosity and being willing to ask really naive and dumb questions is probably far more important."* What helps is a habit of decomposition — *"what is the smallest size you can tackle that makes progress but it's not so big that it's kind of like trying to eat a whale"* — plus a willingness to be wrong on the first attempts, and **conviction**: *"put both feet in the boat."* He adds *"accountability, not just ownership."*

## Quantum by 2029

About a third of the episode is on quantum, less central to this wiki. Krishna predicts that **in 2029 quantum will do something that surprises us**, comparing it to ChatGPT's release in November 2022. He cites Cleveland Clinic modelling a 12,000-atom protein fragment (the protein's name is garbled in the ASR) and work on plasma flow and magnetism as signs. He names four problem classes where quantum should beat classical computing: **Hamiltonians** (computational chemistry, materials — he sizes the physical-materials world at ~10% of world GDP), **partial differential equations** (Black–Scholes, Navier–Stokes), **constrained optimisation**, and, later and on larger machines, **finding hidden patterns in data** (*"more a category in the middle of the 2030s"*).

He and Ng agree that neither quantum nor AI will solve every problem. Krishna on AGI: *"Why do we expect techniques and technologies that are looking at past data are going to suddenly go way beyond?"* — *"very useful, but they're not silver bullets."*

## Three pieces of advice, and Elk on pivoting

Krishna closes with three points:

1. **Open-weight models, run on premise** — to keep critical proprietary IP from being *"taken away"*, and because *"people outside the US may worry a lot about where their queries and data is going."* A cost advantage on top. See [[open-source-ai]] and [[ai-sovereignty]]. This is the enterprise-side version of the case [[2026-07-29-ng-washington-post-china-open-source-ai-competitiveness|Ng makes on policy grounds]]; Ng is co-host here, so the two are not independent voices.
2. **Unlock internal data for AI**, with governance.
3. **Conviction** — *"the art of the leader to figure out the two or three areas where AI could be a huge unlock and put enough resource and enough investment behind those."*

Elk, co-author of Bain's *Doing Agile Right*, adds the counterweight: choosing two or three areas *"takes judgment and… you could be wrong, whereas if you choose a 100 things you know you're less likely to be wrong."* So the bets have to be de-risked by testing and pivoting, which she says few companies do in practice: *"leaders find it hard to acknowledge that they're wrong."* Her line: *"acknowledging a mistake in 6 months is far better than going 3 years and getting a mediocre result."* This is the `digital-seizing/strategic-agility` side of the episode: concentration only works if the organisation will change course. Her claim that *"100% of the market value is driven by 20% of the companies"* because they pivot is asserted, not sourced.

## Linked entities and concepts

- **Entities:** [[Bain & Company]] (channel; Elk's firm), [[Andrew Ng]] (co-host), [[Anthropic]] (COBOL translation claim).
- **Concepts:** [[enterprise-ai-adoption]], [[micro-productivity-trap]], [[open-source-ai]], [[ai-sovereignty]], [[foundation-models]], [[automation-vs-augmentation]], [[dynamic-capabilities]], [[technology-adoption-theories]].
- **Dangling** (single-source mention, deferred): Arvind Krishna, Sarah Elk, IBM (mentioned incidentally in three earlier sources, never as a subject), Cleveland Clinic.

## Source quality

Auto-generated ASR transcript, cleaned in quotation only. A vendor CEO on a consultancy's podcast; both firms sell the transformation the episode recommends. IBM's internal figures (200 processes, ~60 done, 17 touchpoints) are self-reported. The Bain CEO-survey figure (80%) is cited, not shown. Useful as an operator's account with unusually concrete numbers, and as a rare CEO admission of a named strategic error.
