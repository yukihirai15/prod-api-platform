from fastapi import FastAPI
from app.db import get_connection
from app.db import check_db_health
from app.logger import get_logger
from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
import socket
from app.metrics import (
    REQUEST_COUNT,
    router as metrics_router,
    REQUEST_LATENCY,
    ERROR_COUNT,
)
import time

HOSTNAME = socket.gethostname()

MAX_Retires = 5
RETRY_DELAY = 2

logger = get_logger(__name__)
app = FastAPI()

app.include_router(metrics_router)

db_ready = False


@app.exception_handler(StarletteHTTPException)
async def starlette_http_exception_handler(
    request: Request, exc: StarletteHTTPException
):
    ERROR_COUNT.labels(endpoint=request.url.path, status_code=exc.status_code).inc()
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    ERROR_COUNT.labels(endpoint=request.url.path, status_code=500).inc()

    return JSONResponse(
        status_code=500,
        content={"detail": " Internal Server Error "},
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    ERROR_COUNT.labels(endpoint=request.url.path, status_code=exc.status_code).inc()

    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@app.on_event("startup")
def startup_event():
    logger.info("API service started")


@app.get("/ready")
def readiness():
    try:
        check_db_health()
        return {"status": "ready"}

    except Exception:
        raise HTTPException(status_code=503, detail="Database not ready")
        logger.warning("Readiness check failed", exc_info=True)


@app.get("/")
def root():
    start_time = time.time()

    result = {"message": "Hello", "served_by": HOSTNAME}

    duration = time.time() - start_time
    REQUEST_COUNT.labels(endpoint="/").inc()
    REQUEST_LATENCY.labels(endpoint="/").observe(duration)

    return result


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/users")
def get_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


@app.get("/boom")
def boom():
    raise Exception("Something broke")


@app.get("/bad")
def bad():
    raise HTTPException(status_code=400, detail="Bad Request")
