"""
Зависимости для API
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.database import SessionLocal, get_db
from app.models.user import User
from app.services.auth_service import AuthService


security = HTTPBearer()


def get_database() -> Session:
    """Получить сессию БД"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_database)
) -> User:
    """Получить текущего пользователя по токену"""
    # TODO: Реализовать JWT токены для продакшена
    # Пока используем упрощенную схему - передаем login в токене
    token = credentials.credentials
    
    auth = AuthService(db)
    user = auth._users.get_by_login(token)
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователь не найден"
        )
    
    return user