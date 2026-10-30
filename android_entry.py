"""
Точка входа для Android-сборки.
Активирует pg8000 и запускает приложение.
"""
import os
import sys


def setup_android():
    """Настройка окружения для Android"""
    # Включаем pg8000 вместо psycopg2
    os.environ['USE_PG8000'] = '1'
    
    # ВАЖНО: укажите адрес вашего PostgreSQL-сервера
    # Это может быть внешний IP, домен или сервис вроде Railway/Neon
    # Пример: postgresql+pg8000://user:password@host:5432/dbname
    if 'DATABASE_URL' not in os.environ:
        # Замените на реальные данные вашего сервера!
        os.environ['DATABASE_URL'] = (
            'postgresql+pg8000://postgres:password@YOUR_SERVER_IP:5432/postgres'
        )
    
    print(f'[Android] DATABASE_URL настроен')


if __name__ == '__main__':
    setup_android()
    
    # Добавляем корень проекта в PYTHONPATH
    root_dir = os.path.dirname(os.path.abspath(__file__))
    if root_dir not in sys.path:
        sys.path.insert(0, root_dir)
    
    # Добавляем backend в путь для импорта app.*
    backend_dir = os.path.join(root_dir, 'backend')
    if backend_dir not in sys.path:
        sys.path.insert(0, backend_dir)
    
    # Добавляем frontend в путь для импорта screens, controllers, services
    frontend_dir = os.path.join(root_dir, 'frontend')
    if frontend_dir not in sys.path:
        sys.path.insert(0, frontend_dir)
    
    # Запускаем Kivy-приложение
    from main import MunchkinApp
    MunchkinApp().run()