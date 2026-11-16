## Hints

**Silver 1**
- *Level 1*: Install `loguru` (`pip install loguru`) and replace `uvicorn` logger with `loguru` in `main.py`.
- *Level 2*: Configure `loguru` with `sink=sys.stdout`, `format="{{time}}|{{level}}|{{message}}"`, and set `serialize=True` to emit JSON.
- *Level 3*: Make a request (`curl http://localhost:8000/items`) and observe a single JSON line containing `"level":"INFO"` and the request path.

**Silver 2**
- *Level 1*: Add a FastAPI route `@app.get("/health")` that returns `{"status":"ok"}`.
- *Level 2*: In the Dockerfile, add `HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1`.
- *Level 3*: Run `docker compose up`, then `docker inspect --format='{{json .State.Health}}' <container>` to see the health status become `healthy`.

**Gold**
- *Level 1*: `pip install prometheus_client` and add `from prometheus_client import Counter, start_http_server`.
- *Level 2*: Create a `REQUEST_COUNT = Counter('request_total', 'Total requests')` and increment it in a dependency that runs on every request.
- *Level 3*: Start the Prometheus exporter (`start_http_server(8001)`) and configure a local Prometheus `scrape_configs` to pull from `http://api:8001/metrics`. Then import the metric into Grafana and build a panel showing `request_total` over time.
