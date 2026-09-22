# Persona: The Skeptical Verifier

Evaluation side — recruiter / hiring manager. Not a marketplace participant
in the two-sided sense; a downstream verifier whose behaviour retroactively
determines whether the supply-side value proposition holds.

**"I've seen a hundred 'credentials.' Prove this one means something before I spend my time on it."**

- Screens high volumes of entry-level and internship applications, often hundreds per role
- Works through a mix of ATS keyword filtering and fast manual skims
- Pattern-matches against known signals; treats unfamiliar credentials with default suspicion

**Grounding: HYPOTHESIS-HEAVY** — zero primary interviews yet. This persona
didn't exist anywhere else in the model until this was written, despite
being the person whose behaviour determines whether
[The Unconnected Student's](unconnected-student.md) entire Job to Be Done is
real or imagined.

**Evidence review — 2026-09-22:** not addressed by this round — the four
teammate-reported interviews were two students and two business owners, not
recruiters. This remains the least-evidenced persona in the set; validating
it requires a distinct recruiter-interview effort (see Validate next below).

## How this differs from every other persona

[The Unconnected Student](unconnected-student.md) and
[The Late Sprinter](late-sprinter.md) both *assume* a recruiter will weight
a SkillBridge credential meaningfully. Nobody previously represented that
recruiter's actual decision process, their existing filters, or what would
make them trust — or dismiss — the signal. Without this persona, the
credential hypothesis is untestable, because there was no model of the
person doing the crediting.

## Job to be done

When I'm screening a large pool of candidates with limited time per resume,
I want a fast, reliable way to tell real applied experience from resume
padding, so I don't waste interview slots on someone who can't actually do
the work.

## Situation / trigger

Screening a high-volume entry-level or internship pipeline. Encounters a
candidate listing a "SkillBridge campaign" or similar unfamiliar credential
on a resume or LinkedIn profile, sitting alongside — or instead of — a
formal internship.

## Recent behaviour — WORKING ASSUMPTION

Relies heavily on pattern-matching against known signals: recognised
company names, referral source, keyword match to the job description, GPA
and school tier as a rough filter. Unfamiliar credentials get default
suspicion unless something forces a second look — a referral, a strikingly
specific project description, or repeated exposure to the same credential
across multiple strong candidates.

## Current alternatives — WORKING ASSUMPTION

- Filter on traditional signals only (internships, referrals, known bootcamps) and ignore anything unfamiliar entirely
- Rely on ATS keyword match and never manually evaluate the credential at all
- Occasionally click through to a linked portfolio or GitHub if the resume otherwise looks strong — but inconsistently, and under time pressure

## Friction → consequence

Unfamiliar credential plus no time to verify → default skepticism → the
credential gets **ignored rather than actively rejected**. This is a
quieter failure mode than distrust: the risk isn't that the recruiter
thinks SkillBridge is bad, it's that they don't think about it at all, and
it never enters the decision.

Potential consequence: the credential becomes invisible in practice even
when the underlying work was genuinely strong. The Unconnected Student's
whole theory of change — that the credential offsets a missing network —
then fails silently, not because the work was bad, but because the
evaluator never engaged with the artefact.

## Tool / service behaviour — HYPOTHESIS

Likely to give more weight to:

- A credential that's **independently verifiable** — a link, a rating, a business testimonial — not self-reported text on a resume
- **Specificity over a generic label**: "built a booking system for a real local business, shipped on deadline" beats "completed SkillBridge program"
- Signals that map onto what they already screen for: team collaboration, client-facing communication, ownership of a deliverable — not just "wrote code"
- **Third-party corroboration** (the business owner's rating or review) over student self-report, since self-report is exactly what they're trained to discount

## Trust boundary — HYPOTHESIS

May weight the credential meaningfully if:

- It's in a format their existing tools can parse — a standard LinkedIn certification field or an ATS-readable line, not a separate PDF
- There's a verification link a skeptical recruiter can click in under 10 seconds
- The business-side rating is visible and specific, not a pass/fail checkmark
- They've seen the credential before and formed a baseline opinion — first exposure is the highest-friction moment, and recognition compounds

A credential that requires independent research to understand will likely
get skipped entirely under time pressure, regardless of how good it
actually is.

## Failure threshold — UNKNOWN

Possible triggers that would permanently discount the credential:

- One bad public experience with a SkillBridge-credentialed hire who couldn't perform
- A credential that reads as vague, or interchangeable with any other "leadership program" resume line
- No mechanism to spot-check authenticity, making it indistinguishable from a self-issued claim

These need to be tested rather than assumed — this is the least-evidenced
persona in the set, because it requires access to actual recruiters, not
students or business owners.

## Evidence

| | |
|---|---|
| SUPPORTED | Employers say skills-based hiring matters, but under 1 in 700 hires actually move on it without independent proof (`../opportunity.md`, HBS/Burning Glass 2024) — the strongest existing evidence here, and it cuts against the credential hypothesis as much as it supports it |
| SUPPORTED | Referrals convert 30–60% to interview vs. 0.1–2% for cold applications (`../opportunity.md`) — implies recruiters heavily favour pre-vetted signals over self-reported ones, exactly the skepticism this persona embodies |
| WORKING ASSUMPTION | A verified campaign record + business rating is a claim recruiters will actually weight — currently a claim on [The Unconnected Student](unconnected-student.md), untested from the recruiter's own side |
| UNKNOWN | Whether recruiters would even notice, let alone credit, this credential without prior brand recognition |
| UNKNOWN | What minimum format and verification threshold moves this from "ignored" to "actively weighted" |

## Assumptions this persona stresses

- **Area 3 (credential credibility)** — this persona *is* the test of that assumption, more directly than any student-side persona can be. The Unconnected Student and the Late Sprinter both assume the credential lands; here it either survives or dies.
- Whether the platform needs a distribution and brand-recognition strategy aimed at recruiters directly, not just at students and businesses — a gap nothing else in the current model addresses.
- Format and integration questions (ATS-readability, LinkedIn certification fields) that appear nowhere else in these personas, since nobody else interacts with the credential as a static, skimmed artefact under time pressure.

## Product implications — HYPOTHESES

- A standardised, ATS- and LinkedIn-parseable credential format, not just an internal platform badge
- Verified, specific business testimonials attached to each credential, rather than a generic completion marker
- A recognisable brand name that compounds with repeated exposure — meaning early cohort quality matters disproportionately, since a few bad early hires could poison the well before the brand exists at all
- Possibly a direct-to-recruiter education motion, separate from the student and business acquisition funnels entirely

## Validate next

This is the hardest persona to validate with the current 10-business
outreach test, since it requires reaching recruiters rather than students
or business owners. Possible approaches:

- Recruiter interviews: "Here's a resume line describing a SkillBridge campaign. Walk me through what you'd do with it in a 30-second resume scan."
- Show the same recruiter a mock LinkedIn profile with and without the credential, and compare stated likelihood to advance
- Ask directly: "What would make you trust a credential like this without ever having heard of the company before?"
- Once real credentials exist, track whether any hiring manager who advanced a SkillBridge candidate actually engaged with the credential, or whether the candidate advanced for unrelated reasons and the credential was along for the ride

## Related personas

- [The Unconnected Student](unconnected-student.md) and [The Late Sprinter](late-sprinter.md) — both assume this persona's behaviour without modeling it; this file is the missing other half of their credential hypothesis.

## Sources and companion output

- [Overview: why the personas split this way, and the update rule](README.md).
- Added via PR #8, "Add The Skeptical Verifier persona," 2026-09-22 (Abhiram Kidambi, with Claude Opus 5).
- [Opportunity](../opportunity.md).

**Readiness:** hypothesis-heavy except where marked SUPPORTED above. The
least-evidenced persona in the set. Real-user validation remains open.
