# Artificial Intelligence Adoption for Sustainable Growth in SMEs: An Extended Dynamic Capability Framework

**Authors:** Antonio Cimino, Vincenzo Corvello, Ciro Troise, Asha Thomas, Mario Tani
**Affiliations:** University of Messina (Cimino, Corvello); University of Turin (Troise, corresponding); Wrocław University of Science and Technology (Thomas); University of Naples Federico II (Tani)
**Journal:** Corporate Social Responsibility and Environmental Management, 2025; 32(5): 6120–6138
**DOI:** 10.1002/csr.70019
**URL:** https://onlinelibrary.wiley.com/doi/10.1002/csr.70019
**Received / Revised / Accepted:** 30 March 2025 / 28 May 2025 / 31 May 2025
**Published online:** 2025-06-15 (Crossref `published-online`; print issue 2025-09)
**Licence:** CC BY 4.0 (open access)
**Captured:** 2026-09-17 (user-supplied PDF, Wiley Online Library via Hogeschool van Arnhem en Nijmegen)
**fulltext_source:** pdf-converted
**converter:** pdftotext (default reading-order mode; `-layout` used separately to recover tables)
**pages:** 19 (journal pp. 6120–6138 — complete article)
**raw PDF:** `raw/papers/2025-06-15-cimino-ai-adoption-sustainable-growth-smes.pdf` (gitignored)

---

## Pre-flight checks

**Check 1 — Scope.** 19 PDF pages against journal pagination 6120–6138 = 19 pages. Complete
article, front matter through references. Not a sample or excerpt.

**Check 2 — Identity.** The on-disk filename supplied by the user was
`Corp Soc Responsibility Env - 2025 - Cimino - Artificial Intelligence Adoption for Sustainable
Growth in SMEs  An Extended.pdf` — a truncated Wiley export name. Cover page, DOI, and the
Crossref record all agree on the identity above; renamed to the wiki slug on acquire. No
mismatch.

**Check 3 — Honest scoping.** Full text read. `pdftotext` default mode resolves the two-column
layout into correct reading order but flattens all seven tables and both figures; the
`-layout` pass was used to recover Table 1 (sample), Table 3 (reliability), Tables 4–5
(discriminant validity), Table 6 (VIF) and Table 7 (path coefficients). **Figures 1 and 2 (the
theoretical model diagram and the structural-model result diagram, which carries the R² values)
are images and did not survive conversion — R² is not recoverable from this file.**

## Data-quality note (prose vs. Table 7)

The discussion prose and Table 7 disagree on several coefficients, and the significance legend
is incomplete. Table 7's `Support` column is the authoritative verdict and is what the wiki
source page cites.

- H1 `DC➔TP`: prose β = 0.47, Table 7 β = 0.447.
- H9 `AIAI➔CP`: prose β = 0.288, Table 7 β = 0.268.
- H12 `AIAR➔EP`: prose reports "p = 0.010" while calling the hypothesis rejected; Table 7 gives
  T = 1.264 with CI [−0.053, 0.242], which straddles zero. The CI is the basis for rejection;
  the quoted p-value appears to be an error.
- H13 `AIAR➔CP`: prose "p = 0.061"; Table 7 β = −0.108, CI [−0.238, 0.033].
- The table legend defines `**p < 0.05` and `***p < 0.001` but the `*` used on H2 (0.138*) is
  never defined, and H8 is starred `**` though the prose claims p < 0.001.

## Why acquired

Direct extension of the Warner & Wäger (2019) lens the wiki already runs as its
`dynamic_capabilities:` tagging vocabulary — same sensing/seizing/transforming spine, but
quantified via PLS-SEM on 210 firms rather than derived from 32 interviews, and applied to
early-stage SMEs rather than incumbents.

---

Corporate Social Responsibility and Environmental Management

RESEARCH ARTICLE

OPEN ACCESS

Artificial Intelligence Adoption for Sustainable Growth in
SMEs: An Extended Dynamic Capability Framework
Antonio Cimino1

| Vincenzo Corvello1 | Ciro Troise2

| Asha Thomas3 | Mario Tani4

1Department of Engineering, University of Messina, Messina, Italy

| 2Department of Management, University of Turin, Turin, Italy | 3Department
of Operations Research and Business Intelligence, Wrocław University of Science and Technology, Wrocław, Poland | 4Department of Economics,
Management, Institutions, University of Naples Federico II, Naples, Italy
Correspondence: Ciro Troise (ciro.troise@unito.it)
Received: 30 March 2025 | Revised: 28 May 2025 | Accepted: 31 May 2025
Keywords: artificial intelligence | dynamic capabilities | SMEs | triple bottom line

ABSTRACT

The adoption of Artificial Intelligence is transforming enterprises worldwide, influencing various aspects of business operations and affecting all dimensions of the triple bottom line. Companies ready to leverage the potential of this technology can
significantly improve their performance. Therefore, it is crucial to understand the relationship between internal capabilities
and contextual factors on one hand, and Artificial Intelligence adoption and its impact on performance on the other. Within
this research framework, this study introduces an extended dynamic capability framework to analyze the interplay between
internal factors, Artificial Intelligence adoption, and companies performance. The proposed model is tested using Partial Least
Squares—Structural Equation Modeling on survey data from 210 Italian innovative startups. The findings indicate that companies with well-developed dynamic capabilities, enabling them to adapt more effectively to environmental changes, are also better
equipped to adopt Artificial Intelligence, leading to positive social, economic, and environmental performance.

1   |   Introduction
For the last few years, Artificial Intelligence (AI) has been a
dominant topic of discussion across a vast number of industries (Tutore et al. 2024). According to the McKinsey Global
Survey (2018), the adoption of AI is rapidly gaining traction
across businesses worldwide (McKinsey 2018). Alongside this
discourse, the adoption of AI solutions has accelerated rapidly,
with corporate investments in AI reaching nearly 92 billion
USD in 2022 and estimates projecting an even more dramatic expansion in the coming years (Thormundsoon 2024).
Unsurprisingly, these investments have had a transformative
impact across industries, with organizations of every stripe integrating AI-d riven technologies and processes into their core
operations. In fact, it is now commonly believed that adopting
and implementing AI automation and optimization is essential for any organization that wishes to gain a competitive advantage in the current market (Davenport and Ronanki 2018;

Duan et al. 2019; Yang et al. 2024). With AI playing an increasingly significant role in business, research on small-scale
organizations and startups is crucial for understanding AI
adoption (Rawashdeh et al. 2023). While large firms are able
to marshal substantial resources and leverage their R&D departments to drive incremental innovation, smaller firms have
a distinct advantage when it comes to digital technologies. In
fact, startups, rather than large corporations, often take the
leading role with disruptive innovations such as AI, due to
their agility and ability to engage in riskier decision-making
(Cohen 2010). The literature also highlights the transformative impact of digital technologies like AI, IoT, blockchain,
and social media on SME entrepreneurship (Li et al. 2017;
Islam et al. 2024; Kimani et al. 2020; Chatterjee et al. 2022;
Arranz et al. 2023; Thomas 2024). Among these technologies,
AI has received particular attention for its diverse applications
and strategic potential within SMEs. Cooper (2025) highlights
that the most common applications of AI in SMEs include

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium,
provided the original work is properly cited.
© 2025 The Author(s). Corporate Social Responsibility and Environmental Management published by ERP Environment and John Wiley & Sons Ltd.

https://doi.org/10.1002/csr.70019

Within this research context, the aim of this study is to provide a framework for understanding how firms' Dynamic
Capabilities (DC) facilitate AI adoption and enhance firms'
sustainability across four critical dimensions: technological
performance (TP), economic performance (EP), collaborative
performance (CP), and sustainable performance (SP). This
framework also advances existing research by differentiating
two distinct aspects of AI adoption: AI Adoption Intensity
(AIAI), which represents the extent to which AI has been integrated into a firm's processes (Chen and Tajdini 2024), and AI
Acceptance Rate (AIAR), which reflects a firm's openness to
and readiness for adopting AI solutions (Almaiah et al. 2022).
Introducing this distinction addresses a critical gap in the
literature, which has traditionally examined DC's direct effects on AI adoption without exploring the distinct pathways
through which AI adoption influences a firm's sustainability
across various dimensions. Furthermore, while there is published research on the influence of AI adoption on a firm's
sustainability, there is currently no study that examines AI's
impact on distinct categories of sustainability metrics, namely,
technological, economic, collaborative, and sustainable, in
a holistic way. Some of the studies on the subject examine
overall organizational performance (Vanpoucke et al. 2014;
Ringov 2017; Wamba et al. 2024; Pundziene et al. 2022), while
others focus on specific dimensions and specifically innovation performance (Falasca et al. 2017), competitive and strategic performance (Fang and Zou 2009; Pundziene et al. 2022),
and lastly economic and financial performance (Ringov 2017;
Eslami et al. 2024). To date, however, to the best of the authors
knowledge, none of the research has taken performance in a
holistic way to uncover some of the nuances that may exist
when various aspects of firm performance are compared.
Likewise, there is room to explore this topic more closely from
the DCs approach. A recent systematic review by Baía and
Ferreira (2024) analyzed 92 studies on the relationship between
DC and firms' performances, with 24 of the studies testing the

direct impact of DCs on firms' performances and 32 taking a
mixed approach by measuring both its direct and indirect effects. However, none of the studies examine how DCs influence
firms' performances when mediated through the concepts of
AIAI and AIAR. This limits the ability to form a holistic understanding of the role these capabilities play in AI-driven organizational transformation. Studying how AIAI and AIAR
influence firms' sustainability performances would allow us to
uncover how firms strategically deploy DCs to drive AI adoption, enhance organizational capabilities, and achieve a sustainable competitive advantage. This research study focuses
specifically on a particular subset of SMEs, namely, innovative
startups at their early stages.
The remainder of the paper is organized as follows: Section 2 introduces the study's theoretical background, including the proposed theoretical model, and the formulation of hypotheses to
guide the research. Section 3 details the methodology employed,
including the procedure used for empirical analysis. Section 4
presents the study's results, followed by a discussion of the key
findings in Section 5. Section 6 summarizes the key theoretical
and practical implications of the study. Section 7 concludes the
paper by discussing its limitations and presenting potential avenues for future research.

2   |   Theory
2.1   |   Theoretical Background
This study is grounded in DC theory (Teece et al. 1997;
Teece 2007, 2014) to examine how SMEs' dynamic capabilities influence AI adoption and sustainable growth across
four key performance dimensions: TP, EP, CP, and SP. TP is
strongly influenced by DCs, as these capabilities enable firms
to sense emerging technological trends, seize innovation opportunities, and reconfigure internal processes to foster technological advancement (Deeds et al. 2000; Kunanoppadol and
Igel 2023). EP benefits from DCs that support agile resource
reallocation and strategic responsiveness to market shifts,
thus improving operational efficiency and financial outcomes
(Wang et al. 2015; Aftab et al. 2024). However, some scholars question the consistency of this relationship, noting that
the link between DCs and financial performance may depend
on contextual or executional factors (Wilden et al. 2013). CP
is shaped by a firm's dynamic ability to identify, initiate, and
maintain effective internal and external relationships. In
addition, sensing collaboration opportunities enable the creation of ecosystems (Barreto 2010). SP is supported by DCs
that help firms anticipate environmental and societal expectations and adapt their strategies accordingly. The transforming
component of DCs is particularly relevant for embedding sustainability into core business practices (Dangelico et al. 2017;
Hoai et al. 2023; Zhao et al. 2025). While all four performance
dimensions are conceptually linked to DC theory, their relationship with internal capabilities may vary in emphasis and
impact depending on the firm's organizational age and learning modes (Zahra et al. 2006).
Numerous studies have investigated the impact of dynamic capabilities on SME's performance. For instance,

