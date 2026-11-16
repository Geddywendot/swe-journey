## Retro

- **What was hard?**
  - Configuring Loki to ingest JSON logs and ensuring the log format matched the expected label schema.

- **What can I do now?**
  - Deploy structured logging and Prometheus metrics in production, and use Grafana to monitor service health.

- **What will I change?**
  - Add a dedicated logging library wrapper to standardize fields (timestamp, request_id) across all services before enabling Loki.