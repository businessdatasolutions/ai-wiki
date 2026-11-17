---
video_id: DIRcJBbRRUo
url: https://www.youtube.com/watch?v=DIRcJBbRRUo
transcript: raw/videos/ontology-vs-taxonomy-vs-knowledge-graph-vs-semantic-layer-whats-the-difference.md
stills_dir: raw/images/ontology-vs-taxonomy-vs-knowledge-graph-vs-semantic-layer-whats-the-difference
stills_count: 24
extractor:
  method: hand-picked (no Gemini call)
  reason: Gemini API returned 402 (prepayment credits depleted)
  sampling: 106 frames at 360p, one every 4 s, consecutive repeats merged (160x90 grayscale MAD < 1.5) into 82 tiles, read as 5x6 contact sheets
  frames: yt-dlp stream URL (<=1080p) seeked with ffmpeg
acquired: '2026-11-17'
---

# Stills manifest (hand-picked)

Each still was chosen from the contact sheets and then read at full resolution. Unlike a Gemini manifest, the readings below were made by viewing the pixels; the source page carries the verified transcriptions of the published stills.

The video is an animated explainer: one diagram per term, built up element by element while the presenter talks, with her camera inset in some shots. Each build was cut at its fully built state; earlier build stages were not saved. Most diagrams draw what the narration says; the published ones add worked data the narration does not give (example rows, IDs, numbers, a change log, the five per-term questions).

## 01 · 0:08 · Five terms
- File: `01-00m08-five-terms.png` · [0:08](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=8s)
- "Next steps: align on the ontology." with the four other terms as chips (taxonomy, knowledge graph, semantic model, semantic layer). **Not published:** title sequence.

## 02 · 0:32 · Ontology, one line
- File: `02-00m32-ontology-definition-card.png` · [0:32](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=32s)
- "ONTOLOGY: the kinds of things + the rules about how they relate". **Not published:** narrated word for word.

## 03 · 0:56 · Soccer field and the goal rule
- File: `03-00m56-soccer-field-ifab-rule.png` · [0:56](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=56s)
- Field diagram with photo chips (goalkeeper is a player, referee, goal) and the IFAB quote "…the whole of the ball passes over the goal line, between the goalposts and under the crossbar"; photos credited to Wikimedia Commons. **Not published:** narrated; superseded by still 04.

## 04 · 1:04 · Rulebook and scoreboard
- File: `04-01m04-rulebook-and-scoreboard.png` · [1:04](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=64s)
- Rulebook = ontology ("Laws of the Game", IFAB: what exists, how they relate, rules players per team ≤ 11, exactly 1 goalkeeper; "in general") beside scoreboard = knowledge graph (1-0, minute 32, "32' player scored"; "one match"). Cut at 1:22. **Not published:** the narration gives every element.

## 05 · 1:36 · The university ontology, fully built
- File: `05-01m36-university-ontology.png` · [1:36](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=96s)
- Class diagram (Person, Employee, Student, Instructor, Graduate TA, Course, Section, Department) with is-a, enrolls-in, teaches and offering-of edges, the five-rule panel and the Calculus 1→2→3 chain with the implied, unwritten link. Builds from 1:36 to 2:52; cut at 2:53. **Published.**

## 06 · 2:36 · The reasoner derives a fact nobody wrote
- File: `06-02m36-reasoner-derives-unwritten-fact.png` · [2:36](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=156s)
- Close-up of the calculus chain: "[not written]", "implied", "reasoner: derives facts nobody wrote down". **Not published:** narrated; the chain is in still 05.

## 07 · 2:44 · The reasoner flags a record that breaks a rule
- File: `07-02m44-reasoner-flags-rule-break.png` · [2:44](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=164s)
- Rule panel plus "records the reasoner checks": Maya is_a Graduate TA; Maya enrolled_in Section 2; Maya teaches Section 2; "breaks the rule above". Cut at 2:50. **Published.**

## 08 · 3:12 · Taxonomy tree inside the ontology network
- File: `08-03m12-taxonomy-vs-ontology.png` · [3:12](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=192s)
- "TREE taxonomy" vs "NETWORK + RULES ontology": is-a edges to Person, plus teaches, enrolls in, offering of and offered by (Section → Course → Department), with an edge-type legend. Cut at 3:34. **Published.**

## 09 · 3:36 · Knowledge graph triples
- File: `09-03m36-knowledge-graph-triples.png` · [3:36](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=216s)
- Five subject → relation → object triples about Student 1042/1043, Instructor 17, Sections 1 and 2 and Statistics, drawn as a graph under the ontology classes. Cut at 3:58. **Published.**

