---
title: "Hannah Foxwell - The Reinvention of the Dev Team - AI Native DevCon June 2026"
video_id: pyYKOLEnsZk
url: "https://www.youtube.com/watch?v=pyYKOLEnsZk"
channel: "AI Native Dev"
channel_id: UCg3pI4p6OKSFrDVZcwRIx8A
channel_url: "https://www.youtube.com/channel/UCg3pI4p6OKSFrDVZcwRIx8A"
publish_date: '2026-07-08T20:56:59-07:00'
upload_date: '2026-07-08T20:56:59-07:00'
category: Entertainment
duration: '35:22'
length_seconds: 2122
view_count: 181
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
  I don't need to tell you that AI has changed software development forever. You know this. Whether you're positive, negative or indifferent to this change, you can't deny that the past 2 years have radically changed the role of the software developer.
  
  Just a few years ago I would have advocated for The Balanced Team. A Product Manager, a Product Designer, an Engineering Manager and 4-8 Developers. It worked.
  
  18 months ago I was telling people that "I've never seen a dev team get to the end of their backlog, I don't see that happening". I've seen it now. Actually, I've seen it more than once.
  
  The balanced team as we knew it doesn't work any more.
  
  The seismic shift in software is only just getting started. I don't offer a proven strategy to navigate this change, we are sailing these turbulent waters together. What I propose is that we go back to fundamentals, refocus on outcomes and evaluate our options for evolving team composition.
  
  In this talk Hannah brings these options, what she's seen work, what she's ready to throw out, and most importantly, the things she will keep no matter what.

  If you liked the talk, listen to The AI Native Dev Podcast at https://www.youtube.com/playlist?list=PLISstAySqk7KNRW1vfsjTqJnm4lXXBgPe
notes: |
  Metadata + transcript fetch succeeded headless on first attempt (60s timeout),
  no retry needed. 268 segments. Light ASR cleanup: "Hannah Fox is" -> "Hannah
  Foxwell is" (self-introduction mangled by ASR). "Andrew Noon" left as transcribed
  and flagged ASR-uncertain -- could not confidently resolve to a known public figure;
  do not treat as a verified attribution.
---

## Transcript

