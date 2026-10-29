from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.dungeon import Dungeon
from app.repositories.base import BaseRepository


class DungeonRepository(BaseRepository[Dungeon]):
    """Слой доступа к данным таблицы dungeons"""
    
    def __init__(self, db: Session):
        super().__init__(Dungeon, db)
    
    def get_by_id_dungeon(self, id_dungeon: int) -> Optional[Dungeon]:
        return self.db.query(Dungeon).filter(Dungeon.id_dungeon == id_dungeon).first()
    
    def get_by_name(self, name: str) -> Optional[Dungeon]:
        return self.db.query(Dungeon).filter(Dungeon.name == name).first()
    
    def search_by_name(self, name_part: str) -> List[Dungeon]:
        return self.db.query(Dungeon).filter(Dungeon.name.ilike(f"%{name_part}%")).all()