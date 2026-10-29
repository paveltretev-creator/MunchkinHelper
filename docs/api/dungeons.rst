Подземелья
==========

Endpoints для работы с подземельями.

GET /dungeons/
--------------

Получить список всех подземелий.

**Response:**

.. code-block:: json

   [
     {
       "id_dungeon": 1,
       "name": "string",
       "description": "string"
     }
   ]

GET /dungeons/{dungeon_id}
--------------------------

Получить подземелье по ID.

**Path Parameters:**

- ``dungeon_id`` (integer) — ID подземелья

**Response:**

.. code-block:: json

   {
     "id_dungeon": 1,
     "name": "string",
     "description": "string"
   }

POST /dungeons/
---------------

Создать новое подземелье. Требует авторизации.

**Request Body:**

.. code-block:: json

   {
     "name": "string",
     "description": "string"
   }

**Response:**

.. code-block:: json

   {
     "id_dungeon": 1,
     "name": "string",
     "description": "string"
   }

PUT /dungeons/{dungeon_id}
--------------------------

Обновить подземелье. Требует авторизации.

**Path Parameters:**

- ``dungeon_id`` (integer) — ID подземелья

**Request Body:**

.. code-block:: json

   {
     "name": "string",
     "description": "string"
   }

**Response:**

.. code-block:: json

   {
     "id_dungeon": 1,
     "name": "string",
     "description": "string"
   }

DELETE /dungeons/{dungeon_id}
-----------------------------

Удалить подземелье. Требует авторизации.

**Path Parameters:**

- ``dungeon_id`` (integer) — ID подземелья

**Response:**

.. code-block:: json

   {
     "message": "string"
   }