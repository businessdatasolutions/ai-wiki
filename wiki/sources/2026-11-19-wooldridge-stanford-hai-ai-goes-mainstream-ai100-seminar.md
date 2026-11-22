---
type: source
kind: video
title: "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI"
author: ["Stanford HAI"]
publisher: "Stanford HAI (YouTube channel); seminar recorded 18 November 2026 at Stanford, moderated by Russ Altman (AI100 faculty director), with Michael Wooldridge (AI100 2026 Study Panel chair, University of Oxford) presenting remotely from Oxford"
url: "https://www.youtube.com/watch?v=WGjuvTvz90U"
date_published: 2026-11-19
date_ingested: 2026-11-22
length: "~59:06 minutes (transcript ~452 lines + 13 stills; ASR auto-generated track, no chapters; talk only, the Q&A is not in the recording)"
raw: "../../raw/videos/ai-goes-mainstream-the-scaling-era-and-the-rise-of-generative-ai.md"
stills: "../../raw/videos/ai-goes-mainstream-the-scaling-era-and-the-rise-of-generative-ai.stills.md"
tags: [stanford-hai, ai100, michael-wooldridge, russ-altman, seminar, scaling-era, scaling-laws, bitter-lesson, nvidia, data-centers, data-center-backlash, copyright, sovereign-ai, undersea-cables, helium, export-controls, open-weight-models, us-china, cybersecurity, software-development, mathematics, ai-for-science, white-collar-work, ai-governance, science-technology]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-sensing/digital-scenario-planning
  - contextual/external-triggers
  - digital-seizing/balancing-digital-portfolios
relationships:
  - type: depends-on
    target: 2026-11-10-ai100-ai-goes-mainstream-2026
    via: "the panel chair presenting his own report a week after release; eight of its twelve takeaways appear as slides in near-verbatim wording, and both deep dives are condensed. Same author restating the report, so not independent support. The talk adds Wooldridge's personal views, which the report deliberately leaves out, and a few figures that are not in the report"
    confidence: 0.85
  - type: contradicts
    target: 2026-09-18-bloomberg-originals-how-china-plans-to-win-global-ai-race
    via: "Wooldridge expects Europe, North America and like-minded countries to 'focus around US-led AI' while China becomes the AI provider for 'the rest of the world'; Bloomberg reports OpenRouter data in which Germany and the US already used more Chinese than US models by June 2026. OpenRouter counts developer API traffic, not national adoption, so the conflict is real but narrow"
    confidence: 0.5
---

# Stanford HAI seminar: Michael Wooldridge on the AI100 2026 report

> This talk unpacks key insights from the third AI100 report, "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI," released in November 2026. Commissioned by the AI100 standing committee and led by study panel chair Michael Wooldridge, the report documents what it calls the "scaling era" – the pivotal five years that reshaped how the world works with AI.
>
> In this talk, you'll explore the report's findings across twelve standing questions and two deep dives, including:
> • Advances in reasoning models and agentic systems
> • The geopolitics of compute and data
> • The contested evidence on AI's effects on work
>
> The talk closes by revisiting the 2021 panel's predictions: asking why even the field's own insiders underestimated how far scaling the transformer would go, and what that reveals about our ability to forecast what comes next.
>
> Recorded November 18, 2026 at Stanford University.
>
> *— Channel description, Stanford HAI* (the "About AI100" paragraph that follows it is omitted)

## TL;DR

A 59-minute seminar on the [[Stanford HAI]] channel. Russ Altman, the faculty director of [[AI100]], introduces it in the room (0:00–4:00). [[Michael Wooldridge]], who chaired the study panel, then presents [[2026-11-10-ai100-ai-goes-mainstream-2026|the AI100 2026 report]] over Zoom from Oxford (4:05–58:52). The report's own page links this video as "the Seminar on the 2026 Report's Findings." **Auto-generated transcript, ASR-cleaned at acquire**, proper nouns only: "Russ Alman" → Altman, "Michael Waldridge" → Wooldridge, "Sheila Marith/Mackraith" → McIlraith, "Jensen Hong" → Jensen Huang, "McCullik and Pittz" → McCulloch and Pitts, "Quen … Kimmy" → Qwen, Kimi, "states of Hormuz" → Strait of Hormuz. The Q&A announced at the start is not in the recording.

