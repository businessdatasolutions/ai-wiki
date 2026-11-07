---
title: "Large Language Models, Small Labor Market Effects"
authors: ["Anders Humlum", "Emilie Vestergaard"]
publisher: "Becker Friedman Institute for Economics at the University of Chicago (BFI Working Paper 2025-56); also NBER Working Paper 33777 (first version)"
date_published: 2025-05-09
url: "https://bfi.uchicago.edu/wp-content/uploads/2025/04/BFI_WP_2025-56-3.pdf"
nber_url: "https://www.nber.org/papers/w33777"
doi: "10.3386/w33777"
attachment: 2025-05-09-humlum-vestergaard-large-language-models-small-labor-market-effects.pdf
version: "First version, dated May 9, 2025 (BFI cover: May 2025). Superseded by NBER revisions of October 2025 and March 2026 (retitled)."
fulltext_source: pdf-converted
converter: pdftotext -layout
notes: |
  Fetched 2026-11-07 from the BFI URL above, the link given by the Dutch research report
  "Nieuwe onderzoeken naar AI volwassenheid". 117-page PDF (BFI cover page + paper; created 2025-05-13).
  The upload folder in the URL says 2025/04; the paper itself is dated May 9, 2025 (PDF p. 2), matching
  the first NBER version (w33777.rev0, 2025-05-09, same abstract). Complete (ends with the Danish
  questionnaire). Printed page = PDF page - 2 in the body.
  This version says "precise zeros", confidence intervals "ruling out effects larger than 1%", with
  registers through June 2024 ("one and a half years after ChatGPT", PDF p. 5). The wording
  "precise null effects ... two years after" belongs to the later NBER versions.
---

WORKING PAPER · NO. 2025-56

Large Language Models, Small Labor Market
Effects
Anders Humlum and Emilie Vestergaard
MAY 2025




                                       5757 S. University Ave.
                                           Chicago, IL 60637
                                          Main: 773.702.5599
                                            bfi.uchicago.edu
 Large Language Models, Small Labor Market Effects∗

                        Anders Humlum†                Emilie Vestergaard‡

                                           May 9, 2025



                                            Abstract

       We examine the labor market effects of AI chatbots using two large-scale adoption
       surveys (late 2023 and 2024) covering 11 exposed occupations (25,000 workers, 7,000
       workplaces), linked to matched employer-employee data in Denmark. AI chatbots
       are now widespread—most employers encourage their use, many deploy in-house
       models, and training initiatives are common. These firm-led investments boost
       adoption, narrow demographic gaps in take-up, enhance workplace utility, and
       create new job tasks. Yet, despite substantial investments, economic impacts remain
       minimal. Using difference-in-differences and employer policies as quasi-experimental
       variation, we estimate precise zeros: AI chatbots have had no significant impact
       on earnings or recorded hours in any occupation, with confidence intervals ruling
       out effects larger than 1%. Modest productivity gains (average time savings of 3%),
       combined with weak wage pass-through, help explain these limited labor market
       effects. Our findings challenge narratives of imminent labor market transformation
       due to Generative AI.

       JEL Codes: J23, J24, J31, O33




   ∗
     We thank David Autor, Marianne Bertrand, Jacob Conway, Matthew Notowidigdo, Chad Syverson,
and seminar participants at the Becker Friedman Institute, Chicago Booth, INSEAD, Microsoft Research,
and MIT Sloan for helpful comments and suggestions. This project received financial support from the
Center for Applied Artificial Intelligence and the Polsky Center for Entrepreneurship and Innovation.
Caspar Ringhof provided excellent research assistance.
   †
     University of Chicago, Booth School of Business, anders.humlum@chicagobooth.edu
   ‡
     University of Copenhagen, Department of Economics, emilievestergaard@econ.ku.dk
       The emergence of AI chatbots marks the rise of Generative Artificial Intelligence (AI).

By some measures, these technologies are already living up to the immense hype: AI

chatbots have seen the fastest worker take-up of any new technology (Bick, Blandin and

Deming, 2025; Humlum and Vestergaard, 2025), randomized controlled trials (RCTs)

demonstrate substantial productivity gains for users (Brynjolfsson, Li and Raymond, 2025;

Noy and Zhang, 2023), and case studies indicate notable effects on online labor market

platforms (Teutloff et al., 2025). These effects on productivity and labor demand are

remarkable in both magnitude—ranging from 15% to 50%—and speed, materializing

within a few months.

       However, the broader labor market implications of Generative AI remain unclear

for at least three reasons. First, while workers have embraced AI chatbots for their

low costs and ease of use, we lack evidence on whether firms are making meaningful

investments in integrating these tools into workplace processes (Bonney et al., 2024).

Second, RCTs show that the effects of AI chatbots can turn negative if applied to the wrong

tasks (Dell’Acqua et al., 2023; Otis et al., 2024b), raising caution in extrapolating effects

from controlled settings to the broader economy. Third, while studies have documented

effects on productivity, it remains unclear how these translate into earnings and hours, as

high-quality microdata on such outcomes is rarely available.

       This paper addresses these gaps by conducting two large-scale surveys on AI chatbot

adoption and linking the responses to matched employer-employee data in Denmark. Our

dataset includes two survey rounds (late 2023 and 2024), each covering about 25,000

workers from 7,000 workplaces across 11 occupations exposed to AI chatbots, linked to

monthly administrative panel data on earnings, hours, and occupations.1 Our analysis

proceeds in four parts.
   1
     Our list of occupations is accountants, customer support specialists, financial advisors, HR profession-
als, IT support specialists, journalists, legal professionals, marketing professionals, office clerks, software
developers, and teachers.



                                                      1
   First, we examine how firm-led investments in AI chatbots influence workers’ take-up

of the tools. Employers are now heavily invested in AI chatbots: most encourage their

use, 38% deploy in-house models, and 30% of employees have received training.

   These initiatives greatly boost adoption, nearly doubling take-up rates for the typical

worker from 47% to 83%. The relative importance of employer encouragement becomes

even more pronounced for more intensive usage. Notably, these efforts narrow demographic

disparities in take-up: the gender gap in chatbot adoption shrinks from 11.9 to 5 percentage

points when firms actively encourage use, with training initiatives proving particularly

effective.

   Second, we investigate how chatbot adoption affects work processes. While AI chatbots

save time across all exposed occupations (for 64%–90% of users), their impact on work

quality and job satisfaction varies. Notably, AI chatbots have created new job tasks for

8.4% of workers, including some who do not use the tools themselves. We examine how

AI chatbots are reshaping work by analyzing workers’ free-text descriptions of their new

tasks. The role of task creation in shaping the impact of AI chatbots on work aligns with

existing theories on how automation technologies reinstate labor demand (Acemoglu and

Restrepo, 2019; Autor et al., 2024).

   Importantly, the benefits from AI chatbots—time savings, quality improvements,

creativity, task expansion, and job satisfaction—are 10%-40% greater when employers

encourage their usage. This underscores the importance of firm-led complementary

investments in unlocking the productivity potential of new technologies (Brynjolfsson,

Rock and Syverson, 2021; David, 1990).

   However, despite substantial investments in AI chatbots, their overall impact on work

remains modest: users report average time savings of 2.8% of work hours. This contrasts

with the significant productivity gains—often exceeding 15%—documented by RCTs in

our study occupations (Brynjolfsson, Li and Raymond, 2025; Noy and Zhang, 2023; Peng


                                             2
et al., 2023). Two key factors help explain this discrepancy. First, effect heterogeneity:

while existing RCTs concentrate on occupations with the largest productivity gains from

AI chatbots, our broader survey reveals that several exposed occupations see more modest

gains. Second, the lack of firm-based complementary investments: many real-world workers

do not operate under the same favorable conditions as those in experimental settings,

limiting realized productivity gains. These findings caution against directly extrapolating

productivity gains from controlled experiments to the broader economy.

   In the third part of the paper, we examine the effects of AI chatbots on labor market

outcomes. We link our survey data to administrative records on monthly earnings, hours,

and occupations through June 2024—one and a half years after ChatGPT’s launch. Using

a difference-in-differences framework, we compare adopters and non-adopters before and

after the arrival of AI chatbots and leverage employer policies to isolate quasi-exogenous

variation in adoption.

   Our main finding is that AI chatbots have had minimal impact on adopters’ economic

outcomes. Difference-in-differences estimates for earnings, hours, and wages are all

precisely estimated zeros, with confidence intervals ruling out average effects larger than

1%. At the occupation level, estimates are similarly close to zero, generally excluding

changes greater than 6%. These limited impacts persist in our quasi-experimental analysis

based on employer policies, suggesting that the average causal effect is indeed negligible. A

direct survey question—“Have AI chatbots affected your labor earnings?”—confirms that

workers overwhelmingly report no impact on earnings as of November 2024. Moreover,

difference-in-differences estimates show no differential trends over time and are not larger

among adopters whose use is encouraged by employers, indicating that the limited impacts

are not merely a very short-term phenomenon.

   While reported time savings from AI chatbots are modest, we have statistical power to

rule out comparable earnings effects. Specifically, we estimate that only 3–7% of workers’


                                             3
productivity gains are passed through to higher earnings, with greater elasticity at firms

that encourage chatbot use. These pass-through estimates align with, but fall at the

lower end of, existing estimates (Card et al., 2018). In summary, the limited impacts of

AI chatbots on workers’ earnings reflect a combination of modest productivity gains and

weak pass-through to wages, although employer policies can enhance both.

    As a final analysis, we examine whether AI chatbots have affected broader workplace

outcomes, potentially influencing even non-adopting workers. Comparing workplaces with

high versus low rates of chatbot usage, we find no evidence that firms with greater adoption

have experienced differential changes in total employment, wage bills, or retention of

incumbent workers. Direct survey responses from non-users confirm that they perceive no

chatbot-related changes in earnings.

    Overall, our findings challenge narratives of imminent labor market transformations

due to Generative AI. While adoption has been rapid, with firms now heavily invested in

unlocking the technological potential, the economic impacts remain small.


1     Data and Institutional Setting

Denmark offers an ideal setting for examining the labor market impacts of Generative AI.

    First, Danish workers have been at the forefront of Generative AI adoption, with

take-up rates comparable to those in the United States (Bick, Blandin and Deming, 2025;

Humlum and Vestergaard, 2025; RISJ, 2024).

    Second, Denmark’s labor market is highly flexible, with low hiring and firing costs

and decentralized wage bargaining—similar to that of the U.S.—which allows firms and

workers to adjust hours and earnings in response to technological change (Botero et al.,

2004; Dahl, Le Maire and Munch, 2013). In particular, most workers in our sample engage

in annual negotiations with their employers, providing regular opportunities to adjust

earnings and hours in response to AI chatbot adoption during the study period.

                                             4
   Third, Denmark has exceptional infrastructure for tracking the adoption of new

technologies. In particular, every Dane has a digital mailbox that Statistics Denmark can

use to distribute survey invitations. We use this infrastructure to conduct two large-scale,

representative surveys on AI chatbot adoption, which we detail below.

   Finally, our partnership with Statistics Denmark allows us to link these surveys to

matched employer-employee data, providing a unique opportunity to analyze labor market

effects such as changes in earnings, working hours, and job mobility.

   Taken together, these factors make Denmark a prime setting for observing early

labor market effects of Generative AI, with insights that may extend to other advanced

economies—including the US—and an unparalleled data infrastructure to assess these

impacts rigorously.


1.1    Data Sources

This paper builds on two large-scale surveys on AI chatbot adoption, conducted in

November–December of 2023 and 2024. The first survey provided the dataset for Humlum

and Vestergaard (2025), which documented adoption patterns of ChatGPT, the dominant

AI chatbot. This paper extends that dataset in two key ways. First, we link survey

responses to administrative labor market data after the introduction of ChatGPT, enabling

us to assess impacts on earnings, work hours, and job mobility. Second, we introduce

a second survey round in 2024 that (i) broadens the scope to include all AI chatbots,

including in-house models, (ii) provides extensive data on firm-led adoption initiatives,

and (iii) offers deeper insights into workers’ actual usage and perceived benefits of these

tools. Section 1.3 outlines the 2024 survey, which is the primary focus of this paper.




                                             5
1.2    Occupations

Our surveys focus on 11 occupations that are exposed to AI chatbots: accountants,

customer support specialists, financial advisors, HR professionals, IT support specialists,

journalists, legal professionals, marketing professionals, office clerks, software developers,

and teachers. These occupations were selected based on three criteria: (i) they have

at least one O*NET job task where AI chatbots can save time, as measured by the

“Direct Exposure (E1)” metric from Eloundou et al. (2024); (ii) they are captured by a

well-defined set of ISCO codes; and (iii) they contain a sufficient number of workers for

statistical analysis. Humlum and Vestergaard (2025) details the selection and empirical

measurement of these occupations.


1.3    Survey Outline

Our 2024 survey is organized into the four blocks summarized below. The 2023 round

followed a similar structure. The full questionnaires are in Appendix J.


Block 1: Occupation and tasks. Workers first select their occupation and report the

importance of six representative tasks in their occupations.


Block 2: Adoption. Workers report their experiences with various AI chatbots,

including the domains, frequency, and duration of usage.


Block 3: Employer initiatives. Workers are asked about any employer initiatives

related to AI chatbots, including usage policies, in-house chatbots, and employee training.


Block 4: Impact on work. Workers are asked about their experienced benefits and

estimated effects of AI chatbots.




                                              6
1.4    Register Data

We use several administrative registers at Statistics Denmark. Our matched employer-

employee data come from the E-Income Register, which records earnings, hours, occupation,

and industry for all job spells in Denmark on a monthly basis from 2008 onward. This

register is compiled by the Danish tax authorities and subsequently harmonized by

Statistics Denmark into the Employment Statistics of Employees (BFL) dataset. We

complement this with demographics data on individuals from the Population Register

(BEF), and wealth information for the Personal Wealth Register (FORMPERS). Finally,

we draw firm-level data (e.g., annual revenue and employment) from the Firm Statistics

(FIRM) Register. Because our survey was sent to workers identified in the register data

by their (deidentified) social security numbers (pnr), all respondents can be matched to

the register data.


1.5    Survey Sample

We invited 115,000 workers to participate in each of our survey rounds in 2023 and 2024.

The registers at Statistics Denmark enabled us to target these invitations by occupation

and workplace. In particular, for each of our 11 occupations, we conducted a workplace-

based sampling procedure, first drawing a random set of workplaces within the occupations

and then sampling all relevant workers for these workplaces. This sampling procedure

maximizes the statistical power of the workplace-level analyses whilst keeping our sample

representative. Appendix A.1 details the sampling protocol. We sent three reminders per

survey round, two by e-mail and one by text. The invitation letters are in Appendix I.

We received about 25,000 valid and complete responses to each of the survey. Appendix

A.2 details our survey response rates. While our main analysis focuses on responses from

the 2024 round, we use the 2023 round to examine the dynamics of our estimated effects.




                                           7
1.5.1       Representativeness and Response Quality

Appendix A.2.1 conducts several checks on the representativeness and quality of our

survey responses. These analyses extend the checks in Humlum and Vestergaard (2025) to

the 2024 survey round. First, we ensure that our sample represents the population based

on observables, including age, gender, experience, earnings, and wealth. Second, following

Dutz et al. (2025), we use randomized participation incentives to show that our findings

are also balanced on workers’ latent willingness to participate in the survey. Finally, we

cross-check that the survey responses align with variables that are also recorded in the

administrative registers.


2         Adoption
2.1        Employer Initiatives

Figure 1, Panel (a) shows the prevalence of employer policies related to AI chatbot

usage across our 11 occupations. Firms are now heavily invested in AI chatbots: about

43% of workers are explicitly encouraged to use them, another 21% are allowed, while

only about 6% are explicitly prohibited from doing so. This marks a shift from early

responses to ChatGPT, when many employers restricted its use due to concerns over data

confidentiality and output accuracy (Humlum and Vestergaard, 2025).2

        Employers’ encouragement is supported by substantial investments in tools and training.

Panel (b) shows that 38% of firms have their own AI chatbots—most often customized

versions—and Panel (c) shows that 30% of employees have participated in training courses

on AI chatbot usage, with most of these courses organized by their employer.3 Notably,
    2
      Although outright bans are now rare, they persist in some occupations that involve sensitive data
(e.g., financial advisors) or require high factual accuracy (e.g., legal professionals).
    3
      Customized chatbots are typically versions of ChatGPT, tailored for workplace use through adjust-
ments such as compliance with data security, training on internal data, and custom prompt creation.
Often, these are thin wrappers around ChatGPT Enterprise or the OpenAI API. Appendix B.2.1 details
the usage of AI chatbot products, showing that ChatGPT remains the dominant player. It also provides
additional information on the characteristics of in-house chatbots.


                                                  8
these firm-wide investments are prevalent in all 11 occupations but are particularly

widespread in journalism and marketing and more limited in teaching. The widespread

investments in AI chatbots at the workplace are consistent with their potential as a

general-purpose technology (Eloundou et al., 2024).

       Which firms have adopted different AI chatbot initiatives? Table 1 shows that firms

encouraging AI chatbot use tend to be slightly younger (each additional 10 years of age

is associated with a 1.4 percentage point decrease in encouragement), more productive

(a doubling of productivity corresponds to a 4.7 percentage point increase), and more

likely to be privately owned (associated with a 4.1 percentage point increase), but not

systematically larger than others.4,5 Overall, however, chatbot initiatives are largely

unrelated to observable firm characteristics, which account for just 1.3% of the within-

occupation variation in encouragement—far less than the 10.6% explained by our 11

occupation categories alone. In other words, many otherwise comparable firms have

adopted markedly different strategies toward AI chatbots, even for similar workers within

the same occupation. We examine the implications of these divergent approaches in the

sections that follow.

2.1.1      Employer Initiatives and Worker Outcomes

Throughout the paper, we explore how the employer initiatives for AI chatbots relate to

workers’ adoption and benefits from the tools. This analysis is motivated by the literature

on “Productivity J-Curves,” which emphasizes that complementary organizational invest-

ments may be critical for realizing the gains from new technologies (Brynjolfsson and
   4
     Appendix Table B.1 shows that these correlations with firms’ characteristics are robust to controlling
for worker characteristics.
   5
     Younger and more productive firms are commonly found to adopt new technologies faster; see, e.g.,
Acemoglu et al. (2022), who document adoption patterns for a range of advanced technologies in 2019,
including AI and robotics. One difference stands out: while larger firms are typically found to adopt new
technologies faster, this pattern does not hold for AI chatbots, whose employer encouragement appears
unrelated to firm size. This may reflect the low fixed costs associated with AI chatbots—many of which
are free and relatively easy to start using. As shown in Column (7) of Table 1, however, larger firms are
more likely to have their own AI chatbot.


                                                    9
Hitt, 2000; Brynjolfsson, Rock and Syverson, 2021). Moreover, because early adoption of

AI chatbots was largely worker-driven, this analysis sheds light on the extent to which

employers can move the needle and influence outcomes by also investing in the technology.

       Specifically, we compare workers in the same occupations with similar characteristics

and estimate how their adoption behaviors and reported benefits vary with employer

initiatives for AI chatbots:


                           Yi = γ ′ Xi + β × EmployerInitiativei + εi ,                        (1)


where Yi is a chatbot-related outcome for worker i, such as use or reported benefits of

AI chatbots for work; Xi is a vector of worker pre-determined characteristics, including

age, gender, experience, and occupation fixed effects;6 and EmployerInitiativei captures

employer-driven initiatives, such as encouraging employees to use AI chatbots. Appendix H

presents a simple Roy-style model of chatbot adoption to help interpret the estimates in

Equation (1). We draw on this framework in the discussions that follow.

       Although employer initiatives are not assigned through a randomized design, our rich

data on firms and workers allow us to examine the robustness of our findings to several

potential confounders. Appendix F.1 presents these robustness checks. First, we show that

all results hold when controlling for firm characteristics (Table 1), ensuring that differences

across encouraged workplaces are not driven by variation in firm age, size, or productivity.

Second, we show that the results are robust to controlling for workers’ detailed task mixes

within occupations, demonstrating that the effects of employer encouragement are not

driven by differences in the types of tasks more amenable to AI chatbot use.7 Together,

these robustness checks help rule out confounding from observable factors and support

the validity of our findings.
   6
    All worker characteristics are measured in 2022, before AI chatbots became available.
   7
    We do not include task controls in our main specification, as task mix may itself be endogenous
to chatbot adoption. Indeed, Section 3.2 shows that AI chatbots have created new job tasks for many
workers.


                                                10
   Finally, although our main analysis relies on workers’ self-reports of employer initiatives,

Appendix F.2 shows that the findings also hold when instead using coworker reports to

measure employer initiatives. This robustness supports our interpretation of employer

initiatives as workplace-level treatments.


2.2    Worker Adoption

Figure 2 shows how AI chatbot adoption varies with employer encouragement for a

typical worker. The Non-Encouraged estimates highlight the bottom-up nature of chatbot

adoption: even without employer encouragement, 47% of workers have used AI chatbots

for work, and 8% use them daily. Despite this high baseline, the Encouraged estimates

show that employer encouragement significantly boosts adoption, nearly doubling take-up

rates to 83% for a typical worker. The relative impacts are even more pronounced for

intensive use, with daily adoption rising to 21% when employers actively promote chatbot

use.

   Do employer initiatives influence which workers use AI chatbots? Figure 3 examines

differences in adoption across demographic groups within occupations, estimated separately

for settings with and without employer encouragement. The Non-Encouraged estimates

reveal substantial adoption gaps across worker groups. For example, in workplaces without

employer encouragement, women are about 12 percentage points less likely to have used

AI chatbots than comparable men in the same occupation. Younger, less experienced,

and higher-earning workers are also more likely to have adopted the tools.

   Importantly, the demographic gaps in adoption are markedly smaller in workplaces

where employers actively encourage chatbot use. In particular, the gender gap narrows

from 12 to 5 percentage points in encouraged settings. Similarly, the age gap shrinks by

approximately 40% when employers promote adoption. In contrast, the reduction in gaps

is smaller among more experienced workers, suggesting that established work habits may


                                             11
be more resistant to change—even when encouraged by employers.

       Figures B.2–B.3 examine how other types of employer initiatives are associated with

AI chatbot adoption, yielding two key insights.

       First, firm-provided training programs are particularly effective, boosting overall

adoption and reducing the gender gap in uptake to 3.6 percentage points.8 The effectiveness

of training aligns with findings from the 2023 survey round, in which women were

significantly more likely to cite lack of training as a barrier to ChatGPT adoption

(Humlum and Vestergaard, 2025).

       Second, the gender gap in chatbot adoption persists even in workplaces where the

tools are prohibited. Although employer bans are associated with a reduction in overall

adoption to roughly one-third of the baseline rate, about 80% of the baseline gender gap

remains. This pattern mirrors findings by Carvajal, Franco and Isaksson (2024), who

document a similar gender gap in ChatGPT use among Norwegian bachelor’s students and

show, using a vignette experiment, that the gap largely reflects male students continuing

to use the tools even when explicitly banned.


2.3       Comparison to the Literature

The widespread adoption of AI chatbots—and the substantial demographic gaps in

usage—are now well documented in the literature. For example, our 2023 survey found

that 39.8% of workers had used ChatGPT for work, with adoption rates 15.9 percentage

points lower among women within occupations (Humlum and Vestergaard, 2025). Higher

adoption rates among younger, less experienced, and higher-earning workers also replicate

the patterns observed in our earlier round.9 Bick, Blandin and Deming (2025) report
   8
      Figure B.3 shows that while training consistently reduces disparities across all usage intensi-
ties—including daily use—employer encouragement alone may widen the gender gap in frequent chatbot
usage.
    9
      For comparison, in our 2024 survey round, ChatGPT adoption rose to 49.1%, with a gender gap of
12.3 percentage points (see Appendix B.2.2 for a comparison of the 2023 and 2024 adoption patterns).




                                                 12
similar adoption patterns among U.S. workers, and Otis et al. (2024a) show that gender

gaps in Generative AI adoption are pervasive across contexts.

    We contribute to this evidence by documenting that employer-driven initiatives to

support AI chatbot adoption are now common and play an important role in shaping

overall adoption rates and demographic disparities in usage.10

    By contrast, earlier surveys found relatively low take-up rates of AI at the firm level.

For example, Bonney et al. (2024) document that as of February 2024, only 5.4% of U.S.

firms reported using AI, with adoption in the leading sector (Information) still below 20%.

    Our survey provides the first comprehensive evidence on how employers are integrating

Generative AI into the workplace. We find that employer initiatives—especially those

focused on training—substantially increase adoption and help narrow demographic gaps

in take-up. This finding aligns with Dillon et al. (2025), who document that firm effects

are a primary driver of workers’ take-up of a randomized offer for Microsoft Copilot.

    More broadly, the importance of employer initiatives for AI chatbot adoption echoes

an extensive literature on the diffusion of general-purpose technologies, which stresses

the need for complementary investments and coinvention (Bresnahan and Greenstein,

1996; David, 1990; Feigenbaum and Gross, 2024). In the sections that follow, we examine

how employer investments in AI chatbots shape the tools’ effects on work processes and

labor-market outcomes.
  10
     For instance, the rise of employer initiatives may explain much of the shift observed between the
2023 and 2024 surveys—namely, increased adoption and a narrowed gender gap—as most initiatives
were implemented in the interim. One of the first in-house AI chatbots, DanskeGPT, was launched by
Denmark’s largest bank in March 2024 (Danske Bank, 2024).




                                                 13
