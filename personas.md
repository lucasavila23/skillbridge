# Personas

**SkillBridge — Persona Builder output. v1, provisional, 2026-09-17.**
Inputs: `opportunity.md`, `goals.md`, `assumptions.md`, `experiment-card.md`.

Two personas, one for each side of the marketplace — this is a two-sided
platform, so "the target customer" is actually two different people with
different jobs, different evidence bases, and different risk. Per the
homework rule: **only real-user evidence changes these or the Jobs to Be
Done grounding** — nothing below has been interview- or pilot-tested yet.

---

## Persona 1 — The Guarded Owner (small business, demand side of trust)

**Won't risk it without proof.**

- Runs day-to-day operations personally — no dedicated marketing/IT hire, wears the hat herself
- Has a real, undone piece of digital work (no website, or a stale one) too small to justify agency pricing
- Has never worked with a student team, and has no reason yet to think one won't waste her time or money

> "I'll believe it when I see it delivered. With my own money on the line, I need proof this won't blow up in my face." — illustrative persona voice

**Job to be done:** When I have digital work that matters to my business but isn't big enough for an agency budget, I want a low-risk way to get it done properly, so I don't have to choose between overpaying and gambling on an unproven freelancer.

### What we know

| | |
|---|---|
| SUPPORTED | 36% of small businesses spend $1k–$10k on a website (median ~$5k), and ~27% still have none — the underlying digital work and budget genuinely exist (`opportunity.md`) |
| REPORTED | The founder independently flagged business-side trust as the single riskiest assumption in the whole model (`assumptions.md`) |
| SUPPORTED | Desk research turned up **no existing evidence** on whether SMBs will trust a student team specifically — this isn't a solved question anywhere, not just internally (`assumptions.md`) |

### What we still need to test

| | |
|---|---|
| HYPOTHESIS | A signed project charter + refundable 10% deposit + fixed scope/deadline is enough structure to convert guardedness into a "yes" (`experiment-card.md`) |
| HYPOTHESIS | Seeing real, named student profiles (coursework work, skills toolkit, a short "why this project" statement) lowers perceived risk more than an anonymous pitch (`experiment-card.md`) |
| UNKNOWN | What specific guarantee or structure actually flips a "no" — the risk-perception interviews to find out haven't happened yet (`assumptions.md`) |
| UNKNOWN | Whether delivered quality will be good enough, often enough, that she'd repeat or refer — untested until a real project ships (`assumptions.md`) |

**Note:** this persona has zero OBSERVED evidence — no business has been pitched yet. The 10-business cold-outreach test in `experiment-card.md` *is* the first real data point, and the whole current sprint goal exists to interrogate this persona specifically.

---

## Persona 2 — The Unconnected Student (tech student, supply side of talent)

**Ready to prove it — nobody will let them.**

- 2nd–4th-year tech student (software / web / data), solid coursework record
- No internship, no industry network, not in the connected/top-GPA slice that gets pulled in through referrals
- Applying broadly and getting filtered out before ever reaching a human

> "I have the skills. I just don't have the one thing every posting actually wants — proof I've already done it." — illustrative persona voice

**Job to be done:** When I have no internship and no network, I need to accumulate a verifiable record of real, team-delivered client work, so an employer has a reason to trust me before I have any formal experience.

### What we know

| | |
|---|---|
| SUPPORTED | 66.8% of grads name lack of experience as their #1 obstacle; ~35% of "entry-level" postings still ask for 3+ years (`opportunity.md`) |
| SUPPORTED | Referrals convert 30–60% to interview vs. 0.1–2% for cold applications — this persona is structurally locked out of the channel that actually works (`opportunity.md`) |
| SUPPORTED | Verified real work beats unverifiable resume claims: employers say skills-based hiring matters, but under 1 in 700 hires actually move on it without proof (`opportunity.md`, HBS/Burning Glass 2024) |
| REPORTED | The founder's own path — rejected everywhere, eventually hired by a startup deliberately recruiting overlooked candidates — is the seed insight for the entire venture (`opportunity.md`) |

### What we still need to test

| | |
|---|---|
| HYPOTHESIS | A verified campaign record + business rating is a claim recruiters will actually weight, partly offsetting "no formal experience" (`assumptions.md`) |
| HYPOTHESIS | The credential — not the cash, not the work itself — is a top-3 reason this student joins and sticks with a campaign to completion (`assumptions.md`) |
| UNKNOWN | Whether 5–6 strangers can self-organize and ship a scoped client project without a paid PM, and what dropout rate that produces (`assumptions.md`) |
| UNKNOWN | How recruiters and ATS systems would actually read this credential on a CV/LinkedIn — the recruiter interviews haven't happened yet (`assumptions.md`) |

**Note:** same caveat as Persona 1 — founder's account plus market statistics only, no primary student interviews conducted yet (`opportunity.md`, "Open gaps").

---

## Why two personas, not one

The two sides don't share a Job to Be Done — one is buying trust, the other is buying a credential — and they carry very different evidence weight right now. The student persona rests on solid third-party labor-market data (SUPPORTED throughout); the business owner persona rests almost entirely on the absence of contrary evidence and the founder's own read of the risk (REPORTED/HYPOTHESIS/UNKNOWN). That asymmetry is itself useful: it's exactly why `assumptions.md` names business-side trust, not student pull, as the riskiest assumption the model depends on.

## Update rule

Per the course workflow: only real-user evidence updates these personas or the Jobs to Be Done above. The 10-business pitch test in `experiment-card.md` is the next event that can move Persona 1 out of pure hypothesis; nothing currently planned tests Persona 2 directly until the student supply-side test triggers on the decision rule.
