from pydantic import BaseModel, Field

from app.schemas.planning_task import PlanningTask


class PlanningResult(BaseModel):
    tasks: list[PlanningTask] = Field(default_factory=list)