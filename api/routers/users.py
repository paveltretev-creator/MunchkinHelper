from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List

from services.user_service import UserService
from models.user_status import UserStatus
from exceptions import AppException
from api.dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["users"])


# ---------- Схемы ----------

class StatusChangeRequest(BaseModel):
    new_status: UserStatus


class UserOut(BaseModel):
    login: str
    age: int
    email: str
    status: UserStatus

    class Config:
        use_enum_values = True


# ---------- Эндпоинты ----------

@router.get("/", response_model=List[UserOut])
def get_all_users(service: UserService = Depends(get_user_service)):
    return service.get_all_users()


@router.get("/{login}", response_model=UserOut)
def get_user(login: str, service: UserService = Depends(get_user_service)):
    try:
        return service.get_user(login)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.patch("/{login}/status", response_model=UserOut)
def change_status(
    login: str,
    body: StatusChangeRequest,
    service: UserService = Depends(get_user_service)
):
    """Часть 1: смена статуса с валидацией переходов."""
    try:
        return service.change_status(login, body.new_status)
    except AppException as e:
        # Критерий 4: ошибка 409 возвращается корректно
        raise HTTPException(status_code=e.status_code, detail=e.detail)