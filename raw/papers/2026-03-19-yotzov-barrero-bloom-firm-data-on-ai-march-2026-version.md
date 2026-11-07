---
title: "Firm Data on AI (March 2026 version)"
authors: ["Ivan Yotzov", "Jose Maria Barrero", "Nicholas Bloom", "Philip Bunn", "Steven J. Davis", "Kevin M. Foster", "Aaron Jalca", "Brent H. Meyer", "Paul Mizen", "Michael A. Navarrete", "Pawel Smietanka", "Gregory Thwaites", "Ben Zhe Wang"]
publisher: "National Bureau of Economic Research (NBER Working Paper 34836)"
date_published: 2026-03-19
doi: "10.3386/w34836"
url: "https://www.nber.org/papers/w34836"
pdf_url: "https://www.nber.org/system/files/working_papers/w34836/revisions/w34836.rev1.pdf"
attachment: 2026-03-19-yotzov-barrero-bloom-firm-data-on-ai-march-2026-version.pdf
version: "February 2026, Revised March 2026 (second version; superseded on NBER by the October 2026 revision)"
fulltext_source: pdf-converted
converter: pdftotext -layout
notes: |
  Fetched 2026-11-07 from the NBER revisions URL above, as a reference copy for the version that the Stanford
  Digital Economy Lab Adoption Monitor (firm summary updated 10 June 2026) reports. 70-page PDF (created
  2026-03-18, modified 2026-03-19); NBER lists this version as "March 19, 2026". Complete (body, references,
  figures, appendix ending with Figure B6). Printed page = PDF page - 2.
  Key figures: four countries (US, UK, Germany, Australia), "nearly 6,000" executives, fielded Nov 2025-Jan 2026;
  69% of firms use AI (US 78%, UK 71%, Germany 65%, Australia 59%), PDF p. 12. The first version (rev0, dated
  February 2026, NBER date 2026-02-24, https://www.nber.org/system/files/working_papers/w34836/revisions/w34836.rev0.pdf)
  carries the same figures (rev0 PDF p. 12) and was not landed separately.
---

                              NBER WORKING PAPER SERIES



                                     FIRM DATA ON AI

                                         Ivan Yotzov
                                      Jose Maria Barrero
                                       Nicholas Bloom
                                         Philip Bunn
                                        Steven J. Davis
                                       Kevin M. Foster
                                          Aaron Jalca
                                        Brent H. Meyer
                                          Paul Mizen
                                     Michael A. Navarrete
                                       Pawel Smietanka
                                       Gregory Thwaites
                                        Ben Zhe Wang

                                      Working Paper 34836
                              http://www.nber.org/papers/w34836

                    NATIONAL BUREAU OF ECONOMIC RESEARCH
                             1050 Massachusetts Avenue
                                Cambridge, MA 02138
                          February 2026, Revised March 2026



The authors would like to thank the Economic and Social Research Council, Smith Richardson
Foundation and Stanford Impact Labs for funding. Any views expressed are solely those of the
individual authors and so cannot be taken to represent those of the Federal Reserve Bank of
Atlanta, the Federal Reserve System, Bank of England, Bundesbank, or the National Bureau of
Economic Research. Tables can be downloaded from https://bit.ly/3Zrvfs5

At least one co-author has disclosed additional relationships of potential relevance for this
research. Further information is available online at http://www.nber.org/papers/w34836

NBER working papers are circulated for discussion and comment purposes. They have not been
peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies
official NBER publications.

© 2026 Bank of England, circulated with permission. All rights reserved. Short sections of text,
not to exceed two paragraphs, may be quoted without explicit permission provided that full
credit, including © notice, is given to the source.
Firm Data on AI
Ivan Yotzov, Jose Maria Barrero, Nicholas Bloom, Philip Bunn, Steven J. Davis, Kevin M.
Foster, Aaron Jalca, Brent H. Meyer, Paul Mizen, Michael A. Navarrete, Pawel Smietanka,
Gregory Thwaites, and Ben Zhe Wang
NBER Working Paper No. 34836
February 2026, Revised March 2026
JEL No. E0

                                         ABSTRACT

We survey nearly 6,000 senior business executives at US, UK, German, and Australian firms to
develop new evidence on AI adoption and its effects on jobs, productivity, and output.
Specifically, we ask executives about AI usage, its effects at their own firms over the past three
years and, looking ahead, what they anticipate over the next three years. We find four main
results. First, 69% of firms actively use AI, with higher usage rates at younger and more
productive firms. Second, more than two thirds of executives regularly use AI, but their usage
rate averages only 1.5 hours a week. Third, executives report little own-firm impact of AI over
the last 3 years, with nine-in-ten reporting no impact on employment or productivity. Fourth,
these same executives predict sizable effects over the next 3 years, predicting that AI will boost
productivity at their firms by an average of 1.4%, raise output 0.8%, and cut employment 0.7%.
In contrast, employees anticipate that AI will raise employment 0.5% at their firms in the next 3
years, highlighting an expectations gap between employers and employees.

Ivan Yotzov                                            Steven J. Davis
Bank of England                                        Stanford University
Ivan.Yotzov@bankofengland.co.uk                        Hoover Institution
                                                       and NBER
Jose Maria Barrero                                     stevend5@stanford.edu
Instituto Tecnológico Autónomo de
México (ITAM)                                          Kevin M. Foster
Business School                                        Federal Reserve Bank of Atlanta
barsanjmb@gmail.com                                    kevin.foster@atl.frb.org

Nicholas Bloom                                         Aaron Jalca
Stanford University                                    Federal Reserve Bank of Atlanta
Department of Economics                                aaron.jalca@atl.frb.org
and NBER
nbloom@stanford.edu                                    Brent H. Meyer
                                                       Federal Reserve Bank of Atlanta
Philip Bunn                                            brent.meyer@atl.frb.org
Bank of England
Philip.Bunn@bankofengland.co.uk
Paul Mizen
King's College London
Department of Economics
Paul.Mizen@kcl.ac.uk

Michael A. Navarrete
Federal Reserve Bank of Atlanta
mnavarrete.econ@gmail.com

Pawel Smietanka
Deutsche Bundesbank
Research Centre
pawel.smietanka@bundesbank.de

Gregory Thwaites
University of Nottingham
Department of Economics
gregorythwaites@gmail.com

Ben Zhe Wang
Macquarie University
ben.wang@mq.edu.au
1. Introduction
How widespread is the adoption of artificial intelligence (AI) technologies in commercial
enterprises? How have these technologies affected productivity, employment, and output in a
broad cross section of firms? And how will AI affect productivity, employment, and output in
the next few years?

To address these questions, we exploit new data based on surveys of our own design. Our
samples cover senior business executives at nearly 6,000 firms in the United States, United
Kingdom, Germany, and Australia. To elicit high response rates from executives, we
collaborate with central banks in their respective countries. To facilitate comparisons across
countries, we put the same questions to executives in each country. To compare the perceptions
and expectations of executives with those of workers, we also put the same questions to
employees in the United States. Our survey collections offer insights into the workplace
diffusion of AI technologies and their effects.

News coverage of AI and the economy has exploded since 2022 (Figure 1). This pattern reflects
a tremendous surge of interest in the economic and social ramifications of AI. Previous research
draws on data derived from surveys, job postings, and other sources to estimate AI adoption
rates. These estimates differ by more than a factor of ten across recent studies, underscoring
the importance of measurement challenges related to sample size, representativeness, question
design, and respondent incentives. Few sources capture the views of senior business executives,
who have the best line of sight on how AI will affect their own firms in the next few years.

Forecasting the consequences of new AI technologies is a deeply challenging prediction
problem. First, AI-related developments are unfolding in a highly non-stationary setting.
Extrapolations from the recent past, even sophisticated ones, are prone to major errors. Second,
some observers think AI technologies are unprecedented in the extent to which they will drive
rapid transformations in how we work, produce, and live. That view argues for caution in
forming predictions grounded mainly in historical analogies. A similar point holds for
predictions grounded in theoretical models that lack compelling foundations in suitable data.
Third, no one — including technologists, AI firms, and professional forecasters — possesses
the information and expertise needed to independently predict how AI technologies and their
effects will play out in all corners of the economy. The relevant information and expertise are
highly dispersed. Fourth, and more constructively, some people have useful information and
expertise on how AI adoption and its effects are likely to play out in their own corners of the

                                                  2
economy. In particular, senior business executives are likely to have informed views about
their own firms.

Our prediction strategy exploits this last observation. Specifically, we ask senior business
executives about AI usage and its effects at their own firms over the past three years and,
looking ahead, what they anticipate over the next three years. We then aggregate their
responses. Working with teams at the Federal Reserve Bank of Atlanta, Bank of England,
Deutsche Bundesbank, and Macquarie University, we fielded parallel survey questions to broad
samples of senior executives between November 2025 and January 2026. Our aim is to collect
high-quality, representative data on AI usage and to understand its (future) effects.

Our survey data collection efforts yield four main results.

First, AI technologies are already in wide use. On average across our four countries, 69% of
businesses currently use AI. The most common uses are ‘text generation using large language
models,’ followed by ‘visual content creation’ and ‘data processing using machine learning.’
Larger, more productive, and higher-paying firms are more likely to deploy AI technologies.
Older firms and those with older directors have lower usage rates. Looking ahead, 75% of
executives expect their firms to use some forms of AI in the next three years.

Second, over two-thirds of survey respondents (mostly CEOs, CFOs, and senior finance
managers) themselves use AI technologies in a typical work week, with an average usage of
1.5 hours per week. Usage rates have risen since early 2025 and are higher at better-paying
firms and those with younger directors. CEOs are more likely to use AI than CFOs and other
senior executives.

Third, most executives report small effects thus far on own-firm employment and productivity.
More than 90% report no impact of AI on own-firm employment over the past three years, and
89% report no impact on labor productivity (sales per employee). A small percentage of
executives report positive productivity effects to date.

Fourth, executives anticipate much larger future effects on their businesses. They expect AI
technologies to raise productivity by 1.4%, on average, over the next three years. If correct,
this prediction implies a sizable improvement relative to a long period of weak productivity
growth in many advanced economies (Bloom et al. 2020, and Goldin et al. 2024). Executives
at larger and higher-paying firms anticipate greater productivity gains from AI, as do those in
the information, communications and administrative support sectors. US business executives

                                                3
foresee a stronger AI productivity boost – 2.25% over the next three years – than executives in
other countries we cover.

At the same time, executives expect AI to reduce own-firm employment by 0.7%, on average,
over the next three years. That’s equivalent to about 1.75 million fewer jobs by 2028 across
our four countries. Large-firm executives anticipate greater negative effects on employment,
as do those in accommodation, food services, wholesale, and retail sectors. Of course, AI
technologies can also raise employment at new firms, and firms yet to open, which are outside
the scope of our sample frames. 1 Moreover, we don’t ask executives to forecast the equilibrium
employment effects of the higher real incomes that productivity gains generate in the form of
greater profits, higher real wages, or lower prices and better products. Our survey-based
employment predictions should be understood in this light.

Related Literature: Our paper contributes to four literatures on AI technologies and their
effects.

First, we build on studies that measure AI adoption. Earlier works yield a wide range of
estimates, likely owing to differences in survey timing, question wording, sample mix, and
respondent characteristics and incentives. Drawing on the 2019 US Annual Business Survey,
Acemoglu et al. (2022) and McElheran et al. (2024) estimate that 3% of firms and 13% of
workers use AI. Drawing on the US Business Trends and Outlook Survey (BTOS), Bonney et
al. (2024) estimate that 5% of businesses (9% employment-weighted) use AI as of February
2024.2 McKinsey (2025) estimates that 88% of organizations use AI in at least one business
function as of 2025. Estimated AI adoption rates for the UK also vary widely. According to the
Management and Expectations Survey, 9% of firms use AI as of 2023 (ONS 2025). An Institute
of Directors survey (2025) finds that 49% of businesses use AI as of 2025, while an LSE-CBI
survey finds that 25% of firms made specific investments in AI technologies by 2024 (Oliveira-
Cunha 2024).

We ask business executives about AI usage and its effects at their own firms, a topic on which
they have incentives to be well informed. We also lean on long-standing relationships between


1
  Since 2021, U.S. business formation rates – and derived projections of new employer businesses – have greatly
outpaced their pre-pandemic counterparts. See, for example, the U.S. Census Bureau series on projected new
employer business at https://fred.stlouisfed.org/series/BFPBF4QTOTALSAUS. This measure of new employer
business has risen further since early 2025.
2
  As of December 2025, adoption rates in the BTOS have risen to 18% of businesses and are expected to rise to
21% over the ensuing six months. See https://www.census.gov/hfp/btos/data

                                                      4
central banks and business executives, and the desire of executives to maintain them. These
features of our approach help us enlist a representative sample of senior business executives
who are well positioned to supply informed responses to our survey questions.

We also contribute to a second literature that measures AI take-up rates across individuals.
Bick et al. (2024), Hartley et al. (2025), Barrero et al. (2025), Sidoti and McClain (2025) and
Bloom and Makridis (2026) all estimate individual AI usage rates at around 50%. Roughly half
of this usage is work-related, and half is for other purposes.

A third literature considers the realized and expected impact of AI technologies on businesses
and the economy. Some studies find large productivity gains from AI in specific settings.
Brynjolfsson et al. (2025a) find that generative AI yields large gains among customer-support
agents at a large software firm. del Rio-Chanona et al. (2025) review several studies that report
large gains from generative AI in various settings. Noy and Zhang (2023) conduct an RCT and
find that access to ChatGPT boosts productivity in writing assignments.3 Babina et al. (2024a)
link AI investment to product innovation and greater firm value, and Eisfeldt et al.
(forthcoming) find a 5% relative value gain at firms with highly AI-exposed workforces in the
two weeks after ChatGPT’s release. Babina et al. (2024b) develop evidence that AI investments
expand firm-level growth options.

Despite large gains associated with AI in specific tasks and certain firms, the implications for
economy-wide productivity are unclear. Adopting a task-based model and applying Hulten’s
Theorem, Acemoglu (2025) estimates that AI technologies will boost US total factor
productivity by at most 0.66% over the next ten years. In sharp contrast, Briggs and Kodnani
(2023) estimate that generative AI alone can boost US labor productivity by 1.5 percentage
points per year over ten years. Misch et al. (2025), adopting the framework of Acemoglu
(2025), estimate that AI will boost TFP in Europe by around 1.1% over five years.

Finally, we contribute to a literature on the labor market implications of AI. Survey evidence
points to modest AI effects to date on overall employment (e.g., Abel et al. 2024, Cañas and
Kerr 2024), with larger effects in certain occupations and age groups. Using ADP payroll data,
Brynjolfsson et al. (2025b) estimate that generative AI has reduced the relative employment of
young Americans (ages 22-25) by 16% in the most AI-exposed occupations, conditional on



3
 Other research finds productivity gains from AI in legal analysis (Choi and Schwarcz 2025), consulting work
(Dell’Acqua et al. 2023), and programming (Peng et al. 2023 and Cui et al. 2025)

                                                      5
firm-level shocks. Teutloff et al. (2025) develop evidence that ChatGPT shifted the structure
of demand for freelance work, lowering the demand for writing and translation tasks by 20-
50% while raising the demand for machine learning programming by 24%. Humlum and
Vestergaard (2025) estimate near-zero effects of AI-powered chatbots on earnings and
employment at the level of workers and workplaces in Denmark as of 2024.

The next section describes our main data sources. Section 3 validates our data, showing a tight
relationship between our survey-based measures and national aggregates. Section 4 presents
our results on firm-level AI adoption, AI usage rates by business executives, backward-looking
assessments of AI effects on firm-level outcomes, and executive forecasts of how AI
technologies will affect outcomes at their firms in the next three years. Section 5 presents
perceptions and forecasts based on surveys of employees. Section 6 concludes.


2. Our Surveys of Business Executives
We now provide an overview of our surveys of business executives in the United States, United
Kingdom, Germany, and Australia. Section 5 covers our employee survey.

The US Survey of Business Uncertainty (SBU)

The Survey of Business Uncertainty (SBU), fielded by the Federal Reserve Bank of Atlanta, is
a monthly online panel survey of senior executives at US firms. 4 The SBU aims to cover a
broadly representative sample of firms across US regions, industries, and size categories.
Potential survey participants are initially identified using proprietary and public sources of
information, then recruited by telephone to confirm their position and company, and finally
moved into the survey panel. Sponsorship by the Atlanta Fed greatly facilitates the recruitment
of senior executives. Figure 2, Panel A shows that 70% of respondents are CEOs, CFOs or
other senior managers, while Figure A1 shows the close match of SBU coverage to all US firms
and across industries and Census geographic divisions.

First established in 2014, the SBU yields about 1,000 survey responses per month as of 2026.
Core survey modules ask each executive about current, past, and future own-firm employment
and sales revenue growth. Forward-looking questions elicit subjective probability distributions
for these outcomes over the next year. Thus, SBU respondents are accustomed to providing
complex forecasts in their survey responses. See Altig et al. (2022) for details and an extended

4
    https://www.atlantafed.org/research/surveys/business-uncertainty

                                                         6
analysis of forecast characteristics and performance.

In addition to the core modules, each monthly edition of the SBU includes special questions
on a topic of interest. The November 2025 edition contains several questions on AI adoption
and usage intensity, the effects of AI on own-firm employment and productivity in the past
three years, and expected own-firm effects of AI over the next three years. Figure B1 presents
screenshots of these questions.

SBU respondents do not receive any monetary or in-kind compensation for joining the panel
or completing the surveys. They are motivated to participate to share their views, maintain their
relationships with the Federal Reserve System, receive information about the survey results,
and perhaps out of a sense of civic responsibility. We view these motivations as a design
feature. A challenge with paid online surveys of targeted populations, like senior executives,
is that they can generate high impostor shares – as high as 80% according to Chandler and
Paolacci (2017). See, also, Bell and Gift (2021). In contrast, the SBU is unpaid and respondent
identities are verified by Atlanta Fed staff.

The UK Decision Maker Panel (DMP)

The Decision Maker Panel (DMP) is a monthly online panel survey of UK business
executives.5 It is an economy-wide survey and matches the industry composition of the UK
economy (Appendix Figure A2). Launched in 2016, the Bank of England runs the DMP. Since
2022, the DMP yields about 2,500 survey responses per month. Like the SBU, interviewees
are unpaid and are initially recruited by telephone to confirm their position and company, and
then moved into the survey panel. 6 Sponsorship by the Bank of England greatly facilitates the
recruitment of senior executives. Over 90% of respondents are either CFOs, CEOs, or in other
senior management positions (Figure 2, Panel B).

Each month the DMP asks senior executives about the evolution of sales, prices, employment,
wages, and capital expenditures at their firm over the past year and expectations for the year
ahead. In addition to these standard questions, the DMP regularly includes special questions
on topical issues. For further information, see Bunn et al. (2024) who provide a detailed
overview of the survey, including the structure, quality checks against other datasets, and


5
 https://decisionmakerpanel.co.uk/
6
 A team at the University of Nottingham in the UK contacts businesses by phone to invite them to join the
panel (Figure B6).

                                                      7
information on how to access the data.

Several DMP editions from February 2025 to January 2026 include questions about the
adoption of AI technologies and the impact of AI on their employment and sales per employee
(a proxy for productivity). In addition, survey respondents were asked how frequently they
personally use AI technologies during the work week (Figure B2).

We match DMP data with firm-level financials in the Bureau van Dijk (BvD) database, which
contains basic accounts and directors data for UK companies. 7 BvD is based on the population
of UK firms in Companies House.

The Bundesbank Online Panel of German Firms (BOP-F)

The Bundesbank Online Panel – Firms (BOP-F) is an online survey of a representative panel
of firms in Germany. Operated by the Deutsche Bundesbank, Germany’s central bank, the
survey began in June 2020. Since July 2021, the BOP-F yields 8,000 to 9,000 survey responses
per quarter from the CEOs and CFOs of registered German companies.

The BOP-F sample is drawn from the Business Register, with the sponsorship of the
Bundesbank supporting the recruitment of senior executives. Firms from nearly all economic
sectors with more than 12,500 EUR annual turnover or at least one employee and a firm address
are eligible for inclusion in the sample. See Boddin et al. (2024) for more information about
how the sample is drawn.

While the survey operates at a quarterly frequency for any given firm, new responses are
collected every month. This is because the survey design follows a rotating panel principle,
whereby one third of all new firms in the sample are randomly selected into group A, B, or C,
with one group surveyed each month.

The January 2026 BOP-F includes questions on the adoption of AI technologies, AI effects on
employment and productivity, and average weekly AI usage by survey respondents. These
questions follow analogous SBU and DMP questions (Figure B3), yielding responses from
about 2,500 firms.




7
 Figure A3 shows a very strong relationship between survey data in the DMP on employment and sales to
matched annual company accounts data from BvD, an initial indicator of survey response quality.

                                                    8
The Australian Business Outlook Scenarios Survey (BOSS)

The Business Outlook Scenarios Survey (BOSS) is a monthly online survey of Australian
business executives. 8 The BOSS targets senior financial decision makers at a representative
sample of Australian firms, covering all locations and industries. CFOs, CEOs, and other senior
managers account for 87% of BOSS respondents. The BOSS was established in 2024 by
Macquarie University. The BOSS obtains more than 500 responses per month. Questions
pertain to one-year-ahead expectations of key macroeconomic variables such as inflation and
interest rate and own-firm sales growth, prices, employment, wages and operating cost. BOSS
procedures include various data checks to guard against response falsification.

The BOSS survey edition fielded from December 1 to 8 in 2025 included questions on AI
adoption, realized and expected AI effects on productivity and employment, and personal AI
usage by the respondents. See Figure B4. Executives from 602 firms participated in the
December 2025 edition of the BOSS.


3. Data Validation
To validate the quality of our firm survey panels before showing our AI data we run two
exercises.

First, in Figure 3 we show how 10 years of data on output and employment from our firm
panels compare against aggregate data for the US SBU and UK DMP surveys. Output data
from the US survey tracks US GDP growth (top-left) and private employment (top-right), as
do UK data when compared to UK GDP growth (bottom-left) and private sector employment
(bottom-right). Hence, our surveys are accurate and representative of macro aggregates over
the past decade. Their performance is similar across the pre-pandemic period, the COVID
recession and recovery, and post-pandemic stabilization. Hence, we are confident that, due to
our large representative sample of senior executives, our data reflect aggregate trends across
the business cycle.

Second, we show the performance of the sales and employment forecasting questions included
in our surveys on a quarterly basis. Once a quarter, executives are asked to forecast their year-
ahead (12 months ahead) sales growth and employment growth. One year later we compare


8
 https://www.mq.edu.au/macquarie-business-school/our-departments/
department-of-economics/our-research/business-outlook-scenarios-survey-boss

                                                    9
these forecasts to actual realizations of sales and employment growth for these firms. This
enables a large sample evaluation of our survey respondents’ forecast accuracy. As we see in
Figure 4, our responding executives make accurate forecasts, with sales and employment
predictions lining up tightly with realizations occurring over the next year. This positive
relationship suggests that our panel is well-equipped to predict the future business conditions
for their firms, increasing our confidence in the accuracy of their forecasts of the impact of AI.


4. Main Results
Having established the broad representative nature of our four national firm surveys, and their
strong track record in matching aggregate output and employment data and forecasting future
growth, we now turn to their responses and predictions regarding AI. We present the overall
results which combine firm-level results from each country into one figure, and also provide
country-level values. Tables can also be downloaded from https://bit.ly/3Zrvfs5

4.1 Current and expected use of AI technologies

We begin by analyzing the current use of AI technologies by businesses. In all four surveys,
firms are asked to select which of the following they are currently using, if any: data processing
using machine learning; visual content creation; text generation using large language models;
image processing using machine learning; robotics; autonomous vehicles; or other. Firms could
select more than one technology.

Figure 5 presents the main results. The black bars in the figure correspond to the average across
firms in all four surveys, weighted by the sample sizes of the respective surveys. Across all
four countries, we find that a majority of businesses are currently using some AI technology.
Adoption is highest in the US (78% of firms), followed by the UK (71%), Germany (65%), and
Australia (59%). On average, 69% of all firms are currently using AI.

The figure also shows that adoption is not concentrated in a single use case. The most popular
current use is ‘text generation using LLMs’ (by 41% of firms on average), but around 30% of
firms also report using data processing using machine learning and visual content creation.
Less commonly cited uses were image processing using machine learning (20%), robotics (9%
of firms), and autonomous vehicles (3%), which are likely more specific to certain industries.

Adoption of AI technologies has increased since the start of 2025. Figure A4 compares the
results on current AI adoption from the UK DMP between February-April 2025 and November


                                               10
2025 to January 2026.9 We find that the use of all technologies has increased. On average, the
percentage of businesses using at least one AI technology increased from 61% in February-
April 2025 to 71% in November 2025-January 2026. This emphasizes the importance of having
consistency in the timing of the questions across data sources during a time when adoption is
increasing rapidly across businesses.

We next study the characteristics of firms which predict the current use of AI technologies. In
Figure 6, we present a series of binned scatter plots of the relationships between current use of
AI (on the vertical axes) and a series of firm characteristics. This figure uses data from the
DMP survey, due to the larger sample size and the availability of more firm covariates. 10 We
find that more productive (Panel A), larger (Panel B), and higher-paying firms (Panel C) are
more likely to be using AI. 11 In contrast, in Panels D and E, we show that firms with older
directors on average, and older firms are less likely to be currently using AI. Use of AI
technologies also varies by sector. In Figure A6 Panel A, we show that current AI adoption by
UK firms is highest in the finance and insurance and professional and scientific sectors.

In Table 1, we test the robustness of these relationships in a regression table where we combine
all the variables in a single specification and also control for industry and time fixed effects.
The dependent variable across all columns is a dummy for whether a firm uses any AI
technology, scaled by 100 for interpretability. In addition to all the univariate relationships
(Columns 1-11), in Columns 12 and 13 we find that the most robust predictors of AI use from
Figure 6 are labor productivity, firm employment, average wage per employee, and the average
age of directors.12 We also find that firms with higher average productivity growth in 2025 are
more likely to be using some AI technology. 13

Finally, we consider how firms expect adoption of AI technologies to change over the next


9
  These national AI surveys will be run twice yearly from 2026 onwards to track the evolution of AI. However,
the only survey prior to the current wave was run by the UK.
10
   In Figure A5, we show similar results for a subset of variables from the US SBU. More productive (Panel A)
and larger (Panel B) firms are more likely to be using an AI technology in US firms as well.
11
   Labor productivity is constructed using firm-level accounts data from BvD as the real gross value-added per
employee. The data from the latest accounts available for each firm are used in the figure. The average wage per
employee (Panel C) is constructed as the total wage bill per employee, again using accounts data.
12
   We do not include a regression of productivity growth, real sales growth, and employment growth in the same
specification because productivity growth is defined in our analysis as real sales growth – employment growth.
Running these three variables in the same specification would result in collinearity. Therefore, we split the
results into Columns 12 and 13.
13
   As further robustness, in Table A1 we use as a dependent variable the number of AI technologies currently
used instead of a dummy for whether any AI technology is used. The results are consistent across the two
specifications.

                                                      11
three years. Figure A7 shows that AI adoption is expected to increase on average. Across all
four countries, 75% of firms expect to be using some AI technology over the next three years.
Furthermore, we find that the most common technology firms expect to use is data processing
using machine learning, suggesting firms are expecting to build capacity to use AI tools for
data processing, even if they are not currently used as extensively. 14

Overall, this section highlights that AI use is widespread across businesses in the US, UK,
Germany, and Australia. Larger and more productive firms are more likely to be using AI
technologies, as are higher-paying businesses. AI adoption has increased since the start of 2025
and is expected to increase over the coming years. One limitation of this analysis is that it only
refers to the extensive margin of adoption, but not about how intensively firms are using these
technologies or the impact on their businesses. In Sections 4.3 and 4.4, we present new
evidence on how firms estimate that AI has been impacting their employment and productivity,
and how they expect these effects to change in the next three years.

4.2 Use of AI by survey respondents

In this section, we analyze how frequently the respondents themselves use AI during a typical
work week. As these respondents typically hold senior positions in their firms (e.g. CEOs,
CFOs, senior finance managers), these results are another useful proxy for AI adoption more
broadly since they are in a position to instruct their subordinates to make use of AI as they see
the opportunity. They are also less likely to be subject to measurement error, as the respondents
are reporting about their personal use, rather than for the business as a whole. The survey asks
whether they personally use AI technologies: “Not at all”; “Up to 1 hour a week”; “1 to 5 hours
a week”; or “More than 5 hours a week”.

Figure 7 Panel A presents the distribution of responses across these categories for US, UK,
German and Australian respondents. Across all firms, only 28% of respondents do not use AI
at all during the working week. The modal response is up to 1 hour a week (41%), but more
intensive AI use is not uncommon. 24% of respondents report 1-5 hours of AI use per week,
and 7% report using AI more than five hours in a typical working week. In Panel B, we assign
quantitative values to each of the categories to estimate the average number of hours of AI use.
Across all firms, our respondents use AI around 1.5 hours per week on average. These results



14
  AI adoption is also expected to increase across almost all industries over the next 3 years (Figure A6, Panel
B)

                                                       12
are similar across all four countries, ranging from 1.7 hours in the US to 1.4 hours in the UK
and Germany, and 1.5 hours in Australia.

We next consider how AI use varies with firm-level and respondent characteristics. Figure A8.a
presents binned scatterplots with the average weekly AI use on the vertical axis for UK firms.
We find that respondents in younger firms use AI technologies more often during the working
week (Panel A), as do respondents in firms where the average age of directors is lower (Panel
B). These relationships are similar to Figure 6, Panels D and E, where the firm age and average
age of directors are shown to be negatively correlated with current AI adoption across the
business.15 Figure A8.b shows that a similar negative relationship is present between firm age
and average weekly AI use in US firms as well. In Figure A9 we split the frequency of AI use
by the position of the respondent in the business. Specifically, we distinguish between CEOs,
CFOs, and other senior executives. In both the US (Panel A) and UK (Panel B), we find that
AI is more frequently used by CEOs than other respondents. Finally, in Figure A10 we analyze
how the frequency of AI use has changed since the start of 2025. This figure is based on
responses to the DMP survey. We find that AI use has increased sharply since the start of 2025.
The percentage of respondents who did not use AI at all dropped from 45% to 25%, and the
frequency in each of the other categories increased. On average, AI use by senior executives
increased by around 50%, from 0.9 hours a week to 1.4 hours a week in less than a year.

4.3 Impact of AI on firm employment

In this section we present results on the impact of AI technologies on firm realized and expected
employment. Firms are asked to estimate these impacts using five categories, ranging from a
large positive impact (increasing employment by more than 5%) to a large negative impact
(decreasing employment by more than 5%). Figure 8 presents the main results over the past
three years. In Panel A, we show the distribution of responses across the five categories. Across
the four surveys, more than 90% of firms on average estimate no impact over the last three
years. This percentage is highest in Germany (95% of firms), followed by the US (89% of
firms), UK (89%), and Australia (81%). Among the remaining firms which report some impact,
the results are skewed slightly to the negative side in the UK and US, and slightly to the positive



15
  In Table A2 we analyze the determinants of weekly AI use with univariate and multivariate regressions,
following the structure presented in the remaining regression tables of the paper. In the most demanding
specifications with sector and time fixed effects (Columns 12-13), we find that the average age of directors
remains the most significant predictor of average weekly AI use.

                                                       13
in Germany and Australia.

To estimate an average quantitative impact of AI on employment, we assign numerical values
to each of the five categories in Panel A. We assign values ±7.5% to large positive/negative
impacts; ±2.5% to small positive/negative impacts; and 0% to no impact. In Figure 8, Panel
B we present these average impacts. Across all firms, the impact of AI is essentially zero over
the past three years. However, there is some heterogeneity across the four countries. In the UK,
firms estimate that AI has lowered employment by around 0.14% over the last 3 years. In the
US, there is also a small negative average impact at -0.09%. In contrast, in Germany firms
estimate that AI has increased employment by 0.07%, and in Australia firms estimate a positive
AI employment impact of around 0.32% over the past 3 years.

There is substantial sectoral heterogeneity in the realized employment impacts of AI. Figure
A11, Panel A shows the average realized employment impacts from AI across industries in the
UK. The impacts vary from positive in the Construction sector (+0.1%) to negative in the
Accommodation and Food (-0.4%) and Transport and Storage (-0.4%).

In Figure 9, we present results on how firms expect AI to impact their employment over the
next three years. The distribution of responses in Panel A looks markedly different from the
realized employment impacts in Figure 8. In Figure 9 Panel A, 63% of all firms expect no
impact over the next three years, with the distribution of responses being skewed much more
to the negative side. 18% of all firms expect a small negative impact, lowering employment by
less than 5%, and 8% expect a large negative impact on employment, greater than 5%. These
results are similar across the US and UK. German firms record an expectation of a smaller
change (positive or negative) compared to US and UK firms, which may reflect characteristics
of the German labor market, but with a higher negative impact expected than a positive impact.
In contrast, Australian firms remain more evenly balanced on the expected employment
impacts of AI – 16% expect a negative impact and 16% expect a positive impact overall. Panel
B of Figure 9 presents the corresponding quantitative estimate on the expected employment
impacts of AI. Over the next three years, firms across the four countries expect AI to lower
employment by around 0.7%. The largest effects are in the UK (-1.4%), followed by the US (-
1.2%). German and Australian firms do not expect AI to have as large an effect on overall
employment over the next three years, possibly due to more regulated labor markets.

To gauge how lower employment may be achieved, a sub-sample of UK firms were asked a
follow up question about the expected importance of hiring fewer new employees versus

                                              14
increased exits of existing employees. 16 Around two-thirds of the reduction in employment is
expected to come from firms hiring fewer new employees.

There remains heterogeneity across sectors in the expected employment impacts, as we show
in Figure A11, Panel B. The expected impacts over the next three years are negative across all
sectors of the economy for firms in the UK. The largest negative impacts are in the
Accommodation and Food (-1.8%) and Wholesale and Retail (-2%) sectors.17

Beyond the sectoral differences, we also consider how the expected employment impacts vary
with various firm-level characteristics. Table 2 presents the determinants of expected AI
employment impacts using univariate and multivariate regressions for UK firms. We use the
same set of variables here as those in Table 1 where we analyzed the determinants of current
AI adoption. To maximize the sample size, the regressions use the latest firm observation on
the expected employment impact using data collected over February-April 2025 and November
2025-January 2026. Focusing on Columns 12-13 which include all the variables as well as
industry and time fixed effects, we find that larger firms expect more negative impacts of AI
on employment. In contrast, higher realized employment growth in 2025 and higher expected
employment growth in 2025 are both associated with less negative AI employment impacts.

4.4 Impact of AI on firm productivity

In this section we present results on the impact of AI technologies on firms’ realized and
expected productivity. The survey questions follow the same structure as the employment
impacts. Productivity in this analysis is defined as the volume of sales per employee. Figure 10
presents the main results on realized productivity impacts over the past three years. In Panel A,
we show the distribution of responses across the five categories. Across the four surveys, 89%
of firms on average estimate no impact over the last three years. This percentage is highest in
the US and Germany (91% of firms), followed by the UK (89%), and Australia (79%). Among
the remaining firms which report some impact, the results are skewed to the positive across all
four countries, indicating some positive impacts in the aggregate.

To estimate an average quantitative impact of AI on productivity, we assign numerical values

16
   This question was included for half of the firms in the DMP survey in January 2026 (one-sixth of the total UK
sample), and was only asked to firms who expected AI to lower their employment over the next three years.
17
   The expected impacts of AI on employment have also become more negative since the questions were asked
in the beginning of 2025 in the DMP survey. Over February-April, the expected impact on employment was -
0.8% over the next three years, compared to the -1.4% expected impact for the same questions over November
2025-January 2026.

                                                      15
to each of the five categories in Panel A. As with the employment impact, we assign values
±7.5% to large positive/negative impacts; ±2.5% to small positive/negative impacts; and 0%
to no impact. In Figure 10, Panel B we present these average impacts. Across all firms, AI is
reported to have boosted productivity by around 0.29% over the past three years. The effects
are very similar across the US, UK, and Germany, ranging from 0.24% to 0.29%. In contrast,
in Australia firms estimate a larger positive AI productivity impact so far, at around 0.49%
over the past 3 years. Figure A12, Panel A shows a breakdown of the realized AI productivity
impacts by industry. These are positive across all industries in the UK. Firms in the Information
and Communications and Professional and Scientific sectors report the largest positive
productivity impacts from AI so far, at +0.8% and +0.5%, respectively.

In Figure 11, we present results on how firms expect AI to impact their productivity over the
next three years. The distribution of responses in Panel A looks markedly different from the
realized productivity impacts in Figure 10. 60% of all firms expect no impact over the next
three years, with the distribution of responses being clearly skewed to the positive. 25% of all
firms expect a small positive impact, increasing productivity by less than 5%, and 12% expect
a large positive impact on productivity, greater than 5%. These results are similar across UK,
US, German and Australian firms. Panel B of Figure 11 presents the corresponding quantitative
estimates on the expected productivity impacts of AI. Over the next three years, firms across
the four countries expect AI to increase productivity by an average of around 1.4%. The largest
effects are in the US (+2.3%), followed by the UK (+1.9%), Australia (+0.9%), and Germany
(+0.9%).

The productivity boost from AI is not expected to be equally distributed across sectors of the
economy, as we show in Figure A12, Panel B. The largest impacts are in the information and
communications and administrative and support sectors, which expect AI to increase
productivity by 2.8% and 2.5% over the next three years, respectively. 18 Much smaller impacts
are expected by firms in Accommodation and Food, Construction, and Recreational Services.

As with the expected employment impacts, we also consider how the expected productivity
impacts vary with various firm-level characteristics. Table 3 presents the determinants of
expected AI productivity impacts using univariate and multivariate regressions for UK firms.
We use the same set of variables here as those in Tables 1 and 2 for comparability. As was the


18
  Between February-April 2025 and November 2025-January 2026, the expected productivity impacts of AI
over the next three years increased from +1.5% to +1.9%

                                                   16
case for employment, the regressions use the latest firm observation on the expected
productivity impact using data collected over February-April 2025 and November 2025-
January 2026, which is again 2,793 unique firm observations. Focusing on Columns 12-13
which include all the variables as well as industry and time fixed effects, we find that larger
firms, higher-paying firms, and those with higher expected employment growth have more
positive expected impacts of AI on productivity.

Overall, the last two sections show that the adoption of AI technologies has had little impact
on firm employment and only a small positive impact on firm productivity so far. However,
firms anticipate large impacts over the next few years. On average, businesses expect AI to
boost productivity by around 1.4% over the next three years, while lowering employment by
around 0.7% over the same period. This also implies an increase in output of around 0.8%.


5. Estimated AI impacts by employees

So far, the evidence presented in Section 4 has focused on executives responding on behalf of
their businesses. Are the perceived and expected impacts of AI similar across business
executives and employees? To answer this, we asked the identical questions to employees using
the Survey of Working Arrangements and Attitudes (SWAA).19 The SWAA is a monthly
survey of between 2,500 and 10,000 US residents aged between 20 and 64. Specifically, we
asked about the impact of AI on employment and productivity in their current firms over the
last three years and looking ahead in the next three years. We also asked employees how
frequently they used generative AI in their jobs. These questions were added in the December
2025 SWAA wave. Figure B5 shows screenshots of the questions in the SWAA. Around 3,000
people answered.

We present the main results in Figure 12. In Panel A, we see employees report using AI for
about the same amount of time as executives do, averaging around 1.8 hours a week. 20 In Panel
B we see employees are more optimistic over the last 3 years on the impact of AI on
productivity and employment, suggesting this has had a moderately positive impact on both.
Strikingly, in Panel C we see employees are far more optimistic than executives on the impact
of AI on future employment, while less optimistic about the positive productivity impacts. In

19
  https://wfhresearch.com/data/
20
  The identical question on average AI use was asked in a survey of approximately 2,000 UK employees in
December 2025. On average, UK employees reported using AI for about two hours per week, similar to US
employees.

                                                    17
particular, employees predict that AI will increase employment by approximately 0.5% in their
firms over the next three years compared to the prediction from executives that it will reduce
employment by 0.7% in all firms and 1.2% in US firms. Hence, there appears to be a large gap
in the perceptions on the impact of AI, from a view by employees that AI will create jobs versus
a view from executives that it will reduce jobs. Likewise, employees expect AI to increase
productivity by around 0.9% over the next three years, compared to an expected increase of
1.4% across all firms and 2.3% by US firm executives in particular.


6. Concluding Remarks
Our study presents new evidence on how firms are using AI technologies, as well as their
realized and expected effects on employment and productivity. We use survey evidence from
four large, economy-wide business surveys – the US Survey of Business Uncertainty, the UK
Decision Maker Panel, the German Bundesbank Online Panel - Firms, and the Australian
Business Outlook Scenarios Survey – using identical questions asked between November 2025
and January 2026. We began asking AI-related questions in the UK Decision Maker Panel in
February 2025, allowing for some evidence on AI developments over time.

We obtain four chief findings. First, AI technologies are currently used by around 70% of
businesses, and adoption is expected to increase. Larger, more productive, and higher-paying
firms are more likely to be using some AI technology. Second, we show that AI technologies
are being actively used by senior survey respondents (typically CEOs, CFOs, and senior
finance managers). On average, respondents use AI for around 1.5 hours in a typical working
week, and this frequency has increased sharply since the start of 2025. Third, firms estimate
that AI has had little impact on their employment so far, and only a modest boost to productivity
over the past three years. Finally, firms expect AI to have larger impacts over the medium-
term. Over the next three years, firms predict that the adoption of AI will boost productivity by
around 1.4%, on average, while reducing employment by around 0.7%. This is in sharp contrast
to expectations of employees, who expected higher job creation as a result of AI, along with
smaller productivity gains over the next three years. Overall, our approach can be used to
monitor the adoption and impacts of AI over time and across multiple countries. We
furthermore emphasize the importance of consistency in survey design and timing for obtaining
comparable, high-quality results across countries.




                                               18
References
Abel, J R, R Deitz, N Emanuel and B Hyman (2024), “AI and the labor market: Will firms
hire, fire, or retrain?”, Liberty Street Economics, 4 September.
Acemoglu, D (2025), “The simple macroeconomics of AI”, Economic Policy 40(121): 13-58.

Acemoglu, D, D Autor, J Hazell and P Restrepo (2022a), “Artificial Intelligence and Jobs:
Evidence from Online Vacancies”, Journal of Labor Economics 40(S1).
Acemoglu, D, G W Anderson, D N Beede, C Buffington, E E Childress, E Dinlersoz, L S
Foster, N Goldschlag, J C Haltiwanger, Z Kroff, P Restrepo and N Zolas (2022b),
“Automation and the workforce: A Firm-level view from the 2019 Annual Business Survey”,
NBER Working Paper 30659.
Altig, D, J M Barrero, N Bloom, S J Davis, B H Meyer, and N Parker (2022), “Surveying
Business Uncertainty”, Journal of Econometrics 231(1): 282-303.
Baker, S, N Bloom and S Davis (2016), “Measuring economic policy uncertainty”, The
Quarterly Journal of Economics 131: 1593–1636.
Babina, T, A Fedyk, A He and J Hodson (2024a), “Artificial intelligence, firm growth, and
product innovation”, Journal of Financial Economics 151: 103745.
Babina, T, A Fedyk, A He and J Hodson (2024b), “Artificial Intelligence and Firms'
Systematic Risk”, Working Paper.
Barrero, J, N Bloom and S Davis (2025), “Why working from home will stick”, Stanford
working paper.
Bell, Andrew M. and Gift, Thomas, (2023), “Fraud in Online Surveys: Evidence from a
Nonprobability, Subpopulation Sample” Journal of Experimental Political Science, Vol.
10(1), Spring 2023, 148-153,
Bick, A, A Blanden and D Demming (2024), “The Rapid Adoption of Generative AI”, NBER
Working Paper 32966.
Bloom, N, C I Jones, J Van Reenen and M Webb (2020), “Are Ideas Getting Harder to
Find?”, American Economic Review 110(4): 1104–44.
Bloom, N. and Makridis, C (2026), “The politics of AI”, NBER WP 34813.
Boddin, D, M Köhler and P Smietanka (2024), “Bundesbank Online Panel - Firms Data
Report 2023-07”, DOI: 10.12757/BBk.BOPF.2022Q2.01.
Bonney, K, C Breaux, C Buffington, E Dinlersoz, L S Foster, N Goldschlag, J C
Haltiwanger, Z Kroff and K Savage (2024), “Tracking firm use of AI in real-time: A
snapshot from the Business Trend and Outlook Survey”, NBER Working Paper 32319.
Briggs, J and D Kodnani (2023), “The Potentially Large Effects of Artificial Intelligence on
Economic Growth”, Goldman Sachs Global Economics Analyst, 26 March.

Brynjolfsson, E, D Li and L Raymond (2025a), “Generative AI at Work”, The Quarterly
Journal of Economics 140(2): 889-942.


                                             19
Brynjolfsson, E, B Chandar and R Chen (2025b), “Canaries in the Coal Mine? Six Facts
about the Recent Employment Effects of Artificial Intelligence”, Working Paper.
Bunn, P, N Bloom, A Crundwell, S Khan, C Menzies, P Mizen, M Sculthorpe, K Shah, G
Thwaites and I Yotzov (2024), “The Decision Maker Panel: A User’s Guide”, Bank of
England Staff Working Paper 1096.
Cañas, J and E Kerr (2024), “Texas firms using AI report little impact on employment”,
Federal Reserve Bank of Dallas, 25 June.
Chandler, J and G Paolacci (2017), "Lie for a Dime: When Most Prescreening Responses Are
Honest but Most Study Participants Are Impostors", Social Psychological Personality
Science 8(5): 500-508.
Choi, J H and D Schwarcz (2025), “AI Assistance in Legal Analysis: An Empirical Study”,
Journal of Legal Education 73(2): 384-420.
Cui, Z (Kevin), M Demirer, S Jaffe, L Musolff, S Peng and T Salz (2025), “The Effects of
Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software
Developers”, SSRN Scholarly Paper No. 4945566.
Dell’Acqua, F, E McFowland III, E Mollick, H Lifshitz-Assaf, K Kellogg, S Rajendran, L
Krayer, F Candelon and K R Lakhani (2023), “Navigating the Jagged Technological Frontier:
Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and
Quality”, Harvard Business School Working Paper.
del Rio-Chanona, R. Maria, Ekkehard Ernst, Rossana Merola, Daniel Samaan, and Ole
Teutloff. 2025. “AI and Jobs: A Review of Theory, Estimates, and Evidence.” arXiv preprint
arXiv:2509.15265v1
Eisfeldt, A L, G Schubert, B Taska and M Ben Zhang (Forthcoming), “Generative AI and
Firm Values”, Journal of Finance.

Goldin, I, P Koutroumpis, F Lafond and J Winkler (2024), “Why Is Productivity Slowing
Down?”, Journal of Economic Literature 62(1): 196–268.
Hartley, J, F Jolevski, V Melo and B Moore (2025), “The Labor Market Effects of Generative
Artificial Intelligence”, SSRN Working Paper
Humlum, A and E Vestergaard (2025), “Large Language Models, Small Labor Market
Effects”, University of Chicago working paper.
Institute of Directors (2025), “Major blockers to AI adoption in British business”, 28 April.
McElheran, K, J F Li, E Brynjolfsson, Z Kroff, E Dinlersoz, L S Foster and N Zolas (2024),
“AI Adoption in America: Who, What, and Where”, Journal of Economics & Management
Strategy 33(2): 375–415.

McKinsey (2025), “The state of AI in 2025: Agents, innovation, and transformation”,
November.
Misch, F, B Park, C Pizinelli and G Sher (2025), “AI and Productivity in Europe”, IMF
Working Paper 2025/067.


                                              20
Noy, S and W Zhang (2023), “Experimental evidence on the productivity effects of
generative artificial intelligence”, Science 381(6654).
ONS (2025), “Management practices and the adoption of technology and artificial
intelligence in UK firms: 2023”, 24 March.
Oliveira-Cunha, J, B Serra-Lorenzo, A Valero (2024), “What an LSE-CBI survey found
about AI adoption in UK firms”, 2 July.
Peng, S, E Kalliamvakou, P Cihon and M Demirer (2023), “The Impact of AI on Developer
Productivity: Evidence from GitHub Copilot”, Working Paper.

Sidoti, O and C McClain (2025), “34% of U.S. adults have used ChatGPT, about double the
share in 2023”, PEW Research Center Short Read.
Teutloff, O, J Einsiedler, O Kassi, F Braesemann, P Mishkin and R Maria del Rio-Chanona
(2025), “Winners and losers of generative AI: Early Evidence of Shifts in Freelancer
Demand”, Journal of Economic Behavior & Organization 235, 106845.




                                            21
Figure 1 Media coverage of AI and the Economy since 2015
                                       2500                                                Source: AI Economic
                                                                                           Uncertainty       Index,
                                                                                           measuring            the




Media coverage of AI and the Economy
                                                                                           coverage of AI in
                                       2000                                                around 2000 daily
                                                                                           newspapers in the
                                                                                           US. Normalized to
                                                                                           100 on 2015 to 2021
                                                                                           inclusive. Coverage
                                       1500
                                                                                           defined as articles
                                                                                           that included (AI,
                                                                                           artificial intelligence,
                                                                                           genAI,         machine
                                       1000                                                learning,     computer
                                                                                           vision)             AND
                                                                                           (economic,
                                                                                           economy). Based on
                                        500                                                the methodology of
                                                                                           Baker, Bloom and
                                                                                           Davis (2016) and
                                                                                           provided              on
                                          0                                                www.policyuncertaint
                                                                                           y.com
                                              2016   2018   2020      2022   2024   2026
                                                               Year
   Figure 2 Position of respondents within their firm

       Panel A US Firms (SBU)                                                                             Panel B UK Firms (DMP)

                                                                                                         70
                                                                                                                                            64.4

                                                                                                         60




                                                                          Percentage of businesses (%)
                                                                                                         50


                                                                                                         40


                                                                                                         30


                                                                                                         20
                                                                                                                     13.8                                         14.8

                                                                                                         10                                                                     7.1


                                                                                                          0
                                                                                                              CEO/Chief Executive   CFO/Finance Director   Senior Management   Other




Notes: This figure shows the position of survey respondents. Panel A shows data from the US Survey of Business Uncertainty (SBU), averaged over
January 2017 to January 2025. Panel B shows data from the UK Decision Maker Panel (DMP), averaged over 2017-2025.
  Figure 3 Firm sales and employment growth vs aggregate statistics
                         Panel A Sales growth                                                 Panel B Employment growth



 US Firms
 (SBU)




 UK Firms
 (DMP)


Sources: SBU; ADP; BEA; DMP; ONS; HMRS and authors’ calculations. Notes: SBU sales data are compared to GDP growth from the BEA. SBU employment growth
data are compared to ADP employment growth. DMP sales data are compared to whole economy nominal GDP growth at current market prices. DMP employment (for the
private sector) is compared to ONS/HMRC data on the number of payrolled employees. DMP and SBU data are adjusted to match the mean and variance of growth in the
corresponding ONS, HMRC, GDP, and ADP series over the time period shown on each chart.
  Figure 4 Sales and Employment Forecasts vs Realizations
                                                         Panel A Sales growth                                                                                   Panel B Employment growth



US Firms
(SBU)


                                             40                                                                                                          20




                                                                                                                                                         10




                                                                                                                              Annual employment growth
UK Firms
                                             20




                       Annual sales growth
                                                                                                                                                          0


(DMP)                                         0
                                                                                                                                                                                                            Coef = .47** (.01)
                                                                                                                                                         -10                                                90% CI = [.46 , .48]
                                                                                                                                                                                                               N = 40717

                                                                                                      Coef = .49** (.01)
                                                                                                      90% CI = [.48 , .51]
                                             -20                                                         N = 35857                                       -20
                                                   -40      -20      0                20             40                  60                                    -40    -20                    0                       20            40
                                                                  Expected sales growth a year ago                                                                          Expected employment growth a year ago


Notes: This figure shows binned scatter plots of the relationship between expected year-ahead sales growth and annual sales growth a year later at the firm level (Panel A)
and expected year-ahead employment growth and annual employment growth a year later (Panel B). The sample from the SBU covers 2014-2025. The sample from the
UK DMP covers 2017-2025.
 Figure 5 Current use of AI technologies by businesses




Notes: This figure is based on responses to the question: “Which of the following artificial intelligence technologies, if any, does your business currently use?” Firms could
select more than one option. The data from the US Survey of Business Uncertainty was collected in November 2025. The data from the UK Decision Maker Panel was
collected over November 2025 – January 2026. The data from the German Bundesbank Online Panel-Firms (BOP-F) was collected in January 2026. The data from the
Australian Business Outlook Scenarios Survey was collected in December 2025. The data results from the SBU, DMP, and BOP-F are employment-weighted; the results
from the BOSS are unweighted. The results for all firms is the average of the four surveys, weighted by the respective number of responses.
Figure 6 Characteristics of firms using AI technologies (UK Firms)
   Panel A Labor Productivity                                                                                                                                    Panel B Firm employment                                                   Panel C Average wage per employee
                                                                                                                                                                90
                                           80                                                                                                                                                                                                                                         90




   Percentage of businesses using AI (%)                                                                                Percentage of businesses using AI (%)                                                                                 Percentage of businesses using AI (%)
                                                                                                                                                                80                                                                                                                    80
                                           70

                                                                                                                                                                                                                                                                                      70
                                                                                                                                                                70
                                           60
                                                                                                                                                                                                                                                                                      60

                                                                                                                                                                60
                                           50                                                                                                                                                                                                                                         50
                                                                                              Coef = 6.31** (1.26)
                                                                                              90% CI = [4.25 , 8.38]
                                                                                                   N = 2065
                                                                                                                                                                                                                   Coef = 3.22** (.56)                                                                                      Coef = 12.72** (1.89)
                                                                                                                                                                50                                                90% CI = [2.3 , 4.14]                                               40                                    90% CI = [9.62 , 15.83]
                                           40                                                                                                                                                                          N = 2772                                                                                                   N = 2107

                                                     10                             100                    500    800                                                          10              100        500 1000                  8000                                                   10    20       35           70             150
                                                                    Labor Productivity (log scale)                                                                                   Latest Employment (log scale)                                                                              Average Wage per Employee (log scale)


 Panel D Average age of directors                                                                                                                                Panel E Firm age
                                           80                                                                                                                   80




   Percentage of businesses using AI (%)                                                                                Percentage of businesses using AI (%)
                                                                                                                                                                70
                                           70


                                                                                                                                                                                                                                                                                      Notes: This figure shows binned scatter plots.
                                           60
                                                                                                                                                                60                                                                                                                    The vertical axis is the percentage of businesses
                                                                                                                                                                                                                                                                                      currently using any AI technology. The data are
                                                                                                                                                                                                                                                                                      from the UK Decision Maker Panel, collected
                                           50
                                                                                                                                                                50
                                                                                                                                                                           Coef = -.11 (.06)                                                                                          over February-April 2025 and November 2025 –
                                                      Coef = -.53** (.12)
                                                     90% CI = [-.73 , -.32]
                                                                                                                                                                         90% CI = [-.21 , -.02]
                                                                                                                                                                              N = 2775                                                                                                January 2026, with the latest firm observation
                                                          N = 2460
                                                                                                                                                                                                                                                                                      used in the figures.
                                                                                                                                                                40
                                           40
                                                                                                                                                                     0                  20                   40                    60
                                                40               50             60             70                  80
                                                                                                                                                                                                  Firm Age
                                                                      Average Age of Directors
 Figure 7 Frequency of AI use by survey respondent
   Panel A Distribution of responses                                                                  Panel B Average AI use per week




Notes: This figure is based on responses to the question: “On average, how frequently do you personally use artificial intelligence technologies in a typical working week?”
The data from the US Survey of Business Uncertainty was collected in November 2025. The data from the UK Decision Maker Panel was collected over November 2025 –
January 2026. The data from the Australian Business Outlook Scenarios Survey was collected in December 2025. The data from the German Bundesbank Online Panel –
Firms (BOP-F) were collected in January 2026. The data results from the SBU, DMP, and BOP-F are employment-weighted; the results from the BOSS are unweighted.
The results for all firms is the average of the four surveys, weighted by the respective number of responses. To calculate the average use per week (Panel B), values are
assigned to each of the options in Panel A: 0 to “Not at all”; 0.5 to “up to 1 hour a week”; 3 to “1 to 5 hours a week”; 7.5 to “>5 hours a week”.
Figure 8 Impact of AI on employment over past 3 years
  Panel A Distribution of responses                                                                    Panel B Average impacts




Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected the number of employees in your business
over the past three years?” The data from the US Survey of Business Uncertainty was collected in November 2025. The data from the UK Decision Maker Panel was
collected over November 2025 – January 2026. The data from the German Bundesbank Online Panel-Firms (BOP-F) was collected in January 2026. The data from the
Australian Business Outlook Scenarios Survey was collected in December 2025. The data results from the SBU, DMP, and BOP-F are employment-weighted; the results
from the BOSS are unweighted. To calculate the average impacts (Panel B), values are assigned to each of the options in Panel A: large negative/large positive impacts
are treated as ±7.5%; small negative/small positive impacts are treated as ±2.5%. The impact for all firms is the average of the impacts for the four surveys, weighted by
the respective number of responses. 90% confidence intervals are shown for these impacts.
 Figure 9 Expected impact of AI on employment over next 3 years
    Panel A Distribution of responses                                                                Panel B Average impacts




Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected the number of employees in your business
over the past three years? And how do you expect this to affect your number of employees over the next 3 years?” The data from the US Survey of Business Uncertainty
was collected in November 2025. The data from the UK Decision Maker Panel was collected over November 2025 – January 2026. The data from the German
Bundesbank Online Panel-Firms (BOP-F) was collected in January 2026. The data from the Australian Business Outlook Scenarios Survey was collected in December
2025. The data results from the SBU, DMP, and BOP-F are employment-weighted; the results from the BOSS are unweighted. To calculate the average impacts (Panel
B), values are assigned to each of the options in Panel A: large negative/large positive impacts are treated as ±7.5%; small negative/small positive impacts are treated as
± 2.5%. The impact for all firms is the average of the impacts for the four surveys, weighted by the respective number of responses. 90% confidence intervals are shown
for these impacts.
Figure 10 Impact of AI on productivity over past 3 years
   Panel A Distribution of responses                                                                 Panel B Average impacts




Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected the volume of sales per employee in your
business over the past three years?” The data from the US Survey of Business Uncertainty was collected in November 2025. The data from the UK Decision Maker Panel
was collected over November 2025 – January 2026. The data from the German Bundesbank Online Panel-Firms (BOP-F) was collected in January 2026. The data from
the Australian Business Outlook Scenarios Survey was collected in December 2025. The data results from the SBU, DMP, and BOP-F are employment-weighted; the
results from the BOSS are unweighted. To calculate the average impacts (Panel B), values are assigned to each of the options in Panel A: large negative/large positive
impacts are treated as ±7.5%; small negative/small positive impacts are treated as ±2.5%. The impact for all firms is the average of the impacts for the four surveys,
weighted by the respective number of responses. 90% confidence intervals are shown for these impacts.
Figure 11 Expected impact of AI on productivity over next 3 years
   Panel A Distribution of responses                                                                  Panel B Average impacts




Notes: This figure is based on responses to the question: “How has the adoption of artificial intelligence technologies affected volume of sales per employee in your
business over the past three years? And how do you expect this to affect your volume of sales per employee over the next 3 years?” The data from the US Survey of
Business Uncertainty was collected in November 2025. The data from the UK Decision Maker Panel was collected over November 2025 – January 2026. The data from
the German Bundesbank Online Panel-Firms (BOP-F) was collected in January 2026. The data from the Australian Business Outlook Scenarios Survey was collected in
December 2025. The data results from the SBU, DMP, and BOP-F are employment-weighted; the results from the BOSS are unweighted. To calculate the average
impacts (Panel B), values are assigned to each of the options in Panel A: large negative/large positive impacts are treated as ±7.5%; small negative/small positive impacts
are treated as ±2.5%. The impact for all firms is the average of the impacts for the four surveys, weighted by the respective number of responses. 90% confidence
intervals are shown for these impacts.
   Figure 12 Impacts of AI and weekly AI use by employees
  Panel A AI Use at work                                           Panel B Past 3 Years                                Panel C Next 3 Years




Responses to the questions: You indicated that you sometimes use Generative AI for your job. Did you use Generative AI for your job LAST WEEK? Please think back to the
days LAST WEEK on which you used Generative AI for your job. On average, how much time did you spend actively using Generative AI for your job How has the adoption of
Artificial Intelligence technologies affected the NUMBER OF EMPLOYEES who work for your employer: over the past three years? over the next three years? How has the
adoption of Artificial Intelligence technologies affected your employer's SALES PER WORKER (PRODUCTIVITY): over the past three years? over the next three years?

Notes: The sample includes respondents to the December 2025 SWAA wave who worked for pay during the week prior to the survey and pass our attention-check questions.
In Panel A, we impute zero AI use for respondents who did not use it last week, or do not use it for their job. In Panels B and C, we restrict attention to wage and salary
employees, (excluding self-employed workers and contractors). We reweight the raw responses to match the 2024 US population in cells defined by the cross product of age,
sex, education and earnings.
   Table 1 Characteristics of firms using AI technologies (UK Firms)
                                            (1)       (2)       (3)        (4)      (5)       (6)       (7)        (8)        (9)       (10)       (11)      (12)       (13)
  Dependent Variable:                                                              Any AI Technology Currently Used (scaled by 100)
  Labor productivity (logs)               6.31***                                                                                                            3.16*      3.04*
                                          (1.23)                                                                                                             (1.82)     (1.83)
  Employment (logs)                                 3.22***                                                                                                 4.99***    4.88***
                                                    (0.51)                                                                                                   (0.59)     (0.60)
  Average Wage per Employee (logs)                            12.72***                                                                                       6.43**     6.87**
                                                               (1.77)                                                                                        (2.75)     (2.77)
  Firm Age                                                               -0.11*                                                                              0.15**     0.15*
                                                                         (0.06)                                                                              (0.08)     (0.08)
  Average Age of Directors                                                         -0.53***                                                                 -0.60***   -0.61***
                                                                                    (0.12)                                                                   (0.16)     (0.16)
  Average productivity growth (2025)                                                          0.22**                                                         0.24**
                                                                                              (0.11)                                                         (0.11)
  Expected productivity growth (2025)                                                                   0.38*                                                 0.15
                                                                                                        (0.21)                                               (0.20)
  Average real sales growth (2025)                                                                                  0.10                                                0.12
                                                                                                                   (0.09)                                              (0.09)
  Expected real sales growth (2025)                                                                                           0.21                                     -0.18
                                                                                                                             (0.18)                                    (0.19)
  Average employment growth (2025)                                                                                                      -0.06                          -0.17
                                                                                                                                        (0.10)                         (0.11)
  Expected employment growth (2025)                                                                                                                0.22                 0.06
                                                                                                                                                  (0.18)               (0.18)
  Mean of Dependent Variable               63.6      63.6       63.6      63.6      63.6       63.6      63.6       63.6      63.6      63.6       63.6      63.7       63.7
  SIC2 industry and time fixed effects      No        No         No        No        No         No        No         No        No        No         No       Yes        Yes
Notes: The dependent variable is an indicator for whether the firm currently uses an AI technology, scaled by 100 for interpretability. The data from the UK Decision Maker
Panel was collected over February-April 2025 and November 2025 – January 2026, with the latest firm observation used in the regressions (N=2,793). A constant has also
been estimated, but not reported in the table. Where data are missing for a particular variable a dummy variable is included to account for that (results not reported). Standard
errors are clustered at the firm level, stars indicate *** p<0.01, ** p<0.05, * p<0.1.
Table 2 Determinants of expected AI employment impacts (UK Firms)
                                         (1)       (2)       (3)      (4)         (5)      (6)       (7)       (8)        (9)        (10)      (11)      (12)       (13)
 Dependent Variable:                                                          Expected AI Employment Impact over next 3 Years (%)
 Labor productivity (logs)               -0.10                                                                                                            -0.08      -0.11
                                        (0.07)                                                                                                           (0.12)     (0.12)
 Employment (logs)                               -0.18***                                                                                               -0.20***   -0.20***
                                                  (0.03)                                                                                                 (0.04)     (0.04)
 Average Wage per Employee (logs)                           -0.19*                                                                                        -0.05      -0.10
                                                            (0.10)                                                                                       (0.18)     (0.17)
 Firm Age                                                             -0.00                                                                               -0.01      -0.01
                                                                     (0.00)                                                                              (0.00)     (0.00)
 Average Age of Directors                                                        0.01                                                                     0.02*     0.02**
                                                                                (0.01)                                                                   (0.01)     (0.01)
 Average productivity growth (2025)                                                        -0.01                                                          -0.01
                                                                                          (0.01)                                                         (0.01)
 Expected productivity growth (2025)                                                                -0.02*                                                -0.02
                                                                                                    (0.01)                                               (0.01)
 Average real sales growth (2025)                                                                              0.01                                                 0.00
                                                                                                              (0.01)                                               (0.01)
 Expected real sales growth (2025)                                                                                       0.01                                       -0.00
                                                                                                                        (0.01)                                     (0.01)
 Average employment growth (2025)                                                                                                   0.03***                        0.02***
                                                                                                                                    (0.01)                         (0.01)
 Expected employment growth (2025)                                                                                                            0.05***              0.05***
                                                                                                                                              (0.01)               (0.01)
 Mean of Dependent Variable              -0.9     -0.9       -0.9     -0.9       -0.9      -0.9      -0.9      -0.9      -0.9        -0.9      -0.9      -0.9        -0.9
 SIC2 industry and time fixed effects     No       No         No       No         No        No        No        No        No          No        No       Yes         Yes

Notes: The data from the UK Decision Maker Panel was collected over February-April 2025 and November 2025 – January 2026, with the latest firm observation used in
the regressions. A constant has also been estimated, but not reported in the table (N=2,793). Where data are missing for a particular variable a dummy variable is
included to account for that (results not reported). Standard errors are clustered at the firm level, stars indicate *** p<0.01, ** p<0.05, * p<0.1.
Table 3 Determinants of expected AI productivity impacts (UK Firms)
                                         (1)      (2)       (3)       (4)         (5)        (6)        (7)       (8)        (9)       (10)      (11)      (12)       (13)
 Dependent Variable:                                                           Expected AI Productivity Impact over next 3 Years (%)
 Labor productivity (logs)               0.01                                                                                                               -0.17    -0.18*
                                        (0.06)                                                                                                             (0.10)    (0.10)
 Employment (logs)                                0.06*                                                                                                    0.15***   0.14***
                                                 (0.03)                                                                                                    (0.04)    (0.04)
 Average Wage per Employee (logs)                         0.29***                                                                                          0.36**    0.38**
                                                          (0.10)                                                                                           (0.16)    (0.16)
 Firm Age                                                           -0.01***                                                                                -0.00     -0.00
                                                                     (0.00)                                                                                (0.00)    (0.00)
 Average Age of Directors                                                       -0.04***                                                                  -0.02***   -0.02**
                                                                                 (0.01)                                                                    (0.01)    (0.01)
 Average productivity growth (2025)                                                          0.01                                                           0.01
                                                                                            (0.01)                                                         (0.01)
 Expected productivity growth (2025)                                                                   0.01                                                 0.00
                                                                                                      (0.01)                                               (0.01)
 Average real sales growth (2025)                                                                                 0.01*                                               0.00
                                                                                                                 (0.00)                                              (0.01)
 Expected real sales growth (2025)                                                                                         0.04***                                    0.02
                                                                                                                           (0.01)                                    (0.01)
 Average employment growth (2025)                                                                                                       0.00                          -0.00
                                                                                                                                       (0.01)                        (0.01)
 Expected employment growth (2025)                                                                                                              0.03***               0.02*
                                                                                                                                                (0.01)               (0.01)
 Mean of Dependent Variable              1.7      1.7      1.7        1.7          1.7       1.7        1.7       1.7       1.7         1.7       1.7      1.7         1.7
 SIC2 industry and time fixed effects    No       No       No         No           No        No         No        No        No          No        No       Yes         Yes

Notes: The data from the UK Decision Maker Panel was collected over February-April 2025 and November 2025 – January 2026, with the latest firm observation used in
the regressions (N=2,793). A constant has also been estimated, but not reported in the table. Where data are missing for a particular variable a dummy variable is
included to account for that (results not reported). Standard errors are clustered at the firm level, stars indicate *** p<0.01, ** p<0.05, * p<0.1.
Table 4 Summary of realised and expected AI impacts
                                                                     Firms                                              Employees
                                                                                  Germany            Australia
                                   All        US (SBU)          UK (DMP)                                               US (SWAA)
                                                                                  (BOP-F)            (BOSS)
    Cumulative impact over past 3 years (%)

    Sales/Employee                0.29              0.24              0.29              0.24              0.49               0.49

    Employment                    0.00              -0.09             -0.14             0.07              0.32               0.33

    Output (implied)              0.28              0.15              0.15              0.32              0.82               0.82

    Expected cumulative impact over next 3 years (%)

    Sales/Employee                1.44              2.25              1.86              0.87              0.92               0.92

    Employment                    -0.68             -1.19             -1.36             -0.06             0.05               0.45

    Output (implied)              0.76              1.06              0.50              0.81              0.96               1.37

    Notes: This table summarises the realised and expected AI impacts on sales per employee and employment from Figures 8-11. The implied
    impacts on output are calculated as the sum of the sales/employee and employment impacts.
Figure A1 SBU vs. US industrial and regional distribution

Panel A: By Industry                                                                    Panel B: By Region

                                                       Economic Census
                       Construction                                                        South Atlantic
                                                       SBU Data
               Educational services
                                                                                                   Pacific
             Finance and insurance
  Health care and social assistance                                                    East North Central

                         Information                                                       Middle Atlantic
             Leisure and hospitality
                                                                                      West South Central
                      Manufacturing
                 Mining and utilities                                                           Mountain

 Professional and business services                                                   West North Central
  Real estate and rental and leasing
                                                                                      East South Central
         Retail and wholesale trade
                                                                                                                                             Economic Census
    Transportation and warehousing                                                          New England
                                                                                                                                             SBU Data

                                        0   5    10    15      20   25
                                                                                                             0      5       10       15         20         25
                                            Percentage of firms (%)                                                     Percentage of firms (%)

Notes: This figure compares the percentage of firms by industry (Panel A) and region (Panel B) in the US Survey of Business Uncertainty against the 2022 Economic
Census. The shares are employment-weighted. Panel A is based on 6835 firms in the SBU. Panel B is based on 6995 firms in the SBU.
Figure A2 DMP vs. UK industrial and regional distribution

Panel A: By Industry                                                                        Panel B: By Region

                Manufacturing
             Other Production
                 Construction
           Wholesale & Retail
          Transport & Storage
      Accommodation & Food
Information & Communications
         Finance & Insurance
                  Real Estate
      Professional & Scientific
     Administration & Support
                        Health
        Recreational Services
                                                           Business register shares
               Other Services                              DMP data

                                  0        5            10         15           20
                                               Percentage of employment


Notes: Other production includes agriculture; forestry & fishing; mining & quarrying; electricity, gas & air conditioning supply; water supply; and sewerage, waste
management & remediation activities. Data are averages from 2017 to 2025.
Figure A3 Firm responses vs. company accounts data (UK firms)
                                                8                                                                                                14



                                                7




                   Log employment in DMP data
                                                                                                                                                 12




                                                                                                                         Log Sales in DMP data
                                                6

                                                                                                                                                 10
                                                5


                                                                                                                                                  8
                                                4



                                                3
                                                                                                                                                  6
                                                     2       4                               6                    8                                   6       8               10               12               14
                                                                 Log employment in accounts data                                                                  Log Sales in accounts data


                                                                                                                                                 .4
                                                                                                        DMP data                                                                                    DMP data
                                                .3
                                                                                                        Accounts data                                                                               Accounts data

                                                                                                                                                 .3

                                                .2


                  Density                                                                                               Density
                                                                                                                                                 .2



                                                .1
                                                                                                                                                 .1




                                                0                                                                                                0
                                                     2   4         6               8               10        12                                       2   4   6   8          10          12    14      16       18
                                                                         Log employment                                                                                   Log sales



Notes: Sales values from the DMP survey are annualised average quarterly sales reported by businesses across the year. DMP employment data are averages across the
year. DMP data are plotted against annual company accounts data from Bureau Van Dijk for the corresponding financial year. The dots on the top charts each represent 5% of
observations, grouped by log employment/sales from accounts data. Charts are based on annual data between 2017 and 2024.
Figure A4 Change in current use of AI technologies by businesses (UK Firms)

                                             80
                                                                                                                                        Feb-Apr 2025
                                                         71
                                             70                                                                                         Nov-25 to Jan-26




              Percentage of businesses (%)
                                                    61
                                             60

                                             50

                                             40
                                                                                   33             35
                                                                      33
                                                                 29           29                               29
                                             30
                                                                                                                              25
                                                                                             23
                                                                                                          19
                                             20                                                                          18
                                                                                                                                   13    14

                                             10
                                                                                                                                                   2.7    3
                                              0
                                                  Any AI Tech      Data          Text         Other    Visual content   Image      Robotics     Autonomous
                                                                processing   generation                   creation    processing                  vehicles
                                                                 using ML    using LLMs                                using ML
                                                                                        AI Technologies Currently Used

Notes: This figure is based on responses to the question: “Which of the following artificial intelligence technologies, if any, does your business currently use?” The results are
based on responses from the UK Decision Maker Panel, collected over February-April 2025 and November 2025 – January 2026. The results are employment-weighted.
   Figure A5 Characteristics of firms using AI technologies (US Firms)
   Panel A Labor Productivity                                                               Panel B Firm employment




Notes: This figure shows binned scatter plots. The vertical axis is the percentage of businesses currently using any AI technology. The data are from the US Survey of Business
Uncertainty, collected in November 2025. Labor productivity is defined as sales revenue per employee, and deflated using 2016 gross output deflators.
  Figure A6 Current and expected AI adoption by industry (UK firms)
        Panel A Current AI Adoption                                                              Panel B Expected Adoption Next 3
                                                                                                 Years
         Prof & Scientific                                                  87
                                                                                                        Real Estate                                                        87
   Finance & Insurance                                                      86
                                                                                                   Prof & Scientific                                                     84
           Info & Comms                                                    83
                                                                                                  Admin & Support                                                     83
    Transport & Storage                                               73
                                                                                                Wholesale & Retail                                                    83
             Real Estate                                              72
                                                                                                  Other Production                                                   82
     Wholesale & Retail                                               71
                                                                                                     Manufacturing                                                   82
       Admin & Support                                               70
                                                                                              Finance & Insurance                                                    80
           Manufacturing                                             69
                                                                                                    Other Services                                                  79
          Other Services                                         66
                                                                                                     Info & Comms                                                   79
                   Health                                        66
                                                                                            Recreational Services                                               76
  Recreational Services                                          66
                                                                                              Transport & Storage                                              75
       Other Production                                         63
                                                                                                             Health                                            75
            Construction                                        63
                                                                                                       Construction                                            73
          Accom & Food                                     58
                                                                                                    Accom & Food                                          68


                             0      20      40       60       80                 100                                   0       20      40       60       80                     100
                                     Percentage of businesses (%)                                                               Percentage of businesses (%)

Notes: This figure is based on responses to the question: “Which of the following artificial intelligence technologies, if any, does your business currently use? And which do you
intend to make use of over the next three years?” The results are based on responses from the UK Decision Maker Panel, collected over November 2025 – January 2026. The
results are employment-weighted.
Figure A7 Expected use of AI technologies over next 3 years




Notes: This figure is based on responses to the question: “Which of the following artificial intelligence technologies, if any, does your business currently use? And which
do you intend to make use of over the next three years?” Firms could select more than one option. The data from the US Survey of Business Uncertainty was collected in
November 2025. The data from the UK Decision Maker Panel was collected over November 2025 – January 2026. The data from the German Bundesbank Online Panel –
Firms (BOP-F) were collected in January 2026. The data from the Australian Business Outlook Scenarios Survey was collected in December 2025. The data results from
the SBU, DMP, and BOP-F are employment-weighted; the results from the BOSS are unweighted. The results for all firms is the average of the four surveys, weighted by
the respective number of responses.
  Figure A8.a Frequency of AI use by survey respondent: Heterogeneity by
  firm characteristics (UK Firms)

                                                   Panel A Firm age                                                 Panel B Average age of firm directors
                                                   2.5                                                                                                      3




   Average AI use by respondent per week (hours)                                                           Average AI use by respondent per week (hours)
                                                                                                                                                           2.5
                                                    2


                                                                                                                                                            2

                                                   1.5

                                                                                                                                                           1.5


                                                    1          Coef = -.02** (0)
                                                             90% CI = [-.02 , -.01]
                                                                  N = 2625                                                                                  1
                                                                                                                                                                       Coef = -.04** (.01)
                                                                                                                                                                      90% CI = [-.05 , -.04]
                                                                                                                                                                           N = 2332
                                                    .5                                                                                                      .5
                                                         0                  20                   40   60                                                         40                50             60             70   80
                                                                                      Firm Age                                                                                          Average Age of Directors

Notes: The binned scatter plots are based on responses from the UK Decision Maker Panel, collected over February-March 2025 and November 2025 – January 2026.
  Figure A8.b Frequency of AI use by survey respondent: Heterogeneity by
  firm age (US Firms)




Notes: This figure presents a binned scatter plot of average weekly AI use by the survey respondent again firm age. It is based on responses to the question: “On average,
how frequently do you personally use artificial intelligence technologies in a typical working week?” The data from the US Survey of Business Uncertainty was collected in
November 2025.
 Figure A9 Frequency of AI use by survey respondent: Heterogeneity by
 respondent position
   Panel A US Firms (SBU)                Panel B UK Firms (DMP)
                                                                                                                                                  50
                                                                                                                        50
                                                                                                                                                                        CEO
                                                                                                                                                                        CFO
                                                                                                                                                                        Senior Execs
                                                                                                                        40                                              (excl. CEO/CFO)




                                                                                        Percentage of respondents (%)
                                                                                                                                                       38
                                                                                                                                             34


                                                                                                                        30
                                                                                                                                                              27
                                                                                                                                       26
                                                                                                                             24                                         25
                                                                                                                                  24                               23

                                                                                                                        20
                                                                                                                                                                                 15
                                                                                                                                                                                           12
                                                                                                                        10

                                                                                                                                                                                      3

                                                                                                                         0
                                                                                                                              Not at all    <1 hour a week   1-5 hours a week   >5 hours a week
                                                                                                                                    Frequency of AI use by DMP respondent

Notes: This figure is based on responses to the question: “On average, how frequently do you personally use artificial intelligence technologies in a typical working week?”
The data from the US Survey of Business Uncertainty was collected in November 2025. The data from the UK Decision Maker Panel was collected over November 2025 –
January 2026. The data are employment-weighted.
  Figure A10 Frequency of AI use by survey respondent: Feb-March 2025 vs.
  Nov-25 to Jan-26 (UK Firms)
                                              50                                                                                    Feb-March 2025
                                                   45                          45                                                   Nov-25 to Jan-26

                                              40




              Percentage of respondents (%)
                                                                   36



                                              30
                                                             25
                                                                                                                 23

                                              20
                                                                                                    15


                                              10
                                                                                                                                                   6
                                                                                                                                      4

                                               0
                                                    Not at all    <1 hour a week                  1-5 hours a week                 >5 hours a week
                                                                  Frequency of AI use by DMP respondent

Notes: This figure is based on responses to the question: “On average, how frequently do you personally use artificial intelligence technologies in a typical working week?” The
results are based on responses from the UK Decision Maker Panel, collected over February-March 2025 and November 2025 – January 2026.
   Figure A11 Realised and expected impacts of AI on employment
   by industry (UK Firms)
        Panel A Past 3 Years                                                                Panel B Next 3 Years
            Construction                                                   0.1           Other Production                                         -0.7
             Real Estate                                                  0.1                       Health                                       -0.7
       Admin & Support                                                    0.0        Recreational Services                                       -0.7
         Other Services                                                   0.0              Other Services                                       -0.8
    Finance & Insurance                                            -0.0                       Construction                                      -0.8
                  Health                                          -0.0                    Prof & Scientific                              -1.2
          Manufacturing                                           -0.1                         Real Estate                           -1.2
     Wholesale & Retail                                       -0.1                    Finance & Insurance                            -1.2
   Recreational Services                                      -0.2                    Transport & Storage                           -1.2
          Info & Comms                                        -0.2                          Manufacturing                           -1.3
        Prof & Scientific                                    -0.2                           Info & Comms                           -1.3
       Other Production                                    -0.4                          Admin & Support                          -1.4
    Transport & Storage                                    -0.4                            Accom & Food                 -1.8
         Accom & Food                                  -0.4                             Wholesale & Retail           -2.0


                            -2.5    -2     -1.5 -1       -.5    0     .5         1                            -2.5          -2     -1.5         -1       -.5   0   .5   1
                                         Impact over last 3 years (%)                                                            Impact over next 3 years (%)
                            Source: Decision Maker Panel                                                      Source: Decision Maker Panel


Notes: The results are based on responses from the UK Decision Maker Panel, collected over November 2025 – January 2026. The results are employment-weighted.
  Figure A12 Realised and expected impacts of AI on productivity
  by industry (UK Firms)
        Panel A Past 3 Years                                                                Panel B Next 3 Years
            Info & Comms                    0.8                                               Info & Comms                                                                           2.8
          Prof & Scientific          0.5                                                   Admin & Support                                                                     2.5
            Manufacturing            0.5                                                    Prof & Scientific                                                                  2.5
           Accom & Food           0.4                                                   Finance & Insurance                                                        2.1
      Finance & Insurance        0.3                                                     Wholesale & Retail                                                  1.9
         Admin & Support       0.2                                                            Manufacturing                                                1.8
     Recreational Services     0.2                                                      Transport & Storage                                                1.8
           Other Services      0.2                                                                    Health                                         1.6
                    Health     0.2                                                               Real Estate                                         1.6
      Transport & Storage      0.2                                                           Other Services                                  1.2
               Real Estate   0.1                                                             Accom & Food                                1.2
       Wholesale & Retail   0.1                                                        Recreational Services                           1.0
              Construction 0.0                                                                  Construction                 0.7
         Other Production 0.0                                                              Other Production           0.4


                            0       .5       1       1.5    2      2.5    3                                     0      .5          1           1.5           2           2.5          3
                                         Impact over last 3 years (%)                                                       Impact over next 3 years (%)
                             Source: Decision Maker Panel                                                       Source: Decision Maker Panel


Notes: The results are based on responses from the UK Decision Maker Panel, collected over November 2025 – January 2026. The results are employment-weighted.
 Table A1 Number of AI technologies currently used (UK Firms)
                                         (1)       (2)        (3)       (4)        (5)       (6)       (7)       (8)        (9)       (10)      (11)       (12)      (13)
Dependent Variable:                                                                  Number of AI Technologies Currently Used
Labor productivity (logs)              0.23***                                                                                                            0.14**     0.14**
                                       (0.04)                                                                                                             (0.06)     (0.06)
Employment (logs)                                0.10***                                                                                                  0.18***    0.17***
                                                 (0.02)                                                                                                   (0.02)     (0.02)
Average Wage per Employee (logs)                            0.44***                                                                                       0.17**     0.19**
                                                            (0.06)                                                                                        (0.09)     (0.09)
Firm Age                                                              -0.01***                                                                             0.00       0.00
                                                                       (0.00)                                                                             (0.00)     (0.00)
Average Age of Directors                                                         -0.02***                                                                -0.02***   -0.02***
                                                                                  (0.00)                                                                  (0.00)     (0.00)
Average productivity growth (2025)                                                           0.01                                                          0.01*
                                                                                            (0.00)                                                        (0.00)
Expected productivity growth (2025)                                                                  0.02***                                               0.01*
                                                                                                     (0.01)                                               (0.01)
Average real sales growth (2025)                                                                                 0.00                                                 0.00
                                                                                                                (0.00)                                               (0.00)
Expected real sales growth (2025)                                                                                           0.01                                      -0.00
                                                                                                                           (0.01)                                    (0.01)
Average employment growth (2025)                                                                                                     -0.00                          -0.01***
                                                                                                                                     (0.00)                         (0.00)
Expected employment growth (2025)                                                                                                               0.00                 -0.00
                                                                                                                                               (0.01)               (0.01)
Mean of Dependent Variable              1.4        1.4       1.4        1.4        1.4       1.4       1.4       1.4        1.4       1.4       1.4        1.4        1.4
SIC2 industry and time fixed effects    No         No        No         No         No        No        No        No         No        No         No        Yes        Yes
Notes: The dependent variable is the number of AI technologies currently being by firms. The data from the UK Decision Maker Panel was collected over February-April
2025 and November 2025 – January 2026, with the latest firm observation used in the regressions (N=2,793). A constant has also been estimated, but not reported in the
table. Where data are missing for a particular variable a dummy variable is included to account for that (results not reported). Standard errors are clustered at the firm level,
stars indicate *** p<0.01, ** p<0.05, * p<0.1.
Table A2 Determinants of frequency of AI use by survey respondent (UK Firms)
                                           (1)       (2)        (3)       (4)        (5)         (6)      (7)        (8)       (9)     (10)     (11)      (12)       (13)
   Dependent Variable:                                                                        Average Weekly AI Use (hours)
   Labor productivity (logs)               0.07                                                                                                            -0.02      -0.01
                                          (0.05)                                                                                                          (0.08)     (0.08)
   Employment (logs)                               -0.10***                                                                                                0.01       0.01
                                                    (0.02)                                                                                                (0.03)     (0.03)
   Average Wage per Employee (logs)                           0.22***                                                                                      0.18       0.19
                                                              (0.07)                                                                                      (0.12)     (0.12)
   Firm Age                                                             -0.02***                                                                           0.00       0.00
                                                                         (0.00)                                                                           (0.00)     (0.00)
   Average Age of Directors                                                        -0.04***                                                              -0.03***   -0.03***
                                                                                    (0.01)                                                                (0.01)     (0.01)
   Average productivity growth (2025)                                                           0.00                                                       0.00
                                                                                               (0.00)                                                     (0.00)
   Expected productivity growth (2025)                                                                   0.02**                                            0.02*
                                                                                                         (0.01)                                           (0.01)
   Average real sales growth (2025)                                                                                 -0.00                                            -0.00
                                                                                                                   (0.00)                                           (0.00)
   Expected real sales growth (2025)                                                                                          0.02**                                 0.01
                                                                                                                              (0.01)                                (0.01)
   Average employment growth (2025)                                                                                                     -0.01                        -0.01
                                                                                                                                       (0.00)                       (0.00)
   Expected employment growth (2025)                                                                                                             0.01                -0.01
                                                                                                                                                (0.01)              (0.01)
   Mean of Dependent Variable              1.4       1.4       1.4        1.4        1.4         1.4       1.4      1.4        1.4      1.4      1.4      1.4         1.4
   SIC2 industry and time fixed effects    No        No        No         No         No          No        No       No         No       No        No      Yes         Yes

 Notes: The data from the UK Decision Maker Panel was collected over February-March 2025 and November 2025 – January 2026, with the latest firm observation used
 in the regressions (N=2,642). A constant has also been estimated, but not reported in the table. Where data are missing for a particular variable a dummy variable is
 included to account for that (results not reported). Standard errors are clustered at the firm level, stars indicate *** p<0.01, ** p<0.05, * p<0.1.
Figure B1 Screenshots of AI survey questions in SBU
Figure B1 Screenshots of AI survey questions in SBU (continued)
Figure B2 Screenshots of AI survey questions in DMP
Figure B2 Screenshots of AI survey questions in DMP (continued)
Figure B3 Screenshots of AI survey questions in BOP-F
Figure B3 Screenshots of AI survey questions in BOP-F (continued)
Figure B3 Screenshots of AI survey questions in BOP-F (continued)
Figure B3 Screenshots of AI survey questions in BOP-F (continued)
Figure B4 Screenshots of AI survey questions in BOSS
Figure B4 Screenshots of AI survey questions in BOSS (continued)
Figure B4 Screenshots of AI survey questions in BOSS (continued)
Figure B4 Screenshots of AI survey questions in BOSS (continued)
Figure B5 Screenshots of AI survey questions in SWAA
Figure B5 Screenshots of AI survey questions in SWAA (continued)
Figure B5 Screenshots of AI survey questions in SWAA (continued)
Figure B6 Executives are Recruited by Phone and Then Moved to
an Online Panel

                                       Random sampling from
                                       population of firms with 10+
                                       employees (median ≈100)