## 10 · 4:00 · Google, 2012
- File: `10-04m00-google-2012-things-not-strings.png` · [4:00](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=240s)
- "Outside source: Google, 2012. Introducing the Knowledge Graph. 'things, not strings'". **Not published:** a citation card; the narration paraphrases the slogan.

## 11 · 4:12 · What is allowed vs what is true here
- File: `11-04m12-ontology-validates-graph.png` · [4:12](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=252s)
- Ontology band (faded) validating the graph ("what is true here", each edge ticked) and a nonsense triple "Statistics enrolled_in Maya" marked "no check". Cut at 4:25, after a cut at 4:22 showed the triple before its label. **Published.**

## 12 · 4:32 · One metric, two counts
- File: `12-04m32-semantic-model-two-counts.png` · [4:32](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=272s)
- Enrollments table (four rows), the "Enrolled students" definition `COUNT DISTINCT student_id WHERE status = 'enrolled' AND term = current`, and two ad hoc queries returning 1,240 and 1,198. Cut at 4:42. **Published.**

## 13 · 4:44 · Semantic layer to a dashboard
- File: `13-04m44-semantic-layer-dashboard.png` · [4:44](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=284s)
- "Enrolled students 1,240, one number for everyone" served to a Dashboard showing 1,240. **Not published:** narrated; the number is in still 12.

## 14 · 4:52 · The question each term answers
- File: `14-04m52-five-questions.png` · [4:52](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=292s)
- Two question cards (metrics vs kinds of things) and one question under each of the five terms. Builds from 4:52 to 5:12; cut at 5:14. **Published.**

## 15 · 5:16 · The ontology informs the semantic model
- File: `15-05m16-ontology-informs-semantic-model.png` · [5:16](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=316s)
- Student –enrolls in→ Section mapped onto the student_id and section_id columns; "1,240, one definition, one number". **Not published:** the narration states the link; the table and number are in still 12.

## 16 · 5:28 · The LLM and the same person in two systems
- File: `16-05m28-llm-same-person.png` · [5:28](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=328s)
- LLM beside an abbreviated table (enr_tbl: stu_id, sec_id, st, trm); inside an ontology box, student_system S-1042 enrolled and payroll E-7731 TA joined as "same person". Cut at 5:50. **Published.**

## 17 · 5:52 · The 2023 benchmark
- File: `17-05m52-2023-benchmark.png` · [5:52](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=352s)
- "2023 benchmark: database questions answered correctly — without / through a knowledge graph", tagged "one vendor study". No figures or bars on the slide either. **Not published:** no content beyond the narration.

## 18 · 6:04 · A governed definition with a change log
- File: `18-06m04-student-definition-change-log.png` · [6:04](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=364s)
- "Student" card: definition, owner, version 4 changed 2026-10-06, and a four-entry change log; tag "data governance work". Builds from version 3 (6:04) to 4 (6:12); cut at 6:14. **Published.**

## 19 · 6:20 · Failure mode: the whole enterprise
- File: `19-06m20-failure-whole-enterprise.png` · [6:20](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=380s)
- The university ontology lost in a sprawling enterprise graph; label "whole enterprise". **Not published:** narrated.

## 20 · 6:24 · Start with one question
- File: `20-06m24-failure-one-question-first.png` · [6:24](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=384s)
- One path highlighted (Student → Section → Course → Department): "one question the business cannot answer today". **Not published:** narrated.

## 21 · 6:28 · Failure mode: label only
- File: `21-06m28-failure-label-only.png` · [6:28](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=388s)
- The is-a tree stamped "Ontology" with "relationships: none, rules: none". **Not published:** narrated.

## 22 · 6:32 · Failure mode: never connected
- File: `22-06m32-failure-never-connected.png` · [6:32](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=392s)
- The ontology above the enrollments table with its links to the columns crossed out. **Not published:** narrated.

## 23 · 6:40 · Failure mode: no owner
- File: `23-06m40-failure-no-owner.png` · [6:40](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=400s)
- "Student: Person admitted to a program", owner field empty, ≠ business glossary "student = enrolled this term"; the four failure labels below. Cut at 6:46. **Published.**

## 24 · 6:48 · The whole picture
- File: `24-06m48-whole-picture.png` · [6:48](https://www.youtube.com/watch?v=DIRcJBbRRUo&t=408s)
- Three bands: ontology (classes), knowledge graph (Student 1042 → Instructor 17 → Section 2 → Statistics), semantic model and layer (students, enrollments → enrolled_students), above the five term chips. **Not published:** the closing line of the narration says it.
