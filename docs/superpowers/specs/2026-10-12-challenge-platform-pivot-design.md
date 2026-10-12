# SkillBridge v2: challenge platform pivot (design)

**Date:** 2026-10-12 · **Deadline:** Group Project I, Session 14 (2026-10-13)
**Status:** draft for team review

## Intent

Pivot SkillBridge from paid student-team projects for small businesses (v1) to a
challenge platform: SaaS, engineering and data science companies post
challenges; students compete alone or in teams; submissions are scored and
certified; students build a stackable profile for their CV.

Success for tomorrow: one coherent evidence chain in which existing evidence
explains the pivot, every live file agrees with v2, the ERRC has four distinct
moves, and the press release, value curve and next test are present.

## Decisions (confirmed with Lucas)

| Decision | Choice |
|---|---|
| Scope | Full pivot before Group Project I |
| History | Keep all v1 work as evidence (option B: archive snapshot, fresh live files) |
| Student user and Job | Unchanged: the JTBD is solution-neutral |
| Revenue | Hypotheses, not decided. R1 students pay a certification fee (lead); R2 companies pay to use challenges as a hiring screen; R3 companies pay a sponsorship |
| Grading | Automated tests and an AI rubric score every submission; a company engineer signs off the rubric and reviews the top submissions |
| New evidence before tomorrow | None. Present the pivot with existing evidence and a precommitted next test |

## Differentiation hypothesis

Not validated. Each line rests on existing evidence or a named gap.

1. **Verified individual contribution in team submissions**: pilot, 9/11 could
   not explain their contribution. No alternative reviewed records it.
2. **Company-calibrated score with written feedback**, not a rank or a
   completion badge: "lack of feedback or guidance" in survey and pilot.
3. **Challenges sized to 2–7 hours**: stated capacity in pilot and survey.
4. **Score as a take-home replacement** for employers: hypothesis only; it is the
   proposed reason companies join and recruiters trust the certificate.

## Repository changes

### Archive (copy, links fixed)

`evidence-log/archive/v1-paid-projects/` receives copies of `opportunity.md`,
`goals.md`, `assumptions.md`, `experiment-card.md`, `jtbd.md`, `recruitment.md`,
`ERRC.md` and `personas/` as they stand on 2026-10-12, plus a `README.md`
explaining what v1 was and why it was archived. Relative links inside the
copies are rewritten so they resolve from the new location. `prototype/` v0 is
already versioned and stays where it is.

### Rewritten live files

| File | v2 content |
|---|---|
| `opportunity.md` | New one-liner and user/need/insight/HMW; companies and recruiters replace small businesses; pivot rationale with evidence links |
| `jtbd.md` | Same Job; solution hired and switching forces updated for challenge platforms |
| `goals.md` | Product Goal and new Sprint Goal (will students pay for a company-calibrated score; will employers trust it) |
| `assumptions.md` | Three areas re-mapped (student pull and payment, company supply, credential credibility); riskiest assumption named; revenue options R1–R3 |
| `experiment-card.md` | v1 card closed as "not run, pivoted"; new precommitted test with metric, threshold and decision rule |
| `recruitment.md` | Who the next test recruits and how; v1 interviews kept as references |
| `ERRC.md` | Completed: baseline, four moves, cost and buyer-value effects, falsifiable value hypothesis, validation points |
| `press-release.md` (new) | Lean Working Backwards opener |
| `personas/` | `ai-persona-01` Tinkerer and `ai-persona-02` Late Sprinter kept with a v2 note; **`ai-persona-03` becomes the Skeptical Verifier** (recruiter); Once-Bitten Owner moves to `drafts/` |
| `market-research/competitive-analysis.md` | Add Devpost, HackerEarth/HackerRank, Kaggle and a deeper Forage entry, each web-researched with sources |
| `market-research/value-curve.md` (new) + chart | About seven factors: SkillBridge v2 vs Forage, Devpost, Kaggle and coursework |
| `market-research/analysis.md` | Note: student-pool Fermi estimate still applies; revenue not recomputed for v2 |
| `prototype/prototype-v1.html` (new) | Clickable flow: challenge brief, team submission with contribution records, AI and company score, certificate on profile; exported to PDF and PNG |
| `ai-usage-log.md` | One entry for the pivot |

### Unchanged

`validation/`, `market-research/` sources and deep research, `downloads/`,
prototype v0.

## Evidence rules

- No new real-user evidence is claimed. Every v2 claim is tagged as evidence
  (with link), team decision or hypothesis.
- Competitor facts come from the competitor's own pages, with access dates.
- Revenue numbers are not invented; the Fermi estimate covers the student pool only.

## Verification

- Every relative Markdown link resolves (link checker run over the repo).
- Live files agree on the one-liner, riskiest assumption and next test.
- Prototype v1 opens offline and exports to PDF and PNG.

## Out of scope

`specs/` constitution (Session 13 onward), any working code beyond the
clickable prototype, recalculating the market estimate.
