# skills.md — project skill & MCP registry

> Before installing a new skill or MCP, or searching a marketplace, check this
> file first. If the capability is listed, use it. If not, resolve it, install
> it, then ADD an entry here with a one-line "when to use".

Project: **skillbridge** (Rapid Prototyping with AI). Stack: not yet established —
update the sections below as the stack is chosen.

## Active in this project

Installed at user scope and expected to be used here:

- **superpowers** (`superpowers@claude-plugins-official`) — process backbone.
  - `superpowers:brainstorming` — run first, before planning any feature/behavior change.
  - `superpowers:writing-plans` / `superpowers:executing-plans` — spec → ordered checkpointed plan → execute.
  - `superpowers:test-driven-development` — failing test first for every feature/bugfix.
  - `superpowers:systematic-debugging` — any bug: reproduce, hypothesize, prove.
  - `superpowers:verification-before-completion` — run the commands and show output before claiming done.
  - `superpowers:requesting-code-review` / `receiving-code-review` — around merges.
  - `superpowers:using-git-worktrees`, `superpowers:dispatching-parallel-agents`, `superpowers:subagent-driven-development` — isolation & parallelism.
- **code-review** (`code-review@claude-plugins-official`) — `/code-review` on the
  current diff or a PR; correctness + simplification. Levels low → ultra.
- **pr-review-toolkit** (`pr-review-toolkit@claude-plugins-official`) —
  `/review-pr` full multi-agent PR review plus specialist agents
  (silent-failure-hunter, type-design-analyzer, pr-test-analyzer,
  code-simplifier, comment-analyzer).
- **grill-me** (`~/.claude/skills/grill-me`, from `mattpocock/skills`) —
  stress-test a plan or design by relentless interview until every decision
  branch is resolved. Run before locking a plan. Invoke: `/grill-me`.
- **context7** (`context7@claude-plugins-official`, MCP) — live library/framework
  docs; use before web search for API syntax and migration guides.
- **github** (`github@claude-plugins-official`, MCP) — structured PR / issue /
  repo operations for the team PR workflow; `gh` CLI still fine for quick ops.

## Available but unused

<installed at user scope but not yet exercised in this project — none beyond the Active list>

## Known from past projects (seed catalog)

Seed data from **dev-ecosystem-bootstrap.md**. Source project: **ViralTrans**
(fleet management; FastAPI + PostgreSQL + Supabase + N8N; 2026). Not yet installed
here — install on demand, then move the entry up to "Active".

### Process / workflow

- **superpowers:finishing-a-development-branch** — deciding how to integrate a
  completed branch.
- **judgment-day** — explicit blind dual review with bounded fix rounds. Used for
  autonomous PR-chain merges on the UI redesign.

### Review

- **pr-review-toolkit:silent-failure-hunter** — hunts swallowed errors and bad
  fallbacks. High value after error-handling changes.
- **pr-review-toolkit:type-design-analyzer** — reviews new types for
  encapsulation and invariants.
- **pr-review-toolkit:pr-test-analyzer** — test coverage / quality on a PR.
- **pr-review-toolkit:code-simplifier** — post-implementation clarity pass.
- **pr-review-toolkit:comment-analyzer** — comment accuracy / rot.

### Stack — Python / FastAPI / Postgres / Supabase

- **fastapi-python** — FastAPI best practices, async patterns.
- **supabase:supabase** (`supabase@claude-plugins-official`, MCP) — any Supabase
  task: Auth, RLS, Edge Functions, migrations, client SSR, log queries, error
  triage. Install `if Postgres`.
- **supabase:supabase-postgres-best-practices** — load **before** writing or
  changing anything in Postgres: tables, column types, RLS policies + tests,
  indexes, triggers, functions, pg_cron / pgmq, pgvector, slow-query diagnosis.

### Frontend / design

- **frontend-design:frontend-design** (`frontend-design@claude-plugins-official`)
  — distinctive, non-templated UI direction. Install `if UI`.
- **ui-ux-pro-max** — UI/UX database: styles, palettes, font pairings, UX
  guidelines, motion presets, chart types across many stacks.
- **ui-styling** — shadcn/ui + Tailwind + accessible components (dialogs,
  dropdowns, forms, tables), dark mode, theming.
- **design-system** — three-layer token architecture
  (primitive → semantic → component), component specs.

### Documents / decks

- **pptx** — any `.pptx` / `.potx`: create, read, edit.
- **slides** — strategic HTML presentations with Chart.js and design tokens.
- **Gamma** (MCP, claude.ai connector) — AI presentation / document generation.

### PR / repo hygiene

- **chained-pr** — split changes > 400 lines into stacked, individually
  reviewable PRs.
- **branch-pr** — create PRs with issue-first checks.
- **work-unit-commits** — plan commits as reviewable work units; tests + docs
  travel with the code.
- **issue-creation** — structured GitHub issues / bug reports.

### MCPs

- **playwright** (`playwright@claude-plugins-official`) — browser automation,
  screenshots, visual verification. Install `if UI`.
- **codegraph** — structural questions: call flow, callers / callees, blast
  radius. Needs `codegraph init` per repo (separate CLI).
- **engram** (`engram@engram` marketplace — registered) — cross-session
  persistent memory. Optional if the native file memory suffices.

## Added this project

- **2026-09-08 — github MCP** (`github@claude-plugins-official`) — team project,
  repo now on GitHub; want structured PR/issue tooling. Auto-loads once its token
  env var is set (see local setup notes); `/mcp` to check. Promoted to Active.
