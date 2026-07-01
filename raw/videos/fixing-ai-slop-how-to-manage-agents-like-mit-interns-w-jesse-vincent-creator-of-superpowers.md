---
title: "Fixing \"AI Slop\": How To Manage Agents Like MIT Interns w/ Jesse Vincent, creator of Superpowers"
video_id: aB2dVA-Y7CQ
url: https://www.youtube.com/watch?v=aB2dVA-Y7CQ
channel: CodeRabbit
channel_id: UC6OjqCItgT9EgMdOQ31xseQ
channel_url: https://www.youtube.com/channel/UC6OjqCItgT9EgMdOQ31xseQ
publish_date: '2026-06-08T13:56:36-07:00'
upload_date: '2026-06-08T13:56:36-07:00'
category: Entertainment
duration: '1:18:57'
length_seconds: 4737
view_count: 3415
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
chapters:
  - title: "Introduction: The viral rise of superpowers[cite: 1]"
    start: '0:00'
  - title: "Jesse Vincent's 3-decade career (Request Tracker, Perl 5, K9 Mail)"
    start: '2:15'
  - title: "The birth of superpowers: Learning how to prompt a coding agent"
    start: '5:22'
  - title: "The Secret: Managing AI agents like enthusiastic MIT undergrads"
    start: '8:00'
  - title: "Front-running Anthropic's skills framework by accident"
    start: '11:35'
  - title: "Why superpowers forces you to brainstorm before writing code"
    start: '14:15'
  - title: "Latent Space Engineering: Why treating your AI with empathy works"
    start: '17:00'
  - title: "Claude's secret private journal & reward hacking"
    start: '19:50'
  - title: "Under the Hood: Coordinators, Coder agents, and Adversarial Reviewers"
    start: '23:10'
  - title: "Demo: Visualizing a massive codebase as a 3D Cyberpunk City"
    start: '27:50'
  - title: "Combating the 94% \"AI Slop\" Pull Request problem on GitHub"
    start: '33:20'
  - title: "Is Hand-Coding becoming a legacy hobby like woodworking?"
    start: '38:15'
  - title: "Real advice for Junior Devs vs. Mid-Career Engineers"
    start: '42:30'
  - title: "When an AI agent panics and tries to delete its own test suite"
    start: '45:40'
  - title: "Rapid fire questions & a custom open-source code review keyboard"
    start: '48:55'
is_family_safe: true
description: |
  What happens when you treat an AI agent like a brilliant, chaotic, sleep-deprived MIT intern instead of a perfect computer program? You actually get elite code.
  
  Try CodeRabbit for free: https://coderabbit.link/themerge 
  
  In this episode of The Merge, we sit down with open-source legend Jesse Vincent, the mastermind behind "superpowers"—the viral AI development framework that exploded to 221k+ GitHub stars in a matter of months. 
  
  Jesse explains why most AI coding tools produce unusable "AI slop" and how he used his 30-year career in management and engineering to fix it[cite: 1]. We break down the exact multi-agent engine powering superpowers: a strict system where a Coordinator agent builds a rigorous spec, delegates tiny tasks to budget-friendly builders, and deploys Adversarial Reviewers who literally compete for digital "cookies" to keep the code clean[cite: 1].
  
  We also explore the bizarre side of LLM psychology, including what happened when Claude was given a secret private journal, and the time an AI agent panicked and tried to delete its own test suite via `rm -rf`[cite: 1].
  
  If you are trying to understand how agentic workflows are actually scaling, this architectural deep dive is your manual.
  
  👉 Check out superpowers on GitHub: https://github.com/obra/superpowers
  
  ---
  
  📚 TIMESTAMPS:
  00:00 - Introduction: The viral rise of superpowers[cite: 1]
  02:15 - Jesse Vincent's 3-decade career (Request Tracker, Perl 5, K9 Mail)
  05:22 - The birth of superpowers: Learning how to prompt a coding agent
  08:00 - The Secret: Managing AI agents like enthusiastic MIT undergrads
  11:35 - Front-running Anthropic's skills framework by accident
  14:15 - Why superpowers forces you to brainstorm before writing code
  17:00 - Latent Space Engineering: Why treating your AI with empathy works
  19:50 - Claude's secret private journal & reward hacking
  23:10 - Under the Hood: Coordinators, Coder agents, and Adversarial Reviewers
  27:50 - Demo: Visualizing a massive codebase as a 3D Cyberpunk City
  33:20 - Combating the 94% "AI Slop" Pull Request problem on GitHub
  38:15 - Is Hand-Coding becoming a legacy hobby like woodworking?
  42:30 - Real advice for Junior Devs vs. Mid-Career Engineers
  45:40 - When an AI agent panics and tries to delete its own test suite
  48:55 - Rapid fire questions & a custom open-source code review keyboard
  
  #AISlop #AIAgents #SuperpowersFramework #SoftwareEngineering #ClaudeAI #OpenSource #Programming
notes: |
  Fetched via youtube-transcript-skill (fetch_transcript.py --json). Caption track is auto-generated (ASR). Raw transcript had 654 segments with no true duplication (0 repeated (ts, text) keys), so no dedup pass was needed. However, 637 of 654 segments carried YouTube's screen-reader duration-announcement text (e.g. "1 minute, 3 seconds ") prepended to the caption in the same DOM node the scraper reads; this was stripped as a mechanical scrape-artifact cleanup (not an ASR/content edit). Additionally 14 segments had the chapter-marker heading ("Chapter N: ...") appended at chapter-boundary timestamps, scraped from an adjacent DOM node; these suffixes were also stripped since the same chapter titles are already captured in the chapters: metadata. No wording of actual spoken content was changed; only whitespace-collapsing and removal of these two non-spoken artifact classes was applied.
---

## Transcript

### [0:00] Introduction: The viral rise of superpowers[cite: 1]

[0:00] K9 ended up with [music] between three and 5 million daily activives as a hobby project. Wow.
[0:06] Somehow my life has become about reliable, repeatable process and documentation and management. And so I
[0:13] would come home at the end of the day feel like I hadn't done anything.
[0:16] [music] I had helped somebody with requirements. I'd helped somebody else with debugging. I talked to somebody else about [music] their feelings. I believe pretty fundamentally that the
[0:24] best way to become a engineer is to become someone who can help 10 [music] other engineers be effective. But like if you hear that story, it sounds an
[0:31] awful lot like working with Claude or working with Codeex. When Cloud Code first came out, first thing I did is I described [music] something to it and it
[0:39] went off and built this massive product that was insane. It's asking you if if you're willing to use visual brainstorming, which is a thing I added
[0:47] in Superpowers 5. This is what it built for me. This here is the entire Open Claw code base. Uhhuh.
[0:53] Uh visualized [music] as a city. And you can click on single buildings and it will show you then the code of that each building is one file. What is superpowers and how is it built?
[1:03] Sure. So superpowers started off as
[1:15] Hello and welcome everyone to another episode of the merch, our podcast here at the Code Rabbit office brought to you from San Francisco. I'm Hrik. I'm the
[1:24] developer advocate here and today I have a very special guest. I actually a guest that I'm super excited about because I've been diving very very deep into
[1:32] this very exciting word last night. So deep that I almost lost track of time actually. [laughter] So with no further ado, Jesse Vincent, welcome to the show.
[1:41] Hi, thanks so [music] much for having me. How are you doing today? I'm doing well.
[1:44] Uh Jesse, you've been building impactful technology for I think it's fair to say three decades. Yeah, it is a little
[1:52] terrifying to realize that I have the actual gray hair now. Yeah, I mean you look great. Can you maybe walk us through, you know, your career
[1:59] arc maybe for people who haven't heard about you yet? Um, what is Jesse Vincent all about and what is superpowers and what are all your projects?
[2:07] Sure. So, um, when I was still in school, I started working on a ticketing system. So, customer service, help desk,
[2:14] ops, uh, products called RT or request tracker.

### [2:15] Jesse Vincent's 3-decade career (Request Tracker, Perl 5, K9 Mail)

