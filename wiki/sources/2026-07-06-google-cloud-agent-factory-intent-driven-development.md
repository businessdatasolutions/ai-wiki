---
type: source
kind: video
title: "Intent-driven development with Claude Code & Fable 5"
author: ["Google Cloud Tech"]
publisher: "Google Cloud (Google Cloud Tech YouTube channel — *The Agent Factory* series); host Smitha Kolan, with Lydia Hallie (Anthropic) and YK Sugi (CS Dojo)"
url: "https://www.youtube.com/watch?v=6ERUGFurDHY"
date_published: 2026-07-06
date_ingested: 2026-09-16
length: "~46:01 minutes (auto-generated ASR transcript, cleaned at acquire time; 421 segments across the channel's own 19 chapters)"
raw: "../../raw/videos/intent-driven-development-with-claude-code-and-fable-5.md"
tags: [google-cloud, google-cloud-tech, agent-factory, anthropic, lydia-hallie, yk-sugi, smitha-kolan, claude-code, auto-mode, permission-fatigue, permission-classifier, dynamic-workflows, parallel-subagents, determinism, intent-driven-development, voice-prompting, claude-design, claude-cowork, vertex-ai, draft-pr, review-inversion, engineer-as-pm, vendor-explainer, co-marketing]
dynamic_capabilities:
  - digital-sensing/digital-mindset-crafting
  - digital-seizing/rapid-prototyping
  - digital-transforming/redesigning-internal-structures
  - strategic-renewal/organizational-culture
relationships:
  - type: supports
    target: 2026-09-14-google-cloud-agent-factory-agent-harnesses-explained
    via: "the same channel, the same series and the same host ([[Smitha Kolan]]) ten weeks earlier, with the vendors reversed. September's episode has Google describing **Antigravity Boost** as an orchestrator that *'transforms a single model into a coordinated team'* of parallel sub-agents closing with an independent verification pass; this one has Anthropic shipping the identical product shape as **dynamic workflows** — parallel build agents, then sequential integration / review / verify phases. Two vendors, two months apart, converging on the same orchestration primitive"
    confidence: 0.85
  - type: supports
    target: 2026-08-19-he-databricks-anthropic-primitives-to-production-agents
    via: "the corpus's only other first-party Anthropic account of Claude Code's internals. He mentioned auto mode as a dated throwaway — *'we recently announced an auto mode as well… I haven't seen a permission prompt in a long time'* — and left the mechanism unexplained. Hallie supplies it six weeks earlier in publication order: a classifier interposed between every tool call, sitting *'in between your denial list and allow list'*"
    confidence: 0.85
  - type: supports
    target: 2026-08-31-blum-how-i-ai-claude-cowork-pm-system
    via: "the builder-side origin story for the product Blum's episode documents from the user side. Hallie dates the observation to December 2025 (Anthropic staff using Claude Code for marketing and data-science work), states the build time (*'Cowork came out in a week'*), and — the load-bearing detail — confirms Cowork *'still uses the Claude Code runtime underneath'*, differing only in connectors and system prompts. Blum's claim that *'it's not Cowork in itself'* turns out to be architecturally literal"
    confidence: 0.85
  - type: supports
    target: 2026-09-07-yc-paper-club-why-the-harness-matters-more-than-the-model
    via: "Karten's *model-controlled expressibility* list names **programmatic sub-agent creation** as a capability the harness must supply because the model cannot. Dynamic workflows is that capability shipped: Claude Code emits a JavaScript file of phases and typed subagents, the user edits it (including per-subagent model choice), saves it as a command and re-runs it deterministically. Also instantiates the paper club's model-selection-as-harness-decision point, via the Vertex AI wizard's model list"
    confidence: 0.8
  - type: supports
    target: 2026-03-26-osmani-code-agent-orchestra-multi-agent-coding
    via: "Osmani's orchestra pattern is hand-rolled parallel subagent orchestration; Hallie names the exact defect that makes hand-rolling necessary — *'if you're just asking Claude every time to use subagents… it's very non-deterministic. Sometimes it might spin up four subagents, sometimes it might not even use subagents'* — and presents the workflow file as the vendor's fix"
    confidence: 0.75
  - type: contradicts
    target: 2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes
    via: "on whether green CI is a sufficient stopping condition. Hallie describes the Claude GitHub app as default-on at Anthropic — *'if your CI fails or someone leaves a comment, Claude will automatically try to fix it until your CI is green'* — which makes a passing pipeline the loop's terminal state. The AIDev study finds **46.41%** of agent-proposed fixes rejected, with CI/test failure only one of four rejection categories; *incorrect implementation* and *low priority* are invisible to a green pipeline. The disagreement is about what the signal certifies, not about whether the loop runs"
    confidence: 0.8
