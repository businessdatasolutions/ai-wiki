---
type: source
kind: video
title: "HAI Seminar: Industry Conversation with Instacart"
author: ["Stanford HAI"]
publisher: "Stanford HAI (YouTube) — HAI Seminar recorded 23 September 2026; speakers Alexandr Lenk (Instacart Economics) and Arvind Karunakaran (Stanford MS&E)"
url: "https://www.youtube.com/watch?v=ZByKqo03krQ"
date_published: 2026-09-30
date_ingested: 2026-10-08
length: "~1:12:15 minutes (transcript ~695 segments; auto-generated captions, proper nouns corrected)"
raw: "../../raw/videos/hai-seminar-industry-conversation-with-instacart.md"
tags: [stanford-hai, hai-seminar, instacart, alexandr-lenk, arvind-karunakaran, ai-pioneers, peer-effects, social-diffusion, agentic-ai, cursor, staggered-difference-in-differences, experimentation, ticket-resolution, legal-profession, paralegals, job-enrichment, framing, task-first-reskilling, lump-of-task-fallacy, role-redesign, performance-evaluation, work-intensification, jobs-as-bundles, vacancy-chains, deskilling, junior-attorneys, radiation-oncology, coase, science-technology]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - contextual/internal-enablers
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over
    via: "Shared topic: AI adoption spreading through peers inside one firm. Krishna describes IBM's process owners following what 'their friends had done'; Lenk estimates the effect of a team's first heavy agentic-AI user on teammates' use."
  - type: supports
    target: 2025-06-01-autor-thompson-expertise
    via: "Shared topic: what happens to expertise when some of a job's tasks are automated. Autor & Thompson tie the outcome to which tasks are removed; Karunakaran describes paralegals taking up legal research and associates defending it, and cites newer Autor work on junior attorneys who lose foundational skill when AI is taken away."
  - type: supports
    target: 2026-08-11-ellmer-dhar-bcg-so-what-is-your-ai-rollout-built-to-fail
    via: "Shared topic: how employees hear an AI rollout. Ellmer & Dhar: people dislike being changed, and AI threatens identity. Karunakaran's paralegals heard a manager's 'productivity' message as substitution."
---

# Lenk & Karunakaran — Industry conversation with Instacart (Stanford HAI seminar, Sep 2026)

> What does AI adoption actually look like inside a firm — and what happens to the people working in it?
>
> This HAI seminar pairs two perspectives on that question. Alexandr Lenk of Instacart Economics will share findings on how AI adoption diffuses through peer networks inside firms and drives productivity gains, drawing on evidence from engineering and data-science teams. Arvind Karunakaran of Stanford MS&E will offer an organizational lens on what follows: how AI tools reshape roles, workflows, expert authority, and oversight relationships at work.
>
> Discussion will explore where these two pictures meet, where they diverge, and how to assess the enterprise value of AI.
>
> This video was recorded at Stanford University on September 23, 2026.
>
> — channel description, Stanford HAI (chapter list omitted)

## TL;DR

A 72-minute seminar on the **[[Stanford HAI]]** channel, recorded 23 September 2026 and published 30 September. Two talks of about 20 minutes each, then 24 minutes of questions:

- **Alexandr Lenk** (Instacart Economics; Stanford economics PhD) presents a working paper on how agentic-AI use spreads inside a firm through **"pioneers"**, a team's first heavy user, and what that does to output.
- **Arvind Karunakaran** (Stanford Management Science & Engineering, a former software engineer and product manager) presents field research on what happens to roles and expertise after adoption, centred on a Bay Area law firm.

The captions are auto-generated, with proper nouns corrected at acquire time. The two halves answer different questions and agree on one point: access to AI tools does not by itself produce use, and use does not by itself produce value.

### Lenk: pioneers and peer diffusion (0:57–20:56)

**The puzzle.** The engineering and data-science teams studied had free access to AI tools throughout 2025, yet use varied widely between people and over time. Regular agentic-AI use rose from about **3.5 days a month to about 10 days by January 2026**. Lenk says the first agentic coding tool came from [[Cursor]] in late November 2024, so 2025 is the period when agentic AI was new. Anecdotally, people learned about agentic tools *"almost randomly from people in their networks."* The company is called *"a major e-commerce tech company that we cannot disclose for legal purposes,"* although the event title and the host name Instacart; Lenk adds that the views are not Instacart's.

