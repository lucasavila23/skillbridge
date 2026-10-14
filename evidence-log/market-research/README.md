# SkillBridge market research — the piano-tuners exercise

> **v2 note (2026-10-12):** after the pivot to a challenge platform, the student
> pool below still applies, but "paid client project" and "team campaign" read as
> "short company challenge", and the business deposit experiment is closed
> ([experiment card](../experiment-card.md)). v2 market research:
> [competitive analysis, v2 section](competitive-analysis.md#v2-alternatives-challenge-and-assessment-platforms-2026-10-12),
> [value curve](value-curve.md) and the [v2 market report](deep-research/reports/SkillBridge%20v2%20challenge%20market.md).

**Date:** 2026-10-01 · **Geography:** Madrid region, confirmed by the user.
**Status:** Pilot results reviewed; the regional participation rate remains
unmeasured and all four model rates remain assumptions.

## Latest validation update

**2026-10-13 market feature review:** [individual-contribution verification](contribution-verification-review-2026-10-13.md)
now has an explicit definition and a dated competitor/source table. NUWE is
labelled **not publicly disclosed**; the claimed difference is scoped to the
reviewed benchmark offers and does not establish market-wide uniqueness.
This is desk research, not new user validation.

The [actual pilot assessment](pilot-assessment-2026-10-01.md) strengthens the
case for the student problem and reports commitments, accepted client work and
clearer contribution evidence for recruiters. In the 11-person survey, 9 selected
difficulty showing experience beyond coursework and 9 selected explaining their
contribution. The survey's full Madrid-segment fit is unconfirmed.

The report does **not** validate the 20% readiness rate or the business
charter-and-deposit threshold. Keep the estimate below as a hypothesis. The
assessment separates reported outcomes from stated intentions, flags a survey
selection-count inconsistency, and specifies the records needed to resolve the
remaining questions.

## v2 Fermi estimate: challenge completers in Madrid (2026-10-12)

> **About 2,000 students per academic year in the Madrid region would complete
> at least one short company challenge**, if one relevant to their target role
> were offered.

One known anchor, four assumptions, one number. A1–A3 are unchanged from v1
because the student user did not change; A4 is redefined for a 4-hour challenge.

| Step | Evidence status | Input and choice | Calculation |
|---|---|---|---|
| 1. Undergraduate population | **KNOWN, provisional official data** | 261,707 enrolments, 18 Madrid universities, 2024/25; round to **260,000** | Anchor |
| 2. Relevant tech studies | **ASSUME A1** | 5–15%; use **10%** | **26,000** |
| 3. Years 2–4 | **ASSUME A2** | 60–80%; use **75%** | **19,500** |
| 4. Experience gap | **ASSUME A3** | 30–70%; use **50%** | **9,750** |
| 5. Complete a challenge this year | **ASSUME A4 (v2)** | 10–30%; use **20%**. Benchmarks: about 15% of registrants submit in a free online hackathon; 46% of paying MOOC learners finish against 3% of all registrants ([student motives](deep-research/research_notes/SkillBridge%20v2%20challenge%20market/student_motives.md)) | **1,950** |
| 6. Result | **DERIVED** | Round to the uncertainty | **≈ 2,000 completers / year** (range 975–2,925 on A4 alone) |

```text
260,000 × 0.10 × 0.75 × 0.50 × 0.20 = 1,950 ≈ 2,000
```

### Why the number matters for the decision

If students are the only payers and each certifies one result a year at €15:

| Share of completers who pay | 5% | 10% | 30% (experiment threshold) |
|---|---|---|---|
| Madrid student-fee revenue / year | €1,462 | €2,925 | €8,775 |

**So what:** even at the experiment's 30% threshold, student fees alone in Madrid
come to under €9,000 a year. That does not fund company engineers' time or the
platform. It supports the research finding that companies (revenue hypotheses 2
and 3) must pay, and it makes "which side pays first" the most decision-relevant
detail to narrow ([experiment card](../experiment-card.md#next-details-to-narrow)).
The 10% base for paying is a judgement; a freemium benchmark is Duolingo's about
9% of active users paying ([willingness to pay](deep-research/research_notes/SkillBridge%20v2%20challenge%20market/willingness_to_pay.md)).

**First thing to challenge:** A4. Will one in five eligible students actually
finish a 4-hour challenge? The pilot challenge measures it directly (starts vs
submissions).

Reproduce: `python3 calculate.py` prints both the v1 and v2 chains.

## v1 Fermi estimate (paid client projects, kept as history)

### The one number (v1)

> **About 2,000 potential student participants per academic year in the Madrid
> region**, conditional on reaching them with a suitable paid client project.

Specifically: students in years 2–4 of software/web/data-related undergraduate
programmes, without a relevant internship or an effective professional referral
route, who would make a concrete commitment to join a scoped team campaign.
Count each student once in the academic year, even if they join several projects.

This estimates student demand under a suitable offer. It does not establish how
many students SkillBridge can acquire, how many projects businesses will fund,
completed campaigns, or revenue.

### One known anchor → four broad assumptions → one result (v1)

| Step | Evidence status | Input and choice | Calculation |
|---|---|---|---|
| 1. Undergraduate population | **KNOWN, provisional official data** | 261,707 enrolments across the 18 universities in Madrid's in-person undergraduate dataset, 2024/25; round to **260,000** | Starting population proxy |
| 2. Relevant tech studies | **ASSUME A1** | 5–15%; use **10%** in software/web/data-related programmes | 260,000 × 10% = **26,000** |
| 3. Target stage | **ASSUME A2** | 60–80%; use **75%** in years 2–4, conditional on A1 | 26,000 × 75% = **19,500** |
| 4. Experience gap | **ASSUME A3** | 30–70%; use **50%** with neither a relevant internship nor an effective referral route, conditional on A2 | 19,500 × 50% = **9,750** |
| 5. Ready to commit this academic year | **ASSUME A4** | 10–30%; use **20%** able and willing to commit when offered a suitable paid campaign, conditional on A3 | 9,750 × 20% = **1,950** |
| 6. Result | **DERIVED** | Round to match the uncertainty | **≈ 2,000 students / academic year** |

```text
260,000 × 0.10 × 0.75 × 0.50 × 0.20 = 1,950 ≈ 2,000
```

The anchor comes from the [Comunidad de Madrid open-data catalogue](https://datos.gob.es/es/catalogo/a13002908-estudiantes-matriculados-en-estudios-de-grado-presenciales-por-universidad),
summing its 2025 rows; the catalogue uses the ending year of each academic year.
All 18 selected rows are marked provisional. The university-based population is
a proxy for regional campus participation, not a census of Madrid residents or
every student physically studying in Madrid. See [source coverage and the saved
data](sources.md) before expanding or applying the estimate to a specific campus.

The four percentages and their ranges are judgement calls, not findings from the
official dataset or our interviews. They apply successively to the preceding
group; they do not assume that the four characteristics are independent.

### First thing to challenge (v1)

**Will roughly one in five eligible students make a concrete commitment when
shown a real, suitable offer?** Inspect a work sample, record availability, and
observe acceptance of scope, dates and compensation; a positive survey answer
or waitlist registration is insufficient. The [analysis and validation plan](analysis.md)
defines the denominator, observable actions, and how new evidence changes the
number. The current business deposit experiment remains a separate requirement.

## Files

- [Consolidated deep research — five AI reports](deep-research/merged-market-research.md):
  synthesis received 2026-10-03, with disagreements, source limitations and
  proposed tests kept explicit. [All five original reports](deep-research/README.md)
  are preserved unchanged; external claims have not been independently rechecked
  as part of the merge.
- [Pilot assessment](pilot-assessment-2026-10-01.md): findings, model/competitor
  updates, evidence limits and prioritised next actions, linked to the preserved
  source report and transcription.
- [Coverage audit and next validation work](validation-audit.md): checks all six
  comparison fields, defines measurable criteria and prioritises the missing tests.
- [Blank validation record](validation-record-template.md): eligibility screen,
  behaviour interview, evidence ledger and offer/delivery measurement fields.
- [Competitive alternatives](competitive-analysis.md): five representative
  alternatives, their appeal, evidence gaps and concrete switching tests.
- [Analysis](analysis.md): why each assumption was chosen, sensitivity, evidence
  limits and the proposed validation steps.
- [Sources](sources.md): provenance, university rows, coverage and reproduction.
- [Calculator](calculate.py): reproduces the anchor, funnel and sensitivity from
  the saved official JSON, using only the Python standard library.

The supplied piano-tuner screenshot informed the estimation method only. Its
Madrid population, piano ownership and tuner-capacity figures are not inputs to
SkillBridge's estimate.
