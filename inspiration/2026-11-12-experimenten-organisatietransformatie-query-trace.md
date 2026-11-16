---
type: query-trace
question: "Zoek in de wiki naar modellen, best-practices en cases voor het inzetten van experimenten tbv organisatietransformatie"
date: 2026-11-12
language: nl
trace: "2026-11-12-experimenten-organisatietransformatie-query-trace.json"
pages_used: 9
pages_ignored: 77
---

# Query trace — experimenten voor organisatietransformatie

## 1. Question

- **Original:** Zoek in de wiki naar modellen, best-practices en cases voor het inzetten van experimenten tbv organisatietransformatie
- **Restated:** Welke modellen, best practices en cases bevat de wiki over het gebruik van experimenten om organisaties te transformeren?
- **Facets:** 1) Modellen: frameworks die experimenteren een plek geven in transformatie (W&W rapid prototyping, fasenmodellen, portfoliovormen) 2) Best practices: hoe experimenten op te zetten, te begrenzen, op te schalen en te meten (pilot naar productie) 3) Cases: organisaties die experimenten aantoonbaar zo hebben ingezet

## 2. Paths explored

Retrieval: `node scripts/wiki-retrieve.mjs --json -n 12 "<question>"` (hops 1, k_rrf 60, graph_w 0.5). Graph available: true. 10 qmd hits, 83 candidates.

**qmd hits** (relevance stream)

| # | Page | type | qmd score | fused | verdict |
|---|------|------|-----------|-------|---------|
| 1 | `wiki/entities/Ron%20Carucci.md` | entity | 1.00 | 0.880 | IGNORE |
| 2 | `wiki/sources/2026-10-07-from-conversations-to-an-executive-learning-architecture-ep-22.md` | source | 0.33 | 0.925 | IGNORE |
| 3 | `wiki/sources/2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook.md` | source | 0.20 | 0.910 | IGNORE |
| 4 | `wiki/sources/2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026.md` | source | 0.17 | 0.896 | IGNORE |
| 5 | `wiki/sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage.md` | source | 0.14 | 0.882 | IGNORE |
| 6 | `wiki/sources/2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero.md` | source | 0.13 | 0.869 | IGNORE |
| 7 | `wiki/sources/2026-08-19-rohrer-goto-modern-enterprise-architecture-architecting-for-outcomes.md` | source | 0.11 | 0.856 | IGNORE |
| 8 | `wiki/concepts/enterprise-ai-adoption.md` | concept | 0.10 | 0.864 | **USE W4** |
| 9 | `wiki/sources/2026-06-25-carroll-stanford-gsb-making-organizational-culture-great.md` | source | 0.09 | 0.831 | IGNORE |
| 10 | `wiki/sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees.md` | source | 0.08 | 0.819 | IGNORE |

**graph neighbours** (`--hops 1`, typed-edge stream)