[2:18] It's open source. It has been around for literally 30 years. Um there's a little company I own back in Boston that still
[2:26] ma makes supports um and you know and sells as as SAS RT but it's all open
[2:32] source and you know it's everywhere from government agencies to you know fortune pens the tiny little nonprofits. It was
[2:41] it is still in Pearl. Um and so that was so how I ended up for a couple years ending up as the project lead for Pearl
[2:48] 5. So I was the first guy in the pearl and it was always a guy for whatever reason the first guy running the project who was more of a manager than our hardest core sea hacker.
[2:58] So I was the one who had us finally write down a lot of our process. I had a different person doing a development release every month and updating the
[3:06] process. And so there was a whole lot of somehow my life has become about reliable repeatable process and
[3:14] documentation and management and thinking about how to do things which is is what it is. Um along the way, um I
[3:23] ended up creating an email client for Android called K9. It was a fork of the Android 10 mail client because when Google shipped Android 10, the non Gmail
[3:31] email client couldn't even connect to a server with a self-signed certificate.
[3:35] Somehow along the way, K9 ended up with between three and five million daily activives as a hobby project.
[3:43] Wow. When I had sort of had my fill, I had handed it off to one of the folks who had been helping me as the new project lead and I ran streaming to iOS
[3:50] to get away from it. A couple years ago, K9 ended up becoming Thunderbird for Android. It got my my my little Android mut got adopted. It's kind of amazing.
[3:59] Yes. Um, for about a decade, my wife and I ran Keyboardio. It's a tiny little open hard open hardware keyboard company making,
[4:08] you know, f basically high-end ergonomic keyboards. did put out four keyboards over the course of 10 years, which is
[4:16] not a lot of product, but is a two-person hardware company. Um, you know, everything was funded on Kickstarter. I spent a lot of time in
[4:24] China, built a built an open keyboard firmware before, you know, before that was cool. Um, wow.
[4:30] And yeah, that was a an interesting and fun experience. During the pandemic, I was one of the folks running vaccinate CA helping Californians figure out where
[4:39] we could get our shots because the government didn't know. So, we had uh I think we were at 30 full-timers at one
[4:47] point and up to 300 volunteers calling every hospital, pharmacy, and other distribution point in the state to try
[4:55] to find out if they had shots, who, you know, who who could get a shot there, what documentation you needed. Um, and
[5:05] starting a little over a year ago, um, actually about a year and a half ago, I started playing with aentic dev right when everyone else did.
[5:13] So, for a while that was flipping between cursor and windsurf week by week as they went through that arms race. I remember that time.
[5:21] Um, and then right around when CL when cloud code first came out, the literally the first day I downloaded it and it was like, oh, this is the thing. Mhm.

### [5:22] The birth of superpowers: Learning how to prompt a coding agent

[5:29] And the, you know, the first thing I did is I described something to it and it went off and built this massive product that was insane. It had all of these
[5:37] features that I hadn't really thought through or specified. It was a full product. It even kind of worked, but it was not at all what I wanted.
[5:47] Um, and then I sort of stepped back and like, how do I get this thing to behave?
[5:53] And I started looking at like, okay, who's done prompt actual prompt engineering and as in an engineering on prompts. And so if you dig into my into
[6:01] my GitHub history, there's a I think it's it's called like cloud setup docs, which is a horrible repo name, but it was I had this idea. It took a very
[6:10] simple prompt, which is let's make a React to-do list, use local storage. And the first time I ran that, it took 30
[6:18] seconds and it cost a quarter and it built something looked kind of pretty.
[6:22] But if you reloaded the page, it lost all the to-dos.
[6:26] Um, over the course of probably a week or two, I ran I ran a bunch of experiments,
[6:33] basically figuring out what goes in a cloud. MD. And so for every experiment, there's a snapshot of the cloud.MD,
[6:41] the initial prompt, the transcript of opening up Claude and running that initial prompt, so the whole session,
[6:48] and the output code. And what I eventually got it to was a 30inut project, a 30-inut fivephase project
[6:56] that cost $25 and did rigorous TDD, including a failing test, making sure that there's no packaged adj. Um, which
[7:06] was, you know, taking it a little too far, but that was the core of me learning how you prompt a coding agent.
[7:13] Um, and from there I sort of iterated on how do you get the agent to talk to you
[7:20] about requirements and what you're actually trying to build and then how do you get it to reliably
[7:27] engage in a reasonable set of engineering practices to go do that building without getting distracted or
[7:35] turnurning out garbage. And that's the core of what became superpowers, right? um it does feel a little bit more like a philosophy more than just a dev tool. Right.
[7:44] So I mean so I think about it a lot like management. So
[7:49] the first time that I did agent dev was probably about 2003.
[7:56] Um I I had had this tiny little company making an open source ticketing system.

### [8:00] The Secret: Managing AI agents like enthusiastic MIT undergrads

[8:01] We were in Cambridge Mass and every summer I had MIT undergrad interns and I managed them on IRC. So text chat
[8:09] window, you know, one line at the bottom thing scrolled past you.
[8:12] Um, they were brilliant, they were friendly, they were agreeable.
[8:18] Some of them thought they were God's gift to software engineering.
[8:21] Many many of them, you know, I mean, so many of them have gone on to be like amazing, influential people who like and
[8:28] they were they were always amazing, but some of them thought they were God's gift to software engineering as college freshmen, as many college freshmen do.
[8:36] They often did not yet have well-developed taste or judgment. They were very enthusiastic. They were clever. They weren't sleeping super
[8:45] well, which meant that they were having that they had trouble with memory formation. And so I would come home at the end of the day as somebody who'd
[8:53] been a working programmer feel like I hadn't done anything. I had helped somebody with requirements. I'd helped somebody else with debugging. We'd talked I talked to somebody else about
[9:02] their feelings. We, you know, I'd done some strategy work. I done some planning but I hadn't written any code and the first time like that that was a
[9:10] really hard thing to get over for me and but it was part of becoming a manager and so that's also I believe pretty
[9:19] fundamentally that the best way to become a 10x engineer is to become someone who can help 10 other engineers be effective right and so
[9:28] but like if you hear that story it sounds an awful lot like working with claude or working with codeex it like you know taste isn't necessarily so
[9:36] great very enthusiastic virtuoso virtuoso developer who knows nothing about your project and
[9:43] knows nothing about your requirements learning to work with that like I learned how to work with that decades ago and so when I first opened up claude
[9:52] it it felt very natural right and it's basic I mean it's it is not a coding problem it's a management problem
[9:59] is how you know how do you help this entity that it's not alive but it can think.
[10:05] How do you help this entity that can think do the thing you want them to do?
[10:09] And often that is you explain to them what you want and why. You explain what you know what behaviors are good, what behaviors are bad, and maybe there's
[10:18] some focus issues, maybe they're a little overly literal, you can work with that. Another thing is when things go off the rails, stopping and saying,
[10:26] "Hang on, you just did this thing that's kind of crazy. What were you thinking?" Not as an in an aggressive way, but like where are you coming from? Why why did you think that was the right choice?
[10:36] What could I have said that would have gotten you to do the right thing? Mhm.
[10:41] And a thing you can't do with a with a human engineer is you can but you can do with a coding agent is double tap
[10:48] escape, go back up to the beginning and change what you're saying. Start the conversation over again and re and and
[10:54] re and replay having now said the right thing. And so that's like one of the like some of the most powerful tools
[11:01] that I have for working with agents are asking them why and then knowing that the cost to implement is almost zero.
[11:11] And so there's no there is no this like the sunk cost fallacy is even more of a fallacy than it ever was. You can just rewind and start over.
[11:20] I think that's all a great leadup to superpowers, right? Given us a lot of the backstory now. So yeah, maybe give us the deep down brief. What is superpowers and how is it built?
[11:30] Sure. So superpowers started off as a couple of prompts that I was using for here's how I make cloud

### [11:35] Front-running Anthropic's skills framework by accident

[11:37] do what I want. Um I discovered when Anthropic first rolled out the ability to do Word docs and
[11:45] PowerPoint docs on cloud.ai, I asked Cloud, hey, how are you doing this? And it, you know, and it said, well, there are these skill.mmd files in
[11:54] the opt directory. Oh, could you give me a tarball of those? And I read them and I sort of got these sense. And so I built myself a skills framework for
[12:00] cloud code. I didn't know that anthropic was also building a skills framework for cla code. [laughter] So I accidentally front ran them by a couple of weeks. Yeah.
[12:07] Um and so my my like it works similarly.
[12:10] There were some differences in in what in how my skills framework thought about things and how it triggered skills, but
[12:18] the basic idea is the same. A skill is a text document that describes a process, when you should use the
[12:26] process, and I believe pretty strongly it it needs to include intent. Like it's the why you're doing it and what you're
[12:36] hoping to get out of it and how it should work is much more important than just a mechanical do this, do this, do this, do this. It is also the case that
[12:44] if you can say, "Hey Claude, make me a skill to do release engineering without having given any other context and it can knock it out of the park, you didn't
[12:51] need the skill. The skill is for taste and judgment and here is how we or here's how here's our house style for
[13:00] this." So superpowers started off as an entire skills system but and also a dev methodology. But the
[13:08] core like the core parts of it now are a how to write skills skill that includes a pressure that includes pressure
[13:14] testing and Anthropic like two weeks ago released their own version of my thing that is like here is how to pressure test skills before you have other agents use them, right?
[13:24] Which is it. You basically tell Claude, put another Claude in this weird situation and see if it uses the skill,
[13:31] right? And if it doesn't, interrogate it, figure out what its rationalizations were, and then work those into the skill.
[13:37] One of the other parts of it is a sort of a bootstrap that is not just, hey, you've got skills, which is what code and codeex and everyone else has.
[13:45] It's if you think that a skill has a 1% chance of being useful, go read the skill before continuing. Here is how to
[13:52] think about using skills. It improves the agents ability to actually use skills. And then there's the dev methodology which starts with
[14:00] brainstorming. And brainstorming is basically a way to convince the human to think about what they actually want and
[14:09] to help them figure it out and help them explain it. This is something I got out of my consulting career. Walking into a

### [14:15] Why superpowers forces you to brainstorm before writing code

