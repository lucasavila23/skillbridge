# Legal Build Constraints — Spain (SkillBridge)

READ THIS FILE before implementing: payments or deposits, student payouts,
any matching/scoring/rating logic, account suspension or dispute handling,
onboarding forms, or the public-facing legal/about page.

This file states hard constraints only, for direct use while coding. Full
legal reasoning, dates, and sources: `docs/legal-spain.md`. Not legal advice —
the items in §B are open decisions for the founders, not defaults to infer.

Rule format: `[ID] MUST / MUST NOT / MAY <requirement>. Why: <one line>.`

---

## A. Hard constraints

### A1 — Payments & deposits
- **[PAY-1]** MUST NOT hold, receive, or transfer business deposits or student
  payouts through SkillBridge's own bank account, a custom wallet, or an
  in-house ledger of client funds.
- **[PAY-2]** MUST route all money movement through a licensed third-party
  payment/marketplace provider (see B1 for which one).
  *Why: holding client funds directly puts SkillBridge inside Bank of Spain
  payment-institution licensing (RD-ley 19/2018).*

### A2 — Automated decisions about students
- **[ALG-1]** MUST NOT let a fully automated process suspend an account, deny
  a payout, or lower a credential rating with no human review step.
- **[ALG-2]** MUST log which human reviewed/approved any such decision, with a
  timestamp.
- **[ALG-3]** MUST be able to produce a plain-language explanation, on
  request, of why a student received a given match, score, or rating.
  *Why: EU Directive 2024/2831 requires human review of decisions with an
  effect equivalent to suspension/termination; Spain transposes it by
  2 Dec 2026.*

### A3 — Task-level control
- **[CTRL-1]** MUST NOT enforce fixed working hours, mandatory real-time
  check-ins, or algorithmic task assignment inside a campaign.
- **[CTRL-2]** MAY set and enforce milestone/kickoff deadlines already defined
  in `experiment-card.md` — that's a delivery term, not work direction.
  *Why: platform control over how work gets done is the core test for
  employment-relationship reclassification under Spanish labour law.*

### A4 — AI-assisted matching or evaluation
- **[AI-1]** MUST visibly label any AI-assisted matching, scoring, or
  feedback as AI-assisted at the point a student or business sees it.
- **[AI-2]** MUST log the inputs behind any AI-generated match or score.
  *Why: EU AI Act Annex III covers employment/access-to-self-employment
  systems; high-risk enforcement is deferred to 2 Dec 2027, but the audit
  trail is far cheaper to build now than retrofit later.*

### A5 — Non-EU student work hours
- **[HRS-1]** MUST record hours logged per student per active campaign.
- **[HRS-2]** MUST be able to output a total-hours-this-week figure per
  student on request.
  *Why: non-EU students on a study permit are capped at 30 hrs/week of paid
  work (RD 1155/2024).*

### A6 — Public disclosure
- **[LSSI-1]** MUST publish an About/Legal page showing operator name, NIF,
  and contact details before any public pitch goes out.
- **[PRIV-1]** MUST publish a privacy notice and MUST NOT collect more
  personal data than a campaign requires, before any real student/business
  data is collected.

### A7 — Contract consistency
- **[SYNC-1]** MUST keep the charter's deposit percentage, refund conditions,
  and IP-assignment terms in one source of truth referenced by both the
  checkout flow and `experiment-card.md`. MUST NOT hardcode these numbers in
  more than one place.

---

## B. Do not decide — ask a human

- **[B1]** Which payment provider to integrate (Stripe Connect / MangoPay /
  PayComet / other) — founders' commercial decision.
- **[B2]** Whether students invoice the business directly, or SkillBridge
  invoices the business and pays students separately — changes who carries
  the RETA/tax exposure.
- **[B3]** The pricing method itself (flat tiers / hourly cap / business-
  stated budget) — must be defined once, documented, then applied
  consistently.
- **[B4]** Whether IP assignment triggers "on delivery" or "on full payment."

If a task touches one of these and no answer exists yet in the repo, stop and
ask — do not pick a default and proceed.

---

## Reference
Full citations and reasoning: `docs/legal-spain.md`. Rule IDs above are
stable — use them in PR descriptions or code-review comments
(e.g. "resolves PAY-1") so violations stay traceable.
