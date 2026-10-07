from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List

from services.user_service import UserService
from exceptions import AppException
from api.dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["characters"])


class CharacterIn(BaseModel):
    name: str
    race: str
    character_class: str


class RegisterRequest(BaseModel):
    """Часть 2: создание User + Characters в одной транзакции."""
    login: str
    age: int
    email: str
    characters: List[CharacterIn]


@router.post("/register-with-characters")
def register_with_characters(
    body: RegisterRequest,
    service: UserService = Depends(get_user_service)
):
    try:
        user = service.register_with_characters(
            login=body.login,
            age=body.age,
            email=body.email,
            characters_data=[ch.dict() for ch in body.characters]
        )
        return {"message": "Пользователь и персонажи созданы", "login": user.login}
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))