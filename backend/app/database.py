"""
Подключение к БД с поддержкой pg8000 для Android
"""
import os
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from app.config import settings


def get_database_url() -> str:
    """Получить URL базы данных"""
    env_url = os.environ.get('DATABASE_URL')
    if env_url:
        return env_url
    return settings.database_url


DATABASE_URL = get_database_url()

# Для pg8000 используется схема postgresql+pg8000
# Для psycopg2 — postgresql или postgresql+psycopg2
if os.environ.get('USE_PG8000') == '1':
    # Преобразуем postgresql:// в postgresql+pg8000://
    if DATABASE_URL.startswith('postgresql://'):
        DATABASE_URL = DATABASE_URL.replace('postgresql://', 'postgresql+pg8000://', 1)
    engine = create_engine(DATABASE_URL)
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()