market analysis, project and product portfolio management,
as well as the analysis of unstructured text from market research studies. AI solutions are also employed by SMEs for
predictive analytics and the automation of business processes
(Wei and Pardo 2022). Furthermore, Lu et al. (2022) outline
both AI-enabled opportunities and transformation challenges
for SMEs. Among the opportunities are process improvement
and optimization, real-time customer insights, product and
service innovation, risk reduction, and demand forecasting.
The main challenges, on the other hand, are primarily related to organizational readiness, technical limitations, and
environmental threats. Additionally, Mugisha et al. (2025)
highlight the use of AI-powered chatbots by SMEs to enhance
customer engagement, resolving common issues and assisting
human agents in handling more complex customer queries. In
parallel, Kant and Johannsen (2022) present several AI-d riven
use cases aimed at strengthening cybersecurity defenses for
SMEs. Given the increasingly widespread adoption of AI technologies among SMEs, it becomes essential to investigate the
underlying dynamics that drive AI adoption and implementation with the aim of delving into the strategic role AI plays in
enhancing competitiveness and ensuring the long-term sustainability of these entrepreneurial firms.

In addition, DC theory posits that firms must continuously
sense, seize, and reconfigure resources in response to external pressures, such as market dynamics, competition, and
technological advancements, making it particularly relevant
for understanding AI adoption in dynamic environments
(Teece 2014; Sjödin et al. 2023). Chen et al. (2023) adopt a dynamic capability perspective to explore the antecedents and
outcomes of AIAI in the marketing sector. Aljarboa (2024) examines the key factors influencing AI adoption in e-commerce
among SMEs. This study further advances the DC theory
by offering a process-level explanation of how firms use AI
adoption to translate their sensing, seizing, and transforming
capabilities into technological, economic, collaborative, and
sustainable performance outcomes. Specifically, the study
introduces a dual-pathway operationalization of AI adoption:
AIAI, which reflects the degree to which AI has been embedded into the firm's internal systems and processes (Chen and
Tajdini 2024), and AIAR, which represents the firm's internal
openness and preparedness to adopt and scale AI solutions
(Almaiah et al. 2022). In doing so, this study unpacks the internal mechanisms through which firms implement digital
technologies, offering new insight into the dynamics of AI-
enabled transformation, particularly within the context of
innovative startups and SMEs operating in rapidly evolving
environments.

2.2   |   Theoretical Model
In this research study, the principles of the DC theory are used
to develop a theoretical model with the aim of exploring the relationship between SMEs behavior, AI adoption, and firm sustainability. Specifically, the model investigates how SMEs behavior
influences the adoption of AI technologies and how, in turn, AI
adoption affects their sustainability. Additionally, the study also
investigates the direct impact of SMEs behavior on their sustainability. By analyzing these relationships, the aim is to understand the interplay among all the model's variables through a
holistic perspective on their dynamics.
SME behavior has been approached through the lens of DC
theory (Teece et al. 1997; Teece 2007, 2014), using a second-
order construct called DC. This construct has been operationalized through the three key components of the theory: Sensing,
Seizing, and Transforming. Sensing refers to the firm's capacity
to identify, understand, and respond to signals from the external
environment in order to detect arising opportunities and threats
(Teece 2014; Corvello et al. 2023). Seizing refers to the firm's
ability to act quickly upon identified opportunities by managing
resources and implementing strategic initiatives (Teece 2014;
Corvello et al. 2023). Transforming refers to the firm's ability

to adapt and reorganize its resources and processes to align
with market conditions and maintain competitive advantage
(Teece 2014; Corvello et al. 2023).
The adoption of AI by SMEs has been conceptualized through
two distinct variables: AIAI and AIAR. Following the study by
Chen and Tajdini (2024), AIAI is defined as the extent to which
AI has been integrated into the firm's processes. Meanwhile,
based on the work of Almaiah et al. (2022), AIAR has been defined as the degree to which a firm is open to and prepared for
adopting AI technologies.
Finally, SMEs sustainability is addressed across four performance dimensions: TP, EP, CP, and SP. TP is defined as a firm's
ability to develop, introduce, and commercialize new products
or technological innovations within its market. This definition is derived by combining key aspects from the studies of
Hagedoorn and Cloodt (2003) and Chen and Chen (2006).
Based on the study from Vo Thai et al. (2024), EP has been
defined as a firm's ability to generate financial returns, sustain profitability, and optimize its operational effectiveness
over time. CP has been defined as a firm's ability to effectively
engage and cooperate with their stakeholders to drive innovation, share resources and reach mutual goals. This definition is derived from the analysis of the works by Fawcett
et al. (2011) and Liu et al. (2022). Finally, SP refers to a firm's
commitment to environmental and social responsibility in
terms of resource efficiency, environmental protection, and
long-term sustainability in its operations and business model
(Rauter et al. 2018; Shen et al. 2020). The proposed theoretical
model is depicted in Figure 1.

2.3   |   Hypotheses Development
2.3.1   |   Dynamic Capabilities and Firms' Performance
Researchers have emphasized the critical role of dynamic
capabilities in improving the performance of firms, establishing a competitive advantage, and securing a sustainable
market presence (Teece et al. 1997; Teece 2007; Laaksonen and
Peltoniemi 2018; Choi et al. 2019; Khan et al. 2020). Teece (2007)
classifies these capabilities into three distinct categories: sensing capabilities (allowing firms to identify new opportunities),
seizing capabilities (enabling firms to capitalize on emerging opportunities by designing new products, adapting business models, and engaging in innovation), and reconfiguring capabilities
(optimizing resource use through asset redeployment, resource
management, and process refinements). Together, these capabilities contribute to various aspects of a company's success,
including its profitability, efficiency, growth, market share,
and customer satisfaction (Griffith et al. 2006; Wu 2010; Chien
and Tsai 2012). These are particularly essential in dynamic environments, where firms must continuously accumulate new
capabilities and develop new products to improve profitability
and maintain an advantage over the competition (Blonigen and
Taylor 2000; Hsu and Wang 2012). While these factors have
been investigated and examined several times over, firm performance has often been studied as a singular construct, which
does not reflect its multifaceted character. This study seeks to
address this by categorizing firm sustainability into four distinct

Eikelenboom and de Jong (2019) analyze how integrative dynamic capabilities influence the social, environmental, and
economic performance of SMEs in the Netherlands. Similarly,
Hernández-L inares et al. (2020) assess the individual effects of dynamic capability dimensions on firm performance
using a sample of 509 Spanish SMEs. Furthermore, Rahman
et al. (2023) explore the relationship between dynamic capabilities, SME internationalization, and firm performance in
emerging economies.

performance categories: technological, collaborative, economic,
and sustainable performance.
2.3.2   |   Dynamic Capabilities and Technological
Performance
While Schumpeter identified five types of innovation
(Fagerberg 2005), research has primarily evaluated technological performance through product and process innovations
(Edquist 2005). For the purposes of this study, product innovation is defined as the introduction of products that differ
significantly from previous ones due to the application of technology (OECD 2018). Process innovation, meanwhile, refers
to the use of technology to enhance the efficiency, quality, or
cost-effectiveness of production or delivery methods. As such,
generally, product innovation is based on the proportion of total
sales generated from newly introduced products and process innovation performance is based on the number of successfully
completed innovation projects that lead to new products, processes, or services.
Research shows that organizations with insufficient dynamic
capabilities typically struggle to innovate, primarily due to their
lack of agility and inability to adapt to changing technological
and market environments (Khattab 2017). This is particularly
true in high-tech industries and manufacturing, where the presence of dynamic capabilities is a strong predictor of technological performance and the development of new products (Deeds
et al. 2000; Kunanoppadol and Igel 2023). Based on these findings, the following hypothesis is proposed:

H1. Dynamic Capabilities (DC) positively influence SMEs'
Technological Performance (TP).

2.3.3   |   Dynamic Capabilities and Economic
Performance
Economists widely acknowledge that a firm's ability to advance
technologically has a direct impact on its economic outcomes
and market position (Piening and Salge 2015). Recently, this has
been highlighted by the significant role of AI in driving market
success, with companies that readily adopt AI seeing gains in
productivity, reduced wasted through optimized resource allocation, and a stronger competitive advantage over companies
that lag behind in adopting the technology. Dynamic capabilities enable firms to adopt new income-generating models, such
as revenue sharing, while simultaneously minimizing their cost
of operations (Drnevich and Kriauciunas 2011). This allows
them to improve performance and respond swiftly and efficiently to market turbulence (Chmielewski and Paladino 2007).
Fainshmidt et al. (2017) provide evidence of this enhanced
economic performance by showing that dynamic capabilities
positively impact the return on assets (ROA) of multinational
enterprises. Similarly, Wang et al. (2015) demonstrate that dynamic capabilities contribute to growth in sales and profitability
in UK high-tech small and medium-sized firms. Furthermore,
the positive role of dynamic capabilities in shaping firms' financial performance was evidenced by Aftab et al. (2024) through a
survey conducted among 755 manufacturing firms in Pakistan.
While a number of studies find a link between dynamic capabilities and economic performance, not all researchers are
convinced. Wilden et al. (2013), for example, found that these
capabilities do not have a significant direct impact on financial
solvency and may even negatively affect sales growth. However,
the findings are nuanced, showing that external factors play a
role in how well dynamic capabilities translate to profitability.
For instance, dynamic capabilities drive solvency and growth in

FIGURE 1    |    Theoretical model.

H2. Dynamic Capabilities (DC) positively influence SMEs'
Economic Performance (EP).

2.3.4   |   Dynamic Capabilities and Collaborative
Performance
Collaboration performance is typically defined as achieving a
competitive advantage through collaborative activities, including strategic partnerships and knowledge exchange between organizations (Hurmelinna et al. 2005; Agarwal and Selen 2009,
2013; Roundy et al. 2018; Santos 2022). Internally, organizations
that invest in hiring skilled talent and allow greater flexibility
in their processes provide fertile ground for knowledge sharing
and the innovation that arises from it (Pique et al. 2018; Falcke
et al. 2024). Externally, inter-organizational trust can significantly enhance collaboration and speed the rate of innovation
(Lee et al. 2015). However, while a wider range of interaction
channels improves innovation output, it does not correspond
to greater satisfaction with the collaborations, as SMEs struggle with the operational burden of managing multiple channels
with limited resources. Barreto (2010) notes that dynamic capabilities allow firms to integrate both internal and external
collaboration activities by creating ecosystems of stakeholders.
Moreover, collaboration experience has been found to positively
influence innovation output but not satisfaction, due to the rigidity and limited strategic flexibility of partnerships. Overall,
trust emerges as the most critical factor influencing collaboration performance in manufacturing SMEs, and no innovation
can reach its full potential without collaborative support (Haans
et al. 2016). Thus, the following hypothesis is proposed:

H3. Dynamic Capabilities (DC) positively influence SMEs'
Collaborative Performance (CP).
2.3.5   |   Dynamic Capabilities Sustainable Performance
SMEs operating in dynamic business environments face extraordinary challenges to implementing sustainable practices,
since they must implement sustainable practices that will optimize their limited resources and allow them to achieve long-
term sustainability (Chang et al. 2018; Chege and Wang 2020;
Omri 2020). Dynamic capabilities help organizations overcome
these difficulties by making their processes more efficient,
improving their performance, and identifying and seizing on
emerging sustainable innovations (Russo 2003; Chakrabarty
and Wang 2012; Mousavi et al. 2018). Building on Zahra's (1993)
perspective, Wilden et al. (2013) find that high-competition environments push companies to leverage dynamic capabilities
in order to sustain or enhance their performance, rather than
allowing these capabilities to become redundant or contribute
to inefficiencies, they might when competition is low. This underscores the critical role of competitive intensity in driving sustainable performance. Additionally, Hoai et al. (2023) and Zhao

et al. (2025) demonstrate that leveraging dynamic capabilities
can significantly contribute to firms sustainable development.
Furthermore, Taneja et al. (2023) confirmed that dynamic capabilities play a crucial role in advancing firms' sustainability-
oriented goals and in fostering sustainable, long-term competitive
advantages. The link between dynamic capabilities and the
achievement of sustainable competitive advantage has also been
supported by the findings of Qiu et al. (2020) and Andersson
et al. (2022). Furthermore, dynamic capabilities support SMEs
to address sustainability at lower costs (Boons and Lüdeke-
Freund 2013) as well as enable SMEs to increase the success of
their sustainable performances (Dangelico et al. 2017). Based on
these findings, the following hypothesis is proposed:

