---
type: entity
kind: organization
aliases: ["Microsoft", "Microsoft Corporation", "Microsoft Visual Studio", "MSFT"]
tags: [microsoft, azure, azure-devops, visual-studio-code, vs-code, github-parent, copilot, responsible-ai, azure-sre-agent, openai-partner, developer-tools, agentic-devops]
website: "https://microsoft.com"
confidence: 0.85
last_confirmed: "2026-10-25"
accessed_at: "2026-10-25"
source_count: 17
relationships:
  - type: employs
    target: GitHub
    via: "GitHub has operated as a Microsoft subsidiary since the 2018 acquisition"
  - type: published-by
    target: 2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life
    via: "Published on the Microsoft Visual Studio YouTube channel; demos Azure DevOps, VS Code, the Microsoft responsible-AI pipeline, and the Azure SRE Agent (22 Dec 2025)"
  - type: authored-by
    target: 2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm
    via: "CEO Satya Nadella articulating Microsoft's enterprise-AI worldview post-Build 2026 — token capital, the hill-climbing machine, Agent 365, Foundry asserts, the agentic development environment (5 Jun 2026)"
  - type: published-by
    target: 2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026
    via: "Published on Microsoft's WorkLab podcast — host Molly Wood interviews LinkedIn's Aneesh Raman on AI-era career and organizational identity (29 Jun 2026)"
  - type: published-by
    target: 2026-08-10-miller-worklab-the-ai-shift-most-companies-didnt-see-coming
    via: "Published on Microsoft's WorkLab podcast, recorded live at the Copilot Summit — Molly Wood interviews advisor Allie K. Miller on the multi-agent third shift, the frontier unit, and 'AI is not a tool' (10 Aug 2026)"
  - type: published-by
    target: 2025-11-24-sadun-wood-worklab-hard-to-become-ai-first-organization
    via: "Published on Microsoft's WorkLab podcast, recorded at Harvard Business School — Molly Wood interviews Raffaella Sadun on the Frontier Firm, strategic experimentation and reskilling (24 Nov 2025)"
  - type: published-by
    target: 2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about
    via: "Collaborator in the Frontier Firm AI Initiative hosted by the HBS AI Institute; the page is the institute's, Microsoft is the named partner (captured 15 Oct 2026)"
  - type: published-by
    target: 2025-12-16-diasio-wood-worklab-agentic-ai-corporate-ladder
    via: "Published on Microsoft's WorkLab podcast — Molly Wood interviews EY's Dan Diasio on managers of agents on day one, mindset/skill set/tool set, and the billable hour (16 Dec 2025)"
---

# Microsoft

**Microsoft** is the cloud-and-developer-tools giant that owns [[GitHub]] (since 2018), partners deeply with [[OpenAI]], and ships the developer surfaces central to the wiki's agentic-coding corpus: **Azure**, **Azure DevOps**, **Visual Studio Code**, and the **responsible-AI pipeline** that proxies Copilot requests. Promoted to an entity page on 9 June 2026 via **cross-page-presence promotion** (precedent: [[LangChain]], [[Andrej Karpathy]]): Microsoft is a plain-text mention across ~21 source pages, and the [[2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life|Agentic DevOps keynote]] — published on the **Microsoft Visual Studio** channel — is the first source centred on Microsoft's own agentic developer tooling.

> **Backlinking note.** `source_count` counts formal inbound source-page wikilinks (**7** after the 2026-10-15 ingests), not ~21 (plain-text mentions). Backfilling the historical mentions into wikilinks is a deferred lint cleanup.

## Role in the wiki

Microsoft is the **platform-and-cloud vantage** on agentic development — the vendor whose IDE (VS Code), cloud (Azure), ALM tooling (Azure DevOps), and safety layer (responsible-AI pipeline) host the agentic workflows that [[GitHub]]'s Copilot drives. The channel-author convention applies: *Microsoft Visual Studio* (the YouTube channel) maps to **Microsoft** as the publishing entity.

### Visual Studio Code

Microsoft's cross-platform editor — the keynote's hub for agentic development. The **four Copilot interaction modes**: **Ask / Edit / Agent / Plan** (*Plan* is the newest — the agent states its implementation plan before acting, bounding the over-autonomy failure mode). Instructions files encode house rules + exemplars; agents run locally (CPU/GPU) or push to GitHub's cloud; profiles swap toolsets; **Ollama + the Continue extension** enable offline/local-model agents.

