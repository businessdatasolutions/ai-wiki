---
type: source
kind: video
title: "Building And Structuring An AI Native Company"
author: ["Y Combinator"]
publisher: "Y Combinator (YC Root Access channel) — recorded at Startup School Paris; speaker Tom Blomfield (General Partner)"
url: "https://www.youtube.com/watch?v=Z3JyAqh4ixg"
date_published: 2026-08-14
date_ingested: 2026-08-20
length: "~21:20 minutes (transcript ~570 segments; auto-generated captions, ASR-cleaned)"
raw: "../../raw/videos/building-and-structuring-an-ai-native-company.md"
tags: [tom-blomfield, y-combinator, startup-school-paris, ai-native-company, self-improving-loops, company-brain, roman-legions, org-chart, humans-as-bottleneck, middle-management, dri, burn-tokens-not-headcount, legibility, quality-gates, adversarial-llm, meta-agent, posthog, jack-dorsey, karpathy, investor-call-simulation, openclaw, agent-vm]
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
  - digital-transforming/improving-digital-maturity
  - strategic-renewal/collaborative-approach
  - contextual/internal-barriers
relationships:
  - type: supports
    target: 2026-05-19-garg-yc-internal-ai-agent-evolves-itself
    via: "the general claim and its worked instance, from the same accelerator three months apart. Garg (May 2026) describes one company's self-extending ops agent — Claude Code wrapped in Python, 45+ self-authored CLIs, an agent-editable instructions.md, three memory types. Blomfield generalises the pattern into a company-design principle and supplies YC's own instance: a second agent that runs overnight over the day's queries against the internal data agent, classifies them as success or failure, and *\"goes and puts in pull requests to fix all of the problems from the day before, and so if you go back as a human on the second day and run the same query as yesterday, it now works.\"* Garg is the mechanism; Blomfield is the organising theory plus a second data point"
    confidence: 0.8
  - type: supports
    target: 2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up
    via: "same accelerator, same thesis, four months apart, with Blomfield the later and more structural statement. Hu argues for building the company AI-first from day one; Blomfield supplies the argument for WHY the default is wrong — the hierarchical org chart exists because humans were the information-routing mechanism, an inheritance he traces to the Roman legions, and *\"AI breaks that apart… you don't have to have humans as a coordinating mechanism any longer.\"* He also converts the thesis into practice-level advice (burn tokens not headcount, no middle management, ban Slack DMs, every action must create an artifact)"
    confidence: 0.75
  - type: supports
    target: 2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer
    via: "both argue the AI-native company is defined by a structural property rather than a productivity multiple, and both are YC voices. Tan and Hu develop the 1000x-engineer framing; Blomfield explicitly rejects the multiplier framing as the interesting part — *\"previously AI is like make each person 20% more productive or 30% more productive. What happens if we reimagine the company as a series of AI loops?\"* — and relocates the claim from individual capability to loop closure. The pair is useful because it shows the same institution moving from a per-person to a per-loop unit of analysis"
    confidence: 0.7
  - type: supports
    target: 2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm
    via: "two accounts of the firm's boundary changing under AI, from a startup-accelerator and a hyperscaler-CEO vantage. Both converge on the claim that management layers exist to route information and that this rationale weakens; Blomfield states it as *\"the humans are no longer necessary to do the information routing… all of the information is routed automatically to the person who needs it. They don't need to go through layers and layers of management to get approved\"* and concludes *\"no middle management.\"* The vantages differ in scale and in stakes — Blomfield is advising sub-20-person startups where the layers do not yet exist, which is a much weaker test of the claim than an incumbent removing them"
    confidence: 0.6
---

# Blomfield — Building And Structuring An AI Native Company

> In this presentation from Startup School Paris, Y Combinator General Partner Tom Blomfield shares findings from his research on how companies are being built with AI infrastructure placed in from the start.

## TL;DR

