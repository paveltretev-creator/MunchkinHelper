"""
Менеджер сессий — сохранение и загрузка учётных данных
"""
import json
import os
from pathlib import Path
from typing import Optional, Dict

from cryptography.fernet import Fernet, InvalidToken


class SessionManager:
    _DATA_DIR = Path.home() / '.munchkin'
    _KEY_FILE = _DATA_DIR / 'key.key'
    _CREDS_FILE = _DATA_DIR / 'credentials.enc'
    
    def __init__(self):
        print(f'[SessionManager] Папка данных: {self._DATA_DIR}')
        print(f'[SessionManager] Файл ключа: {self._KEY_FILE}')
        print(f'[SessionManager] Файл учётных данных: {self._CREDS_FILE}')
        self._fernet = self._load_or_create_key()
    
    def _load_or_create_key(self) -> Fernet:
        self._DATA_DIR.mkdir(parents=True, exist_ok=True)
        
        if self._KEY_FILE.exists():
            key = self._KEY_FILE.read_bytes()
            print('[SessionManager] Ключ загружен из файла')
        else:
            key = Fernet.generate_key()
            self._KEY_FILE.write_bytes(key)
            try:
                os.chmod(self._KEY_FILE, 0o600)
            except OSError:
                pass
            print('[SessionManager] Создан новый ключ')
        
        return Fernet(key)
    
    def save_credentials(self, login: str, password: str) -> None:
        print(f'[SessionManager] Сохранение учётных данных для: {login}')
        try:
            data = {'login': login, 'password': password}
            plaintext = json.dumps(data, ensure_ascii=False).encode('utf-8')
            encrypted = self._fernet.encrypt(plaintext)
            self._CREDS_FILE.write_bytes(encrypted)
            try:
                os.chmod(self._CREDS_FILE, 0o600)
            except OSError:
                pass
            print(f'[SessionManager] Данные сохранены в {self._CREDS_FILE}')
            print(f'[SessionManager] Файл существует: {self._CREDS_FILE.exists()}')
        except Exception as e:
            print(f'[SessionManager] Ошибка сохранения: {e}')
            raise
    
    def load_credentials(self) -> Optional[Dict[str, str]]:
        print(f'[SessionManager] Загрузка учётных данных...')
        print(f'[SessionManager] Файл существует: {self._CREDS_FILE.exists()}')
        
        if not self._CREDS_FILE.exists():
            print('[SessionManager] Файл не найден')
            return None
        
        try:
            encrypted = self._CREDS_FILE.read_bytes()
            print(f'[SessionManager] Прочитано байт: {len(encrypted)}')
            plaintext = self._fernet.decrypt(encrypted)
            creds = json.loads(plaintext.decode('utf-8'))
            print(f'[SessionManager] Данные расшифрованы: login={creds.get("login")}')
            return creds
        except (InvalidToken, json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f'[SessionManager] Ошибка расшифровки: {e}')
            self.clear_credentials()
            return None
    
    def clear_credentials(self) -> None:
        if self._CREDS_FILE.exists():
            self._CREDS_FILE.unlink()
            print('[SessionManager] Данные удалены')
    
    @property
    def has_saved_credentials(self) -> bool:
        result = self._CREDS_FILE.exists()
        print(f'[SessionManager] has_saved_credentials = {result}')
        return result