**Pioneers.** A pioneer is the first person on a team to cross a heavy-use threshold (roughly eight days of agentic-AI use in a two-week window). The slide: pioneers are *"initially sporadic agentic AI users (~2 days in a 2-week period)"*, the ramp-up is *"quite sudden (2 weeks)"*, and use then stays high. When a pioneer emerges, the median teammate is not using agentic AI at all. Pioneers do not differ much in seniority or tenure; what sets them apart is **AI enthusiasm**, measured as heavier earlier use of the firm's pre-agentic chatbot. They emerged at staggered times, and some teams had none, which the design exploits.

**Data and method.** Over 1,000 employees in about 200 teams (the ASR says *"2005 teams"*); an employee-month panel from June 2024 to December 2025 joining HR records, AI usage logs, the experimentation database and engineering tickets; a **staggered difference-in-differences** estimator.

**Results.**
- **Adoption.** After a pioneer emerges, teammates' use jumps by about **4.6 usage days**, with no pre-trend. Lenk attributes about **23% of the whole 2025 rise** in AI use to pioneers.
- **Experiments.** Teams with earlier pioneers create significantly more experiments; about **30% of experimental output** is attributed to agentic AI. The rate of successful launches rises in proportion, so the extra experiments are not waste.
- **Tickets.** The share of unresolved engineering tickets falls.

**Who responds, and which pioneers matter.**
- Individual contributors respond more than managers, and less-tenured staff more than long-tenured (the ASR garbles the tenure sentence; the outcome slides he describes point this way).
- A pioneer's **authority** matters (senior individual contributor or manager); a pioneer's tenure does not.
- For experiments, the effect comes **only from pioneers already skilled at experimentation**. For ticket resolution, a more routine task, any pioneer works. *"It is not just enough to have AI enthusiasts… teaching AI to others… the pioneer himself has to be skilled."*

His conclusion: with infrastructure and access in place, *"the next stage… is really about the social architecture… of AI transmission,"* and the right pioneer depends on the task.

### Karunakaran: acceleration, expansion, and role redesign (20:56–48:34)

**Two frames for value.** *Acceleration*: doing current tasks faster. *Expansion*: doing more complex tasks and creating new products. *"Only like a small part of value comes through acceleration alone."* His analogy is steel: not the same carriages in steel, but skyscrapers and bridges. The research covers law, manufacturing, advertising agencies and tech, with interviews, ethnography and lab and field experiments; the talk zooms in on one site.

**The site.** A Bay Area law firm (pseudonym *Legal Code*) that adopted a generative-AI drafting tool for paralegals in 2022, before ChatGPT. Two divisions with similar patent and IP caseloads, cultures and pay used it very differently. One also used it for legal research and case analysis, beyond the contracts and NDAs it was bought for.

**Division A: "you say productivity, I hear substitution."** The manager framed it as a productivity tool, in the vendor's language: *"Make your day-to-day work faster and more efficient."* The paralegals heard: *"if I'm more productive today and tomorrow, what's going to happen to us, a team of paralegals, the day after."* They thought the tool could do only about 20% of their work. They feared how management would deploy it, for example consolidating them into a shared service, more than they feared the tool itself. Low trust meant little experimentation, and they anchored on the hallucinations (*"three strikes and you're out"*): *"It takes me a lot more time to catch the mistakes… as opposed to me doing it myself."*

**Division B: job enrichment.** The manager asked two questions: *"what are the things you hate to do… Could you find a way to use [the tool] to do some or all of it?"* and *"What are the tasks you always wanted to do but never had the time or bandwidth to do?"* The second mattered more. The paralegals were just as sceptical at first (*"another fancy new IT tool that some tech bro successfully managed to sell to my managers"*), and the tool hallucinated just as much. But they repurposed it for legal research, which they found meaningful and which built skills some wanted for law school or a lateral move, so they kept experimenting.

**Management followed through.** The manager gave training and slack time. The firm replaced an AI-fluency programme with **task-first reskilling**: it identified the higher-order task (legal research), brought in legal-research experts, and taught AI as part of that task rather than teaching AI first.

