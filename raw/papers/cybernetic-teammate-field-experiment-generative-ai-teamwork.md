---
title: "The Cybernetic Teammate: A Field Experiment on Generative AI and Teamwork"
authors: ["Fabrizio Dell'Acqua", "Charles Ayoubi", "Hila Lifshitz", "Raffaella Sadun", "Ethan Mollick", "Lilach Mollick", "Yi Han", "Jeff Goldman", "Hari Nair", "Stew Taub", "Karim R. Lakhani"]
venue: "Organization Science 37(4):1217-1242 (2026), INFORMS"
doi: "10.1287/orsc.2025.20702"
url: "https://doi.org/10.1287/orsc.2025.20702"
date_published: 2026-01-01
license: CC BY 4.0
attachment: cybernetic-teammate-field-experiment-generative-ai-teamwork.pdf
fulltext_source: pdf-converted
converter: "pdftotext -layout"
notes: |
  Acquired 2026-09-15 from a PDF the user placed in raw/articles/. **Routing corrected at
  Process time**: peer-reviewed Organization Science article — moved to raw/papers/.
  27 pages; `pdftotext -layout`, column padding collapsed, page breaks as `---`. The INFORMS
  download banner and licence block on p.1 are retained verbatim. Figures absent; tables survive
  as whitespace-aligned text and should be read against the PDF where alignment matters.
  Distinct from the Dell'Acqua paper already in the corpus
  (wiki/sources/2026-04-28-dellacqua-jagged-technological-frontier.md, the BCG jagged-frontier
  study) — same first author, different experiment (Procter & Gamble, teams rather than individuals).
---

This article was downloaded by: [2a02:a456:278c:0:d04a:3b49:409a:335c] On: 14 September 2026, At: 22:32
Publisher: Institute for Operations Research and the Management Sciences (INFORMS)
INFORMS is located in Maryland, USA

 Organization Science
 Publication details, including instructions for authors and subscription information:
 http://pubsonline.informs.org

 The Cybernetic Teammate: A Field Experiment on
 Generative AI and Teamwork
 Fabrizio Dell’Acqua, Charles Ayoubi, Hila Lifshitz, Raffaella Sadun, Ethan Mollick,
 Lilach Mollick, Yi Han, Jeff Goldman, Hari Nair, Stew Taub, Karim R. Lakhani

To cite this article:
Fabrizio Dell’Acqua, Charles Ayoubi, Hila Lifshitz, Raffaella Sadun, Ethan Mollick, Lilach Mollick, Yi Han, Jeff
Goldman, Hari Nair, Stew Taub, Karim R. Lakhani (2026) The Cybernetic Teammate: A Field Experiment on
Generative AI and Teamwork. Organization Science 37(4):1217-1242. https://doi.org/10.1287/orsc.2025.20702

This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy,
distribute, transmit and adapt this work, but you must attribute this work as “Organization Science. Copyright ©
2026 The Author(s). https://doi.org/10.1287/orsc.2025.20702, used under a Creative Commons Attribution License:
https://creativecommons.org/licenses/by/4.0/.”

 Copyright © 2026 The Author(s)

Please scroll down for article—it is on subsequent pages

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations
research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning
opportunities for individual professionals, and organizations of all types and sizes, to better understand and use
O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.
For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

---

 ORGANIZATION SCIENCE
 Vol. 37, No. 4, July–August 2026, pp. 1217–1242
 https://pubsonline.informs.org/journal/orsc ISSN 1047-7039 (print), ISSN 1526-5455 (online)

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 The Cybernetic Teammate: A Field Experiment on Generative
 AI and Teamwork
 Fabrizio Dell’Acqua,a,b,* Charles Ayoubi,c Hila Lifshitz,b,d Raffaella Sadun,a,b Ethan Mollick,e Lilach Mollick,e Yi Han,f
 Jeff Goldman,f Hari Nair,f Stew Taub,f Karim R. Lakhania,b
 a
 Harvard Business School, Harvard University, Boston, Massachusetts 02134; b HBS AI Institute, Harvard University, Boston, Massachusetts
 02163; c ESSEC Business School, 95000 Cergy, France; d Warwick Business School, University of Warwick, Coventry CV4 7AL, United
 Kingdom; e The Wharton School, University of Pennsylvania, Philadelphia, Pennsylvania 19104; f Procter & Gamble, Cincinnati, Ohio 45202
 *Corresponding author
 Contact: fdellacqua@hbs.edu, https://orcid.org/0000-0002-1998-0542 (FDA); ayoubi@essec.edu, https://orcid.org/0000-0002-0752-3328 (CA);
 hdiginnovation@gmail.com, https://orcid.org/0000-0002-3461-003X (HL); rsadun@hbs.edu, https://orcid.org/0000-0002-0987-8923 (RS);
 emollick@wharton.upenn.edu, https://orcid.org/0000-0001-6231-496X (EM); lmollick@wharton.upenn.edu (LM); han.y.7@pg.com (YH);
 goldman.js@pg.com (JG); nair.h.1@pg.com (HN); taub.sl@pg.com (ST); klakhani@hbs.edu, https://orcid.org/0000-0002-5535-8304 (KRL)

 Received: June 3, 2025 Abstract. We examine how artificial intelligence (AI) impacts three core pillars of
 Revised: November 17, 2025; March 26, 2026 collaboration—performance enhancement, expertise integration, and social engagement—
 Accepted: April 1, 2026 through a preregistered field experiment with 791 professionals at Procter & Gamble, a
 Published Online in Articles in Advance: global consumer packaged goods company. Working on real product innovation chal­
 June 12, 2026 lenges, professionals were randomly assigned to work either with or without AI, and either
 individually or with another professional in new product development teams. Our find­
 https://doi.org/10.1287/orsc.2025.20702 ings show that (1) AI significantly enhances performance: individuals with AI matched the
 performance of teams without AI, suggesting that AI can effectively replicate certain bene­
 Copyright: © 2026 The Author(s)
 fits of human collaboration. Moreover, (2) AI helps bridge functional silos: without AI,
 research and development professionals tended to suggest more technical solutions,
 whereas commercial professionals leaned toward commercially oriented proposals. Profes­
 sionals using AI produced more balanced solutions, regardless of their professional back­
 ground. (3) AI’s language-based interface prompted more positive self-reported emotional
 responses among participants, suggesting it can fulfill part of the social and motivational
 role traditionally offered by human teammates. Finally, decomposing the innovation pro­
 cess suggests that AI primarily enhances the quality of generated ideas, shifting the distri­
 bution of creative output upward, whereas human judgment retains value in evaluative
 selection. This finding highlights the multiple and complementary roles that human and
 AI partners can play in new product development tasks and creative problem solving.
 More generally, our results suggest that AI adoption in knowledge work affects not only
 performance but also how expertise and sociality appear within teams, offering insights
 into the impact of generative AI on collaborative work within organizations.

 Open Access Statement: This work is licensed under a Creative Commons Attribution 4.0 International
 License. You are free to copy, distribute, transmit and adapt this work, but you must attribute this
 work as “Organization Science. Copyright © 2026 The Author(s). https://doi.org/10.1287/orsc.2025.
 20702, used under a Creative Commons Attribution License: https://creativecommons.org/licenses/
 by/4.0/.”
 Funding: Funding for this research was provided in part by Harvard Business School.
 Supplemental Material: The online appendix is available at https://doi.org/10.1287/orsc.2025.20702.

 Keywords: technology and innovation management • research design and methods • field experiments • implementation of new technology •
 organization and management theory • organizational processes • economics and organization • organizational economics

 1. Introduction performance: teamwork is often more effective than
 Teamwork is central to modern organizations. Whether individual work and allows for more complex pro­
 designing a new product, solving strategic challenges, blems to be tackled (Ancona and Caldwell 1992, Lind­
 or supporting impactful innovation, human collabora­ beck and Snower 2000, Deming 2017, Weidmann and
 tion has often been associated with higher-quality Deming 2020). The second is expertise sharing and
 results than individuals working alone (Wuchty et al. knowledge complementarities: teamwork allows people
 2007, Singh and Fleming 2010). There are three main with different expertise to come together and work on
 pillars commonly used to justify teamwork. The first is the same problem effectively (Kogut and Zander 1992,

 1217

---

 Dell’Acqua et al.: The Cybernetic Teammate
 1218 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s)

 Argote 1999, Faraj and Sproull 2000, Nickerson and Gamble (P&G), a global consumer packaged goods
 Zenger 2004). Finally, there is human sociality: people company with roughly 7,000 research and development

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 often enjoy connecting with other people, which can (R&D) professionals worldwide. The experiment was
 increase their motivation to work (Deutsch 1949, John­ developed in close collaboration with the company
 son and Johnson 2005, Kozlowski and Bell 2013). In over the course of a year, requiring sustained coordina­
 this paper, we investigate how the introduction of artifi­ tion with senior leadership to design a protocol that
 cial intelligence (AI) impacts these three pillars of team­ mirrored the company’s actual new product develop­
 work in the context of a field experiment in a large ment routines. R&D and commercial professionals ded­
 organization. icated a full working day to the study, engaging with
 The integration of AI into knowledge work poses real, long-standing business challenges from their own
 an important challenge: although AI, particularly gen­ units, not hypothetical tasks. Participation carried real
 erative AI (GenAI), has demonstrated the capacity to professional stakes: the best proposals would be pre­
 enhance individual creativity, productivity, and deci­ sented to business unit leaders. The evaluation process
 sion making (Dell’Acqua et al. 2023, Noy and Zhang was based on assessments by multiple independent
 2023, Peng et al. 2023, Brynjolfsson et al. 2025), its evaluators, without time constraints, under a protocol
 ramifications for team-based collaboration remain validated by P&G managers. The best ideas generated
 largely unexplored. Prior work has treated AI primar­ were of sufficient quality to enter the company’s actual
 ily as a tool, like a spreadsheet or calculator, that can innovation pipeline. The resulting data set is grounded
 be used to enhance individual performance. But a in existing business problems, within the company’s
 unique aspect of large language models (LLMs), the core organizational processes, and with strong profes­
 most common form of GenAI, is that they are trained sional incentives.
 on human language and often act more like a person Our participants were randomly assigned to one of
 than a machine (Mollick 2024). This leads to a key ques­ four conditions, in a 2 × 2 experimental design: (1) an
 tion: Can GenAI fill some of the roles of humans in individual working without GenAI, (2) a team of
 teamwork in specific collaborative contexts? We exam­ two humans without GenAI, (3) individuals with
 ine this by moving past considering AI as a mere tool, GenAI, and (4) a team of two humans plus GenAI.
 but instead ask whether it can provide some of the All teams comprised one commercial professional
 same benefits of human teamwork, namely, collective and one R&D professional, ensuring authentic cross-
 performance, expertise sharing, and social connection. functional collaboration that reflects real-world orga­
 Understanding these dimensions has profound impli­ nizational structures.1 Each individual or team was
 cations for organizational learning and innovation strat­ assigned to develop a new solution to address a real
 egies. As companies integrate GenAI into day-to-day business need for their business unit, ensuring they
 work (Bick et al. 2026), its influence may extend beyond could leverage their domain expertise on the business
 one-off productivity gains: it may affect how knowledge needs they regularly target in their work. The build-
 is shared and recombined across functional lines and up of teams working on early-stage specific product
 how knowledge workers experience their work. By development problems resembles “flash teams” (Val­
 examining AI as a potential collaborator rather than entine and Bernstein 2025) and enables precise causal
 simply a tool, our research considers how these tech­ identification while remaining embedded within the
 nologies might affect knowledge work by facilitating organization.
 knowledge diffusion, reducing functional silos, and Within this framework, we focus on three main out­
 creating more positive emotional experiences during comes that map onto the pillars of teamwork. First, we
 innovation activities—all factors that may matter for examine performance: Can AI help people produce
 organizational learning. high-quality work in innovative product development,
 To do so, we designed a field experiment exploring potentially with better ideas or more thorough explo­
 three main dimensions. (1) Does GenAI provide the ration of solutions? Second, we look at expertise: Does
 performance gains traditionally attributed to team­ AI enable participants to breach typical functional
 work? (2) Does GenAI enable a broadening of expertise boundaries—for instance, allowing R&D professionals
 even when employees lack some specialized knowl­ to produce commercially viable ideas or commercial
 edge? Finally, (3) can GenAI offer the kind of social professionals to propose technically sound solutions?
 engagement that we typically associate with human Third, we measure human sociality. Although this can
 collaboration? Put simply, to what extent can AI be take many forms, we operationalize it as the emotional
 treated as a “cybernetic teammate,” rather than as yet dimensions of the collaborative experience. Specifi­
 another software tool? cally, we ask, To what extent does AI actually affect
 Our research addresses these questions through a emotional experiences—such as excitement, engage­
 field experiment and organizational upskilling program ment, or frustration—that traditionally emerge from
 involving 791 experienced professionals at Procter & human-to-human interaction?

