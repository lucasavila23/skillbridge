# Eliminate-Reduce-Raise-Create Grid

**Status:** Four strategic moves and their cost/value trade-offs defined;
outcomes remain hypotheses (v2, revised 2026-10-14).
The v1 working file (Extern baseline, Stages A–B) is in the
[archive](archive/v1-paid-projects/ERRC.md).

**Target user:** a 2nd–4th-year software, web or data student whose experience
is mainly coursework ([opportunity](opportunity.md)).

**Job to Be Done:** when applying for internships and asked for project examples
or something delivered, have practical work they can demonstrate and explain to
an employer ([JTBD](jtbd.md)).

**Strongest current alternative:** coursework and personal projects (what
students actually do: 9/17 latest project reviewed only by class or staff), and,
among platforms, **Forage**: free, employer-branded, 2–6 hour simulations with a
completion certificate ([competitive analysis](market-research/competitive-analysis.md#v2-alternatives-challenge-and-assessment-platforms-2026-10-12)).

**Evidence basis for the baseline:** student survey n = 17 and pilot n = 11
(stated behaviour, probably overlapping; the survey collected no year,
programme or university, so its fit to the target profile is unconfirmed);
competitor facts from published pages;
market facts from the [deep research notes][N] and the synthesised
[v2 market report](market-research/deep-research/reports/SkillBridge%20v2%20challenge%20market.md). No student was observed using
Forage, HackerRank, Devpost or Kaggle.

## Market baseline: competing factors

| Factor | What the market offers today | Source |
|---|---|---|
| Prizes and events | Hackathons compete on prize pools and 24–48 h events; prize amount is the top reason Devpost participants pick a hackathon | [student motives][N-s], Devpost 2023 survey (organiser) |
| Time required | Hackathons 24–48 h; Kaggle weeks; Forage 2–6 h; Extern 10–15 h/week | [student motives][N-s], [competitive analysis](market-research/competitive-analysis.md) |
| Realness of the brief | Forage: employer-designed simulations; HackerRank: standard puzzles; coursework: no client | Published pages |
| Feedback depth | Forage: compare with a model answer; HackerRank: a score; hackathons: judging for prizes | Published pages |
| Verification of individual work within a team | The four benchmark offers do not describe the combined contribution-verification certificate proposed by SkillBridge. Riipen has partial overlap. NUWE: not publicly disclosed in the reviewed material. | [Dated feature comparison](market-research/contribution-verification-review-2026-10-13.md) |
| Integrity | Cheating attempts in entry-level assessments rose from 15% to 40% (CodeSignal, Feb 2026, vendor); ISE: employers meeting cheating doubled 7% → 15% (Dec 2025, independent) | [company motives][N-c] |
| Price to student | Forage, HackerRank certifications, Kaggle, student hackathons: free | [willingness to pay][N-w] |
| Who pays | Employers or universities pay the platforms (HackerRank from $79/month; Riipen FuturePath $11.67/hour per student; hackathon sponsorship $500–$50k+) | [company motives][N-c] |

**Conventions we challenge:** free student access in benchmark offers such as
Forage; completion certificates in self-checked simulations; shared team results
without an inspectable account of each member's work. These are comparison
patterns, not universal features of every competitor.

## ERRC Grid

**Certification rule, revised 2026-10-13:** students can fail. Only results
meeting the published challenge requirements, with individual work verified,
are eligible for certification. The engineer confirms eligibility before the
€15 offer; failed results stay private and receive no certificate or
certification charge. See the [eligibility rules](experiment-card.md#certification-eligibility).
Eligibility checks add reviewer work beyond the calibration sample; the cost
saving below remains a hypothesis to measure, not a demonstrated saving.

| Action | Strategic move | Assumption challenged | Cost effect | Buyer value effect | Evidence status | What must be verified |
|---|---|---|---|---|---|---|
| Eliminate | Prize pools, venues and mandatory weekend-long events | "A challenge needs prizes and an event to attract students" | Removes prize and event expenditure; brief preparation, scoring, verification and feedback still cost time | Students can participate without an event schedule; companies fund evidence of skill instead of event logistics | **Mixed:** clear scope and career relevance each 11/17 versus payment 3/17 in our survey; prize appeal remains counterevidence in hackathon research [N-s] | Whether students start and finish without prizes; actual event costs avoided |
| Reduce | Challenge length to 2–7 h (4 h in the pilot); routine first-pass grading through automated tests and an AI rubric | "Useful evidence needs a long project and full manual grading of every entry" | Aims to reduce student time and repetitive grading; retains the engineer sample, eligibility checks and feedback for every certified result | A bounded task fits stated capacity and can be repeated around coursework | **Capacity evidence:** 12/17 can give ≤4 h/week. Completion, score agreement and net savings are untested | Completion, paired AI/engineer scores and total review time, including all retained work |
| Raise | Depth of human feedback and confidence in authorship: engineer-written feedback on every certified result; individual eligibility checks and the planned live debriefs | "A score or badge alone is sufficient evidence" | Adds work for each certification request and every certified student, plus debriefs; cost is not confined to top submissions | Students receive actionable feedback; recruiters can inspect who did the work and why it passed | **Conditional evidence:** V2-S01 wants specific human feedback; V2-R01 values work and an engineer's note ([findings](validation/v2-findings-2026-10-12.md)). Delivery cost and trust remain untested | Feedback coverage for every certificate, attribution quality, reviewer capacity and recruiter response |
| Create | A portable, company-calibrated challenge certificate connecting the work, rubric, individual-contribution record and engineer feedback; earned by passing, shared only by choice | "Students must rely on a CV, completion badge or shared team result to explain their own work" | Profile and sharing can be software; issuing another certificate still requires individual verification and engineer feedback | A reusable piece of work evidence for applications, with the student's contribution inspectable | **Proposed difference from four benchmark offers**, with partial overlap elsewhere; NUWE: **not publicly disclosed** ([feature comparison](market-research/contribution-verification-review-2026-10-13.md)). Employer value remains a hypothesis | Whether recruiters use the bundle in shortlisting and whether eligible students pay for it (Arms B and A) |

## How the four moves work together

Eliminate removes event spending. Reduce limits the task and automates routine
scoring. Raise spends human attention on verification and feedback for every
certified student. Create packages that work into evidence the student can
reuse in applications. Raise describes the quality of assessment; Create
describes the portable result produced by it.

**New-demand hypothesis:** attract students who currently stay with coursework
or personal projects and do not take part in long events or placements, along
with employers unwilling to organise an event for early screening. The intended
new offer is a short route to inspectable work evidence, rather than another
prize competition. The capacity and contribution findings support investigating
this group; they do not establish that these people will switch or participate.

The trade-off is explicit: fewer prizes and less event experience, but more
feedback and attributable evidence. Students still face an optional €15 fee
against free alternatives. Reduced event and grading work must offset the
added verification and feedback effort for total company cost to fall.

## Engineer workload and cost

**Coverage rule:** every certified result includes engineer-written feedback
about that student's work and contribution, regardless of rank. A team can
share a code review, but each student's certificate still needs individual
eligibility confirmation and feedback. The five-submission calibration sample
does not cap the number of students receiving feedback.

| Work | What must be counted | Current evidence |
|---|---|---|
| Setup | Brief, examples, rubric and pass requirements | Proposed, not timed or signed off |
| Calibration sample | Top three distinct submissions plus two from the lower half; all available submissions if fewer than five | At the interview estimate of 20 min per review, five reviews are about 100 min; not an observed duration |
| Additional eligibility work | Performance/authorship checks outside the sample, individual checks within teams, and disputes; include requests that fail or do not lead to payment | Scope and time to confirm before the pilot |
| Feedback | Specific written feedback on **every certified result** | Coverage decided; additional writing time not yet measured |
| Other human work | Live debriefs, coordination, corrections and rework | Time to record, including the engineer's stated concern about meetings |

**Total engineer time = setup + sample reviews + additional eligibility work + feedback + debriefs + coordination/rework.** Log each minute once by activity;
reuse a review when it serves several purposes. If its timed duration already
includes writing feedback, do not add that same writing time again. Record
distinct project submissions separately from individual students/certificates.

For **10 solo submissions and 3 certificates**, the five-review sample alone
is estimated at **100 minutes**, plus the other work above; three paid results
produce **€45 gross revenue**. This is not a one-hour workload or evidence of
profitability. If all 10 certify, all 10 receive engineer-written feedback;
the sample stays at five but total workload does not stay fixed. The engineer's
original estimate covered reviewing three solutions, not this entire service
([V2-E01 Q3–Q4](validation/v2-interviews-2026-10-12.md#v2-e01-q3)).

Record actual engineer minutes, operator time, automation costs and cash costs
in the pilot. Value donated engineer time explicitly before claiming a cost
advantage. Compare against the company's stated alternative for an equivalent
cohort and assessment quality; approval of €15 or a positive recruiter answer
does not establish lower operating cost. Reviewer capacity and the time/cost
baseline must be agreed before committing to the student cohort; no rate or
saving is invented here.

## Value innovation hypothesis

SkillBridge aims to lower event and routine-grading costs and student time,
while raising the value of each result through company calibration, verified
contribution and engineer-written feedback on every certificate. **Net savings
are conditional on the full workload above**, not a consequence of using AI.

The demand tests remain ≥30% of submitting students paying €15 (at least 10
submitting students) and ≥3 of 5 recruiters saying the bundle changes or
supports shortlisting. Fewer than 10 students is inconclusive; the
[experiment card](experiment-card.md) retains the existing decision branches.
These test demand and stated credibility, not cost savings. Even if both pass,
do not claim lower company cost unless the complete cost comparison supports it.

This is a strategy ready to be challenged, not a validated blue ocean or
confirmed business model. The net-cost advantage fails if retained review and
feedback costs erase the proposed savings at comparable assessment quality.

## Critical outstanding validation points

1. Recruiters treat the score and contribution record as credible enough to
   shortlist on (A3.1); vendor surveys say yes, behaviour studies say rarely.
2. Students pay for the certified result despite free alternatives (A1.3);
   research finds students pay for prep, rarely for the signal itself
   ([willingness to pay][N-w]).
3. Students finish a 4-hour challenge without a prize (A1.2).
4. AI rubric scores agree with the engineer's closely enough to skip full human
   review (A2.3).
5. A company will provide a real brief and sign off a rubric (A2.1).
6. The engineer can deliver the sample, eligibility checks and feedback on every
   certified result within the agreed capacity; net cost is below the agreed
   comparison after accounting for human time (A2.2).

## Evidence boundaries

- **Real evidence:** students' difficulty proving contribution and experience
  beyond coursework, their short time capacity and their wish for clear scope and
  feedback (survey n = 17, pilot n = 11, two student interviews UV-S01/S02).
  V2 interviews (one student, one recruiter, one engineer) and three
  one-on-ones add stated, conditional willingness to pay €15, recruiter trust
  in the full evidence bundle but not a bare score, and a view from all three
  one-on-one interviewees that companies should pay
  ([claims changed](validation/claims-changed.md)).
- **Desk research:** competitor offers, market prices, cheating trends and the
  Stanford certificate trial ([deep research notes][N]); the
  [current contribution comparison](market-research/contribution-verification-review-2026-10-13.md)
  records the proposed distinction and partial overlap. Most platform outcome
  figures are vendor claims; market-wide exclusivity is not established.
- **Team or AI inference:** the €15 price, the 30% and 3-of-5 thresholds, the
  value-curve scores and the claim that employers value attributed team work.
- **Contradictions:** prizes motivate hackathon participants; free alternatives
  compete for students; paying after seeing a good score could look like buying a
  certificate. The revised rule requires a passing, individually verified
  result before payment is offered, and the certificate shows the actual score.
  Whether recruiters find this credible remains untested.

[N]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/
[N-c]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/company_motives.md
[N-s]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/student_motives.md
[N-m]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/market_landscape.md
[N-r]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/credential_credibility.md
[N-w]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/willingness_to_pay.md
