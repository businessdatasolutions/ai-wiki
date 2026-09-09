---
title: "How Agentic AI Is Reshaping Finance Workflows, Processes, and Governance | CFA Institute"
video_id: E8BbWoP9-Xk
url: "https://www.youtube.com/watch?v=E8BbWoP9-Xk"
channel: "CFA Institute"
channel_id: UC8Zy7crsNBL8NJCc_ueF-CA
channel_url: "https://www.youtube.com/channel/UC8Zy7crsNBL8NJCc_ueF-CA"
publish_date: '2026-09-01T04:00:32-07:00'
upload_date: '2026-09-01T04:00:32-07:00'
category: "Nonprofits & Activism"
duration: '26:35'
length_seconds: 1595
view_count: 31354
is_live: false
thumbnail: "https://i.ytimg.com/vi/E8BbWoP9-Xk/maxresdefault.jpg"
keywords:
  - "#CFAInstitute"
  - "CFA Institute"
  - "InvestmentFinance"
  - "CharteredFinancialAnalyst"
  - "#CFAProgram"
  - "James Tate"
  - "Agentic AI"
  - "AI in investment management"
  - "AI in finance"
  - "Investment management"
  - "Asset management"
  - "Generative AI"
  - "Financial services"
  - "Artificial intelligence"
  - "AI governance"
  - "Investment research"
  - "Financial technology"
  - "Machine learning"
  - "Large language models"
  - "Small language models"
  - "Synthetic data"
  - "Portfolio management"
  - "CFA Institute Research and Policy Center"
caption_tracks:
  - language_code: en
    name: "English (auto-generated)"
    kind: asr
    is_translatable: true
  - language_code: en-US
    name: "English (United States)"
    kind: manual
    is_translatable: true
description: |
  How is agentic AI changing investment management?
  In this CFA Institute roundtable, Rhodri Preece, CFA, Senior Head of Research at CFA Institute, is joined by Brian Pisaneschi, CFA, and James Tate to explore how agentic AI is transforming investment workflows, financial data analysis, governance, and decision-making.

  Learn about practical applications of AI for investment professionals, including:

  • Building agentic AI tools for investment workflows 
  • Working with incomplete and fragmented financial datasets 
  • Using synthetic data for scenario modelling and portfolio stress testing 
  • Training small language models using open-source data 
  • Improving AI governance, transparency, and trust 
  • Addressing bias in large language models 
  • The future role of AI agents in investment management 

  Whether you're a finance professional, researcher, technology leader, or simply interested in the future of AI in finance, this discussion gives you practical insights into how agentic AI is reshaping the investment industry.

  Learn more from the CFA Institute Research and Policy Center:
  https://rpc.cfainstitute.org/



  CFA Institute:
  The global organization delivering excellence, ethics and education in the investment industry.

  Subscribe for insights and thought leadership that is shaping the future of finance.

  CFA® is a registered trademark of CFA Institute.
notes: |
  Acquired 2026-09-09 via the youtube-transcript skill (Playwright route). Transcript scraped from the
  auto-generated (ASR) caption track; 831 segments, timestamps preserved verbatim.
  No chapters published by the channel.
  SCRAPE DEFECT REPAIRED AT ACQUIRE TIME: the Playwright scrape returned 955 segments, of which the
  last 124 carried timestamps past this video's 26:35 runtime (up to 36:22) and belonged to a
  DIFFERENT video whose transcript panel had also mounted on the page. This is a new variant of the
  two-panel bug noted in the skill's failure modes: not an exact duplication (which `_dedupe_segments`
  catches) but a second, distinct video's segments appended. The foreign tail was dropped; this file
  holds only the 831 segments belonging to the video named above, which signs off at 26:19.
---

## Transcript

[0:00] We can really create incredibly robust workflows

[0:04] just by our own knowledge and iteration.

[0:07] It's still being

[0:08] actively explored in the research as to

[0:10] what are the implications of this?

[0:18] Hello, and welcome to

[0:19] this edition of Roundtable.

