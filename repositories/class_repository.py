from typing import List, Optional

from repositories.base_repository import BaseRepository
from models.character_class import CharacterClass
from models.ability import Ability


class ClassRepository(BaseRepository):

    def get_all(self) -> List[CharacterClass]:
        with self.get_cursor() as cursor:
            cursor.execute("SELECT * FROM Classes ORDER BY name")
            rows = cursor.fetchall()
        return [CharacterClass(id=r['id'], name=r['name']) for r in rows]

    def get_by_id(self, class_id: int) -> Optional[CharacterClass]:
        with self.get_cursor() as cursor:
            cursor.execute("SELECT * FROM Classes WHERE id = %s", (class_id,))
            row = cursor.fetchone()
        return CharacterClass(id=row['id'], name=row['name']) if row else None

    def get_abilities_for_class(self, class_id: int) -> List[Ability]:
        """Получить все способности, принадлежащие конкретному классу."""
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT a.id, a.name, a.description
                FROM Class_Abilities ca
                JOIN Abilities a ON ca.ability_id = a.id
                WHERE ca.class_id = %s
                ORDER BY a.name
            """, (class_id,))
            rows = cursor.fetchall()
        return [Ability(id=r['id'], name=r['name'], description=r.get('description'))
                for r in rows]