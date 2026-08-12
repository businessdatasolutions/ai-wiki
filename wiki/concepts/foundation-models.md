---
type: concept
aliases: ["foundation model", "foundation models", "FM", "frontier model", "frontier models"]
tags: [foundation-models, generative-ai, ai-research]
confidence: 0.87
last_confirmed: "2026-08-12"
accessed_at: "2026-08-12"
source_count: 21
quality_score: 0.95
quality_notes: ['1 near-empty section(s)', '2 broken body wikilink(s)']
---

# Foundation Models

Large pretrained models — typically transformer-based — that serve as the substrate for downstream AI applications via prompting, fine-tuning, or retrieval. Foundation models drive most modern [[generative-ai]] capability and are the locus of the "frontier" debate (capability, safety, transparency). In the [[software-3.0]] framing they are *the interpreter* — the runtime that executes context-window programs.

Their capability profile is **jagged** — see [[jagged-frontier]] for the task-level observation (Dell'Acqua et al. 2026) and the cause-of-jaggedness mechanism ([[Andrej Karpathy]] in [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Sequoia AI Ascent 2026]]: *"LLMs automate what you can verify"* — verifiability + labs-care editorial choices about RL training data combine to produce uneven peaks and valleys).

## Working definition

A **foundation model** is a model trained on broad data at scale that can be adapted to a wide range of downstream tasks. The term, coined by Stanford's [[Center for Research on Foundation Models]] (CRFM), foregrounds the *adaptation* role — the model is a foundation other things are built on, not the end product.

**Frontier model** is a near-synonym foregrounding *capability* (top of the leaderboard). The two terms diverge in policy/regulatory contexts: "frontier" often implies the regulator-relevant subset of foundation models above a capability threshold.

## Key claims

### Industry has decisively taken the frontier

- **~90% of notable AI models in 2024 came from industry** (vs. 60% in 2023); **91.18% in 2025** per the [[2026-04-30-ai-index-report-2026|AI Index 2026]] update. Academia remains the leading source of *highly cited* research, but not of new notable models.
- **2024**: U.S. 40 notable models, China 15, Europe 3.
- **2025** ([[2026-04-30-ai-index-report-2026|AI Index 2026]]): U.S. 59, China 35, South Korea 8, Europe 2.
- **Top organizations 2025**: OpenAI 20, Google 14, Alibaba 11, Anthropic 7, xAI 5, DeepSeek 4, LG AI Research 4, Meta 4, Tsinghua University 4 (only academic institution in the top 9), ByteDance / Moonshot / Nvidia 3 each.
- The U.S.-China **performance** gap has effectively closed: DeepSeek-R1 briefly matched the top U.S. model in Feb 2025; as of March 2026, Anthropic's top model leads by just **2.7%**.

### Compute is scaling fast

- Training compute for notable models doubles every **~5 months**.
- Dataset size for training LLMs doubles every **~8 months**.
- Power required for training doubles **annually**.
- **Global AI compute capacity reached 17.1M H100-equivalents** by 2025, growing **3.3× per year since 2022** ([[2026-04-30-ai-index-report-2026|AI Index 2026]] §1.2).
- **Nvidia: >60%** of total compute; Google + Amazon supply most of the remainder; Huawei holds small but growing share.
- **U.S. hosts 5,427 AI data centers** — more than 10× any other country.
- **TSMC** fabricates almost every leading AI chip; TSMC-U.S. expansion began operating in 2025.
- **AI data center power capacity: 29.6 GW** — comparable to New York state at peak demand.
- Carbon emissions trajectory:
  - AlexNet (2012): 0.01 tons
  - GPT-3 (2020): 588 tons
  - GPT-4 (2023): 5,184 tons
  - Llama 3.1 405B (2024): 8,930 tons
  - **Grok 4 (2025): 72,816 tons** ([[2026-04-30-ai-index-report-2026|AI Index 2026]])
  - (Reference: average American = 18 tons/year.)
- **Annual GPT-4o inference water use** alone may exceed the drinking water needs of **1.2 million people**.

### Disclosure is dropping ([[2026-04-30-ai-index-report-2026|AI Index 2026]])

- Training code, dataset sizes, parameter counts increasingly **withheld** for the most resource-intensive systems including those from OpenAI, Anthropic, Google.
- Reported parameter counts have stayed near **1 trillion for three years** as disclosure dropped — but training compute (estimable independently from hardware) has continued to rise.
- **OLMo 3.1 Think 32B** with ~90× fewer parameters than Grok 4 achieves comparable benchmark results via pruning, deduplication, curation alone — evidence that data quality and post-training matter as much as scale.

### Open-weight catching up to closed-weight

- Performance gap between top closed-weight and top open-weight models on the **Chatbot Arena Leaderboard**: **8.0% in early Jan 2024 → 1.7% by Feb 2025** on some benchmarks.
- The frontier is also tightening overall: **top-2 model gap = 0.7%, top-10 gap = 5.4%** (down from 4.9% / 11.9% the year before).

### U.S.-China performance gap narrowing fast

- End-2023 vs. end-2024 gaps on major benchmarks:
  - **MMLU**: 17.5pp → 0.3pp
  - **MMMU**: 13.5pp → 8.1pp
  - **MATH**: 24.3pp → 1.6pp
  - **HumanEval**: 31.6pp → 3.7pp

### Transparency improving

- **Foundation Model Transparency Index** (CRFM): avg score among major developers **37% (Oct 2023) → 58% (May 2024)**. Substantial progress, ~42% gap remaining. See [[responsible-ai]].

### Smaller is mighty

- **142× model-size reduction for the same MMLU >60% threshold** in two years: **PaLM (540B params, 2022) → Phi-3-mini (3.8B, 2024)**.

### Models converging to commodity status: the "rent vs own" framing ([[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]] + [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 2026]])

By April–May 2026, practitioner writing on [[agent-harness|agent harnesses]] had converged on a sharp framing of foundation models as **commercial inputs to differentiated products** rather than as the differentiator itself:

> *"Models are converging toward commodity status. They are rented from vendors whose competitors will outperform them within the year. They are swapped between, routed across, replaced quarterly. Two years ago, choosing a foundation model felt like choosing a database. Today it feels closer to choosing a CDN. The decision still matters, but the moat it produces lasts months, not years."* — [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]

The framing has three implications worth flagging:

1. **The CDN analogy** is sharper than prior wiki framings (database, library, API). It captures the *speed* of substitution: you do not architect a multi-quarter CDN selection process; you keep your stack CDN-agnostic and switch when the price/performance gradient justifies it.
2. **Layer-4-swappable architectures are now the practitioner default.** Kokane's harness diagram explicitly labels the model layer as "swappable backends" — Azure OpenAI/GPT-5, Claude (Anthropic), Gemini/Llama/Ollama, AWS Bedrock — selected at runtime. This is consistent with the open-weight performance gap closing trend documented above (1.7% on Chatbot Arena by Feb 2025).
3. **Where competitive advantage moves**: from model selection to the **harness layer** (memory architecture, quality contracts, learned per-customer overrides, telemetry). The "rent vs own" aphorism: *"The model is what you rent. The harness is what you own."* See [[agent-harness]] for the full treatment. As of [[2026-05-04-rethinking-agents-harness-is-all-you-need|May 2026]] this framing now has its first **empirical anchor**: an optimised harness from Khattab et al. (DSPy team) **transferred across five different foundation models** without re-optimisation, lifting all of them — turning *"plan for swap"* from a prudential design hint into a measured property of the harness layer.

**Caveat against over-commoditization narrative**: [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]] documented that Claude Sonnet 4.5's "context anxiety" failure mode was *absent* on Opus 4.5 — same family, different reliability. Within-family variation can be large enough that the "models converging" framing needs nuance: the *frontier* converges in benchmark performance, but *production-relevant reliability characteristics* (long-horizon stability, refusal behaviour, cost/latency curves) can vary substantially even between sibling models. The "plan for swap, not for marriage" prescription survives the caveat — but harness designers should expect to discover model-specific quirks at production scale and budget for them.