---

 Dell’Acqua et al.: The Cybernetic Teammate
 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s) 1219

 Our findings show that AI reproduces some of the team workflows. Unlike previous technologies that
 benefits of human collaboration, acting as a cybernetic primarily automated routine tasks, GenAI’s capacity

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 teammate.2 Individuals with AI produce solutions at a to converse, reason, and create positions it less as a
 quality level comparable to two-person teams, indicat­ passive tool and more as a cybernetic teammate
 ing that AI can indeed stand in for certain collabora­ whose presence alters team design, as it can be con­
 tive functions. The adoption of AI also broadens the ceptualized as an active participant in collaborative
 user’s reach in areas outside their core expertise. processes. This perspective requires organizations to
 Workers without deep product development experi­ consider the complex dynamics of human–AI team
 ence, for example, can leverage AI’s suggestions to integration, drawing on what we know about effective
 bridge gaps in knowledge or domain understanding, team functioning—including knowledge sharing and
 reproducing some of the knowledge integration typi­ human sociality. Additionally, the introduction of
 cally achieved through human collaboration. This GenAI as a teammate may significantly impact orga­
 has the potential to diminish functional boundaries, nizational learning trajectories, potentially restructur­
 improving access to expertise within teams and orga­ ing how knowledge is created and retained within
 nizations. Moreover, professionals reported more pos­ teams.
 itive emotions and fewer negative emotions when
 engaging with AI compared with working alone, 2.1. Teamwork
 echoing some of the emotional benefits traditionally The nature of knowledge work is becoming ever more
 associated with human teamwork. This pattern differs collaborative (Lazer and Katz 2003, Deming 2017, Pur­
 from previous findings about technology’s typically anam 2018). Teamwork forms the backbone of mod­
 negative impact on workplace social dynamics. ern organizations for multiple reasons, but foremost
 We also examine how AI affects the innovation pro­ among them is performance. A wide range of scholar­
 cess itself. New product development involves multi­ ship shows that collaboration can outperform indi­
 ple stages—generating ideas, selecting among them, vidual effort in organizations by integrating multiple
 and developing chosen concepts into detailed solu­ perspectives, thereby tackling complex problems
 tions. By analyzing performance at each stage, we find more effectively (Ancona and Caldwell 1992, Cohen
 that AI’s benefits stem primarily from enhancing idea and Bailey 1997, Csaszar 2012). Although collabora­
 tive production creates unique organizational chal­
 generation quality rather than improving selection
 lenges (Alchian and Demsetz 1972), Cohen and Bailey
 accuracy. AI shifts the distribution of creative output
 (1997) highlight that well-structured teamwork can
 upward, producing better ideas from the outset while
 mobilize broad-based knowledge under high task
 preserving variance in outcomes. This pattern sug­
 complexity. In the same vein, Csaszar (2012) demon­
 gests AI functions as a quality amplifier in collabora­
 strates how collective decision making reduces errors
 tive work, improving the raw material of innovation
 by drawing on a wider range of input.
 while human evaluative judgment continues to play a
 These performance advantages have been shown to
 role in identifying the most promising concepts. These
 stem from the synergy that arises when team mem­
 findings may help motivate future research on more
 bers share real-time feedback, pool different skill sets,
 elaborate collaborations within organizations.
 and engage in collective problem solving (DiBenigno
 Overall, our findings indicate that adopting AI in
 and Kellogg 2014, Page 2019). Such interplay curtails
 knowledge work involves more than simply adding
 blind spots, encourages scrutiny of multiple viewpoints,
 another tool. By enhancing performance, blurring func­ and fosters collaborative creativity. By distributing
 tional boundaries, and altering emotional experiences, workload and leveraging complementary skills, collabo­
 the introduction of GenAI into organizations may rative teamwork adapts fluidly to shifting requirements,
 affect how organizations structure teams and define ultimately producing more robust results than isolated
 individual roles. As firms integrate AI technologies contributors could achieve on their own.
 more widely, they must consider not only operational Beyond raw performance, a second key rationale
 efficiencies but also emotional and social implications for teamwork is the sharing of expertise across func­
 for workers. Our study provides a basis for under­ tional or disciplinary boundaries (Ayoubi et al. 2017).
 standing these shifts and offers insights that may help A central tenet of the knowledge-based view is
 inform the design of AI-enhanced work environments, that specialized knowledge resides in individuals and
 where AI can play an active collaborative role. must be integrated to solve complex problems. Kogut
 and Zander (1992) show how recombining distinct
 2. Theoretical Background skill sets can spur innovation, whereas Nickerson and
 Organizations face a critical implementation chal­ Zenger (2004) emphasize that problem solving often
 lenge with the emergence of GenAI: how to effec­ demands multiple domains of expertise working in
 tively integrate this powerful new technology into tandem. Argote (1999), in turn, suggests that teams

---

 Dell’Acqua et al.: The Cybernetic Teammate
 1220 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s)

 are the primary locus of learning and knowledge highlighting gains in productivity, creativity, and deci­
 retention, because members can refine and transfer sion making. Yet, as the reliance on team-based innova­

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 insights during direct interaction. Additionally, team tion grows, we need to understand GenAI’s influence
 performance depends not merely on having expertise on collaborative settings—the very context where orga­
 present, but on the team’s capacity to effectively coordi­ nizational value is most often created.
 nate that expertise through processes of identifying GenAI represents a particularly significant develop­
 where knowledge exists, recognizing where it is needed, ment for teamwork because of two distinctive charac­
 and successfully bringing it to action on tasks (Faraj and teristics. Unlike previous waves of technology that
 Sproull 2000, Orlikowski 2002, Beane and Anthony primarily automated explicit, codifiable tasks, GenAI
 2024). In this sense, teamwork serves as on-the-ground can engage with tacit knowledge—the kind of implicit
 conduits of knowledge exchange, bridging cognitive understanding that traditionally could only be shared
 gaps that would otherwise constrain performance. through direct human interaction (Kogut and Zander
 Recent studies emphasize the importance of distin­ 1992, Zander and Kogut 1995, Argote et al. 2021).
 guishing between functional and industry expertise Additionally, GenAI’s ability to engage in natural lan­
 when understanding collaboration (Kacperczyk and guage dialogue enables it to participate in the kind of
 Younkin 2017, Souitaris et al. 2023). Task or functional open-ended, contextual interactions that characterize
 expertise pertains to the methods and technical princi­ effective teamwork, potentially allowing it to serve
 ples guiding a given task (Kogut and Zander 1992, not just as a tool but as an active participant in collab­
 Garud 1997), whereas domain expertise focuses on orative processes (De Freitas et al. 2024, Mollick 2024).
 the norms and application contexts that are unique The integration of GenAI into team-based work pre­
 to each sector. Both types of expertise can be relevant sents a mix of opportunities and challenges. On one
 for surfacing and implementing innovative solutions hand, AI can enhance collaborative performance by
 effectively (Ayoubi et al. 2026). automating certain tasks and broadening the range of
 The interplay between performance gains and exper­ expertise available to team members (Agrawal et al.
 tise sharing is further magnified by the increasing com­ 2018, Raj and Seamans 2019). It might also enhance
 plexity of modern scientific, technical, and commercial collaborative team dynamics and modify the division of
 tasks. Wuchty et al. (2007) document a global shift labor by expanding the potential performance on certain
 toward greater collaboration across research fields, a tasks beyond what humans or AI could achieve on their
 trend they link to the expanding breadth of knowledge own (Hoffmann et al. 2024, Choudhary et al. 2025).
 required to stay at the cutting edge. Jones (2009) frames Finally, AI may also facilitate boundary-spanning across
 this as the “burden of knowledge,” showing how deep different knowledge domains, drawing a parallel with
 individual specialization necessitates team-based coor­ the effects of earlier technologies (Levina and Vaast
 dination to integrate fragmented skill sets. In other 2005, Cattani et al. 2017).
 words, as the volume and sophistication of available On the other hand, organizational theory cautions
 knowledge grow, teams have become the indispens­ that new technologies often require careful integration,
 able scaffolding to achieve both depth (through special­ lest they destabilize existing routines (March and Simon
 ized experts) and breadth (through interdisciplinary 1958, Nelson and Winter 1982). Automation may dis­
 collaboration) in problem solving. rupt habitual ways of coordinating tasks (Weber and
 Finally, human collaboration provides critical social Camerer 2003). Additionally, when complex tasks are
 and motivational benefits that enhance work satisfaction performed by different technologies and individuals,
 (Deutsch 1949, Johnson and Johnson 2005, Kozlowski coordination becomes an essential mechanism for man­
 and Bell 2013). Teamwork can create promotive interac­ aging the gaps created in the division of work (Becker
 tion, reducing fear of retaliation and encouraging open and Murphy 1992, Bailey et al. 2010). A recent labora­
 participation (Johnson and Johnson 2005). The resulting tory study highlights these potential coordination pit­
 sense of belonging, collective commitment, and recipro­ falls in human–AI partnerships (Dell’Acqua et al. 2025).
 cal support fosters both stronger motivation and greater Even when AI outperforms humans on a specific task,
 persistence in challenging tasks. overall team performance declines, reflecting reduced
 trust and coordination failures. Moreover, technology-
 2.2. Generative AI driven shifts in roles and expertise may create new silos,
 Against this backdrop of increasingly team-based limit learning opportunities, or reduce human interac­
 knowledge work, GenAI has emerged as a highly tion (Kellogg et al. 2006, Beane 2019, Balasubramanian
 promising technology (Dell’Acqua et al. 2023, Noy and et al. 2022).
 Zhang 2023, Peng et al. 2023, Doshi and Hauser 2024, These issues resonate with longstanding concerns
 Eloundou et al. 2024, Otis et al. 2024, Boussioux et al. that technology can undercut the social aspects of
 2025, Brynjolfsson et al. 2025).3 Early studies have work, thereby lowering human satisfaction, psycholog­
 focused on GenAI’s impact on individual performance, ical well-being and affecting emotional relationships at

---

 Dell’Acqua et al.: The Cybernetic Teammate
 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s) 1221

 work (Beaudry and Pinsonneault 2010, Dell’Acqua et al. mirror the complexity of actual innovation work
 2025). A growing body of research shows that what (Dougherty 1992, Brown and Eisenhardt 1995). This

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 finally determines whether new technologies create or context is particularly valuable because it requires
 destroy value is not only output quality but also the both technical feasibility and market viability which
 human experience of using them—an angle that is demand the integration of diverse functional expertise
 largely absent from productivity-oriented studies. In that has traditionally justified team-based approaches
 a thorough ethnographic study, Beane (2019) finds in organizations (Kogut and Zander 1992, Nickerson
 that surgeons confronting robotic systems engage in and Zenger 2004, Jeppesen and Lakhani 2010, Teodor­
 “shadow learning” to preserve status while coping idis 2018). However, this reliance on teamwork is a
 with heightened anxiety, and these emotions ulti­ double-edged sword, as such cross-functional collabo­
 mately shape how quickly the technology is mastered. ration faces significant internal barriers in large firms,
 Similarly, field research on algorithmic platforms where different departments often operate with con­
 reveals that frontline employees actively negotiate, flicting “thought worlds” that impede successful prod­
 resist, or embrace automated controls depending on uct innovation (Dougherty 1992).
 whether they feel the systems respect their profes­ Moreover, new product development typically
 sional autonomy, with workers even engaging in vari­ involves generating solutions under time pressure with
 ous forms of “algoactivism” (Kellogg et al. 2020). limited resources. This process mirrors key features of
 Additionally, shared fears among different organiza­ an innovation tournament, where organizations must
 tional groups may hinder information sharing inside identify the most promising concepts from a broad set
 organizations, contributing to underperformance in of possibilities for further investment and development
 innovation (Vuori and Huy 2016). Together, these (Terwiesch and Loch 2004, Terwiesch and Xu 2008,
 pieces of evidence warn that the emotional footprint Boudreau et al. 2011). The challenge is compounded by
 of a technology can redirect its entire productivity organizational tendencies toward local search and exist­
 path, making it a core element to understand GenAI’s ing routines, which can constrain the exploration of
 organizational effects. novel solutions precisely when breakthrough thinking
 From this perspective, GenAI represents a further is most needed (Nelson and Winter 1982, March 1991),
 inflection point. Recent meta-analytic evidence suggests creating a clear opportunity for a cybernetic teammate
 that GenAI-based conversational agents can strengthen to potentially broaden the scope of exploration and
 individuals’ social and emotional experience—for overcome the challenges posed by these organizational
 example, by providing encouraging, human-like dia­ tendencies.
 logue that reduces distress and fosters well-being, and Although recent studies have demonstrated that
 demonstrating empathetic responses that humans rate AI can enhance individual creative performance in
 as human-like (Li et al. 2023, 2024; Ayers et al. 2023). At controlled settings (Dell’Acqua et al. 2023, Noy and
 the same time, GenAI’s characteristics may lead to neg­ Zhang 2023), to the best of our knowledge, there are
 ative emotional responses. Algorithms that generate no studies examining AI’s impact on real-world col­
 responses resembling those of a knowledge worker cre­ laborative team settings. This gap exists even as new
 ate opacity that workers struggle to interpret and navi­ theories begin to map out how different “hybrid
 gate (Faraj et al. 2018), and “techno-distress” arises problem-solving” processes, that is, the specific ways
 when opaque AI recommendations clash with estab­ humans and AI collaborate, can lead to systematically
 lished work norms (Tarafdar et al. 2019). Whether different creative outcomes (Raisch and Fomina 2025).
 GenAI produces a J-curve dip (Brynjolfsson et al. 2021) Boussioux et al. (2025) provide a critical benchmark,
 or a smooth learning curve therefore hinges in part on showing that human–AI partnerships can outperform
 the emotions it elicits: positive affect can motivate human crowdsourcing in creative problem solving.
 continued use, whereas confusion or anxiety can stall Our study unpacks the “black box” of this collabora­
 adoption. Our experiment explores these emotional tive process in an organizational setting by leveraging
 dynamics alongside performance to ask whether GenAI the theoretical framework developed by Girotra et al.
 can become a sustainable teammate that accelerates, (2010). We adapt their model to our data, deconstruct­
 rather than derails, long-run organizational learning. ing performance into a set of distinct levers: the aver­
 age quality of the ideas generated, the variance in that
 2.3. New Product Development quality, the effectiveness of selection processes, and
 New product development represents an ideal context the quality of execution in articulating the final chosen
 for examining how AI affects collaborative work. idea. This framework is particularly powerful as it
 Unlike abstract creative tasks often studied in labora­ incorporates factors like idea variance, shown to be
 tory settings, new product development involves real critical for breakthrough innovation (Singh and Flem­
 organizational constraints, domain expertise require­ ing 2010), and is motivated by the need for effective
 ments, and measurable commercial outcomes that selection from a pool of ideas, a concept grounded in

