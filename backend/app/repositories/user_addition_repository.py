from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.user_addition import UserAddition
from app.repositories.base import BaseRepository


class UserAdditionRepository(BaseRepository[UserAddition]):
    """Слой доступа к данным таблицы user_additions"""
    
    def __init__(self, db: Session):
        super().__init__(UserAddition, db)
    
    def get_by_user(self, id_user: int) -> List[UserAddition]:
        """Все добавления конкретного пользователя"""
        return self.db.query(UserAddition).filter(UserAddition.id_user == id_user).all()
    
    def get_by_target(self, target_entity_type: str, target_entity_id: int) -> Optional[UserAddition]:
        """Найти добавление по типу и id сущности"""
        return self.db.query(UserAddition).filter(
            UserAddition.target_entity_type == target_entity_type,
            UserAddition.target_entity_id == target_entity_id,
        ).first()