H4. Dynamic Capabilities (DC) positively influence SMEs'
Sustainable Performance.
2.3.6   |   Dynamic Capabilities and Artificial
Intelligence Adoption
Dynamic capabilities are particularly critical for SMEs in the
context of AI adoption. As Arroyabe et al. (2024) note, SMEs
approach AI implementation through three key processes: opportunity identification (assessing the potential value of AI
technology), resource mobilization (investing in AI-
powered
tool and AI training), and continuous adaptation (refining processes to maximize AI's impact). Notably, this model roughly
corresponds to the dynamic capabilities' framework of sensing,
seizing, and reconfiguring. Deploying these capabilities is crucial for startups and SMEs, as those that fail to leverage AI due
to constraints on resources, skills, and capabilities will struggle
to meet sudden shifts in consumer demand and, as such, face a
lower likelihood of survival. For instance, companies that readily adopt cloud computing platforms like Amazon Web Services
(AWS) and Microsoft Azure can enhance their data storage,
processing, and computing efficiency, enabling seamless integration of AI technologies to adapt to evolving market conditions (Sultan 2013). Soto-Acosta et al. (2018) further highlight
that successful exploratory and exploitative innovation depends
not only on developing internal capabilities, such as information
technology and knowledge management, but also on the ability
to respond swiftly to external factors, including technological
advancements, shifting customer preferences, and fluctuations
in product demand. Additionally, Aljarboa (2024) has confirmed
the positive impact of dynamic capabilities on the adoption of
AI tools in e-commerce by SMEs. Based on these findings, the
following hypothesis is proposed:

H5. Dynamic Capabilities (DC) positively influence SMEs'
Artificial Intelligence Adoption Intensity (AIAI).
H6. Dynamic Capabilities (DC) positively influence SMEs'
Artificial Intelligence Acceptance Rate (AIAR).
2.3.7   |   Artificial Intelligence Adoption and Firms'
Performance
Technological progress has long been recognized as a significant driver of economic growth and social welfare.

firms that have more organic structures and in environments
with greater competitive intensity. This highlights the importance of aligning dynamic capabilities with external conditions
to secure better financial outcomes. Considering these findings,
the following hypothesis is proposed:

Building on these findings, it has been hypothesized that AI
adoption, as operationalized in this study through AIAI and
AIAR, positively impacts firms' performance across all identified dimensions (technological, economic, collaborative, and
sustainable).

H7. AIAI

positively
Performance (TP).

influences

SMEs'

Technological

H8. AIAI positively influences SMEs' Economic Performance

(EP).

H9. AIAI positively
Performance (CP).

influences

SMEs'

Collaborative

H10. AIAI

positively
Performance (SP).

influences

SMEs'

Sustainable

H11. AIAR

influences

SMEs'

Technological

positively
Performance (TP).

H12. AIAR positively influences SMEs' Economic Performance
(EP).

H13. AIAR positively
Performance (CP).

influences

SMEs'

Collaborative

H14. AIAR positively
Performance (SP).

influences

SMEs'

Sustainable

3   |   Methodology
3.1   |   Sample and Data Collection
This study examines startups operating in Italy using self-
reported surveys, a method widely used in research on SMEs.
Data was collected using a structured questionnaire that
was distributed to startups listed in the Business register of
Innovative Startups in Italy (https://​start​up.​regis​t roim​prese.​
it/​). Nine pilot tests were initially conducted to evaluate the
clarity, readability, and validity of the questionnaire, leading
to refinements in the grammar and improvements in the writing. The survey was then administered between November 15,
2024, and January 10, 2025, using multiple channels, including email, LinkedIn, and WhatsApp, in order to maximize
reach. To reduce social desirability bias, participants were
guaranteed anonymity. To mitigate common method bias
(CMB), a dedicated message was sent to participants explaining the academic purposes of the research, and survey items
were intermixed to vary their order. A total of 234 complete
questionnaires have been collected; however, 24 responses
were deemed ineligible due to missing values, ensuring that
only fully completed questionnaires were included in the final
dataset. The characteristics of the startups in the final sample
are presented in Table 1.

3.2   |   Measures
Survey participants first provided general information about
their startups, including demographic details. They were then
asked to rate their agreement with various survey items, using
a Likert scale ranging from 1 (strongly disagree) to 7 (strongly
agree). As the original scales were in English, a translation and
back-translation procedure was employed to ensure conceptual
accuracy and linguistic consistency in the Italian version. To
enhance its readability and clarity, the translated questionnaire
underwent pilot testing and refinement, as outlined in the previous section. The measurement items used in this study are based

Schumpeter's early writings highlight its critical role in shaping market dynamics and firm competitiveness. Solow's (1957)
identification of technological change as a key contributor
to economic performance further cemented its significance,
leading to extensive empirical research on how firms and
industries leverage innovation to sustain long-term growth
(Cohen 2010). Economists now widely acknowledge that a
firm's ability to advance technologically directly influences its
economic outcomes and market position. Given this, it's unsurprising that AI adoption is seen as playing a crucial role
in shaping economic performance, as firms can integrate AI
technologies to enhance their productivity, optimize resource
allocation, and gain an edge over competitors. Research has
backed this up, showing that AI helps businesses improve their
decision-making, reduce inventory costs through advanced logistics, enhance productivity, and boost their overall financial
performance (Chen et al. 2020; Dubey et al. 2020; Badghish
and Soomro 2024). Cannavale et al. (2022) show that AI-based
solutions also improve supply chain management by reducing
errors and providing buyers with direct access to supplier data,
allowing a vast range of organizations to improve their performance. Necula et al. (2024) also highlight the positive link
between AI and efficiency (i.e., productivity). Furthermore,
Nayal et al. (2021) find that AI adoption plays a crucial role in
improving supply chain risk mitigation performance. AI adoption also enhances a firm's dynamic marketing capabilities
and, as a result, its marketing performance (Chen et al. 2023).
Abrokwah-L arbi and Awuku-L arbi (2024) establishes the significance of AI adoption by SMEs in achieving financial performance, customer performance, internal business process
performance and learning and growth performance. SMEs are
at greater risk of failure when AI adoption is low, leading to
a decline in competitiveness, shrinking market share, and the
creation of fewer job opportunities (Baabdullah et al. 2021). Li
and Jin (2024) found specifically that AI adoption has a positive influence on the sustainability performance of corporations. This is partly driven by the fact that AI adoption allows
and encourages transformations within the organization that
result in more sustainable practices, reduced waste, and other
measures of performance. Similarly, Spagnuolo et al. (2025)
demonstrate a statistically significant association between AI
adoption and sustainable performance, with the greatest impact observed in environmental outcomes. Furthermore, Olan
et al. (2022), which apply a fuzzy set-theoretic approach, state
that the combination of AI and knowledge sharing provides a
more sustainable organizational performance strategy for business operations. Furthermore, AI adoption contributes to eco-
friendly innovation, helping SMEs minimize their emissions,
limit their environmental impact, and reducing cost (Badghish
and Soomro 2024). The positive impact of AI adoption on firms'
innovation capabilities is further supported by the findings of
Wael Al-K hatib (2023), Khan et al. (2024), and Xu et al. (2024).

Characteristics
Industry sector

Geographical location

Number of employees

Frequency (n)

Percentage (%)

Service activities and utilities

122

58%

Industry and Manufacturing

45

22%

ICT

21

10%

R&D

9

4%

Crafts

9

4%

Tourism

2

1%

Healthcare

2

1%

North

105

50%

Center

57

27%

South and Islands

48

23%

≤ 10

170

81%

11–20

23

11%

≥ 21

17

8%

on established research, with some items adapted to align with
the specific context of this study. A detailed list of the scale items
is provided in Table 2.

4   |   Results
4.1   |   Data Analysis
In this study, Partial Least Squares Structural Equation
Modeling (PLS-SEM) has been used to test and validate the
proposed research model and hypotheses. This statistical
method is particularly recommended for studies with small
sample sizes (Willaby et al. 2015) and exploratory research
(Hair et al. 2019). Furthermore, it is highly advised for datasets with a limited number of indicators per latent variable
(Hair Jr. et al. 2017). The SEMinR software package was used
to conduct the analysis. The sample size of 210 valid questionnaires meets the recommended guideline, which suggests
having at least 10 times the maximum number of arrowheads pointing at the latent variables in the model (Hair Jr
et al. 2021). The analysis began with an evaluation of the measurement model, followed by an assessment of the predictive
power of the structural model (Hair Jr. et al. 2016, 2017, 2021;
Ravand and Baghaei 2016).

4.2   |   Measurement Model
The evaluation of the measurement model began with an assessment of indicator reliability (Hair Jr et al. 2021). Among
the indicators, only the loadings of the TP2 and CP6 items
fall slightly below the recommended threshold of 0.708.
However, as these values remain above 0.6, they are still considered acceptable for exploratory studies (Hair et al. 2011;
Hair Jr et al. 2021). As the next step, the internal consistency
reliability has been assessed by evaluating the composite

reliability coefficient rhoC (Hair Jr. et al. 2017), Cronbach's
alpha (Hair Jr. et al. 2017), and the reliability coefficient
rhoA (Dijkstra 2014; Dijkstra and Henseler 2015). The results
shown in Table 3 demonstrate that all values fall within the
recommended thresholds, further confirming the validity and
reliability of the measurement model. The convergent validity
of the model was also assessed using the Average Variance
Extracted (AVE), with positive results presented in Table 3
(Hair et al. 2022). Finally, the evaluation of the measurement
model was completed by assessing its discriminant validity
(Hair Jr et al. 2021). This was done using the Fornell-L arcker
criterion (Fornell and Larcker 1981) and the Heterotrait-
Monotrait Ratio (HTMT) (Henseler et al. 2015). The results
of these analyses, which are also positive, are presented in
Tables 4 and 5, respectively.

4.3   |   Structural Model and Hypotheses Testing
The assessment of collinearity among constructs initiated the
evaluation of the structural model. The Variance Inflation
Factor (VIF) has been used to evaluate collinearity. As reported
in Table 6, none of the VIF values exceeded the threshold limit
of 5. This confirmed the absence of collinearity issues (Hair
et al. 2011; Kock and Lynn 2012).
The evaluation process moved forward with the assessment
of the significance and relevance of the structural model
relationships. In this regard, the PLS-
SEM algorithm was
launched, and the bootstrapping analysis was performed with
5000 sub-samples (Hair Jr. et al. 2017; Hair et al. 2019). The
analysis results, including beta values, sample mean, standard
deviation, T-values, confidence intervals, and p-values, are
presented in Table 7. Finally, the coefficient of determination
(R 2), which serves as a measure of the model's explanatory
power (Shmueli and Koppius 2011), has also been calculated.
For a more visual representation, Figure 2 illustrates the key

TABLE 1    |    Characteristics of the sample.

Variable

Items

Measurement items

Source

Sensing (SEN)

SEN1

Our company knows the best
practices in the market

Kump and Kessler (2019)

SEN2

Our company is up to date on the
current market situation

SEN3

Our company systematically searches for
information on the current market situation

SEN4

As a company, we know how to
access new information

SEN5

Our company always has an eye
on our competitors' activities

SEI1

Our company can quickly relate to
new knowledge from the outside

SEI2

We recognize what new information
can be utilized in our company

SEI3

Our company is capable of turning
new technological knowledge into
process and product innovation

SEI4

Current information leads to the
development of new products or services

TRA1

By defining clear responsibilities,
we successfully implement plans
for changes in our company

TRA2

Even when unforeseen interruptions
occur, change projects are seen through
consistently in our company

TRA3

Decisions on planned changes are
pursued consistently in our company

TRA4

In the past, we have demonstrated our
strengths in implementing changes

TRA5

In our company, change projects can be put
into practice alongside the daily business

AIAR1

My company is ready to adopt AI
technology to generate innovations

AIAR2

My company is willing to upgrade
their technology and ready to
include AI as part of it

AIAI1

We have implemented AI in all
our company processes

AIAI2

Relative to the potential of AI for
our company activities, our AI
implementation is extensive

AIAI3

AI has substantially changed
our business processes

Seizing (SEI)

Transforming (TRA)

AI Acceptance Rate (AIAR)

AI Adoption Intensity (AIAI)

Kump and Kessler (2019)

Kump and Kessler (2019)

Adapted from Almaiah et al. (2022)

Adapted from Chen and
Tajdini (2024)

(Continues)

TABLE 2    |    Variables and measures.

Variable

Items

Measurement items

Source

