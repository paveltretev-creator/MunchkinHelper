from dataclasses import dataclass
from typing import Optional


@dataclass
class Monster:
    id: int
    name: str
    level: int
    description: Optional[str] = None