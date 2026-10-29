"""
Роутер рас
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_database, get_current_user
from api.schemas.race import RaceCreate, RaceUpdate, RaceResponse
from app.models.user import User
from app.services.catalog_service import CatalogService
from app.services.content_service import ContentService

router = APIRouter(prefix="/races", tags=["Расы"])


@router.get("/", response_model=List[RaceResponse])
def get_all_races(db: Session = Depends(get_database)):
    """Получить список всех рас"""
    catalog = CatalogService(db)
    return catalog.races_list()


@router.get("/{race_id}", response_model=RaceResponse)
def get_race(race_id: int, db: Session = Depends(get_database)):
    """Получить расу по ID"""
    catalog = CatalogService(db)
    race = catalog.race_detail(race_id)
    
    if race is None:
        raise HTTPException(status_code=404, detail="Раса не найдена")
    
    return race


@router.post("/", response_model=RaceResponse)
def create_race(
    race: RaceCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_database)
):
    """Создать новую расу"""
    content = ContentService(db)
    ok, message = content.add_race(
        user=current_user,
        name=race.name,
        ability_1=race.ability_1,
        ability_2=race.ability_2,
        epic_ability_1=race.epic_ability_1,
        epic_ability_2=race.epic_ability_2
    )
    
    if not ok:
        raise HTTPException(status_code=400, detail=message)
    
    catalog = CatalogService(db)
    created_race = catalog.race_detail(int(message.split('id_race=')[1].split(')')[0]))
    
    return created_race


@router.put("/{race_id}", response_model=RaceResponse)
def update_race(
    race_id: int,
    race: RaceUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_database)
):
    """Обновить расу"""
    content = ContentService(db)
    ok, message = content.update_race(
        id_race=race_id,
        name=race.name,
        ability_1=race.ability_1,
        ability_2=race.ability_2,
        epic_ability_1=race.epic_ability_1,
        epic_ability_2=race.epic_ability_2
    )
    
    if not ok:
        raise HTTPException(status_code=400, detail=message)
    
    catalog = CatalogService(db)
    updated_race = catalog.race_detail(race_id)
    
    return updated_race


@router.delete("/{race_id}")
def delete_race(
    race_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_database)
):
    """Удалить расу"""
    content = ContentService(db)
    ok, message = content.delete_race(race_id)
    
    if not ok:
        raise HTTPException(status_code=400, detail=message)
    
    return {"message": message}