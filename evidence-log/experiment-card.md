# Experiment Card

**v2, 2026-10-12.**

## v1 card: closed 2026-10-12, not run

The v1 test (pitch 10 small businesses, ≥2 sign a charter and pay a 10% deposit)
never reached a qualifying pitch; no charter or deposit was recorded. It is
closed without a result, not scored as a failure. The team pivoted on the
existing student evidence instead
([archive README](archive/v1-paid-projects/README.md),
[v1 card](archive/v1-paid-projects/experiment-card.md)).

## Hypothesis

Students will pay for a certified challenge score, because employers treat that score as credible evidence of job-ready skill.

Falsifiable form: at least 30% of students who submit a pilot challenge pay
€15 for the certified result, **and** at least 3 of 5 recruiters or hiring
managers say the certificate would change or support a shortlisting decision.

## Method

Concierge pilot, two arms run in parallel, 2026-10-16 to 2026-10-30.

**Arm A: students (A1.3).**
1. Prepare one challenge: a real brief from one SaaS, engineering or data
   company contact, or, if none confirms by 2026-10-16, a brief built on a public
   API or dataset and labelled "illustrative company". Time box: 4 hours. One
   rubric with 4–6 criteria, signed off by a working engineer.
2. Recruit students from survey respondents who left a contact, classmates and
   IE tech clubs ([recruitment](recruitment.md)). Solo or teams of up to 3; teams
   log who did what in a shared commit history or task list.
3. Entry is free. After submitting, each student sees their overall score.
4. Offer the **certified result** (rubric breakdown, written feedback, engineer
   sign-off, contribution record, shareable link) for **€15**, payable by Bizum
   or card link within 5 days. Refund on request within 14 days.
5. Score with the AI rubric and the engineer independently on every submission;
   record both (tests A2.3).

**Arm B: recruiters (A3.1, A3.3).**
1. Contact 5+ recruiters or hiring managers who screen interns or juniors in
   software, web or data (IE Talent & Careers, LinkedIn, alumni).
2. Show two anonymised profiles side by side: CV only, and the same CV plus a
   SkillBridge certificate from the prototype. 15-minute call or form.
3. Ask: which would you shortlist and why; does the certificate change your
   decision; would you accept it instead of your take-home test; what would make
   you distrust it.

## Metric

- **A:** paid conversion = students who pay ÷ students who submit.
- **B:** share of recruiters who say the certificate would change or support a
  shortlisting decision (stated).
- **Secondary:** AI vs engineer score gap per submission; completion rate
  (submit ÷ start).

## Threshold

- **A:** ≥ 30% paid conversion with at least 10 submissions.
- **B:** ≥ 3 of 5 recruiters.

Fixed before the test; not adjusted after seeing results.

## Evidence strength

A is **High**: real money, real submissions. B is **Medium**: stated intent from
real recruiters, not observed hiring. Fewer than 10 submissions makes A
inconclusive, not a pass or fail.

## Decision rule

| A (students pay) | B (recruiters trust) | Decision |
|---|---|---|
| Pass | Pass | **Continue:** build the working skeleton in Phase 2; recruit a second company. |
| Fail | Pass | **Change revenue:** students free, test hypothesis 2 (companies pay for the screen). |
| Pass | Fail | **Narrow:** sell practice and feedback, drop the hiring-credential claim; retest B with a stronger calibration. |
| Fail | Fail | **Stop** the v2 credential model; return to the evidence and the archived v1 options. |

**Owner:** Lucas Avila (coordination); arm owners assigned at Session 14.
**Stop condition:** no brief and no engineer sign-off by 2026-10-20 → run Arm B
alone and record Arm A as not run.