[0:21] I'm Rhodri

[0:22] senior head of research at CFA Institute.

[0:25] And today's

[0:26] topic of conversation

[0:27] will be on AI in finance, specifically

[0:30] how AI is reshaping workflows,

[0:33] investment processes

[0:34] and the implications of AI

[0:36] for governance

[0:37] in investment organizations.

[0:39] Joining me for this

[0:40] conversation are my colleagues, Brian Pisaneschi.

[0:43] Brian is the director for Applied

[0:46] Investment Practice and Tools

[0:48] and is our resident

[0:49] AI expert within the CFA Institute

[0:51] Research and Policy Center.

[0:53] And my colleague James Tait,

[0:54] who is a data science researcher

[0:56] and an affiliate researcher

[0:58] with CFA Institute.

[0:59] So welcome, James, and welcome, Brian.

[1:01] Thanks for Rhodri.

[1:02] So let's

[1:02] dive into the topic

[1:03] of today's conversation.

[1:05] As I mentioned,

[1:06] a lot is changing in finance right now.

[1:08] It's often hard to keep pace

[1:10] given the rapid adoption of AI,

[1:12] but as we know that tools are being

[1:15] rolled out

[1:16] continuously, workflows are having

[1:18] to change and evolve

[1:19] and to keep pace

[1:20] with technological developments.

[1:22] Sometimes it's it's

[1:23] hard to know for practitioners

[1:24] where to start,

[1:25] what they should be focusing on.

[1:27] I wonder if you could just

[1:28] start off, Brian, and talk about

[1:29] some of the

[1:30] the latest tools

[1:31] and opportunities to use AI,

[1:34] either to automate investment

[1:36] processes or to enhance

[1:37] part of the workflow

[1:39] by using some of these tools.

[1:41] Yeah.

[1:41] I mean,

[1:42] as far as the latest tools,

[1:44] the thing

[1:44] I'm talking about most every

[1:46] day now is, is skills.

[1:49] So, we've heard plenty about agentic AI.

[1:53] And you know, I was a year ago

[1:57] building these

[1:59] agentic AI solutions within Python.

[2:01] And I was

[2:02] you know,

[2:03] I had to learn these different

[2:06] Python libraries to be able

[2:07] to put together these,

[2:08] these agentic workflows.

[2:11] But Anthropic last year

[2:16] came up with this new industry

[2:18] kind of standard called skills and all

[2:20] they are just master prompts.

[2:22] But these master prompts have

[2:26] a very sound structure

[2:29] to allow them to do tasks autonomously.

[2:33] So they're like I say,

[2:35] they're just these markdown files,

[2:37] which markdown is semi-structured text

[2:40] that outline a very specific workflow.

[2:43] And inside that workflow

[2:45] it might have potentially

[2:47] some other resources to use.

[2:50] It could be like

[2:51] if you're going to create

[2:51] a valuation model,

[2:52] it could have some Excel file

[2:55] in in the skill file

[2:57] that it can pre-populated.

[2:58] But of course

[2:59] it can also kind of create its own

[3:02] CSV file as well.

[3:03] But it could also have connectors

[3:06] to outside data

[3:07] to pull in, data to manipulate that data.

[3:10] And those are MCP servers.

[3:12] So that's

[3:12] another tool that has become industry standard.

[3:17] Now these tools

[3:18] just allow you very quickly

[3:20] to be able to leverage

[3:21] agentic AI within your workflow.

[3:23] So if you have some sort of repetitive

[3:25] task, you can come up with a skill file

[3:30] and you don't need to know

[3:31] how to program.

[3:32] Now, you don't need to

[3:35] be a highly technical person

[3:38] to be able to create these agentic workflows.

[3:40] However,

[3:41] if you do have those abilities,

[3:43] you can make them far more robust.

[3:45] You can create your own custom

[3:47] MCP servers,

[3:48] and the MCP server

[3:49] is just something

[3:50] that allows the large language model

[3:53] to be able to almost natively interact