| Page | reached via | hops | fused | verdict |
|------|-------------|------|-------|---------|
| `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` | 2026-10-07-from-conversations-to-an-executive-learning-architecture-ep-22 --supports--> | 1 | 0.448 | IGNORE |
| `wiki/entities/MIT-Sloan-CIO-Symposium.md` | 2026-10-07-from-conversations-to-an-executive-learning-architecture-ep-22 --published-by--> | 1 | 0.440 | IGNORE |
| `wiki/sources/2026-09-15-from-debate-to-inquiry-designing-conversations-worth-preserving-ep-21.md` | 2026-10-07-from-conversations-to-an-executive-learning-architecture-ep-22 --supports--> | 1 | 0.434 | IGNORE |
| `wiki/entities/Allan-Tate.md` | 2026-10-07-from-conversations-to-an-executive-learning-architecture-ep-22 --authored-by--> | 1 | 0.433 | IGNORE |
| `wiki/entities/Irving-Wladawsky-Berger.md` | 2026-10-07-from-conversations-to-an-executive-learning-architecture-ep-22 --authored-by--> | 1 | 0.426 | IGNORE |
| `wiki/sources/2025-06-09-krakowski-human-centered-ai-field-experiment.md` | 2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook --supports-->; 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees --supports--> | 1 | 0.422 | IGNORE |
| `wiki/sources/2026-07-10-when-ai-becomes-common-organizational-capability-becomes-the-advantage-ep-16.md` | 2026-10-07-from-conversations-to-an-executive-learning-architecture-ep-22 --supports-->; 2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --supports--> | 1 | 0.413 | IGNORE |
| `wiki/sources/2026-06-18-dumra-mit-smr-dbs-everyone-an-innovator.md` | 2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook --supports-->; 2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026 --supports--> | 1 | 0.410 | **USE W8** |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | 2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook --supports-->; 2026-08-19-rohrer-goto-modern-enterprise-architecture-architecting-for-outcomes --supports--> (+1) | 1 | 0.407 | IGNORE |
| `wiki/sources/2026-08-16-hill-bloomberg-leaders-ceo-skills-age-of-ai.md` | 2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook --supports-->; 2026-06-25-carroll-stanford-gsb-making-organizational-culture-great --supports--> | 1 | 0.404 | IGNORE |
| `wiki/entities/Bloomberg-Podcasts.md` | 2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook --published-by--> | 1 | 0.401 | IGNORE |
| `wiki/sources/2026-09-08-west-lacroix-zimmerman-mckinsey-why-strategy-needs-mobilization.md` | 2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook --supports-->; 2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --supports--> | 1 | 0.398 | IGNORE |
| `wiki/entities/Microsoft.md` | 2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026 --published-by--> | 1 | 0.391 | IGNORE |
| `wiki/sources/2026-03-31-roslansky-smith-tools-and-weapons-open-to-work.md` | 2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026 --supports--> | 1 | 0.387 | IGNORE |
| `wiki/sources/2026-05-02-schoening-lennys-podcast-cultivating-agency-ai-era.md` | 2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026 --supports--> | 1 | 0.382 | IGNORE |
| `wiki/sources/2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai.md` | 2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026 --supports--> | 1 | 0.377 | IGNORE |
| `wiki/sources/2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset.md` | 2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026 --supports--> | 1 | 0.372 | IGNORE |
| `wiki/sources/2026-07-14-khan-academy-ceo-the-real-ai-opportunity-is-in-boring-industries-sal-khan.md` | 2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026 --supports--> | 1 | 0.368 | IGNORE |
| `wiki/sources/2026-07-27-george-wood-worklab-future-of-work-has-no-org-chart.md` | 2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026 --supports--> | 1 | 0.363 | **USE W9** |
| `wiki/sources/2026-08-10-miller-worklab-the-ai-shift-most-companies-didnt-see-coming.md` | 2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026 --supports--> | 1 | 0.358 | IGNORE |
| `wiki/sources/2026-03-28-nguyen-ai-adoption-toe-dynamic-capabilities.md` | 2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --supports--> | 1 | 0.350 | IGNORE |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | 2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --supports-->; 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees --supports--> | 1 | 0.345 | IGNORE |
| `wiki/sources/2026-05-03-rewired-second-edition-sample.md` | 2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --supports--> | 1 | 0.341 | IGNORE |
| `wiki/sources/2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china.md` | 2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --supports-->; enterprise-ai-adoption --supports--> | 1 | 0.337 | IGNORE |
| `wiki/sources/2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services.md` | 2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --supports--> | 1 | 0.333 | IGNORE |
| `wiki/entities/McKinsey-&-Company.md` | 2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --authored-by--> | 1 | 0.331 | IGNORE |
| `wiki/sources/2026-08-10-banholzer-laberge-mckinsey-how-to-maximize-competitive-advantage.md` | 2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --supports--> | 1 | 0.330 | IGNORE |
| `wiki/sources/2026-10-27-catlin-durth-hamalainen-montard-mckinsey-ceo-agenda-agentic-age.md` | 2026-07-09-catlin-mckinsey-podcast-real-ai-advantage --supports--> | 1 | 0.326 | IGNORE |
| `wiki/sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships.md` | 2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero --supports--> | 1 | 0.322 | IGNORE |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | 2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero --supports-->; enterprise-ai-adoption --supports--> | 1 | 0.319 | IGNORE |
| `wiki/sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation.md` | 2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero --supports-->; 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees --supports--> | 1 | 0.315 | IGNORE |
| `wiki/sources/2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook.md` | 2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero --supports--> | 1 | 0.312 | IGNORE |
| `wiki/sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs.md` | 2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero --supports--> | 1 | 0.308 | IGNORE |
| `wiki/sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company.md` | 2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero --supports--> | 1 | 0.305 | IGNORE |
| `wiki/sources/2025-07-02-joshi-venkatraman-fowler-expert-generalists.md` | 2026-08-19-rohrer-goto-modern-enterprise-architecture-architecting-for-outcomes --supports--> | 1 | 0.302 | IGNORE |
| `wiki/sources/2026-08-14-blomfield-yc-building-structuring-ai-native-company.md` | 2026-08-19-rohrer-goto-modern-enterprise-architecture-architecting-for-outcomes --supports--> | 1 | 0.299 | IGNORE |
| `wiki/concepts/ai-in-health-care.md` | enterprise-ai-adoption --instance-of--> | 1 | 0.287 | IGNORE |
| `wiki/concepts/automation-vs-augmentation.md` | enterprise-ai-adoption --supports--> | 1 | 0.287 | IGNORE |
| `wiki/concepts/ai-knowledge-hiding.md` | enterprise-ai-adoption --instance-of--> | 1 | 0.284 | IGNORE |
| `wiki/concepts/ai-sovereignty.md` | enterprise-ai-adoption --supports--> | 1 | 0.281 | IGNORE |
| `wiki/concepts/dynamic-capabilities.md` | enterprise-ai-adoption --supports--> | 1 | 0.281 | **USE W1** |
| `wiki/concepts/ai-employment-effects.md` | enterprise-ai-adoption --caused--> | 1 | 0.279 | IGNORE |
| `wiki/concepts/agentic-web.md` | enterprise-ai-adoption --supports--> | 1 | 0.278 | IGNORE |
| `wiki/concepts/jagged-frontier.md` | enterprise-ai-adoption --uses--> | 1 | 0.275 | IGNORE |
| `wiki/concepts/micro-productivity-trap.md` | enterprise-ai-adoption --caused--> | 1 | 0.274 | **USE W3** |
| `wiki/concepts/generative-ai.md` | enterprise-ai-adoption --caused--> | 1 | 0.266 | IGNORE |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | enterprise-ai-adoption --supports--> | 1 | 0.265 | IGNORE |
| `wiki/concepts/answer-engine-optimization.md` | enterprise-ai-adoption --supports--> | 1 | 0.264 | IGNORE |
| `wiki/concepts/responsible-ai.md` | enterprise-ai-adoption --part-of--> | 1 | 0.261 | IGNORE |
| `wiki/concepts/open-source-ai.md` | enterprise-ai-adoption --supports--> | 1 | 0.257 | IGNORE |
| `wiki/concepts/document-intelligence.md` | enterprise-ai-adoption --part-of--> | 1 | 0.256 | IGNORE |
| `wiki/concepts/founder-led-sales.md` | enterprise-ai-adoption --supports--> | 1 | 0.255 | IGNORE |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | enterprise-ai-adoption --supports-->; 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees --contradicts--> | 1 | 0.247 | IGNORE |
| `wiki/sources/2026-05-06-mit-ocw-future-of-mit-open-education.md` | enterprise-ai-adoption --supports--> | 1 | 0.245 | IGNORE |
| `wiki/concepts/technology-adoption-theories.md` | enterprise-ai-adoption --supports--> | 1 | 0.244 | IGNORE |
| `wiki/sources/2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas.md` | enterprise-ai-adoption --supports--> | 1 | 0.243 | IGNORE |
| `wiki/sources/2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells.md` | enterprise-ai-adoption --supports--> | 1 | 0.239 | IGNORE |
| `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | enterprise-ai-adoption --instance-of--> | 1 | 0.236 | **USE W2** |
| `wiki/sources/2026-07-01-bello-mckinsey-podcast-serial-builder-advantage.md` | 2026-06-25-carroll-stanford-gsb-making-organizational-culture-great --supports--> | 1 | 0.233 | IGNORE |
| `wiki/sources/2026-07-07-sinofsky-amble-a16z-software-in-the-age-of-agents.md` | 2026-06-25-carroll-stanford-gsb-making-organizational-culture-great --supports--> | 1 | 0.231 | IGNORE |
| `wiki/sources/2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces.md` | 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees --supports--> | 1 | 0.229 | IGNORE |
| `wiki/syntheses/ai-worker-maturity-levels.md` | enterprise-ai-adoption --supports--> | 1 | 0.228 | IGNORE |
| `wiki/sources/2026-05-02-dutt-chatterji-ai-experimentation-to-transformation.md` | 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees --supports--> | 1 | 0.228 | IGNORE |
| `wiki/concepts/systems-thinking.md` | enterprise-ai-adoption --supports--> | 1 | 0.226 | IGNORE |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | enterprise-ai-adoption --supports--> | 1 | 0.226 | IGNORE |
| `wiki/sources/2026-07-08-jensen-huang-why-companies-need-open-agent-systems.md` | 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees --supports--> | 1 | 0.222 | IGNORE |
| `wiki/sources/2026-05-08-running-an-ai-native-engineering-org.md` | 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees --supports--> | 1 | 0.221 | IGNORE |
| `wiki/sources/2026-06-11-mit-smr-agentic-ai-what-leaders-wish-they-knew-sooner.md` | 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees --contradicts--> | 1 | 0.221 | IGNORE |
| `wiki/sources/2026-06-17-priest-atlantic-pwc-ai-agents-changing-business.md` | 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees --supports--> | 1 | 0.219 | IGNORE |
| `wiki/sources/2026-08-11-ellmer-dhar-bcg-so-what-is-your-ai-rollout-built-to-fail.md` | 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees --supports--> | 1 | 0.217 | IGNORE |
| `wiki/sources/2026-09-30-singh-botha-bloomberg-flow-engineering-ai-hardware-design.md` | 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees --contradicts--> | 1 | 0.216 | IGNORE |
| `wiki/concepts/strategic-foresight.md` | enterprise-ai-adoption --supports--> | 1 | 0.215 | IGNORE |
| `wiki/sources/2026-05-19-garg-yc-internal-ai-agent-evolves-itself.md` | 2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees --contradicts--> | 1 | 0.214 | IGNORE |

**index.md / gap-expansion** (Step 5, one round)

Trigger: all three facets: the qmd stream (Dutch phrasing with 'zoek in de wiki naar' noise) returned mostly generic transformation pages; the core experimentation sources were absent. Method: grep of wiki/index.md for experiment|test-and-learn|sandbox|ambidext plus a corpus count of 'experiment' on pages outside the ledger.

| Page | why added |
|------|-----------|
| `wiki/sources/2025-11-24-sadun-wood-worklab-hard-to-become-ai-first-organization.md` | defines the Frontier Firm by its investment in strategic experimentation; strategy → buy-in → compliance sequence; build adoption into the experiment |
| `wiki/sources/2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about.md` | structured frontline experimentation → adaptation → scaling; four managerial problems; Skill–Will 2×2 |
| `wiki/sources/2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over.md` | the corpus's explicit case against dispersed experimentation, with budget arithmetic and IBM's volunteer-owner process portfolio |

Considered in the same round but not promoted: `sources/2026-01-21-deloitte-state-of-ai-in-the-enterprise-2026` (its scale-up figure is cited via W4); `sources/2026-09-30-lenk-karunakaran-stanford-hai-industry-conversation-instacart` (cited via W4); `sources/2026-06-12-dellacqua-cybernetic-teammate-field-experiment-genai-teamwork` (a research experiment on teams, not experimentation as a transformation method); `sources/2026-10-20-beauchene-bcg-so-what-ai-strategy-more-than-rollout` (strategy-vs-rollout; adjacent, not about experiments).

## 3. Ignore policy applied

- `off-facet` — semantically or structurally adjacent, but addresses none of the three facets. (33×)
- `redundant` — covers a claim already carried by a stronger USE page; the stronger page is named. (11×)
- `wrong-granularity` — entity catalogue card where the facet needs claims or cases. (7×)
- `below-threshold` — low fused score and no facet needs the page; the graph-only long tail. (26×)

Graph-only candidates (`qmd_rank: null`) needed a higher bar. Five of them were promoted to USE anyway, because they carry the experimentation content that the qmd hits lacked. `dutt-chatterji` has the most on-topic title in the ledger, but it is `redundant`: W3 reproduces its framework and cases and adds ten corroborating sources. No `contradicts` or `supersedes` edge changed the answer; no candidate carried `status: stale`.

## 4. Information ignored

| Page | reason-class | one-line reason |
|------|--------------|-----------------|
| `wiki/sources/2026-10-07-from-conversations-to-an-executive-learning-architecture-ep-22.md` | off-facet | qmd #2, but about a CIO-community conversation-recording prototype; no experiment-led transformation content (W2 itself excludes it from Sources consulted) |
| `wiki/sources/2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook.md` | off-facet | non-AI turnaround on performance culture; no experiments as a transformation instrument |
| `wiki/sources/2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026.md` | off-facet | skills and professional identity, not experimentation |
| `wiki/sources/2026-07-09-catlin-mckinsey-podcast-real-ai-advantage.md` | redundant | Rewired reinvention sequence already represented by W2 (Rewired layer) and W3 (four-step) |
| `wiki/entities/Ron%20Carucci.md` | wrong-granularity | entity card; his resistance-as-data lens is carried by W2 as the cross-cutting layer (note: accessed_at bump failed on the URL-encoded slug) |
| `wiki/sources/2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero.md` | off-facet | Dutch SME case, but its 'experiment' is a day-zero thought experiment, not organisational experimentation |
| `wiki/sources/2026-08-19-rohrer-goto-modern-enterprise-architecture-architecting-for-outcomes.md` | off-facet | enterprise architecture for outcomes; no experiment design |
| `wiki/sources/2026-06-25-carroll-stanford-gsb-making-organizational-culture-great.md` | off-facet | organisational culture in general; experimentation not addressed |
| `wiki/sources/2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees.md` | redundant | its 'experiment' hits are its own RCT on AI framing, summarised on W3 as anthropomorphizing lock-in |
| `wiki/sources/2026-05-07-ransbotham-augmented-learners.md` | redundant | test-and-learn / failure-tolerance traits already carried by W2 |
| `wiki/entities/MIT-Sloan-CIO-Symposium.md` | wrong-granularity | publisher entity card |
| `wiki/sources/2026-09-15-from-debate-to-inquiry-designing-conversations-worth-preserving-ep-21.md` | off-facet | designing executive conversations, not experiments |
| `wiki/entities/Allan-Tate.md` | wrong-granularity | person entity card |
| `wiki/entities/Irving-Wladawsky-Berger.md` | wrong-granularity | person entity card |
| `wiki/sources/2025-06-09-krakowski-human-centered-ai-field-experiment.md` | redundant | the field experiment's design and result are summarised on W3 (tenth-source corroboration), which is cited instead |
| `wiki/sources/2026-07-10-when-ai-becomes-common-organizational-capability-becomes-the-advantage-ep-16.md` | off-facet | organisational capability as differentiator; no experimentation mechanics |
| `wiki/sources/2026-05-21-allen-aws-london-exec-forum-agentic-team-structures.md` | redundant | pilot purgatory and the 5%-pattern prescription are summarised on W3 |
| `wiki/sources/2026-08-16-hill-bloomberg-leaders-ceo-skills-age-of-ai.md` | off-facet | CEO skills; experimentation not a theme |
| `wiki/entities/Bloomberg-Podcasts.md` | wrong-granularity | publisher entity card |
| `wiki/sources/2026-09-08-west-lacroix-zimmerman-mckinsey-why-strategy-needs-mobilization.md` | off-facet | strategy mobilisation; experimentation only in passing |
| `wiki/entities/Microsoft.md` | wrong-granularity | company entity card; the Microsoft case is taken from W9 |
| `wiki/sources/2026-03-31-roslansky-smith-tools-and-weapons-open-to-work.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-05-02-schoening-lennys-podcast-cultivating-agency-ai-era.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-07-14-khan-academy-ceo-the-real-ai-opportunity-is-in-boring-industries-sal-khan.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-08-10-miller-worklab-the-ai-shift-most-companies-didnt-see-coming.md` | redundant | frontier unit / double-path allocation already summarised on W1 and W3 |
| `wiki/sources/2026-03-28-nguyen-ai-adoption-toe-dynamic-capabilities.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-05-03-rewired-second-edition-sample.md` | redundant | sample-only ingest; the Rewired capability model is represented by W2 |
| `wiki/sources/2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china.md` | off-facet | demo-vs-revenue in China's agent market; not organisational experimentation |
| `wiki/sources/2026-08-03-mckinsey-agentic-ai-and-the-future-of-global-business-services.md` | redundant | materiality-threshold-first sequencing summarised on W3 and W1 |
| `wiki/entities/McKinsey-&-Company.md` | wrong-granularity | company entity card |
| `wiki/sources/2026-08-10-banholzer-laberge-mckinsey-how-to-maximize-competitive-advantage.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-10-27-catlin-durth-hamalainen-montard-mckinsey-ceo-agenda-agentic-age.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md` | off-facet | startup building from scratch, not transforming an existing organisation |
| `wiki/sources/2026-04-28-warner-wager-dynamic-capabilities-digital-transformation.md` | redundant | the microfoundation table is reproduced on W1 |
| `wiki/sources/2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook.md` | off-facet | YC's internal AI use; not experiment-led transformation |
| `wiki/sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company.md` | off-facet | 'pilot' here means customer pilots for an AI-native services startup, not internal experimentation |
| `wiki/sources/2025-07-02-joshi-venkatraman-fowler-expert-generalists.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-08-14-blomfield-yc-building-structuring-ai-native-company.md` | off-facet | structuring a new AI-native company |
| `wiki/concepts/ai-in-health-care.md` | off-facet | concept neighbour of enterprise-ai-adoption reached by a generic edge; covers a different topic than experimentation |
| `wiki/concepts/automation-vs-augmentation.md` | off-facet | automation/augmentation distinction, not experiment design |
| `wiki/concepts/ai-knowledge-hiding.md` | off-facet | concept neighbour of enterprise-ai-adoption reached by a generic edge; covers a different topic than experimentation |
| `wiki/concepts/ai-sovereignty.md` | off-facet | concept neighbour of enterprise-ai-adoption reached by a generic edge; covers a different topic than experimentation |
| `wiki/concepts/ai-employment-effects.md` | off-facet | concept neighbour of enterprise-ai-adoption reached by a generic edge; covers a different topic than experimentation |
| `wiki/concepts/agentic-web.md` | off-facet | concept neighbour of enterprise-ai-adoption reached by a generic edge; covers a different topic than experimentation |
| `wiki/concepts/jagged-frontier.md` | off-facet | task-level AI capability boundary; not about organisational experiments |
| `wiki/concepts/generative-ai.md` | off-facet | concept neighbour of enterprise-ai-adoption reached by a generic edge; covers a different topic than experimentation |
| `wiki/sources/2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/concepts/answer-engine-optimization.md` | off-facet | concept neighbour of enterprise-ai-adoption reached by a generic edge; covers a different topic than experimentation |
| `wiki/concepts/responsible-ai.md` | off-facet | concept neighbour of enterprise-ai-adoption reached by a generic edge; covers a different topic than experimentation |
| `wiki/concepts/open-source-ai.md` | off-facet | concept neighbour of enterprise-ai-adoption reached by a generic edge; covers a different topic than experimentation |
| `wiki/concepts/document-intelligence.md` | off-facet | concept neighbour of enterprise-ai-adoption reached by a generic edge; covers a different topic than experimentation |
| `wiki/concepts/founder-led-sales.md` | off-facet | concept neighbour of enterprise-ai-adoption reached by a generic edge; covers a different topic than experimentation |
| `wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-05-06-mit-ocw-future-of-mit-open-education.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/concepts/technology-adoption-theories.md` | off-facet | diffusion theory; IBM's diffusion-by-example is taken from W7 directly |
| `wiki/sources/2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-07-01-bello-mckinsey-podcast-serial-builder-advantage.md` | off-facet | corporate venture building outside the existing organisation, not experimentation inside it |
| `wiki/sources/2026-07-07-sinofsky-amble-a16z-software-in-the-age-of-agents.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/syntheses/ai-worker-maturity-levels.md` | off-facet | individual worker maturity levels, not organisational experiments |
| `wiki/sources/2026-05-02-dutt-chatterji-ai-experimentation-to-transformation.md` | redundant | title fits exactly, but the four-step framework and the Lowe's/FabricationCo cases are reproduced in full on W3, which also carries ten corroborating sources |
| `wiki/concepts/systems-thinking.md` | off-facet | concept neighbour of enterprise-ai-adoption reached by a generic edge; covers a different topic than experimentation |
| `wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-07-08-jensen-huang-why-companies-need-open-agent-systems.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-05-08-running-an-ai-native-engineering-org.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-06-11-mit-smr-agentic-ai-what-leaders-wish-they-knew-sooner.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-06-17-priest-atlantic-pwc-ai-agents-changing-business.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/sources/2026-08-11-ellmer-dhar-bcg-so-what-is-your-ai-rollout-built-to-fail.md` | redundant | behavioural change-failure points summarised on W4 (§Concentrate, then change the people) |
| `wiki/sources/2026-09-30-singh-botha-bloomberg-flow-engineering-ai-hardware-design.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |
| `wiki/concepts/strategic-foresight.md` | off-facet | sensing/scenario planning, not experimentation (also decayed: eff 0.49) |
| `wiki/sources/2026-05-19-garg-yc-internal-ai-agent-evolves-itself.md` | below-threshold | graph-only long-tail neighbour (fused < 0.45) reached via a generic supports/published-by edge; no experimentation-design content for any facet |

