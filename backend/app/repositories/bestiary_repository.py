from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.bestiary import Bestiary
from app.repositories.base import BaseRepository


class BestiaryRepository(BaseRepository[Bestiary]):
    """Слой доступа к данным таблицы bestiary"""
    
    def __init__(self, db: Session):
        super().__init__(Bestiary, db)
    
    def get_all_entries(self) -> List[Bestiary]:
        """Все записи бестиария по порядку id"""
        return self.db.query(Bestiary).order_by(Bestiary.id_bestiary).all()
    
    def get_by_id_bestiary(self, id_bestiary: int) -> Optional[Bestiary]:
        return self.db.query(Bestiary).filter(Bestiary.id_bestiary == id_bestiary).first()
    
    def get_by_name(self, name: str) -> Optional[Bestiary]:
        return self.db.query(Bestiary).filter(Bestiary.name == name).first()
    
    def search_by_name(self, name_part: str) -> List[Bestiary]:
        return self.db.query(Bestiary).filter(Bestiary.name.ilike(f"%{name_part}%")).all()
    
    def get_by_type(self, monster_type: str) -> List[Bestiary]:
        """Монстры указанного типа: 'normal' | 'undead' | 'dragon'"""
        return self.db.query(Bestiary).filter(
            Bestiary.monster_type == monster_type
        ).order_by(Bestiary.level).all()
    
    def get_by_level(self, level: int) -> List[Bestiary]:
        return self.db.query(Bestiary).filter(Bestiary.level == level).all()
    
    def get_by_level_range(self, min_level: int, max_level: int) -> List[Bestiary]:
        return self.db.query(Bestiary).filter(
            Bestiary.level >= min_level,
            Bestiary.level <= max_level,
        ).order_by(Bestiary.level).all()