[3:56] with outside data APIs and the like.

[4:00] So.

[4:01] So just to pick up on a couple of things

[4:03] you said.

[4:03] So it sounds really interesting.

[4:05] If you think about the traditional way

[4:07] a practitioner would use tools,

[4:08] they don't burn their Excel file,

[4:10] they go into their market data

[4:11] terminal like a Bloomberg.

[4:13] And they would

[4:14] they would use a variety

[4:16] of different platforms

[4:17] to extract the information

[4:19] and then perform the analysis.

[4:21] Whereas in the example

[4:22] you just gave, it sounds like the

[4:24] the AI tool

[4:25] kind of sits

[4:25] above all of these,

[4:27] these tools

[4:27] that are then connected

[4:28] or that it can interface with.

[4:29] And so your main point of the main,

[4:33] the main way in which you conduct

[4:34] the task

[4:35] is to first interface

[4:37] with the AI platform itself.

[4:38] Is that a fair characterization

[4:40] that yeah, that's it.

[4:42] So once you've connected

[4:43] all of those sources that you want.

[4:45] And again,

[4:46] like I said,

[4:46] if you have some sort of Excel

[4:48] like model

[4:49] that you're already working with,

[4:51] you can just provide that

[4:52] inside the skill file.

[4:54] And then the

[4:56] AI can actually autonomously decide

[4:58] whether or not, you know,

[4:59] whatever question you give it is,

[5:01] are we working on that specific task

[5:03] that you've already kind of defined?

[5:04] It'll pull that in

[5:05] and then it'll start

[5:06] that conversation, start that workflow.

[5:09] The interesting,

[5:10] the most interesting thing about it

[5:12] is that it's something

[5:13] that's not revolutionary.

[5:14] The beauty is in the simplicity.

[5:16] But of course, an

[5:17] AI has

[5:18] a baseline

[5:19] of what it will do

[5:19] with a given kind of skill.

[5:22] And what we've already been doing is,

[5:26] you know, it screws up.

[5:27] Then you can say, oh,

[5:29] you screwed up there,

[5:30] don't do that again.

[5:31] And as an individual

[5:34] working on a specific project,

[5:36] you know, I can build up, I can change it

[5:39] if it screws up

[5:40] and I can build that into the skill file.

[5:42] And but over and over,

[5:44] especially if you have the same task done

[5:46] with several analysts in a in a firm

[5:49] or even across the industry,

[5:50] you can have everybody kind of making

[5:54] that skill better and better and better,

[5:57] that even if the models

[5:59] don't get any better at all, underlying

[6:02] models that just us

[6:03] creating these skill files

[6:05] for these particular tasks,

[6:07] we can really create

[6:09] incredibly robust workflows

[6:12] just by our own knowledge

[6:14] and iteration on these models.

[6:16] Yeah. Fantastic insights.

[6:18] And it's clear how

[6:20] the conduct of task is going to evolve

[6:23] even more.

[6:24] And we're already seeing that

[6:25] in the examples that you gave.

[6:26] Yeah,

[6:27] I want to bring James

[6:27] into the conversation

[6:28] and talk a little bit more

[6:29] about kind of the data side of it,

[6:31] because obviously

[6:31] your model is only as good

[6:33] as the sources of data it has access to.

[6:36] And we often talk about this

[6:38] being the new age of data

[6:40] and there being an abundance of data,

[6:42] but it's often

[6:44] the case that this a lack of

[6:45] still a lack of good quality

[6:47] or reliable data.

[6:48] There's still gaps in data sets.

[6:50] And so

[6:51] can you talk about some of the ways

[6:52] in which we can address

[6:54] those shortfalls,

[6:55] either through

[6:56] the latest advancements

[6:57] in machine learning concepts

[6:59] or more traditional methods?

[7:01] But how can we address those issues

[7:03] where, on the face of it,

[7:05] you may have an abundance of data,

[7:06] but we know that this a limited history

[7:08] or this some gaps.

[7:09] Talk about

[7:11] talk about this problems in finance.

