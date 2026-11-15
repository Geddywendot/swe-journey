# Build Log

This document tracks the step-by-step construction of the `swe-journey` repository, batch by batch.

| Batch | Description | Commit Hash | Date | Status |
|---|---|---|---|---|
| Batch 0 | Repository initialization (`README.md`, `.gitignore`, `.env.example`, `BUILD_LOG.md`) | `2f4abd7` | 2026-11-15 | Complete |
| Batch 1 | Start-here section (`00-start-here/`, `CONTRIBUTING.md`, `LICENSE`) | `c4a5030` | 2026-11-15 | Complete |
| Batch 2 | Roadmap and timeline (`01-roadmap/`) | `59c80da` | 2026-11-15 | Complete |
| Batch 3 | Tools and setup guides (`02-tools/`) | Pending | 2026-11-15 | In Progress |
| Batch 4 | Syllabus weeks 1–3 (`03-syllabus/week-01` to `week-03`) | Pending | 2026-11-15 | Planned |
| Batch 5 | Exams, rubrics, and project 1 starter (`05-exams/`, `06-projects/01-log-analyzer-cli/`, `instructor-keys/`) | Pending | 2026-11-15 | Planned |
| Batch 6 | Syllabus weeks 4–5 and project 2 starter (`06-projects/02-static-api-page/`) | Pending | 2026-11-15 | Planned |
| Batch 7 | Syllabus weeks 6–8, project 3 starter, and phase 2 exam | Pending | 2026-11-15 | Planned |
| Batch 8 | Syllabus weeks 9–11, project 4 starter, and phase 3 exam | Pending | 2026-11-15 | Planned |
| Batch 9 | Syllabus weeks 12–15, CI/CD starter, Docker guide, and phase 4 exam | Pending | 2026-11-15 | Planned |
| Batch 10 | Syllabus weeks 16–17, system design practice, and practice katas (`09-tests-and-practice/`) | Pending | 2026-11-15 | Planned |
| Batch 11 | Specialization tracks (weeks 18–20), projects 05–07 starters, phase 5 exam, and final mock exam | Pending | 2026-11-15 | Planned |
| Batch 12 | Reference library (`04-references/`) and glossary updates | Pending | 2026-11-15 | Planned |
| Batch 13 | Final consistency pass, checks, and release tag `v1.0.0` | Pending | 2026-11-15 | Planned |

---

## Batch Details

### Batch 0: Repository and GitHub
- **Date:** 2026-11-15
- **Commit:** `2f4abd7`
- **Files created:**
  - `README.md`
  - `.gitignore`
  - `.env.example`
  - `BUILD_LOG.md`
- **Actions:**
  - Initialized git repository on branch `main`.
  - Configured git ignore for instructor keys, secrets, build artifacts, and virtual environments.
  - Published public repository to GitHub: `https://github.com/Geddywendot/swe-journey`.

### Batch 1: Start-Here Section
- **Date:** 2026-11-15
- **Commit:** `c4a5030`
- **Files created:**
  - `00-start-here/plan-at-a-glance.md`
  - `00-start-here/how-to-study.md`
  - `00-start-here/stack-decision.md`
  - `00-start-here/learning-partner.md`
  - `00-start-here/glossary.md`
  - `CONTRIBUTING.md`
  - `LICENSE`
  - `.github/PULL_REQUEST_TEMPLATE.md`
- **Actions:**
  - Formulated full 20-week plan at a glance.
  - Documented daily rhythm, 30-minute struggle rule, and 3-level hint policy.
  - Authored ADR-001 explaining rationale for Python/FastAPI/Postgres/React stack.
  - Defined learning partner roles, meeting agendas, and evaluation criteria.
  - Established initial living engineering glossary.

### Batch 2: Roadmap and Timeline
- **Date:** 2026-11-15
- **Commit:** `59c80da`
- **Files created:**
  - `01-roadmap/phases.md`
  - `01-roadmap/milestones.md`
  - `01-roadmap/timeline.md`
- **Actions:**
  - Outlined the 6 engineering phases from fundamentals through capstone.
  - Established go/no-go milestone checkpoints at weeks 3, 8, 11, 15, and 20.
  - Created customizable 20-week timeline initialized with `YYYY-MM-DD` start date placeholder.

### Batch 3: Tools and Setup Guides
- **Date:** 2026-11-15
- **Files created:**
  - `02-tools/setup-windows.md`
  - `02-tools/setup-macos.md`
  - `02-tools/setup-linux.md`
  - `02-tools/git-cheatsheet.md`
  - `02-tools/terminal-basics.md`
  - `02-tools/uv-and-python.md`
  - `02-tools/docker-cheatsheet.md`
  - `02-tools/vscode-setup.md`
- **Actions:**
  - Authored setup guides for Windows (WSL2 & native), macOS (Homebrew), and Linux (Debian/Ubuntu/Fedora).
  - Covered installation and configuration of `uv`, Python 3.12, Node.js LTS, Git, Docker, and VS Code.
  - Documented commands and mental models for Git DAGs, Unix standard streams, and container lifecycles.
