"""
Менеджер игры для бэкенда API
"""
import json
from pathlib import Path
from typing import Optional, Dict


class GameManager:
    _DATA_DIR = Path.home() / '.munchkin_api'
    _GAME_FILE = _DATA_DIR / 'game_state.json'
    
    def __init__(self):
        self._DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    def save_game(self, level: int, strength: int, debuff: int) -> None:
        data = {'level': level, 'strength': strength, 'debuff': debuff}
        with open(self._GAME_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_game(self) -> Optional[Dict[str, int]]:
        if not self._GAME_FILE.exists():
            return None
        try:
            with open(self._GAME_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return None
    
    def delete_game(self) -> None:
        if self._GAME_FILE.exists():
            self._GAME_FILE.unlink()