[0:00] Hello? Hello.
[0:01] People are still coming in, but as as towards the end of the day, I want to make sure that we're thanking a couple of the other people who are in here as well.
[0:12] So can we get a big cheer for everyone on the sound? Woo!
[0:21] And down behind the camera. And we've got our lovely volunteer in the room.
[0:29] I didn't catch your name. You have to shout it to me, do you ness?
[0:38] All of the tech and volunteers here today have been absolutely fantastic. So yeah, big cheers for all of them. Right?
[0:44] One more big cheer for Hannah who is going to come onto the stage now. Hannah Foxwell, would you like to join us on the left?
[0:51] Well, am I on?
[0:54] Hannah Foxwell is an independent advisor, writer and creator of founder of creator, founder of AI.
[1:01] 1 minute, 1 second For the rest of us, creating accessible AI learning experiences for everyone, regardless of their role or background.
[1:08] 1 minute, 8 seconds And and you're going to be talking about the reinvention of AI for the dev team. No, no AI, no AI in this one.
[1:15] 1 minute, 15 seconds So yes, it's the end of the day. I'm stocking reading now. It's all good. Hi everyone.
[1:22] 1 minute, 22 seconds Thank you for coming towards the end of the day.
[1:25] 1 minute, 25 seconds I'm going to be talking about agentic software development, but I'm not going to be talking about the tools or technology.
[1:34] 1 minute, 34 seconds I'm going to be talking about what it means for our teams and how we organize ourselves with these new capabilities.
[1:42] 1 minute, 42 seconds So ever since I started working in tech, this has been the fixation of every manager or engineering leader I have ever worked with.
[1:52] 1 minute, 52 seconds How do we get more velocity from the developers in our organization? We even we even call it velocity.
[2:01] 2 minutes, 1 second We even track it in story points.
[2:03] 2 minutes, 3 seconds And I feel like right now, today, the velocity that we've been yearning for is here and it changes everything.
[2:13] 2 minutes, 13 seconds And for a lot of teams, we don't quite know what to do with it yet. We don't know. We don't know.
[2:19] 2 minutes, 19 seconds I've been through these transformations that have impacted our velocity.
[2:23] 2 minutes, 23 seconds I've been through cloud transformation, which meant we didn't have to wait weeks for a server to run our software.
[2:29] 2 minutes, 29 seconds I've been through DevOps transformation, which means that we automated the path to production.
[2:33] 2 minutes, 33 seconds We didn't go through week long test cycles and like every one of them, bought with it new organizational challenges, new patterns for success.
[2:43] 2 minutes, 43 seconds And so what I'm very, very interested in right now is what agentic software development does.
[2:49] 2 minutes, 49 seconds Now that we've unlocked that massive next step of velocity, we've even like we've even created words around it.
[2:57] 2 minutes, 57 seconds Like, like just a couple of years ago, you would have been on a stage and you would have been talking about developer experience, developer productivity.
[3:05] 3 minutes, 5 seconds There were whole conferences organized around it. I think that that dialog has kind of it's kind of quietened now.
[3:13] 3 minutes, 13 seconds It's like we've got the velocity that we've all been wanting, and now we have to figure out what to do with it.
[3:20] 3 minutes, 20 seconds You may have already seen this slide because Luke Marsden had it in his deck and I stole it from him. But this is this is Steve.
[3:30] 3 minutes, 30 seconds Sort of like levels of identity coding maturity.
[3:35] 3 minutes, 35 seconds And we like we start at the bottom with like a narrow ID agent and we get all the way down to level eight, which is like an agent orchestrator, something like a gas town, something where like it's pure identity and we're all on a journey.
[3:48] 3 minutes, 48 seconds And I want to just reassure everyone that if you're still over here at like level 2 or 3, that's absolutely fine and normal.
[3:58] 3 minutes, 58 seconds Like, I don't know many people who are operating at level eight, and I certainly don't know anybody who could say credibly that they're doing it safely.
[4:05] 4 minutes, 5 seconds So we are all on a journey, but I do think that it is worth keeping an eye on these things, because this is what the future could look like for all of us.
[4:16] 4 minutes, 16 seconds Earlier this year, Cursor published their blog post talking about the third era of software development.
[4:22] 4 minutes, 22 seconds And this is when the on their platform, on their coding platform, agentic task started to supersede the tab completes and accepts.
[4:33] 4 minutes, 33 seconds And so whether whether your team is doing it or not, this is a clear signal that this is the way that software is being written.
[4:40] 4 minutes, 40 seconds Now, these are these are the metrics that show us that on that platform, agentic software development is superseding type completes and other forms.
[4:50] 4 minutes, 50 seconds And so let's talk about what it means for our teams.
[4:52] 4 minutes, 52 seconds And so when I start to do thought experiments about and how to reason about this, I try to go back to basics.
[4:59] 4 minutes, 59 seconds I try to think about what things do I believe will be true, no matter how good the coding agents get.
[5:06] 5 minutes, 6 seconds And so these are my three anchors that I use to navigate this change. The first one we need to build something worth building.
[5:16] 5 minutes, 16 seconds The second, I believe speed requires safety. And the third one, and I hope there's no disagreement on this one. People matter.
[5:25] 5 minutes, 25 seconds So I'm going to start I'm going to get straight into it because like I believe that we always, always must pursue the outcome and not the and not the task.
[5:37] 5 minutes, 37 seconds We always must build something with building. We must be solving a problem. We must be clear on the problem that we're solving. The code is how we solve that problem.
[5:46] 5 minutes, 46 seconds It's not the what. And so when you think about organizations, the typical organization today, what you have is you have a load of users and they have a problem.
[5:57] 5 minutes, 57 seconds And then there's usually a person whose job it is to understand that problem and translate that into requirements, which are then delivered by developers using code.
[6:07] 6 minutes, 7 seconds The solution to that problem is shipped as a product, and the users will benefit from that. And if you do a good job, you can do this into a business.
[6:16] 6 minutes, 16 seconds And the way that teams structure themselves is that there are usually far, far, far too many user problems that any one team can solve.
[6:23] 6 minutes, 23 seconds And so you filter them, you filter the noise, and the product manager filters that noise and tries to get the maximum value out of the product that they can.
[6:33] 6 minutes, 33 seconds They make decisions about what to build and what not to build, and that doesn't change. But what has changed is the pace at which we can solve problems.
[6:40] 6 minutes, 40 seconds And so what I'm seeing is I'm seeing actually like the pace that we can address these problems in the development team,
[6:48] 6 minutes, 48 seconds creating what I call back pressure in product, the speed of decision making, the speed of analysis is actually not able to keep up with the pace of software development in a typical team.
[7:03] 7 minutes, 3 seconds And the right answer is not to just build more faster. Intuitive is a thing.
[7:09] 7 minutes, 9 seconds If you say yes to every idea and to every user request, your product will come bloated, you'll impact user experience, and eventually your product will actually suffer.
[7:21] 7 minutes, 21 seconds And so like saying yes and building everything isn't the right answer either.
[7:28] 7 minutes, 28 seconds But one thing is true today and is new for us as an industry, is that it is becoming increasingly cheap to test our ideas with real prototypes.
[7:41] 7 minutes, 41 seconds And previously, because I've sat on both sides of the fence, I've been in product and I've been in engineering, and so I've been on both sides of the negotiation of like, what do we build next?
[7:51] 7 minutes, 51 seconds And as a product person, it was really difficult to justify the investment in building a prototype when you had like a three year backlog.
[8:00] Like, are we going to test this idea with real code, or am I going to try and figure out how to test my ideas in other ways? But that is no longer true.
[8:07] 8 minutes, 7 seconds We can prototype and we can do it quickly and cheaply. So what does this new world look like?
[8:15] 8 minutes, 15 seconds We have to make sure that we make good, informed decisions about how to deliver the maximum value through the software that we're creating.
[8:23] 8 minutes, 23 seconds And so what I've seen is a few different manifestations of this. The Vibe coding product manager is for sure here.
[8:31] 8 minutes, 31 seconds That product manager is building prototypes themselves and their testing the ideas to make sure that the work that's funneling through to the dev team is, am I getting away from a Vive coding product manager in the back?
[8:42] 8 minutes, 42 seconds Yes, yes. So yeah.
[8:46] 8 minutes, 46 seconds So the work that flows through to the dev team is validated by a real working prototype. And that's a very powerful pattern that I'm seeing.
[8:54] 8 minutes, 54 seconds If your product manager isn't comfortable prototyping, then what you can do is you can you can move developers to be more front facing,
[9:02] 9 minutes, 2 seconds to be more exploratory, explorative, and to partner with your product team on validating that you're building the right thing before it goes
[9:11] 9 minutes, 11 seconds to the rest of the dev team that we're going to work on production that feature once it's proven to deliver value.
[9:17] 9 minutes, 17 seconds Another pattern that is becoming very, very widespread is the forward deployed engineer, now a forward deployed engineer isn't a sales engineer.
[9:27] 9 minutes, 27 seconds They're not a solution architect. They're an empowered engineer that sits side by side with the users.
[9:33] 9 minutes, 33 seconds And if they see a gap in the product, they are empowered to fix the product and deliver that value to that user.
[9:40] 9 minutes, 40 seconds So you're actually really, really, really reducing that feedback loop from user to product by embedding an engineer side by side with your users.
[9:49] 9 minutes, 49 seconds And it was only just a couple of weeks ago that there was announced from Google that they're now they're building a capability of forward deployed engineers to go and do this with their AI products.
[10:02] 10 minutes, 2 seconds Another thing that works particularly well for reducing that feedback loop between users and engineers is the idea of a product engineer.
[10:10] 10 minutes, 10 seconds And there's some fantastic writing by Incident.io 179 00:10:13,080 --> 00:10:17,000 IO on the role of product engineers, but these are engineers that don't need to ask permission of a product manager to go and improve the product.
[10:19] 10 minutes, 19 seconds And this pattern works incredibly well if you're building products for software developers, because you have that user empathy already, you're building for yourself.
[10:29] 10 minutes, 29 seconds You are the user persona. And so teams like incident, they're building products for software engineers. And so they have that empathy.
[10:36] 10 minutes, 36 seconds And so they are empowered to go and improve the product.
[10:41] 10 minutes, 41 seconds So when we talk about team design, like I work with, I work with a number of startups and one of the startups I work with, they hired your typical engineering team.
[10:53] 10 minutes, 53 seconds So they got some pre-seed funding and they hired like six, six engineers.
[10:56] 10 minutes, 56 seconds And what became apparent very, very quickly is they just ran out of well qualified work to deliver.
[11:04] 11 minutes, 4 seconds And I think we really need to challenge like what we consider a normal development team, because at the moment,
[11:12] 11 minutes, 12 seconds this normal development team of sort of 6 to 8 engineers and a single PM, it feels imbalanced. You end up with bottlenecks, especially around decision making.
[11:20] 11 minutes, 20 seconds And so what I've seen some folks do is experiment with different ratios, two developers to every product manager.
[11:28] 11 minutes, 28 seconds And one of the companies that I've seen experimenting with this is called NPM. So they're running this experiment at the moment.
[11:36] 11 minutes, 36 seconds That different ratio, the one that we're not used to to see whether or not that can unlock more value, putting more product people per developer on the team.
[11:46] 11 minutes, 46 seconds Earlier this year, Andrew Noon [ASR-uncertain] was speaking at Davos Summit and proposed that actually the typical dev team
[11:54] 11 minutes, 54 seconds might even look something like this two product people to a single developer, because the speed of decision making is such that a single developer can keep on top of a backlog driven by two product managers.
[12:07] 12 minutes, 7 seconds Who knows? Like, I don't know, I'm not up here for any of these.
[12:10] 12 minutes, 10 seconds I'm talking to you about what I'm seeing people experiment with to unlock the velocity that agent development gives them.
[12:20] 12 minutes, 20 seconds I also sat down with the CTO of a consultancy because I thought that would be really interesting across a broad
[12:28] 12 minutes, 28 seconds spectrum and lots of different development teams about how AI driven software development is impacting them.
[12:35] 12 minutes, 35 seconds And what was really interesting is actually like they're not reducing team size, but they are expecting far more outputs.
[12:44] 12 minutes, 44 seconds Only 2 or 3 of actually intentionally reduced team size because they feel like they had too many people.
[12:52] 12 minutes, 52 seconds And, you know, this is this is one sample.
[12:55] 12 minutes, 55 seconds And we can look at the news and we can see in the news all of these various rounds of layoffs the companies are doing. And everyone is sort of challenging themselves.
[13:03] 13 minutes, 3 seconds And I don't think it's necessarily about reducing headcount. It's just making sure you have people in the right places doing the right work.
[13:10] 13 minutes, 10 seconds And I think the dynamics of our teams have absolutely, fundamentally changed.
[13:16] 13 minutes, 16 seconds So I spent last year working with startups, and this year I was like, I've spent too much time helping other people be successful.
[13:26] 13 minutes, 26 seconds I want to have a go at it myself. And so I started to build a product. It's called it is a base image management platform.
[13:35] 13 minutes, 35 seconds So it's a platform that manages your container base images.
[13:38] 13 minutes, 38 seconds And the hypothesis of this product is that zero CV base images are becoming the new normal, and that most organizations,
[13:48] 13 minutes, 48 seconds at some point in the near future will transition from the container base images they're using today to a zero CV version. So while you do that.
[13:56] 13 minutes, 56 seconds Why not have a platform to automate it for you? So we are a two person team, a ratio of one developer to one product person.
[14:04] 14 minutes, 4 seconds I am wearing the product hat and I felt the new pain of this extra velocity in a very, very real way.
[14:15] 14 minutes, 15 seconds So we gave ourselves two weeks to build to build the sort of MVP, the first iteration of this product.
[14:22] 14 minutes, 22 seconds And on day one, we decided what we were going to build that week. And on day one we had finished by lunchtime.
[14:33] 14 minutes, 33 seconds And so it was like, oh, brilliant.
[14:35] 14 minutes, 35 seconds On day two, I was catching, I was catching a train to London, so I, I was, I was chatting to Stu and we were like deciding what we should, what we should build.
[14:45] 14 minutes, 45 seconds And I was on the train platform and I got a text saying, done 11 a.m., 11 a.m. and I love to think about that.
[14:53] 14 minutes, 53 seconds And I'm like, gosh, what could life look like if work just existed between 9 a.m. and 11 a.m.? And then I got the rest of my day free?
[15:00] Wouldn't that be fantastic?
[15:02] 15 minutes, 2 seconds But I think it's a common theme that I've heard across a few of the talks here is that actually this this unlocking of this velocity, it makes us more ambitious and we have to be more ambitious.
[15:13] 15 minutes, 13 seconds And so we had to relearn, like I had to completely throw out a lot of my product toolkit about ruthless prioritization, about slicing up features.
[15:23] 15 minutes, 23 seconds I had to think way, way, way ahead about what the or the end goal of this product was and how I wanted it all to work.
[15:30] 15 minutes, 30 seconds Instead of focusing on one thing, I had to think bigger. So. So that's what we did.
[15:37] 15 minutes, 37 seconds We gave ourselves two weeks to test an idea. We tested our idea at KubeCon.
[15:44] 15 minutes, 44 seconds The idea seemed to be very well received, and so we were able then to make an informed decision about, actually, we're going to we're going to invest more time in this product idea.
[15:51] 15 minutes, 51 seconds And so from my own kind of real lived experience, I feel so excited about this new era of software development, because you can test every idea and you can you can make more informed decisions.
[16:06] 16 minutes, 6 seconds Like, I haven't had to go and knock on the door of a VC and say, please give me money, because I've got a good idea. I've actually been able to build a thing and test that it's a good idea.
[16:14] 16 minutes, 14 seconds And so when I think about team design and I think about how we make sure that no matter how fast we get, we always build something with building, we always build something that has an impact.
[16:26] 16 minutes, 26 seconds Here are the things that I'm keeping. Here are the things that I'm trashing, and here are the things that I'm trying. So I'm keeping empowered product teams.
[16:33] 16 minutes, 33 seconds No one should have to ask permission to to help their users. Absolutely. Fast feedback with real users is your superpower.
[16:41] 16 minutes, 41 seconds You have to really understand the problem that you're solving.
[16:44] 16 minutes, 44 seconds And I think when everybody is empowered to build and everyone is empowered to build quickly, user experience and usability are going to be your differentiators.
[16:53] 16 minutes, 53 seconds So don't don't forget about those. I'm absolutely trashing the two pizza team and my six month roadmap.
[17:00] I was at a conference earlier this year and someone suggested that we start calling a team, which I really liked, like the teeny tiny tapas team, the small plates.
[17:11] 17 minutes, 11 seconds I like that a lot.
[17:12] 17 minutes, 12 seconds And I'm trying forward-deployed engineer model the empowered engineer that sits side by side with the customer.
[17:19] 17 minutes, 19 seconds Love that product engineers and I think that's a very powerful one.
[17:23] 17 minutes, 23 seconds If you're building dev tools, prototyping and testing your ideas quickly fail fast. If it's a bad idea.
[17:30] 17 minutes, 30 seconds And then smaller teams for sure.
[17:33] 17 minutes, 33 seconds Really thinking about the right ratio, developers to product people to keep that flow of ideas and value moving smoothly through your organization.
[17:45] 17 minutes, 45 seconds My next anchor is that speed requires safety, so we can go very, very quickly and we can break things.
[17:54] 17 minutes, 54 seconds But your users aren't going to thank you for that.
[17:57] 17 minutes, 57 seconds And so I think the the second pillar is, is about how we move quickly and do it safely.
[18:07] 18 minutes, 7 seconds The path to production is so, so important.
[18:12] 18 minutes, 12 seconds And I think the evolution of how we engineer our pipelines and our past production and the platforms that support them are going to be differentiating.
[18:21] 18 minutes, 21 seconds And if you have these capabilities already, you're going to be able to unlock a lot of value from agentic software development.
[18:27] 18 minutes, 27 seconds But what I've seen happen in a few places is that actually what was a kind of smooth process from idea into production
[18:36] 18 minutes, 36 seconds becomes a little bit of a car crash somewhere after the code is written, and before that code delivers value to users.
[18:44] 18 minutes, 44 seconds And so if there's any manual steps on that path to production for your software, you're going to end up with a pile up,
[18:51] 18 minutes, 51 seconds whether that be code reviews, whether that be your testing suite, you're going to end up with a bottleneck somewhere else.
[18:56] 18 minutes, 56 seconds And so investing in your path to production, your pipelines, your automation is so important to actually leveraging AI for software development.
[19:08] 19 minutes, 8 seconds It's a forever truth that like high confidence, requires testing.
[19:13] 19 minutes, 13 seconds And if you want high confidence quickly, you have to automate that.
[19:19] 19 minutes, 19 seconds One of the blog posts that I particularly like, and this was actually from last year, so things may have changed, was from AWS
[19:28] 19 minutes, 28 seconds about how they had to completely rethink their path to production, to be able to get the extra velocity, and to get the volume of code that the software developers we're delivering safely into production.
[19:40] 19 minutes, 40 seconds And I think if your organization hasn't started to think about that, started to map that path of reduction, look for those bottlenecks.
[19:48] 19 minutes, 48 seconds Think about investing time in optimizing it, then this is my sort of rice to you.
[19:53] 19 minutes, 53 seconds I think that problem might not might not be manifesting today, but I feel like it will eventually.
[20:00] And so getting your pipelines in order is super important.
[20:04] 20 minutes, 4 seconds There's really good news here is and that is that AI is fantastic at writing tests.
[20:09] 20 minutes, 9 seconds So if you have manual testing or slow testing on your path to production, then this is a really fantastic use case for using AI to improve your software development capability.
[20:22] 20 minutes, 22 seconds And there's a great case study for from JP Morgan that talks about how they are using AI to do continuous component testing,
[20:30] 20 minutes, 30 seconds making it safer to deliver a larger number of changes into production because you have that enhanced test coverage.
[20:38] 20 minutes, 38 seconds So again, when we talk about like we talk about your team of developers today, you might not need all of them working on features right now.
[20:47] 20 minutes, 47 seconds Today what you might want to do is split that team and have some folks focused on pipeline, some folks focused on test coverage, something that makes it safe to move quickly.
[21:00] I don't need to read out that quote.
[21:05] 21 minutes, 5 seconds So yeah, in my experience, the cost of data is always greater than day one to scale
[21:12] 21 minutes, 12 seconds and maintain an application that has real users is going to cost you a lot more in the long run than just getting version one of that application into the hands of users.
[21:23] 21 minutes, 23 seconds We don't we don't talk about it enough, really. Users also care about this stuff.
[21:30] 21 minutes, 30 seconds Like you're never going to get a feature request that comes in and says, like, don't be shipping any vulnerabilities, but they expect it like they expect it from you.
[21:40] 21 minutes, 40 seconds And reliability issues will make the news, especially if you're on a popular platform.
[21:46] 21 minutes, 46 seconds And so investing in reliability is is super important.
[21:51] 21 minutes, 51 seconds We must always, always balance velocity with reliability because our users may not care about us shipping 100 features every month.
[22:00] What they care about is you actually doing the thing that you said you were going to do and doing it reliably and safely.
[22:08] 22 minutes, 8 seconds Again, like very few customers will come knocking on your door and say, make sure you're secure. They expect it of you.
[22:16] 22 minutes, 16 seconds And so good security tends to be invisible. It's an absence of problems.
[22:24] 22 minutes, 24 seconds And what I have found is that, like good security is invisible. Bad security is an absolute reputation killer.
[22:34] 22 minutes, 34 seconds So these are areas where we actually want to be investing time.
[22:39] 22 minutes, 39 seconds And in the past, having to negotiate the time on the backlog to do that important work was always a trade off.
[22:48] 22 minutes, 48 seconds Do we build this feature the users are asking for, or do we do this important invisible work? Now, we don't necessarily have to make those trade offs.
[22:56] 22 minutes, 56 seconds We can do it all, or we should at least be trying to do it all.
[23:02] 23 minutes, 2 seconds Practices like progressive delivery that make it safe to deliver a large, a large amount of change into the hands of your users are super important.
[23:13] 23 minutes, 13 seconds So I'm talking about things like feature flags, so that you decouple feature delivery from the actual deployment of the software.
[23:20] 23 minutes, 20 seconds I'm talking about blue green deployments, where you can actually have a new release being used by a subset of your users.
[23:27] 23 minutes, 27 seconds Progressive delivery will make it much, much more safe for you to move quickly and deliver a lot more change to your users.
[23:34] 23 minutes, 34 seconds So if you haven't got those capabilities in your platform at the moment, now might be the moment that now might be the time to try it out.
[23:42] 23 minutes, 42 seconds I said that we always need to balance velocity and stability, and luckily we already have a language to reason about this.
[23:51] 23 minutes, 51 seconds So I will advocate for site reliability engineering forever.
[23:55] 23 minutes, 55 seconds Having SLIs — service level indicators that tell you whether your product is doing the right thing for its users objectives, about how often it has to work to meet your users needs and error budgets.
[24:07] 24 minutes, 7 seconds The amount of kind of forgivable failure in in the system.
[24:11] 24 minutes, 11 seconds By getting these things in place, by measuring them continuously, you can have a better dialog about whether or not you need
[24:18] 24 minutes, 18 seconds to intentionally slow down the amount of change that's getting shipped to your users, so that you can make sure that you're always meeting their expectations on reliability.
[24:29] 24 minutes, 29 seconds And so when I think about the future of organizational design, I'm seeing a future where actually platform engineering and SRE
[24:37] 24 minutes, 37 seconds are even more important than they were, because they unlock the velocity of the development teams who are serving users, the development teams who are building building features.
[24:49] 24 minutes, 49 seconds So platform teams who make it safe to move quickly using automation, and SRE teams that can act as internal consultants,
[24:58] 24 minutes, 58 seconds helping teams invest in reliability so that you can deliver with this velocity.
[25:03] 25 minutes, 3 seconds But you don't do it at the expense of your availability and your performance of the product.
[25:10] 25 minutes, 10 seconds So I'm going to talk another another little bit about about BIM and my experience of my two person team building our first product.
[25:18] 25 minutes, 18 seconds So like I said, we had the first version of the product ready in two weeks. So what did we do after that?
[25:25] 25 minutes, 25 seconds I can honestly tell you, it looks a hell of a lot like platform engineering. Reliability engineering, like there was not a lot of feature development.
[25:33] 25 minutes, 33 seconds It was about scalability, security, and doing and doing it right.
[25:38] 25 minutes, 38 seconds So while it was cheap to actually build like a functioning application, what then took the time was making sure that application was ready to scale and that it was safe to do so.
[25:50] 25 minutes, 50 seconds So this is my kind of like my own experience of where the time went. It wasn't in feature delivery at all.
[25:58] 25 minutes, 58 seconds It was in making sure that that that platform was robust enough to be used by real enterprise customers.
[26:05] 26 minutes, 5 seconds And so when we talk about our organization design and the humans, like, I can see a world where actually at the moment I find platform teams, SRE,
[26:16] 26 minutes, 16 seconds team security teams, they are massively outnumbered by the number of developers who are focused on features. I can see that balance shifting.
[26:24] 26 minutes, 24 seconds I can see an increased and increased importance for the platform and the SRE capabilities, because they are the people who unlock the value of those feature aligned teams.
[26:37] 26 minutes, 37 seconds So what am I keeping? What am I trashing and what am I trying?
[26:41] 26 minutes, 41 seconds I'm definitely keeping SRE practices, progressive delivery, and internal platforms. These are things that make it safe.
[26:47] 26 minutes, 47 seconds I am trashing anything manual on my path to production.
[26:53] 26 minutes, 53 seconds That doesn't mean we can't do manual testing, it just can't be on the critical path and use things like feature flags to make sure that it is safe to ship something buggy and that your users won't notice.
[27:04] 27 minutes, 4 seconds And I'm absolutely going to be addressing tech debt using AI.
[27:09] 27 minutes, 9 seconds I'm going to be trying to improve my test coverage, make it make it really easy to to spot issues.
[27:15] 27 minutes, 15 seconds I'm using AI to accelerate my migrations, and my refactor is and I'm definitely looking at bringing back the SRE team as internal consultants that can help teams invest in reliability.
[27:28] 27 minutes, 28 seconds Now, as I wrap up, my third anchor is is actually probably the most important.
[27:35] 27 minutes, 35 seconds And it's that people matter.
[27:38] 27 minutes, 38 seconds And so as we reinvent our teams for this new age of software development, it has to be done with people in mind.
[27:47] 27 minutes, 47 seconds We have to create jobs that are worth doing.
[27:50] 27 minutes, 50 seconds And the first thing that I'm going to controversially say is that reviewing code that was written by a I love lines of it, it's not fun.
[27:59] 27 minutes, 59 seconds It is not a very fun job.
[28:01] 28 minutes, 1 second And so I've got a very keen eye on the organizations that are trying new things, like instead of having a massive pile up of of code reviews, what are they doing instead?
[28:12] 28 minutes, 12 seconds There's a couple there's a couple of organizations that have publicly said that they're not doing mandatory code reviews.
[28:19] 28 minutes, 19 seconds That doesn't mean that they don't do code reviews.
[28:21] 28 minutes, 21 seconds It just means that they're not doing them in a mandatory way on every single, every single change.
[28:29] 28 minutes, 29 seconds Some of these organizations are actually shifting left on the peer review.
[28:33] 28 minutes, 33 seconds So previously a code review would actually, you know, go to a senior engineer who would spot issues with it.
[28:41] 28 minutes, 41 seconds When I was shifting left to maybe at the point where you write the spec for the agent, you're shifting left that decision making and that oversight and that peer review to make sure that you're building the right thing.
[28:52] 28 minutes, 52 seconds I really like this quote by Joseph Russia.
[28:56] 28 minutes, 56 seconds The mistake would be to treat unread code as a failure of discipline, rather than a signal that the discipline itself must change. And I don't again, I don't have answers here.
[29:05] 29 minutes, 5 seconds I just know that asking engineers to review thousands and thousands of lines of AI authored code is going to create a lot of very unhappy engineers.
[29:14] 29 minutes, 14 seconds And so we have to figure out another way that we can build quality and assurance into our process without creating unsustainable work.
[29:25] 29 minutes, 25 seconds Another thing that I know for sure people are not going to want to do is to support a fragile service.
[29:32] 29 minutes, 32 seconds An agent cannot hold the page in, and so this is one of like the fungible sort of things that I believe, like engineering teams need to navigate.
[29:41] 29 minutes, 41 seconds And it's who is owning the service in production because on call is still a thing and you have to have a sustainable on-call rota.
[29:51] 29 minutes, 51 seconds You can't have a single engineer being on-call all of the time. That's not fair. That's not right. That's not sustainable.
[29:58] 29 minutes, 58 seconds And so when I think about how small we might be able to make our teams, this is the thing that I keep coming back to. It's like, well what?
[30:04] 30 minutes, 4 seconds Like what is the most the smallest team that you can have a sustainable on-call rota.
[30:09] 30 minutes, 9 seconds And I think it's for people for people capable of supporting that, that product in production, because you always have a primary
[30:17] 30 minutes, 17 seconds and you have a secondary and you can't be on-call more than 50% of the time. I know a lot of people who wouldn't even want to be on-call 50% of the time.
[30:25] 30 minutes, 25 seconds So like the minimum viable human like is going to be dictated by some of these roles.
[30:34] 30 minutes, 34 seconds I think I said at the beginning, like when we were building, we absolutely like we ran out of work on day one.
[30:42] 30 minutes, 42 seconds We ran out of work on day two.
[30:43] 30 minutes, 43 seconds I think the thing that I would urge folks to challenge is a lot of the ceremony that we surround our development teams with might not be adding value, or it might not be adding value anymore.
[30:57] 30 minutes, 57 seconds In some cases, it might be slowing us down.
[30:59] 30 minutes, 59 seconds The sprint planning that only happens every two weeks is that the right pace of decision making that we need? Do I have any do?
[31:09] 31 minutes, 9 seconds Do I have any managers in the room? Yes, managers.
[31:14] 31 minutes, 14 seconds It's a tough time to be a manager of software engineering teams, because we don't really know what the role of software engineering is evolving into.
[31:24] 31 minutes, 24 seconds But one thing that I'm going to urge you all to do is to go and watch a talk by Sophie Weston from Qcon last year, where she talked about the broken comb
[31:33] 31 minutes, 33 seconds instead of the T shaped folks develop people who have a broad understanding and a few various areas of depth.
[31:43] 31 minutes, 43 seconds And when you're doing career. Coaching with folks, think about the skills that they may need that were that will help them think about what I've talked about.
[31:53] 31 minutes, 53 seconds It's like, do you have engineers who are going to lean to more towards product, or are you going to have engineers who are going to lean more towards platform?
[32:01] 32 minutes, 1 second And can you help people develop those skills that we really need right now?
[32:05] 32 minutes, 5 seconds I am almost out of time, but I think one of the things that I like to do, I like to, I like to, I like to imagine the team that I would build in the future.
[32:14] 32 minutes, 14 seconds And the one thing that is absolutely critical for me right now is user empathy.
[32:21] 32 minutes, 21 seconds If you hire someone like and they can't sit down with a user, understand their problem and design a solution that solves that problem, then that person is going to become a bottleneck.
[32:33] 32 minutes, 33 seconds They're going to need to spoon fed requirements, and that has become normal in our industry. And I think that's a practice that needs to end.
[32:39] 32 minutes, 39 seconds And so you'll be very relieved to hear this as my final slide. I've been trying to be subtle. Oh, no.
[32:49] 32 minutes, 49 seconds People matter. Like I want to make sure that every engineer has a sustainable on-call rota.
[32:54] 32 minutes, 54 seconds I want to make sure that we have a language to discuss, like our error budgets and our availability targets, and invest appropriately.
[33:02] 33 minutes, 2 seconds And I want to do realistic career planning for the skills that we need today, not the skills that we needed yesterday. I am trashing heavy planning processes.
[33:12] 33 minutes, 12 seconds Two week sprints are absolutely too long right now, and mandatory code reviews feels like an unsustainable practice that's going to need to be replaced with some other ways of assuring quality.
[33:24] 33 minutes, 24 seconds I'm definitely shifting left on peer review using spec driven development, and I'm going to encourage all of you in this room, and especially the managers,
[33:34] 33 minutes, 34 seconds to think about how we create people who are less T-shaped and more of a broken comb, people with a diverse area, diverse areas of depth, because those are the sort of people who are going to thrive in this new age.
[33:48] 33 minutes, 48 seconds We are all on a journey and we do not know where we're heading, and I find it exciting, but it can also be daunting.
[33:56] 33 minutes, 56 seconds And so as you leave here, hopefully I've given you some ideas to experiment with or to help you address some of the new challenges.
[34:05] 34 minutes, 5 seconds I would just urge all of you to experiment with empathy because it is not an easy thing to change, to change your discipline so fundamentally and at such speed.
[34:19] 34 minutes, 19 seconds So yes, we do need to try new things. We need to share our learning, but do it with people. Don't do it to them.
[34:27] 34 minutes, 27 seconds And so here are the things that I'm keeping.
[34:32] 34 minutes, 32 seconds No matter what, no matter how good agents become, I'm always going to build an organization that focuses on the user. Build something worth building.
[34:40] 34 minutes, 40 seconds Solve a real problem. I'm going to be investing in ways that we can move safely with speed.
[34:47] 34 minutes, 47 seconds And I'm going to always, always focus on the people because people matter and we need to create teams that are joyful to work in and careers that are worth pursuing.
[34:59] 34 minutes, 59 seconds So that's me. I'm Hannah. Come and find me for questions over a beer. I will. Release you now.
[35:08] 35 minutes, 8 seconds Thank you. Thank you for.
