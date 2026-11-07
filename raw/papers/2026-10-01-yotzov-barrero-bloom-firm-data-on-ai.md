---
title: "Firm Data on AI"
authors: ["Ivan Yotzov", "Jose Maria Barrero", "Nicholas Bloom", "Philip Bunn", "Chanya Chawla", "Steven J. Davis", "Kevin M. Foster", "Aaron Jalca", "Brent H. Meyer", "Paul Mizen", "Michael A. Navarrete", "Samil Oh", "Katia Garcia Loredo", "Monique Reid", "Pawel Smietanka", "Gregory Thwaites", "Ben Zhe Wang"]
publisher: "National Bureau of Economic Research (NBER Working Paper 34836)"
date_published: 2026-10-01
date_first_issued: 2026-02-16
doi: "10.3386/w34836"
url: "https://www.nber.org/papers/w34836"
pdf_url: "https://www.nber.org/system/files/working_papers/w34836/w34836.pdf"
attachment: 2026-10-01-yotzov-barrero-bloom-firm-data-on-ai.pdf
version: "February 2026, Revised October 2026 (third version)"
fulltext_source: pdf-converted
converter: pdftotext -layout
notes: |
  Fetched 2026-11-07 from the NBER PDF URL above (the current version on the paper page). 86-page PDF
  (created 2026-10-17, modified 2026-10-21). The cover says "February 2026, Revised October 2026"; the NBER
  page gives only "Revision Date October 2026", so the day is unknown and the filename uses -01.
  Working paper with no TOC: body pp. 4-26 (printed pp. 2-24), references, figures, tables, Appendices A-C
  (Appendix C, Bank of Korea survey, ends on printed p. 84). Complete. Printed page = PDF page - 2.
  Version history on the NBER page: first version 2026-02-24 (rev0, 70 pp., "almost 6000" executives, four
  countries, ~70%/69% of firms use AI), second 2026-03-19 (rev1, 70 pp., same data, 69%), this third version
  (Summer 2026 wave, seven countries, "nearly 9,000", 78%). Footnote 13 (PDF p. 15): US adoption was 78% in
  the first version because firms that skipped the question were coded as non-users; now treated as missing,
  giving 94% (Nov 2025) and 95% (June 2026). The employee survey of rev0/rev1 is not in this version.
  pdftotext flattens the figures; bar values are legible as numbers but verify against the PDF.
---

                               NBER WORKING PAPER SERIES



                                       FIRM DATA ON AI

                                          Ivan Yotzov
                                       Jose Maria Barrero
                                        Nicholas Bloom
                                          Philip Bunn
                                         Chanya Chawla
                                         Steven J. Davis
                                        Kevin M. Foster
                                           Aaron Jalca
                                         Brent H. Meyer
                                           Paul Mizen
                                      Michael A. Navarrete
                                            Samil Oh
                                      Katia Garcia Loredo
                                         Monique Reid
                                        Pawel Smietanka
                                        Gregory Thwaites
                                         Ben Zhe Wang

                                       Working Paper 34836
                               http://www.nber.org/papers/w34836


                      NATIONAL BUREAU OF ECONOMIC RESEARCH
                               1050 Massachusetts Avenue
                                  Cambridge, MA 02138
                           February 2026, Revised October 2026

We would like to thank the Economic and Social Research Council, Smith Richardson Foundation
and Stanford Impact Labs for funding. We are grateful to Crystal Arnburg for her valuable
contributions to the development and implementation of the Canadian survey component of this
project. Any views expressed are solely those of the individual authors and so cannot be taken to
represent those of the National Bureau of Economic Research, the Federal Reserve Bank of
Atlanta, the Federal Reserve System, Bank of England, Bank of Canada, Bank of Korea, Banco de
Mexico, South African Reserve Bank, or Bundesbank.

At least one co-author has disclosed additional relationships of potential relevance for this
research. Further information is available online at http://www.nber.org/papers/w34836

NBER working papers are circulated for discussion and comment purposes. They have not been
peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies
official NBER publications.

© 2026 by Ivan Yotzov, Jose Maria Barrero, Nicholas Bloom, Philip Bunn, Chanya Chawla,
Steven J. Davis, Kevin M. Foster, Aaron Jalca, Brent H. Meyer, Paul Mizen, Michael A.
Navarrete, Samil Oh, Katia Garcia Loredo, Monique Reid, Pawel Smietanka, Gregory Thwaites,
and Ben Zhe Wang. All rights reserved. Short sections of text, not to exceed two paragraphs, may
be quoted without explicit permission provided that full credit, including © notice, is given to the
source.
Firm Data on AI
Ivan Yotzov, Jose Maria Barrero, Nicholas Bloom, Philip Bunn, Chanya Chawla, Steven J.
Davis, Kevin M. Foster, Aaron Jalca, Brent H. Meyer, Paul Mizen, Michael A. Navarrete,
Samil Oh, Katia Garcia Loredo, Monique Reid, Pawel Smietanka, Gregory Thwaites, and
Ben Zhe Wang
NBER Working Paper No. 34836
February 2026, Revised October 2026
JEL No. C83, D22, D84, J23, J24

                                           ABSTRACT

We survey nearly 9,000 CFOs, CEOs and senior executives at firms in the US, UK, Germany,
Australia, Canada, Mexico and South Africa in Summer 2026 on AI adoption and its effects on jobs
and productivity. We establish four key facts. First, 78% of firms use AI, with US firms expecting to
spend $2,000 per employee on AI-related expenditures in 2026, implying around $300 billion in
aggregate annual firm spending. This AI spending is highly concentrated, with just 2% of firms
accounting for over 50%of total spending. Second, 80% of executives report regularly using AI,
with an average use of 2.1 hours per week, up from 1.5 hours per week in Winter 2026,
highlighting the rapid growth in managerial AI use. Third, executives report that AI has had
essentially no net effect on firm employment over the last 3 years, and predict little net impact over
the next 3 years. These small net effects, however, mask considerable job churn: more than 40% of
firms anticipate positive or negative employment effects that roughly offset only in the aggregate.
Fourth, executives report AI adoption has raised annual labor productivity growth by 0.2% over the
last 3 years, a modest impact, but expect a substantially larger 0.6% per annum boost over the next
3 years.

Ivan Yotzov                                       Chanya Chawla
Bank of England                                   Bank of Canada
Ivan.Yotzov@bankofengland.co.uk                   CChawla@bank-banque-canada.ca

Jose Maria Barrero                                Steven J. Davis
Instituto Tecnológico Autónomo                    Stanford University
de México (ITAM)                                  Hoover Institution
Business School                                   and NBER
jose.barrero@itam.mx                              stevend5@stanford.edu

Nicholas Bloom                                    Kevin M. Foster
Stanford University                               Federal Reserve Bank of Atlanta
Department of Economics                           kevin.foster@atl.frb.org
and NBER
nbloom@stanford.edu                               Aaron Jalca
                                                  Federal Reserve Bank of Atlanta
Philip Bunn                                       aaron.jalca@atl.frb.org
Bank of England
Philip.Bunn@bankofengland.co.uk
Brent H. Meyer
Federal Reserve Bank of Atlanta
brent.meyer@atl.frb.org

Paul Mizen
King's College London
Department of Economics
Paul.Mizen@kcl.ac.uk

Michael A. Navarrete
Federal Reserve Bank of Atlanta
mnavarrete.econ@gmail.com

Samil Oh
Bank of Korea
samil.oh@bok.or.kr

Katia Garcia Loredo
Banco de México
katia.garcia@banxico.org.mx

Monique Reid
South African Reserve Bank
Monique.Reid@resbank.co.za

Pawel Smietanka
Deutsche Bundesbank
pawel.smietanka@bundesbank.de

Gregory Thwaites
University of Nottingham
gregorythwaites@gmail.com

Ben Zhe Wang
Macquarie University
ben.wang@mq.edu.au




Aggregated statistics for the charts are available at https://bit.ly/4B2zU5c
A project website is available at https://www.firmdataai.com/
1. Introduction
There has been a recent surge in interest around the potential economic effects of AI, with a 20-fold
surge in media focus since 2020 alone. 1 A variety of sources, including surveys, Census data, and
job postings, yield data on AI adoption rates (e.g., Acemoglu et al. 2022a, 2022b, Baslandze et al.
2026, Bonney et al. 2024, McKinsey 2025). Estimates can differ by more than a factor of ten across
studies, possibly because they differ in terms of samples, representativeness, and the nature of the
responses.2 Few sources capture the views of senior business executives, who make the strategic
decisions on AI adoption and have the best line of sight on how AI will affect their own firms in the
next few years. But senior business executives are particularly likely to have informed views about
what is happening in their own firms.

So to collect timely data on the impact of AI, we run surveys every 6 months on senior business
executives (CEOs, CFOs, and senior finance managers) about AI usage and its effects at their own
firms over the past three years and, looking ahead, what they anticipate over the next three years.
We then aggregate their responses. We first fielded parallel survey questions to representative
samples of senior executives in the US, UK, Germany, and Australia between November 2025 and
January 2026. We ran a second wave between May and July 2026, adding data from Canada,
Mexico, and South Africa in addition to the original four countries.

Our surveys yield four key results.

First, AI technologies are already in wide use and spreading rapidly. On average, across the seven
countries surveyed in mid-2026, 78% of businesses currently use some AI technology. At the
beginning of 2026, 69% did. The most commonly cited uses are ‘Generative AI’ followed by ‘visual
content creation’ and ‘data processing using machine learning’. We also find substantial
heterogeneity in the use of AI technologies. Larger, more productive, and higher-paying firms are
more likely to deploy AI technologies. Older firms and those with older directors have lower usage
rates. Looking ahead, 82% of executives expect their firms to use some form of AI in the next three
years.



1
  See, for example, the AI media coverage index available here: https://www.policyuncertainty.com/aieu_daily.html
2
  For example, McKinsey (2025) estimate around 88% of businesses use AI in a paid internet survey. Bonney et al.
(2024) estimate that around 9% used AI based on the US Census Business Trends and Outlook Survey (BTOS). The
ten-fold difference between these sources illustrates challenges with survey data on AI adoption by businesses. It is not
clear whether the McKinsey survey's respondents come from a representative sample of businesses. BTOS does have a
representative sample of US firms, but the respondents might not be executives who are informed about the firm's
strategic adoption of AI and its potential effects on the business

                                                           2
Many businesses are spending sizable amounts on AI adoption. In the US about 30% of businesses
plan to spend more than $1,000 per employee on AI in 2026. In the UK the number is 13%. Average
AI expenditures per employee amount to about $2,000 in the US and $725 in the UK, including AI-
related expenditures on software, subscriptions to AI services, hardware, worker training, and IT
staff support.

Strikingly, there is extremely wide dispersion in AI spending, with the top 2% of UK and US firms
accounting for over 50% of total businesses spending on AI. Thus, AI spending appears to be
extremely concentrated in just a handful of firms, much more concentrated than say employment or
capital expenditures.

Second, four-fifths of survey respondents themselves use AI technologies in the typical working
week, with an average use of around 2.1 hours per week by mid-2026. Average weekly use has also
increased since the start of the year, when respondents reported using AI around 1.5 hours per week.

Third, more than 80% of executives report that AI has had no effect on employment at their own
firms over the past three years. The remaining respondents report small and largely offsetting
increases and decreases, implying a near-zero average effect of AI adoption on employment over
this period.

Looking ahead, executives expect AI to reduce employment at their own firms by an average of
around 0.4% over the next three years. This projected decline is modest and reflects only incumbent
firms; employment creation at new firms could offset some or all of it. The small average effect also
masks substantial variation across firms: more than 40% expect AI to lead to increases or decreases
in employment. Although these anticipated changes largely offset one another at the aggregate level,
they suggest that AI could drive considerable job creation and destruction. Hence, AI could reshape
the distribution of employment across firms, generating major labor market churn, while leaving
overall employment levels broadly unchanged

Fourth, executives report a rising impact of AI adoption on their own firm's labor productivity (sales
per employee). Over the last 3-years they estimate that AI-adoption has boosted labor productivity
growth by 0.2% a year. This is twice the reported impact (of 0.1%) in our survey run 6 months ago.
The share of executives that report no impact of AI on productivity dropped from 89% to 83%, and
the share that report positive impacts almost doubled, going from 8% to 15%.

Looking forward over the next 3 years executives anticipate larger future effects on productivity.


                                                  3
They forecast AI will increase annual productivity growth by 0.6% on average, a large impact given
average productivity growth of around 1% to 2% in Europe and North America. If correct, these
predictions imply a sizable improvement relative to a long period of weak productivity growth in
many advanced economies (Bloom et al. 2020, and Goldin et al. 2024). Executives of larger and
higher-paying firms anticipate greater productivity gains from AI, as do those in the information,
communications, finance, and insurance sectors. Executives from the US, UK, and Canada foresee
stronger AI productivity boosts than those in other countries we cover.




Related Literature Our paper relates to four strands of the rapidly growing literature on AI
technologies.

First, we build on studies that measure AI adoption. Earlier work yields a wide range of estimates,
likely owing to differences in methodology, including survey timing, question wording, sample mix,
and respondent characteristics and incentives. Drawing on the 2019 US Annual Business Survey,
Acemoglu et al. (2022) and McElheran et al. (2024) estimate that 3% of firms and 13% of firms use
AI. Drawing on the US Business Trends and Outlook Survey (BTOS), Bonney et al. (2024) use this
to estimate that 5% of businesses (9% employment-weighted) use AI as of February 2024. 3
McKinsey (2025) estimates that 88% of organizations used AI in at least one business function in
2025. Estimated AI adoption rates for the UK also vary widely. According to the Management and
Expectations Survey, 9% of firms use AI in 2023 (ONS 2025). An Institute of Directors survey
(2025) finds that around 49% of businesses use AI as of 2025, while an LSE-CBI survey finds that
25% of firms had made specific investments in AI technologies by 2024 (Oliveira-Cunha 2024).

We ask business executives about AI usage and its effects at their own firms, a topic on which they
have incentives to be well informed. We also lean on long-standing relationships between central
banks and business executives, and the desire of executives to maintain them. These features of our
approach help us enlist a representative sample of senior business executives who are well positioned
to supply informed responses to our survey questions. We use standardized questions across
countries and survey waves to allow for comparisons in the cross section and over time.

We contribute to a second literature that measures AI take-up rates across individuals. Bick et al.
(2024, 2026), Hartley et al. (2025), Barrero et al. (2025), Sidoti and McClain (2025) and Bloom and


3
  As of December 2025, adoption rates in the BTOS have increased to around 18% of businesses and are expected to
rise to 21% over the ensuing six months. See https://www.census.gov/hfp/btos/data

                                                        4
Makridis (2026) all estimate individual AI use at around 30% to 50% of the population. Roughly
half of this usage is work-related, and half is for other purposes. Complementing survey-based
measures, Iscenko et al. (2026) analyze 15 million interactions across Google’s AI products and
document broad occupational coverage but shallow penetration, with usage predominantly
collaborative rather than involving end-to-end task automation.