### The pricing scissors quantified ([[2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world|Brovich / AWS Sydney 2026]])

Brovich puts numbers on the commodity dynamic above: **training costs rising ~2.4× per year**, **inference costs falling ~10× per year**, so the gap — the "pricing scissors" — **opens by 12–24× per year**. Practical consequence: creating a frontier model approaches the *billions* (a handful of firms can), while *using* one collapses toward zero. This is the economic engine behind the USE/COMPOSE/BUILD decision ([[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|already on the Allen page]]) — *build* is justified only where differentiation outweighs the collapsing cost of *compose*. A second AWS strategist independently delivering the same framework strengthens the wiki's read that "rent the model, own the harness" is settled vendor doctrine, not one strategist's pitch.

### Cross-model deliverable comparison on real work ([[2025-10-05-patwardhan-et-al-openai-gdpval|GDPval, OpenAI 2025]])

GDPval supplies a rare *head-to-head, deliverable-quality* comparison across frontier families on real economic tasks (not academic benchmarks). On the gold subset, **Claude Opus 4.1 was the best** of GPT-4o / o4-mini / o3 / GPT-5 / Claude Opus 4.1 / Gemini 2.5 Pro / Grok 4, with **47.6% wins-or-ties** vs human experts. The model *personalities* are the load-bearing detail for the commodity-vs-differentiated debate above: **Claude excels at aesthetics and file formats** (`.pdf`/`.xlsx`/`.ppt`), **GPT-5 excels at accuracy and instruction-following**; Gemini and Grok most often failed by not delivering or using the wrong format. So even as raw benchmark scores converge, models retain *distinct deliverable profiles* — a reason the "swap freely" framing needs the same nuance the within-family caveat raises. GDPval also confirms performance is improving **roughly linearly over time**, consistent with the frontier-keeps-moving picture.

