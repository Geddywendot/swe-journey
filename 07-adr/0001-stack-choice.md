# ADR-001: Stack Choice

**Title:** Technology Stack Selection

**Status:** Accepted

**Date:** 2026-11-16

---

## Context and Problem Statement

The learner needs a cohesive, modern stack for the 20‑week self‑guided software engineering journey, avoiding churn and ensuring depth across backend, frontend, data, and deployment.

## Decision

We will use **Python with FastAPI** for the backend, **React with TypeScript** for the frontend, **PostgreSQL** for the database, **Docker** for packaging, and **GitHub Actions** for CI. This mirrors the decision documented in `00-start-here/stack-decision.md`.

## Alternatives considered

- **MERN Stack (Node.js/Express/MongoDB/React)** – examined as a comparative exercise in week 17; not chosen as the primary stack.
- Java/Spring, Go/Gin, etc., were also evaluated but rejected due to language mismatch with the learner’s background.

## Consequences

- **Positive:** Unified language (Python) for backend, data, and security tooling; strong ecosystem for ML and security labs; end‑to‑end type safety with TypeScript on the frontend.
- **Negative:** Learner must handle both Python and TypeScript contexts, introducing some context‑switching.

---

*Write an ADR whenever a significant architectural, tooling, or process choice is made that will affect future development or maintenance.*