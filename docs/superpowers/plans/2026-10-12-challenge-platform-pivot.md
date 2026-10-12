# SkillBridge v2 Challenge Platform Pivot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Pivot the SkillBridge evidence repo from v1 (paid student projects for small businesses) to v2 (company-calibrated challenge platform) for Group Project I on 2026-10-13, keeping v1 as an archived evidence trail.

**Architecture:** Plain Markdown evidence files in the professor's folder structure. v1 decision files are copied to `evidence-log/archive/v1-paid-projects/` with links fixed; live files are rewritten for v2. One stdlib Python link checker guards every task. Prototype v1 is one self-contained HTML file exported with headless Chrome.

**Tech Stack:** Markdown, Python 3 stdlib, self-contained HTML/CSS/JS, inline SVG, headless Google Chrome for PDF/PNG export.

**Spec:** `docs/superpowers/specs/2026-10-12-challenge-platform-pivot-design.md`

## Global Constraints

- Branch: `group-project-1-structure`. Never push to `main` directly (PR required).
- No new real-user evidence is claimed. Every v2 claim is tagged **Evidence** (with link), **Decision** (team) or **Hypothesis**.
- Competitor facts come from the competitor's own pages, with access date 2026-10-12.
- Revenue hypotheses ranked: 1. students pay a certification fee; 2. companies pay to use challenges as a hiring screen; 3. companies pay a sponsorship. No invented revenue numbers.
- Grading model: automated tests + AI rubric score every submission; a company engineer signs off the rubric and reviews the top submissions.
- Personas: `ai-persona-01` Tinkerer, `ai-persona-02` Late Sprinter, `ai-persona-03` Skeptical Verifier; Once-Bitten Owner goes to `drafts/`.
- One-liner (used verbatim in every live file that states it): **"SkillBridge lets tech students solve short, real challenges set by SaaS, engineering and data companies, and turns each result into a company-calibrated score with a verified record of what each student contributed."**
- Riskiest assumption (verbatim): **"Students will pay for a certified challenge score, because employers treat that score as credible evidence of job-ready skill."**
- Each commit message ends with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## Review Focus

1. Links inside archived copies resolve from their new, deeper location; expected: the link checker reports 0 broken links outside `prototype/backups/`.
2. A live file still describes small businesses, deposits or paid campaigns as the current model; expected: the consistency grep in Task 10 finds such terms only in archive, validation, market-research history notes or explicit "v1" references.
3. A competitor claim with no source; expected: every row added in Task 3 has a URL in `sources.md`.
4. Prototype v1 opened offline (no network) or printed; expected: it renders fully, with all four steps visible in the PDF.
5. Value curve read in the PDF or in grayscale; expected: series are distinguishable by marker shape and label, not colour alone.

---

### Task 1: Link checker

**Files:**
- Create: `tools/check_links.py`

**Interfaces:**
- Produces: `python3 tools/check_links.py` prints each broken `file -> target` and exits 1 if any are found outside `prototype/backups/` and `market-research/sources/`; exits 0 otherwise.

- [ ] **Step 1: Write the script**

```python
"""Report relative Markdown links that do not resolve. Exit 1 if any are found."""
import os, re, subprocess, sys

SKIP = ("prototype/backups/", "evidence-log/market-research/sources/", ".codegraph/")
LINK = re.compile(r"\]\(([^)\s#]+)(?:#[^)]*)?\)")

def broken():
    files = subprocess.run(["git", "ls-files", "-co", "--exclude-standard", "*.md"],
                           capture_output=True, text=True, check=True).stdout.split()
    for f in files:
        if f.startswith(SKIP) or not os.path.exists(f):
            continue
        for target in LINK.findall(open(f, encoding="utf-8").read()):
            if target.startswith(("http:", "https:", "mailto:")):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), target))):
                yield f, target

if __name__ == "__main__":
    bad = list(broken())
    for f, t in bad:
        print(f"{f} -> {t}")
    sys.exit(1 if bad else 0)
```

- [ ] **Step 2: Prove it catches a break**

