# Quiz 07

Test your understanding of asynchronous Python, FastAPI mechanics, and Pydantic validation. Record your answers before checking with your learning partner.

1. What occurs if a developer calls a long-running, blocking synchronous function (such as `time.sleep(10)` or a synchronous database driver) directly inside an `async def` FastAPI route handler?
   a) FastAPI automatically spins up a background OS thread for it.  
   b) The entire asyncio event loop is blocked for 10 seconds, stalling all other concurrent HTTP requests on that worker process.  
   c) The request is aborted with a 504 Gateway Timeout immediately.  
   d) The function runs concurrently without issue.  
   *(Answer key: `instructor-keys/quiz-07.md`)*

2. In Pydantic v2, how is an optional field with a default value of `None` properly typed?
   a) `name: str = None`  
   b) `name: Optional = ...`  
   c) `name: str | None = None`  
   d) `name: Nullable[str]`  
   *(Answer key: `instructor-keys/quiz-07.md`)*

3. What HTTP response status code does FastAPI return by default when a client submits a JSON request body that fails Pydantic schema validation?
   a) `400 Bad Request`  
   b) `422 Unprocessable Entity`  
   c) `500 Internal Server Error`  
   d) `405 Method Not Allowed`  
   *(Answer key: `instructor-keys/quiz-07.md`)*

4. How does FastAPI's dependency injection system handle dependencies that use Python generator functions (`yield`)?
   a) It only executes the code before `yield`, ignoring code after `yield`.  
   b) The code before `yield` runs before the route handler, and the code after `yield` runs after the response is generated, ensuring cleanup (like closing database connections).  
   c) Generator functions are not supported as dependencies.  
   d) It creates an infinite streaming loop.  
   *(Answer key: `instructor-keys/quiz-07.md`)*

5. Why is `app.dependency_overrides` particularly powerful when authoring automated integration tests?
   a) It allows replacing heavy external services (e.g., live databases, payment gateways) with fast in-memory test doubles without altering production code.  
   b) It speeds up Python's bytecode compilation.  
   c) It disables Pydantic type validation during testing.  
   d) It converts all async functions into sync functions.  
   *(Answer key: `instructor-keys/quiz-07.md`)*

6. What is the fundamental difference between HTTP `PUT` and `PATCH` in REST API conventions?
   a) `PUT` is used for queries; `PATCH` is used for deletions.  
   b) `PUT` replaces the entire target resource representation; `PATCH` applies partial modifications to specific fields.  
   c) `PUT` is asynchronous; `PATCH` is synchronous.  
   d) `PUT` requires JSON; `PATCH` requires XML.  
   *(Answer key: `instructor-keys/quiz-07.md`)*

7. If a route handler needs to run CPU-bound work (like image resizing or cryptography) in FastAPI, what is the recommended approach?
   a) Run it directly inside `async def`.  
   b) Offload it using `asyncio.to_thread(func, *args)` or a background task queue (Celery/RQ) to prevent starving the event loop.  
   c) Decrease the server port number.  
   d) Increase Pydantic timeout.  
   *(Answer key: `instructor-keys/quiz-07.md`)*

8. How does declaring `response_model=ProductResponse` on an endpoint protect application security?
   a) It encrypts the HTTP transmission with SSL.  
   b) It filters and serializes the return value through the schema, ensuring internal fields (such as `hashed_password` or internal IDs) are omitted from the client response.  
   c) It checks for SQL injection strings.  
   d) It limits request rate to 10 requests per minute.  
   *(Answer key: `instructor-keys/quiz-07.md`)*