A third literature considers the realized and expected impact of AI technologies on businesses and
the economy. Some studies find large productivity gains from AI in specific settings. Brynjolfsson
et al. (2025a) find that generative AI yields large gains among customer-support agents at a large
software firm. Del Rio-Chanona et al. (2025) review several studies that report large gains from
generative AI in various settings. Noy and Zhang (2023) conduct an RCT and find that access to
ChatGPT boosts productivity in writing assignments.4 Babina et al. (2024a) link AI investment to
product innovation and greater firm value, and Eisfeldt et al. (forthcoming) find a 5% relative value
gain at firms with highly AI-exposed workforces in the two weeks after ChatGPT’s release. Babina
et al. (2024b) develop evidence that AI investments expand firm-level growth options, while Babina
et al. (2026) argue that it builds organization capital and raises productivity.

Despite large gains associated with AI in specific tasks and certain firms, the implications for
economy-wide productivity are unclear. Adopting a task-based model and applying Hulten’s
Theorem, Acemoglu (2025) estimates that AI technologies will boost US total factor productivity
by at most 0.66% over the next ten years. In sharp contrast, Briggs and Kodnani (2023) estimate that
generative AI alone can boost US labor productivity by 1.5 percentage points per year over ten years.
Misch et al. (2025), adopting the framework of Acemoglu (2025), estimate that AI will boost TFP
in Europe by around 1.1% over five years. Aldasoro et al. (2026) estimate that AI adoption raises
labor productivity among European firms by around 4%, with no detectable employment effects.

Finally, we contribute to a literature on the labor market implications of AI. Survey evidence points
to modest AI effects to date on overall employment (e.g., Abel et al. 2024, Cañas and Kerr 2024),
with larger effects in certain occupations and age groups. Using ADP payroll data, Brynjolfsson et
al. (2025b) estimate that generative AI has reduced the relative employment of young Americans
(ages 22-25) by 16% in the most AI-exposed occupations, conditional on firm-level shocks. Teutloff
et al. (2025) develop evidence that ChatGPT shifted the structure of demand for freelance work,
lowering the demand for writing and translation tasks by 20-50% while raising the demand for


4
 Other research finds productivity gains from AI in legal analysis (Choi and Schwarcz 2025), consulting work
(Dell’Acqua et al. 2023), and programming (Peng et al. 2023 and Cui et al. 2025)

                                                         5
machine learning programming by 24%. Humlum and Vestergaard (2025) estimate near-zero effects
of AI-powered chatbots on earnings and employment at the level of workers and workplaces in
Denmark as of 2024.

The next section describes our main data sources. Section 3 validates our data, showing a tight
relationship between our survey-based measures and national aggregates. Section 4 presents our
results on AI adoption and impact, while Section 5 concludes.


2. Data
This section provides an overview of the seven surveys of business executives we use in our
analysis.5

We work with central banks and other reputable institutions to reach a representative sample of
business executives. A majority of respondents are CEOs, CFOs, or in senior management positions.
Our US data come from the Survey of Business Uncertainty (SBU), an economy-wide monthly
business survey organized by the Federal Reserve Bank of Atlanta. In the UK, our data are from the
Decision Maker Panel (DMP), a monthly, economy-wide survey of UK businesses with ten or more
employees run by the Bank of England. In Germany, we use data from the Bundesbank Online Panel
of Firms (BOP-F), a quarterly representative survey of firms, run by the Deutsche Bundesbank. In
Australia, we use data from the monthly Business Outlook Scenarios Survey (BOSS), fielded by
Macquarie University. In Canada, we use data from the Bank of Canada’s Business Leaders’ Pulse
(BLP) survey. In Mexico, we use data from the Monthly Survey on Regional Economic Activity
(EMAER) run by the Banco de México. Finally, in South Africa, we use data from the BER/SARB
Inflation Expectations Survey organized by the South African Reserve Bank. Below, we provide
more detail about each survey and the fielding periods.




      Survey Name                      Country                     Institution                   AI Waves


5
  The Bank of Korea also ran a survey that included our main AI questions in June 2026 and received responses from
749 firms. As the survey differed in scope from the other business surveys used in our main analysis, we report these
results separately in Appendix C.

                                                          6
    Survey of Business           USA                            Federal Reserve Bank   November 2025; June
    Uncertainty (SBU)                                           of Atlanta             2026

    Decision Maker Panel         UK                             Bank of England        February-April 2025;
    (DMP)                                                                              November 2025-
                                                                                       January 2026; May-
                                                                                       July 2026

    Bundesbank Online            Germany                        Deutsche Bundesbank    January 2026; July
    Panel - Firms (BOP-                                                                2026
    F)

    Business Outlook             Australia                      Macquarie University   December 2025; June
    Scenarios Survey                                                                   2026
    (BOSS)

    Business Leaders’            Canada                         Bank of Canada         May-June 2026
    Pulse

    Monthly Survey on            Mexico                         Bank of Mexico         June 2026
    Regional Economic
    Activity (EMAER)

    Quarterly inflation          South Africa                   South African          May 2026
    expectation survey                                          Reserve Bank



US firms: Survey of Business Uncertainty (SBU)

The Survey of Business Uncertainty (SBU) is a monthly online survey of CEOs, CFOs and senior
executives at US firms run by the Federal Reserve Bank of Atlanta. 6 It targets senior managers at a
representative sample of firms covering all US regions, industries, and size categories. Respondents
are initially recruited by telephone to confirm their position and company, and then moved into the
survey panel. The sponsorship of the Atlanta Fed facilitates the recruitment of senior management.
Figure 1, Panel A shows that 70% of respondents are CEOs, CFOs or other senior managers while
Figure A1 shows the close match of SBU coverage to the population of all US firms, across
industries (Panel A) and Census geographic divisions (Panel B).

The SBU was established in 2014, and as of January 2026 receives responses from around 1,000
firms per month. Core survey modules ask each executive about current, past, and future own-firm
employment and sales revenue growth. Forward-looking questions elicit subjective probability
distributions for these outcomes over the next year. Thus, SBU respondents are accustomed to


6
    https://www.atlantafed.org/research/surveys/business-uncertainty

                                                            7
providing complex forecasts in their survey responses. See Altig et al. (2022) for details and an
extended analysis of forecast characteristics and performance.

In addition to the core modules, each monthly edition of the SBU includes special questions on a
topic of interest. The November 2025 and June 2026 editions contain several questions on AI
adoption and usage intensity, the effects of AI on own-firm employment and productivity in the past
three years, and expected own-firm effects of AI over the next three years. For reference, Figure B1
presents screenshots of these questions.7 The March 2026 edition asked an additional question on
AI-related spending (covering software, hardware, subscription services, worker training, and IT
support) in 2025 and 2026.8

SBU respondents do not receive any monetary or in-kind compensation for joining the panel or
completing the surveys. They are motivated to participate to share their views, maintain their
relationships with the Federal Reserve System, receive information about the survey results, and
perhaps out of a sense of civic responsibility. We view these motivations as a design feature. A
challenge with paid online surveys of targeted populations, like senior executives, is that they can
generate high impostor shares – as high as 80% according to Chandler and Paolacci (2017). See,
also, Bell and Gift (2023). In contrast, in the SBU respondent identities are verified by Atlanta Fed
staff.

UK firms: Decision Maker Panel (DMP)

The Decision Maker Panel (DMP) is a monthly, online survey of UK business executives. 9 It is an
economy-wide survey and matches the industry and region composition of the UK economy
(Appendix Figure A2). Launched in 2016, the Bank of England runs the DMP. Since 2022, the DMP
yields about 2,500 survey responses each month. Like the SBU, interviewees are unpaid and are
initially recruited by telephone to confirm their position and company, and then moved into the
survey panel. Sponsorship by the Bank of England facilitates the recruitment of senior executives.
Over 90% of respondents are either CFOs, CEOs, or in other senior management positions (Figure
1, Panel B).

Each month the DMP asks senior executives about the evolution of sales, prices, employment,
wages, and capital expenditures at their firm over the past year and expectations for the year ahead.

7
  Screenshots of the survey questions from all the surveys are available on the project website: https://firmdataai.com/
8
  A summary of the main results is available here: https://www.atlantafed.org/research-and-data/publications/policy-
hub-macroblog/2026/05/06/how-much-firms-spending-on-ai-and-what-will-happen-to-headcounts
9
  https://decisionmakerpanel.co.uk/

                                                           8
In addition to these standard questions, the DMP regularly includes special questions on topical
issues. For further information, see Bunn et al. (2024) who provide a detailed overview of the survey,
including the structure, quality checks against other datasets, and information on how to access the
data.

Several DMP editions include questions about the adoption of AI technologies and the impact of AI
on their employment and sales per employee (a proxy for productivity). In addition, survey
respondents were asked how frequently they personally use AI technologies during the work week.
We focus on data collected from November 2025 to January 2026 and May to July 2026, which
overlap with the fielding period for several of the other surveys. But the DMP also collected data on
AI adoption between February and April 2025, which adds one additional data point in the time
series dimension.

We match DMP data with firm-level financials in the Bureau van Dijk (BvD) database, which
contains basic accounts and directors data for UK companies. 10 BvD is based on the population of
UK firms in Companies House.

German firms: Bundesbank Online Panel – Firms (BOP-F)

The Bundesbank Online Panel – Firms (BOP-F) is an online survey of a representative panel of
firms located in Germany and is run by the Deutsche Bundesbank – Germany’s central bank. The
survey was first conducted in June 2020 and since July 2021, it surveys around 8,000-9,000 CEOs
and CFOs in German-registered companies per quarter.

The sample for the BOP-F survey is drawn from the Business Register, with the sponsorship of the
Bundesbank supporting the recruitment of senior executives. Firms from nearly all economic sectors
with more than 12,500 EUR annual turnover or at least one employee who also provided information
on their full address are eligible (see Boddin et al. 2024 for more information on how the sample is
drawn).

While the survey has a quarterly frequency from the firm’s perspective, new responses are collected
every month, with the questionnaire being in the field for about three weeks. This is because the
survey follows the rotating panel principle, whereby one third of all new firms in the sample are
randomly selected into group A, B, or C, with only one group being surveyed per month.



10
  Figure A3 shows a strong relationship between survey data in the DMP on employment and sales to matched annual
company accounts data from BvD, which is indicative of high-quality survey responses.

                                                       9
In January 2026, questions on adoption of AI technologies, impacts of AI on employment and
productivity, and the average weekly use of AI by the survey respondent were asked in the BOP-F
based on the SBU and DMP questions, with responses from around 2,500 firms. The questions on
adoption of AI technologies and average weekly use of AI were also asked in July 2026 and received
responses from around 2,300 businesses.

Australian firms: Business Outlook Scenarios Survey (BOSS)

The Business Outlook Scenarios Survey (BOSS) is a monthly, online survey of Australian
businesses.11 The BOSS targets senior financial decision makers at a representative sample of firms
over all Australian locations and industries, with 87% being either CFOs, CEOs, or in senior
management positions, and was established in 2024 by Macquarie University.

Each month BOSS surveys more than 500 businesses on their one-year-ahead expectations of key
macroeconomic variables such as inflation and interest rate, as well as the evolution of key business
indicators such as growth rates of sales, prices of their own products and services, employment,
wages and operating cost.

The questions on AI adoption, realized and expected impacts on productivity and employment, and
personal use by the survey respondent were added to the BOSS survey and administered between 1
and 8 December 2025, with 602 firms participating in the survey. The questions were asked again
in June 2026 and received responses from around 900 firms.

Canadian firms: Business Leaders’ Pulse (BLP)

The Business Leaders' Pulse (BLP) is a monthly online survey of businesses in Canada run by the
Bank of Canada (see Chernis et al. 2022 for further details). The panel is designed to be informative
for assessing aggregate economic conditions relevant to Canadian gross domestic product (GDP).
Established in 2021, the BLP collects responses from around 800 or more firms each month.

The BLP gathers information from Canadian business leaders on a range of topics, including sales,
current business conditions, employment, inflation expectations and investment intentions. Each
month, a subset of participating firms is also asked topical questions that address specific
information needs of the Bank.




11
  https://www.mq.edu.au/macquarie-business-school/our-departments/department-of-economics/our-
research/business-outlook-scenarios-survey-boss

                                                      10
Questions on adoption of AI technologies, impacts of AI on employment and productivity, and
average weekly use of AI by the survey respondent were asked in the BLP over May and June 2026.
The Canadian results are based on approximately 900 survey responses, except for questions on
labor productivity, which were asked to a subset of roughly 600 firms.

Mexican firms: Monthly Survey on Regional Economic Activity (EMAER)

The Monthly Survey on Regional Economic Activity (EMAER, for its name in Spanish) is a
representative survey of establishments with more than 100 workers in the manufacturing and non-
manufacturing sectors at both the regional and national levels in Mexico. It collects the perceptions
of managers of large firms regarding the performance of their businesses and their short-term
expectations. The survey was first implemented in March 2009 for the manufacturing sector and has
covered the non-manufacturing sectors since November 2010.
The EMAER is conducted monthly, generally beginning on the first day of each month, and has an
approximate duration of four weeks. Responses are submitted electronically through an online
platform designed specifically for the survey. Businesses whose responses are delayed are contacted
and may also provide their responses by telephone. Respondents do not receive any monetary or in-
kind compensation for participating in the survey. Since 2025, Banco de México has collected
responses from an average of 1,670 firms per month, while ensuring that the responses meet the
representativeness requirements for each region and sector.
In addition to its recurring monthly modules, which collect information on the retrospective and
prospective evolution of firms' economic indicators and on inflation expectations, the survey
includes special modules that change every month. These modules collect timely information on
specific economic circumstances that become particularly relevant at different points in time.
Questions on AI adoption, realized and expected impacts on productivity and employment, and
personal use of AI by the survey respondent were included in the EMAER in June 2026 and received
responses from 1,719 firms.
South African firms: Quarterly inflation expectation survey

The Bureau for Economic Research has conducted a quarterly inflation expectations survey on
behalf of the South African Reserve Bank since the adoption of inflation targeting in 2000. 12 The
survey was initially administered through a combination of online and paper-based questionnaires
submitted by post. However, since the COVID-19 pandemic, it has been conducted entirely online.



12
     https://www.ber.ac.za/Documents/Index/Inflation-Expectations

                                                     11
Among the groups surveyed are South African firms, which provide expectations for inflation
alongside a range of other macroeconomic indicators, including GDP growth and wages. In May
2026, 96% of the firm survey respondents were CFOs or CEOs. While the survey sample size has
decreased to around 120 respondents in the last few years due to falling response rates, Reid et al.
(2026) recently confirmed that the sample was still representative in terms of firm size, region, and
industrial sector in 2024.

The questions on AI adoption, personal AI use, and its impacts on productivity and employment
were included in the May 2026 inflation expectations survey and 121 firms responded.


3. Data Validation
To validate the quality of our firm survey panels before showing our AI data we run two exercises.

