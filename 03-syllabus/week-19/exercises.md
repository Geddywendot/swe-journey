## Exercises

**Silver 1 – Refresh token rotation & logout**
- [ ] Implement OAuth2 password flow that issues an access token (15 min) and a refresh token (30 min).
- [ ] Store refresh tokens in a database table with a unique identifier and a revoked flag.
- [ ] On each refresh request, verify the token is not revoked, issue a new access token **and** a new refresh token, and mark the old refresh token as revoked (rotation).
- [ ] Add a `/logout` endpoint that revokes the provided refresh token.

**Silver 2 – Rate limiting login**
- [ ] Integrate a rate‑limiting library (e.g., `fastapi-limiter`) with Redis backend.
- [ ] Apply a limit of 5 login attempts per minute per IP.
- [ ] Write a test that attempts 6 rapid logins and asserts the 6th receives a 429 response.

**Gold – Broken object‑level authorization tests**
- [ ] Write integration tests that create two users, each with their own tasks.
- [ ] Attempt to `GET /tasks/{id}` for a task belonging to the other user and assert a 403/404 response.
- [ ] Attempt to `PUT /tasks/{id}` to modify another user's task and assert the request is denied.
- [ ] Ensure the tests run against the secured API without disabling security middleware.
