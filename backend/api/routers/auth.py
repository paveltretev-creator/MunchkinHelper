"""
Роутер авторизации и регистрации
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_database
from api.schemas.auth import LoginRequest, LoginResponse, RegisterRequest, RegisterResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Авторизация"])


@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest, db: Session = Depends(get_database)):
    """Авторизация пользователя"""
    auth = AuthService(db)
    user, message = auth.authenticate(request.login, request.password)
    
    if user is None:
        return LoginResponse(success=False, message=message)
    
    return LoginResponse(
        success=True,
        message=message,
        user_id=user.id_user,
        login=user.login
    )


@router.post("/register", response_model=RegisterResponse)
def register(request: RegisterRequest, db: Session = Depends(get_database)):
    """Регистрация нового пользователя"""
    auth = AuthService(db)
    ok, message = auth.register(request.login, request.password, request.password_confirm)
    
    if not ok:
        return RegisterResponse(success=False, message=message)
    
    # Получаем ID созданного пользователя
    user = auth._users.get_by_login(request.login)
    
    return RegisterResponse(
        success=True,
        message=message,
        user_id=user.id_user if user else None
    )