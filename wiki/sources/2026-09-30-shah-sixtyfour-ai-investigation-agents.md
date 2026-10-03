---
type: source
kind: video
title: "Investigation Agents: Joining Public Records into Source-Backed Claims for Fraud and Due Diligence (Sixtyfour)"
author: ["YC Root Access"]
publisher: "YC Root Access (YouTube livestream), The Startup Industrial Base: Building for the Next 250, Washington, D.C.; chapter 5:45:12–5:51:41; Saarth Shah (co-founder and CEO, Sixtyfour)"
url: "https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20712s"
date_published: 2026-09-30
date_ingested: 2026-10-03
length: "~6:29 minutes (chapter 5:45:12–5:51:41 of an 8:01:10 livestream; ~155 ASR segments, quotes lightly corrected + 9 stills)"
raw: "../../raw/videos/the-startup-industrial-base-building-for-the-next-250-washington-dc.md"
stills: "../../raw/videos/the-startup-industrial-base-building-for-the-next-250-washington-dc.search-slides-and-diagrams.stills.md"
tags: [yc-root-access, startup-industrial-base, sixtyfour, osint, ai-agents, investigation-agents, research-agents, fraud-detection, healthcare-fraud, medicare, due-diligence, entity-networks, continuous-vetting, founder-pitch]
relationships:
  - type: part-of
    target: 2026-09-30-yc-root-access-startup-industrial-base-dc
    via: "Chapter 5:45:12-5:51:41, a six-minute founder pitch in the afternoon block, just before the afternoon break"
  - type: instance-of
    target: osint
    via: "Agents that gather and join publicly available records about people and organisations, plus clear-web and dark-web material"
  - type: supports
    target: 2026-05-12-techlatest-hacker-search-engines-osint-tools-2026
    via: "Both describe AI agents that correlate many public sources to find relationships between entities. TechLatest names AI-augmented OSINT as a 2026 category and lists its capabilities without naming a system; this talk presents one company's investigation agents and two worked cases from Medicare hospice billing."
    confidence: 0.75
  - type: supports
    target: 2026-04-10-khan-osint-information-gathering-like-a-hacker
    via: "Both rest on information that was public but had not been joined up. Khan audits her own organisation by hand in two hours; this talk describes agents doing that joining across public records, the clear web and the dark web, for fraud, contractor-ownership and personnel cases."
    confidence: 0.65
---

# Investigation Agents: Joining Public Records into Source-Backed Claims for Fraud and Due Diligence (Sixtyfour)

> The defense industrial base of the future will be built by small, fast-moving teams working on some of the hardest problems in national security.
>
> Live from Washington, D.C., Y Combinator brings together founders, senior government officials, and military leaders for a day of conversations about rebuilding America's defense industrial base, working with the government, and closing critical capability gaps across autonomy, munitions, space, secure communications, manufacturing, and more.
>
> *— Channel description, [[Y Combinator|YC Root Access]] (event description; this page covers one chapter)*

**Saarth Shah**, co-founder and CEO of **Sixtyfour**, gives a six-minute founder pitch in the afternoon of YC Root Access's day on the defense industrial base (see [[2026-09-30-yc-root-access-startup-industrial-base-dc|the event page]]). Sixtyfour sells what Shah calls **investigation agents**: research agents that search public records, the clear web and the dark web about a person or an organisation and return claims, each with a source and a confidence score. Most of the six minutes is two worked cases from Medicare hospice billing, one closed and prosecuted, one live and anonymised. The defense link is the customer list Shah names: supply-chain due diligence, screening for North Korean infiltrators, and the kind of vetting a security clearance file needs.

It earns its own page for two reasons. The wiki's [[osint]] pages name AI-augmented OSINT as a category but have no named system behind it; this is one, with cases. And it points OSINT at people and organisations, for fraud and due diligence, where the corpus so far has pointed it at an organisation's own infrastructure.

## TL;DR

