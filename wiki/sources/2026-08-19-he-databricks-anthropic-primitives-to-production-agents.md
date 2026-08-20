---
type: source
kind: video
title: "From Primitives to Production: How Anthropic Builds Agents"
author: ["Databricks"]
publisher: "Databricks (YouTube channel) — recorded at the Agentic + AI Observability Meetup, San Francisco, 9 April 2026; speaker Isabella He (Applied AI, Anthropic)"
url: "https://www.youtube.com/watch?v=8pzHCfsSaYQ"
date_published: 2026-08-19
date_ingested: 2026-08-20
length: "~25:20 minutes (transcript ~194 segments; auto-generated captions, ASR-cleaned) — includes a ~7-minute live SRE-agent demo"
raw: "../../raw/videos/from-primitives-to-production-how-anthropic-builds-agents.md"
tags: [isabella-he, anthropic, databricks, agentic-ai-observability-meetup, claude-code, claude-agent-sdk, managed-agents, agent-skills, progressive-disclosure, subagents, context-engineering, compaction, tool-result-clearing, hooks, permissions, sandboxing, mcp, evals, sre-agent, incident-response, postmortem, pagerduty, core-primitives, first-party-vendor-account]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
  - digital-transforming/improving-digital-maturity
relationships:
  - type: supports
    target: 2026-05-07-anthropic-managed-agents-decoupling-brain-hands
    via: "same vendor, same product line, four months apart — and this talk closes with Managed Agents as the deployment layer the earlier announcement introduced. He describes it in exactly the brain/hands terms the wiki recorded: Managed Agents *\"abstracts away all the work that we didn't talk about today, which is deployment and hosting of an agent… how do you make sure everything is containerized and make sure that the access to computer is safe and deployed in a virtual machine.\"* The value here is that she reaches it at the END of a talk whose first 24 minutes are about primitives, so the announcement's claim is placed in its engineering context rather than stated as a launch"
    confidence: 0.8
  - type: supports
    target: 2026-05-04-rethinking-agents-harness-is-all-you-need
    via: "a first-party statement of the subtraction principle and the general-purpose-harness claim that the Prompt Engineering video established empirically. He: *\"a couple of months maybe around a year ago we thought about agents as needing very specialized domains… you might need almost an entire new harness for something like a research agent or a customer service agent… Where we are now is that instead of breaking down agents by domain, we actually see that it's more effective if we just think about agents as this really almost general purpose\"* — i.e. one harness plus swapped context, not one harness per domain. The empirical source shows harnesses transfer across models; this shows the vendor claiming they transfer across domains"
    confidence: 0.7
  - type: supports
    target: 2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness
    via: "two vendor accounts of the same definition, five weeks apart and from competitors. Baugues (Google): *an agent is an LLM with tools running in a loop to accomplish a goal*, attributed to Simon Willison. He (Anthropic): *\"what an agent is, is it is a large language model, it is then put into a loop, it uses tools at its disposal, and it has a particular goal that it's optimizing towards.\"* The four clauses are identical and the phrasing is near-identical. He adds the prior states the definition is defined against — single-LLM features, then code-orchestrated workflows — which Baugues does not"
    confidence: 0.75
  - type: supports
    target: 2026-08-11-ummadisetti-langchain-toyota-deep-agents-rd-research
    via: "the vendor prescription and a customer instance of it, on the same mechanism. He argues skills are how domain expertise enters a general-purpose harness without polluting the system prompt — *\"skills let you do is essentially have those instructions only loaded in when it's relevant to the prompt\"*; Ummadisetti describes Toyota's Enterprise AI group authoring per-function curated skills (branding, research, manufacturing, supply chain) as the carrier of institutional knowledge. Same primitive, one side stating the design intent and the other reporting a deployment — though note both are vendor-channel content and neither measures anything"
    confidence: 0.65
---

# He — From Primitives to Production: How Anthropic Builds Agents

> Recorded at: Agentic + AI Observability Meetup | SF | April 9, 2026
>
> Speaker: Isabella He (Member of Technical Staff, Anthropic)
>
> Session: ​Skills and Security
>
> Large Language Models (LLMs) are evolving from simple "tokens in/out" processors into autonomous agents. This session breaks down the engineering principles and frameworks used at Anthropic to build agents capable of navigating complex environments without human-encoded logic. The talk highlights the transition from orchestrated workflows to modern agentic systems, featuring tools like Claude Code and the Claude Agent SDK.

