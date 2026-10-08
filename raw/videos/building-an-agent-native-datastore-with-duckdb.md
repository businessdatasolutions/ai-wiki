---
title: Building an agent-native datastore with DuckDB
video_id: vtll31BjojA
url: https://www.youtube.com/watch?v=vtll31BjojA
channel: MotherDuck
channel_id: UCC0AT6XjO_ebWIifTDp5REg
channel_url: https://www.youtube.com/channel/UCC0AT6XjO_ebWIifTDp5REg
publish_date: '2026-10-06T01:08:31-07:00'
upload_date: '2026-10-06T01:08:31-07:00'
category: Science & Technology
duration: '28:05'
length_seconds: 1685
view_count: 27
is_live: false
is_upcoming: false
is_private: false
is_family_safe: true
thumbnail: https://i.ytimg.com/vi/vtll31BjojA/maxresdefault.jpg
keywords:
- AI SRE
- AI agents
- Amsterdam
- DuckDB
- GlassFlow
- MotherDuck
- agent observability
- data engineering
- embedded database
- meetup
caption_tracks:
- language_code: ar
  name: Arabic (auto-generated)
  kind: asr
  is_translatable: true
- language_code: bn
  name: Bangla (auto-generated)
  kind: asr
  is_translatable: true
- language_code: nl
  name: Dutch (auto-generated)
  kind: asr
  is_translatable: true
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
- language_code: fr
  name: French (auto-generated)
  kind: asr
  is_translatable: true
- language_code: de
  name: German (auto-generated)
  kind: asr
  is_translatable: true
- language_code: iw
  name: Hebrew (auto-generated)
  kind: asr
  is_translatable: true
- language_code: hi
  name: Hindi (auto-generated)
  kind: asr
  is_translatable: true
- language_code: id
  name: Indonesian (auto-generated)
  kind: asr
  is_translatable: true
- language_code: it
  name: Italian (auto-generated)
  kind: asr
  is_translatable: true
- language_code: ja
  name: Japanese (auto-generated)
  kind: asr
  is_translatable: true
- language_code: ko
  name: Korean (auto-generated)
  kind: asr
  is_translatable: true
- language_code: ml
  name: Malayalam (auto-generated)
  kind: asr
  is_translatable: true
- language_code: pl
  name: Polish (auto-generated)
  kind: asr
  is_translatable: true
- language_code: pt
  name: Portuguese (auto-generated)
  kind: asr
  is_translatable: true
- language_code: pa
  name: Punjabi (auto-generated)
  kind: asr
  is_translatable: true
- language_code: ru
  name: Russian (auto-generated)
  kind: asr
  is_translatable: true
- language_code: es
  name: Spanish (auto-generated)
  kind: asr
  is_translatable: true
- language_code: te
  name: Telugu (auto-generated)
  kind: asr
  is_translatable: true
- language_code: uk
  name: Ukrainian (auto-generated)
  kind: asr
  is_translatable: true
thumbnails:
- url: https://i.ytimg.com/vi/vtll31BjojA/hqdefault.jpg?sqp=-oaymwEmCKgBEF5IWvKriqkDGQgBFQAAiEIYAdgBAeIBCggYEAIYBjgBQAE=&rs=AOn4CLBwwz0ezR0JC1kyopPYOemJ3pgdAg
  width: 168
  height: 94
- url: https://i.ytimg.com/vi/vtll31BjojA/hqdefault.jpg?sqp=-oaymwEmCMQBEG5IWvKriqkDGQgBFQAAiEIYAdgBAeIBCggYEAIYBjgBQAE=&rs=AOn4CLAMDxtv5C3wsJxaaNoNlfKJzZtRBw
  width: 196
  height: 110
- url: https://i.ytimg.com/vi/vtll31BjojA/hqdefault.jpg?sqp=-oaymwEnCPYBEIoBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLB36eBz-s3W0UDtd8dbwJaHGrEffQ
  width: 246
  height: 138
