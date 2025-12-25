import psycopg2
import os
from app.logger import get_logger

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
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            cur.fetchone()
        conn.close()
        return True
    except Exception:
        return False
