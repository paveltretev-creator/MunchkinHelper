from enum import Enum


class UserStatus(str, Enum):
    CREATED = "CREATED"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"


# Матрица разрешённых переходов (Часть 1 — критерий 2, 3)
ALLOWED_TRANSITIONS = {
    UserStatus.CREATED:  {UserStatus.ACTIVE},
    UserStatus.ACTIVE:   {UserStatus.INACTIVE, UserStatus.DELETED},
    UserStatus.INACTIVE: {UserStatus.ACTIVE},
    UserStatus.DELETED:  set(),  # из DELETED никуда нельзя
}