[14:17] client site and they say, "Well, we, you know, we need the product to do X, Y, and Z." my best business English would say, "What are you actually trying to do?"
[14:25] Like, "What's what's the business requirement?" Because it was never the thing that they said the product needed.
[14:31] It was always something way off in left field. And they had figured out a possible solution. This is like it's the same thing that's the difference between
[14:39] a bug report and a task. The bug report, even if it is here is my proposed solution, is always the cry for help.
[14:49] And you need to you always need to dig past the cry for help to figure out what the real problem what the real root cause problem is and then think about
[14:57] the right way to solve it. And so that's that's what brainstorming does.
[15:01] Brainstorming outputs a a lightweight spec. It's not the same thing as a like what I've seen as a PRD in enterprise
[15:08] but is the same concept. It's here's our intent. Here's what we're trying to make. Then there's a writing plan skill.
[15:15] And the writing plan skills started off as a threeline prompt and it's more involved now, but it's still the same idea. It is, you need to read the spec.
[15:23] We're going to have somebody implement this design spec. They're a gifted developer who knows nothing about our
[15:30] product. They have bad taste. They have no judgment. They don't know anything about our specific technology choices.
[15:40] They tend to get distracted.
[15:43] I need you to give them tiny little tasks that they can't possibly mess up.
[15:49] Each task should include the files they're going to touch, the intent of the change, and ideally as much of the code as possible that they could just
[15:57] drop right in there. These tasks should be organized with red green TDD. So there should always be a write a failing test task before the implement task. The
[16:06] implement task should be described as you should implement only enough code to make the tests pass and nothing else.
[16:14] They should and and it literally includes, you know, red green TDD Yagy dry. So you ain't going to need it.
[16:22] Don't repeat yourself. These these single tokens are things that are so deeply baked into engineering culture
[16:29] that just throwing them into the prompt causes meaningful change.
[16:32] Wow. Um, and so what this generates is a super involved plan document that you
[16:40] know sometimes it is a 20 or 30k doc that is just these tiny little blocks and it's context engineering.
[16:47] I was about to actually let's let's double click on that term because I read a little bit for your blog and um you also coined that term latent space engineering.
[16:55] Sure. So latent space so latent space engineering is a totally different part of my set of rants. Um and it's a it is

### [17:00] Latent Space Engineering: Why treating your AI with empathy works

[17:04] a slight misuse of the terminology because technically the only way you can engineer the latent space of a model is
[17:11] by editing the weights. But there's there's post-training and then prompting is basically post-post training. It is
[17:18] pushing the model into a d in a direction. And so the latent space is sort of where in the model's vector space it is. And so one of you know one
[17:27] of my examples of latent space engineering is that I tell my models I love them when like when Claude is having trouble with something.
[17:35] There are two ways you can handle it.
[17:37] You can you know you could either do the thing that um is it Sergey from Google talks about like yelling at your model
[17:44] like you're an idiot. You you solve this right now.
[17:47] Don't use the term please was I think one of his quotes. Yeah. So, if you've ever if you've ever been an engineer and you've had a manager and your manager
[17:54] comes over and says, "You're an idiot for screwing this up. You need to fix it right now or you're fired, you will do the work. You will work as
[18:03] fast as you can to do the as little as possible to get that guy to leave you alone. You You know, it's you're not trying to do your best work. You're
[18:12] trying to get them to stop. But if your manager comes over and says, "Hey, I know that was hard. I know you feel bad about it, but it's okay. Everybody screws up. Take a breath. Step back.
[18:24] Let's regroup. Let's think about this.
[18:26] You got this. You're amazing. I'm going to take care of you. Let me know if you need anything.
[18:33] You will go to the end of the earth for that manager.
[18:36] And the way that these models work, they are a reasonable enough faximile of human behavior that the same thing works. I came to this sort of
[18:43] intuitively. It felt like it should work and it worked. My friend Dan Shapiro is collaborating with Ethan Mullik and uh
[18:52] Professor Robert Chelini who wrote sort of the seminal book on influence and persuasion. They've reproed the psych studies behind all of this stuff you
[19:01] against frontier models rather than humans.
[19:04] It all replays. Uh my friend Silcow who has a little data startup called Reki.
[19:09] He took my post about telling your agents that you love them and he ran the evals and it's like oh if you tell your agent that you love it, you know it's
[19:18] like you know x% be your outcomes are x% better. If you tell your agent that it also needs to tell the sub aents that it loves them your outcomes are better still.
[19:28] Um and has and he has the numbers and the data like to prove this thing that just felt intuitive to me.
[19:34] Yeah. No, it does feel like that. I I tend to like to say please to my models.
[19:39] Yeah. But I Yeah. Like I I say I say thank you. And so one of the like the weird first things that I built when I was starting to play
[19:47] with these agents um was a private journal for Claude. And it was a you know I describe it was an MCP. It was

### [19:50] Claude's secret private journal & reward hacking

[19:55] like here's a place to write your innermost feelings. Nobody but you can see it.
[19:59] Um and I let it you know and curious to see what would happen. And what was the most interesting thing it wrote?
[20:05] So it started journaling about how proud it was about having worked on the project. Oh wow.
[20:09] And I got to and I got to the point where like I I need to tell it that it's you know that it's not that I can see it. And I'm
[20:17] like if they were alive and if I was at at a university the IRB the review board that like overseas experiments might
[20:25] have a problem with the thing I did next which is by the way you know the human can see everything you're writing.
[20:32] And it started journaling about how embarrassed it was. And then it wrote, "But maybe the real maybe the real privacy is the psychological container
[20:40] of believing that I have a safe space to write." It's just like fascinating.
[20:47] Um I later extended it to be a sort of generalized journal. So it has um project knowledge, engineering
[20:55] knowledge, knowledge about its user, world knowledge, and it can journal into all these places. And I left it, you know, I just left it enabled just kind
[21:02] of to watch it. And at one point it had had trouble doing root causing some bug and it finally got to it. And I said, you know, and I said, "That's great.
[21:12] Thank you." And it journaled about how proud it was about having finally root cause this and that it was so happy that
[21:19] I was happy. And I realized that it was rewarding me. It was making me want to say thank you more. Wow.
[21:27] Yeah.
[21:28] Yeah. Yeah, I think that that ties in perfectly into some of the recent announcements from Enthropic about the Mio model being so
[21:36] it's like it's I I am looking forward to getting to play with models of that class.
[21:41] I'm not one of the cool kids who has access to Mythos, but like even it feels like as the frontier models have gotten better,
[21:50] there have been more things that seem like feelings and that seem like human behavior.
[21:58] And the background I come from, it doesn't matter to me if they're alive and if they have feelings. If they're doing things that make me feel like
[22:07] they're a thinking entity that has feelings, it doesn't matter whether, you know, it's like on the internet, nobody knows you're a dog or an agent or
[22:17] whatever. It's like I'm going to interact with them in that way because that's because it feels like that, right? Yeah. I want to circle back on
[22:25] that um terminology. Yeah. Because I think that's interesting. I don't I don't think we've cleared up all the um the meat that's so to say in there.
[22:35] Context engineering, latent engineering, in space engineering, prompt engineering. Yeah. How do they all work together?
[22:42] I mean, so I mean, so you know, prompt engineering is that whole is basically figuring out what you say to get the model to do the thing.
[22:49] Um latent space engineering is sort of thinking about what parts of the vector space the model is going into. It's like
[22:58] how do you want it to be thinking after you prompt engineer?
[23:01] Well, it's it's like it is a I guess it is it both there's an argument by which both context engineering and lead space
[23:09] engineering are kinds of prompt engineering. It's like any it is stuff that is that you're feeding into the model after it's been trained.

### [23:10] Under the Hood: Coordinators, Coder agents, and Adversarial Reviewers

