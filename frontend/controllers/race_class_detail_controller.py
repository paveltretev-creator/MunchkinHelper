"""
Контроллер детального описания расы или класса
"""


class RaceClassDetailController:
    """Логика экрана детального описания"""
    
    def __init__(self, screen):
        self.screen = screen
        self._item_data = None
    
    def set_item_data(self, item_data):
        """Установить данные для отображения"""
        self._item_data = item_data
        self.screen.update_info(item_data)
    
    def go_back(self):
        """Вернуться на экран списка"""
        self.screen.manager.current = 'races_classes'