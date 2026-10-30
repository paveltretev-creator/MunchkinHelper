"""
Экран новой игры — только UI-логика
"""
from kivy.uix.screenmanager import Screen


class GameScreen(Screen):
    """Экран новой игры"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None
    
    def on_enter(self):
        """При входе на экран — загрузить сохраненные данные"""
        if self.controller:
            self.controller.load_saved_game()

    # =========== #
    def on_level_up(self):
        if self.controller:
            self.controller.change_level(1)
    
    def on_level_down(self):
        if self.controller:
            self.controller.change_level(-1)
    
    def on_strength_up(self):
        if self.controller:
            self.controller.change_strength(1)
    
    def on_strength_down(self):
        if self.controller:
            self.controller.change_strength(-1)
    # =========== #
    
    def on_debuff_up(self):
        # Дебаф увеличивается в минус (например, от -1 до -2)
        if self.controller:
            self.controller.change_debuff(-1)
    
    def on_debuff_down(self):
        # Дебаф уменьшается в минус (например, от -2 до -1)
        if self.controller:
            self.controller.change_debuff(1)
    
    def update_display(self, level: int, strength: int, debuff: int, total: int):
        """Обновить отображение счетчиков"""
        self.ids.level_value.text = str(level)
        self.ids.strength_value.text = str(strength)
        self.ids.debuff_value.text = str(debuff)
        self.ids.total_value.text = str(total)
    
    def on_back(self):
        """Вернуться на главный экран"""
        self.manager.current = 'main'
    
    def on_catalog(self):
        """Перейти в справочник"""
        if self.controller:
            self.controller.open_catalog()

    def on_clear(self):
        """Очистить данные игры"""
        if self.controller:
            self.controller.clear_game()