from typing import Optional, Tuple

from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories import (
    BestiaryRepository,
    CharacterClassRepository,
    DungeonRepository,
    RaceRepository,
    UserAdditionRepository,
)

VALID_MONSTER_TYPES = ("normal", "undead", "dragon")
MAX_NAME_LENGTH = 255


class ContentService:
    """Слой бизнес-логики: добавление, изменение и удаление данных"""
    
    def __init__(self, db: Session):
        self._bestiary = BestiaryRepository(db)
        self._races = RaceRepository(db)
        self._classes = CharacterClassRepository(db)
        self._dungeons = DungeonRepository(db)
        self._additions = UserAdditionRepository(db)
    
    # ==================== ДОБАВЛЕНИЕ ====================
    
    def add_monster(
        self,
        user: User,
        name: str,
        level: int,
        monster_type: str,
        description: Optional[str],
        quirk: Optional[str],
        xp_reward: int,
        treasure_reward: int,
    ) -> Tuple[bool, str]:
        error = self._validate_name(name)
        if error:
            return False, error
        if monster_type not in VALID_MONSTER_TYPES:
            return False, f"Недопустимый тип монстра: '{monster_type}'."
        
        monster = self._bestiary.create({
            "name": name,
            "level": level,
            "description": description,
            "quirk": quirk,
            "xp_reward": xp_reward,
            "treasure_reward": treasure_reward,
            "monster_type": monster_type,
        })
        self._register_addition(user, monster.id_bestiary, "monster")
        return True, f"Монстр '{monster.name}' добавлен (id_bestiary={monster.id_bestiary})."
    
    def add_race(
        self,
        user: User,
        name: str,
        ability_1: Optional[str],
        ability_2: Optional[str],
        epic_ability_1: Optional[str],
        epic_ability_2: Optional[str],
    ) -> Tuple[bool, str]:
        error = self._validate_name(name)
        if error:
            return False, error
        
        race = self._races.create({
            "name": name,
            "ability_1": ability_1,
            "ability_2": ability_2,
            "epic_ability_1": epic_ability_1,
            "epic_ability_2": epic_ability_2,
        })
        self._register_addition(user, race.id_race, "race")
        return True, f"Раса '{race.name}' добавлена (id_race={race.id_race})."
    
    def add_class(
        self,
        user: User,
        name: str,
        ability_1: Optional[str],
        ability_2: Optional[str],
        epic_ability_1: Optional[str],
        epic_ability_2: Optional[str],
    ) -> Tuple[bool, str]:
        error = self._validate_name(name)
        if error:
            return False, error
        
        char_class = self._classes.create({
            "name": name,
            "ability_1": ability_1,
            "ability_2": ability_2,
            "epic_ability_1": epic_ability_1,
            "epic_ability_2": epic_ability_2,
        })
        self._register_addition(user, char_class.id_class, "class")
        return True, f"Класс '{char_class.name}' добавлен (id_class={char_class.id_class})."
    
    def add_dungeon(self, user: User, name: str, description: Optional[str]) -> Tuple[bool, str]:
        error = self._validate_name(name)
        if error:
            return False, error
        
        dungeon = self._dungeons.create({
            "name": name,
            "description": description,
        })
        self._register_addition(user, dungeon.id_dungeon, "dungeon")
        return True, f"Подземелье '{dungeon.name}' добавлено (id_dungeon={dungeon.id_dungeon})."
    
    # ==================== ИЗМЕНЕНИЕ ====================
    
    def update_monster(
        self,
        id_bestiary: int,
        name: str,
        level: int,
        monster_type: str,
        description: Optional[str],
        quirk: Optional[str],
        xp_reward: int,
        treasure_reward: int,
    ) -> Tuple[bool, str]:
        if self._bestiary.get(id_bestiary) is None:
            return False, "Запись не найдена."
        error = self._validate_name(name)
        if error:
            return False, error
        if monster_type not in VALID_MONSTER_TYPES:
            return False, f"Недопустимый тип монстра: '{monster_type}'."
        
        self._bestiary.update(id_bestiary, {
            "name": name,
            "level": level,
            "monster_type": monster_type,
            "description": description,
            "quirk": quirk,
            "xp_reward": xp_reward,
            "treasure_reward": treasure_reward,
        })
        return True, f"Монстр '{name}' (id_bestiary={id_bestiary}) обновлён."
    
    def update_race(
        self,
        id_race: int,
        name: str,
        ability_1: Optional[str],
        ability_2: Optional[str],
        epic_ability_1: Optional[str],
        epic_ability_2: Optional[str],
    ) -> Tuple[bool, str]:
        if self._races.get(id_race) is None:
            return False, "Запись не найдена."
        error = self._validate_name(name)
        if error:
            return False, error
        
        self._races.update(id_race, {
            "name": name,
            "ability_1": ability_1,
            "ability_2": ability_2,
            "epic_ability_1": epic_ability_1,
            "epic_ability_2": epic_ability_2,
        })
        return True, f"Раса '{name}' (id_race={id_race}) обновлена."
    
    def update_class(
        self,
        id_class: int,
        name: str,
        ability_1: Optional[str],
        ability_2: Optional[str],
        epic_ability_1: Optional[str],
        epic_ability_2: Optional[str],
    ) -> Tuple[bool, str]:
        if self._classes.get(id_class) is None:
            return False, "Запись не найдена."
        error = self._validate_name(name)
        if error:
            return False, error
        
        self._classes.update(id_class, {
            "name": name,
            "ability_1": ability_1,
            "ability_2": ability_2,
            "epic_ability_1": epic_ability_1,
            "epic_ability_2": epic_ability_2,
        })
        return True, f"Класс '{name}' (id_class={id_class}) обновлён."
    
    def update_dungeon(self, id_dungeon: int, name: str, description: Optional[str]) -> Tuple[bool, str]:
        if self._dungeons.get(id_dungeon) is None:
            return False, "Запись не найдена."
        error = self._validate_name(name)
        if error:
            return False, error
        
        self._dungeons.update(id_dungeon, {
            "name": name,
            "description": description,
        })
        return True, f"Подземелье '{name}' (id_dungeon={id_dungeon}) обновлено."
    
    # ==================== УДАЛЕНИЕ ====================
    
    def delete_monster(self, id_bestiary: int) -> Tuple[bool, str]:
        monster = self._bestiary.get(id_bestiary)
        if monster is None:
            return False, "Запись не найдена."
        self._remove_addition_link("monster", id_bestiary)
        self._bestiary.delete(id_bestiary)
        return True, f"Монстр '{monster.name}' удалён."
    
    def delete_race(self, id_race: int) -> Tuple[bool, str]:
        race = self._races.get(id_race)
        if race is None:
            return False, "Запись не найдена."
        self._remove_addition_link("race", id_race)
        self._races.delete(id_race)
        return True, f"Раса '{race.name}' удалена."
    
    def delete_class(self, id_class: int) -> Tuple[bool, str]:
        char_class = self._classes.get(id_class)
        if char_class is None:
            return False, "Запись не найдена."
        self._remove_addition_link("class", id_class)
        self._classes.delete(id_class)
        return True, f"Класс '{char_class.name}' удалён."
    
    def delete_dungeon(self, id_dungeon: int) -> Tuple[bool, str]:
        dungeon = self._dungeons.get(id_dungeon)
        if dungeon is None:
            return False, "Запись не найдена."
        self._remove_addition_link("dungeon", id_dungeon)
        self._dungeons.delete(id_dungeon)
        return True, f"Подземелье '{dungeon.name}' удалено."
    
    # ==================== ВНУТРЕННЕЕ ====================
    
    def _register_addition(self, user: User, target_id: int, target_type: str) -> None:
        """Зафиксировать добавление в таблице user_additions"""
        self._additions.create({
            "id_user": user.id_user,
            "target_entity_id": target_id,
            "target_entity_type": target_type,
        })
    
    def _remove_addition_link(self, target_type: str, target_id: int) -> None:
        """Удалить связь из user_additions, чтобы не оставалось сирот"""
        addition = self._additions.get_by_target(target_type, target_id)
        if addition is not None:
            self._additions.delete(addition.id_addition)
    
    @staticmethod
    def _validate_name(name: str) -> Optional[str]:
        if not name or not name.strip():
            return "Название не может быть пустым."
        if len(name) > MAX_NAME_LENGTH:
            return f"Название слишком длинное: максимум {MAX_NAME_LENGTH} символов."
        return None