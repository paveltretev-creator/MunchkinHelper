"""
Pydantic схемы для игровых данных
"""
from pydantic import BaseModel, Field


class GameStateCreate(BaseModel):
    """Схема создания/обновления игрового состояния"""
    level: int = Field(..., ge=1, description="Уровень (минимум 1)")
    strength: int = Field(..., ge=0, description="Сила (не отрицательная)")
    debuff: int = Field(..., le=0, description="Дебаф (не положительный)")


class GameStateResponse(BaseModel):
    """Схема ответа с игровым состоянием"""
    level: int = Field(..., description="Уровень")
    strength: int = Field(..., description="Сила")
    debuff: int = Field(..., description="Дебаф")
    total: int = Field(..., description="Общая сила")