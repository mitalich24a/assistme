from fastapi import FastAPI

from app.api.v1.router import router
from app.config.settings import settings
from app.core.logger import setup_logger

logger = setup_logger()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(router, prefix="/api/v1")


@app.get("/")
async def root():
    return {
        "message": "Welcome to AssistMe 🚀"
    }