---
type: concept
aliases: ["AI in health care", "AI in healthcare", "health-care AI", "hospital AI adoption", "clinical AI"]
tags: [health-care, hospitals, clinical-ai, hospital-ai-adoption, pilot-to-scale, ambient-documentation, patient-safety, incident-reporting, ai-governance, netherlands]
confidence: 0.85
last_confirmed: "2026-11-07"
accessed_at: "2026-11-07"
source_count: 17
relationships:
  - type: instance-of
    target: enterprise-ai-adoption
    via: "the adoption pattern of the wider economy (broad use, thin scale) measured in one sector"
  - type: uses
    target: responsible-ai
    via: "AI policy, AI boards, model evaluation and high-risk classification under the EU AI Act"
quality_score: 1
---

# AI in health care

How hospitals, health systems and clinicians adopt AI, and how far that adoption goes. The sector repeats the pattern of [[enterprise-ai-adoption]] in sharper form: almost every organisation uses some AI, few use it at scale, and the measured impact is still small. Most of the evidence is self-reported by executives or IT leads, which the sources themselves flag.

This page was created on 2026-11-07, when an ingest of AI-maturity surveys brought in twelve health-care sources. Before that, four sources treated the sector at their core.

## Breadth against depth

| Population | Breadth | Depth | Source |
| --- | --- | --- | --- |
| 52 Dutch hospitals (2026) | 90% use generative AI | 8% apply AI "op grote schaal" (at large scale), 0% at very large scale; of 18 applications per hospital, 1 is scaling | [[2026-03-16-mxi-ai-monitor-ziekenhuizen-2026\|M&I AI Monitor Ziekenhuizen 2026]] |
| 180 health-system executives, six countries incl. NL (2025) | ~30% use GenAI at scale in some areas | 2% have AI across the whole organisation; 3% report significant ROI | [[2025-12-11-deloitte-2026-global-health-care-outlook\|Deloitte 2026 Outlook]] |
| 43 US health systems (2024) | Ambient notes: 60% deploy at least in part | 14% deploy fully; fall-risk prediction 36% any, 19% full | [[2025-05-05-poon-jamia-health-system-ai-adoption\|Poon et al., JAMIA 2025]] |
| US non-federal acute care hospitals (2024) | 71% use predictive AI in the EHR | 71% check all or most models for accuracy, 57% for bias | [[2025-09-17-astp-hospital-predictive-ai\|ASTP data brief]] |
| 408 respondents, payers, pharma, providers | — | ~30% of completed proofs of concept reach production (providers 35%) | [[2025-04-15-bessemer-healthcare-ai-adoption-index\|Bessemer, AWS and Bain]] |
| 60+ US health-system IT leaders (2026) | 42% deploy AI across several use cases | 4% have scaled AI with measurable outcomes | [[2026-04-09-qventus-cio-report-2026\|Qventus CIO report]] (vendor) |
| US physicians (2026) | 81% use AI in their practice | — | [[2026-03-12-ama-physicians-ai-survey\|AMA survey]] (secondary coverage only) |
| Dutch doctors and nurses (2025) | 53% of doctors, 41% of nurses use at least one AI application | — | [[2026-03-09-rivm-monitor-digitale-zorg-2025\|RIVM Monitor Digitale Zorg 2025]] |
| 50 WHO European member states (2024–25) | — | 4 of 50 (8%) have a health-specific national AI strategy | [[2025-11-19-who-europe-ai-health-systems-readiness\|WHO/Europe]] |

The units differ by row: hospitals, executives, health systems, proofs of concept, physicians, countries. The rows share a direction, not a scale.

## Where AI is used

- **Administration first.** Administration and billing is the most common AI process in Dutch hospitals (80%, M&I). [[2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals|Luminai]] builds agents for US hospital back offices, starting from referral faxes. US hospitals' predictive AI for billing rose from 36% to 61% in one year (ASTP).
- **Documentation and voice.** Speech-driven or ambient reporting is the clearest case of start-but-not-finish: 69% of Dutch hospitals have started, while on average 21% of the intended clinicians use it actively (M&I). In the US, all 43 surveyed systems at least pilot ambient notes and 14% deploy them fully (Poon). [[2026-10-20-parikh-google-cloud-hippocratic-ai-voice-agents-healthcare|Hippocratic AI]] sells voice agents for routine patient calls.
- **Imaging.** Radiology holds the most important implementations in Dutch hospitals (41%, M&I). [[2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care|Peron (Philips)]] recalls that the predicted displacement of radiologists did not happen.
- **Patients ahead of institutions.** [[2026-07-14-keneally-bcg-so-what-llm-or-md-patient-journey|Keneally (BCG)]] argues that patients already use LLMs as the first step in care, and that health systems should shape this rather than block it.
- **Agents.** 0% of Dutch hospitals are scaling AI agents; 48% are exploring (M&I).