A **~21-minute talk** by **Tom Blomfield**, General Partner at **[[Y Combinator]]**, at Startup School Paris. He opens with an unusually strong epistemic caveat and repeats it in substance throughout: *"the main caveat I want to start with is **no one knows how to do this**. And so this is very theoretical. It's based on hundreds of YC companies that we're working with right now. Lots and lots of people are trying things, and I think if anyone tells you they've got it all figured out, they are probably lying."* He is explicit that even YC has not finished: *"I don't think we've yet got it fully figured out."*

**1. The opening provocation — a forecast about YC's own core function.** *"I expect by the end of 2026, or possibly by the first batch in 2027 — I don't know if we'll take the PR risk of it — it will be possible to, end to end, have an AI fully read all the applications, pick the companies to interview, conduct the interview, select the companies to fund, give them advice throughout the batch on how to run their companies more effectively, introduce them to investors, review their pitch decks, and then debug their pitch meetings. I think an AI will be able to do all of that end to end… We've got quite a lot of it working already."*

**2. The historical argument for why org charts look the way they do.** He starts from the Roman legion — the *contubernium* (eight soldiers sharing a tent, equipment and a mule, led by a *decanus*), ten of which form a century — and the point of the hierarchy: *"this was the way that the Roman Empire projected power, and they would pass information down and receive reports up, and a human being was responsible for being that conduit the whole way. And bizarrely, like 2,000 years later, we're still basically running the same kind of thing."* He credits a [[Andrej Karpathy|Karpathy]] tweet for the observation and a Jack Dorsey tweet for the formulation that *"there's an underlying assumption that organizations have to be hierarchically organized with humans as a coordinating mechanism. And I basically think AI breaks that apart."*

**3. The diagnosis of how most companies use AI, and why it caps out.** *"Most companies sort of experienced ChatGPT as a Q&A bot… and then maybe they've moved to longer-running, perhaps what you might call an agentic system. But basically you ask the agent to go and do something, it goes away until it gets stuck, and it comes back to you. And you as a human are like the gating mechanism. So while you are asleep, the thing can't work. If it stops halfway through at 3 in the morning, it's waiting on input from you, it can't go anymore."* The result is the productivity framing he wants to displace: *"you can do things like making engineers 20% more productive. You can add copilots for lawyers to make their existing workflows go a little better… but really, all of these things are dependent on humans being the coordinating mechanism."*

**4. The AI loop — the talk's central construct.** Five components, in his order:

- **Signal in** — *"product telemetry, inbound messages… data from the real world, like billing signals, support tickets, code changes."*
- **Policy layer** — *"what rules constrain the AI? What things must it ask for approval for? What does it have to log?"*
- **Tool layer** — internal APIs, sending emails, updating billing, *"and you might have APIs for this or MCP or whatever."*
- **Quality gates** — and here he takes an explicit position against the default: *"which could be a human, and I'd argue **probably should not be a human** in all but the most extreme cases. The quality gate can often be a second adversarial LLM. It might be something that's looking at the output saying, are we suffering from prompt injection here? Or in the case of a bank, are we giving financial advice here, yes or no? … A really easy example for engineers is the quality gate might simply be a second model doing code review."*
- **Learning mechanism** — *"you loop back around, you deploy the thing, you make the change and you see how it impacts the real world."*

The payoff condition: **"If you can do this entire loop without a human, your product starts improving itself when you're sleeping."**

**5. The worked example — YC's own overnight meta-agent, and why he calls it a head-explosion moment.** The first layer is unremarkable by 2026 standards: an English-to-SQL agent over YC's data (*"7,000 companies, 20,000 founders, many hundreds of thousands of applications"*), built *"a year or two ago"*, which he assesses honestly as *"a tool that kind of makes a data analyst 20 or 30% more productive… It was fine, and it would keep hitting edge cases or not be able to do certain things, and I'd be like, oh, that's annoying."*

