"""
Модуль безопасности: хэширование и проверка паролей.
Используется PBKDF2-HMAC-SHA256 из стандартной библиотеки (без внешних зависимостей).
Формат хранимого хэша: pbkdf2_sha256$<iterations>$<salt_base64>$<hash_base64>
"""
import base64
import hashlib
import hmac
import os

ALGORITHM = "sha256"
ITERATIONS = 200_000
SALT_BYTES = 16


def hash_password(password: str) -> str:
    """Создать хэш пароля с уникальной солью"""
    salt = os.urandom(SALT_BYTES)
    digest = hashlib.pbkdf2_hmac(
        ALGORITHM, password.encode("utf-8"), salt, ITERATIONS
    )
    return (
        f"pbkdf2_{ALGORITHM}"
        f"${ITERATIONS}"
        f"${base64.b64encode(salt).decode('ascii')}"
        f"${base64.b64encode(digest).decode('ascii')}"
    )


def verify_password(password: str, stored_hash: str) -> bool:
    """Проверить пароль против сохраненного хэша"""
    try:
        prefix, iterations_str, salt_b64, hash_b64 = stored_hash.split("$")
        if not prefix.startswith("pbkdf2_"):
            return False
        iterations = int(iterations_str)
        salt = base64.b64decode(salt_b64)
        expected = base64.b64decode(hash_b64)
    except (ValueError, TypeError):
        return False
    
    actual = hashlib.pbkdf2_hmac(
        ALGORITHM, password.encode("utf-8"), salt, iterations
    )
    # compare_digest защищает от атак по времени
    return hmac.compare_digest(actual, expected)