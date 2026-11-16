## Exercises

**Silver 1**
- [ ] Add `fastapi-cache2` to a GET endpoint (e.g., `/items`) with a 60‑second expiration. Verify that repeated requests hit the cache (observe faster response time).
- [ ] Write a pytest test that calls the endpoint twice and asserts the second call is served from cache (you can mock the underlying data function to confirm it was called only once).

**Silver 2**
- [ ] Set up a Redis service in `docker-compose.yml` and configure `fastapi-cache2` to use Redis as the backend.
- [ ] Implement a background job using RQ: enqueue a function that simulates a long task (e.g., `time.sleep(5)`) and have a worker process it.
- [ ] Write a test that enqueues a job, runs the worker, and checks that the job result is stored.

**Gold**
- [ ] Apply `slowapi` middleware to the FastAPI app with a limit of 5 requests per minute per IP.
- [ ] In the React frontend, use Axios interceptors to cache GET responses for 30 seconds.
- [ ] Add a Prometheus metric that counts rate‑limit hits and ensure it is exported.
- [ ] Verify that rapid requests from the same client receive HTTP 429 responses with proper `Retry-After` headers.