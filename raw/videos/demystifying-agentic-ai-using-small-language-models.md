---
title: Demystifying Agentic AI Using Small Language Models [PyCon DE & PyData 2026]
video_id: nk5BNz8v_9E
url: https://www.youtube.com/watch?v=nk5BNz8v_9E
channel: PyData
channel_id: UCOjD18EJYcsBog4IozkF_7w
channel_url: https://www.youtube.com/channel/UCOjD18EJYcsBog4IozkF_7w
talk_page: https://2026.pycon.de/talks/YZM8TA/
presenter: Serhii Sokolenko
event: PyCon DE & PyData 2026, Darmstadt — recorded 15 April 2026
publish_date: '2026-08-25T11:20:23-07:00'
upload_date: '2026-08-25T11:20:23-07:00'
category: Science & Technology
duration: '32:00'
length_seconds: 1920
view_count: 8731
default_language: null
is_live: false
thumbnail: https://i.ytimg.com/vi/nk5BNz8v_9E/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGsgayhrMA8=&rs=AOn4CLBc-pffivFBh_GPKqVxVqsTjbtw3g
keywords:
- PyCon DE
- PyCon DE 2026
- PyData
- Python
- conference talk
- data science
- machine learning
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
description: "\U0001F50A Recorded at PyCon DE & PyData 2026, 15.04.2026\nhttps://2026.pycon.de/talks/YZM8TA/\n\n\U0001F393 Watch Serhii Sokolenko demystify agentic AI as he reveals how to build powerful, scalable data agents using Small Language Models and Iceberg tables—without the need for a GPU farm.\n\nSpeakers:\nSerhii Sokolenko\n\nDescription:\nAgentic AI utilizes language models as decisioning engines to perceive environments, make decisions, and execute actions to achieve specific goals. While large language models (LLMs) are often used for these reasoning loops, they are computationally expensive and contain redundant data. Small language models (SLMs), defined as models with 10 to 30 billion parameters that fit within 16 to 32 gigabytes of consumer RAM, provide a cost-effective, private alternative for agentic workflows.\n\nEffective agents require four core capabilities: task decomposition, tool calling, glue code generation, and instruction following. The Salesforce xLAM-2 model,\
  \ a 32-billion parameter open-source SLM created via supervised fine-tuning on synthetic function-calling data, demonstrates accuracy comparable to much larger proprietary models on the Berkeley function calling leaderboard.\n\nA practical implementation stack for local experimentation includes xLAM-2 with 4-bit quantization, the Llama.cpp inference server for GPU acceleration on Apple silicon, and the LangChain framework for orchestrating agent logic. To prevent hallucinations and ensure data integrity, agents can be integrated with Apache Iceberg lakehouses to access verified business data. This approach allows developers to replace rigid directed acyclic graphs (DAGs) with flexible business rules and guardrails.\n\n⭐️ About PyCon DE:\nPyCon DE is the leading conference on open-source Python applications in AI and data science. It brings together industry professionals, researchers, AI and data science practitioners, and software engineering communities, providing a unique platform for\
  \ collaboration, knowledge sharing, and innovation.\n\nThe PyCon DE & PyData 2026 conference delivered an exceptional experience, fostering stronger connections within the Python community while showcasing the latest advancements in artificial intelligence and data science. Attendees enjoyed a diverse and engaging program of talks, workshops, and networking opportunities, further establishing the conference as a premier event for Python, AI, and data science enthusiasts across Germany.\n\nPyCon DE 2027 will take place in Heidelberg from 19 to 23 April 2027.\n\nFollow us:\n   •  Newsletter: https://2027.pycon.de/newsletter/\n   •  LinkedIn: https://www.linkedin.com/company/pyconde\n   •  X: https://www.x.com/pyconde\n\nLinks:\n   • Conference website: http://pycon.de\n   • Other sessions: https://2026.pycon.de/talks/\n\nThe conference was organized by\n   • Python Softwareverband e.V.: http://pysv.org\n   • Pioneers Hub gemeinnützige GmbH: http://pioneershub.org\n   in collaboration with\
  \ NumFOCUS Inc.: http://numfocus.org\n\n\nIf you enjoyed this session, please like, and subscribe to our channel for more insightful talks and discussions.\nShare this video with your network to spread the knowledge!\n\nHashtags:\n#Python #PyConDE #PyData #OpenSource #AI #DataScience #MachineLearning #SoftwareEngineering #LLMs #Community #Sovereignty\n\nAcknowledgements:\nSpecial thanks to all the volunteers and sponsors who made this event possible.\n\nAbout:\nPython Softwareverband e.V.:\nPySV is a non-profit that promotes the use and development of Python in Germany through events, education, and advocacy, fostering an open Python community.\n\nPioneers Hub gemeinnützige GmbH:\nis a non-profit fostering innovation in AI and tech by connecting experts and promoting knowledge exchange through events and collaborative initiatives.\n\nNumFOCUS Inc.\nsupports open-source scientific computing by providing financial and logistical support to key projects like NumPy and Jupyter, promoting sustainable\
  \ development and collaboration.\n\n\nwww.pydata.org\n\nPyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R."
