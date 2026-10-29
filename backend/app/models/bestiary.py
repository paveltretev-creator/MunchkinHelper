from typing import Optional

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Bestiary(Base):
    """Единая таблица бестиария"""
    __tablename__ = "bestiary"
    
    id_bestiary: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    level: Mapped[int]
    description: Mapped[Optional[str]] = mapped_column(Text)
    quirk: Mapped[Optional[str]] = mapped_column(Text)
    xp_reward: Mapped[int]
    treasure_reward: Mapped[int]
    monster_type: Mapped[str] = mapped_column(String(50))  # 'normal' | 'undead' | 'dragon'
    
    def __repr__(self):
        return f"<Bestiary(id_bestiary={self.id_bestiary}, name={self.name}, type={self.monster_type})>"