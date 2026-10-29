from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.race import Race
from app.repositories.base import BaseRepository


class RaceRepository(BaseRepository[Race]):
    """Слой доступа к данным таблицы races"""
    
    def __init__(self, db: Session):
        super().__init__(Race, db)
    
    def get_by_id_race(self, id_race: int) -> Optional[Race]:
        return self.db.query(Race).filter(Race.id_race == id_race).first()
    
    def get_by_name(self, name: str) -> Optional[Race]:
        return self.db.query(Race).filter(Race.name == name).first()
    
    def search_by_name(self, name_part: str) -> List[Race]:
        return self.db.query(Race).filter(Race.name.ilike(f"%{name_part}%")).all()