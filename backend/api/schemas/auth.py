"""
Pydantic схемы для авторизации
"""
from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    """Схема запроса авторизации"""
    login: str = Field(..., min_length=1, max_length=255, description="Логин пользователя")
    password: str = Field(..., min_length=1, description="Пароль пользователя")


class LoginResponse(BaseModel):
    """Схема ответа авторизации"""
    success: bool = Field(..., description="Успешность операции")
    message: str = Field(..., description="Сообщение")
    user_id: int | None = Field(None, description="ID пользователя")
    login: str | None = Field(None, description="Логин пользователя")


class RegisterRequest(BaseModel):
    """Схема запроса регистрации"""
    login: str = Field(..., min_length=3, max_length=50, pattern=r'^[A-Za-z0-9_]+$', description="Логин (3-50 символов, латиница/цифры/_)")
    password: str = Field(..., min_length=6, description="Пароль (минимум 6 символов)")
    password_confirm: str = Field(..., min_length=6, description="Подтверждение пароля")


class RegisterResponse(BaseModel):
    """Схема ответа регистрации"""
    success: bool = Field(..., description="Успешность операции")
    message: str = Field(..., description="Сообщение")
    user_id: int | None = Field(None, description="ID созданного пользователя")