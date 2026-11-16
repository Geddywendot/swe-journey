## Reflection on Week 10 – Data Fetching & Forms

- **What was hard?** Managing asynchronous state for loading, error, and success simultaneously while keeping the UI responsive was tricky. Implementing reusable validation logic without leaking state was also a challenge.
- **What can I do now?** I can structure fetch logic with a custom hook that returns `data`, `loading`, and `error`, and I can build validation hooks that return error objects and a `validate` function.
- **What will I change?** I will start with a minimal form and add validation incrementally, and I will write unit tests for the validation hook early to catch regressions.
