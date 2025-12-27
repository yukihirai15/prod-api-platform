import psycopg2
import os
from app.logger import get_logger
import time

logger = get_logger(__name__)


def get_connection():
    logger.info(" Connecting to Database ")
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        connect_timeout=3,
    )


def check_db_health():
    from app.metrics import DB_HEALTH, DB_HEALTH_LATENCY, DB_HEALTH_FAILURES

    start = time.time()
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            cur.fetchone()
        # DB is healthy
        DB_HEALTH.set(1)
    except Exception:
        # DB is unhealthy
        DB_HEALTH.set(0)
        DB_HEALTH_FAILURES.inc()
        raise

    finally:
        DB_HEALTH_LATENCY.observe(time.time() - start)
        if "conn" in locals():
            conn.close()
