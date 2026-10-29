"""
Pydantic схемы для классов персонажей
"""
from typing import Optional
from pydantic import BaseModel, Field


class ClassCreate(BaseModel):
    """Схема создания класса"""
    name: str = Field(..., min_length=1, max_length=255, description="Название класса")
    ability_1: Optional[str] = Field(None, description="Способность 1")
    ability_2: Optional[str] = Field(None, description="Способность 2")
    epic_ability_1: Optional[str] = Field(None, description="Эпическая способность 1")
    epic_ability_2: Optional[str] = Field(None, description="Эпическая способность 2")


class ClassUpdate(BaseModel):
    """Схема обновления класса"""
    name: str = Field(..., min_length=1, max_length=255, description="Название класса")
    ability_1: Optional[str] = Field(None, description="Способность 1")
    ability_2: Optional[str] = Field(None, description="Способность 2")
    epic_ability_1: Optional[str] = Field(None, description="Эпическая способность 1")
    epic_ability_2: Optional[str] = Field(None, description="Эпическая способность 2")


class ClassResponse(BaseModel):
    """Схема ответа с данными класса"""
    id_class: int = Field(..., description="ID класса")
    name: str = Field(..., description="Название")
    ability_1: Optional[str] = Field(None, description="Способность 1")
    ability_2: Optional[str] = Field(None, description="Способность 2")
    epic_ability_1: Optional[str] = Field(None, description="Эпическая способность 1")
    epic_ability_2: Optional[str] = Field(None, description="Эпическая способность 2")
    
    class Config:
        from_attributes = True