## Exercises

**Silver 1**
- [ ] Add a logging configuration to FastAPI that outputs JSON logs using `loguru` or Python `logging` with a JSON formatter.
- [ ] Verify that a request to any endpoint produces a JSON line in the console.

**Silver 2**
- [ ] Implement a `/health` endpoint that returns `{ "status": "ok" }` with HTTP 200.
- [ ] Add a Docker `HEALTHCHECK` that curls this endpoint and exits with code 0 on success.

**Gold**
- [ ] Install `prometheus_client`, expose a `/metrics` endpoint, and define a counter for total requests.
- [ ] Run Prometheus locally, scrape the `/metrics` endpoint, and create a Grafana dashboard showing request rate.
- [ ] Configure Loki to collect the JSON logs, and add a Grafana panel that queries logs for `level="error"`.
- [ ] Define a Prometheus alert that fires if the `/health` endpoint returns non‑200 for more than 2 minutes.
