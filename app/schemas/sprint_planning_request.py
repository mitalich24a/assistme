from pydantic import BaseModel


class SprintPlanningRequest(BaseModel):
    design_text: str