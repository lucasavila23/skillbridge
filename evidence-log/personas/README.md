# Personas — overview

This folder holds every SkillBridge persona, one file each, split out of a
single `personas.md` that originally lived at the project root.

**Evidence review — 2026-09-22:** four teammate-reported interviews (two IE
University students, Baya's owner, Nolita's manager) were reviewed against
the full persona set. Grounding status per persona is noted inline below;
full source material is in [`../validation/`](../validation/interviews-2026-09-22.md)
and the claim-level breakdown in
[`../validation/findings-2026-09-22.md`](../validation/findings-2026-09-22.md).
These are second-hand, teammate-shared notes — participant-reported, not
independently observed by the team.

**V2 evidence intake — 2026-10-12:** the user supplied interviews they conducted
with one student (October 5), one recruiter (October 6) and one engineer
(October 10). [Records](../validation/v2-interviews-2026-10-12.md) and
[findings](../validation/v2-findings-2026-10-12.md) add initial v2 grounding.
V2-S01 overlaps with some student-persona behaviours but is not identified as
UV-S01 or UV-S02. V2-R01 adds the first recorded v2 mock-profile response for
the Skeptical Verifier. Neither payment nor hiring outcomes are established.

## File layout (course structure)

**v2 selection (2026-10-12):** after the pivot to a challenge platform, the
credential's credibility with recruiters is the riskiest assumption, so the
Skeptical Verifier replaces the Once-Bitten Owner as the third critical persona.
No `persona-hypothesis-04` file exists any more; numbering is kept so old
references in the [v1 archive](../archive/v1-paid-projects/personas/README.md) stay meaningful.

### The three critical personas and why

| Persona | Why it is critical in v2 | Assumptions it carries |
|---|---|---|
| [The Tinkerer](ai-persona-01.md) | The core student user: tool-curious, builds side projects that nobody outside reviews. Tests whether a student finishes a 2–7 hour challenge without a prize. Best grounded (UV-S01, V2-S01). | A1.2 completion, A1.3 paying |
| [The Late Sprinter](ai-persona-02.md) | The most likely payer: an application deadline makes a fast, credible signal worth money. Also the counter-case: may churn after one certificate. | A1.3 paying, A3.1 recruiter trust |
| [The Skeptical Verifier](ai-persona-03.md) | The recruiter who decides whether the certificate is worth anything. In v2 the riskiest assumption sits here, so it replaced the Once-Bitten Owner (small businesses are no longer the customer). | A3.1 trust, A3.3 replacing take-homes |

The Tinkerer and Late Sprinter were selected in the
[Session 8 deck](session8-personas-deck.pptx), the Skeptical Verifier on
2026-10-12. The other hypotheses stay in `drafts/` as history.

| File | Persona | Status |
|---|---|---|
| [ai-persona-01.md](ai-persona-01.md) (+ [agent prompt](ai-persona-01-agent-prompt.md)) | The Tinkerer | Selected |
| [ai-persona-02.md](ai-persona-02.md) (+ [agent prompt](ai-persona-02-agent-prompt.md)) | The Late Sprinter | Selected |
| [ai-persona-03.md](ai-persona-03.md) | The Skeptical Verifier | Selected (v2, 2026-10-12) |
| [drafts/persona-hypothesis-01.md](drafts/persona-hypothesis-01.md) | The Guarded Owner | Draft |
| [drafts/persona-hypothesis-02.md](drafts/persona-hypothesis-02.md) | The Unconnected Student | Draft |
| [drafts/persona-hypothesis-03.md](drafts/persona-hypothesis-03.md) | The Solo Specialist | Draft |
| [drafts/persona-hypothesis-05.md](drafts/persona-hypothesis-05.md) | Two-sided persona set (Juan, v1, 2026-09-17) | Draft, earlier v1 set |
| [drafts/persona-hypothesis-06.md](drafts/persona-hypothesis-06.md) | The Once-Bitten Owner | Draft (selected in v1; small businesses are no longer the paying side in v2) |

## Current personas

Business side (v1 only, archived; small businesses are not a v2 customer):

- [The Guarded Owner](drafts/persona-hypothesis-01.md) — general uncertainty about trusting a student team. **Partial participant-reported grounding (UV-B01).**
- [The Once-Bitten Owner](drafts/persona-hypothesis-06.md) — a specific prior bad experience with paid digital work. **Untested by the 2026-09-22 round** — neither business interviewed reported a bad prior experience.

Student side (supply side of talent):

- [The Unconnected Student](drafts/persona-hypothesis-02.md) — locked out of the referral channel, seeking a sustained, verifiable track record. **Partial overlap (UV-S01, UV-S02)** on the shared application pain; the network-specific claim is untested.
- [The Tinkerer](ai-persona-01.md) — a more developed take on the same broad student profile, with a full evidence-boundary treatment and a standalone [agent prompt](ai-persona-01-agent-prompt.md). **Partial participant-reported grounding (UV-S01)** — now the most evidenced student-side persona.
- [The Late Sprinter](ai-persona-02.md) — a late-timing, one-shot counter-case to the above two, with its own [agent prompt](ai-persona-02-agent-prompt.md). **Limited overlap (UV-S02)** — the reported project was collaborative, not solo, which cuts against this persona's defining current-alternative.
- [The Solo Specialist](drafts/persona-hypothesis-03.md) — technically capable alone, but risks going a ghost collaborator once a real client and team are involved. **No direct evidence**; the closest signal (both students worked in small teams) points mildly the other way.

Evaluation side (the person who decides whether the credential means anything):

- [The Skeptical Verifier](ai-persona-03.md) — the recruiter/hiring manager whose screening behaviour determines whether the student-side credential hypothesis is real. **Partial participant-reported grounding (V2-R01):** one supportive mock-profile judgment, with engineer feedback and rubric provenance valued above an unexplained number. Hiring effects remain untested.

## Cross-cutting finding: not owned by any single persona

Nolita's manager (UV-B02) reported no current project and said even cheap
work costs real time to brief and review. That's a counter-example to
assuming most SMBs have a current undone digital task — it argues for
qualifying a business's actual current need *before* counting it toward the
v1 10-business outreach test, which was closed without running
([experiment card](../experiment-card.md)). It was one of the reasons for the v2 pivot.

## Why three sides, not two

The marketplace was originally modeled as two-sided — one is buying trust,
the other is buying a credential — and they carry very different evidence
weight right now. The student-side personas rest on solid third-party
labor-market data (SUPPORTED throughout); the business-side personas rest
almost entirely on the absence of contrary evidence and the founder's own
read of the risk (REPORTED/HYPOTHESIS/UNKNOWN). That asymmetry is itself
useful: it's why v1 named business-side trust as its riskiest assumption.
In v2 the risk moved to the credential: [`assumptions.md`](../assumptions.md#riskiest-assumption)
names students paying because employers trust the score (A1.3 + A3.1).

The Skeptical Verifier (2026-09-22) adds a third side: nobody who actually
decides whether the credential works — a recruiter or hiring manager — was
modeled until then. The Unconnected Student and the Late Sprinter both
*assume* a recruiter weights the credential; the Skeptical Verifier is the
first attempt to model that recruiter's actual decision process instead of
assuming it.

## Update rule

Per the course workflow: only real-user evidence updates these personas or
the Jobs to Be Done grounding in [`jtbd.md`](../jtbd.md). The v2
[experiment card](../experiment-card.md) is the next event: Arm A (students
pay for a certified result) tests the Tinkerer and Late Sprinter, and Arm B
(recruiters judge the certificate) tests the Skeptical Verifier.
