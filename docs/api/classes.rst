Классы
======

Endpoints для работы с классами персонажей.

GET /classes/
-------------

Получить список всех классов.

**Response:**

.. code-block:: json

   [
     {
       "id_class": 1,
       "name": "string",
       "ability_1": "string",
       "ability_2": "string",
       "epic_ability_1": "string",
       "epic_ability_2": "string"
     }
   ]

GET /classes/{class_id}
-----------------------

Получить класс по ID.

**Path Parameters:**

- ``class_id`` (integer) — ID класса

**Response:**

.. code-block:: json

   {
     "id_class": 1,
     "name": "string",
     "ability_1": "string",
     "ability_2": "string",
     "epic_ability_1": "string",
     "epic_ability_2": "string"
   }

POST /classes/
--------------

Создать новый класс. Требует авторизации.

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
     "id_class": 1,
     "name": "string",
     "ability_1": "string",
     "ability_2": "string",
     "epic_ability_1": "string",
     "epic_ability_2": "string"
   }

PUT /classes/{class_id}
-----------------------

Обновить класс. Требует авторизации.

**Path Parameters:**

- ``class_id`` (integer) — ID класса

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
     "id_class": 1,
     "name": "string",
     "ability_1": "string",
     "ability_2": "string",
     "epic_ability_1": "string",
     "epic_ability_2": "string"
   }

DELETE /classes/{class_id}
--------------------------

Удалить класс. Требует авторизации.

**Path Parameters:**

- ``class_id`` (integer) — ID класса

**Response:**

.. code-block:: json

   {
     "message": "string"
   }