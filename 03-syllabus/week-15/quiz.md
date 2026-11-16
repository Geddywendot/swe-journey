## Quiz

1. What is the main benefit of structured (JSON) logging?
   a) Smaller file sizes
   b) Easier to read by humans
   c) Machine‑readable fields for filtering and aggregation
   d) Faster write performance

2. Which HTTP status code should a health‑check endpoint return when the service is healthy?
   a) 200
   b) 201
   c) 302
   d) 500

3. In Docker, which instruction defines a periodic health test for a container?
   a) `HEALTHCHECK`
   b) `CMD`
   c) `ENTRYPOINT`
   d) `RUN`

4. Which Python library provides a `/metrics` endpoint compatible with Prometheus?
   a) `prometheus_client`
   b) `statsd`
   c) `grafana-client`
   d) `monitoring`

5. Which metric type is best suited for counting the total number of HTTP requests?
   a) Gauge
   b) Counter
   c) Histogram
   d) Summary

6. Which tool is commonly used to collect and query JSON logs in Grafana?
   a) Prometheus
   b) Loki
   c) ElasticSearch
   d) InfluxDB

7. A Prometheus alert rule should use which field to specify the condition duration?
   a) `for`
   b) `duration`
   c) `time`
   d) `interval`

8. Which of the following is NOT a recommended practice for logging in production?
   a) Logging at `DEBUG` level for all requests
   b) Including request IDs for traceability
   c) Using a structured format like JSON
   d) Rotating log files or streaming to a central system