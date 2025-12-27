from prometheus_client import (
    Counter,
    generate_latest,
    CONTENT_TYPE_LATEST,
    Histogram,
    Gauge,
)
from fastapi import APIRouter, Response

router = APIRouter()

# Count every request to the API root
REQUEST_COUNT = Counter(
    "api_requests_total", "Total number of API requests", ["endpoint"]
)

REQUEST_LATENCY = Histogram(
    "api_request_latency_seconds", "Requst latency in seconds", ["endpoint"]
)

ERROR_COUNT = Counter(
    "api_errors_total", "Total numer of API errors", ["endpoint", "status_code"]
)

DB_HEALTH = Gauge("db_health_status", "Database health status (1 = up, 0 = down)")
DB_HEALTH_FAILURES = Counter(
    "db_health_failures_total", "Number of failed database health checks"
)
DB_HEALTH_LATENCY = Histogram(
    "db_health_latency_seconds", "Time taken to check DB health"
)


@router.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(data, media_type=CONTENT_TYPE_LATEST)
