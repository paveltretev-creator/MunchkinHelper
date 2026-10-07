from typing import List

from models.user import User
from repositories.user_repository import UserRepository


class UserService:

    def __init__(self):
        self.repository = UserRepository()
        if not self.repository.connect():
            raise ConnectionError("Не удалось подключиться к БД")

    def create_user(self, login: str, age: str, email: str) -> User:
        
        login = login.strip()
        email = email.strip()
        age = age.strip()

        if not login or not age or not email:
            raise ValueError("Заполните все поля")

        try:
            age_int = int(age)
        except ValueError:
            raise ValueError("Возраст должен быть числом")

        if age_int <= 0 or age_int > 150:
            raise ValueError("Возраст должен быть в диапазоне 1-150")

        user = User(login=login, age=age_int, email=email)
        self.repository.add_user(user)
        return user

    def get_all_users(self) -> List[User]:
        return self.repository.get_all_users()

    def close(self):
        self.repository.close()