The description promises the 2021 retrospective and the evidence on work, but the talk gives little of either. The 2021 report gets one passage (24:43–25:27: it *"correctly predicted that AI was going to be transformative"*, but not how). Jobs come up only in the software-developer passage, the public's lack of say and Wooldridge's personal aside, never through the studies. The talk ends after the geopolitics deep dive; the report's Five Years On section and its labour evidence are only on the [[2026-11-10-ai100-ai-goes-mainstream-2026|report page]].

What it adds to the report:

1. **Wooldridge's personal views, labelled as his own.** The report avoided these on purpose.
   - He doubts large-scale white-collar displacement.
   - His chief worry is AI used to attack poorly secured infrastructure.
   - He expects the world to split into US-led AI and China-provided AI.
2. **Figures that are not in the report:** Nvidia at about $5.25 trillion on 28 October 2026, and data-centre water use of *"up to 5M gallons/day"*. The rest of the slide figures are the report's own.
3. **What the talk leaves out.** It shows eight takeaways and skips four: military AI, synthetic media as evidence, science-fiction risks, and frontier concentration (which reappears in the deep dive). Military AI and deepfakes do not come up at all.
4. **A news hook the report could not have.** The talk opens on *"the Nvidia scandal"*, a story about Nvidia's CEO that broke as the report came out. Wooldridge uses it to argue that only the scaling era explains why a CEO's private life became a geopolitical question. The talk never says what the story is.

## The frame (4:48–13:03)

*"The private life of a CEO of a sausage company would be unlikely to make the front pages of the world's newspapers"* (5:32). The Nvidia story became an international issue, Wooldridge says, because AI went from *"something which was widely discussed to something which was at the top of governmental agendas internationally"* (6:18), alongside conflicts and the pandemic. The answer *"is in our report"*: the scaling era (still 1).

On AI100 itself: Altman calls this *"the third or fourth report depending on how you count"* (2:13). Wooldridge calls the project *"extraordinarily visionary … I think unprecedented in technological history"* (7:20). He notes that impartiality is hard to assemble *"because so much of AI is going on behind the closed doors of the private sector"* (8:12). The panel met in Singapore (February) and Oxford (April) and delivered a first draft at the beginning of May 2026. *"Every time we thought we'd finished, events kept happening"* (10:05). He wonders whether the Horvitzes *"thought when they endowed this that AI would be where it is in 2026"* (11:59).

## The scaling era (13:03–24:10)

The history is told at length: McCulloch and Pitts, Geoff Hinton's 1980s work, deep learning around 2005, the 2012 discovery that GPUs, *"invented … so that teenagers could have realistic renditions"* of computer games, give 10× *"bang for your buck"*, and the 2017 transformer, which OpenAI scaled *"on a scale that seemed impossible to imagine"* (still 2). Even OpenAI's former executives *"have admitted that they did not anticipate the extraordinary success"* of ChatGPT (20:50).

On scaling laws: *"as an AI scientist, I have to say I find scaling laws kind of embarrassing"* (22:19), because they say capability comes reliably from size. What they give Silicon Valley is *"a simple reliably low-risk investment rule. The scaling era: build it bigger"* (23:05). Rich Sutton's bitter lesson is cited as the field's own version (still 3).

## The takeaways as he tells them (24:10–43:49)

