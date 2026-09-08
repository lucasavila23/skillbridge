# Assumptions — SkillBridge

**Status: LOCKED v1 — 2026-09-08.** Produced by running
`downloads/ai-prompt-assumptions.md` autonomously against the locked Opportunity
framing + desk research. Clean deliverable mirrored in
`evidence-log/assumptions.md`.

Input carried in: USER / NEED / INSIGHT / HOW MIGHT WE from `opportunities.md`.

---

## Stage A — Raw assumptions (what must be true for SkillBridge to work)

**Student side**
- Enough unconnected tech students will invest real, sustained hours in a campaign for the record + certification + small cash, rather than a solo side project or interview grind.
- 5–6 students who don't know each other can self-organise and deliver a scoped client project without a paid manager/PM.
- Coursework-level skills + light platform structure are enough to ship something a real small business accepts.
- Mid-campaign dropout stays low enough not to break delivery.

**Business side**
- Enough small businesses have real digital projects too small for an agency but real enough to matter (websites, small apps, data tasks).
- A small business will hand a real, **paid** project to a team of inexperienced students, given some structure/guarantee.
- They'll pay at least a small amount — enough to fund the student cash and signal seriousness.
- Delivered quality is good enough, often enough, that businesses aren't burned and would repeat or recommend.
- The two sides can be bootstrapped together despite the chicken-and-egg problem.

**Credential side**
- A "verified campaign" record + business rating is a claim recruiters actually weight — enough to partly offset "no formal experience".
- Target students believe it will help enough that it's a real reason they join.
- The verification resists gaming (fake businesses, inflated ratings, ghost contributors).
- (Future) LinkedIn / ATS surfacing treats it as a legitimate verified credential, not noise.

---

## Stage B — Three MECE areas (confirmed)

### Area 1: Student pull & delivery capability
**Must be true**
- Enough unconnected tech students will commit real, sustained hours to a campaign for the CV record + certification + small cash (vs a solo side project or the interview grind).
- 5–6 students who don't know each other can self-organise and deliver a scoped client project without a paid PM.
- Coursework-level skills + light platform scaffolding are enough to ship something a real small business accepts.
- Mid-campaign dropout stays low enough not to break delivery.

**Evidence needed**
- Landing-page / waitlist sign-up intent from target students.
- 5+ interviews with 2nd–4th-year tech students who job-hunted in the last year (→ `recruitment.md`).
- One real pilot campaign with a volunteer student team; observe self-organisation, output quality, dropout.

### Area 2: Business supply & trust
**Must be true**
- Enough small businesses have real digital projects too small for an agency but real enough to matter.
- A small business will hand a real, paid project to a team of inexperienced students, given structure/guarantee.
- They'll pay at least a small amount — enough to fund the student cash and signal seriousness. *(Context: 36% of SMBs spend $1k–$10k on a website, median ~$5k; agencies impose retainer minimums.)*
- Delivered quality is good enough, often enough, that businesses aren't burned and would repeat/recommend.
- Both sides can be bootstrapped together despite chicken-and-egg (CE-gap assumption, folded here).

**Evidence needed**
- Outreach to 10–15 local small businesses with a concrete campaign offer; measure interest + willingness to pay.
- One real **paid** pilot; post-delivery satisfaction + repeat/referral intent.
- Interviews on risk perception: what guarantee/structure would make them say yes.

### Area 3: Credential credibility
**Must be true**
- A "verified campaign" record + business rating is a claim recruiters/hiring managers actually weight — enough to partly offset "no formal experience". *(Context: skills-based-hiring rhetoric high but implementation lags; certs act as a tie-breaker, not an experience replacement.)*
- Target students believe it will help enough that it's a top reason they join.
- The verification resists gaming (fake businesses, inflated ratings, ghost contributors) or it loses all value.
- (Future) LinkedIn / ATS surfacing accepts it as a legitimate verified credential.

**Evidence needed**
- Interviews with 3–5 recruiters / hiring managers: how would they read this on a CV / LinkedIn?
- Test with target students whether the credential is a top-3 motivator (vs cash, vs the work itself).
- Adversarial walkthrough of the verification design for abuse paths.

