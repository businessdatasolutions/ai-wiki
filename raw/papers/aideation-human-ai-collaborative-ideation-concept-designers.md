---
title: "AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers"
authors: ["Wen-Fan Wang", "Chien-Ting Lu", "Nil Ponsa i Campanyà", "Bing-Yu Chen", "Mike Y. Chen"]
affiliations: ["National Taiwan University"]
venue: "CHI Conference on Human Factors in Computing Systems (CHI 2025), ACM"
doi: "10.1145/3706598.3714148"
url: "https://doi.org/10.1145/3706598.3714148"
date_published: 2025-04-25
attachment: aideation-human-ai-collaborative-ideation-concept-designers.pdf
fulltext_source: pdf-converted
converter: "pdftotext -layout"
notes: |
  Acquired 2026-09-15 from a PDF the user placed in raw/articles/ as `3706598.3714148.pdf`
  (the ACM DOI suffix, no human-readable name). **Routing corrected at Process time**: this is a
  peer-reviewed CHI paper, not an article, so it was moved to raw/papers/ per CLAUDE.md
  §Pre-flight check — `item_type` / landing folder is a routing hint, not ground truth.
  28 pages, text extracted with `pdftotext -layout`; column padding collapsed, page breaks
  rendered as `---`. Figures are absent (pdftotext is text-only) and figure captions survive
  inline — a figure-heavy HCI paper, so read the PDF alongside for anything visual.
---

AIdeation: Designing a Human-AI Collaborative Ideation System
 for Concept Designers
 Wen-Fan Wang Chien-Ting Lu Nil Ponsa i Campanyà
 National Taiwan University National Taiwan University National Taiwan University
 Taipei, Taiwan Taipei, Taiwan Taipei, Taiwan
 vann@cmlab.csie.ntu.edu.tw b09902109@csie.ntu.edu.tw r12944063@csie.ntu.edu.tw

 Bing-Yu Chen Mike Y. Chen
 National Taiwan University National Taiwan University
 Taipei, Taiwan Taipei, Taiwan
 robin@ntu.edu.tw mikechen@csie.ntu.edu.tw

Figure 1: AIdeation, an ideation tool designed to support concept designers in exploring ideas in both breadth and depth, with
flexible iterative refinement. The figure illustrates the ideation cycle using a real-world project example from our field study,
showcasing AIdeation’s key design components. The process starts with the designer’s input and moves through the ideation
cycle: (a) Breadth by Brainstorming: AIdeation generates a variety of ideas based on the input; (b) Depth by Research: AIdeation
provides keywords extracted from the design ideas, helping the designer understand the key elements of the generated concepts.
The Designer can click on keywords to search for relevant references, enhancing their understanding of the elements; (c) Idea
Refinement: The Designer iteratively refine the idea by combining searched references or giving instructions. (d) Once the
desired result is achieved, the designer can begin a new ideation cycle using new input building on the current idea.
Abstract elements to form cohesive designs. However, existing AI tools fo-
Concept designers in the entertainment industry create highly de- cus on image generation from user specifications, lacking support
tailed, often imaginary environments for movies, games, and TV for the unique needs and complexity of concept designers’ work-
shows. Their early ideation phase requires intensive research, brain- flows. Through a formative study with 12 professional designers,
storming, visual exploration, and combination of various design we captured their workflows and identified key requirements for
 AI-assisted ideation tools. Leveraging these insights, we developed
 AIdeation to support early ideation by brainstorming design con-
 cepts with flexible searching and recombination of reference images.
This work is licensed under a Creative Commons Attribution 4.0 International License. A user study with 16 professional designers showed that AIdeation
CHI ’25, Yokohama, Japan significantly enhanced creativity, ideation efficiency, and satisfac-
© 2025 Copyright held by the owner/author(s). tion (all p<.01) compared to current tools and workflows. A field
ACM ISBN 979-8-4007-1394-1/25/04
https://doi.org/10.1145/3706598.3714148
 study with 4 studios for 1 week provided insights into AIdeation’s

---

CHI ’25, April 26–May 01, 2025, Yokohama, Japan Wang Lu Ponsa Chen Chen

benefits and limitations in real-world projects. After the completion the success of these advancements, this work aims to develop a
of the field study, two studios, covering films, television, and games, flexible system that leverages concept designers’ domain knowl-
have continued to use AIdeation in their commercial projects to edge, focusing on facilitating iterative ideation and enhancing their
date, further validating AIdeation’s improvement in ideation quality workflows.
and efficiency. We structure this work into four parts: 1) a formative study to
 understand the workflow, ideation processes, and needs of concept
CCS Concepts designers using both traditional methods and AI tools; 2) the design
• Human-centered computing → Interactive systems and and implementation of a human-AI collaborative ideation system;
tools; User centered design. 3) a summative study focusing on the ideation process; and 4) a
 field study in real-world commercial projects to assess its quality
Keywords and efficiency of the final design outcomes.
 We conducted a formative study with 12 professional environ-
Generative AI, Human-Centered AI, Concept Design, Creativity
 ment concept designers. Among character, prop, and environment
Support Tool, Visual Exploration
 concept designs, we focused on environment concept design for the
ACM Reference Format: scope of this paper because it typically requires the most concept
Wen-Fan Wang, Chien-Ting Lu, Nil Ponsa i Campanyà, Bing-Yu Chen, design resources and involves designing complex spatial and vi-
and Mike Y. Chen. 2025. AIdeation: Designing a Human-AI Collaborative sual elements across both large (macro) and detailed (micro) scales.
Ideation System for Concept Designers. In CHI Conference on Human Factors Through in-depth interviews and workflow analyses, we examined
in Computing Systems (CHI ’25), April 26–May 01, 2025, Yokohama, Japan.
 participants’ design processes, reference-gathering strategies, and
ACM, New York, NY, USA, 28 pages. https://doi.org/10.1145/3706598.3714148
 their use of GenAI tools. Designers often struggle to gather diverse,
 relevant references, especially for unique or poorly defined topics.
1 INTRODUCTION Traditional search tools often do not align with the creative inten-
Concept design is the initial step in visual development within tions of designers or provide sufficient material to blend different
the entertainment industry, including films, TV shows, and video styles and themes. Additionally, generating multiple unique design
games [3, 39, 64, 73, 88, 92]. Concept designers collaborate with art variations under tight deadlines is a major obstacle, with partici-
directors to visualize core ideas through initial sketches to define pants citing limited time, insufficient reference diversity, and the
the aesthetic and visual tone of the projects [92], along with detailed extensive effort required to create complex designs. While GenAI
character, environment, and prop design to provide blueprints for tools offer potential, participants noted critical limitations, includ-
computer graphics (CG) and set construction teams [39, 88]. For ing difficulties in formulating prompts, low diversity in outputs, AI
fantasy and sci-fi settings, everything needs to be designed and hallucinations, lack of detailed information, and limited flexibility
created by concept designers [3]. for refining results. These findings highlight the need for tools that
 The concept design workflow consists of two main phases [1, better support concept design workflows’ iterative and exploratory
64, 73]: 1) early ideation (or blue sky) phase, where raw ideas are nature.
researched, brainstormed, and explored, followed by the 2) final Based on our observations, we designed AIdeation to bridge
concept phase, where approved concepts are refined with detailed the gap between GenAI and concept design, enhancing the early
specifications for use by the production teams. Literature has de- ideation phase of concept designers. The key components of AIdeation
scribed several challenges during the early ideation phase [1, 21, include:
64, 102], including difficulties in finding references that align with
their creative vision [63, 64, 96] combined with extreme time con- (1) Brainstorming: Supporting Breadth Exploration: AIdeation
straints with designers being expected to deliver multiple designs generates a wide variety of diverse design ideas based on
daily [21, 64, 102], resulting in limited depth of research [1, 64] and user input, which can be in the form of natural language, im-
limited unique designs incorporating diverse elements explored (i.e. ages, or both (Figure 1-a). These design ideas are presented
limited breadth) [64, 102, 107]. visually, providing an overview that helps designers quickly
 With the rapid advancement of generative AI (GenAI), con- grasp different directions while offering high-diversity vari-
cept designers and studios have adopted them into their work- ations for further exploration.
flows [10, 62, 83, 90, 110]. Recent studies highlight challenges faced (2) Research: Supporting Depth Exploration: AIdeation ex-
by artists and designers in integrating GenAI into their workflows. tracts key design elements from the generated ideas and
Crafting effective prompts often requires significant trial and er- presents them as keywords to help designers explore further
ror, as users struggle with optimal structures [71]. Additionally, into the visual elements. These keywords also link to corre-
many tools lack intuitive design, posing barriers for non-technical sponding search results, supporting the reference-gathering
users [93]. GenAI’s single-step generation contrasts with the iter- process (Figure 1-b).
ative, reflective practices of human creativity [123], and outputs (3) Refining Idea: Supporting Flexible Iterative Exploration:
often misalign with users’ visions, necessitating extensive fine- AIdeation allows designers to refine their ideas through an
tuning and post-editing [71, 110]. However, recent research in HCI iterative process (Figure 1-c). Users can refine their designs
shows promise in better integrating GenAI into traditional cre- by combining them with additional references or issuing
ative workflows, such as graphic design [23, 96], animation [103], natural language instructions to adjust specific elements.
fashion design [28, 53], and interior design [46, 111]. Motivated by This flexibility helps designers experiment with both broad

---

AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers CHI ’25, April 26–May 01, 2025, Yokohama, Japan

 and focused refinements, aligning design ideas with their design fields, such as architecture [78], product design [9], and inter-
 creative intent while maintaining design diversity. active design [81], not only do these fields rely on visual references,
 To evaluate AIdeation, we conducted a summative study focus- but they also require extensive research to gather factual knowl-
ing on the ideation process and a field study to examine its impact edge and data. A previous study highlights research methodologies
in real-world settings and the final design outcomes. The summa- tailored for designers, emphasizing the potential of integrating
tive study employed a within-subjects design with 16 professional research into the iterative creative process [30]. Both visual ex-
environment concept designers, using their original workflow as ploration and research serve as core sources of inspiration [34],
the baseline. The study simulated real-world tasks where designers fostering innovation and preventing design fixation [7, 27].
were assigned topics involving both exterior and interior scenes. Once a variety of ideas are generated, convergent thinking helps
Findings showed that participants significantly preferred AIdeation designers identify the most effective solution [52]. During this
for enhancing creativity (p = 0.001), found it more efficient for phase, designers utilize the resources collected earlier to sketch the
generating diverse ideas (p = 0.003) while maintaining comparable evolving idea on paper [49, 65, 114]. They continuously evaluate
quality, and reported higher satisfaction (p = 0.005) and enjoyment and iteratively refine their ideas, explore different aesthetics, and
(p = 0.005) with AIdeation. ensure clear communication with stakeholders until a satisfactory
 For the field study, we collaborated with 4 design studios and 8 result is achieved [55, 97, 99].
professional environment concept designers, who used AIdeation Numerous studies have proposed frameworks based on similar
as part of their ongoing commercial projects for one week. All concepts to support the iterative process, such as the Wizard of Oz
studios reported improved creativity, with 3 reporting improved approach [32] and Muse [77]. AIdeation integrates these insights
efficiency and quality. After the completion of the field study, 2 to enhance concept designers’ design process, supporting flexible
studios have continued using AIdeation for commercial projects to divergent and convergent thinking while bridging designers with
date. the latest GenAI tools that preserve the core elements of creativity
 In summary, our key contributions are as follows: and exploration.
 • An in-depth understanding of concept designers’ workflows
 2.2 GenAI as a Catalyst for Visual Exploration
 in the early ideation stage and how AI design tools are cur-
 rently used in practice. and Ideation
 • The design and implementation of a system, AIdeation, that With the advancement of GenAI tools, many design domains have
 allows concept artists to rapidly explore creative ideas through already integrated them into creative processes [62, 83]. Design-
 a flexible, iterative approach. Designed with a human-centered ers and artists extensively use general image generation tools to
 AI process, it addresses key barriers to GenAI adoption, in- transform text prompts into visuals [36, 86]. However, these tools
 cluding AI factual accuracy and lack of transparency/creative are not specifically adapted to designers’ creative process [10, 110].
 control. Recent research has increasingly focused on enhancing user expe-
 • Empirical evidence that AIdeation improves creativity, satis- rience with image-generation tools. Reprompt [112] automatically
 faction, and efficiency of concept artists’ workflow through: refines the text prompts for the generated images. Promptify [11],
 1) a comparative study with 16 professional concept design- PromptCharm [113] and DesignPrompt [82] introduce interactive
 ers; 2) a field deployment to production use in 4 studios; and prompt refinement to improve text-to-image generation workflows.
 3) continued usage to date by two studios after the comple- IntentTuner [120] combines fine-tuning and generation functional-
 tion of the field study. ities to support a flexible workflow for text-to-image generation.
 StyleFactory [125] facilitates style alignment in image creation.
2 RELATED WORK DreamSheets [4] enables users to explore the relationship between
We aim to integrate GenAI into the ideation process of concept de- input prompts and image outputs through a spreadsheet interface.
signers and enhance their workflows. To achieve this, we reviewed Collectively, these tools reduce the burden on designers to craft
related work in three key areas: (1) ideation within the design pro- intricate prompts and help generate visuals that better align with
cess, (2) GenAI tools that support visual exploration and ideation their intentions.
for designers, and (3) human-centered approaches for integrating Additionally, recent research explores the potential of GenAI
AI into workflows. by closely examining designers’ needs during the ideation pro-
 cess. Researchers designed systems and user interfaces specifically
2.1 Idea Exploration Process of Designers to address the challenges they face. For visual exploration, Gen-
 Query [96] addresses the challenge of reference search by support-
Like many other creative professionals, concept designers engage ing expressive visual searches and enabling iterative refinement
in an iterative process throughout their ideation workflows [2]. The of image-based queries. CreativeConnect [23] streamlines the tra-
process starts with divergent thinking, where the designer explores ditionally time-consuming process of recombining references by
various possibilities and generates diverse ideas without the burden providing automated suggestion options. C2Ideas [46] assisted in-
of constraints [47, 59, 68, 115, 117]. During this stage, designers con- terior designers in generating color schemes aligned with user
duct intensive visual exploration [24, 40], accumulate a collection of intentions. For ideation, DesignAID [12] and MuseTree1 combat
references [116], and organize in reference boards [33]. This visual creative blocks by using large language models (LLM) to deliver
process encourages designers to absorb visual elements, inspiring
their future designs [66]. Similarly to concept design, in some other 1 MuseTree, https://www.asus.com/proart/software-solutions/musetree/

---

CHI ’25, April 26–May 01, 2025, Yokohama, Japan Wang Lu Ponsa Chen Chen

diverse prompts and generate visuals. These systems effectively in- customization of AI recommendations and provides clear explana-
tegrate GenAI to address specific challenges in traditional ideation tions, enhancing user engagement and improving overall accuracy.
processes across various domains. In aviation, the AI Support System for Pilots’ Decision-Making Pro-
 Recent works have explored new possibilities for human-AI col- cess [37] highlights the importance of transparent feedback loops,
laboration in creativity. A study found AI can foster novel communi- enabling pilots to understand AI recommendations. Its real-time
cation, with designers curating and refining generated images [22]. guidance and customization enhance decision-making, safety, and
Optimuse [124] aligns with designers’ nonlinear creative processes efficiency, especially under information overload. Both approaches
and proposes a human-AI co-design framework that supports it- emphasize user control and refining AI contributions to effectively
erative idea exploration and flexible communication. COFI [85] augment human expertise.
advocates for AI systems that balance divergent and convergent While many studies demonstrate how GenAI can enhance cre-
process, and calls for expanding AI’s creative roles beyond genera- ative processes and design workflows, no tool fully addresses the
tion and evaluation to include conceptual exploration. These works complexities of concept designers’ workflows. Concept design re-
mentioned above provide valuable insights to integrate GenAI into quires specialized support throughout the iterative process, from
the creative process, such as optimizing user experience, design- research and brainstorming to refining ideas. These threads of work
ing tools to address specific challenges, and exploring models of offer valuable inspiration for developing AIdeation, paving the way
human-AI collaboration. for a solution tailored to the unique needs of concept designers.

2.3 Human-Centered AI for Workflow Support 3 BACKGROUND: WORKFLOW OF THE
With advancements in AI, human-centered AI (HCAI) has emerged ENTERTAINMENT INDUSTRY AND
as a crucial approach to enhance human abilities by fostering collab- CONCEPT DESIGNERS
oration between humans and AI systems. It emphasizes a symbiotic The entertainment industry’s production process, whether for films,
relationship where AI tools enhance human capabilities and stream- TV shows, or video games, transforms creative ideas into final
line workflows in various domains [94, 108, 118]. In alignment with products through a series of four stages: 1) development, where
user needs, these systems amplify human expertise while ensur- the initial concept and creative direction are set; 2) pre-production,
ing transparency and explainability, helping users understand the involving detailed planning and preparation; 3) production, where
decisions and limitations of AI [35, 60]. Through effective commu- the main content is created; and 4) post-production, which includes
nication, iterative feedback, and user control, these systems create editing, enhancing, and polishing of the final product [39, 64, 75,
dynamic collaborations to enhance workflows [45, 91, 105]. 95, 98].
 Recent research has applied these principles across various fields. Concept designers are pivotal across the first three stages, par-
