# Phase 1 Comprehensive Exam: Systems & Python Foundations

- **Scope:** Weeks 01–03 (Unix, Git internals, modern Python data model, typing, pytest, CLI design)
- **Time Allocated:** 3 Hours (180 minutes)
- **Passing Threshold:** 70% overall, and **Part B must be passed on its own**.
- **Rules:** No AI assistance. Official Python and Git documentation permitted. Answer keys are retained by your learning partner.

---

## Part A: Conceptual Depth (30% - 45 Minutes)

Answer each question in 3 to 5 clear sentences.

1. **Git Content Addressability:** How does Git use cryptographic hashing (SHA-1/SHA-256) to ensure data integrity, and what allows Git to detect duplicate files across different directories without inspecting timestamps?
2. **Standard Stream Separation:** Why do production CLI tools write machine-readable output to `stdout` and human-readable diagnostics to `stderr`? What failure occurs in a Unix pipeline if this convention is violated?
3. **Generators vs. Collections:** Explain how Python's iterator protocol (`__iter__` and `__next__`) operates at the bytecode level, and why a generator expression requires $O(1)$ auxiliary memory compared to a list comprehension's $O(N)$.
4. **Context Manager Guarantees:** Describe the sequence of method calls when an exception occurs inside a `with` block. What dictates whether the exception propagates upward or is silenced?
5. **Structural Subtyping:** How does `typing.Protocol` differ from inheritance under `abc.ABCMeta`? What architectural advantages does structural typing provide in decoupled systems?
6. **Test Isolation:** Explain why mutable test fixtures or global module variables cause flaky test suites. What mechanisms does `pytest` provide to ensure fresh test boundaries?

---

## Part B: Practical Timed Engineering Task (50% - 90 Minutes)

> **Scenario:** A production microservice emits semi-structured access log records. You are tasked with implementing a standalone Python CLI tool that parses these records, computes aggregate latency statistics, identifies abnormal traffic spikes, and outputs a structured summary report.

### Requirements:
1. **Input:** Accept a log file path or stream from standard input (`sys.stdin`).
2. **Parsing & Data Model:**
   - Parse each record into an immutable `@dataclass(frozen=True)` instance.
   - Ignore corrupt lines without aborting the process; log warnings to `sys.stderr`.
3. **Analysis:**
   - Compute total requests, total successful responses (2xx), client errors (4xx), and server errors (5xx).
   - Calculate median and 95th percentile response times (latency) using exact arithmetic or Python's `statistics` module.
   - Identify the top 3 most requested URI endpoints.
4. **Output:**
   - Output valid formatted JSON to `stdout` when `--format json` is passed.
   - Output human-readable plain text to `stdout` by default.
5. **Exit Codes:**
   - Return `0` on success.
   - Return `1` on unhandled runtime or calculation error.
   - Return `2` on invalid command line arguments.
6. **Tests:**
   - Write a complete pytest suite verifying the CLI, handling of corrupted input, and calculation accuracy.

---

## Part C: Technical Defense & Socratic Interview (20% - 30 Minutes)

During the partner sync, walk through your implementation. You will defend your code and answer these two live questions:

1. *"Suppose your log file grows to 50 gigabytes on a server with only 4 gigabytes of RAM. Which parts of your implementation would succeed, which would exhaust memory, and how would you redesign the bottlenecks?"*
2. *"If two team members branch off `main` and refactor the parser module while modifying the CLI interface simultaneously, what steps would you take in Git to rebase and resolve the merge cleanly?"*
