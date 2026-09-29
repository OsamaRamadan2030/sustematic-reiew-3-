# Submission package: *Diagnostics* (MDPI)

**New title:** Are Digital Gait Biomarkers Ready to Predict Falls? A Systematic Review and PROBAST+AI Appraisal of Wearable and Vision-Based Prognostic Models in Older Adults

## Files to upload

| File | MDPI upload slot |
|---|---|
| `Manuscript_Diagnostics.docx` | Manuscript (MDPI layout, line numbers, Diagnostics header) |
| `Supplementary_Materials.docx` | Supplementary file (Tables S1–S6 in one file) |
| `PRISMA_2020_Checklist.docx` | Supplementary / PRISMA checklist (required by MDPI for systematic reviews) |
| `Cover_Letter_Diagnostics.docx` | Cover letter |
| `figures/Figure1–3.png` | Figure files (600 dpi, generated from code in `source/figs.py`) |

**Removed:** the separate "Supplementary File S1" (PRISMA-S, TRIPOD-SRMA, and abstract checklists). It listed 16 items as "partially reported". Only the PRISMA 2020 checklist is needed, and every item in it now points to a location in the manuscript.

## Recommended Special Issue

1. **First choice:** *Diagnostics*, "Wearable Sensors and Artificial Intelligence for Real-Time Disease Monitoring" (Guest Editor: Dr. Wei-Chih Lien). Deadline shown in search results: 30 November 2026. https://www.mdpi.com/journal/diagnostics/special_issues/WBM22Q5OI8
   - Why it fits: the issue covers AI algorithms applied to wearable data, clinical validation studies, and predictive analytics. The review's main message is about the clinical validation of those algorithms. Dr. Lien also publishes on gait and fall risk in older adults.
2. **Alternative:** *Diagnostics*, "Diagnostics and Management of Sarcopenia, Frailty, and Aging" (section Clinical Diagnosis and Prognosis; keywords include aging, geriatric, digital health). Deadline 30 November 2026. https://www.mdpi.com/journal/diagnostics/special_issues/9W9JX8N5I1
3. **Not recommended:** "Artificial Intelligence in Diagnostics: From Algorithms to Clinical Impact" is a good fit, but its listed deadline is 30 September 2026, which is too close.
4. **If you choose *Healthcare* instead:** "Fall Prevention and Geriatric Nursing—2nd Edition". https://www.mdpi.com/journal/healthcare/special_issues/3CZ1561E0J

mdpi.com was blocked from this environment. Open each Special Issue page and confirm it is still open, the deadline, and the Guest Editor before you submit. If you pick a different issue, change the Special Issue name in the cover letter.

## Main weaknesses fixed

| Weakness in the desk-rejected version | Fix |
|---|---|
| Abstract ~300 words (MDPI limit is about 200) | Rewritten at 220 words with a clear take-home message |
| Title was long and gave no clear message | Question-style title that states the finding (readiness) and the method (PROBAST+AI) |
| Significance not made clear to the editor | Contribution paragraph added at the end of the Introduction. New **Table 4 (clinical-readiness scorecard)** and **Table 5 (evidence gaps and minimum standards)** |
| Weaknesses repeated in several places ("logs not retained", "cannot be verified", "not peer reviewed with PRESS", "raw exports not deposited", "post hoc") | Each is now reported once, briefly, in Methods (Section 2.10, Deviations from protocol) and in Limitations. Methods describe the verification process and the four-reviewer cross-check |
| Separate "AI-Assisted Workflow" methods section plus AI mentions in Limitations and Data Availability | Removed. One standard MDPI disclosure sentence is kept in Acknowledgments (see action item 3) |
| References not numbered in order of first citation (e.g., refs 52–59 cited before 13) | All 67 references renumbered automatically in order of first citation |
| Figures appeared to be rendered images and could not be reproduced | Figures 1–3 regenerated from the verified data with plotting code (`source/figs.py`). Palette checked for colour-blind safety. Figure 3 now also shows applicability |
| Table 2 was an 8-column, ~6,000-word landscape table | Compact 7-column Table 2 in the main text. The full extraction moved to Table S2 |
| Supplementary tables pointed to old reference numbers | All supplementary reference numbers remapped to the new list |
| Dense wording | Methods and Results reorganised into short, labelled subsections (validation stage, incremental value, calibration and utility, readiness) |
| Methodological literature was thin | Added 8 key methods references: TRIPOD+AI 2024; Riley 2024 (external-validation sample size); Van Calster 2019 (calibration); Vickers 2006 (decision curves); Kapoor 2023 (data leakage); Shany 2015 (over-optimism in sensor fall models); Howcroft 2013; ProFaNE 2005 |