Run: `printf '[x](nope.md)\n' > tmp-link-test.md && python3 tools/check_links.py; echo "exit $?"; rm tmp-link-test.md`
Expected: prints `tmp-link-test.md -> nope.md` and `exit 1`.

- [ ] **Step 3: Run on the clean repo**

Run: `python3 tools/check_links.py; echo "exit $?"`
Expected: `exit 0`.

- [ ] **Step 4: Commit** — `git add tools/check_links.py && git commit -m "Add Markdown link checker"`

### Task 2: Archive v1 snapshot

**Files:**
- Create: `evidence-log/archive/v1-paid-projects/` (copies of `opportunity.md`, `goals.md`, `assumptions.md`, `experiment-card.md`, `jtbd.md`, `recruitment.md`, `ERRC.md`, `personas/` incl. `drafts/` and the pptx)
- Create: `evidence-log/archive/v1-paid-projects/README.md`

**Interfaces:**
- Consumes: `tools/check_links.py`
- Produces: archive paths that later tasks link to as `archive/v1-paid-projects/<file>` from `evidence-log/`.

- [ ] **Step 1: Copy and fix links.** For each copied file, every relative link `T` is resolved against the original location; if the target was also copied, point to the copy, otherwise point to the live path, both relative to the copy's new folder. Run from repo root:

```python
import os, re, shutil
SRC = "evidence-log"; DST = "evidence-log/archive/v1-paid-projects"
FILES = ["opportunity.md", "goals.md", "assumptions.md", "experiment-card.md",
         "jtbd.md", "recruitment.md", "ERRC.md"]
shutil.copytree(f"{SRC}/personas", f"{DST}/personas")
for f in FILES:
    shutil.copy(f"{SRC}/{f}", f"{DST}/{f}")
copied = {os.path.normpath(f"{SRC}/{f}") for f in FILES}
for root, _, names in os.walk(f"{SRC}/personas"):
    copied |= {os.path.normpath(os.path.join(root, n)) for n in names}
LINK = re.compile(r"(\]\()([^)\s#]+)((?:#[^)]*)?\))")
for root, _, names in os.walk(DST):
    for n in names:
        if not n.endswith(".md"):
            continue
        new = os.path.join(root, n)
        old = os.path.normpath(new.replace(DST, SRC, 1))
        def fix(m):
            t = m.group(2)
            if t.startswith(("http:", "https:", "mailto:")):
                return m.group(0)
            tgt = os.path.normpath(os.path.join(os.path.dirname(old), t))
            dest = tgt.replace(SRC, DST, 1) if tgt in copied else tgt
            return m.group(1) + os.path.relpath(dest, os.path.dirname(new)) + m.group(3)
        s = open(new, encoding="utf-8").read()
        open(new, "w", encoding="utf-8").write(LINK.sub(fix, s))
```

- [ ] **Step 2: Write `README.md`** with: what v1 was (one paragraph, original one-liner quoted from `opportunity.md`), date archived 2026-10-12, why it was archived (business-side trust untested: 0 formal pitches; Nolita: briefing/review cost; stated student capacity 2–7 h/week; 9/11 cannot explain contribution; each linked to its live evidence file), and a table of archived files.

- [ ] **Step 3: Verify** — `python3 tools/check_links.py; echo "exit $?"` → `exit 0`.

- [ ] **Step 4: Commit** — `git add evidence-log/archive && git commit -m "Archive v1 paid-projects evidence snapshot"`

### Task 3: Competitive research for v2

**Files:**
- Modify: `evidence-log/market-research/competitive-analysis.md` (new section "v2 alternatives: challenge and assessment platforms (2026-10-12)")
- Modify: `evidence-log/market-research/sources.md` (append sources)

- [ ] **Step 1: Research** Devpost, HackerEarth, HackerRank, Kaggle, Forage (deeper) from their own pages: who sets the challenge, who scores, what the student receives, team support, individual-contribution record, cost to student, company pricing model, time per challenge.
- [ ] **Step 2: Write** one table row per platform with those columns plus "Gap SkillBridge v2 targets" and "Evidence basis" (Published / Reported / Unknown). Add a "So what" paragraph naming the two strongest alternatives and why.
- [ ] **Step 3: Add sources** to `sources.md` with URL and access date 2026-10-12.
- [ ] **Step 4: Verify** link checker exit 0; every new row has a source.
- [ ] **Step 5: Commit** — `git commit -am "Add v2 challenge-platform competitors with sources"`