The second layer is the point: *"we shipped something about two or three months ago which for me was the head-explosion moment, which was a **second agent** which lives on top of this data query agent. The second agent **runs overnight** and it looks for all the queries that any human has done during the day, and it looks for success and failure. The success is like, yeah, I copy it, I send the email. The failure is, ah, this didn't work, or I hit a permission issue, or the database index doesn't work, or it requests some permission it doesn't have. And then that second AI agent overnight goes and **puts in pull requests to fix all of the problems from the day before**. And so if you go back as a human on the second day and run the same query as yesterday, it now works."*

He generalises immediately, citing PostHog doing the same for product telemetry (*"eventually you'll automerge those pull requests… your entire product surface will become self-improving"*) and a Karpathy auto-research experiment. His reduction: *"all this is is **hill climbing**. If you have a measurable outcome, you can just come up with ideas, you can test it. Did we go up the hill or down the hill? If down, discard. If up, keep, and just keep hill climbing. And computer systems are really really good at this kind of hill climbing work **because they never stop**."*

**6. A second YC example — office hours as a self-rewriting user manual.** YC's internal user manual is *"written over the last 15 years and it's like 500 pages long, and a lot of it was very very good like 5 years ago, and then AI happened, and honestly a bunch of the advice is just not relevant anymore."* Blomfield was assigned the rewrite and *"procrastinated and procrastinated and procrastinated."* The loop replaced the task: YC began recording office hours ~6 months ago, now holds *"3 or 4 thousand hours"*, and *"someone on the team had the idea of, what if we just transcribe and then mine all of the advice we actually give in office hours and then use that to rewrite the user manual. And so when the advice changes, the AI will see what the humans are saying, extract the insight, and just rewrite the user manual and push it, so it becomes this living guide."* Then the manual becomes queryable by an advice agent — and he makes a superhuman claim about the composite: *"I think you can actually get **superhuman advice** from this thing, because it's able to recall perfectly and access the intelligence of **16 partners**, not just one with fallible memory."*

**7. From loops to AI employees, and then to a company brain.** Give the agent a VM with web search, an internal company-directory crawler, Slack-history search, persistent file storage (*"so it can come up with a plan and write the plan to disk, so if it fails halfway through it can resume"*), and code execution. *"And now you've basically got an AI employee. We're at the very very early stages of this with something like OpenClaw."* The next step he expects is loop-to-loop communication. On *company brain* — a term he flags as already worn out (*"it got very very popular about six weeks ago and as of two weeks ago I see people in the audience with company brain written on a t-shirt"*) — his substantive definition borrows Dorsey's phrasing: *"in a conventional company, intelligence is spread throughout the people and the hierarchy routes it. In this new model, **intelligence lives in the system**."* The mechanism he names is the SOP-vs-practice gap: *"lots of companies try and write down standard operating procedures, but then when you actually observe how people do the job, they're like, oh, well, in this edge case really I should do this other thing. And there's a lot of stuff in people's heads that if it weren't in people's heads and it was actually written down, you'd get a lot of value out of it."*

**8. Where humans go — the edge, not the middle.** Quoting Dorsey: *"people reach into places the model can't yet go. They sense things the model can't perceive. Intuition, opinionated direction, cultural context, trust dynamics, the feeling in a room… They make the calls a model shouldn't make on its own, especially ethical decisions, novel situations, and high-stakes moments where the cost of being wrong is existential. A world model that can't touch the real world is just a database."* Blomfield's gloss: humans are *"in the sales calls, visiting the client office to reassure people, to convince the CEO, to pitch the investor. It's all of the emotional, interpersonal stuff that the humans are there for. But the humans are no longer necessary to do the information routing."*

**9. Four practical prescriptions.**

- **Burn tokens, not headcount.** *"We're seeing founders get to demo day with a million dollars of revenue, and some getting to Series A with 10 million of revenue, with a fraction of the people they had before. You can argue about whether it's a thousand x or whatever, but it's multiple times more."*
- **No middle management; two roles matter.** *"Everyone has to be an individual contributor actually doing the work, coming to meetings with **working prototypes, not decks**."* And the **DRI** — *"a single person whose head is on the block to make something happen. As soon as you have a committee — I worked at a bank and we had so many committees for everything, and it grinds things to a halt."*
- **Make everything legible to AI.** *"Make all your data readable to AI. That means recording everything, transcribing literally every meeting. If you can't get access to Slack DMs, **I would ban Slack DMs**. Make everything in public channels the AI can access. **Every action needs to create an artifact** — a written or recorded version. Otherwise it basically didn't happen to the AI."*
- **On-demand internal software for all company operations.**

