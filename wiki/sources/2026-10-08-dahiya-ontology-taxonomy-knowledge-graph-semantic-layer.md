---
type: source
kind: video
title: "Ontology vs Taxonomy vs Knowledge Graph vs Semantic Layer: What's the Difference?"
author: ["Aanchal Dahiya"]
publisher: "Aanchal Dahiya (YouTube channel); presenter Aanchal Dahiya"
url: "https://www.youtube.com/watch?v=DIRcJBbRRUo"
date_published: 2026-10-08
date_ingested: 2026-11-16
length: "~7:05 minutes (transcript ~55 lines; human-written track, 9 chapters)"
raw: "../../raw/videos/ontology-vs-taxonomy-vs-knowledge-graph-vs-semantic-layer-whats-the-difference.md"
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

## Linked entities and concepts

- **Entities:** [[Google]].
- **Concepts:** [[knowledge-graphs]], [[industrial-ai-agents]].
- **Dangling** (single-source mention, deferred): Aanchal Dahiya (channel and presenter), Tom Gruber, W3C, data.world.

## Source quality

Human-written captions. The video is slide-led; its diagrams and photos are not captured, and stills are deferred after the extraction run failed (Gemini 402). One presenter's synthesis, with its sources listed in the description (Gruber 1993, W3C OWL 2, Google's 2012 post, the data.world study). The benchmark is the only empirical claim: vendor-run, as the channel notes, unquantified here and not ingested. A vocabulary reference, not evidence.
