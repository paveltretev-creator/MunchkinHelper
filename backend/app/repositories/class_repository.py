from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.character_class import CharacterClass
from app.repositories.base import BaseRepository


class CharacterClassRepository(BaseRepository[CharacterClass]):
    """Слой доступа к данным таблицы classes"""
    
    def __init__(self, db: Session):
        super().__init__(CharacterClass, db)
    
    def get_by_id_class(self, id_class: int) -> Optional[CharacterClass]:
        return self.db.query(CharacterClass).filter(CharacterClass.id_class == id_class).first()
    
    def get_by_name(self, name: str) -> Optional[CharacterClass]:
        return self.db.query(CharacterClass).filter(CharacterClass.name == name).first()
    
    def search_by_name(self, name_part: str) -> List[CharacterClass]:
        return self.db.query(CharacterClass).filter(CharacterClass.name.ilike(f"%{name_part}%")).all()