---
type: source
kind: video
title: "The New Full-Stack Designer"
author: ["Y Combinator"]
publisher: "Y Combinator — Design Review, host Aaron Epstein"
url: "https://www.youtube.com/watch?v=eojywvxqoLc"
date_published: 2026-10-26
date_ingested: 2026-10-30
length: "~1:05:44 minutes (transcript ~284 lines)"
raw: "../../raw/videos/the-new-full-stack-designer.md"
tags: [y-combinator, design-review, aaron-epstein, marvin-schwaibold, shopify, sidekick, molly-studio, collins, full-stack-designer, designer-as-editor, figma-as-scratchpad, codex, claude-code, prototypes-over-prds, dialkit, blossom-carousel, grass-shader, interruptible-interfaces, progressive-disclosure, scroll-jacking, one-primary-goal, taste]
dynamic_capabilities:
  - digital-seizing/rapid-prototyping
  - digital-sensing/digital-mindset-crafting
  - digital-transforming/redesigning-internal-structures
relationships:
  - type: supports
    target: 2026-02-06-figma-make-prompts-to-prototypes-with-claude
    via: "design moving from static canvas to working prototypes built with AI"
    confidence: 0.65
  - type: supports
    target: 2026-05-02-schoening-lennys-podcast-cultivating-agency-ai-era
    via: "designers shipping code and prototyping in the terminal"
    confidence: 0.65
  - type: supports
    target: 2026-07-19-why-netflix-is-betting-on-systems-thinkers-not-specialists-in-the-ai-era
    via: "designers, engineers and PMs getting further along the product cycle before a handoff"
    confidence: 0.6
---

# Schwaibold & Epstein (YC, Design Review) — the new full-stack designer

> In this episode of Design Review, Marvin Schwaibold, who leads the product design studio at Shopify, joins YC's Aaron Epstein to walk through his design process. He shows the admin redesign and Sidekick work his team recently shipped, a weekend project where he rebuilt real grass as a shader, and a carousel that took 91 attempts to get right. Then they review five viewer-submitted websites with a focus on motion and interactivity.

## TL;DR

A 65-minute episode on the [[Y Combinator]] channel. **Aaron Epstein** talks with **Marvin Schwaibold**, who leads the product design studio at **Shopify** and ran the Brooklyn studio *Molly* before Shopify absorbed it. The second half reviews viewer-submitted websites. Five claims:

1. **The process hasn't changed; the tools have.** It is still iterative, but work moves from Figma to Codex, Claude Code and the terminal. Figma is now *"a scratch pad"* for drawing what he cannot put into words.
2. **The designer is the editor.** *"The output isn't the issue anymore, it's us being extremely selective."* AI *"can write code, but it doesn't know what looks good and what looks bad and that's for me to decide."*
3. **You must decompose.** The tools *"are extremely capable at creating anything,"* but *"you have to be able to take a … concept … and break it down into all its little components."*
4. **Prototypes outrun documents.** *"Prototypes are a million times more useful than any PRD document you can write,"* and they spread *"like wildfire."* He sees *"one-off armies or teams of two"* doing the work of many, and it gets buy-in faster than rallying a team round an idea.
5. **Expose the variables.** Chat cannot tune motion. *"I know when it feels off, but the back and forth with chat just doesn't work,"* so he builds sliders (DialKit) into the prototype. Doing so also exposed a terrain map he had got wrong *"five prompts ago."*

## Key claims

### Shopify's mandate

Shopify's Tobi Lütke said at some point last year that *"that future needs to be designed,"* and hired designers to paint a picture. The studio runs inside **Sidekick**, Shopify's AI layer. Two efforts pair up: a redesign of the admin, and using chat to manipulate the store, with suggestions on the home feed that open a conversation and change the store directly. Prototypes are built in a playground with its own dev panel. *That code is not production code* and is not allowed into Shopify's main repo.

### Worked examples

- **Grass as a shader.** He fed a video to Codex, got a poor result, then took screenshots to ChatGPT and asked why the first agent did not understand. The trick that worked was rendering a topographic map of the ground, since the model had not grasped that the grass stood on hills. A colleague's question about blade length led to a toggle: the model had about 217,000 blade variations differing by only about 0.7–0.8.
- **The carousel.** 91 prompts to imitate a design by Mike Matas, to look under the hood of it. *"Codex won't get mad at me if I need 91 approaches … If I had done that with my engineer, they would probably flip out."* He calls AI *"an infinitely patient collaborator."*
- **A drawing rather than words.** He drew coloured boxes in Figma to explain an interruptible interaction he could not describe.

