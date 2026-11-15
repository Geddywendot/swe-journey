# Learning Partner Guide

A structured guide for the weekly sync between the learner and the learning partner.

---

## 1. Roles & Responsibilities

### The Learner
- Complete lessons, exercises, and the practical gate prior to the weekly meeting.
- Push clean, atomic commits to a branch (`week-NN/gate`) and open a Pull Request.
- Present code and explain architecture without reading directly from notes.
- Own your progress: write honestly in `08-journal/` about blockers and triumphs.

### The Learning Partner
- Act as an engineering lead, code reviewer, and accountability anchor.
- Retain exclusive access to `instructor-keys/` (do not share the files directly with the learner).
- Guide using Socratic questions rather than providing direct answers:
  - *"What does the stack trace tell you happened right before the crash?"*
  - *"How does this function behave if the input list is empty?"*
  - *"Why did you choose a dictionary lookup here instead of a list search?"*
- Enforce the 70% passing threshold on practical gates and phase exams.

---

## 2. Weekly Partner Session Agenda (45–60 Minutes)

Every week concludes on Day 5 with a structured sync:

```
┌──────────────────────────────────────────────────────────────┐
│ Part 1: Concept Explain-Back (15 minutes)                    │
│ • Partner selects 2 random concepts from concepts.md.        │
│ • Learner explains them in plain English with analogies.     │
│ • Partner probes edge cases: "What happens when X fails?"    │
├──────────────────────────────────────────────────────────────┤
│ Part 2: Gate Demonstration & Verification (20 minutes)       │
│ • Learner runs test suites live in terminal.                 │
│ • Demonstrates the working artifact (CLI, API, UI).          │
│ • Partner inspects edge case handling.                       │
├──────────────────────────────────────────────────────────────┤
│ Part 3: PR Code Review (15–20 minutes)                       │
│ • Partner inspects the Pull Request diff on GitHub.          │
│ • Check acceptance criteria: no commented-out code,         │
│   meaningful commit messages, no hardcoded secrets.          │
│ • Partner approves PR or requests specific revisions.       │
│ • Learner records takeaways in retro.md.                     │
└──────────────────────────────────────────────────────────────┘
```

---

## 3. How to Conduct a Constructive Code Review

When reviewing the learner's weekly PR:

1. **Focus on Readability and Intent:**
   - Are variable and function names self-describing?
   - Does each function do exactly one thing?
   - Are edge cases (null values, network errors, empty inputs) handled gracefully?

2. **Verify Test Discipline:**
   - Are tests actually asserting behavior, or just executing code without meaningful assertions?
   - Do tests fail when the implementation is intentionally broken?

3. **Check for Security & Hygiene:**
   - Are there any `.env` files or API keys accidentally committed?
   - Are queries parameterized to prevent SQL injection?
   - Is all debug code (`console.log`, `print()`) removed or converted to proper logging?

---

## 4. Partner Evaluation Rubric Headings

When reviewing phase exams and major gates, score across four standard engineering dimensions:
1. **Correctness & Functionality:** Does it satisfy 100% of the acceptance criteria?
2. **Code Quality & Architecture:** Clean modular design, separation of concerns, idiomatic conventions.
3. **Testing & Robustness:** Meaningful unit/integration tests covering positive and negative paths.
4. **Defense & Articulation:** Can the learner explain the tradeoffs, time complexity, and failure modes?
