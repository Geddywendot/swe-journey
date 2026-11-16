## Concepts

1. **CORS (Cross‑Origin Resource Sharing)** – A browser security feature that restricts web pages from making requests to a different origin unless the server explicitly allows it via response headers. In FastAPI you enable it with `CORSMiddleware` to let your React app talk to the API.
   
   *Explain it back:*

2. **Environment Configuration** – Keeping secrets and settings (like API URLs, DB credentials) outside source code, typically in `.env` files or CI variables, and loading them at runtime. Both React (via `process.env`) and FastAPI (via `python‑dotenv`) rely on this pattern.
   
   *Explain it back:*

3. **HTTP Status Codes for API Errors** – Standard codes (`200`, `400`, `401`, `403`, `404`, `500`) that convey the result of a request. Your front‑end should interpret these to show appropriate UI feedback.
   
   *Explain it back:*

4. **Fetch API Error Handling** – The `fetch` promise resolves for network‑level success; you must manually check `response.ok` and handle JSON parsing errors to surface loading and error states.
   
   *Explain it back:*

5. **Docker Compose Service Networking** – Containers in the same `docker‑compose.yml` share a virtual network and can reach each other via service names, eliminating CORS issues in local development.
   
   *Explain it back:*