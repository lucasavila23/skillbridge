# Persona: The Tinkerer

**Version:** 0.3 — 2026-09-22

**Grounding status:** Partial participant-reported grounding; broader pattern and client delivery unvalidated.

**Use:** Research rehearsal and planning real-user validation.

Version 0.3 incorporates UV-S01 from the teammate-reported interviews received
on 2026-09-22. The user identifies Student 1 as an IE University student and
dates the interviews to September 15–20; the individual date and original
source material are unspecified. This is a reported account, not an observed
project or a verified transcript.

This is one bounded behavioural hypothesis about a tech student seeking
experience. It does not represent a verified individual or all tech students.
The business-owner perspective discussed during the exercise is separate from
this persona.

## Target-user profile contribution

- **Context, frequency and trigger:** A tech student applying for internships or
  jobs, or considering business projects. UV-S01 Q1 reports an application
  requesting GitHub and project examples, prompting uncertainty about whether
  coursework counted. An explicit experience requirement in the listing,
  frequency and the next action taken remain unconfirmed.
- **Progress sought:** A useful portfolio project (UV-S01 Q5). The same student
  reports choosing paid tutoring over a competition when money was needed;
  this does not establish pay as the main motive for coding or sustained work.
- **Most relevant current behaviour:** Built a study planner with two classmates,
  contributed the frontend and needed database-integration help. Weekend work
  paused during exams; core features were completed but calendar integration was
  dropped (UV-S01 Q2–Q3). These are reports, not inspected work traces.
- **Current alternative:** Coursework and collaborative student projects are
  reported; a solo-project default or switching sequence is not established.
- **Main friction or consequence:** Uncertainty about presenting coursework as
  experience, plus a need for integration help. Insufficient business relevance
  and adverse hiring consequences remain hypotheses.
- **Tool or service behaviour:** UV-S01 Q2 reports adapting a component library.
  A general preference for tool customisation and competence to deliver client
  work are not established by that single example.
- **Trust and control pattern:** Comfortable letting tools access relevant
  project files and assist with building, debugging and organising work, while
  retaining the ability to inspect, modify or override outputs. Wants control
  over technical decisions and approval of submissions or publication on their
  behalf. This is a working assumption, not a demonstrated permission boundary.
- **Verification and recovery pattern:** UV-S01 Q4 reports professor/friend
  review and simplifying task creation after feedback about too many steps.
  Inspecting tool outputs, independently debugging and tolerating rough edges
  remain working assumptions; they were not demonstrated by this account.
- **Failure threshold:** Would stop relying on an approach when repeated failures
  cost more time than it saves, or when they cannot inspect or modify the result.
  This is a hypothetical threshold, not an observed abandonment event.
- **Evidence anchors:** [UV-S01 Q1–Q6](../validation/interviews-2026-09-22.md#uv-s01),
  supplied as a teammate's notes. The earlier workshop remains the source of
  untested tool-control and failure-threshold hypotheses.
- **Working assumptions:** The reported behaviour recurs across situations;
  portfolio value and pay motivate client-project participation; the proposed
  trust, technical-control and failure patterns apply. None is established as
  a stable preference or a cause of sustained commitment.
- **Known unknowns:** Application-to-project chronology; actual contributions
  over time; frequency; measured availability; independent technical capability;
  needed support; client acceptance and hiring outcomes.
- **Decision this Persona may affect:** Whether SkillBridge can rely on students
  to sustain participation and deliver work a business accepts using
  coursework-level skills with light scaffolding. The decision requires real
  evidence; a persona response cannot settle it.

## Evidence boundaries

### GROUNDED

The following grounding is **participant-reported**, with source limitations
recorded in UV-S01; it is not independent observation:

- Q1: application requested GitHub and project examples.
- Q2–Q4: component-library adaptation, database help, an exam pause, reduced
  scope, and revision following professor/friend feedback.
- Q5: portfolio motivation and a past choice of paid tutoring over a competition.
- Q6: stated requirements for technical clarity, team/support information,
  portfolio permission and a finite commitment. These are intentions, not an
  accepted offer or completed client project.

Exam interruption and reduced scope challenge any claim that an interest in
experience guarantees dependable availability. Neither student enthusiasm nor
tool adaptation proves business-ready delivery.

### WORKING ASSUMPTIONS

The tool-permission boundaries, technical-control preferences, failure
threshold and generalisation beyond this episode remain workshop assumptions.
The label is a research hypothesis, not the participant's confirmed identity.
First-person rehearsal language remains synthetic, not an interview quote.

### UNKNOWN

The reported project supplies an initial episode, but no work trace links
motivation, actual hours and acceptable business output. No commitment rate,
hours threshold, campaign completion rate or client acceptance result is known.

## Assumptions this persona should help challenge

Selected by the user in Question 8; both remain unvalidated:

1. **Sustained commitment:** Students will commit real, sustained hours to a
   campaign. Whether gaining experience and a money incentive sustain that
   commitment remains open.
2. **Delivery with coursework-level skills:** Coursework-level skills and light
   scaffolding are enough to deliver something a real small business accepts.

These correspond to Area 1 in [the assumption map](../assumptions.md#area-1-student-pull--delivery-capability).
This selection defines the persona's research focus; it does not establish a
new venture-wide risk ranking or a completed student-supply test.

## Exactly three real-user validation priorities

1. **Recent behaviour and commitment:** Ask a student to walk through their most
   recent project from starting to finishing or stopping. With their permission,
   inspect anonymised progress records for actual contributions over time and
   ask what affected their decision to continue.
2. **Practical delivery:** Observe a student using their current skills on a
   bounded real-business task with agreed acceptance criteria. Record the help
   and rework needed, then have the business assess the output against those
   criteria.
3. **Tools, control and recovery:** Ask the student to show a recent occasion
   when a tool's output was wrong: what they checked, what they changed and how
   they decided the result was usable. Use a sanitised example that does not
   expose private project information.

## Sources and companion output

- [Persona Builder exercise](../../downloads/ai-prompt-persona-builder.md).
- Persona workshop conversation, 2026-09-17, Questions 1–8: working hypotheses
  and the user's selected label and assumptions; no real-user episode supplied.
- Subsequent JTBD conversation, 2026-09-17: user-supplied trigger and money
  incentive, retained as hypotheses where not supported by the new notes.
- [UV-S01 interview record](../validation/interviews-2026-09-22.md#uv-s01)
  and [cross-interview findings](../validation/findings-2026-09-22.md).
- [Current JTBD hypothesis](../jtbd.md): revised application trigger and
  claim-level evidence status.
- [Opportunity](../opportunity.md): venture context, not validation of this persona.
- [Goals](../goals.md): team intent, not customer evidence.
- [Assumptions](../assumptions.md): the two selected student-side risks.
- [Complete Persona Agent prompt](tinkerer-agent-prompt.md): standalone prompt
  for a fresh conversation.

**Readiness:** Ready for research rehearsal with explicit evidence boundaries.
Synthetic Persona answers are hypotheses for research rehearsal, never customer
evidence. Real-user validation remains open.