---

 Dell’Acqua et al.: The Cybernetic Teammate
 1222 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s)

 the statistical view of innovation (Dahan and Mendel­ R&D and commercial representatives are the core
 son 2001). By applying this extended framework to units where innovation happens in the company—it is

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 human–AI collaboration in an authentic organiza­ where ideas are generated and the entire innovation
 tional setting, we can move beyond asking if AI funnel begins. Senior executives at P&G emphasized
 improves team performance to understanding the pre­ how improving the quality of work at this early stage
 cise contributions it makes at each stage of the collabo­ of the innovation process is crucial for the whole inno­
 rative process. vation pipeline, producing high-quality “seeds” that
 Innovation research increasingly recognizes that orga­ can then grow within P&G’s innovation funnel. How­
 nizations often derive disproportionate value from ever, they also reported that coordination frictions—
 exceptional outcomes—the very best ideas that may gen­ such as finding time to convene representatives of
 erate outsized returns if implemented. NK-landscape both functions in a meeting, as well as cultural divides
 models of organizational search show that on a rugged between R&D and commercial—could lower the qual­
 performance surface, agents who take larger or more ity of innovation-related activities. The experiment
 varied exploratory steps are more likely to scale the was motivated by the willingness to test how an AI
 highest peaks, even if their average move is no better teaming model affects innovation and potentially
 than that of more cautious searchers (Levinthal 1997, reduces these frictions.
 Rivkin 2000). In innovation contexts, a handful of top This setting provides a specific instance where team
 ideas can make a significant impact on new product activity, coordination across functions, and selection
 success (Dahan and Mendelson 2001, Girotra et al. processes converge, offering a rich environment to
 2010, Boudreau et al. 2011). Relatedly, Li et al. (2026) study the impact of AI on collaborative work. By
 find that algorithms designed for “exploration” rather examining how GenAI affects these established collab­
 than mere “exploitation” identify candidates with higher oration processes, our research provides insights that
 upside potential in hiring contexts, suggesting that are directly applicable to the challenges faced by
 AI-augmented collaboration may excel at boundary- many large organizations in today’s rapidly evolving
 spanning exploration that produces rare but dispropor­ technological landscape.
 tionately valuable ideas.
 3.2. Experimental Approach
 This experiment was preregistered prior to data collec­
 3. Experimental Design tion.5 In line with our theoretical framework, our pre­
 3.1. Empirical Setting registration focused on two primary dimensions: the
 Between May and July 2024, we conducted a field effects of introducing AI on performance quality and
 experiment at Procter & Gamble to evaluate how whether AI could blur the functional boundaries
 GenAI influences cross-functional new product devel­ between commercial and R&D professionals. These
 opment.4 P&G, a large multinational firm with struc­ questions directly correspond to the first two pillars of
 tured R&D processes and a skilled workforce, provides teamwork—performance and expertise sharing—that
 a useful setting in which to investigate GenAI’s role in frame our investigation.
 innovation-focused knowledge work. With roughly In presenting our findings, we complement our
 7,000 R&D professionals worldwide, the firm encom­ main analysis with an exploration of the emergent pat­
 passes end-to-end product development activities, from terns discovered during our investigation. Although
 concept to launch. This breadth of expertise, alongside performance and expertise dimensions were our pri­
 well-defined organizational routines and substantial mary focus, our examination of emotional responses
 operational scope, offers a valuable context through emerged as a significant factor during the study. This
 which to examine human collaboration with GenAI in third pillar—sociality, part of the preregistration sub­
 real-world contexts. Over several months, we worked mission as a variable of interest but with unclear
 closely with P&G’s leadership to tailor our experimen­ effects—completes our assessment of AI’s potential as
 tal design, aligning it with the company’s established a cybernetic teammate. Finally, our exploration of the
 innovation practices and strategic priorities. right tail of performance distribution (breakthrough
 The idea of studying the effects of AI on product innovations) emerged as another important dimen­
 innovation tasks at the interplay between commercial sion, critical to understanding AI’s organizational
 and R&D functions originated from several in-depth impact, particularly in innovation contexts.
 discussions with the leadership team of the organiza­ The experimental design was carefully crafted to
 tion. As it often happens in companies of this nature mirror P&G’s actual new product development pro­
 and scale, work at P&G typically occurs in teams and cesses, particularly focusing on the early stages where
 follows structured routines, often involving cross- new ideas are generated and initially developed. P&G
 functional collaboration. This is especially true for emphasizes this early seed stage as a crucial element
 innovation activities, for which teams composed of in their entire innovation process. A senior leader at

---

 Dell’Acqua et al.: The Cybernetic Teammate
 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s) 1223

 the company emphasized that “better seeds lead to to the existence of multiple experimental conditions
 better trees,” reflecting the importance of high-quality and simply told each person they would experience a

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 ideation. Through extensive collaboration with P&G personalized version of the workshop. Participants in
 over multiple months, we developed a deep under­ teams were put in contact only when both attended,
 standing of their innovation practices and structured ensuring no contamination or selection biases due to
 our experiment accordingly. A key insight from this participation attrition. Table 1 provides an overview of
 engagement was that early-stage innovation typically the participants, indicating a balanced distribution
 involves very small cross-functional teams comprised of key functions within P&G. Figure 1 illustrates our
 of commercial and R&D professionals.6 We thus mim­ 2 × 2 experimental design, with participants randomly
 icked this structure in our experimental design. assigned to work either individually or in teams, and
 The experiment was conducted as a one-day virtual with or without AI assistance.
 product development workshop, involving 826 parti­ The sample size was determined to ensure suffi­
 cipants from P&G’s commercial and R&D functions.7 cient statistical power to detect meaningful differ­
 Our analyses focus on 791 of these participants,8 who ences between conditions, accounting for potential
 were randomly assigned across four conditions.9 Spe­ attrition and the nested structure of the data.11 The
 cifically, the four conditions are (1) the control, an inclusion of both commercial and R&D functions
 individual without AI (Individual No AI); (2) Treat­ allows for a comprehensive examination of cross-
 ment 1 (T1), a team (R&D + commercial) without AI functional collaboration, a critical aspect of innova­
 (Team No AI); (3) Treatment 2 (T2), an individual tion and product development in large consumer
 with AI (Individual + AI); and (4) Treatment 3 (T3), a goods companies.
 team (R&D + commercial) with AI (Team + AI). Parti­ The two team conditions (with and without AI) were
 cipants were randomly assigned to these conditions formed by randomly pairing a commercial and an R&D
 within each of the eight randomization clusters, professional. Collaboration occurred remotely through
 defined by four business units (Baby Care, Feminine Microsoft Teams, as is standard practice at P&G, with
 Care, Grooming, and Oral Care) across two geogra­ one team member randomly designated to share their
 phies (Europe and Americas).10 Randomization was screen and submit the team’s solution.12 This structure
 stratified by business unit and geography to ensure bal­ ensured that team members could contribute to and
 anced representation across all groups. To preempt refine their solution in real time, while maintaining a sin­
 social-comparison concerns, we kept participants blind gle, coherent workflow for submission. Consequently,

 Table 1. Summary Statistics

 Panel A: Individual

 Individual No AI Individual + AI Mean diff.

 Female 0.578 (0.494) 0.555 (0.497) �0.023
 Male 0.422 (0.494) 0.432 (0.495) 0.010
 Band level 2.071 (0.742) 2.065 (0.762) �0.006
 Experience inside company (years) 12.351 (8.293) 11.816 (7.807) �0.535
 R&D specialist 0.604 (0.491) 0.594 (0.493) �0.010
 Use of ChatGPT at work (1–5 Likert) 2.786 (1.126) 2.735 (1.206) �0.050
 Use of ChatGPT personal (1–5 Likert) 2.468 (1.200) 2.529 (1.147) 0.061
 Access to ChatGPT at work (yes � 1, no � 0) 0.812 (0.392) 0.800 (0.401) �0.012
 Expectation of AI use at work pre-exp (1–5 Likert) 3.539 (0.951) 3.555 (1.027) 0.016
 Individuals 154 155
 Panel B: Team

 Team No AI Team + AI Mean diff.

 Female 0.596 (0.492) 0.556 (0.498) �0.040
 Male 0.404 (0.492) 0.444 (0.498) 0.040
 Band level 2.000 (0.714) 2.083 (0.734) 0.083
 Experience inside company (years) 10.091 (7.616) 10.476 (8.108) 0.385
 R&D specialist 0.500 (0.501) 0.500 (0.501) 0.000
 Use of ChatGPT at work (1–5 Likert) 2.574 (1.225) 2.615 (1.179) 0.041
 Use of ChatGPT personal (1–5 Likert) 2.326 (1.056) 2.480 (1.092) 0.154
 Access to ChatGPT at work (yes � 1, no � 0) 0.713 (0.427) 0.746 (0.384) 0.033
 Expectation of AI use at work pre-exp (1–5 Likert) 3.430 (1.003) 3.534 (1.021) 0.103
 Team participants 230 (115 teams) 252 (126 teams)
 Notes. Standard deviations are in parentheses. Diff., difference; pre-exp, pre-experiment.

---

 Dell’Acqua et al.: The Cybernetic Teammate
 1224 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s)

 Figure 1. Treatment Matrix Postsurvey data were also collected, and follow-up
 interviews were conducted with some participants.

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 Participant motivation was both intrinsic and
 extrinsic. First, they enrolled in the study as part of an
 organizational upskilling initiative to enhance their
 knowledge about GenAI and its applications in their
 work. Additionally, a key incentive was the opportu­
 nity for visibility: participants were informed that the
 best proposals would be presented to their respective
 business unit leaders, offering a chance to showcase
 their skills and ideas to top management. To maintain
 fairness and encourage participation across all condi­
 tions, rewards for the best proposals were determined
 within each treatment group (control, individual with
 Note. This figure displays the 2 × 2 experimental design showing four
 conditions: individuals and teams working either with or without AI AI, etc.). This approach ensured that participants in all
 assistance. conditions had equal opportunities for recognition,
 regardless of their assigned experimental group.
 our analysis treats each team as a cohesive unit, focusing
 on overall team performance and AI integration rather
 4. Empirical Strategy
 than on individual roles within the team structure. 4.1. Analytical Approach
 Participants (whether alone or in teams) were assigned Our empirical analysis primarily relies on regression
 tasks within their own business units to develop viable analysis to estimate the causal effect of AI adoption
 ideas for new products, packaging, communication and team configuration on various outcome measures.
 approaches, or retail execution, among others. All sup­ Our main specification takes the following form for a
 porting data and processes mirrored what P&G employ­ given solution generated i:
 ees would typically use in similar real-world efforts. This Yi � β0 + β1 TeamNoAIi + β2 AloneAIi + β3 TeamAIi
 design choice enhanced ecological validity by allowing
 + γControlsi + δFEi + ɛi ,
 participants to tackle challenges relevant to their day-to-
 day work. Before random assignment, every participant where Yi represents different outcome variables that
 took part in a brief training session led by a coauthor that we examine in our analysis. Each outcome captures a
 reviewed P&G’s standard frameworks questions for distinct dimension of performance, expertise and col­
 tackling the task. As all participants were P&G domain laboration that we investigate to understand the multi­
 experts, this first session served as a refresher and faceted impact of AI adoption and team configuration
 ensured that no group received differential guidance. on work processes and outputs. The baseline category
 The GenAI tool used in the experiment was built on is individuals without AI. We describe these outcome
 GPT-4 and accessed through Microsoft Azure.13 In the variables in detail in Section 4.2 below.
 AI-enabled conditions (T2 and T3), participants received a The term Controlsi includes a list of preexperimen­
 one-hour training session on how to prompt and interact tal features including demographic and professional
 with the GenAI tool for Consumer Product Goods-related characteristics, and FEi includes day and business unit
 tasks. One of the authors led this training and provided a fixed effects.
 PDF with recommended prompts.14 This standardized We estimate three variants of this model. Model 1
 approach ensured a uniform baseline of familiarity with includes only the treatment indicators. Model 2 includes
 the GenAI interface for all AI-enabled participants.15 only fixed effects for business unit and date of participa­
 In addition to our primary measures of overall per­ tion. Model 3 adds controls including band level,
 formance, expertise sharing, and social interaction, we years of experience in the company, gender, and prior
 also collected information on solution novelty, feasi­ AI usage both at work and for personal purposes.16
 bility, and impact as robustness checks. These mea­ Throughout our analysis, we use robust standard errors
 sures confirm the findings reported in the main text. to account for potential heteroskedasticity.17
 Beyond these direct comparisons to the baseline,
 3.3. Collected Outcomes we conduct additional analyses comparing outcomes
 Data collection occurred in multiple stages. Presurvey across treatment conditions. Of particular interest are
 data were collected to gather individual information the comparisons between the two team conditions
 about participants. During the product development (team without AI versus team with AI) and between
 workshop, all GenAI prompts and responses were the two AI-enabled conditions (alone with AI versus
 recorded, and team interactions were transcribed. team with AI). These additional comparisons help us

---

 Dell’Acqua et al.: The Cybernetic Teammate
 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s) 1225

 understand both the value of AI in team settings non-core-job role (i.e., individuals in the same business
 and the complementarity between AI and teamwork. unit but involved less frequently in new product inno­

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 Whenever relevant, we report the p-values for these vation). This dichotomy provides insight into how
 comparisons at the bottom of our regression tables prior knowledge and domain familiarity might inter­
 and discuss their implications in the text. act with AI or team structures. Additionally, we mea­
 sured the degree of Technicality of a solution using a
 4.2. Dependent Variables one-to-seven Likert score assigned by the same human
 Our primary outcome measure is Quality, which cap­ evaluators assessing solution quality, where higher
 tures the overall quality of submitted solutions on a values indicate more technically oriented ideas. Con­
 scale from 1 to 10. These quality scores were assigned versely, lower values suggest commercially oriented,
 by human expert evaluators with backgrounds in market-focused concepts.
 both business and technology, who independently Finally, we measure changes in participants’ self-
 assessed each solution. The evaluators were blind to reported emotional states before and after completing
 the conditions of the experiment and the profile of the the task through two composite measures. Positive emo­
 submitters. We standardized these scores based on tions combine participants’ reported levels of Enthusi­
 the control group (individuals working alone without asm, Energy, and Excitement, whereas negative emotions
 AI), resulting in scores that represent standard devia­ aggregate feelings of Anxiety, Frustration, and Distress.20
 tions from the control group mean. During the same Each component is measured on a scale from one to
 evaluation process, experts also assessed two addi­ seven, and standardized based on the control group
 tional key dimensions of the solutions: Novelty and mean and standard deviation. Both measures are calcu­
 Feasibility.18 Novelty measures the degree of innova­ lated as the difference between post-task and pretask
 tion and originality in the submitted solutions on a responses: that is, we measure emotional change from
 scale from 1 to 10, whereas Feasibility evaluates how baseline levels established at the beginning of the task,
 practical and implementable the solutions are, also on not absolute emotional states. Because baseline measure­
 a 1–10 scale. These dimensions were evaluated simul­ ments were taken after treatment assignment but before
 taneously with the overall quality assessment, provid­ task engagement, any initial emotional reactions to
 ing a comprehensive evaluation of each solution’s assignment conditions would already be incorporated in
 merits.19
 these baselines, making the observed positive emotional
 These innovation outcomes are grounded in the lit­
 shifts attributable to the actual experience of working
 erature (e.g., Boudreau et al. 2016, Lane 2023) and are
 with AI.21
 also used extensively by P&G. On average, each solu­
 tion received more than three independent evalua­
 tions, though the exact number varies across solutions. 5. Results
 This multiple-evaluation approach helps ensure the 5.1. Performance
 robustness of our quality measurements. Figure 2 provides instructive insights into the quality
 We also analyze other performance measures such as of solutions across different groups. It displays aver­
 Solution Length and Expected Quality. Solution Length age quality scores, showing the relative performance of
 measures the total number of words in the solutions AI-treated versus non-AI treated groups is significantly
 submitted by participants. This variable helps us under­ higher. The distributions of these quality scores, shown
 stand how AI and team configuration affect the com­ in Figure 3, reveal that while both teams without AI
 prehensiveness and detail level of submitted solutions. and individuals with AI significantly outperform the
 Expected Quality is a binary variable based on sur­ control group, their quality distributions are remark­
 vey responses, where participants indicated whether ably similar, providing further evidence that AI can rep­
 they expected their solution to rank in the top 10% licate key performance benefits of teamwork. Table 2
 (one) or not (zero). Participants answered this question quantifies these quality differences through regression
 after submitting their final solution. This measure helps analysis. Teams without AI show a quality improve­
 us understand how different working configurations ment of 0.24 standard deviations over individuals with­
 affect participants’ confidence and self-assessment of out AI (p < 0.05), highlighting the traditional benefits of
 their performance. collaboration. This replication of traditional team bene­
 In addition to performance metrics, we capture how fits serves as an important validation of our experimen­
 expertise is configured and deployed. Specifically, we tal setting, confirming that teams function as expected
 categorize participants based on their domain of in real organizational contexts, as well as confirming
 knowledge (R&D or Commercial) and their functional P&G’s new product development experience.
 experience embodied in whether product develop­ The impact of AI is greater: individuals with AI dem­
 ment is a Core Job responsibility (i.e., employees who onstrate a 0.37 standard deviation increase (p < 0.01),
 regularly engage in new product initiatives) or a and teams with AI show a 0.39 standard deviation

