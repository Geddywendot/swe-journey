# The Six Phases of Engineering Mastery

The 20-week curriculum is partitioned into six distinct architectural phases. Each phase builds upon the previous, transforming raw syntax familiarity into production-ready software engineering capability.

---

## Phase 1: Engineering Foundations & Python Systems (Weeks 1–3)
- **Primary Goal:** Transition from syntax memorization to engineering discipline. Master the Unix toolchain, Git internals, object-oriented/functional Python, type annotations, and automated test-driven development with pytest.
- **Key Technologies:** Linux shell, Git, Python 3.12+, `pytest`, `uv`.
- **Core Artifact:** `06-projects/01-log-analyzer-cli/`
- **Phase Gate:**
  - Build a CLI tool processing gigabyte-scale server log files with streaming streams, regex parsing, and formatted summary reports.
  - 100% passing pytest suite with >= 85% branch coverage.
  - Complete `05-exams/phase-1-exam.md`.

---

## Phase 2: Web Architecture & Modern Frontend (Weeks 4–5)
- **Primary Goal:** Master the HTTP protocol, browser runtime mechanics, DOM rendering, and client-side component architecture using strict TypeScript and React.
- **Key Technologies:** HTTP/1.1 vs HTTP/2, TypeScript, React 18+, Vite, CSS Grid/Flexbox.
- **Core Artifact:** `06-projects/02-static-api-page/`
- **Phase Gate:**
  - Build a responsive, accessible React single-page application consuming public REST APIs with client-side caching, filtering, and error handling.
  - Zero TypeScript `any` types allowed.

---

## Phase 3: High-Performance Backend & Relational Data (Weeks 6–8)
- **Primary Goal:** Design normalized relational databases and engineer high-throughput asynchronous REST APIs with strict input validation, database migrations, and secure token-based authentication.
- **Key Technologies:** PostgreSQL, FastAPI, Pydantic v2, SQLAlchemy 2.0 (async), Alembic, PyJWT, passlib/bcrypt.
- **Core Artifact:** `06-projects/03-task-api/`
- **Phase Gate:**
  - Fully tested RESTful Task Management API with user registration, password hashing, JWT bearer auth, Alembic migration history, and relational CRUD.
  - Complete `05-exams/phase-2-exam.md`.

---

## Phase 4: Fullstack Architecture & The Testing Pyramid (Weeks 9–11)
- **Primary Goal:** Integrate frontend and backend into a cohesive fullstack system. Implement server-state synchronization (React Query), optimistic UI updates, integration testing, and contract verification.
- **Key Technologies:** TanStack React Query, Axios, React Testing Library, pytest async fixtures, testcontainers / in-memory PostgreSQL.
- **Core Artifact:** `06-projects/04-taskboard-fullstack/`
- **Phase Gate:**
  - End-to-end operational Kanban taskboard with real-time feedback, optimistic updates, drag-and-drop state transitions, and integration tests across both frontend and backend.
  - Complete `05-exams/phase-3-exam.md`.

---

## Phase 5: Containerization, CI/CD & Cloud Delivery (Weeks 12–15)
- **Primary Goal:** Package applications for reproducible environments, orchestrate multi-container systems, automate validation with GitHub Actions, and deploy to managed cloud platforms with monitoring.
- **Key Technologies:** Docker (multi-stage builds), Docker Compose, GitHub Actions, Fly.io / Render, structured JSON logging, health checks.
- **Phase Gate:**
  - Automated CI pipeline running linters (ruff, eslint) and test suites on every pull request.
  - Zero-downtime automated deployment to production cloud host with managed Postgres database.
  - Complete `05-exams/phase-4-exam.md`.

---

## Phase 6: Distributed Systems, Specializations & Capstone (Weeks 16–20)
- **Primary Goal:** Understand distributed system design trade-offs (caching, queues, eventual consistency), explore machine learning service deployment and application security, and deliver an original capstone project.
- **Key Technologies:** Redis, Background Workers, scikit-learn, OWASP Top 10, Bandit, pip-audit.
- **Core Artifacts:**
  - `06-projects/05-ml-model-service/` (Week 18)
  - `06-projects/06-security-scanner/` (Week 19)
  - `06-projects/07-capstone/` (Week 20)
- **Phase Gate:**
  - Complete `05-exams/phase-5-exam.md`.
  - Capstone architectural defense and live demo before the learning partner.
  - Complete `05-exams/final-mock-exam.md`.
