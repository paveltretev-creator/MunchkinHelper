from fastapi import FastAPI
from api.routers import users, characters

app = FastAPI(title="Beta App API", version="0.1.0")

app.include_router(users.router)
app.include_router(characters.router)


@app.get("/health")
def health():
    return {"status": "ok"}


# Запуск: uvicorn api_main:app --reload --port 8000