---

 Dell’Acqua et al.: The Cybernetic Teammate
 1226 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s)

 Figure 2. Average Solution Quality Table 2. Solution Quality (Standardized)

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 Quality Quality Quality

 Team No AI 0.245** 0.262** 0.307**
 (0.120) (0.122) (0.131)
 Individual + AI 0.373*** 0.386*** 0.370***
 (0.106) (0.108) (0.107)
 Team + AI 0.392*** 0.404*** 0.463***
 (0.122) (0.123) (0.139)
 Team + AI � Team No AI p � 0:242 p � 0:254 p � 0:216
 Fixed effects X X
 Controls X
 Control mean 0.000 �0.173 0.306
 (0.081) (0.173) (0.228)
 Observations 550 550 550
 Adjusted R2 0.023 0.023 0.048
 Notes. The p-values for the t-tests comparing Team + AI and Team No
 AI are reported. Fixed effects and controls are as discussed in the text.
 **p < 0.05; ***p < 0.01.

 Whereas teams without AI produced solutions only
 Note. This figure displays the average quality scores for solutions
 across different groups, showing the relative performance of marginally longer than individual controls, the intro­
 AI-treated versus non-AI-treated groups with standard errors. duction of AI led to significantly longer outputs. As
 shown in Table 3, these large effects persist across all
 improvement (p < 0.01). These effects remain robust specifications.
 across all specifications. The data reveal a hierarchy in
 solution quality across different working configurations. 5.2. Expertise
 Individuals working alone without AI assistance pro­ We now turn to how AI impacts how team expertise
 duced the lowest-quality solutions on average. Teams is leveraged in the new product development task.
 working without AI showed a modest improvement We start by examining the heterogeneity of the results
 over individuals. The introduction of AI led to notable across workers who have different familiarity with
 performance changes: individuals working with AI this type of task, as shown in Figure 4 and the corre­
 performed at a level comparable to teams without AI, sponding Table 4. Figure 4 splits our sample between
 suggesting that AI-enabled individuals can match the employees for whom product development is a core-
 output quality of traditional human teams, effectively job task (left panel; core job) and employees who are
 substituting for team collaboration in certain contexts. less familiar with new product development (right
 Finally, as has been the case with individual work­ panel; non–core job), comparing their performance
 ers, we see AI leading to more developed outcomes. across our experimental conditions.22

 Figure 3. Pairwise Density Comparisons

 Notes. These figures illustrate the pairwise comparisons of solution quality distributions across different experimental conditions. The left panel
 compares solutions between individuals and teams working without AI assistance. The middle panel shows the quality distribution between
 individuals working alone with and without AI assistance. The right panel compares solutions between teams without AI and individuals with
 AI assistance.

---

 Dell’Acqua et al.: The Cybernetic Teammate
 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s) 1227

 Table 3. Solution Length workers (e.g., Dell’Acqua et al. 2023, Brynjolfsson
 et al. 2025). AI allows less experienced employees to

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 Length Length Length
 achieve performance levels that previously required
 Team No AI 30.456 56.746* 57.184+ either direct collaboration or supervision by collea­
 (27.419) (30.865) (38.673) gues with more task-related experience.
 Individual + AI 504.507*** 511.568*** 503.833***
 Figure 5 illustrates the difference in idea generation
 (42.963) (45.206) (45.081)
 Team + AI 543.745*** 556.997*** 551.578*** between commercial and technical participants, with
 (42.328) (43.737) (51.989) and without AI assistance. The left graph shows parti­
 Fixed effects X X cipants working alone without AI. In this scenario,
 Controls X commercial participants (green) demonstrate a higher
 Control mean 381.422 306.565 336.197 likelihood of proposing less technical ideas, as indi­
 Observations 550 550 550
 cated by their distribution toward lower values on the
 Adjusted R2 0.317 0.337 0.344 x-axis. In contrast, technical participants (yellow) tend
 to suggest more technically oriented ideas, clustering
 Notes. Standard errors are in parentheses. Fixed effects and controls
 are as discussed in the text. toward higher x-axis values. The right graph depicts
 +
 p < 0.2; *p < 0.1; ***p < 0.01. participants working with AI assistance. Notably, the
 distinction between commercial and technical partici­
 The results are particularly noteworthy for non-core- pants disappears in this scenario. The distribution of
 job employees. Without AI, non-core-job employees both groups appears similar across the x-axis, suggest­
 working alone performed relatively poorly. Even when ing that AI assistance leads these groups to propose
 working in teams, non-core-job employees without AI ideas of a similar level of technicality. Figure 5 illus­
 showed only modest improvements in performance. trates a shift in idea generation patterns with the intro­
 However, when given access to AI, non-core-job duction of AI. Without AI assistance, participants
 employees working alone achieved performance tended to generate ideas closely aligned with their pro­
 levels comparable to teams with at least one core-job fessional backgrounds. However, when aided by AI,
 employee. This suggests that AI can effectively substi­ this distinction largely disappeared. Both commercial
 tute for the expertise and guidance typically provided and technical participants generated a more balanced
 by team members that are familiar with the task mix of ideas, spanning the commercial/technical spec­
 at hand. This pattern demonstrates AI’s potential trum. Moreover, quality scores did not significantly
 to improve access to expertise within organizations, vary based on a solution’s technical orientation, indicat­
 extending prior work on individual knowledge ing that these effects did not come at the cost of solution

 Figure 4. Average Solution Quality: Core Jobs vs. Not

 Note. This figure displays the average quality scores for solutions across different groups, separating between participants who are more familiar
 with this type of task (on the left) and participants less familiar with it (on the right) with standard errors.

---

 Dell’Acqua et al.: The Cybernetic Teammate
 1228 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s)

 Table 4. Solution Quality by Familiarity with the Type of Task (Standardized)

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 Quality

 Noncore jobs Core jobs

 Model 1 Model 2 Model 3 Model 1 Model 2 Model 3

 Team No AI 0.023 0.026 �0.132 0.309** 0.328** 0.377**
 (0.228) (0.240) (0.248) (0.152) (0.151) (0.165)
 Individual + AI 0.324** 0.356** 0.360** 0.433*** 0.457*** 0.457***
 (0.149) (0.151) (0.156) (0.152) (0.150) (0.153)
 Team + AI 0.330+ 0.299+ 0.203 0.397** 0.386** 0.455**
 (0.213) (0.212) (0.253) (0.157) (0.157) (0.179)
 Fixed effects X X X X
 Controls X X
 Control mean �0.009 �0.194 0.382 0.010 �0.143 0.311
 (0.112) (0.258) (0.336) (0.117) (0.232) (0.317)
 Observations 218 218 218 332 332 332
 Adjusted R2 0.014 0.009 0.032 0.019 0.040 0.062
 Notes. Standard errors are in parentheses. Fixed effects and controls are as discussed in the text.
 +
 p < 0.2; **p < 0.05; ***p < 0.01.

 effectiveness. By leveraging AI, participants effectively 0.457 standard deviation increase in positive emotions
 expanded their problem-solving horizons, demonstrat­ (p < 0.01) compared with the control group, and teams
 ing AI’s potential to foster more holistic and interdisci­ with AI demonstrated an even larger 0.635 standard
 plinary thinking. deviation increase (p < 0.01). Simultaneously, both
 individuals and teams using AI reported significant
 5.3. Sociality decreases in negative emotions (�0.233 and �0.235
 Finally, we find that AI integration leads to enhanced standard deviations respectively, p < 0.05). This pattern
 positive emotional experiences. Figures 6 and 7 pre­ of emotional responses provides further evidence of
 sent emotional responses across groups, illustrating AI’s effectiveness as a teammate. Without AI assis­
 that participants using AI reported significantly higher tance, individuals working alone show lower positive
 levels of positive emotions (excitement, energy, and emotional responses compared with those working in
 enthusiasm) and lower levels of negative emotions teams, reflecting the traditional psychological benefits
 (anxiety and frustration). Tables 5 and 6 confirm these of human collaboration. However, individuals using
 results. Specifically, individuals with AI showed a AI report positive emotional responses that match or

 Figure 5. Degree of Solution Technicality for Individuals

 Notes. These figures illustrate the difference in idea generation between commercial and technical participants, with and without AI assistance.
 In both graphs, blue represents commercial participants and yellow represents technical participants. The x-axis indicates the commercial nature
 of ideas, with higher values representing more technically oriented suggestions.

---

 Dell’Acqua et al.: The Cybernetic Teammate
 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s) 1229

 Figure 6. Evolution of Positive Emotions During the Task Table 5. Evolution of Self-Reported Positive Emotions
 Before and After the Task (Standardized)

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 Positive Positive Positive
 emotions emotions emotions

 Team No AI 0:269∗∗ 0.254** 0.257*
 (0.124) (0.126) (0.137)
 Individual + AI 0.457*** 0.475*** 0.485***
 (0.107) (0.106) (0.106)
 Team + AI 0.635*** 0.635*** 0.666***
 (0.131) (0.129) (0.153)
 Fixed effects X X
 Controls X
 Control mean 0.000 �0:315 0.012
 Observations 533 533 533
 Adjusted R2 0.050 0.064 0.070
 Notes. Standard errors are in parentheses. Fixed effects and controls
 are as discussed in the text.
 *p < 0.1; **p < 0.05; ***p < 0.01.

 individual work settings. At the same time, it is impor­
 Notes. This figure presents the difference in self-reported positive tant to recognize that not all negative emotions in
 emotions among participants before and after the task, comparing teams are necessarily detrimental. A certain degree of
 AI-treated and non-AI-treated groups to examine the emotional creative tension and disagreement can stimulate dee­
 impact of AI on teamwork with standard errors. Positive emotions
 are answers to questions about enthusiasm, energy, and excitement.
 per exploration and higher-quality ideas over time,
 Higher numbers indicate stronger emotional responses. suggesting that the reduction of interpersonal friction
 we observe here may not always translate into long-
 exceed those of team members working without AI. term creative gains and may in fact be harmful (Jonas­
 This suggests that AI can substitute for some of the sen et al. 2026).
 emotional benefits typically associated with teamwork, These emotional responses correlate with partici­
 serving as an effective collaborative partner even in pants’ evolving expectations about AI use. As shown
 in Tables 7 and 8, participants who reported larger
 Figure 7. Evolution of Negative Emotions During the Task
 increases in their expected future use of AI also
 reported more positive and fewer negative emotions
 during the task. Although this correlation cannot
 definitively establish causality, it suggests an interest­
 ing relationship between positive experiences with

 Table 6. Evolution of Self-Reported Negative Emotions
 Before and After the Task (Standardized)

 Negative Negative Negative
 emotions emotions emotions

 Team No AI �0:136 �0:094 �0:006
 (0.124) (0.121) (0.141)
 Individual + AI �0.233** �0.247** �0.263**
 (0.117) (0.116) (0.117)
 Team + AI �0.235** �0.221* �0:157
 (0.118) (0.116) (0.138)
 Fixed effects X X
 Controls X
 Control mean 0.000 0.166 0.068
 (0.082) (0.166) (0.252)
 Notes. This figure presents the reduction in self-reported negative Observations 530 530 530
 emotions among participants before and after the task, comparing Adjusted R2 0.005 0.022 0.031
 AI-treated and non-AI-treated groups to examine the emotional
 impact of AI on teamwork with standard errors. Negative emotions Notes. Standard errors are in parentheses. Fixed effects and controls
 are answers to questions about anxiety, frustration, and distress. are as discussed in the text.
 Higher numbers indicate negative emotions decreased. *p < 0.1; **p < 0.05.

---

 Dell’Acqua et al.: The Cybernetic Teammate
 1230 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s)

 Table 7. Average Evolution of Self-Reported Positive Emotions Before and After the Task Based on Expectation
 of Use of AI at Work

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 Without AI (control) With AI (treatment)

 Positive Positive Positive Positive Positive Positive
 emotions emotions emotions emotions emotions emotions

 Diff. in expected use of GenAI 0:297∗ 0.231+ 0.140 0.678*** 0.701*** 0.638***
 (0.171) (0.178) (0.182) (0.248) (0.234) (0.243)
 Fixed effects X X X X
 Controls X X
 Control mean �0:992 �1:606 �1:083 0.013 �0:931 0.992
 Observations 262 262 262 271 271 271
 Adjusted R2 0.007 0.025 0.036 0.029 0.059 0.086
 Notes. Standard errors are in parentheses. Fixed effects and controls are as discussed in the text. Diff., Difference.
 +
 p < 0.2; *p < 0.1; ***p < 0.01.

 AI and anticipated future engagement with the of generated ideas, with both AI-enabled conditions
 technology. showing marked improvements over their non-AI
 counterparts. Panel (b) examines selection effective­
 5.4. Beyond Aggregate Performance: Process ness. We measure it as the probability of choosing the
 and Extremes highest-quality idea to go forward with. This selection
 5.4.1. Decomposing AI’s Contributions. To understand process reveals an interesting pattern: teams without
 the specific mechanisms through which AI affects AI demonstrate the strongest capability at identifying
 collaborative performance, we leverage our experi­ their best idea from their portfolio of five, correctly
 mental design’s multistage structure, which allows us selecting their highest-quality concept approximately
 to decompose the innovation process into its core sta­ 50% of the time compared with roughly 37% for
 tistical levers. Participants first generated five initial AI-enabled conditions. Interestingly, panel (c) shows
 ideas, then selected the one they wanted to proceed that AI’s improvement in average quality occurs
 with, and finally developed that chosen idea into a across the full distribution of idea quality—the range
 detailed solution. By constraining idea quantity to five between highest and lowest-quality ideas remains
 across all conditions—an explicit design choice that extremely similar across all conditions, indicating that
 suppresses an additional channel through which AI AI elevates the entire quality spectrum rather than
 could provide an advantage—we can isolate AI’s constraining variance or eliminating creative extremes.
 impact on the core levers identified in our theoretical However, panel (d) shows that despite the selection
 framework: average idea quality, quality variance, disadvantage observed in panel (b), AI conditions
 and selection effectiveness. still produce higher-quality selected ideas in absolute
 Figure 8 reveals where AI exerts its primary collab­ terms. This occurs because AI’s boost to average idea
 orative influence across the innovation process. Panel quality (panel (a)) more than compensates for any
 (a) demonstrates that AI enhances the average quality modest reduction in selection accuracy, resulting in

 Table 8. Average Evolution of Self-Reported Negative Emotions Before and After the Task Based on Expectation
 of Use of AI at Work

 Without AI (control) With AI (treatment)

 Negative Negative Negative Negative Negative Negative
 emotions emotions emotions emotions emotions emotions

 Diff. in expected use of GenAI �0.270* �0.240* �0:170 �0.581*** �0.607*** �0.663***
 (0.137) (0.144) (0.154) (0.190) (0.188) (0.201)
 Fixed effects X X X X
 Controls X X
 Control mean �0:134 0.122 0.109 �0.449** 0.110 0.880
 Observations 259 259 259 271 271 271
 Adjusted R2 0.007 0.032 0.071 0.023 0.028 0.077
 Notes. Standard errors are in parentheses. Fixed effects and controls are as discussed in the text. Diff., Difference.
 *p < 0.1; **p < 0.05; ***p < 0.01.

