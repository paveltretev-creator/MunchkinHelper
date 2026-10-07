from services.user_service import UserService

# Простой singleton-сервис для роутов
_user_service = None


def get_user_service() -> UserService:
    global _user_service
    if _user_service is None:
        _user_service = UserService()
    return _user_service