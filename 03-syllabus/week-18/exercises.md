## Exercises

**Silver 1 – Profile a slow endpoint**
- [ ] Identify one endpoint that takes >500 ms.
- [ ] Write a small Python script that records the response time before any changes.
- [ ] Use `uvicorn --log-level debug` and SQL `EXPLAIN` to find the bottleneck.
- [ ] Fix one N+1 query in the endpoint and re‑run the script.
- [ ] Record the before and after timings.

**Silver 2 – Move side‑effect to a background job**
- [ ] Choose a side‑effect (e.g., sending a confirmation email) that currently runs synchronously.
- [ ] Refactor the endpoint to enqueue the work with FastAPI `BackgroundTasks`.
- [ ] Ensure the background function is **idempotent** – add a deduplication check or unique token.
- [ ] Run the endpoint and verify the response returns immediately while the job runs in the background.

**Gold – Load‑test script**
- [ ] Write a Locust script that hits the profiled endpoint twice in succession, capturing latency each time.
- [ ] The script should output a clear comparison (e.g., `Baseline: 620 ms, Optimised: 420 ms`).
- [ ] Ensure the script cleans up any test data it creates so it can be run repeatedly.
- [ ] Run the script and verify the reported improvement matches the manual timing from Silver 1.