- **What an investigation agent is.** *"It's like a research agent that works like your best analyst."* It combines *"open source intelligence, the dark web, clear web"* and comes up with *"claims that are source backed and scored for really high confidence because we are playing in a space where you cannot afford to be wrong"* ([5:45:44](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20744s)). The opening frame: *"we are heading into a world where AI agents and AI is going to make really critical decisions on people and associated entities and vice versa"* ([5:45:20](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20720s)).
- **Uses named, and the speed claim.** Supply-chain due diligence (*"who are our contractors who actually own them"*), illicit networks (the slide: front companies, sanctions evasion and export-control diversion), DPRK screening (*"catching bad actors who are trying to infiltrate our companies and corporations"*), and personnel exposure: checking what people publish that adversaries could abuse. *"These are all things that an analyst would take weeks but an agent can do within minutes"*, *"at a scale and at a price that was never possible before"* ([5:46:47](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20807s)).
- **One model for people and organisations.** *"Across the board entities and individuals actually look very similar. They have digital footprints."* Their networks, *"whether it is a hospice network or a defense supplier"*, look alike ([5:46:56](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20816s)).
- **A closed case, replayed.** In Monterey Park, LA County, seven people from three hospices were charged with allegedly taking $3.2 million over eight years (the agent's case report on the slide: $3,211,419.79, from Medi-Cal and Medicare) by enrolling patients who were not dying and *"rotating them between three hospices every 6 months to avoid Medicare's review trigger"* ([5:47:39](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20859s)). Shah says the agent found *"seven hospices not three"*, *"1,900 hospice certifications that were signed by a pathologist"*, and hospices in the top 1% for spending and the bottom 3% for care ([5:48:43](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20923s)), and that *"none of this is actually in the news or in the case filing"* ([5:49:16](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20956s)).
- **How it works, in one sentence.** *"It will look at one piece of evidence and then go deeper and deeper and deeper until it can connect the pieces of information together"* ([5:49:07](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20947s)).
- **A live case, anonymised.** Run on one address in Simi Valley, California, four Medicare-certified hospices that each present as independent trace to three clusters: two share a phone number and email domain, two were incorporated on the same day at adjacent suites, one was dissolved in 2024 and is still an active federal provider. *"Now I'm not saying that any of this is fraud but that's the whole point of Sixtyfour. We will build a map that an analyst would spend weeks building within minutes"* ([5:50:26](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=21026s)).
- **From tips to continuous checks.** *"Today, investigations across the board would happen when a tip comes in. But with Sixtyfour, every supplier, every entity, every filing can be continuously checked for compliance and red flags"* ([5:50:49](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=21049s)). For vetting, *"self-reporting usually misses all of this information but public records and the internet and the dark web has this information at all times"* ([5:49:39](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20979s)).

## Visual canon

A slide-led pitch: Shah points at the screen twice (*"on the right is…"*), and the slides carry the agent's case report, the timeline, the clearance mapping and two finding cards, none of which he reads out. Of 12 stills cut from the chapter (a second targeted search run, made after a fix to how Gemini's timestamps were parsed; see the manifest), 9 are published below, each transcribed from the frame; Gemini's reading was corrected where it matters for this page: it twice named the third hospice *Alpha Hospice* (it is Fountain Hospice), read the loss as Medicare-only (the slides say $3,211,419.79, Medi-Cal and Medicare), garbled the CCN and list name on the first finding card, miswired both network diagrams, and missed the confidence scores and open leads on the finding cards.

### 1 · A finding, with its source and its confidence

![[assets/2026-09-30-shah-sixtyfour-ai-investigation-agents/19-346m11-research-agents-that-work-like-your-best-analyst.webp|Research agents that work like your best analyst, beside a finding card from Sixtyfour Atlas with its source and confidence score]]

