import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load environment variables from the .env file (e.g., DATABASE_URL)
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

#If DATABASE_URL is missing – stop the program with an error
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in .env")

# Create the engine — the main object for connecting to PostgreSQL
engine = create_engine(DATABASE_URL)

# Create a session factory for interacting with the DB
#     autocommit=False  → We manually control commit
#     autoflush=False   → Prevents automatic flush
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy models
# All models (User, Product…) must inherit from Base
Base = declarative_base()


# FastAPI dependency:
#     every time an endpoint needs DB access,
#     FastAPI calls get_db(), creates a session,
#     and closes it after the request is complete.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
