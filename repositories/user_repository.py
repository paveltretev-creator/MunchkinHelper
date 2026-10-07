from typing import List

from repositories.base_repository import BaseRepository
from models.user import User


class UserRepository(BaseRepository):

    def get_all_users(self) -> List[User]:
        with self.get_cursor() as cursor:
            cursor.execute("SELECT login, age, email FROM users ORDER BY login")
            rows = cursor.fetchall()
        return [User(login=r['login'], age=r['age'], email=r['email']) for r in rows]

    def add_user(self, user: User) -> None:
        with self.get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (login, age, email) VALUES (%s, %s, %s)",
                (user.login, user.age, user.email)
            )
            self.connection.commit()