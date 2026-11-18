# main.py
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.routers import main_router
from core.config import settings


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
)


app.include_router(main_router)

app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)