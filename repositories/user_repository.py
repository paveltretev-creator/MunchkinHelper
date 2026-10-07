from typing import List, Optional
from contextlib import contextmanager

from repositories.base_repository import BaseRepository
from models.user import User
from models.user_status import UserStatus
from models.character import Character


class UserRepository(BaseRepository):

    # ---------- Базовые методы ----------

    def get_all_users(self) -> List[User]:
        with self.get_cursor() as cursor:
            cursor.execute(
                "SELECT login, age, email, status FROM users ORDER BY login"
            )
            rows = cursor.fetchall()
        return [self._row_to_user(r) for r in rows]

    def get_by_login(self, login: str) -> Optional[User]:
        with self.get_cursor() as cursor:
            cursor.execute(
                "SELECT login, age, email, status FROM users WHERE login = %s",
                (login,)
            )
            row = cursor.fetchone()
        return self._row_to_user(row) if row else None

    def add_user(self, user: User) -> None:
        with self.get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (login, age, email, status) VALUES (%s, %s, %s, %s)",
                (user.login, user.age, user.email, user.status.value)
            )
            self.connection.commit()

    # ---------- Методы для статусов (Часть 1) ----------

    def update_status(self, login: str, new_status: UserStatus) -> None:
        with self.get_cursor() as cursor:
            cursor.execute(
                "UPDATE users SET status = %s WHERE login = %s",
                (new_status.value, login)
            )
            self.connection.commit()

    # ---------- Транзакция: User + Characters (Часть 2) ----------

    @contextmanager
    def transaction(self):
        """Контекст для атомарных операций."""
        if not self.connection:
            self.connect()
        try:
            yield self.connection
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise

    def create_user_with_characters(
        self, user: User, characters: List[Character]
    ) -> None:
        """Создаёт пользователя и его персонажей в ОДНОЙ транзакции."""
        with self.transaction():
            cursor = self.connection.cursor()
            try:
                # 1. Создаём пользователя
                cursor.execute(
                    "INSERT INTO users (login, age, email, status) "
                    "VALUES (%s, %s, %s, %s)",
                    (user.login, user.age, user.email, user.status.value)
                )
                # 2. Создаём всех персонажей
                for ch in characters:
                    cursor.execute(
                        "INSERT INTO characters (name, race, character_class, user_login) "
                        "VALUES (%s, %s, %s, %s)",
                        (ch.name, ch.race, ch.character_class, user.login)
                    )
            except Exception:
                # rollback произойдёт автоматически в contextmanager
                raise
            finally:
                cursor.close()

    # ---------- Helpers ----------

    @staticmethod
    def _row_to_user(row) -> User:
        return User(
            login=row['login'],
            age=row['age'],
            email=row['email'],
            status=UserStatus(row['status'])
        )