## 5. Information used

| Anchor | Page | type | effConf | origin | contribution |
|--------|------|------|---------|--------|--------------|
| W1 | `wiki/concepts/dynamic-capabilities.md` | concept | 0.90 | graph | model: rapid prototyping as a seizing microfoundation; double-path portfolio; concentration + pivot capacity |
| W2 | `wiki/syntheses/organizational-frameworks-for-ai-adoption.md` | synthesis | 0.86 | graph | model comparison: pilots as stage vs trap; organisational learning as upstream variable |
| W3 | `wiki/concepts/micro-productivity-trap.md` | concept | 0.90 | graph | four-step framework; worked cases; pilot purgatory; middle governance team; Krakowski field experiment |
| W4 | `wiki/concepts/enterprise-ai-adoption.md` | concept | 0.91 | qmd #8 | scale-up statistics (Deloitte, IBM); Kropp's big rocks; Mollick's leadership-lab-crowd; Instacart pioneers; law-firm framing; structured-vs-bottom-up tension |
| W5 | `wiki/sources/2025-11-24-sadun-wood-worklab-hard-to-become-ai-first-organization.md` | source | — | gap-expansion | model + practices: strategic boundaries, experimentation team, scientific method, late compliance metrics |
| W6 | `wiki/sources/2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about.md` | source | — | gap-expansion | model: structured frontline experimentation and its four managerial problems |
| W7 | `wiki/sources/2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over.md` | source | — | gap-expansion | practice + case: concentrate on 3–5 bets; IBM process portfolio; Watson negative case; Elk on pivoting |
| W8 | `wiki/sources/2026-06-18-dumra-mit-smr-dbs-everyone-an-innovator.md` | source | — | graph | case: DBS Bank innovation system |
| W9 | `wiki/sources/2026-07-27-george-wood-worklab-future-of-work-has-no-org-chart.md` | source | — | graph | case: Microsoft Copilot sales rollout; Camp Air; role huddles; continuous experimentation officers |

