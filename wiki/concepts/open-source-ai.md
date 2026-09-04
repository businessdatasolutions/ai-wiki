---
type: concept
aliases: ["open source AI", "open-source AI", "open-weight models", "open weights", "open models", "AI sovereignty", "own vs rent AI"]
tags: [open-source-ai, open-weight-models, own-vs-rent, ai-sovereignty, concentration-of-power, china-open-models, safety-through-transparency, hugging-face]
confidence: 0.90
last_confirmed: "2026-09-04"
accessed_at: "2026-09-04"
source_count: 10
relationships:
  - type: supports
    target: enterprise-ai-adoption
    via: "the own-vs-rent flow (frontier APIs for experimentation, owned/open models for production at scale) is a driver of how enterprises adopt AI"
  - type: supports
    target: small-language-models
    via: "small is what makes local ownership practical — the own-vs-rent argument only reaches a laptop if the model fits on it. Both the SLM position paper and its practitioner reading argue the point in the reverse direction too: you cannot experiment with a model you can only rent"
  - type: supports
    target: agent-harness
    via: "shares the own-vs-rent ownership motif — 'the model is what you rent, the harness is what you own'; open weights are the substrate that specialization/harnessing is owned on top of"
quality_score: 1
---

# Open-Source AI

The stance — and the class of **open-weight models, datasets, and tooling** — that treats AI as something organizations should **own rather than rent**, published transparently rather than gated behind closed APIs. The wiki uses "open-source AI" as an umbrella for four interlocking claims that recur across vendor-CEO sources: (1) the **own-vs-rent** economics of production AI, (2) **open vs. closed** as a *safety* question, (3) **AI sovereignty** (who *shares* the open source a country *uses*), and (4) **concentration of power** as the field's top risk.

The motif is already latent in [[agent-harness]] — *"the model is what you rent, the harness is what you own"* — and crystallizes across two independent vendor-CEO interviews two days apart: [[2026-07-08-jensen-huang-why-companies-need-open-agent-systems|Jensen Huang (NVIDIA)]] and [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|Clem Delangue (Hugging Face)]].

## The own-vs-rent thesis

Both vendor CEOs make the same core argument from different vantages:

- **Delangue** ([[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|Hugging Face]]): "companies need to **own AI and own models instead of renting them** and outsourcing them to someone else." An AI/tech company shouldn't outsource its core capability to "a black-box API you don't control, don't have visibility on, don't have ownership" of. AI is "the next generation of software" / **software 2.0**, and software was always built in-house. The empirical flow he reports: enterprises **start on frontier APIs** to experiment and launch, then **switch to open models when they hit production and scale** because frontier-model cost "becomes too big." His projection: frontier models for experimentation and high-value tasks; **most production workloads on private or open-source models.**
- **Huang** ([[2026-07-08-jensen-huang-why-companies-need-open-agent-systems|NVIDIA]]): "you can't possibly not continue to control it, improve it, make it better" — outsourcing your specialized intelligence "makes no sense," whether for a person, company, or country. Huang's framing is **proprietary specialization on an open substrate**: build domain-specific "super agents" on open weights (Nemotron) inside a harness you own. Same "start with the frontier, specialize once it's good enough" sequencing.

The convergence is strong; the emphasis differs. Delangue foregrounds **open source specifically** and **cost-at-scale** as the switching driver; Huang foregrounds **owned specialization** and the [[agent-harness|harness]] as the ownership locus. Both cite [[NVIDIA]]'s **Nemotron** open-weight family as evidence open models are reaching frontier performance cheaply (Huang: Nemotron 3 Ultra 86% vs. Claude Opus 87% at ~10× lower cost).

## Open vs. closed as a safety question

Delangue's contested position: **open source has historically been *less* dangerous than closed initiatives** because it is transparent — capabilities are legible and defenders can patch them. API guardrails are "very shallow and quite ineffective" ("easy to jailbreak," weights can be stolen), so keeping models "behind closed doors for just a few players" doesn't make AI safe — it makes it *more* dangerous by creating **asymmetry of power** between actors who can access/steal/misuse weights and those who can't defend themselves. His prescription: level the playing field, maximize transparency, and make the *attacks* illegal rather than the *tools*. This runs against the closed-labs framing that (per the interview's own premise) halted the Anthropic **Fable** and OpenAI **GPT 5.6** releases on cybersecurity grounds — see Debates, and [[responsible-ai]].

