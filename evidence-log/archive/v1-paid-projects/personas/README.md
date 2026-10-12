# Personas — overview

This folder holds every SkillBridge persona, one file each, split out of a
single `personas.md` that originally lived at the project root.

**Evidence review — 2026-09-22:** four teammate-reported interviews (two IE
University students, Baya's owner, Nolita's manager) were reviewed against
the full persona set. Grounding status per persona is noted inline below;
full source material is in [`../validation/`](../../../validation/interviews-2026-09-22.md)
and the claim-level breakdown in
[`../validation/findings-2026-09-22.md`](../../../validation/findings-2026-09-22.md).
These are second-hand, teammate-shared notes — participant-reported, not
independently observed by the team.

## File layout (course structure)

The three critical personas selected in the
[Session 8 deck](session8-personas-deck.pptx) are `ai-persona-01..03.md`; the
other hypotheses stay in `drafts/` until the team records its merge decisions.

| File | Persona | Status |
|---|---|---|
| [ai-persona-01.md](ai-persona-01.md) (+ [agent prompt](ai-persona-01-agent-prompt.md)) | The Tinkerer | Selected |
| [ai-persona-02.md](ai-persona-02.md) (+ [agent prompt](ai-persona-02-agent-prompt.md)) | The Late Sprinter | Selected |
| [ai-persona-03.md](ai-persona-03.md) | The Once-Bitten Owner | Selected |
| [drafts/persona-hypothesis-01.md](drafts/persona-hypothesis-01.md) | The Guarded Owner | Draft |
| [drafts/persona-hypothesis-02.md](drafts/persona-hypothesis-02.md) | The Unconnected Student | Draft |
| [drafts/persona-hypothesis-03.md](drafts/persona-hypothesis-03.md) | The Solo Specialist | Draft |
| [drafts/persona-hypothesis-04.md](drafts/persona-hypothesis-04.md) | The Skeptical Verifier | Draft |
| [drafts/persona-hypothesis-05.md](drafts/persona-hypothesis-05.md) | Two-sided persona set (Juan, v1, 2026-09-17) | Draft, earlier v1 set |

## Current personas

Business side (demand side of trust):

- [The Guarded Owner](drafts/persona-hypothesis-01.md) — general uncertainty about trusting a student team. **Partial participant-reported grounding (UV-B01).**
- [The Once-Bitten Owner](ai-persona-03.md) — a specific prior bad experience with paid digital work. **Untested by the 2026-09-22 round** — neither business interviewed reported a bad prior experience.

Student side (supply side of talent):

- [The Unconnected Student](drafts/persona-hypothesis-02.md) — locked out of the referral channel, seeking a sustained, verifiable track record. **Partial overlap (UV-S01, UV-S02)** on the shared application pain; the network-specific claim is untested.
- [The Tinkerer](ai-persona-01.md) — a more developed take on the same broad student profile, with a full evidence-boundary treatment and a standalone [agent prompt](ai-persona-01-agent-prompt.md). **Partial participant-reported grounding (UV-S01)** — now the most evidenced student-side persona.
- [The Late Sprinter](ai-persona-02.md) — a late-timing, one-shot counter-case to the above two, with its own [agent prompt](ai-persona-02-agent-prompt.md). **Limited overlap (UV-S02)** — the reported project was collaborative, not solo, which cuts against this persona's defining current-alternative.
- [The Solo Specialist](drafts/persona-hypothesis-03.md) — technically capable alone, but risks going a ghost collaborator once a real client and team are involved. **No direct evidence**; the closest signal (both students worked in small teams) points mildly the other way.

Evaluation side (the person who decides whether the credential means anything):

- [The Skeptical Verifier](drafts/persona-hypothesis-04.md) — the recruiter/hiring manager whose screening behaviour determines whether the student-side credential hypothesis is real. **Untouched** — this round interviewed students and business owners, not recruiters. Still the least-evidenced persona in the set.

## Cross-cutting finding: not owned by any single persona

Nolita's manager (UV-B02) reported no current project and said even cheap
work costs real time to brief and review. That's a counter-example to
assuming most SMBs have a current undone digital task — it argues for
qualifying a business's actual current need *before* counting it toward the
[10-business outreach test](../experiment-card.md), not just chasing volume.

## Why three sides, not two

The marketplace was originally modeled as two-sided — one is buying trust,
the other is buying a credential — and they carry very different evidence
weight right now. The student-side personas rest on solid third-party
labor-market data (SUPPORTED throughout); the business-side personas rest
almost entirely on the absence of contrary evidence and the founder's own
read of the risk (REPORTED/HYPOTHESIS/UNKNOWN). That asymmetry is itself
useful: it's exactly why [`assumptions.md`](../assumptions.md) names
business-side trust, not student pull, as the riskiest assumption the model
depends on.

The Skeptical Verifier (2026-09-22) adds a third side: nobody who actually
decides whether the credential works — a recruiter or hiring manager — was
modeled until then. The Unconnected Student and the Late Sprinter both
*assume* a recruiter weights the credential; the Skeptical Verifier is the
first attempt to model that recruiter's actual decision process instead of
assuming it.

## Update rule

Per the course workflow: only real-user evidence updates these personas or
the Jobs to Be Done grounding in [`jtbd.md`](../jtbd.md). The 10-business
pitch test in [`experiment-card.md`](../experiment-card.md) is the next
event that can move the business-side personas out of pure hypothesis;
nothing currently planned tests the student-side personas directly until
the student supply-side test triggers on the decision rule.