---

 Dell’Acqua et al.: The Cybernetic Teammate
 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s) 1231

 Figure 8. Decomposition of AI’s Impact on the New Product Development Process

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 Notes. Panel (a) shows the average quality of ideas generated across experimental conditions, standardized relative to the control group (Individual
 No AI). Panel (b) displays the probability that participants selected their highest-quality idea to develop further. Panel (c) displays the average gap
 between highest- and lowest-quality ideas within each portfolio. Panel (d) shows the average quality of selected ideas; although AI conditions show
 higher absolute quality, this reflects their elevated baseline rather than improved selection capability. All error bars represent standard errors.

 superior final outcomes even when participants are human teammates, who naturally introduce friction
 slightly less effective at identifying their strongest and dissent, AI tends to affirm. That affirmation may
 concepts. feel productive in the moment while diminishing par­
 Panel (b) shows that participants working without ticipants’ evaluative judgment—a dynamic consistent
 AI appear to have been better at identifying their own with evidence that AI overreliance can cause users to
 best ideas than those who worked with AI. This pat­ exert less effort (Dell’Acqua 2022). Additionally, when
 tern suggests that AI assistance may subtly undermine ideas are developed with AI assistance, they may be
 the evaluative judgment needed to select the most less deeply internalized by their human collaborators,
 promising concepts from a generated set. Several making critical evaluation more challenging—and
 mechanisms could be at play. For one, the sycophantic recent work suggests that AI-generated explanations
 tendencies sometimes observed in LLMs may have can suppress independent human judgment in evalua­
 reinforced participants’ confidence in their initial ideas tions (Lane et al. 2026). That being said, AI’s boost to
 (Randazzo et al. 2025a). The validating nature of AI idea quality more than compensates for this selection
 feedback may itself erode critical engagement: unlike effect, yielding superior final outcomes overall.

---

 Dell’Acqua et al.: The Cybernetic Teammate
 1232 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s)

 Overall, these results illuminate AI’s primary mecha­ Table 9. Probability of Being Rated Top 10% of Quality
 nism as a collaborative partner: it functions as a quality Scores

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 amplifier rather than a decision enhancer. AI consistently
 Top Top Top
 elevates the baseline quality of creative output while also quality quality quality
 preserving the natural variance that drives breakthrough
 innovation. Interestingly, human teams without AI dem­ Team No AI 0.037 0.045+ 0.054+
 (0.033) (0.034) (0.041)
 onstrate a small advantage in selection accuracy, sug­ Individual + AI 0.019 0.029 0.030
 gesting that human-to-human collaboration may offer (0.029) (0.029) (0.029)
 unique benefits for evaluative judgment. This confirms Team + AI 0.092** 0.098** 0.112**
 GenAI’s unclear potential as a decision maker for inno­ (0.037) (0.038) (0.045)
 vation selection (Csaszar et al. 2024, Doshi et al. 2025, Team + AI � Team No AI p � 0:190 p � 0:207 p � 0:175
 Lane et al. 2026), noting that AI-aided participants may Team + AI � Individual + AI p � 0:061 p � 0:077 p � 0:069
 have not used AI for the selection of ideas. Fixed effects X X
 Controls X
 5.4.2. Exceptional Performance Measures. Although Control mean 0.058 �0.040 0.025
 the decomposition analysis reveals how AI affects aver­ Observations 550 550 550
 age performance across different stages of the innova­ Adjusted R2 0.008 0.010 0.003
 tion process, many organizations place disproportionate Notes. The p-values for the t-tests comparing Team + AI with Team No
 emphasis on exceptional outcomes that can reinforce AI and Individual + AI are reported. Fixed effects and controls are as
 their competitive position. To explore whether AI facili­ discussed in the text.
 +
 p < 0.2; **p < 0.05.
 tates standout solutions, we examine the likelihood of
 generating top-tier innovations across our experimen­
 tal conditions. using AI were more likely to generate solutions rank­
 We developed additional metrics capturing top-tier ing in the top 10% of all submissions. Specifically, as
 performance. We created a binary measure called Top quantified in Table 9, teams with AI were 9.2 percent­
 10% Solutions, which equals one if a solution’s quality age points more likely to produce solutions in the top
 score (on a 1–10 scale) ranked in the highest decile across decile compared with the control mean of 5.8%, which
 all submissions in the sample, and zero otherwise. By corresponds to roughly three times more chances of
 isolating these top performers, we can assess the extent being in the top decile of solutions. Although indivi­
 to which AI-enabled conditions and team configurations duals with AI show a small positive effect, this effect
 produce exceptionally high-quality innovations. is not statistically significant, suggesting that the com­
 Figure 9 highlights the extent to which AI improves bination of AI and teamwork might be particularly
 innovative performance. Both individuals and teams powerful for achieving exceptional performance.
 These patterns indicate that AI, particularly when
 Figure 9. Top 10% Solutions combined with teamwork, does not just improve aver­
 age performance but also increases the likelihood of
 producing the kind of breakthrough solutions that
 drive organizational success.

 5.5. Additional Analyses
 5.5.1. Expected Quality. We captured Expected Quality—
 a self-reported binary variable indicating whether parti­
 cipants believed their solution would be in the top
 10% or not. Participants answered this question immedi­
 ately after submitting their final solution. Interestingly,
 although objective performance improved, participants
 using AI were actually less confident about their solu­
 tions. As shown in Figure 10, AI-enabled participants
 were 9.2 percentage points less likely to expect their solu­
 tions to rank in the top 10% compared with the control
 group (p < 0.05), suggesting a disconnect between actual
 and perceived performance.

 5.5.2. Human Team Collaboration. Figure 11 shows
 Note. This figure displays the proportion of top 10% solutions across the distribution of solution types, ranging from techni­
 different treatments with standard errors. cally focused to market-focused approaches. Without

---

 Dell’Acqua et al.: The Cybernetic Teammate
 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s) 1233

 Figure 10. Perceived Likelihood of Top 10 Percent Placement overall levels of technical content. This moderate shift
 by Treatment Group from bimodality to unimodality, while preserving the

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 range of technical depth, suggests that AI helps reduce
 dominance effects in team collaboration. Overall, AI
 appears to facilitate more balanced contributions from
 both technical and commercial perspectives.

 5.5.3. Patterns of AI Use. Our data also allowed us to
 assess the extent to which teams actually used the AI in
 their work. To assess the extent of AI utilization in solution
 generation, we analyzed the retention rate of AI-generated
 content in participants’ final submissions. Our retention
 measure quantifies the percentage of sentences in the sub­
 mitted solutions that were originally produced by AI,
 with a threshold of at least 90% similarity. This metric
 excludes sentences that were part of the initial human-
 authored prompts, focusing solely on AI-generated con­
 tent. Figure 12 illustrates the distribution of retention rates
 for both individual and group AI conditions.
 The retention analysis reveals an interesting pattern
 relating to AI reliance among participants. For both
 Notes. This table shows the percentage of participants in each treat­ individuals and groups using AI, we observe a signifi­
 ment group who expected their solution to rank among the top 10 per­
 cent. It reflects participants’ confidence in their solutions across cant skew toward high retention rates, with a substan­
 different conditions with standard errors. tial proportion of participants retaining more than
 75% of AI-generated content in their final solutions.
 AI, teams exhibit a clear bimodal distribution (bimodal­ This suggests that many participants heavily lever­
 ity coefficient � 0.564), suggesting that solutions tend to aged AI capabilities in crafting their responses. How­
 cluster around either technical or commercial orienta­ ever, high retention rates do not necessarily indicate
 tions, likely reflecting the dominant perspective of the passive AI adoption—participants may engage ex­
 more influential team member. In contrast, AI-enabled tensively with the tool through iterative prompting,
 teams show a more uniform, unimodal distribution validation of responses, critical evaluation, and incorpo­
 (bimodality coefficient � 0.482), while maintaining similar ration of domain expertise in their prompting strategy.

 Figure 11. Degree of Solution Technicality for Teams

 Notes. These figures illustrate the difference in idea generation for teams. Dark blue represents Team No AI, and red represents Team + AI. The
 x-axis indicates the commercial nature of ideas, with higher values representing more technically oriented suggestions.

---

 Dell’Acqua et al.: The Cybernetic Teammate
 1234 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s)

 Figure 12. Retention of AI-Aided Solutions

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 Notes. This figure shows the distribution of AI-generated content retained in final solutions for AI-treated participants (individuals and teams).
 The retention rate represents the proportion of sentences in submitted solutions that were originally produced by AI (with at least 90% similar­
 ity), excluding content from initial human prompts.

 Interestingly, the distribution also shows a nontrivial and perspectives traditionally provided by team mem­
 percentage of participants with zero retention. These bers. Teams augmented with AI showed similar levels
 cases represent participants who engaged with AI for of improvement (0.39 standard deviations, or around
 ideation, brainstorming, or validation purposes rather 10.2% improvement, over baseline): their performance
 than direct solution generation. This polarized distribu­ was not significantly different from that of individuals
 tion points to two distinct patterns of AI usage: one using AI. This pattern suggests that AI’s immediate
 where participants heavily rely on AI-generated content impact appears to stem more from its capacity to bolster
 for their final solutions, and another where AI serves individual cognitive capabilities than affecting human-
 primarily as a collaborative tool for ideation and refine­
 to-human collaboration.
 ment rather than direct content generation, confirming
 Building on these performance patterns, perhaps
 the broad variety in the style of use of GenAI by workers
 our most noteworthy finding concerns AI’s role in
 (Randazzo et al. 2025b).
 blurring professional expertise boundaries. Organiza­
 tional theory has long emphasized the importance of
 6. Discussion specialized knowledge and clear functional bound­
 Our study offers insights about the potential impact
 aries. Our results suggest AI is starting to disrupt
 of GenAI on team collaboration in the workplace,
 this paradigm. Without AI, we observed clear pro­
 with implications for both theory and practice. Our
 fessional silos—commercial specialists submitted
 findings suggest that AI integration does more than
 predominantly commercial solutions, whereas R&D
 augment existing work processes and may also affect
 the nature of collaboration and expertise in organiza­ professionals favored technical approaches. When
 tional settings. Our results begin by confirming tradi­ teams worked without AI, they produced more
 tional assumptions about team effectiveness—teams balanced solutions through cross-functional collabo­
 without AI demonstrated modestly better performance ration. Interestingly, individuals using AI achieved
 (0.24 standard deviation, which represents around 6.3% similar levels of solution balance on their own, effec­
 improvement on the final outcome) compared with tively replicating the knowledge integration typically
 individuals working alone, reflecting the traditional achieved through team collaboration. This suggests
 benefits of cross-functional collaboration. However, the AI serves not just as an information provider but
 introduction of AI has the potential to gradually modify as an effective boundary-spanning mechanism, help­
 this performance landscape. Individuals working with ing professionals reason across traditional domain
 AI showed a 0.37 standard deviation performance boundaries and approach problems more holistically.
 increase (equating to around 9.6% improvement) over Complementing the expertise shift, our experimen­
 the baseline of working alone without AI.23 This finding tal design seems to reveal a well-documented eco­
 suggests that AI can effectively substitute for certain nomic principle at work: diminishing marginal returns
 collaborative functions, acting as a genuine teammate in team expansion. As we view GenAI as a cybernetic
 by granting individuals access to the varied expertise teammate, we can conceptualize our experimental