notes: 'Acquired 2026-09-04 via youtube-transcript-skill (Playwright/Chromium). Auto-generated (ASR) English track; 299 segments, no chapters published by the channel. ASR clean-up applied programmatically: filler words (uh/um) stripped; proper nouns and product names corrected — agentic (from ''aantic''/''aentic''), Nadella, Russell & Norvig, Blade Runner / Eldon Tyrell, Claude Opus 4.5, Kimi K2, DeepSeek V3.2, Qwen, xLAM-2 (from ''XLM2''), LangChain, LlamaIndex, llama.cpp, vLLM, Marimo, dlt, dbt Core, Polars, Apache Iceberg, Together AI, Hugging Face, Modal, pyproject.toml, Agentforce, Cloud Dataflow, Databricks, Cursor, talks.pycon.de. Timestamps preserved verbatim. The talk-page abstract (structured outline + speaker bio) is reproduced below the transcript under ''## Talk page (2026.pycon.de/talks/YZM8TA/)'' because the PyCon session page and the recording are the same source seen from two sides.'
---

## Transcript

[0:06] Thank you everyone. I am based in Berlin. Tower is a startup in the

[0:12] Berlin area. we got founded about 18 months ago. But this talk is not about Tower. this talk is about a

[0:18] passion project of mine. understanding all the hype about

[0:24] agentic AI and trying to make it you know understanding what we can do with this.

[0:31] about eight months ago I came

[0:36] across this concept of a small language model and started experimenting and

[0:42] using tower for this and turns out there's a pretty interesting stuff happening in the space. Who of you

[0:48] have heard of small language models? raise your hand. I would say maybe 60ish% who of you have actually tried

[0:55] to use it for agentic work. Smaller percentage but maybe 25%. Okay, nice.

[1:02] there will be some new ideas here for you. some of the stuff you probably already know. for the rest of the

[1:08] audience, you will learn entirely a new concept of small versus large.

[1:14] yes, there's such a thing called small language models. If you traveled 150 years ago in United

[1:22] States, if you're one of the travelers during the gold rush,

[1:27] you would see a sign like this advertising Clipper routes to

[1:33] California promising promising you riches during the gold rush. If you go

[1:39] to the Bay Area today, you will see a different kinds of advertisements advertising another gold rush, the

[1:46] agentic gold rush. Salesforce will try to sell you the Agentforce. some

[1:53] consumer service company will try to sell you AI agents for customer service. even Postman the API company will ask

[2:01] you are your APIs ready for agents. a smart person [Satya] Nadella CEO of

[2:08] Microsoft, has recently said that AI agents will become the primary way of

[2:13] interacting with computers in the future. So, how do we survive this this hype,

[2:20] this temporary craziness and madness? And if you take anything away from this

[2:25] talk, it's it's this it's this phrase of getting your hands

[2:31] dirty. use the tools from the talk, use the ideas that we'll present on

[2:36] your laptop today and lean on small language models as a way of

[2:42] experimenting. by the way if you have questions I think there is a website to submit

[2:50] your questions to please use that if you know the link I think it's talks.pycon.de. we also have micros

[2:56] microphones in the audience. and at the end of the talk I'll try to take

[3:01] several several questions and we'll also talk to you after after the after the

[3:06] talk at the table. tower has a booth where I will be after this talk. So if you want to talk more about

[3:13] SLMs about what I do come downstairs in the sponsor area. a

[3:20] little bit about myself. I I worked for several big tech companies

[3:25] including Google. I worked on a product called Cloud Dataflow in GCP. It's a data processing service high

