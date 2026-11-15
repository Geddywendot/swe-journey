# Contributing & Engineering Workflow

Welcome to the `swe-journey` repository. This repository functions as a private classroom for the learner and learning partner. All contributions must adhere to the engineering standards outlined below.

---

## 1. Branch Strategy

Direct commits to the `main` branch are prohibited for weekly work. All work must follow a strict feature-branch workflow:

1. Create a dedicated branch from `main`:
   ```bash
   git checkout -b week-NN/<topic-or-gate>
   # Example: git checkout -b week-01/unix-git-basics
   ```
2. Commit frequently in small, logical chunks using conventional commit messages:
   - `feat:` for new capabilities or implementations
   - `fix:` for debugging and bug resolution
   - `test:` for adding or updating unit/integration tests
   - `docs:` for updating journals, reflections, or documentation
   - `refactor:` for code cleanups without behavior changes
3. Push your branch to GitHub:
   ```bash
   git push -u origin week-NN/<topic-or-gate>
   ```

---

## 2. Pull Requests and Review

At the end of each week (Day 5), open a Pull Request into `main`:

1. Fill out `.github/PULL_REQUEST_TEMPLATE.md` completely.
2. Confirm that all automated checks, linter runs, and pytest tests pass.
3. Request review from your learning partner.
4. Address all review comments with follow-up commits.
5. Once approved, perform a clean squash-and-merge or merge commit into `main`.

---

## 3. Confidentiality of Instructor Keys

- The `instructor-keys/` folder contains solution keys, full grading rubrics, and quiz answers.
- `instructor-keys/` is listed in `.gitignore` and must **never** be committed or exposed in public PRs or issues.
- The learning partner maintains these keys independently.

---

## 4. Code Standards & Hygiene

- **No Secrets:** Never commit `.env` files, API keys, passwords, or production credentials.
- **No AI-Generated Dumps:** You must understand and be capable of explaining every line of code you commit.
- **Test-Driven Discipline:** Every new feature or bugfix should include corresponding automated tests.
