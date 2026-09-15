---
title: "Backfiring AI? AI Deployment in Workplace"
authors: ["Di Yuan", "Manmohan Aseri", "Narayan Ramasubbu"]
affiliations: ["Harbert College of Business, Auburn University", "Robert H. Smith School of Business, University of Maryland", "Joseph M. Katz Graduate School of Business, University of Pittsburgh"]
venue: "SSRN working paper (id 6103949)"
url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6103949"
date_published: 2026-01-01
attachment: backfiring-ai-ai-deployment-in-workplace.pdf
fulltext_source: pdf-converted
converter: "pdftotext -layout"
notes: |
  Acquired 2026-09-15 from a PDF the user placed in raw/articles/ as `ssrn-6103949.pdf`.
  **Routing corrected at Process time**: a working paper — moved to raw/papers/.
  49 pages; `pdftotext -layout`. **Analytical paper — the body is dense with LaTeX-set
  mathematics that pdftotext flattens badly**: subscripts, superscripts, fractions and Greek
  symbols lose structure, so propositions and proofs are legible in outline but NOT reliable
  for reproducing the formal model. Read the PDF for any equation you intend to cite.
  No date is printed on the PDF cover; `date_published` is a placeholder pending confirmation
  from the SSRN record.
---

Backfiring AI? AI Deployment in Workplace
 Di Yuana , Manmohan Aserib , Narayan Ramasubbuc
 a
 Harbert College of Business, Auburn University, diy0002@auburn.edu
 b
 Robert H. Smith School of Business, University of Maryland, maseri@umd.edu
 c
 Joseph M. Katz Graduate School of Business, University of Pittsburgh, narayanr@pitt.edu

 Seeking value from artificial intelligence (AI) technologies, firms are rapidly deploying them to augment
 employees and improve business performance. The diffusion of AI into a firm’s business processes affords
 the tracking of task actions performed by high-performing employees and the codification of best practices
 into recommendation systems and training programs. The rising trend in AI deployment reveals managers’
 expectations that AI-facilitated knowledge transfer would elevate overall firm performance. However, deploying
 AI in a workplace has the potential to change the competitive dynamics among employees. The AI system
 can learn from high-performing employees and make that knowledge available to others. In a competitive
 environment, this can disincentivize high-performing employees and ultimately backfire, leading to a decline
 in overall firm productivity. In this paper, we study this problem of employee incentive issues when deploying
 AI in a competitive workplace, using a game-theoretic model.

 Our results show that when employees compete using both tangible (“hard”) and intangible (“soft”) skills,
 firm policies that favor AI-facilitated knowledge transfer and task outcome-based compensation may lower
 firm performance. We illustrate that payoffs from AI deployments depend on workforce heterogeneity, reliance
 on tangible skills, the skill-disparity between employees, and AI efficacy. Using our model, we develop policy
 recommendations for maximizing the return on organizational AI deployments. Our results suggest that some
 ostensibly simple solutions, like guaranteeing or increasing the wages of adversely affected employees, may
 not solve the problem effectively, and firms would have to judiciously choose optimal AI efficacy levels for
 achieving better outcomes.

 Key words : AI Deployment, AI in Competitive Workplace, Knowledge Transfer

1. Introduction
Artificial Intelligence (AI) technologies are increasingly augmenting human workers in various tasks
(e.g., Zolas et al. 2020, Brynjolfsson et al. 2025, Kanazawa et al. 2025, Sun et al. 2025, Wang et al.
2025, Yang et al. 2025). Modern AI systems are designed to accomplish task automation using both
symbolic and data-driven software models (Brynjolfsson and Mitchell 2017, Garnelo and Shanahan
2019). Symbolic models use rule-based, logical, and deductive instructions to precisely describe tasks’
information-processing structure. They can automate well-defined and repetitive task components,
such as generating and posting invoices, payroll processing, and job scheduling. In contrast, data-
driven models utilize statistical and machine learning algorithms for estimating outputs with inputs

 1

---

2 Incentive Issues in AI Deployment

when tasks lack precise information-processing structures, such as making a medical diagnosis based
on various health data (Levy 2018). Recent advancements facilitate the combination of symbolic and
data-driven models as well as the automatic and continuous improvement of performance utilizing
large volumes of real-world data, which increases the generative affordances of AI systems and their
applications to a broader array of tasks (Mitchener et al. 2022). Increasingly, such AI systems are
considered general-purpose technology that positively contributes to business performance improve-
ments, innovation, and firm value (Furman and Seamans 2019, Eloundou et al. 2023, Eisfeldt et al.
2023).

 Firm-level investments in AI have experienced explosive growth, and a wide variety of occupa-
tions have been identified as having significant exposure to AI (Felten et al. 2018, Webb 2020,
Felten et al. 2021). This has spurred discussions about the potential impact of AI on employees
and their productivity (e.g., Autor 2015, Brynjolfsson et al. 2018, Acemoglu and Restrepo 2019,
Frank et al. 2019, Brynjolfsson et al. 2025). Similar to any other general-purpose technology, AI-
induced automation may substitute labor, and market analysts have indeed predicted that about
15% of the global workforce, or about 400 million workers in roles such as financial advisors, medical
transcriptionists, legal assistants, and customer service representatives may be potentially impacted
(McKinsey Global Institute 2018). At the same time, AI adoption is also expected to enhance labor
productivity in a variety of ways, including freeing up employees from monotonous and repetitive
task components, speeding up information processing, and providing decision support for avoiding
type 1 and type 2 errors (Agrawal et al. 2019, Rai et al. 2019, Brynjolfsson et al. 2025). AI systems,
especially those with explainable predictions and generative capabilities, have been reported to help
employees enhance their learning, decision making, quality management, and overall productivity
(Senoner et al. 2021, Mele et al. 2022, Noy and Zhang 2023).

 Amidst this background, we raise the issue of whether the deployment of AI in firms would induce
differential effects on the incentives and performance of employees in a heterogeneous workforce. Prior
literature suggests that when organizations cannot precisely define and monitor requisite employee
behaviors, outcome-based and pay-for-performance (PFP) compensation schemes perform better
than fixed compensation schemes (Lazear 2000, Cadsby et al. 2007, Lazear 2018, He et al. 2021).
Indeed, PFP is the dominant form of compensation scheme across industry sectors in the U.S., with
more than 80% of the firms utilizing PFP schemes (Gerhart and Fang 2014, Groysberg et al. 2021).

 The impacts of PFP, however, are also contingent on other organizational and individual factors,
such as competition, peer performance, and risk aversion (Stroh et al. 1996, Chan et al. 2014,
Rubel and Prasad 2016, Abernethy et al. 2020). Since the deployment of AI can have profound
impacts on the operating environment of organizations and the task environments of employees, it

---

 Incentive Issues in AI Deployment 3

is not clear if extant PFP schemes would offer the same level of economic incentive for employees
to boost their performance in the presence of AI. For instance, AI systems deployed at a firm can
track and observe the tangible, task-related actions of high-performing employees and codify these
practices in organizational memory, which may then be utilized for training other employees. While
such AI-induced transfer of know-how would benefit low-skilled employees, it may also increase
the competition for performance-based rewards and dampen the incentives offered by PFP. Other
factors, such as the workforce composition, ability gaps between employees, and the efficacy of AI-
induced knowledge transfer, are also likely to influence the payoffs from AI deployment. In this
context, we raise the research question of whether and how AI deployments in organizations that
have instituted PFP schemes would improve overall employee and organizational performance. We
answer the question by analytically modeling the deployment of AI in a PFP regime, and we describe
the conditions under which AI deployments would be beneficial and harmful.

2. Model Setup
We build a game-theoretic model to understand the impact of AI deployment in an organizational
PFP environment. In this setup, a firm deploying AI is able to observe its employees’ task activities
and utilize data for assessment of task performances. Such data is also used to continuously train and
refine the AI system. Since the AI system learns from employees’ activities and makes this knowledge
available to all employees, it acts as a conduit for knowledge transfer between employees. We posit
that the presence of such an AI-facilitated conduit for knowledge transfer, which does not require
deliberate or extra efforts from employees, is likely to alter employee perceptions of incentives in a
PFP regime. For example, some “star” employees may perceive that their skills no longer yield a
relative advantage over peers because their idiosyncratic task actions can simply be imitated even if
other employees do not fully understand the underlying rationale of the task actions. Such a threat of
task imitation, thus, can demotivate high-performing employees. This dynamic mirrors a real-world
scenario often seen in professional service industries. For example, in firms with performance-based
compensations, such as those for financial advisors or customer-facing sales and service representa-
tives, a star employee might feel disincentivized if an AI system can codify and distribute their best
sales techniques, thereby eroding their competitive edge and the value of their unique expertise. In
contrast, employees who benefit from the AI-facilitated knowledge transfer may be motivated to fur-
ther boost their contribution. Therefore, AI deployment can potentially affect employees’ incentives
and behaviors in a PFP environment, which can be consequential to the overall firm performance.
We examine these dynamics by considering the firm’s workforce composition, employee skill levels,
and the efficacy of the AI system, and assess the overall performance consequences of AI deployment
in PFP regimes.

---

4 Incentive Issues in AI Deployment

 Employees: In our model, there are two types of skills that an employee needs to accomplish
daily operational tasks: (i) tangible skills and (ii) intangible skills. An example of a tangible skill is
knowing when to solicit a customer through email (and when not to). For instance, for an employee
in a sales function, it may be a bad idea to solicit customer leads through email on Friday afternoons
because the response rates are typically lower at that time. Similarly, a more advanced tangible
skill would be to create a personalized “check-in” message rather than multi-channel campaigns to
court dormant clients who haven’t made a purchase in a long time but have a history of high-value
transactions. In the context of our paper, the defining characteristic of a tangible skill is that the
AI system can detect features of the skill from task-level activity data generated by employees and
learn from it. Tools that learn from employee behaviors are already widely implemented across a
range of business functions. For instance, in its warehouses, Amazon utilizes wearable devices and
AI-powered systems to track employee movements and identify the most productive task completion
patterns (Solon 2018). Similarly, Uber leverages driver feedback, trip data, and app activity to
pinpoint the effective habits of its high-performing drivers (Verma 2024). In the sales function, firms
using Salesforce’s Einstein AI, can analyze historical successes to recommend optimal sales tactics
and follow-up strategies (Srivastava 2023). For improving workflow, tools like Microsoft Viva Insights
analyze employee communications across all channels, including emails, meetings, and instant chats
to recommend the most effective coordination patterns (see Microsoft 2025). Beyond these examples,
a growing number of organizations are now using employee data to train AI models for various
human resources functions, such as recruitment, training and development, and talent management
(Gartner 2024).

 In contrast to those trackable employee activities, we define intangible skills as those that an
AI system would not be able to codify and learn from because they lack clear, specifiable, and
measurable features. For example, in customer-facing roles, an employee’s ability to upsell at the
right moment, appease angry customers, or tactfully decline an unwarranted merchandise return are
skills that, while discernible to humans, are often too nuanced for an AI system to explicitly codify.
These tasks involve imprecise information structures and rely on the tacit knowledge of employees,
which often eludes accurate detection by AI. We note that AI technologies are rapidly advancing,
and the current gap in AI’s ability in discovering tangible and intangible task activities is poised to
decrease. Nevertheless, current AI deployments lack the affordances of general artificial intelligence,
and there is a persistent gap in AI’s ability to detect and leverage data related to tangible and
intangible employee skills (Fjelland 2020, Heaven 2020). For simplicity of notations, we use subscripts
‘t’ and ‘i ’ to denote the tangible and intangible skills, respectively.

 To incorporate variance in workforce abilities, we consider two levels of abilities, high and low,
for both the tangible and intangible skills. The high-type tangible skill is denoted by aHt , and the

---

 Incentive Issues in AI Deployment 5

low-type tangible skill is denoted by aLt . Similarly, the high-type intangible skill is denoted by aHi ,
and the low-type intangible skill is denoted by aLi . We assume that a pt proportion of employees
have high-type tangible skills. Thus, a 1 − pt proportion of employees have low-type tangible skills.
Similarly, a pi proportion of employees have high-type intangible skills, and a 1 − pi proportion of
employees have low-type intangible skills. We assume that tangible skill levels and intangible skill
levels are independent. That is, the probability for a worker to possess high intangible skill is always
pi regardless of her tangible skill level. The total number of employees in our paper is normalized to
1. Thus, there are four types of employees in a firm’s workforce, as listed in Table 1 (and pictorially
depicted in Figure 1).

 Table 1 Employees
 Type
 Ability level Proportion
 (Tangible, Intangible)
 HH (aHt , aHi ) pHH = pt pi
 H L
 HL (at , ai ) pHL = pt (1 − pi )
 L H
 LH (at , ai ) pLH = (1 − pt )pi
 L L
 LL (at , ai ) pLL = (1 − pt )(1 − pi )

Figure 1 Illustration of four employee types by skill levels.

 Firm’s Reward Policy: Consistent with industry practice in a PFP regime, we model that the
employees are paid at a salary rate per unit output. Thus, the total salary earned by an employee

---

6 Incentive Issues in AI Deployment

