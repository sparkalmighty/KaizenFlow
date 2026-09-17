"""Application configuration.

Database recommendation for production (online hosting):
  PostgreSQL — use a managed provider (Neon, Supabase, Railway, Render,
  or AWS RDS). Pair with SQLAlchemy + Alembic later, store the connection
  URL in DATABASE_URL, never commit secrets.

For local prototyping only, SQLite is fine. Do not use SQLite in production.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-me")
    DEBUG = os.getenv("FLASK_DEBUG", "1") == "1"
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", "5000"))

    # Prefer PostgreSQL in production, e.g.:
    # postgresql+psycopg://user:pass@host:5432/kaizenflow
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///kaizenflow.db")