---

 Dell’Acqua et al.: The Cybernetic Teammate
 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s) 1235

 conditions onto a sequential expansion of team head emerging evidence on the psychological effects of con­
 count. We move from individual to dyad (human– versational AI (Li et al. 2023, De Freitas et al. 2024,

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 human or human–AI) to triad (human–human–AI), Riedl and Weidmann 2025). These findings should be
 and our results suggest that the first teammate addi­ interpreted cautiously, as they reflect immediate reac­
 tion, regardless of type, delivered significant average tions to AI collaboration rather than the complex
 quality gains.24 However, the subsequent addition yielded social dynamics that develop in long-term team rela­
 less significant average improvement, while increasing the tionships. Moreover, although AI reduced negative
 likelihood of producing top-decile, breakthrough ideas. emotions and friction in our setting, some level of con­
 This pattern echoes classic organizational research find­ structive disagreement can be valuable for creative
 ings where additional team members simultaneously exploration, meaning that lower tension does not
 contribute knowledge while increasing coordination com­ always imply better collaboration.
 plexity and diffusing individual accountability (Steiner These emotional patterns, in turn, suggest implica­
 1972, Latané et al. 1979, Hambrick and D’Aveni 1992, tions for learning dynamics in AI-augmented work
 Bernerth et al. 2023). Importantly, the cross-functional environments. The positive emotional responses to AI
 composition of commercial and R&D expertise in our collaboration could create a self-reinforcing cycle if
 dyads already matches the professional diversity that participants who reported the most positive emotional
 P&G’s experience suggests is most critical for early-stage experiences while working independently with AI
 product development. This pattern may indicate that opti­ showed the strongest preference for AI collaboration
 mal team configurations depend more on capturing essen­ over human teammates. The results of Tables 7 and 8
 tial functional expertise than on raw head count. suggest that positive initial AI experiences are corre­
 Although our design does not permit a clean separa­ lated with a higher expected likelihood of AI use in
 tion between AI augmenting noncollaborative tasks the participants’ future work. Hence, positive affect
 and AI substituting for collaborative functions, the may help turn a one-shot productivity boost into more
 magnitudes in Table 2 offer an illustrative guide. Indi­ sustained adoption, potentially accelerating organiza­
 viduals using AI performed about 0.37 standard devia­ tional learning curves.
 tions higher than individuals without AI, whereas Beyond examining whether AI improves outcomes,
 teams using AI outperformed teams without AI by our findings also help clarify how and where it contri­
 about 0.15 standard deviations. This pattern suggests butes to the creative process. Two common questions
 that roughly 40% of the solo performance improve­ arise: Does AI merely improve the presentation of ideas
 ment likely reflects AI enhancing noncollaborative
 rather than their substantive quality? And does AI
 aspects of work that also benefit teams, whereas the
 homogenize the quality distribution? First, regarding
 remaining 60% appears linked to AI substituting for
 presentation versus substance, our evidence suggests
 some collaborative functions that human teammates
 that AI improves idea quality. We find no relationship
 typically provide. Because individuals and teams
 between solution length and quality ratings among non-
 engage with AI in systematically different ways, this
 AI participants, indicating evaluators did not simply
 comparison should be viewed as indicative rather
 reward longer or more polished text. Similarly, control­
 than causal: it captures overlapping but not identical
 ling for typographical errors does not meaningfully alter
 processes of AI use across contexts. We view this as an
 indicative rather than definitive decomposition, but it our treatment effects.25 Our decomposition analysis fur­
 highlights that a meaningful portion of AI’s value ther suggests that AI’s benefits emerge at the idea-
 for solo workers comes from its capacity to partially generation stage itself: AI significantly increases the
 replicate the benefits of teamwork, rather than from average quality of the five initial ideas participants gen­
 surface-level assistance alone. erate before selecting one to develop further (Figure 8,
 Another important benefit of teamwork is the emo­ panel (a)), suggesting the improvements reflect better
 tional boost it provides all along the process. In that concepts from the outset rather than superior polish.
 regard, our result on the positive impact of AI on Second, regarding homogenization, we find that AI
 workers’ experience are particularly noteworthy. Con­ elevates rather than compresses the variance of quality
 trary to fears about AI creating negative workplace distribution. The range between the highest- and
 experiences, we found consistently positive emotional lowest-quality ideas remains similar across all condi­
 responses to AI use, including increased excitement tions, suggesting AI elevates the entire quality distribu­
 and enthusiasm, as well as reduced anxiety and frus­ tion rather than narrowing it toward a homogeneous
 tration. Unlike some earlier waves of technological mean.26 Moreover, AI-augmented teams were signifi­
 change, and even earlier iterations of AI technologies cantly more likely to produce high-quality ideas in the
 (Stein et al. 2015, Glikson and Woolley 2020, Dell’Ac­ top decile of the distribution, with Team + AI showing
 qua et al. 2025), GenAI’s interactive features appear to roughly three times the likelihood of breakthrough solu­
 create positive experiences for workers, aligning with tions compared with individuals without AI, indicating

---

 Dell’Acqua et al.: The Cybernetic Teammate
 1236 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s)

 that AI enhances rather than diminishes innovation comparable to traditional teams suggests opportuni­
 potential. ties for more flexible and efficient organizational struc­

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 Taken together, these results indicate that AI may be tures. At the same time, an important nuance emerges
 more than a passive tool and may function as a cyber­ when considering top-tier solutions: AI-augmented
 netic teammate. By interfacing with human problem teams were more likely to produce proposals ranking
 solvers—providing real-time feedback, stimulating the in the top decile, underscoring the unique synergy
 ideation process, bridging cross-functional expertise, produced by combining human collaboration with
 and influencing self-reported emotional states—GenAI AI-based augmentation. This may be a crucial consider­
 appears able to perform roles we typically associate ation for organizations, as different firms may respond
 with human collaborators. In this sense, AI not only differently. Some firms may focus on the efficiency side,
 enhances individual cognitive work but may also per­ whereas others may focus on the complementarity.28
 form some collective functions, such as ideation and The increased quality and comprehensiveness of
 iterative refinement, helping teams address complex AI-enabled work suggest opportunities to redesign
 challenges. Although AI cannot fully replicate the rich­ work processes and deliverable expectations. Organiza­
 ness of human social and emotional interaction, its tions should invest in developing their workers’ AI
 ability to contribute to collaborative work suggests the interaction capabilities, as this appears to be an increas­
 possibility of changes in how knowledge work is ingly critical skill. Given AI’s ability to break down
 structured and carried out.27 silos, there may also be value in training workers to
 This view aligns with a body of literature that con­ think more broadly across functional boundaries.
 ceptualizes AI not merely as a tool or a medium, but Two important caveats shape the interpretation of
 as an active “counterpart” within broader sociotechni­ these findings. First, our participants were relatively
 cal systems. Drawing on distributed cognition (Hutch­ inexperienced with AI prompting techniques, sug­
 ins 1991, 1995) and actor–network theory (Callon 1984; gesting the observed benefits may represent a lower
 Latour 1987, 2007), recent organizational scholarship bound. As users develop more sophisticated AI inter­
 argues for examining AI as an active counterpart in action strategies, the advantages of AI-enabled work
 systems of work involving multiple organizational
 could increase substantially. Second, the AI tools used
 actors and technologies (Anthony et al. 2023). Our
 were not optimized for collaborative work environments.
 study supports and extends these arguments by sug­
 Purpose-built collaborative AI systems could potentially
 gesting that GenAI can shape expertise sharing, team
 unlock significantly greater benefits by better supporting
 dynamics, and social engagement in ways that extend
 group dynamics and collective problem-solving pro­
 beyond the traditional boundaries of automation. In
 cesses. Related to this, we should also highlight two
 other words, AI’s role may be more than that of a tool
 organizational limitations. First, although we followed
 or facilitator, affecting patterns of collaboration. By
 treating AI as an active counterpart, we gain insight the firm’s early-stage product development routine, our
 into how GenAI mediates, and is mediated by, the col­ experiment relied on one-day virtual collaborations that
 lective processes involved in teamwork. did not fully capture the day-to-day complexities of team
 Along these lines, conceptualizing AI as a cybernetic interactions in organizations—such as extended coordina­
 teammate raises important questions about how humans tion challenges and iterative rework cycles. Second, we
 develop and apply theories of mind in human–AI collab­ focused on cross-functional pairs of human workers,
 oration (Kelley 1973, Malle 2006). Just as effective human whereas collaborations involving team members with
 teamwork relies on understanding teammates’ cognitive similar expertise, or in larger, more intricate team struc­
 processes, motivations, and decision-making patterns, tures, may exhibit different patterns of AI adoption and
 successful collaboration with AI will lead humans to effectiveness.
 form (possibly inaccurate) mental models of how AI sys­ Several scope conditions further shape the generaliz­
 tems process information, generate responses, and ability of our findings. Our study was conducted within
 approach problems (Glikson and Woolley 2020, Lebo­ a single company in the consumer goods industry, focus­
 vitz et al. 2022, Anthony et al. 2023). These “theories of ing on early-stage new product development through
 the AI mind” may significantly influence collaboration virtual interactions between largely unfamiliar partici­
 effectiveness. Unpacking how such theories arise, and pants. These conditions resemble flash teams rather than
 whether they track the technology’s jagged capabilities established organizational teams with embedded rela­
 (Dell’Acqua et al. 2023) remains a critical frontier for tionships and knowledge (Retelny et al. 2014, Valentine
 effective human–AI collaboration. and Edmondson 2015, Valentine and Bernstein 2025).
 These findings have significant organizational Additionally, our findings reflect the capabilities of a sin­
 implications. First, organizations may need to reeval­ gle AI model at a particular point in time, and all colla­
 uate optimal team sizes and compositions. The fact borations occurred remotely, where the dynamics of
 that AI-enabled individuals can perform at levels human–AI collaboration may differ from face-to-face

---

 Dell’Acqua et al.: The Cybernetic Teammate
 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s) 1237

 settings that involve nonverbal communication and expertise remains key to leveraging the use of technol­
 physical presence. ogy for innovative processes (Lazar et al. 2025): How

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 does AI integration affect the development of domain
 7. Conclusion expertise over time? What features of AI systems speci­
 Our research suggests that AI adoption may require fically support effective knowledge integration across
 reconsidering assumptions about team structures and professional boundaries? Does AI-enabled boundary
 organizational design. By showing that AI can raise spanning foster genuine knowledge growth, or merely
 individual performance to levels comparable to tradi­ facilitate temporary access to existing expertise? Stud­
 tional teams while also reducing professional silos, our ies examining how positive initial AI experiences
 findings contribute to both the emerging literature might create self-reinforcing adoption cycles could also
 on AI in organizations and classical theories of team clarify the emotional path of AI interactions within
 effectiveness. The increased likelihood of exceptional organizations.
 performance in AI-enabled teams, combined with Overall, our findings suggest that AI may be more
 evidence of reduced functional boundaries and posi­ than an advanced search engine or text generator,
 tive emotional effects, suggests interactions between instead playing a more active role in collaborative
 human and artificial capabilities that merit further work. By contributing to decision making, creativity,
 investigation. As organizations continue to integrate and emotional responses, AI may affect the conditions
 AI technologies, understanding these dynamics may under which teams form and function. Although ques­
 be important for organizational theory and practice. tions remain about how AI will influence long-term
 Future research should examine how these patterns skill development and trust, our evidence points to the
 evolve as users develop greater AI proficiency, how possibility of broader changes in knowledge work,
 different organizational contexts moderate these raising new questions about the evolving interplay
 effects, and how sustained AI use impacts the develop­ between human and machine contributions.
 ment and transfer of expertise within organizations.
 Against this backdrop, our findings suggest several Acknowledgments
 promising avenues for future research. First, how do The authors thank Ramona Pop for her critical help manag­
 the benefits of AI integration evolve as users become ing the experiment. The authors thank Andrea Dorbu, Bandy
 more sophisticated in their AI interactions? Given our Chin, Corey Gelb-Bicknell, Conor Mackey, Hadi Abbas, John
 participants’ relative inexperience with AI, under­ Kalil, Michael Menietti, Sarah Stegall-Rodriguez, and Vishnu
 standing the learning curve and potential ceiling effects Kulkarni for very helpful support and research assistance.
 becomes crucial. Second, researchers should investi­ The authors thank Iavor Bojinov, Jacqueline Lane, Simon
 Friis, and Brent Hecht for thoughtful comments. Seminar par­
 gate the economic principles governing team composi­
 ticipants at Harvard, New York University, ESSEC Business
 tion in AI-augmented environments. Our observation
 School, INSEAD, Bristol University, London Business School,
 of diminishing returns when expanding from dyads to Michigan Ross, Berkeley, Northeastern, Stanford, Wharton,
 triads raises several questions about optimal team siz­ OpenAI, the Organisation for Economic Co-operation and
 ing in the presence of AI teammates. Future work Development, the French Department of the Treasury, and
 could systematically vary both skill complementarity the European Commission provided helpful feedback. The
 and human–AI ratios to determine whether AI funda­ authors are grateful for the guidance of Sharique Hasan and
 mentally alters traditional team-scaling principles. three referees at Organization Science in helping to improve
 Finally, given the rapid pace of AI model advancement this paper. Procter & Gamble provided financial support to
 and increasing use of AI in organizations (Bick et al. the HBS AI Institute through gifts to Harvard Business
 2026), it is incumbent upon researchers to consider con­ School during the period 2023–2025. Karim Lakhani received
 ducting “clinical trials” of AI in partnership with orga­ compensation as a consultant for Procter & Gamble for the
 nizations. We believe that management scholars can period 2021–2022. The authors maintained full intellectual
 have a significant say in the rate and direction of AI independence throughout the study. Author contributions
 adoption and usage inside of organizations if they can are as follows: F.D.A., C.A., R.S., and K.R.L. established the
 collaboration and designed the experiment. F.D.A., C.A., and
 marshal causal evidence on AI’s positive and negative
 K.R.L. oversaw the execution of the experiment, and led the
 impact on individuals, teams and organizations.
 analyses, framing, and write-up. H.L. and E.M. contributed
 Furthermore, our findings on breakthrough innova­ to the experimental design. H.L., R.S., and E.M. contributed
 tions warrant deeper examination of exploration– to the framing. E.M. and L.M. contributed to the prompt
 exploitation dynamics in AI collaboration. Does AI’s training. Y.H., J.G., H.N., and S.T. facilitated organizational
 ability to enhance the right tail of performance apply access and enabled the execution of the experiment inside
 across different innovation contexts and task complexi­ P&G. All coauthors contributed to revisions of the manu­
 ties? This connects to multiple questions about expertise script. They used Claude, Manus, and ChatGPT for light
 development, especially given recent findings on how copyediting.

