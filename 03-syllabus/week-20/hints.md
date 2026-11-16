## Hints

**Silver 1**
- Level 1: Start by running the existing test suite locally.
- Level 2: Remember the concept of *scoping a feature* – focus on the minimum viable change.
- Level 3: Add the new endpoint/module, then run `pytest` in CI; ensure the CI config runs `pytest` on push.

**Silver 2**
- Level 1: Look at the project’s existing README for structure.
- Level 2: Use the *README for a stranger* concept – cover setup, run, test, and deployment.
- Level 3: Create an `adr/` directory and write a one‑page ADR using the template from the repo’s `docs/ADR_TEMPLATE.md`.

**Gold**
- Level 1: Record your screen while walking through the demo.
- Level 2: Deploy using the *Demo vs. Deployment* concept – you need a stable public URL.
- Level 3: Push the Docker image to a registry and configure Render (or Fly.io) with the image tag, then verify the link.
