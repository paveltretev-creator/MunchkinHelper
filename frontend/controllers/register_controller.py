"""
Контроллер регистрации — бизнес-логика создания пользователя
"""
from app.database import SessionLocal
from app.services.auth_service import AuthService


class RegisterController:
    """Логика регистрации пользователя"""
    
    def __init__(self, screen):
        self.screen = screen
    
    def try_register(self, login: str, password: str, password_confirm: str):
        """Попытка регистрации"""
        if not login:
            self.screen.show_message('Введите логин')
            return
        if not password:
            self.screen.show_message('Введите пароль')
            return
        if password != password_confirm:
            self.screen.show_message('Пароли не совпадают')
            return
        
        db = SessionLocal()
        try:
            auth = AuthService(db)
            ok, message = auth.register(login, password, password_confirm)
            
            # ok=True — успех, ok=False — ошибка валидации от сервиса
            self.screen.show_message(message, is_error=not ok)
        except Exception as e:
            self.screen.show_message('Ошибка подключения')
            print(f'Ошибка регистрации: {e}')
        finally:
            db.close()