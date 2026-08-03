from pydantic import BaseModel

from app.schemas.planning_result import PlanningResult


class PublishRequest(BaseModel):

    planning: PlanningResult