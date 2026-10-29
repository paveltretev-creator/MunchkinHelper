from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class UserAddition(Base):
    __tablename__ = "user_additions"
    
    id_addition: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id_user", ondelete="CASCADE"), index=True)
    target_entity_id: Mapped[int]
    target_entity_type: Mapped[str] = mapped_column(String(50))  # 'race' | 'class' | 'monster' | 'dungeon'