"""
Контроллер игры — бизнес-логика управления счетчиками
"""
from services.game_manager import GameManager


class GameController:
    """Логика экрана новой игры"""
    
    def __init__(self, screen):
        self.screen = screen
        self._game_manager = GameManager()
        self._level = 1
        self._strength = 0
        self._debuff = 0  # Дебаф всегда <= 0
    
    def load_saved_game(self):
        """Загрузить сохраненную игру"""
        game_data = self._game_manager.load_game()
        if game_data:
            self._level = game_data.get('level', 1)
            self._strength = game_data.get('strength', 0)
            self._debuff = game_data.get('debuff', 0)
            
            # Защита от некорректных данных
            if self._level < 1:
                self._level = 1
            if self._strength < 0:
                self._strength = 0
            if self._debuff > 0:
                self._debuff = 0
        
        self._update_display()
    
    def change_level(self, delta: int):
        """Изменить уровень (минимум 1)"""
        self._level += delta
        if self._level < 1:
            self._level = 1
        self._update_display()
        self._save_game()
    
    def change_strength(self, delta: int):
        """Изменить силу (не может быть отрицательной)"""
        self._strength += delta
        if self._strength < 0:
            self._strength = 0
        self._update_display()
        self._save_game()
    
    def change_debuff(self, delta: int):
        """Изменить дебаф (всегда <= 0, кнопка '+' делает более отрицательным)"""
        self._debuff += delta
        if self._debuff > 0:
            self._debuff = 0
        self._update_display()
        self._save_game()
    
    def _update_display(self):
        """Обновить отображение"""
        total = self._level + self._strength + self._debuff
        self.screen.update_display(self._level, self._strength, self._debuff, total)
    
    def _save_game(self):
        """Сохранить игру"""
        self._game_manager.save_game(self._level, self._strength, self._debuff)
    
    def open_catalog(self):
        """Открыть справочник (заглушка)"""
        print('Переход в справочник из игры')

    def clear_game(self):
        """Сбросить игру к начальным значениям"""
        self._level = 1
        self._strength = 0
        self._debuff = 0
        self._update_display()
        self._save_game()
        print('Игра очищена')

    def open_catalog(self):
        """Открыть справочник из экрана игры"""
        print('Переход в справочник из игры')
        catalog_screen = self.screen.manager.get_screen('catalog')
        catalog_screen.controller.set_previous_screen('game')
        self.screen.manager.current = 'catalog'