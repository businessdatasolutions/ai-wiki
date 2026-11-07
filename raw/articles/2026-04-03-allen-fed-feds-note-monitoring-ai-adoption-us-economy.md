---
title: "Monitoring AI Adoption in the U.S. Economy"
authors: ["Jeffrey S. Allen"]
publisher: "Board of Governors of the Federal Reserve System (FEDS Notes)"
url: "https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html"
accessible_data_url: "https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-accessible-20260403.htm"
doi: "10.17016/2380-7172.4032"
date_published: 2026-04-03
fulltext_source: web-extract
converter: curl + BeautifulSoup HTML-to-markdown script on the page's #content block (python3 -I), links kept
notes: |
  Fetched 2026-11-07 with curl from the URL above (HTTP 200). Full note text kept: summary, Background, The
  Surveys, Estimated AI Adoption Rates, Firm Size, Industries, Intensive Margin, Potential Sources of
  Estimation Differences, Appendix (data sources with exact question wording), References, 12 footnotes,
  disclaimer. ~3,300 words of prose. Left out: site navigation and share buttons, and the duplicate
  figure-note blocks the page prints twice under each figure. The four figures are PNG images (linked, not
  saved). Their text descriptions from the separate "Accessible version" page are appended at the end, because
  they carry values the body text does not (legacy BTOS series ends at about 10%; new series about 18%).
  Two HTML tables with merged cells (Table 1 scope column, Table 3 two-level header) were flattened by hand;
  the flattening is marked in italics under each table. FEDS Notes are staff views, not Board policy (see the
  disclaimer at the end).
---

# Monitoring AI Adoption in the U.S. Economy

*FEDS Notes · Board of Governors of the Federal Reserve System · Jeffrey S. Allen · 3 April 2026 · DOI 10.17016/2380-7172.4032*

