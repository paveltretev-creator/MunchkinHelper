"""
Экран регистрации — только UI-логика
"""
from kivy.uix.screenmanager import Screen


class RegisterScreen(Screen):
    """Экран регистрации нового пользователя"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None
    
    def on_enter(self):
        """Очистка полей при входе на экран"""
        self.ids.login_input.text = ''
        self.ids.password_input.text = ''
        self.ids.password_confirm_input.text = ''
        self.ids.message_label.text = ''
        self.ids.message_label.color = (0.55, 0.0, 0.0, 1)  # Красный по умолчанию
    
    def on_back(self):
        """Вернуться на экран авторизации"""
        self.manager.current = 'login'
    
    def on_register_button(self):
        """Обработчик кнопки регистрации"""
        login = self.ids.login_input.text.strip()
        password = self.ids.password_input.text
        password_confirm = self.ids.password_confirm_input.text
        
        if self.controller:
            self.controller.try_register(login, password, password_confirm)
    
    def show_message(self, text: str, is_error: bool = True):
        """Показать сообщение (красное для ошибок, зеленое для успеха)"""
        self.ids.message_label.text = text
        if is_error:
            self.ids.message_label.color = (0.55, 0.0, 0.0, 1)  # Темно-красный
        else:
            self.ids.message_label.color = (0.0, 0.55, 0.0, 1)  # Темно-зеленый