3        Work
3.1       Benefits for Users

What benefits do users report from AI chatbots? Figure 4 shows that workers primarily

cite time savings in completing job tasks (Panel (a)), with an average of 25 minutes saved

per day of use (Panel (b)). Additionally, nearly half of users report improvements in

work quality and enhanced creativity from using AI chatbots. In contrast, increased job

satisfaction is the least commonly reported benefit.11

       Table C.1 breaks down these benefits by occupation, revealing significant variation.

For instance, marketing professionals are more than twice as likely as teachers to report

that chatbots improve work quality (69.8% vs. 32.1%), while software developers are

more than twice as likely as journalists to report increased job satisfaction from chatbot

use (30.5% vs. 12.6%). Despite these differences, AI chatbots help save time across all

exposed occupations, with time savings reported by 64%–90% of users.

       Importantly, the benefits from AI chatbots—time savings, quality improvements,

creativity, task expansion, and job satisfaction—are all 10%-40% greater when employers

encourage their usage. This highlights the importance of firm-based complementary

investment for unlocking the work-related benefits of new technologies (Brynjolfsson and

Hitt, 2000).

       Appendix H presents a simple Roy model of chatbot adoption to interpret the differences

between encouraged and non-encouraged users in Figure 4. The model shows that employer

encouragement affects the average benefits reported by users through two distinct forces:

a direct, individual-level effect of encouragement, and a selection effect arising from

broader adoption. The selection effect tends to be more negative when users are more

positively selected on their potential benefits and when employer encouragement primarily
  11
    Toner-Rodgers (2024) shows that other generative models—specifically those that generate materials
designs rather than text—have profound impacts on the scientific discovery process for materials scientists,
significantly enhancing their innovative capacity but also reducing their job satisfaction.


                                                    14
reduces adoption costs rather than increases user benefits. In this light, the consistently

greater reported benefits in workplaces that encourage chatbot use, as shown in Figure 4,

are especially noteworthy. They suggest that employer-led initiatives primarily work by

enhancing the benefits of the tools—consistent with “Productivity J-curves”—and that

these effects are large relative to any selection on worker-level gains from AI chatbot use.12

    What is the economic significance of the reported benefits of AI chatbots? In Table 2,

we combine workers’ frequency of use (from Figure 2) with their reported time savings per

day of usage (from Figure 4.(b)) to estimate time savings as a percent of total work hours.

Average time savings from AI chatbots vary from 6.8% among marketing professionals

whose employers encourage their use to 0.6% among teachers in schools that do not

encourage their use. The larger time savings for encouraged workers reflect both that they

use the AI chatbots more often and report greater time savings per day of use. Across

our 11 occupations and employer policies, the average time savings amount to 2.8% of the

total work hours of users.

    How do workers allocate the time savings from AI chatbots? Figure 4.(c) shows that

the vast majority (80%) reallocate this time to other job tasks, while fewer than 10% use

it for additional breaks or leisure. In addition, 25% spend more time on the same tasks

they initially saved time on, especially when employers actively encourage chatbot use.

This pattern suggests that firm-led initiatives play an important role in enabling workers

to expand task outputs in response to the task-specific productivity gains from chatbots.
  12
     Disentangling the individual-level causal effects from the selection effects would require additional
assumptions (e.g., on the functional form of the adoption model à la Heckman (1979)) or alternative
sources of variation (e.g., an instrument that shifts adoption costs without affecting perceived benefits).
We do not attempt to separate these effects, as we view the bundled impact of employer encouragement
as informative in itself—highlighting the average benefits of AI chatbots that may arise when employers
actively invest in unlocking the tools’ potential.




                                                   15
3.2       Workloads and Task Creation

Figure 5 examines how AI chatbots influence workloads. Notably, AI chatbots have

created new workloads for 17% of users (Panel (a)), with 4.4 percentage points performing

more of the same tasks, 10.9 percentage points taking on new tasks, and 1.7 percentage

points doing both. Importantly, new workloads are 20-50% more pronounced in workplaces

that encourage the use. This highlights the importance of firm-led initiatives for realizing

workplace transformations from new technologies.

       To further understand how AI chatbots affect the nature of work, we asked respondents

to describe the new job tasks they perform as a result of AI chatbots. In Appendix C.2,

we categorize the free-text responses into common new tasks associated with AI chatbots

in each occupation. AI chatbots have generated new job tasks for workers across all 11

occupations, with 50% to 95% of these directly linked to AI use.

       Figure 6 breaks down the composition of AI-related job tasks by occupation. The most

common task relates to the integration of AI chatbots into the workplace, accounting for

15%–40% of all new tasks, with the highest shares observed in IT support and software

development.13 This pattern highlights that we are currently in a phase where substantial

resources are being devoted to adapting workflows to AI chatbots. It is consistent with

firms being in the trough of a productivity J-curve (Brynjolfsson, Rock and Syverson,

2021) and helps contextualize the modest time savings we observe in Table 2.

       The second most common task involves using AI for content drafting, which appears

across most occupations. AI ethics and compliance issues are especially prominent in

teaching—where educators increasingly need to detect AI-generated homework—and in

the legal profession, where practitioners are formulating guidelines for chatbot use. Tasks
  13
     AI Integration refers to embedding AI chatbots into workflows to automate or enhance tasks. For
example, software developers report “fine-tuning AI coding assistants by providing feedback and project-
specific examples,” legal professionals describe “developing organizational AI usage policies and guidelines,”
and teachers mention “adapting exams and assignments to account for AI tool usage.” See Appendix C.2
for additional examples.



                                                     16
involving idea generation and data insights are present in all occupations but are less

central, typically comprising 5%–20% of new tasks.14

       Consistent with the finding that workloads from AI chatbots extend beyond tasks

directly related to using them, Figure 5.(b) shows that 5% of non-users report new

workloads stemming from AI chatbots. Specifically, Figure C.1.(b) shows that about

10%–15% of teachers who have not used AI chatbots report new workloads from the

technology. In general, these new workloads for non-users consist almost entirely of novel

tasks, with effects more pronounced in workplaces that encourage AI chatbot use.

       Taken together, the widespread creation of new tasks, the spillovers to non-users,

and the stronger effects in workplaces that encourage the tools all highlight the broader

workplace transformations caused by AI chatbots.


3.3       Comparison to the Literature

The importance of employer initiatives for realizing the benefits of AI chatbots aligns with

the concept of “Productivity J-curves,” where firm-based complementary investments are

needed to unlock the potential of new technologies (Brynjolfsson, Rock and Syverson,

2021; David, 1990).

       The importance of task creation for the impact of AI chatbots on workloads supports

key theoretical predictions for how automation technologies may reinstate the demand

for labor in the production process (Acemoglu and Restrepo, 2019; Autor et al., 2024).

Notably, across all occupations, workplaces that encourage AI chatbot use experience

greater task creation from these tools. This further underscores the importance of firm-led

investments for driving workplace transformations from technological change (Brynjolfsson

and Hitt, 2000; Brynjolfsson, Rock and Syverson, 2021).
  14
    More broadly, we may classify the new job tasks into “core AI use” (AI Ideation, AI Content Drafting,
and AI Data Insights) and “implementation and oversight” (AI Quality Review, AI Integration, and AI
Ethics & Compliance). Using this taxonomy, on average, 41% of the new tasks are related to core AI use,
with the remaining 59% focused on enabling and managing the use of AI chatbots.


                                                  17
       That said, the average reported time savings of 2.8% for adopters may seem small

compared to the substantial productivity gains—often exceeding 15%—documented by

RCTs in our study occupations.15,16 How can we reconcile workers’ modest reported time

savings with the substantial effects observed in RCTs?

       First, our reported time savings are highest precisely in the occupations covered by

RCTs, such as customer and IT support (Brynjolfsson, Li and Raymond, 2025), marketing

and human resources (Noy and Zhang, 2023), and software development (Peng et al., 2023).

In contrast, reported savings are about half as large among teachers, accountants, and

financial advisors, whose tasks may be less suited to chatbot assistance. This occupational

heterogeneity supports the concept of a “jagged frontier” of AI chatbot costs and benefits

(Dell’Acqua et al., 2023), warranting caution against extrapolating productivity estimates

across tasks or occupations.

       Relatedly, while RCTs often focus on jobs where AI chatbots are continuously applicable,

the typical adopter in our data uses chatbots only every third to fourth day, diluting

their overall time savings accordingly. On days when they do use the tools, however,

average time savings still amount to just 6–7%, substantially below experimental estimates.

Limited applicability may again be an important explanation: even on usage days, adopters

spend only 5-6% of their work hours actively using AI chatbots (see Table B.2).17,18
  15
      Noy and Zhang (2023) report time savings of 37% from ChatGPT in text writing tasks representative
of marketing and HR professionals. Brynjolfsson, Li and Raymond (2025) estimate productivity effects of
15% from a GPT-based chat assistant among customer and IT support agents, with more pronounced
effects for less experienced workers. Cui et al. (2024) estimate a 26% productivity gain from GitHub
Copilot among software developers, while Peng et al. (2023) report a 58% increase.
   16
      Our estimated productivity gains are closer to those of Acemoglu (2025), though for different reasons.
While Acemoglu (2025) combines the experimental productivity estimates with a calibrated adoption
curve, we measure both adoption and (self-reported) time savings directly. Bick, Blandin and Deming
(2025) provide a thoughtful comparison between their survey-based estimates of productivity gains and
the predictions of Acemoglu (2025).
   17
      Our time use estimates align with, but fall at the lower end of, the range reported by Bick, Blandin
and Deming (2025).
   18
      The time use estimates should be interpreted with caution, as we might not expect a 100% active
utilization rate even in tasks where AI chatbots are directly applicable. For example, in the writing task
studied by Noy and Zhang (2023), treated workers spent on average 3 minutes before pasting in a large
block of text—presumably generated by ChatGPT. The workers then spend an additional 14 minutes
manually editing and refining the output. In our data, adopters spend an average of 2.2% of their total


                                                    18
    Second, reported time savings are significantly higher when employers actively en-

courage chatbot use. For example, marketers and software developers whose employers

promote AI chatbots report time savings of approximately 7%. In this sense, RCTs may

capture the productivity effects of a well-coordinated and carefully managed adoption of

these tools. While such estimates provide valuable insight into the workplace potential of

AI chatbots, our survey indicates that many users do not operate under similarly favorable

conditions. This highlights the need for caution when extrapolating productivity benefits

from controlled settings onto the broader economy.19

    Our time savings estimates align more closely with those of Bick, Blandin and Deming

(2025), who, in a nationally representative U.S. survey, find an average reported time

savings of 5.4% among users. However, their study does not split the time savings by

occupation or employer policies, limiting direct comparability to our estimates.20


4      Labor Market Outcomes

Our preceding analysis shows that AI chatbots are now widespread, with adopters

reporting time savings and other work-related benefits, especially in workplaces that

encourage their usage. Have these changes affected workers’ labor market outcomes, such

as earnings or recorded work hours? To answer this question, we link the survey responses
work hours using AI chatbots—less than the time savings they report. This pattern is also consistent
with Noy and Zhang (2023), where treated workers saved 10 minutes on average despite only 3 minutes
of initial tool use.
  19
     Another source of discrepancy between our time savings estimates and those from RCTs lies in the
parameter of interest: whereas experiments typically identify Average Treatment Effects (ATE) for the
study population, our estimates reflect self-reported time savings among users—closer to an Average
Treatment Effect on the Treated (ATT). However, if workers adopt chatbots based on their expected
individual benefits—such that users tend to derive greater gains than non-users—the modest time savings
reported in our survey appear even more stark when contrasted with the larger effects found in RCTs.
  20
     Edelman, Ngwe and Peng (2023) shows that self-reported time savings from AI chatbots—particularly
Microsoft Copilot—may overstate actual productivity gains. This further reinforces the point that workers’
productivity improvements from AI chatbots are modest, as our self-reported time savings estimates would
then represent an upper bound on realized benefits. That said, overstated gains may not be the full story:
Section 4.3 shows that workers’ self-reported earnings effects closely align with our difference-in-differences
estimates based on administrative data, reflecting that workers recognize that AI chatbots have not
materially improved their earnings.



                                                     19
to administrative data on labor market outcomes (see Section 1.4 for details). We first

outline our empirical strategy in Section 4.1 before presenting our results in the subsequent

sections.


4.1       Empirical Strategy

Our primary analysis employs a difference-in-differences specification, comparing the labor

market outcomes of adopters and non-adopters before and after the introduction of AI

chatbots. A key concern in this analysis is that adopters may have fared differently in the

labor market even without AI chatbots. We take three steps to address this issue.

      First, we control for workers’ pre-determined characteristics—including gender, age,

and labor market experience—to ensure these factors do not drive our estimates (e.g.,

adopters being younger and naturally on upward earnings trajectories).

      Second, we leverage our panel data to implement a difference-in-differences approach

indexed to November 2022, the release date of ChatGPT.21 This allows us to control for

time-invariant differences between workers (e.g., high-ability adopters who would have

earned more regardless) and examine whether adopters experienced differential changes

after this date. Additionally, we assess whether adopters were on distinct labor market

trends even before AI chatbots became available, enabling us to control for potential

pre-existing differences.

      Finally, to address unobserved confounding shocks (e.g., adopters facing sudden

setbacks or tailwinds in the labor market after November 2022), we leverage quasi-

exogenous variation from the employer policies documented in Section 2.1. Specifically,

we compare similar workers whose AI chatbot adoption differs due to employer-wide usage

policies. Section 4.2.1 presents the results from these quasi-experimental analyses, which

closely align with our main difference-in-differences estimates.
 21
      Appendix B.2.1 shows that ChatGPT remains the dominant AI chatbot to date.




                                                20
4.1.1   Regression Specifications

Let Yit denote a labor market outcome (e.g., earnings) for worker i in month-year t, let Xi

represent a vector of workers’ pre-determined characteristics (age, gender, experience, and

occupation FEs), and let Ai indicate whether the worker has adopted AI chatbots. Our

primary adoption measure is whether workers have used AI chatbots for work, but we also

examine the effects of more intensive adoption (e.g., daily usage) and early adoption (based

on responses to our 2023 survey round). We study impacts on log earnings, recorded

hours, and wages, and also consider effects on extensive-margin employment.


Dynamic Difference-in-Differences. To assess overall impacts, we employ a dynamic

difference-in-differences specification that compares the monthly outcomes of adopters

and non-adopters before and after the introduction of AI chatbots:

               X                          X                          X
     Yit =             λ1τ Xi 1{t=τ } +       λ2m 1{m=m(t)} +                  βτ Ai 1{t=τ } +β0 Ai + εit ,   (2)
                   τ                      m                     τ ̸=2022M 11
               |          {z      }       |       {z        }   |              {z           }
             Pre-Determined Controls          Seasonality           Dynamic Diff-in-Diffs


   where λ2m are month fixed effects that control for seasonality in labor market outcomes.

The parameters of interest, βτ , capture the differential changes in labor market outcomes

for adopters, indexed to November 2022, the release of ChatGPT. Motivated by the

greater work-related benefits when employers encourage AI chatbot use (Section 3), we

further split the difference-in-differences estimates by whether adopters are encouraged.

In both cases, we use all non-adopters as the comparison group and control for workers’

pre-determined characteristics and seasonality.


Pooled Difference-in-Differences. To examine heterogeneous impacts across multiple

dimensions, we use a pooled specification that compares the average outcomes of adopters




                                                       21
and non-adopters before and after the introduction of AI chatbots:

          X                          X
Yit =             λ1τ Xi 1{t=τ } +       λ2m 1{m=m(t)} + λ3 t + λ4 Ai t + βAi 1{t≥2022M 11} +β0 Ai + εit ,
              τ                      m
                                                            |       {z        }   |           {z            }
          |          {z      }       |       {z        }        Time Trends           Pooled Diff-in-Diff
        Pre-Determined Controls          Seasonality

                                                                                                                (3)

where we add adopter-specific time trends to ensure our pooled difference-in-differences

estimates are not driven by spurious trends in outcomes. The parameter of interest, β,

captures the average differential change in the labor market outcomes of adopters after

November 2022.


4.2      Results

Figure 7 examines the labor earnings of adopters relative to non-adopters, before and

after the introduction of AI chatbots.

   Panel (a) begins by presenting the difference in means. The estimates show that

adopters earn about 7% more than comparable non-adopters. Panel (b) splits adopters

based on whether their usage is employer-encouraged, showing that encouraged users

exhibit even larger earnings premia. However, leveraging the panel dimension of our

administrative data reveals that these earnings differentials entirely predate the arrival of

AI chatbots. When indexing differences to November 2022, the difference-in-differences

estimates in Panel (c) show no differential changes for adopters following the introduction

of AI chatbots. The estimates remain flat even among adopters whose employers actively

encourage chatbot use.

   The dynamic difference-in-differences in Figure 7.(c) reveal that adopters are on slightly

stronger labor market trends. However, because these trends entirely predate AI chatbots,

the pooled difference-in-differences in Figure 9.(a) (which control for pre-trends; see

Equation (3)) are precise zeros, with confidence bands ruling out effects larger than 1%.

   Figure 7 provides three key insights. First, one and a half years after their launch,


                                                       22
AI chatbots have had minimal average impact on adopters’ earnings. The confidence

intervals of our dynamic difference-in-differences estimates rule out changes larger than

2%, and our pooled difference-in-differences estimates rule out effects larger than 1%.

Second, these effects show no differential trends after the introduction of AI chatbots,

indicating that the minimal impacts are not merely a very short-term phenomenon.22

Lastly, despite evidence in Section 3 that employer encouragement boosts work-related

benefits of AI chatbots, we find no differential changes in earnings for adopters whose

employers encourage their use.

       While Figure 7 shows that adopters have not fared better in terms of earnings following

the introduction of AI chatbots, this pattern could mask offsetting effects on wages and

hours. Figure 8 examines this possibility by presenting separate estimates for workers’

hourly wages, intensive-margin hours, and extensive-margin employment. Once again,

we find no differential changes for adopters in any of these outcomes, even among those

encouraged to use the tools.

       Do the overall zero effects mask heterogeneous gains and losses across workers? To

investigate this, Figure 9.(a) first estimates the effects of AI chatbots on worker earnings

separately for each of the 11 occupations in our sample. Notably, we do not find significant

effects of AI chatbots in any occupation: the occupation-specific estimates are all close to

zero, generally ruling out effects larger than 6%.

       Further probing heterogeneous effects, Figure 9.(b) splits the difference-in-differences

estimates according to workers’ demographics, reported effects of AI chatbot use, usage

intensity, and timing of adoption. The figure reveals three insights about the limited

impacts of AI chatbots on labor market outcomes.

       First, while chatbot adoption has been highly unequal across demographic groups—with

younger men more likely to use the tools—we find no differential effects on their labor
  22
    Section 4.3 shows that survey responses from November 2024 similarly report no earnings impacts of
AI chatbots.


                                                 23
market outcomes. Second, while some workers do report substantial benefits from AI

chatbots (e.g., daily time savings of more than an hour), we cannot detect significantly

better labor market outcomes for these workers. Similarly, workers who report enhanced

quality or creativity or new workloads from AI chatbot usage have not fared better in the

labor market since their introduction. Finally, we find no evidence that AI chatbots have

had differential impacts on workers who use them more intensively (i.e., daily users for

work) or who adopted them early (i.e., within the first year of ChatGPT’s launch). The

absence of effects even for early adopters aligns with our dynamic difference-in-differences

estimates, which show no differential trend in outcomes following the arrival of AI chatbots

and suggest that the minimal impacts may not be merely a short-term phenomenon.

4.2.1    Impacts of Employer Initiatives

The difference-in-differences results above show that adopters have not fared better in

the labor market after the introduction of AI chatbots, even those who adopted early or

report large benefits from their use. To ensure that these estimates are not confounded

by unobserved shocks to adopters,23 we now isolate the variation in adoption associated

with employer policies only (Figure 2). Table B.3 reports the corresponding “first stage”

estimates, showing that encouragement increases adoption by 36.3 percentage points

among otherwise similar workers.

    Figure 10 shows the “reduced form” effects of employer encouragements on workers’

labor market outcomes, with dynamic effects in Panel (a) and occupation-specific impacts

in Panel (b). Across all of our occupations studied, workers who are encouraged to use

AI chatbots have not fared differently in the labor market. These results support our

conclusion that AI chatbots have had no causal effect on the labor market outcomes of

adopters. Section F.2 further supports this conclusion by using coworkers’ reports to
  23
     For example, workers experiencing unforeseen personal or professional setbacks may struggle to adopt
new technology. Conversely, those who expect to succeed regardless may see little need for chatbot
assistance.


                                                   24
measure employer encouragement.


4.3    Perceived Impacts

The absence of earnings impacts from AI chatbots may seem surprising, given that workers

report work-related benefits in Section 3. While reported time savings are also modest

(around 2%–4% for the average user; see Table 2), the confidence bands in Section 4.2

are narrow enough to rule out a comparable effect on earnings. For example, our pooled

estimate (“All” in Figure 9.(a)) rejects effects on earnings larger than 1%. More specifically,

software developers and marketing professionals report time savings of approximately 7%

when employers encourage AI chatbot use—effect sizes that Figure 9.(a) also rules out for

earnings.

   To further investigate the earnings impacts, we directly asked workers: “Have AI

chatbots affected your labor earnings?” If so, we followed up with, “By how much?” Figure

11 plots workers’ responses against their estimated time savings, yielding four key insights.

   First, workers overwhelmingly report that AI chatbots have not meaningfully affected

their earnings: the average perceived earnings impact ranges from 0.04% to 0.2%, de-

pending on whether their employer encourages their use. These estimates are an order

of magnitude smaller than the reported time savings in Section 3 and fall within the

confidence bands of the actual earnings effects in Section 4.2. Moreover, because these

perceived earnings effects were collected in November 2024, they provide reassurance that

the zero difference-in-differences estimates in Section 4.2 are not merely a consequence of

a short post-treatment window ending in June 2024. The continued absence of meaningful

effects in November 2024 aligns with the difference-in-differences estimates, which show

no differential trend following the introduction of AI chatbots.

   Second, the limited perceived earnings effects primarily reflect that 97% of workers

report no change in earnings due to AI chatbots—rather than large positive and negative


                                              25
effects canceling each other out (see Appendix D.2 for a detailed breakdown). This

further supports our conclusion from Figure 9 that AI chatbots have not had significant

heterogeneous impacts on labor market outcomes.

       Third, workers’ perceived earnings effects are only weakly correlated with their reported

time savings. As the slopes in Figure 11 indicate, only 3–7% of their estimated time

savings translate into earnings. This suggests that the limited labor market impacts result

from a genuinely weak pass-through of time savings and other benefits, rather than from

workers generally misperceiving their gains from AI chatbots.24

       Fourth and finally, all these effects—time savings, pass-through rates, and ultimately

earnings impacts—are significantly larger when employers encourage AI chatbot use. This

highlights the critical role of firm-led adaptions, not only in unlocking the work-related

benefits of the technology (as documented in Section 3) but also in translating these

benefits into labor market outcomes such as earnings.


4.4       Comparison to the Literature

The existing literature provides little evidence on whether adopters of AI chatbots have

fared better in the labor market, and a core contribution of this paper is to fill that gap.

While a host of studies document productivity effects within jobs, it remains unclear

how these translate into workers’ earnings and hours, as high-quality microdata on such

outcomes is rarely available. We address this limitation by leveraging the comprehensive

administrative labor market data offered in the Danish setting.

       Our key finding is that the adoption of AI chatbots has had no significant impact on

workers’ earnings, recorded hours, or wages. Although the productivity gains from chatbot

use are themselves modest—averaging 2.8% in time savings per user (see Section 3)—we
  24
    We do not have sufficient statistical power to detect comparable pass-through effects in our difference-
in-differences estimates of administrative labor market outcomes (Section 4.2). As such, readers may
wish to interpret our findings on the precise pass-through rates with some caution.




                                                    26
can rule out comparable effects on labor market outcomes. Our best estimate suggests

that only about 3–7% of workers’ time savings are passed through to higher earnings,

with greater elasticity at firms that actively encourage chatbot use.

       What might explain the weak relationship between reported productivity gains and

workers’ earnings? One possibility is that workers simply overestimate their actual

benefits from the tools. Given that the reported time savings are already modest, this

would reinforce the conclusion from Section 3.3 that realized gains are substantially lower

than RCT estimates. Nevertheless, overstated gains may not be the full story: workers

themselves recognize that only a small fraction of their reported time savings translates

into higher earnings. Indeed, workers’ self-reported earnings effects closely align with our

difference-in-differences estimates based on administrative data.

       Are the weak wage pass-through rates from AI chatbot gains theoretically surprising?

One benchmark is the competitive labor market model, in which wages equal marginal

productivity and do not respond to firm-specific shocks. Under this model, workers’

productivity gains from chatbot adoption should pass through one-to-one into wages,

while firm-level investments in the tools should have no effect on worker pay (Becker,

1964). Relative to this benchmark, it is surprising both that (i) workers’ adoption of AI

chatbots has had such limited effects on wages, and (ii) employer investments appear to

increase the pass-through to earnings.25

       What might explain the limited effects of AI chatbots on earnings, especially when

employers do not encourage their use? First, while chatbots may save time on existing

tasks, these savings may not increase productivity on marginal tasks unless employers
  25
     As described in Footnote 24, our conclusions about differential pass-through by employer encourage-
