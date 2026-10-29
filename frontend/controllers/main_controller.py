"""
Контроллер главного экрана — бизнес-логика навигации
"""


class MainController:
    def __init__(self, screen):
        self.screen = screen
    
    def logout(self, clear_session: bool = False):
        print(f'Выход пользователя: {self.screen._current_user}')
        
        if clear_session and self.screen.controller_session:
            self.screen.controller_session.clear_saved_session()
        
        self.screen.manager.current = 'login'
    
    def open_catalog(self):
        """Переход в справочник с главного экрана"""
        print(f'Открытие справочника для пользователя: {self.screen._current_user}')
        catalog_screen = self.screen.manager.get_screen('catalog')
        catalog_screen.controller.set_previous_screen('main')
        self.screen.manager.current = 'catalog'
    
    def start_new_game(self):
        """Переход на экран новой игры"""
        print(f'Переход в новую игру для пользователя: {self.screen._current_user}')
        self.screen.manager.current = 'game'