## TL;DR

A **~25-minute meetup talk** by **Isabella He** of **[[Anthropic]]**'s Applied AI team, delivered at the Agentic + AI Observability Meetup in San Francisco on **9 April 2026** and published by **Databricks** on 19 August 2026. She describes her role as split: half internal (*"I've contributed to Claude Code designer news/init experience… I work on context engineering, so things like compaction and tool result clearing"*), half working with Anthropic's big-tech and startup customers. The talk is explicitly a **playbook** — *"I want everyone to hopefully leave with just a little bit of a playbook of, if you were to leave this room, how would you actually go and build agents?"* — and closes with a live incident-response demo.

**1. The three-stage progression, and what "agent" is defined against.** Single-LLM features (tokens in, tokens out) → **workflows** (*"LLMs essentially orchestrated by code… you chain together different LLM calls orchestrated by code. But this was still very deterministic, relying on human-encoded logic to guide LLMs around where they were going"*) → **agents** (*"where LLMs are actually deciding their own trajectories… able to look at complex environments, look at the tools it has at its disposal, and essentially work in a loop in order to strive towards a particular goal without deterministic elements encoded in"*). The definition itself: *"what an agent is is it is a large language model, it is then put into a loop, it uses tools at its disposal, and it has a particular goal that it's optimizing towards."*

**2. Claude Code's mechanism, stated concretely.** *"Claude Code has access to about 14 or 15 tools, things like bash, edit, grep, glob. And these are actually tools that you all have at your disposal in your terminal as a developer as well."* The comparison she draws is against the prior art: *"What a lot of agents did before Claude Code was essentially semantic search over a particular file, which is looking for things like keyword phrasing, and you had to feed it a specific file to edit. But Claude Code instead essentially has the same set of tools that you have access to as a developer… You can run Claude Code on a codebase that is millions or hundreds of millions lines of code."* This is a **retrieval-architecture claim** — developer-grade navigation tools replacing embedding search — and it is a rare on-the-record statement of it from the vendor.

**3. The domain-specialisation reversal — the talk's most transferable claim.** *"A couple of months, maybe around a year ago, we thought about agents as needing very specialized domains across different expertise areas… We used to think you might need almost an entire new harness for something like a research agent or a customer service agent or a site reliability agent. But… with every new model that we see, we can unlock a whole new set of capabilities. So instead of breaking down agents by domain, we actually see that it's more effective if we just think about agents as this really almost general purpose but with access to different tools that you can then tailor to specific domains."* The core primitives she names as domain-invariant: **code execution, file system, web search, to-do list**. The consequence: *"Claude Code could power a customer support agent. It could power an incident response agent."*

**4. What is actually missing between generic Claude Code and a purpose-built agent.** Her answer is one thing: *"The key thing that is actually missing is domain expertise."* Four mechanisms for supplying it —

- **Skills** — *"packaged instructions that you can give to Claude. And the key thing here is that they're progressively loaded."* Her worked example is the anti-pattern: for a customer support agent, ticket-opening instructions *"would pollute the context and that would let you read those useless instructions for a customer asking any other question into that system prompt instruction on every single prompt to Claude. Instead, what skills let you do is essentially have those instructions only loaded in when it's relevant."* Skills also carry executables — she cites the open-source PowerPoint skill, which *"other than instructing Claude how to create PowerPoints, it actually also has scripts to edit the actual PowerPoint files itself."*
- **MCP servers** — *"our default way to talk to external systems"*, and specifically for *taking action* in them.
- **Subagents** — framed primarily as **context isolation**, not delegation: *"a way to kick off a parallel workstream for Claude but also have their own context window… You might launch a bunch of different subagents to read different aspects of the document. They can each write their own version of writing summaries of that portion of the document, then report back to a main agent. What this does, it essentially prevents the main agent from having to read in that entire document into context."* She adds a model-tiering pattern: *"the Claude Code default subagent for the explore mode is a Haiku subagent… then report back to maybe a more intelligent model like an Opus or Sonnet."*
- **System prompts and custom tools.**

