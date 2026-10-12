# Press release opener (Working Backwards), v2

**2026-10-12.** A future customer story written before the product exists, as
the course's lean press-release format asks. The evidence loop below it says
what is known and what would prove it wrong. Quotes are illustrative.

---

## SkillBridge lets tech students prove what they can do, and exactly what they did, in an afternoon

*Real company challenges, scored against the company's own bar, with every
team member's contribution on the record: the proof that coursework and free
certificates cannot give.*

**MADRID, September 2027.** SkillBridge today opened its challenge platform to
university tech students in Spain. Students spend two to seven hours on a short,
real brief from a SaaS, engineering or data company, alone or in a small team,
and get a score calibrated to that company's rubric, written feedback from one of
its engineers, and a verified record of their own contribution that they can add
to their CV and LinkedIn.

**The problem.** Internship applications ask students for work beyond coursework
and for an account of what they personally did. Most cannot give one: their
projects were graded only by classmates and staff, and team work hides who did
what. Free certificates prove a course was finished, not that the work was good,
and employers are growing wary of remote tests as AI-assisted cheating rises.

**The solution.** Each SkillBridge challenge is a bounded piece of real work
with a clear scope and deadline. Automated tests and an AI rubric score every
submission; a company engineer signs off the rubric, reviews the top results and
holds a ten-minute debrief to confirm the student did the work. For teams,
contribution comes from the commit history plus teammates' ratings.

> "We stopped grading a hundred take-homes. The scores matched our engineers'
> judgement, and the debrief told us who had really built it."
> **Head of data engineering, a Madrid SaaS company (illustrative)**

**How it works.** Pick a challenge that matches the role you want, work on it
in an evening or a weekend afternoon, submit, see your score for free, and
certify the result if you want it on your profile. Each certified result stacks
on a profile recruiters can open to see the brief, the rubric and your part.

> "In interviews they always asked what I did on the group project. Now I send
> the link and talk them through it."
> **Third-year software engineering student, Madrid (illustrative)**

Find your first challenge at skillbridge.example.

---

## Evidence loop (outside the press release)

| Claim in the release | Status | Source |
|---|---|---|
| Students struggle to show work beyond coursework and explain their contribution | **Evidence (unscreened sample, n = 17)**: 12/17 and 14/17 | [survey summary](validation/survey-summary-2026-10-12.md) |
| Their projects are graded only by classmates and staff | **Evidence (unscreened sample, n = 17)**: 9/17 | [survey summary](validation/survey-summary-2026-10-12.md) |
| Two to seven hours fits students | **Evidence (unscreened sample, n = 17)**: 12/17 can give ≤4 h a week; 0 can give 8+ | [survey summary](validation/survey-summary-2026-10-12.md) |
| The market context: 24.5% under-25 unemployment in Spain; new grads 7% of Big Tech hires | **Desk research** (INE Q1 2026; SignalFire 2025) | [internship struggles][N-i] |
| AI cheating makes employers wary of remote tests | **Desk research** (ISE Dec 2025 independent; CodeSignal Feb 2026 vendor) | [company motives][N-c] |
| Not found in the published materials of Forage, HackerRank, Devpost or Kaggle; NUWE unverified | **Desk research, bounded** | [market landscape][N-m] |
| Companies will post briefs and engineers will review | **Hypothesis** | [assumptions](assumptions.md) A2.1–A2.2 |
| Recruiters trust the score; students pay to certify | **Hypothesis: the riskiest assumption** | [experiment card](experiment-card.md) |

**What would prove this release wrong:** students do not pay for the certified
result, recruiters do not change a shortlist because of it, or no company
provides a brief. Each has a precommitted test and decision rule in the
[experiment card](experiment-card.md).

[N-i]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/internship_struggles.md
[N-c]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/company_motives.md
[N-m]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/market_landscape.md
