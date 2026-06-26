---
title: "From Demo to Production: Why Agentic AI Systems Fail - and How to Fix Them"
video_id: yCIl1-dIVnc
url: https://www.youtube.com/watch?v=yCIl1-dIVnc
channel: InfoQ
channel_id: UCkQX1tChV7Z7l1LFF4L9j_g
channel_url: https://www.youtube.com/channel/UCkQX1tChV7Z7l1LFF4L9j_g
publish_date: '2026-06-24T02:00:24-07:00'
upload_date: '2026-06-24T02:00:24-07:00'
category: Science & Technology
duration: '39:08'
length_seconds: 2348
view_count: 70
default_language: null
keywords:
  - AI
  - Artificial Intelligence
  - Generative AI
  - LLM
  - Software Engineering
  - Machine Learning
  - AI Architecture
  - Claude
  - Anthropic
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
description: |
  Most agentic AI systems look great in demos - and collapse in production.

  This talk reveals why: it's a systems problem, not a model problem. Through hard lessons building a platform for 10M+ users, learn how to master context management, tool exposure, agent boundaries, and observability to ship AI that actually works.

  #AgenticAI #LLMOps #AIEngineering
notes: |
  ASR transcript, lightly cleaned at ingest. Proper-noun normalisations applied:
  "visig editor" → visual editor; "w coding"/"web coding" → vibe coding;
  "Obased" → OAuth-based; "ooth"/"oath" → OAuth; "Langfuse"/"langu" → Langfuse;
  "light LLM"/"light llm" → LiteLLM; "langraph" → LangGraph; "MCPS" → MCP.
  Segment-level timestamps were empty in the source (flat transcript, no chapters).
  Presenter not named in the transcript or YouTube metadata; attribution is the
  InfoQ channel. Speaker describes building an agentic app-generation platform
  (mobile/web app builder, visual editor + chat) serving 10M+ users.
---

## Transcript

So in 2024 November Anthropic released MCP, which enabled us to build agentic applications with enterprise data. So that's where we are right now. The kind of system that we built is about having 10 agents, 200-plus tools that we were using in our platform, and there are thousands of instructions for everything that we do in every agent. Because all of these are required even to build any enterprise application, we get into a lot of challenges. Even if you build any enterprise application where you want to get your data into the LLM and serve the request, you will be facing some of these problems.

So I'm going to talk about the problems we faced and how we solved them. These are not the only problems — these are just four problems that we chose for this particular talk. I'm only going to talk about four problems that we solved and how we solved them.

Just to give a background and set the context: what we are building is an agentic app-generation platform that generates applications for mobile and web. This uses both a visual editor as well as an agentic chatbot interface. Either you can build apps through the web interface, or you can build with vibe coding — similar to web coding, you can build with a chat interface.

The initial architecture — I'm talking about 2025, one year back — what we decided is that we want to build agents for every feature of the product. Whether you are doing a database, or whether you are enabling security in your application, or you're configuring environment properties — anything that you do, we wanted to build an agent. All these agents have to communicate with each other; that's where we introduced something called an orchestrator. The job of the orchestrator is taking the user's request and delegating it to the respective agents, and it internally communicates with the MCP server so that it talks to our platform APIs to perform the actual operation inside the user project. This is all running in the cloud — nothing on your local, everything working out of the browser.

So what happened? In early 2025 we built a small pilot and showed it to our CEO. We quickly realized the pilot is good, it's faster, we are able to deliver faster. But the pilot we built is not enough to prove that the production system works. The reason: if you take an example, you're building a Salesforce implementation — you know that if the pilot is working, your production will work, because there is deterministic behavior that you can expect. But in the case of pilots related to agentic AI, the pilots may work faster because onboarding is super fast — you just buy a $20 cloud account and you start building it. So you can build quick pilots, but the same pilots won't work in the context of production. The reason is simple: the deterministic behavior is not there in an LLM. When you are testing, you take a small scope of the problem and test it with a limited context and a limited set of tools. But all these constraints are artificial in a pilot. When you go to production, they are not artificial anymore. There is an open area where there are a lot of things that will block the implementation.