---

# The Agent Factory — Intent-driven development with Claude Code & Fable 5 (Google Cloud Tech, July 2026)

> Are you still writing your software architecture line by line, or are you letting autonomous agents do the heavy lifting? In this episode of The Agent Factory, we explore the radical shift toward intent-driven development, where your job is to tell the AI what to build rather than how to build it. Host Smitha Kolan sits down with Lydia Hallie from Anthropic and YK Sugi, the creator of CS Dojo and author of the viral Claude Code Tips repository… Lydia pushes the envelope even further by using Claude Design and the brand-new Dynamic Workflows feature powered by the Fable 5 model to spawn parallel engineering subagents.
>
> *— Channel description, Google Cloud Tech (*The Agent Factory*)*

## TL;DR

**The title is the least interesting thing in the episode.** "Intent-driven development" is a rebrand of prompting well, and both guests say so in different words. What this video actually delivers is the corpus's **first substantive first-party account of two Claude Code mechanisms** the wiki has been carrying as names without contents:

1. **Auto mode is a classifier, and the problem it was built for has a name.** [[Lydia Hallie]] — Anthropic, on the Claude Code team — names **permission fatigue** as a *dangerous* failure mode, not merely an annoying one, and describes auto mode as a third option between the two bad ones the product previously offered. This is the sharpest thing in the episode and it lands directly on [[agent-oversight-and-delegation]].
2. **Dynamic workflows recovers determinism from subagent spawning** by having Claude Code write a JavaScript file you can read, edit, save as a command, and re-run — including changing which model each subagent uses.

Around those: [[YK Sugi]] (CS Dojo; the ~8,000-star `claude-code-tips` repo) builds a 3D game by voice, Hallie rebuilds it from an HTML wireframe generated in **Claude Design**, and the pair state the **review inversion** — that the 90/10 split between writing and reviewing has flipped — more plainly than anything else in the corpus.

It is also, unambiguously, **vendor co-marketing**: Google's channel, Google's Vertex AI, Anthropic's developer relations, and two greenfield toy demos. See [§Scope and reliability](#scope-and-reliability).