**5. Her decision rule for skill vs. MCP vs. subagent** — asked-and-answered in the talk because *"I know there's some confusion around, hey, when do I use a skill versus MCP versus subagent"*: **skills** for *"procedural knowledge that you always want to persist and you want to call on"* (her example: Claude Code's own front-end design skill, invoked whenever Claude does front-end work); **MCP servers** when you want to *take action* in an external system; **subagents** *"for parallel exploration and also fresh context windows."*

**6. Governance: hooks as deliberately re-injected determinism.** *"Hooks are essentially a way for you to inject a little bit of determinism into your agent, otherwise letting the model decide its own trajectory and be flexible and be dynamic. But hooks are a way to add some of those guardrails back into the system."* Concretely: a `PreToolUse` hook forcing human approval before a write to Salesforce or Jira, *"deterministically every single time"*; and blocking destructive commands. **Sandboxing** is described as the permission-prompt-reduction mechanism, not just a containment one: *"we want to give an agent sort of the free rein to reduce permission prompts and also execute commands within an existing environment. But anytime the agent tries to exit that sandbox environment, run a command that it's not allowed to, or access a network that it's not supposed to access, that's when a permission prompt is triggered."*

**7. Evals framed as the model-upgrade mechanism, not the quality mechanism.** Her argument for why evals matter is specifically about staying on the capability curve: *"without evals, let's say a new model comes out, you have your existing agent, you have your existing prompts and your existing tooling — you don't know objectively in a quick way to test if a new model put into your system is actually going to help you achieve new capabilities."* The shape: *"almost like unit tests, but built for agents and built for dynamic paths."* She notes the recurring gap she sees in customer work: *"a lot of times people are just behind on building evals with how quickly agents are evolving."*

**8. The SRE demo (~16:48–24:00) — a genuinely closed loop, run live.** She sets the pain point (on-call engineers spend half their time debugging production incidents, get paged at 3am, then have to write a postmortem), then breaks her own demo codebase by dropping a database pool size to 1, redeploys via Docker, and watches 500-errors spike on a dashboard. PagerDuty calls her phone on stage. The agent then: identifies the user service as the culprit and the pool size as the cause; edits the code (pool size 1 → 20) with the file open side-by-side; **redeploys the server and verifies its own work**; watches the error graph fall; resolves the PagerDuty incident; and publishes a postmortem into Jira/Confluence via MCP. Her framing of the write-access moment: *"I think write access, or agents taking actions, can feel pretty dangerous sometimes. But the important thing is just to add the appropriate guardrails around the agent."* And the reason the postmortem is a skill rather than a system-prompt section: *"the Claude agent is not going to read instructions about the postmortem into a system prompt until I actually say as a user that I want it to execute and kick off a postmortem for me. That means that we can make this postmortem skill instruction more detailed."*

**9. Managed Agents as the closing pitch** (~24:01), released *"today or maybe yesterday"* relative to the April recording. The problem it removes is deployment and hosting, *"especially when you think about giving Claude access to a computer or file system… how do you make sure everything is containerized and… deployed in a virtual machine."* She notes its abstraction is **sessions and environments** rather than the message-level decomposition of the Messages API.

## What was actually ingested

The **complete** talk — all 194 caption segments across the full `duration: 25:20` / `length_seconds: 1520`, with all ten chapter markers, including the demo. Nothing was truncated.

**Two acquire-time artifacts were cleaned and are documented in the raw file's `notes:`.** YouTube's accessibility time label (*"1 minute, 4 seconds"*) had leaked into 184 of 194 segment texts, and the ten chapter titles were appended mid-sentence into the prose. Both were stripped; the chapters are preserved as `chapters:` and as body headings. Neither artifact appeared in the other five videos acquired in the same batch, so this looks video-specific rather than a skill regression. Standard ASR proper-noun cleanup was also applied (*Enthropic* → Anthropic, *cloud code* → Claude Code, *grap* → grep, *page duty* → PagerDuty, and others).

**A material scope caveat: the recording is four months older than the publication date.** The talk was given **9 April 2026**; Databricks published it **19 August 2026**. Everything He says about what is "new" or "just released" — Managed Agents especially, and the custom-commands/skills merge — is April-2026-current, not August-2026-current. The wiki source page is dated on the publication date per convention, but any claim about product timing should be read against April.

**No numbers.** The talk contains no benchmark, no eval score, no adoption figure, no latency or cost data. The tool count (*"about 14 or 15"*) is the only quantity in it, and it is hedged. The demo is a single scripted run of a fault the presenter injected herself, in a sample codebase, with a known cause — it demonstrates that the loop closes, and nothing about reliability.

## Dynamic-capabilities tagging

- **`digital-seizing/rapid-prototyping`** — the talk is structured as a build-it-tomorrow playbook (*"if you were to leave this room, how would you actually go and build agents?"*), and its central architectural argument is a prototyping-speed argument: because the primitives are domain-invariant, a team building a finance, audit, contract-review or SRE agent starts from a working general-purpose harness and adds skills and tools rather than constructing a new one. Managed Agents is pitched on the same axis — *"if you're building an agent from scratch, you're just prototyping something new, test out the managed agent."* This is the cell's *"creating minimum viable products"* activity at agent-engineering altitude.
- **`digital-transforming/improving-digital-maturity`** — the skills mechanism is a codification argument: domain expertise that would otherwise live in an individual's head or a wiki page is packaged as progressively-loaded instructions plus executables that agents inherit, which is *"leveraging digital knowledge inside the firm"* in the cell's literal sense. The SRE demo makes the same point operationally — runbooks (*"previously when you saw this similar incident, what are the steps you took to debug it"*) and postmortem conventions become skills, so an organisation's accumulated incident knowledge becomes machine-executable rather than documentary.

## Linked entities and concepts

- [[Anthropic]] — the speaker's employer and the subject of the talk. Updated in this ingest.
- [[Claude Code]] — described mechanically (~14–15 tools, developer-grade navigation over semantic search) more concretely than anywhere else in the corpus. Updated in this ingest.
- [[concepts/agent-harness|agent-harness]] — the domain-specialisation reversal, hooks-as-re-injected-determinism, sandboxing as permission-prompt reduction, subagents as context isolation, and the skill/MCP/subagent decision rule all land here.
- [[concepts/ai-agents|ai-agents]] — the three-stage progression and the four-clause agent definition.
- [[concepts/agent-development-lifecycle|agent-development-lifecycle]] — evals framed as the mechanism for absorbing model upgrades, and Managed Agents as the deploy/host stage.
- [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] — the SRE use case and the customer-facing observation that eval practice lags agent practice.
- [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic — Managed Agents]] — the product this talk ends on; see `relationships:`.
- [[2026-07-16-baugues-thurium-google-cloud-what-is-an-agentic-harness|Baugues & Thurium / Google Cloud]] — the same agent definition from a competitor, five weeks later.
- [[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering — *Harness Is All You Need*]] — the empirical anchor for harness-over-model.
- [[2026-08-11-ummadisetti-langchain-toyota-deep-agents-rd-research|Ummadisetti / Toyota via LangChain]] — a customer instance of the skills-as-institutional-knowledge mechanism.

