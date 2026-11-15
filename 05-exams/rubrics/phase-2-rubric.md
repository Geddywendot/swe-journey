# Phase 2 Evaluation Rubric Headings

This document outlines the evaluation dimensions and criteria categories for `05-exams/phase-2-exam.md`. Full scoring thresholds and solution answers are maintained by the learning partner in `instructor-keys/phase-2-exam-key.md`.

---

## 1. Part A: Conceptual Depth (30 Points Total)

### Evaluation Headings
- **1.1 HTTP Protocols & Application-Layer Multiplexing** (5 pts)
- **1.2 React Reconciliation, Virtual DOM & Key Reconciliation** (5 pts)
- **1.3 Relational Normalization (3NF) & Analytical Denormalization** (5 pts)
- **1.4 B-Tree Execution Plans & Planner Cost Heuristics** (5 pts)
- **1.5 Async Event Loop Starvation & Concurrency Boundaries** (5 pts)
- **1.6 Stateless JWT Cryptography & Revocation Patterns** (5 pts)

---

## 2. Part B: Practical Engineering Task (50 Points Total)

### Evaluation Headings
- **2.1 Schema Definition & Integrity Constraints** (10 pts)
  - `CHECK (balance_cents >= 0)` constraint, foreign keys, non-null guarantees.
- **2.2 Atomic Transaction Boundaries & Rollback** (10 pts)
  - Single atomic transaction, explicit rollback on error, no partial writes.
- **2.3 Concurrency Control & Double-Spend Prevention** (10 pts)
  - `SELECT ... FOR UPDATE` or atomic decrement queries, deterministic lock ordering to prevent deadlocks.
- **2.4 Authentication & Tenant Boundary Enforcement** (10 pts)
  - JWT Bearer validation, ownership check between token and source account.
- **2.5 Automated Async Test Suite & Isolation** (10 pts)
  - Pytest async client, clean test database fixtures, boundary assertions.

---

## 3. Part C: Architecture Defense & Interview (20 Points Total)

### Evaluation Headings
- **3.1 High-Contention Ledger Scaling & Hot-Spotting** (10 pts)
  - Explaining row lock contention, distributed ledger strategies (e.g. append-only transaction logs, batching, distributed sharding).
- **3.2 Dual-Write Hazards & Transactional Outbox Pattern** (10 pts)
  - Explaining the distributed 2PC problem, partial network failures, and how the outbox pattern guarantees at-least-once message delivery.
