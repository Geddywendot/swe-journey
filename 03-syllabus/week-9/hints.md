## Hints

**Silver 1**
- *Level 1*: The endpoint should return `[{"id":1,"name":"Item A"}, …]`.
- *Level 2*: Use `@app.get("/items")` and return a Python list; in React call `fetch(import.meta.env.VITE_API_URL + "/items")`.
- *Level 3*: Remember `fetch` returns a `Response` that you need to `await response.json()`.

**Silver 2**
- *Level 1*: Add `CORSMiddleware` with `allow_origins=["http://localhost:3000"]`.
- *Level 2*: Put the API URL in a `.env` file (`VITE_API_URL=http://localhost:8000`) and access it via `import.meta.env.VITE_API_URL`.
- *Level 3*: After changing the env file, restart the React dev server so the variable is picked up.

**Gold**
- *Level 1*: Install `python‑dotenv` and load `FASTAPI_SECRET` from `.env`.
- *Level 2*: Create an endpoint `/secret` that reads the env variable and returns it **only** when a mock auth header `X‑Mock‑User` is present.
- *Level 3*: In React, call `/secret` with `fetch(..., {headers:{"X‑Mock‑User":"student"}})` and handle 401/403 by showing “Access denied”.
