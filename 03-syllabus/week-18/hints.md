## Hints

**Silver 1 – Profile a slow endpoint**
- *Level 1:* Run `time curl http://localhost:8000/slow` to see the total time.
- *Level 2:* Look at the FastAPI log output for the request duration and the SQL query printed by SQLAlchemy.
- *Level 3:* Add `EXPLAIN (ANALYZE, BUFFERS)` to the query in your repository code and compare the plan before/after fixing the N+1.

**Silver 2 – Background job**
- *Level 1:* Add `BackgroundTasks` as a parameter to the endpoint function.
- *Level 2:* Store a unique UUID in a `processed_jobs` table before sending the email; skip if it already exists.
- *Level 3:* Verify the email sending code checks the UUID and returns early on duplicates.

**Gold – Load‑test script**
- *Level 1:* Use `locust -f load_test.py --headless -u 1 -r 1 --run-time 30s`.
- *Level 2:* Inside `load_test.py`, call the endpoint, record `response.elapsed.total_seconds()`, and store in a list.
- *Level 3:* After the run, compute the average of the two runs and `print(f"Baseline: {a} ms, Optimised: {b} ms")`.
