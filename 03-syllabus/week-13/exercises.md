## Exercises

**Silver 1**
- [ ] Write a Dockerfile for the FastAPI backend that uses a `python:3.12-slim` base, installs dependencies from `requirements.txt`, copies the source code, and sets the entrypoint to `uvicorn app:app --host 0.0.0.0 --port 8000`.
- [ ] Build the image locally (`docker build -t api .`) and run a container to verify the API responds on `http://localhost:8000/health`.

**Silver 2**
- [ ] Write a Dockerfile for the React frontend that uses a multi‑stage build: first stage with `node:20-alpine` to run `npm install && npm run build`, second stage with `nginx:alpine` to serve the `dist` folder.
- [ ] Build and run the frontend container, ensuring the UI loads at `http://localhost:80` and can fetch data from the API container via the compose network.

**Gold**
- [ ] Create a `docker-compose.yml` that defines three services: `api`, `frontend`, and `db` (PostgreSQL). Configure environment variables for database credentials, healthchecks for both API and DB, and a shared network.
- [ ] Bring the stack up with `docker compose up -d`, run a simple curl against the API from the frontend container, and verify data flows end‑to‑end.
- [ ] Push both images to a container registry (e.g., GitHub Packages) using `docker push`, and update the compose file to pull the images instead of building locally.
