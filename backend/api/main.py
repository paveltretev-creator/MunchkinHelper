"""
Главный файл API - точка входа FastAPI
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import auth, bestiary, races, classes, dungeons, game

app = FastAPI(
    title="Munchkin Helper API",
    description="API для приложения Munchkin Helper",
    version="1.0.0"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене указать конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(auth.router)
app.include_router(bestiary.router)
app.include_router(races.router)
app.include_router(classes.router)
app.include_router(dungeons.router)
app.include_router(game.router)


@app.get("/")
def root():
    """Корневой endpoint"""
    return {
        "message": "Munchkin Helper API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    """Проверка работоспособности API"""
    return {"status": "ok"}