ment rely on workers’ self-reported earnings effects, as we lack the statistical power to detect comparable
effects in the administrative labor market outcomes. Readers may therefore wish to interpret these con-
clusions about pass-through rates with caution. Nevertheless, Appendix F.2 shows that the self-reported
pass-through estimates remain robust when using coworker reports to measure employer encouragement,
helping to mitigate concerns that the higher pass-through effects observed in these workplaces simply
reflect correlated reporting errors across variables.




                                                   27
adapt workflows accordingly. Consistent with this view, Section 3 shows that workers in

encouraged settings are better able to take on more work in response to chatbot use.

    Second, even if productivity increases, users of AI chatbots may be poorly positioned

to bargain for higher pay when employers do not endorse the tools. The bottom-up nature

of adoption—often occurring without managerial involvement—may create principal-agent

frictions that weaken the link between productivity and pay.

    More broadly, labor markets exhibit imperfections that both weaken the connection

between individual productivity and pay and allow firm-level productivity shocks to affect

wages (Kline, 2025; Manning, 2011). For example, Balke and Lamadon (2022) estimate

pass-through rates of 26% for worker-specific and 10% for firm-specific productivity shocks

using matched employer-employee data from Sweden. Similarly, Card et al. (2018) report

firm-level pass-through estimates ranging from 5% to 15%, a range that encompasses

our 7% estimate in encouraged settings. Such firm-level pass-through effects are often

attributed to firms expanding along upward-sloping labor supply curves. In the following

section, we directly examine the firm-level effects of chatbot adoption.


5     Broader Impacts

Our earlier analysis shows that while AI chatbots are now widely used—saving users

time and creating new job tasks, especially in workplaces that encourage their use—their

impact on adopters’ earnings and employment remains limited.

    In this final section, we examine whether AI chatbots have influenced broader workplace

outcomes. Even if the benefits to individual users have not yet translated into changes

in their earnings or hours, employers may still be adjusting overall employment levels

or wage bills in response to these tools. For instance, if AI chatbots reduce labor needs,

high-adoption workplaces might slow hiring or even lay off workers. Conversely, if the

tools enhance productivity and spur demand, these workplaces may instead expand

                                            28
employment and increase wage bills. Such adjustments could also affect non-adopting

workers, thereby violating the “no spillovers” assumption underlying our worker-level

difference-in-differences analysis in Section 4.2. Indeed, Section 3.2 showed that AI

chatbots have already created new workloads for non-users, indicating broader workplace

changes.


5.1    Empirical Strategy

To investigate the workplace impacts of AI chatbots, we shift our difference-in-differences

analysis to the workplace level, comparing workplaces with high versus low adoption

rates. Specifically, we run the regression models in Section 4.1.1, where Yit is now an

outcome of workplace i (e.g., total employment or wage bill), Xi are the average pre-

determined characteristics of its employees, and Ai is the share of its employees who

have adopted AI chatbots. We study these workplace relationships among employees

within each occupation. For instance, we examine how the total wage bill for marketing

professionals evolves in workplaces where a larger share of marketing professionals adopt

AI chatbots. We also examine incumbent workers—those employed before the introduction

of AI chatbots—whose outcomes we can track regardless of whether they remain with

their original firms.

   A concern for this analysis is that our survey may not cover all employees at workplace

i, leading to measurement error in the survey-based adoption rates Ai , which could bias

our difference-in-difference estimates. We take two steps to address this issue. First, as

described in Section 1.5, we implement a two-stage sampling strategy that maximizes

the coverage of our sampled workplaces—first drawing a random set of workplaces, then

sampling all their employees. Second, as described in Appendix G, we apply an Empirical

Bayes shrinkage procedure to correct for measurement error in the survey-based adoption

rates. Importantly, workplaces exhibit substantial variation in adoption rates even after


                                            29
correcting for measurement error: the standard deviation across workplaces remains 20

percentage points after shrinkage. Notably, all our results remain robust when using the

raw survey-based adoption rates.


5.2       Results

Figure 12 shows the impacts of AI chatbot adoption on total workplace wage bills and

employment hours. Panel (a) shows dynamic difference-in-differences, and Panel (b) shows

the pooled difference-in-differences for each occupation. Across the board, workplaces

with higher rates of AI chatbot adoption have not fared differently. Scaling the point

estimates with the standard deviation of workplace adoption rates (20pp after shrinkage;

see Appendix G), we can rule out standardized effects larger than 1%.

       The introduction of AI chatbots could also shift the composition of employment

between incumbent workers and new hires. For instance, adopting and operating new

tools may require hiring new workers who displace incumbents (Bessen et al., 2023),

whereas assistance from the tools could instead help retain workers (Brynjolfsson, Li

and Raymond, 2025). To explore these possibilities, Figure E.1 examines the impact of

workplace adoption on incumbent workers—those employed before the introduction of AI

chatbots—whose labor market outcomes we can track regardless of whether they remain

with or separate from their initial firm.26 Once again, we find no evidence that workers

initially employed at high-adoption workplaces have been affected differently.


5.3       Perceived Impacts

While the analysis above shows that high-adoption workplaces have not experienced

differential outcomes—even for non-adopting workers—AI chatbots could still affect non-

users through other channels. For example, if chatbot availability constitutes a broader,
  26
    This analysis of incumbent workers resembles the research designs of Autor et al. (2014); Walker
(2013).



                                                30
economy-wide shock, it could affect earnings across entire occupations, regardless of

individual or workplace adoption.

       To assess this possibility, we directly asked non-users whether they perceive AI chatbots

to have affected their earnings. Tellingly, Figure E.2 shows that 99.6% responded “No.”

This finding reinforces our conclusion that—despite changes in workloads, even among

non-users—AI chatbots have not caused broader impacts on labor market outcomes, such

as equilibrium wages or hours.


5.4       Comparison to the Literature

We have limited evidence on how AI chatbots affect workplace outcomes, largely because

firm-level data on Generative AI adoption remain scarce, and even fewer datasets link

adoption to workplace economic outcomes.27 We leverage our matched employer-employee

links and comprehensive sample coverage to aggregate workers’ responses to the workplace

level and assess their impacts in administrative labor market data.

       The closest related evidence comes from online job postings. Eisfeldt et al. (2024)

show that firms with occupational compositions more exposed to AI chatbots—based

on pre-ChatGPT job postings—experienced stock price increases following the release of

ChatGPT.28 Schubert (2025) further shows that hiring for Generative AI skills, as listed

in job postings, interacts with the demand for remote work. While these studies based

on job postings suggest notable changes in firms’ labor demand immediately following

the release of ChatGPT, we find no corresponding effects for high-adoption workplaces in

administrative labor market data.29
  27
     The few existing surveys on Generative AI adoption all sample individual workers, whose responses
cannot be linked at the workplace level (Blandin, Bick and Deming, 2025; Hartley et al., 2024; Pew,
2024). Bonney et al. (2024) survey AI adoption in U.S. firms as of February 2024 but do not specifically
measure Generative AI or link adoption to subsequent changes in economic outcomes.
  28
     This rise in market capitalization is consistent with firms being at an early stage of a productivity J-
curve, where current investments are expected to yield economic returns over the longer term (Brynjolfsson,
Rock and Syverson, 2021).
  29
    While job postings offer a rich source of data, it is less clear how well they capture employees’ actual
use of tools, particularly non-specialized ones like ChatGPT. First, although the emergence of Generative


                                                    31
    At the broader market level, the closest existing evidence comes from case studies of

online labor market platforms for freelance work. These studies document remarkable shifts

in labor demand following the launch of ChatGPT (Hui, Reshef and Zhou, 2024; Teutloff

et al., 2025). For example, Teutloff et al. (2025) report that demand for substitutable

freelance services, such as writing and translation, declined by 20–50% after ChatGPT. In

contrast, we find no significant impact on labor market outcomes across our diverse set of

11 occupations. What might explain this difference? Our evidence points to three factors.

    First, while freelance proofreading may be highly substitutable by AI chatbots, most

exposed occupations do not fall into this extreme category.30 Indeed, workers in our

survey report only modest time savings from AI chatbots. This reiterates our observations

from Section 3.3 that existing studies tend to concentrate on the occupations where the

productivity effects from the tools are the largest.

    Second, freelance work offers far less job security and rigidity, allowing productivity

changes to manifest more quickly in labor market outcomes. In contrast, we find only a

weak relationship between workers’ time savings and labor market effects from AI chatbots.

While the flexibility of freelance work makes it useful for identifying short-run changes

in labor demand, our findings on the limited pass-through of productivity gains caution

against extrapolating these effects to the broader labor market.

    Finally, although existing studies document shifts in the demand for certain tasks on

specific platforms, it remains unclear how these shifts affect workers’ total earnings and

hours, as workers may reallocate their time across tasks. In our survey, most workers report

using time saved by AI chatbots to perform other tasks, including new responsibilities
AI skills in job postings is notable, it remains unclear how such listings correspond to employees’ actual
use of AI chatbots (Schubert, 2025). Second, while Eisfeldt et al. (2024); Schubert (2025) rely on variation
in firm-level exposure to AI chatbots across occupations (i.e., variation in hiring across jobs with different
relevance to AI chatbots), our analysis instead examines variation in firm-level adoption of AI chatbots
within occupations (i.e., variation in actual use of AI chatbots for the same relevant jobs).
  30
     Teutloff et al. (2025) show that the overall impacts of ChatGPT on freelance work are more mixed,
with some complementary skills seeing increases.




                                                     32
introduced by AI. A key advantage of our administrative data is that it allows us to

measure workers’ total earnings and hours, regardless of how they reallocate their time in

the labor market.


6     Conclusion

Generative AI is heralded as the engine of a new industrial revolution (World Economic

Forum, 2024), yet we lack evidence on its economic impacts outside laboratory settings

and case studies (Brynjolfsson, Li and Raymond, 2025; Noy and Zhang, 2023).

    This paper provides large-scale evidence on the labor market impacts of AI chatbots,

the most widely adopted Generative AI tool to date. Our study is based on a series of

extensive surveys on AI chatbot usage in 11 exposed occupations, linked to administrative

matched employer-employee data in Denmark.

    Despite rapid adoption and substantial investments by both workers and firms, our

key finding is that AI chatbots have had minimal impact on productivity and labor

market outcomes to date. Moreover, we find no evidence of differential trends over time,

suggesting that the limited effects are not merely a very short-run phenomenon. In this

sense, our results echo Robert Solow’s famous observation about the IT revolution: “You

can see the computer age everywhere but in the productivity statistics” (Solow, 1987).

    However, our analysis sheds light on mechanisms through which Generative AI could

become transformative over time. First, consistent with Brynjolfsson, Rock and Syverson

(2021), we find that firm-driven investments and workplace reorganizations are critical

to unlocking AI’s potential: Take-up rates and productivity benefits of AI chatbots

are substantially higher when employers encourage usage, provide training, or deploy

in-house models. Second, aligning with theoretical predictions for how automation

technologies may reinstate labor demand (Acemoglu and Restrepo, 2019), we find that AI

chatbots have created new job tasks—extending even to workers who do not use the tools

                                           33
directly—signaling broader workplace transformations. Finally, labor market rigidities

appear to delay the economic impact, as productivity gains from AI chatbots translate

only weakly into earnings growth, particularly in firms that do not actively promote their

usage.

   Still, we believe that the key finding in this paper will remain central to understanding

the labor market effects of Generative AI. Any account of transformational change must

contend with a simple fact: two years after the fastest technology adoption ever, labor

market outcomes—whether at the individual or firm level—remain untouched.




                                            34
References
Acemoglu, Daron. 2025. “The Simple Macroeconomics of AI.” Economic Policy, 40(121): 13–58.
Acemoglu, Daron, and Pascual Restrepo. 2019. “Automation and New Tasks: How
 Technology Displaces and Reinstates Labor.” Journal of economic perspectives, 33(2): 3–30.
Acemoglu, Daron, Gary W Anderson, David N Beede, Cathy Buffington, Eric E
 Childress, Emin Dinlersoz, Lucia S Foster, Nathan Goldschlag, John C Halti-
 wanger, Zachary Kroff, et al. 2022. “Automation and the Workforce: A Firm-Level View
 from the 2019 Annual Business Survey.” National Bureau of Economic Research.
Altonji, Joseph G, Todd E Elder, and Christopher R Taber. 2005. “Selection on
  Observed and Unobserved Variables: Assessing the Effectiveness of Catholic Schools.” Journal
 of political economy, 113(1): 151–184.
Autor, David, Caroline Chin, Anna Salomons, and Bryan Seegmiller. 2024. “New
 Frontiers: The Origins and Content of New Work, 1940–2018.” The Quarterly Journal of
 Economics, qjae008.
Autor, David H, David Dorn, Gordon H Hanson, and Jae Song. 2014. “Trade Adjust-
 ment: Worker-Level Evidence.” The Quarterly Journal of Economics, 129(4): 1799–1860.
Balke, Neele, and Thibaut Lamadon. 2022. “Productivity shocks, long-term contracts, and
 earnings dynamics.” American Economic Review, 112(7): 2139–2177.
Becker, Gary S. 1964. Human Capital: A Theoretical and Empirical Analysis, with Special
 Reference to Education. Chicago:University of Chicago Press.
Bessen, James, Maarten Goos, Anna Salomons, and Wiljan Van den Berge. 2023.
 “Automatic Reaction-What Happens to Workers at Firms That Automate?” The Review of
 Economics and Statistics, , (Feb. 6, 2023).
Bick, Alexander, Adam Blandin, and David J Deming. 2025. “The Rapid Adoption of
  Generative AI.” National Bureau of Economic Research.
Blandin, Adam, Alexander Bick, and David Deming. 2025. “The Rapid Adoption of
  Generative AI.” Working Paper.
Bonney, Kathryn, Cory Breaux, Cathy Buffington, Emin Dinlersoz, Lucia S Foster,
  Nathan Goldschlag, John C Haltiwanger, Zachary Kroff, and Keith Savage. 2024.
 “Tracking Firm Use of AI in Real Time: A Snapshot From the Business Trends and Outlook
  Survey.” National Bureau of Economic Research.
Botero, Juan C, Simeon Djankov, Rafael La Porta, Florencio Lopez-de Silanes, and
 Andrei Shleifer. 2004. “The Regulation of Labor.” The Quarterly Journal of Economics,
 119(4): 1339–1382.
Bresnahan, Timothy F., and Shane Greenstein. 1996. “Technical Progress and Co-
 invention in Computing and in the Uses of Computers.” Brookings Papers on Economic
 Activity: Microeconomics, 1996: 1–83.
Brynjolfsson, Erik, and Lorin M Hitt. 2000. “Beyond Computation: Information Technology,
  Organizational Transformation and Business Performance.” Journal of Economic perspectives,
 14(4): 23–48.
Brynjolfsson, Erik, Danielle Li, and Lindsey R. Raymond. 2025. “Generative AI at
 Work.” The Quarterly Journal of Economics.
Brynjolfsson, Erik, Daniel Rock, and Chad Syverson. 2021. “The Productivity J-Curve:
  How Intangibles Complement General Purpose Technologies.” American Economic Journal:
 Macroeconomics, 13(1): 333–372.



                                             35
Card, David, Ana Rute Cardoso, Joerg Heining, and Patrick Kline. 2018. “Firms
 and Labor Market Inequality: Evidence and Some Theory.” Journal of Labor Economics,
 36(S1): S13–S70.
Carvajal, Daniel, Catalina Franco, and Siri Isaksson. 2024. “Will Artificial Intelligence
 Get in the Way of Achieving Gender Equality?” NHH Dept. of Economics Discussion Paper,
 , (03).
Cui, Zheyuan Kevin, Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng, and
 Tobias Salz. 2024. “The Effects of Generative AI on High Skilled Work: Evidence from
 Three Field Experiments with Software Developers.” Available at SSRN 4945566.
Dahl, Christian M, Daniel Le Maire, and Jakob R Munch. 2013. “Wage Dispersion and
 Decentralization of Wage Bargaining.” Journal of Labor Economics, 31(3): 501–533.
Danske Bank. 2024. “Danske Bank News Article.” Accessed: 2025-02-23.
David, Paul A. 1990. “The Dynamo and the Computer: An Historical Perspective on the
 Modern Productivity Paradox.” The American Economic Review, 80(2): 355–361.
Dell’Acqua, Fabrizio, Edward McFowland, Ethan R Mollick, Hila Lifshitz-Assaf,
 Katherine Kellogg, Saran Rajendran, Lisa Krayer, François Candelon, and
 Karim R Lakhani. 2023. “Navigating the Jagged Technological Frontier: Field Exper-
 imental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality.”
 Harvard Business School Technology & Operations Mgt. Unit Working Paper, , (24-013).
Dillon, Eleanor Wiske, Sonia Jaffe, Nicole Immorlica, and Christopher T Stanton.
 2025. “Shifting Work Patterns with Generative AI.” arXiv preprint arXiv:2504.11436.
Dutz, Deniz, Ingrid Huitfeldt, Santiago Lacouture, Magne Mogstad, Alexander
 Torgovitsky, and Winnie Van Dijk. 2025. “Selection in Surveys: Using Randomized
 Incentives to Detect and Account for Nonresponse Bias.” Working Paper.
Edelman, Benjamin G, Donald Ngwe, and Sida Peng. 2023. “Measuring the Impact of
 AI on Information Worker Productivity.” Available at SSRN 4648686.
Eisfeldt, Andrea L, Gregor Schubert, Miao Ben Zhang, and Bledi Taska. 2024.
 “Generative AI and Firm Values.” Available at SSRN 4436627.
Eloundou, Tyna, Sam Manning, Pamela Mishkin, and Daniel Rock. 2024. “GPTs are
  GPTs: Labor Market Impact Potential of LLMs.” Science, 384(6702): 1306–1308.
Feigenbaum, James, and Daniel P Gross. 2024. “Organizational and Economic Obstacles to
  Automation: A Cautionary Tale from at&T in the Twentieth Century.” Management Science,
  70(12): 8520–8540.
Groes, Fane, Philipp Kircher, and Iourii Manovskii. 2015. “The U-Shapes of Occupational
 Mobility.” The Review of Economic Studies, 82(2): 659–692.
Hartley, Jonathan, Filip Jolevski, Vitor Melo, and Brendan Moore. 2024. “The Labor
 Market Effects of Generative Artificial Intelligence.” Available at SSRN.
Heckman, James J. 1979. “Sample Selection Bias as a Specification Error.” Econometrica:
 Journal of the econometric society, 153–161.
Hui, Xiang, Oren Reshef, and Luofeng Zhou. 2024. “The Short-Term Effects of Generative
 Artificial Intelligence on Employment: Evidence from an Online Labor Market.” Organization
 Science, 35(6): 1977–1989.
Humlum, Anders, and Emilie Vestergaard. 2025. “The Unequal Adoption of ChatGPT
 Exacerbates Existing Inequalities Among Workers.” Proceedings of the National Academy of
 Sciences, 122(1): e2414972121.




                                            36
Hvidberg, Kristoffer B, Claus T Kreiner, and Stefanie Stantcheva. 2023. “Social
 Positions and Fairness Views on Inequality.” Review of Economic Studies, 90(6): 3083–3118.
Kline, Patrick M. 2025. “Labor Market Monopsony: Fundamentals and Frontiers.”
Manning, Allan. 2011. “Imperfect Competition in the Labor Market.” In Handbook of Labor
 Economics. Vol. 4, 973–1041. Elsevier.
Noy, Shakked, and Whitney Zhang. 2023. “Experimental Evidence on the Productivity
 Effects of Generative Artificial Intelligence.” Science, 381(6654): 187–192.
Oster, Emily. 2019. “Unobservable Selection and Coefficient Stability: Theory and Evidence.”
 Journal of Business & Economic Statistics, 37(2): 187–204.
Otis, Nicholas G, Solène Delecourt, Katelyn Cranney, and Rembrand Koning. 2024a.
 Global Evidence on Gender Gaps and Generative AI. Harvard Business School.
Otis, Nicholas, Rowan P Clarke, Solene Delecourt, David Holtz, and Rembrand
 Koning. 2024b. “The Uneven Impact of Generative AI on Entrepreneurial Performance.”
 Available at SSRN 4671369.
Peng, Sida, Eirini Kalliamvakou, Peter Cihon, and Mert Demirer. 2023. “The Im-
  pact of AI on Developer Productivity: Evidence from Github Copilot.” arXiv preprint
 arXiv:2302.06590.
Pew. 2024. “Pew Research Center: Americans’ Use of ChatGPT Is Ticking Up, but Few Trust
  Its Election Information.” https: // www. pewresearch. org/ short-reads/ 2024/ 03/ 26/
  americans-use-of-chatgpt-is-ticking-up-but-few-trust-its-election-information ,
  [Accessed 28-June-2024].
RISJ. 2024. “Reuters Institute for the Study of Journalism: What Does the Public in Six
 Countries Think about Generative AI in News?” https: // reutersinstitute. politics.
 ox. ac. uk/ what-does-public-six-countries-think-generative-ai-news# : ˜ :
 text= Averaging% 20across% 20six% 20countries% 2C% 20people,tried% 20to% 20use%
 20generative% 20AI , [Accessed 28-June-2024].
Roy, Andrew Donald. 1951. “Some thoughts on the distribution of earnings.” Oxford economic
 papers, 3(2): 135–146.
Schubert, Gregor. 2025. “Organizational Technology Ladders: Remote Work and Generative
  AI Adoption.” Available at SSRN.
Solow, Robert M. 1987. “We’d Better Watch Out.” New York Review of Books.
Teutloff, Ole, Johanna Einsiedler, Otto Kässi, Fabian Braesemann, Pamela Mishkin,
  and R Maria del Rio-Chanona. 2025. “Winners and Losers of Generative AI: Early
  Evidence of Shifts in Freelancer Demand.” Journal of Economic Behavior & Organization,
  106845.
Toner-Rodgers, Aidan. 2024. “Artificial Intelligence, Scientific Discovery, and Product Inno-
  vation.” arXiv preprint arXiv:2412.17866.
Walker, W Reed. 2013. “The Transitional Costs of Sectoral Reallocation: Evidence from the
 Clean Air Act and the Workforce.” The Quarterly journal of economics, 128(4): 1787–1835.
Walters, Christopher. 2024. “Empirical Bayes Methods in Labor Economics.” In Handbook of
 Labor Economics. Vol. 5, 183–260. Elsevier.
World Economic Forum. 2024. “Generative AI: Steam Engine of the Fourth Industrial
 Revolution?” Accessed: 2024-12-11.




                                             37
Figures and Tables
            Figure 1: Prevalence of Employer Initiatives for AI Chatbot Adoption
                                                    (a) Usage Policies
                    Marketing
                    Software Developers
                    Journalists
                    HR Professionals
                    IT Support
                    Financial Advisors
                    Customer Service
                    Accountants
                    Office Clerks
                    Legal Professionals
                    Teachers

                                          0   0.1   0.2       0.3    0.4      0.5      0.6     0.7   0.8    0.9   1
                                               Encouraged     Allowed    Not Allowed     No Policy   Don’t Know

                                               (b) In-House AI Chatbots
                                                          1
                    Marketing
                    Software Developers
                    Journalists
                    HR Professionals
                    IT Support
                    Financial Advisors
                    Customer Service
                    Accountants
                    Office Clerks
                    Legal Professionals
                    Teachers

                                          0   0.1   0.2       0.3    0.4      0.5      0.6     0.7   0.8    0.9   1
                                                                    Customized      Standard

                                              (c) Training in AI Chatbots
                                                          1
                    Marketing
                    Software Developers
                    Journalists
                    HR Professionals
                    IT Support
                    Financial Advisors
                    Customer Service
                    Accountants
                    Office Clerks
                    Legal Professionals
                    Teachers

                                          0   0.1   0.2       0.3    0.4      0.5      0.6     0.7   0.8    0.9   1
                                                              Firm-Arranged      Worker-Arranged

Notes: This figure shows the share of workers affected by various employer initiatives related to AI chatbot adoption. Panel
(a) shows employers’ policies on AI chatbot usage for work. Panel (b) indicates whether the employer has its own AI chatbot.
Panel (c) reports whether workers have participated 1in AI chatbot training courses. Figure B.1 provides a workplace-level
version of this graph, yielding similar results. Sample: All completed responses from the 2024 survey.

                                                                    38
              Figure 2: Importance of Employer Policies in AI Chatbot Adoption


      Ever Used                                                                     p< 0.01




Monthly or More                                                 p< 0.01




Weekly or More                                      p< 0.01




             Daily                p< 0.01

                      0                     .2                .4                  .6                  .8                     1

                                                    Encouraged             Non-Encouraged


Notes: This figure illustrates the impact of employer policies on workers’ use of AI chatbots. The estimates are based on
predicted values from Equation (1), varying employer usage policies (Encouraged = 1 vs. Encouraged = 0) while holding
workers’ characteristics X at their mean values. Whiskers represent 95% confidence bands of the predicted values. Some
confidence intervals are too narrow to be distinguished from the point estimates at this scale. The reported p-values test
whether the coefficients differ between the two groups. Sample: All completed responses from the 2024 survey linked to
registry data.




                                                           39
Figure 3: Influence of Employer Encouragement on Worker Gaps in AI Chatbot Adoption


                      Female                       p< 0.01



             Age (10 Years)                                       p< 0.01



     Experience (10 Years)                                              p= 0.255



               log(Earnings)                                                                         p= 0.012



      Net Wealth / Earnings                                                           p= 0.032


                               -.15                -.1                -.05                 0                 .05

                                                         Encouraged          Non-Encouraged


