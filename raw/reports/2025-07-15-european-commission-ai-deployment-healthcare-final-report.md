---
title: "Study on the deployment of AI in healthcare: Final report"
authors: ["PwC EU Services EEIG", "Open Evidence"]
publisher: "European Commission, Directorate-General for Health and Food Safety (DG SANTE); Publications Office of the European Union"
date_published: 2025-07-15
doi: "10.2875/2169577"
isbn: "978-92-68-28758-3"
catalogue_number: "EW-01-25-076-EN-N"
url: "https://op.europa.eu/en/publication-detail/-/publication/9ddf7bf8-62bf-11f0-bf4e-01aa75ed71a1/language-en"
mirror_url: "https://medicaldevices.ipn.pt/wp-content/uploads/2025/08/Final-Report.pdf"
attachment: 2025-07-15-european-commission-ai-deployment-healthcare-final-report.pdf
licence: "CC BY 4.0"
fulltext_source: pdf-converted
converter: pdftotext -layout
notes: |
  Fetched 2026-11-07. The DOI 10.2875/2169577 resolves to the Publications Office record above
  (datePublished 2025-07-15; "Manuscript completed in June 2025"; study period January 2024 - May 2025).
  The PDF was downloaded from the Publications Office's own download handler (identifier
  9ddf7bf8-62bf-11f0-bf4e-01aa75ed71a1, format pdf, language en). The mirror cited in the trigger report
  (medicaldevices.ipn.pt) was also fetched: same 241 pages, same creation date (2025-07-03), different file
  hash, and pdftotext output byte-identical to the official copy. The official copy is the one kept.
  A second OP record with DOI 10.2875/7784225 (EW-01-25-077-3A-N) exists; probably another language or
  summary version; not read.
  241-page A4 PDF. TOC ends at Annex 11 (Monitoring framework, printed p. 220 = PDF p. 228); the PDF runs to p. 241 with the back cover, so the file is complete.
  Printed page numbers = PDF page index minus 8 (e.g. printed p. 41 = PDF p. 49). Many odd pages carry
  no extracted footer number, so count by the TOC.
  Charts are flattened by pdftotext; verify chart-level numbers against the PDF.
  Written by PwC EU Services EEIG and Open Evidence for DG SANTE (Unit C.1 Digital Health; contact Yiannos
  Tolias). The cover states the views are the authors' and not the Commission's.
  Known slip in the source: p. 10 (PDF p. 18) says the surveys "closed on the 25th September 2025", which
  cannot be right for a June 2025 manuscript; 2024 is meant.
---

                   Study on the deployment of
                        AI in healthcare
                                                         Final report




      Written by PwC EU Services EEIG and Open Evidence
      For the Directorate General For Health and Food Safety
      January 2024 – May 2025
for



                                                               DG SANTE
EUROPEAN COMMISSION

Directorate General For Health and Food Safety
Directorate C – Digital, EU4Health and Health Systems Modernisation
Unit C.1 – Digital Health

Contact: Yiannos Tolias
E-mail: Yiannos.Tolias@ec.europa.eu/ SANTE-CONSULT-C1@ec.europa.eu

European Commission
B-1049 Brussels
LEGAL NOTICE

This document has been prepared for the European Commission however it reflects the views only of the authors, and the
European Commission is not liable for any consequence stemming from the reuse of this publication. More information on
the European Union is available on the Internet (http://www.europa.eu).




 PDF       ISBN: 978-92-68-28758-3               doi: 10.2875/2169577                 EW-01-25-076-EN-N



Manuscript completed in June 2025

Luxembourg: Publications Office of the European Union, 2025
© European Union, 2025




The reuse policy of European Commission documents is implemented by the Commission Decision 2011/833/EU of 12
December 2011 on the reuse of Commission documents (OJ L 330, 14.12.2011, p. 39). Except otherwise noted, the reuse
of this document is authorised under a Creative Commons Attribution 4.0 International (CC-BY 4.0) licence
(https://creativecommons.org/licenses/by/4.0/). This means that reuse is allowed provided appropriate credit is given and
any changes are indicated.

For any use or reproduction of elements that are not owned by the European Union, permission may need to be sought
directly from the respective rightsholders.
                                                        Deployment of AI in healthcare – Final Report


Table of contents


1     Abstract ...................................................................................................... 2
2     Introduction ................................................................................................ 5
3     Methodology................................................................................................ 5

    3.1      Task 1: Literature review ....................................................................... 6
    3.2      Task 2: Consultation Activities ................................................................ 7
      3.2.1       Exploratory interviews and workshop ................................................. 7
      3.2.2       Stakeholder Mapping ....................................................................... 8
      3.2.3       Surveys ........................................................................................10
      3.2.4       Interviews .....................................................................................12
      3.2.5       Workshops (regulatory and hospital) ................................................12
      3.2.6       Case studies ..................................................................................13
    3.3      Task 3: Analysis ...................................................................................14
      3.3.1       Preliminary findings workshop .........................................................14
      3.3.2       Market analysis ..............................................................................15
    3.4      Task 4: Monitoring framework ...............................................................15
    3.5      Limitations of this study ........................................................................16
4     Potential of AI to address healthcare needs ....................................................17

    4.1   Potential of AI to address challenges related to the increase in healthcare
    demand ........................................................................................................19
    4.2   Potential of AI to address challenges related to the growing administrative
    burden .........................................................................................................21
    4.3   Potential of AI to address challenges related to delayed diagnoses and
    treatment .....................................................................................................22
    4.4   Potential of AI to improve cancer care .....................................................24
      4.4.1       Screening, early detection and diagnosis ...........................................24
      4.4.2       Treatment planning and delivery ......................................................26
      4.4.3       Clinical decision support ..................................................................27
      4.4.4       Equity and access to care ................................................................27
    4.5   Potential of AI to harness large amounts of health data .............................28
    4.6   Potential of AI to address challenges related to the widening disparities and
    access to healthcare .......................................................................................28
    4.7   Summary ............................................................................................30
5     Current EU regulatory landscape ...................................................................31

    5.1      Key EU regulatory frameworks for AI deployment in healthcare ..................31
      5.1.1    Cross-Sector Regulations ................................................................31
      5.1.2    Healthcare-specific legal acts ...........................................................31
      5.1.3    Artificial Intelligence Act (AIA) .........................................................32
      5.1.4    Medical Device Regulation (MDR) and In-Vitro Diagnostic Medical Devices
      Regulation (IVDR) .......................................................................................34
      5.1.5    Product Liability Directive (PLD) .......................................................35
      5.1.6    Health Technology Assessment Regulation (HTAR) .............................35
      5.1.7    European Health Data Space (EHDS) ................................................36
    5.2      EU regulatory ecosystem and the path to AI deployment in healthcare ........36
6     Current state of deployment of AI in healthcare in the EU ................................37
    6.1    Research of AI/ML-enabled medical devices in clinical practice ...................37
    6.2    Development of AI/ML-enabled medical devices in clinical practice .............38
    6.3    Deployment of AI/ML-enabled medical devices in clinical practice ...............40
7    Challenges and accelerators to AI deployment and use in healthcare .................47

    7.1    Technological and data challenges and accelerators ..................................47
     7.1.1      Data standardisation and interoperability ..........................................48
     7.1.2      IT infrastructure .............................................................................52
     7.1.3      Local AI performance ......................................................................55
     7.1.4      Post-deployment monitoring and maintenance ...................................58
     7.1.5      Transparency and explainability .......................................................60
     7.1.6      High-level overview of the EU regulatory landscape ............................62
     7.1.7      Summary ......................................................................................65
    7.2    Legal and regulatory challenges and accelerators .....................................65
     7.2.1      Complex regulatory landscape .........................................................65
     7.2.2      Data security and privacy ................................................................66
     7.2.3      Liability .........................................................................................68
     7.2.4      High-level overview of the EU regulatory landscape ............................69
     7.2.5      Summary ......................................................................................71
    7.3    Organisational and business challenges and accelerators ...........................72
     7.3.1      Financing mechanisms ....................................................................72
     7.3.2      End-user involvement .....................................................................74
     7.3.3      Local Added Value Assessment (real-world local added value) ..............77
     7.3.4      AI strategy ....................................................................................80
     7.3.5      High-level overview of the EU regulatory landscape ............................86
     7.3.6      Summary ......................................................................................87
    7.4    Social and cultural challenges and accelerators ........................................87
     7.4.1      Trust ............................................................................................87
     7.4.2      Digital health literacy ......................................................................89
     7.4.3      Job security and overreliance on AI ..................................................93
     7.4.4      Doctor-patient relationship ..............................................................95
     7.4.5      High-level overview of the EU regulatory landscape ............................95
     7.4.6      Summary ......................................................................................97
    7.5    Challenges faced by generative AI systems .............................................97
8    Future Considerations ................................................................................ 100

    8.1    Considerations to facilitate the deployment of AI in healthcare ................. 100
     8.1.1    Establishing common standards for data governance and interoperability
              101
     8.1.2    Establishing centres of excellence for AI in healthcare ....................... 102
     8.1.3    Consolidated funding and introduction of financing mechanisms ......... 103
     8.1.4    Local performance testing; local real-world added-value assessment and
     post-deployment monitoring....................................................................... 104
     8.1.5    Development of a catalogue of AI solutions in healthcare .................. 105
     8.1.6    Summary .................................................................................... 106
    8.2    Monitoring framework for considerations for future actions. ..................... 106
9 Conclusions .............................................................................................. 108
10  Annexes ............................................................................................... 110

    10.1      Annex 1 – Analytical framework ........................................................ 110
                                                 Deployment of AI in healthcare – Final Report


10.2      Annex 2 – Survey questionnaires ...................................................... 114
 10.2.1     Patient Survey ............................................................................. 114
 10.2.2     Healthcare Professional Survey ...................................................... 117
 10.2.3     Hospital Representative Survey ...................................................... 124
 10.2.4     AI Developer Survey ..................................................................... 131
 10.2.5     Regulatory Expert Survey .............................................................. 136
10.3      Annex 3 – Interview guides .............................................................. 140
 10.3.1     Targeted interview questions for AI developers ................................ 140
 10.3.2     Targeted interview guide for HCPs and hospital representatives ......... 143
 10.3.3     Interview Guide - Case studies....................................................... 147
10.4      Annex 4 – Synopsis report ................................................................ 149
 10.4.1     Current and future needs in clinical practice that AI can/will address .. 149
 10.4.2     Impact of AI in clinical practice ...................................................... 151
 10.4.3     Areas where the use of AI has the greatest transformative potential ... 153
 10.4.4     State of deployment of AI in healthcare .......................................... 156
 10.4.5     Challenges and accelerators to AI deployment in healthcare .............. 157
 10.4.6     Impact of the current regulatory landscape ..................................... 174
 10.4.7     Considerations for future actions at EU level to support AI deployment
            177
 10.4.8     Conclusions ................................................................................. 181
10.5      Annex 5 – Details on data sources and methodology for market analysis 183
 10.5.1     Research ..................................................................................... 183
 10.5.2     Development ............................................................................... 185
 10.5.3     Deployment ................................................................................. 187
 10.5.4     Overall data limitations and challenges ........................................... 191
10.6      Annex 6 – List of specific actions for each consideration for future action 193
10.7      Annex 7 – Triage Use Case – Case Study 1 ......................................... 194
 10.7.1     Overview of the need .................................................................... 194
 10.7.2     Overview of the use case .............................................................. 195
 10.7.3     Challenges to Deployment ............................................................. 195
 10.7.4     Accelerators to Deployment ........................................................... 197
 10.7.5     Complementary Actions ................................................................ 199
10.8      Annex 8 – Administrative Use Case – Case Study 2 ............................. 200
 10.8.1     Overview of the need .................................................................... 200
 10.8.2     Overview of the use case .............................................................. 201
 10.8.3     Challenges to Deployment ............................................................. 201
 10.8.4     Accelerators to Deployment ........................................................... 203
 10.8.5     Complementary Actions ................................................................ 206
10.9      Annex 9 – Cancer Treatment Use Case – Case Study 3 ........................ 206
 10.9.1     Overview of the need .................................................................... 207
 10.9.2     Overview of the use case .............................................................. 208
 10.9.3     Challenges to Deployment ............................................................. 209
 10.9.4     Accelerators to Deployment ........................................................... 210
 10.9.5     Complementary Actions ................................................................ 212
10.10     Annex 10 – Cancer Detection Use Case – Case Study 4 ........................ 212
 10.10.1       Overview of the need ................................................................. 213
 10.10.2       Overview of the use case ........................................................... 214
 10.10.3       Challenges to Deployment .......................................................... 214
 10.10.4     Accelerators to Deployment ........................................................ 216
 10.10.5     Complementary Actions ............................................................. 218
10.11   Annex 11 – Monitoring framework ..................................................... 220
‘The information and views set out in this report are those of the author(s) and do not
necessarily reflect the official opinion of the Commission. The Commission does not
guarantee the accuracy of the data included in this study. Neither the Commission nor any
person acting on the Commission’s behalf may be held responsible for the use which may
be made of the information contained therein.’




                                                                                        1
                                            Deployment of AI in healthcare – Final Report


1     Abstract
Present day healthcare systems face several complex challenges, including rising demand
due to an aging population, increasing prevalence of chronic and complex conditions, rising
costs, and shortages in the healthcare workforce. Artificial intelligence (AI) has the
potential to address some of these by improving operational efficiency, reducing
administrative burdens, and enhancing diagnosis and treatment pathways. Despite the
promise and availability AI-based tools in the market, their deployment in clinical practice
is slow.

Using a mixed methods approach, entailing a literature review and consultation activities,
the study identifies a range of challenges to AI deployment in healthcare, spanning
technological and data-related issues, legal and regulatory complexities, organisational
and business challenges, and social and cultural barriers. It also highlights successful
strategies (accelerators) employed by hospitals globally to overcome these common
obstacles, offering valuable inspiration in the broader European Union (EU) context.

The EU is uniquely positioned to support the safe, effective, ethical and equitable scale-up
of AI deployment in healthcare, balancing the need to nurture innovation with
safeguarding the fundamental rights of patients. This report presents considerations for
future action and proposes a monitoring and indicators framework that could enable
progress to be tracked with the view of enabling the sustainable integration of AI into
healthcare systems.
Abstrakt
Die heutigen Gesundheitssysteme stehen vor mehrerlei komplexen Herausforderungen,
darunter die steigende Nachfrage aufgrund einer alternden Bevölkerung, die zunehmende
Prävalenz chronischer und komplexer Erkrankungen, steigende Kosten und ein Mangel an
Arbeitskräften im Gesundheitswesen. Künstliche Intelligenz (KI) hat das Potenzial, einige
dieser Herausforderungen zu bewältigen, unter anderem durch die Verbesserung
operativer Effizienz, die Einschränkung von Verwaltungslasten und die Fortentwicklung
von Diagnosen- und Behandlungswegen. Trotz des vielversprechenden Potenzials und der
Verfügbarkeit von KI-basierten Instrumenten auf dem Markt erfolgt der Einsatz von KI in
der klinischen Praxis nur langsam.

Diese Studie stellt, anhand von einer Mischung aus Literaturrecherche und
Konsultationstätigkeiten, eine Reihe von Herausforderungen für den Einsatz von KI im
Gesundheitswesen dar. Diese Herausforderung umfassen, unter anderem, technologische
und datenbezogene Aspekte, rechtliche und regulatorische Komplexität, organisatorische
und geschäftliche Herausforderungen sowie soziale und kulturelle Barrieren. Darüber
hinaus hebt die Studie erfolgreiche Strategien (Beschleuniger) hervor, die von
Krankenhäusern weltweit eingesetzt werden, um diese Hindernisse zu überwinden, und
die im breiteren Kontext der Europäischen Union (EU) wertvolle Inspiration anbieten.

Die EU ist in einer einzigartigen Position, um die sichere, wirksame, ethische und gerechte
Einsatzverbreitung von KI im Gesundheitswesen zu unterstützen und dabei ein
Gleichgewicht zwischen der Notwendigkeit, Innovationen zu fördern, und gleichermaßen
das Grundrecht der Patienten zu schützen. Diese Studie liegt Überlegungen für künftige
Maßnahmen hervor, sowohl auch als ein Überwachungs- und Indikatorrahmen, der es
ermöglichen könnte, die Fortschritte zu verfolgen, um die nachhaltige Integration von KI
in die Gesundheitssysteme zu ermöglichen.




                                                                                          3
                                             Deployment of AI in healthcare – Final Report


Résumé
Les systèmes de santé en place sont confrontés à des défis complexes, parmi lesquels,
l'augmentation de la demande de soins due au vieillissement de la population, la
prévalence croissante des maladies chroniques et complexes, l'augmentation des coûts et
la pénurie de main-d'œuvre dans le secteur des soins de santé. L'intelligence artificielle
(IA) a le potentiel de répondre à certains de ces défis en améliorant l'efficacité
opérationnelle, en réduisant les charges administratives et en améliorant les parcours de
diagnostic et de traitement. Malgré les promesses et la disponibilité sur le marché d'outils
basés sur l'IA, leur déploiement dans la pratique clinique est lent.

À l'aide d'une approche méthodologique mixte, composée d’une analyse documentaire et
d’activités de consultation, l'étude identifie une série de défis liés au déploiement de l'IA
dans les soins de santé, couvrant les questions technologiques, les questions liées aux
données, les complexités juridiques et réglementaires, les défis organisationnels et
commerciaux, et les barrières sociales et culturelles. L’étude met également en évidence
les stratégies efficaces (accélérateurs) employées par les hôpitaux du monde entier pour
surmonter ces obstacles communs, offrant ainsi une inspiration précieuse dans le contexte
plus large de l'Union européenne (UE).

L'UE est particulièrement bien placée pour soutenir l'expansion sécurisée, efficace,
éthique et équitable du déploiement de l'IA dans les soins de santé, en conciliant la
nécessité de favoriser l'innovation et la sauvegarde des droits fondamentaux des
patients. Ce rapport présente des considérations pour l'action future et propose un cadre
de suivi et d'indicateurs susceptibles de permettre un suivi des progrès réalisés, en vue
d’une possible intégration durable de l'IA dans les systèmes de soins de santé.
2       Introduction
It is widely accepted that European healthcare systems are currently grappling with
significant challenges, raising concern over their long-term sustainability. The proportion
of the population aged 65 and above has increased from 16% in 2000 to over 21% in
2023, with projections indicating a further rise to nearly 30% by 2050. Coupled with the
consideration that 40% of EU citizens aged 65 and above live with at least two chronic
conditions – this demographic shift is likely to translate into increasing demand for
healthcare services1. The World Health Organisation (WHO) projects that the EU will
experience a shortage of 4.1 million healthcare workers by 20302, translating into a
constrained supply of healthcare. In addition to the abovementioned hurdles, inequalities
in healthcare between EU countries and within EU countries persist with an estimated cost
of 980 billion per year as a result of lower productivity and higher healthcare and welfare
costs3. Innovative solutions are needed in order to improve healthcare delivery, optimise
resource allocation, and enhance patient outcomes 4.

Artificial Intelligence (AI) has emerged as a promising tool to help address such challenges.
An AI system, as defined in the EU AIA, refers to a machine-based system that is designed
to operate with varying levels of autonomy and that may exhibit adaptiveness after
deployment, and that, for explicit or implicit objectives, infers, from the input it receives,
how to generate outputs such as predictions, content, recommendations, or decisions that
can influence physical or virtual environments 5. It has the potential to transform various
aspects of healthcare, from early diagnosis and personalised treatment plans to
operational efficiencies and administrative support. AI applications may analyse vast
amounts of data, speed up processes, and offer insights that could enhance clinical
decision-making and streamline routine tasks, potentially helping healthcare systems
manage resources more effectively and meet the needs of diverse patient populations.
Despite the potential of AI solutions, there are various challenges and barriers hindering
the effective deployment of AI tools in healthcare in the EU. Such challenges and barriers
highlight the importance of a structured approach to AI deployment, addressing
technological, social, legal, and organisational challenges.

The objective of the study was to identify the current and future needs in clinical practice
that AI could address, the potential of AI to transform healthcare (with a particular focus
on cancer and delivery of healthcare in remote areas) and assess the most prominent
sector-specific challenges and accelerators, both present today as well as the ones that
may emerge in the future, for the successful deployment of AI in healthcare. The study
aimed to provide recommendations on how these gaps can be addressed, drawing
inspiration from all EU 27 Member States and relevant third countries where the
deployment of AI in healthcare is advanced, such as the USA, Israel and Japan.

3       Methodology
The methodological approach for this study on the deployment of AI in healthcare adopted
a comprehensive and mixed-methods framework across several tasks to ensure a nuanced


1 OECD (2024) Health at a Glance: Europe 2024
2 Zapata T, Muscat N.A et al (2023) From Great Attrition to Great Attraction: Countering the Great Resignation
of Health and Care Workers.
3 Forster T, Kentikelenis A et al (2018) Health Inequalities in Europe: Setting the Stage for Progressive Policy
Action
4 EIT Health (2020) Transforming Healthcare with AI – The Impact on the Workforce and Organisations.
5 Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down
harmonised rules on artificial intelligence and amending Regulations (EC) No 300/2008, (EU) No 167/2013,
(EU) No 168/2013, (EU) 2018/858, (EU) 2018/1139 and (EU) 2019/2144 and Directives 2014/90/EU, (EU)
2016/797 and (EU) 2020/1828 (Artificial Intelligence Act)



                                                                                                               5
                                                  Deployment of AI in healthcare – Final Report


and multi-dimensional analysis. A detailed description of the methodological approach
across each of the tasks is described in the following sections.


    3.1     Task 1: Literature review
Task 1 aimed to review existing literature on the deployment of AI in healthcare,
identifying key challenges, barriers, and best practices. This process involved a structured
search and screening strategy to ensure the inclusion of the most relevant and up-to-date
sources for further analysis. As a first step, a literature review was conducted on the 3rd
of June 2024 using multiple databases, including Google Scholar, PubMed, and Web of
Science. The search aimed to identify relevant publications on the deployment of AI in
healthcare, using the search terms described in Box 1.

                         Box 1: Search terms for the literature review

 ("artificial intelligence" OR "machine learning" OR "AI" OR "deep learning" OR
 "neural networks" OR “natural language processing” OR “language models” OR
 “chatbot”) AND ("deploy*" OR "adopt*" OR "application*" OR “use”) AND ("healthcare"
 OR "clinical practice" OR “hospital”) AND ("challenge*" OR "barrier*" OR
 "obstacle*" OR “issue*” OR "best practice*" OR "success").

                                     Source: Authors’ elaboration

A total of 14,407 articles were retrieved. To refine the results and ensure only the most
relevant literature were further analysed, the inclusion and exclusion criteria outlined in
Table 1 were applied.

                 Table 1: Inclusion and exclusion criteria for literature review.
 Criteria         Inclusion             Exclusion            Rationale
                                                             Review articles provide a
                  Review,
 Type of                                Any other article    comprehensive summary of
                  Systematic
 publication                            type                 existing research, highlighting key
                  review
                                                             concepts, findings, and gaps.
                  Articles                                   To ensure the validity of the
                  published                                  content and gather information on
 Publication                            Articles published
                  between                                    the most recent and relevant
 year                                   prior to 2019
                  January 2019                               challenges, barriers, and
                  and June 2024                              accelerators.
                  English               Any language other   English is the official language of
 Language
                  language              than English         research articles.
                                                             Searching for open access or
                                                             freely available literature will
                  Open access,          Articles behind a    ensure that the proposed
 Accessibility
                  freely available      paywall              methodology can be replicated in
                                                             the future without any access
                                                             issues.
                                     Source: Author’s elaboration


To further refine the search results, the titles and abstracts of the remaining articles were
manually reviewed. This process was supported by the machine-learning software
ASReview, which works by employing active learning by iteratively selecting the most
informative documents for human review. This process helped prioritise documents that
were most likely relevant to the research question, and reduced the time and effort
required for manual screening.
To complement the review of academic and scientific literature, relevant “grey” literature
sources6 were identified via a traditional web search in Google using the possible
combinations of keywords described above. We focused on sources published in the last 5
years (2019-2024) in consideration of recent technological advancements and the
changing regulatory landscape to capture the most up-to-date perspective. The screening
process is detailed in Figure 1.

                                        Figure 1: PRISMA Diagram




                                       Source: Author’s elaboration


Following the screening process, information from the 237 sources was collected in a data
extraction sheet structured along the study questions to ensure all relevant information
were captured in a consistent and comparable manner. Between June 2024 and November
2024, additional relevant literature was identified, with 119 more sources reviewed and
incorporated into the analysis, bringing the total number of sources to 356.

     3.2     Task 2: Consultation Activities
Task 2 aimed to gather in-depth insights from stakeholders through exploratory
interviews, targeted interviews, surveys, workshops, and case studies.

3.2.1 Exploratory interviews and workshop

Prior to conducting the literature review initial exploratory consultation activities were
conducted with key stakeholders. The aim of these exploratory interviews was to improve
the understanding of the study questions and context, to identify additional data sources
and information, and to refine the methodological approach of the study. These activities
formed an important complement to the desk research in recognition that the deployment



6 Grey literature is information produced outside of traditional publishing and distribution channels, and can
include reports, policy literature, working papers, newsletters, government documents, speeches, white
papers.



                                                                                                                 7
                                                       Deployment of AI in healthcare – Final Report


of AI in healthcare is a rapidly evolving topic, and as such many more recent and important
concepts/accelerators/challenges may not be found in the published literature.

Three exploratory interviews were conducted between the 14th of March and the 9th of
April with relevant stakeholders from Europe, the USA and Israel, covering the geographic
scope of the study. The stakeholders were agreed upon with DG SANTE and included a
hospital representative from Sweden, an Academic researcher in Medical AI from the USA
and a hospital representative from Israel, all of which have deployed AI solutions in
healthcare. In addition to the exploratory interviews, an exploratory workshop was held
on the 29th of April 2024 with the overall objective to identify the sector specific challenges
as well as accelerators for the effective and efficient deployment of AI in healthcare and
clinical practice. The workshop focused on several key areas, including the current and
future needs in healthcare that AI could address, areas with the greatest potential for AI
transformation, discussion of the challenges to AI deployment, and identifying accelerators
for effective AI integration. The workshop was attended by 11 stakeholders, all of which
were from the EU, from a range of stakeholder categories, namely Healthcare
Professionals, Patients, Regulatory Experts and AI Developers (See Table 2).

                              Table 2: Exploratory Workshop Stakeholders
 Stakeholder Group                   Description
 Healthcare Professionals            Two EU-level Associations
 Patients                            Two EU-level Associations
 Regulatory Experts                  One EU level Industry Association
 AI Developers                       Three EU level Industry Associations
                                       Source: Author’s elaboration
3.2.2 Stakeholder Mapping

For this study, five key stakeholder groups were identified, and a tailored approach was
taken to ensure that the insights extracted from each stakeholder group are tailored both
to their unique expertise and experiences as illustrated below:


                Patients and patient associations7 - to gather information on the level
                of digital health literacy amongst patients and patient associations, the level
                of comfort in AI solutions being used in their care, the perceived impact of
                AI tools in healthcare, their concerns of AI being used in their care, and
                actions that could improve their digital health literacy and would make them
                more comfortable with AI being used in their care.

                Healthcare professionals (HCP) and healthcare professional
                associations8 - to gather information on the level of digital health literacy
                amongst HCP and HCP associations, the needs in healthcare that could be
                addressed by AI in the short term and long term, the perceived impact of
                AI tools in healthcare, the areas where AI tools are expected to have the
                most transformative potential, the AI tools they use, the challenges
                affecting the deployment of AI tools, any good practices to ensure the
                effective deployment of AI and improving digital health literacy, their level
                of knowledge on the EU AI Act, and any complementary actions that could
                facilitate the deployment process.




7 EU wide, national, and international patient associations across different medical conditions.
8 EU wide, national, and international HCP associations across different medical specialties.
                Hospital representatives and hospital representative associations 9
                - to gather information on the needs in healthcare that could be addressed
                by AI in the short term and long term, the perceived impact of AI tools in
                healthcare, the areas and medical specialties where AI tools are expected
                to have the most transformative potential, the AI tools currently deployed
                within their hospital, the challenges affecting the deployment of AI tools,
                any good practices they employed to ensure the effective deployment of
                AI, the impact of the regulatory landscape, and any complementary actions
                that could facilitate the deployment process.

                AI developers and researchers and AI developer associations10 - to
                gather information on the needs in healthcare that could be addressed by
                AI in the short term and long term, the areas where AI tools are expected
                to have the most transformative potential, the tools they develop and
                deploy and reasons for not deploying AI tools they have developed, the
                challenges affecting the deployment of AI tools, any good practices they
                employed to ensure the effective deployment of AI and the transferability
                of these good practices, and the impact of the regulatory landscape.

                AI regulatory experts11 - to gather information on the impact of the
                regulatory landscape including the EU AI Act (AIA), the Product Liability
                Directive (PLD), the European Health Data Space (EHDS), the Medical
                Devices Regulation (MDR) and the In-Vitro Diagnostic Medical Device
                Regulation (IVDR), the General Data Protection Regulation (GDPR), the
                Health Technology Assessment (HTA) Regulation on the deployment of AI
                in healthcare.



The organisation of consultation activities across stakeholder groups was based on their
operational proximity to the AI deployment process, aiming to provide granular insights
into the accelerators and challenges of AI deployment (
Table 3).

     Table 3: The organisation of the consultation activities across the stakeholder groups
    Stakeholder Group              Targeted            Targeted          Workshops12         Case Studies
                                    Survey             Interview
 Patient and Patient
                                       X                                        X
 Representatives
 Healthcare
                                       X                   X                    X                   X
 Professionals
 Hospital
                                       X                   X                    X                   X
 Representatives
 AI Developers and
                                       X                   X                    X                   X
 Researchers
 AI Regulatory Experts                 X                                        X




9 Hospital representatives include the decision makers within hospitals (e.g., Chief Information Officers (CIO),
Chief Executive Officers (CEO), AI officers) and EU wide, national, and international hospital representative
associations.
10 EU wide and international associations representing AI developers, and developers of AI solutions based in
the EU and internationally.
11 Individuals that have published work on the impact of the regulatory landscape on AI in healthcare.
12 Exploratory Workshop, Regulatory Workshop and Workshop on the AI Deployment Journey



                                                                                                                   9
                                                     Deployment of AI in healthcare – Final Report


                                     Source: Author’s elaboration
3.2.3 Surveys

3.2.3.1 Survey design and distribution

The information collected from the literature review and exploratory activities informed
the design of the surveys. This approach ensured that the questions within the survey
were targeted and precise, allowing the survey respondents to indicate specific challenges
and accelerators, allowing for actionable insights.

To complement this information, five separate surveys were developed, one for each of
the following stakeholder groups: Hospital representatives; healthcare professionals; AI
developers/researchers; Patients; and AI regulatory experts. The surveys were then coded
into the EUSurvey platform and initially launched in English on June 10, 2024. Translated
versions for the surveys for healthcare professionals, hospital representatives, and
patients, available in all EU languages, followed on July 3, 2024. The survey closed on the
25th September 202513.

A total of 1,224 stakeholders were invited to participate directly in the survey (See Table
4)14. In addition, several relevant EU and international networks/associations distributed
the surveys to their members. The table below presents the distribution of stakeholders
contacted across the stakeholder groups in addition to the response rate achieved.

                 Table 4: Distribution of surveys across the five stakeholder groups
 Stakeholder         EU              National                       Stakeholders             Total
                                                     Individuals
 category            associations    associations                   initially contacted      responded
 Healthcare
                     28              102             112            242                      83
 professionals
 Hospital
                     5               49              253            307                      35
 representatives

 AI developers       9               34              392            435                      36

 Patients and
 patient             55              80              0              135                      70
 representatives
 EU regulatory
                     0               0               105            105                      14
 experts

 TOTAL               97              265             862            1,224                    238

                                     Source: Author’s elaboration

The distribution of stakeholders that responded to the survey based upon whether they
were based within the EU or outside of the EU (International) is presented in the figure
below. When considering all stakeholder groups together, we received at least one
response per Member State (with the exception of Slovakia). The most responses were
received from the Netherlands (27), Latvia (21) and Spain (15).




13 It should be noted that the survey was conducted at a time where the final texts for EHDS (Jan 2025), new
PLD (Oct 2024) were not yet adopted. The final text for AIA was only adopted 4-months prior to the workshop
(May 2024)
14 We had initially proposed to invite at least 175 stakeholders to participate in the targeted surveys.
          78

                                60



                                               31
                                                                26

                                     10                              10                 10
                 5                                   4                                        4


           HCP                  Patient        Hospital         Developer              Regulatory

                                          EU    International

                      Figure 2: Geographical distribution of survey responses


Healthcare professionals and patients received different sets of questions according to
their self-attributed level of awareness of AI (presented in the figure below). The surveys
for patients and HCPs were organised so that participants with no, basic or solid knowledge
were able to contribute through a distinct set of questions to those with solid and advanced
knowledge who received more specific, granular and targeted surveys, presented in the
Annex.
HCPs                                                      Patients

                       4                                                           3

                 19                                                            9
                           28                                                           27
                                                                          31
                 32




         No or limited knowledge                                     No or limited knowledge
         Basic knowledge                                             Basic knowledge
         Solid knowledge                                             Solid knowledge
         Advanced knowledge                                          Advanced knowledge

          Figure 3: Self-reported level of knowledge for HCPs and Patients Survey

3.2.3.2 Survey analysis:

A total of 16 survey responses were excluded for the following reasons:

   •   5 duplicate responses (1 in the hospital representative survey and 4 in the HCP
       survey). The most recent contribution from the respective stakeholders was
       included in the analysis.

   •   11 responses due to geographic location

The cleaned and structured dataset was then subjected to quantitative and qualitative
analysis. The specific analytical approach was determined according to the specific
questions and the quantity/quality of the data collected. Quantitative analysis was
conducted in Excel. For qualitative data analysis, in-house AI tools specifically designed



                                                                                                    11
                                                     Deployment of AI in healthcare – Final Report


for qualitative data analysis, employing natural language processing techniques to extract
meaningful insights from a diverse range of textual data (free text responses) were used.
These tools enabled the identification of recurring themes, sentiments, and patterns within
the qualitative data, providing a nuanced understanding of respondents’ perspectives.

3.2.4 Interviews

A total of 26 targeted interviews were conducted with healthcare professionals, hospital
representatives and AI developers within Europe (11 interviews) and regions outside of
Europe (15 interviews). The interviews aimed to gather insights on the recent and
expected future developments to the deployment of AI in clinical practice, the specific
challenges affecting this deployment as well as good practices used to overcome the
challenges, and considerations for future actions that may facilitate the deployment of AI
in clinical practice. As one of the aims of the targeted interviews was to identify good
practices to overcome the challenges affecting the deployment of AI in healthcare, the
majority of stakeholders interviewed (57.7%) were from regions outside of the EU
(international) where AI deployment could be considered advanced.

The content of the interview guides was informed by the literature review and the
exploratory consultations (interviews and workshop) and was tailored towards the
stakeholder expertise. The qualitative findings from the interviews were grouped into
thematic areas according to converging and diverging perspectives presented. The table
below shows an overview of the stakeholder distribution according to geographical location
and type.



Table 5: Overview of the stakeholder distribution according to geographical location and type
 Country                            AI Developer                       Hospital Rep/HCP
 Austria                                                                            1
 Belgium                                                                            1
 Denmark                                                                            2
 Germany                                           1
 Italy                                                                                2
 Netherlands                                       1                                  1
 Spain                                                                                1
 EU level association                                                                 1
 Total EU-level                                    2                                  9
 Japan                                             1                                  1
 South Korea                                                                          1
 United Kingdom                                                                       4
 United States of America                          3                                   5
 Total International                               4                                  11
 Total Interviewees                                6                                  20
                                     Source: Author’s elaboration


3.2.5 Workshops (regulatory and hospital)

Two workshops were organised with relevant stakeholders to discuss specific themes in
detail. The first workshop, held on July 17, 2024, titled "EU Regulatory Environment,"
aimed at evaluating the extent to which existing EU legal frameworks, including horizontal
AI proposals and sector-specific regulations such as the AIA, PLD), MDR, and IVDR,
address challenges and barriers affecting the deployment of AI in clinical practice 15.
Participants, consisting of six academic EU regulatory experts, discussed potential gaps in



15 It should be noted that the workshop was conducted at a time where the final texts for EHDS (Jan 2025),
new PLD (Oct 2024) were not yet adopted. The final text for AIA was only adopted 2-months prior to the
workshop (May 2024)
these regulations and identified complementary actions that may facilitate AI integration
in clinical settings.

The second workshop, titled "The AI Deployment Journey," was held on September 23,
2024. This workshop was attended by six participants, primarily hospital representatives
and healthcare professionals from the USA (3 participants), Israel (2 participants) and
Europe (1 participant), who shared their hospital’s experiences regarding the challenges,
barriers, and accelerators associated with AI deployment in healthcare. The workshop
emphasised perspectives from participants across different regions to allow for a "compare
and contrast" approach, particularly examining the challenges unique to regional
healthcare systems.

3.2.6 Case studies

To complement the findings from the literature review and the consultation activities, four,
in-depth case studies were conducted to analyse AI tools deployed in clinical practice
across different medical specialities, geographic areas, and applications. The objective of
these case studies was to collect first-hand information from key relevant stakeholders on
their experience with the deployment of a specific AI tool in clinical practice, the challenges
and barriers experienced, how these challenges and barriers may differ across different
regions, any good practices to address the described barriers, and the overall impact of
the tool so far. When selecting AI tools for further analysis, we ensured that the criteria
described below were fulfilled.
 Criterion                  Description

 Medical specialty          We ensured that the following criteria are covered:
                            •   Oncology
                            •   General Hospital (covering administrative processes)
                            And two of the following:
                            •   Cardiology
                            •   Anaesthesiology
                            •   Neurology
 Type of application        We ensured that we have one case study addressing each of the following
                            applications:
                            •   Administrative processes (e.g., Large Language Models, Natural
                                Language Processing for clinical documentation, chatbots)
                            •   Triage
                            •   Diagnostic tools
                            •   Treatment and monitoring tools
                            We ensured that at least one of the AI tools selected covers the following:
 Healthcare settings        •   Urban healthcare settings
                            •   Rural healthcare setting
 Geographic region          We ensured each case study focuses on an AI tool developed in the EU, USA,
                            Israel and Japan
 Company size               We ensured that the AI tools selected are developed by both:
                            •   Large enterprises
                            •   Small-Medium enterprises (SMEs)
 Approval pathway           We ensured that at least three of the four AI tools selected have regulatory
                            approval between January 2021 and June 2023 by:
                            •   European Conformity (CE) Marking
                            •   FDA approval
                            •   Both
In line with the above-mentioned selection criteria, we conducted four case studies on the
AI-based tools described in the table below.




                                                                                                      13
                                                                         Deployment of AI in healthcare – Final Report


                           Table 6: Selection of AI-based tools for case studies.




                                                                                                    Application
       Case Study
                                                                            Regulatory
                              Medical           Country        Company                                                    Health
                                                                             approval
                                                                 Size                                                     Setting
         Name                Speciality        Developed                     pathway


 Cardiology -
 Triage                  Cardiology          Israel        Large           Both            Triage                     Rural, Urban
 Administrative -
 Clinical                General                                                           Administrative
 Documentation           Hospital            USA           Large           N/A             processes                  Rural, Urban

 Radiology -
 Diagnosis               Radiology           Japan         Large           N/A             Diagnostic purposes        Urban, Rural
 Oncology -
 Treatment and                                                                             Treatment and
 Monitoring              Oncology            France        SME             Both            Monitoring                 Rural, Urban
                               Source: Authors’ elaboration.
A maximum of five interviews per case study were conducted. Interviews with AI
developers focused on gathering insights into the development process, industry trends,
and challenges faced in bringing the AI tool into clinical practice. Interviews with hospital
representatives and healthcare professionals focused on collecting information from those
either impacted by or involved in the deployment of AI into clinical practice, the practical
challenges, benefits, and concerns related to using the specified AI tool as well as their
views on organisational priorities, financial considerations, and the strategic vision for
implementing the AI tool in healthcare. The stakeholders interviewed for each of the case
studies can be found in the specific case study summary reports in Interview Guide - Case
studies. For two of the case studies, the AI developers declined to participate in the
interview.

    3.3             Task 3: Analysis
Task 3 involved a comprehensive analysis of all the qualitative and quantitative data
gathered from Task 1 and Task 2. The findings from the literature review, surveys,
interviews, workshops, and case studies were triangulated together as part of the analysis
to identify common discussion points and themes. Task 3 also included a preliminary
findings workshop where the initial findings of the study were presented, and a market
analysis focused on the state of deployment AI in healthcare within the EU.

3.3.1 Preliminary findings workshop

The preliminary findings workshop was held online on November 14, 2024, with 36
participants representing various stakeholder groups (Table 7), including AI developers,
healthcare professionals, hospital representatives, and patient associations 16. The
emerging findings of the study were presented, and additional insights were gathered from
the stakeholders to test and refine the validity of the conclusions developed.
                     Table 7: Preliminary findings workshop participants
 Stakeholder group                        Number of EU participants                      Number of international participants
 AI Developer                                              4                                                      5
 Healthcare professional                                   8                                                      3
 Hospital representative                                   6                                                      1
 Patient representative                                    5                                                      0
 Regulatory expert                                         4                                                      0
                                              Source: Authors’ elaboration.




16 The target number of workshop participants proposed was 30.
3.3.2 Market analysis

The market analysis aimed to provide an economic overview of the market of AI for
clinical practice in the EU, including a detailed overview of the extent of current research,
development, and deployment of AI for clinical practice across the EU, the analysis of key
trends and differences across countries and medical specialities, as well as an outlook for
the next five years.

The market analysis was based mainly on desk research complemented by findings from
the consultation activities carried out as part of Task 2 (e.g. survey). We collected a variety
of data from several sources including EU and US databases, institutional reports, and
scientific articles. To estimate the level of deployment of AI-based medical devices we
retrieved from the US Food & Drug Administration (FDA) Medical Device Database the
number of FDA-approved AI-based medical devices17. Given the limitations (See Annex 6)
on the data available in the European Database on Medical Devices (EUDAMED), to assess
the level of deployment of CE-marked AI medical devices, the study team included
information from the Radiology Health AI Register developed by researchers from Radboud
University Medical Centre in the Netherlands 18. The market analysis included available
information on AI-based medical devices between January 2021 and June 2024.

     3.4     Task 4: Monitoring framework
The monitoring framework was done in line with the Better Regulations Guidelines, in
particular Tool #43. For the preliminary identification of indicators, a mapping was
conducted of qualitative and quantitative data sources via desk research of available
indicators and reporting requirements. The mapping was not successful in identifying a set
of indicators. Hence, many of the proposed indicators are to be collected upon request, as
there is a lack of available indicators to inform the effective implementation of the
recommended considerations for future actions.




17 U.S. Food & Drug Administration, 2024. Artificial Intelligence and Machine Learning (AI/ML)-Enabled Medical
Devices.
18 The database can be accessed via the following link: www.radiology.healthairegister.com (Last accessed
10/10/2024).



                                                                                                           15
                                                    Deployment of AI in healthcare – Final Report


     3.5     Limitations of this study
There are several methodological limitations to the study design that should be carefully
considered by the reader in their interpretation of the findings. Firstly, although the
literature review19 covered a broad range of topics, it may not cover all emerging trends
and niche studies in the rapidly evolving field of AI in healthcare. Given the large volume
and continuous publication of AI research, some recent developments may be
underrepresented. In addition, the literature available may present more successful
deployment cases whilst under-representing those that were unsuccessful or subject to
significant obstacles – this study aimed to mitigate this bias within the consultation
activities.

Secondly, whilst the consultation activities (surveys, interviews, and workshops) captured
the perspective of a diverse range of stakeholders and geographic regions. The focus of
the study required the targeted identification of stakeholders who have had exposure to
deployment of AI, resulting in a potential bias of the results. Stakeholders whose
knowledge and/or exposure to AI tools in healthcare delivery are likely to have contributed
to a lesser extent to the findings of this study, as they may not have been sufficiently
aware of the challenges and accelerators to deployment to answer the consultation.

The consultation phase of this study was conducted during, or shortly thereafter the final
text of several key pieces of regulation relevant for this study were adopted including the
EU’s AIA (May 202420), the EHDS (January 202521) and the revised PLD (October 202422).
This should be carefully considered by the reader when reflecting upon the stakeholder
perspectives and desk research presented in this report, and how they apply to the
regulatory reality in present day. Similarly, some of the challenges raised by the
stakeholders have been reported in this study regardless of whether the aforementioned
regulatory frameworks shape them (directly or indirectly) to maintain the comprehensive
nature of this report, and in consideration that a full regulatory assessment was not part
of the scope of this study. The study therefore in reference to the accelerators and
challenges provides a high-level overview of the EU regulatory framework which may
potentially shape or influence (directly and indirectly) the findings reported.

The study’s specific focus on advanced regions outside of the EU for accelerators and
challenges that may not yet be experienced in Europe, means that some of the
accelerators identified may not be fully transferable. The same limitation also applies to
the reporting of the potential of AI use cases to address healthcare challenges, as several
studies and publications were from authors outside of the EU. Nevertheless, these findings
are important to report for future consideration – notwithstanding differences in healthcare
system structures.

The market analysis conducted as part of this study was subject to several limitations
regarding the availability of data on AI technologies. Further detailed elaboration of these
limitations are described in detail within Annex 5 – Details on data sources and
methodology for market analysis. The data availability limitations and lack of currently
established reporting requirements also impacted the establishment of the monitoring
framework, which is subject to several assumptions and considerations.




19 search conducted June 2024, and complemented by additional sources between June and November 2024
20 European Council (2024) AI act: Council gives final green light to the first worldwide rules on AI
21 European Council (2025) EHDS: Council adopts new regulation improving cross-border access to EU health
data.
22 European Council (2024) EU brings product liability rules in line with digital age and circular economy
4       Potential of AI to address healthcare needs
 Within the EU and globally, the sustainability of healthcare systems is facing a growing
challenge. Over the past century, average life expectancy at birth has risen from less than
50 years to 78.9 years in the USA and 80.8 years on average in EU Member States, with
some reaching 83 years23. By 2050, 1 in 6 people will be over the age of 65 – in Europe
and North America, this will be 1 in 4. This demographic shift has led to a growing incidence
of chronic and complex conditions. In 2014, people aged 60 and above accounted for 23%
of the total global disease burden in terms of disability-adjusted life years, with the highest
burden in high-income regions24.

The rising prevalence of chronic conditions, particularly among aging populations, has
increased the demand on healthcare systems, with healthcare expenditure
becoming one of the largest government expenses—8.1% of Gross Domestic Product
(GDP) in Europe (EU) and 18.3% in the United States of America (USA) 25,26. Additionally,
worsening shortages in the health workforce restricts the ability of healthcare systems to
respond to demand, particularly in the EU, where disparities exist across Member
States27,28. Twenty EU countries reported a shortage of doctors in 2022 and 2023, while
fifteen countries reported a shortage of nurses. Based on minimum staffing thresholds for
universal health coverage (UHC), EU countries had an estimated shortage of
approximately 1.2 million doctors, nurses and midwives in 2022 29.

This shortage increases the pressure on healthcare systems, leading to high levels
of burnout among HCPs 30. In a study conducted by the European Employment Services
(EURES), over 70% of HCPs reported poor mental health, with 40% experiencing
depression and anxiety31. In USA, more than half of the doctors (53%) reported persistent
burnout, with 62% experiencing burnout for over 13 months32.

            Figure 4: Summary of challenges leading to increased healthcare demand


                                                          Increase in
                                                           healthcare
                                                          expenditure

                  Increase in          Increase in
                 nu    er and            chronic
               proportion of old       conditions
                    people                                Increase in                    Healthcare     Pande ic
                                                           healthcare                    workforce      worsened
                                                          de and and                      shortage      econo ic
                                                            pressure                                   factors and
                                                                                                           ental
                                                                                                      health of the
                                                                                                       healthcare
                                                                                                        workforce


                                                                        High levels of
                                                                            urnout




23 Eurostat, 2019. Life expectancy at birth.
24 Prince et al., 2015. The burden of disease in older people and implications for health policy and practice.
25 Eurostat, 2023. Sickness and healthcare expenditure down in 2022.
26 Peter G. Peterson Foundation, 2023. Healthcare spending in the United States remains high
27 Lehmann C, 2023. More physicians are experiencing burnout and depression.
28 Sipos, D et al., 2024. Addressing burnout in the healthcare workforce: current realities and mitigation
strategies.
29 OECD (2024), Health at a Glance: Europe 2024
30 Sipos, D., Goyal, R. and Zapata, T., 2024. Addressing burnout in the healthcare workforce: current realities
and mitigation strategies.
31 European University Hospital Alliance, 2024. Rethinking healthcare systems in Europe: A call for urgent,
Europe-wide and EU-funded research and collaboration.
32 Lehmann C, 2023. More physicians are experiencing burnout and depression.



                                                                                                                      17
                                                        Deployment of AI in healthcare – Final Report


                                      Source: Author’s elaboration


Whilst not resolving the issues at their root, AI, including generative AI tools 33 such as
Large Language Models (LLMs)34, may relieve some of the strains experienced by global
healthcare systems through their ability to rapidly process and analyse vast datasets
reduce task-related fatigue and improve consistency in areas prone to human error 35. In
2020, estimates suggested that AI could meet 20% of unmet clinical demand in the USA
and save healthcare systems $150 billion annually by 2026 36.

Stakeholders consulted in this study highlighted that existing AI solutions (“low-hanging
fruit”37) have the potential to address some of these challenges and healthcare needs by
optimising resource allocation and workflow efficiency streamlining administrative tasks
and improving diagnostic accuracy (see Figure 5).
 Figure 5: Healthcare needs that can already be addressed by existing AI solutions according
                    to HCPs, Hospital representatives, and AI developers 38.
                                     HCPs            Hospitals          Developers


                                              Optimizing resource
                                            allocation and workflow
                                                    efficiency
                                                             83%
                                               73%
                     Ensuring equitable                            74%       Streamlining
                    access to healthcare       61%                        administrative tasks

                                                       34%               72%
                                              33%
                                                          61%
                                           42%
                                                                           74%
            Addressing skill gaps
                                       41%                       61%           Improving diagnostic
            among the healthcare                  37%                               accuracy
                 workforce
                                     56%            43%                    72%
                                                      43%        27%
                                       43%
                                                                        60%
                      Improving patient    53%         47%
                       engagement and                            61%      Creating personalized
                         adherence to                                        treatment plans
                       treatment plans                72%
                                             Predictive analytics for
                                                patient outcomes




                                      Source: Author’s elaboration

They also identified opportunities for AI expected to have an impact in the mid- to long-
term future (“high-hanging fruit”39) in personalised medicine, real-time decision-making,
and predictive healthcare. In terms of AI applications expected to have the most
transformative potential, these include administrative support tools, clinical workflow
optimisation tools, and AI-assisted diagnostic tools according to the stakeholders
consulted (Figure 6). These AI systems are both traditional AI systems such as machine

33 Generative AI refers to algorithms that are designed with the capability to generate outputs that can range
from text and images. Such models operate by learning patterns and structures from given datasets, allowing
them to produce outcomes based on the input they receive
34 Zhang and Kamel, 2023. Generative AI in Medicine and Healthcare: Promises, Opportunities and Challenges
35 Roppelt, J.S., Kanbach, D.K. and Kraus, S., 2024. Artificial intelligence in healthcare institutions: A
systematic literature review on influencing factors.
36 Collier, M and Fu, Richard., 2020. Accenture - AI: Healthcare's new nervous system.
37 AI solutions that are already available and are expected to be deployed widely in the next 1 or 2 years.
38 Question was responded to by 36 AI developers, 51 HCPs and 35 hospital representatives
39 AI solutions that are expected to be available and deployed in the next 5 years.
learning models and generative AI systems such as LLMs. For example, LLMs have
demonstrated promise for improving the efficiency and accuracy of healthcare delivery by
extracting clinical information from electronic health records, summarising, structuring, or
explaining medical texts, streamlining administrative tasks in clinical practice, enhancing
medical research, quality control, and education, and supporting diagnosis or serving as
prognostic models40,41,42,43.
   Figure 6: Areas where the use of AI is expected to have the most transformative potential
               according to HCPs, hospital representatives, and AI developers 44.

                                           HCP         Hospital          Developers




                                             Administrative support tool
                                                               88%

                     AI-assisted                   71%
                                                                             Clinical workflow
             surgery/medical robotics to
                                                                     66%        optimisation
               optimize surgical skills
                                                          61%            59%
                                              28%
                                                               44%
                                            25%                             59%
            AI-assisted prognosis                        20%
                                                                   57%
               prediction (risk     64%                35%                             AI-assisted diagnostics
                stratification)       47%              37%28%                    78%
                                                         37%
                                           42%                             44%
                                                                     47%
                                                 56%                          AI-assisted symptom
                Conversational platforms
                                                                  64%        checkers and support in
                 for patient assistance
                                                       66%                     treatment decisions

                                             AI-assisted remote patient
                                                     monitoring



                                      Source: Author’s elaboration

     4.1     Potential of AI to address challenges related to the increase in
             healthcare demand
AI tools have the potential to address the challenges posed by the increase in healthcare
demand by enhancing operational efficiency, helping to alleviate the strain on
healthcare systems. For example, at John Hopkins University Hospital in the USA, the use
of AI tools that accompany medical personnel on patient rounds, analyse medical records,
facilitate patient information retrieval, and schedule appointments reduced Emergency
Room (ER) bed assignment times by 30%, operating room transfer delays by 70%, and
ambulance response times by 63 minutes45.


40 Yang et al., 2022. A large language model for electronic health records.
41 Tian et al., 2024. Opportunities and challenges for ChatGPT and large language models in biomedicine and
health.
42 Adams et al., 2023. Leveraging GPT-4 for post hoc transformation of free-text radiology reports into
structured reporting: a multilingual feasibility study.
43 McDuff et al., 2023. Towards accurate differential diagnosis with large language models.
44 Question was responded to by 36 AI developers, 51 HCPs and 35 hospital representatives. Categories of
answers were extracted based upon free-text responses
45 Shiv Kumar et al., 2022. Real-world application, challenges and implication of artificial intelligence in
healthcare: an essay.



                                                                                                                 19
                                                       Deployment of AI in healthcare – Final Report


Similarly, in the United Kingdom (UK), an AI tool pilot project at Mid and South Essex NHS
Foundation Trust reduced patient non-attendances by 30% over six months, allowing an
additional 1,910 patients to be seen and preventing 377 missed appointments. Co-
designed by a frontline workers and clinical fellows, the tool used anonymised data to
predict the likelihood of a missed appointment based upon factors such as weather, traffic,
and patient’s employment type and offered back-up bookings when the likelihood is high.
It is estimated that the trust, which supports a population of 1.2 million people, could save
£27.5 million a year by using the AI tool 46.

AI tools may also help predict patient flow and service demand by identifying patients
likely to require intensive care or longer hospital stays, assisting in efficient allocation
of staff, equipment, and beds to improve healthcare service delivery 47. For example, an
AI solution (utilising the Holistic Artificial Intelligence in Medicine framework) was
developed in the USA that increased the accuracy of length of stay predictions from 8%
to 20%, enhancing medical and economic decision-making and ensuring better care based
on anticipated hospital duration. This framework also increased 48-hour mortality
prediction rates from 11% to 33%, helping physicians identify patients who may benefit
from immediate attention or intensive monitoring 48. An AI tool currently in use at Vestre
Viken hospitals in Norway has analysed 10,000 patients since its deployment in August
2023 and reduced patient waiting times, saving more than 100 days overall, eliminated
the need for 15 doctor consultations per day and may even have the potential to analyse
up to 39,000 patients annually, as reported by an HCP at the hospital 49. In South Korea,
a medical centre has deployed an AI solution that analyses the severity of pressure ulcers
and identifies deep tissue damage from photos of the affected area while also
recommending appropriate dressings. This tool may alleviate the workload of pressure
ulcer specialists in a hospital where, on average, 200 patients—representing 10% of all
inpatients—suffer from pressure ulcers at any given time 50.

AI tools may also reduce the growing pressure on the healthcare workforce by assisting
in patient triage, which helps prioritise care, optimise resources, and improve efficiency.
The use of chatbots and virtual assistants may enhance patient monitoring, facilitate
communication, and improve the overall efficiency of healthcare systems. For instance, an
AI-powered chatbot in the UK uses natural language processing (NLP) to assess patient
symptoms and provide initial diagnoses. This can reduce the burden on primary care by
triaging non-emergency cases and delivering health information quickly 51. However, the
deployment of the tool within the UK faced obstacles, related to its tailoring for specific
medical needs and complex cases52.

In Spain, Parc Taulí Hospital, a public hospital, collaborated with an AI software developer,
to implement an AI-driven triage system and launch the Advanced Resolution Assistance
Unit (ARA). The AI model redirects low-complexity patients, such as those with urinary
tract infections or ankle sprains, to the ARA and away from the Emergency Department,
which averages 130,000 visits per year. As a result, the model reduced waiting times and
improved patient flow, streamlining operations and potentially lowering emergency room
congestion53. While such tools may improve access to care and enable HCPs to focus on

46 NHS England, 2024. NHS AI expansion to help tackle missed appointments and improve waiting times.
47 Aung et al., 2021. The promise of artificial intelligence: a review of the opportunities and challenges of
artificial intelligence in healthcare.
48 Soenksen et al., 2022. Integrated multimodal artificial intelligence framework for healthcare applications.
49 NRK, 2023. Har allereie spart 115 døgns ventetid for pasientar i Vestre Viken takka vere kunstig intelligens.
50 Hospital Management Asia, 2024. Samsung Medical Centre’s path to smart healthcare.
51 Heaven, D., 2020. An algorithm that can spot cause and effect could supercharge medical AI.
52 Vermeulen, J., 2024. The fall of Babylon? Lessons for AI in the NHS
53 Barcelona Health Hub, 2024. Mediktor's AI integration at Parc Taulí sets a milestone in Spain's public health
history
complex cases, concerns about trust may arise between patients and HCPs if AI systems
are not well-calibrated or monitored. Poor calibration in chatbots can result in inaccurate
recommendations and prevent access to care in a timely manner 54.

Another example of an AI tool used for triage is a model designed to assist in the
management of pulmonary embolisms (PEs). This tool diagnoses, prioritises, and manages
PEs by continuously analysing Computed Tomography (CT) scans and streamlining
communication among multidisciplinary teams. This tool has improved time-sensitive
outcomes, including reductions in turnaround time (TAT), time to treatment, and wait
times across multiple hospitals. For instance, at the Region Halland Health System in
Sweden, TAT decreased from 24.68 hours to 0.66 hours, while time to treatment dropped
from 28.05 hours to 0.98 hours55. Similarly, the Cancer Institute in the Netherlands
reported a reduction in TAT from 7,714 minutes to 87 minutes56. In the United States, the
University of Alabama also observed improvements, with TAT reduced from 53.7 minutes
to 45 minutes and wait times reduced from 22.8 minutes to 15.9 minutes57.

     4.2      Potential of AI to address challenges related to the growing
              administrative burden
Hospitals are becoming increasingly digital and            "The least risk and most acceptable
paperless, which has a number of benefits but also         AI-based solutions will likely be in
introduces some challenges. For example, the               medical billing, improving workflow
implementation of electronic health records (EHRs)         efficiency in documentation, and in
in some instances has resulted in a growing                overall      resource       allocation
administrative burden faced by HCPs globally. A            optimization.  These  are  unlikely  to
study involving 200,081 HCPs across 396                    cause    patient  harm    and    more
                                                           positioned     to   improve      clinic
organisations in the USA using an EHR system found
                                                           operations and clinic finances, which
that HCPs spend 5.8 hours out of 8 hours allocated
                                                           are a significant motivator." – AI
for patient care actively working on the EHR58.            developer from the USA.
Another study conducted at a university hospital in
Switzerland found that nurses in an internal
medicine unit spent 12.3% of their 12.5-hour shift on non-medical tasks activities,
including logistic tasks59. These findings are consistent with the survey for this study where
61% of HCPs and 60% of hospital representatives reported that 20–60% of HCPs’ time is
consumed by clinical documentation. AI tools may have the potential to reduce the
administrative burden, allowing HCPs to focus more on direct patient care. AI tools for
administrative tasks, such as LLMs and Natural Language Processing (NLP), were reported
as having the most transformative potential by 71% of HCPs (36 out of 51) and 87% of
hospital representatives (28 out of 32) who responded to this question, along with 83%
of patients (25 out of 30) who reported feeling comfortable with their use. Such tools may
achieve quick, measurable benefits in hospital settings by assisting HCPs in non-clinical
tasks such as documenting encounters, back-office functions, and patient scheduling.



54 Lucian Leape Institute, 2024. Patient safety and artificial intelligence: opportunities and challenges for care
delivery. Boston: Institute for Healthcare Improvement
55 Wiklund et al., 2023. Use of a Deep Learning Algorithm for Detection and Triage of Cancer-associated
Incidental Pulmonary Embolism
56 Topff L, Ranschaert ER, Bartels-Rutten A, et al. 2023, Artificial Intelligence Tool for Detection and Worklist
Prioritization Reduces Time to Diagnosis of Incidental Pulmonary Embolism at CT
57 Rothenberg et al., 2023. Prospective Evaluation of AI Triage of Pulmonary Emboli on CT Pulmonary
Angiograms
58 Holmgren, A.J. et al., 2024. National Comparison of Ambulatory Physician Electronic Health Record Use
Across Specialties
59 Michel, O. et al., 2021. How do nurses spend their time? A time and motion analysis of nursing activities in
an internal medicine unit



                                                                                                                21
                                                       Deployment of AI in healthcare – Final Report


One example of such tools are digital scribes, which combine speech recognition with NLP
to automate clinical documentation and enhance data accuracy60. A study
conducted in 2023 at The Permanente Medical Group in USA demonstrated the potential
of these AI tools to reduce the documentation burden of HCPs while producing high-quality
clinical records. Among primary care physicians, the AI tool users experienced statistically
significant reductions in the time spent on clinical documentation outside working hours
and in the time spent in notes during appointments compared to non-users. Unadjusted
analyses comparing metrics before and after implementation showed a decrease in mean
time spent in notes from 5.3 to 4.8 minutes for the AI tool users and from 5.0 to 4.7
minutes for non-users. In terms of documentation quality, transcripts and encounter
summaries generated by the digital scribes in the study at The Permanente Medical Group
averaged a score 48 out of a possible 50 points. Ratings were particularly high (>4.95 out
of 5 on average) in domains such as being free from bias, synthesis, internal consistency,
and succinctness and slightly lower in domains like thoroughness, organisation, and
accuracy (4.6 to 4.7). Hallucinations and missing details were reported but were
infrequent, including errors like falsely reporting a prostate exam as performed or
misinterpreting symptoms61.

Similarly, in a study at Northwestern Medicine (USA), an ambient AI tool that generates
clinical notes tailored to specific medical specialty from patient conversations led to a 24%
reduction in time spent on notes and a 17% decrease in after-hours work, commonly
referred to as “pyjama” time. Overlake Medical Center (USA) also reported an 81%
reduction in cognitive burden, allowing more personal and family time, along with
improvements in documentation quality when using the same tool, with 77% of HCPs
reporting better documentation62.

     4.3     Potential of AI to address challenges related to delayed
             diagnoses and treatment
Healthcare systems also face unmet diagnostic and treatment needs, which may result in
delayed diagnosis63 which can result in disease progression and subsequently reduce
treatment effectiveness. One such unmet need is the reduction of variability between
HCPs responsible for interpreting diagnostic results (e.g. in diagnostic imaging), which
based on a study conducted at 3 different hospitals in South Korea, can range from 75%
to 88%64. A prospective observational study conducted in a university hospital in
Switzerland found that one in nine patients admitted through the emergency room
experience diagnostic discrepancies, which in turn were associated with increased in-
hospital mortality65.

Studies have shown that AI can improve the speed and accuracy of diagnosis in
medical specialties such as radiology and digital pathology. From the stakeholders
surveyed in this study, 78% of AI developers (28 out of 36), 59% of hospital
representatives (19 out of 32) and 57% of HCPs (29 out of 51) anticipated that AI-


60 Pavuluri et al., 2024. Balancing act: the complex role of artificial intelligence in addressing burnout and
healthcare workforce dynamics.
61 Tierney, A.A. et al., 2024. Ambient Artificial Intelligence Scribes to Alleviate the Burden of Clinical
Documentation.
62 Microsoft, 2024. A year of DAX Copilot: Healthcare innovation that refocuses on the clinician-patient
connection.
63 Young et al., 2023. The Role of Artificial Intelligence in Colorectal Cancer Screening: Lesion Detection and
Lesion Characterization.
64 Kim et al., 2019. Interpretive Performance and Inter-Observer Agreement on Digital Mammography Test
Sets.
65 Hautz, W.E. et al., Diagnostic error increases mortality and length of hospital stay in patients presenting
through the emergency room
assisted diagnostics66 will have the most transformative potential in healthcare. For
example, in the USA, diagnostic errors cause 40,000 to 80,000 deaths annually 67.
Radiology, in particular, was referred to by stakeholders as among the most mature fields
of AI utility, as highlighted in section 3.3.2. This may be attributed to the vast amounts of
digital data accumulated over the years and through the widespread adoption of standards
like DICOM (Digital Imaging and Communications in Medicine) and systems like PACS
(Picture Archiving and Communication Systems). Hospital representatives from Austria,
Denmark, Italy, the USA and UK highlighted that department specific AI tools may offer
benefits such as improved diagnosis efficiency through requiring only one radiologist to
validate results rather than two, and better prioritisation of urgent cases. However the
stakeholders also highlighted that these tools may face challenges when applied beyond
their training environment, and as such broader applications should be approached with
caution

A study at a German university found that using an AI tool reduced the time taken to
report findings in chest radiographs from 80 minutes to 35–50 minutes68. Another study
conducted by the National Consortium of Intelligent Medical Imaging in Oxford (UK)
revealed that an AI-assisted image analysis algorithm improved junior readers' proficiency
in identifying pneumothoraxes on chest X-rays, achieving accuracy comparable to
senior/consultant readers69. Additionally, in USA, an AI system that can prioritise
intracranial haemorrhage reduced the waiting time from 16 min to 12 min per positive
case70.

However, not all AI algorithms showed improved performance in assessing radiographs
compared to human readers. A recent study of 9 commercially available AI products in the
UK (7 for lung nodule detection and 2 for bone age prediction) found that only 4 of the 7
AI algorithms for detecting lung nodules on chest radiographs showed improved
performance compared to human readers. The remaining 5 algorithms showed no
evidence of a difference in performance 71. A hospital representative from Japan highlighted
that the use of AI in diagnostic imaging could increase the workload of radiologists by
requiring them to review an increased number of false positive results. Additionally, an
HCP from the UK indicated that some diagnostic AI tools may slow down experienced HCPs
by causing them to second-guess themselves.

In terms of treatment, AI algorithms in cardiology can analyse patient data, including
medical history, genetic information, and lifestyle factors, supporting cardiologists to
tailor prevention and treatment strategies to individual patients, thereby improving
outcomes72. A study conducted at four stroke centres in Houston, in USA, assessed the
impact of automated CT angiogram interpretation on in-hospital endovascular
thrombectomy (EVT) workflows for stroke patients73. Prompt EVT can dramatically
improve outcomes in patients with large vessel occlusion (LVO) acute ischemic stroke,

66 Not all stakeholders responded to this question
67 Rodziewicz, T.L. et al., 2024. Medical Error Reduction and Prevention.
68 Van Leeuwen et al., 2022. How does artificial intelligence in radiology improve efficiency and health
outcomes
69 G Lip et al., 2024. Adoption, orchestration, and deployment of artificial intelligence within the National
Health Service—facilitators and barriers: an expert roundtable discussion
70 O'Neill et al., 2020. Active reprioritization of the reading worklist using artificial intelligence has a beneficial
effect on the turnaround time for interpretation of head CT with intracranial haemorrhage
71 G Lip et al., 2024. Adoption, orchestration, and deployment of artificial intelligence within the National
Health Service—facilitators and barriers: an expert roundtable discussion
72 Stafie et al., 2023. Exploring the Intersection of Artificial Intelligence and Clinical Healthcare: A
Multidisciplinary Review.
73 Endovascular thrombectomy, or EVT, is a minimally invasive surgical procedure used to treat acute ischemic
stroke. EVT involves the removal of a blood clot from a blocked artery in the brain, which can restore blood
flow and prevent further brain damage.



                                                                                                                    23
                                                    Deployment of AI in healthcare – Final Report


however its efficacy is time sensitive. The findings showed that AI-assisted LVO detection
significantly decreased the door-to-intervention time by 11.2 minutes and the time from
CT initiation to EVT start by 9.8 minutes in 243 LVO stroke patients, thus speeding up EVT
treatment plans74.

AI-driven robotic systems may also be used in surgical procedures to enhance precision
and improve recovery times. These systems analyse preoperative imaging for surgical
planning, guide instruments with precision, and predict complications, reducing surgical
errors and improving outcomes75,76. A study conducted at Hyogo College of Medicine, in
Japan, found that a deep learning model using surgical video from robot-assisted
gastrectomy was capable of automatically segmenting loose connective tissue fibres to
define a safe dissection plane and demonstrated a mean sensitivity score of 3.52/4.00,
indicating good model performance for safe plane identification 77. Additionally, another
study conducted at the University of California Davis Medical Centre in USA found that an
AI model was able to generate and overlay a heatmap of probable cancer location within
the oral cavity to guide surgeons during cancer excision78.

     4.4     Potential of AI to improve cancer care
The application of AI in healthcare, particularly in cancer care, has increased in recent
years. These tools may contribute to improving diagnostic accuracy, personalizing
treatment approaches, and enhancing patient outcomes 79.

4.4.1 Screening, early detection and diagnosis

Early detection of cancer is important for improving survival rates and reducing treatment-
related morbidity. Detecting cancer involves various methods depending on the type,
location, and suspected stage of the tumour. These include imaging techniques (e.g., x-
rays, mammography, ultrasound, CT scan, Magnetic Resonance Imaging (MRI) etc.),
laboratory and blood tests, endoscopic procedures, biopsies, molecular genetic tests and
physical examinations. The following section provides some examples of AI tools used in
the early detection and diagnosis of certain cancers; however this is not a comprehensive
picture of all the AI tools available for cancer detection across the different cancer types.

AI tools have been demonstrated effectiveness in developing advanced screening and
early detection techniques that improve sensitivity and specificity compared to
traditional methods. For example, AI algorithms are effective in analysing medical
imaging, such as mammograms, CT scans, and MRIs, to detect cancerous lesions earlier
than human radiologists80,81,82. For example, in a study in the USA, an AI tool used for
cervical cancer screening achieved 91% accuracy, surpassing the 69% accuracy of human
experts83. Similarly, in another study conducted in 2022 at the same clinic, the Intelligent
Real-time Image Segmentation (IRS) algorithm improved the detection of abnormal pre-

74 Khalifa and Albadawy, 2024. AI in diagnostic imaging: Revolutionising accuracy and efficiency
75 Guni, A et al., 2024. Artificial Intelligence in Surgery: The Future is Now.
76 Reddy, K at al., 2023. Advancements in Robotic Surgery: A Comprehensive Overview of Current Utilizations
and Upcoming Frontiers
77 Kumazu, Y. et al., 2021. Automated segmentation by deep learning of loose connective tissue fibres to
define safe dissection planes in robot-assisted gastrectomy.
78 Marsden, M. et al., 2021. Intraoperative Margin Assessment in Oral and Oropharyngeal Cancer Using Label-
Free Fluorescence Lifetime Imaging and Machine Learning.
79 Chua, I.S. et al., 2021. Artificial intelligence in oncology: Path to implementation.
80 Hwang and Park, 2020. Clinical Implementation of Deep Learning in Thoracic Radiology: Potential
Applications and Challenges.
81 Ahn et al., 2023. Artificial Intelligence in Breast Cancer Diagnosis and Personalised Medicine.
82 Vobugari et al., 2022. Advancements in Oncology with Artificial Intelligence-A Review Article
83 Nagam VM, 2023. Diagnostic medical artificial intelligence: Futuristic prospects for implementation in
healthcare settings.
cancerous cells (dysplasia) in Barrett’s Oesophagus84, identifying 100% of dysplastic areas
compared to 76.9% with standard methods.

A prospective study at Capio Sankt Göran Hospital in Sweden involving 55,581 women
demonstrated that double reading mammograms by one radiologist plus AI achieved a
non-inferior cancer detection rate (0.5%) compared to standard double reading (0.4%)
by two radiologists85. Moreover, a retrospective study in Norway conducted on 122,969
mammograms from 47,877 women found that an AI system detected 77.9% of all breast
cancers, including 86.8% of screen-detected cancers, highlighting its potential to
accurately detect true-positive cases and reduce radiologists' workload 86. Furthermore, a
study in the UK demonstrated that applying AI to interpret mammograms for breast cancer
diagnosis reduced false positives by 5.7% and false negatives by 9.4% 87. Lastly, in the
USA, an AI-assisted cancer contouring tool using data from the University of California
achieved a balanced accuracy of 84.7% in tumour delineation, outperforming manual
methods (67.2%) by experienced radiologists and urologists 88.

AI tools are being used in endoscopy for early detection of certain cancers such as
colorectal cancer. Most colorectal cancers develop from colorectal polyps, of which
adenomas are the most common type. Early detection and treatment of adenomas by
colonoscopy can therefore prevent colorectal cancer.. The Chinese University of Hong
Kong’s (CUHK) Faculty of Medicine (CU Medicine) introduced an AI system that can analyse
endoscopic images real-time during colonoscopy to alert doctors to identify adenomas and
tumours. A study conducted between 2021 and 2022, showed that junior endoscopists-
in-training achieved an approximately 40% increase in adenoma detection rate with the
use of AI tools89. Additionally, AI systems can assist in the diagnostic process by
integrating data from diverse sources such as imaging, pathology slides, and genomic
analyses. In a study using multiple datasets from China, USA, and Germany, an AI tool
outperformed expert pathologists in diagnosing colorectal cancer, achieving an area under
the curve90 (AUC) of 0.988 surpassing that of pathologists (0.970)91.

In Japan, an AI tool was developed to automate Temporal Subtraction (TS), a process that
compares medical images taken at different times to diagnose new bone metastases. This
tool helps radiologists quickly assess changes alongside CT scan series and is valuable due
to the complexity and urgency of identifying bone metastases 92. Studies found improved
lesion-based sensitivity (46.1% with the AI tool vs 33.9% without the AI tool) without
increasing interpretation time per each lesion found 93, shorter reading times compared to




84 Barrett's oesophagus is a condition in which the flat pink lining of the swallowing tube that connects the
mouth to the stomach (oesophagus) becomes damaged by acid reflux, which causes the lining to thicken and
become red. The condition is associated with an increased risk of developing oesophageal cancer.
85 Karin et al., 2023. Artificial intelligence for breast cancer detection in screening mammography in Sweden:
a prospective, population-based, paired-reader, non-inferiority study.
86 Marthe Larsen et al., 2022. Artificial Intelligence Evaluation of 122 969 Mammography Examinations from a
Population-based Screening Program.
87 Alowais et al., 2023. ‘Revolutionizing healthcare: the role of artificial intelligence in clinical practice.
88 Mota, S. M. et al., 2024. Artificial Intelligence Improves the Ability of Physicians to Identify Prostate Cancer
Extent
89 Lau et al., 2024. Effect of Real-Time Computer-Aided Polyp Detection System (ENDO-AID) on Adenoma
Detection in Endoscopists-in-Training: A Randomised Trial.
90 A metric used to assess performance of AI tools, with a value closer to 1.0 indicating higher diagnostic
accuracy.
91 Wang, K.S. et al., 2021. Accurate diagnosis of colorectal cancer based on histopathology images using
artificial intelligence.
92 Iima M et al. 2023. The efficacy of CT temporal subtraction images for fibrodysplasia ossificans progressiva.
93 Onoue K, Yakami M, Nishio M, et al. 2021. Temporal subtraction CT with nonrigid image registration
improves detection of bone metastases by radiologists: results of a large-scale observer study.



                                                                                                                 25
                                                     Deployment of AI in healthcare – Final Report


bone scintigraphy94, and a 25% reduction in reading time for identifying new metastases
using the TS AI tool95.

4.4.2 Treatment planning and delivery

AI can play a role in optimising cancer treatment, from selecting appropriate therapies
to enhancing precision in treatment delivery (AI personalised medicine). In the USA, a
machine learning model from the National Cancer Data Base 96 (NCDB), developed to
generate novel recurrence scores and identify high-risk patients who may benefit from
adjuvant chemotherapy, achieved an AUC of 0.785 overall and an AUC of 0.817 for
Hormone Receptor-positive (HR+/HER2-)97 subtypes98. In China, in a study conducted at
Fudan University Shanghai Cancer Centre, an AI model analysed key patient factors, such
as weight, number of chemotherapy treatments, and metastases, and accurately predicted
the optimal medication dose for metastatic positive breast cancer, enhancing precision and
minimising side effects99.

Additionally, in a retrospective study at the Netherlands Cancer Institute, an AI algorithm
developed to identify patterns in medical images that could act as biomarkers for
predicting treatment response was assessed. The AI tool analysed 1,055 cancer lesions
from 203 patients with advanced melanoma and non-small-cell lung cancer (NSCLC)
undergoing immunotherapy and achieved an AUC of 0.83 for NSCLC lesions and an AUC
of 0.64 for melanoma lymph nodes. The AI tool then predicted immunotherapy response
with an overall accuracy of 76%, which led to a 24% improvement in 1-year survival
rates100. Lastly, in the USA, an AI tool predicted 30-day cardiotoxicity risk in 36,030
colorectal cancer patients undergoing chemotherapy by analysing key risk factors such as
pre-existing cardiac conditions, recent surgery, and older age 101.

AI may also optimise treatment by enhancing radiotherapy planning, improving both
precision and efficiency. A high-precision AI tool for automatic anatomical delineation on
3D cancer patient images reduced the time required for contour corrections. A study on
head-and-neck cancers demonstrated a reduction in correction time to two minutes with
the AI tool compared to 30 minutes for manual delineation—a 93%-time savings102.
Another study evaluating deep learning solutions for CT image contouring found that the
AI solution took less than two minutes to compute the segmentations, with all participating




94 Onoue K, Nishio M, Yakami M, et al. 2019. CT temporal subtraction improves early detection of bone
metastases compared to SPECT.
95 Sakamoto R, Mori S, Miller MI, et al. 2014. Detection of time-varying structures by large deformation
diffeomorphic metric mapping to aid reading of high-resolution CT images of the lung.
96 A nationally representative hospital-based registry covering approximately 70% of all new invasive cancer
diagnoses in USA
97 HR+/HER2-: Hormone Receptor-positive (HR+) and Human Epidermal Growth Factor Receptor 2-negative
(HER2-). HR+ refers to cancer cells that have receptors for hormones like oestrogen or progesterone, which
can stimulate cancer growth. HER2- indicates the absence of excess HER2 protein on cancer cells. Together,
HR+/HER2- is a common subtype of breast cancer that responds to hormonal therapies but not to treatments
targeting HER2.
98 Zhao, F. et al., 2024. Predicting pathologic complete response to neoadjuvant chemotherapy in breast
cancer using a machine learning approach.
99 Yu, Ze et al, 2022. Predicting Lapatinib Dose Regimen Using Machine Learning and Deep Learning
Techniques Based on a Real-World Study.
100 Trebeschi S et al., 2019. Predicting response to cancer immunotherapy using non-invasive radiomic
biomarkers.
101 Li, C.et al., 2022. Using Machine Learning Approaches to Predict Short-Term Risk of Cardiotoxicity Among
Patients with Colorectal Cancer After Starting Fluoropyrimidine-Based Chemotherapy.
102 Grégoire V et al., 2020. Deep learning auto contouring of OAR for HN radiotherapy: a blinded evaluation
by clinical experts.
physicians approving the AI-generated contours, which were comparable or superior to
manual ones 103.

4.4.3 Clinical decision support

AI-powered clinical decision support systems (CDSS) can assist oncologists by analysing
vast datasets and offering evidence-based treatment recommendations. A
hospital in South Korea tested a CDSS developed to support hepatocellular carcinoma
treatment using internal and external datasets from nine institutions (935 internal and
1,750 external patients). The system achieved an accuracy of up to 87.27% when tested
on internal datasets and 86.06% on external datasets, and the integrated time-dependent
AUC score for survival prediction was 0.89 and 0.86, respectively104.

Additionally, a new AI-powered platform, developed by scientists at a hospital in USA
demonstrated 94% accuracy in cancer detection across 15 datasets with 11 cancer types,
achieving 96% accuracy in biopsy datasets and over 90% accuracy on surgically removed
tumour slides. The tool also excelled in predicting molecular profiles, identifying genetic
mutations linked to cancer growth, and accurately detecting mutations related to
treatment response, such as 96% accuracy for a mutation in blood cancer. For predicting
patient survival, the tool improved prediction accuracy by 8%, or 10% for advanced
cancers, across 17 institutions. The AI tool also identified unique tumour patterns, such
as immune cell presence in long-term survivors and abnormal cell characteristics in short-
term survivors, offering insights into tumour aggressiveness 105.

4.4.4 Equity and access to care

AI tools may have the potential to bridge disparities in cancer care by making advanced
diagnostic and therapeutic tools accessible to underserved populations. With its ability to
enhance diagnoses, predict responses, and plan treatments, AI tools have the potential to
optimise resource allocation and make healthcare more inclusive and accessible,
extending advancements to remote areas where resources are scarce 106. In
Kenya, an AI tool achieved sensitivities of 95.7% and 100% for detecting cervical
squamous cell atypia using digital and physical slides, with AUCs of 0.94 and 0.96 107. In
Ethiopia, an AI tool reduced leukaemia subtyping time from 30 minutes to under one
minute while improving accuracy from 70% to 97% 108. Similarly, in South Africa, six AI
algorithms predicted colorectal cancer recurrence and survival with high accuracy, the best
achieving 87.0% for recurrence and 82.0% for survival. These tools offer oncologists
valuable insights for resource allocation and assist them in their informed decisions,
optimising patient management in resource-limited areas109.




103 Costea M, Zlate A, Serre AA, et al. 2023. Evaluation of different algorithms for automatic segmentation of
head-and-neck lymph nodes on CT images.
104 Lee, Kyung Hwa et al., 2024. Machine learning-based clinical decision support system for treatment
recommendation and overall survival prediction of hepatocellular carcinoma: a multi-center study.
105 The Harvard Gazette, 2024. New AI tool can diagnose cancer, guide treatment, predict patient survival
106 Garcia-Saiso, Sebastian et al., 2024. Artificial Intelligence as a Potential Catalyst to a More Equitable
Cancer Care.
107 Holmström O et al., 2021 Point-of-Care Digital Cytology With Artificial Intelligence for Cervical Cancer
Screening in a Resource-Limited Setting
108 K. Dese et al., 2021. Accurate Machine-Learning-Based classification of Leukaemia from Blood Smear
Images
109 Achilonu, Okechinyere J et al., 2021. Predicting Colorectal Cancer Recurrence and Patient Survival Using
Supervised Machine Learning Approach: A South African Population-Based Study



                                                                                                            27
                                                       Deployment of AI in healthcare – Final Report


     4.5     Potential of AI to harness large amounts of health data
There is a need for healthcare systems to harness the vast amounts of data generated
by modern diagnostic systems110. It is estimated by the World Economic Forum that 97%
of the health data assets are not utilised 111. AI has the potential to unlock patient value
and efficiently manage unused data assets (e.g., imaging, patient histories) to assist HCPs
in diagnosing and optimising treatment for patients 112. One example is an AI model that
analyses vast genomic, molecular, and clinical data and predicts which DNA variations are
likely to cause disease, facilitating faster diagnoses of rare disorders 113.

AI also has the potential to cross reference diverse data sources to improve clinical
outcomes. For instance, AI can scan patient records alongside prescriptions and alert
nurses to potential drug interactions or allergies. By streamlining the medication
management process, nurses can focus more on patient care, delivering safer and more
effective treatments to patients114. According to an association for AI developers based in
Sweden, AI tools will have the potential to manage large amounts of health data for each
patient through various applications across multiple medical fields. The stakeholder
reflected that in radiology, these tools will rapidly and accurately evaluate vast amounts
of imaging data to identify anomalies, such as tumours and fractures, with high precision,
leading to faster diagnoses and improved patient outcomes. In oncology, the stakeholder
explained that the need for personalised treatment plans is even more important, as
therapies must be tailored to individual patients. According to the stakeholder, future AI
tools will be able to analyse genomic, molecular, and clinical data to predict the most
effective treatments based on a patient’s unique genetic makeup, enhancing therapeutic
efficacy while minimising side effects. Furthermore, in chronic conditions such as diabetes
and in cardiology, future AI tools will leverage predictive analytics to assess the risk of
cardiovascular events such as heart attacks and strokes. Those tools will analyse EHRs,
lifestyle factors, and wearable device information and provide early warnings and facilitate
prompt interventions, ultimately preventing serious health crises.

     4.6     Potential of AI to address challenges related to the widening
             disparities and access to healthcare
Across Member States, there are widening disparities reflecting gaps in access, quality,
and affordability of healthcare services 115. AI tools have the potential to reduce such
healthcare disparities by improving healthcare delivery, diagnostics, and operational
efficiency that can help bridge healthcare access gaps, particularly for populations in rural
and underserved areas116. In many rural areas, the scarcity of healthcare resources
presents a barrier to providing comprehensive care. AI algorithms are increasingly used
to optimise resource allocation, from staffing schedules to inventory management,
enabling healthcare facilities to operate more efficiently (see section 4.1). Predictive AI
models can forecast patient admission rates, enabling better preparation for seasonal
fluctuations in healthcare demand, such as increased respiratory cases during winter




110 PwC. How artificial intelligence may improve quality and efficiency, whilst reducing healthcare costs in
Europe.
111 Thomason, J, 2021. Big tech, big data and the new world of digital health.
112 Thomason, J, 2021. Big tech, big data and the new world of digital health.
113 MIT Technology Review. 2023. DeepMind’s AlphaMissense AI can pinpoint causes of genetic disease.
114 Eggerth, A. et al., 2020. Medication management needs information and communications technology-
based approaches, including telehealth and artificial intelligence.
115 European Commission, 2018. Inequalities in access to healthcare: A study of national policies 2018.
116 Cruickshank et al., 2024. How AI Could Help Reduce Inequities in Health Care
months117. Additionally, AI-driven supply chain management can prevent shortages of
critical medications and medical supplies, reducing disruptions in patient care 118.

AI can also help optimise the distribution of HCPs across regions by analysing data on
patient needs, available personnel, and transport logistics. For instance, a healthcare
system could use AI to determine the optimal placement of mobile clinics or to schedule
rotating specialists who can serve multiple remote communities119. By strategically
managing resources with AI, healthcare facilities in underserved areas can maximize the
utility of available assets, ensuring that patients in remote areas do not face excessive
delays or shortages in critical healthcare services.

AI can also play an essential role in upskilling local healthcare providers in remote
areas, where continuing medical education opportunities may be limited. Through virtual
training modules, AI can simulate clinical scenarios, teach new diagnostic methods, and
offer insights based on real-world data. This capability can help bridge knowledge gaps in
rural settings where practitioners may not have the same level of access to specialty
training as their urban counterparts. For example, AI-enabled training platforms use
realistic simulations to help healthcare providers practice procedures, learn about new
treatments, or refine diagnostic skills120.

A primary advantage of AI in healthcare is its capacity to enable rapid diagnostics and
patient triage (see sections 4.3 and 4.1), an area critical to remote and underserved
populations with limited access to in-person medical consultations. AI-powered diagnostic
tools, including those based on machine learning algorithms and image recognition, have
been shown to provide accurate assessments for various conditions such as diabetic
retinopathy, pneumonia, and certain cancers (see section 4.4). These systems can
function remotely, often requiring only images or basic patient data, which allows patients
to be screened and diagnosed without visiting a specialist. HCPs and hospital
representatives consulted reported that AI can help bridge gaps in healthcare access by
bringing advanced diagnostic tools to areas with fewer medical resources. For example,
an app developed in Germany offers patients an AI-driven smartphone app that assesses
symptoms, diagnoses various medical issues, and suggests personalised care. The app
has outperformed human doctors in accurately diagnosing rheumatological disease, skin
rashes, and the source of abdominal pain in emergency room visits 121. Such AI-powered
tools democratise access to a highly effective and scalable “pocket doctor,” no matter how
physically far patients find themselves from health care providers, which empowers
patients in under-resourced areas to reliably triage themselves and subsequently seek
health care through the most appropriate avenue.

The rise of wearable devices equipped with AI algorithms has allowed for continuous
remote patient monitoring, a feature that is especially beneficial for individuals with
chronic illnesses living far from healthcare facilities 122. AI-powered remote monitoring tools
can track vital signs, detect early warning signals, and predict potential health

117 Dixon et al., 2024. Unveiling the Influence of AI Predictive Analytics on Patient Outcomes: A
Comprehensive Narrative Review
118 Kudrenko, 2024. Navigating the Future: AI-Driven Healthcare Supply Chains
119 World Economic Forum, 2022. How autonomous mobile clinics can transform healthcare in least developed
countries.
120 Allan Hamilton, 2024. Artificial Intelligence and Healthcare Simulation: The Shifting Landscape of Medical
Education.
121 Gräf et al., 2022. Comparison of physician and artificial intelligence-based symptom checker diagnostic
accuracy; Berry et al., 2023. Online symptom checkers lack diagnostic accuracy for skin rashes; Faqar-Uz-
Zaman et al., 2022. The Diagnostic Efficacy of an App-based Diagnostic Health Care Application in the
Emergency Room: eRadaR-Trial. A prospective, Double-blinded, Observational Study.
122 Shajari et al., 2023. The Emergence of AI-Based Wearable Sensors for Digital Health Technology: A
Review



                                                                                                            29
                                                      Deployment of AI in healthcare – Final Report


complications. For instance, AI models can monitor patients with diabetes by analysing
blood glucose levels, exercise patterns, and diet 123. These systems provide alerts to both
patients and healthcare providers if patterns indicate an elevated risk of complications,
enabling timely medical intervention without the need for regular clinic visits. For
healthcare systems in remote regions, this can reduce the need for frequent in-person
consultations, lessen transportation costs for patients, and alleviate the demand on local
clinics, thereby making healthcare resources more efficient and accessible.

Telemedicine and AI Chat-bots have emerged as an important tool in bridging
healthcare gaps in rural areas, and AI has the potential to further enhance this service 124.
Through NLP, machine learning algorithms and AI-driven chatbots, telemedicine platforms
can offer preliminary consultations, answer questions, and guide patients toward
appropriate care pathways. AI-powered chatbots, for instance, can handle patient intake,
conduct symptom checks, and even provide preliminary diagnostic suggestions, enabling
healthcare providers to focus on more complex cases while maintaining consistent patient
engagement. A study in the UK evaluating an AI-chatbot, alongside seven primary care
physicians, revealed that while human doctors managed to identify 100% of conditions,
the AI chatbot effectively recognised 99%, covering a wide array of areas, including
obstetrics and mental health. Human doctors achieved a higher accuracy than the AI-
chatbot (82% in comparison to 71%) but when used together provided safe advice 97%
of the time, showcasing the potential of AI in enhancing healthcare delivery 125.

AI technologies offer transformative potential in addressing healthcare disparities across
Europe, particularly in remote and underserved regions. From AI-driven diagnostics and
remote monitoring to telemedicine enhancements and resource optimisation, AI tools can
significantly improve healthcare access, reduce travel needs, and alleviate the burden on
limited healthcare resources in rural areas.

     4.7     Summary
In summary, healthcare systems today face a number of challenges. Challenges include a
rise in the burden of chronic and complex conditions with an aging population, a global
shortage of healthcare workforce, widening health disparities and access to care,
inefficiencies in the delivery of healthcare, and a rise in the cost of healthcare. To address
these challenges, it is important to prepare and transform healthcare systems, leveraging
the large amount of health data available and using innovative solutions such as AI, to
improve the overall efficiency, quality, and access to healthcare. The use of AI systems
has the potential to transform the delivery of healthcare and are already deployed and
used in several hospitals globally with a demonstrable impact. AI systems have proven to
improve operational efficiency by optimising processes and assisting in patient triage, to
automate manual and repetitive tasks (e.g., scheduling, clinical documentation) relieving
HCPs from the growing administrative burden, and to directly improve patient outcomes
by improving diagnosis, monitoring and the delivery of care. For example, AI tools have
shown to improve the speed and accuracy of diagnosis, as well as tailoring treatment
strategies to needs of individual patients.




123 Ahmed et al., 2023. Performance of artificial intelligence models in estimating blood glucose level among
diabetic patients using non-invasive wearable device data
124 Sharma et al., 2023. Addressing the challenges of AI-based telemedicine: Best practices and lessons
learned
125 Gilbert et al., 2020. How accurate are digital symptom assessment apps for suggesting conditions and
urgency advice? A clinical vignettes comparison to GPs
5       Current EU regulatory landscape
To realise the transformative potential of AI in healthcare, its deployment must occur
within a framework that not only promotes innovation, but also ensures safety,
transparency, and fairness. Realising these opportunities requires alignment with existing
regulations that balance innovation with ethical and societal safeguards. The EU regulatory
landscape plays a pivotal role in shaping how AI technologies are designed, deployed, and
used across healthcare systems, ensuring they address healthcare needs while upholding
trust among patients, HCPs and other stakeholders. The below section presents a high-
level informative overview of the regulatory frameworks that may directly or indirectly be
relevant for the deployment of AI in healthcare.

     5.1     Key EU regulatory frameworks for AI deployment in healthcare
The regulatory landscape for AI in healthcare within the EU is shaped by several
frameworks, each addressing directly or indirectly specific aspects of AI development,
deployment, and use. The landscape can be distinguished by both cross-sector and
healthcare specific regulation.

5.1.1 Cross-Sector Regulations

Cross-Sector regulations provide a foundational framework for safety, transparency, and
liability throughout the lifecycle of AI systems, but with different focal points:

    •   The AI Act (AIA) establishes a risk-based approach to AI governance, classifying
        AI systems into different risk categories (unacceptable risk, high risk, limited
        transparency risk, minimal to no risk) and subject these to different rules while
        ensuring safety, transparency, and fairness.

    •   The Product Liability Directive (PLD): The PLD focuses on liability for harm
        caused by defective products, including AI systems, regardless of fault. The PLD
        as amended126 addresses the unique challenges posed by AI technologies, such as
        their complexity, opacity, and autonomous capabilities. The updated directive
        clarifies the liability rules for AI-related defects, ensuring that victims are
        compensated even in cases where a defect cannot be directly attributed to a specific
        fault. This reinforces the importance of robust safety and quality measures
        throughout an AI system’s lifecycle.

5.1.2 Healthcare-specific legal acts

    Healthcare-specific legal acts address the unique requirements of healthcare AI,
    emphasising patient safety, clinical effectiveness, and data governance across different
    lifecycle stages:

    •   The Medical Device Regulation (MDR): Encompasses the entire medical device
        lifecycle, with strong emphasis on clinical evidence, traceability, post-market
        surveillance and transparency. It mandates rigorous clinical evidence and
        continuous post-market surveillance for AI systems that qualify as medical devices
        (Medical Device Artificial Intelligence - MDAI). This ensures that systems maintain
        safety and performance standards throughout their lifecycle.

    •   The In Vitro Diagnostic Medical Devices Regulation (IVDR): Similar to the
        MDR, the IVDR spans the full lifecycle of diagnostic AI tools, with a particular focus
        on development and clinical evidence. The IVDR requires proof of both scientific


126 The revised PLD was adopted in November 2024, after the main analysis of this study had already been
completed.



                                                                                                           31
                                                    Deployment of AI in healthcare – Final Report


        validity, analytical and clinical performance before market entry, ensuring that
        diagnostic AI tools are safe and performant. In addition to rigorous pre-market
        conformity assessments, post-market surveillance and reporting obligations also
        apply.

    •   The Health Technology Assessment Regulation (HTAR) provides a framework
        to support Member States to assess the relative effectiveness and relative safety
        of health technologies through joint-clinical assessments focusing on clinical value.

        The HTAR Includes in scope of joint clinical assessments high-risk medical devices
        of which devices incorporating software using AI. In addition the HTAR provides a
        voluntary mechanism for health technologies not in mandatory scope and
        assessment of non-clinical assessments domains.

    •   The European Health Data Space (EHDS) 127 aims at improving data
        standardisation, interoperability, and secure access to health data, creating a
        robust foundation for AI integration in healthcare. There are provisions in the EHDS
        both on primary and secondary uses of health data that could both aid AI
        integration in clinical practice. The EHDS will support data governance and
        interoperability across all stages, facilitating secure and standardised access to
        health data for AI research, deployment, and post-market use. The EHDS will
        promote secure data access for healthcare innovation, helping improve data
        accessibility and AI model accuracy while maintaining data privacy and security.

5.1.3 Artificial Intelligence Act (AIA)

The AIA (Regulation (EU) 2024/1689)128 is a cornerstone of the EU’s regulatory framework
for governing AI systems, addressing risks associated with their design, deployment, and
use. In line with the New Legislative Framework (NLF) 129 policy, the AI Act is conceived as
safety legislation that will complement existing sectoral measures, such as the MDR/IVDR,
by specifically targeting hazards posed by AI systems. With its risk-based approach, the
AIA provides a robust foundation for ensuring the safety, transparency, and
trustworthiness of AI technologies, particularly in critical sectors like healthcare. Notably,
the AI Act and the sectoral legislation will apply jointly.

Most healthcare AI applications, such as diagnostic tools, clinical decision support systems,
and patient monitoring systems, largely fall under the high-risk category. In the “health
sector where the stakes for life and health are particularly high, increasingly sophisticated
diagnostics systems and systems supporting human decisions should be reliable and
accurate” (recital 47). Such systems would be largely classified as medical devices, which
may present risks not addressed by the essential health and safety requirements set out
in the relevant Union harmonised legislation. The AIA establishes strict requirements
across the AI value chain to ensure safety, transparency, and accountability. Some of
these requirements focus on providers—such as ensuring risk management, robustness,
and compliance through conformity assessments—while others focus on deployers of AI
systems    who     also   bear    critical  responsibilities,   particularly   for   high-risk




127 The EHDS was adopted in January 2025, after the main analysis of this study had been completed.
128 Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down
harmonised rules on artificial intelligence and amending Regulations (EC) No 300/2008, (EU) No 167/2013,
(EU) No 168/2013, (EU) 2018/858, (EU) 2018/1139 and (EU) 2019/2144 and Directives 2014/90/EU, (EU)
2016/797 and (EU) 2020/1828 (Artificial Intelligence Act)
129 EU Commission (2008) New legislative framework
applications130,131,132,133. The AIA defines a "deployer" as any natural or legal person,
public authority, agency, or other body that uses an AI system under their authority within
the EU, except where the AI system is used in the course of a personal non-professional
activity. In healthcare, deployers typically include hospitals, healthcare organisations, and
private practitioners adopting high-risk AI systems such as diagnostic tools, clinical
decision support systems, or patient monitoring applications. Table 8 summarises the AIA
risk categories and the requirements for deployers of AI systems under each category.

               Table 8: Requirements for health-related AI systems in the EU AIA 134.
 Risk              Examples                                          Deployer obligations
 categories

 Unacceptable     •   Social scoring of individuals for health       The placing on the market, the putting
 risk                 benefits                                       into service and the use are prohibited
                                                                     (Article 5).

 High-risk        •   AI-based medical devices falling within the    • AI literacy measures (Article 4)
                      scope of Regulation (EU) 2017/745 and          • Use systems in accordance with
                      2017/746 (e.g. AI Clinical Decision                instructions (Article 26(1))
                      Support Systems);
                                                                     • Assign human oversight to qualified
                  •   AI for risk assessment and pricing for             natural persons (Article 26(2))
                      health insurance;                              • Ensure      relevant and sufficiently
                  •   AI    for    evaluating   and    classifying       representative input data (Article
                      emergency calls; AI for decisions on               26(4))
                      dispatching medical aid;                       •   Monitor the functioning and inform
                  •   AI for emergency healthcare patient triage         stakeholders of serious incidents
                      systems;                                           (Article 26(5) and Article 72)
                  •   AI used by public authorities to evaluate      •   Keep automated logs (Article 26 (6))
                      eligibility for essential public assistance
                                                                     •   Registration obligations for certain
                      benefits and services, including healthcare
                                                                         deployers (Article 26(8) and Article
                      services.
                                                                         49)
                                                                     •   Carry out data protection impact
                                                                         assessment (Article 26(9))
                                                                     •   Fundamental        rights       impact
                                                                         assessment (Article 27)

 Transparency     •   AI-chatbots providing advice on wellbeing;     • AI literacy measures (Article 4);
 risk             •   AI-generated medical deepfakes (e.g.           • Transparency obligations (Article 50).
                      adding and eliminating tumours from
                      medical images);
                  •   AI-based wandering detectors in long-term
                      care homes;
                  •   AI-based food intake sensors in home care
                      settings.

 Minimal to no    •   AI used in pharmaceutical research and         No requirements in the EU AIA.
 risk                 development;
                  •   AI-based systems used for administration
                      in healthcare;



According to the stakeholders consulted 86% of HCPs (26 out of 30) believe that the AIA
references some of the challenges that their healthcare facilities are facing. However, 72%
(18 out of 25) indicated that the AIA also exposes new challenges related to how the


130 Sandra Wachter., 2024. Limitations and Loopholes in the EU AI Act and AI Liability Directives: What This
Means for the European Union, the United States, and Beyond
131 St John Lynch et al., 2024. Artificial Intelligence-Enabled Medical Device Standards: A Multidisciplinary
Literature Review.
132 Busch et al. 2024. Navigating the European Union Artificial Intelligence Act for Healthcare
133 Van Kolfschooten, H. and van Oirschot, J., 2024. The EU Artificial Intelligence Act: Implications for
healthcare.
134 Van Kolfschooten, H. and van Oirschot, J., 2024. The EU Artificial Intelligence Act: Implications for
healthcare.



                                                                                                                33
                                                   Deployment of AI in healthcare – Final Report


regulation should be implemented and complied with at hospital level. Examples provided
by stakeholders include the additional training requirements for accountability standards
and the need for more risk management protocols. In addition, only 26% (6 out of 25) of
the hospital representatives that responded to the survey feel prepared for the obligations
introduced by the AIA, expressing concerns about the financial and logistical burden of
compliance, including difficulties in recruiting skilled personnel and the need for
investments in infrastructure and training.

In contrast, among AI developers consulted, 47% (16 out of 34) are prepared for the
implementation of the AIA and the associated obligations, especially those experienced
with MDR/IVDR compliance, viewing the AIA as an extension of their current efforts. Some
AI developers indicated they had already integrated transparency measures and ethical
frameworks, though others remain in a transition phase, delaying new tool deployment
until they fully understand the AIA.

Training and compliance support is a concern amongst the stakeholders consulted. HCPs
suggested the implementation of short, accessible training programs that fit into their busy
schedules and proposed the establishment of peer-to-peer support networks and
collaboration with legal experts. Hospital representatives echoed the need for government-
accredited auditors and increased access to training resources. AI developers who
indicated they are prepared for the provisions of the AIA have started to create frameworks
for early identification of AI risks and conducting workshops to educate teams on
compliance.

5.1.4 Medical Device Regulation (MDR) and In-Vitro Diagnostic Medical Devices
      Regulation (IVDR)

The MDR (Regulation (EU) 2017/745)135 and the IVDR (Regulation (EU) 2017/746) 136
establish safety and performance requirements for medical devices and in-vitro diagnostic
medical devices, including those incorporating AI. The MDR applies to a broad range of
medical devices, such as AI-powered diagnostic tools, while the IVDR focuses on in-vitro
diagnostic devices (IVD). Both regulations employ a risk-based classification system
with four classes, for MDR:
    • Class I - low risk such as bandages,
    • Class IIa/IIb - medium to higher risk such as diagnostic imaging software, and
    • Class III - highest risk such as AI tools for direct clinical decision-making

Similarly, for IVDR the following risk classes apply:
   • Class A - low risk such as specimen receptacles
   • Class B/C – medium to high risk including self-testing pregnancy tests, and those
       used for the detection of infectious agent without a high risk of propagation
   • Class D- highest risk such as those that are used to detect life-threatening
       transmissible agents with a high risk of propagation

High-risk devices in must undergo rigorous conformity assessments by independent
notified bodies to ensure clinical safety, robust performance, and proven patient benefits.
Key regulatory tools, including the Eudamed database and unique device identification
(UDI) system, support traceability and post-market monitoring, ensuring ongoing
oversight.


135 Regulation (EU) 2017/745 of the European Parliament and of the Council of 5 April 2017 on medical
devices, amending Directive 2001/83/EC, Regulation (EC) No 178/2002 and Regulation (EC) No 1223/2009
and repealing Council Directives 90/385/EEC and 93/42/EEC
136 Regulation (EU) 2017/746 of the European Parliament and of the Council of 5 April 2017 on in vitro
diagnostic medical devices and repealing Directive 98/79/EC and Commission Decision 2010/227/EU
The MDR and IVDR ensure that medical devices and in-vitro diagnostic medical devices
meet stringent safety and performance requirements.

5.1.5 Product Liability Directive (PLD)

The new PLD, (Directive (EU) 2024/2853)137, formally Directive 85/374/EEC, is a key EU
framework aimed at ensuring liability and protecting individuals who suffer harm caused
by defective products. The directive establishes strict liability, meaning that injured parties
are not required to prove negligence but only that the product was defective and caused
harm. This is particularly important in healthcare, where AI systems are increasingly
integrated into critical medical devices and diagnostic tools. By holding manufacturers
liable for defects, the PLD can indirectly incentivise for robust design, rigorous testing, and
continuous monitoring of AI-powered healthcare solutions.

In healthcare, AI systems used for clinical decision support, diagnostics, or patient
monitoring can have significant implications for patient safety. Under the current PLD
framework, harm caused by a defective AI system—such as incorrect diagnoses or
treatment recommendations—could result in liability for the manufacturer. Clarity of
liability regimens protects patients and aids in clarifying the liability between healthcare
providers and manufacturers as well as maintaining high standards for safety and
reliability throughout the product lifecycle.

The complexity and opacity of AI systems, particularly those based on machine learning,
presented challenges for traditional liability frameworks, such as attributing defects or
proving causation. The new product liability directive (Directive (EU) 2024/2853) seeks to
modernise liability rules to address challenges posed by AI and digital products. It explicitly
includes digital products, such as standalone software and AI systems, under its scope to
ensure that liability frameworks remain relevant in the evolving technological landscape.
The revision also aims to address the complexity of proving causation in AI-related harm
by introducing mechanisms for courts to request technical information from
manufacturers, helping to balance transparency with innovation protection138.

Recognising the dynamic nature of AI systems, the updated PLD proposes considerations
for risks that may emerge over a product’s lifecycle, such as those linked to learning and
adaptation post-deployment. These updates reflect efforts to align liability rules with the
unique characteristics of AI, while maintaining a balance between consumer protection
and fostering innovation.

5.1.6 Health Technology Assessment Regulation (HTAR)

The HTA Regulation (Regulation (EU) 2021/2282) 139 establishes a framework for the
coordinated clinical evaluation of health technologies across EU Member States, including
pharmaceuticals and high-risk medical devices, and in vitro diagnostic medical devices. Its
primary objective is to enable faster, more consistent clinical evaluation and reduce delays
in patient access to innovative healthcare technologies. By a Joint Clinical Assessment
(JCA) process, the HTAR ensures that new technologies are evaluated for their relative
clinical effectiveness, safety, compared to existing alternatives in a harmonised manner.




137 Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for
defective products and repealing Council Directive 85/374/EEC
138 European Parliamentary Research Service, 2023. The Artificial Intelligence Act: A step towards a
comprehensive EU framework for AI
139 Regulation (EU) 2021/2282 of the European Parliament and of the Council of 15 December 2021 on health
technology assessment and amending Directive 2011/24/EU



                                                                                                           35
                                                  Deployment of AI in healthcare – Final Report


The HTAR represents a shift towards a unified approach to the clinical assessment of health
technologies in the EU140.

5.1.7 European Health Data Space (EHDS)

The EHDS (Regulation (EU) 2025/327)141 establishes a unified and secure framework for
health data exchange across EU Member States. Its overarching goal is to enhance
healthcare delivery, improve patient access to their health data, and enable broader uses
of health data for research, policymaking, and innovation, including the development and
deployment of AI in healthcare. The EHDS addresses two key aspects of health data usage:

    1   Primary Use: Facilitating individuals' access and control over their personal health
        data, allowing seamless sharing across borders. This includes interoperability
        standards for electronic health records and health information systems to ensure
        consistent data exchange across EU Member States.

    2   Secondary Use: Enabling those interested in using data (data users) such as
        individuals, researchers, public health authorities and AI developers to access
        health data for innovation, regulatory, and policy purposes. Strict privacy and
        security standards govern this access, ensuring sensitive information is protected.

The proposed framework includes provisions for a secure, interoperable digital
infrastructure that supports health data accessibility and cross-border collaboration. For
example, the European electronic health record exchange format seeks to facilitate the
cross-border interoperability of EHRs in the EU. It delineates a set of principles that should
govern this exchange and a process for further development, monitoring and review. It
also lays down set of common technical specifications for the cross-border exchange of
data. Additionally, specifically, for AI deployment in healthcare, the EHDS is expected to
provide a valuable foundation that could incentivise the establishment of high-quality
datasets essential for training, performance testing, and monitoring AI systems142. This
will help address challenges related to data availability, quality, and fragmentation, which
often hinder the scalability of AI solutions. The EHDS also emphasises trust through
privacy safeguards, data anonymisation, and secure access protocols.

    5.2     EU regulatory ecosystem and the path to AI deployment in
            healthcare
The aforementioned frameworks collectively shape key aspects such as safety,
performance, data quality and interoperability, and clinical evidence. While these
regulations lay the groundwork for innovation and adoption, the actual deployment of AI
in healthcare involves navigating diverse clinical environments, addressing
implementation challenges, and meeting the unique needs of healthcare systems.




140 European Commission, 2023. Factsheet - Implementing the EU Health Technology Assessment Regulation.
141 Regulation (EU) 2025/327 of the European Parliament and of the Council of 11 February 2025 on the
European Health Data Space and amending Directive 2011/24/EU and Regulation (EU) 2024/2847.
142 for example see Data quality and utility label requirements under Article 56 EHDS
6       Current state of deployment of AI in healthcare in the EU
This section presents an overview of the current market of AI/ML-enabled medical devices
in clinical practice within the EU, and to provide a future outlook on their level of
deployment. The section is organised into three sections, one analysing the trends in
research, the second focused upon AI development and the last focusing on deployment
in clinical practice. More details on the methodology and data sources used can be found
in Annex 5 – Details on data sources and methodology for market analysis.

6.1     Research of AI/ML-enabled medical devices in clinical practice
AI applications in healthcare are rapidly expanding and gaining increasing interest, with
data showing numerous companies, universities, and research institutes both in Europe
and internationally investing in the research of these technologies 143. To assess the level
of research on AI in the healthcare sector, various data sources were consulted 144.
According to the CORDIS database145, there were a total of 553 funded research projects
over the past 10 years on the topic of “AI in healthcare”. The majority were initiated from
2019 onwards, beginning with 33 projects in 2015 and peaking at 85 projects in 2022 146.
Specifically, the number increased consistently from 2019 to 2022, indicating a
sustained momentum for AI research in healthcare during those years.

Figure 7: Number of EU-funded research projects on AI in healthcare initiated each year (2015-
                                          2024)




* The number of approvals in 2024 is based on data last accessed on 13/11/2024. Additionally, the 553 projects
include 8 that are scheduled to start in 2025.

                      Source: Authors’ elaboration based on CORDIS database.

The number of EU-funded projects slowed down in the last two years, however this may
be an artefact of the period between the completion of previously funded projects and
launch of follow-up calls. The total budget of the research projects considered above
between 2015 and 2024 amounted to approximately EUR 3.53 billion, with an average
budget per project of EUR 6.73 million. It should be noted that at the time of writing this
report, the Commission recently launched a call as part of the EU4Health Programme


143 Secinaro et al., 2021. The role of artificial intelligence in healthcare: a structured literature review.
144 details on these data sources are provided in Annex 5 – Details on data sources and methodology for
market analysis
145 CORDIS is the European Commission’s primary source of results from the projects funded by the EU’s
framework programmes for research and innovation. It has a structured public repository with all project
information held by the European Commission such as project factsheets, participants, reports, deliverables and
links to open-access publications
146 The number of projects is indicative and is based upon extracting projects from CORDIS using the search
string “(Artificial Intelligence) AND (Healthcare). It is possible that relevant projects that did not include these
terms within their description were excluded. Please see the Annex 6 for more details.



                                                                                                                 37
                                                         Deployment of AI in healthcare – Final Report


aiming at supporting the deployment of AI in the healthcare sector 147 with an estimated
budget of EUR 4.5 million.

In addition to EU-funded research projects, the rapid technological advancements in AI
are evident from the sharp rise in patenting activity. In the medical field, in particular,
patent data underscores a strong and growing trend in AI-related inventions148. Data from
the platform Espacenet from the European Patent Office (EPO) includes 675 patents of AI
in healthcare, with the majority of patents being filled from 2019 onward. There was a
significant increase from 22 patents in 2017 to 118 in 2023 (representing a five-fold
increase). Research in AI can also be estimated by the number of clinical trials on
AI/ML-enabled medical devices. The data from the WHO International Clinical Trials
Registry Platform (WHO ICTRP) 149 on clinical trials involving AI or ML-enabled medical
devices provided a total of 3,320 results between 2014 and 2024, showing a stark increase
from 6 trials in 2015 to 657 trials in 2024. The number increased consistently over the 10-
year span, highlighting growing progress in the development of AI/ML-based
solutions in healthcare. A significant increase was particularly evident from 2020, when
numbers doubled compared to the previous year. Although no clear causal relationship
has been established, this increase may be related to the rise in research funding following
the implementation of the EU4Health programme in response to the COVID-19 pandemic,
along with the new priorities emerging and recent advancements in the field of AI.

Figure 8: Number of clinical trials on AI/ML-based interventions started each year (2014-2024)*




* The number of clinical trials started in 2024 is based on data last accessed on 19/11/2024. The total number
for the full year 2024 is expected to be higher.

6.2     Development of AI/ML-enabled medical devices in clinical practice
In this section we provide an in-depth analysis of the list published by the Food and Drug
Administration (FDA) of the US in August 2024 of the approved AI/ML-enabled medical
devices150. More information on the database and data limitations with respect to
information on CE-marked AI/ML-enabled medical devices can be found in Annex 5 –
Details on data sources and methodology for market analysis.
The FDA list contains 950 AI/ML-enabled medical devices approved by the FDA up
to June 2024151. According to Muehlematter et al, prior to 2021, the number of FDA
approved devices was low but was following an upward trend. In fact, the number of

147 For more information on the call, please refer to the following link: here
148 Aboy et al., 2023. Mapping the patent landscape of medical machine learning.
149 The WHO ICTRP provides a searchable database containing the trial registration data sets made available
by data providers around the world meeting criteria for content and quality control. It compiles data from national
and regional clinical trial registries worldwide, including ClinicalTrials.gov (USA), the EU Clinical Trials Register,
the Chinese Clinical Trial Registry, and the Japan Primary Registries Network.
150 While the exact criteria for inclusion in the FDA list were not specified, the FDA website defined artificial
intelligence as “a device or product that can imitate intelligent behaviour or mimic human learning and reasoning”
151 U.S. Food & Drug Administration, 2024. Artificial Intelligence and Machine Learning (AI/ML)-Enabled
Medical Devices.
FDA approved devices had more than a 12-fold increase between 2015 and 2020,
from 9 devices listed in 2015, up to 77 in 2019 and 111 in 2020152. Between January 2021
to June 2024, 611 AI/ML-based medical devices had been approved by the FDA.
As it can be observed in Figure 9, there’s been a steady increase in recent years in the
number of approved devices, with a 71% increase between 2021 (129 devices) and 2023
(221 devices).
Figure 9: Number of FDA approvals of AI/ML-enabled medical devices between 2015 and 2024
                                        (per year)




*Number of approvals in year 2024 only includes approvals between January and June. Assuming that the
number of approvals remains constant throughout the year, 212 AI-ML-based medical devices would be approved
in the whole year 2024.

                        Source: Authors’ elaboration based on FDA database.
According to the data retrieved from January 2021 to June 2024, 598 (98%) of 611 AI/ML-
based medical devices were approved through the 510(k) pathway 153, indicating that
almost every device on the market presents a low risk or was preceded by a similar product
that had already been legally placed on the market. Each device was assigned one lead
medical specialty review panel. As exhibited in Figure 10, the most common medical
specialty assigned for the approved FDA AI/ML medical devices was radiology
with 81% of entries (492 out of 611). The second most common medical specialty
related to cardiovascular devices with 56 (9.2%), followed by neurological devices with 20
(3.3%), and gastroenterology-urology with 11 devices (1.8%).
As Figure 10 shows, the number of AI products for radiology has rapidly expanded over
the past years, and the sector is perceived to be leading the way with the implementation
of AI/ML-based solutions for worldwide applied image reading software 154. Most AI/ML-
based medical devices are approved for radiological use, substantially more so than other
medical specialties. One contributing factor to this trend could be the exponential growth
of radiological imaging data compared to the number of available trained readers 155.

152 Muehlematter et al., 2021. Approval of artificial intelligence and machine learning-based medical devices in
the USA and Europe (2015–20): a comparative analysis.


153 Before medical hardware or software can be legally introduced to the US market, the parent company must
submit it to the FDA for evaluation. Depending on the devices' risks, the FDA centrally approves medical devices
through three pathways: the premarket approval pathway (the most rigorous review for high-risk devices), the
de novo premarket review (for low and moderate-risk devices), and the 510(k) pathway, each of which needs
specific criteria to be fulfilled to be granted to be granted. For simplicity, we use "approval" to denote the
clearance of these devices.
154 Benjamens et al., 2020. The state of artificial intelligence-based FDA-approved medical devices and
algorithms: an online database.
155 Hosny et al., 2018. Artificial intelligence in radiology.



                                                                                                             39
                                                       Deployment of AI in healthcare – Final Report


The routine collection of imaging data during clinical practice has resulted in the
availability of large datasets, which are valuable resources for scientific and medical
exploration. Moreover, the adoption of AI technologies may further be driven by the
shortage of radiologists, as these AI devices have the potential to reduce the time
required for radiologists to interpret large volumes of medical images. Consequently, the
number of approved AI/ML-based medical devices in radiology has risen since 2015,
suggesting a continued increase in such devices related to radiology in the future 156.
However, clinical implementation remains limited157,158,159, and the available evidence
for commercially available AI software is still scarce 160.
    Figure 10: Number of FDA approvals of AI/ML-enabled medical devices per lead medical
                                  specialty review panel




                        Source: Authors’ elaboration based on FDA database

6.3    Deployment of AI/ML-enabled medical devices in clinical practice
In multiple studies, healthcare emerges as one of the most prominent sectors for AI
deployment, alongside industries such as ICT, financial services, and education 161,162.
Based on the insights into research and development discussed above, the deployment of
AI technologies in clinical practice could be expected to follow a similar upward trend.
Despite these increasing shares and encouraging data, there is a large disconnect
between the amount of research and development on AI medical devices and
their adoption in clinical practice.

A limited body of literature attempts to estimate the level of AI deployment in clinical
practice due to the lack of comprehensive and complete databases on actual
deployment of AI in general terms, and on AI medical devices in clinical practice in
particular. To overcome these data limitations, two main methodological approaches were
identified in the literature. The first, used in a study by Goldfarb et al provides evidence
on a slow adoption of AI in healthcare in the US163. The study analysed data from


156 Muehlematter et al., 2021. Approval of artificial intelligence and machine learning-based medical devices in
the USA and Europe (2015–20): a comparative analysis.
157 Huisman et al., 2020. Implementation of artificial intelligence: is the community ready? An international
survey of 1,041 radiologists and residents.
158 Strohm et al., 2020. Implementation of artificial intelligence (AI) applications in radiology: hindering and
facilitating factors.
159 Wichmann et al., 2020. Artificial intelligence and machine learning in radiology: current state and
considerations for routine clinical implementation.
160 Van Leeuwen et al., 2021. Artificial intelligence in radiology: 100 commercially available products and their
scientific evidence.
161 O’Reilly, 2021. AI Adoption in the Enterprise 2021.
162 PwC Netherlands, 2017. Adoption of artificial intelligence in healthcare.
163 Goldfarb et al., 2020. Artificial Intelligence in Health Care? Evidence from Online Job Postings
online job postings in the US between 2015 and 2018 and inferred that based upon open
positions in healthcare roles related to machine learning and AI that fewer than 5% of
healthcare organisations have adopted AI tools164. Specifically, the study found that
less than 3% of hospitals posted any jobs requiring AI expertise. It should be noted
that the interpretation of these results is subject to potential biases as some research has
demonstrated that some companies may publish job advertisements requiring AI
capabilities with the purpose of positively influencing investor perceptions and company
valuations165. Equally, job advertisements may be anticipatory of future deployment,
rather than current deployment activities.

The other common approach to estimate the deployment of AI in clinical practice relates
to the use of surveys. For instance, in 2020 the Commission conducted the European
enterprise survey on the use of technologies based on AI 166. According to the results, 47%
of respondents working in the human health services sector claimed to be using
at least one AI tool, while 19% had plans to use AI tools in the future. Earlier this year,
in February 2024, a group of researchers also conducted an online survey across general
practitioners in the UK on their use of generative AI 167. A total of 1,006 general
practitioners responded to the survey, of which 20% (205 out of 1,006) reported to be
using AI tools in clinical practice. Those who claimed to be using generative AI were
asked a follow-up question on the tasks they were using it for. Out of the 205 respondents,
47 claimed to be using the tools to generate documentation after patient appointments
(29%), and 45 for the use of differential diagnosis (28%).
Similarly, there are several papers that analyse data on surveys conducted specifically
among radiologists, as they are one of the groups of medical professionals who are
expected to make the most use of AI tools. A 2024 survey conducted by the European
Society of Radiology among its members showed that 48% of respondents (274 out of
572) claimed to be currently using AI systems in their clinical practice, 27% were
not using any, and 25% were not using any but were planning to do so in the future 168.
Similarly, the American College of Radiology Data Science Institute also conducted a
survey among its members169. Their results show that approximately 35% of total
respondents (493 out of 1,427) claimed to be currently using AI as part of their
clinical practice. The percentage of radiologists claiming to be using AI tools in their
clinical practice is therefore higher compared to the data for healthcare professionals in
general terms.
However, surveys may lead to overly optimistic estimations of AI deployment in healthcare
since participants are usually more familiar with these technologies than the average
healthcare professional, potentially skewing responses toward a more favourable
perception. Moreover, respondents may conflate traditional rule-based or knowledge-
based systems – such as clinical decision support tools – with more recent deep learning-
based AI, which only remains in the early stages of deployment in clinical workflows.
Additionally, methodological limitations, such as unclear phrasing of survey questions or
a lack of transparency regarding respondent selection, may further affect the reliability of
these findings.


164 Johns Hopkins University – Hopkins Business of Health Initiative, 2022. AI in healthcare is here, but
uptake is slow.
165 Elder, 2024. If you want your company’s stock to go up, hire worker IT people.
166 European Commission, 2020. European enterprise survey on the use of technologies based on Artificial
Intelligence.
167 Blease et al., 2024. Generative artificial intelligence in primary care: an online survey of UK general
practitioners.
168 European Society of Radiology, 2022. Current practical experience with artificial intelligence in clinical
radiology: a survey of the European Society of Radiology.
169 Allen et al., 2021. 2020 ACR Data Science Institute Artificial Intelligence Survey.



                                                                                                                 41
                                                      Deployment of AI in healthcare – Final Report


Conversely, several other studies indicate that medical AI device adoption remains in its
early stages, with usage concentrated around a few leading devices. Moreover, the overall
utilisation of medical AI products is still limited, primarily applied to a select number of
procedures170. Further research suggests that AI integration into clinical practice will
remain modest in the coming years, as many AI healthcare products are still in the design
and development phase171,172,173.

The survey conducted as part of this study174 also collected information on whether
surveyed healthcare professionals and hospital representatives claimed to be using AI
medical devices in their clinical practice, and whether AI developers had deployed their AI
applications.
For HCPs and HCP associations, the question on the use of AI tools was only asked to
those respondents who previously indicated to have a good knowledge of AI usage.
In addition, in order to gather granular insights on deployment in practice, HCPs from
technologically advanced hospitals were consulted. The responses collected may therefore
be positively biased, than if the opinion of all healthcare professionals had been
considered. From the 51 responses collected, 63% of respondents (32 out of 51) stated
to have used or to be currently using AI tools in clinical practice against 31% (16
out of 51) who claimed not to be using them. For EU-based respondents, the responses
stayed similar, with 63% of respondents (29 out of 46) claiming to use AI tools compared
to 30% who claimed not to be using them. It should be noted, however, that from the
HCPs that claimed to be using AI tools in their clinical practice, five did not provide
further information on the AI tools while four of them mentioned the use of
ChatGPT. In one of these cases, the HCP claimed that they were testing the use of
ChatGPT with bad outcomes so far. Considering that only 20 out of the 46 respondents
(43%) provided evidence on the actual use of AI/ML-enabled medical devices the survey
results be interpreted with caution, as they may provide biased estimations.
Additionally, the results show that there is a higher percentage of healthcare professionals
based in urban areas who have deployed AI in their clinical practice compared to
professionals in rural areas. Notably, 31 respondents stated to be based on a large city or
metropolitan area of which 58% claimed to have adopted AI. On the other hand, three of
the respondents were based in small towns, of which only one (33%) had deployed AI in
their institution.
In the case of hospital representatives, of the 35 hospital representatives responding
to the survey, 20 claimed to be currently piloting an AI solution (57%), 19 had
already purchased and deployed a commercially available solution (54%), and 11 had
developed and deployed an in-house AI solution (31%). Only two hospital representatives
mentioned not to have yet adopted AI. Thus, the percentage of hospital representatives
who claimed to have deployed AI medical devices was lower than in the case of healthcare
professionals. This may be due to hospital representatives not considering the use of
general-purpose AI tools when replying to this question. From the responses collected,
three respondents mentioned to be from a hospital in a small town with none of them
having deployed AI in their institution. On the other hand, 6 out of the 11 respondents
(55%) from large or metropolitan areas; and 7 out of 10 (70%) from medium cities
claimed to have deployed AI. These results suggest that the adoption of AI tools remains
more prevalent in urban compared to rural regions.


170 Wu et al., 2024. Characterizing the clinical adoption of medical AI devices through US insurance claims.
171 Davenport et al., 2019. The potential for artificial intelligence in healthcare.
172 Apell et al., 2023. Artificial intelligence (AI) healthcare technology innovations: the current state and
challenges from a life science industry perspective.
173 Bajwa et al., 2021. Artificial intelligence in healthcare: transforming the practice of medicine.
174 Subject to the same limitations discussed above for surveys
In terms of the responses collected by 36 AI developers and researchers, a total of 25
respondents (69%) claimed to have developed or to be developing AI tools for healthcare
use – including 16 EU respondents and 9 international respondents. It should be noted,
however, that when AI developers were asked on the specific state of deployment of their
developed AI medical devices there was a significant number of respondents who
mentioned that their tool was in testing and/or piloting phases. In the case of EU
developers, 10 out of the 12 respondents who said they had deployed AI tools provided
more information on their tools. In total, they provided information for 28 developed
tools, of which five were still under development and therefore not actually deployed.
From the 28 AI tools they provided information, 46% (13 out of 28) had been
deployed, while 21% (6 out of 28) were in a piloting phase and 7% in clinical trial phase.
In the case of international respondents, AI developers provided information for 16 AI
tools they had developed of which 12 have been deployed (75%) while 4 were in a piloting
phase (33%). Hence, although the broader question on deployment may have hinted to
an overall fair level of deployment; the actual level of deployment was lower when
respondents provided further details.
      Figure 11: State of deployment of AI tools by EU developers identified in the survey




                                   5                                   Deployed


                                                                       Clinical trial

                                                        13
                                                                       Piloting phase
                              6
                                                                       Under
                                                                       development
                                        2




                       Source: Authors’ elaboration based on survey results
Further assessment on the deployment of AI in the EU was conducted based on the data
available in the Radiology Health AI Register175. As of October 2024, the Register
included information for 214 CE-marked AI products in the field of radiology. The
Register provides information on the date that the AI medical devices listed have been on
the market since. This information was available for 202 devices, of which 183 (90%) had
been on the market since 2015. In the figure below we include the annual number of AI
medical devices in the Register which have been deployed between 2015 and 2024 (up to
June).




175 An online overview of CE-marked AI products based on vendor-supplied product specifications created by
a research team from the Department of Medical Imaging at the Radboud University Medical Center (The
Netherlands). The database can be accessed via the following link: www.radiology.healthairegister.com (Last
accessed 29/11/2024).



                                                                                                          43
                                            Deployment of AI in healthcare – Final Report


        Figure 12: Annual number of AI medical devices in radiology in the EU market




           Source: Authors’ elaboration based on the Radiology Health AI Register
As it can be observed, the number of medical devices that entered the EU market followed
an upward trend until 2020. Since 2021, the number of AI radiology devices on the
market has considerably diminished, which could be inferred as being a result of market
saturation, or the changing regulatory landscape (MDR/IVDR). It should be noted that the
data on market entry dates collected by the Register also shows that there was a peak in
May 2021 on the number of AI medical devices entering the market, prior to the entry into
force of the MDR/IVDR. As exhibited in Figure 13, in May 2021 there were 16 AI radiology
devices entering the market. For the following months of June and July 2021 the number
of products that entered the market was zero. A similar trend could not be identified in
the data analysed on FDA-approved medical devices (see Figure 13 Annex 5 – Details on
data sources and methodology for market analysis).
   Figure 13: Monthly entries in the market of AI devices in radiology between 2020 and 2021
               18
               16
               14
               12
               10
                8
                6
                4
                2
                0    Jan-2020
                    Feb-2020
                    Mar-2020
                    Apr-2020
                    May-2020
                    Jun-2020
                      Jul-2020
                    Aug-2020
                    Sep-2020
                    Oct-2020
                    Nov-2020
                    Dec-2020
                     Jan-2021
                    Feb-2021
                    Mar-2021
                    Apr-2021
                    May-2021
                    Jun-2021
                      Jul-2021
                    Aug-2021
                    Sep-2021
                    Oct-2021
                    Nov-2021
                    Dec-2021

           Source: Authors’ elaboration based on the Radiology Health AI Register
To ensure the comparability with the previous analysis conducted on FDA approved
medical devices, the project team analysed the data on medical devices which had been
CE-marked between January 2021 and June 2024. Between these dates, a total of 50
new AI software for clinical radiology were launched on the EU market and marked
with CE conformity.
Regarding the modalities, we observe that products are distributed over Computed
Tomography (CT) (34%, 17 out of 50 devices), followed by MR and X-ray (each of them
accounting for 13 devices, 26%), ultrasound (4 devices, 8%), and mammography (3
devices, 6%). These figures are in line with the results of a 2024 survey among members
of the European Society of Radiology, whereby AI impact was predominantly expected on
breast and oncologic imaging, primarily involving CT, mammography, and MRI 176. The
extensive use of AI tools for CT is justified by the high volume of imaging data it generates
and its critical role in diagnosing complex conditions, making it ideal for leveraging AI to
enhance accuracy and efficiency177. Additionally, half of the products (25 out of 50)
were marked with IIa risk class, that is products with low and medium risk
levels178. Such result is also in line with the analysis conducted on FDA approved medical
devices, which also showed a higher percentage of low-risk devices. In terms of tasks
performed, the main ones are diagnostic tasks (39 devices, 78%), AI-assisted prognosis
prediction and risk stratification (18%, 9 out of 50 devices), and AI-assisted symptom
checker and support in treatment decisions (4%, 2 out of 50 devices). AI devices, in this
regard, are particularly helpful for diagnostic tasks as they excel at analysing complex
imaging data to detect abnormalities with high accuracy 179.
The Register also includes information on the type of deployment of the AI medical
devices for four pre-defined options: locally on dedicated hardware; locally virtualised
(virtual machine, docker); cloud-based; and hybrid solution. Data was available for 47 out
of the 50 analysed AI medical devices: the majority of analysed devices were deployed
cloud-based (77%, 36 out of 47) or locally on dedicated hardware (72%, 34 out of 47). It
should be noted that the majority of AI medical devices offered more than one type of
deployment. In this regard, those that usually only offered one form of deployment were
the ones being cloud-based – 7 out of the 36 solutions (19%) which could be deployed via
cloud services only had that option for deployment. This analysis therefore evidences the
importance of cloud services for the deployment of AI medical devices, particularly
in the field of radiology. This is in particular the case for small/rural hospitals which may
lack the infrastructure to deploy AI medical devices and may therefore need to rely on
cloud-services.
Hence, the information provided above clearly shows that the breadth of applications
has continuously and rapidly increased in the last few years and, it is not
anticipated to decelerate in the near future180. This is evident when examining both
the research phase of AI technologies in healthcare, the development of AI-based tools
for clinical use and the actual deployment of AI/ML-enabled medical devices in clinical
practice. All indicators mentioned above point to a clear upward trend:
    •    In terms of research, the number of EU-funded research projects on AI in
         healthcare initiated annually tripled, rising from 33 in 2015 to 85 in 2022. 181 The
         number of patents on AI in healthcare published annually experienced a 20-fold
         increased, rising from 6 in 2016 to 122 in 2024 182. The number of clinical trials on
         AI/ML-based interventions initiated annually increased approximately by 109-fold,
         growing from 6 in 2014 to 657 in 2024.




176 Zanardo et al., 2024. Impact of AI on radiology: a EuroAIM/EuSoMII 2024 survey among members of the
European Society of Radiology.
177 Mello-Thoms and Mello, 2023. AI in imaging and therapy: innovations, ethics, and impact: review article.
178 According to the MDR, there are four different classes of medical devices depending on the risk level of the
product (described in detail in section 6.1.2): class I low risk, class IIa low/medium risk, class IIb medium/high
risk, and class III high risk. Whereas a class I CE mark is obtained through self-certification, classes II and III
necessitate an external evaluation by a notified body, which entails a more complex process that also includes
the review of results.
179 Mello-Thoms and Mello, 2023. AI in imaging and therapy: innovations, ethics, and impact: review article.
180 U.S. Food & Drug Administration, 2024. Artificial Intelligence Program: Research on AI/ML-Based Medical
Devices.
181 The number of projects is indicative and is based upon extracting projects from CORDIS using the search
string “(Artificial Intelligence) AND (Healthcare). It is possible that relevant projects that did not include these
terms within their description were excluded. Please see the Annex 6 for more details.
182 Please note it cannot be inferred that these patented products derived from EU funded initiatives/research



                                                                                                                 45
                                                     Deployment of AI in healthcare – Final Report


    •     In terms of development, the number of FDA approvals for AI/ML-enabled medical
          devices has a 25-fold increase, going from 9 in 2015 to 221 in 2023.
    •     Lastly, in terms of deployment in clinical practice, when looking at the number of
          AI-based medical devices in radiology available in the EU market, this also had a
          12-fold increase, growing from 4 in 2016 to 48 in 2020.
Despite the clear upward trend in terms of research and development of AI/ML-enabled
medical devices, their market presence is however still proportionally limited. In
particular, our research shows that even for radiology, that is the medical field which is
expected to leverage the most on AI tools in the future, the number of medical devices in
use is limited. Moreover, our research shows that relying on survey results might
provide biased estimations given that either those participating in surveys may be
those most familiar with AI technologies; or that their responses may not be fully accurate
(e.g. they may be considering the use of general AI application such as ChatGPT). Another
interesting result of our analysis is the fact that most AI/ML-enabled devices are still
products with a medium/low risk, indicating that the human component is still
predominant in higher risk clinical operations and interventions.
Given the limitations in terms of data needed to assess the level of deployment, it becomes
even more challenging to provide a future outlook. Nevertheless, it can be assumed that,
as research and development on AI progresses, and AI enabled medical devices access
the market, a corresponding rise in clinical deployment will follow, albeit this might be
at a slower pace. In Table 9, we provide three different scenarios of the future outlook
of deployment of AI/ML-enabled medical devices in clinical practice in the EU.
 Table 9. Three different scenarios of future outlook of deployment of AI/ML-enabled medical
                                  devices in clinical practice.
                         Level of
                       deployment
        Scenario        in clinical                               Description
                         practice
                           (%)
                                        Under the baseline scenario, we assume that AI deployment
    Baseline                            in clinical practice will progress more slowly than the trends
 scenario – slow             5%         observed in research and development, resulting in levels of
    adoption                            clinical adoption comparable to the estimates provided by
                                        Goldfarb et al. (2020).
                                        Under the best-case scenario, we assume that AI
    Best-case                           deployment in clinical practice will align with those reported
    scenario –              48%         by radiologists who have been identified as the group of
  rapid adoption                        medical professionals using the most AI/ML-enabled medical
                                        devices.
                                        Under the average scenario, we assume that the level of AI
                                        deployment in clinical practice will reach a midpoint between
        Average
                            27%         the slower adoption trends projected under the baseline
        scenario
                                        scenario and the higher adoption levels anticipated in the
                                        best-case scenario.
                                      Source: Authors’ elaboration
Reliable forecasts for the deployment of AI/ML-enabled medical devices, however, are
significantly undermined by the lack of robust data on their actual use in clinical
practice. This highlights a crucial gap between official databases and the real-
world deployment of these tools. Existing official databases and market indicators are
insufficient for tracking the true extent of these technologies' adoption 183.



183 Alderucci et al., 2019. Quantifying the impact of AI on productivity and labour demand: evidence from
U.S. census microdata.
7     Challenges and accelerators to AI deployment and use in
      healthcare
AI tools have the potential to address several needs that healthcare systems face today
(see section 4). However, despite the number of tools on the market today, deployment
remains limited (see section 6.3). The findings of this study extracted several challenges
faced by both developers and deployers of AI solutions that impact the effective and
efficient deployment of AI tools in healthcare. For the scope of this study, these challenges
are grouped into four categories as described in Figure 14. In the following sections we
elaborate on each of these challenges and present the identified accelerators for the
effective deployment of AI tools in clinical practice based on information collected via the
desk research and the consultation activities. Where relevant, the existing regulatory
frameworks directly and indirectly relevant to the challenges identified is also presented.

              Figure 14: Challenges affecting the deployment of AI in healthcare




 Technological and      Legal and                Organisational and     Social and cultural
 data challenges        regulatory               business challenges    challenges
 •Lack of data          challenges               •Lack of funding and   •Lack of trust
  standardisation and   •Complexity of            financing             •Low levels of digital
  interoperability       regulatory               mechanisms             health literacy
 •Outdated IT            landscape               •Lack of end-user      •Concerns on job
  infrastructure        •Concerns                 involvement            security and
 •Lack of validation     surrounding data        •Lack of added-value    overreliance on AI
  protocols              security and privacy     assessment            •Concerns
 •Lack of post-         •Lack of liability and   •Lack of strategic      surrounding impact
  deployment             accountability           direction              on doctor-patient
  monitoring             frameworks                                      relationship
  mechanisms
 •Lack of
  transaprency and
  explainability

                                 Source: Authors’ elaboration


    7.1    Technological and data challenges and accelerators
The technological and data challenges affecting the deployment of AI in healthcare
identified in this study can be grouped into five categories presented in the sections below.




                                                                                                 47
                                                        Deployment of AI in healthcare – Final Report


7.1.1 Data standardisation and interoperability

7.1.1.1 Challenges

According     to    the    literature,   data
                                                  “The lack of interoperability of AI solutions
heterogeneity is a common challenge that          with existing IT solutions is the single most
hinders the deployment of AI tools as it          common challenge cited by customers.
complicates      the     integration      and     Transferring data from system to system is
interoperability       of     various     data    highly tedious, laborious, and can bring
sources184,185. Data heterogeneity refers to      mistakes too easily.” – AI developer from
differences in data types (e.g., text, images,    the USA.
audio, or video), data structures (e.g.,
structured, semi-structured, and unstructured data) and formats across different sources
or systems186. According to hospital representatives consulted, such differences exist
between different healthcare systems, and in some instances between different
departments within the same healthcare institution. The lack of standardised data
structures was described as a significant challenge affecting the deployment of AI in
healthcare by 61% of HCPs (30 out of 49), 62% of hospital representatives (16 out of 26),
and 70% of AI developers (24 out of 34) that responded to the survey question. When
integrating an AI system with an EHR, compatibility challenges may arise due to
differences in data formats, structures, and communication protocols. For instance, an AI
system might use JSON187 for data exchange, while the EHR system uses Health Level 7
(HL7) Fast Healthcare Interoperability Resources (FHIR) standard, leading to discrepancies
in data interpretation. An example in the literature highlights the integration of an AI tool
in oncology, where data transformation tools had to be developed to convert the oncology-
specific data from the AI solution into a format that the relevant EHR system could process
accurately188. Data heterogeneity hinders AI's ability to analyse and aggregate data
effectively across various systems and requires complex mapping and conversion
processes to ensure interoperability between systems. In addition, according to an AI
developer consulted, the lack of standardised data structures impacts the availability of
large and diverse datasets which could be used to train, refine, and test AI algorithms that
would subsequently improve their overall performance and result in more widescale
deployment of AI tools.

Interoperability is defined by the Healthcare Information and Management Systems
Society (HIMSS) as “the ability of different information systems, devices and applications
(systems) to access, exchange, integrate and cooperatively use data in a coordinated
manner, within and across organisational, regional and national boundaries, to provide
timely and seamless portability of information and optimise the health of individuals and
populations globally”189. The lack of interoperable systems was described as a
significant challenge affecting the deployment of AI in healthcare by 49% of HCPs (24 out
of 49), 68% of hospital representatives (19 out of 26), and 74% of AI developers (25 out
of 34) that responded to the survey question. According to the HCPs and hospital
representatives consulted, the lack of standardised data structures and

184 Ahmed et al., 2023. A Systematic Review of the Barriers to the Implementation of Artificial Intelligence in
Healthcare
185 Roppelt et al., 2024. Artificial intelligence in healthcare institutions: A systematic literature review on
influencing factors
186 Gala et al., 2024. The Role of Artificial Intelligence in Improving Patient Outcomes and Future of
Healthcare Delivery in Cardiology: A Narrative Review of the Literature
187 JSON is an open standard file format and data interchange format that uses human-readable text to store
and transmit data objects consisting of attribute–value pairs and arrays.
188 Gao et al., 2024. Artificial Intelligence Applications in Smart Healthcare: A Survey.
189 Li et al., 2022. The impact of electronic health record interoperability on safety and quality of care in high-
income countries: systematic review.
interoperable systems increases operational complexity, creates workflow
inefficiencies and subsequently reduces user adoption. Non-interoperable systems
can lead to manual handling of data (e.g. printing the result of AI and carrying it further
through the existing workflow), which is inefficient and often results in errors. According
to an AI developer from Israel, interoperability is lacking between advanced AI solutions
and existing hospital systems and is often attributed to the incomplete implementation of
EHRs and the fragmented digital health infrastructure across the region. This creates
obstacles to seamless integration and data sharing, forcing HCPs to switch between
multiple platforms, which disrupts their workflow and increases cognitive load. In addition,
the lack of interoperability is a major barrier to scaling AI tools across different healthcare
settings according to AI developers.

7.1.1.2 Accelerators

For AI solutions to be effectively deployed and used within clinical practice, it is important
for AI tools operate seamlessly within existing digital platforms such as an EHR
already familiar to users. They should be readily accessible, require minimal or no
manual data entry by HCPs, and reduce clerical tasks or additional work generated by
their use (e.g., extra clicks, menu navigation, more documentation), thereby minimising
disruptions to the clinical workflow190,191.Establishment of data sharing policies,
standardisation of data collection processes, and promotion of interoperability was
highlighted as a good practice to facilitate the deployment of AI in clinical practice by 71%
of the HCPs who answered the survey question (36 out of 51). Overall, the workflow,
existing practice, current roles, and functions should be minimally impacted to
accommodate the AI system192. Non-disruptiveness is often perceived as safer for patients
and increases the likelihood of successful implementation.

To address the feasibility of interoperability, it was highlighted by stakeholders interviewed
that AI developers should conduct an internal screening of relevant information
systems deployed in the hospital and workflows related to the identified problem (e.g.,
how are they currently solving the problem, what integrations with other systems and
supporting infrastructure will be needed). Collaboration between AI developers and
deployers early on in the deployment process has proven to be effective in ensuring that
AI solutions are interoperable within the existing hospital infrastructure and allowing for
seamless integration according to an HCP from the USA. Ensuring that AI tools are
developed with compatibility in mind supports integration of AI solutions within existing IT
infrastructure and clinical workflows, facilitating cross-regional deployment, particularly in
rural or remote areas. In addition, healthcare organisations might need to invest in
custom middleware solutions such as application programming interfaces (APIs) to
bridge the data format differences and ensure seamless data flow between the AI system
and the EHR system, as carried out by the Mayo Clinic193.

Siloing of data and cumbersome data access approval processes involving multiple
data custodians may be replaced by efficient, standardised processes for accessing
and sharing data from EHR and other sources which is rendered interoperable using
data exchange standards. According to an interviewed hospital representative from Israel
and an AI developer from Germany, radiology provides valuable lessons on the importance


190 Scott et al., 2024. Achieving large-scale clinical adoption of AI-enabled decision support
191 This was evident across the four case studies described in Interview Guide - Case studies.
192 Davis et al., 2020. Machine Learning and Improved Quality Metrics in Acute Intracranial Haemorrhage by
Non-Contrast Computed Tomography.
193 N’gbesso, Y. 2020. Integration of Artificial Intelligence in electronic health records: Impacts and
challenges.



                                                                                                         49
                                                       Deployment of AI in healthcare – Final Report


of data standardisation and system interoperability, particularly through the widespread
adoption of standards like DICOM (Digital Imaging and Communications in Medicine) and
systems like PACS (Picture Archiving and Communication Systems). DICOM ensures a
universal format for medical images, enabling compatibility across various imaging devices
and software, while PACS facilitates the storage, retrieval, and sharing of these images.
These systems exemplify how standardised data, and interoperable frameworks allow for
seamless integration with broader healthcare systems, such as EHR and Radiology
Information Systems (RIS). This integration enhances workflow efficiency and ensures
that imaging data is readily accessible to healthcare providers within a unified digital
ecosystem, paving the way for smoother AI deployment in clinical practice. Outside of the
field of radiology, there are several standards available to achieve data integration and
interoperability:

1. The Artificial Intelligence Modern Data Platform (AIMDP) integrates the core
   features of the modern data platform with data science capabilities to handle
   various data types. In practice, this platform can manage both structured data (e.g.,
   EHR) and unstructured data (e.g., medical images). For instance, in a large healthcare
   institution, AIMDP can integrate data from different departments, such as laboratory
   results, patient monitoring data, and clinical notes. By utilizing its experimentation and
   knowledge extraction modules, the platform helps clinicians extract valuable insights
   from integrated data, thereby optimising patient treatment plans194.

2. Transform available data into data with similar properties and structure. This
   can be achieved by developing a data harmonisation pipeline that adheres to the
   common FHIR data standard. The process includes querying data from the hospital
   database, performing FHIR mapping, conducting syntactic validation, transferring
   harmonised data into a patient-model database, and exporting data in an AI-friendly
   format. The FHIR uses a set of resources and APIs to enable interoperability, allowing
   healthcare data to be accessed, exchanged, and integrated across different systems.
   It is widely adopted by recognised leaders in the healthcare industry such as the Mayo
   clinic195. For example, in diabetes management, a hospital can consolidate patient
   blood glucose data, weight, and dietary records from various sources into a unified
   FHIR standard. This ensures that the data can be consistently used across different
   medical applications, enhancing the personalisation and accuracy of treatment196. The
   advantage of this method is that it ensures data consistency and standardisation,
   which facilitates interoperability between different systems and applications. However,
   it requires rigorous data validation and transformation processes, with a
   substantial initial workload.

3. Use health data content modelling and exchange standards. This includes the
   use of HL7 FHIR or the Observational Medical Outcomes Partnership (OMOP) and other
   agreed-upon international standards as a health data content modelling and exchange
   standard. This involves extracting health data from various sources, converting them
   into a standardised FHIR format, and ensuring data consistency and
   interoperability. For example, in a cross-regional healthcare network, hospitals can
   share patient medical records using the FHIR standard, facilitating seamless
   information exchange. Such standards have already been used in a hospital in Belgium
   to improve interoperability between system. For example, a publicly accessible

194 Ortega-Calvo et al., 2023. An artificial intelligence modern data platform. use case for Spanish national
health service data silo.
195 Learn about HL7 international, 2024. Health Level Seven International - Homepage
196 Williams et al., 2023. A Standardised Clinical Data Harmonization Pipeline for Scalable AI Application
Deployment (FHIR-DHP): Validation and Usability Study.
    foundation model pretrained on longitudinal, structured medical records from 2.7
    million patients from Stanford Medicine that is compatible with the widely adopted
    OMOP Common Data Model (CDM) can be shared and built upon across hospitals. Using
    standardised data structures allows for adapting such models to new tasks that
    significantly reduces the amount of training labels needed, thereby lowering label
    acquisition costs and speeding up the deployment of new applications 197. In addition,
    pre-training on a larger and more diverse patient population improves the
    adaptability of the foundation model across healthcare settings (a single external
    foundation model consistently achieved strong performance across both a Canadian
    paediatric cohort and an American adult ICU-based cohort). In Europe, the European
    Health Data and Evidence Network (EHDEN), an Innovative Health Europe funded
    study, supported data partners in transforming data into the OMOP CDM, as well as
    launching the EHDEN Portal – a gateway to the EHDEN ecosystem with a Database
    Catalogue of 210 databases, over 359M patient records, and 1,300 registered
    researchers198. Another example is in cancer treatment, where genetic information,
    treatment history, and current clinical data can be integrated through FHIR standards,
    allowing specialists across different hospitals to access comprehensive patient
    information on a unified platform and devise the best treatment plans199. The benefits
    of such a method include widespread adoption and support, promoting collaborative
    care and treatment planning. For example, the Scottish Breast Screening Service
    transitioned to a fully paperless allowing for seamless HL7 (international standards for
    transfer of clinical and administrative data between software applications used by
    various healthcare providers) integration, electronic messaging and commands
    between systems200. However, it demands significant effort to convert and maintain
    data in the FHIR format and ensure consistent implementation across different
    systems201.

In addition to the above-mentioned data standards allowing for data integration and
interoperability, according to a hospital representative from Israel and AI developers from
the Israel and the UK, establishing a single platform within which AI solutions can be
integrated, trialled, adopted, and evaluated would also ensure that AI tools can be
seamlessly deployed into clinical workflows. Many AI developers are developing niche
algorithms for specific tasks, meaning that hospitals must procure and integrate multiple
point solutions with often limited IT resources. Using such platforms, hospitals can ensure
that AI tools will already be configured within the enterprise AI platform, acting as the AI
interoperability layer, with all the contracting and deployment built into the system. Such
a platform could allow healthcare providers to evaluate and implement AI tools more
effectively and efficiently without adding to the hospital IT burden.




197 Guo et al., 2024. A multi-center study on the adaptability of a shared foundation model for electronic
health records.
198 van Bochove et al., 2020. EHDEN - D4.5 - Roadmap for interoperability solutions; Oja et al., 2023.
Transforming Estonian health data to the Observational Medical Outcomes Partnership (OMOP) Common Data
Model: lessons learned
199 Sinaci et al., 2023. A Data Transformation Methodology to Create Findable, Accessible, Interoperable, and
Reusable Health Data: Software Design, Development, and Evaluation Study.
200 Lip et al., 2024. Adoption, orchestration, and deployment of artificial intelligence within the National Health
Service—facilitators and barriers: an expert roundtable discussion.
201 Setyawan et al., 2021. Data integration and interoperability problems of HL7 FHIR implementation and
potential solutions: A systematic literature review.



                                                                                                                51
                                                  Deployment of AI in healthcare – Final Report


7.1.2 IT infrastructure

7.1.2.1 Challenges

The successful deployment and continuous use of AI solutions in clinical practice relies

  “The deployment of AI tools requires a base level of digital and physical infrastructure to be
  effective. However, many hospitals in Europe still have limited digitalisation requiring more
  investment in basic digital and physical infrastructure prior to deploying AI tools. Indeed,
  physical infrastructure is also essential for supporting AI, making sure that digital services are
  dependable, safe, and accessible to healthcare professionals in each hospital.” – Hospital
  representative association based in Belgium.

upon having the right IT infrastructure in place. Outdated IT infrastructure is a
significant issue202, especially in Europe where hospitals in rural or underfunded regions
face even greater challenges in updating their systems. Many healthcare facilities do not
have digital EHRs and still operate on legacy systems that are not designed to support the
advanced computational requirements of AI technologies 203. These systems often lack the
necessary processing power, storage capabilities, and network bandwidth needed for AI
applications, leading to slow performance and inefficiencies. Such varying levels of digital
maturity can also exacerbate the issue of interoperability previously described.
Outdated IT infrastructure was described as a significant challenge affecting the
deployment of AI in healthcare by 59% of HCPs (29 out of 49) , 68% of hospital
representatives (19 out of 28), and 53% of AI developers (18 out of 34) that responded
to the survey question. According to an HCP from Italy, some hospitals are not aware of
the infrastructure requirements they should have in place, resulting in improper
deployment of AI solutions.

7.1.2.2 Accelerators

Defining the minimum IT standards to facilitate widespread deployment across hospitals
in the EU was highlighted as a good practice by 55% of the HCPs surveyed (28 out of
51204). Investing in the appropriate IT infrastructure prior to adoption may allow for
interoperable systems and a more seamless integration of AI tools in the clinical
workflow according to consulted stakeholders (hospital representatives from France and
Italy, an HCP from the USA, and an HCP from the UK). Upgrading IT infrastructure
improves hospital operations by reducing the need for manual tasks, which can save time
and improve the integrity of the data by minimising the risk of errors. To support the
computational demands of AI, robust IT infrastructure that includes high-performance
computing (HPC) clusters, advanced data storage solutions, high-speed networks, and
resilient systems was indicated by stakeholders as important (Figure 15)205. A total of 63%
of hospital representatives who responded to the survey question (15 out of 24) indicated
that they invested in upgrading and modernising their IT infrastructure prior to deployment
to support the implementation of AI solutions. For example, the Mayo Clinic updated its IT
infrastructure to include HPC clusters and advanced data storage solutions that can
handle the large data volumes required for AI analysis as part of its “big data” platform
(see section 4.5). The robust IT infrastructure enables real-time processing and
analysis, providing HCPs with timely insights that improve patient outcomes. Such
investments, allow for AI solutions to not only be deployed within healthcare settings, but
to also be scaled effectively. According to an AI developer from the USA, an effective


202 Hospital Management Asia. 2024. Samsung Medical Centre’s path to smart healthcare.
203 European Commission: Directorate-General for Communications Networks, Content and Technology, Page,
M., Winkel, R., Behrooz, A. and Bussink, R. 2024. 2024 digital decade ehealth indicator study.
204 For this survey question 32 HCPs did not respond.
205 Noorbakhsh-Sabet et al., 2019. Artificial intelligence transforms the future of health care.
strategy for updating the IT infrastructure is to use a bottom-up approach where a
specific use-case is selected and the necessary infrastructure and data requirements for
integrating the use-case are identified. Such an approach ensures that deployed AI
solutions are tailored to specific needs rather than trying to fit existing infrastructure into
new technologies.

In the healthcare field, scalability presents a significant challenge for deploying AI
solutions. While AI applications may perform optimally in small-scale clinical evaluations
with a limited data pool, they may face substantial difficulties in maintaining accuracy and
operational speed when the scope expands to a national healthcare framework. For
example, AI systems may struggle with handling large volumes of inpatient data due to
the vast amount of patient information, the diversity of medical conditions, and the need
for seamless integration with various healthcare information technology systems. To
address this challenge, hospitals and healthcare institutions need to implement effective
data processing strategies and sophisticated system architectures to ensure the
integrity and effectiveness of AI applications at scale 206.

The use of modular architecture is one solution for achieving scalability in AI
applications. Such architecture supports parallel processing, which enhances speed and
efficiency, especially when dealing with extensive patient data. For instance, in a
healthcare AI application, the architecture might include separate modules for processing
patient data, performing predictive analytics, and generating reports. Each module
operates independently and concurrently, which improves overall performance 207. For
example, the Modular Health Information System at Mount Sinai hospital in the USA
integrates various specialised modules to handle tasks like patient monitoring,
data analysis and reporting which enables effective management of large volumes of
patient data and flexibility to adapt to evolving needs without extensive system
modifications208.




206 Barmer et al., 2021. Scalable AI.
207 Cohen et al., 2021. A Methodology for a Scalable, Collaborative, and Resource-Efficient Platform to
Facilitate Healthcare AI Research.
208 Gao et al., 2024. Artificial Intelligence Applications in Smart Healthcare: A Survey.



                                                                                                          53
                                                      Deployment of AI in healthcare – Final Report


                    Figure 15: IT infrastructure to effectively deploy AI solutions.




     High-performance           Advanced storage           High-speed                 Redundant and
     computing clusters         solutions                  networks                   resilient systems
     •Provide the               •Data storage              •Reliable and high-        •Ensures
      computational              systems that can           speed network              continuous
      power required             handle the large           connectivity is            operation and
      for processing             volumes of data            important for the          data availability,
      large datasets and         generated in               real-time                  even in the event
      runnign complex            healthcare. This           transmission and           of hardware
      AI algorithms.             includes both on-          analysis of data.          failures or
      Such clusters              premises and               This ensures that          maintenance. This
      enable real-time           cloud-based                AI tools can access        reliability is
      analysis and               storage solutions          and process data           important for
      support the                that offer                 quickly, providing         maintaining the
      scalability needed         scalability,               timely insights to         functionality of AI
      for AI applications.       security and               HCPs.                      applications.
                                 redundancy.

                                      Source: Authors’ elaboration.

Cloud computing also offers a solution for achieving scalability as it provides scalable
computing resources and storage capabilities that adjust dynamically to meet the demands
of AI workloads without the need for on-premises infrastructure. Cloud services also offer
scalable storage systems that are essential for managing large amounts of medical data
that can be used to train, test, optimise, and monitor AI models. Cloud computing services
enable efficient scaling of computational power and storage, maintaining system
stability and performance during high demand periods 209. For example, smaller hospitals
in rural or remote areas, which often lack the infrastructure to manage large data volumes,
increasingly rely on cloud computing services to store their data. According to a hospital
representative from Israel that took the strategic decision to migrate all its processes to
the cloud, the use of cloud services improves reliability, flexibility, and agility compared to
on-premises solutions, which also made the deployment of cloud-based AI solutions
smoother and more streamlined. The establishment of a “Cloud Committee” within the
hospital, whose role is to approve and certify all cloud-based solutions before they are
deployed, made the deployment process easier.

Although cloud computing offers dynamic scalability and cost efficiency by adjusting
resources in real time, there are concerns about data security (see section 7.2.2.1) and
reliance on external service providers210. Such concerns were mentioned by a hospital
representative from Denmark. The transmission of patient data to cloud-based services
is often subject to internal approval processes defined by the healthcare organisation,
which may involve the Data Protection Officer (DPO) or data security team—particularly
when the processing involves international data transfers under the GDPR 211. In addition,


209 Wittig et al., 2023. Amazon Web Services in Action: An In-Depth Guide to AWS.
210 Amajuoyi et al., 2024. Transforming business scalability and operational flexibility with advanced cloud
computing technologies.
211 In this context see Penzkofer T. 2024. Prostate MRI: what to consider when shopping for AI tools.
different countries and sometimes different regions have different guidelines and
regulations regarding the use of cloud services for medical data, which may complicate
the standardisation of AI deployment across different sites. In most data protection
legislations, processing of health data has additional requirements since health data is
considered sensitive. According to an AI developer interviewed from the USA, most
healthcare organisations in Europe prefer on-premises AI systems over cloud-based
solutions. Three AI developers from the USA and the hospital representative from South
Korea indicated that the reluctance of healthcare providers to use cloud-based solutions
is a barrier to scaling AI solutions within healthcare. According to an AI developer from
the USA, cloud-based solutions facilitate data sharing allowing for more efficient
post-deployment monitoring (see section 7.1.4.2) and help overcome any limitations
with on-premises data storage and computational power.

7.1.3 Local AI performance

7.1.3.1 Challenges

In some instances, there is a lack of real-world evidence, to indicate the effectiveness
of AI use in real-life settings212. AI platforms are limited by the quality of the data inputs
they receive, implying that the algorithm is only as good as the data source “teaching”
it213. The local performance of AI tools is often evaluated and validated using a different
set of evaluation criteria or small datasets leading to difficulty in comparing
algorithms and variations in performance that may occur within the same healthcare
settings, across different healthcare settings and across medical specialties. This issue is
compounded when applied to the wide variety of predictive AI models from disease
detection to clinical intervention that need performance testing and ongoing
monitoring for algorithmic effectiveness across demographic and social determinants
such as race and ethnicity, gender, age, geography, and income214. The accuracy and
quality of AI tools within specific healthcare settings are some of the main contributors
to adoption hesitance amongst HCPs according to HCPs and hospital representatives
consulted. A lack of an agreed standard and benchmark for accuracy (e.g., how
accurate does an AI tool need to be before it is approved for clinical practice) is an
impediment to implementation, and subsequently, adoption 215. The lack of accuracy of
AI outputs could pose a potential risk of harm by both HCPs and patients, for example
false negative results may provide an incorrect sense of reassurance and cause a delay in
treatment216. The lack of protocols for local performance testing to assess variations
in performance across healthcare settings for existing AI solutions was described as a
significant challenge affecting the deployment of AI in healthcare by 55% of HCPs (18 out
of 49), 39% of hospital representatives (9 out of 26), and 56% of AI developers (13 out
of 34) that responded to the survey question. It is also important to consider that AI tools
do not only fail because of how the algorithm was trained, but may also fail because of
variability in human behaviour, both by HCPs and patients. For example, a hospital
representative from Israel stated that variations in performance may arise due to
differences in HCPs preferences, workflows, and the types of cases handled (in-patients



212 Liu et al., 2019. A comparison of deep learning performance against health-care professionals in detecting
diseases from medical imaging: a systematic review and meta-analysis.
213 Singh et al., 2020. Current challenges and barriers to real-world artificial intelligence adoption for the
healthcare system, provider, and the patient.
214 Shah et al., 2023. A Nationwide Network of Health AI Assurance Laboratories.
215 Morrison K, 2021. Artificial intelligence and the NHS: a qualitative exploration of the factors influencing
adoption.
216 Mlodzinski et al., 2023. Assessing barriers to implementation of machine learning and artificial intelligence-
based tools in critical care: web-based survey study.



                                                                                                               55
                                                        Deployment of AI in healthcare – Final Report


versus out-patients). If appropriate standards and benchmarks are established, it could
provide rationale for the accuracy of such AI tools.

7.1.3.2 Accelerators

Training on diverse datasets to account for local performance variation was highlighted as
an important good practice by 67% of the HCPs who answered the survey question (34
out of 51). According to a stakeholder consulted from the USA, there is a need for well
designed, multi-site, multi-centre (ideally heterogenous population) local performance
testing using standardised methodologies to understand the real-world impacts of AI in
healthcare and explore robustness, interpretability, and trust of data within specific
healthcare settings. Under regulatory frameworks pre-market conformity assessments to
ensures that AI systems meet predefined safety and performance standards. However,
pre-market conformity assessments alone may not guarantee that the AI performs
optimally in all healthcare settings, as differences in demographics, clinical practices, and
healthcare infrastructure can impact outcomes. Additionally, AI tools not within the
regulatory oversight (for example some administrative use cases) may not be subject to
the same framework.

Local performance testing examines whether AI tools (including AI Medical Devices)
maintain consistent performance when applied in different regions or clinical environments
- such as determining whether an AI based medical device developed and tested in the US
or Germany and performs equally well in Cyprus.

Unlike pre-market conformity assessments, local performance testing is not explicitly
required by regulation and can be carried out by the developer, the deployer, or both in
collaboration. Incorporating local performance testing as a standard practice could
potentially improve trust and ensure consistent AI performance across diverse healthcare
settings. Local performance testing has the added benefit of involving a subset of future
users of an AI tool prior to wide-spread deployment, which may help to alleviate resistance
to change, by allowing HCPs to explore first-hand the performance of an AI solution against
their own data.

AI systems should be tested on analogous datasets so that performance can be
assessed and compared using standardised high-quality data to produce reports on model
performance that can be widely shared. A total of 54% of the hospital representatives
surveyed (13 out of 24) indicated that they conducted local performance tests of the AI
solutions prior to deployment to address any concerns on variations in performance.
Forming partnerships between the relevant stakeholders including other hospitals, and AI
developers allow for the formation of collaborative data infrastructures that facilitates such
local performance studies, ensuring that AI tools are suitable for local use 217. This was
supported by a number of different stakeholders consulted from both Europe and the USA.
For example, an AI developer from the USA highlighted that the establish partnerships
with clinic healthcare centres and research institutes to perform such local
performance studies and address variations in performance, while an HCP from
Denmark reported that a central entity for data collection and storage is being
investigated that will allow for such performance studies to be conducted effectively.
Should local performance be suboptimal, AI models should be retrained to ensure they
perform as required within the given healthcare setting218.



217 Lip et al., 2024. Adoption, orchestration, and deployment of artificial intelligence within the National Health
Service—facilitators and barriers: an expert roundtable discussion.
218 Scott et al., 2024. Achieving large-scale clinical adoption of AI-enabled decision support.
A digitally advanced hospital in the USA has established a distributed data network, in
which partners contribute their unique data in an agreed-upon standard (see section
7.1.1.2), while each organisation maintains strict control over their own data within the
confines of their organisational IT infrastructure and cybersecurity boundaries 219. This
model relies upon a unique collaborative design             “If AI is going to be used as a
philosophy with technical and administrative                clinical  tool    (diagnostic    or
controls that ensure privacy and confidentiality.           otherwise), then it should be
While network controls vary from partner to partner,        subjected to the same level of
two overarching principles ensure consistency and           scrutiny that any new clinical tool
promote trust:                                              is subjected to when coming to
    • Data de-identification: users cannot see or           market. Given that this particular
                                                            tool constantly improves, there is
        interact with identifiable data and cannot
                                                            need for constant monitoring on
        export, co-mingle, or attempt to reidentify
                                                            deployment and oversight by
        individual de-identified records. Depending on      medical professionals to ensure
        the data owner’s jurisdiction, the system uses a    that it does what is intended.” –
        variety of techniques to accomplish de-             HCP from Ireland.
        identification or its equivalent.
    • Secure, federated architecture: Data and
        intellectual property remain under the control of each respective partner or model
        developer and are only viewed or used as authorised.

Users can view and analyse data in a federated manner across the network when they use
the data to develop, train, and test algorithms. During performance testing, data and
models remain with their respective owners. In some cases, a model developer may agree
to securely transmit their model to the platform for testing. The model is never visible to
the owners of the platform, as it remains encrypted. In all local performance testing use
cases, a report detailing model performance is securely transmitted back to the user and
the platform securely disposes of any models in its possession once testing is complete.

Additionally, single platforms within which AI solutions can be integrated and
procured, may both enable seamless integration and interoperability (see section 7.1.1.2)
and allow hospitals to test AI products using anonymised data to evaluate the tool’s
performance in a standardised way, acting as an ‘AI sandbox’. An EU-level association and
a hospital representative from Israel consulted highlighted that having a single platform
where deployment teams can analyse and locally test AI-solutions on high-quality
and anonymised data could accelerate deployment. Such single platforms could:
   • Accelerate sales cycles with real-world validation: demonstrate performance
       in healthcare settings to streamline decision-making and improving go-to-market
       success.
   • Unique performance insights: on how the AI tool performs in varying conditions
       and demographics.
   • Market adaption: evaluate the AI tool in new markets, getting local evidence and
       helping the AI developer to understand and adapt to local healthcare practices.
   • Build collaborations: new strategic partnerships or collaborative research
       opportunities by working closely with the owners of the enterprise platform and
       healthcare providers during evaluations.

A network of assurance laboratories, consisting of hospitals with large datasets and
interested in deploying AI solutions, could serve as a shared resource for developers to
locally test the performance of AI models across different healthcare setting and
populations. This approach could accelerate the pace of development and innovation,

219 Mayo Clinic Platform. Data Behind Glass.



                                                                                            57
                                                      Deployment of AI in healthcare – Final Report


responsive and safe AI deployment, and successful market adoption, including in low-
resource settings that may lack the capability of deployment and performance testing of
AI tools220. Such laboratories could provide different levels of performance testing,
ranging from a technical evaluation of model performance and bias for a specific use
case, to an interpretation of its performance for stratified subgroups of patients, to a
prospective evaluation of usability and adoption via human-machine teaming and
pre-deployment simulation of the consequences of using the model’s output
considering specific policies and work capacity constraints. Additionally, these laboratories
could partner with model developers to help remediate specific areas for
improved performance and adherence to best practices. Independent third-party
testing of AI models—irrespective of the source of the model—may provide a path for
adhering to assurance standards agreed on via a community consensus and would greatly
facilitate governance decisions at health systems about which algorithms are trustworthy.
A blueprint for trustworthy AI implementation guidance and assurance for healthcare in
the form of assurance laboratories as a place to evaluate and validate AI models via an
agreed-on set of community best practices was recently published by such a community 221.

7.1.4 Post-deployment monitoring and maintenance

7.1.4.1 Challenges

The deployment of AI tools is an ongoing process involving continuous monitoring and
adaptation to ensure that AI tools continue to perform as expected. The performance of
AI models can decline over time due to shifts in local input data, changes to
infrastructure or protocols, software updates, or naturally occurring changes in patient
populations and demographics222. Without effective monitoring frameworks to detect and
address these drifts, healthcare providers may be hesitant to trust AI tools for critical
decision-making as undetected performance degradation could have significant impact on
patient safety and care. Therefore, as the use of AI becomes more prevalent and diverse,
institutions using AI should establish ongoing performance oversight as one function
of a local AI governance process223. Strategies for real-world monitoring of AI in clinical
practice should be tailored according to the AI tool and the corresponding risk to patient
safety if model performance declines. The inclusion of a defined baseline input data
characteristic at the time of initial acceptance of the AI tool will allow the system to
monitor for data drift against the baseline 224. By monitoring for individual components of
data drift, institutions could trigger re-evaluation of model performance depending on
timing and severity of changes and initiate appropriate steps to safeguard patient care.

Post-deployment monitoring mechanisms differ from post-market surveillance required
under regulatory approval processes. While post-market surveillance focuses on
compliance, safety reporting, and addressing adverse events to meet regulatory
standards, post-deployment monitoring emphasises the continuous evaluation of an AI
tool’s performance and use in real-world settings. This includes detecting performance
drifts, ensuring alignment with evolving clinical workflows, and maintaining accuracy over
time. Unlike regulatory surveillance, which is typically episodic and compliance-driven,
post-deployment monitoring requires ongoing, proactive oversight tailored to the dynamic
nature of AI systems and their operational environments. This distinction highlights the



220 Shah et al., 2023. A Nationwide Network of Health AI Assurance.
221 Coalition for Health AI (CHAI), 2022. Blueprint for trustworthy AI implementation guidance and assurance
for healthcare.
222 Pianykh et al., 2020. Continuous learning AI in radiology: implementation principles and early applications.
223 Daye et al., 2022. Implementation of Clinical Artificial Intelligence in Radiology: Who Decides and How?
224 Geis, JR. 2023. Drifting away: When you’re A+ decision-making AI machine falls to average… or worse.
need for dedicated frameworks that go beyond regulatory obligations to support the
sustained and effective use of AI in healthcare.

7.1.4.2 Accelerators

Post-deployment monitoring of AI tools used in clinical practice is an important driver for
safe implementation, and sustained use of AI tools. Post-deployment monitoring and
performance assessment was highlighted as an important accelerator for AI
deployment by 80% of HCPs surveyed (41 out of 51). The assurance laboratories
(described in section 7.1.3.2) and the enterprise level platforms (described in section
7.1.1.2) could monitor the ongoing performance of AI models to ensure their intended
objectives are achieved. This would support hospitals to verify the long-term
appropriateness of AI models and provide credible verification of information for the use
of such AI tools. Post-deployment monitoring also allows hospitals to identify when the AI
algorithms do not work as well in a given population and can continually test AI systems
against historical data (according to an HCP from the UK). Post-deployment monitoring
mechanisms to assess the performance of AI systems were employed by 35% (8 out of
23) of the hospital representatives who responded to
this survey question. According to a hospital               “Providing clear, understandable
representative in the USA, the hospital developed an        explanations    for   AI    model
AI Hub to track every AI ‘transaction’, including both      predictions helps clinicians and
inputs and outputs, as well as their own in-house           patients trust the AI system.
solutions to ensure internal monitoring and                 When users can see and
                                                            understand the rationale behind
performance with set thresholds to ensure sustainable
                                                            the AI’s recommendations or
impact. The information collected supports the creation
                                                            decisions, they are more likely to
of quality assurance plans to assess the model’s            rely on and accept these tools.” –
performance over time which is shared with the AI           AI developer from France.
developer to make the necessary adjustments to the
model should they be necessary, ensuring that AI tools
remain effective and reliable. According to a hospital representative consulted, in Portugal,
the hospital collects and analyses post-deployment data to evaluate the impact and
ongoing effectiveness of AI tools. This helps in making data-driven decisions for further
improvements and ensuring that AI solutions continue to meet clinical needs.

Sustaining the use of AI tools within healthcare settings can be reinforced by creating a
support system after the deployment process225. Suitable strategies to reinforce this
support system is the organisation of information sharing meetings between
hospital representatives and AI developers. These meetings can be utilised in order
to facilitate “check-ups” on the AI tool deployed in terms of its functioning and identify
future possibilities. Collaboration between hospitals and developers of AI tools to monitor
performance of AI systems post-deployment was highlighted by a number of hospital
representatives consulted. Such an approach, already employed by a hospital in Sweden,
allows the developer of the AI solution to update the AI algorithm when necessary and
ensure it effectively meets the hospital’s specific needs and positively impacts patient
outcomes. An AI developer from the USA stated that they meet with HCPs on a weekly
basis immediately post-deployment which allows for early detection of performance
issues or model degradation. In addition to this meeting, the AI Developer reflected that
an internal service desk handling deviation reports and answering questions and
a dedicated contact person from the AI developer side who could be contacted any
time was a valuable bridge to support HCPs. Another strategy implemented by a hospital
representative from the USA is to establish a cross-functional governance committee

225 Nair et al., 2024. A comprehensive overview of barriers and strategies for AI implementation in
healthcare: Mixed-method design.



                                                                                                      59
                                                         Deployment of AI in healthcare – Final Report


for AI implementation, which is recommended to meet monthly. Such committees
include professionals from the closest to the patient (HCPs) to innovation managers and
leaders of the organisation. The committee’s goals could include AI’s usage promotion,
training new users in terms of application and workflow, tracking effectiveness and
compliance, reporting, and planning financial sustainability for continuing using the AI
system in the organisation. The agenda of such a committee could also include reviewing
individual patient cases where the treatment had failed to increase learning.

Effective post-deployment monitoring also allows deployers to monitor how end-users
interact with the AI solution over time. An approach described by a hospital representative
from Canada allows the identification of low or inadequate use of deployed AI tools. This
information can be used to follow-up with end-users on the reasoning behind the
low/inadequate utility and inform approaches to encourage engagement and future tool
improvements. Additional post-deployment monitoring mechanisms already employed by
hospitals in Canada and the USA include running surveys with HCPs using or affected by
deployed AI solutions to monitor the impact of the tool on their clinical practice, as well as
integrating patient satisfaction, where relevant, as an additional key performance indicator
to monitor the impact of the AI tool.

7.1.5 Transparency and explainability

7.1.5.1 Challenges

The term “black box” refers to a phenomenon whereby an AI algorithm reaches a
conclusion without users being able to understand the basis or ‘see inside’ the system 226.
The difficulty in interpreting and tracing the techniques used by some AI models
and the lack of explainability could in certain instances erect barriers to AI deployment.
The lack of transparency and explainability could in some instances be argued to
contradict evidence-based medicine, which relies on HCPs understanding both the
scientific and clinical bases of the recommendations provided by AI and high standards of
explainability to confidently validate and apply the decision 227. The lack of transparency
and explainability of AI tools was described as a challenge affecting the deployment of AI
in healthcare by 41% of HCPs (20 out of 49), 58% of hospital representatives (15 out of
26), and 38% of AI developers (13 out of 34) that responded to the survey question. In
addition, 59% of patients and patient associations that responded to the survey (41 out
of 70) expressed concerns regarding the lack of information on how decisions are made
by AI systems. This lack of HCP oversight could lead to errors in clinical settings. One
example is the study from Mount Sinai Hospital, where an AI model's predictive
performance relied on data from specific x-ray machines rather than clinically relevant
data. This misinterpretation was uncovered through explainability methods, emphasising
the need for robust transparency measures228. The degree of explainability however, may
vary according to the use case in question. For example, greater explainability may be
warranted for high stakes, nuanced, decision-making such as choosing the right antibiotic
in a septic, immunosuppressed patient or determining organ donor and recipient
matches229. A hospital representative from Israel highlighted that HCPs do not necessarily
need to understand the complex computational processes behind AI algorithms but should
be able to understand what specific features resulted in the AI algorithms decision. Such
an approach fosters trust, promotes responsible usage, and establishes a common
understanding between AI developers and HCPs.


226 Poon et al., 2021. Opening the black box of AI-Medicine.
227 Morrison K, 2021. Artificial intelligence and the NHS: a qualitative exploration of the factors influencing
adoption.
228 Amann et al., 2020. Explainability for artificial intelligence in healthcare: a multidisciplinary perspective
229 Scott et al., 2024. Achieving large-scale clinical adoption of AI-enabled decision support.
Despite the importance of explainability, there is a trade-off when it comes to accuracy.
This is particularly relevant in consideration that full explainability in some instances is
neither possible nor necessary for HCP and patient acceptance 230. In a study conducted in
the UK, citizen jurors favoured accuracy over explainability of AI tools because of the
potential for harm from inaccurate predictions and the potential of accurate tools to
increase the efficiency of, and access to, care 231. In addition, the value to HCPs of any
explanation will vary according to the specific model and its use case and the expertise
(i.e., level of AI or domain knowledge), preferences for accuracy relative to explainability
and other contextual values of the user232.

The lack of transparency and explainability could result in a lack of trust amongst HCPs
and patients, and subsequently could negatively impact the doctor-patient
relationship (see section 7.4.4). There is an overall lack of agreement on the different
levels of explainability, no clear guidance on how to choose among different explainability
methods and an absence of standardised methods for evaluating explainability 233.
Explainability methods may present plausible but misleading explanations and may
subsequently affect the human ability to detect model mistakes, resulting in decreased
vigilance and auditing of AI tools and over-reliance on their outputs234.


7.1.5.2 Accelerators

There is a need to improve transparency and explainability of AI tools to build trust of
deployers, facilitating acceptability and the adoption of such tools 235. Short and concise
guidelines on how the AI model works to ensure transparency, interpretability and
explainability was highlighted as a good practice to facilitate AI deployment by 67% of
HCPs surveyed (34 out of 51). According to HCPs consulted, this could be achieved by
creating a user-friendly interface of the AI tool with input from experts in the field. This
would subsequently reduce the complexity and ensure that HCPs can efficiently and
accurately interpret model decisions without having to have extensive technical knowledge
of the tool to interpret confidence scores, visualise hidden layers, and conduct sensitivity
analyses. This can be achieved by the creation of clear and comprehensive guidelines
addressing the following points:
    1. Having mechanisms in place to support HCPs in case of disagreements on
        decisions due to a lack of transparency and explainability236.
    2. Revealing the process of how the algorithm was developed, who was involved in
        the development process, whether clinicians were consulted, and how the data was
        processed237.



230 Van der Veer et al., 2021. Trading off accuracy and explainability in AI decision-making: findings from 2
citizens’ juries.
231 Van der Veer et al., 2021. Trading off accuracy and explainability in AI decision-making: findings from 2
citizens' juries.
232 Bienefeld et al., 2023. Solving the explainable AI conundrum by bridging clinicians’ needs and developers’
goals.
233 Ghassemi et al., 2021. The false hope of current approaches to explainable artificial intelligence in
healthcare.
234 Tonekaboni et al., 2019. What clinicians want: contextualizing explainable machine learning for clinical end
use.
235 Watson et al., 2020. Overcoming barriers to the adoption and implementation of predictive modelling and
machine learning in clinical care: what can we learn from US academic medical centers?
236 Li et al., 2021. Digital technology, tele-medicine and artificial intelligence in ophthalmology: a global
perspective.
237 Sangers et al., 2021. Views on mobile health apps for skin cancer screening in the general population: an
in-depth qualitative exploration of perceived barriers and facilitators.



                                                                                                             61
                                                       Deployment of AI in healthcare – Final Report


     3. Informing HCPs about what the AI takes as input, how the input is processed,
        and what the AI produces as output238.
     4. Producing user-friendly visualisations of output that are readily understood
        and clinically actionable239 (HCPs prefer graphical or numerical displays of
        probabilities or alert thresholds for a diagnosis, confidence scores for these outputs
        and links to relevant, consistent recommendations for tests or treatments 240).
     5. Clearly presenting information about the indications and contraindications
        of the AI model, demonstrating awareness of its strengths and weaknesses (e.g.,
        in the form of model report cards that are regularly updated, see section 7.1.3.2,
        or model facts label, see Box 2).
     6. Using established explainable AI methods that strike a balance between
        explainability and high accuracy.

Additionally, according to the patients/patient associations surveyed, 55% of respondents
(39 out of 70) reported that clear communication from HCPs on how the AI model works
and comes to its decisions would make them more comfortable with AI being used in their
healthcare.

                       Box 2: The “Model Facts” label developed by the FDA241.
 •    Defined by the United States Food and Drug Administration (FDA) as “the term of art used
      for situations when people need good information to make sound choices”.
 •    The “Model Facts” label was designed by an interdisciplinary team including developers,
      clinicians, and regulatory experts.
 •    The target audience are HCPs who make decisions supported by an AI model.
 •    The purpose is to collate relevant, actionable information in 1-page to ensure that HCPs know
      how, when, how not, and when not to incorporate model output into clinical decisions.
 •    The label also contains important information about the model, such as the demographic
      representation of training and evaluation data.
 •    The “Model Facts” label needs to be localized and needs to be updated over time. “Model
      Facts” labels include information about model performance within the local population. If a
      model is adopted in a new setting, a new “Model Facts” label needs to be generated and
      distributed to clinical end users.
 •    The target population of model use is also specified in both the “Uses and directions” and
      “Validation and performance” sections.
 •    The version of the “Model Facts” label is documented and version control with documentation
      of changes should be accessible to all end users.



7.1.6 High-level overview of the EU regulatory landscape

The current EU regulatory framework may both directly and indirectly in shape some of
the technological and data challenges affecting the deployment of AI in healthcare. The
section below presents a high-level non-exhaustive summary overview of key regulation
to be considered in the view of the challenges identified and should be reflected in line
with the limitations of this study identified in section 3.5.




238 Hassan et al., 2024. Barriers to and facilitators of Artificial Intelligence adoption in health care: Scoping
review.
239 Scott et al., 2024. Achieving large-scale clinical adoption of AI-enabled decision support.
240 Tschandl et al., 2020. Human-computer collaboration for skin cancer recognition.
241 Sendak et al., 2020. Presenting machine learning model information to clinical end users with model facts
labels.
At the outset and as a foundation, the GDPR (Regulation (EU) 2016/679)242 ensures that
personal data is processed lawfully, securely, and transparently, protecting individuals’
rights while enabling responsible data use. This minimises risks associated with data
misuse and fosters public confidence in AI-driven healthcare solutions. Frameworks like
the EHDS243 promote some level of data standardisation, data quality (primary use),
interoperability and secure access, particularly to electronic health data for secondary
use (see also section 5.1.7).

The measures on interoperability for primary uses of electronic health data could aid AI
integration into clinical practice. Under the EHDS, the Commission shall establish a central
interoperability platform for digital health (‘MyHealth@EU’) to provide services to support
and facilitate the exchange of personal electronic health data for primary use between the
national contact points for digital health of the Member States (Article 23 EHDS). Also of
relevance are the obligation in the EHDS providing that EHR systems shall include a
European interoperability software component for EHR systems and a European logging
software component for EHR systems (the ‘harmonised software components of EHR
systems’), in accordance with the provisions laid therein (Art. 25 EHDS). In addition,
manufacturers of medical devices or in vitro diagnostic medical devices, that claim
interoperability of those medical devices or in vitro diagnostic medical devices with the
harmonised software components of EHR systems shall prove compliance with the
essential requirements on the European interoperability software component for EHR
systems and the European logging software component for EHR systems, laid down in
Section 2 of Annex II to the EHDS (Article 27 EHDS).

The provisions in the EHDS on secondary uses of data are also of relevance as they provide
the possibility to access diverse health data for defined purposes including training, testing
and evaluation of algorithms. In this respect, there are measures on health data quality
and utility for secondary use (see dataset description and dataset catalogue (Art. 77
EHDS), data quality and utility label (Art. 78 EHDS), EU dataset catalogue (Art. 79 EHDS),
minimum specifications for datasets of high impact (Art. 80 EHDS).

The AIA244 sets standards for, among others, high-risk AI systems (see section 5.1.3 for
the different risk categories covered by the AIA), ensuring transparency, robust risk
management, and accountability throughout the AI lifecycle. The AIA lays down a
uniform legal framework in particular for the development, the placing on the market, the
putting into service and the use of artificial intelligence systems (AI systems) in the Union,
in accordance with Union values, to promote the uptake of human centric and trustworthy
artificial intelligence while ensuring a high level of protection of health, safety, fundamental
rights (recital 1 AIA).

The AIA mandates that high-risk AI systems shall be designed and developed in such a
way as to ensure that their operation is sufficiently transparent to enable deployers to
interpret a system’s output and use it appropriately (Art. 13 AIA). Additionally high-risk
AI systems shall be designed and developed in such a way that they achieve an
“appropriate level of accuracy, robustness, and cybersecurity, and that they perform
consistently in those respects throughout their lifecycle” (Art. 15 AIA). As noted in the


242 Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the
protection of natural persons with regard to the processing of personal data and on the free movement of such
data, and repealing Directive 95/46/EC (General Data Protection Regulation)).
243 Regulation (EU) 2025/327 of the European Parliament and of the Council of 11 February 2025 on the
European Health Data Space and amending Directive 2011/24/EU and Regulation (EU) 2024/2847.
244 Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down
harmonised rules on artificial intelligence and amending Regulations (EC) No 300/2008, (EU) No 167/2013,
(EU) No 168/2013, (EU) 2018/858, (EU) 2018/1139 and (EU) 2019/2144 and Directives 2014/90/EU, (EU)
2016/797 and (EU) 2020/1828 (Artificial Intelligence Act)



                                                                                                           63
                                                   Deployment of AI in healthcare – Final Report


recitals of the AIA (see recital 71 AIA) “having comprehensible information on how high-
risk AI systems have been developed and how they perform throughout their lifetime is
essential to enable traceability of those systems, verify compliance with the requirements
under the AIA as well as monitoring of their operations and post market monitoring.
Consequently, there are requirements on keeping records and the availability of technical
documentation, containing information which is necessary to assess the compliance of the
AI system with the relevant requirements and facilitate post market monitoring”.
Additional transparency obligations for providers and deployers of certain AI systems are
presented within Art. 50.

The MDR245 and IVDR246 subjects AI Medical Devices (MDAI) to vigorous requirements
through clinical investigation/clinical performance studies and conformity assessment
(Chapter VI of the MDR and Chapter VI of the IVDR). Additionally, manufacturers must
maintain robust clinical evidence and technical documentation (MDR Art. 10, and IVDR
Art. 10).

The AIA places distinct obligations on providers of high-risk AI systems, including pre-
market conformity assessment procedures (Articles 24, 43, 47, and 48 AIA). High-risk AI
systems which make use of techniques involving the training of AI models with data to be
developed on the basis of training, validation and testing data sets that meet the quality
criteria referred to therein (Art. 10 AIA), providers of high-risk AI systems shall put a
quality management system in place that ensures compliance with the AIA including
examination, test and validation procedures to be carried out before, during and after the
development of the high-risk AI system, and the frequency with which they have to be
carried out (Art. 17 AIA); transparency and provision of information to deployers also
encompassing the level of accuracy, including its metrics, robustness and cybersecurity
against which the high-risk AI system has been tested and validated and which can be
expected, and any known and foreseeable circumstances that may have an impact on that
expected level of accuracy, robustness and cybersecurity (Art. 13). For AI systems
classified as medical devices, the MDR (Chapter VII) and IVDR (Chapter VII) enforce
rigorous post-market surveillance requirements.

While the AIA, MDR and IVDR post-monitoring primarily focus upon safety, technical
performance, and compliance — findings from our study suggest that complementary
forms of post-deployment monitoring mechanisms may help foster trust and adoption of
AI in healthcare. Beyond technical oversight, deployers and stakeholders in healthcare
environments may benefit from post-deployment evaluations that capture qualitative
insights, such as user satisfaction, physician and patient feedback, and alignment
with clinical workflows. For instance, some initiatives highlight the value of holistic
monitoring approaches that go beyond technical metrics to assess whether AI systems
effectively address local needs, improve patient outcomes, and enhance healthcare
efficiency. These broader monitoring practices complement existing regulatory obligations
by providing a more comprehensive understanding of AI’s real-world impact, ultimately
supporting continuous improvement and increasing stakeholder confidence in AI tools.
This underscores the importance of integrating both technical and qualitative post-
monitoring measures into deployment strategies. During the workshop conducted with EU
regulatory experts, the variation in AI performance across healthcare settings and
populations, as well as the importance of conducting local performance studies, was
discussed. Experts acknowledged that frameworks like the MDR and IVDR and AIA aim

245 Regulation (EU) 2017/745 of the European Parliament and of the Council of 5 April 2017 on medical
devices, amending Directive 2001/83/EC, Regulation (EC) No 178/2002 and Regulation (EC) No 1223/2009
and repealing Council Directives 90/385/EEC and 93/42/EEC
246 Regulation (EU) 2017/746 of the European Parliament and of the Council of 5 April 2017 on in vitro
diagnostic medical devices and repealing Directive 98/79/EC and Commission Decision 2010/227/EU
to ensure robust performance. However, concerns were raised about the need for
additional complementary actions to assess AI performance in specific local contexts.
Experts highlighted that addressing these variations—through local performance testing
processes (see sections 7.1.3 and 7.1.4)—could mitigate risks of healthcare disparities
and ensure equitable access to AI benefits.

7.1.7 Summary

The deployment of AI in healthcare faces several technological and data challenges. Data
heterogeneity complicates AI integration due to differences in data types, structures, and
formats across systems, limiting interoperability and requiring complex data conversion
processes. The lack of interoperable systems further exacerbates this issue, increasing
operational inefficiencies and creating workflow disruptions that hinder AI adoption.
Additionally, outdated IT infrastructure in many healthcare facilities, particularly in
underfunded regions, limits the computational capabilities necessary for AI deployment.
The absence of standardised local performance testing protocols also affects AI
deployment, as AI performance varies across healthcare settings and medical specialties,
and there is a lack of clear benchmarks for accuracy and effectiveness. Post-deployment
monitoring is another important challenge, as AI models require continuous oversight to
detect performance drifts and maintain reliability in real-world settings. Furthermore, the
“black box” nature of many AI models raises concerns about transparency and
explainability, leading to trust issues among HCPs and patients. Addressing these
challenges is important for ensuring the seamless integration, scalability, and responsible
use of AI in healthcare.

To overcome technological and data challenges in AI deployment in healthcare, several
accelerators have been identified. Ensuring data standardisation and interoperability
through seamless integration with existing hospital IT systems, early collaboration
between AI developers and deployers, and adopting common data standards like FHIR and
OMOP can facilitate data exchange. Investing in modern IT infrastructure, including
high-performance computing, cloud storage, and modular architecture, is important for AI
scalability, though security and regulatory concerns impact cloud adoption. Establishing
robust performance testing protocols through multi-site local performance studies,
federated data-sharing networks, and AI sandboxes can enhance real-world AI
performance assessments and address variations in performance across diverse
healthcare settings. Post-deployment monitoring frameworks, such as AI hubs and
governance committees, ensure AI tools maintain effectiveness and compliance over time.
Additionally, improving transparency and explainability with user-friendly
visualisations, confidence scores, and standardised reporting can build trust among
healthcare professionals and patients. Implementing such strategies could enhance AI
adoption, ensuring safe, effective, and scalable integration into clinical workflows.

    7.2    Legal and regulatory challenges and accelerators
There are a number of different legal and regulatory challenges affecting the deployment
of AI in healthcare that can be grouped into three categories presented in the section
below.

7.2.1 Complex regulatory landscape

7.2.1.1 Challenges

The healthcare sector is highly regulated, and obtaining approval for AI applications can
be a lengthy process, which can limit the ability of these innovations to reach the market
(see section 5). The complexity of the regulatory approval process for AI product
commercialisation was described as a significant challenge to AI deployment according to



                                                                                        65
                                                       Deployment of AI in healthcare – Final Report


47% of HCPs (23 out of 47), 56% of hospital representatives (14 out of 25), and 62% of
AI developers (21 out of 32) that responded to the survey question. Regulatory experts
during the workshop highlighted that the administrative burden of ensuring compliance
with these regulations, coupled with the need for extensive documentation, may deter
healthcare institutions from adopting AI tools, particularly those with limited resources or
technical expertise. Sustained use of AI tools may be further complicated by the need for
post-market surveillance obligations. This may require robust infrastructure, technical
capacity, and interdisciplinary collaboration, which are often challenging to maintain over
time.

The uncertainty surrounding regulatory interpretations 247 also impacts deployment.
Healthcare stakeholders, including HCPs and hospital representatives, may struggle to
understand the nuanced requirements for using AI in clinical settings leading to delays in
adoption as organisations seek legal or technical guidance to ensure compliance, or avoid
AI altogether due to fear of non-compliance and associated liabilities. In addition, the
complex regulatory landscape and associated procedures (e.g., thorough clinical
evaluations, risk management procedures, and post-market surveillance to ensure the
safety and performance of medical devices) can sometimes prolong the time it takes for
AI tools to reach the market. This subsequently delays the deployment of AI-based
medical devices into clinical practice and increase the cost of deploying the AI solution in
Europe. In the USA, where regulatory approval processes are shorter, the cost of AI
solutions is often lower according to an AI developer from Israel.

7.2.1.2 Accelerators

Regulatory guidance and clarification of roles throughout the deployment process was
highlighted as a good practice by 67% of HCPs surveyed (34 out of 51). To address the
above-mentioned challenges, hospital representatives consulted from Italy, Israel and the
USA, have established a legal support at hospital level with knowledge of the regulatory
landscape impacting the deployment of AI solutions from the perspective of the deployers.
Another effective strategy employed by two hospitals in the USA is the establishment of
interdisciplinary AI governance committees comprising HCPs, IT specialists, legal experts,
data scientists, and compliance officers. These committees are responsible for assessing
potential AI tools, ensuring alignment with regulatory requirements, and overseeing the
integration of these tools into clinical workflows. According to hospital representatives who
answered the survey question, 61% (13 out of 21) have implemented dedicated
compliance teams to oversee the process of AI deployment from the regulatory
perspective. By centralising decision-making within hospitals and fostering cross-
functional collaboration, hospitals can navigate the regulatory landscape more efficiently
and mitigate risks associated with non-compliance.

7.2.2 Data security and privacy

7.2.2.1 Challenges

Concerns surrounding data privacy and data protection was described as a significant
challenge to AI deployment according to 49% of HCPs (23 out of 47), 56% of hospital
representatives (14 out of 26), and 44% of AI developers (14 out of 32) that responded
to the survey. In addition, 54% of the patients and patient associations that responded to
the survey (38 out of 70) expressed concerns about data privacy, confidentiality and
security. A primary concern shared by hospital representatives from Europe, Japan and
the USA is the uncertainty about where and how the data processed by AI solutions is
stored. Many AI tools, particularly those relying on cloud-based platforms, may require


247 See limitations section of this report with regard to the timing of the analysis conducted in this study and
the evolving regulatory environment.
data to be transferred and stored across different jurisdictions, potentially outside the EU.
This raises concerns about compliance with the GDPR and the risk of unauthorised access,
especially in regions with weaker data protection standards, a concern raised by a hospital
representative from Belgium. Healthcare providers hesitate to adopt AI solutions without
robust assurances that data storage and processing comply with local and international
privacy regulations.

In addition, another concern involves the potential misuse of data collected by AI tools.
Consulted stakeholders highlighted concern that sensitive health data, initially used for
specific diagnostic or therapeutic purposes, could be repurposed for secondary uses, such
as commercial profiling or research, without a proper legal basis. This is exacerbated by a
lack of transparency in how some AI solutions handle data after deployment, creating
challenges in maintaining patient trust.

Concerns surrounding cybersecurity and vulnerability of data to breaches was
described by 38% of HCPs (18 out of 47), 52% of hospital representatives (13 out of 25),
and 48% of AI developers (15 out of 31). The sensitive nature of medical data makes it a
prime target for malicious activities, and the integration of AI introduces additional
vulnerabilities, such as insecure APIs, model inversion attacks, or adversarial exploitation
of algorithms 248. A breach involving an AI system not only jeopardises patient
confidentiality but also undermines trust in the technology, prompting regulators and
providers to adopt stricter data protection measures. These measures, while essential, can
increase the cost and complexity of deploying AI solutions, further discouraging adoption.

7.2.2.2 Accelerators

To address the concerns surrounding data privacy and security, there is a need for
comprehensive data governance framework clarifying the role of all stakeholders in data
processing. Policies and guidance on information access and sharing within healthcare
facilities was highlighted as a good practice by 61% of HCPs surveyed (28 out of 51). As
a foundational step, these frameworks should establish clear governance protocols that
outline responsibilities, accountability, and processes for data oversight. They must define
protocols for data storage, access, and processing by AI solutions, ensuring compliance
with regulations like GDPR and the EHDS. A key practice identified in this study is the
employment local data storage solutions as described by a hospital representative from
South Korea or using certified cloud providers that adhere to stringent data protection
standards, as described by hospital representatives from Israel and Canada. By keeping
data within jurisdictions with robust privacy laws, healthcare providers may mitigate
concerns about unauthorised access or misuse. Employing advanced encryption methods
ensures that patient information remains secure, even in the event of unauthorized access.
This includes de-identifying data for data stored on local or cloud servers, an approach
employed by several hospitals in the USA and Israel. In addition, according to an AI
developer from the USA, integrating privacy-by-design technologies into AI solutions that
incorporate advanced data protection features helps address some of the challenges
related to data privacy 249.

In addition, prior to deploying AI solutions, it is important to assess them to ensure they
comply with data security and privacy standards. Clarification on how privacy and data
protection rules apply to AI is a good practice employed by 61% of the hospital
representative surveyed (13 out of 21). A number of hospital representatives consulted
(42% of hospital representatives surveyed Hospital representatives from Israel referenced


248 Ahmad et al., 2020. Barriers and pitfalls for artificial intelligence in gastroenterology: ethical and
regulatory issues.
249 Wolf et al., 2021. Success factors of artificial intelligence implementation in healthcare.



                                                                                                             67
                                                       Deployment of AI in healthcare – Final Report


a dedicated internal review board responsible for reviewing and assessing ethical and
regulatory considerations for each new AI tool prior to deployment. Other hospital
representatives in the USA, had implemented a rigorous review process for all third-party
vendors and strategic partners, ensuring they meet stringent security standards to protect
patient data used by these AI solutions and prevent potential data breaches. According to
the patients/patient associations surveyed, 44% (31 out of 70)of respondents reported
that clear communication of data protection measures when using AI would make them
more comfortable with AI being used in their healthcare.

Informed consent protocols to maintain patient autonomy and data privacy was
highlighted as a good practice by 61% (31 out of 51) of the HCPs surveyed. A hospital in
the USA has implemented a policy requiring verbal or written informed consent prior to
deploying AI solutions in patient care. This required the establishment of clear and
coherent communication mechanisms for patients impacted using such AI solutions.
However, the hospital outlines that there is a lack of guidance on when patient consent
should be obtained, for what types of AI applications, and what specific information needs
to be provided to the patients. According to the patients/patient associations surveyed,
53% of respondents (37 out of 70) reported that informed consent on the use of AI in the
delivery of care would make them more comfortable with AI being used in their healthcare.

7.2.3 Liability

7.2.3.1 Challenges

There are growing concerns amongst hospital representatives and HCPs as to who is liable
or responsible for a bad outcome where decision-making was guided, or in some instances
even entirely devolved, to AI tools 250,251. Additionally questions regarding the extent to
which an HCP should follow the advice of an AI tool, and their liability in the event that AI
advice is ignored and later shown to have caused harm. Lack of clarity in liability was
described as a significant challenge to AI deployment according to 43% of HCPs (20 out
of 47), 40% of hospital representatives (10 out of 25), 22% of AI developers (7 out of 32)
who responded to this survey question. In addition 57% of patients/patient associations
(40 out of 70) that responded to the survey also flagged concerns regarding liability. Such
concerns may lead to slow uptake or lack of use altogether of AI tools. Additionally, during
interviews, hospital representatives and HCPs highlighted the need for clear guidance for
hospitals on which AI applications require consent when used for some clinical tasks and
what specific information should be communicated to patients.


7.2.3.2 Accelerators

Regulatory guidance to define user responsibilities and liabilities concerning AI models was
highlighted as a good practice to address the abovementioned challenge by 80% of the
HCPs surveyed (41 out of 51). According to the patients/patient associations surveyed,
70% of respondents (49 out of 70) reported that clear information related to liability in
case of errors or adverse outcomes caused by AI systems would make them more
comfortable with AI being used in their healthcare. For example, a hospital representative
from Portugal highlighted that they are establishing clear liability framework to define the
responsibilities of all parties involved in AI deployment.

A step is to also avoid grouping all AI applications together, as the potential AI use cases
in healthcare vary widely-from image analysis to precision medicine-with some tools being


250 Ho et al., 2019. Governance of automated image analysis and artificial intelligence analytics in healthcare.
251 The timing of the analysis (prior to the updated PLD) should be carefully considered in reflection of the
findings presented.
riskier than others. A policy brief from Stanford University 252 described a framework for
establishing liability that conceptualises risk as a function of four major factors and
recommends calibrating adoption decisions and post-deployment safety monitoring based
on these risk indicators:

    •   The likelihood and nature of errors (based on the AI model, its training data, its
        task design, and how it is integrated into clinical workflow).

    •   The likelihood that humans or another system will detect errors before they harm
        patients (which depends in part on how much time with and visibility into the AI
        tool humans have).

    •   The potential harm if errors are not caught (especially for tools that perform critical
        clinical functions or are used in caring for patients with serious health conditions).

    •   The likelihood that injuries would garner compensation in the tort system (which
        turns on, among other things, the severity of the injury, the ease of proving
        negligence, and the causal relationship between the AI tool and the injury).

In addition to the above, having clearly defined mechanisms to assess and monitor risk,
test the performance of AI systems prior to widespread deployment (see section 7.1.3.2),
and monitoring the performance of AI systems post-deployment are effective mechanisms
to address concerns regarding liability. Deployers of AI systems can also use
indemnification clauses253 to establish who is responsible for paying in the case of a claim
(e.g., requiring that developers pay for errors in the model’s output while hospitals pay
for errors arising from poor deployment or misuse of the AI technology). Regulators,
policymakers, and deployers could also establish guidelines for informing patients when
AI is used in diagnostic or treatment decisions to provide a basis for informed consent,
addressing some of the liability concerns of HCPs.



7.2.4 High-level overview of the EU regulatory landscape

The section below presents a high-level non-exhaustive summary overview of key
regulation to be considered in the view of the challenges identified and should be reflected
in line with the limitations of this study identified in section 3.5.

The AIA254 and the MDR255/IVDR256 present obligations on the development and, to
some extent, the deployment of AI systems in healthcare. These include requirements
related to transparency, cybersecurity, risk management, pre-market assessments, and
post-market surveillance. Together, these frameworks provide guidance to support the
safe, effective, and ethical development and deployment of AI systems in healthcare.
However, deployers must navigate compliance processes which can be complex. This




253 Provisions in contracts that require one party to compensate or reimburse another party for losses,
damages, liabilities, or costs that arise from certain actions or events specified in the agreement
254 Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down
harmonised rules on artificial intelligence and amending Regulations (EC) No 300/2008, (EU) No 167/2013,
(EU) No 168/2013, (EU) 2018/858, (EU) 2018/1139 and (EU) 2019/2144 and Directives 2014/90/EU, (EU)
2016/797 and (EU) 2020/1828 (Artificial Intelligence Act)
255 Regulation (EU) 2017/745 of the European Parliament and of the Council of 5 April 2017 on medical
devices, amending Directive 2001/83/EC, Regulation (EC) No 178/2002 and Regulation (EC) No 1223/2009
and repealing Council Directives 90/385/EEC and 93/42/EEC
256 Regulation (EU) 2017/746 of the European Parliament and of the Council of 5 April 2017 on in vitro
diagnostic medical devices and repealing Directive 98/79/EC and Commission Decision 2010/227/EU



                                                                                                           69
                                                     Deployment of AI in healthcare – Final Report


underscores the importance of fostering coordination among these frameworks, ensuring
that AI deployers have clear pathways to meet their obligations without uncertainty.

When addressing data privacy and security concerns, the GDPR257 remains the
cornerstone of data protection in the EU. It sets clear obligations for entities processing
personal data of individuals within the EU, ensuring robust safeguards for individual rights.
For organisations deploying AI in healthcare, GDPR compliance is critical, particularly in
managing sensitive health data, ensuring lawful processing, and addressing principles such
as data minimisation and purpose limitation. Additionally, the AIA includes provisions on
cybersecurity which state that high-risk AI systems shall be designed and developed in
such a way that they achieve an appropriate level of cybersecurity, and that they perform
consistently in those respects throughout their lifecycle (Article 15 AIA).

Regarding liability, the recently updated PLD258 includes software, AI systems, and
digital services within its scope. This ensures that AI systems are clearly recognised as
products under EU liability law, addressing previous ambiguities and enhancing the legal
framework for liability in AI-driven healthcare solutions. The updated PLD by introducing
measures to ease the burden of proof in liability claims involving AI systems, aids to
address some of the unique challenges associated with these technologies. In a product
liability case, the claimant (plaintiff) is required to prove the defectiveness of the product,
the damage suffered and the causal link between that defectiveness and that damage.

As regards product liability cases, the updated PLD provides presumptions concerning
causation that will aid in dealing with the issue of causation. The updated PLD provides
that the causal link between the defectiveness of the product and the damage shall be
presumed where it has been established that the product is defective and that the damage
caused is of a kind typically consistent with the defect in question (Article 10 PLD). A
national court shall presume the defectiveness of the product or the causal link between
its defectiveness and the damage, or both, where, despite the disclosure of evidence as
required in the updated PLD and considering all the relevant circumstances of the case.
Specifically when (a) the claimant faces excessive difficulties, in particular due to technical
or scientific complexity, in proving the defectiveness of the product or the causal link
between its defectiveness and the damage, or both; and (b) the claimant demonstrates
that it is likely that the product is defective or that there is a causal link between the
defectiveness of the product and the damage, or both. (Article 10 PLD). The updated PLD
also provides that the defendant shall have the right to rebut some of these presumptions.
(Article 10 PLD).

The transparency provisions in the AIA may also enhance clarity in the usage of AI systems
in healthcare and therefore enhance the trust of HCP as well as a step in aiding to clarify
the liability of HCPs in using AI systems. Article 13 provides that high-risk AI systems shall
be designed and developed in such a way as to ensure that their operation is sufficiently
transparent to enable deployers to interpret a system’s output and use it appropriately.
Additionally, the provisions in the AIA on human oversight could provide further clarity to
the interaction between HCP and AI. Article 14 AIA provides that high-risk AI systems shall
be designed and developed in such a way, including with appropriate human-machine
interface tools, that they can be effectively overseen by natural persons during the period
in which they are in use. The aim of human oversight shall be to prevent or minimise the
risks to health, safety or fundamental rights that may emerge when a high-risk AI system


257 Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the
protection of natural persons with regard to the processing of personal data and on the free movement of such
data, and repealing Directive 95/46/EC (General Data Protection Regulation)).
258 Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for
defective products and repealing Council Directive 85/374/EEC
is used in accordance with its intended purpose or under conditions of reasonably
foreseeable misuse, in particular where such risks persist despite the application of other
requirements set out therein. Moreover, Article 14 AIA provides that the oversight
measures shall be commensurate with the risks, level of autonomy and context of use of
the high-risk AI system and shall be ensured through different types of measures set
therein. Finally, the obligations on deployers of high-risk AI systems (Art. 26) provide
further clarity in the how AI systems should be used.

Accountability is also enhanced by the AIA with different obligations such as the obligation
to draw up a technical documentation of a high-risk AI system before that system is placed
on the market or put into service and be kept up-to date (Article 11 AIA).

As far as issues of regulatory complexity are concerned, the AIA includes provisions to aid
in simplifying the regulatory landscape. Some of these measures, include AI sandboxes
for testing (Art. 58) and guidelines on the practical implementation of the AIA that are
being developed by the commission; the harmonised standards to be developed across
the EU will also provide further clarity (Art. 40). In the context of standards, the
Commission issued a standardisation request to the European Committee for
Standardisation and the European Committee for Electrotechnical Standardisation in
support of Union policy on artificial intelligence. This request includes European
standard(s) and/or European standardisation deliverable(s) for example on human
oversight of AI systems259. Moreover, the Commission sets course for Europe's AI
leadership with an ambitious AI Continent Action Plan. The AI Act raises citizens' trust in
technology and provides investors and entrepreneurs with the legal certainty they need to
scale up and deploy AI throughout Europe. In this regard, the Commission will launch the
AI Act Service Desk, to help businesses comply with the AI Act. It will serve as the
central point of contact and hub for information and guidance on the AI Act 260.

It was highlighted during the regulatory workshop with stakeholder, there are nuances in
practical implementation—such as localised challenges in aligning diverse frameworks and
the need for more granular guidance on addressing specific concerns like contextual bias,
operational performance in varied settings, and inter-regulatory interactions. This
highlights the importance of continuous dialogue and exploration of complementary
measures to support the effective deployment of AI systems in healthcare. Such efforts
can help ensure that AI solutions align not only with technical and regulatory requirements
but also with the broader societal and clinical contexts in which they operate.

7.2.5 Summary

The deployment of AI in healthcare faces several legal and regulatory challenges. As
developers and deployers they may need to comply with multiple frameworks such as the
AIA, GDPR, MDR/IVDR, and upcoming EHDS complexities may occur in the navigation of
this landscape. Data security and privacy concerns, particularly regarding cross-border
data storage and cybersecurity threats, create some concerns to the stakeholders
consulted and this may lead to a hesitation in adopting AI without robust data protection
assurances. Liability issues may also raise challenges, for example, concerning the
liability of healthcare professionals using AI systems.

To address challenges in AI deployment in healthcare, several accelerators have been
identified. For example, at clinical setting, to navigate the complex regulatory


259 Commission implementing Decision of 22.5.2023 on a standardisation request to the European Committee
for Standardisation and the European Committee for Electrotechnical Standardisation in support of Union policy
on artificial intelligence Brussels, 22.5.2023 C(2023) 3215 final
260 EU Commission (2025) Commission sets course for Europe’s AI leadership with an ambitious AI Continent
Action Plan.



                                                                                                           71
                                                       Deployment of AI in healthcare – Final Report


landscape, some stakeholders indicated that interdisciplinary AI governance committees
can be established to oversee compliance and streamline decision-making. Data security
and privacy concerns may be addressed through comprehensive data governance
frameworks, robust data storage policies, encryption methods, and privacy-by-design
technologies. To clarify liability, some healthcare institutions are defining clear
frameworks, differentiating AI risk levels, and implementing risk assessment mechanisms.
Such strategies collectively promote regulatory clarity, data security, and trust in AI
adoption within healthcare.

     7.3     Organisational and business challenges and accelerators
There are a number of different organisational and business challenges affecting the
deployment of AI in healthcare that can be grouped into four categories presented in the
section below.

7.3.1 Financing mechanisms

7.3.1.1 Challenges

The deployment and maintenance of AI solutions in healthcare can be costly and is often
associated with uncertainty regarding the return on investment for healthcare providers 261.
They entail significant investment in personnel, infrastructure and technology to test,
validate, implement, and improve AI tools262. Underinvestment in the required
infrastructure within healthcare settings can be a barrier to the sustained use of AI tools
as it creates problems for interoperability with other systems or increases demand for
human resources (e.g., due to manual data entries together with digital ones) 263. The high
financial costs of effectively deploying AI solutions, when taken together with the lack of
funding and clear reimbursement mechanisms limits the potential to scale AI deployment.
AI innovations may fall outside the scope of EU Member State reimbursement frameworks
and as a result, stakeholders remarked that direct reimbursement remains sparse or
almost non-existent across mainland Europe. Stakeholders highlighted that they perceive
this is primarily a result the difficulty to demonstrate improved outcomes for patients. In
addition, there is a lack of published evidence of the value of some types of AI systems
which hinders attracting funding or introducing reimbursement frameworks for effectively
deploying AI solutions264.

The lack of funding, investment and financial incentives to deploy AI in clinical
practice was described as a significant challenge affecting the deployment of AI by 62%
of HCPs (29 out of 47), 50% of hospital representatives (13 out of 26), and 61% of AI
developers (19 out of 31) that responded to the survey. Restricted budgets, primarily in
public healthcare systems, often make it hard to justify the financial investments in AI
tools, a sentiment shared by stakeholders from Spain, Denmark, the UK, the USA,
Germany and Austria. According to an HCP from the UK, existing funding is often used
only on implementing AI, without considering the broader needs like education, policy
development, and the creation of necessary platforms to ensure effective AI integration in
the healthcare system. The stakeholder emphasised that due to the abovementioned
financial constraints, deployment of AI solutions is often limited to large University
hospitals with the financial means and access to research grants to fund the deployment


261 Bongurala et al., 2024. Transforming healthcare with Artificial Intelligence (AI): Redefining Medical
Documentation.
262 Scott et al., 2024. Achieving large-scale clinical adoption of AI-enabled decision support.
263 Wijnhoven F., 2021. Organisational learning for intelligence amplification adoption: lessons from a clinical
decision support system adoption project.
264 Strohm et al., 2020. Implementation of artificial intelligence (AI) applications in radiology: hindering and
facilitating factors.
of innovative AI solutions, putting smaller hospitals and those found in remote or rural
areas at a disadvantage. In addition, the high licencing costs of AI solutions, in some
cases, limits the deployment of AI solutions to only a small number of HCPs that are
deemed to make the most of the solution and not readily accessible to all potential users.

7.3.1.2 Accelerators

The greatest benefits from AI deployment can only be realised if AI solutions are deployed
at scale within entire healthcare systems rather than specific point-solutions in niche areas
according to hospital representatives from the USA and Belgium. Improving affordability
through funding, capital investment and financial incentives was highlighted as good
practice for AI deployment by 47% of the HCPs surveyed (24 out of 51).

In the USA, health-insurance programs already reimburse hospitals for the use of
certain AI devices, making them economic appealing as health institutions may be inclined
to adopt AI tools that promise cost savings, even if they do not necessarily improve patient
care265.

In Europe, an analysis of assessment frameworks for digital medical devices (DMDs)
reveals the existence of five distinct clusters266. As of today, Germany, Belgium and France
are the three EU countries with national statutory frameworks for DMDs that integrate
both regulatory and reimbursement pathways with Finland, Spain, the Netherlands and
Estonia, characterised as fast followers that have swiftly introduced robust assessment
frameworks. However, as of now, these frameworks either are not directly linked to
reimbursement decisions, lack a unified centralised approach, or are in the process of
consolidation.

Japan has also introduced reimbursement frameworks for certain AI tools, accessible to
approximately 50 hospitals across Japan. To be eligible for reimbursement of AI tools,
hospitals need to comply with guidelines established by related academic societies (e.g.,
Japanese Society of Radiological Medicine) and having a certain amount of full-time
equivalent HCPs working in the specific department of the healthcare facility. This
framework has encouraged hospitals to deploy and use AI tools across different medical
specialties. However, this reimbursement framework is challenging for smaller hospitals
in rural settings, which often do not fulfil the requirements for reimbursement. Hospitals
in such healthcare settings are those where the use of AI tools is expected to be the most
beneficial, as they often have a shortage of specialised HCPs and lack the necessary
expertise.

Beyond the reimbursement of AI solutions, several deployers of AI solutions reported that
establishing clear budget allocations for AI deployment and flexible financing options
offered by developers (e.g., where deployers can chose to pay a fixed flat rate or pay-per-
scan depending on the needs of the healthcare institution), has also proven to be beneficial
in addressing the financial constraints limiting AI deployment. Budgeting recruitment
and the involvement of several roles to actively engage in AI deployment during the
planning of AI implementation has been reported as a strategy that contributes to
successful implementation. Healthcare leaders should plan to recruit and involve trusted
HCPs and innovation managers that are qualified to work cross-functionally with HCPs and
other stakeholders during the deployment phase267. Financial sustainability of the AI use
and continuous maintenance and improvement of the model could be resolved through


265 Lenharo M. 2024. The testing of AI in medicine is a mess. Here’s how it should be done.
266 Tarricone et al., 2024. Towards harmonizing assessment and reimbursement of digital medical devices in
the EU through mutual learning.
267 Nair et al., 2024. A comprehensive overview of barriers and strategies for AI implementation in
healthcare: Mixed-method design



   Final Report                                                                                          73
                                                       Deployment of AI in healthcare – Final Report


fundraising or through public-private partnerships that have been proven to be a
sustainable model to ensure financing 268. For example, the AI in Health and Care Award in
the UK ran from 2020 to 2024 and was part of the NHS AI Lab, a Department of Health
and Social Care initiative included in the Government Major Projects Portfolio. It allocated
more than 100 million GBP to support the design, development and deployment of
promising AI technologies. The AI Award was structured into 4 ‘phases’ based on how
ready products were for real-world implementation and the evidence available to support
wider adoption.

Additionally, given the high cost of deployment, some hospitals in the USA monitor the
usage of AI solutions across users (e.g., in terms of number of hours per week spent on
the AI application) and reallocate the available licenses of the AI tools accordingly should
there be users not making the most of the available tools. However, it is expected that as
more AI solutions are developed and available on the market, the cost of deploying such
solutions will inevitably decrease.

7.3.2 End-user involvement

7.3.2.1 Challenges

The lack of involvement of end-users in the development, testing and deployment of
AI tools was described as a significant challenge affecting the deployment of AI tools by
55% of HCPs (26 out of 47), 50% of hospital representatives (13 out of 26), and 45% of
AI developers (14 out of 31) that responded to the survey. The lack of end-user
involvement in the deployment process of AI in healthcare creates significant challenges,
undermining the effectiveness and acceptance of these technologies. End-users, such as
clinicians, nurses, and administrative staff, are the ones interacting with AI tools in their
daily workflows. Without ensuring adequate engagement and buy-in from these
stakeholders, even the best AI tools are unlikely to be accepted and integrated into clinical
practice and will be unable to improve clinical outcomes. This sentiment was shared by a
number of hospital representatives and HCPs consulted. The lack of end-user involvement
often results in AI solutions that are not aligned with the clinical needs that need to be
addressed, systems that fail to integrate seamlessly into existing clinical workflows and
processes. This can lead to inefficiencies, increased cognitive workload, and user
frustration, ultimately diminishing the value AI is meant to bring. For example, a diagnostic
AI tool that doesn't align with clinicians’ decision-making workflows or provides outputs in
a non-intuitive format may face resistance, regardless of its technical accuracy.

Additionally, the lack of end-user involvement hinders trust and liability, both important
factors to the successful deployment of AI in healthcare. Without their involvement, end-
users feel alienated, perceiving AI as a "black box" technology imposed upon them rather
than a tool designed to enhance their capabilities. This perception exacerbates fears of job
displacement and raises ethical concerns about decision-making authority (see section
7.4.3.1). Furthermore, end-user feedback during deployment is essential for identifying
practical issues, such as errors in real-world data interpretation or gaps in the tool’s
functionality. When such insights are not captured early in the deployment process, it
leads to suboptimal systems that require costly and time-consuming adaptations, delaying
widespread adoption and negatively impacting confidence in the potential of the AI
solution.




268 Romero-Brufau et al., 2020. Implementation of artificial intelligence based clinical decision support to
reduce hospital readmissions at a regional hospital.
7.3.2.2 Accelerators

To ensure buy-in from end-users and those impacted by AI tools, it is important to
incorporate relevant stakeholders such as HCPs, potential users of AI, hospital leaders,
IT departments, and patients early in the development and deployment lifecycle of AI
tools, especially during the testing phase with the application of a user-centred designed
and testing approaches269. Early engagement of end-users to ensure relevance and
usability of AI solutions was highlighted as a good practice by 75% of the HCPs surveyed
(38 out of 51). It has been demonstrated that the buy-in from the leadership and
managers within healthcare institutions creates conditions for the buy-in from HCPs. Of
the hospital representatives that replied to the survey question, 83% (20 out of 24)
highlighted that they explored partnerships with AI vendors to access different AI solutions
to ensure usability, while 67% created opportunities for staff involvement in AI
implementation projects (16 out of 24).

Multidisciplinary collaboration to ensure integration into clinical workflow was also
highlighted as a good practice by 71% of the HCPs surveyed (36 out of 51). Establishing
multidisciplinary teams (including IT experts, data engineers, HCPs, financial analysts,
etc.) that are involved throughout the deployment process has proven to be an effective
strategy to ensure the effective deployment and use of AI solutions as evident by digitally
advanced healthcare institutions such as the Mayo Clinic and Duke Health. Such an
approach was also employed by a hospital in Israel and the USA consulted.
Multidisciplinary teams may also facilitate the deployment process by providing on-site
support to ensure seamless integration into clinical workflows, and by facilitating
explainability, interpretability and the overall understanding of AI tools, encouraging inter-
professional learning. According to AI developers, multidisciplinary collaboration and
inclusive design and testing processes that involve end-users early in the
development process fosters greater acceptance and trust by HCPs. For example, the
Cleveland Clinic established a Center for Artificial Intelligence and Data Science (CAIDS)
consisting of a dedicated AI team focusing on advancing research and applications in AI
and data science. CAIDS serves as a hub for innovation and collaboration, driving
interdisciplinary efforts to address complex challenges. Another example described by a
hospital representative from the USA is the introduction of fellowship programs within the
hospital Data Science Institute which aim to onboard a balanced cohort of 50% medical
doctors engaged in research and 50% of data and computer scientists, fostering
collaboration between these stakeholders and improving AI integration into clinical
practice.

The establishment of multidisciplinary teams is further enhanced by the introduction of
new roles within healthcare settings, such as “AI champions” and Clinical Information
Officers (CIOs). According to hospital representatives from the USA and Japan, CIOs are
often individuals with clinical backgrounds tasked with driving AI deployment, ensuring AI
tools align closely with clinical needs. On the other hand, “AI champions” are transitioning
into technology-focused roles and operate within specific departments, are involved in the
end-to-end process of deployment, have in-depth knowledge of AI and are serving as the
technology leads in any deployment processes. According to a hospital representative from
the USA, these “champions” should not only be "tech-savvy" but also deeply involved in
their respective fields, which best positions them to understand and identify specific
healthcare needs and workflows that AI tools can address. To support this approach, a
hospital in the USA has introduced a new financial strategy that compensates clinical “AI
champions” with an additional 10–70% of their salary for their role in deploying AI, all
while they continue their clinical duties. A hospital representative from Israel indicated


269 Moorman LP, 2021. Principles for real-world implementation of bedside predictive analytics monitoring.



   Final Report                                                                                              75
                                                       Deployment of AI in healthcare – Final Report


that such “AI champions” could be appointed at the specific department level to promote
collaboration with AI developers and the use of AI tools among colleagues. For example,
the Mayo Clinic appointed a ‘local AI cha pion’ to oversee bridging the gap between
developers and the end-users. The AI champion identified the need for further guidance
on how to talk to patients about the algorithm’s findings and developed recommendations
to include bullets points with important information to communicate to the patient.
Conditions for a strong buy-in are created when the request for developing an AI solution
is initiated by local HCPs. Feeling the local importance of the problem and the necessity to
solve it creates better chances that HCPs could achieve buy-in and promote the AI project
and system to their peers270. This co-design approach also ensures that AI tools
developed are interoperable with existing digital solutions ensuring seamless integration
into the clinical workflow, have a user-friendly design informed by end-users that interact
with the AI tool, and providing minimal to no disruption to the workflow, existing practice,
roles and functions.

Communication is another important factor for ensuring buy-in by the end-users during
the deployment phase of AI solutions. Effective communication increases awareness
amongst the impacted healthcare workforce about the upcoming change due to the AI
system and its potential impact on processes 271. To ensure buy-in, the communication
needs to be adjusted and address value that is meaningful to different types of
stakeholders272. It is important to tailor the amount and type of information based on
relevance when communicating about the model. For example, patient outcomes are of
most interest to HCPs, while numbers and statistics are more interesting to administrative
staff and managers. The communication should focus on a vision for change that needs to
be communicated to all relevant stakeholders in the form of periodic meetings and/or
newsletters. In addition, the formation of partnerships between hospitals and AI
developers and the promotion of informal communication between these stakeholders
during the deployment phase helps create trust in AI and helps HCPs understand the value
of outputs better273. By dedicating time prior to the deployment phase to build
communication channels and clear feedback mechanisms, allows for the strengthening of
the relationship between the relevant stakeholders and contributes to a more effective and
efficient deployment process in the longer term. Clear communication and education of
the benefits of using AI in healthcare and clear communication from HCPs on how AI is
used in the delivery of care would make patients more comfortable with AI being used in
their healthcare according to 64% and 60% of patients/patient associations surveyed
respectively. For example, a hospital in the USA has a representative on the healthcare
advisory board of an AI developer, with additional representatives from other healthcare
facilities, providing feedback on desired features of the AI solution and addressing any
challenges. This collaborative approach supports continuous improvement and ensures
alignment with healthcare needs. To ensure sustained use of AI tools amongst HCPs,
performance-based incentive schemes or gamification strategies have been introduced
within hospital settings to create a sense of competition and potential rewards for using
an AI system274.




270 Sendak et al., 2020. Real-world integration of a sepsis deep learning technology into routine clinical care:
implementation study.
271 Gonçalves et al., 2020. Implementation of an artificial intelligence algorithm for sepsis detection.
272 Sendak et al., 2020. “The human body is a black box" supporting clinical decision-making with deep
learning.
273 Sendak et al., 2020. Real-world integration of a sepsis deep learning technology into routine clinical care:
implementation study.
274 Chong et al., 2021. Development and implementation of venous thromboembolism stewardship across a
hospital network.
7.3.3 Local Added Value Assessment (real-world local added value)

7.3.3.1 Challenges

The deployment of AI in healthcare faces significant challenges due to the lack of
comprehensive assessments of its added value compared to existing clinical
solutions/currently employed approaches. A lack of assessment of the added value at
hospital level of integrating AI tools in clinical practice was described as a significant
challenge affecting the deployment of AI by 53% of HCPs (25 out of 47), 54% of hospital
representatives (14 out of 26), and 42% of AI developers (13 out of 31) that answered
the survey question. How local (hospital level) added value is assessed also varies across
regions, with some hospitals balancing different elements.

Evaluating the clinical value of AI tools is important to determine whether they truly
improve patient outcomes, diagnostic accuracy, or treatment efficacy beyond what current
methods provide at local level. For example, AI tools must enhance decision-making for
commonly encountered scenarios where current clinical judgement is suboptimal such as
early detection of sepsis275 and timely diagnosis of stroke276, resulting in improved patient
care277. Tools used in such instances do not have to be perfectly accurate, as a modestly
accurate tool substantially better than current clinical judgement will be favoured over a
highly accurate tool no better than current judgement 278. AI tools must also perform better
than current well-accepted, high-performing but simpler decision rules.

In addition, HCPs need to know if deployed AI tools will improve patient care and
outcomes to an extent they and their patients would regard as clinically relevant,
irrespective of the statistical significance of reported results. Whether an effect is clinically
important depends on the nature of the condition, the effect, and the context such as
patient population and clinical setting. Based upon findings from the literature,
prospective impact studies of clinically deployed tools are few and incomplete.
In one review, only one-third of 51 studies examined patient outcomes, with mixed results
(8 positive effects, 6 no change) 279. In a more recent review of 32 studies, only 8 (25%),
10 (31%) and 12 (38%) assessed effects on decision-making, care delivery and patient
outcomes, respectively, in all cases reporting mixed results 280.

Without robust evidence demonstrating tangible benefits, healthcare providers and
decision-makers are reluctant to invest in and integrate these technologies. This lack of
clarity can lead to scepticism, as stakeholders may view AI as a costly and unproven
innovation rather than a transformative tool for healthcare improvement. Stakeholders
emphasised that AI developers, in collaboration with HCPs, must first deeply understand
the clinical task and the datasets being targeted, their amenability to AI, current clinical
decisional performance, end-user needs and the primary goals to be achieved. The goals
should be expressed in measurable targets in improved clinical processes and
outcomes, patient and professional experience, economic and efficiency gains or greater
equity and sustainability in care delivery. The absence of such evaluations hampers the
ability to prioritise resources effectively, potentially diverting funding and effort toward
tools that offer limited practical benefits. For example, in many healthcare settings,

275 Barket et al., 2023. Recognition and management of hospital-acquired sepsis among general medical
inpatients in Queensland public hospitals.
276 Tarnutzer et al., 2017. ED misdiagnosis of cerebrovascular events in the era of modern neuroimaging: a
meta-analysis.
277 Gunda et al., 2022. Improved stroke care in a primary stroke centre using AI decision support.
278 Sanders et al., 2015. A systematic review of studies comparing diagnostic clinical prediction rules with
clinical judgment.
279 Yin et al., 2021. Role of artificial intelligence tools in real-life clinical practice: systematic review.
280 Susanto et al., 2023. Effects of machine learning-based clinical decision support systems on decision-
making, care delivery, and patient outcomes: a scoping review.



   Final Report                                                                                                  77
                                                      Deployment of AI in healthcare – Final Report


individual department heads or chief quality or medical information officers face complex
decisions about medical AI without support from expert interdisciplinary committees,
potentially selecting AI tools instead based on pragmatic considerations (e.g., models from
current vendors may be preferred over models that would require new contracts, security
and compliance reviews)281.

Beyond clinical outcomes, the operational and financial value of AI tools also requires
thorough assessment to ensure their adoption aligns with healthcare system goals. AI
solutions often promise to streamline workflows, reduce costs, or enhance resource
allocation, but these claims must be validated through real-world evidence. According to
hospital representatives consulted, without clear metrics for operational efficiency and
financial returns, healthcare organisations cannot justify the significant upfront costs of
implementation and training. Moreover, failure to assess these aspects risks introducing
tools that may inadvertently increase workloads or create inefficiencies.

The lack of standardised approaches and performance metrics to assess the clinical,
operational, and financial added value of AI solutions, when taken together with the
fragmentation of AI tools and vendors, makes selecting and effectively deploying the most
appropriate AI solutions very difficult. It is not feasible for hospitals to test and pilot every
available AI solution prior to deployment to determine which one would work in the specific
healthcare setting. This issue is further exacerbated by the lack of endorsement of specific
AI developers and tools by professional societies and associations, often leaving healthcare
providers uncertain about which AI tools to deploy and thereby slowing down the
deployment process. These issues were highlighted by several stakeholders consulted
from Israel, Italy and the USA.

7.3.3.2 Accelerators

Comprehensive evaluations that quantify AI’s added value across clinical, operational, and
financial dimensions are essential for gaining stakeholder confidence, informing policy and
reimbursement decisions, and ensuring the sustainable deployment of AI in healthcare
systems. Tools to assess and evaluate the local/hospital level added value of deploying an
AI solution in clinical practice compared to existing solutions was highlighted as a good
practice to facilitate the deployment of AI by 73% of the HCPs who answered this survey
question (37 out of 51). To develop a comprehensive value proposition, according to an
AI developer from the USA, it is important to consider the following:

    1. Define and measure the tool's impact across three criteria: clinical value
       (improvement in patient outcomes), operational efficiency (enhancements in
       workflow and time savings), and financial impact (economic benefits and cost-
       effectiveness).

    2. Conduct value proposition research by using frameworks to quantify and
       communicate the tool’s benefits, such as time savings in operational contexts or
       adherence to clinical guidelines.

    3. Provide real-world evidence and case studies demonstrating the tool’s
       effectiveness and impact, including publications and comparisons with similar
       health systems.

    4. Tailor the metrics and value propositions to the specific medical specialty and
       domain to ensure relevance and accuracy.



281 Price et al., 2023. Enabling collaborative governance of medical AI.
This approach can be facilitated by conducting pilot studies on AI tools that aim to address
a specific healthcare need within specific healthcare settings with a small number of end-
users to ensure that the AI model performs as described by the developers (see section
7.1.3.2), but also to assess the widespread impact of AI solutions in terms of measurable
outcomes and indicators on their clinical value, operational efficiency gains, and potential
financial impact and Return on Investment (ROI). Such pilot studies clearly outline the
specific needs that AI solutions will address and highlight the potential impact to both
HCPs and patients, assisting the hospital leadership in their decision-making process, a
statement supported by a hospital representative from Germany. It is important to ensure
that pilot studies are timely, and that pre-defined Key Performance Indicators (KPIs) are
reported and presented appropriately. In addition, pilot studies could be conducted
comparing the performance of multiple AI solutions from different vendors, considering
any necessary modifications to the existing infrastructure and workflows.

Of the hospital representatives surveyed, 38% (10 out of 26) have developed tools to
assess and evaluate the added value of deploying an AI solution in clinical practice
compared to existing solutions. At Michigan Medicine and Duke Health, an
assessment of added value is carried out by teams combining technical, clinical, and
operational experts282. Evaluation involves analysing model performance, generalisability
to local settings, transparency, bias, workflow integration, and total ownership cost. Often,
there is no universally best AI system; for instance, Duke Health implemented the Sepsis
Watch system differently across two hospitals due to varying workflows. Selected models
are rigorously tested on controlled local EHR data, with local performance compared to
reported outcomes to ensure clinical utility. Successful integration into clinical workflows
is followed by continuous monitoring to detect and address changes in performance due
to factors like patient population shifts or workflow modifications. This process relies on
close collaboration between technical and clinical teams to maintain model reliability and
efficacy post-deployment.

A hospital representative from Belgium highlighted that they are developing a
comprehensive model to assess the operational efficiency gains as a result of deploying AI
solutions. According to this model, value is determined by outcomes that matter to
patients divided by the cost. To assess the value of the AI solution, the hospital is focusing
on various metrics, including the time required for accurate diagnosis, improvements in
hospital capacity, reductions in staff working hours, enhanced availability of services, and
the speed of diagnosis. By using these indicators, the hospital aims to quantify how the AI
solution contributes to patient outcomes and operational efficiency, thereby providing a
comprehensive evaluation of its impact and justifying its integration into clinical practice.
On the other hand, a hospital representative from Japan highlighted that they conduct
simulations of AI deployment to assess their impact on workload and efficiency, such as
working hours and financial expenditure, allowing for informed decision-making prior to
widespread adoption.

The few economic evaluations of AI tools assessing the added financial value of deploying
AI solutions are of limited quality, mostly cost minimisation analyses of specific cost
elements within single-use cases over short time horizons 283. For HCPs to effectively
conduct economic evaluations, a key consideration is estimating, for the outcome being
predicted, the number of patients the tool flags as being positive, thereby incurring costs
of preventive or therapeutic interventions, versus the number of true positives284. This
equation and the estimated costs will vary according to what clinicians perceive as the

282 Price et al., 2023. Enabling collaborative governance of medical AI.
283 Voets et al., 2022. Systematic review of health economic evaluations focused on artificial intelligence in
healthcare: the tortoise and the cheetah.
284 Liu et al., 2019. The number needed to benefit estimating the value of predictive analytics in healthcare.



   Final Report                                                                                              79
                                                       Deployment of AI in healthcare – Final Report


most clinically appropriate sensitivity and specificity thresholds or cut-off points for the
tool which, using simulation methods, determine the net monetary benefit 285. According
to AI developers consulted, failing to evaluate the economic value of AI tools (through
methods such as ROI) will make it harder to prioritise investments in financially
constrained or low-resource environments and justify the high up-front costs of AI tools
286
   .

There are challenges in defining and quantifying the ROI, as such a metric is highly
dependent on the healthcare system (e.g. public, private, not for profit) which results
in complexities in terms of how it can be evaluated, as supported by a hospital
representative from the USA. Past implementations should be taken into
consideration when calculating ROI according to hospital representatives from the USA
and Italy. To maximize ROI from AI projects, hospitals could divide initiatives into
smaller, impactful use cases that deliver quick returns with minimal infrastructure
investment according to an AI developer from the USA. A two-phased approach is
highlighted, focusing on immediate financial gains—such as increased efficiency and
reduced labour—while also considering foundational investments in data infrastructure and
systems integration needed for sustainable deployment. To justify the operational
efficiency gains of the AI tool, an AI developer proposed demonstrating performance
gains from retrospective studies in the short term, before large-scale prospective
trials.

To address the challenge posed by the fragmented AI landscape and facilitate the
hospital/local-level added-value assessment, the NHSX pu lished “A Buyer’s Guide to
AI in Health and Care”, which sets out 10 questions that Healthcare Trusts in the NHS
need to consider to make well-informed procurement decisions287. These cover problem
identification, product assessment, implementation considerations, and procurement and
delivery. Establishing a feasibility checklist to assess whether AI solutions could be
adapted and/or integrated into internal hospital frameworks and creating a catalogue of
AI vendors with specific key performance indicators on which hospitals can
assess their local added value could be an effective strategy according to a hospital
representative from Italy. This could also be achieved through enterprise platforms
provided by local vendors (see section 7.1.3.2), within which various AI solutions can be
piloted and purchased, all integrated into the same platform for ease of integration.

7.3.4 AI strategy

7.3.4.1 Challenges

The absence of a clear AI strategy from hospital leadership poses a challenge to the
successful deployment of AI in healthcare. Lack of strategic direction to promote AI in
healthcare was described as a significant challenge affecting the deployment of AI in
healthcare by 53% of HCPs (25 out of 47), 44% of hospital representatives (11 out of 25)
and 39% of AI developers (12 out of 31) that responded to the survey question. Without
a cohesive hospital-level vision, hospitals often struggle to align AI initiatives with their
overarching clinical and operational goals which can result in fragmented efforts and AI
tools adopted in isolated departments without system-wide integration. The absence of
strategic oversight may also lead to inefficiencies in resource allocation, with hospitals
investing in AI projects that may not deliver meaningful value or that fail to address high-


285 Parsons et al., 2023. Integrating economic considerations into cut point selection may help align clinical
decision support toward value-based healthcare.
286 Brat et al., 2024. Cutting through the hype: the true economic impact and ROI of AI in radiology.
287 NHSX. 2020. A Buyer’s Guide to AI in Health and Care – 10 questions for making well-informed
procurement decisions about products that use AI.
priority challenges. For example, several hospital representatives and HCPs consulted
reported that delays in AI deployment arise due to the lack of central coordination,
redundant projects and poorly allocated resources.

A clear AI strategy is also important for fostering organisational buy-in and addressing
cultural resistance to change. When hospital leadership does not articulate the hospital
level vision for AI in improving care delivery, healthcare professionals may view these
technologies with scepticism or fear of disruption to established workflows leading to a
lack of engagement from end-users, who are critical to the successful implementation and
sustained use. In addition, an unclear strategy may result in inconsistent policies around
training, data governance, and ethical considerations, creating additional barriers to
deployment.

In addition, the absence of coordinated efforts at the national and regional level further
exacerbates these issues, as healthcare providers lack the necessary guidance and support
to navigate the complexities of AI deployment. This often results in highly variable
strategic directions, as described by AI developers from the USA. This challenge was
also raised by a recent report by the Standing Committee of European Doctors where
European doctors stressed the importance of publicly coordinated efforts to establish
knowledge environments of sufficient scale and clinical expertise within national
settings288. The lack of strategic direction is perceived by HCPs in Denmark and the UK to
be most prevalent in countries with fragmented healthcare systems.

7.3.4.2 Accelerators

Strategic planning should involve setting clear objectives, allocating resources, and
establishing a roadmap for AI deployment289,290. A clearly defined strategy for AI
deployment in clinical practice was highlighted as a good practice for AI deployment by
55% of the HCPs surveyed (28 out of 51). To effectively deploy, ensure use, and scale AI
solutions in clinical practice stakeholders emphasised that it is important to have a
co prehensive “top-down strategy” in place that includes the organisation’s goals
and resource distribution for AI implementation. Engaging stakeholders from different
departments and creating cross-functional teams can ensure a coordinated approach to AI
implementation291.
According to hospital representatives surveyed, 48% (10 out of 21) have developed a
strategy or action plan for the efficient and effective deployment of AI in healthcare. For
example, a hospital representative from the USA reported that they developed a
‘play ook’ describing the experiences of early adopters from which late adopters can
learn from. In addition, as part of the AI strategy, the same hospital encourages
department leaders to identify AI use cases which are then centrally evaluated
through a business case process to ensure alignment with the operational capabilities of
the hospital. When deploying AI tools, senior leadership (e.g., hospital managers with
both clinical and IT background) should employ their formal power to establish
follow-up procedures (e.g., weekly meetings) on the utilisation of the AI tool 292. A
recent paper based on the NHS in the UK highlighted six critical challenges that an AI in
healthcare strategy should prioritise, together with some of the actions needed to address


288 The Standing Committee of European Doctors – CPME, 2024. Deployment of artificial intelligence in
healthcare.
289 Roppelt et al., 2024. Artificial intelligence in healthcare institutions: A systematic literature review on
influencing factors
290 DNV. Adoption of AI in healthcare.
291 Mennella et al., 2024. 'Ethical and regulatory challenges of AI technologies in healthcare: A narrative
review
292 Sun TQ., 2021. Adopting artificial intelligence in public healthcare: the effect of social power and learning
algorithms.



   Final Report                                                                                                 81
                                                     Deployment of AI in healthcare – Final Report


them in order to harness the potential of AI in healthcare 293. To effectively develop an AI
strategy, the integration of AI in healthcare should be guided by the perspectives and
needs of patients, the public, and healthcare professionals. It is important to build a deep
understanding of how different stakeholders perceive AI-driven health technologies to
ensure they are both effective and widely accepted. Mechanisms for engagement should
be established to enable patients, the public, and healthcare staff to participate in
discussions on emerging issues and inform strategic decision-making. In addition,
involving these groups in the co-design of AI solutions can maximise the potential of AI in
a way that aligns with their expectations and priorities.

Healthcare leaders could focus AI development and deployment on addressing critical
challenges in the sector. While encouraging local innovation and experimentation, it is
important to identify certain high-priority areas where AI can provide the greatest impact.
Demonstrating, testing, and scaling successful AI tools requires a well-defined strategy
that includes proactive horizon scanning and opportunities for healthcare staff and
organisations to highlight areas where AI could have the most benefit. Finally, equipping
the healthcare workforce with the skills and knowledge needed to leverage AI is critical.
Comprehensive plans should focus on training both current and future professionals,
developing specialised career pathways in AI, and empowering staff to shape the evolution
of their roles in light of technological advancements.

An indicative example of an strategy is that of Northwestern University Hospital,
where in 2022 it institutionalised the Collaborative AI in Healthcare Initiative into
the Centre for Collaborative AI in Healthcare as a means to promote the use AI in
healthcare (for details see Box 3)294. The lessons learned from this initiative include:
   • Early and ongoing engagement with a wide range of stakeholders, including
       clinicians, scientists, administrators, and industry partners, enriched the centre’s
       understanding of diverse needs and perspectives. This inclusivity has been
       instrumental in designing resources and programs such as AI4H clinics and NM
       Healthcare AI Forum that are both comprehensive and targeted.
   • Treating the centre’s offerings as products meant adopting a mindset focused
       on the end-user—whether a clinician, researcher, or educator. This shift
       emphasised the importance of understanding user needs, preferences, and
       challenges, leading to the development of more accessible, intuitive, and valuable
       resources.
   • Embracing a product development approach encouraged the adoption of
       iterative cycles, where resources and programs are continuously refined based on
       user feedback and performance metrics. This process ensures that the centre’s
       offerings remain at the cutting edge of utility and effectiveness.
   • Designing with scalability in mind, the centre has focused on creating resources
       and programs that can grow and evolve (e.g., partnering with the health system,
       the schools of engineering and art and science when launching NM Healthcare AI
       Forum). This foresight has been critical for ensuring long-term sustainability,
       allowing the centre to adjust its strategies in response to changing demands and
       new opportunities.




293 Thornton, N. 2024. Priorities for an AI in healthcare strategy.
294 Luo et al., 2024. Northwestern University resource and education development initiatives to advance
collaborative artificial intelligence across the learning health system. Learning Health Systems.
           Box 3: Northwestern University strategy to promote the use AI in healthcare

   Governance and oversight framework

     •Established a governance framework that includes an Executive Steering Committee and an Advisory Board,
      while leveraging the Community Engagement Panel from Northwestern University Clinical and Translational
      Science Institute (NUCATS) for community outreach.
     •The 12 members of the Advisory Board bring expertise from core AI techniques applied to multimodal health
      data (e.g., imaging, clinical notes, multi-omics), health equity, ethics and patient engagement, various clinical
      specialties (e.g., from general internal medicine to cardiovascular and pulmonary care), basic science powered
      translational medicine, as well as education innovation and knowledge management.
     •This governance structure not only ensures strategic alignment and ethical integrity but also facilitates broad
      stakeholder engagement, drawing on a wealth of expertise to create an inclusive and collaborative ecosystem.
   Disseminating collaborative education resources
     •AI for Health (AI4H) Clinic, aimed at providing practical guidance and support to the approximately 4000
      practicing clinicians within the faculty.
     •The AI4H clinic sessions serve as a platform where clinicians interested in AI for healthcare can discuss their
      clinical challenges and ideas.
     •Clinicians, alongside AI and data scientists, bring forth clinical, research, or operational problems to explore
      AI/ML-based solutions through brainstorming, consultation, and iterative solution development. This process
      not only leads to pilot projects, prototype systems, and academic publications but also deepens the
      appreciation of the nuances of clinical data among AI professionals.
     •The clinic has empowered clinicians, especially those previously lacking resources, to develop and deploy AI
      models with the support of AI scientists and informatics trainees.
     •Clinicians are paired with AI trainees, creating a mentorship dynamic where both parties could learn from each
      other.
     •These collaborative efforts have led to the development of AI models tackling critical clinical challenges.
     •The Northwestern Medicine Healthcare AI Forum was established in 2023 to expand AI literacy and foster
      patient-centred innovation. This pioneering biweekly forum is uniquely inclusive, inviting not only faculty and
      students from Northwestern University but also healthcare professionals, patients, and the broader community
      within the Greater Chicago area.
     •The sessions are designed to break down the complexities of AI in healthcare, presenting the latest
      advancements in a manner that is accessible and engaging to everyone, including patients and their advocates.
     •Each forum features multiple succinct and modular presentations that distill complex research and
      technological innovations into intuitive, easily understandable insights. These 10–15 min segments avoid
      technical jargon, opting instead for plain English explanations that invite questions, stimulate open discussion,
      and encourage participation from all attendees.

   Democratizing access to unstructured health information
     • Developed bulk natural language processing (NLP) and data harmonization pipelines to systematically extract
      structured information from unstructured clinical notes, and stored processing results in interoperable data
      marts to power augmented intelligence in clinical practice.
     •The outputs are mapped to the Unified Medical Language System and the relations and concepts are stored in
      OMOP Common Data Model tables to ensure interoperability across the 12 hospitals in the adult health
      system, the pediatric hospital and clinics, and with external health systems.
     •To disseminate the use of this state-of-the-art language model, they developed easy-to-follow tutorial with a
      simplified version of TextGCN and introduced it into classroom teaching so that trainees can run a graph deep
      learning model on their laptop within 10 min.
     •To ensure broad use of the data and tools, tutorials and educational resources (e.g., case studies, consulting
      sessions, currently available to approved Northwestern Medicine Enterprise Data Warehouse [NMEDW] users)
      were created for the data marts produced by the bulk NLP pipelines.
     •Validation studies demonstrated a significant enhancement in model performance when incorporating
      information extracted through the NLP pipelines when compared to predictive models based on structured
      data alone.



Establishing a roadmap for AI adoption and implementation has also proven to be an
effective strategy to facilitate the deployment of AI technologies as evidenced by the first
full-scale deep learning technology deployed into routine clinical care 295. The Mayo Clinic

295 Sendak et al., 2020. Real-World Integration of a Sepsis Deep Learning Technology Into Routine Clinical
Care: Implementation Study.



   Final Report                                                                                                           83
                                             Deployment of AI in healthcare – Final Report


has also developed a roadmap for AI adoption known as the wheel of AI, which aligns with
the AI lifecycle proposed by Coalition on Health AI (CHAI) in its assurance standards guide.
The following steps are outlined to effectively develop a roadmap for AI deployment:
    1. Define problem and plan: Identify the problem, understand stakeholder needs,
        evaluate feasibility, and decide whether to build, buy, or partner.
    2. Design the AI system: Capture technical requirements, design system workflow,
        and plan deployment strategy.
    3. Engineer the AI solution: Develop and validate the AI model, prepare data, and
        plan for operational deployment.
    4. Assess: Conduct local validation, establish a risk management plan, train end
        users, and ensure compliance.
    5. Pilot: Implement a small-scale pilot, monitor real-world impact, and update risk
        management. An HCP from the USA highlighted the importance of conducting a
        limited rollout of the AI tool to evaluate its seamless integration into the clinical
        workflow.
    6. Deploy and monitor: Deploy the AI solution at scale, conduct ongoing monitoring,
        and maintain quality assurance.

Across all steps in the roadmap for AI deployment, it is important to consider several
core principles that includes:
   1. Usefulness, usability and efficacy: AI solutions should be beneficial, reliable,
       and improve user experience. They must solve specific problems and show clear
       benefits for patients and healthcare providers, such as better clinical outcomes and
       patient satisfaction. Usability means the AI should be easy to use and fit well into
       existing workflows. Efficacy ensures the AI achieves its goals and continues to
       perform well through ongoing testing and monitoring.

   2. Fairness, equity and bias management: AI solutions must be fair and work
      equally well for all demographic groups. Fairness means the AI’s performance
      should be consistent across different groups, and outcomes should not depend on
      protected attributes like race or gender. Equity involves ensuring that AI solutions
      help reduce health disparities. Bias management includes regularly checking and
      correcting any biases in the data or AI system to promote fairness and equity.

   3. Safety and reliability: AI solutions should not harm patients or healthcare
      providers. This involves thorough testing and risk assessments before
      implementation, and continuous monitoring to detect and address any safety
      issues. Clear liability and governance structures must be in place to ensure the AI
      system remains safe and reliable throughout its use.

   4. Transparency, intelligibility and liability: Stakeholders need clear and
      understandable information about AI systems and their outputs. Transparency
      involves sharing how the AI system works and its limitations. Intelligibility ensures
      stakeholders can understand the AI’s decision-making processes. Liability means
      being responsible for minimising harm and addressing any negative impacts of the
      AI system.

   5. Security and privacy: AI systems must protect data confidentiality and integrity
      with strong security measures. This includes preventing unauthorised access and
      data breaches, and ensuring personal data is handled in compliance with privacy
      regulations. Organisations should have protocols for monitoring security and
      privacy, and for addressing any incidents, to keep data safe and maintain trust.
A recent study from the UK presented the strategy and structured approach to AI
deployment through a comprehensive case study of a hospital in Southwest London,
resulting in widespread deployment and use of an AI solution 296.

  Artificial intelligence (AI) implementation within the National Health Service (NHS): the Southwest London (SWL) AI
                                               Working Group experience.

 1.  Aspiration for AI adoption and shared learning that aligns with the wider NHS long-term workforce plan for “new
     ways of working by harnessing digital innovations.”
 2. Establishment of an AI Work Group following early buy-in from senior management.
 3. Development of a robust AI strategy
           a. Collaboration: every radiology department within the 5 NHS hospitals making up the SWL Imaging
                Network were contacted, and any interested members of staff from any background were encouraged
                to join.
           b. Data driven decisions: adopting a data-centric mindset to foster better decisions for patient care from
                objective outcome measures and actionable insights
           c. Engagement with AI vendors for clinical evaluation: assess viability and efficacy of AI in a real-world
                healthcare setting allowing a pipeline of implementation to be set.
           d. Scalability for future sustainability: understanding that offerings from AI vendors are likely to grow in
                the future, with adoption of greater tools and post-deployment evaluation being a continual process
                and foresight in how to fund, maintain, and expand AI integration beyond single, narrow applications or
                single-site deployment for the widest-possible patient benefit.
 4. ‘First project’ based on a problem-led solution so that improvements in clinical care can be evaluated. The AI
     Group agreed upon the clinical problem to be tackled and started exploring various AI tools available on the
     market.
 5. Application of Kotter’s 8-step model and the BS30550 structure to guide the AI implementation plan across three
     stages: pre-implementation, implementation, and post-implementation.
 6. Development of an ‘AI implementation team’ to instigate the change ensuring a shared sense of belonging and
     ownership of the project, as well as a common understanding of the challenges and solutions. The team consisted
     of expertise from 4 key domains:
           a. Management: clinical lead, divisional directors, finance, and procurement
           b. Clinical: patient advocates, clinical stakeholders, research lead
           c. Governance: legal, compliance, and information governance
           d. Technical: IT, PACS, integration leads
 7. Development of a comprehensive score sheet for AI product selection based on existing guidelines to be used by
     all core AI team members, with different members playing a greater role in evaluating certain aspects of the AI
     product and vendor.
 8. In-depth market research for all AI vendors with suitable tools for the specific use-case. Invitation of all identified
     vendors to provide written information about their product and attend a virtual meeting with the AI team for a
     live demonstration of the product. One score sheet was used per product with a point system used to aid and
     differentiate between products.
 9. Short-listing and tool selection based on scoring across the different criteria.
 10. Retrospective analysis on local healthcare data for comparison with published evidence from the AI vendor.
 11. Collaboration between the AI vendor and the IT department to develop a local virtual server to act as the portal
     between the local PACS and the cloud-based servers of the vendor, allowing for information exchange and
     interoperability.
 12. Agreement between the AI core team and the AI vendor to conduct a probationary 6–8-month prospective
     service evaluation project to evaluate the accuracy of the tool, improvements in patient care, issues with any
     technical integration, and canvas staff opinions at regular intervals during implementation, with a view to building
     a business case based on several key performance indices that would result from this evaluation project. These
     would help build a case for future formal funding and longer-term adoption, should improvements in care be
     demonstrated.




296 Shelmerdine et al., 2024. Artificial intelligence (AI) implementation within the National Health Service
(NHS): the Southwest London AI Working Group experience.



      Final Report                                                                                                        85
                                                   Deployment of AI in healthcare – Final Report


7.3.5 High-level overview of the EU regulatory landscape

The current EU regulatory framework may both directly and indirectly in shape some of
the organisational and business challenges affecting the deployment of AI in healthcare.
The section below presents a high-level non-exhaustive summary overview of key
regulation to be considered in the view of the challenges identified and should be reflected
in line with the limitations of this study identified in section 3.5.

 The HTAR297 supports organisational decision-making at national level by providing
evidence-based clinical assessments. These assessments can guide healthcare
providers in understanding the clinical added value of AI tools, helping align AI
deployments with healthcare needs and system priorities. The HTAR specifies that some
high-risk medical devices including those incorporating software using AI (Art. 7) can be
subject to joint clinical assessment. In addition, Art. 23 provides a voluntary mechanism
for health technologies not in mandatory scope and assessment of non-clinical
assessments domains such as cost-effectiveness and organisational impact.

The AIA298 lays down harmonised rules on AI needed to “foster the development, use and
uptake of AI in the internal market that at the same time meets a high level of protection
of public interests, such as health and safety” and the protection of fundamental rights as
recognised and protected by Union law (recital 8 AIA). To achieve these objectives, there
are rules regulating the placing on the market, the putting into service and the use of
certain AI systems. Moreover, the AIA provides clarity on risk categorisation, compliance
obligations, and governance mechanisms, which can aid healthcare organisations in
developing robust AI strategies. In the context of financing challenges, the AI sandboxes
(Art. 58) under the AIA, may indirectly support innovation and reduce initial testing costs.

In the context of involvement of end-users, the AIA transparency provisions of high-risk
AI systems and provision of information to deployers (Art. 13), helps aligning system
functionality with practical use, despite that this provision does not require end-user
involvement in the design phase. As regards challenges around the local added value
assessment of AI systems in real-world clinical practice, the AIA does not mandate added-
value assessments but does require transparency and documentation of system
capabilities (Art. 13), which aids deployers in understanding system effectiveness and
potential alignment with workflows.


As regards helpful elements for aiding in formulating an AI strategy, the AIA’s provisions
on Governance (Ch. VII) can be valuable. Specifically, these elements in the AIA include:
the Commission to develop Union expertise and capabilities in the field of AI through the
AI Office; the establishment of a European Artificial Intelligence Board (the ‘Board’); the
establishment of an advisory forum to provide technical expertise and advise the Board
and the Commission, and to contribute to their tasks under this Regulation and the
establishment of a scientific panel of independent experts (the ‘scientific panel’) intended
to support the enforcement activities under the AIA.




297 Regulation (EU) 2021/2282 of the European Parliament and of the Council of 15 December 2021 on health
technology assessment and amending Directive 2011/24/EU
298 Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down
harmonised rules on artificial intelligence and amending Regulations (EC) No 300/2008, (EU) No 167/2013,
(EU) No 168/2013, (EU) 2018/858, (EU) 2018/1139 and (EU) 2019/2144 and Directives 2014/90/EU, (EU)
2016/797 and (EU) 2020/1828 (Artificial Intelligence Act)
7.3.6 Summary

The deployment of AI in healthcare faces several organisational and business challenges.
The high costs of implementation, infrastructure, and licensing, combined with unclear
reimbursement mechanisms, limit AI adoption, especially in smaller or rural hospitals.
Lack of end-user involvement in AI development and deployment leads to
misalignment with clinical needs, clinical workflows, resistance to adoption, and concerns
over trust and liability. Inadequate assess ent of AI’s added value complementary
to regulatory provisions — both clinically and operationally—creates uncertainty about
its benefits, making decision-makers hesitant to invest in AI tools. Additionally, the
absence of a clear AI strategy from hospital leadership results in fragmented
deployment efforts, inefficient resource allocation, and a lack of long-term vision,
particularly in public healthcare institutions. Without strategic coordination at institutional,
national, and regional levels, AI deployment remains inconsistent, limiting its full potential
in improving healthcare delivery.

To address organisational and business challenges in AI deployment in healthcare, several
accelerators have been identified. Financing mechanisms can be improved through
value-based reimbursement models, clear budget allocations, and flexible financing
options. Public-private partnerships and structured funding initiatives, such as the NHS AI
Lab, have also been effective in supporting AI deployment. End-user involvement is
important for successful integration, and this can be achieved through early stakeholder
engagement, multidisciplinary teams, and dedicated roles like AI champions and Clinical
Information Officers to facilitate adoption. Added-value assessments focusing on
demonstrating AI’s clinical, operational, and financial benefits using real-world evidence,
key performance indicators, and structured pilot studies have proven to be effective.
Additionally, economic evaluations, including ROI assessments, help justify AI
investments. AI strategy development is also important, requiring clear objectives,
resource allocation, and structured implementation roadmaps. Engaging stakeholders,
aligning AI initiatives with healthcare priorities, and ongoing monitoring ensure effective
and scalable AI deployment. These accelerators collectively support AI’s integration into
healthcare.

    7.4     Social and cultural challenges and accelerators
There are a number of different societal and cultural challenges affecting the deployment
of AI in healthcare that can be grouped into five categories presented in the section
below.

7.4.1 Trust

7.4.1.1 Challenges

Trust is important in the adoption and long-term use of AI solutions and is multifaceted in
its root causes. Concerns regarding a lack of trust in AI tools were raised as a significant
challenge by 28% of HCPs (13 out of 47), 50% of hospital representatives (13 out of 26)
and 59% of AI Developers (17 out of 29). In addition 51% of patients and patient
associations (36 out of 70) that responded to the survey reported concerns related to lack
of trust in the accuracy of decisions made by AI systems. These apprehensions may be
further exacerbated when AI tools are introduced without adequate communication or
education about their benefits and limitations. Building trust requires transparent
communication, patient-centred design, and rigorous performance testing of AI tools to
ensure that they are perceived as reliable, equitable, and beneficial by all stakeholders.




   Final Report                                                                              87
                                                         Deployment of AI in healthcare – Final Report


The "black box" nature of many AI systems, where decision-making processes are not
easily explainable, is one of the main contributors to the lack of trust amongst HCPs who
are accustomed to evidence-based, transparent methodologies (see section 7.1.5.1). This
was echoed by HCPs and AI developers consulted, indicating that a lack of trust in AI is
often compounded when it differs from conventional human decision-making. HCPs are
also wary of potential biases embedded in AI algorithms, which could lead to incorrect
diagnoses or disparities in treatment recommendations. If AI tools do not undergo rigorous
evaluation prior to their introduction and use in real-world settings (see section 7.1.3),
they could lead to significant patient harm, irreversible loss of confidence amongst the
medical profession, and inaccurate conclusions being made at the population level 299.

According to stakeholders consulted, amongst HCPs, there is often a generational divide
in attitudes towards AI where younger HCPs are generally more open to incorporating AI
solutions into their practice, while more senior HCPs could be more resistant to change.
This was reported by hospital representatives from Germany, Japan and the USA. In
addition, there are also concerns related the level of scrutiny that AI solutions undergo
prior to their release into the clinical environment 300.

Patients, too, are often wary of AI tools, further complicating their deployment in
healthcare settings with 51% of patients and patient associations (36 out of 70) that
responded to the survey having concerns and lack of trust in the accuracy of decisions
made by AI systems. Based on free text responses provided, this lack of trust arises from
concerns about privacy, data security, and the potential for impersonal or dehumanized
care. Patients ad patients representatives consulted question whether AI systems can fully
understand their unique medical conditions or prioritize their well-being over operational
efficiency. The lack of trust is most prevalent when AI solutions are used for tasks that are
traditionally performed by highly trained medical professionals. Building trust requires
transparent communication, patient-centred design, and rigorous validation of AI tools to
ensure that they are perceived as reliable, equitable, and beneficial by all stakeholders.

7.4.1.2 Accelerators

Development of a consistent narrative of the benefits of AI for patients, HCPs, and
organisations to improve trust was highlighted as a good practice to facilitate the
deployment of AI in clinical practice by 57% of the HCPs (29 out of 51) surveyed. In this
regard, the results of robust local level performance testing could be transparently shared
to all stakeholders including end-users to foster confidence in the technology’s reliability
(see sections 7.1.3.2 and 7.1.5.2). Clear communication channels have been identified as
a key factor in gaining trust, as reported by hospital representatives from Japan and the
UK, alongside insights from an EU level HCP association and an AI developer in the USA.
Transparent communication involves articulating the AI tool’s goals, benefits for both
patients and HCPs, and any operational changes required for its integration. Sharing
lessons learned from deployment experiences, such as successes, errors, and areas for
improvement, also provides valuable guidance for other institutions looking to adopt
similar technologies. Of the hospital representatives surveyed, 62% (13 out of 21)
promoted open and transparent communication about the utilisation of the AI tool and the
risks and benefits associated with it.




299 Ahmad et al., 2020. Barriers and pitfalls for artificial intelligence in gastroenterology: ethical and
regulatory issues.
300 He et al., 2019. The practical implementation of artificial intelligence technologies in medicine.
According to stakeholders consulted, in Swedish hospitals, the use of standardised notes
by radiologists to explain the purpose and functionality of AI tools to patients has proven
to be an effective strategy to improve trust. This approach has helped to demystify the
technology, addressing common concerns about dehumanisation and data privacy. First-
hand interaction with AI tools also plays a pivotal role in building trust; allowing healthcare
professionals to test and observe these systems in real-world conditions fosters familiarity
and confidence in their capabilities. For instance, according to a hospital representative
from Japan live demonstrations by AI developers, tailored to specific departments, are
instrumental in showcasing the tool’s capabilities and fostering trust among end-users. AI
developers can also enhance trust by prioritising transparency, offering clear explanations
of how their tools operate, and using visual markers or analogies to make complex
processes more comprehensible. Educating end-users about the limitations and risks of
AI, including the likelihood and potential impact of errors, further promotes a balanced
understanding and supports the responsible adoption of AI in healthcare.

The presence of younger healthcare professionals (HCPs) within healthcare facilities has
emerged as a key accelerator for the adoption and sustained use of AI tools. In a hospital
in Germany, for example, younger doctors have demonstrated strong advocacy for AI,
playing a pivotal role in showcasing its value to their more senior colleagues according to
a hospital representative. Their familiarity with technology and enthusiasm for innovation
make them effective ambassadors for AI, bridging the generational gap and fostering a
culture of acceptance. By involving younger HCPs in demonstrating the tangible benefits
of AI, such as improved diagnostics or streamlined workflows, hospitals can build
credibility and trust among their broader medical staff, ensuring a smoother deployment
process.

Another driver of trust reported by stakeholders is the use of real-world evidence and
testimonials from institutions that have successfully deployed AI solutions. Decision-
makers within healthcare facilities are more likely
to embrace AI tools when they see tangible proof    “By incorporating AI and related
                                                    technologies into medical education,
of their effectiveness and hear feedback from
                                                    you prepare future healthcare
peer institutions. Highlighting the number of
                                                    professionals not only to understand
facilities that have already adopted the            and effectively use AI tools in their
technology and presenting evidence of added         practice, but most importantly to
clinical or operational value provides reassurance  accept them. This approach helps
about its reliability and utility.                  overcome resistance due to
                                                                    unfamiliarity or fear of AI by
7.4.2 Digital health literacy                                       embedding technological literacy from
                                                                    the start of their careers. Likewise,
7.4.2.1 Challenges                                                  when all stakeholders understand how
Detailed knowledge regarding the potential and                      AI can improve patient outcomes,
                                                                    reduce workload, and enhance
workings of AI in the medical community remains
                                                                    decision-making, it reduces fear and
rudimentary and considerable AI education and                       resistance. If we would like to prepare
training will be needed301. Many HCPs lack the                      members of the health and care
foundational knowledge and skills needed to                         workforce for todays and tomorrow’s
effectively engage with AI tools, including                         challenges and opportunities –
understanding how these systems function, their                     investing in skills is a must by
potential applications, and their limitations. The                  updating university curricula, offering
low level of digital health literacy among                          training programmes.” – HCP
healthcare providers and the public was                             association based in Belgium.
described as a significant challenge affecting the
deployment of AI in healthcare by 43% of HCPs (20 out of 47), 58% of hospital

301 Paranjape et al., 2021. The value of artificial intelligence in laboratory medicine.



   Final Report                                                                                               89
                                                        Deployment of AI in healthcare – Final Report


representatives (15 out of 26) and 27% of AI developers (8 out of 30) that responded to
the survey question. In addition, 59% of patients and patient associations (41 out of 70)
expressed concerns about the lack of competence amongst HCPs, which is related to the
lack of digital health literacy. This gap can lead to resistance or hesitation in adopting AI,
as clinicians may feel unprepared to use the technology responsibly or may distrust its
outputs. Without a basic understanding of AI concepts, such as machine learning, data-
driven decision-making, or the interpretation of algorithmic results, healthcare
professionals are less likely to integrate these tools into their clinical workflows. This lack
of familiarity can also impede their ability to critically evaluate AI recommendations,
potentially reducing the quality of care and undermining the benefits AI is designed to
deliver. This was described as a very important issue that needs to be addressed by a
hospital representative from Israel. The hospital representative explained that using AI
without adequate training not only limits the value extracted from these technologies but
also poses potential risks to patient safety. This is further exacerbated by the lack of
structured training programs available to HCPs.

The absence of digital health literacy also affects the ability of HCPs to communicate
effectively with patients about AI-enabled care. Patients increasingly expect clear and
informed explanations of how AI tools influence their diagnoses or treatments, a sentiment
shared by 54% of the patients/patient associations (39 out of 70) that responded to the
survey. When HCPs lack confidence or understanding of the technology, they may struggle
to provide such explanations, potentially eroding patient trust. In addition, low levels of
digital literacy can hinder collaboration between HCPs and AI developers, as HCPs may be
unable to articulate their needs or provide meaningful feedback during the design and
deployment of AI tools. Today’s medical education system is lacking in AI training,
representing a significant barrier in both the medium and long-term. There are limited
individuals in medical faculties who are AI competent and capable of teaching the
relevance and importance of AI in the healthcare setting302. The barrier resulting from a
lack of education also extends beyond clinical staff, as specific technical expertise and
mathematical knowledge is required to develop and use AI tools and proficiency is
still rare within healthcare settings.

7.4.2.2 Accelerators

Addressing the issue of digital health literacy requires comprehensive educational
programs, ongoing professional development, and the inclusion of digital health literacy
as a core competency in healthcare training curricula to ensure that clinicians are well-
equipped to engage with and benefit from AI technologies. Healthcare providers will need
to develop training programmes specifically targeted at HCPs required to use AI
systems and designed to ameliorate the multiple concerns resulting from unfamiliar
technology (Box 4), a good practice highlighted by 65% of HCPs (33 out of 51) surveyed.
Such training programs can be conducted by a quality improvement team, an innovation
team, AI developer, or through combined efforts between the hospital and the AI
developer, with different stakeholders included in creating the training materials 303. The
focus of the training should be on how to understand the outputs of the AI system and
how to act in the new workflows, which will help make decisions regarding the workflow,
and better understand the needs for staff recruitment in using the AI system. According
to 50% of the hospital representatives surveyed, training programs were conducted for
the staff and management programs were tailored accordingly. For example, the Mayo
Clinic College of Medicine and Science launched a new initiative called Advanced Digital

302 Singh et al., 2020. Current challenges and barriers to real-world artificial intelligence adoption for the
healthcare system, provider, and the patient.
303 Sun TQ., 2021. Adopting artificial intelligence in public healthcare: the effect of social power and learning
algorithms.
Education to oversee and advance digital technology and AI education across the
organisation. This team aims to develop a comprehensive strategy for integrating digital
tools and AI into education at Mayo Clinic and equip HCPs with the knowledge and skills
to effectively and responsibly utilise these technologies304. Another successful approach to
improving digital health literacy amongst the healthcare workforce and the public is via
more informal communications, such as social media communication or in-person
communication. IT staff and AI experts could then leverage these communication channels
to disseminate AI-related knowledge to HCPs305. According to HCPs surveyed, digital
health literacy could also be improved by providing clear communication and education of
the benefits of using AI in healthcare (66% of respondents, 21 out of 32), by providing
clear communication form healthcare facilities/AI developers on how the AI model works
and comes to its decisions (59% of respondents, 19 out of 32), or by providing clear
communication from the healthcare facility/AI developer on how AI is used in delivery of
care (53% of respondents, 17 out of 32).

Several countries have adopted innovative practices to equip HCPs with the skills needed
to effectively use AI in clinical settings. These initiatives emphasise tailored training,
interdisciplinary collaboration, and accessible resources, reflecting a global commitment
to fostering AI literacy across healthcare roles. In the UK, efforts to integrate AI into
healthcare have focused on comprehensive education programs. A year-long AI fellowship
program trains doctors in clinical AI applications, initially targeting junior doctors before
expanding to early and mid-career professionals across various disciplines. A tiered
education model ensures that foundational AI literacy is accessible to all HCPs, while
specialised training is available for those involved in deploying AI technologies. Leaders
and executives receive targeted education to help them understand AI's strategic
implications, enabling informed decision-making at all levels. The UK has also explored
integrating AI awareness into medical school curricula and postgraduate training, ensuring
future healthcare providers are well-prepared. Resources like webinars, including those
from the British Institute of Radiology, provide accessible learning opportunities for
radiologists and other professionals. A hospital in Israel, is developing and implementing
a course on machine learning and AI in medicine, which will be available to all medical
staff within the hospital.

In the USA, collaborative programs between HCPs and AI experts foster hands-on learning.
The AI Scholars Program pairs HCPs with data scientists to work on real-world AI
development projects, combining theoretical education with practical experience.
Educational resources include playbooks, offering self-guided tutorials and lessons distilled
from the experiences of early adopters to support late adopters in navigating AI
integration. Fellowship programs through data science institutes recruit both medical and
technical professionals to advance AI-driven research and innovation. In Canada, a
hospital integrated a multifaceted education strategy which includes gate checks every
two months where HCPs participate in 30-minutes calls, with 5 minutes dedicated to data
presentation and the remaining 25 minutes focused upon informal peer discussions on AI
deployment and use. These initiatives emphasise experiential learning, equipping
healthcare teams to contribute to AI development and deployment actively.

Italy has addressed the need to educate nurses, who are frontline users of healthcare AI
but often lack access to professional development opportunities compared to physicians.
Courses specifically tailored to nurses aim to bridge this gap, ensuring a more inclusive
and well-rounded approach to AI adoption within healthcare teams. Japan has taken a

304 Mayo Clinic College of Medicine and Science, 2024. New Advanced Digital Education Team to Coordinate
Digital and AI Education for Mayo Clinic Learners
305 Sendak et al., 2020. Real-world integration of a sepsis deep learning technology into routine clinical care:
implementation study.



   Final Report                                                                                               91
                                                                 Deployment of AI in healthcare – Final Report


forward-looking approach with its "Medical Professionals 2030" training project, focusing
on providing healthcare providers with the AI literacy and tools needed to integrate AI into
their practices. This long-term initiative highlights the importance of preparing healthcare
systems for future challenges and innovations. These practices demonstrate the
importance of structured and accessible AI education, targeted to various roles within
healthcare systems. By offering hands-on learning opportunities, interdisciplinary
collaboration, and tiered training programs, countries are paving the way for HCPs to
harness the full potential of AI technologies, ensuring better patient outcomes and
operational efficiency.

In addition, future medical undergraduate and postgraduate curricula should be updated
to include a basic understanding of AI methodology and limitations and include advanced
statistical and computational skills 306. An HCP from the UK stated that there is a growing
consideration for integrating AI training into medical curricula at both the
undergraduate and postgraduate levels. This was also highlighted as a good practice
by 73% of the HCPs surveyed (37 out of 51). Such courses would include mandatory AI
awareness training alongside existing modules like information governance and data
protection. For example, at Northwestern University, a mandatory curriculum in
digital health and data science has been instituted for all medical students, equipping
future doctors with essential AI/ML competencies required for modern healthcare
practice307. In Europe, EIT Health established Digital Health Transformation
courses allowing HCPs to deepen their knowledge of key aspects and apply them in real
case examples. The course aims to equip students with a foundational knowledge of AI
and its practical applications in the healthcare sector. Understanding AI is critical for
innovating and improving patient safety measures and decision-makers involved in
procuring and implementing AI-based systems in healthcare settings.

Improvements in digital health literacy are not only needed amongst the healthcare
workforce, but also for those impacted by the use of AI, patients. A study conducted in
the USA on 2,675 responses where minoritised populations were oversampled indicated
that 52.9% of respondents chose a human doctor, with 47.1% choosing an AI clinic. Older
and black respondents were less likely to choose AI. However, for each unit increase in
education, the odds are 1.1 greater for selecting an AI provider indicating that while many
patients appear resistant to the use of AI, accuracy information, nudges and a listening
patient experience may help increase acceptance 308.

           Box 4: NHS AI Lab and HEE: Developing healthcare workers’ confidence in AI.
 Aim: inform how educational and training providers and educators of healthcare workers plan, resource, develop and deliver
 educational offerings to equip the workforce with necessary knowledge, skills and capabilities to develop healthcare workers’
 confidence in AI.
 Details:
 •    Definition of 5 archetypes where each has different knowledge and skill requirements to confidently develop, implement or use AI
      technologies, and hence specific educational needs.




306 Ahmad et al., 2020. Barriers and pitfalls for artificial intelligence in gastroenterology: ethical and
regulatory issues.
307 Luo et al., 2024. Northwestern University resource and education development initiatives to advance
collaborative artificial intelligence across the learning health system. Learning Health Systems.
308 Robertson et al., 2023. Diverse patients’ attitudes towards Artificial Intelligence (AI) in diagnosis.
                                                         Shaper: set the direction
                                                             for AI policy and
                                                          governance at national
                                                                   level.



                                                                                       Driver: champion and
                                     User: use AI
                                                                                     lead AI development and
                                 technolgoies within
                                                                                          deployment at
                                 healthcare settigns.
                                                                                        regional/local level.




                                         Embedder: implement,
                                        evaluate, and monitor AI             Creator: create AI
                                         technologies deployed            technologies for use in
                                           within healthcare                healthcare settings.
                                                settings.


 •     Educational priorities:
            o    Produce foundational AI educational content across the whole healthcare workforce, including basic AI literacy and
                 awareness of the limitations and risks of using AI technologies.
            o    Advanced AI education that is specific to the workforce archetypes, including development of skills and capabilities that
                 could be available through a centralised online learning hub.
            o    Product-specific training for users of each AI technology during its deployment.
 •     Proposed workforce transformation to support AI-related education.
                        ▪ Establish clear job roles and career pathways for digital, data and technology specialists
                        ▪ Expand the specialist, digital, data and technology (DDaT) data family professions and clinical informatics
                          workforce through targeted recruitment, increased education and training opportunities, competitive
          Supply
                          renumeration and flexible equivalence pathways for those with skills from experience outside the NHS
                        ▪ Support professionalisation and accreditation of the DDaT data family professions and clinical informatics
                          workforce through recognised and trustworthy national bodies

                        ▪ Maximise the potential of the workforce through recognised and accredited digital career and education
                          pathways
                        ▪ Support ongoing CPD (Continuing Professional Development) frameworks for development and validation
                          of digital professionals
       Upskilling
                        ▪ Provide protected education time for digital skill development supported by flexible hybrid training
                          pathways for digital specialist clinicians
                        ▪ Provide equitable access to training and support, including special efforts to engage and support the
                          digitally unengaged or unconvinced

       New roles        ▪ Identify gaps that may be filled by development or implementation of new roles

                        ▪ Establish and support AI multi-disciplinary teams (MDTs) involving clinical and technical roles to lead the
                          evaluation, deployment and product-specific user training for AI technologies. A diverse team and a flat
     New ways of          organisational structure should be encouraged to avoid hierarchy and minimise bias
        working
                        ▪ Through innovative placements and recruitment, promote an integrated workforce that creates new
                          relationships and networks and a working environment that embraces intrapreneurship and collaboration

                        ▪ Develop a new cadre of digital leadership roles with recognition of the value of specialist skills at a senior
                          level for individuals with DDaT data family and clinical informatics skills
      Leadership
                        ▪ Set out clear training pathways and career trajectories to achieve a specific set of competencies required
                          for digital leadership.
 •     Existing initiatives that address aspects of the workforce development cycle include the Health Education England Data Science
       Program, the Informatics Skills Development Networks, the ‘Data Saves Lives’ strategy, the NHSE Digital Workforce Program, the
       National Competency Framework for Data Professionals in Health and Care.



7.4.3 Job security and overreliance on AI

7.4.3.1 Challenges

Some HCPs may have concerns about job displacement or radically changed job plans as
a result of AI adoption, a sentiment shared by hospital representatives and HCPs from
Japan and the USA. The level of concern regarding AI use varies between HCPs, which



     Final Report                                                                                                                          93
                                                    Deployment of AI in healthcare – Final Report


may be derived from concerns regarding job security in clinical specialties where
investigations and results can be readily digitised and interpreted by autonomous AI
systems (e.g., ophthalmology, cardiology, pathology, and radiology) 309. For example,
those in the emergency department may be more eager to use the AI tool for decision-
making (e.g., discharging patients based on AI evaluations before a radiologist reviews
the study), whereas other groups such as radiologists may be more cautious. This is
brought upon by concerns that AI tools will ultimately become decision-makers in the
clinical care pathway rather than assistive tools. However, “whether AI systems will
eventually replace radiologists is the wrong question, the more apt question to be asked
is will radiologists who use AI replace radiologists who don’t” 310. However, it should be
noted that only 10% of HCPs (5 out of 47) and 12% of hospital representatives (3 out of
26) indicated concerns surrounding job security as a significant challenge to deployment
of AI in clinical practice.

Additionally, as deployment and adoption of AI solutions in healthcare becomes more
widespread, there are concerns that overreliance on such technologies can lead to
decreased critical thinking amongst HCPs311. Of the patients and patient associations that
responded to the survey, 59% (41 out of 70) expressed concerns about over-reliance on
technology and the lack of human oversight. Overreliance on AI could lead to
automation bias and overshadow human expertise, particularly among younger
clinicians, who may become too reliant or trusting of AI tools. Such concerns were raised
by HCPs, hospital representatives and AI developers from Israel, France, the UK, Austria
and Germany. As clinicians increasingly depend on AI for diagnostics and treatment
recommendations, there is a tangible risk that their clinical skills may deteriorate. This
dependency could impair HCPs’ abilities to make independent, critical decisions, especially
in situations where AI systems are unavailable, malfunction or yield erroneous
results312. Moreover, the dynamic nature of healthcare employment, where
professionals often transition between diverse clinical settings, exacerbates this
risk313. This variability across workplaces underscores the urgency of sustaining and
enhancing clinical skills in tandem with AI utilisation.

7.4.3.2 Accelerators

To address such issues, it is important to establish clear communication when AI
solutions are used as supportive tools with the output evaluated by trained
professionals, maintaining an element of human oversight. HCPs have the clinical
knowledge needed to make sure AI tools are well designed for the task required and then
tested using large amounts of clinical data that needs to be tagged manually. Once AI
systems are integrated into routine healthcare, they will need human oversight
introducing a new role for HCPs to provide the ongoing oversight of such systems. In
addition, there will also be new roles at executive level to manage the implementation
of AI in hospitals and healthcare systems. Such new positions are already becoming more
common with the introduction of roles such as the Chief AI officer. Such roles are
pioneered by hospitals in the USA, where many individual hospitals or healthcare networks
are developing their own AI systems. Although the number of such positions is still
relatively small, HCPs have already been appointed to them, such as the Mayo Clinic in
Arizona and University of California San Diego Health. Finally, it is important to
consider that unlike many other professions, the human and personal aspects of medicine


309 Brady et al., 2020. Artificial intelligence in radiology-ethical considerations.
310 Laglotz, 2019. Will artificial intelligence replace radiologists?
311 Cabitza et al., 2017. Unintended consequences of machine learning in medicine.
312 Choudhury et al., 2024. Large Language Models and User Trust: Consequence of Self-Referential Learning
Loop and the Deskilling of Health Care Professionals.
313 Sparrow et al., 2019. The promise and perils of AI in medicine.
is important and cannot be replaced with AI. For the abovementioned reasons, AI in the
future could reduce mental tasks, improve treatments, and free up clinician time for
human interactions rather than replace them314. Overall, concerns surrounding job security
and overreliance on AI can be addressed by improving the digital health literacy of the
healthcare workforce and the public (see section 7.4.2.2).

7.4.4 Doctor-patient relationship

The patient-doctor relationship is an important aspect of healthcare, characterised by
mutual trust, effective communication, and collaboration. A trustworthy doctor-patient
relationship is foundational for successful medical care - involving open communication,
empathy, and a shared understanding of the patient's concerns, values, and treatment
preferences315. Patients place trust in the expertise of their healthcare providers, relying
on their guidance for accurate diagnoses and effective treatments. At the same time,
healthcare providers trust in the information shared by patients to make informed
decisions about their care.

Widespread integration of AI in healthcare could intensify feelings of alienation between
patients and healthcare workers. As AI assumes greater responsibilities, the essential
human touch in patient care might become less prevalent, potentially diminishing
patient satisfaction and trust316. Of the patients and patient associations that responded
to the survey, 56% (39 out of 70) expressed concerns about the loss of the doctor-patient
relationship with the use of AI. In addition, patients arriving with AI-informed information,
be it accurate or misleading, could complicate collaborative decision-making with the
doctor. This could result in adherence to AI-driven advice without considering individual
medical history or difficulties for physicians attempting to reconcile their expertise with AI
suggestions. This not only risks eroding the HCP’s role but also could reshape the doctor-
patient relationship into a consumer-provider model317. To effectively ensure that AI has
a positive impact on the doctor-patient relationship, it is important to promote realistic
and aligned expectations regarding AI via education for HCPs and patients before
implementing AI tools (see section 7.4.2.2).

7.4.5 High-level overview of the EU regulatory landscape

The current EU regulatory framework may both directly and indirectly in shape some of
the social and cultural challenges affecting the deployment of AI in healthcare. The section
below presents a high-level non-exhaustive summary overview of key regulation to be
considered in the view of the challenges identified and should be reflected in line with the
limitations of this study identified in section 3.5.

As regards trust, the AIA318, as explained throughout this study, is central to fostering
trust. The requirements on high-risk AI systems enhance trust of AI systems in healthcare.
For example, the requirements for human oversight (Art. 14) ensure that clinicians remain
integral to decision-making processes, mitigating concerns about the absence of a human
touch in patient care. Additionally, the requirements on transparency and provision of
information to deployers (Art. 13 AIA), aid to ensure healthcare professionals remain
central to AI-assisted care.



314 Dobbs, T. 2024. Will artificial intelligence lead to new jobs in healthcare?
315 Mennella, C. et al., 2024. Ethical and regulatory challenges of AI technologies in healthcare: A narrative
review.
316 Sauerbrei et al., 2023. The impact of artificial intelligence on the person-centred, doctor-patient
relationship: some problems and solutions.
317 Allen et al., 2024. Navigating the doctor-patient-AI relationship - a mixed-methods study of physician
attitudes toward artificial intelligence in primary care.
318



   Final Report                                                                                                  95
                                                     Deployment of AI in healthcare – Final Report


Ethical considerations, such as preventing discrimination and bias, are critical to
ensuring trust and equitable outcomes during the deployment of AI systems in healthcare.
In this regard, the provision in Article 10 AIA on data and data governance requires that
high-risk AI systems to be developed on the basis of training, validation and testing data
sets that meet quality criteria set therein. Such provisions aim to ensure that deployed
systems make decisions that are unbiased and equitable, regardless of patient
demographics or socio-economic factors, and effectively address the needs of diverse
populations. The EHDS319 facilitates equitable access to health datasets (Chapter IV EHDS
– Secondary use). Such access can ensure that deployed AI tools are trained and validated
on comprehensive data, reducing the risk of bias in their outputs.

The AIA also acknowledges that AI, can also be misused and provide novel and powerful
tools for manipulative, exploitative and social control practices. Such practices are
particularly harmful and abusive, and the AIA prohibits them because they contradict
Union values of respect for human dignity, freedom, equality, democracy and the rule of
law and fundamental rights enshrined in the Charter, including the right to non-
discrimination, to data protection and to privacy and the rights of the child320. The
European Commission has recently issued guidelines detailing AI practices prohibited
under the AI Act, aiming to safeguard European values and fundamental rights 321.

The PLD322 may indirectly reinforce trust by ensuring liability, holding providers liable for
defective AI products. The PLD, particularly in its revised form, addresses trust by ensuring
that patients and healthcare providers have clear recourse in the event of harm caused by
defective AI systems. Its strict liability provisions create accountability for manufacturers,
reinforcing confidence in the safety and reliability of AI technologies. The HTAR323 may
indirectly enhance trust by contributing to assessing the clinical value of some high-risk
medical devices including those using AI based software (Art. 7), allowing healthcare
institutions to validate AI tools based on clinical evidence, which can be shared with HCPs
and patients to increase confidence.

As regards digital and health literacy, the AIA also tackles digital literacy challenges by
requiring providers (such as developers) and deployers of AI systems to take measures to
ensure a sufficient level of AI literacy of their staff and other persons dealing with the
operation and use of AI systems on their behalf, taking into account their technical
knowledge, experience, education and training and the context the AI systems are to be
used in, and considering the persons or groups of persons on whom the AI systems are to
be used (Article 4). This provision helps bridge knowledge gaps and empowers healthcare
providers to effectively integrate AI into their workflows.

The EHDS, may also play a role in improving digital literacy by facilitating access to
structured data, which can support educational efforts to enhance the digital health literacy
of healthcare providers and stakeholders. This may improve understanding and
acceptance of AI solutions, fostering trust and collaboration in their deployment.
Additionally, the EHDS specifies that the Commission shall support the sharing of best
practices and expertise to build capacity within Member States to strengthen digital health


319 Regulation (EU) 2025/327 of the European Parliament and of the Council of 11 February 2025 on the
European Health Data Space and amending Directive 2011/24/EU and Regulation (EU) 2024/2847
320 See recital 28 and chapter II AIA
321 Commission Guidelines on prohibited artificial intelligence practices established by Regulation (EU)
2024/1689 (AI Act), 04 February 2025
322 Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for
defective products and repealing Council Directive 85/374/EEC
323 Regulation (EU) 2021/2282 of the European Parliament and of the Council of 15 December 2021 on health
technology assessment and amending Directive 2011/24/EU
systems for primary use and secondary use considering the specific circumstances of the
different categories of stakeholders involved. To support that capacity building, the
Commission shall in close cooperation and consultation with Member States establish
indicators for self-assessment for primary use and secondary use (Article 82 EHDS); Art.
83 EHDS requires accessible training for health professionals, and Art. 84 EHDS calls for
campaigns to improve patients’ digital literacy regarding their rights and benefits.

As regards doctor-patient relationship, the AIA supports the doctor-patient relationship by
promoting human oversight (Art. 14) and transparency (Art. 13), ensuring healthcare
professionals remain central to AI-assisted care.

7.4.6 Summary

The deployment of AI in healthcare faces several social and cultural challenges. Trust
issues among HCPs and patients hinder adoption, with concerns about AI transparency,
potential biases, and the "black box" nature of decision-making. Resistance is more
common among senior clinicians, while patients fear AI may lead to impersonal care. Low
digital health literacy among HCPs and patients further complicates adoption, as many
lack the necessary training to understand, interpret, and effectively use AI tools. This
knowledge gap also affects communication, reducing patient confidence in AI-assisted
care. Job security concerns are prevalent, particularly in specialties like radiology and
pathology, where AI could automate tasks, while overreliance on AI raises fears of
diminished critical thinking and clinical skills among HCPs. Lastly, the doctor-patient
relationship may be strained by AI deployment, with patients fearing reduced human
interaction and HCPs struggling to reconcile AI-driven recommendations with traditional
expertise.

To address social and cultural challenges in AI deployment, several accelerators have been
identified. Building trust requires transparent communication about AI’s functionality,
performance testing processes, and real-world benefits. Hospitals have successfully
improved trust by involving younger HCPs as AI advocates, using standardised
explanations for patients, and showcasing AI’s effectiveness through real-world evidence.
Enhancing digital health literacy is important for both HCPs and patients, achieved
through structured AI training programs, interdisciplinary collaborations, and curriculum
updates in medical education. Countries like the UK, USA, and Japan have implemented
tailored AI literacy initiatives, ensuring HCPs are equipped to engage with AI effectively.
Addressing job security concerns involves clearly defining AI as a supportive tool
rather than a replacement for HCPs, with new roles such as Chief AI Officers emerging to
oversee AI integration. Lastly, preserving the doctor-patient relationship requires
balancing AI’s efficiencies with human-centred care, ensuring AI supports rather than
replaces clinician-patient interactions. These accelerators collectively promote AI
acceptance, responsible usage, and integration into healthcare workflows.

     7.5     Challenges faced by generative AI systems
The deployment of generative AI in healthcare introduces some unique challenges in
addition to all of the abovementioned challenges relevant to both traditional and
generative AI systems. A recent systematic review highlighted the limitations of LLMs that
can broadly be categorised into design limitations and output related limitations that affect
the deployment of such tools324. Trust and performance testing are essential to generative
AI’s adoption success in healthcare. The ‘unpredictability’ of generative AI tools is the main
barrier to adoption success, as we do not know when it is going to return a good answer


324 Busch et al., 2025. Current applications and challenges in large language models for patient care: a
systematic review.



   Final Report                                                                                            97
                                                      Deployment of AI in healthcare – Final Report



and when its answers are going to be wrong or misleading, or in other words, when to
trust generative AI and when not to trust it, especially when the user is not sufficiently
qualified to assess the quality (accuracy and completeness) of a given response. This is
particularly relevant given that some generative AI tools are known to make stuff up,
termed generative AI “hallucinations”. The issue of “hallucinations” was highlighted by
HCPs and hospital representatives consulted, given that such generative AI models lack
the long-standing reliability mechanisms found in more traditional machine learning
models. To address this issue, it is important to have generative AI models that have been
specifically and comprehensively trained using a large amount of quality evidence-based
medical texts that sufficiently cover a given medical specialty.

The rapid evolution of generative AI models, such as LLMs, introduces an additional
challenge regarding their clinical evaluation, regulation, and certification. Generative AI
continuously evolves, adapting its outputs based on new data inputs. This dynamic nature
necessitates ongoing performance testing to confirm that the AI remains accurate and
reliable over time325,326. However, clinical evaluation and certification are processes that
traditionally take a relatively long time to complete, so there is always the risk that by the
time an evaluation is completed, the evaluated AI has already changed substantially with
the release of a new version requiring a new evaluation. Generative AI models bring new
challenges compared with already regulated AI-based technologies and will therefore
require additional regulatory adaptations 327.

Generative AI models often contain billions of parameters that require significant
computational power to generate accurate responses. As a result, resource-limited labs or
healthcare providers may be compelled to rely on external, third-party digital tools for
computational support. However, there are ethical, regulatory, and patient privacy
concerns with using third-party generative AI tools. Before sensitive data are uploaded
into these tools, potential users must conduct a thorough legal and data privacy review,
which itself is resource intensive. Concerns surrounding data privacy and protection were
raised by HCPs and hospital representatives consulted, with HCPs stating that generative
AI models may struggle with privacy concerns, particularly in cases where models are
trained on limited or sensitive data. One approach to address this issue is by using localised
architecture with fewer parameters that can run on local networks or mobile devices, are
optimised for specific tasks, and can be trained in less time than larger models, using a
combination of model compression and higher-quality training data. Using generative AI
models locally lessens privacy risks, as the data never leave the secure local network or
device328. Using federated learning, where multiple actors collaboratively train a model by
exchanging model updates without sharing patient data, is another approach that can be
used to maintain data privacy and keep patient data local but enable HCPs to benefit from
models trained on more patient records.

Overall, most stakeholders consulted as part of this study where not aware of specific
accelerators to facilitate the deployment of generative AI tools in clinical practice. Those
who were aware focused on avoiding the inclusion of personal identifiable
information in software outside the EHR system and on training and fine-tuning
generative AI models with specific medical contexts to improve their relevance in
clinical settings.



325 Hwang and Park, 2020. "Clinical Implementation of Deep Learning in Thoracic Radiology."
326 Reddy, S., 2024. Generative AI in healthcare: an implementation science informed translational path on
application, integration and governance. 15 March
327 Mesko et al., 2023. The imperative for regulatory oversight of large language models (or generative AI) in
healthcare.
328 Zou et al., 2023. Universal and transferable adversarial attacks on aligned language models.
                                                         Deployment of AI in healthcare – Final Report



8        Future Considerations
      8.1      Considerations to facilitate the deployment of AI in healthcare
The successful deployment of AI in healthcare requires a multifaceted strategy that
addresses the various challenges described in the previous sections while leveraging
identified accelerators. A recent publication indicated the need for a comprehensive
approach that includes consolidating funding, creating a level playing field, clarifying
regulations, supporting centres of excellence, promoting trustworthy AI, fostering
coordinated efforts, and implementing monitoring and assessment mechanisms to ensure
safe and effective deployment of AI into clinical practice 329. The stakeholders consulted
during this study identified specific considerations for future actions, both regulatory and
non-regulatory, that could be implemented at the EU level to support the deployment of
AI tools in healthcare (Figure 16).

    Figure 16: Considerations for future actions to facilitate the deployment of AI in healthcare
         according to hospital representatives (34 responses) and HCPs (51 responses).

         Establishment of common standards on data
        governance, privacy, and interoperability across              79%                   73%
                 European healthcare systems

     Provide clarity on regulatory processes for product
            approval, accountability, and liability
                                                                     65%              69%


       Consolidated funding to support specific strategic
                          priorities
                                                                    56%           65%

        Redesigning workforce planning and clinical
       education to address future healthcare and AI            50%             61%
     professional needs, investing in upskilling frontline…

         Organisation and centralised collection of post-
          deployment data to monitor on the ongoing             44%             63%
                    effectiveness of AI tools

    Development of platforms to facilitate dialogues and
    exchange of good practices to facilitate deployment         50%             59%
                        of AI tools

            Ensure consistent access to public data and
                 promoting open-data initiatives
                                                                    53%         49%

 Encourage the establishment of centres of excellence
    for AI in healthcare to concentrate talent and                  56%         39%
                       resources

 Establish an EU AI in healthcare center to coordinate
             and facilitate AI deployment
                                                              21%         49%



                                                   Hospital     HCP


                                        Source: Authors’ elaboration

The sections below present considerations identified by the activities conducted that could
be considered to facilitate the effective and efficient deployment of AI in healthcare by
addressing the abovementioned challenges (Figure 17 describes the challenges addressed



329 EIT Health, 2020. Transforming healthcare with AI: The impact on the workforce and organisations.
by each of the considerations for future action). They are presented without any specific
order or prioritisation.

       Figure 17: Challenges addressed by the proposed considerations for future action.
        Establishing common standards for data governance and
        interoperability
        •Data standardisation and interoperability


        Establishing centres of excellence for AI in healthcare
        •Complex regulatory lanscape
        •AI strategy
        •Trust
        •Digital health literacy
        •Job security and overreliance on AI
        •Doctor-patient relationship

        Consolidated funding and introduction of financing
        mechanisms
        •IT infrastructure
        •Financing mechanisms

        Local performance testing, local added value assessment and post-
        deployment monitoring of AI solutions
        •Validation protocols
        •Post-deployment monitoring and maintenance
        •Transparency and explainability
        •Added-value assessment


        Development of a catalogue of AI solutions in healthcare

        •Added-value assessment
        •AI strategy


                                      Source: Authors’ elaboration.


8.1.1 Establishing common standards for data governance and interoperability

The first action focuses upon the establishment of common standards for data
governance and interoperability across European healthcare systems (see section
7.1.1)330. Such an action was identified by 73% of HCPs (37 out of 51) and 79% of hospital
representatives (27 out of 34) surveyed. Common standards have the potential to support
the integration of AI across different healthcare systems within the EU. Establishing these
standards could address hurdles related to data governance and the interoperability of
systems, facilitating more effective data exchange that is required to effectively use
and scale AI solutions. By establishing rules for data access, and cross-border exchanges,
the EHDS aligns closely with the need for common standards that facilitate AI deployment
(see section 5.1.7). While the EHDS lays an important foundation, its eventual success
depends on complementary actions to fully realise the potential of AI in healthcare. The
EHDS     enables AI innovation through access to richer and more diverse datasets. In
addition, the EHDS framework could aid in testing and validating AI models across
healthcare systems, facilitating compliance with EU regulations while ensuring that AI




330 The CEN-CENELEC Joint Technical Committee 21. responsible for the development and adoption of
standards for AI and related data, as well as provide guidance to other Technical Committees concerned with
AI, could be leveraged to provide such standards for the field of healthcare.
                                             Deployment of AI in healthcare – Final Report



applications perform reliably across different demographic and clinical settings (see section
8.1.4).

Adherence to international interoperability standards reinforced, such as those described
in section 7.1.1.2, to ensure uniform data exchanges and establish a certification program
for AI developers and healthcare systems to validate compliance with these standards. A
certification program could be used to assess the technical readiness and compliance with
the standards. In addition, an open-source projects could be promoted that develop tools
for data standardisation, integration, and exchange tailored to healthcare environments,
an action highlighted by 53% of hospital representatives (18 out of 26) and 49% of HCPs
(25 out of 51) surveyed. Such tools could include interoperable APIs and middleware that
integrate with existing healthcare systems (see section 7.1.1.2). Financial incentives could
accelerate the transition to a standardised data environment and interoperable systems
that would facilitate the deployment of AI tools in healthcare.

8.1.2 Establishing centres of excellence for AI in healthcare

The study suggests that the establishment of Centres of Excellence for AI in healthcare,
which could serve as hubs for concentrating talent and resources to develop playbooks for
AI deployment, advance digital health literacy, foster collaboration between developers
and deployers, digitally advanced with less advanced countries, and disseminate best
practices across Member States. The establishment of such centres and community of
experts was proposed by 56% of hospital representatives (19 out of 34) and 39% of HCPs
(20 out of 51) surveyed.

These Centres of Excellence could:

   1. Provide advanced training programs for the healthcare workforce: a
      function of these Centres of Excellence could be to develop and deliver training
      programs tailored for HCPs, focusing on AI fundamentals, practical applications,
      ethics, and data governance, an action highlighted as important by 50% of hospital
      representatives (17 out of 34) and 61% of HCPs surveyed (31 out of 51) in the
      context of workforce redesign. Such programs could be designed for clinicians,
      healthcare administrators, and IT staff, covering topics from understanding AI-
      generated insights to safely integrating AI tools into clinical workflows.. To
      accommodate various needs across the workforce, these centres could offer
      programs at different levels—from introductory courses for non-technical staff to
      in-depth training for healthcare practitioners and data scientists working directly
      with AI technologies (see section 7.4.2.2). Certification programs and continuing
      education credits could be awarded to encourage participation, with the centres
      partnering with universities, research institutions, and AI companies to provide
      current, high-quality training resources. These programs could ensure that
      healthcare providers across the EU are equipped to use and understand AI tools
      confidently, maximising their effectiveness in clinical settings. One example of such
      an initiative is the TRANSiTION (Digital Transition And Digital Resilience In
      Oncology) study already implemented at EU level that aims to develop training on
      digital skills for the health workforce.

   2. Provide public education and digital health literacy initiatives: to build a
      well-informed public that can engage with AI-driven healthcare, the Centres of
      Excellence could also deliver digital health literacy programs for the general public.
      These initiatives would aim to demystify AI in healthcare, helping individuals
      understand how these technologies are used in diagnostics, treatment, and
      preventative care. Educational campaigns could focus on common uses of AI,
      patient data privacy, and ways to interpret AI-driven insights responsibly. These
         programs could empower citizens to make informed choices and engage actively
         with their healthcare, fostering a sense of trust and transparency. The centres could
         achieve this through accessible online courses, interactive workshops, and public
         seminars, tailored to different age groups and levels of digital literacy. Partnerships
         with public health agencies, patient advocacy groups, and educational institutions
         could further amplify outreach, ensuring wide engagement across diverse
         demographics.

    3. Create a collaborative environment for knowledge and best practice
       sharing: the Centres of Excellence could serve as collaborative hubs where
       researchers, clinicians, AI developers, and policymakers come together to share
       knowledge and best practices. Such collaborations and exchange of best practices
       was highlighted as an important action by 50% of hospital representatives (17 out
       of 34) and 59% of HCPs (30 out of 51) surveyed. They could facilitate cross-border
       collaboration and provide a structured environment for piloting AI technologies,
       running clinical trials, and developing guidelines. Regular workshops, conferences,
       and hackathons could foster innovation, while shared repositories of case studies,
       model documentation, and regulatory resources could support consistent standards
       across the EU. By centralising best practices and success stories, these centres may
       help standardise safe, ethical AI deployment in healthcare. Moreover, such
       collaboration could accelerate regulatory alignment, enabling Member States to
       learn from each other’s experiences and address common challenges more
       effectively.

The collaborative environment in these Centres of Excellence could facilitate the
development of AI playbooks, such as those developed in the UK (BS 30440:2023 331) and
the USA (the Coalition for Health AI assurance standards guide 332), that could guide the
effective deployment of AI solutions in healthcare, outlining a clear and structured
roadmap for deployment at various levels of the healthcare system. These playbooks could
also provide clear regulatory guidelines for AI deployment, highlighted as an important
action by 65% of hospital representatives (22 out of 34) and 69% of HCPs (35 out of 51)
surveyed. They could build on the provisions of the EU AIA and bridge the gap between
the requirements of the AIA and the practical implementation of AI solutions in
healthcare.

8.1.3 Consolidated funding and introduction of financing mechanisms

Consolidated funding or financing mechanisms could support specific strategic
priorities. This was highlighted by 56% of hospital representatives (19 out of 34) and 65%
of HCPs (33 out of 51) surveyed. This approach may accelerate both the development and
deployment of promising AI applications and overcome some of the obstacles to
deployment by setting the overall strategy. This could also support Member States, and
in turn healthcare organisations align their own strategic objectives related to AI
deployment in healthcare (see section 7.3.4).

Dedicated funding streams, grants, and subsidies could support healthcare
institutions to pilot and deploy AI solutions across different strategic areas. Given the
significant administrative tasks often associated with securing funding, deployers
(particularly smaller hospital in remote areas) could be supported by connecting them with
expert consultants who understand what is needed to secure, for example, EU funding.




331 BSI Knowledge, 2023. Validation framework for the use of artificial intelligence (AI) within healthcare.
332 Coalition for Health AI, 2024. CHAI Assurance Standards Guide.
                                             Deployment of AI in healthcare – Final Report



Guidelines for reimbursement of AI tools in healthcare (through case studies and practice
sharing). The framework could establish example reimbursement criteria for AI tools,
focusing on clinical efficacy, safety, and patient outcomes. By providing clear guidelines,
developers could be encouraged to focus on meeting these standards, thereby fostering
the creation of high-quality, clinically assessed AI applications.

8.1.4 Local performance testing; local real-world added-value assessment and
      post-deployment monitoring

AI deployment could be facilitated by introducing local added-value assessments (see
section 7.3.3), local performance       tests (see section 7.1.3), and post-deployment
monitoring of AI tools (see section 7.1.4), as highlighted by 24% of hospital
representatives (8 out of 34) and 49% of HCPs (25 out of 51) surveyed. Assurance
laboratories could be established to evaluate the local performance (does the
solution perform as in my local setting) and local added value of AI tools already on the
market for healthcare (see section 7.1.3.2). The assurance laboratories could be
strategically located in leading university hospitals across EU Member States with access
to high-quality real-world evidence, that could collaborate with each other and serve as
“AI sandboxes”. This network could build on the existing work of the Testing and
Experimentation Facility for Health AI and Robotics (TEF-Health), a project supported by
the European Commission and national funding agencies, where 51 academic and private
partners from 9 European countries have come together to facilitate medical devices that
incorporate AI to fulfil their regulatory obligations. This allows AI developers and
healthcare providers to locally test the performance of models in a secure environment
using anonymised, ethically sourced data from across the EU to ensure there are no
variations in performance across healthcare settings. Additionally, the performance of AI
systems in real world settings could be assessed on factors such as clinical workflows, local
infrastructures, clinical guidelines and explainability of AI systems. Such a setup could
ensure diverse and representative pre-deployment performance testing, capturing
nuances across different patient demographics and healthcare contexts, and ensuring that
AI tools perform accurately and safely across different healthcare settings before being
integrated into clinical workflows.

A standardised model could be developed to evaluate the real-world local added
value of AI solutions at hospital or regional level by focusing on three core
dimensions: clinical value, operational efficiency, and financial impact. This model would
provide a robust framework to present the impact of AI tools across several dimensions
(performance benchmarks) such as clinical (e.g. reductions in adverse events), operational
(e.g. time saving) and financial domains (e.g. ROI). Once local performance testing has
completed, AI tools could be issued a "Model Report Card" or "Model Fact Label"
summarising the tool’s strengths, limitations, and validated use cases, offering HCPs,
patients, and regulators a transparent overview of the model’s performance and intended
applications. This transparency may help healthcare providers make informed decisions
about deploying AI tools, while also fostering trust among patients by clearly
communicating the AI’s capabilities and boundaries. Each assurance laboratory could then
contribute insights and AI performance data to the centralised catalogue for AI tools
proposed in section 8.1.5.

Assurance laboratories could also play an important role in conducting post-
deployment monitoring of AI tools, ensuring their sustained performance and
safety after deployment into clinical practice. The organisation and centralised
collection of post-deployment data to monitor on the ongoing effectiveness of AI tools was
highlighted as important by 63% (32 out of 51) of HCPs and 44% (15 out of 34) of hospital
representatives surveyed. Assurance laboratories could establish a systematic framework
to periodically assess AI tools in real-world settings. This ongoing monitoring could verify
that the AI models continue to meet predefined performance benchmarks, adapt to
evolving healthcare needs and maintain consistency across diverse clinical environments.
Such evaluations may focus on aspects like model drift (where AI performance may
degrade over time due to changes in underlying data distributions) and the robustness of
AI outputs when faced with new, unanticipated scenarios. The results of these periodic
assessments could be shared with healthcare providers and end-users, fostering
confidence in the AI's continued use.

In addition to monitoring the technical performance of AI tools, the assurance laboratories
could evaluate the interaction between end-users, such as HCPs, and the AI systems, as
well as the impact on patient experiences. This may involve gathering qualitative and
quantitative feedback from users, analysing how effectively the tools integrate into clinical
workflows, and identifying potential issues such as misuse, over-reliance, or resistance
among healthcare providers. Similarly, patient interaction with AI-assisted care could be
assessed to ensure tools are used in ways that enhance, rather than compromise, the
quality of care and trust in healthcare systems. By incorporating this human-centred
perspective, the labs could provide a holistic understanding of the AI tools' effectiveness,
usability, and impact.

8.1.5 Development of a catalogue of AI solutions in healthcare

Stakeholders interviewed highlighted that the abundance of AI solutions available results
in challenges to the identification of the most appropriate tool for their setting and
objective. A centralised catalogue of AI solutions for healthcare could serve as a
centralised repository of AI tools available across all medical specialities and application
types.

This catalogue could act as a one-stop platform where healthcare providers, HCPs, and
other stakeholders are able to access detailed information about AI solutions tailored to
their needs. It could provide a structured database that categorises AI tools by
functionality (e.g., diagnostic imaging, predictive analytics, patient triage), medical
specialty (e.g., cardiology, oncology), and operational context (e.g., primary care,
emergency settings). Such a platform may enhance transparency and accessibility,
ensuring that stakeholders can make informed choices based on the specific requirements
of their clinical environments.

A feature of the AI Tool Catalogue could be the inclusion of detailed performance
metrics for each listed AI tool. These metrics, verified through the assurance labs (see
section 7.1.3.2), could cover dimensions such as accuracy, sensitivity, specificity,
robustness, generalisability, and adherence to ethical standards. The “AI catalogue” could
also integrate user reviews and feedback mechanisms, enabling end-users to share their
experiences with specific tools post-deployment. This feature may provide a dynamic layer
of evaluation, capturing real-world insights into how AI tools perform under various clinical
conditions and complementing the technical performance data provided by assurance labs.
Additionally, the platform could include resources such as user guides, case studies, and
tutorials to help healthcare providers understand and implement AI solutions effectively.
By facilitating peer-to-peer knowledge exchange and continuous learning, the
catalogue could support a community-driven approach to AI adoption in healthcare.

To ensure the catalogue remains up-to-date and relevant, a governance framework could
be established to oversee its operations. This framework could involve regular updates to
reflect new AI solutions, performance re-assessments of existing tools, and adaptations to
emerging healthcare needs or regulatory changes. Partnerships with AI developers,
healthcare institutions, and Member States would be important to maintaining the
                                            Deployment of AI in healthcare – Final Report



platform's accuracy and comprehensiveness. By serving as a curated, trustworthy
repository of healthcare AI tools, the catalogue may accelerate the safe and equitable
integration of AI into healthcare systems across the EU, driving innovation while
safeguarding public health interests.

8.1.6 Summary

In summary, several considerations for future actions are presented to facilitate AI
deployment in healthcare. First, establishing common standards for data governance and
interoperability across European healthcare systems would enable seamless AI integration,
support secure cross-border data exchange, and facilitate compliance with regulations.
Secondly, the creation of Centres of Excellence would help address skills gaps, provide
advanced training for healthcare workers, promote public digital health literacy, and foster
collaboration on AI innovations. Thirdly, consolidated funding and financing mechanisms
could support AI projects and ensure equitable access to AI tools across healthcare
systems. Additionally, added-value assessment, local performance tests/studies through
assurance labs and conducting post-deployment monitoring of AI tools could ensure their
effectiveness, safety, and compliance. Finally, developing an AI Catalogue would create a
central repository of AI solutions available, enabling healthcare providers to make
informed decisions and driving innovation across the EU.

    8.2    Monitoring framework for considerations for future actions.
As established by the Better Regulation Guidelines (Tool #43), the first step to design a
monitoring framework for potential EU interventions is to define the scope of such
interventions. To do so, we have assessed what are the objectives of the abovementioned
considerations for future action, the problems they want to address, and the results and
impacts they aim for. This assessment takes the form of an intervention logic which lay
downs the links between the drivers, problems and the objectives of a given intervention
by analysing intertwined inputs, outputs, outcomes and impacts. Below we include the
intervention logic we have developed for the considerations for future actions identified in
the previous sub-sections.
Figure 18: Intervention logic




Source: Authors’ elaboration.
                                                    Deployment of AI in healthcare – Final Report


Once the intervention logic has been established, the second step is to conduct a mapping
of indicators which could feed the monitoring framework to assess the level of
achievement of the objectives in terms of the input, output, outcome and impacts of the
intervention. The selection of indicators is to be done based on the RACER principles
outlined in the Better Regulation Guidelines (Tool #43). The selected indicators should be
relevant (i.e. linked to the objectives to be achieved), acceptable (i.e. are to be accepted
by the Commission and other relevant stakeholders), credible (i.e. accessible to non-
experts, unambiguous and easy to interpret), easy to monitor (i.e. feasible to monitor
at a reasonable cost and administrative burden), and robust (i.e. difficult to manipulate).

To make this exercise easier, we have drawn specific actions for each of the considerations
for future action actions (i.e. activities/output in the intervention logic). These specific
actions were mentioned in the main text explaining the steps to be taken for each
recommended action through the previous sub-sections. In the table in Annex 7, we
provide the list of specific actions for each consideration for future action.

Following the Better Regulation guidelines, the study team has tried to rely as much as
possible on existing reporting requirements for the development of the monitoring
framework. However, this has encountered some limitations as there is a lack of data
available which could inform the monitoring framework 333. Secondly, the monitoring
framework is developed for potential considerations for future action that the Commission
could recommend or implement, and not actual implemented interventions. This makes
the possibility of using existing reporting requirements more difficult. Given the overall
data gaps on indicators that could be used, it remains challenging to suggest measures on
the effectiveness of the actions taken by the Commission without creating a significant
burden in reporting requirements.

As a result of the above, the framework relies primarily on desk research and information
that can be only retrieved upon specific request, which constrains its practical application.
At the same time, the entry into force of key databases, such as EUDAMED, will represent
a significant step forward, as such databases might facilitate the identification and
adoption of more practical indicators, enhancing the operationalisation of the monitoring
framework.

In Annex 8 of this document we provide some data collection and reporting guidelines and
include the full monitoring framework for the proposed considerations for future actions at
EU level.

9       Conclusions
AI has the potential to transform the healthcare sector, addressing challenges that
healthcare systems are facing today such as workforce shortages, diagnostic and
treatment inefficiencies, and disparities in access to care. However, despite significant
progress in AI research and its demonstrated benefits across several medical specialties
and operational tasks, the level of adoption across healthcare systems, remains slow, and
limited. This underlines the need to address existing challenges to deployment, build on
lessons from diverse healthcare systems, and implement actionable strategies to facilitate
equitable and impactful AI deployment across Europe.

There are a number of challenges that need to be overcome to allow for the effective and
efficient deployment of AI across healthcare systems. Technological and data challenges
such as data fragmentation remain a persistent issue, with healthcare systems struggling

333 In Annex 5 – Details on data sources and methodology for market analysis, we provide more details on the
limitations in terms of data sources to assess the level of deployment of AI/ML-enabled medical devices in
clinical practice.
to standardise formats and ensure interoperability across platforms. This lack of uniformity
limits the ability of AI tools to be seamlessly integrated into clinical workflows to process
and analyse data effectively, diminishing their overall utility. Additionally, many healthcare
systems rely on outdated IT infrastructure, which is insufficient to support modern AI
applications, creating an additional barrier to adoption. The lack of standardised local
performance testing protocols to address variations in performance across health care
systems, show the added value of deploying AI systems in clinical practice, as well as the
lack of post-deployment monitoring mechanisms to assess the long-term performance of
AI tools and how end-users interact with them is another barrier to adoption as it often
results in a lack of trust and confidence amongst HCPs. This is further compounded by the
lack of transparency and explainability of AI solutions, often referred to as the “black box”
phenomenon.

The regulatory environment governing AI in healthcare, while robust, presents
complexities that may contribute to hesitancy in AI deployment. The interplay of multiple
regulations also raises challenges to deployers to navigate. Concerns surrounding data
privacy, security, and liability further complicate the terrain.

Organisational and financial challenges also hinder the deployment of AI solutions. The
absence of clear financing mechanisms and reimbursement frameworks for AI-based
systems makes it difficult for healthcare providers to justify investments in these
technologies. Inadequate end-user engagement during the development of AI solutions
can lead to tools that misalign with the practical needs of healthcare professionals or
patients. Additionally, a lack of standardised models for assessing the local added value of
AI tools limits deployers’ ability to evaluate solutions in terms of hospital level performance
and potential benefits.. Obstacles on assessing the local-added value is often compounded
by unclear of strategic direction and clear AI deployment roadmap in some healthcare
systems, which undermines efforts to integrate AI effectively.

Social and cultural factors also play an important role in delaying AI adoption. The level of
trust among HCPs and patients regarding the reliability and ethical implications of AI is a
key factor, which is often exacerbated by concerns surrounding job-security and
overreliance on technology, as well as its impact on the doctor-patient relationship. One
of the drivers of the lack of trust and concerns shared by HCPs and patients is digital health
literacy and technological competence to understand how AI tools operate, their potential
and limitations, and their use as supportive tools in the provision of care.

In addition to the EU, countries that have advanced in the deployment of AI in healthcare,
such as the USA, Israel, and Japan provide valuable insights into addressing these
challenges.. Healthcare systems/providers in these regions have employed various good
practices (accelerators) that may address a range of these challenges, which could further
be investigated within the European context to support the scale-up of deployment.

Widespread AI deployment in healthcare is complex, but the potential rewards are
transformative. By addressing the challenges affecting the deployment of AI in healthcare
and implementing targeted strategies, it is possible to encourage and facilitate healthcare
systems in the EU to adopt AI solutions to deliver high-quality, accessible, and sustainable
healthcare. A collaborative effort involving policymakers, healthcare providers,
developers, and patients is important to realise this vision, ensuring that AI becomes an
integral part of the healthcare landscape in Europe. Through strategic action and a
commitment to overcome deployment challenges, the EU can position itself as a global
leader in AI-driven healthcare innovation.
                                                                                                     Deployment of AI in healthcare – Final Report




10     Annexes
     10.1 Annex 1 – Analytical framework
The analytical framework illustrated in the table below presents the study questions provided within the terms of reference, the framework
served to guide the investigation and analysis toward the overall objectives and scope.

 Study questions                                                  Sub-questions

                                                                  1.1 What are the present-day needs in clinical practice that currently available
 1. What are the current needs in clinical practice that AI
                                                                  AI technology could address?
 could address? How are the needs expected to evolve in the
                                                                  1.2 What are the needs in clinical practice that could be addressed by
 next 5 years?
                                                                  advancements in AI technology in the next 5-years (i.e. GenAI)?
 2. Among those unmet needs, what are the areas where the
                                                                  2.1 In what medical specialties or areas do AI technologies have the greatest
 use of AI in healthcare has the greatest potential to
                                                                  potential?
 transform healthcare including clinicians' daily practice and
                                                                  2.2 In what medical specialities or areas have AI technologies already been
 individuals'/patients' diagnosis, treatments, and
                                                                  adopted?
 management?
                                                                  What are the specific challenges of using AI in healthcare, related to:
 3. What are the specific challenges of using AI in healthcare?
                                                                  3.1 Healthcare professionals that interact with AI tools, for example resistance to
 - What are the specific challenges of using generative AI in
                                                                  change/digital literacy
 healthcare?
                                                                  3.2 Ethical issues (that are not resolved by the AI Act)
 - Are there ethical issues emerging due to the use of AI in
                                                                  3.3 Patient Data protection (that are not resolved by GDPR compliance and the
 healthcare? If so, what are they?
                                                                  upcoming EHDS regulation)
 - Are there data protection and/or IP issues involved? If so,
                                                                  3.4 Patient specific concerns/hesitancy towards use of AI in their care
 what are they?
                                                                  3.5 Related to transparency issues (that are not resolved by the obligations of
 - Are there patient specific concerns in the use of AI?
                                                                  the AI Act)
 - Are there particular transparency issues when deploying AI
                                                                  3.6 Related to clinicians’ liability/standard of care issues (that are not resolved
 in healthcare?
                                                                  by the obligations of the AI Act and the PLD)
 - Are there clinicians’ liability/standard of care issues when
                                                                  3.7 What are the challenges posed by the specific use of generative AI in
 using AI systems?
                                                                  healthcare that may not be considered in the broad scope of the AI act?
                                                                  4.1. How many AI-based medical devices have been CE marked in the EU? And
                                                                  what medical domains do they cover?
 4. How many AI-based medical devices have been CE
                                                                  4.2. How many AI-based medical devices have been FDA approved in the US?
 marked in the EU and how many FDA approved in the US? In
                                                                  And what medical domains do they cover?
 what medical domains?
                                                                  4.3. Are there any other relevant AI-based medical devices deployed in the EU
                                                                  and US which are not CE marked or FDA approved?
5. What is the current state of deployment of AI in clinical
practice? Provide a mapping distinguishing the deployment         5.1. What is the extent of AI deployment in clinical practice across Member
of AI in clinical practice per Member State and relevant third    States and relevant third countries (e.g., USA, Israel, Japan)?
countries as well as drawing a distinction between rural and      5.2. What is the difference of AI deployment in healthcare between urban and
urban areas as well as between medical specialties. Are           rural areas?
there some patterns developing (e.g., geographical,               5.3. What are the differences of AI deployment across medical specialties?
regional, medical specialty related)? If so, what could be        5.4. What are the factors explaining these differences in AI deployment?
possible explanations? Is the deployment of AI benefiting         5.5. To what extent is AI deployment in healthcare benefitting patients equally?
patients equally?
                                                                  6.1. How does AI impact clinical workflows?
6. How does AI impact/transform clinical practice? Among          6.2. How does AI impact the application of clinical guidelines?
others, how does the deployment of AI impact clinical             6.3. How does AI impact healthcare systems?
workflows, clinical guidelines, healthcare system                 6.4. How does AI impact collaboration amongst clinicians?
transformation, clinicians’ collaborations, healthcare workers    6.5. How does AI impact the healthcare workforce working time?
working time, patients, doctor-patient relationships,             6.6. How does AI impact the relationship between healthcare professionals and
standard of care?                                                 patients?
                                                                  6.7. How does AI impact the standard and quality of care?
7.    What are the challenges and barriers in the EU and
relevant third counties – including technical, operational,       7.1. To what extent do technological and data challenges (e.g., IT infrastructure)
budgetary, administrative, legal, ethical, educational, data      impact the effective and efficient deployment of AI in clinical practice?
protection, privacy, social, cultural, and other – to the         7.2. To what extent do legal and regulatory challenges (e.g., data protection,
effective and efficient deployment of AI in clinical practice?    privacy) impact the effective and efficient deployment of AI in clinical practice?
                                                                  7.3. To what extent do organisational and business challenges (e.g., operational,
- How do these barriers compare in terms of significance?         budgetary, administrative) impact the effective and efficient deployment of AI in
- Do the same or similar AI systems perform differently in        clinical practice? List specific challenges.
diverse environments? If so, what are the factors that lead       7.4. To what extent do social and cultural challenges (e.g., digital health literacy,
to this diverse performance beyond those attributed to the        lack of trust in AI) impact the effective and efficient deployment of AI in clinical
technical development of an AI system and data used for           practice? List specific challenges.
training/validating the algorithm (e.g., how is AI used in        7.5. To what extent and how do certain factors (e.g., the healthcare setting, the
different environments (e.g., urban v rural hospitals etc.), by   healthcare professional, the medical specialty) impact the performance of AI
different clinicians (GPs, specialists etc.), within different    technologies in clinical practice?
specialties etc.)?                                                7.6. How can the barriers described above be addressed at EU level to ensure AI
- How could AI be deployed in healthcare settings in a way        is deployed in healthcare settings in a way that is acceptable for and trusted by
that is acceptable for and trusted by patients? What makes        patients?
patients distrust or reject AI healthcare settings?
                                                                                                     Deployment of AI in healthcare – Final Report




                                                                  7.1. To what extent do good practices addressing technological and data
                                                                  challenges (e.g., ethical challenges) ensure the effective and efficient
                                                                  deployment of AI in clinical practice? List specific favouring conditions and good
                                                                  practices and describe why they are successful.
                                                                  7.2. To what extent do good practices addressing legal and regulatory
8.    What are the existing favouring conditions and
                                                                  challenges (e.g., data protection, privacy) ensure the effective and efficient
practices - including technical, operational, budgetary,
                                                                  deployment of AI in clinical practice. List specific favouring conditions and good
administrative, legal, ethical, educational, social, cultural,
                                                                  practices and describe why they are successful.
and other – to the effective and efficient deployment of AI in
                                                                  7.3. To what extent do good practices addressing organisational and business
clinical practice?
                                                                  challenges (e.g., operational, budgetary, administrative) ensure the effective
- Indicate best (good) AI deployment practices in the EU as
                                                                  and efficient deployment of AI in clinical practice? List specific favouring
well as in third countries based on the conditions and
                                                                  conditions and good practices and describe why they are successful.
practices identified.
                                                                  7.4. To what extent do good practices addressing social and cultural
- Why are these conditions and practices successful? To what
                                                                  challenges (e.g., educational, social, cultural) ensure the effective and efficient
extent can they be transferred or adapted in diverse settings
                                                                  deployment of AI in clinical practice? List specific favouring conditions and good
(e.g., university v non-university hospital, rural v urban
                                                                  practices and describe why they are successful.
hospital, size of hospital and expertise of clinicians etc.)?
                                                                  7.5. Specify other favouring conditions and good practices can ensure the
                                                                  effective and efficient deployment of AI in clinical practice and describe to what
                                                                  extent.
                                                                  7.6. To what extent are each of the above favouring conditions and good
                                                                  practices transferable across healthcare settings and regions?
9. Do the existing legal frameworks (e.g., HTA, MDR/IVDR),        9.1. To what extent does the HTAR address the barriers in deploying AI in clinical
horizontal AI proposals (e.g., AIA, PLD, AILD) and sector         practice (consider at which stage in the life cycle of a health technology would AI
specific initiatives (e.g., EHDS) address some of the barriers    have the greatest potential to support joint work through evidence generation
and accelerators in deploying AI in clinical practice? Are        such as for horizon scanning of emerging health technologies, joint scientific
there gaps in these legislations/complementary needed             consultations, joint clinical assessments, and post-marketing)? What are the
actions related specifically to deployment of AI in clinical      gaps?
practice?                                                         9.2. To what extent does the MDR/IVDR address the barriers in deploying AI in
- What is the impact of the “human oversight” provisions in       clinical practice (consider how the requirements under these Regulations could
the AIA on a clinical setting (Art. 14)?                          be applicable for AI-based solutions in terms of health, safety, and innovation in
- Is there an impact, and if so what, of the “transparency        practice)? What are the gaps?
and provision of information to users” under the AIA on           9.3. To what extent does the AIA address the barriers in deploying AI in clinical
clinical practice (Art 13)?                                       practice (consider the impact of the “human oversight” provisions in the AIA on a
- What is the impact of the “obligations of users of high-risk    clinical setting (Art. 14), the impact of the "transparency and provision of
AI systems” under the AIA on clinicians, hospitals etc (Article   information to users under the AIA on clinical practice (Art 13), the impact of the
26 AIA)?                                                          "obligations of users of high-risk AI systems" under the AIA on clinicians,
- Are there implications on the development of a “risk            hospitals (Art 29), and the implications on the development of a "risk
management system” in the AIA in clinical practice beyond        management system" in the AIA in clinical practice beyond the manufacturers'
the manufacturers’ obligations (Article 9)?                      obligations (Art 9)) ? What are the gaps?
- How should “causation” in the proposed product liability       9.4. To what extent does the PLD address the barriers in deploying AI in clinical
directive (PLD) be better interpreted for AI in healthcare?      practice (consider how "causation" be better interpreted for the use of generative
Especially as regards generative AI systems used in clinical     AI systems in clinical practice)? What are the gaps?
practice.                                                        9.5. To what extent does the AILD address the barriers in deploying AI in clinical
- As regards the Health Technology Assessment Regulation         practice? What are the gaps?
(HTAR), at which stage in the life cycle of a health             9.6. To what extent does the EHDS address the barriers in deploying AI in clinical
technology would AI have the greatest potential to support       practice? What are the gaps?
joint work through evidence generation such as for horizon       9.7. Are additional actions needed to address the barriers for the deployment of
scanning of emerging health technologies, joint scientific       AI in clinical practice?
consultations, joint clinical assessments, and post-
marketing?
- As regards the MDR and IVDR, how the requirements
under these Regulations could be applicable for AI-based
solutions in terms of health, safety, and innovation in
practice?
10. What complementary actions (EU, national etc. as well
as regulatory/non-regulatory etc.) might still be required to
                                                                 10.1 What complementary actions (regulatory/non-regulatory) are still required
ensure the safe and effective deployment of AI in light of the
                                                                 to ensure the safe and effective deployment of AI in clinical practice?
challenges and accelerators identified? What would be their
                                                                 10.2 What complementary actions are required to enhance trust, acceptability,
advantages and limitations?
                                                                 transparency and explainability of AI in clinical practice with respect to
- Among others, what complementary actions could
                                                                 deployment?
contribute to enhancing trust and acceptability of AI in
                                                                 10.3 What complementary actions are required to ensure equal access for
clinical practice, as well as transparency and explainability?
                                                                 patients to the use of AI in clinical practice?
- In addition, how can equal access for patients to the use of
AI in clinical practice be ensured?
                                                                 11.1. What are real-world scenarios where the recommended actions can be
11. How could the recommended actions identified in this
                                                                 assessed?
study be empirically assessed in real world scenarios (e.g.,
                                                                 11.2. What are the existing indicators and data sources to monitor the
pilot projects etc.)? What indicators would allow to monitor
                                                                 effectiveness and efficiency of the recommended actions?
the effectiveness and efficiency of the recommended
                                                                 11.3. What indicators and data sources are missing to measure the effectiveness
actions?
                                                                 and efficiency of the recommended actions?
                                                                                                                    Deployment of AI in healthcare – Final Report


     10.2 Annex 2 – Survey questionnaires
A mapping of the study questions addressed to each stakeholder category can be found in the table below.

10.2.1 Patient Survey

     1. How would you rate your knowledge about the use of artificial intelligence in healthcare 334? (single answer)
            • Advanced knowledge
            • Solid knowledge
            • Basic knowledge
            • No or limited knowledge
                                                                                                       Advanced/Solid                         Basic/No/ Limited
     2. What factors contribute to your current level of knowledge about AI in healthcare?
        (multiple answer)
            • Limited exposure to information and/or educational resources
            • Lack of interest in technology or healthcare advancements
            • Lack of trust in new technologies
            • Complexity of AI concepts and terminology                                                                                               X
            • Difficulty understanding the potential applications of AI in healthcare
            • Limited discussions or explanations from healthcare providers
            • Fear of technology or apprehension about AI replacing human healthcare providers
            • Other (please specify)
            • None of the above
     3. What methods do you believe would be effective in improving your knowledge about
        artificial intelligence in healthcare? (multiple answer)
            • Clear communication and education of the benefits of using AI in healthcare
            • Clear communication from the healthcare professional on how AI is used in
                 delivery of care                                                                              X
            • Clear communication from the healthcare professional on how the AI model works
                 and comes to its decisions
            • Other (please specify)
            • I do not know
     4. How do you feel about the idea of the following types of AI being used in your healthcare
        (Options: Very comfortable, somewhat comfortable, neutral, somewhat uncomfortable,                                                            X
        very uncomfortable, I do not know)


334 Patients were asked specific sets of questions dependent upon their level of knowledge of AI. This is indicated by “X”
       •  Assisting healthcare professionals with diagnosis
       •  Assisting healthcare professionals with your treatment
       •  Assisting healthcare professionals with remote monitoring of your health
       •  Assisting healthcare professionals with administrative tasks
       •  Optimisation of clinical workflows (e.g., optimize the allocation of medical staff,
          equipment, and rooms based on patient load and predicted demand, ensuring
          efficient use of resources and reducing wait times)
       • Conversational platforms (“chatbots”) for patient assistance
5. In your opinion, what impact will the use of artificial intelligence have on healthcare
   settings in the coming years?
   (Options: Significantly improve, slightly improve, no impact, slightly worsen, significantly
   worsen, I do not know)
       • Speed and accuracy of diagnosis of medical conditions
       • Personalised treatment plans tailored to my individual needs
       • Access to healthcare services, especially in rural or underserved areas
       • Efficiency in healthcare delivery, reducing waiting times
       • Management of chronic conditions through remote monitoring and proactive
          interventions
       • Cost saving on healthcare expenses
       • Communication and coordination among healthcare providers
       • Other (please specify)

   If worsen or slightly worsen was selected:                                                     X
   Why do you feel uncomfortable with artificial intelligence tools being used in your
   healthcare or believe that artificial intelligence will have a negative impact on the
   standard and quality of care in the coming years? (multiple answer)
       • AI algorithms are not reliable or accurate enough to positively impact the standard
          and quality of care
       • Increased reliance on AI in healthcare will lead to a loss of the human touch in
          medical care, potentially worsening patient experiences and outcomes
       • The use of AI in healthcare could compromise patient privacy or result in data
          breaches, leading to negative consequences for patient outcomes
       • Increasing use of AI in healthcare could lead to job loss for healthcare
          professionals, potentially affecting the quality of patient care and outcomes
       • Negative experiences with technology in the past made me sceptical about the
          benefits of AI in healthcare and its potential impact on the standard and quality of
          care
                                                                                        Deployment of AI in healthcare – Final Report


       •   Concerns that AI algorithms may be biased or unfair, leading to disparities in
           healthcare outcomes for certain patient populations
       • Concerns about the lack of regulation and oversight surrounding the use of AI in
           healthcare, as well as ethical implications related to issues such as consent and
           transparency
       •    Other (please specify)
       • I do not have sufficient knowledge to respond
6. What concerns, if any, do you have about the use of AI in healthcare? (multiple answer)
       • Concerns about data privacy, confidentiality, and security
       • Lack of trust in accuracy of decisions made by AI and technical malfunctions
           resulting in misdiagnosis
       • Lack of information on how decisions are made by AI models
       • Over-reliance on technology and lack of human oversight
       • Concerns about the lack of AI competence amongst healthcare professionals                     X                  X
       • Loss of patient-doctor relationship
       • Unclear liability and accountability structure in case of errors or adverse outcomes
           caused by AI solutions
       • Other (please specify)
       • I do not have any concerns
       • I do not have sufficient knowledge to respond
7. Which of the following factors, if any, would make you more comfortable with artificial
   intelligence being used in your healthcare? (multiple answer)
       • Clear communication and education of the benefits of using artificial intelligence in
           healthcare
       • Clear communication from the healthcare professional on how artificial intelligence
           is used in delivery of care
       • Clear communication from the healthcare professional on how the artificial
           intelligence model works and comes to its decisions
                                                                                                       X                  X
       • Informed consent on the use of artificial intelligence in delivery of care
       • Human oversight over artificial intelligence decisions
       • Clear communication of data protection measures when using artificial intelligence
       • Clear liability and accountability in case of errors or adverse outcomes caused by
           artificial intelligence solutions
       • Clear communication on how the artificial intelligence model is regulated
       • Other (please specify)
       • None of the above
            • I do not have sufficient knowledge to respond
     8. In your opinion, does the use of artificial intelligence-based tools in the delivery of
        healthcare to vulnerable groups require additional measures beyond those you described
        above?
                                                                                                                                       X
            • Yes (please specify)
            • No
            • I do not know


10.2.2 Healthcare Professional Survey

     1. Please indicate your medical speciality or the medical speciality your association represents (single answer):
            • Radiology
            • Pathology
            • Oncology
            • Cardiology
            • Neurology
            • Orthopaedics
            • Psychiatry
            • Ophthalmology
            • Pulmonology
            • Endocrinology
            • Nephrology
            • Rheumatology
            • Other (please specify)
     2. How would you rate your knowledge about the use of artificial intelligence in healthcare? (single answer)335
            • Advanced knowledge
            • Solid knowledge
            • Basic knowledge
            • No or limited knowledge
                                                                                                           Advanced/Solid                    Basic/Limited
     3. What is the reason for your lack of knowledge of artificial intelligence tools and their use in
        healthcare? (multiple answer)
                                                                                                                                                   X
            • Limited exposure to information and/or educational resources
            • Lack of interest in technology or healthcare advancements

335 Healthcare Professionals were asked specific sets of questions dependent upon their level of knowledge of AI. This is indicated by “X”
                                                                                        Deployment of AI in healthcare – Final Report


       •   Lack of trust in new technologies
       •   Lack of interpretability and transparency of AI tools in giving a case-specific decision
       •   Concerns about the quality and robustness of AI tools
       •   Lack of empirical evidence demonstrating the potential transformative effect of
           applications of AI in healthcare
       • Lack of education and training on this topic at the healthcare facility, and unsure where
           to seek relevant training
       • Fear of technology or apprehension about AI replacing human healthcare providers
       • Other (please specify)
       • None of the above (please specify
4. What methods do you believe would be effective in improving your knowledge about artificial
   intelligence in healthcare? (multiple answer)
       • Clear communication and education of the benefits of using AI in healthcare
       • Clear communication from the healthcare facility/AI developer on how AI is used in
                                                                                                                            X
           delivery of care
       • Clear communication from the healthcare facility/AI developer on how the AI model
           works and comes to its decisions
       • Other (please specify)
5. In your opinion, what impact will the use of artificial intelligence have on healthcare settings
   in the coming years?
   (Options: Significantly Improve, Slightly Improve, No Impact, Slightly Worsen, Significantly
   Worsen, I do not know)
       • Speed and accuracy of diagnosis of medical conditions
       • Personalised treatment plans tailored to my individual needs
       • Access to healthcare services, especially in rural or underserved areas                                            X
       • Efficiency in healthcare delivery, reducing waiting times
       • Management of chronic conditions through remote monitoring and proactive
           interventions
       • Cost saving on healthcare expenses
       • Communication and coordination among healthcare providers
       • Other (please specify)
6. In your medical specialty, what are the current healthcare needs that existing artificial
   intelligence technologies have the potential to already address now? (multiple answer)
       • Optimizing resource allocation and workflow efficiency                                            X
       • Streamlining administrative tasks Improving diagnostic accuracy
       • Creating personalized treatment plans
        • Predictive analytics for patient outcomes
        • Improving patient engagement and adherence to treatment plans
        • Addressing skill gaps among the healthcare workforce
        • Ensuring equitable access to healthcare
        • Other (Please specify)
        • I do not know
7. If applicable, what percentage of time do you or healthcare professionals in general spend in
    carrying out administrative tasks related to the provision of healthcare but that are not strictly   X   X
    medical tasks? (Sliding scale)
8. In your opinion, what are the needs in healthcare that artificial intelligence advances could
    address in the next 5 years (needs that cannot be addressed by existing AI technologies)?            X
    (Free text)
9. In your opinion, to what extent do the following applications have the potential to provide
    concrete added value to the existing delivery of healthcare in your medical specialty?
    (Options: Large Extent, Moderate Extent, Small Extent, I do not know, Not applicable)
        • AI-assisted diagnostics
        • AI-assisted surgery/medical robotics to optimize surgical skills
        • AI-assisted remote patient monitoring
        • AI-assisted symptom checkers and support in treatment decisions (e.g. surgical                 X
           indications, use and dosage of medications, and complication management)
        • Administrative support tool (e.g., EHR management, for clinical documentation)
        • Clinical workflow optimisation (e.g., predicting patient admissions, bed occupancy)
        • Conversational platforms for patient assistance (e.g., chatbots, virtual assistants)
        • AI-assisted prognosis prediction (risk stratification)
        • Other (please specify)
10. Have you used or are you currently using artificial intelligence technologies in your clinical
    practice? (Single answer)
        • Yes (Please specify tools and state of deployment)                                             X
        • No
        • I don’t know
11. Have you used or are you aware of any generative AI tools used in the healthcare facility
    within which you work? (Single answer)
                                                                                                         X
        • Yes (Please specify tools and state of deployment)
        • No
                                                                                           Deployment of AI in healthcare – Final Report


12. Based on your knowledge, to what extent do the following technological and data
    challenges impact the effective and efficient deployment of artificial intelligence tools in the
    healthcare facility within which you work?
    (For each option, impact was rated significant, moderate, no or I do not know. The
    responders were also asked for the relevance of the challenge for in house developed tools,
    commercially available tools or both)
       • Outdated IT infrastructure
       • Lack of interoperability of AI solutions with existing IT solutions                                  X
       • Lack of standardised data structures
       • Variations in performance across healthcare settings and populations
       • Quality concerns amongst end-users
       • Lack of transparency and explainability of AI tools
       • Lack of validation protocols for existing AI solutions
       • Other (Please specify)

13. Based on your knowledge, to what extent did the following legal and regulatory challenges
    and barriers impact the effective and efficient deployment of artificial intelligence tools in the
    healthcare facility within which you work?
    (For each option, impact was rated significant, moderate, no or I do not know. The
    responders were also asked for the relevance of the challenge for in house developed tools,
    commercially available tools or both)
                                                                                                              X
        • Lack of accountability and liability structure for errors by AI
        • Cybersecurity issues and vulnerability of data-to-data breaches
        • Complexity of regulatory approval process for AI product commercialisation
        • Lack of guidance on compliance of AI tools with current legislation
        • Concerns surrounding data privacy and data protection
        • Other (Please specify)
14. Based on your knowledge, to what extent did the following organizational and business
    challenges and barriers impact the effective and efficient deployment of artificial intelligence
    tools in the healthcare facility within which you work?
    (For each option, impact was rated significant, moderate, no or I do not know. The
    responders were also asked for the relevance of the challenge for in house developed tools,               X
    commercially available tools or both)
        • Lack of strategic direction to promote AI in healthcare
        • Lack of technological skills and knowledge amongst healthcare professionals to use AI
            tools effectively
       •   Lack of involvement of end-users in the development, validation and deployment of AI
           tools
       •   Lack of cost-benefit analysis of AI tools versus existing clinical solutions
       •   Lack of funding, investment and financial incentives to deploy AI in clinical practice
       •   Other (please specify)

15. Based on your knowledge, to what extent do the following social and cultural challenges and
    barriers impact the effective and efficient deployment of artificial intelligence tools in the
    healthcare facility within which you work?
    (For each option, impact was rated significant, moderate, no or I do not know. The
    responders were also asked for the relevance of the challenge for in house developed tools,
    commercially available tools or both)
        • Concerns among healthcare professionals on job security
                                                                                                     X
        • Low level of digital health literacy among healthcare providers and the general public
        • Concerns about AI's impact on the personal relationship between doctor and patient
        • Concerns about patient autonomy and consent in the use of AI tools for their care
        • Lack of trust in AI tools
        • Concerns about skill shift to remain competitive in the job market
        • Concerns about overreliance on AI
        • Other (please specify)
16. Are there any other challenge and barriers not described above affecting the effective and
    efficient deployment of artificial intelligence in healthcare? (Single answer)
                                                                                                     X
        • Yes (Please specify)
        • No
17. Are you aware of specific challenges affecting the deployment of generative AI models in
    clinical practice? (Single answer)
                                                                                                     X
        • Yes (Please specify)
        • No
18. Which of the following practices could address technological and data challenges in the
    healthcare facility within which you work and improve the uptake of artificial intelligence
    tools? (Multiple answer)
        • Early engagement of end users, such as yourself, to ensure relevance and usability
                                                                                                     X
        • Short and concise guidelines on how the AI model works to ensure transparency,
             interpretability and explainability
        • Definition of minimum IT standards to facilitate widespread deployment and promotion
             of interoperability
                                                                                        Deployment of AI in healthcare – Final Report


       •    Testing and pilot studies to ensure safety, efficacy and interoperability
       •    Training and validation on diverse datasets to account for performance variation
       •    Post-deployment monitoring mechanism to assess the performance of AI systems in
            real and diverse clinical settings
        • Human oversight over AI model decisions
        • Other (Please Specify)
        • Not applicable
        • I do not know
19. Which of the following practices could be implemented within the healthcare facility within
    which you work to address legal and regulatory challenges and improve the uptake of artificial
    intelligence tools? (Multiple answer)
        • Legal guidance and clarification of roles
        • Policies and guidance on information access and sharing within your healthcare facility
                                                                                                           X
        • Regulatory guidance to define user responsibilities and liabilities concerning AI models
        • Informed consent protocols to maintain patient autonomy and data privacy
        • Other (Please Specify)
        • Not applicable
        • I do not know
20. Which of the following practices could address organizational and business challenges in the
    healthcare facility within which you work and improve uptake of artificial intelligence tools?
    (Multiple answer)
        • Tools to assess and evaluate the added value of deploying an AI solution in clinical
            practice compared to existing solutions
        • Multidisciplinary collaboration to ensure integration into clinical workflow
        • Renewing reimbursement models to align with value-based care
        • Involvement of all stakeholders in decision-making processes
        • Validation of the system by healthcare professionals before deployment
        • New talent acquisition to ensure workflow readiness and expertise
        • Clearly defined strategy for AI deployment in clinical practice
        • Improving affordability through funding, capital investment and financial incentives
        • Other (Please Specify)
        • Not applicable
        • I do not know
21. Which of the following practices could address social and cultural challenges in the healthcare
    facility within which you work and improve uptake of artificial intelligence tools? (Multiple
    answer)
        • Integration of technology into medical curricula
        • Promoting continuous learning to keep up with the advancements
        • Targeted training programs to upskill workforce                                               X
        • Development of a consistent narrative of the benefits of AI for patients, practitioners,
             and organizations to improve trust
        • Other (Please Specify)
        • Not applicable
        • I do not know
22. Are you aware of specific good practices for the deployment of generative AI models in clinical
    practice? (Single answer)
                                                                                                        X
        • Yes (Please specify)
        • No
23. Are you aware of the EU AI Act? (Single answer)
        • Yes                                                                                           X
        • No
24. Does the AI Act address any of the challenges you highlighted above affecting the effective
    and efficient deployment of AI in healthcare? (Single answer)
       • Yes (Please specify)
       • No                                                                                             X
       • I do not know

25. Do any of the deployer (user) obligations under the AI Act described above introduce new or
    additional challenges to healthcare professionals such as yourself?
       • Yes (Please specify)
       • No                                                                                             X
       • I do not know

26. What additional support could be provided to healthcare professionals such as yourself to
    address the challenges introduced by the AI Act?                                                    X

27. In your opinion, what action could support healthcare institutions to efficiently and effectively
    deploy artificial intelligence tools in clinical practice?                                          X
        • Consolidated funding to support specific strategic priorities
                                                                                               Deployment of AI in healthcare – Final Report


           •   Establishment of common standards on data governance, privacy, and interoperability
           •   Ensure consistent access to public data and promoting open-data initiatives
           •   Organisation and centralised collection of post-deployment data to monitor on the
               ongoing effectiveness of AI tools
           •   Provide clarity on regulatory processes for product approval, accountability, and
               liability
           •   Encourage the establishment of centres of excellence for AI in healthcare to
               concentrate talent and resources
           •   Establish an EU AI in healthcare centre to coordinate and facilitate AI deployment
           •   Redesigning workforce planning and clinical education to address future healthcare and
               AI professional needs, investing in upskilling frontline staff.
           •   Development of platforms to facilitate dialogues and exchange of good practices to
               facilitate deployment of AI tools
           •   Other (please specify)
           •   I do not know
           •   None of the above


10.2.3 Hospital Representative Survey

    2. What of the following best represents the location of the healthcare facility you represent? (single answer):
         • Small town (less than 50,000 inhabitants)
         • Medium-sized city (50,000-250,000 inhabitants)
         • Large city (250,000-1,000,000 inhabitants)
         • Metropolitan area (over 1,000,000 inhabitants)
         • Other (please specify)
    3. The healthcare facility I represent is a (single answer):
           • Public healthcare facility
           • Private healthcare facility
           • I work at both a private and public healthcare facility
           • Other (please specify)
    4. What are the top 3 challenges in your healthcare facility that hinder productivity, efficiency, and effectiveness in diagnosing,
       treating, and managing patients? (Free text)
    5. What are the current needs in your healthcare facility that existing artificial intelligence technologies have the potential to
       already address now? (multiple answer)
       • Optimizing resource allocation and workflow efficiency
       • Streamlining administrative tasks Improving diagnostic accuracy
       • Creating personalized treatment plans
       • Predictive analytics for patient outcomes
       • Improving patient engagement and adherence to treatment plans
       • Addressing skill gaps among the healthcare workforce
       • Ensuring equitable access to healthcare
       • Other (Please specify)
       • I do not know
6. If applicable, what percentage of time do you or healthcare professionals in general spend in carrying out administrative tasks
   related to the provision of healthcare but that are not strictly medical tasks? (sliding scale)
7. In your opinion, what are the needs in healthcare that artificial intelligence advances could address in the next 5 years (needs
   that cannot be addressed by existing AI technologies)? (Free text)
8. In your opinion, to what extent do the following applications have the potential to provide concrete added value to the existing
   delivery of healthcare in your medical specialty?
   (Options: Large Extent, Moderate Extent, Small Extent, I do not know, Not applicable)
       • AI-assisted diagnostics
       • AI-assisted surgery/medical robotics to optimize surgical skills
       • AI-assisted remote patient monitoring
       • AI-assisted symptom checkers and support in treatment decisions (e.g. surgical indications, use and dosage of
           medications, and complication management)
       • Administrative support tool (e.g., EHR management, for clinical documentation)
       • Clinical workflow optimisation (e.g., predicting patient admissions, bed occupancy)
       • Conversational platforms for patient assistance (e.g., chatbots, virtual assistants)
       • AI-assisted prognosis prediction (risk stratification)
       • Other (please specify)
9. In your opinion, in which medical specialties does the use of artificial intelligence have the biggest transformative potential?
   (single answer)
       • Radiology
       • Pathology
       • Oncology
       • Neurology
       • Cardiology
       • Primary care
       • Psychiatry
                                                                                           Deployment of AI in healthcare – Final Report


        • Triage
        • General hospital administration
        • Other (please specify)
        • I do not know
10. Which of the following best describes your experience with development and/or deployment of artificial intelligence tools in
    healthcare? (Multiple answer)
        • Developed (in house) an AI solution and deployed it
        • Purchased a commercially available AI solution and deployed it
        • Developed (in house) an AI solution but not deployed it
        • Purchase a commercially available AI solution but has not deployed it yet
        • Piloting an AI solution
        • In the process of purchasing/developing an AI solution that we intent to deploy
        • Is not developing and has not purchased any AI solutions, and has not deployed any AI solutions (please elaborate)
        • None of the above
11. Please list the names of the artificial intelligence tools you use or intend to use in clinical practice in your healthcare facility
    (Specify tool and current state of deployment. Options: early deployment in the absence of formal processes and policies; pilot
    phase; advanced deployment including widespread and ongoing use)
12. Do you use specific indicators to monitor the effectiveness of artificial intelligence tools in clinical practice?
        • Yes
        • No
13. Do you use specific indicators to monitor the efficiency of artificial intelligence tools in clinical practice?
        • Yes
        • No
14. If applicable, what are the reasons why some of the artificial intelligence tools you developed and/or purchased have not yet
    been deployed in clinical practice? (Multiple answer)
        • The AI tool is undergoing regulatory approval processes
        • The AI tool is undergoing testing and validation to ensure its accuracy, reliability, and safety before deployment in real-
            world healthcare settings
        • Limited access to high-quality healthcare data for training and testing the AI tool
        • Lack of interoperability and compatibility with electronic health records (EHRs), medical devices, and other existing IT
            infrastructure
        • Lack of funding or resources to support deployment
        • Unfavourable market conditions for effective deployment
        • Concerns about usability, workflow integration, and training
        • Concerns surrounding data privacy, liability, and patient consent
        • Technical limitations related to scalability and computational resources required for effective deployment
        • Considerations regarding the competitive market landscape
        • Other (please specify)
        • None of the above
        • Not applicable
15. Have you deployed any generative AI solutions in your healthcare facility?
        • Yes (Specify tool and transformative potential of tool. Options: high, moderate, low, I do not know)
        • No
16. Based on your knowledge, to what extent do the following technological and data challenges impact the effective and
    efficient deployment of artificial intelligence tools in the healthcare facility within which you work?
    (For each option, impact was rated significant, moderate, no or I do not know. The responders were also asked for the
    relevance of the challenge for in house developed tools, commercially available tools or both)
        • Outdated IT infrastructure
        • Lack of interoperability of AI solutions with existing IT solutions
        • Lack of standardised data structures
        • Variations in performance across healthcare settings and populations
        • Quality concerns amongst end-users
        • Lack of transparency and explainability of AI tools
        • Lack of validation protocols for existing AI solutions
        • Other (Please specify)
17. Based on your knowledge, to what extent did the following legal and regulatory challenges and barriers impact the
    effective and efficient deployment of artificial intelligence tools in the healthcare facility within which you work?
    (For each option, impact was rated significant, moderate, no or I do not know. The responders were also asked for the
    relevance of the challenge for in house developed tools, commercially available tools or both)
        • Lack of accountability and liability structure for errors by AI
        • Cybersecurity issues and vulnerability of data-to-data breaches
        • Complexity of regulatory approval process for AI product commercialisation
        • Lack of guidance on compliance of AI tools with current legislation
        • Concerns surrounding data privacy and data protection
        • Other (Please specify)
18. Based on your knowledge, to what extent did the following organizational and business challenges and barriers impact the
    effective and efficient deployment of artificial intelligence tools in the healthcare facility within which you work?
    (For each option, impact was rated significant, moderate, no or I do not know. The responders were also asked for the
    relevance of the challenge for in house developed tools, commercially available tools or both)
        • Lack of strategic direction to promote AI in healthcare
        • Lack of technological skills and knowledge amongst healthcare professionals to use AI tools effectively
        • Lack of involvement of end-users in the development, validation and deployment of AI tools
                                                                                          Deployment of AI in healthcare – Final Report


        • Lack of cost-benefit analysis of AI tools versus existing clinical solutions
        • Lack of funding, investment and financial incentives to deploy AI in clinical practice
        • Other (please specify)
19. Based on your knowledge, to what extent do the following social and cultural challenges and barriers impact the effective and
    efficient deployment of artificial intelligence tools in the healthcare facility within which you work?
    (For each option, impact was rated significant, moderate, no or I do not know. The responders were also asked for the
    relevance of the challenge for in house developed tools, commercially available tools or both)
        • Concerns among healthcare professionals on job security
        • Low level of digital health literacy among healthcare providers and the general public
        • Concerns about AI's impact on the personal relationship between doctor and patient
        • Concerns about patient autonomy and consent in the use of AI tools for their care
        • Lack of trust in AI tools
        • Concerns about skill shift to remain competitive in the job market
        • Concerns about overreliance on AI
        • Other (please specify)
20. Are there any other challenge and barriers not described above affecting the effective and efficient deployment of artificial
    intelligence in healthcare? (Single answer)
        • Yes (Please specify)
        • No
2. Are you aware of specific challenges affecting the deployment of generative AI models in clinical practice? (Single answer)
        • Yes (Please specify)
        • No
21. Which approach do you believe facilitated a more seamless deployment of artificial intelligence tools into the clinical workflow at
    your healthcare facility?
        • Purchasing a commercially available AI tool
        • Developing an AI tool in-house
        • No difference
        • I do not know, we only deployed commercially available AI tools
        • I do not know, we only deployed in-house developed AI tools
        • I do not know; we have not deployed any AI tools
22. What good practices did your healthcare facility implement to address technological and data challenges affecting the
    deployment of artificial intelligence in healthcare? (Multiple answer)
        • Invested in upgrading and modernizing our IT infrastructure prior to the deployment to support the AI implementation
        • Conducted validation tests of the AI algorithms and models
        • Implemented data governance frameworks to ensure the quality and integrity of the AI data
        • Explored partnerships with the AI vendors to access different AI solutions
        • Guidance on transparency, interpretability and explainability of AI solutions to ensure trust in outcomes
        • Post-deployment monitoring mechanism to assess the performance of AI systems
        • Collection of post-deployment data to evaluate impact and ongoing effectiveness of AI tools
        • Other (please specify)
23. What good practices did your healthcare facility implement to address legal and regulatory challenges affecting the deployment
    of artificial intelligence in healthcare? (Multiple answer)
        • Clarification on how privacy and data protection rules apply to AI
        • Regulatory clarification and guidance on secondary use of health data
        • Policies and guidance around the ethical use of AI in healthcare
        • Accountability and liability rules for manufacturers, deployers and users applicable to AI systems in health care
        • A dedicated compliance team to oversee the process of AI deployment
        • Regular reviewing of AI usage policies to remain up to date with any changes
        • Regular audits to monitor compliance
        • Collaboration with regulatory bodies to share best practices
        • Other (please specify)
24. What good practices did your healthcare facility implement to address organisational and business challenges affecting the
    deployment of artificial intelligence in healthcare? (Multiple answer)
        • Tools to assess and evaluate the added value of deploying an AI solution in clinical practice compared to existing
             solutions
        • Developed a strategy or action plan for the efficient and effective deployment of AI in healthcare
        • A comprehensive implementation plan was developed with defined roles and responsibilities for all the staff
        • Sufficient resources and budget were planned and allocated for the deployment
        • Training programs were conducted for the staff and management programs were tailored accordingly
        • Clear metrics and benchmarks were established to measure the impact of AI deployment and look for areas for
             improvement
        • Other (please specify)
25. What good practices did your healthcare facility implement to address social and cultural challenges affecting the deployment of
    artificial intelligence in healthcare? (Multiple answer)
        • Communicated openly with stakeholders to address any concerns and gather regular feedback
        • Promoted open and transparent communication about the utilization of the AI tool and the risks and benefits associated
             with it
        • Conducted community outreach and education campaigns
        • Gradually introduced the AI tool encouraging experimentation and learning, and rewarded creative initiatives that drove
             positive change
        • Other (please specify)
26. What steps did your healthcare facility take to prepare the workforce for artificial intelligence tool deployment?
                                                                                        Deployment of AI in healthcare – Final Report


    For each option specify implemented (yes/no) and transferability of practice (highly transferable, moderately transferable,
    limited transferability, I do not know or not applicable)
        • Provided comprehensive training on AI tool usage and best practices.
        • Fostered a culture of lifelong learning and skill development
        • Created opportunities for staff involvement in AI implementation projects
        • Offered support services and resources to address staff concerns and challenges
        • Other (please specify)
27. Are you aware of specific good practices for the deployment of generative AI models in clinical practice?
        • Yes (please specify)
        • No
28. Are you aware of the EU AI Act? (Single answer)
        • Yes
        • No
29. Are you prepared for the implementation of the AI Act and the associated obligations within it on deployers of high-risk AI
    systems? (Single answer)
        • Yes (if yes, please elaborate on the steps taken to comply with deployer obligations)
        • No (if no, please explain)
        • I do not know
30. Does the AI Act address any of the challenges you highlighted above affecting the effective and efficient deployment of AI in
    healthcare? (Single answer)
        • Yes (Please specify)
        • No
        • I do not know
31. Do any of the deployer (user) obligations under the AI Act described above introduce new or additional challenges to hospitals?
        • Yes (Please specify)
        • No
        • I do not know
32. What additional support could be provided to hospitals to address the challenges introduced by the AI Act? (Free text)
33. Are you aware of the European Health Data Space? (Single answer)
        • Yes
        • No
34. Does the EHDS address any of the challenges you highlighted above affecting the effective and efficient deployment of artificial
    intelligence in healthcare? (Single answer)
        • Yes (Please specify)
        • No
        • I do not know
   35. In your opinion, what action could support healthcare institutions to efficiently and effectively deploy artificial intelligence tools
       in clinical practice?
           • Consolidated funding to support specific strategic priorities
           • Establishment of common standards on data governance, privacy, and interoperability
           • Ensure consistent access to public data and promoting open-data initiatives
           • Organisation and centralised collection of post-deployment data to monitor on the ongoing effectiveness of AI tools
           • Provide clarity on regulatory processes for product approval, accountability, and liability
           • Encourage the establishment of centres of excellence for AI in healthcare to concentrate talent and resources
           • Establish an EU AI in healthcare centre to coordinate and facilitate AI deployment
           • Redesigning workforce planning and clinical education to address future healthcare and AI professional needs, investing
                in upskilling frontline staff.
           • Development of platforms to facilitate dialogues and exchange of good practices to facilitate deployment of AI tools
           • Other (please specify)
           • I do not know
           • None of the above


10.2.4 AI Developer Survey



   1. Please indicate the number of employees in the organisation you work for. (Single answer)
          • Less than 250 employees
          • More than 250 employees
          • I do not know
          • Not applicable
   2. What are the top 3 challenges that hinder productivity, efficiency, and effectiveness in diagnosing, treating, and managing
       patients? (Free text)
   36. What are the current needs in your healthcare facility that existing artificial intelligence technologies have the potential to
       already address now? (multiple answer)
           • Optimizing resource allocation and workflow efficiency
           • Streamlining administrative tasks Improving diagnostic accuracy
           • Creating personalized treatment plans
           • Predictive analytics for patient outcomes
           • Improving patient engagement and adherence to treatment plans
           • Addressing skill gaps among the healthcare workforce
                                                                                         Deployment of AI in healthcare – Final Report


3. In your opinion, what are the needs in healthcare that artificial intelligence advances could address in the next 5 years (needs
    that cannot be addressed by existing artificial intelligence technologies)? (Free text)
28. In your opinion, to what extent do the following applications have the potential to provide concrete added value to the existing
    delivery of healthcare in your medical specialty?
    (Options: Large Extent, Moderate Extent, Small Extent, I do not know, Not applicable)
        • AI-assisted diagnostics
        • AI-assisted surgery/medical robotics to optimize surgical skills
        • AI-assisted remote patient monitoring
        • AI-assisted symptom checkers and support in treatment decisions (e.g. surgical indications, use and dosage of
             medications, and complication management)
        • Administrative support tool (e.g., EHR management, for clinical documentation)
        • Clinical workflow optimisation (e.g., predicting patient admissions, bed occupancy)
        • Conversational platforms for patient assistance (e.g., chatbots, virtual assistants)
        • AI-assisted prognosis prediction (risk stratification)
        • Other (please specify)
4. Have you developed or are you developing an artificial intelligence tool to be used in healthcare? (Single answer)
        • Yes (If yes, specify name, current state of deployment and countries deployed in)
        • No
        • Not applicable
5. For the tools you have developed and have already been deployed, do you offer any post-deployment assistance? (Single
    answer)
        • Yes (Please specify)
        • No
        • Not applicable
6. If applicable, what are the reasons why some of the artificial intelligence tools you developed have not yet been deployed in
    clinical practice? (multiple answer)
        • The AI tool is undergoing testing and validation to ensure its accuracy, reliability, and safety before deployment in real-
             world healthcare settings
        • The AI tool is undergoing regulatory approval processes
        • Limited access to high-quality healthcare data for training and testing the AI tool
        • Lack of interoperability and compatibility with electronic health records (EHRs), medical devices, and other existing IT
             infrastructure
        • Lack of funding or resources to support deployment
        • Unfavourable market conditions for effective deployment (e.g., waiting to identify suitable pilot sites or establishing
             partnerships with healthcare organisations before deploying the AI tool)
        • User concerns about usability, workflow integration, and training
      •     User concerns surrounding data privacy, liability, and patient consent
      •     Technical limitations related to scalability and computational resources required for effective deployment
      •     Considerations regarding the competitive market landscape (this includes evaluating the presence and performance of
            competing AI solutions, market demand, and strategic business decisions)
        • Other (please specify)
        • None of the above
        • Not applicable
7. Have you developed or are you developing generative AI tools to be used in healthcare? (Single answer)
        • Yes (Please specify)
        • No
        • Not applicable
8. Have you deployed a generative AI tool that you have developed in healthcare? (Single answer)
        • Yes
        • No
9. Based on your knowledge, to what extent do the following technological and data challenges impact the effective and
    efficient deployment of artificial intelligence tools in the healthcare facility within which you work?
    (For each option, impact was rated significant, moderate, no or I do not know. The responders were also asked for the
    relevance of the challenge for in house developed tools, commercially available tools or both)
        • Outdated IT infrastructure
        • Lack of interoperability of AI solutions with existing IT solutions
        • Lack of standardised data structures
        • Variations in performance across healthcare settings and populations
        • Quality concerns amongst end-users
        • Lack of transparency and explainability of AI tools
        • Lack of validation protocols for existing AI solutions
        • Other (Please specify)
10. Do these technological and data challenges differ between regions (e.g., between EU Member States, between EU countries and
    non-EU countries)? (Single answer)
        • Yes (please specify)
        • No
        • I don’t know
11. Based on your knowledge, to what extent did the following legal and regulatory challenges and barriers impact the
    effective and efficient deployment of artificial intelligence tools in the healthcare facility within which you work?
    (For each option, impact was rated significant, moderate, no or I do not know. The responders were also asked for the
    relevance of the challenge for in house developed tools, commercially available tools or both)
        • Lack of accountability and liability structure for errors by AI
                                                                                     Deployment of AI in healthcare – Final Report


        • Cybersecurity issues and vulnerability of data-to-data breaches
        • Complexity of regulatory approval process for AI product commercialisation
        • Lack of guidance on compliance of AI tools with current legislation
        • Concerns surrounding data privacy and data protection
        • Other (Please specify)
12. Based on your knowledge, to what extent did the following organizational and business challenges and barriers impact the
    effective and efficient deployment of artificial intelligence tools in the healthcare facility within which you work?
    (For each option, impact was rated significant, moderate, no or I do not know. The responders were also asked for the
    relevance of the challenge for in house developed tools, commercially available tools or both)
        • Lack of strategic direction to promote AI in healthcare
        • Lack of technological skills and knowledge amongst healthcare professionals to use AI tools effectively
        • Lack of involvement of end-users in the development, validation and deployment of AI tools
        • Lack of cost-benefit analysis of AI tools versus existing clinical solutions
        • Lack of funding, investment and financial incentives to deploy AI in clinical practice
        • Other (please specify)
13. Do these organisational and business challenges differ between regions (e.g., between EU Member States, between EU countries
    and non-EU countries)? (Single answer)
        • Yes (please specify)
        • No
        • I don’t know
14. Based on your knowledge, to what extent do the following social and cultural challenges and barriers impact the effective and
    efficient deployment of artificial intelligence tools in the healthcare facility within which you work?
    (For each option, impact was rated significant, moderate, no or I do not know. The responders were also asked for the
    relevance of the challenge for in house developed tools, commercially available tools or both)
        • Concerns among healthcare professionals on job security
        • Low level of digital health literacy among healthcare providers and the general public
        • Concerns about AI's impact on the personal relationship between doctor and patient
        • Concerns about patient autonomy and consent in the use of AI tools for their care
        • Lack of trust in AI tools
        • Concerns about skill shift to remain competitive in the job market
        • Concerns about overreliance on AI
        • Other (please specify)
15. Do these social and cultural challenges differ between regions (e.g., between EU Member States, between EU countries and
    non-EU countries)? (Single answer)
        • Yes (please specify)
        • No
        • I don’t know
16. Are there any other challenge and barriers not described above affecting the effective and efficient deployment of artificial
    intelligence in healthcare? (Single answer)
        • Yes (Please specify)
        • No
17. Do the challenges associated with deploying a generative artificial intelligence tool in healthcare differ from those of traditional
    AI tools?
        • Yes (Please specify)
        • No
        • I don’t know
18. To what extent do the following good practices addressing technological and data challenges contribute to the effective and
    efficient deployment of artificial intelligence in healthcare and clinical practice?
    For each option specify impact (significant, moderate, no, not applicable) and transferability of practice (highly transferable,
    moderately transferable, limited transferability, I do not know or not applicable)
        • Ensure that the training data used to develop the AI algorithms are diverse and representative of the population the
            model will serve
        • Generate explanations for AI model predictions
        • Develop AI tools with visualization tools for model inputs and outputs as well as case specific decisions
        • Develop and deploy low complexity models with sufficient performance
        • Train healthcare professionals to recognize model limitations, interpret confidence scores, visualize hidden layers as well
            as conduct sensitivity analyses to ensure they know how to interpret model decisions
19. To what extent do the following good practices addressing legal and regulatory challenges contribute to the effective and
    efficient deployment of artificial intelligence in healthcare and clinical practice?
    For each option specify impact (significant, moderate, no, not applicable) and transferability of practice (highly transferable,
    moderately transferable, limited transferability, I do not know or not applicable)
        • Conduct routine compliance audits to ensure adherence to regulatory requirements (e.g., HIPAA, GDPR)
        • Adopt a secure storage system to safeguard patient data and anonymization /encryption/de-identification techniques to
            block any unauthorized access and traceability.
        • Ensure secure data transfer protocols upon sharing data between systems to prevent interception, unauthorized access
        • Restrict access to authorized users
        • Utilize bias detection algorithms as well as bias mitigation techniques
        • Other (please specify)
20. To what extent do the following good practices addressing organisational and business challenges contribute to the effective and
    efficient deployment of artificial intelligence in healthcare and clinical practice?
    For each option specify impact (significant, moderate, no, not applicable) and transferability of practice (highly transferable,
    moderately transferable, limited transferability, I do not know or not applicable)
                                                                                              Deployment of AI in healthcare – Final Report


           •   Regular multidisciplinary clinician advisory boards to obtain user feedback, ensure the usability of the AI tools and their
               efficient integration into clinical practice, and look into areas for improvement
           • Involvement of end-users in the development and deployment of the AI tool
           • Conduct training programs for the healthcare professionals on the AI tools to be deployed.
           • Conduct analyses on the healthcare facility’s existing workflow to understand their process and accordingly redesign our
               AI tool to integrate seamlessly.
           • Ensure stakeholder engagement including healthcare professionals, administrators, and support staff.
           • Other (please specify)
    21. Are you aware of the EU AI Act? (Single answer)
           • Yes
           • No
    22. Are you prepared for the implementation of the AI Act and the associated obligations within it on developers of high-risk AI
        systems? (Single answer)
           • Yes (please specify
           • No (please specify)
           • Not applicable
           • I don’t know


10.2.5 Regulatory Expert Survey

    1. How familiar are you with the EU Regulatory landscape governing the use of AI? (Single answer)
           • Very familiar
           • Familiar
           • Not at all familiar
    2. Are you aware of the EU AI Act? (Single answer)
           • Yes
           • No
    3. To what extent do you believe the following challenges affecting the deployment of AI in healthcare addressed by the provisions
       of the AI Act? (Options: High extent, moderate extent, small extent, I do not know, not applicable)
           • Variations in performance across healthcare settings and populations
           • Quality concerns amongst end-users
           • Lack of transparency and explainability of AI tools
           • Lack of validation protocols for existing AI solutions
           • Lack of accountability and liability structure for errors by AI
           • Cybersecurity issues and vulnerability of data-to-data breaches
           • Complexity of regulatory approval process for AI product commercialisation
      • Lack of technological skills and knowledge amongst healthcare professionals to use AI tools effectively
      • Lack of human oversight over decisions made by AI-based tools.
      • Low level of digital health literacy among healthcare providers and the general public
      • Concerns about AI's impact on the personal relationship between doctor and patient
      • Concerns about patient autonomy and consent in the use of AI tools for their care
      • Lack of trust in AI tools
      • Concern about skills required of notified bodies to apply the AI Act.
4. Are there any other challenges affecting the deployment of AI in clinical practice, beyond the ones listed above? (Single answer)
      • Yes (Please specify)
      • No
      • I do not know
5. To what extent are these other challenges addressed by the provisions of the AI Act? (Single answer)
      • High extent
      • Moderate extent
      • Small extent
      • I do not know
      • Not applicable
6. Do you believe the current provisions of the EU AI Act adequately cover generative AI models used in healthcare? (Single
   answer)
      • Yes
      • No
      • I do not know

7. Are you aware of the Product Liability Directive (September 2022) (Single answer)
        • Yes
        • No
8. Considering that AI in healthcare might be used as stand-alone software that would be essentially providing information to the
    healthcare professional, how should the requirement of “causation” in a liability action under the proposed product liability
    directive (PLD) be interpreted in such cases? (Free text)
9. Are you aware of the Health Technology Assessment Regulation? (Single answer)
        • Yes
        • No
10. At which stage in the life cycle of a health technology would AI have the greatest potential to support joint work through
    evidence generation such as for horizon scanning of emerging health technologies, joint scientific consultations, joint clinical
    assessments, and post-marketing? (Free text)
11. Are you aware of the General Data Protection Regulation that came into force in the EU in 2018?
                                                                                          Deployment of AI in healthcare – Final Report


12. To what extent are concerns surrounding data privacy and data protection (e.g., Growing concerns about the privacy and
    security of healthcare data collected, processed, and shared by AI systems) addressed by the provisions of the GDPR?
        • High extent
        • Moderate extent
        • Small extent
        • I do not know
        • Not applicable
13. To what extent are concerns about patient autonomy and consent in the use of AI tools for their care (e. g., concerns arise
    regarding patients' ability to understand, control, and consent to the use of AI-driven technologies in their diagnosis, treatment,
    and decision-making processes) addressed by the provisions of the GDPR? (Single answer)
        • High extent
        • Moderate extent
        • Small extent
        • I do not know
        • Not applicable
14. To what extent do concerns about patients' rights (in terms of GDPR) in the use of AI tools for their care align with the
    provisions of the AI Act (for example, in terms of impact assessment, right to an explanation of individual decisions, exceptional
    authorization for processing sensitive data for detecting and correcting negative biases with specific conditions)? (Single
    answer)
        • High extent
        • Moderate extent
        • Small extent
        • I do not know
        • Not applicable
15. Are you aware of the MDR/IVDR? (Single answer)
        • Yes
        • No
16. To what extent does the MDR/IVDR address the barriers in deploying AI in clinical practice (consider how the requirements
    under these Regulations could be applicable for AI-based solutions in terms of health, safety, and innovation in practice)?
    (Single answer)
        • High extent
        • Moderate extent
        • Small extent
        • I do not know
        • Not applicable
17. Are there any gaps in the MDR/IVDR when it comes to AI-based tools used in clinical settings? (Single answer)
        • Yes (Please specify)
        • No
18. Are there any additional complementary actions (regulatory or non-regulatory) needed to ensure the safe and effective
    deployment of AI in clinical practice? (Free text)
19. Are there any additional complementary actions (regulatory or non-regulatory) needed to enhance trust, acceptability,
    transparency and explainability of AI in clinical practice with respect to deployment? (Free text)
20. Are there any additional complementary actions (regulatory or non-regulatory) needed to ensure equal access for patients to
    the use of AI in clinical practice? (Free text)
21. Are you aware of any actions (regulatory/non-regulatory) implemented at national level within the EU that could be considered
    as best practices for the effective deployment of AI in clinical practice? (Single answer)
        • Yes (Please specify)
        • No
22. Are you aware of any actions (regulatory/non-regulatory) implemented outside the EU that could be considered as best
    practices for the effective deployment of AI in clinical practice? (Single answer)
        • Yes (Please specify)
        • No
                                          Deployment of AI in healthcare – Final Report


    10.3 Annex 3 – Interview guides
10.3.1 Targeted interview questions for AI developers

1. What are the current needs in clinical practice that AI can address? Consider:

       a.   Healthcare workforce shortage
       b.   Ageing population and rise in chronic and complex conditions
       c.   Increased demand on healthcare services
       d.   Rising costs of healthcare
       e.   Inefficiencies within healthcare systems
       f.   Increase in administrative burden faced by healthcare professionals

2. How can AI tools you have developed or are developing help in addressing some of
   the needs described previously? Consider:

       a. How do you decide what AI tools you will develop? Do you work closely with
          healthcare professionals to make sure the tool you are developing is
          addressing an unmet need?

3. In which medical specialties and what types of applications will be used in the short-
   term (in the next 2 years)? Consider:

       a. Radiology and digital pathology
       b. Tools used for administrative purposes and diagnostic purposes

4. In which medical specialties and what types of AI applications will be used in the
   longer term? Consider:

       a. The potential of generative AI
       b. The applications of generative AI
       c. The challenges faced for generative AI solutions versus traditional machine-
          learning models
       d. What are the challenges related to the development of generative AI solutions
          to be used in healthcare settings? How do these challenges impact
          deployment?

5. Can you describe any AI tools deployed in clinical practice that excite you and you
   believe are having a significant impact on healthcare systems today? These can be
   AI solutions you have developed.

6. How do you see the AI landscape in healthcare evolving in the coming years?

7. From your experience, how easy is it to deploy AI solutions in clinical practice?

8. What is the impact or expected impact of the AI tools you have developed and
   deployed (or not yet developed or deployed)? Consider:

       a.   Impact on healthcare workforce working time
       b.   Reduction of administrative burden and lower rates of burnout and fatigue
       c.   Number of missed diagnoses avoided
       d.   Length of stay of patients
       e.   Time to treatment
       f.   Collaboration amongst healthcare professionals and multidisciplinary teams
       g.   Patient satisfaction and overall relationship between doctors and patients
       h.   Operational efficiency and waiting times
       i.   Costs on healthcare systems
9. How do you demonstrate the added value of AI solutions you developed versus
   existing clinical solutions? What metrics are used to assess added value? How do
   these metrics vary across different specialties and types of AI solutions? Consider
   the metrics described in Q4. Have you established a model to build a business-case
   for potential customers?

10. To what extent do technological and data challenges affect the deployment of AI
    solutions in clinical practice? Consider:

       a. Outdated IT infrastructure and lack of digitalisation (e.g., lack of EHRs, lack
          of cloud computing services)
       b. Lack of interoperability amongst existing IT solutions
       c. Lack of standardisation of data structures and data reporting requirements
       d. Poor quality of data
       e. Variations in performance across healthcare settings

11. What good practices have you employed to address technological and data
    challenges? Consider:

       a. Post-deployment monitoring mechanisms to assess performance in the given
          healthcare setting. What metrics are used to assess performance?
       b. Ensure generalisability within the specific healthcare setting
       c. Additional evaluations within specific healthcare settings to ensure the AI
          solution meets specific performance metrics and standards

12. To what extent do legal and regulatory challenges affect the deployment of AI
    solutions in clinical practice? Consider:

       a. The complexity of the regulatory approval process and lack of guidance on
          compliance of AI tools with existing legislation
       b. Concerns surrounding data privacy and data protection
       c. Cybersecurity issues and vulnerability of data to breaches
       d. Concerns regarding clinicians’ liability/standard of care issues when suing the
          AI tool
       e. Concerns regarding transparency and explainability of decisions made by AI
          solutions
       f. Concerns surrounding equity and digital divide caused by AI

13. What good practices have you employed to address legal and regulatory challenges?

14. To what extent do organisational and business challenges affect the deployment of
    AI solutions in clinical practice? Consider:

       a. Lack of strategic direction from the decision makers of healthcare facilities to
          promote innovation and the deployment of AI solutions
       b. Lack of technological skills and digital health literacy amongst healthcare
          professionals
       c. Lack of assessment of added value of AI solutions versus existing clinical
          solutions
       d. Lack of funding, investment and financial incentives

15. What good practices have you employed to address organisational and business
    challenges? Consider:

       a. Training and upskilling of healthcare workforce. Was this carried out by you?
          How was this carried out?
                                          Deployment of AI in healthcare – Final Report


16. To what extent do social and cultural challenges affect the deployment of AI solutions
    in clinical practice? Consider:

       a. Lack of trust in AI solutions from healthcare professionals and patients
       b. Concerns about the impact of AI solutions on the doctor-patient relationship
       c. Concerns about job security

17. What good practices have you employed to address social and cultural challenges?
    Consider:

       a. Education and training on how the AI systems are used
       b. Information material and/or explanations to be shared with patients
       c. Informing end-users (healthcare professionals) that the AI solution has
          undergone the relevant regulatory assessment and is CE marked/FDA
          approved
       d. Providing healthcare professionals with performance metrics within their
          healthcare setting and medical specialty
       e. Collaborations amongst the developers of the AI tools and those deploying
          and using it (e.g., healthcare professionals, hospital representatives,
          administrative staff). Have such collaborations been beneficial and why? Do
          such collaborations increase trust in AI solutions?

18. Are you aware of the EU AI Act and the various provisions published on the 12 th July
    in the Official Journal of the European Union? Does the EU AI Act introduce new
    challenges and obstacles to developers such as yourself?

19. To what extent do the provisions address some of the challenges described above?
    Consider:

       a.   Transparency and provision of information to deployers (Article 13)
       b.   Data protection impact assessment (Article 26)
       c.   Human oversight (Article 14)
       d.   Monitoring of performance (Article 26)
       e.   AI literacy (Article 4)

20. Why are the challenges described above not addressed by existing legal
    frameworks? Consider:

       a. GDPR in addressing data privacy concerns

21. Based on your knowledge, do the challenges described above differ across
    healthcare settings and regions? Consider:

       a. The deployment challenges in hospitals found in urban areas versus those in
          rural areas.
       b. Deployment in EU, USA, Israel, Japan

22. Based on your knowledge, to what extent are the good practices you employed
    transferable across healthcare settings and regions? Consider:

       a. Urban and rural areas
       b. Across the EU, USA, Israel etc.

23. How can the deployment of AI in clinical practice be scaled?

24. What complementary actions (regulatory/non-regulatory) are needed within the
    next 2-3 years to ensure the widespread deployment of AI tools in clinical practice?
    Consider:
      a. Consolidated funding to support specific strategic priorities.
      b. Ensure consistent access to public data and promoting open-data initiatives
      c. Organisation and centralised collection of post-deployment data to monitor
         on the ongoing effectiveness of AI tools. How would this work in your opinion?
         Would this be centralised at an EU level?
      d. Encourage the establishment of centres of excellence for AI in healthcare to
         concentrate talent and resources. How do you envisage such centres? How
         should they be established and structured to provide concrete benefits?
      e. Establish an EU AI in healthcare centre to coordinate and facilitate AI
         deployment. How do you envisage such centres? How should they be
         established and structured to provide concrete benefits?
      f. Redesigning workforce planning and clinical education to address future
         healthcare and AI professional needs, investing in upskilling frontline staff.
         How would this work in practice?
      g. Development of platforms to facilitate dialogues and exchange of good
         practices to facilitate deployment of AI tools
10.3.2 Targeted interview guide for HCPs and hospital representatives

1. What are the current needs in clinical practice that AI can address? Consider needs
   relevant to your work such as:
       a. Healthcare workforce shortage
       b. Ageing population and rise in chronic and complex conditions
       c. Increased demand on healthcare services
       d. Rising costs of healthcare
       e. Inefficiencies within healthcare systems
       f. Increase in administrative burden faced by healthcare professionals
       g. Need for improved screening, diagnosis and treatment
2. How could AI help in addressing some of the needs described previously?
3. In which medical specialties and what types of AI applications (within your specialty)
   will be used in the short-term (in the next 2 years)? Consider:
       a. Radiology and digital pathology
       b. Tools used for administrative purposes and diagnostic purposes
4. In which medical specialties and what types of AI applications will be used in the
   longer term? Consider:
       a. Precision medicine and clinical decision support systems
       b. The potential of generative AI
       c. The applications of generative AI
       d. The challenges faced for generative AI solutions versus traditional machine-
           learning models
5. Can you describe a few AI tools deployed in clinical practice (and within your
   specialty if applicable) that excite you and you believe are having a significant impact
   on efficiency and effectiveness of healthcare? Why are these tools effective?
6. What is the impact of these AI tools? Consider:
       a. Impact on healthcare workforce working time
       b. Reduction of administrative burden and lower rates of burnout and fatigue
       c. Number of missed diagnoses avoided
       d. Length of stay of patients
       e. Time to treatment
       f. Collaboration amongst healthcare professionals and multidisciplinary teams
       g. Patient satisfaction and overall relationship between doctors and patients
       h. Operational efficiency and waiting times
                                           Deployment of AI in healthcare – Final Report


        i. Costs on healthcare systems
7. Does the impact of the AI tool vary based on the healthcare setting? Why? Consider:
        a. Urban university hospital versus a hospital in a remote setting
        b. Existing clinical workflows and clinical guidelines
8. Given that there are many AI-based tools on the market today, how do you choose
    between solutions? Consider:
        a. Assessment of added value of AI-based solution versus existing clinical
           solutions. What metrics are used to assess added value? How do these
           metrics vary across different specialties and types of AI solutions? Consider
           the metrics described in Q4.
        b. The cost of the AI solution and potential reimbursement mechanisms.
        c. Assessment of whether the AI solution address a clear need highlighted by
           HCPs.
9. To what extent do technological and data challenges affect the deployment of AI
    solutions in clinical practice? Consider:
        a. Outdated IT infrastructure and lack of digitalisation (e.g., lack of EHRs)
        b. Lack of interoperability amongst existing IT solutions
        c. Lack of standardisation of data structures and data reporting requirements
        d. Poor quality of data
        e. Variations in performance across healthcare settings
10. What good practices have you employed to address technological and data
    challenges? Consider:
        a. Updating IT infrastructure and ensuring interoperability between systems and
           integration of AI-based solutions with EHR for seamless integration (e.g.,
           minimise the amount of software and applications to be used amongst the
           healthcare workforce)
        b. Post-deployment monitoring mechanisms to assess performance in the given
           healthcare setting. What metrics are used to assess performance? Does
           performance change over time?
        c. Establishment of clear data governance to address data related issues (use
           standardised formats for data reporting, data quality requirements)
11. To what extent do legal and regulatory challenges affect the deployment of AI
    solutions in clinical practice? Consider:
        a. The complexity of the regulatory approval process and lack of guidance on
           compliance of AI tools with existing legislation
        b. Concerns surrounding data privacy and data protection
        c. Cybersecurity issues and vulnerability of data to breaches
        d. Concerns regarding clinicians’ liability/standard of care issues when using the
           AI tool
        e. Concerns regarding transparency and explainability of decisions made by AI
           solutions
12. What good practices have you employed to address legal and regulatory challenges?
13. To what extent do organisational and business challenges affect the deployment of
    AI solutions in clinical practice? Consider:
        a. Lack of strategic direction from the decision makers of healthcare facilities to
           promote innovation and the deployment of AI solutions
        b. Lack of technological skills and digital health literacy amongst healthcare
           professionals
        c. Lack of assessment of added value of AI solutions versus existing clinical
           solutions
        d. Lack of funding, investment and financial incentives
14. What good practices have you employed to address organisational and business
    challenges? Consider:
        a. Training and upskilling of healthcare workforce. How was this carried out?
        b. Establishment of multidisciplinary teams which includes IT experts, data
             scientists, and/or data engineers to interpret and explain the decisions made
             by AI solutions
        c. Creating “AI champions” across different medical specialties to promote and
             encourage the healthcare professionals to use AI solutions.
        d. Establishment of an AI deployment strategy to increase adoption.
        e. Established models to assess added value and return-on-investment
15. To what extent do social and cultural challenges affect the deployment of AI solutions
    in clinical practice? Consider:
        a. Lack of trust in AI solutions from healthcare professionals and patients
        b. Concerns about the impact of AI solutions on the doctor-patient relationship
        c. Concerns about job security
16. What good practices have you employed to address social and cultural challenges?
    Consider:
        a. Education and training on how AI systems are used
        b. Information material and/or explanations to be shared with patients
        c. Informing end-users (healthcare professionals) that the AI solution has
             undergone the relevant regulatory assessment and is CE marked/FDA
             approved
        d. Providing healthcare professionals with performance metrics within their
             healthcare setting and medical specialty
        e. How do you enhance trust and acceptability of AI to your patients?
        f. How do you enhance trust and acceptability of AI to HCP?
        g. Collaborations amongst the developers of the AI tools and those deploying
             and using it (e.g., healthcare professionals, hospital representatives,
             administrative staff). Have such collaborations been beneficial and why? Do
             such collaborations increase trust in AI solutions?
17. Do you have any concerns surrounding equity and digital divide caused by AI? How
    can these be addressed?
18. Are you aware of the EU AI Act and the various provisions published on the 12 th July
    in the Official Journal of the European Union? Does the EU AI Act introduce new
    challenges and obstacles to deployers/hospitals/HCPs? Do you have any concerns?
    Consider:
        a. Article 26 – Obligations for deployers of high-risk AI systems:
                i.   Deployers of high-risk AI systems shall take appropriate technical and
                     organisational measures to ensure they use such systems in
                     accordance with the instructions for use accompanying the systems
               ii.   Deployers shall assign human oversight to natural persons who have
                     the necessary competence, training and authority, as well as the
                     necessary support.
              iii.   Deployers shall monitor the operation of the high-risk AI system on
                     the basis of the instructions for use and, where relevant, inform
                     providers
              iv.    Deployers of high-risk AI systems shall keep the logs automatically
                     generated by that high-risk AI system
                                          Deployment of AI in healthcare – Final Report


            v.     Before putting into service or using a high-risk AI system at the
                   workplace, deployers who are employers shall inform workers’
                   representatives and the affected workers that they will be subject to
                   the use of the high-risk AI system.
            vi.    Deployers of high-risk AI systems shall carry out a data protection
                   impact assessment
19. To what extent do the provisions address some of the challenges described above?
    Consider:
        a. Transparency and provision of information to deployers (Article 13)
        b. Data protection impact assessment (Article 26)
        c. Human oversight (Article 14)
        d. Monitoring of performance (Article 26)
        e. AI literacy (Article 4)
20. Why are the challenges described above not addressed by existing legal
    frameworks? Consider:
        a. GDPR in addressing data privacy concerns
21. Based on your knowledge, do the challenges described above differ across
    healthcare settings? Consider:
        a. The deployment challenges in hospitals found in urban areas versus those in
           rural areas.
22. Based on your knowledge, to what extent are the good practices you employed
    transferable across healthcare settings and regions? Consider:
        a. Urban and rural areas
        b. Across the EU, USA, Israel etc.
23. How can the deployment of AI in clinical practice be scaled?
24. What complementary actions (regulatory/non-regulatory) are needed within the
    next 2-3 years to ensure the widespread deployment of AI tools in clinical practice?
    Consider:
        a. Consolidated funding to support specific strategic priorities.
        b. Ensure consistent access to public data and promoting open-data initiatives
        c. Organisation and centralised collection of post-deployment data to monitor
           on the ongoing effectiveness of AI tools. How would this work in your opinion?
           Would this be centralised at an EU level?
        d. Encourage the establishment of centres of excellence for AI in healthcare to
           concentrate talent and resources. How do you envisage such centres? How
           should they be established and structured to provide concrete benefits?
        e. Establish an EU AI in healthcare centre to coordinate and facilitate AI
           deployment. How do you envisage such centres? How should they be
           established and structured to provide concrete benefits?
        f. Redesigning workforce planning and clinical education to address future
           healthcare and AI professional needs, investing in upskilling frontline staff.
           How would this work in practice?
        g. Development of platforms to facilitate dialogues and exchange of good
           practices to facilitate deployment of AI tools
10.3.3 Interview Guide - Case studies

The case study interview guides can be found in the table below. The case studies will
be submitted as a separate file.

                        Table 10: Case study interview questions
                                                                  AI       Hospital
                        Question                                                      HCPs
                                                               developer    reps.
 1. What needs in healthcare does the AI tool address?            X           X        X
 2. Did you face any of the following challenges when
    deploying the AI tool in clinical practice (if so
    please specify):

 - Technological and data challenges                              X           X
 - Legal and regulatory challenges
 - Organisational and business challenges
 - Social and cultural challenges


 3. Did these barriers and challenges differ across
    healthcare settings (e.g., urban versus rural)                X           X
    and/or regions (e.g., USA versus EU)?

 4. How did you address these barriers to ensure the
    AI tools is deployed in clinical practice in a way
    that is acceptable for and trusted by patients (e.g.,
    for hospital representatives - how has the hospital           X           X
    addressed any staff concerns or resistance to
    adoption of the AI tool) ?

 5. Can you describe any good practices to ensure the
    efficient and effective deployment of the AI tool in          X           X
    clinical practice? Why were these successful?

 6. How transferable/adaptable is this good practice
    across healthcare settings (e.g., urban versus                X           X
    rural) and regions (e.g., USA versus EU)?

 7. What are the specific challenges you face when
    interacting with the AI tool in clinical practice?                                 X

 8. How was the training process for using the AI tool
    conducted, and what were the challenges faced by
    healthcare professionals? What ongoing support                            X        X
    mechanisms are in place?

 9. To your knowledge, are there any challenges
    concerning clinicians’ lia ility/standard of care             X           X        X
    issues when using the AI tool in clinical practice?

 10. How does using      the   AI   tool   impact   clinical
     workflows?                                                               X        X

 11. How does using the AI tool impact the application
     of clinical guidelines?                                                  X        X

 12. How does using the AI tool impact the healthcare
     system overall?                                                          X        X

 13. How does using the AI tool impact the
                                                                              X        X
     collaboration amongst clinicians and healthcare
                                          Deployment of AI in healthcare – Final Report


   professionals? How has adoption of the AI tool
   changed over time?

14. How does using the AI tool impact the healthcare
    workforce working time?                                              X        X

15. How does using the AI tool impact the relationship
    between healthcare professionals and patients?                       X        X

16. How is deployment and the impact of the AI tool
    monitored? Do you use existing indicators, or have
    you developed new reporting or data collection                       X        X
    requirements?

17. To your knowledge, what are the specific
    challenges    surrounding     patient     specific
    concerns/hesitancy on using the AI tool in clinical                  X        X
    practice?

18. To your knowledge, what are the specific
    challenges surrounding transparency issues with           X          X        X
    the specific AI tool?

19. To your knowledge, are there any ethical issues of
    using the AI tool in clinical practice?                              X        X

20. What complementary actions (regulatory/non-
    regulatory) are needed within the next 2-3 years
    to ensure the safe and effective deployment of the
    AI tool in clinical practice providing concrete           X          X
    benefits to patients, healthcare professionals and
    healthcare systems?

21. What complementary actions are required to
    enhance trust, acceptability and explainability of
    AI in clinical practice? How will the introduction of     X          X        X
    the    Artificial  Intelligence   Act   impact   the
    deployment of AI in clinical practice?

22. What complementary actions are required to
    ensure equal access for patients to the use of AI in                 X        X
    clinical practice?

23. Are there existing collaborations between the
    developers of AI tools and those deploying the AI
    tool (e.g., healthcare professionals, hospitals) for
    the effective and efficient deployment of the AI          X          X        X
    tool in clinical practice (e.g., to understand their
    needs and challenges)? If not, would such
    collaborations be beneficial?

24. What are the main lessons learned from the
    deployment of the AI tool in clinical practice?           X          X        X
    10.4 Annex 4 – Synopsis report
 In the following sections, a summary of the findings from each of the consultation
activities for each of the key themes of the study is presented, clearly indicating who
said what, and end each section with a summary where the insights from the interviews,
surveys and workshops are brought together. The findings contained herein should be
reflected upon in careful consideration of the limitations of this study (section 2.5).

10.4.1 Current and future needs in clinical practice that AI can/will address

According to the survey responses from HCPs, hospital representatives, and AI
developers, the existing needs in healthcare affecting productivity and patient care
include administrative burden, healthcare workforce shortages, long waiting
times, and issues with digitalisation and interoperability. For HCPs, the biggest
concern is the growing administrative burden, with 53% of respondents indicating that
non-medical tasks (e.g., report writing, clinical documentation etc.) impacts their
productivity. On average, HCPs reported spending 20-60% of their time on
administrative tasks, such as clinical documentation, a figure that is consistent
between EU and international respondents, with averages of 41% and 47%,
respectively. According to 51 HCPs, existing AI solutions (“low-hanging fruit”) have the
potential to address some of these needs by optimising resource allocation and
workflow efficiency (73% of responses), streamlining administrative tasks (61%
of responses), and improving diagnostic accuracy (57% of responses).

Hospital representatives similarly highlighted the current needs in healthcare posed by
workforce shortages and growing administrative burden. Out of 35 respondents,
43% pointed to workforce shortages as the most important need, while 29%
emphasised the burden of administrative tasks and bureaucratic procedures. According
60% of the hospital representatives, HCPs within their healthcare facility spend
between 20-60% of their time on administrative tasks related to healthcare
provision, which are not strictly medical. Unlike HCPs, however, hospital
representatives placed more focus on the inadequacy of technology and IT infrastructure
within healthcare settings (26% of responses). Some of the healthcare needs described
above can already be addressed by existing AI solutions (“low-hanging fruit”) according
to the 35 hospital representatives. AI solutions can be used to optimise resource
allocation and improve workflow efficiency (83% of responses), improve
diagnostic accuracy (74% of responses), and streamline administrative tasks
(74% of responses).

 "The least risk and most acceptable AI-based solutions will likely be in medical billing, improving workflow
 efficiency in documentation, and in overall resource allocation optimization. These are unlikely to cause
 patient harm and more positioned to improve clinic operations and clinic finances, which are a significant
 motivator." – AI developer from the USA.




AI developers, while acknowledging similar healthcare needs to HCPs and hospital
representatives, provided more emphasis on technical and data-related needs. For AI
developers, the most important need is data access and quality, with 47% of
respondents pointing to issues with unstructured data, fragmented healthcare
systems, and poor data governance. Administrative burden and workforce shortages
were also mentioned by AI developers (28% and 17% of responses respectively), but
with less emphasis than seen among HCPs and hospital representatives. Some of the
healthcare needs described above can already be addressed by existing AI solutions
(“low-hanging fruit”) according to the 36 AI developers/AI developer associations that
responded. AI solutions can be used for predictive analytics for patient outcomes (26
                                                 Deployment of AI in healthcare – Final Report


responses), improving diagnostic accuracy (72% of responses), and streamlining
administrative tasks (72% of responses).
Figure 19: Healthcare needs that can already be addressed by existing AI solutions according
to HCPs, Hospital representatives, and AI developers
                                HCPs         Hospitals            Developers


                                        Optimizing resource
                                          allocation and
                                        workflow efficiency
                                                       83%
                                           73%
             Ensuring equitable                               74%        Streamlining
            access to healthcare           61%                        administrative tasks

                                                                     72%
                                      33%
                                                 34% 61%
                                   42%
                                                                         74%
    Addressing skill gaps
                                 41%                      61%                Improving diagnostic
    among the healthcare                    37%                                   accuracy
         workforce
                               56%          43%                          72%
                                                 43%      27%
                                 43%
                                                                   60%
               Improving patient     53%         47%
                engagement and                             61%        Creating personalized
                  adherence to                                           treatment plans
                treatment plans                  72%

                                       Predictive analytics for
                                          patient outcomes




When asked about future needs in healthcare that cannot be addressed by existing AI
technologies but could be addressed within the next 5 years (“high-hanging fruit”), there
was consensus among all stakeholder groups that AI advancements could drive
personalised medicine, real-time decision-making, and predictive healthcare.
All stakeholders believe AI has the potential to improve personalised patient care by
tailoring treatment plans based on individual patient data, including genetic profiles.

From the interviews the most common challenges highlighted by 7 HCPs 336, 2 hospital
representatives337 and an EU-level association centred around the need to alleviate the
administrative burden faced by HCPs and the excessive time spent on documentation,
scheduling, and organisational/operational tasks. One HCP from Italy along with the AI
developers from the Netherlands also pointed to challenges with operational
efficiency that AI could help address by, for example, speeding up and increasing the
efficiency of diagnosing and triaging of patients.

All stakeholder groups interviewed agreed that there is a need and potential for AI to
improve screening, diagnosis and treatment as HCPs from the Netherlands, Spain
the UK emphasised that they are facing an increased demand for diagnostics,
particularly in the medical specialties of radiology and pathology. Four HCPs 338, two
hospital representatives339, four AI developers340 and the EU-level association also

336 HCPs from Spain, Denmark, one from the UK, four from the USA
337 Hospital representatives from Japan and Belgium
338 Three HCPs from the UK, one from Denmark
339 Hospital representative from Japan and the USA
340 AI developers from the Netherlands, Germany, Japan, and the USA
mentioned workforce shortages as an issue that AI tools can help mitigate. For
example, three hospital representatives from the UK explained that in radiology, AI has
the potential to ease workload by identifying normal cases with a higher accuracy,
especially in centres handling high volumes of scans where the majority are normal,
requiring only radiologist to review the findings of the AI solution. AI developers from
the US and the HCP from the Netherlands believe that AI has the potential to aid in
precision diagnostics by identifying medical patterns that are too complex or subtle
for the human brain to fully comprehend.

In the hospital workshop, hospital representatives provided further insights into the
needs AI could address. A hospital representative from the USA described their approach
of running internal innovation competitions, where clinicians apply highlighting a
clinical need within their medical specialty that can potentially be addressed by AI
solutions. In the latest round, over 300 applications were submitted across different
medical specialties, with needs ranging from staffing shortages to early disease
detection. A hospital representative from Italy highlighted the need for AI systems
that optimise entire hospital processes for sustainability and efficiency,
focusing on resource management rather than isolated, single-point solutions within
diagnostics or therapy. These needs closely mirror the survey and interview findings,
focusing on alleviating administrative burden, workforce shortages, and
improving technological infrastructure

10.4.2 Impact of AI in clinical practice

The survey responses from patients, patient associations, HCPs, and HCP associations
with advanced or solid knowledge of AI in healthcare provide a comparative perspective
on the anticipated impact of AI in healthcare settings over the coming years. Both
stakeholder groups—patients and HCPs—believe that AI will have a positive impact,
particularly in improving diagnosis speed and accuracy as well as in managing chronic
conditions through remote monitoring and proactive interventions.

From the patient perspective, 70% of the patients indicated that AI would have a
positive impact across all areas. Among these areas, respondents highlighted the
potential for AI to significantly improve the speed and accuracy of medical
diagnoses (70% responses) and enhance chronic condition management (55% of
responses), particularly through remote patient monitoring. Patients also highlighted
several broader impacts, including improved doctor-patient interactions, reduced
administrative burdens on HCPs, and enhanced education and training for HCPs. These
factors suggest that patients expect AI to not only improve direct healthcare outcomes
but also to improve the experience and quality of care by improving efficiency
and communication between HCPs and patients.

The responses from HCPs (32 responses) align closely with the patient group in terms
of their positive outlook on AI’s future impact. Over 65% of HCPs indicated that AI would
have a positive effect across most areas, with the greatest improvements expected in
diagnostic accuracy and chronic condition management, where 91% of
respondents believe that AI will have an important impact. However, HCPs were
sceptical that adoption of AI tools would lead to cost savings in healthcare (28% of
respondents indicating that AI adoption will have no impact on cost saving on healthcare
expenses).

From the interviews, HCPs had a positive outlook towards the use of AI to improve
healthcare workforce well-being, working time and workload. In the field of
radiology, HCPs from the UK and Austria noted that AI automation allows for one
radiologist to verify results rather than two, saving time and improving the overall
                                                   Deployment of AI in healthcare – Final Report


efficiency of the clinical workflow. Similarly, HCPs from the USA and Denmark
highlighted that AI could improve work-life balance and efficiency, with tools like AI-
generated discharge letters and EHR-integrated systems easing administrative
tasks. The hospital representative from Japan described two AI solutions currently
deployed in their hospital to assist with administrative documentation. Similarly, a
hospital representative from the USA highlighted the benefits of using EHR vendors that
incorporate AI solutions within their platform to streamline administrative tasks, such
as virtual scribes and organising messages for easier management. On the other hand,
one HCP from the UK believed that some AI technologies do not provide added
value in clinical settings, with many tools, particularly in radiology often being
“solutions looking for a problem”.

HCPs, hospital representatives and AI developers all agreed on the benefits that AI has
in improving operational efficiency and care delivery. A hospital representative
from South Korea and two HCPs from the UK reflected on its ability to improve
detection efficiency, thereby shortening waiting time. One HCP from the UK
stated that tools that focus on narrow, well-defined tasks have the greatest positive
effect because their use minimises disruptions elsewhere in the healthcare system. AI
tools that speed up diagnosis were mentioned by the AI developer from the
Netherlands and an HCP from Spain.

HCPs341, hospital representatives342 and AI developers343 generally agreed on the
transformative potential of AI tools in enhancing diagnostic accuracy across a
number of medical fields, such as lung cancer screening, breast cancer pathology,
and rare disease identification. One HCP from the UK highlighted AI's ability to
improve efficiency in cancer detection when used alongside human reviewers. However,
the hospital representative from Japan raised concerns that AI could also
potentially increase workload due to the need for radiologists to review false
positives. The hospital representative from Japan, HCPs 344, the EU-level organisation
and one AI developer from the USA agreed on the positive impact of AI tools in
enhancing doctor-patient relationships345. They noted that AI solutions, for
example chatbots, provide layman-friendly explanations of diagnoses and medical
decisions, which improves patient understanding and satisfaction. One HCP from the UK
and one HCP from the USA also attributed financial benefits to AI, especially in
settings where it is used for early detection, thereby reducing the cost of treatment.
Two HCPs from the USA, one HCP from Austria, one HCP from the Netherlands, and an
HCP from the UK believed that AI tools have the potential to democratise healthcare
as well as provide high-quality diagnostics in rural settings. This would allow for
the maintenance of consistent care quality across regions.

In the workshop, hospital representatives from Israel highlighted the positive impact
generative AI tools could have on hospital administration, back-office functions,
and operational efficiency. However, they stressed the importance of deploying,
controlling, and monitoring these tools centrally within hospitals to ensure their
effectiveness.




341 Healthcare professionals from the Netherlands, one from UK, one from Italy, one from the USA
342 Hospital representative from USA and Japan
343 AI developer from Germany, Japan, one from US
344 One healthcare professional from Italy, one healthcare professional from the UK
345 A reflection also provided by patients and patient associations in the survey (described above)
10.4.3 Areas where the use of AI has the greatest transformative potential

In this section, stakeholders’ views on the areas where the use of AI is expected to have
the greatest transformative potential in healthcare are presented. The analysis focuses
on two key questions:

   •    Which medical specialties have the biggest potential for AI-driven
        transformation, as identified by hospital representatives.
    • The specific AI applications that are expected to provide significant added value
        to healthcare delivery, as assessed by all stakeholder groups.
The survey responses from patients, HCPs, hospital representatives, and AI developers
offer distinct yet overlapping perspectives on the use of AI in healthcare, particularly
around comfort levels, transformative potential, and areas of concern. From the
patient’s perspective, 63% of the patients reported feeling generally comfortable with
AI in healthcare, mostly in areas that indirectly affect their care, such as support with
administrative tasks (83% of responses) and optimisation with clinical workflows
(70% of responses). However, patients expressed discomfort with the use of AI in
conversational platforms, such as chatbots for direct patient assistance, with only
43% of respondents feeling comfortable. However, patients raised concerns about
potential negative impacts. Key issues included bias in AI algorithms leading to
disparities (63% of responses), fear of loss of the human touch in healthcare
(60% of responses), concerns about patient privacy and data security (57% of
responses), and a perceived lack of regulation and oversight (53% of responses).

The responses from HCPs, based on 51 respondents, align closely with the patient group
in terms of their positive outlook on AI's potential role in supporting administrative
tasks and clinical workflow optimisation. Over 70% of respondents believe AI tools
for managing tasks like electronic health records and clinical documentation will
have the greatest impact on healthcare delivery. However, only 20% of respondents
believe AI-assisted surgery or medical robotics will add much value, reflecting a
cautious view on these more complex AI applications. The HCPs highlighted, however,
for AI to have an impact, better access to quality data, which includes diverse patient
populations, and system interoperability is required.

Hospital representatives (32 respondents) aligned with HCPs in their views on AI’s
potential in healthcare. Over 87% of respondents believe administrative support
tools, such as AI systems for EHR management, will have the most transformative
impact on healthcare delivery, with 65% of respondents highlighting AI-driven clinical
workflow optimisation as another area of value. Interestingly, hospital
representatives were also sceptical about the potential of AI-assisted surgery, with
less than 30% of respondents seeing much value in its implementation. One key area
where hospital representatives see the most transformative potential is in radiology,
indicated by 94% of respondents.

AI developers and researchers (36 respondents) offered a different perspective. Over
70% of respondents believe AI-assisted diagnostics will have the most
transformative potential, followed by AI-assisted prognosis prediction (64% of
respondents). Like HCPs and hospital representatives, AI developers are less
enthusiastic about the potential of AI-assisted surgery, with only 30% of respondents
viewing it as adding value.
                                                    Deployment of AI in healthcare – Final Report




 “AI has the potential to significantly enhance the delivery of healthcare in our medical specialty. By
 leveraging AI-assisted diagnostics, we can achieve more accurate and timely diagnoses, which is critical
 for effective patient treatment. AI-assisted surgery and medical robotics can optimise surgical outcomes,
 reducing recovery times and improving patient prognosis. Remote patient monitoring via AI can ensure
 continuous care, especially for chronic conditions, while AI-powered predictive maintenance ensures all
 medical equipment operates optimally. Additionally, AI-driven personalised patient education and mental
 health support tools can provide tailored and accessible care, further improving patient engagement and
 adherence to treatment plans. These applications collectively contribute to a more efficient, effective, and
 patient-centred healthcare delivery system.”

 - Hospital representative from Portugal.



Figure 20: Areas where the use of AI is expected to have the most transformative potential
according to HCPs, hospital representatives, and AI developers.
                                    HCP          Hospital          Developers



                                          Administrative support
                                                   tool
                                                         88%
                 AI-assisted
                                              71%
               surgery/medical                                           Clinical workflow
             robotics to optimize                               66%         optimisation
                surgical skills
                                                     61%            59%
                                         28%
                                        25%              44%
                                                                        59%
    AI-assisted prognosis                         20%
                                                              57%
       prediction (risk   64%                   35%                              AI-assisted diagnostics
        stratification)     47%                 37% 28%                     78%
                                                   37%
                                     42%                            44%
                                                               47%
               Conversational             56%                             AI-assisted symptom
            platforms for patient                         64%             checkers and support
                  assistance                     66%                     in treatment decisions

                                            AI-assisted remote
                                            patient monitoring




In the short-term, the stakeholders participating in the interviews identified
radiology and pathology as the medical specialties with the greatest potential for
transformation, while clinical decision support along with general administrative
support were highlighted as other key areas. Due to their potential to enhance
diagnostic efficiency, the transformative potential of AI tools in radiology, medical
imaging and digital pathology was highlighted by HCPs346, AI developers347, a
hospital representative from Belgium and the EU-level organisation. One HCP from Italy
noted that department-specific AI tools are likely to see the most widespread adoption
due to a mature market, with capabilities to reduce diagnosis times and prioritise urgent
cases in the Emergency Room. While the HCP from Denmark acknowledged the benefits
of AI-assisted diagnostics, they also cautioned that such tools may struggle to
perform outside of their trained niches. Similarly, one HCP from Italy believed that


346 Healthcare professional from the Netherlands, one from the UK, one from the USA
347 The AI developer from Germany, one from the US
the value of AI tools that focus on diagnostic or therapeutic improvements is often
difficult to quantify because they bring limited improvement in the overall quality of
care.

The HCP from the Netherlands believed that the greatest transformative potential
is expected in patients with metastatic or advanced-stage tumours, where AI-based
clinical decision support tools can predict treatment responses for costly
therapies. One HCP from the USA, on the other hand, highlighted AI's transformative
potential in early detection and intervention for cancers (e.g., pancreatic, prostate,
breast), improving risk assessment and reducing the need for invasive procedures. The
AI developer from Germany and the EU-level organisation agreed on the significance of
decision-support tools, with the EU organisation also pointing out AI’s potential to
generate systematic reviews, thereby strengthening the evidence base for medical
associations.

The hospital representative from South Korea explained that there is a lot of focus on
the use of AI tools that improve operational efficiency such as those suggesting
interventions for critically ill patients and continuously monitoring vital signs to predict
patient outcomes. The HCP from Denmark reflected on the potential for AI tools in
improving surgical operations, for example by predicting capacity, while one
healthcare professional from the UK noted that AI currently excels in binary diagnostic
tasks, like fracture detection, but faces challenges with more complex diagnoses,
such as identifying cancer in lung scans.

Three HCPs348, two AI developers349 and two hospital representatives350 reflected on the
application of AI tools to improve administrative efficiency and streamline non-
clinical tasks, for example summarisation tasks with the use of generative AI. One HCP
from the USA explained that generative AI also has the potential to provide operational
support for rural areas in streamlining patient workflows.

In the long-term, one HCP from the UK and one HCP from Denmark stated that they
expect digital pathology to be the next medical specialty to experience transformative
AI potential, after radiology.

In terms of application, one AI developer from the USA and two HCPs 351 expressed
optimism about the future of general-purpose AI tools such as Large Language
Models (LLMs). These tools could be used for example, to analyse population health
data, streamline workflows in areas like surgical planning and medication logistics as
well as measure the psychological well-being of healthcare professionals to prevent
burnout. The hospital representative from the USA noted that current AI tools are
primarily focused on point solutions for specific needs but also envision the application
of general-purpose AI tools to provide comprehensive system-wide support in the
future. The AI developer from Japan, one HCP from the UK and one HCP from the USA
reflected that generative AI models may hold significant potential. Nevertheless,
the HCP from the UK reflected that they currently require clinicians to verify the AI's
outputs, limiting immediate time savings. The hospital representative from Japan and
the HCP from Denmark, however, believed that AI-driven chatbots can help mitigate
the scarcity of HCPs as well as avoid patients paying high-costs for visits.
Hospital representatives from Japan, South Korea and Belgium also referenced the
potential for AI in genomics.



348 HCPs from the US, Germany and one from the UK, one from Denmark
349 AI developer from Japan, one from USA
350 Hospital representative from the Netherlands and the USA
351 One healthcare professional from Italy and one from the UK, one from the USA
                                           Deployment of AI in healthcare – Final Report


In the hospital workshop, the hospital representatives provided more specific insights
into the types of AI applications. A hospital representative from the USA highlighted
that AI tools for organisational and administrative tasks are the "low-hanging
fruit" for achieving quick, measurable benefits in hospital settings. Similarly, a hospital
representative from Israel noted that generative AI assisting HCPs in non-clinical
settings, such as hospital administration, back-office functions, patient
communication bots, and scheduling, can add value.

In terms of medical specialties, the hospital representative from the USA identified
radiology as an early adopter due to the availability of vast amounts of data that
have been aggregated over decades, along with the nature of the work that is closely
tied to imaging technology. According to the representative, cardiology is the second
medical specialty to follow in early adoption, and behavioural health, psychology,
and psychiatry were viewed as slower adopters of AI tools.

10.4.4 State of deployment of AI in healthcare

The survey results from hospital representatives, and AI developers highlight varied
experiences and challenges with AI deployment in healthcare settings, focusing on the
practical deployment of AI tools, including generative AI, across these stakeholder
groups.

Of the hospital respondents (35 respondents), 20 are currently piloting an AI solution,
19 have already purchased and deployed a commercially available solution, and 11 have
developed and deployed an in-house AI solution. Only two hospitals have not yet
adopted AI. However, challenges in deployment persist, particularly with
interoperability issues between AI tools and existing infrastructure like EHRs
and medical devices, which 17 respondents highlighted as an important barrier. Other
challenges include the ongoing testing and performance testing of AI tools for
accuracy and safety (16 responses) and a lack of funding to support deployment
(15 responses). While 43% of respondents believe commercially available AI tools
facilitate more seamless integration into clinical workflows, 20% see no difference
between in-house and commercially available solutions. Among those hospitals that
have deployed AI tools, only a minority track specific performance or efficiency metrics,
highlighting a need for more structured evaluation of AI’s impact on healthcare delivery.

AI developers and researchers (36 respondents) present a more technical perspective,
as 25 of them have developed or are developing AI tools for healthcare use, with all
international respondents but only 16 EU respondents actively involved in AI tool
development. A reason some AI tools have not yet been deployed is regulatory approval
and the need for thorough testing and performance testing to ensure the tools'
safety and reliability, echoing the concerns raised by hospital representatives.
Another key issue, highlighted by an AI developer from the USA, is the fragmented
data landscape in Europe, which complicates scalable solutions and necessitates
extensive contracting. Post-deployment, AI developers provide significant support,
including routine communication, training, implementation support, system
monitoring, and ensuring legal compliance. This support is important to ensuring
the tools’ continued effectiveness and integration into healthcare systems. When it
comes to generative AI, 18 out of the 36 developers are involved in the development of
such tools, with 8 having deployed generative AI tools in clinical practice.
10.4.5 Challenges and accelerators to AI deployment in healthcare

10.4.5.1 Technological and data challenges and good practices

The survey results highlighted several technological and data challenges impacting the
deployment of AI in healthcare (Figure 21). Although all groups recognize similar
challenges, their emphasis and proposed solutions differ based on their specific roles
within the AI ecosystem. The technological and data challenge believed to have the
most significant impact on deployment of AI solutions according to all stakeholder
groups is the lack of standardised data structures. Among HCPs, 61% respondents
identified data fragmentation as an important challenge, as healthcare systems often
use isolated or proprietary platforms with inconsistent data formats. This lack of
standardization hinders AI's ability to analyse and aggregate data effectively across
various systems. Hospital representatives concurred, with 62% of respondents pointing
to the absence of uniform data models as a barrier to AI integration, particularly when
working with external institutions that do not follow the same standards. AI developers
also highlighted the importance of standardised data structures, with 71%
of respondents indicating that the lack of uniform standards across regions, especially
in Europe, complicates AI deployment.
Figure 21: Technological and data challenges believed to have a significant impact on the
deployment of AI tools according to 26 hospital representatives, 49 HCPs, and 34 AI
developers


         Lack of standardised data structures       62%       61%          71%

  Lack of interoperability of AI solutions with
                                                     68%      49%          74%
              existing IT solutions

                   Outdated IT infrastructure        68%         59%       53%

   Lack of validation protocols for existing AI
                                                  39%      55%       56%
                    solutions

 Lack of transparency and explainability of AI
                                                    58%     41%      38%
                    tools

         Quality concerns amongst end-users         46%    37% 38%

 Variations in performance across healthcare
                                                  32% 37% 38%
           settings and populations


                                 Hospital     HCP    AI developers


Interoperability of AI solutions with existing IT systems is another key challenge
shared by all three stakeholder groups. Among HCPs, 49% of respondents highlighted
the difficulty AI tools face in integrating with existing healthcare systems such as EHR
platforms, forcing manual data input and creating workflow inefficiencies. Hospital
representatives agreed, with 68% of respondents emphasising that without seamless
integration, AI systems disrupt clinical workflows, increasing operational complexity
and reducing user adoption. AI developers also highlighted this issue, with 74%
of respondents reporting that the fragmented nature of hospital IT systems, even within
the same institution, is a major barrier to scaling AI tools across different healthcare
settings.
                                               Deployment of AI in healthcare – Final Report


 “The lack of interoperability of AI solutions with existing IT solutions is the single most common
 challenge cited by customers. Transferring data from system to system is highly tedious,
 laborious, and can bring mistakes too easily.” – AI developer from the USA.


Another area of convergence between stakeholder groups is outdated IT
infrastructure. Among HCPs and their associations, 59% of respondents indicated that
outdated IT systems are a major barrier to effective AI deployment. Many healthcare
facilities still operate with technology that cannot handle the large datasets and complex
computations required for AI, leading to inefficiencies, higher costs, and limited
scalability of AI applications. Hospital representatives echoed this concern, with 68%
of respondents indicating that outdated infrastructure is a significant issue, especially in
Europe where hospitals in rural or underfunded regions face even greater
challenges in updating their systems. Similarly, 53% of AI developers reported that
outdated IT infrastructure, including legacy systems like EHRs, complicates AI
deployment due to poor interoperability with modern tools.

 “The deployment of AI tools requires a base level of digital and physical infrastructure to be
 effective. However, many hospitals in Europe still have limited digitalisation requiring more
 investment in basic digital and physical infrastructure prior to deploying AI tools. Indeed,
 physical infrastructure is also essential for supporting AI, making sure that digital services are
 dependable, safe, and accessible to healthcare professionals in each hospital.” – Hospital
 representative association based in Belgium.


While these challenges are universally recognised, there are also key differences in how
the stakeholder groups perceive and prioritise certain issues. HCPs expressed
considerable concern about the lack of clear performance testing procedures for
AI tools to assess variations in performance across healthcare settings, with 55%
of respondents raising this issue. Many HCPs are sceptical about the reliability of AI,
particularly due to the "black box" nature of many systems, which makes it difficult to
understand how decisions are made. Without transparent and standardised performance
testing processes, HCPs lack trust in AI-driven clinical decisions. Hospital
representatives also raised concerns about performance testing, though their focus was
more on pilot studies and testing AI systems within their specific infrastructure to
ensure safety and efficacy before full deployment. In addition, 56% of AI developers
reported that the lack of standardised performance testing protocols impacts AI
adoption, particularly for teams with less experience. The absence of consistent
frameworks leads to uncertainty about AI reliability, especially when integrating these
tools into clinical workflows.

Explainability and trust in AI present another point of divergence. HCPs emphasised
the need for transparency in AI decision-making, as the inability to understand how AI
models arrive at their conclusions can undermine trust, especially in high-stakes clinical
environments. Some international respondents further stressed that clear, concise
guidelines on how AI models work are essential for improving transparency and building
confidence among users. However, hospital representatives did not prioritise
explainability to the same degree, focusing instead on ensuring the AI system's
performance within their workflows. For AI developers, explainability was recognised as
important but secondary to data quality and performance . Many developers believe
that while transparency is essential in some contexts, AI performance and ease of use
are more important for gaining clinician trust.

In terms of addressing these challenges, there is convergence on several good practices.
One such practice is post-deployment monitoring and performance assessment.
Among HCPs, 84% of respondents highlighted the importance of real-time monitoring
to ensure that AI systems perform effectively in diverse clinical settings. This includes
continuous assessments and adjustments based on AI performance data and user
feedback. Hospital representatives similarly highlighted the importance of monitoring AI
systems post-deployment, often by collaborating with AI developers to implement
performance tracking mechanisms. AI developers also agreed, with 49% of respondents
highlighting that monitoring AI performance after deployment is crucial, particularly for
ensuring that AI models remain fair and effective across different patient populations.

Another area of agreement is the need for training AI models on diverse datasets.
Among HCPs, 80% of respondents emphasised the importance of training on diverse
datasets to ensure that AI systems account for variations in patient demographics
and clinical environments. Hospital representatives also recognised this need,
indicating that AI models must be tested in different real-world settings to avoid
performance biases. AI developers concurred, with 79% of respondents indicating that
ensuring training data diversity is critical for developing AI models that can generalise
effectively across different populations and healthcare systems.

The main challenges highlighted by the interviewees were related to data
accessibility, quality and standardisation, insufficient IT infrastructure and the
lack of interoperability. A lack of standardisation in data structures (for example
between EHR systems), including the absence of a common language was highlighted
by three HCPs352 along with hospital representatives353 and AI developers 354.
Additionally, four HCPs355, the hospital representative from Japan and four AI
developers356 highlighted significant challenges related to data quality and access,
which can be inaccurate or incomplete. One AI developer from the USA noted the overall
limited availability of digitised data in the EU, which another AI developer from the USA
believes is also due to the absence of secure cloud solutions. Two AI developers from
the USA and one HCP from the UK highlighted concerns from hospitals when it comes
to the applicability of AI models to their diverse patient populations.

Insufficient or outdated IT infrastructures pose major challenges to the
deployment of AI in healthcare according to six HCPs 357, the hospital representative
from South Korea and one AI developer from the USA. For example, five HCPs 358 and
two the hospital representatives359 explained that interoperability issues can arise
due to varying digital maturity within healthcare centres that lack foundational
systems such as EHR. Additionally, one HCP from Italy pointed out that some hospitals
are not aware of the infrastructure requirements they should have in place, resulting in
improper deployment of AI solutions. Additionally, issues with seamless integration
were mentioned by one HCP form Denmark and one AI developer from the USA,
highlighting the necessity to integrate solutions into a single platform. Furthermore,
barriers due to preferences in Europe for on-premises AI systems over cloud
solution was mentioned by one AI developer from the USA. One HCP from Denmark
and the hospital representative from the USA agreed, highlighting a reluctance to
transition to cloud-based solutions among hospitals due to concerns surrounding data
privacy. Similarly, three AI developers from the USA as well as the hospital


352 HCPs from Austria, three from the USA, one from the UK
353 One hospital representative from Italy and one from the USA
354 AI developer from Japan, one from the USA
355 HCPs from the Netherlands, one from Italy, two from USA
356 AI developer from Germany, three from the USA
357 HCPs from the Netherlands, the US, one from Denmark, one from Italy
358 One HCP from the USA, three form the UK, one from Italy
359 The hospital representative from Japan and Belgium
                                           Deployment of AI in healthcare – Final Report


representative from South Korea explained that many hospitals are still using on-
premises systems which poses challenges for integration.

In terms of best practices to mitigate the abovementioned challenges, one AI developer
from the USA explained that they conduct site assessments for data quality prior to
deployment. Additionally, post-deployment monitoring is carried out by one HCP
from the UK and two AI developers from the USA, to be able to flag when the algorithm
does not work as well in a given population. Additionally, one HCP from the UK explained
they continually test AI systems against historical data. To collect accurate and
representative data, one AI developer from the USA, one HCP from Denmark, one
HCP from the UK and the EU-level HCP organisation stressed the importance of
facilitating collaborative data infrastructures for effective AI application in healthcare.
For example, one AI developer from the USA establishes partnerships with clinical
healthcare centres and research institutes, while one HCP from Denmark highlighted
ongoing discussions to establish a central entity for data collection and storage.
The EU-level HCP organisation highlighted a single platform where data science teams
in urology will be able to analyse high-quality and anonymised data.

To ease the challenges stemming from interoperability, investing in IT systems prior
to adoption was stressed by the hospital representatives from Italy, one HCP from the
USA and one HCP from the UK with pilot testing AI systems. Additionally, the hospital
representative from South Korea and one HCP from the UK monitor and upgrade
their AI algorithms alongside their hospital technologies to better facilitate AI
adoption and maintain accuracy post-deployment. One AI developer from the
Netherlands along with one HCP from the USA also conduct rigorous post-deployment
assessment to monitor for performance and effectiveness. Adopting cloud-based
solutions for scaling and securely deploying AI solutions was emphasised by one AI
developer form the USA, one HCP from the UK and the hospital representative from
South Korea. One AI developer from the USA explained that cloud systems facilitate
data sharing and enable post-deployment monitoring as well as help overcome any
limitations with on-premises data storage.

In terms of the hospital workshop, the hospital representatives described several
technological and data challenges specific to different regions. One hospital
representative from Israel raised concerns over variation in AI performance due to
differences in healthcare professionals’ preferences, workflows, and the types of cases
handled (inpatients versus outpatients). The other hospital representative from Israel
echoed this challenge adding that each model behaves differently in different realities
which, in absence of standardised methods to extract hospital specific value from
performance profiles and the literature, means piloting is the only option.

A common challenge reported by hospital representatives from Israel and Italy was the
fragmentation of AI tools and vendors, which makes piloting every available
solution and determining which one would work best in specific hospital settings difficult.
A hospital representative from the USA added that vendors provided varying levels of
post-deployment monitoring, with some offering none. Moreover, this representative
raised concerns surrounding validation and accuracy, highlighting that the main
challenge with conducting quality assurance for the tools is the need to review
thousands of radiology notes for diagnostic support tools.

Hospital representatives in the workshop also highlighted several good practices to
address these challenges. To address the fragmentation of AI tools and vendors, a
hospital representative from Italy reported that their healthcare facility developed a
feasibility checklist to assess whether AI solutions could be adapted and/or integrated
into their internal hospital framework. The representative also suggested a catalogue
of AI vendors with specific key performance indicators. A hospital representative
from Israel added that the catalogue could include an “AI sand ox” where hospitals
could test AI products using anonymised data to evaluate the tool’s performance in a
standardised way. The hospital representative from Israel also described single
platforms provided by local vendors, within which various AI solutions can be piloted
and purchased, all integrated into the same platform for ease of integration.

To address the variation in performance, the hospital representative from Israel
reflected upon the importance of conducting pre-evaluation or pilot projects within
their hospital to ensure AI tools work correctly for their specific patient population, use
cases, and clinical workflows. Lastly, to address the lack of post-deployment
mechanisms a hospital representative from the USA explained that they developed an
AI hub to track every AI transaction, including inputs and outputs. This information
supports quality assurance plans, which then become the vendor's responsibility.
Additionally, the hospital has developed in-house solutions to ensure internal
monitoring and performance, with set thresholds to ensure sustainable impact.

10.4.5.2 Legal and regulatory challenges and good practices

In the survey, legal and regulatory challenges affecting the deployment of AI in
healthcare revealed several points of convergence and divergence across stakeholder
groups (Figure 22).
Figure 22: Legal and regulatory challenges believed to have a significant impact on the
deployment of AI tools according to 25 hospital representatives, 47 HCPs, and 32 AI
developers

  Complexity of regulatory approval process for
                                                       56%            47%           66%
         AI product commercialisation

   Concerns surrounding data privacy and data
                                                       56%            49%       44%
                   protection

  Cybersecurity issues and vulnerability of data
                                                       52%       38%          48%
                to data breaches

     Lack of guidance on compliance of AI tools
                                                      39%     39%       35%
               with current legislation

 Lack of accountability and liability structure for
                                                      40%      43%      22%
                  errors by AI


                                   Hospital     HCP   AI developers

One of the areas of convergence across all stakeholder groups is the concern
surrounding the complexity of the regulatory approval process for AI products.
HCPs (47% of respondents), hospital representatives (56% of respondents), and AI
developers (66% of respondents) all view the EU regulatory frameworks, such as the
Medical Device Regulation (MDR) and the AI Act, as barriers to market entry and
adoption. HCPs and hospital representatives described the regulatory process as slow
and cumbersome, and AI developers indicated that these lengthy approval processes,
compared to those in the USA, hinder innovation by prolonging the time it takes for AI
tools to reach the market.

Another common challenge is data privacy and protection, highlighted
by HCPs (49% of respondents), hospital representatives (56% of respondents), and AI
                                            Deployment of AI in healthcare – Final Report


developers (444% of respondents). All stakeholder groups indicated that AI requires the
use of sensitive health data, raising concerns about data breaches and misuse.
While the General Data Protection Regulation (GDPR) provides a framework for data
protection, HCPs and      hospital   representatives highlighted the lack     of    clear
guidance on how AI tools can comply with these regulations. AI developers added that
the collection, storage, and sharing of data pose challenges that affect patient trust, as
concerns over privacy increasingly impact how patients engage with AI technologies.
The shared focus on data protection indicates a broad concern about how the current
legislative landscape addresses AI’s handling of sensitive information, with all groups
calling for clearer compliance guidelines to improve trust in AI solutions.

Cybersecurity issues was a third area of convergence. HCPs (38% of respondents)
indicated that cybersecurity vulnerabilities, such as data breaches and
unauthorised access, undermine trust in AI systems and require costly protective
measures, which can delay deployment. Hospital representatives (52% of respondents)
acknowledged that while cybersecurity challenges existed before AI, the increased
digitalization of healthcare, including AI tools, increases the importance of maintaining
data integrity and confidentiality. AI developers (48% of respondents) highlighted
the potential damage to patient trust from cybersecurity threats, emphasising the risks
of unauthorised access to sensitive medical data, which could lead to identity theft
and misuse.

The lack of accountability and liability structures for AI errors raised concerns
for HCPs and hospital representatives. Both groups highlighted the uncertainty created
by the absence of clear guidelines on who is responsible for AI mistakes. HCPs (43%
of respondents) worried about the legal repercussions if they were held accountable
for errors made by AI tools over which they have no control, and hospital
representatives (40% of respondents) felt this uncertainty could discourage reliance
on AI in clinical settings due to fears of being blamed for AI-related errors. In
contrast, AI developers placed less emphasis on accountability concerns, focusing more
on regulatory approval and getting their products to market, suggesting that while end-
users are concerned about legal risks, they prioritise getting their products through
regulatory approval and to market.

There were also divergences on how those stakeholder groups view the necessary
practices to address the legal and regulatory challenges. Hospital representatives have
implemented compliance teams to ensure adherence to privacy and data protection
rules, while AI developers emphasised the importance of routine audits (e.g., for
GDPR compliance) but cautioned that excessive audits could slow down the development
of AI tools unless clearer guidance is provided. Additionally, both HCPs and hospital
representatives, highlighted the need for clearer legal frameworks that define the
responsibilities and liabilities of AI users, especially under regulations like the AI Act and
GDPR, while AI developers focused more on addressing barriers to market entry.

In the interviews, key topics for challenges centred around the complexity of the
regulatory landscape, the difficulty of keeping regulations up to date with
innovation and issues related to data security. Challenges stemming from the
complexity of the regulatory landscape was highlighted by one AI developer from
the USA, both HCPs from Denmark, all four HCPs from the UK and the EU-level
organisation. Specifically, both stakeholders from the USA, noted that the regulatory
landscape in the EU is more fragmented than in the USA, with regulations existing at
the EU-level as well as at individual country level that are often stricter, thereby
hindering dataflow between countries. The stakeholders from Europe underpinned this,
highlighting that this challenge may be further compounded by fragmentation between
regulations such as the EU AI Act, General Data Protection Regulation (GDPR) 360 and
the Medical Device Regulation (MDR)361.

Additionally, the AI developer form the Netherlands, one HCP from Denmark and one
HCP from the USA noted concerns regarding clinician liability when using AI -driven
tools due to their often opaque and potentially controversial decision-making processes.
Two HCPs from the UK highlighted challenges with AI deployment under GDPR. In terms
of monitoring, they noted that patient anonymisation becomes difficult for real-
time algorithm evaluation, adding that there is unclear guidance on when and how to
inform patients about the use of AI in their treatment.

Difficulties with keeping regulations up to date with rapid technological innovation
was highlighted by four HCPs362, the hospital representative from the USA and two AI
developers from the USA. Specifically, the hospital representative form the USA as well
as one HCP from Denmark expressed concerns that a lag in regulation can result in the
unregulated use of certain tools, particularly in high-impact scenarios.

Challenges due to strict regulations on data sharing and the lack of clear
guidelines on how data can be used was highlighted by three HCPs 363 and four AI
developers364. The EU-level organisation added that different regulations between EU
Member States on data governance also create inconsistencies with how data can be
used, complicating the deployment of AI solutions across borders. On an international
scale, one AI developer from the USA and the EU-level organisation agreed that
diverging regulatory standards can create challenges for international companies when
it comes to accessing and sharing data. The AI developer explained that the varying
levels of strictness to privacy laws, for example, between the EU and the USA can
sometimes result in tools being trained on lower-quality data.

Challenges with data security, particularly when it comes to cloud systems were
expressed by the hospital representative from South Korea, the hospital representative
from Belgium as well as the HCP from the USA and one HCP from Italy. For instance,
the hospital representative from South Korea pointed out challenges with maintaining
data security and quality when shifting from on-premises to cloud systems. In relation,
the hospital representative from Belgium highlighted uncertainty about where cloud-
stored data is sent, such as whether it stays in Europe or is transferred abroad.

Legal and regulatory best practices were described by three HCPs from the UK who
explained they navigate the complex regulatory landscape through dedicated
platforms that help AI developers, adopters and the public to navigate the regulations,
guidelines and incident reporting around AI for health and care. They are also using
readiness checklists to guide technical and governance requirements. The AI
developer from Japan also mentioned country-wide systems in place that eases
regulatory complexity for developers by allowing them to eliminate the need to




360 Official Journal of the European Union (2016). Regulation (EU) 2016/679 of the European Parliament
and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of
personal data and on the free movement of such data. Available at: Link
361 Official Journal of the European Union (2017). Regulation (EU) 2017/745 of the European Parliament
and of the Council of 5 April 2017 on medical devices. Available at: Link
362 One HCP from the USA and three HCPs from the UK
363 HCP from the Netherlands, Austria, one from Denmark
364 The AI developer from the Netherlands, three from the USA
                                           Deployment of AI in healthcare – Final Report


obtain approval for each new version of medical device software tools. Additionally, they
also highlighted processes in place to speed up the approval process for certain tools.

In terms of best practices for data sharing, the AI developer from the Netherlands stated
the importance of forming long-term partnerships with external companies to
manage data privacy effectively. From the hospital point of view, one HCP from the UK
described their practice of sending developers anonymised data to assess the
algorithm’s performance. This maintains the confidentiality of patient information while
supporting the continuous improvement of the AI system. To ease the regulatory
confusion around data privacy, one AI developer from the USA recommended having
standard regulations that go across all nations with some-specific extra regulations
for states such as California.

In the hospital workshop, hospital representatives highlighted the complexity of the
regulatory framework as a barrier to effective deployment of AI. A hospital
representative from Italy noted that the biggest challenge with complex frameworks,
especially emerging ones like the AI Act, is retrofitting regulatory compliance for
already-developed in-house solutions. The hospital representative from the USA added
that such complex frameworks can sometimes burden and hinder advancements, like
cloud migration, by increasing costs and certification requirements.

The hospital representatives described the practices they have adopted at their
healthcare facilities to mitigate the legal and regulatory challenges. One hospital
representative from Israel reported that, prior to implementation, an internal review
board (IRB) assesses the ethics and regulatory considerations of AI tools. The
representative highlighted that vendors of commercialised products that are considered
medical devices must present the necessary certifications, equivalent to the CE
marking, as a minimum requirement for deployment. Another hospital representative
from Israel indicated that their healthcare facility similarly manages regulation in-house,
including a committee for cloud solutions and an IRB that reviews each new
product. A hospital representative from Italy added that before any AI project is
considered, a hospital readiness assessment and feasibility study is conducted,
along with extensive regulatory evaluation. The hospital representative from the USA
reflected on the importance of holding vendors accountable for efficacy and utility,
while also emphasising the need for a fallback plan to ensure safe hospital operations
during outages.

10.4.5.3 Organisational and business challenges and good practices

The survey analysis revealed convergences and divergences in perspectives across
stakeholder groups regarding the organisational and business challenges associated
with AI deployment (Figure 23). Each stakeholder group highlights specific barriers and
good practices, with some overlap in the key challenges they identify, while other
concerns are more specific to certain stakeholder groups.
Figure 23: Organisational and business challenges believed to have a significant impact on
the deployment of AI tools according to 25 hospital representatives, 47 HCPs, and 32 AI
developers

      Lack of funding, investment and financial
                                                      50%        62%         61%
      incentives to deploy AI in clinical practice

    Lack of involvement of end-users in the
 development, validation and deployment of AI         50%        55%    45%
                     tools

 Lack of cost-benefit analysis of AI tools versus
                                                      54%        53%    42%
            existing clinical solutions

    Lack of technological skills and knowledge
    amongst healthcare professionals to use AI        46%       53%    39%
                 tools effectively

    Lack of strategic direction to promote AI in
                                                      44%      53%     38%
                     healthcare


                                   Hospital     HCP   AI developers

The lack of funding, investment, and financial incentives for deploying AI tools in
clinical practice is a common challenge across all stakeholder groups. This concern was
raised by 62% of HCPs, 50% of hospital representatives, and 61% of AI developers. All
groups agree that insufficient financial resources slow AI deployment, with AI
developers highlighting the stark differences in funding availability between the USA
and the EU. HCPs from countries like Portugal and Italy, along with EU-wide HCP
associations based in Belgium, pointed out that the lack of public funding is a barrier
for wider AI uptake. The shared concern among these stakeholders’ points to a need for
better financial models and clearer economic evaluations to demonstrate the value of
AI, which is important for securing investment and achieving widespread adoption.

The lack of involvement of end-users—both HCPs and patients—in the development
of AI tools is another point of convergence across stakeholders. HCPs and hospital
representatives highlighted that the absence of co-design and local performance
testing processes often results in AI solutions that are not aligned with clinical needs
or workflows, making them difficult to integrate into daily practice. HCPs pointed out
that older or less technologically competent staff members are particularly slow to adopt
new technologies when they are not actively involved in their development or training.
Hospital representatives agreed that multidisciplinary collaboration and
performance testing by end-users are essential to ensure AI tools meet clinical
needs. Similarly, AI developers acknowledged that a lack of user engagement leads to
tools that are less usable or not trusted by HCPs. They pointed out that conservative
attitudes among some HCPs further hinder adoption. This shared concern suggests a
strong need for more inclusive design and performance testing processes that
involve end-users early in development, fostering greater acceptance and integration of
AI tools.

Another point of convergence is the lack of cost-benefit analyses of AI tools
compared to existing clinical solutions. According to the survey responses, 54% of
hospital representatives, 53% of HCPs and HCP associations, and 42% of AI developers
reported that failing to evaluate the economic value of AI tools will make it harder
for leaders to prioritise AI investments in financially constrained/low-resource
environments and justify the high upfront costs of AI tools. AI developers also
                                               Deployment of AI in healthcare – Final Report


emphasised the challenge, stating that they need to generate sufficient revenue to
justify their tools, but the absence of robust cost-benefit studies complicates this effort.

Divergence emerged in views on strategic leadership and AI training. HCPs and
hospital representatives emphasised fragmented leadership in AI deployment as a
barrier, citing delays due to a lack of central coordination, redundant projects, and
poorly allocated resources. Regarding AI training, HCPs highlighted insufficient AI
training as an important barrier to effective AI use. They indicated that while some HCPs
are willing to engage with AI if given the time to acquire the necessary skills, the lack
of structured training programs hinders widespread adoption. On the other hand, AI
developers placed more emphasis on the role of training programs for HCPs but were
less concerned with resistance to technology. They believe that comprehensive training
programs can overcome resistance and enable HCPs to use AI tools effectively. Hospital
representatives also recognised training as an important component of AI adoption, with
many already implementing staff training programs as part of their AI deployment
strategies. This divergence suggests that while all groups see training as important,
HCPs are more focused on the practical and psychological barriers to learning new
technologies, while AI developers and hospital representatives view training as a more
straightforward solution to the adoption challenge.

In terms of good practices, there is a general convergence across stakeholder groups.
HCPs, hospital representatives, and AI developers all highlighted the importance of
testing/piloting AI tools before deployment and ensuring they fit seamlessly into
existing clinical workflows. Multidisciplinary collaboration and stakeholder
engagement, including involving HCPs, administrators, and support staff, were seen
as important for successful AI integration. AI developers also highlighted the importance
of conducting workflow analyses within healthcare facilities to understand processes
and redesign AI tools to fit into those workflows. These practices were described as
transferrable across different regions and healthcare settings, highlighting broad
agreement on the steps required to overcome organisational challenges and ensure the
effective use of AI.

 “Assessment helps justify the cost of AI technologies by demonstrating their potential benefits
 over traditional practices, thereby facilitating stakeholder buy-in. Aligning reimbursement
 models with value-based care ensures that the financial incentives for using AI tools reflect
 their actual contributions to patient outcomes. Having healthcare professionals validate AI
 systems before deployment not only ensures that the tools meet clinical needs, but at the
 same time helps reduce resistance. The recruitment of data scientists and AI specialists has so
 far enabled hospitals to tailor AI solutions to their specific clinical needs and integrate them
 into existing workflows. Alternative funding models, particularly for publicly financed facilities
 allow for continuous investment in upgrades and training.” – EU-wide HCP association based
 in Belgium.


Interviewees also reflected on several organisational and business challenges, with
key themes emerging around a lack of strategic direction by hospitals/healthcare
systems, financial challenges, bureaucratic hurdles in adopting AI tools as well as
challenges related to the lack of training and user literacy when it comes to using
AI tools.

From an AI developer point of view, diverging strategic directions causing challenges
to AI deployment were pointed out by two developers from the USA, explaining the
difficulties around meeting the often highly variable strategic directions of stakeholders.
For example, healthcare systems with large budgets may be willing to experiment with
innovative AI technologies, while others may prioritise tools that offer a clear return on
investment and cost-effectiveness. Additionally, one AI developer believes AI tools that
provide a broad utility and ease workflows are more likely to see widespread adoption.
However, one HCP from Denmark expressed concerns over having to tailor commercially
available AI solutions to address specialised needs of subspecialties.

In terms of the hospital viewpoint, differing approaches between hospital leaders
and clinicians can also cause strain when using AI tools according to the hospital
representative from USA and one HCP from the UK. For example, while AI scribes can
free up clinicians' time by handling note-taking, leadership might suggest using the time
saved to increase patient load instead of allowing clinicians more time with their
patients. Equally, one AI developer from the USA and one HCP from the USA explained
that a competitive mindset among hospital leadership can result to a lack of
collaboration and data sharing, both within and between healthcare organisations,
thereby slowing down the adoption of AI solutions.

Challenges due to a lack of strategic direction from leadership, particularly in
countries with fragmented healthcare systems was pointed out by one HCP from
Denmark, one HCP from the UK and one AI developer from the USA. The HCP from
Denmark and the HCP from Austria highlighted additional challenges posed by a lack
of collaboration between AI developers and end-users as well, for example when
communicating feedback and improvements to deployed solutions.

Challenges to AI adoption due to a lack of funding, investment and financial
incentives were highlighted by the hospital representatives from Belgium and South
Korea along with the AI developer from Japan. Five HCPs 365 along with one AI developers
from the USA and one AI developer from Germany also pointed out that tight budgets
and slim margins in healthcare systems make it hard to justify financial investments in
AI tools. Specifically, the HCP from Austria and the HCP from Spain explained that
financial constraints, particularly in public hospitals, make it challenging to translate the
clinical value of AI into financial terms. Similarly, one HCP from the UK reflected that
existing government funding is often used inefficiently by focusing only on implementing
AI, without considering the broader needs like education, policy development, and the
creation of necessary platforms to ensure effective AI integration in the healthcare
system.

In terms of reimbursement, one AI developer from the USA, one HCP from Denmark
and the hospital representative from Belgium also pointed out uncertainties around who
should cover the costs of deploying AI, as well as low reimbursement rates
discouraging HCPs from using AI tools, especially in radiology. The AI developer
added that the financial burden and time required to conduct clinical trials further
complicates AI tool adoption. One HCP from the UK agreed, stating that the long
timelines needed to demonstrate the effectiveness of AI, such as in cancer treatment,
make it hard for healthcare systems like the NHS to adopt AI innovations when
immediate benefits are required. This leads to insufficient assessment of AI's added
value compared to existing practices.

Inefficiencies in selecting and deploying AI solutions due to bureaucratic
hurdles were mentioned by the HCP from Austria and the HCP from Spain from a
hospital perspective. In terms of vendor selection, the HCP from Austria explained that
different companies offer various financial models for AI tools, which makes it difficult
for departments to standardise contracts. Following vendor selection, the HCP from
Spain added that legal agreements for initial pilots as well as obtaining ethical


365 HCPs from Spain, one from Denmark, one from UK, one from US
                                                Deployment of AI in healthcare – Final Report


committee approval, which can take approximately two years in Spain, are time-
consuming for departments to negotiate and can cause delays for AI adoption. From the
perspective of AI developers, one developer from the USA stated issues with the lack of
support from professional societies and associations, which often avoid endorsing
specific vendors to remain neutral. They stated that this neutrality can leave healthcare
providers uncertain about which AI tools to deploy, thereby slowing down the
deployment process. Another developer from the USA highlighted bureaucratic
resistance from hospital administrators, who may refuse or delay the deployment of
tools, even when it has been recommended by their healthcare professionals.

A lack of AI scientists and leadership in data literacy complicating the integration
of AI was perceived by six HCPs366 and one AI developer from Germany, concluding that
without leaders who are well-versed in data-driven decision-making, it becomes difficult
to coordinate AI efforts effectively. Another HCP from the UK noted that there is a lack
of mandatory training and outcome checks for AI products, with minimal training
required for the use of AI tools and sparse post-market surveillance.

In terms of good practices, hospital representatives, HCPs and AI developers shared
several practices to mitigate organisational and business challenges related to AI
deployment. These converged around highlighting the importance of collaboration,
adopting a multidisciplinary approach, providing training for hospital staff as well as
practices to mitigate financial challenges. The importance of collaboration for
successful AI deployment in healthcare systems was emphasised by one HCP from Italy,
one HCP from Denmark and one hospital representative from Japan. One AI developer
from the USA added that it is important to collaborate with healthcare professionals who
do not have a financial stake in the company, highlighting how they worked closely with
urologists during the development of their AI tools. On a networking level, the HCP
from Denmark participates in the European University Hospital Alliance 367, where
specific forums are held to discuss key parameters related to AI implementation. One
HCP from the USA also highlighted how major hospitals often work together in networks
that facilitate collaboration and knowledge-sharing. They additionally noted the
importance of public-private partnerships in fostering innovative patient care in a way
that balances the interests of developers with societal benefits.

Adopting a multidisciplinary approach when deploying AI tools across healthcare
systems was also recommended by two HCPs from the USA and one AI developer from
the USA. Some centres integrate AI solutions through a comprehensive strategy
involving multidisciplinary teams, including IT experts, data engineers, clinicians, and
financial analysts.

Three HCPs from the UK and one HCP from the USA described digital literacy efforts
and various training programmes for the use of AI tools. One HCP from the UK also
explained that there is growing consideration for integrating AI training into medical
curricula at both the undergraduate and postgraduate levels. These courses would
include mandatory AI awareness training alongside existing modules like information
governance and data protection. With reference to expert knowledge, the hospital
representative from the USA sated that investing in a team of technological leads
had been a key accelerator for AI deployment in their hospital.

To mitigate financial challenges, one HCP from the USA reflected on the benefits of
segmenting AI projects into smaller, manageable use cases that can deliver faster

366 HCPs from the Netherlands, Austria, one from Denmark, two from the USA, one from UK
367 European University Hospital Alliance. Available at: Link
returns. Two AI developers from the USA also described measure and demonstrating
the AI tool's impact across three key areas: clinical value (improved patient outcomes),
operational efficiency (workflow improvements and time savings), and financial impact
(cost-effectiveness). One HCP from the USA concluded that financial support from
management contributes to the success of AI programmes, explaining that strong
backing from top leadership is critical for building the necessary infrastructure for AI
solutions.

The hospital representatives in the hospital workshop provided more specific
challenges. Two hospital representatives from the USA described challenges in
recruiting and affording the right talent. For instance, one representative indicated
that the starting salary for a 23-year-old computer science graduate is considerably
high, making it unaffordable for most hospitals. Additionally, one hospital representative
from the USA highlighted the challenges in defining and quantifying the return on
investment (ROI). The representative described that this metric is highly dependent
on the healthcare system– public, private, not for profit etc which results in complexities
in terms of how it can be evaluated. Furthermore, one hospital representative from
Israel pointed out that scaling AI solutions beyond niche applications, such as
imaging and digital pathology, to a broader organisational level is also a
challenge. The representative explained that hospitals struggle to justify the ROI to the
management and to manage the dozens of deployed models while integrating them into
existing risk and quality assessment frameworks. This transition represents a new phase
in AI deployment that healthcare facilities are still navigating.

Hospital representatives shared several best practices to mitigate organisational and
business challenges related to AI deployment. A hospital representative from the USA
emphasised the importance of having multidisciplinary teams, operational
readiness, and ensuring that data is prepared. The representative described a
playbook they created for late adopters to learn from early adopters' experiences. In
addition, department leaders in the USA are tasked with identifying AI use cases,
which are then centrally evaluated through a business case process to ensure
alignment with operational capabilities. Another hospital representative from the
USA highlighted that, rather than focusing on billing, they prioritised efficiency gains
from AI tools and warned against billing codes incentivising inappropriate AI
tool use. In terms of ROI, the representatives from the USA and Italy both stressed
the importance of learning from past implementations and noted that efficiency-
focused AI tools are less impacted by regulations, allowing faster deployment.

A hospital representative from Israel pointed to the importance of having an AI
champion within departments to ensure effective deployment. The representative
from the USA highlighted that their hospital took a holistic change management
approach, involving business stakeholders, users, healthcare professionals, and nurses
to foster a person-centred understanding of how AI will fit into workflows. The
representative from the USA also promoted internal innovation competitions, where
HCPs submit clinical needs for investigation. Finally, the hospital representative from
Israel explained that hospital advisory boards, representing physicians, nurses, and
researchers, can gather input using a scoring system to prioritise needs based on
patient impact and urgency.

10.4.5.4 Social and cultural challenges and good practices

The survey provided converging and diverging perspectives across stakeholder groups
on the social and cultural challenges affecting the deployment of AI in healthcare. Across
HCPs, hospital representatives, and AI developers, several shared concerns emerged,
                                               Deployment of AI in healthcare – Final Report


particularly regarding digital literacy, trust in AI, and concerns about overreliance on AI
technologies (Figure 24).

Figure 24: Social and cultural challenges believed to have a significant impact on the
deployment of AI tools according to 26 hospital representatives, 47 HCPs, and 30 AI
developers

                       Lack of trust in AI tools         50%           28%           55%

   Low level of digital health literacy among
                                                          58%                43%         26%
  healthcare providers and the general public

           Concerns about overreliance on AI            46%            36%         23%

     Concerns about patient autonomy and
                                                      38%        21%    23%
   consent in the use of AI tools for their care
  Concerns about AI's impact on the personal
                                                      38%        15%13%
   relationship between doctor and patient
          Concerns about skill shift to remain
                                                    27%     15%13%
            competitive in the job market
 Concerns among healthcare professionals on
                                                   12% 11% 10%
               job security

                                  Hospital    HCP      AI developers


A shared concern is the lack of trust in AI tools was shared by hospital
representatives (50%) and HCPs (28%) highlighting their concerns about the safety and
transparency of AI in decision-making. Additionally, 59% of AI developers recognised
that trust issues slow AI adoption describing that the lack of trust can lead to
resistance to using these technologies. Patients may opt out of AI-assisted treatments
or diagnostics, which could affect the overall effectiveness of their care and potentially
limit the benefits that AI could offer.

Another area of convergence is the low level of digital health literacy among HCPs
and the general public. In the survey, 43% of HCPs, 58% of hospital representatives,
and 27% of AI developers agreed that limited digital literacy hinders effective AI
deployment. Upskilling staff and improving digital literacy were seen as key to
integrating AI in clinical practice, with continuous education and AI-related content in
medical curricula identified as important steps. HCPs and hospital representatives also
indicated that older HCPs and patients may struggle with new technologies,
highlighting the need for targeted education efforts in these populations.

Divergence occurs in the perception of overreliance on AI and the implications this might
have on healthcare delivery. While 46% of hospital representatives and 36% of HCPs
identified it as a barrier, indicating that AI could undermine critical thinking and clinical
judgment, only 23% of AI developers viewed it as a challenge. AI developers generally
see AI as a tool to enhance decision-making, with less concerns on the risks of
overreliance.

There is divergence in the perception of AI’s effect on doctor-patient relationships. HCPs
and hospital representatives are split on this issue, with some viewing AI as a threat to
the personal connection between doctors and patients, while others see AI as a tool that
can improve care by optimising time and resource allocation. There is also variation in
how these challenges are perceived across regions. Some AI developers, particularly
those from countries like Italy, Sweden, and Germany, noted that regional differences
in digital literacy, regulatory environments, and the level of trust in technology can
influence the adoption of AI. For example, in regions that deal with vulnerable
populations, such as migrants or the elderly, concerns about doctor-patient relationships
and consent may be more pronounced, adding complexity to AI deployment.

In terms of good practices, there is a consensus on the need for comprehensive
education and training to tackle social and cultural challenges. Both hospital
representatives (57% of respondents) and HCPs (65% of respondents) emphasised the
importance of continuous learning and targeted training programs to upskill
HCPs and improve digital literacy.

 “By incorporating AI and related technologies into medical education, you prepare future
 healthcare professionals not only to understand and effectively use AI tools in their practice,
 but most importantly to accept them. This approach helps overcome resistance due to
 unfamiliarity or fear of AI by embedding technological literacy from the start of their careers.
 Likewise, when all stakeholders understand how AI can improve patient outcomes, reduce
 workload, and enhance decision-making, it reduces fear and resistance. If we would like to
 prepare members of the health and care workforce for todays and tomorrow’s challenges and
 opportunities – investing in skills is a must by updating university curricula, offering training
 programmes.” – EU-wide HCP association based in Belgium.


In the interviews, the key social and cultural challenges highlighted by stakeholders
related to user’s resistance to change and lack of trust as well as an overreliance
on AI’s outputs. On the part of healthcare professionals, the HCP from Italy along with
one HCPs from the USA and the hospital representative Japan agreed that resistance to
change can be compounded by the fear created due to uncertainties about how AI might
affect healthcare roles, such as concerns about job loss. The hospital representative
from Belgium added that fear over AI tools becoming decision-makers rather than being
consultative tools can also cause reluctance in adoption by clinicians.

On the part of patients, the hospital representative from the Netherlands observed
patient discomfort with a recently deployed digitalised therapy administration system,
while the hospital representative from Japan and one AI developer from the USA noted
patient resistance, particularly when it comes to the uploading of AI data to
the cloud. Conversely, one HCP from the UK felt that there is a relatively high level of
trust among patients for the use of AI within healthcare. Two HCPs 368, the hospital
representatives from the USA and South Korea as well as one AI developer from the
USA believed that trust issues are more problematic among HCPs than patients
because they remain sceptical of the quality of AI tools. Similarly, the AI developer from
Japan along with the hospital representative from the USA highlighted that there is a
lack of willingness to change, especially among older HCPs. Nevertheless, the AI
developer from Japan reflected that this resistance is slowly starting to shift as digital
technology is becoming more widespread and accepted in healthcare.

Six HCPs369 and two AI developers370 also reflected that a lack of trust in AI is often
compounded by a lack of explainability of AI’s outputs, especially when it differs from
human choices. Overall, the AI developer from the Netherlands pointed to the lack of
requirements for explainability, stating that there are no obligations at present for
vendors to provide detailed information about how an AI tool was tested, who conducted
the testing, or other in-depth analyses. Nevertheless, they stated that in resource-


368 HCP from Austria, one HCP from Denmark, two from Italy
369 HCPs from the US, one from the UK, Austria, one from Denmark
370 AI developers from the Netherlands, one from the US
                                          Deployment of AI in healthcare – Final Report


limited areas, traditional trust issues may be set aside in favour of adopting the most
accessible AI solution, as it is better than having no solution at all.

One HCP from the UK, the HCP from Austria and the AI developer from Germany
reflected that overreliance on AI could lead to automation bias and overshadow
human expertise, particularly among younger clinicians, who may become too reliant or
trusting of AI tools. One AI developer form the USA agreed with this sentiment,
concluding that people tend to trust and adopt technologies that offer clear benefits
more quickly.

To address challenges in AI transparency and trust, one AI developer from the USA, the
hospital representative from Japan, one HCP from the UK and the EU-level organisation
highlighted the importance of clearly communicating with stakeholders, including
on the benefits of AI technologies to patients as well as how their data is managed. One
HCP from the USA referred the best practices adopted by leading AI hospitals for
communicating with their stakeholders about responsible AI adoption and
implementation. These organisations clearly communicated their goals, benefits, and
operational changes associated with AI integration to all stakeholder as well as shared
their processes publicly, pointing out what they did, where they made mistakes, and
where they could have improved for other centres to learn from those mistakes and
best practices. To alleviate automation bias, one HCP from Austria explained that
educating radiologists on the role of AI tools as supportive tools rather than definitive
tools could be helpful.

The low level of digital literacy among HCPs and the public was a key challenge
during the hospital workshop. A hospital representative from Israel emphasised that
limited AI literacy among HCPs can lead to two issues: reluctance to use AI out
of fear and overreliance on AI technologies without proper education. The
representative explained that using AI without adequate training not only limits the
value extracted from these technologies but also poses potential risks to patient safety.

Hospital representatives reported several social and cultural practices to address the
challenges associated with AI deployment in healthcare. A hospital representative from
Israel reported that the proximity to an innovation ecosystem and local leading
start-ups might have been an accelerator for AI adoption in Israel. The representative
added that for HCPs to use AI tools effectively, there must be a degree of
explainability tailored to their needs. HCPs do not necessarily need to understand
the complex computational processes behind algorithms but should be able to
understand what specific features resulted in the AI algorithms decision. This
approach fosters trust, promotes responsible usage, and establishes a common
understanding between data scientists, engineers, and HCPs. A hospital representative
from the USA echoed the importance of user-tailored explainability and highlighted
fellowship programs. These programs aim to onboard a balanced cohort of 50%
medical doctors engaged in research and 50% data scientists and computer scientists,
fostering collaboration and improving AI integration into clinical practice. Lastly, this
representative reported that this is a cultural shift, and the hospital has recently
recruited individuals to have a specific focus on data literacy, culture, and
policy to champion the transformation.

10.4.5.5 Generative AI challenges and best practices

The assessment of challenges affecting the deployment of generative AI tools in clinical
practice reveals both convergence and divergence among HCPs, hospital
representatives, and AI developers/associations according to the survey responses. All
stakeholder groups highlighted that generative AI tools pose distinct issues compared
to traditional AI tools, particularly concerning reliability, transparency, and ethical
implications. However, their perspectives differed on the specific nature of these
challenges and the best ways to address them.

An area of convergence across the groups is the concern about hallucinations—AI-
generated outputs that appear valid but are factually incorrect—and the low
explainability of AI decisions. HCPs (43% of respondents) pointed out that
hallucinations and poor explainability are major challenges, as the reliability of
generative AI outputs is not yet guaranteed. This sentiment was echoed by hospital
representatives (49% of respondents), with one from the Netherlands highlighting the
importance of validating AI-generated information, as it fundamentally differs from
traditional AI, which relies on existing patient data. Similarly, AI developers also
identified hallucinations as a key issue, particularly with LLMs, as generative AI
lacks the long-standing reliability mechanisms found in more traditional machine
learning AI tools.

Another point of convergence across stakeholders is the shared concern over data
privacy and protection. Both HCPs and hospital representatives recognised that
generative AI, which often requires large datasets for training, must navigate the
challenge of protecting patient-identifying data (PID). HCPs highlighted that
generative AI models might struggle with privacy concerns, particularly in cases where
models are trained on limited or sensitive data. Hospital representatives highlighted the
risk of personal data leakage and noted that generative AI might require local data
processing to ensure security. AI developers also acknowledged that generative AI tools,
many of which are designed for public datasets, face more challenges in healthcare
environments due to the sector’s strict data protection requirements.

A divergence appears, however, in how these groups perceive the technological
challenges. HCPs and hospital representatives primarily focused on the practical
implications of AI-generated outputs in clinical contexts. For example, HCPs
expressed concerns a out generative AI’s a ility to accurately process edical
information, particularly given the variations in free-text writing, grammatical
inconsistencies, and differing word meanings in medical documents. AI developers were
more focused on the broader technical limitations of generative AI, such as its lack
of reliable error-prevention mechanisms compared to traditional AI tools.

Legal and regulatory challenges were another area of divergence, where AI developers
emphasised the complexities of navigating intellectual property (IP) rights, which
were not a major concern for HCPs or hospital representatives. AI developers were
particularly concerned with the lack of clarity around IP protection for AI elements
such as training data, model outputs, and model improvements. On the other hand,
HCPs and hospital representatives focused more on the liability and accountability
concerns associated with generative AI in clinical practice.

In terms of good practices for deploying generative AI, only a small portion of HCPs
(22% of 51 respondents) and hospital representatives (29% of respondents) reported
knowledge of good practices. Among those who did, the focus was on avoiding the
inclusion of personal identifiable information in software outside the EHR
system and on training and fine-tuning generative AI models with specific
medical contexts to improve their relevance in clinical settings.
                                         Deployment of AI in healthcare – Final Report


10.4.6 Impact of the current regulatory landscape

On the impact of the current regulatory landscape within the EU, insights were gathered
from hospital representatives, HCPs, AI developers/researchers, and EU regulatory
experts through the surveys, the AI deployment journey workshop, the regulatory
workshop, and the interviews.

From the survey, an area of convergence among the stakeholder groups is the
increased workload and resource demands imposed by the EU AI Act. HCPs (87%
of 30 respondents) believe the AI Act addresses key challenges in healthcare, such as
patient protection, but 72% (25 respondents) indicated that it also adds new barriers,
including additional training requirements for accountability standards and the
need for more risk management protocols. Hospital representatives indicated that
only 23% (6 out of 25 respondents) feel prepared for the obligations introduced
by the AI Act, expressing concerns about the financial and logistical burden of
compliance, including difficulties in finding skilled personnel and the need for
investments in infrastructure and training. AI developers noted the
administrative burden of aligning with both the AI Act and the MDR, with some
finding the AI Act’s impact marginal if they are already familiar with the MDR.

Training and compliance support emerged as another shared concern. HCPs
suggested the implementation of short, accessible training programs that fit into
their busy schedules and proposed the establishment of peer-to-peer support
networks and collaboration with legal experts. Hospital representatives echoed the
need for government-accredited auditors and increased access to training
resources. AI developers who are prepared 47% of 34 respondents) for the AI Act
have begun creating frameworks for early identification of AI risks and
conducting workshops to educate teams on compliance.

The area of divergence was reported in how each stakeholder group perceived specific
challenges introduced by the EU AI Act. HCPs expressed frustration over issues related
to accessing and assessing AI training data, uncertainties about HCP training
requirements, and the extent of patient consent needed for AI use. Hospital
representatives focused on financial and logistical compliance challenges, with a
hospital representative from Sweden noting a lack of funding for legal advisory
roles and difficulties adapting the AI Act to healthcare settings, and hospital
representatives from Finland and the Netherlands echoing this difficulty in adaptation
and drawing parallels to earlier challenges with the GDPR. AI developers prioritised
legal and technical aspects, highlighting challenges related to intellectual property
protection, transparency, and synthetic data usage.

Another point of divergence relates to the readiness for the AI Act’s
implementation. Only 23% of hospital representatives (6 out of 25 respondents)
reported feeling prepared for the obligations introduced by the EU AI Act, with
only a small proportion taking concrete steps like implementing oversight protocols
and staff training. However, the majority face resource shortages and lack clarity
on how to      eet the Act’s require ents, particularly in risk assessment and data
quality evaluation. In contrast, among AI developers, 47% (16 out of 34 respondents)
are prepared for the implementation of the AI Act and the associated
obligations, especially those experienced with MDR/IVDR compliance, viewing the AI
Act as an extension of their current efforts. Some AI developers indicated they had
already integrated transparency measures and ethical frameworks, though others
remain in a transition phase, delaying new tool deployment until they fully understand
the AI Act.
Regarding the European Health Data Space (EHDS) regulation, there is a lack of
consensus on its effectiveness on the deployment of AI tools in healthcare. While 71%
(18 out of 25 respondents) of hospital representatives are aware of the EHDS, only 48%
(12 out of 25 respondents) believe it addresses challenges in deploying AI tools. On the
contrary, AI developers have not expressed any concerns about the EHDS in relation to
AI deployment, likely because their focus is more on regulatory frameworks like the AI
Act and MDR, which have more direct implications for their operations.

In the interviews, four EU-level stakeholders (two HCPs371 and two AI developers 372)
along with two AI developers from the USA and one hospital representative from the
USA discussed the implications of the EU AI Act on the AI landscape in healthcare. One
HCP from Italy and the AI developer from Germany first stated the benefits of the AI
Act noting that it provides a clear regulatory framework for AI technologies. They
emphasised that it helps address accountability by defining responsibilities when issues
arise and brings a strong focus on data security and patient privacy.

Nevertheless, all four EU-level stakeholders also noted that the initial regulatory
transition to comply with the AI Act may present difficulties, for example, when
it comes to adapting existing processes to meet new regulatory requirements. As such,
one HCP from Denmark surmised that the complex regulatory demand coupled with a
lack of guidance risk driving AI developers towards regions like the USA, where
regulations are more lenient. To help mitigate these challenges, one HCP Italy suggested
that organisations and manufacturers already integrate compliance with the AI Act into
their development processes from the outset.

The AI developers from the Netherlands and USA, along with a hospital representative
from the USA expressed the need to find the balance between regulations ensuring
safety without hindering innovation. To enable this, two AI developers from the
USA called for a focus on simplicity and future proofing in regulations, for example,
proposing deeper collaboration with regulators in order to ensure regulations are
conducive to innovation while maintaining safety and effectiveness in AI deployment.

In terms of the hospital workshop, the participants provided insights into the regulatory
landscape for AI in healthcare across different countries, highlighting varying levels of
development and implementation of regulations. The hospital representative from Italy
reported that the compliance landscape for the AI Act mirrors the initial challenges
faced during the transition to GDPR compliance. The representative explained that, while
there was confusion during the transition period, GDPR compliance eventually became
integrated into existing processes.

As for the regulatory workshop with EU regulatory experts, several key challenges
regarding the deployment of AI in healthcare were discussed. These included the
complexity of the regulatory approval process for AI-based technologies, variation in AI
performance across healthcare settings and populations, the lack of accountability and
liability frameworks for AI errors, concerns about data privacy and cyberattacks, and
the impact of AI on the doctor-patient relationship and the accuracy of AI decisions.

The challenge of the complexity of the regulatory approval process for AI-based
technologies was discussed. According to the regulatory experts, the regulatory
sandboxes for real-world testing under compliance introduced in the AI Act (Article
57373), along with the MDR, help address this challenge. Additionally, the experts added
that the AI Act, sets market entry requirements and clarifies interactions with clinical

371 One HCP from Italy, one from Denmark
372 AI developers from Germany and the Netherlands
373 Article 57 of the AI Act introduces regulatory sandboxes to allow real-world testing of AI systems while
ensuring compliance with regulations.
                                                     Deployment of AI in healthcare – Final Report


guidelines (Article 8374). However, despite those provisions, the regulatory experts
identified persisting gaps, including the discrepancies between the MDR and AI Act
regarding clinical investigations and certification of solutions before market entry,
concerns about the interpretation of some regulations (e.g. confusion around the
research exemptions for medical devices), the complexity of MDR regulation for in-
house solutions, and the high costs and resource demands associated with
regulatory sandboxes. Furthermore, the regulatory experts expressed uncertainty
about the EU's legal preparedness and whether sandboxes will facilitate AI
acceptance after CE375 marking and deployment.

The variation in AI performance across different healthcare settings and
populations was the second challenge discussed. According to the regulatory experts,
provisions mandating a comprehensive risk management system (Article 9 376 of the AI
Act), the stringent data governance for high-risk AI systems (Article 10 377), the
provisions on ensuring the accuracy, robustness, and cybersecurity of AI systems
throughout their lifecycle (Article 15 378), and the transparency and performance metrics
requirements (Article 13379) partly address this challenge. Despite those efforts, the
regulatory experts highlighted that there is a lack of clear guidance on how to manage
AI performance variations across different populations and settings, raising concerns
about potential healthcare disparities. They also discussed the lack of alignment
between the GDPR and the AI Act in addressing bias, particularly contextual bias, and
noted insufficient data availability for certain populations, which would further
increase the disparities.

In discussing the lack of accountability and liability frameworks for AI errors, the
regulatory experts acknowledged that the AI Act, which mandates a quality
management system (QMS) for high-risk AI systems (Article 17 380), as well as the
Product Liability Directive, partly address this challenge. Nevertheless, gaps were
identified, particularly inconsistencies across Member States regarding liability laws,
which create confusion and hinder HCPs from using AI tools due to fear of legal
repercussions. The regulatory experts also indicated a lack of clarity on the division
of responsibilities at different stages of AI deployment and inconsistencies between
the AI Act and GDPR regarding the role of the data controller.

Data privacy and cyberattacks were also discussed as pressing concerns. The
provisions of the AI Act, addressing cybersecurity (Article 15), testing in regulatory
sandboxes (Article 57), informed consent (Article 61381), and the right to an
explanation (Article 86 382) partly address these concerns. However, the regulatory
experts raised issues regarding the interaction between frameworks such as the GDPR,
MDR, and EHDS. Specifically, they pointed to discrepancies between the AI Act, which


374 Article 8 sets out market entry requirements and clarifies interactions with clinical guidelines for high-
risk AI systems.
375 CE marking (Conformité Européenne) certifies that a product meets EU safety, health, and
environmental standards for sale within the European Economic Area.
376 Article 9 mandates that high-risk AI systems must implement a risk management system to identify
and mitigate potential risks.
377 Article 10 outlines the need for proper data governance and the use of high-quality datasets for high-
risk AI systems.
378 Article 15 ensures that AI systems maintain accuracy, robustness, and cybersecurity throughout their
lifecycle.
379 Article 13 mandates that AI systems provide clear and transparent information on their capabilities,
performance, and limitations.
380 Article 17 mandates that developers implement a quality management system (QMS) for high-risk AI
systems.
381 Article 61 ensures that informed consent is obtained for real-world testing of AI systems on patients.
382 Article 86 grants patients the right to an explanation regarding the role of AI systems in decision-
making processes.
supports comprehensive patient profiles, and GDPR, which emphasises data
minimization to protect patient privacy. This misalignment creates uncertainty
about the extent of data protection required, especially in cases involving EHRs.

Concerns about AI’s i pact on the doctor-patient relationship were also raised.
The provisions of the AI Act, which mandates transparency on AI system capabilities
and limitations (Article 13), emphasises human oversight (Article 14 383) and requires
qualified personnel to oversee AI deployment (Article 26 384), were designed to
safeguard patient trust. While the regulatory experts acknowledge those provisions,
they highlighted ongoing gaps, particularly regarding informed consent. There is still
uncertainty about when and how patients should be informed about the use of AI tools,
how much detail to provide, and the alternatives available. Regulatory experts explained
that the misconception that the more impactful the AI tool, the more information needs
to be disclosed can sometimes overwhelm patients and cause a loss of trust.
Furthermore, differences in Member State requirements on informed consent make it
challenging to provide consistent levels of explanation without overwhelming patients
with technical details.

10.4.7 Considerations for future actions at EU level to support AI deployment

This section outlines considerations for future actions —both regulatory and non-
regulatory that could be implemented at the EU level to support the deployment of AI
tools in healthcare. Based on the survey responses, there was both convergence and
divergence in the complementary actions with input from 35 hospital representatives
and 52 HCPs (Figure 25).




383 Article 14 mandates human oversight for high-risk AI systems, allowing healthcare professionals to
intervene when necessary.
384 Article 26 requires that qualified individuals oversee the deployment and monitoring of AI systems in
clinical settings.
                                              Deployment of AI in healthcare – Final Report


Figure 25: Considerations for future actions to facilitate the deployment of AI in healthcare
according to hospital representatives and HCPs.



             Establishment of common standards on data
               governance, privacy, and interoperability        79%         73%
                 across European healthcare systems

              Provide clarity on regulatory processes for
                                                               65%      69%
             product approval, accountability, and liability


                  Consolidated funding to support specific
                                                               56%     65%
                            strategic priorities

             Redesigning workforce planning and clinical
            education to address future healthcare and AI      50%    61%
              professional needs, investing in upskilling…
                 Organisation and centralised collection of
                 post-deployment data to monitor on the        44%    63%
                     ongoing effectiveness of AI tools
                 Development of platforms to facilitate
             dialogues and exchange of good practices to       50%    59%
                   facilitate deployment of AI tools

              Ensure consistent access to public data and
                                                               53%    49%
                   promoting open-data initiatives

             Encourage the establishment of centres of
            excellence for AI in healthcare to concentrate     56%    39%
                         talent and resources

                Establish an EU AI in healthcare center to
                                                           24% 49%
                 coordinate and facilitate AI deployment




                                          Hospital    HCP


10.4.7.1 Common standards on data governance, privacy, and interoperability

   •   73% of HCPs emphasised that harmonised standards across European
       healthcare systems are important for integrating AI tools without
       compromising data security or patient privacy.

   •   79% of hospital representatives reported that standardised data practices
       would ease AI deployment across diverse platforms and healthcare systems.

   •   HCPs from Italy, Denmark and the UK, an AI developer from the USA, and the
       EU level association suggested creating a centralised data platform with
       standards in place to ensure interoperability, data quality and performance.

   •   Regulatory experts highlighted the importance of having clear interoperability
       standards to allow for the seamless integration of AI tools.
   •   A hospital representative from Belgium highlighted the importance of
       establishing cloud-based data-storage locations within Europe to facilitate data
       storage and sharing capabilities.
10.4.7.2 Clarity on regulatory processes

   •   69% of HCPs and 65% of hospital representatives highlighted the importance of
       having clear guidelines for product approval, accountability, and liability to
       ensure that AI tools can be implemented without ambiguity regarding their legal
       and ethical implications.

   •   AI regulatory experts highlighted the importance of harmonising existing
       regulatory frameworks, such as the EU AI Act and the Medical Device Regulation
       (MDR), without introducing additional complexities by providing clear and
       streamlined processes to reduce uncertainty and foster more confidence in AI
       adoption.

   •   An AI developer and a hospital representative from Japan advocated for better
       coordination between regulatory frameworks.

   •   Educational initiatives to better navigate regulations was suggested by one
       HCP from Denmark, the hospital representative from Belgium and one AI
       developer from the USA.

   •   The EU-level association and regulatory experts suggested establishing
       regulatory advisory bodies to guide professionals through the regulatory
       framework.

   •   An HCP from Netherlands proposed having specialised bodies to provide stages
       and checkpoints to ensure a tools' usefulness and public acceptance.

   •   Regulatory experts proposed providing clear guidance and coordination at the
       EU level through “regulatory sand oxes”.

   •   An AI developer and an HCP from the USA recommended developing a checklist
       of regulations along with guidelines for hospitals that want to develop AI
       tools.

   •   An AI developer and an HCP from the USA emphasised the importance of strong
       public-private relationships, for example with regulatory authorities to
       facilitate a bi-lateral flow of information between regulators and technology
       developers.

10.4.7.3 Consolidated funding and guidelines on reimbursement mechanisms

   •   65% of HCPs and 56% of hospital representatives called for targeted funding
       to prioritise AI-related projects, particularly those that focus on healthcare-
       specific challenges.

   •   A hospital representative from Belgium, an AI developer from Japan and an HCP
       from Denmark proposed government reimbursement mechanisms, for
       example, through higher payments or tax incentives for hospitals that deploy AI
       tools.

10.4.7.4 Common performance         testing   studies   to   assess   variations   in
         performance

   •   An HCP from Italy and the hospital representative from Belgium called for a
       common performance testing framework for AI solutions, particularly in
       areas like radiology and mammography, to enable the comparison of
       effectiveness, value, and efficiency gains across different AI products.
                                                 Deployment of AI in healthcare – Final Report


10.4.7.5 Centralised post-deployment monitoring of AI tools

    •   63% of HCPs and 44% of hospital representatives highlighted the importance of
        post-deployment monitoring mechanisms through centralized data collection
        to assess the ongoing effectiveness of AI tools.

    •   Three HCPs385 and one AI developer form the USA also recommended the
        strengthening of testing and monitoring mechanisms of AI tools post-
        deployment.

    •   A hospital representative from the USA highlighted the importance of having
        centralised monitoring and quality assurance plans to assess AI
        performance drifts post-deployment.

10.4.7.6 Redefining the healthcare workforce and promoting collaboration

    •   The HCP from Austria and one HCP from the USA emphasised the need to re-
        design hospital workflows and introduce new roles, such as data scientists
        and IT experts, within hospitals to enhance the understanding and transparency
        of AI tools and facilitate their integration into daily clinical practice.

    •   Four HCPs386 advocated for multidisciplinary collaboration to better guide AI
        development. The EU-level organisation and one hospital representative from
        Italy emphasised the need for multidisciplinary teams that include data
        scientists and data engineers to facilitate the transfer of information from
        developers to end-users.

    •   HCPs from Austria and the UK, and a hospital representative from Italy
        highlighted the need for the establishment of clinical champions who can
        mediate between developers and healthcare professionals, speaking the
        language of both to ensure smooth communication and collaboration.

10.4.7.7 Centres of excellence for AI in healthcare

    •   56% of hospital representatives indicated the importance of such centres to
        concentrate talent and resources, providing a dedicated space for research,
        training, and collaboration on AI-driven healthcare innovations.

    •   The EU-level organisation, one AI developer from the USA and the hospital
        representative from Belgium explained that actively involving HCPS both in
        the development and deployment of AI, listening to their concerns, and
        taking their feedback seriously helps foster trust between physicians and the AI
        development team.

    •   One HCP from Italy also suggested involving patients alongside HCPs in
        research projects to build awareness, acceptance and trust.

    •   An HCP from the UK suggested that national funding for AI centres, such as
        centres of excellence, should include requirements for training, post-deployment
        support, and performance testing protocols.

    •   Three HCPs387, three hospital representatives 388 and the AI developer from
        Germany recommended EU-level guidelines to facilitate the exchange of best



385 The HCP from Austria, one from the UK, one from the USA
386 HCPs from the Netherlands, Austria, one from Italy, one from the USA
387 HCPs from Spain and one from the UK, one form US
388 Hospital representatives from South Korea, Belgium and Italy.
        practices and experiences across different institutions to enhance the
        understanding and effectiveness of AI solutions.

    •   An HCP from the UK, one HCP from Italy, the hospital representative from the
        USA and one AI developer from the USA proposed creating centres of
        excellence to guide the deployment of AI, providing expert support to
        healthcare organisations for example with challenges related to regulation and
        capabilities.

    •   HCPs from Denmark and the USA, and an AI developer from the USA emphasised
        the importance of developing roadmaps to guide organisations through
        digital literacy and technology deployment via these centres of excellence.

10.4.7.8 Clear transparency and accountability mechanisms

    •   Regulatory experts stressed the importance of ensuring that the roles and
        responsibilities of AI usage in clinical practice are clearly defined.

    •   Regulatory experts highlighted the need for transparency in the training data
        used for AI models, especially in large language models (LLMs) via clear
        documentation of the datasets and methodologies used, to ensure
        regulatory compliance and build trust among healthcare providers and patients.

    •   One HCP from Denmark and one from Italy and two AI developers 389 suggested
        providing clear transparency and explainability guidance to help users
        understand how AI reaches clinical decisions.

10.4.7.9 Education and training programs to improve digital health literacy

    •   Regulatory experts highlighted the importance of training programs that are
        regularly updated to reflect the latest advancements of AI to ensure technological
        competence.

    •   An AI developer from Germany pointed out the importance of training
        healthcare professionals to use the AI solutions effectively, while one AI
        developer from the USA also noted the importance of in-person training during
        AI product demos at hospitals.

    •   Two HCPs from the UK, hospital representatives from Israel and the USA, and
        an AI developer from the USA proposed instating continuous training
        programmes for individuals, companies, and hospitals on AI solutions to ensure
        accountability, ongoing learning across the healthcare system and bolster
        confidence in adoption.

    •   Two HCPs390, the hospital representative from the USA two AI developers 391
        highlighted the need to educate the population and HCPs on AI's role as a
        supportive tool for augmentation, rather than replacement to improve trust in AI
        tools.

10.4.8 Conclusions

AI holds significant promise in addressing key healthcare challenges such as
administrative burden, workforce shortages, and the need for improved technology
infrastructure. Stakeholders agree that AI can streamline administrative tasks, reduce
non-clinical workloads, and enhance overall workflow efficiency, allowing healthcare


389 AI developer from the Netherlands, one from the US
390 One HCP from UK, one from Denmark
391 AI developers from Netherlands and Germany
                                           Deployment of AI in healthcare – Final Report


providers to focus more on patient care. AI's role in diagnostics, particularly in fields
like radiology and pathology, is widely recognised for improving accuracy and speeding
up results, which helps to alleviate the impact of workforce shortages and optimise
hospital operations.

Looking ahead, AI's potential extends beyond current capabilities, with opportunities in
personalised medicine, real-time decision-making, and hospital-wide optimisation.
Stakeholders anticipate that AI will improve healthcare accessibility, particularly in
underserved regions, and enhance doctor-patient relationships through clearer
communication. While challenges remain, such as concerns over false positives and
infrastructure limitations, AI is expected to play a transformative role in healthcare,
improving patient outcomes and operational efficiency across diverse medical fields.

The integration of AI into healthcare is faced by a number of challenges, ranging from
technical issues like data standardisation and interoperability to regulatory, ethical, and
operational complexities. Key hurdles include fragmented healthcare data, outdated IT
infrastructures, and a lack of clear regulatory and performance testing procedures for
AI tools. Moreover, the complexity of the regulatory landscape, particularly in the EU
with frameworks like the AI Act and GDPR, poses a steep learning curve for healthcare
providers and AI developers alike. These challenges not only affect the deployment of
AI but also raise concerns about data privacy, cybersecurity, and trust among healthcare
professionals.

However, there are promising practices emerging globally that can help address these
challenges. Collaborative data infrastructures and centralised data entities to overcome
data fragmentation, and pilot projects have been useful in testing AI integration into
existing workflows. Hospitals have shown success by adopting single platforms to
consolidate AI solutions, while countries like the UK and Japan are pioneering regulatory
innovations like fast-track approval processes and digital regulation platforms.

Investing in IT upgrades, fostering multidisciplinary collaboration, and promoting
training programs for both HCPs and AI developers are important steps for the
successful deployment of AI in healthcare. Hospitals are exploring various strategies,
such as involving end-users in AI development, implementing cost-benefit analyses, and
creating internal review boards to assess AI tools' regulatory compliance and liability.
Addressing concerns about transparency and explainability of AI is also essential for
building trust, with various initiatives emphasising the importance of clear
communication and the continued human oversight of AI tools.

Moving forward, establishing a centralised body for AI assessment, local performance
testing, and post-deployment monitoring would standardise evaluation processes and
improve oversight. A structured local performance testing framework would enable
performance benchmarking and address variations in performance across healthcare
settings, while centralised monitoring mechanisms would track AI tool effectiveness
over time, ensuring ongoing quality and compliance. In addition, centres of excellence
for AI in healthcare could serve as dedicated hubs for research, training, and
implementation support. These centres could provide expertise on regulatory
compliance, digital adoption strategies, and best practices, ensuring AI solutions align
with healthcare needs. Multidisciplinary collaboration would further support knowledge
transfer and stakeholder engagement. Developing common standards for data
governance, privacy, and interoperability, as well as consolidated funding and structured
financing mechanisms would facilitate AI integration across healthcare systems.
Targeted investment, reimbursement models, and financial incentives would encourage
deployment while ensuring long-term sustainability. Additionally, developing a
comprehensive AI solutions catalogue would improve transparency and assist
healthcare providers in selecting appropriate technologies. These initiatives collectively
could support a structured and scalable approach to AI integration in healthcare.
     10.5 Annex 5 – Details on data sources and methodology for
          market analysis
10.5.1 Research

An examination of the number of results on the academic library Scopus 392 for the search
terms “Artificial Intelligence” and “healthcare” already provides an indication of the vast
amount of literature and ongoing research on this topic. A search within article titles,
abstracts, and keywords using the search string “(“Artificial intelligence” AND
healthcare)” yields 21,055 documents on the topic, with numbers skyrocketing after
2020, as 84% of the results pertain to publications from that date onward. However,
significantly fewer papers are retrieved when one includes the words “Clinical practice”
in the search string (1,188 results, i.e. only 5.6%).

The Community Research and Development Information Service393 (CORDIS)
database, serves as a proxy to indicate and evaluate research advancements in the
field, as it highlights those areas where research projects are initiated. The search string
using the key terms “Artificial Intelligence” and “healthcare” results in a list of 553
funded research projects over the past 10 years (covering projects launched from
2014 to the present). The majority were initiated from 2019 onwards, beginning with
33 projects in 2015 and peaking at 85 projects in 2022 (Figure 7). Specifically, the
number increased consistently from 2019 to 2022, indicating a momentum for AI
research in healthcare during those years.

To provide estimates of patents in medical AI, we used data from the European Patent
Office (EPO), which provides data on patents covering all EU27 Member States and the
UK through Espacenet394. Espacenet is a structured public repository managed by EPO,
and it provides free access to over 120 million patent documents from around the world,
including technical information, patent classifications, bibliographic data, and legal
statuses. General patenting trends throughout the years and the country of patents’
applicants are described in the following paragraphs. We used the same search string,
with the terms “Artificial Intelligence” and “healthcare” over the past 10 years. The
search provided 675 results of patents, with the majority of patents being filled from
2019 onward. As exhibited in Figure 26, there was a significant increase from 22 patents
in 2017 to 118 in 2023 (representing a five-fold increase). It is also important to note
that an all-time high has been already reached in year 2024 with 122 patents. This
steady increase highlights a growing focus on AI/ML-enabled medical devices in recent
years.




392 Scopus is a scientific abstract and citation database, launched by the academic publisher Elsevier.
Available at: https://www.scopus.com/search/form.uri?display=basic&zone=header&origin=#basic
393 CORDIS is the European Commission’s primary source of results from the projects funded by the EU’s
framework programmes for research and innovation. It has a structured public repository with all project
information held by the European Commission such as project factsheets, participants, reports, deliverables
and links to open-access publications. Available at: https://cordis.europa.eu/about
394 Espacenet is a structured public repository managed by EPO, and it provides free access to over 120
million patent documents from around the world, including technical information, patent classifications,
bibliographic data, and legal statuses. Available at: https://worldwide.espacenet.com/
                                                       Deployment of AI in healthcare – Final Report


      Figure 26: Number of patents on AI in healthcare published each year (2014-2024)*




* The number of patents published in 2024 is based on data last accessed on 13/11/2024 and may therefore
be higher.

                        Source: Authors’ elaboration based on Espacenet database.

As a final factor to estimate trends in term of research in AI in clinical practice, the study
team also analysed available data on AI/ML-enabled medical devices in clinical trials.
As part of clinical trials, medical devices are also tested to evaluate their effects on
human health outcomes as a prior step to get regulatory approval and eventually be
deployed. In this regard, various clinical trial registries exist to ensure that a
comprehensive view of research is accessible to all stakeholders involved in healthcare
decision-making. The European Union Clinical Trials Register395 allows to search for
protocols and results information on interventional clinical trials that were approved in
the EU/EEA under the Clinical Trials Directive 2001/20/EC. Our search involved
identifying clinical trials on AI/ML-based interventions using the terms ‘“Artificial
Intelligence” OR “Machine Learning”’ over the past 10 years (covering clinical trials
conducted from 2014 to the present) and provided only 13 results. It should be noted
that, starting of January 31st, 2023, and by January 30th, 2025, all initial clinical trial
applications in the EU/EEA must be submitted through the Clinical Trials Information
System. The latter date marks the end of a three-year transition period that began when
the Clinical Trials Directive (EC) No. 2001/20/EC became applicable in the EU. The
Clinical Trials Regulation (CTR) harmonised the processes for assessment and
supervision of clinical trials throughout the EU. Under the CTR, clinical trial sponsors
must submit all new clinical trial applications in the abovementioned Clinical Trials
Information System396 (CTRI). Our search involved identifying clinical trials on AI/ML-
based interventions using the search terms ‘“Artificial Intelligence” OR “Machine
Learning”’ over the past 10 years (covering clinical trials conducted from 2014 to the
present) and, not much differently from the search based on the EU Clinical Trials
Register, provided only 12 results.

The WHO International Clinical Trials Registry Platform 397 (WHO ICTRP) aims to
provide a single point of access to information about ongoing and completed trials. The
WHO ICTRP compiles data from national and regional clinical trial registries worldwide,
including ClinicalTrials.gov (USA), the EU CTRI, the Chinese Clinical Trial Registry, and
the Japan Primary Registries Network. Thus, trial data from various countries is


395 https://www.clinicaltrialsregister.eu/ctr-search/search
396 https://www.ema.europa.eu/en/human-regulatory-overview/research-development/clinical-trials-
human-medicines/clinical-trials-information-system
397 The WHO ICTRP provides a searchable database containing the trial registration data sets made available
by data providers around the world meeting criteria for content and quality control. It compiles data from
national and regional clinical trial registries worldwide, including ClinicalTrials.gov (USA), the EU Clinical Trials
Register, the Chinese Clinical Trial Registry, and the Japan Primary Registries Network. Available at:
https://www.who.int/clinical-trials-registry-platform
centralised, allowing for broader access and comparison. Our objective was to identify
clinical trials involving AI/ML-based interventions. Given that clinical trials already
pertain to the healthcare domain, the search string was changed accordingly, and we
carried out two separate searches: one for ‘Artificial Intelligence’ and one for ‘Machine
Learning,' covering the past 10 years (from 2014 to the present). These two searches
combined provided a total of 3,320 results between 2014 and 2024.

10.5.2 Development

Once a medical device has been developed, manufacturers in the EU and in the US must
comply with respective laws and regulations before legally placing a medical device on
the market. The situation on the regulatory approval of medical devices presents
differences between the US and the EU. While the EU has a single competent authority
handling the approval and monitoring of pharmaceuticals and biologics, the European
Medicines Agency (EMA), there is no centralised authority for medical devices.
The approval process relies instead on Notified Bodies, i.e., organisations designated
by an EU Member State (or by other countries under specific agreements) to assess the
conformity of certain products before being placed on the market. As of October 2024,
there were 50 Notified Bodies designated under the Medical Device Regulation
(MDR)398. Given the relative novelty of AI in medical devices, there is no current
standard and specific categorisation of AI/ML-enabled medical devices.
Although it should be noted that some of the notified bodies are increasingly specialising
in assessing whether manufacturers meet the state-of-the-art requirements for AI-
driven medical devices, aiming to minimise regulatory compliance issues during
certification, surveillance audits, and technical documentation reviews 399.
Moreover, in the EU, while AI-enabled medical technologies must generally comply with
regulatory requirements applicable to all medical devices, there are at present no
harmonised standards that specifically address the unique performance aspects of AI
technologies400. Thus, efforts to study CE-marked medical devices in Europe may be
impacted by the lack of a publicly accessible register of approved devices, the
confidentiality of information submitted to Notified Bodies and regulators, and the
decentralised process for CE-marking decisions401,402. According to the MDR, there are
four different classes of medical devices depending on the risk level of the product
(described in detail in section 5.1.4): class I low risk, class IIa low/medium risk, class
IIb medium/high risk, and class III high risk 403. Whereas a class I CE mark is obtained
through self-certification, classes II and III necessitate an external evaluation by a
notified body, which entails a more complex process that also includes the review of
results404.
As part of the updated Medical Devices Regulation (MDR)405, the Commission set up
the objective of establishing a centralised EU database on CE-marked medical devices


398 Fink and Akra, 2023. Comparison of the international regulations for medical devices–USA versus
Europe.
399 See for example: https://www.tuvsud.com/en/industries/healthcare-and-medical-devices/artificial-
intelligence-in-medical-devices
400 TÜV SÜD, 2021. Artificial Intelligence in Medical Devices. Verifying and validating AI-based medical
devices. White Paper.
401 Hwang et al., 2016. Comparison of rates of safety issues and reporting of trial outcomes for medical
devices approved in the European Union and United States: cohort study.
402 Kramer and Kesselheim, 2012. How does medical device regulation perform in the United States and
the European union? A systematic review.
403 For more information, please refer to : https://webgate.ec.europa.eu/udi-helpdesk/en/other-relevant-
information/medical-device-classification.html (Last accessed 10/10/2024).
404 Van Leeuwen et al., 2021. Artificial intelligence in radiology: 100 commercially available products and
their scientific evidence.
405 https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32017R0745
                                                  Deployment of AI in healthcare – Final Report


in the EU – the European Database on Medical Devices (EUDAMED). Notably,
Article 34 established the gradual roll out of EUDAMED which was initially set to become
fully operational in May 2022. The full functionality has not been achieved yet, with the
Commission postponing the mandatory use of EUDAMED to early 2026. The information
included in the database is therefore updated on a voluntary basis by medical
devices manufacturers and is therefore not comprehensive.
Conversely, in the United States, the FDA oversees the regulation of medical devices,
pharmaceuticals, and biologics. The FDA provides publicly accessible information on
approved medical devices through summary documents that include details about
the device description, indications for use, and performance data from the device's
evaluation study406. Given the lack of data available on CE-marked devices, for our
analysis on developed AI/ML-enabled medical devices we have analysed the data
provided by the FDA.
Before medical hardware or software can be legally introduced to the US market, the
parent company must submit it to the FDA for evaluation407. Depending on the devices'
risks, the FDA centrally approves medical devices through three pathways: the
premarket approval pathway (the most rigorous review for high-risk devices), the
de novo premarket review (for low and moderate-risk devices), and the 510(k)
pathway, each of which needs specific criteria to be fulfilled in order to be granted to be
granted (see Table 11)408. For simplicity, we use "approval" to denote the clearance of
these devices.
 Table 11: Description of the types of FDA approvals for AI/ML-based medical technologies
 Level of FDA                 Description
 clearance
                              A 510(k) clearance for an algorithm is granted when it has been
                              shown to be at least as safe and effective as another similar, legally
                              marketed algorithm. The submitter seeking this clearance must
                              provide substantial proof of equivalence in their application.
                              Without an approval of being substantially equivalent to the other
 510(k) clearance
                              algorithm, the one pending approval cannot be legally marketed.
                              An example of AI/ML-based medical technology that has been
                              approved through the 510(k) clearance is a deep-learning model
                              used in radiology which accelerates MRI scans by up to 50% by
                              enhancing low-quality initial outputs from accelerated scans.
                              Premarket approval is issued to algorithms for Class III medical
                              devices. The latter are those that can have a large impact on
                              human health as such, their evaluation undergo more thorough
                              scientific and regulatory processes to determine their safety and
                              effectiveness. To approve an application, the FDA determines that
                              the device’s safety and effectiveness is supported by satisfactory
 Premarket approval
                              scientific evidence. Upon approval, the applicant can proceed with
                              marketing the product. An example of AI/ML-based medical
                              technology that went through the FDA’s premarket approval is a
                              breast imaging system used in radiology which provides
                              substantially improved confidence in breast cancer diagnostics
                              thanks to a non-invasive, real-time ultrasound scan.
                              Regarding the de novo classification, it is used to classify those
                              novel medical devices for which there are no legally marketed
 De novo pathway              counterparts, but which offer adequate safety and effectiveness
                              with general controls. The FDA performs a risk-based assessment
                              of the device in question before approval and allowing the device to


406 Wu et al., 2021. How medical AI devices are evaluated: limitations and recommendations from an
analysis of FDA approvals.
407 Benjamens et al., 2020. The state of artificial intelligence-based FDA-approved medical devices and
algorithms: an online database.
408 Muehlematter et al., 2021. Approval of artificial intelligence and machine learning-based medical
devices in the USA and Europe (2015–20): a comparative analysis.
                              be marketed. An example of AI/ML-based medical technology that
                              has been approved through the de novo pathway is an end-to-end
                              approach used in cardiology for detecting and directing
                              hypertrophic cardiomyopathy patients.
                 Source: Authors’ elaboration based on Benjamens et al. (2020)
For the development and marketing of medical algorithms, the FDA’s stringent
regulatory requirements currently pose important challenges to the companies
developing them. In the past, every new product had to go through the regulatory
process. However, as companies update their algorithms on a much shorter time scale,
namely in days, the FDA has realised that this process might become impossible to
maintain409. Therefore, the FDA started to consider “a total product lifecycle-based
regulatory framework for these technologies that would allow for modifications to be
made from real-world learning and adaptation, while still ensuring that the safety and
effectiveness of the software as a medical device is maintained” 410.
In the figure below we provide the monthly approvals of FDA medical devices in the US
between January 2021 and May 2024.
 Figure 27: Number of FDA approvals of AI/ML-enabled medical devices between 2021 and
                                   2024 (per month)




                          Source: Authors’ elaboration based on FDA database



10.5.3 Deployment

The Radiology Health AI Register411 is an online overview of CE-marked AI products
based on vendor-supplied product specifications created by a research team from the
Department of Medical Imaging at the Radboud University Medical Center (The
Netherlands). To build the register, first the team at Radboud University Medical Center
mapped and reviewed AI software products from exhibitor lists from the Radiological
Society of North America (RSNA) and European Congress of Radiology (ECR) as well as
marketplace offerings. Additionally, news sources were monitored to identify the
emergence of new vendors, products, or certifications 412. In a second step, a

409 Benjamens et al., 2020. The state of artificial intelligence-based FDA-approved medical devices and
algorithms: an online database.
410 Regulations.gov, 2019. Proposed Regulatory Framework for Modifications to Artificial
Intelligence/Machine Learning (AI/ML)-Based Software as a Medical Device (SaMD) – Discussion Paper and
Request for Feedback. https://www.regulations.gov/document/FDA-2019-N-1185-0001
411 The database can be accessed via the following link: www.radiology.healthairegister.com (Last
accessed 10/10/2024).
412 Van Leeuwen et al., 2021. Artificial intelligence in radiology: 100 commercially available products and
their scientific evidence.
                                                Deployment of AI in healthcare – Final Report


comprehensive assessment was carried out on the existing scientific literature on the
identified products, gathering details such as their modality, subspeciality, main task,
regulatory information, deployment, and pricing model. In a final step, vendors for these
products were contacted to verify the information collected. According to the authors,
the Register is currently the most comprehensive overview of available AI-based
software for clinical radiology practice. We believe that the data on AI medical devices
in the field of radiology could work as a good proxy on the number of CE-marked AI
medical devices given that the majority of medical devices are developed for this
medical specialisation.
As can be seen in Figure 28, the majority of devices were developed by organisations
based in France (12 out of 50, 24%), followed by Israel (5 devices, 10%), South Korea
(4 devices, 8%), Lithuania, Spain and the United States (each of them with 3 devices,
6%). The remaining countries, as observed in the graph below, accounted for 20 devices
(40% of the total).
Figure 28: Number of medical devices for clinical radiology on the market per origin country
                                  of the manufacturer

                France
                 Israel
          South Korea
        United States
                 Spain
             Lithuania
      United Kingdom
             Romania
                   Italy
                  India
             Denmark
                Austria
            Singapore
              Portugal
             Germany
               Czechia
                 China
               Canada
              Bulgaria
             Australia
                           0                5                     10                     15

                Source: Authors’ elaboration based on the Radiology Health AI Register
Results in Figure 29 show that available AI products mostly addressed chest radiology
(15, i.e. 30% of 50 devices), followed by neuroradiology (10 devices, i.e. 20%),
musculoskeletal (MSK) radiology (9 devices, i.e. 18%), abdomen radiology (7 devices,
i.e. 14%), and cardio radiology (7 devices, i.e. 14%).
Figure 29: Number of medical devices for clinical radiology on the market per subspeciality




               Source: Authors’ elaboration based on the Radiology Health AI Register

Regarding the modalities, we observe that products are distributed over CT (34%, 17
out of 50 devices), MR and X-ray (each of them accounting for 13 devices, 26%),
ultrasound (4 devices, 8%), and mammography (3 devices, 6%). These figures are in
line with the results of a 2024 survey among members of the European Society of
Radiology, whereby AI impact was predominantly expected on breast and oncologic
imaging, primarily involving CT, mammography, and MRI 413. The extensive use of AI
tools for CT is justified by the high volume of imaging data it generates and its critical
role in diagnosing complex conditions, making it ideal for leveraging AI to enhance
accuracy and efficiency414.
In terms of tasks performed, the main ones are diagnostic tasks (39 devices, 78%),
AI-assisted prognosis prediction and risk stratification (18%, 9 out of 50 devices), and
AI-assisted symptom checker and support in treatment decisions (4%,2 out of 50
devices). AI devices, in this regard, are particularly helpful for diagnostic tasks as they
excel at analysing complex imaging data to detect abnormalities with high accuracy 415.




413 Zanardo et al., 2024. Impact of AI on radiology: a EuroAIM/EuSoMII 2024 survey among members of
the European Society of Radiology.
414 Mello-Thoms and Mello, 2023. AI in imaging and therapy: innovations, ethics, and impact: review
article.
415 Mello-Thoms and Mello, 2023. AI in imaging and therapy: innovations, ethics, and impact: review
article.
                                              Deployment of AI in healthcare – Final Report


   Figure 30: Number of medical devices for          Figure 31: Number of medical devices for
 clinical radiology on the market per modality       clinical radiology on the market per main
                                                                     functionality




              Source: Authors’ elaboration based on the Radiology Health AI Register

Regarding the class of approval, 25 out of the 50 products (50%) are marked with IIa
risk class, 13 of them (26%) with IIb risk class, and 12 devices (24%) with I risk class,
showing that AI in radiology is mostly used for devices with low and medium risk levels.
Additionally, 20 out of 50 analysed medical devices also obtained a class II approval via
the 510(k) pathway from the FDA.
The Register also provides commercial information for 26 out of the 50 medical devices
that had been CE-marked between January 2021 and June 2024. The 26 AI medical
devices were in use in 11 different countries. In these countries, there were 201
paying customers who were using the devices for clinical purposes while 19 were using
them for research or for testing. This distinction was made since many companies tend
to claim that they have deployed their technology in several centres when, in reality, it
is just for performance testing studies or free installation for a specific doctor to test the
tool.
Lastly, the Radiology AI Health Register also provided information on the type of
integration needed for the deployment of each of the AI medical devices listed. In this
case there were also some pre-defined categories of integration: integration in standard
reading environment (PACS); integration in Radiological Information System (RIS);
integration in Clinical Information System (CIS); integration via AI marketplace or
distribution platform; stand-alone third-party application; stand-alone web based; and
embedded on the MRI console. There was information available for 48 out of the 50
analysed AI medical devices. It was also the case that the AI tools could be integrated
via various of the integration options, while the majority of analysed AI tools could be
integrated via PACS (83%, 40 out of 48 devices). The second most available option for
integration was via AI marketplace or distribution platform (58%) followed by
integration in RIS (44%). In the figure below we provide an overview on the information
provided for each integration model. This provides evidence that the adoption of AI in
radiology may be facilitated by the fact that there are available several standard
information systems to which AI tools can be easily adapted to.
    Figure 32: Type of integration model for the analysed AI medical devices in radiology
                                    1
                                                                     Integration in standard
                                                                     reading environment (PACS)
                            16
                                                                     Integration RIS (Radiological
                                                   40                Information System)
                                                                     Integration CIS (Clinical
                 19                                                  Information System)
                                                                     Integration via AI marketplace
                                                                     or distribution platform
                                                                     Stand-alone third party
                                                                     application
                                                                     Stand-alone webbased
                      28                         21

                                        8                            Embedded on the MRI console




               Source: Authors’ elaboration based on the Radiology Health AI Register


10.5.4 Overall data limitations and challenges

Some limitations need to be mentioned regarding the approach followed for the market
analysis conducted in the context of this study. Firstly, detecting FDA-approved and CE-
marked AI/ML-based medical devices is challenging, as the use of the terms
associated with AI/ML on anufacturers’ we sites and in news articles ight
be different. This inconsistency may also contribute to a lower number of detected
AI/ML-based devices. Moreover, as already mentioned throughout the text, the EU
lacks a comprehensive database for CE-marked medical devices, significantly
hindering the transparency of the CE-marking process in the EU.

Concerning the FDA database of AI/ML-based devices approved, it should be noted that
the number of FDA-approved devices does not provide insights into whether these
devices are deployed in practice. Conversely, there may be AI/ML-based medical
devices developed and used internally within hospitals or research institutions
without obtaining approval416. Hence, although FDA approval permits commercial
distribution, we cannot assess the actual availability and clinical deployment of these
devices in healthcare facilities, making it challenging to evaluate the real-world impact
of AI/ML devices417. Secondly, the FDA does not require companies to label their
technology as AI/ML-based, even if it is: while some companies disclose that their
technology is AI/ML-based in their FDA approval announcements, including the specific
ML methods used, others do not provide this information 418. Moreover, because of the
strong incentives for companies to market and sell their devices as widely as possible,
some devices might contain references to AI/ML to be more attractive on the
market, although they are not fully AI/ML-based419.

Similarly, concerning the Radiology Health AI Register, defining AI and its role in
clinical radiological practice is quite complex, making the criteria for product

416 Muehlematter et al., 2021. Approval of artificial intelligence and machine learning-based medical
devices in the USA and Europe (2015–20): a comparative analysis.
417 Zhu et al., 2022. The 2021 landscape of FDA-approved artificial intelligence/machine learning-enabled
medical devices: An analysis of the characteristics and intended use.
418 Benjamens et al., 2020. The state of artificial intelligence-based FDA-approved medical devices and
algorithms: an online database.
419 Muehlematter et al., 2021. Approval of artificial intelligence and machine learning-based medical
devices in the USA and Europe (2015–20): a comparative analysis.
                                          Deployment of AI in healthcare – Final Report


inclusion debatable. For instance, products that analyse cardiac ultrasound were
excluded from the database, as these are frequently associated with cardiology.
Moreover, some vendors did not respond to the authors’ requests for information or
opted not to be included, choosing to retain some information. In addition, vendors
often do not specify on their websites whether their products carry a CE mark
and, even when they do, they do not specify which risk class applies. For some products,
the missing information was completed with public data where possible. Therefore, while
the website aims to offer a continually updated overview of AI radiology products and
is maintained voluntarily by the study team, the database cannot be regarded as
comprehensive and complete as an official governmental database (e.g. the FDA
database).
In light of the above, it is important to note that our analysis primarily focused on FDA-
approved devices and CE-marked AI tools used in radiology that are available on the EU
market. This scope significantly limits the generalisability of our conclusions.
Moreover, while these indicators demonstrate whether the tools are commercially
distributed, they do not provide insight into their actual availability or clinical
deployment in healthcare facilities, making it challenging to assess the real-
world impact of AI/ML devices.
To fill such gaps, insights from the survey results were included in the analysis,
although there were also some limitations concerning the data collection and analysis
of such responses as well. In particular, the responses come from a limited number
of stakeholders which cannot be considered as representative sample to assess the
actual state of deployment of AI medical devices in the EU. Hence, the analysis provided
works as an estimation on the deployment of healthcare, but the analysis needs to be
interpreted carefully without leading to significant conclusions.
    10.6 Annex 6 – List of specific actions for each consideration for
         future action
             Recommendations                                            Specific actions

                                                     Rules to standardise data formats, protocols and
                                                     metadata
Establishing common standards for data
                                                     Standards on mechanisms to support real-time data
governance, privacy, and interoperability
                                                     exchanges
                                                     Incentives to adopt interoperable technologies
                                                     Actual establishment of Centres of Excellence of AI in
                                                     healthcare
                                                     Provision of advanced training programmes for
                                                     healthcare workforce
                                                     Run digital health literacy programmes for the general
Establishment of Centres of Excellence for AI
                                                     public
healthcare
                                                     Creation of a collaborative environment for knowledge
                                                     and best practice sharing
                                                     Drafting of guidelines on data governance and privacy
                                                     Drafting of protocols to identify and mitigate biases in
                                                     AI models
                                                     Introduction of financing mechanisms to support
Consolidated funding     and   introduction     of   strategic priorities for AI in healthcare
financing mechanisms                                 Introduction of standardised EU-level reimbursement
                                                     framework for AI in healthcare
                                                     Establishment of a network of assurance labs to test
                                                     the performance of AI tools for healthcare
                                                     Provide standardised infrastructure for evaluating AI
                                                     models at local/regional level
                                                     Establishment of performance benchmarks designed for
                                                     different AI tools to be used by local performance
                                                     testing centres
                                                     Provision of sandbox environment to test the
                                                     performance of AI tools
Establishment of a centralised body for added-
                                                     Promote collaboration across EU Member States with a
value assessment, local performance testing
                                                     central data repository
and post-deployment monitoring of AI solutions
                                                     Value proposition research activities using evidence-
                                                     based frameworks to quantify and articulate the
                                                     specific benefits of AI tools
                                                     Collection and dissemination of real-world evidence and
                                                     case studies demonstrating the practical effectiveness
                                                     and impact of AI tools
                                                     Establishment of a centralized governance body to
                                                     oversee the implementation and refinement of the
                                                     evaluation model
                                                     Inclusion of detailed performance metrics for each
                                                     listed AI tool, user reviews, and feedback mechanisms
                                                     Inclusion of user guides, case studies, and tutorials,
Development of a catalogue of AI solutions           helping healthcare providers understand and implement
                                                     AI solutions effectively
                                                     Establishment of a governance framework to oversee
                                                     the catalogue’s operations
                                                     Deployment of AI in healthcare – Final Report


     10.7 Annex 7 – Triage Use Case – Case Study 1
This case study report focuses on an AI solution used in cardiology for triage purposes
that has been developed by a large enterprise and has been approved by the U.S. Food
and Drug Administration (FDA), the Therapeutic Goods Administration (TGA) of
Australia, and has a European Conformity marking (CE marked) and deployed in
healthcare settings globally. To provide an overview of the AI solution, we conducted
desk research and in-depth interviews with 5 selected stakeholders:

    •    the developer of the AI solution from Israel,
    •    1 healthcare professional from the USA using the AI solution,
    •    1 healthcare professional from Sweden using the AI solution,
    •    1 representative of a hospital from Israel that has deployed the AI solution,
    •    1 representative of a hospital from Belgium that has deployed the AI solution.

The insights gathered contribute to building an overall picture of the use case and its
impact, in addition to gathering information on the challenges and good practices
employed in its deployment in healthcare settings.

10.7.1 Overview of the need

Pulmonary Embolisms (PE), a form of Venous Thromboembolisms (VTEs), are potentially
life-threatening conditions that require timely and accurate diagnosis for effective
treatment. PE is the third most common cause of cardiovascular death in the United
States, with an annual mortality rate of 100,000 420. Diagnosing PE often requires a
specific type of Computed Tomography (CT) scan called a CT Pulmonary Angiogram
(CTPA). PE’s can be prone to missed or delayed diagnosis due to their often-varied
clinical presentations, making them challenging to detect. In some cases, PEs are
detected in routine chest imaging procedures without the presence of symptoms which
are referred to as incidental PEs 421. Approximately 44.8% of incidental PEs are not
detected by radiologists, with miss rates ranging from 32% to 79% 422.

The treatment of PE varies depending on the size, location of the embolus, and the
patient's overall risk factors for thromboembolic events such as strokes and heart
attacks. Treatment options vary from anticoagulants in less urgent cases to surgery in
more urgent and serious cases. Having a multidisciplinary team, such as a Pulmonary
Embolism Response Team (PERT)423, is the most effective approach to developing
personalized treatment plans for patients at risk of PE or with a suspected PE (see figure
below). Despite such benefits, 75% of PE patients still receive standard bedside
treatments such as anticoagulants irrespective of PE severity, rather than being referred
to a PERT for personalised care.




420 Rothenberg SA, Savage CH, Abou Elkassem A, et al. 2023. Prospective Evaluation of AI Triage of
Pulmonary Emboli on CT Pulmonary Angiograms.
421 Incidental PEs are found unexpectedly during imaging tests (like CT scans) performed for reasons
unrelated to PE suspicion. For example, a patient might undergo a CT scan for cancer staging or abdominal
pain, and a PE is noticed on the scan. Patients with incidental PE typically do not present with the classic
symptoms associated with PE. Although these PEs are found by chance, they can still be clinically significant.
422 Topff L, Ranschaert ER, Bartels-Rutten A, et al. 2022 Artificial Intelligence Tool for Detection and Worklist
Prioritization Reduces Time to Diagnosis of Incidental Pulmonary Embolism at CT
423 A PERT often includes emergency physicians, radiologists, pulmonologists, cardiologists and vascular
surgeons.
Figure 33: Impact of a PERT on the number of personalised procedures, intensive care unit
                             days, and overall length of stay.


The workload of radiologists has increased over the past decades with reports showing
a higher demand and complexity of imaging examinations. This has led to backlogs of
unreported examinations, especially during unexpected surges in imaging requests. The
detection of incidental PEs, where patients do not present with classic symptoms, can
be particularly challenging under these conditions, due to the requirement for careful
review of CT scans, often in a high-pressure environment. This can result in delays in
identifying both non-urgent and urgent cases of PEs, and a subsequent delayed time to
treatment424. This can compromise the prognosis of patients, as evidence suggests that
the survival outcome is directly linked to the speed of intervention, with one study
reporting that in the most severe cases up to 10% of PE patients can die within the first
hour following the onset of symptoms.

Recent studies highlight the potential for Artificial Intelligence (AI)-enhanced PERT
workflows to help prioritize the most urgent and serious cases for personalised
treatments and increase efficiencies in healthcare delivery by enhancing patient
outcomes, reducing hospital stays and optimizing the cost of PE triage and treatment.

10.7.2 Overview of the use case

The AI solution is a platform that assists in the rapid diagnosis, prioritisation, and
treatment of PEs by reviewing CT scans and streamlining communication and
coordination among multidisciplinary teams, facilitating timely decision-making and
patient care. The AI solution is used both for patients that present with symptoms of
PE, and in patients at risk of incidental PE, for example patients undergoing surgery,
immobilized patients following surgery, long term hospitalizations and patients with
specific conditions (i.e. heart disorders, chronic disorders, cancer, history of
thrombolytic events) 425. The AI solution assists radiologists in the detection of PE, risk
stratification and post treatment patient management.

Studies indicate that the AI solution has improved time-sensitive outcomes, such as the
time required for radiologists to interpret and report the findings of CT scans known as
turn-around time, time to treatment, wait time, and length of stay of patients with PEs.
It has also shown to affect the quality of radiological interpretations such as the
diagnostic accuracy, the sensitivity and specificity, and the overall coordination and
collaboration of healthcare professionals involved in patient care.

10.7.3 Challenges to Deployment

10.7.3.1 Technical and Data Challenges

The AI developer described several technological and data challenges, particularly in
Europe. One of the main barriers is the reluctance of healthcare providers to use
cloud services, with a preference for local servers. While there are often concerns


424 Topff L, Ranschaert ER, Bartels-Rutten A, et al. 2022 Artificial Intelligence Tool for Detection and Worklist
Prioritization Reduces Time to Diagnosis of Incidental Pulmonary Embolism at CT
425 American Heart Association. 2023. Risk Factors for Venous Thromboembolism
                                          Deployment of AI in healthcare – Final Report


surrounding the security of cloud services, the hospital representative from Israel
reported that there is a common belief that data in the cloud is less secure than
on-premises data.

While it was not specifically flagged as a concern during the deployment process, the AI
developer noted that interoperability is lacking between advanced AI solutions
and existing hospital systems. This problem is attributed to the incomplete
implementation of electronic health records (EHRs) and the fragmented digital
health infrastructure, which creates obstacles to seamless integration and data sharing.
Additionally, according to the developer of the AI solution, the high costs associated
with integrating AI solutions, partly due to the lack of standardized processes across
healthcare systems, presented a significant challenge. This challenge of interoperability
was also raised by the healthcare professional from a hospital in Sweden. According to
them, interoperability, and successful integration of AI solutions is a complex
and time-consuming process. The healthcare professional from Sweden reflected
that increased interoperability of solutions may help overcome this obstacle.

The hospital representative from Israel reflected on the fragmentated market of AI
solutions, with many companies developing niche algorithms for specific tasks. For
hospitals who want to integrate AI solutions, they must contract with numerous
companies and integrate diverse solutions using limited IT resources which is
impractical.

The challenges surrounding post-deployment monitoring mechanisms were also
raised by the hospital representative from Israel. According to the interviewee one of
the key issues debated is whether AI companies should be mandated to have an
annual review of the performance of their products. The Israeli hospital
representative emphasized the importance of ensuring that the training data
reflects the patient population that the AI solution will be used on. This is crucial
because the performance promised by the vendor (i.e., the developer of the AI solution)
may not be the same when deployed in a different healthcare setting.

10.7.3.2 Legal and Regulatory Challenges

The developer of the AI solution stated that the complex regulatory landscape in Europe
is an obstacle to deployment. While the solution successfully obtained a CE marking,
the stringent regulatory requirements posed some challenges. More specifically, the
interviewee highlighted that it could take significant time to gather data, creating a
barrier to market entry, especially for smaller startups.

In combination with the aforementioned challenges related to the reluctance towards
use of cloud services, the healthcare professional from a hospital in Sweden highlighted
the complexity surrounding cloud computing regulations. The interviewee stated that
varying rules regarding the use of cloud services for medical data complicates
the standardization of AI deployment across multiple sites.

Concerns surrounding liability due to AI errors were raised by the hospital
representative from Belgium and the healthcare professional from the hospital in
Sweden. The healthcare professional emphasized such concerns particularly in cases of
discrepancies between AI-generated results and radiologists' diagnoses, especially if a
mistake leads to adverse patient outcomes. He added that hospitals may have
varying tolerance levels for AI's confidence in diagnoses.

10.7.3.3 Organisational and business challenges

The developer of the AI solution highlighted a general lack of dedicated budgets for AI
solutions in hospitals, in addition to an unclear division of responsibilities in
hospitals regarding AI deployment (for example the radiology department,
innovation department, CEO or the IT department). Furthermore, hospitals may lack
the necessary IT capacity and have difficulties in attracting the expertise
required for effective AI deployment, such as data scientists and engineers.

The hospital representative from Belgium echoed these concerns and emphasized the
difficulty in selecting the right AI solution due to the exponential increase of
alternative options available in recent years. The Belgian stakeholder also reflected
that the widespread deployment of AI technology is limited by the lack of
reimbursement mechanisms. In terms of funding, the stakeholder perceived that
deployment of AI solutions may be more widely found in University Hospitals who are
more willing to obtain research grants, innovate and investigate in comparison to public
hospitals.

In contrast, the healthcare professional in the USA indicated that from their experience
there were no significant organizational or business challenges in the deployment of the
solution. The AI solution was integrated without burdening healthcare professionals with
unnecessary technical details, facilitated by extensive support and training from the
developer.

10.7.3.4 Social and Cultural Challenges

The representative from Israel shared the general concern that healthcare
professionals may become over-reliant on AI. Particularly junior clinicians and
interns who may potentially lose the opportunity to fine-tune their image
reading skills without support from AI solutions. The representative from Israel also
reflected that the level of concern raised varies between healthcare professional
groups – for example, those in the emergency department may be more eager to use
the AI solution for decision-making (e.g., discharging patients based on AI evaluations
before a radiologist reviews the study), whereas other groups may be more cautious,
potentially due to concerns regarding job security.

The hospital representative from Israel also added that there is a growing concern about
healthcare professionals experiencing cognitive overload due to the need to
switch between different AI systems. This challenge is closely related to the
recognized gap in digital health literacy among healthcare professionals, particularly
regarding the understanding and use of AI solutions, a need that is acknowledged by
the Israeli stakeholder.

Conversely, the hospital representative from Belgium perceived that there were no
significant concerns from healthcare professionals in the deployment of the AI solution
in their specific context. The radiologists at the hospital were described as driven by
innovation and open to cutting-edge tools, creating a supportive environment for AI
deployment. The healthcare professional in the USA echoed these views, reporting no
significant resistance during implementation. The healthcare professional from the
hospital in Sweden also added that patients also have a positive attitude towards the
use of the AI solution in their care, particularly since it speeds up the time to treatment.

10.7.4 Accelerators to Deployment

10.7.4.1 Technical and Data

According to the hospital representative from Israel, the most critical step of effective
deployment is seamless integration within the existing IT infrastructure. In their
deployment the AI solution integrated with existing systems and provided a familiar
user interface that radiologists recognize and can easily interact without significant
reskilling. This seamless integration is attributed to the developer's design of the
                                                   Deployment of AI in healthcare – Final Report


solution to be compatible with existing software. In addition, the hospital is also focused
upon integrating all AI solutions into a single user interface to alleviate the
cognitive burden experienced by healthcare professionals when interacting with multiple
separate AI tools.

The hospital representative from Israel also referenced the use of cloud computing as
an accelerator to AI deployment, noting the advanced nature of their own cloud
adoption. They highlighted benefits in cloud computing including improved reliability,
flexibility, and agility compared to on premises solutions which made the technological
deployment of cloud-based AI solutions smoother and more streamlined. This process
was also facilitated by the creation of a committee within the hospital, whose role
is to approve and certify all cloud-related solutions before they are implemented, making
the integration process easier.

The Belgian stakeholder reflected on strategies implemented to monitor and take
agile action on alarm fatigue426 experienced by healthcare professionals using some
AI clinical decision support systems. Monitoring of alarm frequency enabled the hospital
to fine-tune the stratification of urgent and non-urgent cases. Similar adjustments are
being considered in other medical specialties to prevent overwhelming healthcare
professionals with unnecessary alarms and reduce the perception of the AI tools as a
burden.

10.7.4.2 Organisational and Business

The hospital representative from Belgium highlighted the importance of a
comprehensive approach (model) for assessing the added value of an AI
solution in comparison to others. To assess the value of the AI solution, the hospital
is focusing on various metrics, including the time required for accurate diagnosis,
improvements in hospital capacity, reductions in staff working hours, enhanced
availability of services, and the speed of diagnosis. By using these indicators, the
hospital aims to quantify how the AI solution contributes to patient outcomes and
operational efficiency, thereby providing a comprehensive evaluation of its impact and
justifying its integration into clinical practice. The hospital representative from Sweden
highlighted the importance of selecting AI solutions based upon addressing a specific
need, and in turn the conduct of pilot studies tailored to the unique environment of the
hospital setting.

The Belgium hospital representative reflected upon the importance of
multidisciplinary teams combining data scientists and engineers and
healthcare professionals which can support the overall more comprehensive
understanding of AI tools, facilitate explainability and interpretability and encourage
inter-professional learning. The healthcare professional from a hospital in the USA
reflected that they avoid, where possible, adding additional burden to their healthcare
professionals with excessive technical detail on the AI solutions. The AI developer
highlighted that the company provides training sessions for the relevant
individuals in hospitals, tailored to their schedules to ensure they are comfortable
with the technology without feeling overwhelmed.

The healthcare professional from Sweden highlighted the importance of training a
“super user” and conducting introductory sessions with radiologists to present
the AI solution and its features. The hospital also conducted pilot studies on the AI
tools performance to compare its findings with the radiologists, complemented with a
rapid feedback loop allowing for open discussion of uncertain findings and


426 The experience of an overwhelming number of alerts, many of which did not require immediate action,
leading to the risk of important notifications being overlooked and potentially compromising patient safety.
continuous feedback resulting in iterative improvements and adjustments to
the solution. With this in mind, the healthcare professional emphasised the importance
to consider that the deployment of AI solutions is not as an isolated one-time event, but
an ongoing process involving continuous evaluation and adaptation to ensure
performance is as expected.

10.7.4.3 Social and cultural

The hospital representative from Belgium emphasized several important practices to
support clinicians in the deployment of AI technologies. Starting with the development
of a clear strategic vision for innovation and robust security requirements to
build trust, and a safe, innovative environment. The stakeholder also reflected on the
importance that AI tools are perceived as supportive tools, rather than healthcare
professional replacements, and in this regard the positioning of AI tools as
enhancements to existing clinical workflows facilitates smoother deployment
and acceptance.

The hospital representative from Israel ensured that relevant stakeholders
(including healthcare professionals) were involved earlier in the decision-
making process for new technologies including AI, through revising their internal
procedures. The stakeholder also referred to the implementation of their own
internal rules regarding AI technology, ensuring that any new AI solution is
accompanied with proper training to all impacted stakeholders. The hospital
representative from Belgium also emphasised the importance of improving digital
literacy amongst healthcare professionals, and noted the added benefit that this can
improve the utilisation of tools, but also can encourage innovation.

The radiologist from a hospital in Sweden noted that open communication on the
use of the AI solution with patients and provision of a standardized note for
radiologists to explain the purpose of the solution helped build trust and fostered
a positive attitude toward the technology.

10.7.5 Complementary Actions

On the technological side, the developer of the AI solution described the importance of
developing a European cloud service to avoid concerns regarding data control and
compliance with European data protection standards. The AI developer, the hospital
representative from Israel and the healthcare professional from Sweden also discussed
the importance of setting interoperability standards to facilitate the seamless
integration of AI solutions into different healthcare systems with minimal
disruption to existing clinical workflows, enabling better data sharing and operational
efficiency. While it is challenging to force AI developers to consolidate or create a single
platform, standardization could help address the issue and avoid adding further
complexity to the daily tasks of healthcare professionals. Standardization could ensure
that AI solutions have a consistent user interface and reporting format, including
the transmission of results and confidence intervals.

The hospital representative from Belgium, the developer of the AI solution and the
healthcare professional from Sweden suggest that regulatory frameworks should be
adjusted to better accommodate for smaller AI startups, which often face high barriers
to market entry. By tailoring requirements, regulators can encourage innovation and
make the market more accessible. They suggest providing appropriate guidance on
how to comply with the Medical Device Regulation (MDR) and increasing the
capacity of notified bodies to speed up the approval process, facilitating the
easier and faster deployment of AI tools in clinical settings by avoiding lengthy and
complex approval processes.
                                                     Deployment of AI in healthcare – Final Report


The developer of the AI solution emphasized the importance of national initiatives
and funding mechanisms. Additionally, the developer highlighted the importance of
creating robust models to assess the added value and return-on-investment of
AI solutions to clearly demonstrate the benefit of deploying AI solutions to hospital
representatives. Such models should consider factors like improved diagnosis accuracy,
increased hospital capacity, reduced working hours, and enhanced service availability.

Furthermore, the developer believes that increasing IT capacity in hospitals and
establishing multidisciplinary teams that include data scientists and IT experts
would facilitate the deployment of AI solutions. These teams can support the technical
aspects of AI deployment and ensure smooth integration with existing systems without
further burdening healthcare professionals.

The developer also recommends more flexible testing environments and quick
assessment processes to evaluate the effectiveness of AI tools quickly. From the
perspective of the healthcare professional from Sweden, deploying an AI solution
requires continuous evaluation and adaptation to ensure it effectively improves hospital
operations and patient outcomes. The interviewee added that radiologists and other
stakeholders need to be involved throughout the entire process—from initial pilots to
long-term use—to ensure that the AI solution meets the specific needs and standards
of the hospital. The developer of the AI solution echoed this statement and pointed out
that early collaboration with end-users, particularly healthcare professionals, is a key
factor in developing relevant and practical, user-friendly AI tools that address specific
clinical needs. Centres could be established to centralise these testing environments and
assessment processes and promoting collaboration between healthcare professionals
and AI developers.

     10.8 Annex 8 – Administrative Use Case – Case Study 2
This case study report focuses on a generative AI solution for clinical documentation
purposes that has been developed by a large enterprise. The specific generative AI
solution does not require regulatory approval before use in the USA nor in Europe. To
provide an overview of the AI use case, we conducted desk research and in-depth
interviews with 6 selected stakeholders 427:

    •    1 healthcare professional from the United States using a clinical documentation
         AI solution,
    •    3 representatives of different hospitals from the United States that have
         deployed a clinical documentation AI solution,
    •    2 representatives of the same hospital in Canada that have deployed a clinical
         documentation AI solution.

The insights gathered contribute to building an overall picture of the use case and its
impact, in addition to gathering information on the challenges and good practices
employed in its deployment in healthcare settings.

10.8.1 Overview of the need

Staffing shortages, increased demand for services fuelled by the growing aging
population, poor patient experiences and burned-out healthcare professionals are some
of the many challenges facing healthcare systems today. Many of these challenges are
interconnected and share a consistent factor: the burden of clinical documentation.
According to the American Medical Association, healthcare professionals spend more
time documenting care than delivering it, spending up to two hours on administrative

427 In this specific case study, the developer of a clinical documentation AI solution did not participate in an
interview.
tasks for each hour of care provided 428. A separate study in Italy reported that
healthcare professionals spend on average 47% of their time on administrative tasks,
with 63% of respondents reporting spending at least half of their time on such
activities429. According to a recent survey by Medscape, more than half (54%) of
healthcare professionals would sacrifice some of their salaries to have a better work-life
balance430.

The administrative burden faced by healthcare professionals has several knock-on
effects. Firstly, the burden of clinical documentation puts increased pressure on
healthcare professionals and has led to higher rates of burnout and turnover, resulting
in a negative impact on patient safety and patient experience. The Health and Human
Services in the USA predict there will be a shortage of nearly 90,000 clinicians by 2025
as a result of burnout, COVID-19, retirement and limits on medical school and residency
programs431. In addition, the number of clinicians aged 60 years and older in 2020 was
31%432. Since 2020, 1 in 5 healthcare professionals have quit their jobs, with surveys
suggesting that up to 47% of US healthcare professionals planning to leave their
positions by 2025433.

Secondly, patients are increasingly report experiencing reduced engagement with
healthcare professionals that are often rushed or distracted during visits as a result of
the documentation burden, resulting in poor patient experiences. In a survey conducted
by Dynata, 71% of patients said they are frustrated with their healthcare experience,
and 61% said they would visit their healthcare professional more often if the
communication experience felt more personalized 434. Reducing the growing clinical
documentation burden faced by healthcare professionals today can improve the clinician
experience by reducing cognitive load and burnout, improve clinician-patient
relationships and patient care, and reduce administrative costs through more efficient
and effective documentation methods435.

10.8.2 Overview of the use case

AI solutions developed for clinical documentation leverage conversational AI and
generative AI technology to transcribe and contextualise the patient-healthcare
professional (HCP) conversation. The solutions enable clinicians to engage in natural
conversation with patients and other family members, connecting with patients rather
than screens. The output of the AI solution (once the HCP-patient conversation has
ended, and recording stopped) can be uploaded into the patients Electronic Health
Record (EHR) for final review, edit and signature by the healthcare professional.

10.8.3 Challenges to Deployment

10.8.3.1 Technical and Data Challenges

Several technological and data challenges were described by the stakeholders
interviewed. One barrier highlighted by one of the hospital representatives in the United

428 Colligan L et al., 2016. Sources of physician satisfaction and dissatisfaction and review of administrative
tasks in ambulatory practice: A qualitative analysis of physician and staff interviews.
429 Petruzzelli et al., 2024. Exploring the administrative burden faced by haematologists: a comprehensive
study in Italy.
430 Jon McKenna, 2024. Medscape Physician Lifestyle & Happiness Report 2024: The Ongoing Struggle for
Balance.
431 Shanafelt TD et al., 2016. Potential Impact of Burnout on the US Physician Workforce.
432 Young A et al., 2021. FSMB census of licensed physicians in the United States, 2020.
433 Elsevier Health, 2022. Clinician of the Future.
434 Redpoint global, 2020. 75% of U.S. Consumers Wish Their Healthcare Experiences Were More
Personalized, Redpoint Global Survey Reveals.
435 Sloss et al., 2024. Toward Alleviating Clinician Documentation Burden: A Scoping Review of Burden
Reduction Efforts.
                                           Deployment of AI in healthcare – Final Report


States is the variation in performance of the AI solution across different medical
specialties. The hospital representative from the United States reported that this poses
a challenge for medical specialties with specific needs. Hospital representatives from
Canada also raised concerns about performance variability. They noted that while the
solution performs well in ambulatory settings, healthcare professionals in complex
internal medicine settings with long consultations can experience difficulties

The other hospital representative from the United States highlighted a similar challenge.
According to the interviewee, although time savings of up to two hours daily have been
reported in healthcare settings where documentation is usually typed and that these
benefits appeared less significant in settings where documentation processes
were simpler. In inpatient environments, issues like noise and the fast-paced nature
of emergency departments, where work is often done outside the patient’s room,
present obstacles. In critical care, the presence of simultaneous conversations among
multiple healthcare professionals adds further complexity.

One hospital representative from the United States noted that a barrier to the
deployment of the AI solution across EU Member States may be the language as its
effectiveness in other EU languages may add complexity to cross-region transferability.

The healthcare professional from the United States reflected concerns surrounding
the accuracy of the AI solution’s perfor ance. According to the interviewee, the
AI solution occasionally misses some discussion points, requiring manual reconciliation
by healthcare professionals.

Another challenge raised by the healthcare professional from the United States are the
concerns surrounding training and tuning the AI solution to match the
personalized preferences of the healthcare professionals. The interviewee reported that
even within the same medical specialty, healthcare professionals’ preferences and
approaches may vary.

10.8.3.2 Legal and Regulatory Challenges

Two hospital representatives from the United States stated that privacy concerns were
barriers to deployment. At enterprise level, there are concerns about where the data
collected by the AI solution is stored, its potential uses, and the risks of data breaches.
On an individual level, the hospital representative reported that there is a requirement
to obtain verbal or written consent from patients before using ambient technology,
ensuring transparency and compliance with privacy standards.

Additionally, another hospital representative from the United States reported that AI
developers who access data in the cloud are required to demonstrate certification and
qualification according to specific cybersecurity regulations. While such
regulations may not be a problem for large developers, their stringency could pose
challenges for smaller startups. The hospital representatives from Canada reflected
the same concerns and added that the negotiations with the legal counsel prior to the
deployment to ensure safety and security were months long and delayed the process.
A hospital representative from the United States also raised concerns about liability
and accountability.

10.8.3.3 Organisational and business challenges

Hospital representatives from the United States highlighted that the high cost limits
the deployment of the AI solution to only a number of healthcare professionals, primarily
the ‘heavy users’. The hospital representatives from Canada echoed those concerns and
added that the high cost, along with the general lack of funding, limits their goal to scale
the AI solution further.
10.8.3.4 Social and Cultural Challenges

All the hospital representatives from the United States raised concerns about
healthcare professionals’ resistance to change. One hospital representative
reported that the initial interest among healthcare professionals was around 60-70%
but dropped to about 50% after the trial period. This resistance was attributed to the
healthcare professionals’ preference for their own familiar, personalized templates or,
as some reported, the language used by the AI solution that included a lot of laymen
terms instead of precise medical terminology. Another hospital representative from the
United States echoed this resistance, attributing it to a preference for an alternative,
familiar solution that not only transcribes notes but also sends orders and prepares
charts ahead of visits. Additionally, the healthcare professional from the United States
highlighted that the resistance was particularly strong among older practitioners who
were accustomed to other tools, attributing this reluctance to a desire to maintain
established routines than to distrust of the new technology.

The hospital representatives from Canada also reflected resistance to the solution at
their hospital, adding that the non-familiarity with the language was evident in the early
stage of deployment.

Regarding the patient’s attitude towards the AI solution, one hospital representative
from the United States reported some patient resistance mainly due to privacy
concerns. Additionally, the hospital representative highlighted that some patients were
concerned about the lack of human oversight, fearing that healthcare professionals
might become overly reliant on the AI solution, potentially leading to missed information
or gaps in their care.

10.8.4 Accelerators to Deployment

10.8.4.1 Technical and Data

All stakeholders interviewed reported that a key accelerator of the deployment process
is the seamless integration of the AI solution within the existing IT
infrastructure. The AI solution integrated seamlessly within existing EHR systems and
provided a familiar user interface that healthcare professionals already use and can
easily navigate, reducing the cognitive burden of interacting with multiple software. One
hospital representative from the United States noted that the solution works well with
most local systems, which could facilitate cross-region deployment, particularly in rural
areas or locations still reliant on paper charts due to limited digital infrastructure such
as EHRs.

One hospital representative from the United States highlighted the leadership’s early
decision to invest in infrastructure and equip every room with computers as a
key accelerator. This proactive approach eased the downstream deployment and
minimized logistical and financial challenges. Another hospital representative from a
different hospital in the United States added that the hospital intentionally slowed
down the initial deploy ent process to o serve the solution’s i pact on
workflow and functionality.

The hospital representatives from Canada reported that the project evaluation approach
prioritized both timeliness and completeness by implementing a two-stream strategy.
Recognizing the need for rapid results to address initial concerns from the leadership
team, the evaluation team established a plan for early data collection and frequent
reporting of key performance indicators (KPIs). Although timeliness was prioritized, the
evaluation team also integrated academic rigor by involving a health economist and
applying a health economics methodology.
                                           Deployment of AI in healthcare – Final Report


For post-deployment monitoring, the hospital representatives from Canada highlighted
that the hospital’s existing EHR software auto atically collects data, such as
time spent on administrative tasks, enabling easy before-and-after comparisons.

One hospital representative from the United States reported conducting post-
deployment testing to ensure that the AI solution is a good fit, with assessments
being more qualitative rather than quantitative. Another hospital representative from a
different hospital in the United States added that the hospital conducted a usability
analysis to compare charting time across different settings, four months before
and after deployment.

To ensure the AI solution’s adapta ility to healthcare settings, the hospital
representatives from Canada and the AI developer agreed to pilot it among
physicians across several medical specialties. This ensured the AI solution
addressed the specific needs of each subspecialty. The healthcare representatives
emphasized that the expertise of the AI developer was a key factor in accelerating
the deployment.

10.8.4.2 Legal and Regulatory

The healthcare representatives from Canada identified several practices they
implemented to address legal and regulatory challenges. They began by conducting due
diligence with the AI developer. This helped define liability and accountability
measures in the event of unforeseen issues. Following this, open conversations
were held with the AI developer. These discussions helped the hospital to better
understand the risks, implications, and mitigation measures involved in deploying the
AI solution. Finally, the hospital consulted with its legal counsel to ensure
compliance with data protection and security standards before proceeding with
the deployment.

10.8.4.3 Organisational and Business

Stakeholders from the United States emphasized the crucial role of clinical champions
—healthcare professionals who are knowledgeable about AI and actively advocate for
its adoption within their specialties. One hospital representative highlighted the
importance of these champions being deeply involved in their fields, enabling them to
pinpoint specific needs that AI solutions should address. Once these needs are identified,
multidisciplinary teams, including data scientists, IT specialists, and AI developers, work
together to refine and adapt the AI solution to fit seamlessly into clinical workflows.

A hospital representative from the United States highlighted that in one hospital a
specific annual budget was allocated for AI licenses, distributed through a
selection process that considered factors like ambulatory visits per week, potential value
of use, and current usage of other tools. This approach allowed the center to identify
candidates who would benefit most from the solution and ensure equitable distribution
across specialties.

Hospital representatives from Canada proposed a gradual scale-up approach,
beginning with early investments in a small group of physicians and subspecialties. This
controlled rollout made it easier to manage and adjust the implementation in later
stages, with scalability in mind. The goal was to steadily build a solid foundation for
wider hospital adoption, ensuring that the expansion remained manageable and
sustainable. Representatives explained that the hospital planned to evaluate the return
on investment (ROI) once the AI solution was deployed to a larger group of healthcare
professionals.
Regarding workflow integration, a U.S. hospital representative emphasized their
hospital’s long-term investment in IT personnel. These specialists play a critical role in
translating the solution's functionality into practical applications for healthcare
professionals, providing on-site support to facilitate seamless integration into daily
workflows. The representative also highlighted a growing trend of appointing chief
innovation officers (CIOs) with clinical backgrounds, ensuring that AI tools align
closely with clinical needs.

Canadian hospital representatives similarly stressed the importance of adjusting
workflows to integrate the AI solution effectively, acknowledging an initial learning
curve for users. They observed that as healthcare professionals became more familiar
with the solution, productivity and efficiency improved, enhancing overall effectiveness
in clinical settings.

10.8.4.4 Social and cultural

The healthcare professional from the United States identified a few practices to deploy
the AI solution while addressing social and cultural challenges. To ensure transparency
and patient comfort, the interviewee recommended including a written consent form
and an informational note in the template for all users. This documentation should
explain what the AI solution is and how it functions. This approach would help manage
patient expectations and clarify the AI solution’s role in their care. Additionally, instead
of broadly informing all patients about the AI solution, the hospital representative
reported that the hospital only communicates such for patients coming in for
visits in the chosen subspecialties where the AI solution is used. This targeted
communication minimizes unnecessary concerns among patients who are not affected
by its use.

The hospital representatives in Canada implemented several best practices to ensure
the AI solution’s successful integration and use in their clinical settings. To facilitate
continuous learning and adaptation, a multifaceted education strategy was
adopted. This strategy includes gate checks every two months, where healthcare
professionals participate in 30-minute calls, with 5 minutes dedicated to data
presentation and the remaining 25 minutes for informal peer discussions. These
sessions create a space for reflection and sharing experiences, fostering a supportive
learning environment.

Additionally, a dedicated communication channel was established to ensure
continuous interaction between healthcare professionals and the developers. This
ongoing communication supports regular feedback collection through discussion
sessions, workshops, and surveys.

The hospital representatives from Canada reported closely tracking the usage of the
AI solution by healthcare professionals to identify those who may not be utilizing it
adequately. Feedback is gathered to determine whether low use is due to dissatisfaction
with the solution or a lack of necessary skills. Finally, training healthcare
professionals to navigate the complexity of clinical work with the AI solution
was also recognized. As clinical work itself is inherently complex, this training supports
teams and introduces streamlined workflows, ultimately reducing barriers to the
solution’s effective use.

The hospital representative from the United States echoed the importance of ensuring
healthcare professionals are comfortable and competent to use the solution. An
additional accelerator reported by the stakeholder was the involvement of early
                                          Deployment of AI in healthcare – Final Report


adopters in the pilot studies. Those early adopters provided positive feedback on the
solution to their colleagues, encouraging its use.

10.8.5 Complementary Actions

On the technological side, the healthcare representative from the United States
emphasized the importance of selecting the appropriate solution for each specific
task, following clear discussions with developers about the solution’s limitations. The
healthcare professional added that for any AI solution to be effective, simplicity and
consistency in design are essential. This approach enhances user-friendliness,
allowing reliable, long-term use. Additionally, the healthcare professional recommended
that healthcare professionals should have the ability to directly train and adjust
the solution in real-time clinical settings. This hands-on involvement of the users
would facilitate the customization of the solution to meet specific clinical needs and
address functionality gaps more effectively.

Another hospital representative from a different hospital in the United States
recommended establishing assurance labs to rigorously validate AI tools before
deployment. Such labs would serve as controlled environments to test the tools'
reliability, accuracy, and performance, ensuring they meet the necessary standards for
clinical use. The interviewee also emphasized the importance of creating
standardized data structures to ensure interoperability across systems, which would
improve the usability of AI tools and help users understand and mitigate potential biases
in the models. Furthermore, these standardized data structures should be diverse and
representative of patient populations to ensure the AI models are equitable and
applicable in varied clinical settings.

From an organizational and business perspective, the healthcare representatives from
Canada pointed to the necessity of establishing funding and reimbursement
mechanisms to support AI deployment and scalability. On the social and cultural
side, the hospital representative from the United States recommended educating
healthcare systems on both the capabilities and constraints of the solution to
avoid potential setbacks and mitigate unrealistic expectations. The hospital
representatives from Canada focused on the importance of educating healthcare
professionals on the cultural shift. They noted that AI deployment is accelerating
rapidly, and preparing healthcare professionals now will ease the transition when AI
tools become more widely integrated into clinical practice.

    10.9 Annex 9 – Cancer Treatment Use Case – Case Study 3
This case study report focuses on an AI solution used in the treatment of cancer that
has been developed by a small-medium enterprise (SME) and has been approved by the
U.S. Food and Drug Administration (FDA) and has a European Conformity marking (CE
marked) and deployed in urban healthcare settings globally. To provide an overview of
the AI solution, we conducted desk research and in-depth interviews with a range of
stakeholders to understand the current need in healthcare addressed by the AI solution,
its impact on clinical workflow and overall delivery of care, the challenges faced during
deployment, and any good practices that facilitated its deployment. A total of 5
stakeholders were interviewed:

   •   the developer of the AI solution from France,
   •   1 healthcare professional from Germany using the AI solution,
   •   1 healthcare professional from France using the AI solution,
   •   1 hospital representative from France that has deployed the AI solution,
    •   1 hospital representative from Germany that has deployed the AI solution.

The insights gathered contribute to building an overall picture of the use case and its
impact, in addition to gathering information on the challenges and good practices
employed in its deployment in healthcare settings.

10.9.1 Overview of the need

Cancer is responsible for one in every four deaths in Europe, making it the second
leading cause of death and disability after cardiovascular disease. The impact of cancer
on European healthcare systems is expected to increase, with the number of people
diagnosed with cancer across Europe having risen by approximately 50% over the past
two decades436. Given an ageing and growing European population, this trend is set to
continue with the cancer incidence and mortality in Europe expected to increase by 38%
and 44% respectively by 2040437.

Radiation therapy is an effective cancer treatment, with at least half of all cancer
patients expected to undergo radiotherapy (RT) at some stage during their care.
However, more than one out of four cancer patients in Europe do not receive the
radiotherapy they need438. Limited availability of the necessary resources – in terms of
both trained personnel and equipment – is one of the biggest barriers contributing to
suboptimal access to radiotherapy. Moreover, effective RT planning may be challenging
as each patient’s tumour characteristics, such as size, location, and sensitivity to
radiation are unique. Tumours can also move due to patient breathing or changes in
body position, making real-time monitoring and accurate targeting complex.
Additionally, RT can cause acute and long-term side effects, such as skin irritation,
fatigue, and damage to healthy organs 439. RT planning must account for these risks,
particularly for tumours located near sensitive structures.

Tumour contouring, or target delineation, consists of the process of outlining the shape,
size, and location of a tumour and surrounding critical structures on medical imaging
scans. It is a critical step in RT planning, due to its impact on both treatment efficacy
and patient safety, as it defines the area that will receive the radiation dose while
sparing healthy tissues as much as possible440. Considering the above, to be as effective
as possible, contouring must be precise, focused on the tumour, and be personalised
for each patient to minimise any potential side effects.

Computed tomography (CT) is currently the gold standard for tumour contouring.
Nevertheless, as a patient’s anatomy changes during treatment, the initial CT-based
treatment plan may no longer accurately reflect the dose being delivered to the tumour
and surrounding organs at risk (OARs)441. Repeated imaging, such as cone-beam
computed tomography (CBCT), which is often used for patient positioning, can assist in
making plan adaptation decisions442.



436 Hofmarcher T, Bradvik G, Svedman C, et al. 2019. Comparator Report on Cancer in Europe 2019.
437 European Commission – Joint Research Centre. 2023. Cancer in 2040: Estimates for an ageing Europe.
438 Zeman EM, Schreiber EC, Tepper JE, et al. 2020. Basics of radiation therapy.
439 Zeman EM, Schreiber EC, Tepper JE, et al. 2020. Basics of radiation therapy.
440 Jameson MG, Holloway LC, Vial PJ, et al. 2010. A review of methods of analysis in contouring studies
for radiation oncology.
441 Precise contouring of all OARs is needed to minimise damage to surrounding healthy tissues and
organs. This process is often tedious, time-consuming, and costly, requiring significant resources and
expertise
442 Yoo S, Yin FF. 2006. Dosimetric feasibility of cone-beam CT-based treatment planning compared to CT-
based treatment planning.
                                                  Deployment of AI in healthcare – Final Report


Magnetic resonance imaging (MRI) is frequently used alongside CT imaging to improve
the contouring of tumours and OARs due to its superior soft-tissue contrast443. MRI
offers additional advantages over CT, such as the use of non-ionising radiation and the
ability to gather more detailed information on tumour activity and response to therapy.
However, despite these benefits, radiotherapy planning cannot rely solely on MR images,
as they do not provide the tissue electron density 444 information required for dose
calculations in a treatment planning system (TPS) 445.

Adaptive radiotherapy (ART) is a treatment strategy developed in recent years to
address anatomical variations between treatment sessions. ART enables more precise
and personalised radiation delivery, with the potential to enhance patient outcomes.
The primary aim of ART is to enhance the accuracy of dose delivery to patients while
minimising the risk of side effects on healthy tissues. ART can be applied to various
cancer types, including prostate, lung, and head and neck cancers. A key factor enabling
ART is the advent of image-guided radiotherapy, where patients undergo repeated
imaging, such as CBCT446. Once several 3D images are obtained, they need to be
registered, by aligning multiple 3D images of the same patient into a unified coordinate
system for precise comparison, analysis, and merging of data from different imaging
modalities or time points. However, CBCT images have several limitations, including
poor image quality, soft-tissue differentiation, and a limited field of view. These issues
restrict the effectiveness of CBCT images for dose calculations and objective clinical
decision-making regarding the need for adaptation447.

Moreover, these tasks are highly time-consuming. Within the current clinical workflow
of adaptive MR-guided radiotherapy, the most time-consuming factor is a new daily
accurate and consistent annotation of structures. As these tasks need to be carried out
manually by radiotherapists, this workflow not only limits the number of patients being
treated, but also introduces time delays which can result in intra-fractional motion (i.e.
movement of a patient’s tumour or internal organs during a RT session) of the relevant
structures448.

To address these challenges, an Artificial Intelligence (AI) based solution has been
developed for ART.

10.9.2 Overview of the use case

The AI use case is a radiotherapy software that assists in automatic contouring
delineation of anatomical regions on 3D images of cancer patients scheduled for
radiotherapy, hence optimising the treatment process, from preparation to follow-up.




443 Nachbar M, Lo Russo M, Gani C, et al. 2023. Automatic AI-based contouring of prostate MRI for online
adaptive radiotherapy.
444 Electron density refers to the average number of electrons per unit of volume of material. This
information is used to assess how different tissues absorb or scatter radiation from X-ray cancer therapy
and is crucial for guaranteeing an efficient treatment.
445 Khoo VS, Joon DL. 2006. New developments in MRI for target volume delineation in radiotherapy.
446 Alves A, Dias JM, Rocha H, et al. 2021. Assessing the need for adaptive radiotherapy in head and neck
cancer patients using an automatic planning tool.
447 Gianoli C, De Bernardi E, Parodi K. 2024. “Under the hood”: artificial intelligence in personalized
radiotherapy.
448 Nachbar M, Lo Russo M, Gani C, et al. 2023. Automatic AI-based contouring of prostate MRI for online
adaptive radiotherapy.
10.9.3 Challenges to Deployment

10.9.3.1 Technical and Data Challenges

The hospital representative from France noted that requirements specific IT
infrastructure such as a server with a Graphics Processing Unit (GPU) resulted in
additional deployment costs. The hospital representative from France also emphasised
the risks of high fragmentation of AI solutions market, hence entailing significant
challenges in terms of interoperability of solutions. The stakeholder emphasised
that merging distinct products into one single, unified AI solution could
streamline processes and lower costs, although reflected that the technology to achieve
this “multi-modal” approach may not yet be available.

10.9.3.2 Legal and Regulatory Challenges

The AI developer reflected on the complex regulatory processes in the EU. Despite
the AI solution being CE marked, the AI developer highlighted that the auditing and
approval process was considerably longer and more burdensome than in the USA. In
relation to deployment, the AI Developer highlighted that the cost of regulatory
procedures increases the cost of deploying the AI solution in Europe.

Similarly, the hospital representative from France highlighted the importance of
targeted financial support for Small-Medium-Enterprises (SMEs), noting that
whilst SMEs are frequently the main source of AI innovations, they encounter significant
regulatory and financial barriers when trying to enter the market.
10.9.3.3 Organisational and business challenges

The stakeholders interviewed also highlight some organisational and business
challenges affecting the deployment of the AI solution. The introduction of any type of
technology always involves an assessment of added value to select the best
solution available. As noted by a healthcare professional of a hospital in Germany, it
was challenging to convince some members of the management team of the added
value of the AI solution versus existing clinical solutions. Since such AI tools are often
expensive to deploy, it is necessary to clearly outline to the decision makers within a
healthcare facility that the investment was worthwhile (i.e. return on investment).

Another major issue highlighted by the AI Developer is that AI innovations often fall
outside the scope of European reimbursement frameworks. The AI developer also
highlighted a significant difference between the EU and the USA on how decisions are
taken regarding the deployment of AI technologies within a healthcare facility, as the
value attributed to efficiency gains and time savings are considered differently
among healthcare facilities.

Moreover, the AI developer emphasised the need for wider utilisation of innovative
AI tools in public healthcare institutions. The AI developer added that European
public healthcare facilities, despite having a strong demand for these advancements,
are frequently the last to adopt them, and this lag is primarily caused by bureaucratic
obstacles. Consequently, the stakeholder emphasised that these facilities require a
fast-track pathway for financing and adopting AI solutions, as the current process is
excessively long and time-consuming.

10.9.3.4 Social and Cultural Challenges

One of the key challenges highlighted by all stakeholders interviewed is the hesitation
of some healthcare professionals to adopt the AI solution. Stakeholders reflected
                                            Deployment of AI in healthcare – Final Report


upon a generational divide in attitudes towards AI, with younger doctors generally
more open to incorporating AI solutions into their practice. According to the AI
developer, younger healthcare professionals are less inclined to spend time on tedious
tasks that can be carried out by the AI solution, freeing up their time for direct patient
care. A healthcare professional from a German hospital noted that the presence of many
younger doctors in their institution played a crucial role in promoting the adoption of
the AI solution.

Moreover, according to the AI developer, some doctors fear that over-reliance on the
solution could diminish younger doctors' ability to perform tasks
independently, and in turn result in over-reliance which degrades essential medical
skills, or prevents them being fine-tuned (for example, doctors may not develop their
own critical decision-making abilities when preparing contouring delineations).

The healthcare professional from a hospital in Germany highlighted that some doctors
were uneasy about using an AI solution for tasks traditionally performed by
highly trained medical professionals, and that this underscores the need for
rigorous validation and transparent testing of the AI system to build confidence. The
representative from the French hospital echoed similar sentiments, stressing the
importance of verifying the AI solution's results to make sure no eventual
errors go unnoticed. This professional emphasized that ultimate accountability lies
with the doctors, who are responsible for patient outcomes.

10.9.4 Accelerators to Deployment

10.9.4.1 Technical and Data

The hospital representative from France emphasized the advantages of upgrading
their IT infrastructure which significantly enhanced the hospital's operations, allowing
healthcare professionals to move more efficiently between various tools and data sets.
With this system in place, staff no longer need to manually enter all the information,
which streamlines the process of uploading and downloading data. This not only
saves time but also bolsters data integrity, as reducing manual input helps minimize
the risk of errors.

Alongside these infrastructure improvements, the hospital has benefited from
enhanced interoperability between tools. This seamless integration allowed
healthcare professionals to experience the advantages of the AI solution from the early
stages of deployment. Importantly, this interoperability ensures that the AI solution
complements, rather than disrupts, existing workflows. By integrating smoothly with
the hospital's current systems, the AI solution increases efficiency without the need for
extensive retraining or major adjustments from the staff, making the transition easier
and more effective.

According to the healthcare professional from a hospital in Germany, the AI solution
was seamlessly integrated into the existing IT infrastructure and was
compatible with other tools in use. They highlighted key features like the AI’s user-
friendly design, easy installation process, and strong interoperability with
current systems as critical factors in its success. The integration also facilitated reliable
data exchange between systems, supporting more accurate and comprehensive
analysis. These practices reflect a focus on user-centred design, smooth data
integration, and maintaining high standards of data quality, all of which contributed to
the solution’s effective deployment.
10.9.4.2 Organisational and Business

One key approach highlighted by the AI developer was the importance of conducting
pilot studies with as many future users as possible before rolling out the AI
solution widely. This strategy helped mitigate resistance to change by allowing
healthcare professionals to validate the AI’s perfor ance in their specific
settings. The healthcare professional from a hospital in Germany emphasized that such
pilot studies were important in addressing concerns among colleagues. Some
healthcare professionals initially doubted the AI solution’s ability to save time, while
others believed that although the solution might speed up tasks, they would still need
to verify the results, potentially offsetting any time saved. The healthcare professional
of a hospital in Germany explained that demonstrating measurable improvements
in clinical outcomes and workflow efficiency was key to securing
  anage ent’s support, as without clear evidence of these advantages decision-
makers might have hesitated to commit to such a financial investment.

Another good practice involved the provision of highly effective training during the
deployment phase by the AI developer. According to the hospital representative
from Germany, the training was concise and focused on the practical use of the AI
solution, which helped build confidence among healthcare professionals. The
involvement of project managers, who were also lead physicists, further ensured a
smooth deployment process. These "AI champions" were important in managing
workflows and optimizing the integration of the AI solution within the
institution.

Additionally, the healthcare professional of a French hospital emphasised the value of
strong collaboration between the deployers and AI developers. Healthcare
professionals played an active role in validating the AI’s results and providing
detailed feedback on any discrepancies. Since the data used for testing the solution
came from within the hospital, it was easier for professionals to verify the AI’s accuracy.
This ongoing feedback loop between the hospital staff and developers was
essential in building trust and confidence in the technology and is a practice that should
extend beyond the deployment phase.


10.9.4.3 Social and cultural

When discussing social and cultural practices that accelerated the deployment of the AI
solution, the healthcare professional of a hospital in France emphasised that having a
deep understanding of the AI solution’s capa ilities, the data it was trained on,
and the quality control processes behind it, helped build trust in the technology.
Since healthcare professionals remain fully responsible for their actions, complete
confidence in the AI solution is essential to ensure its widespread adoption.

The AI developer emphasised the importance of ensuring confidence and trust in the
AI solution from a healthcare professional’s perspective. Demonstrating the
development process in terms of the AI solution’s internal validation procedures and
highlighting the number of institutions that have already deployed the AI solution helps
build trust and confidence, allowing for more widespread deployment. As more centres
deploy the solution and share its benefits and added value, new facilities are more easily
persuaded to try and eventually deploy the AI solution. As a result, due to the
demonstrated added value of such AI solutions, there is overall acceptance among
healthcare professionals for its widespread use.
                                                     Deployment of AI in healthcare – Final Report



10.9.5 Complementary Actions

The AI developer highlighted that the regulatory process should be streamlined.
Notably, to reduce the time-for-approval, the interviewee mentioned that more AI
experts should be involved in the process to support the assessment and audit
of AI-based medical devices. In this regard, the developer suggested offering clear
regulatory guidance and expanding the resources of notified bodies to accelerate
the process. This would help alleviate delays, enabling quicker and smoother integration
of AI tools in healthcare and, thus, streamline the approval procedures while reducing
potential bottlenecks.

The healthcare professional and the management representative of a hospital in France
as well as the healthcare professional from a hospital in Germany agreed that defining
and optimising the quality assurance and monitoring processes is a necessary step
to further streamline the regulatory process. Since single hospitals might not have
defined processes in place to monitor the quality of the AI tools they use, EU-level
guidelines on how AI should be used and monitored in European hospitals
should be developed.

The healthcare professional of a hospital in Germany emphasised that clear patient-
friendly assurance about how their health data is protected should be provided
at EU-level through regulation so as to make sure that any AI healthcare solution is in
line with GDPR requirements. The interviewee noted that patients are increasingly
worried about the safety of their data and need reassurance to accept the use of AI
technologies as part of their healthcare services. Additionally, the interviewee stressed
that anonymisation might not always be sufficient, as some AI tools require access to
patients' personal data.

Concerning the issues at the business and organisational level an action highlighted by
the AI developer was the provision of funding to public healthcare facilities support
a faster adoption of AI tools. In this respect, the AI developer reflected upon the
different reimbursement models by which hospitals deploying the solution could
choose. The representative of a hospital in Germany recognised that this was an
advantage that facilitated the introduction of the AI solution in their circumstance.

The hospital representative from France stressed that specific support should be
given to SMEs developing AI healthcare technology. The hospital representative
from France also emphasised that, although many tools are being introduced to the
market, certain disease areas receive limited funding for R&D. This raises the risk
that patients in these areas may fall behind in accessing new AI solutions.


     10.10        Annex 10 – Cancer Detection Use Case – Case Study 4


This case study report focuses on an AI use case used in radiology for the early detection
of metastasis that has been developed by a large enterprise and deployed in healthcare
settings in Japan. To provide an overview of the AI solution, we conducted desk research
and in-depth interviews with 5 selected stakeholders 449:



449 In this specific case study, the developer of the AI solution did not participate in an interview.
    •   two healthcare professionals from Japan using the AI solution who were also
        involved in the development of the AI solution,
    •   two healthcare professionals from Japan of different hospitals using the AI
        solution in their clinical practice,
    •   one representative of a hospital from Japan that has deployed the AI solution.

The insights gathered contribute to building an overall picture of the use case and its
impact, in addition to gathering information on the challenges and good practices
employed in its deployment in healthcare settings.

10.10.1           Overview of the need

Metastasis is the process by which cancer cells spread from the primary tumour site to
other parts of the body. Bone metastasis, in particular, occurs when cancer cells migrate
to the bones, with bone being the third most common site for metastasis, after the lungs
and liver450. This spread can lead to bone pain, fractures, and other complications as
the cancer cells disrupt normal bone tissue. Thus, if identified or treated late, bone
metastases can impair motor function and severely impact a patient’s quality of life.
Vertebral metastases, in particular, may lead to compression fractures and neurological
issues, such as quadriplegia. Although advancements in anticancer treatments have
reduced complications, early detection remains essential, underscoring the importance
of clinical follow-up to prevent these issues through prompt diagnosis and
intervention451.

Computed tomography (CT) serves as the primary tool for early and precise detection
of bone metastases in cancer follow-ups. Since cancer patients undergo frequent CT
scans to monitor local recurrence and distant metastasis, early detection is possible.
Recent advances in CT technology allow for the identification of small, subtle lesions.
However, such lesions are often obscured by the vast amount of anatomical detail, which
can delay radiologists in locating them. Although CT capabilities have improved with
higher resolution and better signal-to-noise ratios, the increased volume of anatomical
data has heightened the challenge for radiologists, making timely detection more
difficult452. Furthermore, the high CT density of bone compared to other organs makes
it challenging to clearly visualise density changes caused by bone metastases on
standard CT images453.

Additionally, comparing past and current CT images is subject to several complexities.
Even for the same area on the same person, variations in body condition can alter how
tissue appears on imaging (e.g. cancer patients may experience changes like weight
loss). This requires highly precise image alignment technologies. Without this precision,
numerous other differences - such as subtle variations due to breathing depth during
scans- would appear on subtracted images, complicating the detection of bone




450 Onoue K, Yakami M, Nishio M, et al. 2021. Temporal subtraction CT with nonrigid image registration
improves detection of bone metastases by radiologists: results of a large-scale observer study.
451 Onoue K, Nishio M, Yakami M, et al. 2019. CT temporal subtraction improves early detection of bone
metastases compared to SPECT.
452 Sakamoto R, Yakami M, Fujimoto K, et al. 2017. Temporal subtraction of serial CT images with large
deformation diffeomorphic metric mapping in the identification of bone metastases.
453 Onoue K, Yakami M, Nishio M, et al. 2021. Temporal subtraction CT with nonrigid image registration
improves detection of bone metastases by radiologists: results of a large-scale observer study
                                                  Deployment of AI in healthcare – Final Report


metastases454. Other methods to identify bone metastasis, such as bone scintigraphy 455,
have also proven to be time-consuming, placing significant burden on both patient and
doctor456.

Detecting bone metastases with CT remains challenging, with a risk of missing
potentially dangerous lesions457. As highlighted by a healthcare professional interviewed
for this case study, the process of examining bone metastases can be cumbersome,
repetitive and is often completed at the end of the CT review sequence. Typically, the
examination begins with the chest, followed by the abdomen, with the bones examined
last. Consequently, when the patient volume is high, this step may sometimes be
overlooked. This is particularly concerning given the current shortage of radiologists,
and the significant increase in their workloads in recent years given the greater demand
and complexity of CT interpretations. These factors combined have led to backlogs of
unread CT scans, potentially delaying the identification of bone metastases in cancer
patients458.

In response to the above, the AI developer has partnered with university hospitals to
create an AI solution for early detection of bone metastasis.

10.10.2           Overview of the use case

Temporal subtraction (TS) is a technique used to extract an earlier image from the
latest scan, utilising medical images captured at two distinct times in a sequence 459. In
other words, this technique allows to compare the same body part between two points
in time. The use of TS with CT images enhances the ability of radiologists to identify
new bone lesions, including bone metastasis. Traditionally, identification of differences
between two scans is a manual process performed by radiologists. Since its introduction,
the TS method has evolved, allowing for better visualisation of bone metastasis 460. AI
solutions can streamline this process by automatically retrieving previous images,
identifying bone regions, reduce noise perform and the analysis – transmitting the
outputs into medical image repository.

10.10.3           Challenges to Deployment

10.10.3.1        Technical and Data Challenges

The representative of a Japanese hospital highlighted interoperability issues with pre-
existing systems, along with limited accessibility to the hospital's patient medical
records. This restricted access posed significant challenges for the deployment of the
AI solution, as this relies on patient data to function effectively, raising concerns related
to data transparency and privacy.




454 Onoue K, Yakami M, Nishio M, et al. 2021. Temporal subtraction CT with nonrigid image registration
improves detection of bone metastases by radiologists: results of a large-scale observer study
455 This method involves using a specialised camera to capture images of radioactive substances injected
into the patient’s bloodstream.
456 Yang HL, Liu T, Wang XM, et al. 2011. Diagnosis of bone metastases: a meta-analysis comparing 18
FDG PET, CT, MRI and bone scintigraphy.
457 Onoue K, Nishio M, Yakami M, et al. 2019. Temporal subtraction of computed tomography images
improves detectability of bone metastases by radiology residents.
458 Yamada K. 2023. What has caused the shortage of radiologists? Features exclusive to Japan.
459 Iima M, Sakamoto R, Kakigi T, et al. 2023. The efficacy of CT temporal subtraction images for
fibrodysplasia ossificans progressiva.
460 Onoue K, Nishio M, Yakami M, et al. 2019. Temporal subtraction of computed tomography images
improves detectability of bone metastases by radiology residents.
Moreover, a healthcare professional involved in the development of the solution
observed that integrating the AI solution within the depart ent’s existing
medical image repository required careful planning to maintain efficient data flow,
as the additional data processing demands of the AI solution risked slowing down the
system and potentially delaying access to critical imaging information. As highlighted
by the healthcare professional, in fact, ensuring seamless integration was essential to
avoid workflow disruptions and maintain the timely delivery of patient care .

Given that the AI solution operates without requiring specialised IT infrastructure, its
integration was streamlined. Nonetheless, the limited storage capacity at the hospital
prompted radiologists to explore options with the developers for reproducing the AI
outputs should they be inadvertently deleted.

Additionally, significant efforts were made to keep all data on-premises within the
hospital, as this is a strict requirement from the IT department. However, this approach
may vary depending on the hospital’s capacity.

10.10.3.2        Legal and Regulatory Challenges

The healthcare professionals interviewed emphasised that no significant legal or
regulatory challenges were encountered during the specific adoption of the AI solution
in their clinical settings: the regulatory process for the AI solution proceeded smoothly,
allowing for its adoption in the hospital without legal obstacles.
A healthcare professional emphasised that the radiology department staff faced some
considerations specific to data privacy concerns. For instance, medical personnel
engaged in detailed discussions with the AI developers to determine the source of
images accessed by the solution, the recipients of the solution’s output, and
the duration for which this output should remain accessible.

The Japanese government has a reimbursement system encouraging the uptake
of AI solutions in healthcare facilities, approximately 50 hospitals in Japan are
entitled to receive additional diagnostic allowance from the government for adopting AI
solutions. The current reimbursement system requires healthcare facilities to comply
with certain requirements. In particular, healthcare facilities need to have in place
appropriate safety management of diagnostic imaging assistance software utilizing
artificial intelligence-related technologies based on the guidelines established by related
academic societies (i.e. Japanese Society of Radiological Medicine) 461. Other
requirements involve having a certain amount of full-time equivalent radiologists
working in the facility for image diagnosis 462. Smaller hospitals usually in rural
settings may not fulfil the requirements to be reimbursed for the introduction
of AI solutions in diagnostics.



10.10.3.3        Organisational and business challenges

According to one healthcare professional interviewed, the introduction of any new
technology necessitates a thorough assessment of its added value to ensure the
selection of the most suitable solution.. According to the hospital representative,
extensive internal discussions took place among radiologists, the hospital


461 Reference only available in Japanese: Japanese Society of Radiological Medicine. 2024. List of AI
Software Certifications. Available at: https://www.radiology.jp/member_info/ai_softwear_ninsyou.html
462 Reference only available in Japanese, template on requirements to receive reimbursement for the use
of AI tools in for diagnostic in radiology: https://kouseikyoku.mhlw.go.jp/kinki/r6-t32.pdf
                                           Deployment of AI in healthcare – Final Report


administration, the management board, and other departments to assess the
implications of adopting the AI solution. This included determining whether
  odifications were required to the hospital’s internal IT and infor ation
storage systems. Subsequently, multiple rounds of testing were conducted to
evaluate the solution’s performance and outcomes, ultimately leading to its adoption
once its effectiveness was demonstrated.
Lastly, a significant obstacle highlighted by an interviewed healthcare professional
pertains to the limited time available for training doctors to effectively use the AI
solution. Physicians are often occupied with demanding schedules, and this time
constraint frequently poses a substantial challenge to the introduction of any new
technology. Additionally, some doctors may perceive the training process as an
inefficient use of time that could otherwise be allocated to their primary
responsibilities. Moreover, AI solutions may occasionally require additional time to
generate precise results, which can be challenging for doctors who operate within
strict time constraints. Often, if results are not available within one to two seconds,
many physicians may opt to proceed without them, potentially bypassing the solution's
insights due to the demands of their workflow.

10.10.3.4     Social and Cultural Challenges

As noted by a healthcare professional, the cultural context in Japan influences patients’
expectations regarding diagnoses. Patients prefer that their findings from CT scans be
interpreted and communicated by radiologists rather than by a machine or an AI
solution. A significant proportion of Japanese patients express distrust toward AI-
generated results, as they seek diagnoses from human physicians. Additionally,
concerns regarding the potential misuse of their data for training other AI solutions
contribute to this scepticism.

Moreover, regarding the reluctance of some colleagues within the department to
adopt the AI solution, a healthcare professional observed that more experienced
clinicians often find it challenging to embrace AI deployment. These individuals tend to
view the solution as less of a supportive resource for error prevention, preferring to rely
on traditional manual methods. In contrast, younger generations recognise the
solution's potential and are generally more receptive to its use. Consequently, this
reluctance appears to correlate with individual careers and attitudes toward technology.
Ultimately, not all radiologists utilise the solution.

Lastly, the hospital representative acknowledged that, after observing the AI solution in
operation, many healthcare professionals who were initially sceptical understood that
the solution serves to assist rather than replace them. Consequently, their concerns
regarding job security and over-reliance on technology significantly diminished.

10.10.4        Accelerators to Deployment

10.10.4.1     Technical and Data

As noted by a healthcare professional, prior to deploying the solution, it was essential
to engage in discussions with the IT department and continuous communication
with the AI developer. The healthcare professional reflected that during the adoption
phase, regular meetings were held with the developers to discuss and promptly resolve
any technical issues that arose. Additionally, since the solution’s implementation had to
align with the specific infrastructure of each hospital, significant customisation was
often required. This customisation process has proven to be a valuable practice, as it
ensures that the existing infrastructure is adequately assessed, and that the solution is
tailored to meet the department’s specific needs effectively.

10.10.4.2       Legal and Regulatory

All of the interviewees highlighted the reimbursement system and financial
incentives established by the Japanese government as an accelerator to the
deployment of AI solutions in healthcare. The reimbursement system in fact aims at
encouraging the integration of AI in clinical settings. In Japan, a unique
reimbursement structure exists, wherein hospitals are not directly reimbursed for the
AI solutions themselves but rather for their management. Initially, reimbursement was
directed toward tools for image digitalisation, later expanding to cover the management
of AI systems. A list specifies reimbursement eligibility for these tools 463. Within this
framework, reimbursement served as a significant driver for the solution's adoption. In
this regard, as highlighted by a hospital representative interviewed, this increased the
incentives for hospital management to accept requests from healthcare professionals on
the possibility to introduce AI solutions in clinical settings.
10.10.4.3       Organisational and Business

A healthcare professional stated that, given the novelty of the solution and the potential
challenges associated with troubleshooting, the developers have shown a high level of
responsiveness and support. Lectures on the solution’s usage were conducted,
accompanied by detailed information on its features and functionalities. Additionally, at
the start of the solution's introduction, an initial training session was conducted,
including both a lecture and hands-on activities that allowed clinicians to familiarise
themselves with the solution. According to the interviewee, providing hands-on
experience and concrete examples of its diagnostic support also serve to encourage
adoption, particularly among younger clinicians.
Another effective practice highlighted by the hospital representative involved
simulating the deployment of the AI solution to assess its impact on workload and
efficiency. This process included measuring reductions in working hours and associated
costs over time, once staff became familiar with the solution. Based on these
simulations, estimates were made regarding the decrease in labour hours and financial
expenditure. Effectiveness was evaluated in terms of potential revenue changes, with
specific consideration for diagnostic AI solutions, as the government has adjusted
reimbursement rates for hospitals adopting AI technologies. By calculating the
financial impact of AI adoption versus non-adoption, hospitals are able to make
informed decisions about investment in such tools.
Lastly, it was observed that appointing a mediator, such as the Chief Information
Officer (CIO), who is fluent in both the technical language of developers and the clinical
language of healthcare providers, proved to be an effective strategy for facilitating the
adoption process and ensuring that solution was aligned with the practical needs of the
hospital and clinicians.


10.10.4.4       Social and cultural

To overcome the reluctance of some healthcare professionals to use the AI solution, a
healthcare professional mentioned that within their healthcare institution, repeated
demonstrations of the AI solutions were conducted. Specifically, cases were


463 https://www.radiology.jp/member_info/ai_softwear_ninsyou.html
                                          Deployment of AI in healthcare – Final Report


shared in which the AI solution successfully identified findings that had been overlooked
by radiologists, thereby highlighting its value as a diagnostic aid. These instances were
presented within the department to illustrate the solution’s effectiveness in supporting
diagnostic accuracy. In the case of another hospital, the healthcare professionals
involved in the development of the solution were willing to provide explanations to those
who were hesitant to use it and conducted several trials to demonstrate its functionality.
Additionally, to address some concerns related to data privacy concerns with the use of
cloud services to start images and reports generated by the AI solution, a hospital
representative interviewed mentioned that further explanation on what is cloud
computing would help to gain acceptance. This refers to the healthcare professionals
constantly explaining to patients what cloud services mean, and how data protection is
guaranteed; but also further efforts could be made on to include more information on
cloud services and AI technologies in the media.


10.10.5        Complementary Actions

In light of the technological and data challenges outlined above, the hospital
representative emphasised the need for enhanced collaboration between
developers and healthcare institutions. Such collaboration would enable developers
to gain a clearer understanding of current market demands and to address potential
barriers, particularly those concerning data accessibility and interoperability.

With regard to the legal and regulatory framework, the reimbursement system
introduced by the Japanese government proved to be successful in encouraging the
uptake of AI solutions in healthcare. In this respect, the hospital representative
emphasised the importance of establishing clear reimbursement mechanisms to
facilitate developers' entry into the market. In rural areas, where the availability of
radiologists is especially limited, deploying AI solutions is crucial to help mitigate the
shortage of medical personnel.

In considering the organisational and business actions required, a healthcare
professional highlighted that diagnostic imaging practices vary among individual
radiologists, underscoring the need for standardised guidelines to promote greater
consistency across hospitals and among radiologists. Specifically, guidelines on utilising
the solution’s findings, as well as on reviewing images based on those findings, would
support uniformity..
Another healthcare professional suggested that for the software to be more effective
within the hospital, efforts should prioritise educating colleagues and physicians
across departments. This initial educational focus would allow for a broader adoption
of the solution. Specifically, healthcare staff should first gain an understanding of the
solution’s features, including its strengths and potential limitations, to foster informed
use. Furthermore, AI solutions that alleviate rather than add to the workload of
healthcare professionals should be prioritised.

Finally, when considering social and cultural aspects, a healthcare professional believed
that it is essential to first establish a professional consensus on the implementation
and usage of AI solutions before introducing these concepts to patients. Ideally,
patients should have a clear understanding of both the benefits and limitations of AI
solutions; therefore, prior to sharing AI-generated results, efforts should be made to
inform patients and, ideally, reach a shared understanding on how these tools should
be utilised in the clinical context. To address their resistance stemming from data
privacy concerns related to the use of cloud services to store data generated by AI
solutions, continuous information might also be provided through newspapers,
websites, and social media. Such efforts would help clarify data management
practices and foster a better understanding of cloud computing among patients.
                                           Deployment of AI in healthcare – Final Report


    10.11     Annex 11 – Monitoring framework
The Commission will oversee the design and operationalisation of the data collection
and reporting of the developed monitoring framework. In this regard, as part of this
study, we have set a list of recommendations on how the data collection and reporting
could be done in an efficient manner.

Based on the monitoring tool developed, the study team proposes a reporting template
which will take the form of a table to be filled out to facilitate the reporting of data as
well as the cross-country comparison. The reporting template lists each recommended
action and the corresponding indicators that will inform on the level of implementation
and effectiveness of each action.

For each indicator, the data collectors will fill up the information and include the source
from which the information was retrieved from. When they indicate the source of the
data, a link to the source needs to be included in the column “Link to source of
information”. Additionally, depending on the unit of measurement of each indicator, the
information to be provided in this column will differ. In some cases, specific figures are
requested such as the number of assurance labs established in each Member State. In
other cases, a binary (yes or no) response is requested on, for instance, whether a
central data repository has been created or not. For qualitative information, data
collectors will include free text always with a mandatory link where to find the
information included in the value cell. In the table below we have included an illustrative
example of the reporting template for the considerations for future actions.
                                                                    Table 12: Monitoring framework template
                                                                                Type of                                                                              Reporting
   Consideration        Evaluation question                Target                                  Indicator               Data source            Limitations
                                                                               Indicator                                                                              method

Establishing common standards for data governance, privacy, and interoperability




                                                                                                                                                 No information
                                                                                                                      Desk research: EU          with regard to        Single
                                                                                           Establishment of common    official communications                        reporting
                                                                                                                                                 the
                                                                                           EU standards on data
                                                                                Output                                                           establishment
                                                                                           formats, protocols and
                                                                                                                                                 of other
                                                                                           metadata
                                                                                                                                                 national
                                                                                                                                                 standards


Rules to standardise   Are data formats,         All data formats, protocols
data formats,          protocols and metadata    and metadata follow
protocols and          standardised across the   common standards across                                                                                              Annual
metadata               EU?                       the EU
                                                                                                                                                 Data on
                                                                                           Estimated percentage of                               number of
                                                                                                                      Desk research: hospitals
                                                                                           data that follows the                                 standardised
                                                                               Outcome                                using standard data                           Upon request
                                                                                           common EU standard                                    data may not
                                                                                                                      format
                                                                                           format                                                be up to date or
                                                                                                                                                 comprehensive
                                                                                                                      Surveys with AI
                                                                                           Higher number of AI
                                                                                                                      developers, healthcare
                                                                                Impact     integrated into various                               Responses
                                                                                                                      professionals, and
                                                                                           healthcare systems                                    collected from a
                                                                                                                      hospital representatives
                                                                                                                                                 sample of          Upon request
                                                                                           Improved data exchanges                               stakeholders
                                                                                                                      Surveys with healthcare
                                                                                           / improved                                            may not be
                                                                                Impact                                professionals/hospital
                                                                                           interoperability between                              representative
                                                                                                                      representatives
                                                                                           healthcare organisations
                                                                                                                      Deployment of AI in healthcare – Final Report




                                                                                                                                                 No information
                                                                                                                                                 with regard to
                                                                                        Establishment of common                                  the
                                                                                        EU standards on data          Desk research: EU          establishment         Single
                                                                              Output
                                                                                        formats, protocols and        official communications    of other            reporting
Standards on                                                                            metadata                                                 national
mechanisms to          Are mechanisms to         Mechanisms to support                                                                           standards
support real-time      support real-time data    real-time data exchanges
data exchanges, for    exchanges standardised    follow common standards
both primary and       across the EU?            across the EU                                                                                   Responses
secondary use                                                                           Increase in the flow of       Surveys with healthcare    collected from a
                                                                              Outcome   real-time data exchanges      professionals/hospital     sample of          Upon request
                                                                                        across the EU                 representatives            stakeholders
                                                                                                                                                 may not be
                                                                                                                                                 representative

                                                                                        Funding allocated to                                     Funding plans
                                                                                        incentivise the adoption of   Annual reporting on EU     do not translate
                                                                               Input                                                                                  Annual
                                                                                        interoperable technologies    budgetary plans            in actual
                                                                                        in healthcare institutions                               funding spent
                                                                                                                                                 Data on
                                                                                        Number and type of
                                                                                                                                                 number of
                                                                                        supporting actions to
                                                                                                                      Desk research: EU          supporting
                                                                              Output    incentivise the adoption of                                                 Continuous
                                                                                                                      official communications    actions might
                                                                                        interoperable technologies
                                                                                                                                                 not be up to
                                                                                        in healthcare institutions
                                                                                                                                                 date
                                                                                                                                                 Data on
                                                                                                                                                 number of
Establish incentives                             The adoption of                                                      Desk research:
                       Are there incentives to                                                                                                   interoperable
to adopt                                         interoperable technologies                                           information provided by
                       adopt interoperable                                                                                                       technologies       Continuous
interoperable                                    is incentivised by EU                                                AI developers and
                       technologies in place?                                                                                                    might not be up
technologies                                     institutions                                                         healthcare institutions
                                                                                        Number of interoperable                                  to date or
                                                                              Outcome   technologies adopted by                                  comprehensive
                                                                                        healthcare institutions                                  Responses
                                                                                                                      Surveys with AI            collected from a
                                                                                                                      developers, healthcare     sample of
                                                                                                                                                                    Upon request
                                                                                                                      professionals, and         stakeholders
                                                                                                                      hospital representatives   may not be
                                                                                                                                                 representative
                                                                                        Higher level of               Information on metrics     It might be
                                                                                        interoperability of the       and feedback provided      challenging to
                                                                              Impact                                                                                Upon request
                                                                                        technologies adopted by       by healthcare              evaluate the
                                                                                        healthcare institutions       institutions               increased level
                                                                                                                                                     of
                                                                                                                                                     interoperability

Establishment of Centres of Excellence for AI healthcare

Actual establishment   Are there Centres of                                                                               Desk research: official    Information
                                                   Every EU Member State
of Centres of          Excellence of AI in                                                  Number of Centres of          EU communication, MS       may not be
                                                   has established a Centre of    Output                                                                                Continuous
Excellence of AI in    healthcare established in                                            Excellence established        national authorities’      comprehensive
                                                   Excellence
healthcare             all EU Member States?                                                                              communications             or up to date
                                                                                            Number of advanced            Desk research:             Information
                                                                                            training programmes           information on websites    may not be
                                                                                  Output                                                                                Continuous
                                                                                            offered by Centres of         of Centres of Excellence   comprehensive
                                                                                            Excellence of AI              of AI                      or up to date
                                                                                            Number of healthcare          Desk research:             Information
                                                                                            professionals who             information on websites    may not be
                                                                                  Outcome                                                                               Continuous
                                                                                            participated in the           of Centres of Excellence   comprehensive
                                                   All Centres of Excellence of             training programmes           of AI                      or up to date
                       Do the Centres of
Provision of                                       AI provide advanced                                                                               Responses
                       Excellence of AI provide
advanced training                                  training programmes for                                                                           collected from a
                       advanced training                                                    Level of satisfaction of      Surveys with
programmes for the                                 the healthcare workforce                                                                          sample of
                       programmes for the                                         Outcome   participants to the           participants to training                      Upon request
healthcare workforce                               with high participation and                                                                       stakeholders
                       healthcare workforce?                                                training programmes           programmes
                                                   satisfaction levels                                                                               may not be
                                                                                                                                                     representative
                                                                                                                                                     Responses
                                                                                            Increased number of
                                                                                                                                                     collected from a
                                                                                            healthcare professionals
                                                                                                                          Surveys with healthcare    sample of
                                                                                  Impact    who are willing to deploy                                                   Upon request
                                                                                                                          professionals              stakeholders
                                                                                            AI medical devices in their
                                                                                                                                                     may not be
                                                                                            clinical practice
                                                                                                                                                     representative
                                                                                            Number of digital health      Desk research:             Information
                                                                                            literacy programmes           information on websites    may not be
                                                                                  Output                                                                                Continuous
                                                                                            offered by Centres of         of Centres of Excellence   comprehensive
                                                                                            Excellence of AI              of AI                      or up to date
                                                   All Centres of Excellence of
                                                                                            Number of individuals         Desk research:             Information
                       Do the Centres of           AI provide advanced digital
Provision of digital                                                                        who have participated in      information on websites    may not be
                       Excellence of AI provide    health literacy                Outcome                                                                               Continuous
health literacy                                                                             the digital health literacy   of Centres of Excellence   comprehensive
                       digital health literacy     programmes for the
programmes for the                                                                          programmes                    of AI                      or up to date
                       programmes for the          general public with high
general public                                                                                                                                       Responses
                       general public?             participation and
                                                                                            Level of satisfaction of                                 collected from a
                                                   satisfaction levels                                                    Surveys with
                                                                                            participants to the digital                              sample of
                                                                                  Outcome                                 participants to training                      Upon request
                                                                                            health literacy                                          stakeholders
                                                                                                                          programmes
                                                                                            programme                                                may not be
                                                                                                                                                     representative
                                                                                                                           Deployment of AI in healthcare – Final Report




                                                                                                                                                      Responses
                                                                                             Increased number of                                      collected from a
                                                                                             citizens who are willing to   Surveys with general       sample of
                                                                                   Impact                                                                                Upon request
                                                                                             be treated with AI medical    public                     stakeholders
                                                                                             devices                                                  may not be
                                                                                                                                                      representative
                                                                                             Establishment of a            Desk research:             Information
                                                                                             collaborative environment     information on websites    may not be
                                                                                   Output                                                                                Continuous
                                                                                             for knowledge and best        of Centres of Excellence   comprehensive
                                                                                             practice sharing              of AI                      or up to date
                                                                                             Number of articles,
                                                                                                                           Desk research:
                                                                                             papers, conference                                       Information
                                                                                                                           information on
                                                                                             proceedings, and other                                   may not be
                                                                                   Outcome                                 collaborative                                 Continuous
                                                                                             forms of knowledge                                       comprehensive
                                                                                                                           environment of Centres
                                                                                             available in the                                         or up to date
                                                                                                                           of Excellence of AI
                                                                                             collaborative environment
                                                                                                                           Desk research:
                         Is there a central                                                                                                           Information
                                                    All Centres of Excellence of             Number of best practices      information on
Creation of a            collaborative                                                                                                                may not be
                                                    AI are collaborating and       Outcome   shared among Centres of       collaborative                                 Continuous
collaborative            environment for                                                                                                              comprehensive
                                                    sharing best practices                   Excellence of AI              environment of Centres
environment for          knowledge and best                                                                                                           or up to date
                                                    through the collaborative                                              of Excellence of AI
knowledge and best       practice sharing among
                                                    environment for                                                                                   A high number
practice sharing         Centres of Excellence of
                                                    knowledge                                Number of downloads of                                   of
                         AI?                                                                                               Information provided by
                                                                                             different type of                                        readers/downlo
                                                                                                                           company running the
                                                                                   Outcome   documents available in                                   ads does not       Upon request
                                                                                                                           data repository on
                                                                                             the collaborative                                        imply that they
                                                                                                                           traffic to the website
                                                                                             environment                                              found them
                                                                                                                                                      useful
                                                                                                                                                      Responses
                                                                                             Percentage of
                                                                                                                           Surveys with AI            collected from a
                                                                                             stakeholders who found
                                                                                                                           developers, healthcare     sample of
                                                                                   Outcome   the resources in the                                                        Upon request
                                                                                                                           professionals and          stakeholders
                                                                                             collaborative environment
                                                                                                                           hospital representatives   may not be
                                                                                             relevant and useful
                                                                                                                                                      representative
                                                                                                                                                      No information
                                                                                                                                                      with regard to
                                                                                                                           Desk research:
                                                                                                                                                      the
                         Did the Centres of         Issuance of common                       Issued guidelines for data    information on websites                          Single
                                                                                   Output                                                             establishment
Drafting of guidelines   Excellence of AI draft     guidelines for data                      governance and privacy        of Centres of Excellence                       reporting
                                                                                                                                                      of other
on data governance       common guidelines on       governance and privacy by                                              of AI
                                                                                                                                                      national
and privacy              data governance and        the Centres of Excellence
                                                                                                                                                      standards
                         privacy?                   of AI
                                                                                                                                                      A high number
                                                                                             Number of                     Information provided by
                                                                                   Outcome                                                            of                 Upon request
                                                                                             readers/downloads of the      company running the
                                                                                                                                                      readers/downlo
                                                                                           data governance and          data repository on         ads does not
                                                                                           privacy guidelines           traffic to the website     imply that they
                                                                                                                                                   found them
                                                                                                                                                   useful
                                                                                                                                                   No information
                                                                                                                                                   with regard to
                                                                                                                        Desk research:
                                                                                           Issued protocols to                                     the
                                                                                                                        information on websites                          Single
                                                                                 Output    mitigate biases in AI                                   establishment
                                                                                                                        of Centres of Excellence                       reporting
                                                                                           models                                                  of other
                                                                                                                        of AI
                                                                                                                                                   national
                                                                                                                                                   standards
                                                                                                                                                   A high number
                                                                                                                                                   of
                        Did the Centres of         Issuance of common                                                                              readers/downlo
Drafting of protocols                                                                                                   Information provided by
                        Excellence of AI draft     protocols to mitigate                   Number of                                               ads does not
to mitigate biases in                                                                                                   company running the
                        protocols to mitigate      biases in AI models by        Outcome   readers/downloads of the                                imply that they    Upon request
AI models                                                                                                               data repository on
                        biases in AI models?       Centres of Excellence of AI             protocols                                               found them
                                                                                                                        traffic to the website
                                                                                                                                                   useful or that
                                                                                                                                                   they apply
                                                                                                                                                   them
                                                                                                                                                   Responses
                                                                                                                        Surveys with AI            collected from a
                                                                                           Increased trust in AI
                                                                                                                        developers, healthcare     sample of
                                                                                 Impact    medical devices which                                                      Upon request
                                                                                                                        professionals and          stakeholders
                                                                                           have applied the protocols
                                                                                                                        hospital representatives   may not be
                                                                                                                                                   representative
                                                                                           Release of AI playbook
                                                                                 Output
                                                                                           with regulatory roadmap
                                                                                                                                                   A high number
                                                                                                                                                   of
                                                                                                                        Information provided by
                                                                                           Number of                                               readers/downlo
                                                                                                                        company running the
                                                                                 Outcome   readers/downloads of the                                ads does not       Upon request
                                                                                                                        data repository on
                                                   The Centres of Excellence               AI playbook                                             imply that they
                                                                                                                        traffic to the website
                        Did the Centres of         for AI released an AI                                                                           found them
Development of AI
                        Excellence of AI release   playbook including                                                                              useful
playbooks with
                        an AI playbook including   regulatory roadmap that                                                                         Responses
regulatory roadmap
                        regulatory roadmap?        relevant stakeholders find              Percentage of                Surveys with AI            collected from a
                                                   useful                                  stakeholders who find the    developers, healthcare     sample of
                                                                                 Outcome                                                                              Upon request
                                                                                           AI playbook useful and       professionals and          stakeholders
                                                                                           clear                        hospital representatives   may not be
                                                                                                                                                   representative
                                                                                           Improved understanding                                  Responses
                                                                                                                        Surveys with AI
                                                                                 Impact    of the requirements of the                              collected from a   Upon request
                                                                                                                        developers, healthcare
                                                                                           AI Act leading to increase                              sample of
                                                                                                                                 Deployment of AI in healthcare – Final Report




                                                                                                  implementation of AI           professionals and           stakeholders
                                                                                                  solutions in healthcare        hospital representatives    may not be
                                                                                                                                                             representative

Consolidated funding and introduction of financing mechanisms

                                                                                                  Amount of funding                                          Not all
                                                                                                  provided at EU level to                                    budgetary plans
                                                                                                                                 Annual reporting on EU
                                                                                         Input    support strategic priorities                               may be               Annual
                                                                                                                                 budgetary plans
                                                                                                  for AI in healthcare                                       translated into
                                                                                                                                                             actual funding
                                                                                                                                                             Financing
                                                                                                                                                             mechanisms
                                                                                                  Number of financing                                        may have been
                                                                                                  mechanisms introduced to       Desk research: Official     established but
                                                                                        Output                                                                                  Continuous
                                                                                                  support strategic priorities   EU communication            the numbers of
                                                                                                  for AI in healthcare                                       applicants/awar
Introduction of
                        Are strategic priorities for                                                                                                         ded entities
financing                                              Strategic priorities for AI in
                        AI in healthcare                                                                                                                     may be low
mechanisms to                                          healthcare are supported
                        supported through                                                                                                                    Data may not
support strategic                                      through adequate                                                          Desk research: Official
                        adequate financing                                                        Number of                                                  be up to date or   Upon request
priorities for AI in                                   financing mechanisms                                                      EU communication
                        mechanisms?                                                               projects/initiatives funded                                comprehensive
healthcare                                                                              Outcome
                                                                                                  through the established                                    Data may not
                                                                                                  financing mechanisms           CORDIS database             be up to date or   Continuous
                                                                                                                                                             comprehensive
                                                                                                                                                             Difficulty in
                                                                                                  Strategic priorities for AI                                assessing the
                                                                                                                                 Desk research:
                                                                                                  in healthcare are                                          level of
                                                                                                                                 evaluation reports by
                                                                                                  enhanced via projects                                      achievement of     Continuous/
                                                                                        Impact                                   the Commission
                                                                                                  funded through the                                         strategic          Upon request
                                                                                                                                 services; publications by
                                                                                                  established financing                                      priorities with
                                                                                                                                 relevant stakeholders
                                                                                                  establishments                                             unbiased
                                                                                                                                                             indicators

                                                                                                                                                             No information
                                                                                                  Actual establishment of                                    with regard to
Introduction of a                                                                                 standardised EU-level                                      the
                        Is there a standardised        Establishment of a                                                        Desk research: Official
standardised EU-level                                                                   Output    reimbursement                                              establishment         Single
                        EU-level reimbursement         standardised EU-level                                                     EU communication
reimbursement                                                                                     frameworks for AI in                                       of other            reporting
                        framework for AI in            reimbursement framework
framework for AI in                                                                               healthcare                                                 national
                        healthcare in place?           for AI in healthcare
healthcare                                                                                                                                                   programmes

                                                                                                  Number of                      Information provided by     Data on
                                                                                        Outcome                                                                                 Upon request
                                                                                                  reimbursements provided        competent EU institution    reimbursement
                                                                                       to healthcare institutions                              provided may
                                                                                       for the adoption of AI                                  not be publicly
                                                                                       tools in healthcare                                     available
                                                                                                                                               Responses
                                                                                       Increased percentage of      Survey with AI             collected from a
                                                                                       healthcare institutions      developers, healthcare     sample of
                                                                             Impact                                                                               Upon request
                                                                                       adopting AI medical          professionals, and         stakeholders
                                                                                       devices                      hospital representatives   may not be
                                                                                                                                               representative

Establishment of a centralised body for added-value assessment, local performance testing and post-deployment monitoring of AI solutions

                                                                                                                                               The fact that
                                                                                                                                               funding was
                                                                                       Amount of funding
                                                                                                                                               allocated does
                                                                                       provided at EU and           Annual reporting on
                                                                                                                                               not mean that        Annual
                                                                                       Member State level to        EU/MS budgetary plans
                                                                                                                                               validation labs
                                                                                       establish assurance labs
                                                                              Input                                                            were efficiently
                                                                                                                                               established
                                                                                       EU projects funded with
                                                                                                                                               Missing national
                                                                                       the objective of
                                                                                                                    CORDIS database            funding            Continuous
                                                                                       establishing assurance
                                                                                                                                               initiatives
                                                                                       labs
                                                                                                                                               An assurance
                                                                                                                                               lab may have
                                                                                                                    Desk research: Official    been
Establishment of a                                                                     Number of assurance labs
                                                                             Output                                 MS’ national gazette       established but    Continuous
network of assurance   Is there at least one                                           established
                                                    Every EU Member States                                          reporting, desk research   might not be
labs to test the       assurance lab available in
                                                    has an assurance lab                                                                       efficiently
performance of AI      each EU Member State?
                                                                                                                                               operating
tools for healthcare
                                                                                       Number of AI tools tested
                                                                                       for performance via                                     Data on tested
                                                                                                                    Desk research:
                                                                                       assurance labs                                          AI tools may       Continuous/
                                                                             Outcome                                Information provided by
                                                                                       Number of AI tools                                      not be up to       Upon request
                                                                                                                    assurance labs
                                                                                       validated via assurance                                 date
                                                                                       labs
                                                                                                                    Desk research:
                                                                                                                                               Data on
                                                                                                                    commercial information
                                                                                                                                               adoption rates
                                                                                       Higher adoption rates of     available in AI
                                                                                                                                               of AI tools may
                                                                                       AI tools which have been     developers’ websites,                         Continuous/
                                                                             Impact                                                            not be
                                                                                       validated by assurance       hospitals adopting the                        Upon request
                                                                                                                                               available, nor
                                                                                       labs                         technology;
                                                                                                                                               those not
                                                                                                                    Annual surveys to
                                                                                                                                               validated for
                                                                                                                    collect information
                                                                                                                       Deployment of AI in healthcare – Final Report




                                                                                                                       Eurostat data on            comparison
                                                                                                                       enterprises using AI in     purposes           Continuous
                                                                                                                       the EU (isoc_eb_ai)
                                                                                                                                                   Only AI tools
                                                                                                                       Reporting on post-
                                                                                          Positive evaluation of                                   under the high-
                                                                                                                       market monitoring
                                                                                          post-market monitoring of                                risk
                                                                                                                       system to be
                                                                                          deployed AI tools which                                  categorisation     Continuous
                                                                                                                       established for high-risk
                                                                                          have been validated by                                   are obliged to
                                                                                                                       systems according to
                                                                                          assurance labs                                           comply with
                                                                                                                       Article 72 EU AI Act
                                                                                                                                                   this provision.
                                                                                                                                                   The fact that
                                                                                                                                                   funding was
                                                                                                                                                   allocated does
                                                                                                                                                   not mean that
                                                                                          EU institutions support in
                                                                                                                                                   support in
                                                                                          establishing EU-level
                                                                                                                       Annual reporting on EU      establishing EU-
                                                                                 Input    harmonised standards for                                                    Upon request
                                                                                                                       budgetary plans             level
                                                                                          evaluation according to
                                                                                                                                                   harmonised
                                                                                          Article 40 EU AI Act
                                                                                                                                                   standards for
                                                                                                                                                   evaluation was
                                                                                                                                                   efficiently
                                                                                                                                                   provided
                                                                                                                                                   It might be
                                                                                          Assurance labs’
Establishment of                                                                                                                                   challenging to
                         Do all established                                               infrastructure for
performance                                         All established assurance                                          Information provided by     evaluate the
                         assurance labs use the                                 Output    evaluating AI models with                                                   Upon request
benchmarks designed                                 labs use the same set of                                           assurance labs              quality of
                         same set of performance                                          the same performance
for different AI tools                              performance benchmarks                                                                         assurance labs’
                         benchmarks which are                                             benchmarks
to be used by                                       adequately testing the                                                                         infrastructure
                         adequately testing the
performance testing                                 performance of AI tools                                                                        Data on
                         performance of AI tools?
centres                                                                                                                Information provided by     evaluated AI
                                                                                                                                                                      Upon request
                                                                                                                       assurance labs              models may not
                                                                                          Increased level of
                                                                                                                                                   be up to date
                                                                                          accuracy, reliability and
                                                                                                                                                   Only AI tools
                                                                                          safety as measured in the    Reporting on post-
                                                                                Outcome                                                            under the high-
                                                                                          evaluations of AI models     market monitoring
                                                                                                                                                   risk
                                                                                          carried out by assurance     system to be
                                                                                                                                                   categorisation     Continuous
                                                                                          labs                         established for high-risk
                                                                                                                                                   are obliged to
                                                                                                                       systems according to
                                                                                                                                                   comply with
                                                                                                                       Article 72 EU AI Act
                                                                                                                                                   this provision.
                                                                                                                       Desk research:              Data on quality
                                                                                          Higher performance           commercial information      of AI models
                                                                                Impact                                                                                Continuous
                                                                                          standards of AI tools        available in AI             may not be
                                                                                                                       developers' websites,       available
                                                                                                                   hospitals adopting the
                                                                                                                   technology
                                                                                                                                               Data on
                                                                                                                                               sandbox
                                                                                                                   Information provided by
                                                                                                                                               environments        Continuous/
                                                                                                                   assurance labs in their
                                                                                                                                               may not be up       Upon request
                                                                                                                   website
                                                                                                                                               to date or
                                                                                                                                               comprehensive
                                                                                      Number of sandbox
                                                                                                                                               Information on
                                                                            Output    environments established
                                                                                                                                               activities
                                                                                      in assurance labs
                                                                                                                                               successfully
                                                                                                                   Reporting on compliance
                                                                                                                                               carried out by
                                                                                                                   with Article 57 of the EU                       Upon request
                                                                                                                                               in the sandbox
                                                                                                                   AI Act
                                                                                                                                               only collected
                                                                                                                                               upon request
                                                                                                                                               (Article 57(7))
                                                                                      Number of issued “Model
                                                                                                                                               Data on
                                                                                      Report Card” or “Model
                                                                                                                                               sandbox
Provision of sandbox   Do all assurance labs      Every assurance lab                 Fact Label”                  Information provided by
                                                                                                                                               environments        Continuous/
environment to test    provide sandbox            provides a sandbox                  Number of successfully       assurance labs in their
                                                                                                                                               may not be up       Upon request
the performance of     environments to test the   environment to test the             issued “Model Report         website
                                                                                                                                               to date or
AI tools               performance of AI tools?   performance of AI tools             Card” or “Model Fact
                                                                            Outcome                                                            comprehensive
                                                                                      Label”
                                                                                                                   Information provided by     Potential lack of
                                                                                                                   national competent          standardisation
                                                                                      Number of exit proofs
                                                                                                                   authorities as              on information      Continuous
                                                                                      issued
                                                                                                                   established by Article      provided in
                                                                                                                   57(7) of EU AI Act          these proofs
                                                                                                                   Desk research:
                                                                                                                   commercial information
                                                                                                                                               It might be
                                                                                                                   available in AI
                                                                                                                                               challenging to
                                                                                                                   developers’ websites,
                                                                                      Enhanced trust and                                       evaluate the
                                                                                                                   hospitals adopting the                          Continuous/
                                                                            Impact    reliability on tested AI                                 increase in trust
                                                                                                                   technology,                                     Upon request
                                                                                      tools                                                    and reliability
                                                                                                                   Annual surveys to
                                                                                                                                               following
                                                                                                                   collect information from
                                                                                                                                               testing
                                                                                                                   HCPs using AI tools as
                                                                                                                   well as patients
                                                                                      Creation of a central data   Desk research: EU
Promote                                                                     Output                                                                     -           Continuous
                       Did the EU Member                                              repository                   official communications
collaboration across
                       States create a central    Member States have a                Number of collaboration
EU Member States                                                                                                                               Not all
                       data repository to         central data repository             partnerships across EU       Desk research: data
with a central data                                                         Outcome                                                            collaboration       Continuous
                       enhance collaboration?                                         Member States on             repository website
repository                                                                                                                                     partnerships
                                                                                      healthcare data
                                                                                                                           Deployment of AI in healthcare – Final Report




                                                                                                                                                     might be
                                                                                                                                                     published
                                                                                                                                                     A high number
                                                                                                                           Information provided by
                                                                                                                                                     of visitors does
                                                                                             Level of use of the           company running the
                                                                                   Outcome                                                           not imply a         Continuous
                                                                                             repository                    data repository on
                                                                                                                                                     high level of
                                                                                                                           traffic to the website
                                                                                                                                                     engagement
                                                                                                                                                     No information
                                                                                             Enhanced collaboration        Information provided by   available for the
                                                                                   Impact                                                                                Upon request
                                                                                             across EU Member States       Member States             quality of the
                                                                                                                                                     collaborations
                                                                                             The central data
                                                                                                                           Desk research: EU
                                                                                   Output    repository includes good                                        -           Continuous
Collection and          Did the centralised body                                                                           official communications
                                                     Collection and                          practice case studies
dissemination of        collect and disseminate
                                                     dissemination of good                                                                           Databases
good practice case      good practice case                                                   Number of good practice
                                                     practice case studies                                                 Desk research: data       might not be up
studies                 studies?                                                   Outcome   case studies in the                                                         Continuous
                                                                                                                           repository website        to date or
                                                                                             repository
                                                                                                                                                     comprehensive

Development of a catalogue of AI solutions
                                                                                             Release of a catalogue of
                                                                                             AI solutions including
                                                                                             detailed performance          Desk research: EU                                Single
                                                                                   Output                                                                    -
                                                                                             metrics for each listed AI,   official communications                        reporting
                                                                                             user reviews, and
Include detailed        Does the catalogue of AI     The catalogue of AI                     feedback mechanisms
performance metrics     solutions include detailed   solutions includes detailed             Number of AI tools listed                               Database might
for each listed AI      performance metrics for      performance metrics for                 with detailed performance     Desk research: website    not be up to
                                                                                   Outcome                                                                               Continuous
tool, user reviews,     each listed AI, user         each listed AI, user                    metrics, user reviews, and    of the catalogue          date or
and feedback            reviews, and feedback        reviews, and feedback                   feedback mechanisms                                     comprehensive
mechanisms              mechanisms?                  mechanisms
                                                                                                                                                     A high number
                                                                                                                           Information provided by
                                                                                                                                                     of visitors does
                                                                                             Number of visitors to the     company running the
                                                                                   Outcome                                                           not imply a         Continuous
                                                                                             catalogue of AI solutions     data repository on
                                                                                                                                                     high level of
                                                                                                                           traffic to the website
                                                                                                                                                     engagement

Include user guides,                                 The catalogue of AI                     Inclusion of user guides,                               Database might
                        Does the catalogue of AI
case studies, and                                    solutions includes user                 case studies, and tutorials   Desk research: website    not be up to
                        solutions include user                                     Output                                                                                Continuous
tutorials, helping                                   guides, case studies, and               in the catalogue of AI        of the catalogue          date or
                        guides, case studies, and
healthcare providers                                 tutorials, helping                      solutions                                               comprehensive
                        tutorials, helping
understand and                                       healthcare providers
                        healthcare providers                                                 Number of user guides,        Desk research: website    Database might
implement AI                                         understand and implement      Outcome                                                                               Continuous
                        understand and                                                       case studies, and tutorials   of the catalogue          not be up to
solutions efficiently                                AI solutions efficiently
                      implement AI solutions                                           available in the catalogue                             date or
                      efficiently?                                                     of AI solutions                                        comprehensive
                                                                                       Establishment of a
                                                                                                                                              Database might
                                                                                       governance framework to
                                                                                                                    Desk research: website    not be up to        Single
                                                                             Output    oversee the catalogue’s
                                                                                                                    of the catalogue          date or           reporting
                                                                                       operations within the AI
                                                                                                                                              comprehensive
                                                                                       catalogue
                                                                                                                                              Data on
Establishment of a    Does the catalogue of AI   The catalogue of AI                   Number of catalogue’s        Desk research:
                                                                                                                                              operations may
governance            solutions include a        established a governance              operations overseen by       Information provided by
                                                                             Outcome                                                          not be up to     Upon request
framework to          governance framework to    framework to oversee                  the governance               the governance
                                                                                                                                              date or
oversee catalogue’s   oversee catalogue’s        catalogue’s operations                framework                    framework
                                                                                                                                              comprehensive
operations            operations?                which is up to date
                                                                                                                    Desk research:            It may be
                                                                                                                    commercial information    challenging to
                                                                                       Higher governance
                                                                                                                    available in AI           assess the
                                                                             Impact    standards in catalogue’s                                                Upon request
                                                                                                                    developers’ websites,     increase in
                                                                                       operations
                                                                                                                    hospitals adopting the    governance
                                                                                                                    technology                standards
                                                                        Source: Authors’ elaboration
                                          Deployment of AI in healthcare – Final Report




GETTING IN TOUCH WITH THE EU

In person

All over the European Union there are hundreds of Europe Direct information centres.
You can find the address of the centre nearest you at: https://europa.eu/european-
union/contact_en

On the phone or by email

Europe Direct is a service that answers your questions about the European Union. You
can contact this service:

- by freephone: 00 800 6 7 8 9 10 11 (certain operators may charge for these calls),

- at the following standard number: +32 22999696, or

- by electronic mail via: https://europa.eu/european-union/contact_en

FINDING INFORMATION ABOUT THE EU

Online

Information about the European Union in all the official languages of the EU is
available on the Europa website at: https://europa.eu/european-union/index_en

EU publications

You can download or order free and priced EU publications from EU Bookshop at:
https://publications.europa.eu/en/publications. Multiple copies of free publications
may be obtained by contacting Europe Direct or your local information centre (see
https://europa.eu/european-union/contact
   doi: 10.2875/2169577
ISBN 978-92-68-28758-3