[7:13] Yeah. Thanks Rhodri.

[7:15] I would say that you have really that

[7:19] there's two

[7:20] there's two

[7:20] main approaches

[7:21] that that you can take

[7:22] to addressing data gaps

[7:24] and it really depends

[7:25] on the kind of data

[7:26] that that is missing essentially.

[7:29] So to take a very simple example,

[7:31] if you had downloaded

[7:34] some historical returns

[7:36] for for different asset classes,

[7:38] but you found that

[7:39] some of the data was was missing,

[7:41] one of those

[7:42] you could quite easily

[7:43] take is something

[7:44] called a linear interpolation.

[7:46] So essentially

[7:47] it's like joining a line

[7:49] between each of the

[7:50] the missing, data points and the points

[7:54] that are actually present to take it up.

[7:57] Her step in complexity.

[7:59] If you had a data set

[8:01] where you didn't just have returns,

[8:03] but you also had

[8:05] other macroeconomic variables

[8:06] or information about companies,

[8:09] and you had points missing in that,

[8:12] in that, in that data set,

[8:14] then you could do something called

[8:16] k nearest neighbors imputation,

[8:18] which is quite a simple

[8:19] box down the data science

[8:21] approach that you can take to

[8:23] to address a missing data.

[8:25] But the third step that you can take,

[8:28] and this is

[8:30] where I think it's very interesting,

[8:31] and it's what

[8:32] some of my research has been on

[8:33] is on synthetic data.

[8:36] And so this is when you would have a,

[8:39] an AI

[8:41] trained model essentially,

[8:42] or a generative

[8:43] AI model

[8:44] that has been trained

[8:45] to generate synthetic data,

[8:47] which is, data

[8:49] that has been generated

[8:50] by some kind of, of statistical model.

[8:54] And where

[8:55] I think

[8:55] there's a lot of value in that,

[8:58] in the finance industry

[9:01] is for things like, scenario, simulation

[9:06] or stress testing

[9:07] portfolios or backtesting

[9:09] trading strategies.

[9:10] Because what you can, you can do is,

[9:14] you can train something called like

[9:17] a generative

[9:19] model using historical,

[9:23] time series data,

[9:26] which you can also combine

[9:27] with other data

[9:28] like macroeconomic variables,

[9:30] for example.

[9:31] And that model can essentially learn

[9:35] the underlying

[9:37] relationships between the returns and the

[9:39] the macroeconomic variables.

[9:42] So so just to pick up on that point,

[9:43] because I think it's an important one.

[9:45] So are you saying that with this

[9:48] AI driven approach,

[9:49] you don't have to prescribe

[9:51] a functional form on the data

[9:52] or assume a given distribution. - Exactly. Yes, exactly.

[9:55] The more of an empirical approach?

[9:57] Yes, yes.

[9:58] So so what's nice about the these

[10:00] these generative models is that,

[10:04] theoretically they can they can model

[10:07] any underlying relationship

[10:09] between the different variables.

[10:10] So they don't need to,

[10:13] you don't need to impose

[10:14] like linearity assumptions.

[10:16] The models learn from the data themselves.

[10:19] So they're data driven.

[10:20] And where that's really nice is

[10:23] you could train a generative model

[10:25] on historical returns and macroeconomic

[10:28] data like,

[10:29] you know, inflation and yields, you know,

[10:32] changes in GDP and employment data

[10:36] and so on. That's released.

[10:38] And then once that model is trained,

[10:41] trained, you can do some simulations.

[10:44] And you can basically see,

[10:46] okay, if inflation changes to this value

[10:49] yields fall by x amount GDP changes by this.

[10:54] What is a possible

[10:56] path of future returns

[10:58] that my portfolio could take?

[11:00] And those models can do that

[11:03] which, which is, which is very

[11:05] which is very promising. And it's better.

[11:08] It's not better,

[11:08] but it's another way

[11:10] that you can simulate

[11:12] your, you know, outcomes for your portfolio,

[11:16] beyond just,

