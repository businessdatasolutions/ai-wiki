---
type: source
kind: paper
title: "Automated Triaging and Transfer Learning of Incident Learning Safety Reports Using Large Language Representational Models"
author: ["Peter Beidler", "Mark Nguyen", "Kevin Lybarger", "Ola Holmberg", "Eric Ford", "John Kang"]
publisher: "arXiv (preprint, cs.CL)"
url: "https://arxiv.org/abs/2509.13706"
date_published: 2025-09-17
date_ingested: 2026-11-07
length: "16 pages (11 main text + 5 supplement), read in full; v1 is the only version"
raw: "../../raw/papers/2025-09-17-beidler-nguyen-incident-report-severity-triage-radiotherapy.md"
tags: [patient-safety, incident-reporting, incident-learning-systems, radiation-oncology, severity-triage, nlp, bluebert, svm, transfer-learning, external-validation, generalisability, alert-fatigue, human-in-the-loop, iaea-safron, university-of-washington, preprint]
relationships:
  - type: supports
    target: 2023-03-08-meg-lfpse-mussett-interview
    via: "machine triage of free-text patient-safety incident reports, because people can read only a fraction of them: the paper measures a severity screen at one department and on a multinational repository; the interview describes national plans for England's LFPSE"
    confidence: 0.65
  - type: supports
    target: 2026-04-30-ai-index-report-2026
    via: "evaluating clinical AI on real data: the AI Index finds only 5% of 500+ clinical AI studies use real clinical data; this paper trains and tests on real incident reports and reports what happens outside the training institution"
    confidence: 0.6
---

# Automated triaging and transfer learning of incident safety reports (Beidler, Nguyen et al., arXiv 2025)

## TL;DR

A preprint from the University of Washington radiation oncology department, with a co-author from the International Atomic Energy Agency (IAEA). It tests whether a language model can flag **high-severity incident reports** so that a human reviews them first. Five findings:

1. **In-house, the screen works.** On the department's own test set, a support vector machine (SVM) reaches **AUROC 0.82** and the clinical language model BlueBERT **0.81** (p. 2, p. 8).
2. **Outside the training data, it fails.** On reports from the IAEA's multinational SAFRON repository, the same models fall to **AUROC 0.42 (SVM)** and **0.56 (BlueBERT)** (p. 2, p. 8). An AUROC of 0.42 is worse than chance.
3. **A little local data repairs much of it.** BlueBERT fine-tuned first on the department's reports and then on SAFRON's training split reaches **AUROC 0.78** on the SAFRON test set (p. 2, p. 8). SAFRON has only **571 labelled reports**, against 7,094 in-house (p. 2).
4. **Comparable to individual staff.** On 59 curated in-house reports, the models score AUROC 0.85 (SVM), 0.76 (BlueBERT) and 0.74 (transfer model), against **0.81 for 26 human raters** (p. 9).
5. **The alert rate is a clinical choice.** At a 20% alert rate the transfer model catches 46% of high-severity SAFRON reports with 5 false alarms; at 50% it catches 79% with 27 false alarms (p. 8–9). The authors say each institution must set that rate with its clinicians (p. 11).

## Key data

| Model | Trained on | AUROC, in-house test set | AUROC, SAFRON test set |
| --- | --- | ---: | ---: |
| SVM (TF-IDF) | In-house | **0.82** | **0.42** |
| BlueBERT | In-house | 0.81 | **0.56** |
| BlueBERT-transfer | In-house, then SAFRON | 0.79 | **0.78** |
| Human raters (26 staff, 709 ratings) | n/a | 0.81 on 59 curated reports | n/a |

Sources: abstract (p. 2), results (p. 8–9), Figure 3 (p. 8).

| Dataset | Reports | Median length (words) | High-severity |
| --- | ---: | ---: | ---: |
| In-house (UW radiation oncology, 2012–2020) | 7,094 | 44 | 15.6% |
| SAFRON (IAEA, 50+ facilities worldwide) | 1,684, of which 571 labelled | 71 | 34.2% |

Source: Table 1 (p. 4) and text (p. 4–6).

