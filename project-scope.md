# Project Scope — SkillBridge

Living document. Captures the concept, the class context, what we've decided, what's
still open, and a running log of our working sessions. **Updated after every round
of questions.**

Companion working files (also kept current):
- `opportunities.md` — compiled Empathize/Define material (feeds `evidence-log/opportunity.md`)
- `assumptions.md` — compiled assumption brainstorm (feeds `evidence-log/assumptions.md`)
- `evidence-log/goals.md` — confirmed Product Goal and current Sprint Goal
- `evidence-log/experiment-card.md` — current concierge test plan and precommitted decision rule

---

## 1. One-liner

SkillBridge is a platform where tech students and aspiring professionals join small,
real projects ("campaigns") from small businesses and brands — building a CV full of
hands-on work, earning certification and a bit of cash, and getting a faster route
into the industry.

## 2. How it works (concept)

- A small business (e.g. a local burger shop that wants a website) posts a
  **campaign**: a scoped, real deliverable that doesn't justify hiring an agency
  or a senior freelancer.
- Tech students / aspiring professionals **join** a campaign based on interest and fit.
- They form a **team** and deliver the project together, learning how to work with
  other people, what the real-world scope of their classroom skills actually is,
  and how to deal with a real client.
- Outcomes for the student: **CV-able hands-on projects**, a **verified
  certification** from the platform, some small income, and a faster path to a
  first job/internship.

**Certification model = A + C:** a platform-issued *"verified campaign"* record
(deliverable attached, scope, dates, role) **plus** a *rating/reference from the
business*. Proof-of-work, not an exam. **Future:** auto-publish these to the
student's **LinkedIn** profile.

Two-sided marketplace, but **the student is the primary market and the design focus.**
Small businesses are the supply of projects — important, but treated as an
assumption to validate, not the user we design for.

## 3. Class context

- Course: *Rapid Prototyping with AI* (4th-year elective).
- The `downloads/` prompts and `evidence-log/` structure are the **professor's
  prescribed method** for prototyping with AI — the required workflow, not our
  invention.
- Flow: Opportunity → Assumptions → Goals → (recruit users) → Experiment →
  Evidence log.
- **Semester-long project, running until December 2026.**
- **Team size: 5–6 people.**
- AI's role in this repo: brainstorming partner + keeper of `opportunities.md`,
  `assumptions.md`, `goals.md`, and `evidence-log/ai-usage-log.md`. Every AI
  working session is logged.

## 4. The person behind the idea

The founder (Lucas) has **personally experienced** this pain. Getting a first
internship was very hard: rejected repeatedly by bigger companies, and the first
break came from a startup that was deliberately recruiting people *without* much
experience — effectively "fishing" among candidates the big firms had turned down.
With something like SkillBridge, that first experience would have come much faster.
Many peers hit the same wall.

---

## 5. Decisions log

| Date | Decision | Status |
|---|---|---|
| 2026-09-08 | Concept = campaign-based platform matching student teams to small-business projects | ✅ confirmed |
| 2026-09-08 | The idea is genuinely felt first-hand by the founder | ✅ confirmed |
| 2026-09-08 | **Primary user / market = the student / aspiring professional** (not the business) | ✅ confirmed |
| 2026-09-08 | **Starting segment = tech students** | ✅ confirmed |
| 2026-09-08 | **Core pain point = "experience without experience" — real, CV-able hands-on projects** | ✅ confirmed |
| 2026-09-08 | Platform issues a **certification** per completed campaign — model = **A + C** (verified-campaign record + business rating), no exam | ✅ confirmed |
| 2026-09-08 | **Future:** push verified certifications to the student's **LinkedIn** profile | 🔭 future scope, not v0 |
| 2026-09-08 | Target user refined: the **normal** tech student — no strong network, not top-5% GPA (the connected students already get in via referrals) | ✅ confirmed (from research) |
| 2026-09-08 | Project duration = whole semester, until **December 2026** | ✅ confirmed |
| 2026-09-08 | Team size = **5–6 people** | ✅ confirmed |
| 2026-09-08 | Prototype medium (`prototype-v0`) | ⏳ undecided — decide as project develops |
| 2026-09-08 | Assignment logistics: exact deadlines, # of recruited testers, rubric | ❓ deferred (grill Q5) |
| 2026-09-08 | Repo initialised: private `github.com/lucasavila23/skillbridge`, `main` protected (PR + 1 approval) | ✅ confirmed |
| 2026-09-08 | GitHub MCP (`github@claude-plugins-official`) adopted for PR/issue tooling | ✅ confirmed (activation pending token + restart) |
| 2026-09-09 | Product Goal and current Sprint Goal recorded in `evidence-log/goals.md`; Product Goal includes student experience and completed projects for businesses; Sprint Goal addresses business willingness to entrust paid projects to inexperienced student teams | ✅ user-confirmed via confirm-check |
| 2026-09-09 | Experiment Card recorded: concierge test, 10% conditional deposit, ≥ 2/10 conversions, separate five-pitch follow-up for 1/10, 10-day response window, and Project Kickoff within 5 business days | ✅ plan recorded; test results pending |
| 2026-09-09 | Pilot projects are delivered by student teams; pitch profiles show individuals from the available talent pool, with final team composition and project matching after the deposit | ✅ user-confirmed |

