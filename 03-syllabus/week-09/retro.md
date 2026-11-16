## Reflection on Week 9 – React ↔ FastAPI Integration

- **What was hard?** I struggled with configuring CORS correctly on the FastAPI side and ensuring the React front‑end respected the environment variable prefixes. Debugging the 401 responses and tracing missing headers took extra time.
- **What can I do now?** I can set up `CORSMiddleware` with specific origins, manage secrets using `.env` files in both projects, and use `process.env` (or `import.meta.env`) safely in React components.
- **What will I change?** I will start with a minimal CORS configuration and add origins incrementally, and I will verify that env variables are loaded before writing any fetch logic.