Notes: This figure illustrates the impact of employer usage policies on worker disparities in AI chatbot adoption. The
estimates are obtained from a multivariate regression of AI chatbot adoption on worker characteristics X, controlling for
occupation fixed effects, and are estimated separately based on employers’ AI chatbot initiatives (Encouraged = 1 vs.
Encouraged = 0). Whiskers represent 95% confidence intervals. The reported p-values test whether the coefficients differ
between the two groups. Sample: All completed responses from the 2024 survey linked to registry data.




                                                          40
                              Figure 4: Benefits of AI Chatbots for Adopters
                                                             (a) Reported Benefits

                          Time Savings                                                                                    p< 0.01



                                Quality                                                            p< 0.01



                              Creativity                                                      p< 0.01



                        Job Satisfaction                      p< 0.01



                            No Benefits            p< 0.01



                            Don't Know         p< 0.01

                                           0                        .2                   .4                     .6                  .8              1

                                                                              Encouraged                 Non-Encouraged



                                                       (b) Estimated Time Savings

                        Any Time Saving                                                                                   p< 0.01




                            15+ min/day                                                             p< 0.01




                            60+ min/day                    p< 0.01


                                           0                        .2                   .4                     .6                  .8              1

                                                                              Encouraged                 Non-Encouraged



                                                  (c) Allocation of Time Savings

                        More of Same Tasks                                     p< 0.01




                          More of Diff. Tasks                                                                                            p= 0.030




                                More Breaks            p= 0.168




                                More Leisure             p= 0.044

                                                   0                     .2                   .4                     .6              .8             1

                                                                                Encouraged                    Non-Encouraged


Notes: This figure illustrates how employer initiatives influence the benefits workers report from using AI chatbots. Panel
(a) presents the share of adopters reporting various benefits, Panel (b) shows the share reporting different levels of time
savings, and Panel (c) details how these workers allocate their saved time. The estimates are based on predicted values
from Equation (1), varying employer usage policies (Encouraged = 1 vs. = 0) while holding workers’ characteristics X at
their mean values. Whiskers represent 95% confidence bands of the predicted values. Some confidence intervals are too
narrow to be distinguished from the point estimates at this scale. The reported p-values test whether the coefficients differ
between the two groups. Sample: All completed responses from the 2024 survey linked to registry data.

                                                                                  41
                              Figure 5: New Workloads from AI Chatbots

                                                   (a) Adopters

                Same Tasks                      p< 0.01




                  New Tasks                                                p< 0.01




      Same and New Tasks             p< 0.01


                                 0                   .05                  .1                  .15                   .2

                                                           Encouraged          Non-Encouraged



                                                (b) Non-Adopters

                Same Tasks       p= 0.857




                  New Tasks                      p< 0.01




      Same and New Tasks p= 0.015

                                 0                   .05                  .1                  .15                   .2

                                                           Encouraged          Non-Encouraged


Notes: This figure illustrates how employer initiatives influence the new workloads created by AI chatbots. Panel (a)
presents results for adopters, while Panel (b) focuses on non-adopters (workers who have never used AI chatbots for work).
Estimates are predicted values from Equation (1), varying employer usage policies (Encouraged = 1 vs. Encouraged = 0)
while holding workers’ characteristics X at their mean values. Whiskers represent 95% confidence bands of the predicted
values. Some confidence intervals are too narrow to be distinguished from the point estimates at this scale. The reported
p-values test whether the coefficients differ between the two groups. Sample: All completed responses from the 2024 survey
linked to registry data.

                                                            42
                                     Figure 6: Composition of AI Tasks


 IT Support
 Software Developers
 HR Professionals
 Legal Professionals
 Office Clerks
 Customer Support
 Teachers
 Marketing Professionals
 Journalists
 Accountants
 Financial Advisors

                             0        0.1      0.2      0.3        0.4     0.5      0.6       0.7      0.8      0.9        1

                                        AI Integration         AI Content Drafting        AI Ethics & Compliance
                                      AI Quality Review         AI Data Insights                AI Ideation
Notes: This figure shows the distribution of reported new job tasks across major task categories for each occupation. AI
Ideation refers to “using AI to generate or expand creative ideas, such as concepts, strategies, or solutions,” AI Content
Drafting refers to “using AI tools to produce initial drafts of text or media,” AI Quality Review refers to “reviewing and
correcting AI-generated content for accuracy, clarity, and relevance,” AI Data Insights refers to “using AI to analyze data or
documents and extract key patterns or insights,” AI Integration refers to “embedding AI into workflows to automate or
enhance tasks,” and AI Ethics & Compliance refers to “ensuring AI use follows ethical, legal, and organizational standards.”
See Appendix C.2 for details and occupation-specific examples. Tasks are ordered according to their average shares among
the eleven occupations. Occupations are ordered according to their shares on AI Integration, the most frequent tasks across
the occupations. Sample: All completed responses from the    1 2024 survey who reported new job tasks due to AI chatbots.




                                                              43
                    Figure 7: Log Earnings Around the Launch of AI Chatbots

                                          (a) Adopters – Non-Adopters
                           .15




                             .1




                           .05




                             0




                           -.05
                             2021m1    2021m7       2022m1      2022m7       2023m1     2023m7         2024m1

                                                                         Adopters



                            (b) Encouraged / Other Adopters – Non-Adopters
                           .15




                             .1




                           .05




                             0




                           -.05
                             2021m1    2021m7       2022m1      2022m7       2023m1     2023m7         2024m1

                                                Encouraged Adopters          Non-Encouraged Adopters



                                            (c) Difference-in-Differences
                           .15




                             .1




                           .05




                             0




                           -.05
                             2021m1    2021m7       2022m1      2022m7       2023m1     2023m7         2024m1

                                                Encouraged Adopters          Non-Encouraged Adopters


Notes: This figure shows the earnings gap between AI chatbot adopters and non-adopters, before and after the launch of
ChatGPT in November 2022. Panel (a) reports the difference in log earnings between AI chatbot adopters and non-adopters,
controlling for occupation fixed effects, pre-determined worker characteristics, and seasonality. Panel (b) splits adopters
by whether their employers encourage chatbot use, keeping all non-adopters as the control group in both cases. Panel (c)
presents the difference-in-differences that correspond to Panel (b), indexed to November 2022, the launch date for ChatGPT.
The difference-in-difference estimates are based on the specification in Equation (2). Shaded areas represent 95% confidence
intervals. Sample: All completed responses from the 2024 survey linked to registry data.

                                                                 44
          Figure 8: Labor Market Outcomes of Adopters Relative to Non-Adopters
                                              Difference-in-Differences

                                                 (a) log Hourly Wage
                          .15




                           .1




                          .05




                           0




                         -.05
                           2021m1      2021m7         2022m1         2022m7       2023m1      2023m7        2024m1

                                              Encouraged Adopters        Non-Encouraged Adopters




                                                       (b) log Hours
                          .15




                           .1




                          .05




                           0




                         -.05
                           2021m1    2021m7       2022m1       2022m7    2023m1      2023m7        2024m1

                                              Encouraged Adopters        Non-Encouraged Adopters




                                     (c) Extensive-Margin Employment
                          .15




                           .1




                          .05




                           0




                         -.05
                           2021m1      2021m7         2022m1         2022m7       2023m1      2023m7        2024m1

                                              Encouraged Adopters        Non-Encouraged Adopters


Notes: This figure presents the differential labor market outcomes of AI chatbot adopters relative to non-adopters, indexed
to the launch of ChatGPT in November 2022. Effects are estimated separately for adopters whose employers encourage AI
chatbot use (“Encouraged”) and those without encouragement (“Non-Encouraged”), with all non-adopters serving as the
control group in both cases. Estimates are based on the dynamic difference-in-differences specification in Equation (2).
Shaded areas represent 95% confidence intervals. Sample: All completed responses from the 2024 survey linked to registry
data.

                                                                    45
          Figure 9: How Do the Earnings Effects of Adoption Vary Across Workers?
                      Pooled Difference-in-Differences in Log Earnings

                                            (a) Occupation-Level Effects

                              All
                      Journalists
                  Software Dev.
                     Legal Prof.
                    Accountants
              Customer Service
                      Marketing
              Financial Advisors
                        HR Prof.
                   Office Clerks
                       Teachers
                      IT Support
                                    -.1          -.05              0             .05             .1              .15

                                                Encouraged Adopters         Non-Encouraged Adopters


                            (b) Differential Effects by Worker Characteristics

                           Female

                             Older

                      Experienced

                    Higher Earner

              Large Time Savings

                 Increased Quality

               Increased Creativity

                    Incr. Workload

                         Daily Use

                    Early Adopters

                                      -.1          -.05                0          .05             .1             .15

                                                 Encouraged Adopters         Non-Encouraged Adopters


Notes: This figure presents the differential labor market outcomes of AI chatbot adopters relative to non-adopters, indexed
to the launch of ChatGPT in November 2022. Effects are estimated separately for adopters whose employers encourage AI
chatbot use (“Encouraged”) and those without encouragement (“Non-Encouraged”), with all non-adopters serving as the
control group in both cases. Estimates are based on the pooled difference-in-differences specification in Equation (3), with
whiskers representing 95% confidence intervals. Panel (a) first shows a pooled estimate (All) and then reports impacts
separately for each of our 11 study occupations. Panel (b) shows differential effects by workers’ characteristics, estimated by
interacting the regression model in Equation (3) with an indicator for the particular characteristic. These indicators are coded
as follows: Female indicates women, Older/Experienced/Higher Earner indicates above-median age/experience/earnings
within the occupation, Large Time Savings indicates users who report time savings exceeding 60 minutes per day of use
(see Figure 4.(b)), Increased Quality / Creativity indicates reporting improved quality / creativity from using AI chatbots
(see Figure 4.(a)). Incr. Workload indicates reporting new job tasks due to AI chatbots (see Figure 5). Daily Use indicates
users who report using AI chatbots for work on a daily basis (see Figure 2). Early adopters are workers who had adopted
ChatGPT in our 2023 survey round. (Because the 2023 round did not ask about employer encouragement, we can only
report the average effect.) Sample: All completed responses from our surveys linked to registry data.


                                                              46
     Figure 10: Have Encouragements Affected Workers’ Outcomes? (Reduced Form)

              (a) Labor Market Effects of Encouragement (Dynamic Diff-in-Diffs)




              (b) Occupation-Level Effects of Encouragement (Pooled Diff-in-Diffs)

                       All
              Journalists
          Software Dev.
             Legal Prof.
            Accountants
     Customer Service
               Marketing
     Financial Advisors
                HR Prof.
           Office Clerks
               Teachers
              IT Support
                             -.1             -.05                0                .05                .1               .15

                                                          log(Earnings)         log(Hours)


Notes: This figure presents the differential labor market outcomes of workers who are encouraged to use AI chatbots by
their employers, compared to all other workers, indexed to the launch of ChatGPT in November 2022. Panel (a) is based on
the dynamic difference-in-differences specification in Equation (2), with shaded areas representing 95% confidence intervals.
The plot also reports the corresponding first-stage effect on adoption (0.363) from Table B.3. Panel (b) first shows a pooled
estimate (All) and then reports impacts separately for each of our 11 study occupations. These effects are based on the
pooled difference-in-differences specification in Equation (3), with whiskers representing 95% confidence intervals. Sample:
All completed responses from the 2024 survey linked to registry data.


                                                            47
Figure 11: How Do Workers’ Earnings Impacts Relate to Their Time Savings? (Binscatter)




Notes: This figure presents a binned scatterplot of workers’ perceived earnings impacts from AI chatbots against their
estimated time savings from these tools, absorbing occupation fixed effects. The sample is divided based on whether
employers encourage AI chatbot use. The regression line represents the line of best fit for each group, controlling for
occupation fixed effects. Sample: All completed responses from the 2024 survey.




                                                         48
                   Figure 12: Have High-Adoption Workplaces Fared Differently?

                                             (a) Workplace Outcomes
         .15


          .1


         .05


           0


        -.05


         -.1


        -.15
           2021m1         2021m7         2022m1            2022m7      2023m1         2023m7          2024m1

                                           log(Total Earnings)               log(Total Hours)


                                          (b) Occupation-Level Effects

                          All
                  Journalists
               Software Dev.
                  Legal Prof.
                Accountants
        Customer Service
                   Marketing
        Financial Advisors
                    HR Prof.
                Office Clerks
                   Teachers
                  IT Support
                                 -1                  -.5                 0                   .5                  1

                                                     log(Total Earnings)         log(Total Hours)


Notes: This figure shows changes in workplace outcomes by adoption rates, indexed to the launch of ChatGPT in November
2022, at the workplace-occupational level. We study these workplace relationships among employees within each occupation.
Adoption rates are measured as the share of employees who have used AI chatbots for work, adjusted for measurement error
using an Empirical Bayes shrinkage procedure detailed in Appendix G. The standard deviation of workplace adoption rates
within occupations, after shrinkage, is 20 percentage points. Panel (a) is based on the dynamic difference-in-differences
specification in Equation (2), weighted by the number of respondents at the workplace; shaded areas indicate 95% confidence
intervals. Panel (b) shows the effects separately by occupation, based on the pooled difference-in-differences specification in
Equation (3), also weighted by the number of respondents at the workplace; whiskers indicate 95% confidence intervals.
Sample: All completed responses from workplaces with at least two respondents from the 2024 survey linked to registry
data.


                                                              49
                Table 1: Which Workplaces Have Adopted AI Chatbot Initiatives?
                                                                                                   Firm-Arranged   In-House
                                Encouraged     Allowed     Not Allowed No Policy     Don’t Know       Training     Chatbot
                                   (1)           (2)           (3)        (4)            (5)            (6)           (7)
 Firm Age (10 Years)              -0.0140∗∗     0.0030       0.0028      0.0038∗       0.0044        -0.0122∗∗     -0.0091∗
                                  (0.0044)     (0.0021)     (0.0026)     (0.0016)     (0.0025)       (0.0039)      (0.0043)

 log(Firm Employment)              0.0036     -0.0082∗∗∗     0.0036     -0.0195∗∗∗    0.0204∗∗∗       -0.0048      0.0362∗∗∗
                                  (0.0048)     (0.0023)     (0.0023)     (0.0022)     (0.0029)       (0.0043)      (0.0056)

 log(Firm Labor Productivity)     0.0468∗∗    0.0275∗∗∗      0.0051     -0.0374∗∗∗    -0.0420∗∗∗     0.0765∗∗∗     0.0697∗∗∗
                                  (0.0153)    (0.0077)      (0.0051)     (0.0077)      (0.0084)      (0.0135)      (0.0176)

 Private Firm                     0.0414∗       -0.0076     -0.0141∗      -0.0104      -0.0092        0.0257       0.0554∗∗
                                  (0.0168)     (0.0094)     (0.0072)     (0.0066)     (0.0096)       (0.0144)      (0.0180)
 Occupation FE’s                     ✓            ✓            ✓            ✓             ✓              ✓            ✓
 Mean of Outcome                   0.419        0.209        0.061        0.132         0.178          0.231        0.375
 Within R2                         0.013        0.003        0.009        0.016         0.016          0.010        0.042
 R2                                0.106        0.005        0.032        0.046         0.071          0.023        0.123
 Observations                      24184        24184        24184        24184         24184          24184        24184

Notes: This table examines which firm characteristics predict the adoption of various employer initiatives to promote AI
chatbot use. Columns (1)–(5) report results for employer usage policies, while Columns (6)–(7) report results for in-house
chatbots and firm-provided training. Firm characteristics are measured in 2021, our latest data year available. Labor
productivity is measured as value added per full-time equivalent worker. The regressions control for whether the firm reports
value added. The regressions also control for occupation fixed effects, and Table B.1 shows that the estimates are robust to
adding controls for worker characteristics. Standard errors, reported in parentheses, are clustered at the firm level. Sample:
The table is based on all completed responses from the 2024 survey that can be linked to the registry data.




                                                             50
               Table 2: What Drives Adopters’ Time Savings from AI Chatbots?
                                                  Time Savings     Time Saved Per Day Used  Days Used
                                                  / Work Hours       / Daily Work Hours    / Work Days Covariance
  Occupation                                          (1)                    (2)               (3)        (4)
  Marketing Professionals      Encouraged              .068                   .109                  .515          .012
  Marketing Professionals      Non-Encouraged          .046                   .087                  .388          .012
  Software Developers          Encouraged              .065                   .093                  .567          .012
  Software Developers          Non-Encouraged          .039                   .074                  .378          .011
  HR Professionals             Encouraged              .042                   .081                  .405          .009
  HR Professionals             Non-Encouraged          .026                   .074                  .237          .009
  IT Support                   Encouraged              .041                   .075                  .407          .011
  IT Support                   Non-Encouraged          .028                    .06                  .283          .011
  Customer Service Rep.        Encouraged              .039                   .066                  .439          .010
  Customer Service Rep.        Non-Encouraged          .020                   .050                  .240          .008
  Legal Professionals          Encouraged              .033                   .074                  .336          .008
  Legal Professionals          Non-Encouraged          .018                   .065                  .166          .007
  Office Clerks                Encouraged              .029                   .065                  .309          .009
  Office Clerks                Non-Encouraged          .015                   .047                  .177          .007
  Journalists                  Encouraged              .028                   .050                  .374          .010
  Journalists                  Non-Encouraged          .021                   .048                  .221          .011
  Financial Advisors           Encouraged              .022                   .053                  .288          .007
  Financial Advisors           Non-Encouraged          .015                   .040                  .179          .008
  Accountants and Auditors     Encouraged              .022                   .055                  .282          .006
  Accountants and Auditors     Non-Encouraged          .009                   .041                  .143          .003
  Teachers                     Encouraged              .010                   .049                  .140          .003
  Teachers                     Non-Encouraged          .006                   .044                  .088          .002
  All                          Encouraged              .036                   .070                  .369          .010
  All                          Non-Encouraged          .022                   .057                  .227          .009
Notes: This table presents workers’ time savings from AI chatbots, categorized by workers’ occupations and employer policies.
The table focuses on workers who have ever used AI chatbots for work. Column (1) reports the average time savings as a
percentage of total work hours. The remaining columns decompose these time savings into three components: time savings
per day of use (Column (2)), the share of workdays with AI chatbot usage (Column (3)), and the covariance between Columns
(2) and (3) (Column (4)). These components satisfy the relationship: Column (1) = Column (2) × Column (3) + Column (4),
which follows from the identity: E[XY ] = E[X]E[Y ] + Cov(X, Y ). Occupations are sorted by their average time savings
(Column (1)) among encouraged users. We code daily time savings (Column (2)) as follows: 0–15 minutes/day as 7.5
minutes, 15–60 minutes as 37.5 minutes, and 60+ minutes as 90 minutes. We code frequency of use (Column (3)) as follows:
daily use is divided by 1; weekly use by 5 (corresponding to 5 workdays per week); monthly use by 21 23 (corresponding to
4 13 weeks per month); and use a few times by 65 (corresponding to 4 uses over 12 months). We set daily work hours to 8, as
nearly all sampled workers are full-time employees. Sample: The table is based on all completed responses from the 2024
survey that can be linked to the registry data.




                                                              51
                             Online Appendix
Large Language Models, Small Labor Market Effects

                    Anders Humlum              Emilie Vestergaard
                  University of Chicago     University of Copenhagen



A Data and Institutional Setting                                                            3
  A.1 Sampling Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          3
  A.2 Survey Sample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          4

B Adoption                                                                                   9
  B.1 Employer Initiatives . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         9
  B.2 Worker Adoption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         11

C Work                                                                                      20
  C.1 Benefits for Users . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      20
  C.2 Workloads and Task Creation . . . . . . . . . . . . . . . . . . . . . . . .           21

D Labor Market Outcomes                                                                     27
  D.1 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     27
  D.2 Perceived Impacts       . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   27

E Broader Impacts                                                                           29
  E.1 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     29
  E.2 Perceived Impacts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       30

F Robustness Analysis                                                                       30
  F.1 Additional Controls       . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   31
  F.2 Coworker Encouragement . . . . . . . . . . . . . . . . . . . . . . . . . .            34

G Empirical Bayes Shrinkage                                                                 40
  G.1 Workplace Adoption Rates . . . . . . . . . . . . . . . . . . . . . . . . . .          41
  G.2 Coworker Encouragement Rates . . . . . . . . . . . . . . . . . . . . . . .            42


                                             1
H Theoretical Framework                                                                     44
    H.1 Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   44
    H.2 Predictions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     45
    H.3 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    48

I   Invitation Letter                                                                       49
    I.1 English Translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   50
    I.2 Original Danish Version . . . . . . . . . . . . . . . . . . . . . . . . . . . .     52

J Survey Questionnaire                                                                      54
    J.1 English Translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   55
    J.2 Original Danish Version . . . . . . . . . . . . . . . . . . . . . . . . . . . .     60




                                               2
A      Data and Institutional Setting
A.1     Sampling Protocol

Our 2024 survey invited 115,000 workers across 11 occupations. Ideally, we would sample

an equal number from each—i.e., 10,450 journalists, 10,450 software developers, etc.

However, some occupations in Denmark employ fewer than 10,450 workers. To address

this, we follow these steps:


  1. If an occupation has fewer than 10,450 workers, we sample all available workers.

  2. The remaining invitations are redistributed equally among the other occupations.

  3. Workplaces are randomly selected for sampling, and if chosen, all relevant workers

      (i.e., those in the target occupation) within the workplace are included.

  4. Large workplaces can distort the sample balance. To mitigate this, we apply

      individual-level sampling to the top 2.5% of workplaces (ranked by the number of

      employees in the relevant occupation), randomly selecting employees using the same

      sampling probability as in Step 3.

  5. To precisely reach our target of 115,000 workers, we make final adjustments by

      randomly including or excluding workers, independent of their workplace.


The 2023 survey followed a similar protocol, with minor modifications; see Humlum and

Vestergaard (2025) for details.




                                            3
A.2         Survey Sample

Table A.1 outlines how successive sample restrictions define our analysis sample. In total,

we obtained about 25,000 complete and valid responses per survey round that can be

linked to registry data. The attrition and response rates in our survey are comparable

to those obtained in previous Danish surveys (Hvidberg, Kreiner and Stantcheva, 2023).

While our main analysis focuses on responses from the 2024 round, we use the 2023 round

to examine the dynamics of our estimated effects.


                                           Table A.1: Sample Construction

                                           2024 Survey                                        2023 Survey
                                                                             Main Survey                    Follow-Up Only
                                Individuals   Percent of invitees   Individuals Percent of invitees Individuals Percent of invitees
 1.   Invitees                   115,000            100.0            100,000           100.0          15,000           100.0
 2.   Respondents                 30,411             26.4             29,067           29.1            4,094           27.3
 3.   In target occupation(s)     26,925             23.4             25,121           25.1            3,504           23.4
 4.   Complete responses          25,241            21.9             18,109            18.1           2,561            17.1
 5.   Linked to registers        24,796              21.6             17,907            17.9           2,559           17.1

Notes: This table outlines how successive sample restrictions define our analysis sample. We conducted two survey rounds
in November 2023 and 2024, each inviting 115,000 workers to participate. The 2023 survey included both a main survey
and a two-week follow-up, with 15,000 workers invited only to the follow-up. Row 2 reports the number of individuals who
responded to the survey. Row 3 shows the respondents who were still employed in one of our 11 target occupations at the
time of the surveys. Row 4 presents the respondents who fully completed the survey questionnaire. Row 5 indicates the
complete responses that could be linked to registry data.




                                                                    4
A.2.1       Representativeness and Response Quality

In this section, we extend the checks of representativeness and response quality provided

in Humlum and Vestergaard (2025) to include the 2024 survey round.

    Table A.2 show that our survey respondents resemble our survey populations on

observable characteristics.


                          Table A.2: Balance Table for Survey Respondents

                                      2024 Survey                                  2023 Main Survey
                            Population Sampled Responded                   Population Sampled Responded
                               (1)        (2)     (3)                         (1)        (2)        (3)

  Age                           42.93          42.94          46.11            42.41          42.40         45.38
                              (11.54)         (11.52)        (11.50)          (11.57)        (11.57)       (11.51)
  Female                        0.56            0.56           0.56             0.52           0.52          0.49
                               (0.50)          (0.50)         (0.50)           (0.50)         (0.50)        (0.50)
  log(Earnings)                12.98           12.98          13.01            13.07          13.07         13.11
                               (0.70)          (0.70)         (0.64)           (0.58)         (0.59)        (0.53)
  Experience                     6.11           6.11           7.24             6.05           6.05          7.12
                               (4.80)          (4.80)         (4.92)           (4.58)         (4.57)        (4.67)
  Wealth / Earnings            10.92            6.50           6.74             4.09           4.87          4.10
                             (2,148.09)      (286.36)       (204.16)         (157.40)       (262.31)       (39.57)
  Observations                284,439        115,000            25,241       283,806        100,000         18,109