### Azure DevOps + the responsible-AI pipeline

Copilot agents are coming to **Azure DevOps** (private preview) — but routed through [[GitHub]] (*"you still have to link it up to GitHub"*). Every Copilot request passes through **Microsoft's responsible-AI pipeline**, which validates input and the returned code (security vulnerabilities, NSFW) **even when the chosen model is third-party** ([[Anthropic]]/[[Google]]) — sending only enough across the wire and checking the response before it reaches the developer, in milliseconds. See [[responsible-ai]].

### Azure SRE Agent

Microsoft's autonomous cloud-monitoring + incident-response agent (preview). Scope it to an Azure resource group; it performs incident management, can be permissioned to **autonomously remediate** certain conditions, and files health/security reports — framed as *"a site reliability engineer on my team."* A worked instance of an [[agentic-engineering|autonomous agent]] in the IT-operations (not just coding) domain.

### OpenAI partnership

Microsoft hosts and routes [[OpenAI]] models (and now the Codex agent inside Copilot), alongside [[Anthropic]] and [[Google]] models. The keynote frames model choice as a developer decision, with Microsoft's proxy doing the safety validation regardless of model.

### Satya Nadella / Build 2026 — the CEO-worldview source

The [[2026-06-05-nadella-hoffman-possible-ai-future-of-the-firm|Nadella / Possible interview]] (5 Jun 2026, post-Build 2026) is the wiki's first **platform-CEO worldview** source and Microsoft's second formal inbound source. Nadella frames *AI as the future of the firm* (not a technology), introduces **token capital** as the firm-level asset that compounds alongside human capital, and lays out Microsoft's enterprise-AI stack as the manageability/security answer: the **hill-climbing machine** (evals/objectives as the new IP), **Agent 365** (agent identity/sandbox/policy/observability via Entra/Defender/Purview — see [[responsible-ai]]), **Foundry asserts** (runtime boundary enforcement — see [[agent-harness]]), and the **agentic development environment** (the GitHub app as an inbox of agents with Canvas, for *micro-steering of macro-delegation*). The dictum *"don't use frontier models for non-frontier problems"* anchors his token-efficiency argument. Co-designed silicon (**Maya**, **Cobalt**) and the *platform-company-defined-by-value-created-on-top* trust doctrine round out the strategy.

### WorkLab podcast — the owned-media future-of-work vantage