Technological performance
(TP)

TP1

Our company develops and introduces
new products to the market at a
fast pace compared to others in
the innovation ecosystem

Adapted from Hagedoorn and Cloodt
(2003), Chen and Chen (2006)

TP2

Our company frequently announces new
products or technological innovations to the
market within the innovation ecosystem

TP3

The products developed by our company
achieve strong sales performance
compared to our innovation ecosystem
standards and expectations

TP4

Our company invests significantly in
R&D and technological innovation
to maintain competitiveness within
the innovation ecosystem

TP5

Our company successfully completes
innovation projects that lead to new
products, processes, or services

EP1

Our company's profit increases every year

EP2

Our company's return on investment
(ROI) is improving every year

EP3

Our company's sales volume
increases every year

EP4

Our company increases shareholder value

EP5

Our company increases productivity

CP1

Our company often generate innovative
idea and/or solutions to problems by
collaborating with other IE members

CP2

Our company often search out new working
methods, techniques, or instruments by
collaborating with other IE members

CP3

Our company share resources to help IE
members (i.e., other companies, partners,
suppliers, customers, government,
etc.) improve their capabilities

CP4

IE members (i.e., other companies,
partners, suppliers, customers,
government, etc.) is closely monitored
and is the basis for future business

CP5

Value-added resources are shared among IE
members (i.e., other companies, partners,
suppliers, customers, government, etc.)

CP6

In general, our company has achieved
most of the goals in innovative ways by
collaborating with other IE members (i.e.,
other companies, partners, suppliers,
customers, government, etc.)

Economic performance (EP)

Collaborative performance
(CP)

Adapted from Vo Thai et al. (2024)

Adapted from Fawcett
et al. (2011), Liu et al. (2022)

(Continues)

TABLE 2    |    (Continued)

Variable

Items

Measurement items

Source

Sustainable performance (SP)

SP1

Our company has always attached
great importance to reducing
environmental pollution

Rauter et al. (2018), Shen et al. (2020)

SP2

Our company gives priority on
resource efficiency in production

SP3

Our company puts great emphasis
on social responsibility

SP4

Our company regards product
sustainability as its top priority

SP5

Our company is focused on building
a sustainable business model

findings, including R 2 , to highlight the main results of the
structural model analysis.
The analysis results confirm a positive impact of DC on TP, CP, and
SP, thereby supporting hypotheses H1, H3, and H4. Specifically,
the path coefficient of DC on TP (β = 0.47, p < 0.001) indicates a
strong and statistically significant positive effect. Similarly, DC exhibits a relevant positive impact on CP (β = 0.615, p < 0.001) and
SP (β = 0.662, p < 0.001). Conversely, hypothesis H2, which proposed a significant effect of DC on EP, was not supported, as the
confidence interval for this relationship includes zero (CI [−0.13,
0.281]), indicating that the effect is not statistically significant
(Hair Jr et al. 2021). Hypotheses H5 and H6 are supported by the
model, with DC having a stronger influence on AIAR (β = 0.523,
p < 0.001) compared to its effect on AIAI (β = 0.279, p < 0.001).
Additionally, AIAI positively influences TP (β = 0.390, p < 0.001),
EP (β = 0.498, p < 0.001), and CP (β = 0.288, p < 0.001), thereby confirming hypotheses H7, H8, and H9. Nonetheless, its positive effect on SP (H10) was not supported (β = −0.079, p = 0.059). Finally,
AIAR positively impacts TP and SP, confirming hypotheses H11
(β = 0.192, p = 0.001) and H14 (β = 0.213, p < 0.001). Meanwhile, its
influence on EP and CP was not statistically significant, leading
to the rejection of hypotheses H12 (β = 0.094, p = 0.010) and H13
(β = −0.108, p = 0.061).

5   |   Discussion
5.1   |   Dynamic Capabilities and Firms'
Performance
The first set of results confirms the positive impact of DC on
TP (H1), CP (H3), and SP (H4), while the hypothesized relationship between DC and EP (H2) is not supported. The confirmation of H1, H3, and H4 is consistent with prior research,
reinforcing the idea that firms with strong dynamic capabilities
are more equipped to improve technological (Deeds et al. 2000;
Kunanoppadol and Igel 2023), collaborative (Barreto 2010;
Haans et al. 2016), and sustainable (Russo 2003; Chakrabarty
and Wang 2012; Mousavi et al. 2018) performances. The positive
relationship between DC and TP suggests that firms with well-
developed dynamic capabilities are better positioned to sense,

seize, and reconfigure technological opportunities (Teece 2014).
The significant effect of DC on CP indicates that firms with
greater agility and adaptability are more capable of establishing
strategic partnerships and sharing knowledge with other stakeholders to drive innovation (Pique et al. 2018; Falcke et al. 2024).
The positive impact of DC on SP highlights the role of dynamic
capabilities in driving sustainability-oriented innovation with
a focus on limited resources optimization (Chang et al. 2018;
Chege and Wang 2020; Omri 2020). These findings underscore
the importance of dynamic capabilities as strategic levers for
managers, especially within the context of resource-constrained
and innovation-driven SMEs. By cultivating DCs, managers can
more effectively align their firms with fast-evolving technological and sustainability demands. This strategic alignment enhances operational adaptability and also strengthens the firm's
capacity to build collaborative ecosystems and embed long-
term sustainability into its innovation agenda. In early-stage
ventures, where formal structures and stable routines may be
lacking, DCs provide a critical foundation for shaping strategic
direction and ensuring resilience in uncertain and dynamic
markets.
Contrary to expectations, the results do not support a significant relationship between DC and EP in the sampled SMEs.
Although prior literature often highlights a positive association between DC and economic outcomes (Drnevich and
Kriauciunas 2011; Wang et al. 2015; Fainshmidt et al. 2017),
the findings of this research align with those studies that
point to a more complex or conditional relationship (Wilden
et al. 2013). This result may be influenced by the specific
nature of the surveyed SMEs, which are innovative startups
and thus represent early-stage firms. In this context, dynamic
capabilities are often directed toward experimentation, product development, and market entry rather than immediate financial returns. In fact, often economic performance in such
firms tends to lag behind strategic capability development,
and the prioritization of growth or technological advancement
over short-term profitability can limit the immediate financial
benefits of DCs. Additionally, in the Italian context, additional
systemic factors such as limited access to venture capital and
regulatory complexity may further constrain the financial returns associated with capability-d riven strategies.

TABLE 2    |    (Continued)

The second set of findings confirms the positive impact of DC
on both AIAI (H5) and AIAR (H6), with DC having a stronger
influence on AIAR. These results align with prior research
on the positive relationship between dynamic capabilities and
AI adoption (Aljarboa 2024; Arroyabe et al. 2024). In addition
TABLE 3    |    Internal consistency reliability and convergent validity.

Cronbach's alpha

rhoA

rhoC

AVE

DC

0.832

0.842

0.900

0.750

AIAI

0.840

0.857

0.905

0.762

AIAR

0.893

0.897

0.949

0.903

TP

0.812

0.829

0.879

0.650

EP

0.876

0.896

0.909

0.668

CP

0.837

0.847

0.879

0.550

SP

0.848

0.855

0.891

0.620

SEN

0.787

0.801

0.859

0.604

SEI

0.785

0.795

0.861

0.608

TRA

0.846

0.855

0.897

0.685

Note: DC is a second order of SEN, SEI and TRA.

to existing literature, this study contributes by examining the
relationships between DC and the two dimensions of AI adoption identified, AIAI and AIAR. The positive effects of DC on
both AIAI and AIAR highlight the role of dynamic capabilities in facilitating both the integration of AI technologies into
a firm's processes (AIAI) and the organization's openness and
readiness to adopt AI solutions (AIAR). These findings emphasize that SMEs with strong dynamic capabilities are more
likely to integrate AI into their core operations and demonstrate a higher degree of acceptance and willingness to embrace AI innovations at all levels. The stronger effect of DC on
AIAR compared to AIAI can be further explained in the context of startups, which are the focus of this survey. In early-
stage firms, dynamic capabilities are more likely to influence
organizational mindsets and readiness for change than to
immediately translate into large-scale, resource-intensive implementation efforts. Startups often operate with limited financial and technical resources, making full-scale adoption
of complex AI systems challenging, even when the organizational willingness and openness (i.e., high AIAR) are present.
In this context, DCs help cultivate a culture of innovation and
experimentation, encouraging teams to explore and accept AI
technologies conceptually. However, turning that acceptance
into intensive, operational use (AIAI) may require capabilities or infrastructure that early-stage firms have not yet developed. Thus, DCs are more immediately reflected in firms'
positive attitudes toward AI than in the extent of its concrete,
widespread application.

TABLE 4    |    Fornell-Larcker.

DC

AIAI

AIAR

TP

EP

CP

SP

DC

0.866

AIAI

0.502

0.873

AIAR

0.255

0.749

0.950

TP

0.657

0.713

0.618

0.806

EP

0.327

0.545

0.589

0.558

0.817

CP

0.624

0.384

0.387

0.644

0.303

0.742

SP

0.75

0.472

0.220

0.529

0.141

0.703

0.788

AIAR

TP

EP

CP

SP

TABLE 5    |    Heterotrait-Monotrait Ratio (HTMT).

DC

AIAI

DC
AIAI

0.593

AIAR

0.297

0.878

TP

0.797

0.852

0.724

EP

0.392

0.641

0.642

0.637

CP

0.709

0.434

0.440

0.767

0.365

SP

0.867

0.536

0.244

0.616

0.274

0.788

5.2   |   Dynamic Capabilities and Artificial
Intelligence Adoption

organizations. From a managerial perspective, these findings
highlight the strategic value of intensifying AI adoption as a
lever to enhance multiple dimensions of organizational performance. However, the lack of a significant effect of AIAI on SP
suggests that, in the specific context of startups, AI technologies
are often adopted with an experimental or developmental focus.
These early-stage SMEs tend to use AI primarily to explore technical capabilities or improve internal processes, rather than as a
direct means to achieve sustainability objectives. Consequently,
even when AI is implemented intensively, its impact on broader
sustainability outcomes may remain limited in the short term,
largely due to the firms' underdeveloped sustainability strategies
and constrained resources.

The third set of results confirms that AIAI positively influences
TP (H7), EP (H8), and CP (H9), but its impact on SP (H10) is not
supported. These findings mainly align with the existing literature, which has broadly examined AI adoption's positive effects
on firm performance, without differentiating between AIAI
and AIAR, across multiple dimensions (Chen et al. 2020; Dubey
et al. 2020; Cannavale et al. 2022; Badghish and Soomro 2024;
Li and Jin 2024).
AIAI positively impacts TP by enabling process automation
and data-driven decision-making, leading to overall efficiency
improvements. Its effect on EP suggests that AI integration
contributes to cost reductions and productivity improvements,
reinforcing financial performance. The positive impact on
CP highlights how AI adoption facilitates data sharing and
communication, improving collaboration within and across

The last set of results confirms that AIAR positively affects
TP (H11) and SP (H14) but does not show a significant impact
on EP (H12) and CP (H13). High levels of AIAR demonstrate
firms' willingness to explore AI solutions, promoting a culture
of continuous learning and innovation, which accelerates the
adoption of cutting-edge technologies, directly impacting TP.
The significant relationship between AIAR and SP highlights
the role of AI readiness in driving sustainability efforts, as firms
that actively explore AI technologies may be more inclined to
adopt AI-driven sustainability initiatives, such as resource optimization and environmental impact reduction. The absence
of a significant relationship between AIAR and EP can be explained by the unique characteristics and developmental stage
of the Italian innovative startups. While a high rate of acceptance among employees and managers may indicate openness
to technological change, it does not necessarily translate into
immediate economic gains. Specifically, in early-stage firms,
AIAR often reflects a willingness to experiment with or explore
new tools, but these tools may not yet be strategically embedded in revenue-generating activities or operational processes.

TABLE 6    |    VIF Values.

DC➔TP

AIAI➔TP

AIAR➔TP

1.399

2.976

2.381

DC➔EP

AIAI➔EP

AIAR➔EP

1.399

2.976

2.381

DC➔CP

AIAI➔CP

AIAR➔CP

1.399

2.976

2.381

DC➔SP

AIAI➔SP

AIAR➔SPE