## Notable foundation model series (mentioned via [[2026-04-28-ai-index-report-2025|AI Index 2025]])

To be promoted to standalone entity pages when discussed in depth in another source. Currently noted here as a roster:

- **OpenAI**: GPT-4, GPT-4o, **o1**, o3 (test-time compute reasoning), **SORA** (video).
- **Google DeepMind**: Gemini family (Gemini-1.5-Flash-8B is the 280×-cost-reduction marker), Veo 2 (video).
- **Anthropic**: Claude 3 family (incl. Sonnet — implicit-bias study); [[Claude Sonnet 4.5]] (predominant model in AEI 4 sample, exhibits "context anxiety" per [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Managed Agents post]]); **Claude Opus 4.5** (released between AEI 4 and AEI 5 windows; the Managed Agents post notes the "context anxiety" failure mode is *absent* on Opus 4.5 — first evidence in this wiki of long-horizon reliability varying by model **within** a family, not just across families); **Claude Opus 4.6** (released coincident with AEI 5 sample window, Feb 2026).
- **Meta**: Llama 3.1 405B (the 8,930-ton-CO2 marker), Movie Gen (video).
- **Microsoft**: Phi-3-mini (the 3.8B-param-MMLU marker).
- **Mistral AI**: French open-source.
- **xAI**: Grok family.

## The *commodity-utility, not platform* value-capture thesis ([[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Evans / Lenny's Podcast May 2026]])

[[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Evans (May 2026)]] poses the wiki's most direct independent-analyst-altitude challenge to the *foundation-models-as-the-value-capture-layer* presumption:

> *"The models don't seem to have network effects. So there doesn't seem to be a winner-takes-all effect where one of these will run away ahead of the others. So you should have competition indefinitely. You have competition indefinitely. You don't have really radical differentiation in what the product is. Then why would you have pricing power?"*

The structural analogy: foundation models look more like **AWS than Windows** — every developer doesn't have to standardise on one because the customers don't care which one runs underneath. *"If you're an engineering company or a law firm buying a piece of software, you don't care which cloud it runs on and you don't have to standardize on AWS because that's where all the software is and like the developers all standardize on AWS because all the customers use AWS. That's not how it works. That's how Windows OS works, but that's not how AWS works."*