First, in Figure 2 we show how 10 years of data on output and employment from our firm panels
compare against aggregate data for the US SBU and UK DMP surveys. Output data from the US
survey tracks US GDP growth (top-left) and private employment (top-right), as do UK data when
compared to UK GDP growth (bottom-left) and private sector employment (bottom-right). Hence,
our surveys are accurate and representative of macro aggregates over the past decade. Their
performance is similar across the pre-pandemic period, the COVID recession and recovery, and post-
pandemic stabilization. Hence, we are confident that, due to our large representative sample of senior
executives, our data reflect aggregate trends across the business cycle.

Second, we show the performance of the sales and employment forecasting questions included in
our surveys on a quarterly basis. Once a quarter, executives are asked to forecast their year-ahead
(12 months ahead) sales growth and employment growth. One year later we compare these forecasts
to actual realizations of sales and employment growth for these firms. This enables a large sample
evaluation of our survey respondents’ forecast accuracy. As we see in Figure 3, our responding
executives make accurate forecasts, with sales and employment predictions lining up tightly with
realizations occurring over the next year. This positive relationship suggests that our panel is well-
equipped to predict the future business conditions for their firms, increasing our confidence in the
accuracy of their forecasts of the impact of AI.


4. Main Results
We present the overall results which combine firm-level results from each country into one figure,
and also provide country-level values. Tables can also be downloaded from https://bit.ly/4B2zU5c

                                                   12
4.1 Current and expected use of AI technologies

We begin by analyzing the current use of AI technologies by businesses. In all seven surveys, firms
are asked to select which of the following they are currently using, if any: data processing using
machine learning; visual content creation; Generative AI; image processing using machine learning;
robotics and autonomous vehicles; or other. Firms could select more than one technology.

Figure 4A presents the main results. The black bars in the figure correspond to the average use across
firms in all seven surveys, weighted by the sample sizes of the respective surveys. Across all seven
countries, we find that a majority of businesses are currently using some AI technology. Adoption
is highest in the US (95% of firms), followed by the UK (88%), Canada (82%), Germany (78%),
Australia (68%), Mexico (64%), and South Africa (56%). On average, 78% of all firms are currently
using AI.

Figure 4B shows that adoption is not concentrated in a single use case. The most popular current use
is ‘Generative AI’ (by 63% of firms on average), but 34% of firms also report using visual content
creation and 33% use data processing using machine learning. Less commonly cited uses were image
processing using machine learning (22%), and robotics and autonomous vehicles (8% of firms),
which are likely more specific to certain industries.

Adoption of AI technologies has increased since the start of 2026. Figure A4 compares the trends in
AI adoption over the available survey waves. Current use of AI technologies increased across all
four countries in the original sample. In the US, adoption is near-universal, with around 95% of
businesses using at least one AI technology even at the start of the year. 13 In the UK, adoption has
also increased further since February-April 2025, when the questions were asked for the first time.
This emphasizes the importance of having consistency in the timing of the questions across data
sources during a time when adoption is increasing rapidly across businesses.

We next study the characteristics of firms which predict the current use of AI technologies. In Figure
A5.a, we present a series of binned scatter plots of the relationships between current use of AI (on
the vertical axes) and a series of firm characteristics. This figure uses data from the DMP survey,
due to the larger sample size and the availability of more firm covariates. 14 We find that more

13
   In the first version of the paper, the percentage of US businesses using any AI technology was 78%. In that
calculation, firms which skipped the question on use of AI technologies were treated as non-users rather than missing.
In the current draft, we treat firms that skip the questions as missing observations, which increases the AI adoption to
94% in November 2025 and 95% in June 2026.
14
   In Figure A5.b, we show similar results for a subset of variables from the US SBU. More productive (Panel A) and
larger (Panel B) firms are more likely to be using an AI technology in US firms as well.

                                                           13
productive (Panel A), larger (Panel B), and higher-paying firms (Panel C) are more likely to be using
AI.15 In contrast, in Panels D and E, we show that firms with older directors on average, and older
firms are less likely to be currently using AI. Use of AI technologies also varies by sector. In Figure
A6 Panel A, we show that current AI adoption by UK firms is highest in the finance and insurance
and information and communications sectors.

In Table 1, we test the robustness of these relationships in a regression table where we combine all
the variables in a single specification and also control for industry and time fixed effects. The
dependent variable in Columns 1-2 is a dummy for whether a firm uses any AI technology, scaled
by 100 for interpretability. We find that the most robust predictors of AI use from Figure A5.a are
firm employment, average wage per employee, and the average age of directors. 16

Measures of firm AI adoption vary widely across recently published studies, especially those
drawing on survey data. We highlight three features of survey design which can partly account for
these gaps, and illustrate them using data from the UK Decision Maker Panel. The first is the
composition of the sample across firm size categories. Consistent with the results above, larger firms
are more likely to use AI: 80% of firms with 10-49 employees currently use at least one AI
technology, rising to 83% among firms with 50-99 employees, 87% among firms with 100-249
employees, and 92% among firms with 250 or more employees (Figure A7, Panel A). Surveys which
over-sample larger businesses, or which exclude the smallest firms altogether, will therefore report
higher adoption rates than surveys which do not. Table A1 presents the breakdown of survey
responses by firm size category across the seven surveys in our main dataset. The second is the
choice of weighting scheme, which follows directly from this size gradient. Panel B of Figure A7
shows that current AI use among UK firms is 88% when responses are weighted by employment,
86% when unweighted, and 83% when weighted by the number of businesses in each industry and
size band. Employment weighting places more weight on the large, AI-intensive firms, while
business-count weighting places more weight on the small firms which dominate the firm
population, generating a spread of five percentage points from identical underlying responses. The
third is the position of the survey respondent within the business. Panel C shows that adoption is


15
   Labor productivity is constructed using firm-level accounts data from BvD as the real gross value-added per
employee. The data from the latest accounts available for each firm are used in the figure. The average wage per
employee (Panel C) is constructed as the total wage bill per employee, again using accounts data.
16
   We do not include a regression of productivity growth, real sales growth, and employment growth in the same
specification because productivity growth is defined in our analysis as real sales growth – employment growth.
Running these three variables in the same specification would result in collinearity. Therefore, we split the results into
two columns.


                                                            14
89% when the respondent is a CEO or CFO, compared with 84% when the respondent holds any
other position.

We examine this last difference further in Table A2, which regresses our indicator for current AI
use on a dummy for whether the respondent is a CEO or CFO. The gap does not appear to be driven
by the types of firms that senior executives run. Respondents in these roles report adoption rates four
to seven percentage points higher than other respondents, and the estimated difference remains
statistically significant and stable in specifications controlling for firm size, labor productivity, firm
age, the average age of directors, and industry and time fixed effects. Two interpretations are
consistent with this pattern. CEOs and CFOs may have a more complete view of AI use across their
organization, in which case surveys of more junior respondents understate true adoption;
alternatively, senior executives may be more willing to report AI use that they do not directly
observe, in which case surveys of executives overstate it. Either way, comparisons of adoption rates
across surveys should take account of who is answering the questionnaire. Taken together, these
three factors each move measured adoption by between five and twelve percentage points, and they
compound: a survey of small firms, weighted by business counts and answered by non-executives,
will report substantially lower adoption than one of large firms, weighted by employment and
answered by CEOs. They therefore narrow the range of estimates in the literature without closing it.
Differences in question wording and in survey timing remain important additional explanations for
differences in AI adoption measures.

Finally, we consider how firms expect adoption of AI technologies to change over the next three
years. Figure A8.1 shows that AI adoption is expected to increase on average. Across all seven
countries, 82% of firms expect to be using some AI technology over the next three years.
Furthermore, we find that the most common technology firms expect to use is data processing using
machine learning (Figure A8.2), suggesting firms are expecting to build capacity to use AI tools for
data processing, even if they are not currently used as extensively. 17 Expected AI adoption has also
been trending up over time (Figure A8.3), having increased in all four countries sampled in the
beginning of the year.

4.2 Firm Spending on AI

To complement the results on the use of different AI technologies, in the US and UK, additional
questions were asked in 2026 about AI-related spending in the 2025 and 2026 calendar years. AI-

17
     AI adoption is also expected to increase across almost all industries over the next 3 years (Figure A6, Panel B).

                                                             15
related spending captures software, subscription services, hardware, worker training, and IT staff
support, and provides a quantitative measure of the intensity of AI adoption. Figure 5 presents
distributions of these results across five categories. We scale AI spending by firm employment and
convert the UK results into US dollars for comparability. Panel A shows the results for the US,
where firms spent around $1,363 per employee in 2025 and expect to spend $2,043 per employee in
2026 (employment-weighted). Over 80% of firms were spending on AI in 2025, and 23% were
spending more than $1,000 per employee. For 2026, only 11% of firms expect not to make any AI-
related spending. But this spending is very skewed, with 55.7% of the total in firms spending $10,000
or more, and the top 10% of firms accounting for 90% of all spending, with an average spend of
$7,480 per employee each. Total US AI spending based on these numbers aggregates up to an overall
spend of about $280 billion on AI across the entire US economy. Table 2 shows the AI spending per
employee in both 2025 and 2026 for different percentiles of the distribution.

Panel B of Figure 5 shows the results for UK firms in the DMP. A larger share (33% of firms) did
not make AI-related expenditures in 2025, but this is expected to drop sharply to 17% in 2026.
Meanwhile, increases are expected in AI-spending between $100 to $999 per employee (29% to
44%) and in firms spending more than $1,000 per employee (8% to 13%). Based on these responses,
we estimate that UK firms spent $422 per employee on AI-related expenditures in 2025 and this is
expected to increase to $725 per employee in 2026. Again, like the US this spending is very skewed,
with 30% of the total in firms spending $10,000 or more in 2026, and the top 10% of firms
accounting for 69% of all spending with an average spend of $5,200 per employee each. Total UK
AI spending based on these numbers aggregates up to an overall spend of about $25 billion on AI
across the entire UK economy in 2026.

The firm characteristics that are highly correlated with AI adoption are also highly correlated with
AI spending per employee. In Figure A9, we present five binned scatterplots of AI spending per
employee in 2026 against the same characteristics used in Figure A5.a. This figure is based on data
collected for UK firms over August-September 2026. More productive (Panel A) and higher-paying
firms (Panel C) spend significantly more on AI per employee in 2026; we also find that AI spending
is higher at younger firms (Panel E) and firms with younger directors (Panel D). Larger firms spend
less per employee (Panel B), although they spend more in aggregate terms. In Columns 3-4 of Table
1, we test how robust these relationships are in multivariate regressions that also control for industry
and time fixed effects. Higher-paying firms spend significantly more on AI per employee. We also
find that firms that expect higher productivity growth and higher real sales growth in 2026 spend
more on AI.

                                                  16
Figure 6 provides further evidence that AI spending is highly concentrated across firms. This figure
plots the cumulative share of total AI spending in 2026 against the cumulative share of firms.18 In
both the US and the UK, the curves indicate that a small share of firms accounts for a very large
share of aggregate expenditure. Specifically, 1.8% of US firms and 1.3% of UK firms account for
50% of all AI spending in 2026 in the respective countries. This is consistent with evidence from AI
producing firms: Anthropic’s IPO documents showed that one-quarter of its sales are to two firms.19
Similarly, the AI spending Gini coefficient for 2026 is 0.92 in the UK and 0.9 in the US, materially
higher than income Gini coefficients in the two countries. 20

Overall, these two sections highlight that AI use is widespread across businesses in seven countries
sampled. Larger and more productive firms are more likely to be using AI technologies, as are
higher-paying businesses. AI adoption has increased since the start of 2026 and is expected to
increase over the coming years. But this spending is extremely skewed across firms, with the top
10% of firms accounting for 90% and 69% of spending in the US and UK, respectively. In Sections
4.4 and 4.5, we present new evidence on how firms estimate that AI has been impacting their
employment and productivity, and how they expect these effects to change in the next three years.

4.3 Use of AI by survey respondents

In this section, we analyze how frequently respondents themselves use AI during a typical work
week. As these respondents typically hold senior positions in their firms (e.g. CEOs, CFOs, senior
finance managers), these results are another useful proxy for AI adoption more broadly since they
are in a position to instruct their subordinates to make use of AI as they see the opportunity. They
are also less likely to be subject to measurement error, as the respondents are reporting about their
personal use, rather than for the business as a whole. The survey asks whether they personally use
AI technologies: “Not at all”; “Up to 1 hour a week”; “1 to 5 hours a week”; or “More than 5 hours
a week”.

In Figure 7A, we assign quantitative values to each of the categories to estimate the average number
of hours of AI use. Across all firms, our respondents use AI around 2.1 hours per week on average.
These results are similar across the seven countries, ranging from 1.7 hours in Mexico to 2.5 hours


18
   In Figure A10 we present a similar figure for the distribution of cumulative AI spending per employee across firms.
We again find a very skewed distribution, with less than 5% of firms accounting for 50% of all AI spending per
employee in 2026.
19
   See ‘Anthropic warns of ‘existential risks to humanity’ in IPO prospectus, Financial Times, 29 September 2026
20
   The latest data from the World Bank estimate an income Gini coefficient of 0.42 for the US in 2024 and 0.32 in the
UK in 2021. https://data.worldbank.org/indicator/SI.POV.GINI

                                                          17
in the US and Canada. Figure 7B presents the distribution of responses across the four categories.
Across all firms, 21% of respondents do not use AI at all during the working week. The modal
response is up to 1 hour a week (35%), but more intensive AI use is not uncommon. 30% of
respondents report 1-5 hours of AI use per week, and 13% report using AI more than five hours in
a typical working week. The use of AI by survey respondents has also been increasing steadily over
time (Figure A11), from around 1.5 hours a week on average in the beginning of the year. In the UK,
the average use has more than doubled since the February-April 2025 wave.

We next consider how AI use varies with firm-level and respondent characteristics. Figure A12.a
presents binned scatterplots with the average weekly AI use on the vertical axis for UK firms. We
find that respondents in younger firms use AI technologies more often during the working week
(Panel A), as do respondents in firms where the average age of directors is lower (Panel B). These
relationships are similar to Figure A5.a, Panels D and E, where the firm age and average age of
directors are shown to be negatively correlated with current AI adoption across the business. 21 Figure
A12.b shows that a similar negative relationship is present between firm age and average weekly AI
use in US firms. In Figure A13 we split the frequency of AI use by the position of the respondent in
the business. Specifically, we distinguish between CEOs, CFOs, and other senior executives. In both
the US (Panel A) and UK (Panel B), we find that AI is more frequently used by CEOs than other
respondents.

4.4 Impact of AI on firm employment

In this section we present the results on the impact of AI technologies on firm realized and expected
employment. For the US, UK, Canada, Mexico, Australia, and South Africa we use the latest data
collected in mid-2026. German firms were not asked this question in the latest survey; for Germany,
we instead refer to the results from January 2026. Firms are asked to estimate the employment
impacts using five categories, ranging from a large positive impact (increasing employment by more
than 5%) to a large negative impact (decreasing employment by more than 5%). To estimate an
average quantitative impact of AI on employment, we assign numerical values to each of the five
categories. We assign values ±7.5% to large positive/negative impacts; ±2.5% to small
positive/negative impacts; and 0% to no impact.




