## Quiz

1. Which GitHub Actions event triggers a workflow on every push to any branch?
   a) `pull_request`
   b) `push`
   c) `workflow_dispatch`
   d) `schedule`

2. In a workflow matrix, how do you specify two Python versions to test against?
   a) `python: ["3.10", "3.12"]`
   b) `python-version: ["3.10", "3.12"]`
   c) `matrix: { python: ["3.10", "3.12"] }`
   d) `versions: python 3.10, 3.12`

3. Which GitHub Action is commonly used to cache `node_modules` between runs?
   a) `actions/checkout`
   b) `actions/cache`
   c) `actions/setup-node`
   d) `actions/upload-artifact`

4. What secret should you store in the repository to authenticate Docker pushes?
   a) `DOCKER_TOKEN`
   b) `DOCKER_PASSWORD`
   c) `DOCKER_REGISTRY`
   d) `DOCKER_URL`

5. Which step in the CI workflow is responsible for building the Docker images?
   a) `docker build`
   b) `docker compose up`
   c) `docker run`
   d) `docker push`

6. When using `vercel-action`, which flag tells Vercel to create a preview deployment instead of production?
   a) `--prod`
   b) `--preview`
   c) `--token`
   d) `--no-commit`

7. How can you add a status badge for CI to the repository README?
   a) Insert an image link from shields.io referencing the workflow name
   b) Add a markdown table with the workflow status
   c) Use a GitHub UI widget
   d) Write a custom HTML tag

8. Which of the following is NOT a recommended practice when storing secrets in GitHub Actions?
   a) Use repository secrets
   b) Hard‑code them in the workflow file
   c) Reference them with `${{ secrets.NAME }}`
   d) Keep them out of logs
