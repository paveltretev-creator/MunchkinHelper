from typing import List, Optional

from repositories.base_repository import BaseRepository
from models.race import Race
from models.ability import Ability


class RaceRepository(BaseRepository):

    def get_all(self) -> List[Race]:
        with self.get_cursor() as cursor:
            cursor.execute("SELECT * FROM Races ORDER BY name")
            rows = cursor.fetchall()
        return [Race(id=r['id'], name=r['name']) for r in rows]

    def get_by_id(self, race_id: int) -> Optional[Race]:
        with self.get_cursor() as cursor:
            cursor.execute("SELECT * FROM Races WHERE id = %s", (race_id,))
            row = cursor.fetchone()
        return Race(id=row['id'], name=row['name']) if row else None

    def get_abilities_for_race(self, race_id: int) -> List[Ability]:
        """Получить все способности, принадлежащие конкретной расе."""
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT a.id, a.name, a.description
                FROM Race_Abilities ra
                JOIN Abilities a ON ra.ability_id = a.id
                WHERE ra.race_id = %s
                ORDER BY a.name
            """, (race_id,))
            rows = cursor.fetchall()
        return [Ability(id=r['id'], name=r['name'], description=r.get('description'))
                for r in rows]