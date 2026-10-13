# Eliminate-Reduce-Raise-Create Grid

**Status:** Confirmed value innovation hypothesis requiring evidence (v2, 2026-10-12).
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
| Proof of individual contribution | Solo tests prove the individual; not found in the published materials of Forage, HackerRank, Devpost or Kaggle; NUWE unverified | [market landscape][N-m] |
| Integrity | Cheating attempts in entry-level assessments rose from 15% to 40% (CodeSignal, Feb 2026, vendor); ISE: employers meeting cheating doubled 7% → 15% (Dec 2025, independent) | [company motives][N-c] |
| Price to student | Forage, HackerRank certifications, Kaggle, student hackathons: free | [willingness to pay][N-w] |
| Who pays | Employers or universities pay the platforms (HackerRank from $79/month; Riipen FuturePath $11.67/hour per student; hackathon sponsorship $500–$50k+) | [company motives][N-c] |

**Taken for granted by the industry:** the student pays nothing; the certificate
proves completion, not quality; team results are shared, not attributed.

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
| Eliminate | Prize pools and weekend-long events: no prizes, no venues, no 24–48 h hackathons | "Students participate for prizes" | No prize budget or event logistics for companies or for us; a company's cost becomes one brief, one rubric sign-off, a sampled check of the AI scores and feedback on certified results | Students keep their evenings and weekends; the reward is the scored result itself | **Contradicted in part:** prize amount is the top hackathon-choice reason (Devpost 2023, organiser survey); our survey shows clear scope (11/17) and career relevance (11/17) far above payment (3/17) | Whether students start and finish a challenge with no prize |
| Reduce | Time per challenge to 2–7 h; company judging time by letting automated tests and an AI rubric score every submission, with the engineer scoring a sample (the top three plus two from the lower half), confirming eligibility for certification requests and writing feedback on every certified result, whatever its rank | "A credible result needs a long project and a human grading every entry" | Intended reduction in engineer hours, including eligibility checks and feedback; lower student time cost | Fits stated capacity: 12/17 can give ≤4 h/week, 0 can give 8+ | **Evidence** for capacity (survey). Completion risk: 15% of registrants submitted in one Devpost online hackathon; MOOC completion 3% overall vs 46% for payers (Science 2019) | Completion rate on a 4 h challenge; AI vs engineer score agreement; total review time |
| Raise | Verifiability: per-member contribution from commits **plus** peer ratings, and a 10-minute live debrief for top results; written feedback on every certified result | "A certificate or a final output is enough proof" | Higher cost per top submission (debrief and engineer time) | Answers the recruiter's "what did *you* do?" and the AI-cheating worry | **Evidence** for the need: 14/17 struggle to explain contribution; peer assessment cut free-riding complaints from 26% to 7% in one study; git data alone misses silent or absent members ([student motives][N-s]). AI cheating rising (see baseline) | That the debrief scales; that students accept contribution scoring |
| Create | A company-calibrated score with a verified individual-contribution record, stacked on a portable profile and shareable to LinkedIn and Europass | "Credentials prove completion, not quality, and team work cannot be attributed" | Low marginal cost once the rubric exists; profile and sharing are software | A signal the market lacks: showing certificates on LinkedIn raised new jobs by about 6% and by about 12% for the weakest candidates (Athey & Palikot, Stanford randomised trial, 2024–2025, with Coursera learners
without a degree in developing countries, not Spanish students) ([credential credibility][N-r]) | **Gap evidenced in published features only:** not found for Forage, HackerRank, Devpost or Kaggle; NUWE's contribution model is unpublished and unverified ([market landscape][N-m]). **Employer value: Hypothesis.** Skills-based hiring changed fewer than 1 in 700 hires (HBS & Burning Glass, 2024) | Whether recruiters shortlist on it (experiment card, Arm B) |

## Value innovation hypothesis

By dropping prizes and long events and letting automated tests and AI do
first-pass scoring, SkillBridge cuts the cost of a challenge for companies and
the time cost for students, while raising what the result is worth: a score
calibrated to a real company's bar, with each student's contribution and an
integrity check on record. It is falsified if fewer than 30% of submitting
students pay €15 for the certified result (with at least 10 submissions; fewer
is inconclusive), or fewer than 3 of 5 recruiters say
it would change or support a shortlisting decision
([experiment card](experiment-card.md)).

This remains a hypothesis, not a validated blue ocean or confirmed business model

## Critical outstanding validation points

1. Recruiters treat the score and contribution record as credible enough to
   shortlist on (A3.1); vendor surveys say yes, behaviour studies say rarely.
2. Students pay for the certified result while every alternative is free (A1.3);
   research finds students pay for prep, rarely for the signal itself
   ([willingness to pay][N-w]).
3. Students finish a 4-hour challenge without a prize (A1.2).
4. AI rubric scores agree with the engineer's closely enough to skip full human
   review (A2.3).
5. A company will provide a real brief and sign off a rubric (A2.1).

## Evidence boundaries

- **Real evidence:** students' difficulty proving contribution and experience
  beyond coursework, their short time capacity and their wish for clear scope and
  feedback (survey n = 17, pilot n = 11, two student interviews UV-S01/S02).
  V2 interviews (one student, one recruiter, one engineer) and three
  one-on-ones add stated, conditional willingness to pay €15, recruiter trust
  in the full evidence bundle but not a bare score, and a view from all three
  one-on-one interviewees that companies should pay
  ([claims changed](validation/claims-changed.md)).
- **Desk research:** competitor offers, market prices, cheating trends, the
  Stanford certificate trial and the absence of team-attribution platforms
  ([deep research notes][N]). Most platform outcome figures are vendor claims.
- **Team or AI inference:** the €15 price, the 30% and 3-of-5 thresholds, the
  value-curve scores and the claim that employers value attributed team work.
- **Contradictions:** prizes motivate hackathon participants; every alternative
  is free to students; paying after seeing a good score could look like buying a
  certificate. The revised rule requires a passing, individually verified
  result before payment is offered, and the certificate shows the actual score.
  Whether recruiters find this credible remains untested.

[N]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/
[N-c]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/company_motives.md
[N-s]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/student_motives.md
[N-m]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/market_landscape.md
[N-r]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/credential_credibility.md
[N-w]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/willingness_to_pay.md
