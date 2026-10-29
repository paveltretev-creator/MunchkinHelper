"""
Pydantic схемы для подземелий
"""
from typing import Optional
from pydantic import BaseModel, Field


class DungeonCreate(BaseModel):
    """Схема создания подземелья"""
    name: str = Field(..., min_length=1, max_length=255, description="Название подземелья")
    description: Optional[str] = Field(None, description="Описание")


class DungeonUpdate(BaseModel):
    """Схема обновления подземелья"""
    name: str = Field(..., min_length=1, max_length=255, description="Название подземелья")
    description: Optional[str] = Field(None, description="Описание")


class DungeonResponse(BaseModel):
    """Схема ответа с данными подземелья"""
    id_dungeon: int = Field(..., description="ID подземелья")
    name: str = Field(..., description="Название")
    description: Optional[str] = Field(None, description="Описание")
    
    class Config:
        from_attributes = True