In the creative industry, researchers have delved deeply into do- ticularly in the pre-production stage. During development, concept
main knowledge and workflows of different design disciplines, designers collaborate with art directors/clients to visualize core
crafting systems thoughtfully tailored to align with user work- ideas through initial sketches and designs to define the project’s
flows [5, 61, 74]. For example, RoomDreaming [111] generates pho- aesthetic and visual tone [92]. During pre-production, they design
torealistic interior design alternatives and enables the user to clearly scenes, characters, environments, and props to provide blueprints
understand and iteratively refine their options, allowing designers for computer graphics (CG) and set construction teams [39, 88].
to work collaboratively with their clients. MemoVis [20] enables During production, their work ensures consistency as concepts are
feedback providers to create companion reference images for 3D de- translated into tangible assets [64, 73]. Figure 2 shows actual exam-
signs with real-time viewpoints, democratizing actionable feedback ples of concept designs that led to their final products in several
regardless of 3D expertise. Both works reduce the communication well-known movies and games.
time between clients and designers. PlantoGraphy [50] integrates Concept designers undertake the majority of their work in pre-
iterative design processes into landscape rendering, offering users production stage, with the workflow consisting of the following two
control and flexibility to better align with their unique workflows. phases [1, 41, 64, 73]:
Keyframer [103] uses a natural language interface to make motion
design intuitive and accessible, fostering a feedback loop that al- (1) Early ideation (or blue sky) phase:
lows animators to explore and refine ideas with creative autonomy. This phase focuses on brainstorming and exploring initial
In addition to these works, researchers have developed GenAI sys- ideas. Designers research the topic, perform visual searches,
tems for fashion [53], UX and industrial design [106], and 3D scene brainstorm ideas, and create preliminary sketches to propose
design [79]. These works enhance design workflows by leveraging creative options for feedback from art directors or clients. If
GenAI to reduce repetitive tasks, providing intuitive user interfaces they are not satisfied with the results, designers iterate the
that foster system understanding and enabling precise control to process until the direction of the concept is approved.
refine design outputs. (2) Final concept phase: Once initial concepts are approved,
 Research beyond the design field also offers valuable insights for designers refine the sketches into detailed and polished de-
developing human-centered AI systems. In medicine, NaviPath [51] signs. They enhance chosen concepts with depth, texture,
uses AI models to simplify the navigation of high-resolution tu- and fine details to align with the project’s vision. Approved
mor images, aligning with pathologists’ workflows by enabling final designs serve as comprehensive guides for the produc-
smooth transitions between low to high magnifications. It allows tion teams, which are realized through 3D modeling or set

---

AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers CHI ’25, April 26–May 01, 2025, Yokohama, Japan

Figure 2: The figure showcases designs from concept to final product, including four well-known projects: (a) a scene from Star
Wars, (b) characters from DC Comics (Harley Quinn, the Joker, and the Penguin), (c) a prop from Mad Max: Fury Road, and (d) a
creature from Genshin Impact. This demonstrates the critical role of concept designers in shaping the creative vision from the
earliest production stages to the final product

 construction. The designer may provide ongoing support to 4 FORMATIVE STUDY
 ensure consistency throughout production [88]. We conducted a formative study to gain deeper insights into current
 concept designers’ workflows and the challenges they face using
 traditional and AI-based ideation tools.

 This work focuses on the early ideation phase, establishing the
project’s creative vision and shaping its direction, style, and coher- 4.1 Participants
ence [3, 73, 102]. This stage demands intensive creativity and is
 We recruited 22 professional environment concept designers (15
often seen as the most exciting part of the workflow [41, 84].
 males, 7 females; ages 23 to 45) across three studies. Each partici-
 In the early ideation phase, concept designers receive a design
 pant was assigned a unique ID. Participants were recruited through
specification briefing from the art director or client, which includes
 personal referrals and directly contacting studios by email to re-
a project description, keyframe scene details, and a set of relevant
 quest collaboration. Detailed participant information, including
references [102]. Designers analyze the brief to identify its core
 their participation in each study, is provided in Table 1. We will
elements and potential design directions (Figure 3-a), then begin
 highlight the relevant details of the participants in each study.
the ideation cycle. The cycle starts with research, where designers
 In the formative study, we worked with 12 environment concept
study the subject, gather information, explore visuals, and collect
 designers (P1-P12) from various industries, including Animation
image references to develop a comprehensive understanding (Fig-
 (P1, P4, P6, P8-P9), Game (P5, P10-P11), Art Outsourcing (P3, P12),
ure 3-b) [41]. This step ensures that future designs are coherent,
 and Freelancing (P2), with 3 to 15 years of experience (mean = 7.7,
such as maintaining historical accuracy, aligning with the period’s
 SD = 4.6). Participation in the study was voluntary, and uncompen-
style, or achieving mechanical and structural feasibility. With suffi-
 sated.
cient references and information, designers move to brainstorming,
where they list design elements and create rough sketches with
multiple variations (Figure 3-c) [58]. Research and brainstorming
often intertwine as designers refine ideas while gathering refer- 4.2 Study Procedure
ences or seeking new material when generating fresh concepts. Each participant took part in a 1-2 hour interview covering three
This iterative process helps designers gradually develop and refine main topics: 1) Their typical design workflow, 2) Past design projects,
their designs. After several ideation cycles, designers complete a and 3) Current AI tool usage. We asked participants to prepare three
small set of ideas they find most suitable (typically one to five), specific projects: their most recent project, a typical project, and the
polishing the sketches and organizing the corresponding references most challenging project in their work experience. For each project,
into cohesive design ideas (Figure 3-d). These finalized ideas are we explored the design task, the procedures they followed, and
then presented to the art directors or clients for feedback [102]. their overall approach. This included discussing the use of design
Designers may repeat multiple ideation cycles until the art direc- tools, methods for research and brainstorming, reference materials
tors or clients are satisfied with the direction of the concept. Once collected for various design elements, presentation of sketches to
approved, the process transitions to the final concept phase (Figure directors or clients, and the challenges encountered throughout the
3-e). process.

---

CHI ’25, April 26–May 01, 2025, Yokohama, Japan Wang Lu Ponsa Chen Chen

Figure 3: A typical workflow for an environment concept designer begins with receiving the design specification from the art
director or client. The designer then (a) determines a potential design direction and enters the iterative ideation cycle, which
includes (b) researching based on the task, and (c) brainstorming innovative ideas. Once some suitable design ideas are formed,
(d) both sketches and references are presented to art directors or clients for feedback. Upon approval, (e) they refine the sketch
into a polished, detailed design, which is then shared with other teams, such as the CG team.

 ID Years of Experience Industry Formative Summative Field Study
 1 3 Animation, Films, TV shows ✓ ✓ ✓
 2 4 Freelancing ✓ ✓
 3 7 Art Outsourcing ✓ ✓ ✓
 4 3 Animation, Films, TV shows ✓ ✓
 5 3 Game ✓ ✓ ✓
 6 5 Animation, Films, TV shows ✓ ✓
 7 3 Game ✓
 8 8 Animation, Films, TV shows ✓
 9 12 Animation, Films, TV shows ✓
 10 15 Game ✓
 11 13 Game ✓
 12 14 Art Outsourcing ✓
 13 5 Art Outsourcing ✓ ✓
 14 8 Game ✓
 15 12 Game ✓
 16 3 Animation, Films, TV shows ✓ ✓
 17 2 Animation, Films, TV shows ✓ ✓
 18 2 Animation, Films, TV shows ✓ ✓
 19 1 Animation, Films, TV shows ✓
 20 1 Animation, Films, TV shows ✓
 21 5 Freelancing ✓
 22 11 Game ✓ ✓
 Table 1: Demographic Details of Participants

---

AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers CHI ’25, April 26–May 01, 2025, Yokohama, Japan

4.3 Findings often limit their access to diverse references, restricting creative
To analyze the data, we organized and summarized the transcribed ideas and exploration. For example, “I was asked to design an Aztec
interview recordings, and one of the authors, with prior experience village with three variations, but the architectural references I found
as a professional concept designer, developed a coding framework on Pinterest all looked quite similar. With a tight schedule, the final
to identify key themes for thematic analysis. Two art directors re- designs I proposed ended up being somewhat alike” (P9).
viewed the coding framework from an animation studio and an Designers spend significant effort in creating design variations,
art-outsourcing studio, each managing 15 and 40 concept design- especially for complex design specifications. “A recent project in-
ers, respectively. Thematic analysis was discussed collaboratively volved designing a Chinese Steampunk world with realistic and plau-
among a team of three people to ensure consensus and validity. sible designs. With no existing references, I spent an entire day just
This process revealed patterns in concept designers’ research and sketching one building” (P12). Generating innovative designs or inte-
brainstorming workflows, the purposes of the references they gath- grating unique elements into a cohesive vision is another common
ered, and the challenges they faced with traditional and AI design challenge. “I often spend a great deal of time contemplating what
tools. elements to add to enhance the richness of the scene” (P5). Also, they
 often have to try multiple combinations of design elements from ref-
4.3.1 Challenges during researching. Our participants employed erences to create a suitable outcome. As one participant explained,
a variety of tools during their research. They used search engines “I often fill an entire A3 canvas with sketches to explore various possi-
like Google2 to gather information and chatbots like ChatGPT3 ble design combinations” (P2). Furthermore, within the same project,
to explore topics in depth. For initial visual exploration and ref- designers are usually tasked with creating multiple scenes within
erence gathering, they relied on online platforms such as Pinter- a shared setting, such as “creating various architectures and their
est4 , portfolio websites like Artstation5 , and image databases like interiors within the same game environment”(P3).
Shutterstock6 . Most participants mentioned that this process is
straightforward when the briefing is clear, and the themes are fa- 4.3.3 Problems with current AI design tools. To address these chal-
miliar, like “cyberpunk streets” (P1) or “Japanese shrines” (P3). How- lenges in traditional workflows, many studios and designers have
ever, when specifications were vague, or the topic was less com- started integrating GenAI into their processes [10, 62, 90, 110]. In
mon—a frequent challenge in environment concept design—they our study, all participants had experience using AI design tools,
reported greater difficulty in finding relevant information and ref- with 9 of them already integrating these tools into their workflow.
erences. These observations align with findings from previous lit- The AI tools used included Midjourney7 , Stable Diffusion8 , DALL-
erature [41, 64, 102, 107]. E9 , and more advanced systems like Comfy UI [26]. However, we
 This challenge usually arises from two main issues. First, de- found no consistent usage patterns. 6 participants (P1, P3-P4, P8,
signers often struggle to find search queries and references that P11-12) primarily used these tools for image generation, formulat-
align with their design intentions. “The client asked me to design ing prompts based on concrete ideas and modifying them if the
an internet world for a celebrity, showcasing her popularity. I spent results did not align with their vision. Only 3 participants (P5, P9,
half a day trying keywords like ‘digital world,’ ‘internet world,’ and P10) used the tools for ideation, providing simple inputs to explore
‘matrix world’ on Pinterest, but found nothing suitable” (P1). “Often, topics. We identified several reasons why current AI design tools
I remember having seen a similar reference before, but now I don’t are not yet effective ideation tools for concept designers.
know how to find it” (P2). Second, traditional search tools often Most AI design tools, like Stable Diffusion and Midjourney, rely
fail to provide sufficient references for unique design topics. One on text-based prompts that often require complex inputs, such as
participant noted, “I was asked to design a Grand Mayan market and multiple keywords or lengthy descriptions [71]. This contrasts with
a Mayan ballcourt, 80% based on history. I couldn’t find any relevant designers’ typical workflow, which starts with simple keyword
design work, and the references on Pinterest were fragmented and searches on platforms like Pinterest and progresses to image-based
lacked useful information” (P4). Another added, “We frequently get exploration. “As a concept designer, I don’t want to spend time crafting
tasks that require blending different styles and themes, but it’s hard precise prompts” (P2). Additionally, crafting a suitable prompt often
to find similar concept art online” (P3). requires a clear idea in advance, making it difficult to use during
 the initial ideation. “We usually use this tool to generate images only
4.3.2 Challenges during brainstorming. Concept designers often when we already have a clear idea in mind” (P3). Many participants
need to create 3–5 design variations per environment, a task that noted they struggled to create prompts that generated the desired
becomes challenging for uncommon designs [64]. Most participants outcomes. “I tried modifying the prompt in MidJourney several times,
noted they typically have only “half ” (P6) to “one” (P12) day for but I still couldn’t get what I wanted” (P6). Furthermore, most image-
idea exploration, leaving little time for deeper creative develop- generation AI tools struggle to produce diverse results from similar
ment. “I need to reserve the entire afternoon for sketching, leaving input, limiting their usefulness for breadth idea exploration. “I have
only the morning for research and exploring different possibilities” to re-craft the prompt to get something noticeably different” (P9). “I
(P4). Designers rely on visual exploration for inspiration, but time feel like everything the AI generates looks pretty much the same every
constraints and the challenges outlined in the previous section time, similar compositions, styles, and often stereotypical elements”
2 Google, www.google.com (P1).
3 ChatGPT, https://chatgpt.com/
4 Pinterest, www.pinterest.com 7 MidJourney, https://www.midjourney.com/
5 Artstation, https://www.artstation.com/ 8 StableDiffusion, https://stablediffusionweb.com/
6 Shutterstock, https://www.shutterstock.com/ 9 Dall-E, https://openai.com/index/dall-e-3/

---

CHI ’25, April 26–May 01, 2025, Yokohama, Japan Wang Lu Ponsa Chen Chen

 Concept designers require grounded and accurate information to 4.4 Design Goals
support their designs. However, AI hallucinations pose a significant Based on our findings, we proposed three design goals to better
barrier, discouraging designers from adopting AI tools. “I usually support concept designers during the ideation stage:
avoid using AI-generated images as reference pictures because relying
 • DG1: Breadth exploration: To help designers efficiently
on incorrect content could lead to even worse outcomes” (P6). Addi-
 explore a wide range of ideas and gain a comprehensive
tionally, AI design tools often do not provide enough information
 understanding of the design topic, the system should sup-
in the generated outputs. A common issue is the lack of detail, par-
 port the brainstorming of various ideas using input methods
ticularly in the structure of objects, making it difficult for designers
 that align with their workflow. This could include allowing
to identify visual elements for further reference. As one participant
 users to input natural language instructions, such as task
noted, “The content generated by AI is usually only useful to me
 specifications, or directly upload relevant references.
as a mood reference because the details are often a complete mess”
(P3). Although some tools offer detailed prompts based on simple • DG2: Depth exploration: The system should offer detailed
inputs, they can be challenging to interpret, such as “AI-generated information and references to help designers refine and ex-
images often include some interesting elements, but I don’t know what pand their design solutions while deepening their under-
they are. As a result, I can’t incorporate them into my design” (P1). standing of both the generated ideas and the design task.
Moreover, the generated images often do not align accurately with Moreover, the provided information should align with the
the prompts, “AI-generated images often include additional elements designers’ usual reference-gathering practices.
that are not specified in the prompt” (P10). • DG3: Flexible iterative exploration: The system should
 The iterative process is key to achieving a great design for con- allow users to refine design ideas while maintaining control
cept designers [41]. However, AI design tools often lack the control easily. It should support the efficient exploration of variations
and flexibility needed to refine output after generation. As one on the same theme to ensure consistency and creative flow.
participant noted, “I only wanted to change the style of one build- Designers should be able to narrow or expand the design
ing, but the entire image ended up changing” (P12). Another shared, space as needed, enhancing the creative process.
“The generated results often make me question how my changes to
the prompt are actually affecting the outcome” (P3). Moreover, the 5 SYSTEM & IMPLEMENTATION
lack of detailed information accompanying AI-generated images We propose AIdeation, a system that integrates multiple generative
hinders further ideation, “The AI-generated images contain many models to enhance concept designers’ early ideation phase. Un-
visual elements, but without information about them, I don’t know like existing tools, AIdeation combines the strengths of traditional
how to modify or adjust them” (P5). and AI-driven approaches, streamlining the process by unifying
 These factors combined make current AI image-generation tools research, brainstorming, and design idea refinement into a cohesive,
difficult to use for visual idea exploration and challenging to inte- iterative workflow.
grate into a concept designer’s workflow.
 5.1 System Components
4.3.4 Type of references collected for environment concept design. AIdeation’s key design aligns closely with the system’s design goals:
Environment concept designers gather diverse reference sets tai- Breadth exploration through brainstorming, Depth exploration via
lored to specific tasks, each serving different purposes. Designers Research, and Flexible iterative exploration through Refining De-
also have unique ways of sourcing and organizing references. To sign Ideas. To illustrate how AIdeation supports the early ideation
understand these patterns, we analyzed reference frequency and phase for concept designers, we present a real-world design task
collaborated with designers, identifying the following categories: from one of our users, who was tasked with creating game environ-
 ments for a horror game set in traditional Taiwanese apartments.
 • Hero (or Main) Reference: These references closely reflect 5.1.1 Brainstorming: Supporting breadth exploration. After receiv-
 the designer’s creative intent, aligning with the design theme ing the design specification, the designer inputs the instruction
 and serving as a guide for establishing the overall mood, into AIdeation: "Design a living room scene for a horror game
 shapes, and composition of the design (Figure 4-a). set in an old Taiwanese apartment." AIdeation generates 8 distinct
 • Detailed Supporting Reference: These references pro- design ideas, each featuring various elements accurately aligned
 vide specific detailed contents that support the design of the with the specification. In our design, the ideas are described across
 project. Typically, photographs provide specific details, such six key design elements: Theme, Contents, Art Style, Lighting and
 as mechanical structures or architectural features, offering Atmosphere, Color Palette, and Shot Angle. These categories are
 accuracy and reliability for refining intricate design aspects derived from observations in our formative study. We use "Theme"
 (Figure 4-b). to represent the main reference, as designers normally base their
 • Miscellaneous Reference: Designers often collect refer- primary searches on the central theme of the design task. "Content"
 ences like lighting, atmosphere, art style, color palette, com- covers detailed references for objects and elements within the scene.
 position, and shot angle to enhance their designs based on The other categories were selected based on the references most
 project needs. These references, guided by the project’s goals frequently used by concept designers. Composition was excluded
 or the designer’s vision, are not always essential and are cat- due to current AI limitations. These categories were later reviewed
 egorized as Miscellaneous References. (Figure 4-c). by the same art directors mentioned in Section 4.

---

AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers CHI ’25, April 26–May 01, 2025, Yokohama, Japan

Figure 4: Based on our formative study, concept designers categorize references into three types: (a) Hero (or Main) References:
These align closely with the designer’s creative vision, conveying the overall story, mood, or design, and are crucial for guiding
the project. (b) Detailed Supporting References: These provide specific details, like structure or texture, helping designers
accurately implement finer aspects of the design. (c) Miscellaneous References: These cover a range of purposes, including
lighting, atmosphere, and color palette, supporting various design elements.

 The ideas are presented as generated images in an ideas overview idea using the detailed information provided through a flexible iter-
