from pydantic import BaseModel, Field


class Checkpoint(BaseModel):
    """
    Represents the current execution state
    of a workflow.
    """

    workflow_id: str

    current_step: int = 0

    completed_steps: list[str] = Field(
        default_factory=list,
    )

    status: str = "RUNNING"