21
  In Columns 5-6 of Table 1 we analyze the determinants of weekly AI use. We find that the average wage per
employee and average age of directors remains the most significant predictor of average weekly AI use.

                                                       18
In Figure 8A we present these average impacts. Across all firms, the impact of AI is essentially zero
over the past three years. However, there is some heterogeneity across the seven countries. In the
UK and South Africa firms report small negative effects, on average, of around -0.1% over the past
three years. Meanwhile, in the US, Canada, Germany, and Mexico, firms report small positive
effects, ranging from +0.1% to +0.2%. Australian firms report an impact around zero. Figure 8B
shows the distribution of responses across the five categories. Across the seven surveys, 87% of
firms on average estimate no impact over the last three years. This percentage varied somewhat
across countries: Germany (95%), US, Canada, and the UK (88% of firms), South Africa (82%),
Mexico (80%), and Australia (74%). Finally, Figure A14 plots the estimated impacts of AI on
employment over survey waves. There is no clear trend in the series, suggesting the employment
effects have not changed over time.

There is substantial sectoral heterogeneity in the realized employment impacts of AI. Figure A15,
Panel A shows the average realized employment impacts from AI across industries in the UK. The
impacts vary from positive in the Real estate sector (+0.3%) to negative in the Wholesale and retail
(-0.2%) and Recreational services (-0.4%) sectors.

Turning to the next three years, in Figure 9A we present the quantitative estimates of the expected
employment impacts of AI. On average, firms across the seven countries expect AI to lower
employment by around 0.4% over the next three years. Even this projection of a modest negative
employment impact is too pessimistic for three reasons. First, our forward-looking survey data don’t
capture the positive general equilibrium effects of AI-driven productivity gains on aggregate
employment. Second, our survey forecasts miss net job gains by firms not yet born. Third, our
sample frames underrepresent the youngest firms. If AI advances have relatively positive effects on
employment at younger firms, we undercount those gains as well. In short, the key message is that
our survey evidence suggests that AI technologies will not have large effects on aggregate
employment in the next three years.

Looking at individual countries the largest effects are in the UK and the US (both -1.3%). Australian
firms expect AI to lower employment by around 0.5%, and Canadian and German firms expect only
a 0.1% employment decline. At the same time, Mexican firms expect a small employment boost due
to AI of around 0.6% over the next three years, and South African firms expect a small increase of
around 0.1%.

Figure 9B shows the distribution of responses across the five categories. Here the results are much
more striking with a wide range of responses, and over 40% of firms reporting that AI will impact

                                                 19
employment either positively or negatively. This highlights that while AI may not impact overall
employment it looks likely to generate considerable churn across firms, with large movements of
employment across firms. Finally, Figure A16 shows how these expected employment impacts have
changed over time. In the UK and US, there has not been a significant change since the beginning
of the year, with estimated impacts ranging from -1.2% to -1.3%. The expected employment impacts
in Australia have become more negative, from around zero in the beginning of the year to -0.5% in
mid-2026.

There remains heterogeneity across sectors in the expected employment impacts, as we show in
Figure A15, Panel B. The expected impacts over the next three years are negative across all sectors
of the economy for firms in the UK. The largest negative impacts are in the Wholesale and retail (-
1.7%), Professional and scientific (-1.7%), and Finance and insurance (-1.9%) sectors.

Beyond the sectoral differences, we also consider how the expected employment impacts vary with
various firm-level characteristics. Columns 7-8 of Table 1 present the covariates of expected AI
employment impacts for UK firms. To maximize the sample size, the regressions use the latest firm
observation on the expected employment impact using data collected over February-April 2025,
November 2025-January 2026, and May-July 2026. We find that larger firms expect more negative
impacts of AI on employment. 22 In contrast, higher realized employment growth in 2025 and higher
expected employment growth in 2025 are both associated with less negative AI employment
impacts.23

4.5 Impact of AI on firm productivity

In this section we present results on the impact of AI technologies on firms’ realized and expected
productivity. The survey questions follow the same structure as the employment impacts.
Productivity in this analysis is defined as the volume of sales per employee. These questions were
included in the mid-2026 waves in all surveys except Germany; for Germany, we use earlier data
from January 2026 in the figures below.

Figure 10A presents the main results on realized productivity impacts over the past three years. To

22
   Expected employment impacts are also more negative among firms whose survey respondent personally uses AI
more intensively, ranging from -0.7% where the respondent reports no personal use to -2.2% where they use AI for
more than five hours per week (Figure A17).
23
   One concern is that firms expecting more negative employment impacts from AI are simply more pessimistic about
their employment prospects in general. To assess this, we relate expected AI employment impacts to firms'
employment growth forecast errors. Figure A18 shows no systematic relationship for both forecast errors (Panel A)
and absolute employment growth forecast errors (Panel B). Thus, firms that habitually over- or under-predict their own
employment growth do not report systematically different impacts of AI.

                                                         20
estimate an average quantitative impact of AI on productivity, we assign numerical values to each
of the five categories. As with the employment impact, we assign values ±7.5% to large
positive/negative impacts; ±2.5% to small positive/negative impacts; and 0% to no impact. Across
all firms, AI is reported to have boosted productivity by around 0.5% over the past three years. The
effects are very similar across the US, Canada, UK, Germany, and Australia, ranging from +0.2%
to +0.5%. Mexican firms report slightly larger productivity gains, at +0.7% over the past three years,
on average. Figure A19, Panel A shows a breakdown of the realized AI productivity impacts by
industry for UK firms. These are positive across all industries in the UK. Firms in the Information
and Communications and Professional and Scientific sectors report the largest positive productivity
impacts from AI so far, at +1.3% and +1%, respectively.

In Figure 10B, we show the distribution of responses across the five categories. Across the seven
surveys, 83% of firms on average estimate no impact over the last three years. This percentage is
highest in Germany (91%), followed by Canada (85% of firms), South Africa (84%), the US (83%),
the UK and Australia (82% in both), and Mexico (75%). Among the remaining firms which report
some impact, the results are decisively skewed to the positive across all seven countries, indicating
some positive impacts in the aggregate. Finally, Figure A20 shows how the realized AI productivity
impacts have changed since past survey waves. The estimated impacts have increased in both the
UK and US since the start of 2026, from 0.2-0.3% to 0.5% in mid-2026. The impacts have remained
about 0.5% in Australia.

In Figure 11A, we present results on how firms expect AI to impact their productivity over the next
three years. Over the next three years, firms across the seven countries expect AI to increase labor
productivity by an average of around 1.7%, implying an increase in annual productivity growth of
about 0.6%. The largest expected effects are in the UK (+2.6%), the US (+2.3%), Canada (+2%),
and Mexico (+1.9%). Smaller, but still positive and significant effects are expected in Germany
(+0.9%), Australia (+0.7%) and South Africa (+0.6%).

Figure 11B shows the distribution of these responses across the five categories. 53% of all firms
expect no impact over the next three years, with the distribution of responses being clearly skewed
to the positive. 27% of all firms expect a small positive impact, increasing productivity by less than
5%, and 16% expect a large positive impact on productivity, greater than 5%. Figure A21 shows
how the expected productivity impacts have changed over time. UK firms expect even larger
productivity gains than at the beginning of 2026, rising from 1.9% to 2.6%. US firms now expect a
2.3% productivity boost, compared with 2.2% in the beginning of the year. Expected productivity

                                                 21
gains among Australian firms have declined slightly, from 0.9% to 0.7% in the latest data.

The productivity boost from AI is not expected to be equally distributed across sectors of the
economy, as we show in Figure A19, Panel B. Based on data from the UK, the largest impacts are
in the information and communications sector, which expects AI to increase productivity by 4.4%.
The finance and insurance, real estate, and professional and scientific sectors also expect large gains,
at around 3.4% over the next three years. Much smaller impacts are expected by firms in
construction, recreational services, and other production (which include agriculture and mining and
quarrying).

As with the expected employment impacts, we also consider how the expected productivity impacts
vary with various firm-level characteristics. Table 1, Columns 9-10 present the covariates of
expected AI productivity impacts using multivariate regressions for UK firms.24 As was the case for
employment, the regressions use the latest firm observation on the expected productivity impact
using data collected over February-April 2025, November 2025-January 2026, and May-July 2026
which gives 3,215 unique firm observations. We find that larger firms, firms with younger directors,
and those with higher expected real sales growth have more positive expected impacts of AI on
productivity.25

To quantify the potential aggregate productivity effects of AI adoption, we combine estimated
impacts of AI on firms' sales per employee and employment from the DMP with UK national
accounts aggregates and data on AI-related expenditures. We use the latest DMP estimates that AI
increased sales per employee by 0.54% and reduced employment by 0.1% over the past three years,
and will increase sales per employee by 2.6% while reducing employment by 1.3% over the next
three years. AI expenditure is assumed to average £313 per worker per year over the past three years
and £537 per worker per year over the next three years, based on data collected from the DMP over
August-September 2026. In the accounting framework, AI expenditure is treated primarily as an
additional intermediate input, with a small proportion contributing to the capital stock. Under these
assumptions, AI is estimated to have raised sales per employee growth by around 0.18 percentage
points per year over the past three years and to raise it by a further 0.69 percentage points per year


24
   Expected productivity impacts are also larger among firms whose survey respondent personally uses AI more
intensively, rising from +1.1% where the respondent reports no personal use to +3.9% where they use AI for more
than five hours per week (Figure A22). Together with Figure A17, this suggests respondents with more direct
experience of AI anticipate both larger productivity gains and larger displacement, rather than simply holding a more
favorable view of the technology.
25
   Similar to Figure A18, in Figure A23 we find no systematic relationship between expected AI productivity impacts
and firms' sales growth forecast errors. Expectations of larger productivity impacts from AI are not associated with
firms' general forecasting optimism.

                                                         22
over the next three years (Table 3). Because additional AI expenditure increases intermediate input
costs, the implied impact on gross value added (GVA) per worker is smaller, amounting to around
0.17 percentage points per year over the past three years. Over the next 3 years, the reduction in
employment compensates and the impact on labor productivity is estimated at +0.85 percentage
points per year over the next three years. Lastly, applying a standard growth-accounting
decomposition with labor and capital shares of 0.67 and 0.33, respectively, implies corresponding
contributions to total factor productivity (TFP) growth of approximately +0.13 percentage points per
year over the past three years and +0.68 percentage points per year over the next three years.

Finally, we examine how expected employment and productivity impacts relate to one another
within firms. Because we define productivity as the volume of sales per employee, a firm expecting
to hold output constant and reduce employment would report an expected productivity gain exactly
equal in magnitude to its expected employment reduction. Figure A24 presents a binned scatter plot
of expected employment impacts against expected productivity impacts, controlling for industry and
time fixed effects. The relationship is negative and statistically significant, but the slope is well
below one in absolute value (-0.07): firms anticipating larger productivity gains from AI expect only
modestly larger reductions in employment. Firms therefore expect a substantial share of the
productivity gains from AI to arrive through higher output rather than lower headcount.

Overall, the last two sections show that the adoption of AI technologies has had little impact on firm
employment and a small positive impact on firm productivity so far. However, firms anticipate large
impacts over the next few years. On average, businesses expect AI to boost productivity by around
1.7% over the next three years, while lowering employment by around 0.4% over the same period.
This also implies an increase in output of around 1.3% (Table 4). A limitation of our analysis is that
we cannot assess how AI affects employment across different groups of workers. For example, a
decline in employment among younger workers could be offset by an increase among older workers,
leaving little change in a firm’s total employment.


5. Conclusion
Drawing on our original surveys of nearly 9,000 senior business executives, we present new
evidence on how firms and the executives use AI technologies, and on the past and expected future
effects of AI advances on employment, productivity, and AI-related spending in the US, Canada,
the UK, Germany, Australia, Mexico and South Africa. We put our questions to executives from
November 2025 to January 2026 and again from May to July 2026.



                                                 23
We obtain several findings. First, 78% of businesses use some form of AI technologies as of May-
June 2026, and adoption is expected to increase. Larger, more productive, and higher-paying firms
are more likely to use AI technologies. Second, US executives expect AI spending per employee to
reach $2,000 per employee in 2026, 50% more than in 2025. Third, this spending is highly
concentrated with 2% of firms accounting for over half of $300 billion in aggregate AI spending.
Fourth, senior business executives use AI tools about 2.1 hours per week on average, as of May-July
2026, up from 1.5 hours at the start of 2026. Fifth, our survey evidence AI has had little employment
impact to date as of mid-2026. In contrast, the same executives estimate that AI has increased labor
productivity by around 0.5% over the past three years. Sixth, these executives anticipate larger AI-
driven productivity gains of about 1.7% over the next three years. Seventh, combining our survey
evidence with basic economic reasoning suggests that AI technologies will have little impact on
aggregate employment over the next three years but may materially boost the extent of job creation
and destruction.

We will continue our efforts to survey senior business executives across many countries in
cooperation with central banks and other leading institutions. Our goal is to monitor the adoption of
AI technologies over time, the spending on AI-related investments and activities, and the (perceived)
effects of AI technologies on employment, productivity, and other outcomes.




                                                 24
References
Abel, J R, R Deitz, N Emanuel and B Hyman (2024), “AI and the labor market: Will firms hire,
fire, or retrain?”, Liberty Street Economics, 4 September.
Acemoglu, D, D Autor, J Hazell and P Restrepo (2022a), “Artificial Intelligence and Jobs:
Evidence from Online Vacancies”, Journal of Labor Economics 40(S1).
Acemoglu, D, G W Anderson, D N Beede, C Buffington, E E Childress, E Dinlersoz, L S Foster,
N Goldschlag, J C Haltiwanger, Z Kroff, P Restrepo and N Zolas (2022b), “Automation and the
workforce: A Firm-level view from the 2019 Annual Business Survey”, NBER Working Paper
30659.

Acemoglu, D (2025), “The simple macroeconomics of AI”, Economic Policy 40(121): 13-58.

Aldasoro, I, L Gambacorta, R Pal, D Revoltella, C Weiss and M Wolski (2026), “AI Adoption,
Productivity and Employment: Evidence from European Firms”, BIS Working Paper 1325.

Altig, D, J M Barrero, N Bloom, S J Davis, B H Meyer, and N Parker (2022), “Surveying Business
Uncertainty”, Journal of Econometrics 231(1): 282-303.

Babina, T, A Fedyk, A He and J Hodson (2024a), “Artificial intelligence, firm growth, and product
innovation”, Journal of Financial Economics 151: 103745.
Babina, T, A Fedyk, A He and J Hodson (2024b), “Artificial Intelligence and Firms' Systematic
Risk”, Working Paper.
Babina, T, A He and R Jiang (2026), “Canaries in the Gold Mine: Early Productivity Gains from
Artificial Intelligence Creating Organization Capital,” NBER Working Paper 35684.
Barrero, J, N Bloom and S Davis (2025), Survey of Working Arrangements and Attitudes data,
discussed in “Why working from home will stick”, Stanford working paper.

