from fastapi import APIRouter

from app.schemas.sprint_planning_request import SprintPlanningRequest

router = APIRouter()


@router.post("/workflows/sprint-planning")
async def sprint_planning(
    request: SprintPlanningRequest,
):
    return {
        "message": "Received",
        "design_text": request.design_text,
    }