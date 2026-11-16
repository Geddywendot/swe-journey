## Hints

**Silver 1**
- *Level 1*: Draw a component diagram on paper or using draw.io, showing Client → API Gateway → Application Service → Database.
- *Level 2*: Identify three failure points (e.g., API instance crash, DB connection loss, network partition) and note a mitigation such as load balancer health checks, replica databases, or circuit breaker patterns.
- *Level 3*: Translate the diagram into Mermaid syntax (`graph TD; client-->api; api-->service; service-->db;`), then render it with the Mermaid live editor to verify correctness.

**Silver 2**
- *Level 1*: Write a 500‑word essay comparing MERN (Express + MongoDB) vs FastAPI‑Postgres focusing on data modeling, scaling, and ops.
- *Level 2*: Outline the essay with headings (e.g., Language, Data Model, Scaling, Deployment) and fill in bullet points for each.
- *Level 3*: Convert the outline into Markdown, ensuring you have at least three paragraphs per section and a concluding summary.

**Gold**
- *Level 1*: Sketch a high‑level system: Load balancer → multiple FastAPI instances → Redis cache → PostgreSQL replica set → background worker queue.
- *Level 2*: Write the Mermaid diagram for the full system, adding sub‑graphs for the cache and worker.
- *Level 3*: Draft a brief presentation outline (intro, design goals, architecture diagram, MERN vs FastAPI trade‑offs, conclusion) and record a mock partner explanation of one design choice.
