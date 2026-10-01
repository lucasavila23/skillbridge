# Analysis and how to challenge the estimate

**2026-10-01 · Working hypothesis · Madrid region**

The headline is **about 2,000 potential student participants in one academic
year**. The unrounded model gives 1,950. This is a student-side opportunity
estimate conditional on a suitable offer, not a forecast of the first year's
customers. The [summary](README.md) contains the complete six-step calculation.

## Scope and unit

The [project scope](../../project-scope.md) identifies students as the primary
market. We therefore count students, rather than starting with all small
businesses or adding the two sides of the marketplace together.

Use an academic year as the participation window. The 2024/25 enrolment stock is
the latest year in the downloaded source and is held constant as a planning
proxy for 2026/27; there is no measured growth adjustment. A4 converts that stock
into students ready to join during one year. It does not imply 2,000 new students
every month, a new graduating cohort, or 2,000 additional users every year.

The first estimate focuses on undergraduate software/web/data programmes and
years 2–4. It leaves first-year students, postgraduate students, vocational
training, bootcamps, graduates and career changers outside the model. These may
be future markets. The source's institutional coverage also needs a campus
check before treating the anchor as an exact regional headcount.

## Why these four assumptions

| Assumption | Reason for the base choice | What could make it wrong | How to replace it |
|---|---|---|---|
| **A1: 10% relevant tech studies**; explore 5–15% | One in ten is a simple working guess for a narrower software/web/data segment within an all-subject undergraduate population. No measured local subject share supports 10%. | Counting all engineering as software would inflate it; excluding relevant data or interdisciplinary degrees could reduce it too far. A degree label also does not prove delivery skill. | Agree the included programme list, obtain matching enrolment counts, deduplicate dual degrees and divide by the same population used for the anchor. |
| **A2: 75% in years 2–4**; explore 60–80% | Three of four years is the simple starting model for an evenly distributed four-year course. Equal cohorts and four-year duration are assumptions. | Dropout, repeat years, part-time study and longer or dual degrees alter the distribution. | Request year-of-study counts within the included programmes. Count years 2–4 directly rather than equating all non-first-years with the target. |
| **A3: 50% match the experience gap**; explore 30–70% | Half is a deliberately broad placeholder for the joint condition of no relevant internship and no effective professional referral route. | Many later-year students may already have internships; some students without internships can still obtain referrals. Our two interviewees do not establish either prevalence. | Screen a broad sample of A2 students. Ask about completed/current relevant internships and a concrete contact able and willing to refer them to a relevant employer. Record both conditions per person. |
| **A4: 20% ready to commit in a year**; explore 10–30% | One in five allows for competing coursework, other paid work, skill gaps, timing and alternatives. It is an unmeasured combined readiness-and-willingness rate under a suitable offer. | Interest may collapse when dates, pay, teammates or support are concrete. Offers at a different time or with different terms may get different uptake. | Make real offers to eligible students, review relevant work, and observe a recorded availability commitment and acceptance of the actual terms. Measure the full denominator. |

For A3, an effective referral route means a specific professional contact able
and willing to make a relevant introduction; it does not mean having zero
LinkedIn connections. This is a proposed operational definition of the project's
"no network" segment. GPA is not an additional eligibility cut: the original
"normal student" framing is about access to opportunity, not an agreed grade
threshold. Confirm these definitions before fieldwork.

Each rate is conditional on the previous filters. A3 measures the two access
conditions together; do not multiply separate guessed internship and network
rates. A4 already includes basic readiness, so do not add another skill filter
without revising its definition and measuring the changed denominator.

## What the existing evidence contributes

The [September interview findings](../validation/findings-2026-09-22.md) contain
two teammate-reported IE student accounts. They describe difficulty presenting
project experience, a need for integration/deployment help and limits around
exams. These support testing the problem and commitment conditions; they do not
validate the four percentages, degree-year distribution or annual participation.
Neither student has demonstrated a SkillBridge campaign commitment or delivery.

The Baya account describes a past digital task and conditional interest. Nolita
reports no current project. Neither is a sale or a denominator for business
conversion. The [existing Experiment Card](../experiment-card.md) still governs
the ten-business charter-and-deposit test and its separate extension rule.

The estimate assumes enough appropriate offers exist to reveal student demand.
Actual participation will also be limited by distribution, funded project seats,
matching, supervision and delivery capability. Team size, campaign frequency,
pricing and platform fees are not established here, so the student count is not
converted into projects, revenue or a claimed obtainable market.

