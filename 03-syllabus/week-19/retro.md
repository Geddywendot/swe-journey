## Retro

- **What was hard?**
  - Understanding the nuances of secure token rotation and ensuring revocation was complex, and configuring Redis for rate limiting added extra setup steps.
- **What can I do now?**
  - Apply the same token‑rotation pattern to other services, enable comprehensive logging for auth events, and reuse the rate‑limiting middleware for other endpoints.
- **What will I change?**
  - Allocate more time for secrets management research early on, and write unit tests for the revocation logic before implementing the feature.