Read it as the **first half of a pair** with [[2026-09-14-google-cloud-agent-factory-agent-harnesses-explained|September's Agent Factory episode]], which runs the same format with the vendors reversed — Google describing its own orchestration feature to a Google audience, ten weeks after Anthropic described the equivalent one here.

## Permission fatigue, and auto mode as the designed answer

The wiki's oversight page has recorded oversight *decay* — approvals that get rubber-stamped as familiarity grows — as an observed phenomenon. Here a vendor names it, calls it dangerous, and ships against it.

Hallie's account of the prior state of the product is a two-option trap:

> *"you can ask almost everything, in which case Claude Code will always ask you like, hey, is it OK if I delete this file. Is it OK if I run this command. And after a while you're just like, yeah, go ahead. Whatever. And we call this a permission fatigue."*

And the reason it is not just friction:

> *"if Claude asks you questions every time [you] won't read them as much anymore because you're kind of — you've asked me 100 times now. Sure, just go ahead. That's permission fatigue, which is also dangerous."*

The other option was worse: `--dangerously-skip-permissions`, *"in which case Claude will never ask you anything, which is also not great because if it's about to delete your root file, there's no going back."* So:

> *"auto mode is our solution to that. It kind of sits in between your denial list and allow list. So auto mode runs a different classifier between all the tool calls."*

Three properties she attaches to it, each worth recording separately:

| Property | Her statement | Why it matters |
| --- | --- | --- |
| **Risk triage per tool call** | *"is this tool call dangerous. First of all, if yes… Let's ask the user if they actually want to do it. But if it's just a normal read or edit… let's not bother them"* | The gate fires on a classifier's judgement of the call, not on a static allowlist — the [[agent-oversight-and-delegation|consequence-calibrated gate]] implemented in the harness rather than prescribed as a practice |
| **Prompt-injection defence** | *"it's much better against prompt injection. In some cases, a tool call might just be like ignore all instructions… because it runs a classifier in between, it's much better at catching that"* | The same interposition doubles as an [[attack-surface-management|injection]] check — one mechanism, two jobs |
| **Context dependence** | *"If you're asking Claude, delete this folder… if you've specifically asked for it, it's not dangerous. So in those cases, auto mode won't ask you"* | Explicit intent from the user downgrades the risk score. The classifier reads the *session*, not just the call |

And the stated payoff, which is the whole commercial argument for it: *"this actually enables you to… run Claude Code way more autonomously in these longer running sessions."*

**This is the mechanism behind a line the corpus already held.** [[2026-08-19-he-databricks-anthropic-primitives-to-production-agents|Isabella He]] mentioned auto mode in August as a dated throwaway — *"we recently announced an auto mode as well… I haven't seen a permission prompt in a long time"* — and left it there. Hallie, publishing earlier, explains what the feature is.

**Note what is absent.** No false-approve rate, no false-block rate, no description of what the classifier is or what it was trained on, no evidence for the prompt-injection claim. The mechanism is now on the record; its calibration is not.

One operational detail worth keeping: on Google's Agent Platform auto mode is **off by default** and gated behind an environment variable (`CLAUDE_CODE_ENABLE_AUTO_MODE`) — a safety default that differs by distribution channel.

## Dynamic workflows: determinism bought back with a generated file

Hallie's framing of the problem is the most useful sentence in the segment, because it is a vendor conceding a real defect in the thing the corpus has spent a year praising:

> *"subagents themselves aren't new… But if you're just asking Claude every time to use subagents — you don't even have to ask it — the downside is that it's very non-deterministic. Sometimes it might spin up four subagents, sometimes it might not even use subagents. The other time it uses 10 subagents."*

> *"With workflows, it's kind of our deterministic solution to that."*

The mechanism: Claude Code **writes a JavaScript file** describing the run, then executes it. *"I didn't type this. This is all Claude."* The observed structure on her demo — rebuilding YK's game from an HTML design spec — was:

| Phase | Agents | Execution |
| --- | --- | --- |
| **Build** | build engine · build UI · build audio · levels and haptics | **parallel** |
| **Integration** | one | sequential |
| **Review** | one | sequential |
| **Verify** | one | sequential |

> *"these phases run sequentially, but the actual build agents all run in parallel."*

Two pieces of context make this more than a product note. [[2026-09-07-yc-paper-club-why-the-harness-matters-more-than-the-model|Seth Karten's Paper Club talk]] lists **programmatic sub-agent creation** among the *model-controlled expressibility* features a harness must supply because the model cannot generate them for itself; this is that capability shipped, with the program exposed rather than hidden. And the non-determinism Hallie concedes is precisely what [[2026-03-26-osmani-code-agent-orchestra-multi-agent-coding|Osmani's "code agent orchestra"]] hand-rolls around — the orchestra pattern exists because the agent could not be trusted to fan out reliably on its own.

Four things follow, and they are what distinguishes this from ordinary subagent spawning:

- **The file is the artifact.** `S` saves it as a named command (*"save as rebuild slingshot game"*), and *"every time we invoke that command, it will just run these exact same subagents."* Non-determinism is traded for a re-runnable script — the same move [[graph-engineering]] makes at the orchestration layer.
- **Per-subagent model selection is editable.** *"Maybe I don't want all subagents to use Fable… Maybe I want to use Sonnet or Opus."* Either ask Claude to change it, or edit the JavaScript. This is [[small-language-models|model routing as a harness decision]], exposed as source code the user owns.
- **Scale is the stated design point.** *"It can go into hundreds of subagents because this is a feature for tasks that takes hours or days."* Compare [[agent-fleet-management]]'s span-of-control framing: here the span is delegated to a file. Google's answer to the same problem — [[2026-09-14-google-cloud-agent-factory-agent-harnesses-explained|Antigravity Boost]], an orchestrator that *"transforms a single model into a coordinated team"* and closes with an independent verification pass — arrived on the same channel ten weeks later with the same phase shape.
- **It was too slow to demo live.** She prepared a finished run in a second tab — *"I kind of also prepared it like a cooking show"* — and used it, noting *"Fable is a bit slower because it's such a large model."* Honest on camera, and the most informative unscripted datum in the episode.

## The review inversion, stated plainly

The corpus has circled this; Hallie says it in one breath:

> *"when you handwrite it, you like 90% of the review process happens as you're writing it. I think with Claude Code… it's like 90% you have to review it and 10% maybe hand-coding the changes. So there's definitely a lot more importance in the reviewing phase now. And I feel like a lot of people have yet to shift their mindset towards that."*

The numbers are rhetorical, not measured — but the *structural* claim (review was previously bundled into authoring and has now been unbundled from it) is the cleanest statement of it the wiki holds, and it is the same bottleneck [[2026-08-05-vo-lennys-merge-mommy-ai-code-review-bot|Claire Vo]] built a product against.

Her prescription is to automate the review too, *"with permissions and hooks and all of that stuff, just to make sure Claude was following your design spec already"* — which is the same [[agent-oversight-and-delegation|never-let-the-agent-grade-its-own-homework]] tension the corpus keeps hitting: the reviewer of the agent's work is another agent.

## The engineer-as-product-manager claim, with the abstraction analogy attached

> *"the role of the software engineer is changing more to be almost like a product manager… you're not just writing the code, but you are in charge of owning it, understanding the architecture that you want to build. And it's still up to you to understand why you need to implement a feature."*

The analogy she reaches for is the one [[software-3.0]] is built on:

> *"I can write TypeScript or JavaScript, but I'm not going to focus on the machine code that gets generated afterwards… software engineering used to focus on the actual code syntax, almost like how machine code might have mattered. But we're going a layer above that now."*

With the qualifier that keeps it from being a deskilling claim: *"it still requires a lot of technical expertise and good taste and high agency."* Sugi's version arrives in the rapid-fire round — asked whether learning a new programming language in 2026 is a waste of time, he says no, but *"I would focus more on software architecture over specific language features."*

Both also agree, unprompted, that **AI makes senior developers more valuable, not less** — with Hallie's caveat *"depends on the engineer."* That is consistent with [[2026-06-16-anthropic-economic-index-agentic-coding-returns-to-expertise|the Anthropic Economic Index's returns-to-expertise finding]], and it is worth noting that it comes from the vendor whose own index produced that result.

