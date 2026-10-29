Игровые данные
==============

Endpoints для работы с игровым состоянием.

GET /game/state
---------------

Получить текущее игровое состояние. Требует авторизации.

**Response:**

.. code-block:: json

   {
     "level": 1,
     "strength": 0,
     "debuff": 0,
     "total": 1
   }

POST /game/state
----------------

Обновить игровое состояние. Требует авторизации.

**Request Body:**

.. code-block:: json

   {
     "level": 1,
     "strength": 0,
     "debuff": 0
   }

**Response:**

.. code-block:: json

   {
     "level": 1,
     "strength": 0,
     "debuff": 0,
     "total": 1
   }

DELETE /game/state
------------------

Очистить игровое состояние. Требует авторизации.

**Response:**

.. code-block:: json

   {
     "message": "Игровое состояние очищено"
   }