So what did we observe when we moved from pilot to production? When we started, it was a small demo application with some tens of instructions given, and the output is super fast and very nice. But the moment we started adding our proprietary knowledge base of the product — each agent has exhaustive prompts and rules; we had to write a lot of rules to make the LLM understand how our product works. To complete the entire behavior, we had to write a lot of tools. If you take any example of an enterprise application, you may have a lot of functionality — everything has to be written as a tool — and we had added a lot of agents. At that point there was no insight into what is happening, how this whole execution is happening. If you look at any distributed application, you have tracing, you have logs. But in the initial days of this implementation there was no visibility into the execution.

So how did we solve it? These are the problems we have seen in enterprise applications, and this is the kind of problems you will also see when you move into an enterprise AI. Today I'm going to talk about four failure patterns that we found, how we solved them initially, and how you can solve them now — the technology has advanced a lot in the last year.

### Problem 1 — Context overload

Every agent in our system had a lot of instructions, and along with that we have documentation, examples, a lot more things, and that became a bloat. Given that everything has to work in the context window of the LLM, there is very small space for reasoning. So that became a problem.

When your user makes a request — "I want to import my database into this application" — the same request is not sent to the LLM as-is. There are a lot of system instructions we give along with the user request. And to perform those operations, you have to have certain functions exposed to the LLM, like an API. That API is called a tool in the LLM world. Every operation you want to perform on my platform, the LLM has to call a tool, and that will invoke the platform.

So the context contains not only the user request — it contains the system instructions given behind the scenes, the tool information (what APIs are available in my platform which the LLM can invoke), and some context about your application (what your application already contains). When we give all these things, there is a limit of context size — 200k tokens for any LLM. So those 200k tokens are getting consumed and the LLM has no space for reasoning. The context got bloated, and because of that, hallucination increased, our token costs increased, and reasoning became inconsistent.

Simple example: we have a security agent. That security agent has instructions for how to configure a database provider, how to configure OAuth-based implementation, or JWT, or Google SSO — different instructions in the same security agent. Now the user is asking, "I only want to enable OAuth." But because this instruction set has everything related to all types of providers, everything went into the context — a lot of information is irrelevant. What the LLM has to know is only how to enable OAuth, nothing else. But because our instruction set has everything in one agent, everything is being sent. The model is spending more time filtering the noise than on the real content. Even if you look at a larger model with a bigger context window, this was not helping us, because the information is irrelevant. So you have to give the model what is required, not everything you have.

**Solution: progressive disclosure.** Give the model information when it needs it. Don't give everything at once. The industry calls this progressive disclosure — you disclose the information when the model asks for it. It's like lazy loading in software terminology. With progressive disclosure, I am not pumping my entire security agent at once. I am only telling it, "I have these providers which I can configure; now tell me which provider's additional details you need."

How do you achieve this in an LLM? That's where skills come in. Skills enable you to expose information to the LLM in a progressive manner, on demand. A skill contains a name and a description — these are the two important things — and the rest is the system instructions of the skill. When the agent sends the message to the LLM, it is only sending "I have this skill and this description," nothing else. That way my prompt becomes very compact. When the LLM needs it, it will say "load me this skill," then you send the additional set of instructions. Now the LLM context has very small information required to finish the task, it is more predictable, no hallucinations, and your token costs are reduced — imagine there are thousands of instructions, but now I have only 20 instructions to solve a problem.

So my architecture has changed four times in the last year. Every time we had to adapt to new market trends and make the output predictable. We modified all our agents to skill-based systems — every agent has a set of skills. That's how we solved the context overload problem.

### Problem 2 — Tool explosion

A tool is a capability in your platform. Can you add JWT authentication? Can you add SSO authentication? To enable that, I need one API in the platform — that is a tool. App generation has a lot of functionality, a lot of things I need to generate inside the application, and for every such thing we added one capability. We kept adding capabilities to reach the end goal, and ended up with 200-plus tools in the platform.

Even if every tool takes about 200 to 300 tokens, 200 tools became some 6,000–7,000 tokens. I took data from online sources to see whether we were doing something wrong or whether the industry has this problem too. From publicly available information: GitHub has 35 tools and 26k tokens. Slack, Sentry, Grafana — everybody has a set of tokens for their tools. In your enterprise, if you are using a Jira tool, you have 17k tokens added to your context window out of 200k. If your API requires integration with all these services, you are almost spending 72k tokens — about 36% of your token window.

We observed the same in our system: even though 200 tools are required for our functionality, the context window needs to be reduced. I cannot reduce the capability of the system; I cannot ask my developers to stop writing tools. The more tools you add, the performance degrades — both in latency and in tool selection, and even in the output. Anthropic claims that if you have more than 50 tools, your performance is going to get reduced by 30%. The same thing happened to us.

