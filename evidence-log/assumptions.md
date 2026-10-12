# Assumptions

**v2, 2026-10-12.** v1's map (business trust in paid student work) is in the
[archive](archive/v1-paid-projects/assumptions.md).
Inputs: [opportunity](opportunity.md), [JTBD](jtbd.md),
[competitive analysis](market-research/competitive-analysis.md),
[survey summary](validation/survey-summary-2026-10-12.md).

Tags: **Evidence** (linked), **Decision** (team), **Hypothesis** (untested).
Importance and evidence are rated High / Medium / Low.

## Area 1: Student pull and payment

| # | Assumption | Importance | Evidence | Status |
|---|---|---|---|---|
| A1.1 | Students struggle to prove contribution and experience beyond coursework. | High | High | **Evidence:** 14/17 and 12/17 (survey); 9/11 each (pilot). |
| A1.2 | Students will complete a challenge sized to 2–7 hours. | High | Medium | **Evidence** for capacity (12/17 at ≤4 h/week); completion itself untested. 7/17 cite losing motivation. |
| A1.3 | Students will pay a certification fee for a calibrated score. | High | **None** | **Hypothesis.** Never asked; every alternative is free to students. |
| A1.4 | Students will join teams and accept a per-member contribution record. | Medium | Low | **Hypothesis.** 4/17 cite teammate coordination as a blocker. |

## Area 2: Company supply

| # | Assumption | Importance | Evidence | Status |
|---|---|---|---|---|
| A2.1 | SaaS, engineering and data companies will provide a real brief and sign off a rubric. | High | None | **Hypothesis.** Companies already pay Devpost and HackerEarth to host events ([competitive analysis](market-research/competitive-analysis.md#v2-alternatives-challenge-and-assessment-platforms-2026-10-12)), so the behaviour exists elsewhere. |
| A2.2 | A company engineer will review the top submissions within one week. | Medium | Low | **Hypothesis.** v1 interview UV-B02: reviewing work costs time ([findings](validation/findings-2026-09-22.md)). |
| A2.3 | An AI rubric plus automated tests scores close enough to the engineer's judgement. | High | None | **Hypothesis.** Testable by comparing AI and engineer scores on the same submissions. |

## Area 3: Credential credibility

| # | Assumption | Importance | Evidence | Status |
|---|---|---|---|---|
| A3.1 | Recruiters treat a company-calibrated score as credible evidence of job-ready skill. | High | None | **Hypothesis.** The [Skeptical Verifier](personas/ai-persona-03.md) models this; no recruiter interviewed. |
| A3.2 | A verified contribution record answers the recruiter's "what did *you* do?" question. | High | Low | **Evidence** that recruiters ask it (pilot P016); that a record answers it: Hypothesis. |
| A3.3 | Employers would use the score in place of a take-home test. | Medium | None | **Hypothesis.** Basis for revenue hypothesis 2. |

## Revenue hypotheses (ranked by the team)

1. **Students pay** a certification fee to be more attractive for internships. Depends on A1.3 and A3.1.
2. **Companies pay** to use challenges as a hiring screen. Depends on A2.1 and A3.3.
3. **Companies pay a sponsorship** for employer branding. Depends on A2.1; competes with Devpost and HackerEarth.

The ranking is a **Decision**; none is validated.

## MECE checks

- Areas split by actor: student (1), company (2), recruiter (3). Each assumption
  has one owner actor.
- Payment sits in Area 1 (student pays) and in the revenue list (who pays);
  company payment is covered by A2.1 + A3.3, not repeated.
- v1's business-trust assumptions are retired, not merged; see the archive.

## Riskiest assumption

Students will pay for a certified challenge score, because employers treat that score as credible evidence of job-ready skill.

It combines A1.3 and A3.1: both are High importance with no evidence, and
revenue hypothesis 1 fails if either fails. Test: [experiment card](experiment-card.md).

## Open gaps

- Price point for the certification fee (the test uses one price; see the card).
- Whether students prefer solo or team challenges.
- Legal: IP of student submissions on a company brief (see
  [legal constraints](../legal-constraints.md)).