Notes: This table compares the mean characteristics of workers in our population (Column 1), our sampled survey invitees
(Column 2), and survey respondents with complete responses (Column 3) for each survey round. The Sampled columns
correspond to line 1 of Table A.1. The Responded columns correspond to line 4 of Table A.1. Population columns (1)
show a difference in the female share between the 2023 and 2024 survey rounds that warrants explanation. This difference
arises from a slight modification to the sampling protocol in 2023, in which some sampled workplaces had only (a random)
50% of their relevant workers invited to the survey. This altered the weight each of our 11 occupations received in the
invite population, leading to the shifts in gender share observed in columns (1). Importantly, and as expected, the gender
composition of the survey population within each of our 11 occupations remains virtually unchanged between survey rounds,
as does the total unweighted worker population (i.e., without reweighting occupations to reflect our sampling protocol).
Since all analyses include occupation fixed effects, this change in occupational composition across survey rounds does not
affect our results. Moreover, nearly all analyses in this paper rely on the 2024 survey round, which did not involve the
sampling protocol modification. Sample: The table includes all individuals in our survey population.




                                                            5
    Table A.2 shows that complete respondents (who form the basis of our main analysis

sample) and partial respondents have similar characteristics and give similar responses to

the survey (before partial respondents drop out).


                  Table A.3: Balance Table for Complete vs. Partial Responses

                                                    2024 Survey                   2023 Main Survey
                                                Completed Drop Out              Completed Drop Out
                                                   (1)        (2)                  (1)        (2)

              Panel A: Characteristics
              Age                                   46.11          44.46           45.38           45.00
                                                   (11.50)        (11.98)         (11.51)         (11.53)
              log(Earnings)                         13.01          13.00           13.11           13.10
                                                    (0.64)         (0.71)          (0.53)          (0.53)
              Experience                             7.24           6.52            7.12            6.88
                                                    (4.92)         (4.82)          (4.67)          (4.63)
              Net Wealth/Earnings                    6.74           3.77            4.10            3.75
                                                  (204.16)        (10.08)         (39.57)         (16.43)
              Female                                 0.56           0.57            0.49            0.60
                                                    (0.50)         (0.49)          (0.50)          (0.49)
              Panel B: Adoption
              Used                                  0.69            0.75            0.55            0.51
                                                   (0.46)          (0.43)          (0.50)          (0.50)
              Used for Work                         0.49            0.58            0.40            0.38
                                                   (0.50)          (0.49)          (0.49)          (0.48)
              Used for Core Task                    0.31            0.15            0.21            0.17
                                                   (0.46)          (0.35)          (0.41)          (0.38)
              Observations                         25,241          1,773           18,109          7,012


Notes: This table compares the mean characteristics and adoption behaviors of workers who fully completed (Column 1)
and partially completed (Column 2) our surveys. The Completed columns correspond to line 4 of Table A.1. Standard
deviations are shown in parentheses. See the note of Table A.2 for an explanation of the difference in the female population
shares between the 2023 and 2024 survey rounds. Sample: All individuals with partial survey responses.




                                                             6
       Table A.4 shows that workers who are randomly offered a higher participation prize

are more likely to take part in our surveys but do not systematically differ in their

responses. Dutz et al. (2025) develop an econometric framework that uses this variation

to reweight the sample based on workers’ latent willingness to participate; see Humlum

and Vestergaard (2025) for its application to our survey.


                       Table A.4: Balance Table for Participation Prize Categories

                                                  2024 Survey                                      2023 Main Survey
                              Levels         Differences to 1000 DKK   p-value     Levels         Differences to 1000 DKK   p-value
                            1000 DKK   2500 DKK 5000 DKK 10000 DKK               1000 DKK   2500 DKK 5000 DKK 10000 DKK
                               (1)        (2)           (3)        (4)   (5)        (1)        (2)           (3)        (4)   (5)

 Panel A: Characteristics
 Age                          46.11      -0.25       -0.18      -0.44    0.18      45.38      -0.46      -0.42      -0.49     0.15
                                        (0.20)      (0.90)     (0.91)                        (0.24)     (0.96)     (0.97)
 log(Earnings)                13.01      -0.00       -0.01      -0.01    0.48      13.11      -0.03      -0.00      -0.01     0.04
                                        (0.01)      (0.11)     (0.11)                        (0.01)     (0.06)     (0.06)
 Experience                   7.24       -0.09       -0.11      -0.06    0.55      7.12       -0.01      -0.01      -0.05     0.95
                                        (0.08)      (0.40)     (0.40)                        (0.09)     (0.35)     (0.35)
 Net Wealth/Earnings          6.74       -1.96        0.62       0.94    0.50      4.10       -0.05       0.87       0.38     0.55
                                        (1.71)     (36.33)    (35.44)                        (0.27)     (0.42)     (0.42)
 Female                       0.56       -0.02       -0.00      -0.02    0.04      0.49        0.00      -0.01      -0.00     0.41
                                        (0.01)      (0.03)     (0.04)                        (0.01)     (0.04)     (0.04)
 Panel B: Adoption
 Used                         0.69       0.00       -0.00      -0.01     0.69      0.55       -0.02      -0.01      -0.01     0.40
                                        (0.01)     (0.03)     (0.03)                         (0.01)     (0.03)     (0.03)
 Used for Work                0.49       -0.00      -0.02      -0.02     0.02      0.40       -0.01      -0.00      -0.00     0.61
                                        (0.01)     (0.03)     (0.03)                         (0.01)     (0.04)     (0.04)
 Used for Core Task           0.31       -0.00      -0.01      -0.00     0.75      0.21       -0.01      0.00       -0.00     0.59
                                        (0.01)     (0.03)     (0.03)                         (0.01)     (0.04)     (0.04)
 Response Rate                0.20       0.02       0.02       0.03      0.00      0.16       0.02       0.02       0.04      0.00
                                        (0.00)     (0.00)     (0.00)                         (0.00)     (0.00)     (0.00)
 Observations                 5,787      6,351     6,432       6,671               4,026      4,525     4,549       5,009



Notes: This table shows that individuals assigned to different participation prize categories (1,000 DKK, 2,500 DKK, 5,000
DKK, and 10,000 DKK) have similar characteristics (Panel A) and adoption behaviors (Panel B) but differ in their rates of
completed responses (last row). Column (5) reports p-values from a joint test of whether mean outcomes are equal across
the four prize categories. The total number of observations corresponds to line 4 of Table A.1. See the note of Table A.2 for
an explanation of the difference in the female population shares between the 2023 and 2024 survey rounds. Sample: All
complete survey responses.




                                                                   7
       As an external validation of our survey responses, we cross-check variables workers’

reported occupations with those recorded in the administrative registers. Table A.5 shows

that the survey and registers agree on the occupation of 87% of our respondents.

Table A.5: Correlation Between Occupation in Survey vs. Register, P (Survey|Register)
                                                                                                                                                           In Survey
                           Journalists   Software Developers   Paralegals Accountants and Auditors   Customer Service Rep.   Marketing Professionals   Financial Advisors   HR Professionals   Office Clerks   Teachers   IT Support   Observations

                                                                                                             Panel A: 2024 Survey

       Journalists            0.98              0.00             0.00               0.00                     0.00                     0.00                    0.00                0.00             0.00          0.00        0.00         325.00
  Software Developers         0.00              0.86             0.00               0.00                     0.01                     0.01                    0.00                0.00             0.01          0.00        0.08        2,799.00
       Paralegals             0.01              0.03             0.81               0.02                     0.00                     0.00                    0.02                0.02             0.07          0.01        0.01        2,106.00
Accountants and Auditors      0.00              0.02             0.01               0.86                     0.01                     0.01                    0.02                0.01             0.05          0.00        0.01        2,793.00
 Customer Service Rep.        0.00              0.02             0.01               0.01                     0.79                     0.03                    0.00                0.01             0.09          0.01        0.01         631.00
 Marketing Professionals      0.00              0.07             0.01               0.01                     0.09                     0.69                    0.01                0.01             0.07          0.01        0.03        1,781.00
   Financial Advisors         0.00              0.00             0.00               0.00                     0.01                     0.00                    0.96                0.00             0.01          0.00        0.00        1,243.00
    HR Professionals          0.01              0.03             0.03               0.01                     0.00                     0.02                    0.02                0.73             0.12          0.01        0.01         849.00
      Office Clerks           0.00              0.01             0.00               0.00                     0.00                     0.00                    0.00                0.00             0.97          0.00        0.01        6,488.00
        Teachers              0.00              0.00             0.00               0.00                     0.00                     0.00                    0.00                0.00             0.00          1.00        0.00        6,440.00
      IT Support              0.00              0.13             0.00               0.00                     0.02                     0.02                    0.00                0.00             0.03          0.00        0.79        1,470.00
                                                                                                             Panel B: 2023 Survey

       Journalists            0.97              0.00             0.00               0.00                     0.00                     0.01                    0.00                0.00             0.01          0.00        0.00         555.00
  Software Developers         0.00              0.87             0.00               0.00                     0.01                     0.02                    0.00                0.00             0.01          0.00        0.08        3,185.00
       Paralegals             0.01              0.03             0.79               0.02                     0.01                     0.00                    0.01                0.02             0.08          0.01        0.01        2,518.00
Accountants and Auditors      0.00              0.02             0.01               0.85                     0.01                     0.01                    0.02                0.02             0.05          0.00        0.01        2,710.00
 Customer Service Rep.        0.01              0.03             0.01               0.01                     0.79                     0.04                    0.01                0.01             0.07          0.01        0.01         869.00
 Marketing Professionals      0.00              0.05             0.00               0.00                     0.09                     0.74                    0.01                0.01             0.06          0.00        0.03        2,125.00
   Financial Advisors         0.00              0.00             0.00               0.00                     0.01                     0.00                    0.95                0.00             0.02          0.00        0.00        1,918.00
    HR Professionals          0.01              0.03             0.06               0.01                     0.00                     0.01                    0.02                0.68             0.14          0.01        0.02        1,434.00
      Office Clerks           0.00              0.01             0.00               0.00                     0.00                     0.01                    0.00                0.00             0.96          0.00        0.01        3,395.00
        Teachers              0.00              0.00             0.00               0.00                     0.00                     0.00                    0.00                0.00             0.00          1.00        0.00        4,135.00
      IT Support              0.00              0.15             0.00               0.00                     0.02                     0.02                    0.00                0.01             0.03          0.00        0.76        2,277.00


Notes: This table presents the correlation between occupational codes reported in the survey and those recorded in the
administrative data of Statistics Denmark. Each cell represents the probability of reporting the column occupation in the
survey, conditional on having the row occupation registered with Statistics Denmark. The average agreement rate (diagonal
elements) is 87%. Sample: All completed survey responses.




       The disagreements in Table A.5 likely reflect measurement error in the registers because

firms generally do not update occupational switches of existing employees (Groes, Kircher

and Manovskii, 2015). Furthermore, some workers may have switched jobs between June

2024 (our latest month of register data) and November 2024 (the launch of our survey).

Table A.5 shows the disagreements occur in cells that reflect likely switches, such as (IT

Support, Software Developer). By contrast, the survey and register data agree on the

occupation of 100% of our school teachers.




                                                                                                                       8
B       Adoption
B.1       Employer Initiatives

Figure B.1: The Prevalence of Employer Initiatives for AI Chatbot Adoption (Workplaces)
                                                          (a) Usage Policies
                         Marketing
                         Software Developers
                         Journalists
                         HR Professionals
                         IT Support
                         Financial Advisors
                         Customer Service
                         Accountants
                         Office Clerks
                         Legal Professionals
                         Teachers

                                               0    0.1    0.2    0.3           0.4   0.5       0.6    0.7    0.8    0.9   1
                                                     Encouraged   Allowed         Not Allowed     No Policy   Don’t Know


                                                   (b) In-House AI Chatbots
                         Marketing
                         Software Developers
                         Journalists
                                                                        1
                         HR Professionals
                         IT Support
                         Financial Advisors
                         Customer Service
                         Accountants
                         Office Clerks
                         Legal Professionals
                         Teachers

                                               0    0.1    0.2    0.3           0.4   0.5       0.6    0.7    0.8    0.9   1
                                                                            Customized      Standard


                                                   (c) Training in AI Chatbots
                         Marketing
                         Software Developers
                         Journalists
                                                                        1
                         HR Professionals
                         IT Support
                         Financial Advisors
                         Customer Service
                         Accountants
                         Office Clerks
                         Legal Professionals
                         Teachers

                                               0    0.1    0.2    0.3           0.4   0.5       0.6    0.7    0.8    0.9   1
                                                                  Firm-Arranged          Worker-Arranged

Notes: This figure shows the share of workplaces affected by various employer initiatives related to AI chatbot adoption.
Workers in our sample have been reweighted so all workplaces have the same weight. Panel (a) shows employers’ policies on
AI chatbot usage for work. Panel (b) indicates whether the employer has its own AI chatbot. Panel (c) reports whether
workers have participated in AI chatbot training courses. Sample: All completed responses from the 2024 survey.

                                                                        1




                                                                            9
             Table B.1: Which Workplaces Have Adopted AI Chatbot Initiatives?


 Panel A: Within Occupations (Table 1)
                                                                                                  Firm-Arranged   In-House
                                Encouraged    Allowed     Not Allowed   No Policy    Don’t Know      Training     Chatbot
                                   (1)          (2)           (3)          (4)           (5)           (6)           (7)
 Firm Age (10 Years)             -0.0140**     0.0030       0.0028       0.0038*       0.0044       -0.0122**     -0.0091*
                                  (0.0044)    (0.0021)     (0.0026)      (0.0016)     (0.0025)       (0.0039)     (0.0043)

 log(Firm Employment)             0.0036     -0.0082***     0.0036      -0.0195***   0.0204***       -0.0048      0.0362***
                                 (0.0048)     (0.0023)     (0.0023)      (0.0022)     (0.0029)      (0.0043)       (0.0056)

 log(Firm Labor Productivity)    0.0468**    0.0275***      0.0051      -0.0374***   -0.0420***     0.0765***     0.0697***
                                 (0.0153)     (0.0077)     (0.0051)      (0.0077)     (0.0084)       (0.0135)      (0.0176)

 Private Firm                    0.0414*       -0.0076     -0.0141*       -0.0104      -0.0092       0.0257       0.0554**
                                 (0.0168)     (0.0094)     (0.0072)      (0.0066)     (0.0096)      (0.0144)      (0.0180)
 Occupation FE’s                    ✓            ✓            ✓             ✓            ✓              ✓            ✓
 Mean of Outcome                  0.419        0.209        0.061         0.132        0.178          0.231        0.375
 Within 2                         0.013        0.003        0.009         0.016        0.016          0.010        0.042
 2
                                  0.106        0.005        0.032         0.046        0.071          0.023        0.123
 Observations                     24184        24184        24184         24184        24184          24184        24184
 Panel B: Within Occupations, Worker Controls
 Firm Age (10 Years)       -0.0135**   0.0026               0.0029       0.0039*       0.0041       -0.0119**     -0.0088*
                            (0.0045)  (0.0021)             (0.0026)      (0.0016)     (0.0025)       (0.0039)     (0.0043)

 log(Firm Employment)             0.0035     -0.0081***     0.0037      -0.0197***   0.0206***       -0.0050      0.0362***
                                 (0.0047)     (0.0023)     (0.0023)      (0.0022)     (0.0028)      (0.0043)       (0.0055)

 log(Firm Labor Productivity)    0.0415**     0.0251**      0.0051      -0.0363***   -0.0355***     0.0716***     0.0640***
                                 (0.0145)     (0.0077)     (0.0050)      (0.0077)     (0.0077)       (0.0131)      (0.0170)

 Private Firm                    0.0396*       -0.0094     -0.0140*       -0.0098      -0.0064       0.0238       0.0533**
                                 (0.0167)     (0.0092)     (0.0071)      (0.0067)     (0.0094)      (0.0144)      (0.0178)
 Worker Controls                    ✓            ✓            ✓             ✓            ✓              ✓            ✓
 Occupation FE’s                    ✓            ✓            ✓             ✓            ✓              ✓            ✓
 Mean of Outcome                  0.419        0.209        0.061         0.132        0.178          0.231        0.375
 Within R2                        0.024        0.006        0.010         0.018        0.039          0.017        0.053
 R2                               0.116        0.008        0.033         0.047        0.093          0.029        0.133
 Observations                     24184        24184        24184         24184        24184          24184        24184

Notes: This table examines which firm characteristics predict the adoption of various employer initiatives to promote AI
chatbot use. Columns (1)–(5) report results for employer usage policies, while Columns (6)–(7) report results for in-house
chatbots and firm-provided training. Firm characteristics are measured in 2021, our latest data year available. Labor
productivity is measured as value added per full-time equivalent worker. The regressions control for whether the firm reports
value added. Panel A controls for occupation fixed effects (corresponding to Table 1), whereas Panel B additionally controls
for worker characteristics. Standard errors, reported in parentheses, are clustered at the firm level. Sample: The table is
based on all completed responses from the 2024 survey that can be linked to the registry data.




                                                             10
B.2        Worker Adoption
             Figure B.2: Importance of Employer Policies in AI Chatbot Adoption

                                                (i) Usage Policy: Encouraged
                                   Ever Used                                                                    p< 0.01




                              Monthly or More                                                 p< 0.01




                              Weekly or More                                  p< 0.01




                                        Daily            p< 0.01

                                                0                   .2                       .4                .6               .8   1

                                                                          Encouraged                   Other (Non-Encouraged)



                                            (ii) Usage Policy: Not Allowed
                                   Ever Used                                                 p< 0.01




                              Monthly or More                            p< 0.01




                              Weekly or More                  p< 0.01




                                        Daily       p< 0.01

                                                0                   .2                       .4                .6               .8   1

                                                                                        Not Allowed            Other



                                                (iii) Firm-Arranged Training
                                   Ever Used                                                                        p< 0.01




                              Monthly or More                                                     p< 0.01




                              Weekly or More                                       p< 0.01




                                        Daily             p< 0.01

                                                0                   .2                       .4                .6               .8   1

                                                                               Firm-Arranged Training                  Other

Notes: This figure illustrates the impact of employer policies on workers’ use of AI chatbots. The estimates are based
on predicted values from Equation (1), varying employer initiatives (EmployerInitiative = 1 vs. EmployerInitiative = 0)
while holding workers’ characteristics X at their mean values. Panel (i) splits workers based on whether their employer
encourages AI chatbot use, Panel (ii) splits workers based on whether their employer allows AI chatbot use, and Panel (iii)
splits workers based on whether they have participated in firm-arranged AI chatbot training. Panel (i) is identical to Figure
1. Whiskers represent 95% confidence intervals. The reported p-values test whether the coefficients differ between the two
groups. Sample: All completed responses from the 2024 survey linked to registry data.




                                                                                      11
Figure B.3: Influence of Employer Initiatives on Worker Gaps in AI Chatbot Adoption
                                                                         (i) Usage Policy: Encouraged
                                  (a) Ever Used                                                                                                              (b) Daily Use

                Female                 p< 0.01                                                                                      Female                                p< 0.01



         Age (10 Years)                                  p< 0.01                                                             Age (10 Years)                                                      p= 0.094



  Experience (10 Years)                                         p= 0.255                                               Experience (10 Years)                                    p< 0.01



           log(Earnings)                                                                      p= 0.012                         log(Earnings)                                                                    p= 0.072



   Net Wealth / Earnings                                                       p= 0.032                                Net Wealth / Earnings                                                                 p= 0.044


                           -.15        -.1                    -.05                  0                  .05                                            -.08      -.06              -.04            -.02               0     .02

                                           Encouraged           Other (Non-Encouraged)                                                                          Encouraged                Other (Non-Encouraged)


                                                                        (ii) Usage Policy: Not Allowed
                                  (a) Ever Used                                                                                                              (b) Daily Use

                Female            p= 0.080                                                                                          Female                        p< 0.01



         Age (10 Years)                               p< 0.01                                                                Age (10 Years)                                               p= 0.026



  Experience (10 Years)                                   p= 0.231                                                     Experience (10 Years)                                        p< 0.01



           log(Earnings)                                                                p= 0.015                               log(Earnings)                                                                    p= 0.121



   Net Wealth / Earnings                                                p= 0.320                                       Net Wealth / Earnings                                                                p= 0.235


                           -.15      -.1               -.05                0                .05              .1                                -.06             -.04                      -.02                  0                .02

                                                      Not Allowed           Other                                                                                           Not Allowed              Other


                                                                          (iii) Firm-Arranged Training
                                  (a) Ever Used                                                                                                              (b) Daily Use

                Female                      p< 0.01                                                                                 Female                                 p= 0.038



         Age (10 Years)                                       p< 0.01                                                        Age (10 Years)                                              p= 0.257



  Experience (10 Years)                                           p< 0.01                                              Experience (10 Years)                              p= 0.196



           log(Earnings)                                                                          p= 0.034                     log(Earnings)                                                                p= 0.076



   Net Wealth / Earnings                                                       p= 0.015                                Net Wealth / Earnings                                                        p= 0.681


                           -.15            -.1                 -.05                 0                  .05                                     -.1                       -.05                            0                       .05

                                                 Firm-Arranged Training             Other                                                                              Firm-Arranged Training                Other



Notes: This figure illustrates the impact of employer initiatives on worker disparities in AI chatbot adoption. The estimates
are obtained from regressions of AI chatbot adoption on worker characteristics X, controlling for occupation fixed effects,
and are estimated separately based on employers’ AI chatbot initiatives. Panel (i) splits workers based on whether their
employer encourages AI chatbot use, Panel (ii) splits workers based on whether their employer allows AI chatbot use, and
Panel (iii) splits workers based on whether they have participated in firm-arranged AI chatbot training. For each of these,
subpanels (a) predicts whether workers have ever used AI chatbots for work, while subpanels (b) predicts whether workers
use AI chatbots daily. Panel (i) is identical to Figure 3. Whiskers represent 95% confidence intervals. The reported p-values
test whether the coefficients differ between the two groups. Sample: All completed responses from the 2024 survey linked to
registry data.




                                                                                                                  12
               Table B.2: Decomposition of Adopters’ Time Use with AI Chatbots

                                                   Time Use       Time Used Per Day Used  Days Used
                                                 / Work Hours       / Daily Work Hours   / Work Days Covariance
  Occupation                                          (1)                   (2)              (3)        (4)
  Software Developers         Encouraged              .053                  .074                 .567           .011
  Software Developers         Non-Encouraged          .033                   .06                 .378            .01
  Marketing Professionals     Encouraged              .049                  .076                 .515            .01
  Marketing Professionals     Non-Encouraged          .036                  .062                 .388           .011
  Customer Service Rep.       Encouraged              .035                  .058                 .439            .01
  Customer Service Rep.       Non-Encouraged          .014                   .04                  .24           .005
  IT Support                  Encouraged              .034                   .06                 .407           .009
  IT Support                  Non-Encouraged          .023                  .051                 .283           .008
  HR Professionals            Encouraged              .031                  .056                 .405           .009
  HR Professionals            Non-Encouraged          .016                  .049                 .237           .004
  Legal Professionals         Encouraged              .027                  .057                 .336           .007
  Legal Professionals         Non-Encouraged           .01                  .044                 .166           .003
  Journalists                 Encouraged              .025                  .048                 .374           .007
  Journalists                 Non-Encouraged          .013                  .038                 .221           .005
  Office Clerks               Encouraged              .023                  .054                 .309           .006
  Office Clerks               Non-Encouraged          .012                  .044                 .177           .004
  Accountants and Auditors    Encouraged              .018                  .044                 .282           .006
  Accountants and Auditors    Non-Encouraged          .007                  .038                 .143           .002
  Financial Advisors          Encouraged              .016                  .038                 .288           .005
  Financial Advisors          Non-Encouraged           .01                  .031                 .179           .005
  Teachers                    Encouraged              .009                  .052                  .14           .002
  Teachers                    Non-Encouraged          .005                  .043                 .088           .001
  All                         Encouraged              .029                  .056                 .369           .008
  All                         Non-Encouraged          .016                  .046                 .227           .006
Notes: This table presents workers’ time use with AI chatbots, categorized by workers’ occupations and employer policies.
The table focuses on workers who have ever used AI chatbots for work. Column (1) reports the average time used as a
percentage of total work hours. The remaining columns decompose this time use into three components: time use per day
of use (Column (2)), the share of workdays with AI chatbot usage (Column (3)), and the covariance between Columns (2)
and (3) (Column (4)). These components satisfy the relationship: Column (1) = Column (2) × Column (3) + Column (4),
which follows from the identity: E[XY ] = E[X]E[Y ] + Cov(X, Y ). We code daily time savings (Column (2)) as follows:
0–15 minutes/day as 7.5 minutes, 15–60 minutes as 37.5 minutes, and 60+ minutes as 90 minutes. We code frequency of use
(Column (3)) as follows: daily use is divided by 1; weekly use by 5 (corresponding to 5 workdays per week); monthly use by
21 23 (corresponding to 4 13 weeks per month); and use a few times by 65 (corresponding to 4 uses over 12 months). We set
daily work hours to 8, as nearly all sampled workers are full-time employees. Sample: The table is based on all completed
responses from the 2024 survey that can be linked to the registry data.




                                                             13
                               Table B.3: Who Has Adopted AI Chatbots?

                                             Ever Used    Monthly or More     Weekly or More      Daily
                                                (1)             (2)                (3)             (4)
                   Encouraged                 0.363∗∗∗         0.337∗∗∗           0.285∗∗∗       0.137∗∗∗
                                              (0.006)          (0.006)            (0.005)        (0.004)

                   Female                     -0.106∗∗∗       -0.130∗∗∗          -0.098∗∗∗      -0.041∗∗∗
                                               (0.006)         (0.006)            (0.006)        (0.004)

                   Age (10 Years)             -0.060∗∗∗       -0.051∗∗∗          -0.038∗∗∗      -0.017∗∗∗
                                               (0.004)         (0.004)            (0.003)        (0.003)

                   Experience (10 Years)      -0.040∗∗∗       -0.044∗∗∗          -0.044∗∗∗      -0.032∗∗∗
                                               (0.007)         (0.007)            (0.007)        (0.005)

                   log(Earnings)              0.043∗∗∗         0.018∗∗∗           0.011∗∗         -0.000
                                              (0.005)          (0.005)            (0.005)        (0.004)

                   Net Wealth / Earnings        0.002           -0.001             -0.001       -0.003∗∗∗
                                               (0.001)         (0.001)            (0.001)        (0.001)
                   Occupation FE’s               ✓                 ✓                 ✓              ✓
                   Mean of Outcome             0.596             0.392             0.285          0.126
                   Observations                24796             24796             24796          24796
