# Assumptions

**v2, 2026-10-12.** v1's map (business trust in paid student work) is in the
[archive](archive/v1-paid-projects/assumptions.md).
Inputs: [opportunity](opportunity.md), [JTBD](jtbd.md),
[competitive analysis](market-research/competitive-analysis.md),
[survey summary](validation/survey-summary-2026-10-12.md), and
[v2 interview findings](validation/v2-findings-2026-10-12.md) from one student,
one recruiter and one engineer. V2 source IDs refer to the
[interview records](validation/v2-interviews-2026-10-12.md).

Tags: **Evidence** (linked), **Decision** (team), **Hypothesis** (untested).
Importance and evidence are rated High / Medium / Low.

## Area 1: Student pull and payment

| # | Assumption | Importance | Evidence | Status |
|---|---|---|---|---|
| A1.1 | Students struggle to prove contribution and experience beyond coursework. | High | High | **Evidence:** 14/17 and 12/17 (survey); 9/11 each (pilot). |
| A1.2 | Students will complete a challenge sized to 2–7 hours. | High | Medium | **Evidence** for capacity (12/17 at ≤4 h/week); completion itself untested. 7/17 cite losing motivation. |
| A1.3 | Students will pay a certification fee for a calibrated score. | High | Low | **Stated interest:** V2-S01 Q10 would pay EUR 15 after completing the work if feedback is specific and engineer-written. No SkillBridge payment or submission recorded; acceptance of an AI-only result is not established. |
| A1.4 | Students will join teams and accept a per-member contribution record. | Medium | Low | **Hypothesis.** 4/17 cite teammate coordination as a blocker. |

## Area 2: Company supply

| # | Assumption | Importance | Evidence | Status |
|---|---|---|---|---|
| A2.1 | SaaS, engineering and data companies will provide a real brief and sign off a rubric. | High | Low | **Interview proposal:** V2-E01 Q1-Q2 identifies a CSV task, offers non-sensitive examples and gives five criteria. No written brief, examples or final rubric sign-off supplied. |
| A2.2 | A company engineer will score a sample of submissions and write feedback on every certified result within one week. | Medium | Low | **Stated willingness:** V2-E01 Q3 estimates one hour for three submissions if coordination stays minimal. No completed review or one-week deadline agreed. |
| A2.3 | An AI rubric plus automated tests scores close enough to the engineer's judgement. | High | None | **Hypothesis.** V2-E01 Q4 suggests checking a low-ranked submission; this is a trust condition, not a measured accuracy result. Compare paired AI and engineer scores in the pilot. |

## Area 3: Credential credibility

| # | Assumption | Importance | Evidence | Status |
|---|---|---|---|---|
| A3.1 | Recruiters treat a company-calibrated score as credible evidence of job-ready skill. | High | Low | **Stated screening judgment:** V2-R01 Q6-Q7 favours a mock profile with work and engineer feedback, but discounts an unexplained numerical score. [DF-R01](validation/sources/company-interview-deem-finance.md) Q10-Q12 picks the certified profile on the same conditions. Two recruiters; no observed hiring effect. |
| A3.2 | A verified contribution record answers the recruiter's "what did *you* do?" question. | High | Low | **Reported problem:** pilot P016, V2-S01 Q3 and V2-R01 Q3. The recruiter values inspectable evidence (Q6-Q7); actual contribution verification remains untested. |
| A3.3 | Employers would use the score in place of a take-home test. | Medium | Low | **Conditional interest:** V2-R01 Q8 would consider the company's own brief and engineer sign-off, retaining a live check. [DF-R01](validation/sources/company-interview-deem-finance.md) Q14 says the same for the first screen. No replacement decision recorded. |

## Revenue hypotheses (ranked by the team)

1. **Students pay** a certification fee to be more attractive for internships. Depends on A1.3 and A3.1.
2. **Companies pay** to use challenges as a hiring screen. Depends on A2.1 and A3.3.
3. **Companies pay a sponsorship** for employer branding. Depends on A2.1; competes with Devpost and HackerEarth.

The ranking is a **Decision**; none is validated.

V2-S01 Q10 adds conditional student willingness at EUR 15. V2-R01 Q10 and
V2-E01 Q6 connect possible company spending to screening effort and mention
existing budgets, but supply no accepted SkillBridge price or payment. The
engineer is not the spending decision-maker. These signals do not change the
ranking or establish a paying customer.

The [one-on-one interviews](validation/one-on-one-interviews-2026-10-12.md)
add a contrary signal: all three interviewees (a graduate, an IE student and a
recruiter) say companies should pay most or all of the cost, with students
paying at most a small fee. This matches the desk research. The ranking stays
until the pilot decides; the company price is defined alongside the pilot
([details to narrow](experiment-card.md#next-details-to-narrow), row 3) so the
"students fail, recruiters pass" branch of the
[decision rule](experiment-card.md#decision-rule) can start at once.

[DF-R01](validation/sources/company-interview-deem-finance.md) supports hypotheses 2 and 3 from the buyer's side: it would pay per
hire or per challenge from the campus and employer-branding budget, signed off
by the HR director, replacing part of a datathon sponsorship. Stated and
conditional; no price agreed.

## MECE checks

- Areas split by actor: student (1), company (2), recruiter (3). Each assumption
  has one owner actor.
- Payment sits in Area 1 (student pays) and in the revenue list (who pays);
  company payment is covered by A2.1 + A3.3, not repeated.
- v1's business-trust assumptions are retired, not merged; see the archive.

## Riskiest assumption

Students will pay for a certified challenge score, because employers treat that score as credible evidence of job-ready skill.

It combines A1.3 and A3.1: both remain High importance with limited interview
signals, and revenue hypothesis 1 fails if either fails. Conditional payment
interest and one mock-profile judgment do not establish the combined claim.
Test: [experiment card](experiment-card.md).

## Open gaps

- Price point for the certification fee (the test uses one price; see the card).
- Whether students prefer solo or team challenges.
- Whether engineer-written feedback on every certified result (decided
  2026-10-12) still fits the engineer's time once more than three students pay.
- Public-score visibility, pass criteria, live authenticity checks and rubric
  calibration; see [v2 findings](validation/v2-findings-2026-10-12.md).
- Legal: IP of student submissions on a company brief (see
  [legal constraints](../legal-constraints.md)).
