import psycopg2
import os
from logger import get_logger

logger = get_logger(__name__)

def get_connection():
   logger.info(" Connecting to Database ")
   return psycopg2.connect(
       host=os.getenv("DB_HOST"),
       port=os.getenv("DB_PORT"),
       database=os.getenv("DB_NAME"),
       user=os.getenv("DB_USER"),
       password=os.getenv("DB_PASSWORD"),
    )