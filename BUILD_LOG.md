# Build Log

This document tracks the step-by-step construction of the `swe-journey` repository, batch by batch.

| Batch | Description | Commit Hash | Date | Status |
|---|---|---|---|---|
| Batch 0 | Repository initialization (`README.md`, `.gitignore`, `.env.example`, `BUILD_LOG.md`) | `2f4abd7` | 2026-11-15 | Complete |
| Batch 1 | Start-here section (`00-start-here/`, `CONTRIBUTING.md`, `LICENSE`) | `c4a5030` | 2026-11-15 | Complete |
| Batch 2 | Roadmap and timeline (`01-roadmap/`) | `59c80da` | 2026-11-15 | Complete |
| Batch 3 | Tools and setup guides (`02-tools/`) | `e8380a7` | 2026-11-15 | Complete |
| Batch 4 | Syllabus weeks 1–3 (`03-syllabus/week-01` to `week-03`) | `b723111` | 2026-11-15 | Complete |
| Batch 5 | Exams, rubrics, and project 1 starter (`05-exams/`, `06-projects/01-log-analyzer-cli/`, `instructor-keys/`) | `07ad514` | 2026-11-15 | Complete |
| Batch 6 | Syllabus weeks 4–5 and project 2 starter (`06-projects/02-static-api-page/`) | `42abf1e` | 2026-11-15 | Complete |
| Batch 7 | Syllabus weeks 6–8, project 3 starter, and phase 2 exam | Pending | 2026-11-15 | Complete |
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
- **Commit:** `e8380a7`
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

### Batch 4: Syllabus Weeks 1–3
- **Date:** 2026-11-15
- **Commit:** `b723111`
- **Files created:**
  - `03-syllabus/week-01/` (README, lessons, concepts, exercises, hints, quiz, gate, retro)
  - `03-syllabus/week-02/` (README, lessons, concepts, exercises, hints, quiz, gate, retro)
  - `03-syllabus/week-03/` (README, lessons, concepts, exercises, hints, quiz, gate, retro)
  - `instructor-keys/README.md`
  - `instructor-keys/quiz-01.md`, `quiz-02.md`, `quiz-03.md` (Gitignored)
- **Actions:**
  - Populated all 8 standard pedagogical files for Weeks 1 through 3.
  - Authored Silver (expected) and Gold (stretch) exercises with calibrated 30-minute 3-level hint progressions.
  - Included a dedicated "debug this" exercise with broken code in each week.
  - Formatted Gates and conceptual Quizzes with external answer keys safely separated.

### Batch 5: Exams, Rubrics, and First Project
- **Date:** 2026-11-15
- **Commit:** `07ad514`
- **Files created:**
  - `05-exams/phase-1-exam.md`
  - `05-exams/rubrics/phase-1-rubric.md`
  - `06-projects/01-log-analyzer-cli/README.md`
  - `06-projects/01-log-analyzer-cli/pyproject.toml`
  - `06-projects/01-log-analyzer-cli/data/sample.log`
  - `06-projects/01-log-analyzer-cli/src/log_analyzer/` (models, parser, analyzer, cli skeletons)
  - `06-projects/01-log-analyzer-cli/tests/` (test_parser, test_analyzer, test_cli with failing tests)
  - `instructor-keys/phase-1-exam-key.md` (Gitignored)
  - `instructor-keys/project-01-solution.md` (Gitignored)
- **Actions:**
  - Created Phase 1 3-part comprehensive exam (Part A conceptual, Part B practical, Part C defense).
  - Outlined grading rubric headings in `05-exams/rubrics/phase-1-rubric.md` with complete scoring guide in `instructor-keys/`.
  - Built Project 1 starter skeleton with failing pytest test suite for the learner to solve.

### Batch 6: Weeks 4–5 and Project 2 Starter
- **Date:** 2026-11-15
- **Commit:** `42abf1e`
- **Files created:**
  - `03-syllabus/week-04/` (README, lessons, concepts, exercises, hints, quiz, gate, retro)
  - `03-syllabus/week-05/` (README, lessons, concepts, exercises, hints, quiz, gate, retro)
  - `06-projects/02-static-api-page/` (Vite, TypeScript, React app, components, failing tests)
  - `instructor-keys/quiz-04.md`, `quiz-05.md` (Gitignored)
  - `instructor-keys/project-02-solution.md` (Gitignored)
- **Actions:**
  - Authored full Week 4 (Web Protocols, CORS, DOM, CSS Grid/Flexbox) and Week 5 (TypeScript, React, hooks) syllabi.
  - Built Project 2 GitHub Organization Explorer starter skeleton with strict TypeScript, components, and Vitest/React Testing Library test suite.

### Batch 7: Weeks 6–8, Project 3 Starter, and Phase 2 Exam
- **Date:** 2026-11-15
- **Files created:**
  - `03-syllabus/week-06/` (README, lessons, concepts, exercises, hints, quiz, gate, retro)
  - `03-syllabus/week-07/` (README, lessons, concepts, exercises, hints, quiz, gate, retro)
  - `03-syllabus/week-08/` (README, lessons, concepts, exercises, hints, quiz, gate, retro)
  - `05-exams/phase-2-exam.md`
  - `05-exams/rubrics/phase-2-rubric.md`
  - `06-projects/03-task-api/` (FastAPI, SQLAlchemy 2.0 async, Alembic, Pydantic v2, Pytest async test suite)
  - `instructor-keys/quiz-06.md`, `quiz-07.md`, `quiz-08.md` (Gitignored)
  - `instructor-keys/phase-2-exam-key.md` (Gitignored)
  - `instructor-keys/project-03-solution.md` (Gitignored)
- **Actions:**
  - Authored comprehensive syllabi for Week 6 (Relational Modeling, Indexing, ACID), Week 7 (FastAPI, asyncio, Pydantic v2, DI), and Week 8 (SQLAlchemy 2.0 async, Alembic migrations, JWT Auth).
  - Designed Phase 2 3-part comprehensive exam covering web architecture, relational systems, transaction locking, and Socratic technical defense.
  - Built Project 3 Task API starter skeleton with models, schemas, routers, Alembic async migration runner, and full async pytest suite enforcing tenant isolation and multi-tenant security.