is the salary rate multiplied by the total output of the employee. In PFP regimes, firms typically
use a multi-tiered salary model with built-in incentives to reward high performance (i.e., bonus or
promotion for top performers). We introduce a similar setup into our model with two reward levels:
base salary-rate γ and bonus salary-rate γB , where γB > γ. We use γ for the general notation to
represent the salary rate. Thus,
 (
 γ, base salary-rate,
 γ= , γB > γ. (1)
 γB , bonus salary-rate for promoted employees,
 In our model, we assume that when the firm decides to promote an employee of a particular
type, it will promote all the employees of that type because they all have identical performance.
For example, if an employee of the HL type is promoted, then all the employees of the HL type
will be promoted. Thus, the firm’s decision is to determine which employee groups to promote for
bonus considerations. For simplicity, we assume that the firm promotes the top two employee groups.
We also assume that the firm cannot directly observe employee types, and therefore, the promotion
decision – which type(s) of employees must receive the bonus salary rate – is based only on observed
task outcomes. This assumption is consistent with the studies in the PFP literature (Lazear 2000,
2018). In the base case, we model the salary rates as exogenously given and unchanged after AI
deployment. Later, we endogenize the firm’s decision of salary rates in Section 6.1.

 Employees’ Decisions & Utilities: Each employee devotes two types of input into a task
activity, tangible skill input and intangible skill input. The tangible type input is denoted by wt ,
and the intangible type input is denoted by wi . Each type of employee decides how much input to
expend of each type. Employees’ utility function has two components, benefit and cost. The benefit
is determined by the final total output and the firm’s reward policy. We assume that the final total
output is a weighted sum of labor inputs based on the intangible and tangible skills of employees.
Let o denote the final output from an individual employee. Then, we have o = βt wt + βi wi for each
employee’s output, where βt and βi are the relative importance of tangible and intangible skills in
production. We also introduce O to represent the total output of all the employees.
 2
 We assume that an employee with tangible ability at incurs watt cost to produce wt amount of
tangible input. That is, to produce the same level of input, the employee with higher ability would
 w2
incur a lower cost. Similarly, an employee with intangible ability ai incurs aii cost to produce wi
amount of intangible input. Thus, the net utility of an employee with abilities (at , ai ), is
  2
 wt wi2
 
 u(at , ai ) = γ (βt wt + βi wi ) − + , (2)
 at ai
where γ is given in (1).

 Employees are strategic players who choose the optimal labor levels (i.e., wt and wi ) that maximize
their net utility. We solve for a symmetric equilibrium where employees of the same type make the

---

 Incentive Issues in AI Deployment 7

same decision. This is a commonly used assumption in settings where there are a large number of
strategic players (see Iyer and Katona 2016, Hassin and Roet-Green 2020).

 AI-Assisted Abilities: AI can observe employees’ actions through data collection and then
provide suggestions to employees on how to complete tasks with improved efficiency. It enables
automatic knowledge-sharing and learning processes in daily business operations. We make a few
assumptions about the learning process. First, the knowledge transfer via AI happens only for the
tangible skills (i.e., explicit knowledge) and from high-type employees to low-type ones. With the
help of AI, employees with low tangible skills could improve their natural ability (aLt ). We define the
new ability level with an AI assistant as effective ability (denoted by aLte ). Second, the effectiveness
of AI, denoted by f ∈ (0, 1), decides the learning rate at which employees with low skill levels could
improve their tangible abilities. Specifically, we model the effective ability aLte as a function of the
AI effectiveness rate, f , and the original ability levels:

 aLte = aLt + f (aHt − aLt ). (3)

Note that a perfect AI (i.e., when f = 1) will serve to equalize the ability of all employees with respect
to their tangible skills. That is, when f = 1, we have aLte = aHt . Similarly, a completely ineffective AI
(i.e., when f = 0) will have no knowledge transfer effect, and the ability of a low-type worker will
not change due to AI deployment. That is, we have aLte = aLt , when f = 0.

 Firm: The firm’s revenue comes from the final output produced by its employees. The cost of the
firm is the salary paid to these employees. Thus, the firm’s profit can be written as
 X
 1 − γ k ok pk , k ∈ {HH, HL, LH, LL},
 
 π= (4)
 k

where ok and pk are the output and the proportion of employee type k, and γ k is the reward received
by the employee type k. All notations are summarized in Table 2.

 Our analysis assumes that employees are able to accurately assess their own skill type and are also
aware of the organizational environment (i.e., know the other parameters considered in our stylized
model, such as the composition of the workforce and the ability levels of peers). Employees are also
aware of the firm’s AI deployment and its potential for knowledge transfer. The firm knows the
proportion of different types of employees it has hired, but it doesn’t directly observe which employees
utilize which type of skills for accomplishing tasks, and employee rewards are solely determined on
the basis of task output.

---

8 Incentive Issues in AI Deployment

 Table 2 Notations
 Notation Description
 L
 at Low (L) tangible (t) ability level.
 H
 at High (H) tangible (t) ability level.
 L
 ai Low (L) intangible (i) ability level.
 H
 ai High (H) intangible (i) ability level.
 L
 ate Effective ability level of employees with low tangible skills, after AI deployment.
 pt The proportion of employees with high tangible abilities.
 pi The proportion of employees with high intangible abilities.
 wt Employee’s labor decision of tangible skill input.
 wi Employee’s labor decision of intangible skill input.
 βt Weightage of tangible input in the final output.
 βi Weightage of intangible input in the final output.
 k
 o Final output from labor of an employee in type k, for k ∈ {HH, HL, LH, LL}.
 O The total production output (or the productivity level).
 k
 u Net utility of an employee in type k, for k ∈ {HH, HL, LH, LL}.
 γ The base salary rate.
 γB Bonus salary-rate, γB > γ.
 f The efficacy of AI, 0 ≤ f ≤ 1.
 πnoAI Firm’s profit in the absence of AI.
 πAI Firm’s profit in the presence of AI.

 Firm Decides:
 Stage 1
 Wage Policy and AI Deployment

 Before AI After AI
 Deployment Deployment

 Employees Employees
 Stage 2 Decide: Output Decide: Output
 Levels Levels

 𝐻𝐻 𝐻𝐿 𝐿𝐻 𝐿𝐿 𝐻𝐻 𝐻𝐿 𝐿𝐻 𝐿𝐿
 Payoffs: {𝜋𝑛𝑜 𝐴𝐼 , 𝑢𝑛𝑜 𝐴𝐼 , 𝑢𝑛𝑜 𝐴𝐼 , 𝑢𝑛𝑜 𝐴𝐼 , 𝑢𝑛𝑜 𝐴𝐼 } Payoffs: {𝜋𝐴𝐼 , 𝑢𝐴𝐼 , 𝑢𝐴𝐼 , 𝑢𝐴𝐼 , 𝑢𝐴𝐼 }

Figure 2 The sequence of events. In stage 1, the firm sets the wage policy and chooses whether to deploy AI.
 Then, in stage 2, employee decide their output levels.

---

 Incentive Issues in AI Deployment 9

3. Analyses & Results

We now analyze the model and examine overall firm performance before and after the deployment
of AI, and assess the impact of AI on the welfare of different stakeholders. The game has two stages,
Figure 2 illustrates these two stages.

Stage 1: The firm first announces its base and bonus salary-rates and the criteria to get the bonus.
Then, the firm chooses whether to deploy AI or not.

Stage 2: For given values of salary rates, bonus criteria, and the firm’s AI deployment decision, the
employees produce their output. To determine the optimal output levels, employees need to know
the salary rate they will receive (γ or γB ). However, the salary rate depends on the output ranking
of all employees, because only the top two employee groups get the bonus salary rate γB . Note the
circular dependency here: the output of an employee depends on output rank (via salary rate), and
the output rank (and consequently, salary rate) depends on the outputs of all employees. To obtain
the equilibrium output of employees in this context, we employ the notion of rational expectations
equilibrium (REE), a concept commonly used to model such circular dependencies.

Rational Expectations Equilibrium: In the rational expectations equilibrium, the employees
“rationally” anticipate the rank order of their output and the corresponding salary rate. With this
expectation about the rank order, all employees produce their outputs, and eventually, an output
ranking is realized in equilibrium. Under the REE framework, employees’ output ranking in equilib-
rium matches their expectations (hence, “rational” expectations). The REE concept originated in
modeling macroeconomic quantities such as inflation, for instance in the seminal work of Lucas Jr
(1972). In the case of modeling inflation, consumers make consumption decisions based on their
expectations of future inflation, while inflation itself is influenced by aggregate consumption levels.
Consequently, consumers form expectations about inflation in a rational manner and choose their
consumption accordingly. In equilibrium, the realized rate of inflation matches the rate that con-
sumers had rationally anticipated. More recently, the REE framework has been used to analyze
technology-induced behaviors and their consequences. For example, in the model proposed by Aseri
et al. (2020), a user’s decision to engage with a website (e.g., a social media platform) depends on the
perceived value of the website. However, the value of the website is itself a function of the number
of active users engaging with it. In this context, each user anticipates how valuable the website will
be based on their expectations about how many other users will use it, and makes their engagement
decision accordingly. In equilibrium, the realized value of the website would match what users had
rationally anticipated. Similarly, Acemoglu et al. (2022) use the REE framework for examining a
market with data intermediaries where firm decisions both affect and are affected by information
aggregation.

---

10 Incentive Issues in AI Deployment

 In stage 2, each employee knows their own skill types and input weights (βi and βt ), and the
announced salary scheme. They form rational expectations about their ranking in equilibrium. Hence,
we can obtain the equilibrium outputs of all employees using the REE framework. We then obtain
the firm’s profit corresponding to the employee outputs. We repeat this process for both with and
without AI deployment, and then compare the firm’s profit under those two scenarios. Having
derived the impact of AI deployment through the solution in stage 2, we then solve for stage 1 to
analyze firm strategies for mitigating the potential adverse effects of AI deployment. We describe
and analyze those potential remedies in Section 4. Specifically, we analyze how the firm can alter
employee incentives (i.e., remuneration) or strategically choose the AI efficacy level for maximizing
the benefits of AI deployment. When we solve for the firm’s problem in stage 1, the firm knows the
distribution of employee types (HH, HL, LH, LL) and their input weights (βi and βt ). With this
knowledge, the firm anticipates employees’ equilibrium output responses under REE to obtain its
profit under different AI strategies.

3.1. Model Solution

Each employee decides the labor inputs based on their ability level and the expected salary. Because
employees are heterogeneous in their abilities, naturally, their performance also varies. Under the
two-tier reward policy, the ranking of employees’ output levels determines the salary rate that
each employee type receives. To solve for the rational expectations equilibrium, we first solve the
employees’ problem for the case when the firm offers only one salary rate, γ (no bonus rate). This
analysis will reveal how the employee output will be ranked if the firm doesn’t offer a bonus. Building
on this analysis, we will then proceed to the case when the firm offers a bonus salary to the top two
employee groups.

 We now obtain employees’ decisions of labor inputs (wt and wi ). An individual employee’s net
utility is the total salary minus the cost of working. Thus, an employee with an endowed natural
ability, (at , ai ), and a salary rate, γ, will get the net utility of
  2
 wt wi2
 
 u = max γ (βt wt + βi wi ) − + , (5)
 wt ,wi at ai
where, at ∈ {aHt , aLt , aLte }, ai ∈ {aHi , aLi } and γ ∈ {γ, γB }.

 Solving the optimization problem of an employee in (5), we obtain the following results:

Lemma 1 The employees’ optimal choices of labor, equilibrium final output, and net utility are
 1 1 1 2
 wt∗ = βt at γ, wi∗ = βi ai γ, u∗ = βt at + βi2 ai γ 2 .
 
 2 2 4
 ∗ ∗ ∗ 1 2 2
 
 o = βt wt + βi wi = β at + βi ai γ.
 2 t

---

 Incentive Issues in AI Deployment 11

 In later sections, we refer to values from Lemma 1 as employees’ “natural” equilibrium decisions
and output, because this is what employees will produce when all employees are paid the same salary.

 3.1.1. Prior to AI: In Lemma 1, we can see that the natural output (o∗ ) increases with
both ability levels (i.e., at and ai ). Thus, it is straightforward to see that the HH type is always
the top-performing employee group, while the LL type has the lowest output level. Note that we
assume the firm would only promote members of the top two performing employee groups (out of
four). The uncertainty in the ranking of employee output lies with the HL and LH types: which
type of employees can deliver the second-highest output? Comparing the outputs of HL and LH,
we find that the output of HL is higher than LH when (aHt − aLt )βt2 > (aHi − aLi )βi2 , where the HL
employees’ advantage in tangible skills (i.e., the left-hand side of the inequality) can fully make up
for their lower level of intangible skills. An example of a production environment in a firm that
satisfies this condition is an engineering task where the tangible skills of an employee may play a
more important role in achieving higher task performance. For instance, engineers and programmers
with strong technical design and coding abilities (“hard” skills) may be highly valued even if their
general communication skills are below par. In contrast, when the advantage in intangible (or “soft”)
skills is more important, i.e., when (aHt − aLt )βt2 ≤ (aHi − aLi )βi2 , the LH type would take the second
place in performance ranking. An example of such a situation could be in business development,
where the ability to court and persuade new customers or resolve customer grievances may be highly
valued even if the employee lacks strong technical skills, for instance, in examining and analyzing
data. In this paper, we focus on the production environment where the HL type employees produce
a higher level of “natural” output, which happens when (aHt − aLt )βt2 > (aHi − aLi )βi2 . Thus, we assume
that

 (aHt − aLt )βt2 > (aHi − aLi )βi2 . (6)

From this point onward, all analyses will proceed under the above assumption.

 When the firm introduces the reward policy of promoting the top two groups of employees with
a bonus rate, γB (where γB > γ), the HH and HL types will receive the bonus if they continue
to produce their natural output (i.e., the output when everybody is paid the same salary rate).
However, the competition will intensify as the bonus rate incentivizes the lower-ranking LH type
employees to increase their output to surpass the HL type. It makes sense for the LH type to do so
because if they advance themselves to the second rank, the net utility could be larger than the utility
when they settle for the third position. Under the same incentives, the HL employees also raise their
effort to defend their rank. Employees can improve their overall ranking by producing more output.
All employees would produce more output at the bonus salary rate. However, no employee would

---

12 Incentive Issues in AI Deployment

produce so much output at the bonus salary rate that their net utility is lower than their net utility
with a lower salary rate. To obtain the equilibrium output of different employee groups under a
reward policy with a bonus, we first obtain the maximum possible output produced by an employee.
To this end, we solve the following optimization problem for the maximum possible output under
the two-tier salary rates.

 o = max βt wt + βi wi
 wt ,wi

 wt2 wi2
  
 1 2
 βt at + βi2 ai γ 2
 
 s.t. γB (βt wt + βi wi ) − + ≥
 at ai 4
 The output of the above problem represents the maximum output an employee with abili-
ties (at , ai ) will produce in order to get the bonus salary rate. The constraint in the above opti-
mization problem ensures that the net utility of the employee at the bonus salary rate (γB ) is higher
than the net utility at the base salary rate (γ). Otherwise, there is no benefit of aiming for the bonus
salary rate.

 Solving the above optimization problem, we have the following result:

Lemma 2 The highest possible output from an employee with ability level (at , ai ) is
 1 2  q 
 o∗max = βt at + βi2 ai γB + γB2 − γ 2 .
 2
 From the results in Lemma 1 and 2, we have all possible production outputs for each employee type
summarized in Table 3. We use subscripts and superscripts to denote output from a specific employee
type at a specific salary rate. For example, oHH
 γ is the natural output from an HH employee under
salary rate γ, and oLH
 max is the maximum output from an LH type employee. Under the assumption

in (6), the outputs in the second and third columns of Table 3 are in decreasing order.

 Table 3 Employees’ output under different salary rates
 Type
 Natural output at rate γ Maximum output
 (Tangible, Intangible)
 
 = 12 (βt2 aHt + βi2 aHi ) γ 1 2 H 2 H
 p 2
 HH oHH
 γ oHH
 max = 2 (βt at + βi ai ) γB + γB − γ 2
 1 2 H 2 L 1 2 H 2 L
 p 2 
 HL oHL
 γ = 2 (βt at + βi ai ) γ oHL
 max = 2 (βt at + βi ai ) γB + γB − γ 2
 1 2 L 2 H 1 2 L 2 H
 p 2 
 LH oLH
 γ = 2 (βt at + βi ai ) γ oLH
 max = 2 (βt at + βi ai ) γB + γB − γ 2
 1 2 L 2 L 1 2 L 2 L
 p 2 
 LL oLL
 γ = 2 (βt at + βi ai ) γ oLL
 max = 2 (βt at + βi ai ) γB + γB − γ 2

 We now need to find out each employee’s labor effort decisions at equilibrium. Recalling the
REE framework discussed earlier, each employee forms expectations about their relative rank, and
this ranking determines their bonus eligibility. The main challenge in equilibrium arises in ranking

---

 Incentive Issues in AI Deployment 13

the HL and LH types. Although employees can, in principle, choose any output level, two levels
are particularly relevant: producing at their natural output level or exerting effort to reach their
maximum output level. We assume that the LH type’s maximum output exceeds an HL employee’s
natural output at the bonus salary rate γB (i.e., oLH HL
 max > oγ ), which threatens HL’s position as
 B

the second-highest performer. To secure the bonus, the HL type must therefore produce at the
LH’s maximum output level, oLH
 max , deterring LH employees from attempting to overtake them.

Importantly, the LH employees do not need to actually produce at this maximum level—the threat
of being able to do so is sufficient to induce HL employees to match it. As a result, in equilibrium,
HH, LH, and LL employees produce at their natural output levels, while HL employees exert higher
effort to maintain their second-place rank.

 The condition for competition for bonus to exist (i.e., oLH HL
 max > oγ ) can be rearranged into
 B

 βt2 aLt + βi2 aHi
 γB > p γ,
 (βt2 aLt + βi2 aHi ) [βt2 (2aLt − aHt ) + βi2 (2aHi − aLi )]
indicating that there should be a sufficient difference between γB and γ. Under this scenario, we can
write the firm’s profit. Let πnoAI and πAI represent the firm’s profit before and after AI. Substituting
the output values from Table 3 into the firm’s profit equation (4), we get
 p 
 (1 − γB ) γB 2 H 2 H
 (1 − γB ) γB + γB2 − γ 2
 βt2 aLt + βi2 aHi pt (1 − pi )
  
 πnoAI = βt at + βi ai pt pi +
 2  2 (7)
 1−γ γ  2 L
 βt at + βi2 aHi (1 − pt )pi + βt2 aLt + βi2 aLi (1 − pt )(1 − pi ) .
   
 +
 2
 We now proceed to the analysis in the presence of AI.

 3.1.2. Post AI: with the AI system, employees with low tangible skills improve their ability
to aLte = aLt + f (aHt − aLt ) as given in equation (3). With the enhanced ability in tangible skills, the
ranking of employees’ output can differ from the case prior to the AI deployment. We focus on the
most interesting scenario where LH can outperform HL with the help of AI, as portrayed in Figure
3. That is, the natural output from LH is higher than the natural output from HL in an AI-assisted
environment, this happens when (aHt − aLt )(1 − f )βt2 < (aHi − aLi )βi2 . Thus, we assume that

 (aHt − aLt )(1 − f )βt2 < (aHi − aLi )βi2 . (8)

Note that the corresponding inequality in the before-AI case, i.e., inequality (6), can also be written
 (a −a )β 2
 H L
as (aiH −aiL )βi2 ≤ 1. Thus, the above inequality, along with the inequality in (6), are true together when
 t t t

 f > fˆ, (9)

where
 H L 2
 (a − ai )βi
 fˆ = 1 − iH . (10)
 (at − aLt )βt2

---

14 Incentive Issues in AI Deployment

Note that under the assumption of (6), we have fˆ > 0. Thus, when the efficiency of AI is very high,
it can change the natural output ranking of employees.

 The competition for the second place follows a similar logic that LH employees need to devote
extra effort to ensure the HL type employees stay in the third place. Hence, we have the post-AI
output ranking in Table 4.

Figure 3 Employee ranking Before AI vs. After AI: AI helps LH type employees overtake HL type employees.

 Table 4 Employees’ optimal decisions - prior to & after AI deployment
 Before AI After AI
 Type
 Ranking Output Ranking Output
 1 1
 HH 1 2
 (βt2 aHt + βi2 aHi ) γB 1 2
 (βt2 aHt + βi2 aHi ) γB
 1
  1
 (βt2 aLt + βi2 aHi ) (βt2 aHt + βi2 aLi ) γ
 p 2
 HL 2 2
 γB + γB − γ 2 3 2
 1 1
 
 (βt2 aLt + βi2 aHi ) γ (βt2 aHt + βi2 aLi )
 p 2
 LH 3 2
 2 2
 γB + γB − γ 2
 1 1
 LL 4 2
 (βt2 aLt + βi2 aLi ) γ 4 2
 (βt2 aLte + βi2 aLi ) γ

 Substituting the output values from Table 4 into the firm’s profit equation in 4, we get
 p 2 
 (1 − γB ) γB 2 H (1 − γ B ) γ B + γ B
 − γ 2
 βt at + βi2 aHi pt pi + βt2 aHt + βi2 aLi (1 − pt )pi
  
 πAI =
 2  2 (11)
 1−γ γ  2 H 2 L
  2 L 2 L
  
 + βt at + βi ai pt (1 − pi ) + βt ate + βi ai (1 − pt )(1 − pi ) .
 2
 To assess the impact of AI, we now compare the observed performances during the periods before
and after AI deployment.

3.2. Impact on Firm’s Output and Profit

To obtain the impact of AI on the firm’s output and profit, we first understand AI’s impact on
output and profit from each employee type. Then, we will aggregate this to understand the overall
impact on the firm.

---

 Incentive Issues in AI Deployment 15

Impact on Output of Employee Groups: Using the notations for equilibrium output levels
specified in Table 3, we have the total output as:

 OnoAI = oHH
 γ
 pHH + oLH LH LL
 max pHL + oγ pLH + oγ pLL .
 B

 OAI = oHH
 γ
 pHH + oHL
 B
 HL LL
 max pLH + oγ pHL + oγ pLL . AI

 Let ∆oXY represent the change in output of employee type (X, Y ), X, Y ∈ {L, H }, defined as the
post-AI output minus the prior-to-AI output. By comparing the production output of each employee
type in Table 4, we get the following:

 ∆oHH = 0,
 ∆oHL = oHL
 γ
 − oLH
 max ,
 | {z }
 Competition Effect

 ∆o LH
 = oHL
 max − oγ ,
 LH

    
 = oHLmax − o LH
 γ
 + o LH
 γ
 AI
 − o LH
 γ
 AI
 ,
 | {z } | {z }
 Competition Effect Learning Effect

 ∆o LL
 = o LLAI
 γ
 −o .
 LL
 γ
 | {z }
 Learning Effect

From the above breakdown of output, we observe the following: (i) productivity of the HH type
is not affected by AI deployment, because AI doesn’t increase their abilities. Since they have high
tangible and high intangible abilities, they continue to stay at the top of the output ranking. Thus,
their salary rate remains unchanged, and they don’t have any incentive to increase their output.
Therefore, they continue to produce the same level of output. (ii) AI has a direct and an indirect
impact on the productivity of employees. AI’s direct impact on productivity is through boosting the
abilities related to the tangible skills of the LH and LL types (we refer to this as the “learning effect”
of AI). (iii) AI also has an indirect impact on productivity as a result of the change in employees’
performance ranking (we refer to this as the “competition effect” of AI): This competition effect is
negative on HL type, and they produce less because they are pushed down to the third place and
don’t receive the bonus salary. This is because, in the presence of AI, HL’s high tangible skills are
not advantageous, because AI facilitates the transfer of knowledge stemming from tangible skills
to all employee groups. However, LH’s high intangible skills yield competitive advantages, because
such skills are harder for AI to learn and transfer. Thus, the output ranking of HL goes down, and
that of LH goes up. Therefore, in contrast to HL, the competitive effect is positive on the LH type
employees. Thus, apart from their increased productivity due to ability improvement (via “learning
effect”), LH employees are further incentivized by the bonus rate after AI deployment due to the
improvement in their output ranking. Formally, we note the AI’s impact on the output of different
employee types as follows:

---

16 Incentive Issues in AI Deployment

Proposition 1 After AI deployment, the output from the HL type employees decreases, and the
output of LH and LL employees increases. The output of HH remains the same after AI deployment.

 To illustrate the practical implications of the above proposition, we utilize the context of software
development. The integration of AI tools in the software development context presents a potential
shift in the value of different skill sets. Based on our proposition, the impact of AI on employee
output is not uniform and highlights a potential reversal of traditional hiring priorities. Employees
with high technical skills but low interpersonal skills (HL type) may find their traditional compet-
itive advantage eroding. The very technical tasks that once defined their value—like writing code,
debugging errors, or performing data queries—can now be learned by AI. As a result, the output
they once generated independently can be produced more efficiently using an AI assistant, such
as GitHub Co-Pilot, by employees with low technical skills but high people skills (LH type). This
shift and the ability to bridge the gap between technical teams and end-users becomes a critical,
non-automatable skill, making the LH type employees a highly sought-after talent pool.

Impact on Profit from Employee Groups: We now analyze the AI’s impact on the profit of the
 XY XY
firm. We define ∆π XY = πAI − πnoAI as the change in profit contributed by an individual employee of
type (X, Y ), with X, Y ∈ {L, H }. We compare the expression of πnoAI and πAI from equations (7)
and (11) and break down the total profit change by employee types and get the following:
 ∆π HH =0,

 ∆π HL = (1 − γ)oHL
 γ
 − (1 − γB )oLH
 max ,
 | {z }
 Competition Effect

 ∆π LH =(1 − γB )oHL
 max − (1 − γ)oγ
 LH

     (12)
 = (1 − γB )oHLmax − (1 − γ)oγ
 LHAI
 + (1 − γ) oLHγ
 − oLH
 AI
 γ
 ,
 | {z } | {z }
 Competition Effect Learning Effect
  
 ∆π = (1 − γ) oγ − oγ .
 LL LL AI LL

 | {z }
 Learning Effect

 It is easy to see that the profit from HH has no impact from AI, because the output and salary of
this employee group remain unchanged after the AI deployment. Similarly, it is also easy to see that
the profit from LL type employees increases, because their output increases, but the salary remains
the same. Thus, the firm gets more output from these employees at the same salary. However, the
direction of impact on the firm’s profit from HL and LH is not clear, because the output of HL
decreases, but the firm has to pay a lower salary rate too. Similarly, the output of LH, increases,
but the firm also has to pay a bonus salary. In Figure 4, we illustrate how AI affects the output of
HL and LH employees differently. The color represents the change in profit contribution after AI
(i.e., πAI − πnoAI ). The green color means that the profit attributed to an employee type increased

---

 Incentive Issues in AI Deployment 17

after AI, and the red color represents a decrease in the profit after AI. We can see that the profit
from HL type employees decreases after AI, and the profit from LH type employees increases after
AI.

 πAI -πnoAI

 -0.0060 -0.0036 -0.0012 0.0012 0.0036 0.0060

Figure 4 The color represents the change in profit after AI (i.e., πAI − πnoAI ). The green color means that the
 profit increased after AI from that employee type. The profit from HL type employees decreases after
 AI, and the profit from LH type employees increases after AI.

Impact on Firm’s Output and Profit: Combining the analyses of individual employees’ output
and profit contribution, we now compare the total output and profit for the firm.
 HH HL HL HH
 (o −oγ )pHL −(o −oγ )pLH
 Define K1 = γB + γB2 − γ 2 , M1 = 1 − γ, M2 = 1 − γB , â(o) = 2 maxβ 2 (K p +γp max
 p
 +f γp )
 ,
 t 1 HL LH LL
 HH HL HL HH
 (o) ∆oLH pLH +∆oLL pLL (M2 omax −M1 oγ )pHL −(M2 omax −M1 oγ )pLH (π) ∆π LH pLH +∆π LL pLL
 (π)
p̂HL = ∆oHL
 , â = 2 βt2 (M2 K1 pHL +M1 γpLH +M1 f γpLL )
 , p̂HL = ∆π HL
 ,
 (o) (π)
p̂HL = max{p̂HL , p̂HL }, and â = min{â(o) , â(π) }. We reach the following conclusion:

Theorem 1 The firm’s output and profit decrease after the deployment of the AI, when the ability
gap related to tangible skills between employees is low and there are a large number of HL type
employees. That is, OAI < OnoAI and πAI < πnoAI , when ∆at = aHt − aLt ≤ â and pHL ≥ p̂HL .

---

18 Incentive Issues in AI Deployment

 πAI -πnoAI

 -0.015 -0.009 -0.003 0.003 0.009 0.015

Figure 5 How gap in tangible skills and workforce composition affect the change in profits (πAI − πnoAI ): this plot
 visually shows Theorem 1–how the firm’s profit changes after AI deployment, with respect to the ability
 of low-type (aLt ) and employee composition (pt & pi ).

 From Theorem 1, we can see that the parametric conditions for the firm’s productivity and profit
follow similar patterns. First, the parameter condition ∆at = aHt − aLt ≤ â indicates that when the
tangible-skill gap between low-type and high-type employees is small, AI deployment can reduce
profit. Intuitively, if low-type employees already possess skills close to the high-type, AI offers limited
scope for further improvement; hence, the “learning effect” is weak. In contrast, when this gap is
large, AI substantially enhances the productivity of low-type employees, increasing overall output.
Second, the composition of the workforce also matters. A firm with a large share of HL employees
(i.e., pHL ≥ p̂HL ) is more likely to experience a profit decline. For the HL type, AI substitutes for their
primary advantage, lowering their motivation. With AI hurting the motivation of the main body of
employees, we expect the firm’s performance to fall.

 Figure 5 illustrates the results in Theorem 1, showing how AI affects firm profit across different
tasks and workforce environments. Green areas indicate profit increases after AI deployment, while
red gradients represent profit declines. In the software development context discussed earlier, the
comparison between the plots reveals that AI deployement is more likely to backfire when the
technical skill gap between employees is small (i.e., a large αL )—as seen in the larger red-gradient

---

 Incentive Issues in AI Deployment 19

area in the right-hand plot—or when a large share of the workforce consists of HL employees with
strong technical but weaker interpersonal skills. These patterns underline that AI’s overall impact on
firm performance depends on the employees’ skill set and on the firm’s employee composition. When
tangible-skill differences are small, AI offers limited room for productivity improvement. However,
when AI substitutes for the core strengths of technically skilled HL employees, their motivation
diminishes, leading to a reduction in overall firm performance.

 We now proceed to analyze the impact of AI deployment on the welfare of employees.

3.3. Impact on Employee Welfare

In the previous section, we saw that AI can negatively impact a firm’s profit. We now analyze the
impact of AI on the welfare of employees. We measure the employees’ welfare by their net utility in
equilibrium. Using employees’ decisions as given in Table 4, we find the following result:

Proposition 2 After the AI deployment, the welfare of HH employees is unaffected, because they
have both high tangible and intangible skills and, therefore, continue to remain the top perform-
ing employees. The welfare of HL employees decreases, because their high tangible skills are no
longer advantageous in the presence of AI-induced knowledge transfer. The welfare of LH employees
increases, because their high intangible skills make them valuable, since AI cannot easily transfer
such skills. The welfare of LL employees increases, because their productivity increases with the help
of AI-facilitated knowledge transfer.

 The conclusion on the welfare of individual employee types is consistent with the breakdown
analyses for productivity in Section 3.2. The HH type employees remain unaffected by AI, because
AI doesn’t improve their ability, and they continue to maintain the top position in the output
ranking. The HL type employees suffer a welfare loss because of the lower output ranking after AI.
As AI improves the abilities of LH and LL employees, they become more productive and competitive
and achieve a higher net utility after AI.

 From Proposition 2, we also observe that employees with a high level of tangible skills i.e., HH
  
and HL can be worse off, and the employees with a low level of tangible skills i.e., LH and LL are
 
better off after AI deployment. Similarly, employees with high-intangible skills i.e., HH and LH
will be better off. Interestingly, AI benefits employees who are better at intangible skills. Intuitively,
this is because as AI evens out the differences in tangible skills, those who are strong in intangible
skills emerge as the more competitive employees and become the top performers.

 Thus far, we have illustrated the possibility that AI deployment in a firm using PFP remuneration
scheme could lead to a decrease in profit. We now analyze some remedies that can be used to mitigate
profit loss stemming from the demotivating effect of AI deployment.

---

20 Incentive Issues in AI Deployment

4. Remedies
To recall, the main reason behind the profit reduction after a firm’s AI deployment is the decrease
in output from HL type employees. This happens because the output ranking of HL employees goes
down after the AI deployment, and they are paid a lower salary rate, relative to the HL employees.
We analyze the following three policies to mitigate the problem:
 • Guaranteed Salary: In this policy, the firm guarantees that no employee’s salary rate will
 go down after the deployment of AI. Thus, if an employee type were getting a bonus salary
 rate before the AI deployment, they would continue to get that salary rate even after the AI
 deployment.
 • Choosing Optimal AI Level: In our model, HL type employees’ output ranking goes down
 because AI transfers knowledge drawn from the tangible skills of HL employees to their com-
 peting peers. This knowledge transfer makes the competitors of HL employees more productive,
 and they overtake HL employees in the overall task output ranking. The firm can mitigate
 this problem by deliberately choosing a less effective AI. We model this by allowing the firm to
 choose the optimal value of AI efficacy, f .
 • Strategic Hiring: In this policy, the firm actively tries to hire more high-tangible ability
 employees. We model this by allowing the firms to exert a costly effort to identify the high-
 tangible-ability candidates in the hiring process.

 We analyze these policies in detail below.

4.1. Guaranteed Salary
In this policy, the firm guarantees that no employee’s salary rate will decrease after the AI system
 g
is deployed. We name this reward scheme the ‘guaranteed-salary’ policy and use πAI to denote the
firm’s post-AI profit under this reward policy (here, the superscript ‘g’ stands for ‘guarantee’). We
 ng ng
use the notation πnoAI and πAI for the profits under the base model reward scheme to emphasize that
it doesn’t provide any salary guarantee (‘ng’ for ‘no-guarantee’).

 Since the guaranteed-salary policy ‘guarantees’ that none of the employees’ salary rates will
decrease in the post-AI era, it is rational for the HL employees to expect to continue receiving the
bonus rate, as they did prior to AI adoption. This guarantee of bonus rate has an anti-competitive
element because now the HL employees do not have to exert additional effort to maintain their
second position and bonus. Hence, the HL type simply produces the ‘natural’ output according to
Lemma 1.

 Similarly, LH type employees also produce their ‘natural’ output because HL employees are no
longer giving them competition, and the natural output is enough to place them in the second

---

 Incentive Issues in AI Deployment 21

position in the output ranking to get the bonus rate. Overall, all employee types produce their
‘natural’ output as given in Lemma 1, and nobody produces any extra output (or competitive
output). Therefore, we can write the profit of the firm under the guaranteed-salary policy as:
 g
 πAI = (1 − γB )(oHH
 γ
 pHH + oLH
 B γ
 pLH + oHL
 B
 AI
 γ
 pHL ) + (1 − γ)oLL
 B γ
 pLL . AI

 To understand whether the guaranteed salary could prevent AI from backfiring, we com-
pare the firm’s post-AI profit under the guaranteed policy with the firm’s profit before
 HH HL HH HH
 g M2 (o −oγ )pHL +(M1 oγ −M2 oγ )pLH
AI deployment (πAI vs πnoAI ). Denote â(g) = 2 β 2 [M Kmax
 p +(M γ−M γ [1−f ])p
 B B
 and
 t 2 1 HL 1 2 B LH +M1 f γpLL ]
 LHAI LH LL LL
 (g) (M2 oγ −M1 oγ )pLH +M1 (oγ AI −oγ )pLL
p̂HL = B
 LH HL
 M2 (omax −oγ )
 . Formally, we note the result as follows:
 B

Proposition 3 The firm’s profit after AI deployment under the guaranteed policy can be lower than
 g (g)
its profit before AI deployment, i.e., πAI ≤ πnoAI when ∆at = aHt − aLt ≤ â(g) and pHL ≥ p̂HL .

The above result suggests that the guaranteed salary policy may not prevent AI from backfiring.
The intuition is that although a guaranteed policy prevents ranking reversal between HL and LH
type employees, it also removes the need for HL employees to compete for the bonus rate, and
weakens their incentive to exert additional effort. While LH and LL employees may still experience
productivity gains through AI’s knowledge transfer, these gains are often smaller than the decrease
in output from the previously competitive HL group. As a result, the overall output and profit of
the firm can decline relative to the pre-AI case. This effect is most pronounced when the ability gap
in tangible skills between employee types is small (i.e., αL is high) or when the workforce includes
many HL employees, as illustrated in Figure 6. In such environments, the drop in motivation among
technically-skilled employees outweighs the incremental productivity improvements of others.

 One might wonder if the guaranteed policy serves to mitigate the backfiring problem, even if it
doesn’t eliminate the problem. That is, although the profit under the guaranteed policy is lower than
the profit before AI, can it be higher than the profit without the guarantee after AI deployment?
To examine this, we compare the firm’s profit after AI deployment with and without the guarantee.
 g ng
That is we compare πAI and πAI and get the following result:

Proposition 4 After AI deployment, the firm’s profit under the guaranteed policy can be lower than
 g ng
that under the no-guarantee policy, i.e., πAI ≤ πAI , when (1 − γB )γB < (1 − γ)γ.

 Proposition 4 shows that, when comparing two post-AI reward policies—one with a guaranteed
salary and one without—the guaranteed policy can further reduce firm profit. Under the guarantee,
HL employees anticipate that their bonus rate will be maintained and produce at a higher output
level than the no-guaranteed policy; however, this output level comes at a higher wage cost to the

---

22 Incentive Issues in AI Deployment

 0.75

 % of employees with high tangible skills (pt )
 g
 πAI < πnoAI

 0.6

 0.45

 0.3
 0. 0.1 0.2 0.3

 Low tangible skills level (aLt )
 g
Figure 6 Comparison of profit under the guaranteed policy (πAI ) and before AI (πnoAI ): The guaranteed policy can
 also lead to lower profit for the firm after AI deployment. This is more likely to happen when the ability
 gap in tangible skills is low (i.e., aLt is high) or if there is a significantly high proportion of employees
 with high ability in tangible skills (i.e., pt is high).

firm. Meanwhile, LH employees face less competitive pressure and reduce their output compared to
the no-guarantee scenario. The combination of higher compensation expenses and lower incremental
output leads to a smaller profit margin. Note that the guaranteed policy doesn’t affect the incentives
of other employee types, i.e., HH and LL, because these employee groups continue to remain at the
top and at the bottom of output ranking, respectively, after AI deployment, and their salary rate
remains unchanged. An important managerial implication for Proposition 4 is that the guaranteed
policy not only fails to mitigate profit loss but can actually worsen it compared with a standard
PFP scheme.

 We now proceed to analyze the policy where the firm chooses an optimal level of AI efficacy.

4.2. Choosing Optimal AI Efficacy Level
Thus far, we have focused on the case when AI changes the productivity ranking between HL and
LH employees. When this flip in productivity rankings happens, the HL employees are expected
to deliberately reduce their task output, resulting in a total productivity loss and profit reduction
for the firm. From our analysis of Section 3.1, we know that the reversal in performance ranking
between HL and LH does not always occur. Specifically, when the AI efficacy is low (i.e., when f
is low), the performance ranking between HL and LH doesn’t reverse and stays as it was before AI

---

 Incentive Issues in AI Deployment 23

deployment. Thus, the firm can choose an optimal level of AI efficacy in order to avoid performance
ranking reversal between HL and LH employees.
 q
 γ 2 −γ 2 (βt2 at +βi2 a )
 H L
 β 2 (a −a ) β 2 (a −a )
 H L H L

 Define fˆ(l) = 1 − βi2 aiH −aiL and fˆ(u) = 1 − βi2 aiH −aiL + Bγ β 2 aH −aL i . To find the optimal AI
 t( t t) t( t t) B t( t t)
efficacy, we first consider the case when AI is not very effective, that is when AI efficacy f ≤ fˆ(l) . In
this case, the HL employees can keep their lead in performance ranking over the LH type employees.
Hence, employees’ output decisions will be similar to the before-AI scenario in Table 4, with the
LH and LL producing at their new effective-ability levels (corresponding to the optimal value of
f ). The other extreme scenario is when AI becomes extremely effective, i.e., f ≥ fˆ(u) . In this case,
AI could boost the LH type to be so productive that the HL employees cannot compete with them
for the bonus. In other words, the natural-output gap between second and third-ranked employee
types is so high that the third-ranked employee type’s (i.e., HL’s) maximum output is also lower
than the natural output of the second-ranked employee type (i.e., LH). Thus, under this scenario,
all employees will produce at the natural output level. The third scenario is when the AI efficacy
is between intermediate, i.e., fˆ(l) < f < fˆ(u) . In this case, the output ranking between HL and LH
employee types is reversed after AI deployment. However, the gap between their natural output
is not much. Thus, the LH type must match the maximum output produced by the HL type to
maintain its second position. We combine these three cases of employee competition and derive the
firm’s profit as a function of f as follows:
 
  (1 − γB )(oγ pHH + omax pHL ) + (1 − γ)(oγ pLH + oγ pLL ), f ≤ fˆ
  HH LH AI LH AI LL AI (l)
 B
 HH HL HL LL
 πAI (f ) = (1 − γB )(oγ pHH + omax pLH ) + (1 − γ)(oγ pHL + oγ pLL ),
 B
 AI
 fˆ(l) < f < fˆ(u) (13)
 f ≥ fˆ(u)
 
  (1 − γ )(oHH p + oLH p ) + (1 − γ)(oHL p + oLL p ),
 AI AI
 B γ HHB γB LH γ HL γ LL

 Figure 7 plots the profit of the firm πAI (f ) against f . We see that πAI (f ) has two kinks at thresholds
fˆ(l) and fˆ(u) , and increases otherwise. The vertical dotted line on the left captures the flipping
threshold fˆ(l) above which the AI-induced knowledge transfer leads to the flipping of performance
ranking between HL and LH. We can see that if the firm picks an AI system that is less effective
than fˆ(l) , it can avoid flipping in productivity ranking because there will be no disincentive for HL
type employees.

 On the other hand, when the firm picks an AI efficacy level more than fˆ(l) , the profit could suddenly
drop to a level that AI implementation becomes a sub-optimal investment. Even though the profit
level recovers as the firm chooses an even more effective AI, the profit generated even by a perfect AI
(i.e., when f = 1) could still be lower than the profit without flipping of ranking. This is illustrated
with Figure 7: in each case, the profit increases as f increases. Given this behavior of πAI (f ) with
respect to f , it is easy to see that the maximum value of πAI (f ) is achieved at either f = fˆ(l) or at

---

24 Incentive Issues in AI Deployment

 0.050 Firm's profit

 0.048

 0.046

 0.044

 0.042
 Effectiveness
 of AI (f )
 0.040
  l  0.5  (u ) 1
 f f

 πAI πnoAI

Figure 7 The change in the firm’s profit changes with the choice of AI (f ).

 2 H L
 β (a −a )
f = 1. To avoid trivial cases, we assume that the πAI (f ) is maximized at f = fˆ(l) = 1 − βi2 aiH −aiL .
 t( t t)
 (f )
This happens when pHL ≥ p̂HL , where
 γ 2
 (f ) (M2 oHH
 γB
 − M1 oHL H L
 γ )pLH + M1 2 βi (ai − ai )pLL
 p̂HL = .
 M2 oHL HL
 max − M1 oγ

Formally, we note the result as follows:

Proposition 5 The firm can achieve the highest level of profit by choosing an AI efficacy level that
is just enough to avoid the flipping in the performance ranking of HL and LH employees. That is,
the maximum profit is achieved at f = fˆ(l) , when pHL ≥ p̂HL .
 (f )

Proposition 5 shows that the firm’s optimal strategy of leveraging an AI system is by deploying
one with an efficacy level just high enough to avoid a reversal in the performance ranking between
HL and LH employees. From a managerial perspective, this result implies that pursuing the most
advanced AI system is not always optimal. Instead, firms should calibrate AI capabilities to balance
the enhancement in employee technical skills with their motivation. Denote the optimal AI efficacy
level as f ∗ . We can interpret it as the optimal level of involuntary knowledge transfer among the
employees. In the result below, we note the behavior of f ∗ :

Proposition 6 The optimal AI efficacy level, i.e., f ∗ , increases with the ability gap in tangible skills
(i.e., aHt − aLt ) and decreases with the ability gap in intangible skills (i.e., aHi − aLi ).

---

 Incentive Issues in AI Deployment 25

Intuitively, the firms that have very high heterogeneity in their employees’ tangible skills stand to
gain a lot from AI deployment. Thus, the optimal level of AI efficacy increases with the ability
gap related to tangible skills because AI can significantly improve the firm’s low-ability employees.
Interestingly, the second part of the Proposition 6 suggests that intangible skills also play a role in
choosing the optimal efficacy level of AI. Although AI in our framework does not improve employees’
intangible skills (by definition), the heterogeneity in these skills still affects the firm’s optimal AI
decision. When the workforce exhibits a large gap in intangible abilities—such as communication or
coordination—the LH employees, who excel in these areas, can easily surpass HL employees once AI
assists their technical tasks, reducing overall profitability. To avoid ranking reversal, the firm finds it
optimal to limit the AI’s efficacy further to preserve motivation and effort among technically skilled
HL employees. Managerially, this result emphasizes that AI investment should account for the skills
AI cannot replicate. In teams with high variation in such skills, a more moderate AI deployment
may lead to higher overall performance.

4.3. Strategic Hiring

The workforce in any organization is rarely static. Instead, companies actively seek new talent.
Given the firm’s strategic role in choosing the workforce, we would like to explore whether combining
strategic hiring with AI adoption could rectify AI’s pitfalls. Therefore, we extend our base model
by allowing the firm to choose the employee composition. Specifically, we model that the firm can
assess job candidates’ ability in tangible skills and increase the proportion of high-tangible-ability
employees (pt ) by investing in the recruitment process. In most of the hiring process, there is an
‘average’ percentage of job candidates with high-tangible skills. That is, even if the firm does not
invest any additional effort in the recruitment process, it can still obtain a certain percentage of
high-types in tangible skills. We denote this percentage as p̄t . As with any other type of performance-
enhancing investment, the firm would bear a cost if it attempts to achieve a pt level different from
the natural level p̄t . We use a quadratic cost function 2c (pt − p̄t )2 , where c is a scaling cost coefficient.
Mathematically, the firm optimizes its profit over pt for both before AI and after AI:
 h i h i c
max πnoAI = max (1 − γB ) oHH
 γ
 pi + oLH
 max (1 − pi ) pt + (1 − γ) oγ pi + oγ (1 − pi ) (1 − pt ) −
 LH LL
 (pt − p̄t )2
 pt pt B
 2
 h i h i c
 max πAI = max (1 − γB ) oHH
 γ
 p t + o HL
 max (1 − p t ) pi + (1 − γ) o HL
 γ
 p t + o LL
 γ
 (1
 AI
 − p t ) (1 − pi ) − (pt − p̄t )2
 pt pt B
 2
 Solving the above problems for the optimal values of pt , we get
 (M2 oHH
 γ − M1 oLH LH LL
 γ )pi + (M2 omax − M1 oγ )(1 − pi )
 pnoAI
 t = B
 + p̄t ,
 c
 M2 (oHH
 γ − oHL HL
 max )pi + M1 (oγ − oγ
 LL
 )(1 − pi )
 AI

 pAI
 t = B
 + p̄t ,
 c

---

26 Incentive Issues in AI Deployment

where M1 = 1 − γ, M2 = 1 − γB . Figure 8 plots pnoAI
 t and pAI
 t . We note that after AI adoption, the firm

hires a lower proportion of high-tangible ability employees. As we show in Theorem 1, too many
high-tangible ability employees may be detrimental to the firm since they might get demotivated in
the presence of AI due to the increased competition from low-tangible ability employees.

 Optimal level of employees with high-tangible skills

 0.25 0.35 0.45 0.55 0.65

Figure 8 Optimal level of employees with high-tangible skills that the firm chooses to hire.

 After substituting the optimal values of pnoAI
 t and pAI
 t in the profit expressions, we numerically

compare the profit of the firm before and after the AI adoption. Figure 9 depicts the change in profit
(πAI − πnoAI ) with respect to p̄t and cost coefficient of strategic hiring (c). We can observe that the
trend shown in Theorem 1 continues to hold when p̄t is high; that is, the firm’s profit would decrease
after AI adoption when there is a high proportion of HL type. Even with strategic hiring, where the
firm could optimize the percentage of employees with high-tangible skills, the firm could be worse
off after AI adoption.

 We also note that strategic hiring is more likely to mitigate the drawbacks of AI when the cost
coefficient c is high. This is because, when it is costly to assess job candidates’ tangible skills, the
firm would hire a low percentage of HL type employees before AI and maintain an even lower level
of HL employees after AI. As a result, the demotivating effect experienced by HL type is less likely
to dominate AI’s positive effect through productivity gains.

---

 Incentive Issues in AI Deployment 27

 0.002

 0.

 -0.002

 -0.004

Figure 9 How the natural percentage of employees with high-tangible skills (p̄t ) and the cost coefficient (c) affect
 the profit change (πAI − πnoAI ).

 In the next section, we generalize our base model to include the following features: (i) We model the
training of AI system using the data generated within the firms, (ii) We allow firm to endogenously
decide the salary rate.

5. Generalized Model of AI
When a firm deploys an AI system, it typically buys the system or major components of it from
specialized vendors with relevant domain and technical expertise. The efficacy of such a commercial-
off-the-shelf (or COTS) AI system further improves when it is used within the firm because it is
further trained on the data generated by employee activities specific to the firm. In this section, we
generalize our model to incorporate the dependence of AI effectiveness f on training from employee
activity data. We model the two factors that contribute to overall AI efficacy: the first factor is the
base effectiveness of the system when the firm purchased the COTS solution, and the second factor
stems from the system’s local observations and continuous training based on employees’ task-level
activity data. Specifically, we model AI effectiveness as
 WtH
 f = f0 + (1 − f0 )θ . (14)
 Wtmax
The first part in the above formulation, i.e., f0 , represents the base efficacy of a COTS AI system.
In the second component of AI efficacy, we use θ ∈ [0, 1] to represent the quality of the training

---

28 Incentive Issues in AI Deployment

infrastructure to collect employee data and use it to refine the AI system. The term WtH is the total
tangible labor from high-type employees. The normalization factor Wtmax is the maximum possible
total tangible labor produced by the high-type employees. Let γ̄ denote the maximum possible salary
rate offered by the firm. Then, Wtmax = γ̄2 βt aHt (pHH + pHL ).

 Recall our discussion of rational expectation equilibrium in Section 3, where employees rationally
anticipate their output rank and expected salary rate to produce the output. Eventually, the output
ranking realized in the equilibrium matches the output rank “rationally” anticipated by employees.
Here, again, we use the same concept of rational expectations equilibrium to obtain the equilibrium
AI efficacy. In this case, the employees form rational expectations over AI efficacy, in addition to
rational expectations over their output ranking. Note that in the context of the COTS AI system
refined with firm-specific data and fine-tuning, the efficacy of AI depends on the output of employees,
and the output of employees depends on the efficacy of AI. To solve for this circular dependency
and obtain the equilibrium output of employees and the AI efficacy, we once again use the REE
framework. Specifically, the employees will “rationally” anticipate the equilibrium efficacy of AI, and
produce the output. Eventually, the output produced by employees leads to the same AI efficacy
that they had “rationally expected”.

 We should also note that the model of AI in (14) assumes that only the training data obtained
from employees with high tangible ability is effective to continuously refine the AI system. This
assumption reflects the idea that a well-trained AI system is designed to mimic the actions of
employees with high tangible ability. This provides another strategic lever to employees with high
tangible ability, as they can deliberately choose to produce a lower level of output with the intention
of denying learning opportunities for the AI system. With this strategic choice related to the use of
tangible skills, it is possible that the HL type employees opt to minimize the AI system’s impact on
improving the skills of the LH type employees. Given these considerations, we need to analyze the
following three scenarios in order to obtain the equilibrium:

 1. The equilibrium AI efficacy is too low, and it doesn’t lead to the reversal of ranking between
 HL and LH.
 2. The equilibrium AI efficacy is neither too low nor too high. In this case, the flipping of per-
 formance ranking between the HL and LH employees does not occur. That is, HL type of
 employees strategically devote a lower level of labor utilizing tangible skills to keep their superior
 task output rank over LH type of employees.
 3. The equilibrium AI efficacy is too high, and even the natural labor output of HL type of
 employees at the base rate is sufficient to trigger the flipping of performance ranking between
 HL and LH types of employees.

---

 Incentive Issues in AI Deployment 29

 Next, we analyze how employees make decisions under the above three scenarios and accordingly
derive the AI-deploying firm’s profit.

 Case 1 : In this case, the HL type maintains its lead over LH type employees because the
equilibrium efficacy of AI is not enough to reverse the output ranking between HL and LH. However,
the level of labor utilizing tangible skills from the HL employees is affected by the LH type’s
commitment to challenging the top performers. Under this generalized model, where the output
of high-type employees improves the quality of AI, the LH type at a lower rank has a stronger
motivation as they can benefit from the increased high-type tangible labor. Hence, the HL employees
would have to produce at the maximum level as shown in Table 4. Thus, the overall AI effectiveness
can be written as:
 γB
 β aH p + K21 βt aHt A
 2 t t HH
 5
 p
 A2 HL
 f = f0 + (1 − f0 )θ γ̄ H
 ,
 β a (pHH + pHL )
 2 t t
 βt2 aLte + βi2 aHi
  
 θ
 = f0 + (1 − f0 ) γB pi + K1 2 H (1 − pi ) .
 γ̄ βt at + βi2 aLi
Recall that aLte = aLt + f (aHt − aLt ). Thus, in the above equation, f appears on both sides of the
equation. We can obtain the rational expectations equilibrium value of f by solving the above
equation for f . Let f = F1 (f0 , θ) denote this equilibrium value of AI efficacy under Case 1, and
define A1 = βt2 aHt + βi2 aHi , A2 = βt2 aHt + βi2 aLi , A3 = βt2 aLt + βi2 aHi , A4 = βt2 aLt + βi2 aLi , A5 = βt2 aLte + βi2 aHi
and A6 = βt2 aLte + βi2 aLi . Then, we have
 γ̄A2 f0 + (1 − f0 )[γB A2 pi + K1 A3 (1 − pi )]θ
 F1 (f0 , θ) = .
 γ̄A2 − (1 − f0 )K1 βt2 (aHt − aLt )(1 − pi )θ

 We now identify the conditions under which case 1 will hold. From inequality (9) in Section 3.1,
we require F1 (f0 , θ) ≤ fˆ for this case to hold. This condition is equivalent to f0 ≤ fˆ0 , where
 (l)

 fˆγ̄ − [γB pi + K1 (1 − pi )] θ
 fˆ0 =
 (l)
 . (15)
 γ̄ − [γB pi + K1 (1 − pi )] θ
 The performance ranking and employee incentives remain the same as in the prior-AI period in
this case. As a result, the firm’s profit can be obtained from the output decisions of the ‘Before-AI’
scenario in Table 4, with AI improving the low-type employees’ ability related to tangible skills by
rate F1 (f0 , θ). That is, the profit of the firm is as given in equation 11 with f = F1 (f0 , θ).

 Case 2 : In this case, if the HL type decides to produce as much as in Case 1, the equilibrium
AI-efficacy can become too high. Consequently, with this high AI-efficacy, the output of LH can
become higher than that of HL. As a result, the HL employees strategically reduce their labor
utilizing tangible skills to a level that the equilibrium efficacy of AI is not enough to trigger flipping
of output ranking. Let F2 (f0 , θ) denote the equilibrium AI efficacy. Then, we have

 F2 (f0 , θ) = fˆ − .

---

30 Incentive Issues in AI Deployment

where fˆ is as defined in (10). To obtain the firm’s profit, we need to determine employee decisions
in equilibrium. Interestingly, employee awareness about how AI works would affect the competitive
dynamic for the second place. As the HL type uses its strategic leverage in deciding the overall AI
effectiveness, the LH type is no longer a credible threat. Therefore, the LH type produces at the
natural level with the expectation of receiving the base rate. The HL type decides its labor utilizing
tangible and intangible skills separately, with the labor utilizing tangible skills maintained at the
level of avoiding the flip in performance ranks, and the labor utilizing intangible skills maximizing
the overall utility. Let wtHL and wiHL denote the equilibrium values of HL’s decisions on labor input
related to tangible and intangible skills; we have the equilibrium output from an HL employee as
 βt2 aHt (aHi − aLi )βi2 βi2 aLi
    
 HL HL γ̄
 βt wt + βi wi = 1− H − γB p i + .
 2(1 − pi ) θ (at − at )βt2 (1 − f0 )
 L
 2

 Next, we identify the parametric condition for this equilibrium. As the HL employees deliberately
lower their effort utilizing tangible skills, their utility level would also decrease. They would keep
doing so till the utility level decreases to the level of being paid at the base rate. This condition is
equivalent to
 fˆγ̄ − [γB + K2 (1 − pi )] θ
 fˆ0 ≤ f0 ≤ fˆ0 =
 (l) (u)
 ,
 γ̄ − [γB + K2 (1 − pi )] θ
 s 
 L
 βi2 ai
where K2 = 1 + β 2 aH (γB2 − γ 2 ).
 t t

 Case 3 : In this case, the equilibrium AI efficacy is so high that even the natural output of
employees will trigger a flipping of ranking between LH and HL. Thus, LH will be placed at the
second rank, and HL will attain the third rank. Also, since HL type knows that their output benefits
the LH type (via an improved AI efficacy), they have little incentive to challenge the LH employees
because the more they produce, the more capable LH becomes. If the HL type produces at its
maximum output level, it will make the LH type even more productive, and even their maximum
output level would not be a threat to the LH type. As a result, it is not in the HL employees’
interests to challenge those promoted. Thus, the LH type only needs to produce at the natural level
with the expectation of receiving the bonus rate. Therefore, we have the tangible labor from the HL
 γ
to be 2 βt aHt . The HH employees would also produce at the natural level with the expected salary
 γB
γB (their tangible labor is β aH ). Let F3 (f0 , θ) represent the equilibrium AI efficacy in this case.
 2 t t

Then, we have
 γB γ
 β aH p + 2 βt aHt pHL
 2 t t HH
 F3 (f0 , θ) = f0 + (1 − f0 )θ γ̄
 β aH (pHH + pHL )
 2 t t
 γB pi + γ(1 − pi )
 = f0 + (1 − f0 )θ .
 γ̄

---

 Incentive Issues in AI Deployment 31

 0.5 Overall AI
 Effectiveness (f )

 0.4

 0.3 Case 3

 Case 1
 0.2
 Case 2

 0.1
 AI's Base
 Effectiveness (f0 )
 0.0
  l   (u ) 0.2 0.4
 f0 f0
Figure 10 Trend in the overall AI effectiveness with the choice of f0 .

 Firm's profit
 0.050

 0.045 Case 1

 0.040 πAI
 Case 3
 πnoAI
 Case 2
 0.035

 AI's Base
 0.030
 Effectiveness (f0 )

  l   (u ) 0.2 0.4
 f0 f0
Figure 11 Trend in firm’s post-AI profit with the choice of f0 .

 Next, we plot the above three equilibria under different values of f0 and focus on how the choice of
base AI effectiveness f0 affects the final equilibrium AI efficacy and the overall profit. Figure 10 and 11
depict how the choice of f0 affects the overall AI effectiveness and the firm’s profit, respectively. In
Figure 11, we can see a significant drop in the firm’s profit at the boundary value between Case
1 and Case 2 (i.e., when f0 = fˆ0 ). If the firm decides to pick the value of f0 , it would be better
 (l)

off choosing the base AI capability at f0 = fˆ0 . This observation is consistent with our finding in
 (l)

Section 4.2 that the firm can prevent AI’s negative impact by picking a less effective AI product.

---

32 Incentive Issues in AI Deployment

 fˆγ̄−[γB pi +K1 (1−pi )]θ
Let f0∗ represent the optimal value of f0 . Then, we have f0∗ = fˆ0 = γ̄− γ p +K (1−p ) θ . From the
 (l)
 [B i 1 i ]
 (ai −ai )βi2
 H L
 ˆ(l) p 2 ˆ
definition of f0 and knowing that K1 = γB + γB − γ and f = 1 − (aH −aL )β 2 we have the following
 2
 t t t
observation:

Observation: We note that when the AI system relies on the firm’s own training data (not just the
COTS vendor’s), it will take the competition effect away when choosing the base AI that is higher
than fˆ0 . In Case 2, that is fˆ0 ≤ fo ≤ fˆ0 , we note that the equilibrium AI effectiveness f stays
 (l) (l) (u)

at the same level even if the firm invests in a more effective AI (which is also likely to be more
costly). This is because HL type employees deliberately lower their labor utilizing tangible skills.
In addition, such a strategic behavior from HL type employees leads to decreasing profits at the
firm level, even if f0 increases, as shown in Figure 11. Under the region of Case 3, the firm’s profit
remains low because the HL type employees have no incentive to compete for the bonus rate, and,
therefore, LH type employees do not need extra effort to maintain their promotion status. Overall,
under this generalized model of AI, we see that the firm’s best option is still to choose a base AI
efficacy level that is low enough to ensure employees’ incentives remain the same as prior to the AI
system’s deployment.

 The dashed line in Figure 12 represents the firm’s profit before AI. When the ability gap related
to tangible skills is small (or aLt is large), we once again see in this generalized model that the firm’s
profit after AI deployment can be lower than that prior to the AI deployment. Similarly, Figure
13 plots equilibrium AI-efficacy against aLt . We see that there is a non-monotonic relation between
equilibrium AI-efficacy (f ) and aLt .

6. Robustness Check
In this section, we check the robustness of our main results by incorporating some additional features.

6.1. Endogenous Salary Rate

In our analysis thus far, we assumed the salary rates to be exogenously given. In this section, we allow
the firm to choose an optimal salary rate that maximizes its profit. For analytical tractability, we
assume that is γ = δγB , where δ ∈ [0, 1]. The firm optimizes the profit - Equation (7) and (11) - with
respect to γB . We use γBnoAI and γBAI to represent the firm’s equilibrium decision on the bonus salary
 √ 
rate, prior-to-AI, and post-AI, respectively. To simplify the equations, we define K3 = 1 + 1 − δ 2 .

Lemma 3 Before AI deployment, the optimal bonus rate chosen by the firm is
 A1 pHH + A3 [K3 pHL + δpLH ] + A4 δpLL
 γBnoAI = ;
 2 (A1 pHH + A3 [K3 pHL + δ 2 pLH ] + A4 δ 2 pLL )
 With AI, the firm’s choice of salary rate becomes
 A1 pHH + A2 [K3 pLH + δpHL ] + A6 δpLL
 γBAI = .
 2 (A1 pHH + A2 [K3 pLH + δ 2 pHL ] + A6 δ 2 pLL )

---

 Incentive Issues in AI Deployment 33

 0.060 Firm's profit

 0.055

 0.050
 Case 1
 0.045
 πAI
 0.040
 Case 3 πnoAI
 0.035 Case 2

 0.030

 0.025 Low-type
 Tangible Skills (atL )
 0.020
 at
 L l  L (u )
 at 0.15 0.3

Figure 12 Trend in firm’s profit with the level of low-type tangible skills aLt .

 Overall AI
 0.4
 Effectiveness (f )

 0.3
 Case 1

 0.2 Case 2 Case 3

 0.1
 Low-type
 Tangible Skills (atL )
 0.0
 at
 L l  L (u )
 at 0.15 0.3

Figure 13 Trend in the overall AI effectiveness with the level of low-type tangible skills aLt .

 Figure 14 illustrates the different workforce composition configurations where the firm would be
willing to pay a higher salary rate after AI deployment. Thereby, we make the following observation:

Observation 1 The firm pays a higher salary rate after AI deployment when there is a high per-
centage of employees in the HL group.

---

34 Incentive Issues in AI Deployment

 0.8

 % of employees with high intangible skills (pi )
 Salary rate decreases
 0.65
 (γBnoAI >γBAI )

 0.5

 0.35 Salary rate increases
 (γBnoAI <γBAI )

 0.2
 0.2 0.35 0.5 0.65 0.8

 % of employees with high tangible skills (pt )

Figure 14 Optimal salary rate: the blue shaded region depicts when the salary rate increases after AI deployment.

 The intuition of the above observation is that if there are more employees of HL type (or fewer
LH ones), the firm ends up paying a smaller number of employees at the promoted rate, as it is the
HH and LH types that are receiving the bonus rate.

 Figure 15 shows that our main result (Theorem 1) continues to hold for this extension. We also
identify an interesting relationship between the overall productivity, total salary paid, and the firm’s
profit. Formally, we reach the following conclusion:

Proposition 7 When the firm is worse off after AI deployment, both the firm’s profit and the total
wages paid to employees drop; these reductions in the firm’s and employees’ welfare come ‘entirely’
from the decrease in productivity.

 Recall that we find that the salary rates go up after AI deployment; one might suspect that the
higher salary causes the profit drop. However, we show with Proposition 7 that the total salary
paid to all employees actually decreases. The reason is that the total economic value generated from
employee efforts is divided between the firm and its workers through the reward scheme. When the
firm can adjust the bonus rate freely, the relative split of value remains the same before and after AI
deployment. Thus, the observed decline in both profit and total employee welfare reflects a genuine
drop in productivity. This result also highlights that flexible salary rates alone cannot offset the
negative productivity effects of AI if the technology undermines employees’ incentives.

---

 Incentive Issues in AI Deployment 35

 πAI -πnoAI

 -0.010 -0.006 -0.002 0.002 0.006 0.010

Figure 15 How tangible skill gap and employee composition affect the profit change (πAI − πnoAI ): this plot visually
 shows the Theorem 1 still holds when salary rates are endogenously picked by the firm.

6.2. Mixed Strategy

The competition for the second place in the performance ranking can also be examined with a mixed
strategy of employees HL and LH. Recall that in Section 3.1, we show that the two-tier reward
scheme can incentivize the employees to compete for the bonus. When the HL type is naturally
more productive, LH could exert more effort to challenge HL’s 2nd place. On the other hand, HL
is able to maintain its lead by producing more output. In other words, both types of employees face
two strategies. For HL, it chooses between the ‘natural’ output level or the ‘deterring’ level. For LH,
it decides whether to produce at the ‘natural’ output level or the ‘challenging’ level. The production
decisions (i.e., the output levels) using the notations specified in Section 3.1 and competition results
(i.e., employees’ utility) can be summarized by the payoff matrix of Table 5, with HL being the
row player. To simplify the equilibrium utility values, we rewrite the optimal utility of Lemma 1 for
employee type i as function Ui (O, γ), in terms of productivity level and salary rate1 .
 Following the mixed strategy equilibrium condition, we know that HL would choose a qHL value
to make LH indifferent between the ‘natural’ output and the ‘challenge’ one. Similarly, LH would

1
 For instance, UHL (oLH LH
 max , γB ) is HL’s utility when it receives the bonus rate with the production level omax .

---

36 Incentive Issues in AI Deployment

 Table 5 Decision and Payoff matrix of employee HL and LH
 Natural Challenge
 HL LH
 Natural  (oγ , o )
 B γ
   (oγ , oHL
 γ
 HL
 B
 + ) B 
 HL LH HL HL
 UHL (oγ , γB ), ULH (o , γ)
 B γ UHL (oγ , γ), ULH (oγ + , γB )
 B B

 Deterring  (oLH LH
 max , oγ )   (oLH LH
 max + , omax ) 
 LH LH LH LH
 UHL (omax , γB ), ULH (oγ , γ) UHL (omax +, γB ), ULH (omax , γ)

pick a qLH level under the same rationale. Hence, before AI adoption, the probability profile for HL
and LH satisfies:

 ULH (oLH
 γ
 , γ) = qHL ULH (oHL
 γ
 + , γB ) + (1 − qHL )ULH (oLH
 B max , γ),

 LH LH
 qLH UHL (oHL
 γ B
 , γB ) + (1 − qLH )UHL (oLH
 max , γB ) = qLH UHL (omax , γB ) + (1 − qLH )UHL (omax + , γB )

 We solve for the probabilities for employees to play the ‘natural’ decision:
 noAI
 ULH (oLH LH
 γ , γ) − ULH (omax , γ)
 qHL = ,
 ULH (oHL
 γ + , γB ) − ULH (oLH
 B max , γ)

 noAI
 UHL (oLH HL
 max , γB ) − UHL (oγ , γ) B
 qLH = .
 UHL (oHL HL
 γ , γB ) − UHL (oγ , γ)
 B B

For the after-AI scenario where LH becomes naturally more productive, we can solve for the mixed
strategy equilibrium following the same procedure:
 AI
 UHL (oHL HL
 γ , γ) − UHL (omax , γ)
 qLH = ,
 UHL (oLH
 γ + , γB ) − UHL (oHL
 B
 AI
 max , γ)

 AI
 ULH (oHL LH
 max , γB ) − ULH (oγ , γ) B
 AI

 qHL = LH LH
 .
 ULH (oγ , γB ) − ULH (oγ , γ)
 B
 AI
 B
 AI

With the mixed strategy decisions for employee type HL and LH as outlined above, we numerically
compare the firm’s profit before and after AI adoption with Figure 16, showing that our main finding
continues to hold; that is, the profit decreases when the ability gap between employees is small and
the proportion of HL type employees is large.

7. Conclusion
Despite the growing optimism for an AI-driven productivity boost, there are long-standing con-
cerns about the challenges in trusting and effectively deploying transformational digital technologies
(Gregory et al. 2015, Glikson and Woolley 2020, Brynjolfsson 2022). This study illuminates one
such challenge that stems from potential misalignment between the deployment of AI technologies
and organizational policies related to employee compensation and performance management. We
demonstrate that AI deployment in a PFP organizational environment can have adverse effects and

---

 Incentive Issues in AI Deployment 37

 0.005

 0.003

 0.001

 -0.001

 -0.003

 -0.005

Figure 16 Profit change (πAI − πnoAI ) under the mixed strategy equilibrium: Theorem 1 continues to hold when
 the skill gap is narrow and a large proportion of HL employees.

highlight the key parameters available to managers for mitigating the adverse effects. A summary of
our model results is presented in Table 6, detailing the impact of AI on different stakeholders under
various AI deployment policies. In the table, a value of “0” indicates no impact on the specified
employee groups following AI implementation.

 Table 6 Results Summary
 Impact of AI Under Policy
 Stakeholders
 No Intervention Guaranteed Salary Optimal AI Efficacy
 Firm – – +
 HH Employees 0 0 0
 HL Employees – – 0
 LH Employees + – +
 LL Employees + 0 +

 To recap, organizational deployment of an AI system has the potential to facilitate knowledge
transfer between employees, as the system can be designed to continuously learn from data gen-
erated by task activities. In a PFP regime, high-performing employees who rely on their tangible

---

38 Incentive Issues in AI Deployment

skills are likely to develop negative perceptions towards the AI-facilitated knowledge transfer as they
encounter increased competition from peers who benefit from the AI-facilitated knowledge transfer
and are able to boost their task productivity. Thus, AI deployment in a PFP regime would trig-
ger a demotivation effect on employees who involuntarily participate in knowledge transfer but are
not explicitly compensated for it. The greater the proportion of workforce that relies on tangible
skills and the greater the efficacy of the AI system, the worse the demotivating effect, which nega-
tively impacts overall firm performance. To mitigate this, we recommend that firms judiciously align
the configurations of their AI systems with the task structures of employees, adapt performance
management schemes, and provide incentives for employees for contributing data to the continuous
improvement of the AI systems.

 While we believe the modeling framework presented in the paper illuminates the core issues of
deploying AI in a PFP environment, we acknowledge several limitations. First, the framework focused
on tasks completed entirely by individual employees and did not consider complex, interdependent
task structures, such as those tackled by project teams. AI deployments in PFP regimes that also
involve project teams are admittedly more complex, but they are important and relevant to examine.
Indeed, market surveys indicate that workforce anxiety and managerial skepticism about AI are real
hurdles for the success of organizational AI deployments (Ransbotham et al. 2017, Lohr et al. 2023).
Second, while our analysis considered a broad AI efficacy parameter, we did not specifically account
for task-level mechanisms such as serendipitous discovery, employee noncompliance, and learning
from mistakes, which could inject additional variance in the efficacy of AI-induced knowledge transfer
in a diverse workforce. Finally, it is possible that leaps of refinement in a deployed AI system can
be induced through updates from the COTS vendor, and there are competing internal and external
influences during such system refinements (Ramasubbu and Kemerer 2016). The analysis in this
study did not consider such effects on the efficacy of the deployed AI system. We believe our modeling
framework and results can be extended to address these limitations in future work.

 We conclude by highlighting a couple of adaptive strategies for firms that operate in a PFP
regime and are considering AI deployments. First, instead of evaluating employee performance solely
based on traditional outcomes (e.g., task productivity), considerations of indirect contributions, such
as the generation of unique training data, would encourage high-performing employees to share
their idiosyncratic resources without anxiety. Policies that explicitly recognize and compensate the
role of training data generated by employees would aid smoother deployments and the continuous
refinement of AI systems. Second, we recommend firms considering AI deployments to embrace
modular task structures with specialized labor. Given the complexity of designing optimal incentive
policies for a PFP environment with AI, firms may be motivated to reconsider the diversity of

---

 Incentive Issues in AI Deployment 39

skills in their workforce. An extreme case would be to focus on the ‘perfect’ employees (the HH
type in our framework), who are unaffected by AI. A reduction in the diversity of skills in the
workforce may not always be a desirable or feasible strategy, especially in high-tech domains that
often face a shortage of skilled labor. A feasible alternative would be to adopt streamlined task
structures, which facilitate modular allocation of specialized labor. Such a reconfiguration of the
division of labor in the presence of AI can be facilitated either through task redesign or self-selection
of employees (e.g., Zhou 2013, Raveendran et al. 2021). The division of labor across these specialized
labor configurations would, then, facilitate different modes of AI augmentation depending on the
unique composition of the tangible and intangible skills of the workforce. Thus, AI deployment with
a focus on the augmentation of specialized labor may serve to alleviate the problem of demotivating
and competitive effects that arise from involuntary knowledge transfer. A division of labor design
that focuses on AI augmentation for specialized labor configurations would also help firms to offer
targeted training opportunities to employees who need to improve their intangible skills for better
complementing the AI system.

References
Abernethy, M. A., C.-Y. Hung, and L. van Lent. 2020, January. Expertise and Discretionary Bonus Decisions.
 Management Science 66 (1): 415–432.

Acemoglu, D., A. Makhdoumi, A. Malekian, and A. Ozdaglar. 2022. Too Much Data: Prices and Inefficiencies
 in Data Markets. American Economic Journal: Microeconomics 14 (4): 218–256.

Acemoglu, D., and P. Restrepo. 2019, May. Automation and New Tasks: How Technology Displaces and
 Reinstates Labor. Journal of Economic Perspectives 33 (2): 3–30.

Agrawal, A., J. S. Gans, and A. Goldfarb. 2019, May. Artificial Intelligence: The Ambiguous Labor Market
 Impact of Automating Prediction. Journal of Economic Perspectives 33 (2): 31–50.

Aseri, M., M. Dawande, G. Janakiraman, and V. S. Mookerjee. 2020. Ad-Blockers: A Blessing or a Curse?
 Information Systems Research 31 (2): 627–646.

Autor, D. H. 2015, August. Why Are There Still So Many Jobs? The History and Future of Workplace
 Automation. Journal of Economic Perspectives 29 (3): 3–30.

Brynjolfsson, E. 2022. The Turing Trap: The Promise and Peril of Human-Like Artificial Intelligence.
 Daedalus 151 (2): 272–287.

Brynjolfsson, E., B. Chandar, and R. Chen. 2025. Canaries in the Coal Mine? Six Facts about the Recent
 Employment Effects of Artificial Intelligence. Working Paper .

---

40 Incentive Issues in AI Deployment

Brynjolfsson, E., D. Li, and L. Raymond. 2025, May. Generative AI at Work. Quarterly Journal of Eco-
 nomics 140 (2): 889–942.

Brynjolfsson, E., and T. Mitchell. 2017, December. What Can Machine Learning Do? Workforce Implications.
 Science 358 (6370): 1530–1534.

Brynjolfsson, E., D. Rock, and C. Syverson. 2018, January. Artificial Intelligence and the Modern Productivity
 Paradox: A Clash of Expectations and Statistics, 23–57. University of Chicago Press.

Cadsby, C. B., F. Song, and F. Tapon. 2007, April. Sorting and Incentive Effects of Pay for Performance: An
 Experimental Investigation. Academy of Management Journal 50 (2): 387–405.

Chan, T. Y., J. Li, and L. Pierce. 2014, August. Compensation and Peer Effects in Competing Sales Teams.
 Management Science 60 (8): 1965–1984.

Eisfeldt, A. L., G. Schubert, and M. B. Zhang. 2023, May. Generative AI and Firm Values. Working Paper
 31222, National Bureau of Economic Research.

Eloundou, T., S. Manning, P. Mishkin, and D. Rock. 2023. GPTs are GPTs: An early look at the labor market
 impact potential of large language models. Arxiv working paper .

Felten, E., M. Raj, and R. Seamans. 2021, December. Occupational, Industry, and Geographic Exposure to
 Artificial Intelligence: A Novel Dataset and Its Potential Uses. Strategic Management Journal 42 (12):
 2195–2217.

Felten, E. W., M. Raj, and R. Seamans. 2018, May. A Method to Link Advances in Artificial Intelligence to
 Occupational Abilities. AEA Papers and Proceedings 108:54–57.

Fjelland, R. 2020, June. Why General Artificial Intelligence Will Not Be Realized. Humanities and Social
 Sciences Communications 7 (1): 1–9.

Frank, M. R., D. Autor, J. E. Bessen, E. Brynjolfsson, M. Cebrian, D. J. Deming, M. Feldman, M. Groh,
 J. Lobo, E. Moro, D. Wang, H. Youn, and I. Rahwan. 2019, April. Toward Understanding the Impact of
 Artificial Intelligence on Labor. Proceedings of the National Academy of Sciences 116 (14): 6531–6539.

Furman, J., and R. Seamans. 2019. AI and the Economy. Innovation Policy and the Economy 19:161–191.

Garnelo, M., and M. Shanahan. 2019, October. Reconciling Deep Learning with Symbolic Artificial Intelligence:
 Representing Objects and Relations. Current Opinion in Behavioral Sciences 29:17–23.

Gartner 2024. AI in HR: How AI Is Transforming the Future of HR. https://www.gartner.com/en/human-
 resources/topics/artificial-intelligence-in-hr.

Gerhart, B., and M. Fang. 2014, March. Pay for (Individual) Performance: Issues, Claims, Evidence and the
 Role of Sorting Effects. Human Resource Management Review 24 (1): 41–52.

---

 Incentive Issues in AI Deployment 41

Glikson, E., and A. W. Woolley. 2020. Human trus in artificial intelligence: Review of empirical research.
 Academy of Management Annals 14 (2): 627–660.

Gregory, R. W., M. Keil, J. Muntermann, and M. Mähring. 2015. Paradoxes and the nature of ambidexterity
 in IT transformation programs. Information Systems Research 26 (1): 57–80.

Groysberg, B., S. Abbott, M. R. Marino, and M. Aksoy. 2021, January. Compensation Packages That Actually
 Drive Performance. Harvard Business Review .

Hassin, R., and R. Roet-Green. 2020. On Queue-Length Information When Customers Travel to a Queue.
 Manufacturing & Service Operations Management 23 (4): 989–1004.

He, W., S.-L. Li, J. Feng, G. Zhang, and M. C. Sturman. 2021, February. When Does Pay for Performance
 Motivate Employee Helping Behavior? The Contextual Influence of Performance Subjectivity. Academy
 of Management Journal 64 (1): 293–326.

Heaven, W. D. 2020, October. Artificial General Intelligence: Are We Close, and Does It Even Make Sense
 to Try? https://www.technologyreview.com/2020/10/15/1010461/artificial-general-intelligence-robots-
 ai-agi-deepmind-google-openai/.

Iyer, G., and Z. Katona. 2016. Competing for Attention in Social Communication Markets. Management
 Science 62 (8): 2304–2320.

Kanazawa, K., D. Kawaguchi, H. Shigeoka, and Y. Watanabe. 2025. AI, Skill, and Productivity: The Case of
 Taxi Drivers. Management Science Articles in Advance (forthcoming).

Lazear, E. P. 2000. Performance Pay and Productivity. The American Economic Review 90 (5): 75.

Lazear, E. P. 2018, August. Compensation and Incentives in the Workplace. Journal of Economic Perspec-
 tives 32 (3): 195–214.

Levy, F. 2018, July. Computers and Populism: Artificial Intelligence, Jobs, and Politics in the Near Term.
 Oxford Review of Economic Policy 34 (3): 393–417.

Lohr, T., E. Brook, S. Chase, S. Krishna, M. Shank, P. Edin, B. McGowan, and E. Frolick. 2023, June.
 Generative AI: from buzz to business value. Technical report, KPMG.

Lucas Jr, R. E. 1972. Expectations and the Neutrality of Money. Journal of Economic Theory 4 (2): 103–124.

McKinsey Global Institute 2018, June. AI, Automation, and the Future of Work: Ten Things to
 Solve For. https://www.mckinsey.com/featured-insights/future-of-work/ai-automation-and-the-future-
 of-work-ten-things-to-solve-for.

Mele, C., M. Marzullo, S. Morande, and T. R. Spena. 2022. How Artificial Intelligence Enhances Human
 Learning Abilities: Opportunities in the Fight Against COVID-19. Service Science:14.

---

42 Incentive Issues in AI Deployment

Microsoft 2025. Wellbeing and Productivity Tools. https://www.microsoft.com/en-us/microsoft-viva/insights.

Mitchener, L., D. Tuckey, M. Crosby, and A. Russo. 2022, April. Detect, Understand, Act: A Neuro-symbolic
 Hierarchical Reinforcement Learning Framework. Machine Learning 111 (4): 1523–1549.

Noy, S., and W. Zhang. 2023. Experimental evidence on the productivity effects of generative artificial intel-
 ligence. Science 381 (6654): 187–192.

Rai, A., P. Constantinides, and S. Sarker. 2019, March. Next Generation Digital Platforms: Toward Human-AI
 Hybrids. MIS Quarterly 43 (1): iii–ix.

Ramasubbu, N., and C. F. Kemerer. 2016. Technical Debt and the Reliability of Enterprise Software Systems:
 A Competing Risks Analysis. Management Science 62 (5): 1487–1510.

Ransbotham, S., D. Kiron, P. Gerbert, and M. Reeves. 2017. Reshaping business with artificial intelligence:
 Closing the gap between ambition and action. MIT Sloan Management Review 59 (1): 1–17.

Raveendran, M., P. Puranam, and M. Warglien. 2021. Division of Labor Through Self-Selection. Organization
 Science 33 (2): 810–830.

Rubel, O., and A. Prasad. 2016, July. Dynamic Incentives in Sales Force Compensation. Marketing Science 35
 (4): 676–689.

Senoner, J., T. Netland, and S. Feuerriegel. 2021, December. Using Explainable Artificial Intelligence to
 Improve Process Quality: Evidence from Semiconductor Manufacturing. Management Science.

Solon, O. 2018, January. Amazon Patents Wristband that Tracks Warehouse Workers’ Movements.
 https://www.theguardian.com/technology/2018/jan/31/amazon-warehouse-wristband-tracking.

Srivastava, V. 2023, November. Evolution of AI in Salesforce Ecosystem (2014 to 2025).

Stroh, L. K., J. M. Brett, J. P. Baumann, and A. H. Reilly. 1996, June. Agency Theory and Variable Pay
 Compensation Strategies. Academy of Management Journal 39 (3): 751–767.

Sun, J., D. J. Zhang, H. Hu, and J. A. V. Mieghem. 2025. Predicting Human Discretion to Adjust Algorithmic
 Prescription: A Large-Scale Field Experiment in Warehouse Operations. Management Science Articles
 in Advance (forthcoming).

Verma, A. 2024. Use of Data Analytics by Uber to Enhance Supply Efficiency and Service Qual-
 ity. https://www.pickl.ai/blog/use-of-data-analytics-by-uber-to-enhance-supply-efficiency-and-service-
 quality/.

Wang, H., Y. Zhang, H. Hu, and T. Lu. 2025. The Power of Disagreement: A Field Experiment to Investi-
 gate Human–Algorithm Collaboration in Loan Evaluations. Management Science Articles in Advance
 (forthcoming).

---

 Incentive Issues in AI Deployment 43

Webb, M. 2020. The Impact of Artificial Intelligence on the Labor Market. Working Paper,
 https://dx.doi.org/10.2139/ssrn.3482150 .

Yang, C., K. Bauer, X. Li, and O. Hinz. 2025. My Advisor, Her AI, and Me: Evidence from a Field Experi-
 ment on Human–AI Collaboration and Investment Decisions. Management Science Articles in Advance
 (forthcoming).

Zhou, Y. M. 2013. Designing for Complexity: Using Divisions and Hierarchy to Manage Complex Tasks.
 Organization Science 24 (2): 339–355.

Zolas, N., Z. Kroff, E. Brynjolfsson, K. McElheran, D. Beede, C. Buffington, N. Goldschlag, F. Lucia, and
 E. Dinlersoz. 2020, December. Advanced technologies adoption and use by U.S. firms: Evidence from
 the annual business survey. NBER Working paper 28290.

---

44 Incentive Issues in AI Deployment

Appendix A Proofs
A.1 Proof of Lemma 1

Employee’s utility maximization under the general ability level (at , ai ) and salary rate γ is:
  2
 wt wi2
 
 max u = max γ (βt wt + βi wi ) − + .
 wt ,wi wt ,wi at ai
Take first-order conditions with respect to the labor decision wt &wi :
 ∂u 2wt
 =− + βt γ = 0
 ∂wt at
 ∂u 2wi
 =− + βi γ = 0
 ∂wi ai
 We also check the second-order condition:
 One can easily see that the Hessians are negative definite as the second-order conditions are
negative.
 The equilibrium employee decisions, the output level, and net utility are:
 1 1
 wt∗ = βt at γ, wi∗ = βi ai γ
 2 2
 ∗ ∗ ∗ 1 2
 βt at + βi2 ai γ
 
 o = βt wt + βi wi =
  ∗ 2 2 ∗ 2
 (wt ) (w ) 1 2
 u∗ = γo∗ − + i βt at + βi2 ai γ 2
 
 =
 at ai 4
 

A.2 Proof of Lemma 2 and Table 4

Under the competition for the bonus salary, employees make their choices of labor by maximizing
the final output under the bonus rate as long as the net utility is higher than that under the base
salary. The optimization under the general ability level (at , ai ) is,

 max βt wt + βi wi
 wt ,wi

 wt2 wi2
  
 1 2
 βt at + βi2 ai γ 2
 
 s.t. γB (βt wt + βi wi ) − + ≥
 at ai 4
 Construct the Lagrangian as follows:
  2
 wt wi2
   
 1 2 2
  2
 L = βt wt + βi wi + λ γB (βt wt + βi wi ) − + − βt at + βi ai γ
 at ai 4
 With the following FOCs:
  
 ∂L 2wt
 = βt + − + βt γB λ = 0
 ∂wt at
  
 ∂L 2wi
 = βi + − + βi γB λ = 0
 ∂wi ai
  2
 wt wi2
 
 ∂L 1
 + βt2 at + βi2 ai γ 2 − γB (βt wt + βi wi ) = 0
 
 = +
 ∂λ at ai 4

---

 Incentive Issues in AI Deployment 45

 We can obtain two sets of possible optimal value of (wt∗ , wi∗ , λ∗ ) to be
 p  p 
 βt at γB + γB2 − γ 2 βi ai γB + γB2 − γ 2 1
 ( , ,p 2 ) and
 2 2 γB − γ 2
 p  p 
 βt at γB − γB2 − γ 2 βi ai γB − γB2 − γ 2 1
 ( , ,−p 2 )
 2 2 γB − γ 2
By checking the condition of the bordered Hessian, we find that solution set 1 meets the
criteria of the maximum point. Therefore, the highest possible output from an employee
 
is o∗ = βt wt∗ + βi wi∗ = 12 (βt2 at + βi2 ai ) γB + γB2 − γ 2 .
 p

 Next, we show the employees’ performance ranking and each type’s production decisions. For
HH, LH, and LL types, each produces at the natural output level as specified in Lemma 1. For
HL employees, they need to produce at the LH’s maximum level oLH
 max to maintain its second place.

Hence, HL faces the following problem:
 wt2 wi2
 min + L
 wt ,wi aHt ai
 s.t. βt wt + βi wi = oLH
 max

 The optimal decisions are
 βt aHt K1 βt2 aLt + βi2 aHi βi aLi K1 βt2 aLt + βi2 aHi
 wt∗ = , wi∗ =
 2 βt2 aHt + βi2 aLi 2 βt2 aHt + βi2 aLi
 

A.3 Proof of Proposition 1
From the breakdown of productivity change by employee type, we have:

 ∆oHH =0,

 ∆oHL = oHL
 γ
 − oLH
 max ,
 | {z }
 Competition Effect

 ∆oLH =oHL
 max − oγ ,
 LH

    
 = oHL
 max − o LH
 γ
 + o LH
 γ
 AI
 − o LH
 γ
 , AI

 | {z } | {z }
 Competition Effect Learning Effect
 LL
 ∆o = o LLAI
 γ
 −o . LL
 γ
 | {z }
 Learning Effect

 In the environment that we are interested in, HL naturally ranks over LH before AI, ranking
swaps after AI, and there is intensified competition between them. We have oHL
 γ < oHL
 γ < oLH
 max and B

 LHAI LHAI HL
o γ < oγ B
 < omax . Therefore, the competition effect is negative on HL and positive on LH. Because
learning effect is always positive, we have ∆oHL < 0 and ∆oLH > 0.

---

46 Incentive Issues in AI Deployment

A.4 Proof of Theorem 1
We first compare the firm’s productivity before and after AI (OAI − OnoAI ):

 (oHL
 γ
 − oLH HL
 max )pHL + (omax − oγ )pLH + (oγ
 LH LL
 − oLL
 γ
 ), AI

 or it can be simplified as

 ∆oHL pHL + ∆oLH pLH + ∆oLL pLL .

 For this expression to be negative, we derive the condition in terms of aHt − aLt and pHL as
 HH HL HL HH
 (omax −oγ )pHL −(omax −oγ )pLH (o) ∆oLH pLH +∆oLL pLL
â(o) = 2 βt2 (KpHL +γpLH +f γpLL )
 and p̂HL = ∆oHL
 .
 Similarly, we derive the parameter condition for πAI − πnoAI < 0 with respect to aHt − aLt and pHL as
 HH HL HL HH
 (M2 omax −M1 oγ )pHL −(M2 omax −M1 oγ )pLH (π) ∆π LH pLH +∆π LL pLL
â(π) = 2 βt2 (M2 KpHL +M1 γpLH +M1 f γpLL )
 and p̂HL = ∆π HL
 . 

A.5 Proof of Proposition 2
Employee’s utility for those who rank first, third, and last follows the natural utility identified before.
That is, before AI:
 1 2 H 1 2 L 1 2 L
 βt at + βi2 aHi γB2 , uLH = βt at + βi2 aHi γ 2 , uLL = βt at + βi2 aLi γ 2 ;
   
 uHH =
 4 4 4
 After AI:
 1 2 H 1 2 H 1 2 L
 βt at + βi2 aHi γB2 , uHL = βt at + βi2 aLi γ 2 , uLL = βt ate + βi2 aLi γ 2 .
   
 uHH =
 4 4 4
 For the utility for the ones at rank 2, we need to solve their decision by minimizing the cost with
an output constraint. For example, for the HL type’s decision before AI:
  2
 wt wi2
 
 min +
 wt ,wi aHt aLi
 p
 γB + γB2 − γ 2 2 L
 βt at + βi2 aHi .
 
 s.t. βt wt + βi wi =
 2
 Solving for the employees’ decision, we derive for the utility of HL before AI to be
 !
 (γB + γB2 − γ 2 )(βt2 aLt + βi2 aHi )γB (γB + γB2 − γ 2 )(βt2 aLt + βi2 aHi )
 p p
 2γB − .
 4 βt2 aHt + βi2 aLi
 It is straightforward to see that this utility is higher than the after-AI value. 

A.6 Proof of Proposition 3
Compare the profit under the guaranteed salary to that under :
 g
 πAI − πnoAI = (M2 oLH
 γ
 − M1 oLH
 γB
 )pLH + M2 (oHL
 AI
 γ
 − oLH LL
 max )pHL + M1 (oγ B
 − oLL
 γ
 ). AI

 g
 We can easily derive the thresholds for πAI − πnoAI < 0 in terms of tangible skill gap aHt − aLt and pHL
 HH HL HH HH LHAI LH LL LL
 M2 (o −oγ )pHL +(M1 oγ −M2 oγ )pLH (g) (M2 oγ −M1 oγ )pLH +M1 (oγ AI −oγ )pLL
as â(g) = 2 β 2 [M Kmax B

 p +(M γ−M γ [1−f ])p
 B
 and p̂HL = B
 LH HL . 
 t 2 1 HL 1 2 B LH +M1 f γpLL ] M2 (omax −oγ )
 B

---

 Incentive Issues in AI Deployment 47

A.7 Proof of Proposition 4
Compare the profit under the guaranteed salary to that under the base reward policy:

 g ng
 πAI − πAI = M2 (oLH
 γ
 − oHL
 max )pLH + (M2 oγ − M1 oγ )pHL .
 B
 HL
 AI HL
 B

 Because the first term (oLH
 γ B
 AI
 − oHL
 max ) < 0, the overall value can only be positive when

(1 − γB )γB > (1 − γ)γ. Therefore, we can see that (1 − γB )γB < (1 − γ)γ is a sufficient condition for
 g ng
πAI < πAI . 

A.8 Proof of Proposition 5 and 6
The upper threshold of AI effectiveness fˆ(u) is that the HL’s maximum output is still
lower than LH’s
 q
 natural output with the expectation of receiving the bonus. That is, fˆ(u)
 γB + 2 −γ 2
 γB γB
satisfies 2
 (βt2qaHt + βi2 aLi ) = 2
 ((βt2 aLte + βi2 aHi )), with aLte = aLt + (aHt − aLt )fˆ(u) . Hence,
 2 −γ 2 (β 2 aH +β 2 aL )
 βi2 (ai −ai )
 H L
 γB
fˆ(u) = 1 − β 2 aH −aL +
 t t i i
 H L .
 t( t t) γB βt2 (at −at )

 From Equation (13), we can see that the profit is increasing in f under each case; therefore, we
have two candidates for the maximum value as
 h γ 2 H  i
 πAI (fˆ(l) ) = M2 (oHH p + o HL
 p ) + M 1 o HL
 p + β a − β 2
 (a H
 − 2a L
 ) pLL ,
 2 t t i i i
 γ HH max HL
 B γ LH

 πAI (1) = M2 oHH
 γ
 (pHH + pLH ) + M1 oHL
 B γ
 (pHL + pLL ).

 Compare these two values and derive the condition for πAI (fˆ(l) ) > πAI (1) in terms of pHL , we get
 γ
 −M1 oγ )pLH +M1 2 βi2 (ai −ai )pLL
 HH HL H L
 (f ) (M2 oγ
the threshold p̂HL = B
 HL HL
 M2 omax −M1 oγ
 .

 β 2 (a −a )
 H L

 When the optimal level of AI is hatf (l) = 1 − βi2 aiH −aiL , we can see that this value is decreasing
 t( t t)

in (aHi − aLi ) and increasing in (aHt − aLt ). 

A.9 Strategic Hiring
With the firm’s maximization over the level of high-tangible ability employees:
 h i h i c
max πnoAI = max (1 − γB ) oγ pi + omax (1 − pi ) pt + (1 − γ) oγ pi + oγ (1 − pi ) (1 − pt ) − (pt − p̄t )2
 HH LH LH LL

 pt pt B
 2
 h i h i c
 max πAI = max (1 − γB ) oHH
 γ
 pt + oHL
 max (1 − pt ) pi + (1 − γ) oγ pt + oγ
 HL LL
 (1 − pt ) (1 − pi ) − (pt − p̄t )2
 AI

 pt pt B
 2
We can obtain the optimal levels:
 (M2 oHH
 γ − M1 oLH LH LL
 γ )pi + (M2 omax − M1 oγ )(1 − pi )
 pnoAI
 t = B
 + p̄t ,
 c
 M2 (oHH
 γ − oHL HL
 max )pi + M1 (oγ − oγ
 LL
 )(1 − pi ) AI

 pAI
 t = B
 + p̄t ,
 c

---

48 Incentive Issues in AI Deployment

 Take the derivatives of the optimal values, we can see that the firm should hire after AI adoption
 AI
 ∂pt
(pAI
 t ) decreases when AI effectiveness f increases or the ability gap narrows. That is, ∂f
 < 0 and
 AI
∂pt
∂at
 L < 0:

 ∂pAI
 t aHt − aLt
 =− < 0,
 ∂f c
 ∂pAI
 t aL (1 − f )
 L
 =− t < 0.
 ∂at c
 

A.10 Generalized Model of AI
We identify the equilibrium under each case:
 Case 1 - without flipping
 Without flipping, LH produces at the natural output level with the expected salary at the base
rate, and HL produces at the LH’s maximum level. Thereby, the rational expectation of AI efficacy
follows:
 βt2 aLte + βi2 aHi
  
 θ
 f = f0 + (1 − f0 ) γB pi + K1 2 H (1 − pi ) .
 γ̄ βt at + βi2 aLi
 The equilibrium value of AI efficacy, denoted as F1 (f0 , θ) is:
 γ̄A2 f0 + (1 − f0 )[γB A2 pi + K1 A3 (1 − pi )]θ
 F1 (f0 , θ) = .
 γ̄A2 − (1 − f0 )K1 βt2 (aHt − aLt )(1 − pi )θ
 Case 2
 To determine HL’s output level, we first find out its tangible labor decision wtHL that can make
HL and LH have the same productivity level; that is, wtHL satisfies:

 βt2 aHt + βi2 aLi = βt2 aLte + βi2 aHi
 γB βt aHt pi + 2wtHL (1 − pi )
   
 2 H 2 L 2 L H L
 βt at + βi ai = βt at + (at − at ) f0 + (1 − f0 )θ + βi2 aHi
 γ̄βt aHt
 Next, the HL’s intangible labor is to maximize its utility, with wtHL identified as above:
  HL 2
 wi2
 
 (wt )
 max u = γB βt wtHL + βi wi −
 
 +
 wi aHt aLi
 (aHi − aLi )βi2
    
 HL βt aHt γ̄
 s.t. wt = 1− H − γB pi
 2(1 − pi ) θ (at − aLt )βt2 (1 − f0 )
 L
 γB βi ai
 The solution for HL’s intangible labor decision wiHL is 2
 . Next, we identify the threshold for
f0 . The above solution for HL’s utility shows that this value is decreasing in f0 . Therefore, HL will
keep a lower wtHL as f0 increases till the utility is no better than staying at third place. Hence, we
can find the condition for f0 from the following inequality:
 (wiHL )2
  HL 2 
 (wt ) 1 2 H
 γB βt wtHL + βi wiHL − βt at + βi2 aLi γ 2 .
  
 H
 + L
 ≥
 at ai 4

---

 Incentive Issues in AI Deployment 49

 Case 3 - with flipping
 Under this scenario, all employees produce at their natural output level with HH & LH expecting
the bonus and HL & LL expecting the base salary. Therefore, the equilibrium AI efficacy F3 (f0 , θ)
is:
 γB pi + γ(1 − pi )
 F3 (f0 , θ) = f0 + (1 − f0 )θ .
 γ̄
 

A.11 Proof of Lemma 3 & Proposition 7
The productivity, as measured by the total final output, is
 2
 (A1 pHH + A3 [DpHL + δpLH ] + A4 δpLL )
 OnoAI = ,
 4 (A1 pHH + A3 [DpHL + δ 2 pLH ] + A4 δ 2 pLL )
 2
 (A1 pHH + A2 [DpLH + δpHL ] + A6 δpLL )
 OAI = .
 4 (A1 pHH + A2 [DpLH + δ 2 pHL ] + A6 δ 2 pLL )
The firm’s profit is
 2
 (A1 pHH + A3 [DpHL + δpLH ] + A4 δpLL )
 πnoAI = ,
 8 (A1 pHH + A3 [DpHL + δ 2 pLH ] + A4 δ 2 pLL )
 2
 (A1 pHH + A2 [DpLH + δpHL ] + A6 δpLL )
 πAI = .
 8 (A1 pHH + A2 [DpLH + δ 2 pHL ] + A6 δ 2 pLL )
The total salary paid to the employees (denoted as S):
 2
 (A1 pHH + A3 [DpHL + δpLH ] + A4 δpLL )
 SnoAI = ,
 8 (A1 pHH + A3 [DpHL + δ 2 pLH ] + A4 δ 2 pLL )
 2
 (A1 pHH + A2 [DpLH + δpHL ] + A5 δpLL )
 SAI = .
 8 (A1 pHH + A2 [DpLH + δ 2 pHL ] + A5 δ 2 pLL )
 From these equilibrium values, it is easy to observe that the total economic value generated from
the production, measured as the total productivity, is allocated at a fixed rate between the firm (as
π) and the employees (the total salary paid S). That is, π = O2 and S = O2 . Hence, when the total
productivity drops after AI (OAI < OnoAI ), the firm’s profit and total salary also decrease. 

---