**10. The investor-call simulation — the newest and most double-edged example.** Founders take 40–60 investor calls; recording them yields immediate coaching (*"you spent 90% of the time talking, or you really fumbled this question"*). But YC sits on the other side of the aggregation: *"we also get data on the other side of that conversation. These founders are meeting the same investors. So we could **simulate the investment call** — here's exactly how [firm X] does every single investment call, whereas [firm Y] will ask you this question and this question, or this particular partner will always say what's your wedge, or what's your moat if Anthropic comes after this, and here's a great way to answer that."* His stated justification: *"I don't feel bad about doing this at all, because I absolutely know that those investors are also recording this and pumping it into their AI."*

He closes with the question the talk is really asking: *"If you were starting a company today, would you build it like this? … Most of you are early-stage enough to just build it right from the start."*

## What was actually ingested

The **complete** talk — all 570 caption segments across `duration: 21:20` / `length_seconds: 1280`, with all thirteen chapter markers. The Q&A that follows is **not** in this recording (he defers to a joint panel: *"I think we have — we'll just do questions with all of us"*). He also notes this is an update of an earlier talk *"about a month, maybe six weeks ago"* which is on YouTube separately and is **not** in the wiki.

ASR cleanup was applied (*contouium* → contubernium, *carpathy* → Karpathy, *Andre Horitz* → Andreessen Horowitz, *Post Hog* → PostHog, *DRR* → DRI, and the repeated *rooting/roots* → *routing/routes* where the sense is information routing; full list in the raw file's `notes:`).

**Scope warning.** The speaker's own caveat is the right frame and should be carried into any citation: *"no one knows how to do this… this is very theoretical… if anyone tells you they've got it all figured out, they are probably lying."* Concretely, the source contains:

- **Two verifiable-in-principle internal examples** (the overnight PR agent; the office-hours-to-user-manual loop), both from YC itself, both described without any measurement — no error rate, no PR acceptance rate, no measure of whether the rewritten user manual is better, no cost.
- **No counter-examples and no failure modes.** Nothing in the talk describes a loop that went wrong, an automerged bad PR, or a company that tried this and regressed. The absence is notable given the talk's own claim that quality gates should usually not be human.
- **Revenue-per-headcount claims stated as a range with the multiplier explicitly waved off** (*"you can argue about whether it's a thousand x or whatever"*). No baseline, no denominator, no sample.
- **A selection-biased population.** The evidence base is *"hundreds of YC companies"* — early-stage, small, greenfield, self-selected for AI enthusiasm, and advised by the speaker's own firm. His strongest practical claim (*"this is by the way easier when you're starting out"*) is also the boundary condition: nothing here tests whether the loop architecture survives contact with an incumbent's legacy systems, compliance regime, or existing management layer.

## Dynamic-capabilities tagging

- **`digital-transforming/redesigning-internal-structures`** — the talk's core is a structural claim, and it is explicit about the mechanism it wants to remove. Hierarchy exists because humans routed information; if routing is automated, the layers lose their rationale, hence *"no middle management"* and *"the key roles for me are the IC… and the DRI."* The cell's canonical activities include *"designing team-based structures"*; this is the sharper version — designing the structure around loops rather than around people, with humans repositioned at the edge where the system touches reality.
- **`digital-transforming/improving-digital-maturity`** — the legibility prescriptions are a digital-maturity programme stated as house rules: transcribe every meeting, ban Slack DMs so knowledge lives in AI-accessible public channels, and *"every action needs to create an artifact… otherwise it basically didn't happen to the AI."* The office-hours-to-user-manual loop is the same cell's *"leveraging digital knowledge inside the firm"* taken to its conclusion — 15 years of tacit partner advice mined out of 3,000–4,000 recorded hours into a self-updating document, then made queryable.
- **`strategic-renewal/collaborative-approach`** — the loop-to-loop and human-at-the-edge model replaces the internal collaboration pattern wholesale: coordination stops being a chain of human handoffs and becomes agents exchanging state, with humans contributing the interpersonal and high-stakes judgement work the model cannot reach. The investor-call simulation extends the pattern outward, turning a shared cross-portfolio experience into a collective asset.
- **`contextual/internal-barriers`** — the talk names its barriers precisely, and they are the cell's: *"high level of hierarchy"* (the Roman-legion inheritance, layers of directors and VPs) and slow decision-making by committee (*"I worked at a bank and we had so many committees for everything, and it grinds things to a halt"*). The human-as-gating-mechanism diagnosis — the loop stalls at 3am waiting for a person — is a barrier claim about process rather than culture.

## Linked entities and concepts

- [[Y Combinator]] — publisher and the speaker's firm; also the subject of both worked examples. Updated in this ingest.
- [[Andrej Karpathy]] — credited for the org-chart observation and for the auto-research hill-climbing experiment. Updated in this ingest.
- [[concepts/ai-agents|ai-agents]] — the AI loop's five components, the AI-employee-with-a-VM construction, and loop-to-loop communication.
- [[concepts/agent-harness|agent-harness]] — the quality-gate-as-adversarial-LLM pattern, the policy layer, and the persistent-plan-on-disk resume mechanism are harness-layer claims.
- [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] — the human-as-gating-mechanism diagnosis of why most deployments cap at 20–30% productivity.
- [[concepts/knowledge-graphs|knowledge-graphs]] — the company-brain construct and the SOP-vs-practice gap as the codification problem it addresses.
- [[concepts/automation-vs-augmentation|automation-vs-augmentation]] — the talk is an explicit argument for moving from augmentation (copilots, 20% faster) to closed-loop automation, with humans relocated rather than assisted.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the four cells tagged above.
- [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|Garg / YC]] — the mechanism-level instance of the same self-improving pattern; see `relationships:`.
- [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu / YC]] and [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan & Hu / Stanford CS153]] — the accelerator's earlier statements of the AI-native thesis.
- [[2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm|Nadella / *Possible*]] — the incumbent-scale version of the disappearing-management-layer claim.

