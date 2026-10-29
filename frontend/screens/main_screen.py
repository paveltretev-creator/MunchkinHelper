"""
Главный экран — только UI-логика
"""
from kivy.uix.screenmanager import Screen


class MainScreen(Screen):
    """Главный экран авторизованного пользователя"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None  # MainController
        self.controller_session = None  # AuthController (для очистки сессии)
        self._current_user = ''
    
    def set_user(self, login: str):
        self._current_user = login
        self.ids.user_label.text = f'Игрок: {login}'
    
    def on_logout(self):
        if self.controller:
            # При выходе спрашиваем, удалять ли сохранённые данные
            # Для простоты — всегда очищаем сессию при выходе
            self.controller.logout(clear_session=True)
    
    def on_catalog(self):
        if self.controller:
            self.controller.open_catalog()
    
    def on_new_game(self):
        if self.controller:
            self.controller.start_new_game()