[11:18] what has historically been done,

[11:20] which is either using

[11:21] your empirical return

[11:23] distribution and,

[11:26] just bootstrapping

[11:27] from the empirical returns.

[11:35] Because we know regimes change over time.

[11:37] Why would these generative models

[11:38] there is to address for those.

[11:41] So a lot more flexibility in your

[11:45] modeling capabilities

[11:46] and in the assumptions

[11:47] that need to go into

[11:50] into a particular model

[11:51] when you're looking at data.

[11:53] So better data,

[11:54] better tools, we've learned

[11:57] one point that you both touched on is,

[11:59] is sort of open source

[12:01] versus proprietary models and

[12:05] keen to understand

[12:06] what does the landscape look like.

[12:08] So, Brian,

[12:08] you gave some examples

[12:09] early on about some magenta

[12:13] capabilities.

[12:13] Do you need a highly paid subscription

[12:16] to be able to execute

[12:17] some of these workflows?

[12:19] Can it be done with open source models?

[12:21] And and if so, how is the landscape today

[12:24] different from maybe

[12:25] where finance traditionally is being,

[12:27] which has all

[12:28] been about private information and

[12:31] relatively high costs

[12:33] that are paid to vendors to

[12:34] to source these tools?

[12:36] I mean,

[12:37] you have obviously that issue,

[12:39] the private information.

[12:40] So plenty of people in our industry

[12:42] are just focused

[12:43] only on using open source

[12:45] because they can't send

[12:47] any of their information

[12:48] and data outside.

[12:51] So there are

[12:53] of course, all these really great open

[12:55] source large language models,

[12:56] but they lag behind,

[12:57] probably around I would say like

[13:01] three months.

[13:02] I mean

[13:02] depending now

[13:03] it's it's I would say Anthropic, OpenAI

[13:07] their latest is is really really good.

[13:11] But it's almost turned

[13:14] to a lot of the value being the

[13:17] they call it harness,

[13:19] but it's essentially how

[13:23] the architecture

[13:24] underlying the agentic framework is.

[13:28] So Claude Code, for example, is a

[13:31] agenetic architecture

[13:32] underlying that

[13:34] that they've built into the platform.

[13:36] And,

[13:38] well, ironically,

[13:39] they actually leaked

[13:40] their entire code base

[13:41] and the open source community

[13:43] has taken that and run with it

[13:45] and created

[13:46] really great open source alternatives.

[13:48] But they still have this kind of

[13:51] you have that competitive advantage

[13:53] because they've created

[13:55] some incredible parallelization.

[13:56] They've optimized their harness

[14:00] for these agentic tasks.

[14:02] And so if you just took, for example,

[14:06] an open source model,

[14:07] a Deepseek or something like that,

[14:09] and then you threw it into the harness,

[14:11] the open source harness,

[14:12] it is not going to quite

[14:15] it's not going to be as good

[14:16] as Claude Code.

[14:19] And it's very clear that

[14:22] in this space it's a winner

[14:25] kind of take all scenario.

[14:26] Like if you don't have the best model,

[14:30] then you're, you're missing something.

[14:33] And, and there is just this huge

[14:36] like competitive advantage

[14:38] of having that best model.

[14:40] So if you are kind of

[14:43] just stuck in that space that you

[14:45] you can't put your any of your data

[14:46] into Anthropic,

[14:48] OpenAI again,

[14:49] there are still plenty of really

[14:51] great open source models out there.

[14:53] The other thing I wanted to say,

[14:54] though,

[14:54] is that

[14:55] what a lot of the value

[14:57] of open source is, is optimization.

[15:00] So, you know,

[15:01] James and I

[15:02] have been working on a project.

[15:03] It's,

[15:04] you know,

[15:04] we're dealing with a lot of data now.

[15:07] And when you're dealing

[15:08] with a lot of data, if you just send,

[15:12] you know, API calls to OpenAI

[15:15] every single time,

[15:16] that's going to be a lot of money.

[15:19] So what you do is