[3:32] scale streaming and batch analytics. I then went to snowflake where I broke

[3:38] a few things including search optimization and metadata. and then I went to Databricks and broke more

[3:45] things including shipping serverless filtering for spark clusters and dedicated clusters that teams can use to

[3:52] share GPUs. all very exciting stuff. so as you can see I spend most of my

[3:58] career either in databases or in data processing. Now and nowadays I work on tower

[4:04] with several co-founders and and engineers founding engineers. we're building a Python native data

[4:11] backbone for your data pipelines and agents.

[4:16] So now that we've got the motivational example out of the picture, the temporary madness of humanity, the

[4:22] agentic madness, let's I wanted to spend the rest of the time motivating

[4:27] how LLMs became equated with autonomous intelligence. and then I wanted to compare large

[4:34] models with small models and see if we can use the smaller ones better for

[4:40] the task tasks at hand and then I'll give you a few tips for using SLMs

[4:46] how how to experiment with them and how to run agentic flows

[4:53] in in in a in a sense the reason why we are here where we are with this hype about agents is because of the

[5:00] agelong quest by humanity to create something that is more human than

[5:06] humans. To quote Dr. Eldon Tyrell from the Tyrell Corporation who of you have

[5:12] heard talks by Mr. Tyrell. he was right. I see maybe two hands here.

[5:17] it's a reference to Blade Runner. Okay. So it's it's a bit of a it was a test

[5:27] in 1995. So almost more than 30 years ago. The concept of an agent was

[5:34] already explained in a seminal book by Russell and Norvig. they defined

[5:40] an agent. So it it's not a new concept. agents were defined and existed for a

[5:46] while now, three decades. So Russell Norvig defined an agent as an entity that perceives its

[5:52] environment, makes decisions and takes actions. And why does it do it? To

[5:58] achieve goals. So there's a goal. There's a goal and the agent perceives

[6:04] the environment, makes decisions and takes actions. It's very simple really.

[6:12] Agents are not new. They were classic agents in the '9s, 2000s, 2010s. the

[6:18] most important reasoning or decisioning frameworks for agents are the utility

[6:25] theory and the re and reinforcement learning. if you think of elevators

[6:30] in our buildings the Otises and the Schindlers they all used some

[6:36] sort of a reinforcement learning mechanism to decide which floor to go

[6:42] first, how to optimize the routes between different elevators and using

[6:47] a common resource in order to sh to to to bring the passenger the fastest

[6:54] to the destination. So it's not a entirely new concept but recently

[7:01] more recently I would say fiveish years ago language models started becoming

[7:08] decisioning engines so that is new and it and this process started with

[7:14] GPT3 who of you have has you has used GPT3 in their lives all right maybe 60

[7:22] 70% so when GPT3 was trained And the

[7:27] interesting thing that happened was it was trained on data that contained reasoning like patterns. So it was

[7:34] trained on stack overflow on coding tutorials on forum answers and if

[7:41] you've ever visited stack overflow it's a site where you start ask a question

[7:46] and then people start responding to it explaining their their thinking process and giving you answers. So it's

[7:53] a treel like structure. It's a reasoning structure. Then a couple of years later they and

[8:02] other authors have published another very important paper on chain of

[8:07] thought prompting and their their ev innovation

[8:14] and new idea that they brought in was using intermediate reasoning steps and

[8:21] embedding it into training data. So the way they trained models was they had a

[8:26] prompt and the final answer, but they also had intermediate reasoning steps.

[8:32] The user wants me to do X. In order for me to do X, I need to do ABC. And to do

[8:38] A, I need to do one, two, and three. So these are the intermediate reasoning steps. And they were part of the

[8:44] training data. And so now they ran they they use expensive hardware to run

[8:50] these tuples of prompts, intermediate reasoning steps and final answers to

[8:57] create new models. And this is how reasoning got injected into large

[9:02] language models. So they became our decisioning engines because we used reasoning patterns from

[9:09] GPT3 training area and intermediate reasoning steps. So now how does it all work in a

[9:17] simplified form in an agent that uses an LLM to make decisions.

[9:22] A prompt comes in. This is the question from the user. the agent enters a

[9:28] reasoning loop. The reasoning loop divides the prompt into a plan. The plan

[9:34] will contain an execution of multiple tools. The tools can be API calls. They

