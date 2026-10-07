import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager

from config.db_config import DB_CONFIG


class BaseRepository:

    def __init__(self):
        self.db_config = DB_CONFIG
        self.connection = None

    def connect(self) -> bool:
        try:
            self.connection = psycopg2.connect(**self.db_config)
            return True
        except Exception as e:
            print(f"Ошибка подключения к БД: {e}")
            return False

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    @contextmanager
    def get_cursor(self):
        if not self.connection:
            self.connect()

        cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        try:
            yield cursor
        finally:
            cursor.close()