1.399

2.976

2.381

TABLE 7    |    Significance and relevance of structural model relationships.

Path coefficient

β

Sample mean

SD

T_ stat.

2.50 CI

97.50 CI

Support

H1

DC➔TP

0.447***

0.445

0.069

6.487

0.315

0.577

Yes

H2

DC➔EP

0.138*

0.138

0.075

1.834

−0.013

0.281

No

H3

DC➔CP

0.615***

0.615

0.059

10.35

0.491

0.721

Yes

H4

DC➔SP

0.662***

0.664

0.041

16.19

0.577

0.737

Yes

H5

DC➔AIAI

0.279***

0.284

0.055

5.033

0.174

0.391

Yes

H6

DC➔AIAR

0.523***

0.528

0.061

8.550

0.398

0.637

Yes

H7

AIAI➔TP

0.390***

0.388

0.049

7.973

0.290

0.480

Yes

H8

AIAI➔EP

0.498**

0.502

0.080

6.218

0.339

0.652

Yes

H9

AIAI➔CP

0.268***

0.267

0.060

4.480

0.151

0.385

Yes

H10

AIAI➔SP

−0.079

−0.082

0.050

−1.570

−0.179

0.016

No

H11

AIAR➔TP

0.192**

0.196

0.063

3.056

0.080

0.325

Yes

H12

AIAR➔EP

0.094

0.092

0.074

1.264

−0.053

0.242

No

H13

AIAR➔CP

−0.108

−0.104

0.069

−1.550

−0.238

0.033

No

H14

AIAR➔SP

0.213***

0.212

0.059

3.601

0.098

0.330

Yes

**p < 0.05.
***p < 0.001.

5.3   |   Artificial Intelligence Adoption and Firms'
Performance

Startups frequently face challenges in converting technological potential into concrete financial outcomes, especially when
their business models are still evolving, and scalability is limited. In the startup context, where resources are scarce and financial sustainability is fragile, the gap between technological
acceptance and measurable economic return may be particularly wide. Therefore, although AIAR is a necessary enabler for
long-term impact, it may not be sufficient in itself to influence
short-term startups EP. On the other hand, the positive impact
of AIAI on EP (H8) suggests that, when startups go beyond
mere acceptance and engage in more intensive and purposeful
implementation of AI technologies, they are better positioned to
generate tangible financial benefits such as improved efficiency,
automation of routine tasks, enhanced decision-making, and
faster responsiveness to market demands. Finally, the lack of a
significant impact of AIAR on CP may stem from the fact that
collaborative performance is more strongly shaped by external
industry relationships than by internal openness to AI. While
a high AIAR indicates a firm's readiness to embrace new technologies, effective collaboration depends on the presence of elements that many early-stage startups have yet to build, such as
well-established partnerships and robust mechanisms for cross-
organizational knowledge exchange.
To conclude, it is important to highlight the differing effects of
AIAI and AIAR on SP and CP. To justify these apparently counterintuitive findings, the distinct nature of AIAI and AIAR and
their implications for startups must be considered. AIAI reflects
the extent to which AI is integrated within firms' processes,

meaning that firms with high AIAI have already incorporated
AI-driven tools and systems into their processes. This integration facilitates data sharing, real-
time communication, and
workflow automation, all of which enhance collaboration within
and beyond the organization. On the other hand, AIAR represents a firm's openness and readiness to adopt AI rather than
its actual implementation. While startups with high AIAR may
recognize the potential of AI for collaboration, the mere willingness to adopt AI does not immediately translate into effective
collaborative practices, which often require concrete AI-driven
systems that enhance connectivity, support knowledge-sharing,
all elements that are more closely tied to AIAI than to AIAR.
In addition, AIAR exhibits a significant impact on SP, whereas
AIAI does not. This may be due to the fact that AIAR captures
a firm's broader strategic intent and long-term vision regarding
AI adoption. Startups that demonstrate a high level of AI readiness are more likely to explore AI applications aimed at sustainability, such as resource optimization and carbon footprint and
energy reduction initiatives. These firms are forward-thinking
and more inclined to experiment with AI for long-term environmental and social impact. On the other hand, AIAI primarily
focuses on integrating AI into immediate business operations,
often prioritizing efficiency, automation, and profitability over
sustainability. Startups, which generally operate with constrained resources, may implement AI in ways that maximize
short-term gains rather than investing in sustainability-driven
AI applications that require longer-term commitment and additional financial resources.

FIGURE 2    |    Results of structural model assessment.

6.1   |   Theoretical Implications
From a theoretical perspective, this study contributes to the literature in several important ways.
First, it extends DC theory by offering a process-level explanation
of how firms translate sensing, seizing, and transforming capabilities into performance outcomes through AI adoption. Rather
than treating AI adoption as a single construct, this study introduces two distinct but complementary mediators: AIAI, which
reflects the extent of AI integration into business processes, and
AIAR, which represents organizational openness and readiness
for AI implementation. This dual-pathway operationalization
deepens the understanding of how dynamic capabilities manifest in the context of digital transformation, particularly within
start-up SMEs. Second, the study advances existing research
by linking these internal adoption mechanisms to four distinct
dimensions of firm sustainability: technological, economic, collaborative, and sustainable performance. While prior studies
often examine performance outcomes in isolated terms, such
as financial or innovation performance, this research offers a
more holistic view of how AI adoption contributes to a multidimensional sustainability agenda. This perspective provides new
insight into the trade-offs and synergies that SMEs encounter
when leveraging AI for long-term value creation. In doing so,
the study not only enhances the theoretical richness of the DC
framework but also contributes to the growing literature on AI-
enabled transformation in resource-
constrained, high-
agility
environments such as those faced by early-stage and innovative SMEs.

6.2   |   Practical Implications
This study provides several key practical implications for
startups, SMEs, and policymakers. First, SMEs that actively
sense market trends, seize AI opportunities, and reconfigure resources can more effectively implement AI solutions.
To support this, SMEs should focus on targeted capability-
building strategies. For example, AI training programs should
not only aim to improve general digital literacy but also be
tailored to different functional roles such as training operations teams in process automation tools, sales teams in AI-
enabled CRM systems, and leadership in strategic AI adoption
planning. Additionally, SMEs should foster cross-functional
collaboration by creating AI task forces that include both technical experts and domain specialists to align implementation
with business needs. Finally, adopting agile decision-making
frameworks such as iterative prototyping or lean experimentation can enable faster adaptation to evolving AI technologies
and market feedback.
Managers should view AIAI as a lever for short-to medium-
term operational and financial gains. Its positive effects on TP,
EP, and CP highlight the importance of concrete implementation. To improve AIAI, startups should prioritize high-impact,
scalable AI solutions tailored to their business models, such as
automating customer service with AI chatbots, streamlining

logistics with predictive analytics, or enhancing team collaboration with AI-
integrated platforms. Developing internal
roadmaps with clear metrics for success and involving multidisciplinary teams in the design and testing phases will enhance
implementation success. However, since AIAI does not impact
SP, SMEs should adopt a broader sustainability strategy beyond
AI. This might include forming partnerships with green-tech
firms and leveraging government sustainability programs to
gain access to expertise, funding, and AI solutions tailored for
environmental impact.
In contrast, AIAR reflects an organization's cultural and cognitive readiness to embrace AI, which is crucial for fostering
long-term transformation. Its positive influence on TP and SP
underscores the role of leadership commitment and organizational mindset in enabling change. To strengthen AIAR,
managers should invest in targeted training programs that
go beyond technical skills, focusing also on change management, ethical AI use, and cross-departmental collaboration.
Cultivating internal AI champions and integrating AI into the
company's vision can also build shared ownership and reduce
resistance.
The absence of AIAR's effect on EP and CP suggests that readiness without follow-through may not lead to tangible results.
Therefore, managers must ensure that a high level of acceptance
is matched by corresponding investments in AI infrastructure,
talent, and operational integration. Simply fostering enthusiasm
for AI is insufficient if not supported by resource allocation and
strategic alignment.
In this regard, policymakers should tailor AI adoption policies
to address SMEs' financial and resource constraints. This can be
achieved through financial incentives like grants and tax credits, subsidized AI consulting services, and regulatory support to
simplify AI integration while ensuring compliance.

7   |   Conclusions
This study explored how dynamic capabilities and AI-related
factors influence the performance of Italian innovative startups
across four key dimensions: technological, economic, collaborative, and sustainable. The findings confirm the significant
role of DCs in enhancing technological, collaborative, and sustainable performance, positioning them as strategic levers for
innovation-driven growth. However, the absence of a direct link
between DC and economic performance underscores the complexity of translating internal agility into immediate financial
gains, particularly for early-stage startups still navigating resource constraints and evolving business models.
AIAI emerged as a key driver of performance, particularly in
improving technological advancements, operational efficiency,
and collaboration. In contrast, AIAR showed a more selective
influence, contributing positively to technological and sustainable performance but not to economic or collaborative outcomes.
These results highlight the importance of complementing a positive attitude toward AI with tangible investments and operational integration to realize its full potential.

6   |   Theoretical and Practical Implications

Acknowledgements
The authors have nothing to report. Open access publishing facilitated
by Universita degli Studi di Torino, as part of the Wiley - CRUI-CARE
agreement.

References
Abrokwah-
Larbi, K., and Y. Awuku-
Larbi. 2024. “The Impact of
Artificial Intelligence in Marketing on the Performance of Business
Organizations: Evidence From SMEs in an Emerging Economy.”
Journal of Entrepreneurship in Emerging Economies 16, no. 4: 1090–
1117. https://​doi.​org/​10.​1108/​J EEE-​07-​2 022-​0207.
Aftab, J., N. Abid, H. Sarwar, A. Amin, M. Abedini, and M. Veneziani.
2024. “Does Corporate Social Responsibility Drive Financial
Performance? Exploring the Significance of Green Innovation, Green
Dynamic Capabilities, and Perceived Environmental Volatility.”
Corporate Social Responsibility and Environmental Management 31, no.
3: 1634–1653. https://​doi.​org/​10.​1002/​csr.​2654.
Agarwal, R., and W. Selen. 2009. “Dynamic Capability Building in
Service Value Networks for Achieving Service Innovation.” Decision
Sciences 40, no. 3: 431–475. https://​doi.​org/​10.​1111/j.​1540-​5915.​2 009.​
00236.​x.
Agarwal, R., and W. Selen. 2013. “The Incremental and Cumulative
Effects of Dynamic Capability Building on Service Innovation in