---

 Dell’Acqua et al.: The Cybernetic Teammate
 1238 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s)

 Endnotes self-directed collaboration rather than dependence on specific
 1 prompting techniques.
 Bernerth et al. (2023, pp. 1230–1231) define workplace teams as

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 15
 “two or more individuals who share some interdependency and LLM capabilities are rapidly evolving, and our specific effect
 responsibility of work tasks and collective outputs.” sizes should be interpreted as directional indicators rather than pre­
 2 cise estimates that will hold across all future models. However, the
 The term draws from Norbert Wiener’s (1948, 1950) foundational
 core mechanisms we identify (AI’s ability to provide continuous
 work on cybernetics, which describes feedback-regulated systems
 creative input, reduce ideation fatigue, and substitute for certain
 that dynamically adjust their behavior in response to environmental
 collaborative functions) represent core capabilities that are likely to
 inputs. Rather than simply automating tasks, such systems modify
 persist and strengthen as LLMs improve (Xiao et al. 2025) and get
 their functioning through iterative feedback loops, a property that
 increasingly adopted by organizations (Bick et al. 2026).
 makes them capable of participating in collaborative processes. 16
 3 Note that we consider the average of these values for the team
 This builds on existing literature investigating the adoption and conditions (with and without AI). Results are robust to the use of
 impact of earlier waves of AI technologies. See, for example, Bryn­ alternative specifications for these controls such as the sum or the
 jolfsson et al. (2019, 2018), Agrawal et al. (2018), Furman and Sea­ minimum or maximum of the team value.
 mans (2019), Iansiti and Lakhani (2020), Raisch and Krakowski 17
 (2021), Jacobides et al. (2021), and McElheran et al. (2024). As a robustness check, we also estimate all models with standard
 4
 errors clustered at the randomization-unit level (eight clusters
 This project (IRB24-0202) received institutional review board defined by business unit × geography) using wild cluster bootstrap
 approval. for clustered regressions. Results remain substantively unchanged
 5
 The study was preregistered at the American Economic Association (see Table A3 in the Online Appendix).
 Randomized Controlled Trial Registry (AEARCTR-0013603), detail­ 18
 Evaluators assessed five dimensions of each solution, Quality,
 ing our experimental conditions, outcome variables, and analytical Novelty, Feasibility, Impact, and Business Potential, using the same
 approaches. 1–10 scale and blinded evaluation process. When we combine these
 6
 A long literature in management confirms the benefit of this four measures into a composite index of overall quality, our results
 approach for successful innovation (e.g., Dougherty 1992). replicate. When we disaggregate them, we find that Novelty, Impact,
 7
 The detailed description of the tasks given to participants can be and Business Potential closely mirror the patterns reported for over­
 found in Online Appendix A. all Quality, whereas no significant differences emerge for Feasibility.
 19
 8
 Of the 791 participants who completed the workshop, 776 pro­ As a robustness check, we replicated all analyses using AI-generated
 vided complete data including post-task surveys. The 15 partici­ evaluations of the solutions. Results remain consistent across all
 pants with incomplete surveys were distributed across conditions models.
 20
 (4 from non-AI teams and 11 from AI teams), and their exclusion For two-person teams, we construct the team-level outcome by
 does not affect our main results. averaging the individual participants’ post-task changes in these
 9 composite measures.
 Thirty-five participants were not randomly assigned either because
 21
 they entered the product development workshop too late (in which Positive and negative emotions show no significant differences
 case they completed the task alone without AI) or because their between conditions in the preexperimental period, as can be seen in
 seniority was above band 3 (in which case they completed the task Table 1.
 alone with AI). All our analyses exclude these participants but our 22
 Teams where only one employee has as their core job to work on
 results are consistent when we include these nonrandomized partici­ new product development are classified as core-job teams. For
 pants. These participants were isolated in separate sessions and did teams without AI, teams with one core-job participant are indistin­
 not interact with randomly assigned participants, eliminating poten­ guishable from teams composed of two core-job participants.
 tial contamination effects. 23
 Although we cannot directly observe downstream development
 10
 The randomization clusters included a geographical component or commercialization decisions, this early-stage product develop­
 primarily in order to accommodate time-zone differences and ment task represents a core component of P&G’s innovation pipeline.
 ensure that team members could collaborate in real time. Our workshop involved approximately 800 professionals; running a
 11
 The nested structure refers to individuals being grouped within session of this scale would represent an investment exceeding one
 teams, which are further nested within business units and geograph­ million dollars. In this context, even a modest increase in the proba­
 ical regions, requiring careful statistical consideration. Maintaining bility of advancing a high-impact product concept could translate
 team integrity posed a significant challenge; if one member of a two- into hundreds of millions of dollars in additional expected revenue,
 person team failed to participate, the entire team was nullified, lead­ underscoring the economic significance of the productivity gains we
 ing us to automatically reassign individuals from incomplete teams document.
 24
 to individual assignments to preserve data collection opportunities. Although the point estimates are directionally consistent with
 12
 The random assignment of leadership role between R&D and diminishing marginal returns, the incremental differences between
 conditions are not statistically significant.
 commercial professionals had no statistically significant impact on
 25
 any of our team outcomes. See Table A2 in the Online Appendix.
 13 26
 Participants at the July workshop had access to GPT-4o. The We do observe, however, that AI-assisted solutions exhibit greater
 results remain consistent across the various workshop sessions. semantic similarity to one another in embedding space, consistent
 14 with recent evidence on LLM-driven content homogenization (Doshi
 Interestingly, despite providing structured prompts to all partici­
 and Hauser 2024, Wang et al. 2026). Whether this semantic conver­
 pants in AI-enabled conditions, only 38% actually utilized these
 gence carries implications for organizational innovation diversity
 suggested prompts in their interactions. Participants who did not fol­
 over time is an important question for future research.
 low the prompt guidance achieved performance levels equivalent to
 27
 those who did, with both groups significantly outperforming the con­ See Leonardi and Neeley (2022) and Farrell et al. (2025) for
 trol conditions. This pattern suggests that participants quickly related discussions.
 28
 adapted the AI tool to their own working styles rather than relying Our partner P&G was squarely focused on the potential for top
 on prescribed approaches, and that AI’s benefits reflect authentic, quality solutions.

---

 Dell’Acqua et al.: The Cybernetic Teammate
 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s) 1239

 References Brynjolfsson E, Mitchell T, Rock D (2018) What can machines learn
 Agrawal A, Gans J, Goldfarb A (2018) Prediction Machines: The Sim­ and what does it mean for occupations and the economy? AEA

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 ple Economics of Artificial Intelligence (Harvard Business Review Papers Proc. 108:43–47.
 Press, Boston). Brynjolfsson E, Rock D, Syverson C (2019) Artificial intelligence and
 Alchian AA, Demsetz H (1972) Production, information costs, and the modern productivity paradox. Agrawal A, Gans J, Goldfarb
 economic organization. Amer. Econom. Rev. 62(5):777–795. A, eds. The Economics of Artificial Intelligence: An Agenda (Uni­
 Ancona DG, Caldwell DF (1992) Bridging the boundary: External versity of Chicago Press, Chicago), 23–57.
 activity and performance in organizational teams. Admin. Sci. Brynjolfsson E, Rock D, Syverson C (2021) The productivity J-curve:
 Quart. 37(4):634–665. How intangibles complement general purpose technologies.
 Anthony C, Bechky BA, Fayard AL (2023) “Collaborating” with AI: Amer. Econom. J.: Macroeconomics 1(13):333–372.
 Taking a system view to explore the future of work. Organ. Sci. Callon M (1984) Some elements of a sociology of translation:
 34(5):1672–1694. Domestication of the scallops and the fishermen of St Brieuc
 Argote L (1999) Organizational Learning: Creating, Retaining and Trans­ Bay. Law J, ed. Power, Action and Belief: A New Sociology of
 ferring Knowledge (Kluwer Academic Publishers, Norwell, MA). Knowledge? (Routledge, Boston), 196–223.
 Argote L, Lee S, Park J (2021) Organizational learning processes and Cattani G, Ferriani S, Lanza A (2017) Deconstructing the outsider puz­
 outcomes: Major findings and future research directions. Man­ zle: The legitimation journey of novelty. Organ. Sci. 28(6):965–992.
 agement Sci. 67(9):5399–5429. Choudhary V, Marchetti A, Shrestha YR, Puranam P (2025) Huma­
 Ayers JW, Poliak A, Dredze M, Leas EC, Zhu Z, Kelley JB, Faix DJ, n-AI ensembles: When can they work? J. Management 51(2):
 et al. (2023) Comparing physician and artificial intelligence 536–569.
 chatbot responses to patient questions posted to a public social Cohen SG, Bailey DE (1997) What makes teams work: Group effec­
 media forum. JAMA Internal Medicine 183(6):589–596. tiveness research from the shop floor to the executive suite. J.
 Ayoubi C, Lane JN, Szajnfarber Z (2026) The two faces of expertise: Management 23(3):239–290.
 How skills and experience shape the evaluation of innovation. Csaszar FA (2012) Organizational structure as a determinant of per­
 Working paper, ESSEC Business School, Cergy, France. formance: Evidence from mutual funds. Strategic Management J.
 Ayoubi C, Pezzoni M, Visentin F (2017) At the origins of learning: 33(6):611–632.
 Absorbing knowledge flows from within the team. J. Econom. Csaszar FA, Ketkar H, Kim H (2024) Artificial intelligence and stra­
 Behav. Organ. 134:374–387. tegic decision-making: Evidence from entrepreneurs and inves­
 Bailey DE, Leonardi PM, Chong J (2010) Minding the gaps: Under­ tors. Strategy Sci. 9(4):322–345.
 standing technology interdependence and coordination in knowl­ Dahan E, Mendelson H (2001) An extreme-value model of concept
 edge work. Organ. Sci. 21(3):713–730. testing. Management Sci. 47(1):102–116.
 Balasubramanian N, Ye Y, Xu M (2022) Substituting human De Freitas JD, Uguralp AK, Uguralp Z, Puntoni S (2024) AI compa­
 decision-making with machine learning: Implications for orga­ nions reduce loneliness. Preprint, submitted July 26, https://
 nizational learning. Acad. Management Rev. 47(3):448–465. doi.org/10.2139/ssrn.4893097.
 Beane M (2019) Shadow learning: Building robotic surgical skill Dell’Acqua F (2022) Falling asleep at the wheel: Human/AI collabo­
 when approved means fail. Admin. Sci. Quart. 64(1):87–123. ration in a field experiment on HR recruiters. Working paper,
 Beane M, Anthony C (2024) Inverted apprenticeship: How senior Harvard Business School, Boston.
 occupational members develop practical expertise and preserve Dell’Acqua F, Kogut B, Perkowski P (2025) Super Mario meets AI:
 their position when new technologies arrive. Organ. Sci. 35(2): Experimental effects of automation and skills on team perfor­
 405–431. mance and coordination. Rev. Econom. Statist. 107(4):951–966.
 Beaudry A, Pinsonneault A (2010) The other side of acceptance: Dell’Acqua F, McFowland E, Mollick ER, Lifshitz-Assaf H, Kellogg
 Studying the direct and indirect effects of emotions on informa­ K, Rajendran S, Krayer L, Candelon F, Lakhani KR (2023) Navi­
 tion technology use. MIS Quart. 34(4):689–710. gating the jagged technological frontier: Field experimental evi­
 Becker GS, Murphy KM (1992) The division of labor, coordination dence of the effects of AI on knowledge worker productivity
 costs, and knowledge. Quart. J. Econom. 107(4):1137–1160. and quality. Working Paper 24-013, Technology and Operations
 Bernerth JB, Beus JM, Helmuth CA, Boyd TL (2023) The more the Management Unit, Harvard Business School, Boston.
 merrier or too many cooks spoil the pot? A meta-analytic exam­ Deming DJ (2017) The growing importance of social skills in the
 ination of team size and team effectiveness. J. Organ. Behav. labor market. Quart. J. Econom. 132(4):1593–1640.
 44(8):1230–1262. Deutsch M (1949) A theory of co-operation and competition. Human
 Bick A, Blandin A, Deming DJ (2026) The rapid adoption of genera­ Relations 2(2):129–152.
 tive AI. Management Sci., ePub ahead of print January 20, DiBenigno J, Kellogg KC (2014) Beyond occupational differences: The
 https://doi.org/10.1287/mnsc.2025.02523. importance of cross-cutting demographics and dyadic toolkits
 Boudreau KJ, Lacetera N, Lakhani KR (2011) Incentives and prob­ for collaboration in a US hospital. Admin. Sci. Quart. 59(3):
 lem uncertainty in innovation contests: An empirical analysis. 375–408.
 Management Sci. 57(5):843–863. Doshi AR, Hauser OP (2024) Generative AI enhances individual cre­
 Boudreau KJ, Guinan EC, Lakhani KR, Riedl C (2016) Looking ativity but reduces the collective diversity of novel content. Sci.
 across and looking beyond the knowledge frontier: Intellectual Adv. 10(28):eadn5290.
 distance, novelty, and resource allocation in science. Manage­ Doshi AR, Bell JJ, Mirzayev E, Vanneste BS (2025) Generative artifi­
 ment Sci. 62(10):2765–2783. cial intelligence and evaluating strategic decisions. Strategic
 Boussioux L, Lane JN, Zhang M, Jacimovic V, Lakhani KR (2025) Management J. 46(3):583–610.
 The crowdless future? How generative AI is shaping the future Dougherty D (1992) Interpretive barriers to successful product inno­
 of human crowdsourcing. Organ. Sci. 35(5):1589–1607. vation in large firms. Organ. Sci. 3(2):179–202.
 Brown SL, Eisenhardt KM (1995) Product development: Past Eloundou T, Manning S, Mishkin P, Rock D (2024) GPTs are GPTs:
 research, present findings, and future directions. Acad. Manage­ An early look at the labor market impact potential of large lan­
 ment Rev. 20(2):343–378. guage models. Science 384(6702):1306–1308.
 Brynjolfsson E, Li D, Raymond LR (2025) Generative AI at work. Faraj S, Sproull L (2000) Coordinating expertise in software develop­
 Quart. J. Econom. 140(2):889–942. ment teams. Management Sci. 46(12):1554–1568.

