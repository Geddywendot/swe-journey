# Week 18 – Production Readiness for the FastAPI Backend

**Goal:** Make the task API measurably faster, profile slow endpoints, off‑load long‑running work to background jobs, and be able to diagnose performance bottlenecks from logs.

**4‑hour‑per‑day plan**
1. **Day 1 (1 h):** Identify the slowest endpoint by running a simple timing script. Record baseline response times.
2. **Day 1 (1 h):** Use `EXPLAIN (ANALYZE, BUFFERS)` in PostgreSQL to understand query plans for the endpoint.
3. **Day 1 (1 h):** Refactor any N+1 query patterns using eager loading or explicit joins.
4. **Day 1 (1 h):** Add a background task (e.g., sending a confirmation email) using FastAPI’s `BackgroundTasks` and ensure it is idempotent.
5. **Day 2 (2 h):** Write a Locust load‑test script that repeats the endpoint call twice, captures latency, and prints a diff.
6. **Day 2 (1 h):** Run the load test, compare against the baseline, and iterate on the optimisations.
7. **Day 2 (1 h):** Inspect logs (`/var/log/fastapi/*.log`) for warning patterns and bottlenecks, add structured logging where missing.

**Done when** the endpoint latency is at least 30 % faster, the background job processes without duplicate side‑effects, and the load‑test script reports consistent timings across runs.