[15:22] you can train a small language model

[15:26] off of a data set.

[15:27] And it, you know, it's becoming so easy

[15:31] to do that now, just very quickly

[15:33] is just kind of train a model.

[15:35] Of course, you've got to build

[15:36] that, that, that data

[15:37] set and garbage in, garbage out

[15:39] to be able to train.

[15:40] But if you can get a good enough model,

[15:42] you put this small language model in,

[15:44] you can run it

[15:45] locally and you've saved tons of money.

[15:49] That would have been tons of API calls.

[15:52] Now you're just running a small language

[15:55] model locally and it's practically free.

[15:57] So it becomes a cost

[15:58] optimization problem with open source

[16:02] rather than

[16:04] the actual capabilities itself.

[16:06] What's really important

[16:07] there is that you.

[16:08] So as part of the work

[16:10] that Brian's just mentioned,

[16:12] you have a means of comparing,

[16:15] like all the different approaches

[16:16] that you're taking.

[16:16] So you have your proprietary models

[16:18] that maybe can serve

[16:19] as the baseline that you want to get to,

[16:22] that you can just test out

[16:23] with a couple of your,

[16:26] you know, your processes,

[16:27] and then you can take a lot of

[16:29] freely available

[16:30] like open source

[16:31] alternative models

[16:33] and then run them

[16:33] through the same process.

[16:35] And then you can compare

[16:36] all of the results.

[16:37] And what what I found was that with,

[16:42] a much smaller large language model

[16:44] that was open source,

[16:45] I was able to to replicate

[16:48] more or less what

[16:50] the proprietary OpenAI model

[16:52] was able to do for the task

[16:53] that I had specified.

[16:55] But where I was

[16:56] struggling was the scalability,

[16:59] because running even a small,

[17:03] large language model now, which

[17:05] I think at the time it was 36

[17:08] billion parameters,

[17:10] which is quite small in today's terms.

[17:11] But you go back three years

[17:13] and it was much, much larger.

[17:15] It still took a very, very long time

[17:19] for me to be able to,

[17:22] to get the results that I needed.

[17:23] Whereas with, to Brian's point,

[17:25] like using one of these

[17:27] proprietary models,

[17:28] you have that ability to scale

[17:29] very, very quickly

[17:30] and you can have

[17:31] batch requests where you send 50,000,

[17:35] you know, requests to and through an API

[17:38] and you get results back within 24 hours.

[17:40] It's very,

[17:41] very difficult to replicate that,

[17:44] locally

[17:45] unless you invest a lot

[17:46] in the infrastructure.

[17:48] And I think for most,

[17:51] firms, you know,

[17:53] that's maybe not something that they

[17:55] need to do because there are

[17:58] yeah, easier alternatives

[18:00] So, so it sounds like you,

[18:02] you need to think carefully about

[18:04] what is the use case,

[18:05] what is what is the needs,

[18:07] the constraints that you're

[18:08] operating under to select the right

[18:10] the right model.

[18:11] And it can come from both proprietary

[18:13] as well as open source.

[18:15] It does raise some questions

[18:16] though around governance.

[18:18] So I think AI

[18:18] governance is generally a huge area

[18:21] and probably beyond the scope

[18:24] of this conversation.

[18:25] But just to touch on that area

[18:26] a little bit,

[18:27] you know,

[18:28] I know organizations are struggling

[18:30] with this issue is

[18:30] how do I put the right

[18:32] frameworks in place

[18:33] to ensure that I can use tools and data

[18:36] sets responsibly,

[18:38] that I can protect

[18:39] confidentiality of client data,

[18:42] and that I uphold

[18:43] my fiduciary responsibility

[18:45] to the extent

[18:46] that I have a fiduciary obligation

[18:48] to clients.

[18:49] And obviously,

[18:50] CFA Institute as a professional

[18:52] body, is very focused on this issue.

[18:53] We have our own code of ethics

[18:55] and standards of professional conduct.

[18:57] James, just wondered

[18:58] if you want to share some thoughts on