*Still at [5:46:11](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20771s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

Left, **Investigation Agents. Research agents that work like your best analyst.** *They trace people, companies, and the connections between them.* **Every claim is linked to its source and scored for confidence.** *In this work, you can't afford to be wrong, and you can't afford to be unable to show your work.*

Right, **A finding in Sixtyfour Atlas**:

> **Spiritual Touch Hospice Inc. (CCN 551731, Monterey Park CA) listed on CMS FY2026 Hospice Non-Compliant for APU list**
> CMS FY2026 APU non-compliant list and CMS direct mailing notification R12405OTN (Dec 15, 2023) confirm both Spiritual Touch and Compassionate Touch at 2063 S Atlantic Blvd, Monterey Park CA
> cms.gov (+1) · **91%** · Answer

The evidence chain under the claim, top to bottom:

1. *Identify the background behind these individuals connected to a hospice care fraud case.* (the task)
2. CA AG Press Release: 7 Arrested for Hospice Fraud in Monterey County (Feb 5, 2026)
3. Fraud scheme: April 1, 2016 – June 1, 2024; three hospices (Compassionate Touch, Spiritual Touch, Fountain Hospice); total loss $3,211,419.79 to Medi-Cal… *(cut off on the slide)*
4. Spiritual Touch Hospice, Inc. – 2063 S Atlantic Blvd Ste 2A, Monterey Park, CA 91754; NPI #1043534746; President/CEO: [redacted]; Phone: [redacted]…
5. Spiritual Touch Hospice Inc. (CCN 551731, Monterey Park CA) listed on CMS FY2026 Hospice Non-Compliant for APU list

*The claim, its source and its confidence · names redacted.*

*Still vs. transcript:* the narration says claims are *"source backed and scored for really high confidence"* and *"on the right is an example."* The card shows what one looks like: a claim, the record behind it (cms.gov plus one more source), a score of 91%, and the chain of steps from the task to the claim. The claim itself is a regulatory listing, not a finding of fraud.

### 2 · One agent, three missions

![[assets/2026-09-30-shah-sixtyfour-ai-investigation-agents/20-346m56-one-agent-many-missions.webp|One agent, many missions: supply chain due diligence, illicit networks and personnel exposure]]

*Still at [5:46:56](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20816s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

**Where this matters. One agent. Many missions.**

| | Mission | On the card |
|---|---|---|
| 01 | **Supply chain due diligence** | Who actually owns and controls our suppliers? |
| 02 | **Illicit networks** | Front companies, sanctions evasion and export control diversion. |
| 03 | **Personnel exposure** | What can an adversary learn about our people from public data? |

Each card carries a small graph: three suppliers converging on a node tagged *Same owner*; several nodes feeding a node tagged *Front company*; a person linked to records, two of them tagged *Exposed*.

**What takes an analyst weeks takes an agent minutes.** *At a scale that was never possible before.*

*Still vs. transcript:* the slide settles two ASR garbles: *"Alison networks"* is **illicit networks**, and *"our personal"* is **personnel exposure**. It defines the illicit-networks mission (front companies, sanctions evasion, export-control diversion), which the narration does not. The DPRK screening Shah mentions has no card.

### 3 · The same network shape in two domains

![[assets/2026-09-30-shah-sixtyfour-ai-investigation-agents/21-347m26-entities-that-look-independent-but-aren-t.webp|Entities that look independent but are not: a hospice network and a defense supplier network sharing one address, one owner and one phone]]

*Still at [5:47:26](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20846s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

Tag, top left: *The same structure, every time.* Banner, top right: **Aug 2026 · DOJ launches the National Fraud Detection Center**.

**Entities that look independent, but aren't.** *They share addresses, phone numbers and owners. They rotate names, dissolve and reappear.*

- **A hospice network:** Hospice 1 links to *One address* and *One owner*; *One address* links to Hospice 2, *One owner* to Hospice 3; Hospice 2 and Hospice 3 share *One phone*.
- **A defense supplier network:** Supplier links to *One address* and *One owner*; *One address* links to a Front company, *One owner* to a Shell company; the Front company and the Shell company share *One phone*.

**The trail sits in public filings for years before anyone connects it.**

*Still vs. transcript:* the narration says the two networks *"would look very similar"*; the slide draws the one shape both share. Its banner most likely names what Shah calls *"the NDFC"*: a **National Fraud Detection Center**, launched by the DOJ in August 2026 according to the slide. Not checked.

### 4 · The case, and the agent's own case report

![[assets/2026-09-30-shah-sixtyfour-ai-investigation-agents/22-348m04-seven-people-charged-three-hospices-3-2m-allegedly-taken-ove.webp|The Monterey Park case: seven people charged and three hospices, beside the run's intelligence overview from Sixtyfour Atlas]]

*Still at [5:48:04](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20884s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

Left, *The case · Monterey Park, LA County · Charged in Monterey County, January 30, 2026.* **Seven people charged. Three hospices. $3.2M allegedly taken over 8 years.** *The alleged scheme: enroll patients who weren't dying, then rotate them between the three hospices every six months to avoid Medicare's review trigger.* Arrests announced · Feb 5, 2026: *"Attorney General Bonta Announces Seven Arrests for Hospice Fraud"*. *Six defendants have not been convicted. One pleaded guilty.*

Right, **Monterey Park Hospice Fraud Ring — Intelligence Overview** (*the run's own report in Sixtyfour Atlas · names redacted*):

- **Case:** California AG (DMFEA) v. Seven Defendants — Monterey County Superior Court
- **Charges Filed:** January 30, 2026 | **Arrests Announced:** February 5, 2026
- **Fraud Period:** April 1, 2016 – June 1, 2024 (8+ years)
- **Total Loss:** $3,211,419.79 (Medi-Cal + Medicare)
- **Status (as of Sep 2026):** Ongoing — one defendant ([redacted]) pleaded guilty; Medical Board actions against [redacted] and [redacted]; [redacted]'s case still active

| Entity | Address | NPI / CCN | CMS Status |
|---|---|---|---|
| Compassionate Touch Hospice Care, Inc. | 2063 S Atlantic Blvd Ste 2A/2J, Monterey Park, CA 91754 | NPI 1578159737 | Non-compliant APU |
| Spiritual Touch Hospice, Inc. | 2063 S Atlantic Blvd Ste 2A, Monterey Park, CA 91754 | NPI 1043534746 / CCN 551731 | Non-compliant APU FY2026 |
| Fountain Hospice, Inc. (a.k.a. Genesis Health Services DBA Fountain Hospice) | 6308 Woodman Ave Ste 214, Van Nuys, CA 91401 (also Monterey Park) | NPI 1720697196 / CCN 551736 | **CMS Excluded / Terminated** |

Key structural facts:

- All three hospices operated simultaneously under connected ownership/management
- Compassionate Touch and Spiritual Touch share the identical address (Monterey Park)
- Fountain Hospice was excluded from CMS APU and carries a termination date
- Defendants owned, operated, or worked for all three simultaneously
- Patients were "rotated" between companies after 6 months to avoid billing detection
- CMS direct mailing (Dec 15, 2023 - R12405OTN) flagged both Spiritual Touch and Compassionate Touch at the same address

*Still vs. transcript:* the narration's *"almost two $3.2 million"* is $3.2M on the slide and $3,211,419.79 in the report, taken from Medi-Cal as well as Medicare. The slide says *allegedly* and gives the case status (one guilty plea, six not convicted), which the narration does not. It also puts a Monterey Park (LA County) case in Monterey County and its Superior Court, a different county; the press-release title on still 1 says the same. Not checked against the court record.

### 5 · The breadcrumbs, each with its source

![[assets/2026-09-30-shah-sixtyfour-ai-investigation-agents/23-348m32-it-was-all-public-for-years.webp|It was all public, for years: a timeline from the scheme's start to the charges, each event tagged with its public source]]

*Still at [5:48:32](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20912s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

**The breadcrumbs. It was all public, for years.**

| When | Event | Source |
|---|---|---|
| 2016 | Scheme begins. The head nurse arrives straight from a previously prosecuted fraud network. | Court records |
| 2017 | Families post reviews describing billing for visits that never happened. | Public reviews |
| Apr 2021 | The principals start suing each other. Three lawsuits follow. | Court docket |
| 2022 | The medical director's Medicare data links him to seven hospices, not three. | CMS data |
| 2023 | New palliative care companies registered, and the head nurse is convicted of elder abuse. | Registry, court |
| Mid-2024 | Billing stops. A court filing reveals hidden co-ownership of a company billing Medicare. | Court docket |
| | *18 months: no charges* | |
| Jan 2026 | **Charged.** | |

**Hidden ownership was admitted in court 18 months before anyone was charged.**

*Still vs. transcript:* the narration compresses this to *"2021 2022 the directors started suing each other"* and *"in 2024 is when this came to some attention."* The slide gives every event a source type, adds the 2022 CMS link to seven hospices and the head nurse's 2023 conviction, and makes the 18 months between a court admission and the charges its headline.

### 6 · Found in minutes

![[assets/2026-09-30-shah-sixtyfour-ai-investigation-agents/24-349m22-found-in-minutes.webp|Found in minutes: four findings from the Monterey Park run beside its attribution graph in Sixtyfour Atlas]]

*Still at [5:49:22](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20962s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

**What our agent found. Found in minutes.** *Starting from the names in the public charge sheet, the agent mapped:*

| Figure | Finding |
|---|---|
| **7 vs. 3** hospices | CMS data showed seven linked hospices. The case covers three. |
| **1,900+** hospice certifications | Signed by a pathologist, a lab specialist |
| **18 months** early warning | Hidden ownership admitted in a public court filing before charges |
| **Top 1% / Bottom 3%** spend vs. care | Highest spending per patient, fewest nursing visits |

Right, an **Attribution Graph** headed *Compassionate Touch Hospice and Spiritual Touch Hospice · completed*: a task node and the CA AG press release at the top, fanning out to entity nodes (one legible as a Facebook profile; the rest too small or redacted). *The Monterey Park run in Sixtyfour Atlas, each finding cited and scored · names redacted.*

**None of this was connected in the news coverage.**

*Still vs. transcript:* the narration says *"none of this is actually in the news or in the case filing."* The slide claims less: the findings were not *connected* in the news coverage. Its own third card sources one finding to a public court filing, and still 5 sources others to court records and dockets. The slide also defines spend versus care: highest spending per patient, fewest nursing visits.

### 7 · The case read as a clearance file

![[assets/2026-09-30-shah-sixtyfour-ai-investigation-agents/25-349m48-now-read-it-as-a-clearance-file.webp|Now read it as a clearance file: five Monterey Park findings mapped to the question an analyst asks and the vetting category it fits]]

*Still at [5:49:48](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20988s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

**Clearance and vetting. Now read it as a clearance file.**

| What we found in Monterey Park | The question an analyst asks | Where it fits |
|---|---|---|
| Hidden co-owners, revealed only in a court filing | Who really owns and controls this company? | *For the company:* Beneficial ownership, key management personnel |
| State filings and prosecutors named different owners | Does what they reported match reality? | *For the people:* Personal conduct (Guideline E) |
| Head nurse convicted in 2023, still in her role | What changed since the last check? | *For the people:* Continuous vetting, criminal conduct (Guideline J) |
| Principals suing each other; a bank suing the owner personally | Is there financial pressure? | *For the people:* Financial considerations (Guideline F) |
| New companies registered while under scrutiny | Is this a successor to an entity we already know? | *For the company:* Affiliated and successor entities |

**Self-reporting missed all of it. Public records had it for years.**

*Still vs. transcript:* the narration lists *"UBO or personal conduct or continuous vetting or people suing each other for financial pressure."* The slide maps each finding to a vetting category, three of them to lettered adjudicative guidelines (E, J, F), and adds two findings the narration does not mention: state filings and prosecutors naming different owners, and a bank suing the owner personally.

### 8 · Simi Valley: four hospices, three control groups

![[assets/2026-09-30-shah-sixtyfour-ai-investigation-agents/26-350m26-same-agent-a-building-no-one-is-looking-at.webp|Same agent, a building no one is looking at: four Simi Valley hospices resolved into three control groups, with a redacted finding card]]

*Still at [5:50:26](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=21026s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

**Now point it forward. Same agent. A building no one is looking at.** *One address in Simi Valley, California. Four Medicare-certified hospices, each presenting as independent.*

**4 → 3.** *Four "independent" hospices resolved into three control groups, in minutes.*

- Two "separate" hospices share one phone number and one email domain.
- Two hospices, incorporated the same day in adjacent suites.
- Dissolved by the state in 2024. Still an active federal provider.

Middle, one finding card (names and identifiers redacted on the slide):

> **[redacted] HOSPICE CARE, INC — CA entity doc no. [redacted], filed 2020-11-12, business type HOSPICE, principal [redacted] St. #207, Simi Valley CA 93063. Officers: [redacted] (CEO, Director, Secretary, registered agent); [redacted] (Director, Chief Financial Officer). STATUS: TERMINATED — California inactive date 01/29/2024. Its [redacted] nonetheless still lists [redacted] as RN/DPCS at [redacted] St Ste 207 (state corporate record cancelled, federal NPI record not updated).**
> CA Secretary of State registry data mirrored by bizprofile entity page for [redacted] Hospice Care, Inc (doc [redacted]) showing the officer list, the [redacted] St #207 address and Status 'Terminated' with Inactive Date 01/29/2024; cross-referenced with the NPPES NPI record for [redacted] which still carries [redacted] as authorized official (RN/DPCS)
> bizprofile.net (+1) · **75%** · other entities · Answer
> **Explored:** primary record (SOS-derived)
> **Unexplored:** why terminated; successor entity; whether Medicare billing continued after the 2024 termination

Left, the building's report, under the headings *The control clusters* and *Why the address matters*; its body text is too small to transcribe. *The building's report and one finding in Sixtyfour Atlas · names and identifiers redacted.* Footer: *Names withheld. Built from public records by Sixtyfour Atlas and Lattice.*

*Still vs. transcript:* the narration gives the three red flags. The card shows the third as the agent returns it: a score of 75%, a secondary source (a business-profile site mirroring the state registry), and a list of what the agent did **not** explore, including whether Medicare billing continued after the termination. That open question is what separates the red flag from a finding. The footer names the two tools: Atlas and Lattice.

### 9 · No charges, and the map

![[assets/2026-09-30-shah-sixtyfour-ai-investigation-agents/27-350m43-that-s-the-point.webp|That's the point: the Monterey Park timeline beside one corner of the Simi Valley building's network in Sixtyfour Lattice]]

*Still at [5:50:43](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=21043s) from YC Root Access, "The Startup Industrial Base: Building for the Next 250 — Washington, D.C.".*

Tag: **No one here has been charged. None of this proves fraud.**

**That's the point.** *This is the map an analyst would spend weeks building. We produce it in minutes, with every claim sourced and scored for confidence.*

Timeline card: **The Monterey Park scheme ran 8 years. Public from year one, unmistakable by year six.** 2016 *Scheme begins* → 2021 *First public lawsuit* → 2026 *Charged*; 2016–2021 marked *Public from year one*, 2021–2026 *Unmistakable by year six*.

Right, an entity graph: *Sixtyfour Lattice · one corner of the building's network · names withheld.* One hub node, its labelled edges reading *identified by*, *associated with*, *has role in*, *located in* and *has address*; filters *Agents* and *All types*.

*Still vs. transcript:* the narration says *"I'm not saying that any of this is fraud."* The slide adds that no one in the Simi Valley case has been charged, dates the Monterey Park case as public from 2016 and *"unmistakable"* from the first lawsuit in 2021, and shows the map as a graph with typed edges, the only view the talk gives of how the map is structured.

## Why this matters to the wiki

**1. A named system for a category the corpus had only as a label.** [[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026|TechLatest 2026]] names *AI-Augmented Offensive & Defensive Security* as a 2026 category: LLMs and agents that correlate multiple OSINT sources, detect relationships and automate reconnaissance. The [[osint]] and [[ai-agents]] pages record that the claim came with no benchmarks, no named systems and no failure modes. This talk names one system and walks through two cases. It supplies no benchmark and no failure modes.

**2. OSINT pointed at people and organisations.** The [[osint]] and [[attack-surface-management]] pages treat OSINT mainly as finding what an organisation itself has exposed: servers, credentials, code. Shah's uses are other parties: who owns a contractor, whether a hire is an infiltrator, what a clearance file should contain, whether a billing pattern looks like fraud. The premise is the one [[2026-04-10-khan-osint-information-gathering-like-a-hacker|Khan 2026]] works by hand on her own company, *"Everything I found was public. We just never thought to look."* Shah on the Monterey Park case: *"all of this was public for years"* ([5:48:04](https://www.youtube.com/watch?v=T6hVGJ4gepk&t=20884s)). His shift from tip-driven investigation to continuous checks of every supplier and filing mirrors the continuous-monitoring practice that TechLatest and the [[attack-surface-management]] page set out for infrastructure.

**3. The loop, and what it returns.** The method as described is the agent loop of [[ai-agents]] applied to an investigation: take one piece of evidence, follow it, repeat until the pieces connect. What comes back is a set of claims, each with a source and a confidence score, and what Shah calls *"a map"* of the entities involved. The [[knowledge-graphs]] page treats entity graphs mostly as something an agent reads, as memory or retrieval context; here the entity map is what the agent produces. The slides name two tools, Sixtyfour Atlas for the runs and their findings and Sixtyfour Lattice for the graph, and show the map with typed edges such as *has address* and *has role in* (Visual canon, stills 8–9). Beyond that, the talk does not say how the map is built, stored or scored.

**4. Who decides.** [[2026-04-28-anand-wu-genai-playbook|Anand and Wu]] put *"conducting due diligence of records"* in their quality control zone, where errors are costly and the rule is that AI produces and a human verifies; the [[automation-vs-augmentation]] page carries that grid. Shah opens with AI agents making *"really critical decisions on people"*, and closes the live case with *"I'm not saying that any of this is fraud"*: the agent builds the map an analyst would have built. The talk does not say who acts on the map, or how.

**Dynamic capabilities.** No cell tagged. The talk pitches a tool for investigating outside parties; it says nothing about how an organisation senses, seizes or transforms around digital technology, and none of the Warner & Wäger cells fits without stretching.

## Linked entities and concepts

- **Entities**: [[Y Combinator]] (host; YC Root Access is the channel and the event).
- **Sources**: [[2026-09-30-yc-root-access-startup-industrial-base-dc|YC Root Access, The Startup Industrial Base (event page)]], [[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026|TechLatest 2026]], [[2026-04-10-khan-osint-information-gathering-like-a-hacker|Khan 2026]], [[2026-04-28-anand-wu-genai-playbook|Anand & Wu 2025]].
- **Concepts**: [[osint]] (the discipline, here run by agents and pointed at people and organisations), [[ai-agents]] (the evidence-following loop), [[attack-surface-management]] (the continuous-monitoring practice the talk's "continuously checked" mirrors), [[knowledge-graphs]] (entity networks as agent output rather than input), [[automation-vs-augmentation]] (due diligence in the produce-and-verify zone).
- **Dangling** (single-source mention, deferred): **Saarth Shah**, **Sixtyfour**, **Medicare** (and its review trigger for hospice stays), **National Fraud Detection Center** (DOJ, launched August 2026 according to a slide; spoken as *"the NDFC"*).

## Debates and supersession

- **A founder's own demo.** Everything about Sixtyfour's capability rests on Shah's account of his own product: the definition, the two cases, *"weeks"* versus *"minutes"*, and the confidence scoring. No accuracy figures, error rates, false-positive rates or comparison with human analysts are given. The two finding cards on the slides carry scores of 91% and 75%; how the scores are computed is not described.
- **The closed case.** The case figures (seven people charged, three hospices, $3.2 million over eight years, a six-monthly rotation between hospices) and the timeline the agent reconstructs (a head nurse arriving in 2016 from a previously prosecuted fraud network, complaints about billing for visits that never happened in 2017, directors suing each other in 2021–2022, attention in 2024, prosecution in 2026) were not checked against court records or press releases. The agent's extra findings (seven hospices, 1,900 certifications signed by a pathologist, top 1% spend and bottom 3% care) and the claim that *"none of this"* is in the news or the case filing are unverified here. The slides claim less than the speech: *"None of this was connected in the news coverage"*, and they source the 18-month finding to a public court filing and other events to court records and dockets (Visual canon, stills 5–6). The dollar figure, garbled in the ASR, is $3,211,419.79 from Medi-Cal and Medicare in the agent's case report, which also puts the Monterey Park (LA County) case in Monterey County Superior Court; neither was checked.
- **The live case is red flags, not findings.** Shah anonymised the Simi Valley entities and says himself that he is *"not saying that any of this is fraud"*. Shared contact details, same-day incorporation at adjacent suites and a dissolved company still on the provider list are indicators; the talk shows the map, not an outcome.
- **Decision language versus product.** The opening line has AI agents making *"really critical decisions on people"*; the product as demonstrated builds a map for an analyst. The talk does not say which of the two Sixtyfour sells, or where a human checks the output.
- **Investigating individuals.** The [[osint]] page sets out an authorization and privacy envelope: the line *"depends heavily on intent and authorization"*. Several of Shah's uses concern individuals (personnel exposure, clearance-style vetting, insider screening, continuous checks of every entity). The talk does not discuss authorization, consent, false accusations or the rights of the people named.
- **Context claims not checked.** *"Fraud has been a big federal priority this year"* and the reference to having *"just launched the NDFC"* a couple of months earlier are Shah's; neither was checked. A slide names the second: *"Aug 2026 · DOJ launches the National Fraud Detection Center"* (Visual canon, still 3), so "NDFC" is most likely that center's initials as spoken; the launch itself was not checked.

## What was actually ingested

The chapter **5:45:12–5:51:41** of the 8:01:10 livestream; speech runs 5:45:13–5:51:23, about 154 segments of raw auto-generated English captions, not cleaned at acquire. Quotes were checked against the raw transcript at the cited timestamps and corrected only for names and one filler: *"64"* → Sixtyfour, *"Sarth"* and *"This is hard from 64"* → Saarth / Saarth from Sixtyfour (from the chapter heading), *"Semi Valley"* → Simi Valley, *"theospices"* → the hospices, a stray *"u"* before *"Medicare's"* dropped. Left unquoted because the ASR is unclear: *"almost two $3.2 million"*, *"top percent 1%"*, *"Alison networks"*, *"DPRK scanning"* (possibly *screening*), *"our personal"*. The slides settle four of them: **$3.2M** (and $3,211,419.79 in the agent's case report), **Top 1%**, **illicit networks** and **personnel exposure**; *"DPRK scanning"* has no slide. Of 12 stills cut from the chapter by a targeted Gemini search (the second run, after a timestamp-parsing fix; see the `stills:` manifest), 9 are published in the Visual canon after checking each against the frame; left out are the title card (with a *Trusted by* row of company logos), a slide on continuous monitoring that the narration says almost word for word, and the closing call to action (a one-week pilot offer). Not checked: Sixtyfour's website and product, the Monterey Park court filings and press coverage, the Simi Valley entities, and the National Fraud Detection Center launch.
