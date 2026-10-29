from typing import TypeVar, Generic, Type, Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import inspect
from app.database import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):
    """Базовый репозиторий с динаическим определением первичного ключа"""
    
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db
        # Динамически получаем имя колонки первичного ключа (id_user, id_monster и т.д.)
        self.pk_name = inspect(self.model).primary_key[0].name
    
    def get(self, pk_value: int) -> Optional[ModelType]:
        """Получить объект по его первичному ключу"""
        return self.db.query(self.model).filter(getattr(self.model, self.pk_name) == pk_value).first()
    
    def get_multi(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """Получить список объектов"""
        return self.db.query(self.model).offset(skip).limit(limit).all()
    
    def create(self, obj_in: dict) -> ModelType:
        """Создать новый объект"""
        db_obj = self.model(**obj_in)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
    
    def update(self, pk_value: int, obj_in: dict) -> Optional[ModelType]:
        """Обновить объект"""
        db_obj = self.get(pk_value)
        if not db_obj:
            return None
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
    
    def delete(self, pk_value: int) -> bool:
        """Удалить объект"""
        db_obj = self.get(pk_value)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_all(self) -> List[ModelType]:
        """Получить все объекты таблицы"""
        return self.db.query(self.model).all()