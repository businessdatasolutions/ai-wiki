# The role of the level of artificial intelligence adoption on business model innovation, sustainable competitive advantage, and firm performance: Integrating the TOE framework and Dynamic Capabilities theory

**Authors:** Nguyen Thi Phuong Anh, Bui Huy Khoi, Nguyen Quang Thu, Tran Nha Ghi (corresponding)
**Affiliations:** Faculty of Business Administration, Industrial University of Ho Chi Minh City (Anh, Khoi, Ghi); School of Management, University of Economics Ho Chi Minh City (Thu)
**Journal:** Green Technologies and Sustainability 4 (2026), article 100384 (KeAi / Elsevier)
**DOI:** 10.1016/j.grets.2026.100384
**URL:** https://doi.org/10.1016/j.grets.2026.100384
**Received / Revised / Accepted:** 14 October 2025 / 23 March 2026 / 23 March 2026
**Published online:** 2026-03-28 (first page, "Available online"; Crossref carries no `published-online`, print issue 2026-07)
**Licence:** CC BY 4.0 (open access)
**Captured:** 2026-09-21 (user-supplied PDF from ScienceDirect, `1-s2.0-S2949736126000503-main.pdf`)
**fulltext_source:** pdf-converted
**converter:** pdftotext (default reading-order mode)
**pages:** 16 (complete article)
**raw PDF:** `raw/papers/2026-03-28-nguyen-ai-adoption-toe-dynamic-capabilities.pdf` (gitignored)

---

## Pre-flight checks

**Check 1 — Scope.** 16 PDF pages: complete article, highlights and abstract through references
and Appendix I. Not a sample.

**Check 2 — Identity.** Cover page, DOI and journal match. ScienceDirect's download name
(`1-s2.0-S2949736126000503-main.pdf`) renamed to the wiki slug on acquire. **A first attempt on
2026-09-18 delivered the wrong paper** — Dukhaykh & Alangri (2026), *Dynamic Capabilities and
Sustainable Competitive Advantage in SMEs*, Sustainability 18, 1320 — caught by this check and
deleted at the user's instruction before any conversion.

**Check 3 — Honest scoping.** Full text read. `pdftotext` flattens Tables 1–10; Table 7
(hypothesis tests), Table 8 (R², Q²), Table 9 (controls) and Table 10 (multi-group analysis) were
reconstructed column by column. Figures 1–4 (model, PLS-SEM result, slope plot, power plot) are
images and did not survive conversion.

## Data-quality notes

- **H11 and H12 swap labels.** §2.2 defines H11 as AI adoption moderating BMI → FP and H12 as
  moderating SCA → FP. Table 7 and §4.3 use the opposite numbering (H11 = AI × SCA → FP,
  accepted; H12 = AI × BMI → FP, rejected). The results themselves are consistent: the SCA
  moderation is significant (β = 0.123, p = 0.008), the BMI moderation is not (β = 0.067,
  p = 0.135). The wiki cites paths, not hypothesis numbers.
- **H6 is marked "Accepted" at p = 0.063.** Cost-effectiveness → AI adoption is β = 0.106, CI
  [−0.007, 0.214], significant only at the 10% level the table legend allows; the text calls it
  "marginal", the conclusion says cost-effectiveness "positively affects" adoption.
- **Model fit reported selectively.** §3.4 sets an SRMR threshold of 0.10 for the *estimated*
  model; Table 6 gives the estimated model SRMR = 0.130, and the text reports only the saturated
  model (0.053).
- **Low explained variance on the dynamic-capabilities side.** R²: AI adoption 0.180, BMI 0.040,
  SCA 0.062, FP 0.438 (Table 8). AI adoption explains 4% of business-model innovation and 6% of
  sustainable competitive advantage.
- **SCA and FP overlap in content.** Retained SCA items include "Our company's profits are
  better"; FP is ROA, ROE, ROS, market share and sales growth. SCA1 loaded −0.42 and was dropped
  with SCA6 and FP6. HTMT(SCA, FP) = 0.509, so the constructs separate statistically, but the
  SCA → FP path (β = 0.321) partly relates profit to profit.
- **Moderation power** for AI × SCA → FP is 0.795 (post-hoc), just under 0.80.
- **Table 9 is internally inconsistent**: the coefficients labelled "after controls" (0.125,
  0.417, 0.321) equal Table 7's main-model values, whose R² (0.438) is the "before controls" R²;
  "AI adoption level" also appears as a control variable on FP while AI → FP is a main effect.
- **Common-method bias** checked by full-collinearity VIF only; single respondent per firm;
  perceptual performance measures.

## Why acquired

Identified on 2026-09-18 in an OpenAlex search for organisational (non-education) studies of
classical adoption theories; the one paper in the shortlist that joins TOE and dynamic
capabilities in a single model. Recorded as an open question on
`wiki/concepts/technology-adoption-theories.md` until retrieved.

---

## Full text (pdftotext)

Green Technologies and Sustainability 4 (2026) 100384

Contents lists available at ScienceDirect

Green Technologies and Sustainability
journal homepage:
https://www.keaipublishing.com/en/journals/green-technologies-and-sustainability/

Full-length article

The role of the level of artificial intelligence adoption on business model
innovation, sustainable competitive advantage, and firm performance:
Integrating the TOE framework and Dynamic Capabilities theory
Nguyen Thi Phuong Anh a , Bui Huy Khoi a , Nguyen Quang Thu b , Tran Nha Ghi a ,∗
a

Faculty of Business Administration, Industrial University of Ho Chi Minh City, Viet Nam

b School of Management, University of Economics Ho Chi Minh City, Viet Nam

HIGHLIGHTS
• Technology, organization, and environment drive technology adoption.
• Leadership, government support, and cost shape technology adoption.
• Technology adoption improves innovation, advantage and performance.
• Technology adoption strengthens the advantage-performance link.
• Technology and firm capabilities drive performance.

ARTICLE

INFO

Keywords:
The level AI adoption
Business model innovation
Firm performance
Sustainable competitive advantage
TOE framework

ABSTRACT
Drawing on the TOE framework (Technology-Organization-Environment) and Dynamic Capabilities theory, this
study aims to explain the mechanisms driving the level of Artificial Intelligence adoption (AI) and its resulting
impacts on firm performance. Using the Partial Least Squares Structural Equation Modeling (PLS-SEM) with a
sample of 325 managers from Vietnamese firms, the findings reveal that top leadership support, government
support, and cost-effectiveness of AI investment are critical determinants of AI adoption level. Furthermore,
the level of AI adoption has a positive relationship with business model innovation (BMI) and sustainable
competitive advantage (SCA), thereby enhancing firm performance (FP). The results reveal that the level of
AI adoption strengthens the link between SCA and FP by improving firms’ capacity to identify opportunities
and reconfigure strategic resources, thereby enabling SCA to be translated into FP. Theoretically, this research
contributes by integrating structural (TOE) and dynamic capability perspectives to explain the level of AI
adoption and its outcomes. Practically, the firm should leverage government support policies and leadership
support to optimize AI adoption and translate it into sustainable business value.

1. Introduction
Artificial intelligence (AI) has increasingly captured the attention
of both businesses and society [1]. Emerging opportunities enabled
by AI technologies can strengthen firms and reshape global economic
systems [2]. AI is increasingly important in modern economies and
should be encouraged. According to the Stanford AI Index Report
(2025), private AI investment was USD 109.1 billion in 2024, with 78%
of firms’ AI usage, up from 55% in 2023, showing its rapid adoption in
business activities [3].

In Vietnam, the national strategy envisions that by 2025, with an
orientation toward 2030, the country will become a digital government,
society, and economy (accounting for 20% of GDP), with globally competitive digital firms [4]. According to the Viettel Cyberspace Center,
approximately 92% of digital transformation applications are directly
related to AI [5]. Consequently, AI is considered a key enabler of comprehensive and successful digital transformation [6]. The foundation
for AI adoption is assessed through three pillars: government, technology, and organization. AI applications allow businesses to develop new

∗ Correspondence to: Faculty of Business Administration, Industrial University of Ho Chi Minh City, 12 Nguyen Van Bao, Hanh Thong Ward, Ho Chi Minh
City, Viet Nam.
E-mail addresses: anhntp24121@pgr.iuh.edu.vn (N.T.P. Anh), buihuykhoi@iuh.edu.vn (B.H. Khoi), ngthu@ueh.edu.vn (N.Q. Thu), trannhaghi@iuh.edu.vn
(T.N. Ghi).

