from dataclasses import dataclass
from typing import Optional


@dataclass
class Character:
    name: str
    race: str
    character_class: str
    user_login: str          # внешний ключ → User
    id: Optional[int] = None