- **Disruption.** Software development is *"thoroughly disrupted"*. Two years overturned the belief that *"software engineers imagined that they had a safe job for life"* (27:38). His reading: *"It's going to value not the brick layers but the architects"* (28:24). Creative day jobs such as restaurant copy are going, and *"everywhere I look I'm seeing AI generated text and AI generated images"* at the Oxford food markets. On mathematics he goes further than the report: mathematicians told him at the start of summer 2026 that their field was immune, and since then AI has solved *"some of the most complex problems … the millennium prize problems"*. He adds that *"the exponential time hypothesis was not just solved but solved in a way that people did not expect at all"* (30:55). The report has one contested Millennium Prize claim and does not mention the exponential time hypothesis.
- **Science.** AlphaFold turns months into less than a day. *"Fully authenticated pieces of completely AI generated science"* now appear in human peer-reviewed literature (34:00).
- **Capital.** *"If you factor out the incredible capital investment particularly in data centers, this is what's propping up the US economy"* (34:43). *"It isn't clear at the moment whether is a bubble bursting or just a modest correction in the markets"* (35:03).
- **Cybersecurity.** The summer's incidents *"were not AI programs going rogue … the AI is weaponized"*, and experts told him the attacks were *"fairly mundane"*. His personal view (36:49): *"if I had to characterize my risk about major harms that could be done by AI, it would be that AI was used to attack a poorly secured piece of infrastructure,"* with air-traffic-control failures as the model.
- **The public.** If AI is *"as consequential as fire or electricity"*, as industry leaders say, *"why aren't the public having more say in it?"* (38:47).
- **Geopolitics and governance.** Safety talk after ChatGPT has *"shifted in focus"* to national security, and *"the fledgling … legislation … has in many cases dissolved or been put on the back burner"* (41:16).
- **Pace, and a personal aside on work (42:19).** If the pace continues, *"the world is going to be utterly transformed within the next 5 years."* Then, *"speaking personally, not as the report"*: whether AI tools displace large numbers of white-collar workers *"still seems rather doubtful to me,"* though they will change the work. Knowledge-intensive R&D is where he expects the most change.

## The two deep dives (43:49–58:52)

**Scaling** (stills 4–9):
- A frontier model costs *"half a billion dollars"* and *"has a lifespan of what 6 months, nine months, a year"* (45:29).
- *"15% of the 2025 growth in the US stock market is from gains in Nvidia alone … I didn't believe that statistic, but I went and checked it"* (46:17). Nvidia *"has now gone down a bit"*.
- GPT-3's electricity bill alone was *"greater than the total value of all of the research projects that I've ever had funded"* (47:41).
- The *"physical world manifestation of AI"* line comes from *"a beautiful quote, I momentarily forget who"*. The report attributes it to Alondra Nelson (p. 62).
- On copyright he speaks *"as an author who's published books, and I know some of my books were in those … data, I'm not happy about that"* (50:05).
- Whether scaling continues: *"We were somewhat divided on this"* (51:28).

**Geopolitics** (stills 10–13):
- Sovereign AI means controlling the whole stack: *"Who are the two nations that can definitively do it? The US and China"* (54:35).
- For the UK, *"we have the most expensive energy in the developed world"* and *"everybody objects to building of data centers"* (54:13).
- He adds a link the slide does not show: most of the world's helium *"passes through the Strait of Hormuz"*, *"an international conflict having knock-on consequences for the AI race"* (55:10).
- **The closing forecast (57:43), his own:**

> *"I think we're heading to a world where frontier AI is controlled largely by the US with its very capable, very large scale closed weight models and by China pioneering its way in these open-weight models. And where it looks from where I'm sitting is, you know, Europe and North America and a few other like-minded countries around the world will focus around US-led AI. For the rest of the world, the AI provider is likely to be China."*