https://doi.org/10.1016/j.grets.2026.100384
Received 14 October 2025; Received in revised form 23 March 2026; Accepted 23 March 2026
Available online 28 March 2026
2949-7361/© 2026 The Authors. Publishing services by Elsevier B.V. on behalf of KeAi Communications Co. Ltd. This is an open access article under the CC
BY license (http://creativecommons.org/licenses/by/4.0/).


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

goods and services, improve customer support, and understand customer needs, preferences, and behaviors [7]. Consequently, AI adoption
fosters business model innovation (BMI). Moreover, AI-driven organizations tend to strengthen human creativity and innovation, thereby improving overall firm performance (FP). For instance, generative AI tools
like ChatGPT have been shown to boost employee creativity in realworld settings, especially among employees with strong metacognitive
strategies [8].
Existing evidence has identified key aspects of success for information technology adoption. Earlier AI-related research primarily
focused on technical aspects and specific applications [9,10]. Recent research has examined technical, organizational, and environmental factors affecting AI adoption [11–14]. These findings indicate that internal
organizational conditions (especially managerial roles), external environmental factors, and technological characteristics play crucial roles
in successful AI adoption. AI helps firms streamline processes [14],
improve decision-making [15], and boost productivity [16].
Furthermore, top management support is crucial for AI adoption
[17]. In addition, government support is a crucial environmental factor
that promotes the adoption of AI [13,18]. Moreover, cost-effectiveness
of AI investment is both a barrier and a driver of AI adoption. Numerous
studies indicate that implementation costs, infrastructure requirements,
and limited financial resources negatively affect AI adoption, particularly among firms [19–21]. However, prior studies have mainly
examined these relationships in isolation. A comprehensive model explaining the mechanisms underlying AI adoption decisions remains
lacking.
More importantly, recent studies have confirmed that AI capabilities can drive innovation, generate sustainable competitive advantage
(SCA), and improve FP [18,22,23]. However, the role of AI adoption
in transforming antecedent conditions – such as leadership support,
government policy support, and cost-effectiveness of AI investment –
into strategic outcomes, including BMI, SCA, and improved business
performance, remains insufficiently understood. The lack of linkage
between AI adoption antecedents and consequences creates a gap in
understanding AI value-creation mechanisms at the firm level. This gap
is particularly evident among firms in developing countries such as
Vietnam, where resource constraints and reliance on the institutional
environment significantly influence AI adoption [24].
Chen, et al. [11] proposed several theoretical lenses to explore
how these factors affect AI adoption, notably integrating the TOE
framework [25] and the Diffusion of Innovation theory [26]. Other
models have also been used to assess users’ acceptance of AI, including
the Technology Acceptance Model [27], the Unified Theory of Acceptance and Use of Technology [28] and more recently, the Artificial
Intelligence Device Use Acceptance Model [29]. Alsheiabni, et al. [30]
used the TOE framework to identify implementation constraints such
as inadequate AI deployment skills. Pumplun, et al. [31] enhanced the
TOE model by incorporating data accessibility, safety, and quality as
additional aspects of organizational readiness for AI implementation.
AI adoption has been studied across diverse industries, including
hospitality [32], public organizations [18], telecommunications [11],
and retail [33]. Focusing on the public sector, Mikalef, et al. [18]
identified five factors that affect AI growth: perceived financial expenses, organizational creativity, political pressure, government subsidies, and regulatory approval. Similarly, AI readiness in the service and
exhibition industries has also been examined [34].
AI adoption is inherently complex, requiring not only advanced
software and hardware but also long-term investment in infrastructure and human resources. Hence, it is vital to examine the factors
affecting AI adoption under the combined conditions of organizational
capabilities, government policies, and environmental context. Despite
AI’s emergence as a technological priority, research on its business
value and organizational use remains limited [18]. Consequently, there
is still insufficient understanding of the mechanisms through which

AI generates and transforms business value [34]. Therefore, it is crucial to examine the mechanisms that drive the level of AI adoption
and the value created through AI adoption [35]. The prior studies
rarely examine how government support, top leadership support, and
cost-effectiveness interact to influence AI adoption and its strategic
outcomes. However, firms that adopt AI often differ significantly in
the level of AI adoption. Understanding these variations is important
because deeper AI integration may generate different strategic and
performance outcomes. Nevertheless, empirical research examining the
determinants and consequences of the extent of AI adoption among
adopting firms remains limited, particularly in emerging economies
such as Vietnam. Based on the identified research gap, this study
proposes an integrated model that incorporates the level of AI adoption,
linking government support, top leadership support, and the costeffectiveness of AI investment to BMI, SCA, and FP. To guide this
investigation, two research questions (RQs) are formulated:
RQ1: How do environmental factors (government support), organizational factors (top leadership support), and technological factors
(cost-effectiveness) affect the level of AI adoption?
RQ2: How does the level of AI adoption transform these antecedent
components into strategic outcomes (BMI, SCA, and FP) under what
conditions does AI amplify these effects?
This study addresses the gap (answers two RQs above) by integrating TOE and Dynamic Capabilities perspectives. First, given that
AI adoption level is context-dependent, the TOE framework serves
as a suitable theoretical foundation, as it highlights the contextual
factors that shape adoption behavior. Although numerous scholars
have examined the influence of TOE dimensions on AI adoption [17,
36,37], the linkages between technical, organizational, and environmental components are yet little examined. This gap is supported by
recent studies [38,39] showing that interrelations among TOE components significantly affect digital transformation. Therefore, this study
contributes to the theoretical foundation regarding the relationship
between the components of the TOE framework and AI adoption level,
an area that has remained underexplored in previous research. Second, this study extends theoretical understanding by investigating the
outcomes of AI adoption. Dynamic capabilities theory explains how AI
adoption benefits organizations. AI adoption serves as the platform for
flexible abilities, especially in BMI. AI adoption can help businesses
get better at sensing market opportunities, capturing value, and reconfiguring resources, thereby improving SCA and FP. Drawing upon
Dynamic Capabilities theory, the research examines how AI adoption
influences BMI, SCA and FP. These relationships and the moderating
role of AI adoption remain underexplored in prior research, especially
in emerging economies like Vietnam.
Vietnam serves as a suitable research context due to its representativeness and unique institutional characteristics. First, Vietnamese firms
have limited resources, face significant risks when adopting new technologies, and rely on government support [24]. These challenges are
all common problems in developing countries where cost-effectiveness,
policy support, and leadership support are critical determinants of modern technology adoption. Second, Vietnam’s national AI strategy and
large-scale digital transformation programs create a strongly supportive
institutional environment, emphasizing governmental assistance as a
critical environmental factor within the TOE framework.
While the TOE framework explains the contextual conditions that
facilitate the level of AI adoption, Dynamic Capabilities theory explains
how firms transform the level of AI adoption into strategic value. By
combining these perspectives, this study aims to clarify the mechanisms
influencing the level of AI adoption – particularly the roles of top
leadership support, government support, and cost-effectiveness of AI investment – and their influence on strategic and performance outcomes,
including BMI, SCA, and FP among Vietnamese firms. This approach
addresses the lack of integrated models that examine how these factors jointly shape AI adoption level and its outcomes in emerging
economies. The subsequent sections outline the theoretical foundation,
research methodology, empirical results, discussion, and conclusions.
2


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

2. Theoretical background and research model

advanced AI and Generative AI [57,58]. Furthermore, in emerging
economies, public policies and incentives bolster corporate innovation capabilities and technological competencies, thereby facilitating
the upgrading of AI adoption intensity [59]. Governments worldwide
have allocated substantial resources to AI development [11], providing
subsidies, tax reliefs, training, and consultancy programs to enhance
technological competencies [13,21], reduce adoption risks [21]. Such
assistance is particularly vital for resource-constrained firms, enabling
them to optimize costs and improve the cost-effectiveness of AI investment [14,17,60]. When governments establish clear AI adoption
strategies (e.g., Vietnam’s national AI roadmap to 2030), such initiatives send strong market signals [12]. While AI adoption involves
high levels of risk and uncertainty [61] and requires strong commitment from top leadership [17], government support fosters a favorable
institutional environment [11], strengthens leadership confidence in
AI’s potential [13], and enhances willingness to allocate resources,
financial, technological, and human for AI implementation [17]. This
support also shapes leadership strategic vision, encouraging firms to
review AI as a strategic core competence [11,13].
Firms are more willing to adopt AI when the institutional environment is stable enough to mitigate switching costs, risks, and
policy-related barriers [62]. Accordingly, stronger government support
is expected to increase AI adoption, aligning their internal financial
capabilities with the investment requirements of AI technologies. When
financial resources are well matched with technological investment,
cost-effectiveness improves. Supportive public policies create a favorable environmental context for optimizing the costs of AI implementation, operation, and training [59]. Moreover, government support
facilitates alignment between firms’ business strategies and external
environmental conditions, making it easier for top management to
approve, endorse, and invest in AI technologies. The stronger the
level of government support, the more likely leaders are to perceive
AI investment as consistent with environmental trends and long-term
benefits, thereby increasing the adoption of AI [63].
𝐻3 : Government support positively affects the level of AI adoption among
adopting firms.
𝐻4 : Government support positively affects cost-effectiveness of AI investment.
𝐻5 : Government support positively affects top leadership support for AI.
Cost-effectiveness refers to managers’ perceptions regarding the
balance between the expected benefits and the costs associated with
adopting a particular technology [64]. In the context of Artificial
Intelligence (AI), cost-effectiveness reflects the extent to which managers believe that AI technologies can improve organizational efficiency while reducing operational costs and time [65]. Within the TOE
framework, technological characteristics including relative advantage,
compatibility, complexity and cost are major factors in technology
adoption [36]. When AI delivers cost-effectiveness through operational
optimization, reductions in transaction costs, and resource saving, firms
perceive the technology as strategically valuable [47]. Consequently,
cost-effectiveness enhances organizational readiness and increases the
likelihood of AI adoption [36,66,67]. Davenport [68] emphasized that
AI-driven analytics optimize marketing strategies, such as promotions
and discounts. Costs can be further reduced by automating simple
customer service tasks, thereby facilitating marketing operations and
reducing market transaction efforts. These advantages together recognize cost-effectiveness as a crucial technological element boosting AI
adoption in the TOE framework. Within the technological dimension of
the TOE framework, cost-effectiveness emerges as a critical determinant
of the extent of AI assimilation [58]. Similarly, research grounded in the
TOE framework demonstrates that cost-related enablers significantly
enhance the intention to expand AI adoption [57]. New technologies adoption is achieved when technology investment requirements
align organization’s financial capacity. AI adoption requires a major
investment, including technology acquisition, data infrastructure and
specialized personnel training. When firms assess AI investment as

2.1. Theoretical background
The TOE framework, proposed by Eveland and Tornatzky [25],
highlights the technological, organizational, and environmental variables influencing technology adoption decisions. In addition to technological characteristics, organizational readiness and external forces
substantially affect the adoption of technological innovation [25]. This
framework is widely used in IT, manufacturing, healthcare, tourism,
and financial services after conceptual and empirical validation [40,
41]. Recently, the TOE framework has been extended in developing
countries by emphasizing the roles of perceptions, facilitating conditions, environmental knowledge, and installation costs as critical
barriers to technology adoption [42]. Firms in emerging markets often face resource constraints and increased risk when implementing
new technologies [24]. This theoretical perspective is consistent with
the context of AI adoption, where cost-related factors and capability
constraints play decisive roles.
The Dynamic Capabilities theory emerged as a response to the
limitations of the Resource-Based View (RBV) in environments that
change quickly. Teece, et al. [43] and later Teece [44] defined dynamic
capabilities as the organization’s capacity to identify opportunities
and threats (sensing), seize opportunities (seizing), and reconfigure or
realign resources (reconfiguring) to sustain competitive advantage in
turbulent markets. Recent research has further developed this theoretical viewpoint within digital transformation, specifically concerning AI
adoption [45].
2.2. Research hypotheses and research model
Top leadership support, a core component of the organizational
context within the TOE framework, is widely acknowledged as a critical determinant of AI adoption [21,46,47]. It refers to the active
involvement and commitment of senior executives in implementing
information systems and information technology initiatives [46]. Prior
research emphasized that leadership support enhances a firm’s technological capability to successfully adopt and deploy new products or
services [48]. Moreover, senior management commitment positively
influences the AI adoption by aligning strategic objectives, ensuring sufficient financial investment, and allocating resources appropriately [11,
49]. Prior research suggests that managers are more likely to adopt
new technologies when they perceive that the expected benefits outweigh the implementation and operational costs [50]. Importantly,
such evaluations are often subjective and shaped by organizational
and institutional support that reduces perceived financial risks and
uncertainty. Within the AI context, top leadership support signals organizational readiness and legitimacy, fosters a digital culture, reduces
employee resistance, and promotes cross-functional collaboration [21].
Moreover, strategic endorsement from top management is essential
for integrating AI into core business processes [51]. When leadership
proactively provides support and drives organizational change, firms
exhibit a higher probability of achieving full-scale AI implementation
across all business processes [52].
𝐻1 : Top leadership support positively affects the level of AI adoption
among adopting firms.
𝐻2 : Top leadership support positively affects cost-effectiveness of AI
investment.
Regarding the TOE framework, government support represents a
crucial environmental factor influencing technological innovation and
AI adoption [13,46,53,54]. Supportive policies, financial incentives,
training programs, or clear regulatory frameworks are more likely to
lead to the adoption of innovative technology [24,55]. Governmental
policies often provide guidelines for AI development [56]. Empirical
evidence indicates that governmental support significantly influences
an organization’s readiness and strategic commitment to deploying
3


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

cost-effective, they are more likely to adopt AI [69]. Within the TOE
framework, cost-effectiveness represents a critical technological aspect
that enhances organizational readiness for adoption [59,62].
𝐻6 : Cost-effectiveness of AI investment positively affects the level of AI
adoption among adopting firms.
The level of AI adoption measures the extent to which firms integrate AI technologies into their processes and decision-making [65]. AI
adoption level is reflected in the extent to which AI technology is deeply
integrated into operations (e.g., marketing processes) and the degree to
which it significantly transforms core business processes [70]. Under
the TOE, technological enablers (e.g., perceived cost-effectiveness), organizational enablers (e.g., top leadership support), and environmental
enablers (e.g., government support) are expected to drive how broadly
and deeply AI is deployed once initial adoption has occurred.
AI technology enables transformative changes in goods, services, innovation processes, and business structures. By automating operations
and enhancing data-driven decision-making, AI provides opportunities
for value creation [71] and gains revenue within business models [72,
73]. Digitalization, supported by AI, facilitates a firm’s shift from
product-centered models to more digitally integrated business models with higher revenue potential [74]. Recent studies emphasized
that AI-driven capabilities will radically reshape value propositions
and reconfigure mechanisms for creating, delivering, and capturing
value [71]. These capabilities of AI provide substantial potential to
boost BMI, generate new income streams, and increase competitiveness,
particularly in digital services [71]. Furthermore, empirical evidence
suggests that the deeper integration of AI adoption requires firms to
reconfigure their value propositions and catalyze BMI [75]. Accordingly, dynamic capabilities promote BMI [76]. Therefore, AI is widely
recognized as a strategic enabler of BMI. Previous studies suggested
that firms with competitive advantages are more likely to provide services and goods superior to competitors [77]. AI adoption strengthens
the delivery of automated services, minimizing errors and aligning
offerings with customer expectations [78]. The adoption of AI completely changes competition by accelerating firms’ decision-making
processes and operational efficiency, thereby creating significant performance differences among competitors [79]. Along with boosting
information for better decision-making, AI enables changes in business
operations and governance structures, fostering sustainable competitive
practices across industries [80]. Furthermore, AI-integrated organizations indicate that higher levels of AI maturity enable firms to improve
their competitive positioning, enhance operational efficiency, and drive
sustainable long-term value creation [81]. By linking AI with organizational resources, firms develop dynamic capabilities which serve as
vital mechanisms for sustainable competitive advantage in uncertain
environments [82,83].
𝐻7 : T he level of AI adoption positively affects BMI.
𝐻8 : T he level of AI adoption positively affects SCA.
BMI enhances the initial business model by enabling modifications
to obtain more value [84]. A company cannot rely on a single unique
model for long-term success [85]; instead, it must adapt and innovate
its business models to maintain a competitive advantage and enhance
performance [86]. BMI encompasses innovation related to value creation, value acquisition, and value delivery [87]. Transaction and
operational performance can be improved by BMI and market volume
via digital channels. In addition, empirical evidence confirmed that BMI
strongly influences operational performance [87–91].
𝐻9 : BMI positively affects FP.
SCA defines a company’s capacity to achieve outstanding performance over time by utilizing resources that are precious, scarce, and
unique [92]. Within the framework of sustainable digitization, sustainability also reflects firms’ capacity to continuously adapt and reconfigure resources – such as AI-enabled processes – in response to
environmental pressures and sustainability-oriented efficiency goals
[93]. Firms with strong SCA differentiate their offerings through superior quality, reliability, and responsiveness, which enhances customer

loyalty and raises switching costs, thereby improving sales and profitability [22,78,94]. From a dynamic capabilities perspective, SCA in
the context of AI-driven transformation is increasingly associated with
a firm’s ability to realign its technological capabilities and generate
long-term value. Accordingly, AI adoption is expected to strengthen the
transformation of sustainability-oriented competitive advantages into
FP.
𝐻10 : SCA positively affects FP.
The adoption of AI functions as a complementary organizational
capability enhances BMI’s ability to gain FP. From a dynamic capabilities perspective, AI is considered a catalyst for redesigning business
models more rapidly and aligning resources with evolving market
demands [95]. By integrating AI into BMI processes, firms can leverage advanced analytics and automation to accelerate innovation in
value creation, delivery, and capture, thereby improving operational
performance. When BMI serves as the transmission channel for AI’s
positive impact on performance [96], a high level of AI adoption
optimizes business model redesign, leading to productivity gains and
increased profitability [17,97]. In dynamic environments, continuous
BMI is essential, and AI’s rapid data analytics capabilities enable firms
to adjust and optimize their BMI in response to market changes, thereby
maximizing the performance outcomes of BMI [95]. When AI is implemented at a high level, firms are better able to leverage business
model innovation (BMI) through predictive analytics, automation, and
process optimization, thereby enhancing the efficiency with which BMI
is translated into financial performance outcomes. A higher level of AI
integration enables firms to accelerate innovation processes and realize
business value more effectively [75]. In addition, firms with higher
AI adoption levels are better able to amplify the impact of innovation
strategies on organizational performance [23,98].
Regarding Dynamic capability theory, AI adoption serves as a supplementary capacity to foster SCA and improve FP. AI adoption boosts
sensing, seizing, and reconfiguring mechanisms, enabling firms to leverage valuable and rare resources more effectively [99]. Empirical evidence showed that the influence of marketing analytics capacity on
dynamic capabilities and SCA is stronger with higher levels of AI adoption. Because it accelerates the transformation process through dynamic
capabilities, which translates into SCA [22]. In dynamic and hazardous
business environments, AI adoption allows firms to swiftly adjust business operations, mitigate risks, and enhance efficiency, thereby sustaining and leveraging SCA [100]. When a firm already possesses SCA, such
as a distinctive business model and unique resources, AI enables it to
optimize automation, process and forecasting [22] and converts into
superior performance [37]. Recent studies on AI-integrated organizations suggest that higher levels of AI maturity enable firms to leverage
their core competitive advantages more effectively and achieve more
sustainable performance outcomes ( [81].
𝐻11 : T he level of AI adoption moderates the link between BMI and FP.
𝐻12 : T he level of AI adoption moderates the link between SCA and FP.
AI technology enables companies to overcome challenges in the
marketplace and enhance operational efficiency [37]. In dynamic business environments, firms utilize data and analytics to enhance decisionmaking, thereby optimizing operational efficiency and maximizing return on investment [101]. Company success is influenced by abilities
in data analysis and decision-making, both of which rely on the use
of modern technologies like AI. Recent research on firms in Pakistan
suggested that AI adoption and the level of technological readiness
enhance sustainable performance through the roles of organizational
capability building and organizational learning [102]. When AI adoption is high, firms tend to improve operational efficiency, forecasting
accuracy, and decision-making speed, thereby enhancing financial performance. Empirical evidence also suggests that AI adoption level
is associated with more effective decision-making and higher overall
organizational performance [65].
𝐻13 : T he level of AI adoption positively affects FP.
Based on these arguments, the suggested research framework is
displayed in Fig. 1.
4


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

Fig. 1. Proposed research model.
Table 1
Main construct non-response bias.

3. Methodology
3.1. Research process
The study was conducted through two main stages: a preliminary
study and a formal study. A preliminary study was carried out through
group discussions with nine experts who are senior managers of firms,
in order to adjust the measurement scales to fit the research context.
The formal study was a quantitative research phase conducted with a
sample size of 325 managers.

Constructs

Response

Mean

SD

SE

𝑃 -value

LS

1
2
1
2
1
2
1
2
1
2
1
2
1
2

2.424
2.468
2.252
2.200
3.393
3.235
2.353
2.475
3.413
3.214
3.097
3.181
2.702
2.626

0.825
0.825
0.868
0.849
0.873
0.877
0.735
0.854
0.827
0.867
0.634
0.704
0.799
0.768

0.057
0.076
0.060
0.078
0.061
0.081
0.051
0.079
0.057
0.080
0.044
0.065
0.056
0.071

0.642

GS
CE
AI
BMI
SCA

3.2. Data collection

FP

The target respondents of the study comprised firms located in the
Southeast region of Vietnam that had adopted AI. The respondents
were middle and senior-level managers who possessed comprehensive
knowledge of their firm’s strategic orientation and the process of AI
adoption within the organization. Due to limitations in accessing firms
that have adopted AI in the research area, this study did not employ
stratified sampling. A targeted sampling approach was employed to
guarantee that only firms that have adopted AI were included in the
survey. Firms were considered to be adopting AI if they were using
at least one AI activity, such as data analytics, process automation,
decision support, demand forecasting, or customer interaction on a
Chatbot [22]. Firms that did not satisfy these standards were excluded
from the sample. Given this sampling design, the objective of the study
is not to examine the determinants of AI adoption versus non-adoption.
Instead, the study focuses on understanding the factors that influence
the level of AI adoption among firms that have already implemented AI
technologies. This approach allows the study to investigate variations
in AI adoption level across firms and identify the organizational and
environmental factors that drive deeper and more advanced use of AI
technologies.
A 75-person pilot test refined the measurement scales for reliability
and validity before the main survey. Subsequently, the finalized questionnaire was distributed between March 2025 and June 2025. Data
were gathered via an established survey distributed in both printed
form (offline) and online (through Google Forms and email). 400 questionnaires were sent to firms. The response rate was 87.5%, with 350
surveys returned. 325 questionnaires were kept for examination after
filtering for incomplete or inconsistent responses. This corresponds to
a valid response rate of 92.86% of the returned questionnaires and
81.25% of the total questionnaires distributed.

0.600
0.117
0.195
0.141
0.281
0.401

Note: 1 (early respondents); 2 (late respondents); SD: standard deviation; SE: standard
error.

To evaluate the possible existence of non-response bias, the study
compared early respondents (the first 50%) and late respondents (the
last 50%), based on the rationale that late responses may most closely
represent non-respondents [103]. Independent samples T-test was used
to examine the mean scores of constructs between the 2 groups. No
significant changes were identified (p > 0.05), demonstrating that nonresponse bias is low and does not affect data validity (Table 1). The
relatively low mean values observed for some constructs reflect the
respondents’ perceptions of limited adoption or implementation levels
within their firms. This can be explained by the fact that AI adoption
level and related organizational capabilities are still at an early stage
among many firms in the sample.
3.3. Measurement development and translation procedure
To test the research model’s constructs, validated items from previous studies were modified for a suitable research context. All items
were evaluated with a five-point Likert scale (1 = ‘‘Strongly disagree’’ 5
= ‘‘Strongly agree’’). Specifically, the measurement scales included top
leadership support with four items [36], government support with five
items [21], cost-effectiveness of AI investment with three items [64],
BMI with four items [96], and SCA with six items [104].
The level of AI adoption is the extent to which organizations use
AI in their business processes. The measurement items were adapted
from the scale developed by Chen and Tajdini [70], which evaluates AI
5


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

Table 2
Sample characteristics.
Categories
Firm size

Industry sector

Years in operation
Geographical area
Level of AI adoption

Sub-categories

Frequency

Percentage (%)

Small (< 50 employees)
Medium (50–250 employees)
Large (> 250 employees)
Manufacturing & processing
Trade & services
Technology & software
Others (education, logistics, healthcare, etc.)
< 5 years
5–10 years
> 10 years
Southeast Vietnam (Ho Chi Minh City, Binh Duong, Dong Nai, etc.)
Basic (experimental)
Intermediate (management and operations)
Advanced (strategic and innovative)

91
146
88
114
104
65
42
72
124
129
325
98
146
81

28
45
27
35
32
20
13
22
38
40
100
30
45
25

integration into business processes and organizational activities. Firm
performance was measured using perceptual indicators reflecting overall organizational performance. The items measure revenue growth,
market share, ROI, and ROE [105,106].
The study used measurement scales from previous studies in strategic management and digital technology research. Back-translation was
used to ensure linguistic comparability of the questionnaire. Two bilingual research domain experts translated the English questionnaire into
Vietnamese. A third bilingual translator independently translated the
Vietnamese version into English. The original questionnaire and backtranslated version were examined for semantic equivalence and consistency.
A panel of three academic experts in strategic management and
digital technologies, and two industry practitioners with experience in
digital transformation and AI implementation, assessed the questionnaire to ensure content validity. Each measurement item was assessed
by specialists for relevance, clarity, and representativeness. In addition,
cognitive interviews were conducted with ten respondents from firms
that have experience with AI-related business practices. The purpose of
these interviews was to assess whether respondents clearly understood
the questionnaire items and interpreted them consistently with the
intended constructs. In response to expert panel and cognitive interview
input, numerous small phrasing changes were made to improve clarity.

In the evaluation of the structural model, the variance inflation
factor (VIF < 5) was used to test multicollinearity and confirm variable
independence [107]. Hypotheses were tested using bootstrapped path
coefficients and significance levels from 5000 resamples [113]. R2
coefficient values of 0.25, 0.50, and 0.75 indicate poor, moderate, and
strong explanatory power of the research model [108]. The effect size
(f2 ) assessed the impact of each independent variable [112]. Predictive
relevance (Q2 ) was evaluated using the Blindfolding technique, Q2
values above zero indicate model capability [107].
The study data were obtained from only one source. This study
is controlled for common method bias (CMB) using the VIF value, as
recommended by Kock [114]. Within the recommended threshold of
3.3, VIF values suggest CMB is not a significant issue.
A multi-group analysis (MGA) was performed to compare structural relationships across firms of different sizes. The sample included
SMEs and large firms. Whether SMEs and large firms had significantly
different structural relationships was assessed using PLS-MGA.
4. Results
4.1. Sample
The study was conducted on 325 firms located in the Southeastern
region of Vietnam, encompassing diverse types and scales of firms
(Table 2). In terms of firm size, approximately 28% were small firms
(< 50 employees), 45% were medium-sized (50–250 employees), and
27% were large firms (more than 250 employees). Regarding industry
sectors, most firms operated in manufacturing and processing (35%),
trade and services (32%), and technology and software (20%), with
a smaller portion in other sectors such as education, logistics, and
healthcare (13%). In terms of years in operation, 22% of firms had been
established for less than five years, 38% had been operating for 5–10
years, and 40% had been in business for more than 10 years. Notably,
all firms were in the Southeast region, primarily in economically developed provinces such as Ho Chi Minh City, Binh Duong, and Dong
Nai. Regarding the level of AI adoption, around 30% of firms were at
the basic (experimental) stage, 45% were at the intermediate (managerial/operational) level, and 25% had reached an advanced level, where
AI was strategically integrated into innovation and business model
transformation.

3.4. Data analysis method
PLS-SEM approach was employed with SmartPLS (version 4.1.1.4)
software to evaluate the proposed hypotheses. This method is appropriate for exploratory studies, complex models involving mediating and
moderating effects, and is suitable for small sample sizes [107].
In assessment of the measurement model, outer loadings (> 0.7)
were acceptable for indicator reliability [108]. Next, Cronbach’s alpha and composite reliability assessed construct internal consistency.
The threshold is usually above 0.70 [107,109]. Convergent validity is
assessed by the average variance extracted (AVE > 0.5) [110]. Furthermore, the Fornell–Larcker criterion and the Heterotrait–Monotrait
ratio (HTMT < 0.85) were to assess discriminant validity among constructs [111]. Additionally, the overall model fit was assessed by the
SRMR indicator of the estimated model, with a threshold of 0.10. The
NFI also provides additional evidence supporting the overall model
fit. To ensure path coefficient robustness, all direct and moderating
effects were examined using bootstrapping with 5000 resamples and
95% confidence intervals.
Statistical power analysis for moderating testing was carried out
using G*Power (version 3.1.9.7) with a linear multiple regression fixed
model, focusing on the increase in R2 . With a statistically significant
𝛼 = 0.05, the number of predictors includes independent variables,
moderating variables, interaction variables, and an effect size. The
minimum sample size to a power of 0.80 is 300 observations [112],
so 325 is sufficient to assess the model’s moderating impact.

4.2. Measurement model assessment
Table 3 shows that construct reliability and internal consistency
are satisfactory. Specifically, Cronbach alpha (𝛼) coefficients ranged
from 0.809 to 0.882, exceeding the minimum threshold of 0.70 [109].
Similarly, the CR values ranged from 0.885 to 0.914, also surpassing
the recommended 0.70 cutoff [107]. AVE values of 0.656 to 0.729
exceeded the 0.50 threshold, ensuring convergent validity [110]. Most
outer loadings (𝜒) were above 0.70, indicating good construct-items
6


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

Table 3
Outer loadings, Cronbach Alpha, CR, AVE.
Construct

𝜒

The level of AI adoption (AI):
AI1

AI2

AI3

Our firm has implemented AI technologies across
its business
processes (e.g., marketing processes).
Compared to AI’s potential, the firm’s AI
implementation is
extensive.
AI technologies have significantly transformed our
firm’s
business processes.

BMI3
BMI4

The firm redesigned customer value.
New businesses and participants were added to the
firm’s value
generation process.
The firm invented new revenue streams.
The firm introduced new goods, info, and services.

AI technologies help firms save time and cost.
AI systems are cheaper than others.
AI technologies reduce time and effort costs.

FP5

GS2

GS3

GS4

GS5

LS3

LS4

SCA3
SCA4
SCA5

0.723

0.809

0.885

0.719

0.869

0.905

0.656

0.882

0.914

0.68

0.849

0.898

0.688

0.86

0.905

0.705

0.877
0.874
0.791

Firm performance measured by ROA.
Firm performance measured by ROE.
Firm performance measured by ROS.
The firm’s market share in its primary product and
market
segments.
Sales growth in its primary markets and goods.

0.777
0.827
0.815
0.831

0.798

The government has prepared public infrastructure
for digital
technology adoption.
The government promotes the adoption of digital
technology
through training and education.
Government consulting services for the utilization
of digital
technology are adequate.
Government financial support encourages the use
of digital
technology.
Under the national AI policy, the government is
providing tax
incentives, AI training, and infrastructure to
promote the
adoption of digital technology.

0.875

0.795

0.837

0.839

0.775

Managers are willing to risk AI adoption.
Managers know how AI can boost firm
performance.
The firm is committed to acquiring management
and technical
skills for AI implementation.
Managers can strategically use new IT technology.

0.822
0.832
0.837

0.826

Sustainable competitive advantage (SCA)
SCA2

0.913

0.852
0.858

Top leadership support (LS)
LS1
LS2

0.873
0.820
0.871

Government support (GS)
GS1

0.729

0.820

Firm performance (FP)
FP1
FP2
FP3
FP4

AVE

0.889

0.905

Cost-Effectiveness (CE)
CE1
CE2
CE3

CR

0.814
0.833

Business model innovation (BMI)
BMI1
BMI2

𝛼

Our company has better R&D capabilities than our
competitors.
Our company has better management capabilities
than our competitors.
Our company’s profits are better.
Our company’s corporate image is better than our
competitors.

0.875
0.892
0.835
0.750

Note: Outer loadings (𝜒), Cronbach Alpha (𝛼), Composite reliability (CR), Average variance extracted (AVE) (after removing FP 6; SCA1 and
SCA6).

7


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

Table 4
Fornell–Larcker discriminant validity assessment.
AI
BMI
CE
FP
GS
LS
SCA

4.3. Structural model assessment

AI

BMI

CE

FP

GS

LS

SCA

0.854
0.200
0.240
0.335
0.291
0.361
0.249

0.850
0.330
0.505
0.260
0.262
0.168

0.848
0.564
0.349
0.252
0.244

0.810
0.498
0.350
0.445

0.825
0.270
0.303

0.829
0.132

0.840

The hypothesis testing results reveal that the majority of hypotheses
were validated at statistically significant levels, except for H12 (Table
7). Specifically, top leadership support had a significant positive impact
on both the level of AI adoption (𝛽 = 0.286, p = 0.000) and costeffectiveness (𝛽 = 0.171, p = 0.001). Similarly, government support
positively influenced cost-effectiveness (𝛽 = 0.303, p = 0.000), the level
of AI adoption (𝛽 = 0.177, p = 0.001), and top leadership support
(𝛽 = 0.270, p = 0.000). Cost-effectiveness showed a marginal effect
on the level of AI adoption (𝛽 = 0.106, p = 0.063). In addition, the
level of AI adoption had significant positive effects on BMI (𝛽 = 0.200,
p = 0.000), SCA (𝛽 = 0.249, p = 0.000), and FP (𝛽 = 0.125, p = 0.004).
Notably, BMI (𝛽 = 0.417, p = 0.000) and SCA (𝛽 = 0.321, p = 0.000)
were the strongest drivers of FP (Fig. 2).
The interaction between AI × SCA → FP (H11: 𝛽 = 0.123, p = 0.008),
with a coefficient within the 95% confidence interval of [0.030; 0.211),
shows the statistical relevance of the moderating impact. As illustrated
in Fig. 3, when the level of AI adoption is low (–1 SD), the relationship
between SCA and FP is weak; when the level of AI adoption is at a
moderate level, the effect of SCA on FP becomes stronger; and when the
level of AI adoption is high (+1 SD), the relationship between SCA and
FP is the strongest, as reflected by a significantly steeper slope. These
findings suggest that the level of AI adoption functions as an amplifying
mechanism, enabling firms to leverage existing competitive advantages
to achieve superior business performance more effectively. However,
the moderating effect of AI × BMI → FP (H12: 𝛽 = 0.067, p = 0.135) is
not statistically significant at the 5% level due to a confidence interval
of [−0.025; 0.152], which includes zero.
A post-hoc power was conducted to assess the moderation effect (AI
× SCA → FP). The noncentral F approach was used at an 𝛼-level of
0.05, with one tested predictor (u = 1) and four other predictors (m
= 4). According to the effect size (f2 = 0.024) (Table 7) and the actual
sample size (n = 325), the achieved power was 0.795, which is slightly
below the conventional threshold of 0.80. With 1 numerator and 320
denominator degrees of freedom (df), the critical F value was 3.87. A
considerable interaction effect was detected by the sample size (n =
325), suggesting the robustness of the substantial moderation finding
(Fig. 4).
The VIF values for all independent variables were below 3.3, meeting the recommended threshold [107,114], confirming that multicollinearity was not a concern and that CMB was negligible (Table 7).
The effect size (f2 ) ranged from 0.012 to 0.289, with minor effects
at CE → AI (f2 = 0.012) and medium-to-strong effects at BMI → FP
(f2 = 0.289) and SCA → FP (f2 = 0.168) [112]. Explanatory power for
FP was moderate-to-substantial (R2 = 0.438), while other endogenous
factors, such as AI (R2 = 0.180), CE (R2 = 0.149), LS (R2 = 0.073),
BMI (R2 = 0.040), and SCA (R2 = 0.062), had lower values [116]. The
model has predictive relevance, as all Q2 values were positive (0.026
to 0.113) [107,111] (Table 8).
After including control variables, the model’s explanatory power
(R2 ) increased, rising from 0.438 to 0.470 (𝛥R2 = 0.032). The main
hypothesized associations (AI → FP, BMI → FP, and SCA → FP) remained significant, with equal size effects, indicating that the research
findings are robust to firm-level heterogeneity. Among the control
variables, industry type, firm size, and AI adoption level show positive
and statistically significant effects on FP; however, firm age does not
show a statistically significant effect (Table 9).
A permutation-based multi-group analysis (MGA) was used to compare the structural relationships between SMEs and large firms (Table
10). The results indicate that most relationships are statistically invariant across the two groups, suggesting that the overall model is robust
across firm sizes. However, a significant difference is observed for the
path from government support to AI adoption level (p = 0.036), which
is positive and significant among SMEs but not among large firms. This
finding implies that SMEs rely more heavily on external institutional

correlation. Item FP6 (−0.024), SCA1 (−0.42), and SCA6 (0.00) have
very low or negative outer loadings, ignoring reliability criteria and
convergent validity (Appendix I). Therefore, these items were removed
to enhance construct validity and measurement quality.
The remaining indicators still adequately represent the theoretical
domain of sustainable competitive advantage (SCA). Specifically, the
retained items capture several key dimensions of competitive superiority relative to competitors. The indicators related to R&D capabilities (SCA2) and management capabilities (SCA3) reflect the firm’s
superior internal capabilities, which are widely recognized as fundamental sources of competitive advantage in the resource-based view
(RBV) literature. In addition, profit performance (SCA4) represents the
economic outcomes associated with superior competitive positioning,
while corporate image (SCA5) reflects reputational advantages that
strengthen a firm’s competitive standing in the market. Taken together,
these indicators capture both capability-based advantages and marketbased outcomes, which are core elements of SCA. Therefore, despite
the removal of two indicators, the remaining items still provide a
theoretically meaningful representation of the SCA construct.
Similarly, the retained indicators for firm performance (FP) continue to capture the key dimensions of organizational performance
commonly used in strategic management and business research. The
firm’s resource efficiency and profit generation are measured by ROA,
ROE, and ROS. In addition, market share and sales growth also reflect
the firm’s competitiveness and growth in its primary markets. Financial and market performance indicators were used to evaluate firm
performance. The remaining indicators comprehensively represent firm
performance.
After removing the problematic indicators (FP6, SCA1 and SCA6),
the measurement model was reassessed. All constructs have Cronbach’s
alpha and composite reliability above 0.70 for internal consistency.
Convergent validity was also supported, as the AVE values were above
the recommended level of 0.50. The Fornell–Larcker criterion (Table 4)
and HTMT (Table 5) assessed discriminant validity. The results show
that all constructs are empirically distinct. These findings suggest the
refined measurement model is reliable and valid.
According to Fornell and Larcker [110], each construct is conceptually distinct and exhibits sufficient discriminant validity, as the
diagonal square roots of the AVEs are greater than the inter-construct
correlations within the same row and column (Table 4).
Heterotrait–Monotrait (HTMT) ratio results showed that all HTMT
values ranged from 0.156 to 0.666, below the recommended 0.85
[111], confirming that the measurement constructs were distinct and
not conceptually overlapping (Table 5).
The SRMR value of the saturated model was 0.053 (< 0.08), indicating a good model fit [115] (Table 6). The saturated model has
an acceptable overall fit because the NFI value of 0.826 exceeds 0.80.
Additionally, D_ULS and d_G indexes also fall within reasonable ranges,
indicating that the theoretical and empirical models differ slightly. The
research model meets the overall model fit requirements in the current
PLS-SEM methodological guidelines [111].
8


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

Table 5
HTMT discriminant validity assessment.
AI
BMI
CE
FP
GS
LS
SCA
AI × SCA
AI × BMI

AI

BMI

CE

FP

GS

LS

SCA

AI × SCA

0.235
0.282
0.392
0.339
0.431
0.293
0.303
0.197

0.382
0.573
0.292
0.300
0.189
0.101
0.060

0.666
0.400
0.291
0.295
0.186
0.113

0.565
0.402
0.509
0.281
0.151

0.306
0.337
0.164
0.133

0.156
0.075
0.062

0.142
0.102

0.295

Fig. 2. PLS-SEM results.

Fig. 3. Moderating effect of the level of AI adoption between SCA and FP.

9

AI × BMI


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

Fig. 4. A post-hoc power for the moderating role of the level of AI adoption between SCA and FP.
Table 6
Model fit assessment.
SRMR
d_ULS
d_G
Chi-square
NFI

Saturated model

Estimated model

0.053
1.124
0.439
873.033
0.826

0.130
6.897
0.559
1004.940
0.800

emerging economies, where firms prioritize external support, government support creates a suitable institutional environment that boosts
leadership confidence and strategic alignment [119]. The findings align
with the framework of TOE (environmental context) which emphasize
the fit between resource conditions and technological requirements.
Furthermore, Vietnam’s institutional policy, particularly the National
AI Strategy and digital transformation programs, reduces uncertainty
and risk, enables firms to adopt AI. In contrast, Mustafa, et al. [120]
found that corporate social responsibility, environmental knowledge,
and costs, except for government incentives, play decisive roles in installation intentions. In order to effectively reduce risk and transaction
costs, support programs should be combined with training, consulting,
and compliance monitoring.
This empirical evidence indicates that the level of AI adoption is
positively associated with BMI, SCA, and FP. The results match with
previous works that emphasize AI adoption as an essential enabler
of BMI [97]. AI adoption boosts business operations, changes and
governance structures [51], and it is integrated as a core component of
business models to maintain competitiveness [61]. Although the effect
of the level of AI adoption on BMI is relatively small, it shows that
AI plays a complementary rather than a primary role in driving BMI.
While AI supports experimentation and resource reconfiguration, BMI
remains shaped mainly by strategic, organizational, and market factors.
While AI capabilities enable process optimization, fostering innovation
and transformation [121], AI adoption reduces costs and improves profitability [122]. AI also improves dynamic capabilities (sensing, seizing,
and reconfiguring resources) to respond to environmental turbulence,
making it a strategic tool for competitiveness [83,100].
Empirical evidence proves that the level of AI adoption influences
the link between SCA and FP by enhancing the value of strategic resources. From a Dynamic Capabilities viewpoint, AI enhances sensing,
seizing, and reconfiguring mechanisms, allowing firms to utilize rare
and unique resources more efficiently in dynamic environments [100].
AI allows firms to convert sustainability-oriented competitive advantages into superior financial outcomes. In line with the green technology context, SCA should incorporate environmental dimensions,
as AI facilitates eco-efficiency and green innovation rather than focusing solely on economic benefits [102]. Accordingly, the level of
AI adoption acts as a complementary capability that accelerates resource transformation and enhances the strategic impact of SCA on
performance.

support to adopt AI technologies, whereas large firms may depend more
on internal resources and capabilities. Additionally, the moderating
effect of the level of AI adoption on the BMI–FP relationship shows
marginal differences between the two groups (p = 0.062), suggesting
that AI may strengthen the performance impact of BMI more strongly
in large firms.
5. Discussion
Using the TOE framework and dynamic capabilities perspective,
this study helps explain how AI adoption affects organizational outcomes. The research results indicate that top leadership support and
government support are crucial factors influencing cost-effectiveness
of AI investment. Specifically, top leadership support significantly and
positively affects AI adoption and cost-effectiveness, consistent with
prior works, highlighting the meaning of leadership support in the
level of AI adoption. Leadership support is a vital component in the
implementation of new technology [117]. Particularly, when AI aligns
with the existing values of a company, top executives are to support
AI adoption [21]. Without top leadership support, securing the necessary financial and infrastructural resources for AI initiatives may be
challenging [13]. The results support the TOE theory by proposing that
organizational context affects technology adoption.
The findings also show that government support, representing the
environmental dimension within the TOE framework, significantly contributes to leadership support, improves the cost-effectiveness of AI
investment, and is positively associated with the level of AI adoption.
The findings match previous research. Government policies, such as
grants, training, and regulations, reduce the cost and risk of AI adoption, thereby fostering organizational readiness for AI [21,118]. In
10


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

Table 7
Hypothesis testing.
Hypothesis

Direct effects
H1
H2
H3
H4
H5
H6
H7
H8
H9
H10

Paths

SD

𝛽

LS → AI
LS → CE
GS → CE
GS → AI
GS → LS
CE → AI
AI → BMI
AI → SCA
BMI → FP
SCA → FP

T

f2

VIF

CIs
2.50%

97.50%

P values

Conclusion

0.286***
0.171***
0.303***
0.177***
0.270***
0.106*
0.200***
0.249***
0.417***
0.321***

0.057
0.052
0.052
0.055
0.057
0.057
0.056
0.053
0.044
0.043

5.033
3.282
5.798
3.244
4.724
1.857
3.569
4.731
9.442
7.426

0.090
0.032
0.100
0.032
0.079
0.012
0.042
0.066
0.289
0.168

1.113
1.079
1.079
1.186
1.000
1.175
1.000
1.000
1.070
1.090

0.175
0.069
0.200
0.069
0.158
−0.007
0.091
0.143
0.328
0.235

0.400
0.269
0.405
0.282
0.381
0.214
0.309
0.354
0.502
0.407

0.000
0.001
0.000
0.001
0.000
0.063
0.000
0.000
0.000
0.000

Accepted
Accepted
Accepted
Accepted
Accepted
Accepted
Accepted
Accepted
Accepted
Accepted

Moderating effects
H11
H12

AI × SCA → FP
AI × BMI → FP

0.123***
0.067ns

0.046
0.045

2.65
1.495

0.024
0.008

1.168
1.120

0.030
−0.025

0.211
0.152

0.008
0.135

Accepted
Rejected

H13

AI → FP

0.125***

0.043

2.906

0.023

1.180

0.043

0.211

0.004

Accepted

Note: CI (Confidence intervals);*, **, ***: p < 0.1, p < 0.05, p < 0.01, respectively; ns: non-significant.

Table 8
Model evaluation.
Relationship

R2

Evaluation

Q2 predict

Evaluation

AI
BMI
CE
FP
LS
SCA

0.180
0.040
0.149
0.438
0.073
0.062

Low
Very low
Low
Moderate-substantial
Low
Low

0.076
0.026
0.113
0.079
0.065
0.038

Low
Very low
Moderate
Moderate
Low
Low

firms. This finding aligns with the TOE framework, which suggests that
environmental factors become more critical when firms face resource
constraints. This finding suggests that smaller firms rely more heavily
on external institutional support to overcome resource and capability
constraints when adopting emerging technologies. In contrast, large
firms may possess stronger internal resources and technological capabilities, enabling them to pursue AI adoption with less dependence on
external support.
Finally, the moderating effect of the level of AI adoption on the
BMI–FP relationship is not statistically significant in the full sample.
However, the multi-group analysis reveals a marginally significant
difference between SMEs and large firms. Specifically, the moderating
effect appears stronger among large firms, suggesting that the level of
AI adoption may enhance the firm performance of BMI, primarily in organizations with greater resources and technological capabilities. This
finding indicates potential heterogeneity in how AI-enabled innovation
translates into firm performance across different firm sizes.

Table 9
Comparison of structural model results before and after including control
variables.
Relationship

Before controls

After controls

𝛽

𝑝-value

𝛽

𝑝-value

0.104***
0.395***
0.369***

0.016
0.000
0.000

0.125***
0.417***
0.321***

0.004
0.000
0.000

0.182*
0.067
0.094*
0.211***

0.012
0.184
0.041
0.003

Main effects
AI → FP
BMI → FP
SCA → FP

5.1. Theoretical contributions

Control variables → FP
Firm size
Firm age
Industry type
AI adoption level
R2 (FP)
𝛥R2

0.438

This research advances AI adoption literature in several ways:
First, the study contributes to the AI adoption literature by clarifying
the mechanisms influencing the level of AI adoption within organizations. While prior research has largely examined whether firms adopt
AI technologies, relatively little attention has been given to variations
in the extent and depth of AI implementation among adopting firms.
By conceptualizing AI adoption as a continuum reflecting the level of
AI integration in organizational processes, this study reveals how firms
use AI technologies.
Second, this research extends the TOE framework by identifying
key drivers that influence the level of AI adoption in organizations.
Specifically, the study highlights the roles of top leadership support,
government support, and the cost-effectiveness of AI investment as critical technological, organizational, and environmental factors shaping
the extent of AI adoption. By empirically examining these factors in
the context of AI technologies, the study enriches the application of
the TOE framework in emerging digital technology contexts, especially
in Vietnamese firms.
Third, the study supports Dynamic Capabilities theory by showing
how AI adoption enables BMI and SCA. The findings suggest that higher
levels of AI adoption enhance firms’ ability to identify opportunities, reconfigure resources, and implement innovative business models,
thereby improving firm performance.
Finally, the multi-group analysis reveals that while the mechanisms
linking the level of AI adoption to BMI and SCA are largely consistent across firms of different sizes, the determinants of the level of

0.47
0.032

Note: * (p < 0.1), ** (p < 0.05), *** (p < 0.01).

The moderating effect of the level of AI adoption on the link between BMI and FP was not statistically significant. This finding supports
the assumption that BMI primarily functions as a transformation and
restructuring process [123], serving as an indirect pathway through
which AI generates value rather than as an environmental or strategic
condition that amplifies its direct effect on FP [23]. Prior studies
confirm that AI improves dynamic capabilities, thereby improving competitiveness [124], and BMI represents one of these transformative
outcomes [97,123]. However, the impact of BMI on FP depends largely
on the quality of strategic design rather than the level of AI adoption.
In this context, AI acts as a complementary capability that supports
innovation rather than as a factor that strengthens BMI’s effect on FP.
Importantly, the multi-group analysis reveals that while the mechanisms linking the level of AI adoption to BMI, SCA and FP are broadly
consistent across firm sizes, the drivers of the level of AI adoption
may differ across them. In particular, government support significantly
influences the level of AI adoption among SMEs but not among large
11


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

Table 10
Permutation multigroup analysis (MGA).
Paths

Original
(SMEs)

Original
(Large)

Original
difference

Permutation mean
difference

2.50%

97.50%

Permutation
p value

AI → BMI
AI → FP
AI → SCA
AI × BMI → FP
AI × SCA → FP
BMI → FP
CE → AI
GS → AI
GS → CE
GS → LS
LS → AI
LS → CE
SCA → FP

0.243
0.156
0.246
0.016
0.169
0.388
0.069
0.247
0.319
0.257
0.302
0.17
0.347

0.075
0.098
0.275
0.216
−0.001
0.470
0.201
−0.01
0.235
0.327
0.234
0.192
0.248

0.168
0.058
−0.029
−0.200
0.170
−0.082
−0.131
0.257
0.084
−0.07
0.068
−0.023
0.099

−0.007
−0.008
−0.002
0.006
−0.002
0.003
−0.006
−0.005
−0.010
−0.018
−0.006
0.004
0.001

−0.252
−0.210
−0.232
−0.207
−0.210
−0.190
−0.256
−0.241
−0.237
−0.242
−0.255
−0.218
−0.190

0.242
0.193
0.220
0.208
0.206
0.199
0.249
0.239
0.232
0.243
0.262
0.252
0.210

0.182
0.558
0.815
0.062
0.119
0.424
0.334
0.036
0.508
0.616
0.619
0.857
0.319

6. Conclusion

AI adoption level may vary. In particular, government support plays
a more critical role in facilitating the level of AI adoption among
SMEs than among large firms. These findings enrich the literature by
highlighting the heterogeneous effects of institutional support across
firm sizes during digital transformation.

This study combines the TOE framework and Dynamic Capabilities
theory to understand how organizations adopt AI and turn it into FP.
The study examines how external (government support) and internal
(top leadership support, cost-effectiveness) enablers lead to strategic
outcomes (BMI and SCA) and FP. Government support has a positive
influence on top leadership support, cost-effectiveness and improves the
level of AI adoption, reinforcing the view that government support and
leadership support are core drivers of AI adoption. This underscores
the essential role of the institutional environment in promoting technological adoption, particularly in developing countries. Furthermore,
cost-effectiveness positively affects the level of AI adoption, indicating
that the important roles of government and leadership support are in
effective AI investment.
The results reveal that the level of AI adoption has a significantly
positive effect on BMI, SCA, and FP, confirming the role of AI in
enhancing organizational competitiveness and performance. Both BMI
and SCA have stronger effects on FP than the direct effect of AI adoption
level, indicating that the value of AI is primarily realized indirectly
through business model transformation and the strengthening of competitive positioning. Furthermore, the level of AI adoption moderates
the link between SCA and FP, confirming AI’s role as an amplifier
of existing competitive advantages, strengthening the linkage between
SCA and FP. Finally, the hypothesis regarding the moderating role
of AI adoption level on the link between BMI and FP was rejected,
suggesting that BMI functions as a mediating mechanism through which
AI generates business value.
Although the study is practical, it has several limitations. First, the
investigation was conducted in Vietnam, thus limiting generalizability.
Future studies should consider diverse geographical areas to boost
representativeness. Furthermore, Vietnamese cultural norms of respect
for authority and collectivism may cause managers to overstate their
AI commitment, especially in ‘‘top leadership support’’. Prejudices from
culture and social desirability bias may influence responses. Although
CMB was assessed using full collinearity VIF, the reliance on selfreported data from an only source does not eliminate the risk of bias.
In the future, these studies should use multi-source data collection
(e.g., integrating managerial surveys with employee responses) and
utilize extensive statistical techniques, such as the unmeasured latent
method factor, to further eliminate CMB. Next, cross-sectional techniques involved gathering data at a single period do not allow for the
assessment of dynamic processes as described by Dynamic Capabilities theory. Therefore, the findings of this study cannot demonstrate
processes of ‘‘resource transformation’’ or ‘‘resource reconfiguration’’
over time. Future studies should adopt longitudinal, time-lagged, or
panel data designs to more rigorously examine the dynamic nature
of the relationships proposed by Dynamic Capabilities theory. Finally,
this study conceptualizes SCA in a general strategic sense and does not
explicitly measure environmental performance outcomes. SCA includes

5.2. Practical contributions
This study has significant managerial and policy implications for
firms using AI to improve BMI, SCA, and FP:
First, the results highlight the critical role of top leadership support in driving the effective implementation of AI technologies. Senior
managers should actively champion AI initiatives by allocating strategic
resources, fostering a data-driven culture, and encouraging organizational learning related to AI capabilities. Leadership commitment is
particularly important for overcoming organizational resistance and
ensuring that the level of AI adoption is aligned with long-term strategic
objectives.
Second, the study underscores the importance of evaluating the
cost-effectiveness of AI investments. Firms should carefully assess the
expected benefits of AI technologies relative to their implementation
and operational costs. Developing clear investment strategies, prioritizing high-impact AI applications, and gradually scaling AI initiatives
can help firms maximize the value derived from AI adoption.
Third, the findings demonstrate that government support plays a
significant role in facilitating the level of AI adoption. Managers should
actively leverage government programs such as digital transformation
initiatives, financial incentives, and innovation support schemes to
reduce the barriers associated with AI implementation. Policymakers,
in turn, should continue to develop supportive regulatory frameworks
and targeted support programs that encourage firms to adopt and scale
AI technologies. In addition, the Vietnamese government’s policy on
AI adoption in the public sector by 2030 is a positive step [12]. AI
training and advisory programs should be developed through national
support centers to enhance firms’ implementation capabilities. Investment in AI platforms will help reduce costs. Additionally, financial and
informational assistance should be provided [21].
Fourth, the results suggest that firms should not only adopt AI
technologies but also increase the level of AI integration across organizational processes. A higher level of AI adoption enables firms to
enhance business model innovation and strengthen sustainable competitive advantages. Therefore, managers should focus on embedding
AI capabilities into core business processes such as decision-making,
forecasting, customer engagement, and operational optimization.
Finally, the study shows that a higher level of AI adoption strengthens the ability of firms to translate sustainable competitive advantages
into superior firm performance. Managers should therefore view AI not
merely as a technological tool but as a strategic capability that supports
resource reconfiguration, opportunity recognition, and long-term value
creation.
12


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

Table A.11
Original reliability and validity assessment before removing FP6, SCA1 and SCA6 Outer loadings (𝜒), Cronbach Alpha (𝛼), CR,
AVE.
Construct

𝜒

Firm performance (FP):
FP1
FP2
FP3

FP4

FP5
FP6

Firm performance measured by ROA.
Firm performance measured by ROE.
Firm performance measured by ROS
(percentage of profits over
billing volume).
The firm’s market share in its primary product
and market
segments.
Sales growth in its primary markets and goods.
Our relationship with this supplier has helped
achieve rapid
growth.

SCA2
SCA3

SCA4
SCA5
SCA6

The quality of the products or services our
company provides is
better than that of our competitors.
Our company has better R&D capabilities than
our competitors.
Our company has better management
capabilities than our
competitors.
Our company’s profits are better.
Our company’s corporate image is better than
our competitors.
Competitors can hardly replace our company’s
competitive
advantage

CR

AVE

0.778

0.856

0.547

0.604

0.710

0.464

0.778
0.826
0.815

0.832

0.797
−0.024

Sustainable competitive advantage (SCA)
SCA1

𝛼

−0.42

0.845
0.866

0.795
0.718
0.000

Appendix I. Original reliability and validity assessment before removing FP6, SCA1 and SCA6

economic and environmental dimensions to better understand green
technologies. Environmental outcomes are also affected by mediating practices like green manufacturing and total quality management
(TQM), which the current model ignores. The study by Gul, et al. [125]
indicates that green manufacturing approaches mediate the link between TQM and sustainable development, with environmental strategy
serving as a moderating element. Furthermore, TQM positively affected
corporate social responsibility (CSR) and corporate green performance
(CGP); however, the moderating role of environmental strategy was
not supported in the relationship between CSR and CGP [126]. Future
studies should integrate these variables to clarify how AI is transformed
into sustainable outcomes. Finally, only firms that had already adopted
AI were included in the study. Future research should incorporate
both adopters and non-adopters and model adoption using a binary or
ordinal approach, or employ multi-group analysis, to achieve stronger
causal identification of adoption antecedents.

See Table A.11.
References
[1] D.L. Torre, C. Colapinto, I. Durosini, S. Triberti, Intelligence Collaboration,
Team formation for human-artificial in the workplace: A goal programming
model to foster organizational change, IEEE Trans. Eng. Manage. 70 (5) (2023)
1966–1976, http://dx.doi.org/10.1109/TEM.2021.3077195.
[2] I.M. Cockburn, R. Henderson, S. Stern, The Impact of Artificial Intelligence
on Innovation: An Exploratory Analysis, University of Chicago Press,
2019, pp. 115–148, [Online]. Available: https://www.nber.org/books-andchapters/economics-artificial-intelligence-agenda/impact-artificial-intelligenceinnovation-exploratory-analysis,
[3] Stanford Institute for Human-Centered AI, Artificial Intelligence Index Report
2025, Stanford University, 2025, Available : https://hai.stanford.edu/assets/
files/hai_ai_index_report_2025.pdf.

CRediT authorship contribution statement

[4] OECD AI, Vietnam, national strategy on research and development and application of AI (2021–2030), 2021, Available: https://oecd.ai/en/dashboards/policyinitiatives/national-strategy-on-rd-and-application-of-ai-9280.

Nguyen Thi Phuong Anh: Writing – review & editing, Writing
– original draft, Visualization, Validation, Supervision, Software, Resources, Project administration, Methodology, Investigation, Funding
acquisition, Formal analysis, Data curation, Conceptualization. Bui
Huy Khoi: Writing – original draft, Visualization, Investigation, Funding acquisition, Formal analysis, Conceptualization. Nguyen Quang
Thu: Writing – review & editing, Writing – original draft, Visualization,
Conceptualization. Tran Nha Ghi: Writing – review & editing, Writing
– original draft, Visualization, Validation, Supervision, Software, Resources, Project administration, Methodology, Investigation, Funding
acquisition, Formal analysis, Data curation, Conceptualization.

[5] N.M. Quy, Trí tuệ nhân tạo là cốt lõi của chuyển đổi số (artificial
intelligence is the core of digital transformation), 2022, Available: https:
//nhandan.vn/special/viettel-tri-tue-nhan-tao/index.html.
[6] V. Anh, H. Van, Phát triển và ứng dụng công nghệ trí tuệ nhân
tạo: đòn bẩy thúc đẩy chuyển đổi số quốc gia (development and
adoption of artificial intelligence: A lever for national digital transformation), 2023, Available: https://special.nhandan.vn/tri-tue-nhan-tao-vietnam/index.html. (Accessed April 3 2024).
[7] Cục thương mại điện tử và kinh tế số (department of E-commerce and
digital economy), in: Lợi ích ứng dụng trí tuệ nhân tạo cho doanh nghiệp
thương mại điện tử (Benefits of Artificial Intelligence Adoption for ECommerce Firms), 2024, Available: https://vnshort.com/T6ZX. (Accessed 3
April 2024).
[8] Jeong I., J. Jeong, Driving creativity in the AI-enhanced workplace: roles
of self-efficacy and transformational leadership, Curr. Psychol. 44 (9) (2025)
8001–8014, http://dx.doi.org/10.1007/s12144-024-07135-6.

Declaration of competing interest
This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. The authors
declare no conflicts of interest related to this work.

[9] J.-H. Wu, S.-C. Wang, L.-M. Lin, Mobile computing acceptance factors in the
healthcare industry: A structural equation model, Int. J. Med. Inform. 76 (1)
(2007) 66–77, http://dx.doi.org/10.1016/j.ijmedinf.2006.06.006.
13


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

[10] S. Walczak, Artificial neural networks and other AI applications for business
management decision support, Int. J. Sociotechnol.Knowl. Dev. 8 (4) (2016)
1–20, http://dx.doi.org/10.4018/ijskd.2016100101.
[11] H. Chen, L. Li, Y. Chen, Explore success factors that impact artificial intelligence
adoption on telecom industry in China, J. Manag. Anal. 8 (1) (2021) 36–68,
http://dx.doi.org/10.1080/23270012.2020.1852895.
[12] N.V. Phuoc, The critical factors impacting artificial intelligence applications
adoption in Vietnam: A structural equation modeling analysis, Economies 10
(6) (2022) 1–16, http://dx.doi.org/10.3390/economies10060129.
[13] S. Gupta, W. Ghardallou, D.K. Pandey, G.P. Sahu, Artificial intelligence
adoption in the insurance industry: Evidence using the technology–
organization–environment framework, Res. Int. Bus. Financ. 63 (2022) 101757,
http://dx.doi.org/10.1016/j.ribaf.2022.101757.
[14] A. Bettoni, D. Matteri, E. Montini, B. Gładysz, E. Carpanzano, An AI adoption
model for SMEs: a conceptual framework, IFAC-PapersOnLine 54 (1) (2021)
702–708, http://dx.doi.org/10.1016/j.ifacol.2021.08.082.
[15] K. Ragazou, I. Passas, A. Garefalakis, C. Zopounidis, Business intelligence model
empowering SMEs to make better decisions and enhance their competitive
advantage, Discov. Anal. 1 (1) (2023) 2, http://dx.doi.org/10.1007/s44257022-00002-3.
[16] Q. Wu, D. Yan, M. Umair, Assessing the role of competitive intelligence and
practices of dynamic capabilities in business accommodation of SMEs, Econ.
Anal. Policy 77 (2023) 1103–1114, http://dx.doi.org/10.1016/j.eap.2022.11.
024.
[17] S. Lada, B. Chekima, M.R.A. Karim, N.F. Fabeil, M.S. Ayub, S.M. Amirul,
R. Ansar, M. Bouteraa, L.M. Fook, H.O. Zaki, Determining factors related to
artificial intelligence (AI) adoption among Malaysia’s small and medium-sized
businesses, J. Open Innov.: Technol. Mark. Complex. 9 (4) (2023) 100144,
http://dx.doi.org/10.1016/j.joitmc.2023.100144.
[18] P. Mikalef, K. Lemmer, C. Schaefer, M. Ylinen, S.O. Fjørtoft, H.Y. Torvatn, M.
Gupta, B. Niehaves, Enabling AI capabilities in government agencies: A study of
determinants for European municipalities, Gov. Inf. Q. 39 (4) (2022) 101596,
http://dx.doi.org/10.1016/j.giq.2021.101596.
[19] M. Ghobakhloo, Determinants of information and digital technology implementation for smart manufacturing, Int. J. Prod. Res. 58 (8) (2020) 2384–2405,
http://dx.doi.org/10.1080/00207543.2019.1630775.
[20] P. Pham, H. Zhang, W. Gao, X. Zhu, Determinants and performance outcomes
of artificial intelligence adoption: Evidence from U.S. hospitals, J. Bus. Res. 172
(2024) 114402, http://dx.doi.org/10.1016/j.jbusres.2023.114402.
[21] F. Faiz, V. Le, E.K. Masli, Determinants of digital technology adoption in
innovative SMEs, J. Innov. Knowl. 9 (4) (2024) 100610, http://dx.doi.org/10.
1016/j.jik.2024.100610.
[22] M.A. Hossain, R. Agnihotri, M.R.I. Rushan, M.S. Rahman, S.F. Sumi, Marketing
analytics capability, artificial intelligence adoption, and firms’ competitive
advantage: Evidence from the manufacturing industry, Ind. Mark. Manag. 106
(2022) 240–255, http://dx.doi.org/10.1016/j.indmarman.2022.08.017.
[23] S. Sahoo, S. Kumar, N. Donthu, A.K. Singh, Artificial intelligence capabilities, open innovation, and business performance – empirical insights from
multinational B2B companies, Ind. Mark. Manag. 117 (2024) 28–41, http:
//dx.doi.org/10.1016/j.indmarman.2023.12.008.
[24] H.D.X. Trieu, P.V. Nguyen, D. Vrontis, The interplay of IT adoption, government
support and firm performance: mediating roles of innovation and resilience in
Vietnamese SMEs, J. Asia Bus. Stud. 19 (4) (2025) 935–953, http://dx.doi.org/
10.1108/JABS-12-2024-0690.
[25] J. Eveland, L.G. Tornatzky, Technological innovation as a process, in: The
Processes of Technological Innovation: Lexington Books, 1990, pp. 27–50,
[Online]. Available: https://www.researchgate.net/publication/291824703_
Technological_Innovation_as_a_Process.
[26] R. Turner, Diffusion of innovations, J. Minim. Invasive Gynecol. 14 (6) (2007)
776, http://dx.doi.org/10.1016/j.jmig.2007.07.001.
[27] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of
information technology, MIS Q. 13 (3) (1989) 319–340, http://dx.doi.org/10.
2307/249008.
[28] V. Venkatesh, M.G. Morris, G.B. Davis, F.D. Davis, User acceptance of information technology: Toward a unified view, MIS Q. 27 (3) (2003) 425–478,
http://dx.doi.org/10.2307/30036540.
[29] D. Gursoy, O.H. Chi, L. Lu, R. Nunkoo, Consumers acceptance of artificially
intelligent (AI) device use in service delivery, Int. J. Inf. Manage. 49 (2019)
157–169, http://dx.doi.org/10.1016/j.ijinfomgt.2019.03.008.
[30] S. Alsheiabni, Y. Cheung, C. Messom, Factors inhibiting the adoption of artificial
intelligence at organizational-level: A preliminary investigation, presented at the
Americas Conference on Information Systems, vol. 2019, 2019, Available: https:
//aisel.aisnet.org/amcis2019/adoption_diffusion_IT/adoption_diffusion_IT/2/.
[31] L. Pumplun, C. Tauchert, M. Heidt, A new organizational chassis for artificial
intelligence-exploring organizational readiness factors, presented at the proceedings of the 27th European conference on information systems (ECIS), 2019,
Available: https://aisel.aisnet.org/ecis2019_rp/106/.
[32] K. Nam, C.S. Dutt, P. Chathoth, A. Daghfous, M.S. Khan, The adoption of artificial intelligence and robotics in the hotel industry: prospects and challenges,
Electronic Markets 31 (3) (2021) 553–574, http://dx.doi.org/10.1007/s12525020-00442-3.

[33] K. Mahroof, A human-centric perspective exploring the readiness towards smart
warehousing: The case of a large retail distribution warehouse, Int. J. Inf.
Manage. 45 (2019) 176–190, http://dx.doi.org/10.1016/j.ijinfomgt.2018.11.
008.
[34] D. Hradecky, J. Kennell, W. Cai, R. Davidson, Organizational readiness to
adopt artificial intelligence in the exhibition sector in western europe, Int.
J. Inf. Manage. 65 (2022) 102497, http://dx.doi.org/10.1016/j.ijinfomgt.2022.
102497.
[35] R. van de Wetering, P. Mikalef, D. Dennehy, Artificial intelligence ambidexterity, adaptive transformation capability, and their impact on performance under
tumultuous times, presented at the the role of digital technologies in shaping the
post-pandemic world, cham, 2022, Available: http://dx.doi.org/10.1007/978-3031-15342-6_3.
[36] O.M. Horani, A.S. Al-Adwan, H. Yaseen, H. Hmoud, W.M. Al-Rahmi, A.
Alkhalifah, The critical determinants impacting artificial intelligence adoption
at the organizational level, Inf. Dev. (2023) 1055–1079, http://dx.doi.org/10.
1177/02666669231166889.
[37] A.M. Baabdullah, A.A. Alalwan, E.L. Slade, R. Raman, K.F. Khatatneh, SMEs
and artificial intelligence (AI): Antecedents and consequences of AI-based B2B
practices, Ind. Mark. Manag. 98 (2021) 255–270, http://dx.doi.org/10.1016/j.
indmarman.2021.09.003.
[38] X. Zhang, Y. Xu, L. Ma, Research on successful factors and influencing
mechanism of the digital transformation in SMEs, Sustainability 14 (5) (2022)
http://dx.doi.org/10.3390/su14052549.
[39] G. Zhang, T. Wang, Y. Wang, S. Zhang, W. Lin, Z. Dou, H. Du, Study on the
influencing factors of digital transformation of construction enterprises from the
perspective of dual effects—A hybrid approach based on PLS-SEM and fsQCA,
Sustainability 15 (7) (2023) http://dx.doi.org/10.3390/su15076317.
[40] M. Aboelmaged, Predicting e-readiness at firm-level: An analysis of technological, organizational and environmental (TOE) effects on e-maintenance
readiness in manufacturing firms, Int. J. Inf. Manage. 34 (2014) 639–651,
http://dx.doi.org/10.1016/j.ijinfomgt.2014.05.002.
[41] D. Zhang, L.G. Pee, L. Cui, Artificial intelligence in E-commerce fulfillment:
A case study of resource orchestration at Alibaba’s smart warehouse, Int. J.
Inf. Manage. 57 (2021) 102304, http://dx.doi.org/10.1016/j.ijinfomgt.2020.
102304.
[42] S. Mustafa, Y. Long, S. Rana, Role of domestic renewable energy plants in
combating energy deficiency in developing countries, End-User Perspect. Energy
Rep. 11 (2024) 692–705, http://dx.doi.org/10.1016/j.egyr.2023.04.370.
[43] D.J. Teece, G. Pisano, A. Shuen, Dynamic capabilities and strategic
management, Strat. Manag. J. 18 (7) (1997) 509–533.
[44] D.J. Teece, Explicating dynamic capabilities: the nature and microfoundations
of (sustainable) enterprise performance, Strat. Manag. J. 28 (13) (2007)
1319–1350, http://dx.doi.org/10.1002/smj.640.
[45] J. Zhang, Y. Chen, Q. Li, Y. Li, A review of dynamic capabilities evolution—
based on organisational routines, entrepreneurship and improvisational capabilities perspectives, J. Bus. Res. 168 (2023) 114214, http://dx.doi.org/10.1016/
j.jbusres.2023.114214.
[46] S. Alsheibani, Y. Cheung, C.H. Messom, Artificial intelligence adoption: AIreadiness at firm-level, presented at the PACIS, 2018, Available: https://aisel.
aisnet.org/pacis2018/.
[47] R. Pillai B. Sivathanu, Adoption of artificial intelligence (AI) for talent acquisition in IT/ITeS organizations, Benchmarking: Int. J. 27 (9) (2020) 2599–2629,
http://dx.doi.org/10.1108/BIJ-04-2020-0186.
[48] H.-Y. Hsu, F.H. Liu, H.-T. Tsou, L.-J. Chen, Openness of technology adoption,
top management support and service innovation: a social innovation perspective, J. Bus. Ind. Mark. 34 (3) (2018) 575–590, http://dx.doi.org/10.1108/
JBIM-03-2017-0068.
[49] J. Jöhnk, M. Weißert, K. Wyrtki, Ready.or. Not, AI comes— an interview study
of organizational AI readiness factors, Bus. Inf. Syst. Eng. 63 (1) (2021) 5–20,
http://dx.doi.org/10.1007/s12599-020-00676-7.
[50] M. Ghobakhloo, T.S. Hong, M.S. Sabouri, N. Zulkifli, Strategies for Successful Information Technology Adoption in Small and Medium-sized Enterprises, vol. 3, (1) 2012, pp. 36–67, https://www.semanticscholar.org/reader/
87f4c047d6e3028d8903a75f80c85da6ce3218c4.
[51] P. Mikalef, K. Conboy, J. Krogstie, Artificial intelligence as an enabler of
B2B marketing: A dynamic capabilities micro-foundations approach, Ind. Mark.
Manag. 98 (2021) 80–92, http://dx.doi.org/10.1016/j.indmarman.2021.08.003.
[52] A.A. Abonamah N. Abdelhamid, Managerial insights for AI/ML implementation:
a playbook for successful organizational integration, Discov. Artif. Intell. 4 (1)
(2024) 22, http://dx.doi.org/10.1007/s44163-023-00100-5.
[53] M. Dora, A. Kumar, S. Mangla, A. Pant, Muhammad, M. Kamal, M. Kamal,
Critical success factors influencing artificial intelligence adoption in food supply
chains, Int. J. Prod. Res. 60 (14) (2021) 4621–4640, http://dx.doi.org/10.1080/
00207543.2021.1959665.
[54] Y. Pan, F. Froese, N. Liu, H. Yunyang, M. Ye, The adoption of artificial
intelligence in employee recruitment: The influence of contextual factors,
Int. J. Hum. Resour. Manag. 33 (6) (2021) 1–23, http://dx.doi.org/10.1080/
09585192.2021.1879206.
14


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

[55] S. Kergroach, SMEs going digital: policy challenges and recommendations,
OECD Publishing2021, Available: https://www.oecd.org/en/publications/smesgoing-digital_c91088a4-en.html.
[56] I.M. Enholm, E. Papagiannidis, P. Mikalef, J. Krogstie, Artificial intelligence
and business value: a literature review, Inf. Syst. Front. 24 (2021) 1709–1734,
http://dx.doi.org/10.1007/s10796-021-10186-w.
[57] V. Kumar, S. Kumar, P. Durana, R. Chaudhuri, D. Vrontis, S. Chatterjee,
Enhancing organizational readiness for generative AI integration: an empirical
investigation, Int. J. Organ. Anal. (2025) http://dx.doi.org/10.1108/K-07-20242002.
[58] Romeo J., E. Lacko, Adoption and integration of AI in organizations: a systematic review of challenges and drivers towards future directions of research,
Kybernetes 55 (3) (2025) 1286–1307, http://dx.doi.org/10.1108/K-07-20242002.
[59] Q. Liu, J. Xia, Government technology support, digital finance development and
corporate innovation performance, China Account. Financ. Rev. 27 (3) (2025)
397–420, http://dx.doi.org/10.1108/CAFR-06-2024-0085.
[60] N. Haefner, J. Wincent, V. Parida, O. Gassmann, Artificial intelligence and
innovation management: A review, framework, and research agenda, Technol. Forecast. Soc. Change 162 (2021) 120392, http://dx.doi.org/10.1016/j.
techfore.2020.120392.
[61] P. Jorzik, A. Yigit, D. Kanbach, S. Kraus, M. Dabic, Artificial intelligenceenabled business model innovation: Competencies and roles of top management,
IEEE Trans. Eng. Manage. 71 (2024) 7044–7056, http://dx.doi.org/10.1109/
TEM.2023.3275643.
[62] A.A. Khanfar, R. Kiani Mavi, M. Iranmanesh, D. Gengatharen, Factors influencing the adoption of artificial intelligence systems: a systematic literature review,
Manag. Decis. 63 (10) (2025) 3727–3755, http://dx.doi.org/10.1108/MD-052023-0838.
[63] A.P. Rodriguez Müller, L. Tangi, A. Lerusse, Understanding the Adoption of
Artificial Intelligence in Local Government Decision-Making: The Influence
of Institutional Pressures and Managerial Perceptions, Public Administration.
http://dx.doi.org/10.1111/padm.70033.
[64] F.T.S. Chan A., Y.-L. Chong, Determinants of mobile supply chain management
system diffusion: a structural equation analysis of manufacturing firms, Int.
J. Prod. Res. 51 (4) (2013) 1196–1213, http://dx.doi.org/10.1080/00207543.
2012.693961.
[65] Y. Song, X. Qiu, J. Liu, The Impact of Artificial Intelligence Adoption on
Organizational Decision-Making: An Empirical Study Based on the Technology
Acceptance Model in Business Management, vol. 13, (8) 2025, p. 683, http:
//dx.doi.org/10.3390/systems13080683.
[66] M. Ren, Why technology adoption succeeds or fails: an exploration from the
perspective of intra-organizational legitimacy, J. Chin. Sociol. 6 (1) (2019) 21,
http://dx.doi.org/10.1186/s40711-019-0109-x.
[67] B. Puklavec, T. Oliveira, A. Popovič, Understanding the determinants of business
intelligence system adoption stages: An empirical study of SMEs, Ind. Manag.
Data Syst. 118 (2017) 00, http://dx.doi.org/10.1108/IMDS-05-2017-0170.
[68] T.H. Davenport, The AI advantage: How to put the artificial intelligence
revolution to work: Mit press, 2018, [Online]. Available: http://dx.doi.org/10.
7551/mitpress/11781.001.0001.
[69] S. Yang, P. Jin, Does AI adoption in financial management enhance corporate
risk resilience? IEEE Access 13 (2025) 66211–66227, http://dx.doi.org/10.
1109/ACCESS.2025.3560397.
[70] S. Chen, J. Tajdini, A moderated model of artificial intelligence adoption in
firms and its effects on their performance, Inf. Technol. Manag. 26 (3) (2025)
407–419, http://dx.doi.org/10.1007/s10799-024-00422-5.
[71] D. Sjödin, V. Parida, M. Kohtamäki, J. Wincent, An agile co-creation process
for digital servitization: A micro-service innovation approach, J. Bus. Res. 112
(2020) 478–491, http://dx.doi.org/10.1016/j.jbusres.2020.01.009.
[72] M. Kohtamäki, V. Parida, P. Oghazi, H. Gebauer, T. Baines, Digital servitization
business models in ecosystems: A theory of the firm, J. Bus. Res. 104 (2019)
380–392, http://dx.doi.org/10.1016/j.jbusres.2019.06.027.
[73] V. Parida, D. Sjödin, W. Reim, Reviewing literature on digitalization, business
model innovation, and sustainable industry: Past achievements and future
promises, Sustainability 11 (2) (2019) http://dx.doi.org/10.3390/su11020391.
[74] H. Paiola, M. Gebauer, Internet of things technologies, digital servitization and
business model innovation in BB manufacturing firms, Ind. Mark. Manag. 89
(2020) 245–264, http://dx.doi.org/10.1016/j.indmarman.2020.03.009.
[75] H. Heimberger, D. Horvat, F. Schultmann, Exploring the factors driving AI
adoption in production: a systematic literature review and future research
agenda, Inf. Technol. Manag. 27 (1) (2026) 53–69, http://dx.doi.org/10.1007/
s10799-024-00436-z.
[76] A. Heider, M. Gerken, N. van Dinther, M. Hülsbeck, Business model innovation
through dynamic capabilities in small and medium enterprises – evidence from
the german mittelstand, J. Bus. Res. 130 (2021) 635–645, http://dx.doi.org/
10.1016/j.jbusres.2020.04.051.
[77] R.D. Galliers, D.E. Leidner, B. Simeonova, Strategic information management:
Theory and practice: Routledge, 2020, [Online]. Available: http://dx.doi.org/
10.4324/9780429286797.

[78] A.N. Awamleh, F.T. Bustami, Examine the mediating role of the information
technology capabilities on the relationship between artificial intelligence and
competitive advantage during the COVID-19 pandemic, Sage Open 12 (3)
(2022) 21582440221119478, http://dx.doi.org/10.1177/21582440221119478.
[79] C. Giachino, M. Cepel, E. Truant, A. Bargoni, Artificial intelligence-driven
decision making and firm performance: a quantitative approach, Manag. Decis.
63 (10) (2024) 3454–3476, http://dx.doi.org/10.1108/MD-10-2023-1966.
[80] S. Shahidi Hamedani, S. Aslam, S. Shahidi Hamedani, AI in business operations:
driving urban growth and societal sustainability, Front. Artif. Intell. 8 (2025)
(2025) http://dx.doi.org/10.3389/frai.2025.1568210.
[81] P.S.S. Moosa, S. Pundhir, AI-responsive agile leadership and sustainable organizational outcomes in AI-integrated environments, Glob. J. Flex. Syst. Manag.
(2026) http://dx.doi.org/10.1007/s40171-026-00489-9.
[82] R. van de Wetering, Artificial intelligence as an enabler of dynamic capabilities:
A ‘sense–shape–shift’ perspective on digital transformation during disruption,
presented at the pervasive digital services for People’s well-being, in: Inclusion
and Sustainable Development, Cham, 2026, Available: http://dx.doi.org/10.
1007/978-3-032-06164-5_18.
[83] A. Sánchez-Rodríguez, G. García-Vidal, Y. Fernández-Ochoa, R. Martínez-Vivar,
A.E. Gavilanes-Venegas, R. Pérez-Campdesuñer, Navigating uncertainty through
AI adoption: Dynamic capabilities, strategic innovation performance, and competitiveness in ecuadorian SMEs, Adm. Sci. 15 (12) (2025) 468, http://dx.doi.
org/10.3390/admsci15120468.
[84] C. Amit, R. Zott, Creating value through business model innovation, MIT Sloan
Manag. Rev. (2012) Available: https://sloanreview.mit.edu/article/creatingvalue-through-business-model-innovation/.
[85] T. Foss, N.J. Saebi, Fifteen years of research on business model innovation:
How far have we come, and where should we go? J. Manag. 43 (1) (2016)
200–227, http://dx.doi.org/10.1177/0149206316675927.
[86] R. Zott, C. Amit, Business Model Design and the Performance of Entrepreneurial
Firms, vol. 18, (2) 2007, pp. 181–199, http://dx.doi.org/10.1287/orsc.1060.
0232.
[87] T. Clauss, Measuring business model innovation: conceptualization, scale development, and proof of performance, R & D Manage. 47 (3) (2017) 385–403,
http://dx.doi.org/10.1111/radm.12186.
[88] Z. Wei, X. Song, D. Wang, Manufacturing flexibility, business model design, and
firm performance, Int. J. Prod. Econ. 193 (2017) 87–97, http://dx.doi.org/10.
1016/j.ijpe.2017.07.004.
[89] I. Visnjic, F. Wiengarten, A. Neely, Only the brave: Product innovation, service
business model innovation, and their impact on performance, J. Prod. Innov.
Manage. 33 (1) (2016) 36–52, http://dx.doi.org/10.1111/jpim.12254.
[90] M.-A. Latifi, S. Nikou, H. Bouwman, Business model innovation and firm
performance: Exploring causal mechanisms in SMEs, Technovation 107 (2021)
102274, http://dx.doi.org/10.1016/j.technovation.2021.102274.
[91] E. Moradi, S.M. Jafari, Z.M. Doorbash, A. Mirzaei, Impact of organizational
inertia on business model innovation, open innovation and corporate performance, Asia Pac. Manag. Rev. 26 (4) (2021) 171–179, http://dx.doi.org/10.
1016/j.apmrv.2021.01.003.
[92] J. Barney, Firm Resources and Sustained Competitive Advantage, vol. 17, (1)
1991, pp. 99–120, http://dx.doi.org/10.1177/014920639101700108.
[93] I. Belyamani, M.F.B. Mfarrej, S.Z. Ahmad, A.R. Abu Bakar, Pathways linking
green digital transformation to sustainable development through knowledge
sharing and dynamic capabilities, Discov. Sustain. 6 (1) (2025) 1183, http:
//dx.doi.org/10.1007/s43621-025-02075-y.
[94] J. h. Kim, B. i. Seok, H. j. Choi, S. h. Jung, J. p. Yu, Sustainable management
activities: A study on the relations between technology commercialization
capabilities, Sustain. Compét. Advant. Bus. Perform. Sustain. 12 (19) (2020)
7913, http://dx.doi.org/10.3390/su12197913.
[95] D.K. Kanbach, L. Heiduk, G. Blueher, M. Schreiter, A. Lahmann, The genai is out
of the bottle: generative artificial intelligence from a business model innovation
perspective, Rev. Manag. Sci. 18 (4) (2024) 1189–1220, http://dx.doi.org/10.
1007/s11846-023-00696-z.
[96] Y. Zhang, X. Ma, J. Pang, H. Xing, J. Wang, The impact of digital transformation
of manufacturing on corporate performance — The mediating effect of business
model innovation and the moderating effect of innovation capability, Res. Int.
Bus. Financ. 64 (2023) 101890, http://dx.doi.org/10.1016/j.ribaf.2023.101890.
[97] D.R. Metzler, N. Neuss, J. Muntermann, Artificial intelligence and business
model innovation in incumbent firms a cross-industry case study, Die Unternehm. 75 (3) (2021) 324–339, http://dx.doi.org/10.5771/0042-059X-20213-324.
[98] A. Cimino, V. Corvello, C. Troise, A. Thomas, M. Tani, Artificial Intelligence
Adoption for Sustainable Growth in SMEs: An Extended Dynamic Capability
Framework, vol. 32, (5) 2025, pp. 6120–6138, http://dx.doi.org/10.1002/csr.
70019.
[99] D. De Fano, R. Schena, A. Russo, Harnessing AI ambidexterity for competitive
advantage: the role of dynamic capabilities in digital innovation ecosystems,
Eur. J. Innov. Manag. (2025) 1–15, http://dx.doi.org/10.1108/EJIM-11-20241404.
[100] N. Drydakis, Artificial intelligence and reduced smes’ business risks. a dynamic
capabilities analysis during the COVID-19 pandemic, Inf. Syst. Front. 24 (4)
(2022) 1223–1247, http://dx.doi.org/10.1007/s10796-022-10249-6.
15


N.T.P. Anh, B.H. Khoi, N.Q. Thu et al.

Green Technologies and Sustainability 4 (2026) 100384

[101] M.S. Rahman, M.A. Hossain, F.A.M. Abdel Fattah, Does marketing analytics
capability boost firms’ competitive marketing performance in data-rich business
environment? J. Enterp. Inf. Manag. 35 (2) (2022) 455–480, http://dx.doi.org/
10.1108/JEIM-05-2020-0185.
[102] K. Jamil, W. Zhang, A. Anwar, S. Mustafa, Exploring the influence of AI
adoption and technological readiness on sustainable performance in Pakistani
export sector manufacturing small and medium-sized enterprises, Sustainability
17 (8) (2025) 3599, http://dx.doi.org/10.3390/su17083599.
[103] Armstrong T.S., J.S. Overton, Estimating nonresponse bias in mail surveys, J.
Mark. Res. 14 (3) (1977) 396–402, http://dx.doi.org/10.2307/3150783.
[104] C.-H. Chang, The influence of corporate environmental ethics on competitive
advantage: The mediation role of green innovation, J. Bus. Ethics 104 (3)
(2011) 361–370, http://dx.doi.org/10.1007/s10551-011-0914-x.
[105] Y.T. Tran, T.H.P. Chau, Q.T. Pham, Transformational leadership and firm
performance: The mediating roles of innovation capacity and management
accounting systems usage, Sustain. Futur. 10 (2025) 100988, http://dx.doi.org/
10.1016/j.sftr.2025.100988.
[106] V.J. García-Morales, F.J. Lloréns-Montes, A.J. Verdú-Jover, The Effects of Transformational Leadership on Organizational Performance through Knowledge and
Innovation, vol. 19, (4) 2008, pp. 299–319, http://dx.doi.org/10.1111/j.14678551.2007.00547.x.
[107] J. Hair, J. Risher, M. Sarstedt, C. Ringle, When to use and how to report the
results of PLS-SEM, Eur. Bus. Rev. 31 (2022) http://dx.doi.org/10.1108/EBR11-2018-0203.
[108] M. Sarstedt, C.M. Ringle, J.F. Hair, Partial Least Squares Structural Equation
Modeling, Springer Nature Switzerland, Cham, 2020, pp. 1–56, [Online].
Available:http://dx.doi.org/10.1007/978-3-319-05542-8_15-3,
[109] J. Nunnally I. Bernstein, The assessment of reliability, 1994, pp. 248–292, [Online]. Available: https://not-equal.org/References/Reference27-Nunnally1994.
pdf.
[110] D.F. Fornell, C. Larcker, Evaluating structural equation models with unobservable variables and measurement error, J. Mark. Res. 18 (1) (1981) 39–50,
http://dx.doi.org/10.2307/3151312.
[111] J. Henseler, C.M. Ringle, M. Sarstedt, A new criterion for assessing discriminant
validity in variance-based structural equation modeling, J. Acad. Mark. Sci. 43
(1) (2015) 115–135, http://dx.doi.org/10.1007/s11747-014-0403-8.
[112] J. Cohen, Statistical Power Analysis for the Behavioral Sciences, Routledge,
2013, [Online]. Available: http://dx.doi.org/10.4324/9780203771587.
[113] G. Chin, W. Marcoulides, The partial least squares approach to structural
equation modeling, 1998, [Online]. Available: https://www.taylorfrancis.
com/chapters/edit/10.4324/9781410604385-10/partial-least-squares-approachstructural-equation-modeling-wynne-chin.
[114] N. Kock, Common method bias in PLS-SEM, Int. J. E-Collaboration 11 (2015)
1–10, http://dx.doi.org/10.4018/ijec.2015100101.

[115] P.M. Hu, L.T. Bentler, Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives, Struct. Equ.
Model.: A Multidiscip. J. 6 (1) (1999) 1–55, http://dx.doi.org/10.1080/
10705519909540118.
[116] W.W. Chin, The Partial Least Squares Approach for Structural Equation
Modeling, Lawrence Erlbaum Associates Publishers, Mahwah, NJ, US,
1998, [Online]. Available: https://www.taylorfrancis.com/chapters/edit/10.
4324/9781410604385-10/partial-least-squares-approach-structural-equationmodeling-wynne-chin.
[117] S. Sharma, G. Singh, N. Islam, A. Dhir, Why do SMEs adopt artificial
intelligence-based chatbots? IEEE Trans. Eng. Manage. 71 (2024) 1773–1786,
http://dx.doi.org/10.1109/TEM.2022.3203469.
[118] O. Neumann, K. Guirguis, R. Steiner, Exploring artificial intelligence adoption
in public organizations: a comparative case study, Public Manag. Rev. 26 (1)
(2024) 114–141, http://dx.doi.org/10.1080/14719037.2022.2048685.
[119] M. Mohiuddin, M.N.H. Reza, S. Jayashree, M.S. Al-Azad, S. Ed-dafali, The role
of governments in driving industry 4.0 adoption in emerging countries, J. Glob.
Inf. Manage. 31 (1) (2023) http://dx.doi.org/10.4018/JGIM.323439.
[120] S. Mustafa, Y. Long, S. Rana, The role of corporate social responsibility and
government incentives in installing industrial wastewater treatment plants:
SEM-ANN deep learning approach, Sci. Rep. 13 (1) (2023) 16529, http://dx.
doi.org/10.1038/s41598-023-37239-1.
[121] S.-L. Wamba-Taguimdje, S. Fosso Wamba, K.K. Jean Robert, C.E. Tchatchouang,
Influence of artificial intelligence (AI) on firm performance: The business value
of AI-based transformation projects, Bus. Process. Manag. J. 26 (7) (2020)
1893–1924, http://dx.doi.org/10.1108/BPMJ-10-2019-0411.
[122] Y.S. Lee, T. Kim, S. Choi, W. Kim, When does AI pay off? AI-adoption intensity,
Complement. Investments, R D Strat. Technovation 118 (2022) 102590, http:
//dx.doi.org/10.1016/j.technovation.2022.102590.
[123] T. Burström, V. Parida, T. Lahti, J. Wincent, AI-enabled business-model innovation and transformation in industrial ecosystems: A framework, model and
outline for further research, J. Bus. Res. 127 (2021) 85–95, http://dx.doi.org/
10.1016/j.jbusres.2021.01.016.
[124] K. Bley, S.F.B. Fredriksen, M.E. Skjærvik, I.O. Pappas, The Role of Organizational Culture on Artificial Intelligence Capabilities and Organizational
Performance, Presented At the the Role of Digital Technologies in Shaping the
Post-PandEmic World, Cham, 2022, Available: http://dx.doi.org/10.1007/9783-031-15342-6_2.
[125] R.F. Gul, K. Jamil, S. Mustafa, N.R. Jaffri, A. Anwar, Mitigating the environmental concerns through total quality management and green manufacturing
practices, Environ. Sci. Pollut. Res. 31 (27) (2024) 39285–39302, http://dx.
doi.org/10.1007/s11356-024-33826-5.
[126] R.F. Gul, K. Jamil, S. Mustafa, N.R. Jaffri, A. Anwar, F.H. Awan, Studying the
green performance under the lens of total quality management in Chinese SMEs,
Environ. Dev. Sustain. 26 (9) (2024) 22975–22996, http://dx.doi.org/10.1007/
s10668-023-03586-2.

16