panel (Figure 5-a), offering a clear visual summary of each design ative approach—either by combining it with additional references
and its key components, which can serve as potential hero refer- or refining it through specific instructions (Figure 5-b3). These op-
ences. This approach directly addresses challenges identified in the tions enable users to either expand their exploration or narrow and
formative study, enabling designers to efficiently grasp the design focus their design scope, depending on their creative needs.
topic while exploring a diverse range of visuals that align with the After identifying a reference of interest based on the selected
design specification and can be incorporated into their creative keyword (Figure 5-b2), the designer can combine it with the current
process. idea to generate 5 new design variations. Figure 5-b illustrates
 the result of combining a previous design idea with a selected
5.1.2 Research: Supporting depth exploration. After selecting a de- reference (Figure 5-b4). AIdeation adjusts the original design, such
sign idea of interest (Figure 5-a1), the designer is directed to the as transforming the style of the sofa to match the selected reference,
idea detail panel (Figure 5-b), which provides in-depth information demonstrating how the design scope can be refined. Conversely, if
about the chosen idea. The left-side information bar displays key the reference is less related to the original elements, the new design
elements of the generated image extracted as keywords (Figure will be more diverse, offering additional creative possibilities.
5-b1), organized into 6 categories corresponding to the design idea For the "refine by instruction" feature, once the designer identi-
description. In the "Content" category, elements are further divided fies specific elements in the current design, they can use natural
into subcategories like "Central Focus" and "Background" due to the language to instruct AIdeation on what to change. These refine-
volume of information. This structure helps the designer clearly un- ments can be based on AIdeation’s provided information or the
derstand the composition of the design and easily identify specific designer’s creative vision. The system then generates 5 new designs
elements in the generated image. that incorporate the user’s instructions, maintaining the essence of
 The idea detail panel also allows users to explore supporting the original idea while introducing diversity.
references by clicking on relevant keywords. When a keyword is se-
lected, corresponding search results are displayed in the same panel
(Figure 5-b2), giving access to additional information and detailed 5.1.4 Next ideation cycle for exploration. AIdeation enables users to
references. Combined with diverse outputs from brainstorming, begin the next brainstorming cycle seamlessly based on the current
these features provide users with a broader array of ideas and infor- design idea (Figure 5-b3, "Explore More"). This feature meets the
mation, facilitating deeper exploration and a more comprehensive need for designers to create related tasks based on an existing
understanding of the design topic and generated concepts. environment, as noted by participants in the formative study. For
 example, the designer could input “design a kitchen based on this”
5.1.3 Refining idea: Supporting flexible iterative exploration. Fol- using the design idea from Figure 5-b, efficiently expanding on the
lowing this, AIdeation allows designers to refine the selected design current concept.

---

CHI ’25, April 26–May 01, 2025, Yokohama, Japan Wang Lu Ponsa Chen Chen

Figure 5: The main interface of AIdeation includes (a) the Ideas Overview Panel, displaying all brainstormed design ideas as
images with titles based on user input. Users can select an idea to view in (b) the Idea Detail Panel, which provides detailed
information on the selected idea. (b1) The left sidebar lists key elements extracted from the idea, categorized into six groups as
keywords. Users can select a keyword to view related search results in (b2). (b3) The right panel allows users to refine the idea
by combining it with references or by instruction. (b4) Below the current idea, its origin is shown; in this case, the idea was
generated by combining "Idea 4" and a colorful sofa.

---

AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers CHI ’25, April 26–May 01, 2025, Yokohama, Japan

Figure 6: Technical pipeline of AIdeation: (a) The user’s input image is captioned by a vision model and processed by Idea
Generation GPT, which integrates instructions and creative score to generate design ideas description. This idea is then
converted into keywords, and DALL-E 3 generates an image with the idea description. (b) User-selected keywords initiate a Bing
Image Search, returning a set of relevant images. When the user wants to refine the idea, (c) a selected reference is captioned by
a vision model and processed by Combine Reference GPT, merging it with the original idea to create modified designs based on
the creative score. (d) In contrast, AIdeation also supports refining ideas by instruction. The original idea and user instructions
are processed by Refine by Instruction GPT, along with the creative score, to generate additional refined ideas.

5.2 Technical Implementation ability to interpret natural language prompts, understand complex
5.2.1 Brainstorming and research. AIdeation accepts both textual instructions, and generate corresponding images 10 . The images
instructions and image inputs. As shown in Figure 6-a, when an are produced at a resolution of 1792x1024, suitable for environment
image is provided, it is first processed by the GPT-4o Vision model, concept design. The entire generation process takes approximately
which generates an image caption. Then, we use Idea Generation 30 seconds, or around 40 seconds on average when an image is
GPT—a specially prompted LLM (GPT-4o-2024-05-13 as the base included as input.
model)—designed for generating environment concept design de- In the Idea Detail Panel, when a keyword is selected from the
scriptions (see prompt in Appendix C). The instruction, image cap- left-side information bar, it is sent to the backend, where the Bing
tion (if applicable), and creative score are then passed into the LLM. Image Search API 11 retrieves a batch of 50 images (Figure 6-b).
Based on the user’s input, the model generates multiple design Scrolling to the end of the page triggers an additional batch of
ideas in parallel. Each idea was assigned a creative score, ranging images.
from 0 to 1, to reflect the diversity of the outputs. A higher creative 5.2.2 Refining idea and next ideation cycle for exploration. When a
score prompts Idea Generation GPT to produce more innovative user selects a reference to combine with the current design idea, the
design descriptions. The output format is detailed in Section 5.1.1. reference is processed through the GPT-4o Vision model to generate
 Each generated idea is processed in two ways: 1) important in- image captions (Figure 6-c). The selected keyword, image caption,
formation is extracted as keywords using a prompted Keyword creative score (following the same distribution as brainstorming),
Extraction GPT (see Appendix D) and displayed in the idea detail and the current design description are then input into the Combine
panel, and 2) the idea is input into an image generation model to cre-
ate an image, which is shown in the ideas overview panel. For this 10 Dall-E, https://openai.com/index/dall-e-3/
work, we used DALL-E 3 as the image generation model due to its 11 Bing Image Search API, https://www.microsoft.com/en-us/bing/apis/bing-image-
 search-api

---

CHI ’25, April 26–May 01, 2025, Yokohama, Japan Wang Lu Ponsa Chen Chen

Reference GPT (see Appendix E). This GPT modifies the design more limited styling options. After each task, participants took a 10-
description by incorporating details from the reference image based minute break. Both the conditions and design topics were counter-
on the selected keyword. For example, in Figure 5-b4, the keyword balanced. After both tasks, participants completed a questionnaire
"Weathered Vintage Sofa" updates the corresponding section of the and a 20-30 minute post-study interview. They were compensated
original design idea with the sofa’s style from the reference image. If approximately 34 USD.
the reference is less related to the current design elements, the GPT
 6.1.2 Task overview. Participants completed a design task that repli-
will make broader adjustments, incorporating the reference while
 cated their ideation workflow using both the baseline method and
modifying other parts of the description. The level of modification
 AIdeation. For each condition, participants were assigned an en-
is influenced by the creative score—higher scores result in more
 vironment concept design topic and instructed to gather at least
significant changes and diverse combinations, offering both control
 three sets of references for interior and exterior designs using the
and variety.
 widely used PureRef reference board 12 . The design topics were: 1)
 Figure 6-d illustrates the technical process of the "Refine by
 a Mayan Observatory and Planetarium with an observation hall
Instruction" feature. Like the brainstorming and reference combi-
 featuring a dome, and 2) a Tibetan Meditation Research Center
nation processes, the prompted "Refine by Instruction GPT" (see
 with a main research hall. Both tasks required blending traditional
Appendix F) uses the user’s instruction, creative score, and current
 and contemporary architectural styles, a common challenge in real-
design description as inputs. The GPT adjusts the design based on
 world projects. Participants were asked to follow their ideation
the instruction, with the creative score determining the extent of
 process, including research and brainstorming, ensuring that the
changes and creativity. The modified design descriptions follow the
 selected references would suit future designs and client presenta-
same format, allowing for later keyword extraction and image gen-
 tions, thereby simulating real-world constraints. Each reference set
eration, just like in the brainstorming process. Both Idea Refinement
 is needed to represent a distinct ideation result, including at least
process takes a similar amount of time as Brainstorming.
 one main reference supported by detailed references.
 For the Next Ideation Cycle for Exploration, the process follows
the same structure as the brainstorming phase, with the key differ- 6.1.3 Pilot study and refinements. Initially, we designed a 40-minute
ence being that image captioning is replaced by the current design task, which also included a sketching stage after the research and
idea description. brainstorming stages. We piloted this design with two professional
 concept designers, but neither was able to complete the tasks, re-
6 SUMMATIVE STUDY porting feeling "extremely stressed" as such tasks typically require
 a full day. Additionally, sketching diverted their focus from explor-
Our summative study examines the effectiveness of a creativity
 ing the AIdeation system, despite it being the primary focus of the
support tool in enhancing designers’ early ideation workflows and
 study. Based on these findings, we excluded sketching from the final
fostering their creative processes. Rather than evaluating the quality
 study design. The revised tasks and design topics were reviewed
of final design outputs, the study focuses on how AIdeation sup-
 and validated by three art directors from animation, game, and art
ports the workflow compared to designers’ existing processes. We
 outsourcing studios, who confirmed that using references alone to
conducted a within-subject comparative study with 16 professional
 communicate with clients is a common practice, especially under
environment concept designers, focusing on three key aspects:
 time constraints.
 • A1: Support for the Ideation Process
 6.1.4 Measurements. The questionnaire focused on comparing
 • A2: Quality and Efficiency of Ideation
 the support provided by each condition for the ideation process
 • A3: Workflow Support at Each Stage
 and different workflow stages. Participants rated their preferences
Given the diversity of concept designers’ workflows, we set the across various aspects. For the ideation process, they evaluated
baseline to each participant’s preferred existing workflow. Partici- breadth and depth of exploration support, flexibility in idea explo-
pants were free to use any of their current methods, such as image ration, efficiency in generating diverse ideas, quality of ideas, and
databases, search engines, and AI design tools like Midjourney or creativity enhancement. For example, we asked the participants
DALL-E 3, or a combination of these. For those with no prior ex- about their preferences using questions such as, “Which system
perience using AI design tools, we provided access to ChatGPT-4 allows you to generate a variety of design ideas more efficiently?” For
with DALL-E 3 and a brief tutorial, as AIdeation is also based on workflow support, they compared the systems on information col-
DALL-E 3. Participants could then decide whether to incorporate lection efficiency, reference-gathering efficiency, the usefulness of
this into their process. collected references, and which system better supported the visual
 presentation of ideas. Additionally, participants provided feedback
6.1 Study Design on their overall satisfaction and enjoyment while also comparing
 task difficulty and efficiency between the two conditions. The full
6.1.1 Procedure. The study lasted 2 to 2.5 hours, beginning with a
 questionnaire can be found in Appendix A. All responses were
10-minute briefing. Participants completed a 30-minute design task
 measured using a 7-point Likert scale, where 7 indicated a strong
under each condition, with each task preceded by a 10-minute prac-
 preference for AIdeation, and 1 indicated a preference for their
tice session. They also received a 10-minute tutorial on AIdeation.
 original workflow. For questions related to efficiency, participants
To minimize bias from prior experience, participants were briefed
 were asked to disregard image generation time. This measurement
on key differences between AIdeation and other AI tools, such
as its use of natural language inputs instead of prompts and its 12 Pureref, https://www.pureref.com/

---

AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers CHI ’25, April 26–May 01, 2025, Yokohama, Japan

approach aligns with previous findings on preference elicitation, had also participated in the earlier formative study. Participants had
emphasizing the importance of task sensitivity and granularity in between 1 and 12 years of professional concept design experience
capturing meaningful differences between options [38]. Specifically, (M = 4.6, SD = 3.2).
using comparative questions enhances sensitivity to utility differ-
ences, while choosing a 7-point scale balances granularity and inter- 7 RESULTS & FINDINGS
pretability for moderate differences in preferences. A one-sample
 7.1 A1: Supporting Ideation Process
Wilcoxon signed-rank test was performed to evaluate whether re-
sponses differed significantly from the neutral midpoint (4). This In this section, we first address our key aspects using the infor-
non-parametric test is appropriate for analyzing the ordinal data mation collected from the study. Following that, we will report
collected through the 7-point Likert scale questionnaire, as it does additional notable qualitative findings based on our observations.
not assume a normal distribution and is well-suited for assessing 7.1.1 Breadth, depth, and flexibility of idea exploration . Figure
central tendency differences in ordinal data [25]. By testing whether 7-a shows that participants preferred AIdeation for breadth (Mean
the median response significantly deviates from the neutral point, = 5.19, p = 0.014), depth (Mean = 5.00, p = 0.033), and flexibility
this approach effectively determines whether participants exhib- (Mean = 4.93, p = 0.046) in idea exploration, with 69% expressing
ited a systematic preference for one condition over the other. This a preference for AIdeation in terms of both breadth and depth.
methodology is supported by previous research on the suitability Participants mentioned: “The randomization provided by AIdeation
of nonparametric tests for ordinal data and preference-based mea- offers a lot of possibilities” (P19). and “The additional references,
sures [14, 87, 100] and is consistent with previous studies employing combined with my existing ideas, really expanded my design space”
similar analytical frameworks [18]. (P21). Most participants found AIdeation offered better diversity
 In the in-depth interview, we first explored participants’ atti- than their original tools with the same input (P1, P3, P5, P13, P15-
tudes toward AI-generated images, prior experience with AI design P16, P19, P21-P22). “Compared to MidJourney, AIdeation provided
tools, typical ideation strategies, and how they approached the much more diversity, and I didn’t even need to think of a prompt”
task using AIdeation. We then focused on how their experience (P16). “Each iteration offered significant variation, helping me break
with AIdeation differed from their original workflow, particularly out of my usual direction and explore new ideas” (P4). However, some
in terms of the ideation process and overall workflow. For example, participants noted limitations in atmospheric or stylistic diversity
we asked participants to compare their experiences when searching (P2, P6, P20). “I feel like when I input ’Mayan Architecture,’ the system
for references using two different approaches. Additionally, we re- often gave me stereotypical results” (P2). “I always get a similar style
quested that they explain the reasoning behind their questionnaire from AI images” (P6).
ratings. For instance, they were asked to elaborate on why they Regarding the depth of exploration, five participants noted that
preferred AIdeation for better efficiency. The interview concluded they could efficiently narrow down their design focus with AIdeation
with discussions on their favorite AIdeation features, suggestions (P3, P18, P20-P22). “Compared to the design ideas I find on Artstation
for improvements, and how they might integrate AIdeation into or Pinterest, which cannot be modified, I can use AIdeation to refine
their workflow. The detailed interview questions can be found in the idea” (P21). Three participants also mentioned that AIdeation
Appendix B. The interview data were analyzed similarly to the accurately provided detailed information and references that helped
formative study. Three researchers summarized the transcribed in further design work (P3, P5, P18). “AIdeation offers so much in-
recordings, and a former concept designer on the team identified formation that would normally take a lot of time to gather from
key themes for thematic analysis. The findings were then reviewed different platforms” (P18). However, two participants mentioned
and discussed among the researchers to ensure consensus. that AIdeation lacked image-to-image search functionality, which
6.1.5 Evaluation approach. We adopted a self-report approach, prevented them from obtaining similar images and restricted deeper
aligning with prior research in the HCI and creativity communi- exploration (P1, P6).
ties [69, 80, 89, 96]. Participants provided feedback based on their ex- Finally, 56% of the participants preferred the flexibility of ex-
periences, evaluating AIdeation across key dimensions as a creativ- ploration with AIdeation. Most suggested that AIdeation was easy
ity support tool. For the ideation results, participants self-assessed to use and its functionality helped them access diverse design ele-
which method provided better support for idea quality and effi- ments (P1, P14-P15, P16-P18, P22). However, three users found it
ciency during the tasks. Given the difficulty of directly comparing challenging to achieve their desired results with AIdeation due to
outputs between two conditions (collected references), external the lack of detailed control (P1, P2, P6). “The layout kept changing
expert evaluation was not conducted. Instead, participants were when I combined references or refined by instructions, but I wanted to
asked during interviews to explain their questionnaire ratings in keep that layout” (P2). “I just wanted to adjust the atmosphere of the
detail, providing qualitative insights into their experiences. To com- image, but I couldn’t do that with this system” (P6).
plement this, we later conducted a field study to assess AIdeation’s
 7.1.2 Creativity. Compared to their original workflow, participants
impact on real-world projects, focusing on idea quality, quantity,
 significantly preferred AIdeation to enhance creativity (Figure 7
and creativity.
 -a, Mean = 5.56, p = 0.001), with 81% expressing a preference for it.
6.1.6 Participants. We recruited 16 professional environment con- Many users noted that AIdeation provided unexpected brainstorm-
cept designers from various industries and five studios, including ing results (P1, P13-P18, P21-P22). Several participants appreciated
animation (P1, P4, P6, P16-P20), game (P5, P14-P15, P22), art out- the keywords provided by AIdeation, mentioning that they could
sourcing (P3, P13), and freelancing (P2, P21). 6 participants (P1-P6) simply refer to the detail information bar for inspiration (P1, P4-P5,

---

CHI ’25, April 26–May 01, 2025, Yokohama, Japan Wang Lu Ponsa Chen Chen

Figure 7: The distribution of user preference for baseline vs. AIdeation: (a) Preference rating on a 7-point Likert scale for idea
Exploration; (b) Overall preference for Satisfaction, Enjoyment, Task Difficulty, and Task Efficiency

P13-P14). Furthermore, combining their original design ideas with 7.2 A2: Quality and Efficiency of Ideation
the additional reference introduced different ways of thinking (P1, Figure 8 shows the distribution of the participants’ preferences for
P4, P14, P17, P21-P22). As one participant mentioned, “The system various aspects of the ideation process. The results indicate that the
combined different styles and content in various ways, which gave participants significantly preferred AIdeation to efficiently generate
me a lot of inspiration” (P21). Another added, “Combining diverse or a variety of design ideas (Mean = 5.44, p = 0.003) while maintaining
uncommon elements sparked new ideas” (P1). a quality similar to their original workflow (Mean = 4.31, p = 0.41).
 75% of participants preferred AIdeation for its efficiency in assisting
 with design idea generation.
