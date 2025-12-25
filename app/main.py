from fastapi import FastAPI
from app.db import get_connection, check_db_health
from app.logger import get_logger
from fastapi import HTTPException
import socket

HOSTNAME = socket.gethostname()

MAX_Retires = 5
RETRY_DELAY = 2

logger = get_logger(__name__)
app = FastAPI()

db_ready = False


@app.on_event("startup")
def startup_event():
    logger.info("API service started")


@app.get("/ready")
def readiness():
    if check_db_health():
        return {"status": "ready"}
    ##logger.warning("Readiness check failed", exc_info=True)
    raise HTTPException(status_code=503, detail="Database not ready")


@app.get("/")
def root():
    return {"message": "Hello", "served_by": HOSTNAME}


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
