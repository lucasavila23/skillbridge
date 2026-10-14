# Claims changed by real-user evidence

**2026-10-13.** Answers the Challenge II feedback: "Talk to a handful of real
target users, both students and small business owners, and write down which of
your claims changed", and "the link between what changed and what you learned
isn't clear" ([feedback response](../feedback-response.md#challenge-ii-venture-skeleton-v01-65--80)).

Each row reads left to right: what we believed, what real people told us, and
what we changed. Interview sources are participant reports, not observed
behaviour. Samples are never added together because participants may overlap.

## Who we talked to

| Round | Who | n | Strength | Record |
|---|---|---|---|---|
| Sep interviews (15–20 Sep) | 2 IE students, 2 small-business respondents (Baya, Nolita) | 4 | Medium: teammate-reported | [records](interviews-2026-09-22.md) |
| Student survey (from 22 Sep) | Students, unscreened | 17 | Medium: stated | [summary](survey-summary-2026-10-12.md) |
| Pilot (1 Oct) | 3rd-year software students, Madrid | 11 | Medium: aggregate only | [assessment](../market-research/pilot-assessment-2026-10-01.md) |
| V2 interviews | 1 IE CSAI student, 1 tech recruiter, 1 company engineer | 3 | Medium: one per role | [records](v2-interviews-2026-10-12.md) |
| One-on-ones | 1 graduate (outside target), 1 IE student, 1 recruiter | 3 | Low–medium: undated, direct price questions | [record](one-on-one-interviews-2026-10-12.md) |
| Company interview | 1 fintech recruiter (Deem Finance) who screened interns in the last 12 months | 1 | Low–medium: undated, interviewer and consent not recorded | [record](sources/company-interview-deem-finance.md) |

## What changed

| # | Claim before | What people told us | What changed | Now in |
|---|---|---|---|---|
| 1 | **v1:** small businesses will hand paid projects to student teams; business trust is the riskiest assumption | Nolita (UV-B02): no current project, and even cheap work costs time to brief and review. No business reached a formal pitch. | **Pivot (12 Oct):** the business side stops being the customer. Companies that already hire juniors set short challenges instead. | [v1 archive](../archive/v1-paid-projects/README.md), [opportunity](../opportunity.md) |
| 2 | Students join for the money and the experience | Survey Q5: clear scope 11/17, career relevance 11/17, **payment 3/17**. | Paid client work dropped; the reward is proof of skill. | [opportunity](../opportunity.md), [ERRC](../ERRC.md) Eliminate |
| 3 | Students can commit to a multi-week client project | Survey Q6: 12/17 can give 4 h a week or less, 0 can give 8+. One-on-ones: 3–5 h and 4–6 h. V2-S01: four hours clashes with deadlines. | Challenges sized to 2–7 h; the pilot uses a 4-hour time box. | [ERRC](../ERRC.md) Reduce, [experiment card](../experiment-card.md) |
| 4 | The core student pain is getting experience | Survey Q2: **explaining personal contribution 14/17**, showing work beyond coursework 12/17. V2-S01 froze when asked which parts they wrote. | The product centres on a **verified individual-contribution record**. | [opportunity](../opportunity.md), [ERRC](../ERRC.md) Create |
| 5 | "Nobody combines real projects, teams and verification" | **Desk evidence, not an interview:** the 13 Oct feature review distinguishes individual-contribution verification from rosters and solo tests; Riipen has partial overlap. | Proposed differentiation is verified individual work within a company-calibrated challenge certificate, not a blanket claim that no competitor checks contribution. NUWE: **not publicly disclosed** in the reviewed material. | [Dated feature comparison](../market-research/contribution-verification-review-2026-10-13.md) |
| 6 | The score is the product ("82/100") | V2-R01: "82 out of 100 means nothing to me on its own." OO-R01 wants the rubric, company review, work sample and a benchmark. [DF-R01](sources/company-interview-deem-finance.md) Q12: their own rubric, an engineer's note, the code and the candidate's rank; "a bare number would be ignored". | **Certified result = evidence bundle** (work, company-named rubric, contribution record, engineer's note), never a bare score. Arm B shows the full bundle. | [experiment card](../experiment-card.md) Arm B, [v2 findings](v2-findings-2026-10-12.md#consequences-for-the-current-offer) |
| 7 | The engineer reviews only the top submissions | V2-S01 would pay €15 if "an actual engineer wrote it, not generated" and the feedback is specific. | **Every paying student gets engineer-written feedback.** | [experiment card](../experiment-card.md) Arm A step 4 |
| 8 | Results appear on a public profile; the 12 Oct offer allowed certification at any score | V2-S01: "If a bad score is attached to my name somewhere public, that's worse for me than…"; and if "the money is what gets you the certificate rather than the work, then it's worthless". | **Revised team decision, 13 Oct:** private by default, sharing is optional, and certification can be failed. Only passing, individually verified results are eligible for the €15 offer; payment cannot buy a pass. Certificates show the actual score. Recruiter acceptance remains untested. | [certification eligibility](../experiment-card.md#certification-eligibility), [decision history](v2-findings-2026-10-12.md#consequences-for-the-current-offer) |
| 9 | The AI rubric can rank submissions; the engineer checks the top | V2-E01 Q4: check a low-ranked submission before trusting the AI ranking. | The engineer scores five distinct submissions, **including two from the lower half**, to measure AI–engineer agreement; review all if teams produce fewer than five. This sample does not limit feedback for certified students. | [experiment card](../experiment-card.md) Arm A step 5 |
| 10 | The critical third persona is a wary small-business owner | The riskiest assumption moved to whether recruiters trust the credential (rows 1 and 6). | **Skeptical Verifier** (recruiter) replaces the Once-Bitten Owner as a critical persona. | [personas](../personas/README.md) |
| 11 | Students pay first (revenue hypothesis 1) | All three one-on-one interviewees say **companies should pay** most or all; students at most a small fee. Desk research: free alternatives compete with our student fee. V2-R01 links company spend to replacing take-home review. [DF-R01](sources/company-interview-deem-finance.md) Q15–16: maybe, **per hire or per challenge**, not a subscription, from the campus and employer-branding budget (HR director signs), replacing part of a ~€5,000 datathon sponsorship that hired no one. | **Not yet reversed.** The ranking stays until the pilot decides; the company price is defined alongside the pilot so the "students fail, recruiters pass" branch can start at once. | [assumptions](../assumptions.md#revenue-hypotheses-ranked-by-the-team), [experiment card](../experiment-card.md#decision-rule) |

## What did not change, and why

- **The student Job to Be Done.** Every round supports it; it is
  solution-neutral, so it survived the pivot ([JTBD](../jtbd.md)).
- **The €15 price and the 30% / 3-of-5 thresholds.** Interview answers are
  stated and conditional; only the pilot (16–30 Oct) can move them. They were
  fixed before the test and are not adjusted after.

## What is still unknown

Real payment, real challenge completion, a signed company brief and rubric,
AI–engineer score agreement, and any hiring decision made on a certified
result. The [experiment card](../experiment-card.md) tests the first two
directly; the [stakeholder map](../stakeholder-map.md) lists the rest.
