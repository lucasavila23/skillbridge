# Persona: The Skeptical Verifier

> **v2 note (2026-10-12):** Selected as a critical persona on 2026-10-12. In v2 this persona decides whether the certificate is worth anything, so it carries A3.1 and Arm B of the [experiment card](../experiment-card.md). The V2-R01 intake adds one recruiter's trust conditions and a stated mock-profile choice; generalisation and actual hiring effects remain unknown. Assumption IDs refer to [assumptions](../assumptions.md).

Evaluation side — recruiter / hiring manager. Not a marketplace participant
in the two-sided sense; a downstream verifier whose behaviour retroactively
determines whether the supply-side value proposition holds.

**"I've seen a hundred 'credentials.' Prove this one means something before I spend my time on it."**

- Screens high volumes of entry-level and internship applications, often hundreds per role
- Works through a mix of ATS keyword filtering and fast manual skims
- Pattern-matches against known signals; treats unfamiliar credentials with default suspicion

**Grounding: PARTIAL PARTICIPANT-REPORTED** — V2-R01 on 2026-10-06 plus the
[five CV comparisons received 2026-10-26](../validation/recruiter-comparison-findings-2026-10-26.md).
The new set supports interest in inspectable work and human review, conditional
on reviewer credibility, authorship checks and no pay-to-pass. All five saw
illustrative profiles; three predate the formal window, screening and exact
files remain pending. Wider screening patterns and hiring outcomes remain
hypotheses. The persona voice above is illustrative, not an interview quote.

**Evidence review — 2026-09-22:** not addressed by this round — the four
teammate-reported interviews were two students and two business owners, not
recruiters. The October interview update below is separate from that round.

## V2 interview grounding

[V2-R01 Q1-Q5](../validation/v2-interviews-2026-10-12.md#v2-r01-q1) reports
high-volume screening, very short first-pass reviews, limited GitHub
inspection, difficulty identifying group contributions and costly take-home
review. These are one participant's reported practices, not measured rates.

Q6-Q7 records a preference for the mock profile containing a task, work and
an engineer's note. The respondent values specific human feedback and rubric
provenance, but would skip an unexplained numerical score. The actual mock
profiles are not attached, and no candidate was advanced through a real
recruitment process in the supplied record.

Q8-Q9 makes possible take-home replacement conditional on the company's own
brief, engineer sign-off and a live explanation of the work. Q10 identifies
a possible budget route, not approved spending. See the
[v2 findings](../validation/v2-findings-2026-10-12.md) for limits and the
distinction between stated screening value and financial commitment.

## How this differs from every other persona

[The Unconnected Student](drafts/persona-hypothesis-02.md) and
[The Late Sprinter](ai-persona-02.md) both *assume* a recruiter will weight
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

V2-R01 Q9 adds stated distrust of similar-looking submissions and work with
no live explanation. Neither a permanent rejection threshold nor the
frequency of these concerns across recruiters has been observed.

## Evidence

| | |
|---|---|
| SUPPORTED | Employers say skills-based hiring matters, but under 1 in 700 hires actually move on it without independent proof (`../../opportunity.md`, HBS/Burning Glass 2024) — the strongest existing evidence here, and it cuts against the credential hypothesis as much as it supports it |
| SUPPORTED | Referrals convert 30–60% to interview vs. 0.1–2% for cold applications (`../../opportunity.md`) — implies recruiters heavily favour pre-vetted signals over self-reported ones, exactly the skepticism this persona embodies |
| STATED JUDGMENT | V2-R01 Q6-Q7 favours a mock profile with inspectable work and engineer feedback; an unexplained score alone has little value to this respondent |
| UNKNOWN | Whether recruiters notice and credit this record in an unprompted real screening process; the supplied comparison explicitly drew attention to it |
| STATED CONDITIONS | V2-R01 Q7-Q9 asks for rubric provenance, human sign-off and a live explanation; a general minimum format or verification threshold remains unknown |
| STATED COMPARISON | CV-R01–CV-R05 Q2/Q3: five favourable judgments about illustrative profiles. R01/R04 require credible reviewer provenance; R03 wants authorship checks; R02/R05 require no pay-to-pass. R04's distrust of automated grading challenges the AI-assisted model. No actual hiring behaviour or final Arm B pass established. |

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

Use Arm B of the [v2 experiment](../experiment-card.md). The new five-record
intake is completed concept research, but only two interviews are in-window;
recover screening and exact profiles, then complete the qualifying cohort.
Preserve trust conditions and distinguish illustrative-profile choices from
actual shortlist decisions. Possible subsequent tests:

- Recruiter interviews: "Here's a resume line describing a SkillBridge campaign. Walk me through what you'd do with it in a 30-second resume scan."
- Show the same recruiter a mock LinkedIn profile with and without the credential, and compare stated likelihood to advance
- Ask directly: "What would make you trust a credential like this without ever having heard of the company before?"
- Once real credentials exist, track whether any hiring manager who advanced a SkillBridge candidate actually engaged with the credential, or whether the candidate advanced for unrelated reasons and the credential was along for the ride

## Related personas

- [The Unconnected Student](drafts/persona-hypothesis-02.md) and [The Late Sprinter](ai-persona-02.md) — both assume this persona's behaviour without modeling it; this file is the missing other half of their credential hypothesis.

## Sources and companion output

- [Overview: why the personas split this way, and the update rule](README.md).
- Added via PR #8, "Add The Skeptical Verifier persona," 2026-09-22 (Abhiram Kidambi, with Claude Opus 5).
- [Opportunity](../opportunity.md).
- [V2-R01 source record](../validation/v2-interviews-2026-10-12.md#v2-r01) and
  [v2 evidence assessment](../validation/v2-findings-2026-10-12.md).

**Readiness:** partial interview grounding with wider hypotheses retained.
Observed hiring and actual spending remain open; the formal recruiter cohort
and source checks are incomplete despite five favourable reported comparisons.