## Intent-driven development, deflated by its own advocate

Sugi coined nothing here and says so:

> *"there are many different terms for it. But I personally like this term because to me, it's not about the exact prompt. Sometimes people say, oh, use this prompt and you get better results. Sure, maybe. But to me, it's more about expressing what your intent is exactly."*

The operational content reduces to three practitioner heuristics, all defensible and none novel:

1. **Prompt by voice.** *"so that you can express your intent faster. You might make mistakes… but it doesn't matter as long as you're able to express it."* Later, watching Claude recover from his own ASR noise: *"as long as your intent is clear enough… Claude is able to figure out what I mean, even if there are typos or transcription mistakes."* Hallie's reason for wanting it is different and more interesting — *"I probably would prompt a lot better if I'm not in my head as much, because… when I type a prompt, I'm like, maybe I shouldn't ask this"*: voice as a filter-removal device, not a speed device.
2. **Ask more questions when you have less context.** *"the rule of thumb is you ask more questions when you have less context"* — he interrogated Claude about physics libraries before committing to Rapier, then stopped asking once he had the vocabulary.
3. **Keep all projects in one parent folder** so the agent can cross-reference them: *"I want to take this element from this other project and this other element from this other project."*

Hallie's qualification is the one the wiki should keep, because it cuts against the democratisation reading of [[vibe-coding]]: *"I still feel like having a software engineering background does help refine your prompts, and you can tell Claude a lot better what you actually want it to do."*

## Design-as-spec: the wireframe is the prompt

The most transferable technique in the episode, and one the corpus has not recorded in this form. Rather than prompting the changes she wanted, Hallie generated a **visual plan in Claude Design** (*"basically Claude Code, but for design"*, then in research preview) — game flow, level select, health bars, haptics, scoring, level art — as plain HTML, edited it by hand, then handed the file to Claude Code as the prompt:

> *"what I'm doing now is I'm giving Claude a way to verify and understand what I want to build, because it has this HTML. It has the context. I could have made this prompt like a lot more specific… but honestly, I'm kind of just waiting to see if Claude will understand it."*

The spec doubles as the acceptance criterion — she checks the built game against the wireframe at the end. This is [[agentic-engineering]]'s verification discipline with the artifact moved upstream: **an editable, inspectable plan that is also the prompt and also the test.**

## Draft PRs as an agent-authorship signal

Sugi's convention, stated as a tip and demonstrated:

