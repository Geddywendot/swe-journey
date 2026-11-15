# Phase 1 Evaluation Rubric Headings

This document outlines the evaluation dimensions and criteria categories for `05-exams/phase-1-exam.md`. Full scoring thresholds and solution answers are maintained by the learning partner in `instructor-keys/phase-1-exam-key.md`.

---

## 1. Part A: Conceptual Depth (30 Points Total)

### Evaluation Headings
- **1.1 Git Content-Addressable Storage & Tree Integrity** (5 pts)
- **1.2 Unix Process File Descriptors & Stream Redirection** (5 pts)
- **1.3 Python Iterator Protocol & Memory Complexity** (5 pts)
- **1.4 Context Manager Exception Suppression Semantics** (5 pts)
- **1.5 Static Typing & Structural Protocols vs ABCs** (5 pts)
- **1.6 Test Isolation, State Leakage & Fixture Scopes** (5 pts)

---

## 2. Part B: Practical Engineering Task (50 Points Total)

### Evaluation Headings
- **2.1 CLI Interface & POSIX Exit Code Compliance** (10 pts)
  - Argument parsing (`argparse`), help menus, exit codes (0, 1, 2), stream separation (`stdout`/`stderr`).
- **2.2 Streaming Architecture & Data Model Integrity** (10 pts)
  - Lazy generator evaluation, immutable typed dataclasses, resilient error recovery on corrupt lines.
- **2.3 Statistical Aggregation Correctness** (10 pts)
  - Accurate status counts, percentiles (p95), top-k ranking.
- **2.4 Output Formatting & Formatting Flags** (10 pts)
  - Valid JSON schema emission, tabular plain-text layout.
- **2.5 Automated Test Suite & Coverage** (10 pts)
  - Pytest fixtures, test parameterization, edge case scenarios, assertion depth.

---

## 3. Part C: Architecture Defense & Interview (20 Points Total)

### Evaluation Headings
- **3.1 High-Volume Scale Bottleneck Articulation** (10 pts)
  - Explaining memory boundaries, streaming vs buffered percentiles, external sorting or approximation algorithms (e.g. t-digest or reservoir sampling).
- **3.2 Git Conflict & Branch Workflow Resolution** (10 pts)
  - Clear, precise explanation of rebase onto main, conflict resolution markers, and tree validation.
