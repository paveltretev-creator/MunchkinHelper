# README.md для Munchkin Helper

markdown
# Munchkin Helper

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green.svg)](https://fastapi.tiangolo.com/)
[![Kivy](https://img.shields.io/badge/Kivy-2.3.0-purple.svg)](https://kivy.org/)

Приложение-помощник для настольной игры **Манчкин**. Позволяет вести учёт игрового состояния, просматривать справочники (бестиарий, расы, классы, подземелья) и управлять пользовательскими данными через удобный графический интерфейс и REST API.

![Munchkin Helper Screenshot](docs/images/screenshot.png)

## Содержание

- [Возможности](#-возможности)
- [Структура проекта](#-структура-проекта)
- [Требования](#-требования)
- [Установка](#-установка)
- [Запуск](#-запуск)
- [API Documentation](#-api-documentation)
- [Использование](#-использование)
- [Технологии](#-технологии)
- [Документация](#-документация)
- [Лицензия](#-лицензия)
- [Авторы](#-авторы)

## Возможности

### Для пользователей
- ✅ Регистрация и авторизация с сохранением сессии
- ✅ Автоматический вход при повторном запуске
- ✅ Ведение игрового состояния (уровень, сила, дебаф)
- ✅ Автоматический расчёт общей силы
- ✅ Сохранение прогресса между сессиями

### Справочники
- **Бестиарий** — просмотр монстров с фильтрацией по типу (обычные, андеды, драконы)
- **Расы и классы** — информация о доступных расах и классах с их способностями
- **Поиск** — быстрый поиск по названию в справочниках
- **Детальные карточки** — полная информация о каждом элементе

### Управление данными
- Создание новых монстров, рас, классов, подземелий
- Редактирование существующих записей
- Удаление записей с подтверждением
- Все операции требуют авторизации

### API
- Полноценный REST API на FastAPI
- JWT-аутентификация для защищённых endpoints
- Валидация данных через Pydantic схемы
- Автоматическая документация Swagger/OpenAPI

## Структура проекта

```
MunchkinHelper/
├── backend/                    # Серверная часть
│   ├── api/                    # REST API (FastAPI)
│   │   ├── routers/            # Endpoints
│   │   ├── schemas/            # Pydantic схемы
│   │   ├── main.py             # Точка входа API
│   │   └── dependencies.py     # Зависимости
│   ├── app/                    # Бизнес-логика
│   │   ├── models/             # SQLAlchemy модели
│   │   ├── repositories/       # Слой доступа к данным
│   │   ├── services/           # Сервисы
│   │   ├── database.py         # Подключение к БД
│   │   └── config.py           # Конфигурация
│   ├── alembic/                # Миграции БД
│   ├── requirements.txt
│   └── run_api.py              # Запуск API
│
├── frontend/                   # Клиентское приложение
│   ├── screens/                # UI-экраны (Kivy)
│   ├── controllers/            # Бизнес-логика UI
│   ├── services/               # Локальные сервисы
│   ├── main.py                 # Точка входа
│   ├── main.kv                 # Разметка интерфейса
│   └── requirements.txt
│
├── docs/                       # Документация (Sphinx)
│   ├── backend/                # Документация бэкенда
│   ├── frontend/               # Документация фронтенда
│   ├── api/                    # Документация API
│   ├── conf.py                 # Конфигурация Sphinx
│   └── generate_docs.py        # Скрипт генерации
│
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt            # Общие зависимости
```

## Требования

- **Python** 3.11 или выше
- **PostgreSQL** 14 или выше
- **pip** (менеджер пакетов Python)

### Опционально
- **Git** (для клонирования репозитория)
- **pgAdmin** или другой инструмент для работы с PostgreSQL

## Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/ваш-username/MunchkinHelper.git
cd MunchkinHelper
```

### 2. Настройка базы данных

Создайте базу данных PostgreSQL:

```sql
CREATE DATABASE munchkin;
CREATE USER munchkin_user WITH PASSWORD 'ваш_пароль';
GRANT ALL PRIVILEGES ON DATABASE munchkin TO munchkin_user;
```

Настройте подключение в `backend/app/config.py`:

```python
DATABASE_URL = "postgresql://munchkin_user:ваш_пароль@localhost:5432/munchkin"
```

### 3. Установка зависимостей бэкенда

```bash
cd backend
pip install -r requirements.txt
```

### 4. Применение миграций базы данных

```bash
alembic upgrade head
```

### 5. Установка зависимостей фронтенда

```bash
cd ../frontend
pip install -r requirements.txt
```

### 6. Установка зависимостей для документации (опционально)

```bash
cd ../docs
pip install -r requirements.txt
```

## Запуск

### Запуск API сервера

```bash
cd backend
python run_api.py
```

API будет доступен по адресу: **http://localhost:8000**

Документация API (Swagger UI): **http://localhost:8000/docs**

Альтернативная документация (ReDoc): **http://localhost:8000/redoc**

### Запуск клиентского приложения

```bash
cd frontend
python main.py
```

Откроется окно приложения с экраном авторизации.

## API Documentation

### Базовый URL

```
http://localhost:8000
```

### Аутентификация

Для защищённых endpoints используйте Bearer токен:

```http
Authorization: Bearer <login_пользователя>
```

### Основные endpoints

#### Авторизация

| Метод | Endpoint | Описание | Авторизация |
|-------|----------|----------|-------------|
| POST | `/auth/login` | Вход в систему | Нет |
| POST | `/auth/register` | Регистрация | Нет |

#### Бестиарий

| Метод | Endpoint | Описание | Авторизация |
|-------|----------|----------|-------------|
| GET | `/bestiary/` | Список всех монстров | Нет |
| GET | `/bestiary/{id}` | Монстр по ID | Нет |
| POST | `/bestiary/` | Создать монстра | ✅ Да |
| PUT | `/bestiary/{id}` | Обновить монстра | ✅ Да |
| DELETE | `/bestiary/{id}` | Удалить монстра | ✅ Да |

#### Расы

| Метод | Endpoint | Описание | Авторизация |
|-------|----------|----------|-------------|
| GET | `/races/` | Список всех рас | Нет |
| GET | `/races/{id}` | Раса по ID | Нет |
| POST | `/races/` | Создать расу | ✅ Да |
| PUT | `/races/{id}` | Обновить расу | ✅ Да |
| DELETE | `/races/{id}` | Удалить расу | ✅ Да |

#### Классы

| Метод | Endpoint | Описание | Авторизация |
|-------|----------|----------|-------------|
| GET | `/classes/` | Список всех классов | Нет |
| GET | `/classes/{id}` | Класс по ID | Нет |
| POST | `/classes/` | Создать класс | ✅ Да |
| PUT | `/classes/{id}` | Обновить класс | ✅ Да |
| DELETE | `/classes/{id}` | Удалить класс | ✅ Да |

#### Подземелья

| Метод | Endpoint | Описание | Авторизация |
|-------|----------|----------|-------------|
| GET | `/dungeons/` | Список всех подземелий | Нет |
| GET | `/dungeons/{id}` | Подземелье по ID | Нет |
| POST | `/dungeons/` | Создать подземелье | ✅ Да |
| PUT | `/dungeons/{id}` | Обновить подземелье | ✅ Да |
| DELETE | `/dungeons/{id}` | Удалить подземелье | ✅ Да |

#### Игровые данные

| Метод | Endpoint | Описание | Авторизация |
|-------|----------|----------|-------------|
| GET | `/game/state` | Получить игровое состояние | ✅ Да |
| POST | `/game/state` | Обновить состояние | ✅ Да |
| DELETE | `/game/state` | Очистить состояние | ✅ Да |

### Примеры запросов

#### Регистрация

```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "login": "test_user",
    "password": "password123",
    "password_confirm": "password123"
  }'
```

#### Создание монстра

```bash
curl -X POST "http://localhost:8000/bestiary/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer test_user" \
  -d '{
    "name": "Гоблин",
    "level": 1,
    "monster_type": "normal",
    "description": "Обычный гоблин",
    "quirk": "Трусливый",
    "xp_reward": 1,
    "treasure_reward": 1
  }'
```

#### Получение списка монстров

```bash
curl -X GET "http://localhost:8000/bestiary/"
```

Полная интерактивная документация доступна по адресу: **http://localhost:8000/docs**

## Использование

### Первый запуск

1. Запустите API сервер: `python backend/run_api.py`
2. Запустите приложение: `python frontend/main.py`
3. Зарегистрируйте нового пользователя
4. Войдите в систему
5. Начните использовать приложение!

### Игровой экран

- **Уровень** — текущий уровень персонажа (минимум 1)
- **Сила** — бонусы к силе (не может быть отрицательным)
- **Дебаф силы** — штрафы к силе (всегда ≤ 0)
- **Общая сила** — автоматический расчёт: Уровень + Сила + Дебаф

Данные автоматически сохраняются и восстанавливаются при следующем запуске.

### Справочники

- Используйте поиск для быстрого нахождения нужного элемента
- Фильтруйте монстров по типу (обычные, андеды, драконы)
- Нажимайте на элементы для просмотра детальной информации

## Технологии

### Backend
- **FastAPI** — современный веб-фреймворк для создания API
- **SQLAlchemy 2.0** — ORM для работы с базой данных
- **Alembic** — система миграций базы данных
- **Pydantic** — валидация данных и настройки
- **PBKDF2** — хеширование паролей
- **PostgreSQL** — реляционная база данных

### Frontend
- **Kivy** — фреймворк для создания кроссплатформенных GUI
- **cryptography** — шифрование данных (Fernet)
- **JSON** — хранение локальных данных

### Инструменты
- **Sphinx** — генератор документации
- **pytest** — тестирование (опционально)
- **Git** — система контроля версий

## Документация

### Генерация документации

```bash
cd docs
pip install -r requirements.txt
python generate_docs.py
```

Документация будет сгенерирована в папке `docs/_build/html/`.

Откройте `docs/_build/html/index.html` в браузере для просмотра.

### Структура документации

- **Обзор проекта** — общая информация и архитектура
- **Backend** — документация серверной части
  - Модели данных
  - Репозитории
  - Сервисы
  - API
- **Frontend** — документация клиентской части
  - Экраны
  - Контроллеры
  - Сервисы
- **API Reference** — полная документация REST API
  - Endpoints
  - Pydantic схемы
  - Примеры запросов

## Лицензия

Этот проект распространяется под лицензией MIT. См. файл [LICENSE](LICENSE) для подробностей.

```
MIT License

Copyright (c) 2026 [Ваше имя]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## Авторы

- **@paveltretev-creator** — начальная разработка