[9:39] can be analytical database data access patterns or operational database access

[9:45] patterns. And this loop continues

[9:50] until a token is emitted in one of the outputs. The token is final answer. It's

[9:56] literally final answer final underscore answer. This is the token that the agent is looking for. at which point the

[10:03] agent will stop create the final textual output. It will store the prompt the

[10:09] input and the output into a thing called memory so that it can use later on and

[10:16] the loop begins again begins again. Now some smart folks have

[10:23] realized that large language models contain a lot of useless data to operate

[10:32] this reasoning loop. Does it really matter to know who the queen of England was in 1980s

[10:39] in order to make a decision whether to call a data access API?

[10:46] Probably not. The problem with large language models is it contains compressed information

[10:54] from training data. These models are large which means inference is

[10:59] expensive. And because inference is expensive and the models are large, you

[11:05] cannot experiment with them as easily as as you you would like because they

[11:10] don't fit on the hardware that is readily available to you.

[11:16] Couple of months ago some researchers from Nvidia and Georgia Tech published a

[11:22] paper on small language models as the future of agentic AI.

[11:30] What is small? There are a couple of definitions. Small versus large. I and a few others prefer a definition

[11:37] that is time based. So in 2026 small is well the definition is

[11:44] independent of time. A definition is whatever fits into a memory of a

[11:49] regular consumer device. And this year this happens to be maybe 16 or 32 GB of

[11:56] virtual virtual memory. With this amount of memory, a model that will fit

[12:02] into the virtual RAM will probably have somewhere between 10 to 30 billion

[12:07] parameters. and the consequences of using these models typically the

[12:13] strengths of small language models are you get more privacy because you can run them on your private hardware. Um,

[12:20] the cost is much lower. I can literally run many of these models on on this laptop which is already two years

[12:27] late two years old. I already depreciated it. It costs me zero.

[12:34] However, the problem with the SLMs is it doesn't know who the queen of England

[12:39] was in in 1800s. So there's some hallucination. If I do ask it who was

[12:44] the queen of England, it will probably some fake me some name out of its

[12:51] weights. Now the authors of the of the paper h

[12:57] have made three statements that those were the the three main statements of the paper. Statement number one is that

[13:06] today SLMs are now sufficiently powerful to handle the demands of agentic

[13:12] workflows which is a qualified statement. It means

[13:17] they didn't claim that they were as good as OPUS 4.6 for generic tasks. They only

[13:23] said for agentic workflows these SLMs are good enough.

[13:28] And because they're small, they are more flexible in where I deploy them and

[13:35] they're more economical. I can deploy them on local hardware. I can deploy them on really cheap Nvidia GPUs in the

[13:41] cloud. cost becomes less of an issue. So what is important for agentic

[13:48] workflows? there are four four real factors that are that are important four

[13:55] important capabilities of language models as they relate to use in agents.

[14:01] Number one is the ability to break down a task into subtasks. This is what

[14:06] reasoning is. The first task is always the prompt. you break it down into subtasks and then you continue and

[14:17] yeah you break it down in subtasks and you keep going the subtasks into smaller tasks. The second important

[14:24] quality is tool calling the ability to initiate pass parameters and format your

[14:30] output. quality number three is for the use cases where you don't have

[14:37] the tools to solve a problem you need to generate some glue code. So the ability

[14:42] to generate glue code is important. And lastly the ability to follow guard rails

[14:49] instruction following that's also important. Now there's a table comparison table

[14:55] in the paper which I'm not going to read you line by line but the main idea of this table is to say that for agentic

[15:02] the the four tasks that are important for agents the small language models of

[15:10] a size x are now as good as large language models of 10 times that size

[15:20] which is pretty awesome if you ask me Who of you have has heard of the

[15:25] Berkeley function calling leaderboard? Yeah, a few of you. So, this is a

[15:31] leaderboard by UC Berkeley. they keep track of about 110

[15:38] different model families. all the important ones are there. GLM, Claude,

[15:44] Qwen, Meta, everything. vendors kind of supply the the execution and

[15:50] benchmark runs and there's verification going on as well. as of December '25

[15:56] so last year December '25 I I need to check if there's a newer version. They typically do updates every 3 months.

[16:03] as of December the top models

[16:09] for these four important qualities were still the usual suspects.

[16:14] Claude Opus 4.5, Gemini 3, GLM 4.6, but they all proprietary. So you cannot

