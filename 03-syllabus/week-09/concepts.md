- **Concept 1 – CORS Basics**: Cross‑Origin Resource Sharing is a browser security mechanism that blocks requests from origins that differ from the server’s origin unless explicitly allowed via response headers. It protects users from malicious sites reading privileged data.
  **Explain it back**: What does the browser check before allowing a cross‑origin request?

- **Concept 2 – FastAPI Middleware**: Middleware functions wrap each request/response cycle, letting you add headers, handle authentication, or modify responses globally. `CORSMiddleware` is a built‑in FastAPI middleware that sets the necessary CORS headers.
  **Explain it back**: How does adding `CORSMiddleware` affect every request?

- **Concept 3 – React Environment Variables**: In a Vite or CRA project, variables prefixed with `VITE_` (or `REACT_APP_`) are injected at build time and accessed via `import.meta.env` (or `process.env`). This keeps secrets out of source code.
  **Explain it back**: Why must env vars be prefixed and how are they accessed?

- **Concept 4 – API Contract**: Defining a clear request and response schema (e.g., using Pydantic models) ensures the front‑end knows the shape of data it will receive, reducing runtime errors.
  **Explain it back**: What advantage does a Pydantic response model give the React client?

- **Concept 5 – Error Boundaries**: React error boundaries catch JavaScript errors in component trees, preventing the entire UI from crashing and allowing graceful fallback UI.
  **Explain it back**: What happens if an uncaught error occurs without a boundary?
