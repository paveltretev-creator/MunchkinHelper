Расы
====

Endpoints для работы с расами.

GET /races/
-----------

Получить список всех рас.

**Response:**

.. code-block:: json

   [
     {
       "id_race": 1,
       "name": "string",
       "ability_1": "string",
       "ability_2": "string",
       "epic_ability_1": "string",
       "epic_ability_2": "string"
     }
   ]

GET /races/{race_id}
--------------------

Получить расу по ID.

**Path Parameters:**

- ``race_id`` (integer) — ID расы

**Response:**

.. code-block:: json

   {
     "id_race": 1,
     "name": "string",
     "ability_1": "string",
     "ability_2": "string",
     "epic_ability_1": "string",
     "epic_ability_2": "string"
   }

POST /races/
------------

Создать новую расу. Требует авторизации.

**Request Body:**

.. code-block:: json

   {
     "name": "string",
     "ability_1": "string",
     "ability_2": "string",
     "epic_ability_1": "string",
     "epic_ability_2": "string"
   }

**Response:**

.. code-block:: json

   {
     "id_race": 1,
     "name": "string",
     "ability_1": "string",
     "ability_2": "string",
     "epic_ability_1": "string",
     "epic_ability_2": "string"
   }

PUT /races/{race_id}
--------------------

Обновить расу. Требует авторизации.

**Path Parameters:**

- ``race_id`` (integer) — ID расы

**Request Body:**

.. code-block:: json

   {
     "name": "string",
     "ability_1": "string",
     "ability_2": "string",
     "epic_ability_1": "string",
     "epic_ability_2": "string"
   }

**Response:**

.. code-block:: json

   {
     "id_race": 1,
     "name": "string",
     "ability_1": "string",
     "ability_2": "string",
     "epic_ability_1": "string",
     "epic_ability_2": "string"
   }

DELETE /races/{race_id}
-----------------------

Удалить расу. Требует авторизации.

**Path Parameters:**

- ``race_id`` (integer) — ID расы

**Response:**

.. code-block:: json

   {
     "message": "string"
   }