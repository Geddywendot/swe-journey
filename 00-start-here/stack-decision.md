# ADR-001: Technology Stack Selection

- **Status:** Accepted
- **Date:** 2026-11-15
- **Deciders:** Learner & Learning Partner

---

## Context and Problem Statement

The goal is to prepare a self-taught learner for a professional software engineering role within 20 weeks (4–6 months). The learner already has introductory familiarity with Python and Java syntax and basic Git, with interests in backend engineering, data systems/ML, and security. In past attempts, shifting between multiple languages and frameworks (tech stack churn) caused fragmentation and dropped momentum.

We need a cohesive, modern, industry-standard stack that:
1. Minimizes unnecessary context switching while providing fullstack depth.
2. Serves as a solid foundation for backend APIs, data engineering/machine learning, and application security.
3. Teaches modern software engineering paradigms (strict typing, asynchronous I/O, relational data modeling, component architecture, testing, and CI/CD).

---

## Decision Drivers

- **Market Demand:** High demand in enterprise and high-growth companies.
- **Modernity & Longevity:** Current standards (not legacy idioms from 10 years ago).
- **Type Safety & Rigor:** Static typing on both backend and frontend to catch defects early.
- **Path Cohesion:** Synergistic crossover into Machine Learning (scikit-learn) and Cybersecurity (OWASP, secure coding) without switching languages.

---

## Considered Options

1. **Python / FastAPI + React (TypeScript) + PostgreSQL** *(Selected)*
2. **Node.js / Express / MongoDB (MERN Stack)**
3. **Java / Spring Boot + Angular + PostgreSQL**
4. **Go / Gin + Svelte + PostgreSQL**

---

## Decision Outcome: Option 1 (Python / FastAPI + React + PostgreSQL)

Chosen because it provides the highest alignment with the learner's background, professional standards, and future specializations.

### Component Breakdown

### 1. Backend: Python 3.12+ with FastAPI & Pydantic v2
- **Why:** FastAPI is built on modern Python features: type annotations (`typing`), ASGI asynchronous handling (`async`/`await`), and runtime data validation (`pydantic`). It delivers near-Go/Node performance with superior developer ergonomics and automatic OpenAPI documentation.
- **Synergy:** Python is the undisputed industry standard for Machine Learning and Security automation, allowing direct leverage in weeks 18 and 19 without learning a secondary runtime.
- **Tooling:** Managed with `uv`, an extremely fast Python package and environment manager written in Rust, replacing slow legacy tooling (`pip`, `virtualenv`).

### 2. Database: PostgreSQL with SQLAlchemy 2.0 & Alembic
- **Why:** PostgreSQL is the gold standard of relational database systems, offering ACID compliance, robust indexing, JSONB flexibility, and enterprise reliability.
- **ORM & Migrations:** SQLAlchemy 2.0 enforces modern typed query constructs (`select()`, async sessions), while Alembic provides industrial-grade database schema migration tracking.

### 3. Frontend: React 18+ with TypeScript and Vite
- **Why:** React remains the dominant web UI library worldwide. Pairing React with strict TypeScript ensures end-to-end type safety from database schemas to UI components.
- **Build Tool:** Vite provides instant hot module reloading (HMR) and clean ESM-native builds.
- **Testing:** React Testing Library teaches user-centric behavior testing rather than fragile implementation testing.

### 4. Delivery & Operations: Docker, GitHub Actions, Render / Fly.io
- **Why:** Modern engineering mandates containerization and automation. Using Docker Compose for multi-container orchestration mirrors real-world staging and production environments.

### 5. Role of Alternative Stacks (MERN)
- Express and MongoDB are intentionally excluded from the primary path to prevent drift. They are examined exclusively in **Week 17** as a comparative architecture exercise (Document Store vs Relational, Node event loop vs Python ASGI).

---

## Consequences

### Positive
- One primary language (Python) powers backend, data/ML, and security tools.
- Strict typing across the stack (Pydantic models on backend, TypeScript interfaces on frontend).
- Complete production-grade portfolio projects showcasing clean architecture, test suites, and containerized deployments.

### Negative / Trade-offs
- Fullstack breadth requires context switching between Python (backend) and TypeScript (frontend). This is mitigated by introducing frontend only in Phase 2 (Week 4), after Python foundations are solid.