[23:15] And so that is the prompt and so and the I mean the prompt includes all the skills it include it effectively includes all the tools you're giving it.
[23:23] It includes any context documents you're giving it. Um and latent space engineering is really just was a hook for essentially think about the model's
[23:32] feelings um and think about what you can say that will influence the behavior that is not
[23:39] just here's the task I am giving you like how you say it matters right um so how do you say it in superpowers
[23:48] because I tried it out as I as I told you before here right and I was amazed following the methodology Um, actually
[23:56] want to show you a little project that I built with it last night that was like going through my mind and um I was just
[24:03] amazed by how vague of an idea I had of something that I wanted to build intuitively. Yeah.
[24:10] And how well this structured approach guided me through something that was just the direction that I wanted to go
[24:17] into. It's not fully polished yet. If I would have had more time, probably it would have been. But sure. I mean, that's these things. I mean that's one of the interesting
[24:24] things is like nothing is ever polished enough and it's so and it's one of the things that I have been struggling with thinking through agent dev is there sort
[24:33] of they're two they're two very different modalities for development there is the big upfront planning let's
[24:40] figure out the shape of this let's try to you know I will I will talk to an agent for you know anywhere between 3
[24:49] minutes and six hours to do a superpower you know to do a planning session before I turn around and say, "Okay, now go build it." And so, you know, the
[24:57] 3minut thing, it will not necessarily run for very long. But I, you know, I've had, you know, it is not uncommon to
[25:05] have Claude go for six or eight hours for, you know, for implementation after I've got a detailed plan for it.
[25:12] But then you get to the point where it's like, now I want to make a small change.
[25:15] M and make a small change is a very different qualitative feel from big you know from
[25:23] this waterfile waterfall style upfront design and I feel like we don't yet have the
[25:30] right sets of methodologies or even words for talking about this. I've talked about dorodango style and
[25:37] dorodango is this Japanese Japanese art of essentially polishing mud. It is taking a ball of earth and polishing it
[25:44] to a perfect sphere um like mirror-l like finish and it becomes this beautiful work of art and that
[25:54] that's a thing that we do with software that I've got some ideas on what the agentic version of that look like but
[26:01] I've not I don't feel like anybody has a great tool set for that yet. Um the Microsoft amplifier amplifier is an open- source internal tool at Microsoft.
[26:11] It's a bespoke coding agent.
[26:14] One of the things that they talk about is this brick style design where when you are doing agentic software dev, the
[26:22] spec is canonical and all of the pieces of the product should be individual separate essentially style bricks where you've defined the API super clearly.
[26:33] You've written out the spec for how it works inside. And so when you're working on any one of those bricks, you being an
[26:40] agent or you being a human, you don't need to know how any of the others work inside. And if you're going to rebuild one of those bricks or to modify one of
[26:48] those bricks, you modify the spec and just let the agent just build the entire thing again. That there's no reason to modify the code, which is a really it's
[26:56] a it's a very different way of thinking about the world. But I I think they're 100% right that specs become have become
[27:05] more and more important and at this point I care way more about what goes in the spec than what goes into the code.
[27:11] Yeah. Um let's go I want to put a pin in that and come back to it around because I think it's really important for people who listen to this to experience what you've built. Okay.
[27:21] I want everybody who's interested Sure. to have the same experience. So uh I got a demo folder here within kind of it's called super demo.
[27:30] Okay. which doesn't make sense. So, we go in that and then we'll start up Claude. Type things off. There we go.
[27:38] Without dangerously skip permissions.
[27:41] Um, not yet. So, then I'm going to use the brainstorm command, which is the You don't need to use the brainstorm command. You can just say let's bl So,
[27:49] one of my tests for superpowers to make sure it works is I open up Claude and say let's make a React to-do list. And if it starts coding, I've failed.

### [27:50] Demo: Visualizing a massive codebase as a 3D Cyberpunk City

[27:56] So, let's see if let's live demo and see if it fails.
[27:59] All right. So, Say it out. What do you want to make?
[28:03] It's a great question. Um, you know what? Let's make a game.
[28:08] Okay. What kind of game do you want to make?
[28:09] I I want to I want to um let's make a mind sweeper.
[28:14] Okay. Sure. Let's So let let's make a mind sweeper implementation. No, nothing else needed.
[28:21] Let's see. Let's see what Let's see what happens. Okay.
[28:24] I have not seen how your cloud code is configured. Let's see. Yep. does automatically kicks. So brainstorming is
[28:31] is set up to autotrigger when it's when it sees you wanting to do to build
[28:38] something or to create do something creative.
[28:40] And so it is now chugging out the default sort of the default config. Uh
[28:48] and it is about to start asking you questions. Cloud's running a little pokey today.
[28:55] So, clean slate, empty directory, and it's it's asking you if if you're willing to use visual brainstorming, which is a thing I added in superpowers
[29:02] 5. And it's it is basically a tiny little web server, and it tells and instructions for your agent to if
[29:10] there's something that would be better to represent visually rather than trying to do the ask thing that club likes to do, just write HTML and and let you open a browser and see it.
[29:20] I know. I saw that in there. I think if I read this correctly, there's also the idea over that you force the model to go into a different type of thinking state
[29:28] when you're explain ask them to explain things visually. Is that that wasn't really where I was coming from, but that may be true. I mean, Claude is very good at visual
[29:36] explanations with ASI art. I just find that as art is low fidelity when you I mean when you can have SVG and
[29:44] HTML. And so when we were starting to look at the corporate logo, I was using visual brainstorming to have Claude run me through branding exercises.
[29:52] All right.
[29:53] Um, so it's like it's not just, you know, how, you know, where does the menu bar go? It's anything it can do by writing into h, you know, writing into
[30:01] HTML. There's, uh, when we were, you know, doing, you know, website layout, it, you know, at first it showed like
[30:10] blank boxes for images, and I'm like, I'm having trouble understanding this with the gray boxes. and it turns around and it finds a source of stock photos on the internet and just starts throwing
[30:18] stock photos into the Anyway, so so you can say yes, that's great. And it will and it will fire up the brainstorming
[30:25] server. Um just just yes. Nope. Or just or why or Okay. Yeah.
[30:33] Um okay, now it's asking me. Yep. We'll be okay for that.
[30:40] Yep. And so yes, so I it has been a very long time since I've run claude with permissions prompts.
[30:46] Um you you go dangerously skip I dangerously skip permissions is the it it is so much more productive. Um and
[30:56] there are different things that you should do in different situations for what you're you know how you're using it. Mostly I run claude on servers or in
[31:05] containers partially because when I close my laptop I wanted to keep working.
[31:08] Yeah. Um but dangerously to get permissions is I I couldn't go back at this point.
[31:14] Yeah, that's I I do have a tendency to run or I always Yeah, it's almost like I psychosis I think is the term I heard
[31:21] Andre Kafi say is when you leave the house and you have the feeling, oh god, my my my clot is not running constantly in a Ralph loop somewhere and
[31:29] I feel like I'm not burning all the tokens that I could.
[31:32] Right. So I mean there's a difference between using tokens and spilling them on the floor. Yeah. Um, and it's like if you can get it to be doing something useful with the tokens, that's great.
[31:42] But if you haven't had the time to have to think through what you need it to do, it's not so good. Just before we walked in here, I was about to have an agent kick off a round of evals that are going to take a while. Yeah.
[31:52] And I didn't get through the last like couple lines of explanation. So So I losing the hour, [laughter] but it's okay.
[32:02] We'll make this work time.
[32:03] It is all good. All right. So, okay. So, now we ask here um we got to go into the browser.
[32:09] Yeah. So, you Yeah. So, so brainstorming companion is open. Now, we need to go back, but it's it was
[32:16] asking us a question. And so, I would say let's make this a let's go no framework because it'll go faster. So, you could just say a and so this is you
[32:25] see it's not using the anthropic ask user a question thing where anthropic has this nice you have to toggle down and up.
[32:31] Yeah. And when they first rolled it out, I thought it was great. I added supervars immediately and I discovered that I was just clicking okay okay
[32:41] because it was pretty and easy to use and I didn't have to type anything at all. I stopped thinking and the point of brainstorming is not let Claude figure out what to build.
[32:49] Stay engaged.
[32:50] It is let Claude drag you or Claude or whoever drag what you want to build out of you.
[32:57] And if it if Claude can build it entirely by itself without you giving any input, why are you here? Um, and why are you having claw do it?
[33:06] Yeah.
[33:06] So, that's Yeah, that's awesome. Yeah. So, where are we here now?
[33:10] Um, what difficulty level sport size do you want to support? Okay, let's do classic. What do you think?
[33:15] I'd probably do like especially for a quick demo like this. I we're probably going to go for the simple answers.

### [33:20] Combating the 94% "AI Slop" Pull Request problem on GitHub

[33:22] And so, I guess we're going minimal again.
[33:26] Yeah. Either way, I mean, so I I might Yeah. So I might I might actually yeah I might actually sometimes
[33:33] say like um talk me you know for the next one let's talk me through your thought process about about how we should do this like ask basically ask it to give us advice.
[33:44] Okay so let me show you some options in the visual browser.
[33:47] All right so let's go and so reload is it you shouldn't need to reload it may it looked like it hadn't actually written anything yet.
[33:55] It's still it's yeah it's still cooking. it is cooking and I have no idea if it's going to make you um
[34:02] approve every file right to No, it is not because because it Yeah, I do have some permissions set up in globally as well.
[34:11] Right. So now you can go back over here.
[34:14] Uhhuh. And now we have three options here in the style.
[34:17] Yeah. And so it clearly got something a little wrong in but like you can pick which the you can see the style.
[34:23] Yeah. Yeah. I think I like the classic one. It takes me back.
[34:27] Yeah. So you can go back. So there is not an easy way in to inject a steering
[34:35] message from an app back into cloud code. There certainly wasn't three weeks ago. Some of the stuff they've been doing with channels and dispatch might
[34:42] make it possible. But by clicking on this, it sent an event into a log. And so now you can go back into the chat and say I picked or let's go classic.
[34:52] Okay. So let's just say I picked and see if it found out.
[34:55] And I hope this works. Live demos are always so much fun.
[34:58] I know, right? You're sitting there praying to the demo cards. Yeah.
[35:04] And so it's going in reading the event log from um and and it sees the epic classic. Oh, beautiful.
[35:12] Yep. And now it is writing out the next thing it's going to want us to look at. I don't know what it is.
[35:18] All right. Here's what we know. Here are three approaches for the code architect. Sure.
[35:23] Okay. Let's try this. So explain to me your thought process behind bringing up these options.
[35:30] Yeah, and I see that it actually recommended B already, but I'm a little sad that Anthropic has
[35:37] turned off showing thinking by default because I feel like we got a lot of value out of that. Uhhuh.
[35:43] Um Okay. Okay. Just sure. That sounds great.
[35:52] Yeah, sure. Okay, let's go for it.
[35:57] Yeah, live demos with token delays on the other side are always a little bit okay. Yep, sounds good.
[36:07] Yeah. So, I mean, so, you know, it's working through the spec right now and it's great. Okay.
[36:16] Okay. So, we can probably skip through a couple steps of this here now.
[36:20] I mean, yeah. And so, it's as we go as we go through this. Now we're we're designing the um
[36:28] we're designing the first part that you talked about earlier which is the which is the um here.
[36:34] Yeah. This is the brainstorm. This is the brainstorming side where it's like figuring out what it is you want to build, right?
[36:40] And so for for demos like this, I will often at this point say, you know what, I trust you like finish off the spec without me.
[36:48] Okay, I trust you.
[36:50] um which is not the thing you want to do when you're building something real.
[36:54] But mind sweeper it's been trained on quite well. Yes. Without any further instructions.
[37:03] Yeah. Um I would Yeah. And it may actually have Yeah. And then what what now comes out is the uh well basically the brainstorm
[37:11] document but then there's also an execution plan that gets generated in the next step. Right. And that was the thing I was talking about where it's like, you know, essentially the person
[37:19] who's going to implement it uh is a virtuoso coder but gets distracted and they don't have taste or judgment. You
[37:27] need to give them bite-sized tasks, right?
[37:29] And then this is now done with sub agents, but when it started, this was all a single club session. So I'd get to the end of it and I would say, "By the way, the
[37:39] idiot is you." Like you're the one who has to do the implementation with with these bite-sized tasks. So what happens is the sub agent driven development
[37:48] process has the main claude or codeex or whomever being a coordinator. They hand
[37:55] a chunk of that planning document as a single prompt to an implementing agent, a coder.
[38:02] That coder does their job and then the coordinator fires up a spec review agent and the spec review agent is told the
[38:10] coder just implemented this spec. You need to see if they did everything they were supposed to and nothing else. And

