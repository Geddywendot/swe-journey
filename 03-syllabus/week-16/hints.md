## Hints

**Silver 1**
- *Level 1*: Install `fastapi-cache2` (`pip install fastapi-cache2`) and add `from fastapi_cache import FastAPICache` and `from fastapi_cache.backends.inmemory import InMemoryBackend`.
- *Level 2*: In `main.py` call `FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")` and decorate the route with `@cache(expire=60)`.
- *Level 3*: Use `time.time()` before and after two requests to see the second call is significantly faster; optionally mock the data function to assert it runs once.

**Silver 2**
- *Level 1*: Add a `redis:` service in `docker-compose.yml` (image `redis:7-alpine`).
- *Level 2*: Change the cache backend to `RedisBackend(redis_url="redis://redis:6379")` and restart the compose stack.
- *Level 3*: Install `rq` (`pip install rq`) and create a `worker.py` that runs `Worker(['default'])`. Enqueue a job with `await q.enqueue(my_task, arg)` and start the worker container.

**Gold**
- *Level 1*: Install `slowapi` (`pip install slowapi`) and add `limiter = Limiter(key_func=get_remote_address)` then `app.state.limiter = limiter` and include `app.add_exception_handler(429, _rate_limit_exceeded_handler)`.
- *Level 2*: Decorate a route with `@limiter.limit("5/minute")` and test by sending six rapid requests; the sixth should return 429.
- *Level 3*: In the React project, set up an Axios interceptor that stores GET responses in a simple in‑memory map with a timestamp, returning the cached value if the request URL matches and is younger than 30 seconds.
- *Level 4*: In the FastAPI app, use `from prometheus_client import Counter` to create `RATE_LIMIT_HITS = Counter('rate_limit_hits', 'Number of rate limit violations')` and increment it in the 429 exception handler. Verify the metric appears at `/metrics`.