Baslandze, S, Z Edwards, J R Graham, T McClure, B H Meyer, M Sparks, S R Waddell and D
Weitz (2026), “Artificial Intelligence, Productivity, and the Workforce: Evidence from Corporate
Executives”, Journal of Finance: Insights and Perspectives, forthcoming

Bell, Andrew M. and Gift, Thomas, (2023), “Fraud in Online Surveys: Evidence from a
Nonprobability, Subpopulation Sample” Journal of Experimental Political Science, Vol. 10(1),
Spring 2023, 148-153.
Bick, A, A Blandin and D Deming (2024), “The Rapid Adoption of Generative AI”, NBER
Working Paper 32966.

Bick, A, A Blandin, D J Deming, N Fuchs-Schündeln and J Jessen (2026), “Mind the Gap: AI
Adoption in Europe and the U.S.”, NBER Working Paper 34995.

Bloom, N, C I Jones, J Van Reenen and M Webb (2020), “Are Ideas Getting Harder to Find?”,
American Economic Review 110(4): 1104–44.
Bloom, N. and Makridis, C (2026), “The politics of AI”, NBER WP 34813.
Boddin, D, M Köhler and P Smietanka (2024), “Bundesbank Online Panel - Firms Data Report
2023-07”, DOI: 10.12757/BBk.BOPF.2022Q2.01.

                                               25
Bonney, K, C Breaux, C Buffington, E Dinlersoz, L S Foster, N Goldschlag, J C Haltiwanger, Z
Kroff and K Savage (2024), “Tracking firm use of AI in real-time: A snapshot from the Business
Trend and Outlook Survey”, NBER Working Paper 32319.

Briggs, J and D Kodnani (2023), “The Potentially Large Effects of Artificial Intelligence on
Economic Growth”, Goldman Sachs Global Economics Analyst, 26 March.
Brynjolfsson, E, D Li and L Raymond (2025a), “Generative AI at Work”, The Quarterly Journal
of Economics 140(2): 889-942.
Brynjolfsson, E, B Chandar and R Chen (2025b), “Canaries in the Coal Mine? Six Facts about the
Recent Employment Effects of Artificial Intelligence”, Working Paper.
Bunn, P, N Bloom, A Crundwell, S Khan, C Menzies, P Mizen, M Sculthorpe, K Shah, G
Thwaites and I Yotzov (2024), “The Decision Maker Panel: A User’s Guide”, Bank of England
Staff Working Paper 1096.
Cañas, J and E Kerr (2024), “Texas firms using AI report little impact on employment”, Federal
Reserve Bank of Dallas, 25 June.
Chandler, J and G Paolacci (2017), "Lie for a Dime: When Most Prescreening Responses Are
Honest but Most Study Participants Are Impostors", Social Psychological Personality Science
8(5): 500-508.
Chernis, T, C D’Souza, K MacLean, T Reader, J Slive and F Suvankulov (2022), “The Business
Leaders’ Pulse - An Online Business Survey”, Staff Discussion Paper 2022-14.
Choi, J H and D Schwarcz (2025), “AI Assistance in Legal Analysis: An Empirical Study”,
Journal of Legal Education 73(2): 384-420.
Cui, Z (Kevin), M Demirer, S Jaffe, L Musolff, S Peng and T Salz (2025), “The Effects of
Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software
Developers”, SSRN Scholarly Paper No. 4945566.

Dell’Acqua, F, E McFowland III, E Mollick, H Lifshitz-Assaf, K Kellogg, S Rajendran, L Krayer,
F Candelon and K R Lakhani (2023), “Navigating the Jagged Technological Frontier: Field
Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality”,
Harvard Business School Working Paper.
Del Rio-Chanona, R. Maria, Ekkehard Ernst, Rossana Merola, Daniel Samaan, and Ole Teutloff.
2025. “AI and Jobs: A Review of Theory, Estimates, and Evidence.” arXiv preprint
arXiv:2509.15265v1
Eisfeldt, A L, G Schubert, B Taska and M Ben Zhang (Forthcoming), “Generative AI and Firm
Values”, Journal of Finance.
Goldin, I, P Koutroumpis, F Lafond and J Winkler (2024), “Why Is Productivity Slowing Down?”,
Journal of Economic Literature 62(1): 196–268.
Hartley, J, F Jolevski, V Melo and B Moore (2025), “The Labor Market Effects of Generative
Artificial Intelligence”, SSRN Working Paper
Humlum, A and E Vestergaard (2025), “Still Waters, Rapid Currents: Early Labor Market
Transformation under Generative AI”, NBER Working Paper 33777.

                                                26
Institute of Directors (2025), “Major blockers to AI adoption in British business”, 28 April.

Iscenko, Z, S Strand, Y Chen, G Aimard, M Codreanu, V Sampathkumar, A Imas, J Jacobs, E
Muiruri, J Mateos-Garcia, J J Ng, S Javed, J Martin, O Ajmeri, D Calin, A Kim, F Curto Millet
and J Manyika (2026), “Google’s AI & Economy ATLAS v1.0: Mapping Gemini Usage in the
Economy”, arXiv preprint 2608.00038.

McElheran, K, J F Li, E Brynjolfsson, Z Kroff, E Dinlersoz, L S Foster and N Zolas (2024), “AI
Adoption in America: Who, What, and Where”, Journal of Economics & Management Strategy
33(2): 375–415.

McKinsey (2025), “The state of AI in 2025: Agents, innovation, and transformation”, November.
Misch, F, B Park, C Pizinelli and G Sher (2025), “AI and Productivity in Europe”, IMF Working
Paper 2025/067.
Noy, S and W Zhang (2023), “Experimental evidence on the productivity effects of generative
artificial intelligence”, Science 381(6654).

ONS (2025), “Management practices and the adoption of technology and artificial intelligence in
UK firms: 2023”, 24 March.
Oliveira-Cunha, J, B Serra-Lorenzo, A Valero (2024), “What an LSE-CBI survey found about AI
adoption in UK firms”, 2 July.
Peng, S, E Kalliamvakou, P Cihon and M Demirer (2023), “The Impact of AI on Developer
Productivity: Evidence from GitHub Copilot”, Working Paper.
Reid, M, D von Fintel and A Foresto (2026), “From Deliberate Sample to Representative Sample:
Pilot Study for the BER Inflation Expectations Survey”, Journal of Business Cycle Research 22:
157-186.
Sidoti, O and C McClain (2025), “34% of U.S. adults have used ChatGPT, about double the share
in 2023”, PEW Research Center Short Read.

Teutloff, O, J Einsiedler, O Kassi, F Braesemann, P Mishkin and R Maria del Rio-Chanona
(2025), “Winners and losers of generative AI: Early Evidence of Shifts in Freelancer Demand”,
Journal of Economic Behavior & Organization 235, 106845.




                                                 27
   Figure 1 Position of respondents within their firm

       Panel A US Firms (SBU)                                                 Panel B UK Firms (DMP)




Notes: This figure shows the position of survey respondents. Panel A shows data from the US Survey of Business Uncertainty (SBU), averaged over
January 2017 to January 2025. Panel B shows data from the UK Decision Maker Panel (DMP), averaged over 2017 -2025.                     28
  Figure 2 Firm sales and employment growth vs aggregate statistics
                         Panel A Sales growth                                                 Panel B Employment growth



 US Firms
 (SBU)




 UK Firms
 (DMP)


Sources: SBU; ADP; BEA; DMP; ONS; HMRS and authors’ calculations. Notes: SBU sales data are compared to GDP growth from the BEA. SBU employment growth
data are compared to ADP employment growth. DMP sales data are compared to whole economy nominal GDP growth at current market prices. DMP employment (for the
private sector) is compared to ONS/HMRC data on the number of payrolled employees. DMP and SBU data are adjusted to match the mean and variance of growth
                                                                                                                                                       29 in the
corresponding ONS, HMRC, GDP, and ADP series over the time period shown on each chart.
  Figure 3 Sales and Employment Forecasts vs Realizations
                                 Panel A Sales growth                                                     Panel B Employment growth



US Firms
(SBU)




UK Firms
(DMP)



Notes: This figure shows binned scatter plots of the relationship between expected year-ahead sales growth and annual sales growth a year later at the firm level (Panel A)
and expected year-ahead employment growth and annual employment growth a year later (Panel B). The sample from the SBU covers 2014-2025. The sample from the
                                                                                                                                                                30
UK DMP covers 2017-2025.
     Figure 4A Current use of AI technologies by businesses
                               100
                                               95
                                                                                                                                            All Firms (N=8879)
                                90                                      88
                                                           82
                                80
                                     78                                             78                                                      US SBU (N=1012)

                                                                                                68                                          Canada (N=872)




Percentage of businesses (%)
                                70
                                                                                                            64

                                60                                                                                       56                 UK DMP (N=1964)
                                50
                                                                                                                                            DE BOP-F (N=2303)
                                40
                                                                                                                                            AUS BOSS (N=908)
                                30
                                                                                                                                            Mexico (N=1719)
                                20


                                10
                                                                                                                                            S. Africa (N=101)

                                 0
                                                                   Any AI Tech

Notes: This figure is based on responses to the question: “Which of the following artificial intelligence technologies, if any, does your business currently use?” Firms could
select more than one option. The results for all firms is the average of the seven surveys, weighted by the respective number of responses. The data for all seven
countries was collected over May to July 2026. The results for the US, UK, Germany, and Mexico are employment-weighted. The results for Canada, Australia, 31       and South
Africa are equal-weighted.
 Figure 4B Current use of AI technologies by businesses
                                 100

                                  90                                                                                                                              88
                                                                                                                                                                            82
                                  80
                                                                                                                                                                       74




  Percentage of businesses (%)
                                                                                                                                                                                 70
                                  70
                                                                                                                                                             63
                                  60

                                  50                                              47
                                                                                            42                            43        43
                                                                                                                                                                                      38
                                  40        36                                                             36        34
                                                                             33                                                          33        34                                                      33        32
                                                                                                      28                                                                                        30
                                  30                                                                                                                    28                                 27
                                                      23               24                                       24                            25
                                                                                       21        23                            23                                                                     22                          22
                                       19                  19 20                                                                                                                                                          17 17
                                  20
                                                 12                                                                                                                                                                                    12                             13
                                                                                                                                                                                                                10                              11       10
                                                                   8                                                                                                                                                                        8                              9
                                  10                                                                                                                                                                                                                              7
                                                                                                                                                                                                                                                     4        4

                                   0
                                                      Other                 Data processing using ML                 Visual content creation                       Generative AI                     Image processing using ML Robotics and autonomous
                                                                                                                                                                                                                                       vehicles
                                                                            All Firms (N=8879)                                            US SBU (N=1012)                                               Canada (N=872)
                                                                            UK DMP (N=1964)                                               DE BOP-F (N=2303)                                             AUS BOSS (N=908)
                                                                            Mexico (N=1719)                                               S. Africa (N=101)
Notes: This figure is based on responses to the question: “Which of the following artificial intelligence technologies, if any, does your business currently use?” Firms could
select more than one option. The data for all seven countries was collected over May to July 2026. The results for all firms is the average of the seven surveys, weighted
by the respective number of responses. The results for the US, UK, Germany, and Mexico are employment-weighted. The results for Canada, Australia, and South         32 Africa
are equal-weighted.
   Figure 5 AI Spending per Employee
         Panel A US Firms (SBU)                                                                 Panel B UK Firms (DMP)




Notes: Respondents were asked to answer the following two question: (1) Thinking back to last year (calendar year 2025), approxima tely how much did your firm spend on
artificial intelligence adoption and AI related technologies? Include software, subscription services, hardware, worker training and IT staff support. (2) Now think about this
year. For calendar year 2026, approximately how much do you expect your firm will spend on artificial intelligence adoption and AI related technologies? Include software,
subscription services, hardware, worker training and IT staff support. Panel is based on 845 responses from firms in the US Survey of Business Uncertainty in March 2026.
Panel B is based on 1273 responses to the Decision Maker Panel in August-September 2026. Original responses in Panel B are in GBP and converted to USD using           33
exchange rate of 1.35 $/£"
   Figure 6 Firm AI spending is highly skewed




                                                                                                                                                         2% of firms
                                                                                                                                                         account for
                                                                                                                                                         over 50% of
                                                                                                                                                         AI spend in
                                                                                                                                                         the UK and
                                                                                                                                                         US




Notes: This figure is based on responses to the question: For calendar year 2026, approximately how much do you expect your firm will spend on artificial intelligence
adoption and AI related technologies? Include software, subscription services, hardware, worker training and IT staff support . The results are based on 845 responses from
firms in the US Survey of Business Uncertainty in March 2026 and 1,273 responses to the Decision Maker Panel in August-September 2026.                             34
 Figure 7A Frequency of AI use by survey respondent
   3.0
                                                                                                                                    All Firms (N=9224)
                                         2.5
                                                    2.5
   2.5
                                                                                                                                    US SBU (N=1097)
                                                              2.2
                   2.1                                                   2.1
                                                                                    2.0
   2.0                                                                                                   1.9                        Canada (N=873)
                                                                                               1.7

                                                                                                                                    UK DMP (N=2014)
 Hours
   1.5

                                                                                                                                    DE BOP-F (N=2492)
   1.0
                                                                                                                                    AUS BOSS (N=908)

   0.5                                                                                                                              Mexico (N=1719)


   0.0
                                                                                                                                    S. Africa (N=121)
                                Average weekly use of AI by survey respondent

Notes: This figure is based on responses to the question: “On average, how frequently do you personally use artificial intelligenc e technologies in a typical working week?”
The results for all firms is the average of the seven surveys, weighted by the respective number of responses. To calculate t he average use per week, values are assigned
to each of the options: 0 to “Not at all”; 0.5 to “up to 1 hour a week”; 3 to “1 to 5 hours a week”; 7.5 to “>5 hours a week”. The data for all seven countries was collected
over May to July 2026. The results for the US, UK, Germany, and Mexico are employment-weighted. The results for Canada, Australia, and South Africa are equal-
                                                                                                                                                                      35
weighted.
 Figure 7B Frequency of AI use by survey respondent
                                    45

                                                                                                39
                                    40
                                                                                                     37                     37
                                                                                   35                     35 35
                                    35




    Percentage of respondents (%)
                                                                                                                  31             32 32
                                                                                                                       30
                                                                                        29 30                                                    29
                                                                                                                                                      30
                                    30
                                                                                                                                         28 28
                                                                          27 27
                                                                     24
                                    25
                                                              22
                                         21        20
                                    20                                                                                                                                  18
                                              17                                                                                                                   17
                                                         15
                                    15                                                                                                                        13             13 14 13
                                                                                                                                                                                              12
                                    10                                                                                                                                                    9


                                     5


                                     0
                                                        Not at all                       Up to 1 hour a week                 1 to 5 hours a week                        >5 hours a week

                                                                   All Firms (N=9224)       US SBU (N=1097)            Canada (N=873)                  UK DMP (N=2014)

                                                                   DE BOP-F (N=2492)        AUS BOSS (N=908)           Mexico (N=1719)                 S. Africa (N=121)