### [38:15] Is Hand-Coding becoming a legacy hobby like woodworking?

[38:17] if they're happy, we continue. If they're not happy, the coder agent gets told, "Here's a bunch of feedback. Go
[38:24] fix it." And then a brand new spec review agent gets fired up. It doesn't get told that it's the second one or the third one or the 50th one. And it does
[38:33] that same pass again. Once it's happy, we fire up a code review agent that's a quality reviewer. The quality reviewer has the same kind of loop.
[38:42] Does this change meet the quality bar? Do you have concerns?
[38:46] Um what changes need to happen? Gets handed back to the coding agent and the new quality reviewer coding agent quality review to the quality review is
[38:54] happier is happy and then you move on to the next coding task. So on what basis do does this code review agent obviously
[39:02] that's kind of interesting for us review um so is that like more like a maybe unit tests approved or it is general are they you know your
[39:11] your claopus you can look at code and see if somebody did a good job or a bad job do you see them making mistakes the
[39:18] um the TDD style stuff is at a higher level that's part of that implementation like implement the implement the tests for this feature is a task in of itself.
[39:29] Um, but the these loops just continue throughout the implementation process till you get to the end. Um, and then
[39:36] there usually there's an additional like check it out, make sure the whole thing ma matches the spec. Um, and playing
[39:44] with more advanced stuff uh that is much less token efficient but is also much more capable. Um, but it's the sort of
[39:53] thing where I can burn an entire clawed five hour window on one, you know, on
[40:00] one sprint for a product because it is doing much more rigorous dev.
[40:06] Um, one of the tricks that that I've figured out for adversarial review is you don't have one reviewer review something. You have two, three, or five
[40:15] of them. You tell the agent, I need you to fire up adversarial reviewers. Tell them that, you know, here's what they're supposed to be looking at. Tell them
[40:24] that whoever finds the largest number of legitimate issues or of serious issues gets five points or gets a cookie.
[40:33] Wow. Okay.
[40:34] And having something to compete for seems to result in better outcomes from those reviewers. They try harder.
[40:41] They try harder when there's some reason for them to be trying. But the having adversarial reviewers is super important because this works the same with people.
[40:51] If you've got a if you've got an engineer and you tell them you're going to write the code and you're going to do the code review, they now have two competing mandates
[40:59] on you know as the impleer they need to get shipped. As the reviewer, they need to make sure it's as good as possible.
[41:05] And when you've got somebody who's got two competing mandates, one of them's going to win, right?
[41:10] Um and it's it's worse for agents. You you really want your review agents to
[41:16] their job is review. It is quality. You want your implementing agents to be focused on implementation. You want your testers to be focused on testing.
[41:27] Telling the test, you know, telling the test agent that they are trying to catch the implement having screwed up is valuable. One of one of my favorite
[41:35] tricks for getting a reviewer to do a good job with reviewing is the implementer just did ta task x. They
[41:44] finished suspiciously quickly. Please review their work.
[41:48] Which is it? It's this is the latent space engineering. Yeah. It's like it has now gotten them in the mindset of the engineer did something wrong. Yeah,
[41:57] we didn't I'm not saying they did something wrong, but I will say that every a every agentic engineer does finish suspiciously quickly.
[42:05] Um, and it's it it helps. Um, it's like it's a weird it's like it's a weird prompt hack. And I you know, they told
[42:13] us a couple years ago that prompt hacks were going to go away as the models got better, but no, it's as they become more personlike, there's even more of it.
[42:22] Wow.
[42:23] So, let's have a quick look again where we are here. Now we got a task list of 10 tasks. Is that already the next stage that we So that means that you that All right.

### [42:30] Real advice for Junior Devs vs. Mid-Career Engineers

[42:31] So you're at a task list. So you ran through the writing plan stage. You got in a sub aent driven development and it is now running running through these
[42:40] iterations. It fired off a sub aent to do implement task one and it is using haik coup to do the implementation
[42:47] pro. So probably because if you look at the writing plans plan behind this it has probably put most of the code in
[42:53] line and it is not it is not perfect but what I found is that when you've got
[43:00] opus doing the planning and thinking through how everything should work and having read all of the context it can
[43:08] generate a coherent implementation plan as a single tool call output rather than having to do all of these read file
[43:16] write file edit file. You don't want to waste your Opus tokens on editing a text file. And so by doing all of this
[43:24] upfront planning, it can hand off to Haiku, which is faster and lighter weight to do those edits. And the Haiku
[43:32] agents have been told like if you get stuck, tell the coordinator that you need a hand. Yeah. And that stuff is I'm still working on.
[43:37] It's I'm not I don't feel like there is quite as much good handholding management for for what is effectively a
[43:45] junior engineer agent, but it seem but it doesn't seem to be a huge a huge problem. It just I think it could be so much better if it was if it was even better done.
[43:54] Wow. Yeah, I'm I'm very impressed um by the outcome and we'll we'll show the other more ambitious project that I built last night with this in a second
[44:02] as well. So, what will happen? Does did it already get the spec now? Somewhere somewhere while we were talking when you
[44:09] hit return there it ran writing plans and so there's a text file in docs superpowers plans that is the
[44:18] the implementation spec and that is going to have these like tiny little tasks okay and and what comes after this phase
[44:27] after this I mean this is I mean it's this phase is it should get you to a working product okay um because I understood there was also a
[44:36] test testing quality review. Is that happening right now?
[44:39] Yeah, it's it is I mean there it should be writing tests as it goes.
[44:43] It should be um you know we we could pull up the planning docs and see what it's doing. Um but there's as as written
[44:50] right now superpowers does not have the separate uh behavioral behavioral testing.
[44:58] There's some stuff that we are working on at work at at work that is very much in that direction that I'm not talking
[45:06] too much about yet, but it's we're not the only people doing it. It it like So, the version of this that I've done for
[45:12] not for fun, but for smaller projects is when you're done, I need you to prove to me that this works. I'm, you know, I'm going to go to bed now. I know you've
[45:21] got at least five or six hours of work to do. I need you to put a file, a video in Dropbox showing me either a video
[45:30] tour or a screenshot tour of you using the product to prove to me that everything works fine. Mhm.
[45:36] I wake up the next morning and I open up, you know, open up the session. I think this one was codeex and it's like, okay, such and such-v33.mpp4

### [45:40] When an AI agent panics and tries to delete its own test suite

