Авторизация
===========

Endpoints для регистрации и авторизации пользователей.

POST /auth/login
----------------

Авторизация пользователя.

**Request Body:**

.. code-block:: json

   {
     "login": "string",
     "password": "string"
   }

**Response:**

.. code-block:: json

   {
     "success": true,
     "message": "string",
     "user_id": 1,
     "login": "string"
   }

POST /auth/register
-------------------

Регистрация нового пользователя.

**Request Body:**

.. code-block:: json

   {
     "login": "string (3-50 символов)",
     "password": "string (минимум 6 символов)",
     "password_confirm": "string"
   }

**Response:**

.. code-block:: json

   {
     "success": true,
     "message": "string",
     "user_id": 1
   }