from pydantic import BaseModel, Field


class PlanningTask(BaseModel):

    name: str = Field(...)

    description: str = Field(...)

    story_points: int | None = Field(
        default=None,
        ge=1,
        le=8,
    )

    depends_on: list[str] = Field(default_factory=list)