Sam Altman's *"AI on a meter like water or electricity"* line gets Evans's response: *"my dear sweet child, you need me to explain the margin structure of the utility industry to you ... when you watch television the TV company isn't paying a percentage of your monthly bill to the electricity company, you know, when you wash your clothes, Bosch isn't paying a percentage of the price of the washing machine."*

The telecom worked example Evans offers as the precedent: *"Global mobile industry has revenue of about a trillion dollars a year, maybe a bit more now. And it spends about $200 billion a year on capex every year. Total telecoms is about 300 ... if you look at a chart of mobile data consumption, it's an exponential curve like perfect curve going straight up. And then the number now I think it's about 1500 to 2000 times what it was in 2010 globally. And the stocks have gone nowhere in 25 years because it's an X-growth low-margin commodity utility."*

The structural implication Evans names: *"What is the steady state equilibrium point where all of these lines on the chart kind of get lined up and we don't have this kind of weird crazy stuff going on, and then will you have pricing power or have you got like three or four or five companies kind of all selling the same thing — and so then you should have a pricing — you should have lower pricing and lower margins and the value got — stack."*

The under-asked question Evans poses (in response to *"what's a question about AI that nobody's asking?"*): *"I'm not sure how many people are asking whether model labs have pricing power. I think a lot of people are just presuming that the situation today will continue or that of course they will."*

