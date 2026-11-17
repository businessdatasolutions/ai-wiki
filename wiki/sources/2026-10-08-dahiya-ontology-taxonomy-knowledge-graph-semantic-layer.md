---
type: source
kind: video
title: "Ontology vs Taxonomy vs Knowledge Graph vs Semantic Layer: What's the Difference?"
author: ["Aanchal Dahiya"]
publisher: "Aanchal Dahiya (YouTube channel); presenter Aanchal Dahiya"
url: "https://www.youtube.com/watch?v=DIRcJBbRRUo"
date_published: 2026-10-08
date_ingested: 2026-11-16
length: "~7:05 minutes (transcript ~55 lines + 10 stills; human-written track, 9 chapters)"
raw: "../../raw/videos/ontology-vs-taxonomy-vs-knowledge-graph-vs-semantic-layer-whats-the-difference.md"
stills: "../../raw/videos/ontology-vs-taxonomy-vs-knowledge-graph-vs-semantic-layer-whats-the-difference.stills.md"
tags: [ontology, taxonomy, knowledge-graph, semantic-model, semantic-layer, owl, reasoner, tom-gruber, data-governance, data-modeling, enterprise-data, vocabulary, explainer, education]
relationships:
  - type: supports
    target: 2026-02-01-manditereza-ontology-driven-industrial-ai
    via: "both separate an ontology from the knowledge graph that holds its instances: Manditereza stacks a semantic model (shared organisational vocabulary), domain ontologies and a knowledge graph for industrial agents; Dahiya defines five terms on a university example, with the semantic model holding business definitions and metric calculations tied to tables"
    confidence: 0.7
  - type: supports
    target: 2026-07-24-turnbaugh-motherduck-context-layers-explained
    via: "both define the semantic layer and describe an LLM guessing when business definitions are missing: Turnbaugh puts schema, joins and annotations in the semantic layer and business-term definitions in a separate context layer; Dahiya puts business definitions and metric calculations in the semantic model, which the semantic layer serves to dashboards and agents"
    confidence: 0.7
  - type: supports
    target: 2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings
    via: "both address facts a knowledge graph does not state: Dahiya describes an OWL reasoner deriving them from written rules (a transitive prerequisite), Leskovec trains embeddings to predict missing (head, relation, tail) triples"
    confidence: 0.6
---

# Dahiya: ontology, taxonomy, knowledge graph, semantic model, semantic layer

> "Ontology" shows up in meetings next to taxonomy, knowledge graph, semantic model and semantic layer, and people often use all five as if they were one idea. They're related, but each answers its own question, and mixing them up is how teams end up buying or building the wrong thing.
>
> In this video you'll learn what an ontology is and how it differs from a taxonomy, a knowledge graph, a semantic model and a semantic layer, with a worked example you can follow. You'll see what each one is for, how they work together, why it matters now that AI and LLMs need to understand your business data, and the common mistakes teams make when they build one.
>
> The university data is an illustrative example. The 2023 benchmark is a single vendor study, not independent research. This is general education.
>
> *— Channel description, Aanchal Dahiya*

## TL;DR

A seven-minute explainer by Aanchal Dahiya on her own channel. It defines five data-architecture terms that *"tend to arrive in a meeting with no explanation attached"*, first with a soccer analogy, then on a worked university example. **Human-written caption track**; no corrections were needed in quotation.

What it adds to the wiki:

