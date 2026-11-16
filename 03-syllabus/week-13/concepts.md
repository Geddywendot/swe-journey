## Concepts

1. **Dockerfile Structure** – A Dockerfile is a series of instructions that create an image layer by layer. It starts from a base image, adds files, runs commands, and defines the default entrypoint. Well‑ordered layers improve cache reuse and build speed.
   
   *Explain it back:* 

2. **Multi‑Stage Builds** – By separating a build stage (e.g., compiling TypeScript or installing dependencies) from a final stage that only contains runtime assets, you dramatically reduce image size and remove build‑time tools from production containers.
   
   *Explain it back:* 

3. **FastAPI Container Entrypoint** – The API container typically runs `uvicorn app:app --host 0.0.0.0 --port 8000`. Exposing the port and configuring `WORKDIR` ensures the code is reachable from other services in the compose network.
   
   *Explain it back:* 

4. **React Production Build with Nginx** – After building the React app (`npm run build`), the static files are copied into an Nginx image that serves them on port 80. This pattern separates the build toolchain from the lightweight web server.
   
   *Explain it back:* 

5. **Docker‑Compose Service Networking** – Services declared in the same `docker‑compose.yml` share an internal network and can reach each other via the service name (`api`, `db`, `frontend`). This eliminates CORS issues in local development and mirrors production service discovery.
   
   *Explain it back:*