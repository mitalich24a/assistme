from fastapi import APIRouter

from app.api.v1.agent import router as agent_router


router = APIRouter()

router.include_router(
    agent_router,
)