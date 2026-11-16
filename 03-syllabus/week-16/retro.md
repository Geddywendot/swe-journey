## Retro

- **What was hard?**
  - Coordinating Redis cache and RQ workers in Docker Compose, and ensuring the rate‑limit middleware correctly shared state across multiple instances.

- **What can I do now?**
  - Deploy cached endpoints and background job processing to production, and monitor rate‑limit metrics for abuse detection.

- **What will I change?**
  - Add explicit health‑checks for the Redis service and configure a shared cache namespace to avoid key collisions across environments.