## AI sovereignty and China's open-model lead

Per Hugging Face's own Spring 2026 report (cited in [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|the Delangue interview]]), **Chinese models accounted for ~41% of downloads** — the plurality, surpassing the US. Delangue's causal claim: US AI leadership 2016–2023 came *from* open research ("the T in ChatGPT came out of Google sharing an open source transformer"), so open source "creates the conditions for AI leadership almost automatically" — and if China keeps leading in open source, it may "lead AI in general, next year or the year after." He calls the "China is only good because of distillation attacks" rebuttal "reductive and simplistic" (distillation is a small factor everyone uses). The **sovereignty** worry: US scale-ups (Cruise, Airbnb) and *all academia* already build on Chinese open weights because "you can't study an API — it's a black box"; ideally more of the open source *used* in the US would be *shared by* US organizations ([[NVIDIA]] as "the king of American open source AI"; startups like Reflection).

## Concentration of power as the top risk

Delangue: "the biggest risk in AI is **concentration of power**." The AI companies becoming the most *valuable* are also becoming the most *powerful* (he cites an AI firm's leverage vis-à-vis the US Department of War); a world where "a few companies completely dominate AI" is "basically similar to if there were just one or two companies able to do software" — "the real dangerous scary scenario." Open source is the counter-force: it "enables innovation, competition, job creation; you don't create monopolies." The same logic drives his robotics argument — a home robot shouldn't be "a black box controlled by a few," "especially if these organizations' CEO is not the most stable person in the world."

## Two non-vendor routes to the same conclusion ([[2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company|BBC AI Decoded]] + [[2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity|Frey / Bloomberg]], August 2026)

Both of this page's founding sources were open-model vendors, which capped its confidence at 0.72 for self-interest. Two August 2026 sources reach substantially the same conclusions **without selling open weights** — an enterprise-AI advisor arguing from data trust, and an academic economist arguing from national capacity.

**Peter Grant**, on the BBC's *AI Decoded* panel, states the enterprise buyer's version of the own-vs-rent argument, and reaches a stronger conclusion than this page previously held — a partial **return to on-premise**:

> *"Kimi just got released from China, which is an open model… you can take that model, you can install it yourself, you could put a firewall around it, you understand the weights, the algorithms and everything else. Where a closed model, you'll be giving your data to that model. They can take it, they can use all that information. And that's what scares enterprises the most… I think what you're going to see is a hybrid. You're going to see large organizations actually go back to on-prem. They will protect all their data at all costs and they decide where they send the query to for the agent — whether it goes outside the organization for a very basic query or internally for something to protect their own IP. Which ultimately **comes back to trust.**"*

The routing decision he describes — per-query, by sensitivity, between an external frontier API and an internal open model — is a more granular version of the own-vs-rent flow this page holds from [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|Delangue]], and it is driven by **IP protection rather than by cost at scale**. Note the caveat: Grant sells enterprise AI advisory services, so he is not a disinterested party, but he has no stake in open weights specifically.

**Carl Benedikt Frey** supplies the page's first genuinely independent vantage — an academic economist with no commercial position in the question — and adds a **geopolitical trigger** the page has not carried. His premise is that frontier-model access is becoming a lever of statecraft: "you saw that recently with the Trump administration imposing restrictions on foreign use of Anthropic's latest model. We can expect to see similar things happening going forward, perhaps at greater scale." The conclusion he draws for every country behind the frontier:

> *"You cannot really be dependent on the technology leader. You have to try to grow some domestic capacity, and with large language models **the easiest way of doing that is through open source or open weights** — and that's how China has closed the gap. It really embraced an open-weight ecosystem, in large part because of **export controls on chips**, which essentially forced it to go there."*