That forecast conflicts with recent usage data. [[2026-09-18-bloomberg-originals-how-china-plans-to-win-global-ai-race|Bloomberg's documentary]] reports OpenRouter figures in which Germany and the US already used more Chinese than US models by June 2026. OpenRouter counts developer API traffic, not national adoption, so the two may measure different things.

## Takeaway slides against the report

The eight takeaway slides (deck slides 12–19) are not published; their verified wording is in the manifest. Four are the report's own sentences verbatim (KT 4, 6, 11 and the core of 3). Two compress a takeaway into a headline and a subtitle (KT 2 and 9). One, *"AI has become a geopolitical issue,"* has no takeaway of its own in the report. The last restates KT 12 in a third wording: *"If the current pace is sustained, the world will be very different in 5 years."*

| Report takeaway | In the talk |
| --- | --- |
| 1 Scaling under pressure | Deep dive (still 9) |
| 2 Disruption | Slide (25:30) |
| 3 Science | Slide (31:50) |
| 4 Capital investment | Slide (34:20) and deep dive |
| 5 Concentration in US and China | Deep dive (stills 6, 10, 13) |
| 6 Cybersecurity | Slide (35:45) |
| 7 Military AI | Absent |
| 8 Synthetic media as evidence | Absent |
| 9 Public has little say | Slide (37:30) |
| 10 Sci-fi risks emerging | Absent (sandbox escapes come up only as "not rogue") |
| 11 Governance fragmented | Slide (40:05) |
| 12 Pace | Slide (42:15) |

## Visual canon

Thirteen of the deck's 34 slide windows, chosen by hand: Gemini returned HTTP 402, so the frames were sampled every 5 seconds and checked every 2 (see the manifest). Navigation slides, the title and the eight takeaway slides are left out.

### 1 · Why the Nvidia story became global

![[assets/2026-11-19-wooldridge-stanford-hai-ai-goes-mainstream-ai100-seminar/02-07m05-why-did-this-become-a-topic-of-global-concern.webp|Why did this become a topic of global concern]]

*Still at [5:00](https://www.youtube.com/watch?v=WGjuvTvz90U&t=300s) from Stanford HAI, "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI".*

Title: **Why did this become a topic of global concern?** A clipped screenshot from The Verge: *"The Nvidia scandal isn't slowing down."* The overlay box:

> To understand why, you need to read our report.
> We are living through the **scaling era of AI**, in which **AI became a geopolitical issue**.
> Our report gives you the context to understand what's happening in AI right now, and why AI is now at the top of international government agenda.

*Still vs. transcript:* the narration never names the outlet or quotes the headline. The box puts the talk's thesis in one sentence, which the report spreads across its introduction.

### 2 · The scaling era in six dates

![[assets/2026-11-19-wooldridge-stanford-hai-ai-goes-mainstream-ai100-seminar/07-21m55-the-scaling-era.webp|The scaling era, key developments in neural nets]]

*Still at [13:40](https://www.youtube.com/watch?v=WGjuvTvz90U&t=820s) from Stanford HAI, "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI".*

**The scaling era.** The current AI boom rests upon one technology: **neural nets**. Key developments in neural nets:

| When | What |
| --- | --- |
| 1940s | the original idea |
| 1980s | Hinton et al figure out the key science and algorithms |
| 2005ish | big data and big compute start to make useful neural nets viable |
| 2012 | GPUs for building neural nets supercharges the field |
| 2017 | **transformer architecture** for LLMs invented by Google |

**Transformer + (Compute & Data on an unprecedented scale) gives:** 2022: ChatGPT. 2023-26: "Code Red" in Silicon Valley.

*Still vs. transcript:* the narration takes eight minutes over this history. The slide reduces it to an equation, transformer plus compute and data at scale, and dates "Code Red" to the whole of 2023–26 rather than to Google's December 2022 alarm in the report.

### 3 · Scaling laws as an investment rule

![[assets/2026-11-19-wooldridge-stanford-hai-ai-goes-mainstream-ai100-seminar/09-24m10-scaling-laws.webp|Scaling laws, more data and compute give better AI]]

*Still at [22:05](https://www.youtube.com/watch?v=WGjuvTvz90U&t=1325s) from Stanford HAI, "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI".*

**Scaling Laws: More Data+Compute ➔ Better AI.**
- **Empirical scaling laws**: *performance improves predictably with more parameters, compute, and data*.
- In other words: "scale the recipe up and you'll get better AI".
- a **simple**, **reliable**, **low-risk investment** rule that drove **massive** capital flows, and largely accounts for many aspects of current AI market
- Key discovery in 2012: **Graphics Processing Units (GPUs)** perfect for training ML; 10x more bang for your $
- GPUs enabled entirely new classes of ML/AI systems, including **generative AI**

*Still vs. transcript:* the spoken version is close. The slide adds that the rule *"largely accounts for many aspects of current AI market"*, and its quotation, *"scale the recipe up"*, is Sutskever's, as the report attributes it (p. 107).

### 4 · Scaling has defined the last five years

![[assets/2026-11-19-wooldridge-stanford-hai-ai-goes-mainstream-ai100-seminar/20-46m05-scaling-has-defined-the-last-five-years.webp|Scaling has defined the last five years]]

*Still at [44:10](https://www.youtube.com/watch?v=WGjuvTvz90U&t=2650s) from Stanford HAI, "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI".*

| Figure | Meaning |
| --- | --- |
| ~100M | monthly ChatGPT users within two months of its November 2022 launch |
| $500M | per frontier training run in 2026, versus about $5M to develop a frontier model in 2021 |
| 5× | yearly growth in compute used to train frontier language models since 2020 |

Sources: UBS/Similarweb estimates (Feb. 2023) for ChatGPT users; Epoch AI for frontier training compute.

*Still vs. transcript:* the narration gives the $500M but not the 2021 comparison, and names no sources. The 2021 figure is the one that makes the scale visible: a hundredfold rise in five years.

### 5 · The scale of investment

![[assets/2026-11-19-wooldridge-stanford-hai-ai-goes-mainstream-ai100-seminar/21-47m00-the-scale-of-investment-is-unprecedented.webp|The Scale of Investment is Unprecedented]]

*Still at [46:10](https://www.youtube.com/watch?v=WGjuvTvz90U&t=2770s) from Stanford HAI, "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI".*

| Figure | Meaning |
| --- | --- |
| $5T | Nvidia market value in October 2025, the largest company in history |
| ~3× | today's AI data center buildout versus the late-1990s boom, inflation-adjusted |
| 15%+ | share of 2025 U.S. stock market gains from Nvidia alone |
| $6.7T | further data center investment estimated if current demand continues |

*Yet the economic impact is not yet visible in aggregate macro data or company returns. AI is not yet paying its way.*

*Still vs. transcript:* Wooldridge says *"6 trillion"*, and never says aloud either the comparison with the late-1990s boom or the slide's last line, *"AI is not yet paying its way."* That line is Key Takeaway 4 of the report.

### 6 · Concentration and its consequence

![[assets/2026-11-19-wooldridge-stanford-hai-ai-goes-mainstream-ai100-seminar/22-48m15-concentration-and-its-consequence.webp|The Race to Scale, concentration and its consequence]]

*Still at [47:05](https://www.youtube.com/watch?v=WGjuvTvz90U&t=2825s) from Stanford HAI, "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI".*

**The Race to Scale: Concentration and its Consequence.**
- GPT-3 required **20,000+ GPUs (each with capital cost ~ $30k)** running for months. Capital costs beyond the reach of all but the wealthiest universities; energy costs in $millions.
- ➔ **Frontier development became concentrated in Silicon Valley** ⬅
- NVIDIA market cap (28 Oct 26): **~ $5.25 trillion**
- **Nvidia is worth more than the annual GDP of every country in the world except the US & China**: the largest in history, **solely because they build the GPUs of choice**
- Staggering capital investment in data centers to provide compute resources
- Who can do this? Tiny number of private sector companies & two nation states.

*Still vs. transcript:* the dated market cap, $5.25 trillion on 28 October 2026, is in neither the narration nor the report, which stops at October 2025. Spoken, the GPU cost is *"between 20 and $50,000"*; the slide says about $30k.

### 7 · Data-centre pushback

![[assets/2026-11-19-wooldridge-stanford-hai-ai-goes-mainstream-ai100-seminar/23-49m35-data-center-pushback.webp|The Race to Scale, data center pushback]]

*Still at [48:20](https://www.youtube.com/watch?v=WGjuvTvz90U&t=2900s) from Stanford HAI, "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI".*

**The Race to Scale: Data Center Pushback.** Inset: a newspaper feature, *"Big, noisy and coming to a town near you - why the data centre backlash is growing"* (October 2026; the date line is too small to read with confidence).
- Data centers are the gasoline that powers modern AI
- Generative AI at scale only possible because of vast data centers
- But data center development increasingly faces pushback: *energy costs, CO₂ emissions, water use (up to 5M gallons/day), financial sustainability*

*Data centers are the physical world manifestation of AI: they provide something tangible to push back on.*

*Still vs. transcript:* the water figure, up to 5 million gallons a day, is not spoken and not in the report. The report frames water differently: about 0.1% of U.S. water, a fifth of what golf courses use (p. 101). The closing line is the quote Wooldridge cannot attribute aloud; the report credits it to Alondra Nelson.

### 8 · The data race

![[assets/2026-11-19-wooldridge-stanford-hai-ai-goes-mainstream-ai100-seminar/24-51m20-the-data-race.webp|The Race to Scale, the data race]]

*Still at [49:40](https://www.youtube.com/watch?v=WGjuvTvz90U&t=2980s) from Stanford HAI, "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI".*

**The Race to Scale: The Data Race.**
- Huge neural nets require correspondingly huge amounts of data: GPT-3 trained on ~45 terabytes of text
- Virtually the entire accessible web scraped — raising widespread copyright concerns
- US courts (2025) suggested AI training may constitute **fair use**; Anthropic settled **pirated books case** for $1.5B — largest copyright settlement in history
- **Responses to data scarcity**: **Synthetic data**; **Physical AI & robotics**; **Data quality over quantity**

*Still vs. transcript:* the narration hedges the legal point, *"I don't claim to be a copyright lawyer,"* and does not call the settlement the largest in history. The slide states both, as the report does.

### 9 · The scaling paradigm under pressure

![[assets/2026-11-19-wooldridge-stanford-hai-ai-goes-mainstream-ai100-seminar/25-52m10-the-scaling-paradigm-is-under-pressure.webp|The scaling paradigm is under pressure]]

*Still at [51:25](https://www.youtube.com/watch?v=WGjuvTvz90U&t=3085s) from Stanford HAI, "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI".*

| The scaling recipe | The next phase |
| --- | --- |
| More compute and more data gave predictable gains | Smarter algorithms and smaller models rebuilt less often |
| Capabilities have doubled every three to six months | Better context and memory |
| A frontier model uses tens of trillions of tokens and 100,000+ GPUs for months | More reasoning time at inference |
| | Tools and agents for complex tasks |

Source: Kaplan et al. (2020), scaling laws for neural language models, arXiv:2001.08361.

*Still vs. transcript:* the narration gives the right-hand column, close to word for word. The left-hand figures (doubling every three to six months, tens of trillions of tokens, 100,000+ GPUs) are only on the slide. The slide also leaves out the disagreement the narration admits: *"We were somewhat divided on this."*

### 10 · Sovereign AI means the whole stack

![[assets/2026-11-19-wooldridge-stanford-hai-ai-goes-mainstream-ai100-seminar/27-54m35-the-emergence-of-sovereign-ai.webp|Geopolitics, the emergence of sovereign AI]]

*Still at [52:25](https://www.youtube.com/watch?v=WGjuvTvz90U&t=3145s) from Stanford HAI, "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI".*

**Geopolitics: The Emergence of Sovereign AI.** Nations now seeking **sovereign AI**. Sovereign AI = **you control the whole AI stack**:
- Human skills (high level AI expertise) at scale
- Data at scale
- Access to frontier semiconductors at scale
- Secure data pipelines (networks, undersea cables)
- Low energy costs
- Ability to build and deploy physical data centers (the slide reads "centersa")

Who can do this? USA. China.

*Still vs. transcript:* this six-part stack is the talk's own condensation. The report defines sovereignty as developing, deploying and governing AI *"via their own infrastructure, data, models, and expertise"* (p. 13), and does not reduce the answer to two countries. The narration adds the UK's case: the most expensive energy in the developed world, and planning objections.

### 11 · Chips, minerals and energy

![[assets/2026-11-19-wooldridge-stanford-hai-ai-goes-mainstream-ai100-seminar/28-55m35-chips-minerals-and-energy.webp|Geopolitics, chips, minerals and energy]]

*Still at [54:40](https://www.youtube.com/watch?v=WGjuvTvz90U&t=3280s) from Stanford HAI, "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI".*

**Geopolitics: Chips, Minerals, & Energy.**
- **Semiconductors**: Advanced chip manufacturing centred in geopolitical flashpoints; Export controls on AI chips already a source of international dispute
- **Raw Materials**: Rare earth metals and helium critical for chip production; Supply chain integrity risks
- **Energy**: Frontier training and inference consume electricity at the scale of towns; Gulf states (UAE, Saudi Arabia), Nordics, and North America competing

*Still vs. transcript:* the narration names the flashpoint for helium, the Strait of Hormuz, which the slide and the report do not. The slide says "towns" where the report says *"small cities"* (p. 100).

### 12 · Regulation, and the open question

![[assets/2026-11-19-wooldridge-stanford-hai-ai-goes-mainstream-ai100-seminar/29-56m25-regulation.webp|Geopolitics, regulation]]

*Still at [55:40](https://www.youtube.com/watch?v=WGjuvTvz90U&t=3340s) from Stanford HAI, "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI".*

**Geopolitics: Regulation?**
- EU AI Act (2024): first comprehensive binding regulation of AI worldwide
- UK AI Safety/Security Summit process: Bletchley Park 2023 → Seoul 2024 → Paris 2025; growing network of national institutes
- UN Convention on Certain Conventional Weapons: LAWS discussions since 2014; draft legal instrument expected end 2026
- Council of Europe Framework Convention on AI; G7 Hiroshima AI Process; UN Global Digital Compact
- Global Commission on Responsible AI in the Military Domain (REAIM)

**Central open question: will these cohere into a durable regime, fragment geopolitically, or be captured by the most advanced AI states?**

*Still vs. transcript:* the narration covers half the list. It does not say the open question aloud, and adds that the EU AI Act *"struggled to keep up with developments"* and that some governments actively push back for fear of stifling innovation. The summit chain on the slide stops at Paris 2025; the report continues to India 2026 and Switzerland 2027.

### 13 · Closed versus open, US versus China

![[assets/2026-11-19-wooldridge-stanford-hai-ai-goes-mainstream-ai100-seminar/30-57m40-closed-vs-open-us-vs-china.webp|Geopolitics, closed vs open, US vs China]]

*Still at [56:30](https://www.youtube.com/watch?v=WGjuvTvz90U&t=3390s) from Stanford HAI, "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI".*

**Geopolitics: Closed vs Open; US vs China.**
- USA dominates in development of very large, powerful, general purpose models: OpenAI, Anthropic, Google, …; Dominate the top of league tables; Private sector; Closed models
- China has forged a distinctive path in **open weight *models***: DeepSeek, Qwen, Kimi, …; Typically smaller, often more specialized; But freely available

At 57:45 a box covers the slide: *"The world is heading to a future where frontier AI is controlled by the US and China."*

*Still vs. transcript:* the box states the report's two-ecosystem conclusion. The spoken forecast that follows, with Europe and North America on US-led AI and China supplying the rest, is Wooldridge's own and goes beyond both the slide and the report.

## How this source reads through the W&W lens

- `digital-sensing/digital-scouting`: a 54-minute scan of the trends an organisation needs to track: scaling, reasoning models, data-centre limits, open-weight models.
- `digital-sensing/digital-scenario-planning`: the talk turns the report into an explicit scenario, *"if this pace of progress continues … the world is going to be utterly transformed within the next 5 years,"* plus a geopolitical forecast of two AI blocs.
- `contextual/external-triggers`: disruption of software, creative work and mathematics is the disruptive-technology trigger. Wooldridge's architects-not-bricklayers reading says which roles it favours.
- `digital-seizing/balancing-digital-portfolios`: the sovereign-AI stack and the closed-versus-open split frame the choice between external suppliers (US closed models, Chinese open weights) and building internal capability.

## Linked entities and concepts

- **Entities:** [[Stanford HAI]] (channel and host), [[AI100]], [[Michael Wooldridge]] (speaker), [[NVIDIA]] (the opening story; market value), [[Anthropic]] (the $1.5 billion settlement), [[OpenAI]] (ChatGPT; scaling the transformer).
- **Concepts:** [[generative-ai]], [[foundation-models]], [[ai-sovereignty]], [[open-source-ai]], [[small-language-models]], [[attack-surface-management]], [[ai-employment-effects]], [[strategic-foresight]].
- **Dangling** (single-source mention, deferred): Russ Altman (moderator; also an author of the AI Index 2026, so a second mention but not as author here), Sheila McIlraith, Christine Raval, Eric and Mary Horvitz, Rich Sutton, Geoff Hinton, The Verge.

## Source quality

The speaker is the report's chair presenting his own work, so the talk is not independent evidence for the report's claims; where its figures differ from the report, the report is footnoted and the talk is not. The automatic captions are fair, with errors mostly in names, which were corrected at acquire. Wooldridge marks his personal views clearly (*"speaking personally, not as the report"*). A few spoken claims go further than the report: "Millennium Prize problems" in the plural, the exponential time hypothesis "solved", and an unexplained "Nvidia scandal". They are recorded here as his statements, not as facts. The water figure and the dated Nvidia market cap appear on slides without a source. The recording has no Q&A, so the questions Altman collected via Slido are lost.
