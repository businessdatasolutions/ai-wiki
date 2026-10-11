---
type: query-trace
question: "What does the evidence say about how AI answer engines and AI agents change buyer discovery and decision-making (answer engine optimization, generative engine optimization, agentic web, agentic commerce), and which claims are well supported versus weakly supported?"
date: 2026-10-09
language: en
trace: "2026-10-09-ai-answer-engines-agents-buyer-discovery-evidence-query-trace.json"
pages_used: 8
pages_ignored: 64
---

# Query trace - AI answer engines and agents: buyer discovery and evidence quality

## 1. Question
- **Original:** What does the evidence say about how AI answer engines and AI agents change buyer discovery and decision-making (answer engine optimization, generative engine optimization, agentic web, agentic commerce), and which claims are well supported versus weakly supported?
- **Restated:** What does the wiki evidence say about how AI answer engines and agents change buyer discovery and decision-making, and which claims are strongly vs weakly supported?
- **Facets:** 1) How answer engines/agents change buyer discovery (search to answers, referral traffic) 2) What AEO/GEO practice claims and how it is evidenced 3) Agentic web and agentic commerce: agents as buyers/intermediaries 4) Evidence quality: which claims are well vs weakly supported

## 2. Paths explored
Retrieval: `node scripts/wiki-retrieve.mjs --json -n 12 "<question>"` (qmd + graph, hops 1, RRF, decay-ranked). 72 candidates, 10 qmd hits, graph available, no graph_warning. No gap-expansion round. Extra checks (not retrieval): a corpus grep for "aggarwal" / "generative engine optim" found only the AEO concept page and one raw transcript (Kilpatrick), i.e. no GEO academic source.

**qmd hits** (relevance stream)
| # | Page | type | qmd score | fused | verdict |
|---|------|------|-----------|-------|---------|
| 1 | `wiki/concepts/enterprise-ai-adoption.md` | concept | 0.77 | 0.976 | IGNORE |
| 3 | `wiki/sources/2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook.md` | source | 0.61 | 0.91 | USE |
| 4 | `wiki/sources/2026-06-17-priest-atlantic-pwc-ai-agents-changing-business.md` | source | 0.59 | 0.896 | IGNORE |
| 5 | `wiki/sources/2026-08-13-a16z-lighthouse-or-landgrab-ai-sales-strategy.md` | source | 0.59 | 0.882 | IGNORE |
| 6 | `wiki/sources/2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet.md` | source | 0.48 | 0.869 | USE |
| 2 | `wiki/concepts/agentic-web.md` | concept | 0.62 | 0.858 | USE |
| 7 | `wiki/sources/2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china.md` | source | 0.48 | 0.856 | USE |
| 8 | `wiki/sources/2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells.md` | source | 0.41 | 0.843 | USE |
| 9 | `wiki/sources/2026-08-10-maza-a16z-kavak-rebuilding-a-company-around-ai.md` | source | 0.36 | 0.831 | IGNORE |
| 10 | `wiki/sources/2025-06-09-krakowski-human-centered-ai-field-experiment.md` | source | 0.26 | 0.819 | IGNORE |

**graph neighbours** (typed-edge stream; 62 pages, listed in full in the JSON trace; those with a verdict of USE or a distinct IGNORE class are shown, the rest are `below-threshold`)
| Page | reached via | fused | verdict |
|------|-------------|-------|---------|
| `wiki/concepts/answer-engine-optimization.md` | concepts/enterprise-ai-adoption --supports--> this | 0.422 | USE |
| `wiki/concepts/generative-ai.md` | concepts/enterprise-ai-adoption --caused--> this | 0.383 | IGNORE |
| `wiki/concepts/ai-agents.md` | concepts/agentic-web --depends-on--> this | 0.35 | USE |
| `wiki/entities/HubSpot.md` | sources/2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook --published-by--> this | 0.324 | IGNORE |
| `wiki/sources/2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook.md` | sources/2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook --supports--> this | 0.319 | USE |
| `wiki/sources/2026-04-28-ai-index-report-2025.md` | sources/2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet --supports--> this | 0.281 | IGNORE |
| `wiki/sources/2026-06-09-cloudflare-investor-day-2026.md` | sources/2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet --depends-on--> this | 0.278 | IGNORE |
| `wiki/entities/Cloudflare.md` | sources/2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet --published-by--> this | 0.267 | IGNORE |