Notes: This figure is based on responses to the question: “On average, how frequently do you personally use artificial intelligenc e technologies in a typical working week?”
The data for all seven countries was collected over May to July 2026. The results for all firms is the average of the seven surveys, weighted by the respective number of
responses. The results for the US, UK, Germany, and Mexico are employment-weighted. The results for Canada, Australia, and South Africa are equal-weighted.36
Figure 8A Impact of AI on employment over past 3 years
                                                                                                                1.00
                                                                                                                                      All Firms (N=8744)
                                                                                                                0.50
                                                                                     0.22
                                             0.06                                                                                     US SBU (N=974)
               0.06                0.10                          0.07
                                                                                                                0.00
                                                                           -0.01                                                      Canada (N=799)
                                                       -0.09




                                                                                                                        Percent (%)
                                                                                               -0.11
                                                                                                                -0.50                 UK DMP (N=1988)

                                                                                                                -1.00
                                                                                                                                      DE BOP-F* (N=2240)

                                                                                                                                      AUS BOSS (N=908)
                                                                                                                -1.50

                                                                                                                                      Mexico (N=1719)
                                                                                                                -2.00
                                                                                                                                      S. Africa (N=116)
                                                                                                                -2.50
                                     Cumulative impact over past 3 years (%)

Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected the number of employees in your business
over the past three years?” To calculate the average impacts, values are assigned to each of the options: large negative/large positive impacts are treated as ±7.5%;
small negative/small positive impacts are treated as ±2.5%. 90% confidence intervals are shown for these impacts. The data for the US, Canada, the UK, Australia,
Mexico, and South Africa were collected over May-July 2026. The data for Germany were collected in January 2026. The results for all firms is the average of the seven
surveys, weighted by the respective number of responses. The results for the US, UK, Germany, and Mexico are employment-weighted. The results for Canada, Australia,
and South Africa are equal-weighted.                                                                                                                             37
  Figure 8B Impact of AI on employment over past 3 years
                                    100                                                                                     95

                                     90                                                                       87 88 88 88
                                                                                                                                           82
                                                                                                                                      80
                                     80                                                                                          74




     Percentage os businesses (%)
                                     70

                                     60

                                     50

                                     40

                                     30

                                     20
                                                                                               8                                                                     10 10
                                     10                                                7           7                                                                         8
                                                               4       4   5   5   4                   4                                        5   6        4
                                                  2                                        1                                                            4        2               2       3           3   3   2
                                          1   0       1    0       1                                                                                                                 1       1   1
                                      0
                                              Large negative >5%               Small negative <5%                     No impact                     Small positive <5%               Large positive >5%
                                                                                                       Impact of AI on employment past 3 years

                                                          All Firms (N=8744)           US SBU (N=974)                  Canada (N=799)                       UK DMP (N=1988)

                                                          DE BOP-F* (N=2240)           AUS BOSS (N=908)                Mexico (N=1719)                      S. Africa (N=116)

Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected t he number of employees in your business
over the past three years?” The data for the US, Canada, the UK, Australia, Mexico, and South Africa were collected over May-July 2026. The data for Germany were
collected in January 2026. The results for all firms is the average of the seven surveys, weighted by the respective number of responses. The results for the US, UK,
                                                                                                                                                                   38
Germany, and Mexico are employment-weighted. The results for Canada, Australia, and South Africa are equal-weighted.
 Figure 9A Expected impact of AI on employment over next 3 years
                                                                                                                             1.00
                                                                                                0.6
                                                                                                           0.06                                    All Firms (N=8869)
                                                                                                                             0.50

                                                                                                                                                   US SBU (N=1030)
                                                                                                                             0.00
                 -0.40                                                                                                                             Canada (N=841)
                                                                          -0.06
                                                   -0.1



                                                                                                                                     Percent (%)
                                                                                                                             -0.50
                                                                                                                                                   UK DMP (N=1964)
                                                                                      -0.50
                                                                                                                             -1.00                 DE BOP-F* (N=2289)

                                       -1.26                                                                                 -1.50                 AUS BOSS (N=908)
                                                              -1.31

                                                                                                                                                   Mexico (N=1719)
                                                                                                                             -2.00

                                                                                                                                                   S. Africa (N=118)
                                                                                                                             -2.50
                                               Average impact over next 3 years (%)


Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected t he number of employees in your business
over the past three years? And how do you expect this to affect your number of employees over the next 3 years?” To calculate the average impacts, values are assigned
to each of the options: large negative/large positive impacts are treated as ±7.5%; small negative/small positive impacts are treated as ±2.5%. 90% confidence intervals
are shown for these impacts. The data for the US, Canada, the UK, Australia, Mexico, and South Africa were collected over May-July 2026. The data for Germany were
collected in January 2026. The results for all firms is the average of the seven surveys, weighted by the respective number of responses. The results for the US, UK,
Germany, and Mexico are employment-weighted. The results for Canada, Australia, and South Africa are equal-weighted.                                               39
Figure 9B Expected impact of AI on employment over next 3 years
                                     100

                                      90
                                                                                                                                         81
                                      80




      Percentage of businesses (%)
                                      70

                                                                                                                     57                            59
                                      60                                                                                       54
                                                                                                                                              52        52
                                      50
                                                                                                                                    41
                                      40                                           36                                     38
                                                                                             35

                                      30
                                                                              20        20
                                      20                                                                        17                                                                 16 17
                                                                 14                                   15
                                               12       12                                                 12                                                10 10 11 9       11
                                           8                                                      7                                                                                              8         9 10 8
                                      10            7                     7                                                                                               6                6 4
                                                             3        4                                                                                                                              3 3
                                       0
                                               Large negative >5%                  Small negative <5%                          No impact                       Small positive <5%           Large positive >5%
                                                                                                       Expected impact of AI on employment next 3 years

                                                             All Firms (N=8869)                       US SBU (N=1030)                         Canada (N=841)                  UK DMP (N=1964)
                                                             DE BOP-F* (N=2289)                       AUS BOSS (N=908)                        Mexico (N=1719)                 S. Africa (N=118)

Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected the number of employees in your business
over the past three years? And how do you expect this to affect your number of employees over the next 3 years?” The data for the US, Canada, the UK, Australia,
Mexico, and South Africa were collected over May-July 2026. The data for Germany were collected in January 2026. The results for all firms is the average of the seven
surveys, weighted by the respective number of responses. The results for the US, UK, Germany, and Mexico are employment-weighted. The results for Canada,40       Australia,
and South Africa are equal-weighted.
Figure 10A Impact of AI on productivity over past 3 years

                                                                                                                 3.50
                                                                                                                                       All Firms (N=8438)
                                                                                                                 3.00
                                                                                                                                       US SBU (N=964)
                                                                                                                 2.50
                                                                                                                                       Canada (N=517)
                                                                                                                 2.00
                                                                                                                                       UK DMP (N=1964)

                                                                                                                         Percent (%)
                                                                                                                 1.50
                                                                                                                                       DE BOP-F* (N=2251)
                                                                                       0.72                      1.00

                                                          0.54                                                                         AUS BOSS (N=908)
                  0.46                0.48     0.36
                                                                                                 0.04            0.50
                                                                   0.24
                                                                             0.47                                                      Mexico (N=1719)
                                                                                                                 0.00

                                                                                                                                       S. Africa (N=115)
                                                                                                                 -0.50
                                       Cumulative impact over past 3 years (%)

Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected the volume of sales per employee in your
business over the past three years?” To calculate the average impacts, values are assigned to each of the options: large negative/large positive impacts are treated as
± 7.5%; small negative/small positive impacts are treated as ±2.5%. 90% confidence intervals are shown for these impacts. The data for the US, Canada, the UK,
Australia, Mexico, and South Africa were collected over May-July 2026. The data for Germany were collected in January 2026. The results for all firms is the average of
the seven surveys, weighted by the respective number of responses. The results for the US, UK, Germany, and Mexico are employment-weighted. The results for      41
Canada, Australia, and South Africa are equal-weighted.
Figure 10B Impact of AI on productivity over past 3 years
                                  100
                                                                                                                     91
                                   90                                                                      85                       84
                                                                                                   83 83        82        82
                                   80                                                                                          75




   Percentage os businesses (%)
                                   70

                                   60

                                   50

                                   40

                                   30
                                                                                                                                                                  20
                                   20                                                                                                                14
                                                                                                                                         12 14
                                                                                                                                                 9            9        8
                                   10                                                                                                                     6                                 5 4
                                                       1 0    3     1 1 2 1         3 2 3                                                                                  3 2 3 3      2          2
                                        0 0 1 0    0                              0
                                    0
                                         Large negative >5%           Small negative <5%                    No impact                       Small positive <5%                Large positive >5%
                                                                                           Impact of AI on productivity past 3 years

                                                             All Firms (N=8438)       US SBU (N=964)                           Canada (N=517)                     UK DMP (N=1964)
                                                             DE BOP-F* (N=2251)       AUS BOSS (N=908)                         Mexico (N=1719)                    S. Africa (N=115)
Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected the volume of sales per employee in your
business over the past three years?” The data for the US, Canada, the UK, Australia, Mexico, and South Africa were collected over May-July 2026. The data for Germany
were collected in January 2026. The results for all firms is the average of the seven surveys, weighted by the respective number of responses. The results for the US, UK,
                                                                                                                                                                 42
Germany, and Mexico are employment-weighted. The results for Canada, Australia, and South Africa are equal-weighted.
Figure 11A Expected impact of AI on productivity over next 3 years

                                                                                                                          4.00

                                                                                                                                               All Firms (N=8568)
                                                                                                                          3.50

                                                                                                                                               US SBU (N=1018)
                                                                                                                          3.00
                                                                                                                                               Canada (N=542)
                                                                                                                          2.50



                                                                                                                                 Percent (%)
                                                                                                                                               UK DMP (N=1964)
                                                                                                                          2.00
                                                                                                                                               DE BOP-F* (N=2299)
                                                                                                                          1.50
                                                            2.62                                        0.61                                   AUS BOSS (N=908)
                                      2.33
                                                 2.02                                                                     1.00
                                                                                             1.85
                1.70                                                                                                                           Mexico (N=1719)
                                                                        0.87                                              0.50
                                                                                    0.73                                                       S. Africa (N=118)
                                                                                                                          0.00
                                             Average impact over next 3 years (%)

Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected volume of sales per employee in your
business over the past three years? And how do you expect this to affect your volume of sales per employee over the next 3 years?” To calculate the average impacts,
values are assigned to each of the options in Panel A: large negative/large positive impacts are treated as ±7.5%; small negative/small positive impacts are treated as
± 2.5%. 90% confidence intervals are shown for these impacts. The data for the US, Canada, the UK, Australia, Mexico, and South Africa were collected over May-July
2026. The data for Germany were collected in January 2026. The results for all firms is the average of the seven surveys, wei ghted by the respective number of
responses. The results for the US, UK, Germany, and Mexico are employment-weighted. The results for Canada, Australia, and South Africa are equal-weighted.     43
Figure 11B Expected impact of AI on productivity over next 3 years
                                    100

                                     90

                                     80
                                                                                                                     72




     Percentage of businesses (%)
                                     70                                                                                   66

                                     60
                                                                                                 53                            54 55
                                                                                                           50
                                     50

                                     40                                                                                                     38        38
                                                                                                      36        35

                                     30                                                                                                27                            28
                                                                                                                                                 25                       25                24
                                                                                                                                                                                    22 21
                                                                                                                                                           19
                                     20                                                                                                                         15             16                         16
                                                                                                                                                                                                     10
                                     10                         6                            6                                                                                                   7             8
                                                        4                           5
                                          1 2 2 1 1                  2 3 2 2 1           2
                                                            0
                                      0
                                           Large negative >5%          Small negative <5%                   No impact                       Small positive <5%                      Large positive >5%
                                                                                    Expected impact of AI on productivity next 3 years
                                                            All Firms (N=8568)          US SBU (N=1018)                    Canada (N=542)                        UK DMP (N=1964)
                                                            DE BOP-F* (N=2299)          AUS BOSS (N=908)                   Mexico (N=1719)                       S. Africa (N=118)
Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected volume of sales per employee in your
business over the past three years? And how do you expect this to affect your volume of sales per employee over the next 3 years?” The data for the US, Canada, the
UK, Australia, Mexico, and South Africa were collected over May-July 2026. The data for Germany were collected in January 2026. The results for all firms is the average
of the seven surveys, weighted by the respective number of responses. The results for the US, UK, Germany, and Mexico are employment-weighted. The results44for
Canada, Australia, and South Africa are equal-weighted.
  Table 1 Characteristics of firms using AI and covariates of expected
  impacts (UK Firms)
                                                    (1)             (2)         (3)            (4)       (5)           (6)        (7)           (8)        (9)            (10)
  Dependent Variable:                               Any AI Technology       AI Spending per Employee   Average Weekly AI Use   Expected AI Employment    Expected AI Productivity
                                                      Currently Used              in 2026 (logs)              (hours)          Impact Next 3 Years (%)   Impact Next 3 Years (%)
                                                      (scaled by 100)
  Labor productivity (logs)                         0.48           0.50        0.09          0.10       -0.02         0.01       0.15          0.08         0.01           0.02
                                                   (1.41)         (1.41)      (0.10)        (0.10)      (0.09)       (0.09)     (0.12)        (0.12)       (0.12)         (0.12)
  Employment (logs)                                3.24***        3.21***    -0.15***      -0.15***      0.04         0.04     -0.15***      -0.16***     0.14***        0.14***
                                                   (0.48)         (0.48)      (0.04)        (0.04)      (0.03)       (0.03)     (0.04)        (0.04)       (0.04)         (0.04)
  Average Wage per Employee (logs)                 7.41***        7.42***    0.74***       0.72***     0.34***      0.35***      -0.24        -0.25         0.29           0.29
                                                   (2.19)         (2.20)      (0.15)        (0.15)      (0.13)       (0.13)     (0.18)        (0.18)       (0.18)         (0.18)
  Firm Age                                          0.06           0.06       -0.01         -0.00       -0.00        -0.00       -0.00        -0.00        -0.00          -0.00
                                                   (0.06)         (0.06)      (0.00)        (0.00)      (0.00)       (0.00)     (0.00)        (0.00)       (0.00)         (0.00)
  Average Age of Directors                        -0.52***       -0.52***     -0.01         -0.01      -0.03***     -0.03***     0.02*        0.02**      -0.02**        -0.02**
                                                   (0.13)         (0.13)      (0.01)        (0.01)      (0.01)       (0.01)     (0.01)        (0.01)       (0.01)         (0.01)
  Average productivity growth (2025)                -0.01                      0.00                      0.00                    -0.00                      0.00
                                                   (0.09)                     (0.01)                    (0.01)                  (0.01)                     (0.01)
  Expected productivity growth (2025)               0.27                      0.03**                    0.02**                  -0.03**                    0.03**
                                                   (0.17)                     (0.01)                    (0.01)                  (0.01)                     (0.01)
  Average real sales growth (2025)                                 0.00                      0.00                      0.00                    0.01                       -0.00
                                                                  (0.07)                    (0.01)                    (0.00)                  (0.01)                     (0.01)
  Expected real sales growth (2025)                                0.10                     0.03**                     0.01                    -0.00                     0.04***
                                                                  (0.15)                    (0.01)                    (0.01)                  (0.01)                     (0.01)
  Average employment growth (2025)                                 0.02                     -0.01*                   -0.01**                  0.02***                     -0.00
                                                                  (0.09)                    (0.01)                    (0.01)                  (0.01)                     (0.01)
  Expected employment growth (2025)                                0.05                     -0.00                     -0.01                   0.06***                     -0.00
                                                                  (0.16)                    (0.01)                    (0.01)                  (0.01)                     (0.01)
  Mean of Dependent Variable                        76.7           76.7        5.7            5.7        1.9            1.9      -1.0           -1.0       2.4             2.4
  SIC2 industry and time fixed effects              Yes            Yes         Yes           Yes         Yes           Yes       Yes            Yes        Yes             Yes
