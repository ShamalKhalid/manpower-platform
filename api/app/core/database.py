import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def wait_for_db(retries=10, delay=2):
    for attempt in range(retries):
        try:
            engine.connect()
            print("✅ Database is ready")
            return
        except OperationalError:
            print(f"⏳ Waiting for database... ({attempt + 1}/{retries})")
            time.sleep(delay)
    raise Exception("❌ Database not available")