[19:00] what do you see

[19:01] as some of the main, let's say,

[19:03] ethical considerations

[19:05] when you're working with large language

[19:07] models, AI tools and large data sets?

[19:12] I'd say the,

[19:13] the biggest, the biggest concern

[19:18] that I have is around biases

[19:20] in large language models.

[19:21] So going back to

[19:24] and this is an active topic of research

[19:26] that we're working on, of course. Yes.

[19:28] And, and and many others.

[19:30] It's a very hot topic at the moment.

[19:32] But the idea is that

[19:33] these large language models,

[19:35] because they've been trained

[19:36] on, you know,

[19:37] all of the publicly available data,

[19:40] there

[19:41] there's a very heavy

[19:42] skew towards Western data sets of

[19:46] American stocks,

[19:48] tech stocks, for instance.

[19:49] And it's very easy for you to

[19:52] to test this out.

[19:53] You know yourself using these models

[19:55] when you're using them in your

[19:57] in your day to day processes,

[19:58] you might find

[19:59] that they happen to recommend

[20:01] like certain paths

[20:02] or a default to certain recommendations,

[20:05] or that comes from the pre-training data.

[20:08] Now where you can

[20:10] somewhat address that is by,

[20:13] using MCP servers,

[20:14] giving them access to other data sets,

[20:18] giving them specific skills.

[20:20] So you know exactly,

[20:22] you know what,

[20:23] what they need to look for.

[20:24] So maybe you have certain

[20:27] profitability ratios that you use

[20:29] for when you're screening stocks.

[20:30] If you don't give those

[20:32] specific requirements to an LLM,

[20:34] when you're doing a stock screening,

[20:35] it might

[20:36] implicitly choose

[20:37] one of those ratios

[20:39] to do its screening, for instance.

[20:40] So that's where you need to have those,

[20:43] those instructions in, in place.

[20:45] But the big concern around it for me

[20:47] is that

[20:49] I don't think enough

[20:50] people are really aware

[20:52] of these biases in these models.

[20:54] And it's very interesting because

[20:58] a lot of research has shown

[21:00] that the biases in these large language

[21:01] models basically mirror investor biases.

[21:05] You know,

[21:05] they're trained on human generated data.

[21:07] So naturally they mirror human biases.

[21:10] So LLM’s have been shown

[21:12] to have loss aversion bias.

[21:13] So what are the implications of that.

[21:15] Well if you gave them

[21:17] access to a portfolio

[21:19] and you had gains and losses,

[21:21] they're more likely to hold on to

[21:24] the losses

[21:25] when potentially they should,

[21:27] you know, delegate those funds

[21:28] to a better investment.

[21:30] Now, that's

[21:30] something that it's still being

[21:33] actively explored in the researchers to

[21:35] what are the actual implications of this?

[21:37] But it's very clear if you're, you know,

[21:40] a manager and,

[21:41] and you're using these,

[21:42] these models,

[21:43] you need to be aware

[21:44] that they have these, these limitations.

[21:46] And you need to understand

[21:48] how you can try and find these,

[21:51] these limitations.

[21:52] And then you can

[21:53] make explicit decisions

[21:55] about how you want to address them.

[21:58] I think it's

[21:59] a really interesting point

[22:00] because I think, the behavioral finance literature

[22:04] obviously is pretty extensive,

[22:06] and it's

[22:06] well known that humans have biases.

[22:08] But I think there is often

[22:10] a misplaced assumption

[22:11] that if I can

[22:13] delegate some tasks to a machine

[22:16] tool of some of some description,

[22:19] that that would be a way to

[22:20] negate some of the human biases

[22:22] that filter

[22:23] through to investment decisions.

[22:24] Whereas actually, what you're saying

[22:25] is with the advent

[22:27] of large language models

[22:28] actually that’s not the case.

[22:30] And we need to be conscious

[22:31] that there are biases

[22:32] both in machine driven outputs

[22:35] as well as in human decision making.

[22:37] So knowing how to address that is critical.

