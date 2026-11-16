## Quiz

1. What is the main advantage of a multi‑stage Docker build?
   a) It allows you to run containers on multiple hosts.
   b) It reduces the final image size by discarding build‑time dependencies.
   c) It automatically creates a Kubernetes deployment.
   d) It enables hot‑reloading of code inside the container.

2. Which base image is recommended for a lightweight FastAPI production container?
   a) `python:3.12`
   b) `python:3.12‑slim`
   c) `ubuntu:22.04`
   d) `alpine:3.18`

3. In a Dockerfile for a React app built with Vite, which command is typically used to produce the static files?
   a) `npm run dev`
   b) `npm run build`
   c) `npm start`
   d) `npm test`

4. When using Docker‑Compose, how can the `frontend` service reach the `api` service by name?
   a) Use the host IP address of the machine.
   b) Use the environment variable `API_URL`.
   c) Use the service name `api` as the hostname.
   d) Use the container ID.

5. Which Docker‑Compose key is used to ensure a service starts only after another service is healthy?
   a) `links`
   b) `depends_on`
   c) `restart`
   d) `volumes`

6. What environment variable is commonly used to pass the database connection string to a FastAPI container?
   a) `DB_HOST`
   b) `DATABASE_URL`
   c) `POSTGRES_CONN`
   d) `FASTAPI_DB`

7. Which Docker command pushes a built image to a remote registry?
   a) `docker upload`
   b) `docker commit`
   c) `docker push`
   d) `docker export`

8. For a production‑ready Nginx container serving a React build, which directory should the static files be copied to?
   a) `/usr/share/nginx/html`
   b) `/var/www/html`
   c) `/app/dist`
   d) `/etc/nginx/conf.d`
