from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Конфигурация приложения"""
    
    # Настройки базы данных
    DB_HOST: str = Field(default="localhost", alias="DB_HOST")
    DB_PORT: int = Field(default=4267, alias="DB_PORT")
    DB_NAME: str = Field(default="simpledb", alias="DB_NAME")
    DB_USER: str = Field(default="postgres", alias="DB_USER")
    DB_PASSWORD: str = Field(default="", alias="DB_PASSWORD")
    
    @property
    def database_url(self) -> str:
        """Формирование URL для подключения к БД"""
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()