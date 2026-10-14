# Value curve (strategy canvas), v2

**2026-10-12.** Offering level from 1 (low) to 5 (high) on the factors the
challenge and assessment market competes on. **Scores are team judgement** from
published offers and the [deep research notes][N]; they are not measured. The
moves behind SkillBridge's curve are in the [ERRC grid](../ERRC.md).

**Contribution clarification, 2026-10-13:** SkillBridge's score represents the
intended offer, not measured verification quality. The feature checks what a
person actually did within a team. The [current source comparison](contribution-verification-review-2026-10-13.md)
separates that from solo assessment and team membership, records Riipen's
partial overlap, and labels NUWE **not publicly disclosed**. The chart does
not establish that contribution verification is unique to SkillBridge.

![Strategy canvas: SkillBridge v2 against Forage, HackerRank certification, Devpost hackathons and coursework](value-curve.png)

Source chart: [value-curve.svg](value-curve.svg). Kaggle and NUWE are discussed
below but left off the chart to keep it readable.

## Scores and reasons

| Factor | SkillBridge v2 | Forage | HackerRank cert. | Devpost hackathon | Coursework |
|---|---|---|---|---|---|
| Price to student | 2: €15 optional certified result (test price) | 1: free | 1: free certifications | 1: student hackathons free | 1: no extra cost |
| Prizes and events | 1: **eliminated** | 1: none | 1: none | 5: prize pools, 24–48 h events | 1: none |
| Time required | 2: 2–7 h | 2: 2–6 h | 1: short timed test | 4: 24–48 h | 5: weeks or a semester |
| Realness of brief | 4: real company brief | 3: employer-designed simulation | 1: standard puzzles | 3: sponsor themes or APIs | 2: academic exercise |
| Feedback depth | 4: rubric breakdown and engineer's written feedback (**raised**) | 1: compare with a model answer | 2: a score | 2: judged for prizes | 3: grade and some comments |
| Individual contribution proof | 5: commits plus peer ratings plus debrief (**created**) | 2: solo but unverified | 3: solo, proctored | 1: team result | 2: often peer-graded |
| Integrity checks | 4: live debrief for top results (**raised**) | 1: none published | 3: proctoring, but AI cheating rising | 2: judges see a demo | 2: varies |
| Employer calibration | 4: rubric signed off by the company (**created**, credibility untested) | 3: employer brand on the certificate | 3: tests built on recruiting data | 2: sponsor judging | 1: none |

## Reading the curve

- **Divergence:** SkillBridge drops prizes and events and stays low on time and
  price, then rises on proof of contribution, integrity, feedback and employer
  calibration. This is the proposed value-innovation shape in the [ERRC](../ERRC.md),
  not a measured superiority claim across all alternatives.
- **Where we lose:** the €15 fee competes with free benchmarks, including
  Forage. Do not extend the chart's price comparison to every alternative:
  paid courses also exist and NUWE's student pricing is not publicly disclosed
  in the reviewed material ([competitive analysis](competitive-analysis.md)).
- **Off-chart alternatives:** Kaggle (free, data science only, leaderboard rank,
  weeks of work); NUWE (Barcelona, company challenges for CaixaBank, Oracle and
  Schneider Electric; €739k raised), the closest local competitor, whose student
  pricing and individual-contribution verification are **not publicly disclosed**
  in the material reviewed ([feature comparison](contribution-verification-review-2026-10-13.md)).

## Four actions and cold start

**Four actions in one line:** eliminate prizes and weekend events, reduce time
per challenge and company judging hours, raise verifiability and feedback,
create a company-calibrated score with a verified individual-contribution record
([ERRC grid](../ERRC.md)).

**Cold-start principle:** start with a dense niche and create both sides by hand,
doing things that do not scale until we understand what makes the marketplace
work (the course's Uber and Airbnb principles). A two-sided platform has a
chicken-and-egg problem: students come for company names, companies come for
students.

| Cold-start move | Why | Evidence status |
|---|---|---|
| One university, one city: IE and Madrid tech students first | Dense, reachable niche; we already have 17 survey respondents and classmates | Reachability: Evidence (survey). Fit to target profile: partly unknown ([participant fit](../recruitment.md#participant-fit-against-the-target-user)) |
| Secure the harder side first: one company brief and one engineer | Without a real company name the certificate has no calibration; students are easier to reach | Hypothesis; Arm A stop condition if no brief by 2026-10-20 ([experiment card](../experiment-card.md)) |
| Do the matching and scoring by hand alongside the AI | Learn what the rubric, debrief and contribution record really need before automating | Decision |
| Free entry; charge only for the certified result | Lowers the start barrier while still testing payment | Decision; tests revenue hypothesis 1 |

## So what

The curve is only as good as two untested claims: that recruiters value the
calibrated, attributed score (Arm B) and that students pay for it (Arm A) in the
[experiment card](../experiment-card.md). If either fails, the "Employer
calibration" and "Price" points move first.

[N]: deep-research/research_notes/SkillBridge%20v2%20challenge%20market/
[N-m]: deep-research/research_notes/SkillBridge%20v2%20challenge%20market/market_landscape.md