- url: https://i.ytimg.com/vi/vtll31BjojA/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCvHyLblywUgjac-TXmhVQJv-ItNg
  width: 336
  height: 188
- url: https://i.ytimg.com/vi/vtll31BjojA/maxresdefault.jpg
  width: 1920
  height: 1080
chapters:
- title: Intro
  start: 0:00
  start_ms: 0
- title: What happened to checkout-service?
  start: '1:51'
  start_ms: 111000
- title: The consumer changed
  start: '3:36'
  start_ms: 216000
- title: What we set out to build
  start: '5:49'
  start_ms: 349000
- title: 'End of May: twelve components, and who would run them'
  start: '7:24'
  start_ms: 444000
- title: One table, nine columns, every source
  start: '8:57'
  start_ms: 537000
- title: No indexes on the events table
  start: '10:19'
  start_ms: 619000
- title: One read query
  start: '11:30'
  start_ms: 690000
- title: A trigger is a GROUP BY
  start: '12:09'
  start_ms: 729000
- title: The agent's data model is the catalog
  start: '13:03'
  start_ms: 783000
- title: 'What it cost: memory, disk, retention'
  start: '13:38'
  start_ms: 818000
- title: 'Demo: an AI SRE with Tares'
  start: '15:33'
  start_ms: 933000
- title: What you can build with Tares
  start: '16:33'
  start_ms: 993000
- title: Wrap-up
  start: '17:26'
  start_ms: 1046000
- title: Full Tares demo walkthrough
  start: '17:51'
  start_ms: 1071000
description: |-
  GlassFlow's first design for agent observability was twelve components: brokers, an external database, the lot. They threw it away and rebuilt it on one DuckDB file per project: one table, nine columns, no indexes, and a single read query. Ashish Bagri walks through what that cost them and what it bought.

  In this video Ashish Bagri, co-founder and CTO of GlassFlow, explains why a product built for non-agentic streaming workloads was the wrong starting point, how Tares stores every connector's events in one JSON-payload table, why a trigger is really just a GROUP BY, and where DuckDB pushed back — memory overflow at a million events on a small VM, disk pressure, and retention. Recorded at the Agents in Prod meetup in Amsterdam, hosted by MotherDuck.

  📓 Resources
  GlassFlow: https://glassflow.dev
  MotherDuck: https://motherduck.com
  DuckDB: https://duckdb.org

  ➡️ Follow Us
  LinkedIn: https://www.linkedin.com/company/motherduck
  X: https://x.com/motherduck

  Chapters
  0:00 Intro
  1:51 What happened to checkout-service?
  3:36 The consumer changed
  5:49 What we set out to build
  7:24 End of May: twelve components, and who would run them
  8:57 One table, nine columns, every source
  10:19 No indexes on the events table
  11:30 One read query
  12:09 A trigger is a GROUP BY
  13:03 The agent's data model is the catalog
  13:38 What it cost: memory, disk, retention
  15:33 Demo: an AI SRE with Tares
  16:33 What you can build with Tares
  17:26 Wrap-up
  17:51 Full Tares demo walkthrough

  #DuckDB #MotherDuck #AIAgents #DataEngineering #Observability
playability:
  status: OK
  reason: null
notes: |
  Acquired 2026-10-06 via youtube-transcript-skill (fetch_transcript.py --json,
  rendered with its to_markdown) for a tutorial requested by the user; no wiki
  page written (Acquire only). Auto-generated (ASR) English track; 204 segments,
  complete 0:05-28:02 of 28:05, 15 creator chapters, no doubled segments.
  Proper nouns corrected at acquire time (23 replacements): GlassFlow, DuckDB,
  MotherDuck, agent native, MCP, Claude Code. NOT corrected: the product name
  Tares, which the ASR renders as TAS / TARS / Taurus / TS / RS / SARS / Dallas.
  Talk recorded at the Agents in Prod meetup, Amsterdam, 17 September 2026 (date
  from the title slide). Stills manifest alongside:
  building-an-agent-native-datastore-with-duckdb.stills.md (Gemini full scan,
  158,320 tokens, 17 stills; verified at tutorial time, not yet at Process).
