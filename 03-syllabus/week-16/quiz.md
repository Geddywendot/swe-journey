## Quiz

1. Which library provides easy response caching for FastAPI?
   a) fastapi-cache2
   b) redis-py
   c) slowapi
   d) rq

2. When configuring fastapi-cache2 with Redis, which URL format is used for the backend?
   a) `redis://redis:6379/0`
   b) `http://redis:6379`
   c) `memcached://redis`
   d) `sqlite:///cache.db`

3. What is the default return HTTP status code when a rate‑limit is exceeded by slowapi?
   a) 400
   b) 401
   c) 429
   d) 503

4. Which component in RQ is responsible for executing queued jobs?
   a) Scheduler
   b) Worker
   c) Broker
   d) Dispatcher

5. In React Query, what does the `staleTime` option control?
   a) How long data is kept in the browser cache after page refresh
   b) The time before a query is considered fresh and will not refetch automatically
   c) The maximum number of retries for a failed fetch
   d) The interval between background refetches

6. Which HTTP header does slowapi add to indicate how many seconds a client should wait before retrying?
   a) `Retry-After`
   b) `RateLimit-Reset`
   c) `X-RateLimit-Limit`
   d) `Cache-Control`

7. Which Prometheus metric type is most appropriate for counting total rate‑limit violations?
   a) Gauge
   b) Counter
   c) Histogram
   d) Summary

8. When using Axios interceptors for caching, where should the cached responses typically be stored?
   a) In localStorage
   b) In a global in‑memory map
   c) In a cookie
   d) In the Redux store