Collaborative Service Organizations.” Journal of Management &
Organization 19, no. 5: 521–543. https://​doi.​org/​10.​1017/​jmo.​2 014.​5.
Aljarboa, S. 2024. “Factors Influencing the Adoption of Artificial
Intelligence in e-Commerce by Small and Medium-Sized Enterprises.”
International Journal of Information Management Data Insights 4:
100285. https://​doi.​org/​10.​1016/j.​j jimei.​2 024.​100285.
Almaiah, M. A., R. Alfaisal, S. A. Salloum, et al. 2022. “Measuring
Institutions' Adoption of Artificial Intelligence Applications in Online
Learning Environments: Integrating the Innovation Diffusion Theory
With Technology Adoption Rate.” Electronics 11: 3291. https://​doi.​org/​
10.​3390/​elect​ronic​s1120​3291.
Andersson, S., G. Svensson, F.-J. Molina-Castillo, et al. 2022. “Sustainable
Development—Direct and Indirect Effects Between Economic, Social,
and Environmental Dimensions in Business Practices.” Corporate
Social Responsibility and Environmental Management 29, no. 5: 1158–
1172. https://​doi.​org/​10.​1002/​csr.​2261.
Arranz, C. F. A., M. F. Arroyabe, N. Arranz, and J. C. F. de Arroyabe.
2023. “Digitalisation Dynamics in SMEs: An Approach From Systems
Dynamics and Artificial Intelligence.” Technological Forecasting and
Social Change 196: 122880. https://​doi.​org/​10.​1016/j.​techf​ore.​2 023.​
122880.
Arroyabe, M. F., C. F. Arranz, I. F. De Arroyabe, and J. C. F. de Arroyabe.
2024. “Analyzing AI Adoption in European SMEs: A Study of Digital
Capabilities, Innovation, and External Environment.” Technology in
Society 79: 102733. https://​doi.​org/​10.​1016/j.​techs​oc.​2 024.​102733.
Baabdullah, A. M., A. A. Alalwan, E. L. Slade, R. Raman, and K. F.
Khatatneh. 2021. “SMEs and Artificial Intelligence (AI): Antecedents
and Consequences of AI-Based B2B Practices.” Industrial Marketing
Management 98: 255–270. https://​doi.​org/​10.​1016/j.​indma​rman.​2 021.​
09.​0 03.
Badghish, S., and Y. A. Soomro. 2024. “Artificial Intelligence Adoption
by SMEs to Achieve Sustainable Business Performance: Application of
Technology–Organization–Environment Framework.” Sustainability
16, no. 5: 1864. https://​doi.​org/​10.​3390/​su160​51864​.
Baía, E. P., and J. J. M. Ferreira. 2024. “Dynamic Capabilities and
Performance: How has the Relationship been Assessed?” Journal of
Management & Organization 30, no. 1: 188–217. https://​doi.​org/​10.​1017/​
jmo.​2 019.​88.
Barreto, I. 2010. “Dynamic Capabilities: A Review of Past Research and
an Agenda for the Future.” Journal of Management 36, no. 1: 256–280.
https://​doi.​org/​10.​1177/​01492​0 6309​350776.
Blonigen, B. A., and C. T. Taylor. 2000. “R&D Intensity and Acquisitions
in High-Technology Industries: Evidence From the US Electronic and
Electrical Equipment Industries.” Journal of Industrial Economics 48,
no. 1: 47–70. https://​doi.​org/​10.​1111/​1467-​6 451.​0 0112​.
Boons, F., and F. Lüdeke-Freund. 2013. “Business Models for Sustainable
Innovation: State-Of-T he-A rt and Steps Towards a Research Agenda.”
Journal of Cleaner Production 45: 9–19. https://​doi.​org/​10.​1016/j.​jclep​ro.​
2012.​07.​0 07.
Cannavale, C., A. Esempio Tammaro, D. Leone, and F. Schiavone.
2022. “Innovation Adoption in Inter-
Organizational Healthcare
Networks – The Role of Artificial Intelligence.” European Journal of
Innovation Management 25, no. 6: 758–774. https://​doi.​org/​10.​1108/​
EJIM-​08-​2 021-​0378.
Chakrabarty, S., and L. Wang. 2012. “The Long-Term Sustenance of
Sustainability Practices in MNCs: A Dynamic Capabilities Perspective
of the Role of R&D and Internationalization.” Journal of Business Ethics
110: 205–217. https://​doi.​org/​10.​1007/​s1055​1-​01214​22-​3.
Chang, R. D., J. Zuo, Z. Y. Zhao, et al. 2018. “Sustainability Attitude
and Performance of Construction Enterprises: A China Study.” Journal
of Cleaner Production 172: 1440–1451. https://​doi.​org/​10.​1016/j.​jclep​ro.​
2017.​10.​277.

Acknowledging the valuable contributions of this research
study, it is essential to recognize and address certain limitations.
The focus on Italian startups may limit the generalizability of
the findings to other cultural or organizational contexts. Future
research could extend the analysis in different countries or industries to validate these results. Furthermore, the study relies
on cross-sectional survey data, which captures relationships
at a single point in time but does not account for the dynamic
evolution of AI adoption and its long-term impact on firms' performances. A longitudinal study would provide a deeper understanding of how AI adoption and dynamic capabilities influence
firm performance over time. Additionally, the use of a questionnaire as a single data collection method may have limitations
in capturing the richness of the surveyed sample's experiences.
While survey-based research ensures statistical rigor, it may
not fully reflect organizational challenges or decision-making
rationales. Future studies could benefit from a mixed-methods
approach, incorporating qualitative methods such as interviews,
case studies, or focus groups to get a deeper understanding of
firms' AI adoption strategies and their contextual determinants.
Moreover, the study does not explore potential moderating factors that could influence the strength of the relationships identified, such as firm size and industry type. These factors may
shape how SMEs leverage AI, affecting their ability to translate
AI adoption into tangible business outcomes. Future research
could incorporate these moderating variables to refine the theoretical model and offer more tailored recommendations for
different types of SMEs. Finally, it is important to emphasize
that the findings of this study should be interpreted within the
specific context of the surveyed sample, early-stage innovative
startups. These firms, as a distinct subset of SMEs, are characterized by high uncertainty, limited resources, and a strong orientation toward innovation. Consequently, the results may not
be directly generalizable to the broader SME sector.

Chege, S. M., and D. Wang. 2020. “The Influence of Technology
Innovation on SME Performance Through Environmental Sustainability
Practices in Kenya.” Technology in Society 60: 101210. https://​doi.​org/​10.​
1016/j.​techs​oc.​2 019.​101210.
Chen, J., and S. Tajdini. 2024. “A Moderated Model of Artificial
Intelligence Adoption in Firms and Its Effects on Their Performance.”
Information Technology and Management. https://​doi.​org/​10.​1007/​
s1079​9 -​024-​0 0422​-​5.
Chen, J., and Y. F. Chen. 2006. “The Study of System on Technological
Innovation Performance in Enterprises.” Management Science, S&T 27:
86–91.
Chen, J., W. Zhou, and G. L. Frankwick. 2023. “Firm AI Adoption
Intensity and Marketing Performance.” Journal of Computer
Information Systems 65, no. 2: 172–189. https://​doi.​org/​10.​1080/​08874​
417.​2 023.​2277751.
Chen, T., W. Guo, X. Gao, and Z. Liang. 2020. “AI-Based Self-Service
Technology in Public Service Delivery: User Experience and Influencing
Factors.” Government Information Quarterly 101520: 101520. https://​
doi.​org/​10.​1016/j.​giq.​2 020.​101520.
Chien, S.-Y., and C.-H. Tsai. 2012. “Dynamic Capability, Knowledge,
Learning, and Firm Performance.” Journal of Organizational Change
Management 25, no. 3: 434–444. https://​doi.​org/​10.​1108/​0 9534​81121​
1228148.
Chmielewski, D. A., and A. Paladino. 2007. “Driving a Resource
Orientation: Reviewing the Role of Resource and Capability
Characteristics.” Management Decision 45, no. 3: 462–483. https://​doi.​
org/​10.​1108/​0 0251​74071​0745089.
Choi, S. B., Y. Feng, J. Liu, and Q. Zhu. 2019. “Motivating Corporate
Social Responsibility Practices Under Customer Pressure Among
Small-and Medium-Sized Suppliers in China: The Role of Dynamic
Capabilities.” Corporate Social Responsibility and Environmental
Management 26, no. 1: 213–226. https://​doi.​org/​10.​1002/​csr.​1673.
Cohen, W. M. 2010. “Fifty Years of Empirical Studies of Innovative
Activity and Performance.” In Handbook of the Economics of Innovation,
vol. 1, 129–213. North-Holland. https://​doi.​org/​10.​1016/​S 0169​-​7218(10)​
01004​-​X .
Cooper, R. G. 2025. “Smes' Use of AI for New Product Development:
Adoption Rates by Application and Readiness-To-Adopt.” Industrial
Marketing Management 126: 159–167. https://​doi.​org/​10.​1016/j.​indma​
rman.​2 025.​01.​016.
Corvello, V., A. Cimino, and A. M. Felicetti. 2023. “Building Start-Up
Acceleration Capability: A Dynamic Capability Framework for
Collaboration With Start-Ups.” Journal of Open Innovation: Technology,
Market, and Complexity 9: 100104. https://​doi.​org/​10.​1016/j.​joitmc.​
2023.​100104.
Dangelico, R. M., D. Pujari, and P. Pontrandolfo. 2017. “Green
Product Innovation in Manufacturing Firms: A Sustainability-
Oriented Dynamic Capability Perspective.” Business Strategy and the
Environment 26, no. 4: 490–506. https://​doi.​org/​10.​1002/​bse.​1932.
Davenport, T. H., and R. Ronanki. 2018. “Artificial Intelligence for the
Real World.” Harvard Business Review 96, no. 1: 108–116.
Deeds, D. L., D. DeCarolis, and J. Coombs. 2000. “Dynamic Capabilities
and New Product Development in High Technology Ventures: An
Empirical Analysis of New Biotechnology Firms.” Journal of Business
Venturing 15, no. 3: 211–229. https://​doi.​org/​10.​1016/​S 0883​-​9026(98)​
00013​-​5.

Dijkstra, T. K. 2014. “PLS' Janus Face–Response to Professor Rigdon's
‘Rethinking Partial Least Squares Modeling: In Praise of Simple
Methods’.” Long Range Planning 47, no. 3: 146–153. https://​doi.​org/​10.​
1016/j.​lrp.​2 014.​02.​0 04.
Dijkstra, T. K., and J. Henseler. 2015. “Consistent Partial Least Squares
Path Modeling.” MIS Quarterly 39, no. 2: 297–316.
Drnevich, P. L., and A. P. Kriauciunas. 2011. “Clarifying the Conditions
and Limits of the Contributions of Ordinary and Dynamic Capabilities
to Relative Firm Performance.” Strategic Management Journal 32: 254.
Duan, Y., J. S. Edwards, and Y. K. Dwivedi. 2019. “Artificial Intelligence
for Decision Making in the Era of Big Data–Evolution, Challenges and
Research Agenda.” International Journal of Information Management
48: 63–71. https://​doi.​org/​10.​1016/j.​ijinf​omgt.​2 019.​01.​021.
Dubey, R., A. Gunasekaran, S. J. Childe, et al. 2020. “Big Data Analytics
and Artificial Intelligence Pathway to Operational Performance
Under the Effects of Entrepreneurial Orientation and Environmental
Dynamism: A Study of Manufacturing Organisations.” International
Journal of Production Economics 226: 107599. https://​doi.​org/​10.​1016/j.​
ijpe.​2 019.​107599.
Edquist, C. 2005. “Systems of Innovation: Perspectives and Challenges.”
In The Oxford Handbook of Innovation, edited by J. Fagerberg, D. C.
Mowery, and R. R. Nelson, 181–208. Oxford University Press.
Eikelenboom, M., and G. de Jong. 2019. “The Impact of Dynamic
Capabilities on the Sustainability Performance of SMEs.” Journal of
Cleaner Production 235: 1360–1370. https://​doi.​org/​10.​1016/j.​jclep​ro.​
2019.​07.​013.
Eslami, M. H., H. Jafari, L. Achtenhagen, J. Carlbäck, and A. Wong.
2024. “Financial Performance and Supply Chain Dynamic Capabilities:
The Moderating Role of Industry 4.0 Technologies.” International
Journal of Production Research 62, no. 22: 8092–8109. https://​doi.​org/​
10.​1080/​0 0207​5 43.​2 021.​1966850.
Fagerberg, J. 2005. Innovation: A Guide to the Literature, edited by J.
Fagerberg, D. C. Mowery, and R. R. Nels. Oxford University Press.
Fainshmidt, S., A. Nairb, and M. R. Mallon. 2017. “MNE Performance
During a Crisis: An Evolutionary Perspective on the Role of Dynamic
Managerial Capabilities and Industry Context.” International Business
Review 26: 1088–1099. https://​doi.​org/​10.​1016/j.​ibusr​ev.​2 017.​0 4.​0 02.
Falasca, M., J. Zhang, M. Conchar, and L. Li. 2017. “The Impact
of Customer Knowledge and Marketing Dynamic Capability on
Innovation Performance: An Empirical Analysis.” Journal of Business
and Industrial Marketing 32, no. 7: 901–912. https://​doi.​org/​10.​1108/​
JBIM-​12-​2 016-​0289.
Falcke, L., A. K. Zobel, and S. D. Comello. 2024. “How Firms Realign
to Tackle the Grand Challenge of Climate Change: An Innovation
Ecosystems Perspective.” Journal of Product Innovation Management
41, no. 2: 403–427. https://​doi.​org/​10.​1111/​jpim.​12687​.
Fang, E. E., and S. Zou. 2009. “Antecedents and Consequences of
Marketing Dynamic Capabilities in International Joint Ventures.”
Journal of International Business Studies 40, no. 5: 742–761. https://​doi.​
org/​10.​1057/​jibs.​2 008.​96.
Fawcett, S. E., C. Wallin, C. Allred, A. M. Fawcett, and G. M. Magnan.
2011. “Information Technology as an Enabler of Supply Chain
Collaboration: A Dynamic-Capabilities Perspective.” Journal of Supply
Chain Management 47, no. 1: 38–59. https://​doi.​org/​10.​1111/j.​1745-​
493X.​2 010.​03213.​x.
Fornell, C., and D. F. Larcker. 1981. “Evaluating Structural Equation
Models With Unobservable Variables and Measurement Error.” Journal
of Marketing Research 18, no. 1: 39–50. https://​doi.​org/​10.​1177/​0 0222​
43781​01800104.
Griffith, D. A., S. M. Noble, and Q. Chen. 2006. “The Performance
Implications of Entrepreneurial Proclivity: A Dynamic Capabilties