Notes: The data in Columns 1-2 and 5-10 in the UK Decision Maker Panel was collected over February-April 2025, November 2025 – January 2026, and May-July 2026 with
the latest firm observation used in the regressions. The data on AI spending in 2026 was collected over August-September 2026. A constant has also been estimated, but not
reported in the table. Where data are missing for a particular variable a dummy variable is included to account for that (results not reported). Standard errors are clustered at
                                                                                                                                                                      45
the firm level, stars indicate *** p<0.01, ** p<0.05, * p<0.1.
    Table 2 Distribution of AI spending per employee
                                                          US Firms (SBU)                                                    UK Firms (DMP)

                                                 2025                             2026                              2025                             2026

        10th percentile                            $0                               $0                               $0                                $0

        25th percentile                           $11                              $41                               $0                               $26

        50th percentile                          $125                             $294                               $41                             $136

        75th percentile                          $746                            $1,366                             $223                             $450

        90th percentile                         $2,400                           $5,000                             $649                           $1,380

               Mean                             $1,363                           $2,043                             $422                             $725

       Top 10% of Firms                         $5,129                           $7,480                           $3,408                           $5,197

Notes: This table shows the distribution of AI spending per employee (employment weighted) using data collected from the US and UK. Respondents were asked to answer
the following two question: (1) Thinking back to last year (calendar year 2025), approximately how much did your firm spend on artificial intelligence adoption and AI related
technologies? Include software, subscription services, hardware, worker training and IT staff support. (2) Now think about th is year. For calendar year 2026, approximately
how much do you expect your firm will spend on artificial intelligence adoption and AI related technologies? Include software , subscription services, hardware, worker
training and IT staff support. Columns 1-2 based on 845 responses from firms in the US Survey of Business Uncertainty in March 2026. Columns 3-4 are based on 1,273
                                                                                                                                                                    46
responses to the Decision Maker Panel in August-September 2026. Original responses in Columns 3-4 are in GBP and converted to USD using exchange rate of 1.35 $/£"
 Table 3 Expected AI contributions to productivity over next 3 years: Splitting
 up into labour productivity and TFP impacts (UK)

        Summary - Average impacts on annual growth (pp)


                                                                                              Last 3 years                           Next 3 years


        Sales per employee                                                                           0.18                                   0.69
        Labor productivity (GVA per employee)                                                        0.17                                   0.85
        Total Factor Productivity (TFP)                                                              0.13                                   0.68

Notes: The calculations combine estimated effects of AI adoption on firms' sales per employee, employment with aggregate UK national accounts data and data on AI-
related expenditures. Aggregate output is calculated as employment multiplied by sales per employee, while gross value added (GVA) equals output less intermediate
consumption. AI spending data is based on data collected from the DMP over August-September 2026 and is assumed to increase intermediate consumption in proportion
to employment (£313 and £537 per worker per year in the past 3 years and next 3 years, respectively). Labour productivity is measured as GVA per worker. The
contribution to total factor productivity (TFP) is derived using a standard growth-accounting framework, calculated as the change in GVA less the weighted contributions of
labour and capital inputs, with labour and capital shares of 0.67 and 0.33, respectively. Capital deepening is assumed to ref lect AI-related expenditure equivalent to 6% of
the aggregate capital stock. Reported figures are expressed as average annual contributions to growth over a three-year horizon.                                   47
Table 4 Summary of realised and expected AI contributions
                                                                                          Firms
                                                                                                Germany          Australia
                                All          US (SBU)          Canada          UK (DMP)                                            Mexico        South Africa
                                                                                                (BOP-F)*          (BOSS)
 Cumulative impact over past 3 years (%)

 Sales/Employee                0.46             0.48             0.36             0.54             0.24             0.47             0.72             0.04

 Employment                    0.06             0.10             0.06             -0.09            0.07             -0.01            0.22             -0.11

 Output (implied)              0.52             0.58             0.42             0.44             0.32             0.46             0.95             -0.06

 Expected cumulative impact over next 3 years (%)

 Sales/Employee                1.70             2.33             2.02             2.62             0.87             0.73             1.85             0.61

 Employment                   -0.40            -1.26            -0.08             -1.31            -0.06            -0.50            0.585            0.06

 Output (implied)              1.30             1.07             1.94             1.31             0.81             0.23             2.43             0.68

Notes: This table summarises the realised and expected AI impacts on sales per employee and employment from Figures 8-11. The implied impacts on output are
calculated as the sum of the sales/employee and employment impacts. The data for the US, Canada, the UK, Australia, Mexico, a nd South Africa were collected over
May-July 2026. The data for Germany were collected in January 2026. The results for all firms is the average of the seven survey s, weighted by the respective
number of responses. The results for the US, UK, Germany, and Mexico are employment-weighted. The results for Canada, Australia, and South Africa are equal-   48
weighted.
Figure A1 SBU vs. US industrial and regional distribution

Panel A: By Industry                                                                    Panel B: By Region




Notes: This figure compares the percentage of firms by industry (Panel A) and region (Panel B) in the US Survey of Business Uncertainty against the 2022 Economic
Census. The shares are employment-weighted. Panel A is based on 6835 firms in the SBU. Panel B is based on 6995 firms in the SBU.
                                                                                                                                                            49
Figure A2 DMP vs. UK industrial and regional distribution

Panel A: By Industry                                                                        Panel B: By Region




Notes: Other production includes agriculture; forestry & fishing; mining & quarrying; electricity, gas & air conditioning supply; water supply; and sewerage, waste
management & remediation activities. Data are averages from 2017 to 2025.
                                                                                                                                                                   50
Figure A3 Firm responses vs. company accounts data (UK firms)




Notes: Sales values from the DMP survey are annualised average quarterly sales reported by businesses across the year. DMP employmen t data are averages across the
year. DMP data are plotted against annual company accounts data from Bureau Van Dijk for the corresponding financial year. The dots on the top charts each represent 5% of
                                                                                                                                                             51
observations, grouped by log employment/sales from accounts data. Charts are based on annual data between 2017 and 2024.
 Figure A4 Current use of AI technologies by businesses
                                    100

                                     95
                                                                                                                                                US SBU
                                     90

                                                                                                                                                UK DMP




     Percentage of businesses (%)
                                     85

                                     80
                                                                                                                                                DE BOP-F
                                     75

                                     70                                                                                                         AUS BOSS

                                     65
                                                                                                                                                Canada
                                     60

                                     55                                                                                                         Mexico
                                     50
                                          Feb-Apr 2025                      Nov-25 to Jan-26                May-July 2026
                                                                                                                                                S. Africa
                                                    Businesses currently using at least one AI technology

Notes: This figure is based on responses to the question: “Which of the following artificial intelligence technologies, if any, does your business currently use?” Firms could
select more than one option. The results for the US, UK, Germany, and Mexico are employment-weighted. The results for Canada, Australia, and South Africa are        52equal-
weighted.
Figure A5.a Characteristics of firms using AI technologies (UK Firms)
   Panel A Labor Productivity       Panel B Firm employment   Panel C Average wage per employee




 Panel D Average age of directors   Panel E Firm age




                                                                   Notes: This figure shows binned scatter plots.
                                                                   The vertical axis is the percentage of businesses
                                                                   currently using any AI technology. The data are
                                                                   from the UK Decision Maker Panel, collected
                                                                   over February-April 2025, November 2025 –
                                                                   January 2026, and May-July 2026 with the latest
                                                                   firm observation used in the figures.

                                                                                                           53
   Figure A5.b Characteristics of firms using AI technologies (US Firms)
   Panel A Labor Productivity                                                               Panel B Firm employment




Notes: This figure shows binned scatter plots. The vertical axis is the percentage of businesses currently using any AI technology. The data are from the US Survey of Business
Uncertainty, collected in November 2025 and June 2026. Labor productivity is defined as sales revenue per employee, and deflated using 2016 gross output deflators.
                                                                                                                                                                  54
  Figure A6 Current and expected AI adoption by industry (UK firms)
        Panel A Current AI Adoption                                                          Panel B Expected Adoption Next 3 Years




Notes: This figure is based on responses to the question: “Which of the following artificial intelligence technologies, if any, does your business currently use? And which do you
intend to make use of over the next three years?” The results are based on responses from the UK Decision Maker Panel, collected over May-July 2026. The results are
employment-weighted.                                                                                                                                                 55
Figure A7 Role of firm size, weighting, and respondent position on AI
adoption metrics (UK firms)

 Panel A AI adoption by    Panel B AI adoption by    Panel C AI adoption by
 firm size                 survey weighting          respondent position




                                                                         56
 Figure A8.1 Expected use of AI technologies over next 3 years
                                 100           96
                                                                      91
                                  90                                                                                                          All Firms (N=8610)
                                       82                  83
                                                                                  80
                                  80
                                                                                                         73
                                                                                                                                              US SBU (N=902)
                                                                                             73
                                                                                                                    71




  Percentage of businesses (%)
                                  70
                                                                                                                                              Canada (N=868)
                                  60
                                                                                                                                              UK DMP (N=1964)
                                  50


                                  40                                                                                                          DE BOP-F (N=2148)

                                  30
                                                                                                                                              AUS BOSS (N=908)
                                  20
                                                                                                                                              Mexico (N=1719)
                                  10

                                                                                                                                              S. Africa (N=101)
                                   0
                                                                  Any AI Tech


Notes: This figure is based on responses to the question: “Which of the following artificial intelligence technologies, if any, does your business currently use? And which
do you intend to make use of over the next three years?” Firms could select more than one option. The results for all firms is the average of the seven surveys, weighted
by the respective number of responses. The data for all seven countries was collected over May to July 2026. The results for the US, UK, Germany, and Mexico57      are
employment-weighted. The results for Canada, Australia, and South Africa are equal-weighted.
 Figure A8.2 Expected use of AI technologies over next 3 years
                                   80
                                                                                                                                                                           71
                                   70

                                                                                     60




    Percentage of businesses (%)
                                   60                                                          58
                                             52                                                                                                                                 52
                                                                                          51                                                                                                                   50
                                                                                49                            48 47        48                            48           48
                                   50
                                                                                                                                     44                          45
                                                                                                                                                                                     42                                  41
                                                                                                    40                39        39                  40
                                   40                  37                                                37                                                                                         38
                                                                          35                                                                   34                                         35              34                            33             34
                                                                                                                                          31                                                   33                                  32
                                                            30
                                   30   28                                                                                                                                                                                    27             28                            27 27
                                                                                                                                                                                                                    26
                                                  22             21                                                                                                                                                                               22             22
                                   20                                                                                                                                                                                                                                 16
                                                                                                                                                                                                                                                            14                     15
                                                                      9
                                   10


                                    0
                                                       Other                   Data processing using ML               Visual content creation                          Generative AI                     Image processing using ML Robotics and autonomous
                                                                                                                                                                                                                                           vehicles

                                                        All Firms (N=8610)                                US SBU (N=902)                                      Canada (N=868)                                UK DMP (N=1964)

                                                        DE BOP-F (N=2148)                                 AUS BOSS (N=908)                                    Mexico (N=1719)                               S. Africa (N=101)
Notes: This figure is based on responses to the question: “Which of the following artificial intelligence technologies, if any, does your business currently use? And which
do you intend to make use of over the next three years?” Firms could select more than one option. The results for all firms is the average of the seven surveys, weighted
by the respective number of responses. The data for all seven countries was collected over May to July 2026. The results for the US, UK, Germany, and Mexico are
                                                                                                                                                                    58
employment-weighted. The results for Canada, Australia, and South Africa are equal-weighted.
 Figure A8.3 Expected use of AI technologies over next 3 years
                                    100

                                     95
                                                                                                                                               US SBU
                                     90




     Percentage of businesses (%)
                                     85
                                                                                                                                               UK DMP

                                     80
                                                                                                                                               DE BOP-F
                                     75

                                     70                                                                                                        AUS BOSS

                                     65
                                                                                                                                               Canada
                                     60

                                     55                                                                                                        Mexico
                                     50
                                          Feb-Apr 2025                      Nov-25 to Jan-26                     May-July 2026
                                                                                                                                               S. Africa
                                                    Businesses expecting to use any AI technology over next 3 years

Notes: This figure is based on responses to the question: “Which of the following artificial intelligence technologies, if any, does your business currently use? And which
do you intend to make use of over the next three years?” Firms could select more than one option. The results for the US, UK, Germany, and Mexico are employment-
weighted. The results for Canada, Australia, and South Africa are equal-weighted.                                                                                   59
Figure A9 Covariates of AI spending per employee (UK Firms)
  Panel A Labor Productivity       Panel B Firm employment   Panel C Average wage per employee




Panel D Average age of directors   Panel E Firm age



                                                                  Notes: The vertical axis is based on the
                                                                  question: “For calendar year 2026,
                                                                  approximately how much do you expect your firm
                                                                  will spend on artificial intelligence adoption and
                                                                  AI related technologies? Include software,
                                                                  subscription services, hardware, worker training
                                                                  and IT staff support.” The data are from the UK
                                                                  Decision Maker Panel, collected over August-
                                                                  September 2026.
                                                                                                              60
   Figure A10 Distribution of AI spending per employee across US and
   UK firms in 2026




Notes: This figure is based on responses to the question: For calendar year 2026, approximately how much do you expect your firm will spend on artificial intelligence
adoption and AI related technologies? Include software, subscription services, hardware, worker training and IT staff support . The results are based on 845 responses from
                                                                                                                                                                   61
firms in the US Survey of Business Uncertainty in March 2026 and 1,273 responses to the Decision Maker Panel in August-September 2026.
 Figure A11 Frequency of AI use by survey respondent
         3.0


                                                                                                                                                US SBU
         2.5


                                                                                                                                                UK DMP
         2.0

                                                                                                                                                DE BOP-F
 Hours
         1.5

                                                                                                                                                AUS BOSS
         1.0

                                                                                                                                                Canada
         0.5

                                                                                                                                                Mexico
         0.0
                       Feb-Apr 2025                            Nov-25 to Jan-26                          May-July 2026
                                                                                                                                                S. Africa
                                      Average weekly use of AI by survey respondent

