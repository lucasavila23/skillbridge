# Dev Ecosystem Bootstrap

## What this file is

A portable bootstrap for **new** projects. It is **not** a `CLAUDE.md`. Keep it
outside any repo — e.g. `~/dev-ecosystem-bootstrap.md` or a private gist.

When you start a new project, tell Claude:

> Read `~/dev-ecosystem-bootstrap.md` and bootstrap this project.

Claude then runs the steps below: installs the toolchain you rely on, generates a
project-local `skills.md`, and wires a lookup rule so every future
"I need a skill / MCP for this" check consults `skills.md` **before** searching a
marketplace or installing anything new.

This file is the **master seed**. `skills.md` is the **per-project working copy**.
Update this file when you adopt a new tool you want in every future project.

---

## Rules for Claude when this file is invoked

1. Work top to bottom. Every step is idempotent — check before acting.
2. Before running **any** install command, show the full list of what you intend
   to install and wait for a "yes". Never install silently.
3. After the toolchain is in place, generate `skills.md` at the project root from
   the Appendix, adapted to this project's detected stack.
4. Add the **Lookup Rule** (Step 3) to the project's `CLAUDE.md`, creating the
   file if it does not exist.
5. Report what was installed, what was skipped (already present), and what failed.
6. Do not copy the persona / output-style of any past project into this one
   unless asked.

---

## Step 1 — Toolchain install

> Verify exact CLI syntax with `claude plugin --help`, or use the interactive
> `/plugin` menu. Commands below reflect the current known form.

### 1a. Plugin marketplaces

Register these (skip any already listed by `claude plugin marketplace list`):

```
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin marketplace add Gentleman-Programming/engram
```

### 1b. Plugins (skills + MCP servers)

Check `claude plugin list` first; skip anything already installed at user scope.
Install from `claude-plugins-official` unless noted.

| Plugin | Gives you | Install | Always? |
|--------|-----------|---------|---------|
| `superpowers` | brainstorming, TDD, systematic-debugging, writing/executing-plans, subagent-driven-development, verification-before-completion, requesting/receiving-code-review, git worktrees, parallel agents | `claude plugin install superpowers@claude-plugins-official` | yes |
| `code-review` | `/code-review` on a diff or PR | `claude plugin install code-review@claude-plugins-official` | yes |
| `pr-review-toolkit` | `/review-pr` + specialist agents (silent-failure-hunter, type-design-analyzer, pr-test-analyzer, code-simplifier, comment-analyzer) | `claude plugin install pr-review-toolkit@claude-plugins-official` | yes |
| `frontend-design` | distinctive, non-templated UI direction | `claude plugin install frontend-design@claude-plugins-official` | if UI |
| `context7` | live library/framework docs (MCP) | `claude plugin install context7@claude-plugins-official` | yes |
| `playwright` | browser automation, screenshots, visual verification (MCP) | `claude plugin install playwright@claude-plugins-official` | if UI |
| `supabase` | Supabase/Postgres tools + best-practice skills (MCP) | `claude plugin install supabase@claude-plugins-official` | if Postgres |
| `github` | PR / issue / repo operations (MCP) | `claude plugin install github@claude-plugins-official` | if GitHub |

### 1c. Standalone skills (not bundled in a plugin)

Locate the exact source with the `find-skills` skill, then install. Confirm the
resolved source with me before running.

| Skill | Purpose | How to get it |
|-------|---------|---------------|
| `grill-me` | Interviews you relentlessly about a plan or design until every branch of the decision tree is resolved. Run before locking a plan. | `find-skills` to resolve source → `npx skills add <source>` |

### 1d. Optional MCPs (install only if the project needs them)

| MCP | When | Source |
|-----|------|--------|
| `codegraph` | large codebase — structural / call-graph / blast-radius queries | `codegraph init` in the repo (separate CLI) |
| `Gamma` | generating presentation decks / documents | claude.ai connector, or its plugin |
| `engram` | cross-session persistent memory beyond the native file memory | `claude plugin install engram@engram` |

If the native file-based memory is enough, skip `engram`.

---

## Step 2 — Generate `skills.md`

Create `skills.md` at the project root. It is the project's **skill & MCP
registry** and the first place to look before installing or searching for
anything.

Template:

```markdown
# skills.md — project skill & MCP registry

> Before installing a new skill or MCP, or searching a marketplace, check this
> file first. If the capability is listed, use it. If not, resolve it, install
> it, then ADD an entry here with a one-line "when to use".

## Active in this project
<skills / MCPs installed AND used here — trigger + how to invoke>

## Available but unused
<installed, not yet needed here>

## Known from past projects (seed catalog)
<paste the Appendix of dev-ecosystem-bootstrap.md verbatim>

## Added this project
<anything installed mid-project — date + reason + how to invoke>
```

Populate **Active in this project** from the detected stack:

- Always: `superpowers` (brainstorming, TDD, systematic-debugging,
  verification-before-completion), `code-review`, `pr-review-toolkit`,
  `grill-me`, `context7`.
- Web frontend: `frontend-design`, `ui-ux-pro-max` / `ui-styling`, `playwright`.
- Postgres / Supabase: `supabase` + `supabase-postgres-best-practices`.
- Python / FastAPI: `fastapi-python`.
- Decks / marketing in scope: `pptx`, `slides`, `Gamma`.

---

## Step 3 — The Lookup Rule (append to the project `CLAUDE.md`)