Two things this adds. First, an **independent causal account of China's open-model position** that matches Delangue's observation without sharing his interest: not ideology but constraint — chip export controls pushed China toward an efficiency-and-openness strategy. Second, a **forecast about the demand side** of the open ecosystem: many countries "will be probably pivoting either towards Chinese or European technology if they feel that America is an unreliable trading partner in technology," or attempting a domestic open-weight ecosystem, "although that is going to be a harder approach for most places."

Four sources now, from four positions — an open-model platform CEO, a silicon vendor, an enterprise-AI advisor, and an academic economist. The last two have no stake in open weights, which is what lifts this page's confidence from 0.72 to **0.80**. What is still missing is *empirical* corroboration: no source on this page measures how much enterprise inference actually runs on owned or open models versus rented frontier APIs.

## Open weights as an *American competitiveness* argument ([[2026-07-29-ng-washington-post-china-open-source-ai-competitiveness|Ng / Washington Post Live, July 2026]])

The page's existing sources argue for open weights from cost ([[2026-07-08-jensen-huang-why-companies-need-open-agent-systems|Huang]]), data trust ([[2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company|Grant]]) and national capacity ([[2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity|Frey]]). [[2026-07-29-ng-washington-post-china-open-source-ai-competitiveness|Andrew Ng]] adds the argument that has the most political traction and is the most contested: that **open weights are a condition of American leadership, not a threat to it.**

> *"To sustain competitive advantage in America, one of the most important things we have to do is support and sustain open models… **the success of these businesses cannot be at the cost of shutting down everyone else's access to open models.** … I've been alarmed at the amount of lobbying that a handful of businesses have been doing saying that open models are dangerous. **I think that's false.** … **the lobbying against open models has hampered American AI development.**"*

He is careful to establish he is not hostile to the frontier labs first — "I think I'm the only person that both Sam and Dario have worked for… I really hope they do well and have fantastic IPOs."