The thesis sits in productive tension with *foundation-models-as-the-platform* readings ([[2026-04-26-how-to-win-when-software-is-not-a-moat-evan-spiegel-snapchat-ceo|Spiegel's software-is-not-a-moat]] makes the same argument from the application-layer side at a different altitude; the [[agent-harness]] concept's *"harness wraps a (rented, swappable) foundation model"* framing is structurally compatible — *the model is the commodity, the harness is the differentiated layer*). The pricing-power-or-not question is genuinely open in 2026; Evans is the wiki's first explicit *no-they-won't-have-pricing-power* voice at independent-analyst altitude.

## The *beneath-vs-above-the-model* + open-source-substitution buyer view ([[2026-06-18-ramaswamy-mckinsey-every-company-software-company|Ramaswamy / Snowflake 2026]])

[[2026-06-18-ramaswamy-mckinsey-every-company-software-company|Ramaswamy]] (CEO, Snowflake — a major *buyer* and *host* of foundation models) corroborates the commodity-pressure thesis from the platform-vendor chair: **open-source models are "getting better and better,"** Snowflake hosts them alongside the frontier models, and *"if they're as good, our customers will want to use them instead of the frontier model."* He frames the open strategic question as **what stays "beneath the model" vs "above the model"** — will disruption land on the layer close to end-users, or at a lower layer? This is the same *the-model-is-the-swappable-commodity, the differentiated value is elsewhere* structure as Evans's commodity-utility thesis and the [[agent-harness]] *rented-model* framing, now stated as a procurement reality (a buyer that will switch to open weights the moment they reach parity). It also pairs with the [[2026-06-17-ng-langchain-interrupt-future-of-ai-agents|Ng]] *optionality* discipline — both treat model choice as fluid and lock-in as a liability.

## The open-weight-at-scale switch, and China's open-model lead ([[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|Delangue / Hugging Face, July 2026]])

[[2026-07-10-hugging-face-ceo-companies-done-renting-their-ai|Delangue]] ([[Hugging Face]] CEO — host of nearly 3 million public open-weight models) turns the commodity-substitution thesis above into an operational adoption pattern: enterprises **start on frontier APIs, then switch to open-weight models at production scale** as frontier cost bites — the demand-side cost curve behind Ramaswamy's "if they're as good, customers will use them instead." He adds two data points the wiki's foundation-model material otherwise lacks: (a) the **open-weight-vs-closed capability gap is narrow** (echoing [[2026-07-08-jensen-huang-why-companies-need-open-agent-systems|Huang's]] Nemotron 3 Ultra 86% vs. Claude Opus 87% at ~10× lower cost); (b) per Hugging Face's Spring 2026 report, **Chinese models are ~41% of downloads** — the plurality, surpassing the US — with named open families (**GLM 5.2**, **Nemotron**, OpenAI's open GPT) as the off-the-shelf starting points teams then post-train. The full own-vs-rent / sovereignty / concentration-of-power treatment lives on the new [[open-source-ai]] concept; here it sharpens the *"open-weight closing the gap"* debate bullet below into a dated, quantified corpus datapoint.

## The scaling story told from inside a Stanford course — including where it stopped ([[2026-08-03-chowdhery-mirhoseini-stanford-cs329a-self-improving-agents-part-1|Chowdhery & Mirhoseini / CS329A, August 2026]])

A compact instructional account of the three scaling axes (compute, dataset size, parameter count), with the trajectory given concretely — **BERT 340M → GPT-2 1.5B → GPT-3 175B → PaLM 540B → GPT-4 "estimated… trillions"** — and, notably, a stated end point: this held "**until last year, where this was starting to hit some kind of a saturation point.**" (Delivered September 2025.)

Two capabilities are named as what scale bought: **few-shot and zero-shot learning** — "earlier you had to fine-tune the model for [a] specific domain, but just by giving a few examples the model can follow that template" — and **emergent behaviour**, where "capabilities like reasoning only emerge in larger models." Mirhoseini's framing of why emergence matters epistemically is the part worth keeping: beyond "predictable scaling laws… **there are new behaviours that appear in the model that they didn't have before, and we never could predict that until we had these bigger models.**" Chain of thought is the canonical case — LaMDA and GPT at ~7–8B "can't really benefit from chain of thought, it doesn't do anything for them" — with modular arithmetic and word-unscrambling appearing abruptly at scale.

The lecture is also unusually clear that **ChatGPT's advantage over GPT-3 was post-training, not size**: high-quality fine-tuning data ("data that companies pay millions, or hundreds of millions of dollars, to buy"), **instruction tuning**, and **RLHF**, where "instead of just creating some supervised prompt and labels, we are creating a **reward model** out of human preferences," with reward types weighted per objective (correctness, helpfulness, specificity, harmlessness). Their own verdict on alignment is worth recording verbatim: "we try to steer the AI models to follow the goals and preferences and values of humans. And **this is still a big problem. It's a big issue. We haven't mastered it yet.**"

**The pivot the course is built on**: "pre-training and then fine-tuning were the big pieces. But since a year and a half ago, **it turns out inference is also a frontier for making the models much more capable**" — with the self-improvement loop closing when test-time-scaled generations become training data for the next fine-tune. Per [Lifecycle rules](../../CLAUDE.md#lifecycle) confidence lifts only 0.85 → 0.87: this is instructional synthesis of published results rather than new evidence, and the eleven-month publication lag makes its state-of-the-art claims dated.

## Debates and supersession

- **"Frontier" vs. "foundation" framing.** "Frontier" emphasizes capability gap; "foundation" emphasizes adaptation role. Different policy/regulation implications — frontier-model bills target capability thresholds; foundation-model bills target the broader pretraining-then-adapt pattern.
- **Compute-scaling sustainability.** Data-commons shrinkage (see [[responsible-ai]]) plus rising energy demands (driving nuclear-energy partnerships — Microsoft's Three Mile Island, Google's SMRs, Amazon's SMRs) raise structural questions about the 5-month-compute-doubling trajectory continuing.
- **Open-weight closing the gap.** As open-weight performance catches closed-weight, the policy logic for restricting model release weakens — but so does the commercial moat for closed-weight providers. Open question how 2025–2026 plays out.
- **Pricing power yes-or-no.** [[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Evans (May 2026)]] argues no (commodity-utility, AWS-not-Windows analogy); Sam Altman's *AI-on-a-meter* line presumes yes. The wiki has no settled position; the question is one of the load-bearing open questions of 2026 model-economics.

## Related concepts

- [[generative-ai]] — the dominant *use* of foundation models today
- [[ai-benchmarks]] — how foundation-model capabilities are evaluated
- [[responsible-ai]] — the transparency, safety, and governance overlay
- [[enterprise-ai-adoption]] — the deployment context

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "foundation-models") OR contains(tags, "frontier-models")
SORT file.name ASC
```