### Task 4: Opportunity, JTBD, goals

**Files:** Modify `evidence-log/opportunity.md`, `evidence-log/jtbd.md`, `evidence-log/goals.md`

- [ ] **Step 1: `opportunity.md`** — rewrite: header "v2, 2026-10-12" + link to archive; business idea = the verbatim one-liner; PAIN POINT / USER / NEED / INSIGHT / HOW MIGHT WE / combined sentence / summary table / open gaps / supporting evidence; "Why we pivoted" with linked evidence; Sources.
- [ ] **Step 2: `jtbd.md`** — keep the Job statement and evidence rows; replace "solution hired" and forces with v2 alternatives (from Task 3) and anxieties (time, paying for an unproven certificate, team free-riding); note that the Job is unchanged from v1 and link the archived copy.
- [ ] **Step 3: `goals.md`** — Product Goal (help tech students prove job-ready skill through company-calibrated challenges) and Sprint Goal: "Learn whether students will pay for a company-calibrated challenge score, and whether employers treat that score as credible."
- [ ] **Step 4: Verify** link checker exit 0; one-liner appears verbatim in `opportunity.md`.
- [ ] **Step 5: Commit** — `git commit -am "Rewrite opportunity, JTBD and goals for v2"`

### Task 5: Assumptions, experiment card, recruitment

**Files:** Modify `evidence-log/assumptions.md`, `evidence-log/experiment-card.md`, `evidence-log/recruitment.md`

- [ ] **Step 1: `assumptions.md`** — Area 1 student pull and payment; Area 2 company supply (will companies post and calibrate); Area 3 credential credibility (will employers trust the score). Each assumption tagged Evidence/Decision/Hypothesis with links. MECE check. Riskiest assumption verbatim. Revenue hypotheses ranked 1–3.
- [ ] **Step 2: `experiment-card.md`** — "v1 card: closed 2026-10-12, not run" with reason and archive link. New card: Hypothesis (riskiest assumption); Method: concierge pilot challenge, one company-style brief and rubric, students recruited from the survey list and classmates, entry free, certified score offered for a fee after submission; second arm: show 3+ recruiters/hiring managers anonymised scored certificates and ask whether they would use them to shortlist. Metric: share of submitting students who pay; share of recruiters who say they would shortlist on it. Threshold, evidence strength and a three-branch decision rule (continue / narrow / pivot or stop), all fixed before the test.
- [ ] **Step 3: `recruitment.md`** — who the new test recruits, channels (survey respondents via the live sheet, classmates, IE careers, LinkedIn), screening criteria, owner per channel, and a link to the v1 interviews as prior records.
- [ ] **Step 4: Verify** link checker exit 0; riskiest assumption verbatim in `assumptions.md` and `experiment-card.md`.
- [ ] **Step 5: Commit** — `git commit -am "Rewrite assumptions, experiment card and recruitment for v2"`

### Task 6: Personas swap

**Files:**
- Move: `evidence-log/personas/ai-persona-03.md` → `evidence-log/personas/drafts/persona-hypothesis-06.md` (Once-Bitten Owner)
- Move: `evidence-log/personas/drafts/persona-hypothesis-04.md` → `evidence-log/personas/ai-persona-03.md` (Skeptical Verifier)
- Modify: `ai-persona-01.md`, `ai-persona-02.md`, new `ai-persona-03.md`, `personas/README.md`

- [ ] **Step 1: Swap** with `git mv` through a temp name, then run the restructure link-rewrite logic (same as the one used on 2026-10-12) so every link follows the files.
- [ ] **Step 2: Add a "v2 note (2026-10-12)"** section to each selected persona: how this persona meets the challenge model, which v2 assumption it stresses, what is still unknown.
- [ ] **Step 3: Update README** file-layout table and selection reasoning.
- [ ] **Step 4: Verify** link checker exit 0.
- [ ] **Step 5: Commit** — `git commit -am "Select Skeptical Verifier as critical persona for v2"`