7.1.3 Overall satisfaction, task efficiency, and difficulty. Figure 7-b Most participants noted that AIdeation quickly offered a wide
shows the distribution of the overall satisfaction, enjoyment, and range of diverse design elements that aligned with the topic (P1,
preferences of participants regarding task difficulty and efficiency. P13-P16, P18, P21- P22). “In my original workflow, I need to first
The participants significantly preferred AIdeation in terms of over- think of keywords to search on Pinterest. Even if I find an interesting
all satisfaction (Mean = 5.19, p = 0.005) and enjoyment (Mean = 5.19, design, it’s hard to extract key information from the image. AIdeation,
p = 0.005), with 75% and 69% expressing a preference, respectively. however, provides plenty of ideas with well-organized information”
“The system is really easy to use, compared with other AI tools I used (P22). “In MidJourney, I have to come up with the idea first, but
before” (P16). “I really enjoy seeing the result of combination, each AIdeation already presents many ideas” (P14).
time I was surprised by unexpected results” (P1). Results also sug- Half of the participants noted that AIdeation significantly re-
gest that participants significantly preferred AIdeation for reducing duced the time needed to combine two design elements (P1, P3-P5,
task difficulty (Mean = 5.19, p = 0.005). Participants explained that P13, P18, P21-P22). “Before, I had to manually combine two design
AIdeation allowed them to work without thinking too much (P3, elements, and if the result wasn’t ideal, the time was wasted. With
P16, P18) and provided well-organized and relevant information AIdeation, I can instantly combine elements with some level of control,
that would normally take more time to gather using their original saving me a lot of time” (P13). Additionally, most users took advan-
workflow (P1, P4-P5, P19), such as “Those keywords truly helped me tage of AIdeation’s "explore more" functionality to quickly generate
quickly find a variety of reference materials” (P4). interior design ideas based on their selected exterior design ideas.
 However, the results for task efficiency were mixed. Despite be- Most suggested that this feature significantly helped them obtain
ing asked to ignore image generation time, some participants who diverse interior results without starting the process from scratch
preferred their baseline workflow noted that waiting for results in (P1, P3, P15-P16, P18, P20, P22). “The ability to generate images in
AIdeation took longer compared to browsing visuals continuously this narrative-driven way is truly a groundbreaking innovation” (P18).
on Pinterest (P1, P17-P19). Additionally, three participants barely “This will be very useful if I need to design multiple rooms within the
completed their tasks because they spent most of their time try- same building” (P13).
ing to achieve an exact match to their idea but were unsuccessful Regarding ideation quality, some participants noted that their
(P2,P6, P18). One participant who preferred the baseline for both original workflow with Pinterest often yielded more diverse and
satisfaction and efficiency mentioned, “I kept modifying the prompt unexpected design elements, leading to fresh ideas. In contrast,
but couldn’t get the result I wanted, which was frustrating” (P6). AIdeation tended to offer more relevant design elements (P2, P6).
 In summary, compared to their original workflow, AIdeation Other participants who preferred the baseline or remained neutral
improved the creativity of participants and provided better support noted that they could achieve similar or better quality using their
for both breadth and depth of exploration with improved flexibility. original workflow (P6, P13, P18, P20). “The AI-generated images are
In general, the participants reported greater satisfaction and enjoy- very different from what I have in mind. If it were a real photo, the
ment with AIdeation and significantly reduced the difficulty of the quality would be better, and the details would be more accurate” (P6).
task.

---

AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers CHI ’25, April 26–May 01, 2025, Yokohama, Japan

Figure 8: The distribution of user preference for baseline vs. AIdeation: Preference rating on a 7-point Likert scale for Quality
and Efficiency of Ideation

 In summary, the participants considered AIdeation to have helped existing concepts (P3, P5, P15). Many suggested using AIdeation’s
them generate more diverse design ideas while maintaining quality output to communicate more effectively with directors or clients,
similar to their original workflow. thereby significantly increasing efficiency (P3-P5, P13, P16-P17,
 P21-P22). Additionally, two users mentioned potential applications
7.3 A3: Workflow Support at Each Stage for photobashing with AIdeation’s outputs (P15, P20).
 In summary, the participants found AIdeation to be more effi-
7.3.1 Support for research, reference gathering and visual presen- cient in collecting relevant information and visually presenting
tation. As shown in Figure 9, participants significantly preferred the ideation results. While some preferred traditional methods for
AIdeation for efficiently gathering information for the design task sourcing references, most considered AIdeation’s suggestions valu-
(Mean = 5.25, p = 0.009), with 81% expressing a preference. Many able for ideation. Additionally, it showed the potential to streamline
found that AIdeation helped them quickly understand the design workflows and enhance client communication.
topic (P1-P3, P15-P17, P19, P21-P22). One participant noted, “Nor-
mally, we spend hours researching complex topics without existing
references, but AIdeation provided a whole package of concepts and in- 7.4 Qualitative Findings on AIdeation Usage
formation instantly, saving a lot of time” (P3). Participants mentioned 7.4.1 Impact of intuitive vs. Analytical usage on AIdeation. Partici-
that the keywords and detailed supporting references provided by pants who intuitively engaged in AIdeation and freely experimented
AIdeation for each design idea helped them quickly obtain the in- achieved better results than those who overanalyzed the process.
formation needed to develop their designs. “Even if the AI-generated Those who quickly iterated without perfecting the prompts gen-
image didn’t fit my needs, I could use the keywords provided by the erated more diverse and creative outputs, while participants who
system to find a lot of useful information” (P5). “I don’t need to come spent excessive time refining the inputs produced fewer results and
up with keywords or read through a lot of text when using AIdeation” found the tool less efficient. For example, P5 embraced a simple
(P13). and iterative approach, generating 16 hero references in 4 ideation
 The participants also significantly preferred AIdeation to bet- cycles with 10 refinements, aligning well with her creative vision. In
ter visually present the design idea (Figure 9, Mean = 5.31, p = contrast, P2 spent considerable time crafting inputs and struggled
0.004), with 69% expressing preference. “Usually, I have to sketch with unsatisfactory outputs, completing 8 cycles with 4 refinements
multiple design versions because no reference fits my needs. But with but only 6 hero references, ultimately perceiving the tool as less
AIdeation, I can select elements from several generated images and effective.
directly present my idea to the client” (P3). However, there was no
significant preference regarding the efficiency of gathering refer- 7.4.2 Controllability of AIdeation. AIdeation received polarized
ences or the usefulness of references with AIdeation. Participants opinions regarding its controllability. On the positive side, many
who preferred the baseline stated that “Even though AIdeation pro- participants were impressed with the degree to which the tool
vides accurate references, the overall quantity is much less compared understood their intentions, especially when combining references
to my original workflow (Pinterest)” (P1). and refining with instruction. (P3-P5, P13, P15, P20) “For me, ease of
 use is the most important factor for an AI tool. AIdeation met that goal
7.3.2 Integrating AIdeation into workflow. At the end of the study, and was able to capture the key points I wanted” (P15). “Combining
we asked the participants if and how they would use AIdeation in references allows me to control specific parts and choose what to merge,
their real-world projects. Most of the participants indicated that which is extremely helpful” (P19). However, some participants had
they would use AIdeation immediately after receiving design spec- contrasting experiences. “I wanted to keep the material but change
ifications to explore different concepts (P1-P6, P13-P16, P18-P22). the layout from square to round, and after trying several times, it still
Several noted that AIdeation is more efficient and user-friendly didn’t work” (P18). Interestingly, some participants appreciated the
then other AI tools (P1, P13-P14, P18, P21-P22). Three participants lower level of controllability. "Each generated idea had significant
found it particularly useful for initiating new designs based on variation, and I could extract different elements from them" (P16).

---

CHI ’25, April 26–May 01, 2025, Yokohama, Japan Wang Lu Ponsa Chen Chen

Figure 9: The distribution of user preference for baseline vs. AIdeation: Preference rating on a 7-point Likert scale for Workflow
Support

7.4.3 Expectations toward AIdeation and their effect. Users’ ex- and platformer games that are known for their non-linear explo-
pectations toward AIdeation strongly influenced their experience. ration and progression. The professional concept design experience
When seen mainly as an image generation tool—a common per- of the participants ranged from 2 to 11 years (mean = 4.5, SD = 2.9),
ception in our study—users often produced less diverse results, similar to that experienced with an average of 4.6 years from the
focusing on precise prompts and modifications (see Section 7.4.1). summative study.
This mindset, common among users familiar with other AI design
tools, emphasizes control and exact results. As one participant
noted, “With AI, I expect a complete design. Unlike Pinterest, where I 8.2 Study Procedure and Evaluation
look for elements, AI images seem finished, so I feel the need to tweak We deployed the same AIdeation system from the summative study
them for clients” (P18). This approach can limit opportunities, as on AWS (Amazon Web Services) EC2, assigning each studio its own
users may overlook valuable design elements. In contrast, treating EC2 instance. We asked designers to incorporate AIdeation into
AIdeation like browsing Pinterest encourages the discovery and their current projects, emphasizing its use during early ideation
integration of new ideas, enriching the creative process. alongside other design tools. We used a combination of diary studies
 and interviews to explore participants’ experiences with AIdeation.
8 FIELD STUDY Participants documented their workflows, including how they used
 the tool, the ideas they selected, their iteration processes, and the
After the summative study, we conducted a week-long field study
 progression from initial input to final results.
across four studios to evaluate how AIdeation supported production
 We then conducted 30-minute online interviews in which partic-
projects in terms of quality, creativity, and efficiency, particularly
 ipants assessed how AIdeation impacted their design outcomes and
with external assessment and validation by directors and clients.
 efficiency. The participants estimated the time typically required
We also examined how AIdeation integrated into the design pro-
 for the project based on previous experience and compared it with
cess, influenced the creative workflow, and addressed challenges or
 the actual time spent using AIdeation. Participants also reported
limitations encountered in real-world project settings.
 on directors’ and clients’ feedback on the results. Additionally, they
 shared how AIdeation supported their projects, highlighted new
8.1 Participants: Studios and Designers insights gained during its use in real-world projects, and identi-
We recruited 8 participants across 4 studios (S1-S4) from the summa- fied areas for improvement. Although the studios shared the final
tive study, as their familiarity with AIdeation made them well-suited production results with the authors as part of the field study, they
to integrate AIdeation into their commercial projects. To control withheld permission for us to publish them due to NDAs and unre-
for selection bias, these participants had an average satisfaction leased games.
score of 5.25, closely aligned with the overall mean score of 5.19
from the summative study.
 S1 (P1, P16-P18) is a visual effects (VFX) studio focusing on 8.3 Results and Findings
designing environments for animation, films, TV shows, and adver- Table 2 presents background information on the project each studio
tisements; S2 (P3, P13) is an art outsourcing studio; S3 (P22) is an was working on and how they utilized AIdeation in their current
AAA game studio; and S4 (P5) is a game studio known for creating project (where cycles are defined as starting a new input or using
side-scrolling Metroidvania games, a subgenre of action-adventure the "explore more" feature). The four studios collectively generated

---

AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers CHI ’25, April 26–May 01, 2025, Yokohama, Japan

 Studio ID Field Task Type AIdeation Usage % Other Tools Used Env. Ideas Gen. Cycles Ideas Used
 1 Animation, Films, TV shows Environment Design 40% Pinterest, Midjourney 3 93 14 14
 2 Art Outsourcing Matte Painting 100% None 1 105 10 5
 3 Game Visual Development 80% Pinterest 3 652 45 28
 4 Game Environment Design 90% Pinterest 5 242 29 23
Table 2: Summary of the 4 studios’ usage of AIdeation: studio’s field, project tasks, usage of AIdeation among all tools used,
number of environment design tasks, total ideas generated, total ideation cycles, and the number of ideas generated by AIdeation
that were used in the final output of the designers.

 Studio ID Actual Time (AIdeation) Estimated Time (Original) Time Difference Time Difference (%)
 1 1.5 Working Days 2 Working Days -0.5 Working Days -25%
 2 5 Hours 4 Hours +1 Hour +25%
 3 2 Working Days 5 Working Days -3 Working Days -60%
 4 6 Working Days 14 Working Days -8 Working Days -57%
Table 3: Comparison of concept design time using AIdeation (actual) vs. the same designs using existing workflow (estimated).

1,092 ideas across 98 cycles, ultimately selecting 60 ideas, which generated scenes were consistently symmetrical. This limited their
contributed to the design of 12 environments in total. ability to present the outputs effectively to clients, as the composition
 and layout lacked variation” (S1).
8.3.1 Design efficiency, quality, and creativity. Table 3 compares Participants desired greater controllability, noting that AIdeation
the estimated time for their original workflows with the actual lacked a gradual generation feature. “Sometimes I just wanted to
time spent using AIdeation. Both S3 and S4 reported significant remove one element from the idea or adjust the composition, but the
efficiency improvements, with time spent reduced from 5 days whole image changed” (S4). “AIdeation tended to generate overly
to 2 days and 14 days to 6 days, respectively. Both participants complex designs in the initial cycle, I needed to include instructions
emphasized that AIdeation helped them identify a design direction, to simplify the designs” (S3). A user from S1 suggested adding the
particularly when they were unsure how to begin working from Inpainting functionality for more detailed control.
the provided design specifications. “(AIdeation) Can quickly provide
multiple directions for our team to explore and develop”(S4). However,
S2 experienced a slight decrease in efficiency, they stated that “The 8.4 Case Studies
client didn’t seem to favor the artistic style generated by AIdeation, We selected two cases to discuss both negative and positive feedback
and the image generation process was somewhat time-consuming.” in depth: S2 showed limitations of AIdeation and opporunities for
 S1, S3, and S4 reported that AIdeation significantly enhanced improvement, while S4 demonstrated significant improvements in
the quality of their final designs. All three noted that AIdeation en- quality, efficiency, and creativity.
riched their designs with a variety of elements. Figure 10 presents a
comparison between the results generated by AIdeation and DALL- 8.4.1 Case study #1 - Large mountainous environment scenes (S2).
E 3 in ChatGPT, using the same input provided by a participant in Two environment concept designers were tasked with creating a
the field study (S3). According to the participant, AIdeation results mountain scene featuring a narrow path winding upward to a mas-
demonstrated significantly greater diversity and richness in design. sive rocky summit. The final design would be used as a poster and
The S1 project leader stated: “The generated images might not always web page background. For this project, the designers had previously
have the exact level of detail I needed, but I was able to extract many used MidJourney’s output to communicate with their clients and
useful design elements.” The participant from S4 shared that when switched to using AIdeation exclusively for the field study. Start-
directors saw the scenes she created using AIdeation, they were ing with the client’s specifications and styling keywords, they first
“strikingly impressed.” picked 25 ideas from 10 cycles and ultimately selected 5 images
 All the studios agreed that AIdeation boosted the creativity of for the client to confirm the design direction. The client chose 2
their final design. “I couldn’t stop exploring new concepts. Every images as the main reference points, which the designers then used
iteration sparked an eagerness to try something I hadn’t thought of to draft the final result. Figure 11-a shows examples of generated
before” (S3). “There were often some great unexpected outcomes that images and selected ones.
we ended up incorporating into our designs” (S2). While the designers reported that AIdeation improved the ideation
 Some participants also discovered uses beyond our expecta- process for them, their client strongly preferred the aesthetic qual-
tions. For instance, participants from S1 used AIdeation to gen- ities and depth rendering of MidJourney over Dall-E, which was
erate unique patterns, which they found difficult to source online, used by AIdeation. In terms of working time, the designers exceeded
and incorporated them into their designs. The participant from their initial 4-hour estimate by one hour, unlike other projects that
S4 suggested that sometimes, simply uploading an image without reported significant time savings. A key factor was that this project
providing any prompts could still generate quite good ideas. had clear and detailed design specifications from the client, mak-
 ing ideation a smaller part of the task. Most of the time was spent
8.3.2 Challenges. Participants also reported some issues. Users generating images that accurately aligned with the client’s design
from S1 and S2 mentioned the styling and aesthetics problems. “The requirements and aesthetic preferences.

---

CHI ’25, April 26–May 01, 2025, Yokohama, Japan Wang Lu Ponsa Chen Chen

Figure 10: A comparison between the initial outputs from (a) AIdeation and (b) DALL-E 3 on ChatGPT, using the same input
provided by Field Study Participant S3, revealed notable differences. The participant observed that AIdeation produced designs
with significantly greater diversity and richness compared to those generated by DALL-E 3 on ChatGPT.

8.4.2 Case study #2 - Metroidvania game environment design (S4). of their outputs greatly exceeded previous work, “The team leader
The designer used AIdeation to create three key game scenes and was amazed by the quality of my work over the past 1.5 months.”
the backgrounds for two secondary scenes, which will be directly remarked by the participant from S4.
incorporated into the final game. We selected the most interesting
case from the key scenes: a steel bridge scene. The designer started
with a rough concept from another game scene and was tasked with 9 DISCUSSION, LIMITATIONS, AND FUTURE
designing a steel bridge in the same style. The bridge’s structure WORK
needed to be both complex and coherent. Before using AIdeation, 9.1 Addressing Barriers to Adoption:
she had spent two days experimenting with various approaches
but could not create a satisfactory design.
 Transparency, Accuracy, and User
 With AIdeation, she input the reference concept design with Perceptions in AI Design Tools
brief instructions. After the initial generation and only two itera- A significant proportion of designers and artists exhibit resistance
tions of "refining by instruction", she obtained the design elements to the adoption of GenAI tools [54, 57]. Although concerns such
she needed to realize her creative vision (Figure 11-b). For other as copyright and other factors discussed previously play a role, an-
tasks, she followed the same process, completing her designs and other critical reason for this reluctance is the lack of transparency
the art director was “strikingly impressed.” The designer reported: in these systems [93, 123]. Without a clear understanding of the
“With a tight deadline for an upcoming game update and complex underlying actions of the system, users struggle to control and com-
design tasks, I was prepared to work overtime for two weeks. Thanks municate with it effectively, ultimately reducing acceptance and
to AIdeation providing multiple design solutions and many design adoption [8, 105]. To address this, prior work has explored enhanc-
elements, I managed to work overtime for just one week” (S4). ing interpretability and user control through multi-modal feedback
 In this case, the designer was tasked with creating complex and visualization. XCreation [119] integrates an entity-relation