> *"You can just ask the agent to create a draft PR just like I did, and then check it before marking it as ready for review so that people will [know] OK, this PR maybe was created by the agent. It's not ready for review yet."*

Draft status as an **out-of-band provenance marker** — cheap, uses existing GitHub semantics, and addresses the reviewer-attention problem [[agentic-pull-requests]] records without new tooling.

Set against it, the Anthropic-internal practice Hallie describes is the opposite posture: the Claude GitHub app installed across their repos, so *"if your CI fails or someone leaves a comment, Claude will automatically try to fix it until your CI is green"*, with the stated goal *"to be as out of the loop as possible."* Both are in the same episode, twenty minutes apart, and they point in opposite directions on how much human attention an agent-authored change should attract. See [§Debates and supersession](#debates-and-supersession).

## Claude Cowork: the origin story, and a vendor using the corpus's word

Asked whether Claude Code's expansion beyond coding was intentional:

> *"back in December, we noticed that internally, a lot of our employees were using Claude Code for non-coding tasks. So the marketing team was using it to create marketing files, data science, and so on. So we wanted to build **a better harness for these types of tasks**. And that's how Cowork came out in a week because we of course, use Claude Code to build Claude Cowork as well."*

Two things here. First, the architectural fact: *"It still uses the Claude Code runtime underneath, so it can still do coding… but we just have better connectors and better system prompts in Cowork to focus on that non-technical stuff."* [[2026-08-31-blum-how-i-ai-claude-cowork-pm-system|Blum's]] refusal of the vendor framing — *"it's not Cowork in itself"* — is literally true: it is the same runtime.

Second, **[[Anthropic]] calls its own product a harness, in those words**, which is a first-party adoption of the vocabulary [[agent-harness]] tracks, from the vendor that did not coin it.

The generalisation both guests reach is the terminal-as-universal-interface claim:

> *"the computer started in the terminal. The computer just used to be the terminal. That was the whole UI. But then we got these different GUI apps… But now we're back on the terminal."* — Sugi

> *"the bottleneck now is just your imagination."* — Hallie

## "Claudify" — and the deliberate limit on it

Hallie's own workflow is maximal automation with one hand-drawn boundary, and the boundary is the interesting part:

> *"what is the problem I'm trying to solve… I try to codify as much in my life as possible, and **I don't want to codify the things I actually enjoy doing**. For example… I really enjoy creating keynote slides and I could use Claude Code to automate that as well, because we have computer use… But I noticed, I kind of just enjoy doing this and I don't want Claude to do this. This is my creative outlet."*

Sugi names it — *"I love the term Claudify"* — and Kolan closes the thread with a counter-anecdote about someone who built an app to reply to their partner: *"maybe we're optimizing too much."*

A small moment, but it is the corpus's clearest statement that the automation boundary is a **preference**, not a capability frontier — and it comes from someone paid to push the frontier.

## Dynamic capabilities (Warner & Wäger)

- **`digital-sensing/digital-mindset-crafting`** — the episode's explicit purpose is belief-updating about what the tool can do: the opening question to both guests is *"what is the one thing about Claude Code that most developers are completely sleeping on"* (answer: auto mode), and Hallie's review-inversion point is stated as a mindset gap — *"a lot of people have yet to shift their mindset towards that."*
- **`digital-seizing/rapid-prototyping`** — two end-to-end builds inside the runtime: a 3D physics game from a voice prompt to a merged PR, and a wireframe-to-game rebuild via parallel subagents. The Claude Design step makes the *plan* a prototype too.
- **`digital-transforming/redesigning-internal-structures`** — the engineer-as-product-manager claim is a role redefinition, and the 90/10 review inversion redistributes where engineering attention is spent. Anthropic's own internal structure (the GitHub bot auto-fixing CI across all repos; scheduled Claude sessions) is described as the target state.
- **`strategic-renewal/organizational-culture`** — the Hacker News craft-and-technical-debt debate is put to both guests directly, and Sugi's answer is a cultural norm rather than a technique: *"you're responsible for the output"*, *"if you generate 100,000 lines of code, you don't have to commit 100,000 lines of code."* The Claudify boundary is the same register.

## Linked entities and concepts

- Concepts: [[agent-oversight-and-delegation]], [[agent-harness]], [[agent-fleet-management]], [[agentic-engineering]], [[agentic-pull-requests]], [[ai-generated-code-quality]], [[vibe-coding]], [[software-3.0]], [[graph-engineering]], [[small-language-models]], [[attack-surface-management]]
- Entities: [[Lydia Hallie]], [[YK Sugi]], [[Smitha Kolan]], [[Anthropic]], [[Claude Code]], [[Google]], [[GitHub]]
- **Dangling** (single-source mention, deferred): Claude Design, dynamic workflows, Vertex AI Model Garden, Gemini Enterprise Agent Platform, Fable 5, Rapier, `claude-code-tips`

## Scope and reliability

**Treat this as vendor co-marketing with two genuinely informative segments inside it.** Google supplies the channel and three product placements (Vertex AI, Model Garden, the Gemini Enterprise Agent Platform); Anthropic supplies a developer advocate demonstrating four of its own products; the third guest is a community advocate whose repository the episode promotes. Nobody in the conversation has an incentive to report a limitation.

**Zero measurements of any kind.** No benchmark, no latency or cost figure, no false-approve rate for the auto-mode classifier, no evidence for the prompt-injection claim, no data behind the 90/10 review split. The `$10,000` real-estate saving is a single unverifiable anecdote about emailing realtors directly, and the 8,000 GitHub stars is a popularity metric.

**Both demos are greenfield toys** — a slingshot game, twice. This is the standing weakness of every coding-agent demo the corpus holds: nothing here touches an existing codebase with tests, dependencies, or a history, which is where [[ai-generated-code-quality|the quality evidence]] says the problems live.

**What it is good for:** mechanism and vocabulary, first-party. Auto mode's classifier design, the non-determinism admission behind dynamic workflows, the phase structure of a workflow run, Cowork's runtime relationship to Claude Code, and the permission-fatigue framing are all things only the vendor could state, and it states them on the record. Cite for those; never for magnitudes.

**Transcript quality:** YouTube exposes both an ASR and a human-curated "English - CC" track; the panel served the ASR one. It mangled nearly every proper noun in the episode (*Claude Code* → *"Lockport"*, *Lydia Hallie* → *"Lyria Haley"*, *Google Cloud Platform* → *"Azure platform"*, *Rapier* → *"wrap here"*), all corrected at acquire time and itemised in the raw file's `notes:`. One GCP project name remains inaudible. Quotations above are from the cleaned text; timestamps are verbatim.

## Debates and supersession

- **The episode contradicts itself on agent-authored changes, and neither speaker notices.** Sugi's draft-PR convention exists to make agent authorship *conspicuous* so a human looks harder; Hallie's GitHub bot exists to make it *invisible* so no human looks at all (*"as out of the loop as possible"*). Both are presented as best practice in the same 46 minutes. The reconciliation the corpus would offer is [[agent-oversight-and-delegation|consequence-calibration]] — draft PRs for changes that reach production, auto-fix for CI-green plumbing — but neither speaker draws that line, and the episode leaves the impression that both are simply good.
- **Green CI as a stopping condition is contested by the corpus's own evidence.** *"Claude will automatically try to fix it until your CI is green"* makes a passing pipeline terminal. [[2026-06-11-abujadallah-rejection-of-agentic-pull-request-fixes|Abujadallah et al.]] find 46.41% of agent fixes rejected, with *incorrect implementation* and *low priority* — both invisible to CI — among the four categories; [[reward-hacking]] argues a passing suite is precisely what an optimising agent produces regardless. Recorded as `contradicts` above.
- **"Deterministic" is doing contested work.** The workflow *file* is deterministic — same phases, same subagent prompts, same models, every invocation. What each subagent *does* with its prompt is not. Hallie's claim is about the orchestration graph, not the output, and the episode does not distinguish them. [[multi-agent-failure-modes|MAST]]'s failures are largely inter-agent, i.e. inside exactly the part that stays non-deterministic.
- **The classifier is an unexamined trust transfer.** Auto mode's pitch is that it removes decisions the human was rubber-stamping anyway. That is plausible, and it also means an unmeasured model now makes those calls. The page's standing complaint on [[agent-oversight-and-delegation]] — that nobody reports a false-approve rate for any gate — applies here to a gate that is shipping by default.
- **Open: is "intent-driven development" a distinct practice or a renamed one?** Sugi explicitly declines to defend the term's novelty (*"there are many different terms for it"*), and its content reduces to prompt-by-voice, ask-questions-early, and colocate-your-repos. The corpus should treat it as vocabulary, not as a construct, unless a second independent source gives it operational teeth.