Notes: This figure is based on responses to the question: “On average, how frequently do you personally use artificial intelligenc e technologies in a typical working week?”
The results for all firms is the average of the seven surveys, weighted by the respective number of responses. To calculate t he average use per week, values are assigned
to each of the options: 0 to “Not at all”; 0.5 to “up to 1 hour a week”; 3 to “1 to 5 hours a week”; 7.5 to “>5 hours a week”. The results for the US, UK, Germany, and Mexico
are employment-weighted. The results for Canada, Australia, and South Africa are equal-weighted.                                                                     62
  Figure A12.a Frequency of AI use by survey respondent: Heterogeneity by
  firm characteristics (UK Firms)

       Panel A Firm age                                                               Panel B Average age of firm directors




Notes: The binned scatter plots are based on responses from the UK Decision Maker Panel, collected over February-March 2025, November 2025 – January 2026, and May-
July 2026.                                                                                                                                             63
  Figure A12.b Frequency of AI use by survey respondent: Heterogeneity by
  firm age (US Firms)




Notes: This figure presents a binned scatter plot of average weekly AI use by the survey respondent again firm age. It is based on responses to the question: “On average,
how frequently do you personally use artificial intelligence technologies in a typical working week?” The data from the US Survey of Business Uncertainty was collected in
November 2025 and June 2026.                                                                                                                                     64
 Figure A13 Frequency of AI use by survey respondent: Heterogeneity by
 respondent position
      Panel A US Firms (SBU)                                                                   Panel B UK Firms (DMP)




Notes: This figure is based on responses to the question: “On average, how frequently do you personally use artificial intelligenc e technologies in a typical working week?”
The data from the US Survey of Business Uncertainty was collected in November 2025 and June 2026. The data from the UK Decision Maker Panel was collected over
November 2025 – January 2026 and May-July 2026. The data are employment-weighted.                                                                                   65
  Figure A14 Impact of AI on employment over past 3 years
                                               0.50


                                                                                                                                              US SBU




     Cumulative impact over past 3 years (%)
                                               0.00
                                                                                                                                              UK DMP


                                                                                                                                              AUS BOSS
                                               -0.50

                                                                                                                                              DE BOP-F


                                               -1.00                                                                                          Canada


                                                                                                                                              Mexico
                                               -1.50
                                                       Feb-Apr 2025                     Nov-25 to Jan-26        May-July 2026
                                                                                                                                              S. Africa
                                                                 Impact of AI on employment over past 3 years

Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected the number of employees in your business
over the past three years?” The results for the US, UK, Germany, and Mexico are employment-weighted. The results for Canada, Australia, and South Africa are equal-
weighted.                                                                                                                                                         66
   Figure A15 Realised and expected impacts of AI on employment
   by industry (UK Firms)
        Panel A Past 3 Years                                                                 Panel B Next 3 Years




Notes: The results are based on responses from the UK Decision Maker Panel, collected over May-July 2026. The results are employment-weighted.   67
Figure A16 Expected impact of AI on employment over next 3 years
                                             1.00


                                                                                                                                           US SBU




   Cumulative impact over next 3 years (%)
                                             0.50

                                                                                                                                           UK DMP

                                             0.00
                                                                                                                                           DE BOP-F


                                             -0.50                                                                                         AUS BOSS


                                                                                                                                           Canada
                                             -1.00


                                                                                                                                           Mexico
                                             -1.50
                                                     Feb-Apr 2025                     Nov-25 to Jan-26                 May-July 2026
                                                                                                                                           S. Africa
                                                               Expected impact of AI on employment over next 3 years
Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected the number of employees in your business
over the past three years? And how do you expect this to affect your number of employees over the next 3 years?” The results for the US, UK, Germany, and Mexico are
employment-weighted. The results for Canada, Australia, and South Africa are equal-weighted.                                                                     68
   Figure A17 Expected AI employment impacts by frequency of AI
   use (UK firms)




Notes: This figure shows the average expected impact of AI on employment over the next 3 years, split by how frequently the survey respondent uses AI in a typical working
week. Data from the UK Decision Maker Panel was collected over February-April 2025, November 2025 – January 2026, and May-July 2026 with the latest firm observation
used in figure.                                                                                                                                                 69
  Figure A18 Expected AI employment impacts and employment
  growth forecast errors (UK firms)
        Panel A Forecast error                                                                 Panel B Absolute forecast error




Notes: This figure shows binned scatter plots of the expected impacts of AI on employment and employment growth forecast errors. Forecast errors are defined at the firm
level as realised annual employment growth minus expected year-ahead employment growth reported a year earlier. The figures include firms with at least three non-missing
forecast error observations and forecast errors reported before the AI expectations are reported. The scatter plots control for industry fixed effects. Data from the 70
                                                                                                                                                                      UK
Decision Maker Panel was collected over February-April 2025, November 2025 – January 2026, and May-July 2026 with the latest firm observation used in figure.
  Figure A19 Realised and expected impacts of AI on productivity
  by industry (UK Firms)
        Panel A Past 3 Years                                                                 Panel B Next 3 Years




Notes: The results are based on responses from the UK Decision Maker Panel, collected over May-July 2026. The results are employment-weighted.   71
Figure A20 Impact of AI on productivity over past 3 years
                                              3.00


                                                                                                                                              US SBU
                                              2.50




    Cumulative impact over past 3 years (%)
                                                                                                                                              UK DMP
                                              2.00


                                                                                                                                              AUS BOSS
                                              1.50

                                                                                                                                              DE BOP-F
                                              1.00

                                                                                                                                              Canada
                                              0.50

                                                                                                                                              Mexico
                                              0.00
                                                     Feb-Apr 2025                       Nov-25 to Jan-26        May-July 2026
                                                                                                                                              S. Africa
                                                               Impact of AI on productivity over past 3 years


Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected the volume of sales per employee in your
business over the past three years?” The results for the US, UK, Germany, and Mexico are employment-weighted. The results for Canada, Australia, and South 72    Africa are
equal-weighted.
 Figure A21 Expected impact of AI on productivity over next 3 years
                                              3.00


                                                                                                                                             US SBU
                                              2.50




    Cumulative impact over next 3 years (%)
                                                                                                                                             UK DMP
                                              2.00


                                                                                                                                             AUS BOSS
                                              1.50

                                                                                                                                             DE BOP-F
                                              1.00

                                                                                                                                             Canada
                                              0.50

                                                                                                                                             Mexico
                                              0.00
                                                     Feb-Apr 2025                      Nov-25 to Jan-26                  May-July 2026
                                                                                                                                             S. Africa
                                                               Expected impact of AI on productivity over next 3 years


Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected volume of sales per employee in your
business over the past three years? The results for the US, UK, Germany, and Mexico are employment-weighted. The results for Canada, Australia, and South 73     Africa are
equal-weighted.
   Figure A22 Expected AI productivity impacts by frequency of AI
   use (UK firms)




Notes: This figure shows the average expected impact of AI on productivity over the next 3 years, split by how frequently the surv ey respondent uses AI in a typical working
week. Data from the UK Decision Maker Panel was collected over February-April 2025, November 2025 – January 2026, and May-July 2026 with the latest firm observation
used in figure.                                                                                                                                                     74
   Figure A23 Expected AI productivity impacts and sales growth
   forecast errors (UK firms)
        Panel A Forecast error                                                                    Panel B Absolute forecast error




Notes: This figure shows binned scatter plots of the expected impacts of AI on productivity and sales growth forecast errors. Forecast errors are defined at the firm level as
realised annual sales growth minus expected year-ahead sales growth reported a year earlier. The figures include firms with at least three non-missing forecast error
observations and forecast errors reported before the AI expectations are reported. The scatter plots control for industry fixed effects. Data from the UK Decision Maker
                                                                                                                                                                     75 Panel
was collected over February-April 2025, November 2025 – January 2026, and May-July 2026 with the latest firm observation used in figure.
   Figure A24 Relationship between expected employment and
   productivity impacts (UK firms)




Notes: This figure shows binned scatter plots. The vertical axis is the expected AI employment impact over the next 3 years. The horizontal axis is the expected AI
productivity impact over the next 3 years. The data are from the UK Decision Maker Panel, collected over February-April 2025, November 2025 – January 2026, and May-
                                                                                                                                                                  76
July 2026, with the latest firm observation used in the figures.
 Table A1 Breakdown of survey responses by firm size

                                                                                              Firms

Percentage of
businesses (%)                                                                             Germany             Australia               South
                                      US (SBU)          Canada          UK (DMP)                                              Mexico
                                                                                            (BOP-F)             (BOSS)                 Africa


                                          36.6             64.4             39.8                74.3               56.2         0      44.14
0-49 employees
                                          16.5             14.8             19.8                 8.7                6.0         0      20.72
50-99 employees
                                          19.5              9.6             19.7                 8.3               11.5        37.5    22.53
100-249 employees
                                          27.5              7.5             20.8                 8.7               26.4        62.5     8.1
250+ employees
                                         1012              872              1964               2366                908         1719     101
Number of Responses
Notes: This table provides a breakdown of the responses by firm size categories across the seven main surveys in the paper.
                                                                                                                                              77
Table A2 Role of firm size and respondent position on AI adoption metrics
                                             (1)                 (2)              (3)             (4)              (5)                       (6)                (7)
 Dependent Variable:                                                        Any AI Technology Currently Used (scaled by 100)
 =1 Respondent CEO or CFO                  6.84***            6.67***           7.11***        4.45***           5.04***                   5.57***            5.97***
                                           (1.73)             (1.72)            (1.66)          (1.68)           (1.70)                    (1.70)             (1.69)
 50-99 Employees                                                                                 2.15
                                                                                                (2.02)
 100-249 Employees                                                                             7.07***
                                                                                                (1.98)
 250+ Employees                                                                                15.94***
                                                                                                (1.89)
 Employment (logs)                                                                                               2.82***                   3.51***           3.62***
                                                                                                                 (0.45)                    (0.49)             (0.49)
 Labor productivity (logs)                                                                                                                 4.72***           4.59***
                                                                                                                                           (1.10)             (1.10)
 Firm Age                                                                                                                                                      0.06
                                                                                                                                                              (0.06)
 Average Age of Directors                                                                                                                                    -0.53***
                                                                                                                                                              (0.12)
 Mean of Dependent Variable                  69.0               69.0               69.0               69.0               69.0               69.0               69.0
 SIC2 industry fixed effects                  No                 No                Yes                Yes                Yes                Yes                Yes
 Time fixed effects                           No                Yes                Yes                Yes                Yes                Yes                Yes
Notes: The dependent variable is an indicator for whether the firm currently uses an AI technology, scaled by 100 for interpretabi lity. The data from the UK Decision
Maker Panel was collected over February-April 2025, November 2025 – January 2026, and May-July (N=5,631). A constant has also been estimated, but not reported in
the table. Where data are missing for a particular variable a dummy variable is included to account for that (results not reported). Standard errors are clustered at
                                                                                                                                                                   78 the firm
level, stars indicate *** p<0.01, ** p<0.05, * p<0.1.
Figure B1 Screenshots of AI survey questions in SBU




                                                      79
Figure B1 Screenshots of AI survey questions in SBU (continued)




                                                              80
Figure B1 Screenshots of AI survey questions in SBU (continued)




                                                              81
Appendix C. Evidence from the Bank of Korea Firm Survey
The Bank of Korea administered the project’s AI survey module online between 15 and 26 June
2026. Given the specific focus of this survey on firms’ use of AI, its results are presented separately
from the broader cross-country estimates. The survey covered 749 firms with 50 or more employees
and was designed to provide broad coverage across major industries and firm-size groups. All five
questions were translated into Korean while preserving the structure, economic concepts, numerical
thresholds and response categories of the common international questionnaire. The results reported
below are weighted by industry using employment shares from the 2024 Korean Census on
Establishments.
AI adoption among Korean firms was widespread (Figure C.1). An estimated 89% of firms currently
used at least one of the AI technologies listed in the survey, while 97% expected to use at least one
over the next three years. Current use was most commonly reported for text generation using large
language models, at 43%, followed by data processing using machine learning at 37% and visual
content creation at 32%. Expected use was higher across nearly all categories, including data
processing using machine learning, which 59% of firms expected to use within three years.
Figure C.1 Current and expected use of AI technologies




Survey respondents also reported substantially more intensive personal use of AI than respondents
in the seven-country sample analyzed in the main text (Figure C.2). Only 3% of Korean respondents
reported no use of AI during a typical working week, while 44% used it for between one and five
hours and 36% for more than five hours. Applying the same numerical values to the response
categories as elsewhere in the paper gives average use of approximately 4.1 hours per week. By
comparison, average use in the main seven-country sample was 2.1 hours, with country-level
estimates ranging from 1.7 to 2.5 hours.




                                                                                                    82
Figure C.2 Average weekly AI use by survey respondent




Korean firms reported little net effect of AI on employment over the past three years, but
considerably more dispersion than in the main sample (Figure C.3). Approximately 60% reported
no realized employment effect, compared with more than 80% across the countries in the main
analysis. The remaining Korean responses were distributed on both sides of zero: 23% reported a
negative effect and 17% a positive effect. Consequently, the implied average employment impact
was close to zero, at approximately −0.1%. Looking ahead, however, 54% of firms expected AI to
reduce employment over the next three years, including 24% expecting a reduction of more than
5%. The implied average expected employment effect was −1.8%.
Figure C.3 Realized and expected AI employment impacts




Reported productivity effects were also substantially larger than those in the main sample (Figure
C.4). Around 43% of Korean firms reported that AI had already increased sales per employee over
the past three years, producing an implied average realized productivity gain of 1.6%. Looking
ahead, 71% expected a positive productivity effect, with one-third expecting an increase of more
than 5%. The implied average expected productivity gain over the next three years was 3.3%. These
estimates compare with average realized and expected productivity effects of approximately 0.4%


                                                                                               83
and 1.7%, respectively, in the main seven-country dataset.
Figure C.4 Realized and expected AI productivity impacts




The Korean results therefore point in the same qualitative direction as the main findings: AI use is
already extensive, realized employment effects are small on average, and firms anticipate larger
productivity and employment effects in the future. Quantitatively, however, Korean firms report
markedly higher personal AI use and larger expected effects. These differences remain similar under
alternative weighting schemes, including employment weighting and a common 12-sector industry
weighting. One potentially important distinction is that, whereas the data in the main analysis were
collected through ongoing economy-wide business surveys covering a broad range of topics, the
Bank of Korea data came from a survey targeted specifically at firms’ use of AI. This difference in
survey context may have attracted firms or respondents with greater interest in or exposure to AI, or
increased the salience of AI when answering the questions, contributing to the larger reported effects.
We therefore present the Korean evidence separately rather than pooling it with the seven-country
estimates. In future work, we plan to investigate the Korean results further, including by comparing
firms’ survey responses with other measures of firm performance, such as realized employment and
productivity growth.




                                                                                                    84