### MECE checks
- **Collectively exhaustive** — gap identified: *platform / company viability* (chicken-and-egg growth, unit economics, can a 5–6 person team build and test v0 by December 2026). Decision: the chicken-and-egg piece becomes an assumption **inside Area 2**; "team can ship v0 by Dec 2026" is a **project-execution risk** tracked in `project-scope.md`, not part of the opportunity assumption map. No fourth area needed.
- **Mutually exclusive** — two assumptions could sit in two areas:
  - *"Delivered quality is good enough"* → assigned to **Area 2** (the outcome the business experiences). Area 1 keeps the *input* capability.
  - *"Students believe the credential helps"* → assigned to **Area 3** (the credential's pull). Area 1 keeps behaviour/capability.

---

## Stage C — Riskiest assumption

**"A small business will hand a real, paid project to a team of inexperienced
students."** (Area 2)

**Why this one:**
- It's the **supply the entire loop depends on** — no campaigns → nothing for
  students to do → the credential certifies nothing.
- It's the **least under the team's control** — students can be recruited from the
  founders' own network; paying business clients cannot.
- It's the **hardest to fake in a pilot** — a friendly volunteer "client" doesn't
  test real trust or real willingness to pay.
- Research found **no evidence** on SMB willingness to trust a *student team*
  specifically — the biggest genuine unknown.
- The founder independently pointed at business-side trust as the riskiest — this
  matches.

**First test:** cold-outreach 10–15 real local small businesses with a concrete
campaign offer and a price; measure how many say yes to a paid pilot. If that
conversion is near zero, the model needs rethinking before anything else matters.

---

## CROSS-REVIEW HANDOFF (paste into a separate AI for independent critique)

```
Please critically review this assumption map. Check whether the three areas are
genuinely mutually exclusive and collectively exhaustive, whether each assumption
is specific and falsifiable rather than vague, whether the evidence needed is
realistic to gather in one semester, and whether the riskiest assumption is
actually the one most likely to break the idea. Flag anything unsupported,
overlapping, or missing. Suggest concrete improvements.

BUSINESS IDEA (one line): An open platform where teams of tech students take on
small, real, paid campaigns for small businesses and come away with a verified
record of shipped client work, plus some cash.

USER: A 2nd-4th-year tech student (software/web/data), no internship, no network,
not in the connected top tier.
NEED: Accumulate a verifiable track record of real, team-delivered client projects
employers recognise, before having formal experience.
INSIGHT: Demand for inexperienced talent exists but is invisible/unmatched; early
winners rely on connections not merit; no existing option is open + real +
credentialed.
HOW MIGHT WE: Give an unconnected tech student an open, merit-based way to build a
verified record of real, team-delivered client work before any formal experience.

AREA 1 - Student pull & delivery capability
Must be true: enough unconnected students commit real hours for record+cert+cash;
5-6 strangers self-organise and deliver without a paid PM; coursework skills + light
scaffolding are enough to ship acceptable work; dropout stays low enough.
Evidence: waitlist intent; 5+ student interviews; one real pilot campaign.

AREA 2 - Business supply & trust
Must be true: enough SMBs have real "too small for an agency" projects; an SMB will
hand a real paid project to an inexperienced student team given structure; they'll
pay at least a small amount; quality is good enough often enough to avoid burning
them; both sides can be bootstrapped despite chicken-and-egg.
Evidence: outreach to 10-15 SMBs with a priced offer; one real paid pilot +
repeat/referral intent; risk-perception interviews.

AREA 3 - Credential credibility
Must be true: a verified-campaign record + business rating is weighted by
recruiters enough to offset "no experience"; students believe it enough to join
for it; verification resists gaming; (future) LinkedIn/ATS treat it as legitimate.
Evidence: 3-5 recruiter interviews; student motivator ranking; adversarial abuse
walkthrough.

CE gap folded in: chicken-and-egg -> Area 2. "Team ships v0 by Dec 2026" tracked
as a project-execution risk, not in this map.
ME calls: "quality good enough" -> Area 2; "students believe credential helps" ->
Area 3.

RISKIEST ASSUMPTION: An SMB will hand a real, paid project to a team of
inexperienced students. It is the supply the whole loop depends on, the least
controllable, the hardest to fake in a pilot, and the least evidenced.

OPEN GAPS: no primary interviews yet (founder account + market stats only); exact
assignment deadline/rubric not pinned; certification anti-gaming design not
specified.
```

---

## Notes
- Evidence-gathering plan feeds `evidence-log/recruitment.md` and
  `evidence-log/experiment-card.md`.
- This map is v1 — revise as interviews come in.