### Designers, engineers and PMs

*"Designers are becoming more full stack. As are engineers and PMs. It goes in every which way."* His advice to founders and designers is to tinker, not give up, show the model examples you like, and copy things to learn how they are made.

### What the reviews say

Applied to sites by Endstack, SkillSync, InstaPlay, Mintlify, Knowlify and Instinct Space:

- **One thing per page.** *"What is the one thing we want [the user] to take away?"* Too many equal calls to action leave a visitor with nothing to follow. His old professor's word was *"dictatish"*: a poster must direct the eye.
- **AI illustrations add nothing by default.** Epstein names *"the hallmarks"*: very small text, and animations no one would have spent time on. Schwaibold would hire an illustrator, and recalls a Gemini animation that explained the model and stayed in memory.
- **Reduction is the hard part.** On Mintlify: *"It's easy to throw everything. It's much harder to figure out what needs to be edited out,"* because every team wants its feature on the page.
- **Interruptible, native interaction.** *"Smooth scrolling on websites is a disaster in the industry."* Scroll jacking is *"almost an arrogant way of going about it."*
- **Show the output before the sign-up.** A game-maker that asks for a login before showing any result loses people, since the visitor does not yet know if it is good.

## Dynamic-capabilities reading

- **`digital-seizing/rapid-prototyping`**: working demos in place of specifications, in a sandbox on live data, and teams of two.
- **`digital-sensing/digital-mindset-crafting`**: the founder's mandate that *"the future needs to be designed"*, and tinkering as the habit to build.
- **`digital-transforming/redesigning-internal-structures`**: a design studio acquired and embedded in the AI product line, and role lines moving among design, engineering and product.

## How it connects

- [[concepts/vibe-coding|vibe-coding]] — a demo that is not production code, and what experts add to prompting.
- [[concepts/durable-skills|durable-skills]] — taste and editing as what remains with the person.
- [[concepts/expert-generalist|expert-generalist]] — *"designers are becoming more full stack."*
- [[concepts/agentic-engineering|agentic-engineering]] — decomposition into subtasks, and instrumenting a prototype to see its variables.

## Related in this wiki

- [[2026-02-06-figma-make-prompts-to-prototypes-with-claude|Figma Make]] — a design-tool vendor on moving from prompts to prototypes.
- [[2026-05-02-schoening-lennys-podcast-cultivating-agency-ai-era|Schoening (Notion)]] — designers and PMs shipping code.
- [[2026-07-19-why-netflix-is-betting-on-systems-thinkers-not-specialists-in-the-ai-era|Stone (Netflix)]] — role fluidity, *"real but bounded."*
- [[2025-12-16-diasio-wood-worklab-agentic-ai-corporate-ladder|Diasio (EY)]] — AI *"raises the floor, but it doesn't raise the ceiling"*; Schwaibold says AI *"has definitely raised the ceiling for all of us."*
- [[2026-10-27-chase-langchain-interrupt-london-agents-improve-over-time|Chase (Interrupt London)]] — evals as *"the new PRD."*

## What was actually ingested

The full episode (1:05:44, `length_seconds: 3944`) from the auto-generated track via the yt-dlp fallback, 284 lines. ASR corrected against the description in quotes and prose (*Nstack* is Endstack, *Nullify* and *Netlify* at 51:42 are Knowlify, *Toby* is Tobi). The description says five sites; the chapters list six. No stills: the visuals are live screen-shares of products and websites, which carry no claims the wiki would cite. The site reviews are summarised by their general points, not site by site.

## Linked entities and concepts

- [[Y Combinator]] — publisher. Updated in this ingest.
- [[Claude Code]], [[OpenAI]] — Codex, ChatGPT and Claude Code as his tools.
- [[concepts/vibe-coding|vibe-coding]], [[concepts/durable-skills|durable-skills]], [[concepts/expert-generalist|expert-generalist]], [[concepts/agentic-engineering|agentic-engineering]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the three cells tagged above.

**Dangling** (single-source mention, deferred): Marvin Schwaibold, Aaron Epstein, Shopify, Tobi Lütke, Sidekick, Molly, Collins, Mintlify, DialKit, Blossom Carousel.

## Scope and reliability

One senior designer's practice, on a channel that promotes YC, reviewing sites that include YC companies. Nothing is measured: craft claims rest on taste, stated as such. Claims about Shopify are prototypes and direction, not results. The studio's work is by its own account in a playground outside production, so *"full stack"* here means building working demos rather than shipping to Shopify's codebase.