## 6. Answer-element map

| Anchor | Answer element (claim) | Wiki page(s) | Section / span used |
|--------|------------------------|--------------|---------------------|
| [W1] | Rapid prototyping (MVPs, lean startup, digital innovation lab) is a W&W digital-seizing microfoundation | [[concepts/dynamic-capabilities]] | ## Key claims › Microfoundations for digital transformation (table) |
| [W1] | Miller's double path: broad experimentation plus a 60–120-person frontier unit that hands winners back | [[concepts/dynamic-capabilities]] | ## Five video sources on the W&W cells, August 2026 |
| [W1] | Concentration and pivot capacity read as one strategic-agility capability | [[concepts/dynamic-capabilities]] | ## Concentration needs a capacity to pivot (added 2026-09-21) |
| [W2] | MIT CISR pilots-as-stage vs Bain pilots-as-trap; reconcile by passing through Stage 2 quickly | [[syntheses/organizational-frameworks-for-ai-adoption]] | ### Where they genuinely disagree; ## Lessons |
| [W2] | Augmented Learner traits (test-and-learn, failure tolerance, postmortems) map onto MIT CISR Stage 3 | [[syntheses/organizational-frameworks-for-ai-adoption]] | ### Where they genuinely disagree (last bullet) |
| [W3] | Bain/OpenAI four-step framework incl. prototyping culture in all business areas and outcomes + evals | [[concepts/micro-productivity-trap]] | ### The four-step framework for escape |
| [W3] | Lowe's (Mylow >2× conversion) and FabricationCo (14 use cases, ~$30M, 15× quotes, +10pp win rate) | [[concepts/micro-productivity-trap]] | ### Worked cases |
| [W3] | Pilot purgatory: pilots never connected to business decision flows | [[concepts/micro-productivity-trap]] | ### Eighth-source corroboration (Allen / AWS) |
| [W3] | ~3 in 10 pilots reach production, advisor's own unaudited index | [[concepts/micro-productivity-trap]] | ## Where the chain breaks (BBC AI Decoded) |
| [W3] | Hines-Pierce's middle governance team that propagates solved workflows | [[concepts/micro-productivity-trap]] | ## 70% people, 20% process, 10% technology |
| [W3] | Krakowski field experiment: untailored AI gradually lowered market share (N=72 pharma sales experts) | [[concepts/micro-productivity-trap]] | ### Tenth-source corroboration (Krakowski et al.) |
| [W4] | Deloitte 25% moved ≥40% of experiments to production; IBM 16% scaled enterprise-wide | [[concepts/enterprise-ai-adoption]] | ## Maturity re-measured, and new value instruments, 2025–2026 |
| [W4] | Kropp (BCG X): three big rocks instead of 100 initiatives | [[concepts/enterprise-ai-adoption]] | ## Access without use: two October-2026 accounts |
| [W4] | Instacart pioneers explain ~23% of usage growth; law-firm framing decides whether staff keep experimenting | [[concepts/enterprise-ai-adoption]] | ## Access without use: two October-2026 accounts |
| [W4] | Mollick's leadership, lab and crowd | [[concepts/enterprise-ai-adoption]] | ## Use outruns governance, and what to measure instead |
| [W4] | Tension between structured experimentation and bottom-up adoption, possibly a population difference | [[concepts/enterprise-ai-adoption]] | ## The Frontier Firm initiative's early insights |
| [W5] | Strategy → buy-in → compliance; experiments within 1–3 strategic axes; 'too much experimentation' | [[sources/2025-11-24-sadun-wood-worklab-hard-to-become-ai-first-organization]] | ### Three stages, with strategy first |
| [W5] | Build adoption into the experiment ('foreign object'); team composition; scientific method; compliance metrics backfire | [[sources/2025-11-24-sadun-wood-worklab-hard-to-become-ai-first-organization]] | ### Who runs the experiments, and how they reach scale; ### Reskilling |
| [W6] | Structured frontline experimentation → adaptation → scaling; four managerial problems; Skill–Will 2×2; no self-discovery | [[sources/2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about]] | ## Key claims: the early insights |
| [W6] | Early insights are pre-publication bullets without data | [[sources/2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about]] | ## What was actually ingested; ## Scope and reliability |
| [W7] | $200M over 100 experiments = 3–5 people each; pick three to five things | [[sources/2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over]] | ## The shift from experimentation to scale |
| [W7] | IBM's ~200-process portfolio, volunteer owners, diffusion by example, ~60 done; tension with 'three to five' | [[sources/2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over]] | ## How IBM chose where to scale |
| [W7] | Watson as negative case (monoliths, health) | [[sources/2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over]] | ## What IBM got wrong with Watson |
| [W7] | Elk: admit a mistake at 6 months rather than a mediocre result at 3 years; self-reported figures | [[sources/2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over]] | ## Three pieces of advice, and Elk on pivoting; ## Source quality |
| [W8] | DBS innovation pyramid, 20% scorecard, QPR + slush fund, 48-hour builds, every MD built an agent, retrospective business case | [[sources/2026-06-18-dumra-mit-smr-dbs-everyone-an-innovator]] | ## TL;DR items 4–6 |
| [W9] | Copilot sales rollout failed as product launch; Camp Air; role huddles; top down, bottom up; customers moving to three end-to-end processes | [[sources/2026-07-27-george-wood-worklab-future-of-work-has-no-org-chart]] | ### A business transformation, not a product launch; ### Teams, not individuals |
| [W9] | Adoption → behaviour → outcome measurement chain; leaders as continuous experimentation officers; no figures, own channel | [[sources/2026-07-27-george-wood-worklab-future-of-work-has-no-org-chart]] | ### Capability Add; ### The Frontier Firm, roles and leaders; ## Scope and reliability |

