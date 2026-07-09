---
title: "Software in the Age of Agents | The a16z Show"
video_id: Mxs4erDxOEE
url: "https://www.youtube.com/watch?v=Mxs4erDxOEE"
channel: "a16z"
channel_id: UC9cn0TuPq4dnbTY-CBsm8XA
channel_url: "https://www.youtube.com/channel/UC9cn0TuPq4dnbTY-CBsm8XA"
publish_date: '2026-07-07T07:50:32-07:00'
upload_date: '2026-07-07T07:50:32-07:00'
category: Science & Technology
duration: '1:01:09'
length_seconds: 3669
view_count: 6559
caption_tracks:
  - language_code: en
    name: "English (auto-generated)"
    kind: asr
    is_translatable: true
keywords:
  - "a16z"
  - "andreessen horowitz"
description: |
  Seema Amble, Steven Sinofsky, and Elena Burger unpack one of the biggest questions facing enterprise software: what happens when AI agents become the primary users of software instead of humans?

  The conversation explores the rise of "headless" software, why APIs and agentic workflows are reshaping enterprise applications, and whether traditional SaaS products are becoming systems of record rather than systems of engagement. They discuss Salesforce's Headless 360 announcement, MCP, enterprise software architecture, and why AI may fundamentally change how businesses interact with their data.

  Along the way, they examine what actually makes enterprise software sticky, why replacing systems like SAP and Salesforce is harder than it appears, and where startups have the greatest opportunity as AI reshapes the software stack.

  Timestamps:
  00:00 - Intro
  01:00 - What "Headless Software" Actually Means
  06:57 - Agents, APIs & the Definitional Hell We're In
  10:00 - What Makes Enterprise Software Sticky
  15:00 - The Death of Software? Why SAP Isn't Going Anywhere
  22:00 - Vibe Coding Your Way Into Enterprise: Why It Fails
  29:00 - Exception Handling Is the Entire Game
  37:00 - Productivity Creates New Scenarios, Not Fewer Jobs
  54:00 - Where the Biggest Startup Opportunities Are Now

  Resources:
  Follow Seema Amble on X: https://x.com/seema_amble
  Follow Steven Sinofsky on X: https://x.com/stevesi
  Follow Elena Burger on X: https://x.com/VirtualElena

  Related Reading
  Is Software Losing Its Head?
  https://a16z.com/is-software-losing-its-head/

  The Death of Software? Nah.
  https://a16z.com/death-of-software-nah/

  Stay Updated: 
  If you enjoyed this episode, be sure to like, subscribe, and share with your friends! 

  Find a16z on X: https://twitter.com/a16z 

  Find a16z on LinkedIn: https://www.linkedin.com/company/a16z 

  Listen to the a16z Show on Spotify: https://open.spotify.com/show/5bC65RDvs3oxnLyqqvkUYX 

  Listen to the a16z Show on Apple Podcasts: https://podcasts.apple.com/us/podcast/a16z-podcast/id842818711 

  Follow our host: https://x.com/eriktorenberg 

  Please note that the content here is for informational purposes only; should NOT be taken as legal, business, tax, or investment advice or be used to evaluate any investment or security; and is not directed at any investors or potential investors in any a16z fund. a16z and its affiliates may maintain investments in the companies discussed. For more details please see http://a16z.com/disclosures.
notes: |
  Metadata fetch: headless failed twice (30s default timeout AND 60s retry, both
  transcript panel did not render); a --headed retry at 60s ALSO failed; succeeded
  only at --headed --timeout 120000 (61-min video, 1162 segments). Same automation-
  detection class as the 2026-05-13 incident, exacerbated by video length.
  ASR cleanup: Sema/Simo -> Seema (Amble), Sonowski -> Sinofsky. Description credits
  three speakers (Seema Amble, Steven Sinofsky, Elena Burger) but only two distinct
  voices are identifiable in the transcript (Amble hosting, Sinofsky as guest) --
  Elena Burger is never named or clearly present; flagged as an identity discrepancy
  for the wiki source page rather than silently assuming her participation.
---

## Transcript

