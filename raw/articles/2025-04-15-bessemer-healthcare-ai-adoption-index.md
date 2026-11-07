---
title: "The Healthcare AI Adoption Index"
authors: ["Sofia Guerra", "Steve Kraus", "Atlas Editors"]
publisher: "Bessemer Venture Partners (Atlas), in partnership with Amazon Web Services and Bain & Company"
url: "https://www.bvp.com/atlas/the-healthcare-ai-adoption-index"
date_published: 2025-04-15
fulltext_source: web-extract
converter: curl + BeautifulSoup (headings, paragraphs, list items) on the article body; three chart images transcribed by hand
notes: |
  Fetched 2026-11-07 from the URL above with plain curl (HTTP 200). "Published on Apr 15, 2025" on the page.
  Byline: Sofia Guerra, Steve Kraus & Atlas Editors (both Bessemer partners; both formerly at Bain & Company).
  Survey: the page says "more than 400 leaders across Payer, Pharma, and Provider segments"; every chart
  footnote reads "Source: Bain GenAI Survey (N=408)". The page does not state fieldwork dates, survey mode,
  respondent countries, or how respondents were recruited.
  Not accessible: the full slide deck and the appendix are SlideShare embeds; the SlideShare embed returned
  a bot "Client Challenge" page, so they were not read. Bain's own page on the index
  (bain.com/insights/the-healthcare-ai-adoption-index/) returned HTTP 403 (Cloudflare). Neither was
  circumvented. A recorded presentation (YouTube embed) was not transcribed.
  Kept: the full article text (about 3,800 words) and a hand transcription of three of the 16 chart images
  (charts 1, 3 and 5, the ones carrying adoption and pilot-to-production figures). The alt texts of all 16
  chart images are listed at the end so the chart set can be re-located.
  Left out: author bios, related-reading cards, the disclaimer (Bessemer notes that companies discussed may
  be portfolio companies; Steve Kraus's bio lists a board seat at Qventus, a health-AI vendor).
---

# The Healthcare AI Adoption Index

*Sofia Guerra, Steve Kraus & Atlas Editors. Published on Apr 15, 2025.*

The healthcare industry has reached its AI inflection point, a technological shift mirroring the earlier transition to electronic health records (EHRs)—but this time unfolding at warp speed.

The changeover from paper to electronic health records spanned more than a decade, aided by the HITECH Act of 2009 , which paid incentives to doctors to adopt EHRs. Yet progress was slow, plagued by reticence to change and complex, disparate processes. In stark contrast, just two and a half years after LLMs became accessible to the masses, AI is now a top priority in healthcare. It’s shaping boardroom agendas, fueling startups (i.e., healthcare AI applications), and easing daily burdens for clinicians, scientists, and administrators. Curiosity has quickly turned into action, with a wave of experimentation underway to reinvent care delivery, diagnosis, and drug development.

Bessemer Venture Partners, in partnership with Amazon Web Services (AWS) and Bain & Company, surveyed more than 400 leaders across Payer, Pharma, and Provider segments to understand how healthcare buyers are approaching GenAI applications—what jobs-to-be-done they prioritize, how they’re making adoption decisions, and where their projects sit on the adoption curve.

## Recorded presentation

Unlike the earlier shift to EHRs, today’s GenAI innovation isn’t just coming from healthcare AI applications but rather from inside healthcare organizations themselves. Internal development teams are building their own tools by partnering with horizontal AI labs (i.e., Anthropic), Big Tech companies, or by procuring new solutions from incumbent systems of record and healthcare IT (HCIT) vendors.

We found that there is a flood of internally and externally developed GenAI proof of concept (POC) projects, but few make it to implementation at scale. Early-stage application layer startups must learn to navigate healthcare’s evolving go-to-market landscape, while buyers need to separate the signal from the noise and build dynamic AI strategies. This report is a snapshot of today’s healthcare AI landscape and we plan to continue tracking the adoption, evolution, and impact of these solutions. To that end, we give our “diagnosis” of the current state of opportunities with the AI Dx Index , which can help founders, buyers, and investors accurately assess where our industry is in the AI transformation curve and where the most significant areas for opportunity in the near term lie across nearly 60 jobs-to-be-done.

## Top takeaways

- AI adoption is accelerating, driven by internal teams co-developing with Big Tech and cloud providers—not just startups (i.e., healthcare AI applications).
- 60% of execs report AI budgets outpace IT spend, with funding decisions centralized within the C-suite.
- Only 30% of AI pilots reach production, held back by security, data readiness, integration costs, and limited in-house expertise.
- Startups have significant growth opportunities ahead: As of now, only 15% of AI projects involve vertical AI applications, and just 32% of executives believe GenAI solutions from startups are superior to those from large tech incumbents. Yet 48% of executives say they prefer working with startups over established players, highlighting the potential for startup founders to co-build and serve emergent AI strategies.
- Trust and outcomes matter most —procurement is shifting toward co-development as 64% of execs are open to co-developing with early-stage partners, particularly with those startups that show clear and attributable ROI.

## Full slide deck

## The state of AI adoption today

Healthcare organizations overwhelmingly see AI as a strategic priority—and they’re backing that belief with investment. In our survey, 95% of respondents said GenAI will be transformative, with 85% of Provider and 83% of Payer leaders expecting it to reshape clinical decision-making within three to five years. This is faster than we anticipated, given the industry’s regulatory complexity and low tolerance for error.

Across all segments, 84% believe AI will impact clinical decisions, 80% expect it to reduce labor costs through automation, and many see the potential for revenue gains. However, only 57% of Pharma executives believe AI will drive most new therapy discoveries in the next decade, reflecting the complexity and long timelines of drug development.

Executives are putting real money behind their AI ambitions; the data shows that there’s an upfront investment to AI innovation and staying ahead of the curve compared to competitors means starting yesterday. (We describe budgeting trends further below.) Still, it's early days. Only half of the organizations surveyed have a clear AI strategy, while 57% have an AI governance committee, and Payers are leading the way. That said, 54% are already seeing meaningful ROI within the first year of GenAI implementation.

To understand where GenAI can deliver the most impact, we surveyed executives on 59 key jobs-to-be-done across the healthcare value chain:

- 22 for Payers (claims, network, member, pricing)
- 19 for Pharma (preclinical, clinical, marketing, sales)
- 18 for Providers (care delivery, revenue cycle management)
We found that nearly half (45%) of the use cases across these jobs are still in the ideation or POC phase, with far fewer actually in production. For a full description and breakdown of adoption levels of use cases across these three segments, refer to the Appendix.

Providers are ahead in POC experimentation, while most Payer and Pharma use cases remain in the ideation phase. Unlike the EHR adoption wave of the last few decades , Providers haven’t had the need for regulation or government payments to incentivize them to adopt AI.

AI-powered ambient scribes for clinical documentation illustrate this rapid adoption. While EHRs improved data handling, they also increased administrative burden, creating an opening for AI. This wave is defined by speed, enthusiasm, and a focus on boosting productivity. Among providers surveyed, 30% have system-wide deployments, another 22% are in implementation, and another 40% are actively piloting solutions.

## Experimentation but not yet production

Many organizations are running dozens of GenAI POC projects at once, but only 30% of completed POCs have made it into production. Providers have the most projects making it into production among the segments we tracked, and large Providers in particular are leading the charge with 46% of their POCs going to production.

So why are so many organizations stuck in the experimentation phase? This wave of AI adoption has been driven by “test and learn” urgency, with boards and CEOs pushing teams to discover possible use cases. Mid-to-large Providers are the exception, as they are early adopters with more resources to bring AI into production.

Despite enthusiasm, executives across all segments pointed to four main barriers to scaling AI:

- Security concerns (61% Payer, 50% Provider, 52% Pharma)
- Lack of in-house AI expertise (41% Payer, 48% Provider, 52% Pharma)
- Costly integrations, especially for Payers (51% vs. 43% Providers, 49% Pharma)
- Challenges preparing AI-ready data, particularly in Pharma (47% vs. 41% Providers, 39% Payers)
However, budgeting has yet to be a roadblock to GenAI experimentation. According to the survey, 65% of AI projects are being funded through a centralized budget and 35% through departmental dollars. Most importantly, the majority across each segment stated that budget was not a barrier to scaling AI projects from POC into production scale. Healthcare systems and buyers know the urgency of AI and so budgets are being cleared for the sake of experimentation because of these strategic priorities.

On average, 60% of respondents (65% Payers, 57% Pharma, and 56% Providers) are seeing GenAI budgets growing faster than general IT budgets. C-suite leaders are at the helm, controlling the purse strings and determining 70% of the decisions on AI use cases. Given these dynamics, startups need to prioritize strategic relationships with the C-suite, no matter the end user. (More startup lessons later.)

## The development strategy

Many AI projects today are being developed in-house with horizontal AI labs and large tech partners. While startups are no longer the only source of innovation, healthcare AI entrepreneurs have the opportunity to reimagine how to work with buyers to serve emergent AI strategies.

Over half (54%) of executives we surveyed feel comfortable with and want to work with early-stage startups, but, on average, 48% prefer a more innovative startup over an established technology player and 55% of executives would only consider working with startups with proven track records. The takeaway? Startups must rethink their go-to-market strategy as they build market traction and prove results with peer healthcare organizations—healthcare buyers want innovation but are still risk-averse. It's the classic catch-22: You need social proof to sell, but you can’t get social proof until you do.

Less than 15% of projects are currently being developed at and procured from startups, as organizations believe they can build AI tools on their own or procure incremental AI features from incumbents. 51% of Payer projects are being developed internally, compared to 43% of Pharma projects and 27% of Provider projects, with variation by use cases.

Off-the-shelf models and horizontal automation platforms are great for creating simple minimum viable products (MVPs) and automated process improvements that don’t require consistent high accuracy. Startups, however, can offer more applications that are specific, specialized, and more accurate. (More best practices below in the “How to win” section.) We expect the failure rate of early-stage startups in this space to stabilize over time, in turn helping more healthcare AI startups gain traction with buyers.

Cloud infrastructure players are the core platform atop which AI-first applications are being developed—either by internal teams or startups—and we chose to partner with AWS on this report for its unique position in the health AI ecosystem. AWS and other cloud infrastructure partners can curate a list of best-in-class startups to work with, ensure security, and improve integration standardization and data readiness for AI applications. Two example programs include the AWS Partner Network and AWS Marketplace .

## How startups can win

If you’re an entrepreneur building in healthcare, here’s a hard pill to swallow: Buyers aren’t going to assume your tool is best-of-breed just because you’ve got some venture funding and an exciting pitch. Only 32% of our survey respondents agreed that startups have best-of-breed GenAI solutions that are superior to those developed by large technology incumbents. Startups are not just competing with other startups, but with a full ecosystem that includes potential buyers’ internal teams, horizontal AI labs, incumbent systems of record like Epic and Veeva, and HCIT companies deploying AI features.

Founders, here’s how your AI application startup can stand out in this increasingly crowded field in healthcare.

### 1. Pick the right entry point and expand

Winning startups don’t just sell a point solution, they land with a high-impact use case and then expand, adding capabilities to adjacent processes upstream or downstream of the core workflow. This enables a company to deepen touch points either by serving more needs of a particular user or by sitting at the intersection point between stakeholders (e.g., collaborations between internal teams or external parties, like payer-provider interactions).

### Introducing the AI Dx Index

To help AI startups prioritize healthcare use cases, we created the AI Dx Index, based on survey data. It factors in market opportunity, urgency, and current AI adoption to give startups a strategic edge when engaging healthcare buyers.

The Index includes three components:

- Opportunity Score: Measures pain and manual effort, calculated from the % of respondents citing a job as being both a major pain point and largely manual process.
- Adoption Score: Tracks where organizations are on the adoption curve using weighted averages across development stages, from "Not Yet Started" to "Full Rollout."
- Development Strategy: Shows who’s building solutions—startups, incumbents, or internal teams—highlighting areas where startups face the most entrenched competition.
Based on our survey data, here’s how we position these use cases on the index:

- Y-axis: Opportunity Score is calculated as the average of pain point intensity (percentage of respondents claiming a job is a significant pain point) and current level of automation (percentage of respondents of describing job as a mostly manual process);
- X-axis: Adoption Score is calculated using the weighted average of development stage where Not Yet Started is 0-20%% adoption and Implementation/Full Rollout is 80-100% adoption
As AI adoption increases, a use case moves to the right on the x-axis, and its opportunity may shrink as the problem gets solved and manual work is reduced.

Let’s look at documentation support (like AI scribes) as an example. This category has a high Adoption Score (53) because over 60% of organizations are already using it. While it's still a big pain point, especially around physician burnout, much of the manual work is already being automated, so its Opportunity Score is now in the medium range (43).

Sellers and buyers will view the 2x2 chart differently. Entrepreneurs and investors should focus on the top left, where high Opportunity Scores overlap with early AI adoption. Healthcare buyers, meanwhile, will gravitate toward the middle or top right, where solutions show traction—unless they’re open to co-developing early-stage projects.

When selecting the right entry point, prioritize use cases where you can access unique data, engage key stakeholders, and align with the appropriate budget owner. Also consider how mission-critical the process is—these high-impact areas offer significant opportunity but come with higher stakes and slower adoption. To succeed, your solution must demonstrate reliable, accurate results from day one.

Review slides below to see how each of the jobs-to-be-done surveyed score on the three components of the AI Dx Index.

### 2. Prove ROI quickly and navigate the POC trap

The best way to move beyond a POC is to show clear impact, which can start with case studies from similar environments or even other departments within the buyer’s organization.

Our research states the most compelling startups and organizations assess and measure ROI ahead of a POC or pilot by:

- Clearly defining non-financial metrics (e.g., time savings, clinical outcomes, employee Net Promoter Score) and tracking employee utilization and adoption that can serve as leading indicators of impact
- Clearly defining financial metrics (e.g., revenue uplift, cost savings) in a way that is attributed to the specific project
- Conducting a detailed study to understand how technology would change key workflows
- Defining frameworks and processes in partnership with your customer to assess risk to core processes and core system integrations
To avoid getting stuck in POC limbo, startups must demonstrate both financial and non-financial impact. We discovered that buyers expect fast results, with 60% of respondents across segments expecting to see positive ROI in under 12 months. And the onus will be on the startup to acknowledge its customer’s investment of time and resources—75% of survey respondents say startups fail to recognize the real cost of a POC. Lastly, startups must also get ahead of scaling challenges—like data governance, security, and integration—by involving key stakeholders early, including legal and IT.

### 3. Shift from traditional sales to co-development

We learned in this survey that a whopping 64% of buyers are willing to co-develop solutions with startups. “Co-development” in this context might look like embedding sales engineers and developers into the selling process. But how should startups shift from traditional healthcare go-to-market cycles to co-development without becoming glorified custom software development shops?

Enterprise healthcare buyers expect to have some level of control and ride shotgun with companies. Specifically, we mean:

- Successful healthcare AI startups position their platforms as builders alongside a customer by solving a core issue that rises to the C-suite agenda. In turn, customers will pull them into other problems or use cases upstream or downstream of the value chain for expansion.
- The workings of AI applications are often a black box to buyers, and so startups should make their models’ insights and output tractable and explainable.
- A startup’s relationship with healthcare buyers and users can benefit by allowing them to have input into product roadmaps. Startups should be hyper-focused on this product feedback and should then iterate quickly. These tactics will not only enable startup teams to build trust with buyers during the selling process but will also create super users across the organization who leverage the tools daily.

### 4. Reimagine a complex workflow end-to-end

To avoid the churn common in AI services , startups should position their product as a reimagined end-to-end workflow that evolves with customer needs, highlighting domain expertise over technical novelty.

Startups can build defensibility by investing in deep integrations with related software—especially when their solution connects multiple systems and handles novel data sources beyond a single record system. These integrations boost retention, reduce security risks, and set startups apart from incumbents limited to adding features within existing platforms.

We believe that within a year or two many internally built POCs will struggle to scale or deliver reliable accuracy, which will then prompt a shift toward proven solutions, often validated by peer case studies. While it’s easy to stitch together off-the-shelf models to build an MVP, sustaining 99% accuracy at scale is far harder. The more complex the process, the less effective horizontal tools become. That said, there’s still low-hanging fruit in single-step workflows ripe for general automation. Startups should target high-frequency, high-accuracy use cases and pair them with a seamless, user-friendly UI.

Finally, startups must lead with empathy. While buyers are eager to adopt AI, many face internal resistance from colleagues wary of disruption. Our survey revealed key barriers to full deployment: lack of in-house expertise, data readiness, security compliance, costly integrations, and added IT burden. Startups should position their tools as empowering—not replacing—teams, and explain deployment clearly, without technical jargon.

### 5. Align your business model to the value you create

Traditional healthcare software vendors have captured only a fraction of the value they create: Software makes up just <5% of healthcare administrative spend , limited by IT budgets and point-solution sales (aside from systems of record). However, GenAI offers a more scalable way to tap into the remaining 80–90%. The AI wave gives founders a real opportunity to align pricing and business models with the value they deliver.

We have written extensively about these new business models in the age of AI, and you can read about them here and here . A particularly intriguing business model that has emerged in this space is what we refer to as AI services-as-software , which allows you to get compensated for the work you provide. Aligning your model to the value you create underscores the importance of measuring clear, attributable ROI. Over time, we hope AI-first companies can tap into opex budgets—especially since, as the survey shows, funding isn’t a barrier when ROI is well-defined and continuously proven.

## How buyers can navigate the fast-evolving AI ecosystem

If you’re a healthcare executive reading this, you have likely been inundated by AI pitches given the rapid pace of innovation similar to the majority of our survey respondents. At the same time, you are likely under pressure to drive AI progress through managing dozens of projects and POCs.

We’ve developed a shortlist of principles to navigate common challenges, leveraging insights from our report partner Bain & Company, which advises hundreds of healthcare clients on AI strategy.

### 1. Foster a culture primed for AI adoption

Like any technological shift, success with AI requires behavioral change—especially in large organizations. While large companies have the resources to invest, they’re also held back by bureaucracy and legacy processes. And AI’s potential to disrupt workflows can spark fear, despite its promise.

Prime your organization for the potentially massive value that can be created and have strong change management plans in place to help drive adoption of new technology. For example, the CTO of a large health system we surveyed said it well: Storytelling, rather than imposition of a new technology, is required by AI champions to bring stakeholders across their business onboard. Leaders can help establish the willingness to experiment, and mid-level employees can showcase the benefits of AI-powered tools to their colleagues to help drive adoption.

### 2. Establish strong ecosystem relationships among agile partners — and be nimble yourself

Moving quickly and adapting as necessary is the name of the game. This involves collaborating with a range of different stakeholders, from foundational tech partners to agile startup partners. Given the pace of change, building all tools internally is unlikely to be a winning strategy for most organizations.

It is also critical to be nimble and adaptive yourself. We know this can be especially tough for large organizations, but AI is still in its early stages. Success depends on having a flexible strategy with clear priorities, making it easier to prioritize effort. And remember, not every AI project will succeed—many internal efforts and startups will fail. But some will thrive. Watch how your peers are partnering and use those case studies to guide your own decisions. Ecosystem partners can also help to make your governance, tech stack, and cybersecurity AI-ready while enforcing responsible AI policies.

### 3. Make AI adoption your competitive advantage

We know you’re feeling urgency (and you should be!), but don’t forget we are still very early in the AI journey, which will take us from today’s chatbots to AI systems that will one day be able to run organizations. Get ahead of your competitors by developing technology where differentiation matters, adopting tools across your organization and maximizing the value of your unique, proprietary data.

## Healthcare enters the era of AI co-development

AI is no longer a distant promise in healthcare. It’s already here, moving fast, and beginning to reshape how care is diagnosed, delivered, and managed. But unlike past waves of innovation, this one is defined by co-development, not just procurement.

Today, healthcare organizations aren’t simply buying AI—they’re building it, often in partnership with horizontal AI labs, cloud providers like AWS, and a select group of startups. Increasingly, they’re bypassing traditional IT budgets and vendors, tapping into services spend as AI becomes core to workforce productivity and operational performance.

The pace is staggering. Since AI’s watershed moment in 2023, many health systems are now running dozens of pilots at once. Yet most projects, whether startup-led or internally-developed, won’t scale. That’s expected. The winners will be those that:

- Embed deeply into workflows
- Deliver clear and measurable ROI
- Build trust with C-suite decision-makers
- Reimagine ways to solve complex problems end-to-end—not just automate the tasks.
Our AI Dx Index is designed to help founders and healthcare buyers identify the most promising use cases—those with the greatest pain points, lowest automation, and highest potential for transformation. Over time, we expect these scores to evolve as more projects move from ideation to implementation, and as the gap between hype and real value narrows.

The results of this research highlights healthcare’s inflection point. If you're a startup, buyer, or investor shaping this transformation, we want to hear from you. Let us know what you’re seeing, what’s working, and what we should be measuring next. Reach out to steve@bvp.com or sguerra@bvp.com—we’re ready to continue the conversation.


## Charts (transcribed from the page images)

**Chart 1. "Majority of executives have big aspirations and expectations on what GenAI use can do for the healthcare industry."** % of respondents expressing either "Agree" or "Strongly Agree" (Payer / Provider / Pharma):
GenAI will significantly transform how healthcare diagnosis/treatment decisions are made in the next 3-5 years: 83% / 85% / (not asked). GenAI use cases will drive FTE cost savings in the future: 85% / 78% / 79%. GenAI will significantly reduce admin burden my company faces in the next 3-5 years: 82% / 76% / 77%. GenAI use cases will drive incremental revenue in the future: 75% / 76% / 77%. GenAI will drive the majority of new therapy discoveries in the next decade: Pharma 57%.
Source: Bain GenAI Survey (N=408).

**Chart 3. "Most of the use cases are in experimentation phase, with Providers further ahead with more projects in POC stage vs. ideation."** Share of use cases by stage (Not started / Ideation / Proof of concept / Pilot / Implementation-Production), by use-case type:
Provider, Care: 22% / 21% / 26% / 22% / 9%. Provider, RCM: 22% / 25% / 26% / 19% / 7%.
Pharma, Preclinical: 21% / 29% / 26% / 18% / 7%. Pharma, Clinical: 11% / 30% / 30% / 21% / 9%. Pharma, Marketing & Sales: 23% / 30% / 25% / 18% / 4%.
Payer, Claims: 30% / 22% / 28% / 15% / 5%. Payer, Network: 9% / 35% / 24% / 29% / 3%. Payer, Member: 17% / 30% / 24% / 22% / 7%. Payer, Pricing: 15% / 50% / 20% / 15% / 0%.
(Read from a stacked area chart; the Payer column labels at the right edge are small and their assignment to rows is a best reading.)
Source: Bain GenAI Survey (N=408).

**Chart 5. "Only ~30% of completed proofs of concept make it into production with payer and provider being the most successful."** % of POCs reaching production:
Payer 31% on average (small 25%, medium 32%, large 36%). Pharma 24% on average (small 19%, medium 23%, large 28%). Provider 35% on average (small 27%, medium 40%, large 46%).
Bullets: large national payers with highest translation into production; medium payers closely behind with over 30% of POCs reaching production; pharma lags; <20% of POCs developed by small pharma/biotech reach production; providers taking the lead; almost half of POCs developed by large providers reach production.
Source: Bain GenAI Survey (N=408).

**Alt texts of the 16 chart images, in page order:** 1 majority of executives have big aspirations; 2 59 jobs to be done; 3 most of the use cases are in experimentation phase; 4 How this AI wave differs; 5 Only 30 percent of completed POCs make it into production; 6 executives cite roadblocks; 7 buy in is established with large budgets; 8 C-suite is in the driver seat; 9 while many organizations are open to working with startups; 10 majority of projects are developed internally; 11 Components of AI DX; 12 Provider use cases; 13 Key techniques to assess and measure ROI and Maximize POC success; 14 behavior change is particularly a challenge for large organizations; 15 organizations are learning that it's difficult to scale; 16 Being AI ready acknowledges that we are very early in the AI journey.