**Transfer model on the SAFRON test set** (Tables 2–3, p. 9): at a 20% alert rate, sensitivity 0.46, specificity 0.93 (18 true and 5 false alarms); at 50%, sensitivity 0.79, specificity 0.64 (31 true and 27 false alarms). The test set holds 115 reports, 39 of them high-severity.

## Method and definitions

- **Task.** Binary classification: high- versus low-severity. In-house reports carry a near-miss risk index (NMRI) of 0–4 set by a weekly interdisciplinary panel; 3–4 counts as high (p. 5). SAFRON's six categories were mapped by a member of the department's safety committee: "minor" is low, everything else is high (p. 5–6).
- **Models.** An SVM on TF-IDF features, and BlueBERT (about 110 million parameters, pretrained on PubMed and MIMIC-III clinical notes) with a classification layer (p. 6–7). Reports were cut at 150 tokens. Each BlueBERT model was fine-tuned five times and the best run by F1 kept (p. 7).
- **Splits.** 70/15/15 for in-house data, 60/20/20 for SAFRON (p. 6). Test sets were used once, after development (p. 7).
- **Label quality.** Earlier work in the same department found only "fair" agreement between 28 raters on severity (Krippendorff's α 0.376, p. 3, p. 10). The authors name this, and nine years of staff and workflow change, as limits on performance (p. 10).
- **Funding:** none. **Conflicts:** none declared (p. 1).

## Scope and reliability

- **A preprint.** v1 (17 September 2025) is the only version on arXiv; there is no journal reference.
- **Small external test set.** The 0.78 rests on 115 SAFRON reports, 39 of them high-severity. No confidence intervals are given. "No significant difference" between in-house models (p. 8) is stated without a named test.
- **"The other dataset" is not one institution.** SAFRON pools voluntary reports from 50+ facilities in several countries, curated by the IAEA (p. 4, p. 6). The external test is one department against a multinational registry, with a severity mapping made by the authors.
- **Two severity scales.** The in-house NMRI and SAFRON's categories weigh actual harm, potential harm and likelihood differently, so the same text can earn different labels at two sites (p. 4). Part of the drop is a disagreement about labels, not only about language.
- **Supplementary checks point both ways.** On two tiny extra sets (13 RO-ILS case reports, 11 artificial NMRI examples) the in-house BlueBERT did best, and the transfer model did worst on RO-ILS (Table S4, p. 16).

## Dynamic-capabilities reading

Not tagged. The paper is a methods study of one triage model; the Warner & Wäger lens would be forced.

## How it connects

- [[2023-03-08-meg-lfpse-mussett-interview|Mussett on LFPSE]] describes the same problem at national scale: England's service receives over 2.6 million records a year and reads about 10,000 by hand, and expects machine learning to sort which records need reading. This paper measures such a screen at one department and on a multinational repository.
- [[2026-04-30-ai-index-report-2026|AI Index 2026]] reports that only 5% of 500+ clinical AI studies use real clinical data. This study uses real incident reports and tests outside its training institution.
- [[agent-oversight-and-delegation]] — the model is a screen that ranks reports for a human reviewer, and the alert rate sets how much the human sees. The authors leave that threshold to each institution's clinicians.
- [[responsible-ai]] — external validity: a model validated in one institution can perform below chance in another until it is retrained on local data.
- [[ai-in-health-care]]: the concept page that sets the health-care sources in this wiki side by side.

## What was actually ingested

The full v1 PDF (16 pages), including the supplement. Figures 1–3 and Figure S1 are images; their values were read from the text, which repeats every AUROC in the figures. Tables 1–3 and S1–S4 were read as text.

## Linked entities and concepts

- [[agent-oversight-and-delegation]], [[responsible-ai]] — concepts.

**Dangling** (single-source mention, deferred): Peter Beidler, Mark Nguyen, Kevin Lybarger, Ola Holmberg, Eric Ford, John Kang (authors); University of Washington School of Medicine; International Atomic Energy Agency (SAFRON); BlueBERT (model, Peng et al. 2019).