[22:39] Brian would you like to comment on that?

[22:41] Yeah,

[22:41] I think well, that's

[22:41] one of the most important pieces

[22:43] because it's it's about control.

[22:45] So you know

[22:46] we think about quant in investing

[22:49] and even some of the most like basic,

[22:52] you know, tools like

[22:56] stop loss orders, for example

[22:57] they can so easily

[23:00] mitigate your own human emotional bias.

[23:03] And that's why

[23:05] if you just delegate these

[23:06] things in rules based

[23:10] investment tactics,

[23:12] they can really reduce

[23:14] a lot of your own emotional biases.

[23:16] But of course, as James

[23:17] just said,

[23:17] these large language models

[23:19] are so complex

[23:21] that they have kind of this decision

[23:23] making authority that are

[23:24] that is subject to the biases.

[23:26] But what James mentioned

[23:27] also is,

[23:28] is about being able

[23:29] to fix that, being able to

[23:33] inject something to reduce those biases.

[23:36] And once you do that,

[23:38] and which you can do right now

[23:39] with skills

[23:41] that I mentioned earlier, is

[23:43] if you can say red team a

[23:45] and red-teaming would be it's what

[23:50] the cybersecurity industry

[23:51] does to try and essentially

[23:53] hack their own system.

[23:54] So red-teaming is just, you know,

[23:56] figuring out ways to break the system.

[23:58] If you can red-team

[23:59] your model for these biases.

[24:02] And you can create a skill file.

[24:05] And to mitigate those biases,

[24:08] you're giving it more control.

[24:10] And if that control is predictable,

[24:12] then you can absolutely reduce the

[24:15] the human bias that we have,

[24:19] as well as reduce the bias

[24:21] that the large language model has.

[24:23] So it's just about control.

[24:24] It's about being able

[24:25] to find those biases, find the errors

[24:30] and put those those fixes in.

[24:33] And then again

[24:34] test it through,

[24:35] you know,

[24:36] large distributions of outputs

[24:38] so that you can gain comfort

[24:40] and more trust in the system.

[24:42] Because everything about governance,

[24:43] everything about ethics

[24:45] within the actual kind of technical

[24:47] AI side

[24:48] is really just about gaining trust.

[24:51] When we give a large language model

[24:53] a task and we are, you know,

[24:56] we have knowledge,

[24:57] we are financial domain experts.

[24:59] We see the the output

[25:01] and it's either good or it's bad,

[25:02] just like kind of an employee.

[25:04] And so over time

[25:05] you keep giving at these tasks

[25:07] it might start getting better and better.

[25:09] We gain gain trust.

[25:10] Well how do you do that at scale?

[25:12] Well, at scale for an entire firm.

[25:15] How do you gain trust.

[25:17] You give it lots and lots of tasks.

[25:19] You run evaluations.

[25:21] You create the distributions of outputs

[25:24] that it's supposed to

[25:26] that of the tasks that you're doing.

[25:28] And then you gain trust by,

[25:33] you know,

[25:33] reviewing the

[25:34] outputs and the valuations.

[25:37] So it's an interesting concept.

[25:38] I think

[25:38] the whole concept of trust

[25:40] in an AI model mediated world

[25:43] merits a separate conversation entirely.

[25:46] But Thanks, Brian,

[25:48] for sharing those thoughts.

[25:49] Unfortunately,

[25:50] that's all we have time for

[25:51] in today's edition of roundtable.

[25:53] This has been

[25:55] a wide ranging discussion

[25:56] around models, tools,

[25:58] data governance and ethics in AI.

[26:00] And these are all topics of conversation

[26:03] in which you will find

[26:04] more insights,

[26:05] thought leadership and research

[26:07] on the CFA Institute

[26:08] Research and Policy Center.

[26:10] And we encourage you to

[26:11] go and check out the resources

[26:12] that are available to

[26:13] to you on our website.

[26:16] So that just leads me to say a huge

[26:18] thank you to both James and to Brian.

[26:19] Thank you very much.