[16:22] use them for local experimentation. You cannot use them for experimentation in your environment.

[16:28] Now in positions kind of 10 to 20, you're beginning to see open-source

[16:34] models. So you see things like Kimi K2, DeepSeek V3.2, 2 and a model from

[16:41] Salesforce on position 18 xLAM-2. And this is the first model that is not only

[16:47] open- source but also smallish. So it has 32 billion parameters and it

[16:52] provides overall accuracy that is comparable to state-of-the-art. Remember

[16:58] there there are 110 models in this leaderboard and in the top 20 you have a

[17:04] open-source small model. This is actually the model that we're also going to use for our experimentation here

[17:11] in our little demo recording. those of you who want to understand how this model was work was created two

[17:18] things. I'm going to speed up a little bit my talk. they used a synthetic data set with function calls

[17:26] and they they used a process called supervised fine-tuning to create the

[17:31] the final model. So you can actually do it yourself if you generate synthetic data and

[17:39] use this process. So are we now ready to learn how to survive the agentic AI hype? We'll have to science the out

[17:46] of it as as per movie the Martian. for this setup we'll need five things.

[17:53] We'll need a small language model and we recommend the Salesforce xLAM-2

[17:59] because it's open source. It's small you can run it today. we used a

[18:04] particular quantization of this model that actually fits 16 gig gigabytes of RAM. It's the 4bit quantization

[18:12] version. we'll need a inference server or service. For local inference,

[18:18] we recommend llama.cpp. there are reasons why we do this. I will explain it later. for remote inference, once

[18:24] you're ready to move your workload to maybe a cloud production, there are services like Together AI, Hugging Face.

[18:31] We like Together AI and Hugging Face. you might also want to consider a

[18:36] runtime service to run your Python code. There are a couple of examples. I work on tower but you can also use model or

[18:43] fly.io. And I recommend using a framework for agentic agentic framework. LangChain

[18:50] is a good one. I personally prefer that one. there's also LlamaIndex and others. why do we recommend llama

[18:57] cpp? this is more a little bit for folks who use Apple silicon and

[19:03] like simplicity. there are several good inference servers, local inference

[19:09] servers. but Llama actually is able to use local GPUs on Apple whereas

[19:16] vLLM for example does not. and second good reason to use llama.cpp is it uses

[19:22] very simple Hugging Face model naming conventions which vLLM doesn't follow.

[19:28] So, how does a Pyth how does a Python runtime help you in your work?

[19:34] well, it helps you take any Python that you write on your laptop and then package it up into an application and

[19:41] test it locally, but then ship and run in production remotely maybe in your cloud or in their cloud. that's what

[19:48] Tower does. some of these runtimes have a self-hosted version such tower

[19:54] does does have one. and they usually offer you an orchestrator for control flows. what else can you do with

[20:01] tower? Well, you can do boring but necessary things like feature transformations or ETL. You can run

[20:07] ingestion frameworks such as dlt on on tower. You can move data into analytical

[20:14] storage based on Apache Iceberg. you can do transformations transformation jobs using dbt Core or Polars or other

[20:23] libraries. and you can even run your UI on tower as well including

[20:29] Marimo notebooks or LangChain agents. a little bit about Iceberg. Who of

[20:35] you has heard of Iceberg? Apache Iceberg. Okay. Fairly popular technology

[20:43] here. the reason why Iceberg becomes important with agents is because two

[20:49] years ago some lawyers in New York state made a terrible mistake of using ChatGPT to completely fake

[20:56] a legal brief. They actually submitted this brief to the court and got burned

[21:02] because many of the case numbers mentioned in this brief we are hallucinated and they were hallucinated

[21:08] because GPT didn't have access to real legal cases. So since that time

[21:14] people realized we have to give agents access to real business data and

[21:20] Iceberg has very good properties on scaling and

[21:26] performance and accessibility that allows both inference engines as well as

[21:33] data warehouses access a single data set stored in public storage. So how

[21:40] do we do experimentation with with the setup? you'll first install

[21:45] llama.cpp. You'll start running a model the xLAM-2 model. and you'll write your

[21:51] agent using LangChain and maybe perhaps use tower to debug and run it in production.

[21:57] for my demo I I took took an example of a agent that retrieves

[22:04] stock information. but I made it a little bit more complex and I said look there are external stock APIs

