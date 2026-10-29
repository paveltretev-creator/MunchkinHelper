"""
Контроллер авторизации — бизнес-логика входа в систему
"""
from app.database import SessionLocal
from app.services.auth_service import AuthService
from services.session_manager import SessionManager


class AuthController:
    def __init__(self, screen):
        self.screen = screen
        self._session_manager = SessionManager()
    
    @property
    def has_saved_session(self) -> bool:
        return self._session_manager.has_saved_credentials
    
    def try_login(self, login: str, password: str, remember: bool = False):
        print(f'[AuthController] try_login: login={login}, remember={remember}')
        
        if not login:
            self.screen.show_error('Введите логин')
            return
        if not password:
            self.screen.show_error('Введите пароль')
            return
        
        db = SessionLocal()
        try:
            auth = AuthService(db)
            user, message = auth.authenticate(login, password)
            
            if user is not None:
                print(f'[AuthController] Авторизация успешна: {user.login}')
                try:
                    if remember:
                        self._session_manager.save_credentials(login, password)
                    else:
                        self._session_manager.clear_credentials()
                except Exception as e:
                    print(f'[AuthController] Ошибка сохранения сессии: {e}')
                    # Не блокируем вход из-за ошибки сохранения
                
                self.screen.navigate_to_main(user.login)
            else:
                print(f'[AuthController] Авторизация не удалась: {message}')
                self.screen.show_error(message)
        except Exception as e:
            self.screen.show_error('Ошибка подключения')
            print(f'Ошибка авторизации: {e}')
        finally:
            db.close()
    
    def try_auto_login(self) -> bool:
        print('[AuthController] Попытка авто-входа...')
        
        creds = self._session_manager.load_credentials()
        if creds is None:
            print('[AuthController] Сохранённые данные не найдены')
            return False
        
        login = creds.get('login', '')
        password = creds.get('password', '')
        
        if not login or not password:
            print('[AuthController] Данные повреждены, очистка')
            self._session_manager.clear_credentials()
            return False
        
        db = SessionLocal()
        try:
            auth = AuthService(db)
            user, message = auth.authenticate(login, password)
            
            if user is not None:
                print(f'[AuthController] Авто-вход успешен: {user.login}')
                self.screen.navigate_to_main(user.login)
                return True
            else:
                print(f'[AuthController] Авто-вход не удался: {message}')
                self._session_manager.clear_credentials()
                self.screen.show_error('Сохранённые данные недействительны. Войдите заново.')
                return False
        except Exception as e:
            print(f'Ошибка авто-входа: {e}')
            self.screen.show_error('Ошибка подключения')
            return False
        finally:
            db.close()
    
    def clear_saved_session(self):
        self._session_manager.clear_credentials()