1. **All five terms side by side**, each defined on the same example (table below). No earlier source in the wiki includes the taxonomy in the set.
2. **The rulebook/scoreboard split**: *"An ontology is the rulebook and a knowledge graph is closer to the scoreboard"* (1:18).
3. **What the formal side is for**: OWL reasoners derive facts nobody wrote down and flag records that break a rule.
4. **Four ways an ontology goes wrong**, and the claim that maintaining one is data-governance work.
5. **A pointer to evidence the wiki does not hold**: a 2023 benchmark by the data-catalog vendor data.world (Sequeda, Allemang, Jacob; [arXiv:2311.07509](https://arxiv.org/abs/2311.07509)), cited without figures.

General education; the example is illustrative by the channel's own statement.

## The five terms

| Term | Definition in the video | University example |
| --- | --- | --- |
| **Ontology** | *"A written, agreed description of the things that exist in some area and the relationships between them"* (3:03): classes, relationships, rules | Classes person, student, instructor, course, section; *an instructor teaches a section*; prerequisite is transitive |
| **Taxonomy** | *"A hierarchy of categories where each thing falls under a broader one"*, capturing only the *is-a-kind-of* relationship (3:11) | person → student → graduate student |
| **Knowledge graph** | Facts as a network, each *"a small sentence with a subject, a relationship, and an object"* (3:41) | *"Maya enrolled in section two of statistics"* |
| **Semantic model** | *"The set of business definitions tied to your tables"* (4:24) | What counts as an enrolled student; how headcount is calculated |
| **Semantic layer** | *"The service that serves those definitions to dashboards and increasingly to AI agents"* (4:43) | n/a |

Semantic models and layers are *"mainly about metrics and the data underneath them"*; an ontology answers *"what a student is, how that relates to an employee, and what follows from the rules"* (4:51–5:08). Often *"the ontology [informs] the entities and relationships in the semantic model."*

## Rulebook, scoreboard, reasoner

*"The ontology says what kinds of things and links are allowed and the knowledge graph holds the particular students and sections. A graph can be built without a formal ontology, but then nothing checks whether it makes sense"* (4:08). [[Google]] popularised the term *knowledge graph* in 2012.

OWL, the W3C's ontology language, lets a reasoner *"work out facts that nobody stated from the rules that were written down"* (2:30) and *"flag a record that breaks the rule."* Her example: with prerequisite transitive, calculus 1 is required for calculus 3 *"without anyone having to write that third fact down."* [[2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings|Leskovec's CS224W lecture]] treats missing facts as a learning task, predicting a triple's tail from its head and relation. She cites Tom Gruber's 1993 definition: *"an explicit specification of a conceptualization."*

## Why it matters for AI

An LLM *"can guess from the column names that a table of enrollment links students to sections, but it's guessing"*, and may not know a teaching assistant in the student and payroll systems is one person. *"An ontology gives it the relationships and constraints written down"* (5:47). The data.world benchmark found GPT-4 *"answered far more database questions correctly when it worked through a knowledge graph"* (5:51); no numbers are given.

Three wiki sources use the same terms. [[2026-07-24-turnbaugh-motherduck-context-layers-explained|Turnbaugh (MotherDuck)]] also describes the model guessing, and splits a semantic layer (schema, joins, annotations) from a context layer (business-term definitions); Dahiya puts business definitions in the semantic model. [[2026-02-01-manditereza-ontology-driven-industrial-ai|Manditereza (HiveMQ)]] stacks a semantic model, domain ontologies and a knowledge graph for industrial agents. [[2026-08-10-banholzer-laberge-mckinsey-how-to-maximize-competitive-advantage|Banholzer (McKinsey)]] names *"a semantic layer, or what us and others have called an ontology"* together.

## Keeping an ontology useful

*"Somebody has to own the definition of student, decide whether a new kind of thing belongs in the model, and record when the meaning changed, which is data governance work and not only modeling work"* (6:02). The failure modes:

1. Modelling the whole enterprise at once, instead of starting *"with one question the business cannot answer today."*
2. Calling a category tree an ontology: *"the label without the relationships and rules."*
3. Never connecting it to the tables, so *"no query or agent ever uses it."*
4. Nobody owns it, so it *"drifts away from how the business uses its words."*

## Visual canon

Ten stills, hand-picked from contact sheets because the Gemini scan failed. Every term gets an animated diagram built up while she speaks; the ones below are cut at their fully built state and chosen for the worked data they add: example rows, identifiers, two disagreeing counts, a change log, one question per term.

