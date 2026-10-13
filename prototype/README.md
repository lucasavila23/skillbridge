# SkillBridge prototypes

## v1: challenge platform (current, updated 2026-10-13)

Open [prototype-v1.html](prototype-v1.html) in a browser; it works offline.
Updated on 2026-10-13 to match the decisions taken after the v2 interviews:
AI scores are labelled, the engineer scores a sample that includes
lower-ranked entries and writes feedback on every certified result, results
are private by default, and the certificate always shows the true score. The
version presented on 2026-10-12 is kept in
[backups/v1-2026-10-12/](backups/v1-2026-10-12/README.md).
Exports: [prototype-v1.pdf](prototype-v1.pdf) (all four steps) and
[prototype-v1-backup.png](prototype-v1-backup.png) (step 1).

1. **Challenge brief:** an illustrative data company's 4-hour brief, rubric
   weights, solo or team of up to 3, free entry, optional €15 certified result.
2. **Team submission:** each member's contribution from commits and tasks,
   confirmed by teammates.
3. **Score and feedback:** AI rubric and engineer scores side by side, written
   feedback, and the "Certify my result" choice (simulated payment). This is the
   moment the [experiment card](../evidence-log/experiment-card.md) measures.
4. **Certificate and profile:** what a recruiter sees, with stacked results.

Everything shown (company, students, scores, feedback) is invented for the
walkthrough. It demonstrates the v2 flow; it is not evidence.

## v0: paid project for a small business (history, 2026-09-09)


**Version:** v0 — 2026-09-09.

Open [index.html](index.html) in a browser. It is self-contained and works without
installing dependencies or connecting to a service. The prototype demonstrated
the business commitment flow in the [v1 Experiment Card](../evidence-log/archive/v1-paid-projects/experiment-card.md).

## Walkthrough

1. Inspect an illustrative café website offer, its deliverables, boundaries,
   completion date, and quote.
2. Inspect the student profile templates and the evidence required from actual,
   available students. Teams are formed and matched after the deposit.
3. Review team delivery, the five-business-day kickoff milestone, weekly syncs,
   and final evaluation.
4. Inspect the draft charter summary and deposit conditions. Acknowledge the
   terms, simulate signing, and then simulate the deposit transfer. The owner can
   also rehearse asking a question or declining.

The facilitator controls below the walkthrough change the illustrative title,
deliverables, boundaries, completion date, and total price. The 10% deposit and
remaining price recalculate across the offer and charter. Applying a changed
example clears any simulated commitment.

See [rough-test-plan.md](rough-test-plan.md) for the two-minute rehearsal and
the distinction between rehearsal feedback and live conversion evidence.

## What is illustrative

- The café and website brief are examples selected for the walkthrough.
- **€500** and **9 October 2026** are illustrative values, not an agreed price,
  pricing method, or project deadline.
- Student cards are visibly empty templates, not invented students or claims of
  availability. The two cards do not define the delivery team size.
- The charter is a summary for inspection, not a complete agreement. Signature,
  transfer, and feedback actions are simulated in this page. There is no payment
  integration, submission service, or persisted participant record.

The artifact makes the risky step inspectable. Live testing still requires the
pricing method, real business/project details, actual student evidence, a usable
charter and payment route, and recruitment records. No actual experiment results
are produced by clicking through this demo.

## Versioned backups

[backups/v0-2026-09-09/](backups/v0-2026-09-09/) contains the v0 walkthrough,
this README, the rehearsal plan, and a SHA-256 manifest.
[backups/v1-2026-10-12/](backups/v1-2026-10-12/README.md) holds the v1 page and
its exports as presented on 2026-10-12.

Keep that snapshot unchanged. For the next reviewed version, update the working
files and version label, then save them into a new version folder such as
`backups/v1-YYYY-MM-DD/`. Record the change in the project scope and AI usage log
when AI is used. Snapshot paths in this README are relative to `prototype/`.
