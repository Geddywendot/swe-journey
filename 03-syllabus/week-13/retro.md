## Retro

- **What was hard?**
  - Understanding how to correctly configure healthchecks for both the API and the database, and ensuring the compose network allowed the frontend to reach the API without CORS issues.

- **What can I do now?**
  - Build and push production‑ready Docker images, orchestrate multi‑service stacks with docker‑compose, and reliably test end‑to‑end connectivity.

- **What will I change?**
  - Add explicit `docker compose down --volumes` steps in CI to guarantee a clean state, and document the exact order of environment variable propagation.