### Task 7: ERRC and value curve

**Files:**
- Modify: `evidence-log/ERRC.md`
- Create: `evidence-log/market-research/value-curve.md`, `evidence-log/market-research/value-curve.svg`

- [ ] **Step 1: `ERRC.md`** — keep Stage A/B, refresh baseline with Task 3 alternatives; Stage C grid: Eliminate paid client delivery and deposits; Reduce time per challenge and company briefing effort; Raise verifiability of individual contribution and feedback quality; Create a company-calibrated score usable as a take-home replacement. For each: cost effect, buyer-value effect, evidence link or Hypothesis tag. Value innovation hypothesis in falsifiable form; evidence status; critical validation points tied to the experiment card. Remove the NOT FINAL banner and replace it with an evidence-status note.
- [ ] **Step 2: Value curve** — 7 factors (time per challenge, realness of brief, individual-contribution proof, feedback depth, employer credibility of credential, cost to student, team support), scored 1–5 for SkillBridge v2, Forage, Devpost, Kaggle and coursework, each score with a one-line reason in `value-curve.md`. Inline SVG line chart with distinct marker shapes and direct labels.
- [ ] **Step 3: Verify** link checker exit 0; open the SVG with the Read tool and confirm it is legible.
- [ ] **Step 4: Commit** — `git commit -am "Complete ERRC and add value curve"`

### Task 8: Press release and market estimate note

**Files:** Create `evidence-log/press-release.md`; Modify `evidence-log/market-research/analysis.md`

- [ ] **Step 1: Press release** — headline with customer outcome; subhead; problem paragraph naming the current alternative; solution paragraph; illustrative student quote (labelled illustrative); evidence status box (what is evidence, what is hypothesis); "what would prove us wrong".
- [ ] **Step 2: `analysis.md`** — add a dated v2 note at the top: the student-pool estimate still applies; revenue is not recomputed for v2.
- [ ] **Step 3: Verify and commit** — link checker exit 0; `git commit -am "Add Working Backwards press release"`

### Task 9: Prototype v1

**Files:** Create `prototype/prototype-v1.html`, `prototype/prototype-v1.pdf`, `prototype/prototype-v1-backup.png`; Modify `prototype/README.md`

- [ ] **Step 1: Build** a self-contained page (no network requests), four steps matching v0's style: 01 Challenge brief (company, task, time box, rubric), 02 Team submission with per-member contribution records, 03 Score (AI rubric breakdown + company engineer sign-off + written feedback), 04 Certificate on student profile with stacked results. Clear "illustrative" banner. Print stylesheet shows all four steps.
- [ ] **Step 2: Export**

```bash
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; U="file://$PWD/prototype/prototype-v1.html"
"$C" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="$PWD/prototype/prototype-v1.pdf" "$U"
"$C" --headless=new --disable-gpu --hide-scrollbars --window-size=1280,1280 --screenshot="$PWD/prototype/prototype-v1-backup.png" "$U"
```

- [ ] **Step 3: Verify** — read the PDF and PNG with the Read tool; all four steps appear in the PDF; `grep -c "http" prototype/prototype-v1.html` shows no external resource loads.
- [ ] **Step 4: Update `prototype/README.md`** with v1 walkthrough and v0 kept as history; commit.

### Task 10: Log, consistency check, wrap-up

**Files:** Modify `evidence-log/ai-usage-log.md`

- [ ] **Step 1: Log** one 2026-10-12 row for the pivot (tools, asks, outputs, what the user decided).
- [ ] **Step 2: Consistency grep**

Run: `grep -n -i -E "deposit|small business|campaign|charter" evidence-log/*.md evidence-log/personas/*.md`
Expected: matches only inside explicit v1/history references.

- [ ] **Step 3: Links** — `python3 tools/check_links.py` → exit 0.
- [ ] **Step 4: Commit** and report to Lucas; ask before pushing and opening the PR.
