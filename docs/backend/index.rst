Backend
=======

Серверная часть приложения на FastAPI и SQLAlchemy.

.. toctree::
   :maxdepth: 2
   :caption: Модули бэкенда:

   models
   repositories
   services
   api

Структура
---------

Backend организован по принципу слоёной архитектуры:

- **Models** — модели данных SQLAlchemy
- **Repositories** — слой доступа к данным
- **Services** — бизнес-логика
- **API** — REST endpoints

Конфигурация
------------

Настройки подключения к базе данных находятся в ``app/config.py``.

Пример конфигурации:

.. code-block:: python

   DATABASE_URL = "postgresql://user:password@localhost:5432/munchkin"