---

## [0:00] Intro

[0:05] [music]
[0:10] So hey everyone, nice to see all of you here. My name is Ashish. Uh I'm the CTO and co-founder of GlassFlow. A few
[0:18] words about myself. Uh yeah, my like I have a background in machine learning and data. Started off writing uh machine learning algorithms 15 years ago or so.
[0:29] uh before transformers were a thing. Uh then spent the last years building yeah data pipelines, machine learning
[0:36] algorithms still leading teams basically doing all of that. Uh with always the manner of bringing more machine learning
[0:43] into production uh since the last few years been running GlassFlow. Uh yeah.
[0:49] Uh so today is part of a event series that we run called agents in prod uh with the goal of essentially what does
[0:58] an agent need when it's running in a prod and not in a notebook. Uh yeah thanks again for MotherDuck for hosting us
[1:04] today. Uh yeah today's talk is about building an agent native uh data store with DuckDB. Uh the the talk today is divided into three halves basically.
[1:16] First half would be why why did we think that we need an data store for an agent?
[1:22] What does it mean to actually have what does a data store for agent even look like? What does it even mean? Then we talk about how does DuckDB play a role
[1:30] and then we end up with a demo on how everything comes together. Uh yeah, the product that we basically are building is called TAS. So it's uh yeah, it's open source uh built by glass.
[1:44] Let's start.

## [1:51] What happened to checkout-service?

[1:52] Okay. So, let's start with an uh error situation. So, uh you have an alert on Slack which talks about uh which pings
[2:00] and says something is happening on your checkout service. You have an agent running on the systems. You ask the agent what happened to the checkout
[2:08] service. Uh the agent has access to all the underlying systems. It has access to your Prometheus, your logs via Loki, uh
[2:17] your GitHub, even deploy logs, all of that. The agent starts investigating. It goes in and it pings all of these
[2:26] services. Each of them has their own MCP server or service and it tries to figure out together what exactly happened. What
[2:34] this means is that it's going to connect to all of these MCP tools, figure out like the the capability of these tools,
[2:42] pull the data in, try to make the context and align the timeline in its context and figure out like what came before what to come up to a reasoning.
[2:51] It actually does that eventually, but it takes more it's more expensive and more slow than it should be. So then we tried
[3:00] basically by putting all the data already together, right? And then the agent basically was able to get all of
[3:06] this data with one single store, one single tool call uh and gave us more precise results much faster and much
[3:16] cheaper. And then we tried instead of actually letting the agent pull we when there was an error we pushed to the
[3:23] agent the trigger and the data attached to it so that the agent basically starts we're already seeing what is exactly
[3:31] happening. Uh so this basically is where we started to think about like uh agent

## [3:36] The consumer changed

[3:38] data store and why did we think about that? So as I said I've been building data systems for a while. I spent a lot of time building the modern data stack.
[3:48] And in that sense, if you if you compare what a lakehouse basically was, it
[3:55] basically let analysts create data views on the raw data, right? And that flow
[4:02] typically looked like was a dashboard needed to be built. Uh you would go as an analyst go and talk to the stakeholder understand what they
[4:10] wanted to see. You go basically as analyst go back build your data models use dbt spark whatever you you were
[4:18] using and then deploy it and then the dashboard was working. This cycle typically was slow it took time but it worked. But what has changed is the
[4:27] consumer. Now the agents are doing that basically and the kind of data that the agent needs is is different. The kind of
[4:36] the agents are able to understand much more data together. they are able to request more information to come up with
[4:44] a more precise conclusion. Uh what we wanted basically in such a store was that all the data basically is aligned
[4:51] and is available across many systems in one uh timeline basically.
[4:58] And we basically started to think about like oh we would like to actually push this information to the agent and not
[5:05] just have the agent wait uh and and query us. Uh and all of these basically
[5:12] together is what we mean by an agent native data store. It's not simply a database which agents happen to query
[5:20] but it's it's a much more complete framework which lets agent define what
[5:27] data views should exist there what kind of uh queries that they are able to run what
[5:35] kind of data that can they are able to pull basically and essentially do the things that the analysts were
[5:42] also doing but basically without this whole cycle without specific prompting.

