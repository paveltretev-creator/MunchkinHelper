"""
Экран авторизации — только UI-логика
"""
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):
    """Экран авторизации"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = None
        self._auto_login_attempted = False
    
    def on_enter(self):
        print('[LoginScreen] on_enter вызван')
        
        self.ids.login_input.text = ''
        self.ids.password_input.text = ''
        self.ids.message_label.text = ''
        self.ids.remember_checkbox.active = False
        
        if self.controller is None:
            return
        
        try:
            has_session = self.controller.has_saved_session
            if has_session:
                Clock.schedule_once(self._try_auto_login, 0)
        except Exception as e:
            print(f'[LoginScreen] Ошибка в on_enter: {e}')
    
    def _try_auto_login(self, dt):
        self._auto_login_attempted = True
        
        if 'main' not in self.manager.screen_names:
            Clock.schedule_once(self._try_auto_login, 0.1)
            return
        
        try:
            self.controller.try_auto_login()
        except Exception as e:
            print(f'[LoginScreen] Ошибка авто-входа: {e}')
    
    def on_login_button(self):
        """Обработчик кнопки авторизации"""
        login = self.ids.login_input.text.strip()
        password = self.ids.password_input.text
        remember = self.ids.remember_checkbox.active
        
        if self.controller:
            self.controller.try_login(login, password, remember)
    
    def on_register_click(self):
        """Обработчик клика на Зарегистрироваться"""
        print('[LoginScreen] on_register_click вызван')
        
        if 'register' in self.manager.screen_names:
            self.manager.current = 'register'
        else:
            print('[LoginScreen] Экран register не найден в ScreenManager')
    
    def on_forget_me(self):
        if self.controller:
            self.controller.clear_saved_session()
            self.ids.message_label.text = 'Сохранённые данные удалены'
    
    def show_error(self, message: str):
        self.ids.message_label.text = message
    
    def navigate_to_main(self, user_login: str):
        if 'main' not in self.manager.screen_names:
            Clock.schedule_once(lambda dt: self.navigate_to_main(user_login), 0.1)
            return
        
        main_screen = self.manager.get_screen('main')
        main_screen.set_user(user_login)
        self.manager.current = 'main'