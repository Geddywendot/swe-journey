## Concepts

1. **Response Caching with fastapi-cache2** – The library stores the result of a route in an in‑memory or Redis backend, so repeated requests for the same parameters return the cached response instantly. Cache keys are generated from the request path and query parameters, and you can configure expiration times per endpoint.
   
   *Explain it back:* 

2. **Distributed Cache using Redis** – Redis provides a shared key‑value store that can be accessed by multiple service instances. It enables fast data retrieval, cross‑process caching, and can also serve as a message broker for queues.
   
   *Explain it back:* 

3. **Background Queues with RQ** – RQ (Redis Queue) lets you enqueue a Python function call that a separate worker process will execute asynchronously. This is useful for tasks like sending emails, processing images, or heavy calculations.
   
   *Explain it back:* 

4. **Rate Limiting with slowapi** – Middleware that tracks request counts per client (IP or API key) and enforces limits (e.g., 100 requests per minute). It adds `Retry-After` and `X-RateLimit-*` headers, and returns HTTP 429 when the limit is exceeded.
   
   *Explain it back:* 

5. **Client‑Side Caching with React Query** – React Query caches fetched data in memory, deduplicates identical requests, and provides automatic refetching policies (stale‑while‑revalidate). It reduces UI latency and network load.
   
   *Explain it back:*