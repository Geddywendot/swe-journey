## Concepts

1. **Structured Logging** – Instead of plain text logs, each log entry is emitted as a JSON object containing fields such as timestamp, level, message, and request ID. This makes logs machine‑readable and easy to filter in observability platforms.
   
   *Explain it back:* 

2. **Health‑Check Endpoint** – A minimal HTTP endpoint (usually `/health` or `/ready`) that returns a simple `200 OK` when the service can accept traffic. Orchestrators like Docker and Kubernetes use it to decide if a container is healthy.
   
   *Explain it back:* 

3. **Prometheus Metrics Exporter** – The `prometheus_client` library provides a `/metrics` endpoint that emits text‑based metrics (counters, gauges, histograms) that Prometheus scrapes. Metrics are defined in code and automatically updated.
   
   *Explain it back:* 

4. **Docker Healthcheck Directive** – Adding a `HEALTHCHECK` instruction in the Dockerfile instructs Docker to periodically call the health endpoint and mark the container as `healthy` or `unhealthy`.
   
   *Explain it back:* 

5. **Log Aggregation with Loki** – Loki collects log streams, indexes only metadata, and stores raw logs. When combined with Grafana, you can search logs by label (e.g., `service=api`) and correlate with metrics.
   
   *Explain it back:*