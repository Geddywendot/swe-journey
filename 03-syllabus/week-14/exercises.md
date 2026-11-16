## Exercises

**Silver 1**
- [ ] Add the CI workflow file by copying `templates/github-actions/ci.yml.example` into `.github/workflows/ci.yml` (do not commit it yet, just verify the copy works locally).
- [ ] Update the workflow to run Vitest unit tests for the React frontend.
- [ ] Verify the GitHub Actions run succeeds on a draft push.

**Silver 2**
- [ ] Extend the CI matrix to include Python 3.10 and 3.12 for FastAPI pytest tests.
- [ ] Add a step that caches `node_modules` and `~/.cache/pip`.
- [ ] Confirm the cache hits on a second run.

**Gold**
- [ ] Add a deployment job that uses the `vercel-action` to deploy the Docker images when the workflow runs on the `main` branch.
- [ ] Store `VERCEL_TOKEN`, `DOCKER_USERNAME`, and `DOCKER_PASSWORD` as repository secrets and reference them securely.
- [ ] Verify that a preview URL appears on a pull‑request and that a production URL is updated after merging to `main`.
