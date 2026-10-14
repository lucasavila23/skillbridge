# Stakeholder map: value, hurdles and options

**2026-10-13.** Answers the Challenge II defense feedback: "you need a better
understanding of the dynamics at play, the value for each player in the
market, and the actual hurdles and options available, e.g. partnerships,
private and public pro-bono programs, university plans… Break it down and
prioritize what is worth doing and feasible"
([feedback response](feedback-response.md#challenge-ii-venture-skeleton-v01-65--80)).

Tags: **Evidence** (real users, linked), **Desk** (published sources, linked),
**Hypothesis** (team reasoning, untested). Research notes live in
[deep research][N].

## 1. The players and what each gets

| Player | What they get | What it costs them | Biggest hurdle | Status |
|---|---|---|---|---|
| **Student** (2nd–4th year, mainly coursework) | Proof of what they personally did on a real brief, plus specific feedback | 2–7 hours; €15 if they certify | Free alternatives compete for attention; a poor score is a risk; four hours clash with exams | Pain: **Evidence** (14/17 contribution, 12/17 beyond coursework). Paying: stated, conditional ([claims changed](validation/claims-changed.md) rows 4, 7, 11) |
| **Company engineer** (writes the brief, signs off the rubric) | A potentially cheaper first screen; net saving untested | Brief/rubric setup, sample reviews, individual eligibility checks, feedback for every certified result, debriefs and coordination; [full accounting](ERRC.md#engineer-workload-and-cost) | Total capacity, and no say over the budget | One CSV task offered, not signed; 20 min per solution review is an estimate, not the complete service cost (V2-E01) |
| **Recruiter / talent lead** (decides whether the result counts) | A shortlist signal they can inspect: work, company rubric, engineer note, contribution record | Learning a new signal | Distrusts unfamiliar credentials and bare scores; worries about AI cheating | Conditional trust in the bundle (V2-R01, OO-R01, [DF-R01](validation/sources/company-interview-deem-finance.md)). **Hypothesis** that it changes real shortlists |
| **Budget owner** (head of talent / HR) | Potential reduction in take-home review time; employer branding with students | A per-challenge or sponsorship fee plus any engineer time supplied | Needs a named budget, a comparison and complete costs | V2-R01 and the engineer point to talent-brand budgets; DF-R01 names the campus and employer-branding budget, signed by the HR director, paid per hire or per challenge; no price or saving established ([v2 findings](validation/v2-findings-2026-10-12.md) F10) |
| **University careers office** (e.g. IE Talent & Careers) | Better outcomes for its students; a ready-made partner programme | Promotion, perhaps a licence fee | Already backs other routes (IE × Extern externships) | **Desk:** IE publicises Extern ([competitive analysis](market-research/competitive-analysis.md) CA6). Interest untested |
| **SkillBridge** (operator) | Fees from whichever side values the result most | Matching, scoring, engineer coordination, payments, legal compliance | Cold start: students come for company names, companies come for students | [Value curve](market-research/value-curve.md#four-actions-and-cold-start) |

## 2. The dynamics

1. **Credibility is borrowed, not owned.** The certificate is worth what the
   setting company's name and rubric are worth. V2-R01, OO-R01 and DF-R01 all trust
   it only with the company's rubric, its engineer's note and the work itself.
   So the company is the scarce side, and SkillBridge must secure it first.
2. **The side that values the result most is not the side the team ranked
   first.** Students value it but have free alternatives and little money;
   companies already pay for screening (HackerRank from $79/month), challenges
   (Parker Dewey 10-hour projects at about $200–600) and hackathon sponsorship
   ($500–$50k+) ([company motives][N-c]). All three one-on-one interviewees say
   companies should pay. Student fees alone in Madrid stay under €9,000 a year
   even at the 30% threshold ([v2 Fermi](market-research/README.md#v2-fermi-estimate-challenge-completers-in-madrid-2026-10-12)).
3. **Scarcity protects value.** V2-S01: "The second it's on fifty profiles it's
   noise." Certificates must be possible to fail and limited per company, which
   caps student volume and makes company-side revenue more important.
4. **AI cuts both ways.** It may reduce routine scoring work (the Reduce move) but also
   makes remote work less trustworthy (cheating encounters doubled 7% → 15%,
   ISE Dec 2025). Hence the sample, eligibility checks, live debriefs and
   engineer-written feedback on every certified result. All count toward cost.
5. **Regulation favours proof without employment.** Spain's pending Estatuto
   del Becario would make internships more regulated and costly; a challenge is
   not an internship ([internship struggles][N-i], speculative until passed).

## 3. Hurdles

| Hurdle | Why it matters | How we handle it now | Status |
|---|---|---|---|
| No signed company brief | Without it the certificate has no calibration | Written CSV brief by 20 Oct (owner: Lucas Avila), else Arm B alone ([experiment card](experiment-card.md)) | Open |
| Students won't pay while alternatives are free | Breaks revenue hypothesis 1 | Pilot Arm A at €15; company price defined alongside the pilot ([details to narrow](experiment-card.md#next-details-to-narrow), row 3) | Open, tested 16–30 Oct |
| Engineer time grows with requests and certificates | Eligibility work can occur without payment; every certified student still needs written feedback | Five sample reviews alone are estimated at 100 min, before additional work. Agree capacity before committing to the cohort, count reused reviews once, and limit intake to what can receive the promised feedback. See [workload accounting](ERRC.md#engineer-workload-and-cost). | Open risk even at 3 certificates; one-hour capacity is not established |
| AI-only scores | The team's legal notes require a human review step before an automated process lowers a credential rating, a plain-language explanation of any score, and a visible AI label ([legal constraints](../legal-constraints.md) ALG-1, ALG-3, AI-1) | Engineer scores a sample; label AI-scored results; certified results always get a human | Partly handled |
| Payments | Holding money directly needs a payment-institution licence ([legal constraints](../legal-constraints.md) PAY-1) | Pilot uses a payment link from a licensed provider, not a team member's account | To confirm before 16 Oct |
| IP and data | Who owns student code; GDPR for profiles | Students keep their code; assessment use only (V2-E01 Q5); results private by default | Agreed in interview, not in writing |
| A local incumbent | NUWE (Barcelona) offers company challenges ([company description](https://uk.linkedin.com/company/nuweio)) | Test the value of the individual-contribution certificate rather than assuming exclusivity | Individual-contribution verification is **not publicly disclosed** in the reviewed material; [comparison](market-research/contribution-verification-review-2026-10-13.md) |

## 4. Options, prioritised

Effort is what the team can do this semester with no money. Priority:
**Now** = during the 16–30 Oct pilot; **Next** = Phase 2 (Sessions 16–28);
**Later** = after Phase 2; **Not now** = considered and set aside.

| Option | What it is | Value | Effort | Evidence | Priority |
|---|---|---|---|---|---|
| One company, one brief | Turn V2-E01's CSV task into a signed brief and rubric | Unlocks Arm A and calibration | Low | Offered verbally | **Now** |
| IE Talent & Careers | Ask for help reaching recruiters (Arm B) and students; later, co-promotion | Recruiters plus a trusted channel to students | Low | **Desk:** the service exists; interest untested | **Now** |
| Student tech associations | Recruit through IE clubs; the HackUPC and LleidaHack pattern shows associations feed challenges ([student motives][N-s]) | Fills Arm A's ≥15 starts | Low | Desk | **Now** |
| Company-pays offer | A per-challenge price for companies, ready if Arm A fails and B passes (Arm A company contact and Arm B recruiters asked what they would pay) | Revenue from the side that already pays | Low to draft | One-on-ones 3/3; desk benchmarks | **Now** (draft), **Next** (test) |
| University plan | The university pays or co-issues the certificate for its students, as Forage (1,000+ partner universities) and Riipen institutional partnerships do ([company motives][N-c], [competitive analysis](market-research/competitive-analysis.md) R2) | Students get it free; the university brand adds trust | Medium: a sales cycle | Desk precedent only | **Next** |
| Employer-branding sponsorship | Company sponsors a challenge from its talent-brand budget instead of a hackathon | Uses an existing budget (V2-R01's hackathon) | Medium | V2-R01 reported a sponsored hackathon; DF-R01 co-sponsored a ~€5,000 datathon and hired no one from it | **Next** |
| EU-standard credential | Issue results in the EU micro-credential format so they sit in Europass and LinkedIn ([credential credibility][N-r]) | Cheap credibility with EU employers and universities | Medium (software) | Desk | **Later** |
| Public funding | Digital Europe "advanced digital skills" calls, reached through a university consortium; Spain funds university micro-credentials through the Recovery Plan ([market landscape][N-m], [credential credibility][N-r]) | Non-dilutive money | High: consortium needed | Desk | **Later** |
| Pro-bono briefs | NGOs or academic projects as challenge sources when no company signs (Kaggle offers free hosting to academic and non-profit hosts, [company motives][N-c]) | Keeps students supplied | Low | Desk | **Later**, fallback only: weaker credibility than a company brief |
| Kit Digital / Kit Consulting | Spain's SME digitisation grants | Funds SMEs' digital services, not student challenge platforms | — | Desk | **Not now** |
| Enterprise clients | Large brands with hackathons | Big budgets | High: GDPR and legal review first | Hypothesis | **Not now** |

**What we will do first:** sign one brief, recruit through IE Talent & Careers
and tech clubs, run the two-arm pilot, and define the company price before
results come in. Everything else waits for the pilot's decision rule.

[N]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/
[N-c]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/company_motives.md
[N-i]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/internship_struggles.md
[N-m]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/market_landscape.md
[N-r]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/credential_credibility.md
[N-s]: market-research/deep-research/research_notes/SkillBridge%20v2%20challenge%20market/student_motives.md