**index.md / gap-expansion:** none.

## 3. Ignore policy applied
- `off-facet` - semantically adjacent (AI adoption, sales, org design) but none of the four facets.
- `below-threshold` - low fused score, graph-only, no facet needs it.
- `wrong-granularity` - entity card where a claim/figure is needed.
- `redundant` - restated in a higher-ranked USE page.

## 4. Information ignored
| Page | reason-class | one-line reason |
|------|--------------|-----------------|
| `wiki/concepts/enterprise-ai-adoption.md` | off-facet | top qmd hit but generic adoption concept; AEO/agentic web appear only as cases already covered by the two USE concepts |
| `wiki/sources/2026-06-17-priest-atlantic-pwc-ai-agents-changing-business.md` | off-facet | internal org design and hourglass organisation, not buyer behaviour |
| `wiki/sources/2026-08-13-a16z-lighthouse-or-landgrab-ai-sales-strategy.md` | off-facet | seller-side B2B sales strategy; says nothing on AI intermediating buyers (page itself notes no source on agents selling) |
| `wiki/sources/2026-08-10-maza-a16z-kavak-rebuilding-a-company-around-ai.md` | off-facet | company transformation, not buyer discovery |
| `wiki/sources/2025-06-09-krakowski-human-centered-ai-field-experiment.md` | off-facet | worker-AI field experiment, not buyer discovery |
| `wiki/concepts/automation-vs-augmentation.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/concepts/ai-sovereignty.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/concepts/ai-employment-effects.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/concepts/micro-productivity-trap.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/concepts/jagged-frontier.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/concepts/dynamic-capabilities.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/concepts/ai-knowledge-hiding.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/concepts/open-source-ai.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/concepts/responsible-ai.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/concepts/founder-led-sales.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/concepts/systems-thinking.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/concepts/generative-ai.md` | off-facet | general GenAI concept; only the sea-of-sameness aside is relevant and is covered in AEO concept |
| `wiki/concepts/technology-adoption-theories.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/concepts/strategic-foresight.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-05-06-mit-ocw-future-of-mit-open-education.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/concepts/document-intelligence.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-06-12-dellacqua-cybernetic-teammate-field-experiment-genai-teamwork.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/entities/HubSpot.md` | wrong-granularity | entity card; claims live in the two HubSpot source pages |
| `wiki/sources/2026-06-16-mollick-simon-sinek-ai-skills-experience-edge.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-04-28-dellacqua-jagged-technological-frontier.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/syntheses/ai-worker-maturity-levels.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-07-10-building-the-future-of-agentic-infrastructure.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-07-14-khan-academy-ceo-the-real-ai-opportunity-is-in-boring-industries-sal-khan.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-06-22-yc-kolysh-how-to-get-your-first-10-customers.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-02-09-hubspot-customer-success-with-claude.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-06-24-rubinstein-onyemah-startup-founders-new-sales-playbook.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-07-31-collison-yc-startup-school-is-ai-breaking-the-lean-startup-playbook.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-08-12-tan-a16z-new-rules-for-founders.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-04-28-ai-index-report-2025.md` | off-facet | data-commons crawler restrictions, tangential to buyer discovery |
| `wiki/sources/2026-06-09-cloudflare-investor-day-2026.md` | redundant | its attention-share, traffic-decline and x402 figures are restated in the USE Cloudflare blog post and agentic-web; deck marks attention figure as illustrative |
| `wiki/sources/2026-04-26-how-to-win-when-software-is-not-a-moat-evan-spiegel-snapchat-ceo.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-05-10-ries-lennys-force-destroys-companies-within.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-09-18-bloomberg-originals-how-china-plans-to-win-global-ai-race.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/entities/Cloudflare.md` | wrong-granularity | entity card; claims live in the Cloudflare source pages |
| `wiki/sources/2026-09-18-reuters-on-assignment-inside-chinas-ai-race.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-06-18-dumra-mit-smr-dbs-everyone-an-innovator.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2025-03-17-cemri-why-do-multi-agent-llm-systems-fail.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-08-11-huang-sequoia-own-your-intelligence-sovereign-ai.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-05-07-kiron-schrage-compound-benefits.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-08-18-covello-gs-new-models-ai-investment-landscape.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-09-14-google-cloud-agent-factory-agent-harnesses-explained.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2025-01-08-khanfar-factors-influencing-ai-adoption-slr.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-04-28-anand-wu-genai-playbook.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |
| `wiki/sources/2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook.md` | below-threshold | graph-only or low-ranked neighbour; no decomposed facet needs it |

## 5. Information used
| Page | type | effConf | contribution |
|------|------|---------|--------------|
| `wiki/sources/2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook.md` | source | - | single-firm traffic -80% / leads +20% and its caveats |
| `wiki/sources/2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet.md` | source | - | network-level non-human traffic, crawler-purpose and referral data; vendor, unaudited |
| `wiki/concepts/agentic-web.md` | concept | 0.679 | on-facet: zero-click shift, Cloudflare network data, licensing, x402/agentic commerce, evidence-independence debate |
| `wiki/sources/2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china.md` | source | - | agentic commerce deployed at consumer scale (Alibaba, JD) - practitioner keynote claims |
| `wiki/sources/2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells.md` | source | - | incumbent retailer CEO view: agents disintermediate customer relationship (prediction) |
| `wiki/concepts/answer-engine-optimization.md` | concept | 0.679 | on-facet: AEO/GEO definition, SEO contrast, consensus claim, six content signals, and an explicit Debates section on vendor-only evidence (graph-only, promoted on relevance: it is the wiki page for the question) |
| `wiki/concepts/ai-agents.md` | concept | 0.94 | agentic-commerce and disintermediation sections (graph-only, USE for the agents facet) |
| `wiki/sources/2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook.md` | source | - | primary source for all AEO figures and its own Scope and reliability section (vendor, no method) |

## 6. Answer-element map
| Anchor | Answer element (claim) | Wiki page(s) | Section / span used |
|--------|------------------------|--------------|---------------------|
| [W1] | HubSpot reports losing ~80% of web traffic (140M visits in a year from May 2024) while leads grew 20%, attributed to buyers moving research into ChatGPT/Claude; single-firm, self-reported | [[agentic-web]], [[2026-09-18-bodnar-flanagan-hubspot-unbound-ai-broke-marketing-playbook]] | Key claims 1 / Scope and reliability |
| [W2] | Cloudflare network data: non-human traffic >50% of Internet traffic; human traffic -35 to -40% (Jun 2025 to Apr 2026) in retail, software, IT, financial services; 52% of crawler requests for AI training; vendor, unaudited, "traffic" undefined | [[2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet]], [[agentic-web]] | Parts I-V / Scope and reliability |
| [W3] | Attention-share figure (open web ~25% vs 55%) is labelled illustrative by the source deck; the 2x Google information advantage is asserted without method | [[2026-07-01-cloudflare-content-independence-day-one-year-on-agentic-internet]] | Scope and reliability |
| [W4] | AEO/GEO is the practice of being named and cited in AI answers; it differs from SEO in unit of demand (long prompts), absence of demand data, and goal (mention/citation) | [[answer-engine-optimization]] | Working definition; How AEO differs from SEO |
| [W5] | Core AEO claim: brand mentions across the web (consensus) matter most; cited-source shares of ~8% own site, ~30% PR/news, ~10% social come from HubSpot/XFunnel analysis without method or date | [[2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook]], [[answer-engine-optimization]] | Key claims 3 / Scope and reliability |
| [W6] | AEO outcome figures (+170% MQLs, +82% closed deals, +8% monthly visibility, Fresha 86% visibility/16% share of voice) are vendor/customer self-reports without baseline and confounded by adopter selection; the wiki holds them at confidence 0.75 | [[2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook]], [[answer-engine-optimization]] | Scope and reliability; Debates |
| [W7] | Six on-site content signals (direct answers, original expertise, entity richness, full-funnel coverage, freshness, bot accessibility) are practitioner guidance from one session, not independently tested | [[answer-engine-optimization]] | Key claims 4 |
| [W8] | Only the zero-click 60% figure and Similarweb prompt-length chart (15-16 words, ~5 prompts/session for ChatGPT/Claude) in the AEO session come from non-HubSpot sources, and neither is reproduced in the wiki | [[2026-09-29-amiel-sanders-hubspot-unbound-aeo-playbook]] | Scope and reliability; Key claims 2 |
| [W9] | Open questions in the wiki: prompt sets as stand-in for demand, personalisation undercutting measurement, whether paid placement shrinks organic AEO, whether agents need different signals than human-read answers | [[answer-engine-optimization]] | Debates and supersession |
| [W10] | Agentic commerce at consumer scale is claimed for China (Alibaba Qen >100M users; JD Joy Streamer ~2.3bn RMB / ~$250M in sales in one Double 11) from a conference keynote; no independent verification in the wiki | [[ai-agents]], [[2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china]] | Agentic commerce at consumer scale |
| [W11] | A retail CEO (DFI Retail Group) names agentic personal assistants disintermediating the retailer-customer relationship (loyalty and data) as a main concern; an executive prediction, not evidence of effect | [[ai-agents]], [[2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells]] | Agents as strategic threat |
| [W12] | Machine payments: Cloudflare reports x402 (with Coinbase and Stripe) and 2bn 402 responses/day; no independent measure of money moved | [[agentic-web]] | Key claims 4 |
| [W13] | Wiki gap: no peer-reviewed GEO literature (e.g. Aggarwal et al.) and no independent measurement of AI-answer citations or referral traffic is ingested; the wiki names these as the ingest targets that would raise confidence | [[answer-engine-optimization]], [[agentic-web]] | Debates and supersession |

## 7. Final answer
**Short answer.** The wiki holds a coherent *story* but little *independent evidence*. Almost everything on this question comes from vendors describing their own products or from practitioner talks, and the wiki itself caps confidence at 0.75 for that reason [W13][W6].

**Better supported (measured, but by interested parties).**
- Discovery is moving from search results to AI answers and referral traffic is not following. Two independent vantage points agree in direction: Cloudflare's network data (non-human traffic above 50%; human traffic down 35-40% in retail, software, IT and finance between June 2025 and April 2026) [W2] and HubSpot's own site (-80% traffic, +20% leads) [W1]. Both are self-reported by vendors, unaudited, and neither separates AI substitution from other causes (seasonality, bot classification, customer mix) [W1][W2].
- Buyers who arrive via an answer engine are reported to arrive late in the journey, ready to decide; HubSpot calls answer-engine visits its strongest purchase predictor [W5][W6]. This is one firm's claim without method.

**Weakly supported (assertion, unsourced numbers, or prediction).**
- What drives citation in answer engines: that cross-web mentions ("consensus") matter most, with cited-source shares of about 8% own site, 30% PR/news, 10% social, comes from HubSpot/XFunnel's own analysis with no method, sample or date [W5]. The six on-site content signals are practitioner guidance, not tested effects [W7].
- That AEO works: +170% MQLs, +82% closed deals, +8% monthly visibility and Fresha's 86% visibility are vendor or customer self-reports without baselines and are confounded by which customers chose to adopt [W6]. Cloudflare's 25%-vs-55% attention share is marked illustrative by its own deck and the 2x Google advantage is asserted without method [W3].
- Agentic commerce: Alibaba and JD figures come from a single keynote [W10]; the retail-CEO view is a prediction about disintermediation [W11]; x402 volumes are vendor-reported [W12].

**Open or not covered.** Whether a constructed prompt set represents real demand, whether personalisation makes tracked answers unrepresentative, whether paid placement will shrink organic AEO, and whether agents acting without a human reader need different signals [W9]. The wiki contains no peer-reviewed GEO study and no independent referral-traffic study [W13]. It contains no evidence on how buyers' *decisions* (as opposed to discovery) change beyond the late-arrival claim [W5].

## 8. Trace artifact
Machine-readable provenance: [`2026-10-09-ai-answer-engines-agents-buyer-discovery-evidence-query-trace.json`](2026-10-09-ai-answer-engines-agents-buyer-discovery-evidence-query-trace.json)
