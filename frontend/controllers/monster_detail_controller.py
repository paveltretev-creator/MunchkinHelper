"""
Контроллер детального описания монстра
"""


class MonsterDetailController:
    """Логика экрана детального описания монстра"""
    
    def __init__(self, screen):
        self.screen = screen
        self._monster_data = None
    
    def set_monster_data(self, monster_data):
        """Установить данные монстра для отображения"""
        self._monster_data = monster_data
        self.screen.update_monster_info(monster_data)
    
    def go_back(self):
        """Вернуться на экран списка бестиария"""
        self.screen.manager.current = 'bestiary'