## [5:49] What we set out to build

[5:50] So we we started basically by by talking about like four properties that we wanted. So first we wanted a lossless
[5:57] system basically. So uh we didn't want to actually summarize the data and put it in a store for agents to
[6:05] query. We didn't wanted to run an LLM to have embeddings. What we wanted was raw data because every transformation you do
[6:13] embeddings or or summarization you lose some information in the data and we wanted the agent to have all the data that's available for it to come to uh
[6:22] the reasoning or the solution that it's trying to do. Uh we wanted to be organized so that the agent doesn't have to do this organization part and organization is typically deterministic
[6:31] right like you know basically how to organize the data across many different sources agent doesn't need to learn it again and again every time. uh we wanted
[6:38] it to be served two ways as I said agents are should be able to query the data but we should be able to push the
[6:44] data to the agents and uh agent shaped basically right like uh as I said like
[6:52] everything that humans are able to do on a data store the agent should be able to do that so which means able to create
[7:00] new data sources create like uh new views on that data create triggers on that views and subscribe itself to it.
[7:09] So let's say whenever something like a condition is fired, I need to be woken up basically and this is the this is the
[7:18] amount of context window that you would that I would like basically to have directly. So this were the principles

## [7:24] End of May: twelve components, and who would run them

[7:26] and this was the first diagram that we started to build. Uh
[7:34] this was roughly end of May. U as you can see a lot of components a lot of systems partly because we came from a
[7:42] world where we were doing real-time data streaming for click house and we tried to bring a lot of these concepts into this world
[7:51] but we took a step back right like that was that product that we built was built for a different era that was built for
[8:00] knowledge workloads that were built basically uh so we what we wanted to do basically was we wanted to have a very
[8:08] simple system that the user is able to run it on their machine with a couple of commands, no external dependencies, no broker, no external database to connect.
[8:17] Um we wanted AI engineers to be able to run it and not like a whole platform team that runs that. Uh right like and what
[8:26] we've ended up basically was these a complex system complex architecture which no doubt would have worked uh
[8:35] operationally very complicated and and difficult to run to what we have now basically which is a simple very very
[8:43] naive very simple system uh powered by DuckDB. It has one DuckDB file a Python process that manages everything
[8:51] around it. Um yeah and one big events table. Um

## [8:57] One table, nine columns, every source

[8:58] so now let's go into the second half of how DuckDB actually plays a role in that. Uh so here I'm going to show you a little bit about like what kind of
[9:07] queries we run, how we organize the data in DuckDB. So this is the actual table. This is the actual table of where we store events. Uh as
[9:16] you can see there's one common structure across all different connectors. So we have plenty of different connectors that we pull data from inside the tool inside
[9:23] the RS. Um the payload is the key that stores the raw data. As I said like no
[9:31] trans no like we wanted to persist the raw uh information. So that's the key that stores the raw information. Of course right now we basically work with JSON data. So it's uh has a JSON type.
[9:43] the event the the key value and the labels is basically what makes it organized. So what we do is we extract
[9:51] some key uh parameters from the event and put that as part of labels. This is
[10:00] also something that the agents are allowed to do that basically. So agents can configure that and create new labels
[10:06] and we have a couple of time stamps basically. There are other tables of course in the system but in
[10:14] terms of storing the actual data or events this is the one uh where we store all the events.

## [10:19] No indexes on the events table

