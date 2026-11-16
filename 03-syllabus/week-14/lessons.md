## Lessons

1. **GitHub Actions Overview** – Introduction to CI/CD with GitHub Actions, workflow syntax, and runners. *Time: 45 min* – https://docs.github.com/en/actions/learn-about-github-actions/introduction-to-github-actions
2. **Adding a CI Workflow** – Copying the `templates/github-actions/ci.yml.example` file into `.github/workflows/ci.yml` and customizing the job matrix. *Time: 45 min* – https://docs.github.com/en/actions/using-workflows/about-workflows
3. **Running Tests in CI** – Configuring Vitest, pytest, and Cypress steps, caching dependencies, and publishing test reports. *Time: 45 min* – https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobs
4. **Docker Build in CI** – Building multi‑stage Docker images for the API and frontend inside the workflow, using the `docker/build-push-action`. *Time: 30 min* – https://github.com/docker/build-push-action
5. **Deploying to Vercel (or similar)** – Setting up the `vercel-action` to deploy Docker images or the static site, handling output URLs. *Time: 45 min* – https://github.com/amondnet/vercel-action
6. **Managing Secrets** – Adding `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `VERCEL_TOKEN` as repository secrets and accessing them in the workflow. *Time: 30 min* – https://docs.github.com/en/actions/security-guides/encrypted-secrets
7. **Preview Environments** – Using Vercel preview links or GitHub Pages to generate a live URL for each PR. *Time: 30 min* – https://vercel.com/docs/concepts/projects/environment-variables#preview-environments
8. **Badge Badging** – Adding status badges to the README for CI status and deployment preview. *Time: 15 min* – https://shields.io/