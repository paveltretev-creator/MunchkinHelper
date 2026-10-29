"""
Роутер классов персонажей
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_database, get_current_user
from api.schemas.character_class import ClassCreate, ClassUpdate, ClassResponse
from app.models.user import User
from app.services.catalog_service import CatalogService
from app.services.content_service import ContentService

router = APIRouter(prefix="/classes", tags=["Классы"])


@router.get("/", response_model=List[ClassResponse])
def get_all_classes(db: Session = Depends(get_database)):
    """Получить список всех классов"""
    catalog = CatalogService(db)
    return catalog.classes_list()


@router.get("/{class_id}", response_model=ClassResponse)
def get_class(class_id: int, db: Session = Depends(get_database)):
    """Получить класс по ID"""
    catalog = CatalogService(db)
    char_class = catalog.class_detail(class_id)
    
    if char_class is None:
        raise HTTPException(status_code=404, detail="Класс не найден")
    
    return char_class


@router.post("/", response_model=ClassResponse)
def create_class(
    char_class: ClassCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_database)
):
    """Создать новый класс"""
    content = ContentService(db)
    ok, message = content.add_class(
        user=current_user,
        name=char_class.name,
        ability_1=char_class.ability_1,
        ability_2=char_class.ability_2,
        epic_ability_1=char_class.epic_ability_1,
        epic_ability_2=char_class.epic_ability_2
    )
    
    if not ok:
        raise HTTPException(status_code=400, detail=message)
    
    catalog = CatalogService(db)
    created_class = catalog.class_detail(int(message.split('id_class=')[1].split(')')[0]))
    
    return created_class


@router.put("/{class_id}", response_model=ClassResponse)
def update_class(
    class_id: int,
    char_class: ClassUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_database)
):
    """Обновить класс"""
    content = ContentService(db)
    ok, message = content.update_class(
        id_class=class_id,
        name=char_class.name,
        ability_1=char_class.ability_1,
        ability_2=char_class.ability_2,
        epic_ability_1=char_class.epic_ability_1,
        epic_ability_2=char_class.epic_ability_2
    )
    
    if not ok:
        raise HTTPException(status_code=400, detail=message)
    
    catalog = CatalogService(db)
    updated_class = catalog.class_detail(class_id)
    
    return updated_class


@router.delete("/{class_id}")
def delete_class(
    class_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_database)
):
    """Удалить класс"""
    content = ContentService(db)
    ok, message = content.delete_class(class_id)
    
    if not ok:
        raise HTTPException(status_code=400, detail=message)
    
    return {"message": message}