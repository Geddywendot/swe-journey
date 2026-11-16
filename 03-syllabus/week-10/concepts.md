## Concepts

1. **Controlled Form Components** – In React, each form input's value is stored in component state and updated via `onChange`. This gives the app full control over user input, enables validation, and ensures the UI reflects the model.
   
   *Explain it back:* 

2. **Optimistic UI Updates** – Updating the UI before the server confirms the change improves perceived performance. If the request later fails, the UI must roll back and display an error.
   
   *Explain it back:* 

3. **Error Boundaries** – A React component that implements `componentDidCatch` (or the `ErrorBoundary` wrapper) can catch rendering errors in its subtree and render a fallback UI, preventing the whole app from crashing.
   
   *Explain it back:* 

4. **Loading State Patterns** – Showing a spinner, skeleton, or placeholder while data is being fetched keeps users informed. Choose a pattern that matches the amount of expected content and perceived latency.
   
   *Explain it back:* 

5. **Pydantic Validation in FastAPI** – Request bodies are declared as Pydantic models, automatically validating types, required fields, and constraints. Validation errors are returned as a structured JSON response that the front‑end can display.
   
   *Explain it back:*