Microsoft's **WorkLab** podcast (host Molly Wood) is a separate publishing channel from *Microsoft Visual Studio* — owned media focused on the future of work broadly, not Microsoft's own developer tooling. [[2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026|Raman/Wood (29 Jun 2026)]] is the wiki's first WorkLab source: an interview with LinkedIn's Chief Economic Opportunity Officer Aneesh Raman on AI-era career and organizational identity ("onlyness," the 5 C's, the electricity-bolt-on-failure analogy). The channel-author convention applies here as it does for *Microsoft Visual Studio*: WorkLab maps to **Microsoft** as publishing entity, with **LinkedIn** (a Microsoft subsidiary since 2016) as the guest's employer — a third, futures-of-work-focused channel alongside the developer-tooling (*Agentic DevOps*) and CEO-worldview (Nadella/*Possible*) vantages already held.

WorkLab's second wiki source, [[2026-08-10-miller-worklab-the-ai-shift-most-companies-didnt-see-coming|Miller/Wood (10 Aug 2026)]], is a live recording from the **Copilot Summit** — so the venue as well as the channel is Microsoft's, and the audience is Microsoft customers. Guest **Allie K. Miller** (Open Machine) is an independent advisor rather than an employee, but two of the statistics she cites are Microsoft first-party research: an 1,800-employee study finding a 22-point lift in critical thinking and a 30-point lift in trust of agentic AI where managers model AI use themselves, and the **Work Trend Index** split in which 65% of AI users fear falling behind while 45% say it feels safer to focus on current goals than to redesign their work. The episode's durable contributions are structural rather than statistical — the **frontier unit** (a 60–120-person cross-disciplinary experimentation group on a higher per-head token budget), the **Gremlin-mode** ladder of usage depth, and the **context layer** prescription ("make your whole company queryable").

WorkLab's third wiki source, [[2025-11-24-sadun-wood-worklab-hard-to-become-ai-first-organization|Sadun/Wood (24 Nov 2025)]], was recorded at Harvard Business School and promotes the **Frontier Firm AI Initiative**, a research collaboration between Microsoft and HBS for which Sadun is a research leader. "Frontier Firm" is Microsoft's own term for the AI-first organisation, so here the publisher is a partner in the research being discussed. The initiative's own page, [[2026-10-15-hbs-ai-institute-frontier-firm-ai-initiative-about|hosted by the HBS AI Institute]], describes the collaboration: member firms run experiments with Harvard and Microsoft researchers, starting with sales, IT and finance.

### Microsoft Advertising — the answer-engine owner selling into the shift

[[2026-10-14-longo-marchiaro-hubspot-unbound-ai-transforming-search|Longo & Marchiaro (HubSpot UNBOUND, Oct 2026)]] gives Microsoft's view as the owner of a search engine (Bing, one billion monthly users) and an answer engine (Copilot): three eras of the web running at once, paid placement (Performance Max, AI Max) on conversational queries and AI surfaces, and Microsoft Clarity's free AI-visibility metrics (citation rate, share of authority by domain). The session launched the first HubSpot–Microsoft Advertising integration. Its statistics are mostly Microsoft first-party research.

## Open questions

- **Full backlinking.** ~21 plain-text "Microsoft" mentions across the corpus await promotion to wikilinks.
- **Product sub-pages.** Azure, VS Code, Azure DevOps, and the Azure SRE Agent are Dangling product mentions; promote on a second source each.
- **The Microsoft–OpenAI commercial relationship.** Referenced but not characterised; a dedicated source would let the wiki track it properly.

## Mentioned in

- [[2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life]] — the promotion trigger: VS Code modes, Azure DevOps, responsible-AI pipeline, Azure SRE Agent.
- [[GitHub]] — Microsoft subsidiary; the developer-platform half of the keynote.
- [[2026-06-29-raman-wood-worklab-job-titles-dont-matter-2026]] — WorkLab podcast; Aneesh Raman (LinkedIn) on AI-era career and organizational identity.

## Its own transformation, told by its workforce-transformation lead (added 2026-10-17)

[[2026-07-27-george-wood-worklab-future-of-work-has-no-org-chart|Katy George on WorkLab (July 2026)]]: George, corporate vice president of workforce transformation, describes Microsoft's internal practice. The first Copilot rollout to its own sales force was run *"as a typical product launch"* and people *"tried it and then they stopped using it"*; Harvard Business School wrote it up as a case in the Frontier Firm research. What replaced it: outcome goals, and redesign of tech, process and people with the people who do the work. Programmes named: **Camp Air**, a bootcamp that whole engineering teams attend together, and weekly **role-based huddles** in sales, taught practitioner to practitioner. Her team has written **100 internal case studies** of AI transformation, whose common pattern is top-down goals with bottom-up citizen-developer builds. The internal audit team is her example of **"Capability Add"**: *"every internal audit now delivers proactive risk identification."* Microsoft's own account, on its own channel.

## Tools and Weapons, and two earlier WorkLab episodes (added 2026-10-25)

- [[2026-03-31-roslansky-smith-tools-and-weapons-open-to-work|Roslansky (LinkedIn) on Tools and Weapons (Mar 2026)]]: Brad Smith, Microsoft's vice chair and president, interviews LinkedIn's CEO about *Open to Work*; LinkedIn's builder role and associate-builder entry route; Smith's *"schism"* between AI that outperforms people and AI that empowers them, with Microsoft on the second side.
- [[2025-10-30-bornet-wood-worklab-ai-agents-leaders|Bornet on WorkLab (Oct 2025)]]: a WorkLab episode from October 2025 on agents, the Frontier Firm's traits, and the Work Trend Index finding that more than 80% of leaders plan to use agents to fill capacity gaps.
- [[2025-12-16-diasio-wood-worklab-agentic-ai-corporate-ladder|Diasio on WorkLab (Dec 2025)]]: [[EY]]'s Global Consulting AI Leader, introduced as a member of the inaugural class of the Frontier Firm initiative that Microsoft runs with Harvard. New joiners as *"managers on day one"* of agents, mindset–skill set–tool set, and the billable hour as EY's hardest change.
