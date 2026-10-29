"""
Роутер подземелий
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_database, get_current_user
from api.schemas.dungeon import DungeonCreate, DungeonUpdate, DungeonResponse
from app.models.user import User
from app.services.catalog_service import CatalogService
from app.services.content_service import ContentService

router = APIRouter(prefix="/dungeons", tags=["Подземелья"])


@router.get("/", response_model=List[DungeonResponse])
def get_all_dungeons(db: Session = Depends(get_database)):
    """Получить список всех подземелий"""
    catalog = CatalogService(db)
    return catalog.dungeons_list()


@router.get("/{dungeon_id}", response_model=DungeonResponse)
def get_dungeon(dungeon_id: int, db: Session = Depends(get_database)):
    """Получить подземелье по ID"""
    catalog = CatalogService(db)
    dungeon = catalog.dungeon_detail(dungeon_id)
    
    if dungeon is None:
        raise HTTPException(status_code=404, detail="Подземелье не найдено")
    
    return dungeon


@router.post("/", response_model=DungeonResponse)
def create_dungeon(
    dungeon: DungeonCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_database)
):
    """Создать новое подземелье"""
    content = ContentService(db)
    ok, message = content.add_dungeon(
        user=current_user,
        name=dungeon.name,
        description=dungeon.description
    )
    
    if not ok:
        raise HTTPException(status_code=400, detail=message)
    
    catalog = CatalogService(db)
    created_dungeon = catalog.dungeon_detail(int(message.split('id_dungeon=')[1].split(')')[0]))
    
    return created_dungeon


@router.put("/{dungeon_id}", response_model=DungeonResponse)
def update_dungeon(
    dungeon_id: int,
    dungeon: DungeonUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_database)
):
    """Обновить подземелье"""
    content = ContentService(db)
    ok, message = content.update_dungeon(
        id_dungeon=dungeon_id,
        name=dungeon.name,
        description=dungeon.description
    )
    
    if not ok:
        raise HTTPException(status_code=400, detail=message)
    
    catalog = CatalogService(db)
    updated_dungeon = catalog.dungeon_detail(dungeon_id)
    
    return updated_dungeon


@router.delete("/{dungeon_id}")
def delete_dungeon(
    dungeon_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_database)
):
    """Удалить подземелье"""
    content = ContentService(db)
    ok, message = content.delete_dungeon(dungeon_id)
    
    if not ok:
        raise HTTPException(status_code=400, detail=message)
    
    return {"message": message}