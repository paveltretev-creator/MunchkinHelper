"""
Pydantic схемы для пользователя
"""
from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    """Схема ответа с данными пользователя"""
    id_user: int = Field(..., description="ID пользователя")
    login: str = Field(..., description="Логин пользователя")
    
    class Config:
        from_attributes = True