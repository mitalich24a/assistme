from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.api.v1.workflows import router as workflow_router

router = APIRouter()

router.include_router(health_router, tags=["Health"])
router.include_router(
    workflow_router,
    tags=["Workflows"],
)