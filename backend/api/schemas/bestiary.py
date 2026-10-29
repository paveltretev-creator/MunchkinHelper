"""
Pydantic схемы для бестиария
"""
from typing import Optional
from pydantic import BaseModel, Field


class BestiaryCreate(BaseModel):
    """Схема создания монстра"""
    name: str = Field(..., min_length=1, max_length=255, description="Название монстра")
    level: int = Field(..., ge=1, le=100, description="Уровень (1-100)")
    monster_type: str = Field(..., pattern='^(normal|undead|dragon)$', description="Тип монстра")
    description: Optional[str] = Field(None, description="Описание")
    quirk: Optional[str] = Field(None, description="Непотребство")
    xp_reward: int = Field(..., ge=0, le=100, description="Даёт уровней (0-100)")
    treasure_reward: int = Field(..., ge=0, le=100, description="Даёт сокровищ (0-100)")


class BestiaryUpdate(BaseModel):
    """Схема обновления монстра"""
    name: str = Field(..., min_length=1, max_length=255, description="Название монстра")
    level: int = Field(..., ge=1, le=100, description="Уровень (1-100)")
    monster_type: str = Field(..., pattern='^(normal|undead|dragon)$', description="Тип монстра")
    description: Optional[str] = Field(None, description="Описание")
    quirk: Optional[str] = Field(None, description="Непотребство")
    xp_reward: int = Field(..., ge=0, le=100, description="Даёт уровней (0-100)")
    treasure_reward: int = Field(..., ge=0, le=100, description="Даёт сокровищ (0-100)")


class BestiaryResponse(BaseModel):
    """Схема ответа с данными монстра"""
    id_bestiary: int = Field(..., description="ID записи")
    name: str = Field(..., description="Название")
    level: int = Field(..., description="Уровень")
    monster_type: str = Field(..., description="Тип монстра")
    description: Optional[str] = Field(None, description="Описание")
    quirk: Optional[str] = Field(None, description="Непотребство")
    xp_reward: int = Field(..., description="Даёт уровней")
    treasure_reward: int = Field(..., description="Даёт сокровищ")
    
    class Config:
        from_attributes = True