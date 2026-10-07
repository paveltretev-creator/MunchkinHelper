from typing import List, Optional

from repositories.base_repository import BaseRepository
from models.monster import Monster


class MonsterRepository(BaseRepository):

    def get_all(self) -> List[Monster]:
        with self.get_cursor() as cursor:
            cursor.execute("SELECT * FROM Bestiary ORDER BY level, name")
            rows = cursor.fetchall()
        return [self._to_model(r) for r in rows]

    def get_by_id(self, monster_id: int) -> Optional[Monster]:
        with self.get_cursor() as cursor:
            cursor.execute("SELECT * FROM Bestiary WHERE id = %s", (monster_id,))
            row = cursor.fetchone()
        return self._to_model(row) if row else None

    def search(self, search_term: str) -> List[Monster]:
        with self.get_cursor() as cursor:
            cursor.execute(
                "SELECT * FROM Bestiary WHERE name ILIKE %s ORDER BY level, name",
                (f'%{search_term}%',)
            )
            rows = cursor.fetchall()
        return [self._to_model(r) for r in rows]

    @staticmethod
    def _to_model(row) -> Monster:
        return Monster(
            id=row['id'],
            name=row['name'],
            level=row['level'],
            description=row.get('description')
        )