Chatterjee, S., R. Chaudhuri, D. Vrontis, and G. Basile. 2022. “Digital
Transformation and Entrepreneurship Process in SMEs of India: A
Moderating Role of Adoption of AI-
CRM Capability and Strategic
Planning.” Journal of Strategy and Management 15, no. 3: 416–433.
https://​doi.​org/​10.​1108/​JSMA-​02-​2 021-​0 049.

Haans, R. F., C. Pieters, and Z. L. He. 2016. “Thinking About U:
Theorizing and Testing U-
and Inverted U-
Shaped Relationships in
Strategy Research.” Strategic Management Journal 37, no. 7: 1177–1195.
https://​doi.​org/​10.​1002/​smj.​2399.
Hagedoorn, J., and M. Cloodt. 2003. “Measuring Innovative
Performance: Is there an Advantage in Using Multiple Indicators?”
Research Policy 32, no. 8: 1365–1379. https://​doi.​org/​10.​1016/​s 0048​-​
7333(02)​0 0137​-​3.
Hair, F., J. J. Risher, M. Sarstedt, and C. M. Ringle. 2019. “When to Use
and How to Report the Results of PLS-SEM.” European Business Review
31, no. 1: 2–24. https://​doi.​org/​10.​1108/​EBR-​11-​2 018-​0203.
Hair, J. F., C. M. Ringle, and M. Sarstedt. 2011. “PLS-SEM: Indeed a
Silver Bullet.” Journal of Marketing Theory and Practice 19: 139–151.
https://​doi.​org/​10.​2753/​M TP10​69-​66791​9 0202​.
Hair, J. F., Jr., G. T. M. Hult, C. M. Ringle, et al. 2021. Partial Least
Squares Structural Equation Modeling (PLS-SEM) Using R. Springer
publications. https://​doi.​org/​10.​1007/​978-​3 -​030-​80519​-​7.
Hair, J. F., Jr., G. T. M. Hult, C. Ringle, and M. Sarstedt. 2016. A Primer
on Partial Least Squares Structural Equation Modeling (PLS-
SEM).
Sage-P ublications.
Hair, J. F., T. Hult, C. M. Ringle, and M. Sarstedt. 2022. A Primer on
Partial Least Squares Structural Equation Modeling (PLS-SEM). SAGE
Publications.
Hair, J. M., Jr., M. Sarstedt, C. M. Ringle, and S. P. Gudergan. 2017.
Advanced Issues in Partial Least Squares Structural Equation Modeling.
Sage-publications.
Henseler, J., C. M. Ringle, and M. Sarstedt. 2015. “A New Criterion for
Assessing Discriminant Validity in Variance-Based Structural Equation
Modeling.” Journal of the Academy of Marketing Science 43, no. 1: 115–
135. https://​doi.​org/​10.​1007/​s1174​7-​014-​0 403-​8.
Hernández-Linares, R., F. W. Kellermanns, and M. C. López-Fernández.
2020. “Dynamic Capabilities and SME Performance: The Moderating
Effect of Market Orientation.” Journal of Small Business Management
59, no. 1: 162–195. https://​doi.​org/​10.​1111/​jsbm.​12474​.
Hoai, T. T., N. N. Minh, H. V. Van, and N. P. Nguyen. 2023. “Accounting
Going Green: The Move Toward Environmental Sustainability in
Vietnamese Manufacturing Firms.” Corporate Social Responsibility and
Environmental Management 30, no. 4: 1928–1941. https://​doi.​org/​10.​
1002/​csr.​2 464.

Khan, O., T. Daddi, and F. Iraldo. 2020. “The Role of Dynamic
Capabilities in Circular Economy Implementation and Performance
of Companies.” Corporate Social Responsibility and Environmental
Management 27, no. 6: 3018–3033. https://​doi.​org/​10.​1002/​csr.​2 020.
Khan, S., S. Mehmood, and S. U. Khan. 2024. “Navigating Innovation
in the Age of AI: How Generative AI and Innovation Influence
Organizational Performance in the Manufacturing Sector.” Journal of
Manufacturing Technology Management 36, no. 3: 597–620. https://​doi.​
org/​10.​1108/​J MTM-​0 6-​2 024-​0302.
Khattab, S. A. 2017. “The Impact of Dynamic Capability on Innovation
(An Applied Study on Jordanian Pharmaceutical Organizations).”
European Journal of Management and Business Economics 9, no. 20:
73–85.
Kimani, D., K. Adams, R. Attah-Boakye, S. Ullah, J. Frecknall-Hughes,
and J. Kim. 2020. “Blockchain, Business and the Fourth Industrial
Revolution: Whence, Whither, Wherefore and How?” Technological
Forecasting and Social Change 161: 120254. https://​doi.​org/​10.​1016/j.​
techf​ore.​2 020.​120254.
Kock, N., and G. Lynn. 2012. “Lateral Collinearity and Misleading
Results in Variance-Based SEM: An Illustration and Recommendations.”
Journal of the Association for Information Systems 13, no. 7: 546–580.
https://​doi.​org/​10.​17705/​​1jais.​0 0302​.
Kump, B., and A. Kessler. 2019. “Toward a Dynamic Capabilities
Scale: Measuring Organizational Sensing, Seizing, and Transforming
Capacities.” Industrial and Corporate Change 28, no. 5: 1149–1172.
https://​doi.​org/​10.​1093/​icc/​dty054.
Kunanoppadol, J., and B. Igel. 2023. “Dynamic Capabilities in New
Product Development–the Role of Operational Capabilities.” Journal of
Strategy and Management 16, no. 3: 592–608. https://​doi.​org/​10.​1108/​
JSMA-​10-​2 022-​0187.
Laaksonen, O., and M. Peltoniemi. 2018. “The Essence of Dynamic
Capabilities and Their Measurement.” International Journal of
Management Reviews 20, no. 2: 184–205. https://​doi.​org/​10.​1111/​ijmr.​
12122​.
Lee, Y., I. Cho, and H. Park. 2015. “The Effect of Collaboration Quality on
Collaboration Performance: Empirical Evidence From Manufacturing
SMEs in the Republic of Korea.” Total Quality Management & Business
Excellence 26, no. 9–10: 986–1001. https://​doi.​org/​10.​1080/​14783​363.​
2015.​1050169.
Li, B. H., B. C. Hou, W. T. Yu, X. B. Lu, and C. W. Yang. 2017.
“Applications of Artificial Intelligence in Intelligent Manufacturing: A
Review.” Frontiers of Information Technology & Electronic Engineering
18, no. 1: 86–96. https://​doi.​org/​10.​1631/​F ITEE.​1601885.

Hsu, L. C., and C. H. Wang. 2012. “Clarifying the Effect of Intellectual
Capital on Performance: The Mediating Role of Dynamic Capability.”
British Journal of Management 23, no. 2: 179–205. https://​doi.​org/​10.​
1111/j.​1467-​8551.​2 010.​0 0718.​x.

Li, J., and X. Jin. 2024. “The Impact of Artificial Intelligence Adoption
Intensity on Corporate Sustainability Performance: The Moderated
Mediation Effect of Organizational Change.” Sustainability 16, no. 21:
9350. https://​doi.​org/​10.​3390/​su162​19350​.

Hurmelinna, P., K. Blomqvist, K. Puumalainen, and S. Saarenketo.
2005. “Striving Towards R&D Collaboration Performance: The Effect
of Asymmetry, Trust and Contracting.” Creativity and Innovation
Management 14, no. 4: 374–383. https://​doi.​org/​10.​1111/j.​1467-​8691.​
2005.​0 0357.​x.

Liu, T., Y. Mao, and S. Lu. 2022. “Fostering Participants' Collaborative
Innovation Performance in Megaprojects: The Effects of Perceived
Partners' Non-Mediated Power.” Journal of Construction Engineering
and Management 149, no. 1: 04022141. https://​doi.​org/​10.​1061/​(ASCE)​
CO.​1943-​7862.​0 002417.

Islam, M. T., M. M. Hasan, M. Redwanuzzaman, and M. K. Hossain.
2024. “Practices of Artificial Intelligence to Improve the Business in
Bangladesh.” Social Sciences & Humanities Open 9: 100766. https://​doi.​
org/​10.​1016/j.​ssaho.​2 023.​100766.

Lu, X., K. Wijayaratna, Y. Huang, and A. Qiu. 2022. “AI-
Enabled
Opportunities and Transformation Challenges for SMEs in the Post-
Pandemic Era: A Review and Research Agenda.” Frontiers in Public
Health 10: 885067. https://​doi.​org/​10.​3389/​f pubh.​2 022.​885067.

Kant, D., and A. Johannsen. 2022. “Evaluation of AI-Based Use Cases
for Enhancing the Cyber Security Defense of Small and Medium-
Sized Companies (SMEs).” In Proc. IS&T International Symposium
on Electronic Imaging: Mobile Devices and Multimedia: Enabling
Technologies, Algorithms, and Applications, 387-1–387-8. Society for
Imaging Science and Technology. https://​doi.​org/​10.​2352/​EI.​2 022.​3 4.3.​
MOBMU​-​387.

McKinsey. 2018. AI Adoption Advances, but Foundational Barriers
Remain. McKinsey Global Survey.

Mousavi, S., B. Bossink, and M. van Vliet. 2018. “Dynamic Capabilities
and Organizational Routines for Managing Innovation Towards
Sustainability.” Journal of Cleaner Production 203: 224–239. https://​doi.​
org/​10.​1016/j.​jclep​ro.​2 018.​08.​215.

Approach.” Journal of Retailing 82, no. 1: 51–62. https://​doi.​org/​10.​
1016/j.​jretai.​2 005.​11.​0 07.

Roundy, P. T., M. Bradshaw, and M. K. Brockman. 2018. “The
Emergence of Entrepreneurial Ecosystems: A Complex Adaptive
Systems Approach.” Journal of Business Research 86: 1–10. https://​doi.​
org/​10.​1016/j.​jbusr​es.​2 018.​01.​032.

Nayal, K., R. Raut, P. Priyadarshinee, B. E. Narkhede, Y. Kazancoglu,
and V. Narwane. 2021. “Exploring the Role of Artificial Intelligence
in Managing Agricultural Supply Chain Risk to Counter the
Impacts of the COVID-
19 Pandemic.” International Journal of
Logistics Management 33, no. 3: 744–772. https://​doi.​org/​10.​1108/​
IJLM-​12-​2 020-​0 493.

Russo, M. V. 2003. “The Emergence of Sustainable Industries: Building
Natural Capital.” Strategic Management Journal 24, no. 4: 317–331.
https://​doi.​org/​10.​1002/​smj.​298.