[0:00] There are many things that made software sticky, but a lot of it had to do with the fact that the way a human interacts.
[0:06] In an agentic world, do you actually need that? The data, the logic, everything stored below it is really
[0:11] where the value is. There's this wild underestimation about like you could vibe code your way into enterprise software. Larry Ellison at
[0:18] Oracle, he went on a rant about how enterprise software was so stupid
[0:23] because everybody customized it. The minute you automate the most mundane thing and think you have it all squared
[0:29] away, whole new things appear. Misconception right now is that you can
[0:34] just have you know Postgress database and APIs and then bam like you can replace SAP. That's like absolutely not
[0:40] true. That piece around the logic and everything else that is encaptured in SAP is way way more important than the
[0:47] fact that like oh this data just happens to be in this database. One of the things that happens in technology shifts
[0:53] is nobody understands exponential when it's happening. The biggest opportunity right now is
[1:00] Welcome to the A16Z podcast. I'm here with Seema Amble, a partner here on the
[1:06] enterprise team, and Steven Sinofsky, who is a board partner at E16Z, as well
[1:14] as a former uh member of of Microsoft,
[1:20] friend of the firm. Um, and here we are today to talk about um a piece that Seema
[1:27] wrote about a month ago called Is Software Losing Its Head? Uh, and this piece I'll I'll let Seema talk about it
[1:34] in her own words. Um, but this piece was written a couple months ago. Salesforce
[1:40] announced that they would be going headless. Um, and today we're here to kind of discuss, you know, what does
[1:46] that mean? What does that mean for, you know, the future of SAS products, the future of, um, you know, just just kind
[1:54] of software more generally? So, Seema, um, can you just walk me through first what headless software means and explain
[2:02] kind of what changes it introduces? Yeah. Um, so headless software has really it's it's not a new term, but I
[2:08] think has really risen in uh in like the you know public domain of of interest in in a topic that people are talking
[2:15] about. One of the interesting news points has been Salesforce making this announcement. they were launching headless 360 which was really in classic
[2:22] Salesforce motion you know uh history a uh a marketing announcement more than anything else but it does capture um it
[2:30] sort of it's an acknowledgement of what's happening which is you know traditional software had been built
[2:37] around humans accessing it and um it was workflow to capture data and we could
[2:43] talk more about what that meant in an agentic world do you do you actually need that the UI doesn't matter matter
[2:49] because the agent isn't accessing the software via the UI. We could unpack whether the UI matters or not. But in
[2:55] the idea of the being headless is the the data, the logic, everything stored
[3:02] below it is really where the value is, not just the workflow software that's being tracked at the top.
[3:08] Gotcha. Um, and uh, this was announced a couple months ago. I'm curious kind of
[3:14] in in the past couple months, what have we seen? I mean you wrote even in the piece kind of you at the beginning you
[3:21] were a little bit you know funny maybe and you said is this really even that big of an announcement? Is this sort of
[3:27] a rebrand of you know APIs that they had kind of already made available? So does
[3:33] this feel like a significant change? Is this maybe more of a branding exercise? Um and kind of like what have we even
[3:39] seen in the past couple months since we've been able to kind of observe what changes have have really happened? So
[3:45] I'll separate it out into the Salesforce context and then like the broader context which I think the broader context is more interesting. In the
[3:51] Salesforce context probably not that interesting. Uh I think Salesforce I think rightfully again it was
[3:57] acknowledging a shift that's happening in the market. I don't from what I could tell nothing actually changed. Their 360
[4:03] product was uh the same APIs that had always been exposed now rebranded as as
[4:08] as their 360 product. How and and APIs have always existed. So you know many uh
[4:14] or I shouldn't say always but for a long time have existed. Um but I think the broader trend here is there you know
[4:21] Salesforce among others are thinking about how they build themselves for the agentic world. Um and so if an agent
[4:29] needs to access the data in a CRM like Salesforce um what are they doing it?
[4:34] Are they doing it via the UI or are they using the API? And that's the you know Salesforce is saying like okay hey we
[4:40] know what is changing that there are agents who are needing to access the data. Let's look at the you know let's
[4:46] offer a headless version for them to interact with um the data versus going
[4:51] via the UI. That said again I don't think anything actually changed in the Salesforce context but Salesforce is in
[4:56] the old one. Another example is notion has a headless product and actually I think that makes uh even more sense
[5:02] because it's much hard like I think many users of Salesforce are probably less technically adept less likely to be
[5:09] building their own agents although there are many many more people who are doing that with Salesforce notion users tend you know all things being equal are more
[5:17] I'd say techsavvy and more agentic as as builders and I think notion is is one of
[5:22] many other companies that is also trying to figure out okay what is it that I offer for um and you know how do I make
[5:30] you know what APIs do I expose? I think Stephen will talk more about MCP. Um and and again I think a lot of this is also
[5:36] getting caught up a little bit in nomenclature and like okay what are we calling things? Um and I I I think that's one thing but
[5:42] I think the the broader trend around how agents um access systems of record I
[5:48] think is the the bigger point. Yeah. Yeah. And from my understanding it's also I mean it could also apply to
[5:54] something as simple as a chatbot. you know, it's not necessarily just an API or an MCP server. You know, you you
[6:00] could be, you know, Salesforce um acquired Slack a couple of years ago and like it could be something as simple as
[6:06] like you you sort of interacting with with a CRM via chatbot.
[6:12] Totally. And I think I read somewhere that there's been like a 300% increase in Slackbot uh Slack agent usage. Yeah.
[6:18] which is essentially saying that you don't need to log into the Salesforce EOS uh interface to get the data or
[6:25] whatever data it is. So yeah, it's it's essentially again all these are agentic ways of accessing it versus the human
[6:30] needing to go in log the data or or um from a read perspective go back and see
[6:36] okay here were the like here's this opportunity here's what happened and um look at them themselves um and so the
[6:42] that interface is is less relevant. Yeah. And Stephen, do you have anything to add here just on the kind of like
[6:49] definitional territory that we're covering right now or or kind of this discussion?
[6:54] Well, sir, I mean like we're in definitional hell right now where is is,
[7:01] you know, part of a new wave of technology is you make up a lot of new words for things that you kind of did
[7:08] before. And that's just a natural part of technology evolution. Um, but I I
[7:14] actually think it's super important. Like first you have this, you have a agent, which as far as I can tell right
[7:19] now is also a new word for program that takes a very long time to run and might
[7:24] not finish. And and so yet that's just like a a branding that's the best
[7:30] branding ever is to call a program that's takes a really long time, which we used to call a bug, is now like the
[7:36] coolest new feature ever and it's just now an agent. But in in seriousness, the
[7:42] most interesting way I think to think up what you're really talking about doing differently between an agent and an API
[7:50] is really what are you actually doing? What is the agent itself doing? Is it
[7:56] looking something up? Because that's actually a pretty lightweight thing that all systems are pretty good at. And in
[8:02] fact, many many of the newlyannounced, you know, headless agent APIs are are
[8:09] just lookup and they're just you basically have a new interface to the old way to look something up, which is a
[8:16] lot more forgiving, a lot less UI goo and stuff like that. Then there's like I
[8:21] want to do something and that's where you get into very interesting issues over like well if you do something you
[8:29] have to be impersonating a specific person you have to have their credentials like it's a very is it
[8:35] another paid seat is it the same paid seat you have all these interesting enterprise software issues that come up
[8:42] if you actually want to cause a change to a system of record and then there's
[8:47] the third thing which is analyze. And so analyze is more than look something up.
[8:54] It's actually look up a bunch of stuff. It often involves multiple systems. And that seems very very tuned to an agent
[9:01] because you you're not time bounded. You can spend energy iterate. You can route
[9:06] it to different models and get different answers back and compare them. But it's also where hallucination really is a
[9:13] huge issue because if you're going to go and analyze something, you actually need a way to verify that everything every
[9:21] step of that analysis was correct. And so I think it's super interesting and important when you look at headless and
[9:28] agent which are conflated in you sort of have to figure out what you're talking about because we're on different places
[9:35] in the evolution the learning curve and the deployment of agents relative to
[9:40] sort of that three-way matrix matrix. Yeah. I I think this is actually a good
[9:46] leadup into a follow-up question, which is kind of like historically, what has made software sticky and how are agents
[9:54] starting to disrupt that? And I I leave that to either of you to answer. Maybe you guys can both kind of debate about
[10:00] that. Yeah, I'd say there there are many things that made software sticky, but a
[10:06] lot of it had to do with the fact that um it was built around like the the way a human interacts, right? So um the UI
[10:15] was sticky because you know the number of times you had to read and write the frequency of access the downstream
[10:22] workflows all of the like undocumented like you know what we call SOPs or uh standard operating procedures all the
[10:28] stuff that happened around the software that got ingrained in muscle memory and process and then external parties etc.
[10:34] So like a CRM may be sticky because a sales rep needs to go in and out of it
[10:39] all the time. They're used to interacting with Salesforce. A lot of times when like new VPs of sales come into our companies, they they're like
[10:45] they mandate that Salesforce is there because they're used to using it. Their teams are used to using it. Um and then
[10:51] there's, you know, finance may rely on the Salesforce um output for billing and
[10:56] upstream marketing is going to rely on it as well. And so there's these dependencies. Um and these all are
[11:02] driving stickiness. But I think the other piece too is there you need one single set of truth, right? you need to
[11:09] know like an account is closed and who is working on it and all of that needs to be logged in one place. Um and I
[11:16] think if you go from CRM to say an ERP or payroll like that absolutely has even like legal reasons and compliance
[11:23] reasons why you can't have um numbers that are not being you know tracked uh
[11:29] as cleanly and and correctly as you know an auditor might like for example. Um so
[11:34] anyways this all drove stickiness there and and and durability because you know you were used to using Salesforce the
[11:40] whole ecosystem was using Salesforce and it was the default option and maybe you
[11:45] know there's one or two others in the market. Um and so I think historically those were some of the things that were were driving stickiness.
[11:53] Yeah. I mean I those are all exactly right. I I think it's important to also consider that the most sticky thing you
[12:01] could do is actually collect money from a customer. And if you're collecting money, it turns out it's really really
[12:07] hard for them to stop sending you money. And it's really hard for them to figure out what to do if they stop sending you
[12:14] money. And and it it sounds really trit, but the the stickiest software is
[12:19] software that's getting used somewhere. Then when you dig in and try to come up with reasons, well, it just depends on
[12:25] who you talk to in a company, you know, you talk to the HIPPA compliance people in some company and they're going to
[12:32] tell you this is the software you have to use because it's like the most bestest HIPPA compliant software. If you
[12:38] talk to the administrators, you're going to hear about onboarding new users. If you talk to the users, you're going to
[12:44] hear about muscle memory and keystrokes or labor unions or whatever. and and so
[12:51] you have to be yet you you really want to get the software sold and that's your
[12:56] fastest path to sticky and after that it it's sort of you know a winner's tail
[13:02] over over what caused it to be sticky and and in fact the best thing about
[13:07] sticky is if you're the rep for a company that you've sold something to and the company is threatening you like
[13:14] hey we're going to replace you we're just going to listen to them and you're going to find what's sticky. And if that
[13:21] works like three or four times across different accounts, then you've just told the tale as to what made the
[13:27] product sticky. It doesn't matter what the PMs or what anybody else thought of. It could be some crazy arcane thing, you
[13:34] know, like I have stories of lots of sticky software and lots of arcane things, but like anyone who's ever tried
[13:41] to displace um Microsoft Outlook as email very quickly learned about
[13:47] delegate access and and having calendars owned by multiple people and all of this
[13:53] crazy stuff. And like I can tell you there was no meeting where we said, "Okay, let's figure out how to make the
[13:59] calendar the sticky part of Outlook and make sure we handle recurring meeting exception handling well." And then you
[14:06] go and you find out, you know, General Motors isn't going to displace like 600,000 seats because of the calendar or
[14:13] some crazy thing like that. And so you can, it's really amazing in enterprise software what causes sticky and how you
[14:20] can actually capitalize it on it when somebody threatens to take you out of the out of the enterprise.
[14:26] I I think there's a really good point there in two things. Inertia is a really powerful force. And then I think the other thing is
[14:32] yeah, nobody when they're building the software, they're not like thinking about like this rubric we put together and like tick tick tick. We got all
[14:38] these features that are going to do all these things. But I think the practical reality is also as software extends its
[14:44] tentacles across an organization and it gets ingrained in people using it and they've been paying for it for a long
[14:50] time, it just seeps into how people are doing things and that's like hard to rip out.
[14:55] Yeah. Yeah. You even talk about this in your PC mode where there's sort of all of these like invisible tacet sort of
[15:03] understandings about how to use different products or things that are embedded both within the software but
[15:08] also within the people using them where it's just like it does become hard after a while to uh to extricate yourself from
[15:16] from whatever ecosystem you happen to be in. And in fact, Stephen, I think you you've even you know said the SAS
[15:24] apocalypse is overblown. you've written an essay called the death of software. Nah. Um where you where you you know
[15:32] emphatically sort of rejected this idea. So maybe if you want to if you want to maybe just recount that piece a little
[15:38] bit for us. Well, I mean Seema co-wrote a post on on SAP which is sort of the ultimate ultimate example of sticky software. I
[15:46] mean there is nothing the the only software that's stickier than SAP is behind the scenes and it's the software
[15:53] that insurance companies wrote and they wrote all this software like 50 years
[15:59] ago or 75 years ago and if you ever there's no replacing it like it it just
[16:04] it in fact you whenever jokes come up about like businesses that are looking for cobalt programmers it's to go and
[16:11] work on the insurance software that exists in in every state of the union
[16:17] and and in many ways what you're seeing like with the one of the biggest successes to date in Stripe has been
[16:24] somebody actually went in and for the first time in it two generations coded
[16:30] up the software to collect money from people which itself had previously been an unsolved problem on the scale of
[16:38] insurance because nobody put together the tax laws for every country every
[16:44] every jurisdiction every locality, every border crossing, every currency exchange like it it it's
[16:53] mindblowing that. And so now that is the most sticky. So like that is not going anywhere ever. Like it it'll be like
[17:01] we'll be doing this podcast with like great grandchildren 100 years from now talking about how sticky that experience
[17:08] was. Just like I told like oh you didn't know this but the software that runs all state is older than me and it's not
[17:15] going anywhere and that's because the these examples are ones that codified an
[17:22] external force and that external force was the regulatory body that they
[17:27] embraced the seamless examples of SAP like it just codified a company and and
[17:34] so like if you take SAP out of a large automobile manufacturer
[17:39] there's no automobile manufacturer left or or Walmart like the company just evaporates
[17:46] because the the company is defined not just by purchasing the software not even
[17:51] by just using it but by how that they codified the business rules into that
[17:57] product. I think it's a good point to double click on because I think a misconception
[18:03] right now is that SAP okay well you can just have you know Postgress database and APIs and then bam like you can
[18:10] replace API replace SAP and that's like absolutely not true. I think partly I
[18:15] mean Stephen I don't know if you want to elaborate on or not I'm happy to but I think it's that piece around the logic
[18:20] and everything else that is h like that is encaptured in SAP is way way more
[18:26] important than the fact that like oh this data just happens to be in this database there's a reason why also SAP like takes
[18:33] you know multiple years to implement and get it's not because like oh you know yes the system integrators are slow and
[18:40] part of it but it's it's customized to the way that business actually operates.
[18:45] Um, and I think that's like an important part about why you can't just obscure away the software completely from and
[18:51] and turn it into a data database plus APIs. Yeah, this it's just so important because this
[18:57] is one of the things where like startups look at enterprise software and they
[19:02] think about it in terms of startup scale and so they take something like mundane like expense reporting and like okay
[19:08] well we have 40 people and like you know one person could figure out expense reports for 40 people like you you could
[19:15] hire a human and that and be done with it. that like literally you come back from a trip, you dump the receipts in a
[19:20] bucket and one human rifles through them and the expense reporting problem goes away. Or you say, "Oh, forget the human.
[19:26] We'll just all take pictures of our receipts and OCR it and categorize it and the whole thing will go away." And
[19:33] and that's fine until you have a h 100,000 people in 20 countries with
[19:39] different national laws and policies about business expense and all of those and then you overlay corporate policies
[19:46] and and the whole thing just and then your business is just codified that way and it and you can't replace it. You
[19:53] back in the um in the late 1990s who now is sort of the godfather of enterprise software Larry Ellison at Oracle. back
[20:00] then they were only a database company and entering the world of Netswuite and ERP and all this but he went on a rant
[20:08] he a multi-year rant about how enterprise software was so stupid because everybody customized it and he
[20:14] had this saying that just said businesses should just stick with the 80% solution and they should just use
[20:22] whatever works like 80% of the time and most enterprise people were like well a
[20:27] you're just talking your book because your software only does 80% of what I need. But B, like that's that's just not
[20:34] how it works. Like if you take the auto industry and you just take the top 10 companies in autos,
[20:40] they they all, you know, putting aside EV versus gas or whatever, they all just make cars, which is a lot of known
[20:48] technology with assembly lines and workers. Like what differentiates the
[20:53] the companies and what differentiates them is how they operate and the internal processes to decide what car to
[21:00] make, how many more materials to buy, what currencies to hedge, how many people to hire, when to introduce a new
[21:06] product line. All of that is enterprise resource management and planning. And
[21:14] how is all of that done? It's all in SAP. So those companies are effectively run by people sitting in conference
[21:20] rooms looking at SAP screens and and the difference between
[21:27] Ford and Toyota and General Motors and Daimler are just are not just that
[21:32] they're looking at the same screen. it's that they chose which screens to look at, which customizations to make in
[21:38] those screens, and then they go and they buy steel and aluminum and wire and dashboards and radios from all the same
[21:45] places. And so it's a I I just think that people wildly underestimate the the level of house of sophistication
[21:53] that customers apply to this software. Like when back when we were first starting to get Excel used in companies,
[22:00] you'll laugh at this even like like the we used to do these little visits and we go visit bankers and so we're sitting in
[22:06] Goldman Sachs and we're telling him about Excel is better than Lotus 123 blah blah that's super old. You don't
[22:12] even know what 123 I know. Trust me, it's old. And and the guy at Goldman
[22:17] looked at us and said, "I don't think you understand. We make more money from Excel than you do."
[22:25] and and you're and we're just sitting there like what is he talking about? Like it made no sense to us. And then we
[22:30] started to think about it and it's like well we sell Excel to Morgan Stanley and JP and Chase and everybody else and what
[22:37] Goldman was saying is their application of Excel is so differentiated.
[22:43] A and that's and that wasn't just people typing. They built add-ins. They wrote all this code. They defined their
[22:48] WordPress. know there's this wild underestimation about like you could vibe code your way into enterprise
[22:54] software. I uh was at a dinner last night and there was someone there who um
[22:59] was like the head of revops at a I don't know maybe growth stage startup and his task this is like a thousand plus person
[23:06] company was to rebuild their Salesforce instance internally and you know I think he's like oh well
[23:13] you know we know all the fields we can import all the data and I was like that's not really the part that's tough
[23:19] right it's well how are you deciding what like what gets captured how the
[23:24] whole organizational lines around it. Uh, and then who's going to maintain this also over time. I think that's like
[23:30] a piece that just gets falls off. You know, you can you can vibe code a CRM. We've all vibecoded projects that have
[23:36] like already gone stale and know we haven't touched again because it's painful and it's it's it takes time and
[23:41] needs to adapt the business. Mhm. And and Seema, you've also written about how, you know, there are there's an entire
[23:47] ecosystem of startups now that are just building on top of SAP and that are, you
[23:53] know, like sort of building around all of the kind of headacheinducing stuff
[23:58] and but still using SAP. So, like to both of your points earlier, like the
[24:04] these like legacy SAS systems are just like so deeply embedded that the newer
[24:10] insurgents are just coming and they're, you know, building on top and around them rather than kind of like trying to
[24:16] rip out and get people to migrate completely. A lot of what we're seeing AI being used today is for is how do you
[24:24] make it like I think the word is often used like conversational or like how do you pull the information out and actually make it more usable? How do you
[24:31] retrieve the information from SAP without needing to go you know run a SQL query and get all the information or
[24:37] like look at a bunch of screens. It's like okay well if I want to be able to connect to Steven's point around analyze like you know three different uh sets of
[24:44] tables and different geographies like can I quickly you know query that like a natural language way um can I get
[24:50] reports automatically generated that are customized to me without needing to like go back through the like SAP
[24:55] customization process and I think that is that usability layer is I think
[25:01] indicative of what's happening now with software in general which is accessing the UI is optional and like Going back
[25:08] to the Slackbots point, like you want the information delivered to you versus needing to go to the UI, but the data
[25:15] and the business logic inside either it's SAP or something else that's being replacing it that's building it, but
[25:21] that all still needs to exist one way or another. Mhm. That's a that's an incredibly important
[25:27] point is for for folks to take away which is that the the the biggest thing about enterprise software is it almost
[25:34] always does what somebody is wants it to do. They just don't know how to make it
[25:40] do that. Like there's no report that that SAP can't generate. No graph, no
[25:46] chart, no analysis or whatever. But you you just can't figure it out. Or maybe it's configured so you don't have
[25:52] permissions or something. So the two the way to think of it is in enterprise software the two most frequently used
[25:59] features exist in no enterprise software natively it's export to Excel and export
[26:07] as CSV and or PDF you pick and so all enterprise software the first thing they
[26:14] have to do that's missing when they show up and they do that first demo is the customer say does it do export to Excel
[26:20] or does it do export to CSV or PDF because then you know you have an escape
[26:26] valve to do the thing that you couldn't do before on analysis. And and so what's so cool about where we
[26:33] are today is that now with with the language models you have this incredible
[26:39] way to actually consume those in much easier than you could before. If you think about PDF, like the old way used
[26:47] to be like, okay, I want to figure out like exception handling, some report that that my system emits, you know,
[26:54] declined expense reports or whatever, but I want to do it over some weird time period or across different currencies
[27:01] that it doesn't handle or some weirdness that you can't figure out the UI. So now you can export them all and take this 20
[27:08] PDFs and put them in a model and do a bunch of analysis that you couldn't do
[27:13] before or if you did it was all copy and paste and this mundane thing and to
[27:19] something that Seema wrote about these sort of I don't remember the word you used but these ad hoc business processes
[27:24] are the ones that really become the most interesting because they're interesting because that's how a business runs but
[27:31] they're also interesting because those are the next products Like those are the next companies that
[27:36] people start. You know, CRM used to just be a spreadsheet. Like the this if if you were in a
[27:43] business and you were account manager and you kept track of your accounts, you just kept track of it in Excel and then
[27:50] a company got started to to do that. It wasn't SA. It wasn't Salesforce first. It was the predecessor called Seible.
[27:57] And and then like people like oh we should make a whole company that does this. And that's what's that's what some
[28:04] of these apps are that you're seeing using language models and interfaces that are chat to SAP or to Salesforce.
[28:11] They they are just trying to take advantage of what the LMS are really good at which is synthesizing and
[28:16] orchestrating unstructured information. Yeah. I think we also forget that like Salesforce is like really an enforcement
[28:23] mechanism for like the the the go to market team which is like okay are you collecting all of the information that
[28:30] you need to and of course we can talk about Salesforce hygiene etc as a separate point but like do you have all you know is the human doing the getting
[28:38] the data to then have um like the to then you know capture the state of the
[28:44] business um which okay but I think if we like now switch to the agenda world Um, and I
[28:50] think again we can talk about what agent means, but imagine there's an agent that
[28:55] needs to do outbound calling or outbound messaging. They want to be able to
[29:00] retrieve that information. They don't really care about how the fields are organized or, you know, how many clicks
[29:06] it takes, but they do want to be a they still need to access that information. But then the second piece they need is
[29:11] this context thing. So, we've talked a lot. I think I feel like the internet has talked a lot about context graphs uh
[29:16] over the last six months, but what is that? That's all like the exceptions. What do you do? What do you how do you
[29:23] handle certain cases? It's the edge cases and the permissioning and all that stuff that needs to be um and all the
[29:29] policies that are not necessarily in the fields of Salesforce. Um, and so for the agent to then go go back to this 8020
[29:36] thing, the agent can, you know, extract all the information, send an outbound email based on the information that's in
[29:42] the CRM around the person and their persona and what they do and all that, but then like, okay, how do you deal
[29:48] with um, a case, one case versus another, and how they respond? And it's like, oh, well, normally if it's a
[29:53] person who's in Asia, we respond this way, but if it's a person in the US, we respond this other way. That's not captured in Salesforce, but that's
[30:01] that's was in someone's head. And so that's the context that I think is really important now for agents to be able to act on behalf of this data.
[30:09] Oh, that's super. I mean, for Salesforce in particular, that's incredibly important because I've never met a
[30:15] saleserson, an account manager, an account executive who thinks that the default is the right answer for anything
[30:22] with their account. and and like no, even if they get the Japanese language right, you know, oh, it's spring and the
[30:28] birds are chirping and but you're you're overdue on your payment, your license count is wrong, that even if you do that
[30:33] correctly, the rep is going to want to handle it in their in their specific way. And and I think that this notion of
[30:40] exception handling is just the root of the challenge with with agents, which is
[30:47] almost everything interesting in an enterprise is an exception. Yes. Yep. like that. Like all the people
[30:54] are about exception handling it. You know, it's basically like spend 15 minutes at McDonald's and watch people
[31:01] start in the kiosk and give up and then go watch what they really want and they're like, "Well, I wanted a
[31:06] McFlurry, but I wanted two flavors and mix them together and that's not in the" and it's always the exceptions. And
[31:14] everything about automation in enterprise is handling exceptions. It it just is. It's the strangest thing like
[31:20] but you know enterprise pricing is a great example like how much is it per seat? Well, you have to call us. Well,
[31:26] you call then you talk and then it's still an exception. Yeah. And that that's exactly right. So
[31:31] these exceptions and aren't they're not captured anywhere right now. Mhm. Um now
[31:36] I think if you say if there's you know a voice agent that is doing um let's say
[31:42] compliance check calls for freight as one of our portfolio companies does they're now collecting the exceptions
[31:48] through their voice agent and getting some of that context or if they're we're looking we can talk about computer using
[31:53] agents if you're observing humans and how they are clicking through software how they are responding to things and
[32:00] now we have this ability now to you know not only record data or like record interactions but then process that BLMs
[32:06] then you're able to start collecting some of this context but it's a lot there I mean as Stephen was saying it's ever all the interesting work is around
[32:13] the exceptions so it's not like okay you know 3 days later we've we've we've got it all we've got all the context because
[32:18] also like sales cycles take a long time each exception isn't like handled um with the frequency that you get the data
[32:24] immediately right um and so you have to feel comfortable you have to get to that point where you're like okay we've c we've observed enough interactions to
[32:31] actually capture to understand the exceptions and then on the sales side, the buyer trusts that uh that you know
[32:40] this piece of software can actually you know has captured all the context to handle. Well, let me just add to building on that because I think it
[32:46] helps us to to go back to this notion of headless and what are both the challenges and the opportunities because
[32:52] of course if you're an engineer with almost everyone talking about what's going on in the world in AI today is you
[32:59] think headless and API a agent API just interchange them and so you you think oh
[33:05] well it's code I can write the business process down and and the the problem
[33:10] that you hit right at the beginning is is that if you're not an engineer, you can't even explain the process that you
[33:16] use to resolve a customer issue. You and in fact, it's sort of very interesting
[33:21] to watch Amazon really do some of the best work on this because they really
[33:27] really don't want to have humans. Like they you you you can't call Amazon for anything like it's just hopeless. And so
[33:35] what they're doing is they're learning with everybody like the best way to automate something and it's their
[33:41] religion. And it's their core principle which is you just decide it in favor of the customer. You know, oh they sent the
[33:47] wrong thing. So you go to the chatbot, you tell them. The chatbot understands that you got the wrong thing and it just
[33:54] sends you a new one. And I think that that's so interesting compared to sort
[33:59] of old school exception handling. And then they use the data to go and improve the internal shipping and handling and
[34:05] warehouse process. Maybe it's the product description, a zillion other things or reviews. And and so I find
[34:12] that's what I find so interesting about the capabilities of AI is that it's driving a different definition and
[34:19] different behavior at companies about how to handle exceptions. And I think when we get through sort of the 1.0
[34:25] version of this. We're going to get to a new version where people are like comfortable letting AI do or decide
[34:33] things because they realize it's adding a level of predictability and repeatability to their enterprise. It
[34:39] is. It's funny to think that maybe customer service gets worse in the short term because things stop getting default
[34:47] decided in favor of the customer, you know, like suddenly suddenly you actually have to defend your case again
[34:54] instead of like you being, you know, re-shipped the uh the sensitine toothpaste like you you feel like you
[35:00] were owed. Um, but uh I think I I think maybe then more generally it it sounds
[35:06] like you're both saying that automating the long tail is still kind of the hardest thing about about all of this.
[35:13] Is is that true or would you say that there are other hard things uh that that developers and founders also need to
[35:20] think about? I think that's that's part of it. Um I think there are a lot of other things around like permissioning
[35:25] and that this is this is all I think I could you could probably lump it into the hard tail but oh sorry long tail but like permissioning is part of this right
[35:32] and like you know as you give people or give it you know API access it's like
[35:37] okay so which in which cases can people extract data when when can they write versus read like that all needs to be
[35:45] figured out over time as well and like interactions also between agents right um and I think if you go back to the
[35:50] idea of a system of record there's it's one ideally one set of one central repository of data that is the the
[35:57] source of truth well that now if you're have multiple people accessing and
[36:02] writing to it like who gets to access when and I think that's a that anyways these are additional problems that I
[36:08] think need to be solved solvable but will take time you know well one of the things that happens in
[36:13] in technology shifts is it you know everybody knows the thing about nobody understands exponential when it's
[36:19] happening so you have to be very careful to extrapolate and end up extrapolating linear when something exponential is
[36:24] happening. But the same thing happens with productivity or an analogous thing happens with productivity which is
[36:30] people look at the existing body of work that happens today and they say okay how
[36:35] do we make that easier and then all of a sudden there's all this fear that we're going to automate everything away that
[36:41] everything is just going to become an API which developers and engineers say oh that will be easy and then we'll be
[36:47] in this nirvana world where everything is automated and easy and predictable
[36:52] but they forget that productivity drives new scenarios. And so the minute that
[36:58] you can get something easier with automation and you can actually automate it, which I do think is happening right
[37:05] now with agents and with with language models, well then we're going to dream up a whole bunch of new stuff to do.
[37:11] Like I I just mentioned this this loop that Amazon must be in on customer service. Well, they got rid of all the
[37:17] phone people and the phone experience that would be miserable to do a return and the the challenge response and the
[37:25] fighting and like, can I return this and do I have to package it up or will you just ignore like toothpaste? They don't
[37:30] want it back. Like that's an a pioneering invention by Amazon is like, you know, if somebody gets the wrong
[37:37] consumable, we just don't want it. Like they're poisoning it, they used part of it, it's cheaper to just have them throw
[37:43] it away. Well, that never happened before. Like, you used to have to actually bring spoiled food to the
[37:48] supermarket and show it to them. And so, they've fixed that level of productivity, but now there's this
[37:54] backend that's just out there constantly figuring out how to have it not happen again. And that now they need a new
[38:01] level of analysis, a new set of tools. And the long tail got no shorter. It just got longer in a different way.
[38:08] Yes. And and I I think people forget that that's how innovation is this constant reinvention and it's it's a
[38:15] growing pie, not a static pie. And and all the negativity around AI comes from
[38:21] just thinking that the work to be done is this fixed thing that takes n people
[38:27] and m amount of software and we're just going to replace n people with m plus five and then we don't we're done.
[38:33] There's no jobs anymore. There's just an agent running. And that's just never going to happen. Like legal is a great
[38:40] example of this, like where people do contracts and they think that the law is going to help contracts get get done
[38:47] quicker without lawyers. Except I can assure you contracts will get longer and more sophisticated and encompass way
[38:54] more sets of scenarios than a person ever could. And that's going to create a whole more litigation around it. And that
[39:00] creates a whole ecos. Look, there's the the now apocryphal,
[39:06] semi-apocalypical famous example of radiology, which is a correlation, not a causation, but radiologists all love
[39:14] AI, and now we are having a radiology shortage. It it's not it's there's a lot
[39:19] of reasons. It's complicated, but it it it it just shows that the innovation wasn't static and and the market for the
[39:27] demand wasn't static. And and so I think that a lot of what happens just in the micro at the enterprise level is the
[39:34] minute you automate the most mundane thing and think you have it all squared away whole new things appear like
[39:40] actually like expense reporting is a really good example. You know, first there's nothing, then people figure out
[39:45] how to like do spreadsheets, and then people figure out like, oh, now we have a whole system. We can analyze it. And
[39:51] now all of a sudden business travel, you get ahead of the curve. And you're like, well, now let's just use miles for
[39:58] business travel. Let's, you know, route our travel requests to the best prices we could get at any given moment rather
[40:04] than just default to one carrier. Let's use a specific credit card for business travel that buys us a bunch of different
[40:11] added benefits that we know matter to our patterns of travel. And so suddenly
[40:16] like there's a bigger job called business travel analysis that takes way more people than just booking the
[40:22] flights which everybody can just do on their own. There there's always another layer of analysis on top.
[40:29] Always there. But the analysis then drives new processes and new behaviors that themselves differentiate companies.
[40:36] Look, business travel is a to stick with that example is a huge sync in most companies. It's just a giant expense
[40:42] hole that they wish they could shrink. But once they can tie it to how things
[40:48] perform in their company, then it's more than just expense moderation. It's
[40:53] actually figuring out performance optimization. and figuring that whole thing out becomes like a different kind
[40:59] of job than just booking travel and analyzing expenses. It just becomes this
[41:04] whole remote work optimization tool and then it's a different thing. I think the
[41:10] other thing interesting not to double and you know to spend too much time on business travel but I think it it also ties there are the physical and like
[41:18] digital worlds like there are always things that there will be humans doing
[41:23] you know maybe it's not back office TPS reports but like sales people will be
[41:29] closing deal there will be human interaction to close deals um people will be getting on planes as a result
[41:35] and uh maybe they aren't spending as much time entering data into Salesforce
[41:40] or doing things along the way, but they will there there will be these humans doing online and offline world work and
[41:46] I think that actually is something that you know there will always be a data exhaust from things to capture
[41:54] optimization that needs to happen and that that isn't going away either. Yeah. Well, I think open source software
[41:59] development is actually a really good example of this because like the hardest thing in software development is, you
[42:06] know, you have to be finished at some point so that everybody knows this is a stable release and can go build on it.
[42:12] And the art of finishing is this long tale of like not changing the code.
[42:19] And and there's no API for that. Like developers think there don't they developers don't hesitate to think there
[42:25] should be no API for that. They they they could think of a way to automate it with voting and with a discussion that
[42:32] has sentiment analysis or whatever, but they you still need a bunch of people to concur over a decision to fix or not fix
[42:40] something. And yet they'll adv those those same people will just say some
[42:45] other business process like closing the books for earnings that should just be an API.
[42:50] And it's actually the literally the same mental model. like there's a bunch of stuff and we're deciding when to close
[42:57] the books and what sales to account for what and where. It it's fixing a bug and
[43:02] there's a story around it, a narrative and we have to explain it to our boss and if something goes wrong, we need a
[43:08] trail that explains who did what and and so so much of what a business really is
[43:15] it are just the people deciding things. And all that software does is it
[43:20] uplevels, abstracts, and changes what they decide and how and what tools they use.
[43:26] The the other sort of followup to Seema's point is like it's the best case for just recording everything you do like
[43:32] all like just voice recording everything you do to like capture if if people are, you know, going and flying and closing
[43:39] deals in person. Um, make sure the software or the LLM can kind of capture
[43:44] everything that happens at all times. Obviously not advocating for you know full ponopticon but
[43:52] but synthetic gathering. Exactly. Exactly. And it whether it's like you know
[43:57] recording and you know conversations or taking emails and you know written artifacts and ingesting them. This is
[44:04] all that is the way that the world is moving and exactly. So yeah. Yeah. Well, it's also to your earlier
[44:10] point, you know, expertise exists in this cloud in an organization and and it
[44:15] is the the untapped resource of the modern era and Aaron Levy at Box has
[44:21] done the the most eloquent job of explaining repeatedly the the assets that exist in all of these, you know,
[44:29] Word and Excel documents strewn throughout a company. And it's actually very very hard to to understand which
[44:36] documents are important, which ones to believe. And part of being in a company and having a culture is really knowing
[44:42] the answer to that. And and it's super interesting to watch the customers at
[44:49] Box use Box to to to actually answer those questions. You know, which are the
[44:55] sales PowerPoint presentations that are actually working? which are the spreadsheets and the models that people
[45:00] actually rely on and and I think that that AI is the first thing to come along
[45:06] that really taps into that unstructured information in a company. Yeah, I think um before we wrap up, it
[45:15] might be good to to visit the sort of more immediate history and then the more
[45:21] faraway history of kind of what what headless software even is. Uh I know
[45:26] Stephen you wrote last year a piece uh in reaction to to the rise of MCP
[45:32] servers. Um and in that piece you also related it actually to uh sort of like
[45:40] early Microsoft litigation that the that the Justice Department levied against them and and part of the argument was
[45:47] that Microsoft had a lot of products that could be categorized as middleware. Um, and I just kind of curious, you
[45:54] know, in all of these different software waves that you've witnessed, kind of in in what ways is history rhyming and
[46:01] repeating? Maybe not on the litigation side, but on the, you know, product level. That part will continue, too.
[46:07] Yes. Yeah. It's it's super interesting. I, you know, and I I I love Seema Opine on
[46:15] on where she sees things going with startups in this regard as well, so I'll go quick. But the the real thing with
[46:21] MCP is it's very much like everything we're seeing now is that it so much of it is driven by an engineering view of
[46:29] what would make for a good software architecture and very little of it little of it is being driven by sort of
[46:35] the using seamlessly the physical reality of of the world. And so of course if you're an engineer and you
[46:42] would love to have like every tool you want to use to have a very clean API
[46:48] preferably like a command line interface that pipes text in and out would be perfect but that turns out to like not
[46:55] be how the world wants to work. There are many many reasons why it doesn't want to work that way. Seema touched on
[47:02] many like security and compliance and things like that, but the reality is is that no software wants to be
[47:09] disintermediated by some other layer above it. Like nobody wants to to just
[47:15] be put in a corner and said your job is to just store the this SQL format for
[47:22] expense reports and do nothing more and then we're going to use you only for that and then by the way we're we're
[47:28] piping you through to some other tool to analyze expense reports because that's a that's not a growing business that's a
[47:34] decaying business and and so it this whole notion of like everybody is going
[47:41] to be perfectly content to be abst racted by some, you know, benign layer in the middle. It it just doesn't really
[47:48] work that way. And and it's because customers actually do not want to assemble their scenario from a bunch of
[47:55] different providers because all it takes is your system will only be as stable as
[48:00] the most unstable part of that. So if expense report company goes out of business, you're you're completely out
[48:07] of luck. So, you want your expense report company to be thriving and doing
[48:12] more stuff even though you in your head you're like, I I wish they would just stop. I don't want any more from them.
[48:17] It's getting complicated. Oh, they just did a UI reworking that's driving me crazy. And the flip side is the those
[48:24] companies, they they're not just going to sit there and decay and and they're going to look to the left and they're
[48:30] going to look to the right and they're just going to do the stuff that they see people using with their product. And so
[48:36] SAP the example Seema used, we're seeing this whole ecosystem grow up and SAP is
[48:41] just going to do those things and that's the N now not all of them and
[48:47] most of them they're not going to do very well. In fact, just before this I was talking to somebody and we reminded them that in most giant enterprise
[48:54] companies they view just a tie with some competitor as a win because they'll just
[48:59] bundle it into their existing thing and give it away. And so it's but this middleware layer
[49:06] it's always always very unstable. It looks great in a network hierarchy diagram of the OSI levels of networking
[49:13] but it's just never that stable. Yeah I think two things I'll add. So one
[49:19] is yeah the the practical realities like even go back to the Salesforce example
[49:24] or like workday. Workday has had APIs that you could work with. But can you
[49:29] really actually extract all of the data out of workday in a like clean way and just operate without using workday? No.
[49:36] Workday makes it extremely difficult to actually like get access to the
[49:41] documentation and work with the like and they don't they don't expose all the end. everything about the API to use the
[49:47] API example is this is you know analogous to what we're seeing now which is then it makes it a dumb database
[49:53] right the and so they're not incentivized to do that so I think what we're seeing is there's three paths in
[49:58] for in front of you one if if you were a a consumer or like a business that's looking to buy software one is okay I
[50:05] take Salesforce and I either turn on agent force or build all my agents on
[50:11] top of it and then treat Salesforce as kind of the the just the back end I think to what we just talked about some
[50:18] of that will work but some of that will also not work because Salesforce doesn't want you to have want that to be you
[50:23] know to they don't want to be just the data in the background right um and so you know I think that that
[50:29] there will be mixed mixed results around that and I I don't have I'm not bullish on uh the incumbent software building
[50:34] great agents on top there's option two which is you just totally DIY it you have the most control in that situation
[50:41] um however I think to everything we just talked uh that's really hard, right? Like you have to rebuilding true
[50:47] enterprise software and I think for a startup building rebuilding a CRM much easier for rebuilding, you know, a CRM
[50:53] for a Fortune 500 business, it's it's a lot of business logic to capture and you're also trying to like
[50:59] do open heart surgery while like the patient is like alive, right? Or you know, whatever one you want to use the
[51:04] analogy. Well, hopefully they're alive, but yeah. Yeah. Yeah. Yes. Yes. Yes. Of course, if they're alive, but I mean you're like taking the engine out mid-flight, whatever you want to say as
[51:10] the analogy. Um that's that's really hard and you have to get the like practical realities of permissioning and
[51:16] collaboration and all that right. Then there's a third option and I think this is why we are continue to do what we do in investing in in AI software is
[51:23] because there is a reason that like you know agents can continue to be built the
[51:28] data can be sucked in and built in the background. A lot of what we're seeing right now is um things that are working
[51:34] alongside an SAP or a layer of visibility on top that is um enhancing
[51:39] the experience and allowing the business user to then run agents on top of the
[51:45] existing data they have um and not but also not like throw out all of the the
[51:51] logic they've had in the background. Um and then I think also create a new system of record like voice agents are
[51:56] collecting new data recordings are correcting collecting new data transcription ingestion of documents all
[52:02] of that documentation is pulling in and maybe you know one day these AI uh startups will replace the systems of
[52:08] record in the back end but they are doing so in like a systematic way of observing how the business is operating.
[52:15] I guess I guess to close this out though, Seema, you you sort of just touched on this. Where where are we
[52:20] really seeing the biggest opportunities for startups right now? I think look, a
[52:25] lot of this Yeah, what I was just saying, it's it's it's doing the things that the incumbents are not doing right
[52:31] now, which is um which is going from a layer of collection of data and into how
[52:38] do we take action on top of it, right? And so um take the CRM example, right?
[52:43] It's like I'm not just logging all of the like call information but then now I'm providing the intelligence back
[52:48] around okay how do I prioritize leads which uh accounts should we work on what have what has risk of churn flagging all
[52:55] of that and then like sending the outbound right and so and and and part of that is creating this agentic loop
[53:00] which is you now as the agent sends the outbound sees the response you're understanding okay a what works what
[53:08] didn't what how did people respond and then b you're also collecting like benchmark data view on like okay this
[53:15] type of response is most effective in these cases and in Asia we should be using this language you know type of
[53:21] opening versus in Europe etc that sort of stuff you're now agentically collecting all of that um and that's
[53:26] like an interesting data exhaust so I think that's another area and the third area I just would flag too is we talked about this like physical realities but
[53:32] the other part of physical realities is a lot of the vertical software that builds for the you know the physical
[53:38] world actually um and that is a really interesting interesting set of data
[53:43] that's not it's like hard to capture has been hard to capture historically. Um and you know you will have to continue
[53:50] to um pull together things that um can be cap you know agents have been able to
[53:57] operate on software but then also what humans are doing out in the field machines are doing out in the field and pulling that back in. So like
[54:02] construction, manufacturing, all of that. Well, the universal truth for enterprise software is the the most
[54:10] difficult thing to do that happens to be the dumbest is to attempt to just compete head-on with with an existing
[54:16] category. And and by head-on, I mean not just the same category, but doing it the
[54:22] same way. The biggest opportunity right now is always always to look at the
[54:29] existing uh sort of mental map of enterprise categories and be in between two
[54:35] established players because the thing that you know right now during a massive technology shift is the one thing that
[54:42] established players won't do is disturb their existing product line and go to
[54:48] market. So they absolutely will just be bolting AI on top of their existing
[54:53] product. They they won't be getting rid of it. They won't stop working on it. They won't do anything to to break it.
[55:00] They're just going to try to weather this technology storm by sort of power throughing it, powering powering through
[55:07] it. And so your opportunity in a startup is to just look at two big players who
[55:12] are bolting AI onto the side and exposing some existing API as an agent
[55:17] or whatever and just aim for the middle and do things in in the new way and the
[55:23] new way. And by not attacking head-on, you don't show up at every single customer and have them go, you know,
[55:29] well, you need to the do these 8,000 things before you even enter the door. Instead, you have a equally difficult
[55:36] question, but one you're in control of. It's which is why do you even exist?
[55:41] And and that but you that's your own question. You you don't have to answer to a a series of 20-year frameworks that
[55:50] a 20-year-old framework that got created to answer a bunch of questions that aren't even relevant anymore. And and
[55:55] the best example of this is is is HTTP and HTML. client server existed,
[56:03] but the reason that those took over was not because it did all the things that client server did. In fact, it did none
[56:09] of them, but it implemented that concept in an entirely new way. And so, the web
[56:15] exists in spite of the fact that legacy vendors had a trillion dollars invested
[56:20] on how client servers should work. Well, and I and I would say the other piece too, it's not just two between two legacy vendors, but I think now there's
[56:26] like a layer of translation between two different functions within an organization, too. Oh yeah. Yeah, for sure. Software has always sold to like oh I'm
[56:33] selling into just you know the sales team or the finance team but then there's like these handoffs and which is now the context right but on bills and
[56:40] deals and like that actually also presents an interesting opportunity. So the last question I have which is for Stephen is um so network effects is this
[56:50] thing we always talk about on the consumer side and it's a great you know source of defensibility. No enterprise
[56:55] software business as far as I can tell has successfully done you know implemented network effects but you could argue that is a good source of um
[57:04] durability over time right and I think Salesforce has tried this in in in in a couple ways in the past but do you think
[57:10] that like enterprise software will start entering the the uh the you know the
[57:16] field of network effects in terms of like okay we're going to have both buyers and sellers on our CRM and therefore be able to like mediate these
[57:22] transactions or like yeah I'm curious to get your take on that? Well, certainly network effects outside
[57:28] of a company are extremely difficult for a bunch of compliance and security reasons,
[57:34] but but the biggest network effect in enterprise software is inside of a company. And we're seeing that happen
[57:40] now with with just chat. like all of a sudden you're seeing the it's it's so
[57:46] incredible to be at this dynamic that that almost felt like the good old days when some very motivated person like
[57:53] most people who work in enterprises it turns out are not like super interested in making their job better they actually
[58:00] just want to go to work get paid and go home and they don't come to work every day going how can I make my how could I
[58:06] streamline my task they just want to not mess it up that is a lot of the world
[58:12] but There's a small set of people like those bankers at Goldman Sachs that were like, "How do I do more deals faster,
[58:18] better, more clever models?" And so they were using Excel when when the other
[58:23] bankers were using one 123. There's actually floating around on the internet is this old commercial for Excel, the
[58:29] launch this launch TV ad from the from the late 1990s where or sorry the late
[58:35] 1980s where the first Excel spreadsheets were being used and it's a person sitting there with this monstrous laptop
[58:41] that weighed like 12 pounds in an elevator trying to use it. I I'm laughing because of course they were
[58:46] trying to not run out of battery life in the in the elevator ride which was invariably the case. But all all of a
[58:52] sudden this crowded elevator of a bunch of people in in these 1980s ties and 1980s wearing glasses looking at the
[58:58] spreadsheet going, "What are you doing? How are you doing that?" and getting all excited. And fast forward to 2025 and
[59:07] that's exactly what happened with chat. Like, in fact, I had a friend at SAP
[59:12] that was was writing like a um a SAP white paper about something and and I I
[59:18] just asked them, "Tell me what questions you're trying to answer." And I did the prompt and sent them back a white paper.
[59:26] And I'm positive I kicked off some sort of viral loop, not technically a viral
[59:31] loop, but some sort of network effect viral loop inside of her team because
[59:37] like all of a sudden people are seeing how to make their job better and it's accessible to them and they're doing it.
[59:42] So I I think and to your point Tim like this idea of of a tool that enables two
[59:48] functions to talk together that couldn't before is golden. Like that's exactly
[59:54] like that's literally what enterprise software integration is except that's all manual brute force higher accenture
[1:00:01] kind of stuff. And so if you have products that bridge this and you know Figma did a bunch of this with design
[1:00:06] and product development. And so if you can develop software that leverages AI
[1:00:13] in order to bring together parts of an organization that don't normally communicate that's a whole that's a new
[1:00:19] category. And we've seen that with things like IT budgeting where IT and finance would end
[1:00:26] up with tools that ended up helping them both do forecasting and the cloud enabled that. And so I I think that
[1:00:32] that's that's a huge opportunity. Nice. Well, I think that's also an
[1:00:38] amazing note to end on. Uh thank you so much, Stephen, for for joining us here.
[1:00:43] Thanks, Seema. Yeah. And thank you. And thank you, Seema.
[0:00] There are many things that made software sticky, but a lot of it had to do with the fact that the way a human interacts.
[0:06] In an agentic world, do you actually need that? The data, the logic, everything stored below it is really
[0:11] where the value is. There's this wild underestimation about like you could vibe code your way into enterprise software. Larry Ellison at
[0:18] Oracle, he went on a rant about how enterprise software was so stupid
[0:23] because everybody customized it. The minute you automate the most mundane thing and think you have it all squared
[0:29] away, whole new things appear. Misconception right now is that you can
[0:34] just have you know Postgress database and APIs and then bam like you can replace SAP. That's like absolutely not
[0:40] true. That piece around the logic and everything else that is encaptured in SAP is way way more important than the
[0:47] fact that like oh this data just happens to be in this database. One of the things that happens in technology shifts
[0:53] is nobody understands exponential when it's happening. The biggest opportunity right now is
[1:00] Welcome to the A16Z podcast. I'm here with Seema Amble, a partner here on the
[1:06] enterprise team, and Steven Sinofsky, who is a board partner at E16Z, as well
[1:14] as a former uh member of of Microsoft,
[1:20] friend of the firm. Um, and here we are today to talk about um a piece that Seema
[1:27] wrote about a month ago called Is Software Losing Its Head? Uh, and this piece I'll I'll let Seema talk about it
[1:34] in her own words. Um, but this piece was written a couple months ago. Salesforce
[1:40] announced that they would be going headless. Um, and today we're here to kind of discuss, you know, what does
[1:46] that mean? What does that mean for, you know, the future of SAS products, the future of, um, you know, just just kind
[1:54] of software more generally? So, Seema, um, can you just walk me through first what headless software means and explain
[2:02] kind of what changes it introduces? Yeah. Um, so headless software has really it's it's not a new term, but I
[2:08] think has really risen in uh in like the you know public domain of of interest in in a topic that people are talking
[2:15] about. One of the interesting news points has been Salesforce making this announcement. they were launching headless 360 which was really in classic
[2:22] Salesforce motion you know uh history a uh a marketing announcement more than anything else but it does capture um it
[2:30] sort of it's an acknowledgement of what's happening which is you know traditional software had been built
[2:37] around humans accessing it and um it was workflow to capture data and we could
[2:43] talk more about what that meant in an agentic world do you do you actually need that the UI doesn't matter matter
[2:49] because the agent isn't accessing the software via the UI. We could unpack whether the UI matters or not. But in
[2:55] the idea of the being headless is the the data, the logic, everything stored
[3:02] below it is really where the value is, not just the workflow software that's being tracked at the top.
[3:08] Gotcha. Um, and uh, this was announced a couple months ago. I'm curious kind of
[3:14] in in the past couple months, what have we seen? I mean you wrote even in the piece kind of you at the beginning you
[3:21] were a little bit you know funny maybe and you said is this really even that big of an announcement? Is this sort of
[3:27] a rebrand of you know APIs that they had kind of already made available? So does
[3:33] this feel like a significant change? Is this maybe more of a branding exercise? Um and kind of like what have we even
[3:39] seen in the past couple months since we've been able to kind of observe what changes have have really happened? So
[3:45] I'll separate it out into the Salesforce context and then like the broader context which I think the broader context is more interesting. In the
[3:51] Salesforce context probably not that interesting. Uh I think Salesforce I think rightfully again it was
[3:57] acknowledging a shift that's happening in the market. I don't from what I could tell nothing actually changed. Their 360
[4:03] product was uh the same APIs that had always been exposed now rebranded as as
[4:08] as their 360 product. How and and APIs have always existed. So you know many uh
[4:14] or I shouldn't say always but for a long time have existed. Um but I think the broader trend here is there you know
[4:21] Salesforce among others are thinking about how they build themselves for the agentic world. Um and so if an agent
[4:29] needs to access the data in a CRM like Salesforce um what are they doing it?
[4:34] Are they doing it via the UI or are they using the API? And that's the you know Salesforce is saying like okay hey we
[4:40] know what is changing that there are agents who are needing to access the data. Let's look at the you know let's
[4:46] offer a headless version for them to interact with um the data versus going
[4:51] via the UI. That said again I don't think anything actually changed in the Salesforce context but Salesforce is in
[4:56] the old one. Another example is notion has a headless product and actually I think that makes uh even more sense
[5:02] because it's much hard like I think many users of Salesforce are probably less technically adept less likely to be
[5:09] building their own agents although there are many many more people who are doing that with Salesforce notion users tend you know all things being equal are more
[5:17] I'd say techsavvy and more agentic as as builders and I think notion is is one of
[5:22] many other companies that is also trying to figure out okay what is it that I offer for um and you know how do I make
[5:30] you know what APIs do I expose? I think Stephen will talk more about MCP. Um and and again I think a lot of this is also
[5:36] getting caught up a little bit in nomenclature and like okay what are we calling things? Um and I I I think that's one thing but
[5:42] I think the the broader trend around how agents um access systems of record I
[5:48] think is the the bigger point. Yeah. Yeah. And from my understanding it's also I mean it could also apply to
[5:54] something as simple as a chatbot. you know, it's not necessarily just an API or an MCP server. You know, you you
[6:00] could be, you know, Salesforce um acquired Slack a couple of years ago and like it could be something as simple as
[6:06] like you you sort of interacting with with a CRM via chatbot.
[6:12] Totally. And I think I read somewhere that there's been like a 300% increase in Slackbot uh Slack agent usage. Yeah.
[6:18] which is essentially saying that you don't need to log into the Salesforce EOS uh interface to get the data or
[6:25] whatever data it is. So yeah, it's it's essentially again all these are agentic ways of accessing it versus the human
[6:30] needing to go in log the data or or um from a read perspective go back and see
[6:36] okay here were the like here's this opportunity here's what happened and um look at them themselves um and so the
[6:42] that interface is is less relevant. Yeah. And Stephen, do you have anything to add here just on the kind of like
[6:49] definitional territory that we're covering right now or or kind of this discussion?
[6:54] Well, sir, I mean like we're in definitional hell right now where is is,
[7:01] you know, part of a new wave of technology is you make up a lot of new words for things that you kind of did
[7:08] before. And that's just a natural part of technology evolution. Um, but I I
[7:14] actually think it's super important. Like first you have this, you have a agent, which as far as I can tell right
[7:19] now is also a new word for program that takes a very long time to run and might
[7:24] not finish. And and so yet that's just like a a branding that's the best
[7:30] branding ever is to call a program that's takes a really long time, which we used to call a bug, is now like the
[7:36] coolest new feature ever and it's just now an agent. But in in seriousness, the
[7:42] most interesting way I think to think up what you're really talking about doing differently between an agent and an API
[7:50] is really what are you actually doing? What is the agent itself doing? Is it
[7:56] looking something up? Because that's actually a pretty lightweight thing that all systems are pretty good at. And in
[8:02] fact, many many of the newlyannounced, you know, headless agent APIs are are
[8:09] just lookup and they're just you basically have a new interface to the old way to look something up, which is a
[8:16] lot more forgiving, a lot less UI goo and stuff like that. Then there's like I
[8:21] want to do something and that's where you get into very interesting issues over like well if you do something you
[8:29] have to be impersonating a specific person you have to have their credentials like it's a very is it
[8:35] another paid seat is it the same paid seat you have all these interesting enterprise software issues that come up
[8:42] if you actually want to cause a change to a system of record and then there's
[8:47] the third thing which is analyze. And so analyze is more than look something up.
[8:54] It's actually look up a bunch of stuff. It often involves multiple systems. And that seems very very tuned to an agent
[9:01] because you you're not time bounded. You can spend energy iterate. You can route
[9:06] it to different models and get different answers back and compare them. But it's also where hallucination really is a
[9:13] huge issue because if you're going to go and analyze something, you actually need a way to verify that everything every
[9:21] step of that analysis was correct. And so I think it's super interesting and important when you look at headless and
[9:28] agent which are conflated in you sort of have to figure out what you're talking about because we're on different places
[9:35] in the evolution the learning curve and the deployment of agents relative to
[9:40] sort of that three-way matrix matrix. Yeah. I I think this is actually a good
[9:46] leadup into a follow-up question, which is kind of like historically, what has made software sticky and how are agents
[9:54] starting to disrupt that? And I I leave that to either of you to answer. Maybe you guys can both kind of debate about
[10:00] that. Yeah, I'd say there there are many things that made software sticky, but a
[10:06] lot of it had to do with the fact that um it was built around like the the way a human interacts, right? So um the UI
[10:15] was sticky because you know the number of times you had to read and write the frequency of access the downstream
[10:22] workflows all of the like undocumented like you know what we call SOPs or uh standard operating procedures all the
[10:28] stuff that happened around the software that got ingrained in muscle memory and process and then external parties etc.
[10:34] So like a CRM may be sticky because a sales rep needs to go in and out of it
[10:39] all the time. They're used to interacting with Salesforce. A lot of times when like new VPs of sales come into our companies, they they're like
[10:45] they mandate that Salesforce is there because they're used to using it. Their teams are used to using it. Um and then
[10:51] there's, you know, finance may rely on the Salesforce um output for billing and
[10:56] upstream marketing is going to rely on it as well. And so there's these dependencies. Um and these all are
[11:02] driving stickiness. But I think the other piece too is there you need one single set of truth, right? you need to
[11:09] know like an account is closed and who is working on it and all of that needs to be logged in one place. Um and I
[11:16] think if you go from CRM to say an ERP or payroll like that absolutely has even like legal reasons and compliance
[11:23] reasons why you can't have um numbers that are not being you know tracked uh
[11:29] as cleanly and and correctly as you know an auditor might like for example. Um so
[11:34] anyways this all drove stickiness there and and and durability because you know you were used to using Salesforce the
[11:40] whole ecosystem was using Salesforce and it was the default option and maybe you
[11:45] know there's one or two others in the market. Um and so I think historically those were some of the things that were were driving stickiness.
[11:53] Yeah. I mean I those are all exactly right. I I think it's important to also consider that the most sticky thing you
[12:01] could do is actually collect money from a customer. And if you're collecting money, it turns out it's really really
[12:07] hard for them to stop sending you money. And it's really hard for them to figure out what to do if they stop sending you
[12:14] money. And and it it sounds really trit, but the the stickiest software is
[12:19] software that's getting used somewhere. Then when you dig in and try to come up with reasons, well, it just depends on
[12:25] who you talk to in a company, you know, you talk to the HIPPA compliance people in some company and they're going to
[12:32] tell you this is the software you have to use because it's like the most bestest HIPPA compliant software. If you
[12:38] talk to the administrators, you're going to hear about onboarding new users. If you talk to the users, you're going to
[12:44] hear about muscle memory and keystrokes or labor unions or whatever. and and so
[12:51] you have to be yet you you really want to get the software sold and that's your
[12:56] fastest path to sticky and after that it it's sort of you know a winner's tail
[13:02] over over what caused it to be sticky and and in fact the best thing about
[13:07] sticky is if you're the rep for a company that you've sold something to and the company is threatening you like
[13:14] hey we're going to replace you we're just going to listen to them and you're going to find what's sticky. And if that
[13:21] works like three or four times across different accounts, then you've just told the tale as to what made the
[13:27] product sticky. It doesn't matter what the PMs or what anybody else thought of. It could be some crazy arcane thing, you
[13:34] know, like I have stories of lots of sticky software and lots of arcane things, but like anyone who's ever tried
[13:41] to displace um Microsoft Outlook as email very quickly learned about
[13:47] delegate access and and having calendars owned by multiple people and all of this
[13:53] crazy stuff. And like I can tell you there was no meeting where we said, "Okay, let's figure out how to make the
[13:59] calendar the sticky part of Outlook and make sure we handle recurring meeting exception handling well." And then you
[14:06] go and you find out, you know, General Motors isn't going to displace like 600,000 seats because of the calendar or
[14:13] some crazy thing like that. And so you can, it's really amazing in enterprise software what causes sticky and how you
[14:20] can actually capitalize it on it when somebody threatens to take you out of the out of the enterprise.
[14:26] I I think there's a really good point there in two things. Inertia is a really powerful force. And then I think the other thing is
[14:32] yeah, nobody when they're building the software, they're not like thinking about like this rubric we put together and like tick tick tick. We got all
[14:38] these features that are going to do all these things. But I think the practical reality is also as software extends its
[14:44] tentacles across an organization and it gets ingrained in people using it and they've been paying for it for a long
[14:50] time, it just seeps into how people are doing things and that's like hard to rip out.
[14:55] Yeah. Yeah. You even talk about this in your PC mode where there's sort of all of these like invisible tacet sort of
[15:03] understandings about how to use different products or things that are embedded both within the software but
[15:08] also within the people using them where it's just like it does become hard after a while to uh to extricate yourself from
[15:16] from whatever ecosystem you happen to be in. And in fact, Stephen, I think you you've even you know said the SAS
[15:24] apocalypse is overblown. you've written an essay called the death of software. Nah. Um where you where you you know
[15:32] emphatically sort of rejected this idea. So maybe if you want to if you want to maybe just recount that piece a little
[15:38] bit for us. Well, I mean Seema co-wrote a post on on SAP which is sort of the ultimate ultimate example of sticky software. I
[15:46] mean there is nothing the the only software that's stickier than SAP is behind the scenes and it's the software
[15:53] that insurance companies wrote and they wrote all this software like 50 years
[15:59] ago or 75 years ago and if you ever there's no replacing it like it it just
[16:04] it in fact you whenever jokes come up about like businesses that are looking for cobalt programmers it's to go and
[16:11] work on the insurance software that exists in in every state of the union
[16:17] and and in many ways what you're seeing like with the one of the biggest successes to date in Stripe has been
[16:24] somebody actually went in and for the first time in it two generations coded
[16:30] up the software to collect money from people which itself had previously been an unsolved problem on the scale of
[16:38] insurance because nobody put together the tax laws for every country every
[16:44] every jurisdiction every locality, every border crossing, every currency exchange like it it it's
[16:53] mindblowing that. And so now that is the most sticky. So like that is not going anywhere ever. Like it it'll be like
[17:01] we'll be doing this podcast with like great grandchildren 100 years from now talking about how sticky that experience
[17:08] was. Just like I told like oh you didn't know this but the software that runs all state is older than me and it's not
[17:15] going anywhere and that's because the these examples are ones that codified an
[17:22] external force and that external force was the regulatory body that they
[17:27] embraced the seamless examples of SAP like it just codified a company and and
[17:34] so like if you take SAP out of a large automobile manufacturer
[17:39] there's no automobile manufacturer left or or Walmart like the company just evaporates
[17:46] because the the company is defined not just by purchasing the software not even
[17:51] by just using it but by how that they codified the business rules into that
[17:57] product. I think it's a good point to double click on because I think a misconception
[18:03] right now is that SAP okay well you can just have you know Postgress database and APIs and then bam like you can
[18:10] replace API replace SAP and that's like absolutely not true. I think partly I
[18:15] mean Stephen I don't know if you want to elaborate on or not I'm happy to but I think it's that piece around the logic
[18:20] and everything else that is h like that is encaptured in SAP is way way more
[18:26] important than the fact that like oh this data just happens to be in this database there's a reason why also SAP like takes
[18:33] you know multiple years to implement and get it's not because like oh you know yes the system integrators are slow and
[18:40] part of it but it's it's customized to the way that business actually operates.
[18:45] Um, and I think that's like an important part about why you can't just obscure away the software completely from and
[18:51] and turn it into a data database plus APIs. Yeah, this it's just so important because this
[18:57] is one of the things where like startups look at enterprise software and they
[19:02] think about it in terms of startup scale and so they take something like mundane like expense reporting and like okay
[19:08] well we have 40 people and like you know one person could figure out expense reports for 40 people like you you could
[19:15] hire a human and that and be done with it. that like literally you come back from a trip, you dump the receipts in a
[19:20] bucket and one human rifles through them and the expense reporting problem goes away. Or you say, "Oh, forget the human.
[19:26] We'll just all take pictures of our receipts and OCR it and categorize it and the whole thing will go away." And
[19:33] and that's fine until you have a h 100,000 people in 20 countries with
[19:39] different national laws and policies about business expense and all of those and then you overlay corporate policies
[19:46] and and the whole thing just and then your business is just codified that way and it and you can't replace it. You
[19:53] back in the um in the late 1990s who now is sort of the godfather of enterprise software Larry Ellison at Oracle. back
[20:00] then they were only a database company and entering the world of Netswuite and ERP and all this but he went on a rant
[20:08] he a multi-year rant about how enterprise software was so stupid because everybody customized it and he
[20:14] had this saying that just said businesses should just stick with the 80% solution and they should just use
[20:22] whatever works like 80% of the time and most enterprise people were like well a
[20:27] you're just talking your book because your software only does 80% of what I need. But B, like that's that's just not
[20:34] how it works. Like if you take the auto industry and you just take the top 10 companies in autos,
[20:40] they they all, you know, putting aside EV versus gas or whatever, they all just make cars, which is a lot of known
[20:48] technology with assembly lines and workers. Like what differentiates the
[20:53] the companies and what differentiates them is how they operate and the internal processes to decide what car to
[21:00] make, how many more materials to buy, what currencies to hedge, how many people to hire, when to introduce a new
[21:06] product line. All of that is enterprise resource management and planning. And
[21:14] how is all of that done? It's all in SAP. So those companies are effectively run by people sitting in conference
[21:20] rooms looking at SAP screens and and the difference between
[21:27] Ford and Toyota and General Motors and Daimler are just are not just that
[21:32] they're looking at the same screen. it's that they chose which screens to look at, which customizations to make in
[21:38] those screens, and then they go and they buy steel and aluminum and wire and dashboards and radios from all the same
[21:45] places. And so it's a I I just think that people wildly underestimate the the level of house of sophistication
[21:53] that customers apply to this software. Like when back when we were first starting to get Excel used in companies,
[22:00] you'll laugh at this even like like the we used to do these little visits and we go visit bankers and so we're sitting in
[22:06] Goldman Sachs and we're telling him about Excel is better than Lotus 123 blah blah that's super old. You don't
[22:12] even know what 123 I know. Trust me, it's old. And and the guy at Goldman
[22:17] looked at us and said, "I don't think you understand. We make more money from Excel than you do."
[22:25] and and you're and we're just sitting there like what is he talking about? Like it made no sense to us. And then we
[22:30] started to think about it and it's like well we sell Excel to Morgan Stanley and JP and Chase and everybody else and what
[22:37] Goldman was saying is their application of Excel is so differentiated.
[22:43] A and that's and that wasn't just people typing. They built add-ins. They wrote all this code. They defined their
[22:48] WordPress. know there's this wild underestimation about like you could vibe code your way into enterprise
[22:54] software. I uh was at a dinner last night and there was someone there who um
[22:59] was like the head of revops at a I don't know maybe growth stage startup and his task this is like a thousand plus person
[23:06] company was to rebuild their Salesforce instance internally and you know I think he's like oh well
[23:13] you know we know all the fields we can import all the data and I was like that's not really the part that's tough
[23:19] right it's well how are you deciding what like what gets captured how the
[23:24] whole organizational lines around it. Uh, and then who's going to maintain this also over time. I think that's like
[23:30] a piece that just gets falls off. You know, you can you can vibe code a CRM. We've all vibecoded projects that have
[23:36] like already gone stale and know we haven't touched again because it's painful and it's it's it takes time and
[23:41] needs to adapt the business. Mhm. And and Seema, you've also written about how, you know, there are there's an entire
[23:47] ecosystem of startups now that are just building on top of SAP and that are, you
[23:53] know, like sort of building around all of the kind of headacheinducing stuff
[23:58] and but still using SAP. So, like to both of your points earlier, like the
[24:04] these like legacy SAS systems are just like so deeply embedded that the newer
[24:10] insurgents are just coming and they're, you know, building on top and around them rather than kind of like trying to
[24:16] rip out and get people to migrate completely. A lot of what we're seeing AI being used today is for is how do you
[24:24] make it like I think the word is often used like conversational or like how do you pull the information out and actually make it more usable? How do you
[24:31] retrieve the information from SAP without needing to go you know run a SQL query and get all the information or
[24:37] like look at a bunch of screens. It's like okay well if I want to be able to connect to Steven's point around analyze like you know three different uh sets of
[24:44] tables and different geographies like can I quickly you know query that like a natural language way um can I get
[24:50] reports automatically generated that are customized to me without needing to like go back through the like SAP
[24:55] customization process and I think that is that usability layer is I think
[25:01] indicative of what's happening now with software in general which is accessing the UI is optional and like Going back
[25:08] to the Slackbots point, like you want the information delivered to you versus needing to go to the UI, but the data
[25:15] and the business logic inside either it's SAP or something else that's being replacing it that's building it, but
[25:21] that all still needs to exist one way or another. Mhm. That's a that's an incredibly important
[25:27] point is for for folks to take away which is that the the the biggest thing about enterprise software is it almost
[25:34] always does what somebody is wants it to do. They just don't know how to make it
[25:40] do that. Like there's no report that that SAP can't generate. No graph, no
[25:46] chart, no analysis or whatever. But you you just can't figure it out. Or maybe it's configured so you don't have
[25:52] permissions or something. So the two the way to think of it is in enterprise software the two most frequently used
[25:59] features exist in no enterprise software natively it's export to Excel and export
[26:07] as CSV and or PDF you pick and so all enterprise software the first thing they
[26:14] have to do that's missing when they show up and they do that first demo is the customer say does it do export to Excel
[26:20] or does it do export to CSV or PDF because then you know you have an escape
[26:26] valve to do the thing that you couldn't do before on analysis. And and so what's so cool about where we
[26:33] are today is that now with with the language models you have this incredible
[26:39] way to actually consume those in much easier than you could before. If you think about PDF, like the old way used
[26:47] to be like, okay, I want to figure out like exception handling, some report that that my system emits, you know,
[26:54] declined expense reports or whatever, but I want to do it over some weird time period or across different currencies
[27:01] that it doesn't handle or some weirdness that you can't figure out the UI. So now you can export them all and take this 20
[27:08] PDFs and put them in a model and do a bunch of analysis that you couldn't do
[27:13] before or if you did it was all copy and paste and this mundane thing and to
[27:19] something that Seema wrote about these sort of I don't remember the word you used but these ad hoc business processes
[27:24] are the ones that really become the most interesting because they're interesting because that's how a business runs but
[27:31] they're also interesting because those are the next products Like those are the next companies that
[27:36] people start. You know, CRM used to just be a spreadsheet. Like the this if if you were in a
[27:43] business and you were account manager and you kept track of your accounts, you just kept track of it in Excel and then
[27:50] a company got started to to do that. It wasn't SA. It wasn't Salesforce first. It was the predecessor called Seible.
[27:57] And and then like people like oh we should make a whole company that does this. And that's what's that's what some
[28:04] of these apps are that you're seeing using language models and interfaces that are chat to SAP or to Salesforce.
[28:11] They they are just trying to take advantage of what the LMS are really good at which is synthesizing and
[28:16] orchestrating unstructured information. Yeah. I think we also forget that like Salesforce is like really an enforcement
[28:23] mechanism for like the the the go to market team which is like okay are you collecting all of the information that
[28:30] you need to and of course we can talk about Salesforce hygiene etc as a separate point but like do you have all you know is the human doing the getting
[28:38] the data to then have um like the to then you know capture the state of the
[28:44] business um which okay but I think if we like now switch to the agenda world Um, and I
[28:50] think again we can talk about what agent means, but imagine there's an agent that
[28:55] needs to do outbound calling or outbound messaging. They want to be able to
[29:00] retrieve that information. They don't really care about how the fields are organized or, you know, how many clicks
[29:06] it takes, but they do want to be a they still need to access that information. But then the second piece they need is
[29:11] this context thing. So, we've talked a lot. I think I feel like the internet has talked a lot about context graphs uh
[29:16] over the last six months, but what is that? That's all like the exceptions. What do you do? What do you how do you
[29:23] handle certain cases? It's the edge cases and the permissioning and all that stuff that needs to be um and all the
[29:29] policies that are not necessarily in the fields of Salesforce. Um, and so for the agent to then go go back to this 8020
[29:36] thing, the agent can, you know, extract all the information, send an outbound email based on the information that's in
[29:42] the CRM around the person and their persona and what they do and all that, but then like, okay, how do you deal
[29:48] with um, a case, one case versus another, and how they respond? And it's like, oh, well, normally if it's a
[29:53] person who's in Asia, we respond this way, but if it's a person in the US, we respond this other way. That's not captured in Salesforce, but that's
[30:01] that's was in someone's head. And so that's the context that I think is really important now for agents to be able to act on behalf of this data.
[30:09] Oh, that's super. I mean, for Salesforce in particular, that's incredibly important because I've never met a
[30:15] saleserson, an account manager, an account executive who thinks that the default is the right answer for anything
[30:22] with their account. and and like no, even if they get the Japanese language right, you know, oh, it's spring and the
[30:28] birds are chirping and but you're you're overdue on your payment, your license count is wrong, that even if you do that
[30:33] correctly, the rep is going to want to handle it in their in their specific way. And and I think that this notion of
[30:40] exception handling is just the root of the challenge with with agents, which is
[30:47] almost everything interesting in an enterprise is an exception. Yes. Yep. like that. Like all the people
[30:54] are about exception handling it. You know, it's basically like spend 15 minutes at McDonald's and watch people
[31:01] start in the kiosk and give up and then go watch what they really want and they're like, "Well, I wanted a
[31:06] McFlurry, but I wanted two flavors and mix them together and that's not in the" and it's always the exceptions. And
[31:14] everything about automation in enterprise is handling exceptions. It it just is. It's the strangest thing like
[31:20] but you know enterprise pricing is a great example like how much is it per seat? Well, you have to call us. Well,
[31:26] you call then you talk and then it's still an exception. Yeah. And that that's exactly right. So
[31:31] these exceptions and aren't they're not captured anywhere right now. Mhm. Um now
[31:36] I think if you say if there's you know a voice agent that is doing um let's say
[31:42] compliance check calls for freight as one of our portfolio companies does they're now collecting the exceptions
[31:48] through their voice agent and getting some of that context or if they're we're looking we can talk about computer using
[31:53] agents if you're observing humans and how they are clicking through software how they are responding to things and
[32:00] now we have this ability now to you know not only record data or like record interactions but then process that BLMs
[32:06] then you're able to start collecting some of this context but it's a lot there I mean as Stephen was saying it's ever all the interesting work is around
[32:13] the exceptions so it's not like okay you know 3 days later we've we've we've got it all we've got all the context because
[32:18] also like sales cycles take a long time each exception isn't like handled um with the frequency that you get the data
[32:24] immediately right um and so you have to feel comfortable you have to get to that point where you're like okay we've c we've observed enough interactions to
[32:31] actually capture to understand the exceptions and then on the sales side, the buyer trusts that uh that you know
[32:40] this piece of software can actually you know has captured all the context to handle. Well, let me just add to building on that because I think it
[32:46] helps us to to go back to this notion of headless and what are both the challenges and the opportunities because
[32:52] of course if you're an engineer with almost everyone talking about what's going on in the world in AI today is you
[32:59] think headless and API a agent API just interchange them and so you you think oh
[33:05] well it's code I can write the business process down and and the the problem
[33:10] that you hit right at the beginning is is that if you're not an engineer, you can't even explain the process that you
[33:16] use to resolve a customer issue. You and in fact, it's sort of very interesting
[33:21] to watch Amazon really do some of the best work on this because they really
[33:27] really don't want to have humans. Like they you you you can't call Amazon for anything like it's just hopeless. And so
[33:35] what they're doing is they're learning with everybody like the best way to automate something and it's their
[33:41] religion. And it's their core principle which is you just decide it in favor of the customer. You know, oh they sent the
[33:47] wrong thing. So you go to the chatbot, you tell them. The chatbot understands that you got the wrong thing and it just
[33:54] sends you a new one. And I think that that's so interesting compared to sort
[33:59] of old school exception handling. And then they use the data to go and improve the internal shipping and handling and
[34:05] warehouse process. Maybe it's the product description, a zillion other things or reviews. And and so I find
[34:12] that's what I find so interesting about the capabilities of AI is that it's driving a different definition and
[34:19] different behavior at companies about how to handle exceptions. And I think when we get through sort of the 1.0
[34:25] version of this. We're going to get to a new version where people are like comfortable letting AI do or decide
[34:33] things because they realize it's adding a level of predictability and repeatability to their enterprise. It
[34:39] is. It's funny to think that maybe customer service gets worse in the short term because things stop getting default
[34:47] decided in favor of the customer, you know, like suddenly suddenly you actually have to defend your case again
[34:54] instead of like you being, you know, re-shipped the uh the sensitine toothpaste like you you feel like you
[35:00] were owed. Um, but uh I think I I think maybe then more generally it it sounds
[35:06] like you're both saying that automating the long tail is still kind of the hardest thing about about all of this.
[35:13] Is is that true or would you say that there are other hard things uh that that developers and founders also need to
[35:20] think about? I think that's that's part of it. Um I think there are a lot of other things around like permissioning
[35:25] and that this is this is all I think I could you could probably lump it into the hard tail but oh sorry long tail but like permissioning is part of this right
[35:32] and like you know as you give people or give it you know API access it's like
[35:37] okay so which in which cases can people extract data when when can they write versus read like that all needs to be
[35:45] figured out over time as well and like interactions also between agents right um and I think if you go back to the
[35:50] idea of a system of record there's it's one ideally one set of one central repository of data that is the the
[35:57] source of truth well that now if you're have multiple people accessing and
[36:02] writing to it like who gets to access when and I think that's a that anyways these are additional problems that I
[36:08] think need to be solved solvable but will take time you know well one of the things that happens in
[36:13] in technology shifts is it you know everybody knows the thing about nobody understands exponential when it's
[36:19] happening so you have to be very careful to extrapolate and end up extrapolating linear when something exponential is
[36:24] happening. But the same thing happens with productivity or an analogous thing happens with productivity which is
[36:30] people look at the existing body of work that happens today and they say okay how
[36:35] do we make that easier and then all of a sudden there's all this fear that we're going to automate everything away that
[36:41] everything is just going to become an API which developers and engineers say oh that will be easy and then we'll be
[36:47] in this nirvana world where everything is automated and easy and predictable
[36:52] but they forget that productivity drives new scenarios. And so the minute that
[36:58] you can get something easier with automation and you can actually automate it, which I do think is happening right
[37:05] now with agents and with with language models, well then we're going to dream up a whole bunch of new stuff to do.
[37:11] Like I I just mentioned this this loop that Amazon must be in on customer service. Well, they got rid of all the
[37:17] phone people and the phone experience that would be miserable to do a return and the the challenge response and the
[37:25] fighting and like, can I return this and do I have to package it up or will you just ignore like toothpaste? They don't
[37:30] want it back. Like that's an a pioneering invention by Amazon is like, you know, if somebody gets the wrong
[37:37] consumable, we just don't want it. Like they're poisoning it, they used part of it, it's cheaper to just have them throw
[37:43] it away. Well, that never happened before. Like, you used to have to actually bring spoiled food to the
[37:48] supermarket and show it to them. And so, they've fixed that level of productivity, but now there's this
[37:54] backend that's just out there constantly figuring out how to have it not happen again. And that now they need a new
[38:01] level of analysis, a new set of tools. And the long tail got no shorter. It just got longer in a different way.
[38:08] Yes. And and I I think people forget that that's how innovation is this constant reinvention and it's it's a
[38:15] growing pie, not a static pie. And and all the negativity around AI comes from
[38:21] just thinking that the work to be done is this fixed thing that takes n people
[38:27] and m amount of software and we're just going to replace n people with m plus five and then we don't we're done.
[38:33] There's no jobs anymore. There's just an agent running. And that's just never going to happen. Like legal is a great
[38:40] example of this, like where people do contracts and they think that the law is going to help contracts get get done
[38:47] quicker without lawyers. Except I can assure you contracts will get longer and more sophisticated and encompass way
[38:54] more sets of scenarios than a person ever could. And that's going to create a whole more litigation around it. And that
[39:00] creates a whole ecos. Look, there's the the now apocryphal,
[39:06] semi-apocalypical famous example of radiology, which is a correlation, not a causation, but radiologists all love
[39:14] AI, and now we are having a radiology shortage. It it's not it's there's a lot
[39:19] of reasons. It's complicated, but it it it it just shows that the innovation wasn't static and and the market for the
[39:27] demand wasn't static. And and so I think that a lot of what happens just in the micro at the enterprise level is the
[39:34] minute you automate the most mundane thing and think you have it all squared away whole new things appear like
[39:40] actually like expense reporting is a really good example. You know, first there's nothing, then people figure out
[39:45] how to like do spreadsheets, and then people figure out like, oh, now we have a whole system. We can analyze it. And
[39:51] now all of a sudden business travel, you get ahead of the curve. And you're like, well, now let's just use miles for
[39:58] business travel. Let's, you know, route our travel requests to the best prices we could get at any given moment rather
[40:04] than just default to one carrier. Let's use a specific credit card for business travel that buys us a bunch of different
[40:11] added benefits that we know matter to our patterns of travel. And so suddenly
[40:16] like there's a bigger job called business travel analysis that takes way more people than just booking the
[40:22] flights which everybody can just do on their own. There there's always another layer of analysis on top.
[40:29] Always there. But the analysis then drives new processes and new behaviors that themselves differentiate companies.
[40:36] Look, business travel is a to stick with that example is a huge sync in most companies. It's just a giant expense
[40:42] hole that they wish they could shrink. But once they can tie it to how things
[40:48] perform in their company, then it's more than just expense moderation. It's
[40:53] actually figuring out performance optimization. and figuring that whole thing out becomes like a different kind
[40:59] of job than just booking travel and analyzing expenses. It just becomes this
[41:04] whole remote work optimization tool and then it's a different thing. I think the
[41:10] other thing interesting not to double and you know to spend too much time on business travel but I think it it also ties there are the physical and like
[41:18] digital worlds like there are always things that there will be humans doing
[41:23] you know maybe it's not back office TPS reports but like sales people will be
[41:29] closing deal there will be human interaction to close deals um people will be getting on planes as a result
[41:35] and uh maybe they aren't spending as much time entering data into Salesforce
[41:40] or doing things along the way, but they will there there will be these humans doing online and offline world work and
[41:46] I think that actually is something that you know there will always be a data exhaust from things to capture
[41:54] optimization that needs to happen and that that isn't going away either. Yeah. Well, I think open source software
[41:59] development is actually a really good example of this because like the hardest thing in software development is, you
[42:06] know, you have to be finished at some point so that everybody knows this is a stable release and can go build on it.
[42:12] And the art of finishing is this long tale of like not changing the code.
[42:19] And and there's no API for that. Like developers think there don't they developers don't hesitate to think there
[42:25] should be no API for that. They they they could think of a way to automate it with voting and with a discussion that
[42:32] has sentiment analysis or whatever, but they you still need a bunch of people to concur over a decision to fix or not fix
[42:40] something. And yet they'll adv those those same people will just say some
[42:45] other business process like closing the books for earnings that should just be an API.
[42:50] And it's actually the literally the same mental model. like there's a bunch of stuff and we're deciding when to close
[42:57] the books and what sales to account for what and where. It it's fixing a bug and
[43:02] there's a story around it, a narrative and we have to explain it to our boss and if something goes wrong, we need a
[43:08] trail that explains who did what and and so so much of what a business really is
[43:15] it are just the people deciding things. And all that software does is it
[43:20] uplevels, abstracts, and changes what they decide and how and what tools they use.
[43:26] The the other sort of followup to Seema's point is like it's the best case for just recording everything you do like
[43:32] all like just voice recording everything you do to like capture if if people are, you know, going and flying and closing
[43:39] deals in person. Um, make sure the software or the LLM can kind of capture
[43:44] everything that happens at all times. Obviously not advocating for you know full ponopticon but
[43:52] but synthetic gathering. Exactly. Exactly. And it whether it's like you know
[43:57] recording and you know conversations or taking emails and you know written artifacts and ingesting them. This is
[44:04] all that is the way that the world is moving and exactly. So yeah. Yeah. Well, it's also to your earlier
[44:10] point, you know, expertise exists in this cloud in an organization and and it
[44:15] is the the untapped resource of the modern era and Aaron Levy at Box has
[44:21] done the the most eloquent job of explaining repeatedly the the assets that exist in all of these, you know,
[44:29] Word and Excel documents strewn throughout a company. And it's actually very very hard to to understand which
[44:36] documents are important, which ones to believe. And part of being in a company and having a culture is really knowing
[44:42] the answer to that. And and it's super interesting to watch the customers at
[44:49] Box use Box to to to actually answer those questions. You know, which are the
[44:55] sales PowerPoint presentations that are actually working? which are the spreadsheets and the models that people
[45:00] actually rely on and and I think that that AI is the first thing to come along
[45:06] that really taps into that unstructured information in a company. Yeah, I think um before we wrap up, it
[45:15] might be good to to visit the sort of more immediate history and then the more
[45:21] faraway history of kind of what what headless software even is. Uh I know
[45:26] Stephen you wrote last year a piece uh in reaction to to the rise of MCP
[45:32] servers. Um and in that piece you also related it actually to uh sort of like
[45:40] early Microsoft litigation that the that the Justice Department levied against them and and part of the argument was
[45:47] that Microsoft had a lot of products that could be categorized as middleware. Um, and I just kind of curious, you
[45:54] know, in all of these different software waves that you've witnessed, kind of in in what ways is history rhyming and
[46:01] repeating? Maybe not on the litigation side, but on the, you know, product level. That part will continue, too.
[46:07] Yes. Yeah. It's it's super interesting. I, you know, and I I I love Seema Opine on
[46:15] on where she sees things going with startups in this regard as well, so I'll go quick. But the the real thing with
[46:21] MCP is it's very much like everything we're seeing now is that it so much of it is driven by an engineering view of
[46:29] what would make for a good software architecture and very little of it little of it is being driven by sort of
[46:35] the using seamlessly the physical reality of of the world. And so of course if you're an engineer and you
[46:42] would love to have like every tool you want to use to have a very clean API
[46:48] preferably like a command line interface that pipes text in and out would be perfect but that turns out to like not
[46:55] be how the world wants to work. There are many many reasons why it doesn't want to work that way. Seema touched on
[47:02] many like security and compliance and things like that, but the reality is is that no software wants to be
[47:09] disintermediated by some other layer above it. Like nobody wants to to just
[47:15] be put in a corner and said your job is to just store the this SQL format for
[47:22] expense reports and do nothing more and then we're going to use you only for that and then by the way we're we're
[47:28] piping you through to some other tool to analyze expense reports because that's a that's not a growing business that's a
[47:34] decaying business and and so it this whole notion of like everybody is going
[47:41] to be perfectly content to be abst racted by some, you know, benign layer in the middle. It it just doesn't really
[47:48] work that way. And and it's because customers actually do not want to assemble their scenario from a bunch of
[47:55] different providers because all it takes is your system will only be as stable as
[48:00] the most unstable part of that. So if expense report company goes out of business, you're you're completely out
[48:07] of luck. So, you want your expense report company to be thriving and doing
[48:12] more stuff even though you in your head you're like, I I wish they would just stop. I don't want any more from them.
[48:17] It's getting complicated. Oh, they just did a UI reworking that's driving me crazy. And the flip side is the those
[48:24] companies, they they're not just going to sit there and decay and and they're going to look to the left and they're
[48:30] going to look to the right and they're just going to do the stuff that they see people using with their product. And so
[48:36] SAP the example Seema used, we're seeing this whole ecosystem grow up and SAP is
[48:41] just going to do those things and that's the N now not all of them and
[48:47] most of them they're not going to do very well. In fact, just before this I was talking to somebody and we reminded them that in most giant enterprise
[48:54] companies they view just a tie with some competitor as a win because they'll just
[48:59] bundle it into their existing thing and give it away. And so it's but this middleware layer
[49:06] it's always always very unstable. It looks great in a network hierarchy diagram of the OSI levels of networking
[49:13] but it's just never that stable. Yeah I think two things I'll add. So one
[49:19] is yeah the the practical realities like even go back to the Salesforce example
[49:24] or like workday. Workday has had APIs that you could work with. But can you
[49:29] really actually extract all of the data out of workday in a like clean way and just operate without using workday? No.
[49:36] Workday makes it extremely difficult to actually like get access to the
[49:41] documentation and work with the like and they don't they don't expose all the end. everything about the API to use the
[49:47] API example is this is you know analogous to what we're seeing now which is then it makes it a dumb database
[49:53] right the and so they're not incentivized to do that so I think what we're seeing is there's three paths in
[49:58] for in front of you one if if you were a a consumer or like a business that's looking to buy software one is okay I
[50:05] take Salesforce and I either turn on agent force or build all my agents on
[50:11] top of it and then treat Salesforce as kind of the the just the back end I think to what we just talked about some
[50:18] of that will work but some of that will also not work because Salesforce doesn't want you to have want that to be you
[50:23] know to they don't want to be just the data in the background right um and so you know I think that that
[50:29] there will be mixed mixed results around that and I I don't have I'm not bullish on uh the incumbent software building
[50:34] great agents on top there's option two which is you just totally DIY it you have the most control in that situation
[50:41] um however I think to everything we just talked uh that's really hard, right? Like you have to rebuilding true
[50:47] enterprise software and I think for a startup building rebuilding a CRM much easier for rebuilding, you know, a CRM
[50:53] for a Fortune 500 business, it's it's a lot of business logic to capture and you're also trying to like
[50:59] do open heart surgery while like the patient is like alive, right? Or you know, whatever one you want to use the
[51:04] analogy. Well, hopefully they're alive, but yeah. Yeah. Yeah. Yes. Yes. Yes. Of course, if they're alive, but I mean you're like taking the engine out mid-flight, whatever you want to say as
[51:10] the analogy. Um that's that's really hard and you have to get the like practical realities of permissioning and
[51:16] collaboration and all that right. Then there's a third option and I think this is why we are continue to do what we do in investing in in AI software is
[51:23] because there is a reason that like you know agents can continue to be built the
[51:28] data can be sucked in and built in the background. A lot of what we're seeing right now is um things that are working
[51:34] alongside an SAP or a layer of visibility on top that is um enhancing
[51:39] the experience and allowing the business user to then run agents on top of the
[51:45] existing data they have um and not but also not like throw out all of the the
[51:51] logic they've had in the background. Um and then I think also create a new system of record like voice agents are
[51:56] collecting new data recordings are correcting collecting new data transcription ingestion of documents all
[52:02] of that documentation is pulling in and maybe you know one day these AI uh startups will replace the systems of
[52:08] record in the back end but they are doing so in like a systematic way of observing how the business is operating.
[52:15] I guess I guess to close this out though, Seema, you you sort of just touched on this. Where where are we
[52:20] really seeing the biggest opportunities for startups right now? I think look, a
[52:25] lot of this Yeah, what I was just saying, it's it's it's doing the things that the incumbents are not doing right
[52:31] now, which is um which is going from a layer of collection of data and into how
[52:38] do we take action on top of it, right? And so um take the CRM example, right?
[52:43] It's like I'm not just logging all of the like call information but then now I'm providing the intelligence back
[52:48] around okay how do I prioritize leads which uh accounts should we work on what have what has risk of churn flagging all
[52:55] of that and then like sending the outbound right and so and and and part of that is creating this agentic loop
[53:00] which is you now as the agent sends the outbound sees the response you're understanding okay a what works what
[53:08] didn't what how did people respond and then b you're also collecting like benchmark data view on like okay this
[53:15] type of response is most effective in these cases and in Asia we should be using this language you know type of
[53:21] opening versus in Europe etc that sort of stuff you're now agentically collecting all of that um and that's
[53:26] like an interesting data exhaust so I think that's another area and the third area I just would flag too is we talked about this like physical realities but
[53:32] the other part of physical realities is a lot of the vertical software that builds for the you know the physical
[53:38] world actually um and that is a really interesting interesting set of data
[53:43] that's not it's like hard to capture has been hard to capture historically. Um and you know you will have to continue
[53:50] to um pull together things that um can be cap you know agents have been able to
[53:57] operate on software but then also what humans are doing out in the field machines are doing out in the field and pulling that back in. So like
[54:02] construction, manufacturing, all of that. Well, the universal truth for enterprise software is the the most
[54:10] difficult thing to do that happens to be the dumbest is to attempt to just compete head-on with with an existing
[54:16] category. And and by head-on, I mean not just the same category, but doing it the
[54:22] same way. The biggest opportunity right now is always always to look at the
[54:29] existing uh sort of mental map of enterprise categories and be in between two
[54:35] established players because the thing that you know right now during a massive technology shift is the one thing that
[54:42] established players won't do is disturb their existing product line and go to
[54:48] market. So they absolutely will just be bolting AI on top of their existing
[54:53] product. They they won't be getting rid of it. They won't stop working on it. They won't do anything to to break it.
[55:00] They're just going to try to weather this technology storm by sort of power throughing it, powering powering through
[55:07] it. And so your opportunity in a startup is to just look at two big players who
[55:12] are bolting AI onto the side and exposing some existing API as an agent
[55:17] or whatever and just aim for the middle and do things in in the new way and the
[55:23] new way. And by not attacking head-on, you don't show up at every single customer and have them go, you know,
[55:29] well, you need to the do these 8,000 things before you even enter the door. Instead, you have a equally difficult
[55:36] question, but one you're in control of. It's which is why do you even exist?
[55:41] And and that but you that's your own question. You you don't have to answer to a a series of 20-year frameworks that
[55:50] a 20-year-old framework that got created to answer a bunch of questions that aren't even relevant anymore. And and
[55:55] the best example of this is is is HTTP and HTML. client server existed,
[56:03] but the reason that those took over was not because it did all the things that client server did. In fact, it did none
[56:09] of them, but it implemented that concept in an entirely new way. And so, the web
[56:15] exists in spite of the fact that legacy vendors had a trillion dollars invested
[56:20] on how client servers should work. Well, and I and I would say the other piece too, it's not just two between two legacy vendors, but I think now there's
[56:26] like a layer of translation between two different functions within an organization, too. Oh yeah. Yeah, for sure. Software has always sold to like oh I'm
[56:33] selling into just you know the sales team or the finance team but then there's like these handoffs and which is now the context right but on bills and
[56:40] deals and like that actually also presents an interesting opportunity. So the last question I have which is for Stephen is um so network effects is this
[56:50] thing we always talk about on the consumer side and it's a great you know source of defensibility. No enterprise
[56:55] software business as far as I can tell has successfully done you know implemented network effects but you could argue that is a good source of um
[57:04] durability over time right and I think Salesforce has tried this in in in in a couple ways in the past but do you think
[57:10] that like enterprise software will start entering the the uh the you know the
[57:16] field of network effects in terms of like okay we're going to have both buyers and sellers on our CRM and therefore be able to like mediate these
[57:22] transactions or like yeah I'm curious to get your take on that? Well, certainly network effects outside
[57:28] of a company are extremely difficult for a bunch of compliance and security reasons,
[57:34] but but the biggest network effect in enterprise software is inside of a company. And we're seeing that happen
[57:40] now with with just chat. like all of a sudden you're seeing the it's it's so
[57:46] incredible to be at this dynamic that that almost felt like the good old days when some very motivated person like
[57:53] most people who work in enterprises it turns out are not like super interested in making their job better they actually
[58:00] just want to go to work get paid and go home and they don't come to work every day going how can I make my how could I
[58:06] streamline my task they just want to not mess it up that is a lot of the world
[58:12] but There's a small set of people like those bankers at Goldman Sachs that were like, "How do I do more deals faster,
[58:18] better, more clever models?" And so they were using Excel when when the other
[58:23] bankers were using one 123. There's actually floating around on the internet is this old commercial for Excel, the
[58:29] launch this launch TV ad from the from the late 1990s where or sorry the late
[58:35] 1980s where the first Excel spreadsheets were being used and it's a person sitting there with this monstrous laptop
[58:41] that weighed like 12 pounds in an elevator trying to use it. I I'm laughing because of course they were
[58:46] trying to not run out of battery life in the in the elevator ride which was invariably the case. But all all of a
[58:52] sudden this crowded elevator of a bunch of people in in these 1980s ties and 1980s wearing glasses looking at the
[58:58] spreadsheet going, "What are you doing? How are you doing that?" and getting all excited. And fast forward to 2025 and
[59:07] that's exactly what happened with chat. Like, in fact, I had a friend at SAP
[59:12] that was was writing like a um a SAP white paper about something and and I I
[59:18] just asked them, "Tell me what questions you're trying to answer." And I did the prompt and sent them back a white paper.
[59:26] And I'm positive I kicked off some sort of viral loop, not technically a viral
[59:31] loop, but some sort of network effect viral loop inside of her team because
[59:37] like all of a sudden people are seeing how to make their job better and it's accessible to them and they're doing it.
[59:42] So I I think and to your point Tim like this idea of of a tool that enables two
[59:48] functions to talk together that couldn't before is golden. Like that's exactly
[59:54] like that's literally what enterprise software integration is except that's all manual brute force higher accenture
[1:00:01] kind of stuff. And so if you have products that bridge this and you know Figma did a bunch of this with design
[1:00:06] and product development. And so if you can develop software that leverages AI
[1:00:13] in order to bring together parts of an organization that don't normally communicate that's a whole that's a new
[1:00:19] category. And we've seen that with things like IT budgeting where IT and finance would end
[1:00:26] up with tools that ended up helping them both do forecasting and the cloud enabled that. And so I I think that
[1:00:32] that's that's a huge opportunity. Nice. Well, I think that's also an
[1:00:38] amazing note to end on. Uh thank you so much, Stephen, for for joining us here.
[1:00:43] Thanks, Seema. Yeah. And thank you. And thank you, Seema.
