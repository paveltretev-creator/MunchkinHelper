class AppException(Exception):
    """Базовое исключение с HTTP-кодом."""
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
        super().__init__(detail)


class NotFoundException(AppException):
    """404 — сущность не найдена."""
    def __init__(self, detail: str = "Сущность не найдена"):
        super().__init__(404, detail)


class ConflictException(AppException):
    """409 — недопустимый переход / конфликт."""
    def __init__(self, detail: str = "Недопустимая операция"):
        super().__init__(409, detail)