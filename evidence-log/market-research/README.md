# SkillBridge market research — the piano-tuners exercise

**Date:** 2026-10-01 · **Geography:** Madrid region, confirmed by the user.
**Status:** First estimate to challenge; participation has not been measured.

## The one number

> **About 2,000 potential student participants per academic year in the Madrid
> region**, conditional on reaching them with a suitable paid client project.

Specifically: students in years 2–4 of software/web/data-related undergraduate
programmes, without a relevant internship or an effective professional referral
route, who would make a concrete commitment to join a scoped team campaign.
Count each student once in the academic year, even if they join several projects.

This estimates student demand under a suitable offer. It does not establish how
many students SkillBridge can acquire, how many projects businesses will fund,
completed campaigns, or revenue.

## One known anchor → four broad assumptions → one result

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

## First thing to challenge

**Will roughly one in five eligible students make a concrete commitment when
shown a real, suitable offer?** Inspect a work sample, record availability, and
observe acceptance of scope, dates and compensation; a positive survey answer
or waitlist registration is insufficient. The [analysis and validation plan](analysis.md)
defines the denominator, observable actions, and how new evidence changes the
number. The current business deposit experiment remains a separate requirement.

## Files

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
