# Major Milestones and Progress Checkpoints

Major milestones act as go/no-go gates. Progression to the subsequent phase requires passing each milestone evaluation by the learning partner.

---

## Milestone 1: The Systems & Python Foundation Checkpoint (End of Week 3)

- **Deliverables:**
  - Completed `06-projects/01-log-analyzer-cli/` with full documentation and CLI flags.
  - Pytest suite demonstrating >= 85% test coverage.
  - Completion of `05-exams/phase-1-exam.md` (minimum 70% overall, Part B passed independently).
- **Core Competencies Verified:**
  - Can explain Git internals (blobs, trees, commits, references) and recover detached HEAD states.
  - Can write idiomatic, type-hinted Python using generators, context managers, and custom exceptions.
  - Proficient in writing isolated unit tests with pytest fixtures and parameterization.
- **Decision:**
  - **PASS:** Proceed to Phase 2 (Frontend & Web Architecture).
  - **RETRY:** 3-day targeted remediation on generators or testing before re-attempting Phase 1 practical exam.

---

## Milestone 2: The Production Backend Checkpoint (End of Week 8)

- **Deliverables:**
  - Completed `06-projects/03-task-api/` with relational database models, Alembic migrations, and JWT bearer authentication.
  - Passing pytest suite utilizing test database instances and async HTTP client (`httpx`).
  - Completion of `05-exams/phase-2-exam.md`.
- **Core Competencies Verified:**
  - Understands relational database schema design, foreign keys, cascade rules, indexing strategies, and ACID transactions.
  - Capable of structuring modular FastAPI applications with dependency injection (`Depends`) and Pydantic validation.
  - Implements secure authentication: salted password hashing (bcrypt) and stateless JWT verification with expiration.
- **Decision:**
  - **PASS:** Proceed to Phase 4 (Fullstack Integration).
  - **RETRY:** Re-architect database session lifecycles or authentication middleware before advancing.

---

## Milestone 3: The Fullstack Integration Checkpoint (End of Week 11)

- **Deliverables:**
  - Completed `06-projects/04-taskboard-fullstack/` featuring responsive UI, state synchronization, error boundaries, and API integration.
  - End-to-end test suites covering both frontend components and backend endpoints.
  - Completion of `05-exams/phase-3-exam.md`.
- **Core Competencies Verified:**
  - Can construct strict TypeScript React components managing local state and remote server state (React Query).
  - Demonstrates handling of loading states, network failures, and optimistic user interface updates.
  - Can write user-centric integration tests using React Testing Library and mock API handlers.
- **Decision:**
  - **PASS:** Proceed to Phase 5 (DevOps, Docker, CI/CD).
  - **RETRY:** Remediate client-side state bugs or asynchronous test races.

---

## Milestone 4: The Cloud Delivery & DevOps Checkpoint (End of Week 15)

- **Deliverables:**
  - Fully containerized fullstack application with multi-stage Dockerfiles and Docker Compose configuration.
  - Operational GitHub Actions CI pipeline executing linting, formatting, and tests on PRs.
  - Live, production deployment on Render or Fly.io connected to a managed PostgreSQL instance.
  - Completion of `05-exams/phase-4-exam.md`.
- **Core Competencies Verified:**
  - Understands Docker image layering, build cache optimization, and container security (non-root execution).
  - Writes reusable CI workflow definitions with secrets management and automated verification.
  - Diagnoses production failures using structured logging, metrics, and healthcheck probes.
- **Decision:**
  - **PASS:** Proceed to Phase 6 (Distributed Systems, Specializations & Capstone).
  - **RETRY:** Resolve pipeline failures or environment variable leaks.

---

## Milestone 5: The Senior Engineering Defense & Capstone (End of Week 20)

- **Deliverables:**
  - Deployed production capstone project (`06-projects/07-capstone/`) demonstrating end-to-end fullstack depth.
  - Completed ML service (`06-projects/05-ml-model-service/`) and Security scanner (`06-projects/06-security-scanner/`).
  - Architecture Decision Records (ADRs) documenting system tradeoffs.
  - Completion of `05-exams/final-mock-exam.md`.
- **Core Competencies Verified:**
  - Demonstrates clear systems reasoning (horizontal vs vertical scaling, caching invalidation, CAP theorem).
  - Can defend every architectural decision, data model choice, and security safeguard without notes.
  - Produces clean, maintainable, tested, and documented code ready for professional engineering teams.
- **Outcome:** **Full Graduate Clearance for Software Engineering Roles.**
