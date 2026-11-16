# Week 19 – Auth Hardening & API Security for FastAPI

**Goal:** Harden the task API (from weeks 7‑8) so it resists the most common API attacks and demonstrate that the API is secure.

**4‑hour‑per‑day plan**
1. **Day 1 (1 h):** Review OWASP API Security Top 10 and identify which attacks apply to the current API.
2. **Day 1 (1 h):** Implement access‑token / refresh‑token flow with rotation and a logout endpoint that revokes refresh tokens.
3. **Day 2 (1 h):** Add rate‑limiting to the login endpoint and write a test that verifies the limit.
4. **Day 2 (1 h):** Write integration tests that attempt to read or modify another user’s task and confirm they are rejected.

**Done when** the API rejects all OWASP Top 10 attack scenarios covered, a stolen refresh token is detected and limited, and the test suite passes all security checks.
