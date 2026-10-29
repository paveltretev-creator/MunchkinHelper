API Reference
=============

Полная документация REST API.

.. toctree::
   :maxdepth: 2
   :caption: Endpoints:

   auth
   bestiary
   races
   classes
   dungeons
   game

Обзор
-----

API предоставляет RESTful интерфейс для работы с приложением. Все endpoints документированы с примерами запросов и ответов.

Базовый URL
-----------

.. code-block:: text

   http://localhost:8000

Аутентификация
--------------

Для защищённых endpoints используется Bearer токен:

.. code-block:: http

   Authorization: Bearer <login_пользователя>

Формат ответов
--------------

Все ответы возвращаются в формате JSON.

Пример успешного ответа:

.. code-block:: json

   {
     "success": true,
     "message": "Операция выполнена успешно",
     "data": {}
   }

Пример ошибки:

.. code-block:: json

   {
     "detail": "Описание ошибки"
   }