from typing import Optional

from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    """Слой доступа к данным таблицы users"""
    
    def __init__(self, db: Session):
        super().__init__(User, db)
    
    def get_by_login(self, login: str) -> Optional[User]:
        """Получить пользователя по логину"""
        return self.db.query(User).filter(User.login == login).first()
    
    def exists(self, login: str) -> bool:
        """Проверить существование пользователя с таким логином"""
        return self.get_by_login(login) is not None
    
    def create_user(self, login: str, password_hash: str) -> User:
        """Создать нового пользователя"""
        return self.create({"login": login, "password_hash": password_hash})