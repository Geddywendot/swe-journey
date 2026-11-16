## Concepts

1. **Measuring before optimizing** – Benchmark the current response time of the slow endpoint using a simple timing script or `curl -w "%{time_total}"`. Capture the baseline so you can quantify any improvement.\n   \
   *Explain it back:*\n
2. **N+1 query problem** – When an endpoint loads a parent object and then issues a separate query for each child, the number of database round‑trips grows linearly. Use eager loading (`joinedload`) or explicit joins to collapse these into a single query.\n   \
   *Explain it back:*\n
3. **Reading an EXPLAIN plan** – `EXPLAIN (ANALYZE, BUFFERS)` returns the actual query execution steps, cost estimates, and I/O usage. Look for sequential scans, missing indexes, or high `actual total time`.\n   \
   *Explain it back:*\n
4. **Background jobs must be idempotent** – A task that may be retried (e.g., sending an email) should not cause duplicate side‑effects. Store a unique token or check‑once flag before performing the action.\n   \
   *Explain it back:*\n
5. **Idempotent load‑test scripts** – A Locust script that runs the same scenario twice should clean up any state it creates (e.g., delete test data) so the second run measures only the system, not leftover data.\n   \
   *Explain it back:*\n