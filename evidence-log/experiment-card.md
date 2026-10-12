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

## Next: details to narrow

The direction is set; the details are not. Each line below states what we
already know, the specific number or choice we still have to define, and how we
will narrow it. Values marked "to define" are decided by the team **before** the
test starts, not after seeing results.

| # | What we know | What we still need to define | How we narrow it |
|---|---|---|---|
| 1 | Certificates can help: showing a certificate on LinkedIn raised new employment by about 6%, and by about 12% for the weakest candidates (Athey & Palikot, Stanford trial, Coursera learners in developing countries). Platform claims of "2–4x" are vendor figures with no method. | **By how many percentage points our certificate must raise shortlisting** for it to be worth paying for (to define). | Arm B: show recruiters the same CV with and without the certificate; compare shortlist rates and set the minimum uplift in advance. |
| 2 | Every alternative is free to students; students pay for prep they believe works (LeetCode about $35/month, AWS exam about $100). Research puts a plausible one-off student fee at €10–30. | **The student price** within €10–30 that students accept and that still reads as credible, not as buying a pass (€15 is the first test value). | Survey follow-up question on price, then Arm A at €15; record "yes at a lower price" answers. |
| 3 | Companies already pay for screening and challenges: HackerRank from $79/month, Riipen $11.67/hour per student, Parker Dewey 10-hour projects, hackathon sponsorship $500–$50k+. | **The company price per challenge** and what the company gets for it (shortlist, engineer time saved, branding). | Ask the Arm A company contact and Arm B recruiters what they would pay instead of their current take-home or event. |
| 4 | The team ranks students paying first; the research recommends companies pay and students get the certificate free. The [v2 Fermi estimate](market-research/README.md#v2-fermi-estimate-challenge-completers-in-madrid-2026-10-12) shows student fees alone in Madrid stay under €9,000 a year even at the 30% threshold. | **Which side pays first**, and whether the two prices together cover one challenge's cost. | Decided by the Arm A/Arm B results through the decision rule above. |
| 5 | Students can give 2–7 hours a week; 12/17 at four hours or less. | **One time box** (4 hours is the working value) and the **completion rate** we need (to define; free online hackathons see about 15% of registrants submit). | Pilot challenge completion: starts vs submissions. |
| 6 | Git data alone misses silent or absent team members; peer ratings cut free-riding complaints from 26% to 7% in one study. | **How contribution is weighted** between commits, task logs and peer ratings, and the dispute rule. | Run both measures on pilot teams; compare with the engineer's view in the debrief. |
| 7 | Remote assessments face rising AI cheating; employers are adding live stages. | **How long the engineer debrief can be** before companies refuse (10 minutes is the working value). | Ask the company contact; time the pilot debriefs. |
| 8 | The survey (n = 17) shows the student problem but never asked about paying, trust or profile fit. | **Follow-up questions to add to the same Google Form**: year, degree, university and internship status; would you do a 4-hour company challenge; would you pay €15 to certify the score (yes / no / at a lower price); what would make you trust or distrust the certificate. | Send to existing respondents and classmates; new answers flow into the live sheet and [pull-survey.sh](validation/pull-survey.sh). |