[22:11] for example Yahoo finance where the agent can take this data however I I

[22:16] don't want to consistently or constantly go to this external API I want to be able to cache my data in a database

[22:24] so this agent will make decisions if the data is already in a database it will take it from the database our

[22:29] lakehouse Apache Iceberg lakehouse if the data is not there it will go to the external AP API.

[22:36] the interesting piece about agents is how we define what they do, the business rules. So we don't do our typical

[22:44] airflow DAGs anymore. we write business rules. We write things like you can take stock data from an external

[22:51] source, but you should probably take it from a from a cached source from a database if you can if it exists. And

[22:58] this is the preferred way of doing this. So we can now define our flows not in

[23:03] graphs but perhaps in business rules. some of you might ask well how does

[23:11] agents decide which tools to call? It's very interesting because

[23:17] if you use LangChain it uses information in your code including names

[23:23] of functions including the arguments you have and also including even your

[23:28] dock strings to feed it into the decisioning process and determine which

[23:34] tools which tool is the best one to accomplish a task.

[23:40] All right. So I have a quick recording here. I have about like two minutes to to go through. Of course, I use

[23:46] Claude to develop my pipeline. and this pipeline looks like this. I basically ask Claude to develop a tower

[23:53] application that writes a that is a data agent that answers stock prices. and

[24:00] the stock prices should be for a particular set of stock tickers. And

[24:05] there's a time range and I I I'm just looking for the biggest volume of

[24:10] stock trades. So what Claude will do it will first learn based on examples that I provided

[24:17] to it code examples how to write tower applications and once it's knows

[24:23] what the structure of tower applications is it will start generating

[24:29] it will start generating my new application which is a data agent. it uses the tower MCP server. the

[24:37] tower MCP server provides basic commands like create an app, create a

[24:42] configuration file, add parameters, remove parameters. here you're

[24:48] looking at the business rules that I previously defined in my like in the in the prompt that I gave to Claude. These

[24:55] were the business rules I wanted to follow. So Claude inserted it as a as a string into my agent.

[25:04] And what will happen is I want to show you kind of the process to to deploy this agent into cloud production.

[25:12] I will probably take another minute. Sorry guys, I know I'm running a bit over time.

[25:18] tower requires accepts any Python code. You can literally give you give us your

[25:24] existing Python code and we'll run run it. the only ask we have is we

[25:29] need a config file to know what the name of the app is and whether you have any parameters. So this is the what we call

[25:36] a tower file. but everything else from your Python project you can throw over to us as is. just showing you

[25:44] how it looks in Cursor. here's my here's the LangChain agent executor

[25:50] that will be started. and we'll we're getting to the end of the to

[25:55] the reveal as they say in magic and the magicians. Um,

[26:03] all right. So, there's some validation happening. The app is almost done

[26:09] and now it's being deployed to our production environment using the MCP

[26:14] server. and I will share something with you that you will see later in

[26:20] the demo. The first version of the app will kind of work

[26:26] but not really. and this is a this is something that you will see a lot in

[26:31] your development of agents using other agents AI assistants. the first

[26:37] versions will probably fail for some for in this particular reason it will be because a dependency is not installed or

[26:44] it's the wrong dependency but runtime services the Python runtime services like tower are able to

[26:51] feed production logs back into Claude so that Claude can learn and adjust and

[26:57] this is what is happening right now the logs from tower are being routed into Claude the dependency will be

[27:05] modified in pyproject.toml and the second version of the app the agent will

[27:10] actually be successful. So you'll see how it all succeeds. I'm going to speed up a little bit. you'll have to

[27:17] trust me on the successful execution of the second second app. So

[27:24] hopefully I'm at the end of my my talk. Happy to take questions maybe

[27:29] later or even at the table before the next speaker comes. hopefully you

[27:34] were able to see that experimentation is possible. This is the recommended way of learning about

[27:41] agentic workflows. Small can be powerful. use local setups, use open

[27:46] source models. you don't always have to use airflow tags to define your workflows. You can actually start

[27:52] writing your jobs using guardrails and free form text. Would like to

[27:58] connect with me a bit later. I will be at the booth tower booth downstairs as well. You can take a you know QR

[28:04] code pick and connect with me on LinkedIn. thank you for attending this talk. Appreciate it.

[28:13] [applause] we'll take maybe two questions from