[10:20] Also surprising I also had a chat earlier today is what optimizations we did actually on DuckDB none. We
[10:27] basically took the vanilla DuckDB uh I would tell you a little bit later like a couple of hard learnings but
[10:35] DuckDB lets us do this because of how it organizes data by default. So for us it creates blocks of like approximately
[10:44] 120,000 rows together. Uh the columns are stored separately. Each block has the min and max of each column
[10:52] basically. So with TAS we only actually append data. Uh so because of that new
[10:58] events carry new times and when you go and ask what happened in last couple of minutes duct TB by default skips all or
[11:05] most of the blocks basically barring the last couple of them. And so it's a it's a cheap read. Uh and none of our hot
[11:13] queries actually touched the payload which is the biggest column. U one other challenge that we already mitigated was that queries that didn't have a time
[11:22] window. We wanted to show like the counts and of the events and so on. So for that we build a couple of counter tables which are updated during the insert time.

## [11:30] One read query

[11:31] This is a read query again. So basically when we talked about coring data from multiple sources uh right like we do
[11:38] that basically by windowing. So that's the part basically where the labels that we extract we allow basically as a human you could
[11:48] do that and extract labels uh which match across different sources or the agent has the capability. So you can connect your Claude Code basically and
[11:56] let it create different labels and because of that the correlation is is again very cheap. Um yeah and this is
[12:05] basically how the agents pull the data whether via query via read operation and so on and the same for a trigger basically right like so what the trigger

## [12:09] A trigger is a GROUP BY

[12:13] does is so trigger is like like what you would imagine like a Prometheus trigger and so on. It sets a condition on the
[12:21] data and when the condition fires basically it triggers and what it triggers is it sends this to subscribers
[12:30] uh and subscribers are nothing but agents. So inside RS we also have inbuilt RS agents but also there are external agents that you can build and
[12:38] subscribe yourself to this. Um yeah and this is again like something that you
[12:46] could build on in the stream processing layer right like uh but for us to keep things operationally simple and we did
[12:55] that on top of the data basically after it has landed in DuckDB and um yeah so this is basically

## [13:03] The agent's data model is the catalog

[13:04] uh the last part is all the operations that we talked about like creating new data sources, creating new v views,
[13:14] triggers, all of this basically is catalog data data changes. The fact that the events table is is just simple,
[13:21] straightforward allows us to build everything on top of this uh and let the agents build everything on top of this
[13:28] uh basically uh and DuckDB makes it possible because of the way it's organizing the data.

## [13:38] What it cost: memory, disk, retention

[13:39] So yeah, a couple of learnings that we had initially already quickly um basically
[13:46] the first uh yeah difficulty that we ran into was like memory overflow. So uh DuckDB
[13:54] basically yeah for a for a small VM that we were running uh at 1 million events or so uh DuckDB
[14:03] consumed all the memory uh it it went out of memory so we had to adjust to do a good split between what's stored in memory and what's stored in pile uh same
[14:12] with disk space uh the process around it the tus process around it now actively
[14:18] looks at the the disk space available and it actually uh degrades instead of dead. So it basically pauses the ingest
[14:27] at around 95% so the data doesn't like grow and the system doesn't crash and you have time to update that. So
[14:35] increase your volume where the DDI file is residing. Um another thing is like payload is lossless. So you could actually go and create a new label and apply that to all the historical data.
[14:44] But that's an expensive operation in this data design. So we chose to keep the labels only going forward. when the agent says I need this data extracted as
[14:52] a label it's applied immediately but all the events coming from that point onwards if you want to do migration that's a separate background job
[15:00] basically that you would do because doing that on every reapplying label was actually killing the system yeah label
[15:08] column is a JSON looking at like to make it like a map type and another thing is like there's no data retention right now
[15:16] so everything is in the same file and it keeps growing So uh the next thing on the table basically is to do an hot cold separation uh which
[15:26] basically would allow us to actively better manage the data that's available uh yeah in the process.

## [15:33] Demo: an AI SRE with Tares