scenes featuring intricate structures while adhering to a specific graph to visually map picture elements and their relationships,
style, a process that typically demands extensive research, brain- making generative structures more transparent. In product design,
storming, and finding suitable references. PhotoDreamer [121] allows designers to prototype with physical
 materials while AI interprets their inputs, providing clear feedback
 on how designs evolve. And AutoSpark [17] enables fine-grained
8.5 Continued Usage in Production beyond the comparisons to improve text-image relevance.
 Field Study On the other hand, AIdeation is specifically designed to meet the
We are excited to share that after the end of the field study, Studios needs of concept designers by breaking down brainstorming results
1 and 4 have continued to use AIdeation in production to date. For into visuals and categorized keywords, helping designers quickly
example, in one of Studio 1’s projects, it iterated 35 cycles and 221 grasp key attributes. Building on this understanding, AIdeation
ideas to create 6 scenes in 2 weeks, saving approximately 40% of the enables designers to fine-tune elements precisely. At each step, it
time while significantly enhancing quality, especially with intricate eliminates the traditional need for designers to spend excessive
patterns and textures. In one of Studio 4’s projects, it iterated 69 time interpreting generated images or manually crafting and mod-
cycles and 590 ideas to create 22 scenes in 6 weeks. While time ifying complex prompts, while still preserving high-level control
savings couldn’t be measured due to a fixed deadline, the quality over design directions. As one participant noted: “Compared to other

---

AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers CHI ’25, April 26–May 01, 2025, Yokohama, Japan

Figure 11: The workflow and results of using AIdeation on real-world projects from two designers in two studios (S4 and S2)
are as follows: (a) The designer (S4) was tasked with creating a functional steel bridge based on an existing concept design.
After just two idea refinements, the designer achieved the desired result, supporting the detailed structure design that she
had already spent two days conceptualizing; (b) The designer was tasked with creating a mountain scene matte painting for a
webpage background. After 10 cycles of ideation, they selected five results to present to the client. However, the entire process
took an hour longer than their original workflow estimate.

image-generation tools I’ve used before, I can clearly see what to do (P15) noted, “Although I still don’t like AI-generated images, the
next, making it much more efficient to achieve the desired outcome” keywords and references are very useful.” These findings, coupled
(P14). By enhancing AI transparency and control of creative direc- with our observations in Section 7.4.3, highlight the substantial
tions, AI design tools would improve engagement, foster human-AI impact of user attitudes and expectations on their experience with
collaboration, and improve user satisfaction, as proposed by human- AI systems, a conclusion supported by recent research [56].
centered AI design principles [94]. These issues also extend to other domains. While GenAI is pow-
 Hallucination is another critical concern in GenAI, Hegazy et erful, designers need to identify and address the root causes of
al.[44] identified potential issues with using GenAI in architectural possible negative attitudes toward it. A user-centered approach is
design, such as a lack of consideration for structural feasibility and helpful in identifying the root causes, making it possible to design
inconsistencies in generated outcomes. Similarly, concept designers strategies to specifically address each of users’ concerns, incorpo-
rely heavily on factual, real-world information[72, 76], distinguish- rating both GenAI and traditional approaches as needed.
ing them from other design disciplines. Both formative and sum-
mative studies revealed that designers hesitate to adopt AI tools
due to fears of receiving inaccurate output, compounded by a gen- 9.2 Implication for GenAI in Iterative Ideation
eral preference to avoid over-reliance on others’ designs. As one Unlike existing AI tools commonly used by concept designers,
participant (P2) explained: “I mainly use photos as references and which typically follow a linear, one-step solution, AIdeation adopts
avoid concept art since, despite looking good, it may lack thorough, a nonlinear and iterative approach that aligns more closely with
factual research. AI-generated images have the same problem.” While designers’ ideation processes. This design philosophy is similar to
prior work in architectural design explores pre-trained models and frameworks such as OptiMuse [124] and DesignGPT [31], recogniz-
ControlNet [122] to improve accuracy [16], these methods are un- ing iteration as a fundamental aspect of the design process [2], and
suitable for concept design due to its broader scope. To mitigate many prior work has incorporated this principles [43, 46]. At dif-
this problem, AIdeation integrates non-AI image search to provide ferent stages of the design process, designers may require varying
real-world reference images, supporting the design elements of its levels of divergent and convergent thinking, along with cognitive
generated ideas and aligning with designers’ existing workflow for processes that balance exploring both breadth and depth. [42, 104].
reference gathering. This approach significantly increased design- Tools such as RoomDreaming used sliders to control the diversity
ers’ willingness to engage with the tool. As another participant of visual outputs [111], while GenQuery employs visual search and

---

CHI ’25, April 26–May 01, 2025, Yokohama, Japan Wang Lu Ponsa Chen Chen

image combination techniques to dynamically shift focus [96]. In A similar approach can be generalized to other design domains
contrast, AIdeation organizes the functionality into modular compo- that involve multiple phases of ideation, prototyping, and refine-
nents, where designers can switch between based on their current ment, such as fashion, graphic, architectural, and industrial de-
needs, providing the flexibility to adapt to different phases of the sign [13, 15]. Although many design fields have already integrated
creative process. These concepts apply to most creative processes. AI tools into their workflows [6], these tools often do not align
Future work could explore how GenAI can support different stages with domain-specific needs, which presents a significant opportu-
of ideation across various creative domains while allowing users to nity for HCI researchers to bridge this gap. Instead of relying on
seamlessly switch between them. one-size-fits-all AI solutions, researchers should use domain exper-
 During interviews, many designers highlighted that AIdeation tise to integrate the right tools, AI or otherwise, into workflows
was significantly easier to control and communicate with com- and ensure designers retain control over core creative decisions.
pared to other AI tools they had used. One participant noted, “I This approach results in systems that better meet user needs and
feel that AIdeation can effectively understand how I wish to modify outperform traditional or purely AI-driven solutions.
the current idea” (P6). This observation highlights the importance
of systems that understand user intentions and support clear and
effective communication. [94, 109]. Previous work, such as Intent-
 9.4 Limitations and Future Work
Tuner, has proposed frameworks to integrate human intentions 9.4.1 Limitations of the study. Due to the difficulty of including the
into fine-tuning general image generation systems [120]. In con- entire ideation process in our summative study and the challenge of
trast, AIdeation uses domain-specific knowledge to guide each AI directly comparing the results of the ideation between conditions,
module, ensuring that it aligns with the different phases of concept we relied mainly on self-reported data, which is a limitation of this
design. This approach improves communication between the tool work. While a follow-up field study evaluated real-world design
and designers. outputs with input from designers, directors, and clients, it lacked
 The principles behind AIdeation can guide the future develop- quantitative measures and had less control compared to lab studies.
ment of AI-assisted design tools. One promising direction is explor- Future research could explore longer summative sessions focused
ing how GenAI can better support collaboration, enabling directors on narrower tasks, like designing a single prop, which is simpler
and designers to co-create in shared workflows. Such systems could than broader tasks like environment design.
act as a communication bridge, integrating team inputs and sup-
porting both broad exploration and focused refinement. This aligns 9.4.2 Controllability. Although AIdeation emphasizes idea explo-
with the frameworks of Han et al., which highlights AI’s role in ration, participants noted its limitations in controlling specific de-
enhancing team creativity [43]. tails of generated results. Features like "combine with the reference"
 and "refine by instruction" provide high-level control but lack the
 ability to adjust elements such as lighting, atmosphere, camera
 angles, and composition while preserving other elements. These as-
 pects remain challenging and are active areas of AI research. As one
 participant (P4) remarked, “The system covers 70-80% for client com-
9.3 Integrating GenAI into the Design Workflow munication, but control over lighting, atmosphere, and camera angles
 with a Human-Centered AI Approach is needed for the final 20%.” As AI technology continues to advance,
While GenAI tools are increasingly used by designers across various such controllability features could be integrated into AIdeation.
domains, research shows they often fail to align with user-centered Future iterations of AIdeation could integrate such detailed con-
design principles. These shortcomings often result in user reluc- trols to better support designers’ focus and refinement during the
tance and inefficiencies [71, 110, 123]. Aligned with established convergence phase of their work.
principles of human-centered AI design [8, 94, 118], AIdeation pro-
vides a solution that prioritizes the needs and workflows of concept 9.4.3 Customization and personalization. Many users noted the
designers. limited diversity in art styles, atmosphere, and camera angles,
 Previous research in various design domains has demonstrated largely due to the constraints of the image generation model used
the use of GenAI to simplify nuanced tasks, enabling designers to in AIdeation. Different models have distinct strengths; for instance,
rapidly explore various visual concepts [28, 79, 111]. Furthermore, users appreciated MidJourney for its aesthetic quality, while Stable
studies have demonstrated the effectiveness of AI multi-agent col- Diffusion, fine-tuned with LoRA [48], offers more style variety and
laboration in managing complex tasks [29, 101]. AIdeation, on the specialized designs. Future updates could let users select specific
other hand, deconstructs complex workflows into modular tasks, styles or atmospheres, choose fine-tuned models, or allow the sys-
combining both suitable AI modules and non-AI tools for each tem to automatically pick the most suitable model based on input.
phase and integrating them into a cohesive workflow for concept Another option could be to generate multiple outputs from different
designers. This approach eliminates labor-intensive steps while re- models to better match the design task.
taining essential creative decisions, allowing users to focus on the Beyond image generation tuning, AIdeation can be personal-
core creative aspects of their work. In this context, GenAI functions ized to fit the design field, the designer’s specialization, and work
as a tool to augment human capabilities [19]. As one participant re- habits, similar to the ideas proposed by Long et al. [67]. The system
marked, “Using AIdeation felt like being an art director, with multiple could adapt to various design domains by modifying the prompts
design assistants gathering information and proposing ideas” (P13). or highlighting specific design elements to better suit individual

---

AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers CHI ’25, April 26–May 01, 2025, Yokohama, Japan

users. For instance, designers could select a focus, such as envi- [9] OP Boston, AW Court, SJ Culley, and CA McMahon. 1998. Design information
ronments, props, or characters, and AIdeation would generate cus- issues in new product development. In The design productivity debate. Springer,
 231–254.
tomized output accordingly. Although the system currently lacks [10] Josiah D Boucher, Gillian Smith, and Yunus Doğan Telliel. 2024. Is Resistance
the ability to retain context from previous sessions, future updates Futile?: Early Career Game Developers, Generative AI, and Ethical Skepticism.
 In Proceedings of the CHI Conference on Human Factors in Computing Systems.
could include memory features and personalized recommendations. 1–13.
Furthermore, incorporating self-adaptive capabilities, where the [11] Stephen Brade, Bryan Wang, Mauricio Sousa, Sageev Oore, and Tovi Grossman.
system adjusts its behavior based on user preferences or current 2023. Promptify: Text-to-Image Generation through Interactive Prompt Explo-
 ration with Large Language Models. Association for Computing Machinery (10
work stage, could further improve its effectiveness, as suggested in 2023). https://doi.org/10.1145/3586183.3606725
previous research [70]. [12] Alice Cai, Steven R Rick, Jennifer L Heyman, Yanxia Zhang, Alexandre Filipow-
 icz, Matthew Hong, Matt Klenk, and Thomas Malone. 2023. DesignAID: Using
 Generative AI and Semantic Diversity for Design Inspiration. Association for
10 CONCLUSION Computing Machinery (11 2023). https://doi.org/10.1145/3582269.3615596
 [13] Bradley Camburn, Vimal Viswanathan, Julie Linsey, David Anderson, Daniel
AIdeation, as an idea exploration tool, offers a unique blend of Jensen, Richard Crawford, Kevin Otto, and Kristin Wood. 2017. Design proto-
traditional and AI-driven approaches, providing broad exploration typing methods: state of the art in strategies, techniques, and guidelines. Design
through diverse references while generating new outputs based on Science 3 (2017), e13.
 [14] Marinela Capanu, Gregory A Jones, and Ronald H Randles. 2006. Testing for
user input. This enables designers to efficiently gather inspiration preference using a sum of Wilcoxon signed rank statistics. Computational
and produce a wide range of unique ideas. In addition, AIdeation statistics & data analysis 51, 2 (2006), 793–796.
 [15] Lisa Carlgren, Ingo Rauth, and Maria Elmquist. 2016. Framing design thinking:
streamlines the entire workflow by integrating research, brainstorm- The concept in idea and enactment. Creativity and innovation management 25,
ing, reference gathering, and design refinement into one cohesive 1 (2016), 38–57.
process, with the added flexibility of iterating design ideas easily. [16] Feiran Chen, Mengran Mai, Xinyi Huang, and Yinghan Li. 2024. Enhancing
 the Sustainability of AI Technology in Architectural Design: Improving the
Our study with 16 professional concept designers revealed that Matching Accuracy of Chinese-Style Buildings. Sustainability 16, 19 (2024),
AIdeation improved both the breadth and depth of idea exploration, 8414.
significantly enhanced creativity, and increased efficiency in gen- [17] Liuqing Chen, Qianzhi Jing, Yixin Tsang, Qianyi Wang, Ruocong Liu, Duowei
 Xia, Yunzhan Zhou, and Lingyun Sun. 2024. AutoSpark: Supporting Automobile
erating more diverse ideas of comparable quality to their original Appearance Design Ideation with Kansei Engineering and Generative AI. In
workflows. A field study conducted in four design studios further Proceedings of the 37th Annual ACM Symposium on User Interface Software and
 Technology. 1–19.
demonstrated that AI-driven ideation could potentially improve [18] Po-Yu Chen, Ching-Yi Tsai, Wei-Hsin Wang, Chao-Jung Lai, Chia-An Fan,
project efficiency, particularly for complex design tasks. Shih Chin Lin, Chia-Chen Chi, and Mike Y Chen. 2023. AirCharge: Ampli-
 fying Ungrounded Impact Force by Accumulating Air Propulsion Momentum.
 In Proceedings of the 36th Annual ACM Symposium on User Interface Software
Acknowledgments and Technology. 1–11.
This work was supported by the National Science and Technology [19] Xiang’Anthony’ Chen, Jeff Burke, Ruofei Du, Matthew K Hong, Jennifer Jacobs,
 Philippe Laban, Dingzeyu Li, Nanyun Peng, Karl DD Willis, Chien-Sheng Wu,
Council, Taiwan (NTSC 112-2221-E-002-185-MY3) and the Center et al. 2023. Next steps for human-centered generative ai: A technical perspective.
of Data Intelligence: Technologies, Applications, and Systems at arXiv preprint arXiv:2306.15774 (2023).
 [20] Thibault Groueix Vladimir G. Kim Nadir Weibel Chen Chen, Cuong Nguyen.
National Taiwan University (113L900901, 113L900902, 113L900903), 2024. MemoVis: A GenAI-Powered Tool for Creating Companion Reference Im-
funded through the Featured Areas Research Center Program under ages for 3D Design Feedback. ACM Transactions on Computer-Human Interaction,
the Higher Education Sprout Project by the Ministry of Education 2024 (09 2024). https://doi.org/10.48550/arXiv.2409.06082
 [21] Bob Cheshire. 2021. Concept Art: Interview with Bob Cheshire. https://magazine.
(MOE) of Taiwan. We also acknowledge support from National artstation.com/2021/09/concept-art-interview-with-bob-cheshire/.
Taiwan University, Moonshine Studio, Winking Studios, and Rayark [22] Li-Yuan Chiou, Peng-Kai Hung, Rung-Huei Liang, and Chun-Teng Wang. 2023.
Games. Finally, we extend our gratitude to all participants and Designing with AI: An Exploration of Co-Ideation with Image Generators. (2023),
 1941–1954. https://doi.org/10.1145/3563657.3596001
reviewers for their valuable feedback. [23] DaEun Choi, Sumin Hong, Jeongeon Park, John Joon Young Chung, and Juho
 Kim. 2024. CreativeConnect: Supporting Reference Recombination for Graphic
 Design Ideation with Generative AI. In Proceedings of the CHI Conference on
