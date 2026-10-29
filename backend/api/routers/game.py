"""
Роутер игровых данных
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_database, get_current_user
from api.schemas.game import GameStateCreate, GameStateResponse
from app.models.user import User
from app.services.game_manager import GameManager

router = APIRouter(prefix="/game", tags=["Игровые данные"])


@router.get("/state", response_model=GameStateResponse)
def get_game_state(current_user: User = Depends(get_current_user)):
    """Получить текущее игровое состояние"""
    game_manager = GameManager()
    game_data = game_manager.load_game()
    
    if game_data is None:
        # Возвращаем значения по умолчанию
        return GameStateResponse(level=1, strength=0, debuff=0, total=1)
    
    total = game_data['level'] + game_data['strength'] + game_data['debuff']
    
    return GameStateResponse(
        level=game_data['level'],
        strength=game_data['strength'],
        debuff=game_data['debuff'],
        total=total
    )


@router.post("/state", response_model=GameStateResponse)
def update_game_state(
    game_state: GameStateCreate,
    current_user: User = Depends(get_current_user)
):
    """Обновить игровое состояние"""
    game_manager = GameManager()
    game_manager.save_game(
        level=game_state.level,
        strength=game_state.strength,
        debuff=game_state.debuff
    )
    
    total = game_state.level + game_state.strength + game_state.debuff
    
    return GameStateResponse(
        level=game_state.level,
        strength=game_state.strength,
        debuff=game_state.debuff,
        total=total
    )


@router.delete("/state")
def clear_game_state(current_user: User = Depends(get_current_user)):
    """Очистить игровое состояние"""
    game_manager = GameManager()
    game_manager.delete_game()
    
    return {"message": "Игровое состояние очищено"}