"""
Скрипт для автоматической генерации документации Sphinx.
Запуск: python generate_docs.py (из любой папки проекта)
"""
import os
import sys
import subprocess
from pathlib import Path


def get_docs_dir():
    """Получить абсолютный путь к папке docs/"""
    return Path(__file__).parent.resolve()


def check_requirements():
    """Проверка установленных зависимостей"""
    required = ['sphinx', 'sphinx_rtd_theme', 'sphinx_autodoc_typehints']
    missing = []
    
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"Отсутствуют зависимости: {', '.join(missing)}")
        print("Установите: pip install -r requirements.txt (в папке docs/)")
        return False
    return True


def clean_build(docs_dir: Path):
    """Очистка предыдущей сборки"""
    build_dir = docs_dir / '_build'
    if build_dir.exists():
        import shutil
        shutil.rmtree(build_dir)
        print("Очищена папка _build/")


def generate_html(docs_dir: Path) -> bool:
    """Генерация HTML документации"""
    print("Генерация HTML документации...")
    print(f"Рабочая папка: {docs_dir}")
    
    # Проверяем наличие conf.py
    conf_path = docs_dir / 'conf.py'
    if not conf_path.exists():
        print(f"✗ Файл conf.py не найден: {conf_path}")
        return False
    
    # Запускаем Sphinx из папки docs/
    result = subprocess.run(
        [
            sys.executable, '-m', 'sphinx',
            '-b', 'html',           # формат вывода
            '-c', str(docs_dir),     # путь к conf.py
            str(docs_dir),           # путь к исходникам
            str(docs_dir / '_build' / 'html')  # путь к выводу
        ],
        capture_output=True,
        text=True,
        cwd=str(docs_dir)  # рабочая директория
    )
    
    if result.returncode == 0:
        print("✓ Документация успешно сгенерирована")
        output = docs_dir / '_build' / 'html' / 'index.html'
        print(f"  Откройте: {output}")
    else:
        print("✗ Ошибка генерации:")
        print(result.stdout)
        print(result.stderr)
    
    return result.returncode == 0


def main():
    print("=" * 60)
    print("Генератор документации Munchkin Helper")
    print("=" * 60)
    
    docs_dir = get_docs_dir()
    print(f"Папка документации: {docs_dir}")
    
    if not check_requirements():
        sys.exit(1)
    
    clean_build(docs_dir)
    
    if generate_html(docs_dir):
        print("\nГотово!")
    else:
        print("\nНе удалось сгенерировать документацию.")
        sys.exit(1)


if __name__ == '__main__':
    main()