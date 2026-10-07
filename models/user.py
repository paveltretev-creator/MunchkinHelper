from dataclasses import dataclass, field
from typing import List, Optional

from .user_status import UserStatus
from .character import Character


@dataclass
class User:
    login: str
    age: int
    email: str
    status: UserStatus = UserStatus.CREATED
    id: Optional[int] = None
    characters: List[Character] = field(default_factory=list)