**Dangling** (single-source mention, deferred per [author-entity promotion](../../CLAUDE.md#author-entity-promotion)): Tom Blomfield, Jack Dorsey, PostHog, OpenClaw, Startup School Paris.

## Source quality note

Auto-generated captions, ASR-cleaned. Two scraper artifacts (*[snorts]*, *[gasps]*) are mic-noise annotations and were left in the raw file. The Roman-army terminology was the densest cleanup area and is now correct.

**This is accelerator content advising the accelerator's own founders**, delivered by a partner whose firm benefits if its portfolio adopts the described posture, and drawing its two concrete examples from the accelerator's own internal tooling. The investor-call-simulation section additionally describes YC building an information-asymmetry asset out of its portfolio's aggregated fundraising conversations — presented as a founder benefit, and defended on the grounds that investors do it too.

Its value to the wiki is threefold and specific. First, the **overnight meta-agent** is the corpus's clearest description of a closed self-improvement loop operating on an *internal tool* rather than on a product — the failure-classification-to-pull-request path is concrete enough to evaluate or replicate. Second, the **quality-gate-should-not-be-human** position is a stated, arguable claim rather than an assumption, and it directly opposes the human-in-the-loop default that most other corpus sources treat as settled — the wiki should hold it as a live disagreement rather than a consensus. Third, the speaker's **opening caveat is unusually honest for the genre** and is the correct frame for everything after it: this is a theory of the AI-native company, articulated by someone with wide but shallow visibility into hundreds of very early companies, with no measurement attached.
