## Concepts

1. **GitHub Actions Workflow Structure** – A workflow is defined in a YAML file under `.github/workflows/` and consists of `on`, `jobs`, and `steps`. Each job runs on a runner, can have a matrix of environments, and defines the exact sequence of actions to execute.
   
   *Explain it back:* 

2. **Job Matrix for Multiple Test Environments** – Using a matrix allows the same job to run against different configurations (e.g., Node versions, Python versions). This provides broader coverage without duplicating YAML.
   
   *Explain it back:* 

3. **Caching Dependencies** – Caching `node_modules` and `~/.cache/pip` between runs dramatically speeds up CI. The `actions/cache` action stores the files based on a hash of lock files.
   
   *Explain it back:* 

4. **Deploy Step with Vercel Action** – The `vercel-action` authenticates with a token, uploads the built artifact, and returns a preview URL. It can be conditioned to run only on the `main` branch or on PRs.
   
   *Explain it back:* 

5. **Managing Secrets Securely** – Secrets added in the repository settings are injected as environment variables during the run, never exposed in logs. They are accessed via `${{ secrets.NAME }}` in the workflow.
   
   *Explain it back:*