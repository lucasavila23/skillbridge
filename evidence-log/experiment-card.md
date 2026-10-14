# Experiment Card

**v2, 2026-10-12. Certification rule revised 2026-10-13.**

**Interview intake, 2026-10-12:** the user supplied three interviews conducted
on October 5, 6 and 10, before the planned pilot window. See the
[source records](validation/v2-interviews-2026-10-12.md) and
[assessment](validation/v2-findings-2026-10-12.md). They add one conditional
EUR 15 willingness statement, one supportive recruiter mock-profile judgment,
and one engineer's proposed CSV challenge and criteria. No pilot submission,
payment, final brief or rubric sign-off is documented. This is preliminary
interview evidence; neither arm's threshold has been reached. Price, minimum
sample sizes, pilot dates and decision rules below are retained.

**Company interview, confirmed real 2026-10-13:** [DF-R01](validation/sources/company-interview-deem-finance.md), a fintech recruiter,
answered the Arm B questions before the pilot window: picked the certified
profile over CV-only (Q10), would accept it for the first screen if their own
team wrote the brief (Q14), and would pay per hire or per challenge (Q15). Like
V2-R01 it is a preliminary stated judgment and does not count toward B's 3 of 5,
which is measured in the pilot.

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
   rubric with 4–6 criteria, signed off by a working engineer. Publish the
   passing score, mandatory criteria and individual-verification requirements
   with the brief before students start; see [certification eligibility](#certification-eligibility).
2. Recruit students from survey respondents who left a contact, classmates and
   IE tech clubs ([recruitment](recruitment.md)). Solo or teams of up to 3; teams
   log who did what in a shared commit history or task list. Confirm the full
   engineer workload and capacity before committing to the student cohort.
3. Entry is free. After submitting, each student sees their overall score and
   pass/fail status privately. Label AI scores as provisional where human
   review is pending.
4. Only after the student passes and their individual contribution is verified,
   offer the **certified result** (rubric breakdown, written feedback, engineer
   sign-off, contribution record, shareable link) for **€15**, payable by Bizum
   or card link within 5 days of the offer. Refund on request within 14 days.
   Engineer-written feedback covers every certified result, not only top
   submissions (decided 2026-10-12,
   [v2 findings](validation/v2-findings-2026-10-12.md)). Each certified student
   receives feedback about their own work and contribution, including team
   members; attach it before issuing the certificate. Results are private by
   default; the student chooses what to share, and the certified result always
   shows the true score. A failed result cannot be certified or made passing
   by payment; no certification fee is collected for it.
5. The AI rubric scores every submission. The engineer independently scores a
   sample of five distinct project submissions — the top three plus two drawn
   from the lower half, following
   V2-E01 Q4's own suggestion to check a low-ranked submission before trusting
   the AI ranking — and both scores are recorded for each (tests A2.3). If teams
   produce fewer than five distinct submissions, review all and report the
   actual sample size; the primary minimum of 10 submitting students remains.
   At his estimate of 20 minutes per review, five reviews take about 100 minutes,
   plus eligibility checks on certification requests outside that sample and
   written feedback on every certified result (at the threshold, 3 certified
   results). Reuse sample reviews where applicable; do not assume they cover
   every request. Confirm this expanded workload when the brief is signed;
   scoring all ten alone would take about 3.3 hours, before any additional
   contribution checks or feedback time. Include setup, debriefs, coordination
   and rework in the full estimate. The sample is not a limit on feedback
   coverage; use the [ERRC workload accounting](ERRC.md#engineer-workload-and-cost)
   to count shared reviews once and individual feedback for every certificate.

**Arm B: recruiters (A3.1, A3.3).**
1. Contact 5+ recruiters or hiring managers who screen interns or juniors in
   software, web or data (IE Talent & Careers, LinkedIn, alumni).
2. Show two anonymised profiles side by side: CV only, and the same CV plus a
   SkillBridge certified result from the prototype, shown as the full bundle
   (work artifact, rubric breakdown with the company's name on it, engineer
   feedback and contribution record), never a bare score (decided 2026-10-12,
   after V2-R01 discounted an unexplained 82/100). 15-minute call or form.
   Keep a copy of the exact profiles shown.
   Explain the same pass/fail and individual-verification rules used in Arm A:
   the fee buys certification of an earned result, never a passing outcome.
3. Ask: which would you shortlist and why; does the certificate change your
   decision; would you accept it instead of your take-home test; what would make
   you distrust it.

## Certification eligibility

**Team decision, 2026-10-13:** students can fail certification. This replaces
the earlier rule that any score could be certified and aligns the written
offer with the presentation. It is a product rule, not a validation result.

- **Before participation:** the company and reviewing engineer approve the
  challenge's passing score, any mandatory criteria, and how each student's
  contribution and authorship will be checked. Publish these with the brief;
  do not lower the bar after seeing results or willingness to pay.
- **Pass:** meet the published performance requirements and verify individual
  work. The engineer confirms eligibility before the €15 offer. A team's
  passing score does not automatically certify every member.
- **Fail:** fall below the passing score, miss a mandatory criterion, or fail
  the individual-verification requirements. Keep the score and reason private;
  issue no certificate and collect no certification fee. A pending review or
  unresolved contribution dispute stays pending until human review resolves it.
- **Payment and sharing:** passing students may keep their free score or pay
  for the certified evidence bundle. Payment cannot alter the score or outcome.
  Certified results show the actual score and remain private until shared.

**Still to set before Arm A starts:** the challenge-specific pass mark,
mandatory criteria and verification procedure, including reviewer capacity.
No numerical certification pass mark has been agreed or validated yet. The
brief/rubric sign-off milestone below includes these rules; do not start Arm A
without them.

## Metric

- **A:** paid conversion = students who pay ÷ students who submit.
  Count each student once, including members of a shared team submission;
  distinct project submissions are the separate unit for the review sample.
- **B:** share of recruiters who say the certificate would change or support a
  shortlisting decision (stated).
- **Secondary:** AI vs engineer score gap per submission; completion rate
  (submit ÷ start); counts of passed, failed and pending results; eligible-to-paid
  conversion (students who pay ÷ students confirmed eligible and offered
  certification). Report a zero eligible denominator as not applicable.
- **Delivery and cost:** record actual engineer minutes by setup, sample review,
  additional eligibility work, feedback, debrief and coordination/rework;
  also record operator time and cash/automation costs. Track distinct project
  submissions, certification requests and individual certificates separately.
  Check that every issued certificate has its student's written feedback;
  this is an offer-fulfilment requirement, not a replacement for A or B.

The primary A denominator remains **all submitting students**, including
those who fail certification. Keep the 30% threshold unchanged and report
eligibility alongside conversion so failures are not mistaken for refusal to
pay. Do not replace the primary result with the eligible-only rate.

## Threshold

- **A:** ≥ 30% paid conversion with at least 10 submitting students.
- **B:** ≥ 3 of 5 recruiters.

Fixed before the test; not adjusted after seeing results.

## Evidence strength

A is **High**: real money, real submissions. B is **Medium**: stated intent from
real recruiters, not observed hiring. Fewer than 10 submitting students makes A
inconclusive, not a pass or fail.

## Decision rule

| A (students pay) | B (recruiters trust) | Decision |
|---|---|---|
| Pass | Pass | **Continue:** build the working skeleton in Phase 2; recruit a second company. |
| Fail | Pass | **Change revenue:** students free, test hypothesis 2 (companies pay for the screen). |
| Pass | Fail | **Narrow:** sell practice and feedback, drop the hiring-credential claim; retest B with a stronger calibration. |
| Fail | Fail | **Stop** the v2 credential model; return to the evidence and the archived v1 options. |

**Owner:** Lucas Avila (coordination); arm owners assigned at Session 14.
**Milestones:** a real company brief confirmed by 2026-10-16, otherwise the
illustrative brief in step 1; the written brief (owner: Lucas Avila) and an
engineer's rubric sign-off by 2026-10-20.
**Stop condition:** no engineer sign-off of a brief, rubric and published
certification requirements by 2026-10-20 →
run Arm B alone and record Arm A as not run.

## Next: details to narrow

The direction is set; the details are not. Each line below states what we
already know, the specific number or choice we still have to define, and how we
will narrow it. Values marked "to define" are decided by the team **before** the
test starts, not after seeing results.

| # | What we know | What we still need to define | How we narrow it |
|---|---|---|---|
| 1 | Certificates can help: showing a certificate on LinkedIn raised new employment by about 6%, and by about 12% for the weakest candidates (Athey & Palikot, Stanford trial, Coursera learners in developing countries). Platform claims of "2–4x" are vendor figures with no method. | **By how many percentage points our certificate must raise shortlisting** for it to be worth paying for (to define). | Arm B: show recruiters the same CV with and without the certificate; compare shortlist rates and set the minimum uplift in advance. |
| 2 | Free alternatives such as Forage compete with our fee; students pay for prep they believe works (LeetCode about $35/month, AWS exam about $100). Research puts a plausible one-off student fee at €10–30. | **The student price** within €10–30 that students accept and that still reads as credible, not as buying a pass (€15 is the first test value). | Survey follow-up question on price, then Arm A at €15; record "yes at a lower price" answers. |
| 3 | Companies already pay for screening and challenges: HackerRank from $79/month, Riipen $11.67/hour per student, Parker Dewey 10-hour projects, hackathon sponsorship $500–$50k+. | **The company price per challenge** and what the company gets for it (shortlist, engineer time saved, branding). | Ask the Arm A company contact and Arm B recruiters what they would pay instead of their current take-home or event. [DF-R01](validation/sources/company-interview-deem-finance.md) Q15–16: per hire or per challenge, compared with job-board spend, from the campus and employer-branding budget. |
| 4 | The team ranks students paying first; the research recommends companies pay and students get the certificate free. All three [one-on-one interviewees](validation/one-on-one-interviews-2026-10-12.md) say companies should pay most or all. The [v2 Fermi estimate](market-research/README.md#v2-fermi-estimate-challenge-completers-in-madrid-2026-10-12) shows student fees alone in Madrid stay under €9,000 a year even at the 30% threshold. | **Which side pays first**, and whether the two prices together cover one challenge's cost. | Decided by the Arm A/Arm B results through the decision rule above. |
| 5 | Students can give 2–7 hours a week; 12/17 at four hours or less. | **One time box** (4 hours is the working value) and the **completion rate** we need (to define; free online hackathons see about 15% of registrants submit). | Pilot challenge completion: starts vs submissions. |
| 6 | Git data alone misses silent or absent team members; peer ratings cut free-riding complaints from 26% to 7% in one study. | **How contribution is weighted** between commits, task logs and peer ratings, and the dispute rule. | Run both measures on pilot teams; compare with the engineer's view in the debrief. |
| 7 | Remote assessments face rising AI cheating; employers are adding live stages. | **How long the engineer debrief can be** before companies refuse (10 minutes is the working value; [DF-R01](validation/sources/company-interview-deem-finance.md) Q13 asked for a 15-minute walkthrough). | Ask the company contact; time the pilot debriefs. |
| 8 | The survey (n = 17) shows the student problem but never asked about paying, trust or profile fit. | **Follow-up questions to add to the same Google Form**: year, degree, university and internship status; would you do a 4-hour company challenge; would you pay €15 to certify the score (yes / no / at a lower price); what would make you trust or distrust the certificate. | Send to existing respondents and classmates; new answers flow into the live sheet and [pull-survey.sh](validation/pull-survey.sh). |
