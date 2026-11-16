## Hints

**Silver 1**
- *Level 1*: Start from `python:3.12-slim`, add `WORKDIR /app`, copy `requirements.txt`, run `pip install -r requirements.txt`.
- *Level 2*: Use `COPY . .` after installing deps, then set `ENV PYTHONUNBUFFERED=1` and `CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]`.
- *Level 3*: Test the image with `docker run --rm -p 8000:8000 api` and `curl http://localhost:8000/health`.

**Silver 2**
- *Level 1*: In the first stage use `FROM node:20-alpine AS build`, copy `package.json`, run `npm ci`, then `npm run build`.
- *Level 2*: In the second stage `FROM nginx:alpine`, copy the built files with `COPY --from=build /app/dist /usr/share/nginx/html` and expose port 80.
- *Level 3*: Verify with `docker run --rm -p 80:80 frontend` and open `http://localhost` in a browser.

**Gold**
- *Level 1*: Define services `api`, `frontend`, `db` in `docker-compose.yml`. Use `depends_on` and a healthcheck for the API (`curl -f http://api:8000/health`).
- *Level 2*: Set environment variables for `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` in the `db` service, and pass `DATABASE_URL` to the `api` service.
- *Level 3*: After `docker compose up -d`, exec into the `frontend` container (`docker exec -it <frontend_container> sh`) and run `curl http://api:8000/items` to confirm end‑to‑end connectivity.
