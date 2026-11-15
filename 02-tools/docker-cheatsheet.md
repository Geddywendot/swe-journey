# Docker & Docker Compose Reference

Docker isolates applications and their dependencies into immutable containers. This guide provides essential commands and concepts used across Weeks 12–15 and project deployments.

---

## 1. Core Architecture Concepts

- **Dockerfile:** Text recipe defining how an image is assembled (base OS, runtime, code, entrypoint).
- **Image:** Read-only snapshot containing the application binary/code and OS libraries.
- **Container:** Runnable, isolated instance of an image.
- **Volume:** Persistent storage mounted from the host filesystem, surviving container restarts.
- **Network:** Isolated virtual bridge network enabling containers to resolve each other by service name.

---

## 2. Image Management

```bash
# Build an image with a tag from the current directory Dockerfile
docker build -t task-api:latest .

# Build with a specific Dockerfile and build-arg
docker build -f Dockerfile.prod -t task-api:prod --build-arg ENVIRONMENT=production .

# List all local images
docker images

# Remove an image
docker rmi task-api:latest

# Remove unused/dangling build layers and stopped containers
docker system prune -f
```

---

## 3. Container Lifecycle

```bash
# Run container in background (detached), mapping host port 8000 to container port 8000
docker run -d -p 8000:8000 --name api-service task-api:latest

# Run container with an environment variable
docker run -d -p 8000:8000 -e ENVIRONMENT=production task-api:latest

# Mount a local directory for hot-reloading development
docker run -d -p 8000:8000 -v $(pwd):/app task-api:latest

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# View container output logs (follow stream)
docker logs -f api-service

# Execute an interactive bash shell inside a running container
docker exec -it api-service /bin/bash

# Stop and remove container
docker stop api-service
docker rm api-service
```

---

## 4. Docker Compose Multi-Service Management

```bash
# Start all services declared in docker-compose.yml in the background
docker compose up -d

# Build images before starting containers
docker compose up -d --build

# View logs from all services combined
docker compose logs -f

# View logs for a single service
docker compose logs -f db

# Execute a command inside a compose service
docker compose exec web python -m pytest

# Stop and remove all containers, networks, and orphan volumes
docker compose down

# Stop containers and wipe persistent database volumes (clean reset)
docker compose down -v
```

---

## 5. Security Best Practices
- Never run containers as root in production; define a dedicated non-root user (`USER appuser`).
- Use multi-stage builds to exclude compiler tools (`gcc`, build headers) from runtime images.
- Scan images for vulnerabilities using tools like Trivy or Docker Scout.
