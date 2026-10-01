# Assumptions

**SkillBridge — assumption map. v1, locked 2026-09-08.**
Working notes and Stage-A raw list: `../assumptions.md`.

Carried in from the Opportunity exercise: USER / NEED / INSIGHT / HOW MIGHT WE
(see `opportunity.md`).

## Evidence update — 2026-10-01

The three-area map below retains the original hypotheses. The
[actual pilot assessment](market-research/pilot-assessment-2026-10-01.md)
updates their evidence status; the original “evidence needed” lists are not a
claim that all fieldwork is still unrun.

| Area | New support from the actual report | Still unresolved |
|---|---|---|
| Student pull and delivery | 9/11 selected difficulty showing experience beyond coursework and 9/11 explaining contribution; concrete offer acceptance, student payments and M1–M9 delivery outcomes are reported. | Offer denominator and commitment rate; individual logs, full segment fit for the survey, dropout/support costs, and the specific 5–6-strangers/no-paid-manager hypothesis. |
| Business supply and trust | Interest/stated willingness to pay and client use/acceptance are reported. | Charters were not signed. The original signed-and-paid threshold is not demonstrated; qualifying-pitch/deadline logs and student-payment funding need reconciliation. |
| Credential credibility | Recruiters reportedly found individual contribution clearer in campaign records. | Reviewer/pair counts and artifacts, hiring impact, anti-gaming, and LinkedIn/ATS acceptance. The report supports the underlying evidence's usefulness, not the badge alone. |

The riskiest assumption remains business commitment. The roughly 2,000-student
Madrid estimate and all four rates remain hypotheses. The survey obstacle table
also needs reconciliation (23 selections against a maximum of 22).

---

## Area 1: Student pull & delivery capability

**Must be true**
- Enough unconnected tech students will commit real, sustained hours to a campaign
  for the CV record + certification + small cash (vs a solo side project or the
  interview grind).
- 5–6 students who don't know each other can self-organise and deliver a scoped
  client project without a paid PM.
- Coursework-level skills + light platform scaffolding are enough to ship
  something a real small business accepts.
- Mid-campaign dropout stays low enough not to break delivery.

**Evidence needed**
- Landing-page / waitlist sign-up intent from target students.
- 5+ interviews with 2nd–4th-year tech students who job-hunted in the last year.
- One real pilot campaign with a volunteer student team — observe self-organisation,
  output quality, dropout.

## Area 2: Business supply & trust

**Must be true**
- Enough small businesses have real digital projects too small for an agency but
  real enough to matter.
- A small business will hand a real, **paid** project to a team of inexperienced
  students, given some structure/guarantee.
- They'll pay at least a small amount — enough to fund the student cash and signal
  seriousness. *(36% of SMBs spend $1k–$10k on a website, median ~$5k.)*
- Delivered quality is good enough, often enough, that businesses aren't burned and
  would repeat/recommend.
- Both sides can be bootstrapped together despite the chicken-and-egg problem.

**Evidence needed**
- Cold-outreach to 10–15 local small businesses with a concrete, priced campaign
  offer; measure interest + willingness to pay.
- One real **paid** pilot; post-delivery satisfaction + repeat/referral intent.
- Risk-perception interviews: what guarantee/structure would make them say yes.

## Area 3: Credential credibility

**Must be true**
- A "verified campaign" record + business rating is a claim recruiters actually
  weight — enough to partly offset "no formal experience".
- Target students believe it will help enough that it's a top reason they join.
- The verification resists gaming (fake businesses, inflated ratings, ghost
  contributors) or it loses all value.
- (Future) LinkedIn / ATS surfacing accepts it as a legitimate verified credential.

**Evidence needed**
- Interviews with 3–5 recruiters / hiring managers: how would they read this on a
  CV / LinkedIn?
- Test with target students whether the credential is a top-3 motivator (vs cash,
  vs the work itself).
- Adversarial walkthrough of the verification design for abuse paths.

---

## MECE checks

- **Collectively exhaustive** — gap found: *platform / company viability*
  (chicken-and-egg growth, unit economics, can a 5–6 person team build & test v0 by
  December 2026). Resolution: the chicken-and-egg piece is an assumption **inside
  Area 2**; "team ships v0 by Dec 2026" is a **project-execution risk** tracked in
  `../project-scope.md`, not part of this map. No fourth area needed.
- **Mutually exclusive** —
  - *"Delivered quality is good enough"* → **Area 2** (outcome the business
    experiences); Area 1 keeps the input capability.
  - *"Students believe the credential helps"* → **Area 3** (the credential's pull);
    Area 1 keeps behaviour/capability.

---

## Riskiest assumption

**A small business will hand a real, paid project to a team of inexperienced
students.** (Area 2)

- It's the supply the entire loop depends on — no campaigns → nothing for students
  to do → the credential certifies nothing.
- It's the least under the team's control — students come from the founders'
  network; paying clients don't.
- It's the hardest to fake in a pilot — a friendly volunteer "client" doesn't test
  real trust or willingness to pay.
- Desk research found **no evidence** on SMB willingness to trust a *student team*
  specifically — the biggest genuine unknown.
- The founder independently identified business-side trust as riskiest — matches.

**Initial test proposal (2026-09-08):** cold-outreach 10–15 real local small businesses with a priced
campaign offer; measure how many agree to a paid pilot. Near-zero conversion =
rethink the model before anything else.

**Current test design (2026-09-09):** see [Experiment Card](experiment-card.md)
for the concierge method, primary ten-business test, conditional five-business
extension, and precommitted metric, threshold, and decision rule.

---

## Open gaps
- Primary reports now exist: [September interviews](validation/interviews-2026-09-22.md)
  and the [actual pilot findings](validation/pilot-findings-source-2026-10-01.md).
  Recover underlying records, cohort counts/overlap and recruitment details.
- Complete and score the original business test; measure student readiness from
  genuine offers, and document support costs before revising the market estimate.
- Exact assignment deadline / number of required testers / rubric not pinned.
- Certification anti-gaming design not yet specified.