**Consequences.**
- **Spillovers.** Admins and summer interns took on more complex work.
- **Pushback.** Junior associates objected: *"why are you as a paralegal without a law degree doing legal research… you stay in your lane."* Karunakaran calls this the **lump-of-task fallacy**, a zero-sum view of the tasks in a job. Managers then formally redesigned both roles: paralegals do the first cut of legal research, juniors verify it and move earlier into client work and legal strategy. *"You don't redesign one role or workflow at a time."*
- **Copying without metrics.** After two and a half to three years Division B was taking on more clients, and other divisions copied the role changes but kept the old evaluation criterion, **caseload**. Caseload fell as paralegals took on complex work, managers asked why, and motivation and use declined. In the Q&A he says the decline also shows in the quantitative data.

**Lessons.** Redesign several roles at once, rewrite job descriptions, align incentives and performance evaluation with the new tasks, and set up governance for the process. He adds that across industries AI is *intensifying* work rather than reducing it. His lab and field experiments find a **trade-off between productivity and meaning**: when AI is framed purely as a productivity tool, people's sense of meaning and motivation to reskill fall.

**Two caveats from others' research.**
1. **Interdependent tasks.** A Berkeley PhD student and physician (name unclear in the ASR) studied radiation oncologists whose peripheral tasks were handed to AI so they could focus on contouring, the core task. Speed and quality on the core task **declined**, because the peripheral and core tasks depend on each other.
2. **Juniors and foundational skill.** New work by David Autor and colleagues: on a patent-redlining task, AI raised junior attorneys' productivity more than seniors'. When the AI was taken away after about 90 days, juniors made many more mistakes, and seniors much less so. *"If AI makes execution cheaper… the importance is just about judgment and verification and taste… but where does judgment come from? Where does taste come from? Comes from execution."*

**A framework: jobs are more than bundles of tasks.** An *"invisible glue"* ties tasks together. Some bundles are strong (radiation oncologist) and some weak (medical transcriptionist); unbundling a strong one hurts performance. Task-level exposure frameworks miss this. Four things to weigh when redesigning a job:
1. **Bundle strength.**
2. **Handoff sequencing.** Waiting for the AI to finish the whole job is bad, and so is verifying every three steps, *"like having a speed breaker every 30 minutes in the highway."*
3. **Bottlenecks.** The weak link, and whether accountability should stay with a human.
4. **Vacancy chains.** If paralegals do legal research, what happens to the junior associate who did it before?

*"More AI usage does not translate to creating more value… value comes through carefully redesigning, reconfiguring workflows and roles."*

### Q&A (48:44–1:12:15)

- **Billable hours and hiring.** Law clients push back on why a case needs four associates and two paralegals, so the firm documented that both roles now do more complex work. Entry-level hiring is declining, but Karunakaran is unsure that is the equilibrium: juniors are cheaper to hire and train, and *"a lot of the cost is at the middle level."*
- **Peer effect or top-down push?** Lenk: senior pioneers are more effective because of *"personal trust"* in an authority figure, not because leadership directs attention to them. Karunakaran: a mid-level or senior pioneer gives credibility and an *"accountability buffer"*: if a senior colleague uses it, *"my job is not on the line."*
- **How AI differs from ERP.** ERP has features a vendor can teach. Generative and agentic AI is open-ended, so valuable uses have to be discovered bottom-up, and *"why would they experiment if they feel they're training their replacement?"*
- **Harvey and senior lawyers.** Firms adopting integrated platforms such as Harvey face the same organisational issues. Senior associates and partners resist changing their own roles.
- **Shared learning.** Division B's paralegals found the legal-research use independently, then converged on a Slack channel and a prompt library.
- **Why peer effects, if AI has obvious value?** An audience member argues peer effects are strongest under uncertainty. Lenk: there is still much uncertainty about using agentic AI well, and how it reaches answers is a black box. Karunakaran cites his colleague Michael Bernstein: generative AI is good at **rough-edged problems** with many right answers, which need social learning, and less at sharp-edged problems with one.
- **Where the bottleneck goes.** Lenk: engineers spend saved time choosing which ideas to pursue. Karunakaran: Geoff Hinton's prediction about radiologists did not come true, partly through the Jevons paradox and partly because the job includes physicians, residents, patients and signing off. He closes with Ronald Coase: just as transaction costs explain why firms exist, coordination costs explain why jobs exist, so unbundling has a price.

## Dynamic-capabilities reading