**Dangling** (single-source mention, deferred per [author-entity promotion](../../CLAUDE.md#author-entity-promotion)): Isabella He, **Databricks** (first appearance as a publisher in the corpus — promote on a second source), Agentic + AI Observability Meetup, Claude Agent SDK, Managed Agents, Agent Skills, MCP, PagerDuty, Jira/Confluence.

## Source quality note

Auto-generated captions, ASR-cleaned (see the raw file's `notes:` for the full substitution list and the two scraper artifacts). Transcription quality after cleanup is good; the speaker's delivery is fast and heavily hedged with *"essentially"*, which is preserved in quotations.

**This is a vendor account of the vendor's own products**, delivered by an Anthropic employee at a meetup hosted around a third vendor's observability theme and published on a fourth party's channel. Every design claim is Anthropic's design intent, and every product mentioned is Anthropic's. It should not be cited for whether skills, subagents, hooks or Managed Agents work well, or for comparisons against LangGraph, ADK or any other framework.

What it *does* support, and why it earns a page despite the absence of evidence: it is the **most detailed first-party account in the corpus of how Anthropic itself frames the harness layer** — the domain-invariance argument, the retrieval-architecture choice behind Claude Code, the explicit skill/MCP/subagent decision rule, and hooks-as-determinism are all stated by someone who works on the internals (compaction, tool-result clearing) rather than by a marketer. That makes it a useful primary source for *what the design intent is*, against which the wiki's independent and customer-side sources can be checked.
