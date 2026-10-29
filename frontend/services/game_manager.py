"""
Менеджер игры — сохранение и загрузка состояния игры
"""
import json
from pathlib import Path
from typing import Optional, Dict


class GameManager:
    """Сохранение и загрузка состояния игры"""
    
    _DATA_DIR = Path.home() / '.munchkin'
    _GAME_FILE = _DATA_DIR / 'game_state.json'
    
    def __init__(self):
        self._DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    def save_game(self, level: int, strength: int, debuff: int) -> None:
        """Сохранить состояние игры"""
        data = {
            'level': level,
            'strength': strength,
            'debuff': debuff,
        }
        with open(self._GAME_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_game(self) -> Optional[Dict[str, int]]:
        """Загрузить состояние игры. None если файла нет"""
        if not self._GAME_FILE.exists():
            return None
        
        try:
            with open(self._GAME_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return None
    
    def has_game(self) -> bool:
        """Есть ли сохраненная игра"""
        return self._GAME_FILE.exists()
    
    def delete_game(self) -> None:
        """Удалить сохраненную игру"""
        if self._GAME_FILE.exists():
            self._GAME_FILE.unlink()