[28:19] the chat. so let's say you let's say we have a scenario for a

[28:25] multi-agentic workflow. Does each agent need to have its own SLM? In the case

[28:31] that each agent does not does a specified task, would that be more

[28:36] efficient compared to using a single LM? well, you wouldn't use a

[28:43] custom SLM per task. You would you it's totally fine to use existing SLMs

[28:50] such as the xLAM-2 from Salesforce and just modify your prompt and your business rules. works totally well.

[28:58] you might want to maybe invest later on in fine-tuning a model and

[29:04] actually create your custom copy of a SLM for your task based on synthetic

[29:09] data that you will generate and run through a model generation process but you can start with existing versions

[29:16] of SLMs. Okay. for selecting a SLM, what would

[29:24] you say a user should prefer? High parameter with low quantization or

[29:31] higher quantization with lower number of parameters and why? right. So this is kind of a trade-off

[29:36] you'll have to make. remember I recommended a 32 billion parameter xLAM-2

[29:41] model with 4bit quantization. I I I think you the the 8 billion

[29:48] parameters didn't really work for us. they are still stupid and dumb. but kind of starting with 30 billion

[29:54] parameters, things get interesting. for agentic workflows, they begin really good. They start

[30:00] getting really good at reasoning loops. they they don't they terminate correctly. They don't run infinite

[30:07] loops. one of the interesting things you'll encounter these agentic loops can never terminate. they will

[30:14] continue running because the SLMs are incentivized to call as many tools as they can. this is a interesting fact

[30:21] that you will learn. I would say starting with 30 billion parameters 4bit quantization is great. Yep. It will

[30:29] fit your consumer device. if you can use a 70 billion parameter model, you'll get slightly more accuracy.

[30:36] do we have any anyone in the audience that would like to ask a question? We can pass a mic.

[30:46] Thank you. quick question to the to the leaderboard you showed, right? So 70% was like the the highest number

[30:54] 70ish. Y that does not mean that

[30:59] 70% of answer or questions are correctly answered. It does. Yeah, it does. Sorry, I'm leading. I'm

[31:04] No, no, you you you guessed my question, right? Because if seven out of 10 requests were like garbage, agent

[31:10] workflows would be like garbage, too. combined score of four other scores. you can actually if you go to this

[31:16] leaderboard you'll see individual scores. the numbers here the 77.47

[31:23] doesn't mean that 23% of your questions will be garbage. Answer it in

[31:28] wrongly. it's a combined score of four other scores. Think of it as a index. It's

[31:36] just a index and accuracy is the wrong name for it. It should be called overall index.

[31:42] Yep. All right. I'm happy to take maybe questions at this table to give the next

[31:47] speaker a chance to set up. I will also be available downstairs close to

[31:53] the mark plan plenary for more questions. Thank you. [applause]
## Talk page (2026.pycon.de/talks/YZM8TA/)

**Demystifying Agentic AI Using Small Language Models** — Serhii Sokolenko
Track: Autonomous Systems & AI Agents · Skill level: Intermediate · Domain expertise: Novice · Wednesday 10:55

### Description

**The Agentic Buzz - What's Real, What's Marketing**
- The explosion of "agentic" frameworks and the confusion it causes
- What an agent really is at its core: planning, acting, and reasoning

**Anatomy of an Agent**
- The three basic functions: task decomposition, tool use, and code synthesis
- How frameworks like LangChain and Python make it easy to chain these together

**Why Small Models Are Catching Up**
- Review of research from NVIDIA and Georgia Tech
- Benchmarks showing SLMs matching or exceeding performance of larger LLMs
- Cost, latency, and deployability tradeoffs

**Hands-On Demo: Building and Running an Agent on a Laptop**
- Using LangChain and Python to orchestrate reasoning, tool calls, and code execution
- Example workflow: "Plan a dataset cleanup pipeline" using an SLM
- Observing resource use, latency, and performance in real time

**Key Takeaways and Open Research Directions**
- Opportunities for local and edge deployments
- The emerging role of SLMs in allowing everyone to experiment with agents
- Future questions: scaling reasoning vs. scaling models

### Speaker bio

Serhii Sokolenko is a co-founder of Tower, a Pythonic platform for data flows and agents running on top of open analytical storage. Prior to founding Tower, he worked at Databricks, Snowflake, and Google on data processing and databases.
