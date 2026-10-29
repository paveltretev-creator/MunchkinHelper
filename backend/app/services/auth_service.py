import re
from typing import Optional, Tuple

from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.utils.security import hash_password, verify_password

# Логин: 3-50 символов, латиница/цифры/подчеркивание
LOGIN_PATTERN = re.compile(r"^[A-Za-z0-9_]{3,50}$")
MIN_PASSWORD_LENGTH = 6


class AuthService:
    """Слой бизнес-логики: регистрация и авторизация пользователей"""
    
    def __init__(self, db: Session):
        self._users = UserRepository(db)
    
    def register(self, login: str, password: str, password_confirm: str) -> Tuple[bool, str]:
        """Регистрация нового пользователя"""
        login = login.strip()
        
        error = self._validate_credentials(login, password, password_confirm)
        if error:
            return False, error
        
        if self._users.exists(login):
            return False, "Пользователь с таким логином уже существует."
        
        user = self._users.create_user(
            login=login,
            password_hash=hash_password(password)
        )
        return True, f"Регистрация успешна! Пользователь '{user.login}' создан (id_user={user.id_user})."
    
    def authenticate(self, login: str, password: str) -> Tuple[Optional[User], str]:
        """Проверка учетных данных (вход)"""
        user = self._users.get_by_login(login.strip())
        
        if user is None or not verify_password(password, user.password_hash):
            return None, "Неверный логин или пароль."
        
        return user, f"Авторизация успешна. Добро пожаловать, {user.login}!"
    
    @staticmethod
    def _validate_credentials(login: str, password: str, password_confirm: str) -> Optional[str]:
        """Валидация данных при регистрации"""
        if not LOGIN_PATTERN.match(login):
            return "Некорректный логин: разрешено 3-50 символов (латиница, цифры, '_')."
        if len(password) < MIN_PASSWORD_LENGTH:
            return f"Пароль слишком короткий: минимум {MIN_PASSWORD_LENGTH} символов."
        if password != password_confirm:
            return "Пароли не совпадают."
        return None