```markdown
## Skill & MCP lookup

Before invoking, installing, or searching for any skill or MCP:

1. Read `skills.md` at the project root.
2. Listed under "Active" or "Available" → use it. Do not search the marketplace.
3. Listed under "Known from past projects" → install it, then move the entry to
   "Active".
4. Not in `skills.md` at all → use the `find-skills` skill or `/plugin` to
   search. After installing, add an entry under "Added this project" with a
   one-line trigger + how to invoke.
5. Never install a skill / MCP without first showing me the candidate and why.
```

---

## Appendix — Skill & MCP catalog

Seed data for `skills.md` → "Known from past projects". Source project: **ViralTrans**
(fleet management; FastAPI + PostgreSQL + Supabase + N8N; 2026).
Each entry: what it is · when it earned its place · how to invoke.

### Process / workflow

- **superpowers:brainstorming** — explore intent and requirements before any
  feature or behavior change. Invoke at the very start, before planning.
- **superpowers:writing-plans** — turn a spec into an ordered, checkpointed plan
  for a multi-step task.
- **superpowers:executing-plans** — execute a written plan with review
  checkpoints, in a fresh session.
- **superpowers:subagent-driven-development** — implement independent plan tasks
  via subagents in the current session.
- **superpowers:dispatching-parallel-agents** — 2+ independent tasks, no shared
  state; fan them out.
- **superpowers:test-driven-development** — every feature / bugfix: failing test
  first. Ran in strict mode on ViralTrans.
- **superpowers:systematic-debugging** — any bug or unexpected behavior:
  reproduce, hypothesize, prove. Used for the calendar monto-string bug and the
  orphaned `auth.users` bug.
- **superpowers:verification-before-completion** — before claiming done or
  committing: run the commands, show the output. Non-negotiable.
- **superpowers:requesting-code-review** — before merging a feature.
- **superpowers:receiving-code-review** — when acting on review feedback; verify
  before implementing.
- **superpowers:finishing-a-development-branch** — deciding how to integrate a
  completed branch.
- **superpowers:using-git-worktrees** — isolate feature work from the current
  workspace.
- **judgment-day** — explicit blind dual review with bounded fix rounds. Used for
  the autonomous PR-chain merges on the UI redesign.
- **grill-me** — stress-test a plan or design by relentless interview until every
  decision branch is resolved.

### Review

- **code-review:code-review** — `/code-review` on the current diff or a PR;
  correctness bugs + simplification. Levels low → ultra.
- **pr-review-toolkit:review-pr** — full multi-agent PR review.
- **pr-review-toolkit:silent-failure-hunter** — hunts swallowed errors and bad
  fallbacks. High value after error-handling changes.
- **pr-review-toolkit:type-design-analyzer** — reviews new types for
  encapsulation and invariants.
- **pr-review-toolkit:pr-test-analyzer** — test coverage / quality on a PR.
- **pr-review-toolkit:code-simplifier** — post-implementation clarity pass.
- **pr-review-toolkit:comment-analyzer** — comment accuracy / rot.

### Stack — Python / FastAPI / Postgres / Supabase

- **fastapi-python** — FastAPI best practices, async patterns. Core backend stack.
- **supabase:supabase** — any Supabase task: Auth, RLS, Edge Functions,
  migrations, client SSR, log queries, error triage.
- **supabase:supabase-postgres-best-practices** — load **before** writing or
  changing anything in Postgres: tables, column types, RLS policies + tests,
  indexes, triggers, functions, pg_cron / pgmq, pgvector, slow-query diagnosis.

### Frontend / design

- **frontend-design:frontend-design** — distinctive, non-templated UI direction.
  Used across the frontend redesign v1 / v2.
- **ui-ux-pro-max** — UI/UX database: styles, palettes, font pairings, UX
  guidelines, motion presets, chart types across many stacks.
- **ui-styling** — shadcn/ui + Tailwind + accessible components (dialogs,
  dropdowns, forms, tables), dark mode, theming.
- **design-system** — three-layer token architecture
  (primitive → semantic → component), component specs.

### Documents / decks

- **pptx** — any `.pptx` / `.potx`: create, read, edit. Built the 12-slide
  investor deck (PR #222).
- **slides** — strategic HTML presentations with Chart.js and design tokens.

### PR / repo hygiene

- **chained-pr** — split changes > 400 lines into stacked, individually
  reviewable PRs. The UI redesign chain (~30 PRs).
- **branch-pr** — create PRs with issue-first checks.
- **work-unit-commits** — plan commits as reviewable work units; tests + docs
  travel with the code.
- **issue-creation** — structured GitHub issues / bug reports.

### MCPs

- **supabase** — migrations, `get_advisors` (catches bad RLS + missing indexes),
  `query_logs`, `list_tables` before schema changes, `execute_sql`.
  Heaviest-used MCP on ViralTrans.
- **playwright** — screenshots for the investor deck; visual verification of the
  frontend redesign (not just green tests).
- **context7** — up-to-date library / framework docs; beats web search for API
  syntax and migration guides.
- **codegraph** — structural questions: call flow, callers / callees, blast
  radius, "how does X work". One call replaces a grep + read loop. Needs
  `codegraph init` per repo.
- **Gamma** — AI presentation / document generation; alternative path for decks.
- **github** — PR / issue / repo operations. (Configured on ViralTrans; auth
  failed one session — check the token.)
- **engram** — cross-session persistent memory (Gentleman-Programming). Optional
  if the native file memory suffices.

---

## Maintenance

- Adopted a tool you want in **every** future project → add it to the Appendix
  here.
- Tool turned out stack-specific → leave it in the Appendix but note the
  condition ("if Postgres", "if UI").
- Dropped a tool for good → delete its Appendix entry so it stops being seeded.
