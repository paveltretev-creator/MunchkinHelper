"""
Pydantic схемы для рас
"""
from typing import Optional
from pydantic import BaseModel, Field


class RaceCreate(BaseModel):
    """Схема создания расы"""
    name: str = Field(..., min_length=1, max_length=255, description="Название расы")
    ability_1: Optional[str] = Field(None, description="Способность 1")
    ability_2: Optional[str] = Field(None, description="Способность 2")
    epic_ability_1: Optional[str] = Field(None, description="Эпическая способность 1")
    epic_ability_2: Optional[str] = Field(None, description="Эпическая способность 2")


class RaceUpdate(BaseModel):
    """Схема обновления расы"""
    name: str = Field(..., min_length=1, max_length=255, description="Название расы")
    ability_1: Optional[str] = Field(None, description="Способность 1")
    ability_2: Optional[str] = Field(None, description="Способность 2")
    epic_ability_1: Optional[str] = Field(None, description="Эпическая способность 1")
    epic_ability_2: Optional[str] = Field(None, description="Эпическая способность 2")


class RaceResponse(BaseModel):
    """Схема ответа с данными расы"""
    id_race: int = Field(..., description="ID расы")
    name: str = Field(..., description="Название")
    ability_1: Optional[str] = Field(None, description="Способность 1")
    ability_2: Optional[str] = Field(None, description="Способность 2")
    epic_ability_1: Optional[str] = Field(None, description="Эпическая способность 1")
    epic_ability_2: Optional[str] = Field(None, description="Эпическая способность 2")
    
    class Config:
        from_attributes = True