Necula, S. C., D. Fotache, and E. Rieder. 2024. “Assessing the Impact of
Artificial Intelligence Tools on Employee Productivity: Insights From a
Comprehensive Survey Analysis.” Electronics 13, no. 18: 3758. https://​
doi.​org/​10.​3390/​elect​ronic​s1318​3758.
OECD/Eurostat. 2018. Oslo Manual 2018: Guidelines for Collecting,
Reporting and Using Data on Innovation, 4th Edition, the Measurement
of Scientific. Technological and Innovation Activities. OECD Publishing.
https://​doi.​org/​10.​1787/​97892​6 4304​6 04-​en.
Olan, F., E. O. Arakpogun, J. Suklan, F. Nakpodia, N. Damij, and U.
Jayawickrama. 2022. “Artificial Intelligence and Knowledge Sharing:
Contributing Factors to Organizational Performance.” Journal of
Business Research 145: 605–615. https://​doi.​org/​10.​1016/j.​jbusr​es.​2 022.​
03.​0 08.
Omri, A. 2020. “Technological Innovation and Sustainable
Development: Does the Stage of Development Matter?” Environmental
Impact Assessment Review 83: 106398. https://​doi.​org/​10.​1016/j.​eiar.​
2020.​106398.
Piening, E. P., and T. O. Salge. 2015. “Understanding the Antecedents,
Contingencies, and Performance Implications of Process Innovation:
A Dynamic Capabilities Perspective.” Journal of Product Innovation
Management 32, no. 1: 80–97. https://​doi.​org/​10.​1111/​jpim.​12225​.
Pique, J. M., J. Berbegal-Mirabent, and H. Etzkowitz. 2018. “Triple Helix
and the Evolution of Ecosystems of Innovation: The Case of Silicon
Valley.” Triple Helix 5: 11. https://​doi.​org/​10.​1186/​s 4060​4 -​018-​0 060-​x.
Pundziene, A., S. Nikou, and H. Bouwman. 2022. “The Nexus
Between Dynamic Capabilities and Competitive Firm Performance:
The Mediating Role of Open Innovation.” European Journal of
Innovation Management 25, no. 6: 152–177. https://​doi.​org/​10.​1108/​
EJIM-​0 9-​2 020-​0356.
Qiu, L., X. Jie, Y. Wang, and M. Zhao. 2020. “Green Product Innovation,
Green Dynamic Capability, and Competitive Advantage: Evidence From
Chinese Manufacturing Enterprises.” Corporate Social Responsibility
and Environmental Management 27, no. 1: 146–165. https://​doi.​org/​10.​
1002/​csr.​1780.
Rahman, M., D. Hack-Polay, S. Shafique, and P. A. Igwe. 2023. “Dynamic
Capability of the Firm: Analysis of the Impact of Internationalisation on
SME Performance in an Emerging Economy.” International Journal of
Emerging Markets 18, no. 9: 2383–2401. https://​doi.​org/​10.​1108/​I JOEM​
- ​02-​2 021- ​0236.
Rauter, R., D. Globocnik, E. Perl-Vorbach, and R. J. Baumgartner. 2018.
“Open Innovation and Its Effects on Economic and Sustainability
Innovation Performance.” Journal of Innovation & Knowledge 4: 226–
233. https://​doi.​org/​10.​1016/j.​jik.​2 018.​03.​0 04.
Ravand, H., and P. Baghaei. 2016. “Partial Least Squares Structural
Equation Modeling With R.” Practical Assessment, Research &
Evaluation 21, no. 11: 1–16.
Rawashdeh, A., M. Bakhit, and L. Abaalkhail. 2023. “Determinants
of Artificial Intelligence Adoption in SMEs: The Mediating Role of
Accounting Automation.” International Journal of Data and Network
Science 7, no. 1: 25–34.
Ringov, D. 2017. “Dynamic Capabilities and Firm Performance.” Long
Range Planning 50, no. 5: 653–664. https://​doi.​org/​10.​1016/j.​lrp.​2 017.​
02.​0 05.

Santos, D. 2022. “Building Entrepreneurial Ecosystems: The Case of
Coimbra.” Journal of Science and Technology Policy Management 13, no.
1: 73–89. https://​doi.​org/​10.​1108/​JSTPM​- ​02-​2 020- ​0 028.
Shen, J., Z. Sha, and Y. J. Wu. 2020. “Enterprise Adaptive Marketing
Capabilities and Sustainable Innovation Performance: An Opportunity-
Resource Integration Perspective.” Sustainability 12: 469. https://​doi.​
org/​10.​3390/​su120​2 0469​.
Shmueli, G., and O. R. Koppius. 2011. “Predictive Analytics in
Information Systems Research.” MIS Quarterly 35, no. 3: 553–572.
https://​doi.​org/​10.​2139/​ssrn.​1606674.
Sjödin, D., V. Parida, and M. Kohtamäki. 2023. “Artificial Intelligence
Enabling Circular Business Model Innovation in Digital Servitization:
Conceptualizing Dynamic Capabilities, AI Capacities, Business Models
and Effects.” Technological Forecasting and Social Change 197: 122903.
https://​doi.​org/​10.​1016/j.​techf​ore.​2 023.​122903.
Solow, R. 1957. “Technical Change and the Aggregate Production
Function.” Review of Economics and Statistics 39, no. 3: 312–320.
Soto-Acosta, P., S. Popa, and I. Martinez-Conesa. 2018. “Information
Technology, Knowledge Management and Environmental Dynamism
as Drivers of Innovation Ambidexterity: A Study in SMEs.” Journal of
Knowledge Management 22, no. 4: 824–849. https://​doi.​org/​10.​1108/​
JKM-​10-​2 017-​0 448.
Spagnuolo, F., R. Casciello, I. Martino, and F. Meucci. 2025. “Exploring
the Impact of Artificial Intelligence on the Pursuit of SDGs: Evidence
From European State-
O wned Enterprises.” Corporate Social
Responsibility and Environmental Management 32, no. 2: 1987–2001.
https://​doi.​org/​10.​1002/​csr.​3047.
Sultan, N. 2013. “Cloud Computing: A Democratizing Force?”
International Journal of Information Management 33, no. 5: 810–815.
https://​doi.​org/​10.​1016/j.​ijinf​omgt.​2 013.​05.​010.
Taneja, A., V. Goyal, and K. Malik. 2023. “Sustainability-
Oriented
Innovations – Enhancing Factors and Consequences.” Corporate Social
Responsibility and Environmental Management 30, no. 6: 2747–2765.
https://​doi.​org/​10.​1002/​csr.​2513.
Teece, D. J. 2007. “Explicating Dynamic Capabilities: The Nature and
Microfoundations of (Sustainable) Enterprise Performance.” Strategic
Management Journal 28, no. 13: 1319–1350. https://​doi.​org/​10.​1002/​
smj.​6 40.
Teece, D. J. 2014. “The Foundations of Enterprise Performance:
Dynamic and Ordinary Capabilities in an (Economic) Theory of Firms.”
Academy of Management Perspectives 28, no. 4: 328–352. https://​doi.​org/​
10.​5 465/​amp.​2 013.​0116.
Teece, D. J., G. Pisano, and A. Shuen. 1997. “Dynamic Capabilities
and Strategic Management.” Strategic Management Journal 18, no. 7:
509–533. https://​doi.​org/​10.​1002/​(SICI)​1097-​0266(199708)​18:7%​3C509::​
AID-​SMJ882%​3E3.0.​CO;​2-​Z .
Thomas, A. 2024. “Digitally Transforming the Organization Through
Knowledge Management: A Socio-Technical System (STS) Perspective.”
European Journal of Innovation Management 27, no. 9: 437–460. https://​
doi.​org/​10.​1108/​E JIM-​02-​2 024-​0114.
Thormundsoon, B. 2024. “AI Corporate Investment Worldwide 2015–
2022.” Accessed 16 February 2025. https://​w ww.​stati​sta.​com/​stati​stics/​​
941137/​ai-​inves​tment​-​and-​f undi​ng-​world​w ide/​.
Tutore, I., A. Parmentola, M. C. Fiore, and F. Calza. 2024. “A Conceptual
Model of Artificial Intelligence Effects on Circular Economy Actions.”

Mugisha, J., A. F. Adyanga, and J. Ocan. 2025. “The Role of Artificial
Intelligence (AI) in Transforming Small and Medium Enterprises
(SMEs): A Narrative Review.” Applied Data Science and Analysis 2025:
112–117. https://​doi.​org/​10.​58496/​​A DSA/​2 025/​0 07.

Vanpoucke, E., A. Vereecke, and M. Wetzels. 2014. “Developing Supplier
Integration Capabilities for Sustainable Competitive Advantage: A
Dynamic Capabilities Approach.” Journal of Operations Management
32: 446–461. https://​doi.​org/​10.​1016/j.​jom.​2 014.​0 9.​0 04.
Vo Thai, H. C., T.-H. Hong-Hue, and M.-L . Tran. 2024. “Dynamic
Capabilities and Digitalization as Antecedents of Innovation and
Sustainable Performance: Empirical Evidence From Vietnamese
SMEs.” Journal of Asia Business Studies 18, no. 2: 385–411. https://​doi.​
org/​10.​1108/​JABS-​08-​2 023-​0325.
Wael AL-k hatib, A. 2023. “Drivers of Generative Artificial Intelligence
to Fostering Exploitative and Exploratory Innovation: A Toe
Framework.” Technology in Society 75: 1–12. https://​doi.​org/​10.​1016/j.​
techs​oc.​2 023.​102403.
Wamba, S. F., M. M. Queiroz, and L. Trinchera. 2024. “The Role of
Artificial Intelligence-Enabled Dynamic Capability on Environmental
Performance: The Mediation Effect of a Data-Driven Culture in France
and the USA.” International Journal of Production Economics 268:
109131. https://​doi.​org/​10.​1016/j.​ijpe.​2 023.​109131.
Wang, C. L., C. Senaratne, and M. Rafiq. 2015. “Success Traps, Dynamic
Capabilities and Firm Performance.” British Journal of Management 26:
26–44. https://​doi.​org/​10.​1111/​1467-​8551.​12066​.
Wei, R., and C. Pardo. 2022. “Artificial Intelligence and SMEs: How
Can B2B SMEs Leverage AI Platforms to Integrate AI Technologies?”
Industrial Marketing Management 107: 466–483. https://​doi.​org/​10.​
1016/j.​indma​rman.​2 022.​10.​0 08.
Wilden, R., S. P. Gudergan, B. B. Nielsen, and I. Lings. 2013. “Dynamic
Capabilities and Performance: Strategy, Structure and Environment.”
Long Range Planning 46: 72–96. https://​doi.​org/​10.​1016/j.​lrp.​2 012.​
12.​0 01.
Willaby, H. W., D. S. J. Costa, B. D. Burns, C. MacCann, and R. D.
Roberts. 2015. “Testing Complex Models With Small Sample Sizes: A
Historical Overview and Empirical Demonstration of What Partial
Least Squares (PLS) can Offer Differential Psychology.” Personality and
Individual Differences 84: 73–78. https://​doi.​org/​10.​1016/j.​paid.​2 014.​
09.​0 08.
Wu, L. Y. 2010. “Applicability of the Resource-Based and Dynamic-
Capability Views Under Environmental Volatility.” Journal of Business
Research 63, no. 1: 27–31. https://​doi.​org/​10.​1016/j.​jbusr​es.​2 009.​01.​0 07.
Xu, H., R. Xu, H. Lin, and X. He. 2024. “The Impact of Generative
Artificial Intelligence on Organizational Innovation Performance:
Roles of AI Generated Content Quality, AI Experience, and AI Usage
Environment.” In Proc, 1802–1807. ICETSIS.
Yang, J., Y. Blount, and A. Amrollahi. 2024. “Artificial Intelligence
Adoption in a Professional Service Industry: A Multiple Case Study.”
Technological Forecasting and Social Change 201: 123251. https://​doi.​
org/​10.​1016/j.​techf​ore.​2 024.​123251.
Zahra, S. A. 1993. “Environment, Corporate Entrepreneurship, and
Financial Performance: A Taxonomic Approach.” Journal of Business
Venturing 8: 319. https://​doi.​org/​10.​1016/​0883-​9 026(93)​9 0003​-​N.
Zahra, S. A., H. J. Sapienza, and P. Davidsson. 2006. “Entrepreneurship
and Dynamic Capabilities: A Review, Model and Research Agenda.”
Journal of Management Studies 43, no. 4: 917–955. https://​doi.​org/​10.​
1111/j.​1467-​6 486.​2 006.​0 0616.​x.
Zhao, S., Z. Wang, and V. E. Arkorful. 2025. “Political Network
Embeddedness and Ecological Innovation: Do Absorptive Capacity
and Dynamic Capability Have any Influence?” Corporate Social
Responsibility and Environmental Management 32, no. 2: 2085–2103.
https://​doi.​org/​10.​1002/​csr.​3048.

Corporate Social Responsibility and Environmental Management 31, no.
5: 4772–4782. https://​doi.​org/​10.​1002/​csr.​2827.