[15:34] So yeah now is the demo time fingers crossed. Uh so in this demo what we what I'm going to try to show you basically
[15:42] is how did we build an AI system reliability engineer using TARS. So for
[15:50] those of you who don't know what an SR does basically what this is supposed to do is it kind of is the first line line of defense
[15:58] example that I show started with the checkout service is failing you would get an alert on Slack saying something is happening on your service with this
[16:07] the when you get an alert you already start with an agent already having looked at that and you start with like a
[16:14] root cause analysis of like what exactly happened why it failed and I'm going to show you how easy it is to with stars.
[16:21] So uh uh so that was the demo. Let's go back uh quickly.

## [16:33] What you can build with Tares

[16:33] Uh yeah. So what can you build with TARS? So so far uh basically
[16:40] uh as I showed you like an AI sur we also have use cases around like building shared code context. So when you have
[16:48] like multiple GitHub repositories basically for your same product like a UI repository and a and a internal info repository and so on you could build
[16:56] like a system where TS is monitoring everything and every commit that happens in any of these repositories it kind of maintains a shared context. Um you can build like yeah a challenger workflow.
[17:07] So every time you work with locally Claude Code, you can trigger a challenger workflow that's going locally to uh a
[17:15] codeex terminal and then you use TAS to keep a record keeping to see exactly what happened. Uh yeah, for any kind of like failure mode, any kind of
[17:23] triggering, any kind of anomaly detection, you could run basically with TARS. So yeah, that's I think yeah, that's the everything.

## [17:26] Wrap-up

[17:35] Yeah, please scan the QR code. that leads to your uh to the GitHub repo. Um yeah, if you want to keep in touch,
[17:43] start the repo, play around uh over the weekend and let us know what you build. Thank you. Any question?

## [17:51] Full Tares demo walkthrough