---

 Dell’Acqua et al.: The Cybernetic Teammate
 1240 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s)

 Faraj S, Pachidi S, Sayegh K (2018) Working and organizing in the Latour B (1987) Science in Action: How to Follow Scientists and Engineers
 age of the learning algorithm. Inform. Organ. 28(1):62–70. Through Society (Harvard University Press, Cambridge, MA).

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 Farrell H, Gopnik A, Shalizi C, Evans J (2025) Large AI models are Latour B (2007) Reassembling the Social: An Introduction to Actor-
 cultural and social technologies. Science 387(6739):1153–1156. Network-Theory (Oxford University Press, Oxford, UK).
 Furman J, Seamans R (2019) AI and the economy. Innovation Policy Lazar M, Lifshitz H, Ayoubi C, Emuna H (2025) Would Archimedes
 Econom. 19(1):161–191. shout “eureka” with algorithms? The hidden hand of algorithmic
 Garud R (1997) On the distinction between know-how, know-why, design in idea generation, the creation of ideation bubbles, and
 and know-what. Adv. Strategic Management 14:81–101. how experts can burst them. Acad. Management J. 68(5):881–906.
 Girotra K, Terwiesch C, Ulrich KT (2010) Idea generation and the Lazer D, Katz N (2003) Building effective intra-organizational net­
 quality of the best idea. Management Sci. 56(4):591–605. works: The role of teams. Working paper, Northeastern Univer­
 Glikson E, Woolley AW (2020) Human trust in artificial intelligence: sity, Boston.
 Review of empirical research. Acad. Management Ann. 14(2):627–660. Lebovitz S, Lifshitz-Assaf H, Levina N (2022) To engage or not to
 Hambrick D, D’Aveni R (1992) Top team deterioration as part of engage with AI for critical judgments: How professionals deal
 downward spiral of large corporate bankruptcies. Management with opacity when using AI for medical diagnosis. Organ. Sci.
 Sci. 38(10):1445–1466. 33(1):126–148.
 Hoffmann M, Boysel S, Nagle F, Peng S, Xu K (2024) Generative AI Leonardi P, Neeley T (2022) The Digital Mindset: What It Really Takes
 and the nature of work. CESifo working paper, Center for Eco­ to Thrive in the Age of Data, Algorithms, and AI (Harvard Busi­
 nomic Studies, Ludwig-Maximilians-Universität München, ness Review Press, Boston).
 Munich, Germany. Levina N, Vaast E (2005) The emergence of boundary spanning
 Hutchins E (1991) Organizing work by adaptation. Organ. Sci. competence in practice: Implications for implementation and
 2(1):14–39. use of information systems. MIS Quart. 29(2):335–363.
 Hutchins E (1995) Cognition in the Wild (MIT Press, Cambridge, MA). Levinthal DA (1997) Adaptation on rugged landscapes. Management
 Iansiti M, Lakhani KR (2020) Competing in the Age of AI: Strategy and Sci. 43(7):934–950.
 Leadership When Algorithms and Networks Run the World (Har­ Li JZ, Herderich A, Goldenberg A (2024) Skill but not effort drive
 vard Business Review Press, Boston). GPT overperformance over humans in cognitive reframing of
 Jacobides MG, Brusoni S, Candelon F (2021) The evolutionary dynam­ negative scenarios. Working paper, Harvard University, Cam­
 ics of the artificial intelligence ecosystem. Strategy Sci. 6(4):412–435. bridge, MA.
 Jeppesen LB, Lakhani KR (2010) Marginality and problem-solving Li D, Raymond LR, Bergman P (2026) Hiring as exploration. Rev.
 effectiveness in broadcast search. Organ. Sci. 21(5):1016–1033. Econom. Stud. 93(2):1200–1240.
 Johnson DW, Johnson RT (2005) New developments in social interde­ Li H, Zhang R, Lee Y-C, Kraut RE, Mohr DC (2023) Systematic
 pendence theory. Genetic Soc. General Psych. Monographs 131(4): review and meta-analysis of AI-based conversational agents for
 285–358. promoting mental health and well-being. NPJ Digital Medicine
 Jonassen Z, He VF, von Krogh G (2026) Good lessons despite bad 6(1):236.
 feelings: How boundary-spanning teams learn from collabora­ Lindbeck A, Snower DJ (2000) Multitask learning and the reorgani­
 tion failure. Organ. Sci. 37(1):17–47. zation of work: From Tayloristic to holistic organization. J.
 Jones BF (2009) The burden of knowledge and the “death of the Labor Econom. 18(3):353–376.
 Renaissance man”: Is innovation getting harder? Rev. Econom. Malle BF (2006) How the Mind Explains Behavior: Folk Explanations,
 Stud. 76(1):283–317. Meaning, and Social Interaction (MIT Press, Cambridge, MA).
 Kacperczyk A, Younkin P (2017) The paradox of breadth: The ten­ March JG (1991) Exploration and exploitation in organizational
 sion between experience and legitimacy in the transition to learning. Organ. Sci. 2(1):71–87.
 entrepreneurship. Admin. Sci. Quart. 62(4):731–764. March JG, Simon HA (1958) Organizations (John Wiley & Sons, New
 Kelley HH (1973) The processes of causal attribution. Amer. Psych. York).
 28(2):107–128. McElheran K, Li JF, Brynjolfsson E, Kroff Z, Dinlersoz E, Foster L,
 Kellogg KC, Orlikowski WJ, Yates J (2006) Life in the trading zone: Zolas N (2024) AI adoption in America: Who, what, and where.
 Structuring coordination across boundaries in postbureaucratic J. Econom. Management Strategy 33(2):375–415.
 organizations. Organ. Sci. 17(1):22–44. Mollick E (2024) Co-Intelligence (Random House, London).
 Kellogg KC, Valentine MA, Christin A (2020) Algorithms at work: Nelson RR, Winter SG (1982) An Evolutionary Theory of Economic
 The new contested terrain of control. Acad. Management Ann. Change (Harvard University Press, Cambridge, MA).
 14(1):366–410. Nickerson JA, Zenger TR (2004) A knowledge-based theory of
 Kogut B, Zander U (1992) Knowledge of the firm, combinative the firm—The problem-solving perspective. Organ. Sci. 15(6):
 capabilities, and the replication of technology. Organ. Sci. 3(3): 617–632.
 383–397. Noy S, Zhang W (2023) Experimental evidence on the productivity
 Kozlowski SWJ, Bell BS (2013) Work groups and teams in organiza­ effects of generative artificial intelligence. Science 381(6654):
 tions: Review update. Schmitt N, Highhouse S, eds. Handbook of 187–192.
 Psychology, Vol. 12: Industrial and Organizational Psychology, 2nd Orlikowski WJ (2002) Knowing in practice: Enacting a collective
 ed. (Wiley, Hoboken, NJ), 412–469. capability in distributed organizing. Organ. Sci. 13(3):249–273.
 Lane JN (2023) The subjective expected utility approach and a frame­ Otis N, Clarke RP, Delecourt S, Holtz D, Koning R (2024) The
 work for defining project risk in terms of novelty and feasibility–A uneven impact of generative AI on entrepreneurial perfor­
 response to Franzoni and Stephan (2023), “uncertainty and risk- mance. Preprint, submitted January 17, https://doi.org/10.2139/
 taking in science.” Res. Policy 52(3):104707. ssrn.4671369.
 Lane JN, Boussioux L, Ayoubi C, Hao Chen Y, Lin C, Spens R, Wagh Page SE (2019) The Diversity Bonus: How Great Teams Pay off in the
 P, Wang PH (2026) The narrative AI advantage? A field experi­ Knowledge Economy (Princeton University Press, Princeton, NJ).
 ment on AI-augmented evaluations of early-stage innovations. Peng S, Kalliamvakou E, Cihon P, Demirer M (2023) The impact of AI
 Working Paper No. 25-001, Harvard Business School, Boston. on developer productivity: Evidence from GitHub copilot. Pre­
 Latané B, Williams K, Harkins S (1979) Many hands make light the print, submitted February 13, https://arxiv.org/abs/2302.06590.
 work: The causes and consequences of social loafing. J. Personal­ Puranam P (2018) The Microstructure of Organizations (Oxford Uni­
 ity Soc. Psych. 37(6):822–832. versity Press, New York).

---

 Dell’Acqua et al.: The Cybernetic Teammate
 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s) 1241

 Raisch S, Fomina K (2025) Combining human and artificial intelli­ Wiener N (1950) The Human Use of Human Beings: Cybernetics and
 gence: Hybrid problem-solving in organizations. Acad. Manage­ Society, 1st ed. (Houghton Mifflin, Boston).

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 ment Rev. 50(2):441–464. Wuchty S, Jones BF, Uzzi B (2007) The increasing dominance of
 Raisch S, Krakowski S (2021) Artificial intelligence and manage­ teams in production of knowledge. Science 316(5827):1036–1039.
 ment: The automation–augmentation paradox. Acad. Manage­ Xiao C, Cai J, Zhao W, Lin B, Zeng G, Zhou J, Zheng Z, Han X, Liu
 ment Rev. 46(1):192–210. Z, Sun M (2025) Densing law of LLMs. Nature Machine Intelli­
 Raj M, Seamans R (2019) Primer on artificial intelligence and robot­ gence 7:1823–1833.
 ics. J. Organ. Design. 8(1):11. Zander U, Kogut B (1995) Knowledge and the speed of the transfer
 Randazzo S, Joshi A, Kellogg KC, Lifshitz H, Dell’Acqua F, Lakhani and imitation of organizational capabilities: An empirical test.
 KR (2025a) GenAI as a power persuader: How professionals Organ. Sci. 6(1):76–92.
 get persuasion bombed when they attempt to validate LLMs.
 Working paper, Warwick Business School, Coventry, UK. Fabrizio Dell’Acqua is a postdoctoral researcher at Harvard
 Randazzo S, Lifshitz-Assaf H, Kellogg K, Dell’Acqua F, Mollick ER, Can­ Business School and HBS AI Institute. He received his PhD in man­
 delon F, Lakhani KR (2025b) Cyborgs, centaurs and self-automa­ agement from Columbia Business School. His research examines
 tors: The three modes of human-GenAI knowledge work and their how human–AI collaboration reshapes knowledge work at the indi­
 implications for skilling and the future of expertise. The Wharton vidual, team, and organizational levels. Prior to his PhD, he
 School Research Paper, Harvard Business School Working Paper, received degrees in economics from Bocconi University and London
 (26-036), 26-036. Business School.
 Retelny D, Robaszkiewicz S, To A, Lasecki WS, Patel J, Rahmati N, Charles Ayoubi is an assistant professor of management at
 Doshi T, Valentine M, Bernstein MS (2014) Expert crowdsour­ ESSEC Business School, Paris, France. He received his PhD in inno­
 cing with flash teams.Proc. 27th Annual ACM Sympos. User Inter­ vation economics from the École Polytechnique Fédérale de Lau­
 face Software Tech. (Association for Computing Machinery, New sanne. Prior to joining ESSEC, he was a postdoctoral research fellow
 York), 75–85. at Harvard Business School in the Digital Data Design Institute. His
 Riedl C, Weidmann B (2025) Quantifying human-AI synergy. Work­ research explores how organizations generate, evaluate, and diffuse
 ing paper. innovative ideas, with a focus on how generative AI is reshaping
 Rivkin JW (2000) Imitation of complex strategies. Management Sci. decision making, and business opportunities.
 46(6):824–844. Hila Lifshitz is a professor of management at Warwick Business
 Singh J, Fleming L (2010) Lone inventors as sources of break­ School and affiliated faculty at Harvard’s Digital Data Design Insti­
 throughs: Myth or reality? Management Sci. 56(1):41–56. tute. She is the head of the Artificial Intelligence Innovation Net­
 Souitaris V, Peng B, Zerbinati S, Shepherd DA (2023) Specialists, work at Warwick University. She conducts field studies exploring
 generalists, or both? Founders’ multidimensional breadth of the transformation of day-to-day knowledge work processes and
 experience and entrepreneurial ventures’ fundraising at IPO. the use of AI for innovation processes as well as for critical
 Organ. Sci. 34(2):557–588. decision-making processes. She earned her doctorate from Harvard
 Stein MK, Newell S, Wagner EL, Galliers RD (2015) Coping with Business School.
 information technology. MIS Quart. 39(2):367–392. Raffaella Sadun is the Charles E. Wilson Professor of Business
 Steiner ID (1972) Group Process and Productivity (Academic Press, Administration at Harvard Business School (HBS). She received her
 New York). PhD in economics from the London School of Economics. Her research
 Tarafdar M, Cooper CL, Stich JF (2019) The technostress trifecta— focuses on managerial and organizational drivers of productivity and
 Techno eustress, techno distress and design: Theoretical direc­ growth, with emphasis on the measurement of management practices
 tions and an agenda for research. Inform. Systems J. 29(1):6–42. across organizations and countries. She cofounded the World Manage­
 Teodoridis F (2018) Understanding team knowledge production: ment Survey and coleads the Digital Reskilling Lab at HBS.
 The interrelated roles of technology and expertise. Management Ethan Mollick is the Ralph J. Roberts Distinguished Faculty
 Sci. 64(8):3625–3648. Scholar, a Rowan Fellow, and an associate professor of management
 Terwiesch C, Loch CH (2004) Collaborative prototyping and the at the Wharton School of the University of Pennsylvania. He received
 pricing of custom-designed products. Management Sci. 50(2): his PhD and MBA from the Massachusetts Institute of Technology
 145–158. Sloan School of Management. His research interests include the effects
 Terwiesch C, Xu Y (2008) Innovation contests, open innovation, and of artificial intelligence on work and education, with particular
 multiagent problem solving. Management Sci. 54(9):1529–1543. emphasis on how emerging technologies transform organizational
 Valentine M, Bernstein M (2025) Flash Teams: Leading the Future of processes and individual performance.
 AI-Enhanced, On-Demand Work (MIT Press, Cambridge, MA). Lilach Mollick is the codirector of the Wharton Generative AI
 Valentine MA, Edmondson AC (2015) Team scaffolds: How mesole­ Labs. Her work focuses on the development of pedagogical strate­
 vel structures enable role-based coordination in temporary gies that include artificial intelligence and interactive methodologies.
 groups. Organ. Sci. 26(2):405–422. She has worked with Wharton to develop a wide range of educa­
 Vuori TO, Huy QN (2016) Distributed attention and shared emo­ tional tools and games used in classrooms worldwide. She has also
 tions in the innovation process: How Nokia lost the smart­ written several papers on the uses of AI for teaching and training,
 phone battle. Admin. Sci. Quart. 61(1):9–51. and her work on AI has been discussed in publications including
 Wang D, Huang D, Shen H, Uzzi B (2026) A large-scale comparison the New York Times and Vox.
 of divergent creativity in humans and large language models. Yi Han is a researcher and innovation leader at Procter & Gam­
 Nature Human Behav. 10:531–540. ble. His work focuses on the application of artificial intelligence and
 Weber RA, Camerer CF (2003) Cultural conflict and merger failure: digital technologies in innovation processes, with particular empha­
 An experimental approach. Management Sci. 49(4):400–415. sis on how large organizations integrate emerging technologies to
 Weidmann B, Deming DJ (2020) Team players: How social skills drive product and business transformation. His research interests
 improve group performance. NBER Working Paper No. 27071, include AI-enabled innovation, organizational capabilities, and digi­
 National Bureau of Economic Research, Cambridge, MA. tal transformation.
 Wiener N (1948) Cybernetics: Or Control and Communication in the Jeff Goldman is vice president of enterprise AI at P&G, leading
 Animal and the Machine (MIT Press, Cambridge, MA). P&G’s global AI organization across data science, AI engineering,

---

 Dell’Acqua et al.: The Cybernetic Teammate
 1242 Organization Science, 2026, vol. 37, no. 4, pp. 1217–1242, © 2026 The Author(s)

 and AI factory. He founded P&G’s Global Data Science organiza­ innovation programs across multiple business units and regions,
 tion, served as analytic advisor to P&G’s C-suite, led business ana­ including advancing product and package superiority through the

Downloaded from informs.org by [2a02:a456:278c:0:d04a:3b49:409a:335c] on 14 September 2026, at 22:32 . For personal use only, all rights reserved.
 lytics for Global Markets and the Western European Analytics, and integration of digital, data, and artificial intelligence capabilities. He is
 founded the Business Analytics group for China and Product Sup­ also a Harvard Business School, HBS AI Institute Industry Fellow.
 ply Analytics for Asia. He holds a BA in economics and a master’s Karim R. Lakhani is the Dorothy & Michael Hintze Professor of
 in operations research from Cornell. Business Administration at Harvard Business School, specializing in
 Hari Nair is vice president of R&D at Procter & Gamble. He received technology management, open innovation, and AI strategy and
 his BSc in chemical engineering from University of Wisconsin–Madison transformation. He is the founding chair of Harvard’s Digital Data
 and is also a 2019 Harvard Advanced Leadership Initiative Fellow. Design Institute and the Laboratory for Innovation Science. His
 Stew Taub is vice president of R&D for innovation transforma­ work includes pioneering field experiments with organizations like
 tion at Procter & Gamble, where he leads enterprise-wide work on NASA, Harvard Medical School, the Broad Institute, and Procter &
 how to create more meaningful innovation, faster. He has led Gamble. He holds a PhD in management from MIT.

---
