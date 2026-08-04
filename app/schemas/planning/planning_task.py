from pydantic import BaseModel, Field


class PlanningTask(BaseModel):

    name: str

    description: str

    story_points: int | None = None

    depends_on: list[str] = Field(default_factory=list)