from typing import Optional

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Race(Base):
    __tablename__ = "races"
    
    id_race: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    ability_1: Mapped[Optional[str]] = mapped_column(Text)
    ability_2: Mapped[Optional[str]] = mapped_column(Text)
    epic_ability_1: Mapped[Optional[str]] = mapped_column(Text)
    epic_ability_2: Mapped[Optional[str]] = mapped_column(Text)