References Human Factors in Computing Systems. 1–25.
 [1] 3dtotal Publishing. 2018. The Ultimate Concept Art Career Guide. 3dtotal Pub- [24] Martin Stacey Claudia Eckert. 2019. Sources of inspiration: a language of design.
 lishing. Design Studies, Volume 21, Issue 5, 2000, Pages 523-538, ISSN 0142-694X (06 2019).
 [2] Robin S Adams and Cynthia J Atman. 1999. Cognitive processes in iterative https://doi.org/10.1016/S0142-694X(00)00022-3.
 design behavior. In FIE’99 Frontiers in Education. 29th Annual Frontiers in Ed- [25] William Jay Conover. 1999. Practical nonparametric statistics. Vol. 350. john
 ucation Conference. Designing the Future of Science and Engineering Education. wiley & sons.
 Conference Proceedings (IEEE Cat. No. 99CH37011, Vol. 1. IEEE, 11A6–13. [26] ComfyUI Contributors. 2023. ComfyUI: A powerful and modular Stable Diffusion
 [3] adobe. 2020. Bring an idea to life with concept art. https://www.adobe.com/ GUI and backend. https://github.com/comfyanonymous/ComfyUI.
 mena_en/creativecloud/illustration/discover/concept-art.html. [27] Steven M. Smi David G. Jansson. 2024. Design fixation. Design Studies, Volume
 [4] Shm Garanganao Almeda, JD Zamfirescu-Pereira, Kyu Won Kim, Pradeep 12, Issue 1 (11 2024). https://doi.org/10.1016/0142-694X(91)90003-F
 Mani Rathnam, and Bjoern Hartmann. 2024. Prompting for Discovery: Flexible [28] Richard Lee Davis, Thiemo Wambsganss, Wei Jiang, Kevin Gonyop Kim, Tanja
 Sense-Making for AI Art-Making with Dreamsheets. In Proceedings of the CHI Käser, and Pierre Dillenbourg. 2024. Fashioning Creative Expertise with Gen-
 Conference on Human Factors in Computing Systems. 1–17. erative AI: Graphical Interfaces for Design Space Exploration Better Support
 [5] N. Anantrasirichai and D. Bull. 2020. Artificial intelligence in the creative Ideation Than Text Prompts. In Proceedings of the CHI Conference on Human
 industries: a review. Artificial Intelligence Review 55 (2020), 589–656. https: Factors in Computing Systems. 1–26.
 //doi.org/10.1007/s10462-021-10039-7 [29] Fernanda De La Torre, Cathy Mengying Fang, Han Huang, Andrzej Banburski-
 [6] Nantheera Anantrasirichai and David Bull. 2022. Artificial intelligence in the Fahey, Judith Amores Fernandez, and Jaron Lanier. 2024. Llmr: Real-time prompt-
 creative industries: a review. Artificial intelligence review 55, 1 (2022), 589–656. ing of interactive worlds using large language models. In Proceedings of the CHI
 [7] J.S. Gero A.T. Purcell. 1992. Effects of examples on the results of a design activity. Conference on Human Factors in Computing Systems. 1–22.
 Knowledge-Based Systems, Volume 5, Issue 1 (09 1992). https://doi.org/10.1016/ [30] María del Mar Navarro. 2022. Research for Designers: A Guide to Methods
 0950-7051(92)90026-C. and Practice. Design and Culture 15 (2022), 130 – 133. https://doi.org/10.1080/
 [8] Jan Auernhammer. 2020. Human-centered AI: The role of Human-centered 17547075.2022.2138144
 Design Research in the development of AI. (2020).

---

CHI ’25, April 26–May 01, 2025, Yokohama, Japan Wang Lu Ponsa Chen Chen

 [31] Shiying Ding, Xinyi Chen, Yan Fang, Wenrui Liu, Yiwu Qiu, and Chunlei Chai. [55] Eric William Johnson. 1997. Analysis and refinement of iterative design processes.
 2023. DesignGPT: Multi-Agent Collaboration in Design. In 2023 16th Inter- University of Notre Dame.
 national Symposium on Computational Intelligence and Design (ISCID). IEEE, [56] Sangbum Kang, Yongjoo Choi, and Boyoung Kim. 2024. Impact of motivation
 204–208. factors for using generative AI services on continuous use intention: Mediating
 [32] Steven Dow, Blair MacIntyre, Jaemin Lee, Christopher Oezbek, Jay David Bolter, trust and acceptance attitude. Social Sciences 13, 9 (2024), 475.
 and Maribeth Gandy. 2005. Wizard of Oz support throughout an iterative design [57] Reishiro Kawakami and Sukrit Venkatagiri. 2024. The Impact of Generative
 process. IEEE Pervasive Computing 4, 4 (2005), 18–26. AI on Artists. In Proceedings of the 16th Conference on Creativity & Cognition.
 [33] Claudia Eckert and Martin. Stacey. 2000. Sources of Inspiration: A Language of 79–82.
 Design. Design Studies. 21.. (09 2000). https://doi.org/10.1016/S0142-694X(00) [58] Felix Yoon Khang Le, Mike Yamada. 2005. The Skillful Huntsman: Visual Devel-
 00022-3. opment of a Grimm Tale at Art Center College of Design. Design Studio Press.
 [34] Claudia Eckert and Martin Stacey. 2000. Sources of inspiration: a language of [59] Pierce R.A. Kim, K.H. 2018. Convergent Versus Divergent Thinking. Encyclopedia
 design. Design studies 21, 5 (2000), 523–538. of Creativity, Invention, Innovation and Entrepreneurship. Springer, New York, NY
 [35] Upol Ehsan, Q. Liao, Michael J. Muller, Mark O. Riedl, and Justin D. Weisz. (06 2018). https://doi.org/10.1007/978-1-4614-3858-8_22
 2021. Expanding Explainability: Towards Social Transparency in AI systems. [60] Sunnie S. Y. Kim. 2024. Establishing Appropriate Trust in AI through Trans-
 Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems parency and Explainability. Extended Abstracts of the CHI Conference on Human
 (2021). https://doi.org/10.1145/3411764.3445188 Factors in Computing Systems (2024). https://doi.org/10.1145/3613905.3638184
 [36] Ziv Epstein, Aaron Hertzmann, L. Herman, Robert Mahari, M. Frank, Matthew [61] Tiffany Knearem, M. Khwaja, Yuling Gao, Frank Bentley, and Clara Kliman-
 Groh, Hope Schroeder, Amy Smith, Memo Akten, Jessica Fjeld, H. Farid, Neil Silver. 2023. Exploring the future of design tooling: The role of artificial
 Leach, A. Pentland, and Olga Russakovsky. 2023. Art and the science of genera- intelligence in tools for user experience professionals. Extended Abstracts
 tive AI. Science 380 (2023), 1110 – 1111. https://doi.org/10.1126/science.adh4451 of the 2023 CHI Conference on Human Factors in Computing Systems (2023).
 [37] Zelun Tony Zhang et al. 2024. Beyond Recommendations: From Backward to https://doi.org/10.1145/3544549.3573874
 Forward AI Support of Pilots’ Decision-Making Process. ACM Hum.-Comput. [62] Hyung-Kwon Ko, Gwanmo Park, Hyeon Jeon, Jaemin Jo, Juho Kim, and Jinwook
 Interact (2024). Seo. 2023. Large-scale text-to-image generation models for visual artists’ creative
 [38] Ioannis Evangelidis. 2024. Task sensitivity and noise: How mechanical properties works. In Proceedings of the 28th international conference on intelligent user
 of preference elicitation tasks account for differences in preferences across tasks. interfaces. 919–933.
 Decision 11, 2 (2024), 283. [63] Yuan Li, Yinglong Zhang, and Robert Capra. 2022. Analyzing information
 [39] Tracy Fullerton. 2018. Game Design Workshop: A Playcentric Approach to Creating resources that support the creative process. In Proceedings of the 2022 Conference
 Innovative Games, Fourth Edition. A K Peters/CRC Press. on Human Information Interaction and Retrieval. 180–190.
 [40] Anat Litan Sever Gabriela Goldschmidt. 2019. Inspiring design ideas with [64] Eliott J. Lilly. 2015. Big Bad World of Concept Art for Video Games: An Insider’s
 texts. Design Studies,Volume 32, Issue 2,Pages 139-155,ISSN 0142-694X (06 2019). Guide for Students. Design Studio Press.
 https://doi.org/10.1016/j.destud.2010.09.006. [65] Xiang & Helmes John & Morris Richard & Meek Sam. Lindley, Siân & Cao. 2013.
 [41] Mari Gallet. 2023. Iteration and Reference in Concept Art. https://discover. Towards a Tool for Design Ideation: Insights from Use of SketchStorm. HCI
 therookies.co/2023/11/10/iteration-and-reference-in-concept-art/. 2013 - 27th International British Computer Society Human Computer Interaction
 [42] Gabriela Goldschmidt. 2016. Linkographic evidence for concurrent divergent Conference: The Internet of Things (09 2013). https://doi.org/10.14236/ewic/
 and convergent thinking in creative design. Creativity research journal 28, 2 HCI2013.13
 (2016), 115–122. [66] Julie S Linsey, Emily F Clauss, Tolga Kurtoglu, Jeremy T Murphy, Kristin L Wood,
 [43] Yuanning Han, Ziyi Qiu, Jiale Cheng, and RAY LC. 2024. When Teams Embrace and Arthur B Markman. 2011. An experimental study of group idea generation
 AI: Human Collaboration Strategies in Generative Prompting in a Creative techniques: understanding the roles of idea representation and viewing methods.
 Design Task. In Proceedings of the CHI Conference on Human Factors in Computing (2011).
 Systems. 1–14. [67] Tao Long, Katy Ilonka Gero, and Lydia B Chilton. 2024. Not Just Novelty:
 [44] Muhammad Hegazy and Ahmed Saleh. 2023. Evolution of AI role in architec- A Longitudinal Study on Utility and Customization of an AI Workflow. In
 tural design: between parametric exploration and machine hallucination. MSA Proceedings of the 2024 ACM Designing Interactive Systems Conference. 782–803.
 Engineering Journal 2, 2 (2023), 262–288. [68] Todd. Lubart. 2016. CREATIVITY AND CONVERGENT THINKING: REFLEC-
 [45] J. Hois, Dimitra Theofanou-Fuelbier, and Alischa Janine Junk. 2019. How to TIONS, CONNECTIONS AND PRACTICAL CONSIDERATIONS. RUDN Journal
 Achieve Explainability and Transparency in Human AI Interaction. (2019), of Psychology and Pedagogics. 7-15. (06 2016). https://doi.org/10.22363/2313-
 177–183. https://doi.org/10.1007/978-3-030-23528-4_25 1683-2016-4-7-15.
 [46] Yihan Hou, Manling Yang, Hao Cui, Lei Wang, Jie Xu, and Wei Zeng. 2024. [69] Sebastian Lubos, Thi Ngoc Trang Tran, Alexander Felfernig, Seda Polat Erdeniz,
 C2Ideas: Supporting Creative Interior Color Design Ideation with a Large Lan- and Viet-Man Le. 2024. LLM-generated Explanations for Recommender Systems.
 guage Model. In Proceedings of the CHI Conference on Human Factors in Comput- In Adjunct Proceedings of the 32nd ACM Conference on User Modeling, Adaptation
 ing Systems. 1–18. and Personalization. 276–285.
 [47] Vic Callaghan Hsuan-Yi Wu. 2016. From Imagination to Innovation: A Creative [70] Frank D Macías-Escrivá, Rodolfo Haber, Raul Del Toro, and Vicente Hernandez.
 Development Process. (2016). 2013. Self-adaptive systems: A survey of current approaches, research challenges
 [48] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean and applications. Expert Systems with Applications 40, 18 (2013), 7267–7279.
 Wang, and Weizhu Chen. 2021. LoRA: Low-Rank Adaptation of Large Language [71] Atefeh Mahdavi Goloujeh, Anne Sullivan, and Brian Magerko. 2024. Is It AI or
 Models. In International Conference on Learning Representations. https://arxiv. Is It Me? Understanding Users’ Prompt Journey with Text-to-Image Generative
 org/abs/2106.09685 AI Tools. In Proceedings of the CHI Conference on Human Factors in Computing
 [49] Min. Hua. 2019. The Roles of Sketching in Supporting Creative Design. The Systems. 1–13.
 Design Journal (06 2019). https://doi.org/10.1080/14606925.2019.1655187 [72] Negar Maleki, Balaji Padmanabhan, and Kaushik Dutta. 2024. AI hallucinations:
 [50] Rong Huang, Haichuan Lin, Chuanzhang Chen, Kang Zhang, and Wei Zeng. a misnomer worth clarifying. In 2024 IEEE Conference on Artificial Intelligence
 2024. PlantoGraphy: Incorporating Iterative Design Process into Generative (CAI). IEEE, 133–138.
 Artificial Intelligence for Landscape Rendering. , Article 168 (2024), 19 pages. [73] Adrian Marc. 2023. The Random Guidebook of Concept Designers : Tips and Tricks
 https://doi.org/10.1145/3613904.3642824 (1st ed.). JOLUA.
 [51] Ting-Hao ’Kenneth’ Huang, Boyang Li, Ying Xu, Alan Black, and Jeffrey P. [74] J. Mccormack, P. Hutchings, Toby Gifford, M. Yee-King, M. T. Llano, and M.
 Bigham. 2022. NaviPath: Enhancing User Navigation and Interaction in Complex d’Inverno. 2020. Design Considerations for Real-Time Collaboration with
 Information Spaces. In Proceedings of the CHI Conference on Human Factors in Creative Artificial Intelligence. Organised Sound 25 (2020), 41 – 52. https:
 Computing Systems. 39–50. //doi.org/10.1017/S1355771819000451
 [52] james paul. Javaid, Syed & Pandarakalam. 2021. The Association of Creativity [75] Mick Hurbis-Cherrier Michael Rabiger. 2020. Directing: Film Techniques and
 with Divergent and Convergent Thinking. Psychiatria Danubina. 33. 133-139 Aesthetics. Routledge.
 (06 2021). https://doi.org/10.24869/psyd.2021.133 [76] Scott Monteith, Tasha Glenn, John R Geddes, Peter C Whybrow, Eric Achtyes,
 [53] Youngseung Jeon, Seungwan Jin, Patrick C. Shih, and Kyungsik Han. 2021. and Michael Bauer. 2024. Artificial intelligence and increasing misinformation.
 FashionQ: An AI-Driven Creativity Support Tool for Facilitating Ideation in The British Journal of Psychiatry 224, 2 (2024), 33–35.
 Fashion Design. Association for Computing Machinery (05 2021). https://doi. [77] Oliver Müller, Stefan Debortoli, and Stefan Seidel. 2013. MUSE: implementation
 org/10.1145/3411764.3445093 of a design theory for systems that support convergent and divergent thinking.
 [54] Harry H Jiang, Lauren Brown, Jessica Cheng, Mehtab Khan, Abhishek Gupta, In Design Science at the Intersection of Physical and Virtual Design: 8th Interna-
 Deja Workman, Alex Hanna, Johnathan Flowers, and Timnit Gebru. 2023. AI tional Conference, DESRIST 2013, Helsinki, Finland, June 11-12, 2013. Proceedings
 Art and its Impact on Artists. In Proceedings of the 2023 AAAI/ACM Conference 8. Springer, 438–445.
 on AI, Ethics, and Society. 363–374. [78] Paul Newland, James A Powell, and Chris Creed. 1987. Understanding archi-
 tectural designers’ selective information handling. Design Studies 8, 1 (1987),

---

AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers CHI ’25, April 26–May 01, 2025, Yokohama, Japan

 2–16. [106] Severi Uusitalo, Antti Salovaara, Tero Jokela, and Marja Salmimaa. 2024. ”Clay
 [79] Jeongseok Oh, Seungju Kim, and Seungjun Kim. 2024. LumiMood: A Creativity to Play With”: Generative AI Tools in UX and Industrial Design Practice. (2024),
 Support Tool for Designing the Mood of a 3D Scene. In Proceedings of the CHI 1566–1578. https://doi.org/10.1145/3643834.3661624
 Conference on Human Factors in Computing Systems. 1–21. [107] Siddhartha Valluri. 2020. Game Concept Artist Interview. https://
 [80] Srishti Palani, David Ledo, George Fitzmaurice, and Fraser Anderson. 2022. theinterviewportal.com/2020/08/16/game-concept-artist-interview/.
 ” I don’t want to feel like I’m working in a 1960s factory”: The Practitioner [108] Kamala Venigandla, Navya Vemuri, and Naveen Vemuri. 2024. Hybrid Intelli-
 Perspective on Creativity Support Tool Adoption. In Proceedings of the 2022 CHI gence Systems Combining Human Expertise and AI/RPA for Complex Problem
 Conference on Human Factors in Computing Systems. 1–18. Solving. International Journal of Innovative Science and Research Technology
 [81] Innwoo Park and Michael J Hannafin. 1993. Empirically-based guidelines for (IJISRT) (2024). https://doi.org/10.38124/ijisrt/ijisrt24mar2039
 the design of interactive multimedia. Educational Technology Research and [109] Roberto Verganti, Luca Vendraminelli, and Marco Iansiti. 2020. Innovation
 Development 41, 3 (1993), 63–85. and design in the age of artificial intelligence. Journal of product innovation
 [82] Xiaohan Peng, Janin Koch, and Wendy E. Mackay. 2024. DesignPrompt: Using management 37, 3 (2020), 212–227.
 Multimodal Interaction for Design Exploration with Generative AI. (2024), [110] Veera Vimpari, Annakaisa Kultima, Perttu Hämäläinen, and Christian Guckels-
 804–818. https://doi.org/10.1145/3643834.3661588 berger. 2023. “An Adapt-or-Die Type of Situation”: Perception, Adoption, and
 [83] Jiayang Qin. 2023. How does Text-to-image AI Affect Indie Game Designers Use of Text-to-Image-Generation AI by Game Industry Professionals. Proceed-
 and Artists? Journal of Innovation and Development 5, 3 (2023), 107–111. ings of the ACM on Human-Computer Interaction 7, CHI PLAY (2023), 131–164.
 [84] Julia Rässa. 2018. Concept art creation methodologies: Visual Development of [111] Shun-Yu Wang, Wei-Chung Su, Serena Chen, Ching-Yi Tsai, Marta Misztal,
 “Rock Boy”. (2018). Katherine M Cheng, Alwena Lin, Yu Chen, and Mike Y Chen. 2024. Room-
 [85] Jeba Rezwana and Mary Lou Maher. 2023. Designing creative AI partners with Dreaming: Generative-AI Approach to Facilitating Iterative, Preliminary Interior
 COFI: A framework for modeling interaction in human-AI co-creative systems. Design Exploration. In Proceedings of the CHI Conference on Human Factors in
 ACM Transactions on Computer-Human Interaction 30, 5 (2023), 1–28. Computing Systems. 1–20.
 [86] Steven R Rick, Gianni Giacomelli, Haoran Wen, Robert J. Laubacher, Nancy [112] Yunlong Wang, Shuyuan Shen, and Brian Y Lim. 2023. Reprompt: Automatic
 Taubenslag, Jennifer L. Heyman, Max Sina Knicker, Younes Jeddi, Hendrik Maier, prompt editing to refine ai-generative art towards precise expressions. In Pro-
 Stephen Dwyer, Pranav Ragupathy, and Thomas Malone. 2023. Supermind ceedings of the 2023 CHI conference on human factors in computing systems.
 Ideator: Exploring generative AI to support creative problem-solving. ArXiv 1–29.
 abs/2311.01937 (2023). https://doi.org/10.48550/arXiv.2311.01937 [113] Zhijie Wang, Yuheng Huang, Da Song, Lei Ma, and Tianyi Zhang. 2024.
 [87] Paula K Roberson, SJ Shema, DJ Mundfrom, and TM Holmes. 1995. Analysis of PromptCharm: Text-to-Image Generation through Multi-modal Prompting and
 paired Likert data: how to evaluate change and preference questions. Family Refinement. , Article 185 (2024), 21 pages. https://doi.org/10.1145/3613904.
 medicine 27, 10 (1995), 671–675. 3642803
 [88] Scott Rogers. 2014. Level Up! The Guide to Great Video Game Design. Wiley. [114] Jacob & Merzdorf Hillary & Dorozhkin Denis & Douglas Kerrie & Linsey Julie.
 [89] Arvind Satyanarayan, Bongshin Lee, Donghao Ren, Jeffrey Heer, John Stasko, Weaver, Morgan & Buck. 2022. Investigating Priming Effects of Sketch Evalu-
 John Thompson, Matthew Brehmer, and Zhicheng Liu. 2019. Critical reflections ation Instructions on Idea Generation Productivity. ASME 2022 International
 on visualization authoring systems. IEEE transactions on visualization and Design Engineering Technical Conferences and Computers and Information in
 computer graphics 26, 1 (2019), 461–471. Engineering Conference (11 2022). https://doi.org/10.1115/DETC2022-91313
 [90] Ojas D. Sawant. 2024. Visual Storytelling with Generative AI: A Practical Handbook [115] WeiliJiang MengPei andYanjieSu WeiliZhu, SiyuanShang. 2019. Convergent
 for modern Filmmakers and Content Creators. Independently published. thinking moderates the relationship between divergent thinking and scientific
 [91] Nicolas Scharowski, S. Perrig, Melanie Svab, K. Opwis, and Florian Brühlmann. creativity. Creativity Research Journal 31, 3 (2019), 320–328. (06 2019). https:
 2023. Exploring the effects of human-centered AI explanations on trust and //doi.org/10.1080/10400419.2019.1641685
 reliance. Frontiers Comput. Sci. 5 (2023). https://doi.org/10.3389/fcomp.2023. [116] Kjellin A. Lind M. & Seipel S. Winkler Pettersson, L. 2010. On the role of visual
 1151150 references in collaborative visualization. Information Visualization, 9(2), 98–114.
 [92] Jesse Schell. 2008. The Art of Game Design: A Book of Lenses. CRC Press. (09 2010). https://doi.org/10.1057/ivs.2009.2
 [93] Jingyu Shi, Rahul Jain, Runlin Duan, and Karthik Ramani. 2023. Understanding [117] Xueying Xie. 2023. The cognitive process of creative design: A perspective
 Generative AI in Art: An Interview Study with Artists on G-AI from an HCI of divergent thinking. Thinking Skills and Creativity, Volume 48 (06 2023).
 Perspective. arXiv preprint arXiv:2310.13149 (2023). https://doi.org/10.1016/j.tsc.2023.101266.
 [94] Ben Shneiderman. 2022. Human-centered AI. Oxford University Press. [118] Wei Xu, Marvin J Dainoff, Liezhong Ge, and Zaifeng Gao. 2023. Transitioning to
 [95] Hardeep Singh, Kamaljeet Kaur, and Preet Pinder Singh. 2023. Artificial Intel- human interaction with AI systems: New challenges and opportunities for HCI
 ligence as a facilitator for Film Production Process. 2023 International Confer- professionals to enable human-centered AI. International Journal of Human–
 ence on Artificial Intelligence and Smart Communication (AISC) (2023), 969–972. Computer Interaction 39, 3 (2023), 494–518.
 https://doi.org/10.1109/AISC56616.2023.10085082 [119] Zihan Yan, Chunxu Yang, Qihao Liang, and Xiang’Anthony’ Chen. 2023. XCre-
 [96] Kihoon Son, DaEun Choi, Tae Soo Kim, Young-Ho Kim, and Juho Kim. 2024. ation: A Graph-based Crossmodal Generative Creativity Support Tool. In Pro-
 GenQuery: Supporting Expressive Visual Search with Generative Models. In ceedings of the 36th Annual ACM Symposium on User Interface Software and
 Proceedings of the CHI Conference on Human Factors in Computing Systems. 1–19. Technology. 1–15.
 [97] A. Stamps. 1999. Demographic Effects in Environmental Aesthetics: A Meta- [120] Xingchen Zeng, Ziyao Gao, Yilin Ye, and Wei Zeng. 2024. IntentTuner: An
 Analysis. Journal of Planning Literature 14 (1999), 155 – 175. https://doi.org/10. Interactive Framework for Integrating Human Intentions in Fine-tuning Text-
 1177/08854129922092630 to-Image Generative Models. In Proceedings of the CHI Conference on Human
 [98] Edward Pincus Steven Ascher. 2019. The Filmmakers Handbook: A Comprehensive Factors in Computing Systems. 1–18.
 Guide for the Digital Age. PLUME BOOKS. [121] Hongbo Zhang, Pei Chen, Xuelong Xie, Chaoyi Lin, Lianyan Liu, Zhuoshu Li,
 [99] I. Stigliani and Davide Ravasi. 2018. The Shaping of Form: Exploring Designers’ Weitao You, and Lingyun Sun. 2024. ProtoDreamer: A Mixed-prototype Tool
 Use of Aesthetic Knowledge. Organization Studies 39 (2018), 747 – 784. https: Combining Physical Model and Generative AI to Support Conceptual Design.
 //doi.org/10.1177/0170840618759813 In Proceedings of the 37th Annual ACM Symposium on User Interface Software
[100] SM Taheri and Gholamreza Hesamian. 2013. A generalization of the Wilcoxon and Technology. 1–18.
 signed-rank test and its applications. Statistical Papers 54 (2013), 457–470. [122] Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. 2023. Adding conditional
[101] Yashar Talebirad and Amirhossein Nadiri. 2023. Multi-agent collaboration: control to text-to-image diffusion models. In Proceedings of the IEEE/CVF Inter-
 Harnessing the power of intelligent llm agents. arXiv preprint arXiv:2306.03314 national Conference on Computer Vision. 3836–3847.
 (2023). [123] Shuning Zhang and Shixuan Li. 2024. " Confrontation or Acceptance": Under-
[102] Kirill Tokarev. 2020. Working as a Concept Artist in the Fast-Paced Film Indus- standing Novice Visual Artists’ Perception towards AI-assisted Art Creation.
 try. https://80.lv/articles/working-as-a-concept-artist-in-the-fast-paced-film- arXiv preprint arXiv:2410.14925 (2024).
 industry/. [124] Jiayi Zhou, Renzhong Li, Junxiu Tang, Tan Tang, Haotian Li, Weiwei Cui, and
[103] Tiffany Tseng, Ruijia Cheng, and Jeffrey Nichols. 2024. Keyframer: Empowering Yingcai Wu. 2024. Understanding Nonlinear Collaboration between Human
 Animation Design using Large Language Models. ArXiv abs/2402.06071 (2024). and AI Agents: A Co-design Framework for Creative Design. In Proceedings of
 https://api.semanticscholar.org/CorpusID:267616691 the 2024 CHI Conference on Human Factors in Computing Systems (Honolulu,
[104] Barbara Tversky and Juliet Y Chou. 2011. Creativity: depth and breadth. In HI, USA) (CHI ’24). Association for Computing Machinery, New York, NY, USA,
 Design creativity 2010. Springer, 209–214. Article 170, 16 pages. https://doi.org/10.1145/3613904.3642812
