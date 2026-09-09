# Assumptions

**SkillBridge — assumption map. v1, locked 2026-09-08.**
Working notes and Stage-A raw list: `../assumptions.md`.

Carried in from the Opportunity exercise: USER / NEED / INSIGHT / HOW MIGHT WE
(see `opportunity.md`).

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
- No primary interviews yet (founder account + market statistics only).
- Exact assignment deadline / number of required testers / rubric not pinned.
- Certification anti-gaming design not yet specified.
