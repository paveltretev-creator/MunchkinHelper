"""
Роутер бестиария
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from api.dependencies import get_database, get_current_user
from api.schemas.bestiary import BestiaryCreate, BestiaryUpdate, BestiaryResponse
from app.models.user import User
from app.services.catalog_service import CatalogService
from app.services.content_service import ContentService

router = APIRouter(prefix="/bestiary", tags=["Бестиарий"])


@router.get("/", response_model=List[BestiaryResponse])
def get_all_monsters(
    monster_type: str = Query(None, description="Фильтр по типу монстра"),
    db: Session = Depends(get_database)
):
    """Получить список всех монстров"""
    catalog = CatalogService(db)
    
    if monster_type:
        monsters = catalog.bestiary_by_type(monster_type)
    else:
        monsters = catalog.bestiary_list()
    
    return monsters


@router.get("/{monster_id}", response_model=BestiaryResponse)
def get_monster(monster_id: int, db: Session = Depends(get_database)):
    """Получить монстра по ID"""
    catalog = CatalogService(db)
    monster = catalog.bestiary_detail(monster_id)
    
    if monster is None:
        raise HTTPException(status_code=404, detail="Монстр не найден")
    
    return monster


@router.post("/", response_model=BestiaryResponse)
def create_monster(
    monster: BestiaryCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_database)
):
    """Создать нового монстра"""
    content = ContentService(db)
    ok, message = content.add_monster(
        user=current_user,
        name=monster.name,
        level=monster.level,
        monster_type=monster.monster_type,
        description=monster.description,
        quirk=monster.quirk,
        xp_reward=monster.xp_reward,
        treasure_reward=monster.treasure_reward
    )
    
    if not ok:
        raise HTTPException(status_code=400, detail=message)
    
    # Получаем созданного монстра
    catalog = CatalogService(db)
    created_monster = catalog.bestiary_detail(int(message.split('id_bestiary=')[1].split(')')[0]))
    
    return created_monster


@router.put("/{monster_id}", response_model=BestiaryResponse)
def update_monster(
    monster_id: int,
    monster: BestiaryUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_database)
):
    """Обновить монстра"""
    content = ContentService(db)
    ok, message = content.update_monster(
        id_bestiary=monster_id,
        name=monster.name,
        level=monster.level,
        monster_type=monster.monster_type,
        description=monster.description,
        quirk=monster.quirk,
        xp_reward=monster.xp_reward,
        treasure_reward=monster.treasure_reward
    )
    
    if not ok:
        raise HTTPException(status_code=400, detail=message)
    
    catalog = CatalogService(db)
    updated_monster = catalog.bestiary_detail(monster_id)
    
    return updated_monster


@router.delete("/{monster_id}")
def delete_monster(
    monster_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_database)
):
    """Удалить монстра"""
    content = ContentService(db)
    ok, message = content.delete_monster(monster_id)
    
    if not ok:
        raise HTTPException(status_code=400, detail=message)
    
    return {"message": message}