[Jeffrey S. Allen](https://www.federalreserve.gov/econres/jeffrey-s-allen.htm)[^1](#fn1)

This note uses three publicly available surveys with complementary target respondents to examine trends in AI adoption in the U.S. through 2025. Business survey data from the Census Bureau show that about 18 percent of firms have adopted AI as of year-end 2025. Prior to a methodological change in late 2025, the adoption rate grew by 68 percent for the year ending in September. Work-related Generative AI adoption reported by individuals in the Real-Time Population Survey stands at about 41 percent as of November, with the strongest growth occurring in the most recent quarter. Additionally, a November iteration of the Survey of Business Uncertainty, which targets senior leaders at U.S. firms, estimates that 78 percent of the labor force works at firms that have adopted AI, and about 54 percent works at firms that use LLMs. The biggest driver of variation in these estimates likely relates to differences in sampling distributions and units of analysis, but question framing, the materiality of reported usage, information asymmetries between different target respondents, and social desirability bias may play a role as well.

The survey data also show considerable heterogeneity across firm size and industry cohorts. Adoption appears to correlate with size, but adoption among the smallest firms is stronger than would be expected based on size alone. Further, among five peer industries that account for a large share of U.S. output and employment, the levels of AI uptake in the professional services and financial sectors stand out. Robust adoption in these high-value services sectors suggests that current AI usage may be most prevalent in cognitive and analytical work. The remainder of this note lays out some motivating factors for the analysis, examines trends in AI adoption in detail, elaborates on the sources of variation in the survey results, and identifies areas for future research.

#### Background

Among the many important questions surrounding the potential impact of AI on the economy, three have emerged as most pressing. How will AI affect productivity and employment? How sustainable are massive investments in AI infrastructure and firms (figure 1)? And which sectors are most vulnerable to AI disruption? While resolving these questions requires analysis beyond the scope of this note, the pace and pattern of AI adoption are important pieces of analytical context for researchers and policymakers working to understand them.

##### Figure 1. Features of the AI Investment Boom

![Figure 1. Features of the AI Investment Boom. See accessible link for data.](https://www.federalreserve.gov/econres/notes/feds-notes/figure1-4032.png)

Note: Top row - The capex numbers do not include leases. Middle row (left plot) – Key identifies in order from left to right. Middle row (right plot) - Prior to OpenAI's December 2025 capital raise, a secondary share sale completed in October 2025 enabled employees to sell shares at a $500 billion valuation. Bottom row (right plot) – Key identifies in order from top to bottom.
Source: S&P Capital IQ Pro; U.S. Bureau of Economic Analysis, retrieved from FRED
[Accessible version](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-accessible-20260403.htm#fig1)

In recent years, researchers have developed a range of surveys and other estimates that seek to quantify AI uptake in the U.S. economy. Crane, Green, and Soto (2025) examined 16 such surveys and found that, as of mid-2024, point estimates of work-related AI adoption rates ranged from about 5 to 40 percent. This analysis extends their work in two ways. First, I bring together findings from three high-quality surveys to assess trends in AI adoption through 2025 and heterogeneity across firm cohorts. Second, I expand on the potential sources of variation in the survey results to help researchers and policymakers better understand the nature of the estimates.

#### The Surveys

I track AI adoption using three surveys. The highest frequency of these is the Census Bureau's biweekly, firm-level Business Trends and Outlook Survey (BTOS), which has asked U.S. businesses about AI adoption and planned adoption since September 2023 (Buffington, Foster, and Shevlin, 2023; Bonney and others, 2024). In November 2025, the Census Bureau broadened the AI-related questions in the BTOS to include a firm's use of AI "in any of its business functions" (U.S. Census Bureau, 2025). Previously, the survey asked more narrowly about the use of AI in "producing goods or services." The second source is the individual-level Real-Time Population Survey (RPS), which has asked respondents about Generative AI (GenAI) adoption on a quarterly basis since August 2024 (Bick, Blandin, and Deming, 2026). The final source is the Survey of Business Uncertainty (SBU), which is fielded by the Federal Reserve Bank of Atlanta and targets business executives (Altig and others, 2022). Thus far, the SBU only posed the AI survey questions once, in November 2025, but the results are an important complement to the BTOS and RPS given the vantage point of the target respondents (Meyer and others, 2025; Yotzov and others, 2026). Comparing the results of the three surveys is useful because, as discussed further below, the reported adoption rates vary. The Appendix discusses the sources in more detail.

#### Estimated AI Adoption Rates

Figure 2 (left panel) presents trends in AI adoption among U.S. businesses based on the BTOS. Adoption stood at about 18 percent of firms at the end of 2025.[^2](#fn2) Prior to the question revision, the adoption rate had grown by 68 percent (3.9 percentage points) over the prior year but decelerated in Q2 2025. The BTOS also asks firms about planned usage over the next six months. At the beginning of 2025, around 9 percent of firms indicated that they planned to use AI within six months, and by the end of June, the adoption rate was in line with expectations. Over 20 percent of firms expect to use AI in the first half of 2026.

##### Figure 2. Trends in AI Adoption

![Figure 2. Trends in AI Adoption. See accessible link for data.](https://www.federalreserve.gov/econres/notes/feds-notes/figure2-4032.png)

Note: In November 2025, the Census Bureau revised the BTOS AI questions to focus on a firm's use of AI in "any of its business functions," rather than in "producing goods or services." Planned adoption refers to expected adoption over the next six months. See the Appendix for detailed question wording.
Source: U.S. Census Bureau, Business Trends and Outlook Survey (left); Real-Time Population Survey (right)
[Accessible version](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-accessible-20260403.htm#fig2)

While the firm-level BTOS focuses on AI adoption in general, the individual-level RPS asks about GenAI, specifically. The right panel of figure 2 shows that work-related GenAI adoption reported in the RPS stands at about 41 percent of the workforce, and non-work-related usage at about 50 percent of the population as of the latest survey in November 2025. These metrics grew by about 31 percent (9.7 percentage points) and 26 percent (10.4 percentage points), respectively, for the year ending in November. The most recent quarter saw the strongest growth in work-related adoption over the course of the RPS series.

The SBU estimates an employment-weighted firm AI adoption rate of around 78 percent and an LLM adoption rate of about 54 percent. In this context, employment weighting approximates the share of the labor force working at firms that have adopted AI. This weighting method helps account for the fact that large firms are the biggest employers in the U.S. Table 1 summarizes the estimated AI adoption rates in the three surveys. Later I discuss the drivers of variation in these estimates in detail.

##### Table 1. Summary of Estimated AI Adoption Rates

| Scope | Source | Date | Unit of Analysis | Estimation Type | Estimate (%) |
| --- | --- | --- | --- | --- | --- |
| AI | BTOS | Dec. 2025 | Firms | Firm-weighted percentage | 18 |
| AI | SBU | Nov. 2025 | Firms | Employment-weighted percentage | 78 |
| GenAI/LLMs | RPS | Nov. 2025 | Individuals | Share of labor force | 41 |
| GenAI/LLMs | SBU | Nov. 2025 | Firms | Employment-weighted percentage | 54 |

*(Scope cells spanned two rows in the HTML table; repeated here per row.)*

Sources: U.S. Census Bureau, Business Trends and Outlook Survey; Real-Time Population Survey; Federal Reserve Bank of Atlanta, Survey of Business Uncertainty

#### AI Adoption and Firm Size

The association between AI adoption and firm size could have several important implications for the economy. As noted above, the largest firms are the biggest employers in the U.S., so AI adoption initiatives by these organizations could accelerate diffusion in the workforce. Meanwhile, strong adoption by solo entrepreneurs and other micro-enterprises could indicate that AI is facilitating new business formation. More broadly, uneven adoption rates between firm size cohorts could have implications for industry competition and consolidation.

Figure 3 explores the association between AI adoption and firm size based on results from the BTOS and SBU. Both sources clearly show that the largest firms have the highest adoption rates. They also reveal interesting dynamics at the lower end of the size distribution. In the legacy BTOS series, adoption rates among the first three size cohorts depicted in figure 3 (left panel) were comparable. The initial surveys under the new BTOS series show a stronger association between firm size and adoption.[^3](#fn3) The SBU shows a similar pattern of AI adoption among the size classes but with more comparability among the two smallest cohorts. Interestingly, LLM adoption rates are comparable among all but the largest cohort.

##### Figure 3. AI Adoption and Firm Size: Distribution across Employee Size Classes

![Figure 3. AI Adoption and Firm Size: Distribution across Employee Size Classes. See accessible link for data.](https://www.federalreserve.gov/econres/notes/feds-notes/figure3-4032.png)

Note: Left plot - For comparability with the SBU, the left plot aggregates the first four employee count-based firm size cohorts published in the BTOS data into a single group (1-49 employees) using average adoption rates of the constituent groups. Right plot - Key identifies in order from left to right.
Source: U.S. Census Bureau, Business Trends and Outlook Survey (left); Federal Reserve Bank of Atlanta, Survey of Business Uncertainty (right)
[Accessible version](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-accessible-20260403.htm#fig3)

From the adoption metrics alone, it is hard to say whether AI-related gains are accruing disproportionately to the largest firms or whether AI is serving as an equalizer of sorts and helping smaller enterprises compete more effectively. Due to the scale of their operations and number of employees, larger firms have a higher probability than smaller ones of clearing the bar for responding affirmatively to a question about AI adoption, but the relative impact on their business may not be as high. Additionally, the relationship between size and adoption is confounded by several other variables, such as firm age. Published data do not enable presenting these types of interactions in detail, but Bonney and others (2024) and Yotzov and others (2026) generally find that younger firms, which are also more likely to be small, are active AI users. Relatedly, Dinlersoz, Dogan, and Zolas (2024) find that there was a discrete jump in AI-related business formation in 2023, following the launch of ChatGPT. Future research could build on these initial findings to examine the implications of AI adoption for competition and industrial organization.

#### AI Adoption across Industries

The ultimate impact of AI will likely depend on the extent to which it diffuses across important economic industries. Proponents have argued that AI can help a wide range of firms reduce operating costs and execute their business strategies more effectively. To this end, figure 4 shows trends in adoption among five industries that collectively make up four of the top five sectors by total output and three of the top five sectors by total employment (BLS, 2025b).[^4](#fn4) The manufacturing sector is considered a goods-producing industry, and the rest are as classified as part of the services sector, which is the dominant component of the U.S. economy.[^5](#fn5)

##### Figure 4. AI Adoption across Industries

![Figure 4. AI Adoption across Industries. See accessible link for data.](https://www.federalreserve.gov/econres/notes/feds-notes/figure4-4032.png)

Note: The industries depicted in the figure represent four of the top five by total output and three of the top five by total employment.
Source: U.S. Census Bureau, Business Trends and Outlook Survey (left); Real-Time Population Survey (right)
[Accessible version](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-accessible-20260403.htm#fig4)

The left panel of figure 4 presents results from the BTOS. The professional, scientific, and technical services ("professional services") and financial sectors stand out in terms of levels of adoption, at about 33 and 30 percent.[^6](#fn6) The jump in reported adoption between the new and legacy series ranged from 47 percent (10.6 percentage points) for professional services on the low end to 159 percent (7.5 percentage points) for manufacturing on the high end. The five industries had solid growth over the most recent year of the legacy series (median of 76 percent), but most showed some deceleration around Q2 2025. An exception is the financial sector, which reported sustained growth through the end of the legacy series, at 127 percent (9.3 percentage points) for the year ending in September. In line with the BTOS, the right panel of figure 4 shows that work-related GenAI adoption reported in the RPS is highest in the financial (63 percent) and professional services (62 percent) sectors.[^7](#fn7) Year-on-year growth in work-related adoption was strongest in the manufacturing sector at about 58 percent (14.5 percentage points) and was also robust in the financial and professional services sectors at around 30 percent.

Among the service sectors depicted in figure 4, financial and professional services are the highest value measured by output per employee. This suggests that early AI usage in the U.S. may be skewed toward more cognitive or analytical work, rather than commoditized services. Importantly, professional services is an eclectic group that includes lawyers, accountants, consultants, advertising agencies, engineers, and computer services firms, among others.Currently, the data do not enable investigating potentially interesting adoption heterogeneity among these sub-sectors. Additionally, the fact that the health care and social assistance sector lags behind the financial and professional services sectors may, in part, reflect the industry classification system. In particular, pharmaceutical companies and life sciences research firms, which are likely heavy AI users and are often thought of as part of the healthcare industry, are classified as manufacturing and professional services, respectively.

#### Intensive Margin

Beyond adoption rates, the intensity of AI usage can provide additional insight into workforce integration and the potential for efficiency gains. The RPS enables tracking aspects of intensive margin over time. Table 2 presents the most recent level, as well as the year-on-year change and percent change for any usage, daily usage last week, and at least one use last week. Weekly usage is comparable to the overall rate. Daily usage is less than a third of the overall rate but has grown at a similar pace. By comparison, a mid-2025 Gallup survey found that 8 percent of workers use AI daily (Pendell, 2025). In another nationally representative survey, Hartley and others (2026) found that, as of December 2025, 33 percent of workers who use GenAI—a narrower base—do so daily. The SBU also asked respondents how frequently they typically use AI in a given week and found that a plurality (35 percent) use AI up to one hour a week and more than a quarter (29 percent) use AI between 1 and 5 hours a week.

##### Table 2. Generative AI Usage at Work (November 2025)

| Frequency | Level | YoY Chg. | YoY pct Chg. |
| --- | --- | --- | --- |
| Any | 40.7 | 9.7 | 31.3 |
| Daily last week | 12 | 2.9 | 32 |
| At least once last week | 35.2 | 8.9 | 33.7 |

Source: Real-Time Population Survey (Bick, Blandin, and Deming, 2026)

While these sources provide some insight about the intensity of AI usage, an important question for understanding the sustainability of investments in AI infrastructure relates to the price and quantity of LLM token consumption by end-users. It is possible that the volume of tokens used in a few discrete areas, such as software engineering, could justify AI investment dynamics. There has been some early work by AI labs and other technology researchers to assess the emerging market for LLM tokens, but more research is needed to examine this related aspect of usage intensity.

#### Potential Sources of Estimation Differences

Table 1 shows that there are notable differences in the estimated adoption rates among the three surveys. There are several potential sources of variation. The most important relates to the survey goal, unit of analysis, and corresponding sample distribution. First, note that the gap between the RPS and SBU estimates of GenAI adoption is not very wide. An employment-weighted firm-level estimate, like the SBU, should generally be higher than an individual-level estimate because the former weights by employee headcount when calculating the average adoption rate across firms (Crane, Green, and Soto, 2025).[^8](#fn8) A material share of the gap between the RPS and SBU estimates likely relates to this weighting mechanism. Thus, the largest estimation differences are between these surveys and the BTOS.

Table 3 presents the sample distributions for the two firm-level surveys alongside the actual firm and employment distributions in the U.S. For comparability, the table aggregates several more granular firm size classes into the 1-49 employee group. The vast majority of firms in the U.S. are small. For additional context, about 57 percent of firms have fewer than five employees. By contrast, large firms are the biggest employers in the U.S. The BTOS generally mirrors the firm population distribution. Therefore, its firm-weighted estimate is likely a strong representation of the AI adoption rate across all U.S. businesses.

Meanwhile, the SBU sample distribution helps ensure that, in producing an employment-weighted estimate, the survey has stronger representation from the firms that have an outsized impact on the employment landscape.[^9](#fn9) We also know from the discussion above that the largest firms are the heaviest AI adopters. The different sampling distributions combined with adoption heterogeneity across firm size classes likely drives a considerable share of the gap between the BTOS and SBU estimates. The story is similar with respect to the differences between the BTOS and the RPS. Because the latter is a household survey, and given the distribution of employees across firms, a random sample of workers would draw greater representation from larger firms than the BTOS.

##### Table 3. Population and Sample Distributions by Firm Size Class

*(Two-level header in the HTML table: Population distributions = Firms, Employment; Sample distributions = BTOS, SBU. Percent.)*

| Firm size class (No. of employees) | Population: Firms | Population: Employment | Sample: BTOS | Sample: SBU |
| --- | --- | --- | --- | --- |
| 1-49 | 95 | 26.6 | 89.6 | 38.2 |
| 50-99 | 2.6 | 7.6 | 5.1 | 14.9 |
| 100-249 | 1.5 | 9.7 | 3.2 | 19.5 |
| 250+ | 0.9 | 56.2 | 2.2 | 27.4 |

Notes: The BTOS distribution is calculated using the average response counts for the final four surveys of 2025. The SBU distribution is calculated using the distribution of responses to the AI questions.

Sources: BLS (2025a); U.S. Census Bureau, Business Trends and Outlook Survey; Federal Reserve Bank of Atlanta, Survey of Business Uncertainty

A second potential source of variation revolves around question framing and the materiality of reported AI usage. Evolving taxonomy and rapid market developments have posed challenges for measuring AI adoption consistently over time. Further, the accessibility and general-purpose nature of modern GenAI tools have made it difficult to distinguish experimental, incidental or otherwise insignificant AI usage at work from more meaningful adoption patterns. The BTOS was originally designed to capture significant AI usage through more conservative question framing that focused on usage in producing goods and services (Bonney and others, 2024, pp. 3-4). Even with the recent question revision discussed above, it is possible that BTOS respondents are conditioned to understand the survey questions as referring to more material or extensive AI usage than what is covered in other surveys.

Information asymmetries between different target respondents could also play a role. Yotzov and others (2026) argue that the business executives that are surveyed in the SBU are in the best position to comment on a firm's AI usage. And indeed, Bonney and others (2024, p. 7) point out that some BTOS respondents may not be knowledgeable about AI usage at their firms, but most such respondents appropriately respond that they "do not know." In the four BTOS surveys leading up to year-end 2025, the "do not know" rate was about 10-11 percent of respondents. While meaningful, this knowledge gap is likely not the primary driver of the differences in estimates. Separately, early workplace GenAI surveys found that a non-trivial amount of AI usage among employees was occurring either without the knowledge or approval of IT or management (The Conference Board, 2023; Microsoft and LinkedIn, 2024). This could drive some differences in individual- and firm-level surveys, but given the high rates of adoption reported by business executives in the SBU, it is unlikely that this "shadow AI" usage is still a major driver of estimation differences, even if it is still a substantive problem for organizations.

Finally, social desirability bias could account for some of the estimation differences. The direction of such bias has likely evolved over the last few years. Soon after GenAI initially gained popularity, firm representatives or employees may have been biased against reporting AI usage as companies were focused on assessing the security implications of more accessible AI tools. Recently, though, firm representatives, especially senior leaders, may face pressure to report AI usage as an efficiency initiative. This could put upward pressure on estimates that target corporate leaders. Yotzov and others (2026) present parallel findings that have relevance for this. Notably, they find a large gap between senior leaders' and workers' perceptions about the potential productivity gains from AI and the future effects on employment, with the former projecting that gains will be stronger and employment will be lower. More research is needed to examine whether social desirability bias is meaningful in this context.

To conclude, each of the three surveys has slightly different goals and relative strengths and weaknesses. Which estimate researchers and policymakers look to depends on the question they are seeking to answer. The BTOS is the best source for an estimate of the percentage of U.S. businesses that have adopted AI. The RPS is the best source for an estimate of the share of the labor force that uses GenAI at work. Finally, the SBU, which estimates the share of the labor force working at firms that have adopted AI, is a good upper bound on the scope of access to AI tools at work.

#### Appendix: Data Sources

- **Business Trends and Outlook Survey**: The U.S. Census Bureau's Business Trends and Outlook Survey (BTOS) (Buffington, Foster, and Shevlin, 2023) is a fortnightly survey of 1.2 million U.S. businesses, in which cohorts of 200,000 firms are surveyed every 12 weeks. The sample resets every year, so that each firm in the sample receives 4-5 surveys. For the four surveys leading up to year-end 2025, the BTOS received about 20,000 responses on average. Beginning in September 2023, the BTOS included two questions about firms' AI adoption and planned adoption: "In the last two weeks, did this business use Artificial Intelligence (AI) in producing goods or services? (Examples of AI: machine learning, natural language processing, virtual agents, voice recognition, etc.)" and "During the next six months, do you think this business will be using Artificial Intelligence (AI) in producing goods or services?" (Bonney and others, 2024; U.S. Census Bureau, 2025, p. 1). In November 2025, the AI-related questions were modified to focus on a firm's use of AI "in any of its business functions" (U.S. Census Bureau, 2025, p. 1). Data are obtained from the Census Bureau's BTOS website.[^10](#fn10)

- **Real-Time Population Survey**: The GenAI module in the Real-Time Population Survey (RPS) (Bick, Blandin, and Deming, 2026) has asked respondents various questions about GenAI usage at home and at work on a quarterly basis since August 2024. The RPS is designed to be nationally representative, and the GenAI module typically receives between 5,000-6,000 responses. The survey defines GenAI as "a type of artificial intelligence that creates text, images, audio, or video in response to prompts. Some examples of Generative AI include ChatGPT, Gemini, and Midjourney," and the core GenAI adoption question asks, "Do you use Generative AI for your job?" (Bick, Blandin, and Deming, 2026, p. 3). Data are obtained from the study's Generative AI Adoption Tracker.[^11](#fn11)

- **Survey of Business Uncertainty**: The Survey of Business Uncertainty (SBU) is a monthly survey targeting U.S. business executives carried out by the Federal Reserve Bank of Atlanta and developed in collaboration with Steven Davis (Hoover Institution) and Nicholas Bloom (Stanford) (Altig and others, 2022). In November 2025, the SBU included questions about AI usage at respondents' firms (Meyer and others, 2025; Yotzov and others, 2026). It received 1,032 responses. The core AI adoption metrics are derived from a question that asks respondents about their firm's use of seven categories of AI technologies: "Autonomous vehicles, Data processing using machine learning, Image processing using machine learning, Robotics, Text generation using large language models, Visual content creation, Other" (Meyer and others, 2025, p. 9). Data are obtained from the Atlanta Fed's SBU website.[^12](#fn12)

#### References

Altig, David, Jose Maria Barrero, Nicholas Bloom, Steven J. Davis, Brent Meyer, and Nicholas Parker (2022). "Surveying business uncertainty." Journal of Econometrics, 231(1): 282-303, https://doi.org/10.1016/j.jeconom.2020.03.021.

Bick, Alexander, Adam Blandin, and David J Deming (2026). "[The rapid adoption of generative AI](https://doi.org/10.1287/mnsc.2025.02523)." Management Science.

Bonney, Kathryn, Cory Breaux, Cathy Buffington, Emin Dinlersoz, Lucia S Foster, Nathan Goldschlag, John C Haltiwanger, Zachary Kroff, and Keith Savage (2024). "[Tracking firm use of AI in real time: A snapshot from the Business Trends and Outlook Survey (PDF)](https://doi.org/10.3386/w32319)." National Bureau of Economic Research, No. 32319.

Buffington, Catherine, Lucia Foster, and Colin Shevlin (2023). "[Measuring business trends and outlook through a new survey](https://doi.org/10.1257/pandp.20231051)." AEA Papers and Proceedings, 113: 140-144.

Bureau of Labor and Statistics (BLS) (2025a). [Business Employment Dynamics: Data By Firm Size Class](https://www.bls.gov/web/cewbd/table_f.txt).

Bureau of Labor and Statistics (BLS) (2025b). [Industry Output and Employment.](https://www.bls.gov/emp/data/industry-out-and-emp.htm)

Crane, Leland, Michael Green, and Paul Soto (2025). "[Measuring ai uptake in the workplace](https://doi.org/10.17016/2380-7172.3724)." FEDS Notes. Washington: Board of Governors of the Federal Reserve System.

Dinlersoz, Emin, Can Dogan, and Nikolas Zolas (2024). "[Starting up ai](https://ideas.repec.org/p/cen/wpaper/24-09.html)." Center for Economic Studies, U.S. Census Bureau, 24-09.

Hartley, Jonathan, Filip Jolevski, Vitor Melo, and Brendan Moore (2026). "The labor market effects of generative artificial intelligence." Available at SSRN, https://dx.doi.org/10.2139/ssrn.5136877.

Meyer, Brent, Jose Maria Barrero, Nicholas Bloom, Steven J. Davis, Kevin Foster, and Emil Mihaylov (2025). "[Survey of business uncertainty monthly report (PDF)](https://www.atlantafed.org/-/media/Project/Atlanta/FRBA/Documents/datafiles/research/surveys/business-uncertainty/monthly-report/2025/2025-12.pdf)." Federal Reserve Bank of Atlanta.

Microsoft and LinkedIn (2024). "2024 work trend index annual report," https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part.

Pendell, Ryan (2025). "AI use at work has nearly doubled in two years." Gallup, https://www.gallup.com/workplace/691643/work-nearly-doubled-two-years.aspx.

The Conference Board (2023). "[Majority of US workers are already using generative ai tools](https://www.conference-board.org/press/us-workers-and-generative-ai)." Press Release, September 12.

U.S. Census Bureau (2025). "[BTOS ai core questions update (PDF)](https://www.census.gov/hfp/btos/downloads/AI%20Question%20Wording%20Updates.pdf)".

Yotzov, Ivan, Jose Maria Barrero, Nicholas Bloom, Philip Bunn, Steven J. Davis, Kevin M. Foster, Aaron Jalca, Brent H. Meyer, Paul Mizen, Michael A. Navarrete, Pawel Smietanka, Gregory Thwaites, and Ben Zhe Wang (2026). "Firm data on AI." National Bureau of Economic Research, No. 34836, https://doi.org/10.3386/w34836.

1. Email: [[email protected]](https://www.federalreserve.gov/cdn-cgi/l/email-protection#553f3033337b343939303b153327377b323a23). I would like to thank David Mills, Sonja Danburg, Seung Jung Lee, Leland Crane, Paul Soto, Molly Mahar, and Jean Timmerman of the Federal Reserve Board, Alexander Bick of the St. Louis Fed, and Brent Meyer of the Atlanta Fed for their feedback. The note also benefited from discussions with Lucia Foster and Kathryn Bonney of the U.S. Census Bureau. The views expressed in this paper are solely those of the author and should not be interpreted as reflecting the views of the Federal Reserve Board. [Return to text](#f1)

2. I use a 4-period moving average for all BTOS calculations to help account for the way the survey is administered to firm cohorts (see the Appendix for a description) and to smooth out volatility in biweekly point estimates. [Return to text](#f2)

3. Figure 3 aggregates several more granular firm size classes in the BTOS for comparability with the SBU results. When broken out across seven employee size groups, the relationship between firm size and adoption in the legacy BTOS series was consistently U-shaped (Bonney and others, 2024), with highest rates of adoption among firms in the largest (250 or more employees) and smallest (1 to 4 employees) cohorts. This pattern has moderated in the new BTOS series, with the smallest cohort showing comparable rates of adoption to the two other cohorts with less than 20 employees and clearly lower rates of adoption than the larger size classes. [Return to text](#f3)

4. The five sectors depicted in figure 4 account for about 43 percent of both total output and wage and salary employment (BLS, 2025b). The other top five output and employment constituents are Accommodation and Food Services, which is the fourth largest employer, and State and Local Government, which is in the top five on both dimensions. [Return to text](#f4)

5. For the distinction between goods-producing and service-providing industries, see: U.S. Bureau of Labor Statistics, [Industries at a Glance](https://www.bls.gov/iag/tgs/iag07.htm). [Return to text](#f5)

6. The average adoption rates under the new BTOS series for the four surveys leading up to year-end 2025 for other selected industries include: Accommodation and Food Services (8 percent), Wholesale Trade (13 percent), Real Estate and Rental and Leasing (24 percent), and Information (37 percent). [Return to text](#f6)

7. The latest adoption rates reported in the RPS for individuals working in other selected industries include: Accommodation and Food Services (21 percent), Wholesale Trade (48 percent), Real Estate and Rental and Leasing (58 percent), and Information (70 percent). [Return to text](#f7)

8. An example of the employment weighting method is taking a weighted average of estimates for a group of firm cohorts, where the weights are the number of employees in each cohort. [Return to text](#f8)

9. The SBU also publishes equal-weighted AI and LLM adoption rates for its sample of 69.4 percent and 46.4 percent. [Return to text](#f9)

10. See: U.S. Census Bureau, [Business Trends and Outlook Survey](https://www.census.gov/hfp/btos/data_downloads). [Return to text](#f10)

11. See: The Project on Workforce, Generative AI Adoption Tracker, https://www.genaiadoptiontracker.com/. [Return to text](#f11)

12. See: Federal Reserve Bank of Atlanta, [Survey of Business Uncertainty](https://www.atlantafed.org/research-and-data/surveys/business-uncertainty), . [Return to text](#f12)

Allen, Jeffrey S. (2026). "Monitoring AI Adoption in the U.S. Economy," FEDS Notes. Washington: Board of Governors of the Federal Reserve System, April 03, 2026, https://doi.org/10.17016/2380-7172.4032.

***Disclaimer:** FEDS Notes are articles in which Board staff offer their own views and present analysis on a range of topics in economics and finance. These articles are shorter and less technically oriented than FEDS Working Papers and IFDP papers.*

---

## Appended: figure descriptions from the page's "Accessible version"

### Figure 1. Features of the AI Investment Boom

Top row: Capital Expenditure at Major Technology Firms. The left plot presents aggregate quarterly capex at Amazon, Google, Meta, Microsoft, and Oracle. The right plot shows capex for the same firms for the four quarters ending in a given period, expressed as a percentage of seasonally-adjusted and annualized nominal GDP. Capex reached $131 billion in Q4 2025 on a quarterly basis and $412 billion for the year, representing about 1.31 percent of U.S. GDP. Middle row: Investments in Leading AI Labs. The left plot captures new capital raised by Anthropic and OpenAI between 2023 and 2025. The right plot captures post-money valuations based on funding rounds for the two firms in the same years. Anthropic and OpenAI raised $44 and $58 billion over the period and were valued at $350 and $500 billion at year-end 2025. Bottom row: Growth in Market Capitalization of AI Chip Firms. The left plot shows that the market capitalizations of AMD (red dotted line), Broadcom (gray dashed line), and Nvidia (solid blue line) grew by 179 percent, 636 percent, and 975 percent, respectively, between the launch of ChatGPT in late 2022 and year-end 2025. The right plot shows that their collective share of the S&P 500 market capitalization was 11.2 percent at the end of 2025, down from a high of 12.4 percent in October 2025.

### Figure 2. Trends in AI Adoption

The figure presents trends in AI adoption across the U.S. The left plot tracks adoption by U.S. businesses as measured by the Census Bureau's biweekly Business Trends and Outlook Survey on a 4-period moving average basis. The legacy time series is depicted to the left of the vertical dashed line. Adoption (solid gray line) and planned adoption (blue dashed line) rates grew by about 6 and 7 percentage points, respectively, over the legacy series with most recent observations of about 10 and 14 percent. The gray circle (adoption) and blue square (planned adoption) to the right of the dashed line depict the moving average for the four observations in the new series leading up to year-end 2025, which stand at about 18 and 21 percent. The right plot presents trend in non-work (solid gray line) and work-related (blue dashed line) GenAI adoption by adults and workers in the U.S. from August 2024 through November 2025 based on the quarterly Real-Time Population Survey. The series have risen from 36 and 33 percent, respectively, to 50 and 41 percent.

### Figure 3. AI Adoption and Firm Size: Distribution across Employee Size Classes

The left plot presents trends in AI adoption by U.S. businesses based on the BTOS for four employee size classes: 1-49 (gray line and circle), 50-99 (blue dashed line and square), 100-249 (dark blue dotted line and triangle), and 250+ (red dash-dot line and diamond) enterprises. In the legacy series, adoption was highest in the largest group and comparable for the other three groups. On average, the first four surveys of the new BTOS series show a stronger association between adoption and firm size. The right bar plot presents AI adoption (gray bars) and LLM adoption (blue bars) for the same employee size cohorts, as estimated in the November 2025 SBU. Adoption patterns are similar to the BTOS, but there is more comparability among the smaller cohorts, especially for LLM adoption.

### Figure 4. AI Adoption across Industries

The left plot depicts trends in AI adoption by U.S. businesses based on the BTOS for professional services (gray line and circle), finance and insurance (blue dashed line and square), health care and social assistance (dark blue dotted line and triangle), manufacturing (red dash-dot line and diamond), and retail trade (orange long dashed line and pentagon) firms. Adoption rates are highest in the professional services and financial sectors, and growth has been strongest in the latter. The right plot tracks work-related GenAI usage reported by individuals in the RPS for the professional services (solid gray line), finance and insurance (blue dashed line), health care and social assistance (dark blue dotted line), manufacturing (red dash-dot line), and retail trade (orange long dashed line) sectors. Usage is highest in the financial and professional services sectors. Year-on-year growth has been strongest in the manufacturing sector.

