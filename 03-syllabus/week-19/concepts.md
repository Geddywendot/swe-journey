## Concepts

1. **Access tokens vs. refresh tokens** – Access tokens are short‑lived JWTs used for authorising requests; refresh tokens are longer‑lived secrets that can be exchanged for new access tokens. Rotating refresh tokens on each use limits the window an attacker has if a token is stolen.\n   \
   *Explain it back:*\n
2. **Broken object‑level authorization** – Ensures a user cannot access or modify resources belonging to another user (e.g., reading another user's task). Implement checks that compare the authenticated user’s ID with the resource owner’s ID before performing any action.\n   \
   *Explain it back:*\n
3. **Rate limiting for login** – Limits the number of login attempts per IP or user within a time window, mitigating credential‑stuffing attacks. Usually enforced with a token bucket or leaky‑bucket algorithm stored in a fast cache like Redis.\n   \
   *Explain it back:*\n
4. **Input validation as a security boundary** – Validates request data against a strict schema (type, length, pattern) before processing. Prevents injection attacks, malformed data, and helps enforce business rules. Pydantic models in FastAPI provide automatic validation.\n   \
   *Explain it back:*\n
5. **Secrets management** – Never store API keys, JWT secrets, or database passwords in source control. Use environment variables, secret managers (e.g., Vercel Secrets, HashiCorp Vault) and load them at runtime.\n   \
   *Explain it back:*\n