Notes: This table compares workers within occupations and asks what characterizes those who have adopted AI chatbots
for work. The columns vary by frequency of usage. Encouraged indicates that the employer actively encourages AI chatbot
use for work (see definitions in the note of Figure 1 ). All other characteristics are based on register variables from 2022.
Experience is the years of employment in the relevant occupation. Earnings are total labor income. Net Wealth is the
sum of real assets, financial assets, and pension savings minus the sum of priority debt, other private debt, and public
debt, winsorized at the 5th and 95th percentiles. The regressions control for occupation fixed effects. Standard errors in
parentheses. Sample: The table is based on all complete responses from the 2024 survey that can be linked to the registry
data.




                                                            14
B.2.1    AI Chatbot Products

While our main analysis focuses on the adoption of any AI chatbot, our survey also

measures usage of specific products. This section provides details on product-level

adoption.

   The main takeaway is that ChatGPT remains the dominant tool. Figures B.4–B.6

show that approximately 80% of all adopters use ChatGPT, and its dominance holds

across all occupations.

   Table B.4 further reveals that users of other chatbots often multihome—that is, they

also use ChatGPT. For example, 84% of daily Gemini users also use ChatGPT daily.

An exception is Microsoft Copilot: only 39% of its daily users also use ChatGPT. Still,

this figure is substantially higher than the overall share of daily ChatGPT users in

the population (11%), suggesting that workers are generally not exclusive to a single

chatbot—those who use one are more likely to use others as well.

   Table B.5 characterizes workers’ use of AI chatbot products based on whether their

employers provide an in-house chatbot. The patterns of daily and weekly usage in Panels

(a) and (b) are especially informative about ongoing, active use. The table shows that even

customized in-house chatbots are most often versions of ChatGPT. These are typically

thin wrappers around ChatGPT Enterprise or the OpenAI API, adapted for workplace

use through features such as data security compliance, training on internal data, and

custom prompt creation.




                                            15
                            Figure B.4: The Prevalence of AI Chatbot Products


       Any AI Chatbot

       ChatGPT

       Claude

       Microsoft Copilot

       Gemini

       Perplexity

       Other


                               0         0.1         0.2         0.3         0.4         0.5         0.6      0.7      0.8     0.9   1
                                                               Daily     Weekly          Monthly           Few Times
Notes: This figure displays the share of workers who have used various AI chatbots for work, categorized by frequency of
usage. Sample: All completed responses from our 2024 survey round.

                                                           1




                                   Figure B.5: The Dominance of ChatGPT


       Marketing               Any
                               GPT
       Software Developers     Any
                               GPT
       Journalists             Any
                               GPT
       HR Professionals        Any
                               GPT
       IT Support              Any
                               GPT
                               Any
       Financial Advisors      GPT
                               Any
       Customer Service        GPT
       Accountants             Any
                               GPT
                               Any
       Office Clerks           GPT
                               Any
       Legal Professionals     GPT
                               Any
       Teachers                GPT

                                     0         0.1         0.2         0.3         0.4         0.5     0.6      0.7      0.8   0.9   1
                                                                   Daily      Weekly           Monthly       Few Times

Notes: This figure shows the share of workers in our study occupations who have used AI chatbots for work, distinguishing
between those who have used any AI chatbot and those who have specifically used ChatGPT. Sample: All completed
responses from our 2024 survey round.


                                                           1




                                                                        16
       Table B.4: Correlation Between AI Chatbot Product Usage, P (Column|Row)

                                               (a) Ever Used for Work

                         Any       ChatGPT           Claude        Copilot       Gemini        Perplexity         Other

        Any              1.00          0.82            0.04          0.45          0.09             0.04           0.19
     ChatGPT             1.00          1.00            0.05          0.39          0.10             0.05           0.17
      Claude             1.00          0.94            1.00          0.66          0.39             0.23           0.39
      Copilot            1.00          0.72            0.06          1.00          0.11             0.05           0.16
      Gemini             1.00          0.91            0.18          0.56          1.00             0.15           0.32
     Perplexity          1.00          0.90            0.22          0.56          0.32             1.00           0.36
       Other             1.00          0.73            0.08          0.39          0.15             0.08           1.00
    All Workers          0.64          0.53            0.03          0.29          0.06             0.03           0.12


                                               (b) Daily Use for Work


                         Any       ChatGPT           Claude        Copilot       Gemini        Perplexity         Other

        Any              1.00          0.69            0.03          0.36          0.03             0.02           0.13
     ChatGPT             1.00          1.00            0.03          0.20          0.04             0.02           0.07
      Claude             1.00          0.63            1.00          0.38          0.09             0.10           0.20
      Copilot            1.00          0.39            0.04          1.00          0.04             0.01           0.08
      Gemini             1.00          0.84            0.10          0.43          1.00             0.08           0.26
     Perplexity          1.00          0.66            0.14          0.22          0.10             1.00           0.20
       Other             1.00          0.38            0.05          0.21          0.06             0.04           1.00
    All Workers          0.16          0.11            0.01          0.06          0.01             0.00           0.02


Notes: This table presents the correlation between the use of different AI chatbot products. Each cell represents the
probability of using the column product, conditional on using the row product. Panel (a) reports probabilities for any
work-related use, while Panel (b) focuses on daily work-related use. All Workers reports the unconditional usage rate of the
chatbot in the given column, weighting all occupations equally. Sample: All completed survey responses from our 2024
survey round.




                                                            17
        Table B.5: AI Chatbot Product Usage by Availability of In-House Chatbots

                                               (a) Daily Use for Work

                                           Any     ChatGPT         Claude    Copilot Gemini          Perplexity Other

    Customized In-House Chatbot            0.25        0.16         0.01       0.08        0.01         0.01         0.06
     Standard In-House Chatbot             0.22        0.13         0.01       0.12        0.01         0.00         0.02
        No In-House Chatbot                0.13        0.10         0.00       0.04        0.00         0.00         0.01
               All Workers                 0.16        0.11         0.01       0.06        0.01         0.00         0.02


                                              (b) Weekly Use for Work

                                           Any     ChatGPT         Claude    Copilot Gemini          Perplexity Other

    Customized In-House Chatbot            0.52        0.36         0.02       0.18        0.02         0.02         0.14
     Standard In-House Chatbot             0.47        0.30         0.01       0.28        0.02         0.01         0.04
        No In-House Chatbot                0.29        0.24         0.01       0.10        0.01         0.01         0.02
               All Workers                 0.35        0.26         0.01       0.14        0.02         0.01         0.05


                                               (c) Ever Used for Work

                                           Any     ChatGPT         Claude    Copilot Gemini          Perplexity Other

    Customized In-House Chatbot            0.80        0.63         0.04       0.34        0.07         0.03         0.29
     Standard In-House Chatbot             0.80        0.59         0.03       0.54        0.06         0.03         0.11
        No In-House Chatbot                0.59        0.52         0.02       0.24        0.06         0.03         0.07
               All Workers                 0.64        0.53         0.03       0.29        0.06         0.03         0.12


Notes: This table reports usage rates of different AI chatbot products among adopters, split by whether their employers
offer their own in-house chatbot. Panel (a) presents daily usage rates, Panel (b) focuses on weekly usage rates, while Panel
(c) shows rate of any usage for work. Sample: All completed survey responses from our 2024 survey round.




                                                              18
B.2.2      Comparison to 2023 Survey

                       Figure B.6: Use of ChatGPT for Work (Nov ‘23, ‘24)


                      Female



             Age (10 Years)



     Experience (10 Years)



               log(Earnings)



      Net Wealth / Earnings


                                -.15             -.1             -.05              0              .05              .1

                                                                   2023        2024


Notes: This figure presents estimates from a multivariate regression of ChatGPT usage for work on worker characteristics,
controlling for occupation fixed effects. The regressions are estimated separately for the 2023 and 2024 survey rounds.
Sample: All completed responses from the 2023 and 2024 survey rounds.




                                                          19
C       Work
C.1       Benefits for Users

                  Table C.1: Perceived Benefits of AI Chatbots by Occupation

                                Time                          Job        No     Don’t
                               Savings Quality Creativity Satisfaction Benefits Know
  Occupation                     (1)    (2)       (3)         (4)        (5)     (6)
  Accountants                    .709          .524            .418              .156              .08         .059
  Customer Service               .723          .572            .413              .142             .083         .041
  Financial Adv.                 .769           .55            .488              .173             .082         .021
  HR Prof.                       .844          .638            .623              .253             .028          .03
  IT Support                      .76          .526            .423              .239             .097         .034
  Journalists                     .67          .394            .467              .126             .137         .042
  Legal Prof.                    .783          .544             .45              .204             .083         .027
  Marketing                      .898          .698            .625              .289             .023         .014
  Office Clerks                  .689          .563            .489              .185             .073         .067
  Software Dev.                  .838          .528            .446              .305             .076         .022
  Teachers                       .637          .321            .458              .132              .15         .071
Notes: This table presents the share of adopters who report various benefits from using AI chatbots for work, broken down
by occupation and by whether their employer encourages AI chatbot use. Sample: All completed responses from the 2024
survey round.




                                                          20
C.2     Workloads and Task Creation

Our survey includes free-text responses about the new tasks workers have recived due to

AI chatbots. We categorize these responses into six broad AI-related categories, listed in

Table C.2, as well as into more granular, occupation-specific subtasks.

                  Table C.2: Categories of New Tasks from AI Chatbots

 Task                            Description
 AI Ideation                     Leveraging AI to spark or expand creative ideas—such as
                                 concepts, strategies, or solutions. The human selects and
                                 builds on the most promising suggestions.
 AI Content Drafting             Using AI tools to generate initial drafts of text or media (e.g.,
                                 documents, emails, code). The human professional prompts
                                 the AI, then edits and refines the output for accuracy and
                                 tone.
 AI Quality Review               Reviewing AI-generated content for accuracy, clarity, and
                                 relevance. The human fact-checks, corrects errors, and ensures
                                 the output meets required standards.
 AI Data Insights                Using AI to analyze data or documents and surface patterns,
                                 summaries, or key insights. The human then interprets and
                                 applies these findings to decisions.
 AI Integration                  Embedding AI into workflows to automate or enhance tasks.
                                 Professionals design prompts, refine workflows, correct outputs,
                                 and fine-tune systems based on feedback.
 AI Ethics & Compliance          Ensuring AI use follows ethical, legal, and institutional stan-
                                 dards. This includes setting guidelines, monitoring for bias or
                                 misuse, and reviewing outputs for compliance.
                    Notes: This table describes our six broad categories of AI-related tasks.




   Examples of occupation-specific tasks, along with their corresponding general task

categories, include:

  1. Accountants: Brainstorming budget plans or tax strategies with AI suggestions

      (AI Ideation), Drafting financial statements and reports using AI for initial content

      (AI Content Drafting), Reviewing AI-generated financial outputs for accuracy and

                                                      21
  completeness (AI Quality Review), Analyzing financial data with AI tools to identify

  trends or anomalies (AI Data Insights), Ensuring AI-driven accounting processes

  comply with financial regulations and standards (AI Ethics & Compliance)

2. Customer Support: Using AI to draft responses to common customer queries or

  emails (AI Content Drafting), Reviewing AI-suggested responses to ensure accuracy

  and proper tone (AI Quality Review), Analyzing customer interactions with AI to

  identify common pain points and FAQs (AI Data Insights), Creating and refining

  prompts for AI chatbots to handle customer questions (AI Integration), Training

  the AI customer service chatbot by feeding it new Q&As from resolved issues (AI

  Integration), Ensuring the AI chatbot adheres to customer privacy and service

  guidelines (AI Ethics & Compliance)

3. Financial Advisors: Brainstorming investment strategies or portfolio ideas using

  AI insights (AI Ideation), Generating draft financial plans and investment recom-

  mendations with AI assistance (AI Content Drafting), Reviewing AI-suggested

  investment recommendations for accuracy and client suitability (AI Quality Review),

  Analyzing market trends and client data with AI to inform advice (AI Data Insights),

  Ensuring AI-driven financial advice complies with regulations and ethical standards

  (AI Ethics & Compliance)

4. HR Professionals: Brainstorming employee training, development, or wellness

  program ideas using AI (AI Ideation), Drafting job postings, policy documents, or

  employee communications using AI (AI Content Drafting), Reviewing AI-generated

  candidate evaluations or HR reports for accuracy and bias (AI Quality Review),

  Analyzing employee survey results or HR data with AI to gain insights (AI Data

  Insights), Integrating AI tools for resume screening, interview scheduling, and answer-

  ing candidate inquiries in recruitment (AI Integration), Ensuring AI recruitment and

  evaluation tools are fair, unbiased, and legally compliant (AI Ethics & Compliance)

                                         22
5. IT Support Specialists: Generating technical troubleshooting guides and FAQs

  using AI (AI Content Drafting), Validating AI-proposed solutions to ensure they

  resolve issues without risk (AI Quality Review), Crafting effective queries/prompts

  for AI tools to diagnose IT issues (AI Integration), Integrating AI assistants into

  support systems to automate routine help requests (AI Integration)

6. Journalists: Brainstorming story ideas, angles, or interview questions with AI (AI

  Ideation), Using AI to draft article outlines, summaries, or initial news reports (AI

  Content Drafting), Fact-checking and editing AI-generated content to ensure accuracy

  and clarity (AI Quality Review), Summarizing research materials or interview

  transcripts for quick insight with AI (AI Data Insights), Ensuring AI-generated

  content abides by journalistic ethics and standards (AI Ethics & Compliance)

7. Legal Professionals: Brainstorming legal arguments, interpretations, or negoti-

  ation strategies with AI (AI Ideation), Drafting contracts, briefs, or other legal

  documents with AI providing initial content (AI Content Drafting), Reviewing

  AI-generated legal documents or analyses for accuracy and compliance (AI Quality

  Review), Using AI to research and summarize case law, statutes, or legal documents

  (AI Data Insights), Developing organizational AI usage policies and guidelines (AI

  Integration, AI Ethics & Compliance), Ensuring AI tools and outputs uphold legal

  ethics and confidentiality (AI Ethics & Compliance)

8. Marketing Professionals: Brainstorming campaign themes, slogans, or creative

  concepts with AI (AI Ideation), Generating marketing copy, social media posts, or

  product descriptions with AI (AI Content Drafting), Reviewing AI-created marketing

  content for quality and brand consistency (AI Quality Review), Analyzing consumer

  data and campaign results with AI to derive marketing insights (AI Data Insights)

9. Office Clerks: Drafting routine emails, letters, or documents using AI assistance

  (AI Content Drafting), Performing quality control on AI-generated text and doc-

                                        23
      uments (AI Quality Review), Using AI to extract information from documents or

      summarize data for reports (AI Data Insights), Ensuring no confidential information

      is inappropriately shared with AI tools (AI Ethics & Compliance)

 10. Software Developers: Using AI to generate code snippets, boilerplate code, or

      documentation (AI Content Drafting), Reviewing and testing AI-generated code to

      ensure correctness and security (AI Quality Review), Formulating specific prompts

      to guide AI in debugging or coding tasks (AI Integration), Fine-tuning the AI coding

      assistant by providing feedback and project-specific examples (AI Integration),

      Writing prompts for code generation (AI Integration)

 11. Teachers: AI-assisted development of new course material and lesson plans (AI

      Ideation), Personalizing learning materials or feedback using AI insights from student

      performance (AI Data Insights), Adapting exams and assignments to account for

      AI tool usage (AI Integration), Integrating chatbots into lessons (AI Integration),

      Detecting AI-generated homework submissions (AI Ethics & Compliance)

For all broad categories, we include an “Other” subtask for each occupation (e.g., AI

Integration, Other) to ensure that every broad category is represented across all occupations.

In addition, we include a “non-AI” task category, which typically captures new assignments

for the worker that are not novel within the broader workplace or profession. Examples

include “meeting with customers,” “taking over tasks due to freed-up time,” or the more

ambiguous “handling more complex tasks GenAI cannot solve.”

   To categorize the free-text responses, we divided them between two independent coders.

Each coder then cross-checked a random sample of the other’s work, with near-complete

agreement.




                                             24
    Figures C.1 illustrate that AI chatbots have led to the creation of new tasks across all

11 occupations in our study. Figure C.2 shows that 50% to 95% of these tasks are directly

linked to AI use.

                                Figure C.1: Workloads from AI Chatbots

                                                     (a) Adopters

     Teachers            Encouraged
                         Baseline
     Marketing           Encouraged
                         Baseline
     Customer Service    Encouraged
                         Baseline
     Journalists         Encouraged
                         Baseline
     IT Support          Encouraged
                         Baseline
     Software Developers Encouraged
                         Baseline
     Office Clerks       Encouraged
                         Baseline
     Legal Professionals Encouraged
                         Baseline
     Accountants         Encouraged
                         Baseline
     HR Professionals    Encouraged
                         Baseline
     Financial Advisors Encouraged
                         Baseline
                                      0         0.05          0.1         0.15          0.2         0.25          0.3
                                                       Same Tasks   New Tasks    Same and New Tasks


                                                (b) Non-Adopters

     Teachers            Encouraged
                         Baseline
     Marketing           Encouraged
                         Baseline                1

     Customer Service    Encouraged
                         Baseline
     Journalists         Encouraged
                         Baseline
     IT Support          Encouraged
                         Baseline
     Software Developers Encouraged
                         Baseline
     Office Clerks       Encouraged
                         Baseline
     Legal Professionals Encouraged
                         Baseline
     Accountants         Encouraged
                         Baseline
     HR Professionals    Encouraged
                         Baseline
     Financial Advisors Encouraged
                         Baseline
                                      0         0.05          0.1         0.15          0.2         0.25          0.3
                                                       Same Tasks   New Tasks    Same and New Tasks

Notes: This figure presents the share of workers who report increased workloads due to AI chatbots, distinguishing between
additional tasks of the same type, new job tasks, or both. The responses are broken down by occupation and by whether
employers encourage AI chatbot use. Panel (a) focuses on adopters (workers who have ever used AI chatbots for work),
while Panel (b) examines non-adopters. Sample: All completed responses from the 2024 survey round linked to registry
data.

                                                 1




                                                            25
                                Figure C.2: Composition of New Job Tasks


Teachers
Journalists
Legal Professionals
Marketing Professionals
Office Clerks
HR Professionals
IT Support
Accountants
Software Developers
Financial Advisors
Customer Support

                            0       0.1      0.2      0.3        0.4    0.5      0.6       0.7      0.8      0.9       1


                                                             AI Tasks     Non-AI Tasks
Notes: This figure shows the share of new job tasks that are directly linked to AI chatbot use. Occupations are ordered
according to their shares of AI tasks Sample: All completed responses from the 2024 survey who reported new job tasks due
to AI chatbots.




                                                         1




                                                            26
D        Labor Market Outcomes
D.1       Results

D.2       Perceived Impacts

          Figure D.1: Perceived Earnings Effects of AI Chatbots Among Adopters


          Software Developers
       Marketing Professionals
        Customer Service Rep.
             Financial Advisors
                      IT Support
                   Office Clerks
     Accountants and Auditors
              HR Professionals
            Legal Professionals
                       Teachers
                      Journalists
                                    -5               -2.5              0               2.5                        5
                                                 Percent Change in Earnings (Stated by Workers)

                                                               Encouraged         Baseline


Notes: This figure displays the average perceived earnings impact of AI chatbots among adopters, categorized by workers’
occupations and whether their employers encourage AI chatbot use. Whiskers represent 95% confidence intervals. Sample:
All completed responses from the 2024 survey round linked to registry data.




                                                          27
Table D.1: Decomposition of Perceived Earnings Effects of AI Chatbots Among Adopters

                                                                 Share of Impacts           Conditional Average Impacts (in %)
                                           Average       Decreased Unchanged Increased      Decreased Unchanged Increased
                                         Impact (in %)   Earnings    Earnings    Earnings   Earnings     Earnings   Earnings
 Occupation                 Policy           (1)            (2)         (3)        (4)         (5)         (6)          (7)
 Journalists                Baseline         -.118                     .994                                 0
 Journalists                Encouraged       -.159                     .983                                 0
 Software Developers        Baseline          .092         .008        .974       .015       -12.187        0          12.5
 Software Developers        Encouraged        .428                      .96       .037                      0         11.944
 Legal Professionals        Baseline          .031                     .978                                 0
 Legal Professionals        Encouraged        .057                     .987       .009                      0         10.5
 Accountants and Auditors   Baseline            0          .004        .915       .004       -13.75         0         13.75
 Accountants and Auditors   Encouraged        .126                     .973       .015                      0          10
 Customer Service Rep.      Baseline          -.11         .013        .913                  -9.167         0
 Customer Service Rep.      Encouraged       .303                      .942       .041                      0          7.25
 Marketing Professionals    Baseline          .112                     .956       .023                      0          7.25
 Marketing Professionals    Encouraged         .37         .006        .955       .038        -16.5         0         12.422
 Financial Advisors         Baseline          .022                     .964                                 0
 Financial Advisors         Encouraged        .214                     .979       .019                      0         11.667
 HR Professionals           Baseline            0                      .964                                 0
 HR Professionals           Encouraged        .071                     .986                                 0
 Office Clerks              Baseline          .015         .002        .901       .003       -7.143         0         8.462
 Office Clerks              Encouraged        .113                     .978       .014                      0         10.403
 Teachers                   Baseline         -.007         .001        .975       .001       -9.167         0           4
 Teachers                   Encouraged        .041                     .992       .007                      0         7.188
 IT Support                 Baseline          .039         .006        .981                    -4           0
 IT Support                 Encouraged        .172                     .974        .02                      0         11.25

Notes: This table decomposes the average perceived earnings impact (in percent) of AI chatbots among adopters (Column
1) into contributions from workers reporting decreased earnings (Columns 2 and 5), unchanged earnings (Columns 3 and
6), and increased earnings (Columns 4 and 7). Responses are categorized by workers’ occupations and whether their
employers encourage AI chatbot use. Empty cells represent fewer than five individuals and are blanked out in accordance
with confidentiality rules. Sample: All completed responses from the 2024 survey round linked to registry data.




                                                             28
E        Broader Impacts
E.1        Results

  Figure E.1: Incumbent Worker Outcomes by Adoption Rates (Dynamic Diff-in-Diff)

                                   (a) Average Impacts (Dynamic Diff-in-Diff)
                  .15


                    .1


                  .05


                    0


                  -.05


                   -.1


                  -.15
                    2021m1          2021m7         2022m1          2022m7     2023m1             2023m7        2024m1

                                    log(Total Earnings) for Incumbents                  log(Total Hours) for Incumbents


                             (b) Occupation-Level Impacts (Pooled Diff-in-Diff)
                                    All
                            Journalists
                         Software Dev.
                            Legal Prof.
                          Accountants
                  Customer Service
                             Marketing
                  Financial Advisors
                              HR Prof.
                          Office Clerks
                             Teachers
                            IT Support
                                          -1                 -.5                    0                     .5                  1

                                               log(Total Earnings) for Incumbents           log(Total Hours) for Incumbents


Notes: This figure shows changes in incumbent workers’ outcomes by adoption rates, indexed to the launch of ChatGPT in
November 2022, at the workplace-occupational level. Incumbent workers are defined as those employed continuously from
January to November 2022, leading up to the arrival of ChatGPT. Adoption rates are measured as the share of employees in
a worker’s initial workplace who have used AI chatbots for work, adjusted for measurement error using the Empirical Bayes
shrinkage procedure described in Appendix G. The standard deviation of workplace adoption rates within occupations, after
shrinkage, is 20 percentage points. Panel (a) is based on the dynamic difference-in-differences specification in Equation (2),
weighted by the number of respondents at each workplace; shaded areas indicate 95% confidence intervals. Panel (b) shows
the effects separately by occupation, based on the pooled difference-in-differences specification in Equation (3), also weighted
by the number of respondents at each workplace; whiskers indicate 95% confidence intervals. Sample: All completed
responses from workplaces with at least two respondents in the 2024 survey linked to registry data.




                                                                      29
E.2       Perceived Impacts

Figure E.2: Average Effect of AI Chatbots on Earnings (Non-Users of AI Chatbots for
Work)


       Marketing Professionals
                      IT Support
            Legal Professionals
                     Journalists
        Customer Service Rep.
             Financial Advisors
                       Teachers
     Accountants and Auditors
              HR Professionals
                   Office Clerks
          Software Developers
                                   -5               -2.5              0               2.5                        5
                                                Percent Change in Earnings (Stated by Workers)

                                        Encouraged Non-Adopters             Non-Encouraged Non-Adopters


Notes: This figure shows workers’ average perceived earnings impacts from AI chatbots, broken down by their occupations
and whether employers encourage AI chatbot use. The figure focuses on workers who have not used AI chatbots for work.
Sample: All completed responses from the 2024 survey.




F       Robustness Analysis