- **`digital-transforming/redesigning-internal-structures`.** Karunakaran's case is role redesign: paralegal and junior-associate roles rewritten together, evaluation criteria changed, and a governance process for it. His four-part framework (bundle strength, handoff sequencing, bottlenecks, vacancy chains) is a method for redesigning jobs.
- **`digital-transforming/improving-digital-maturity`.** Task-first reskilling replaced an AI-fluency programme: the firm taught legal research with AI inside it. Lenk's pioneers are a channel by which teams build the capability.
- **`contextual/internal-enablers`.** Pioneers with authority and task skill, a manager's job-enrichment framing, slack time, and a shared Slack channel and prompt library all made adoption spread.
- **`contextual/internal-barriers`.** Productivity framing heard as substitution, the lump-of-task fallacy among junior associates, and an unchanged caseload metric each held use back.

## Related in this wiki

- [[2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over|Krishna / IBM on Bain's Winning with AI (Sep 2026)]]: IBM's internal rollout described as a diffusion curve among process owners who followed *"what their friends had done."* Lenk's paper estimates a peer effect of that kind with a causal design.
- [[2025-06-01-autor-thompson-expertise|Autor & Thompson — Expertise (NBER, 2025)]]: a framework in which automation's effect on a job depends on which of its tasks are removed. Karunakaran's paralegal and junior-attorney examples, and the Autor study he cites, are about the same question.
- [[2026-08-11-ellmer-dhar-bcg-so-what-is-your-ai-rollout-built-to-fail|Ellmer & Dhar / BCG So What (Aug 2026)]]: *"People don't dislike change. They dislike being changed"*, and identity threat. Division A is a case of a rollout heard as a threat.
- [[2026-10-06-kropp-bcg-so-what-lessons-from-an-all-ai-company|Kropp / BCG So What (Oct 2026)]] estimates that under 10% of engineers in large firms use agentic coding tools effectively, and names four reasons.
- [[2026-10-07-richardson-reuters-econ-world-ai-at-work|Richardson / Reuters Econ World (Oct 2026)]] proposes counting tasks created and destroyed; Karunakaran argues that task-level frameworks miss the glue between tasks.

## Linked entities and concepts

- **Entities:** [[Stanford HAI]] (channel), [[Cursor]] (named as the first agentic coding tool and as how one engineer discovered agentic AI).
- **Concepts:** [[technology-adoption-theories]] (peer diffusion inside a firm), [[enterprise-ai-adoption]] (access without use; framing; task-first reskilling), [[automation-vs-augmentation]] (acceleration against expansion), [[ai-deskilling]] (judgment comes from execution; the radiation-oncology and junior-attorney caveats), [[ai-employment-effects]] (jobs as more than bundles of tasks; vacancy chains), [[micro-productivity-trap]] (more use without redesign does not create value), [[systems-thinking]] (redesigning several roles at once).
- **Dangling** (single-source mention, deferred): Alexandr Lenk, Arvind Karunakaran, Instacart, Michael Bernstein, Harvey (legal AI). Neither paper is ingested: Lenk's working paper is untitled in the talk; Karunakaran's HBR article and research paper are mentioned but not named.

## Debates and supersession

- **One firm, one task mix.** Lenk's evidence comes from one e-commerce firm's engineering and data-science teams. He says so in the Q&A: in a contract R&D firm, an audience member reports, juniors adopt first and persuade seniors. Karunakaran's four field sites also vary.
- **Experiments as a proxy for value.** The paper measures experiment counts, launches and ticket resolution, not revenue or customer outcomes. Lenk calls them proxies for upcoming business value.
- **Is the peer effect causal?** The staggered design and flat pre-trends support it. The question from the floor (whether senior pioneers stand in for top-down pressure) is answered with an interpretation, not a test.
- **Karunakaran does not claim causality** for the two-division comparison: *"these are like best explanations to the variation we observed."*
- **Task-level measurement.** His argument that jobs are more than bundles of tasks runs against the task-exposure approach behind much of [[ai-employment-effects]], and against [[2026-10-07-richardson-reuters-econ-world-ai-at-work|Richardson's]] proposal to count tasks rather than jobs.
- No supersession.

## What was actually ingested

The full auto-generated English track: 695 segments, 0:00–1:12:11 of 1:12:15, three creator chapters. Speakers are identified from introductions and handovers; Q&A questioners are unnamed except one. No stills: the recording is a room camera with the slides cropped at the top edge. Sample frames show partial slides (Lenk's literature slide cites Dell'Acqua et al. 2023 and Stein & Tamkin 2026 on complementarity between AI and human skill), so a full scan would have returned fragments.
