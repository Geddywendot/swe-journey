## Hints

**Silver 1**
- *Level 1*: Verify the `templates/github-actions/ci.yml.example` file exists in the repository and copy it with `cp` to `.github/workflows/ci.yml`.
- *Level 2*: Open the copied workflow and locate the `run` step for Vitest; ensure the command `npm ci && npm run test` is present.
- *Level 3*: Push a temporary commit to a branch and look at the Actions tab to confirm the job runs without errors.

**Silver 2**
- *Level 1*: Add a `matrix` entry under `strategy` with `python-version: ["3.10", "3.12"]`.
- *Level 2*: Insert an `actions/cache` step before installing dependencies, using `key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}` and a similar one for `node_modules`.
- *Level 3*: Re‑run the workflow and notice the cache summary showing a `Cache hit` on the second run.

**Gold**
- *Level 1*: Add a new job named `deploy` that uses `vercel-action@v20` and runs only on `push` to `main`.
- *Level 2*: In the job, set `vercel-token: ${{ secrets.VERCEL_TOKEN }}`, `vercel-args: "--prod"`, and provide the Docker image tags as inputs.
- *Level 3*: Open a pull request, watch the Actions run, and verify the output contains a `Preview URL:` line; after merging, confirm the production URL updates.