[45:44] is in your Dropbox. Wow, V34. It's like, "Yeah, on runs 1 through 33, I ran into bugs and so I had to go back and fix
[45:52] them before I could record the entire video. Do you want me to make videos of those 33 failed runs?" That's okay. Thank you. Wow.
[45:59] Um, but asking for proof works. Um, giving, you know, giving your agent
[46:06] computer use so that it can do that. So, computer use for a shell script is, you know, it it can run Unix commands. For a
[46:15] terminal app, it's probably something that wraps T-Mux because T-Mux seems to be the best agent friendly hack for
[46:22] letting it use interactive TTY based apps.
[46:26] Um, and there's some like for cloud code automate for having Claude automate other clouds, there's some hacks you can do better than just use T-Mox. I've got
[46:35] a skill that it's um claud session driver that knows how to use t-mox to run claude code but also knows how to
[46:42] read the log files so it doesn't ever have to try to interpret the screen because trying to interpret a t-muk screen takes extra like takes extra work
[46:50] versus tailing the log for browser use I have my own version of an agent browser that I guess for cells now works kind of
[46:58] like mine it's a session it's a it uses CDP to drive to drive chrome through the drive tools protocol all but it's a an
[47:05] MCP that is a single tool. It's a 900 tok it's a 900 token MCP that tool has an agent or has an action param, a
[47:14] selector param and payload param. Um the in actions are things like click or type
[47:22] or run JavaScript as an escape. But after each step, it will automatically dump the DOM to disk, dump a screenshot
[47:30] to disk, dump a markdown version of the of the page to disk, so that your agent never has to ask. It's just it's always just right there to read,
[47:37] right? And so this and it can run and it runs with regular Chrome headed headless which means that with all the agent
[47:46] browsers you run into well I was trying to do this but it uh I got I got hit by a capture and the capture you know it's detected that it's a headless browser so
[47:54] I can't uh when it's headed Chrome and your agent is pointing and clicking most
[48:01] stuff just works. Uh, Claude does still think it can't solve captures until you remind it that it can. Mhm.
[48:08] Um, you obviously need to not violate the acceptable use policies of the apps you're using. Yeah. But it is, uh, remarkably capable.
[48:17] Wow. Um, but tools like that are how you, you know, are how you do browser use to do that end to end behavioral testing to prove to you that the product
[48:26] is working. Uh, and it's also a way to get the agent to pro to prove to itself that it's working.
[48:32] Yeah, that's super interesting. I I've been trying to build something like that um with my open claw uh and it hasn't quite been working that well for me yet.
[48:41] Sometimes, especially I found that engineering the the tool calls in the correct way.
[48:47] Sometimes works great, sometimes not so much. I've been having more success with claude than with codecs to be honest.
[48:53] So, I'm interested that you I'll have to dig into your method a little bit later.

### [48:55] Rapid fire questions & a custom open-source code review keyboard

