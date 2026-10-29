Бестиарий
=========

Endpoints для работы с монстрами.

GET /bestiary/
--------------

Получить список всех монстров.

**Query Parameters:**

- ``monster_type`` (optional) — фильтр по типу: normal, undead, dragon

**Response:**

.. code-block:: json

   [
     {
       "id_bestiary": 1,
       "name": "string",
       "level": 1,
       "monster_type": "string",
       "description": "string",
       "quirk": "string",
       "xp_reward": 1,
       "treasure_reward": 1
     }
   ]

GET /bestiary/{monster_id}
--------------------------

Получить монстра по ID.

**Path Parameters:**

- ``monster_id`` (integer) — ID монстра

**Response:**

.. code-block:: json

   {
     "id_bestiary": 1,
     "name": "string",
     "level": 1,
     "monster_type": "string",
     "description": "string",
     "quirk": "string",
     "xp_reward": 1,
     "treasure_reward": 1
   }

POST /bestiary/
---------------

Создать нового монстра. Требует авторизации.

**Request Body:**

.. code-block:: json

   {
     "name": "string",
     "level": 1,
     "monster_type": "normal|undead|dragon",
     "description": "string",
     "quirk": "string",
     "xp_reward": 1,
     "treasure_reward": 1
   }

**Response:**

.. code-block:: json

   {
     "id_bestiary": 1,
     "name": "string",
     "level": 1,
     "monster_type": "string",
     "description": "string",
     "quirk": "string",
     "xp_reward": 1,
     "treasure_reward": 1
   }

PUT /bestiary/{monster_id}
--------------------------

Обновить монстра. Требует авторизации.

**Path Parameters:**

- ``monster_id`` (integer) — ID монстра

**Request Body:**

.. code-block:: json

   {
     "name": "string",
     "level": 1,
     "monster_type": "normal|undead|dragon",
     "description": "string",
     "quirk": "string",
     "xp_reward": 1,
     "treasure_reward": 1
   }

**Response:**

.. code-block:: json

   {
     "id_bestiary": 1,
     "name": "string",
     "level": 1,
     "monster_type": "string",
     "description": "string",
     "quirk": "string",
     "xp_reward": 1,
     "treasure_reward": 1
   }

DELETE /bestiary/{monster_id}
-----------------------------

Удалить монстра. Требует авторизации.

**Path Parameters:**

- ``monster_id`` (integer) — ID монстра

**Response:**

.. code-block:: json

   {
     "message": "string"
   }