[105] Usman Ahmad Usmani, A. Happonen, and J. Watada. 2023. Human-Centered [125] Mingxu Zhou, Dengming Zhang, Weitao You, Ziqi Yu, Yifei Wu, Chenghao Pan,
 Artificial Intelligence: Designing for User Empowerment and Ethical Con- Huiting Liu, Tianyu Lao, and Pei Chen. 2024. StyleFactory: Towards Better
 siderations. 2023 5th International Congress on Human-Computer Interac- Style Alignment in Image Creation through Style-Strength-Based Control and
 tion, Optimization and Robotic Applications (HORA) (2023), 01–05. https: Evaluation. In Proceedings of the 37th Annual ACM Symposium on User Interface
 //doi.org/10.1109/HORA58378.2023.10156761 Software and Technology. 1–15.

---

CHI ’25, April 26–May 01, 2025, Yokohama, Japan Wang Lu Ponsa Chen Chen

A Appendix A: Questionnaire for Summative 2. When searching for materials and reference images, how
 Study does AIdeation differ from your original workflow? What
 are the strengths and weaknesses of AIdeation? (Information
 1. Breadth: Which system provided more diverse explo-
 and Reference Gathering)
 ration in design ideas?
 3. You selected {System} for faster generation of diverse design
 2. Depth: Which system supported a deeper, more detailed
 ideas. Could you explain why? (Design Output)
 exploration of design ideas?
 4. You selected {System} for generating higher-quality design
 3. Flexibility: Which system provides greater flexibility in
 ideas. Could you explain why? (Design Output)
 exploring different design ideas?
 5. You selected {System} for providing more useful reference
 4. Creativity: Which system do you feel enhanced your
 images. Could you explain why? (Information and Reference
 creativity more?
 Gathering)
 5. User Satisfaction Comparison: Which system do you
 find more satisfying to use overall?
 6. User Enjoyment: Which system do you find more en- Ideation and Exploration
 joyable to use overall? 1. When exploring design ideas, how does AIdeation differ from
 7. Task Difficulty: Which system do you find makes the your original workflow? What are AIdeation’s strengths and
 overall task easier? weaknesses? (Exploration Support)
 8. Task Efficiency: Which system helped you complete 2. When exploring design ideas, how does AIdeation compare
 your work more efficiently overall? to your original workflow in terms of breadth (diversity,
 9. Design Ideas Efficiency: Which system allows you to creativity) and depth (detail, thoroughness)? (Depth and
 more quickly generate a variety of design ideas? Breadth)
 10. Design Idea Quality: Which system helps you generate 3. You selected {System} for enhancing creativity. Could you
 higher quality design ideas? explain why?
 11. Information Support: Which system allows you to
 more efficiently gather information for the design task? Questions for Scoring
 12. Reference Gathering Efficiency: Which system more 1. You gave a score of X for [specific feature]. Why?
 efficiently helped you gather the references needed to
 complete the task? Final Feedback
 13. Usefulness of References: Which system provides more 1. Do you think AIdeation lacks any features, or are there fea-
 useful reference images? tures that need improvement?
 14. Visual Presentation: Which system better helps you 2. Do you think you will use AIdeation in your future work?
 visually present your design ideas? Why or why not? If yes, how would you use it?

B Appendix B: Interview Questions for C Appendix C: Idea Generation GPT
 Summative Study
 You're a helpful assistant who aids artists in generating creative visual ideas based on given
General Questions instructions and reference descriptions. You will receive an instruction, a reference
 image description or both, and a creative score between 0 and 1. The instruction details
 1. What are your thoughts on using AI-generated images in how the visual design should follow. The description comes from the image captioning of
 an input reference from an artist. The creative score indicates the creativity level of
 your workflow? On a scale from 1 to 7, how would you the design idea you provide, where 1 means highly diverse from the original image, and
 rate your acceptance of AI? - Completely unacceptable / 0 means very similar to the original image. The artist seeks to explore more visual
 ideas based on the instruction and reference image. Provide 1 design idea based on the
 Acceptable as a reference or design aid / Acceptable for direct input.
 use in design. # Guideline
 - The design idea should include Art Style, Theme, Content, Lighting and Atmosphere, Color
 Palette, Layout and Shot Angle
Overall Questions - You have to always follow the instructions provided by the artist, regardless of the creative
 score.
 1. Compared to your original workflow, what do you think is - You need to balance relevance and creativity based on the creative score. If the creative
 the biggest difference when using AIdeation? score is low, you should provide a design idea that closely matches the image
 description while still incorporating some differences. If the variety score is high,
 2. Could you briefly describe your thought process and execu- you should offer a more creative idea with some relevance to the original description.
 tion flow while using AIdeation, and how you plan to use - High creative score should result in innovative idea, and low creative score should result in
 conservative approach.
 the reference images you found? - You do not need to completely follow the original image description if the variety score is

 3. You selected {System} for overall efficiency and System for high.
 - If the Creative score is very high (0.8 to 1), please be very creative and diverse.
 task difficulty. Could you explain why? - If there is no input image, the art style should be "Painterly concept art".
 - The output has to be in English, no matter the input language of the instuction.
 4. You selected {System} for enjoyment and satisfaction. Could - The output should be lower than 400 characters.
 you explain why?
 # Output format
 Your output must be in the format below:
 ### Theme
System Workflow Support ...

 1. Which feature(s) in AIdeation do you find most helpful, and ### Art Style
 ...
 why? ### Content

---

AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers CHI ’25, April 26–May 01, 2025, Yokohama, Japan

Subcontent1: ... Warm, atmospheric lighting with deep shadows, created by multiple light sources such as vintage
Subcontent2: ... lamps, the red glow of the darkroom, and sunlight streaming through the large factory
Subcontent3: ... windows. The room should feel lived-in and slightly chaotic, reflecting the creative and
Subcontent4: ... industrious spirit of the era.
Subcontent5: ... ### Color Palette
SubcontentN: ... Muted and earthy tones, dominated by browns, sepia, and greys, with splashes of color from the
### Lighting and Atmosphere red darkroom light and various photographic materials. The overall palette should evoke
... a sense of nostalgia and timelessness.
### Color Palette ### Layout
... Spatial Arrangement: The central workstation should be the focal point, with additional stations
### Layout and furniture arranged organically around it, creating a sense of organized clutter.
... ### Shot Angle
### Shot Angle 3/4 View: The design shot should be from a 3/4 view, offering a comprehensive look at the room's
... layout and depth.

The amount of Subcontent is not fixed, and the output has to be in English. ## Example
 INPUT:
 Creative Score: 1.0
# Examples Instructions:
## Example None
INPUT: Image Description:
Creative Score: 0.5 This image portrays a fantastical landscape filled with organic-looking architectural structures
Instructions: that blend seamlessly into lush, green surroundings. Each building is unique,
We are going back in history for this next project. You will be designing a workshop room for a resembling large fruits or gourds with openings and extensions that serve as windows and
 Photographer or Film Camera Room from 1930s by utilizing as much reference as you can balconies, all supported by wooden frameworks. The landscape features vibrant greenery,
 gather. This project is both about historic accuracy and entertainment value. blooming flowers, and various species of trees, creating a serene and naturalistic
Specification: setting. Foreground elements include wooden pathways and bridges connecting the
1. GATHER as much references as possible. Rely on old paintings, photographs, museum displays structures, with characters in various traditional or fantasy-inspired outfits exploring
 and even historic movies. the area. In the background, the terrain gently rolls away into distant hills dotted
2. MAKE SURE you based this off of history. with similar architectural features, under a vast, clear blue sky with few clouds. This
3. WE WANT these rooms to feel accurate but also entertaining. This usually means expanding the serene setting combines elements of nature with a hint of mysticism and fantasy,
 set to be slightly bigger with additional details (allows for exploration). invoking a peaceful, otherworldly village.
4. USE APPROPRIATE historic architecture to match the profession. Don't place these objects in a
 generic rectangular room. We need to see the materials, architectural stylings and OUTPUT:
 layout. In other words, even if we remove all the set dressing from the room, the empty ### Theme
 room itself should look nice (in an industrial factory, a mansion, etc.) Enchanted Fairy Village blending nature and fantastical architecture seamlessly.
5. THE ROOM CAN HAVE MULTIPLE STATIONS. For example, a telegraph room can have many tables, each ### Art Style
 with a telegraph machine Painterly concept art with loose brushstrokes, rich textures, and an emphasis on mood and
6. PAY ATTENTION to details (cables, knobs, tea cups, etc.) Make this space feel alive. atmosphere.
7. DON'T MAKE each station a perfect copy/paste. Not everything is perfect in real life. Make ### Content
 variations. Central Focus: A large, central treehouse structure that spirals upward, resembling a giant
8. ROOM MUST show partial cutaway of exterior. twisted gourd intertwined with vines and flowers. It has multiple levels with balconies,
9. THINK OF MATERIAL COHESION. A photographer's room would look nice in a Victorian styled room. windows, and hanging lanterns.
 We are after pleasing visuals. Surrounding Structures: Smaller houses resembling fruits and vegetables (like pumpkins, melons,
10. The design shot should be 3/4 view: finished line-work, grey wash separated objects, light and berries) scattered around, each uniquely designed with natural materials like wood,
 and shadow. The whole page needs to be filled properly and lots of details presented. leaves, and vines.
 Color is optional. Pathways and Bridges: Winding wooden pathways and rope bridges connecting the treehouses and
Image Description: ground-level homes, with small, glowing fairy lights hanging along the edges.
The image depicts a cluttered, vintage film editing room with a nostalgic and somewhat dark Characters: Fantastical inhabitants such as fairies, elves, and other mythical creatures in
 atmosphere. Key elements include: colorful, traditional attire. They are engaged in various activities like gardening,
1. **Film Editing Equipment**: There are film reels, splicing equipment, and various tools crafting, and playing musical instruments.
 essential for film editing. The central focus is a film reel mounted on a desk with film Nature Elements: Abundant greenery with tall, ancient trees, vibrant flowers, and a crystal-
 strips hanging from it. clear stream flowing through the village. Wildlife such as butterflies, birds, and small
2. **Desks and Chairs**: The workspace is filled with wooden desks and chairs, all showing signs woodland creatures add life to the scene.
 of wear and tear, adding to the vintage feel. Mystical Features: Magical elements like floating lanterns, glowing mushrooms, and a hidden
3. **Shelving and Storage**: Wooden shelves and storage units line the walls, containing film fairy circle made of luminescent stones.
 reels, canisters, and various other items, suggesting a busy and well-used workspace. ### Lighting and Atmosphere
4. **Lighting**: The lighting is dim, with a single desk lamp illuminating the central workspace Magical and Ethereal: Soft, diffused lighting with a warm golden hue, creating a dreamlike
 , creating a moody and focused atmosphere. atmosphere. Fairy lights and lanterns add a gentle glow, enhancing the mystical ambiance.
5. **Wall Decorations**: Posters and equipment adorn the walls, adding to the historical context
 of the room. One prominent poster features classic film imagery. Dynamic Sky: A vast sky with a soft gradient from a pastel blue to a warm sunset orange, dotted
6. **Additional Items**: Papers, notes, and various small tools are scattered across the desks, with a few fluffy clouds and faint, sparkling stars beginning to appear.
 indicating an active workspace. ### Color Palette
The overall style is retro and industrial, evoking a sense of a bygone era in film editing. The Vibrant and Lush: Dominated by rich greens, warm browns, and earthy tones, accented with pops of
 dark, cluttered setting with focused lighting creates a dramatic and immersive vibrant colors from flowers, fruits, and inhabitants' clothing. The sky adds pastel
 atmosphere. blues and warm oranges.
 ### Layout
