from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.bestiary import Bestiary
from app.models.character_class import CharacterClass
from app.models.dungeon import Dungeon
from app.models.race import Race
from app.repositories import (
    BestiaryRepository,
    CharacterClassRepository,
    DungeonRepository,
    RaceRepository,
)

MONSTER_TYPE_LABELS = {
    "normal": "Обычный монстр",
    "undead": "Андед",
    "dragon": "Дракон",
}


class CatalogService:
    """Слой бизнес-логики: просмотр справочных данных"""
    
    def __init__(self, db: Session):
        self._bestiary = BestiaryRepository(db)
        self._races = RaceRepository(db)
        self._classes = CharacterClassRepository(db)
        self._dungeons = DungeonRepository(db)
    
    # ---------- БЕСТИАРИЙ ----------
    def bestiary_list(self) -> List[Bestiary]:
        """Полный список монстров"""
        return self._bestiary.get_all_entries()
    
    def bestiary_by_type(self, monster_type: str) -> List[Bestiary]:
        """Список монстров с фильтром по типу"""
        return self._bestiary.get_by_type(monster_type)
    
    def bestiary_detail(self, id_bestiary: int) -> Optional[Bestiary]:
        """Полная карточка монстра"""
        return self._bestiary.get(id_bestiary)
    
    @staticmethod
    def monster_type_label(monster_type: str) -> str:
        """Человекочитаемое название типа монстра"""
        return MONSTER_TYPE_LABELS.get(monster_type, monster_type)
    
    # ---------- РАСЫ ----------
    def races_list(self) -> List[Race]:
        return self._races.get_all()
    
    def race_detail(self, id_race: int) -> Optional[Race]:
        return self._races.get(id_race)
    
    # ---------- КЛАССЫ ----------
    def classes_list(self) -> List[CharacterClass]:
        return self._classes.get_all()
    
    def class_detail(self, id_class: int) -> Optional[CharacterClass]:
        return self._classes.get(id_class)
    
    # ---------- ПОДЗЕМЕЛЬЯ ----------
    def dungeons_list(self) -> List[Dungeon]:
        return self._dungeons.get_all()
    
    def dungeon_detail(self, id_dungeon: int) -> Optional[Dungeon]:
        return self._dungeons.get(id_dungeon)