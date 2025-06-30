import time
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import OperationalError

from settings import Config
load_dotenv()

Base = declarative_base()

class Database:
    _engine = None
    _SessionLocal = None

    @staticmethod
    def initialize(retries=10, delay=3):
        if Database._engine is None:
            Database._engine = create_engine(Config.DATABASE_URL)
            Database._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Database._engine)

        for attempts in range(retries):
            try:
                with Database._engine.connect():
                    break
            except OperationalError:
                print(f"Database is not enable, retrying ({attempts+1}/{retries})...")
                time.sleep(delay)
        else:
            raise RuntimeError("Could not connect to the database after several attempts.")
        Base.metadata.create_all(bind=Database._engine)

    @staticmethod
    def get_session() -> Session:
        if Database._SessionLocal is None:
            raise RuntimeError("Database is not initialized. Call 'Database.initialize()' first.")
        return Database._SessionLocal()