**His mechanism for why China's open strategy worked** is knowledge diffusion, and it is the page's clearest causal account: "when you release models freely for anyone to use, it helps the whole world. **Yes, but it helps you even more than it helps the whole world.**" The American counterpart is opaque by construction — "because a lot of American work has gone into closed proprietary models, it's just much harder to know: if you have a question, who should I call up to understand how to do this modelling thing?" This complements [[2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity|Frey's]] account (export controls forced China toward openness) rather than competing with it: Frey supplies the cause, Ng the compounding effect.

**On distillation he is the page's most direct dissenter** from the standard American framing: "the concept that distillation is a major factor has been overstated, **vastly overstated**." Two arguments. A symmetry argument: "AI labs all around the world took data off the open internet and used it to distil knowledge from the internet into their AI models. **Is it fair for them to turn around and say, *I've distilled the internet into my model; if anyone distils my model from here on out, that's not fair?***" And a timing objection to the claim that a recent Chinese release was distilled from a short-lived frontier model — "there just couldn't have been that much data, and how could [it] have been trained in such a short time." He also notes the traffic runs both ways: American labs read Chinese open research heavily, "you have to be dumb not to." This corroborates [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|Delangue's]] near-identical dismissal from an independent vantage a fortnight earlier — **but note both are open-source advocates**, so the page holds this as a well-argued position of two interested parties rather than as a settled technical finding.

**Two economic points.** The market-share consequence of under-investing: "in places where they're a little bit more price sensitive, Chinese models have really gained tremendous market share… for example in Africa, **DeepSeek adoption is through the roof.**" And the unit economics that drive it: "if an open model allows you to get intelligence at one fifth or one third of the cost… **if your supply of intelligence costs three times more, that's a very fundamental business disadvantage.**" On the open-weights business model he is honest that it is unresolved — Red Hat and Linux as precedent, publicly traded Chinese open-source companies "doing just fine at least in the stock market," but "the details of how to do this with open models, I think, are **still being worked out.**"

**His firm-level prescription is the transferable one**: *preserve optionality.* "I can't forecast in a year or even six months what is going to be the top model. So one of the most important things to do is preserve optionality… **I don't let myself be locked into any one of them.**"

Five sources now. Confidence moves 0.80 → **0.85**: Ng is a third distinct argument (competitiveness) alongside cost, trust and sovereignty, and the distillation dissent is now double-sourced. It stays below the cap for the reason the page has always given — **every source here is an interview, none is empirical**, and Ng is the most interested party of the five.

## "Not your weights, not your product" — open weights as the enabling condition for enterprise ownership ([[2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai|Huang / Sequoia, August 2026]])

A venture investor's framing of open weights, which matters here because it is the corpus's third own-vs-rent source and the first from someone who is neither a model platform nor a compute vendor.

Huang defines **sovereign AI** as *"companies owning their own intelligence without external dependencies **down to the weights**"*, and ports the slogan from crypto: *"in the crypto days there was this meme for the DeFi degens — not your keys, not your crypto… I hereby present the AI version of this meme: **not your weights, not your product.**"* She draws the boundary immediately, which is more careful than the slogan: *"we are definitely not telling our companies to get off Opus or GPT… For coding agents, for desktop work, for frontier-level APIs, the closed model APIs are wonderful."*

**The claim that is new relative to what this page already holds** is about performance rather than cost or control:

> *"The beauty of owning your stack is that you can actually drive frontier-level performance now. And so this is somewhat new, and in large part this is thanks to the newest open-weight models, especially **Kimi K3** and **GLM-5.2**, being extremely good. **Because the weights are available, they're actually much more malleable than working with the closed APIs.** And so you start with a baseline that's already close to frontier and then with a good enough technical roadmap — strong post-training, prompt harness engineering, online learning — you can actually reach **better than frontier** performance by owning your stack. And so this is **new for 2026**."*

This reframes the open-weights choice from a **cost-and-control** decision to a potential **performance** one, and does so specifically in-domain. It is the strongest version of the claim in the corpus — and it is **entirely unevidenced**: no benchmark, no company-plus-figure, no before/after, and the speaker twice flags that she is not technical and that the framework is opinionated.

Her four drivers, in stated order, map onto material this page already holds: **cost** (with the COGS inversion — the most advanced deployers switch first), **speed** (*"a small distilled custom model can beat a large general one"* in coding and security), **performance** (the new one, above), and **controlling your own destiny** — where she is notably generous to the labs: *"Anthropic and OpenAI, I actually think to their credit, they've been really wonderful partners to a lot of the ecosystem, but companies are increasingly finding that they want their own set of independent legs to stand on."*

Her **higher-floor / lower-ceiling** characterisation is the most reusable thing in the talk and belongs on this page as a decision frame:

| | Closed-API stack | Owned stack |
| --- | --- | --- |
| Production layer | foundation model + out-of-box harness | open-weight base + heavy post-training; choose and configure an open harness, its logic, tools and context |
| Development layer | prompts, context, your own evals | eval monitoring and drift-watching, high-quality post-training data (expert trajectories / synthetic data / RL environments), online learning |
| Trade | *"a higher floor, but a lower ceiling, because you don't actually have the ability to take your own data, to take online production data and improve your own intelligence"* | *"like opening a Pandora's box"* |

She also notes the policy dependency this page tracks: *"just last week, Jensen led the charge in making sure that open-weight models remain available in the US, and it was awesome to see the near unanimous wave of support"* — the same dependency [[2026-07-29-ng-washington-post-china-open-source-ai-competitiveness|Ng argues from the competitiveness side]].

**Source-quality caveat, load-bearing.** This is investor content addressed to the speaker's own portfolio at an event designed to change that portfolio's behaviour, and the companies named as evidence are largely portfolio companies. The wiki now holds three own-vs-rent sources — a platform CEO ([[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|Delangue]]), a substrate vendor ([[2026-07-08-jensen-huang-why-companies-need-open-agent-systems|Jensen Huang]]) and an investor (Huang) — whose **shared blind spot is that all three sell something that becomes more valuable if enterprises stop renting**, and none of them measures the outcome. Confidence on this page is raised to 0.87 on the strength of a third independent vantage converging, not on the strength of the evidence, which remains absent.

## The three tiers, stated plainly (added 2026-09-03)

This page has carried *open-weight models* as an alias since it was created without ever laying the spectrum out. [[2026-09-02-github-podcast-demystifying-ai-terms-loop-engineering-squads-harness|The GitHub Podcast, S02E02]] supplies the cleanest short version in the corpus, from a developer-education vantage rather than a vendor-CEO one:

| Tier | What you get | What you don't |
|---|---|---|
| **Closed** | An API. *"Everything is just exposed via API"* — the default most people have used ([[OpenAI]], [[Anthropic]]) | Weights, data, method — all of it |
| **Open weight** | *"You can download the weights, you can use the model for free… hosting it on your machine"* | *"You don't have access to the data set and the training method"* |
| **Open source** | *"Every part of the model that was used to train the model is available openly"* — enough to build your own version | — |

The framing underneath it is the transferable claim: *"when we think of open source traditionally, we think of just software — the code. But now in this new AI phase there are more aspects to making a model work than just code, so having an open-source model would mean that every part of that is available to you."* Open weights are therefore *"slightly different because it's not as open, but still kind of has that same ethos."*

Two things this settles for the page. First, **the wiki's own-vs-rent sources are almost entirely arguing about the middle tier, not the top one** — Delangue, Huang, Ng and Frey all say *open source* and mean *open weight*, and the distinction matters exactly where this page's safety argument lives, because transparency claims that hold for a published dataset do not automatically hold for published weights alone. Second, it clarifies what [[concepts/agent-harness|agent-harness]]'s *"the model is rented, the harness is owned"* motif actually buys: open weights make the model **run-anywhere**, not **inspectable**, and specialisation on top of them is ownership of the harness rather than of the model.

The source adds no evidence and does not move this page's confidence — it is a vendor-produced developer podcast with no measurement in it. It is cited for definitional precision only.

## The experimentation argument for open weights (added 2026-09-04)

The page's four claims are all about *production*: own-vs-rent economics, safety, sovereignty, concentration. [[2026-08-25-sokolenko-pycon-de-demystifying-agentic-ai-small-language-models|Sokolenko at PyCon DE 2026]] adds a fifth that is about *learning*, and it is the one a working engineer feels first. Reading the [[Berkeley Function Calling Leaderboard|BFCL]] rankings on stage, he notes that the top three tool-calling models are Claude Opus 4.5, Gemini 3 and GLM 4.6 — and then:

> *"They are all proprietary. So you cannot use them for local experimentation. You cannot use them for experimentation in your environment."*

So the model he actually uses is the highest-ranked one he is *allowed* to run: [[xLAM]]-2 at 32B, 4-bit quantized, on a two-year-old laptop, at zero marginal cost. The whole talk's thesis — the way through the agentic hype is to build one yourself — depends on open weights being available at a size that fits consumer hardware. Openness without smallness would not have delivered it; see [[small-language-models]].

The [[2025-06-02-belcak-nvidia-small-language-models-future-agentic-ai|NVIDIA SLM position paper]] reaches the **democratisation** claim from the compute side rather than the geopolitics side of [[2026-07-29-ng-washington-post-china-open-source-ai-competitiveness|Ng's argument]]:

> *"When more individuals and organizations can participate in developing language models with the aim for deployment in agentic systems, the aggregate population of agents is more likely to represent a more diverse range of perspectives and societal needs."*

Worth noting who is making these arguments: an **enterprise vendor's research lab** ([[Salesforce AI Research]]) open-sourcing both the [[xLAM]] weights and the synthetic training data, while the same company's product line sells the agentic platform Sokolenko cites as the emblem of the hype. Open-weight releases are increasingly a competitive move by large vendors, not only a community one.

## Sources consulted

- [[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|Delangue / Hugging Face (TechCrunch Equity, Jul 2026)]] — the fullest single-source treatment: own-vs-rent flow, safety-through-transparency, China's open-model lead, concentration-of-power, local AI / robotics.
- [[2026-07-08-jensen-huang-why-companies-need-open-agent-systems|Huang / NVIDIA (LangChain, Jul 2026)]] — the own-vs-rent thesis from the substrate/silicon side; proprietary specialization on open weights; the Nemotron benchmark.
- [[2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company|BBC AI Decoded (Aug 2026)]] — the enterprise-buyer vantage: self-hosting an open model behind a firewall, per-query routing by sensitivity, and a predicted partial return to on-premise, driven by IP protection rather than cost.
- [[2026-07-29-ng-washington-post-china-open-source-ai-competitiveness|Ng / Washington Post Live (Jul 2026)]] — the American-competitiveness argument: open weights as the condition of US leadership; knowledge diffusion as the mechanism behind China's gains; distillation "vastly overstated"; price-sensitive markets defaulting to Chinese open models; *preserve optionality* as the firm-level prescription.
- [[2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity|Frey / Bloomberg Trumponomics (Aug 2026)]] — the academic-economist vantage: open weights as the route to domestic AI capacity for countries behind the frontier; export controls as the cause of China's open-weight position; frontier-model access as an instrument of statecraft.
- [[2026-09-02-github-podcast-demystifying-ai-terms-loop-engineering-squads-harness|The GitHub Podcast S02E02 (Sep 2026)]] — the definitional vantage: the closed / open-weight / open-source three-tier spectrum stated plainly, and the observation that "open source" for a model means more than code. No evidence; cited for precision.
- [[2026-03-20-huggingface-agentic-evaluations-workshop|Hugging Face Agentic Evaluations Workshop (Mar 2026)]] — the open-evals corollary: open weights as a precondition for *studying, trusting, and improving* AI (background support, not counted in `source_count`).

## Debates and supersession

- **Open-vs-closed as a safety question is unresolved in the corpus.** Delangue argues transparency makes open source *safer* and concentration is the real danger; the closed-labs framing (which halted the [[Anthropic]] Fable and OpenAI GPT 5.6 releases "for cybersecurity concerns") argues the opposite — that frontier capabilities need gating. The wiki holds both without resolving; see [[responsible-ai]]. No supersession.
- **Vendor-advocacy discount, partially lifted (2026-08-12).** The page's two founding sources are vendor-CEO interviews (Hugging Face sells open-model infrastructure; NVIDIA sells the silicon and Nemotron weights beneath it), so their pro-open claims are self-interested. The August 2026 additions are not: [[2026-08-01-bbc-ai-decoded-why-isnt-ai-working-for-your-company|Grant]] sells enterprise AI advisory rather than open models, and [[2026-08-05-frey-bloomberg-trumponomics-why-ai-isnt-boosting-productivity|Frey]] is an academic with no commercial position. `confidence` moves 0.72 → **0.80** on that basis. It stays below the cap because **no source on this page is empirical** — all four are interviews. The AI Index open-weight-trend data and the primary Hugging Face Spring 2026 report remain the open ingest targets that would close the gap.
- **Two different drivers of the same behaviour, not yet disentangled.** Delangue and Huang argue firms move to open/owned models as **cost** bites at production scale; Grant argues they move for **IP protection and data control**; Frey argues states move for **strategic autonomy** under export-control and access-restriction risk. All three predict the same migration, so the page cannot currently distinguish them — and they imply different things about what would reverse it (cheaper frontier inference, better contractual data guarantees, and geopolitical détente respectively).
- **"Workloads move to open/owned" ≠ "frontier labs decline."** Delangue explicitly hedges that OpenAI/Anthropic can remain "the most valuable companies" on frontier reasoning even if most workloads run on open/owned models. The claim is about *where workloads run*, not frontier-lab viability — keep the two distinct.

## Related concepts

- [[agent-harness]] — the ownership locus of the own-vs-rent motif; open weights are the rented/owned *model*, the harness is the owned *specialization*.
- [[foundation-models]] — open-weight models are a subset of the foundation-model substrate; this concept is the *openness dimension* of that substrate.
- [[enterprise-ai-adoption]] — the frontier-experiment → owned-production flow is an adoption pattern.
- [[responsible-ai]] — the safety-through-transparency vs. closed-gating debate lives across both pages.
- [[generative-ai]] — the broader capability class these open models deliver.

## A security asymmetry (added 2026-08-30)

[[2025-06-12-spracklen-package-hallucinations-code-generating-llms|Spracklen et al.]] measured package hallucination at **≥5.2% for commercial models against 21.7% for open-source models** — a four-fold gap between model *classes* rather than a capability gradient. Worth holding alongside this page's capability-convergence argument: on this particular safety-relevant behaviour, the classes had not converged as of the 2024–25 model vintage studied. See [[ai-generated-code-quality]].