## 7. Final answer

**Kort antwoord.** De wiki heeft geen aparte conceptpagina over experimenteren. Het onderwerp komt wel terug op negen pagina's, en die vertellen een consistent verhaal. Organisaties moeten experimenteren om te ontdekken waar AI waarde oplevert [W6][W5]. Toch is ongericht experimenteren de bekendste reden dat transformaties vastlopen: veel kleine pilots, waarvan weinig de productie haalt [W7][W3][W4]. De bruikbare modellen en praktijken gaan daarom vooral over vier dingen: experimenten begrenzen, de experimenteerders bewust kiezen, opschaling vanaf het begin inbouwen en meten op uitkomst [W5][W6][W3].

### 1. Modellen

| Model | Wat het zegt over experimenteren | Anker |
|---|---|---|
| Warner & Wäger, dynamic capabilities | *Rapid prototyping* (MVP's, lean startup, digitaal innovatielab) is een van de drie microfundamenten van *digital seizing*, naast het balanceren van een digitaal portfolio en strategische wendbaarheid. | [W1] |
| Frontier Firm-volgorde (Sadun, HBS) | Eerst strategie, die de grenzen voor experimenten bepaalt (één tot drie strategische assen). Dan draagvlak en verspreiding. Pas daarna compliance en metrics. | [W5] |
| Frontier Firm AI Initiative (HBS met Microsoft) | Eerst gestructureerd experimenteren op de werkvloer, dan aanpassen, dan opschalen. Vier managementvragen: waarop experimenteer je, met wie, hoe leg je het geleerde vast, welke prikkels zijn nodig voor volledige adoptie. Daarbij de Skill–Will-matrix (Evangelists, Skeptics, Learners, Resisters). | [W6] |
| Bain/OpenAI, vier stappen (Dutt et al.) | Beperk je tot 4–5 domeinen, herontwerp workflows over afdelingen heen, betrek de mensen die het werk nu doen (een prototypingcultuur in alle bedrijfsonderdelen, niet alleen IT) en meet uitkomsten tegen een baseline zonder AI, plus evals. | [W3] |
| MIT CISR tegenover Bain | MIT CISR ziet pilots als een fase (fase 2, *Build pilots and capabilities*); test-and-learn is een kenmerk van fase 3. Bain ziet pilots als een val. De synthese verzoent ze door fase 2 te lezen als een fase die je snel doorloopt. | [W2] |
| Augmented Learners (Ransbotham/Kiron) | Het leervermogen van de organisatie (test-and-learn, fouttolerantie, postmortems, geleerde lessen vastleggen) bepaalt of de stap naar fase 3 lukt. | [W2] |
| Portfoliovormen | DBS' innovatiepiramide met vier lagen [W8]. Millers *double path*: brede experimenten voor iedereen plus een frontier unit van 60–120 mensen met een hoger tokenbudget, die winnaars teruggeeft aan de organisatie [W1]. Mollicks *leadership, lab and crowd* [W4]. | [W8][W1][W4] |

### 2. Best practices

1. **Begrens en concentreer.** Krishna (IBM): $200M verdeeld over 100 experimenten betekent 3–5 mensen per experiment en geen plan om op te schalen; *"pick three, four, five things which you can scale like crazy"* [W7]. Sadun: experimenteer binnen één tot drie strategische assen, want *"there can be also too much experimentation"* [W5]. Microsoft hoort klanten zeggen dat ze van *"lots and lots of pilots"* overstappen op drie end-to-end-processen [W9]. Kropp (BCG X) noemt drie *big rocks* in plaats van 100 initiatieven [W4].
2. **Concentratie vraagt het vermogen om bij te sturen.** Sarah Elk (Bain): een fout na zes maanden toegeven is beter dan na drie jaar een middelmatig resultaat [W7]. De wiki leest dat als strategische wendbaarheid: concentreren en kunnen pivoteren zijn samen één vermogen [W1].
3. **Bouw opschaling in vanaf dag één.** Sadun: experimenten die los van de rest van de organisatie draaiden, werden bij opschaling afgestoten *"as if it was a foreign object"*; redeneer terug vanaf massa-adoptie [W5]. Allen (AWS): pilots die nooit aan echte beslisstromen zijn gekoppeld, belanden in *pilot purgatory* [W3]. HBS: kies de scope *"wide enough for discovery, narrow enough for scaling"* [W6]. Hines-Pierce richtte een apart middenteam op dat ervoor zorgt dat een opgeloste workflow overal wordt gebruikt [W3].
4. **Laat het niet aan zelfontdekking over.** HBS: *"Do not assume that employees would self-discover uses without specific guidance"* [W6]. Microsofts eerste Copilot-uitrol aan de salesorganisatie, opgezet als productlancering, mislukte: mensen probeerden het en stopten ermee [W9]. De wiki noteert hier een spanning met bottom-up-verhalen; het verschil zit mogelijk in de populatie (een enthousiaste vrijwilliger tegenover de hele werkvloer) [W4].
5. **Kies de experimenteerders bewust.** Kies mensen die onzekerheid en tijdelijke onproductiviteit verdragen [W6], en stel een team samen met technische kennis, kennis van de gebruiker en zicht op de te verwachten weerstand [W5]. Bij Instacart trokken *pioneers* met gezag en taakkennis het gebruik in hun team het sterkst omhoog [W4]. IBM liet proceseigenaren zich vrijwillig melden; de volgende golf kwam *"because they saw what their friends had done"* [W7].
6. **Meet op uitkomst, en meet compliance niet te vroeg.** Compliance-metrics invoeren terwijl nieuwe processen nog worden uitgevonden *"can potentially backfire"* [W5]. Microsoft meet een keten: adoptie, dan gedragsverandering, dan bedrijfsresultaat (in sales: omzet per verkoper) [W9]. DBS laat grote gokken en Horizon-3-proposities starten zonder businesscase; die wordt een jaar na lancering geschreven [W8].
7. **Werk als een wetenschapper.** *"It's not just enough to do a pilot. You want to have hypothesis. You want to have measurement and you want to learn."* [W5]
8. **Framing en de rol van leiders.** In één advocatenkantoor stopten paralegals met experimenteren toen de tool als productiviteitsinstrument werd gepresenteerd; in een andere divisie, waar de manager vroeg wat ze graag anders zouden doen, gingen ze het gebruiken voor juridisch onderzoek [W4]. Katy George (Microsoft): leiders moeten *"continuous experimentation officers"* worden [W9].

### 3. Cases

- **DBS Bank** (~39.000 medewerkers): een innovatiepiramide met grote gokken, Horizon 3, customer journeys en een *entrepreneurs*-laag met ~120–130 lopende initiatieven; 20% van elke scorecard gaat over transformatie; een kwartaalherziening plus een *slush fund*; 48-uursbuilds, en op de leiderschapsconferentie bouwde elke MD ter plekke een agent [W8].
- **Microsoft**: de Copilot-uitrol voor sales mislukte als productlancering en werd herstart als bedrijfstransformatie, met Camp Air (een bootcamp voor hele teams) en wekelijkse huddles per rol. Het patroon uit 100 interne cases: *top down, bottom up* [W9].
- **IBM**: ~200 processen van elk ~$100M; eerst vijf vrijwillige eigenaren, ~60 processen klaar in 2,5 jaar, 70 staan klaar, 30–40 zijn *"recalcitrant"*. Watson is de negatieve case: monolithische applicaties in een sector (zorg) waar IBM klant en toezichthouder niet kende [W7].
- **Lowe's en FabricationCo** (Bain-cases): Mylow verdubbelde ruim de online conversie; FabricationCo vond 14 use cases, ~$30M extra winst, offertes ~15× sneller en +10 procentpunt win-rate binnen drie maanden [W3].
- **Krakowski et al.**: een veldexperiment bij 72 Scandinavische farmaceutische verkopers. AI die niet op de gebruiker was afgestemd, liet het marktaandeel geleidelijk dalen ten opzichte van het oude systeem [W3]. Dit is het enige peer-reviewed experiment in deze set, en een voorbeeld van wat een gecontroleerd experiment kan blootleggen voordat er breed wordt uitgerold.
- **Instacart en een advocatenkantoor** (Stanford HAI): de eerste zware gebruiker in een team verklaart ~23% van de gebruiksgroei; de framing door de manager bepaalt of mensen blijven experimenteren [W4].

**Hoe vaak lukt de stap van experiment naar productie?** Deloitte: 25% van de organisaties bracht 40% of meer van hun experimenten naar productie. IBM's CEO-studie: 16% van de AI-initiatieven is enterprise-breed opgeschaald [W4]. Een adviseur meldt dat ongeveer 3 op de 10 pilots productie halen, op eigen, niet-geaudite data [W3].

### Kanttekeningen

- **Het bewijs is overwegend praktijk- en leveranciersmateriaal.** Microsoft vertelt over zichzelf op het eigen kanaal, IBM's cijfers zijn zelfgerapporteerd en Bain verkoopt de transformatie die het aanraadt [W9][W7]. De HBS-inzichten zijn voorpublicaties zonder data [W6].
- **Twee echte spanningen.** Concentreren tegenover breed ontdekken: Krishna en Sadun willen begrenzen, HBS vraagt brede experimenten op de werkvloer [W7][W5][W6]. En gestructureerd tegenover bottom-up [W4]; Microsofts *top down, bottom up* combineert beide [W9]. IBM's eigen ~60 processen passen bovendien niet letterlijk bij "drie tot vijf dingen" [W7].
- **Gat in de wiki.** Er is geen conceptpagina over experimenteren in organisaties (experimentontwerp, lean startup, A/B-testen). Het materiaal staat verspreid over [W1]–[W4]. Een conceptpagina zou het bundelen.

**Bronnen (USE):**
[W1] [[dynamic-capabilities|Dynamic capabilities]] ·
[W2] [[organizational-frameworks-for-ai-adoption|Synthese: organisatieframeworks voor AI-adoptie]] ·
[W3] [[micro-productivity-trap|Micro-productivity trap]] ·
[W4] [[enterprise-ai-adoption|Enterprise AI adoption]] ·
[W5] [[2025-11-24-sadun-wood-worklab-hard-to-become-ai-first-organization|Sadun, WorkLab 2025]] ·
[W6] [[2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about|HBS AI Institute, Frontier Firm AI Initiative]] ·
[W7] [[2026-09-15-krishna-bain-winning-with-ai-era-of-experimentation-is-over|Krishna (IBM), Bain 2026]] ·
[W8] [[2026-06-18-dumra-mit-smr-dbs-everyone-an-innovator|Dumra, DBS Bank, MIT SMR 2026]] ·
[W9] [[2026-07-27-george-wood-worklab-future-of-work-has-no-org-chart|George, Microsoft WorkLab 2026]]

## 8. Trace artifact

Machine-readable provenance: [`2026-11-12-experimenten-organisatietransformatie-query-trace.json`](2026-11-12-experimenten-organisatietransformatie-query-trace.json)

Run notes:
- USE set is 9 pages (guideline 4–8): three facets (models, practices, cases) each needed distinct pages.
- Five USE pages were graph-only or gap-expansion; concepts/syntheses among them need a manual accessed_at bump (Step 8).
- wiki-retrieve's bump step failed on 'Ron%20Carucci': the graph slug is URL-encoded and bump-accessed.mjs does not decode it. Tooling bug, not a content issue.
- Five entity paths in the ledger (MIT-Sloan-CIO-Symposium, Allan-Tate, Irving-Wladawsky-Berger, Bloomberg-Podcasts, McKinsey-&-Company) do not exist under those filenames; graph slug vs filename mismatch. All IGNORE (wrong-granularity).
