from pydantic import BaseModel, Field


class ToolCall(BaseModel):
    """
    Tool requested by an LLM.
    """

    name: str

    arguments: dict = Field(
        default_factory=dict,
    )