Sections 2 and 3 examine how employer encouragement affects workers’ adoption and

benefits of AI chatbots. This section assesses the robustness of our results to potential

confounding factors. First, in Section F.1, we show that our findings are robust to

controlling for a wide range of observable firm and worker characteristics, mitigating

concerns that omitted variables drive the results. Second, in Section F.2, we compare

individual-level and coworker-wide measures of encouragement. We find strong alignment

between the two, supporting our interpretation of employer encouragement as a workplace-

level treatment.

                                                         30
F.1        Additional Controls

This section evaluates the robustness of the relationships between employer encouragement

of AI chatbots and workers’ adoption and reported benefits. We leverage the richness of

our data to examine potential confounders on both the firm and worker sides.

       On the firm side, we show that all results remain robust when controlling for firm

characteristics (Table 1), ensuring that observed differences across workplaces are not

driven by variation in firm age, size, or productivity. On the worker side, we show that

the results are similarly robust to controlling for workers’ detailed task mixes within

occupations, ensuring that the effects of employer encouragement are not merely driven

by differences in task types more amenable to AI chatbot use.31

       Table F.1 and Figure F.1 summarize these robustness checks, showing that our

estimates of the impact of employer encouragement on chatbot adoption and perceived

benefits remain virtually unchanged after accounting for firm characteristics and worker

task mixes.

       The robustness of our estimates to the inclusion of this rich set of controls provides

reassurance that observable confounders are not driving the results. Moreover, Oster

(2019) and Altonji, Elder and Taber (2005) provide conditions under which the stability

of coefficients to the inclusion of observable controls can also help rule out selection on

unobservables.
  31
    Task importances are derived from our survey, which asked workers to rate the importance of six
representative O*NET job tasks in their occupations; see Appendix J and Humlum and Vestergaard
(2025, SI6) for details.




                                                31
           Table F.1: Encouragement, Adoption, and Work (Additional Controls)

                                                   (a) Adoption (Figure 2)
                                           Ever Used        Monthly or More       Weekly or More                Daily
                                     (1)          (2)       (3)        (4)        (5)           (6)       (7)           (8)

 Encouraged                         0.365        0.347     0.337      0.321      0.283         0.268     0.136   0.129
                                   (0.006)      (0.006)   (0.007)    (0.007)    (0.006)       (0.006)   (0.005) (0.005)
 Worker characteristics controls     ✓            ✓         ✓          ✓          ✓             ✓         ✓             ✓
 Firm characteristics controls                    ✓                    ✓                        ✓                       ✓
 Worker task mix controls                         ✓                    ✓                        ✓                       ✓
                                         (b) Reported Benefits (Figure 4.(a))
                                      Time Savings           Quality                    Creativity      Job Satisfaction
                                     (1)          (2)       (3)        (4)        (5)           (6)       (7)           (8)

 Encouraged                         0.098        0.099     0.115      0.112      0.094         0.094     0.071   0.069
                                   (0.008)      (0.008)   (0.009)    (0.009)    (0.009)       (0.009)   (0.007) (0.007)
 Worker characteristics controls     ✓            ✓         ✓          ✓          ✓             ✓         ✓             ✓
 Firm characteristics controls                    ✓                    ✓                        ✓                       ✓
 Worker task mix controls                         ✓                    ✓                        ✓                       ✓
                                     (c) Allocation of Time Savings (Figure 4.(c))
                                   More of Same Tasks More of Diff. Tasks          More Breaks           More Leisure
                                     (1)          (2)       (3)        (4)        (5)           (6)       (7)           (8)

 Encouraged                         0.033        0.026     0.013      0.010      -0.008        -0.009    -0.014 -0.015
                                   (0.009)      (0.010)   (0.007)    (0.008)    (0.005)       (0.005)   (0.006) (0.006)
 Worker characteristics controls     ✓            ✓         ✓          ✓          ✓             ✓         ✓             ✓
 Firm characteristics controls                    ✓                    ✓                        ✓                       ✓
 Worker task mix controls                         ✓                    ✓                        ✓                       ✓
                            (d) New Workloads from AI Chatbots for Adopters (Figure 5.(a))
                                     Same Tasks           New Tasks        Same and New Tasks
                                     (1)          (2)       (3)        (4)        (5)           (6)

 Encouraged                         0.016        0.016     0.046      0.040      0.008         0.008
                                   (0.004)      (0.004)   (0.005)    (0.005)    (0.002)       (0.002)
 Worker characteristics controls     ✓            ✓         ✓          ✓          ✓             ✓
 Firm characteristics controls                    ✓                    ✓                        ✓
 Worker task mix controls                         ✓                    ✓                        ✓

Notes: This table presents estimates of the impact of employer encouragement on AI chatbot adoption (Panel a), the
reported benefits of adoption (Panel b), the allocation of time savings (Panel c), and new workloads resulting from chatbot
use among adopters (Panel d). Odd-numbered columns report our main estimates from Equation (1), corresponding to
the differences between the “Encouraged” and “Non-Encouraged” predicted values shown in Figures 2, 4.(a,c), and 5.(a).
Even-numbered columns report specifications where we augment controls for firms’ characteristics and workers’ detailed
task mixes. Robust standard errors are shown in parentheses. Sample: All complete responses from the 2024 survey that
can be linked to the registry data.




                                                           32
     Figure F.1: Employer Encouragement and Worker Gaps in Adoption (Figure 3)

                                             (a) Main Specification


                        Female                      p< 0.01



                Age (10 Years)                                       p< 0.01



        Experience (10 Years)                                             p= 0.255



                  log(Earnings)                                                                       p= 0.012



         Net Wealth / Earnings                                                          p= 0.032


                                  -.15              -.1                 -.05               0                .05

                                                           Encouraged            Non-Encouraged



                                            (b) Additional Controls


                        Female                             p< 0.01



                Age (10 Years)                                         p< 0.01



        Experience (10 Years)                                                         p= 0.800



                  log(Earnings)                                                                       p= 0.185



         Net Wealth / Earnings                                                             p= 0.107


                                  -.15               -.1                  -.05                   0                .05

                                                           Encouraged            Non-Encouraged


Notes: This figure illustrates the impact of employer usage policies on worker disparities in AI chatbot adoption. The
estimates are obtained from a multivariate regression of AI chatbot adoption on worker characteristics X, controlling
for occupation fixed effects, and are estimated separately based on employers’ AI chatbot initiatives (Encouraged = 1
vs. Encouraged = 0). Panel (a) presents our main specification from Figure 3, while Panel (b) adds controls for firm
characteristics (Table 1) and workers’ detailed task mixes. Whiskers represent 95% confidence intervals. The reported
p-values test whether the coefficients differ between the two groups. Sample: All completed responses from the 2024 survey
linked to registry data.




                                                            33
F.2     Coworker Encouragement

A recurring theme in our analysis is the relationship between employer encouragement

and workers’ use of AI chatbots.

   While our main analysis relies on workers’ self-reports of employer encouragement,

this section examines whether the results change when using coworker reports instead.

This helps clarify whether the estimated effects reflect workplace-level treatments or

individual-targeted interventions.

F.2.1   Empirical Strategy

To operationalize these ideas, we construct leave-one-out averages of coworkers’ reported

employer encouragement for each worker i:

                                            1       X
                     Encouragedj,−i =                        Encouragedk ,                  (4)
                                        Nj(i) − 1 k∈j(i)\i

where Nj(i) denotes the number of workers in the same workplace-occupation cell j(i) as

worker i.

   The coworker measurements are made possible by our workplace-based sampling design

(described in Section 1.5), which ensures that most respondents have coworkers who also

participated in the survey. To mitigate measurement error due to incomplete sample

coverage, we apply an empirical shrinkage procedure to the leave-out encouragement rates,

Encouragedj,−i (see Appendix G for details on this method). Importantly, our results in

Section F.2.2 are robust to using the raw leave-out means instead.

   Table F.2 shows that coworker encouragement strongly predicts an individual worker’s

own reported encouragement: the first-stage coefficient is approximately 1, with an F-

statistic of 3,645. The strong correlation in reported employer encouragement at the

workplace level supports our interpretation of these initiatives as centralized policies.




                                             34
      Table F.2: Relationship Between Self- and Coworker-Reported Encouragement

                                                                          Encouraged
                                                                             (1)
                                Coworker Encouragement (EBS)                1.181***
                                                                             (0.020)

                                Coworker Female Share                         -0.016
                                                                             (0.011)

                                Coworker Age                                  0.001
                                                                             (0.001)

                                Coworker Potential Experience                 -0.001
                                                                             (0.001)
                                Occupation FEs                                  ✓
                                F-Stat (Partial)                             3644.56
                                Observations                                  16974

Notes: This table reports the relationship between workers’ self-reported employer encouragement and those reported by
their coworkers, estimated using the specification in Equation (5). Standard errors (in parentheses) are clustered at the
workplace level. F-Stat (Partial) reports the F-statistic on the partial effect of Coworker Encouragement (EBS). Sample:
The table is based on all completed responses from workplaces with at least two respondents from the 2024 survey linked to
registry data.




    In Section F.2.2, we estimate how employer encouragement affects the impact of AI

chatbots, contrasting the effects of workers’ self-reported encouragement with those of their

coworkers’. To ensure the effects are measured on comparable scales, and not attenuated

by measurement error, we present 2SLS estimates for the impact of coworker-reported

employer encouragement:


                          Encouragedi = π ′ Xj,−i + α × Encouragedj,−i + ε1i                                          (5)

                                        Yi = γ ′ Xj,−i + β ×   \
                                                             Encouragedi + ε2i ,                                      (6)


where Xj,−i denotes the leave-one-out mean of the characteristics X of worker i’s coworkers.

Table F.2 reports estimates of Equation (5).


                                                           35
F.2.2   Results

Adoption and Work. Table F.3 and Figure F.2 compare the effects of self- and coworker-

reported employer encouragement on AI chatbot adoption and associated benefits. The

results broadly align, but with interesting differences.

   The impact of coworker-reported encouragement on adoption (Panel (a)) is 1.5–2

times larger than the effect of self-reported encouragement. Furthermore, Figure F.2.(b)

shows that coworker encouragement can entirely eliminate the gender gap in AI chatbot

adoption. By contrast, coworker encouragement has a more muted effect on reported

benefits among adopters (Panel (b)). For example, self-reported encouragement increases

the share of workers reporting time savings by 10 percentage points, whereas the effect

of coworker encouragement is only 5.3 percentage points. Finally, Panel (d) shows that

coworker encouragement has roughly twice the effect of self-reported encouragement on

the creation of new tasks among adopters, as compared to the effects shown in Figure 5.

   Taken together, these results suggest that workplace-wide encouragement (captured by

coworker reports) significantly boosts chatbot adoption and leads to broader organizational

changes that induce task creation. However, individual-level benefits—such as perceived

time savings—appear more sensitive to whether workers personally feel encouraged, as

measured by self-reports.




                                            36
       Table F.3: Encouragement, Adoption, and Work (Own vs. Coworker Reports)

                                                    (a) Adoption
                         Ever Used              Monthly or More              Weekly or More                  Daily
                     Own           CWs          Own          CWs           Own           CWs           Own         CWs
                      (1)           (2)          (3)          (4)          (5)            (6)           (7)         (8)
  Encouraged        0.363         0.725         0.337        0.640        0.285          0.506         0.137      0.228
                   (0.007)       (0.022)       (0.007)      (0.022)      (0.007)        (0.021)       (0.005)    (0.017)
                                                 (b) Reported Benefits
                        Time Savings                 Quality                    Creativity            Job Satisfaction
                     Own           CWs          Own          CWs           Own           CWs           Own         CWs
                      (1)           (2)          (3)          (4)          (5)            (6)           (7)         (8)
  Encouraged        0.100         0.053         0.116        0.090        0.091          0.088         0.071      0.026
                   (0.008)       (0.031)       (0.009)      (0.033)      (0.009)        (0.031)       (0.007)    (0.025)
                                     (c) Allocation of Time Savings
                   More of Same Tasks More of Diff. Tasks        More Breaks                            More Leisure
                     Own           CWs          Own          CWs           Own           CWs           Own         CWs
                      (1)           (2)          (3)          (4)          (5)            (6)           (7)         (8)
  Encouraged        0.031         0.035         0.016        0.037        -0.007         -0.016        -0.011     -0.010
                   (0.009)       (0.035)       (0.007)      (0.024)      (0.005)        (0.016)       (0.006)    (0.019)
                              (d) New Workloads from AI Chatbots (Adopters)
                         Same Tasks         New Tasks       Same and New Tasks
                     Own           CWs          Own          CWs           Own           CWs
                      (1)           (2)          (3)          (4)          (5)            (6)
  Encouraged        0.016         0.018         0.045        0.106        0.008          0.014
                   (0.004)       (0.012)       (0.006)      (0.021)      (0.002)        (0.008)

 Notes: This table presents estimates of the impact of employer encouragement on: AI chatbot adoption (Panel a), reported
 benefits of adoption (Panel b), the allocation of time savings (Panel c), and new workloads resulting from chatbot use among
 adopters (Panel d). Odd-numbered columns (“Own”) show the impact of self-reported encouragement, estimated using
 the specification in Equation (1). Even-numbered columns (“CWs”) show the impact of coworker-reported encouragement,
 estimated using the specifications in Equations (5)–(6). The “Own” coefficients correspond to the difference between
“Encouraged” and “Non-Encouraged” predicted values shown in Figures 2, 4.(a,c), and 5.(a), respectively. Standard errors
(in parentheses) are clustered at the workplace level. Sample: “Own” columns use all complete responses from the 2024
 survey that can be linked to registry data. “CWs” columns include complete responses from workplaces with at least two
 linked respondents in the 2024 survey.




                                                            37
Figure F.2: Encouragement and Worker Gaps in Adoption (Own vs. Coworker Reports)

                                                (a) Main Specification


                        Female                       p< 0.01



                Age (10 Years)                                      p< 0.01



        Experience (10 Years)                                             p= 0.255



                  log(Earnings)                                                                              p= 0.012



         Net Wealth / Earnings                                                             p= 0.032


                                  -.15               -.1                -.05                  0                      .05

                                                           Encouraged          Non-Encouraged



                                         (b) Coworker Encouragement

                        Female                                      p< 0.01




                Age (10 Years)                                                  p= 0.194




        Experience (10 Years)                                                   p= 0.050




                  log(Earnings)                                                                           p= 0.493




          Net Wealth/Earnings                                                                     p= 0.558

                                         -.15               -.1                -.05                   0                    .05

                                             Encouraged Coworkers              Non-Encouraged Coworkers


Notes: This figure presents the impact of coworker encouragement on worker disparities in AI chatbot adoption. The
estimates are obtained from a multivariate regression of AI chatbot adoption on worker characteristics X, controlling for
occupation-fixed effects, and all interacted with an indicator for employer encouragement. In Panel (b), we instrument these
interaction effects using the corresponding interactions with our coworker encouragement variable. The point estimates
show predicted adoption rates for an average worker, X̄, when Encouraged = 0 or 1, respectively. Whiskers denote 95%
confidence intervals. Reported p-values test whether the coefficients differ between the two groups. Sample: All completed
responses from the 2024 survey linked to registry data.




                                                            38
Labor Market Outcomes. Figure F.3 revisits our analysis of how employer encour-

agement affects individual labor market outcomes, this time using coworker reports to

measure encouragement. The results confirm that employer encouragement policies have

had no measurable impact on workers’ labor market outcomes.

    A key takeaway from our earlier analysis is that the modest labor market effects are

partly explained by weak pass-through from time savings to labor earnings—though pass-

through is somewhat stronger when employers actively encourage chatbot use. Table F.4

replicates this result using coworker reports to measure encouragement. Pass-through

remains modest (ranging from 2% to 6%) but is approximately three times higher when

employers are reported to encourage chatbot use.

 Figure F.3: Have Encouragements Affected Workers’ Outcomes? (Coworker Reports)

                       All
             Journalists
          Software Dev.
             Legal Prof.
            Accountants
     Customer Service
              Marketing
     Financial Advisors
                HR Prof.
           Office Clerks
               Teachers
              IT Support
                             -.25             -.15               -.05             .05               .15              .25

                                                           log(Income)         log(Hours)


Notes: This figure presents the differential labor market outcomes of workers who are encouraged to use AI chatbots by their
employers, compared to all other workers, indexed to the launch of ChatGPT in November 2022. The figure is based on
the pooled difference-in-differences specification in Equation (3), with whiskers representing 95% confidence intervals. The
estimates come from a 2SLS specification where we instrument all effects of Encouraged using the corresponding coworker
encouragement rates described in Section F.2.1. Sample: All completed responses from the 2024 survey linked to registry
data.




                                                            39
Table F.4: Pass-Through of Time Savings to Earnings (Own vs. Coworker Encouragement)

                                                      Baseline              Encouraged
                                                   Own      CWs            Own     CWs
                                                    (1)      (2)            (3)     (4)
                          Pass-through rate        0.031          0.018   0.066          0.059
                                                  (0.005)        (0.032) (0.003)        (0.016)

Notes: This table reports estimates of the pass-through rate from workers’ perceived time savings due to AI chatbots to
their perceived earnings impacts. Estimates are reported separately based on whether employers encourage chatbot use
(Encouraged = 0 or 1). The “Own” coefficients correspond to the slopes of the best-fit lines in Figure 11. The “CWs”
estimates instrument Encouraged using the coworker encouragement rates described in Section F.2.1. Sample: The table is
based on all complete responses from the 2024 survey that can be linked to the registry data.




G        Empirical Bayes Shrinkage

We estimate workplace rates of adoption and encouragement using Empirical Bayes

shrinkage with a Beta-Binomial model; see Walters (2024) for a detailed introduction to

Empirical Bayes methods. The shrinkage is performed separately for each occupation,

allowing underlying adoption rates to vary systematically across occupations.

    We assume the adoption rate at each workplace, pi , follows a Beta prior:


                            xi | pi ∼ Binomial(ni , pi ),           pi ∼ Beta(α0 , β0 ).                          (7)


The Beta prior captures workplace-level variation. We estimate α0 , β0 via Method of

Moments, matching the Beta distribution’s first two moments to observed data:

                                         m                    m          2
                                      1 X   xi             1 X   xi
                                                                                 
                                                        2
                                 p̄ =          ,       s =          − p̄ .                                        (8)
                                      m i=1 ni             m i=1 ni

From the Beta mean and variance formulas:

                                           p̄(1 − p̄)                        1 − p̄
                                   α0 =               − 1,         β0 = α0          .
                                               s2                              p̄




                                                            40
With these, we compute the posterior mean:

                                                            α 0 + xi
                                          E[pi | xi ] =                .
                                                          α0 + β0 + ni

This shrinks estimates toward the overall mean, especially for small ni .


G.1             Workplace Adoption Rates

Figure G.1 compares the raw and adjusted distributions of workplace adoption rates, while

Table G.1 presents summary statistics for the adjusted rates of workplaces. The typical

standard deviation within occupations is 20 percentage points. Notably, our results in

Section 5.2 remain robust when using the raw workplace adoption rates instead.


                     Figure G.1: Workplace Adoption Rates (Raw vs. Shrinkage)

            5



            4



            3


  Density
                                                                                           Raw Adoption Rate
                                                                                           EBS Adoption Rate
            2



            1



            0
                 0         .2           .4           .6           .8            1


Notes: This figure compares the raw and adjusted distributions of workplace adoption rates. The adjusted estimates are
derived using an Empirical Bayes shrinkage procedure, as described in Section G. Sample: All completed responses from
our 2024 survey round linked to registry data.




                                                          41
             Table G.1: Workplace Adoption Rates (Empirical Bayes Shrinkage)

                                                               p25    p50    p75    sd
                                Journalists                    0.71   0.83   0.83   0.14
                                Software Developers            0.90   0.90   0.93   0.12
                                Legal Professionals            0.28   0.70   0.70   0.24
                                Accountants                    0.25   0.25   0.73   0.24
                                Customer Service Rep.          0.27   0.50   0.74   0.24
                                Marketing Professionals        0.97   0.97   0.97   0.19
                                Financial Advisors             0.29   0.48   0.65   0.21
                                HR Professionals               0.54   0.92   0.92   0.30
                                Office Clerks                  0.31   0.38   0.63   0.18
                                Teachers                       0.51   0.63   0.69   0.13
                                IT Support                     0.58   0.88   0.88   0.22
                                All                            0.51 0.68     0.79   0.20
Notes: This table presents summary statistics for the adjusted distributions of workplace adoption rates, categorized by
occupation. The adjusted estimates are derived using an Empirical Bayes shrinkage procedure, as described in Section G.
Sample: All completed responses from our 2024 survey round linked to registry data.




G.2        Coworker Encouragement Rates

Figure G.2 compares the raw and adjusted distributions of coworker encouragement rates,

while Table G.2 presents summary statistics for the adjusted rates of workplaces. The

typical standard deviation within occupations is 17 percentage points. Importantly, our

results in Section F.2.2 remain robust when using the raw coworker encouragement rates

instead.




                                                          42
                      Figure G.2: Coworker Encouragement Rates (Raw vs. Shrinkage)

            4




            3




  Density
                                                                               Encouraged, Leave One Out
            2
                                                                               EBS Encouraged, Leave One Out




            1




            0
                  0        .2     .4        .6         .8          1


Notes: This figure compares the raw and adjusted distributions of coworker encouragement rates. The adjusted estimates
are derived using an Empirical Bayes shrinkage procedure, as described in Section G. Sample: All completed responses from
our 2024 survey round linked to registry data.




                Table G.2: Coworker Encouragement Rates (Empirical Bayes Shrinkage)

                                                                 p25    p50    p75    sd
                                 Journalists                     .414   .457    .58   .138
                                 Software Developers              .53    .68   .768    .16
                                 Legal Professionals             .092   .178   .465    .23
                                 Accountants                     .289   .409   .555   .181
                                 Customer Service Rep.           .291   .358   .466   .116
                                 Marketing Professionals         .607   .823   .869    .18
                                 Financial Advisors              .196    .35   .605   .237
                                 HR Professionals                .289   .509   .737   .244
                                 Office Clerks                   .232    .31   .448   .149
                                 Teachers                        .116   .157   .243    .11
                                 IT Support                      .359    .48   .593   .162
                                 All                             .310 .428     .575   .173
Notes: This table presents summary statistics for the adjusted distributions of coworker encouragement rates, categorized
by occupation. The adjusted estimates are derived using an Empirical Bayes shrinkage procedure, as described in Section G.
Sample: All completed responses from our 2024 survey round linked to registry data.




                                                            43
H         Theoretical Framework

Sections 2 and 3 examine how employer initiatives are associated with workers’ adoption

of AI chatbots and the benefits reported by users. In this section, we introduce a simple

theoretical framework to interpret these empirical patterns. We posit a Roy (1951) style

selection model of chatbot adoption, in which employer initiatives may shift both the costs

and benefits of adoption. We use the model to analyze how these shifts affect workers’

adoption decisions and the benefits they report from using the tools.


H.1        Setup

Worker i derives benefits Bi from using AI chatbots:


                                         Bi = αb + βb × i,                                         (9)


where individuals i ∼ U([0, 1]) are drawn uniformly from the unit interval and sorted

by their individual benefits, such that βb ≤ 0. While we assume linear functional forms

for analytical simplicity, our predictions also hold under more general monotonicity

assumptions.32

       The worker also incurs a cost Ci of adopting chatbots:


                                         Ci = αc + βc × i,                                        (10)


where βc ≥ 0 if workers who benefit more from AI also face lower adoption costs.33
  32
     The key assumption underlying the predictions in Section H.2 is that adoption exhibits positive
selection on benefits (Bi ), meaning that employer encouragement induces adoption among workers with
marginally lower idiosyncratic benefits (i.e., higher i).
  33
     A common finding from RCTs is that AI chatbots tend to yield greater benefits for less experienced
(and thus typically younger) workers (Brynjolfsson, Li and Raymond, 2025; Dell’Acqua et al., 2023; Noy
and Zhang, 2023). If these workers also find it easier to adopt new tools, then βc ≥ 0.




                                                  44
H.2     Predictions

We conceptualize employer encouragement E ∈ {0, 1} as shifting workers’ costs and

benefits of using AI chatbots through the parameters αc and αb :


                                       α = α0 + α1 E.                                   (11)


Figure H.1 illustrates these shifts; formal derivations are provided in the paragraphs below.


Adoption rates. Figure 2 shows how employer encouragement is associated with greater

chatbot adoption by workers. In the Roy model outlined above, workers adopt AI chatbots

if their perceived benefits exceed the associated adoption costs (Bi ≥ Ci ). The resulting

adoption rate is given by:

                                                 αb − αc
                                      i∗ (E) =           ,                              (12)
                                                 βc − βb

where 0 < αb − αc < βc − βb , corresponding to the empirically relevant case in which

adoption rates lie between 0 and 1.

   Equation (12) implies that employer initiatives which raise benefits (αb ) or reduce

adoption costs (αc ) increase adoption, with stronger effects when βc − βb is small—i.e.,

when workers are relatively homogeneous in their net benefits of using AI chatbots.

   In this light, the fact that employer encouragement in Figure 2 is associated with a

doubling of adoption rates suggests that these employer initiatives are powerful relative to

the amount of individual heterogeneity in net benefits.


Benefits for users. Figure 4 shows that employer encouragement is associated with

greater average benefits reported by users. The average benefit among users is:


                     B̄(E) = E[Bi (α) | i ≤ i∗ (α)] = γαc + (1 − γ)αb ,                 (13)



                                             45
