## Hints

**Silver 1 – Refresh token rotation & logout**
- *Level 1:* Remember that a refresh token should be stored server‑side so you can revoke it.
- *Level 2:* Use a DB table with columns `token_id`, `user_id`, `revoked`, and generate a new UUID on each rotation.
- *Level 3:* After issuing a new refresh token, update the DB row to mark the old token as revoked before returning the response.

**Silver 2 – Rate limiting login**
- *Level 1:* Add a rate‑limit decorator to the login route.
- *Level 2:* Choose a Redis key pattern like `login:{ip}` and set an expiry of 60 seconds.
- *Level 3:* On the 6th request within a minute, return `HTTPException(status_code=429, detail="Too many attempts")`.

**Gold – Broken object‑level authorization**
- *Level 1:* Fetch the task from the DB and compare its `owner_id` to `current_user.id`.
- *Level 2:* If they differ, raise `HTTPException(status_code=403, detail="Forbidden")`.
- *Level 3:* Write the test to create two users, obtain tokens for each, then attempt cross‑user access and assert the status code.