## 6. Open questions

**Round 1 — resolved:** idea one-liner; founder's first-hand standing; prototype
form parked; AI usage (prompts = brainstorming tools, usage log maintained).

**Round 2 — resolved:** primary user = students; segment = tech; pain point =
experience-without-experience / CV-able projects; founder's concrete situation
captured; duration & team size set. Q5 (logistics) deferred.

**Round 3 — resolved:**
1. Current student path — researched & written up in `opportunities.md` (typical
   path vs the connected top-tier path; referral vs cold-application data).
2. Existing alternatives — table of 6 alternatives + why each fails, in `opportunities.md`.
3. Certification = **A + C**, future LinkedIn sync.
4. Frequency/scale — partly covered by market research; still want the founder's
   own peer estimate and choice of *the* headline trend (open, low priority).

**Round 4 — done (autonomous):** ran the Opportunity + Assumptions exercises
end-to-end. Framing locked (section 7). Assumption map locked (section 7b).

**Goals — complete (2026-09-09):** ran the First pass / Quick exercise. The user
drafted both goals and confirmed the refined wording in `evidence-log/goals.md`.
The Sprint Goal links to the existing riskiest assumption in section 7b.

**Experiment Card — complete (2026-09-09):** all six fields recorded in
`evidence-log/experiment-card.md`. The current plan uses a concierge test with
actual, available student profiles, delivery by student teams, and real business
payment commitments.
Recruitment channels, participant records, and test results remain to document.

## 7. Problem framing — LOCKED v1 (2026-09-08)

Full version + research + cross-review handoff: `opportunities.md` /
`evidence-log/opportunity.md`. Founder-confirmed direction; sentence wording
AI-drafted and open to adjustment.

- **PAIN POINT:** A tech student with no internship and no industry network can't
  get the real, client-facing project experience employers treat as the deciding
  signal; postings demand experience they can't get without a job, class/tutorial
  projects are discounted, and open marketplaces filter beginners out.
- **USER:** A 2nd–4th-year tech student (software / web / data), solid in
  coursework, with no internship, no professional network, not in the connected /
  top-GPA slice that gets referrals.
- **NEED:** To accumulate a verifiable track record of real, team-delivered client
  projects that an employer will recognise — before having formal experience.
- **INSIGHT:** The founder's first job came from a startup deliberately recruiting
  the candidates big firms rejected — demand for inexperienced talent exists but
  is invisible and unmatched; early winners rely on connections, not ability; and
  no existing option combines real paying client + shipped deliverable + team +
  open access + a portable verified credential.
- **HOW MIGHT WE:** How might we give an unconnected tech student an open,
  merit-based way to build a verified record of real, team-delivered client work
  before they have any formal experience?
- **Combined:** *An unconnected 2nd–4th-year tech student needs to accumulate
  verified, team-delivered client projects because employers treat real client
  experience as the deciding hiring signal, the demand for junior talent already
  exists but is unmatched and invisible, and the normal route in runs on
  connections they don't have.*

## 7b. Assumption map — LOCKED v1 (2026-09-08)

Full version: `assumptions.md` / `evidence-log/assumptions.md`.

- **Area 1 — Student pull & delivery capability:** will enough unconnected students
  commit real hours; can 5–6 strangers deliver without a PM; are coursework skills
  enough to ship acceptable work; is dropout low enough.
- **Area 2 — Business supply & trust:** do the "too small for an agency" projects
  exist; will an SMB hand a real *paid* project to a student team; will they pay;
  is quality good enough to avoid burning them; can both sides bootstrap despite
  chicken-and-egg.
- **Area 3 — Credential credibility:** do recruiters weight a verified-campaign
  record + rating; do students believe it enough to join for it; does verification
  resist gaming; will LinkedIn/ATS treat it as legitimate.
