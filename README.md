
# 🚀 Production-Ready FastAPI Platform (DevOps Project)

This project is a **fully containerized**, **production-grade**, **observable**, and **CI-tested** FastAPI microservice designed to showcase real DevOps engineering skills.

It includes:

- FastAPI backend  
- PostgreSQL database  
- NGINX reverse proxy  
- Docker & Docker Compose  
- CI Pipeline (GitHub Actions)  
- Unit Tests + Linting  
- Health & Readiness endpoints  
- Prometheus Metrics (API + DB + errors + latency)  
- Scalable multi-replica architecture  

---

## 📌 Features Implemented

### ✔ FastAPI Microservice
- `/` — returns message + hostname  
- `/health` — simple health check  
- `/ready` — full DB readiness + metrics  

### ✔ PostgreSQL Integration
- Timeout handling  
- Health checks  
- DB metrics  

### ✔ NGINX Reverse Proxy
- Load balancing across API replicas  
- Proxy headers  
- Production-ready config  

### ✔ Docker + Docker Compose
Services included:
- `api`
- `db`
- `nginx`

### ✔ Observability (Prometheus Metrics)
Metrics exposed at `/metrics`:

| Category | Metrics |
|----------|---------|
| Traffic | `api_requests_total` |
| Latency | `api_request_latency_seconds` |
| Errors | `api_errors_total` |
| DB Health | `db_health_status`, `db_health_failures_total`, `db_health_latency_seconds` |

### ✔ CI/CD Pipeline (GitHub Actions)
Runs on every push:
- Install dependencies  
- Run Flake8 linting  
- Run Black formatter  
- Run Pytest  
- Build Docker image  
- Status badge  

### ✔ Scale API Replicas
```
docker compose up --scale api=3
```

---

## 🐳 Local Development

### Start everything:
```
docker compose up --build
```

### Visit:
- API → http://localhost:8000  
- Metrics → http://localhost:8000/metrics  
- NGINX → http://localhost:8000  

### Run tests:
```
pytest
```

---

# 🧠 Why this project?

✔ Shows DevOps depth  
✔ Production-grade architecture  
✔ Strong resume portfolio project  
✔ Demonstrates CI/CD + Docker + Observability  
✔ Built step-by-step like a real SRE system  

---

# 📌 Author
**Prashant Bisht**
