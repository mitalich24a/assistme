from fastapi import APIRouter

from app.api.v1.workflows import router as workflow_router
from app.api.v1.mcp import router as mcp_router

router = APIRouter()

router.include_router(
    workflow_router,
)

router.include_router(
    mcp_router,
)