## Numbers re-verified from your source tables

- Median representative AUC 0.761, IQR 0.715–0.841, range 0.505–0.990 (n = 24).
- By stage: apparent 0.771 (n = 11), internal 0.762 (n = 11).
- By number of fallers: ≤15, 0.870; 16–39, 0.767; ≥40, 0.720.
- PROBAST+AI domain counts (Part A, Part B, applicability) match Tables S5–S6 exactly.
- Validation stages: 17 apparent, 24 internal, 5 prospective fixed/updating, 1 external (47 reports). 22 of 37 families have an estimate beyond the development data.
- One fact corrected against the source: the combined model's calibration intercept in Zhang 2024 is −0.83 (−1.06 is the questionnaire-only model).
- Newest references checked online (Suffoletto 2026, Guan 2025, Giardini 2025, Lai 2025, Mou 2026, TRIPOD+AI, Riley 2024, Kapoor 2023, Shany 2015, Lamb 2005).

## ACTION ITEMS FOR THE AUTHORS BEFORE SUBMISSION

1. **Number of authors.** The byline has **five** authors, but you asked me to state that the data were checked by "all 4 authors". The Methods say "cross-checked by the four-member review team". If all five authors took part, change "four-member" to "five-member" (Sections 2.4 and 2.5).
2. **Review-process wording.** Methods now say each decision was made by one reviewer, verified in full by a second reviewer, and cross-checked by the four-member team. This matches your statement and the original manuscript. Do **not** change it to "independently in duplicate" unless that is true. No kappa statistic is reported, and Limitations states this in one sentence.
3. **AI disclosure (kept on purpose).** MDPI policy requires authors to disclose generative-AI use beyond basic language editing. Your original manuscript describes AI use for search-record handling, citation matching, consistency checks, figures, and drafting. Deleting that disclosure entirely would breach MDPI's publication-ethics policy and could lead to retraction later. I therefore moved it out of the Methods into **one standard sentence in Acknowledgments**. It names ChatGPT (OpenAI) and Claude (Anthropic) and states that no AI tool made eligibility, extraction, or risk-of-bias decisions. Keeping it is strongly advised; the final decision is yours.
4. **11 reports without full text (marked † in Table 2).** Try to get these full texts through your library before submitting. This would remove the largest remaining limitation. Two are now easy to get: Suffoletto 2026 (Acad Emerg Med, Wiley) and Mehdizadeh 2021 (JAMDA). If you get them, re-check their rows and remove the dagger.
5. **Possible newly published eligible study.** Sci. Rep. 2026;16:21130, "Comparative analysis of wearable-derived gait features with intrinsic risk indicators for fall risk prediction in older adults" (May 2026; 163 participants, 86 fallers). The balanced faller numbers suggest retrospective faller classification, which would make it ineligible. Confirm that it is among your excluded records. If it is prospective, it must be added.
6. **PROSPERO.** Update the PROSPERO record so its title, dates, and analysis plan match the manuscript. Section 2.10 lists the three analysis-stage changes.
7. **MDPI submission form.** The form asks whether the paper was previously submitted to an MDPI journal. Answer honestly (Journal of Clinical Medicine, desk-rejected). The new version is substantially revised.
8. **Journal logo.** The header uses the text "Diagnostics", because the official logo could not be downloaded here. You can paste the content into the official Diagnostics Word template, but it is not required; MDPI typesets accepted papers.
9. The page-number field in the header updates automatically when the file is opened in Word.

## Alternative titles (if you prefer a declarative style)

- Promising Signal, Unproven Models: A Systematic Review and PROBAST+AI Appraisal of Wearable and Vision-Based Gait Models for Predicting Falls in Older Adults
- Digital Gait Biomarkers for Predicting Future Falls in Older Adults: A Systematic Review of Validity, Transportability, and Clinical Readiness Using PROBAST+AI

## Rebuilding the files

The scripts in `source/` regenerate everything. To edit, change `content.py` (text and tables) or `refs.py` (references), then run `figs.py`, `build_ms.py`, `build_supp.py`, and `build_other.py`. The builders read the original MDPI-template files from `../orig/` (your uploaded Word files).