### 1 · The university ontology, fully built

![[assets/2026-10-08-dahiya-ontology-taxonomy-knowledge-graph-semantic-layer/05-01m36-university-ontology.webp|The university ontology with its rules]]

*Still at [1:36](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=96s) from Aanchal Dahiya, "Ontology vs Taxonomy vs Knowledge Graph vs Semantic Layer: What's the Difference?".*

Classes and edges: Employee, Student and Instructor *is a* Person; Graduate TA *is a* Employee and *is a* Student; Student *enrolls in* Section; Instructor *teaches* Section; Section *offering of* Course, marked *exactly 1*; Department stands unconnected. **Rules** (marked *illustrative*):

- `GraduateTA is_a Student AND Employee`
- `Section offering_of EXACTLY 1 Course`
- `prerequisite_of is TRANSITIVE`
- `Calculus 1 prerequisite_of Calculus 3` (dashed, in the purple of the implied link)
- `enrolled student is NOT instructor of same section` (red)

Below: Calculus 1 *prerequisite of* Calculus 2 *prerequisite of* Calculus 3, with a dashed arc from Calculus 1 to Calculus 3 labelled *implied* and *[not written]*.

*Still vs. transcript:* the narration introduces classes, relationships and rules one at a time between 1:37 and 2:50. The diagram holds them in one view, adds Employee as a class of its own (the narration's class list is person, student, instructor, course and section), and enters the derived Calculus 1 → 3 fact in the rule panel, styled apart from the written rules.

### 2 · A record the reasoner rejects

![[assets/2026-10-08-dahiya-ontology-taxonomy-knowledge-graph-semantic-layer/07-02m44-reasoner-flags-rule-break.webp|The reasoner flags a record that breaks a rule]]

*Still at [2:44](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=164s) from Aanchal Dahiya, "Ontology vs Taxonomy vs Knowledge Graph vs Semantic Layer: What's the Difference?".*

The rule panel of still 1 above a table, **records the reasoner checks** (*illustrative*):

| subject | relation | object |
| --- | --- | --- |
| Maya | is_a | Graduate TA |
| Maya | enrolled_in | Section 2 |
| Maya | teaches | Section 2 |

The last two rows are red, labelled **breaks the rule above**: the red rule, *enrolled student is NOT instructor of same section*.

*Still vs. transcript:* the narration states the rule and says a reasoner *"can flag a record that breaks the rule"*; the slide supplies the record, a graduate TA enrolled in the same section she teaches.

### 3 · The taxonomy tree inside the ontology network

![[assets/2026-10-08-dahiya-ontology-taxonomy-knowledge-graph-semantic-layer/08-03m12-taxonomy-vs-ontology.webp|Tree taxonomy versus network and rules ontology]]

*Still at [3:12](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=192s) from Aanchal Dahiya, "Ontology vs Taxonomy vs Knowledge Graph vs Semantic Layer: What's the Difference?".*

Header chips: **TREE** *taxonomy* (greyed) and **NETWORK + RULES** *ontology* (active). Blue *is a* edges: Student, Instructor and Employee → Person; Graduate TA → Student and → Employee. Grey edges: Student *enrolls in* Section; Instructor *teaches* Section; Section *offering of* Course; Course *offered by* Department. Legend, *edge types*: is a · teaches · enrolls in · offering of · offered by · rules.

*Still vs. transcript:* the narration's taxonomy example is one chain (person → student → graduate student). The diagram draws the *is a* edges as the hierarchy inside the larger network, with Graduate TA under both Student and Employee, and adds *offered by* from Course to Department, a relationship the narration does not name.

### 4 · Facts as triples and as a graph

![[assets/2026-10-08-dahiya-ontology-taxonomy-knowledge-graph-semantic-layer/09-03m36-knowledge-graph-triples.webp|Knowledge graph triples about students and sections]]

*Still at [3:36](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=216s) from Aanchal Dahiya, "Ontology vs Taxonomy vs Knowledge Graph vs Semantic Layer: What's the Difference?".*

**knowledge graph**, triples (*illustrative*):

- Student 1042 → enrolled_in → Section 2
- Instructor 17 → teaches → Section 2
- Section 2 → offering_of → Statistics
- Student 1043 → enrolled_in → Section 2
- Section 1 → offering_of → Statistics

Right: the same facts as a graph, each instance linked by a dotted arrow up to its class (Student, Instructor, Section, Course).

*Still vs. transcript:* the narration gives one fact (*"Maya enrolled in section two of statistics"*); the slide gives five, and ties each instance to its ontology class, the link the narration then describes in words.

### 5 · Without the ontology, nothing checks the graph

![[assets/2026-10-08-dahiya-ontology-taxonomy-knowledge-graph-semantic-layer/11-04m12-ontology-validates-graph.webp|What is allowed versus what is true here]]

*Still at [4:12](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=252s) from Aanchal Dahiya, "Ontology vs Taxonomy vs Knowledge Graph vs Semantic Layer: What's the Difference?".*

Top band, faded and dashed in the build's final state: Student, Instructor, Section, Course, Department, with *validates* arrows down to a pink band, **what is true here**: Student 1042 *enrolled in* Section 2, Instructor 17 *teaches* Section 2, Section 2 *offering of* Statistics, each edge ticked. Outside the band: **Statistics → enrolled_in → Maya**, labelled **no check**.

*Still vs. transcript:* the narration says *"a graph can be built without a formal ontology, but then nothing checks whether it makes sense"*; the slide's example of such a fact is a course enrolled in a student.

### 6 · One metric, two counts

![[assets/2026-10-08-dahiya-ontology-taxonomy-knowledge-graph-semantic-layer/12-04m32-semantic-model-two-counts.webp|Semantic model with two ad hoc counts]]

*Still at [4:32](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=272s) from Aanchal Dahiya, "Ontology vs Taxonomy vs Knowledge Graph vs Semantic Layer: What's the Difference?".*

**semantic model**. Table `enrollments` (*illustrative*):

| student_id | section_id | status | term |
| --- | --- | --- | --- |
| 1042 | 2 | enrolled | Fall |
| 1043 | 2 | enrolled | Fall |
| 1043 | 1 | dropped | Fall |
| 1051 | 2 | waitlist | Fall |

The student_id, status and term columns feed **Enrolled students**: `COUNT DISTINCT student_id WHERE status = 'enrolled' AND term = current`. On either side, *ad hoc query 1*: **1,240**; *ad hoc query 2*: **1,198** (both *illustrative*).

*Still vs. transcript:* the narration says a semantic model fixes *"precisely how the headcount is calculated so everyone who asks get the same number"*. The slide shows the problem, two ad hoc queries that disagree (1,240 and 1,198), and the definition that settles it. Its four rows include a dropped and a waitlisted enrolment.

### 7 · The question each term answers

![[assets/2026-10-08-dahiya-ontology-taxonomy-knowledge-graph-semantic-layer/14-04m52-five-questions.webp|The question each of the five terms answers]]

*Still at [4:52](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=292s) from Aanchal Dahiya, "Ontology vs Taxonomy vs Knowledge Graph vs Semantic Layer: What's the Difference?".*

Two cards: **How many students enrolled, calculated which way?** (tags: *metrics*, *the data underneath*) and **What is a student, how does it relate to an employee, what follows** (tags: *kinds of things*, *how they connect*). Below, one question per term:

| Term | Question |
| --- | --- |
| ontology | What kinds of things exist, and how do they connect? |
| taxonomy | What is a kind of what? |
| knowledge graph | What is true about the particular things? |
| semantic model | What do the business numbers mean? |
| semantic layer | Who gets those numbers, and how? |

*Still vs. transcript:* the narration says each term *"answers its own question"* but states only the two on the cards; the slide gives one question for each of the five terms.

### 8 · The same person in two systems

![[assets/2026-10-08-dahiya-ontology-taxonomy-knowledge-graph-semantic-layer/16-05m28-llm-same-person.webp|An LLM, abbreviated columns and one person in two systems]]

*Still at [5:28](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=328s) from Aanchal Dahiya, "Ontology vs Taxonomy vs Knowledge Graph vs Semantic Layer: What's the Difference?".*

**LLM**, *"an AI system trained on huge amounts of text"*, linked to tables (*illustrative*): `enr_tbl` with columns `stu_id`, `sec_id`, `st`, `trm`; and inside a box labelled **ontology**, `student_system` (stu_id `S-1042`, status `enrolled`) and `payroll` (emp_id `E-7731`, job `TA`), joined by a dashed bracket: **same person**.

*Still vs. transcript:* the narration says the model guesses from column names and may miss that a TA appears in both systems. The slide shows the abbreviated column names it would be guessing from, and two unrelated identifiers (S-1042, E-7731) for one person.

### 9 · A definition with an owner and a change log

![[assets/2026-10-08-dahiya-ontology-taxonomy-knowledge-graph-semantic-layer/18-06m04-student-definition-change-log.webp|The Student definition with owner and change log]]

*Still at [6:04](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=364s) from Aanchal Dahiya, "Ontology vs Taxonomy vs Knowledge Graph vs Semantic Layer: What's the Difference?".*

**Student** (*illustrative*): definition *Person admitted to a program*; owner *Registrar data owner*; version **4**; changed on **2026-10-06**. Change log:

| Version | Date | Change |
| --- | --- | --- |
| v1 | 2024-09-02 | defined |
| v2 | 2025-01-20 | owner assigned |
| v3 | 2026-03-14 | scope widened |
| v4 | 2026-10-06 | meaning changed |

Tag: **data governance work**.

*Still vs. transcript:* the narration lists the duties (own the definition, decide what belongs, record when the meaning changed); the slide shows them as one governed record with a named owner, a version number and a dated log.

### 10 · Nobody owns it, so the meaning drifts

![[assets/2026-10-08-dahiya-ontology-taxonomy-knowledge-graph-semantic-layer/23-06m40-failure-no-owner.webp|No owner, so the ontology and the glossary disagree]]

*Still at [6:40](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=400s) from Aanchal Dahiya, "Ontology vs Taxonomy vs Knowledge Graph vs Semantic Layer: What's the Difference?".*

**Student** (*illustrative*): definition *Person admitted to a program*; owner field empty (red, dashed). **≠** **business glossary** (*illustrative*): `student = enrolled this term`. Below, the four failure modes: whole enterprise · label only · never connected · no owner.

*Still vs. transcript:* the narration says an unowned ontology *"drifts away from how the business uses its words"*; the slide shows a drift: the ontology defines a student as admitted to a program, the business glossary as enrolled this term.

## Linked entities and concepts

- **Entities:** [[Google]].
- **Concepts:** [[knowledge-graphs]], [[industrial-ai-agents]].
- **Dangling** (single-source mention, deferred): Aanchal Dahiya (channel and presenter), Tom Gruber, W3C, data.world.

## Source quality

Human-written captions. The video is slide-led: an animated diagram for each term, plus photos in the soccer section. The Gemini stills scan failed (402), so 10 stills were hand-picked from contact sheets (82 tiles, one sample every 4 s; 24 frames cut at full resolution; see [§Visual canon](#visual-canon)). Most diagrams draw what the narration says; the published ones add worked data it does not give. One presenter's synthesis, with its sources listed in the description (Gruber 1993, W3C OWL 2, Google's 2012 post, the data.world study). The benchmark is the only empirical claim: vendor-run, as the channel notes, unquantified here and not ingested; its slide is tagged *"one vendor study"* and shows no figures either. A vocabulary reference, not evidence.