**Solution: progressive disclosure of tools (Tool Search Tool).** You don't load all the tools; the LLM asks for the set of tools it needs in a semantic-search way. That is called the Tool Search Tool — a tool that has access to all the tools in the system but is not counted toward your context window and is not even loaded into it. When the LLM needs tools related to a particular context, the tool search will search for the relevant tools and give only the currently matching tools. Now the LLM only has the limited tools required to finish the job.

Example: "investigate the failures" was the issue. There are 200 tools, but it knows it only needs the log analyzer and maybe a token decoder — so only those three tools get added to the context window, not the whole set. The context window is now freely available for reasoning. A report from Anthropic: in a traditional setup without the tool search tool, about 40% of the space was used by tools; with the tool search tool, it was reduced to 2% — about an 85% reduction in token usage.

Anthropic invented this about 6 months ago, and now OpenAI has started supporting it too. Should you always use the tool search tool? No — it adds one extra step (an extra hop), so there is a slight delay. Don't use it if you have fewer than 20–30 tools; use it directly in that case. If it is more than that, use the tool search tool. That's how we cut down the tool-explosion issue.

### Problem 3 — Complexity in agent orchestration

We created agents such that for every feature of the product there is one agent, and that agent is like a domain expert. A database agent knows how to write queries and read the metadata of a table; a security agent knows security. We thought that would help structure the agents. But in an orchestrator pattern, the request first comes to the orchestrator, then goes to the DB agent, and so on.

Best example: "I want to build an employee onboarding page." The request comes to the orchestrator. The orchestrator knows that to finish employee onboarding it needs to first understand the database schema, create a backend API, and build a UI. First it asks the database agent: is there a database with an employee table? The agent responds, "the table is available," and that information comes to the orchestrator. The orchestrator plays it back to the next agent in the plan — the backend agent — to add the respective backend implementation. When you do this transformation from one agent to another, the database agent sends a summary of the task it performed to the orchestrator, then the orchestrator sends the summary to the next agent.