- **RISKIEST:** *An SMB will hand a real, paid project to a team of inexperienced
  students* — the supply the whole loop depends on, least controllable, hardest to
  fake in a pilot, least evidenced. Current test design (2026-09-09): the concierge
  plan in `evidence-log/experiment-card.md`, with ten primary business pitches
  and a separate five-pitch extension only if the decision rule triggers it.

## 8. Next steps

1. ~~Run the Opportunity exercise~~ ✅ `evidence-log/opportunity.md` locked v1.
2. ~~Run the Assumptions exercise~~ ✅ `evidence-log/assumptions.md` locked v1.
3. Founder review pass on the locked wording; adjust any phrasing.
4. ~~Set Goals~~ ✅ Product Goal and current Sprint Goal confirmed in `evidence-log/goals.md` (2026-09-09).
5. Recruit 5+ target students for interviews; document the available student pool and access to 10 qualifying businesses (+5 only if the extension is triggered) → `evidence-log/recruitment.md`.
6. Run the concierge test using `evidence-log/experiment-card.md` and record the results.
7. ~~Design the experiment~~ ✅ All six fields recorded in `evidence-log/experiment-card.md` (2026-09-09).
8. Decide prototype medium, build `prototype-v0`.
9. Pin assignment logistics with the professor (deadlines, # testers, rubric).

---

## Session notes

### 2026-09-08 — Setup + concept intake
- Bootstrapped repo toolchain; created `downloads/`, `evidence-log/`, `prototype/`.
- Duplicated `ai-prompt-opportunity.md` and `ai-prompt-assumptions.md` into `downloads/`.
- Ran grill Rounds 1–2 on the SkillBridge concept.

### 2026-09-08 — Round 2 answers
- Primary market = the student/aspiring professional; the platform is "for them".
- Narrow to **tech** students first.
- Pain point = **getting experience without experience**: real hands-on projects
  you can put on your CV so employers see proven capability. Class projects feel
  fake/disposable; what matters is CV-visible, real work.
- Founder's story: hard first-internship search, many rejections from big
  companies, first break at a startup that specifically wanted low-experience
  people. SkillBridge would have shortened that path.
- Logistics: semester-long, runs to **December 2026**, team of **5–6**.
- Created `opportunities.md` and `assumptions.md` as running compilation files.

### 2026-09-08 — Round 3 answers + desk research
- **Certification** confirmed as **A + C** (verified-campaign record + business
  rating); future feature = auto-sync to **LinkedIn**.
- **Existing alternatives** — followed the recommendation; 6-row "why it fails"
  table added to `opportunities.md` (Upwork/Fiverr, Forage, Riipen, hackathons,
  open source, unpaid internships).
- **Ran desk research** on how normal tech students actually get first experience.
  Key findings folded into `opportunities.md`:
  - New-grad hiring at the 15 biggest tech firms **down >50% since 2019**;
    ~**666** SWE intern postings nationwide (~1 per **165** CS grads/yr).
  - Recent CS-grad unemployment ~**6.1%**, underemployment ~**41%**.
  - Referrals convert at ~**30–60%** vs ~**0.1–2%** for cold applications — so the
    connected / top-GPA students are on a different track; the "normal" student is
    our user.
  - Tutorial-grade side projects no longer differentiate; employers want real
    problems / shipped work.
- User's steer: focus the user definition on the **normal** student, not the
  top-5% with connections.

### 2026-09-08 — Round 4: Opportunity + Assumptions run autonomously
- Per founder instruction ("do all of this by yourself"), ran both exercises
  end-to-end and locked v1.
- Launched a research subagent for the competitive landscape (Riipen, Parker
  Dewey, Forage, Extern, MLH, Catchafire, Contra, bootcamp dev-agencies,
  university capstones), SMB demand, and credential-credibility evidence.
- Key competitor conclusion: **no existing option combines** real paying SMB
  client + shipped deliverable + delivery team + open access + a portable verified
  credential — that's SkillBridge's wedge.
- Key evidence added: 66.8% of grads cite lack of experience as #1 obstacle;
  no-internship students average 0.77 offers (vs 1.61 for paid interns); SMB
  website spend median ~$5k; skills-based hiring claimed by ~70–81% of employers
  but <1 in 700 hires actually affected by dropping degree requirements → verified
  real work beats unverifiable claims.
- **LOCKED:** PAIN/USER/NEED/INSIGHT/HMW + combined sentence (section 7);
  3-area assumption map + riskiest assumption (section 7b).
- **Riskiest assumption:** an SMB will hand a real, paid project to an
  inexperienced student team.
- Wrote clean deliverables to `evidence-log/opportunity.md` and
  `evidence-log/assumptions.md`; full working versions + cross-review handoff
  blocks in `opportunities.md` / `assumptions.md`.
- Still open: primary interviews; assignment logistics; certification anti-gaming
  design; Goals exercise (awaiting `ai-prompt-goals.md`).

### 2026-09-08 — Experiment Card grill + repo init
- Added `downloads/ai-prompt-experiment-card.md`. Ran `/grill-me` over the
  Experiment Card for the riskiest assumption (17 questions, full design tree).
- Draft card agreed in-chat (fake-door demand test + problem-evidence rider;
  conversion-rate metric + reason-cluster co-output; count threshold with a
  cold-lead floor; MEDIUM tiered evidence strength; full met/missed/ambiguous
  decision rule). **Not** written to `evidence-log/experiment-card.md` yet —
  founder wants it parked. Product/Sprint Goal still an open gap.
- **Repo initialised.** `git init` + `.gitignore` + initial commit; created
  private `github.com/lucasavila23/skillbridge` and pushed `main`.
- `main` branch protection on: PR required + 1 approving review, stale reviews
  dismissed, no force-push / no deletion. Admin bypass left on for bootstrap.
- Installed `github@claude-plugins-official` MCP (remote server, auth via
  `GITHUB_PERSONAL_ACCESS_TOKEN`). `gh auth token` verified against the endpoint
  (HTTP 200). **Pending:** founder exports the token + restarts Claude Code;
  `/mcp` to confirm.
- Added `.github/PULL_REQUEST_TEMPLATE.md`. Promoted github entry to Active in
  `skills.md`.
- **Pending:** teammate GitHub usernames to add 5 collaborators.
- Note: `.gitattributes` declares Git LFS for `prototype/*.{pdf,png}` but
  `git-lfs` is not installed on this machine — install before adding binaries.

### 2026-09-09 — Goals exercise completed
- Ran `downloads/ai-prompt-goals.md` using First pass / Quick mode, carrying
  forward the existing Opportunity and riskiest assumption.
- The user drafted the Product Goal around students gaining real experience,
  then explicitly added the business benefit of getting real projects completed.
- The user drafted the Sprint Goal; clarified that the uncertainty concerns
  businesses trusting inexperienced student teams with real, paid work.
- The user accepted the final confirm-check for both goal sentences. Saved that
  exact wording in `evidence-log/goals.md`.
- Both goals are confirmed; no open fields remain in the Goals exercise.
  Primary interviews, recruitment records, and the saved Experiment Card remain
  outstanding. Experiment methods, metrics, and thresholds belong in that card.

### 2026-09-09 — Experiment Card exercise completed
- Ran `downloads/ai-prompt-experiment-card.md` as First card / Quick, carrying
  forward the confirmed goals and business-side riskiest assumption.
- The user confirmed the hypothesis through a confirm-check and added
  coursework-level skills. Selected Concierge and drafted the manual service,
  student profiles, client meetings, payment terms, metric, threshold, evidence
  rating, and decision branches.
- Final payment plan: 10% of the project price agreed before work, credited
  toward that price, refundable if the agreed project completion deadline is
  missed. This is the current plan after discussing end-of-project tips,
  success fees, and fixed deposits.
- Primary threshold: at least two businesses out of exactly ten must both sign
  the charter and transfer the deposit. One conversion is recorded as missing
  that threshold and triggers a separately scored five-business extension.
- The user supplied a 10-day charter-signing window in response to the question
  about signing and payment deadlines. Applied it to both required conversion
  actions, for both cohorts, and stated that interpretation before saving.
- The user confirmed that pitch profiles represent actual, available students;
  exact matches happen after business deposits. HIGH is the planned evidence
  strength for conditional financial commitment.
- The five-business-day deadline covers the Project Kickoff Milestone: confirmed
  student match, email or phone introduction, and final mutually signed schedule.
  Project completion follows its separately agreed schedule.
- Saved the six-field card. This replaces the parked September 8 fake-door draft
  as the current experiment design. Results, recruitment records/channels, and
  the low-fidelity prototype and backup remain outstanding.

### 2026-09-09 — Student team delivery clarified
- The user confirmed that the Hypothesis and Method should consistently describe
  delivery by **student teams**. Updated team formation, project matching,
  kickoff introductions, weekly syncs, final evaluation, and decision branches.
- Individual student profiles remain evidence of capability within the available
  talent pool; final team composition and project matching follow the deposit.