## Sensitivity: which assumptions matter

Change one input at a time, holding the other three at their base values:

| Input varied | Low input → students | Base input → students | High input → students |
|---|---:|---:|---:|
| A1: relevant studies | 5% → 975 | 10% → 1,950 | 15% → 2,925 |
| A2: years 2–4 | 60% → 1,560 | 75% → 1,950 | 80% → 2,080 |
| A3: experience gap | 30% → 1,170 | 50% → 1,950 | 70% → 2,730 |
| A4: commitment | 10% → 975 | 20% → 1,950 | 30% → 2,925 |

All four rates have the same proportional effect: halving any one halves the
result. A1 and A4 span the widest relative ranges chosen here. A1 is best checked
with administrative data; A4 needs behavioural evidence. Test A4 first in the
field, while improving the population and subject counts.

Setting **all** inputs low gives 234; setting all high gives 6,552. These are
stress cases, not a confidence interval, probability distribution or separate
headline estimates. They show why presenting 1,950 as a precise forecast would
be misleading. Using the exact anchor instead of rounding produces about 1,963,
which leaves the headline at about 2,000; behavioural uncertainty dominates that
rounding difference.

## Proposed validation plan — not yet run

### 1. Check the population and eligibility

Check campus coverage and replace A1/A2 with programme and year counts from
registrars or compatible official tables. Use the same academic year and
geography throughout. In particular, reconcile Madrid campuses associated with
institutions outside this dataset before adding them; do not add entire
multi-campus universities to the regional denominator.

Recruit from programme/class lists where possible, rather than only people
already interested in SkillBridge. Screen for A3 before presenting the offer.
Record eligible respondents, ineligible respondents and unknown/non-responses
separately. Non-response does not establish absence of an internship or network.
The existing two IE interviews are exploratory evidence, not a regional sample.

### 2. Challenge A4 with concrete offers

For an initial diagnostic, aim for **100 unique A3-eligible students** across at
least four institutions, including public and private universities, different
years and relevant programmes. Use IE as an access point, not as the whole
Madrid sample. This is a proposed diagnostic sample, not a statistical guarantee
of regional representativeness or a claim that access has been secured.

Before recruitment, define a bounded campaign offer with a real business brief,
dates, expected hours, compensation, portfolio permission, team arrangement and
named support. Those terms remain to be set; the illustrative prototype price
is not a market observation. Secure sufficient opportunities to avoid measuring
an artificial shortage of seats. If only a few real opportunities exist, start
smaller, report the actual denominator, and do not pretend that a waitlist of
100 people has tested 100 offers.

Count a **readiness commitment** only when the student, within the proposed
10-day offer window, does all of the following:

1. Supplies a relevant work sample that passes a predefined basic capability
   review for the offered role.
2. Records availability compatible with the campaign dates and expected hours.
3. Attends a briefing and explicitly accepts the scope, compensation and role
   conditions, subject to the final team match.

Use unique eligible students who received a suitable offer as the denominator,
including refusals and non-responses. Also retain the full outreach count and
reasons offers were unsuitable, so a narrow selection cannot be described as
the region's whole eligible pool. Availability failure under otherwise suitable
terms is an A4 failure, not a reason to remove someone from the denominator.

Track later kickoff, retention and client acceptance separately. Readiness is
the model's endpoint; it is not evidence of completed delivery. This student
diagnostic does not replace or change the business experiment's decision rule.

### 3. Update the number instead of defending it

At the current base rates, A4 predicts about **20 commitments per 100 eligible
students offered a suitable opportunity**. If there are 10, substituting 10%
reduces the model to 975 (about 1,000); if there are 30, substituting 30% increases
it to 2,925 (about 3,000). These are mechanical updates, not automatic proof or
rejection of regional market size. Preserve refusals and their reasons.

A single 10-day offer wave only challenges commitment under its timing and
terms. To estimate an academic-year rate, repeat across relevant term/exam
windows and track unique students through the year, counting each person once
even if offered several campaigns. Report institution, programme and year
coverage; use population weights only when defensible counts and sampling are
available. Do not extrapolate a convenience-sample conversion rate as if it were
a representative census.

Record recruitment source, anonymous student ID, campus, programme, year,
eligibility answers, offer terms/date, work review, availability, briefing,
acceptance date and refusal/withdrawal reason. Retain missing values. Publish
numerator, denominator, period and evidence links before revising A1–A4.

**Current evidence status:** one official population anchor; four unvalidated
rates; no new participants contacted, commitments observed or test results
created in this research session.
