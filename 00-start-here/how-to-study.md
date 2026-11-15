# How to Study

This repository is designed for deliberate, self-guided mastery. It prioritizes depth, retention, and production-grade coding discipline over passive consumption.

---

## 1. The Daily Rhythm

You have allocated approximately **4 hours per day**, with **5 study days** and **1 lighter review day** each week:

```
┌────────────────────────────────────────────────────────────────────────┐
│ Days 1–2: Theory & Deep Understanding (~8 hours)                       │
│ • Study assigned lessons (official docs, books, articles).             │
│ • Review concepts in concepts.md; write out your own plain-word notes. │
│ • Complete the weekly quiz.                                            │
├────────────────────────────────────────────────────────────────────────┤
│ Days 3–4: Hands-on Implementation (~8 hours)                           │
│ • Solve the Silver exercises in exercises.md.                          │
│ • Attempt the optional Gold stretch task (if time permits).            │
│ • Commit working code to your topic branch incrementally.              │
├────────────────────────────────────────────────────────────────────────┤
│ Day 5: Weekly Gate & Retrospective (~4 hours)                          │
│ • Complete the practical gate.md without consulting solutions.         │
│ • Meet with your learning partner for the weekly session (45–60 min).  │
│ • Open a Pull Request from `week-NN/gate` to `main`.                   │
│ • Write your weekly journal entry in `08-journal/`.                    │
├────────────────────────────────────────────────────────────────────────┤
│ Day 6 (Lighter Day): Review & Consolidation (~2 hours)                 │
│ • Review the `glossary.md` and clarify fuzzy terms.                    │
│ • Read reference materials or catch up on documentation.               │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. The 30-Minute Struggle Rule

Real software engineering ability is built in the gap between confusion and resolution.

1. **When stuck:** Do not immediately search for the answer or ask an AI assistant.
2. **Set a timer for 30 minutes:**
   - Read the error trace from top to bottom.
   - Use `print()` or a debugger to inspect variables at the point of failure.
   - Search the official documentation or language specification.
   - Formulate a testable hypothesis: *"If I change X, then Y should happen because..."*
3. **If 30 minutes elapse without progress:**
   - Open **Hint Level 1** in `hints.md`.
   - Work for another 15 minutes.
   - Only escalate to **Hint Level 2** and **Hint Level 3** if still blocked.

---

## 3. The Hint System

Every exercise in `03-syllabus/` provides 3 progressive hint tiers:

- **Level 1 (Nudge):** Points to the specific file, function, or concept causing the issue.
- **Level 2 (Concept Name):** Explicitly names the algorithm, pattern, or standard library feature required.
- **Level 3 (Direction):** Provides architectural direction or pseudocode steps. **Never contains copy-paste solution code.**

*Note: Gold stretch tasks never include hints. They are designed to test independent problem solving.*

---

## 4. The Minimal AI Policy

To become an employable engineer, your brain must build the neural models for syntax, design patterns, and debugging.

- **AI Assistance is OFF during exercises and gates.** Do not use Copilot, ChatGPT, Claude, or any LLM to write code for you.
- **What is permitted:**
  - Using IDE autocomplete for standard library signatures.
  - Consulting official documentation (MDN, Python Docs, FastAPI docs).
  - Asking AI to explain a theoretical concept or error message *conceptually* (e.g., "Explain what a circular import is in Python without writing code for my project").
- **Rule of Thumb:** If you cannot explain every single line in your commit to your learning partner without notes, you did not write it.

---

## 5. Branching & PR Discipline

- Never commit directly to `main`.
- Create a feature branch for each week: `git checkout -b week-NN/topic`.
- Keep commits small, atomic, and descriptive (`git commit -m "feat: implement token parser"`).
- At the end of the week, open a Pull Request into `main` using `.github/PULL_REQUEST_TEMPLATE.md`.
- Your learning partner reviews the PR before merge.