## Evidence and realised impact

- **Expected impact outruns realised impact.** On the M&I monitor's first question about realised impact over three years, 55% report a positive effect on staff experience, but for most quintuple-aim goals "neutral" is the most common answer, and 47% rate the effect on care costs as negative.
- **Thin clinical evidence.** Of 500+ clinical AI studies, 5% use real clinical data ([[2026-04-30-ai-index-report-2026|AI Index 2026]], citing the ARISE Network).
- **Surveys overstate.** The [[2025-07-15-european-commission-ai-deployment-healthcare-final-report|European Commission study]] warns that *"surveys may lead to overly optimistic estimations of AI deployment in healthcare"*: of 46 EU clinician respondents, 29 (63%) claimed AI use and 20 (43%) gave evidence of actual use.

## Quality and patient safety: not yet measured

No survey from 2025–2026 found in this ingest measures how many hospitals use AI on patient-safety incident reports. In the M&I monitor, quality and patient safety are not a domain: quality appears only as a driver (88% of hospitals), and the agent use case for "meldingen" concerns e-mails and medical-technology malfunctions, not incident reports.

The research that exists shows why local data matter. A severity-triage model for radiotherapy incident reports reached AUROC 0.82 on its own department's reports and 0.42–0.56 on the IAEA's multinational SAFRON reports. Fine-tuning on local data brought it back to 0.78 ([[2025-09-17-beidler-incident-report-severity-triage-radiotherapy|Beidler, Nguyen et al. 2025]]). England's national service reads about 10,000 of 2.6 million yearly reports by hand; its lead expected machine learning to change which reports people read, not to automate the decision ([[2023-03-08-meg-lfpse-mussett-interview|Mussett, 2023]]). See [[agent-oversight-and-delegation]].

## Governance

76% of Dutch hospitals have adopted an AI policy and 60% have an AI board. 53% use high-risk AI under the EU AI Act, whose high-risk obligations start on 1 August 2026 (M&I). In US hospitals, 66% have a dedicated committee for evaluating predictive models (ASTP). Across the WHO European Region, legal uncertainty is the most named barrier (43 of 50 states), and 4 of 50 have liability standards for AI. See [[responsible-ai]].

## Debates and supersession

- **Self-report against verified use.** Nearly every figure on this page is self-reported by executives or IT leads. The EC study is the only source that tested claims against evidence, and it found that fewer than half could document their use. Read high adoption figures as upper bounds.
- **The M&I 53% error.** The M&I report's conclusion and p. 25 text give 53% small-scale use, which is the 2025 value; the 2026 chart shows 42%. Press coverage repeated the 53%. The 8% large-scale and 0% very-large-scale figures agree everywhere.
- **Comparability over time.** RIVM's jump from 13% (2024) to 53% of doctors (2025) follows new answer options; RIVM says the two years "cannot be compared well". The M&I panel grew from 46 to 52 hospitals between editions.
- **Sponsorship.** Bessemer's index is investor- and vendor-sponsored, and one of its authors sits on the board of Qventus; Qventus's report recommends what Qventus sells; M&I is a consultancy. The peer-reviewed (Poon) and government sources (ASTP, RIVM, WHO, EC) point the same way.
- **Open question.** Does the 8% large-scale share in Dutch hospitals grow with the middle (average scale rose from 33% to 46%), or does it stall where the general maturity measures stall? The next M&I edition will tell.

## Related concepts

- [[enterprise-ai-adoption]] — the economy-wide pattern this sector repeats.
- [[ai-maturity-measurement-comparison]] — the thread on why maturity figures differ by instrument.
- [[responsible-ai]], [[agent-oversight-and-delegation]], [[ai-agents]], [[generative-ai]].
