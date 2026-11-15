# Week 07 Concepts

Master these 6 asynchronous API fundamentals. For each concept, practice explaining it aloud in your own words.

---

### 1. The Async Event Loop & Cooperative Multitasking
- **Plain words:** Unlike synchronous code where an I/O wait (like a network request or database query) blocks the entire OS thread, `asyncio` uses a single-threaded event loop. When a coroutine hits `await`, it yields control back to the loop, which executes other tasks while the I/O completes. Running blocking CPU-bound code or synchronous I/O inside an `async def` function stalls the entire event loop.
- **Explain it back prompt:** *"Why does calling `time.sleep(5)` inside an `async def` endpoint freeze all incoming requests to the FastAPI server, whereas `await asyncio.sleep(5)` does not?"*

### 2. Request Parsing, Validation, and Serialization with Pydantic v2
- **Plain words:** Pydantic models define the contract for API payloads. It parses untrusted client input (JSON, query parameters, headers), casts types safely, enforces constraints (e.g. `@field_validator`, regex, min/max values), and returns standardized 422 Unprocessable Entity errors when inputs fail validation. Output models (`response_model`) guarantee sensitive internal data (like password hashes) is never leaked in HTTP responses.
- **Explain it back prompt:** *"How does `response_model` protect an application from unintentional data exposure, and what performance advantage does Pydantic v2's Rust core provide?"*

### 3. FastAPI Dependency Injection (`Depends`)
- **Plain words:** FastAPI's dependency injection system builds an execution graph for every incoming request. It manages reusable logic such as database session creation, authentication token validation, query pagination parsing, and rate limiting. Dependencies can yield resources (using `try ... finally`), ensuring cleanup occurs when the HTTP response is dispatched.
- **Explain it back prompt:** *"How does `app.dependency_overrides` facilitate unit testing without spinning up real external services?"*

### 4. RESTful Route Design and HTTP Status Semantics
- **Plain words:** REST architectures organize endpoints around nouns (resources) and HTTP verbs (`GET` for reading, `POST` for creation, `PUT`/`PATCH` for replacement/partial update, `DELETE` for removal). Endpoints must return precise status codes: `201 Created` with a `Location` header, `204 No Content` on successful deletion, `400 Bad Request` for business logic violations, `404 Not Found`, and `409 Conflict` for duplicate resources.
- **Explain it back prompt:** *"What is the architectural difference between `PUT` and `PATCH`, and why is `204 No Content` used for `DELETE`?"*

### 5. Centralized Error Handling & Exception Handlers
- **Plain words:** Rather than scattering `try/except` blocks across every route handler, custom domain exceptions (e.g., `EntityNotFoundError`, `InsufficientPermissionsError`) are raised within services or repositories. Custom FastAPI exception handlers intercept these errors globally, logging diagnostics and returning consistent, structured RFC-7807 problem details or custom error envelopes.
- **Explain it back prompt:** *"Why is handling errors globally via `@app.exception_handler` superior to wrapping individual endpoint bodies in try-except blocks?"*

### 6. Middleware and CORS Configuration
- **Plain words:** Middleware intercepts every incoming request before routing and every outgoing response before client transmission. Common uses include generating unique request IDs (`X-Request-ID`), calculating request processing latency, and enforcing Cross-Origin Resource Sharing (`CORSMiddleware`) headers to permit trusted frontend clients to access the backend.
- **Explain it back prompt:** *"Why must `CORSMiddleware` be configured carefully in production instead of allowing `allow_origins=['*']` with `allow_credentials=True`?"*
