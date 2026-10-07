from typing import List

from models.user import User
from models.user_status import UserStatus, ALLOWED_TRANSITIONS
from models.character import Character
from repositories.user_repository import UserRepository
from exceptions import NotFoundException, ConflictException


class UserService:

    def __init__(self):
        self.repository = UserRepository()
        if not self.repository.connect():
            raise ConnectionError("Не удалось подключиться к БД")

    # ---------- Часть 1: валидация переходов ----------

    def change_status(self, login: str, new_status: UserStatus) -> User:
        """
        Меняет статус пользователя с проверкой разрешённости перехода.
        Логика НЕ в контроллере — здесь, в сервисе (критерий 2).
        """
        user = self.repository.get_by_login(login)
        if not user:
            raise NotFoundException(f"Пользователь '{login}' не найден")

        current = user.status
        allowed = ALLOWED_TRANSITIONS.get(current, set())

        if new_status not in allowed:
            # Критерий 3: минимум 2 запрещённых перехода
            raise ConflictException(
                f"Переход {current.value} → {new_status.value} запрещён"
            )

        self.repository.update_status(login, new_status)
        user.status = new_status
        return user

    # ---------- Часть 2: транзакция User + Characters ----------

    def register_with_characters(
        self,
        login: str,
        age: int,
        email: str,
        characters_data: List[dict]
    ) -> User:
        """
        Создаёт пользователя и его персонажей в одной транзакции.
        При ошибке — ничего не сохраняется (критерий 4).
        """
        self._validate_user(login, age, email)

        characters = [
            Character(
                name=ch['name'],
                race=ch['race'],
                character_class=ch['character_class'],
                user_login=login
            )
            for ch in characters_data
        ]

        user = User(login=login, age=age, email=email)

        # Если здесь упадёт — транзакция откатится
        self.repository.create_user_with_characters(user, characters)
        return user

    # ---------- Вспомогательные ----------

    def get_all_users(self) -> List[User]:
        return self.repository.get_all_users()

    def get_user(self, login: str) -> User:
        user = self.repository.get_by_login(login)
        if not user:
            raise NotFoundException(f"Пользователь '{login}' не найден")
        return user

    def _validate_user(self, login: str, age: int, email: str):
        if not login or not email:
            raise ValueError("Логин и почта обязательны")
        if not isinstance(age, int) or age <= 0 or age > 150:
            raise ValueError("Возраст должен быть числом 1-150")

    def close(self):
        self.repository.close()