# Prod API Platform (DevOps Project)
A production-style FastAPI application demonstrating:
- Docker Compose multi-service architecture
- Reverse proxy with NGINX
- Scalable API containers
- Health & readiness checks
- Environment-specific overrides
## Architecture
Client → NGINX → FastAPI (scaled) → PostgreSQL
## Tech Stack
- FastAPI
- Docker & Docker Compose
- NGINX
- PostgreSQL
## Run Locally
```bash
docker compose up --build --scale api=2