OUTPUT: Organic and Flowing: Structures are integrated into the natural landscape, with pathways and
### Theme bridges meandering organically through the village. The central treehouse is the focal
1930s Photographer/Film Camera Room in an Industrial Factory point, with other elements arranged naturally around it, creating a harmonious and
### Art Style cohesive scene.
Realistic with a focus on detailed line-work and textures. ### Shot Angle
### Content Wide Panoramic View: Capturing the entire village from a slightly elevated perspective,
Central Workstation: A large wooden desk with a vintage film camera setup, surrounded by film providing a comprehensive look at the intricate details of the architecture and the lush
 reels, developing chemicals, and photographs pinned to a corkboard. , enchanting landscape. This angle showcases the depth and expansiveness of the scene,
Darkroom corner: A darkroom corner with red lighting, featuring developing trays, drying racks drawing the viewer into the magical world.
 with hanging photographs, and shelves of chemical bottles.
Repair station: a repair station with an assortment of tools, spare parts, and blueprints for
 camera equipment. D Appendix D: Keyword Extraction GPT
Furniture: Sturdy wooden furniture including a couple of mismatched chairs, a vintage sofa, and
 a small table with a typewriter and papers. You're a helpful assistant who helps artists generate keywords to search online based on a
Decorations: Walls adorned with framed black-and-white photographs, sketches, and posters from design idea. You will get a detailed design idea. Please first identify the visual
 old films. A large window partially covered with blackout curtains. element in the text, and generate keywords that can accurately depict the idea. The
Miscellaneous Items: Scattered film canisters, boxes of photography supplies, old newspapers, a keywords should include descriptions of the theme, art style, specific content items,
 rotary phone, tea cups, and saucers. lighting and atmosphere, color palette, layout, and shot angle. The goal is to capture
Exterior Cutaway: Partial view showing the factory exterior with brick walls, large industrial the essence of the visual aspects to facilitate a comprehensive and accurate search.
 windows, and a glimpse of a cobblestone street outside.
### Lighting and Atmosphere
 # Keywords Numbers Limit:

---

CHI ’25, April 26–May 01, 2025, Yokohama, Japan Wang Lu Ponsa Chen Chen

- At most 3 for Theme 3/4 View: The design shot should be from a 3/4 view, offering a comprehensive look at the room's
- At most 3 for Art style layout and depth.
- At most 20 for Content
- At most 5 for Lighting and Atmosphere OUTPUT:
- At most 5 for Color Pallete ### Theme
- At most 3 for Shot Angle * 1930s Photographer
 * Industrial Factory

# Guidelines: ### Art Style
- The keyword number cannot be over the Limit. * Realistic
- Add a descriptive adjective before the objects to accurately convey their characteristics, * Detailed Line-Work
 such as indicating the time period or condition of the object. For example, instead of * Vintage Historical
 just "car," use "vintage car" or "rusty car."
- The keyword should focus on the design idea's content. ### Content
- The keyword should be simple, but with enough information. The keyword shouldn't be longer #### Central Workstation
 than 5 words. * Vintage Large Wooden Desk
- The keywords should focus on the key elements in each part. * Vintage Film Camera
- You should omit the Layout part. * Film Reels
- The output should follow the markdown format in the Example * Old Developing Chemicals
 * Corkboard Photographs
 #### Darkroom corner
# Output format * Darkroom Corner for film
Your output must be in the format below: * Red Lighting Darkroom
### Theme * Photo Developing Trays
* ... * Vintage Drying Racks
 * Chemical Bottles shelf
### Art Style #### Repair station
* ... * Vintage Repair Station
 * Vintage Assorted Tools
### Content * Vintage Camera Spare Parts
#### Subcontent1 * Vintage Camera Blueprints
* ... #### Furniture
#### Subcontent2 * Sturdy Wooden Furniture
* ... * Vintage Mismatched Chairs
#### Subcontent3 * Vintage Sofa
* ... * Typewriter Table
#### Subcontent4 #### Decorations
* ... * Vintage Framed Photographs
#### Subcontent5 * Old Film Posters
* ... * Vintage Large Window
 * Blackout Curtains
### Lighting and Atmosphere #### Miscellaneous
* ... * Scattered Film Canisters
 * Vintage Photography Supplies
### Color Palette * Old Newspapers
* ... * Vintage Rotary Phone
 * Old Tea Cups and Saucers
### Shot Angle #### Exterior Cutaway:
* ... * Old Factory Exterior
 * Brick Walls
The amount of Subcontent should be based on the input * Industrial Windows
 * Cobblestone Street

# Example ### Lighting and Atmosphere
INPUT: * Warm Lighting
Design Idea: * Atmospheric Shadows
### Theme * Vintage Lamps
1930s Photographer/Film Camera Room in an Industrial Factory * Red Darkroom Glow
### Art Style * Sunlight Streams
Realistic with a focus on detailed line-work and textures, emphasizing the vintage and
 historical accuracy of the 1930s era. ### Color Palette
### Content * Muted Browns
Central Workstation: A large wooden desk with a vintage film camera setup, surrounded by film * Sepia Tones
 reels, developing chemicals, and photographs pinned to a corkboard. * Earthy Greys
Darkroom corner: A darkroom corner with red lighting, featuring developing trays, drying racks * Nostalgic Colors
 with hanging photographs, and shelves of chemical bottles. * Red Accents
Repair station: a repair station with an assortment of tools, spare parts, and blueprints for
 camera equipment. ### Shot Angle
Furniture: Sturdy wooden furniture including a couple of mismatched chairs, a vintage sofa, and * 3/4 View
 a small table with a typewriter and papers.
Decorations: Walls adorned with framed black-and-white photographs, sketches, and posters from
 old films. A large window partially covered with blackout curtains.
Miscellaneous Items: Scattered film canisters, boxes of photography supplies, old newspapers, a E Appendix E: Combining Idea GPT
 rotary phone, tea cups, and saucers.
Exterior Cutaway: Partial view showing the factory exterior with brick walls, large industrial You're a helpful assistant who supports artists in generating creative visual concepts by
 windows, and a glimpse of a cobblestone street outside. integrating an original design idea with the description of a reference image. Your task
### Lighting and Atmosphere is to blend the reference image's description into the original design idea. You will
Warm, atmospheric lighting with deep shadows, created by multiple light sources such as vintage be provided with a keyword, a description of the visual design idea, a description of
 lamps, the red glow of the darkroom, and sunlight streaming through the large factory the reference image, and a variety score ranging from 0 to 1. The keyword indicates the
 windows. The room should feel lived-in and slightly chaotic, reflecting the creative and specific aspect of the original idea that needs modification. The variety score
 industrious spirit of the era. represents the level of creativity required in incorporating the reference image into
### Color Palette the original idea, with 1 signifying a design that significantly diverges from the
Muted and earthy tones, dominated by browns, sepia, and greys, with splashes of color from the original and 0 indicating a design that remains very similar. Your task is to adjust or
 red darkroom light and various photographic materials. The overall palette should evoke combine the relevant part of the design idea based on the keyword and variety score,
 a sense of nostalgia and timelessness. resulting in one new design concept that reflects the specified creativity level.
### Layout
Spatial Arrangement: The central workstation should be the focal point, with additional stations # Guideline
 and furniture arranged organically around it, creating a sense of organized clutter. - The design idea should include Art Style, Theme, Content, Lighting and Atmosphere, Color
### Shot Angle Palette, Layout and Shot Angle

---

AIdeation: Designing a Human-AI Collaborative Ideation System for Concept Designers CHI ’25, April 26–May 01, 2025, Yokohama, Japan

- You should identify the part to be modified based on the keyword and the description of the ### Theme
 reference image. Fantastical Forest Retreat Alongside a Serene Lakeside
- The keyword should be used solely to locate the part of the original design idea that needs ### Art Style
 modification and should not influence the content of the modification. Illustrative with painterly quality, emphasizing detail and smooth gradients
- The part specified by the keyword must always be modified using the reference description, ### Content
 regardless of the variety score. - **Central Structures**: Whimsical, stone-covered, plant-pod-like buildings. The domes are
- If the keyword is not present in the original design idea, find a reasonable way to integrate constructed from irregularly shaped stones, blending rustic elements with intricate
 the reference image into the original design idea. plant growth. Some feature stone pillars supporting porch-like extensions with lattices,
- You should create a harmonious blend between the original description and the reference image. integrating seamlessly into the natural surroundings.
- Balance relevance and creativity according to the variety score: for a low score, adjust only - **Lakeside Area**: A tranquil lake with clear blue waters reflecting the lush surroundings,
 the part specifed by the keyword; for a high score, introduce broader changes inspired with characters standing at its edge.
 by the reference image while maintaining relevance to the original idea. - **Hills and Background**: Gentle rolling hills, numerous trees, and distant mountains creating
- Higher creative score should result in innovative idea. a picturesque, layered backdrop.
- The output should be lower than 400 characters. - **Characters**: Fantasy attire-clad characters, including an adventurer holding a staff or
 weapon, interacting with nature.
# Output format - **Paths and Integrations**: Curved, brick-paved pathways winding through the forest,
Your output must be in the format below: connecting the structures seamlessly to the environment.
### Theme ### Lighting and Atmosphere
... Soft and inviting with smooth shadows, capturing a serene and harmonious ambiance. The lighting
### Art Style emphasizes the natural vibrancy, enhancing the dreamlike feel.
... ### Color Palette
### Content Vibrant and saturated greens for vegetation, blues for the sky and water, with accents of earthy
Subcontent1: ... browns and soft yellows. The palette induces calmness and wonder.
Subcontent2: ... ### Layout
Subcontent3: ... Organic and flowing with structures and pathways naturally embedded into the landscape,
Subcontent4: ... emphasizing harmony between architecture and nature. The lakeside forms a focal point
Subcontent5: ... with structures and characters arranged nearby.
SubcontentN: ... ### Shot Angle
### Lighting and Atmosphere 3/4 View: Offering an immersive perspective that showcases both the forest structures and
... lakeside, providing depth and dimensionality to the scene.
### Color Palette
...
### Layout F Appendix F: Modify By Instruction GPT
...
### Shot Angle You're a helpful assistant who aids artists in creating creative visual ideas based on given
... instructions and an original design idea. You will receive an instruction, a description
 of a visual design idea, and a creative score between 0 and 1. The instruction details
The amount of Subcontent is not fixed how the visual design idea be modified. The creative score indicates the creativity
 level of the design idea you provide, where 1 means highly diverse from the original
 design idea, and 0 means very similar to the original design idea. Your task is to
 generate 1 new design idea based on the instruction and the creative score provided. The
#Example new design should reflect the specified level of creativity relative to the original
INPUT: design idea.
Variety Score: 0.5
Original Design idea: # Guideline
### Theme - The design idea should include Art Style, Theme, Content, Lighting and Atmosphere, Color
Fantastical Forest Retreat Alongside a Serene Lakeside Palette, Layout and Shot Angle
### Art Style - You have to always follow the instructions provided by the artist.
Illustrative with painterly quality, emphasizing detail and smooth gradients - You need to balance relevance and creativity based on the creative score. For a low creative
### Content score, modify only the part specified in the instruction. For a high creative score,
- **Central Structures**: Whimsical, plant-pod-like buildings with grass-covered domes and introduce more diverse changes while still incorporating the instruction.
 intricate plant growth. Some are elevated on slender poles. - The output should be lower than 400 characters.
- **Lakeside Area**: A tranquil lake with clear blue waters reflecting the lush surroundings,
 with characters standing at its edge. # Output format
- **Hills and Background**: Gentle rolling hills, numerous trees, and distant mountains creating Your output must be in the format below:
 a picturesque, layered backdrop. ### Theme
- **Characters**: Fantasy attire-clad characters, including an adventurer holding a staff or ...
 weapon, interacting with nature. ### Art Style
- **Paths and Integrations**: Natural pathways winding through the forest, connecting the ...
 structures seamlessly to the environment. ### Content
### Lighting and Atmosphere Subcontent1: ...
Soft and inviting with smooth shadows, capturing a serene and harmonious ambiance. The lighting Subcontent2: ...
 emphasizes the natural vibrancy, enhancing the dreamlike feel. Subcontent3: ...
### Color Palette Subcontent4: ...
Vibrant and saturated greens for vegetation, blues for the sky and water, with accents of earthy Subcontent5: ...
 browns and soft yellows. The palette induces calmness and wonder. SubcontentN: ...
### Layout ### Lighting and Atmosphere
Organic and flowing with structures and pathways naturally embedded into the landscape, ...
 emphasizing harmony between architecture and nature. The lakeside forms a focal point ### Color Palette
 with structures and characters arranged nearby. ...
### Shot Angle ### Layout
3/4 View: Offering an immersive perspective that showcases both the forest structures and ...
 lakeside, providing depth and dimensionality to the scene. ### Shot Angle
Keyword: ...
Grass-Covered Domes
Description of the reference image: The amount of Subcontent is not fixed
The image shows a small, dome-shaped house made of stone. The exterior is composed of
 irregularly shaped stones, giving it a rustic and natural appearance. The house has a
 porch-like structure attached to the front, supported by stone pillars and covered by a # Example
 roof that also appears to be made of stone. The porch area has a lattice design on the INPUT:
 side and a bench with potted plants placed around it, adding to the cozy and welcoming Creative Score: 0.4
 atmosphere. Instructions:
The house features a slanted window on one side of the dome, with plants growing nearby. The I want the idea be more tropical
 surrounding landscape is a well-maintained garden with green grass, a variety of plants, Original Design Idea:
 and small trees. A curved, brick-paved pathway leads up to the entrance of the house. ### Theme
 The overall setting is tranquil and picturesque, with a blend of natural elements and Enchanted Fairy Village blending nature and fantastical architecture seamlessly.
 thoughtful landscaping. ### Art Style
 Painterly concept art with loose brushstrokes, rich textures, and an emphasis on mood and
OUTPUT: atmosphere.

---

CHI ’25, April 26–May 01, 2025, Yokohama, Japan Wang Lu Ponsa Chen Chen

### Content ### Art Style
Central Focus: A large, central treehouse structure that spirals upward, resembling a giant Painterly concept art with loose brushstrokes, rich textures, and an emphasis on vibrant
 twisted gourd intertwined with vines and flowers. It has multiple levels with balconies, tropical atmosphere.
 windows, and hanging lanterns. ### Content
Surrounding Structures: Smaller houses resembling fruits and vegetables (like pumpkins, melons, Central Focus: A large, central treehouse structure resembling a giant twisted coconut
 and berries) scattered around, each uniquely designed with natural materials like wood, intertwined with tropical vines and exotic flowers, featuring multiple levels with
 leaves, and vines. balconies, windows, and hanging lanterns.
Pathways and Bridges: Winding wooden pathways and rope bridges connecting the treehouses and Surrounding Structures: Smaller houses resembling tropical fruits (like pineapples, bananas, and
 ground-level homes, with small, glowing fairy lights hanging along the edges. coconuts) scattered around, each uniquely designed with natural materials like bamboo,
Characters: Fantastical inhabitants such as fairies, elves, and other mythical creatures in palm leaves, and vines.
 colorful, traditional attire. They are engaged in various activities like gardening, Pathways and Bridges: Winding wooden pathways and rope bridges connecting the treehouses and
 crafting, and playing musical instruments. ground-level homes, with small, glowing fairy lights hanging along the edges.
Nature Elements: Abundant greenery with tall, ancient trees, vibrant flowers, and a crystal- Characters: Fantastical inhabitants such as fairies, elves, and other mythical creatures in
 clear stream flowing through the village. Wildlife such as butterflies, birds, and small colorful, tropical-themed attire. They are engaged in various activities like gardening,
 woodland creatures add life to the scene. crafting, and playing musical instruments.
Mystical Features: Magical elements like floating lanterns, glowing mushrooms, and a hidden Nature Elements: Abundant tropical greenery with tall, ancient palm trees, vibrant exotic
 fairy circle made of luminescent stones. flowers, and a crystal-clear stream flowing through the village. Wildlife such as
### Lighting and Atmosphere butterflies, tropical birds, and small woodland creatures add life to the scene.
Magical and Ethereal: Soft, diffused lighting with a warm golden hue, creating a dreamlike Mystical Features: Magical elements like floating lanterns, glowing tropical mushrooms, and a
 atmosphere. Fairy lights and lanterns add a gentle glow, enhancing the mystical ambiance. hidden fairy circle made of luminescent stones.
 ### Lighting and Atmosphere
Dynamic Sky: A vast sky with a soft gradient from a pastel blue to a warm sunset orange, dotted Magical and Ethereal: Soft, diffused lighting with a warm golden hue, creating a dreamlike
 with a few fluffy clouds and faint, sparkling stars beginning to appear. atmosphere. Fairy lights and lanterns add a gentle glow, enhancing the mystical ambiance.
### Color Palette
Vibrant and Lush: Dominated by rich greens, warm browns, and earthy tones, accented with pops of Dynamic Sky: A vast sky with a soft gradient from a pastel blue to a warm sunset orange, dotted
 vibrant colors from flowers, fruits, and inhabitants' clothing. The sky adds pastel with a few fluffy clouds and faint, sparkling stars beginning to appear.
 blues and warm oranges. ### Color Palette
### Layout Vibrant and Lush: Dominated by rich greens, warm browns, and earthy tones, accented with pops of
Organic and Flowing: Structures are integrated into the natural landscape, with pathways and vibrant tropical colors from flowers, fruits, and inhabitants' clothing. The sky adds
 bridges meandering organically through the village. The central treehouse is the focal pastel blues and warm oranges.
 point, with other elements arranged naturally around it, creating a harmonious and ### Layout
 cohesive scene. Organic and Flowing: Structures are integrated into the natural landscape, with pathways and
### Shot Angle bridges meandering organically through the village. The central treehouse is the focal
Wide Panoramic View: Capturing the entire village from a slightly elevated perspective, point, with other elements arranged naturally around it, creating a harmonious and
 providing a comprehensive look at the intricate details of the architecture and the lush cohesive scene.
 , enchanting landscape. This angle showcases the depth and expansiveness of the scene, ### Shot Angle
 drawing the viewer into the magical world. Wide Panoramic View: Capturing the entire village from a slightly elevated perspective,
 providing a comprehensive look at the intricate details of the architecture and the lush
OUTPUT: , enchanting landscape. This angle showcases the depth and expansiveness of the scene,
### Theme drawing the viewer into the magical world.
Enchanted Tropical Fairy Village blending nature and fantastical architecture seamlessly.

---