[17:52] Hi everyone, welcome to the demo of Taurus where we will build an AI SRV using Taurus.
[18:02] Uh let's start. So here I already have connected TARS to
[18:11] uh a service that we are running. It's a demo API server. Uh here I have connected three data services uh to TAS.
[18:21] The logs, the metrics and the alerts. Uh there are already data that's been ingested into TAS by these three systems.
[18:31] uh um in Taurus if you look uh let's let's
[18:38] take a look at the what SARS connects so you connect all the three sources we have inbuilt integrators uh to all
[18:46] different kinds of systems uh with after the sources are connected you can create different views on that data here there's a view called service
[18:54] timeline which connects all the three sources together over a key called uh service which carries right now only one
[19:03] value which is an API server um and that there's a trigger which is
[19:11] basically some condition that fires uh based on a view. So there's a condition
[19:18] here which is uh watching the data that's coming through this view service timeline
[19:24] uh and whenever there is an um alert active which is a field that's set for any kind of alert that's been fired by
[19:33] Prometheus whenever there's any alert fired over a time window of 1 minute it
[19:40] basically triggers any subscribers and in this case a subscriber is a t agent that's inbuilt Here
[19:48] uh the cool down is that it basically only triggers once every 5 minutes. Uh but in every figure it connect collects the data for the last 15 minutes over
[19:56] the view and send it to the agent. So the agent doesn't wake up cold. Uh TS
[20:03] agent basically itself is uh connected here. You can connect different models basically. You can send give it the budget the number of routes it's allowed
[20:11] to do and it the prompt basically and you can even configure um external MCP servers if you want to
[20:19] give additional capability to the agent for example the mega PR or to pull additional data from any external service that you don't want to connect to TARS directly.
[20:29] uh you can also send the data from the agent into um uh into external systems via web hook
[20:37] or slack and so on. Yeah. So this is kind of like the setup of TARS. Uh so yeah um now
[20:46] what I let let's take a look at what data has been collected. So uh as I said everything is on correlated on a key
[20:54] called API server. you see the data across many different uh services here basically right now and
[21:01] uh since I said it's everything is agent native you can connect also uh several MCPs uh so several
[21:10] uh agents your agents or your harnesses into TAS via MCP I already connected now
[21:19] here uh for this demo Claude Code basically uh into Taurus.
[21:35] Uh basically let's uh go and ask cloud what is happening in Dallas.
[21:45] So with this what? Yeah, with one uh query it's going to be able
[21:53] to pull all the data that exists for the API server over the last 15 minutes. Uh
[22:00] so
[22:14] yeah, it says it it looks healthy. No, no problems basically. And now let's go back to
[22:23] here. And what I'm going to do is I'm going to create an incident. So we have this lever built basically and I call
[22:30] that incident. It flips a switch basically on the uh demo service which starts to send more 500 errors and we should start
[22:39] to see that already happening in a few seconds. So as events. So you see that there are 500 errors coming in. What's
[22:47] going to also happen is that Prometheus basically will fire uh in about 30
[22:54] seconds or so. Uh because this is high in this example we have used Prometheus.
[23:00] You could have also built the alert directly within DS by using the views and triggers. So uh yeah in a few
[23:09] seconds basically there will be a firing which will uh then exactly so as we speak here there's a firing what happens
[23:17] in the firing is that uh Tus basically got a fire from Prometheus saying oh something is
[23:25] happening. What RS did was it collected all the data across all the services uh including logs and metrics basically and
[23:33] then as you see logs and metrics combi uh over the last 15 minutes uh put them
[23:40] together and send it delivered to an agent. The agent basically caught this uh data. it then had to go and get more
[23:48] information because all the information was already here uh and it was able to actually come to some kind of a conclusion of what is actually
[23:57] happening. So in this case you basically build like an AI sari which is taking a first look at your incident and instead
[24:05] of your alert manager firing into slack saying something is happening you basically have an alert along with uh and uh RCA directly attached to it.
[24:18] What's also cool is that the agent writes the information back into Taurus.
[24:25] Uh so if you look at this the agent wrote it back as a finding right and what will happen is that next time when
[24:31] there's an alert firing the agent basically which we should see in like 5 minutes or so uh you would see
[24:40] that the agent will get the data u will basically get the earlier finding and we'll be able to build on top of
[24:49] that. Uh so while this firing is happening let's go and take a look at some
[24:56] uh something else. So as I said like like with TARS we give agents capability to not just query data but to actually
[25:04] create different kinds of views. So here basically I want to I'm asking Claude Code that okay use SARS and
[25:13] start watching the P99 legend for the API server and then whenever something is happening there please wake up the is there a first location that I already
[25:20] have. Uh so when I do this uh TAS uh so
[25:28] Claude Code is able to use TARS to be able to uh create different triggers and uh views uh which will also fire.
[25:39] So when this happens basically this will lead to uh the data being fired. So let's come
[25:46] back here. Basically uh I am going to clear the fault so that the error spike is not happening. Uh and
[25:56] uh in this meantime basically we have the views that agent created. So if you
[26:03] see this here this is created by an agent uh it's looking at a metrics add a filter automatically and already attached the
[26:11] trigger and the trigger is delivering to uh the agent that we already had built and here you can see the last Friday
[26:19] that we had. So if you see like a simple prompt led to cloud being able to actually configure your system so that you can start to
[26:27] monitor more. So now what I'm going to do is uh we have a latency uh switch. So
[26:34] I'm going to cause an incident uh which will spike up the latency and what will happen is that there will be a firing
[26:41] now and an agent basically will be woken up. So if I look at the trigger basically which the agent created there
[26:50] has been no firings yet. In about 30 seconds or so, there should be a firing that will wake up the agent and we will
[26:59] get an uh RCA for it. Uh
[27:05] yeah. Uh good. So great. So we have that. Now there was recent fire. If you look at the fire, this is what the agent
[27:12] will send. Basically, it was delivered to the agent. The agent is now reasoning. uh it will also have access
[27:20] to the earlier findings because it's the same entity API server. So yeah the picture is not complete. So it's
[27:28] basically able to understand and say okay there is a high P99 uh it [clears throat] is also able to
[27:36] say the highs basically. So yeah with this as you see the
[27:42] um with like all you have to do basically in the build sur is connect your data
[27:50] sources and then everything else can be handled by cloud. Thank you.
[28:02] [music]
