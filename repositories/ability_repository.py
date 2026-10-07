from typing import List, Optional

from repositories.base_repository import BaseRepository
from models.ability import Ability


class AbilityRepository(BaseRepository):

    def get_all(self) -> List[Ability]:
        with self.get_cursor() as cursor:
            cursor.execute("SELECT * FROM Abilities ORDER BY name")
            rows = cursor.fetchall()
        return [Ability(id=r['id'], name=r['name'], description=r.get('description'))
                for r in rows]

    def get_by_id(self, ability_id: int) -> Optional[Ability]:
        with self.get_cursor() as cursor:
            cursor.execute("SELECT * FROM Abilities WHERE id = %s", (ability_id,))
            row = cursor.fetchone()
        return Ability(id=row['id'], name=row['name'], description=row.get('description')) if row else None