where γ = 2(βbβ−β
               b
                 c)
                    ≥ 0. Equation (13) provides two key insights about how employer

encouragement relates to reported user benefits.

   First, employer initiatives that reduce adoption costs (αc ) lower the average benefit

among users due to a selection effect: lower costs induce adoption by workers with lower

idiosyncratic benefits (i.e., higher i). This negative selection effect, γ, is stronger when

workers are more homogeneous in their net benefits from using AI chatbots (i.e., when

βc − βb is small, so that employer initiatives generate larger increases in adoption; cf.

Equation (12)) but more heterogeneous in their gross benefits from the tools (i.e., when βb

is large in absolute value, implying that marginal users have lower idiosyncratic benefits).

   Second, employer initiatives that increase benefits (αb ) have two offsetting effects

on average reported benefits. On the one hand, a higher αb directly raises each user’s

individual benefit Bi . On the other hand, it expands adoption, drawing in users with

lower idiosyncratic benefits (i.e., higher i), thereby triggering the same negative selection

effect as a reduction in αc . The net effect of an increase in αb on the average reported

benefits among users B̄ is positive if and only if γ < 1. This condition is more likely to

hold when workers are relatively homogeneous in their gross benefits from the tools Bi

but more heterogeneous in their adoption costs Ci .

   In summary, the average reported benefits among users provide a lower bound on the

causal effect of employer encouragement on individual benefits, due to the presence of

a negative selection effect. In this light, the fact that Figure 4 shows higher reported

benefits among users in encouraged settings is striking. It suggests two things: (i) employer

encouragement primarily raises perceived benefits (αb ), as reductions in adoption costs (αc )

would only generate the negative selection effect; and (ii) the employer-induced increases

in benefits outweigh the adverse selection effect—implying that employer initiatives are

powerful relative to degree of individual heterogeneity (γ < 1).




                                             46
Figure H.1: The Impact of Employer Initiatives on Adoption Rates and Reported Benefits
                                                     (a) Lower Costs



                                                                                                         Costs0

          B̄0

          B̄1

                                                                                                         Costs1




                                                                                                         Benefits0


                                      i∗0                            i∗1


                                                  (b) Higher Benefits




          B̄1
                                                                                                         Costs0

          B̄0




                                                                                                         Benefits1




                                                                                                         Benefits0
                                      i∗0                 i∗1

Notes: This figure illustrates how employer initiatives affect adoption rates (i∗ ) and average reported benefits among users
(B̄). Panel (a) shows the impact of initiatives that reduce adoption costs (αc ), while Panel (b) depicts the impact of
initiatives that enhance benefits (αb ). Lower adoption costs (αc ) unambiguously increase adoption rates and reduce average
reported benefits due to a negative selection effect. In contrast, initiatives that raise benefits (αb ) also increase adoption,
but their impact on average reported benefits is theoretically ambiguous and, at most, equal to their individual-level effect.



                                                                47
H.3     Discussion

The preceding section examines the implications of workers self-selecting into chatbot

adoption based on their individual benefits. Beyond this margin of selection, at least two

additional forms of selection may be at play.

   First, firms that choose to encourage chatbots may be the ones with the greatest

benefits from the tools—even absent any encouragement initiatives—introducing potential

reverse causality between employer encouragement and reported benefits. In the framework

above, this corresponds to E being positively related to α0b . Second, employers may target

their encouragement toward employees who are expected to benefit the most individually.

This would resemble a “rotation” of the cost and benefit schedules in Figure H.1, rather

than simple vertical shifts.

   Section F addresses both of these additional selection margins empirically. First,

Section F.1 examines whether employers select into encouragement based on their un-

derlying benefits from chatbot use. We show that the effects of encouragement remain

robust when controlling for a range of firm- and worker-level characteristics, including firm

age, size, and productivity, as well as workers’ detailed task mixes and other attributes.

These robustness checks show that the association between employer encouragement and

reported benefits is not driven by observable confounders.

   Second, Section F.2 implements a “coworker encouragement” design, using the average

encouragement reported by a worker’s colleagues to measure workplace-wide encourage-

ment rates. Because coworker encouragement rates capture only workplace-level variation,

this approach helps address potential bias arising from employers targeting encouragement

toward individual employees with the highest idiosyncratic benefits. As shown in Table F.3

and Figure F.2, the findings remain largely robust when using coworker encouragement as

the source of variation.



                                             48
I    Invitation Letter

This section includes the invitation letter for our survey. We sent three reminders: two

via email (Digital Post) and one via text message (SMS).

    The section below focuses on our 2024 survey round. The invitation letter for the 2023

round follows the same format and is documented in Humlum and Vestergaard (2025).

    The English translation begins on page 50, followed by the original Danish version on

page 52.




                                            49
                        Invitation Letter – English Translation




                                                                                      November 2024


Artificial intelligence and your job tasks
Dear [name]

Statistics Denmark is inviting you to participate in a research project about AI chatbots and your
job tasks. You can participate by clicking the link below and completing the questionnaire.
AI chatbots use artificial intelligence to read and write text. You have been selected because
you work in an occupation where AI chatbots may be relevant.
Your responses are important for research on new technology in the labor market. Everyone
who completes the questionnaire will automatically participate in a lottery with a prize of
[X,XXX] DKK tax-free.
Statistics Denmark is conducting the survey on behalf of researchers at the University of Copen-
hagen and the University of Chicago. The questionnaire takes about 10 minutes to complete.



                               Start the survey [url]


Or access www.dst.dk/ditsvar and enter your response code [code].


Statistics Denmark handles your data confidentially. Results are presented in a way that pre-
vents individual answers from being identified, and the data is used solely for statistical and sci-
entific purposes.
Participation is voluntary. If you do not wish to participate, you can indicate this here: [re-
fusal_link]
If you have any questions, you can e-mail info@dstsurvey.dk or call on 7777 7708 (every day be-
tween 9am and 4pm). Please provide your response code when contacting us.


Best regards,

Marie Fuglsang                                          Anders Humlum
Head of Division, DST Survey                            Assistant Professor, University of Chicago




                                                 50
                        Invitation Letter – English Translation




Information about Statistics Denmark’s surveys and your rights


Who is invited to Statistics Denmark’s surveys?
Anyone residing in Denmark may be invited to participate in one of Statistics Denmark’s sur-
veys. Participants are randomly selected. Our surveys aim to reflect the opinions and attitudes
of the entire population, across gender, age, education, and place of residence.


Why is Statistics Denmark allowed to contact you?
Statistics Denmark can use its statistical production and related activities to carry out tasks un-
der the rules for revenue-financed activities. This is stipulated in §1, section 3, no. 5, of the Act
on Statistics Denmark.


How do we process your information?

The responses you provide in the survey are handled in accordance with the European Gen-
eral Data Protection Regulation (GDPR) and the Danish Data Protection Act.

The University of Copenhagen is the data controller for this survey. You can read more about
the data controller and find contact information here: https://informationssikker-
hed.ku.dk/persondatabeskyttelse/publikation-af-videnskab/

Statistics Denmark is the data processor and is responsible for data collection on behalf of the
data controller.

Your responses will only be used for statistical and scientific purposes in this survey. Your an-
swers will be deleted or archived in accordance with applicable laws when they are no longer
needed for the study.

You can read more about how we process your data at: https://www.dst.dk/privatlivspolitik-i-
en-frivillig-undersoegelse.

If you have any other questions regarding the processing of your personal data, you are wel-
come to contact Statistics Denmark’s Data Protection Officer at databeskyttelse@dst.dk.




                                                 51
                           Invitation Letter – Danish Version




                                                                                      November 2024




Kunstig intelligens og dine arbejdsopgaver
Kære [navn]

Danmarks Statistik inviterer dig til at deltage i et forskningsprojekt om AI chatbots og dine ar-
bejdsopgaver. Du deltager ved at klikke på nedenstående link og svare på spørgeskemaet.
AI chatbots bruger kunstig intelligens til at læse og skrive tekst. Du er blevet udvalgt til at del-
tage i denne undersøgelse, fordi du arbejder i et erhverv, hvor det kan være relevant at bruge AI
chatbots.
Dine svar er vigtige for forskning i ny teknologi på arbejdsmarkedet. Alle der gennemfører spør-
geskemaet, deltager automatisk i lodtrækningen om en præmie på [X.XXX] kr. skattefrit.
Danmarks Statistik gennemfører spørgeskemaet for forskere på Københavns Universitet og Uni-
versity of Chicago. Det tager ca. 10 minutter at besvare spørgeskemaet.


                           Start undersøgelsen [url]


Eller gå ind på www.dst.dk/ditsvar og tast svarkoden [kode]

Danmarks Statistik behandler dine svar fortroligt. Vi formidler resultaterne på en måde, så in-
gen kan se, hvad den enkelte har svaret og data anvendes alene til statistiske og videnskabelige
formål.
Det er frivilligt at deltage. Ønsker du ikke at deltage, kan du tilkendegive det: [refusal_link]
Har du spørgsmål, kan du skrive til info@dstsurvey.dk eller ringe på tlf. 7777 7708 (alle dage ml.
kl. 9-16). Oplys venligst din svarkode ved henvendelse.


Med venlig hilsen

Marie Fuglsang                                          Anders Humlum
Kontorchef, DST Survey                                  Adjunkt, University of Chicago




                                                 52
                          Invitation Letter – Danish Version




Information om Danmarks Statistiks undersøgelser og dine rettigheder


Hvem bliver inviteret til Danmarks Statistiks undersøgelser?
Alle, der har bopæl i Danmark, har mulighed for at blive inviteret til at deltage i en af Dan-
marks Statistiks undersøgelser. Udvælgelse af personer til undersøgelsen sker tilfældigt. I vo-
res undersøgelser er det vigtigt at kende meninger og holdninger fra hele befolkningen på
tværs af køn, alder, uddannelse og bopæl.

Hvorfor må Danmarks Statistik kontakte dig?
Danmarks Statistiks kan bruge den statistiske produktion og afledte aktiviteter til at udføre
opgaver efter reglerne for indtægtsdækket virksomhed. Det følger af § 1, stk. 3, nr. 5, i lov om
Danmarks Statistik.


Hvordan behandler vi oplysninger om dig?
De svar, du afgiver ved deltagelse i spørgeskemaundersøgelsen, bliver behandlet i overens-
stemmelse med reglerne i den europæiske databeskyttelsesforordning (GDPR) og den danske
databeskyttelseslov.
Københavns universitet er dataansvarlig for undersøgelsen. Du kan læse mere om den dataan-
svarlige og finde kontaktoplysninger her: https://informationssikkerhed.ku.dk/persondatabe-
skyttelse/publikation-af-videnskab/
Danmarks Statistik er databehandler og står for dataindsamlingen på vegne af den dataan-
svarlige.
Dine svar bruges udelukkende til statistiske og videnskabelige formål i denne undersøgelse.
Dine svar slettes eller arkiveres efter gældende lovgivning, når oplysningerne ikke længere har
et formål i undersøgelsen.
På linket https://www.dst.dk/privatlivspolitik-i-en-frivillig-undersoegelse kan du læse mere
om, hvordan vi behandler oplysninger om dig.
Har du andre spørgsmål til behandling af dine personoplysninger, er du velkommen til at kon-
takte Danmarks Statistiks databeskyttelsesrådgiver på databeskyttelse@dst.dk




                                               53
J     Survey Questionnaire

This section contains our survey questionnaire. The questionnaire follows a common

structure for the different occupations but with job tasks and titles tailored to each specific

occupation.

    For the sake of brevity, the questionnaire below focuses on one occupation (journalism),

listing one of their six job tasks (write commentaries, columns, or scripts).

    The section below focuses on our 2024 survey round. The survey questionnaire for

the 2023 round follows a similar format and is documented in Humlum and Vestergaard

(2025).

    The English translation starts on page 55, with the original Danish version on page 60.




                                              54
                           Survey Questionnaire – English Translation

1. Introduction
AI chatbots use artificial intelligence to read and write text. You have been selected to participate in this
survey because you work in a profession where AI chatbots may be relevant.
Your participation is important regardless of your knowledge of chatbots or artificial intelligence.

                                      Block 1: Occupation and tasks
2.a Occupation
Are you employed in [journalism]?
    • Yes
    • No

2.b Occupation [if 2.a=’No’]
Are you employed in one of the following areas?
If you are employed in multiple areas, please select your primary work area.
     • HR work
     • IT support
     • Office and secretarial work
     • Customer support
     • Legal work
     • Marketing
     • Auditing and accounting work
     • Software development
     • Teaching
     • Financial consulting
     • I am not employed in any of the above work areas

3. Task Importance [if 2.b!= ’I am not employed in any of the above work areas’; all tasks]
We will first ask about some typical work tasks among [journalists].
For each task, please assess how important the task is for your work.
Extremely important means that the task is critical for performing your current job.
[Write commentaries, columns, or scripts]
    • Not important
    • Slightly important
    • Important
    • Very important
    • Extremely important




                                                     55
                            Survey Questionnaire – English Translation

                                             Block 2: Adoption
4. Awareness of AI chatbots
AI chatbots use artificial intelligence to read and write text. We will now ask about your experiences
with AI chatbots.
Had you heard of the following chatbots before this survey?
Mark all tools you had heard of before this survey.
    • ChatGPT (developed by OpenAI)
    • Claude (developed by Anthropic)
    • Copilot (developed by Microsoft)
    • Gemini (developed by Google)
    • Perplexity (developed by Perplexity AI)
    • Other AI chatbots
    • Had not heard of AI chatbots before this survey

5. Prior Use of AI Chatbots [if 4 = ’Yes’]
Have you used the following AI chatbots?
[ChatGPT / Claude / Copilot / Gemini / Perplexity / Other AI chatbots]
    • Yes, only for work
    • Yes, only for leisure
    • Yes, for work and leisure

6.a Purposes of Prior Use [if 5=’Yes, only for leisure’ or ’Yes, for work and leisure’]
How often have you used the following AI chatbots for leisure?
[ChatGPT / Claude / Copilot / Gemini / Perplexity / Other AI chatbots]
    • Never
    • A few times
    • Monthly
    • Weekly
    • Daily

6.b Purposes of Prior Use [if 5=’Yes, only for work or ’Yes, for work and leisure’]
How often have you used the following AI chatbots for work?
[ChatGPT / Claude / Copilot / Gemini / Perplexity / Other AI chatbots]
    • Never
    • A few times
    • Monthly
    • Weekly
    • Daily




                                                      56
                           Survey Questionnaire – English Translation

6.c Purposes of Prior Use [if 5=’Yes, only for work or ’Yes, for work and leisure’ for any option]
Have you used an AI chatbot to perform the following work tasks?
    • [Job task 1-6]
    • None of the above

7. Time use on AI chatbots [if 5=’Yes, only for work or ’Yes, for work and leisure’ for any option]
Think back to the days when you used AI chatbots for your work. How much time did you spend using AI
chatbots on average?
     • Less than 15 minutes per day
     • Between 15 minutes and an hour per day
     • More than an hour per day

8. Paid subscription [if 5=’Yes, only for work or ’Yes, for work and leisure’ for ‘ChatGPT’]
Do you have an active Plus subscription for ChatGPT?
    • Yes
    • No

                                       Block 3: Employer Initiatives
9. Employer policies
What is your employer’s policy regarding the use of AI chatbots?
    • Allowed and encouraged
    • Allowed but not encouraged
    • Not allowed
    • No policy
    • Don't know

10. In-house AI chatbot
Does your workplace have its own AI chatbot?
    • Yes, a custom-designed product
    • Yes, a standard product
    • No
    • Don't know

11.a Training courses
Have you participated in courses on using AI chatbots?
    • Yes
    • No

11.b Training courses [if 11.a = ’Yes’]
Was your AI chatbot course organized by your employer?
    • Yes
    • No


                                                     57
                            Survey Questionnaire – English Translation

                                       Block 4: Effects of AI chatbots
12. Benefits from AI chatbots
Have you experienced any of these benefits from using AI chatbots in your work?
Please select all that apply.
    • Saved time at work
    • Improved work quality
    • Increased creativity
    • Higher job satisfaction
    • Have not experienced benefits
    • Don't know

13. Time savings from AI chatbots [if 12=’Saved time at work’]
Think back to the days when you used AI chatbots for your work. How much time did you save using AI
chatbots on average?
    • Less than 15 minutes per day
    • Between 15 minutes and an hour per day
    • More than an hour per day

14.a Earnings impact of AI chatbots
Have AI chatbots affected how much you earn today?
    • I earn more today as a result of AI chatbots
    • AI chatbots have not affected my income
    • I earn less today as a result of AI chatbots

14.b Earnings impact of AI chatbots [if 14.a=’ I earn more today as a result of AI chatbots‘]
How much have AI chatbots increased your earnings?
    • Under 5 percent
    • Between 5 and 15 percent
    • Over 15 percent

14.c Earnings impact of AI chatbots [if 14.a=’ I earn less today as a result of AI chatbots‘]
How much have AI chatbots reduced your earnings?
    • Under 5 percent
    • Between 5 and 15 percent
    • Over 15 percent




                                                     58
                            Survey Questionnaire – English Translation

15. Allocation of time savings from AI chatbots
If AI chatbots save time on a task, do you expect to:
     • Complete more of the same tasks
     • Spend more time on other tasks
     • Take more breaks
     • Take more leisure time

16. Workloads from AI chatbots
Do you find that AI chatbots have increased your workload?
    • Yes, more of the same job tasks
    • Yes, new types of job tasks
    • No

17. New job tasks [if 16=’Yes, new types of job tasks’]
What types of new tasks have you experienced after using AI chatbots?
    • [open text field]

18. End of survey
Thank you for participating in the survey.
If you win one of the prizes, you will be notified directly in your e-Boks.




                                                     59
                              Survey Questionnaire – Danish Version

1. Introduction
AI chatbots bruger kunstig intelligens til at læse og skrive tekst. Du er blevet udvalgt til at deltage i
denne undersøgelse, fordi du arbejder i et erhverv, hvor det kan være relevant at bruge AI chatbots.
Din deltagelse er vigtig uanset dit kendskab til chatbots eller kunstig intelligens.

                                        Block 1: Occupation and tasks
2.a Occupation
Er du beskæftiget med [journalistik]?
    • Ja
    • Nej

2.b Occupation [if 2.a=’Nej’]
Er du beskæftiget inden for et af følgende områder?
Hvis du er beskæftiget indenfor flere områder, vælg da dit primære arbejdsområde.
    • HR-arbejde
    • IT-support
    • Kontor- og sekretærarbejde
    • Kundesupport
    • Juridisk arbejde
    • Marketing
    • Revisions- og regnskabsarbejde
    • Softwareudvikling
    • Undervisning
    • Økonomisk rådgivning
    • Jeg er ikke beskæftiget inden for ovenstående arbejdsområder

3. Task Importance [if 2.b!= ’Jeg er ikke beskæftiget inden for ovenstående arbejdsområder’; all tasks]
Vi vil først spørge ind til nogle typiske arbejdsopgaver blandt [journalister].
Til hver opgave bedes du vurdere, hvor vigtig opgaven er for dit arbejde.
Ekstremt vigtig betyder, at opgaven er kritisk for varetagelsen af dit nuværende job.
[Skrive kommentarer, klummer eller artikler]
     • Ikke vigtig
     • Lidt vigtig
     • Vigtig
     • Meget vigtig
     • Ekstremt vigtig




                                                     60
                                 Survey Questionnaire – Danish Version

                                                Block 2: Adoption
4. Awareness of AI chatbots
AI chatbots bruger kunstig intelligens til at læse og skrive tekst. Vi vil nu spørge ind til dine erfaringer
med AI chatbots.
Havde du hørt om følgende chatbots før denne undersøgelse?
Markér alle værktøjer, du havde hørt om før denne undersøgelse.
    • ChatGPT (udviklet af OpenAI)
    • Claude (udviklet af Anthropic)
    • Copilot (udviklet af Microsoft)
    • Gemini (udviklet af Google)
    • Perplexity (udviklet af Perplexity AI)”
    • Andre AI chatbots
    • Havde ikke hørt om AI chatbots før denne undersøgelse

5. Prior Use of AI Chatbots [if 4 = ’Ja’]
Har du benyttet følgende AI chatbots?
[ChatGPT / Claude / Copilot / Gemini /Perplexity / Andre AI chatbots]
    • Ja, kun til arbejde
    • Ja, kun til fritid
    • Ja, til arbejde og fritid

6.a Purposes of Prior Use [if 5=’Ja, kun til fritid’ or ’Ja, til arbejde og fritid’]
Hvor ofte har du benyttet følgende AI chatbots til fritid?
[ChatGPT / Claude / Copilot / Gemini /Perplexity / Andre AI chatbots]
    • Aldrig
    • Et par gange
    • Månedligt
    • Ugentligt
    • Dagligt

6.b Purposes of Prior Use [if 5=’Ja, kun til arbejde or ’Ja, til arbejde og fritid’]
Hvor ofte har du benyttet følgende AI chatbots til arbejde?
[ChatGPT / Claude / Copilot / Gemini /Perplexity / Andre AI chatbots]
    • Aldrig
    • Et par gange
    • Månedligt
    • Ugentligt
    • Dagligt




                                                         61
                                Survey Questionnaire – Danish Version

6.c Purposes of Prior Use [if 5=’Ja, kun til arbejde or ’Ja, til arbejde og fritid’ for any option]
Har du benyttet en AI chatbot til at udføre følgende arbejdsopgaver?
    • [Arbejdsopgave 1-6]
    • Ingen af ovennævnte

7. Time use on AI chatbots [if 5=’Ja, kun til arbejde or ’Ja, til arbejde og fritid’ for any option]
Tænk tilbage på de dage, hvor du har brugt AI chatbots til dit arbejde. Hvor meget tid brugte du med AI
chatbots i gennemsnit?
     • Mindre end 15 minutter per dag
     • Mellem 15 minutter og en time per dag
     • Mere end en time per dag

8. Paid subscription [if 5=’Ja, kun til arbejde or ’Ja, til arbejde og fritid’ for ’ChatGPT’]
Har du et aktivt Plus-abonnement på ChatGPT?
    • Ja
    • Nej

                                         Block 3: Employer Initiatives
9. Employer policies
Hvad er din arbejdsgivers politik ift. brugen af AI chatbots?
    • Tilladt og tilskyndet
    • Tilladt men ikke tilskyndet
    • Ikke tilladt
    • Ingen politik
    • Ved ikke

10. In-house AI chatbot
Har din arbejdsplads sin egen AI chatbot?
    • Ja, et specialdesignet produkt
    • Ja, et standardprodukt
    • Nej
    • Ved ikke

11.a Training courses
Har du deltaget i kurser om brugen af AI chatbots?
    • Ja
    • Nej

11.b Training courses [if 11.a = ’Ja’]
Var dit kursus i AI chatbots arrangeret af din arbejdsgiver?
    • Ja
    • Nej


                                                        62
                              Survey Questionnaire – Danish Version

                                      Block 4: Effects of AI chatbots
12. Benefits from AI chatbots
Har du oplevet nogle af disse fordele ved brugen af AI chatbots i dit arbejde?
Markér gerne flere
    • Sparet tid i arbejdet
    • Forbedret kvalitet af arbejdet
    • Øget kreativitet
    • Højere arbejdsglæde
    • Har ikke oplevet fordele
    • Ved ikke

13. Time savings from AI chatbots [if 12=’Sparet tid i arbejdet’]
Tænk tilbage på de dage, hvor du har brugt AI chatbots til dit arbejde. Hvor meget tid sparede AI
chatbots dig i gennemsnit?
    • Mindre end 15 minutter per dag
    • Mellem 15 minutter og en time per dag
    • Mere end en time per dag

14.a Earnings impact of AI chatbots
Har AI chatbots påvirket hvor meget du tjener i dag?
    • Jeg tjener mere i dag som følge af AI chatbots
    • AI chatbots har ikke påvirket min indtjening
    • Jeg tjener mindre i dag som følge af AI chatbots

14.b Earnings impact of AI chatbots [if 14.a=’ Jeg tjener mere i dag som følge af AI chatbots’]
Hvor meget har AI chatbots øget din indtjening?
    • Under 5 procent
    • Mellem 5 og 15 procent
    • Over 15 procent

14.c Earnings impact of AI chatbots [if 14.a=’ Jeg tjener mindre i dag som følge af AI chatbots’]
Hvor meget har AI chatbots reduceret din indtjening?
    • Under 5 procent
    • Mellem 5 og 15 procent
    • Over 15 procent




                                                    63
                              Survey Questionnaire – Danish Version

15. Allocation of time savings from AI chatbots
Hvis AI chatbots sparer tid i løsningen af en opgave, forventer du så, at
    • Løse flere af samme opgaver
    • Bruge mere tid på andre opgaver
    • Tage flere pauser
    • Tage mere fritid

16. Workloads from AI chatbots
Oplever du, at AI chatbots har øget din arbejdsmængde?
    • Ja, flere af de samme arbejdsopgaver
    • Ja, nye slags arbejdsopgaver
    • Nej

17. New job tasks [if 16=’Ja, nye slags arbejdsopgaver’]
Hvilke slags nye arbejdsopgaver oplever du at have fået efter brugen af AI chatbots?
    • [Fritekstfelt]

17. End of survey
Mange tak for at deltage i undersøgelsen.
Hvis du vinder en af præmierne, vil du få direkte besked i din e-Boks.




                                                    64
