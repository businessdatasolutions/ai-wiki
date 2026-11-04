---
type: source
kind: video
title: "Hippocratic AI powers safe, conversational voice agents for healthcare with Google Cloud"
author: ["Google Cloud"]
publisher: "Google Cloud — customer story featuring Vishal Parikh, co-founder and chief product officer of Hippocratic AI"
url: "https://www.youtube.com/watch?v=yPd9prv_26o"
date_published: 2026-10-20
date_ingested: 2026-11-04
length: "~3:13 minutes (transcript ~26 lines)"
raw: "../../raw/videos/hippocratic-ai-powers-safe-conversational-voice-agents-for-healthcare-with-google-cloud.md"
tags: [google-cloud, hippocratic-ai, vishal-parikh, healthcare, voice-agents, patient-outreach, polaris, constellation-architecture, specialist-models, gemma, llm-as-evaluator, automated-evaluation, gke, dynamic-workload-scheduler, latency, hipaa, hitrust, soc-2, vendor-case-study]
dynamic_capabilities:
  - digital-transforming/navigating-innovation-ecosystems
relationships:
  - type: supports
    target: 2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care
    via: "AI taking routine work off clinicians while people stay for clinical judgment: Philips on imaging and radiology, Hippocratic on outreach calls that bring a human in when there is a real clinical need"
    confidence: 0.55
---

# Parikh (Hippocratic AI) on Google Cloud — safe conversational voice agents for healthcare

> Hippocratic AI builds and deploys safe conversational voice AI agents that address healthcare's biggest problems with a mission to transform patient outcomes through healthcare abundance. Built on Polaris, the company's patented, safety tested constellation model, Hippocratic AI's agents have completed more than 270 million patient voice interactions across more than 300 live clinical use cases, with zero safety issues in production. … Founded on the principle "do no harm," the company's agents do not diagnose or prescribe.
>
> Hippocratic AI's Polaris is a novel constellation architecture of more than 30 large language models (LLMs) optimized for healthcare settings, powered by Google's AI Hypercomputer. … Google's open Gemma models help Hippocratic AI to transform its high bar for clinical care into an operational reality, orchestrating millions of evaluations to maintain the highest levels of safety, clinical reasoning, and conversational accuracy.

## TL;DR

A three-minute customer story on the **Google Cloud** channel of [[Google]], published 20 October 2026. **Vishal Parikh**, co-founder and chief product officer of **Hippocratic AI**, describes voice agents that call patients for routine, non-diagnostic care. Four claims:

1. **Outreach at full coverage.** *"Hospitals only often reach the top 5%"* of most critical patients; *"the other 95% go massively underserved."* The agents can contact every patient, monthly, weekly or daily, with *"well over 30 clinical skills"* (the description quotes him as saying 50), and *"if the patient does have a real clinical need … we do bring a human in the loop."* Patients rate the calls **8.9 out of 10** on average.
2. **A constellation of specialist models.** Polaris is *"over 30 models from 30 billion parameters up to 400 billion parameters,"* over 4 trillion parameters in total (the description says more than five), trained with Google Cloud.
3. **Voice needs latency.** On Google Kubernetes Engine: time to first token under 500 ms, and about 1.5 s average end-to-end latency per turn; Dynamic Workload Scheduler scales capacity with demand.
4. **One model tests another.** *"Testing an LLM based system is not like testing a conventional software platform."* *"When you have a world class reasoning model in health, you need another world class reasoning model to test that model."* Google's open **Gemma** models drive automated evaluation: *"We run millions of evaluations with a goal of over a billion."*

## Dynamic-capabilities reading

- **`digital-transforming/navigating-innovation-ecosystems`**: a specialist AI company building on a cloud provider's infrastructure and open models, and exploiting new ecosystem capabilities (scheduling, evaluation models) it did not build.

## How it connects

- [[concepts/small-language-models|small-language-models]] — many specialist models, each sized for one job, instead of one general model; and a separate open model as evaluator.
- [[concepts/responsible-ai|responsible-ai]] — safety as an evaluation programme run at volume, and a design rule that the agents do not diagnose or prescribe.
- [[concepts/ai-agents|ai-agents]] — voice agents doing outbound clinical work.

## Related in this wiki

- [[2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care|Peron (Philips) on Me, Myself, and AI]] — AI taking low-value work off clinicians while their judgment stays; Philips's own survey finds patients worried about less face-to-face time.
- [[2026-07-14-keneally-bcg-so-what-llm-or-md-patient-journey|Keneally (BCG, The So What)]] — consumers using AI as the first step in care, and the case for agents that help people the health system does not reach.
- [[2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals|Dinakaran (LuminAI) at YC]] — agents for hospital back-office work, the administrative side of the same staffing gap.
- [[2026-09-20-shea-roche-langchain-jev-as-a-judge-agent-evals|Shea & Roche (LangChain)]] — comparing judges for agent evaluation; Hippocratic uses an open model as its judge at very large volume.

## What was actually ingested

The whole video (3:13, `length_seconds: 193`) from the transcript panel, 26 lines; a human-written track also exists. Two figures in the narration differ from the description: *"over 30 clinical skills"* against *"well over 50"* in the description's own quote of the same sentence, and a constellation of *"over 4 trillion parameters"* against *"over five trillion."* Both are reported as said. *"$30 billion parameters"* is read as 30 billion. **No stills published**: the stat cards (8.9/10, under 500 ms, 1.5 s, 400B parameters) repeat the narration word for word. A 32-frame probe confirmed there is nothing else on screen to cite.

## Linked entities and concepts

- [[Google]] — publisher (Google Cloud channel) and infrastructure provider. Updated in this ingest.
- [[concepts/small-language-models|small-language-models]], [[concepts/responsible-ai|responsible-ai]], [[concepts/ai-agents|ai-agents]] — updated in this ingest.
- [[concepts/dynamic-capabilities|dynamic-capabilities]] — the cell tagged above.

**Dangling** (single-source mention, deferred): Hippocratic AI, Vishal Parikh, Polaris, Gemma, Google Kubernetes Engine.

## Scope and reliability

A vendor marketing video for a cloud provider, featuring a customer. Every figure is the companies' own, and two differ between the video and its description. *"The world's only safe LLM for health"* and *"zero safety issues in production"* are marketing claims; what counts as a safety issue is not defined. The patient rating is reported without method or sample.
