Frontend
========

Клиентское приложение на Kivy с трёхуровневой архитектурой.

.. toctree::
   :maxdepth: 2
   :caption: Модули фронтенда:

   screens
   controllers
   services

Архитектура
-----------

Frontend разделён на три уровня:

**Screens** — представление (View). Отвечают за отображение UI и обработку пользовательских событий.

**Controllers** — логика (Presenter). Содержат бизнес-логику и координируют работу между Screens и Services.

**Services** — данные (Model). Работают с локальным хранилищем и внешними API.

Главное приложение
------------------

.. automodule:: main
   :members:
   :undoc-members:
   :show-inheritance: