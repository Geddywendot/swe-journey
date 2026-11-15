# Gate 02: Python Data Model & Typed Streams

Pass requires all silver items. Gold items are bonus.

- [ ] **Build:** A typed streaming log parser module `log_stream.py` that processes simulated web server logs, validates data models using immutable `@dataclass(frozen=True)`, and yields structured records.
- [ ] **Test:** Write unit tests in `test_log_stream.py` asserting that malformed rows do not crash the generator, memory usage remains flat when processing a large mock file (100,000 lines), and static types pass `mypy --strict`.
- [ ] **Explain:** Learner explains the lifecycle of a generator and the mechanics of Python context managers to the learning partner without notes.
- [ ] **Commit:** Work pushed to branch `week-02/gate`, with a Pull Request opened into `main` using `.github/PULL_REQUEST_TEMPLATE.md` and approved by the partner.

**Result:** pass | retry  
**Learner note:** *(Document what was hardest to grasp or debug this week)*