What happened? First, there are too many hops for a simple task — it takes a lot of time (latency). And there is information loss. Take this example: you have an employee table with a manager-ID field (which you'd see in any HR portal), where the manager ID can be null — except for one person. There is no database constraint where you can say "only one person can have it null." But the LLM is smart enough to understand, by looking at the schema, that except for one employee (the CEO or similar), there should be a mandatory manager ID. That is a discovery the database agent made — but that summary was not passed to the orchestrator to pass to the next agent, because agents cannot share context windows. The second agent never knew this validation is required.

So the implementation was working fine — DB was readable, we created the backend API, we built the UI, and everyone says "I'm done, successfully." But the end result is that the business rule was not applied: the validation was not there in the backend, the front end, or the DB. That was the information loss, and these are very common issues we have seen.

**Solution: decide agent vs. skill vs. tool.** When do you create an agent? If you make very small agents, the problem is collaboration becomes difficult — you have to pass information from one agent to another. But if you share context across all agents for the same request, then all the instructions from all agents go into one single context window and it goes out of space. Given that skills are now available, we changed our architecture a bit: don't create smaller agents — instead of creating agents, create a skill. Now I have one code-generator agent, and the rest are my skills, which only get loaded when required. Even though I have 10 different skills, not all 10 get loaded — only one or two, depending on your request. Because a skill runs in the shared context of the agent, when the database part figures out a validation is required, it is running in the same context and is able to understand that validation and perform better.

So when to use what: an agent owns an end-to-end job — its responsibility, like a manager in a company (e.g., it has to do a code review with the help of multiple skills); a skill is a capability ("how do I do this?"); a tool is the action, the thing that really does the job. Now our agentic platform has become one agent, multiple skills, and each skill contains the tools it needs. With this, our token cost reduced, hallucination came down, we can predict what is happening, and there is no loss of information. It doesn't mean you should not create agents — you should decide when to create an agent and when to create a skill.

### Problem 4 — The execution black box

Initially, when we were building the platform, there was no way to understand how to debug the system when there is a problem. There is a 10-step plan provided by the orchestrator. After, say, the fourth step, because of some deviation, it started drifting. The LLM never gives up — it continues to try its own options, takes a lot of loops, tries all different ways to solve the problem, then finally it broke and the output didn't work as expected. So there were 10 steps, and after the fifth step, for whatever reason, it didn't perform well, then it started hallucinating and doing something else. In such a system, how do you understand what was in the fifth step? What was the context sent to the LLM at the fifth step?

That's where we spent a lot of time probing an agent. What do you need to know when probing an agent? One, you need traces — how many times the LLM has communicated, human versus LLM. If you look at the whole system: there is a request from the user, a user intent which is just one simple prompt, but behind the scenes it sends all this context to the LLM; the LLM comes back and asks to execute certain tools; the tools come back with a response; that response is given again to the LLM. That loop continues until the end result is achieved. The user doesn't even know what is happening unless you give them a UI — if you look at ChatGPT, it simply says "thinking," but you can give more information ("I'm executing this tool, that tool").

So you need to build a system around it. You need to figure out these traces and understand, at any point in time, what is in the context — that is most important, because the context contains system instructions, tool requests and responses, history, and information about your project. At any point of time I should be able to open a dashboard and see this, and also see the tool execution — how many APIs were called, what requests were given to tools, what responses came out. There was no easy way for us to do this until Langfuse released its open-source platform. We were trying our own custom solutions to monitor the system, but there is an open-source plugin you can use. You have to invest early in building these systems, otherwise debugging will be very tough in an agentic system, because there are too many parts involved.

### Lessons

- The LLM should only be given information when it needs it — don't dump everything into it. Progressively disclose information to the LLMs. That gives predictability and reduces costs.
- Use multi-agent orchestration carefully. Decide when to do agent vs. skill vs. tool — whether you are building an ownership, a capability, or an action.
- Invest early in observability. There are a lot of tools available now; start from day one so you can easily debug, then optimize for predictability.

These are just a couple of the problems — there were a lot of other things we observed (cost optimization, caching, and more). Finally: agentic systems are built through engineering. You still need engineering effort, not just a model. The model is just one component. The industry is saying only builders are required, but engineers are still required.

Thank you. I'm open for questions.

### Q&A

**On what investing in observability means / which tools:** Most of the time logs are good enough for normal non-agentic applications; even in distributed applications you have distributed tracing with some ID. But in an agentic world, the more important thing to observe is what is in the context at any point in time for every request — instructions, tool requests and responses, history; the whole context window needs to be debugged. For this we used LiteLLM with Langfuse, because these are open-source tools and easy to integrate with any agentic system, including LangGraph (you can use LangGraph with Langfuse and LiteLLM). There are also a lot of commercial products now.

**On prompts becoming technical debt as models update:** The model is going to get better, but your domain knowledge never changes. When do you get a chance to change your prompt? Basically when we missed some instructions, we went and added them. But most of the time you should be looking at how the market is evolving — your domain knowledge will not change, but you need to leverage new emerging trends. We started with everything pumped into one agent; then skills came up and we switched to skills. Now there are still problems — imagine you have a single agent and everything else is a skill, and to perform a task you might need to load 10 skills, which again bloats the system; then you need to understand how to compact the context window, how to summarize, and other techniques. We changed our architecture four times in one year. This is inevitable given the pace at which LLMs are improving.

**On giving the agent what it needs when it needs it — does the orchestrator need more global information?** In our case the orchestrator never had global information — it only had a summary of the task performed by every agent. The newest pattern is a planner agent, which contains the overall plan and delegates. But you need to be very careful, especially about the output of the agents. The problem is not the delegation — the problem is the summary that is sent from an agent to the parent agent. Even in multi-agent orchestration you still face these problems. Create an agent that is completely independent and can do its task given a simple query. Example: for code generation I built one agent, but review is a different agent. For review, all it needs is the changes in the source code — it can get that using git diff or other tools and be independent. When you think a task can be independently managed, that is an agent.

**On correlation between correctness/agentic performance and monorepo vs. distributed repos:** I don't see a correlation. It's not about where the code exists; it's about what is put in the context. If you have many repos and your task requires all the files loaded into the context, that's where the challenge is.

**On giving agents web/tool access:** In our case we didn't want to give the agent internet access, because hallucination increases. We wanted the LLM to operate in my project context, not externally. It already knows how to do certain tasks — it already knows coding — so it doesn't really need live information. What it needs is how to do this in my project; for that I don't need web access. For developer docs (which were proprietary), we used a RAG system to load the documents required for a given task.