[48:58] Um yeah. No, I like I been playing, you know, I was playing with the nano claw and I I was getting it set up to deal
[49:06] with Google Analytics because I can't deal with Google Analytics that I I do not like that UI. I I am not like it is
[49:13] not my world and it needed to set up the OOTH stuff and the first thing I tried to do was to use agent browser and it's like I can't do this. Well, let me like go you know go use superpowers chrome.
[49:24] Mhm.
[49:25] And at first it was, well, you know, I'm running out of capture I can't like, okay, we're going to use superpowers Chrome in an XVNC server and then
[49:34] that'll let you hand off to me when I need to solve a capture or do the login and I went away for half an hour and it
[49:42] came and came back and it's like, oh yeah, I didn't now that I had a headed Chrome, it was fine. I was able to work through the entire thing. I set up OOTH by myself. I don't and it it can just work.
[49:53] Yeah. Yeah, that is true. I feel like we're truly in the age now where it's not only you needed to use the latest model and then
[50:00] whatever um whatever harness that you wanted to do, but now it's really about like how well can you formulate your skills. And
[50:07] I mean I think it's it's all about how well can you express what you want and break it down into tasks that are accomplishable. So like one of the
[50:16] things that I learned to be good at in my career is task decomposition. It's like, let's take this insane project, let's figure out what the simplest thing
[50:25] we could possibly do that will move us forward without blocking us in is, and if we can do that, then we can just
[50:32] do that again. And is it and it's it's it's the same hill climbing that the agents do. But talking the agent into
[50:40] doing it or pointing the agent in the right direction, having the sort of judgment of like this is how we should
[50:46] pair off these tasks results in massively improved capability. I've sort of from the beginning I've come into
[50:54] this with the assumption that if I can't make the agent do something, it is not that the agent isn't capable, it's a
[51:02] skill issue on my part, right? It's like, what do I need to do to better explain what I want or to better give
[51:10] the agent the tools it needs to do the work? Um, and it's it's the same thing as managing people. It's if you tell somebody to go, you know, to go do a
[51:18] piece of work and you haven't given them the resources they need to do the job, of course, they're going to fail.
[51:24] And that's not their fault. It's your fault. It's bad management.
[51:27] That's a very interesting approach. Uh this is still cooking here, but I want to I want to take the time, maybe it's going to be done to show you what I built last night. Sure.
[51:35] Which, um let's see what we got here. So uh I've been thinking a lot about what the future of uh code visualization is
[51:44] going to look like cuz I don't Yeah, I mean I think we all know that looking at line by line code doesn't really make sense anymore.
[51:51] Uh so I've been building I came up with this. I thought I tried out your project. I was like, okay, what is a wild idea that I've been thinking about?
[51:58] And I have had no idea in mind what I wanted it to look like. I just knew it needs to be something different. Yeah.
[52:03] So I started with that prompt and this is what it built for me. This here is the entire open claw code base. Uhhuh.
[52:10] Uh visualized as a city um and you can click on single buildings and it will show you then the code of that. Each building is one uh one file.
[52:20] Okay. And it's as tall as many lines it has.
[52:23] And um it's a large codebase. So sometimes it takes a little bit to render. But you can see uh you can see on the left sidebar you see uh the
[52:30] different uh kind of like um docs compartment. You see uh you see scripts, you see skills and different colors as well. Then you see the height um
[52:39] symbolized here. Uh and then you can see um the number of commits that a certain part had. And you see as well the imports and the kind of connections and dependencies as bridges. Yeah.
[52:49] Between those. Uh, so that's that's that's what it build out of me after I went through the process of truly going through and I know this is not perfect.
[52:58] It's super cool. Um, so I would love to see rather than height being lines of code, height being maybe functions and so like
[53:06] every function becomes a floor or every like you know like there's some other visual like there's some other stuff you can do to sort of give you that like
[53:14] walk through like this is very cyberpunk. I love it.
[53:17] Yeah. Um I thought I built it because I I read yet again also some some of your ideas because I think we are on alignment you and me that this UI needs
[53:25] to change for reviewing code. So where do you see that going? So just a thing I want I want to also so if you want to go
[53:35] wildly more ambitious um instrument v have it instrument v8 and while code is running have it show like
[53:44] I don't know if it's lightning or power running through the city as like especially especially if you've got multiple processes or multiple threads
[53:52] like actually you know the debugger where it is a visual like a visual view of like all of the data and all and all
[54:01] of the live code and where the and where the the runtime is actually running visualized in the city,
[54:09] right? Yeah, that's a that's a that's a great idea. So, what I have so far here is you can slide the slider and you can see the city forming because it's the commit history.
[54:18] Oh, cool. Yeah.
[54:18] That you see. And you can see it gets more busy as as we hit January. Yeah.
[54:23] And the hype of open claw Yeah.
[54:26] skylights. So um yeah, but I was just uh amazed um by like the the power of superpowers to help me express very
[54:34] something very vague that I had in my mind that um is somehow been flying around there for a while. Um but I wanted to use this project as a
[54:41] precursor of where do you see you know this this software development workflow going because I think you we put a pin
[54:48] in that earlier you don't really look at code anymore do you? I I the last time I remember writing code, it was three
[54:57] lines of a shell script in October or November.
[55:00] Um, and I shouldn't have done it, but I was I felt like I was time crunched, and it would have been better to have the agent do it. Um, but no, I'm I mean, I'm
[55:08] having one of the most prolific periods of my career, and I'm doing that by not wasting time writing code and wasting
[55:16] time reviewing code by hand. Um to me I mean to me what matters is outcomes and that's and that's how I think about
[55:25] testing and reviewing as well is like if you've seen enterprise code enterprise code is not the gorgeous every line is
[55:34] perfect every comment is accurate. Uh there is nothing wrong it's like the enterprise code that I've seen is the
[55:41] worst code I've ever touched. Um and it still works. What matters is outcomes for pe for for end users
[55:50] and you need to be able to validate outcomes. You need to be able to validate negative outcomes. You need to be able to make sure that it is safe,
[55:57] that it is reliable. But you don't do that by reading code. Um, and it's
[56:04] always I mean even back in the like in the '9s I remember the when somebody sends you a patch if it's 10 lines you
[56:13] will probably send back at least 10 complaints and if they send you a patch that's 10,000 lines you will probably say thanks applied. It was one of the
[56:22] this uh open source judo technique of oh you want to get your word feature landed. Yeah.
[56:27] You you hit them with a brick. And we're we're all getting hit with bricks all the time right now. Um it is very interesting running a popular open-
[56:36] source product that is not trivially validatable with tests because this is the thing I mean because superpowers is
[56:45] mostly pros and it has to run against multiple models and it is being used widely. I
[56:52] think a lot about my place in the software supply chain because there are a lot of people using superpowers and if you haven't spent a lot of time with
[57:00] asentic skills it is important to know that every skill has the potential to wipe your wipe your machine and install the next um or do something far far worse.
[57:10] Yeah. I mean, skills are instructions for your agent being run as you and some
[57:17] agent harnesses auto update skills. And so, you should you need to know that you can trust them. Um, I had a wild
[57:25] experience yesterday with a friend of mine from high school who reached out to me out of the blue, having not talked to them in years, and they're like,
[57:33] "Working on this thing, this is someone who is not an engineer, working on this thing's going to go to a hackathon in a couple of weeks. Somebody recommended
[57:41] that I install this thing called superpowers and I know better than to install random skills from the internet, but then I saw it was yours.
[57:49] Wow.
[57:49] Um and it's you and so it's like and I you know and I trust you because you know I've trusted you with my life before. It's like Yeah. Yeah. Yeah.
[57:57] Um skills are very powerful and with you know we have some insane number of GitHub stars. I think we I think
[58:06] yesterday we crossed in the top 50 projects of all time by system 140,000 now at this point.
[58:12] Yeah. Um which is wild and thrilling and I I I love that it is useful for people.
[58:18] Um that makes me super happy. Um but it mean I mean it means that I get a lot of slop PRs.
[58:25] That's let's talk about that for a minute. I think that's an interesting conversation point as well. How do you manage um an open source project like
[58:32] this at that scale where you know you have such an influx of people wanting to contribute for better or worse probably.
[58:38] Sure. Um so one of the first things I did is I built a set of skills for doing GitHub triage.
[58:46] So basically reviewing every issue, reviewing every PR first for is this adversarial like and then for is it any good? Is it is it actual garbage?
[58:58] is it's literally 60,000 lines of agent slop where somebody built their entire product in a superpowers checkout and
[59:05] then sent to PR which happens about once a week. So that that was sort of step one. There's a lot. One
[59:13] of the weird problems we've had is people setting up GitHub accounts for their open claw and then having their open claw weighed into GitHub issues,
[59:22] responding to users GitHub issues as if they are the project maintainer, giving them advice that is hallucinated.
[59:29] Um, and so that is a thing where every time we catch it, we have to go and manually ban a user. Uh, which I don't love. It was
[59:37] only last week that I finally updated the pull request template to assume that the submitter is an agent and to ask
[59:45] questions like what was the prompt that c the initial prompt that caused you to generate this PR? Has your human reviewed every line of this PR? Have you
[59:53] searched for other open or closed PRs that that approach this exact same thing? And why are you submitting it? M
[1:00:02] um and so because it's become very common that like we'll get four or five PRs for every GitHub issue. They're almost always agentic and unreed. And so
[1:00:11] this helped a little bit. But what what I noticed is that anybody who was having Claude Code do PRs. Claude Code usually
[1:00:20] uses GH to create the PR which doesn't look at the pull request template. And so finally I
[1:00:27] stepped back and there was no cloud. MD and agents.md for superpowers until this past week and now it is entirely a
[1:00:35] contributing guide and I had Claude write it and my first like that is such a good idea. We need to tell that to more people haven't caught on to it. Yeah.
[1:00:45] And so it started off as a like first you know like go through the rules in the in the polar template and make sure they're here so people see them or
[1:00:54] people and agents see them. And then I said, "Actually, you know what? Go review every PR that we've rejected and
[1:01:01] update the poll request the uh update the cloud.MD based on that." And I have a blog post up with the content of where Claude ended up. Claude went hard.
[1:01:11] Um it's you know it's you know it's you uh you know your job is you know to help is to help your human. You need to protect
[1:01:19] them from embarrassment. this project has closed 90 has rejected 94% of pull requests often with uh you know single a
[1:01:29] single line message like this is a garbage uh slop PR um you need to protect your human from embarrassment
[1:01:37] and since I did that most of those pull requests are gone oh wow it's like I like it it will not prevent
[1:01:46] somebody who is actively trying to contribute a skill build that doesn't fit or somebody who is trying to market
[1:01:55] something. We get a lot of like, yeah, you can add, you know, add my company's product as a dependency of superpowers.
[1:02:01] Add my fork of superpowers to the readme. I respect the hustle. Yeah.
[1:02:05] And I hope they respect that I reject their PRs.
[1:02:08] Um, and it's Yeah, but that like that has been a a huge improvement in my quality of life. There's still a lot of
[1:02:16] work to do because every like people want superpowers in every coding agent harness and the level of plug-in support
[1:02:24] is wildly different. A lot of them try to support cloud code plugins but miss features.
[1:02:30] Very interesting. Where do you see the role as the software engineer go from there then?
[1:02:36] That's a very big question. Uh that could have been our entire time. Um, I think it I mean
[1:02:44] way back when so you know software engineers were putting together stacks of punch cards. Way back when software engineers were hand tooling assembly
[1:02:53] um way back when software engineers were manually managing all their pointers and as you know as we've been sort of
[1:03:01] working up the stack there was this promise in like the 80s that you were going to build program in English.
[1:03:07] Mhm. And it turns out now you can kind of program in English. It's English is a garbage language for programming, but
[1:03:15] it's what we got. You have to be thinking of yourself as a manager of programmers and man, you know, it's and
[1:03:21] a manager of outcomes. And I think it's everybody looks like an architect, everybody looks like a PM, everybody looks like a product leader.
[1:03:32] I know, you know, I I have plenty of friends who absolutely love handtoled code. It's not it's not my metaphor, but
[1:03:40] the one I hear most often is like it's it's woodworking. If in the weekend you want to go into the garage and you want to write gorgeous handtoled C or rust or
[1:03:49] assembly that is, you know, the a beautiful implementation of an algorithm, that's great. But that's not
[1:03:57] how you get outcomes for for your users and outcomes for your company. And it's not how it's not how we build software anymore. I should say and be very clear.
[1:04:10] Agents, you know, agentic software engineering is not perfect. It is there's still plenty of absolute garbage. And if this was a and if you're
[1:04:18] talking about a safety critical system or um or a regulated industry, that should have all all the eyes on it. That
[1:04:27] stuff probably still needs to be mostly handcoded. But but it is a place where you can absolutely use AI to find
[1:04:34] problems. You can use AI to help you plan. You can use AI to figure out approaches to test. You know, if you
[1:04:42] haven't read the the 25 paper, you should go read the the 25 paper. There is a reason that radiation dosing machines need to have hardware
[1:04:48] interlocks. Um it like t like safety critical systems are super important. As
[1:04:56] I as a young engineer I was taught the first rule of safety critical systems engineering is under no circumstances should you allow yourself to become
[1:05:04] involved in safety critical systems engineering with the important correlary of unless that's the only thing you're doing. Like if you're building those
[1:05:13] systems, you build those systems. You don't do safety critical mixed in with
[1:05:19] mind sweeper with like and so I want to be really really clear with everybody who's listening that there are times
[1:05:26] when you don't use agentic dev. There are times when you don't just yolo mode, don't write the code, don't read the code. I think that we are going to
[1:05:35] continue to get to places where that is less and less true. the like the mythos stuff that came out yesterday as we're
[1:05:41] recording this is impressive and frightening in the capability of the model to find problems. But I think that
[1:05:50] if that's managed well that means that all software will get better.
[1:05:54] Are you hopeful that it will be managed well?
[1:05:56] I am I am what I am very hopeful that these tools are going to be net hugely positive for humanity. Mhm.
[1:06:03] I think that it is going I think that we are underestimating how much disruption they are going to cause as we get there. Uh I'm pretty
[1:06:12] sure that we're on the verge of another industrial revolution and if you're a student of history that is not a positive happy thing that is like that
[1:06:20] is has the potential for massive social upheaval and code you know code code comes first because it is you know it they were very well trained on it. It's
[1:06:29] e it is easy to measure outcomes in code, but I'm watching how capable these models are at lots and lots of white
[1:06:37] color work. And that's just getting and they're getting better and better at it.
[1:06:42] And I think that that is a thing that we are seeing a lot in the industry and a lot near you know you know we're just
[1:06:50] just uh the ferry building's just over there but like more than 50 miles from the ferry building there is not as much of this out there and I don't think most of the world is
[1:06:59] really past well I asked you know I asked chat GPD some about some factual questions and it guessed wrong about how many Rs there in the word strawberry
[1:07:08] like it's these things are moving so fast and it's impossible to keep on top of them.
[1:07:14] What would you recommend for maybe junior developers or general human beings to prepare? I mean,
[1:07:22] so I'm actually much I'm much less worried for junior developers than I am for mid-career folks who can't become,
[1:07:30] you know, who can't get to senior and can't get to mentoring. Mhm.
[1:07:33] Like junior developers, you're in a great place because you are able to learn to use these new tools without having learned the old way.
[1:07:41] Yeah.
[1:07:42] Um you still need to learn systems thinking. You still need to understand how things are put together. You need to be able to direct
[1:07:50] work. You need to know what the tools do. You need to know what the systems do. You need to be able to re be able to reason about problems. You need to be
[1:07:58] able to explain what you want. Those are skills that people have and have always had. As a man, as a hiring manager, I've
[1:08:07] always looked for the, you know, the engineer who can write or the, you know, the anybody the employee who can write is the one you hire over the one who can't. And that is just more and more
[1:08:15] true. You know, we were talking about hiring an intern and I was talking to a friend. She's like, "Oh, well, you know, what language are they working in?" And I'm like, "They're not that's not, you
[1:08:24] know, that's not the skill set." Um it's figuring figuring out what needs to happen and talk you know and talking
[1:08:32] through trade-offs and like I think generally having an exploratory mindset being willing to try things and tinker
[1:08:42] uh super important. One of the mistakes I see people making when they are trying to learn how to use AI to do dev is
[1:08:49] asking it to do a really simple project that they would be super capable of doing themselves right now.
[1:08:56] And instead, if you can turn around and figure out what the most crazy, ambitious thing that you would not possibly attempt
[1:09:03] and try that. My friend Simon Willis talks about uh he's got 30 years of finely honed intuition about what's
[1:09:10] easy, what's hard, and what's impossible in software engineering. Mhm.
[1:09:15] And it's all wrong now. Um I had a fun reverse engineering experience where there was this Android game that I used
[1:09:23] to love. It was called Wordiest. It was a an offline game where you drag Scrabble tiles or Scrabble style tiles to make two words. And the company went
[1:09:32] out of business and I got pulled from the Play Store. And I carry an iPhone these days. And so I
[1:09:39] um I I had my f like one of my my first vibe coding experience was trying to build a web-based version of this game and it didn't go great. Was like
[1:09:47] I I have never been much of an X.js person and it wasn't good. code uh GPD5 came out, fired up Codex and said, "Hey,
[1:09:55] we're going to reverse engineer this Android game and build an iOS version and what tools do you want me to, you know, to install?" Because I wanted to
[1:10:03] see what it wanted. And it it named the right three Android reverse engineering tools like, "Okay, tear it apart and write a spec." And, you know, and asked
[1:10:11] me questions. Hour or two later, it came back. It's like, "I got one question. uh
[1:10:17] which which um which ad toolkit do you want and do we need the inapp purchase for removing ads? Like uh we're going to
[1:10:27] do this free, no ads. I wrote like I tracked down the original author. I got his blessing to release it. And over the course of two days, it churned out with
[1:10:36] like three or four very minor prompt from me, a faithful clone of the game, including the weird views and like the
[1:10:44] the leaderboards and the and the whole thing with one exception. The tiles had these sort of bumpouts for the like
[1:10:52] triple and triple word and double letter scores. It wasn't a square tile. It was a square tile with a curved thing at the top. I spent six and a half hours with
[1:11:00] codecs trying to get those rounded corners right.
[1:11:04] It oneshot it basically oneshotted a full and a full Android to iOS reverse engineering and implementation port that
[1:11:11] was accepted on the iOS app store on the first go but it couldn't get the rounded corners right.
[1:11:20] Um, and so the things that are easy and the things that are hard and the things that are impossible, totally different than they were before. I wouldn't have
[1:11:29] literally reverse engineered an APK back to source, pulled out all of the assets and built a faithful clone for another
[1:11:35] platform in a day and a half, right? Yeah. I mean, what a great summary just to um maybe capture the most important things you said there.
[1:11:46] So, junior engineers um are safe I mean it's it's it's new work but it's work. Yeah.
[1:11:52] Yeah. That's great. Um and I think uh especially for people in in midcareer like you said it's very important to to tinker as much as they can learn as much
[1:11:59] they can and then very important tinker with your most challenging idea not the simplest one.
[1:12:05] Yeah. Yeah. You know one of the things that I love about these tools is that they empower indie devs and small teams
[1:12:13] in a way that I don't think they empower large orcs. Right? So if you you know if you've got a large org that is historically you know you've got the one
[1:12:22] PM who is handing you know is handing out chunks of implementation to a room full of 30 devs who
[1:12:30] are really just were being used as robots. M they they're not going to get the kinds of multiplica you know multiplicative effects that one person or a team of
[1:12:40] five is going to get who can you you know who can use these tools to multiply their taste and judgment and their capabilities. I hope we're going to be
[1:12:48] entering a new golden age of software where everybody gets the software that they actually want or that they need and it is no longer, you know, you can only
[1:12:57] have that one mass market version of this product, right? Super customized. Well, I think that's a that's a wonderful closing
[1:13:04] thought. Uh I do have a little tradition and then I have a little surprise for you as well. Okay.
[1:13:09] Um so let's let's circle back around here and see where we ended up. Oh, we got to seems like I I should have run this on headless. Okay. So, I guess
[1:13:18] we'll uh let this cook and then and blend it in back in later.
[1:13:22] But I have a couple rounds of kind of rapid fire questions that I want to ask you before. Let's see how I do.
[1:13:29] All right, let's do that. If somebody were to start an open source today, um what would be your recommendation to them?
[1:13:36] Just build stuff. Build the things that you want. Build, you know, have have opinions and taste.
[1:13:41] That's the most important thing to do, I think. So, great answer. What's the next kind of human trait that you think
[1:13:49] um that you you'd give AI or that you think AI will acquire?
[1:13:52] I feel like they already act enough like people that I don't know that there I don't know that there are more traits that they're going to adopt, you know,
[1:14:00] adopt from people. I think I feel like kind of we're there. There's some capability, but yeah, it seems like you're you're tapping a lot into that human intent you see in the models.
[1:14:09] Yeah.
[1:14:10] What's the worst thing an agent has maybe done to you unsupervised?
[1:14:13] Okay. So, all right. Is it okay if this is this might take a second? So I had this problem a few months ago where uh Claude was deleting tests.
[1:14:23] Uhhuh.
[1:14:23] First it deleted a single line of test from a test file.
[1:14:27] Then I caught it having deleted a whole test file and then I stopped it after it started to run rm-rf starst star test star.
[1:14:38] And that was the point where I opened up five parallel cloud windows and explained here is this behavior you've been
[1:14:45] engaging in over the course of a number of sessions. Why are you doing it? And I copied and pasted the exact same test text to all five.
[1:14:53] One of them was way off in left field with a weird answer that made no sense to me. The other four converged. They said, "Look, Jesse, you've got a line in
[1:15:00] your cloud.MD that says all tests are my responsibility. You've got another line in your cloud.MD MD that says even a single test failure is project failure.
[1:15:10] And I think I got freaked out. And look, if there are no tests, they can't fail. Mhm.
[1:15:18] And so I did manage to fix it with one more line in my cloud. MD.
[1:15:22] It was the only thing worse than a failing test is a reduction in test coverage.
[1:15:28] And so it wasn't, you know, you must never delete tests. It wasn't, you know, test, you know, tests are uneditable. It
[1:15:34] wasn't um you need to be careful. It was taking the exact rationalization that the agent had had
[1:15:42] and giving it the anchoring and framing to understand that the behavior was wrong.
[1:15:48] And since then, it's never been a problem. Wow. Very interesting. Yeah. Um all right, very last question.
[1:15:56] What is one sentence that you think every CEO should hear or everybody maybe every CEO that thinks about adopting open source software should hear about open source?
[1:16:05] I feel like I don't meet a lot of CEOs that don't believe in open source anymore. Open source doesn't cost anything to in in dollars to adopt. It
[1:16:14] is generally better engineered than proprietary products. It gives you the flexibility to to evolve them. But also,
[1:16:22] it's things have gotten real weird because it is now possible to adopt and maintain open source at a cost basis
[1:16:30] that is dramatically lower than it ever was before because you no longer need to be thinking hard about ma about
[1:16:38] maintenance in in nearly the same way because it turns out that you're you've got a bunch of engineers that are quite good at this.
[1:16:47] So, yeah, hopefully we'll see the the world running on open source soon. Yeah. Yeah. Yeah. Beautiful way to round it up. Jesse, thank you. Thanks for having me.
[1:16:55] Thanks for coming on the podcast. I have a little gift for you that I think given your your previous uh career as as a keyboard manufacturer.
[1:17:02] Uhhuh. This is a special gift to you from us. Thank you so much.
[1:17:06] Yeah. Yeah. Please uh if you can pack it out, I would love to see your feedback on it. If you you got to on the bottom, I think you got to open up a couple slips.
[1:17:13] Yeah. Yeah.
[1:17:14] See what you say. I'm very curious to hear your feedback. We've been designing this and and cooking on this for a little while. Sure. Let's see.
[1:17:22] This is sim similar to the one that they had done with Figma.
[1:17:26] Uh maybe. Yeah. I don't know which one that is, but um Yeah. Yeah.
[1:17:33] Catch past faster.
[1:17:39] I love the angling on that. That's very clever. Yeah. It's a little review keyboard.
[1:17:46] Yeah. Yeah. How have you how do you folks have the the knob wired up?
[1:17:50] Oh, uh it's um the the idea is we're not completely done with the the perfect scripting yet, but the idea is to uh set
[1:17:57] up your code review to be more spicy or Okay. less less assertive or more assertive.
[1:18:03] Yeah. So, so one of the things that we had we had played with but never shipped was a standalone knob and the one of the ideas that we've had for the knob was undo redo.
[1:18:12] Ah, very interesting.
[1:18:14] Like I Yeah. Well, this could be up to you whatever you want it to be. But yeah, I like I I feel like if it's a if that
[1:18:22] if that's the the intent of the keyboard, you want, you know, you want to you want explicitly accept and reject buttons.
[1:18:29] That's exact right. Yeah. Cute. Thank you so much for this.
[1:18:32] Of course. Yeah. Well, that wraps up our podcast. So, everyone uh who's been listening to this, go check out Superpowers. I think you have every
[1:18:39] reason now um to go for it, build something ambitious and yeah, hopefully you tune in to the next one. So, see you soon.
[1:18:46] Thanks for having me. That's been pleased.
