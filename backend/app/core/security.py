"""
Модуль безопасности: хеширование и проверка паролей.
PBKDF2-SHA256 с солью, без внешних зависимостей.
При необходимости позже можно заменить на bcrypt — сервисный слой не изменится.
"""
import binascii
import hashlib
import hmac
import os

HASH_ALGORITHM = "sha256"
HASH_ITERATIONS = 100_000   # количество итераций PBKDF2
SALT_BYTES = 16             # длина соли в байтах


def hash_password(password: str) -> str:
    """Создать хеш пароля с случайной солью. Формат: 'salt_hex:hash_hex'"""
    salt = os.urandom(SALT_BYTES)
    pwd_hash = hashlib.pbkdf2_hmac(
        HASH_ALGORITHM, password.encode("utf-8"), salt, HASH_ITERATIONS
    )
    salt_hex = binascii.hexlify(salt).decode("utf-8")
    hash_hex = binascii.hexlify(pwd_hash).decode("utf-8")
    return f"{salt_hex}:{hash_hex}"


def verify_password(password: str, stored_hash: str) -> bool:
    """Проверить пароль против сохраненного хеша"""
    try:
        salt_hex, hash_hex = stored_hash.split(":")
        salt = binascii.unhexlify(salt_hex)
        expected = binascii.unhexlify(hash_hex)
    except (ValueError, binascii.Error):
        return False  # поврежденный формат хеша
    
    actual = hashlib.pbkdf2_hmac(
        HASH_ALGORITHM, password.encode("utf-8"), salt, HASH_ITERATIONS
    )
    # compare_digest защищает от атак по времени
    return hmac.compare_digest(actual, expected)